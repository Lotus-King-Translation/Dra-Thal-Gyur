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

The two canonical files now contain 2,659 shared pairs, covering all 5,484
objects once and in release order; all 173 reconciliation footnotes are carried.
All 340 distinct earlier-note IDs remain linked, including 83 absent from the
inline English. Released input hashes still match. Negative/adversarial validation
and the generated manifest remain pending at this provisional checkpoint.
The independent segmentation audit identified the documented transparent
heading exception and five trailing-notice false sentence endings; neither
source nor English wording was changed to address them.
