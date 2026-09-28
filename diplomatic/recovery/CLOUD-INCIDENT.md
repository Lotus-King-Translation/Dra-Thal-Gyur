# Cloud work preservation incident — 2026-09-27

Prepared 2026-09-28. This is a factual incident record and a draft request for an OpenAI-side investigation. It has not been submitted to Support. It does not establish that a recoverable server-side snapshot exists.

## Requested investigation

Determine whether retained hosted execution state, snapshots, or original task/subagent records still contain the missing project files. Preserve any available associated state while investigating. If recovery is possible, export the original files or exact original tool inputs/outputs without replacing the current Git repository.

The work was performed in ChatGPT Work cloud infrastructure. Recovery of the original cloud workspace must not depend on a backup on the user's computer. A later agent used a connected local machine during salvage; its work folder is a separate recovery artifact.

## Identifiers

| Item | Observed value |
|---|---|
| Conversation | https://chatgpt.com/c/6ab8b470-01a0-83eb-90b7-9219f2662cff |
| Conversation title | Root Tantra Diplomatic Edition |
| Repository | https://github.com/Lotus-King-Translation/Dra-Thal-Gyur |
| Affected work date | 2026-09-27; the exact first-disconnection time is not established by the retained evidence |
| User timezone | Europe/Helsinki |
| Reported workspace path | `/workspace/scratch/a117ee885aff` |
| Reported environment ID | `ccarenv_b64_Y2NhcmVudl82YTkxMmNjNDkzZTQ4MTkxYWI4YzExZGE2YjQzZmMyZg` |
| Observed failure | `exec-server connection attempt failed: environment registry request failed (409 Conflict, environment_offline): Environment is not connected.` |
| Current edition baseline | `afb5c5133357942267dc55fc60a1d22704d5ef08` |
| Current edition file SHA-256 | `927d6b36c7d105efa2857ef5f2392fcf5f2f6b54f287f6c8139d43663fe51c40` |

The reported environment ID and path identify an observed connection. Their reuse does not establish that the original filesystem was restored or that this ID identifies every earlier execution. Please resolve the actual hosted execution history from the conversation and task associations.

Original task names included `/root/base_ch1_annotation_audit`, `/root/base_ch1_continuous_early`, `/root/base_ch1_continuous_late`, `/root/dzongsar_late`, `/root/dzongsar_middle`, `/root/w1er119_ch1`, `/root/zhichen_ch1`, `/root/chapter1_etext_collation`, `/root/langtang_ch1`, `/root/gadkar_ch1`, and `/root/editorial_method`. This list describes retained task references, not a complete platform execution manifest.

## What is missing and what survives

The original recovery audit listed 54 absent report filenames. Many are JSON/Markdown pairs; this count is not a percentage of the day's work or a count of independent scholarly checks.

Four report bodies were later reproduced from retained literal construction text. Fifty complete bodies remain unavailable, with varying amounts of partial source and summary evidence. No byte-identity claim has been established for any of the 54 pre-loss original report files.

The [54-file matrix](https://github.com/Lotus-King-Translation/Dra-Thal-Gyur/blob/d510250e83efcbb6c56ac3b6ee0a89140f6e006b/diplomatic/recovery/2026-09-27-task-records/missing-report-recovery-matrix.json) identifies the filenames and surviving evidence. The current work ledger is [WORK-STATUS.md](../WORK-STATUS.md); it distinguishes preserved edition work from claims requiring renewed verification.

A missing historical apparatus snapshot with reported 1,024 comparison observations is referenced by retained integration code. That count is historical and is not the currently integrated total. Recovery should include its dependencies if they survive.

## Completed recovery checks

- Retained original-agent tool inputs, outputs, corrections, and handoffs were archived. Exact original records were distinguished from compacted summaries and generated replays.
- Available project Git history and objects were inspected. The later cloud clone had no unreachable objects, stash, alternate object store, or additional worktree containing the missing original report bodies.
- Its reflog starts with a clone of baseline main on 2026-09-27 at 21:45:50 +03:00. Reconnecting this later clone did not recover the earlier worktree.
- The reconnected workspace's 43 untracked recovery files were preserved as an exact remote full-tree snapshot at `84df27116ea8faf4c441ecccb1e2ffda23e16f54` on `recovery/reconnected-2026-09-28`. Local and remote tree hashes both equal `c5f33680244ac7dcfdc05ce1e0e4311e4061273f`.
- Recovery was consolidated on `recovery/task-records-2026-09-27`; checkpoint `d510250e83efcbb6c56ac3b6ee0a89140f6e006b` includes the latest partial Markdown templates.
- The older outer-scratch archive has only parts000–009 of85. Parts010–084 remain absent. Its manifest does not list the54 report bodies, so restoring that archive alone would not resolve the missing reports.
- The agent has no exposed operation to enumerate or restore earlier hosted execution snapshots or to retrieve full internal task logs. No private platform endpoint or credential workaround has been attempted.

## Questions for OpenAI

1. Are any earlier hosted filesystem states or snapshots retained for the conversation and associated tasks from 2026-09-27?
2. Was execution state replaced, disconnected, or restored during the observed failures, and which state was made available afterwards?
3. Can the original project and scratch files, including untracked reports/evidence, be exported from retained state?
4. If filesystem recovery is unavailable, are exact task/subagent tool-input and tool-output records available through a supported export that preserves untruncated report-generating content?
5. If neither is available, can the unavailable scope and applicable retention/lifecycle outcome be confirmed so rework can proceed on a defined basis?

## Documentation and limits

[Official ChatGPT Work cloud-security documentation](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-cloud-security), checked2026-09-28, describes hosted execution as OpenAI-managed and states that execution state/snapshots have a separate lifecycle from conversations and saved files. This supports requesting an investigation of hosted state. It does not confirm a retained snapshot for this incident or provide this agent a restore operation.

No support request has been sent, no restore has been initiated, and successful server-side recovery cannot be promised.
