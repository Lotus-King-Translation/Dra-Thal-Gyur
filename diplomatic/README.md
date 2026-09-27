# Dra Thal Gyur — diplomatic edition in progress

**Workspace interruption, 2026-09-27:** Later evidence and restart notes are preserved in the [recovery checkpoint](recovery/2026-09-27.md). The newer annotated chapter and reports still need integration from the disconnected workspace; the chapter and validation linked below remain the preceding checkpoint.

**Chapter 1 is under collation. No chapter is yet certified complete.** This directory is the working dossier for the requested single annotated diplomatic edition, not a completed golden text. Chapters 2–6 and the final colophon have not been started here. The original editions, source files, glossary, and translation are unchanged.

The second reading has checked the continuous Adzom main-Tibetan sequence and audited interleaved annotations. The comparison extension now covers Dzongsar’s complete Chapter1 main sequence with local uncertainty flags and records further witness attempts. It has also documented a concrete limit: the current readings cannot certify continuous all-variant collation of several comparison witnesses. This remains a research checkpoint; it does not pass the completed-chapter gate below.

## Read the current work

- [Chapter 1: Tibetan reading text and apparatus](chapter-01.md)
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

## Iteration gate

Complete and validate Chapter 1 before starting Chapter 2. Repeat this gate for each subsequent chapter. A chapter can be marked complete only after its declared witness coverage has been checked, its base transcription has been proofread throughout, all observed differences have apparatus entries, and all outstanding unreadable or unavailable spans are precisely recorded. A mechanical round-trip check establishes transcript coverage, not philological completeness.

Source baseline: [`e17a496ad7532cc627f9ba288b541f7a53efd002`](https://github.com/Lotus-King-Translation/Dra-Thal-Gyur/commit/e17a496ad7532cc627f9ba288b541f7a53efd002). Created 2026-09-27.
