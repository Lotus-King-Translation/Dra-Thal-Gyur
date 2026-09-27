# Missing-report recovery matrix — 2026-09-27

**4 of the 54 report bodies have complete transcript-derived replays. None of the 54 has been recovered as a byte-verified original file; 50 complete report bodies remain unrecovered.** This is a recovery inventory, not completion of Chapter 1 or new witness collation.

Inspected branch: `recovery/task-records-2026-09-27`, commit `91a8aa44ba412844ebc6ee4125288c23d8e036cf`. The denominator is exactly the missing-basename list in `diplomatic/recovery/2026-09-27-local/recovery-audit.json`. The JSON companion records every item and evidence blob SHA.

The four complete replays are the Gcn late JSON/Markdown pair and the W1ER119 import-audit JSON/Markdown pair. Gcn late documents a failed bounded reading attempt; replaying its full historical content does not certify the witness. Its superseded locator guesses remain historical evidence.

## Category meanings

| Category | Files | Meaning |
|---|---:|---|
| Original bytes | 0 | Surviving original report bytes, with original byte identity established; none recovered among these 54. |
| Complete replay | 4 | Complete report content mechanically recreated from retained historical literal source/generator. No inference of unavailable readings and no original-byte identity claim. |
| Partial literal evidence/source | 19 | Exact retained tool input/output, report fragments or related literal audit records survive, but the complete original report is not recovered. For paired Markdown reports, related JSON evidence does not mean original Markdown text survives. |
| Summary only | 23 | Substantive scope/findings/corrections survive only in a compacted summary, recovery summary or handoff; not original report bodies. |
| No original body located | 8 | Only filename, scope/count metadata or distinct secondary-audit records are located; no substantive original report body is recovered. |

## All 54 original report identities

The prior audit records basenames, not one authoritative original absolute location. Sources mention both scratch files and imported repository copies. This inventory preserves those original identities without inventing absolute paths. Evidence references below identify exact current repository paths and blobs.

| Original report | Recovery category | Evidence | Limit |
|---|---|---|---|
| `base-signs-early.json` | Summary only | E01, E02 | Retained summary describes 34 pages and 25 findings, including named signs and bounds. No original page/findings objects or Markdown body survives. |
| `base-signs-early.md` | Summary only | E01, E02 | Retained summary describes 34 pages and 25 findings, including named signs and bounds. No original page/findings objects or Markdown body survives. |
| `base-signs-middle.json` | Partial literal evidence/source | E03, E04 | Exact, hash-matched finalizer survives. It reads a missing pre-existing JSON ledger and evidence files; it cannot restore the complete report. Historical proposals require review before any adoption. |
| `base-signs-middle.md` | Partial literal evidence/source | E03, E04 | Exact, hash-matched finalizer survives. It reads a missing pre-existing JSON ledger and evidence files; it cannot restore the complete report. Historical proposals require review before any adoption. |
| `base-signs-late.json` | Summary only | E02 | Recovery packet retains later sign proposals and pagewise scope. No original late-report body or complete generator has been recovered. |
| `base-signs-late.md` | Summary only | E02 | Recovery packet retains later sign proposals and pagewise scope. No original late-report body or complete generator has been recovered. |
| `tingkye-continuation.json` | Partial literal evidence/source | E05, E06, E07, E08 | Three historical claim snapshots survive as literal stdout; other PDF3–34 scope/findings survive only in a compacted summary. The U183–184 omission claim was withdrawn. Full report body absent. |
| `tingkye-continuation.md` | Partial literal evidence/source | E05, E06, E07, E08 | Three historical claim snapshots survive as literal stdout; other PDF3–34 scope/findings survive only in a compacted summary. The U183–184 omission claim was withdrawn. Full report body absent. |
| `tingkye-late-continuation.json` | Partial literal evidence/source | E09, E10, E02 | Literal related audits retain selected TL references and three guided checks. The 30-page/176-finding original ledger is not recovered at this snapshot; further retained update sources are pending. |
| `tingkye-late-continuation.md` | Partial literal evidence/source | E09, E10, E02 | Literal related audits retain selected TL references and three guided checks. The 30-page/176-finding original ledger is not recovered at this snapshot; further retained update sources are pending. |
| `tingkye-early-omission-audit.json` | Partial literal evidence/source | E08, E06, E05, E11 | Saved construction source, three original claim snapshots and native metadata stdout survive. Later fourth-correction input failed before execution. No complete original output file or original-byte equality is established. |
| `tingkye-early-omission-audit.md` | Partial literal evidence/source | E08, E06, E05, E11 | Saved construction source, three original claim snapshots and native metadata stdout survive. Later fourth-correction input failed before execution. No complete original output file or original-byte equality is established. |
| `tsamdrak-middle.json` | No original body located | E09, E12 | Import audit reports 35 pages/134 findings and consistency checks, but does not contain the report's actual page ledger or finding bodies. Original author reports no retained complete body. |
| `tsamdrak-middle.md` | No original body located | E09, E12 | Import audit reports 35 pages/134 findings and consistency checks, but does not contain the report's actual page ledger or finding bodies. Original author reports no retained complete body. |
| `tsamdrak-late.json` | Summary only | E01, E02 | Summary retains PDF49–83 scope, 80-finding count and selected findings/corrections. No complete original records or generator. |
| `tsamdrak-late.md` | Summary only | E01, E02 | Summary retains PDF49–83 scope, 80-finding count and selected findings/corrections. No complete original records or generator. |
| `langtang-ch1.json` | Summary only | E13, E07 | Summary and original handoff describe PDF1–52/146 loci and the withdrawn U580 reading. No full report or opening generator. |
| `langtang-ch1.md` | Summary only | E13, E07 | Summary and original handoff describe PDF1–52/146 loci and the withdrawn U580 reading. No full report or opening generator. |
| `langtang-middle.json` | Summary only | E07 | Compacted summary retains PDF53–78/159 observations, selected omissions and heading corrections. It is explicitly not original report text. |
| `langtang-middle.md` | Summary only | E07 | Compacted summary retains PDF53–78/159 observations, selected omissions and heading corrections. It is explicitly not original report text. |
| `langtang-late.json` | No original body located | E02, E14 | Scope/count metadata and a separate guided junction audit survive. No original late-report page ledger or 34 finding bodies has been recovered. |
| `langtang-late.md` | No original body located | E02, E14 | Scope/count metadata and a separate guided junction audit survive. No original late-report page ledger or 34 finding bodies has been recovered. |
| `dege-continuation.json` | No original body located | E02 | Recovery packet records continuation scope and DGC restoration cross-references, but no original continuation report body is available. |
| `dege-continuation.md` | No original body located | E02 | Recovery packet records continuation scope and DGC restoration cross-references, but no original continuation report body is available. |
| `dege-late.json` | Summary only | E01 | Summary retains PDF29–41 endpoints, 25-finding breakdown, selected findings and crop bounds. Original JSON/Markdown and helper scripts absent. |
| `dege-late.md` | Summary only | E01 | Summary retains PDF29–41 endpoints, 25-finding breakdown, selected findings and crop bounds. Original JSON/Markdown and helper scripts absent. |
| `dege-final.json` | No original body located | E02 | Packet records the main-row endpoint at PDF54 row3. No original final-report body or complete retained construction source has been recovered. |
| `dege-final.md` | No original body located | E02 | Packet records the main-row endpoint at PDF54 row3. No original final-report body or complete retained construction source has been recovered. |
| `tharpaling-continuation.json` | Summary only | E02 | Three false restoration-absence claims and their withdrawal reasons survive in the recovery packet. Full continuation report absent; original false claims must not be readopted. |
| `tharpaling-continuation.md` | Summary only | E02 | Three false restoration-absence claims and their withdrawal reasons survive in the recovery packet. Full continuation report absent; original false claims must not be readopted. |
| `tharpaling-middle.json` | Summary only | E02, E15 | Summary reports sequential PDF17–43 scope, correction of S01 presence and endpoint corrections. Exact outage messages preserve the later handoff, not this report body. |
| `tharpaling-middle.md` | Summary only | E02, E15 | Summary reports sequential PDF17–43 scope, correction of S01 presence and endpoint corrections. Exact outage messages preserve the later handoff, not this report body. |
| `tharpaling-late-notes.json` | Partial literal evidence/source | E16, E17, E15, E18, E19 | Exact saved append source for PDF44–47 and failed-save source for PDF48–51 survive. Earlier ledger dependency is absent; unsaved PDF48–51 notes are not a recovered original file. |
| `tharpaling-s02-s03-corrections.json` | Summary only | E02, E15 | Correction conclusions and confirmation that a correction file had been saved survive. Complete original correction-file body absent. |
| `tharpaling-late-attempt.json` | Partial literal evidence/source | E20, E21, E22, E12 | Exact original construction, copy and withdrawal bodies survive. Missing pre-existing extracted_pages metadata prevents full recreation. Final stage withdraws all provisional locus mappings; no positive variants or agreement remain. |
| `tharpaling-late-attempt.md` | Partial literal evidence/source | E20, E21, E22, E12 | Exact original construction, copy and withdrawal bodies survive. Missing pre-existing extracted_pages metadata prevents full recreation. Final stage withdraws all provisional locus mappings; no positive variants or agreement remain. |
| `adzom73-mapping.json` | Summary only | E13, E02 | Summary retains root/container and Chapter1 mapping. Complete mapping report text absent. |
| `adzom73-mapping.md` | Summary only | E13, E02 | Summary retains root/container and Chapter1 mapping. Complete mapping report text absent. |
| `gcn-mapping.json` | Summary only | E13, E02 | Summary retains root title/incipit/colophon and Chapter1 boundary mappings with MRC-rendering caveat. Complete mapping report text absent. |
| `gcn-mapping.md` | Summary only | E13, E02 | Summary retains root title/incipit/colophon and Chapter1 boundary mappings with MRC-rendering caveat. Complete mapping report text absent. |
| `gcn-opening.json` | Summary only | E13 | Summary retains PDF408–410 scope, selected findings and queries. Opening generator and original report records absent. |
| `gcn-opening.md` | Summary only | E13 | Summary retains PDF408–410 scope, selected findings and queries. Opening generator and original report records absent. |
| `gcn-middle.json` | Partial literal evidence/source | E23, E24, E13, E25 | Literal later increment contains PDF443–448 and selected rereads; missing earlier checkpoint prevents recovery of full PDF411–448/38-page/68-locus report. |
| `gcn-middle.md` | Partial literal evidence/source | E23, E24, E13, E25 | Literal later increment contains PDF443–448 and selected rereads; missing earlier checkpoint prevents recovery of full PDF411–448/38-page/68-locus report. |
| `gcn-late.json` | Complete replay | E26, E27, E28, E29, E30 | Complete historical failed-attempt report content replayed from retained initial source plus exact amendments. Original byte identity unknown. Historical U1427/U1511 locator guesses remain superseded; this is not completed lexical collation. |
| `gcn-late.md` | Complete replay | E26, E27, E28, E29, E30 | Complete historical failed-attempt report content replayed from retained initial source plus exact amendments. Original byte identity unknown. Historical U1427/U1511 locator guesses remain superseded; this is not completed lexical collation. |
| `root-final-audit.json` | Partial literal evidence/source | E10, E31 | Literal JSON stdout preserves all displayed fields except deliberately excluded evidence_sha256. Original JSON bytes and original Markdown body are unavailable. |
| `root-final-audit.md` | Partial literal evidence/source | E10, E31 | Literal JSON stdout preserves all displayed fields except deliberately excluded evidence_sha256. Original JSON bytes and original Markdown body are unavailable. |
| `langtang-junction-audit.json` | Partial literal evidence/source | E14, E31 | Literal JSON stdout preserves all displayed fields except deliberately excluded evidence_sha256. Original JSON bytes and original Markdown body are unavailable. |
| `langtang-junction-audit.md` | Partial literal evidence/source | E14, E31 | Literal JSON stdout preserves all displayed fields except deliberately excluded evidence_sha256. Original JSON bytes and original Markdown body are unavailable. |
| `integration-final-audit.json` | Partial literal evidence/source | E32, E33 | Literal initial and amendment sources survive. Dynamic fields require the missing historical 1,024-observation apparatus snapshot; running against current data would not recover the original report. |
| `integration-final-audit.md` | Partial literal evidence/source | E32, E33 | Literal initial and amendment sources survive. Dynamic fields require the missing historical 1,024-observation apparatus snapshot; running against current data would not recover the original report. |
| `w1er119-import-audit.json` | Complete replay | E09, E34, E35, E12 | Complete static JSON dictionary and Markdown text replayed from retained successful construction source. Original pre-loss output hashes unavailable; historical consistency findings are not fresh scan certification. |
| `w1er119-import-audit.md` | Complete replay | E09, E34, E35, E12 | Complete static JSON dictionary and Markdown text replayed from retained successful construction source. Original pre-loss output hashes unavailable; historical consistency findings are not fresh scan certification. |

## Evidence locations

These paths were verified in the inspected commit. New scripts and provenance records are preservation artifacts, not extra recovered members of the original 54-file set.

| ID | Current repository path | Git blob SHA |
|---|---|---|
| E01 | `diplomatic/recovery/2026-09-27-task-records/zhichen_ch1/retained-summary-fragments.txt` | `d3a6c15a08b11cabfec7d63391e69c7efe5278da` |
| E02 | `diplomatic/recovery/2026-09-27.json` | `a7cde3de670568edc191d78a4db5992c39519e3f` |
| E03 | `diplomatic/recovery/2026-09-27-task-records/dzongsar_middle/finalize.py` | `f8bb6613e89cffa85ea1236b799d8ce386c0dc9a` |
| E04 | `diplomatic/recovery/2026-09-27-task-records/dzongsar_middle/RECOVERY-PROVENANCE.md` | `d13560cb9b10fc622b8f2494ae754fc85b910123` |
| E05 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tingkye-early-omission-claims.retained-tool-output.txt` | `63d1726404f47b1fa05d104cdb81be7fa3b84008` |
| E06 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tingkye-early-native-metadata.retained-tool-output.txt` | `6a14982b28d8785438fb29a1ac17c09c3a4e41ae` |
| E07 | `diplomatic/recovery/2026-09-27-task-records/dzongsar_middle/retained-context-quotations.md` | `e18e6b5a465ef96abbc15bcb3f008dd2219f0bb6` |
| E08 | `diplomatic/recovery/agent-originals/w1er119_ch1/save-tingkye-early-audit.py.retained-source` | `ea8407a101ac4065edb4dce77c4bd6a40b36b063` |
| E09 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/w1er119-import-audit.replayed.json` | `c03f98ddbea6552b0bcea99e532231d9e109ea0a` |
| E10 | `diplomatic/recovery/2026-09-27-task-records/dzongsar_late/root-final-audit.original-tool-output-excerpt.txt` | `64db7ea880d53f133f0661ef7f8e2e2358a391f4` |
| E11 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tingkye-early-fourth-correction.BLOCKED-retained-source.py.txt` | `561b3f7cda761f2d78201a9d10b93a52bb5f2217` |
| E12 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/PROVENANCE.json` | `3f6fb24e9514909204c41adcf4277efb12ac7d0b` |
| E13 | `diplomatic/recovery/2026-09-27-task-records/langtang_ch1/context-summary-limits.md` | `2c37f62b16d5249a79142175c6c6f09340c34521` |
| E14 | `diplomatic/recovery/2026-09-27-task-records/dzongsar_late/langtang-junction-audit.original-tool-output-excerpt.txt` | `a47fd2b4d486f5b3cd553f892888004885be4f40` |
| E15 | `diplomatic/recovery/2026-09-27-task-records/gadkar_ch1/retained-outage-messages.md` | `f4f107b463990fa75277658fdcd75a41e6950cb9` |
| E16 | `diplomatic/recovery/agent-originals/gadkar_ch1/retained-successful-checkpoint-44-47.py` | `caf08320fbbed308f911da3b5ade23e135f20749` |
| E17 | `diplomatic/recovery/agent-originals/gadkar_ch1/retained-failed-checkpoint-48-51.py` | `e9d380224db1be7a398a660a1e4bd7fbb955f41d` |
| E18 | `diplomatic/recovery/2026-09-27-local/retained-fragments/tharpaling-44-47.json` | `47defe333712f462a01ac64861116d83136568de` |
| E19 | `diplomatic/recovery/2026-09-27-local/retained-fragments/tharpaling-48-51-unsaved.json` | `8f9ab98a8e3d02f85522065aeb4b2aaa91b83e16` |
| E20 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tharpaling-late-attempt.stage1-saved-construction.py.txt` | `680bb3bed2c442058c4d4d80518208ecd73841de` |
| E21 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tharpaling-late-attempt.stage2-copy-saved.py.txt` | `b16dab0affb4091294607e38a447a36a0ee3f9bd` |
| E22 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/tharpaling-late-attempt.stage3-saved-withdrawal.py.txt` | `26dce263a3d8d7f0ca4215f549aa83a35c0c64e3` |
| E23 | `diplomatic/recovery/2026-09-27-task-records/langtang_ch1/finalize-middle.py.txt` | `9fd8ed55b1b426f2dc5ea0adad8291d43879d9bd` |
| E24 | `diplomatic/recovery/2026-09-27-task-records/langtang_ch1/checkpoint.py.txt` | `e67e768ffa312c3ddae77095a9dd36f009be1a3c` |
| E25 | `diplomatic/recovery/2026-09-27-task-records/langtang_ch1/gcn-final-unsaved-handoff.txt` | `35719dc00ffabc9948ffc99c07338ca30a6486da` |
| E26 | `diplomatic/recovery/2026-09-27-task-records/zhichen_ch1/transcript-replay/gcn-late.json` | `98988e0747b780ce7853a4e8f25670000c64538b` |
| E27 | `diplomatic/recovery/2026-09-27-task-records/zhichen_ch1/transcript-replay/gcn-late.md` | `fe512690051bca999e800356764a6dbd36f9193f` |
| E28 | `diplomatic/recovery/2026-09-27-task-records/zhichen_ch1/gcn_late_report.final.py` | `0455c5676c30359374d91c61b75af458f6b667ca` |
| E29 | `diplomatic/recovery/2026-09-27-task-records/zhichen_ch1/gcn_late_report.amendments.txt` | `9aedf55af8802c673790793e3c9dbe7a70ed5f63` |
| E30 | `diplomatic/recovery/2026-09-27-task-records/zhichen_ch1/manifest.json` | `9ab023c74c1f3be44e29e3a851a861148e4dc554` |
| E31 | `diplomatic/recovery/2026-09-27-task-records/dzongsar_late/audit-excerpts-provenance.json` | `4dcea0bd7f8baa47b920309b0544c04c61192746` |
| E32 | `diplomatic/recovery/agent-originals/dzongsar_late/preserved-20260927T164952Z/retained-tool-call-text/integration-final-audit-record.initial.py.txt` | `ff1fc88956dacf0f48896f6845cb5d57f40a17e5` |
| E33 | `diplomatic/recovery/agent-originals/dzongsar_late/preserved-20260927T164952Z/retained-tool-call-text/integration-final-audit-record.amendment.sh.txt` | `eabfe7714288943efc5ac45aeb611f0e8000f4e2` |
| E34 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/w1er119-import-audit.replayed.md` | `81bec68e3120a18489e30eeb7df45575fe2fbe2b` |
| E35 | `diplomatic/recovery/2026-09-27-task-records/w1er119_ch1/w1er119-import-audit.saved-construction.py.txt` | `f27b8e17bfd9d6af1ac0b3374ad0d0866c0ee4be` |

## Remaining source routes and limits

- **Original cloud workspace:** Unavailable in current environment context; original storage/snapshot recovery is not exposed through current tools. Original filesystem/snapshot containing the missing reports, apparatus, and uncommitted evidence. Reusing the same path in a fresh runtime does not recover old bytes.
- **Retained original agent task records:** Exact source/output recovered through reactivated original tasks. Some prior text has been compacted and only summaries remain. Any still-retained original tool input/output or full original task transcript. Do not fabricate missing report records from summaries.
- **Connected local project directories and linked conversation record:** Root reports the local main checkout is clean at afb5c51 and exact project searches found no additional missing report files. The saved read_thread response for the linked ChatGPT conversation contains only five recent user/final turns, not the original work logs. A complete original report copy or original tool-history payload if one becomes available. These current local checks do not prove all historical cloud storage is gone.
- **Reachable Git history:** Original recovery audit found none of the 54 report basenames in reachable history. Current recovery branch now preserves transcript-derived material listed above. A previously unavailable original commit/blob or branch containing the actual original reports. Existing replay blobs must not be mislabeled original filesystem recovery.
- **Outer-scratch split archive:** Incomplete; only the existing prefix has been salvaged. Manifest lists 169 raster files plus crop-map.json, map_crops.py, ch1-ewts.txt and tingkye-qc-read.txt; none of the 54 missing report bodies. Original missing 75 archive parts to restore the complete outer-scratch archive. Even a complete archive would not, by its manifest, restore these 54 report bodies.
  The archive has 85 declared parts, 10 verified present, and 75 missing (010–084; 157,252,187 bytes). Full archive SHA-256: `9475b82b7dae79239437f22f5d7cc408bae699867d25eb5b9b8b582f5dea4cd3`.

## Use of recovered records

Preserve historical errors and their withdrawals together. Do not rerun old integration scripts against the current apparatus and describe the result as the lost historical report. In particular, the integration audit depends on the missing 1,024-observation snapshot, the middle signs and Gcn finalizers depend on earlier ledgers, and the Tharpaling attempted-reading report depends on missing extracted-page metadata. Literal root-final and Langtang-junction stdout omitted `evidence_sha256`; their original Markdown text is not present.

This snapshot may be updated when further exact retained sources are committed. It does not count expected future blobs as recovered content.
