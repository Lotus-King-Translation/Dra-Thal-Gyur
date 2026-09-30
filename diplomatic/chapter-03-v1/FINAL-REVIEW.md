# Chapter 3 — final bounded release review

Reviewer: ChatGPT editorial coordinator, continuing under the user's instruction to finish Chapter 3 before Chapter 4. This is not credentialed human palaeographic certification.

The previously completed [editorial review](EDITORIAL-REVIEW.md), 41 A/B/S decisions, 76 W decisions and ten targeted source dispositions are retained. No new Tibetan reading is introduced by this final gate. All 683 original anchors, three restored main verses, ten source-note components and eleven changed-anchor strings are preserved.

## Resumed tests

The saved corruption-test script now runs successfully: its positive fixture passes and all 29 deliberately corrupted in-memory fixtures are rejected. The originals are never modified by those tests. See [execution receipt](checkpoints/0009-resumed-tests.json). The previous blocked execution remains documented in its original access record; it is not recast as a successful earlier run.

The unsigned final-mode validator was separately run and correctly rejected the unsigned candidate. See [gate rejection](checkpoints/0009-unsigned-gate.json). The normal validator and both reproducibility checks passed before signoff.

Opening and closing reading excerpts, the three-line restoration between U03715 and U03716, and the visible U03952 uncertainty flag were inspected. U04305 retains its closing uncertainty. The transition graphic remains undecoded and non-main. Restored shads and line breaks remain explicitly editorial rather than a claim of facsimile punctuation.

The inherited metric label `source_families_verified` is replaced by `electronic_representations_verified`: A/B/S/W are four electronic representations, not four independent witness families. No source count or Tibetan reading changes.

## Acceptance

Approve the fixed bounded Chapter 3 v1 after source-bound signoff, fresh final-mode validation, and verified publication of its commit and version tag. All 34 retain-base, six evidenced-correction/restoration and one explicit-uncertainty locus choices remain as authored. Counts are release dispositions, not error-rate estimates.

Full Adzom scan proofreading and exhaustive witness collation remain outside this release. Chapters 1 and 2 must remain byte-identical within their released directories. Chapter 4 begins only after the Chapter 3 publication has been verified.
