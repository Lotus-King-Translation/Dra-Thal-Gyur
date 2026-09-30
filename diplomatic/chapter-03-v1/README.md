# Chapter 3 — bounded v1 release candidate

**Editorial checklist and deliverables complete; final publication gate pending.**

[Read the candidate](release/reading.md) · [Apparatus](release/apparatus.md) · [Machine edition](release/reading.json) · [Changes](release/CHANGES.md) · [Coverage](release/COVERAGE.md)

| Fixed workstream | Complete | Remaining |
|---|---:|---:|
| A/B/S passage decisions | 41/41 | 0 |
| W reference-block decisions | 76/76 | 0 |
| Targeted source dispositions | 10/10 | 0 |
| Deliverable groups | 5/5 | 0 |
| Final release gate | Pending | 1 gate |

All 683 original anchors U03623–U04305 remain. The candidate includes three restored main verses, ten separate source-note components and one local word correction. Eleven original anchor strings change without altering any original source file. Chapters 1 and 2 remain unchanged.

[Plan](PLAN.json) · [Progress](PROGRESS.json) · [Editorial review](EDITORIAL-REVIEW.md) · [Successful positive validation](release/VALIDATION.json) · [Final-test access record](checkpoints/0008-test-access.json)

The positive validator and reproducible build passed. The additional corruption-test script is saved but unrun: its tool request was blocked before execution, and no passing result is claimed. Final source-bound signoff, final-mode validation and version-tag publication are still pending. Preserve this distinction rather than restarting the scholarly work or declaring a release from file existence alone.

The next stage is the final gate, not another round of page reading. Use the already saved `test_release.py`, `validate_release.py`, `build_release.py`, decisions and editorial review. Do not recreate the 41/76/10 completed decisions. The blocked request and original error must remain visible.

Run `python3 diplomatic/chapter-03-v1/progress.py --repo .` for the fixed counters. Its inherited `source_families_verified` field means four electronic representations A/B/S/W, not four independent witness families; W remains a related reference. The requested metric-label clarification was part of the blocked call and has not been applied to the script.

Untargeted source text remains supplied Adzom, not independently proofread text. Full physical proofreading, exhaustive comparison of acquired witnesses and a reconstructed original remain outside this release. Chapter 4 has not started.
