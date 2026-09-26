# Dra Thal Gyur — annotated working translation

## Current state

See [CONTINUATION.json](CONTINUATION.json) for the first unprocessed unit, [PROGRESS.json](PROGRESS.json) for chapter coverage, and [COVERAGE.csv](COVERAGE.csv) for every e-text unit. The checkpoint recovered on 26 September 2026 contains U00001–U04000 of 5,466 units: two chapters drafted through their endings, chapter three in progress, and 1,466 units not yet processed.

This is a source-aligned working draft, not a publication-ready edition or independent QC. A represented unit may contain an unresolved reading or provisional wording. The two scan-only records include one untranscribed annotation at the chapter-one/two transition.

## Files

- [data/](data/) preserves exact source units and numbered English JSONL batches.
- [notes/](notes/) contains source-linked review records, terminology proposals, scan decisions, and translation corrections.
- [RUN.json](RUN.json) identifies the source, glossary and guidance by checksum and states the checks and limitations.
- [update_bookkeeping.py](update_bookkeeping.py) regenerates progress and coverage from the files rather than from a manually entered count.

## Assembly rules

Read English batches in numerical order. Apply explicit `english` replacements from `notes/scan-decisions.jsonl`, then from `notes/translation-decisions.jsonl` in file order. Other scan-decision records describe readings already used or unresolved; they are not instructions for automatic semantic rewriting. Preserve all note markers and source locators.

Run from the repository root:

```sh
python3 translations/2026-09-26-full-draft/update_bookkeeping.py
```

The source, established glossary and guidance remain unchanged. Terminology proposals remain unapproved. The source e-text is an aid to the selected Adzom facsimile, not a fully proofread diplomatic transcription. Scan consultation does not certify full collation, and mechanical coverage checks do not certify meaning.
