Living document — update these diagrams when adding features.

# genealogy — Architecture

## 1. Context diagram (level 0)

```mermaid
flowchart
    E1["Kit"]
    E2["Public sources"]
    E3["Public readers"]
    E4["Ancestry dot com"]
    SYS("Verified tree publisher")
    E1 -->|"research and approvals"| SYS
    SYS -->|"evidence queries"| E2
    E2 -->|"source material"| SYS
    SYS -->|"public GEDCOM"| E3
    SYS -.-|"planned upload target"| E4
```

## 2. Level-1 data flow diagram

```mermaid
flowchart
    E1["Kit"]
    E2["Public sources"]
    P1("1.0 Verify persons against sources")
    P2("2.0 Record approved changes")
    P3("3.0 Build verified GEDCOM")
    P4("4.0 Publish public copy")
    D1[("D1 Reference GEDCOM")]
    D2[("D2 Change ledger")]
    D3[("D3 Public GEDCOM")]
    D1 -->|"candidate records"| P1
    E2 -->|"evidence"| P1
    E1 -->|"approvals"| P1
    P1 -->|"applied proposals"| D2
    D2 -->|"verified findings"| P3
    D1 -->|"original records"| P3
    P3 -->|"verified only file"| D3
    D3 -->|"public copy"| E1
    D3 -->|"public copy"| P4
```

## 3. Entity–relationship diagram

```mermaid
erDiagram
    PERSON ||--o{ FAMILY : member_of
    PERSON {
        string indi_id PK
        string name
        string birth
        string death
        string verified_note
    }
    FAMILY {
        string fam_id PK
        string marriage_date
        string marriage_place
    }
    PERSON ||--o{ SOURCE : cited_by
    SOURCE {
        string source_id PK
        string title
        string url
    }
    PERSON ||--o{ LEDGER_ENTRY : logged_in
    LEDGER_ENTRY {
        string proposal_id PK
        string entry_date
        string description
    }
```

## Grounding notes

- OBSERVED: 8 files — `README.md`, `LICENSE`, `1 Timothy 1_4 - verified - public.ged`, `verified/VERIFIED.md`, `verified/build_verified.py`, `applied/ledger.md`.
- OBSERVED: README states this is the public copy built only from verified material; the living root individual's record is withheld; the private working file is not published.
- OBSERVED: `VERIFIED.md` gives the admission rule — historical track needs Wikipedia plus a second independent source; document track needs Kit's explicit approval via a PENDING proposal; every admitted person carries a VERIFIED NOTE stating exactly what was verified; no dangling references.
- OBSERVED: `applied/ledger.md` records every applied proposal in order with snapshots and ID-level edits; `build_verified.py` builds the verified-only GEDCOM from the ledger, keeping original `@I`, `@F`, `@S` IDs.
- OBSERVED: `VERIFIED.md` says the private working file will be uploaded to Ancestry when complete — shown as a planned target, not a live integration.
- INFERRED: external entity "Public readers" — the repo is public, but no reader activity was observed.
- INFERRED: the dotted flow to Ancestry dot com is a future intention only; no upload mechanism is present in the repo.
