<a id="phase-d-review"></a>
# Post-translation review — current working text

**Task:** POST_TRANSLATION_REVIEW · **Mode:** review-and-revise · **Active continuation:** DTG-PD-20261005-Astra-05 · **Original review session:** DTG-PD-20261005-Astra-01 · **Reviewer:** GPT-6 Astra Pro, this review session, distinct from the September 26 authoring run and October 1 source-reconciliation coordinator. Review of the input is independent of those runs; checks of this session's repairs are self-checks, not a second independent review or human certification.

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


### Continuation 04 input freeze — 2026-10-05

Reviewer/session **DTG-PD-20261005-Astra-04**, GPT-6 Astra Pro, continues this same independent review of the original authoring input; repair verification remains self-check. Clean local and remote review-branch input: `a0a76b94593b779222e5bbe69f9ccb37a2d9b5b2`; remote main still `fc3a443ba5987efb0b132990bf131a236fa57320`. The 1,150-pair coverage and prior evidence are preserved, not claimed as a fresh reread of all those pairs in this continuation. Current English input SHA-256: `2a21fc15d3f67ad01941a865b2ea1ee5cfea0b1989897bbedc1772bb5dd2bfcd`. Source, golden, policy, format/lineage hashes match the frozen table above. PR #5 adoption is reconfirmed merged; no later local override or review-branch PR exists at this checkpoint. Existing worktrees, recovery branches, historical readers and tags are untouched. All required active policy and repository instructions, current reports/usage records and operative format documents were read; root FORMAT.md remains absent.

The pre-edit read-only integrity replay passed all 246 existing pair operations (225 English operations in 201 pairs; 213 changed pairs including note-only changes), prior notes/usages, all 2,667 ordered IDs and 700 English local-link targets. This is mechanical preservation evidence, not new semantic coverage. The finite scope remains the whole 2,667-pair work.

### Continuation 05 input freeze — 2026-10-05

Reviewer/session **DTG-PD-20261005-Astra-05**, GPT-6 Astra Pro, continues the independent input review, not the September authoring run. Clean local and fetched remote branch input **66e2607ac0de36b966dfd0f78c927130005b815e**; remote main remains **fc3a443ba5987efb0b132990bf131a236fa57320** and policy-adoption PR #5 is merged. English input SHA-256 **e0cf94a3abf547aa62546ceb893eea13e604ea5bce7304c7504d82399229fcd7**. The previous 1,742-pair coverage is preserved, not claimed as a fresh reread in continuation 05. All required active instructions, the complete standard and 283 × 8 glossary were read; root FORMAT.md remains absent, and the operative paired format was read instead. No later owner-approved local override was found. Fixed source/policy/golden/format/lineage hashes match the table above. Both existing worktrees, unpublished recovery branches, all historical outputs and remote release refs were inspected and preserved. No review PR existed at entry.

Pre-edit exact replay passed all **408** prior pair operations and **355** changed pairs; fixed bytes and 2,667 IDs/order match. All 2,660 lineage records reproduce. Actual pre-edit paired validation fails at the historical protected-glossary gate. The paired suite was actually rerun: **64 tests, 53 pass, 9 fail, 2 error**, with the historical exact-English gate preempting affected checks. These are inherited contract failures, not passed semantic tests. No regression example is counted executed merely from reading it.

<a id="phase-d-coverage"></a>
## Finite whole-work scope and actual coverage

File/source order, not numerical ID order, governs. Chapter 1 includes the title/opening and the twelve split children DTG-002661–DTG-002672; the five retired v1 IDs are not reintroduced. The complete ordered inventory remains the existing canonical source and `paired/v2/PAIR-AUDIT.json`, not a second segmentation ledger. Total scope: **2,667 pairs / 5,484 golden objects** (5,466 original anchors and 18 additions); formats: 48 prose, 2,448 verse, 2 h1, 0 h2, 169 h3.

<!-- phase-d-coverage-start -->
| Part | Expected pairs | Expected source-ordered range | Actually semantically reviewed | Status |
|---|---:|---|---:|---|
| chapter-01 | 1199 | DTG-000001 → DTG-001192 | 1199 (ordinals 1–1199; through DTG-001192) | Covered; linked questions remain |
| chapter-02 | 543 | DTG-001193 → DTG-001735 | 543 (ordinals 1200–1742; through DTG-001735) | Covered; linked questions remain |
| chapter-03 | 354 | DTG-001736 → DTG-002089 | 354 (ordinals 1743–2096; through DTG-002089) | Covered; linked questions remain |
| chapter-04 | 237 | DTG-002090 → DTG-002326 | 237 (ordinals 2097–2333; through DTG-002326) | Covered; linked questions remain |
| chapter-05 | 211 | DTG-002327 → DTG-002537 | 0 | Not started |
| chapter-06 | 108 | DTG-002538 → DTG-002645 | 0 | Not started |
| closing-material | 15 | DTG-002646 → DTG-002660 | 0 | Not started |

<!-- phase-d-coverage-end -->

The fixed golden has **72 uncertainty-bearing objects in 66 pairs**; this is a source-qualification inventory, not the final count of unresolved translation questions. Opening inscriptions, caption, empty annotation carriers, chapter-transition metadata and closing graphics remain in scope. Exact inherited pairs:

`DTG-000001`, `DTG-000002`, `DTG-000003`, `DTG-000004`, `DTG-000005`, `DTG-000008`, `DTG-002662`, `DTG-000016`, `DTG-000023`, `DTG-000034`, `DTG-000038`, `DTG-000048`, `DTG-000059`, `DTG-000068`, `DTG-000070`, `DTG-000080`, `DTG-002665`, `DTG-002666`, `DTG-000166`, `DTG-000167`, `DTG-000181`, `DTG-000182`, `DTG-000183`, `DTG-000563`, `DTG-000584`, `DTG-000696`, `DTG-000709`, `DTG-002667`, `DTG-002668`, `DTG-002671`, `DTG-001187`, `DTG-001191`, `DTG-001192`, `DTG-001331`, `DTG-001332`, `DTG-001333`, `DTG-001334`, `DTG-001354`, `DTG-001519`, `DTG-001735`, `DTG-001826`, `DTG-001904`, `DTG-001905`, `DTG-001906`, `DTG-002088`, `DTG-002089`, `DTG-002091`, `DTG-002195`, `DTG-002218`, `DTG-002284`, `DTG-002325`, `DTG-002326`, `DTG-002396`, `DTG-002480`, `DTG-002486`, `DTG-002495`, `DTG-002514`, `DTG-002536`, `DTG-002537`, `DTG-002559`, `DTG-002585`, `DTG-002624`, `DTG-002633`, `DTG-002645`, `DTG-002653`, `DTG-002654`.

Review protocol: read every source/English pair and associated notes in source order, apply Q1–Q9, I §8.1 and III, read continued sentences across pair boundaries, then perform bidirectional terminology and continuous-English checks. Pattern matches are candidates only. Findings are recorded below before repairs. No percentage of accuracy will be inferred from counts.

<a id="phase-d-findings"></a>
## Current findings and dispositions

The freeze checkpoint had no semantic findings. Batch records below distinguish read coverage, evidence recorded before repair, and actual application/self-check status. Coverage is not inferred from inventory or structural checks.

<a id="phase-d-batch-01"></a>
### Batch 01 — source ordinals 1–100 (DTG-000001 → DTG-000098)

All 100 pairs and all 50 first-encountered attached historical/reconciliation notes were read against the current golden strings, including the opening material and continued clauses. Q1–Q9, I §8.1 and III were applied. The full rows for the correction families below were re-read, including exceptions and allowed forms. **Evidence was recorded before application. All 17 scoped repairs across 15 pairs are now applied and self-checked.**

| Finding | Severity / confidence | Source-based rationale and bounded scope |
|---|---|---|
| PD-T01 | Terminology / high | P1 literary-use exception: explicit titles (including the foreign-title's provisional English rendering), the king of texts gathering all teachings, and the family of texts from which teaching is proclaimed denote tantric scriptures. Use tantra, not continuum. This does not license replacing path-continuum at DTG-000092 or every nearby rgyud. Foreign lettering and the proposed All-Penetrating Word title remain qualified. |
| PD-T02 | Terminology / high | P2 cyclic-existence terminology; the opening coordinated འཁོར་དང་འདས་པ is the recognizably paired technical contrast, not an unrelated isolated 'das. Retain both members, the temporal beginning, and the path's possession relation. |
| PD-T03 | Terminology / high | P2 complete sems can equivalent is karmic being; plural preserved. This does not change 'gro ba, las can, or bare sems. |
| PD-T04 | Terminology / high | P2 dngos grub requires spiritual accomplishment. Retain ultimate, supreme, plurality and the following negation of effort. |
| PD-T05 | Terminology / high | P2 actual spatial bar snang is open sky here, distinct from nam mkha' space in the same clause. No interval or accidental adverbial substring is involved. |
| PD-T06 | Presentation / high | P2 mandates mandala without diacritics in this technical use. No semantic change; thabs cig remains together, not methods. |
| PD-T07 | Rhetorical function / high | Repeated kye kye is the repeated vocative O, O. There is no nyon/listen imperative to translate at this location. Preserve both vocatives, the quotation, Blessed One, and separately written e ma (still locally provisional). |
| PD-E01 | Presentation / high | Lowercase from continues the same sentence after the comma. It does not introduce a second sentence or change source verse form. |
| PD-S01 | Syntax / high | U00116 བྱིན་གྱིས་རླབས་ཀྱིས is instrumental. English incorrectly made blessing the actor. Through blessing plus a passive predicate preserves the instrument without inventing a named agent; the preceding speech instrument and the provisional its-own-sound reference remain. |
| PD-S02 | Modifier attachment / high | U00119's genitive participle བཅུད་བསྡུས་པའི qualifies the following king of tantras, not the preceding kalaviṅka sound. Move the existing English relative clause immediately after its head within the same unchanged pair. Keep the teacher as speaker, 360 sounds, temporal relation, and quintessence. |

The following exact scoped repair records are also the application checklist. Tibetan is quoted byte-for-byte from the frozen pair; newlines are escaped in JSON. Two repairs in DTG-000047 are explicitly sequenced, not counted as two changed pairs.

<!-- phase-d-batch-01 -->
```json
[
  {
    "pair": "DTG-000002",
    "golden": [
      "U00002"
    ],
    "tibetan": "རཏྞཱཀཱརཤབྡམཧཱཔྲསཾགཏནྟྲནཱམབིཧརཏིསྨ།།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000004",
    "golden": [
      "U00004"
    ],
    "tibetan": " རིན་པོ་ཆེ་འབྱུང་བར་བྱེད་པ་སྒྲ་ཐལ་འགྱུར་ཆེན་པོའི་རྒྱུད་ཅེས་བྱ་བ་བཞུགས།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000005",
    "golden": [
      "U00005",
      "U00006"
    ],
    "tibetan": "གཾགརྦམཏགཱ རྒྱ་གར་སྐད་དུ།\n རཏྣ་ཀ་ར་ཤབྡ་མ་ཧཱ་པྲ་སཾ་ག་ཏནྟྲ་ནཱ་མ།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000006",
    "golden": [
      "U00007",
      "U00008"
    ],
    "tibetan": " བོད་སྐད་དུ།\n རིན་པོ་ཆེ་འབྱུང་བར་བྱེད་པ་སྒྲ་ཐལ་འགྱུར་ཆེན་པོའི་རྒྱུད་ཅེས་བྱ་བ།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000047",
    "golden": [
      "U00117",
      "U00118",
      "U00119",
      "U00120",
      "U00121",
      "U00122",
      "U00123"
    ],
    "tibetan": "དེ་ནས་ཕྱོགས་བྲལ་ནམ་མཁའ་ལས། །\nཀ་ལ་པིང་ཀའི་སྒྲ་དབྱངས་ལས། །\nབསྟན་པ་ཀུན་གྱི་བཅུད་བསྡུས་པའི། །\nརྒྱུད་ཀྱི་རྒྱལ་པོ་འདི་ཉིད་ནི། །\nཚིག་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང་། །\nབརྒྱ་ཕྲག་གསུམ་དང་དྲུག་ཅུ་ཡི། །\nསྒྲ་ལས་དྲངས་ཏེ་སྟོན་པས་གསུངས། །",
    "before": "this very king of continua,",
    "after": "this very king of tantras,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000060",
    "golden": [
      "U00158",
      "U00159",
      "U00160",
      "U00161"
    ],
    "tibetan": "དེ་ལྟར་གསུངས་པའི་ཆོ་འཕྲུལ་དུ། །\nརྒྱུད་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང་། །\nརྩ་བའི་སྒྲ་ཚིག་ཐལ་འགྱུར་ལས། །\nཐམས་ཅད་ངེས་འབྱུང་བསྟན་པར་འཕྲོས། །",
    "before": "even before all continua,",
    "after": "even before all tantras,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-002662",
    "golden": [
      "U00013",
      "U00014",
      "U00015",
      "U00016",
      "U00017"
    ],
    "tibetan": "འཁོར་དང་འདས་པའི་ཐོག་མར་ནི། །\nརང་བྱུང་བྱས་པ་མེད་པ་ལས། །\nའབྱུང་བ་འདུས་པའི་ཕུང་པོར་ཤར། །\n ས་ཆུ་མེ་རླུང་འབྱུང་བ་བཞི། །\nདབུས་སུ་རླུང་སེམས་རྒྱུ་དང་རྐྱེན། །",
    "before": "At the beginning of samsara and what is beyond it,",
    "after": "At the beginning of cyclic existence and transcendence of sorrow,",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000061",
    "golden": [
      "U00162",
      "U00163"
    ],
    "tibetan": "བསྟན་པ་དམ་པའི་འདུ་མཆེད་གྲུབ། །\nགསུངས་པས་འཁོར་བ་ནུབ་པར་བྱེད། །",
    "before": "by its being spoken, samsara is made to subside.",
    "after": "by its being spoken, cyclic existence is made to subside.",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000092",
    "golden": [
      "U00209"
    ],
    "tibetan": "འཁོར་བའི་ལམ་རྒྱུད་གང་གིས་བཅད། །",
    "before": "What cuts the continuum of samsara's path?",
    "after": "What cuts the continuum of the path of cyclic existence?",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000086",
    "golden": [
      "U00203"
    ],
    "tibetan": "སེམས་ཅན་དུས་ཀྱི་རིམ་པ་གང༌། །",
    "before": "What are the successive ages of sentient beings?",
    "after": "What are the successive ages of karmic beings?",
    "finding": "PD-T03"
  },
  {
    "pair": "DTG-000040",
    "golden": [
      "U00097",
      "U00098",
      "U00099"
    ],
    "tibetan": "དངོས་གྲུབ་མཆོག་རྣམས་མཐར་ཐུག་པའི། །\nའབད་ཅིང་རྩོལ་བ་མ་ཡིན་པས། །\nགང་སུ་འཕྲད་པ་གྲོལ་བར་ངེས། །",
    "before": "Since the ultimate supreme accomplishments",
    "after": "Since the ultimate supreme spiritual accomplishments",
    "finding": "PD-T04"
  },
  {
    "pair": "DTG-000045",
    "golden": [
      "U00107",
      "U00108",
      "U00109",
      "U00110",
      "U00111",
      "U00112",
      "U00113"
    ],
    "tibetan": "དེ་ལྟར་དངོས་ཀྱི་བསྟན་པ་ལས། །\nགཟུགས་བརྙན་ཆོ་འཕྲུལ་འདི་ལྟ་བུ། །\nསུས་ཀྱང་བརྗོད་དུ་མེད་པར་ནི། །\nནམ་མཁའ་མི་འབྱེད་བར་སྣང་ལས། །\nཚིག་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང༌། །\nདགུ་གཉིས་བཞི་ཡི་ཡང་སྟེང་ནས། །\nཚངས་པ་ཆེན་པོའི་དབྱངས་སུ་བསྒྲགས། །",
    "before": "[was proclaimed] from the sky, undivided from space:",
    "after": "[was proclaimed] from the open sky, undivided from space:",
    "finding": "PD-T05"
  },
  {
    "pair": "DTG-000067",
    "golden": [
      "U00176",
      "U00177",
      "U00178"
    ],
    "tibetan": "དབྱེར་མི་ཕྱེད་པས་སྙོམས་ཞུགས་ཏེ། །\nརང་བཞིན་རྫོགས་པ་ཆེན་པོ་ཡི། །\nདཀྱིལ་འཁོར་གཅིག་ཏུ་ཐབས་ཅིག་འཁོད། །",
    "before": "abided together in a single maṇḍala.",
    "after": "abided together in a single mandala.",
    "finding": "PD-T06"
  },
  {
    "pair": "DTG-000069",
    "golden": [
      "U00180",
      "U00181",
      "U00182",
      "U00183"
    ],
    "tibetan": "དེ་ནས་གཅིག་དང་ཐ་མི་དད། །\nརང་བཞིན་དག་པའི་འཁོར་རྣམས་ལས། །\nལྷ་དབང་གིས་ནི་འདི་སྐད་གསོལ། །\nཨེ་མ་ཀྱེ་ཀྱེ་བཅོམ་ལྡན་འདས། །",
    "before": "‘Ema! Listen, listen, Blessed One!",
    "after": "‘Ema! O, O, Blessed One!",
    "finding": "PD-T07"
  },
  {
    "pair": "DTG-000069",
    "golden": [
      "U00180",
      "U00181",
      "U00182",
      "U00183"
    ],
    "tibetan": "དེ་ནས་གཅིག་དང་ཐ་མི་དད། །\nརང་བཞིན་དག་པའི་འཁོར་རྣམས་ལས། །\nལྷ་དབང་གིས་ནི་འདི་སྐད་གསོལ། །\nཨེ་མ་ཀྱེ་ཀྱེ་བཅོམ་ལྡན་འདས། །",
    "before": "From among the retinue whose intrinsic nature was pure,",
    "after": "from among the retinue whose intrinsic nature was pure,",
    "finding": "PD-E01"
  },
  {
    "pair": "DTG-000046",
    "golden": [
      "U00114",
      "U00115",
      "U00116"
    ],
    "tibetan": "དེ་ནས་ཆོས་ཉིད་ནམ་མཁའ་ལས། །\nཁྱབ་འཇུག་ཆེན་པོའི་གསུང་གིས་ནི། །\nབྱིན་གྱིས་རླབས་ཀྱིས་རང་སྒྲར་སྟོན། །",
    "before": "blessing displayed it as its own sound.",
    "after": "through blessing, it was displayed as its own sound.",
    "finding": "PD-S01"
  },
  {
    "pair": "DTG-000047",
    "golden": [
      "U00117",
      "U00118",
      "U00119",
      "U00120",
      "U00121",
      "U00122",
      "U00123"
    ],
    "tibetan": "དེ་ནས་ཕྱོགས་བྲལ་ནམ་མཁའ་ལས། །\nཀ་ལ་པིང་ཀའི་སྒྲ་དབྱངས་ལས། །\nབསྟན་པ་ཀུན་གྱི་བཅུད་བསྡུས་པའི། །\nརྒྱུད་ཀྱི་རྒྱལ་པོ་འདི་ཉིད་ནི། །\nཚིག་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང་། །\nབརྒྱ་ཕྲག་གསུམ་དང་དྲུག་ཅུ་ཡི། །\nསྒྲ་ལས་དྲངས་ཏེ་སྟོན་པས་གསུངས། །",
    "before": "which gathers the quintessence of all teachings,\nthis very king of tantras,",
    "after": "this very king of tantras,\nwhich gathers the quintessence of all teachings,",
    "finding": "PD-S02",
    "sequence_note": "Applied after PD-T01 in the same batch; frozen input has continua at this location."
  }
]
```
<!-- /phase-d-batch-01 -->

<a id="phase-d-batch-01-nochange"></a>
**Important retentions / rejected false positives.** DTG-000008's incomplete portrait caption and DTG-000070/U00187's separation of the reported purpose variant from enlightened intent already follow the current golden source; old criticisms are not current defects. DTG-000019/U00035 is only a source-delimiter change. DTG-000020/U00039 already reads a thousand [stamens], not the historical upper-part reading. The lotus construction remains provisionally linked to N-004/G-U00039; relocating its descriptive modifiers would require settling more of that compressed construction than this repair authorizes. DTG-000025's distinguishing marks retains the canonical noun marks and a contextual descriptive adjective; a glossary substring alone is not sufficient reason to delete it. The source headings' gleng gzhi remains introductory setting, not Ground. DTG-000057's gzhi ma foundation and DTG-000092's path-continuum are not the literary rgyud/title exception. DTG-000035's longer 'od zer khyim is not proven identical to the listed 'od khyim whole expression. DTG-000067's thabs cig means together; DTG-000044's las can is not sems can. The three embodiment names and complete enjoyment component remain intact, including recognizable short forms.

<a id="phase-d-batch-01-open"></a>
**Local unresolved constructions retained, not silently approved.** The existing notes continue to carry the opening palace/instrumental and retinue groupings (N-003), realm/lotus location and numerical supply (N-004/G-U00039), the unspecified five/two (N-005), khams dang gud bcas (N-006), seventeen yang zhun (N-007), nine–two–four (N-008), the three-intent punctuation (N-009), phonological labels/numerical sets (N-010), fourteen–two and dgod (N-011), one-with-this (N-012/G-U00180), and the byer zug snyoms triad (N-014). Opening foreign strings/caption retain their exact linked qualifications. These are inherited open questions, not newly discovered defects.

Additional exact review questions: DTG-000023/U00048 རྒྱུད་འབྱུང་གླེང་གཞི (arising of the continuum) may denote this scripture's emergence, but this occurrence's scope is retained pending comparison with its later explanation; title proximity alone does not apply P1. DTG-000030/U00069 བསམ་གཏན་དང་པོར (first meditative absorption) requires the shared bsam gtan/ting nge 'dzin family distinction; meditative stability is a proposal, not a silently adopted default. In the same pair, U00070 མངོན་དུ་བྱ་དང་བྱེད་པ་བྲལ (free of manifest doing and agency) permits action/agent versus two-action analysis; no agent is inserted from the glossary alone. DTG-000042/U00101 གཞན་འབད་པ (other exertion versus others' exertion), DTG-000043/U00104 ཆོས་ཀྱི་སྐུ་ལ་ངེས་བརྒྱུད (transmission's attachment/reference), and DTG-000069/U00183 ཨེ་མ (Ema, distinct from full e ma ho) remain construction-specific questions. The following explanations, an explicit parallel, or owner-approved commentary/terminology reconciliation would settle these; retained wording is not a new book-wide default. Whole-work family checking remains pending.

**Notes/usage disposition pending integration:** N-T03's acoustic sound treatment is now approved within P1's actual acoustic scope; N-T04's cognitive thugs/awakened mind is now P2 canonical. Their historical absent/proposed statements are not current policy. N-T01's keep-continuum title instruction is superseded only by P1's literary exception; All-Penetrating Word remains proposed. N-T09's Ground capitalization is approved presentation, not automatic approval of each technical-sense parse. N-T07's short embodiment forms are recognized in their explicit three-embodiment context; no shared entry is added. N-T15's finite hold/maintain constructions are not nominal apprehending subject. Original approval history remains untouched.

<a id="phase-d-notes-01"></a>
### PD-N01 — current note-status reconciliation (recorded before application)

Severity: note-status inconsistency; confidence: high. P1/P2 supersede the earlier proposed/absent terminology statuses only within their approved scopes. The original research notes and original ten usage records remain intact. The current index and existing usage file receive dated dispositions linked to this review rather than rewritten historical approvals. The paired footer needs one explanatory paragraph because its inherited Current English quotations refer to the October 1 checkpoint, not necessarily the corrected current pair.

**Before:** no Phase D notice after `## Golden-source footnotes and endnotes` in `paired/translation.md`; no Phase D disposition for the following legacy IDs in `LEGACY-NOTES.md`; no `phase_d_dispositions` property in existing `USAGES.json`.

**After, footer paragraph:**

> These source-reconciliation notes preserve the October 1 decision evidence. Each **Current English** quotation records the English selected at that historical checkpoint; it is not a second canonical translation of the revised pair. Current corrections and terminology dispositions are recorded in the [post-translation review](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-review). Original source evidence and approval history remain unchanged.

**After, current index/usage dispositions:** N-T01: P1 requires tantra in explicit textual titles; retain the unapproved whole-expression title and foreign-script qualifications. N-T03: acoustic sound is P1-approved only in actual acoustic contexts; word and whole expressions remain distinct. N-T04: cognitive/honorific standalone thugs as awakened mind is P2-approved, not still an absent entry. N-T09: P1 Ground capitalization is approved presentation, not approval of every contextual parse. N-T07: the observed three-embodiment short forms are locally supported realizations of established whole expressions, not new shared assignments. N-T15: the observed finite holding/maintaining uses are resolved as local transitive constructions, not an extension of the nominal apprehending-subject entry.

The affected initial usages are source-linked in the index and in `USAGES.json`. Their English need not change when it already meets the adopted rule. This note correction creates no new glossary assignment and does not certify occurrences outside the reviewed range.

<a id="phase-d-batch-02"></a>
### Batch 02 — source ordinals 101–200 (DTG-000099 → DTG-000197)

All 100 pairs and 30 newly encountered attached notes were read in source order under Q1–Q9, I §8.1 and III, including necessary cross-pair context. Complete applicable glossary rows and whole-expression boundaries were checked. **Evidence was recorded before application. All 25 scoped repairs across 23 additional pairs and one source-annotation note repair are applied and self-checked.**

Repeated findings PD-T01/02/06/07 extend only to the individually checked locations below. PD-T01 at DTG-000023 is now resolved from the complete literary construction together with the text's own explanation of its two introductory settings and six-chapter body (DTG-000183–000196), not title proximity alone. DTG-000195 is followed by an explicit distinction of the tantra's title and textual exposition. The P1 correction of the source annotation at U00272 remains in its note layer, with its earlier English explicitly historical.

| Finding | Severity / confidence | Rationale |
|---|---|---|
| PD-T08 | Terminology/coverage / high for missing practice label; moderate-high for local syntax | The current question omits the established ru shan category, secret preliminary, and leaves only the separate phyed separating predicate. Restore the practice reference as the setting of that separation, retaining both members of the identified 'khor 'das compound, the interrogative instrument, and the actual predicate. N-T11's unapproved literal-only proposal cannot override the complete glossary entry. This does not declare all literal separating verbs a named practice; the later reply remains part of the cross-context self-check. |
| PD-T09 | Terminology / high | All four gnad occurrences are the explicit bodily/contemplative key-point family. P2 requires key point(s), including the direct-perception and cultivation modifiers. |
| PD-T10 | Terminology / high | P2 bem po is matter, contrasted here with rig bcas, the aware. The question still explicitly asks about that contrast. Matter denotes the non-knowing side in this construction; it does not assert immobility, death, or that karmic beings cannot have material bodies. No generic body/entity term is replaced. |
| PD-T11 | Terminology / moderate-high | The question asks about the enlightened intent of grub mtha' as the organized doctrinal system, not a list of individual propositions. Use tenet system; no numerical assertion or philosophical modifier is added. Compare the later detailed reply before closing this local classification. |
| PD-T12 | Terminology / high | Preserve both words of P2 sacred pledge and the distinct sdom pa/vow member. The latter's standalone shared assignment is not approved by this repair. |
| PD-T13 | Terminology / high for bcud; whole-construction confidence remains provisional | In the nourishment-taking question bcud is the extract/concentration family, not receptacle inhabitants. P2 quintessence replaces the unapproved vital-essence label. Keep the existing whole construction and N-T16's open instrumental/nourishment interpretation; this is not approval of that complete practice expression or a reconstruction from a falsely assumed whole entry. |
| PD-T14 | Terminology / moderate-high | Conviction is the epistemic result of the Great Perfection teaching and of its common introductory setting, distinct from the explicit faith at DTG-000146. No personal trusting relationship or confidences set is asserted here. Preserve the future context, recipient, compiler possession and purpose. |
| PD-T15 | Terminology / high | The exact snying po occurrences require core, not quintessence; both core-teaching relations and the purpose of increasing it are preserved. Bare snying in the surrounding heart/pith-instruction epithets is not automatically this complete headword. |
| PD-T16 | Terminology / high | P2 lung in the teaching epithet is transmission. Remove the old proposal's non-source adjective authoritative without changing eye-of-transmission or equating lung with wind/stagnant neutrality. |
| PD-T17 | Terminology / high | The actual coordinated extraction contrast, gathering dwangs ma and separating snyigs ma in the body, supports pure extract and residue. Preserve their distinct actions/order and attested spelling; the physical part exception is not specifically required here. This does not turn dngos ma into an extract or identify a modern substance. |


<!-- phase-d-batch-02 -->
```json
[
  {
    "pair": "DTG-000023",
    "golden": [
      "U00048",
      "U00049"
    ],
    "tibetan": "རྒྱུད་འབྱུང་གླེང་གཞི་དང་པོ་ལ། །\nལྔ་པོ་རྣམས་ཀྱི་ས་བོན་འཛིན། །",
    "before": "In the initial setting for the arising of the continuum,",
    "after": "In the initial setting for the arising of the tantra,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000107",
    "golden": [
      "U00224"
    ],
    "tibetan": "གནད་ཀྱི་འབྱུང་བ་གང་དང་གང༌། །",
    "before": "Which elements belong to the crucial points?",
    "after": "Which elements belong to the key points?",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000111",
    "golden": [
      "U00228"
    ],
    "tibetan": "རིག་བཅས་བེམ་པོའི་བྱེ་བྲག་གང༌། །",
    "before": "What distinguishes the aware from the insentient?",
    "after": "What distinguishes the aware from matter?",
    "finding": "PD-T10"
  },
  {
    "pair": "DTG-000112",
    "golden": [
      "U00229"
    ],
    "tibetan": "གནད་རྣམས་རང་བཟློག་ཐབས་གང་ལགས། །",
    "before": "What method reverses the crucial points themselves?",
    "after": "What method reverses the key points themselves?",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000113",
    "golden": [
      "U00230"
    ],
    "tibetan": "གྲུབ་མཐའ་དགོངས་པ་གང་གིས་འགྲུབ། །",
    "before": "By what is the enlightened intent of the tenets established?",
    "after": "By what is the enlightened intent of the tenet system established?",
    "finding": "PD-T11"
  },
  {
    "pair": "DTG-000123",
    "golden": [
      "U00240"
    ],
    "tibetan": "དམ་ཚིག་སྡོམ་པ་ཅི་ལྟ་བུ། །",
    "before": "What are the pledges and vows like?",
    "after": "What are the sacred pledges and vows like?",
    "finding": "PD-T12"
  },
  {
    "pair": "DTG-000126",
    "golden": [
      "U00243"
    ],
    "tibetan": "མངོན་སུམ་གནད་ལ་ཅི་ལྟར་བསྒྲེ། །",
    "before": "How is this applied to the crucial point of direct perception?",
    "after": "How is this applied to the key point of direct perception?",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000127",
    "golden": [
      "U00244"
    ],
    "tibetan": "འཁོར་འདས་རུ་ཤན་གང་གིས་ཕྱེད། །",
    "before": "By what are samsara and nirvana separated?",
    "after": "By what are cyclic existence and transcendence of sorrow separated in the secret preliminary?",
    "finding": "PD-T08 / PD-T02"
  },
  {
    "pair": "DTG-000135",
    "golden": [
      "U00252"
    ],
    "tibetan": "འཁོར་བའི་ཆུ་རྒྱུན་ཅི་ཡིས་གཅོད། །",
    "before": "By what is samsara's flowing stream cut?",
    "after": "By what is the flowing stream of cyclic existence cut?",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000136",
    "golden": [
      "U00253"
    ],
    "tibetan": "བཅུད་ཀྱིས་ལེན་པ་ཇི་ལྟ་བུ། །",
    "before": "What is the taking of nourishment from vital essences?",
    "after": "What is the taking of nourishment from quintessence?",
    "finding": "PD-T13"
  },
  {
    "pair": "DTG-000146",
    "golden": [
      "U00263",
      "U00264",
      "U00265",
      "U00266"
    ],
    "tibetan": "བདག་ལ་རིམ་པ་གསལ་ཕྱེ་བས། །\nམ་འོངས་པ་ཡི་དུས་རྣམས་སུ། །\nའདི་ལ་དད་ཅིང་འདུན་པ་ཀུན། །\nརྫོགས་ཆེན་འདི་ལ་ཡིད་ཆེས་ནས། །",
    "before": "will come to trust this Great Perfection.",
    "after": "will come to have conviction in this Great Perfection.",
    "finding": "PD-T14"
  },
  {
    "pair": "DTG-000148",
    "golden": [
      "U00268",
      "U00269"
    ],
    "tibetan": "འཁོར་བའི་ཐ་མ་ཟད་ནས་ནི། །\nམྱ་ངན་འདས་པའི་ལམ་སྣ་ཟིན། །",
    "before": "When samsara is exhausted to its very end,",
    "after": "When cyclic existence is exhausted to its very end,",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000148",
    "golden": [
      "U00268",
      "U00269"
    ],
    "tibetan": "འཁོར་བའི་ཐ་མ་ཟད་ནས་ནི། །\nམྱ་ངན་འདས་པའི་ལམ་སྣ་ཟིན། །",
    "before": "they will find the entrance to the path beyond sorrow.",
    "after": "they will find the entrance to the path of transcendence of sorrow.",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000156",
    "golden": [
      "U00287",
      "U00288"
    ],
    "tibetan": "སངས་རྒྱས་རྣམས་ཀྱིས་མ་གསུངས་པ། །\nརྒྱུད་གཞན་ལས་ནི་ཁྱད་འཕགས་འདི། །",
    "before": "surpasses other continua.",
    "after": "surpasses other tantras.",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000157",
    "golden": [
      "U00289",
      "U00290",
      "U00291",
      "U00292"
    ],
    "tibetan": "ཁམས་གསུམ་གནས་སུ་མི་ལྡོག་ཕྱིར། །\nརབ་ཏུ་གསང་ཆེན་ངེས་པའི་བཀའ། །\nབསྟན་པའི་སྙིང་པོ་འཕེལ་དོན་དུ། །\nཐེག་པའི་ཡང་རབ་རྩེ་མོ་སྟེ། །",
    "before": "for increasing the quintessence of the teaching,",
    "after": "for increasing the core of the teaching,",
    "finding": "PD-T15"
  },
  {
    "pair": "DTG-000158",
    "golden": [
      "U00293",
      "U00294",
      "U00295",
      "U00296",
      "U00297",
      "U00298",
      "U00299"
    ],
    "tibetan": "ཆོས་ཀྱི་མེ་ལོང་དོན་གྱིས་སྡུད། །\nབཀའ་ཡི་འགྲེལ་པ་མན་ངག་སྙིང་། །\nརང་བཞིན་གསང་བ་རྫོགས་པ་ཆེ། །\nསྙིང་གི་ཏི་ཀ་ལུང་གི་མིག །\nཡང་གསང་ལྡེ་མིག་བལྟ་བའི་ཕུགས། །\nསྤྱོད་པའི་སྦྱང་ས་བསྒོམ་པའི་གནད། །\nམངལ་གྱི་རྒྱུན་གཅོད་ངན་སོང་ཕྱག །",
    "before": "the heart-commentary, the eye of authoritative transmission,",
    "after": "the heart-commentary, the eye of transmission,",
    "finding": "PD-T16"
  },
  {
    "pair": "DTG-000158",
    "golden": [
      "U00293",
      "U00294",
      "U00295",
      "U00296",
      "U00297",
      "U00298",
      "U00299"
    ],
    "tibetan": "ཆོས་ཀྱི་མེ་ལོང་དོན་གྱིས་སྡུད། །\nབཀའ་ཡི་འགྲེལ་པ་མན་ངག་སྙིང་། །\nརང་བཞིན་གསང་བ་རྫོགས་པ་ཆེ། །\nསྙིང་གི་ཏི་ཀ་ལུང་གི་མིག །\nཡང་གསང་ལྡེ་མིག་བལྟ་བའི་ཕུགས། །\nསྤྱོད་པའི་སྦྱང་ས་བསྒོམ་པའི་གནད། །\nམངལ་གྱི་རྒྱུན་གཅོད་ངན་སོང་ཕྱག །",
    "before": "the training ground of activity, the crucial point of cultivation,",
    "after": "the training ground of activity, the key point of cultivation,",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000159",
    "golden": [
      "U00300",
      "U00301"
    ],
    "tibetan": "གསང་བ་མཆོག་གི་རྒྱུད་བཤད་ཀྱིས། །\nརྡོ་རྗེ་ཡང་འཛིན་འཁོར་རྣམས་ཉོན། །",
    "before": "I will explain the supreme secret continuum;",
    "after": "I will explain the supreme secret tantra;",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000162",
    "golden": [
      "U00307"
    ],
    "tibetan": "དེས་ན་བསྟན་པའི་སྙིང་པོ་བསྟན། །",
    "before": "Therefore I teach the quintessence of the teaching.",
    "after": "Therefore I teach the core of the teaching.",
    "finding": "PD-T15"
  },
  {
    "pair": "DTG-000163",
    "golden": [
      "U00308"
    ],
    "tibetan": "ཀྱེ་ཀྱེ་དགའ་བར་བྱེད་པས་ཟུང་། །",
    "before": "Listen, listen, Joy-Maker—take hold of this!",
    "after": "O, O, Joy-Maker—take hold of this!",
    "finding": "PD-T07"
  },
  {
    "pair": "DTG-000167",
    "golden": [
      "U00319",
      "U00320",
      "U00321",
      "U00322"
    ],
    "tibetan": " འབྱུང་བའི་དགོས་པ་འདི་ལྟ་སྟེ། །\nཆུ་ནི་དྭངས་མ་སྡུད་པ་དང་། །\nསྙིགས་མ་རྣམས་ནི་འབྱེད་པའི་ལས། །\nསོ་སོའི་ལུས་ལ་བྱེད་པས་ན། །",
    "before": "Water gathers the refined part\nand performs the activity of separating the dregs",
    "after": "Water gathers the pure extract\nand performs the activity of separating the residue",
    "finding": "PD-T17"
  },
  {
    "pair": "DTG-000178",
    "golden": [
      "U00336",
      "U00337"
    ],
    "tibetan": "འབྱུང་བཞི་དག་གི་དཀྱིལ་འཁོར་ཆེ། །\nལུས་སོགས་ གྲུབ་པའི་རྒྱུ་བྱས་ཏེ། །",
    "before": "The great maṇḍala of these four elements",
    "after": "The great mandala of these four elements",
    "finding": "PD-T06"
  },
  {
    "pair": "DTG-000187",
    "golden": [
      "U00357",
      "U00358",
      "U00359",
      "U00360"
    ],
    "tibetan": "ཐེག་གཞན་རྣམས་དང་སྒོ་བསྟུན་ཕྱིར། །\nཐུན་མོང་དག་གི་གླེང་གཞི་ཡིས། །\nསྡུད་པ་རང་གི་འཁོར་རྣམས་ལ། །\nཡིད་ཆེས་བྱ་ཕྱིར་བསྟན་པ་སྟེ། །",
    "before": "is taught to inspire trust",
    "after": "is taught to inspire conviction",
    "finding": "PD-T14"
  },
  {
    "pair": "DTG-000195",
    "golden": [
      "U00374",
      "U00375"
    ],
    "tibetan": "ཨེ་མ་རྒྱུད་དག་ངེས་འབྱུང་བ། །\nདགོངས་པ་རྣམ་པ་གཉིས་ཡིན་ཏེ། །",
    "before": "Ema! In the definite arising of the continua,",
    "after": "Ema! In the definite arising of the tantras,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000196",
    "golden": [
      "U00376",
      "U00377"
    ],
    "tibetan": "རིག་པ་རང་སྣང་བློ་ཅན་ལ། །\nརྒྱུད་ཀྱི་མཚན་དོན་རྣམ་ཕྱེ་སྟེ། །",
    "before": "the meaning of the continuum's title is distinguished.",
    "after": "the meaning of the tantra's title is distinguished.",
    "finding": "PD-T01"
  },
  {
    "note": "G-U00272",
    "golden": [
      "U00272"
    ],
    "source_role": "separate source annotation SCAN-CH1-LAYER-00272",
    "tibetan": "རྒྱུད་ཀྱི་ཆེ་བ་རྣམ་པར་བཀོད་པའི་བཀོད་པ",
    "before": "English: The array setting out the greatness of the continuum. This is a separate structural note, not words inside the main subject phrase.",
    "after": "English at the October 1 checkpoint (historical): The array setting out the greatness of the continuum. This is a separate structural note, not words inside the main subject phrase.\n\n    **Current source-annotation English (Phase D):** The array setting out the greatness of the tantra. This remains a separate structural note, not part of the main subject phrase. [Review evidence](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-batch-02).",
    "finding": "PD-T01 / PD-N02"
  }
]
```
<!-- /phase-d-batch-02 -->

<a id="phase-d-batch-02-dispositions"></a>
**No-change checks:** DTG-000115's generic bsgrub accomplishment is not dngos grub/spiritual accomplishment. DTG-000118/000125/000160/000193's spros constructions are not automatically the listed spros bral whole expression; their exposition/elaboration functions are retained. Viewing at DTG-000131 remains a grammatical view-family realization, not a newly introduced gaze entry. DTG-000151's mdangs/luster remains distinct from gdangs/radiance and from unreviewed gzi mdangs cases. Crucially, DTG-000176's whole 'gul 'phrig/vibrating and fluttering is already canonical; it must not be changed to 'gyu/movement by a fuzzy-form comparison. The body/limbs and solid/hollow-organ metaphor in DTG-000184–000190 remains a metaphor for this text, not a new source edition or a list of seven chapters. DTG-000192's mdo means briefly here, not the longer discourse-collection label. DTG-000159's generic vajra-holding retinue is not silently named Vajradhara. Earth supporting a foundation and wind sustaining the body are actual finite holding constructions, not the nominal apprehending-subject entry. The seventy/sixty-six source annotation and the singly displayed first-reply heading remain in their proper layers. The current sel/increases variant separation at DTG-000172 is already correct and remains qualified; no source substitution occurs.

**Inherited questions retained:** N-T43's standalone lama/guru proposal; N-T51's vow; N-T16's complete bcud kyis len pa construction (now using P2 quintessence); N-T17's rgyun/flow and separate womb-succession epithet; N-019's glen pa/simple force; N-020's sixty-limbed melody and unwritten manifestation attachment; N-021's rab gtser/disciplined; N-022's heart-commentary and sweeper epithets; N-023/G-U00316's ngang gzhi bab/settling-of-basic-condition; N-T18's compressed gradual/simultaneous audience; and N-026's audience relation remain exact, linked local treatments. Neither proposed meditative stability nor superficial replaces bsam gtan or kun rdzob globally. Ema at DTG-000155/000195 belongs with the earlier exact e ma question, not automatic e ma ho expansion.

**Additional bounded construction questions:** DTG-000174/U00331 `དགོས་པ་དྲོད་རྣམས་ཤེས་པར་བྱེད། །` is presently It makes one know its purpose in the forms of warmth. The neighboring purpose instructions favor an instructional reading, while byed permits a causative analysis; do not silently add an element as knowing-agent. DTG-000175/U00332 `རླུང་གིས་སྟོངས་དང་འདེགས་པ་དང༌། །` is presently Wind supports and lifts: the exact stongs lexical force needs a construction/lexicon parallel, not emendation to another spelling. DTG-000180/U00340 `འབྱུང་བ་ཆེན་པོ་རྒྱུ་གཅིག་པས། །` retains having a single cause, but being a single cause versus common causal origin needs comparison with the complete causal account. DTG-000181/U00342–343 `དེས་ན་དགོས་པ་རང་དང་གཞན། ། བྱ་བ་རྫོགས་པའི་དོན་ལ་མཁས། །` currently makes purposes the skilled subject; elements as the implicit subject and purposes as its complement is an alternative, but the exact attachment remains open alongside the existing golden qualification. DTG-000188/U00361 `འདུལ་གཞི་ལས་ནི་འདུལ་བྱེད་དུ། །` (Ground of training) requires a supported compound-level basis/trainee versus technical-Ground reading; capitalization alone does not resolve it. Explicit source commentary, an attested constructional parallel, or a later unambiguous internal explanation would settle these. They are retained as questions, not new shared mappings.

**Active-note reconciliation queued in this same package:** N-T11's literal-only ru shan proposal is not adopted; N-T16's vital-essence label is superseded by P2 only within its approved scope; N-T23's authoritative-transmission label is superseded by transmission; N-T50's pledge proposal by sacred pledge; and the dwangs ma/extract part of N-T65 by P2. N-T65's mdangs/gzi mdangs question remains separate. Subsequent whole-work usage integration will append current dispositions without editing original approval history. No new shared label is activated by these notes. Source-ordered review continues at ordinal 201, DTG-000198.



<a id="phase-d-resumption-02"></a>
### Resumption 02 — recovery and input verification

Active continuation identity: **DTG-PD-20261005-Astra-02**, GPT-6 Astra Pro; original Phase D reviewer/session: **DTG-PD-20261005-Astra-01**. Both are distinct from the authoring/source-reconciliation runs. The earlier 200-pair review and self-check statements are retained as that session's records, not redescribed as a fresh semantic review by this continuation.

At resumption the review branch was at `673ee0e57a93057934c9caf88fcc012794f4f71a` with four unfinished modified files. They were preserved before synchronization on `recovery/phase-d-interrupted-20261005-0728`, commit **`ced6486c83555d236e7e41ac1e854044f79ab738`**, pushed and independently matched to the remote branch ref. The review branch was then fast-forwarded to that preservation commit. No other branch/worktree, stash or tag was rewritten. Remote main remains the frozen input `fc3a443ba5987efb0b132990bf131a236fa57320`.

Resumed English input: `ced6486c83555d236e7e41ac1e854044f79ab738`; `paired/translation.md` SHA-256 `f2f2295a543a85e1e62ae438c684c531e9d82990c1fd85282507a71876e3c18b`. The full active standard and glossary were read again; AGENTS, status, handoff, decisions, local format and source provenance were reread. Recomputed source, golden JSON, policy, format/lineage hashes match the freeze table. CSV parsing confirms 283 data rows and eight columns. Exact replay of the existing 42 recorded pair operations reproduces all 2,667 current English pair payloads, with 38 changed pairs. This is a reproducibility check, not a second semantic certification. Read-only `paired/validate.py` again fails at the same pre-existing protected-glossary contract before any new English repair.

<a id="phase-d-batch-03"></a>
### Batch 03 — source ordinals 201–300

**Read coverage:** all 100 pairs DTG-000198–DTG-000297, in actual source order, with continued clauses and the 17 newly encountered legacy/reconciliation notes. Related N-026 and the five queued legacy terminology notes were reread. Current source-correction notes at U00534, U00542, U00578, U00594 and U00596 were checked before considering old criticisms. **Evidence was saved before application. All 20 scoped English operations in 19 pairs and 11 source-linked review-note insertions are now applied and self-checked.**

Repeated finding families retain their previous rationale and severity/confidence: PD-T01 literary tantra, T02 cyclic existence, T06 mandala, T09 key point, T10 matter and T16 transmission. T10 here includes the attested shortened བེམ in its explicit contrast with རིག་བཅས; this is a locally supported short form, not a new shared row.

| Finding | Evidence / minimal repair | Severity | Confidence |
|---|---|---|---|
| PD-S03 | DTG-000200 has gnad in both lines. Keep both occurrences visible while applying key point; preserve the existing passive and the following realization condition. | Medium | High |
| PD-S04 | DTG-000220 marks mkhas pa with -s, not a beneficiary marker. Represent the skilled as the agent of completing the rite, consistent with the clear mkhas pas agent at DTG-000293; add no named person. | Medium | High for the case relationship; ordinary agent/instrument nuance does not name a new referent |
| PD-S05 | DTG-000267 explicitly has drug 'das, as does the parallel distance construction at DTG-000263. Restore beyond rather than assert exactly six worlds away; retain below and do not infer an unexpressed seventh world. | Medium | High |
| PD-E02 | DTG-000296 mixes an imperative with one's/oneself. Use your/yourself for the same generic addressee; preserve both reflexive/possessive occurrences and the instruction. | Low | High |
| PD-T18 | MTshan nyid receives characteristic(s); DTG-000235/000293 do not themselves supply a definition justifying the extra defining. DTG-000198 does give the no-return/exhaustion criterion and is retained. | Low | Moderate-high; scope is these constructions, not a blanket deletion |
| PD-T19 | Standalone zhing khams in the eightfold list and thirteen-realm introduction receives realms, not buddha-fields. No materially active field metaphor or separately written qualification appears in these two expressions. | Medium | High for the default; descriptive realm-name interpretations remain provisional |
| PD-T20 | DTG-000271's by-rgyan construction receives the transparent adorn-family verb. This does not force the same technical identity on the distinct ordinary spras decorations nearby. | Low | High |
| PD-N02 | Link exact unresolved constructions and the matter/knowing qualification to this report in the commentary layer, without inserting an interpretation into root prose. | Documentation | High for link scope, no claim of resolved syntax |

<!-- phase-d-batch-03 -->
```json
[
  {
    "pair": "DTG-000198",
    "golden": [
      "U00380",
      "U00381",
      "U00382"
    ],
    "tibetan": "ཁམས་གསུམ་འཁོར་བའི་རྒྱུན་བཅད་ནས། །\nཕྱི་ཕྱིར་ལྡོག་པ་མེད་པ་ཡིས། །\nཟད་པའི་མཚན་ཉིད་ཤེས་པའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "finding": "PD-T02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000199",
    "golden": [
      "U00383",
      "U00384"
    ],
    "tibetan": "དམིགས་པས་ཡུལ་གྱི་བློ་རྣམས་ལ། །\nརྒྱུད་ཀྱི་གཞུང་རྣམས་རྣམ་ཕྱེ་སྟེ། །",
    "before": "texts of the continua",
    "after": "texts of the tantras",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000200",
    "golden": [
      "U00385",
      "U00386"
    ],
    "tibetan": "གང་ལ་གང་མོས་ངེས་པའི་གནད། །\nརེ་རེ་དག་ལ་གནད་བཙུགས་ནས། །",
    "before": "The definitive crucial point corresponding to each inclination\nis applied to each one individually.",
    "after": "The definitive key point corresponding to each inclination\nis applied as a key point to each one individually.",
    "finding": "PD-T09/PD-S03",
    "kind": "translation"
  },
  {
    "pair": "DTG-000201",
    "golden": [
      "U00387",
      "U00388"
    ],
    "tibetan": "འབྲལ་བ་མེད་པར་ཡོངས་རྟོགས་ན། །\nའཁོར་བ་དག་ལ་གནས་པ་མིན། །",
    "before": "samsara",
    "after": "cyclic existence",
    "finding": "PD-T02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000203",
    "golden": [
      "U00392",
      "U00393"
    ],
    "tibetan": "དགོངས་པའི་གནད་དོན་མན་ངག་ནི། །\nསོ་སོའི་སྐབས་དང་ཤེས་པར་བྱའོ། །",
    "before": "crucial points",
    "after": "key points",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000205",
    "golden": [
      "U00395",
      "U00396",
      "U00397",
      "U00398"
    ],
    "tibetan": "རྒྱུད་ཀྱི་རྒྱལ་པོ་འདི་ཉིད་ཀྱིས།།\nངེས་པའི་མཚན་གྱི་རྣམ་གྲངས་ལ། །\nབསྟན་ནས་རྫོགས་དོན་མན་ངག་ནི། །\nཚིག་ཙམ་ངེས་པར་བརྟགས་ཕྱེ་སྟེ། །",
    "before": "king of continua",
    "after": "king of tantras",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000206",
    "golden": [
      "U00399",
      "U00400",
      "U00401",
      "U00402"
    ],
    "tibetan": "འབྲུ་རྣམས་དོན་དང་མཐུན་པར་ཡང༌། །\nདོན་གྱི་ངོ་ལ་འདི་ལྟར་སྐྱེལ། །\nསྒྲ་ཡི་བརྗོད་པ་འདི་ལྟ་བུ། །\nརྒྱུད་རྣམས་གཞན་དུ་མ་བཤད་པས། །",
    "before": "other continua",
    "after": "other tantras",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000220",
    "golden": [
      "U00439"
    ],
    "tibetan": "མཁས་པས་ཆོ་ག་རྫོགས་པའོ། །",
    "before": "For the skilled, the rite is complete.",
    "after": "The rite is completed by the skilled.",
    "finding": "PD-S04",
    "kind": "translation"
  },
  {
    "pair": "DTG-000225",
    "golden": [
      "U00455",
      "U00456",
      "U00457",
      "U00458",
      "U00459",
      "U00460",
      "U00461"
    ],
    "tibetan": "འདས་དང་མ་འོངས་ད་ལྟར་གྱི། །\nསྟོན་པ་སངས་རྒྱས་བཅོམ་ལྡན་འདས། །\nདབྱངས་གཅིག་གིས་ནི་དཀྱིལ་འཁོར་དུ། །\nསྐལ་བ་ཅན་གྱི་སྣང་བ་ལ། །\nདབང་པོ་དྲུག་གི་རྣམ་དག་པས། །\nབཅུ་བཅུ་ཡི་ནི་སྐུ་གསུམ་ལས། །\nཁྱད་པར་སྤྲུལ་པའི་སྐུ་ལས་འཕྲོས། །",
    "before": "maṇḍala",
    "after": "mandala",
    "finding": "PD-T06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000234",
    "golden": [
      "U00481",
      "U00482",
      "U00483",
      "U00484"
    ],
    "tibetan": "འབྱུང་བ་ལྔ་ལ་སྤྱོད་ནུས་དང༌། །\nམཚོན་དང་དུག་ལས་རྒྱལ་བ་དང༌། །\nབེམ་དང་རིག་བཅས་སྒྲ་རྣམས་དང༌། །\nབརྡའ་དང་ཐ་སྙད་ལ་མཁས་འགྱུར། །",
    "before": "the sounds of the insentient and the aware",
    "after": "the sounds of matter and the aware",
    "finding": "PD-T10",
    "kind": "translation"
  },
  {
    "pair": "DTG-000235",
    "golden": [
      "U00485",
      "U00486"
    ],
    "tibetan": "མདོར་ན་དགོས་པའི་བསྟན་བཅོས་དང༌། །\nབཀའ་ཡི་མཚན་ཉིད་ཤེས་པར་འགྱུར། །",
    "before": "defining characteristics",
    "after": "characteristics",
    "finding": "PD-T18",
    "kind": "translation"
  },
  {
    "pair": "DTG-000240",
    "golden": [
      "U00493",
      "U00494",
      "U00495",
      "U00496",
      "U00497"
    ],
    "tibetan": "ཐལ་བའི་གནས་ནི་རྣམ་པ་བརྒྱད། །\nའཇིག་རྟེན་ཁམས་དང་ཞིང་ཁམས་དང་། །\nདམ་བཅའ་སྐྱོན་དང་སྐྱོན་གནས་དང་། །\nའཕེན་པའི་ལས་དང་སྦྱོར་བ་དང་། །\nགྲགས་དང་སོང་བའི་གནད་དང་བརྒྱད། །",
    "before": "buddha-fields",
    "after": "realms",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000240",
    "golden": [
      "U00493",
      "U00494",
      "U00495",
      "U00496",
      "U00497"
    ],
    "tibetan": "ཐལ་བའི་གནས་ནི་རྣམ་པ་བརྒྱད། །\nའཇིག་རྟེན་ཁམས་དང་ཞིང་ཁམས་དང་། །\nདམ་བཅའ་སྐྱོན་དང་སྐྱོན་གནས་དང་། །\nའཕེན་པའི་ལས་དང་སྦྱོར་བ་དང་། །\nགྲགས་དང་སོང་བའི་གནད་དང་བརྒྱད། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000243",
    "golden": [
      "U00503",
      "U00504",
      "U00505",
      "U00506"
    ],
    "tibetan": "ཞིང་ཁམས་རྣམ་པ་བཅུ་གསུམ་ལ། །\nའདི་ནས་འཇིག་རྟེན་འོག་ན་ནི། །\nཐལ་བའི་དབྱངས་ཞེས་བྱ་བའི་ཡུལ། །\nརྒྱ་ཁྱོན་དཔག་དཀའ་རབ་ཏུ་མཛེས། །",
    "before": "buddha-fields",
    "after": "realms",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000267",
    "golden": [
      "U00560",
      "U00561"
    ],
    "tibetan": "འདི་ནས་འཇིག་རྟེན་ལྷོ་ནུབ་གཡས། །\nདྲུག་འདས་འོག་ན་ཐལ་བའི་རླུང་། །",
    "before": "six worlds away and below",
    "after": "beyond six worlds and below",
    "finding": "PD-S05",
    "kind": "translation"
  },
  {
    "pair": "DTG-000271",
    "golden": [
      "U00567",
      "U00568",
      "U00569",
      "U00570",
      "U00571"
    ],
    "tibetan": "དེ་སྟེང་བཅུ་གསུམ་བརྩེགས་པ་ན། །\nརིན་ཆེན་ཐལ་བ་ཞེས་བྱ་ན། །\nབཀྲ་ཤིས་ཉི་མ་རྣམས་ཀྱིས་སྤྲས། །\nའདོད་པའི་ཡོན་ཏན་རྣམས་ཀྱིས་བརྒྱན། །\nའཕྲུལ་གྱི་རི་མོ་ཡི་གེ་མཛེས། །",
    "before": "ornamented with",
    "after": "adorned with",
    "finding": "PD-T20",
    "kind": "translation"
  },
  {
    "pair": "DTG-000281",
    "golden": [
      "U00595"
    ],
    "tibetan": "སྟོན་པའི་བསྟན་པ་ལུང་གིས་བསྐོར། །",
    "before": "authoritative transmissions",
    "after": "transmissions",
    "finding": "PD-T16",
    "kind": "translation"
  },
  {
    "pair": "DTG-000285",
    "golden": [
      "U00601",
      "U00602",
      "U00603"
    ],
    "tibetan": "རང་འདོད་ངེས་པར་སྐྱོལ་བ་ནི། །\nལུང་དང་རིགས་པ་མན་ངག་གིས། །\nསྐྱོན་བསལ་བསྒྲུབ་དང་འགལ་བ་སྤང་། །",
    "before": "authoritative transmission",
    "after": "transmission",
    "finding": "PD-T16",
    "kind": "translation"
  },
  {
    "pair": "DTG-000293",
    "golden": [
      "U00612"
    ],
    "tibetan": "མཁས་པས་མཚན་ཉིད་རྫོགས་ཀྱིས་སྦྱར། །",
    "before": "defining characteristics",
    "after": "characteristics",
    "finding": "PD-T18",
    "kind": "translation"
  },
  {
    "pair": "DTG-000296",
    "golden": [
      "U00615"
    ],
    "tibetan": "རང་སྐྱོན་རང་གིས་ཤེས་བྱས་ལ། །",
    "before": "Know one's own faults oneself.",
    "after": "Know your own faults yourself.",
    "finding": "PD-E02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000199",
    "golden": [
      "U00383",
      "U00384"
    ],
    "tibetan": "དམིགས་པས་ཡུལ་གྱི་བློ་རྣམས་ལ། །\nརྒྱུད་ཀྱི་གཞུང་རྣམས་རྣམ་ཕྱེ་སྟེ། །",
    "before": "For conceptual minds that focus on objects,\nthe texts of the tantras are distinguished.\n\nEarlier notes: [N-026](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-026).",
    "after": "For conceptual minds that focus on objects,\nthe texts of the tantras are distinguished.\n\nEarlier notes: [N-026](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-026).\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-01).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000227",
    "golden": [
      "U00464",
      "U00465"
    ],
    "tibetan": "གནས་དང་འབྱེད་དང་གནས་བཅུད་ཡུལ། །\nཐོབ་ཅིང་མཐོང་རྟོགས་ངེས་འཇུག་པའོ། །",
    "before": "The sites, distinctions, and domains of their vital cores [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029)\nare attained, and one assuredly enters seeing and realization.\n\nEarlier notes: [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029).",
    "after": "The sites, distinctions, and domains of their vital cores [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029)\nare attained, and one assuredly enters seeing and realization.\n\nEarlier notes: [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029).\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-02).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000238",
    "golden": [
      "U00491"
    ],
    "tibetan": "རྒྱུད་ལ་ངེས་པའི་འཕྲུལ་འབྱེད་ཕྱེ། །",
    "before": "The distinguishing magic definitive for the continuum is set apart.",
    "after": "The distinguishing magic definitive for the continuum is set apart.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-03).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000248",
    "golden": [
      "U00519",
      "U00520",
      "U00521"
    ],
    "tibetan": "འོད་དང་ཁ་དོག་ངེས་གསལ་ཞིང་། །\nསྟོན་པའི་བསྟན་པ་འདུལ་བའི་ཞིང་། །\nསོ་སོའི་ལས་དང་མཚན་བཅས་པའོ། །",
    "before": "Its light and colors are definitely clear;\nit is a field where the teacher's teaching trains beings,\neach with their own karma and characteristics.",
    "after": "Its light and colors are definitely clear;\nit is a field where the teacher's teaching trains beings,\neach with their own karma and characteristics.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-04).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000252",
    "golden": [
      "U00529",
      "U00530"
    ],
    "tibetan": "སྟོན་པའི་བསྟན་པ་འདུ་མཆེད་རྒྱས། །\nབསྐལ་པ་རྫོགས་པས་ཐལ་ཞེས་བྱའོ། །",
    "before": "The sources of the teacher's teaching expand;\nwith the age complete, it is called Penetration.",
    "after": "The sources of the teacher's teaching expand;\nwith the age complete, it is called Penetration.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-05).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000258",
    "golden": [
      "U00543"
    ],
    "tibetan": "སྒྲ་དབྱངས་སྣ་ཚོགས་འབྱུང་བའི་གཞི། །",
    "before": "It is the Ground from which diverse sounds and melodies arise.",
    "after": "It is the Ground from which diverse sounds and melodies arise.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-06).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000244",
    "golden": [
      "U00507",
      "U00508",
      "U00509",
      "U00510"
    ],
    "tibetan": "རྒྱུ་དང་རྐྱེན་དང་རང་བཞིན་དང༌། །\nསྟོན་པའི་བསྟན་པ་དེ་ཡི་འཁོར། །\nསྟེང་དང་འོག་དང་ཕྱོགས་མཚམས་སུ། །\nཆུ་ཞེང་ཉམས་དགའ་བཀོད་ལེགས་སྤྲས། །",
    "before": "Its causes, conditions, and intrinsic nature,\nthe teacher's teaching and its retinue,\nabove, below, and in the directions and intermediate directions—\nits length and breadth are pleasing, well-arrayed and adorned.\n\nEarlier notes: [N-032](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-032).",
    "after": "Its causes, conditions, and intrinsic nature,\nthe teacher's teaching and its retinue,\nabove, below, and in the directions and intermediate directions—\nits length and breadth are pleasing, well-arrayed and adorned.\n\nEarlier notes: [N-032](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-032).\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-07).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000276",
    "golden": [
      "U00587",
      "U00588"
    ],
    "tibetan": "སྟོན་པ་ཉིད་དང་བསྟན་པ་དང་། །\nདེ་ཡི་འཁོར་དང་ལོངས་སྤྱོད་རྫོགས། །",
    "before": "The teacher and the teaching,\nits retinue and enjoyments, are complete.",
    "after": "The teacher and the teaching,\nits retinue and enjoyments, are complete.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-07).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000207",
    "golden": [
      "U00403"
    ],
    "tibetan": "ཨེ་མ་ངོ་མཚར་ཆེ་བ་ཉིད། །",
    "before": "Ema! How greatly wonderful!",
    "after": "Ema! How greatly wonderful!\n\nReview note: [Short exclamation remains provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-batch-03-dispositions).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000111",
    "golden": [
      "U00228"
    ],
    "tibetan": "རིག་བཅས་བེམ་པོའི་བྱེ་བྲག་གང༌། །",
    "before": "What distinguishes the aware from matter?",
    "after": "What distinguishes the aware from matter?\n\nReview note: [Matter and awareness](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-matter-note).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000234",
    "golden": [
      "U00481",
      "U00482",
      "U00483",
      "U00484"
    ],
    "tibetan": "འབྱུང་བ་ལྔ་ལ་སྤྱོད་ནུས་དང༌། །\nམཚོན་དང་དུག་ལས་རྒྱལ་བ་དང༌། །\nབེམ་དང་རིག་བཅས་སྒྲ་རྣམས་དང༌། །\nབརྡའ་དང་ཐ་སྙད་ལ་མཁས་འགྱུར། །",
    "before": "One can act upon the five elements,\nprevails over weapons and poison,\nand becomes skilled in the sounds of matter and the aware,\nin signs and conventions.\n\nEarlier notes: [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).",
    "after": "One can act upon the five elements,\nprevails over weapons and poison,\nand becomes skilled in the sounds of matter and the aware,\nin signs and conventions.\n\nEarlier notes: [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).\n\nReview note: [Matter and awareness](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-matter-note).",
    "finding": "PD-N02",
    "kind": "review-link"
  }
]
```
<!-- /phase-d-batch-03 -->

<a id="phase-d-batch-03-dispositions"></a>
**Important no-change cases:** DTG-000214's personal continuum is not a tantra title. DTG-000221/000237 preserve the established word-and-meaning compound despite neighboring acoustic sound passages; the five acoustic occasions and water sounds support sound in their own constructions. DTG-000202's accomplishment is bsgrub, not dngos grub. DTG-000216's rnam shes is a finite knowing construction, not mechanically the consciousness noun. DTG-000230's body of Vajradhara preserves lus, not an invented embodiment; its proper name is the approved rdo rje 'chang. DTG-000261 already retains object of focus and intrinsic nature. The complete sources do not authorize turning all ordinary moving/decorating verbs into technical glossary nouns. The numerical schemes and logical imagery remain literal and ordered: no four reasons are changed to three; DTG-000292 and DTG-000297 deliberately preserve their different source orders for assertion/proof/reason. The already separated pleasant-region and naga-face variant notes are not current source-layer defects. No empty graphic or missing passage is fabricated.

**Retained linked questions:** N-027's All-Pervader numbers/side-locks/grouping; N-028's hero/hero-goer, neutral member and counts; N-029's six/tens/three and compact final list; N-030's technical-science/archery/thal-yig treatment; N-031's eightfold parsing; N-032's thirteen ordered names, relative directions and opaque counts; N-034's lda-ldi, mer mer po and awnings; and N-036's proof/fortress/wheel relation remain open. The thirteen introduced names were read in order from Melody of Penetration through Star Penetration; descriptive English names, including Sound of Penetration, are not newly approved proper-name defaults. N-T19 higher knowing and N-T21 logical consequence remain shared-label proposals; the logical construction at DTG-000291 is locally supported by assertions, reasons and debate, not a global replacement of penetration. Exact short ཨེ་མ at DTG-000207 continues the existing short-exclamation question (DTG-000069/000155/000195); it is not silently expanded to ཨེ་མ་ཧོ or assigned that whole-expression default.

<a id="phase-d-matter-note"></a>
**Matter and awareness:** At DTG-000111 and DTG-000234 the approved matter label denotes the material/non-knowing side of the stated contrast with the aware. It does not mean immobile/dead, does not assert that karmic beings lack material bodies, and does not replace every body, entity or being expression. Elemental sounds in the surrounding account make the sound-of-matter construction intelligible without adding insentient to the technical label.

<a id="pd-q03-01"></a>
#### PD-Q03-01 — The dmigs pas / yul gyi blo audience construction

Retain the linked N-026 working construction rather than force object of focus into an unparsed clause. The instrumental/relational function of དམིགས་པས and its connection to ཡུལ་གྱི་བློ require resolution. Nominal object-of-focus versus a finite focusing construction remains open; the clear literary tantra repair does not settle it. A constructional parallel or an explicit explanation of the two contrasted audiences would settle the attachment.

**DTG-000199 / U00383 U00384**

Tibetan: `དམིགས་པས་ཡུལ་གྱི་བློ་རྣམས་ལ། །` / `རྒྱུད་ཀྱི་གཞུང་རྣམས་རྣམ་ཕྱེ་སྟེ། །`

English before this batch (provisional):

> For conceptual minds that focus on objects,
> the texts of the continua are distinguished.

<a id="pd-q03-02"></a>
#### PD-Q03-02 — gnas bcud yul and the scope of bcud

N-029's vital cores is not a newly approved label. Quintessence is approved only in its recorded scope; contents/inhabitants is a different authorized construction. The compact གནས་བཅུད་ཡུལ does not yet establish which relation/sense applies. Retain the existing linked provisional list, not a reconstruction from components. A referent-identifying explanation of the sites, distinctions and domains would settle this.

**DTG-000227 / U00464 U00465**

Tibetan: `གནས་དང་འབྱེད་དང་གནས་བཅུད་ཡུལ། །` / `ཐོབ་ཅིང་མཐོང་རྟོགས་ངེས་འཇུག་པའོ། །`

English before this batch (provisional):

> The sites, distinctions, and domains of their vital cores [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029)
> are attained, and one assuredly enters seeing and realization.

<a id="pd-q03-03"></a>
#### PD-Q03-03 — rgyud in the concluding magic clause

Retain continuum provisionally. Unlike the explicit texts/titles at DTG-000199/000205/000206, this clause can concern either an individual's continuum or this tantra's distinctive efficacy. Proximity to a title is insufficient under P1. An unambiguous referent or internal parallel would settle it.

**DTG-000238 / U00491**

Tibetan: `རྒྱུད་ལ་ངེས་པའི་འཕྲུལ་འབྱེད་ཕྱེ། །`

English before this batch (provisional):

> The distinguishing magic definitive for the continuum is set apart.

<a id="pd-q03-04"></a>
#### PD-Q03-04 — Training field, implied beings and possession

The working English makes the teaching train beings and assigns individual karma/characteristics to them. The source instead compactly juxtaposes the teacher's teaching, a training field, and individual las/mtshan. Beings are not overtly named. A nominal training-field description and attachment of las/mtshan to the field/teaching are alternatives. Retain only as a visibly linked provisional construction; do not silently invent a new agent or substitute discipline as a textual-category label. An explicit constructional parallel for the repeated realm descriptions would settle the subject and modifiers.

**DTG-000248 / U00519 U00520 U00521**

Tibetan: `འོད་དང་ཁ་དོག་ངེས་གསལ་ཞིང་། །` / `སྟོན་པའི་བསྟན་པ་འདུལ་བའི་ཞིང་། །` / `སོ་སོའི་ལས་དང་མཚན་བཅས་པའོ། །`

English before this batch (provisional):

> Its light and colors are definitely clear;
> it is a field where the teacher's teaching trains beings,
> each with their own karma and characteristics.

<a id="pd-q03-05"></a>
#### PD-Q03-05 — The exact expanded form du mched

The English sources treats འདུ་མཆེད as a nominal source-expression. Gathering/proliferation or another complete construction is not excluded by the present clause. No spelling change to another headword, component-built glossary equivalent, or independently approved source-family default is justified. A lexical/constructional parallel or later explicit explanation would settle this; retain the working treatment as provisional.

**DTG-000252 / U00529 U00530**

Tibetan: `སྟོན་པའི་བསྟན་པ་འདུ་མཆེད་རྒྱས། །` / `བསྐལ་པ་རྫོགས་པས་ཐལ་ཞེས་བྱའོ། །`

English before this batch (provisional):

> The sources of the teacher's teaching expand;
> with the age complete, it is called Penetration.

<a id="pd-q03-06"></a>
#### PD-Q03-06 — Technical Ground versus a support/origin

The described realm is the གཞི from which sounds and melodies arise. P1 approves capitalization only for an identified technical Ground; it does not decide this support/origin construction. Retain the current capitalized wording provisionally, not as proof of that identification. An explicit identification with the technical Ground or a clear ordinary-support parallel would settle the case.

**DTG-000258 / U00543**

Tibetan: `སྒྲ་དབྱངས་སྣ་ཚོགས་འབྱུང་བའི་གཞི། །`

English before this batch (provisional):

> It is the Ground from which diverse sounds and melodies arise.

<a id="pd-q03-07"></a>
#### PD-Q03-07 — The possessor in de yi khor

The repeated དེ་ཡི་འཁོར follows teacher/teaching descriptions. Its can refer to the realm or teaching in English, while his/the teacher's is another possible construal. Tibetan de yi alone does not resolve the antecedent. Do not silently impose a personal possessor merely because it is more conventional. Retain with N-032 and this question until a clear antecedent or parallel settles it.

**DTG-000244 / U00507 U00508 U00509 U00510**

Tibetan: `རྒྱུ་དང་རྐྱེན་དང་རང་བཞིན་དང༌། །` / `སྟོན་པའི་བསྟན་པ་དེ་ཡི་འཁོར། །` / `སྟེང་དང་འོག་དང་ཕྱོགས་མཚམས་སུ། །` / `ཆུ་ཞེང་ཉམས་དགའ་བཀོད་ལེགས་སྤྲས། །`

English before this batch (provisional):

> Its causes, conditions, and intrinsic nature,
> the teacher's teaching and its retinue,
> above, below, and in the directions and intermediate directions—
> its length and breadth are pleasing, well-arrayed and adorned.

**DTG-000276 / U00587 U00588**

Tibetan: `སྟོན་པ་ཉིད་དང་བསྟན་པ་དང་། །` / `དེ་ཡི་འཁོར་དང་ལོངས་སྤྱོད་རྫོགས། །`

English before this batch (provisional):

> The teacher and the teaching,
> its retinue and enjoyments, are complete.

<a id="phase-d-notes-02"></a>
**Queued note-status reconciliation:** append, without rewriting historical proposals, the current dispositions for N-T11 (retain secret preliminary and the separate phyed predicate at DTG-000127; later reply still to be checked), N-T16 (P2 quintessence in the nourishment context, whole bcud kyis len pa construction still provisional), N-T23 (P2 transmission without unsupported authoritative), N-T50 (P2 sacred pledge, distinct from sdom pa), and N-T65 (P2 pure extract/residue in the reviewed elemental contrast, without settling mdangs/gzi mdangs). These are policy applications in recorded occurrences, not local new shared assignments. The five current dispositions are now appended in LEGACY-NOTES.md and USAGES.json; the historical source notes/proposals remain unchanged.


<a id="phase-d-batch-04"></a>
### Batch 04 — source ordinals 301–450; bounded return to DTG-000188

**Read coverage:** all 150 pairs DTG-000298–DTG-000447, in source order, with the full current source/English, continued sentences, and all 21 newly encountered notes. N-T20 and N-T22 were also read in full. DTG-000187–000189 were reread on returning to the earlier training-basis question. **Evidence checkpoint: the following 20 English operations in 20 pairs and six review-link insertions are recorded before application; application and self-check are pending.**

Repeated terminology families retain their established batch rationale: T01 literary tantra (the text is explicitly read), T02 cyclic existence, T04 full spiritual accomplishment in a transparent descriptive name, T09 key point, T12 sacred pledge (distinct from vows), T18 characteristic without an unprovided definition, and T19 realm. Proper-name repairs preserve the descriptive construction and all modifiers; they do not assert a historical identification or a new canonical whole-name entry. E02 continues the narrowly grammatical imperative-addressee repair without changing the source's position or its possessor.

| Finding | Evidence and scope | Severity | Confidence |
|---|---|---|---|
| PD-S06 | The bodily/training basis at DTG-000322/000351 is explicitly the changing elemental body/five aggregates; DTG-000352 refers back to that basis. DTG-000354 explains the introductory setting's five aspects, not a new assertion that the technical Ground has five constituents. Use ordinary basis, retaining the source wordplay in a linked note. Apply the supported training-basis reading retrospectively to DTG-000188; its broader arising-as-trainer relationship remains provisional. | Medium, sense/attachment control | Moderate-high for these basis referents; not certification of the whole earlier clause |
| PD-T21 | Restore the meaningful ordinary component in the cognitive sems phrases at DTG-000398 and DTG-000426. Neither is the established wind-mind compound or the approved karmic-being entry. Keep the explicit loving/virtuous modifiers. | Medium, lexical component | High |
| PD-T22 | P2 now assigns nominal dngos po to entity, not the older contextual proposal actual presence. DTG-000441 explicitly counts three and does not separately say actual. Apply entities while retaining embodiment, speech, awakened mind, the recipient and effortless result. The precise represented referents remain N-048's question. | Medium, adopted terminology | High for the scoped label; ritual referents remain provisional |
| PD-N03 | Link the precise tenets/construction question and ordinary-basis interpretation in the commentary layer. No source role, metadata or root segmentation changes. | Documentation | High for location/link scope |

<!-- phase-d-batch-04 -->
```json
[
  {
    "pair": "DTG-000299",
    "golden": [
      "U00621",
      "U00622",
      "U00623"
    ],
    "tibetan": "སྒྲ་དོན་བརྗོད་བྱའི་ཚིག་ཙམ་ལས། །\nའབྲེལ་དང་འབྲེལ་མེད་མཚན་ཉིད་ཀྱིས། །\nཁྱབ་བྱའི་དོན་རྣམས་ཐལ་འགྱུར་བརྩིའོ། །",
    "before": "defining characteristics",
    "after": "characteristics",
    "finding": "PD-T18",
    "kind": "translation"
  },
  {
    "pair": "DTG-000307",
    "golden": [
      "U00633"
    ],
    "tibetan": "སྦྱོར་བའི་དམིགས་ཀྱིས་རང་འདོད་བསྐྱང༌། །",
    "before": "maintain one's own position",
    "after": "maintain your own position",
    "finding": "PD-E02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000322",
    "golden": [
      "U00664",
      "U00665"
    ],
    "tibetan": "རླུང་ས་མེ་ཆུ་ཆ་ལྔ་ལས། །\nའགྱུར་ཞིང་བྱེད་པ་ལུས་ཀྱི་གཞི། །",
    "before": "body's Ground",
    "after": "body's basis",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000329",
    "golden": [
      "U00681",
      "U00682",
      "U00683"
    ],
    "tibetan": "གླེང་གཞིར་བཅས་པས་གཞི་བཟུང་སྟེ། །\nགནད་འདུས་བཀོད་པ་སེམས་ཀྱི་རྟེན། །\nརང་ཐོག་འབེབས་པ་གཉིས་པ་ཡིན། །",
    "before": "Crucial Points",
    "after": "Key Points",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000333",
    "golden": [
      "U00689",
      "U00690"
    ],
    "tibetan": "ལྔ་པ་བལྟ་བསྒོམ་བཀོད་པ་སྟེ། །\nབྱ་བྲལ་རྫོགས་པ་དབྱིངས་ཀྱི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000337",
    "golden": [
      "U00696",
      "U00697",
      "U00698",
      "U00699",
      "U00700"
    ],
    "tibetan": "དཔལ་གྱི་དགོངས་པ་འབྱུང་བའི་གཏེར། །\nབདེ་བ་ཐབས་ཀྱི་སྐུ་ཉིད་ཀྱང༌། །\nལུང་བསྟན་རྗེས་འཛིན་སེམས་ཀྱི་གནད། །\nའགྲོ་བ་བདག་སྐྱོབ་རླུང་གི་ལྷ། །\nལྷག་མ་ཉིད་ཀྱང་དེ་ཙམ་མོ། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000348",
    "golden": [
      "U00719"
    ],
    "tibetan": "དབང་དང་དམ་ཚིག་སྡོམ་པ་རྫོགས། །",
    "before": "pledges",
    "after": "sacred pledges",
    "finding": "PD-T12",
    "kind": "translation"
  },
  {
    "pair": "DTG-000188",
    "golden": [
      "U00361",
      "U00362"
    ],
    "tibetan": "འདུལ་གཞི་ལས་ནི་འདུལ་བྱེད་དུ། །\nབྱུང་བས་བསྟན་པ་གནས་པར་བྱེད། །",
    "before": "Ground of training",
    "after": "basis of training",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000351",
    "golden": [
      "U00722",
      "U00723",
      "U00724"
    ],
    "tibetan": "གླེང་གཞི་དག་ལ་ཡང་དག་ཚིག །\nགདུལ་བྱ་གང་ཟག་སོ་སོ་ལ། །\nགདུལ་གཞི་ཕུང་པོ་རྣམ་པ་ལྔ། །",
    "before": "Ground of training",
    "after": "basis of training",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000352",
    "golden": [
      "U00725"
    ],
    "tibetan": "དེ་ཡི་འདུལ་བྱེད་གླེང་གཞི་སྟེ། །",
    "before": "that Ground",
    "after": "that basis",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000354",
    "golden": [
      "U00727"
    ],
    "tibetan": "གཞི་ནི་རྣམ་པ་ལྔ་ཡིན་ཏེ། །",
    "before": "‘Ground’",
    "after": "‘Basis’",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000373",
    "golden": [
      "U00783",
      "U00784",
      "U00785",
      "U00786"
    ],
    "tibetan": "དེ་ཡི་ཡོན་བདག་ཁྱིམ་བདག་རིགས། །\nདགེ་བའི་དངོས་གྲུབ་ཅེས་བྱ་བས། །\nབསྟན་པ་དམ་པ་འདི་ཉིད་ནི། །\nལོ་བརྒྱའི་བར་ལ་གནས་པར་བྱེད། །",
    "before": "Accomplishment of Virtue",
    "after": "Spiritual Accomplishment of Virtue",
    "finding": "PD-T04",
    "kind": "translation"
  },
  {
    "pair": "DTG-000398",
    "golden": [
      "U00838",
      "U00839",
      "U00840",
      "U00841",
      "U00842",
      "U00843"
    ],
    "tibetan": "སྟོང་དང་སུམ་བརྒྱ་འདས་འོག་ཏུ། །\nཡང་ནི་འཛམ་གླིང་བྱང་གི་ངོས། །\nགཟི་བརྗིད་ལྡན་པའི་རི་ཡི་རྩེར། །\nདགེ་སློང་གཟུགས་ལ་བྱམས་སེམས་བྲལ། །\nགཡས་པ་ལ་ནི་རྣ་བ་གཉིས། །\nམིག་ནི་ཟུར་གསུམ་མས་ཡར་འགེབ། །",
    "before": "loving mind",
    "after": "loving ordinary mind",
    "finding": "PD-T21",
    "kind": "translation"
  },
  {
    "pair": "DTG-000421",
    "golden": [
      "U00906",
      "U00907"
    ],
    "tibetan": "དེ་ནས་མཛེས་ལྡན་བཀོད་པ་ཡི། །\nཞིང་ཁམས་དག་ཏུ་ངེས་འཕར་ནས། །",
    "before": "field of Beautiful Array",
    "after": "realm of Beautiful Array",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000426",
    "golden": [
      "U00919",
      "U00920",
      "U00921"
    ],
    "tibetan": "ཐམས་ཅད་བྱང་ཆུབ་སེམས་ཆེན་པོ། །\nམི་སྐྱེའི་ཆོས་ལ་བཟོད་ཐོབ་སྟེ། །\nདགེ་བའི་སེམས་ལྡན་འབའ་ཞིག་འབྱུང་། །",
    "before": "virtuous minds",
    "after": "virtuous ordinary minds",
    "finding": "PD-T21",
    "kind": "translation"
  },
  {
    "pair": "DTG-000430",
    "golden": [
      "U00929",
      "U00930",
      "U00931"
    ],
    "tibetan": "དེ་འོག་གཙུག་ཕུད་དབྱངས་ལྡན་པའི། །\nའཇིག་རྟེན་ཁམས་ནི་ཡངས་པར་ནི། །\nསྟོན་པ་མཐའ་ཡས་འཁོར་བ་འཇིག །",
    "before": "Samsara",
    "after": "Cyclic Existence",
    "finding": "PD-T02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000441",
    "golden": [
      "U00955",
      "U00956",
      "U00957"
    ],
    "tibetan": "སྐུ་གསུང་ཐུགས་ཀྱི་དངོས་པོ་གསུམ། །\nསུ་ལ་བབ་པ་འབད་མེད་པར། །\nགདོན་མི་ཟ་བའི་སངས་རྒྱས་ཐོབ། །",
    "before": "actual presences",
    "after": "entities",
    "finding": "PD-T22",
    "kind": "translation"
  },
  {
    "pair": "DTG-000442",
    "golden": [
      "U00958",
      "U00959",
      "U00960",
      "U00961"
    ],
    "tibetan": "དེ་ཕྱིར་བྱིན་གྱིས་རླབས་ཀྱི་གནད། །\nགསུང་གི་སྤྲུལ་པ་ཉིད་ལས་ཀྱང༌། །\nསྟོན་པའི་ཁ་དོག་ལེགས་བྲིས་ནས། །\nམཆན་ཁུང་གཡོན་དུ་བཏགས་བྱས་ཏེ། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000444",
    "golden": [
      "U00964",
      "U00965"
    ],
    "tibetan": "རྒྱུད་འདི་སུས་ནི་རྟག་བཀླགས་ན། །\nདེས་ཀྱང་གོང་མ་བཞིན་དུ་འགྱུར། །",
    "before": "this continuum",
    "after": "this tantra",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000445",
    "golden": [
      "U00966",
      "U00967",
      "U00968",
      "U00969",
      "U00970"
    ],
    "tibetan": "བཀའ་གསང་ངེས་པ་བཅུ་བདུན་དང་། །\nབསྟན་པའི་གཟེར་དང་འཕྲུལ་ཡིག་བཅས། །\nསྤྲུལ་སྐུའི་ཞིང་ཁམས་ཐོག་མ་ལ། །\nསྟོན་པ་ཀུན་ཏུ་བཟང་པོ་ཡིས། །\nསྟུག་པོ་བཀོད་པའི་གནས་སུ་གསུངས། །",
    "before": "earliest field",
    "after": "earliest realm",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000313",
    "golden": [
      "U00640",
      "U00641"
    ],
    "tibetan": "གྲུབ་མཐའ་བློ་ལ་བརྟེན་པ་ཡིས། །\nརང་གཞན་ཤེས་པའི་རྩལ་གྱིས་སོ། །",
    "before": "through the expressiveness of knowing in oneself and others.",
    "after": "through the expressiveness of knowing in oneself and others.\n\nReview note: [Tenets and construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q04-01).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000188",
    "golden": [
      "U00361",
      "U00362"
    ],
    "tibetan": "འདུལ་གཞི་ལས་ནི་འདུལ་བྱེད་དུ། །\nབྱུང་བས་བསྟན་པ་གནས་པར་བྱེད། །",
    "before": "Earlier notes: [N-T09](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t09).",
    "after": "Earlier notes: [N-T09](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t09).\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000322",
    "golden": [
      "U00664",
      "U00665"
    ],
    "tibetan": "རླུང་ས་མེ་ཆུ་ཆ་ལྔ་ལས། །\nའགྱུར་ཞིང་བྱེད་པ་ལུས་ཀྱི་གཞི། །",
    "before": "Earlier notes: [N-040](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-040).",
    "after": "Earlier notes: [N-040](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-040).\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000351",
    "golden": [
      "U00722",
      "U00723",
      "U00724"
    ],
    "tibetan": "གླེང་གཞི་དག་ལ་ཡང་དག་ཚིག །\nགདུལ་བྱ་གང་ཟག་སོ་སོ་ལ། །\nགདུལ་གཞི་ཕུང་པོ་རྣམ་པ་ལྔ། །",
    "before": "the basis of training is the five aggregates.",
    "after": "the basis of training is the five aggregates.\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000352",
    "golden": [
      "U00725"
    ],
    "tibetan": "དེ་ཡི་འདུལ་བྱེད་གླེང་གཞི་སྟེ། །",
    "before": "The introductory setting is what trains that basis.",
    "after": "The introductory setting is what trains that basis.\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000354",
    "golden": [
      "U00727"
    ],
    "tibetan": "གཞི་ནི་རྣམ་པ་ལྔ་ཡིན་ཏེ། །",
    "before": "Earlier notes: [N-043](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-043).",
    "after": "Earlier notes: [N-043](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-043).\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  }
]
```
<!-- /phase-d-batch-04 -->

<a id="phase-d-basis-04"></a>
**Basis and wordplay — local construction decision, not a shared glossary replacement.** DTG-000322 says `ལུས་ཀྱི་གཞི`, the body's basis, in the sequence of changing elements. DTG-000351 explicitly identifies `གདུལ་གཞི` with five aggregates; DTG-000352's `དེ་ཡི` refers back to what is trained. This provides the internal comparison lacking at the earlier DTG-000188 `འདུལ་གཞི`. The basis reading is locally supported; the precise relationship of arising as what trains at DTG-000188 is still not independently resolved. It must not be counted as a fully settled clause merely because Ground was corrected.

At DTG-000353–000354 the text explains gleng ba and gzhi separately within the introductory-setting account. Basis renders the latter component in that explanation; introductory setting remains the complete expression gleng gzhi. The subsequent place, teacher, retinue, teaching and time are the five aspects being described. This is interpretive source wordplay, not historical etymology. The Tibetan component labels Phun/Gsum/Tshogs, their differing explanations and every stated numeral remain unchanged. Technical Ground at DTG-000344, in the explicit unchanging Ground/path/result sequence, is retained. The chapter-outline Ground uses at DTG-000328/000329/000334 are less decisive: their support-of-a-chapter versus technical referents remain within N-041 for comparison with the chapter endings; they are not changed by this local basis decision.

<a id="pd-q04-01"></a>
#### PD-Q04-01 — Tenets, system and instrumental continuation

**DTG-000313 / U00640–U00641.** Tibetan: `གྲུབ་མཐའ་བློ་ལ་བརྟེན་པ་ཡིས། །` / `རང་གཞན་ཤེས་པའི་རྩལ་གྱིས་སོ། །`

Current English: “Tenets depend on the conceptual mind, / through the expressiveness of knowing in oneself and others.” This is retained provisionally. The immediately preceding assertions/reasons/examples make constituent tenets possible under the P2 row, but a whole tenet system is also possible. The two instrumental constructions do not unambiguously state the finite dependence clause chosen by the English. Compare the full establishment account and DTG-000891 before deciding between a system depending on conceptual mind and establishment through reliance on conceptual mind/knowing. An explicit internal parallel supplying that relationship would settle it. Do not add philosophical or force the noun into a new shared default while this is open.

<a id="phase-d-batch-04-dispositions"></a>
**Other justified retentions and bounded questions:** The logical chos can occurrences DTG-000304/000308/000309 meet P2's subject exception; the paired chos nyid/property at DTG-000304 remains the explicitly linked N-T20 proposal, not an approved extension of that exception. N-037's wind/argument imagery and N-038's impure-wind/primordial-knowing clause remain provisional, preserving the printed negation. Current G-U00626/G-U00632/G-U00651/G-U00710/G-U00800 already separate the variants; the old nus pa/capacity speculation does not supersede the selected bus pa annotation. The additional heading delimiters at G-U00910/G-U00948 do not warrant English edits.

N-039's dngos grouping and the doing/doer-versus-two-operations relationship in DTG-000315 remain provisional: both source members and every listed contrast survive, but no hidden grammatical table is reconstructed. N-040's exact elemental order, the single water after doubled wind/earth/fire, and lung sdeb remain; lung is not silently emended to rlung or certified as the teaching/transmission sense merely from spelling. The clear support construction at DTG-000322 is resolved without pretending to solve that numerical matrix.

At DTG-000332, N-T22's nature of ordinary mind is retained provisionally because this clause identifies the object of the fourth chapter's transmission in a parallel account of the nature of phenomena and completed qualities. That supports a lexicalized nature-reading but does not exclude the owner's preferred intensive ordinary mind itself. The full scope must be compared with DTG-001115; neither book preference nor repeated usage settles it. Ordinary mind remains visible in either alternative. The source's six chapter arrays and compressed remainder (N-041) retain their order and terms; the chapter-title gnad repairs do not add or rename a chapter. Nye bar at DTG-000345 and rigs byed at DTG-000341 retain N-042's exact local questions rather than a new metaphysical interpretation.

The later prophecy's unusual body descriptions are not diagnoses or historical identifications. Preserve the source's front/blue tooth, right elbow, scorpion-shaped mole, triangular-eye covering, westward/Vajra-Seat question, two-tipped tongue and emerald arm projection. The causal connection across DTG-000394–000395 is supported by the preceding yis; the nominal fragment should not be judged in isolation. At DTG-000426 the retinue of five thousand, plural all, attained acceptance, and persons possessing virtuous ordinary minds support the person-reading great bodhisattvas for the shortened byang chub sems chen po; this is a local attested construction, not permission to reconstruct every byang chub sems expression from components.

The names in N-045 remain source-based/provisional, including Sūtrade, Jaya Ākar and Bharabhati Sāli. Glorious Protector and Glory-Holder, Glory of Joy and Deity of Bliss, and the two prophetic sequences' other differing names are deliberately not conflated. DTG-000430's cyclic-existence label is repaired without resolving whether mtha' yas qualifies the destroyer or the cyclic existence; N-045's name-boundary qualification remains operative. Sanskrit transliterations such as Jinamitra and Kamalaśīla are not replaced by familiar identities. N-047's anticipatory half yields seven and a half hundreds, while sa ya drug 'bum remains the expressly unresolved literal count; these are different constructions.

<a id="phase-d-prophecy-comparison"></a>
**Source-linked comparison of the two prophetic sequences (N-044/N-045):** This is a comparison, not a reconciliation. The first account introduces seven named ages (DTG-000364), sixty ages of darkness between them (000365), and then: north/Glorious Protector/Jinamitra, 1,300 years (000366–000369); sixty [years] of darkness (000370); south/Glory of Joy/Spiritual Accomplishment of Virtue, 100 years (000371–000373); 120 years of darkness (000374); east/Sūtrade/Jaya Ākar, 1,400 years (000375–000377); 5,000 years of darkness (000378); west/Protector of Bliss/Holder of Heroes, 1,000 years (000379–000381); 5,000 years of darkness (000382); Vajra Seat/Excellent Intelligence/Pure Cool-Maker, 550 years (000383–000386), then elemental destruction (000387–000389).

The second account instead alternates particular destructive figures with: first Glory-Holder after sixty years (000393–000397), then a 1,300-period statement (000398); Deity of Bliss/100 years following sixty years of darkness (000399–000401); a king suppressing practitioners and sixty years' disappearance (000402–000404); a solitary-buddha form/120 years (000405–000406); a Golden-City elder and sixty years of darkness (000407–000409); Glorious Lion/1,400 years (000410); the king's son and sixty years of darkness (000411–000412); Kamalaśīla's master Protector of Youth/1,000 years (000413); the lion-headed commoner, three months after birth and sixty [years] (000414–000415); Beautifying Youth/550 years (000416); the bird-bodied figure, ten years after birth and sixty [years] (000417–000418); Śākya Dzīka/ten years (000419). The text itself calls this seven stages at 000420. The differing names, duration units and number of narrative notices remain as written. No modern date conversion, arithmetic harmonization, silent eighth-stage correction or identity merger is warranted.

<a id="phase-d-notes-04"></a>
**Active note/usage dispositions to append after this evidence checkpoint:** N-T20: subject now approved only for the three actually read logical occurrences; property, assertion, logical reason and reasoning retain their separate historical proposal statuses. N-T22: apply the U07 construction control and retain the qualified nature-reading for 000332 pending 001115. N-048: actual-presences wording is superseded by P2 entities at 000441, while the sun referent, colored speech-emanation, object worn and ritual relationships remain unresolved. N-043: ordinary basis/setting-component reading and all wordplay preserved, without settling the four gathered in time or scriptural-collection scope. N-T50: sacred pledge also applies at 000348, retaining vows. N-T23: transmission already conforms at 000332/000362; this does not settle opaque lung sdeb at 000325 or the complete lung bstan/prophecy expression at 000337. Historical notes and approval records will not be rewritten.

<a id="phase-d-resumption-03"></a>
### Resumption 03 — preserved interrupted work and current-input verification

Active reviewer/session: **DTG-PD-20261005-Astra-03**, GPT-6 Astra Pro, independent of the authoring and October 1 source-reconciliation runs. Earlier Phase D semantic-review statements remain attributed to sessions 01/02; verification of this review's repairs is a self-check, not another independent certification. The current assignment authorizes minimal English and translation-note repairs only in this repository, with no source, segmentation, glossary-assignment or release-tag changes.

The checkout initially contained unpublished Batch 04 edits in `paired/translation.md`, this report, `LEGACY-NOTES.md` and `USAGES.json`, on `review/post-translation-20261005` at `70ad217392aea5fa0774b5f02a6de9300ab74517`. All four files were preserved unchanged at **`cbb308f20db0dbd00ec261c4bd017ffbfd7ad53c`**, pushed to `recovery/phase-d-interrupted-20261005-cont03`, and matched to that remote ref. The review branch was then fast-forwarded to the preservation commit. Other checkouts/worktrees, stash state and all historical tag objects were left untouched. Remote main remains **`fc3a443ba5987efb0b132990bf131a236fa57320`**. No review pull request existed at this checkpoint; adoption PR #5 is verified merged.

**Resumed English input:** `cbb308f20db0dbd00ec261c4bd017ffbfd7ad53c`; canonical English SHA-256 **`cf32cc7eb0c12173b13b204d86115f31338c9ab821c16e09b2c36419844baa2f`**. The complete active standard (including I §8.1 and III), all 283 glossary rows/all eight columns, AGENTS, status, handoff, decisions, retained format, source provenance and existing review/usage records were read. Root `FORMAT.md` remains absent; the already recorded adopted paired-format documentation governs. The policy, golden/source, format and lineage hashes reproduce the original freeze table. Standard, glossary and DECISIONS reproduce the adopted `10fe4e8c1ea0be37a205753dbb4a7e6e4c84a126` blobs exactly. The file history contains no later local terminology override; the earlier scoped rendering decisions remain structural decisions, not new shared terminology authority.

The finite scope is unchanged: **2,667 pairs / 5,484 golden objects**, including the opening, all six chapters, all 15 closing pairs, source annotations and linked unresolved spans. At this checkpoint, sessions 01/02 have a verified saved semantic-coverage record through ordinal 300. The preserved Batch 04 claims reading through ordinal 450, but its repair verification and status integration are pending. Continuation 03 has additionally reread current ordinals **1–100**, with all **50** first-encountered attached notes, from the actual canonical files; this is not 100 additional distinct pairs. Existing qualifications and supported repairs are retained. Fresh source-order rereading continues at ordinal 101, while the next range absent from the saved earlier read record is 451–2667. No complete-work readiness is claimed.

**Actual current-input checks, before new repairs by continuation 03:** exact replay of all **99** recorded pair operations (**82** English repairs and **17** review-link insertions) reproduces all current pair payloads. There are **77** distinct English-repair pairs and **86** changed pairs including note-only changes. Fixed Tibetan/golden bytes, all 2,667 IDs/order, policy/format/lineage, inherited note associations, original usage history and **696** English local-link targets pass the read-only integrity check. `git diff --check` passes. Replay establishes reproducibility, not semantic correctness of the preserved Batch 04.

The eight existing validators/build checks were actually rerun on this preserved input. `paired/validate.py` (ordinary and `--require-final`), `paired/migrate.py --check`, `paired/project.py --check`, and the golden-review translation validator/build check all fail at the historical protected-glossary contract, as before. The golden-review corruption suite passes its positive case and all **36** deliberately corrupted fixtures. **`paired/test_paired.py` now runs 64 tests: 53 pass, nine fail and two error.** Both positive-case errors are the exact released-English comparison at DTG-000002. That same early comparison preempts the intended rejection in nine negative fixtures: closing-as-seventh-chapter, closing-role change, restored-verse deletion, extraneous source text, missing final signoff, hidden source heading, Tibetan join-newline change, whitespace trimming and Tibetan-word mutation. These are present on the resumed input after earlier authorized English repairs; they are not all the original pre-edit baseline failures, and they do not demonstrate a new Tibetan alteration. The earlier 63-pass/one-error result remains historical, not the current test result. No historical validation contract, signed receipt or release is changed to conceal this mismatch. The standard's 63 semantic regression specifications have **not** been executed as a test suite.

<a id="phase-d-reread-03"></a>
### Continuation 03: current-text reread through ordinal 300

Current ordinals **1–300** have now been reread in source order, with all **97** first-encountered note records (50 + 30 + 17), under Q1–Q9, I §8.1 and III. This is a reread of existing coverage, not 300 additional distinct reviewed pairs. The current source corrections, separated annotations, title/continuum and word/sound distinctions, matter/awareness contrast, sacred pledges/vows, retained descriptive names and exact numerical constructions were checked before proposing changes.

The following three findings were recorded **before application**. S07 clarifies the scope of the five further sites; S08 preserves an explicit ordinal rather than distance phrasing; E02 extends the confirmed imperative-pronoun repair. These are not new terminology assignments. N-019/020/021/022/023/026–036 and the exact-linked earlier Phase D construction questions retain their narrower unresolved scopes. In particular, no source variant is promoted to main text, no thal-yig/lda-ldi decipherment is invented, and no full phrase is reconstructed from component matches.

<!-- phase-d-reread-03-operations -->
```json
[
  {
    "pair": "DTG-000212",
    "ordinal": 215,
    "golden": [
      "U00413",
      "U00414",
      "U00415"
    ],
    "family": "S07",
    "kind": "english",
    "tibetan": "སྟོང་དང་གནས་གཞན་ལྔ་ཡིན་པས། །\nའདི་ཉིད་ཤེས་པ་ཙམ་གྱིས་ནི། །\nབཅོམ་ལྡན་འདས་ལ་རེག་པར་སྦྱོར། །",
    "before": "Since there are a thousand and five further sites,",
    "after": "Since there are a thousand sites and five further ones,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "U00410–U00413 explicitly gives five sites with two hundred each and one additional site each. In སྟོང་དང་གནས་གཞན་ལྔ་ the further/other sites are the five, not the entire thousand-and-five. Make the modifier scope unambiguous without changing either number or the following mere-knowing condition.",
    "context_pairs": [
      "DTG-000211",
      "DTG-000212",
      "DTG-000213"
    ]
  },
  {
    "pair": "DTG-000275",
    "ordinal": 278,
    "golden": [
      "U00582",
      "U00583",
      "U00584",
      "U00585",
      "U00586"
    ],
    "family": "S08",
    "kind": "english",
    "tibetan": "དེ་འོག་འཇིག་རྟེན་དགུ་པ་ན། །\nདུང་ལྡན་ཐལ་བའི་ལྷ་ཞེས་པ། །\nདད་ཅིང་བསུང་བའི་དྲི་ཡིས་མྱོས། །\nའཁྱུག་ཅིང་རབ་ཏུ་འབར་བའི་འོད། །\nརབ་ཏུ་མེར་མེར་པོ་ཡིས་འཁྲིགས། །",
    "before": "Nine worlds below it,",
    "after": "In the ninth world below it,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "དེ་འོག་འཇིག་རྟེན་དགུ་པ་ན། explicitly locates this in the ninth world below the preceding realm. Preserve the ordinal construction, as in the nearby sixth-world expressions, rather than assimilating it to the cardinal-distance and beyond-six constructions. N-032 and N-034 do not settle a different reading of this line. No location or cosmological map is inferred.",
    "context_pairs": [
      "DTG-000273",
      "DTG-000274",
      "DTG-000275",
      "DTG-000276",
      "DTG-000277"
    ]
  },
  {
    "pair": "DTG-000285",
    "ordinal": 288,
    "golden": [
      "U00601",
      "U00602",
      "U00603"
    ],
    "family": "E02",
    "kind": "english",
    "tibetan": "རང་འདོད་ངེས་པར་སྐྱོལ་བ་ནི། །\nལུང་དང་རིགས་པ་མན་ངག་གིས། །\nསྐྱོན་བསལ་བསྒྲུབ་དང་འགལ་བ་སྤང་། །",
    "before": "To bring one's own position to a definite conclusion,",
    "after": "To bring your own position to a definite conclusion,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "རང་འདོད་ is governed here by the explicit second-person instructions remove, establish and abandon in U00603. Retain the same addressee across the purpose clause and its imperatives, extending the already confirmed E02 pattern. The descriptive own/others constructions in DTG-000284 and DTG-000295 are not changed. N-036 preserves the remaining argumentation imagery and unenumerated counts.",
    "context_pairs": [
      "DTG-000284",
      "DTG-000285",
      "DTG-000286"
    ]
  }
]
```

**Application/self-check:** All three recorded repairs were applied and reread with the eleven listed context pairs. The 1,000 plus five further sites, the explicit ninth-world relation, and the imperative addressee are retained without changing a number, agent, negation or technical component. The full integrity replay passes 2,667 pairs and 696 local-link targets: 85 English operations in 79 pairs, 17 review links and 88 changed pairs including note-only changes, plus the separately recorded source-annotation repair. The final paired validator and projector check were rerun; both still report the historical protected-glossary mismatch, so the projector produced no new reader output. `git diff --check` passes. This is repair self-verification, not another independent review.

<a id="phase-d-recovered-04-check"></a>
### Continuation 03: recovered Batch 04 verified

All current ordinals **301–450** (DTG-000298–000447), their **21** first-encountered notes and all necessary preceding context were read in source order. Together with the prior reread this is **450 distinct current pairs and 118 first-encountered attached notes**, not additive coverage across reviewers. The full eight-column rows governing Ground/basis, ordinary mind and whole compounds, key point, sacred pledge, entity, realm, spiritual accomplishment and literary tantra were rechecked. N-T20 was also reread in full, including the limited logical-subject disposition and the still-provisional adjacent expressions.

The recovered **20 English repairs in 20 pairs**, including the earlier DTG-000188 training-basis return, and six note-link insertions were self-checked against their recorded exact source and immediate clauses. The ordinary-basis repairs do not alter technical Ground, the five aggregates or the source's component wordplay. Ordinary mind retains the loving/virtuous qualifiers; entities retains all three embodiment/speech/awakened-mind members and the effortless result. The descriptive-name corrections retain spiritual and cyclic-existence components without certifying names or changing modifier attachment. Key point, realm, sacred pledge and literary tantra preserve number and scope. The imperative pronoun does not introduce a different agent. All six recovered note/usage dispositions accurately retain their stated unresolved boundaries and historical records. This is verification within the review, not a second independent certification.

The source corrections at G-U00626, G-U00632, G-U00651, G-U00710 and G-U00800 already separate annotations; in particular, the selected bus pa alternative is not an unresolved nus pa correction to main text. The impure reading's negation remains. The numerical and name differences in the two prophecy accounts, bodily signs, anticipatory-half construction, large unresolved numerical phrase and unexpanded ritual references remain as documented in Batch 04. No additional main-English repair is justified solely by their unfamiliarity. N-041's six chapter descriptions and N-T22's sems nyid family remain for comparison with the ensuing chapter endings and DTG-001115.

One further narrow construction question is identified below. It is linked without changing the provisional English or treating it as a confirmed mistranslation.

<a id="pd-q04-02"></a>
#### PD-Q04-02 — Maturation and the five families

**DTG-000446 / U00971–U00973.** Tibetan: `དེ་ནས་ལྕང་ལོ་ཅན་གྱི་གནས། །` / `ཀུན་གཟིགས་རྣམ་པར་སྣང་མཛད་ཀྱིས། །` / `འདི་ཉིད་བཟུང་བས་རིགས་ལྔར་སྨིན། །`

Current English: “Then, in the abode of Those with Long Locks, / the All-Seeing Vairocana / held this, bringing the five families to maturity.” Retain provisionally. The teacher is the explicit holder, and the holding has an instrumental connection to maturation. But `རིགས་ལྔར་སྨིན` does not by itself settle whether the five families are the recipients brought to maturity, the forms/aspect in which maturation occurs, or the category into which an unexpressed recipient matures. An internal parallel making the maturation subject and this terminative relationship explicit, or authorized commentary on this clause, would settle it. N-049's existing name/count qualifications remain; no new family designation, agent or historical identity is supplied. **Severity:** medium potential relationship ambiguity. **Confidence:** moderate that the English remains interpretive; no confidence claim that the alternative is superior.

<!-- phase-d-q04-02-link -->
```json
[
  {
    "pair": "DTG-000446",
    "ordinal": 449,
    "golden": [
      "U00971",
      "U00972",
      "U00973"
    ],
    "family": "PD-Q04-02",
    "kind": "review-link",
    "tibetan": "དེ་ནས་ལྕང་ལོ་ཅན་གྱི་གནས། །\nཀུན་གཟིགས་རྣམ་པར་སྣང་མཛད་ཀྱིས། །\nའདི་ཉིད་བཟུང་བས་རིགས་ལྔར་སྨིན། །",
    "before": "Then, in the abode of Those with Long Locks,\nthe All-Seeing Vairocana\nheld this, bringing the five families to maturity.\n\nEarlier notes: [N-049](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-049).",
    "after": "Then, in the abode of Those with Long Locks,\nthe All-Seeing Vairocana\nheld this, bringing the five families to maturity.\n\nEarlier notes: [N-049](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-049).\n\nReview note: [Maturation construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q04-02).",
    "rationale": "Link the exact unresolved maturation construction; no main-English change.",
    "severity": "documentation",
    "confidence": "high for link and source scope"
  }
]
```

**Link application/integrity:** The exact question link was applied without changing the main English. Full recorded-operation replay passes: 2,667 pairs, 103 operations (85 English repairs and 18 review links), 79 distinct English-repair pairs, 89 changed pairs including note-only changes, and 697 local-link targets. Fixed Tibetan/golden/policy/format/lineage, IDs/order and inherited note/history checks pass. English SHA-256: `5ceabb13015b9891ea4103cdca4e7f9d57ac51cc31f2c1ec20f47cde00cbe3b9`. No new generated view was produced; the existing release-bound build failures remain as actually rerun above. `git diff --check` passes. Saved semantic coverage is now 450/2,667; continuation is ordinal 451, DTG-000448. Text readiness remains provisional and the complete-work pass remains in progress.

<a id="phase-d-batch-05"></a>
### Batch 05 — source ordinals 451–600

All **150** current pairs DTG-000448–000597 were read in source order, with all **38** first-encountered active/historical note records, their current source updates and complete proposal fields. Current ordinals 601–615 were also read as connected context for N-064, without adding them to this batch's coverage. For the historical note view only duplicated unit-by-unit Tibetan quotations were omitted; the current fixed Tibetan was read in full in the pair view, and all source-annotation text, alternatives, scope and qualifications were retained.

**Evidence before application:** 25 English operations in 22 pairs and one question-link insertion are specified below. The full eight-column glossary rows and the complete expressions govern; no finding follows solely from an English substring or a historical example. Repeated T03, T02, T19, T01, T09 and T13 findings retain their earlier scoped rationale. New T23 covers the actual category sequence, preserving discipline, discourse collection and higher doctrine rather than conflating their complete labels. T24 applies the process form familiarization without settling N-057's shifting construction. E03 repairs a dangling filial relation; S10 distinguishes physical limbs from the literary branch metaphor; S09 restores a stated wish-condition while leaving the compressed result clause qualified.

<!-- phase-d-batch-05-operations -->
```json
[
  {
    "pair": "DTG-000448",
    "ordinal": 451,
    "golden": [
      "U00978",
      "U00979",
      "U00980"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "བརྫུས་དང་སྒོ་ང་ལས་སྐྱེས་དང་། །\nདྲོད་དང་མངལ་ནས་སྐྱེས་པ་ཡི། །\nསེམས་ཅན་རྣམས་ནི་སྨིན་པར་བྱེད། །",
    "before": "Sentient beings",
    "after": "Karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000450",
    "ordinal": 453,
    "golden": [
      "U00983",
      "U00984",
      "U00985"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "འདི་ཡི་མཛད་པ་སུམ་ཅུ་དྲུག །\nསྐུ་གསུང་ཐུགས་ལ་བརྟེན་ནས་ནི། །\nགདུལ་ཡུལ་སེམས་ཅན་རྣམས་ལ་སྣང༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000485",
    "ordinal": 488,
    "golden": [
      "U01068",
      "U01069",
      "U01070"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "འདི་དུས་འཁོར་བ་དོང་སྤྲུགས་ཏེ། །\nསེམས་ཅན་རྣམས་ཀྱིས་སངས་རྒྱས་འཐོབ། །\nའགྲོ་བ་དྲུག་ཅེས་སྣང་མི་སྲིད། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000486",
    "ordinal": 489,
    "golden": [
      "U01071",
      "U01072",
      "U01073"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "བསྐལ་པ་སྟོང་ཕྲག་ཉི་ཤུར་ནི། །\nསེམས་ཅན་འཁོར་བ་རྒྱུན་ཆད་ནས། །\nལུས་ཅན་རྣམ་པར་མི་སྣང་ངོ༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000487",
    "ordinal": 490,
    "golden": [
      "U01074",
      "U01075",
      "U01076",
      "U01077"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "དེ་ནས་ལས་ཀྱི་བྱེ་བྲག་ལས། །\nསེམས་ཅན་ཉོན་མོངས་མངོན་མེད་ཀྱང༌། །\nབག་ལ་ཉལ་བ་ལངས་པའི་དབང་། །\nཤིན་ཏུ་ཕྲ་བ་བླངས་པའི་གཟུགས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000488",
    "ordinal": 491,
    "golden": [
      "U01078",
      "U01079"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "གྲངས་མང་རབ་ཏུ་ཕྲ་བ་ལས། །\nགཟུགས་ཅན་སེམས་ཅན་ལུས་འཕེལ་འགྱུར། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000510",
    "ordinal": 513,
    "golden": [
      "U01124",
      "U01125",
      "U01126"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སྤྱི་མཐུན་ལས་ཀྱི་བྱེ་བྲག་ལས། །\nསེམས་ཅན་ལས་ཀྱི་བརྟེན་སོ་ཡིས། །\nཕྱི་ཡི་འབྱུང་བ་ལ་བརྟེན་ནས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000522",
    "ordinal": 525,
    "golden": [
      "U01145",
      "U01146"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "རྩི་ནི་སེམས་ཅན་གཞན་དོན་དང་། །\nརང་གི་དོན་ཡང་རྫོགས་པའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000524",
    "ordinal": 527,
    "golden": [
      "U01148",
      "U01149",
      "U01150",
      "U01151"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་དུས་ནི་རྣམ་པ་བརྒྱད། །\nནད་དང་རླུང་དང་ཚ་བ་ནི། །\nཤེས་པ་ཉོན་མོངས་བྱང་སེམས་དང་། །\nཡེ་ཤེས་ཉིད་དང་འབྱུང་བའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000526",
    "ordinal": 529,
    "golden": [
      "U01155"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་རླུང་སེམས་འཕོ་བའི་དུས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000534",
    "ordinal": 537,
    "golden": [
      "U01168"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་གཅིག་གི་དུས་ཡིན་ནོ། །",
    "before": "sentient being",
    "after": "karmic being",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000535",
    "ordinal": 538,
    "golden": [
      "U01169",
      "U01170",
      "U01171",
      "U01172"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་སྤྱི་ཡི་དུས་དག་ནི། །\nདང་པོ་དཔག་ཏུ་མེད་པ་ནས། །\nཐ་མ་ཚེ་ལོ་བཅུ་པའི་བར། །\nདུས་ཀྱི་རིམ་པ་དྲུག་ཅུ་འབྱུང༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000485",
    "ordinal": 488,
    "golden": [
      "U01068",
      "U01069",
      "U01070"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འདི་དུས་འཁོར་བ་དོང་སྤྲུགས་ཏེ། །\nསེམས་ཅན་རྣམས་ཀྱིས་སངས་རྒྱས་འཐོབ། །\nའགྲོ་བ་དྲུག་ཅེས་སྣང་མི་སྲིད། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the adopted cyclic-existence label for khor ba, preserving its negation, possessors, temporal scope and the distinct rgyun/flow construction."
  },
  {
    "pair": "DTG-000486",
    "ordinal": 489,
    "golden": [
      "U01071",
      "U01072",
      "U01073"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "བསྐལ་པ་སྟོང་ཕྲག་ཉི་ཤུར་ནི། །\nསེམས་ཅན་འཁོར་བ་རྒྱུན་ཆད་ནས། །\nལུས་ཅན་རྣམ་པར་མི་སྣང་ངོ༌། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the adopted cyclic-existence label for khor ba, preserving its negation, possessors, temporal scope and the distinct rgyun/flow construction."
  },
  {
    "pair": "DTG-000451",
    "ordinal": 454,
    "golden": [
      "U00986",
      "U00987",
      "U00988",
      "U00989",
      "U00990"
    ],
    "family": "E03",
    "kind": "translation",
    "tibetan": "ང་ནི་མྱ་ངན་འདས་འོག་ཏུ། །\nནུབ་ཕྱོགས་ཨུ་རྒྱན་དག་གི་ཡུལ། །\nདྷ་ན་ཀོ་ཤའི་ལྷ་ལྕམ་ལ། །\nཕ་མེད་བུ་ནི་བཛྲ་ཧེ། །\nའདིས་ནི་དམ་པའི་བསྟན་པ་འཛིན། །",
    "before": "to the divine lady of Dhanakośa,\na fatherless son, Vajrahe,",
    "after": "a fatherless son of the divine lady of Dhanakośa,\nVajrahe,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "U00988–U00990 gives the divine lady, a fatherless son, and this son as the explicit upholder. The dangling English to-phrase currently appears attached to will uphold. Express the already stated filial relation without inserting a birth verb, another upholder, a historical identification or a reconstructed name."
  },
  {
    "pair": "DTG-000469",
    "ordinal": 472,
    "golden": [
      "U01024",
      "U01025",
      "U01026",
      "U01027",
      "U01028",
      "U01029",
      "U01030",
      "U01031"
    ],
    "family": "T19",
    "kind": "translation",
    "tibetan": "བསྟན་པའི་སྙིང་ཐིག་གསང་བ་འདི།།\nདེ་ལྟར་བསྟན་པ་བདུན་འདས་ནས། །\nཞིང་ཁམས་གཉིས་ལ་ངེས་སྤྱད་ནས། །\nདེ་ལྟར་བདུན་པོ་ཐལ་ནས་ཀྱང༌། །\nརྡོ་རྗེ་གདན་གྱི་སྤོ་ལ་ནི། །\nབསྟན་པ་ཀུན་གྱི་གསུང་གི་བཙས། །\nརང་བྱུང་ཆེན་པོའི་ཡི་གེ་ཉིད། །\nསྒྲ་དང་བཅས་ཏེ་བབས་པ་ནི། །",
    "before": "two fields",
    "after": "two realms",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The two zhing khams are the realms in the transmission-course account, not an operative field metaphor. Preserve the repeated seven and the unestablished course, heart-sphere and speech-token constructions."
  },
  {
    "pair": "DTG-000478",
    "ordinal": 481,
    "golden": [
      "U01055",
      "U01056"
    ],
    "family": "T23",
    "kind": "translation",
    "tibetan": "མདོ་སྡེའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nདྲང་ངེས་ལས་ཀྱི་མཐའ་ལ་དགོད། །",
    "before": "Through the sūtra teaching for eight ages,",
    "after": "Through the teaching of the discourse collection for eight ages,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The mdo sde category occurs between the discipline and higher-doctrine teaching categories in U01050–U01066. Apply the complete approved discourse collection label, preserving teaching and eight ages; the drang nges las kyi mtha construction remains N-052."
  },
  {
    "pair": "DTG-000484",
    "ordinal": 487,
    "golden": [
      "U01066",
      "U01067"
    ],
    "family": "T23",
    "kind": "translation",
    "tibetan": "མངོན་པའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nཐམས་ཅད་ཚེ་གཅིག་འབྲས་བུ་ཐོབ། །",
    "before": "Through the higher teaching for eight ages,",
    "after": "Through the teaching of higher doctrine for eight ages,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Mngon pa here names the doctrinal category in the three-category teaching sequence, not a generic higher adjective. Preserve the separate bstan pa/teaching and all eight ages; do not promote the separately reported hundred variant into main text."
  },
  {
    "pair": "DTG-000491",
    "ordinal": 494,
    "golden": [
      "U01084",
      "U01085",
      "U01086"
    ],
    "family": "T01",
    "kind": "translation",
    "tibetan": "རྒྱུད་ཀྱི་ལུས་དང་ཡན་ལག་ནི། །\nལུས་ལ་བཀོད་པ་བརྒྱ་ཕྲག་ནི། །\nགཉིས་དང་ལྔ་བཅུ་ཐམ་པའོ། །",
    "before": "body and branches of the continuum",
    "after": "body and branches of the tantra",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The following explicit questions, six chapter arrays and counted textual body/branches establish the literary sense of rgyud. Apply P1 tantra, without altering the metaphor or any count."
  },
  {
    "pair": "DTG-000497",
    "ordinal": 500,
    "golden": [
      "U01095",
      "U01096",
      "U01097",
      "U01098"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གཉིས་པའི་ལུས་ནི་ཉེར་བསྟན་པ། །\nགནད་རྣམས་འདུས་པའི་བཀོད་པ་ལ། །\nཞུས་པ་ཉི་ཤུ་རྩ་བརྒྱད་ལས། །\nགནད་དུས་བཀོད་པ་སུམ་ཅུ་གཅིག །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete gnad label in the chapter-array description; preserve the twenty-eight questions and thirty-one arrays."
  },
  {
    "pair": "DTG-000497",
    "ordinal": 500,
    "golden": [
      "U01095",
      "U01096",
      "U01097",
      "U01098"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གཉིས་པའི་ལུས་ནི་ཉེར་བསྟན་པ། །\nགནད་རྣམས་འདུས་པའི་བཀོད་པ་ལ། །\nཞུས་པ་ཉི་ཤུ་རྩ་བརྒྱད་ལས། །\nགནད་དུས་བཀོད་པ་སུམ་ཅུ་གཅིག །",
    "before": "crucial-point times",
    "after": "key-point times",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply gnad/key point within the explicitly provisional literal gnad dus rendering while retaining times, its Tibetan identity and N-054. This does not emend dus to dus with an a-chung or approve the entire compound."
  },
  {
    "pair": "DTG-000519",
    "ordinal": 522,
    "golden": [
      "U01142"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "དྲིས་ནི་བཅུད་ཀྱིས་ལེན་པ་འགྲུབ། །",
    "before": "taking nourishment from vital essences",
    "after": "taking nourishment from quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The same bcud kyis len pa nourishment construction as the earlier scoped T13 finding occurs with smell. P2 quintessence applies in this nourishment/concentration sense; the whole expression is still a linked local construction, not a new canonical assignment."
  },
  {
    "pair": "DTG-000538",
    "ordinal": 541,
    "golden": [
      "U01181",
      "U01182"
    ],
    "family": "T24",
    "kind": "translation",
    "tibetan": "གོམས་པའི་འཕོ་དུས་བརྒྱད་རིམ་གྱིས། །\nསྤྱོད་པ་ཕྱི་ནས་ངན་པར་འགྱུར། །",
    "before": "habituation",
    "after": "familiarization",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved process form for goms pa, distinct from sgom/cultivation. The eight stages, shifting relation and subsequent worsening remain unchanged and qualified by N-057."
  },
  {
    "pair": "DTG-000579",
    "ordinal": 582,
    "golden": [
      "U01275",
      "U01276",
      "U01277"
    ],
    "family": "S10",
    "kind": "translation",
    "tibetan": "ས་ཡི་ཟུག་པས་རྡུལ་རྣམས་འབྱིན། །\nབྱེར་བ་ཡིས་ནི་ཡན་ལག་འབྱིན། །\nསྙོམས་པས་ལུས་འབྱུང་རྫོགས་པའོ། །",
    "before": "its dispersal produces branches;",
    "after": "its dispersal produces limbs;",
    "severity": "medium",
    "confidence": "moderate-high",
    "rationale": "The verse concerns earth producing particles and completing the elements of the body. Yan lag here denotes the bodily limbs in that physical sequence, unlike the explicitly textual branches at DTG-000491–000507. No change is made to those textual metaphors or to the elemental functions."
  },
  {
    "pair": "DTG-000594",
    "ordinal": 597,
    "golden": [
      "U01309",
      "U01310"
    ],
    "family": "S09/T02",
    "kind": "translation",
    "tibetan": "འཁོར་བའི་ལས་རྒྱུད་གཅད་འདོད་ན། །\nབྱ་བ་བྲལ་བར་རྫོགས་པས་རྫོགས། །",
    "before": "To cut the karmic continuum of samsara:",
    "after": "If one wishes to cut the karmic continuum of cyclic existence,",
    "severity": "medium",
    "confidence": "high for conditional and label; remainder provisional",
    "rationale": "Preserve the explicit wish-condition gcad dod na rather than recasting it as a bare purpose. Rgyud remains karmic continuum, not literary tantra; khor ba takes cyclic existence. The unexpressed subject and compressed completion clause remain within N-064; no new doctrinal subject is supplied."
  },
  {
    "pair": "DTG-000492",
    "ordinal": 495,
    "golden": [
      "U01087",
      "U01088",
      "U01089",
      "U01090"
    ],
    "family": "PD-Q05-01",
    "kind": "review-link",
    "tibetan": "དང་པོ་ངེས་པ་གསལ་བ་ཡིས། །\nསྣ་ཚོགས་བཀོད་པ་ཡན་ལག་ལ། །\nཞུས་པ་བདུན་ཅུ་ཐམ་པ་ལ། །\nཡན་ལག་བཀོད་པ་བརྒྱ་གཅིག་གོ། །",
    "before": "First, through clarity of ascertainment,\nin the branches of the manifold array,\nthere are exactly seventy questions;\nthe arrays of the branches number one hundred and one. [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054)\n\n[^G-U01090]\n\nEarlier notes: [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054).",
    "after": "First, through clarity of ascertainment,\nin the branches of the manifold array,\nthere are exactly seventy questions;\nthe arrays of the branches number one hundred and one. [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054)\n\n[^G-U01090]\n\nEarlier notes: [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054).\n\nReview note: [Numerical construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q05-01).",
    "severity": "documentation",
    "confidence": "high for exact span and linkage",
    "rationale": "Link the precise main-count question without changing the selected source or asserting that either competing numerical analysis is settled."
  }
]
```

<a id="pd-q05-01"></a>
#### PD-Q05-01 — Main count and separately reported numerical variant

**DTG-000492 / U01087–U01090**, particularly `ཡན་ལག་བཀོད་པ་བརྒྱ་གཅིག་གོ། །`. Current English says “the arrays of the branches number one hundred and one.” Retain this **provisionally**, not as an independently certified count. The scope of `བརྒྱ་གཅིག` needs to distinguish the reading one hundred from an elliptical hundred-and-one count; the separately printed “eleven also occurs” does not by itself establish either the main arithmetic or a full replacement yielding 111. The older N-054 rationale is an inherited interpretation, not an owner-approved numerical rule. A decisive internal count construction or authorized commentary on this enumeration would settle it; no new witness reading, change to the golden text or adjustment to actual chapter totals is made. **Severity:** medium possible numerical difference. **Confidence:** moderate that this requires qualification; neither alternative is certified here.

<a id="phase-d-notes-05"></a>
**Active note/usage dispositions recorded before appending:** The following exact-scope records are to be appended to the existing usage file and linked in the active legacy-note index. The ten original usage records, all seventeen earlier dispositions and original historical notes remain unchanged. These are status/scope updates, not new canonical glossary assignments.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-051",
    "pairs": [
      "DTG-000469"
    ],
    "ids": [
      "U01024",
      "U01025",
      "U01026",
      "U01027",
      "U01028",
      "U01029",
      "U01030",
      "U01031"
    ],
    "source": {
      "DTG-000469": "བསྟན་པའི་སྙིང་ཐིག་གསང་བ་འདི།།\nདེ་ལྟར་བསྟན་པ་བདུན་འདས་ནས། །\nཞིང་ཁམས་གཉིས་ལ་ངེས་སྤྱད་ནས། །\nདེ་ལྟར་བདུན་པོ་ཐལ་ནས་ཀྱང༌། །\nརྡོ་རྗེ་གདན་གྱི་སྤོ་ལ་ནི། །\nབསྟན་པ་ཀུན་གྱི་གསུང་གི་བཙས། །\nརང་བྱུང་ཆེན་པོའི་ཡི་གེ་ཉིད། །\nསྒྲ་དང་བཅས་ཏེ་བབས་པ་ནི། །"
    },
    "realization": "two realms",
    "status": "Approved P2 realm label; remaining constructions provisional",
    "reason": "The realm label is adopted without approving heart-sphere, speech-token, Great Naturally Arisen as a name, or the definite-course construction. Seven/two and the embodiment/speech/awakened-mind sequence remain distinct.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-052",
    "pairs": [
      "DTG-000475",
      "DTG-000478",
      "DTG-000484"
    ],
    "ids": [
      "U01048",
      "U01049",
      "U01050",
      "U01051",
      "U01055",
      "U01056",
      "U01066",
      "U01067"
    ],
    "source": {
      "DTG-000475": "དེ་ལ་སོགས་ཏེ་སྟོན་པའི་འཁོར། །\nའཕགས་པ་ཉན་ཐོས་ཁྲི་ཕྲག་གཉིས། །\nའདུལ་བའི་བསྟན་པ་བསྐལ་པ་གཅིག །\nདགྲ་བཅོམ་འབྲས་བུ་ཉིད་ལ་བཀོད། །",
      "DTG-000478": "མདོ་སྡེའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nདྲང་ངེས་ལས་ཀྱི་མཐའ་ལ་དགོད། །",
      "DTG-000484": "མངོན་པའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nཐམས་ཅད་ཚེ་གཅིག་འབྲས་བུ་ཐོབ། །"
    },
    "realization": "discipline; discourse collection; higher doctrine",
    "status": "Approved P2 category labels in this sequence",
    "reason": "Discipline already conforms and does not require an added collection. Discourse collection and higher doctrine retain the explicit teaching nouns and durations. The participants, perfection attachment and provisional/definitive activity construction remain unresolved; no efficacy or cosmological reconciliation is implied.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-054",
    "pairs": [
      "DTG-000491",
      "DTG-000492",
      "DTG-000497"
    ],
    "ids": [
      "U01084",
      "U01085",
      "U01086",
      "U01087",
      "U01088",
      "U01089",
      "U01090",
      "U01095",
      "U01096",
      "U01097",
      "U01098"
    ],
    "source": {
      "DTG-000491": "རྒྱུད་ཀྱི་ལུས་དང་ཡན་ལག་ནི། །\nལུས་ལ་བཀོད་པ་བརྒྱ་ཕྲག་ནི། །\nགཉིས་དང་ལྔ་བཅུ་ཐམ་པའོ། །",
      "DTG-000492": "དང་པོ་ངེས་པ་གསལ་བ་ཡིས། །\nསྣ་ཚོགས་བཀོད་པ་ཡན་ལག་ལ། །\nཞུས་པ་བདུན་ཅུ་ཐམ་པ་ལ། །\nཡན་ལག་བཀོད་པ་བརྒྱ་གཅིག་གོ། །",
      "DTG-000497": "གཉིས་པའི་ལུས་ནི་ཉེར་བསྟན་པ། །\nགནད་རྣམས་འདུས་པའི་བཀོད་པ་ལ། །\nཞུས་པ་ཉི་ཤུ་རྩ་བརྒྱད་ལས། །\nགནད་དུས་བཀོད་པ་སུམ་ཅུ་གཅིག །"
    },
    "realization": "tantra; key point; key-point times (provisional)",
    "status": "P1/P2 labels applied; counts and complete gnad dus construction provisional",
    "reason": "The body/branches account is explicitly textual. Only gnad terminology is repaired inside the visibly provisional gnad dus wording. The brgya gcig main-count question is now precisely linked; the reported eleven remains a separate variant, and no count is changed to match a chapter inventory.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T16",
    "pairs": [
      "DTG-000519"
    ],
    "ids": [
      "U01142"
    ],
    "source": {
      "DTG-000519": "དྲིས་ནི་བཅུད་ཀྱིས་ལེན་པ་འགྲུབ། །"
    },
    "realization": "taking nourishment from quintessence",
    "status": "Approved P2 component in the same reviewed nourishment construction; complete construction provisional",
    "reason": "Extend the earlier scoped quintessence disposition to this actual smell/nourishment occurrence. Do not turn the older whole-expression proposal into a shared assignment or settle the distinct gnas bcud yul question.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T25",
    "pairs": [
      "DTG-000524",
      "DTG-000531"
    ],
    "ids": [
      "U01148",
      "U01149",
      "U01150",
      "U01151",
      "U01164",
      "U01165"
    ],
    "source": {
      "DTG-000524": "སེམས་ཅན་དུས་ནི་རྣམ་པ་བརྒྱད། །\nནད་དང་རླུང་དང་ཚ་བ་ནི། །\nཤེས་པ་ཉོན་མོངས་བྱང་སེམས་དང་། །\nཡེ་ཤེས་ཉིད་དང་འབྱུང་བའོ། །",
      "DTG-000531": "བྱང་ཆུབ་སེམས་ནི་འཇིལ་བ་དང་། །\nརབ་ཏུ་འཕྲིགས་ཤིང་ཕྲ་བར་འགྱུར། །"
    },
    "realization": "awakening ordinary mind (retained provisionally)",
    "status": "Unresolved whole-expression treatment; not an approved component-built default",
    "reason": "The adjacent short/full forms are internally linked, but the bodily sequence does not settle aspiration, bodily substance or another technical referent. The old component-preservation rationale alone cannot establish this whole expression. Retain its exact-linked provisional treatment pending a decisive internal construction or authorized commentary; do not apply it to bodhisattva occurrences.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-057",
    "pairs": [
      "DTG-000538"
    ],
    "ids": [
      "U01181",
      "U01182"
    ],
    "source": {
      "DTG-000538": "གོམས་པའི་འཕོ་དུས་བརྒྱད་རིམ་གྱིས། །\nསྤྱོད་པ་ཕྱི་ནས་ངན་པར་འགྱུར། །"
    },
    "realization": "familiarization",
    "status": "Approved P2 process label; shifting construction provisional",
    "reason": "Goms pa takes the process form familiarization here, not cultivation. The eight shifting stages, individual/collective times, physiological verbs and lifespan counts remain qualified; the label repair is not approval of their entire scheme.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T30",
    "pairs": [
      "DTG-000512"
    ],
    "ids": [
      "U01129",
      "U01130",
      "U01131"
    ],
    "source": {
      "DTG-000512": "ནང་འབྱུང་ལས་ཀྱི་རིམ་པ་ནི། །\nསས་ནི་ལུས་ཀྱི་གཞི་བྱས་ཏེ། །\nབསྐྱེད་པས་ཤ་ནི་སྨིན་པར་འདོད། །"
    },
    "realization": "foundation",
    "status": "Locally supported physical construction under P1; no shared reassignment",
    "reason": "Earth explicitly provides the bodily foundation. Retain foundation rather than impose technical Ground or replace it with basis merely for uniformity. This disposition does not yet cover U01339 or settle the other Ground-of-words and chapter-outline uses.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-063",
    "pairs": [
      "DTG-000578",
      "DTG-000579",
      "DTG-000584"
    ],
    "ids": [
      "A2000-C01-S01",
      "U01275",
      "U01276",
      "U01277",
      "U01286"
    ],
    "source": {
      "DTG-000578": "ཆུ་ཡི་ཟུག་པས་དབང་པོ་སྡུད།\nབྱེར་བ་ཡིས་ནི་འཁྲུགས་པར་བྱེད།\nསྙོམས་པ་ཡིས་ནི་འབྲས་བུ་འབྱིན།",
      "DTG-000579": "ས་ཡི་ཟུག་པས་རྡུལ་རྣམས་འབྱིན། །\nབྱེར་བ་ཡིས་ནི་ཡན་ལག་འབྱིན། །\nསྙོམས་པས་ལུས་འབྱུང་རྫོགས་པའོ། །",
      "DTG-000584": ""
    },
    "realization": "water triad present; bodily limbs",
    "status": "Current source restoration recognized; specific bodily sense repaired; other constructions provisional",
    "reason": "The three water verses are present at A2000-C01-S01. U01286 remains the qualified inherited omission query, not evidence of a current missing water triad. Retain all source annotations, twelve announced functions and repeated operations. The unnamed pair, entering another and ritual classifications remain unresolved; the bodily limbs repair is not a new universal yan lag assignment.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T68",
    "pairs": [
      "DTG-000487"
    ],
    "ids": [
      "U01074",
      "U01075",
      "U01076",
      "U01077"
    ],
    "source": {
      "DTG-000487": "དེ་ནས་ལས་ཀྱི་བྱེ་བྲག་ལས། །\nསེམས་ཅན་ཉོན་མོངས་མངོན་མེད་ཀྱང༌། །\nབག་ལ་ཉལ་བ་ལངས་པའི་དབང་། །\nཤིན་ཏུ་ཕྲ་བ་བླངས་པའི་གཟུགས། །"
    },
    "realization": "dormant tendencies (retained provisionally)",
    "status": "Existing whole-expression proposal remains provisional; related approved label clarified",
    "reason": "Keep bag la nyal ba distinct from bag chags, now assigned imprints by P2 rather than the historical note's habitual tendencies comparator. No unconscious mechanism is inferred, and later occurrences require their own reading before the family scope can be reconciled.",
    "review": "REVIEW.md#phase-d-notes-05"
  }
]
```

**Important justified retentions and rejected false positives:** The explicit four birth modes retain warmth rather than an unprinted substitute. Ordinary beings (`འགྲོ་བ`), embodied beings (`ལུས་ཅན`), bodhisattvas and the whole wind-mind compound are not changed merely because nearby sems can becomes karmic being. DTG-000462's Word-Specialist/Glorious/holder boundary remains N-050: an English or Tibetan substring does not settle whether dzin is part of a name or the upholding predicate. The source-based lineage names and non-abiding terminal predicate remain qualified without historical identification.

DTG-000520's **substances** is retained under the dngos po row's material-context exception: the clause explicitly concerns taste transforming its objects into nectar in the bodily/sensory sequence. This is not a free synonym for entity, a claim that all entities are matter, or certification of the described practice's efficacy. DTG-000512's bodily foundation is likewise not silently promoted to technical Ground or rewritten to basis for stylistic consistency. The question/array/branch numbers remain as written, with the newly linked main-count question distinguished from the still-qualified gnad dus phrase.

The source's actions/clothing/faculties list is not emended to food or body. The omission notice at U01144 does not license an invented touch instruction or decide the nectar fragment's referent. The eightfold physiological list retains its order and the printed negative “primordial knowing is not clear”; no bodily-fluid interpretation of byang chub sems is silently adopted. Seasonal orders differ between passages and remain different. The sixty/thirty/thirty, seven fire/seven water/fourteen, 180-period, 720 mornings/evenings and 360-day counts are not forced into an external chronology. The twelve-animal sequence keeps snake before dragon. U01233's single displaced formation/destruction/emptiness note is not treated as multiple independent annotations.

The restored water triad is present at DTG-000578; the historical missing-water finding is therefore rejected as a current omission defect. U01286's annotation remains separately qualified, and the unnamed penetration-pair, entering-another clause and ritual categories remain open. Summon/stir and other printed variants remain separated from root prose. The elemental operations are not collapsed, rationalized or expanded into practical instructions. The long N-064 sequence preserves explicit negations, one/many, repeated completion language, intrinsic nature, self-appearance and primordial knowing; changing the first condition does not settle its unstated subject or Ground-of-words construction.

**Pre-commit self-check rejection of a proposed note update:** The ninth provisional disposition above, N-T68, is **rejected and is being withdrawn**, not adopted. Its claim that P2 assigned bag chags to imprints is unsupported. The actual eight-column row is `བག་ཆགས་` / `Habitual tendencies`, with blank scope/forms/exceptions/related fields, source `G, line 74`, status `Established`. The full-row recheck therefore requires removing the newly appended N-T68 usage record and active-index paragraph below, leaving the existing historical and active N-T68 text unchanged. The older dormant-tendencies proposal remains provisional and distinct from habitual tendencies. This records a correction to this review's own proposed note, not a change to owner approval history or a new shared label. No English pair repair in this batch depends on the rejected claim.

```json
{
  "file": "translations/2026-10-01-golden-aligned/LEGACY-NOTES.md",
  "anchor": "n-t68",
  "before": "**Phase D disposition, 2026-10-05 (continuation 03):** Existing whole-expression proposal remains provisional; related approved label clarified. Keep bag la nyal ba distinct from bag chags, now assigned imprints by P2 rather than the historical note's habitual tendencies comparator. No unconscious mechanism is inferred, and later occurrences require their own reading before the family scope can be reconciled. [Current review and scope](REVIEW.md#phase-d-notes-05).\n\n",
  "after": "",
  "usage_action": "Remove only the just-appended session-03 N-T68 disposition; preserve all seventeen inherited records and the eight other supported session-03 dispositions.",
  "reason": "Actual full glossary row retains Habitual tendencies; imprints was an unsupported proposed-policy claim.",
  "severity": "medium",
  "confidence": "high"
}
```

**Application, changed-clause self-check and validation:** All 25 English repairs in 22 pairs and the numerical-question link were applied and checked against the current Tibetan in a 57-pair changed-clause/context view. The wish-condition, filial relation, physical-limbs sense, complete category labels, number, possessors, modifiers and remaining qualified constructions were rechecked. No source, negation, agent, temporal relation, chapter count or technical component changed beyond the recorded corrections. The unsupported N-T68 note proposal was withdrawn as documented above; eight supported append-only note/usage dispositions remain.

The final paired validator and projector check were actually rerun: both exit 1 at the historical protected-glossary check. The full operation-replay/integrity check exits 0, reproducing 129 pair operations: 110 English repairs in 101 distinct pairs and 19 review links, affecting 112 pair payloads including note-only changes. All 2,667 pair identities/order, fixed source/golden/policy/format/lineage, inherited note associations, historical usage/index records and 698 local-link targets pass. The earlier annotation repair remains unchanged. English SHA-256: `3e3a8e68ead43189ecc244276bb60f4932c1ec7c4516c15915cb3232641bb944`. `git diff --check` passes. No new reader output was produced. This is a repair self-check, not another independent review.

**Saved semantic coverage:** 600/2,667 pairs, ordinals 1–600 through DTG-000597, with 156 first-encountered note records read. Continue at ordinal 601 / DTG-000598. The connected N-064 context through ordinal 615 was read but is not separately counted as completed coverage. The whole-work pass remains in progress; text readiness remains provisional.

<a id="phase-d-batch-06"></a>
### Batch 06 — source ordinals 601–750

All 150 current pairs DTG-000598–000747 and all 39 first-encountered note records were read in source order. The connected N-064 argument was completed, as were the U01493–U01513 dream sequence and the bodily/channel sequences; ordinals 751–760 were additionally read as continuation context, not added to completed coverage. The note-view method is the same as Batch 05: current fixed Tibetan and all note prose/qualifications are read; only duplicate historical unit quotations are elided in the convenience view. Q1–Q9, I §8.1 and III govern. The complete relevant rows, including bare dngos versus dngos po, goms process/state, bcud scope, wind-mind, rtog med, the complete lamp expression, realm and spiritual accomplishment, were rechecked; I §8.1 was reread directly.

**Evidence before application:** The following 21 English operations in 20 pairs extend the confirmed labels and repair three local attachment/syntax issues. S13 puts nyid with direct perception rather than key point; E04 fixes the combining-clause syntax without recreating the historically corrected object/time transposition; S12 distinguishes the practitioner condition from its appearing object. Two further constructions are linked provisionally rather than forcibly corrected.

<!-- phase-d-batch-06-operations -->
```json
[
  {
    "pair": "DTG-000603",
    "ordinal": 606,
    "golden": [
      "U01319"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འདི་ཤེས་འཁོར་བའི་ལམ་འགག་གོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved khor ba label without changing the blocking predicate, this/knowing antecedent or its place in the connected view sequence."
  },
  {
    "pair": "DTG-000615",
    "ordinal": 618,
    "golden": [
      "U01334"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འདིས་ཀྱང་འཁོར་བའི་སྒོ་འགག་གོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved khor ba label without changing the blocking predicate, this/knowing antecedent or its place in the connected view sequence."
  },
  {
    "pair": "DTG-000604",
    "ordinal": 607,
    "golden": [
      "U01320",
      "U01321"
    ],
    "family": "S13/T09",
    "kind": "translation",
    "tibetan": "གནད་ལས་བྱུང་བའི་མངོན་སུམ་ཉིད། །\nགོམས་པའི་སྟོབས་ཀྱིས་འཁྲུལ་པ་འཇིག །",
    "before": "Direct perception arising from the crucial point itself—",
    "after": "Direct perception itself, arising from the key point—",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Nyid follows mngon sum and emphasizes direct perception, not the preceding gnad. Restore its modifier attachment and apply key point. Familiarity remains the approved state form; the following delusion-destruction clause and its implicit topic relation are not expanded."
  },
  {
    "pair": "DTG-000678",
    "ordinal": 681,
    "golden": [
      "U01481"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རྩ་རྣམས་ཁུངས་སུ་བཟུང་བ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000680",
    "ordinal": 683,
    "golden": [
      "U01484"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "བརྗོད་པའི་རྒྱུན་རྣམས་གཅད་པ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000682",
    "ordinal": 685,
    "golden": [
      "U01487"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གཉིད་ལ་གོམས་པ་གནད་ཡིན་ནོ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000685",
    "ordinal": 688,
    "golden": [
      "U01493",
      "U01494"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རྨི་ལམ་གནད་ཀྱི་ལམ་ཁྱེར་ནི། །\nསྔོན་དུ་བྱ་དང་གནད་ལ་དབབ། །",
    "before": "crucial points of dreams onto the path\nconsists of preparation and applying the crucial points",
    "after": "key points of dreams onto the path\nconsists of preparation and applying the key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000687",
    "ordinal": 690,
    "golden": [
      "U01499",
      "U01500",
      "U01501",
      "U01502",
      "U01503",
      "U01504"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ནས་གནད་ལ་འབེབས་དུས་སུ། །\nསྦྱང་དང་བསྒྱུར་དང་བཅད་པ་དང༌། །\nདཀྲུགས་དང་བཅུད་དང་གནད་ལ་འབོར། །\nབསྐྱིལ་བཟློག་ལས་ཀྱི་གནད་བྱས་པས། །\nལས་ཀྱི་རྨི་ལམ་མཐའ་ཟད་དེ། །\nབག་ཆགས་འཁྲུལ་པ་དྲུང་ནས་ཐོན། །",
    "before": "crucial points:\ntraining, transformation, cutting off, and\nstirring, concentrating the vitality, and releasing at the crucial point;\nby applying the crucial points",
    "after": "key points:\ntraining, transformation, cutting off, and\nstirring, concentrating the vitality, and releasing at the key point;\nby applying the key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000700",
    "ordinal": 703,
    "golden": [
      "U01533",
      "U01534",
      "U01535"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དངོས་གཞི་རང་གི་རྒྱུད་བརྟེན་ནི། །\nལུས་ཀྱི་གནད་དང་ངག་དང་ཡང་། །\nསེམས་ཀྱི་གནད་ལ་བརྟེན་པ་ཡིས། །",
    "before": "crucial points of body and speech\nand the crucial point",
    "after": "key points of body and speech\nand the key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000710",
    "ordinal": 713,
    "golden": [
      "U01558",
      "U01559",
      "U01560",
      "U01561",
      "U01562",
      "U01563",
      "U01564",
      "U01565",
      "U01566"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ལུས་ཀྱི་གནད་ནི་རྩ་ཡིན་ཏེ། །\nགནས་དང་བཀོད་པ་འགྱུ་བ་དང་། །\nའཁོར་ལོའི་རྟེན་དང་ལུས་ཀྱི་སྲོག །\nམིང་དང་བྱེ་བྲག་རྒྱུ་དང་རྐྱེན། །\nབྱེད་པའི་ལས་དང་མཚན་ཉིད་དང༌། །\nཉོན་མོངས་ལས་དང་ཡེ་ཤེས་ལས། །\nལམ་ལ་བརྟེན་ནས་མངོན་སྣང་བ། །\nནད་དང་འབྱུང་བའི་བྱེ་བྲག་དང༌། །\nའཁྲུག་མར་གནས་པའི་མཐའ་ཡིས་དབྱེ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000715",
    "ordinal": 718,
    "golden": [
      "U01571",
      "U01572"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ལྟར་རྩ་ཡིས་གནད་ཀྱིས་ཀྱང༌། །\nསངས་རྒྱས་གནས་ནི་མཚོན་པའོ། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000719",
    "ordinal": 722,
    "golden": [
      "U01579",
      "U01580",
      "U01581",
      "U01582",
      "U01583"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ཡང་ན་མཁས་པས་གནད་ཉིད་བཙལ། །\nརྩ་ནས་ངེས་པར་འགྱུ་བ་ནི། །\nའབུམ་ཕྲག་གཅིག་དང་ཁྲི་ཕྲག་གཉིས། །\nསྟོང་ཕྲག་དྲུག་དང་བརྒྱ་ཕྲག་དྲུག །\nརྩ་ནས་ངེས་པར་འབྱུང་བ་སྟེ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000722",
    "ordinal": 725,
    "golden": [
      "U01587"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ཡི་གནད་ཀྱིས་སྦྱོར་ཐབས་འབད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000660",
    "ordinal": 663,
    "golden": [
      "U01440",
      "U01441"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "རང་ལོའི་འབྱུང་བ་བཅུད་པ་ལ། །\nགནས་སུ་ཕྱིན་པས་ངེས་པར་འགྲུབ། །",
    "before": "vitality",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Bcud occurs in the extraction/concentration sense, not the receptacle-and-inhabitants construction. Apply the approved label while keeping the already qualified taking/concentrating construction and its actual own-year or dream-practice scope."
  },
  {
    "pair": "DTG-000687",
    "ordinal": 690,
    "golden": [
      "U01499",
      "U01500",
      "U01501",
      "U01502",
      "U01503",
      "U01504"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "དེ་ནས་གནད་ལ་འབེབས་དུས་སུ། །\nསྦྱང་དང་བསྒྱུར་དང་བཅད་པ་དང༌། །\nདཀྲུགས་དང་བཅུད་དང་གནད་ལ་འབོར། །\nབསྐྱིལ་བཟློག་ལས་ཀྱི་གནད་བྱས་པས། །\nལས་ཀྱི་རྨི་ལམ་མཐའ་ཟད་དེ། །\nབག་ཆགས་འཁྲུལ་པ་དྲུང་ནས་ཐོན། །",
    "before": "vitality",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Bcud occurs in the extraction/concentration sense, not the receptacle-and-inhabitants construction. Apply the approved label while keeping the already qualified taking/concentrating construction and its actual own-year or dream-practice scope."
  },
  {
    "pair": "DTG-000661",
    "ordinal": 664,
    "golden": [
      "U01442",
      "U01443",
      "U01444",
      "U01445",
      "U01446"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "བཅུད་ཀྱིས་ལེན་པར་འདོད་པས་ནི། །\nབདུད་རྩི་རྣམ་ལྔ་སྦྱར་བའི་ཐབས། །\nགཞན་དུ་འབྱུང་བ་སྙོམས་པ་ལ། །\nམཁས་པས་ཆ་སྙོམས་ལེགས་སྦྱར་ནས། །\nརིན་པོ་ཆེ་ཡི་སྣོད་དུ་བླུགས། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Extend the confirmed bcud kyis len pa label repair to this actual nourishment construction. Retain the qualified whole phrase, skilled person, explicit materials, sequence and conspicuous editorial warning; no recipe or safety claim is added."
  },
  {
    "pair": "DTG-000663",
    "ordinal": 666,
    "golden": [
      "U01449",
      "U01450",
      "U01451",
      "U01452",
      "U01453"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "དངུལ་ཆུའི་ཐིགས་པ་རེ་བླངས་ནས། །\nནང་བཞིན་སྲན་མའི་རྡོག་མ་ཙམ། །\nམཁས་པ་དག་གིས་ཟ་སྤྱོད་ན། །\nབཅུད་ཀྱིས་ལེན་པ་ཆེན་པོར་ཡང་། །\nའགྱུར་བ་ཐེ་ཚོམ་མི་ཟའོ། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Extend the confirmed bcud kyis len pa label repair to this actual nourishment construction. Retain the qualified whole phrase, skilled person, explicit materials, sequence and conspicuous editorial warning; no recipe or safety claim is added."
  },
  {
    "pair": "DTG-000723",
    "ordinal": 726,
    "golden": [
      "U01588",
      "U01589"
    ],
    "family": "T04",
    "kind": "translation",
    "tibetan": "ཆེན་པོ་ལ་ནི་དུས་བརྩི་སྟེ། །\nམཆོག་དང་ཐུན་མོང་དངོས་གྲུབ་བརྟག །",
    "before": "supreme and common accomplishments",
    "after": "supreme and common spiritual accomplishments",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Preserve both supreme and common modifiers and the spiritual component of the complete dngos grub label. Do not apply the label to generic grub/sgrub or thob elsewhere in this range."
  },
  {
    "pair": "DTG-000740",
    "ordinal": 743,
    "golden": [
      "U01628",
      "U01629",
      "U01630",
      "U01631",
      "U01632",
      "U01633"
    ],
    "family": "T19",
    "kind": "translation",
    "tibetan": "དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །\nགཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ། །\nརེག་གི་ཁམས་ལ་བརྟགས་པ་ཡིས། །\nའཇིག་རྟེན་ཐུན་མོང་ལས་མཐའ་དང༌། །\nམངོན་པར་ཤེས་པ་རྫོགས་པ་དང་། །\nཞིང་ཁམས་རྣམས་ལ་ལོངས་སྤྱོད་དོ། །",
    "before": "the fields",
    "after": "the realms",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Zhing khams names realms enjoyed after the listed accomplishments; there is no operative material-field metaphor. Retain number and the distinct mngon par shes pa expression; this is not higher doctrine."
  },
  {
    "pair": "DTG-000654",
    "ordinal": 657,
    "golden": [
      "U01420",
      "U01421",
      "U01422",
      "U01423",
      "U01424"
    ],
    "family": "E04",
    "kind": "translation",
    "tibetan": "མཁའ་འགྲོ་དབང་དུ་སྡུད་པའི་མིས། །\nམ་མོ་འདུ་བའི་སར་ཕྱིན་ནས། །\nརིན་པོ་ཆེ་ཡི་སྦྱོར་བ་དག །\nའབྱུང་བའི་མགོ་ཉིད་འཚོགས་དུས་སུ། །\nལེགས་པར་སྦྱར་ཏེ་རི་ལུ་ཉིད། །",
    "before": "A person gathering ḍākinīs under his power,\nhaving gone to a place where mamos assemble,\na preparation of precious substances— [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\nat the time when the heads of the elements meet, [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\nproperly combines [them] into the pill itself. [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)",
    "after": "A person gathering ḍākinīs under his power,\nhaving gone to a place where mamos assemble,\nproperly combines a preparation of precious substances— [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\nat the time when the heads of the elements meet— [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\ninto the pill itself. [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Move the existing English verb before its object so the named person, not the preparation, is the grammatical actor. Keep the preparation-before-time order already corrected historically at U01422–U01423; do not recreate that transposition. Remove only the now-unneeded bracketed object pronoun, retaining the pill/result, every source component and all three note links. No ingredient or new operation is supplied."
  },
  {
    "pair": "DTG-000735",
    "ordinal": 738,
    "golden": [
      "U01617",
      "U01618"
    ],
    "family": "S12/T24",
    "kind": "translation",
    "tibetan": "ཉིན་མཚན་མེད་པར་གོམས་སྤྱོད་ན། །\nའདི་ཉིད་རྩོལ་བྲལ་མངོན་དུ་སྣང་། །",
    "before": "Engaging in familiarity without [distinguishing] day and night,",
    "after": "When one engages in familiarization without [distinguishing] day and night,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The source goms spyod na is the practitioner condition, whereas di nyid is the thing appearing in the following clause. Remove the dangling English participle that attaches engaging to that demonstrative; use the approved process form familiarization. Preserve the qualified day/night phrase, direct appearance and freedom from effort."
  },
  {
    "pair": "DTG-000706",
    "ordinal": 709,
    "golden": [
      "U01545",
      "U01546",
      "U01547"
    ],
    "family": "PD-Q06-01",
    "kind": "review-link",
    "tibetan": "བསོད་ནམས་ལས་ཀྱི་བྱེད་པའོ། །\nའགྲོ་བའི་བཀྲག་དང་གཟི་མདངས་བསྐྱེད། །\nམཆེད་ཅིང་སྡུད་པའི་ལས་ཀུན་བྱེད། །",
    "before": "It performs the activities of merit and karma;\nit generates beings' luster and splendor;\nit performs every activity of spreading and gathering.\n\nEarlier notes: [N-074](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-074).",
    "after": "It performs the activities of merit and karma;\nit generates beings' luster and splendor;\nit performs every activity of spreading and gathering.\n\nEarlier notes: [N-074](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-074).\n\nReview note: [Merit/karma construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q06-01).",
    "severity": "documentation",
    "confidence": "high for source scope and linkage",
    "rationale": "Link the exact unresolved construction and competing analyses without changing the main English or treating a component/substring match as proof of an error."
  },
  {
    "pair": "DTG-000740",
    "ordinal": 743,
    "golden": [
      "U01628",
      "U01629",
      "U01630",
      "U01631",
      "U01632",
      "U01633"
    ],
    "family": "PD-Q06-02",
    "kind": "review-link",
    "tibetan": "དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །\nགཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ། །\nརེག་གི་ཁམས་ལ་བརྟགས་པ་ཡིས། །\nའཇིག་རྟེན་ཐུན་མོང་ལས་མཐའ་དང༌། །\nམངོན་པར་ཤེས་པ་རྫོགས་པ་དང་། །\nཞིང་ཁམས་རྣམས་ལ་ལོངས་སྤྱོད་དོ། །",
    "before": "Through the culmination of activities examined in actuality,\nand through examining the domains of form, sound, smell, taste,\nand touch, [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03)\nthe culmination of common worldly activities\nand higher knowing are perfected,\nand one enjoys the realms.\n\nEarlier notes: [N-077](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-077), [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).",
    "after": "Through the culmination of activities examined in actuality,\nand through examining the domains of form, sound, smell, taste,\nand touch, [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03)\nthe culmination of common worldly activities\nand higher knowing are perfected,\nand one enjoys the realms.\n\nEarlier notes: [N-077](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-077), [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).\n\nReview note: [Bare dngos construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q06-02).",
    "severity": "documentation",
    "confidence": "high for source scope and linkage",
    "rationale": "Link the exact unresolved construction and competing analyses without changing the main English or treating a component/substring match as proof of an error."
  }
]
```

<a id="pd-q06-01"></a>
#### PD-Q06-01 — Merit and karma, or meritorious karma?

**DTG-000706 / U01545:** `བསོད་ནམས་ལས་ཀྱི་བྱེད་པའོ། །`. Current English: “It performs the activities of merit and karma.” Retain provisionally. The worldly-wind list supplies the acting wind, but bsod nams las may be a modifier-plus-karma expression (candidate “meritorious karma”) rather than two coordinate objects. Conversely, the absence of dang alone does not prove coordination impossible in a compressed list. No new conjunction or modifier analysis is imposed solely from a component lookup. An internal parallel with an explicit relationship, or authorized commentary on this nominal phrase, would settle it. **Severity:** medium possible modifier/coordination difference. **Confidence:** moderate that the construction needs qualification; no alternative is certified.

<a id="pd-q06-02"></a>
#### PD-Q06-02 — Nominal objects versus actuality

**DTG-000740 / U01628–U01633**, beginning `དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །`. Current English begins “Through the culmination of activities examined in actuality”. The following explicit examination of form/sound/smell/taste/touch domains supports testing the alternative “activities of examining entities”; the present wording instead takes dngos la as an actuality construction. The bare-form row expressly requires this analysis and permits actuality when justified. Retain the clause provisionally rather than treat la or an English substring as conclusive. A decisive parallel distinguishing objects examined from activities tested in actuality, or authorized commentary, would settle the attachment. The separate, explicit actual/nonactual transference contrast at DTG-000743–000746 is not automatically an entity contrast. **Severity:** medium possible object/modifier difference. **Confidence:** moderate for the unresolved boundary, high that an automatic entity substitution is not licensed.

<a id="phase-d-notes-06"></a>
**Active note/usage additions recorded before application:** The following narrow dispositions extend the existing index/usage history without rewriting old proposals or adding a canonical assignment.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T30",
    "pairs": [
      "DTG-000618"
    ],
    "ids": [
      "U01338",
      "U01339"
    ],
    "source": {
      "DTG-000618": "ཕུན་སུམ་ཚོགས་པ་དྲུག་ཅུ་ཡིས། །\nབསྟན་པ་དམ་པའི་གཞི་མ་འཛིན། །"
    },
    "realization": "foundation",
    "status": "Locally supported ordinary teaching-support construction under P1",
    "reason": "U01339 has now been read in the complete qualities account: the teacher upholds the teaching through sixty excellences. Foundation is retained locally, not changed to technical Ground or replaced with basis merely for uniformity. This extends only the earlier physical-foundation disposition to the separately evidenced teaching-support construction; no shared glossary reassignment results.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-066",
    "pairs": [
      "DTG-000627",
      "DTG-000628",
      "DTG-000629",
      "DTG-000630",
      "DTG-000631",
      "DTG-000632",
      "DTG-000633",
      "DTG-000634",
      "DTG-000635",
      "DTG-000636",
      "DTG-000637"
    ],
    "ids": [
      "U01354",
      "U01355",
      "U01356",
      "U01357",
      "U01358",
      "U01359",
      "U01360",
      "U01361",
      "U01362",
      "U01363",
      "U01364",
      "U01365",
      "U01366",
      "U01367",
      "U01368",
      "U01369",
      "U01370",
      "U01371",
      "U01372",
      "U01373",
      "U01374",
      "U01375",
      "U01376",
      "U01377",
      "U01378",
      "U01379",
      "U01380"
    ],
    "source": {
      "DTG-000627": " སྐུ་གསུམ་བསླབ་པའི་རིམ་པ་ཉིད། །\nའབྱུང་བའི་འདོད་དོན་གཙོར་བྱས་ཏེ། །\nམཆོག་ཏུ་ས་ཆུ་མེ་རླུང་གི། །\nསྒྲ་ལ་བསླབས་པས་ངེས་པར་འགྲུབ། །",
      "DTG-000628": "ཆུ་ཡི་སྒྲ་ནི་གཤང་བ་ལ། །\nམཁའ་འགྲོ་མ་ཡི་སྒྲ་དབྱངས་འཛིན། །",
      "DTG-000629": "འདི་ལ་རྟག་ཏུ་གོམས་བྱས་ན། །\nསྤྲུལ་པའི་སྐུ་ཡང་ངེས་པར་འགྲུབ། །",
      "DTG-000630": "ས་ཡི་སྒྲ་ནི་བསིལ་ཞིང་ལྗི། །\nཚངས་པ་ཆེན་པོའི་སྒྲ་སྐད་ལྡན། །",
      "DTG-000631": "འདི་ལ་རྟག་ཏུ་བརྟན་སྤྱོད་ན། །\nལོངས་སྤྱོད་རྫོགས་སྐུ་ངེས་འགྲུབ་པའོ། །",
      "DTG-000632": "མེ་ཡི་སྒྲ་ནི་རིང་བྱེད་བསླབ། །\nཁྱབ་འཇུག་ཆེན་པོའི་གསུང་དབྱངས་སྟོན། །",
      "DTG-000633": "འདི་ལ་མཉན་པར་སུས་སྤྱོད་པ། །\nཆོས་སྐུའི་ཡོན་ཏན་ངེས་པར་འཐོབ། །",
      "DTG-000634": "རླུང་གི་སྒྲ་ནི་གཟིར་ཞིང་དྲག །\nམཁའ་ལྡིང་རྒྱལ་པོའི་སྦྱོར་བ་གསུང་། །",
      "DTG-000635": "འདི་ནི་རྟག་ཏུ་ཟློ་ཤེས་ན། །\nསྐུ་གསུམ་ཐུན་མོང་བསླབ་བྱའོ། །",
      "DTG-000636": "དེ་ལྟར་འབྱུང་བཞིའི་སྒྲ་དོན་ནི། །\nཕྱི་ཡི་དུས་ལ་ངེས་པར་སྦྱོར། །\nདགུན་དང་དཔྱིད་དང་དབྱར་དང་སྟོན། །\nཆུ་དང་ས་སྟེ་མེ་རླུང་གི། །",
      "DTG-000637": "རིམ་པ་དུས་དང་ངེས་སྦྱར་ཏེ། །\nརྣལ་འབྱོར་ལུས་དང་བསྟུན་བྱས་ན། །\nའགྲུབ་པར་ཐེ་ཚོམ་མི་ཟའོ། །"
    },
    "realization": "sound; word and meaning",
    "status": "P1 acoustic exception adopted within the actual acoustic clauses",
    "reason": "The voice/melody, listening and elemental-sound clauses support sound. The complete sgra don expression at U01374 keeps word and meaning. The old proposed-exception status is historical. Gshang, lengtheners, the All-Pervader and sky-soarer designation/application remain qualified; no mantra or seasonal scheme is imported.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-068",
    "pairs": [
      "DTG-000654",
      "DTG-000660"
    ],
    "ids": [
      "U01420",
      "U01421",
      "U01422",
      "U01423",
      "U01424",
      "U01440",
      "U01441"
    ],
    "source": {
      "DTG-000654": "མཁའ་འགྲོ་དབང་དུ་སྡུད་པའི་མིས། །\nམ་མོ་འདུ་བའི་སར་ཕྱིན་ནས། །\nརིན་པོ་ཆེ་ཡི་སྦྱོར་བ་དག །\nའབྱུང་བའི་མགོ་ཉིད་འཚོགས་དུས་སུ། །\nལེགས་པར་སྦྱར་ཏེ་རི་ལུ་ཉིད། །",
      "DTG-000660": "རང་ལོའི་འབྱུང་བ་བཅུད་པ་ལ། །\nགནས་སུ་ཕྱིན་པས་ངེས་པར་འགྲུབ། །"
    },
    "realization": "grammatical combining clause; quintessence",
    "status": "Minimal English repair and approved component; whole ritual constructions provisional",
    "reason": "The preparation still precedes the time clause in source order; only the existing English verb is placed before its object. No old alignment error is reintroduced. Quintessence repairs the bcud component at U01440 without resolving its full own-year construction. Ingredient identities, absorbed/combined and A/ali alternatives, quantities and application referents stay qualified.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T16",
    "pairs": [
      "DTG-000661",
      "DTG-000663"
    ],
    "ids": [
      "U01442",
      "U01443",
      "U01444",
      "U01445",
      "U01446",
      "U01449",
      "U01450",
      "U01451",
      "U01452",
      "U01453"
    ],
    "source": {
      "DTG-000661": "བཅུད་ཀྱིས་ལེན་པར་འདོད་པས་ནི། །\nབདུད་རྩི་རྣམ་ལྔ་སྦྱར་བའི་ཐབས། །\nགཞན་དུ་འབྱུང་བ་སྙོམས་པ་ལ། །\nམཁས་པས་ཆ་སྙོམས་ལེགས་སྦྱར་ནས། །\nརིན་པོ་ཆེ་ཡི་སྣོད་དུ་བླུགས། །",
      "DTG-000663": "དངུལ་ཆུའི་ཐིགས་པ་རེ་བླངས་ནས། །\nནང་བཞིན་སྲན་མའི་རྡོག་མ་ཙམ། །\nམཁས་པ་དག་གིས་ཟ་སྤྱོད་ན། །\nབཅུད་ཀྱིས་ལེན་པ་ཆེན་པོར་ཡང་། །\nའགྱུར་བ་ཐེ་ཚོམ་མི་ཟའོ། །"
    },
    "realization": "taking nourishment from quintessence",
    "status": "Approved P2 component in further occurrences; whole construction provisional",
    "reason": "Extend the already recorded local nourishment treatment to U01442 and U01452. The old vital-essences variant is superseded only in these current clauses. The historical prescription remains explicitly editorially cautioned, and unidentified ingredients, objects and sequence are not reconstructed.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-072",
    "pairs": [
      "DTG-000685",
      "DTG-000686",
      "DTG-000687",
      "DTG-000688",
      "DTG-000689",
      "DTG-000690",
      "DTG-000691"
    ],
    "ids": [
      "U01493",
      "U01494",
      "U01495",
      "U01496",
      "U01497",
      "U01498",
      "U01499",
      "U01500",
      "U01501",
      "U01502",
      "U01503",
      "U01504",
      "U01505",
      "U01506",
      "U01507",
      "U01508",
      "U01509",
      "U01510",
      "U01511",
      "U01512",
      "U01513"
    ],
    "source": {
      "DTG-000685": "རྨི་ལམ་གནད་ཀྱི་ལམ་ཁྱེར་ནི། །\nསྔོན་དུ་བྱ་དང་གནད་ལ་དབབ། །",
      "DTG-000686": "སྔོན་དུ་ལུས་ངག་སེམས་སྦྱངས་ཏེ། །\nའབྱོངས་པའི་རྟགས་ལ་བརྟེན་ནས་ནི། །\nབརྟག་དང་ཟིལ་གྱིས་གནོན་པ་དང༌། །\nབག་ཆགས་གསུམ་པོ་ངེས་གཟུང་བྱ། །",
      "DTG-000687": "དེ་ནས་གནད་ལ་འབེབས་དུས་སུ། །\nསྦྱང་དང་བསྒྱུར་དང་བཅད་པ་དང༌། །\nདཀྲུགས་དང་བཅུད་དང་གནད་ལ་འབོར། །\nབསྐྱིལ་བཟློག་ལས་ཀྱི་གནད་བྱས་པས། །\nལས་ཀྱི་རྨི་ལམ་མཐའ་ཟད་དེ། །\nབག་ཆགས་འཁྲུལ་པ་དྲུང་ནས་ཐོན། །",
      "DTG-000688": "འདི་དུས་རང་གི་བརྩོན་འགྲུས་ཀྱིས། །\nརབ་ལ་ཆད་དང་འབྲིང་ལ་ཤེས། །\nཐ་མ་འགྱུར་བར་ངེས་པ་སྟེ། །",
      "DTG-000689": "འདི་དག་རྨི་ལམ་ཐོག་མ་ཡང༌། །\nརབ་ལ་བརྗེད་དང་ཐ་མ་འགགས། །\nའབྲིང་ལ་ཤིན་ཏུ་གསལ་བ་ལ། །\nཐ་མ་ཡིན་པ་ཤེས་པའོ། །",
      "DTG-000690": "ཐ་མ་མི་གསལ་དེ་ནས་འགྱུར། །",
      "DTG-000691": "དེ་རྣམས་ཀྱིས་ནི་ཚད་ལ་ཕེབ། །"
    },
    "realization": "key point; quintessence; habitual tendencies",
    "status": "Complete continuation read; approved components applied; graded relationships still provisional",
    "reason": "The full U01493–U01513 sequence has now been read together, not stopped at an old authoring-batch boundary. All actions, examination/overpowering/habitual-tendency triad and repeated inferior-grade statements are preserved. The already qualified concentrating construction takes quintessence; no new procedural definition or hierarchy is inferred.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T34",
    "pairs": [
      "DTG-000707"
    ],
    "ids": [
      "U01548",
      "U01549",
      "U01550",
      "U01551",
      "U01552",
      "U01553",
      "U01554",
      "U01555"
    ],
    "source": {
      "DTG-000707": "འདས་པའི་སྐུ་དང་ཡེ་ཤེས་དང༌། །\nཐིག་ལེ་ཉིད་ལ་གོམས་པ་དང༌། །\nཡང་ཞིང་སྟོང་དང་གསལ་བར་ཁྱབ། །\nལུས་ཀྱི་འབྱུང་བ་ཟད་པ་དང་། །\nསེམས་ཀྱི་རྟོག་པ་འགགས་པ་དང༌། །\nམི་རྟོག་ཡེ་ཤེས་སྐྱེ་བ་དང༌། །\nཕྱི་ཡི་སྣང་བ་ཟད་པ་དང༌། །\nརླུང་སེམས་གཉིས་སུ་འདྲེས་པ་སྟེ། །"
    },
    "realization": "wind and ordinary mind, the two",
    "status": "Supported local two-member analysis; not a replacement for canonical wind-mind",
    "reason": "The explicit gnyis and mixing construction support retaining both separately named members in this clause. Their precise gnyis su relation remains qualified; no merging into one or nondual result is supplied. This does not authorize splitting the established wind-mind expression in other constructions.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-071",
    "pairs": [
      "DTG-000676",
      "DTG-000677",
      "DTG-000678",
      "DTG-000679",
      "DTG-000680",
      "DTG-000681",
      "DTG-000682",
      "DTG-000683",
      "DTG-000684"
    ],
    "ids": [
      "U01477",
      "U01478",
      "U01479",
      "U01480",
      "U01481",
      "U01482",
      "U01483",
      "U01484",
      "U01485",
      "U01486",
      "U01487",
      "U01488",
      "U01489",
      "U01490",
      "U01491",
      "U01492"
    ],
    "source": {
      "DTG-000676": " གཉིད་ཀྱི་རྣལ་འབྱོར་སུས་བསྒོམ་པ། །\nའདིས་ནི་གཏི་མུག་ལམ་དུ་བྱེད། །",
      "DTG-000677": "ཕྱི་ཡི་དུས་ནི་གཞི་དག་ལས། །\nརྣལ་འབྱོར་ལུས་ཀྱི་རྩལ་སྦྱངས་ཏེ། །",
      "DTG-000678": "རྩ་རྣམས་ཁུངས་སུ་བཟུང་བ་གནད། །",
      "DTG-000679": "ནང་གི་དུས་ནི་བཞི་ཉིད་ཀྱིས། །\nརྣལ་འབྱོར་དག་གི་རྩལ་སྦྱངས་ཏེ། །",
      "DTG-000680": "བརྗོད་པའི་རྒྱུན་རྣམས་གཅད་པ་གནད། །",
      "DTG-000681": "གསང་བའི་དུས་ནི་བཞི་ཡིས་ཀྱང་། །\nརྣལ་འབྱོར་སེམས་ཀྱི་རྩལ་སྦྱངས་ཏེ། །",
      "DTG-000682": "གཉིད་ལ་གོམས་པ་གནད་ཡིན་ནོ། །",
      "DTG-000683": "ཁོ་ན་ཉིད་ཀྱི་དུས་བཞི་ཡིས། །\nལུས་དང་ངག་སེམས་ངེས་བསྡུས་ནས། །\nའོད་གསལ་ཆེན་པོ་གཉིད་དང་བསྲེ། །",
      "DTG-000684": "དེ་ལྟར་གོམས་ནས་སྐུ་གསུམ་ལ། །\nངེས་པར་སྦྱོར་རོ་རྣལ་འབྱོར་པས། །"
    },
    "realization": "key point; dull confusion and suchness retained provisionally",
    "status": "Approved gnad labels; shared-control family questions remain open",
    "reason": "The current fixed reading gzhi dag is not silently changed to bzhi/four. Technical Ground versus an ordinary basis and dag attachment remain provisional at U01479. Gti mug and kho na nyid remain unapproved whole labels; gti mug will be compared with rmongs/rmugs and the affliction lists, preserving ignorance, delusion and technical dullness. The separate body/yoga/ordinary-mind expressiveness and clear-light/sleep mixing remain visible.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-076",
    "pairs": [
      "DTG-000727",
      "DTG-000728",
      "DTG-000730",
      "DTG-000733",
      "DTG-000735"
    ],
    "ids": [
      "U01597",
      "U01598",
      "U01599",
      "U01600",
      "U01601",
      "U01602",
      "U01603",
      "U01604",
      "U01605",
      "U01608",
      "U01609",
      "U01610",
      "U01613",
      "U01614",
      "U01617",
      "U01618"
    ],
    "source": {
      "DTG-000727": "ཐིག་ལེའི་ཆོས་ཉིད་བརྟན་འདོད་པས། །\nདོན་དམ་དང་ནི་ཀུན་རྫོབ་ལས། །",
      "DTG-000728": "རེ་ཞིག་ཀུན་རྫོབ་ཐིག་ལེ་ལ། །\nབརྟེན་ནས་སངས་རྒྱས་འདོད་པ་ཡིས། །\nརིགས་མ་མཚན་ཉིད་རྫོགས་པ་ནི། །\nལྷ་དང་ལྷ་མིན་ཚངས་པ་དང༌། །\nགལ་ཏེ་རིགས་ངན་མུ་སྟེགས་སམ། །\n མཚན་ཉིད་རྫོགས་པ་དག་མཐོང་ན། །\nའགུགས་པའི་སྦྱོར་བ་ངེས་བརྩམས་ནས། །",
      "DTG-000730": "དེ་ནས་ཀུན་རྫོབ་ཐིག་ལེ་ཉིད། །\nདབབ་ཅིང་གཟུང་དང་བཟློག་པ་དང༌། །\nརྩ་ལ་གདབ་ཅིང་རླུང་དང་བསྲེ། །",
      "DTG-000733": "དོན་དམ་ཐིག་ལེ་བརྟན་པ་ཡིས། །\nཆོས་སྐུ་སྟོང་པའི་ཡུལ་རྣམས་རྙེད། །",
      "DTG-000735": "ཉིན་མཚན་མེད་པར་གོམས་སྤྱོད་ན། །\nའདི་ཉིད་རྩོལ་བྲལ་མངོན་དུ་སྣང་། །"
    },
    "realization": "relative/ultimate spheres retained provisionally; familiarization",
    "status": "P3 paired-label evaluation pending shared assignment; local condition repaired",
    "reason": "The owner-preferred superficial/superfactual pair was tested together against the sphere distinction: the former is linked to the woman/channels/wind sequence, the latter to empty dharma-embodiment domains and the canonical lamp of the empty sphere. This supports a paired proposal but does not settle the physical/visionary scope or authorize a new shared default. Retain current relative/ultimate provisionally; do not apply either proposal to mthar thug or generic English adjectives. The full characteristics repetition, family-woman qualification, caste wording as source language, and unspecified techniques remain intact. At U01617 only the practitioner condition/process is repaired, not its appearing object.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-077",
    "pairs": [
      "DTG-000740",
      "DTG-000742",
      "DTG-000743",
      "DTG-000744",
      "DTG-000745",
      "DTG-000746",
      "DTG-000747"
    ],
    "ids": [
      "U01628",
      "U01629",
      "U01630",
      "U01631",
      "U01632",
      "U01633",
      "U01635",
      "U01636",
      "U01637",
      "U01638",
      "U01639",
      "U01640",
      "U01641",
      "U01642",
      "U01643",
      "U01644",
      "U01645",
      "U01646",
      "U01647"
    ],
    "source": {
      "DTG-000740": "དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །\nགཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ། །\nརེག་གི་ཁམས་ལ་བརྟགས་པ་ཡིས། །\nའཇིག་རྟེན་ཐུན་མོང་ལས་མཐའ་དང༌། །\nམངོན་པར་ཤེས་པ་རྫོགས་པ་དང་། །\nཞིང་ཁམས་རྣམས་ལ་ལོངས་སྤྱོད་དོ། །",
      "DTG-000742": "འཕོ་བའི་བྱེ་བྲག་རྣམ་པ་གསུམ། །\nདབང་པོ་དག་གི་དབྱེ་བ་ཡིས། །\nའོད་གསལ་བ་དང་སྒྱུ་ལུས་དང༌། །\nཐ་མ་ལུས་ངག་ཡིད་ལའོ། །",
      "DTG-000743": "ལུས་ངག་འཕོ་བ་རྣམ་པ་གཉིས། །\nདངོས་སུ་འཕོ་དང་དངོས་མེད་དོ། །",
      "DTG-000744": "དངོས་ནི་རླུང་གིས་སྦྱང་བའི་ཐབས། །",
      "DTG-000745": "སྒྲ་དང་བཟོ་དང་སྒྱུ་རྩལ་དང་། །\nརྟེན་ཅིང་འབྲེལ་ལ་སྦྱངས་པས་ནི། །\nསོ་སོའི་འབྱུང་བ་ནང་མཐུན་པས། །\nལུས་ངག་ཡིད་ཀྱིས་གཏད་པས་འགྲུབ། །",
      "DTG-000746": "དངོས་མེད་སེམས་ཀྱི་གོམས་སྟོབས་བརྟན། །",
      "DTG-000747": "སྒྱུ་ལུས་རྨི་ལམ་དག་ལ་སྦྱངས། །"
    },
    "realization": "realms; actuality construction provisional; actual/nonactual transference",
    "status": "Approved realm label; separate bare-form and whole-expression questions retained",
    "reason": "Dngos la at U01628 is now linked as a nominal-objects versus actuality construction question. Do not force it to entity from the spelling alone. The explicit actual/nonactual transference contrast and method-versus-ordinary-mind-familiarity explanation support retaining those contextual adjective senses at U01639–U01646. Transference, word/craft/illusory-expressiveness and the dream/illusory-body scope remain provisional whole-expression treatments; the ensuing intermediate-state continuation is read as context, not yet added to this batch coverage.",
    "review": "REVIEW.md#phase-d-notes-06"
  }
]
```

**Justified retentions and rejected false positives:** The explicit acoustic passages retain sound while the complete word-and-meaning expression is preserved. The four season/element correspondences, cool/heavy and pressing/fierce descriptions, and unidentified designations are not made more familiar. General accomplishment/attainment verbs are not turned into spiritual accomplishment. All explicit speech/ordinary-mind/mental-faculty distinctions, the main-practice compound and nonliterary personal continuum remain intact. The force of methods is procedural in the local applications; it is not changed merely to conform to a book-wide preference for means.

The actual fixed gzhi dag reading in the sleep passage remains separate from the tempting four-reading. The complete preparatory and operative dream lists were read through their repeated inferior-grade results; none is deleted or reassigned to produce an elegant hierarchy. Habitual tendencies is the unchanged established label, not imprints. The distinct source wind/ordinary-mind two-member wording does not erase wind-mind elsewhere. The eight channel operations retain their individual verbs and qualified objects, and the two counts remain 21,600 and 126,600 without an added daily interval. The lamp of the empty sphere is an established complete expression, not a fresh assembly of components.

The visible N-069 editorial warning is retained as editorial, not attributed to the Tibetan. No ingredient identity, dose conversion, anatomical location, missing characteristic, procedure, medical efficacy or ritual efficacy is supplied. The current main/variant separation at U01414/01417/01422/01439/01567 is already correct; the historical transposition and merged-annotation criticisms are not reused as current defects. N-076's bracketed her refers to the already qualified woman; its compressed characteristics construction is not rewritten merely because a fuller paraphrase is easier to read. Its physical/visionary scope and proposed family-woman label remain open. The P3 superficial/superfactual test remains a paired, source-scoped shared-label proposal, not an activated default or a blanket replacement for English relative/ultimate.

**Application, changed-clause self-check and validation:** All 21 English operations in 20 pairs and both construction-question links were applied and rechecked in a 53-pair changed-clause/context view against the complete Tibetan clauses. The direct-perception emphasis, combining agent/object, source-order preparation/time relationship and practitioner condition were checked explicitly. Number, negation, possessors, qualifications, distinct technical components and the editorial safety warning remain intact. All nine scoped note/usage additions preserve the inherited records. This is repair self-verification, not another independent review.

The final paired validator and projector check were rerun; both still exit 1 at the historical protected-glossary contract. The full recorded-operation replay/integrity check passes all 2,667 pairs, fixed source/golden/policy/format/lineage, inherited note associations/history and 700 English local-link targets. Current totals are 152 operations: 131 English repairs in 121 distinct pairs and 21 review links, affecting 133 pair payloads including note-only changes, plus the previously recorded separate annotation repair. The usage file now has 34 Phase D dispositions, with all 25 inherited from the preceding commit unchanged. English SHA-256: `5f9bc5bf9897eecb087f6c35ba890bd549a28726e60b54e571205623712d08bf`. `git diff --check` passes. No dependent reader was produced by the blocked projector.

**Saved coverage:** 750/2,667 pairs, ordinals 1–750 through DTG-000747, with 195 first-encountered note records. Continue at ordinal 751 / DTG-000748. Ordinals 751–760 have additionally been read as connected context, not counted as completed coverage. Text remains provisional and the whole-work pass is still in progress.

<a id="phase-d-batch-07"></a>
### Batch 07 — source ordinals 751–950

All 200 current pairs DTG-000748–000947 were read in source order with all 43 first-encountered note records, using the same current-source/full-note-prose view described above. Ordinals 951–965 were also read as connected context, including completion of N-093; they are not yet added to completed coverage. Q1–Q9, I §8.1 and III were applied, and the complete eight-column rows for the affected terminology and rejected substring matches were rechecked.

**Findings recorded before application:** 32 English operations in 28 pairs are specified below. Existing family rationales extend only to the actual matching complete expressions. The ordinary-basis reading is supported by the connected vehicle classification, not by a blanket removal of capital Ground. The agent/possessive/condition repairs preserve the same practitioner and do not add a new causal mechanism, actor, sex, count or temporal unit. P3 candidates remain source-scoped proposals rather than newly activated shared labels.

<!-- phase-d-batch-07-operations -->
```json
[
  {
    "pair": "DTG-000754",
    "ordinal": 757,
    "golden": [
      "U01662",
      "U01663",
      "U01664"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རྟེན་འབྲེལ་སྦྱོར་བ་རྣམ་པ་གཉིས། །\nསྣ་ཚོགས་རྫུ་འཕྲུལ་བསྒྲུབ་པ་དང་། །\nའབྱུང་བ་གནད་ཀྱི་ཆོ་གའོ། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000760",
    "ordinal": 763,
    "golden": [
      "U01670",
      "U01671"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "འབྱུང་བའི་གནད་ནི་རང་དང་གཞན། །\nཕན་གནོད་འབྲས་བུ་ངེས་པར་འབྱིན། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000770",
    "ordinal": 773,
    "golden": [
      "U01694",
      "U01695",
      "U01696"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "བྱ་བ་དག་ནི་གསུམ་ཡིན་ཏེ། །\nལུས་ཀྱི་གནད་དང་ངག་དང་ཡང༌། །\nདེ་བཞིན་སེམས་ཀྱི་གནས་ཀྱིས་དགྲོལ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000787",
    "ordinal": 790,
    "golden": [
      "U01752",
      "U01753",
      "U01754",
      "U01755",
      "U01756",
      "U01757"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གནད་ཀྱི་འབྱུང་བ་རྣམ་ཕྱེ་ན། །\nབཞི་བརྒྱ་ཉིད་དང་རྩ་བཞི་ལས། །\nངེས་བཅས་འཇུག་པ་བརྒྱད་ཅུར་སྡུད། །\nདེ་ལས་ཉི་ཤུ་རྩ་བཞིའོ། །\nམཆོག་ཏུ་གནས་པ་བཅུ་དྲུག་ཉིད། །\nཕོ་མོའི་སྡེབས་ཀྱིས་བརྒྱད་དུ་འགྱུར། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000788",
    "ordinal": 791,
    "golden": [
      "U01758",
      "U01759"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རང་ངོ་དག་པ་བཞི་ཡིས་ནི། །\nགནད་རྣམས་བསྡུས་ཏེ་ངེས་པར་བསྟན། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000789",
    "ordinal": 792,
    "golden": [
      "U01760",
      "U01761",
      "U01762",
      "U01763"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "བྱེར་ཟུག་སྙོམས་པའི་བྱེད་ལས་ཀྱི། །\nཚེས་དང་ཟླ་བ་ལོ་རྣམས་དང་། །\nའཁྲུལ་པ་མེད་པར་སྦྱར་བྱས་ན། །\nགནད་རྣམས་དག་ཀྱང་ངེས་པར་འགྱུར། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000791",
    "ordinal": 794,
    "golden": [
      "U01765",
      "U01766"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": " དེ་ལྟར་གནད་ལ་བརྟེན་ནས་ནི། །\nརྩིས་ཀྱི་སྦྱོར་བའི་ཡན་ལག་བཤད། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000857",
    "ordinal": 860,
    "golden": [
      "U01920",
      "U01921",
      "U01922"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རྟེན་འབྲེལ་ཆོ་ག་རྫོགས་པ་ཡིས། །\nགནད་ཀྱི་སྤོ་ལ་གཏང་ཐབས་དང་། །\nསྐད་ཀྱི་བརྗོད་པ་ལས་ཤེས་བྱ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000877",
    "ordinal": 880,
    "golden": [
      "U01969",
      "U01970"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རྒྱུད་གཞན་ཀུན་ལས་མ་བཤད་པའི། །\nའབྱུང་བའི་གནད་རྣམས་དྲང་དང་བཟློག །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000887",
    "ordinal": 890,
    "golden": [
      "U01992"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "བཟློག་པ་དབང་པོའི་གནད་ཀྱིས་སོ། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000898",
    "ordinal": 901,
    "golden": [
      "U02013",
      "U02014",
      "U02015"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དབང་པོ་ཅིག་ཆར་རང་གྲོལ་བས། །\nམངོན་སུམ་མཐོང་བའི་གནད་ཀྱིས་ནི། །\nརང་གི་གྲུབ་པའི་མཐའ་ཞིག་ནས། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved gnad label at this actually read occurrence; retain its bodily, elemental, calculation or direct-perception scope, number, operations and connected qualifications."
  },
  {
    "pair": "DTG-000793",
    "ordinal": 796,
    "golden": [
      "U01768",
      "U01769",
      "U01770",
      "U01771"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "སངས་རྒྱས་གཞན་གྱིས་མ་གསུངས་པའི། །\nའབྱུང་བའི་རྩིས་ཀྱི་རིམ་པ་ལ། །\nབརྟེན་ནས་འཁོར་འདས་འཇལ་བྱེད་པའི། །\nརབ་ཏུ་གསང་བ་འདི་ཉོན་ཅིག །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved khor das coordinated expression, not an assembly inferred from unrelated khor/da s forms. Preserve both members and the measuring relation, as well as the already corrected source-order alignment."
  },
  {
    "pair": "DTG-000831",
    "ordinal": 834,
    "golden": [
      "U01861",
      "U01862",
      "U01863"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "མཆོག་ཏུ་སྐལ་ལྡན་བརྩོན་འགྲུས་ཅན། །\nའཁོར་བའི་ཡིད་དང་བྲལ་བ་ཡིས། །\nབླ་མ་མཆོད་དང་བསྟོད་བྱ་སྟེ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved khor ba noun while preserving the mental-faculty qualifier or three-realm support negation and the space-into-space simile."
  },
  {
    "pair": "DTG-000899",
    "ordinal": 902,
    "golden": [
      "U02016",
      "U02017",
      "U02018",
      "U02019",
      "U02020"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "གང་ལ་ཞེན་དང་འཛིན་མེད་པར། །\nཡང་དག་ཆོས་ཉིད་རོ་མྱངས་ནས། །\nཁམས་གསུམ་འཁོར་བའི་རྟེན་མེད་པར། །\nམཁའ་ལ་མཁའ་ཉིད་ཐིམ་པ་ལྟར། །\nརྣལ་འབྱོར་མཆོག་ཀྱང་དེ་བཞིན་ནོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved khor ba noun while preserving the mental-faculty qualifier or three-realm support negation and the space-into-space simile."
  },
  {
    "pair": "DTG-000839",
    "ordinal": 842,
    "golden": [
      "U01880",
      "U01881",
      "U01882",
      "A2000-C01-S02",
      "U01883",
      "U01884"
    ],
    "family": "E01",
    "kind": "translation",
    "tibetan": "དེ་ལྟར་ཕྱི་རོལ་འབྱུང་བ་ལ། །\nབརྩོན་འགྲུས་རབ་དང་འབྲིང་མཐའ་ཡི། །\nཞག་དང་ཟླ་བ་ལོ་རྣམས་ཀྱིས། །\nསོ་སོའི་ཚད་ལ་རྟགས་ཀྱིས་འགྲུབ། །\nའདི་ལྟར་སྐུ་ཡི་འགྲུབ་པ་ལ། །\nསྤྲུལ་པའི་སྐུ་དང་ལོངས་སྐུ་དང་། །\nཆོས་སྐུ་ངོ་བོ་ཉིད་ཀྱི་སྐུ། །\nམཆོག་ཏུ་སྐུ་ཡི་འབྲས་བུར་སྦྱོར། །",
    "before": "At their respective measures",
    "after": "at their respective measures",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Remove a mid-sentence capital introduced at a former unit/restoration boundary. The phrase continues the preceding comma or dash, not a new sentence. No Tibetan order, verse line, source annotation or clause content is changed."
  },
  {
    "pair": "DTG-000857",
    "ordinal": 860,
    "golden": [
      "U01920",
      "U01921",
      "U01922"
    ],
    "family": "E01",
    "kind": "translation",
    "tibetan": "རྟེན་འབྲེལ་ཆོ་ག་རྫོགས་པ་ཡིས། །\nགནད་ཀྱི་སྤོ་ལ་གཏང་ཐབས་དང་། །\nསྐད་ཀྱི་བརྗོད་པ་ལས་ཤེས་བྱ། །",
    "before": "For transferring",
    "after": "for transferring",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Remove a mid-sentence capital introduced at a former unit/restoration boundary. The phrase continues the preceding comma or dash, not a new sentence. No Tibetan order, verse line, source annotation or clause content is changed."
  },
  {
    "pair": "DTG-000893",
    "ordinal": 896,
    "golden": [
      "A2000-C01-S03",
      "U02006"
    ],
    "family": "E01",
    "kind": "translation",
    "tibetan": "གཞི་ནི་འཇིག་རྟེན་པ་ཡིན་ཏེ། །\nའདི་ལས་འདོད་པ་གཉིས་ཡིན་ནོ། །\nའདས་པ་རྒྱུ་དང་འབྲས་བུ་ལས། །\nརྒྱུ་ལ་གསུམ་ལ་འབྲས་བུར་གཉིས། །",
    "before": "For the cause",
    "after": "for the cause",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Remove a mid-sentence capital introduced at a former unit/restoration boundary. The phrase continues the preceding comma or dash, not a new sentence. No Tibetan order, verse line, source annotation or clause content is changed."
  },
  {
    "pair": "DTG-000941",
    "ordinal": 944,
    "golden": [
      "U02111",
      "U02112",
      "U02113",
      "U02114",
      "U02115"
    ],
    "family": "E01",
    "kind": "translation",
    "tibetan": "འཁོར་ལོའི་ལས་རྣམས་རྫོགས་བྱས་ཏེ། །\nཆོ་གའི་དགོངས་པ་ཚང་བ་ལས། །\nཅི་ལྟར་མོས་པའི་ཡི་གེ་ནི། །\nཁ་དོག་ངེས་པར་བསམ་བྱས་ཏེ། །\nགཤིན་རྗེའི་གཤེད་ཀྱི་རྣལ་འབྱོར་བྱའོ། །",
    "before": "Whichever letters",
    "after": "whichever letters",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Remove a mid-sentence capital introduced at a former unit/restoration boundary. The phrase continues the preceding comma or dash, not a new sentence. No Tibetan order, verse line, source annotation or clause content is changed."
  },
  {
    "pair": "DTG-000860",
    "ordinal": 863,
    "golden": [
      "U01927",
      "U01928"
    ],
    "family": "T04",
    "kind": "translation",
    "tibetan": "འོན་ཏེ་དངོས་གྲུབ་ལ་ཐུག་ན། །\nམི་སྣང་གཟུགས་ཀྱིས་ལུས་ཀུན་འགྲུབ། །",
    "before": "when accomplishment is reached",
    "after": "when spiritual accomplishment is reached",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual source has the complete dngos grub expression. Retain its spiritual component and all modifiers/participants. Do not change the separately expressed generic accomplishing/result verbs or practices of accomplishment in the same passage."
  },
  {
    "pair": "DTG-000919",
    "ordinal": 922,
    "golden": [
      "U02064",
      "U02065"
    ],
    "family": "T04",
    "kind": "translation",
    "tibetan": "ཡེ་ཤེས་དབང་བསྐུར་གྱིས་བརྒྱན་ཏེ། །\nདངོས་གྲུབ་འདོད་པས་རྟག་ཏུ་བསྒོམ། །",
    "before": "desiring accomplishment",
    "after": "desiring spiritual accomplishment",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual source has the complete dngos grub expression. Retain its spiritual component and all modifiers/participants. Do not change the separately expressed generic accomplishing/result verbs or practices of accomplishment in the same passage."
  },
  {
    "pair": "DTG-000923",
    "ordinal": 926,
    "golden": [
      "U02074",
      "U02075"
    ],
    "family": "T04",
    "kind": "translation",
    "tibetan": "དངོས་གྲུབ་སྟོན་པའི་འོད་ཟེར་ཅན། །\nའདི་ལ་བསྒྲུབ་པ་གསུམ་དུ་འགྱུར། །",
    "before": "reveals accomplishments",
    "after": "reveals spiritual accomplishments",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual source has the complete dngos grub expression. Retain its spiritual component and all modifiers/participants. Do not change the separately expressed generic accomplishing/result verbs or practices of accomplishment in the same passage."
  },
  {
    "pair": "DTG-000869",
    "ordinal": 872,
    "golden": [
      "U01945",
      "U01946",
      "U01947",
      "U01948"
    ],
    "family": "T10",
    "kind": "translation",
    "tibetan": "བེམ་པོའི་འབྱུང་བ་བཞི་དག་ལས། །\nདངོས་པོ་འགྱུར་བའི་རྟེན་འབྲེལ་གྱིས། །\nགྲངས་དང་བརྡའ་དང་སྐད་དག་གིས། །\nདམིགས་པ་བསྐྱུར་ཏེ་ནད་སོགས་སྤོ། །",
    "before": "insentient matter",
    "after": "matter",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 explicitly supersedes insentient matter for bem po. Preserve the four elements, their contrast with the preceding living beings, the distinct entities clause and all subsequent objects/actions. No entity/body/substance is relabeled from an English substring match."
  },
  {
    "pair": "DTG-000877",
    "ordinal": 880,
    "golden": [
      "U01969",
      "U01970"
    ],
    "family": "T01",
    "kind": "translation",
    "tibetan": "རྒྱུད་གཞན་ཀུན་ལས་མ་བཤད་པའི། །\nའབྱུང་བའི་གནད་རྣམས་དྲང་དང་བཟློག །",
    "before": "any other continuum",
    "after": "any other tantra",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Rgyud g zhan kun las ma bshad explicitly compares where this teaching has not been explained; with the following promise to explain, it denotes tantric scripture, activating the approved literary-use exception."
  },
  {
    "pair": "DTG-000883",
    "ordinal": 886,
    "golden": [
      "U01982",
      "U01983",
      "U01984"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "ལུས་ཀྱིས་འཁྲུལ་འཁོར་སྣ་ཚོགས་དང༌། །\nབཅུད་ཀྱིས་གཅུན་པའི་ལས་མཐའ་ཡིས། །\nའབྱུང་བའི་ནད་ཀུན་ཕྱིར་ལ་དྲངས། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply bcud in its concentrated/nourishing bodily application, distinct from a receptacle-and-inhabitants construction. Retain the different g cun/restraint verb and the whole technique as provisionally described, not equated with the earlier len pa nourishment construction."
  },
  {
    "pair": "DTG-000892",
    "ordinal": 895,
    "golden": [
      "U02003",
      "U02004",
      "U02005"
    ],
    "family": "S06",
    "kind": "translation",
    "tibetan": "སོ་སོའི་གཞི་དང་དབང་པོ་ཡིས། །\nའཇིག་རྟེན་པ་དང་འདས་པ་ཡི། །\nཐེག་པ་དག་ནི་གཉིས་སུ་འདོད། །",
    "before": "respective Grounds and faculties",
    "after": "respective bases and faculties",
    "severity": "medium",
    "confidence": "moderate-high",
    "rationale": "The connected tenet-system account classifies vehicles by their respective supporting bases and faculties; its worldly/transcendent, cause/result and three/two/six/nine distinctions are not a technical primordial-Ground assertion. Apply ordinary basis locally under P1 without settling the two-assertion referents."
  },
  {
    "pair": "DTG-000893",
    "ordinal": 896,
    "golden": [
      "A2000-C01-S03",
      "U02006"
    ],
    "family": "S06",
    "kind": "translation",
    "tibetan": "གཞི་ནི་འཇིག་རྟེན་པ་ཡིན་ཏེ། །\nའདི་ལས་འདོད་པ་གཉིས་ཡིན་ནོ། །\nའདས་པ་རྒྱུ་དང་འབྲས་བུ་ལས། །\nརྒྱུ་ལ་གསུམ་ལ་འབྲས་བུར་གཉིས། །",
    "before": "The Ground is worldly",
    "after": "The basis is worldly",
    "severity": "medium",
    "confidence": "moderate-high",
    "rationale": "The restored opening continues the classificatory basis/faculty account at DTG-000892. Retain its worldly predicate and every following number/contrast, but do not capitalize an ordinary basis into the technical Ground. The former source-reconciliation instruction to retain Ground is a historical lexical treatment, not a later owner-approved exception to P1."
  },
  {
    "pair": "DTG-000873",
    "ordinal": 876,
    "golden": [
      "U01960",
      "U01961",
      "U01962"
    ],
    "family": "E05",
    "kind": "translation",
    "tibetan": "འགུགས་པའི་ཕྱག་རྒྱ་ལྡན་པ་ཡིས། །\nསེར་སྣས་བཅིངས་པའི་ཟས་ནོར་ལ། །\nབླ་མ་མཆོད་ཕྱིར་སྤོ་བས་བླང༌། །",
    "before": "Possessing the gesture of summoning,",
    "after": "By one possessing the gesture of summoning,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Ldan pa yis supplies the qualified agent of taking, not a property of the following food and wealth. Make the passive agent explicit without changing the objects, manner, purpose, restrictive following condition or adding an actor absent from the practitioner sequence."
  },
  {
    "pair": "DTG-000922",
    "ordinal": 925,
    "golden": [
      "U02069",
      "U02070",
      "U02071",
      "U02072",
      "U02073"
    ],
    "family": "S12/T24",
    "kind": "translation",
    "tibetan": "སླར་གསོ་ཡེ་ཤེས་ལུས་ཀྱིས་ནི། །\nཡང་ནས་ཡང་དུ་གོམས་སྤྱོད་ན། །\nདྲུག་དང་བདུན་དང་དགུ་སྟེ་གཅིག །\nགཉིས་དང་གསུམ་དང་ལྔ་ཡིས་ནི། །\nགདོན་མི་ཟ་བར་འགྲུབ་པའོ། །",
    "before": "repeatedly engaging in familiarity,",
    "after": "when you repeatedly engage in familiarization,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Goms spyod na is an explicit practitioner condition, not a participle modifying the following absence of doubt. Preserve the preceding Restore instruction and its addressee, use the approved process form, and leave the exact seven numbers and their unexpressed counting unit unchanged."
  },
  {
    "pair": "DTG-000929",
    "ordinal": 932,
    "golden": [
      "U02086",
      "U02087",
      "U02088",
      "U02089"
    ],
    "family": "S12",
    "kind": "translation",
    "tibetan": "དེ་ལྟར་རྟག་ཏུ་བསྒོམ་པ་འམ། །\nཡང་ན་ཐུན་དྲུག་རྒྱུན་བརྟེན་ན། །\nདགུ་དང་བདུན་དང་ལྔ་ཡིས་ནི། །\nངེས་པར་འགྲུབ་པར་གདོན་མི་ཟའོ། །",
    "before": "Continually cultivating in this way,\nor relying continuously on six sessions,",
    "after": "When you continually cultivate in this way,\nor rely continuously on six sessions,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The pa am/yang na ... na construction gives two alternatives under a practitioner condition. State that condition without letting the English participle modify the following absence of doubt; preserve cultivation as distinct from familiarization, both alternatives, six sessions and nine/seven/five."
  },
  {
    "pair": "DTG-000932",
    "ordinal": 935,
    "golden": [
      "U02094",
      "U02095"
    ],
    "family": "E06",
    "kind": "translation",
    "tibetan": "ཆོ་ག་ལྡན་པའི་རྣལ་འབྱོར་པས། །\nརང་སེམས་དག་པ་གནས་བསམས་ཏེ། །",
    "before": "imagines one's own ordinary mind",
    "after": "imagines their own ordinary mind",
    "severity": "minor",
    "confidence": "high",
    "rationale": "The explicit grammatical subject is the yogin endowed with the rite, and rang sems is that same subject's own ordinary mind. Replace the mismatched generic one's with a coreferential, gender-neutral possessive; no new owner, gender or mental faculty is introduced."
  },
  {
    "pair": "DTG-000941",
    "ordinal": 944,
    "golden": [
      "U02111",
      "U02112",
      "U02113",
      "U02114",
      "U02115"
    ],
    "family": "E02",
    "kind": "translation",
    "tibetan": "འཁོར་ལོའི་ལས་རྣམས་རྫོགས་བྱས་ཏེ། །\nཆོ་གའི་དགོངས་པ་ཚང་བ་ལས། །\nཅི་ལྟར་མོས་པའི་ཡི་གེ་ནི། །\nཁ་དོག་ངེས་པར་བསམ་བྱས་ཏེ། །\nགཤིན་རྗེའི་གཤེད་ཀྱི་རྣལ་འབྱོར་བྱའོ། །",
    "before": "one's aspiration",
    "after": "your aspiration",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The existing imagine/undertake imperatives govern the preceding letters-in-accord-with-aspiration clause. Keep the same addressee across the instruction, without changing the still-provisional standalone mos pa wording or reconstructing it from mos gus."
  },
  {
    "pair": "DTG-000947",
    "ordinal": 950,
    "golden": [
      "U02124",
      "U02125"
    ],
    "family": "T12",
    "kind": "translation",
    "tibetan": "བསྲུང་བའི་དམ་ཚིག་ལྔ་པོ་ལ། །\nཆོ་ག་རྣམས་ནི་རྫོགས་བྱས་ཏེ། །",
    "before": "five pledges",
    "after": "five sacred pledges",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the complete approved dam tshig label, retaining the explicit five, the to-be-guarded scope and the fact that these five are not enumerated here. Do not substitute vow/restraint terminology."
  }
]
```

<a id="phase-d-notes-07"></a>
**Active note/usage dispositions recorded before appending:** Historical notes and approvals remain unchanged; the following records clarify current scope and status, including tenet system's now-approved label, current restored/source-selected readings, and the still-provisional P3 candidates.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T33",
    "pairs": [
      "DTG-000750",
      "DTG-000847"
    ],
    "ids": [
      "U01652",
      "U01653",
      "U01654",
      "U01655",
      "U01656",
      "U01901",
      "U01902"
    ],
    "realization": "meditative stabilization (retained provisionally)",
    "status": "P3 paired process/state test completed locally; shared label remains proposed",
    "reason": "Both training in the sleep practice and relying on the non-conceptual practice support testing meditative stability, distinct from deep absorption, equipoise and cultivation. They do not by themselves make the current stabilization wording a demonstrable mistranslation or activate a shared assignment. Retain the existing exact-linked provisional wording and record meditative stability for cross-work comparison; no book-specific default is established.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-078",
    "pairs": [
      "DTG-000754",
      "DTG-000756",
      "DTG-000760",
      "DTG-000763",
      "DTG-000765",
      "DTG-000766"
    ],
    "ids": [
      "U01662",
      "U01663",
      "U01664",
      "U01666",
      "U01670",
      "U01671",
      "U01676",
      "U01677",
      "U01678",
      "U01679",
      "U01680",
      "U01681",
      "U01682",
      "U01685",
      "U01686",
      "U01687",
      "U01688"
    ],
    "realization": "key point; one's own knowing (provisional)",
    "status": "Approved gnad labels; exact construction limits retained",
    "reason": "The two elemental accounts were compared: DTG-000763 retains its printed destroy/increase/slayer/decline/restore/equalize/confusion effects rather than being forced to match DTG-000580–000587. The rang shes row allows an ordinary possessive; the applying/knowing relation remains explicitly provisional rather than automatically becoming technical self-knowing. The three members and inquire-of-wind construction are not reconstructed.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-083",
    "pairs": [
      "DTG-000807",
      "DTG-000812",
      "DTG-000813",
      "DTG-000814",
      "DTG-000817",
      "DTG-000821"
    ],
    "ids": [
      "U01802",
      "U01803",
      "U01811",
      "U01812",
      "U01813",
      "U01814",
      "U01819",
      "U01820",
      "U01829"
    ],
    "realization": "ya bzhi unresolved; source-selected numerical readings",
    "status": "Current golden dispositions recognized; old four-million claim superseded",
    "reason": "The actual main text correctly leaves ya bzhi unresolved; the older sa ya/four-million expansion is already withdrawn by G-U01803, not a current defect. Keep the joined thousand-years/300,000-days statement once, the separate thirty-days variant and the qualified folding/contact note. Stars, half-cycles, unqualified 180 and the source's seasonal order remain unresolved as stated; no astronomical or arithmetic repair is made.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-085",
    "pairs": [
      "DTG-000831",
      "DTG-000834",
      "DTG-000836",
      "DTG-000839",
      "DTG-000843",
      "DTG-000846",
      "DTG-000847"
    ],
    "ids": [
      "U01861",
      "U01862",
      "U01863",
      "U01868",
      "U01869",
      "U01873",
      "U01874",
      "U01875",
      "U01876",
      "U01880",
      "U01881",
      "U01882",
      "A2000-C01-S02",
      "U01883",
      "U01884",
      "U01893",
      "U01894",
      "U01899",
      "U01900",
      "U01901",
      "U01902"
    ],
    "realization": "four-embodiment restoration present; cyclic existence; continuing lowercase at",
    "status": "Source updates and approved labels integrated; remaining constructions provisional",
    "reason": "The current list contains four embodiments through A2000-C01-S02 and U01883–U01884, superseding the older two-only treatment. The joining predicate and qualified subjects are already separated correctly; only the mid-sentence capital is repaired. Entity is retained where present, and generic accomplishment is not automatically dngos grub. Freedom from sound remains printed, and the visible breath-cessation editorial warning remains outside the source voice. Regard/refusal, desired qualities and the fifth neuter-empty referent remain qualified.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-086",
    "pairs": [
      "DTG-000850",
      "DTG-000851",
      "DTG-000852",
      "DTG-000853",
      "DTG-000857",
      "DTG-000860",
      "DTG-000861",
      "DTG-000863",
      "DTG-000864"
    ],
    "ids": [
      "U01907",
      "U01908",
      "U01909",
      "U01910",
      "U01911",
      "U01912",
      "U01913",
      "U01914",
      "U01920",
      "U01921",
      "U01922",
      "U01927",
      "U01928",
      "U01929",
      "U01930",
      "U01932",
      "U01933",
      "U01934",
      "U01935",
      "U01936"
    ],
    "realization": "entities; spiritual accomplishment; contextual material substances",
    "status": "Approved complete labels with material-context exception; distinct transferring scope",
    "reason": "The entity/form and emptiness types remain distinct. Material substances at U01929 is retained in the explicit rdzas/material-offering construction, not replaced by an English substring rule. The dngos grub clause gains spiritual, but generic grub does not. The method/voices clause keeps its historically corrected order. Youthful forms is not changed to a mount reading, and spo ba transferring is not silently equated with the earlier ph o ba category.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-087",
    "pairs": [
      "DTG-000866",
      "DTG-000867",
      "DTG-000869",
      "DTG-000873",
      "DTG-000875"
    ],
    "ids": [
      "U01938",
      "U01939",
      "U01940",
      "U01941",
      "U01942",
      "U01943",
      "U01945",
      "U01946",
      "U01947",
      "U01948",
      "U01960",
      "U01961",
      "U01962",
      "U01966",
      "U01967"
    ],
    "realization": "matter; qualified passive agent",
    "status": "Approved P2 matter and agent-attachment repair; existing exact questions retained",
    "reason": "Matter replaces the superseded bem po rendering; living beings at DTG-000866 is srog can and is not changed to karmic being. The passive taking agent, not food/wealth, possesses the summoning gesture. Actual [illness] at U01943 remains a linked, bracketed contextual proposal rather than an automatic entity substitution. The family construction, material supports and exact negative condition on worldly desire remain intact; no clinical claim or permission to harm/take property is endorsed.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-088",
    "pairs": [
      "DTG-000877",
      "DTG-000883",
      "DTG-000887",
      "DTG-000888"
    ],
    "ids": [
      "U01969",
      "U01970",
      "U01982",
      "U01983",
      "U01984",
      "U01992",
      "U01993",
      "U01994",
      "U01995",
      "U01996",
      "U01997"
    ],
    "realization": "tantra; quintessence; key point",
    "status": "Approved labels applied; distinct bodily and quantitative constructions provisional",
    "reason": "The literary scripture reference, concentrated bcud component and gnad uses are repaired without reintroducing old alignment errors. The two causes/eight conditions, half/twelve parts, three places and different restraint/reversal operations remain as written. The whole restraint-through-quintessence construction is not a new canonical expression, and no treatment parameters are supplied.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-089",
    "pairs": [
      "DTG-000891",
      "DTG-000892",
      "DTG-000893",
      "DTG-000894",
      "DTG-000895",
      "DTG-000896",
      "DTG-000897",
      "DTG-000898",
      "DTG-000899"
    ],
    "ids": [
      "U02000",
      "U02001",
      "U02002",
      "U02003",
      "U02004",
      "U02005",
      "A2000-C01-S03",
      "U02006",
      "U02007",
      "U02008",
      "U02009",
      "U02010",
      "U02011",
      "U02012",
      "U02013",
      "U02014",
      "U02015",
      "U02016",
      "U02017",
      "U02018",
      "U02019",
      "U02020"
    ],
    "realization": "tenet system",
    "status": "P2 approved term; full connected two-aspect account now read",
    "reason": "The historical absent-from-glossary/proposed label statement is superseded by the current complete grub mtha row. The full continuation has now been read, including restored lines; keep enlightened intent distinct, all nine-vehicle counts and the unenumerated names. This is not approval of every attachment in the old note.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T38",
    "pairs": [
      "DTG-000891",
      "DTG-000898",
      "DTG-000906"
    ],
    "ids": [
      "U02000",
      "U02001",
      "U02002",
      "U02013",
      "U02014",
      "U02015",
      "U02030",
      "U02031",
      "U02032"
    ],
    "realization": "tenet system; constituent tenets only where warranted",
    "status": "P2 approved assignment; historical proposal no longer pending as a label",
    "reason": "The current entry approves tenet system with tenets allowed only for constituent assertions. The system meanings in these clauses already conform; preserve the distinct enlightened-intent, own/others-assertion and knowing-one's-own-identity relationships. No specific school identity is introduced.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-090",
    "pairs": [
      "DTG-000892",
      "DTG-000893",
      "DTG-000894",
      "DTG-000896",
      "DTG-000898",
      "DTG-000899"
    ],
    "ids": [
      "U02003",
      "U02004",
      "U02005",
      "A2000-C01-S03",
      "U02006",
      "U02007",
      "U02009",
      "U02010",
      "U02011",
      "U02013",
      "U02014",
      "U02015",
      "U02016",
      "U02017",
      "U02018",
      "U02019",
      "U02020"
    ],
    "realization": "ordinary bases/basis; key point; cyclic existence",
    "status": "Locally supported classificatory basis sense under P1; exact hierarchy/attachment questions remain",
    "reason": "The connected worldly/transcendent vehicle classification supports ordinary basis rather than technical Ground. The two assertions, three causes/two results/six subdivisions/nine total, simultaneous-faculty self-liberation relation and the three-realms entering the path remain as printed and qualified. No external vehicle names or different arithmetic are imported. The restored wording is preserved byte-for-byte on the Tibetan side.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T39",
    "pairs": [
      "DTG-000913",
      "DTG-000937"
    ],
    "ids": [
      "U02047",
      "U02048",
      "U02049",
      "U02050",
      "U02105",
      "U02106"
    ],
    "realization": "methods (retained provisionally); means proposed for paired category",
    "status": "P3 construction test identifies the paired category; shared lexical assignment not activated",
    "reason": "The explicit means/discerning-knowing division and later return to thabs establish the technical paired-category role, distinct from actual procedures at DTG-000755 and the releasing method at DTG-000857. Means is the supported candidate for shared reconciliation, but methods is not changed merely for preferred style or promoted to a book-wide rule. The current exact-linked wording remains provisional; do not extend either choice to the queried thab form or the unrelated thabs gcig construction.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-092",
    "pairs": [
      "DTG-000919",
      "DTG-000922",
      "DTG-000923",
      "DTG-000929",
      "DTG-000932"
    ],
    "ids": [
      "U02064",
      "U02065",
      "U02069",
      "U02070",
      "U02071",
      "U02072",
      "U02073",
      "U02074",
      "U02075",
      "U02086",
      "U02087",
      "U02088",
      "U02089",
      "U02094",
      "U02095"
    ],
    "realization": "spiritual accomplishment; familiarization; practitioner conditions",
    "status": "Approved components and minimal condition/reference repairs; names and specifications remain provisional",
    "reason": "Preserve blessings versus spiritual accomplishments versus generic practices of accomplishment; the seven/three/three groups and numerical sequences keep their actual order and unspecified units. The practitioner, not doubt/certainty or another person, engages and owns the ordinary mind. Blessed Lady retains the feminine source addition to the honorific, not an imported proper name. Whole ritual letter, deity, sealing/restoring and phyi nas constructions remain provisional.",
    "review": "REVIEW.md#phase-d-notes-07"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-093",
    "pairs": [
      "DTG-000941",
      "DTG-000947"
    ],
    "ids": [
      "U02111",
      "U02112",
      "U02113",
      "U02114",
      "U02115",
      "U02124",
      "U02125"
    ],
    "realization": "your aspiration; sacred pledges",
    "status": "Imperative reference and complete P2 pledge label; whole continuation checked as context",
    "reason": "The U02113–U02114 letters/colors alignment is already correct and is not reversed. Standalone mos pa is not assigned a new label from the different mos gus entry. The five sacred pledges and all practice/numerical counts remain unexpanded. The context through DTG-000955 has been read, including the command about doubt and the separate expelling variant boundary; no efficacy, harmful instruction or unstated recitation unit is added.",
    "review": "REVIEW.md#phase-d-notes-07"
  }
]
```

**Important no-change cases:** The sound/voice and five-sense clauses retain the P1 acoustic exception, while the selected āli/kāli and deity/class names remain source-based, qualified and unreconstructed. By intrinsic nature without gyis remains the explicitly linked N-T35 grammatical proposal. The material-substance and actual-[illness] constructions are not automatically relabeled entity; the living-being expression is not sems can. Nominal entities, matter, actual/nonactual transference, shifting, and spo ba transferring remain distinguishable. Body/limbs in physical applications and branches of calculation/ritual remain their separate contextual senses.

The two elemental tables, 404/80/24/16/8/4 hierarchy, mother-years and za-ma, 300,000 days, stars' not-being-two, alternating half-cycles, years/months/days and unspecified 180 are preserved with their existing qualifications. The supposedly missing four-embodiment and vehicle-classification lines are already restored; four-million is already withdrawn. These historical examples are not current omission/arithmetic verdicts. The free-from-sound phrase and explicit breath warning remain intact; no practice specification or claim of efficacy is supplied. The offering restrictions, not-accomplished-for-worldly-desire condition and the source's command about doubt are not softened, amplified or made into editorial endorsement.

Whole expressions for generation/completion, mental engagement, leaving primordial liberation just as it is, and the two Great Perfection attachments remain as linked in N-091/N-T40–42. The final five results are not force-mapped onto a borrowed system. Meditative stability and paired-category means are recorded for shared reconciliation, not substituted merely because they are preferred or familiar. The full feminine Blessed Lady designation and ordinary aspiration wording are not reconstructed from different glossary heads.

**Application, changed-clause self-check and validation:** All 32 English operations in 28 pairs were applied and reread against their current Tibetan in a 72-pair changed-clause/context view. The ordinary-basis classification, passive summoning agent, practitioner conditions, possessive references, continuing sentence boundaries and complete approved labels were rechecked without altering numbers, negation, source roles or the remaining qualified attachments. The thirteen scoped note/usage additions preserve the inherited records. G-U02129 was also read directly to verify that the expelling variant remains separate. This is a repair self-check, not another independent review.

The final paired validator and projector check were actually rerun; both exit 1 at the historical protected-glossary contract. The full recorded-operation replay/integrity check exits 0: all 2,667 pair identities/order, fixed source/golden/policy/format/lineage, inherited notes/history and 700 English local-link targets pass. Current totals are 184 operations: 163 English repairs in 149 distinct pairs and 21 review links, affecting 161 pair payloads including note-only changes. The separate annotation repair is unchanged. There are 47 append-only Phase D usage dispositions; the prior 34 remain unchanged. English SHA-256: `109d4f76cd0ad3b0cc4134887a7ae76c786a5a30da0e6b84c76410ccaca6f6bc`. `git diff --check` passes. The blocked projector produced no new reader output.

**Saved coverage:** 950/2,667 pairs, ordinals 1–950 through DTG-000947, with 238 first-encountered note records. Continue at ordinal 951 / DTG-000948. Ordinals 951–965 have additionally been read as connected context, not counted separately. Text remains provisional and the whole-work pass is still in progress.

<a id="phase-d-batch-08"></a>
### Batch 08 — source ordinals 951–1150

All 200 current pairs through DTG-001145 and all 41 first-encountered note records were read in source order, with complete current Tibetan and all active/historical note prose and qualifications. Ordinals 1151–1165 were read as context, completing N-110, not yet counted as completed coverage. Relevant earlier questions, the chapter description and current usage records were reread. Q1–Q9, I §8.1 and III govern; full eight-column rows and attested whole expressions were rechecked.

**Evidence before application:** 62 English operations in 52 pairs are recorded below. New construction findings distinguish maturation recipients from agents, repair instrumental English modifiers, preserve the explicit familiarity condition, and resolve intensive sems nyid locally in the operational sequence. The contiguous short/full addressee name is made consistent without an external identity or shared default. Existing terminology families extend only to supported current constructions.

<!-- phase-d-batch-08-operations -->
```json
[
  {
    "pair": "DTG-000973",
    "ordinal": 976,
    "golden": [
      "U02178",
      "U02179"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ལྡོག་པར་བྱེད་པའི་གནད་ཀྱིས་ཀྱང་། །\nལུས་ཅན་སོ་སོའི་འཁྲུལ་པ་བཟློག །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-000976",
    "ordinal": 979,
    "golden": [
      "U02187",
      "A2000-C01-S04",
      "U02188"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ལུགས་སུ་ཁྱད་པར་སྡེབས་གཉིས་ཀྱི། །\nའདུ་ཤེས་ཅན་དག་མཐའ་ལ་འཇོག།\nམངོན་སུམ་གནད་ཀྱི་མན་ངག་གིས། །\nའཁོར་འདས་འབྱེད་པའི་སྤྲོས་པ་གཅོད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-000977",
    "ordinal": 980,
    "golden": [
      "U02189",
      "U02190"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "བསྒོམ་པ་གནད་ཀྱི་འཁོར་ལོ་ཡིས། །\nརླུང་སེམས་འབྲེལ་པའི་སྤྲོས་པ་གཅོད། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-000997",
    "ordinal": 1000,
    "golden": [
      "U02242",
      "U02243"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དུས་ནི་ལས་འཕྲོ་སད་པ་དང༌། །\nའབྱུང་བའི་འགྱུར་དང་སེམས་ཀྱི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001030",
    "ordinal": 1033,
    "golden": [
      "U02311",
      "U02312",
      "U02313"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "མངོན་སུམ་གནད་དང་བྲལ་བ་ལ། །\nམ་འོངས་གདུལ་བྱའི་སེམས་ཅན་རྣམས། །\nཚིག་ལ་ཡིད་ཆེས་བྱེད་པ་འབྱུང་། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001039",
    "ordinal": 1042,
    "golden": [
      "U02328"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "མངོན་སུམ་གནད་ནི་ལུས་ངག་སེམས། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001040",
    "ordinal": 1043,
    "golden": [
      "U02329"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "སོ་སོའི་གནད་རྣམས་ངེས་པར་བསྟུན། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001044",
    "ordinal": 1047,
    "golden": [
      "U02335"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གནད་གསུམ་མན་ངག་འབྲལ་མི་བྱ། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001045",
    "ordinal": 1048,
    "golden": [
      "U02336",
      "U02337"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ཡང་སྒོ་དང་ཡུལ་ཉིད་དང༌། །\nརླུང་དང་རིག་པའི་གནད་ཉིད་བརྟེན། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001055",
    "ordinal": 1058,
    "golden": [
      "U02351",
      "U02352"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "མི་འགུལ་གསུམ་ལ་གཞི་བཅས་པས། །\nརླུང་སེམས་གནད་ལ་ཕེབ་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001077",
    "ordinal": 1080,
    "golden": [
      "U02398",
      "U02399"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ལྟར་སྤྱོད་པ་རྫོགས་བྱས་ན། །\nམངོན་སུམ་གནད་ལ་རྟག་ཏུ་འགེལ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001088",
    "ordinal": 1091,
    "golden": [
      "U02418",
      "U02419"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "འདི་དུས་ལུས་ངག་སེམས་ཀྱི་གནད། །\nརྣལ་འབྱོར་ལྡན་པས་རྣལ་དབབ་བྱའོ། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001089",
    "ordinal": 1092,
    "golden": [
      "U02420",
      "U02421",
      "U02422",
      "U02423"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "འགྱུ་བྱེད་རླུང་གི་བརྡའ་དང་ཡང༌། །\nབསྲེས་ཤིང་འཕེན་ཅིང་སྡུད་པ་ཡི། །\nགནད་རྣམས་མཁས་པས་བསྟེན་བྱས་ན། །\nསེམས་ཀྱི་རྟོག་པ་རྒྱུན་ཆད་དོ། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001099",
    "ordinal": 1102,
    "golden": [
      "U02441",
      "U02442"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ཆོས་ཉིད་མངོན་སུམ་གནད་ཀྱིས་ཀྱང་། །\nལས་ལ་བཟང་ངན་མེད་པར་རྟོགས། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001106",
    "ordinal": 1109,
    "golden": [
      "U02455",
      "U02456"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གནད་བཞི་གྲོལ་བའི་གདེང་གིས་ནི། །\nའཁོར་དང་མྱ་ངན་འདས་མི་གནས། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001108",
    "ordinal": 1111,
    "golden": [
      "U02459",
      "U02460"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ཐོས་མཐོང་གྲོལ་བའི་གནད་ཉིད་ནི། །\nགཉིས་དང་ལྔ་སྟེ་བརྒྱད་ཀྱིས་རྟོགས། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001114",
    "ordinal": 1117,
    "golden": [
      "U02466",
      "U02467",
      "U02468"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གཞན་ཡང་བསྒོམ་པའི་གནད་རྣམས་ལ། །\nསྔོན་འགྲོ་བ་དང་དངོས་གཞི་དང༌། །\nརྗེས་འགྲོ་རྣམ་པ་གསུམ་དུ་འདོད། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001118",
    "ordinal": 1121,
    "golden": [
      "U02475",
      "U02476"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "འགྲོ་དྲུག་གཡང་ས་མཉམ་པའི་ཕྱིར། །\nལུས་ངག་ཡིད་ཀྱི་གནད་རྣམས་གཟིར། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001131",
    "ordinal": 1136,
    "golden": [
      "U02501",
      "U02502",
      "U02503"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "འཁོར་བའི་རྒྱུན་ཐག་གཅད་འདོད་པས། །\nལུས་ངག་ཞེན་པ་བཟློག་ནས་ཀྱང༌། །\nམངོན་སུམ་གནད་ལ་གཟིར་བར་བྱའོ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-001132",
    "ordinal": 1137,
    "golden": [
      "U02504",
      "U02505",
      "U02506"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "འཁྲུལ་པའི་རྩིས་ཀྱི་སྦྱོར་བ་ཡི། །\nའཁོར་འདས་དུས་ཚོད་བཟུང་བྱས་ཏེ། །\nབཟློག་པའི་གནད་ལ་མཁས་པར་བྱའོ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved gnad label at this exact read occurrence; preserve number, source-restored lines and the connected bodily/direct-perception construction."
  },
  {
    "pair": "DTG-000965",
    "ordinal": 968,
    "golden": [
      "U02158",
      "U02159",
      "U02160",
      "U02161"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འཁོར་དང་འདས་པ་མི་གནས་པས། །\nཆོས་ཉིད་སྟོང་པ་ཀུན་ཁྱབ་ཕྱིར། །\nཡེ་ཤེས་རང་ངོར་གནས་པ་ལས། །\nགསུམ་གྱི་ཚུལ་དུ་དབྱེར་མེད་དོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual khor das compound or explicitly coordinated expanded form supports the full approved equivalent. Preserve both members, negation/conditions and the secret-preliminary designation where present."
  },
  {
    "pair": "DTG-000976",
    "ordinal": 979,
    "golden": [
      "U02187",
      "A2000-C01-S04",
      "U02188"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "ལུགས་སུ་ཁྱད་པར་སྡེབས་གཉིས་ཀྱི། །\nའདུ་ཤེས་ཅན་དག་མཐའ་ལ་འཇོག།\nམངོན་སུམ་གནད་ཀྱི་མན་ངག་གིས། །\nའཁོར་འདས་འབྱེད་པའི་སྤྲོས་པ་གཅོད། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual khor das compound or explicitly coordinated expanded form supports the full approved equivalent. Preserve both members, negation/conditions and the secret-preliminary designation where present."
  },
  {
    "pair": "DTG-001012",
    "ordinal": 1015,
    "golden": [
      "U02284",
      "U02285"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "ཤིན་ཏུ་སྤྲོས་པ་མེད་པ་ལ། །\nའཁོར་འདས་རུ་ཤན་འོག་བཞིན་དབྱེ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual khor das compound or explicitly coordinated expanded form supports the full approved equivalent. Preserve both members, negation/conditions and the secret-preliminary designation where present."
  },
  {
    "pair": "DTG-001060",
    "ordinal": 1063,
    "golden": [
      "U02360",
      "U02361",
      "U02362"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འཁོར་འདས་རུ་ཤན་མ་ཕྱེས་ན། །\nཁམས་གསུམ་ལུས་ངག་ཡིད་ཀྱི་ཡང༌། །\nའབྲེལ་པ་ཆོད་པར་མི་འགྱུར་བས། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual khor das compound or explicitly coordinated expanded form supports the full approved equivalent. Preserve both members, negation/conditions and the secret-preliminary designation where present."
  },
  {
    "pair": "DTG-001061",
    "ordinal": 1064,
    "golden": [
      "U02363"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འཁོར་འདས་རུ་ཤན་ཕྱེ་བ་བཤད། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual khor das compound or explicitly coordinated expanded form supports the full approved equivalent. Preserve both members, negation/conditions and the secret-preliminary designation where present."
  },
  {
    "pair": "DTG-001123",
    "ordinal": 1126,
    "golden": [
      "U02485",
      "U02486",
      "U02487"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "ཆོས་ཀུན་བྱ་བ་བྲལ་བ་དང༌། །\nའཁོར་འདས་འབྲེལ་པ་ཆད་པའི་དུས། །\nརྟོག་བཅས་འཁྲུལ་པ་འགགས་པ་སྟེ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual khor das compound or explicitly coordinated expanded form supports the full approved equivalent. Preserve both members, negation/conditions and the secret-preliminary designation where present."
  },
  {
    "pair": "DTG-001132",
    "ordinal": 1137,
    "golden": [
      "U02504",
      "U02505",
      "U02506"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འཁྲུལ་པའི་རྩིས་ཀྱི་སྦྱོར་བ་ཡི། །\nའཁོར་འདས་དུས་ཚོད་བཟུང་བྱས་ཏེ། །\nབཟློག་པའི་གནད་ལ་མཁས་པར་བྱའོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The actual khor das compound or explicitly coordinated expanded form supports the full approved equivalent. Preserve both members, negation/conditions and the secret-preliminary designation where present."
  },
  {
    "pair": "DTG-000987",
    "ordinal": 990,
    "golden": [
      "U02213",
      "U02214"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "དེ་ལ་དམིགས་ཏེ་བླ་མ་བསྟེན། །\nའཁོར་བའི་གཡུལ་ལས་བཟློག་ཕྱིར་རོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply khor ba without changing the battlefield/flow/precipice metaphor, possessive, or source-positioned heading interruption."
  },
  {
    "pair": "DTG-001053",
    "ordinal": 1056,
    "golden": [
      "U02348",
      "U02349"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "ཆོས་ཉིད་ཟད་པའི་སྣང་བ་ཡིས། །\nཁམས་གསུམ་འཁོར་བའི་རྒྱུན་ཐག་བཅད། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply khor ba without changing the battlefield/flow/precipice metaphor, possessive, or source-positioned heading interruption."
  },
  {
    "pair": "DTG-002667",
    "ordinal": 1127,
    "golden": [
      "U02488",
      "U02489"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འཁོར་བའི་གཡང་ས་རྒྱུན་བཅད་པས། །\nརྣལ་འབྱོར་ཆེན་པོའི་སྤྱོད་པའི། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply khor ba without changing the battlefield/flow/precipice metaphor, possessive, or source-positioned heading interruption."
  },
  {
    "pair": "DTG-001131",
    "ordinal": 1136,
    "golden": [
      "U02501",
      "U02502",
      "U02503"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འཁོར་བའི་རྒྱུན་ཐག་གཅད་འདོད་པས། །\nལུས་ངག་ཞེན་པ་བཟློག་ནས་ཀྱང༌། །\nམངོན་སུམ་གནད་ལ་གཟིར་བར་བྱའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply khor ba without changing the battlefield/flow/precipice metaphor, possessive, or source-positioned heading interruption."
  },
  {
    "pair": "DTG-001134",
    "ordinal": 1139,
    "golden": [
      "U02509"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "དེས་ནི་འཁོར་བའི་རྒྱུན་ཆད་དོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply khor ba without changing the battlefield/flow/precipice metaphor, possessive, or source-positioned heading interruption."
  },
  {
    "pair": "DTG-001106",
    "ordinal": 1109,
    "golden": [
      "U02455",
      "U02456"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "གནད་བཞི་གྲོལ་བའི་གདེང་གིས་ནི། །\nའཁོར་དང་མྱ་ངན་འདས་མི་གནས། །",
    "before": "samsara and passing beyond sorrow",
    "after": "cyclic existence and transcendence of sorrow",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Both coordinated items are the subjects of do not abide. The attested mya ngan das form is the technical noun here, not a separate passing action; preserve the nonabiding predicate."
  },
  {
    "pair": "DTG-001030",
    "ordinal": 1033,
    "golden": [
      "U02311",
      "U02312",
      "U02313"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "མངོན་སུམ་གནད་དང་བྲལ་བ་ལ། །\nམ་འོངས་གདུལ་བྱའི་སེམས་ཅན་རྣམས། །\nཚིག་ལ་ཡིད་ཆེས་བྱེད་པ་འབྱུང་། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved sems can label, preserving number, modifiers, beneficiary role and neither/nor negation. Do not extend it to other being expressions."
  },
  {
    "pair": "DTG-001031",
    "ordinal": 1034,
    "golden": [
      "U02314",
      "U02315"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "རྟོག་པ་རགས་པའི་སེམས་ཅན་རྣམས། །\nཚིག་ལ་སྤྱོད་ཕྱིར་སྨིན་པ་མིན། །",
    "before": "Sentient beings",
    "after": "Karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved sems can label, preserving number, modifiers, beneficiary role and neither/nor negation. Do not extend it to other being expressions."
  },
  {
    "pair": "DTG-001097",
    "ordinal": 1100,
    "golden": [
      "U02435",
      "U02436",
      "U02437"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་དོན་ཕྱིར་ལྷ་དབང་ཁྱོད། །\nབརྩེ་བའི་དོན་དེ་དྲིས་པའི་ལན། །\nངས་བསྟན་འཁྲུལ་པ་མེད་པར་བཟུང་། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved sems can label, preserving number, modifiers, beneficiary role and neither/nor negation. Do not extend it to other being expressions."
  },
  {
    "pair": "DTG-001127",
    "ordinal": 1132,
    "golden": [
      "U02496",
      "U02497"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སྐུ་དང་ཡེ་ཤེས་རྒྱུན་ཆད་པས། །\nསངས་རྒྱས་མེད་ཅིང་སེམས་ཅན་མེད། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete approved sems can label, preserving number, modifiers, beneficiary role and neither/nor negation. Do not extend it to other being expressions."
  },
  {
    "pair": "DTG-001008",
    "ordinal": 1011,
    "golden": [
      "U02271",
      "U02272",
      "U02273"
    ],
    "family": "T06",
    "kind": "translation",
    "tibetan": "གཞན་ཡང་ས་ཡི་ཆོ་ག་དང་། །\nསྟ་གོན་ཐིག་དང་ཚོན་དགྱེ་དང་། །\nརྒྱུད་ལས་འབྱུང་བའི་དཀྱིལ་འཁོར་བཞེངས། །",
    "before": "maṇḍala",
    "after": "mandala",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the approved undiacritized technical loanword. The earth rite, vase pairing and ordinary-mind mandala support the same referent; the Tibetan loan spelling in U02282 is an attested form, not a different assignment."
  },
  {
    "pair": "DTG-001011",
    "ordinal": 1014,
    "golden": [
      "U02280",
      "U02281",
      "U02282",
      "U02283"
    ],
    "family": "T06",
    "kind": "translation",
    "tibetan": "སྤྲོས་མེད་དད་ལྡན་འཇུག་སྨིན་ཕྱིར། །\nསྤྲོས་པ་མེད་པའི་དབང་མཆོག་ནི། །\nམཎྜལ་བུམ་པ་ལ་བརྟེན་ནས། །\nཚིགས་སུ་བཅད་པའི་དབང་སྦྱིན་བྱ། །",
    "before": "maṇḍala",
    "after": "mandala",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the approved undiacritized technical loanword. The earth rite, vase pairing and ordinary-mind mandala support the same referent; the Tibetan loan spelling in U02282 is an attested form, not a different assignment."
  },
  {
    "pair": "DTG-001018",
    "ordinal": 1021,
    "golden": [
      "U02294",
      "U02295",
      "U02296"
    ],
    "family": "T06",
    "kind": "translation",
    "tibetan": "རབ་ཏུ་སྤྲོས་པ་མེད་པ་ལ། །\nསེམས་ཀྱི་དཀྱིལ་འཁོར་སྒོ་ཕྱེ་ལ། །\nལུས་ཀྱི་འདུག་སྟངས་ངེས་པར་བརྩམ། །",
    "before": "maṇḍala",
    "after": "mandala",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the approved undiacritized technical loanword. The earth rite, vase pairing and ordinary-mind mandala support the same referent; the Tibetan loan spelling in U02282 is an attested form, not a different assignment."
  },
  {
    "pair": "DTG-001004",
    "ordinal": 1007,
    "golden": [
      "U02253",
      "U02254",
      "U02255"
    ],
    "family": "T01",
    "kind": "translation",
    "tibetan": "རྒྱུད་གཞན་དག་ཏུ་སྦས་པ་ཡི། །\nསུས་ཀྱང་ཤེས་པ་མེད་པ་ཡི། །\nདབང་བསྐུར་བ་ཡི་ཆོ་ག་བཤད། །",
    "before": "other continua",
    "after": "other tantras",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The clause explicitly refers to a scriptural teaching/text, activating the P1 literary exception. Do not change the distinct personal continua of the faithful."
  },
  {
    "pair": "DTG-001008",
    "ordinal": 1011,
    "golden": [
      "U02271",
      "U02272",
      "U02273"
    ],
    "family": "T01",
    "kind": "translation",
    "tibetan": "གཞན་ཡང་ས་ཡི་ཆོ་ག་དང་། །\nསྟ་གོན་ཐིག་དང་ཚོན་དགྱེ་དང་། །\nརྒྱུད་ལས་འབྱུང་བའི་དཀྱིལ་འཁོར་བཞེངས། །",
    "before": "the continuum",
    "after": "the tantra",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The clause explicitly refers to a scriptural teaching/text, activating the P1 literary exception. Do not change the distinct personal continua of the faithful."
  },
  {
    "pair": "DTG-001035",
    "ordinal": 1038,
    "golden": [
      "U02320",
      "U02321",
      "U02322"
    ],
    "family": "T01",
    "kind": "translation",
    "tibetan": "གསང་བ་ངེས་པའི་རྒྱུད་འདི་ནི། །\nམངོན་སུམ་ལམ་ལ་བརྟེན་པ་ཡི། །\nརང་ཤེས་རིག་པར་འདུས་པའོ། །",
    "before": "This continuum",
    "after": "This tantra",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The clause explicitly refers to a scriptural teaching/text, activating the P1 literary exception. Do not change the distinct personal continua of the faithful."
  },
  {
    "pair": "DTG-001136",
    "ordinal": 1141,
    "golden": [
      "U02511",
      "U02512",
      "U02513"
    ],
    "family": "T01",
    "kind": "translation",
    "tibetan": "བཅུད་ཀྱིས་ལེན་པ་འདི་ལྟ་བུ། །\nརྒྱུད་གཞན་ཀུན་ཏུ་མ་བསྟན་པ། །\nཨེ་མ་ངོ་མཚར་ཆེ་བར་བཤད། །",
    "before": "any other continuum",
    "after": "any other tantra",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The clause explicitly refers to a scriptural teaching/text, activating the P1 literary exception. Do not change the distinct personal continua of the faithful."
  },
  {
    "pair": "DTG-001020",
    "ordinal": 1023,
    "golden": [
      "U02298"
    ],
    "family": "T16",
    "kind": "translation",
    "tibetan": "མངོན་སུམ་རིག་པ་ལུང་གི་བརྡའོ། །",
    "before": "authoritative transmission",
    "after": "transmission",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Lung has the approved transmission label without a source modifier expressing authoritative. Preserve the sign predicate or ordinary-mind possessor and distinguish rlung/wind."
  },
  {
    "pair": "DTG-001113",
    "ordinal": 1116,
    "golden": [
      "U02465"
    ],
    "family": "T16",
    "kind": "translation",
    "tibetan": "སེམས་ཀྱི་ལུང་གིས་ངེས་སྦྱར་ཏེ། །",
    "before": "authoritative transmission",
    "after": "transmission",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Lung has the approved transmission label without a source modifier expressing authoritative. Preserve the sign predicate or ordinary-mind possessor and distinguish rlung/wind."
  },
  {
    "pair": "DTG-001030",
    "ordinal": 1033,
    "golden": [
      "U02311",
      "U02312",
      "U02313"
    ],
    "family": "T14",
    "kind": "translation",
    "tibetan": "མངོན་སུམ་གནད་དང་བྲལ་བ་ལ། །\nམ་འོངས་གདུལ་བྱའི་སེམས་ཅན་རྣམས། །\nཚིག་ལ་ཡིད་ཆེས་བྱེད་པ་འབྱུང་། །",
    "before": "will place their trust in words.",
    "after": "will have conviction in words.",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Yid ches denotes epistemic reliance on verbal formulations contrasted with direct perception, not an interpersonal trusting relationship. Apply conviction without endorsing the source prediction."
  },
  {
    "pair": "DTG-001022",
    "ordinal": 1025,
    "golden": [
      "U02300",
      "U02301",
      "U02302"
    ],
    "family": "T12",
    "kind": "translation",
    "tibetan": "རྟོག་མེད་སེམས་དཔའ་ལྷ་ཡི་བུ། །\nདགའ་བྱེད་དབང་ཕྱུག་མགུ་བྱའི་ཕྱིར། །\nདབང་བརྟེན་པ་ཡི་དམ་ཚིག་བཤད། །",
    "before": "the pledges",
    "after": "the sacred pledges",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Retain the complete approved dam tshig label and the distinct sdom pa/vow account; do not invent unenumerated obligations."
  },
  {
    "pair": "DTG-001136",
    "ordinal": 1141,
    "golden": [
      "U02511",
      "U02512",
      "U02513"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "བཅུད་ཀྱིས་ལེན་པ་འདི་ལྟ་བུ། །\nརྒྱུད་གཞན་ཀུན་ཏུ་མ་བསྟན་པ། །\nཨེ་མ་ངོ་མཚར་ཆེ་བར་བཤད། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Extend the supported bcud nourishment construction to this actual occurrence. Preserve substance classes, source claims and qualifications; do not invent ingredients, doses or efficacy."
  },
  {
    "pair": "DTG-001141",
    "ordinal": 1146,
    "golden": [
      "U02521",
      "U02522"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "རྩི་སྦྱོར་དག་གི་བཅུད་ལེན་གྱིས། །\nགཟི་བརྗིད་ལྡན་ཞིང་གཞོན་པར་འགྱུར། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Extend the supported bcud nourishment construction to this actual occurrence. Preserve substance classes, source claims and qualifications; do not invent ingredients, doses or efficacy."
  },
  {
    "pair": "DTG-001143",
    "ordinal": 1148,
    "golden": [
      "U02525",
      "U02526"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "གཞན་ཡང་རླུང་ལ་བརྟེན་པ་ཡི། །\nངོ་མཚར་ཆེ་བའི་བཅུད་ལེན་བཤད། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Extend the supported bcud nourishment construction to this actual occurrence. Preserve substance classes, source claims and qualifications; do not invent ingredients, doses or efficacy."
  },
  {
    "pair": "DTG-000948",
    "ordinal": 951,
    "golden": [
      "U02126",
      "U02127"
    ],
    "family": "E02",
    "kind": "translation",
    "tibetan": "ཁྲོ་རྒྱལ་མི་གཡོ་མགོན་པོའི་སྐུ། །\nདད་པས་ངེས་པར་རང་ལུས་བསམ། །",
    "before": "one's own body",
    "after": "your own body",
    "severity": "minor",
    "confidence": "high",
    "rationale": "The explicit imagine/rely imperatives govern the practitioner's own body. Preserve the same addressee and ownership throughout the instruction."
  },
  {
    "pair": "DTG-000983",
    "ordinal": 986,
    "golden": [
      "U02200",
      "U02201",
      "U02202"
    ],
    "family": "E02",
    "kind": "translation",
    "tibetan": "སོ་སོའི་མཚན་ཉིད་ཚང་བ་ལ། །\nརྒྱལ་སྲིད་དང་ནི་རང་གི་ལུས། །\nའཁོར་དང་ལོངས་སྤྱོད་རྣམས་ཀྱིས་བསྟེན། །",
    "before": "one's own body",
    "after": "your own body",
    "severity": "minor",
    "confidence": "high",
    "rationale": "The explicit imagine/rely imperatives govern the practitioner's own body. Preserve the same addressee and ownership throughout the instruction."
  },
  {
    "pair": "DTG-000949",
    "ordinal": 952,
    "golden": [
      "U02128",
      "U02129",
      "U02130"
    ],
    "family": "E02",
    "kind": "translation",
    "tibetan": "ལྕགས་ཀྱུ་ཡི་ནི་འོད་ཟེར་གྱིས། །\nདགུག་དང་བསད་དང་བཅིངས་པའི་ལས། །\nརང་གིས་ཅི་ལྟར་འདོད་པ་སྤྲོ། །",
    "before": "in whatever way one desires.",
    "after": "in whatever way you desire.",
    "severity": "minor",
    "confidence": "high",
    "rationale": "The proliferate imperative addresses the same practitioner as rang gis. Preserve that addressee without changing the separately printed expelling variant or inventing a new agent."
  },
  {
    "pair": "DTG-001006",
    "ordinal": 1009,
    "golden": [
      "U02263",
      "U02264",
      "U02265",
      "U02266",
      "U02267"
    ],
    "family": "S15",
    "kind": "translation",
    "tibetan": "སྤྲོས་བཅས་ཉིད་དང་སྤྲོས་མེད་དང༌། །\nཤིན་ཏུ་སྤྲོས་པ་མེད་པ་དང་། །\nདེ་བཞིན་རབ་ཏུ་སྤྲོས་པ་མེད། །\nདབྱེ་བ་བཞི་ཡི་ཚུལ་གྱིས་ནི། །\nདད་ལྡན་རང་རྒྱུད་སྨིན་པར་བྱེད། །",
    "before": "the faithful mature their own continua.",
    "after": "the faithful's own continua are matured.",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Dad ldan rang rgyud is the maturation recipient/object in this empowerment account, confirmed by the fortunate brought to maturity before and the guru's rite after. The source does not make the faithful independent self-maturing agents. Use the passive without adding a named agent; retain own and personal continua."
  },
  {
    "pair": "DTG-001022",
    "ordinal": 1025,
    "golden": [
      "U02300",
      "U02301",
      "U02302"
    ],
    "family": "N01",
    "kind": "translation",
    "tibetan": "རྟོག་མེད་སེམས་དཔའ་ལྷ་ཡི་བུ། །\nདགའ་བྱེད་དབང་ཕྱུག་མགུ་བྱའི་ཕྱིར། །\nདབང་བརྟེན་པ་ཡི་དམ་ཚིག་བཤད། །",
    "before": "Delight-Maker",
    "after": "Joy-Maker",
    "severity": "minor",
    "confidence": "high for this contiguous recurrence",
    "rationale": "The contiguous fifty-sixth/fifty-seventh reply sequence addresses the same sovereign son of the gods as dga byed and lha dbang dga byed. Retain the already used restored Joy-Maker designation consistently. No external deity identity or new shared name assignment is supplied; later roles still need comparison."
  },
  {
    "pair": "DTG-001055",
    "ordinal": 1058,
    "golden": [
      "U02351",
      "U02352"
    ],
    "family": "S06",
    "kind": "translation",
    "tibetan": "མི་འགུལ་གསུམ་ལ་གཞི་བཅས་པས། །\nརླུང་སེམས་གནད་ལ་ཕེབ་པའོ། །",
    "before": "With a Ground in the three nonmovements,",
    "after": "With a basis in the three nonmovements,",
    "severity": "medium",
    "confidence": "moderate-high",
    "rationale": "Gzhi bcas pas supplies the supporting basis in three nonmovements for arrival at the wind-mind key point, not an assertion that these arrangements are the primordial Ground. Apply ordinary basis locally; do not invent the three members."
  },
  {
    "pair": "DTG-001056",
    "ordinal": 1059,
    "golden": [
      "U02353",
      "U02354",
      "U02355"
    ],
    "family": "E07",
    "kind": "translation",
    "tibetan": "སྡོད་པ་གསུམ་གྱིས་ཚད་བཟུང་བས། །\nརྨི་ལམ་བཟློག་དང་ལུས་ངག་ཡིད། །\nརྟགས་དང་ཚད་ནི་ངེས་བཟུང་བའོ། །",
    "before": "Taking the measure through three ways of remaining,",
    "after": "By taking the measure through three ways of remaining,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Instrumental bzung bas leads to dreams being reversed and signs/measures being grasped. Dreams are not the performer taking the measure. Add only the instrumental preposition."
  },
  {
    "pair": "DTG-001057",
    "ordinal": 1060,
    "golden": [
      "U02356",
      "U02357"
    ],
    "family": "E07",
    "kind": "translation",
    "tibetan": "ཐོབ་པ་གསུམ་གྱིས་གཟེར་བཏབ་པས། །\nཟག་བཅས་ཕུང་པོ་མི་སྣང་བའོ། །",
    "before": "Fixing [this] with the three attainments,",
    "after": "By fixing [this] with the three attainments,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Instrumental btab pas leads to contaminated aggregates not appearing; the aggregates do not perform the fixing. Add only the preposition, retaining the bracketed referent, three attainments and negation."
  },
  {
    "pair": "DTG-001115",
    "ordinal": 1118,
    "golden": [
      "U02469",
      "U02470",
      "U02471"
    ],
    "family": "S14/E07",
    "kind": "translation",
    "tibetan": "ལུས་སྦྱངས་སེམས་ཉིད་གདུལ་བ་དང་། །\nངག་གི་བྱ་བ་རྫོགས་པ་ཡིས། །\nསེམས་ཉིད་ལམ་དུ་ཞུགས་པའོ། །",
    "before": "Training the body, taming the nature of ordinary mind,\nand completing the activities of speech,\nthe nature of ordinary mind enters the path.",
    "after": "By training the body, taming ordinary mind itself,\nand completing the activities of speech,\nordinary mind itself enters the path.",
    "severity": "medium",
    "confidence": "moderate-high",
    "rationale": "In this operational body/speech/mind sequence, sems nyid is ordinary mind itself being tamed and entering the path; the next line again separates body and ordinary mind. The added nature abstraction is not supported as the object trained here. Apply I §8.1 U07 locally, keeping both intensives, not a universal default. By preserves the instrumental yis and prevents a dangling performer relation."
  },
  {
    "pair": "DTG-001119",
    "ordinal": 1122,
    "golden": [
      "U02477",
      "U02478"
    ],
    "family": "S14",
    "kind": "translation",
    "tibetan": "སེམས་ཉིད་ཆོས་དང་བསྲེ་བའི་ཕྱིར། །\nརླུང་དང་ཤེས་པ་གྱེན་དུ་དྲང་། །",
    "before": "the nature of ordinary mind",
    "after": "ordinary mind itself",
    "severity": "medium",
    "confidence": "moderate-high",
    "rationale": "This continues the same operational sems nyid subject of DTG-001115, mixing with explicit chos/phenomena, not chos nyid. Preserve the intensive locally and the actual wind/knowing operation. DTG-000332 remains separately qualified."
  },
  {
    "pair": "DTG-001122",
    "ordinal": 1125,
    "golden": [
      "U02482",
      "U02483",
      "U02484"
    ],
    "family": "S09",
    "kind": "translation",
    "tibetan": "སྤྱོད་པའི་སྦྱོར་བ་དབྱིངས་རིག་ལ། །\nགཟེར་གསུམ་ལྡན་པ་འབྲལ་མེད་པར། །\nརྟག་ཏུ་འདྲིས་ན་སྤྱོད་པ་བདེ། །",
    "before": "continual familiarity makes activity easeful.",
    "after": "when there is continual familiarity, activity is easeful.",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Dris na explicitly gives a familiarity condition and spyod pa bde predicates easeful activity. Preserve the condition rather than adding an active makes-causal formulation; keep three fixings, inseparability and basic-space/awareness scope."
  }
]
```

<a id="phase-d-notes-08"></a>
**Active note/usage additions recorded before appending:** Historical proposal and approval text is preserved; these exact-scope dispositions distinguish local resolutions from remaining questions.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-096",
    "pairs": [
      "DTG-000975",
      "DTG-000976",
      "DTG-000977",
      "DTG-000978"
    ],
    "ids": [
      "U02181",
      "U02182",
      "U02183",
      "U02184",
      "U02185",
      "U02186",
      "U02187",
      "A2000-C01-S04",
      "U02188",
      "U02189",
      "U02190",
      "U02191",
      "U02192"
    ],
    "realization": "key point; restored perception lines",
    "status": "Current restoration recognized; remaining attachments provisional",
    "reason": "The question U00235 was reread with the answer. Both restored lines are present and lead into the cutting instruction. Keep two combinations, general/particular, perception, three cutting actions, wind-mind and conceptual mind distinct; their qualified attachments are not filled from an external system.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-097",
    "pairs": [
      "DTG-000980",
      "DTG-000981",
      "DTG-000983",
      "DTG-000987"
    ],
    "ids": [
      "U02194",
      "U02195",
      "U02196",
      "U02197",
      "U02198",
      "U02200",
      "U02201",
      "U02202",
      "U02213",
      "U02214"
    ],
    "realization": "great vajra-holder guru provisionally retained; your own body",
    "status": "Name-versus-description control; reference repair only",
    "reason": "The Vajradhara row governs a named figure. The instrumental guru introduction and root/branch guru explanation do not conclusively distinguish that identity from a descriptive guru designation; retain great vajra-holder provisionally rather than automatically normalize a historical example. Equal union with buddha is not an editorial identity assertion. The Ground-of-complete-awakening scope and N-T43 guru/lama proposal remain qualified, unlike the resolved practical basis at DTG-001055.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-098",
    "pairs": [
      "DTG-000989",
      "DTG-000990",
      "DTG-000991",
      "DTG-000992",
      "DTG-000993",
      "DTG-000994",
      "DTG-000995"
    ],
    "ids": [
      "U02216",
      "U02217",
      "U02218",
      "U02219",
      "U02220",
      "U02221",
      "U02222",
      "U02223",
      "U02224",
      "U02225",
      "U02226",
      "U02227",
      "U02228",
      "U02229",
      "U02230",
      "U02231",
      "U02232",
      "U02233",
      "U02234",
      "U02235",
      "U02236",
      "U02237",
      "U02238",
      "U02239",
      "U02240"
    ],
    "realization": "acoustic sound; entire speaking/bad-news note separate",
    "status": "P1 acoustic scope adopted; old source-boundary criticism superseded",
    "reason": "The elemental sensory list supports sound. The entire smra dang gtam ngan annotation is already separate, not just bad news. Eleven gods, twelve displays and the making-manifest/omen actor remain qualified. No deity list, historical identification, prediction or practical divination scheme is supplied.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-099",
    "pairs": [
      "DTG-000997",
      "DTG-000998",
      "DTG-000999",
      "DTG-001000",
      "DTG-001001"
    ],
    "ids": [
      "U02242",
      "U02243",
      "U02244",
      "U02245",
      "U02246",
      "U02247",
      "U02248",
      "U02249"
    ],
    "realization": "key point; hearth and continuation of karma provisional",
    "status": "Approved component; exact queried source retained",
    "reason": "U00238 was reread. Its juncture wording does not authorize changing the actual thab to thabs/means or bab/juncture. The empty/emptiness/terminator triad and las phro whole construction remain unresolved; no calendar or new witness reading is invented.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-100",
    "pairs": [
      "DTG-001004",
      "DTG-001005",
      "DTG-001006",
      "DTG-001007",
      "DTG-001008",
      "DTG-001011",
      "DTG-001012",
      "DTG-001016",
      "DTG-001018",
      "DTG-001020"
    ],
    "ids": [
      "U02253",
      "U02254",
      "U02255",
      "U02256",
      "U02257",
      "U02258",
      "U02259",
      "U02260",
      "U02261",
      "U02262",
      "U02263",
      "U02264",
      "U02265",
      "U02266",
      "U02267",
      "U02268",
      "U02269",
      "U02270",
      "U02271",
      "U02272",
      "U02273",
      "U02280",
      "U02281",
      "U02282",
      "U02283",
      "U02284",
      "U02285",
      "U02291",
      "U02292",
      "U02294",
      "U02295",
      "U02296",
      "U02298"
    ],
    "realization": "tantra; mandala; transmission; passive maturation",
    "status": "Approved labels and agent/recipient repair; full rite constructions still qualified",
    "reason": "Preserve all fours and eight stages, the approach/accomplishment/close-approach order and distinct body/speech/mental-faculty/ordinary-mind members. The faithful are maturation recipients, not inserted independent self-maturing agents. The own-identity introduction, signs and final perception/transmission predicate remain qualified; no missing empowerment contents or authorization is supplied.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T47",
    "pairs": [
      "DTG-001012",
      "DTG-001060",
      "DTG-001061"
    ],
    "ids": [
      "U02284",
      "U02285",
      "U02360",
      "U02361",
      "U02362",
      "U02363"
    ],
    "realization": "distinguish cyclic existence and transcendence of sorrow through the secret preliminary",
    "status": "Locally supported complete construction; no new canonical assignment",
    "reason": "Explicit distinguishing verbs and coordinated objects support the named secret preliminary plus its stated relationship. The practice designation is retained, not silently omitted under the old question-only exception. This does not add a practice step or derive an entire unlisted expression from isolated components.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-101",
    "pairs": [
      "DTG-001022",
      "DTG-001025",
      "DTG-001026",
      "DTG-001027",
      "DTG-001028",
      "DTG-001030",
      "DTG-001031",
      "DTG-001032"
    ],
    "ids": [
      "U02300",
      "U02301",
      "U02302",
      "U02308",
      "A2000-C01-S05",
      "A2000-C01-S06",
      "A2000-C01-S07",
      "U02311",
      "U02312",
      "U02313",
      "U02314",
      "U02315",
      "U02316",
      "U02317"
    ],
    "realization": "sacred pledges; Joy-Maker; karmic beings; conviction",
    "status": "Adopted labels and contiguous recurring-name consistency; heading present",
    "reason": "The fifty-seventh heading and surrounding main verses are already restored and separately displayed. The immediate dga byed/full lha dbang dga byed recurrence takes the existing Joy-Maker designation consistently without erasing different honorific forms or naming an external deity. Pledges/vows remain distinct. The word-directed yid ches is epistemic conviction; the sa-based ground-of-aspirational-activity whole expression remains a qualified proposal, not technical gzhi/Ground.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T50",
    "pairs": [
      "DTG-001022",
      "DTG-001025"
    ],
    "ids": [
      "U02300",
      "U02301",
      "U02302",
      "U02308"
    ],
    "realization": "sacred pledges; vows unchanged",
    "status": "P2 pledge status extended to this reviewed empowerment account",
    "reason": "The historical pledge proposal is superseded here by the complete approved label. Sdom pa/vows and bka/command remain separate; no unlisted obligations or shared vow assignment are invented.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-102",
    "pairs": [
      "DTG-001034",
      "DTG-001035",
      "DTG-001036",
      "DTG-001037"
    ],
    "ids": [
      "U02319",
      "U02320",
      "U02321",
      "U02322",
      "U02323",
      "U02324",
      "U02325",
      "U02326"
    ],
    "realization": "tantra; rang shes/rang rig relationships provisional",
    "status": "P1 literary reference; unresolved predicate precisely retained",
    "reason": "The affirmative greatly-complete elaboration wording is not changed into its doctrinal opposite, and the all-buddhas/nature-of-phenomena order is already corrected. At DTG-001035, rang shes rig par dus may mean that the tantra is gathered into self-knowing awareness rather than actively gathers one's own knowing into awareness. Technical versus possessive relationship and predicate attachment remain linked provisional alternatives. A decisive internal parallel or authorized commentary would settle them; the different rang rig expression is not conflated.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-103",
    "pairs": [
      "DTG-001039",
      "DTG-001040",
      "DTG-001042",
      "DTG-001044",
      "DTG-001045",
      "DTG-001049",
      "DTG-001050",
      "DTG-001051",
      "DTG-001052",
      "DTG-001053",
      "DTG-001055",
      "DTG-001056",
      "DTG-001057"
    ],
    "ids": [
      "U02328",
      "U02329",
      "U02332",
      "U02333",
      "U02335",
      "U02336",
      "U02337",
      "U02341",
      "U02342",
      "U02343",
      "U02344",
      "U02345",
      "U02346",
      "U02347",
      "U02348",
      "U02349",
      "U02351",
      "U02352",
      "U02353",
      "U02354",
      "U02355",
      "U02356",
      "U02357"
    ],
    "realization": "key points; practical basis; instrumental results",
    "status": "P1/P2 labels and English attachment repairs; threefold sets remain unenumerated",
    "reason": "The full account, four named visions and distinct threefold sets were read together. Basis in nonmovements is a supporting construction. Added instrumental prepositions prevent dreams/aggregates from being the performers. The body-abides supply, door/three-embodiment arrangement, speech-passing-beyond clause and unnamed sets remain qualified; training/waves is already separated.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T54",
    "pairs": [
      "DTG-001050",
      "DTG-001051",
      "DTG-001052",
      "DTG-001053"
    ],
    "ids": [
      "U02342",
      "U02343",
      "U02344",
      "U02345",
      "U02346",
      "U02347",
      "U02348",
      "U02349"
    ],
    "realization": "four established vision labels",
    "status": "Local attested-form equivalence supported",
    "reason": "The explicit four-vision introduction and ordered full clauses establish the particle-omitted, reordered increasing-experience and pheb forms as these existing whole expressions. Retain their canonical English without changing Tibetan spelling or turning every neighboring snang ba into vision. No new glossary assignment is made.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-104",
    "pairs": [
      "DTG-001060",
      "DTG-001061",
      "DTG-001063",
      "DTG-001064",
      "DTG-001067",
      "DTG-001068",
      "DTG-001069",
      "DTG-001070",
      "DTG-001073",
      "DTG-001074",
      "DTG-001075",
      "DTG-001077"
    ],
    "ids": [
      "U02360",
      "U02361",
      "U02362",
      "U02363",
      "U02365",
      "U02366",
      "U02367",
      "U02368",
      "U02369",
      "U02370",
      "U02371",
      "U02376",
      "U02377",
      "U02378",
      "U02379",
      "U02380",
      "U02381",
      "U02382",
      "U02383",
      "U02384",
      "U02385",
      "U02390",
      "U02391",
      "U02392",
      "U02393",
      "U02394",
      "U02395",
      "U02396",
      "U02398",
      "U02399"
    ],
    "realization": "secret preliminary; key point; bodily bcud verb provisional",
    "status": "Approved labels with whole-construction and verbal controls",
    "reason": "Read the entire body/speech/mind sequence through its purposes and final negations. Bcud cing at U02366 is a queried bodily verb, not a noun to replace with quintessence. Mindful/mindfulness and reflection retain the distinct components and N-T48 psychological-sense qualification. No speech-nonreversal mechanism, flow referent or missing technique is supplied.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-107",
    "pairs": [
      "DTG-001113",
      "DTG-001114",
      "DTG-001115",
      "DTG-001116",
      "DTG-001117",
      "DTG-001118",
      "DTG-001119",
      "DTG-001120"
    ],
    "ids": [
      "U02465",
      "U02466",
      "U02467",
      "U02468",
      "U02469",
      "U02470",
      "U02471",
      "U02472",
      "U02473",
      "U02474",
      "U02475",
      "U02476",
      "U02477",
      "U02478",
      "U02479",
      "U02480"
    ],
    "realization": "transmission; ordinary mind itself; key points",
    "status": "Local intensive nyid analysis supported under I §8.1 U07",
    "reason": "The mind being tamed and entering the path, followed by body/ordinary-mind separation, supports the intensive ordinary mind itself, including the return at U02477. Preserve chos/phenomena there and lung/transmission at U02465. This does not create a shared sems nyid default. Life-tree, equal precipices and exact transmission relationship remain qualified; no physiological instruction is elaborated.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T22",
    "pairs": [
      "DTG-000332",
      "DTG-001115",
      "DTG-001119"
    ],
    "ids": [
      "U00687",
      "U00688",
      "U02469",
      "U02470",
      "U02471",
      "U02477",
      "U02478"
    ],
    "realization": "nature of ordinary mind (description, provisional); ordinary mind itself (operational sequence)",
    "status": "Source-sensitive family comparison; no book-wide synonym default",
    "reason": "The chapter-outline transmission complete in qualities beside the nature-of-phenomena heading retains its qualified lexicalized-nature possibility. The later mind being tamed, entering the path and mixed with phenomena is locally intensive. The historical proposal cannot make nature mandatory everywhere, and the local repairs do not make itself a shared default.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-108",
    "pairs": [
      "DTG-001122",
      "DTG-001123",
      "DTG-002667",
      "DTG-002668",
      "DTG-002669",
      "DTG-001125",
      "DTG-001126",
      "DTG-001127",
      "DTG-001128",
      "DTG-001129"
    ],
    "ids": [
      "U02482",
      "U02483",
      "U02484",
      "U02485",
      "U02486",
      "U02487",
      "U02488",
      "U02489",
      "SCAN-CH1-LAYER-02489",
      "U02490",
      "U02491",
      "U02492",
      "U02493",
      "U02494",
      "U02495",
      "U02496",
      "U02497",
      "U02498",
      "U02499"
    ],
    "realization": "conditional familiarity; preserved cross-heading genitive; karmic beings",
    "status": "Minimal condition/label repairs; source-positioned discontinuity retained",
    "reason": "The full phrase was read across the sixty-seventh heading. The genitive before the heading and result after it are source-continuous, not a reason to resegment. The unnamed fixings and strong exhaustion, embodiment/primordial-knowing and nonabiding negations are preserved. The small heading terminal remains uncertain; no annihilation thesis is inserted.",
    "review": "REVIEW.md#phase-d-notes-08"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-110",
    "pairs": [
      "DTG-001136",
      "DTG-001138",
      "DTG-001139",
      "DTG-001140",
      "DTG-001141",
      "DTG-001142",
      "DTG-001143",
      "DTG-001144",
      "DTG-001145",
      "DTG-001146",
      "DTG-001147",
      "DTG-001148"
    ],
    "ids": [
      "U02511",
      "U02512",
      "U02513",
      "U02515",
      "U02516",
      "U02517",
      "U02518",
      "U02519",
      "U02520",
      "U02521",
      "U02522",
      "U02523",
      "U02524",
      "U02525",
      "U02526",
      "U02527",
      "U02528",
      "U02529",
      "U02530",
      "U02531",
      "U02532",
      "U02533",
      "U02534",
      "U02535"
    ],
    "realization": "quintessence; literary tantra; historical claims still qualified",
    "status": "Approved labels in reviewed nourishment account",
    "reason": "The continuation through U02535 was read as context. The remaining matching DTG-001148 occurrence is queued for the next batch. The youthful reading is already source-selected. Splendor here is gzi brjid, not mdangs or gdangs; material substance classes and bodily constituents are not forcibly relabeled entities or modern tissues. Retain warnings and all unspecified preparations, measures and wind relations.",
    "review": "REVIEW.md#phase-d-notes-08"
  }
]
```

**Important no-change cases and rejected false positives:** The conditional Vajradhara row is not automatic proof that the instrumental guru designation names that figure. The natural-state virtue/misdeed assertions and all nonarising/nonabiding negations remain source claims. Zang ma/thal byung is not reconstructed as the different canonical whole expression. The general/particular, appropriation, grid and time measures remain qualified without a new diagram. The actual hearth/empty/emptiness/terminator clause is not emended to match the question or a more familiar means-expression.

The whole speaking/bad-news variant is separate; the restored perception and vajra-secret verses and fifty-seventh heading are present. Training/waves and the source-positioned sixty-seventh heading remain properly layered. Personal continua, the complete wind-mind expression, physical limbs, the four full vision labels and ordinary support versus philosophical Ground are not mechanically homogenized. Technical conviction is kept distinct from confidence, faith and confident devotion.

All fours, the two/five/eight groups, three twenty-onefold accounts, six capabilities/faults and three fixings retain their counts without invented members. No clinical assessment, preparation, breath duration, efficacy or authorization is supplied. The chapter-description sems nyid, self-awareness, own-knowing/awareness predicate, life-tree, dependent connections and six-capability wording retain their linked qualifications. The stronger ordinary-mind-itself analysis is local to the explicitly operational sequence, not a new shared label.

**Application, changed-clause self-check and validation:** All 62 English operations in 52 pairs were applied and reread against their exact current Tibetan in a 114-pair changed-clause/context view. Maturation recipients versus agents, instrumental relationships, the familiarity condition, all three intensive ordinary-mind occurrences, personal versus literary continua, names/honorifics and complete technical labels were rechecked. Number, negation, source roles and the remaining linked qualifications are preserved. Sixteen scoped append-only note/usage dispositions were applied; all 47 inherited dispositions remain unchanged. This is repair self-verification, not another independent review.

The final paired validator and projector check were actually rerun; both exit 1 at the historical protected-glossary contract. Full recorded-operation replay/integrity exits 0: all 2,667 pair identities/order, fixed source/golden/policy/format/lineage, inherited notes/history and 700 English local-link targets pass. Current totals are 246 operations: 225 English repairs in 201 distinct pairs and 21 review links, affecting 213 pair payloads including note-only changes. The separate annotation repair is unchanged. The usage file has 63 Phase D dispositions. English SHA-256: `2a21fc15d3f67ad01941a865b2ea1ee5cfea0b1989897bbedc1772bb5dd2bfcd`. `git diff --check` passes. The blocked projector produced no new reader output.

**Saved coverage:** 1,150/2,667 pairs, ordinals 1–1150 through DTG-001145, with 279 first-encountered note records. Continue at ordinal 1151 / DTG-001146. Ordinals 1151–1165 have additionally been read as connected context, not counted separately. Text remains provisional and the whole-work pass continues.


<a id="phase-d-batch-09"></a>
### Batch 09 — source ordinals 1151–1350

All **200 current pairs** were read in source order: Chapter 1 ordinals 1151–1199, including its colophon/inscription and split annotation carriers; Chapter 2 ordinals 1200–1350, including the full opening questions and connected twelve-root calculation. Context 1146–1150 and 1351–1360 was read without adding duplicate or advance coverage. All **39 first-encountered note records** and their current/historical prose, qualifications and source-annotation text were read; N-T65 and N-T78 were revisited. The actual golden source, not historical appendices, supplied the pair comparison. Full eight-column rows and I §8.1/III controls were applied alongside Q1–Q9.

**Evidence recorded before application:** 55 scoped English operations in 46 pairs and two active annotation-rendering operations below. Repeated terminology cases share their stated rationale. PD-B09-S01 corrects comparative rather than causal force. The independent review does not assert the unsettled conditional, number-grouping, byabyed or counted-gzhi constructions are correct; their exact spans and alternatives remain linked below.

<!-- phase-d-batch-09-operations -->
```json
[
  {
    "finding": "PD-B09-T01",
    "pair": "DTG-001148",
    "golden": [
      "U02534",
      "U02535"
    ],
    "tibetan": "དེ་ལྟར་བཅུད་ཀྱི་ལེན་པ་ཡིས། །\nའགྲོ་བའི་གདུང་བ་ཆོད་པའོ། །",
    "before": "vital essences",
    "after": "quintessence",
    "rationale": "P2 bcud in the same nourishment/extraction construction as the preceding reviewed reply; not the receptacle/inhabitants exception.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T01",
    "pair": "DTG-001154",
    "golden": [
      "U02548",
      "U02549"
    ],
    "tibetan": "ཡང་ནི་ལུས་འབྱུང་རྒྱུན་གཅོད་པའི། །\nབཅུད་ལེན་ངོ་མཚར་ཆེ་བ་བཤད། །",
    "before": "vital essences",
    "after": "quintessence",
    "rationale": "P2 bcud in the same nourishment/extraction construction as the preceding reviewed reply; not the receptacle/inhabitants exception.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T01",
    "pair": "DTG-001156",
    "golden": [
      "U02552",
      "U02553",
      "U02554"
    ],
    "tibetan": "ཡང་ན་བཅུད་ཕྱུང་མར་ཁུ་ནི། །\nཚད་དང་ལྡན་པ་བསྟེན་པ་ཡིས། །\nའབྱུང་བའི་རྒྱུན་རྣམས་ཆད་པར་འགྱུར། །",
    "before": "extracted vital essence",
    "after": "extracted quintessence",
    "rationale": "P2 bcud extraction label; the existing N-112 uncertainty about whether butter is coordinated with or modified by extraction remains, not resolved by this label repair.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001151",
    "golden": [
      "U02539",
      "U02540",
      "U02541",
      "U02542"
    ],
    "tibetan": "རླུང་ནི་འཕེན་ཞིང་སྡུད་པ་ལས། །\nའགྲོ་འོང་བསྐྱིལ་བའི་གནད་ཀྱི་ཡང༌། །\nདམིགས་པ་སོ་སོའི་འབྱུང་བ་དང༌། །\nརྣལ་འབྱོར་ལུས་ལ་མཐུན་པར་དབྱེ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001161",
    "golden": [
      "U02564",
      "U02565",
      "U02566"
    ],
    "tibetan": "གལ་ཏེ་འབྱུང་བ་བཞི་པོ་ལ། །\nརོ་སྙོམས་བྱེད་པའི་རྣལ་འབྱོར་པས། །\nས་ཆུ་མེ་རླུང་གནད་བསྟུན་ཏེ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001163",
    "golden": [
      "U02568",
      "U02569",
      "U02570"
    ],
    "tibetan": "རང་ལུས་སོ་སོའི་འབྱུང་བ་ཡིས། །\nབསྒྱུར་ཞིང་དེ་ཉིད་སྤྱོད་པ་ལ། །\nགནད་འདུས་དཀྱིལ་འཁོར་བསྒོམ་པར་བྱའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001175",
    "golden": [
      "U02593",
      "U02594",
      "U02595",
      "U02596"
    ],
    "tibetan": "རྟོག་མེད་ཡེ་ཤེས་བསྒོམ་པ་དང༌། །\nསྟོང་ཉིད་བསམ་དང་གནད་ཀྱིས་ཀྱང༌། །\nའབད་རྩོལ་མེད་པར་རྫུ་འཕྲུལ་རྣམས། །\nངེས་པར་འགྲུབ་པར་འགྱུར་བའོ།",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001194",
    "golden": [
      "U02644",
      "U02645"
    ],
    "tibetan": "སེམས་ཅན་ཁམས་གསུམ་འཁོར་བ་ལས། །\nགྲོལ་བར་བྱེད་པའི་གནད་ཉིད་གང༌། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001198",
    "golden": [
      "U02649"
    ],
    "tibetan": "སངས་རྒྱས་མ་འཁྲུལ་གནད་འདི་ཅི། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001203",
    "golden": [
      "U02654"
    ],
    "tibetan": "སྒྲོན་མའི་གནད་ནི་ཅི་ལྟ་བུ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001205",
    "golden": [
      "U02656"
    ],
    "tibetan": "ཡུལ་གྱི་གནད་ནི་གང་ལ་འཆར། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001207",
    "golden": [
      "U02658"
    ],
    "tibetan": "བློ་རིམ་གནད་ནི་ཅི་ལྟ་བུ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001213",
    "golden": [
      "U02664"
    ],
    "tibetan": "དེ་ཉིད་ཡེ་ཤེས་གནད་ཉིད་གང༌། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001216",
    "golden": [
      "U02667"
    ],
    "tibetan": "ཀུན་གཞི་ཆོས་སྐུ་གཉིས་གནད་གང༌། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001217",
    "golden": [
      "U02668"
    ],
    "tibetan": "སེམས་དང་ཡེ་ཤེས་གནད་ཉིད་ཅི། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001221",
    "golden": [
      "U02672"
    ],
    "tibetan": "རྩ་ཡི་གནད་ལ་དུ་ཙམ་ཞིག །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001247",
    "golden": [
      "U02727",
      "U02728",
      "U02729"
    ],
    "tibetan": "སྐྱེ་མཆེད་འཁོར་ལོ་དྲུག་གི་ཡང་། །\nཡུལ་དང་ཤེས་པ་དབང་པོའི་གནད། །\nསོ་སོའི་འཇུག་ཆ་བརྒྱད་གཉིས་དྲུག །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001289",
    "golden": [
      "U02798",
      "U02799"
    ],
    "tibetan": "དེ་ཡི་གནད་ནི་ཡུལ་ཡིན་ཏེ། །\nཡུལ་དང་སྟོང་པ་རིག་རྩལ་མཉམ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001291",
    "golden": [
      "U02801",
      "U02802"
    ],
    "tibetan": "ཡང་ནི་འཁྲུལ་པ་མིན་པའི་གནད། །\nགཅིག་ཤེས་པ་ཡིས་ཐམས་ཅད་གྲོལ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001323",
    "golden": [
      "U02868",
      "U02869",
      "U02870",
      "U02871",
      "U02872",
      "U02873",
      "U02874",
      "U02875"
    ],
    "tibetan": "སྨིན་བྱེད་ཐིག་ལེ་སོ་སོའི་གནད། །\nའགྱུ་བྱེད་རྟོག་པ་རགས་འཛིན་པ། །\nཡེ་ཤེས་སྣང་བ་བཞི་གཉིས་ཆ། །\nལས་འབྱུང་འཇུག་པའི་དབྱེ་བ་ལས། །\nཙིཏྟ་རིན་ཆེན་གཞལ་ཡས་སུ། །\nརིན་ཆེན་འདུས་པ་ཟུར་བརྒྱད་སྒོ། །\nཡེ་ཤེས་ལྔ་དང་སྐུ་ལྔ་སྟེ། །\nརླུང་ལྔ་ཤེས་པའི་རྩལ་ཡང་ལྔ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001325",
    "golden": [
      "U02877",
      "U02878"
    ],
    "tibetan": "སྐུ་ཡི་གནད་ནི་གདངས་ཀྱིས་སོ། །\nཡེ་ཤེས་འདུག་སྟངས་དག་གིས་སོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001328",
    "golden": [
      "U02881"
    ],
    "tibetan": "འབྲེལ་ལྡན་བསྡོམས་པས་རླུང་གི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001332",
    "golden": [
      "U02886",
      "U02887"
    ],
    "tibetan": "རིག་པའི་གནད་ནི་བྱུང་བ་དང་། །\nབསྐྱིལ་ཞིང་མཁའ་ལ་གཏད་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001335",
    "golden": [
      "U02890",
      "U02891"
    ],
    "tibetan": "དབྱིངས་ཀྱི་གནད་ནི་བསྡུ་བ་དང༌། །\nདགུག་དང་ཁམས་ཀྱི་བྱེར་ཡས་སྦྱར། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T02",
    "pair": "DTG-001336",
    "golden": [
      "U02892",
      "U02893"
    ],
    "tibetan": "སྣང་བའི་གནད་ནི་འཕེལ་དང་ཟད། །\nསྣ་ཚོགས་རང་སར་གྲོལ་བའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad: current full Tibetan supports the bodily/contemplative technical label, preserving number, modifiers, questions and source relationships.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T03",
    "pair": "DTG-001163",
    "golden": [
      "U02568",
      "U02569",
      "U02570"
    ],
    "tibetan": "རང་ལུས་སོ་སོའི་འབྱུང་བ་ཡིས། །\nབསྒྱུར་ཞིང་དེ་ཉིད་སྤྱོད་པ་ལ། །\nགནད་འདུས་དཀྱིལ་འཁོར་བསྒོམ་པར་བྱའོ། །",
    "before": "maṇḍala",
    "after": "mandala",
    "rationale": "P2 spelling for the named contemplative mandala, not a geometric disc; its identity and construction remain qualified in N-113.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T04",
    "pair": "DTG-001168",
    "golden": [
      "U02577",
      "U02578",
      "U02579"
    ],
    "tibetan": "མཛོད་ཀྱི་ཡོན་ཏན་འདི་ལྟ་སྟེ། །\nཐུན་མོང་མཆོག་གི་དངོས་གྲུབ་ལ། །\nཅི་དགར་རོལ་ཅིང་བདེ་བར་འགྲུབ། །",
    "before": "common and supreme accomplishments",
    "after": "common and supreme spiritual accomplishments",
    "rationale": "P2 complete dngos grub equivalent, retaining both common and supreme modifiers and not relabeling the separate generic accomplishing verb.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T05",
    "pair": "DTG-002672",
    "golden": [
      "U02616"
    ],
    "tibetan": "སྤྲོ་བསྡུ་བསྟིམ་འཁྱིལ་པས་བྱའོ། །",
    "before": "perform proliferating, gathering, absorbing, and coiling.",
    "after": "perform projecting, gathering, absorbing, and coiling.",
    "rationale": "P2 attested spro bsdu action pair, not the differently written established phro du. Read across DTG-002670 and the empty annotation carrier DTG-002671; all four actions and the imperative remain.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T06",
    "pair": "DTG-001188",
    "golden": [
      "U02621",
      "U02622",
      "U02623",
      "U02624",
      "U02625",
      "U02626"
    ],
    "tibetan": "སྟོན་པ་སངས་རྒྱས་བཅོམ་ལྡན་འདས། །\nཡོན་ཏན་ཐམས་ཅད་རང་རྫོགས་པས། །\nབརྗོད་ཅིང་གསུངས་པ་མ་ཡིན་པར། །\nརང་བྱུང་ཡེ་ཤེས་རོལ་པ་ལས། །\nསྒྲ་ཚིག་མིང་གི་ཆོ་འཕྲུལ་དུ། །\nསྐལ་བ་བཟང་པོ་རྣམས་ལ་སྣང་། །",
    "before": "as a miraculous display of words, phrases, and names,",
    "after": "as a magical display of words, phrases, and names,",
    "rationale": "Established cho phrul label; distinguish it from rdzu phrul miracles in the preceding replies. The nonutterance/display contrast is not paraphrased away.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T07",
    "pair": "DTG-001193",
    "golden": [
      "U02636",
      "U02637",
      "U02638",
      "U02639",
      "U02640",
      "U02641",
      "U02642",
      "U02643"
    ],
    "tibetan": "དེ་ནས་ལྷ་དབང་རྟོག་པ་མེད།།\nཆོས་ཀྱི་དབྱིངས་དང་དབྱེར་མེད་ཀྱང་། །\nམ་འོངས་དུས་ཀྱི་སེམས་ཅན་ལ། །\nརྟོགས་པས་ངེས་པར་འཁོར་བ་ལས། །\nབསྒྲལ་བར་བྱ་བའི་བློ་ཡིས་ཀྱང་། །\nསེམས་བསྐྱེད་སྔོན་དུ་བཏང་ནས་ནི། །\nསྟོན་པ་ཉིད་ལ་འདི་སྐད་ཞུས། །\nཀྱེ་ཀྱེ་བརྫུས་ནས་སྐྱེས་པའི་སྐུ།",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent in each actual source construction, preserving plural/possessive grammar. Bare sems and gro ba remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T07",
    "pair": "DTG-001194",
    "golden": [
      "U02644",
      "U02645"
    ],
    "tibetan": "སེམས་ཅན་ཁམས་གསུམ་འཁོར་བ་ལས། །\nགྲོལ་བར་བྱེད་པའི་གནད་ཉིད་གང༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent in each actual source construction, preserving plural/possessive grammar. Bare sems and gro ba remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T07",
    "pair": "DTG-001196",
    "golden": [
      "U02647"
    ],
    "tibetan": "སེམས་ཅན་འཁོར་བའི་ཐོག་མ་གང༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent in each actual source construction, preserving plural/possessive grammar. Bare sems and gro ba remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T07",
    "pair": "DTG-001199",
    "golden": [
      "U02650"
    ],
    "tibetan": "སེམས་ཅན་འཁྲུལ་པ་ཅི་ལས་བྱུང་། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent in each actual source construction, preserving plural/possessive grammar. Bare sems and gro ba remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T07",
    "pair": "DTG-001274",
    "golden": [
      "U02764",
      "U02765",
      "U02766"
    ],
    "tibetan": "སེམས་ཅན་ཁམས་ནི་དུ་མར་བཅས། །\nའཇུག་ཕྱིར་ལས་ཀུན་མཐར་སྤྱད་པ། །\nལྡན་པས་རྫོགས་ཏེ་ཉེར་བསྟན་པའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent in each actual source construction, preserving plural/possessive grammar. Bare sems and gro ba remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T07",
    "pair": "DTG-001278",
    "golden": [
      "U02773",
      "U02774",
      "U02775",
      "U02776",
      "U02777"
    ],
    "tibetan": "འདས་པ་གཞག་ཕྱིར་སེམས་ཅན་ཁམས། །\nརང་བཞིན་དུ་ཡང་འདི་ཉིད་ཡུལ། །\nགཞན་དབང་མ་ཡིན་ཡོངས་སུ་གྲུབ། །\nཀུན་བརྟགས་ལས་དང་བརྗོད་པས་སྟོང༌། །\nམཐའ་ལྡན་ཕྱེ་བ་མ་ཡིན་ནོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent in each actual source construction, preserving plural/possessive grammar. Bare sems and gro ba remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T07",
    "pair": "DTG-001299",
    "golden": [
      "U02814",
      "U02815",
      "U02816"
    ],
    "tibetan": "སེམས་ཅན་འཁྲུལ་པ་གོང་མ་ཡི། །\nརྩ་བའི་རྟེན་འབྲེལ་ལ་འཁྱལ་པས། །\nའཁྲུལ་འཁོར་རྩིས་ཀྱི་གཞི་མར་བྱུང༌། །",
    "before": "Sentient beings",
    "after": "Karmic beings",
    "rationale": "P2 complete sems can equivalent, with sentence-initial capitalization and the existing possessive preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001193",
    "golden": [
      "U02636",
      "U02637",
      "U02638",
      "U02639",
      "U02640",
      "U02641",
      "U02642",
      "U02643"
    ],
    "tibetan": "དེ་ནས་ལྷ་དབང་རྟོག་པ་མེད།།\nཆོས་ཀྱི་དབྱིངས་དང་དབྱེར་མེད་ཀྱང་། །\nམ་འོངས་དུས་ཀྱི་སེམས་ཅན་ལ། །\nརྟོགས་པས་ངེས་པར་འཁོར་བ་ལས། །\nབསྒྲལ་བར་བྱ་བའི་བློ་ཡིས་ཀྱང་། །\nསེམས་བསྐྱེད་སྔོན་དུ་བཏང་ནས་ནི། །\nསྟོན་པ་ཉིད་ལ་འདི་སྐད་ཞུས། །\nཀྱེ་ཀྱེ་བརྫུས་ནས་སྐྱེས་པའི་སྐུ།",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001194",
    "golden": [
      "U02644",
      "U02645"
    ],
    "tibetan": "སེམས་ཅན་ཁམས་གསུམ་འཁོར་བ་ལས། །\nགྲོལ་བར་བྱེད་པའི་གནད་ཉིད་གང༌། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001196",
    "golden": [
      "U02647"
    ],
    "tibetan": "སེམས་ཅན་འཁོར་བའི་ཐོག་མ་གང༌། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001227",
    "golden": [
      "U02685",
      "U02686",
      "U02687",
      "U02688",
      "U02689",
      "U02690",
      "U02691",
      "U02692"
    ],
    "tibetan": "རྟོག་པ་ཟད་པའི་ནམ་མཁའ་ལས། །\nསྒྲ་ཚིག་མིང་དུ་མ་བསྒྲགས་ཀྱང༌། །\nརང་བྱུང་ཡེ་ཤེས་ཆེན་པོ་ཉིད། །\nགདོད་ནས་བྱས་མེད་རང་བཞིན་ལས། །\nམ་བཀོད་ཚིག་ཏུ་འདི་ལྟར་ཤར། །\nའཁོར་བ་རྣམས་ཀྱི་ཐོག་མ་ནི། །\nམི་འབྱེད་བྱས་མེད་རང་གཞན་ལས། །\nདམིགས་པར་འཛིན་པའི་ཡུལ་ཤར་ཏེ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001229",
    "golden": [
      "U02694",
      "U02695"
    ],
    "tibetan": "དམིགས་འཛིན་འབྲེལ་པ་བཅུ་གཉིས་སུ། །\nའཁོར་བའི་ཐོག་མ་ཉིད་དུའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001232",
    "golden": [
      "U02699"
    ],
    "tibetan": "འདི་ཡང་འཁོར་བའི་ཐོག་མའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001273",
    "golden": [
      "U02763"
    ],
    "tibetan": "འདི་དག་འཁོར་བའི་ཐོག་མར་བྱུང་། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001277",
    "golden": [
      "U02769",
      "U02770",
      "U02771",
      "U02772"
    ],
    "tibetan": "མྱ་ངན་འདས་པའི་ཐ་མ་ནི། །\nའཁྲུལ་པའི་རྟོག་པ་ཀུན་ཟད་པས། །\nའཁོར་བའི་བྱེད་སྣང་མེད་ཚེ་ན། །\nརྟོག་ཟད་འཁྲུལ་པ་རང་སྣང་བས། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba; preserve the liberation, beginning or agency relationship rather than applying this to ordinary circling.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001244",
    "golden": [
      "U02721",
      "U02722",
      "U02723"
    ],
    "tibetan": "དེ་ཡང་མིང་གཟུགས་འཁྲུལ་པའི་ཆ། །\nམིང་ལས་གདགས་བཞི་དྲུག་ཅུ་གཉིས། །\nའཁོར་འདས་བཞི་དང་ཡི་གེར་བཅས། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 attested coordinated khor das; retain both members. The counted categories and their grouping are not resolved by the label correction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001281",
    "golden": [
      "U02782",
      "U02783",
      "U02784",
      "U02785"
    ],
    "tibetan": "དེ་ལྟར་འཁོར་འདས་ཐོག་མཐའ་ལས། །\nསངས་རྒྱས་འཁྲུལ་པར་མ་གྱུར་པས། །\nགཞི་ལས་འཕགས་པའི་དབང་པོ་ཡིས། །\nརང་སྣང་རང་བཞིན་མེད་པར་ཤེས། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 attested coordinated khor das; retain both members. The counted categories and their grouping are not resolved by the label correction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T08",
    "pair": "DTG-001278",
    "golden": [
      "U02773",
      "U02774",
      "U02775",
      "U02776",
      "U02777"
    ],
    "tibetan": "འདས་པ་གཞག་ཕྱིར་སེམས་ཅན་ཁམས། །\nརང་བཞིན་དུ་ཡང་འདི་ཉིད་ཡུལ། །\nགཞན་དབང་མ་ཡིན་ཡོངས་སུ་གྲུབ། །\nཀུན་བརྟགས་ལས་དང་བརྗོད་པས་སྟོང༌། །\nམཐའ་ལྡན་ཕྱེ་བ་མ་ཡིན་ནོ། །",
    "before": "To posit transcendence,",
    "after": "To posit transcendence [of sorrow],",
    "rationale": "The immediately preceding full mya ngan das pa at U02769 and repeated final-extent question U02648 establish the local short form. Supply the omitted component visibly; do not assign this to unrelated past-tense das.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B09-T09",
    "pair": "DTG-001193",
    "golden": [
      "U02636",
      "U02637",
      "U02638",
      "U02639",
      "U02640",
      "U02641",
      "U02642",
      "U02643"
    ],
    "tibetan": "དེ་ནས་ལྷ་དབང་རྟོག་པ་མེད།།\nཆོས་ཀྱི་དབྱིངས་དང་དབྱེར་མེད་ཀྱང་། །\nམ་འོངས་དུས་ཀྱི་སེམས་ཅན་ལ། །\nརྟོགས་པས་ངེས་པར་འཁོར་བ་ལས། །\nབསྒྲལ་བར་བྱ་བའི་བློ་ཡིས་ཀྱང་། །\nསེམས་བསྐྱེད་སྔོན་དུ་བཏང་ནས་ནི། །\nསྟོན་པ་ཉིད་ལ་འདི་སྐད་ཞུས། །\nཀྱེ་ཀྱེ་བརྫུས་ནས་སྐྱེས་པའི་སྐུ།",
    "before": "‘Kyé, kyé!",
    "after": "‘O, O!",
    "rationale": "P2 repeated vocative kye kye. Both calls, the quotation opening and the embodiment address remain; no separate listen verb is supplied.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T10",
    "pair": "DTG-001218",
    "golden": [
      "U02669"
    ],
    "tibetan": "འབྱུང་བ་དྭངས་སྙིགས་གང་གིས་འབྱེད། །",
    "before": "the clear and turbid aspects of the elements",
    "after": "the pure extract and residue of the elements",
    "rationale": "P2 attested dwangs snyigs whole pair; retain both members and their genitive relationship to the elements.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T10",
    "pair": "DTG-001343",
    "golden": [
      "U02909",
      "U02910"
    ],
    "tibetan": "མས་ནི་དྭངས་མ་སྡུད་པ་དང༌། །\nགོང་འོག་གནས་ཀྱི་གཞི་མ་བྱེད། །",
    "before": "gathers the refined parts",
    "after": "gathers the pure extract",
    "rationale": "P2 dwangs ma in the channel collection/extract context, with no separate part noun requiring the contextual exception. The ma wordplay and support clause remain.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T11",
    "pair": "DTG-001226",
    "golden": [
      "U02681",
      "U02682",
      "U02683",
      "U02684"
    ],
    "tibetan": "དེ་ནས་སྟོན་པ་རྡོ་རྗེ་འཆང་། །\nརང་བཞིན་སྤྲོས་མེད་རྫོགས་ཆེན་ལས། །\nསྒྲ་ཚིག་མིང་དུ་མི་གནས་ཀྱང་། །\nལྷ་དབང་ཉིད་ལ་འདི་སྐད་གསུངས། །",
    "before": "Then the teacher, the vajra-holder,",
    "after": "Then the teacher, Vajradhara,",
    "rationale": "P2 rdo rje chang designates the named teacher/speaker here. Unlike generic holding constructions and the distinct dzin spelling, this opening identifies the figure directly.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T12",
    "pair": "DTG-001227",
    "golden": [
      "U02685",
      "U02686",
      "U02687",
      "U02688",
      "U02689",
      "U02690",
      "U02691",
      "U02692"
    ],
    "tibetan": "རྟོག་པ་ཟད་པའི་ནམ་མཁའ་ལས། །\nསྒྲ་ཚིག་མིང་དུ་མ་བསྒྲགས་ཀྱང༌། །\nརང་བྱུང་ཡེ་ཤེས་ཆེན་པོ་ཉིད། །\nགདོད་ནས་བྱས་མེད་རང་བཞིན་ལས། །\nམ་བཀོད་ཚིག་ཏུ་འདི་ལྟར་ཤར། །\nའཁོར་བ་རྣམས་ཀྱི་ཐོག་མ་ནི། །\nམི་འབྱེད་བྱས་མེད་རང་གཞན་ལས། །\nདམིགས་པར་འཛིན་པའི་ཡུལ་ཤར་ཏེ། །",
    "before": "an object held as a focus arose.",
    "after": "an object held as an object of focus arose.",
    "rationale": "Established dmigs pa in the predicative dmigs par dzin pai yul construction: retain both the object (yul) and object-of-focus category. The earlier unmade/self-other attachment remains provisional in N-118.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-T13",
    "pair": "DTG-001295",
    "golden": [
      "U02807",
      "U02808"
    ],
    "tibetan": "བྱ་དང་བྱེད་པའི་བློ་མེད་པས། །\nཡུལ་རྐྱེན་སངས་པས་སངས་རྒྱས་སོ། །",
    "before": "conceptual mind of action and agent",
    "after": "conceptual mind of doing and the doer",
    "rationale": "P2 action/agent distinction in the expanded bya dang byed pai construction. Both roles and the absence of their conceptual mind remain; no named agent is added.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-S01",
    "pair": "DTG-001303",
    "golden": [
      "U02824",
      "U02825"
    ],
    "tibetan": "ཕྲ་བས་ཕྲ་འགྱུར་ཤེས་པ་ལས། །\nརྟོག་དཔྱོད་གཟུང་ཆ་གཉིས་སུ་སོང་། །",
    "before": "From knowing that becomes subtle through subtlety,",
    "after": "From knowing that becomes subtler than subtle,",
    "rationale": "The repeated adjective phra bas phra supports a comparative, not an asserted causal relation through subtlety. Retain knowing and the following twofold conceptual-examination/apprehended-portion clause. Other particle-sequence attachments remain qualified in N-124.",
    "severity": "moderate meaning",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B09-T14",
    "pair": "DTG-001323",
    "golden": [
      "U02868",
      "U02869",
      "U02870",
      "U02871",
      "U02872",
      "U02873",
      "U02874",
      "U02875"
    ],
    "tibetan": "སྨིན་བྱེད་ཐིག་ལེ་སོ་སོའི་གནད། །\nའགྱུ་བྱེད་རྟོག་པ་རགས་འཛིན་པ། །\nཡེ་ཤེས་སྣང་བ་བཞི་གཉིས་ཆ། །\nལས་འབྱུང་འཇུག་པའི་དབྱེ་བ་ལས། །\nཙིཏྟ་རིན་ཆེན་གཞལ་ཡས་སུ། །\nརིན་ཆེན་འདུས་པ་ཟུར་བརྒྱད་སྒོ། །\nཡེ་ཤེས་ལྔ་དང་སྐུ་ལྔ་སྟེ། །\nརླུང་ལྔ་ཤེས་པའི་རྩལ་ཡང་ལྔ། །",
    "before": "in the precious palace of the heart (citta),",
    "after": "in the precious palace of citta,",
    "rationale": "P2 retention for the exact tsitta form. The body/palace/eye context supports a possible heart interpretation but N-125 and N-T62 do not establish its referent. Remove only the asserted anatomical gloss; retain it as a provisional alternative in the notes.",
    "severity": "moderate interpretation",
    "confidence": "high"
  }
]
```

<!-- phase-d-batch-09-annotation-operations -->
```json
[
  {
    "finding": "PD-B09-N01",
    "note": "G-U02885",
    "linked_pair": "DTG-001331",
    "tibetan": "རྡོ་རྗེ་ལུ་གུ་རྒྱུད་གནས་ཙིཏྟ་ནས་སྒོ་མིག་ནས་ཡུལ་ནམ་མཁའ་ལ་ཡེ་ཤེས་དངོས་སུ་འཆར་རོ །",
    "before": "English: From their abode, the heart (citta), through the door of the eyes, primordial knowing actually arises as vajra chains in the object, space. Heart (citta) retains the earlier explicitly provisional bodily-context usage.",
    "after": "English: From their abode, citta, through the door of the eyes, primordial knowing actually arises as vajra chains in the object, space. Citta follows the adopted retention policy; the earlier heart identification remains a provisional possibility, not established by this annotation.",
    "rationale": "Same P2 retention boundary as PD-B09-T14, applied only to the active source-annotation rendering/commentary. Previous English and exact Tibetan/source qualifications remain unchanged.",
    "severity": "moderate interpretation",
    "confidence": "high"
  },
  {
    "finding": "PD-B09-N02",
    "note": "G-U02887",
    "linked_pair": "DTG-001332",
    "tibetan": "འདིའི་དུས་ན་རླུང་འདྲེན་པ། གནད་ཡིན་ནོ། །",
    "before": "English: At this time, drawing the wind is the crucial point. The note is assembled across the old U02887–U02889 fragments.",
    "after": "English: At this time, drawing the wind is the key point. The note is assembled across the old U02887–U02889 fragments.",
    "rationale": "P2 gnad in the separate source note. This does not revive the historical direction criticism: the current main clause already correctly follows the golden toward-space reading.",
    "severity": "minor terminology",
    "confidence": "high"
  }
]
```

<a id="phase-d-notes-09"></a>
#### Active-note dispositions and bounded unresolved questions

The following dated dispositions are appended to the existing legacy index and usage record after application. They do not rewrite the historical proposals or declare new shared glossary assignments. PD-Q09-01 through PD-Q09-04 identify four additional bounded construction questions; inherited unresolved spans and family proposals remain separately identified in their existing notes.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-110",
    "pairs": [
      "DTG-001148"
    ],
    "ids": [
      "U02534",
      "U02535"
    ],
    "realization": "quintessence",
    "status": "Queued matching occurrence now corrected",
    "reason": "The remaining nourishment/extraction occurrence at U02534 is reviewed in sequence and corrected. This closes the specific Batch 08 terminology queue, not the unidentified preparation or wind-reference questions.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-111",
    "pairs": [
      "DTG-001151",
      "DTG-001152"
    ],
    "ids": [
      "U02539",
      "U02540",
      "U02541",
      "U02542",
      "U02543",
      "U02544",
      "U02545",
      "U02546"
    ],
    "realization": "key points; numerical grouping retained provisionally",
    "status": "Label repaired; PD-Q09-01 remains open",
    "reason": "At U02544, གཉིས་དང་དྲུག་དང་བདུན་གསུམ་ལ། may enumerate two/six/seven/three or use gsum to sum the preceding three entries. The current four-number wording is provisional, not a settled total. A source-linked explanation of the counting syntax and referents would settle this. The elemental-object/yogin attachment is also still qualified; no preparation is reconstructed.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-112",
    "pairs": [
      "DTG-001154",
      "DTG-001156",
      "DTG-001157",
      "DTG-001158"
    ],
    "ids": [
      "U02548",
      "U02549",
      "U02552",
      "U02553",
      "U02554",
      "U02555",
      "U02556",
      "U02557",
      "U02558",
      "U02559",
      "U02560"
    ],
    "realization": "quintessence; extract/butter syntax retained provisionally",
    "status": "Approved label; existing construction questions retained",
    "reason": "The bcud labels change, but བཅུད་ཕྱུང་མར་ཁུ may coordinate extract and butter or describe an extracted butter preparation. The existing and/[these] treatment remains linked and provisional pending a secure construction/referent. Great odor, purity and cessation claims are retained as textual claims, not identified substances or verified physiological effects.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-113",
    "pairs": [
      "DTG-001161",
      "DTG-001162",
      "DTG-001163",
      "DTG-001164",
      "DTG-001168"
    ],
    "ids": [
      "U02564",
      "U02565",
      "U02566",
      "U02567",
      "U02568",
      "U02569",
      "U02570",
      "U02571",
      "U02572",
      "U02577",
      "U02578",
      "U02579"
    ],
    "realization": "key points; mandala; spiritual accomplishments",
    "status": "Labels repaired; PD-Q09-02 conditional scope unresolved",
    "reason": "The explicit གལ་ཏེ at U02564 is not represented by the current For the four elements opening. Its conditional scope may govern the ensuing coordinated actions or the practice case as a whole; inserting an if only before bringing the elements into accord would prematurely settle that scope. The exact U02564–U02570 construction remains provisional here, requiring syntactic confirmation across the three pairs. The corresponding treasury question DTG-000140 was reread and does not identify the treasury; that referent and the mandala identity remain open.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-114",
    "pairs": [
      "DTG-001173",
      "DTG-001174",
      "DTG-001175",
      "DTG-001177",
      "DTG-001179"
    ],
    "ids": [
      "U02585",
      "U02586",
      "U02587",
      "U02588",
      "U02589",
      "U02590",
      "U02591",
      "U02592",
      "U02593",
      "U02594",
      "U02595",
      "U02596",
      "U02598",
      "U02599",
      "U02601",
      "U02602",
      "U02603"
    ],
    "realization": "karmic wind; byabyed question; unspecified mechanism",
    "status": "Whole-entry status reconciled; PD-Q09-03 retained",
    "reason": "Las rlung is a recognizable short genitive compound in the karmic-wind context, not a newly authorized component reconstruction. At U02590, དཔེ་དང་བྱ་བྱེད་བསླབ་ཐབས་ལ།, the current actions compresses bya byed. Doing and the doer versus doing and making, and the attachment of training methods, require a source-supported choice; the list remains provisional, not silently approved as complete. The entity/nonentity supports are not matter/awareness; khrom, temporal counts and concealed object remain unresolved.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T59",
    "pairs": [
      "DTG-001174",
      "DTG-001330"
    ],
    "ids": [
      "U02588",
      "U02589",
      "U02590",
      "U02591",
      "U02592",
      "U02883",
      "U02884"
    ],
    "realization": "karmic wind",
    "status": "Locally supported short-form use of established entry",
    "reason": "The complete row las kyi rlung is established. Both las rlung occurrences in the reviewed miracle and movement sequence support the short form. The historical claim of no whole entry is not current policy; no global mapping of every las or every wind expression is created.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-115",
    "pairs": [
      "DTG-002670",
      "DTG-002671",
      "DTG-002672",
      "DTG-001188",
      "DTG-001191",
      "DTG-001192"
    ],
    "ids": [
      "U02613",
      "U02614",
      "U02615",
      "U02616",
      "U02621",
      "U02622",
      "U02623",
      "U02624",
      "U02625",
      "U02626",
      "U02634",
      "U02635",
      "A2000-C01-S09"
    ],
    "realization": "projecting and gathering; magical display; preserved title/layers",
    "status": "Supported repairs; source qualifications retained",
    "reason": "The four-action instruction continues across its empty source-annotation carrier without resegmentation. Source variants at U02615 and U02620 remain separate; the chapter-title rang byung attachment remains qualified. The boundary inscription is the same represented object as old S0002, not a second missing passage.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-117",
    "pairs": [
      "DTG-001193",
      "DTG-001194",
      "DTG-001218",
      "DTG-001224",
      "DTG-001225"
    ],
    "ids": [
      "U02636",
      "U02637",
      "U02638",
      "U02639",
      "U02640",
      "U02641",
      "U02642",
      "U02643",
      "U02644",
      "U02645",
      "U02669",
      "U02675",
      "U02676",
      "U02677",
      "U02678",
      "U02679",
      "U02680"
    ],
    "realization": "karmic beings; O, O; key points; extract/residue",
    "status": "Approved labels; abbreviated intention and question relations remain qualified",
    "reason": "The future-time addressees, realization/instrument, request and quotation boundaries were read continuously through the complete question list. Sems bskyed is not automatically identified with a physiological substance or expanded into bodhicitta from components. The current arousing ordinary mind is a linked provisional construction; an established whole-expression sense in this introduction is needed to settle it. Lamp-packing/stages questions require their subsequent replies. The seventeen-subdivision statement is already a separate annotation.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T57",
    "pairs": [
      "DTG-001193",
      "DTG-001208"
    ],
    "ids": [
      "U02636",
      "U02637",
      "U02638",
      "U02639",
      "U02640",
      "U02641",
      "U02642",
      "U02643",
      "U02659"
    ],
    "realization": "arousing ordinary mind; taken up in experience",
    "status": "Local construction proposals remain provisional",
    "reason": "Keep the introductory intention and practice question distinct. Ordinary-mind and experience components alone do not prove the whole constructions; no new shared default is adopted. Corresponding replies and an explicit construction decision, rather than component substitution, would settle them.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T61",
    "pairs": [
      "DTG-001197",
      "DTG-001277",
      "DTG-001278"
    ],
    "ids": [
      "U02648",
      "U02769",
      "U02770",
      "U02771",
      "U02772",
      "U02773",
      "U02774",
      "U02775",
      "U02776",
      "U02777"
    ],
    "realization": "passing beyond [sorrow]; transcendence [of sorrow]",
    "status": "Local short-form identity supported",
    "reason": "The repeated final-extent wording and the full mya ngan das pa in U02769 establish the short forms at U02648 and U02773 in this reply. The absent sorrow component remains bracketed. This does not settle the reply remainder or authorize the same reading for all past/transcending expressions; U02972 is outside this batch.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T58",
    "pairs": [
      "DTG-001230",
      "DTG-001234",
      "DTG-001236"
    ],
    "ids": [
      "U02696",
      "U02703",
      "U02707",
      "U02708",
      "U02709",
      "U02710"
    ],
    "realization": "co-emergent [ignorance]; [imputing ignorance]",
    "status": "Local abbreviated-category relation supported",
    "reason": "The explicit three-ignorance introduction directly governs these subsequent categories. The bracketed supplied noun and the exact brtags spelling remain; four conditions and numerical assignments remain qualified. Unrelated co-emergent/imputed constructions are not assigned these labels.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T56",
    "pairs": [
      "DTG-001238",
      "DTG-001244",
      "DTG-001247",
      "DTG-001249",
      "DTG-001252",
      "DTG-001255",
      "DTG-001257",
      "DTG-001261"
    ],
    "ids": [
      "U02712",
      "U02713",
      "U02714",
      "U02721",
      "U02722",
      "U02723",
      "U02727",
      "U02728",
      "U02729",
      "U02731",
      "U02732",
      "U02735",
      "U02739",
      "U02740",
      "U02743",
      "U02747",
      "U02748"
    ],
    "realization": "formations; name-and-form; sense bases; contact; feeling; craving; grasping; becoming",
    "status": "Contextual category proposals retained for shared reconciliation",
    "reason": "The entire twelve-root calculation through U02766 was read. These eight distinct link-category proposals are locally plausible, not newly shared assignments. Counts, agency and arithmetic are not imported from a textbook list. Grasping here is len pa, not a competing default for dzin or taking-up-in-experience.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-120",
    "pairs": [
      "DTG-001257"
    ],
    "ids": [
      "U02743"
    ],
    "realization": "Grounds versus bases; numerical grouping",
    "status": "PD-Q09-04 remains open",
    "reason": "At ལེན་པའི་འཁྲུལ་གཞི་བཅུ་གསུམ་དྲུག, the counted gzhi may be grounds/bases of the grasping-delusion calculation rather than multiple technical Grounds. Current capitalization is retained provisionally, not certified by P1. A construction-level identification of the counted items and the 13/6 versus 10/3/6 grouping is required; lowercasing solely from an English substring would not settle it.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T67",
    "pairs": [
      "DTG-001296"
    ],
    "ids": [
      "U02809",
      "U02810"
    ],
    "realization": "deep absorption",
    "status": "Recognizable local short form supported",
    "reason": "Ting dzin is the shortened ting nge dzin in this complete-absorption predicate. It remains distinct from bsam gtan, cultivation and equipoise; no arbitrary dzin expansion is allowed.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-124",
    "pairs": [
      "DTG-001303",
      "DTG-001304",
      "DTG-001307",
      "DTG-001312"
    ],
    "ids": [
      "U02824",
      "U02825",
      "U02826",
      "U02830",
      "U02831",
      "U02832",
      "U02841",
      "U02842",
      "U02843",
      "U02844"
    ],
    "realization": "comparative subtlety; unresolved particle/knowing attachments",
    "status": "Comparative repaired; broader interpretation retained provisionally",
    "reason": "Phra bas phra is comparative, so the causal through subtlety is replaced by subtler than subtle. The subtle-particle primordial-knowing phrase, aggregation agents and the counted elemental classes remain unresolved, not a modern material or cognitive model. Gzhi at U02841 retains its technical Ground reading; the ordinary-support uses are separately scoped.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T69",
    "pairs": [
      "DTG-001299",
      "DTG-001343"
    ],
    "ids": [
      "U02814",
      "U02815",
      "U02816",
      "U02909",
      "U02910"
    ],
    "realization": "foundation",
    "status": "Local ordinary-support constructions retained",
    "reason": "Gzhi ma is the support of a calculation at U02816 and the upper/lower abodes at U02910. These constructions support foundation rather than automatically technical Ground. This does not adjudicate the different counted gzhi at U02743 or technical U02841.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T66",
    "pairs": [
      "DTG-001314"
    ],
    "ids": [
      "U02850",
      "U02851"
    ],
    "realization": "environment and its inhabitants",
    "status": "P2 contextual exception now applicable",
    "reason": "The complete snod dang bcud receptacle/contents pair refers here to environment and inhabitants. P2 expressly allows that context; this is not a global bcud assignment and does not revert the extraction-context quintessence repairs.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T65",
    "pairs": [
      "DTG-001218",
      "DTG-001320",
      "DTG-001321",
      "DTG-001343"
    ],
    "ids": [
      "U02669",
      "U02860",
      "U02861",
      "U02862",
      "U02863",
      "U02864",
      "U02865",
      "U02909",
      "U02910"
    ],
    "realization": "pure extract and residue; pure extract; splendor distinctions",
    "status": "P2 extract labels applied; mdangs-family proposal not promoted",
    "reason": "The technical extract/residue pair and dwangs ma collection use follow P2. The bkrag/gzi mdangs pair at U02860 and local mdangs repetition at U02865 retain luster/splendor provisionally, while gdangs remains radiance. The shared luster preference does not automatically collapse all three forms; their family realization requires cross-work reconciliation.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-125",
    "pairs": [
      "DTG-001323",
      "DTG-001331"
    ],
    "ids": [
      "U02868",
      "U02869",
      "U02870",
      "U02871",
      "U02872",
      "U02873",
      "U02874",
      "U02875",
      "U02885"
    ],
    "realization": "citta",
    "status": "P2 retention applied in root and current source-note rendering",
    "reason": "The precious palace/body/eye passage does not securely establish an anatomical heart referent. Citta is retained; heart remains an explained provisional alternative. Four/two grouping, eight-corner/door attachment and the final delusion-arrangement relation remain open. All fivefold components and explicit numbers remain.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T62",
    "pairs": [
      "DTG-001323",
      "DTG-001331"
    ],
    "ids": [
      "U02868",
      "U02869",
      "U02870",
      "U02871",
      "U02872",
      "U02873",
      "U02874",
      "U02875",
      "U02885"
    ],
    "realization": "citta",
    "status": "Historical heart proposal retained as a possibility, not current default",
    "reason": "P2 retention replaces heart (citta) in the reviewed root and source-note occurrence. This changes no Tibetan or historical Previous English and does not adjudicate the eye/caksu or buffalo proposals at later unreviewed occurrences.",
    "review": "REVIEW.md#phase-d-notes-09"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-126",
    "pairs": [
      "DTG-001332",
      "DTG-001333",
      "DTG-001334",
      "DTG-001335"
    ],
    "ids": [
      "U02886",
      "U02887",
      "U02888",
      "U02889",
      "U02890",
      "U02891"
    ],
    "realization": "toward space; key point",
    "status": "Historical direction criticism rejected against current golden source",
    "reason": "The selected main bskyil zhing mkha la gtad already supports toward space; the joined/annotation anchors correctly add no second root clause. Small rig pa remains a qualified gloss/intended-addition question. Only gnad in the active gloss becomes key point. Elements dispersal/spreading and the supplied object remain provisional; no new source reading is claimed.",
    "review": "REVIEW.md#phase-d-notes-09"
  }
]
```

**Important justified no-change cases:** rdzu phrul remains miracles, distinct from cho phrul magical display. Nonliterary circling remains distinct from khor ba cyclic existence. Karmic beings is not extended to bare ordinary mind or every being expression. Entity/nonentity supports are not automatically the matter/awareness contrast. The paired environment/inhabitants expression uses P2's bcud exception. Ordinary support-foundation, local ignorance and deep-absorption short forms are construction-scoped, not new book defaults. The ultimate/relative two-truth and bodily pairs at DTG-001235, DTG-001322 and DTG-001340 remain provisional under the unsettled U10 family control; superficial/superfactual is not silently promoted to a shared rule. Channel names and their ma syllabic play are retained, without substituting Sanskrit identities or equating Kundarma with the separately named central channel. No counts, substances, dosage, practical physiology or anatomical identification is supplied.

**Current-source false positives rejected:** U02597's heading already follows the selected correction; U02615/U02620/U02680 are separate annotations; the boundary inscription is represented once; the hundred/eight and byas-tshe/tshogs-kyang distinctions already follow the current golden layers. The U02887 direction correction is already present, and U02888/U02889 correctly preserve joined/annotation roles rather than duplicate main text. The chapter-title and tiny-note qualifications remain, not re-deciphered here.

**Application and changed-clause verification (same-reviewer self-check):** all 55 recorded English operations in 46 pairs, the two active annotation operations and 21 append-only note/usage dispositions are applied. Every changed clause was reread with its exact current Tibetan and necessary neighbors (114 pairs in the explicit repair-context read), and all 200 revised English pairs were read continuously. Both full active source annotations were reread after application, including their untouched Tibetan, Previous English and source qualifications. The comparative preserves the following subject relationship without adding a cause; the citta correction removes only an unestablished gloss, and both agency roles, explicit counts, negations and modifiers remain. Four newly identified construction questions remain linked and provisional; they are not certified by coverage completion.

**Actual checks after Batch 09:** the custom read-only integrity replay passes all **301** recorded pair operations from frozen main, including **280 English operations in 247 pairs**, 21 review-link operations, and **259 changed pairs including note-only changes**. Two new recorded annotation operations replay exactly from the continuation input; the previously recorded annotation repair is preserved (three annotation operations cumulatively). All 2,667 ordered source/English IDs, fixed Tibetan/golden/policy/format/lineage bytes, inherited note associations, original usage and legacy history, and all **700** English local-link targets pass. `git diff --check` passes. Current English SHA-256: `7612d20e24cba7df262ab58bbc5bf5b67b489374662bac54840a95715f602404`.

The existing `python3 -B paired/test_paired.py` was actually rerun: **64 tests, 53 pass, 9 fail, 2 error; exit 1**. The errors and failed expected-rejection tests encounter the historical exact-English gate at DTG-000002 before their intended checks, as on the continuation input; these are not counted as passing controls. `python3 -B paired/validate.py --require-final`, `python3 -B paired/project.py --check`, and an actual `python3 -B paired/project.py` regeneration attempt each exit **1** at the protected old-glossary check. The projector writes supporting manifest/audit reports, not a newly configurable English reader; validation fails before any generated write. No dependent reader or report was regenerated, and no old release contract was modified. A bundled check command was blocked before execution; only the successfully executed individual commands above are claimed. The 63 semantic regression specifications were not run as tests.

**Coverage checkpoint:** 1,350/2,667 pairs; Chapter 1 all 1,199 covered, Chapter 2 first 151 covered. **318 first-encountered note records** have been read cumulatively. Continue at ordinal **1351, DTG-001344**; context already read through 1360 does not itself count as completed review. Text remains in review and is not ready for whole-work acceptance.


<a id="phase-d-batch-10"></a>
### Batch 10 — source ordinals 1351–1550

**Pre-edit input:** clean local and remotely verified `df033a6d86702e2cf4b140dd80434caa0c040691`, same reviewer DTG-PD-20261005-Astra-04 and frozen policies. All **200 current Tibetan–English pairs** were read in source order, with all **29 first-encountered note records** in their current and historical layers. Existing N-127 and related family notes were revisited. Context 1551–1580 was read, including the explicitly requested U03306–15 comparison, without advance coverage. Full eight-column glossary rows, Q1–Q9, I §8.1 and III controls govern the findings below.

**Evidence before application:** 51 English operations in 45 pairs, one active source-note Current English consistency correction, and 27 append-only note/usage dispositions. Local genitive, instrumental and shared-head repairs are distinguished from approved labels and still-provisional shared families.

<!-- phase-d-batch-10-operations -->
```json
[
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001344",
    "golden": [
      "U02911"
    ],
    "tibetan": "འདི་ལ་བསྐྱིལ་ཞིང་གཏེམས་པ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001346",
    "golden": [
      "U02914"
    ],
    "tibetan": "དྲོད་ཐོབ་འདོད་ན་མཉེ་བ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001351",
    "golden": [
      "U02922"
    ],
    "tibetan": "འདི་ལས་གསེང་ཞིང་མཉེ་བ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001360",
    "golden": [
      "U02934",
      "U02935"
    ],
    "tibetan": "འདི་ཡི་ཡན་ལག་བཅུ་གཉིས་ལ། །\nགསེང་ཞིང་འདྲིལ་བ་གནད་ཡིན་ནོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001373",
    "golden": [
      "U02959",
      "U02960",
      "U02961"
    ],
    "tibetan": "མངོན་སུམ་པ་དང་རང་གནད་ཀྱིས། །\nཆོས་ཉིད་དག་པའི་རང་སྣང་ཡུལ། །\nརྟོག་བཅས་འགགས་པར་གནས་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001384",
    "golden": [
      "U02979",
      "U02980",
      "U02981",
      "U02982"
    ],
    "tibetan": "དབྱིངས་ཀྱི་དྭངས་མ་སྡུད་པ་དང༌། །\nརིག་པའི་སྐུ་རྣམས་འཛིན་པ་དང༌། །\nགནད་གསུམ་བཅུད་དུ་སྨིན་པ་ཡིས། །\nའཁོར་བ་ཉིད་ནི་སྤོང་བར་བྱེད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001385",
    "golden": [
      "U02983",
      "U02984",
      "U02985"
    ],
    "tibetan": "དེ་ལྟར་མིག་ལས་སྒྲོན་ཤར་བས། །\nསངས་རྒྱས་དགོངས་པའི་གནད་འདུས་པར། །\nརང་སྣང་ཡུལ་རྣམས་འཛིན་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001387",
    "golden": [
      "U02987"
    ],
    "tibetan": "སྒྲོན་མའི་གནད་ནི་ངས་བཤད་ཀྱིས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001389",
    "golden": [
      "U02989",
      "U02990",
      "U02991",
      "U02992"
    ],
    "tibetan": "ཡུལ་དང་རིག་པ་རླུང་དག་གིས། །\nཆོས་ཉིད་ལམ་དུ་བཟུང་བའི་ཕྱིར། །\nཡེ་ཤེས་རྫོགས་པའི་ཆོས་ཉིད་དག །\nའདི་ཡང་སྒྲོན་མའི་གནད་ཡིན་ནོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001390",
    "golden": [
      "U02993"
    ],
    "tibetan": "རྒྱང་ཞགས་འགུལ་པ་མེད་པ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001392",
    "golden": [
      "U02995"
    ],
    "tibetan": "ཤེས་རབ་སྒྲོན་མ་སྦྱང་བའི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001393",
    "golden": [
      "U02996",
      "U02997"
    ],
    "tibetan": "ཆོ་ག་གསུམ་གྱིས་སྤེལ་བ་དང་། །\nབསྒྲུབ་པའི་གནད་ཀྱིས་རྒྱ་ཉིད་བསྐྱེད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001394",
    "golden": [
      "U02998"
    ],
    "tibetan": "ཐིག་ལེའི་སྒྲོན་མ་གཏེམས་པ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001396",
    "golden": [
      "U03001"
    ],
    "tibetan": "དབྱིངས་ཀྱི་གནད་ནི་འཁྲིད་པ་སྟེ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001401",
    "golden": [
      "U03011"
    ],
    "tibetan": "འདི་དུས་ཐབས་ཀྱིས་བཅོས་པ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001425",
    "golden": [
      "U03057",
      "U03058",
      "U03059"
    ],
    "tibetan": "འདི་ཉིད་ཡུལ་གནད་འདི་ལྟ་སྟེ། །\nསྤྲིན་བྲལ་ཕྱི་ཡུལ་སྟོང་པ་ལ། །\nརྣལ་འབྱོར་ནམ་མཁའི་བྱ་ལམ་གནས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001434",
    "golden": [
      "U03070",
      "U03071",
      "U03072"
    ],
    "tibetan": "གནད་ཀྱིས་བཅིང་དང་བཞག་པ་དང༌། །\nདངོས་པོ་བསྒྱུར་དང་རྩ་བ་བཅད། །\nའདྲེན་ཅིང་གཟུགས་ལ་བསླབ་པར་བྱའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001461",
    "golden": [
      "U03135",
      "U03136",
      "U03137",
      "U03138",
      "U03139"
    ],
    "tibetan": "བློ་རིམ་གནད་ནི་འདི་ལྟ་སྟེ། །\nའབྱུང་བ་སྣོད་ཀྱི་ཁྱད་པར་ལས། །\nའབྱུང་བའི་སྨིན་སོའི་ཁྱད་པར་གྱིས། །\nའགྲོ་བའི་བློ་ཡི་བྱེ་བྲག་གིས། །\nརིགས་དང་དབང་པོ་ཐ་དད་དོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001492",
    "golden": [
      "U03193",
      "U03194"
    ],
    "tibetan": "ཉམས་སུ་ལེན་པའི་གནད་འདིའོ། །\nདམིགས་རྟེན་ཉིད་དང་བསམ་གནས་སོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T01",
    "pair": "DTG-001526",
    "golden": [
      "U03249",
      "U03250"
    ],
    "tibetan": "རང་གསལ་གནས་པའི་སེམས་དེ་ནི། །\nགནད་ཀྱིས་གྲོལ་བས་ཕྱོགས་རིས་མིན། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual bodily/contemplative key-point construction. Keep source number, the surrounding predicates and the separately qualified physical instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T02",
    "pair": "DTG-001354",
    "golden": [
      "U02927"
    ],
    "tibetan": " དམ་ཚིག་གིས་ནི་རབ་བརྟག་གོ། །",
    "before": "through the pledge.",
    "after": "through the sacred pledge.",
    "rationale": "P2 whole dam tshig equivalent; retain the bracketed unspecified subject. The corrected golden source excludes the smaller water alternative from the main clause.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T03",
    "pair": "DTG-001350",
    "golden": [
      "U02920",
      "U02921"
    ],
    "tibetan": "མས་ནི་སྙིགས་མ་སེལ་བ་དང༌། །\nངོ་བོའི་གཟི་མདངས་བསྐྱེད་པའོ། །",
    "before": "clears away the turbid parts",
    "after": "clears away the residue",
    "rationale": "The explicit channel account pairs collection of dwangs ma at U02909 with clearing snyigs ma at U02920. This locally identifies the residue member of the established extract/residue pair; no separate part noun requires the old paraphrase, and the ma wordplay remains.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-S01",
    "pair": "DTG-001367",
    "golden": [
      "U02944",
      "U02945",
      "U02946"
    ],
    "tibetan": " ཡེ་ཤེས་འཆར་བའི་སྒོ་ཉིད་ནི། །\nལུས་བཅུད་དྭངས་མ་ཀུན་འདུས་པའི། །\nཙཀྵུ་ཞེས་པའི་སྒོ་ལས་འཐོན། །",
    "before": "the gathering of all refined bodily vital essence\nemerges through the door called cakṣu (‘eye’).",
    "after": "[primordial knowing] emerges through the door called cakṣu (‘eye’),\nwhere all the pure extract of the body’s quintessence is gathered.",
    "rationale": "At U02945 the genitive kun dus pai attaches the gathering clause to the door (sgo), rather than making the gathering the emerging subject. U02944 supplies primordial knowing, visibly repeated in brackets, and U02983 explicitly identifies the eyes. P2 pure extract and quintessence preserve both distinct source expressions. The nested bodily-extract description is local grammar, not a newly assigned technical compound; the two/five anatomical referents remain provisional.",
    "severity": "moderate meaning",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-T03",
    "pair": "DTG-001384",
    "golden": [
      "U02979",
      "U02980",
      "U02981",
      "U02982"
    ],
    "tibetan": "དབྱིངས་ཀྱི་དྭངས་མ་སྡུད་པ་དང༌། །\nརིག་པའི་སྐུ་རྣམས་འཛིན་པ་དང༌། །\nགནད་གསུམ་བཅུད་དུ་སྨིན་པ་ཡིས། །\nའཁོར་བ་ཉིད་ནི་སྤོང་བར་བྱེད། །",
    "before": "Gathering the refined part of basic space,",
    "after": "Gathering the pure extract of basic space,",
    "rationale": "P2 dwangs ma collection context: no separate part noun requires the contextual exception. Basic space remains its genitive, and the following subject stays provisionally linked in N-129.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T04",
    "pair": "DTG-001384",
    "golden": [
      "U02979",
      "U02980",
      "U02981",
      "U02982"
    ],
    "tibetan": "དབྱིངས་ཀྱི་དྭངས་མ་སྡུད་པ་དང༌། །\nརིག་པའི་སྐུ་རྣམས་འཛིན་པ་དང༌། །\nགནད་གསུམ་བཅུད་དུ་སྨིན་པ་ཡིས། །\nའཁོར་བ་ཉིད་ནི་སྤོང་བར་བྱེད། །",
    "before": "into vital essence,",
    "after": "into quintessence,",
    "rationale": "P2 bcud concentration/maturation context, distinct from the preceding pure extract and from essence.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T04",
    "pair": "DTG-001489",
    "golden": [
      "U03187"
    ],
    "tibetan": "དེས་ནི་འབྱུང་བས་བཅུད་བསྐྱབས་ཏེ། །",
    "before": "protect the vital essence.",
    "after": "protect the quintessence.",
    "rationale": "P2 bcud in the bodily preservation/concentration context. The later vessel simile does not itself make this the distinct snod bcud environment/inhabitants expression; the particular substance/referent remains unspecified.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001406",
    "golden": [
      "U03019",
      "U03020",
      "U03021",
      "U03022"
    ],
    "tibetan": "སྒྲོན་མའི་མཚན་ཉིད་འདི་ལྟ་སྟེ། །\nསྤྱིར་ཡང་སྣང་བ་སྟོན་པ་དང་། །\nཡེ་ཤེས་མ་བུར་སྦྲེལ་བར་བྱེད། །\nའཁོར་འདས་ས་མཚམས་སྦྱོར་བའོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 attested khor das contrast, retaining both coordinated members and the boundary/life-force/tether/seed/aim relation of each complete source construction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001412",
    "golden": [
      "U03031",
      "U03032",
      "U03033",
      "U03034"
    ],
    "tibetan": "ཤེས་རབ་དག་གི་མཚན་ཉིད་ནི། །\nགསལ་བའི་ཚིག་འཇུག་གཞི་མ་སྡུད། །\nཉོན་མོངས་ལས་དང་བག་ཆགས་བསྲེག །\nསྨིན་བྱེད་འཁོར་འདས་སྲོག་གཅོད་པའོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 attested khor das contrast, retaining both coordinated members and the boundary/life-force/tether/seed/aim relation of each complete source construction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001423",
    "golden": [
      "U03054",
      "U03055"
    ],
    "tibetan": "གཟུང་འཛིན་འཕྲང་ལ་བརྒལ་ནས་ནི། །\nའཁོར་འདས་གདོས་ཐག་ཆོད་པའོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 attested khor das contrast, retaining both coordinated members and the boundary/life-force/tether/seed/aim relation of each complete source construction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001446",
    "golden": [
      "U03094",
      "U03095",
      "U03096"
    ],
    "tibetan": "ཡེ་ཤེས་དག་པའི་སྒྲོན་མའི་རྟེན། །\nསྤྱིར་ནི་རྟེན་དང་བརྟེན་པ་ཡིས། །\nའཁོར་འདས་ས་བོན་འཕེལ་བར་བྱེད། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 attested khor das contrast, retaining both coordinated members and the boundary/life-force/tether/seed/aim relation of each complete source construction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001456",
    "golden": [
      "U03124",
      "U03125"
    ],
    "tibetan": "ཡེ་ཤེས་དག་པའི་སྐུ་མཐོང་ནས། །\nའཁོར་འདས་གཉིས་ཀྱི་འདུན་ས་འཇིག །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 attested khor das contrast, retaining both coordinated members and the boundary/life-force/tether/seed/aim relation of each complete source construction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001384",
    "golden": [
      "U02979",
      "U02980",
      "U02981",
      "U02982"
    ],
    "tibetan": "དབྱིངས་ཀྱི་དྭངས་མ་སྡུད་པ་དང༌། །\nརིག་པའི་སྐུ་རྣམས་འཛིན་པ་དང༌། །\nགནད་གསུམ་བཅུད་དུ་སྨིན་པ་ཡིས། །\nའཁོར་བ་ཉིད་ནི་སྤོང་བར་བྱེད། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba, including the recognizable liberation-from-khor short form at U03067; ordinary circling and different source words remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001431",
    "golden": [
      "U03067"
    ],
    "tibetan": "རྟོག་མཐའ་ཟད་ཕྱིར་འཁོར་ལས་གྲོལ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba, including the recognizable liberation-from-khor short form at U03067; ordinary circling and different source words remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001454",
    "golden": [
      "U03118",
      "U03119",
      "U03120",
      "U03121"
    ],
    "tibetan": "ལས་དང་བག་ཆགས་དག་བྱེད་པས། །\nཆོས་ཉིད་མངོན་སུམ་སྣང་བ་ལ། །\nབརྟེན་པས་འཁོར་བ་དོང་སྤྲུགས་ཏེ། །\nམྱང་འདས་མཚམས་སུ་རེག་ནུས་པའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba, including the recognizable liberation-from-khor short form at U03067; ordinary circling and different source words remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001455",
    "golden": [
      "U03122",
      "U03123"
    ],
    "tibetan": "རྟོག་དཔྱོད་ཟད་པའི་སེམས་ཉིད་ཀྱིས། །\nའཁོར་བ་རྒྱང་དུ་འཕངས་པ་ཡིས། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 technical khor ba, including the recognizable liberation-from-khor short form at U03067; ordinary circling and different source words remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T05",
    "pair": "DTG-001381",
    "golden": [
      "U02972",
      "U02973",
      "U02974"
    ],
    "tibetan": "འདས་པའི་ལམ་གྱི་སྣ་བཟུང་ནས། །\nརླུང་གིས་བཀྲག་དང་གཟི་མདངས་བསྐྱེད། །\nབསྒྱུར་ཅིང་ཡེ་ཤེས་སྣང་བ་སྟོན་པའོ། །",
    "before": "the path of transcendence,",
    "after": "the path of transcendence [of sorrow],",
    "rationale": "The explicitly introduced lamp/release sequence reaches abandoning khor ba at U02982 and the coordinated khor das boundary at U03022. That context supports this local short das identity; the missing component is bracketed. This is not a general assignment of every isolated das or past tense.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-T06",
    "pair": "DTG-001419",
    "golden": [
      "U03047",
      "U03048",
      "U03049"
    ],
    "tibetan": "དཀྱིལ་འཁོར་རྫོགས་པའི་གཟུགས་དང་མཚུངས། །\nཡེ་ཤེས་རྣམས་ཀྱི་གཟི་མདངས་སྟོན། །\nའོད་ཀྱི་གཏིང་མདངས་བཀྲག་ཀྱང་སྟོན། །",
    "before": "a complete maṇḍala,",
    "after": "a complete mandala,",
    "rationale": "P2 spelling for the contemplative mandala-form comparison, not the literal geometric mirror-disc exception. Its completion, form and the surrounding light/knowing predicates remain.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T07",
    "pair": "DTG-001416",
    "golden": [
      "U03044"
    ],
    "tibetan": "འདི་དག་རྣམས་ཀྱང་རང་ཤེས་རྫོགས། །",
    "before": "complete one's own knowing.",
    "after": "complete self-knowing.",
    "rationale": "P2 rang shes in the technical knowing/embodiment account with no separately specified ordinary possessor. The default self-form fits here without asserting a theory of reflexive cognition. The precise causative/resultative force of completion is still qualified with the subject sequence in N-133.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-T08",
    "pair": "DTG-001453",
    "golden": [
      "U03115",
      "U03116",
      "U03117"
    ],
    "tibetan": "རྒྱང་ཞགས་ཉིད་ལས་རྟེན་པས་ནི། །\nསྐྱོན་མེད་བྱ་བྱེད་རྣམས་སྤངས་པས། །\nཆོས་ཉིད་མ་ལ་སྤྱོད་པའོ། །",
    "before": "having abandoned action and agency,",
    "after": "having abandoned doing and doers,",
    "rationale": "P2 actual action/agent contrast in the release account; preserve both members and the plural rnams without supplying a named agent. Skyon med remains free from faults, not an invented faulty action; its attachment remains qualified in N-135.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T09",
    "pair": "DTG-001477",
    "golden": [
      "U03165"
    ],
    "tibetan": "ཆུ་ཡིས་ཏིང་འཛིན་དམིགས་པ་གསལ། །",
    "before": "the object of deep absorption clear.",
    "after": "deep absorption’s object of focus clear.",
    "rationale": "The nominal dmigs pa is the object of focus belonging to deep absorption, not a generic object with the focus component dropped. Ting dzin is a recognizable short form in this predicate; the bracketed Wind group supply remains subject to the existing elemental-construction qualification.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T10",
    "pair": "DTG-001539",
    "golden": [
      "U03266",
      "U03267"
    ],
    "tibetan": "ཤེས་དང་ཤེས་བྱའི་ཡེ་ཤེས་ཀྱིས། །\nམོས་གུས་ཅན་ལ་དངོས་གྲུབ་སྟེར། །",
    "before": "accomplishments are granted",
    "after": "spiritual accomplishments are granted",
    "rationale": "P2 dngos grub whole equivalent; recipient, passive presentation and the preceding knowing/known distinction remain.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-T11",
    "pair": "DTG-001539",
    "golden": [
      "U03266",
      "U03267"
    ],
    "tibetan": "ཤེས་དང་ཤེས་བྱའི་ཡེ་ཤེས་ཀྱིས། །\nམོས་གུས་ཅན་ལ་དངོས་གྲུབ་སྟེར། །",
    "before": "with aspiration and devotion.",
    "after": "with confident devotion.",
    "rationale": "Established whole mos gus equivalent, not a sum of separately assigned aspiration and devotion. No additional requirement or recipient is added.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-S02",
    "pair": "DTG-001392",
    "golden": [
      "U02995"
    ],
    "tibetan": "ཤེས་རབ་སྒྲོན་མ་སྦྱང་བའི་གནད། །",
    "before": "The key point of the discerning-knowing lamp is training.",
    "after": "The key point of training the discerning-knowing lamp:",
    "rationale": "The genitive sbyang bai gnad makes this the key point of training the lamp; it does not assert that training itself is the key point. The colon joins the next pair’s three-rite and accomplishment instructions without changing pair segmentation or inserting an unexpressed lamp name.",
    "severity": "moderate meaning",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-S03",
    "pair": "DTG-001400",
    "golden": [
      "U03007",
      "U03008",
      "U03009",
      "U03010"
    ],
    "tibetan": "དག་པ་ཡེ་ཤེས་ལྔ་ཡི་འོད། །\nས་རྡོ་རི་བྲག་བག་སྟོངས་ནས། །\nགྲུ་ཆད་དང་ནི་ཡུལ་གྲུ་ཙམ། །\nཁྲིད་ལ་མཁས་པས་སྣང་བར་འགྱུར། །",
    "before": "appears to one skilled in guiding.",
    "after": "appears through skill in guiding.",
    "rationale": "Mkhas pas supplies instrumental/causal force, not a dative experiencer. Retain the preceding light as the grammatical subject and do not resolve the existing spatial-expression questions by adding a new person.",
    "severity": "moderate meaning",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-S04",
    "pair": "DTG-001485",
    "golden": [
      "U03176",
      "U03177",
      "U03178",
      "U03179",
      "U03180",
      "U03181"
    ],
    "tibetan": "དེ་ནས་མ་ཡི་མངལ་ཞུགས་པས། །\nལོ་དང་ཟླ་བ་ཞག་གི་རྩིས། །\nསོ་སོའི་འབྱུང་བའི་རང་དུས་ཀྱིས། །\nདུས་ཚོད་ངེས་པར་བཟུང་བྱས་ལ། །\nརང་རང་འབྱུང་བ་གསོ་བ་ཡི། །\nརྟེན་འབྲེལ་སྔགས་པས་འབད་དེ་བརྟེན། །",
    "before": "through restoring each respective element,\nthe mantra practitioner should diligently rely on dependent connections.",
    "after": "the mantra practitioner should diligently rely on dependent connections\nfor restoring each respective element.",
    "rationale": "Gso ba yi modifies the dependent connections relied upon: for restoring each element. The old through made restoration the instrument of reliance. Retain the explicit mantra practitioner, diligence, respective elements and the preceding timing/womb qualification without supplying a prenatal procedure.",
    "severity": "moderate meaning",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-S05",
    "pair": "DTG-001509",
    "golden": [
      "U03224",
      "U03225"
    ],
    "tibetan": "མིག་དང་རྣ་བ་སྣ་དང་ལྕེ། །\nལུས་ཀྱི་དབང་པོ་ཀུན་ཟད་སྟེ། །",
    "before": "Eye, ear, nose, tongue,\nand all bodily faculties are exhausted.",
    "after": "The faculties of eye, ear, nose, tongue,\nand body are all exhausted.",
    "rationale": "Dbang po is the shared head of the five-member list; kun scopes their exhaustion, not an added open class of bodily faculties. Preserve all five source items and the following explanation of exhausted capacities without interpreting them as physical damage.",
    "severity": "moderate meaning",
    "confidence": "high"
  },
  {
    "finding": "PD-B10-C01",
    "pair": "DTG-001415",
    "golden": [
      "U03041",
      "U03042",
      "U03043"
    ],
    "tibetan": "ཐབས་དང་ཤེས་རབ་རྫོགས་པ་ཡིས། །\nཟུང་གཉིས་ཆ་ལས་སྐུ་གཉིས་འཛིན། །\nརབ་ཏུ་སྣང་བ་མཆེད་པར་བྱེད། །",
    "before": "Through methods and discerning knowing being complete,",
    "after": "Through means and discerning knowing being complete,",
    "rationale": "I §8.1 U08: the two paired portions/two embodiments construction explicitly uses the abstract technical polarity, not a list of procedures. This supports means locally; procedural methods in the sun/moon and adjustment clauses are retained. No shared glossary addition is made.",
    "severity": "minor construction",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-C02",
    "pair": "DTG-001455",
    "golden": [
      "U03122",
      "U03123"
    ],
    "tibetan": "རྟོག་དཔྱོད་ཟད་པའི་སེམས་ཉིད་ཀྱིས། །\nའཁོར་བ་རྒྱང་དུ་འཕངས་པ་ཡིས། །",
    "before": "Through the nature of ordinary mind in which",
    "after": "Through ordinary mind itself in which",
    "rationale": "I §8.1 U07: sems nyid kyis identifies the operative ordinary mind with conceptual examination exhausted. The intensive itself preserves that head without introducing a separate nature as an agent. This is not extended automatically to the vessel/stainless simile.",
    "severity": "minor construction",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-C02",
    "pair": "DTG-001536",
    "golden": [
      "U03260",
      "U03261"
    ],
    "tibetan": "དེ་ལྟར་གྲོལ་བའི་སེམས་ཉིད་ལ། །\nཐུགས་རྗེ་མེད་པ་མ་ཡིན་ཏེ། །",
    "before": "In the nature of ordinary mind liberated in this way,",
    "after": "In ordinary mind itself, liberated in this way,",
    "rationale": "I §8.1 U07: the explicitly just-liberated ordinary mind in the preceding reply is resumed intensively by sems nyid. Preserve the double negative about compassionate responsiveness and do not change ordinary mind to awareness.",
    "severity": "minor construction",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-C02",
    "pair": "DTG-001540",
    "golden": [
      "U03268",
      "U03269"
    ],
    "tibetan": "དེ་ཡང་སེམས་ཉིད་སྨིན་པའི་ཚེ། །\nཆོས་ཀྱི་སྐུ་ལ་གཞི་གནས་ཏེ། །",
    "before": "when the nature of ordinary mind matures,",
    "after": "when ordinary mind itself matures,",
    "rationale": "I §8.1 U07: the same resumed ordinary mind is the head of the explicit when/matures construction. Preserve the conditional timing and the separately qualified Ground/dharma-embodiment clause.",
    "severity": "minor construction",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B10-C03",
    "pair": "DTG-001442",
    "golden": [
      "U03086",
      "U03087",
      "U03088"
    ],
    "tibetan": "དབྱིངས་ཀྱི་ཡུལ་ནི་སྟོང་པ་དང༌། །\nགསལ་དང་སྒྲིབ་བྲལ་མདངས་འབྱིན་པ། །\nཁྱབ་ཅིང་ཡངས་ལ་གཅིག་འདུས་པའོ། །",
    "before": "and emitting splendor;",
    "after": "and emitting luster;",
    "rationale": "I §8.1 U13: bare mdangs is emitted in a clear, unobscured luminous-object description, supporting the narrower luminous luster reading locally. Do not normalize its source spelling into gdangs radiance or collapse the separate bkrag/gzi mdangs/gting mdangs combinations. This local realization is not a new shared row.",
    "severity": "minor construction",
    "confidence": "moderate-high"
  }
]
```

<!-- phase-d-batch-10-annotation-operations -->
```json
[
  {
    "finding": "PD-B10-N01",
    "note": "G-U02927",
    "linked_pair": "DTG-001354",
    "tibetan": " དམ་ཚིག་གིས་ནི་རབ་བརྟག་གོ། །",
    "before": "**Current English:** `\"[This] is to be thoroughly examined through the pledge. [N-127]\"`",
    "after": "**Current English:** `\"[This] is to be thoroughly examined through the sacred pledge. [N-127]\"`",
    "rationale": "Keep the active Current English source-note quotation consistent with the authorized P2 repair in its linked pair. Previous English, exact supplied/golden Tibetan, alternative water note and subject qualification remain unchanged.",
    "severity": "minor note consistency",
    "confidence": "high"
  }
]
```

<a id="phase-d-notes-10"></a>
#### Note dispositions, local constructions and unresolved spans

```json
[
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-127",
    "pairs": [
      "DTG-001344",
      "DTG-001345",
      "DTG-001346",
      "DTG-001350",
      "DTG-001354",
      "DTG-001356",
      "DTG-001360"
    ],
    "ids": [
      "U02911",
      "U02912",
      "U02913",
      "U02914",
      "U02920",
      "U02921",
      "U02927",
      "U02930",
      "U02934",
      "U02935"
    ],
    "realization": "key point; sacred pledge; residue; karmic wind",
    "status": "Approved labels; wordplay and source correction preserved",
    "reason": "The full channel continuation was read, including the distinct ma syllabic explanations and generative/summit predicates. The extract/residue link locally identifies snyigs ma, while splendor is not silently made radiance. The conditional/purpose force in the bloodletting, warmth and lifespan clauses is already conveyed by their restricted English constructions; no new physiological method or efficacy is asserted. The water alternative at U02927 is already properly layered, and the bracketed subject stays provisional. Karmic wind remains the recognized las rlung short form, not a new compound built from components.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-128",
    "pairs": [
      "DTG-001367",
      "DTG-001368",
      "DTG-001369",
      "DTG-001370",
      "DTG-001373"
    ],
    "ids": [
      "U02944",
      "U02945",
      "U02946",
      "U02947",
      "U02948",
      "U02949",
      "U02950",
      "U02951",
      "U02952",
      "U02953",
      "U02954",
      "U02955",
      "U02959",
      "U02960",
      "U02961"
    ],
    "realization": "door genitive; pure extract of bodily quintessence; cakṣu",
    "status": "Supported genitive repair; anatomical details still provisional",
    "reason": "The door is modified by where all ... is gathered; the gathered extract is not independently asserted to emerge. Primordial knowing is visibly supplied from U02944, and the eye identification is locally supported by U02983. Pure extract and quintessence both remain. Their detailed bodily relationship, the two/five branching, faults/actions attachment, ba-min and a-bras are not certified anatomical identities. A source-supported account of those referents, not a modern eye diagram, would settle them.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T62",
    "pairs": [
      "DTG-001367",
      "DTG-001370"
    ],
    "ids": [
      "U02944",
      "U02945",
      "U02946",
      "U02953",
      "U02954",
      "U02955"
    ],
    "realization": "cakṣu (eye); buffalo (ba-min) provisional",
    "status": "Local eye identification supported; buffalo/a-bras not newly approved",
    "reason": "Cakṣu is identified in the present eye-door sequence and the explicit mig reply, unlike the unsupported heart inference from citta. The buffalo-horn proposal remains visibly source-linked and provisional; a-bras stays unidentified. This creates no shared anatomical entry.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T65",
    "pairs": [
      "DTG-001350",
      "DTG-001367",
      "DTG-001384",
      "DTG-001442"
    ],
    "ids": [
      "U02920",
      "U02921",
      "U02944",
      "U02945",
      "U02946",
      "U02979",
      "U02980",
      "U02981",
      "U02982",
      "U03086",
      "U03087",
      "U03088"
    ],
    "realization": "residue; pure extract; quintessence; luminous luster",
    "status": "P2 extraction labels; U13 locally supported bare-mdangs reading",
    "reason": "The sequence distinguishes extract/residue, concentrated quintessence and essence. The luminous bare mdangs at U03087 supports luster under U13, while gzi mdangs, gting mdangs, bkrag and gdangs are checked separately and not normalized. Their full shared-family assignments remain a cross-work question, not a book-wide substitution rule.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-129",
    "pairs": [
      "DTG-001375",
      "DTG-001376",
      "DTG-001381",
      "DTG-001384",
      "DTG-001385"
    ],
    "ids": [
      "U02963",
      "U02964",
      "U02965",
      "U02966",
      "U02972",
      "U02973",
      "U02974",
      "U02979",
      "U02980",
      "U02981",
      "U02982",
      "U02983",
      "U02984",
      "U02985"
    ],
    "realization": "key points; quintessence; pure extract; transcendence [of sorrow]",
    "status": "Approved labels and local short form; inherited attachment open",
    "reason": "The complete four-lamp account and following replies were read, including the pure-basic-space characteristics/supports. The U02972 short das is locally a release-path term, with sorrow bracketed. Pervading-emptiness, the subject of U02979–82 and the identities of the three key points remain qualified; no missing fourth name is imported into this earlier stanza.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T61",
    "pairs": [
      "DTG-001381"
    ],
    "ids": [
      "U02972",
      "U02973",
      "U02974"
    ],
    "realization": "transcendence [of sorrow]",
    "status": "Local short form supported in release-path context",
    "reason": "U02972 is now reviewed with the abandonment of cyclic existence at U02982 and explicit coordinated boundary at U03022. This supports the bracketed complement here; ordinary past/transcending forms remain outside its scope.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T64",
    "pairs": [
      "DTG-001377",
      "DTG-001380",
      "DTG-001382",
      "DTG-001390",
      "DTG-001392",
      "DTG-001394"
    ],
    "ids": [
      "U02967",
      "U02971",
      "U02975",
      "U02976",
      "U02977",
      "U02993",
      "U02995",
      "U02998"
    ],
    "realization": "recorded full/short lamp renderings",
    "status": "Local short-form identities supported",
    "reason": "The explicit four-lamp introduction, the subsequent characteristics and supports establish the local identities. Full Water lamp of the far-reaching lasso and Lamp of the empty sphere may realize the first two identified short forms; discerning-knowing lamp and sphere lamp preserve later abbreviated naming. This does not make every lasso/sphere/knowing expression a lamp or insert an absent fourth label.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-130",
    "pairs": [
      "DTG-001392",
      "DTG-001393",
      "DTG-001394",
      "DTG-001395"
    ],
    "ids": [
      "U02995",
      "U02996",
      "U02997",
      "U02998",
      "U02999",
      "U03000"
    ],
    "realization": "key point of training the discerning-knowing lamp",
    "status": "Genitive and cross-pair continuation repaired",
    "reason": "The training genitive introduces the following instructions rather than predicating training as the key point. The three rites, three gazes and channel/thumb/finger relationship remain unspecified or provisional; the correction supplies no pressure, placement, target or duration.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-131",
    "pairs": [
      "DTG-001396",
      "DTG-001397",
      "DTG-001398",
      "DTG-001400",
      "DTG-001401",
      "DTG-001403"
    ],
    "ids": [
      "U03001",
      "U03002",
      "U03003",
      "U03004",
      "U03007",
      "U03008",
      "U03009",
      "U03010",
      "U03011",
      "U03013",
      "U03014"
    ],
    "realization": "through skill in guiding; procedural methods",
    "status": "Instrumental force repaired; spatial/power attachments retained provisionally",
    "reason": "The written mkhas pas supports through skill rather than a new dative experiencer. The existing bag stongs/gru chad/yul gru tsam and elemental-completion qualifications remain; direct sun-gazing or a practical eye/breath method is not inferred. Procedural methods remains distinct from the abstract means pairing in U03041.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T71",
    "pairs": [
      "DTG-001396",
      "DTG-001397",
      "DTG-001400",
      "DTG-001438"
    ],
    "ids": [
      "U03001",
      "U03002",
      "U03003",
      "U03007",
      "U03008",
      "U03009",
      "U03010",
      "U03078",
      "U03079",
      "U03080"
    ],
    "realization": "guiding; decisive resolution; distinguishing",
    "status": "Construction-scoped proposals retained",
    "reason": "The teaching-action list keeps pointing out, guiding, decisive resolution and distinguishing separate. The instrumental repair does not settle guiding as an optical procedure. These unlisted shared labels remain proposals for cross-work reconciliation, not a newly adopted glossary family.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T70",
    "pairs": [
      "DTG-001414",
      "DTG-001451"
    ],
    "ids": [
      "U03039",
      "U03040",
      "U03109",
      "U03110",
      "U03111",
      "U03112"
    ],
    "realization": "pure basic space itself; perfectly pure basic space",
    "status": "Local abbreviated designation supported",
    "reason": "The consecutive four-lamp characteristics/supports support relation to the established perfectly-pure-basic-space lamp. Retain the actual short wording and different source order, without printing an extra lamp head where absent.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T77",
    "pairs": [
      "DTG-001408",
      "DTG-001412"
    ],
    "ids": [
      "U03025",
      "U03026",
      "U03031",
      "U03032",
      "U03033",
      "U03034"
    ],
    "realization": "foundation",
    "status": "Inherited technical/ordinary support question remains open",
    "reason": "Holding/gathering a support fits foundation, but primordial-knowing context also permits technical Ground. The broader loop does not decisively distinguish them; the exact U03025–34 constructions remain provisional pending a referent/attachment analysis. They are not settled by the physical/calculation foundation exceptions elsewhere.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-133",
    "pairs": [
      "DTG-001415",
      "DTG-001416",
      "DTG-001417",
      "DTG-001418",
      "DTG-001419",
      "DTG-001420",
      "DTG-001423"
    ],
    "ids": [
      "U03041",
      "U03042",
      "U03043",
      "U03044",
      "U03045",
      "U03046",
      "U03047",
      "U03048",
      "U03049",
      "U03050",
      "U03054",
      "U03055"
    ],
    "realization": "means; self-knowing; mandala; full cyclic-existence contrast",
    "status": "Local polarity and approved labels; implicit completion/subject questions retained",
    "reason": "The two paired portions support abstract means/discerning knowing rather than procedures, and technical rang shes supports self-knowing without positing a reflexive theory. The completion predicate and implied agents remain qualified with the sequence. Two embodiments are not normalized to three; the later three-embodiment exhaustion and full apprehended/apprehending distinction remain. Hero identity, balance and aspiration/convergence are unresolved.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-134",
    "pairs": [
      "DTG-001425",
      "DTG-001427",
      "DTG-001434",
      "DTG-001435",
      "DTG-001436",
      "DTG-001437",
      "DTG-001438",
      "DTG-001439",
      "DTG-001441",
      "DTG-001442"
    ],
    "ids": [
      "U03057",
      "U03058",
      "U03059",
      "U03061",
      "U03062",
      "U03070",
      "U03071",
      "U03072",
      "U03073",
      "U03074",
      "U03075",
      "U03076",
      "U03077",
      "U03078",
      "U03079",
      "U03080",
      "U03081",
      "U03082",
      "U03085",
      "U03086",
      "U03087",
      "U03088"
    ],
    "realization": "key points; luster; generic words in linguistic-object clauses",
    "status": "Local U12/U13 controls applied; source query and counts preserved",
    "reason": "Bare mdangs is luminous luster here, not gdangs radiance. Generic words in word/meaning and indication clauses does not erase an explicit sgra/tshig/ming contrast; no arbitrary phrase rotation is imposed. Gnang grants, all five/ six/three/two/six numbers, entities and the elements/arising ambiguity remain source-linked. No snang emendation or color chart is supplied.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-135",
    "pairs": [
      "DTG-001453",
      "DTG-001454",
      "DTG-001455",
      "DTG-001456",
      "DTG-001457",
      "DTG-001458"
    ],
    "ids": [
      "U03115",
      "U03116",
      "U03117",
      "U03118",
      "U03119",
      "U03120",
      "U03121",
      "U03122",
      "U03123",
      "U03124",
      "U03125",
      "U03126",
      "U03127",
      "U03128",
      "U03129"
    ],
    "realization": "doing and doers; ordinary mind itself; cyclic existence",
    "status": "Supported labels and intensive; faultless/metaphor relations remain provisional",
    "reason": "The action/agent contrast supports both doing and doers; skyon med is not changed to faulty. Ordinary mind is the operative head with examination exhausted, supporting intensive nyid. The rten/brten and threefold agency constructions remain qualified. At U03128–29 the carried object might be resumed awareness or the practitioner; existing one is brought is provisional, not proof of a newly stated person. The balance/flower/irrigation metaphors and this antecedent require source-supported construction resolution.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-136",
    "pairs": [
      "DTG-001462",
      "DTG-001464",
      "DTG-001465",
      "DTG-001466",
      "DTG-001471",
      "DTG-001477"
    ],
    "ids": [
      "U03140",
      "U03141",
      "U03142",
      "U03143",
      "U03145",
      "U03146",
      "U03147",
      "U03148",
      "U03149",
      "U03159",
      "U03165"
    ],
    "realization": "paired-element constructions; object of focus; rnam phrul question",
    "status": "Focus component repaired; PD-Q10-03 shared-label question open",
    "reason": "The two water/wind clauses and separate source query remain; instrumental-looking particles are not silently rewritten as genitives in Tibetan. The current possessive matrix and its supplements stay provisional. At U03140, རྣམ་འཕྲུལ in the elemental account currently shares magical displays with established cho phrul. This English overlap alone is not an error: manifestations versus magical manifestations/displays requires a whole-expression family decision based on its occurrences. It is not a newly approved cho phrul synonym. Tshigs remains joints, not tshig words.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T73",
    "pairs": [
      "DTG-001462",
      "DTG-001463",
      "DTG-001468",
      "DTG-001472",
      "DTG-001476",
      "DTG-001477"
    ],
    "ids": [
      "U03140",
      "U03141",
      "U03142",
      "U03143",
      "U03144",
      "U03152",
      "U03153",
      "U03154",
      "U03160",
      "U03164",
      "U03165"
    ],
    "realization": "provisional elemental pairing; deep absorption’s object of focus",
    "status": "Historical matrix proposal not promoted; local abbreviated absorption identified",
    "reason": "The actual sequence retains different source case forms, both water/wind entries and bracketed omitted group names. Ting dzin is identified locally as deep absorption, distinct from bsam gtan. Nothing here validates a four-by-four causal or cognitive classification.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T74",
    "pairs": [
      "DTG-001470",
      "DTG-001490",
      "DTG-001507"
    ],
    "ids": [
      "U03157",
      "U03158",
      "U03188",
      "U03189",
      "U03190",
      "U03191",
      "U03222"
    ],
    "realization": "stupefaction; glass (man-shel); store of words",
    "status": "Existing source-linked lexical questions retained",
    "reason": "Rmugs stays distinct from technical dullness, ignorance and delusion; no graded mental taxonomy is adopted. Man-shel and gtam zungs remain provisional whole expressions, not modern material or psychological identifications. A broader source-linked family comparison, rather than component gloss replacement, is still required.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-137",
    "pairs": [
      "DTG-001484",
      "DTG-001485",
      "DTG-001489",
      "DTG-001490"
    ],
    "ids": [
      "U03173",
      "U03174",
      "U03175",
      "U03176",
      "U03177",
      "U03178",
      "U03179",
      "U03180",
      "U03181",
      "U03187",
      "U03188",
      "U03189",
      "U03190",
      "U03191"
    ],
    "realization": "restorative dependent connections; quintessence; path-entry question",
    "status": "Genitive repaired; PD-Q10-01 and simile/timing questions remain",
    "reason": "Gso ba yi modifies the dependent connections relied on for restoration, not restoration as an instrument of relying. Womb-entry subject and timing remain explicitly provisional, not prenatal guidance. At U03174, ཐར་པའི་ལམ་སྣ་སྟོན་པ could show the entrance/course of the liberation path rather than the current many paths; the exact lam sna construction needs parallel syntactic evidence to choose, and the plurality is not certified. The stainless sems nyid in the vessel-color simile may name the contrasted nature rather than intensify a resumed subject: nature of ordinary mind is retained provisionally for that distinct construction, not as a default. Material identity and vessel/contents analogy remain unresolved.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-138",
    "pairs": [
      "DTG-001492",
      "DTG-001493",
      "DTG-001495",
      "DTG-001496",
      "DTG-001498",
      "DTG-001501",
      "DTG-001502"
    ],
    "ids": [
      "U03193",
      "U03194",
      "U03195",
      "U03197",
      "U03198",
      "U03199",
      "U03200",
      "U03201",
      "U03202",
      "U03205",
      "U03206",
      "U03209",
      "U03210",
      "U03211",
      "U03212",
      "U03213",
      "U03214",
      "U03215",
      "U03216"
    ],
    "realization": "key point; five senses; unresolved constructions",
    "status": "No component reconstruction or instructional normalization",
    "reason": "The local list identifies objects of focus, but dmigs rten/bsam gnas, sgyu rtsal, bum ldir, the sixfold taste, crossed bows and pursuit through entities still require their own construction decisions. Rgyud mangs names the many-stringed instrument, not tantra/continuum; sgra is auditory sound here. The affirmative casting into distraction, all five sense domains and the unidentified sound syllables remain, without recipes or devices.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-139",
    "pairs": [
      "DTG-001509",
      "DTG-001510"
    ],
    "ids": [
      "U03224",
      "U03225",
      "U03226"
    ],
    "realization": "all five faculties exhausted",
    "status": "Shared-head/quantifier scope repaired",
    "reason": "The five listed faculties are eye, ear, nose, tongue and body; kun qualifies their total exhaustion. The revision removes the unintended open class of all bodily faculties while retaining the complete five-item list and the following absence-of-intrinsic-nature explanation. Gtam zungs and physiological interpretation remain unverified.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-140",
    "pairs": [
      "DTG-001512",
      "DTG-001515",
      "DTG-001518",
      "DTG-001519"
    ],
    "ids": [
      "U03228",
      "U03229",
      "U03230",
      "U03235",
      "U03239",
      "U03240",
      "U03241"
    ],
    "realization": "unresolved dag function; mental-faculty body; gleg retained",
    "status": "PD-Q10-02 remains open; old source-color issue not invented afresh",
    "reason": "At U03235, ཐིག་ལེ་མཆེད་དང་འབྱུང་སྣང་དག may predicate pure elemental appearances or use dag as a plural/list marker. Current are pure remains provisional pending clause-level determination; an expected pure-bardo doctrine is not proof. Rang bzhin gnas pa aggregate scope, appearance-state boundaries and gleg are already qualified and remain unresolved. No full color taxonomy is imported.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T75",
    "pairs": [
      "DTG-001518"
    ],
    "ids": [
      "U03239"
    ],
    "realization": "body of mental faculty",
    "status": "Local descriptive construction retained, not a new canonical compound",
    "reason": "Yid kyi lus is locally a body characterized by mental faculty in the becoming-appearance sequence. The rendering preserves both heads without asserting a modern entity or substituting embodiment, ordinary mind or awareness. Component matches alone do not establish a shared technical assignment; any broader preferred label requires cross-work reconciliation.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-141",
    "pairs": [
      "DTG-001521",
      "DTG-001522",
      "DTG-001523",
      "DTG-001524",
      "DTG-001525",
      "DTG-001526"
    ],
    "ids": [
      "U03243",
      "U03244",
      "U03245",
      "U03246",
      "U03247",
      "U03248",
      "U03249",
      "U03250"
    ],
    "realization": "ordinary-mind liberation; Ground contrasts",
    "status": "Full reply read; no doctrinal normalization",
    "reason": "The complete reply through U03258 denies movement and a releasing agent, retains both Ground statements and repeats confidence. Those source differences are not contradictory English errors to harmonize. Rgyu mtshan and the exact technical-versus-ordinary gzhi scope stay qualified; no causal explanation is supplied.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T76",
    "pairs": [
      "DTG-001526"
    ],
    "ids": [
      "U03249",
      "U03250"
    ],
    "realization": "abiding in its own clarity",
    "status": "Supported local grammar",
    "reason": "Rang gsal gnas pa directly modifies the resumed ordinary mind in this reply. Own clarity preserves that relation without adding mindfulness, intrinsic nature or awareness; the established self-clear mindfulness entry is a different whole expression.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T79",
    "pairs": [
      "DTG-001527",
      "DTG-001531",
      "DTG-001533",
      "DTG-001537"
    ],
    "ids": [
      "U03251",
      "U03255",
      "U03257",
      "U03262",
      "U03263"
    ],
    "realization": "basis of dependence; nothing to repeat; support for holding; nakedly provisional",
    "status": "Local support constructions supported; remaining attachment qualified",
    "reason": "In the whole liberation reply, ltos gzhi med and bskyar gzhi med deny a dependence basis and any repeated liberation; they do not name a technical Ground to be capitalized by substring. The holding-support construction likewise preserves a support noun, but the actor/rang bzhin attachment at U03263 remains provisional. Cer gyis nakedly remains a source-linked interpretation, not a respelling to gcer.",
    "review": "REVIEW.md#phase-d-notes-10"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-143",
    "pairs": [
      "DTG-001536",
      "DTG-001537",
      "DTG-001539",
      "DTG-001540",
      "DTG-001541",
      "DTG-001543"
    ],
    "ids": [
      "U03260",
      "U03261",
      "U03262",
      "U03263",
      "U03266",
      "U03267",
      "U03268",
      "U03269",
      "U03270",
      "U03272"
    ],
    "realization": "ordinary mind itself; confident devotion; spiritual accomplishments",
    "status": "Supported constructions/whole entries; larger account remains qualified",
    "reason": "The double negative explicitly resumes the ordinary mind just liberated, and its when-matures clause supports intensive itself. Whole mos gus and dngos grub are not split or truncated. The following account through U03315 was read as boundary context without extra coverage: it preserves three embodiment scopes and the later explicit five-knowing sequence. Holding-support, the Ground-abiding clause, purity/stain statement and abbreviated predicates are not silently resolved; their continuation will be adjudicated with its own pairs.",
    "review": "REVIEW.md#phase-d-notes-10"
  }
]
```

**Important no-change cases:** the absent water subject at U02927 is already correctly removed and its alternative remains separate. The repeated water/wind entries are preserved exactly; their source query is not permission to emend. Rgyud mangs remains a musical instrument, tshigs remains joints, auditory sgra remains sound, and ordinary entities are not renamed matter. Lamp short forms preserve their actual naming differences; no unexpressed fourth lamp is inserted. Two and three embodiments, the ma wordplay, paired-element particles, explicit color/count sequences, affirmative distraction and double negation remain. Unresolved gleg and the anatomical/metaphorical names are not guessed from familiar lists.

**Application and verification (same-reviewer self-check):** all **51 English operations in 45 pairs**, the one active Current English note repair and **27 append-only dispositions** are applied. Every changed clause and necessary neighbor was reread against the current Tibetan in the 107-pair repair-context file, all 200 revised English pairs were read continuously, and the complete G-U02927 note was reread with its unchanged Tibetan/Previous English/alternative and subject qualification. The five-faculty shared head, training/door/restoration genitives and guiding instrumental retain their subjects, numbers and scope. Context through ordinal 1580 is not extra completed coverage. Three newly identified bounded questions PD-Q10-01–03 and inherited unresolved notes remain open; local supported U07/U08/U13 choices are not promoted to shared defaults.

**Actual validation after Batch 10:** integrity replay passes **352 pair operations** (331 English operations in 292 pairs, 21 review-link operations; **304 changed pairs including note-only changes**) and all three continuation-04 footer operations. Four footer operations now exist cumulatively: three source-annotation repairs and one active Current English consistency repair. All 2,667 IDs/order, fixed source/golden/policy/format/lineage bytes, historical note/usage contents, inherited links and **700** English local-link targets remain intact; `git diff --check` passes. English SHA-256: `4b7eb9f3a2c9bd681b6876be86d2ca62380036c3339b5ab6c32921bb737c6aba`.

The actual paired suite was rerun: **64 tests, 53 pass, 9 fail, 2 error**, retaining the same historical exact-English preemption at DTG-000002. The default `paired/validate.py` and `paired/migrate.py --check` were actually run and each exit **1** on the protected old-glossary check. The most recent actual projector check and regeneration attempt remain the Batch 09 failures before writes; they were not falsely rerun or called successful here. No released reader, manifest, source or tag was changed. These are software checks, not execution of the standard's semantic regression specifications.

**Verified coverage:** **1,550/2,667**, through DTG-001543; **347** first-encountered note records read cumulatively. Chapter 1 is complete and Chapter 2 has 351/543 pairs covered. Continue at **ordinal 1551, DTG-001544**. Text remains in review, not whole-work ready.


<a id="phase-d-batch-11"></a>
### Batch 11 — source ordinals 1551–1742; Chapter 2 closing

**Input:** clean local and remote `9dd69e0d8e82f6791d276f44e75be1fd29d5516f`, same reviewer/session and frozen policy. All **192 current Tibetan–English pairs** were read in order through the Chapter 2 colophon, with all **24 first-encountered notes**, their current and historical prose and the three active source/boundary notes. Chapter 3 opening ordinals 1743–1750 were read for transition context only. A whole-work literal editorial-warning search found two current occurrences; the earlier DTG-000846 and its surrounding pair context/N-085 were reread without duplicate coverage.

**Evidence recorded before edits:** 56 English operations in 51 pair payloads (including one earlier-layer correction), one active Current English quotation repair, and 24 append-only dispositions. Full eight-column rows, Q1–Q9, I §8.1 and III controls were applied. Three newly bounded lexical/role questions PD-Q11-01–03 remain provisional; they refine existing note uncertainty rather than certify missing source grammar.

<!-- phase-d-batch-11-operations -->
```json
[
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001558",
    "golden": [
      "U03292",
      "U03293",
      "U03294",
      "U03295"
    ],
    "tibetan": "དེ་ཉིད་ཡེ་ཤེས་གནད་བསྟན་པས། །\nདང་པོ་གཞི་ལ་ཁྱབ་ཚུལ་ལ། །\nབར་དུ་ལམ་ལ་རྫོགས་པ་ཡི། །\nཐ་མ་འགྲོ་བའི་ལུས་ལ་ཁྱབ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001587",
    "golden": [
      "U03354",
      "U03355"
    ],
    "tibetan": " ཀུན་གཞི་དང་ནི་ཆོས་སྐུའི་གནད། །\nདེ་ལ་ཀུན་གཞི་རེ་ཞིག་བཤད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001599",
    "golden": [
      "U03370",
      "U03371",
      "U03372"
    ],
    "tibetan": "དེ་ལྟར་དབྱེ་བའི་གནད་ཀྱིས་ནི། །\nདུས་དང་ཐབས་དང་དཔེ་ཉིད་དང་། །\nཕྱེད་པའི་ཚད་ཀྱིས་འབྲས་བུའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001601",
    "golden": [
      "U03374",
      "U03375"
    ],
    "tibetan": "སེམས་དང་ཡེ་ཤེས་གནད་ཉིད་ནི། །\nསེམས་ཞེས་བྱ་བ་འཁྲུལ་རྟོག་ལ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001620",
    "golden": [
      "U03406"
    ],
    "tibetan": "གནད་ཀྱིས་གོམས་ཀྱང་འགྲུབ་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001625",
    "golden": [
      "U03413"
    ],
    "tibetan": "གནད་ཀྱིས་ཟས་ཀྱི་རྣལ་འབྱོར་འགྲུབ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001630",
    "golden": [
      "U03419",
      "U03420"
    ],
    "tibetan": "གཉིད་ཀྱི་བསམ་གཏན་བསྒོམ་པ་དང་། །\nགནད་ཀྱིས་རྨི་ལམ་འགགས་པར་བྱེད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001636",
    "golden": [
      "U03427",
      "U03428"
    ],
    "tibetan": "སྨིན་པས་དབྱིངས་ཀྱི་སྒྲོན་མ་ལས། །\nགནད་ཀྱིས་བག་ཆགས་དྲུངས་ནས་འབྱིན། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001665",
    "golden": [
      "U03488"
    ],
    "tibetan": "རྩ་ཡི་གནད་ནི་བརྒྱ་ཕྲག་གཉིས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001666",
    "golden": [
      "U03489",
      "U03490"
    ],
    "tibetan": "དེ་ལ་ལེགས་པར་གནད་བསྡུས་ནས། །\nབརྒྱ་དང་བཅོ་ལྔས་ལས་ཀུན་བྱེད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001667",
    "golden": [
      "U03491"
    ],
    "tibetan": "རབ་ཏུ་འགྱུར་བ་རྩ་ཡི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001671",
    "golden": [
      "U03498",
      "U03499"
    ],
    "tibetan": "དེ་ཡི་གནད་ཀྱི་མན་ངག་ནི། །\nགནས་དང་འོང་དང་འགྲོ་ལམ་རྟེན། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001681",
    "golden": [
      "U03517",
      "U03518"
    ],
    "tibetan": "ཡུལ་ནི་ཡོད་དང་མེད་པ་དང༌། །\nའགྲོ་དང་འོང་བའི་གནད་ཀྱིས་བསམ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001698",
    "golden": [
      "U03548",
      "U03549"
    ],
    "tibetan": "དེ་ལྟར་འཁྲུལ་མེད་སྣང་བ་ནི། །\nཡེ་ནས་གྲོལ་བའི་གནད་ལས་འབྱུང༌། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001702",
    "golden": [
      "U03556",
      "U03557"
    ],
    "tibetan": "དེ་ལས་འཁྲུལ་པའི་སྣང་བ་ནི། །\nསྒྲོན་མའི་གནད་ལས་བྱུང་བའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001704",
    "golden": [
      "U03561",
      "U03562",
      "U03563"
    ],
    "tibetan": "ངག་ཏུ་ཅི་ལྟར་སྨྲས་པ་ཀུན། །\nགསང་སྔགས་གསང་བའི་བཟླས་པ་སྟེ། །\nཡི་གེའི་རྣམ་འཕྲུལ་གནད་ལས་བྱུང་། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001706",
    "golden": [
      "U03566",
      "U03567"
    ],
    "tibetan": "རང་སེམས་རྟོགས་ལས་གྲོལ་བས་ན། །\nདེ་ནི་འབྱུང་བའི་གནད་ལས་བྱུང༌། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001709",
    "golden": [
      "U03572",
      "U03573"
    ],
    "tibetan": "བྱ་བྱེད་བརྗོད་དང་བསམ་པ་ལས། །\nའཁོར་འདས་གྲོལ་བའི་གནད་བརྟགས་ཏེ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001719",
    "golden": [
      "U03592",
      "U03593",
      "U03594",
      "U03595",
      "U03596"
    ],
    "tibetan": " ས་བོན་ལས་ནི་འབྲས་བུ་བཞིན།།\n རང་གི་རང་བཞིན་གཤིས་ཀྱི་གནད།།\n  བརྗོད་པའི་ཚིག་གིས་མ་ཡིན་པར། །\nདབང་པོ་ཡུལ་ལ་གསལ་སྣང་བས། །\nཅེར་མཐོང་གྲོལ་བའི་བདག་ཉིད་དོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001731",
    "golden": [
      "U03610",
      "U03611",
      "U03612",
      "U03613"
    ],
    "tibetan": "དེ་ཡང་ཆོས་ཉིད་མངོན་སུམ་གནད། །\nམཐོང་བ་ཙམ་གྱིས་ཤེས་པ་དང༌། །\nཤེས་པ་ཡིས་ནི་རྟོགས་པ་དང༌། །\nརྟོགས་པ་ཙམ་གྱིས་གྲོལ་བར་འགྱུར། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad in the actual technical key-point construction; preserve explicit counts, modifiers and rhetorical or instructional force.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001637",
    "golden": [
      "U03429",
      "U03430",
      "U03431"
    ],
    "tibetan": "དུས་དང་ཐབས་དང་གནད་དང་ཚིག །\nདེ་ཡི་རང་བཞིན་འཇུག་པ་ཡིས། །\nའབྱུང་བའི་གནད་ཀྱི་མན་ངག་རྫོགས། །",
    "before": "method, crucial point, and word,",
    "after": "method, key point, and word,",
    "rationale": "P2 gnad in the four-item list; the separate tshig construction remains qualified under U12, not silently relabeled.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001637",
    "golden": [
      "U03429",
      "U03430",
      "U03431"
    ],
    "tibetan": "དུས་དང་ཐབས་དང་གནད་དང་ཚིག །\nདེ་ཡི་རང་བཞིན་འཇུག་པ་ཡིས། །\nའབྱུང་བའི་གནད་ཀྱི་མན་ངག་རྫོགས། །",
    "before": "the elements' crucial points",
    "after": "the elements' key points",
    "rationale": "P2 gnad in the second occurrence of this pair, preserving the genitive elements and pith instructions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T01",
    "pair": "DTG-001735",
    "golden": [
      "U03621",
      "U03622"
    ],
    "tibetan": "ཞེས་སྒྲ་ཐལ་འགྱུར་ཆེན་པོ་ཆོས་རྣམས་ཀུན་གྱི་རྩ་བ་ལས།\n གནད་འདུས་བཀོད་པ་རིག་པའི་རྩ་བ་ངེས་པར་འབྱུང་བའི་ལེའུ་སྟེ་གཉིས་པའོ།།",
    "before": "Gathered Crucial Points",
    "after": "Gathered Key Points",
    "rationale": "P2 gnad in the current chapter-colophon title, preserving gathered, array, the root of awareness and the source second-chapter designation.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T02",
    "pair": "DTG-001559",
    "golden": [
      "U03296",
      "U03297",
      "U03298",
      "U03299",
      "U03300"
    ],
    "tibetan": "ལུས་ཀྱི་དུས་ནི་འདི་ལྟ་སྟེ། །\nའབྱུང་བ་འདུས་པའི་ཕུང་པོ་ཡི། །\nཙིཏྟ་རིན་ཆེན་གཞལ་ཡས་ན། །\nངོ་བོ་ཀ་ནས་དག་པའི་ཆ། །\nསྟོང་གསལ་འདུས་པ་སྐུ་ཡི་གདངས། །",
    "before": "within the precious palace of the heart (citta),",
    "after": "within the precious palace of citta,",
    "rationale": "P2 retention for tsitta. The body/palace description does not independently establish an anatomical heart referent; retain that possibility in N-144/N-T62 rather than asserting it as a gloss.",
    "severity": "moderate interpretation",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001564",
    "golden": [
      "U03310",
      "U03311",
      "U03312",
      "U03313"
    ],
    "tibetan": "དྭངས་མ་འདུས་པའི་མིག་གཉིས་ནས། །\nཐབས་དང་ཤེས་རབ་ཁྱད་པར་ལས། །\nཇི་ལྟར་མཁྱེན་པའི་ཐིག་ལེ་དང་། །\nདག་པ་དབྱིངས་ཀྱི་སྒྲོན་མར་སྨིན། །",
    "before": "where the refined parts gather",
    "after": "where the pure extract gathers",
    "rationale": "P2 dwangs ma in the gathered eye-door account, with mass-number agreement and both explicit eyes retained. No separate part noun requires the exception.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001614",
    "golden": [
      "U03396",
      "U03397",
      "U03398"
    ],
    "tibetan": "འབྱུང་བ་དྭངས་སྙིགས་འབྱེད་འདོད་པས། །\nདོན་དམ་ཀུན་རྫོབ་དབྱེ་བ་ལས། །\nའབྱུང་བ་ལ་ཡང་གཉིས་སུ་འདུས། །",
    "before": "the refined and turbid parts of the elements",
    "after": "the pure extract and residue of the elements",
    "rationale": "The explicit whole dwangs snyigs introduces the following complete four-element series. Preserve both members and their source order under P2; the two-truth label question is separate.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001616",
    "golden": [
      "U03400"
    ],
    "tibetan": "ས་ཡི་སྙིགས་མ་རགས་པ་ལས། །",
    "before": "'s turbid part",
    "after": "'s residue",
    "rationale": "The explicitly introduced dwangs snyigs pair at U03396 identifies snyigs ma as its residue member in this elemental series. Each elemental genitive and distinct predicate is preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001621",
    "golden": [
      "U03407"
    ],
    "tibetan": "ཆུ་ཡི་སྙིགས་མས་རླན་ཞིང་སྡུད། །",
    "before": "'s turbid part",
    "after": "'s residue",
    "rationale": "The explicitly introduced dwangs snyigs pair at U03396 identifies snyigs ma as its residue member in this elemental series. Each elemental genitive and distinct predicate is preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001626",
    "golden": [
      "U03414"
    ],
    "tibetan": "མེ་ཡི་སྙིགས་མས་བསྲེག་ཅིང་མཆེད། །",
    "before": "'s turbid part",
    "after": "'s residue",
    "rationale": "The explicitly introduced dwangs snyigs pair at U03396 identifies snyigs ma as its residue member in this elemental series. Each elemental genitive and distinct predicate is preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001619",
    "golden": [
      "U03403",
      "U03404",
      "U03405"
    ],
    "tibetan": "དྭངས་མས་ལུས་ཟུངས་རྫོགས་པ་དང་། །\nདོན་དམ་བྱང་སེམས་སྤེལ་བ་དང༌། །\nརྒྱང་ཞགས་སྒྲོན་མར་སྨིན་པ་དང༌། །",
    "before": "The refined part",
    "after": "The pure extract",
    "rationale": "P2 dwangs ma as the distinct extract member of the complete series. The different maturation, bodily and lamp predicates remain; no efficacy or anatomical identity is supplied.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001624",
    "golden": [
      "U03410",
      "U03411",
      "U03412"
    ],
    "tibetan": "དྭངས་མས་རྒ་ཤི་ཟིལ་གནོན་དང༌། །\nབྱེད་ལས་ཆོས་ཉིད་བརྟན་པ་དང་། །\nཤེས་རབ་སྒྲོན་མར་སྨིན་པ་དང༌། །",
    "before": "The refined part",
    "after": "The pure extract",
    "rationale": "P2 dwangs ma as the distinct extract member of the complete series. The different maturation, bodily and lamp predicates remain; no efficacy or anatomical identity is supplied.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001629",
    "golden": [
      "U03417",
      "U03418"
    ],
    "tibetan": "དྭངས་མས་ངག་ལུས་རྫོགས་པ་དང་། །\nཐིག་ལེའི་སྒྲོན་མར་སྨིན་པ་དང་། །",
    "before": "The refined part",
    "after": "The pure extract",
    "rationale": "P2 dwangs ma as the distinct extract member of the complete series. The different maturation, bodily and lamp predicates remain; no efficacy or anatomical identity is supplied.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T03",
    "pair": "DTG-001631",
    "golden": [
      "U03421"
    ],
    "tibetan": "རླུང་གི་སྙིགས་མས་དྭངས་འབྱེད་བསྐྱོད། །",
    "before": "Wind's turbid part separates the refined parts and moves [them].",
    "after": "Wind's residue separates the pure extract and moves [it].",
    "rationale": "Both explicitly contrasted members occur in this clause; short dwangs is identified by the full series, not reconstructed from arbitrary syllables. The moved object remains bracketed; mass-number agreement changes them to it, without resolving the existing attachment question.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-S01",
    "pair": "DTG-001634",
    "golden": [
      "U03424"
    ],
    "tibetan": "དྭངས་མས་སེམས་བདེ་ནུས་པ་དང༌།",
    "before": "The refined part gives ordinary mind ease and capacity.",
    "after": "The pure extract can give ordinary mind ease.",
    "rationale": "P2 pure extract plus grammatical repair: in dwangs mas sems bde nus pa dang, nus pa qualifies ability to bring ordinary mind ease; there is no intervening conjunction that gives mind an additional outcome called capacity. The final dang continues the following activity statement. Preserve the ability, recipient and ease without adding a second object or a demonstrated physiological effect.",
    "severity": "moderate meaning",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B11-C01",
    "pair": "DTG-001564",
    "golden": [
      "U03310",
      "U03311",
      "U03312",
      "U03313"
    ],
    "tibetan": "དྭངས་མ་འདུས་པའི་མིག་གཉིས་ནས། །\nཐབས་དང་ཤེས་རབ་ཁྱད་པར་ལས། །\nཇི་ལྟར་མཁྱེན་པའི་ཐིག་ལེ་དང་། །\nདག་པ་དབྱིངས་ཀྱི་སྒྲོན་མར་སྨིན། །",
    "before": "the distinction of methods and discerning knowing",
    "after": "the distinction of means and discerning knowing",
    "rationale": "I §8.1 U08: the two-eyes/two-lamp account uses the abstract technical polarity rather than distinct procedures. Means is justified locally, as in the paired-portions construction at U03041; method remains in procedural time/example lists.",
    "severity": "minor construction",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001546",
    "golden": [
      "U03275"
    ],
    "tibetan": "འཁོར་བ་འདས་པ་ཆད་པ་མིན། །",
    "before": "Samsara and passing beyond",
    "after": "Cyclic existence and passing beyond [sorrow]",
    "rationale": "P2 khor ba and locally identifiable short das pa: the immediately following mirror-reflection khor das and the just-read embodiment/liberation sequence establish this contrast. The omitted sorrow component is visible in brackets. Negation and noncessation remain.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001548",
    "golden": [
      "U03277",
      "U03278"
    ],
    "tibetan": "ཡུལ་དངོས་དག་པས་མེ་ལོང་སྟེ། །\nའཁོར་འདས་གཟུགས་བརྙན་གསལ་བའོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 recorded khor das compound; retain both members and their reflection, desire or liberation relation, without supplying a doctrine to resolve the existing syntax.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001693",
    "golden": [
      "U03539",
      "U03540"
    ],
    "tibetan": "ལ་ལ་འཁོར་འདས་འདོད་པ་ཡང་། །\nབདེན་པ་གཉིས་ལས་སེམས་གཉིས་འཁྲུལ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 recorded khor das compound; retain both members and their reflection, desire or liberation relation, without supplying a doctrine to resolve the existing syntax.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001709",
    "golden": [
      "U03572",
      "U03573"
    ],
    "tibetan": "བྱ་བྱེད་བརྗོད་དང་བསམ་པ་ལས། །\nའཁོར་འདས་གྲོལ་བའི་གནད་བརྟགས་ཏེ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "P2 recorded khor das compound; retain both members and their reflection, desire or liberation relation, without supplying a doctrine to resolve the existing syntax.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001639",
    "golden": [
      "U03433",
      "U03434",
      "U03435"
    ],
    "tibetan": "སྒྲོན་མ་གཏེམས་པ་འདི་ལྟ་སྟེ། །\nདད་ལྡན་འཁོར་བའི་ཡིད་བྲལ་བས། །\nབླ་མ་མཆོད་དང་གཏོར་མ་བྱ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 actual technical khor ba, including the current translated name in U03619, not a historical English quotation. Ordinary ma das beyond-body in U03577 is excluded.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001640",
    "golden": [
      "U03436",
      "U03437",
      "U03438"
    ],
    "tibetan": "འཁོར་བའི་འབྲེལ་པ་ཀུན་སྤངས་ཏེ། །\nདབེན་པའི་ཕྱོགས་སམ་དུར་ཁྲོད་དུ། །\nགྲོགས་སྤང་གཅིག་པུར་གནས་པར་བྱ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 actual technical khor ba, including the current translated name in U03619, not a historical English quotation. Ordinary ma das beyond-body in U03577 is excluded.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001711",
    "golden": [
      "U03575"
    ],
    "tibetan": "ཁམས་གསུམ་འཁོར་བ་དོང་སྤྲུགས་སོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 actual technical khor ba, including the current translated name in U03619, not a historical English quotation. Ordinary ma das beyond-body in U03577 is excluded.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001721",
    "golden": [
      "U03599",
      "U03600"
    ],
    "tibetan": "རང་སྣང་ཡེ་ཤེས་ཆོས་མཐུན་ཕྱིར། །\nའཁོར་བ་ཡེ་ནས་ཡོད་མ་ཡིན། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 actual technical khor ba, including the current translated name in U03619, not a historical English quotation. Ordinary ma das beyond-body in U03577 is excluded.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T04",
    "pair": "DTG-001734",
    "golden": [
      "U03618",
      "U03619",
      "U03620"
    ],
    "tibetan": "མངོན་སུམ་མཐོང་བའི་སྐལ་ལྡན་ལ། །\nཁམས་གསུམ་འཁོར་བའི་མིང་མེད་པས། །\nསྲིད་གསུམ་གདར་ཤ་ཆོད་པའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "P2 actual technical khor ba, including the current translated name in U03619, not a historical English quotation. Ordinary ma das beyond-body in U03577 is excluded.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T05",
    "pair": "DTG-001712",
    "golden": [
      "U03576",
      "U03577",
      "U03578"
    ],
    "tibetan": "གཞན་ཡང་ཁམས་གསུམ་སེམས་ཅན་ཀུན། །\nལུས་ངག་ཡིད་ལས་མ་འདས་པས། །\nསྐུ་གསུམ་གཞན་དུ་བཙལ་མི་དགོས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent; preserve each plural/quantifier, condition and negative or identity claim. Bare sems, gro ba and lus can remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T05",
    "pair": "DTG-001715",
    "golden": [
      "U03582",
      "U03583"
    ],
    "tibetan": "ངོ་མཚར་ཆེན་པོའི་རོལ་པ་ནི། །\nསངས་རྒྱས་སེམས་ཅན་འབྱེད་པ་མེད། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent; preserve each plural/quantifier, condition and negative or identity claim. Bare sems, gro ba and lus can remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T05",
    "pair": "DTG-001717",
    "golden": [
      "U03586",
      "U03587",
      "U03588",
      "U03589"
    ],
    "tibetan": "ཆོས་ཉིད་མངོན་སུམ་ཁྱད་པར་གྱིས། །\nདབང་པོ་རྣོ་དང་བརྟུལ་མེད་པས། །\nསེམས་ཅན་ཐམས་ཅད་སངས་རྒྱས་ལས། །\nགཞན་དུ་གནས་པ་མ་ཡིན་ནོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent; preserve each plural/quantifier, condition and negative or identity claim. Bare sems, gro ba and lus can remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T05",
    "pair": "DTG-001720",
    "golden": [
      "U03597",
      "U03598"
    ],
    "tibetan": "གཞན་ཡང་རྐྱེན་གྱིས་སེམས་ཅན་རྣམས། །\nསངས་མ་རྒྱས་པ་གཅིག་ཀྱང་མེད། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent; preserve each plural/quantifier, condition and negative or identity claim. Bare sems, gro ba and lus can remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T05",
    "pair": "DTG-001730",
    "golden": [
      "U03609"
    ],
    "tibetan": "དེས་ན་སེམས་ཅན་སངས་རྒྱས་སོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 complete sems can equivalent; preserve each plural/quantifier, condition and negative or identity claim. Bare sems, gro ba and lus can remain distinct.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T05",
    "pair": "DTG-001718",
    "golden": [
      "U03590",
      "U03591"
    ],
    "tibetan": "ལུས་ཅན་སེམས་ཀྱིས་ཁྱབ་པའི་ཕྱིར། །\nསངས་རྒྱས་མ་ཡིན་སེམས་ཅན་མིན། །",
    "before": "a sentient being",
    "after": "a karmic being",
    "rationale": "P2 singular sems can. The two negative predicates are intentionally left without an invented connective; N-157 retains the exact unresolved logical relation.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T06",
    "pair": "DTG-001703",
    "golden": [
      "U03558",
      "U03559",
      "U03560"
    ],
    "tibetan": "གཞན་ཡང་ལུས་ཀྱི་སྤྱོད་ལམ་ཉིད། །\nསྐུ་གསུམ་དག་ཏུ་གྲོལ་བའི་ཕྱིར། །\nབྱ་བྱེད་ཐམས་ཅད་ཆོས་ཉིད་དོ། །",
    "before": "actions and agents",
    "after": "doing and doers",
    "rationale": "P2 action/agent realization supported locally by the bodily-conduct and liberated doing/agent contrast continued from U03115–17. Both members remain rather than collapsing to actions, and no new named agent is introduced. This does not assign the same analysis to the different byed pai las construction at U03496.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-T06",
    "pair": "DTG-001709",
    "golden": [
      "U03572",
      "U03573"
    ],
    "tibetan": "བྱ་བྱེད་བརྗོད་དང་བསམ་པ་ལས། །\nའཁོར་འདས་གྲོལ་བའི་གནད་བརྟགས་ཏེ། །",
    "before": "actions and agents",
    "after": "doing and doers",
    "rationale": "P2 action/agent realization supported locally by the bodily-conduct and liberated doing/agent contrast continued from U03115–17. Both members remain rather than collapsing to actions, and no new named agent is introduced. This does not assign the same analysis to the different byed pai las construction at U03496.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-S02",
    "pair": "DTG-001677",
    "golden": [
      "U03506",
      "U03507",
      "U03508"
    ],
    "tibetan": "བྱེད་ལས་རླུང་གི་གྲངས་ཚད་ཀྱིས། །\nམ་འཁྲུལ་པ་ལ་ཆོས་ཉིད་དང་། །\nམ་དག་ལས་ཀྱི་བྱེ་བྲག་སྟོན། །",
    "before": "Through the numerical measure of wind's activities,",
    "after": "As for activity, through the numerical measure of wind,",
    "rationale": "The head governed by rlung gi is grang tshad, the numerical measure of wind; byed las precedes it as the activity topic. The old possessive made activities the counted head. Keep the following bracketed subject and purity/impurity qualification provisional; do not invent a numerical breathing rate.",
    "severity": "moderate meaning",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-S03",
    "pair": "DTG-001681",
    "golden": [
      "U03517",
      "U03518"
    ],
    "tibetan": "ཡུལ་ནི་ཡོད་དང་མེད་པ་དང༌། །\nའགྲོ་དང་འོང་བའི་གནད་ཀྱིས་བསམ། །",
    "before": "For objects, reflect on existence and nonexistence,\nand the key point of going and coming.",
    "after": "For objects, reflect through the key point\nof existence and nonexistence, and going and coming.",
    "rationale": "Gnad kyis is instrumental and its genitive governs the coordinated objects; the old on made key point another object of reflection and reduced its scope to going/coming. Retain both contrasts and the instructional verb without supplying a technique.",
    "severity": "moderate meaning",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B11-L01",
    "pair": "DTG-001641",
    "golden": [
      "U03439",
      "U03440",
      "U03441"
    ],
    "tibetan": "གསུམ་པོ་བརྟེན་པ་མ་ཡིན་པར། །\nརང་གི་མཐེབ་དང་མཛུབ་མོ་ཡིས། །\nཐིག་ལེ་སྟོང་པའི་སྒྲོན་མ་གཏེམས། །",
    "before": "forefinger—[Editorial note: Do not infer or perform eye pressure from this draft.]",
    "after": "forefinger,",
    "rationale": "The explicitly editorial warning has no Tibetan source clause and belongs in the already linked N-150, which already warns against eye pressure. Preserve it verbatim in the appended active disposition, retain both N-150 links, and repair only the connective punctuation. Do not remove or expand the source instruction.",
    "severity": "moderate layer separation",
    "confidence": "high"
  },
  {
    "finding": "PD-B11-L01",
    "pair": "DTG-000846",
    "golden": [
      "U01899",
      "U01900"
    ],
    "tibetan": "ཕྱི་ནང་དབུགས་ནི་རྒྱུན་བཅད་ནས། །\nརྣམ་པར་རྟོག་པ་ཐམས་ཅད་འགགས། །",
    "before": " [Editorial note: Do not attempt breath cessation from this draft.]",
    "after": "",
    "rationale": "Whole-work search found this second and only other literal inline Editorial note. Current Tibetan, neighboring pairs and N-085 were reread. Preserve the warning verbatim in the linked note disposition, not in main translation prose. The earlier review correctly recognized the wording as editorial but had not relocated it; do not rewrite that history.",
    "severity": "moderate layer separation",
    "confidence": "high"
  }
]
```

<!-- phase-d-batch-11-annotation-operations -->
```json
[
  {
    "finding": "PD-B11-N01",
    "note": "G-U03622",
    "linked_pair": "DTG-001735",
    "tibetan": " གནད་འདུས་བཀོད་པ་རིག་པའི་རྩ་བ་ངེས་པར་འབྱུང་བའི་ལེའུ་སྟེ་གཉིས་པའོ།།",
    "before": "**Current English:** `\"this is the second chapter: ‘Array of Gathered Crucial Points: The Definite Arising of the Root of Awareness.’ [N-158]\"`",
    "after": "**Current English:** `\"this is the second chapter: ‘Array of Gathered Key Points: The Definite Arising of the Root of Awareness.’ [N-158]\"`",
    "rationale": "Keep the active Current English quote consistent with the canonical colophon repair. Exact Tibetan, Previous English and the unresolved boundary graphic remain unchanged.",
    "severity": "minor note consistency",
    "confidence": "high"
  }
]
```

<a id="phase-d-notes-11"></a>
#### Active-note dispositions and whole-work pattern extension

```json
[
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-143",
    "pairs": [
      "DTG-001546",
      "DTG-001548",
      "DTG-001554",
      "DTG-001555"
    ],
    "ids": [
      "U03275",
      "U03277",
      "U03278",
      "U03284",
      "U03285",
      "U03286",
      "U03287"
    ],
    "realization": "full cyclic-existence contrast; two knowings",
    "status": "Approved labels; connected account completed",
    "reason": "The remainder of the seventeenth reply was read through its final number-of-training-embodiments conclusion. The locally identified passing-beyond short form preserves a bracketed sorrow complement; the mirror clause keeps both sides of khor das. Knowing how and knowing multiplicity remain separate local constructions with supplied things visibly bracketed; no extra embodiment or anatomical identity is introduced.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T80",
    "pairs": [
      "DTG-001548",
      "DTG-001549",
      "DTG-001550",
      "DTG-001551",
      "DTG-001552",
      "DTG-001563"
    ],
    "ids": [
      "U03277",
      "U03278",
      "U03279",
      "U03280",
      "U03281",
      "U03282",
      "U03304",
      "U03305",
      "U03306",
      "U03307",
      "U03308",
      "U03309"
    ],
    "realization": "five distinct primordial-knowing names",
    "status": "Local abbreviated-list identity supported; new full names remain proposals",
    "reason": "The abbreviated predicates U03277–82 are explicitly named together as ye shes at U03306–07. That supports the local short-form identification, including established discriminating primordial knowing, without rewriting rtogs as rtog in Tibetan. The mirror-like, evenness, activity-accomplishing and basic-space-of-phenomena names remain separate shared-label proposals, not new glossary assignments. The later syllabic explanations U04049–85 are still outside this batch and must be checked separately.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T81",
    "pairs": [
      "DTG-001554",
      "DTG-001555",
      "DTG-001560",
      "DTG-001564",
      "DTG-001565",
      "DTG-001588",
      "DTG-001592"
    ],
    "ids": [
      "U03284",
      "U03285",
      "U03286",
      "U03287",
      "U03301",
      "U03310",
      "U03311",
      "U03312",
      "U03313",
      "U03314",
      "U03315",
      "U03356",
      "U03361",
      "U03362"
    ],
    "realization": "knowing how/multiplicity; vase embodiment; basis",
    "status": "Local constructions distinguished; wordplay lexical question open",
    "reason": "The actual paired knowing/lamp predicates support two kinds of knowing locally, with no youthful added to bum sku. The explicitly explained kun/gzhi components support lower-case basis in that explanation, not a global change to technical Ground. The lettered subdivisions and conjunctions remain provisional. Sogs pa at U03362 requires the separate exact lexical check in N-147, rather than a silently supplied gsogs spelling.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-144",
    "pairs": [
      "DTG-001558",
      "DTG-001559",
      "DTG-001563",
      "DTG-001564",
      "DTG-001565",
      "DTG-001566"
    ],
    "ids": [
      "U03292",
      "U03293",
      "U03294",
      "U03295",
      "U03296",
      "U03297",
      "U03298",
      "U03299",
      "U03300",
      "U03304",
      "U03305",
      "U03306",
      "U03307",
      "U03308",
      "U03309",
      "U03310",
      "U03311",
      "U03312",
      "U03313",
      "U03314",
      "U03315",
      "U03316",
      "U03317",
      "U03318"
    ],
    "realization": "key point; citta; pure extract; means",
    "status": "Approved labels and supported polarity; channel syntax remains provisional",
    "reason": "P2 retains citta without an unestablished heart gloss and pure extract in the two-eye description. U08 supports means in the technical pairing, not a collection of methods. Four named channels, five knowings, moving/nonmoving spheres and both two-lamp groupings are preserved; the conjunctions, completion supports, body-time relation and final faculty/training relation still need source-based attachment analysis. No fifth channel or youthful embodiment is inserted.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T62",
    "pairs": [
      "DTG-001559"
    ],
    "ids": [
      "U03296",
      "U03297",
      "U03298",
      "U03299",
      "U03300"
    ],
    "realization": "citta",
    "status": "Retention extended to the repeated palace passage",
    "reason": "The current body-time/palace passage does not independently establish heart; the proposal remains a possibility in historical notes, not a default. This is the same scoped retention control applied to U02868 and G-U02885, with no change to actual eye/caksu identifications.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-145",
    "pairs": [
      "DTG-001568",
      "DTG-001569",
      "DTG-001570",
      "DTG-001571",
      "DTG-001573",
      "DTG-001575"
    ],
    "ids": [
      "U03320",
      "U03321",
      "U03322",
      "U03323",
      "U03324",
      "U03325",
      "U03326",
      "U03327",
      "U03328",
      "U03329",
      "U03332",
      "U03333",
      "U03337",
      "U03338"
    ],
    "realization": "two abidings; unpartitioned embodiments; leaving constructions",
    "status": "No-change: distinctions and qualified attachment retained",
    "reason": "The initial Ground and delusion-object abidings, three aspects, three embodiments and five colors remain distinct. Bab las grub and shes byai bab may express an already-given condition rather than a process produced from a cause; current from its own condition stays provisional pending a full idiomatic construction determination. Rang bzhag/cog bzhag/sealing retain their separate heads and unresolved relation, not an imported standard exposition.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-146",
    "pairs": [
      "DTG-001577",
      "DTG-001578",
      "DTG-001579",
      "DTG-001585"
    ],
    "ids": [
      "U03340",
      "U03341",
      "U03342",
      "U03343",
      "U03344",
      "U03345",
      "U03351",
      "U03352"
    ],
    "realization": "repeated demonstratives; one/many",
    "status": "No-change: unresolved referents remain explicit",
    "reason": "U03343 still repeats de without identified antecedents; face/image/liberation alternatives cannot be chosen solely from the mirror simile. The distinctions of seeing, knowing and awareness and all one/two/three/many negations are retained. A linked commentary or explicit parallel identifying each demonstrative would settle the construction, not a fluent paraphrase.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-147",
    "pairs": [
      "DTG-001587",
      "DTG-001591",
      "DTG-001592",
      "DTG-001598",
      "DTG-001599"
    ],
    "ids": [
      "U03354",
      "U03355",
      "U03359",
      "U03360",
      "U03361",
      "U03362",
      "U03368",
      "U03369",
      "U03370",
      "U03371",
      "U03372"
    ],
    "realization": "key point; basis; explicit word explanation",
    "status": "Labels repaired; PD-Q11-01 lexical span retained provisionally",
    "reason": "At U03362, གཞི་ནི་ཚོགས་ཤིང་སོགས་པའོ།, current assembling and accumulating may read sogs as an accumulation verb, whereas assembling and so forth follows the usual conjunction/list reading. The fixed spelling is sogs, not gsogs. Its word-explanatory function alone does not authorize emendation or settle a variant lexical use; retain the linked provisional English until an attested use/parallel resolves this. Category identities, arbitrary-holding and the final method/example/measure relation remain qualified.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-148",
    "pairs": [
      "DTG-001601",
      "DTG-001602",
      "DTG-001604",
      "DTG-001605",
      "DTG-001611",
      "DTG-001612"
    ],
    "ids": [
      "U03374",
      "U03375",
      "U03376",
      "U03377",
      "U03379",
      "U03380",
      "U03381",
      "U03387",
      "U03388",
      "U03389",
      "U03390",
      "U03391",
      "U03392",
      "U03393",
      "U03394"
    ],
    "realization": "ordinary mind/primordial knowing; verbal think",
    "status": "Approved label; four roles and support scope still provisional",
    "reason": "The explicit etymology supports sems as a verb without replacing the canonical noun. At U03380–81, གང་ལ་སེམས་དང་གང་གིས་སེམས། གང་སེམས་པ་དང་གང་ཕྱིར་སེམས།, what thinks versus what is thought in the third member, and instrument versus agent in the second, remain exact role alternatives (PD-Q11-02), requiring an explicit question/answer parallel. The current Ground of mindfulness/reflection at U03377 could be a support rather than technical Ground; it remains provisional pending the counted/functional referent. The nominal ending is not an accidental English fragment to repair with invented verbs.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T83",
    "pairs": [
      "DTG-001604",
      "DTG-001605"
    ],
    "ids": [
      "U03379",
      "U03380",
      "U03381"
    ],
    "realization": "think; what is recalled",
    "status": "Local grammatical use supported; role assignment not settled",
    "reason": "Verbal sems in the explicit word explanation and recalled-object dran yul are not the noun ordinary mind and standalone mindfulness respectively. Retain their locally grammatical uses; the four interrogative roles and recalled-object attachment remain qualified in N-148. No new shared psychological definition is adopted.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-149",
    "pairs": [
      "DTG-001614",
      "DTG-001616",
      "DTG-001619",
      "DTG-001621",
      "DTG-001624",
      "DTG-001626",
      "DTG-001629",
      "DTG-001630",
      "DTG-001631",
      "DTG-001634",
      "DTG-001636",
      "DTG-001637"
    ],
    "ids": [
      "U03396",
      "U03397",
      "U03398",
      "U03400",
      "U03403",
      "U03404",
      "U03405",
      "U03407",
      "U03410",
      "U03411",
      "U03412",
      "U03414",
      "U03417",
      "U03418",
      "U03419",
      "U03420",
      "U03421",
      "U03424",
      "U03427",
      "U03428",
      "U03429",
      "U03430",
      "U03431"
    ],
    "realization": "pure extract/residue; ability to give ease; key points",
    "status": "Complete elemental label series repaired; ability scope corrected",
    "reason": "The whole dwangs snyigs introduction establishes both members across all four elemental paragraphs, including short dwangs at U03421. U03424 says the extract can give ordinary mind ease, not that ordinary mind separately receives capacity; only that grammatical defect is resolved. The moved object remains bracketed, and coarse/fine particle transitions, ultimate byang sems, final time/method/word relation and physiological interpretations remain provisional. Meditative stability is tested under U06 for the cultivated sleep state but the existing stabilization wording is not changed merely as a preferred synonym. The source claims are not medical or nutritional findings.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T82",
    "pairs": [
      "DTG-001619"
    ],
    "ids": [
      "U03403",
      "U03404",
      "U03405"
    ],
    "realization": "ultimate awakening ordinary mind",
    "status": "Unresolved whole expression; no component reconstruction",
    "reason": "The explicit don dam byang sems is not settled by the ordinary-mind component or the ultimate/relative headings. Its bodily, aspirational or other technical sense, and the paired U10 superficial/superfactual proposal, require a source-linked whole-expression decision. The bracket-linked existing proposal is retained, not promoted to a local or shared default.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T84",
    "pairs": [
      "DTG-001627",
      "DTG-001632",
      "DTG-001650",
      "DTG-001654",
      "DTG-001658"
    ],
    "ids": [
      "U03415",
      "U03422",
      "U03458",
      "U03467",
      "U03468",
      "U03469",
      "U03470",
      "U03476"
    ],
    "realization": "particle names; provisional measures; father/mother",
    "status": "No-change: contextual limitations retained",
    "reason": "The elemental particle names and subsequent size progression support preserving these exact proposals, not hair-tip ratios, physical dimensions, a finger procedure, blanket material or sexual activity. The two/three grouping and fingerbreadth reading remain provisional; parent designations do not authorize adding consort identities.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-150",
    "pairs": [
      "DTG-001639",
      "DTG-001640",
      "DTG-001641",
      "DTG-001646"
    ],
    "ids": [
      "U03433",
      "U03434",
      "U03435",
      "U03436",
      "U03437",
      "U03438",
      "U03439",
      "U03440",
      "U03441",
      "U03450",
      "U03451",
      "U03452"
    ],
    "realization": "cyclic existence; editorial warning in note layer",
    "status": "Layer repair; source instruction and warning both preserved",
    "reason": "The source gives thumb and forefinger but no pressure target or complete procedure. The embedded editorial warning is removed from translation prose and retained here verbatim: Do not infer or perform eye pressure from this draft. Both existing note links remain. The three supports and three-appearance grouping remain unidentified; the canonical direct-perception vision does not prove the later appearance phrases are the four-vision list.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-085",
    "pairs": [
      "DTG-000846"
    ],
    "ids": [
      "U01899",
      "U01900"
    ],
    "realization": "editorial breath warning in note layer",
    "status": "Whole-work matching layer repair; prior history retained",
    "reason": "The literal Editorial note search found exactly two root-prose occurrences in the whole current English: DTG-000846 and DTG-001641. This earlier pair and its neighbors were reread. Preserve the warning here verbatim: Do not attempt breath cessation from this draft. The source breath-flow clause and all conceptualization remain, with both N-085 links; no hazardous instruction is expanded. The previous disposition recognized the sentence as editorial but did not relocate it; that historical record remains unchanged.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-151",
    "pairs": [
      "DTG-001649",
      "DTG-001650",
      "DTG-001651",
      "DTG-001653",
      "DTG-001654",
      "DTG-001657",
      "DTG-001660",
      "DTG-001662",
      "DTG-001663"
    ],
    "ids": [
      "U03455",
      "U03456",
      "U03457",
      "U03458",
      "U03459",
      "U03460",
      "U03461",
      "U03462",
      "U03465",
      "U03466",
      "U03467",
      "U03468",
      "U03469",
      "U03470",
      "U03474",
      "U03475",
      "U03478",
      "U03479",
      "U03480",
      "U03482",
      "U03483",
      "U03484",
      "U03485",
      "U03486"
    ],
    "realization": "appearance sizes, colors and time",
    "status": "No-change: no standardized vision/count grid imposed",
    "reason": "The full progression retains its exact five-color order, two/three and five/five patterns, comparison objects and days/months/years. Fingerbreadth, patch geometry, nan(g) attachment and the unchanging/individual-time relation remain provisional; no timetable, optical technique or canonical four-vision remapping is supplied.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-152",
    "pairs": [
      "DTG-001665",
      "DTG-001666",
      "DTG-001669",
      "DTG-001670",
      "DTG-001671",
      "DTG-001672"
    ],
    "ids": [
      "U03488",
      "U03489",
      "U03490",
      "U03493",
      "U03494",
      "U03495",
      "U03496",
      "U03497",
      "U03498",
      "U03499",
      "U03500"
    ],
    "realization": "key points; selected Ground; source variant separate",
    "status": "Current-source false positive rejected; PD-Q11-03 agent question retained",
    "reason": "The golden main gzhi yis and separate bzhi yang byung note are already represented correctly; no four is restored into the root and no remainder from 200/115/68 is invented. At U03496, སྨིན་པའི་སྒོ་དང་བྱེད་པའི་ལས།, activities of agents may nominalize byed pa as an agent, whereas activities carried out retains an activity relation without an actor. The parallel door/place/path list alone does not decide; current agent reading stays provisional pending its construction/referent. This is not the P2 byabyed whole pair.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-153",
    "pairs": [
      "DTG-001673",
      "DTG-001674",
      "DTG-001675",
      "DTG-001677",
      "DTG-001678"
    ],
    "ids": [
      "U03501",
      "U03502",
      "U03503",
      "U03504",
      "U03506",
      "U03507",
      "U03508",
      "U03509",
      "U03510"
    ],
    "realization": "activity topic; numerical measure of wind",
    "status": "Genitive/count-head repaired; implicit subject retained",
    "reason": "The complete U03488–U03510 reply was read together. Rlung gi modifies the numerical measure, not byed las, so the counted head is wind. The following supplied these and purity/impure-activity relation remain provisional; body/speech/mental-faculty measures are not rewritten as a breathing rate or physiology.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-154",
    "pairs": [
      "DTG-001680",
      "DTG-001681",
      "DTG-001682",
      "DTG-001683",
      "DTG-001684",
      "DTG-001685"
    ],
    "ids": [
      "U03512",
      "U03513",
      "U03514",
      "U03515",
      "U03516",
      "U03517",
      "U03518",
      "U03519",
      "U03520",
      "U03521",
      "U03522",
      "U03523",
      "U03524",
      "U03525",
      "U03526"
    ],
    "realization": "reflect through the key point",
    "status": "Instrumental scope repaired; remaining instructional syntax retained",
    "reason": "The gnad kyis construction governs both contrasts as the means of reflection, not a second reflected object. The entire outer/body/interval/speech/ordinary-mind sequence remains, including explicit absence of examination in U03526. Speech actions, nonduality of times and the names/particles analysis are still qualified; no rhythm, pressure or intermediate anatomy is supplied.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-155",
    "pairs": [
      "DTG-001689",
      "DTG-001693",
      "DTG-001696",
      "DTG-001698"
    ],
    "ids": [
      "U03530",
      "U03531",
      "U03532",
      "U03539",
      "U03540",
      "U03545",
      "U03546",
      "U03548",
      "U03549"
    ],
    "realization": "full khor das; key point; all-basis contrast",
    "status": "Labels repaired; juxtaposed source positions preserved",
    "reason": "The all-basis definition and later realization as dharma embodiment were read together without reconciling them into permanent identity or absolute separation. Two ordinary minds, two truths, the 120 count and the shadow/intrinsic-nature agent remain unresolved. Counted/support Ground possibilities remain construction questions rather than capitalization-based verdicts.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-156",
    "pairs": [
      "DTG-001702",
      "DTG-001703",
      "DTG-001704",
      "DTG-001705",
      "DTG-001706",
      "DTG-001707",
      "DTG-001709",
      "DTG-001711"
    ],
    "ids": [
      "U03556",
      "U03557",
      "U03558",
      "U03559",
      "U03560",
      "U03561",
      "U03562",
      "U03563",
      "U03564",
      "U03565",
      "U03566",
      "U03567",
      "U03568",
      "U03569",
      "U03570",
      "U03572",
      "U03573",
      "U03575"
    ],
    "realization": "doing/doers; key point; full cyclic-existence contrast",
    "status": "Supported labels; rhetorical contradictions not normalized",
    "reason": "Preserve who has not/why not questions, affirmative delusive appearance from lamps, all conceptual thoughts identified with bsam gtan, and nothing to train/place. U06 meditative stability is tested as the state term but stabilization is retained provisionally rather than changed solely for preference. Rnam phrul at U03563 extends PD-Q10-03 to the letters example, distinct from canonical cho phrul; the shared manifestation/display label remains unresolved. The doing/doer reading is scoped to the continued bodily-action/agent account, not every byed phrase.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-157",
    "pairs": [
      "DTG-001712",
      "DTG-001715",
      "DTG-001717",
      "DTG-001718",
      "DTG-001719",
      "DTG-001720",
      "DTG-001721",
      "DTG-001728",
      "DTG-001730"
    ],
    "ids": [
      "U03576",
      "U03577",
      "U03578",
      "U03582",
      "U03583",
      "U03586",
      "U03587",
      "U03588",
      "U03589",
      "U03590",
      "U03591",
      "U03592",
      "U03593",
      "U03594",
      "U03595",
      "U03596",
      "U03597",
      "U03598",
      "U03599",
      "U03600",
      "U03607",
      "U03609"
    ],
    "realization": "karmic beings; key point; cyclic existence",
    "status": "Approved labels; double-predicate uncertainty preserved",
    "reason": "U03591 still has two negative predicates without a settled connective; the term repair does not turn it into neither/nor or an implication. The source differentiates gro ba, lus can and bare sems from sems can; only the latter changes. All life-stage correspondences, every negation, own-intrinsic-nature and the condition/appearance relation are preserved. Experiential acquaintance is a recognizable local nyams su myong construction, not a replacement for all experience.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-T85",
    "pairs": [
      "DTG-001719",
      "DTG-001728",
      "DTG-001734"
    ],
    "ids": [
      "U03592",
      "U03593",
      "U03594",
      "U03595",
      "U03596",
      "U03607",
      "U03618",
      "U03619",
      "U03620"
    ],
    "realization": "naked seeing; experiential acquaintance; decisively resolved",
    "status": "Local inflection supported; separate expression proposals retained",
    "reason": "Nyams su myong is the recognizable construction of the established experiential-acquaintance entry here. Cer mthong is not silently respelled, and gdar sha chod is not collapsed into differently worded la bzla. Their exact source-linked proposals remain for cross-work reconciliation, with title/settlement comparisons still to follow.",
    "review": "REVIEW.md#phase-d-notes-11"
  },
  {
    "session": "DTG-PD-20261005-Astra-04",
    "legacy_note": "N-158",
    "pairs": [
      "DTG-001731",
      "DTG-001732",
      "DTG-001733",
      "DTG-001734",
      "DTG-001735"
    ],
    "ids": [
      "U03610",
      "U03611",
      "U03612",
      "U03613",
      "U03614",
      "U03615",
      "U03616",
      "U03617",
      "U03618",
      "U03619",
      "U03620",
      "U03621",
      "U03622"
    ],
    "realization": "key points; current colophon title; cyclic-existence name",
    "status": "Labels and active note quote repaired; source layers intact",
    "reason": "The seeing/knowing/realization/liberation progression and space-into-space simile are preserved through the complete Chapter 2 colophon. The causative unbinding contrast does not add a named agent; its force, dmigs med relation and title modifier attachment remain qualified. The exact unresolved boundary graphic stays non-main metadata with no invented verse or chapter heading. Current English in G-U03622 is updated while Previous English and Tibetan remain historical/fixed.",
    "review": "REVIEW.md#phase-d-notes-11"
  }
]
```

**No-change controls:** all counts, the repeated fivefold naming, the distinct four-channel/two-lamp groups, the ma/gzhi word explanations, verse/prose and rhetorical negations remain. Recognized full-entry short forms are not arbitrary component reconstruction; disputed byang sems, ultimate/relative, bsam gtan and manifestation families remain linked proposals. Both historical source-correction examples at U03494 and the Chapter 2 boundary are already correctly layered and are not new defects. Both safety warnings survive in translator-commentary notes rather than disappear or become Tibetan prose.

**Application and verification (same-reviewer self-check):** All 56 recorded English operations in 51 pairs, one active colophon Current English quote repair and 24 append-only dispositions are applied. Every changed clause and necessary neighboring context was reread against current Tibetan in the 103-pair self-check file, all 192 revised English pairs were read continuously, and the complete updated G-U03622 and both newly appended warning dispositions were reread. The extract ability retains ease as its outcome without adding capacity as a second object; the counted head is wind and the reflection instrument governs both contrasts. Both editorial warnings and original note links remain in their proper layer, with no source instruction added or removed. The complete Chapter 2 closing and Chapter 3 opening context remain in source order. Three newly bounded lexical/role questions and inherited unresolved spans remain linked, not certified by coverage.

**Current mechanical preservation checks:** read-only replay passes **408 pair operations** (387 English operations in 343 pair payloads; 21 review-link operations), with **355 changed pairs including note-only changes**. All 4 continuation-04 active footer operations replay exactly; cumulatively there are 3 source-annotation repairs and 2 Current English quote repairs. All 2,667 IDs/order, fixed Tibetan/golden/policy/format/lineage bytes, inherited note associations, historical usage/legacy contents and **700** English local-link targets pass, as does `git diff --check`. Current English SHA-256: `e0cf94a3abf547aa62546ceb893eea13e604ea5bce7304c7504d82399229fcd7`.

**Actual validation/build status:** The most recent actually executed paired suite is **Batch 11: 64 tests, 53 pass, 9 fail, 2 error**. Its historical exact-English gate preempts the affected checks; they are not counted as passed controls. This suite was rerun after this batch. Default paired validation and migration check most recently failed in Batch 10 at the old protected-glossary check. Final paired validation and the projector check/actual regeneration attempt most recently failed in Batch 09 before output writes. Historical contracts and generated readers remain unchanged; no successful regeneration is claimed. These tests do not execute the standard’s 63 semantic regression specifications.

**Coverage checkpoint:** **1742/2,667** pairs through **DTG-001735**, with **371** first-encountered note records read cumulatively. Continue at **ordinal 1743, DTG-001736**. Text remains in review, not whole-work ready.


<a id="phase-d-batch-12"></a>
## Batch 12 — source ordinals 1743–2096

Reviewer/session **DTG-PD-20261005-Astra-05**, review-and-revise. Read every source/English pair in order, **DTG-001736–DTG-002089**, including source headings, across-pair continuations and source layers. 50 newly encountered note records were read with their current dispositions: G-A2000-C03-S01, G-C3-TRANSITION, G-U03673, G-U03802, G-U03803, G-U03851, G-U03945, G-U03946, G-U03952, G-U03953, G-U03954, G-U03955, G-U03976, G-U04305, N-159, N-160, N-161, N-162, N-163, N-164, N-165, N-166, N-167, N-168, N-169, N-170, N-171, N-172, N-173, N-174, N-175, N-176, N-177, N-178, N-179, N-180, N-181, N-182, N-183, N-184, N-185, N-T86, N-T87, N-T88, N-T89, N-T91, N-T92, N-T93, N-T94, N-T97. Q1–Q9, I §8.1 and Part III were applied by reading; subsequent searches test the observed terminology patterns, not replace the reading. The following evidence is recorded before English application.

The whole chapter, including its opening questions, all twenty-three reply headings, syllabic explanations, colophon and unresolved boundary graphic, has now been read. Important rejected false positives: restored ignorance verses are present; main four/twelve are already separate from alternative two/sixty; G-U03946 already preserves uncertain hundred/four grouping; rdzogs is already the selected corrected source. These are not re-reported as current omissions. Acoustic sound, vessel inhabitants, ordinary rdos bcas material weight, descriptive deity names, source wordplay and deliberate repetition are not erased by substring substitutions.

**Readiness limits:** N-165 now explicitly records the potentially major radiance/negation-scope issue at DTG-001817. The title/name attachment (N-159), numerical units (N-160), single-identity ignorance (N-162), causal/object-support grouping (N-163/164), aware/matter coordination (N-165/N-T90), phonetic counts (N-170), primordial-purity attachment (N-173/174), unusual negatives and mar gar/yid ’byung (N-181), instrument identities and sensory syntax (N-184), and the final three/four/graphic (N-185) remain bounded, linked questions. The distinctions and alternatives are recorded below rather than certified away. New shared-label proposals remain with the existing N-T usage records; no template ticket, shared row or book-wide local default is changed.

### Recorded scoped corrections

```json
[
  {
    "finding": "PD-B12-001",
    "pair": "DTG-001778",
    "golden": [
      "U03697",
      "U03698"
    ],
    "tibetan": "འབད་པས་མངོན་སུམ་གནད་གཟིར་བས། །\nམ་བཅོས་གཞི་ལ་གནས་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-002",
    "pair": "DTG-001783",
    "golden": [
      "U03709"
    ],
    "tibetan": "འདི་ནི་ཡེ་ཤེས་གནད་འདུས་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-003",
    "pair": "DTG-001833",
    "golden": [
      "U03821",
      "U03822"
    ],
    "tibetan": "བརྗོད་པ་གནས་དང་འབྱུང་བ་དང་། །\nལས་དང་རྟོག་པ་རང་གནད་དོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-004",
    "pair": "DTG-001835",
    "golden": [
      "U03825",
      "U03826"
    ],
    "tibetan": "དེས་ན་འབྱུང་བའི་རང་གནད་ལས། །\nསེམས་ཅན་ལུས་ཀྱང་ཐ་དད་དོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-005",
    "pair": "DTG-001843",
    "golden": [
      "U03838",
      "U03839",
      "U03840"
    ],
    "tibetan": "བག་རྡུལ་ཆར་གྱིས་དེངས་དུས་སུ། །\nམཁས་པས་མངོན་སུམ་གནད་གཟིར་དང༌། །\nནང་གི་སྒྲོན་མ་ལམ་དུ་བྱའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-006",
    "pair": "DTG-001850",
    "golden": [
      "U03851"
    ],
    "tibetan": "དེ་ཡང་གཞི་ལ་རྫོགས་པའི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-007",
    "pair": "DTG-001863",
    "golden": [
      "U03872",
      "U03873",
      "U03874"
    ],
    "tibetan": "ཁྱད་པར་མིང་གིས་གང་བསྒྱུར་གནད། །\nསོ་སོའི་སྐབས་དང་སྦྱར་བྱས་ནས། །\nབཅོམ་ལྡན་འདས་ཀྱང་འཇིག་པར་འགྱུར། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-008",
    "pair": "DTG-001864",
    "golden": [
      "U03875"
    ],
    "tibetan": "མཐའ་ནི་འབྱུང་བའི་གནད་ཀྱིས་དབྱེ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-009",
    "pair": "DTG-001888",
    "golden": [
      "U03923",
      "U03924"
    ],
    "tibetan": " དེ་ལས་གསུམ་གསུམ་རབ་ཕྱེ་བས། །\nདགུ་སྟེ་ཐེག་དགུ་དབང་པོའི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-010",
    "pair": "DTG-001926",
    "golden": [
      "U03989"
    ],
    "tibetan": "ཡུལ་གནད་དབང་ལ་དབང་གནད་སེམས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-011",
    "pair": "DTG-001927",
    "golden": [
      "U03990"
    ],
    "tibetan": "སེམས་གནད་མིག་ལ་མིག་གནད་རྩ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-012",
    "pair": "DTG-002026",
    "golden": [
      "U04172",
      "U04173"
    ],
    "tibetan": "ཡང་དག་འདུས་པའི་ཡན་ལག་ཏུ། །\nཡེ་ཤེས་གནད་ནི་མིག་ལས་འབྱུང་། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-013",
    "pair": "DTG-002029",
    "golden": [
      "U04179",
      "U04180",
      "U04181",
      "U04182"
    ],
    "tibetan": "གནད་ལས་བྱུང་བའི་ཡེ་ཤེས་གང༌། །\nརིག་ལྡན་ཆོས་ཉིད་ཅི་བཞིན་དུ། །\nརྟོག་པ་ཀུན་ལས་རྣམ་གྲོལ་བས། །\nདབྱིངས་ལས་བྱུང་བའི་ཡེ་ཤེས་སོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-014",
    "pair": "DTG-002030",
    "golden": [
      "U04183",
      "U04184",
      "U04185"
    ],
    "tibetan": "མིག་གི་གནད་ནི་སྟེང་དང་འོག །\nམཁས་པས་རྩོལ་བའི་སྣ་གང་འགྱུར། །\nཀུན་འདུས་ཡེ་ཤེས་སྣང་བའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-015",
    "pair": "DTG-002035",
    "golden": [
      "U04198",
      "U04199",
      "U04200"
    ],
    "tibetan": "གལ་ཏེ་ཁམས་གསུམ་འདས་འདོད་པས། །\nདམ་པའི་ཡེ་ཤེས་གནད་ཆེ་བས། །\nསོ་སོའི་རླུང་གི་དབུགས་སུ་བརྟགས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-016",
    "pair": "DTG-002050",
    "golden": [
      "U04227",
      "U04228",
      "U04229"
    ],
    "tibetan": "ཡང་ནི་རྫོགས་པ་ཆེན་པོ་ཡི། །\nགནད་ཤེས་པ་ལས་ཡེ་ཤེས་ནི། །\nབྱ་བྲལ་ནམ་མཁའ་ཇི་བཞིན་དུ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "The full P2 gnad row requires key point(s). Every listed occurrence is the same explanatory/contemplative key-point noun, not a different sense; all numerals, agents, modifiers and repetitions are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-017",
    "pair": "DTG-001740",
    "golden": [
      "U03630"
    ],
    "tibetan": "སེམས་ཅན་ཐ་དད་ཅི་ཡི་རྒྱུ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-018",
    "pair": "DTG-001824",
    "golden": [
      "U03794",
      "U03795",
      "U03796",
      "U03797",
      "U03798"
    ],
    "tibetan": "སེམས་ཅན་ཀུན་གྱི་ཐ་དད་རྒྱུ། །\nའབྱུང་བའི་རྒྱུ་དང་བྱེད་ལས་དང༌། །\nདབང་པོ་ཉིད་དང་དབྱིབས་དང་ཚད། །\nསྒྲ་དང་སོ་སོའི་བརྗོད་པ་དང༌། །\nགནས་པའི་སྣོད་ཀྱི་བྱེ་བྲག་གོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-019",
    "pair": "DTG-001828",
    "golden": [
      "U03805",
      "U03806",
      "U03807",
      "U03808"
    ],
    "tibetan": "དབང་པོ་མིག་ལ་སོགས་པ་ཡི། །\nདབྱིབས་དང་ཁ་དོག་མི་མཐུན་པས། །\nབཞི་བརྒྱ་དག་དང་བཞི་ཡིས་ཀྱང་། །\nསེམས་ཅན་ལུས་ཀྱང་ཐ་དད་དོ། །",
    "before": "bodies of beings",
    "after": "bodies of karmic beings",
    "rationale": "The body clause explicitly has sems can; retain the approved karmic component, without implying that such beings lack material bodies. Neighboring gro ba is not changed.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-020",
    "pair": "DTG-001835",
    "golden": [
      "U03825",
      "U03826"
    ],
    "tibetan": "དེས་ན་འབྱུང་བའི་རང་གནད་ལས། །\nསེམས་ཅན་ལུས་ཀྱང་ཐ་དད་དོ། །",
    "before": "bodies of beings",
    "after": "bodies of karmic beings",
    "rationale": "The body clause explicitly has sems can; retain the approved karmic component, without implying that such beings lack material bodies. Neighboring gro ba is not changed.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-021",
    "pair": "DTG-001878",
    "golden": [
      "U03899",
      "U03900",
      "U03901",
      "U03902"
    ],
    "tibetan": "སེམས་ཅན་ལས་དང་དབང་པོ་ནི། །\nརླུང་དང་ཤེས་པ་ཕྱི་སྣོད་དང་། །\nའབྱུང་བ་སྤྱི་དང་ཁྱབ་བྱེད་ཚུལ། །\nགསུམ་དང་དགུ་དང་ཉེར་གཅིག་གོ། །",
    "before": "Sentient beings",
    "after": "Karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent; capitalization and plural possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-022",
    "pair": "DTG-001879",
    "golden": [
      "U03903",
      "U03904"
    ],
    "tibetan": "སེམས་ཅན་ལས་ནི་རླུང་གི་ཡང༌། །\nའབྱུང་བའི་འཕེན་པ་དག་ཏུ་ཕུལ། །",
    "before": "Sentient beings",
    "after": "Karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent; capitalization and plural possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-023",
    "pair": "DTG-001884",
    "golden": [
      "U03915",
      "U03916",
      "U03917"
    ],
    "tibetan": "ཁྱབ་བྱེད་སེམས་ཅན་ཐམས་ཅད་ལ། །\nའབྱུང་བཞིའི་ལུས་ལས་མ་འདས་པས། །\nསོ་སོའི་ལས་ཀྱི་སྡེབས་སུའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-024",
    "pair": "DTG-001945",
    "golden": [
      "U04022",
      "U04023"
    ],
    "tibetan": "སྣང་སྟོང་འཇུག་པའི་ཡན་ལག་ཅན། །\nསངས་རྒྱས་སེམས་ཅན་དག་ཡུལ་ལོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-025",
    "pair": "DTG-001952",
    "golden": [
      "U04034",
      "U04035",
      "U04036"
    ],
    "tibetan": "ཆོས་སྐུ་སྟོང་པའི་རང་བཞིན་ལས། །\nཡེ་ཤེས་མཁྱེན་པ་རྫོགས་པའི་ཆ། །\nཐུགས་ཀྱིས་སེམས་ཅན་རྣམས་ལ་འཆར། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-026",
    "pair": "DTG-001997",
    "golden": [
      "U04113",
      "U04114",
      "U04115"
    ],
    "tibetan": "ཤེས་པས་བསྡུས་པའི་ཡེ་ཤེས་ནི། །\nསངས་རྒྱས་སེམས་ཅན་ཐམས་ཅད་ལ། །\nདབྱེར་མེད་རང་བཞིན་མེད་པར་ཁྱབ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-027",
    "pair": "DTG-001999",
    "golden": [
      "U04118",
      "U04119",
      "U04120",
      "U04121",
      "U04122",
      "U04123",
      "U04124",
      "U04125"
    ],
    "tibetan": "སེམས་ཅན་རིགས་དྲུག་སྣང་ཆ་ལ། །\nསོ་སོའི་རྒྱུད་ལ་གནས་པ་དེ། །\nལྷ་རྣམས་རང་གསལ་རྫོགས་པ་སྟེ། །\nལྷ་མིན་རྣམས་ལ་ཕྲ་ཞིང་འཁྱུག །\nམི་རྣམས་རང་གསལ་ཟླུམ་པོ་ཉིད། །\nབྱོལ་སོང་རྣམས་ལ་ནང་དུ་གསལ། །\nཡི་དྭགས་རྣམས་ལ་ཕྲ་བ་ལ། །\nདམྱལ་བར་རང་སྣང་རྫོགས་པའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-028",
    "pair": "DTG-002009",
    "golden": [
      "U04139",
      "U04140"
    ],
    "tibetan": "ཡེ་ནི་སེམས་ཅན་ཀུན་དོན་ལ། །\nཤེས་པས་ཁམས་གསུམ་དོང་ནས་འབྱིན། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can is the approved whole equivalent karmic being; this occurrence actually has sems can, and plural/possession are preserved.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-029",
    "pair": "DTG-001785",
    "golden": [
      "U03711",
      "U03712",
      "U03713"
    ],
    "tibetan": "དེ་ལས་འཁྲུལ་པ་རྒྱུ་དང་རྐྱེན། །\nཆ་དང་ཡན་ལག་ལས་ཉིད་དང༌། །\nམ་སྨིན་རྣམ་རྟོག་འཁོར་བའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "The full cyclic-existence entry applies to actual khor ba here; retain difficult become/exhaustion predicates and their negations rather than doctrinally smoothing them.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-030",
    "pair": "DTG-001795",
    "golden": [
      "U03729",
      "U03730",
      "U03731"
    ],
    "tibetan": "འཁོར་བ་ཞེས་པ་མཚུངས་པ་དང་། །\nཚོགས་པའི་ལས་ཏེ་སྡུད་དང་མཆེད། །\nརྫོགས་དང་བྱེ་བྲག་སྣ་ཚོགས་པའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "The full cyclic-existence entry applies to actual khor ba here; retain difficult become/exhaustion predicates and their negations rather than doctrinally smoothing them.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-031",
    "pair": "DTG-001808",
    "golden": [
      "U03760",
      "U03761",
      "U03762"
    ],
    "tibetan": "དམིགས་པའི་རྟེན་ནི་ཁ་དོག་ལས། །\nགཉིས་ཆ་ཕྲ་བའི་འགྱུ་རྟེན་གྱིས། །\nའཁོར་བ་ལས་ཀྱི་དམིགས་གྱུར་ཏོ། །",
    "before": "samsaric activity",
    "after": "the activity of cyclic existence",
    "rationale": "Preserve khor ba and las separately: the approved full cyclic-existence term plus the existing activity relationship, not an added karmic agent.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-032",
    "pair": "DTG-001849",
    "golden": [
      "U03850"
    ],
    "tibetan": "འདི་ཚེ་འཁོར་འདས་འདྲེས་པའོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "The complete P2 khor ’das compound requires both approved members; source conjunction, negation and referents are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-033",
    "pair": "DTG-001953",
    "golden": [
      "U04037",
      "U04038"
    ],
    "tibetan": "དེ་མེད་འཁོར་འདས་ལྟེ་ཆད་པས། །\n མཁྱེན་པས་རིག་ཅིང་གསལ་བའོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "The complete P2 khor ’das compound requires both approved members; source conjunction, negation and referents are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-034",
    "pair": "DTG-001961",
    "golden": [
      "U04052"
    ],
    "tibetan": "རང་ཆས་སྣང་སྟེ་འཁོར་འདས་སྦྱོར། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "The complete P2 khor ’das compound requires both approved members; source conjunction, negation and referents are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-035",
    "pair": "DTG-001973",
    "golden": [
      "U04069",
      "U04070",
      "U04071"
    ],
    "tibetan": "ཡེ་ཤེས་ཞེས་བྱ་གནས་པ་ལ། །\nདེ་ཡི་མཚན་ཉིད་རྟོགས་པ་ཡིས། །\nའཁོར་འདས་གཉིས་ལ་མི་གནས་པའོ། །",
    "before": "samsara or nirvana",
    "after": "cyclic existence or transcendence of sorrow",
    "rationale": "The source coordinated khor ’das gnyis occurs under negation; preserve both approved members and negative either/or scope.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-036",
    "pair": "DTG-001994",
    "golden": [
      "U04110"
    ],
    "tibetan": "ཤེས་པས་འཁོར་འདས་གཉིས་ལས་གྲོལ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "The complete P2 khor ’das compound requires both approved members; source conjunction, negation and referents are retained.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-037",
    "pair": "DTG-002038",
    "golden": [
      "U04204",
      "U04205"
    ],
    "tibetan": "དྲན་བསམ་འདུས་པའི་རང་བཞིན་ལས། །\nཆོས་ཀྱི་སྐུ་ཡང་འཁོར་བར་འགྱུར། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "The full cyclic-existence entry applies to actual khor ba here; retain difficult become/exhaustion predicates and their negations rather than doctrinally smoothing them.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-038",
    "pair": "DTG-002039",
    "golden": [
      "U04206",
      "U04207"
    ],
    "tibetan": "གང་ཚེ་འཁོར་བའི་མཐའ་ཟད་པས། །\nབྱས་པ་མེད་པར་རང་སར་གྲོལ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "The full cyclic-existence entry applies to actual khor ba here; retain difficult become/exhaustion predicates and their negations rather than doctrinally smoothing them.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-039",
    "pair": "DTG-001736",
    "golden": [
      "U03623",
      "U03624",
      "U03625",
      "U03626"
    ],
    "tibetan": " དེ་ནས་ལྷ་དབང་དགའ་བྱེད་ཀྱིས། །\nཡེ་ཤེས་བཀོད་པ་ཞེས་བྱ་བའི། །\nསངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་ཞུས། །\nཆོས་ཉིད་གནས་པ་ཇི་ལྟར་ལགས། །",
    "before": "Delight-Maker",
    "after": "Joy-Maker",
    "rationale": "Recurring dga byed, with the same lord-of-gods designation, continues the named interlocutor already consistently treated as Joy-Maker at DTG-001028 and its replies. This is within-work identity consistency, not approval of a new shared default.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-040",
    "pair": "DTG-001752",
    "golden": [
      "U03643"
    ],
    "tibetan": "བྱ་བ་ཇི་ལྟར་འགྲུབ་པ་ལགས། །",
    "before": "activity",
    "after": "doing",
    "rationale": "The question actually says bya ba, not a complete lexicalized primordial-knowing name; retain the approved doing component. The later reply DTG-001981/001985 also explicitly explains doing.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-041",
    "pair": "DTG-001759",
    "golden": [
      "U03650"
    ],
    "tibetan": "སྟོན་པ་ཐུགས་རྗེ་ཆེན་པོས་གསུངས། །",
    "before": "Teacher of great compassionate responsiveness, speak.",
    "after": "Teacher, speak with great compassionate responsiveness.",
    "rationale": "thugs rje chen pos is instrumental, not a possessive of the teacher. Preserve the inherited request and speaker boundary while restoring the compassionate-responsiveness manner of speaking.",
    "severity": "moderate syntax",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B12-042",
    "pair": "DTG-001760",
    "golden": [
      "U03651",
      "U03652",
      "U03653",
      "U03654",
      "U03655",
      "U03656"
    ],
    "tibetan": "ནམ་མཁའ་མི་འབྱེད་བར་སྣང་ནས། །\nསུས་ཀྱང་བྱས་པ་མེད་པའི་ཚིག །\nརང་བཞིན་རྟོག་པ་གང་མེད་པར། །\nབརྗོད་མེད་བསམ་དག་སྒྲ་ལས་ཀྱང༌། །\nཚིག་གི་རྒྱལ་པོ་འདི་དག་ནི། །\nསྟོན་པས་གསུངས་པའི་ཚུལ་དུ་ཤར། །",
    "before": "From the intervening space",
    "after": "From the open sky",
    "rationale": "P2 bar snang: this speech-emergence setting does not emphasize an interval between two objects. Keep open sky distinct from nam mkha, space, in the same line.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-043",
    "pair": "DTG-001760",
    "golden": [
      "U03651",
      "U03652",
      "U03653",
      "U03654",
      "U03655",
      "U03656"
    ],
    "tibetan": "ནམ་མཁའ་མི་འབྱེད་བར་སྣང་ནས། །\nསུས་ཀྱང་བྱས་པ་མེད་པའི་ཚིག །\nརང་བཞིན་རྟོག་པ་གང་མེད་པར། །\nབརྗོད་མེད་བསམ་དག་སྒྲ་ལས་ཀྱང༌། །\nཚིག་གི་རྒྱལ་པོ་འདི་དག་ནི། །\nསྟོན་པས་གསུངས་པའི་ཚུལ་དུ་ཤར། །",
    "before": "intrinsically without any conceptual thought,",
    "after": "in intrinsic nature, without any conceptual thought,",
    "rationale": "The complete rang bzhin row requires intrinsic nature even in an adverbial construction. Retain the circumstantial absence of conceptual thought and do not promote by its intrinsic nature to a new universal rule. The following speech-emergence syntax stays provisional.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B12-044",
    "pair": "DTG-001771",
    "golden": [
      "U03683"
    ],
    "tibetan": "རྟོག་པ་འཛིན་པ་སྟོང་ཚིགས་ལའོ། །",
    "before": "Conceptual thought and holding are",
    "after": "Holding conceptual thought is",
    "rationale": "rtog pa ’dzin pa is locally the holding of conceptual thought; the English adds a coordination without dang and makes thought and holding two separate subjects. Preserve the thousand-junctures location without guessing units or an agent.",
    "severity": "moderate syntax",
    "confidence": "moderate"
  },
  {
    "finding": "PD-B12-045",
    "pair": "DTG-001788",
    "golden": [
      "A2000-C03-S01",
      "U03716"
    ],
    "tibetan": "ལྷན་ཅིག་སྐྱེས་པས་རྟོག་པ་གཉིས།\nཀུན་ཏུ་བརྟགས་པས་ཡུལ་དུ་གྱུར།\nརྐྱེན་ནི་རྣམ་པ་བཞི་དག་གིས།\nའདུས་ཤིང་བཟུང་བས་འཁྲུལ་ཞེས་བྱ། །",
    "before": "Through gathering and holding",
    "after": "through gathering and holding",
    "rationale": "The restored preceding clause ends with an em dash; this is its continuing predicate, not a new sentence. Keep the source and restored ignorance construction unchanged.",
    "severity": "minor presentation",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-046",
    "pair": "DTG-001799",
    "golden": [
      "U03740",
      "U03741",
      "U03742"
    ],
    "tibetan": "རྐྱེན་ནི་ཡུལ་དང་གཟུང་ཆ་ལས། །\nམཐའ་དང་མཐའ་ཡི་བྱེད་ པ་དང་། །\nགཅིག་མ་ཤེས་པ་དམིགས་རྟེན་ནོ། །",
    "before": "support of focus",
    "after": "support of the object of focus",
    "rationale": "Read the abbreviated dmigs rten in the announced condition list with expanded dmigs pa’i rten in its explanation. The latter explicitly supplies the object-of-focus noun, further specified by colors; restore that object without resolving the still-provisional causal grouping.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B12-047",
    "pair": "DTG-001808",
    "golden": [
      "U03760",
      "U03761",
      "U03762"
    ],
    "tibetan": "དམིགས་པའི་རྟེན་ནི་ཁ་དོག་ལས། །\nགཉིས་ཆ་ཕྲ་བའི་འགྱུ་རྟེན་གྱིས། །\nའཁོར་བ་ལས་ཀྱི་དམིགས་གྱུར་ཏོ། །",
    "before": "support of focus",
    "after": "support of the object of focus",
    "rationale": "Read the abbreviated dmigs rten in the announced condition list with expanded dmigs pa’i rten in its explanation. The latter explicitly supplies the object-of-focus noun, further specified by colors; restore that object without resolving the still-provisional causal grouping.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B12-048",
    "pair": "DTG-001822",
    "golden": [
      "U03791",
      "U03792"
    ],
    "tibetan": "གཟུགས་ཅན་རིག་བཅས་བེམ་པོ་སྟེ། །\nསེམས་སྡུད་པ་དང་བཀོད་པའོ། །",
    "before": "aware [or] insentient",
    "after": "aware [or] is matter",
    "rationale": "Actual golden rig bcas bem po: P2 fixes bem po as matter. Repeat the copula only to accommodate the mass noun. The bracketed or remains a provisional coordination, not a certified opposition between aware beings and immaterial bodies. N-T90’s old differently worded source form is historical.",
    "severity": "minor terminology",
    "confidence": "high for label; coordination unresolved"
  },
  {
    "finding": "PD-B12-049",
    "pair": "DTG-001904",
    "golden": [
      "U03952",
      "U03953"
    ],
    "tibetan": "གནས་གཞན་རྩ་བ་གཞི་དག་ལས། །\nཚིག་ལ་རྟོག་པས་གནས་བརྒྱ་གཉིས། །",
    "before": "examining words",
    "after": "through conceptual thought about words",
    "rationale": "U03953 reads rtog pas, not brtags pas. Preserve the canonical conceptual-thought noun and its instrumental relation to words; do not silently emend the source to examination. The 102 count and neighboring variants are unchanged.",
    "severity": "moderate terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-050",
    "pair": "DTG-001982",
    "golden": [
      "U04088",
      "U04089"
    ],
    "tibetan": "རང་གྲོལ་རྫོགས་པའི་གཞི་སྣང་ལས། །\nཆ་ཕྲ་རྡུལ་བྲལ་དྲི་མེད་ཐོབ། །",
    "before": "ground-appearance",
    "after": "Ground-appearance",
    "rationale": "P1 requires capital G and the existing hyphenation for the complete gzhi snang expression; no other wording is changed.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-051",
    "pair": "DTG-002014",
    "golden": [
      "U04147",
      "U04148"
    ],
    "tibetan": "དངོས་པོའི་གནས་ལུགས་མཁྱེན་པ་ལས། །\nརང་དོན་རྟོགས་པས་འཁྲུལ་རྒྱུན་ཟད། །",
    "before": "natural state of things",
    "after": "natural state of entities",
    "rationale": "The actual source is dngos po’i gnas lugs. P2 requires entity, with no material-only scope or chapter-local thing substitution.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-052",
    "pair": "DTG-002041",
    "golden": [
      "U04209"
    ],
    "tibetan": "མེད་ཕྱིར་ཆོས་ཉིད་དངོས་པོ་མིན། །",
    "before": "not a thing",
    "after": "not an entity",
    "rationale": "Actual dngos po under min: preserve the complete entity noun and the explicit negation; do not convert it into a claim solely about physical matter.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-053",
    "pair": "DTG-002045",
    "golden": [
      "U04215",
      "U04216"
    ],
    "tibetan": "འགྲོ་ཞིང་འབྱུང་བ་རྙེད་པ་ཡིས། །\nདངོས་པོ་དག་པས་གཟུགས་ཟད་པའོ། །",
    "before": "things being pure",
    "after": "entities being pure",
    "rationale": "Actual dngos po, plural in the inherited construction; P2 entity applies. The difficult finding-going-and-arising clause remains linked and unaltered.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-054",
    "pair": "DTG-002047",
    "golden": [
      "U04218",
      "U04219",
      "U04220"
    ],
    "tibetan": "ས་ཆུ་མེ་རླུང་ནམ་མཁའ་ལས། །\nཡེ་ཤེས་སྣང་བ་ངོ་མཚར་བས། །\nབཅོམ་ལྡན་མགོན་པོ་རིག་མེད་པའོ། །",
    "before": "the blessed protector is",
    "after": "the Blessed One, the protector, is",
    "rationale": "The attested short honorific bcom ldan retains Blessed One under P2; mgon po remains a separate meaningful protector addition. Retain the difficult without-awareness predicate.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-055",
    "pair": "DTG-002071",
    "golden": [
      "U04261",
      "U04262"
    ],
    "tibetan": "གཟུགས་ཀྱིས་བསླབ་པ་གཉིས་དག་ནི། །\nདམིགས་པའི་རྟེན་དང་དམིགས་མེད་དོ། །",
    "before": "a support for focus and freedom from focus",
    "after": "a support for an object of focus and absence of an object of focus",
    "rationale": "dmigs pa’i rten and dmigs med explicitly distinguish a support involving an object of focus from its absence in the two form trainings. Restore the approved object component without adding a technique.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B12-056",
    "pair": "DTG-002074",
    "golden": [
      "U04267",
      "U04268",
      "U04269",
      "U04270",
      "U04271",
      "U04272"
    ],
    "tibetan": "སྒྲ་ནི་དམིགས་པའི་རྟེན་དག་པས། །\nཔི་ཝཾ་རྫ་རྔ་བུམ་ལྡིར་དང་། །\nདྲ་བ་རྒྱུད་མང་མདོ་གསུམ་པ། །\nཧར་དང་གླིང་བུ་ཆ་ལང་དང༌། །\nཕེག་རྡོབ་ཅང་ཏེའུ་དྲིལ་བུ་སོགས། །\nསོ་སོའི་སྒྲ་ལ་རླུང་ཡང་སྦྱར། །",
    "before": "support for focus",
    "after": "support for an object of focus",
    "rationale": "The sensory instructions specify the object/support relation with expanded dmigs pa’i rten or its local short dmigs rten. Retain the object component, not a bare mental act of focus; uncertain instrument/physical operations remain unchanged.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B12-057",
    "pair": "DTG-002078",
    "golden": [
      "U04281",
      "U04282"
    ],
    "tibetan": "རེག་ནི་ཡིད་མཐུན་དམིགས་རྟེན་ལ། །\nསོ་སོའི་རིག་པ་ཉམས་མྱོང་སྦྱར། །",
    "before": "support for focus",
    "after": "support for an object of focus",
    "rationale": "The sensory instructions specify the object/support relation with expanded dmigs pa’i rten or its local short dmigs rten. Retain the object component, not a bare mental act of focus; uncertain instrument/physical operations remain unchanged.",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B12-058",
    "pair": "DTG-002073",
    "golden": [
      "U04265",
      "U04266"
    ],
    "tibetan": "དབྱིབས་ལ་གོམས་ཏེ་ཁ་དོག་ལ། །\nགོམས་པར་བྱས་པས་འཁྲུལ་སྣང་འགགས། །",
    "before": "Become accustomed to",
    "after": "Become familiar with",
    "rationale": "The approved goms row explicitly permits become familiar with. The following familiarity already realizes the allowed state form and is deliberately not changed.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-059",
    "pair": "DTG-002080",
    "golden": [
      "U04285"
    ],
    "tibetan": "ཆོས་ནི་བླ་མའི་ལུང་དང་བསྟུན། །",
    "before": "authoritative transmission",
    "after": "transmission",
    "rationale": "The source says bla ma’i lung. P2 supplies transmission; no separate qualifier supports authoritative. Preserve the lama’s possession and the instruction to accord.",
    "severity": "minor unsupported addition",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-060",
    "pair": "DTG-002081",
    "golden": [
      "U04286",
      "U04287",
      "U04288"
    ],
    "tibetan": "གལ་ཏེ་བསྒོམ་པ་བཟང་པོ་རྟོགས། །\nའདི་ལྟར་བརྩམས་པས་ལམ་དུ་སློང༌། །\nཁམས་གསུམ་འཁྲུལ་འཁོར་རྒྱུན་ཆད་དོ། །",
    "before": "When excellent cultivation is realized",
    "after": "If excellent cultivation is realized",
    "rationale": "gal te introduces a condition, not a guaranteed future event. Restore if while preserving cultivation, realization and the ensuing path/result clauses.",
    "severity": "moderate condition",
    "confidence": "high"
  },
  {
    "finding": "PD-B12-061",
    "pair": "DTG-002073",
    "golden": [
      "U04265",
      "U04266"
    ],
    "tibetan": "དབྱིབས་ལ་གོམས་ཏེ་ཁ་དོག་ལ། །\nགོམས་པར་བྱས་པས་འཁྲུལ་སྣང་འགགས། །",
    "before": "and then to colors",
    "after": "and then with colors",
    "rationale": "The repair self-check caught the preposition governed by become familiar with. Preserve the same second object, colors, with the required with rather than the old accustomed-to preposition. This repairs this reviewer’s change, not an independently found original error.",
    "severity": "minor repair self-check",
    "confidence": "high"
  }
]
```

<a id="phase-d-notes-12"></a>
### Active note/usage dispositions

The following dated dispositions are appended to the existing usage record and linked from the existing legacy index; original approvals/proposals and source notes remain historical. A retained provisional construction is not an approved new shared equivalent.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-159",
    "pairs": [
      "DTG-001736",
      "DTG-001747",
      "DTG-001759",
      "DTG-001760",
      "DTG-002088"
    ],
    "ids": [
      "U03623",
      "U03624",
      "U03625",
      "U03626",
      "U03637",
      "U03638",
      "U03650",
      "U03651",
      "U03652",
      "U03653",
      "U03654",
      "U03655",
      "U03656",
      "U04304",
      "U04305"
    ],
    "realization": "Then the lord of the gods, Joy-Maker,\nconcerning what is called ‘Array of Primordial Knowing,’\nquestioned the buddha, the Blessed One: [N-159](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-159)\n‘How does the nature of phenomena abide?; Essence as primordial purity and primordial knowing,\nand intrinsic nature as spontaneous presence—why are these so?; Teacher, speak with great compassionate responsiveness.’ [N-159](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-159); From the open sky, without dividing space,\nphrases made by no one,\nin intrinsic nature, without any conceptual thought,\nfrom words beyond expression, with reflection pure—[N-159](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-159)\nthese kings of phrases\narose as if spoken by the teacher.; Thus, from the Great All-Penetrating Word, Root of All Phenomena:\nthe third chapter, the Array of Primordial Knowing, in which the root of appearance definitely emerges.",
    "status": "Partly corrected; attachment remains provisional",
    "reason": "Joy-Maker and the explicit instrumental/technical wording are corrected. Reading the opening with the third-chapter colophon confirms that Array of Primordial Knowing is a chapter designation, but does not exclude the Buddha-name attachment in ye shes bkod pa zhes bya ba’i sangs rgyas. The ngo bo ka dag ye shes and brjod med bsam dag sgra constructions remain unresolved; a syntactic parallel or authorized commentary would settle them, not the colophon alone.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-T87",
    "pairs": [
      "DTG-001749",
      "DTG-001751",
      "DTG-001755",
      "DTG-001756",
      "DTG-001975",
      "DTG-001978"
    ],
    "ids": [
      "U03640",
      "U03642",
      "U03646",
      "U03647",
      "U04073",
      "U04074",
      "U04075",
      "U04080",
      "U04081"
    ],
    "realization": "Why is [primordial knowing] like a mirror?; What is the extent of discriminating [primordial knowing]?; What pervades the multiplicity?; What is the enlightened intent of knowing how things are?; Discriminating [primordial knowing]: the types of faculty,\nwhatever appears to them, and the phenomena of that appearance\nare each clear in sequence. [N-177](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-177); What is called ‘realization’ is seeing the characteristics,\ntogether with the increase of self-appearance.",
    "status": "Retained local short-form/name proposal",
    "reason": "The complete question/reply comparison preserves the mirror simile and discriminating [primordial knowing] as explicitly provisional. Golden so sor rtogs pa has final s and its later word explanation explicitly uses realization; it is not silently identified with the different established so sor rtog pa’i ye shes entry. Neither global rtog/rtogs interchange nor a new name entry is approved.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-160",
    "pairs": [
      "DTG-001765",
      "DTG-001766",
      "DTG-001767",
      "DTG-001770",
      "DTG-001771",
      "DTG-001773",
      "DTG-001775"
    ],
    "ids": [
      "U03668",
      "U03669",
      "U03670",
      "U03671",
      "U03672",
      "U03673",
      "U03678",
      "U03679",
      "U03680",
      "U03681",
      "U03682",
      "U03683",
      "U03686",
      "U03687",
      "U03688",
      "U03690",
      "U03691",
      "U03692"
    ],
    "realization": "It abides on the ninth and eighth of the waning moon,\nand the fourteenth and [fifteenth] of the waxing moon. [N-160](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-160); For days, half of twelve parts; [N-160](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-160)\nalso, among twelve times of the sun,\nit abides in four aspects of a part. [N-160](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-160); At this time, train in the nature of phenomena. [N-160](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-160); Abiding in the definite measure of shifting:\nthrough the winds of great movement,\nin the measure of movement at each respective stage,\nat each five hundred,\nthere is a shift in the abiding of the nature of phenomena.; Holding conceptual thought is at the thousand-junctures. [N-160](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-160); The method of making the nature of ordinary mind abide there:\nreckoning from the time of five hundred,\nstrive at the point of applying the respective virtues.; Grasping [this] from the respective intervals of wind,\nthe particulars of lifespan and karma, too,\nare to be known through changes in wind. [N-160](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-160)",
    "status": "Partly corrected; numerical and construction limits retained",
    "reason": "Holding conceptual thought restores the local object relation. Fourteenth and [fifteenth], half of twelve parts, four aspects, five hundred and thousand-junctures retain their stated uncertainty; no duration, rate or calendar is inferred. G-U03673 already separates the apply variant from main train. Nature of ordinary mind for sems nyid and the wind/lifespan constructions remain linked provisional uses, not a new default.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-162",
    "pairs": [
      "DTG-001787",
      "DTG-001788",
      "DTG-001789",
      "DTG-001790",
      "DTG-001796"
    ],
    "ids": [
      "U03715",
      "A2000-C03-S01",
      "U03716",
      "U03717",
      "U03718",
      "U03719",
      "U03732",
      "U03733",
      "U03734",
      "U03735"
    ],
    "realization": "Through their single identity, it makes the root of delusion.; Through co-emergent [ignorance], there are two conceptual thoughts;\nthrough thorough imputation, [it] becomes an object;\nas for conditions, through four aspects—\nthrough gathering and holding, it is called delusion.; As for portions, through formations and so forth,\nsubtract twelve from the portion of delusion's objects. [N-162](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-162); Through maturation, there are years and activities.; Thus, apart from merely the name ‘delusion,’\nthrough the signs of conceptualizing and holding as agents,\nand the agency of assembling and condensing,\nit is imputed through distinctions of names. [N-162](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-162)",
    "status": "Retained bounded syntax/source questions",
    "reason": "The restored ignorance verses are present, not an omission. bdag nyid gcig pas at DTG-001787 may identify a named single-identity ignorance or express the inherited instrument; its pronoun/subject remains provisional pending a construction-level parallel. phri remains subtract rather than an emended phye. The maturation/year, twofold object, and agency-of-conceptualizing clauses remain exact linked queries; dormant tendencies are not collapsed into habitual tendencies.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-163",
    "pairs": [
      "DTG-001798",
      "DTG-001799",
      "DTG-001803"
    ],
    "ids": [
      "U03737",
      "U03738",
      "U03739",
      "U03740",
      "U03741",
      "U03742",
      "U03749",
      "U03750"
    ],
    "realization": "The cause of delusion is ignorance:\nthe Ground, knowing, contamination,\nand the ways apprehended object and faculties circle. [N-163](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-163); Conditions are from the object and the apprehended portion:\nlimits, the agents of limits,\nnot knowing one, and the support of the object of focus.; Even where there is no apprehended object,\n[holding it as] true binds [one] tightly. [N-163](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-163)",
    "status": "Partly corrected; grouping retained provisional",
    "reason": "The object-of-focus component is restored by comparison with DTG-001808. The announced nine points, limit agents and contamination grouping remain unresolved, as do the bracketed holding-as-true supplies in the no-apprehended-object clause. They are not converted into additional agents or a forced count.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-164",
    "pairs": [
      "DTG-001805",
      "DTG-001807",
      "DTG-001808"
    ],
    "ids": [
      "U03753",
      "U03754",
      "U03757",
      "U03758",
      "U03759",
      "U03760",
      "U03761",
      "U03762"
    ],
    "realization": "Through knowing the manner of circling as one,\ndifferentiating conceptualizations unite in pairs.; Not knowing one: from primordial purity,\nbecause the nature of phenomena's own identity is not known,\nthere is appropriation corresponding to the cause.; The support of the object of focus, from colors,\nthrough the moving support of two subtle portions,\nbecomes the object of focus of the activity of cyclic existence. [N-164](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-164)",
    "status": "Partly corrected; causal construction provisional",
    "reason": "Keep appropriation for nyer len provisional rather than automatically equating it with len pa. Restore the expanded object-of-focus component without identifying the two subtle portions or changing the causal correspondence; the source and the approved row do not supply those identifications.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-165",
    "pairs": [
      "DTG-001810",
      "DTG-001817",
      "DTG-001822"
    ],
    "ids": [
      "U03764",
      "U03765",
      "U03766",
      "U03767",
      "U03779",
      "U03780",
      "U03791",
      "U03792"
    ],
    "realization": "The particulars of realizing characteristics:\nexistence, nonexistence, appearance,\nclarity, emptiness, the coarse, the apprehending subject,\nconsciousness, and what possesses form. [N-165](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-165); Emptiness is not birth;\nit reveals radiance and absence of limits or center.; What possesses form is aware [or] is matter,\ngathering and arranging ordinary mind. [N-165](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-165)",
    "status": "Matter corrected; major negation-scope question retained",
    "reason": "DTG-001817 reads གདངས་དང་མཐའ་དབུས་མེད་པར་སྟོན།: current English reveals radiance and absence of limits or center. An alternative scopes med over radiance as well as limits/center: reveals their absence. This potentially consequential negation question is not settled by the glossary or adjacent nonarising line; a syntactic parallel/authorized explanation is needed. Main English remains linked provisional, not cleared. The eight-point annotation and all nine explained items are preserved. In DTG-001822 matter is approved, but [or] and the gathering/arranging predicate remain unresolved.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-T90",
    "pairs": [
      "DTG-001807",
      "DTG-001822",
      "DTG-001868",
      "DTG-002024"
    ],
    "ids": [
      "U03757",
      "U03758",
      "U03759",
      "U03791",
      "U03792",
      "U03884",
      "U03885",
      "U03886",
      "U03887",
      "U03888",
      "U04168",
      "U04169",
      "U04170"
    ],
    "realization": "Not knowing one: from primordial purity,\nbecause the nature of phenomena's own identity is not known,\nthere is appropriation corresponding to the cause.; What possesses form is aware [or] is matter,\ngathering and arranging ordinary mind. [N-165](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-165); In the authentic nature of phenomena, free from conceptual thought,\nhaving thoroughly distinguished the characteristics of names,\nthrough thorough examination of outer and inner,\nbecause characteristics are not found through names,\none wishes to complete one's own rite. [N-168](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-168); Distinguishing the gathered special features,\nfrom the self-radiance of the nature of phenomena, free from conceptual thought,\nthere arises an appearance of primordial knowing without an object of focus.",
    "status": "Split disposition; matter adopted, other constructions provisional",
    "reason": "Current golden DTG-001822 says rig bcas bem po, not the historical note’s rig cing bem par bcas. Matter now realizes P2; the non-knowing side can be explained in this note without replacing it by insentient matter or denying material bodies to karmic beings. The bracketed coordination remains provisional. nyer len and rtog bral remain separate construction questions; free from conceptual thought is not a new default for different negative-family expressions.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-166",
    "pairs": [
      "DTG-001826",
      "DTG-001830",
      "DTG-001831",
      "DTG-001832",
      "DTG-001834",
      "DTG-001835"
    ],
    "ids": [
      "U03802",
      "U03803",
      "U03812",
      "U03813",
      "U03814",
      "U03815",
      "U03816",
      "U03817",
      "U03818",
      "U03819",
      "U03820",
      "U03823",
      "U03824",
      "U03825",
      "U03826"
    ],
    "realization": "The activities of agency, from four,\nwhen examined, become twelve. [N-166](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-166); Measures concern each of the six classes:\nbeginning, middle, and end,\ndistinguished by their respective merit and karma.; Sounds are long and short,\nstrong and weak, pressing and releasing,\nsubtle, seng [unresolved], and pointed. [N-166](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-166); Entities, through earth, water, fire, and wind,\nare examined through knowing itself, merit,\nascendancy, and bodily portions.; The vessels of abiding are pure\nor impure, distinguished by their inhabitants.; Therefore, through the elements' own key points,\nthe bodies of karmic beings differ. [N-166](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-166)",
    "status": "Approved labels corrected; obsolete number criticism rejected",
    "reason": "G-U03802/G-U03803 already keep main four/twelve separate from smaller two/sixty. Those old co-main number criticisms are not current defects. seng remains explicitly unresolved. bsod nams las at DTG-001830 retains the merit/karma coordination question rather than being automatically labeled meritorious karma. Entities remain distinct from matter; bcud is inhabitants in the vessel/inhabitant relation. Acoustic sgra is sound in the long/short/strong/weak list.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-167",
    "pairs": [
      "DTG-001843",
      "DTG-001844",
      "DTG-001846",
      "DTG-001850",
      "DTG-001855"
    ],
    "ids": [
      "U03838",
      "U03839",
      "U03840",
      "U03841",
      "U03842",
      "U03844",
      "U03845",
      "U03851",
      "U03857",
      "U03858"
    ],
    "realization": "When fine dust has been cleared by rain,\nthe skilled person presses the key point of direct perception,\nand takes the inner lamps as the path.; Own identity: awareness as vajra chains,\nseparating going and coming, in space. [N-167](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-167); Distinguish through the ninth wind;\ndistinguish entry into abiding through methods.; This, too, is the key point of completion in the Ground. [N-167](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-167); Self-appearance is complete as pure from the outset;\nknowing, holding, and conceptual thought are all exhausted. [N-167](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-167)",
    "status": "Key-point labels corrected; source repair already effective",
    "reason": "G-U03851 already selects joined rdzogs and English completion: the old rdzo gas issue is not a current defect. Keep the visionary vajra chains, source two/ninth-wind counts, and pure-from-outset wording. Their spatial/operational attachments remain provisional; no optical or breath procedure is supplied.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-168",
    "pairs": [
      "DTG-001857",
      "DTG-001863",
      "DTG-001868",
      "DTG-001871",
      "DTG-001872",
      "DTG-001876"
    ],
    "ids": [
      "U03860",
      "U03861",
      "U03862",
      "U03863",
      "U03872",
      "U03873",
      "U03874",
      "U03884",
      "U03885",
      "U03886",
      "U03887",
      "U03888",
      "U03891",
      "U03892",
      "U03893",
      "U03897"
    ],
    "realization": "What makes the characteristics of names:\ncause, conditions, imputation,\nlimits, the first, transformation of the last,\nnot finding through examination, and the basis of convention. [N-168](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-168); In particular, the key point of what is transformed by a name:\njoining [it] with each respective occasion,\neven the Blessed One will be destroyed. [N-168](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-168); In the authentic nature of phenomena, free from conceptual thought,\nhaving thoroughly distinguished the characteristics of names,\nthrough thorough examination of outer and inner,\nbecause characteristics are not found through names,\none wishes to complete one's own rite. [N-168](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-168); Through examining and analyzing body and ordinary mind, the two,\nthe basis of convention, too, is empty.; The Ground is neither one nor two.; Therefore, the nature of phenomena is empty. [N-168](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-168)",
    "status": "Key points corrected; meaningful differences preserved",
    "reason": "The name-transformation passage actually includes the destruction predicate; do not soften it or invent ritual targets/procedures. Basis of convention is a source-specific support construction, not an automatic technical Ground replacement. Retain all nonfinding/nonabiding negatives and the rtog bral proposal; the eightfold grouping/first-last operations need contextual evidence.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-T88",
    "pairs": [
      "DTG-001857",
      "DTG-001871",
      "DTG-001904"
    ],
    "ids": [
      "U03860",
      "U03861",
      "U03862",
      "U03863",
      "U03891",
      "U03892",
      "U03952",
      "U03953"
    ],
    "realization": "What makes the characteristics of names:\ncause, conditions, imputation,\nlimits, the first, transformation of the last,\nnot finding through examination, and the basis of convention. [N-168](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-168); Through examining and analyzing body and ordinary mind, the two,\nthe basis of convention, too, is empty.; From the root foundation of other places— [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170)\nthrough conceptual thought about words: one hundred and two places. [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170)",
    "status": "Retained construction-level support uses",
    "reason": "Basis of convention and root foundation remain bounded support constructions, distinct from the explicitly technical Ground nearby. The small-print brtse ba bzhi question is in G-U03952, not part of the selected main foundation expression. No global gzhi exception is activated.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-169",
    "pairs": [
      "DTG-001878",
      "DTG-001884",
      "DTG-001887",
      "DTG-001888",
      "DTG-001890"
    ],
    "ids": [
      "U03899",
      "U03900",
      "U03901",
      "U03902",
      "U03915",
      "U03916",
      "U03917",
      "U03922",
      "U03923",
      "U03924",
      "U03927",
      "U03928"
    ],
    "realization": "Karmic beings' karma and faculties:\nwind, knowing, the outer vessel,\nthe elements in general, and the manner of pervading;\nthree, nine, and twenty-one. [N-169](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-169); Pervading: all karmic beings,\nbecause they do not go beyond a body of four elements,\nare in their respective combinations of karma.; Through these, the three vehicles are free from perception. [N-169](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-169); Thoroughly dividing each into three,\nthere are nine: the faculties' key point of the nine vehicles.; Placing three in the Ground, through twenty-one,\nthe twenty-one appearances are complete. [N-169](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-169)",
    "status": "Karmic-being/key-point corrections; written bral retained",
    "reason": "The source at U03922 actually reads ’du shes bral: keep free from perception queried, not silently emended to differentiation. Preserve the explicit three-to-nine, two sets of nine and three/21 sequence without inventing vehicle members or a clinical model; numerical Ground scope remains provisional.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-170",
    "pairs": [
      "DTG-001892",
      "DTG-001899",
      "DTG-001900",
      "DTG-001904",
      "DTG-001905",
      "DTG-001906"
    ],
    "ids": [
      "U03930",
      "U03931",
      "U03932",
      "U03933",
      "U03945",
      "U03946",
      "U03952",
      "U03953",
      "U03954",
      "U03955"
    ],
    "realization": "The entry of words is like this:\nBrahmā, the All-Pervader, and the Hundred-Giver;\nthe Sky-Soarer, the Powerful Lord, and the Fierce One;\ntheir respective sounds and the voices of gods.; For the Fierce One, entry is in three and two. [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170); The activity of arranging signs: seven and four. [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170); From the root foundation of other places— [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170)\nthrough conceptual thought about words: one hundred and two places. [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170); Extending from that: four hundred and four. [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170); The calculation of definite particulars becomes ten. [N-170](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-170)",
    "status": "rtog pa corrected; numerical layers preserved",
    "reason": "Conceptual thought about words restores actual rtog pas, not an assumed brtags pas. Preserve main 102/404 and the separate alternatives. G-U03946 already refuses to certify brgya bzhi as four hundred; old N-170 wording is historical. Deity designations, verse/place/half counts and the unresolved phonetic key remain local; no reconstructed mantra system is supplied.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-171",
    "pairs": [
      "DTG-001910",
      "DTG-001911",
      "DTG-001916",
      "DTG-001917",
      "DTG-001919",
      "DTG-001920"
    ],
    "ids": [
      "U03960",
      "U03961",
      "U03962",
      "U03963",
      "U03964",
      "U03965",
      "U03974",
      "U03975",
      "U03976",
      "U03979",
      "U03980",
      "U03981",
      "U03982"
    ],
    "realization": "What are called conceptual mind and knowing:\nordinary mind, mental faculty, movement,\nproliferation, agitation, rigidity,\nobject, apprehending subject, and clinging.; Ordinary mind: the pure and impure\nthree realms, too, enter buddhahood. [N-171](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-171); Rigidity, from three afflictions,\nchanges into what is called conceptual mind and is cut by knowing.; From the two gathering, three [kinds of] knowing arise. [N-171](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-171); The apprehending subject: through eyes and so forth,\nconceptual mind and knowing are actual in each respective [object].; Clinging: conceptual mind has four measures of realization;\nthrough the measures of knowing, these become eight.",
    "status": "Retained distinct knowing categories and bounded constructions",
    "reason": "The nine named categories and the three kinds of knowing versus separate three-realms variant are intact. rengs rigidity remains an unapproved local proposal. The actual-predicate use of dngos at U03980 remains provisional; P2 does not justify forcing a nominal entity into every occurrence. Entry into buddhahood, the four/eight measures and its subject remain linked questions.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-T89",
    "pairs": [
      "DTG-001910",
      "DTG-001916"
    ],
    "ids": [
      "U03960",
      "U03961",
      "U03962",
      "U03963",
      "U03974",
      "U03975"
    ],
    "realization": "What are called conceptual mind and knowing:\nordinary mind, mental faculty, movement,\nproliferation, agitation, rigidity,\nobject, apprehending subject, and clinging.; Rigidity, from three afflictions,\nchanges into what is called conceptual mind and is cut by knowing.",
    "status": "Retained new-label proposal",
    "reason": "Rigidity for rengs pa remains a proposed label tied to these two occurrences. It is not merged with agitation, dullness or stability and is not a diagnosis. Shared reconciliation, not this local pass, must approve a new entry.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-172",
    "pairs": [
      "DTG-001926",
      "DTG-001927",
      "DTG-001928",
      "DTG-001929"
    ],
    "ids": [
      "U03989",
      "U03990",
      "U03991",
      "U03992",
      "U03993",
      "U03994",
      "U03995",
      "U03996"
    ],
    "realization": "The object's key point is in the faculties; the faculties' key point is ordinary mind.; Ordinary mind's key point is in the eyes; the eyes' key point is the channels.; Therefore, through bodily posture,\nthe connection of habitual tendencies with the body is cut,\nand the buddhas' enlightened intent is complete.; The channels, through the wheel of dependent connections,\nare the place of seeking, holding, and increasing—\nthe yogin's branches. [N-172](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-172)",
    "status": "Key-point labels corrected; relational chain preserved",
    "reason": "Read the whole object/faculty/ordinary-mind/eye/channel chain. Both repeated key points in each affected pair remain; habitual tendencies keep their approved wording. The final wheel/branches relation stays provisional and is not expanded into bodily manipulation instructions.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-174",
    "pairs": [
      "DTG-001931",
      "DTG-001935",
      "DTG-001936",
      "DTG-001939",
      "DTG-001940"
    ],
    "ids": [
      "U03998",
      "U03999",
      "U04004",
      "U04005",
      "U04006",
      "U04011",
      "U04012",
      "U04013"
    ],
    "realization": "From essence as primordial purity and primordial knowing,\nthere is no possible name ‘ignorance.’; Without phrases, nothing is established through expression. [N-174](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-174); Pure self-awareness does not abide at an extreme;\nthe limits of the names ‘apprehended object and apprehending subject’ are exhausted.; Absent from the beginning, pure through purity,\nwith deluded conceptual thought ceased, it does not enact anything.; Since it has not arisen, cessation is empty. [N-174](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-174)",
    "status": "Retained complete negative sequence with exact limits",
    "reason": "U03998–U04013 was read continuously, including the paired opening N-173. Repeated nonestablishment, pure through purity and cessation-is-empty wording remain. The relation of essence/primordial purity/knowing, tshig med brjod las and the honorific agent at U04012 still admit alternatives; neither a positive doctrinal definition nor a new subject is supplied.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-176",
    "pairs": [
      "DTG-001951",
      "DTG-001952",
      "DTG-001953",
      "DTG-001954",
      "DTG-001955"
    ],
    "ids": [
      "U04031",
      "U04032",
      "U04033",
      "U04034",
      "U04035",
      "U04036",
      "U04037",
      "U04038",
      "U04039",
      "U04040",
      "U04041",
      "U04042",
      "U04043"
    ],
    "realization": "From primordial knowing of all-pervading compassionate responsiveness,\nthe inexhaustible gates of diverse arising\nare complete in essence, though appearing to be exhausted. [N-176](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-176); From the empty intrinsic nature of the dharma embodiment,\nthe aspect of primordial knowing whose knowing is complete\narises for karmic beings through awakened mind.; Without that, the central connection of cyclic existence and transcendence of sorrow would be severed;\nthrough knowing, there is awareness and clarity. [N-176](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-176); From the very identity of clear self-awareness,\nthrough the force of intrinsic nature, compassionate responsiveness itself\nhas not ceased and does not cease.; From the pure aspect of the elements,\nthe one that is not an activity is complete. [N-176](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-176)",
    "status": "Approved labels adopted; contradictions not smoothed",
    "reason": "Awakened mind is now approved P2, not merely the historical proposal described in N-176. Karmic beings and the complete cyclic-existence/transcendence pair are restored. Inexhaustible/appearing exhausted, the central connection and las su med pa gcig remain literal provisional constructions; no ma is inserted into Tibetan.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-177",
    "pairs": [
      "DTG-001959",
      "DTG-001962",
      "DTG-001967",
      "DTG-001975",
      "DTG-001978",
      "DTG-001981",
      "DTG-001982",
      "DTG-001985",
      "DTG-001987",
      "DTG-001994"
    ],
    "ids": [
      "U04049",
      "U04050",
      "U04053",
      "U04054",
      "U04062",
      "U04073",
      "U04074",
      "U04075",
      "U04080",
      "U04081",
      "U04085",
      "U04086",
      "U04087",
      "U04088",
      "U04089",
      "U04093",
      "U04096",
      "U04097",
      "U04098",
      "U04110"
    ],
    "realization": "Mirror-like primordial knowing makes forms clear;\nthe appearance aspects of shape and color are complete. [N-177](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-177); Because it sees the forms of all phenomena,\nit is called ‘primordial knowing through itself.’ [N-177](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-177); Here there is no duality, and it is free from awareness. [N-177](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-177); Discriminating [primordial knowing]: the types of faculty,\nwhatever appears to them, and the phenomena of that appearance\nare each clear in sequence. [N-177](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-177); What is called ‘realization’ is seeing the characteristics,\ntogether with the increase of self-appearance.; What is called ‘doing accomplished’:\nwhen striving and effort have self-ceased,\nall phenomena rest of themselves and are self-liberated.; From Ground-appearance in which self-liberation is complete,\nthe subtle aspect attains freedom from particles and stains.; Simultaneous realization is ‘doing.’; ‘Primordial’ has the meaning of abiding;\nthrough ‘knowing,’ it becomes manifest,\nand one reaches the place where phenomena are exhausted. [N-177](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-177); Through ‘knowing,’ one is liberated from both cyclic existence and transcendence of sorrow.",
    "status": "Whole expressions and wordplay preserved",
    "reason": "Keep mirror-like/discriminating named-category proposals distinct from their explicit syllabic explanations and rtogs realization. Free from awareness at U04062 is written, not an omission to repair doctrinally. Doing accomplished, doing, primordial and knowing remain separately explained. Ground-appearance capitalization and the full cyclic-existence pair are corrected without rewriting the wordplay.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-178",
    "pairs": [
      "DTG-001997",
      "DTG-001999",
      "DTG-002004",
      "DTG-002005",
      "DTG-002008",
      "DTG-002009",
      "DTG-002012",
      "DTG-002014",
      "DTG-002015"
    ],
    "ids": [
      "U04113",
      "U04114",
      "U04115",
      "U04118",
      "U04119",
      "U04120",
      "U04121",
      "U04122",
      "U04123",
      "U04124",
      "U04125",
      "U04131",
      "U04132",
      "U04133",
      "U04137",
      "U04138",
      "U04139",
      "U04140",
      "U04144",
      "U04147",
      "U04148",
      "U04149",
      "U04150"
    ],
    "realization": "Primordial knowing encompassed by knowing\npervades all buddhas and karmic beings\nindivisibly, without intrinsic nature.; In the appearance aspect of karmic beings of the six classes,\nit abides in each one's continuum:\nin gods, it is complete in its own clarity;\nin asuras, subtle and flashing;\nin humans, round and clear of itself;\nin animals, clear within;\nin hungry ghosts, subtle;\nin hell, complete as self-appearance. [N-178](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-178); Primordial knowing encompassed by objects of knowledge\nis to be known in two aspects.; Of these, I shall explain objects of knowledge in their multiplicity.; ‘Whatever’ refers to the natural state;\n‘multiplicity’ completes everything without remainder.; ‘Primordial’ concerns the benefit of all karmic beings;\nthrough ‘knowing,’ the three realms are drawn out from their depths. [N-178](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-178); I shall explain the primordial knowing that knows how [things are].; Through knowing the natural state of entities,\nand realizing one's own benefit, the flow of delusion is exhausted.; ‘How’ refers to the natural state;\n‘view’ engages without distraction. [N-178](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-178)",
    "status": "Labels corrected; knowing modes and explanations preserved",
    "reason": "Keep shes pas knowing distinct from shes byas objects of knowledge and preserve all six classes and their visual descriptions. In particular, without intrinsic nature at DTG-001997 stays explicit, with attachment provisional; ji/lta/snyed explanations are the source’s rhetorical explanations, not externally asserted etymologies. Entity and karmic-being labels are corrected without changing predicates.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-179",
    "pairs": [
      "DTG-002022",
      "DTG-002024",
      "DTG-002026",
      "DTG-002028",
      "DTG-002029",
      "DTG-002030",
      "DTG-002033"
    ],
    "ids": [
      "U04163",
      "U04164",
      "U04168",
      "U04169",
      "U04170",
      "U04172",
      "U04173",
      "U04176",
      "U04177",
      "U04178",
      "U04179",
      "U04180",
      "U04181",
      "U04182",
      "U04183",
      "U04184",
      "U04185",
      "U04193",
      "U04194"
    ],
    "realization": "With Ground, core, and flowers,\nit is beautiful and truly complete. [N-179](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-179); Distinguishing the gathered special features,\nfrom the self-radiance of the nature of phenomena, free from conceptual thought,\nthere arises an appearance of primordial knowing without an object of focus.; As a subsidiary aspect of the true gathering,\nthe key point of primordial knowing arises from the eyes.; In order to exhaust the three realms,\nthe pulsating channel behind the eyes\nis turned upward, bringing down primordial knowing. [N-179](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-179); Whatever primordial knowing arises from the key point,\njust as the nature of phenomena endowed with awareness,\nis completely liberated from all conceptual thought:\nit is primordial knowing arising from basic space.; The key points of the eyes are above and below;\nwhichever avenue of effort the adept employs,\nthere is the appearance of all-gathering primordial knowing. [N-179](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-179); From pervasive primordial knowing, subtle in aspect,\nit is through direct perception and on the path. [N-179](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-179)",
    "status": "Key points corrected; metaphor/instruction limits retained",
    "reason": "The Ground/core/flowers metaphor and the channel/upward-reversal predicates are retained without invented anatomy, gaze instructions or timing. The direct-perception/path fragment remains an exact linked ellipsis. Experiential acquaintance for nyams myong remains distinct from subsequent nyams experience.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-180",
    "pairs": [
      "DTG-002034",
      "DTG-002035",
      "DTG-002038",
      "DTG-002039",
      "DTG-002041",
      "DTG-002045"
    ],
    "ids": [
      "U04195",
      "U04196",
      "U04197",
      "U04198",
      "U04199",
      "U04200",
      "U04204",
      "U04205",
      "U04206",
      "U04207",
      "U04209",
      "U04215",
      "U04216"
    ],
    "realization": "Furthermore, this is to be explained:\nfrom mindfulness and reflection in which differentiating conceptualization gathers,\neven the dharma embodiment becomes form. [N-180](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-180); One who wishes to go beyond the three realms,\nthrough the great key point of sacred primordial knowing,\nexamines the respective winds as breaths.; From the intrinsic nature of gathered mindfulness and reflection,\neven the dharma embodiment becomes cyclic existence. [N-180](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-180); When the limits of cyclic existence are exhausted,\none is liberated in one's own place without anything being done.; Because there is nothing, the nature of phenomena is not an entity.; By finding going and arising,\nentities being pure, form is exhausted. [N-180](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-180)",
    "status": "Approved labels corrected; difficult predicates retained",
    "reason": "Preserve dharma embodiment becomes form/becomes cyclic existence, their conditions, the repeated cessation chain and the unnegated finding-going/arising clause. Entity does not mean only matter. gal te in DTG-002035 is already realized by the restrictive one-who-wishes condition; no stylistic rewrite is needed.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-181",
    "pairs": [
      "DTG-002047",
      "DTG-002049",
      "DTG-002051",
      "DTG-002054",
      "DTG-002055",
      "DTG-002056"
    ],
    "ids": [
      "U04218",
      "U04219",
      "U04220",
      "U04224",
      "U04225",
      "U04226",
      "U04230",
      "U04235",
      "U04236",
      "U04237",
      "U04238",
      "U04239",
      "U04240"
    ],
    "realization": "From earth, water, fire, wind, and space,\nthrough the wonder of primordial knowing's appearance,\nthe Blessed One, the protector, is without awareness. [N-181](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-181); The moon, a jewel, ‘mar gar,’ and light—\none who wishes to hold these\nholds the appearance of embodiment arising from holding. [N-181](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-181); Through complete realization, it is free from blue. [N-181](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-181); Beyond phrases, free from the conceptual mind, empty in essence,\nits intrinsic nature not differentiated anywhere,\nthe deeds of compassionate responsiveness do not appear. [N-181](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-181); From the third appearance of primordial knowing,\ndiscerning knowing arising from the mental faculty is held as an aspect of delusion. [N-181](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-181); Here there is no limit of differentiated focus.",
    "status": "Honorific corrected; lexical/negative questions retained",
    "reason": "Blessed One retains the additional protector and the written without-awareness predicate. Free from blue is also written. mar gar is unresolved, not guessed as butter, pearl or lamp. yid ’byung shes rab retains its linked mental-faculty/disenchantment alternatives; the shortened differentiated-focus construction at DTG-002056 remains provisional rather than forced from components.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-183",
    "pairs": [
      "DTG-002061",
      "DTG-002063",
      "DTG-002066",
      "DTG-002067",
      "DTG-002069"
    ],
    "ids": [
      "U04248",
      "U04249",
      "U04251",
      "U04252",
      "U04255",
      "U04256",
      "U04258",
      "U04259"
    ],
    "realization": "There is the appearance of the exhaustion of knowing's experience;\nincrease is shown like the waxing moon.; Through warmth, measure, and signs,\nthe two truths enter in union, and the limits of conceptual thought are exhausted.; Since outflows are exhausted, there is no material weight.; The interior of mindfulness ceases; essence is clear. [N-183](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-183); Free from words, truly without phrases,\nall bases of dependence are exhausted.",
    "status": "No change; continuation and distinct material expression preserved",
    "reason": "Read U04245–U04259 through the next sensory section. Exhaustion and waxing-moon increase remain distinct, as do warmth, measures and signs. khong ’gag remains interior-of-mindfulness provisional. rdos bcas material weight is not bem po: the approved matter label does not justify an English substring replacement. Words/phrases remain distinguished in the same source line.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-184",
    "pairs": [
      "DTG-002071",
      "DTG-002073",
      "DTG-002074",
      "DTG-002075",
      "DTG-002077",
      "DTG-002078",
      "DTG-002079",
      "DTG-002080",
      "DTG-002081"
    ],
    "ids": [
      "U04261",
      "U04262",
      "U04265",
      "U04266",
      "U04267",
      "U04268",
      "U04269",
      "U04270",
      "U04271",
      "U04272",
      "U04273",
      "U04274",
      "U04275",
      "U04276",
      "U04279",
      "U04280",
      "U04281",
      "U04282",
      "U04283",
      "U04284",
      "U04285",
      "U04286",
      "U04287",
      "U04288"
    ],
    "realization": "The two trainings through form\nare a support for an object of focus and absence of an object of focus.; Become familiar with shapes and then with colors;\nthrough this familiarity, delusory appearance ceases.; For sound, with a pure support for an object of focus:\npiwaṃ, earthenware drum, resonant pot,\ndraba, the many-stringed instrument, the three-junctioned instrument,\nhar, flute, cymbals,\npheg, rdob, small hand drum, bell, and so forth—\njoin wind to each respective sound. [N-184](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-184); For smell, through a condition for focus agreeable to the mental faculty,\nfaith and great faith,\nthe supreme and the greatly distinctive,\njoin the yogin to great bliss. [N-184](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-184); Knowing the five stages endowed with restraint,\nmerely tasting makes primordial knowing blaze. [N-184](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-184); For touch, with a support for an object of focus agreeable to the mental faculty,\njoin each awareness to experiential acquaintance.; When a tree leaf curls rightward and contracts,\nraise it: through touch, buddhahood is realized. [N-184](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-184); Concerning phenomena, accord with the lama's transmission.; If excellent cultivation is realized,\npracticing thus brings it onto the path,\nand the flow of the machinery of delusion in the three realms is cut.",
    "status": "Approved components/condition corrected; sensory constructions bounded",
    "reason": "Restore object-of-focus in the paired form/sound/touch support expressions, familiarization-family wording, unmodified transmission and explicit if. Keep acoustic sound, instrument names, six [tastes], five stages, restraint (not sacred pledge), and the leaf operation in their original scope. The different complete dmigs rkyen construction and the yi(d)-agreeable expressions remain provisional rather than automatically rebuilt. No practical recipe or instrument identity is invented.",
    "review": "REVIEW.md#phase-d-notes-12"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-185",
    "pairs": [
      "DTG-002083",
      "DTG-002084",
      "DTG-002085",
      "DTG-002087",
      "DTG-002088"
    ],
    "ids": [
      "U04293",
      "U04294",
      "U04295",
      "U04296",
      "U04297",
      "U04298",
      "U04299",
      "U04300",
      "U04303",
      "U04304",
      "U04305"
    ],
    "realization": "From the yellow that generates qualities,\nin an activity in which the Ground and differentiation are simultaneous,\nthe nature of phenomena is shown. [N-185](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-185); From the red of complete self-expressiveness,\nthe center and surrounding of pure intrinsic nature,\nthe encircling bands and enclosure, are shown in completeness.; From the green free from doing-expressiveness,\nemanations of pure enlightened activity arise.; Through pure intrinsic nature, the embodiments are ‘three, four.’ [N-185](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-185); Thus, from the Great All-Penetrating Word, Root of All Phenomena:\nthe third chapter, the Array of Primordial Knowing, in which the root of appearance definitely emerges.",
    "status": "No change; five-color account and closing uncertainty retained",
    "reason": "Preserve the five colors, center-and-surrounding wording (not blindly replace with mandala), doing-expressiveness construction, and three, four. The Ground/differentiation attachment stays provisional. The colophon was compared with the opening, and the empty golden C3-TRANSITION graphic remains explicitly unresolved rather than deciphered.",
    "review": "REVIEW.md#phase-d-notes-12"
  }
]
```

### Changed-clause self-check and actual tests

Every changed pair was reread against its whole Tibetan clause, with necessary neighboring context and the complete applicable glossary rows. The complete revised Chapter 3 English was then read continuously. The self-check found and repaired the second preposition after become familiar with (PD-B12-061); this is explicitly a repair of this reviewer’s own change. The resulting sequence preserves all objects, conditions, negations, source counts and meaningful term components. Unresolved radiance-negation scope and the other recorded constructions are not certified. This is self-check, not another independent review.

Actual checks pass: 469-operation exact replay, 412 cumulatively changed pairs, fixed Tibetan/golden/policy bytes, all 2,667 IDs/order/envelopes, unchanged inherited note associations/footer, original usage records and previous dispositions, and 700 English local-link targets. The paired suite was actually rerun: 64 tests; 53 pass, 9 fail, 2 error at the historical exact-English gate. The pre-edit protected-glossary failure is unchanged; no successful release-output regeneration is claimed. A diagnostic import of check_links from core failed before that check; the subsequent correct validate.check_links call actually passed. Two bundled commands were blocked before execution; only the successful individual calls support these results. No semantic regression specification is claimed executed.

<!-- pd05-batch-12-verification -->


<a id="phase-d-batch-13"></a>
## Batch 13 — source ordinals 2097–2333

Reviewer/session **DTG-PD-20261005-Astra-05**, review-and-revise. Read every source/English pair in order, **DTG-002090–DTG-002326**, including source headings, across-pair continuations and source layers. 32 newly encountered note records were read with their current dispositions: G-A2000-C04-S01, G-C4-TRANSITION, G-U04312, G-U04519, G-U04562, G-U04703, G-U04763, N-186, N-187, N-188, N-189, N-190, N-191, N-192, N-193, N-194, N-195, N-196, N-197, N-198, N-199, N-200, N-201, N-202, N-203, N-T100, N-T101, N-T102, N-T95, N-T96, N-T98, N-T99. Q1–Q9, I §8.1 and Part III were applied by reading; subsequent searches test the observed terminology patterns, not replace the reading. The following evidence is recorded before English application.

Batch input: **8637559bd2e7fde13d46d4353d7ccb3db6d6e12c**, remote-verified. All 237 chapter pairs were read, including the restored questions, all twenty-one numbered explanations, subsequent continuum/liberation sections, prose colophon and unresolved boundary graphic. Important no-change cases include permitted possessive/verbal rang shes and adjectival rang rig, scoped heart/citta, genuine acoustic sound, material weight from rdos rather than bem po, written negative predicates, and already separated source variants. These require source relations and full rows, not substring verdicts. Newly clarified omissions/rhetorical grammar and the missing quotation close are recorded below; remaining construction questions are explicitly retained with alternatives and evidence needed.

### Recorded scoped corrections

```json
[
  {
    "finding": "PD-B13-001",
    "pair": "DTG-002093",
    "golden": [
      "U04314",
      "U04315",
      "U04316",
      "U04317"
    ],
    "tibetan": "སངས་རྒྱས་དགོངས་པའི་གདེང་རྙེད་ཀྱང༌། །\nམ་འོངས་འཇུག་པའི་སེམས་ཅན་རྣམས། །\nརྟོག་བྲལ་ཡེ་ཤེས་རྫོགས་དོན་དུ། །\nཆོས་ཉིད་བཀོད་པ་མཉམ་པར་འཚལ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can requires the complete karmic-being label; preserve the grammatical plural and the existing body/knowing distinctions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-002",
    "pair": "DTG-002095",
    "golden": [
      "U04319"
    ],
    "tibetan": "འགྱུ་མཚམས་ཉིད་ཀྱི་གནད་དེ་གང༌། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-003",
    "pair": "DTG-002098",
    "golden": [
      "U04322"
    ],
    "tibetan": "སེམས་ཅན་དུས་ན་ཅི་ལྟར་གནས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can requires the complete karmic-being label; preserve the grammatical plural and the existing body/knowing distinctions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-004",
    "pair": "DTG-002099",
    "golden": [
      "U04323"
    ],
    "tibetan": "ལུས་ཀྱི་གནད་ནི་གང་དང་གང་། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-005",
    "pair": "DTG-002110",
    "golden": [
      "U04333"
    ],
    "tibetan": "འབྱུང་དུས་གནད་འདི་ཅི་ཡིས་བཟུང་། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-006",
    "pair": "DTG-002113",
    "golden": [
      "U04336"
    ],
    "tibetan": "འདི་དག་སེམས་ཅན་དོན་དུ་གསུང་། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can requires the complete karmic-being label; preserve the grammatical plural and the existing body/knowing distinctions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-007",
    "pair": "DTG-002138",
    "golden": [
      "U04383"
    ],
    "tibetan": "འཁོར་འདས་མིང་དུ་མ་གྲགས་སོ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "The established complete khor ’das compound preserves both approved members; do not omit sorrow or reinterpret either member as a death event.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-008",
    "pair": "DTG-002142",
    "golden": [
      "U04387",
      "U04388",
      "U04389"
    ],
    "tibetan": "རྒྱུ་རྐྱེན་བྲལ་བའི་སྐད་ཅིག་ལས། །\nསངས་རྒྱས་སེམས་ཅན་གཞི་མར་སྣང༌། །\nདུ་མ་ཆ་ཤས་ཀུན་བྲལ་བའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can requires the complete karmic-being label; preserve the grammatical plural and the existing body/knowing distinctions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-009",
    "pair": "DTG-002144",
    "golden": [
      "U04391",
      "U04392",
      "U04393",
      "U04394",
      "U04395"
    ],
    "tibetan": "གལ་ཏེ་འཁྲུལ་པའི་སེམས་ཅན་ལ། །\nསྐུ་དང་ཡེ་ཤེས་རང་ལུགས་ཏེ། །\nརྣལ་མ་སོ་མ་ལྷུག་པ་སྟེ། །\nགྱི་ནར་གནས་པ་ཁོ་ན་དང་། །\nདབང་པོ་ཡུལ་ལ་རང་བཞིན་ནོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can requires the complete karmic-being label; preserve the grammatical plural and the existing body/knowing distinctions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-010",
    "pair": "DTG-002147",
    "golden": [
      "U04402",
      "U04403"
    ],
    "tibetan": "སྣ་ཚོགས་འགྱུ་བ་སོ་སོའི་གནད། །\nགཅིག་ཤེས་པ་ཡིས་གྲོལ་བར་གནས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-011",
    "pair": "DTG-002150",
    "golden": [
      "U04407",
      "U04408",
      "U04409"
    ],
    "tibetan": "ལུས་ཀྱི་གནད་ནི་འདི་ལྟ་སྟེ། །\nསྤྱི་དང་ཙིཏྟ་རྩ་ཡི་གནད། །\nམ་བཅོས་དག་པའི་ཆོས་ཉིད་གནས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-012",
    "pair": "DTG-002151",
    "golden": [
      "U04410",
      "U04411"
    ],
    "tibetan": "སེམས་ཅན་ཀུན་གྱི་ལུས་སྤྱི་ལ། །\nཆོས་ཉིད་རླུང་གི་ཚུལ་དུ་ཁྱབ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "rationale": "P2 sems can requires the complete karmic-being label; preserve the grammatical plural and the existing body/knowing distinctions.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-013",
    "pair": "DTG-002159",
    "golden": [
      "U04425",
      "U04426"
    ],
    "tibetan": "འཇུག་པའི་ཐིག་ལེ་རྣམ་གསུམ་གྱིས། །\nའཁོར་འདས་འབྲེལ་པའི་ས་བོན་འདེབས། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "The established complete khor ’das compound preserves both approved members; do not omit sorrow or reinterpret either member as a death event.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-014",
    "pair": "DTG-002175",
    "golden": [
      "U04463",
      "U04464"
    ],
    "tibetan": " དེ་ལ་ཅི་ཡིས་མཐོང་བ་ནི། །\nགོམས་དང་གནད་ཀྱིས་མཐོང་བ་སྟེ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-015",
    "pair": "DTG-002176",
    "golden": [
      "U04465",
      "U04466",
      "U04467",
      "U04468"
    ],
    "tibetan": "གོམས་པ་སྔོན་དུ་འགྲོ་བ་ནས། །\nབརྩམས་ཏེ་ལུས་ངག་གནད་གཟིར་བས། །\nརང་སྣང་དག་པའི་གཟུགས་མཐོང་ནས། །\nའཁྲུལ་པ་ཐམས་ཅད་ནུབ་པའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-016",
    "pair": "DTG-002177",
    "golden": [
      "U04469"
    ],
    "tibetan": "གནད་ཀྱི་ལུས་ཀྱིས་མཐོང་བར་བྱེད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-017",
    "pair": "DTG-002183",
    "golden": [
      "U04485"
    ],
    "tibetan": "མཐོང་ནས་གནད་ལ་དབབ་པ་སྟེ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-018",
    "pair": "DTG-002184",
    "golden": [
      "U04486",
      "U04487"
    ],
    "tibetan": "སྣང་བ་འཁྲིད་པའི་ཐབས་ཀྱིས་ཀྱང་། །\nའབྱུང་བཞིའི་སྣང་བ་གནད་ལ་ཕེབས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-019",
    "pair": "DTG-002185",
    "golden": [
      "U04488",
      "U04489"
    ],
    "tibetan": "རླུང་བརྒྱད་ལས་ཀྱི་འབྲེལ་བརྩིས་པས། །\nརྣམ་རྟོག་དུ་མ་གནད་ལ་ཕེབས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-020",
    "pair": "DTG-002186",
    "golden": [
      "U04490",
      "U04491",
      "U04492",
      "U04493"
    ],
    "tibetan": "ལུས་ནི་གཅུད་དང་རྩལ་སྤྲུག་དང་། །\nཡན་ལག་བརྡབ་འཕེན་སྡུད་པའི་གནད། །\nཕྲ་ཞིང་དྲང་ལ་མཉེ་བ་ཡིས། །\nཤ་དང་ཁྲག་སྟེ་རུས་པ་ལའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-021",
    "pair": "DTG-002234",
    "golden": [
      "U04595",
      "U04596",
      "U04597",
      "U04598",
      "U04599"
    ],
    "tibetan": "གནད་ཀྱི་ཆོས་ཉིད་འདི་ལྟ་སྟེ། །\nའབྱུང་བའི་གནས་དང་རང་ལུས་དང་། །\nཡུལ་དང་སྒོ་དང་ཤེས་པ་རླུང༌། །\nརྩ་དང་ཐིག་ལེ་ཡན་ལག་གིས། །\nསོ་སོའི་འཇུག་པ་ཁྱབ་པར་གནས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-022",
    "pair": "DTG-002237",
    "golden": [
      "U04607"
    ],
    "tibetan": "འདིས་ནི་གནད་ཀྱི་འཚང་རྒྱའོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-023",
    "pair": "DTG-002239",
    "golden": [
      "U04609",
      "U04610"
    ],
    "tibetan": "འབྱུང་དུས་གནད་ནི་འདི་ལྟ་བུ། །\nཨེ་མ་ངོ་མཚར་ཆེ་བ་བཤད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-024",
    "pair": "DTG-002242",
    "golden": [
      "U04616",
      "U04617"
    ],
    "tibetan": "རང་བཞིན་དག་པའི་གནད་ཤེས་ནས། །\nབྱས་པ་མེད་པར་ཆོས་རྣམས་ཤེས། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-025",
    "pair": "DTG-002275",
    "golden": [
      "U04684",
      "U04685"
    ],
    "tibetan": "རིགས་དང་དབང་པོའི་རྣམ་འཕྲུལ་ལས། །\nའཁོར་འདས་རྟོག་པ་ཐ་དད་དེ། །",
    "before": "samsara and nirvana",
    "after": "cyclic existence and transcendence of sorrow",
    "rationale": "The established complete khor ’das compound preserves both approved members; do not omit sorrow or reinterpret either member as a death event.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-026",
    "pair": "DTG-002278",
    "golden": [
      "U04689",
      "U04690",
      "U04691",
      "U04692"
    ],
    "tibetan": "མ་དག་པ་ཡི་འཁྲུལ་པ་ལ། །\nདབང་པོའི་སྒོ་རྣམས་མ་བཅོས་པས། །\nཅོག་གེ་བཞག་པ་གནད་ཡིན་ལ། །\nདེ་ལས་མ་བསྒྱུར་མན་ངག་གོ། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-027",
    "pair": "DTG-002307",
    "golden": [
      "U04741"
    ],
    "tibetan": "གནད་ཀྱིས་གྲོལ་བས་འབད་རྩོལ་ཟད། །",
    "before": "crucial point",
    "after": "key point",
    "rationale": "P2 gnad requires key point(s). The actual source here names the explanatory or contemplative key point; keep the source count, modifiers and each repetition.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-028",
    "pair": "DTG-002090",
    "golden": [
      "U04306",
      "U04307",
      "U04308"
    ],
    "tibetan": "དེ་ནས་ལྷ་དབང་དགའ་བྱེད་ཀྱིས། །\nསྟོན་པ་ཁྱབ་བདག་ཆེན་པོ་ལ། །\nཆོས་ཉིད་བཀོད་པའི་རང་བཞིན་ཞུས། །",
    "before": "Maker of Joy",
    "after": "Joy-Maker",
    "rationale": "The same lha dbang dga byed is the recurring interlocutor already named Joy-Maker in Chapters 2–3. Preserve the Lord of Gods honorific. This is within-work identity consistency, not a new shared name assignment.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-029",
    "pair": "DTG-002091",
    "golden": [
      "U04309",
      "U04310",
      "U04311",
      "U04312"
    ],
    "tibetan": "ཀྱེ་ཀྱེ་ཡང་དག་རྫོགས་སངས་རྒྱས། །\nབདག་ནི་ཡེ་ཤེས་བཀོད་པ་ལས། །\nའཁོར་བའི་ལས་ལས་དབུགས་ཕྱུང་སྟེ། །\nམྱང་འདས་ལམ་ལ་བསྟོད། །",
    "before": "samsara",
    "after": "cyclic existence",
    "rationale": "The actual khor ba noun has the approved cyclic-existence equivalent. Retain the activities and respite construction.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-030",
    "pair": "DTG-002091",
    "golden": [
      "U04309",
      "U04310",
      "U04311",
      "U04312"
    ],
    "tibetan": "ཀྱེ་ཀྱེ་ཡང་དག་རྫོགས་སངས་རྒྱས། །\nབདག་ནི་ཡེ་ཤེས་བཀོད་པ་ལས། །\nའཁོར་བའི་ལས་ལས་དབུགས་ཕྱུང་སྟེ། །\nམྱང་འདས་ལམ་ལ་བསྟོད། །",
    "before": "passing beyond sorrow",
    "after": "transcendence of sorrow",
    "rationale": "The explicitly attested myang ’das / mya ngan ’das noun is governed by path of or characteristics of, not a finite passing predicate; use the approved technical noun. The bstod uplifted/praise question remains unresolved at DTG-002091.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-031",
    "pair": "DTG-002156",
    "golden": [
      "U04420",
      "U04421"
    ],
    "tibetan": "དག་པའི་སྐུ་ནི་རྣམ་གསུམ་གྱིས། །\nམྱ་ངན་འདས་པའི་མཚན་ཉིད་འཛིན། །",
    "before": "passing beyond sorrow",
    "after": "transcendence of sorrow",
    "rationale": "The explicitly attested myang ’das / mya ngan ’das noun is governed by path of or characteristics of, not a finite passing predicate; use the approved technical noun. The bstod uplifted/praise question remains unresolved at DTG-002091.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-032",
    "pair": "DTG-002109",
    "golden": [
      "U04332"
    ],
    "tibetan": "གནད་ཀྱི་ཆོས་ཉིད་གང་དང་གང༌། །",
    "before": "What are its crucial points?",
    "after": "What is the nature of phenomena of the various key points?",
    "rationale": "U04332 explicitly has gnad kyi chos nyid. The old pronoun paraphrase loses the nature-of-phenomena head and reverses the genitive relation. The corresponding reply DTG-002234 repeats this same head and confirms the inquiry. Restore it with the approved key-point label and distributed plurality.",
    "severity": "moderate omission and relation",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-033",
    "pair": "DTG-002188",
    "golden": [
      "U04495",
      "U04496",
      "U04497",
      "U04498",
      "U04499",
      "U04500",
      "U04501",
      "U04502",
      "U04503",
      "U04504",
      "U04505"
    ],
    "tibetan": "དེ་ལྟར་ཕེབས་ནས་རྫོགས་པའི་ཚད། །\nཐད་ཀའི་ངོས་སྣང་འགགས་པ་དང་། །\nས་རྡོར་སྣང་བ་གཞུག་པ་དང༌། །\nརང་ཤེས་ཅི་ལའང་ཚུད་པ་དང༌། །\nདེ་བཙུད་བེམ་པོ་འགུལ་བ་དང་། །\nརླུང་གི་འགྱུ་བའི་ཚད་ཟིན་དང༌། །\nལུས་ཀྱི་རྡུལ་ཕྲན་མཐོང་བ་འབྱུང༌། །\nཅིར་སྣང་གཟུགས་སྐུར་རྫོགས་པ་དང༌། །\nདེ་ལ་ཡབ་ཡུམ་འཁྲིལ་པ་དང་། །\nལྔ་ལྔ་ཡབ་དང་ཡུམ་སྦྱོར་དང༌། །\nཀུན་ཀྱང་མུ་ཁྱུད་ཟླུམ་པོ་ལ། །",
    "before": "moving insentient things",
    "after": "moving matter",
    "rationale": "Actual bem po under ’gul ba uses the approved mass-noun matter. Preserve moving: the policy specifically does not assert immobility. Explain the non-knowing side in the linked note rather than replacing matter with insentient matter.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-034",
    "pair": "DTG-002191",
    "golden": [
      "U04510",
      "U04511",
      "U04512"
    ],
    "tibetan": "ཚད་ཕེབས་ལུགས་ཀྱང་འདི་ལྟར་འགྱུར། །\nསོ་སོའི་ལུས་ཀྱི་རྡུལ་བྲལ་ནས། །\nབར་སྣང་འོད་ཀྱི་སྐར་ཁུང་སྣང་། །",
    "before": "intervening space",
    "after": "open sky",
    "rationale": "Actual bar snang describes where windows of light appear, with no stated pair of endpoints or emphatic interval. Use the approved open-sky default while retaining the windows and body-particle qualification.",
    "severity": "minor terminology",
    "confidence": "high"
  },
  {
    "finding": "PD-B13-035",
    "pair": "DTG-002236",
    "golden": [
      "U04604",
      "U04605",
      "U04606"
    ],
    "tibetan": "ཟད་སྣང་གཉིས་མེད་ཡུལ་ལས་ནི། །\nརང་བཞིན་གནས་དང་བཅོས་མ་ལས། །\nཆོས་ཀྱི་དབྱིངས་ཀྱང་དག་པས་སྣང་། །",
    "before": "intrinsic abiding",
    "after": "intrinsic nature’s abiding",
    "rationale": "The Tibetan rang bzhin gnas must preserve intrinsic nature, even in this abbreviated/adverbial construction. Do not use the correction to resolve the still-provisional attachment to bcos ma [practice].",
    "severity": "minor terminology",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B13-036",
    "pair": "DTG-002316",
    "golden": [
      "U04750"
    ],
    "tibetan": "དེ་ལ་གྲོལ་ཞེས་སུ་ལ་དམིགས། །",
    "before": "For whom there is ‘liberated,’ what is the object of focus?",
    "after": "There, in saying ‘liberated,’ who is the object of focus?",
    "rationale": "The source de la grol zhes su la dmigs contains one referential question, su la, about whom the designation liberated concerns. The old English adds a second what question and breaks the grammar. Read the adjacent whose-realization / for-whom-entry questions continuously; preserve the single human referent and question rather than answer it.",
    "severity": "moderate syntax and rhetorical function",
    "confidence": "moderate-high"
  },
  {
    "finding": "PD-B13-037",
    "pair": "DTG-002324",
    "golden": [
      "U04760",
      "U04761"
    ],
    "tibetan": "ཡེ་ནས་འབྲས་བུ་བློ་བྲལ་ཉིད། །\nསྨྲ་བསམ་བརྗོད་པ་ཀུན་འདས་པའོ། །",
    "before": "beyond all speaking, thinking, and expression.",
    "after": "beyond all speaking, thinking, and expression.’",
    "rationale": "The teacher’s direct speech opens with ‘Ema at DTG-002115 and continues through this final verse. The next pair is the narrative chapter colophon introduced by zhes. Close the English quotation at this boundary, without adding speech to the colophon.",
    "severity": "minor quotation boundary",
    "confidence": "high"
  }
]
```

<a id="phase-d-notes-13"></a>
### Active note/usage dispositions

The following dated dispositions are appended to the existing usage record and linked from the existing legacy index; original approvals/proposals and source notes remain historical. A retained provisional construction is not an approved new shared equivalent.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-186",
    "pairs": [
      "DTG-002090",
      "DTG-002091",
      "DTG-002093",
      "DTG-002102",
      "DTG-002109",
      "DTG-002114",
      "DTG-002175"
    ],
    "ids": [
      "U04306",
      "U04307",
      "U04308",
      "U04309",
      "U04310",
      "U04311",
      "U04312",
      "U04314",
      "U04315",
      "U04316",
      "U04317",
      "U04326",
      "U04332",
      "U04337",
      "U04338",
      "U04339",
      "U04340",
      "U04463",
      "U04464"
    ],
    "realization": "Then the Lord of Gods, Joy-Maker,\nasked the teacher, the great all-pervading lord,\nabout the intrinsic nature of the Array of the Nature of Phenomena.; ‘Kye kye! Truly complete buddha,\nthrough the Array of Primordial Knowing,\nI have gained respite from the activities of cyclic existence,\nand been uplifted on the path of transcendence of sorrow. [N-186](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-186); Although I have gained confidence in the buddhas' enlightened intent,\nfor karmic beings who will enter in the future,\nso that primordial knowing free from conceptual thought may be complete,\nI seek the Array of the Nature of Phenomena in evenness. [N-186](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-186); As what does it appear there? [N-186](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-186); What is the nature of phenomena of the various key points?; Then, [the words of] the teacher Vajradhara,\nfrom the space of pure intrinsic nature—\nthese elaborations of words and phrases—\narose in the Ground free from expression. [N-186](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-186); As for by what it is seen:\nit is seen through familiarity and the key points.",
    "status": "Approved labels and omitted question head corrected; construction limits retained",
    "reason": "Joy-Maker consistently names the recurring interlocutor; karmic beings and the transcendence/cyclic-existence nouns are adopted. The gnad kyi chos nyid question is repaired by comparison with its actual reply. G-U04312 already separates gzengs; bstod still leaves uplifted versus praise unresolved. Keep the source difference between as-what appearance in the question and by-what seeing in the ninth reply. The mnyam par attachment and bracketed words of the teacher remain provisional, not a new speaker or independently approved supply.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-187",
    "pairs": [
      "DTG-002118",
      "DTG-002140",
      "DTG-002141",
      "DTG-002142"
    ],
    "ids": [
      "U04345",
      "U04346",
      "U04347",
      "U04348",
      "U04349",
      "U04385",
      "U04386",
      "U04387",
      "U04388",
      "U04389"
    ],
    "realization": "The nature of phenomena of abiding is as follows:\nabiding in its fundamental disposition, it is free from virtue and wrongdoing;\nabiding as cause and result, it is free from dependence;\nabiding through conditions, the elements are pure—\nit does not shift or change. [N-187](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-187); All-arising primordial knowing is not any [thing]. [N-187](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-187); There is no taking and no liberation.; In a moment free from causes and conditions,\nbuddhas and karmic beings appear as a foundation,\nfree from all multiplicity and parts. [N-187](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-187)",
    "status": "Karmic-being label adopted; negative and foundation questions retained",
    "reason": "The three modes of abiding and their absence of change were read with the buddha explanation. gang ma yin still admits a negation of any particular item or a denial of the described all-arising primordial knowing; the bracketed generic [thing] is not dngos po and must not be changed to entity by substring search. Foundation for gzhi ma remains a construction question, not a global Ground exception; len pa taking stays distinct from nyer len appropriation.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-188",
    "pairs": [
      "DTG-002121",
      "DTG-002122",
      "DTG-002124",
      "DTG-002125",
      "DTG-002126",
      "DTG-002129",
      "DTG-002130",
      "DTG-002133"
    ],
    "ids": [
      "U04353",
      "U04354",
      "U04355",
      "U04356",
      "U04357",
      "U04358",
      "U04359",
      "U04361",
      "U04362",
      "U04363",
      "U04364",
      "U04365",
      "U04369",
      "U04370",
      "U04371",
      "U04372",
      "U04373",
      "U04376"
    ],
    "realization": "Wind, according to the sequence of a day,\nis reckoned as twenty thousand, one thousand,\nand six hundred;\nthe winds of one day are thereby complete.; According to the particular distinctions,\nfor the young there are sixty extra;\nfor the old there is a shortfall.; Among sixty movements of wind,\nthe subtle movement of the nature of phenomena is held through reckoning.; From two such groups it is coarse;\nwhen these are gathered as three, it is gross.; Subtract three from that: it is even. [N-188](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-188); The nature of phenomena of time is as follows:\nouter, inner, secret,\nand suchness—four.; The outer is the second [month] of autumn,\nshowing the abiding of the nature of phenomena of time.; Suchness is held through wind.",
    "status": "No change; numerical and time grouping remains provisional",
    "reason": "Every written count and the omission of a definite shortfall for the old are preserved. The two/three grouping and subtract-three operation are not silently converted into a modern breath schedule. [Month] remains a marked supply. khon na nyid suchness remains a whole-expression proposal, not a component-derived canonical entry or a new default.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-189",
    "pairs": [
      "DTG-002144",
      "DTG-002145",
      "DTG-002147"
    ],
    "ids": [
      "U04391",
      "U04392",
      "U04393",
      "U04394",
      "U04395",
      "U04396",
      "U04397",
      "U04398",
      "U04399",
      "U04400",
      "U04402",
      "U04403"
    ],
    "realization": "As for deluded karmic beings:\nembodiments and primordial knowing are in their own manner,\ngenuine, fresh, and letting be—\nabiding solely in ‘gyi nar’ [unresolved expression],\nintrinsic nature at the faculties' objects. [N-189](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-189); Here their own object is shown;\nwithout entering into surrounding conditions,\nin unobstructedness and penetration,\nfrom the appearance aspects of object and knowing,\neach is directly liberated from its own Ground. [N-189](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-189); In the respective key points of diverse movement,\nknowing one, one abides liberated.",
    "status": "Key-point and karmic-being labels adopted; unresolved expressions retained",
    "reason": "gyi nar remains an exact unresolved span. The preceding gal te topical introduction remains bounded as for, not a claim about an actual hypothetical event; its relation to the following sentence remains provisional. zang ma nyid dang thal byung is not the exact zang thal compound: keep the separate provisional wording and do not collapse the two members. khor rkyen surrounding conditions is not an automatic khor ba cyclic-existence hit.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-190",
    "pairs": [
      "DTG-002150",
      "DTG-002151",
      "DTG-002153",
      "DTG-002154",
      "DTG-002155",
      "DTG-002156",
      "DTG-002157",
      "DTG-002158",
      "DTG-002159",
      "DTG-002160",
      "DTG-002161"
    ],
    "ids": [
      "U04407",
      "U04408",
      "U04409",
      "U04410",
      "U04411",
      "U04415",
      "U04416",
      "U04417",
      "U04418",
      "U04419",
      "U04420",
      "U04421",
      "U04422",
      "U04423",
      "U04424",
      "U04425",
      "U04426",
      "U04427",
      "U04428",
      "U04429",
      "U04430"
    ],
    "realization": "The key points of the body are as follows:\nthe general [body], the heart, and the channels—\nthe pure, uncontrived nature of phenomena abides there. [N-190](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-190); Throughout the bodies of all karmic beings,\nthe nature of phenomena pervades in the manner of wind.; Within the heart it abides as embodiment.; The embodiments of radiance have five aspects;\nthey hold the characteristics of their respective families.; The six embodiments of rays\ngather the phenomena of intrinsic nature's appearance.; Through the three aspects of pure embodiment,\nthe characteristics of transcendence of sorrow are held.; Through the eight aspect-embodiments,\nthe doing of completing grounds and paths is done. [N-190](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-190); Within the channels are spheres.; Through three aspects of entering spheres,\nthe seeds connecting cyclic existence and transcendence of sorrow are planted.; Through the five arising spheres,\nthe mandala of yogic experience is established.; Through the six arraying spheres,\nthe manifold nature of phenomena is gathered into one.",
    "status": "Approved labels adopted; locally justified heart retained",
    "reason": "The full citta row permits heart only with established referent and an explanatory note. Here the body’s general/heart/channel sequence, citta’s interior containing embodiments, and the contrasted channels containing spheres support the contextual heart use at DTG-002150/002153. This is a scoped interpretation, not a change from canonical citta or a modern anatomical identification. General [body] is supported by the immediately following lus spyi, unlike the explicit crown later. The key-point list attachment and six short class-label proposals remain provisional; preserve every five/six/three/eight and three/five/six count without invented class members.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-191",
    "pairs": [
      "DTG-002165",
      "DTG-002166",
      "DTG-002167",
      "DTG-002168",
      "DTG-002169",
      "DTG-002171",
      "DTG-002172"
    ],
    "ids": [
      "U04437",
      "U04438",
      "U04439",
      "U04440",
      "U04441",
      "U04442",
      "U04443",
      "U04444",
      "U04445",
      "U04446",
      "U04447",
      "U04448",
      "U04449",
      "U04450",
      "U04452",
      "U04453",
      "U04454",
      "U04455",
      "U04456",
      "U04457",
      "U04458",
      "U04459"
    ],
    "realization": "Moved by pervading wind,\nvajra chains [arise] from awareness itself.; Gathered by ripening wind,\nthey appear as embodiments in fivefold pairs. [N-191](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-191); From the eyes, the two winds of apprehended object and apprehending subject:\nthrough the right, the apprehended aspect, appearance increases;\nthrough the left, the apprehending aspect, colors are complete. [N-191](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-191); At the ears, from pervading and entering winds,\nthe right, through pervasion, displays sounds;\nthe left, through the activity of entering wind,\nholds each respective [sound].; The wind of complete pervasion at the crown,\nsubtle and without generation,\nalso holds the embodiments of awareness. [N-191](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-191); The characteristics of appearing in the object:\nfrom space, clear blue and unstirred,\nlight, colors, and shapes\ndisplay the self-appearance of the five primordial knowings.; From the lamp of pure basic space,\nspheres, embodiments, and purified delusory appearance—\nintrinsic nature itself and essence itself—\nappear nondually, without joining or separating. [N-191](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-191)",
    "status": "No change; gate roles and modifier scope remain qualified",
    "reason": "The whole gate/object account keeps right/left and apprehended/apprehending roles, distinct pervading/entering ear functions and acoustic sounds. The nominal role treatment of bzung/’dzin at U04442–43 versus verbal holding is still a construction question, not settled by the glossary alone. Keep fivefold pairs without inventing a figure count; dag at U04457 may qualify only delusory appearance or the entire list. Vajra chains is supported by the visionary context. No posture or bodily procedure is added.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-192",
    "pairs": [
      "DTG-002175",
      "DTG-002176",
      "DTG-002177",
      "DTG-002178",
      "DTG-002179",
      "DTG-002180",
      "DTG-002181",
      "DTG-002186"
    ],
    "ids": [
      "U04463",
      "U04464",
      "U04465",
      "U04466",
      "U04467",
      "U04468",
      "U04469",
      "U04470",
      "U04471",
      "U04472",
      "U04473",
      "U04474",
      "U04475",
      "U04476",
      "U04477",
      "U04478",
      "U04479",
      "U04480",
      "U04481",
      "U04482",
      "U04483",
      "U04490",
      "U04491",
      "U04492",
      "U04493"
    ],
    "realization": "As for by what it is seen:\nit is seen through familiarity and the key points.; Familiarity starts with the preliminaries;\napplying the key points of body and voice,\none sees the forms of pure self-appearance,\nand all delusion subsides.; Through the body at the key point, seeing occurs.; Through the lion posture of the dharma embodiment,\nfree from all fear of delusion,\none sees with the vajra eye.; Through the posture of the complete enjoyment embodiment,\nrelying on the reclining elephant,\none fully enjoys the nature of phenomena\nand sees with the lotus eye.; Through the posture of the emanation embodiment,\nrelying on the crouching sage,\nthe nature of phenomena emanates of itself,\nand one sees with the dharma eye. [N-192](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-192); Furthermore, through channels and bodily exercises,\none sees the five primordial knowings of intrinsic nature's appearance\nwith the water-bubble eyes. [N-192](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-192); For the body: compressing, shaking out expressiveness,\nand the key points of striking, extending, and gathering the limbs;\nthrough subtlety, straightening, and massage—\nin flesh, blood, and bone. [N-192](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-192)",
    "status": "Key points corrected; posture and exercise proposals remain bounded",
    "reason": "Keep the actual lion, reclining elephant, crouching sage and four eye designations. Familiarity is an allowed goms state form, not a forbidden synonym for cultivation; the preliminaries attachment remains provisional. Bodily exercises for this ’khrul ’khor occurrence remains a local contextual proposal, not a global replacement for machinery of delusion. rtsal sprug and flesh/blood/bone attachment are unresolved complete constructions; do not guess physical techniques from components.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-193",
    "pairs": [
      "DTG-002188",
      "DTG-002189"
    ],
    "ids": [
      "U04495",
      "U04496",
      "U04497",
      "U04498",
      "U04499",
      "U04500",
      "U04501",
      "U04502",
      "U04503",
      "U04504",
      "U04505",
      "U04506",
      "U04507",
      "U04508"
    ],
    "realization": "Having thus arrived, the measures of completeness are:\ncessation of what appears directly before one;\nintroducing appearance into earth and stone;\none's own knowing entering anything;\nthrough that entry, moving matter;\ntaking the measure of wind's movement; [N-193](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-193)\nseeing the body's minute particles arises;\nwhatever appears is complete as form embodiment;\nthere, father and mother embrace;\nfivefold fathers and mothers join;\nall are within a round encircling band.; The yogin's body too is clear light;\ngoing, coming, and abiding—\nall are awareness reaching its measure. [N-194](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-194)",
    "status": "Matter adopted; complete sign list read",
    "reason": "The entire attainment-sign list through the next heading was read, not just its historical split. Matter preserves the bem po non-knowing side while explicitly allowing its stated movement. The possessive one’s own knowing at rang shes remains a permitted construction-level realization; entering objects does not by itself establish a reflexive self-cognition theory. Keep both the entering knowing and moving matter without conflating their agents. thad ka’i ngos snang and the five/five grouping remain provisional; the source’s stated signs are not empirically certified.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-194",
    "pairs": [
      "DTG-002188",
      "DTG-002191",
      "DTG-002193",
      "DTG-002194",
      "DTG-002195",
      "DTG-002197",
      "DTG-002199"
    ],
    "ids": [
      "U04495",
      "U04496",
      "U04497",
      "U04498",
      "U04499",
      "U04500",
      "U04501",
      "U04502",
      "U04503",
      "U04504",
      "U04505",
      "U04510",
      "U04511",
      "U04512",
      "U04515",
      "U04516",
      "U04517",
      "U04518",
      "U04519",
      "U04522",
      "U04525",
      "U04526"
    ],
    "realization": "Having thus arrived, the measures of completeness are:\ncessation of what appears directly before one;\nintroducing appearance into earth and stone;\none's own knowing entering anything;\nthrough that entry, moving matter;\ntaking the measure of wind's movement; [N-193](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-193)\nseeing the body's minute particles arises;\nwhatever appears is complete as form embodiment;\nthere, father and mother embrace;\nfivefold fathers and mothers join;\nall are within a round encircling band.; The manner of reaching the measure also becomes like this:\nfree from the particles of each body,\nwindows of light appear in the open sky.; The body's material weight self-ceases:\na stainless body of light with unimpeded penetration.; At its center is the sign of A,\nand rays from the brow curl measure one armspan.; The topknot appears held back by wind. [N-194](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-194); There is activity of ordinary mind without sound.; At this time one's body is brought to its measure:\nthe three embodiments, with unimpeded penetration, gathered into one. [N-194](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-194)",
    "status": "Open-sky label adopted; current variant handling preserved",
    "reason": "The already separated held-back/lifted source variant is not a current defect. Retain the A sign, armspan, hooked rays, father/mother imagery and the one-fold gathering without an iconographic rewrite. rdos pa material weight is distinct from bem po matter. The soundless ordinary-mind clause preserves acoustic silence as a qualified local reading, with wordless as the alternative if the intended nonverbal cognition sense is established. Window qualification and final gathering syntax remain provisional.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-195",
    "pairs": [
      "DTG-002201",
      "DTG-002209",
      "DTG-002210",
      "DTG-002211",
      "DTG-002212",
      "DTG-002213",
      "DTG-002215"
    ],
    "ids": [
      "U04528",
      "U04529",
      "U04530",
      "U04531",
      "U04540",
      "U04541",
      "U04542",
      "U04543",
      "U04544",
      "U04545",
      "U04546",
      "U04547",
      "U04548",
      "U04549",
      "U04550",
      "U04551",
      "U04552",
      "U04553",
      "U04555",
      "U04556"
    ],
    "realization": "At this time ordinary mind is clear;\nthrough the six higher knowings,\nphenomena that are far away or measurable\nare known in an instant.; At the times of such appearances,\nthe connection between body and ordinary mind is severed.; Even in the body whose contaminated [elements] are exhausted,\nordinary mind, characterized by clarity, emerges outward.; In the manner of a shooting star passing across,\nit is clearly seen in the element of space. [N-195](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-195); At the initial times of this,\neven in separation from wind,\nthrough effort and the activity of pure wind,\nit arises from being projected outside the body.; Through the two aspects of what sees,\nthe body is pure clear light;\nordinary mind is like proliferating sparks,\nnot abiding in one place, a Ground of its own clarity.; Through this, the connection between body and ordinary mind is severed,\nand one does not return to the three realms. [N-195](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-195)",
    "status": "No change; whole separation sequence read",
    "reason": "Read the sequence across U04540–56. Preserve all body/ordinary-mind terms, the shooting-star simile and both separation-from-wind and pure-wind predicates. The scope of [elements], two seeing aspects, and rang gsal gzhi remains provisional. dpag at U04530 may concern measurability or inferability; there is no printed med to justify an immeasurable emendation. Neither the knowledge claims nor bodily separation are independently certified.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-196",
    "pairs": [
      "DTG-002217",
      "DTG-002218",
      "DTG-002220",
      "DTG-002222",
      "DTG-002224",
      "DTG-002226",
      "DTG-002227"
    ],
    "ids": [
      "U04558",
      "U04559",
      "U04560",
      "U04561",
      "U04562",
      "U04565",
      "U04566",
      "U04567",
      "U04569",
      "U04570",
      "U04571",
      "U04572",
      "U04574",
      "U04575",
      "U04576",
      "U04579",
      "U04580",
      "U04581"
    ],
    "realization": "The nature of phenomena of cause and result:\nwhen the source of coarse conceptual thought has ceased,\nin the continuum of self-purified mindfulness,\ndependent connections and wind itself are completely pure.; It is the nature of phenomena arising from wind. [N-196](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-196); There are no embodiments or primordial knowing;\nhaving reached the limit where phenomena are exhausted,\nthis is held to be the nature of phenomena of the result. [N-196](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-196); The nature of phenomena that clears in its own place:\nwhen the elements clear, material weight is purified;\nparticles, subtle and coarse, cease at their limit,\nand not even a mere part abides.; Free from conceptual thought, clinging does not abide;\nneither dormancy nor manifest arising—\nnot even a particle's portion abides.; When the body of the four elements is exhausted,\nall is embodiment complete in primordial knowing.; Deep absorption free from conceptualization abides of itself.",
    "status": "No change; existing source qualification and distinct negatives retained",
    "reason": "G-U04562 already explicitly marks rlu as incomplete-looking; wind remains provisional, not a new Tibetan reading or glossary fuzzy-match license. No-embodiment/no-primordial-knowing at DTG-002220 and complete primordial-knowing embodiment at DTG-002226 are both written; do not harmonize them. rdos material weight differs from matter, dormancy differs from manifest arising, and canonical rtog med free from conceptualization differs from separately provisional rtog bral free from conceptual thought.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-197",
    "pairs": [
      "DTG-002230",
      "DTG-002231",
      "DTG-002232",
      "DTG-002234",
      "DTG-002235",
      "DTG-002236",
      "DTG-002237",
      "DTG-002239",
      "DTG-002240",
      "DTG-002241",
      "DTG-002242"
    ],
    "ids": [
      "U04585",
      "U04586",
      "U04587",
      "U04588",
      "U04589",
      "U04590",
      "U04591",
      "U04592",
      "U04593",
      "U04595",
      "U04596",
      "U04597",
      "U04598",
      "U04599",
      "U04600",
      "U04601",
      "U04602",
      "U04603",
      "U04604",
      "U04605",
      "U04606",
      "U04607",
      "U04609",
      "U04610",
      "U04611",
      "U04612",
      "U04613",
      "U04614",
      "U04615",
      "U04616",
      "U04617"
    ],
    "realization": "The definitive phrase ‘nature of phenomena’ is thus:\n‘phenomena’ means gathering and assembling,\ndoing doings and holding characteristics,\nshowing self-appearance\nand holding the respective classes.; ‘Nature’ means no contrivance;\nabiding in letting be, it genuinely pervades.; Fresh, genuine, and in its original course,\nthe number of words, phrases, and names is exhausted. [N-197](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-197); The nature of phenomena of the key points is as follows:\nthe elements' abodes, one's body,\nobjects, gates, knowing, wind,\nchannels, spheres, and subsidiary aspects—\neach respective entry abides pervasively.; Through transforming their respective preliminaries\nand the abiding of the main practice,\nin the nature of phenomena free from conceptual thought,\nintrinsic nature abides and movement is exhausted.; From the object in which exhaustion and appearance are nondual,\nthrough intrinsic nature’s abiding and contrived [practice],\nthe basic space of phenomena also appears through purity.; Through this, buddhahood comes through the key points. [N-197](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-197); The key point of the time of arising is like this:\nEma! I shall explain a great wonder.; This nature of phenomena has eight times of arising,\nand just as many times of abiding.; Also at four distinctive times,\nwhen the yogin's ordinary mind abides,\nthere is evenness without joining or separating.; Knowing the key point of pure intrinsic nature,\none knows phenomena without anything being done.",
    "status": "Approved components restored; wordplay and practice grouping retained",
    "reason": "Preserve separate chos/nyid explanations and the complete nature-of-phenomena phrase. Intrinsic nature is restored inside its abiding construction; this does not resolve the gnas la bsgyur attachment or contrived [practice] supply. gnyug ma genuine and dkyus ma original course remain local standalone-family proposals rather than deductions from the genuine-intrinsic-nature compound. Main practice is a complete dngos gzhi expression, not an entity/Ground composition. Retain eight arising/eight abiding/four distinctive times without inventing their members.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-198",
    "pairs": [
      "DTG-002246",
      "DTG-002249",
      "DTG-002255",
      "DTG-002258",
      "DTG-002259",
      "DTG-002260",
      "DTG-002261"
    ],
    "ids": [
      "U04623",
      "U04624",
      "U04629",
      "U04630",
      "U04642",
      "U04643",
      "U04644",
      "U04649",
      "U04650",
      "U04651",
      "U04652",
      "U04653",
      "U04654",
      "U04655",
      "U04656",
      "U04657",
      "U04658"
    ],
    "realization": "Distinguished, there are four aspects;\nhere I shall explain the intermediate state of the nature of phenomena.; A body of light endowed with all faculties\nbecomes like a shadow from the body. [N-198](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-198); Knowing how to spread and hold them,\none completes the buddhas' qualities\nand does not enter the three realms. [N-198](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-198); Five connected spheres are single embodiments;\nfrom half-embodiments, forms become complete.; From embodiments with half-forms, there are fivefold pairs.; As each cluster becomes complete,\nthere are groups of five, ten, and a hundred;\nclusters of a thousand and a hundred thousand\nappear pure in the intrinsic nature of what is envisaged. [N-198](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-198); Innumerable, beyond what expression can encompass—\nwhen one oneself knows their intrinsic nature,\none attains the three embodiments gathered into one.",
    "status": "No change; complete intermediate-state progression and conditioned scope read",
    "reason": "Retain the sequence, five-color order, half-form/pair progression and every cluster count. bsam ngo at U04655 remains what is envisaged provisionally; its relation to intrinsic nature is unresolved. At DTG-002261 rang shes is a verbal one oneself knows construction with intrinsic nature as object: preserve that permitted grammatical realization rather than inserting a self-awareness noun. The preceding knowing-how-to-spread/hold clause is conditional in context, not an unconditional guarantee. No external intermediate-state taxonomy is supplied.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-199",
    "pairs": [
      "DTG-002263",
      "DTG-002264",
      "DTG-002266",
      "DTG-002267",
      "DTG-002269",
      "DTG-002270",
      "DTG-002272"
    ],
    "ids": [
      "U04660",
      "U04661",
      "U04662",
      "U04665",
      "U04666",
      "U04667",
      "U04668",
      "U04669",
      "U04670",
      "U04671",
      "U04673",
      "U04674",
      "U04675",
      "U04676",
      "U04679",
      "U04680"
    ],
    "realization": "It comes from making this clear. [N-199](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-199); Furthermore, the essence of the nature of phenomena\nis established as essence from intrinsic nature itself.; Through identity, knowing, and seeing liberation,\nthrough entering, seeing, and familiarity—\nfrom recognition, there is one's own identity;\nthrough trust, one reaches it;\nthrough decision, one enters confidence.; Through these three certainties,\nessence being complete, the continuum ceases. [N-199](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-199); Not fixed as one thing of this kind,\nit appears however it is designated.; From the basis for assigning diverse names,\nit appears as elaborations of many words and phrases.; Since emptiness is not established as anything,\nits intrinsic nature appears pure. [N-199](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-199)",
    "status": "No change; corrected alignment checked and constructions retained",
    "reason": "The current U04661–4720 sequence aligns with the source: the historical shifted-alignment error is not re-reported. Preserve the ngo/shes/grol/mthong sequence, three certainties, and explicit continuum-ceases predicate. Making clear/reminder and identity/recognition grouping remain alternatives needing a parallel or commentary. Basis for assigning names is not automatically technical Ground; generic one thing does not attest dngos po.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-200",
    "pairs": [
      "DTG-002278",
      "DTG-002279",
      "DTG-002280",
      "DTG-002283",
      "DTG-002284",
      "DTG-002285",
      "DTG-002286",
      "DTG-002287",
      "DTG-002288"
    ],
    "ids": [
      "U04689",
      "U04690",
      "U04691",
      "U04692",
      "U04693",
      "U04694",
      "U04695",
      "U04696",
      "U04697",
      "U04698",
      "U04701",
      "U04702",
      "U04703",
      "U04704",
      "U04705",
      "U04706",
      "U04707",
      "U04708",
      "U04709",
      "U04710",
      "U04711",
      "U04712",
      "U04713"
    ],
    "realization": "In impure delusion,\nwithout contriving the gates of the faculties,\nthe key point is leaving [them] as they are;\nnot altering that is the pith instruction. [N-200](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-200); In appearance without an apprehended object,\nordinary mind arises without an apprehending subject.; It is seen by eyes without activity;\ndrawn along a path without a nature of phenomena;\ncarried to a Ground without view and cultivation;\ngathered into a result with nothing to do, free from effort.; Through naked seeing in vajra chains,\nthe mindfulness of moving differentiating conceptualization ceases.; Like going in space along the birds' path,\nthere is nowhere to go from the basic space of phenomena.; With no other, awareness-appearance being completely pure,\nthe causes and conditions of delusive appearance are exhausted.; Since basic space and awareness are inseparable,\nthe connected appearance of vajra chains is shown.; The essence of awareness is vajra chains:\nin past, future, or present,\nno one has made them.; Thus being unconditioned\nis the intrinsic nature of vajra chains.",
    "status": "Key points corrected; negative family and visionary scope retained",
    "reason": "Keep the entire negative path sequence, including without a nature of phenomena, and the explicit equation of awareness’s essence with vajra chains. cog ge bzhag preserves the approved leaving-as-it-is family with a locally plural object, not a new synonym. ’dus ma byas unconditioned remains an unapproved complete-expression proposal distinct from uncontrived or not done. The empty/odd source punctuation at U04703 is already qualified; no unsupported isolated line is inserted.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-201",
    "pairs": [
      "DTG-002290",
      "DTG-002292",
      "DTG-002294",
      "DTG-002297",
      "DTG-002298",
      "DTG-002301",
      "DTG-002303"
    ],
    "ids": [
      "U04716",
      "U04719",
      "U04721",
      "U04722",
      "U04723",
      "U04724",
      "U04725",
      "U04726",
      "U04729",
      "U04730",
      "U04733",
      "U04735",
      "U04736"
    ],
    "realization": "Furthermore, I shall explain the nature of phenomena of the continuum.; The lamp-light of self-aware primordial knowing blazes.; The view, free from fear, completes the lion's expressiveness;\nwith self-awareness ripened, completeness arises naturally;\nvajra chains connect, a garland of pearls;\nappearances of experience form an array of jeweled inlay;\nself-abiding emptiness is the mirror of the core;\ndeviations are cut of themselves: the mirror of awakened mind.; One in basic space, there are also six expanses.; With qualities complete, precious things are heaped.; Because awareness ripens, embodiment-relics blaze.; Thus, because the nature of phenomena is inexpressible,\nit arises as the foundation of conventional phrases.",
    "status": "Awakened-mind status reconciled; possible allusions remain provisional",
    "reason": "Awakened mind for thugs is adopted P2, superseding the note’s old proposed-status description, not a new translation change. Self-aware is an explicitly allowed adjectival form of rang rig; do not replace it with self-knowing. Keep the metaphors, six expanses, precious things, and full clauses instead of inventing a bibliographic list. sku gdung embodiment-relics and title identifications remain unapproved proposals; gzhi ma in the conventional-phrases construction remains provisional.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-202",
    "pairs": [
      "DTG-002307",
      "DTG-002312",
      "DTG-002315",
      "DTG-002316",
      "DTG-002317"
    ],
    "ids": [
      "U04741",
      "U04746",
      "U04749",
      "U04750",
      "U04751"
    ],
    "realization": "Liberated through the key points, striving and effort are exhausted.; Liberated through time, there is no need for familiarity.; Whose phenomena are realization and non-realization?; There, in saying ‘liberated,’ who is the object of focus? [N-202](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-202); For whom could entry into the three realms occur?",
    "status": "Key point and rhetorical-question repairs; taxonomic limits retained",
    "reason": "The final questions were read with the chapter ending, not left at the old batch boundary. DTG-002316 now has the one who-question actually present in su la dmigs, without the unsupported second what-question or a doctrinal answer. Familiarity remains the allowed goms state form; the time-based liberation relation is still unresolved. Preserve every distinct liberation description without assigning an unprinted taxonomy.",
    "review": "REVIEW.md#phase-d-notes-13"
  },
  {
    "session": "DTG-PD-20261005-Astra-05",
    "legacy_note": "N-203",
    "pairs": [
      "DTG-002317",
      "DTG-002318",
      "DTG-002319",
      "DTG-002320",
      "DTG-002321",
      "DTG-002322",
      "DTG-002323",
      "DTG-002324",
      "DTG-002325",
      "DTG-002326"
    ],
    "ids": [
      "U04751",
      "U04752",
      "U04753",
      "U04754",
      "U04755",
      "U04756",
      "U04757",
      "U04758",
      "U04759",
      "U04760",
      "U04761",
      "U04762",
      "U04763",
      "C4-TRANSITION"
    ],
    "realization": "For whom could entry into the three realms occur?; This is the nature of phenomena liberated from the limits of existence.; Furthermore, the nature of phenomena free from doing:\nwith no doing, there is liberation;\nwith no arising, there is no abiding.; With no going, coming and circling are exhausted.; There is neither one nor two of what is done or arisen.; There is not even mere conventional delusion.; It is empty of entry into activities of existence and nonexistence.; From the beginning, the result is free from the conceptual mind,\nbeyond all speaking, thinking, and expression.’ [N-203](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-203); Thus, from the Great All-Penetrating Word, Root of All Phenomena:\nthe fourth chapter, the Array of the Nature of Phenomena, teaching the root of ordinary mind's appearance.; [Unresolved source graphic at the Chapter 4/5 boundary; no transcription supplied.]",
    "status": "Quotation boundary repaired; final syntax and source limits retained",
    "reason": "Close the teacher’s quotation before the narrative colophon introduced by zhes. All final questions and negatives remain; yod med las kyi ’jug pas stong still admits alternative attachment of activities/existence/nonexistence. The title retains ordinary mind in sems snang, while colophon signs and the boundary graphic remain unresolved, not deciphered or added to root verse.",
    "review": "REVIEW.md#phase-d-notes-13"
  }
]
```

### Changed-clause self-check and actual tests

All 36 changed pairs were reread in full against their Tibetan and applicable complete glossary rows. The revised 237-pair English chapter was then read continuously through the colophon and boundary graphic, including the across-pair questions and quotation close. No further repair was required. The open-sky and intrinsic-nature repairs retain the original window/practice attachment questions. This verification is this reviewer’s self-check, not another independent review.

Actual checks pass: exact 506-operation replay from the frozen original English, 448 cumulatively changed pairs; fixed source/golden/policy/manifest/lineage bytes; all 2,667 IDs/order and English envelopes; unchanged inherited note associations and source-note footer; preserved original usage records and previous dispositions; 700 English local links. The paired suite was not rerun in this batch; the actual most recent Batch 12 result remains 64 tests, 53 pass, 9 fail, 2 error. Historical release-output gates remain blockers, not passed tests; full final validation is still due.

<!-- pd05-batch-13-verification -->

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

A bundled command was blocked before execution; the individual commands above were subsequently actually executed. The tests listed here are repository engineering tests, **not** execution of the standard's semantic regression specifications. At the freeze checkpoint no repair self-check had yet occurred. Subsequent batch results follow below.

**Batch 01 repair self-check (not a second independent review):** every changed clause was reread in its full Tibetan pair and necessary neighboring context. The source instruments, modifier head, speaker, numeric values, negation and relationships remain represented. In PD-S01 the passive adds no named agent; PD-S02 keeps the teacher as speaker and attaches quintessence to the text. The title and acoustic exceptions do not replace nonliterary continuum/word uses. The actual read-only integrity check passes: fixed source bytes, all 2,667 stable pair IDs/order, all 173 old note bodies and per-pair note associations. Exact replay of the 17 recorded scoped repairs reproduces every current pair payload; no unrecorded pair change is present. Current local-link check passes (684 targets). The released structural validator also passes with the current unchanged source and frozen English (5,484 golden objects); that is not release validation of revised English. Original ten usage records and legacy-index history reproduce after removing only the recorded dated additions. PD-N01 is applied in the current footer/index/usage layers. An initially bundled check/write/commit command was blocked before execution; the separate read-only check actually ran successfully. Existing signed build failures remain as reported above.

**Batch 02 repair self-check (same reviewer):** all 23 newly changed pairs and the corrected source-annotation sentence were reread against their complete Tibetan strings. Both members of the cyclic-existence/sorrow and sacred-pledge/vow contrasts remain; the aware/matter question preserves the knowing contrast without asserting that bodies are immaterial. The literary title/exposition context supports the scoped tantra occurrences, including the earlier question at DTG-000023; this resolves that Batch 01 question without generalizing all rgyud. The incomplete short Ema and other linked construction limits remain. No new agent, causal clause, numeral, negation or possession was introduced by the label repairs. The secret-preliminary and tenet-system constructions remain subject to the recorded later-reply comparison rather than an unqualified whole-work approval. Actual integrity replay passes all 42 recorded pair operations across 38 distinct pairs, the single note operation, unchanged fixed source and 2,667 IDs/order, unchanged per-pair old note associations, and all 685 current local-link targets. Historical annotation English remains visible alongside the current correction. Deferred legacy-status integration is explicitly listed in the batch disposition, not reported as already done.

**Batch 03 actual verification (continuation 02; repair self-check, not another independent review):** all revised clauses were reread against the exact Tibetan and full glossary rows, including necessary surrounding pairs. The complete revised English span DTG-000197–DTG-000297 was read continuously from the canonical file after application. Both key-point occurrences, the skilled agent/instrument, the beyond-six/below relationship, and the generic reflexive addressee remain source-supported. No numeral, negation, named agent, causal relation, or embodiment/knowing component was added or lost by these repairs. The unresolved constructions remain linked, not silently certified.

The actual read-only integrity check passes: replay of all **73 pair operations** (62 English repairs plus 11 review links) exactly reproduces every current pair payload from frozen main; **57 English-repair pairs / 65 changed pairs including note-only changes**. Fixed Tibetan bytes and golden hash, all **2,667** shared IDs/order/envelopes, all inherited per-pair note associations, **694** current English local link targets, and adopted policy hashes pass. Original usage records and the first six Phase D dispositions are unchanged; exactly five dated dispositions were appended. Removing only the five dated additions reproduces the prior legacy index byte-for-byte. `git diff --check` passes. Canonical English SHA-256: `ef0aecded418e6ef1e2dfdb03a9f53bfe45444cb6c185608be431d3962087c5b`. One attempted custom display command was blocked before execution; the successful canonical-file read and subsequent integrity checks, not that blocked attempt, support these results. No semantic regression fixture is claimed executed by this check.

### Canonical and generated layers

`paired/translation.md` is the sole current authored English. The dated September draft and October 1 readers/JSON are historical release outputs, not separately edited current translations. `paired/MANIFEST.json` and `paired/v2/PAIR-AUDIT.json` describe the released paired import. Existing builders require exact released English and old policy inputs; rerunning them cannot silently become a post-review build. Their signed contracts, receipts and tags will not be rewritten to make revised working English appear historically signed off. Applicable builds will still be attempted and actual failures reported. Any bounded working-output integration left unsupported by the existing process will be distinguished from semantic coverage.

## Coverage versus text disposition

**Current coverage:** 2333/2,667 semantic pairs reviewed, ordinals 1–2333 through DTG-002326; 334 remain unreviewed. **453 first-encountered note records** read cumulatively. **Applied changes:** 485 English operations, 21 earlier review-link operations; **448 changed pairs including note-only changes**. The previously recorded 3 source-annotation and 2 active Current English quote repairs remain preserved. Repair verification is self-check, not another independent review. **Text disposition:** reviewed portions retain linked unresolved questions; no text acceptance, human certification, formal release or cross-work harmonization is claimed. Existing released readers remain historical; their builders reject the changed policy/English, and no successful regeneration is claimed.

## Continuation

Continue at **ordinal 2334, DTG-002327**, after Batch 13. Exact unreviewed ranges: chapter-05 **2334–2544**, chapter-06 **2545–2652**, closing-material **2653–2667**. Preserve fixed source bytes, all IDs/order/source roles/formats, annotations, historical approvals/readers/releases and other worktrees. Context beyond this checkpoint is not advance coverage.

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
