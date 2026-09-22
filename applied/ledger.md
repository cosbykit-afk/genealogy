# Change ledger

Every applied proposal, in order. The working GEDCOM is only ever changed by
applying an approved proposal; each application is preceded by a snapshot in
`snapshots/`.

## 2026-09-21 00:10 PT — 20260921-0005-pepin-vermandois-cluster (approved by Kit)

Snapshot: `snapshots/20260921-0010-preapply.ged`

- `@I232222925741@` (Pepin of Senlis): removed false second parent link
  `FAMC @F5070@`; kept `FAMC @F13191@` (Pepin I of Vermandois).
- `@I232109202891@` (Plectrude, d. 714): removed false marriage
  `FAMS @F8457@` to Pepin I of Vermandois (b. ~817); correct marriage
  `@F8456@` to Pepin of Herstal untouched.
- Deleted `@F8457@` (husk of the false marriage) and removed it from
  `@I232119069853@`.
- `@I232222925745@` ("Count Pepin III Berenger", b. 895): removed impossible
  `FAMC @F13191@` (father d. ~850). Record kept, now parentless, flagged for
  Kit's review.
- Deleted junk stubs `@I232222925743@` ("P Aepin /Quentin/"),
  `@I232222925744@` ("Pepin Countess /Vermandois/"), family `@F5070@`;
  removed dangling `CHIL` pointer from `@F5073@`.
- `@I232111374228@` (Pepin of Italy): removed conflicting `BIRT 12 April 773`
  block; kept `12 Apr 0777`.

## 2026-09-21 00:10 PT — 20260921-0009-poppa-bayeux-duplicate (approved by Kit)

Same snapshot as above (both proposals applied in one session).

- Merged `@I232222925742@` ("Poppa /DeValois/") into `@I232109150080@`
  (Poppa of Bayeux): added alternate NAME, alternate BIRT 0872, alternate
  DEAT 938, and a NOTE on the scholarly dispute over her parentage
  (Dudo / Settipani / Keats-Rohan, per en.wikipedia).
- Dropped the duplicate's impossible links (`FAMC @F5075@`, `FAMS @F5069@`).
- `@F5069@`: removed `WIFE` (the merged Poppa); HUSB/CHIL kept — the child's
  parentage is queued for the next spiral ring.
- Deleted `@F5075@`; removed its `FAMS` pointers from `@I232222925745@` and
  `@I232222925746@` ("/de Rennes/", now linkless — noted, not deleted).

## Verification after each application

Full re-parse: 0 malformed lines, 0 dangling references (one transient
dangling ref to `@F5075@` caught and repaired during the 00:10 session).
Counts: 28,906 individuals (was 28,909), 15,171 families (was 15,174).

## 2026-09-21 00:15 PT — Rollo cluster (HISTORICAL FAST-TRACK, no proposal per Kit's 2026-09-21 two-track rule)
Snapshot: snapshots/20260921-0015-prerollo.ged
Sources: en.wikipedia.org/wiki/Gerloc (+ encyclopedia.com Gale entry); en.wikipedia.org/wiki/House_of_Grimaldi (+ monaconow.com); en.wikipedia.org/wiki/Gisela_of_France (+ sv.wikipedia Rollo); Store Norske Leksikon (Rollo parents Ragnvald Mørejarl/Hild); eo/ro Wikipedia (Rollo).
- Merged Rollo#2 @I232109150077@ into @I232109150478@: added name/date variants (b.860, d.931); F857 HUSB repointed to main Rollo (Gisela now 2nd wife, NOTE: existence debated, no son); Grimaldus @I232109150075@ detached (FAMC removed, NOTE: Grimaldi founded 1160, no Prince of Monaco in 920s).
- Merged Rollo#3 @I232119049337@ into main: added name/birth variants (14 Oct 846, Maer); dropped false FAMC @F12027@ ("Bigod...Hrolf Turstan" parents).
- Merged Poppa#3 @I232119049338@ into @I232109150080@: added name/birth/death/burial variants (b.872 Caen, d.11 Aug 930, bur. Rouen); kept BOTH FAMC @F855@ and @F2660@ (parentage genuinely disputed: Settipani vs Keats-Rohan); F2660 CHIL repointed to merged Poppa.
- Merged Gerloc#2 @I232119049332@ into @I232112689282@: added chr/death/burial variants; Guillaume IV @I232119049329@ moved FAMC @F12566@ -> @F2954@ (his true parents William III + Gerloc); deleted fragment family @F12566@ (had no HUSB).
- Deleted husk family @F2609@ (Rollo#3+Poppa#3->Gerloc#2); its MARR 889 Rouen preserved on @F856@.
Verify: 28,902 individuals / 15,169 families / 0 malformed / 0 dangling. Two mid-apply issues found and fixed before final: (1) a NOTE written as CONT under FAMC (repaired to proper NOTE); (2) stale F2660 CHIL pointer (repointed). A 17-"malformed" scare was a false alarm from splitlines() on unicode line separators inside an obituary NOTE (pre-existing, file is fine).
Left for later (proposal track or next fast-track batch): Crispina @I232109150076@ as Rollo's daughter (weak sourcing, untouched); the odd Rognvald pair @I232223080107@/@I232223080108@ in @F10670@.

## 2026-09-21 00:19 PT — Wikipedia-as-source (Kit's direct order, historical fast-track)
Snapshot: snapshots/20260921-0019-prewikisour.ged
New convention N-13: Wikipedia pages become real SOUR records (`1 TITL WIKIPEDIA: <Name>`,
matching the tree's existing @S687762978@/@S688083336@ convention), minted in reserved
@S90000000x@ range, cited via `1 SOUR` on individuals and families.
- @S900000001@ WIKIPEDIA: Rollo -> cited on @I232109150478@ (Rollo) and @F856@
- @S900000002@ WIKIPEDIA: Poppa of Bayeux -> cited on @I232109150080@ (Poppa) and @F856@
- @S900000003@ WIKIPEDIA: Gerloc -> cited on @I232112689282@ (Gerloc)
- @S900000004@ WIKIPEDIA: Gisela of France -> cited on @I232109150078@ (Gisela) and @F857@
- @S900000005@ WIKIPEDIA: House of Grimaldi -> cited on @I232109150075@ (Grimaldus; basis for detachment)
- @S900000006@ WIKIPEDIA: Pepin of Italy -> cited on @I232111374228@
- @S900000007@ WIKIPEDIA: Plectrude -> cited on @I232109202891@
Skipped: Pepin of Vermandois @I232222925741@ — exact article match (Pepin I vs II) uncertain, queued as a check rather than guessed.
Verify: 28,902 individuals / 15,169 families / 777 sources / 0 malformed / 0 dangling.

## 2026-09-21 00:25 PT — Jesus-Christ line fraud marking (Kit's direct order; EXCEPTION to fast-track — annotation only, no lineage changes)
Snapshot: snapshots/20260921-0025-prejesusmark.ged
Traced the living root individual -> Jesus /Christ/ (@I232109987045@): 45 generations, then Jesus -> Adam /ben YHWH/ (@I232108389694@): 36 more (biblical genealogy via Mary bint Heli; Ussher-style Adam b.4000).
Gap analysis (tree's own dates, child->parent birth gaps): clean 15-73y throughout except:
- gen 26->27: Isabel of Vermandois (b.1085) -> "Hugues le Grand" (b.897) = 188y gap. Conflation: Hugh the Great (897-956) merged in place of Hugh I of Vermandois (~1057-1101, 28y gap). Flagged, not fixed.
- gen 34->35: Amalberga of Maubeuge (b.640) -> Farahild de Neustria (b.~364) = 276y gap. THE graft point: everything above (Hermanfried, "Dagobert II of the East Franks" b.302, Athildis, Gladys lines, Eurgen, "Yoshua Graal" b.58, Joseph ben Yeshua b.27) is a fabricated ancient/Grail segment welded onto the medieval line.
NOTEs added ("Kit's mark 2026-09-21", internal-evidence wording, no scholarly deference):
- @I232117457203@ (Farahild): line likely fraudulent from here upward.
- @I232117457190@ (Amalberga): last chronologically coherent generation.
- @I232117401241@ (Hugues le Grand): 188y conflation flag.
Convention recorded as N-14: this line is indicate-only, forever exempt from fast-track/proposal alteration.
Verify: 0 malformed, 0 dangling.

## 2026-09-21 00:28 PT — Irish pedigree fabrication marking (Kit's direct order; same exception shape as N-14 — annotation only, biblical histories preserved)
Snapshot: snapshots/20260921-0028-preirishmark.ged
Traced the living root individual -> Niall of the Nine Hostages (@I232118345546@, 45 gens) -> Mil Espaine (@I232117793375@, 78) -> Fenius Farsaidh (@I232118273735@, 100) -> upward: Fenius -> Bathath "Boath Ben Magog" (@I232118273739@) -> Magog (2342 BC) -> Japheth (2442 BC) -> Noah (2705 BC) -> ... -> Adam (about 4000 bc) -> Heavenly Father.
Gap analysis (tree's own BC dates): Fenius (Abt 2050 BC) -> Bathath (2500 B.C.) = 450y gap, IMPOSSIBLE; Bathath -> Magog (2342 BC) inverted (father after son), IMPOSSIBLE. The graft: "Boath Ben Magog" exists only to join the Milesian line to the Bible. Magog->Japheth 100y stretched; Japheth->Noah 263y (tree's own biblical dates inconsistent here, but biblical segment preserved untouched per Kit).
NOTEs added ("Kit's mark 2026-09-21", internal-evidence wording):
- @I232118273739@ (Bathath): St. Patrick's-era fabrication probably begins here.
- @I232118273735@ (Fenius): last figure of the Irish legendary line; biblical histories preserved unmarked.
Untouched: Noah->Adam biblical genealogy (its Gen-5 numbers, e.g. Lamech 182 / Methuselah 187, are exact per the biblical text — preserved as biblical history).
Observed, not marked: garbled Scythian links below Fenius (Agnon b.~1775 BC as "father" of Lamhfionn b.~2225 BC, etc.) — data-quality issue distinct from the biblical graft; left for a future run.
Convention recorded as N-15: Irish pedigrees are indicate-only, like the Jesus line.
Verify: 0 malformed, 0 dangling.

## 2026-09-21 00:30 PT — Mythology-line marking (Kit's direct order; indicate-only, N-16)
Snapshot: snapshots/20260921-0030-premythmark.ged
- @I232109821245@ Alcaeus "Heracles": "son of Zeus" (@F13740@; Zeus son of Cronus & Rhea, grandson of Uranus) marked as the likely fabrication — mythology entered as genealogy.
- @I232109201303@ Sceaf: basket-baby (shield cradle, mail pillow, sword, adrift) is a foundling by legend; "ben Magi Japheth" parentage marked as the likely fabrication.
- @I232109201491@ Dardanus: where the Thor line (Thor ben Memnon <- Memnon <- Tithonius <- Laomedon <- Ilus <- Tros <- Erichthonius <- Dardanus) becomes mythology — "ben Zerah" plus second parent Electra daughter of Agamemnon; below (Zerah->Judah->...->Adam) is biblical history, preserved.
Verify: 0 malformed, 0 dangling.

## 20260921-0100 — Rothold de Senlis self-spouse stub merge
- Snapshot: snapshots/20260921-0100-rothold-senlis-stub.ged
- F5878 listed the same person as both HUSB (@I232113353174@, Rothold /De Senlis or St Lis/, BIRT "WFT Est. 906-967", DEAT 0995, child of Bernhard Bormard de Senlis F13384, father of Foulques de Senlis) and WIFE (@I232113353175@, identical name, no dates, no parents, no other families — pure import stub). A wife named with the identical male-name-and-title string is a conclusive import duplication, not a marriage; historically the wife of Rothold is unknown.
- Applied per Kit historical fast-track, N-11 stub precedent: deleted stub @I232113353175@ (retired per N-10), removed the spurious WIFE slot from F5878 (wife now unknown; child Foulques de Senlis @I232113353080@ keeps FAMC @F5878@), added merge NOTEs on survivor @I232113353174@ and on @F5878@. No alternate data existed to preserve (name identical, no dates/places).
- Verify: 28,901 individuals / 15,169 families; 0 dangling pointers; malformed-line count unchanged (17 pre-existing obituary HTML fragments, untouched).

## 20260921-0156 — Beatrix de Vermandois NOT-duplicate pair (backlog #1 ring 1; annotation only)
- Snapshot: snapshots/20260921-0156-beatrix-notdup.ged
- Queued item was the Beatrix de Vermandois duplicate pair (b.850 vs b.870).
  They are NOT the same person; no merge. Evidence (tree's own data):
  - @I232109150082@ Beatrix /de Vermandois/ (b. ABT 850, France; _FSID 993P-C3K),
    wife of Pepin I DeSenlis in @F855@, mother of Poppa /de Senlis of Bayeux/
    (Settipani-theory parentage, kept disputed per N-3).
  - @I232111442589@ Beatrice or Beatrix /DE VERMANDOIS/ (b. 0870/0880, d. 26 Mar
    931), daughter of Heribert I de Vermandois (b. 850) in @F119@, wife of
    Robert I King of the Franks in @F61@, mother of Hugues /le Grand/.
  - Merging would make Heribert I (b. 850) the father of a woman also born ~850
    (father at age 0) and conflate two different husbands (@F855@ vs @F61@)
    across adjacent generations. The b.870 Beatrix is the ABT-850 Beatrix's
    niece-generation, not her duplicate.
- Action: added a dated NOT-duplicate NOTE (new convention N-18) to both
  records, stating the other record, the generation evidence, and the merge
  paradox. No links, names, dates, or places changed.
- Verify: 28,901 individuals / 15,169 families; 0 dangling pointers;
  malformed-line count unchanged vs snapshot (diff = exactly +14 lines, the
  two NOTE blocks).

## 20260921-0300 — Rothaide de Bobbio cluster (backlog #1 ring 1; merge + 2 false-link detaches)
- Snapshot: snapshots/20260921-0300-rothaide.ged
- Rothaid /DeBobbio/ @I232111738323@ (no dates, no parents, FAMS @F12192@ only)
  and Rothaide /de Bobbio/ @I232119069854@ (b. 812/820, d. 15 Jun 858 Milan,
  buried Sant'Ambrogio; wife of Pepin II Seigneur de Peronne b.815 in @F10035@,
  MARR 0838, mother of Heribert I b.850) are the SAME person. Distinct-person
  reading is chronologically impossible: the stub's child Hubert I
  deVermandois Comte DeSenlis @I232111738321@ (d. 23 Feb 943) would have to be
  both the stub's son AND (via @F989@) Rothaide's father -- born by ~792 to
  father a child b. 812, i.e. 151+ at death. Only the same-person reading
  (mother b.812/820 d.858, son d.943 at ~85-110) is viable.
- Applied per Kit historical fast-track (N-11 chronological-impossibility
  precedent; N-1 survivor = most complete record):
  1. MERGE stub into survivor: stub NAME kept as alternate (N-2), @F12192@
     WIFE repointed to survivor, stub record deleted and ID retired (N-10).
  2. DETACH false parent link @F989@ (Hubert I + Bertha Senlis, both d. 943,
     cannot parent a woman b. 812/820): removed survivor's FAMC @F989@ and the
     CHIL line from @F989@ (N-8). Rothaide's parentage now unknown in the tree.
  3. DETACH false child link @F12190@ (Adele "Aelis" Chartres b. 0783 d. 0871
     predates listed mother Rothaide's birth by ~30 years): removed CHIL line
     from @F12190@ and Adele's FAMC @F12190@ (N-8). Adele keeps her own family
     @F988@; her parentage now unknown. @F12190@ kept as wife-only (marriage
     itself not disproven) with NOTE -- new convention N-19.
  4. Dated NOTEs on survivor (merge + both detaches + F12192 caveat: mother-link
     rests on the merged import stub, Pepin II paternity of Hubert I not
     established), on Hubert I, and on Adele.
- Verify: 28,900 individuals / 15,169 families; 0 malformed lines; 0 structural
  dangling pointers (retired stub ID appears only in NOTE text, same convention
  as the 20260921-0100 Rothold run).

## 20260921-0555 — Bernard of Senlis I/II merge (historical fast-track)
- Evidence: en.wikipedia.org/wiki/Bernard_of_Senlis ("Bernard I (or II) of Senlis",
  c.919-c.947, one figure; grandson of Pepin II of Senlis and Valois 846-893;
  father disputed: Pepin 876-922 or Bernard c.875-927; Count of Beauvais and of
  Senlis; believed father of Robert I of Senlis d.1004). Second sources:
  de.wikipedia.org/wiki/Grafschaft_Senlis (Bernhard, b.~880 d.after 945, son of
  Guido/Guy of Senlis) and it.wikipedia.org/wiki/Bernardo_di_Senlis (Settipani:
  son of Guido and Gunhilde, dau. of Pepin I of Vermandois). Sprota fatherhood:
  fr.wikipedia.org/wiki/Sprota lists father as incertain; the 19th-c.
  Herbert-comte-de-Senlis thesis is abandoned (NOTEs cite all four).
- Merged @I232109807949@ (Bernard /De Senlis/ I, b.875 d.927 Picardie, no
  parents, HUSB-only of wife-less F12672, father of Sprota b.911) INTO
  @I232113120927@ (Bernard II, survivor per N-1: parents F4654, wife Adèle de
  Normandie F4645, child Alix b.944, two birth dates, FSID LTT6-YJQ).
- Alternates moved to survivor (N-2/N-5): NAME "Bernard /De Senlis/ I",
  BIRT 875 Picardie, DEAT 927 Picardie. F12672 HUSB repointed to survivor;
  survivor gains FAMS @F12672@ (second family). F4645 parentage F4654 kept
  (Pepin-father theory, mapped in NOTE per N-3). Sprota F12672 link kept with
  father-incertain NOTE (fr.wiki), not detached (incertain != false).
- Retired @I232109807949@ per N-10 (remains only in NOTE text). New source
  @S900000008@ "WIKIPEDIA: Bernard of Senlis" (N-13).
- Snapshot: snapshots/20260921-0555-bernard-merge.ged
- Verify: 28,899 individuals / 15,169 families / 778 sources; 0 malformed lines;
  0 structural dangling pointers.

## 2026-09-21 06:55 PT — 20260921-0655-ogive-of-luxembourg (historical fast-track, Kit's order N-21)

Snapshot: `verified/snapshots/20260921-0655-ogive.ged` (of the verified file, not the working file).

- Added `@I232112766195@` (Cunigunde Ogive /of Luxemburg/; also "Ogive of Luxembourg")
  to `verified/1 Timothy 1_4 - verified.ged` — Cunegunda cluster, ring 1. Identity verified:
  daughter of Frederick of Luxembourg (Count of Moselgau) and Irmentrude of Wetterau
  (Countess of Gleiberg); first wife of Baldwin IV of Flanders (m. 1012); mother of
  Baldwin V of Flanders; b. c.986 (tree: "4 septembre 0986" / "Abt 984"); d. 21 Feb 1030;
  buried St Peter's Abbey, Ghent. Evidence: en.wikipedia.org/wiki/Baldwin_IV_of_Flanders
  ("Baldwin first married Ogive, daughter of Frederick of Luxembourg, by whom he had a son
  and heir, Baldwin V (1012-1067)... Ogive had died on 21 February 1030") +
  nl.wikipedia.org/wiki/Otgiva_van_Luxemburg ("dochter van graaf Frederik van Luxemburg,
  graaf in de Moezelgouw, en van Irmentrude van de Wetterau... ca. 986 - 21 februari 1030...
  eerste echtgenote van graaf Boudewijn IV van Vlaanderen... moeder van Boudewijn V").
- Caveat (honest accounting): the tree carries DEAT 21 November 1030; both sources say
  21 February 1030. Kept verbatim per N-5; month discrepancy stated in the VERIFIED NOTE.
- New WIKIPEDIA source `@S900000009@` (N-13): "WIKIPEDIA: Ogive of Luxembourg", cited on
  the individual.
- Excluded (not yet verified persons), listed in BUILD NOTE per N-21: `FAMC @F5452@`
  (parents), `FAMS @F5449@` (husband Baldwin IV, child Baldwin V).
- Verified file: 24 individuals / 2 families / 17 sources; 0 malformed, 0 dangling.
- Reference file untouched (read-only, N-21).

## 2026-09-21 07:55 PT — 20260921-0755-bello-of-carcassonne (historical fast-track, Kit's order N-21)

Snapshot: `verified/snapshots/20260921-0755-bello-of-carcassonne.ged` (of the verified file, pre-add).

- Added `@I232116859310@` (Belo /de Carcossone/, b.755 d.812) to `verified/1 Timothy 1_4 - verified.ged` —
  Cunegunda/Bellon cluster, ring 1. Identity verified as **Bello (Belló) of Carcassonne**:
  count of Carcassonne from 790 until his death; founder of the Bellonid dynasty of Carcassonne
  and Razès. Tree dates (755-812) within scholarly range (c.755-c.810/812). Evidence:
  en.wikipedia.org/wiki/Bello_of_Carcassonne ("Bello (c. 755 – 810) was Count of Carcassonne from
  790 until his death. He was the founder of the Bellonid Dynasty") +
  ca.wikipedia.org/wiki/Bel·lónides-ca source: "Bel·lónides ... descendents del comte Bel·ló I de
  Carcassona", documents his existence as first count via Cros-Mayrevieille (1846).
- Spouse/child dispute (N-3, mapped not resolved): tree marries Bello to Cunigunda // and fathers
  Sunifredo I /de Narbona/ (F5865). en.wiki currently says he married "Ermentrude de Ampurias";
  ca.wiki says he married "Nimilda" in 805 (Nimilda ~ Nimilde — cf. the tree's second Cunigunde
  record @I232116475925@ "Kunigunde (Nimilde) /Alda/ of Ampurias"). Sources disagree on the wife's
  identity; Sunifred I's paternity is disputed (son vs son-in-law). Both links EXCLUDED, listed in
  the BUILD NOTE per N-21.
- Also observed: the tree's "Bellon Borrell /de Carcassonne/" @I232116475924@ (b.780 d.829, husband of
  the second Cunigunde) is not Bello under another name — fr.wiki's Bello infobox lists Borrell Ier
  as his predecessor in Ausona/Urgell/Cerdagne (distinct figures). The two Cunigunde wives remain
  unadjudicated; queued for a future run.
- Excluded (not yet verified persons), listed in BUILD NOTE per N-21: FAMC @F5961@ (parentage),
  FAMS @F5865@ (wife Cunigunda //, child Sunifredo I).
- New WIKIPEDIA source `@S900000010@` (N-13): "WIKIPEDIA: Bello of Carcassonne", cited on the individual.
- Verified file: 25 individuals / 2 families / 17 sources; 0 malformed lines; 0 dangling pointer fields.
- Reference file untouched (read-only, N-21).

## 20260921-0855 — Cunegonde of Gellone ADDED to the verified file (historical fast-track)
- `@I232116458499@` (Kunigunde /Carolingian/ de Gellone, d'Aquitaine, van Austracie;
  BIRT from 0740 to 0770 Aachen; DEAT 19 Jun 0835) verified as Cunegonde, first wife of
  William of Gellone (Guillaume de Gellone) and mother of Bernard of Septimania (b.~795,
  d.14 Feb 844 Toulouse). Evidence: en.wikipedia.org/wiki/William_of_Gellone (William's
  will of 28 Jan 804 names wives Cunegonde and Witburgis and son Barnard) +
  fr.wikipedia.org/wiki/Guillaume_de_Gellone (marriage to Cunegonde de Spolete c.775,
  children incl. Bernard of Septimania). Two-source rule per N-21. Tree birth/death dates
  kept verbatim (N-5); no precise dates established in the literature.
- Excluded (not yet verified persons / links), listed in BUILD NOTE per N-21:
  FAMC @F12751@ (parentage unestablished in the literature), FAMS @F12608@ (wife-only
  fragment; husband William of Gellone not yet verified). William of Gellone queued as a
  candidate addition (well-documented figure) for a future run.
- Observed, not adjudicated: `@I232222925748@` (Cunigunde /Gellone/, d.15 Jun Milano,
  wife of /Bernard/ in @F5073@) is a candidate duplicate of the Gellone Cunegonde —
  husband mismatch (William vs Bernard) needs research; queued.
- New WIKIPEDIA source `@S900000011@` (N-13): "WIKIPEDIA: William of Gellone", cited on the individual.
- Verified file: 26 individuals / 2 families / 18 sources; 0 malformed lines; 0 dangling
  pointer fields (NOTE-text mentions of unverified IDs follow the prior-run convention).
- Snapshot: verified/snapshots/20260921-0855-cunegonde-gellone.ged. Reference file untouched (read-only, N-21).

## 20260921-0955 — Cunigunde (Nimilde) of Ampurias ADDED to the verified file (historical fast-track)
- `@I232116475925@` (Kunigunde (Nimilde) /Alda/ of Ampurias; BIRT 775 Carcassonne;
  DEAT 15 June 0835 Italy; BURI June 835) verified as Bello of Carcassonne's wife —
  the tree record combines the three Wikipedia attestations: fr.wikipedia.org/wiki/Bello_de_Carcassonne
  (infobox: spouse "Nimilde"), en.wikipedia.org/wiki/Bello_of_Carcassonne (Bello married
  "Ermentrude de Ampurias"), ca.wikipedia.org/wiki/Bel%C2%B7l%C3%B3_de_Carcassona (married
  Nimilda in 805). Two-track rule per N-21. Tree dates kept verbatim (N-5); the literature
  gives no precise dates for her.
- Excluded (not yet verified persons / links), listed in BUILD NOTE per N-21:
  FAMC @F8971@ (parentage — parents not yet verified), FAMS @F8151@ (husband
  "Bellon Borrell /de Carcassonne/" @I232116475924@ (b.780 d.829) is an unsupported
  conflation — no such figure in the literature; fr.wikipedia.org/wiki/Borrell_Ier_d'Osona
  treats Bello and Borrell Ier d'Osona (d.820, parents unknown) as distinct figures).
- Observed, not adjudicated: `@I232116859311@` (Cunigunda //, dateless stub, wife of Bello
  in @F5865@) is a candidate duplicate of this person — record merge deferred under N-21
  (reference file is read-only).
- New WIKIPEDIA source `@S900000012@` (N-13): "WIKIPEDIA: Bello of Carcassonne - wife Nimilde",
  cited on the individual.
- Verified file: 27 individuals / 2 families / 19 sources; 0 malformed lines; 0 dangling
  pointer fields (NOTE-text mentions of unverified IDs follow the prior-run convention).
- Snapshot: verified/snapshots/20260921-0955-cunigunde-ampurias.ged. Reference file untouched (read-only, N-21).

## 20260921-1055 — Cunégonde de Gellone (queen of Italy) ADDED to the verified file (historical fast-track)
- `@I232222925748@` (Cunigunde /Gellone/; BIRT Vermondois Picardie (no date); DEAT 15 Jun
  (no year) Milano) verified as Cunégonde de Gellone (also called Cunégonde de Laon) —
  wife of Bernard of Italy (Bernard d'Italie) from 813 and mother of Pepin of
  Vermandois; queen consort of Italy. Two-track rule per N-21.
  Evidence: fr.wikipedia.org/wiki/Cunégonde_de_Gellone (Origines: Settipani suggests
  daughter of Heribert, possibly named for her grandmother William of Gellone's wife
  Cunegonde — treated as a DIFFERENT person; married Bernard d'Italie avant 817;
  son Pepin b.817, later count of Vermandois; still alive 18 Jun 835 per the San
  Alessandro act) + ca.wikipedia.org/wiki/Cunegunda_d'Austràsia (Cunegunda d'Itàlia,
  "morta 15 de juny de 835" — matches the tree's DEAT 15 Jun; name-coincidence with
  Guillem de Gel·lona's wife discussed as a possible daughter named for the elder).
- NOT a duplicate of William of Gellone's wife Cunegonde `@I232116458499@` (d.19 Jun
  0835, Aachen): the two Cunegondes are two distinct figures in the literature, and the
  tree's husband here is /Bernard/ `@I232222925747@` (the tree's sole surname-only
  Bernard stub: BIRT Vermandois, DEAT 17 Aug (no year) Milan), not William. A dated
  adjudication NOTE was added to @I232116458499@'s entry (N-18 principle).
- Excluded (not yet verified persons / links), listed in BUILD NOTE per N-21:
  FAMS @F5073@ (husband /Bernard/ provisionally Bernard of Italy — husband identity
  not yet verified as a separate item; queued for a future run).
- New WIKIPEDIA source `@S900000013@` (N-13): "WIKIPEDIA: Cunégonde de Gellone (queen
  of Italy)", cited on the individual. (Minted by hand in the verified file only —
  the reference file is read-only per N-21.)
- Maintenance: runs 0755–0955 had hand-added people without updating
  build_verified.py's VERIFIED_PEOPLE list; all four (Bello, Cunegonde-of-Gellone,
  Nimilde, Cunigunde-of-Italy) are now in the list. A builder re-run still FAILS
  LOUDLY on the hand-minted @S900000009@..@S900000013@ sources (fail-closed, by
  design) — queued fix: teach the builder to mint WIKIPEDIA sources on the fly.
- Verified file: 28 individuals / 2 families / 21 sources; 0 malformed lines; 0
  dangling pointer fields (NOTE-text mentions of unverified IDs follow the prior-run
  convention).
- Snapshot: verified/snapshots/20260921-1055-cunigunde-italy.ged. Reference file untouched (read-only, N-21).

## 20260921-1155 — Cunigunda of France (Wigeric's wife) ADDED to the verified file (historical fast-track)
- `@I232118925443@` (Cunigunde /de France, Countess of Lotharingia, Carolingian/, b.0893/about 893,
  d.923/after 923) verified as **Cunigunda of France** (also styled Cunigunda of Sulichgau): daughter of
  Ermentrude of France and granddaughter of Louis the Stammerer (Louis II of France); wife of Wigeric of
  Lotharingia (count palatine of Lotharingia, founder of the House of Ardenne) — married 909 by arrangement
  of Charles III; mother of Frederick I of Upper Lorraine, Adalberon I of Metz, Gilbert, Sigebert, Gozlin of
  Bidgau, Siegfried of Luxembourg, and Liutgarde; remarried c.922 to Ricwin of Verdun (d.923). Two-track rule
  per N-21. Evidence: en.wikipedia.org/wiki/Cunigunda_of_France (references Nash 2017, Vanderputten 2018,
  Parisse 1981) + fr.wikipedia.org/wiki/Wig%C3%A9ric_de_Bidgau ("Cunégonde (v.888 - mort après 923), la fille
  d'Ermentrude..., petite-fille de Louis II le Bègue").
- Tree dates kept verbatim (N-5): b.0893/about 893 and d.923/after 923 match the literature (893-924).
  The 'cunégonde /DE FRIULI/' name variant is unconfirmed in the literature (no Cunigunde of Friuli in the
  sources; likely a conflation with the Eberhard-de-Friuli father tradition).
- Excluded (not yet verified persons / links), listed in BUILD NOTE per N-21:
  - FAMC @F5574@ (Evrard de Friuli + Ermentrude DE FRANCE) and FAMC @F7691@ (Renier I van Henegouwen +
    Alberada van Henegouwen) — the father's identity is genuinely disputed in the literature
    (fr.wiki: "peut-être de Régnier Ier de Hainaut"; Eberhard de Friuli tradition unconfirmed in the
    sources checked). N-3 mapping, persons unverified.
  - FAMS @F4969@ (husband Wigeric of Lotharingia @I232118926224@ not yet verified as a separate item;
    the tree's MARR 0920 postdates the tree's own DEAT 2 July 0919 for Wigeric — noted, not adjudicated;
    en.wiki places the marriage in 909). Wigeric himself is a queued candidate addition.
- Observed: the tree's four-name variant cluster (Cunigunde /de France/, Cunigunda /of France/,
  cunégonde /DE FRIULI/, Cunigunde de France /Carolingian/) all kept as alternates (N-2).
- New WIKIPEDIA source `@S900000014@` (N-13): "WIKIPEDIA: Cunigunda of France", cited on the individual.
- Maintenance: build_verified.py's VERIFIED_PEOPLE list updated (now includes all five hand-added entries).
  Builder re-run still fails loudly on the hand-minted @S900000009@..@S900000014@ sources (fail-closed by
  design) — queued fix unchanged: mint WIKIPEDIA sources on the fly.
- Verified file: 29 individuals / 2 families / 22 sources; 0 malformed lines; 0 dangling pointer fields
  (NOTE-text mentions of unverified IDs follow the prior-run convention).
- Snapshot: verified/snapshots/20260921-1155-cunigunda-france.ged. Reference file untouched (read-only, N-21).
- Note: the public copy `verified/1 Timothy 1_4 - verified - public.ged` was not regenerated this run
  (runs 0755-1055 didn't either; it lags the hand-added entries since Ogive) — queued as a maintenance task.

## 20260921-1355 — Kunigunde (Hemma) von Önningen ADDED (historical fast-track)

- Individual `@I232119044168@` (Kunigunde (Hemma) /von Önningen/ Pfalzgräfin in Schwaben,
  BIRT Cir 980 Öhningen, DEAT 6 March 1020 Dießen am Ammersee, BURI St Stefan Dießen)
  verified and ADDED to the verified file under Kit's historical fast-track (Wikipedia +
  second source, N-21 two-track, no proposal needed).
- Finding: this is Kunigunde [Kunizza] of Diessen — wife of Friedrich I "Roch" (probably
  count of Diessen, successor of Razzo per De Fundatoribus Monasterii Diessenses); she
  founded the monasterium sancti Stephani at Diessen in 1020 after her husband's death;
  bur. Diessen St Stefan (Diessen necrology: "Chuniza com ... uxor Friderici comes
  Rochen", ob. Mar Non / 7 Mar; tree's 6 March within one day, kept verbatim per N-5).
- Evidence: (1) http://fmg.ac/Projects/MedLands/BAVARIAN%20NOBILITY.htm — MedLands
  BAVARIAN NOBILITY: "FRIEDRICH [I] 'Roch' ... m KUNIGUNDE [Kunizza] (-6 Mar after 1020,
  bur Diessen St Stefan)"; De Fundatoribus names "Kunizza comitissa" as wife of
  "Fridericus comes dictus Roch"; she founded St Stefan 1020 after her husband's death.
  (2) https://de.wikipedia.org/wiki/Konradiner — "Kunizza († 1020), ⚭ Friedrich I.,
  1003/1027, Graf wohl von Dießen".
- Excluded per N-21 (unverified), mapped in the BUILD NOTE:
  - FAMC @F10036@ (parents Konrad /De Wetterau/ 910-997 + Regelindis von SACHSEN-LUDOLF):
    parentage conjectural in the literature. MedLands brackets the "daughter of Konrad I
    Duke of Swabia & Richlint" reading and flags Genealogia/Historia Welforum as
    unreliable on Konrad I's daughters; De Fundatoribus instead makes Kunizza the sister
    of sancta Richgardis with Otto the Great as grandfather. Not adjudicated here.
  - FAMS @F526@ (husband Friedrich I /von Wassenburg/ @I232119044167@, b.970 d.1030
    Jerusalem): not yet verified as Friedrich I of Diessen as a separate item; tree's
    d.1030 Jerusalem vs MedLands Friedrich "Roch" d. before 1020 bur. Jerusalem —
    queued as its own verification item.
- Noted: the "(Hemma)" name element and "Pfalzgräfin in Schwaben" style are unconfirmed
  in the literature (no MedLands/Wikipedia attestation of that byname); kept verbatim
  per N-5 with a dated NOTE.
- New WIKIPEDIA source `@S900000015@` (N-13): "WIKIPEDIA: Konradiner (Kunizza) + MedLands
  Bavarian Nobility", cited on the individual.
- Maintenance: build_verified.py's VERIFIED_PEOPLE list updated (now includes all seven
  hand-added entries). Builder re-run still fails loudly on the hand-minted
  @S900000009@..@S900000015@ sources (fail-closed by design) — queued fix unchanged.
- Verified file: 30 individuals / 2 families / 23 sources; 0 malformed lines; 0 dangling
  pointer fields (NOTE-text mentions of unverified IDs follow the prior-run convention).
- Snapshot: verified/snapshots/20260921-1355-kunigunde-oeningen.ged. Reference file untouched (read-only, N-21).
- Note: the public copy `verified/1 Timothy 1_4 - verified - public.ged` still not regenerated
  (lags since Ogive) — queued as a maintenance task.

## 2026-09-21 15:55 PT — 20260921-1555-bernard-of-italy (historical fast-track, N-21)

Snapshot: `verified/snapshots/20260921-1555-bernard-italy.ged`

- `@I232222925747@` (/Bernard/, dateless surname-only stub, DEAT 17 Aug, Milan) VERIFIED
  and ADDED to the verified file: this is **Bernard I, King of Italy** (Bernardo
  d'Italia; 797 - 17 Aug 818), son of Pepin of Italy, grandson of Charlemagne; husband
  of Cunégonde de Gellone (Cunigunde of Laon, `@I232222925748@`) and father of Pepin I
  of Vermandois. Blinded after his failed 817 revolt against Louis the Pious; died at
  Milan, buried San Ambrosio/Sant'Ambrogio. Evidence: en.wikipedia.org/wiki/Bernard_of_Italy
  + fmg.ac MedLands ITALY Kings ("BERNARD ... ([797]-Milan 17 Aug 818, bur Milan, San
  Ambrosio); m ([813]) CUNIGUNDIS"). Tree dates kept verbatim (N-5): DEAT "17 Aug"
  (no year), Milan, matches MedLands' 17 Aug 818 exactly; BIRT place "Vermandois"
  unconfirmed in the literature (birthplace not established - raised at Fulda, returned
  to Italy 812). NOTE: en.wiki gives his death as 17 April 818 rather than 17 Aug -
  death-date variance in the literature, kept as in the tree. Third check:
  it.wikipedia.org/wiki/Bernardo_d'Italia confirms 17 Aug 818, Milan, Sant'Ambrogio.
- Family `@F5073@` (Bernard + Cunégonde de Gellone) now ADDED to the verified file -
  the marriage link is scholarly-attested (m. ([813]) CUNIGUNDIS per MedLands; en.wiki
  notes the marriage year is obscure; it.wiki gives 813). This resolves the open item
  in the Cunégonde entry's BUILD NOTE (ledger 20260921-1055); her NOTE was updated to
  reflect the verified husband identity.
- No parentage (FAMC) added: none on the tree record. The literature's father (Pepin of
  Italy) is not yet admitted to the verified file as this father's record; no false
  link created.
- New WIKIPEDIA source `@S900000016@` (N-13): "WIKIPEDIA: Bernard of Italy + MedLands
  Italy Kings", cited on the individual and the family.
- Maintenance: build_verified.py's VERIFIED_PEOPLE list updated (now includes Bernard)
  and INCLUDE_FAM extended with `@F5073@`. Builder re-run still fails loudly on the
  hand-minted `@S900000009@..@S900000016@` sources (fail-closed by design) - queued fix
  unchanged (public-copy regeneration still pending since Ogive).
- Verified file: 31 individuals / 3 families / 23 sources; 0 malformed lines; 0 dangling
  pointer fields. Reference file untouched (read-only, N-21).

## 20260921-1655 — Friedrich I of Diessen verified and ADDED (historical fast-track)
- @I232119044167@ (Friedrich I /von Wassenburg/ Count im Uber Isar, b.970 Büren, d.1030
  Jerusalem, BURI 1027 Riesgau): VERIFIED as Friedrich [I] "Fridericus comes dictus
  Roch" of Diessen, husband of Kunigunde [Kunizza] of Diessen (already verified,
  @I232119044168@). Evidence: fmg.ac MedLands BAVARIAN NOBILITY (De Fundatoribus
  Monasterii Diessenses: "Kunizza comitissa" wife of "Fridericus comes dictus Roch";
  necrology "uxor Friderici comes Rochen"; d. Jerusalem before 1020) +
  de.wikipedia.org/wiki/Grafschaft_Dießen ("Friedrich I., 1003/1027 Graf, wohl von
  Dießen"). New WIKIPEDIA source @S900000017@ (N-13).
- Tree dates kept verbatim (N-5) with VARIANCE flags: (a) DEAT 1030 Jerusalem — MedLands
  records Friedrich [I] as having died in Jerusalem BEFORE 1020; the 1030 attestation
  belongs to Friedrich [II] (1025/1027/1030), presumably a different person (maybe
  father and son; MedLands: "Wegener conflates Graf Friedrich [I] and Graf Friedrich
  [II] as he appears to ignore the reference to the death of the former before 1020").
  The tree's single Friedrich I record merges data of Friedrich I and II. (b) BURI 1027
  predates DEAT 1030 (internal inconsistency, kept as in tree). (c) BIRT place Büren
  and "von Wassenburg" byname unconfirmed.
- EXCLUDED per N-21: FAMC @F9958@ (parentage unestablished; tree's parents Berthold I +
  Cunigunde /de Lorraine/, the latter RULED OUT 20260921-1255 as unverifiable); CHIL
  @I232119044159@ from @F526@ (tree's "Frederick II Count of Diessen", matches MedLands
  Friedrich [II] fl. 1025-1030, not yet verified as a separate item).
- Family @F526@ added as marriage-only (HUSB+WIFE, MARR attested in De Fundatoribus /
  Diessen necrology) — @F5073@ precedent. Resolves the FAMS @F526@ open item in the
  @I232119044168@ BUILD NOTE (20260921-1355; RESOLVED note appended there).
- Snapshot: verified/snapshots/20260921-1655-friedrich-diessen.ged. Parse: 0 malformed,
  0 dangling pointer fields. Verified file now: 32 individuals / 4 families / 24 sources.
  Reference file untouched.
- 20260921-1706 (follow-up fix to 20260921-1655 run): @F526@ family NOTE corrected —
  de.wiki Grafschaft Dießen does NOT name Kunizza as Friedrich I's wife (worker flag);
  marriage now attributed to MedLands Bavarian Nobility via De Fundatoribus only,
  de.wiki cited only for Friedrich I as count of Diessen. Added SOUR @S900000015@
  (MedLands Bavarian Nobility) to the family record. Parse: 0 malformed, 0 dangling
  pointer fields (NOTE-text ID mentions per standing convention).
