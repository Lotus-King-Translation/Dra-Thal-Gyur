# Dra Thal Gyur — translation handoff

## Template policy baseline — P3

Adopted common snapshot: `Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`. Active standard **2.1.0**, SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`; P2 glossary **283 data rows in the existing eight-column format**, SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`. Both active files match the pinned template byte-for-byte, with no local terminology exception. [P3](../DECISIONS.md#post-translation-review-2026-10-05) defines Phase D; [P1](../DECISIONS.md#terminology-clarification-2026-10-04) and [P2](../DECISIONS.md#terminology-expansion-2026-10-05) retain their exact scopes and provenance. The 63 regression fixtures are specifications, not measured model results.

Adoption is recorded on `policy/adopt-template-882454cb` for a pull request to `main`; merge into `main` is not yet verified. This is policy adoption only, not a translation review or new release. Prior release-time statements that the glossary/standard were unchanged describe those fixed historical inputs. Do not update old manifests, signatures, release receipts or archived policy copies to make them claim the new policy was used then.

## Fixed inputs for the assigned review

- Golden release / commit: `root-tantra-v1.0.0` / `b83051912977268b97615bd382d82e51c3406d61`.
- English release / commit: `translation-golden-aligned-v1.0.0` / `e24e97ddad9cefa339b5583a38389179dba7a365`. Paired presentation remains `dra-thal-gyur-paired-v2.0.0` (`d2285b8fe09e2a27be7aab5bcfb7a87806e949c5`).
- Canonical English/source input checkpoint: starting `main` `3ae74a2adaa734b6332e64bd2f905f25aec1044a`; `paired/source.md` and `paired/translation.md` remain byte-identical to that checkpoint.
- Active glossary: P2, 283 rows, SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`.
- Active translation guideline: **2.1.0**, SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`; read Parts I–III, including Part I §8.1 and Q1–Q9.
- Explicit project decisions: [root decision history and adoption](../DECISIONS.md#policy-adoption-2026-10-05). The existing Adzom source authority, diplomatic recovery/continuation instructions, paired-text/2 source-only formats, immutable membership and v1-to-v2 lineage are retained. Earlier source and English locus decisions stay in their existing ledgers; this root record does not replace them.

## Current translated coverage — not review coverage

All **2667/2667** canonical source pairs have matching English; **0** remain to draft. They represent 5,484 golden objects, including 18 added objects and 23 restored verses. These are representation counts, not accuracy or decipherment scores. 173 reconciliation endnotes, 340 earlier-note IDs and 65 source-annotation components remain preserved. Source-difference reconciliation is not fresh independent semantic review of unchanged English.

[Existing reconciliation review](2026-10-01-golden-aligned/REVIEW.md), [provisional usages](2026-10-01-golden-aligned/USAGES.json), [historical reconciliation handoff](2026-09-26-full-draft/golden-review/HANDOFF.md), and [paired handoff](../paired/HANDOFF.md) remain preserved. Their earlier authoring, source-reconciliation or independent-agent review claims retain only their recorded scope; they do not count as completion of the newly adopted Phase D contract.

## Post-translation review — Phase D

- Review mode: **unassigned / not started**; the next assignment must explicitly choose review-only or authorize revision. This adoption task authorizes neither review nor revision.
- Reviewer/session and authoring run: **reviewer and session unassigned**; no new authoring run. Historical author/reviewer identities remain in the existing release reports above.
- English input commit/release: `translation-golden-aligned-v1.0.0` at `e24e97ddad9cefa339b5583a38389179dba7a365`; unchanged canonical checkpoint `3ae74a2adaa734b6332e64bd2f905f25aec1044a`. Paired presentation remains `dra-thal-gyur-paired-v2.0.0` (`d2285b8fe09e2a27be7aab5bcfb7a87806e949c5`).
- Adopted common policy commit: `882454cb2576d0b2529296bd7a3a7c87371ab4cf`.
- Expected pair inventory: **2667 pairs**, by chapter and terminal material as tabulated below.
- Actually reviewed pair ranges / count: **none / 0**.
- Unreviewed or missing ranges: **all 2667 pairs are unreviewed under Phase D**. Mechanical inventory comparison found no missing or mismatched source/English pair IDs; this is not semantic review.
- Findings — corrected / justified no-change / unresolved: **not assessed**; no Phase D findings or dispositions created. Existing uncertainties remain visible in their original notes and usage records.
- Changed pairs rechecked and dependent views verified: **not applicable; 0 changed pairs**. No reading edition was regenerated. Byte-preservation checks do not count as semantic rechecking.
- Report path/commit and actual validation results: **no Phase D report or review commit yet**. Reuse the appropriate existing review/usage records when assigned, preserving historical reports; do not create parallel ledgers. Adoption-only validation is recorded below.
- Coverage disposition: **not started, 0/2667**. Text disposition, separately: **not assessed**. Neither is clean publication approval or human certification.
- Remaining bounded work / shared proposals: owner assignment, PR integration, then all **2667** pairs under Part III and Q1–Q9, including titles, colophons, closing material and unresolved spans. Unapproved local usage proposals are not activated by local history or by this propagation.

### Expected ordered inventory

| Chapter / part | Expected pairs | First → last in source order |
| --- | ---: | --- |
| chapter-01 | 1199 | `DTG-000001` → `DTG-001192` |
| chapter-02 | 543 | `DTG-001193` → `DTG-001735` |
| chapter-03 | 354 | `DTG-001736` → `DTG-002089` |
| chapter-04 | 237 | `DTG-002090` → `DTG-002326` |
| chapter-05 | 211 | `DTG-002327` → `DTG-002537` |
| chapter-06 | 108 | `DTG-002538` → `DTG-002645` |
| closing-material | 15 | `DTG-002646` → `DTG-002660` |

Source order, not numeric ID order, is authoritative. Chapter 1 includes the twelve split-child IDs DTG-002661–DTG-002672; the five retired v1 IDs are not reintroduced. The existing [full lineage](../paired/v2/PAIR-AUDIT.json) remains authoritative. The 15 closing pairs retain all 18 closing anchors.

## Policy adoption validation

Executed on the connected Mac against starting `main` `3ae74a2adaa734b6332e64bd2f905f25aec1044a` before edits, then against this policy-adoption working tree. These are structural/integrity tests, not English review or semantic certification. `main` was verified unchanged before publication. All 18 remote tag/peeled-ref entries and the local tag inventory remain unchanged.

| Existing command | Before adoption | After adoption | Classification |
| --- | --- | --- | --- |
| `python3 -B paired/validate.py` | PASS | FAIL: PAIRED VALIDATION FAILED: Protected input changed or missing: glossary/expanded_tibetan_english_glossary.csv | Introduced current-tree incompatibility |
| `python3 -B paired/validate.py --require-final` | PASS | FAIL: PAIRED VALIDATION FAILED: Protected input changed or missing: glossary/expanded_tibetan_english_glossary.csv | Introduced current-tree incompatibility |
| `python3 -B paired/test_paired.py` | PASS: 64 tests | FAIL: 64 tests run; 63 pass, 1 error (released-corpus check rejects old glossary hash) | Introduced current-tree incompatibility |
| `python3 -B paired/migrate.py --check` | PASS | FAIL: Protected input changed or missing: glossary/expanded_tibetan_english_glossary.csv | Introduced current-tree incompatibility |
| `python3 -B paired/project.py --check` | PASS | FAIL: Protected input changed or missing: glossary/expanded_tibetan_english_glossary.csv | Introduced current-tree incompatibility |
| `python3 -B translations/2026-09-26-full-draft/golden-review/validate_translation.py --require-final` | PASS | FAIL: ValueError: Protected baseline changed: glossary/expanded_tibetan_english_glossary.csv | Introduced current-tree incompatibility |
| `python3 -B translations/2026-09-26-full-draft/golden-review/test_translation.py` | PASS: positive case and 36 negative controls | PASS: positive case and 36 negative controls | Pass retained |
| `python3 -B translations/2026-09-26-full-draft/golden-review/build_translation.py --check` | PASS | FAIL: ValueError: Protected input changed: glossary/expanded_tibetan_english_glossary.csv | Introduced current-tree incompatibility |
| `git diff --check` | PASS | PASS | Pass retained |

Adoption-specific checks **PASS**: exact pinned standard/glossary bytes and hashes; standard 2.1.0; CSV 283 data rows and eight columns; exact, singly anchored P1/P2/P3 records; full shared Phase D instructions retained; populated project histories preserved; matching ordered inventory of **2667** unchanged source/English pairs; relative links/anchors in the bounded documents checked with **no introduced broken links**; `git diff --check` clean. **5495 tracked files outside the eight-file adoption set are byte-identical** to the starting checkpoint. This includes fixed Tibetan, source editions/registers, canonical English, active notes, pair IDs, historical release inputs and policy copies, generated readers, scripts, schemas and unrelated files.

The introduced failures first reject the old active glossary hash. The protected reconciliation inputs also pin the old standard, and paired final signoff additionally binds the old `AGENTS.md` and root `README.md`. The signed release contracts are historical, not authority to silently replace the newly approved policy. No old input, manifest, signoff, validator or release tag was rewritten to suppress these checks. The previously passing release checks remain documented at the starting checkpoint; the current adoption tree does **not** pass those fixed-release gates.

**Integration blocker:** the adoption branch is complete as a policy-only candidate, but `main` adoption awaits PR merge with the legacy active-path/release-pin incompatibility explicitly visible. Branch protection was not reported on `main`; the PR route is used to avoid silently publishing a failing release-validation state on `main`. Any validator/manifest architecture change is outside this task and requires a separately scoped owner decision. This blocker does not authorize English correction, a new release, or commencement of Phase D.

## Next finite task

Await PR integration and an explicit reviewer assignment. That reviewer must freeze the actual English/source/policy inputs and mode, review the complete inventory above, and record coverage separately from text disposition. **No review or English revision has started.** Do not reopen source collation or create a new release for this policy-only task.

## Preserved release state and continuation

The active paired publication is `dra-thal-gyur-paired-v2.0.0`, evidenced by [its post-tag receipt](../paired/v2/PUBLICATION.json). The fixed English `translation-golden-aligned-v1.0.0` has [its own publication receipt](2026-10-01-golden-aligned/PUBLICATION.json); the golden source is fixed as `root-tantra-v1.0.0`. No release tag is created or moved here.

This missing top-level handoff is populated from the existing [paired handoff](../paired/HANDOFF.md), [English edition overview](2026-10-01-golden-aligned/README.md) and [reconciliation handoff](2026-09-26-full-draft/golden-review/HANDOFF.md); none is replaced or rewritten. All 5,466 original source anchors, 18 added golden objects, 23 restored verses, 65 source-annotation components, 173 reconciliation endnotes and 340 earlier-note IDs remain represented. Unchanged-source English inherits its earlier interpretation limits; no new independent semantic QC is claimed.
