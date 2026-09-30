# Chapter 1 — bounded v1

**Release candidate — final gate pending**

A corrected Adzom-based reading with a scoped comparative apparatus. This release preserves uncertainty and does not claim exhaustive manuscript collation or reconstruction of an original text.

| Deliverable | Contents |
|---|---|
| [Reading](reading.md) | Corrected text, restored verses and separate headings |
| [Apparatus](apparatus.md) | 183 explicit choices, exact A/B/S quotations and accepted interventions |
| [Machine reading](reading.json) | All 2,635 original anchors, ordered restorations and separate source layers |
| [Changes](CHANGES.md) | Restorations and exact changed-anchor ledger |
| [Coverage](COVERAGE.md) | What was compared, deferred and left uncertain |

The [comparison-scan supplement](comparison-scans.md), [structured apparatus](apparatus.json) and [structured coverage](coverage.json) preserve the full supporting records. Evidence images and historical reports remain linked in the repository. These files are not a standalone scan archive.

Rebuild or verify from the repository root with `python3 diplomatic/release-v1-proposal/build_release.py --repo . --check`. Run the release validator before recording final signoff.
