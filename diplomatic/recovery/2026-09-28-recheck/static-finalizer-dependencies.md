# Static recovery dependency audit — 2026-09-28

This audit checks whether the retained finalizers can recover complete Markdown reports independently of their missing JSON ledgers. **They cannot.** The six report identities examined remain partial: `base-signs-middle.json/.md`, `gcn-middle.json/.md`, and `tingkye-late-continuation.json/.md`. No new manuscript readings or missing records were supplied, and no historical script was executed.

Sources were inspected at recovery commit `1dde3761efc21ba653e87b7f1b8bb08261d72453`; the local Adzom and Gcn scripts match the SHA-256 values recorded in their existing provenance. The examination used source reading and Python AST parsing only.

## Adzom middle signs

Source: `diplomatic/recovery/2026-09-27-task-records/dzongsar_middle/finalize.py` (Git blob `f8bb6613e89cffa85ea1236b799d8ce386c0dc9a`; 14,163 bytes; SHA-256 `5cf4d6a94a2544418363f050f36bd2d8c2b62aaa1da7408a13f19fd80b0701d9`).

The finalizer starts by reading the pre-existing `base-signs-middle.json`. Its Markdown builder is not a complete static literal: it renders every final finding, every page's start/end, and every page's observation detail. Earlier records remain in these collections; the finalizer only modifies some fields and appends others. Its page refinements append to unavailable earlier detail strings.

Complete Markdown therefore requires the missing initial `findings` and `pages` objects and source metadata, including source path/hash. Fourteen appended heading records also obtain their page assignments and crop bounds from `heading-single-bounds.json`. Complete JSON additionally uses `heading-focused-bounds.json`, historical reading-unit bytes, and targeted image bytes for hashes. These are dependencies of the historical output; a current reading file cannot establish the historical reading hash.

The retained script contains substantial exact corrections and proposals, but its static paragraphs and correction fragments do not equal the entire report. Historical proposals must not be adopted merely because they have been preserved.

## Gcn middle

Sources:
- `diplomatic/recovery/2026-09-27-task-records/langtang_ch1/finalize-middle.py.txt` (Git blob `9fd8ed55b1b426f2dc5ea0adad8291d43879d9bd`; SHA-256 `fc5fdeac2a52731643228012142ac626fd0605217ed2ed764c91ea5053143d0b`).
- `diplomatic/recovery/2026-09-27-task-records/langtang_ch1/checkpoint.py.txt` (Git blob `e67e768ffa312c3ddae77095a9dd36f009be1a3c`; SHA-256 `77ecf6e2fd240f67e56905c5010951fb7a5f2c5082b188c7ba5e43db95931369`).

The finalizer calls `get()`, which reads the existing `gcn-middle.json` when present. It adds PDF443–448. The helper's Markdown renderer loops over the full accumulated page and locus collections; PDF411–442 records are absent from the retained helper/finalizer.

The helper's fallback to an empty ledger does not recover those earlier records. Running the finalizer from that fallback would produce only the final six pages while retaining a historical completion statement for PDF411–448. Such output would be misleading as a complete replay. Earlier locus records also determine subsequent sequential locus IDs.

Complete JSON additionally uses source-PDF page rectangles and targeted image bytes for evidence hashes. Those image dependencies do not themselves supply the missing page/locus observations. The existing provenance identifies these scripts as literal recovery inputs with compacted-context provenance for their earlier originals; original report byte identity is unverified.

## Tingkye late continuation

Source: `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tk-finish.py.retained-source.txt` (Git blob `8fb344d33d4663565c7bb487e9cd707409ec8cde`).

The finalizer reads the pre-existing `tingkye-late-continuation.json`, corrects selected discriminating spans, and formats all page and finding rows. The static introductory paragraphs do not contain those rows. The retained nine page-update scripts preserve PDF61–69; the earlier PDF40–60 ledger remains missing.

Complete Markdown requires the full prior page/finding records, their original IDs and confidence fields, and source metadata. The exact update helper is also unavailable. Complete JSON additionally requires the historical EWTS base and native image data used for full-unit text and evidence hashes. Those latter dependencies are not independently needed to format the Markdown tables if the complete historical ledger were recovered; the missing ledger is already a sufficient blocker.

The retained finalization stdout reports 30 pages, 176 findings, and 122 evidence stripes. Counts cannot recover the missing records. This conclusion agrees with `PROVENANCE-tingkye61-69-and-import-replay.json` (Git blob `e5bb5d434f95893a16c5277b87782f73401deed4`).

## Recovery accounting

This audit adds **zero complete report replays**. It narrows the needed recovery targets to the historical ledgers and their exact dependencies. Recovering missing records from original files or original tool inputs could change this assessment. Filling them from summaries, fresh scans, current apparatus data, or guessed sequential IDs would create new work rather than recover the lost reports.
