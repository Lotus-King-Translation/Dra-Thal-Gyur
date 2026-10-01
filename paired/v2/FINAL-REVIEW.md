# Paired-text/2 final review

Disposition: accepted for publication on 2026-10-01; zero blocking findings.
This is an agent-led structural and engineering review, not human scholarly
approval, fresh semantic QC or a reopening of either governing text release.
The precise reviewed files and counts are bound by SIGNOFF.json. Publication
itself requires the subsequently verified annotated tag and PUBLICATION.json.

## Scope and independent checks

Two independent reviewers inspected the v2 implementation at `d49388b` and
current finalization changes. The structural reviewer separately parsed the
canonical files without importing core.py or structure.py: all 5,484 Tibetan
and English objects project exactly to their pinned released strings. All
2,660 lineage entries reconcile, including all unchanged memberships. All
173 endnote bodies match after equivalent relative-path normalization.

The structural reviewer reread title/formula pairs, all twelve new child pairs,
and all fifteen closing pairs; reviewed the full heading inventory and chapter
audit reports; and checked the integrated decision ledger. The engineering
review independently reconstructed the exact source/English object projections,
reviewed the parser, validator, generator and tests, and verified protected
inputs, lineages and reproducibility. Neither review claims a fresh scholarly
rereading of every main verse or new scan inspection.

## Accepted structure and preservation

All 2,667 pairs are classified: 48 prose, 2,448 verse, 2 h1, 0 h2, 169 h3.
The two h1 objects are title-leaf headings. Embedded opening language/naming
formulas are prose. All 169 source headings were inventoried and reviewed as
chapter-internal sibling sections before assigning h3; their source role alone
was not treated as proof of rank. Existing chapter wrappers are h2 outside
pairs, so no paired h2 was invented.

Five v1 pairs retire and become twelve new identities; 2,655 pairs retain exact
membership. The complete record is [PAIR-AUDIT.json](PAIR-AUDIT.json). No golden
object is split. Formats derive from Tibetan/editorial structure without
English-punctuation classification. Hearing-formula and closing-paratext prose
choices are qualified rendering decisions; inherited readings and historical
genre uncertainties remain as documented in STRUCTURE-DECISIONS.json.

Preserved: 5,484/5,484 golden objects, 23/23 restored verses, 173/173 reconciliation
endnotes, 340 earlier-note IDs, 4,932 object-note relations, 65 source annotations,
18 closing anchors, six chapters and distinct closing material. Unmatched
source/translation pairs: 0/0. Duplicated/omitted golden objects: 0/0.
All 128 protected input files and both immutable release pins remain unchanged.

## Findings and acceptance gates

The engineering review found that CI initially omitted `--require-final`.
Resolved: CI now requires accepted hash-bound signoff on main, pull requests
and paired version tags. It rejects missing/stale signoff and reruns all
preservation, corruption and reproducibility checks.

The review also found that an alternate `--repo` could combine its corpus with
this checkout's decision ledger. Resolved: the validator now rejects alternate
resolved roots before reading their corpus; run the target checkout's own
validator. A dedicated rejection test covers this defect. The coordinator
reviewed this bounded correction and its test; it changes no canonical content.

Final local checks: corpus validation passes; 64 tests pass (7 positive,
57 rejection cases); canonical migration, manifest and full lineage reproduce
exactly; 683 local link targets validate; `git diff --check` passes. The final
gate rejected the unsigned state before signoff. SIGNOFF.json binds every
release-critical implementation, corpus, decision, audit, review and CI file.
The publication receipt is intentionally excluded because it must be committed
after the immutable tag without moving that tag. Remote CI and tag verification
are recorded in the subsequent publication receipt, not asserted in advance.
