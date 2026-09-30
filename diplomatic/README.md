# Dra Thal Gyur — Chapter 1 bounded v1

**Chapter2 bounded v1 is also released:** [reading and deliverables](chapter-02-v1/release/README.md), [progress](chapter-02-v1/PROGRESS.json), and [validation](chapter-02-v1/release/VALIDATION.json). Its explicit scope is targeted source corrections and exact electronic comparison, not complete scan proofreading.

**Read the completed Chapter 1 v1:** [Release overview](release-v1/README.md) · [Reading text](release-v1/reading.md) · [Apparatus](release-v1/apparatus.md) · [Changes](release-v1/CHANGES.md) · [Coverage and uncertainty](release-v1/COVERAGE.md).

**Preservation and continuation:** [HANDOFF.md](HANDOFF.md) gives the restart checks, next task and verified checkpoint procedure. `main` contains the edition and all preserved recovery archives. The [work ledger](WORK-STATUS.md) records saved coverage; the [work queue](WORK-QUEUE.json) records what to do next; the [recovery index](recovery/README.md) explains historical evidence and missing records.

**Chapter 1 v1 is complete for the user-approved bounded scope.** The release contains 183 explicit passage decisions, all 13 restored main verses, 88 intervention/source-layer/uncertainty records and 682 scoped comparison observations. Two frozen packets were integrated; six were explicitly deferred without collation credit. This does not certify exhaustive witness collation or a reconstructed original. The older working dossier remains available separately. Chapters 2–6 and the final colophon have not been started here. The original editions, source files, glossary, and translation are unchanged.

The second reading has checked the continuous Adzom main-Tibetan sequence and audited interleaved annotations. The comparison extension now covers Dzongsar’s complete Chapter1 main sequence with local uncertainty flags and records further witness attempts. It has also documented a concrete limit: the current readings cannot certify continuous all-variant collation of several comparison witnesses. Those exhaustive research limits remain explicit; they do not reopen the separately approved and completed v1 release gate.

## Read the current work

- [Chapter 1 v1: released reading and apparatus](release-v1/README.md)
- [Historical working dossier and exhaustive apparatus](chapter-01.md)
- [Source inventory and coverage limitations](SOURCES.md)
- [Editorial method](METHOD.md)
- [Machine-readable chapter status](STATUS.json)
- [Continuation instructions and reproduction](HANDOFF.md)
- [Second-reading findings and limits](reviews/chapter-01/second-reading.md)
- [Annotation audit](reviews/chapter-01/annotation-audit.md)
- [Continuous base coverage](collation/chapter-01/scan-coverage.json)
- [Current comparison progress and limits](reviews/chapter-01/comparison-extension.md)

The apparatus distinguishes exact supplied-transcript differences from readings actually checked in a facsimile. An uncollated witness is never represented as agreeing with Adzom. Missing access and unreadable text are not silently treated as omissions by a witness.

## Governing source and decisions

The repository already selects **Adzom W1KG11703, volume 1** as its base, with the **printed scan governing**. This edition follows that decision. A diplomatic text records that witness; it does not silently select a majority or more familiar reading from other witnesses. Every correction to the working Adzom transcription needs a scan locator and a recorded reason. Alternative readings remain visible even when the Adzom reading is retained.

The working text preserves supplied readings pending verification and explicitly inserts individually verified scan-only material. Its unverified title/sign portions and expressly uncertain readings remain provisional. A lexical comparison is not a certification of every physical punctuation sign. The prose reasons in the apparatus are editorial dispositions, not assertions that every printed witness has been read or that the retained reading is the author's original.

## Release and research gates

The approved bounded v1 gate is documented in [PLAN.json](release-v1-proposal/PLAN.json) and checked by [the release validator](release-v1-proposal/validate_release.py). Its final acceptance is distinct from the historical exhaustive gate below. All named uncertainties remain visible; no general manuscript comparison is newly claimed.

### Historical exhaustive gate

Complete and validate Chapter 1 before starting Chapter 2. Repeat this gate for each subsequent chapter. A chapter can be marked complete only after its declared witness coverage has been checked, its base transcription has been proofread throughout, all observed differences have apparatus entries, and all outstanding unreadable or unavailable spans are precisely recorded. A mechanical round-trip check establishes transcript coverage, not philological completeness.

Source baseline: [`e17a496ad7532cc627f9ba288b541f7a53efd002`](https://github.com/Lotus-King-Translation/Dra-Thal-Gyur/commit/e17a496ad7532cc627f9ba288b541f7a53efd002). Created 2026-09-27.
