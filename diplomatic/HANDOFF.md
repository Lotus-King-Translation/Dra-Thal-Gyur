# Continue the diplomatic edition

> **Active chapter: Chapter 2 bounded v1 (authorized 2026-09-30).** Continue at [chapter-02-v1/README.md](chapter-02-v1/README.md) and its fixed source plan. Report status with every verified commit. Do not modify the tagged Chapter 1 release or reopen its completed checklist.

> **Chapter 1 bounded v1 is complete for the user-approved scope (2026-09-30).** Start with the [released edition](release-v1/README.md), [final validation](release-v1/VALIDATION.json), and [status report](release-v1-proposal/PROGRESS.json). All 183 release choices are recorded; the eight frozen packets are dispositioned as two integrations and six explicit deferrals without collation credit; all five deliverable groups are present. Exhaustive witness collation remains unfinished. Run `python3 diplomatic/tools/release_progress.py --repo .` and report status with every verified commit. Do not reopen the completed v1 checklist or commission general reading under its name.

**Start here on `main`. The approved Chapter 1 v1 is released; the exhaustive research dossier remains unfinished.** Its Markdown edition, integrated apparatus, surviving review ledgers and recovery archives are preserved together. Historical recovery branches remain available; they are not separate active work queues. Finish and remotely commit Chapter 1 before starting Chapter 2, then continue chapter by chapter.

## Preservation checks and historical exhaustive workflow

The v1 build and final gate are in `release-v1-proposal/build_release.py` and `validate_release.py --require-final`. Instructions below preserve the earlier exhaustive project and its exact uncertainties; they are not additional prerequisites for the released v1. Chapter 2 has not been started.

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
5. Open [WORK-QUEUE.json](WORK-QUEUE.json) and follow its current batch IDs. **The preserved-report integration backlog is cleared:** the eight CONTINUE2-W02 reports, twenty-one CONTINUE2-W03 reports, and four subsequent new-reading reports are integrated within their stated limits. Do not recreate them. Adzom physical PDF3–13 has bounded physical ledgers; PDF1–2/title/portrait remains partial. Next new Adzom physical page is PDF14/U00277; Tingkye PDF14/U00464; Tsamdrak PDF24/U00682; Degé PDF12/U00539 continuation. Dzongsar's three local rechecks extend existing records rather than duplicating them. [Continued integration receipts](reviews/chapter-01/continuation/SESSION-20260929-INTEGRATION-CONTINUED/README.md) distinguish recovered drafts, integrated reports, and unadopted candidates. Keep U01239, U01286 and all exact base/witness component questions visible. U00156/U00179/U00184/U00197 draft candidates remain pending; report integration did not silently change their Tibetan or punctuation. The earlier page7 rejection of22 proposed shad deletions and S09 raw-incipit rejection remain authoritative within their saved scope. Reassign a stale owner only after preserving its files and recording the handoff.

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

## Historical preserved-report integration snapshot

All previously captured page reports are integrated. [Adzom physical](reviews/chapter-01/continuation/C1-BASE-PHYSICAL.md) reaches the PDF13 inspection; [Tingkye](reviews/chapter-01/continuation/C1-TINGKYE.md) reaches PDF13; [Tsamdrak](reviews/chapter-01/continuation/C1-TSAMDRAK.md) reaches PDF23; [Degé](reviews/chapter-01/continuation/C1-DEGE.md) reaches PDF11. These are inspection/comparison frontiers with exact unresolved components, not claims that every glyph has been resolved. Earlier target/flank distinctions remain in each batch.

Proceed with genuinely missing bounded source coverage, retaining all named local uncertainties, existing main lexical passes and rejected hypotheses. The recovered draft was preserved at `d46ce1579d962c9af78b220534b59bf8942b02c2`; its proposed canonical changes remain separate from adopted edition readings. Current ownership and exact next spans are in the queue. Chapter1 is unfinished; Chapter2 has not started.
