# Recovery of original task records — 2026-09-27

Recovery branch: `recovery/task-records-2026-09-27`. Baseline main commit: `afb5c5133357942267dc55fc60a1d22704d5ef08`.

## What was recovered

- Exact retained original tool inputs, outputs, corrections, and handoffs from the original task agents. Each agent folder records provenance and limits.
- Complete transcript-derived report payloads for `gcn-late.json/md` and `w1er119-import-audit.json/md`. These four bodies were mechanically recovered from retained literal construction data. They are not byte-verified surviving original report files or newly certified manuscript readings.
- Partial original records for other missing reports, including Tingkye PDF61–69 updates and finalization, Gcn middle finalization, middle base-sign proposals, Tharpaling failed-reading withdrawals, and final audit excerpts.
- The later local recovery agent's entire 371-file work folder (75,574,656 bytes), archived in [../2026-09-27-local-agent-work](../2026-09-27-local-agent-work). Compared with baseline main, 146 file contents totaling 20,001,828 bytes were absent. All371 copied files were checked byte-for-byte locally and their Git blob hashes were matched against the remote archive tree, with zero mismatches.

## What remains missing

See the [54-file recovery matrix](missing-report-recovery-matrix.md) and its [machine-readable companion](missing-report-recovery-matrix.json). Four complete transcript-derived bodies are recovered; 50 complete report bodies remain unavailable. None of the54 original files has established pre-loss byte identity.

Some recovered historical records contain incorrect readings or locators that were later withdrawn. Preserve the records and their corrections together. These archives do not authorize adopting their claims into Chapter1.

The original cloud filesystem remains unavailable. Current tools do not expose restoration of its previous storage or snapshots. The [source-access record](source-access-and-verification.json) records the tested routes and their limits. The earlier outer-scratch archive is also incomplete: only parts000–009 of85 were published; parts010–084 remain missing. Its manifest does not list the54 report bodies.

## Preservation and edition status

The coordinator committed each substantive recovered batch and verified the remote branch after every update. The later local archive was first pushed as commit `4dd344ee4febca7cb117f03519c6ec85ede6e930` on `recovery/local-agent-work-2026-09-27`, then consolidated here.

Main and the diplomatic edition text were not changed during this recovery pass. Chapter1 remains incomplete. No new manuscript collation was performed and no historical integration script was executed against the current edition. Further original recovery requires the missing original filesystem/snapshot or a fuller original task transcript, rather than inference from summaries.
