# Dra Thal Gyur — annotated working translation

**The first draft now represents all 5,466 e-text units, all six chapters, and the closing material.** No e-text unit remains unprocessed. Some words, numerical groupings, source readings and constructions remain explicitly unresolved; the scan-only annotation S0002 is still untranscribed. This is not a publication-ready edition or independent QC clearance.

## Read the translation

[Complete English working draft](Dra-Thal-Gyur-English.md)

[Chapter 1](draft/chapter-01.md) · [Chapter 2](draft/chapter-02.md) · [Chapter 3](draft/chapter-03.md) · [Chapter 4](draft/chapter-04.md) · [Chapter 5](draft/chapter-05.md) · [Chapter 6](draft/chapter-06.md) · [Closing material](draft/closing-material.md)

Every unit links to its [Tibetan alignment](alignment/). [Review notes](REVIEW-NOTES.md) include exact source quotations and actionable questions. [Scan-only material](SCAN-ONLY.md) is recorded separately, with retained image evidence for the unread annotation.

## Records and limits

[Handoff](HANDOFF.md) · [Run baseline](RUN.json) · [Continuation](CONTINUATION.json) · [Chapter progress](PROGRESS.json) · [Coverage](COVERAGE.csv) · [Assembly checks](ASSEMBLY-CHECKS.json)

[Usage guide](USAGE-README.md) explains the [declared usages](USAGE.csv), [additional review candidates](USAGE-CANDIDATES.csv), [proposed glossary entries](PROPOSED-GLOSSARY.csv), and [proposed uses of existing entries](PROPOSED-USAGES.csv). All proposals remain unapproved. The original eight-column glossary is unchanged.

The selected Adzom facsimile governs. Exact e-text unit IDs and Unicode-character offsets are the reliable locators for this draft. Associated scan pages in notes are not a completed unit-to-page concordance. All 205 scan pages have been opened during the accumulated work, but full diplomatic proofreading and independent semantic QC have not been performed.

## Rebuild

From the repository root, run `python3 translations/2026-09-26-full-draft/update_bookkeeping.py`, then run `translations/2026-09-26-full-draft/build_edition.py` with a Python environment containing `pyewts`. From this directory, verify the package with `shasum -a 256 -c SHA256SUMS`.

Assembly preserves raw English batches and applies explicit English overrides from `notes/scan-decisions.jsonl`, followed by `notes/translation-decisions.jsonl` in record order. Other scan decisions are evidence, not automatic rewriting instructions. [ALIGNED.jsonl](ALIGNED.jsonl) records the assembled result and its provenance.

The earlier 4,000-unit checkpoint was committed and pushed as `9958c716700dcb829a4f6f16d30a351fb17b8d79`. The current package continues that work through U05466. See [HANDOFF.md](HANDOFF.md) for what remains unresolved.
