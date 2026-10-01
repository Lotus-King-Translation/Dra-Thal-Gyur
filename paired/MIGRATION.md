# Paired-text/2 migration — issue #4

V2 adds one required source-only `format` field and releases the distinct edition
`dra-thal-gyur-paired-v2.0.0`. English inherits the format through the shared ID.
The source words, English words, golden roles and release pins are unchanged.

All 2,660 baseline pairs at `aae8883b13ff0f23da2603aecc12a64a15ffe25b` were
audited before canonical changes. Source-based decisions and their integration
rationale are in [STRUCTURE-DECISIONS.json](v2/STRUCTURE-DECISIONS.json); the
complete v1 → v2 record, including all unchanged pairs, is the generated
[PAIR-AUDIT.json](v2/PAIR-AUDIT.json). It is supporting lineage, not a third
canonical content/alignment authority.

| Retired v1 ID | New v2 IDs in source order | Structural boundary |
| --- | --- | --- |
| DTG-000010 | DTG-002661, DTG-002662 | prose hearing formula / verse |
| DTG-000017 | DTG-002663, DTG-002664 | prose hearing formula / verse |
| DTG-000165 | DTG-002665, DTG-002666 | verse / empty source-annotation carriers |
| DTG-001124 | DTG-002667, DTG-002668, DTG-002669 | verse / h3 heading / verse |
| DTG-001185 | DTG-002670, DTG-002671, DTG-002672 | verse / empty source-annotation carrier / verse |

All 2,655 other pair IDs retain their exact memberships. No old changed identity
is reused, no golden object is split and no pair crosses a format boundary.
The 2,667 resulting pairs are 48 prose, 2,448 verse, 2 h1, 0 h2 and 169 h3.
Existing chapter wrappers remain h2 outside the pairs; closing is not chapter 7.

Structural form is determined from Tibetan and editorial source structure,
never English punctuation. The two title-leaf headings differ from embedded
opening naming formulas. Each source-heading class was reviewed before retaining
its common chapter-internal h3 rank; different words do not invent another level.
The moderate-confidence narrative-formula and closing-paratext dispositions are
explicit presentation decisions, not claims of settled historical poetic genre.

The exact-source join and English markup conventions below remain unchanged.
All 173 reconciliation footnotes retain their bodies; only pair backlinks change
where a containing v1 pair split. All 340 legacy IDs/4,932 object-note relations,
65 annotations, 23 restored verses and 18 closing anchors survive. There is no
fresh semantic QC claim. The v1 account below remains historical provenance.

Audit checkpoints on remote main: `43825d4` (scope/template), `a3181ae`
(heading and Chapter 1 evidence), `e9ebdd6` (complete audit/decisions/lineage),
`d49388b` (canonical v2 implementation and preservation tests).
The final review and hash-bound signoff precede the annotated tag; its verified
object/peeled commit are recorded afterward in v2/PUBLICATION.json on main.

---

# Historical paired-text/1 migration — issue #2

Status: implementation complete; branch publication and pull-request verification
are recorded below. No new Git release tag is created by this migration.

The only new canonical paired content is `source.md` and `translation.md`.
This is a presentation/segmentation migration, without new translation or semantic QC.

## Immutable authorities

| Authority | Tag object | Release commit |
| --- | --- | --- |
| `root-tantra-v1.0.0` | `97379615d268149eee768c9c1ec99b7be2f993b4` | `b83051912977268b97615bd382d82e51c3406d61` |
| `translation-golden-aligned-v1.0.0` | `ed0783c6a394d4ace736a09d812f0666c6743848` | `e24e97ddad9cefa339b5583a38389179dba7a365` |

The clean starting checkout was `5b94a53b19f1c3211adabadbecce08c1b96c0bf1`.
The release receipts and active translation handoff were read; the existing
English final validator and reproducibility check passed before migration.
Both tag objects and peeled commits were checked against the remote.

## Finite implementation batches

1. Pin inputs, document the format, inspect segmentation and exceptional roles.
2. Create deterministic paired files and provenance/notes from the fixed releases.
3. Validate preservation and stable identity; test deliberate corruptions.
4. Independently review, reproduce artifacts, verify remote publication.

No released artifact, glossary assignment, inherited English wording, or
uncertainty is to change. Preserve all 5,484 golden objects (5,466 original
anchors and 18 additions), 23 restored verses, 173 reconciliation endnotes,
six chapters, and 18 full-work closing anchors. Historical scan-only records
remain linked to their golden occurrences, never duplicated as fresh text.

## Initial import checkpoint

At provisional checkpoint `616175172f8ed09bbfd8a63ecb7e2f8dada431c6`,
the two canonical files contained 2,659 shared pairs, covering all 5,484
objects once and in release order; all 173 reconciliation footnotes are carried.
All 340 distinct earlier-note IDs remain linked, including 83 absent from the
inline English. Released input hashes still match. Negative/adversarial validation
and the generated manifest remain pending at this provisional checkpoint.
The independent segmentation audit identified the documented transparent
heading exception and five trailing-notice false sentence endings; neither
source nor English wording was changed to address them.


## Validation checkpoint

The reviewed migration contains **2,660 pairs**. Boundary detection now also
recognizes the trailing `[Numerical construction unresolved.]` notice at
U01192: the completed U01191–U01192 sentence is separate from U01193–U01196.
No wording changed. This correction precedes publication of the paired edition.
Provisional DTG-000545 split into final DTG-000545 and DTG-000546; subsequent
provisional IDs incremented by one. The provisional checkpoint remains in Git.
Final membership is locked by SHA-256
`44a3c8c5b50e932ec08e40d72a4075889521a189aaf40245e815e6a2f024fc0f`.

[MANIFEST.json](MANIFEST.json) is generated from validated canonical Markdown.
It records complete ordered coverage, role and part counts, restored and closing
locations, and every reconciliation note's pair and original golden references.
[NEGATIVE-TESTS.json](NEGATIVE-TESTS.json) records 3 positive checks and rejection
of 41 corrupted fixtures. The validator protects 128 input files; the paired
files reproduce exactly from the fixed releases. Independent reverse projection
also recovered all 5,484 Tibetan and English objects without changed strings.

The counts are 5,466 original anchors plus 18 additions, 23 restored verses in
10 intact objects, 173 reconciliation endnotes, 340 distinct legacy note IDs,
4,932 legacy object/note associations, 65 source annotation components, and
18 closing anchors. Unmatched pairs, duplicated objects and omitted objects
are all zero. Exact preservation checks do not certify the inherited translation
or resolve its uncertainties.


## Final review and continuation

The independent review found no blocking acceptance gap after the U01192
correction. It checked reverse projection, note/evidence reachability and
rejected additional in-memory envelope, Unicode, role, hidden-note, backlink,
closing-structure and historical-scan corruption probes. This is implementation
review, not fresh semantic QC of the inherited translation.

Verified remote checkpoints on `codex/paired-text-issue-2`:

- Scope and immutable authorities: `687801cb862050b43dd08721e39734e3107f507d`.
- Provisional 2,659-pair import: `616175172f8ed09bbfd8a63ecb7e2f8dada431c6`.
- Final 2,660-pair identity, validator and 41 corruption rejections:
  `07e6e57e67a7f00eb9470a388d0baf3327f3d26e`.

The current branch ref is the authority for the newest checkpoint. CI runs the
validator, corruption suite, exact test-receipt comparison, migration check and
manifest check. Future editing starts from the two canonical Markdown files.
For changed membership, create a new paired edition and explicitly record
old/new pair lineage; the validator's membership lock must never be silently
updated under this edition's identity. Never mutate the two input release tags.
