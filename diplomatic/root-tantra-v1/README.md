# Whole root tantra — bounded v1 assembly preview

**[Read the complete text preview](preview/reading.md)** · [Chapter 6](preview/chapter-06.md) · [Colophon and closing](preview/closing-material.md) · [Machine-readable text](preview/reading.json) · [Source annotations](preview/annotations.json) · [Change index](preview/changes.json) · [Preserved uncertainties](preview/UNCERTAINTIES.md)

**This is a preview, not a final whole-work release.** Chapters 1–5 retain their fixed released readings. Chapter 6 and closing material are assembled from the saved working records, with eight passage decisions and 28 W reference decisions still pending because their integration request was blocked before execution.

| Part | Original anchors | State |
|---|---:|---|
| Chapter 1, including opening title/signs | 2,635 | Released; preserved unchanged |
| Chapter 2 | 987 | Released; preserved unchanged |
| Chapter 3 | 683 | Released; preserved unchanged |
| Chapter 4 | 458 | Released; preserved unchanged |
| Chapter 5 | 434 | Released; preserved unchanged |
| Chapter 6 | 251 | Source checks saved; editorial release gate pending |
| Full-work colophon and closing material | 18 | All source dispositions saved; included in the preview |

The [inventory](INVENTORY.json) accounts for all 5,466 original anchors and every character of the supplied A/B/S files, with zero gaps or overlaps between chapter slices. There are 23 scan-restored main verses: 21 in the fixed earlier releases and two newly saved in Chapter 6. Restored headings, captions and unresolved inscriptions are not counted as main verses.

The preview contains 5,484 sequence objects and preserves 110 previously changed original-anchor strings. These 110 changes are inherited from Chapters 1–5, not new corrections in this run. All original strings, annotations, empty joined/annotation anchors and uncertainty references remain represented. The colophon, seals, invocations and final virtue formulas are not dropped or mislabelled as a seventh chapter.

[Positive preservation validation](PREVIEW-VALIDATION.json) passed, and the build is reproducible. Additional negative-test runner creation was blocked and those tests are not claimed as run. Final Chapter 6 decisions, deliverable acceptance, signoff and tag publication remain pending, followed by final whole-work acceptance and publication.

Rebuild with `python3 diplomatic/root-tantra-v1/build_preview.py --repo .`; add `--check` for reproducibility. Reproduce the inventory with `python3 diplomatic/root-tantra-v1/inventory.py --repo . --check`.

This inventory and assembly do not claim full scan proofreading, exhaustive witness comparison or reconstruction of an original text. Those remain outside the approved bounded v1. Exact continuation is in [Chapter 6](../chapter-06-v1/README.md).
