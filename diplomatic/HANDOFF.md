# Continue the diplomatic edition

**Start here on `main`. Chapter 1 is unfinished.** Its Markdown edition, integrated apparatus, surviving review ledgers and recovery archives are preserved together. Historical recovery branches remain available; they are not separate active work queues. Finish and remotely commit Chapter 1 before starting Chapter 2, then continue chapter by chapter.

## Start a session

Use Python 3.11 or newer and Git. The chapter build and validation use only the standard library. Git LFS is needed to fetch scans; the separate full asset verifier additionally needs `pikepdf`.

1. Read the repository [agent instructions](../AGENTS.md), this handoff and the [work status](WORK-STATUS.md). The latter distinguishes saved coverage from unfinished reading. Read the [method](METHOD.md) before making editorial decisions.
2. Inspect `git status --short --branch`, including untracked files. If earlier work is present, preserve it on a new recovery branch and verify the remote checkpoint **before** checkout, regeneration, synchronization or cleanup. Never discard interrupted reports, crops or failed-reading evidence. Only the coordinator publishes while collaborators are working.
3. On a clean checkout, fetch and fast-forward to `origin/main`. Verify the branch SHA through Git or the GitHub connector. Do not use an old recovery branch as the current base. If local and remote histories differ, inspect both; do not reset or force-push.
4. Run the read-only checks from the repository root, before building:

   ```bash
   python3 diplomatic/tools/validate_chapter1.py --repo . --check
   python3 diplomatic/tools/build_chapter1.py --repo . --check
   ```

   Stop to understand a failure. A stale generated file is a synchronization problem, not permission to overwrite evidence. These commands check recorded structure, hashes and reproducibility; they do not certify manuscript readings.
5. Open [WORK-QUEUE.json](WORK-QUEUE.json) and follow its current batch IDs. The eight older CONTINUE2-W02 reports are now integrated: Adzom physical PDF4–7, S09/PDF102, Tingkye PDF5, Tsamdrak PDF15 and Degé PDF3. Their exact unresolved components remain visible; integration is not complete-witness certification. Next integrate the **21 already saved CONTINUE2-W03 reports**, beginning with Adzom physical PDF8–13, then Tingkye PDF6–10, Tsamdrak PDF16–20 and Degé PDF4–8, in bounded groups. Do not recreate these reports or execute the interrupted historical integration script. The [current session receipts](reviews/chapter-01/continuation/SESSION-20260929-INTEGRATION/startup.json) identify the verified raw outputs. Retain the page7 rejection of22 proposed shad deletions; the mistaken raw incipit at S09 is also rejected. U01239 remains blocked, and U01286 note letters/signs and named title/heading questions remain open. Reassign a stale owner only after preserving its files and recording the handoff.

For a dirty inherited tree, create a uniquely named local recovery branch at the current HEAD with `git switch -c recovery/YYYYMMDD-HHMM` (choose an unused name). Review and stage all project work, including untracked reports/evidence, then commit it and use `git push -u origin HEAD` to create that remote branch. Verify it with `python3 diplomatic/tools/checkpoint.py --branch recovery/YYYYMMDD-HHMM --verify-only` before any further changes. The normal checkpoint helper expects the target remote branch to exist. With connector-only access, create the recovery branch at the preserved parent, publish the entire reviewed snapshot there, and verify its ref instead.

If shell authentication is unavailable, use the connected GitHub tools for the same reads and non-forced publication steps. A local checkout can be stale even when a previous chat says it is synchronized. Read the actual remote ref.

## Know which files govern which claims

| File or directory | Role |
| --- | --- |
| [WORK-STATUS.md](WORK-STATUS.md) | Human account of saved coverage, known gaps and recovery limits. Update when supported coverage changes. |
| [WORK-QUEUE.json](WORK-QUEUE.json) | Current task ownership, exact candidate IDs, next bounded work, input/output paths and completion criteria. Keep all candidate rows, including completed ones. |
| [CONTINUATION.json](CONTINUATION.json) | Authored continuation and recovery metadata copied into generated status. |
| [collation/chapter-01](collation/chapter-01/) | Curated source comparisons, corrections, insertions, coverage and witness ledgers. Read the queue's `decision_destinations` before editing. |
| [reviews/chapter-01](reviews/chapter-01/) and [evidence/chapter-01](evidence/chapter-01/) | Review reports and the exact source images that support them. New continuation batches have explicit destinations in the queue. |
| [chapter-01.md](chapter-01.md), [STATUS.json](STATUS.json), `reading-units.json`, `editorial-decisions.json` | Generated products. Edit their authored inputs, then rebuild; do not maintain a second hand-edited edition. |
| [recovery/README.md](recovery/README.md) | Archive index and provenance boundaries. Archived scripts are historical evidence; do not execute them to regenerate current work. |

The machine-readable reading needs **both** `reading-units.json` and `ch1-scan-insertions.json`. The former alone omits restored material. Full source paths, manifests and witness relationships are in [SOURCES.md](SOURCES.md). Materialize the exact required Git LFS sources before inspection; a pointer file is not a scan. Record an access failure precisely instead of claiming the page was read. For the next batch, run `git lfs pull --include="editions/adzom-2000/sgra-thal-gyur.pdf,editions/adzom-2000/original-images.zip"` and compare both SHA-256 values with `pdf_sha256` and `zip_sha256` in `editions/adzom-2000/image-manifest.json`. These two objects were successfully fetched and hash-verified during the 2026-09-28 restart audit; a fresh checkout must verify its own files.

## Do one small batch and preserve it

The queue contains six batches of five punctuation candidates, followed by base-layer/sign tasks and explicit witness gaps. Its `protocols` specify the required report fields and acceptance criteria. For broader witness tasks, start with the named `first_batch`, then proceed in at most five source pages at a time. If one reading is blocked, save its exact obstacle and next step; continue another eligible bounded task. Dependencies give the preferred order, not a reason to abandon other useful work.

For the next punctuation batch, create the planned JSON/Markdown report under the active task's `reviews/chapter-01/continuation/` path and save new context/crops under its `evidence/chapter-01/continuation/` path. Record the source hash, native member, page/row, crop bounds and **actual neighboring Tibetan sequence** before proposing a sign correction. A matching image hash does not prove that a crop belongs to its labeled anchor. Inventory all marks across each unit boundary separately from assigning them to the preceding or following unit, so no printed sign is lost or duplicated. Preserve the historical crops even if their labels prove wrong.

Save partial reports and evidence immediately inside this repository, at the queue's report/evidence paths. Scratch folders and chat messages are not durable handoff storage. Inspect ignored files with `git ls-files --others --ignored --exclude-standard` as well: unfinished project evidence named `.tmp` or `.part` must be preserved explicitly, while caches and credentials must not be staged. Subagents notify the coordinator as soon as a small batch exists, including uncertain or failed findings; they do not accumulate unpublished work. Integrate supported decisions in the authored collation files specified by `decision_destinations`, with rationale and evidence. Then run:

```bash
python3 diplomatic/tools/build_chapter1.py --repo .
python3 diplomatic/tools/validate_chapter1.py --repo .
python3 diplomatic/tools/build_chapter1.py --repo . --check
```

Update queue dispositions, report links, exact remaining spans and the next task. Keep unresolved candidates `blocked`; they are not agreement. Review every diff and all untracked project files. Once all agents have saved and paused writing, stage the reviewed reports, evidence, authored inputs and generated outputs explicitly. The coordinator then runs:

```bash
python3 diplomatic/tools/checkpoint.py --branch main --message 'Checkpoint Chapter 1: bounded review'
```

The helper requires a fully staged working tree, publishes without force, and verifies the remote SHA. A failed push is an unfinished preservation checkpoint: resolve publication before the next substantial batch. With connector publication, create blobs/tree/commit on the freshly read remote parent, update the branch without force, read the ref again and verify its SHA; synchronize the checkout to that verified tree. Never report a local commit or uploaded blob as remotely saved.

Record a verified batch SHA in the next queue/report update; the live Git ref remains the authority for the current checkpoint. Do not put a commit's own unknown hash inside its files. End each session with a verified remote checkpoint and a next task that another agent can execute from the repository alone. The [restart audit](RESUME-AUDIT.json) records the setup checks performed on 2026-09-28; rerun current checks instead of treating that historical receipt as today's result.

## Do not restart preserved work or erase uncertainty

The Adzom and Dzongsar main lexical passes survive within their stated scopes. Use those ledgers; finish their signs, annotations and named uncertainties. The old readiness audit and recovery packet contain historical counts. Current coverage is in WORK-STATUS, current metrics are generated in STATUS, and the queue tracks unfinished actions. Historical claims are not fresh certification.

Recovery still has **54 original report identities: four complete transcript-replayed bodies and 50 incomplete bodies**. That is not a percentage of research time lost. Read the archive index before further recovery; repeat searches only when a new source becomes available. A failed-reading replay, partial template or summary cannot substitute for a missing continuous collation.

The final queue task, `C1-COMPLETION-GATE`, applies the method's full chapter criteria. Passing software checks alone does not close it. All observed conflicts need traceable dispositions, all declared physical spans need evidence or a precise source/access limitation, and unresolved readings must stay visible. Only then mark Chapter 1 complete, commit and verify that state remotely, and begin Chapter 2.

## Current preserved-report integration

The eight preceding page reports are integrated with their exact limitations. [Adzom physical](reviews/chapter-01/continuation/C1-BASE-PHYSICAL.md) reaches the saved PDF7 inspection; [Tingkye](reviews/chapter-01/continuation/C1-TINGKYE.md) reaches PDF5; [Tsamdrak](reviews/chapter-01/continuation/C1-TSAMDRAK.md) reaches PDF15; [Degé](reviews/chapter-01/continuation/C1-DEGE.md) has PDF3's bounded reading. These are inspection frontiers with unresolved components, not whole-page glyph certificates.

The next21 target-page outputs, including their exact sources, have already been remotely preserved. Integrate them in groups of at most five target pages, retain all disagreement and uncertainty, then commission only genuinely missing work. Current ownership and exact remaining spans are in the queue and individual task ledgers. Chapter1 is still unfinished; Chapter2 has not started.
