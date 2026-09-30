# Chapter 4 — bounded v1 work

Chapter 4 starts only after the remotely verified Chapter 3 release, `chapter-03-v1.0.0` at `17abe1f0e68069406f782a77e93dab10841b81fb`.

The fixed scope preserves 458 original anchors U04306–U04763. Exact A/B/S comparison produces 61 differences in 33 readable loci. The related W reference has 55 non-equal blocks. Eight targeted source checks cover chapter boundaries, possible missing question verses, source-note layers, the first reply heading, and two local word questions. Candidate page numbers are locators, not claims of completed inspection.

[Plan](PLAN.json) · [Progress](PROGRESS.json) · [Exact comparison](collation.json) · [W ledger](wikisource.json)

The release gate is 33 passage decisions, 55 W decisions, eight source dispositions, five deliverable groups, final tests, source-bound signoff and verified commit/tag publication. Uncertainty can remain explicitly recorded. Whole-witness collation, a full physical proofread and reconstruction of an original text are not hidden prerequisites.

Run `python3 diplomatic/chapter-04-v1/progress.py --repo .` after each batch and publish its report with every verified remote commit. Preserve all earlier releases. Original source strings are never overwritten; corrections and insertions go into separate authored records.

Two initial combined terminal-read requests failed a platform safety-status check before execution. Standard file reading and shorter terminal reads then succeeded. The [access record](checkpoints/0000-tool-access.json) remains; no failed attempt receives reading credit.

Next: inspect the frozen source targets, then record passage-specific decisions. The completed electronic alignment is not itself scan verification.
