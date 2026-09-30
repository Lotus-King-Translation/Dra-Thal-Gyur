# Chapter 4 — bounded v1

**Completed for the bounded release scope: chapter-04-v1.0.0.**

[Reading](release/reading.md) · [Apparatus](release/apparatus.md) · [Machine edition](release/reading.json) · [Changes](release/CHANGES.md) · [Coverage](release/COVERAGE.md)

| Fixed workstream | Complete | Remaining |
|---|---:|---:|
| A/B/S passage decisions | 33/33 | 0 |
| W reference-block decisions | 55/55 | 0 |
| Targeted source dispositions | 8/8 | 0 |
| Deliverable groups | 5/5 | 0 |
| Final tests and scoped signoff | Passed | 0 |

All 458 original anchors U04306–U04763 are preserved. Three main question verses are restored after U04328. Two source-note components are separately preserved at U04312 and U04519, with their qualifications visible; U04562 remains explicitly uncertain without a conjectural word repair. All earlier released chapters remain unchanged.

[Plan](PLAN.json) · [Progress](PROGRESS.json) · [Final review](FINAL-REVIEW.md) · [Validation](release/VALIDATION.json) · [29 corruption tests](checkpoints/0007-corruption-tests.json)

Exact fine-grained and whole-passage comparisons reconstruct B and S. The 55 W decisions preserve the related reference without treating it as an independent printing. Final signoff is bound to the actual source inputs and review. Remote commit/tag verification is a separate publication step; the version tag stays on released content rather than a later receipt.

Run `python3 diplomatic/chapter-04-v1/validate_release.py --repo . --require-final` to verify. Run `python3 diplomatic/chapter-04-v1/progress.py --repo .` for the fixed counters. Report status with every verified commit.

Untargeted text remains the supplied Adzom transcript. Complete physical proofreading, exhaustive witness comparison and reconstruction of an original remain outside this v1 release. Chapter 5 has not been started.
