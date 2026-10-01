# Paired-text migration — issue #2

Status: provisional implementation; no paired edition published yet.

The only new canonical paired content will be `source.md` and `translation.md`.
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
