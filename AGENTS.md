## Translation and QC: required reading order

At the start of each translation or QC turn:

1. Identify the current task, requested coverage, active file versions,
   and latest explicit user-approved decisions.

2. Read **Part I — Translation guidance** of the
   [Tibetan–English translation standard](guidelines/tibetan_translation_standard_v2.md).

3. Read the
   [expanded Tibetan–English glossary](glossary/expanded_tibetan_english_glossary.csv),
   including its introductory status explanation and all eight columns
   of the entries relevant to the requested passage. Consult related
   entries and compounds. Check the entire glossary before proposing
   new terminology. Established mappings remain authoritative;
   proposed supplementary uses are not automatically approved.

4. For QC, also read **Part II — QC procedure** of the
   [translation standard](guidelines/tibetan_translation_standard_v2.md)
   before reviewing.

5. Read any applicable continuation and user-approved decision records,
   then the Tibetan source with sufficient surrounding context.
   For QC, also read the English draft and its annotations.

6. Perform the requested task. A translation request requires translation
   with the prescribed self-check. Reading the QC instructions does not
   itself authorize a separate QC run or a rewrite.

### Active documents and duplicate copies

Use the
[combined translation standard](guidelines/tibetan_translation_standard_v2.md)
as the active procedural document.

The following files are its separate component copies, not additional
reading stages:

- [Translation guidance](guidelines/tibetan_translation_guidance_v2.md)
- [QC procedure](guidelines/tibetan_translation_qc_v2.md)

Do not also load these separate copies when using the combined standard.
Do not use superseded guidance as active policy. If the copies disagree,
report the discrepancy rather than silently combining their instructions.

The
[expanded glossary](glossary/expanded_tibetan_english_glossary.csv)
is a separate required resource; it is not replaced by the combined standard.

The Tibetan source governs what is said. The glossary governs the
established English terminology used to express it. The guidance and
QC procedure govern how the translation is produced, annotated, and checked.

## Remote preservation checkpoints

User instruction, 2026-09-27: preserve work frequently on the remote branch.

- Save each report, evidence batch, or substantive edit incrementally. Commit and push it before beginning the next substantial batch, handing work to another agent, or ending a turn. Do not wait for a chapter to be complete.
- Preserve interrupted and untracked project work on a recovery branch before editing, cleanup, regeneration, or synchronization. Keep archival originals separate from reconstructed material.
- The coordinating agent serializes commits and pushes. Subagents save small batches and immediately notify the coordinator; they must not build a large unpublished backlog.
- Verify the remote branch SHA after every checkpoint. A local commit or uploaded blob alone is not a completed remote checkpoint. If publication fails, report the failure and prioritize preservation before further substantive work.
- Clearly label provisional checkpoints. Frequent preservation does not change the requirement to complete and commit each chapter before beginning the next.
- Never commit credentials, runtime secrets, unrelated personal data, or dependency caches. Preserve project files and evidence without silently dropping unfinished or unreadable material.

### Commit work to remote every step of the way

You must at all times keep committing work to a remote branch. Even small
progress must continuosly be committed.

## Diplomatic edition continuation

Before resuming diplomatic-edition work, read [diplomatic/WORK-STATUS.md](diplomatic/WORK-STATUS.md) for the current saved coverage and remaining work. It links the separate recovery branch and the exact missing-report inventory.

Treat preserved originals, transcript-derived replays, partial templates, and new scan reviews as distinct provenance categories. File counts and archived historical progress claims are not witness-coverage percentages. Use the saved apparatus and explicit page/anchor ledgers when deciding which checks remain; preserve surviving lexical passes instead of restarting them wholesale.
