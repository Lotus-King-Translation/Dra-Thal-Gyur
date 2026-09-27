# Gadkar / Langtang / Tharpaling agent preservation

Recovery only, 2026-09-27. No new collation or scan reading was performed.

The original scratch files are absent from the replacement workspace. The two Python files here preserve the exact Python heredoc bodies visible in this agent's retained tool-call history. They have not been executed during recovery. They are transcript recoveries, not recovered original filesystem files and not complete reports.

- `retained-successful-checkpoint-44-47.py`: the original tool call completed with exit code 0; it appended Tharpaling PDF44–47 page records and TH-LATE-003 to a pre-existing `tharpaling-late-notes.json`. That pre-existing JSON is not available here.
- `retained-failed-checkpoint-48-51.py`: the original tool call failed before process creation with `409 Conflict, environment_offline`. This preserves the submitted text for PDF48–51. It is not evidence that those records reached the original JSON file.

These scripts depend on missing prior JSON content and append records; executing them would modify a report and could create duplicates. They are being preserved as source text only.

No complete Gadkar, Langtang-late, Tharpaling-middle, Tharpaling-continuation, or Tharpaling S01/S02/S03 correction report body survives verbatim in this agent's currently visible tool history. Earlier compacted state contains summaries and named paths, which may be preserved separately with that weaker provenance. Repository-integrated reports and crops already present are not represented here as original scratch files.
