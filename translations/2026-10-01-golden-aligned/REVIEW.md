<a id="phase-d-review"></a>
# Post-translation review — current working text

**Task:** POST_TRANSLATION_REVIEW · **Mode:** review-and-revise · **Session:** DTG-PD-20261005-Astra-01 · **Reviewer:** GPT-6 Astra Pro, this review session, distinct from the September 26 authoring run and October 1 source-reconciliation coordinator. Review of the input is independent of those runs; checks of this session's repairs are self-checks, not a second independent review or human certification.

**Authority:** the owner's explicit October 5, 2026 assignment authorizes the smallest supported English and translation-note repairs in this repository only. No fresh translation, stylistic rewrite, Tibetan emendation, segmentation change, new shared glossary assignment, release or tag movement is authorized.

## Frozen inputs and adopted policy

English input commit: `fc3a443ba5987efb0b132990bf131a236fa57320` (current remote main at freeze). Canonical authored working English: `paired/translation.md`; fixed paired source: `paired/source.md`. Inherited translation edition: `translation-golden-aligned-v1.0.0` (`e24e97ddad9cefa339b5583a38389179dba7a365`). Paired identity/format edition: `dra-thal-gyur-paired-v2.0.0` (`d2285b8fe09e2a27be7aab5bcfb7a87806e949c5`). Golden Tibetan: `root-tantra-v1.0.0` (`b83051912977268b97615bd382d82e51c3406d61`). These are inherited edition identifiers, not a new release or a certification of revised text.

Common policy commit: `Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`. Local adoption: `10fe4e8c1ea0be37a205753dbb4a7e6e4c84a126`, merged by PR [#5](https://github.com/Lotus-King-Translation/Dra-Thal-Gyur/pull/5) at the frozen main commit; merge verified through GitHub and the remote ref. Standard **2.1.0, Parts I–III**, including I §8.1 and III, and **283 data rows with all eight glossary columns** were read. Active policy hashes and row/column counts were recomputed and match the adopted records. P1/P2/P3 govern only their stated scopes. No later explicit owner-approved local terminology exception was found; the present assignment changes edit authority, not glossary policy.

Root `FORMAT.md` is absent (documentation gap). The operative local format is documented in `paired/README.md`, `paired/MIGRATION.md`, `paired/core.py` and the retained `paired/v2/reference/template-FORMAT.md`; the latter is a historical format reference, not a replacement terminology-policy version. The complete 2,660-entry lineage JSON was parsed and reproduced from the pinned baseline without discrepancy. Source structure and membership will not change.

| Frozen file | SHA-256 |
|---|---|
| `AGENTS.md` | `d12a92da3151ac74995a2f81b517a2329730aa09b441de99b3c81723be1edf71` |
| `PROJECT-STATUS.md` | `156351ff053b1faa1a2c2b58e76abb3fc6ab491d1f36af361eaa61ae2ad84baf` |
| `translations/HANDOFF.md` | `192599bde87085fb5e5b624e3c9ce11554e01917daf438508fa166d961e4da95` |
| `DECISIONS.md` | `138e4a35e028a9be6df7127e66cb58263b83c671dad47f6ea12d7aebe6070693` |
| `guidelines/tibetan_translation_standard_v2.md` | `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f` |
| `glossary/expanded_tibetan_english_glossary.csv` | `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7` |
| `paired/source.md` | `f25ec78468cc5120426ad59e689d8708159a42fa16d5aa3869a990b53f31cc4c` |
| `paired/translation.md` | `06dfdd15d37c504f644a2d76583236eff15cc28bf19417c1b6ddedd89af8d1e8` |
| `paired/v2/STRUCTURE-DECISIONS.json` | `b5b2241b9214cfa0c468341f5b6e25bf08084cf021389595260d60266899fda0` |
| `paired/v2/PAIR-AUDIT.json` | `27285d659160afeced6022d4801f301e365404e8d7ad312d1117ec12787d1efc` |
| `paired/v2/reference/template-FORMAT.md` | `c4c6d00ff8cb09dea5743368087da735c7adb86fde0692c3a10594a5ccba7b98` |
| `diplomatic/root-tantra-v1/release/reading.json` | `d0f03b58e4e60ae8db730dfe2a498742d4e9d2e3f4d74fa5bdb13c9574c9b309` |
| `diplomatic/root-tantra-v1/release/reading.md` | `a49fc523d54a2705fe5a1b712a3703c0cc6539e9824364c23c4f47bb14dc910e` |
| `translations/2026-10-01-golden-aligned/REVIEW.md` | `e727eced469cd6e4e1b94801e9d3e2accb2b703cc039d716f7da520be4364c4a` |
| `translations/2026-10-01-golden-aligned/USAGES.json` | `3233afe2a8d1727d97b5b21a9d79e92b0f68e8f4b8c2e9894ef661fe745ac47c` |

### Preservation and release inventory

Initial local checkout was clean on `policy/adopt-template-882454cb` at `10fe4e8`; remote main was fetched and its tree matched that checkout. The review branch starts at frozen main. No stash existed. The detached recovery worktree at `4dd344ee4febca7cb117f03519c6ec85ede6e930` was clean and was not changed. The local-only recovery baseline `e17a496` is already an ancestor; all existing branches/worktrees were preserved. No reset, cleanup, force push or tag write was performed.

Remote annotated tag objects and peeled commits were read at freeze:

| Ref | Object/commit |
|---|---|
| `refs/tags/chapter-01-v1.0.0` | `7f74249c6378dd9f5b6733456bf4cec5a79af0b8` |
| `refs/tags/chapter-01-v1.0.0^{}` | `cf8430ce08240f179fa1cadefebedb3ec2cc6f4c` |
| `refs/tags/chapter-02-v1.0.0` | `303899657ec087447f3c679208ae43992f530f0d` |
| `refs/tags/chapter-02-v1.0.0^{}` | `6e9b4ed977103b6151bbd75784852a4a17865c90` |
| `refs/tags/chapter-03-v1.0.0` | `79d19d71df1369288ff11ebdfb9306cdea9f9edf` |
| `refs/tags/chapter-03-v1.0.0^{}` | `17abe1f0e68069406f782a77e93dab10841b81fb` |
| `refs/tags/chapter-04-v1.0.0` | `7ba6a17a9e688b7c9ef8f8bc80617839e3b72358` |
| `refs/tags/chapter-04-v1.0.0^{}` | `5abb397ab77a32b6e360d0a269ed92bf71b855e1` |
| `refs/tags/chapter-05-v1.0.0` | `8a9286c3e2053eceb1ff78223858510c07e0591e` |
| `refs/tags/chapter-05-v1.0.0^{}` | `c4e03593e52939c52f989c6611e2ea4df967afb2` |
| `refs/tags/chapter-06-v1.0.0` | `a7edeeabdec771aeefbacd94020d09ca79c00737` |
| `refs/tags/chapter-06-v1.0.0^{}` | `128dc0fedf0de737ca14e025ee4aa0028b145713` |
| `refs/tags/dra-thal-gyur-paired-v2.0.0` | `449483c4003479803f8ee19fd965cd8be1183953` |
| `refs/tags/dra-thal-gyur-paired-v2.0.0^{}` | `d2285b8fe09e2a27be7aab5bcfb7a87806e949c5` |
| `refs/tags/root-tantra-v1.0.0` | `97379615d268149eee768c9c1ec99b7be2f993b4` |
| `refs/tags/root-tantra-v1.0.0^{}` | `b83051912977268b97615bd382d82e51c3406d61` |
| `refs/tags/translation-golden-aligned-v1.0.0` | `ed0783c6a394d4ace736a09d812f0666c6743848` |
| `refs/tags/translation-golden-aligned-v1.0.0^{}` | `e24e97ddad9cefa339b5583a38389179dba7a365` |

The October 1 source-reconciliation report remains verbatim below as history. Its 173 endnotes, 340 earlier-note IDs (4,932 object/note associations), 65 separate source-annotation components, 23 restored verses and 18 closing anchors are inputs, not evidence of fresh semantic review. Existing `USAGES.json`, `LEGACY-NOTES.md`, golden `UNCERTAINTIES.md`, and source-reconciliation `DECISIONS.json` supply current dispositions before an older criticism is evaluated. No new source update after the fixed golden edition is adopted here.

<a id="phase-d-coverage"></a>
## Finite whole-work scope and actual coverage

File/source order, not numerical ID order, governs. Chapter 1 includes the title/opening and the twelve split children DTG-002661–DTG-002672; the five retired v1 IDs are not reintroduced. The complete ordered inventory remains the existing canonical source and `paired/v2/PAIR-AUDIT.json`, not a second segmentation ledger. Total scope: **2,667 pairs / 5,484 golden objects** (5,466 original anchors and 18 additions); formats: 48 prose, 2,448 verse, 2 h1, 0 h2, 169 h3.

<!-- phase-d-coverage-start -->
| Part | Expected pairs | Expected source-ordered range | Actually semantically reviewed | Status |
|---|---:|---|---:|---|
| chapter-01 | 1199 | DTG-000001 → DTG-001192 | 0 | Not started |
| chapter-02 | 543 | DTG-001193 → DTG-001735 | 0 | Not started |
| chapter-03 | 354 | DTG-001736 → DTG-002089 | 0 | Not started |
| chapter-04 | 237 | DTG-002090 → DTG-002326 | 0 | Not started |
| chapter-05 | 211 | DTG-002327 → DTG-002537 | 0 | Not started |
| chapter-06 | 108 | DTG-002538 → DTG-002645 | 0 | Not started |
| closing-material | 15 | DTG-002646 → DTG-002660 | 0 | Not started |
<!-- phase-d-coverage-end -->

The fixed golden has **72 uncertainty-bearing objects in 66 pairs**; this is a source-qualification inventory, not the final count of unresolved translation questions. Opening inscriptions, caption, empty annotation carriers, chapter-transition metadata and closing graphics remain in scope. Exact inherited pairs:

`DTG-000001`, `DTG-000002`, `DTG-000003`, `DTG-000004`, `DTG-000005`, `DTG-000008`, `DTG-002662`, `DTG-000016`, `DTG-000023`, `DTG-000034`, `DTG-000038`, `DTG-000048`, `DTG-000059`, `DTG-000068`, `DTG-000070`, `DTG-000080`, `DTG-002665`, `DTG-002666`, `DTG-000166`, `DTG-000167`, `DTG-000181`, `DTG-000182`, `DTG-000183`, `DTG-000563`, `DTG-000584`, `DTG-000696`, `DTG-000709`, `DTG-002667`, `DTG-002668`, `DTG-002671`, `DTG-001187`, `DTG-001191`, `DTG-001192`, `DTG-001331`, `DTG-001332`, `DTG-001333`, `DTG-001334`, `DTG-001354`, `DTG-001519`, `DTG-001735`, `DTG-001826`, `DTG-001904`, `DTG-001905`, `DTG-001906`, `DTG-002088`, `DTG-002089`, `DTG-002091`, `DTG-002195`, `DTG-002218`, `DTG-002284`, `DTG-002325`, `DTG-002326`, `DTG-002396`, `DTG-002480`, `DTG-002486`, `DTG-002495`, `DTG-002514`, `DTG-002536`, `DTG-002537`, `DTG-002559`, `DTG-002585`, `DTG-002624`, `DTG-002633`, `DTG-002645`, `DTG-002653`, `DTG-002654`.

Review protocol: read every source/English pair and associated notes in source order, apply Q1–Q9, I §8.1 and III, read continued sentences across pair boundaries, then perform bidirectional terminology and continuous-English checks. Pattern matches are candidates only. Findings are recorded below before repairs. No percentage of accuracy will be inferred from counts.

<a id="phase-d-findings"></a>
## Current findings and dispositions

No semantic findings recorded at freeze. No English changes made. Coverage must not be inferred from the inventory or structural checks.

<!-- phase-d-findings -->

<a id="phase-d-verification"></a>
## Actual validation and repair verification

Baseline execution in this session, before any English or report edit:

| Command | Actual result |
|---|---|
| `python3 -B paired/validate.py` | FAIL: protected glossary differs from the historical release contract. |
| `python3 -B paired/validate.py --require-final` | Same pre-existing protected-glossary failure. |
| `python3 -B paired/test_paired.py` | 64 run; 63 pass, 1 error (`positive_released_corpus`, protected glossary). All 57 corruption tests pass. |
| `python3 -B paired/migrate.py --check` | FAIL: protected glossary. |
| `python3 -B paired/project.py --check` | FAIL: protected glossary. |
| `python3 -B translations/2026-09-26-full-draft/golden-review/validate_translation.py --require-final` | FAIL: protected baseline glossary. |
| `python3 -B translations/2026-09-26-full-draft/golden-review/test_translation.py` | PASS: positive case and all 36 deliberately corrupted fixtures. |
| `python3 -B translations/2026-09-26-full-draft/golden-review/build_translation.py --check` | FAIL: protected glossary. |
| `git diff --check` | PASS before edits. |
| Full pinned lineage reproduction, CSV shape and active policy hashes | PASS: all 2,660 lineage records reproduce; 283 × 8 glossary; both adopted hashes match. |

A bundled command was blocked before execution; the individual commands above were subsequently actually executed. The tests listed here are repository engineering tests, **not** execution of the standard's semantic regression specifications. No changed-clause self-check has yet been performed because nothing has been corrected.

### Canonical and generated layers

`paired/translation.md` is the sole current authored English. The dated September draft and October 1 readers/JSON are historical release outputs, not separately edited current translations. `paired/MANIFEST.json` and `paired/v2/PAIR-AUDIT.json` describe the released paired import. Existing builders require exact released English and old policy inputs; rerunning them cannot silently become a post-review build. Their signed contracts, receipts and tags will not be rewritten to make revised working English appear historically signed off. Applicable builds will still be attempted and actual failures reported. Any bounded working-output integration left unsupported by the existing process will be distinguished from semantic coverage.

## Coverage versus text disposition

**Coverage at freeze:** 0/2,667 semantic pairs reviewed; all ranges above remain unreviewed. **Text disposition:** undetermined pending the pass. **Changed pairs:** 0. **New unresolved questions/shared proposals:** not yet assessed. No human certification, new release, or harmonization of the other three works is claimed.

## Continuation

Continue at source-order ordinal 1, DTG-000001. Keep the original Tibetan, all stable IDs/roles/formats, notes and historic releases intact. Save review progress and small explicit commits on `review/post-translation-20261005`.

---

## Historical October 1 report — preserved, not current Phase D certification

# Golden-source reconciliation — review report

**Version:** translation-golden-aligned-v1.0.0. **Golden source:** root-tantra-v1.0.0.

**Mode:** complete comparison of all original anchors and golden additions; source-impact review of every difference with relevant English/context. Unchanged-source passages retain their earlier translation rather than being certified by a new whole-corpus semantic QC.

**Preservation:** the original English draft, its raw batches and decision logs, the Tibetan golden release, and the established glossary remain unchanged. This is a separate annotated revision.

## Completed source reconciliation

All 110 changed original strings, all 18 added golden objects (including 23 main verses), all 42 uncertainty-only passages, two adjacent sentence-continuity revisions, and the Chapter 2 graphic metadata are represented in 173 endnotes. All 65 source-annotation components are retained and rendered separately.

The changed-original-anchor dispositions are: 41 English retentions with notes, 10 meaning/assembly revisions, 43 source-note relocations, and 16 non-main/joined anchors preserved through notes. Two further adjacent English units change for continuity with restored text. These are not counts of confirmed lexical errors.

## Meaningful findings

U00187 no longer treats purpose and the annotation formula as additional root content. U01803 no longer expands ya bzhi to four million after the golden release rejected the required sa/ya split. U02887 follows the selected main clause toward space while preserving smaller rig pa as an unresolved gloss/addition. U03802–U03803 exclude the smaller alternative numbers from the root. U05106 follows main yas gzhi rather than selecting the note ye gzhi.

## Retained uncertainty and limits

The printed source and interpretation are distinct. For example, stong at U00039 is the selected source reading, while a thousand [stamens] is a contextual interpretation; yas gzhi at U05106 is selected main text, while upper basis is provisional. The uplift/praise construction at U04312 is not certified here. Newly restored compressed clauses and sound forms retain explicit provisional notes.

All 72 uncertainty-bearing golden objects retain their flags in the machine edition and linked endnotes. Original omission queries are kept as source annotations, not presented as proof that restored text remains missing. The first portrait-caption line and boundary graphics are represented without invented decipherments.

This review does not alter or certify the exhaustive manuscript-comparison project, perform new scan reading, approve new glossary entries, or claim independent human palaeographic review. Validation measures preservation, coverage and internal consistency rather than a translation-accuracy percentage.

Build and check with [build_translation.py](../2026-09-26-full-draft/golden-review/build_translation.py). Validation results are recorded in VALIDATION.json.
