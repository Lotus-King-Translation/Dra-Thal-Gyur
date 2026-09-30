# Chapter 1: release-scope audit and proposed finite v1

Audit date: 2026-09-30. Audited content: `55d6b61225dc9ef3d7b32ed2e905fce4ef89d5cf`.
**Approved by the user on 2026-09-30. Bounded v1 execution is active; the historical audit below is preserved. This does not certify exhaustive collation.**

## Findings

The inherited local checkout was behind remote main and contained nine unpublished project files/updates. They were preserved on `recovery/ch1-audit-20260930-123749` at `8c3b124a75298779263983a418f7cb8d8247a118`, remotely verified, then merged with the newer remote work. Main was pushed and verified at the audited content commit. No Tibetan reading was changed by this audit.

Read-only chapter validation and build reproducibility passed: 2,635 original anchors; 359 exact transcript differences in 183 readable loci; 88 intervention/source-layer/uncertainty records; 84 curated replacement anchors; 13 restored main verses; 667 comparison observations including uncertainty. Source reconstruction and preservation passed. These counts are not independent accuracy measurements or counts of confirmed variants.

The earlier chat's 401-record apparatus and integration backlog are stale. Later repository work has integrated those old packets and further comparisons. Eight newer batch records still await integration/disposition; their exact identities are frozen in PLAN.json. A stale prepared label does not show whether its reader has finished. Completed receipts and original output bytes must be checked, not replaced by a new reading.

## A real improvement, but not the same as reconstructing an original

The existing edition restores 13 main verses absent from the supplied Adzom e-text and separates source notes from main verse. For example, U00180's supplied string inserts a long structural annotation between `ཐ་མི` and `དད`; the current main text is `དེ་ནས་གཅིག་དང་ཐ་མི་དད། །`, with the annotation preserved separately. U01286 is likewise kept as a source note rather than falsely displayed as a main verse. See the authored additional-interventions and insertion ledgers.

This improves the digital representation of Adzom and its comparative usefulness. It does not establish that the master is textually superior to the Adzom printing. The current method intentionally does not replace Adzom readings simply because another witness is more grammatical or has majority support.

## Why progress has not been intelligible

The method requires complete base coverage and every acquired witness's coverage or a precise unavailable span. That is a much larger endpoint than a useful first reading edition. New page reading also keeps generating further local questions.

The builder's A/B/S dispositions are generated from broad rules, and all 183 are labelled provisional. Several completion fields are hard-coded false. This is an honest guard against unsupported certification, but it is not a calculated release-readiness gate. Removing those flags is not the solution; an explicit, separately approved release contract is.

The existing GitHub reviewed-integration workflow is bound to a particular historical recovery branch. It is useful infrastructure, not a general current-main release pipeline. Hand-written REPL state and repeated recovery operations should not be the primary progress system.

One combined audit-analysis request was safety-status blocked. It was not executed or rerouted. No fresh character-level error rate or lexical-only correction count is asserted here.

## Proposed v1 finish line

Publish a corrected Adzom-based reading, with the existing complete A/B/S transcript comparison, the scoped W comparison, and all integrated scan findings. Preserve the faithful base; do not silently turn this into a normalized eclectic edition. Keep named uncertainties visible. Do not require new general page reading, every marginal mark, or completion of every comparison witness for this release.

| Workstream | Fixed scope | Completion test |
|---|---|---|
| Pending packet intake/integration | Eight exact batch identities in PLAN.json | Every observation receives a traceable disposition; any unsupported or unavailable report is explicitly deferred, never credited as collated. |
| Release choices | 183 existing A/B/S locus identities | Each has a release choice, locus-specific rationale and evidence reference. Reuse prior decisions; do not reread 183 source passages automatically. |
| Accepted-content reconciliation | 88 intervention records and 13 restored main verses at baseline | Preserve every accepted item and link, separate notes from root text, and document any actual change. Existing checks are evidence, not a reason to restart the work. |
| Publication | Five deliverable groups in PLAN.json | Clean reading, apparatus, combined machine reading, change ledger, and coverage/uncertainty register. |
| Final gate | One scope-specific signoff | Reproducible build, exact reconstruction, reference checks, editorial acceptance, and verified remote commit. Exhaustive-witness status remains false. |

An unresolved glyph can have a completed v1 disposition: retain an explicitly uncertain reading and explain the exact scope. It is not a resolved glyph. Failed technical work or missing evidence cannot be counted as successful inspection.

The 183 new acceptance slots are not a claim that all prior scholarship is unfinished. They make the release decision explicit where the current builder supplies a generic provisional paragraph. Their initial empty state is administrative, not a measure of research completed.

## What the old exhaustive scope still entails

| Witness | Ranges still lacking finished continuous comparison ledgers | Range size |
|---|---|---:|
| Tingkye | PDF17-34 and PDF40-69 | 48 |
| Tsamdrak | PDF27-83 | 57 |
| Dege | PDF15-54 | 40 |
| Tharpaling | PDF7-71, including preserved partial fragments | 65 |
| Gadkar | PDF4-91; old locators do not constitute full collation | 88 |
| Adzom1973 | Provider PDF11-112 | 102 |
| Gcn | Provider PDF407-484 | 78 |

These ranges total **478 page/container-page positions**, not 478 untouched pages or equal-sized work items. Pending packets overlap these ranges. Older partial work and local unresolved components also remain. In addition there are Adzom's broad physical-proofreading remainder (PDF17-102 plus earlier open components), Dzongsar's physical/annotation work, Langtang's largely missing continuous ledger, and unresolved Zhichen/W1ER119 coverage. The latter prevent an honest exhaustive-completion percentage. This research belongs to a separately scoped later edition, not a hidden v1 prerequisite.

## OpenPecha / WeBuddhist findings

[Their textual supply-chain requirements](https://forum.openpecha.org/t/pecha-data-data-requirements-document-drd/320) distinguish source-faithful diplomatic transcriptions (Stage 3) from a chosen, normalized master and layered apparatus (Stage 4). This is an architecture proposal, not evidence that every described feature is deployed.

[The 17 Tantras SIG proposal](https://forum.openpecha.org/t/17-tantras-sig-proposal/402) explicitly starts with Adzom, Tharpaling and Sichuan, collated text, variant spellings, consensus decisions and image-linked notes. It supplies a relevant bounded model; its draft claims and milestones are not independent validation of our files.

[Pydurma's current README](https://github.com/Webuddhist-tech/Pydurma/blob/main/README.md) describes preprocessing, collation and configurable variant selection while preserving original character positions. Its stated limitations include no transposition detection and no clearly defined apparatus export format. It explicitly distinguishes automatically selected, temporary vulgate-like outputs from faithful diplomatic editions. Use it as a candidate/alignment engine when appropriate, not as authority for source readings. No installation or benchmark was performed in this audit.

[Toolkit V2](https://github.com/Webuddhist-tech/toolkit-v2/blob/main/README.md) provides STAM stand-off layers for texts, segmentation, alignment, pagination and notes. These principles match much of our existing base-plus-ledger structure. A migration should be tested as an export adapter after v1; it should not become another prerequisite.

[The Critical & Collated Edition Editor PRD](https://forum.openpecha.org/t/prd-critical-collated-edition-editor/314) specifies multi-witness alignment, editorial justification and export. The document describes prototyping and target milestones; this audit does not establish a currently production-ready editor for this project.

## Every checkpoint should report

Report exact changes since the prior verified commit, packet dispositions completed and remaining out of eight, final-release locus entries completed and remaining out of 183, unresolved components separately, preserved restorations, validation results and verified remote SHA. A retained or rejected candidate is a completed editorial decision, not an adopted correction. More variants or more commits do not prove more accuracy.

Never combine file counts, page inspections, decisions, and corrections into one percentage. Keep source/lexical, physical-sign and release-readiness coverage distinct. Existing uncertainties should not force repeated inspection of the same pixels without a new evidentiary reason.

Expected operation: one coordinator, at most one integration batch in flight, persistent input/output manifests, no speculative reader backlog, no new dependency migration before release. Technical failure produces a preserved failure record and no coverage credit. A source-reading job must finish or have its partial state preserved before another is commissioned.

A clock-time forecast is not defensible from the available logs. Establish an end-to-end observed throughput for this frozen checklist before giving a date. Do not repeat unsupported assurances that another session will finish the exhaustive edition.

## Read-only progress meter

Run from the repository root:

```bash
python3 diplomatic/tools/release_progress.py --repo .
```

The meter reads only identifiers and acceptance metadata. It freezes the 183-locus denominator at the audited commit, checks the eight current batch states, requires rationale plus existing evidence references for acceptance entries, and lists the five proposed deliverables. Its saved initial output is [PROGRESS.json](PROGRESS.json). The five deliverables being absent does not mean their source data are absent: the current edition and apparatus already exist outside the proposed release directory.

Initial state: eight pending packet records; zero of 183 **new release-acceptance entries** recorded; five release deliverable groups not yet packaged. These are separate counters, not an assertion of zero prior research. The scope is not yet approved. The meter deliberately does not certify scholarship, infer accuracy, estimate hours, or replace the final editorial review and real validation runs.

To accept a locus, add its existing ID under `DECISIONS.json:loci`, with `status` chosen from the plan, a locus-specific `rationale`, and an `evidence` list of repository-relative files. A packet deferral requires its exact `TASK/BATCH` key, rationale and evidence; it is reported separately and never counted as collation. Keep pre-existing scholarly ledgers as the authorities for readings.
