# Golden-aligned English — completed source reconciliation

The revised translation is [here](../../2026-10-01-golden-aligned/Dra-Thal-Gyur-English.md), with [endnotes](../../2026-10-01-golden-aligned/ENDNOTES.md) and a [publication receipt](../../2026-10-01-golden-aligned/PUBLICATION.json).

Fixed translation tag: **translation-golden-aligned-v1.0.0**, at **e24e97ddad9cefa339b5583a38389179dba7a365**. The governing Tibetan remains **root-tantra-v1.0.0**. Do not move either tag or overwrite the earlier translation.

All 110 changed source anchors and 18 added golden objects have reviewed dispositions. The 23 restored verses have English in sequence; 65 source-note components and all 72 golden uncertainty-bearing objects are accounted for. There are 173 new endnotes. No source-reconciliation or annotation-publication tasks remain.

The interrupted work was already committed and tagged. On resumption, the final validator and all 36 corruption tests were run again; their results reproduced exactly. [RESUME-VERIFICATION.json](RESUME-VERIFICATION.json) records execution and remote refs. No additional Tibetan or English reading was introduced by that publication-finalization step.

Run from the repository root:

```sh
python3 -B translations/2026-09-26-full-draft/golden-review/validate_translation.py --require-final
python3 -B translations/2026-09-26-full-draft/golden-review/test_translation.py
python3 -B translations/2026-09-26-full-draft/golden-review/build_translation.py --check
```

[PROGRESS.json](PROGRESS.json) is the current completion record. PLAN.json is the hash-bound initial scope, not a live status flag. The earlier draft's handoff and notes are preserved historical inputs; [LEGACY-NOTES.md](../../2026-10-01-golden-aligned/LEGACY-NOTES.md) links them to this revision's updates.

Scope: full comparison of the translation's Adzom source against the golden edition and reconciliation of the consequences. Unchanged-source English inherits its prior translation and open questions. Fresh independent semantic review of every unchanged verse, full manuscript collation, and resolution of every uncertain expression are not claimed.
