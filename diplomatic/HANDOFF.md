# Chapter 1 — recovery and continuation

**Not ready:** full base-sign proofreading and reliable continuous comparison remain unfinished. Chapter 2 has not started.
`main` and `recovery/consolidated-2026-09-27` contain the recovery; commit and push every substantive batch, then verify remote SHAs.

Preserved: 2,635 anchors, 359 exact transcript differences in 183 loci, 13 restored main verses, retained cloud evidence, local backup and unreachable blobs. Current counts are authoritative in [STATUS.json](STATUS.json).
The [recovery audit](recovery/2026-09-27-local/recovery-audit.md) lists 54 missing later report bodies and archive parts010–084. No claim that all cloud work was recovered.
The [scratch inventory](recovery/2026-09-27-local/local-scratch/ARCHIVAL-SUBSET.md), [archive extraction](recovery/2026-09-27-local/scratch-prefix-recovered/README.md) and [image integrity audit](recovery/2026-09-27-local/image-integrity-audit.json) distinguish retained bytes from valid images.

Fresh work: Adzom1973/Gcn boundary mappings; Tingkye three-junction recheck; four unresolved base loci; bounded Tharpaling continuation. See [coverage](collation/chapter-01/scan-coverage.json) and [readiness audit](reviews/chapter-01/readiness-audit-20260927.json).
The [sign-adoption audit](reviews/chapter-01/sign-adoption-audit-20260927.md) withdraws ten provisional punctuation adoptions after anchor mismatches. Their proposals and original images remain preserved. Ten targets now pass independent native-context checks: nine new records and one existing-record revision adopted;30 candidates remain.
Tharpaling recovered notes retain their interrupted-report provenance; empty p052.png stays archived while active notes use its intact halves. PDF56 ends at U02100, as supported by the fresh boundary review.

Next: review the30 remaining sign candidates and continuous physical sign/source-layer coverage; obtain reliable Tibetan readings for the precisely listed uncollated witness ranges. Available but unread scans are not missing sources or agreement.
Preserve unresolved U01522/U02615/U02620/S09 and title/portrait material without supplying expected wording. Sichuan remains transcript-only where full scans are unavailable.

Reproduce from repository root: `python3 diplomatic/tools/build_chapter1.py --repo .` then `python3 diplomatic/tools/validate_chapter1.py --repo .`.
Mechanical success certifies its listed reconstruction/link/hash checks, not chapter readiness. Complete only when the [method](METHOD.md) and [acceptance criteria](reviews/chapter-01/readiness-audit-20260927.json) are satisfied.

Current asset check (requires pikepdf): `python3 diplomatic/tools/verify_recovered_assets.py`; preserves historical acquisition files and verifies the documented AGENTS.md revision in GUIDANCE-PROVENANCE.json.
