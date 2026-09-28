# Recovery archive

Start ongoing edition work at [HANDOFF.md](../HANDOFF.md). **`main` is the continuation branch and contains all preserved recovery material.** The September recovery branches are historical checkpoints, not competing active editions. No historical file was deleted or rewritten during consolidation.

The [inventory](ARCHIVE-INVENTORY.json) records the bytes and SHA-256 of every historical file preserved here at consolidation commit `061917d9bc7489d313dbcd428ce743c7c45fa2dc`. These checksums establish the saved snapshot, not identity with unavailable original cloud files. The Chapter 1 validator checks them independently of current edition links.

## What each archive contains

| Location | Meaning and limits |
| --- | --- |
| [2026-09-27-local](2026-09-27-local/README.md) | Earlier preservation, fresh recovery reviews, paused evidence, and superseded sign decisions. Historical reports can disagree with later decisions. |
| [agent-originals](agent-originals/) | Retained agent sources, evidence and checkpoint material; filenames do not establish a complete original report. |
| [2026-09-27-preservation](2026-09-27-preservation/scratch-manifest.json) | Manifest of an 85-part scratch archive; only parts 000–009 survived here. The 75 missing parts must not be assumed restored. This manifest is not the list of 54 missing reports. |
| [2026-09-27-local-agent-work](2026-09-27-local-agent-work/README.md) | A later recovery agent's entire 371-file work folder, with [per-file provenance](2026-09-27-local-agent-work/manifest.json). It is not the lost cloud worktree. |
| [2026-09-27-task-records](2026-09-27-task-records/README.md) | Retained task text, commands, fragments, summaries and four complete transcript-derived report replays. Consult the [54-report matrix](2026-09-27-task-records/missing-report-recovery-matrix.md) before treating a body as recovered. |
| [2026-09-28-recheck](2026-09-28-recheck/README.md) | Reconnection checks, additional retained versions and explicitly incomplete Markdown templates. |
| [Original recovery packet](2026-09-27.md) | Historical recovery account. Its counts are not the current integrated apparatus count. |
| [Cloud incident draft](CLOUD-INCIDENT.md) | What is known about inaccessible cloud state and a proposed support investigation. No request has been submitted and no server restore is established. |

## How to use retained material

Read [WORK-STATUS.md](../WORK-STATUS.md) for current coverage and [WORK-QUEUE.json](../WORK-QUEUE.json) for the next task. The saved edition has 123 comparison records; historical claims of 1,016/1,024 observations do not establish additional integrated readings. Four of the 54 historical report bodies have complete transcript replays; 50 remain incomplete. These file counts cannot measure the fraction of scholarly work lost.

Historical scripts are evidence, not active build tools. Do not execute them, silently fill missing runtime values, repair their text in place, or promote a failed reading into a verified reading. Historical Markdown links preserve their original context and are not required to resolve at the archive's present location. The active index and incident document do have checked links.

If new evidence becomes available, preserve it in a new dated directory with provenance, extend the inventory, and checkpoint it remotely. Integrate supported findings separately into the active collation files, linking the old evidence and recording any superseded claims. Do not restart a recovery search without a genuinely new source to search.
