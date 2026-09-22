#!/usr/bin/env python3
"""Build the verified-only GEDCOM from the working file.

Seed rule (Kit's order 2026-09-21, N-21): include an individual ONLY if the
applied ledger (applied/ledger.md) contains a verified finding about them.
Every included person gets a VERIFIED NOTE stating exactly what was verified.
Family records are included only when all linked members are included AND the
link itself was part of a verified finding. Pointers to non-included records
are dropped and listed in a NOTE (no dangling references, ever).

Original IDs (@I...@/@F...@/@S...@) are kept so the verified file
cross-references cleanly with the working file and the ledger.
"""
import re, textwrap, os

SRC = os.path.expanduser("~/workspace/genealogy/tree/1 Timothy 1_4.ged")
OUTDIR = os.path.expanduser("~/workspace/genealogy/verified")
OUT = os.path.join(OUTDIR, "1 Timothy 1_4 - verified.ged")
BUILD_DATE = "21 SEP 2026"

# (individual id, short label, verified-claim note)
VERIFIED_PEOPLE = [
    ("@I232109150478@", "Rollo",
     "Single identity confirmed - 3 duplicate Rollo records merged. "
     "Parents Ragnvald Mørejarl and Hild (Store Norske Leksikon). "
     "Marriage to Poppa of Bayeux; MARR 889 Rouen preserved on @F856@. "
     "Evidence: en.wikipedia.org/wiki/Rollo + Store Norske Leksikon + eo/ro Wikipedia. "
     "See applied/ledger.md 20260921-0015."),
    ("@I232109150080@", "Poppa of Bayeux",
     "Single identity confirmed - duplicates merged (incl. Poppa#3 with name/birth/death/burial "
     "variants b.872 Caen, d.11 Aug 930, bur. Rouen). Parentage genuinely disputed "
     "(Settipani vs Keats-Rohan) - both FAMC links kept, dispute mapped. "
     "Evidence: en.wikipedia.org/wiki/Poppa_of_Bayeux. "
     "See applied/ledger.md 20260921-0009, 20260921-0015."),
    ("@I232112689282@", "Gerloc",
     "Single identity confirmed - duplicate Gerloc#2 merged (christening/death/burial variants kept). "
     "Evidence: en.wikipedia.org/wiki/Gerloc + encyclopedia.com (Gale). "
     "See applied/ledger.md 20260921-0015."),
    ("@I232109150078@", "Gisela of France",
     "Record carries Wikipedia source; existence as Rollo's wife is DEBATED and she "
     "certainly had no son (per William of Jumieges note on @F857@). "
     "Evidence: en.wikipedia.org/wiki/Gisela_of_France. "
     "See applied/ledger.md 20260921-0015, 20260921-0019."),
    ("@I232109150075@", "Grimaldus",
     "Verified NOT the son of Rollo - FAMC link detached as anachronistic: the Grimaldi "
     "family was founded c.1160, there was no Prince of Monaco in the 920s. "
     "Evidence: en.wikipedia.org/wiki/House_of_Grimaldi. "
     "See applied/ledger.md 20260921-0015."),
    ("@I232119049329@", "Guillaume IV",
     "True parents verified as William III + Gerloc - moved FAMC @F12566@ -> @F2954@; "
     "fragment family @F12566@ deleted. (William III himself not yet verified.) "
     "See applied/ledger.md 20260921-0015."),
    ("@I232111374228@", "Pepin of Italy",
     "Birth 12 Apr 0777 confirmed; conflicting '12 April 773' block removed as erroneous. "
     "Evidence: en.wikipedia.org/wiki/Pepin_of_Italy. "
     "See applied/ledger.md 20260921-0005, 20260921-0019."),
    ("@I232109202891@", "Plectrude",
     "Verified NOT married to Pepin I of Vermandois (b.~817) - false marriage @F8457@ "
     "removed (anachronism: she d.714). Correct marriage @F8456@ to Pepin of Herstal kept. "
     "Evidence: en.wikipedia.org/wiki/Plectrude. "
     "See applied/ledger.md 20260921-0005, 20260921-0019."),
    ("@I232222925741@", "Pepin of Senlis",
     "False second parent link @F5070@ removed; parentage @F13191@ (Pepin I of Vermandois) kept. "
     "(Exact Pepin I vs II article match still uncertain - queued as a check, not guessed.) "
     "See applied/ledger.md 20260921-0005."),
    ("@I232113353174@", "Rothold de Senlis",
     "Self-spouse import artifact resolved: the WIFE-side stub @I232113353175@ (identical "
     "name, no dates/parents/families) was the same person - merged in and retired; "
     "wife of Rothold is unknown. "
     "See applied/ledger.md 20260921-0100."),
    ("@I232109150082@", "Beatrix de Vermandois (ABT 850)",
     "Verified NOT the same person as Beatrice/Beatrix DE VERMANDOIS @I232111442589@ "
     "(b.0870/0880): a merge would make Heribert I (b.850) a father at age 0 and conflate "
     "two husbands (@F855@ vs @F61@) across generations. Likely aunt-niece generation. "
     "See applied/ledger.md 20260921-0156."),
    ("@I232111442589@", "Beatrice/Beatrix DE VERMANDOIS (0870/0880)",
     "Verified NOT the same person as Beatrix /de Vermandois/ @I232109150082@ (ABT 850): "
     "a merge would make her father Heribert I (b.850) a father at age 0. Daughter of "
     "Heribert I, wife of Robert I King of the Franks. "
     "See applied/ledger.md 20260921-0156."),
    ("@I232119069854@", "Rothaide de Bobbio",
     "Single identity confirmed - dateless stub Rothaid /DeBobbio/ @I232111738323@ merged in "
     "(distinct-person reading impossible: stub's child Hubert I d.943 cannot also be her "
     "father). False parent link @F989@ detached (Hubert I + Bertha Senlis, both d.943, "
     "cannot parent a woman b.812/820) - parentage now unknown. False child link @F12190@ "
     "detached (Adele b.783 predates mother). Caveat: @F12192@ mother-link rests on the "
     "merged import stub; Pepin II paternity of Hubert I not established. "
     "See applied/ledger.md 20260921-0300."),
    ("@I232113120927@", "Bernard of Senlis",
     "'Bernard I (or II) of Senlis' is ONE figure - the tree's two unlinked records merged. "
     "Father disputed: Pepin (876-922) or Bernard (c.875-927) - both theories kept and mapped. "
     "Sprota's father link KEPT as incertain (fr.wikipedia.org/wiki/Sprota abandons the "
     "19th-c. Herbert-comte-de-Senlis thesis; incertain != false). "
     "Evidence: en.wikipedia.org/wiki/Bernard_of_Senlis + de.wikipedia.org/wiki/Grafschaft_Senlis "
     "+ it.wikipedia.org/wiki/Bernardo_di_Senlis. "
     "See applied/ledger.md 20260921-0555."),
    ("@I232117457203@", "Farahild de Neustria",
     "Kit's mark (indicate-only, N-14): the Jesus-Christ line likely becomes fraudulent here - "
     "276-year gap to daughter Amalberga (b.640) on the tree's own dates. Lineage unaltered. "
     "See applied/ledger.md 20260921-0025."),
    ("@I232117457190@", "Amalberga of Maubeuge",
     "Kit's mark (indicate-only, N-14): last chronologically coherent generation of the "
     "Jesus-Christ line before the Farahild graft. Lineage unaltered. "
     "See applied/ledger.md 20260921-0025."),
    ("@I232117401241@", "Hugues le Grand",
     "Kit's mark (indicate-only, N-14): 188-year conflation flag - Hugh the Great (897-956) "
     "merged in place of Hugh I of Vermandois (~1057-1101) above Isabel of Vermandois (b.1085). "
     "Lineage unaltered. See applied/ledger.md 20260921-0025."),
    ("@I232118273739@", "Bathath Farssaidh 'Boath Ben Magog'",
     "Kit's mark (indicate-only, N-15): St. Patrick's-era fabrication of the Irish pedigree "
     "probably begins here - 450-year gap from Fenius (Abt 2050 BC) and inverted link to "
     "Magog (2342 BC). Exists only to join the Milesian line to the Bible. Lineage unaltered. "
     "See applied/ledger.md 20260921-0028."),
    ("@I232118273735@", "Fenius Farsaidh",
     "Kit's mark (indicate-only, N-15): last figure of the Irish legendary line; "
     "biblical histories above preserved unmarked. Lineage unaltered. "
     "See applied/ledger.md 20260921-0028."),
    ("@I232109821245@", "Alcaeus 'Heracles'",
     "Kit's mark (indicate-only, N-16): 'son of Zeus' (@F13740@, under Cronus/Rhea) is the "
     "likely fabrication - mythology entered as genealogy. Lineage unaltered. "
     "See applied/ledger.md 20260921-0030."),
    ("@I232109201303@", "Sceaf",
     "Kit's mark (indicate-only, N-16): the basket-baby (shield cradle, adrift) is a foundling "
     "by legend, so 'ben Magi Japheth' parentage is the likely fabrication. Lineage unaltered. "
     "See applied/ledger.md 20260921-0030."),
    ("@I232109201491@", "Dardanus",
     "Kit's mark (indicate-only, N-16): where the Thor line becomes mythology - 'ben Zerah' "
     "(biblical) with second parent Electra daughter of Agamemnon (Greek myth). Below him "
     "biblical history preserved. Lineage unaltered. See applied/ledger.md 20260921-0030."),
    ("@I232112766195@", "Ogive of Luxembourg",
     "Identity verified as Ogive of Luxembourg - daughter of Frederick of Luxembourg "
     "(Count of Moselgau) and Irmentrude of Wetterau (Countess of Gleiberg); first wife "
     "of Baldwin IV of Flanders (m. 1012); mother of Baldwin V of Flanders. Birth c.986 "
     "(tree: 4 septembre 0986 / Abt 984); death 21 Feb 1030 per sources - tree's 21 "
     "November 1030 kept verbatim (N-5), month discrepancy noted; burial St Peter's "
     "Abbey, Ghent. Evidence: en.wikipedia.org/wiki/Baldwin_IV_of_Flanders + "
     "nl.wikipedia.org/wiki/Otgiva_van_Luxemburg. See applied/ledger.md 20260921-0655."),
    # --- Hand-added after the seed (2026-09-21 runs 0655-1055). NOTE: a re-run of this
    # builder currently FAILS LOUDLY on these entries' @S900000009@..@S900000013@
    # WIKIPEDIA sources (minted by hand in the verified file; the reference file is
    # read-only and was never given them). That loud failure is intentional - it beats
    # silently dropping verified people. Queued fix: teach the builder to mint
    # WIKIPEDIA sources on the fly (N-13). Do NOT re-run until that is done.
    ("@I232116859310@", "Bello of Carcassonne",
     "Identity verified as Bello (Belló) of Carcassonne, count of Carcassonne from 790 "
     "until his death (tree dates 755-812 within the scholarly range c.755-c.810/812); "
     "founder of the Bellonid dynasty of Carcassonne and Razès. "
     "Evidence: en.wikipedia.org/wiki/Bello_of_Carcassonne + "
     "ca.wikipedia.org/wiki/Bel·lónides-ca source. See applied/ledger.md 20260921-0755."),
    ("@I232116458499@", "Cunegonde of Gellone (William's wife)",
     "Cunegonde (Kunigunde), first wife of William of Gellone (Guillaume de Gellone) and "
     "mother of Bernard of Septimania (b.~795, d.14 Feb 844 Toulouse). William's will of "
     "28 Jan 804 names his wives Cunegonde and Witburgis and his son Barnard "
     "(en.wikipedia.org/wiki/William_of_Gellone); "
     "fr.wikipedia.org/wiki/Guillaume_de_Gellone confirms the marriage to Cunegonde de "
     "Spolete c.775. Tree dates kept verbatim (N-5). See applied/ledger.md 20260921-0855."),
    ("@I232116475925@", "Kunigunde (Nimilde) of Ampurias",
     "Nimilde (Nimilda) of Ampurias, wife of Bello of Carcassonne (verified 2026-09-21, "
     "@I232116859310@). fr.wikipedia.org/wiki/Bello_de_Carcassonne infobox lists Bello's "
     "spouse as 'Nimilde'; en.wikipedia.org/wiki/Bello_of_Carcassonne says Bello married "
     "'Ermentrude de Ampurias'; ca.wikipedia.org/wiki/Bel%C2%B7l%C3%B3_de_Carcassona says "
     "he married Nimilda in 805. Tree dates kept verbatim (N-5). "
     "See applied/ledger.md 20260921-0955."),
    ("@I232222925748@", "Cunégonde de Gellone (queen of Italy)",
     "Cunégonde de Gellone (also called Cunégonde de Laon), wife of Bernard of Italy "
     "(Bernard d'Italie) from 813 and mother of Pepin of Vermandois; queen consort of "
     "Italy. NOT a duplicate of William of Gellone's wife Cunegonde @I232116458499@: the "
     "literature treats them as two distinct figures (ca.wiki: the younger may have been "
     "named for William's wife - i.e. a different person). Evidence: "
     "fr.wikipedia.org/wiki/Cunégonde_de_Gellone + ca.wikipedia.org/wiki/Cunegunda_d'Austràsia. "
     "Tree dates kept verbatim (N-5): DEAT 15 Jun (no year) matches the ca.wiki 15-Jun-835 "
     "tradition; BIRT place Vermondois unconfirmed (origins unknown). "
     "See applied/ledger.md 20260921-1055."),
    ("@I232118925443@", "Cunigunda of France (Wigeric's wife)",
     "Cunigunda of France (also styled Cunigunda of Sulichgau), b.893-d.924: daughter of "
     "Ermentrude of France and granddaughter of Louis the Stammerer (Louis II of France); "
     "wife of Wigeric of Lotharingia (count palatine of Lotharingia, founder of the House "
     "of Ardenne), married 909 by arrangement of Charles III; mother of Frederick I of "
     "Upper Lorraine, Adalberon I of Metz, Gilbert, Sigebert, Gozlin of Bidgau, Siegfried "
     "of Luxembourg, and Liutgarde; remarried c.922 to Ricwin of Verdun (d.923). "
     "Evidence: en.wikipedia.org/wiki/Cunigunda_of_France (Nash 2017, Vanderputten 2018, "
     "Parisse 1981) + fr.wikipedia.org/wiki/Wig%C3%A9ric_de_Bidgau. Tree dates kept "
     "verbatim (N-5); the 'cunégonde DE FRIULI' name variant is unconfirmed in the "
     "literature. See applied/ledger.md 20260921-1155."),
    ("@I232119044168@", "Kunigunde (Hemma) von Önningen (Diessen)",
     "Kunigunde [Kunizza] of Diessen, wife of Friedrich I 'Roch' (probably count of "
     "Diessen); founded monasterium sancti Stephani at Diessen in 1020 after her "
     "husband's death; bur. Diessen St Stefan, d. 6 Mar (after 1020). Evidence: "
     "fmg.ac MedLands BAVARIAN NOBILITY + de.wikipedia.org/wiki/Konradiner "
     "('Kunizza († 1020), Friedrich I.'). Tree dates kept verbatim (N-5); '(Hemma)' "
     "unconfirmed in the literature; parentage (FAMC @F10036@) conjectural in the "
     "literature - excluded; husband Friedrich I /von Wassenburg/ not yet verified - "
     "FAMS @F526@ excluded, queued. See applied/ledger.md 20260921-1355."),
    ("@I232222925747@", "Bernard I of Italy",
     "Bernard I, King of Italy (Bernardo d'Italia; 797 - 17 Aug 818), son of Pepin of "
     "Italy, grandson of Charlemagne; husband of Cunégonde de Gellone (@I232222925748@) "
     "and father of Pepin I of Vermandois. Evidence: en.wikipedia.org/wiki/Bernard_of_Italy "
     "+ fmg.ac MedLands ITALY Kings (797-Milan 17 Aug 818, bur Milan, San Ambrosio; "
     "m ([813]) CUNIGUNDIS) + it.wikipedia.org/wiki/Bernardo_d%27Italia (17 Aug 818, "
     "Sant'Ambrogio). Tree dates kept verbatim (N-5): DEAT '17 Aug', Milan, matches "
     "MedLands exactly; BIRT place Vermandois unconfirmed in the literature. NOTE: "
     "en.wiki gives his death as 17 April 818 - death-date variance in the literature, "
     "kept as in the tree. See applied/ledger.md 20260921-1555."),
]

# Families to include: id -> note about excluded members
INCLUDE_FAM = {
    "@F856@": ("MARR 889 Rouen preserved per ledger 20260921-0015. "
                "Children @I232109173643@, @I232116199622@ excluded - not yet verified; "
                "@I232109150076@ (Crispina) excluded - weak sourcing per ledger."),
    "@F857@": None,
    "@F5073@": ("Marriage attested in the literature (m. ([813]) CUNIGUNDIS per MedLands ITALY "
                "Kings; en.wiki notes marriage year obscure; it.wiki 813). Ledger 20260921-1555."),
}

XREF = re.compile(r"@([^@]+)@")

def parse_records(path):
    records = {}
    order = []
    cur_id, cur_lines = None, []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line.strip():
                continue  # drop blank lines (import artifacts, not valid GEDCOM)
            if line.startswith("0 "):
                if cur_id is not None:
                    records[cur_id] = cur_lines
                    order.append(cur_id)
                m = re.match(r"0 (@[^@]+@) (\w+)", line)
                if m:
                    cur_id, cur_lines = m.group(1), [line]
                else:
                    cur_id, cur_lines = line, [line]  # e.g. "0 TRLR", "0 HEAD"
            else:
                if cur_id is not None:
                    cur_lines.append(line)
    if cur_id is not None:
        records[cur_id] = cur_lines
        order.append(cur_id)
    return records

def wrap_note(lines, text, level=1):
    chunks = textwrap.wrap(text, 100)
    lines.append(f"{level} NOTE {chunks[0]}")
    for c in chunks[1:]:
        lines.append(f"{level+1} CONT {c}")

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    recs = parse_records(SRC)
    indi_ids = {i for (i, _, _) in VERIFIED_PEOPLE}
    notes = {i: n for (i, _, n) in VERIFIED_PEOPLE}

    out_individuals, out_families = [], []
    needed_sources = set()

    for iid in indi_ids:
        if iid not in recs:
            raise SystemExit(f"MISSING individual {iid} in working file")
        src_lines = recs[iid]
        dropped_fams, dropped_obje = [], []
        new_lines = [src_lines[0]]
        for ln in src_lines[1:]:
            m = re.match(r"1 (FAMC|FAMS) (@[^@]+@)", ln)
            if m:
                if m.group(2) in INCLUDE_FAM:
                    new_lines.append(ln)
                else:
                    dropped_fams.append(f"{m.group(1)} {m.group(2)}")
                continue
            m2 = re.match(r"1 OBJE (@[^@]+@)", ln)
            if m2:
                dropped_obje.append(m2.group(1))
                continue
            new_lines.append(ln)
            m3 = re.match(r"1 SOUR (@[^@]+@)", ln)
            if m3:
                needed_sources.add(m3.group(1))
        wrap_note(new_lines, "VERIFIED " + BUILD_DATE + ": " + notes[iid])
        if dropped_fams or dropped_obje:
            parts = []
            if dropped_fams:
                parts.append("family links not yet verified, excluded from this build: "
                             + ", ".join(dropped_fams))
            if dropped_obje:
                parts.append("media objects excluded (Ancestry export carried no files): "
                             + ", ".join(dropped_obje))
            wrap_note(new_lines, "BUILD NOTE " + BUILD_DATE + ": " + "; ".join(parts)
                      + ". See the working file for the unverified data.")
        out_individuals.append(new_lines)

    for fid, fam_note in INCLUDE_FAM.items():
        if fid not in recs:
            raise SystemExit(f"MISSING family {fid} in working file")
        new_lines = [recs[fid][0]]
        dropped = []
        for ln in recs[fid][1:]:
            m = re.match(r"1 (HUSB|WIFE|CHIL) (@[^@]+@)", ln)
            if m:
                if m.group(2) in indi_ids:
                    new_lines.append(ln)
                else:
                    dropped.append(f"{m.group(1)} {m.group(2)}")
                continue
            new_lines.append(ln)
            m3 = re.match(r"1 SOUR (@[^@]+@)", ln)
            if m3:
                needed_sources.add(m3.group(1))
        if fam_note:
            wrap_note(new_lines, "BUILD NOTE " + BUILD_DATE + ": " + fam_note)
        if dropped:
            wrap_note(new_lines, "BUILD NOTE " + BUILD_DATE + ": excluded non-verified members: "
                      + ", ".join(dropped) + ".")
        out_families.append(new_lines)

    out_sources = []
    needed_repos = set()
    for sid in sorted(needed_sources):
        if sid not in recs:
            raise SystemExit(f"MISSING source {sid} in working file")
        for ln in recs[sid]:
            m = re.match(r"1 REPO (@[^@]+@)", ln)
            if m:
                needed_repos.add(m.group(1))
        out_sources.append(recs[sid])
    out_repos = []
    for rid in sorted(needed_repos):
        if rid not in recs:
            raise SystemExit(f"MISSING repo {rid} in working file")
        out_repos.append(recs[rid])

    head = [
        "0 HEAD",
        "1 SOUR Muse verified build",
        "2 NAME 1 Timothy 1:4 - verified tree",
        "2 VERS 2026-09-21",
        "1 DATE " + BUILD_DATE,
        "1 GEDC",
        "2 VERS 5.5.1",
        "2 FORM LINEAGE-LINKED",
        "1 CHAR UTF-8",
    ]
    wrap_note(head,
              "Verified-only build of the '1 Timothy 1:4' tree (Kit Cosby). Seed: every person "
              "carries a VERIFIED NOTE stating exactly what the applied ledger verified as of "
              "2026-09-21. Family links to unverified persons are excluded and listed in NOTEs. "
              "Admission rule: N-21 (NOTATION_LEDGER.md). Reference file (read-only): "
              "~/workspace/genealogy/tree/1 Timothy 1_4.ged. Private working file - never share, "
              "publish, or upload.", level=1)
    head += ["1 SUBM @SUBM1@",
             "0 @SUBM1@ SUBM",
             "1 NAME Kit Cosby"]

    with open(OUT, "w", encoding="utf-8") as f:
        for block in [head] + out_individuals + out_families + out_sources + out_repos:
            for ln in block:
                f.write(ln + "\n")
        f.write("0 TRLR\n")

    # ---- verify the new file ----
    # Structural pointers only: a level-N line whose entire value is one @XREF@.
    # @...@ inside NOTE/CONT prose is explanatory text (N-10 convention), not a pointer.
    STRUCT = re.compile(r"^\d+ (HUSB|WIFE|CHIL|FAMC|FAMS|SOUR|OBJE|NOTE|SUBM|REPO) (@[^@]+@)$")
    vrecs = parse_records(OUT)
    known = set(vrecs.keys()) | {"HEAD", "TRLR"}
    dangling = []
    malformed = 0
    for rid, lines in vrecs.items():
        for ln in lines:
            if not re.match(r"^\d+ ", ln):
                malformed += 1
            m = STRUCT.match(ln)
            if m and m.group(2) not in known:
                dangling.append((rid, ln.strip()))
    n_indi = sum(1 for r in vrecs if r.startswith("@I"))
    n_fam = sum(1 for r in vrecs if r.startswith("@F"))
    n_sour = sum(1 for r in vrecs if r.startswith("@S"))
    print(f"individuals={n_indi} families={n_fam} sources={n_sour} "
          f"malformed={malformed} dangling={len(dangling)}")
    for d in dangling[:10]:
        print("DANGLING:", d)
    if malformed or dangling:
        raise SystemExit("verification failed")
    print("OK:", OUT)

if __name__ == "__main__":
    main()
