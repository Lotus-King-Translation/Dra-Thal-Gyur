# Interrupted-reader recovery and next integration — 2026-09-29

**Chapter 1 remains unfinished. This restart preserves completed reader outputs; it does not certify additional pages or adopt new Tibetan readings.**

## Verified preservation

The inherited `main` checkout was at `3ebd89387b46fbebbd80fce3946b3956fb89d5c9`, matching the live remote, with 106 untracked project files. Twenty-one reader processes had completed successfully. Their outputs, execution receipts, session logs and capture logs were still unpublished, together with a 27-line, incomplete integration-script draft.

All 106 files were reviewed for project scope and possible credentials, preserved byte-for-byte on `recovery/20260929-interrupted-page-reports-103138`, and published in `f0f8241aa3d1ad52b245e8f4098834a472c6399c`. That commit was then fast-forwarded into `main` and remotely verified. No interrupted output was discarded or replaced.

The individual original hashes are in `restart-audit.json`. Selected surviving coordinator memory is in `interrupted-coordinator-snapshot.json`, published with the audit in verified commit `40fb2d5c4730404df66280fa1adecf717f1c255b`. Those in-memory inputs were older than the saved inputs: 80 versus 81 additional-intervention entries, and 150 versus 180 comparison records. They are historical/provisional snapshots, not permission to overwrite the newer curated ledgers.

Read-only chapter validation and reproducible-build checks passed after the recovery fast-forward. The unchanged chapter Markdown SHA-256 was `542d3851cdc1759a16b8e66d3e302b43ccc95f865a6a49a4d03ceb53201889cc`. The validation counted 2,635 source anchors, 86 total scan-intervention records, 13 restored main verses and 180 comparison observations, including uncertainty. These are preservation and structure checks, not completion certificates.

## Recovered outputs that require integration review

The earlier packet definitions remain in `SESSION-20260928-CONTINUE2/wave03-plan.json`. This restart preserves the following reader outputs at their original paths beside the active continuation reports:

| Task | Batch IDs | Target pages | Reader outputs |
| --- | --- | --- | --- |
| C1-BASE-PHYSICAL | B07-P0008 through B12-P0013 | Adzom PDF8–13 | 6 |
| C1-TINGKYE | B04-P0006 through B08-P0010 | Tingkye PDF6–10 | 5 |
| C1-TSAMDRAK | B04-P0016 through B08-P0020 | Tsamdrak PDF16–20 | 5 |
| C1-DEGE | B02-P0004 through B06-P0008 | Degé PDF4–8 | 5 |

A completed reader process is not a completed collation. Read each output's `coverage_assessment`, `unread_after_inspection` and `unexamined_spans`. Preserve qualified readings, distinctions between target and flank pages, and every failed or superseded proposal.

Before advancing those frontiers, reconcile the eight earlier reports in `SESSION-20260928-CONTINUE2/wave02-plan.json`: Adzom physical PDF4–7; the PDF102/S09 boundary attempt; Tingkye PDF5; Tsamdrak PDF15; and Degé PDF3. Their saved intake and coordinator notes must not be skipped merely because the later outputs now exist. The incomplete `integrate_wave02.py` is an interrupted draft, not a completed integration operation or a script to execute as current authority.

## Important retained decisions and questions

The saved page7 boundary adjudication rejects the earlier blanket proposal to delete 22 shads. Its full-interval inventory supports retaining two detached components at the stated boundaries. Reuse that recorded disposition without silently accepting the earlier raw count or treating the addendum's mistaken lexical labels as source corrections.

The saved S09 coordinator note corrects the raw reader's following-incipit identification: the minimal boundary context is `དེ་ནས་ལྷ་དབང་རྟོག་པ་མེད`, not the raw report's `de nas ston pa`. The compact inscription itself remains unresolved. This is reuse of saved evidence, not a fresh visual finding in this restart.

Desk review of the preserved Adzom PDF4 report identifies pending questions at U00029's small-heading ending, U00045's possible internal separator, U00048's prefix segmentation, and U00049's middle wording. These are reader hypotheses with native bounds, not accepted corrections. The PDF5 report distinguishes full-height boundary bars from short row-end marks and marginal components; its remaining small-mark uncertainties must stay visible. No canonical adoption was made from this desk review alone.

## Connection interruption and safe restart

After preservation and these read-only reviews, the authorized remote computer stopped responding to process requests and repeated connectivity pings. Its device registry still reported it online; that registry entry did not establish successful command or image access. GitHub remained accessible, and `main` was independently read at `40fb2d5c4730404df66280fa1adecf717f1c255b` before publishing this note.

This note is published through the GitHub connector after the last verified local checkpoint. On reconnection, inspect all tracked, untracked and ignored project work again, preserve anything new, then fetch and fast-forward the local checkout. Do not reset, force-push, rerun the older draft integration script, or regenerate over unpreserved work.

Next action: review and integrate the earlier eight saved reports in bounded task groups, then the 21 newly preserved outputs, updating the authored collation and exact coverage before commissioning replacement readings. Keep committing and verifying each small integrated batch. No new chapter or whole-witness completion claim is authorized by this receipt.
