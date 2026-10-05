# Dra Thal Gyur — project status

## Shared policy adoption — 2026-10-05

The active standard **2.1.0**, the **283-row/eight-column** glossary, and the shared Phase D operating contract are adopted from exactly `Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`. Standard and glossary are byte-identical to that snapshot; there is no local terminology exception. See [P1/P2/P3 and adoption provenance](DECISIONS.md#policy-adoption-2026-10-05) and the [review handoff](translations/HANDOFF.md#post-translation-review--phase-d).

Scope completed on this branch: **1/1 repository policy adoption; 0 English reviews; 0 translation corrections**. The four-repository propagation task does not assign reviewers. Publication route: `policy/adopt-template-882454cb` → pull request to `main`; merge into `main` is not yet verified. Legacy release checks bind earlier active policy bytes, so their current-tree incompatibilities are disclosed rather than changing signed manifests or validators.

Ready for an owner-assigned **review-only** pass using this branch's common policy and the fixed English below; adoption on `main` awaits PR merge. Reviewer/session: **unassigned**. Reviewed coverage: **0/2667 pairs**. Review completion: **not started**. Text disposition: **not assessed**. No revision authority, new release, or independent/human certification is inferred from policy adoption.

Preserved starting `main`: `3ae74a2adaa734b6332e64bd2f905f25aec1044a`. Fixed Tibetan: `root-tantra-v1.0.0` (`b83051912977268b97615bd382d82e51c3406d61`). Fixed English: `translation-golden-aligned-v1.0.0` (`e24e97ddad9cefa339b5583a38389179dba7a365`). Canonical content remains `paired/source.md` and `paired/translation.md`; **2667** matching pairs represent 5,484 golden objects, including 18 added objects and 23 restored verses. 173 reconciliation endnotes, 340 earlier-note IDs and 65 source-annotation components remain preserved. Source-difference reconciliation is not fresh independent semantic review of unchanged English.

The existing Adzom source authority, diplomatic recovery/continuation instructions, paired-text/2 source-only formats, immutable membership and v1-to-v2 lineage are retained. Earlier source and English locus decisions stay in their existing ledgers; this root record does not replace them.

Actual before/after policy validation, exact input hashes, complete chapter inventory, and pre-existing versus introduced failures are recorded in [the existing handoff](translations/HANDOFF.md#policy-adoption-validation). Historical policy copies, release tags, English, notes, Tibetan, source registers and pair identities are unchanged. The active policy update does not retroactively certify the English against the new standard.

Next finite task: await the owner's reviewer assignment and PR integration; then review all **2667** pairs, including closing material, under Part III and Q1–Q9. No review has begun here.

## Existing release history and continuation

The six-chapter bounded golden edition and its closing material are released. The golden-aligned English reconciles all 110 changed source strings and 18 added golden objects, including 23 restored verses, with 173 reconciliation endnotes. The paired-text/2 publication contains 2,667 pairs and preserves earlier notes, source annotations and closing material. These earlier accomplishments are not fresh whole-text semantic QC.

[Diplomatic release/continuation](diplomatic/HANDOFF.md), [English publication overview](translations/2026-10-01-golden-aligned/README.md), [historical reconciliation continuation](translations/2026-09-26-full-draft/golden-review/HANDOFF.md), and [paired publication/continuation](paired/HANDOFF.md) remain unchanged. All bounded source-reconciliation and paired-v2 implementation work was already complete before this adoption.
