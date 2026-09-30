# Chapter 2 — bounded v1

**Completed for the approved bounded release scope.** Version: `chapter-02-v1.0.0`.

Start with the [released reading and deliverables](release/README.md), [validation](release/VALIDATION.json), and [progress report](PROGRESS.json). The [final editorial review](FINAL-REVIEW.md) records what was accepted and what remains uncertain.

| Release workstream | Completed | Remaining |
|---|---:|---:|
| Exact A/B/S passage decisions | 56 / 56 | 0 |
| Related Wikisource block decisions | 105 / 105 | 0 |
| Fixed targeted source-check dispositions | 10 / 10 | 0 |
| Deliverable groups | 5 / 5 | 0 |

All **987 original anchors**, U02636–U03622, remain preserved. Eight source-layer corrections affect ten anchor strings and preserve nine separate annotation components. One additional record retains a difficult reading unchanged with an uncertainty flag. No main verse is supplied conjecturally.

This release is not a complete Adzom scan proofread. Untargeted text remains the supplied Adzom scaffold; other printed witnesses have not received continuous Chapter2 collation. Exact electronic comparison, source-linked local corrections, explicit editorial decisions and uncertainty disclosures define this bounded release. The smaller rig pa at PDF111 remains a qualified gloss-or-addition rather than silently certified main wording.

## Reproduce and verify

```bash
python3 diplomatic/chapter-02-v1/collate.py --repo . --check
python3 diplomatic/chapter-02-v1/build_release.py --repo . --check
python3 diplomatic/chapter-02-v1/validate_release.py --repo . --require-final
python3 diplomatic/chapter-02-v1/progress.py --repo .
```

The sources, frozen comparison IDs, evidence locations, decisions and checkpoint receipts remain in this directory. Record a visible status report after every verified commit. Chapter1's tagged release is unchanged. Chapter3 has not been started.
