# Partial Markdown recovery — 2026-09-28

These two readable templates preserve the retained Markdown construction text and successful historical amendments. **Neither is a complete recovered report.** Both contain deliberate `{{UNRECOVERED_SOURCE_PDF}}` and `{{UNRECOVERED_PDF_SHA256}}` placeholders. The missing historical path strings must not be replaced by assumed normalized paths.

The templates are historical records, not new scan assessments. No PDF or image was reread, and no canonical edition or apparatus was changed. The tally remains four complete transcript-derived report replays out of the original 54 missing report identities.

## What was extracted

- `tingkye-early-omission-audit.partial-template.md`: the `lines` constructor from the original successful save source. The later fourth-correction source was blocked before execution and is deliberately **not** applied. The template preserves that historical earlier state, including its then-pending `nas` review and its broader U183 orthographic wording; these are not newly endorsed findings.
- `tharpaling-late-attempt.partial-template.md`: the stage-one Markdown constructor, its five literal page notes, and both exact successful stage-three replacements. Stage two only copied the file bytewise. All provisional locus mappings, including the U1631 opening, remain withdrawn.

Statements in the historical templates about JSON records describe the original workflow. They do not imply those complete JSON reports have been recovered.

## Reproduction

Inspect commit `1dde3761efc21ba653e87b7f1b8bb08261d72453`. Copy these three already-preserved files into one source directory, retaining their basenames:

| Repository source | Required Git blob |
|---|---|
| `diplomatic/recovery/agent-originals/w1er119_ch1/save-tingkye-early-audit.py.retained-source` | `ea8407a101ac4065edb4dce77c4bd6a40b36b063` |
| `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tharpaling-late-attempt.stage1-saved-construction.py.txt` | `680bb3bed2c442058c4d4d80518208ecd73841de` |
| `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tharpaling-late-attempt.stage3-saved-withdrawal.py.txt` | `26dce263a3d8d7f0ca4215f549aa83a35c0c64e3` |

Run `python replay_markdown.py SOURCE_DIRECTORY NEW_OUTPUT_DIRECTORY`. The extractor first verifies all three Git blob hashes. It parses Python AST data expressions through a small whitelist; it never executes the old scripts, imports their modules, reads their historical data dependencies, or runs their mutations. Only literal lists/dictionaries, string concatenation, dictionary indexing, the five bounded formatted rows, and two exact replacements are interpreted. Each historical replacement must match once. A visible recovery notice is added before each template. `checks.json` records generated-file hashes.

## Dependencies that still block complete reports

| Original report | Missing dependency |
|---|---|
| Tingkye early omission audit Markdown | Exact `source_pdf` and `pdf_sha256` values from `tingkye-early-omission-audit-metadata.json`. The original task's retained context no longer contains their metadata-construction input. |
| Tingkye early omission audit JSON | Complete spread-in metadata object, plus hashes of the generated native evidence crops. The three original claim snapshots and native-page metadata excerpts survive separately, but do not establish the whole object. |
| Tharpaling late-attempt Markdown | Exact `source_pdf` and `pdf_sha256` values from the pre-existing `tharpaling-late.json`. No exact historical path string was retained by its original task. |
| Tharpaling late-attempt JSON | Complete pre-existing object, including every `extracted_pages` record and other inherited metadata. Stage one modifies that missing object rather than constructing it fully. |
| Root final audit JSON | The intentionally excluded top-level `evidence_sha256` object, including its historical structure and keys. The three referenced crop files survive, but hashing them now would not establish the exact omitted historical object. |
| Langtang junction audit JSON | The same deliberately omitted `evidence_sha256` field; retained stdout provides the other displayed fields. |
| Root final audit and Langtang junction audit Markdown | No original Markdown body or complete Markdown constructor located in the inspected retained sources. Writing prose from their JSON excerpts would create a new derivative report. |

Independent edition manifests identify a Tingkye PDF hash `573e785a586f1c99af9e4d5c54c0d36fefa4a49c28b4d296f1bf31ef249f1723` and a Tharpaling PDF hash `db895ffc9850a728e25add92491341039547f999fff80d7e73e9521ada10b550`. Their manifest blobs are respectively `3d1373480697e534c9801e77b7e9222b6872aed1` and `0a6d5d106bfcad6f1185d4e2b7ca7eeeb279dd3c`. These support source identification but do not recover the missing metadata objects or exact historical path strings. Consequently neither metadata slot is silently filled.

No original-file byte identity is asserted. These templates improve access to surviving text; they do not reduce the count of 50 incomplete original report bodies.
