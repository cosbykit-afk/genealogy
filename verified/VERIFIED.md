# The verified tree — "1 Timothy 1:4"

Kit's order, 2026-09-21: stop patching the Ancestry import. Build fresh,
admitting only what is verified.

## The file

`1 Timothy 1_4 - verified - public.ged` — GEDCOM 5.5.1, UTF-8, LINEAGE-LINKED.
Public copy. The living root individual's record is withheld from this
copy; the private working file (which will be uploaded to Ancestry when
complete) is not published.

## Admission rule (N-21)

A person enters this file only when verified under Kit's two-track rule:

- **Historical track** (ancient/medieval): Wikipedia **plus** a second
  independent source. May be added directly — snapshot this file first,
  verify the parse after, log in `applied/ledger.md`.
- **Document track** (recent lines, Ancestry hints, record searches):
  needs Kit's explicit approval via a PENDING proposal first, same as before.

Every admitted person carries a `VERIFIED` NOTE stating **exactly what was
verified** (the finding, the evidence, the ledger entry) — never a blanket
"this person is verified." Family links to not-yet-verified persons are
excluded from family records and listed in NOTEs instead, so the file never
contains a dangling reference or an unverified claim.

Original `@I...@` / `@F...@` / `@S...@` IDs are kept, so every record
cross-references cleanly with the reference file and the ledger.

## Seed (2026-09-21)

23 individuals, 2 families, 16 sources, built by `build_verified.py` from
`applied/ledger.md`:

- Rollo cluster: Rollo, Poppa of Bayeux, Gerloc, Gisela (debated),
  Grimaldus (verified NOT Rollo's son), Guillaume IV (true parents verified)
- Carolingian ring: Pepin of Italy (b. 12 Apr 0777), Plectrude (false
  Vermandois marriage removed), Pepin of Senlis (false parent link removed),
  Rothold de Senlis (self-spouse stub resolved), Beatrix de Vermandois pair
  (verified NOT duplicates), Rothaide de Bobbio (stub merged, two false
  links detached), Bernard of Senlis (I/II merged, one figure)
- Kit's marks (indicate-only, lineages unaltered): Farahild, Amalberga,
  Hugues le Grand (Jesus line); Bathath, Fenius (Irish pedigree);
  Heracles, Sceaf, Dardanus (mythology seams)
- the living root individual (record withheld from the public copy)
- Families: @F856@ (Rollo + Poppa, MARR 889 Rouen — children Gerloc kept,
  unverified children excluded), @F857@ (Rollo + Gisela, debated)

## The reference file

`~/workspace/genealogy/tree/1 Timothy 1_4.ged` (28,899 individuals) is now
**read-only reference**. It is the quarry: the hourly worker verifies
clusters in it and adds the verified people here. It is never edited again.

## Rebuilding

`build_verified.py` regenerates the seed from the working file + the
curated verified list at the top of the script. To add a newly verified
person, append their entry (ID, label, verified-claim note) and re-run —
or add them by hand following the same NOTE conventions, then verify
with the script's built-in checks (0 malformed, 0 dangling).
