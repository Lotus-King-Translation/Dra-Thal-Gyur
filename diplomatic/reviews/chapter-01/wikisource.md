# Chapter 1: Wikisource comparison and uncertainty report

## Scope and evidence

Compared all opening material and Chapter 1 in `source/W1KG11703_7.txt`, stable source units **U00001–U02635**, against `editions/adzom-wikisource/source.wikitext` **lines 1–2664**. The website chapter marker `@2` is line 2665; no Chapter 2 or later text was collated. The Chapter 1 closing formula is line 2664, website page marker **102**. These website page markers are locators within the transcription, not independently verified facsimile page identities.

Input commit: `e17a496ad7532cc627f9ba288b541f7a53efd002`. Concatenating the Tibetan of all source units exactly reproduces the source TXT, 157,288 Unicode characters. Chapter 1 occupies characters `[0, 76376)`.

Wikisource provenance: revision **439571**, timestamp **2015-09-09T14:02:11Z**, [revision URL](https://wikisource.org/w/index.php?oldid=439571); [contributor history](https://wikisource.org/w/index.php?title=Sgra%20thal%20%E2%80%99gyur%20%28A-%27dzom%20blocks%29&action=history). Its declared role is a searchable Wylie reference associated with Adzom blocks, **not a newly independent witness or verified diplomatic transcription**. Both repository wikitext copies have identical bytes. Reuse must retain attribution and applicable [Wikimedia terms](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use), including applicable share-alike requirements.

`source/README.md` says the Adzom printed scan governs readings and the cleaned e-text has not been proofread diplomatically. This report collates the two digital transcriptions; it does not settle printed readings. No facsimile was inspected for this report.

## Method and limits

The source-unit EWTS was compared to the exact website Wylie text, excluding numeric page labels, `@1`, poem wrappers and two bracketed website editorial annotations. For line alignment only, `/`, `_`, `*`, `#`, and `@` signs were removed and whitespace collapsed. All source Tibetan, exact EWTS, exact website lines, source offsets, and web line/page locators remain in the JSON and full apparatus below. The `*` represents the source nonbreaking tsek `༌` in these occurrences; its suppression is an alignment operation, not an editorial deletion. The website omits source-style shad punctuation throughout its verse-line presentation. This is a systematic presentation difference, not evidence that the print has no punctuation.

Line alignment uses Python `difflib.SequenceMatcher` with `autojunk=False`. Contiguous unequal line blocks are recorded exhaustively. A separate token comparison in each JSON conflict identifies changed Wylie spans. Some blocks mix several phenomena (for example a source heading and a word variant); the category is a finding aid, not a claim that everything in the block has one cause.

Diagnostic pyewts conversions of all 2,558 web root-text lines are preserved in `wikisource-ch1-raw-ledger.json`, with conversion warnings at lines 933, 1020. The Unicode output is diagnostic only, not an adopted reading or a claim about exact printed Tibetan. “Romanization or spacing difference” is a candidate category based on lowercasing, plus-sign spacing and selected apostrophe joining, not proof of the printed Tibetan form. Sanskrit orthography and vowel quantity remain unresolved when the web transcription underspecifies them.

No translation was made or altered; no glossary term was proposed. Relevant repository source-authority and annotation rules were applied.

## Coverage counts

| Measure | Count |
| --- | ---: |
| source_units_total | 2635 |
| source_units_with_lexical_content | 2633 |
| wikisource_root_text_lines | 2558 |
| exact_normalized_equal_lines | 2333 |
| conflict_blocks | 273 |
| source_units_containing_asterisk | 177 |
| source_only_sign_units | 2 |
| website_editorial_annotation_lines | 2 |
| source_text_absent_in_web_transcription | 7 |
| textual_difference | 173 |
| source_heading_or_label_absent_in_web_transcription | 71 |
| romanization_or_spacing_difference | 18 |
| web_text_absent_in_source_units | 4 |

Counts describe the mechanical comparison under the stated normalization. They do not certify print accuracy or independence of witnesses.

## Priority uncertainty flags

1. **Source inline apparatus is flattened into the e-text.** For example U00180 places `sdud pa po zhu ba rang byung gi bkod pa` inside the verse `de nas gcig dang tha mi … dad`; U00192 begins with a long apparent note before the question; U00328 has `spel yang byung`; U00596 has `glu yang gdung yang byung`. Wikisource omits these intrusions. Their placement in the print must determine separation into root text and annotation; the website’s shorter verse is evidence for investigation, not independent authority to excise them.

2. **Possible missing root lines:** Wikisource has the following unmatched runs; facsimile examination must decide whether they fill e-text omissions or reflect another transcription state.

| Between source units | Web lines | Web page marker | Exact Wylie |
| --- | --- | --- | --- |
| U01274 / U01275 | 1296–1298 | 51 | `chu yi zug pas dbang po sdud` / `byer ba yis ni 'khrugs par byed` / `snyoms pa yis ni 'bras bu 'byin` |
| U01882 / U01883 | 1908–1910 | 74 | `so so'i tshad la rtags kyis 'grub` / `'di ltar su yi 'grub pa la` / `sprul pa'i sku dang longs sku dang` |
| U02005 / U02006 | 2034–2036 | 78 | `gzhi ni 'jig rten pa yin te` / `'di las 'dod pa gnyis yin no` / `'das pa rgyu dang 'bras bu las` |
| U02187 / U02188 | 2221–2222 | 85 | `'du shes can dag mtha' la 'jog` / `mngon sum gnad kyi man ngag gis` |
| Before U02309, within replacement block W-C01-232 | 2344–2345 | 90 | `rdo rje gsang ba'i gnas gzung bya'o` / `yang ni lha dbang dga' byed nyon` |

3. **Explicit e-text missing-text notices:** U01144 `tshig chad song /`; U01286 `chu'i byer snyoms gnyis chad/`. Do not reproduce these as unmarked root-text verses. The water-element web addition at lines 1296–1298 is relevant to the latter, but the exact relationship needs scan verification.

4. **Opening differences:** The web omits source U00002 and the Sanskrit title U00006; U00005 also contains prefatory characters absent from the web. Its omission of Sanskrit is not a reason to remove material from the diplomatic edition. U00001 and U00003 are source ornamental signs without lexical web counterparts.

5. **Website editorial citations at U01529–U01530:** Source U01529 has `sems ni thog ma byung ba dang`; web line 1554 has `sems ni thog ma byung sa dang`. Source U01530 has `bar du gnas pa tha mar 'gro`; web line 1556 has `bar du gnas pa tha ma 'gro`. The two bracketed notes below cite other works, but these are unverified claims by the website editor. They cannot be counted as another directly collated witness or imported into root text.

**Web line 1555, page marker 60:**

[var. ''mTshams brag rnying rgyud'', vol. Na, p. 50 (l. 3) : ''sems ni thog ma byung '''ba''' dang'' ; but Klong chen pa and the ''dGongs pa zang thal'' both always have ''byung '''sa''''', at least in the A ’dzom ’brug pa prints]

**Web line 1557, page marker 60:**

[var. Klong chen rab ’byams, many occurrences of this quotation, in the form : ''bar du gnas dang tha ma ’gro'', as well as in the ''Bi ma'i ’grel tig'' of the ''dGongs pa zang thal'', vol. IV, p. 338]

## Recommended editorial treatment

The golden edition should use one chosen printed witness as its diplomatic base, preserve its readings including difficult or apparently wrong forms, and document every verified departure. Until a print reading is checked, record the present base e-text and website alternatives as **unresolved transcription differences**. Do not choose the web form merely because it reads more fluently, and do not label two Adzom transcriptions as two independent votes. Where source strings are printed marginal or interlinear notes, preserve their wording in the apparatus with print location while removing their accidental insertion into the root-text sentence only after the layout is verified.

The complete apparatus below records the pre-scan digital comparison. Its dispositions remain provisional because this comparison did not inspect the governing scan. Subsequent scan-attested intervention notes in the chapter reading text supersede these provisional dispositions, including where they restore text absent from A. This report does not reject or undo such restorations. Exact supplied readings remain preserved as comparative evidence; no source or edition input was changed.

## Complete lexical difference apparatus

`∅` means no counterpart in this normalized alignment, not proof of omission in the printed book. Exact source Tibetan/EWTS is supplied with each source unit. Web locators identify repository file lines and website page markers.

### W-C01-001

Category: `source_text_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00002**, characters [2, 37): རཏྞཱཀཱརཤབྡམཧཱཔྲསཾགཏནྟྲནཱམབིཧརཏིསྨ།།
  - Exact EWTS: `rat+NAkArashab+damahAprasaMgatan+t+ranAmabiharatisma//`
- Web: ∅ between lines None and 4.

**Provisional comparison disposition and reason:** Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.

### W-C01-002

Category: `textual_difference`. Alignment: `replace`.

- Source **U00005**, characters [110, 134): གཾགརྦམཏགཱ རྒྱ་གར་སྐད་དུ།
  - Exact EWTS: `gaMgarbamatagA_rgya gar skad du/`
- Source **U00006**, characters [134, 170):  རཏྣ་ཀ་ར་ཤབྡ་མ་ཧཱ་པྲ་སཾ་ག་ཏནྟྲ་ནཱ་མ།
  - Exact EWTS: `_rat+na ka ra shab+da ma hA pra saM ga tan+t+ra nA ma/`
- Web line **6**, page marker **2**: `rgya gar skad du`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-003

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00011**, characters [324, 358): ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞི་བཀོད་པ།
  - Exact EWTS: `thun mong ma yin pa'i gleng gzhi bkod pa/`
- Web: ∅ between lines 10 and 11.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-004

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00029**, characters [861, 888): ཐུན་མོང་གི་གླེང་གཞི་བཀོད་པ།
  - Exact EWTS: `thun mong gi gleng gzhi bkod pa/`
- Web: ∅ between lines 29 and 30.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-005

Category: `textual_difference`. Alignment: `replace`.

- Source **U00038**, characters [1121, 1154): པདྨའི་ཟེའུ་འབྲུ་རྫོགས་པའི་གྲངས། །
  - Exact EWTS: `pad+ma'i ze'u 'bru rdzogs pa'i grangs/_/`
- Source **U00039**, characters [1154, 1183): སྟོད་དང་ལྡན་པ་དབུས་མའི་གནས། །
  - Exact EWTS: `stod dang ldan pa dbus ma'i gnas/_/`
- Web line **38**, page marker **4**: `pad ma'i ze'u 'bru rdzogs pa'i grangs`
- Web line **39**, page marker **4**: `stong dang ldan pa dbus ma'i gnas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-006

Category: `textual_difference`. Alignment: `replace`.

- Source **U00067**, characters [1966, 1993): མཛེས་ཞིང་ལྡེམ་བག་ལྡན་པ་ལ། །
  - Exact EWTS: `mdzes zhing ldem bag ldan pa la/_/`
- Web line **68**, page marker **5**: `mdzes shing ldem bag ldan pa la`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-007

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00073**, characters [2138, 2164): ཁྱད་པར་སྙིང་པོའི་པདྨ་ལས། །
  - Exact EWTS: `khyad par snying po'i pad+ma las/_/`
- Web line **74**, page marker **5**: `khyad par snying po'i pad ma las`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-008

Category: `textual_difference`. Alignment: `replace`.

- Source **U00079**, characters [2314, 2340): ང་ནི་ལྷ་བུ་དགའ་བྱེད་སྟེ། །
  - Exact EWTS: `nga ni lha bu dga' byed ste/_/`
- Web line **81**, page marker **6**: `nga ni lta bu dga' byed ste`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-009

Category: `textual_difference`. Alignment: `replace`.

- Source **U00082**, characters [2405, 2434): རང་བཞིན་གྱིས་ནི་བདེ་བ་རྙེད། །
  - Exact EWTS: `rang bzhin gyis ni bde ba rnyed/_/`
- Web line **84**, page marker **6**: `rang bzhin gyis ni bde bas rnyed`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-010

Category: `textual_difference`. Alignment: `replace`.

- Source **U00137**, characters [4021, 4052): དུས་གསུམ་འབྱུང་བས་གསུང་བ་མེད། །
  - Exact EWTS: `dus gsum 'byung bas gsung ba med/_/`
- Source **U00138**, characters [4052, 4081): སྒྲ་ཚིག་མིང་ལ་ངེས་བསྡུས་པས། །
  - Exact EWTS: `sgra tshig ming la nges bsdus pas/_/`
- Web line **141**, page marker **8**: `dus gsum 'byung bas gsung pa med`
- Web line **142**, page marker **8**: `sgra tshig ming la res bsdus pas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-011

Category: `textual_difference`. Alignment: `replace`.

- Source **U00145**, characters [4264, 4297): ངེས་པའི་རྗོད་བྱེད་བརྒྱ་དང་གསུམ། །
  - Exact EWTS: `nges pa'i rjod byed brgya dang gsum/_/`
- Web line **149**, page marker **8**: `nges pa'i brjod byed brgya dang gsum`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-012

Category: `textual_difference`. Alignment: `replace`.

- Source **U00180**, characters [5304, 5361): དེ་ནས་གཅིག་དང་ཐ་མི་སྡུད་པ་པོ་ཞུ་བ་རང་བྱུང་གི་བཀོད་པ་དད། །
  - Exact EWTS: `de nas gcig dang tha mi sdud pa po zhu ba rang byung gi bkod pa dad/_/`
- Web line **186**, page marker **10**: `de nas gcig dang tha mi dad`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-013

Category: `textual_difference`. Alignment: `replace`.

- Source **U00187**, characters [5529, 5575): འབྱུང་བཞིའི་དགོངས་དགོས་པ་ཡང་བྱུང་པ་ཇི་ལྟ་བུ། །
  - Exact EWTS: `'byung bzhi'i dgongs dgos pa yang byung pa ji lta bu/_/`
- Web line **193**, page marker **10**: `'byung bzhi'i dgongs pa ji lta bu`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-014

Category: `textual_difference`. Alignment: `replace`.

- Source **U00192**, characters [5683, 5806): འདི་མཚམས་འོག་གི་རང་དང་གཞན་གྱི་དམ་བཅའི་ཞེས་པ་དང་འཕེན་པ་རླུང་སྟེ་ཞེས་པ་གཉིས་ཀྱི་དྲི་བ་མ་བྱུང་འགྱུར་དང་འགྱུར་བྱེད་གང་དང་གང་། །
  - Exact EWTS: `'di mtshams 'og gi rang dang gzhan gyi dam bca'i zhes pa dang 'phen pa rlung ste zhes pa gnyis kyi dri ba ma byung 'gyur dang 'gyur byed gang dang gang /_/`
- Web line **198**, page marker **10**: `'gyur dang 'gyur byed gang dang gang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-015

Category: `textual_difference`. Alignment: `replace`.

- Source **U00197**, characters [5913, 5945): འཇིག་པའི་རྒྱུ་ནི་ཅི་ལས་འབྱུང་། །
  - Exact EWTS: `'jig pa'i rgyu ni ci las 'byung /_/`
- Web line **203**, page marker **10**: `'jigs pa'i rgyu ni ci las 'byung`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-016

Category: `textual_difference`. Alignment: `replace`.

- Source **U00239**, characters [7138, 7164): དབང་བསྐུར་བ་ཡི་ཆོ་ག་གང༌། །
  - Exact EWTS: `dbang bskur ba yi cho ga gang*/_/`
- Web line **247**, page marker **12**: `dbang bskur pa yi cho ga gang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-017

Category: `textual_difference`. Alignment: `replace`.

- Source **U00248**, characters [7394, 7421): བལྟ་བ་མཐའ་ལ་གང་གིས་བསྐྱལ། །
  - Exact EWTS: `blta ba mtha' la gang gis bskyal/_/`
- Web line **256**, page marker **12**: `lta ba mtha' la gang gis bskyal`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-018

Category: `textual_difference`. Alignment: `replace`.

- Source **U00250**, characters [7452, 7481): སྤྱོད་པའི་སྦྱོར་བ་ཇི་ལྟ་བུ། །
  - Exact EWTS: `spyod pa'i sbyor ba ji lta bu/_/`
- Web line **258**, page marker **12**: `spyod pa'i sbyor pa ji lta bu`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-019

Category: `textual_difference`. Alignment: `replace`.

- Source **U00272**, characters [8076, 8142): དེ་ནས་རྒྱུད་ཀྱི་ཆེ་བ་རྣམ་པར་བཀོད་པའི་བཀོད་པ་ཁྱབ་བདག་སེམས་དཔའ་ནི། །
  - Exact EWTS: `de nas rgyud kyi che ba rnam par bkod pa'i bkod pa khyab bdag sems dpa' ni/_/`
- Web line **281**, page marker **13**: `de nas khyab bdag sems dpa' ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-020

Category: `textual_difference`. Alignment: `replace`.

- Source **U00281**, characters [8371, 8398): ཨིནྡྲ་ལྷ་ཡི་དབང་ཕྱུག་ཉོན། །
  - Exact EWTS: `in+d+ra lha yi dbang phyug nyon/_/`
- Web line **291**, page marker **14**: `in dra lha yi dbang phyug nyon`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-021

Category: `textual_difference`. Alignment: `replace`.

- Source **U00306**, characters [9104, 9134): ཐེ་ཚོམ་མེད་པར་འབྲས་བུ་འབྱིན། །
  - Exact EWTS: `the tshom med par 'bras bu 'byin/_/`
- Web line **317**, page marker **15**: `the tshom med par 'bras bu 'phyin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-022

Category: `textual_difference`. Alignment: `replace`.

- Source **U00309**, characters [9194, 9225): དྲིས་པའི་ཚིག་རྣམས་གསལ་ཕྱེ་བས། །
  - Exact EWTS: `dris pa'i tshig rnams gsal phye bas/_/`
- Web line **320**, page marker **15**: `dris pa'i tshig rnams gsal phye pas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-023

Category: `source_text_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00317**, characters [9424, 9462): དྲི་བ་བདུན་ཅུ་ཟེར་ཀྱང་དོན་དྲུག་པར་ཡོད།
  - Exact EWTS: `dri ba bdun cu zer kyang don drug par yod/`
- Source **U00318**, characters [9462, 9477):  དྲིས་ལན་དང་པོ།
  - Exact EWTS: `_dris lan dang po/`
- Web: ∅ between lines 327 and 328.

**Provisional comparison disposition and reason:** Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.

### W-C01-024

Category: `textual_difference`. Alignment: `replace`.

- Source **U00320**, characters [9508, 9534): ཆུ་ནི་དྭངས་མ་སྡུད་པ་དང་། །
  - Exact EWTS: `chu ni dwangs ma sdud pa dang /_/`
- Source **U00321**, characters [9534, 9565): སྙིགས་མ་རྣམས་ནི་འབྱེད་པའི་ལས། །
  - Exact EWTS: `snyigs ma rnams ni 'byed pa'i las/_/`
- Web line **329**, page marker **15**: `chu ni dangs ma sdud pa dang`
- Web line **330**, page marker **15**: `snyigs ma rnams ni 'byed pa'i sa`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-025

Category: `textual_difference`. Alignment: `replace`.

- Source **U00328**, characters [9734, 9774): མེས་ནི་འབྱུང་བ་སེལ་བ་སྤེལ་ཡང་བྱུང་དང་། །
  - Exact EWTS: `mes ni 'byung ba sel ba spel yang byung dang /_/`
- Web line **337**, page marker **15**: `mes ni 'byung ba sel ba dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-026

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00344**, characters [10232, 10247): དྲིས་ལན་གཉིས་པ།
  - Exact EWTS: `dris lan gnyis pa/`
- Web: ∅ between lines 353 and 354.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-027

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00373**, characters [11049, 11068): དྲིས་ལན་གསུམ་པའོ། །
  - Exact EWTS: `dris lan gsum pa'o/_/`
- Web: ∅ between lines 382 and 383.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-028

Category: `textual_difference`. Alignment: `replace`.

- Source **U00383**, characters [11325, 11355): དམིགས་པས་ཡུལ་གྱི་བློ་རྣམས་ལ། །
  - Exact EWTS: `dmigs pas yul gyi blo rnams la/_/`
- Web line **392**, page marker **17**: `dmigs pas yul kyi blo rnams la`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-029

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00394**, characters [11643, 11657): དྲིས་ལན་བཞི་པ།
  - Exact EWTS: `dris lan bzhi pa/`
- Web: ∅ between lines 403 and 404.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-030

Category: `textual_difference`. Alignment: `replace`.

- Source **U00458**, characters [13447, 13470): སྐལ་བ་ཅན་གྱི་སྣང་བ་ལ། །
  - Exact EWTS: `skal ba can gyi snang ba la/_/`
- Web line **469**, page marker **20**: `skal pa can gyi snang ba la`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-031

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00492**, characters [14454, 14467): དྲིས་ལན་ལྔ་པ།
  - Exact EWTS: `dris lan lnga pa/`
- Web: ∅ between lines 504 and 505.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-032

Category: `textual_difference`. Alignment: `replace`.

- Source **U00502**, characters [14735, 14762): གྲུབ་ཚུལ་དང་ནི་དྲང་ཚད་དོ། །
  - Exact EWTS: `grub tshul dang ni drang tshad do/_/`
- Web line **514**, page marker **22**: `grub tshul dang ni grangs tshad do`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-033

Category: `textual_difference`. Alignment: `replace`.

- Source **U00510**, characters [14968, 15000): ཆུ་ཞེང་ཉམས་དགའ་བཀོད་ལེགས་སྤྲས། །
  - Exact EWTS: `chu zheng nyams dga' bkod legs spras/_/`
- Web line **522**, page marker **22**: `chu zhing nyams dga' bkod legs spras`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-034

Category: `textual_difference`. Alignment: `replace`.

- Source **U00518**, characters [15196, 15222): མརྒད་དག་གིས་ཡོངས་སྤྲས་པ། །
  - Exact EWTS: `margad dag gis yongs spras pa/_/`
- Web line **531**, page marker **23**: `ma rgad ngag gis yongs spras pa`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-035

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00524**, characters [15366, 15394): པདྨ་རྒྱས་པའི་དབྱིབས་འདྲ་བ། །
  - Exact EWTS: `pad+ma rgyas pa'i dbyibs 'dra ba/_/`
- Web line **537**, page marker **23**: `pad ma rgyas pa'i dbyibs 'dra ba`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-036

Category: `textual_difference`. Alignment: `replace`.

- Source **U00534**, characters [15654, 15700): ལྗོངས་བདེ་ཡང་བྱུང་རབ་ཏུ་རྫོགས་ཏེ་ཉམས་དགའ་བར། །
  - Exact EWTS: `ljongs bde yang byung rab tu rdzogs te nyams dga' bar/_/`
- Web line **547**, page marker **23**: `rab tu rdzogs te nyams dga' bar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-037

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00538**, characters [15791, 15818): ཐོད་པའི་ཕྲེང་བ་བཀོད་པ་འོ། །
  - Exact EWTS: `thod pa'i phreng ba bkod pa 'o/_/`
- Web line **551**, page marker **23**: `thod pa'i phreng ba bkod pa'o`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-038

Category: `textual_difference`. Alignment: `replace`.

- Source **U00542**, characters [15911, 15940): བཀོད་པ་ལྔ་ཡིས་ཡོངས་སུ་སྨྲས། །
  - Exact EWTS: `bkod pa lnga yis yongs su smras/_/`
- Web line **555**, page marker **23**: `bkod pa lnga yis yongs su spras`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-039

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00573**, characters [16840, 16870): ལྡ་ལྡི་པདྨའི་སྤྱན་གྱིས་མཛེས། །
  - Exact EWTS: `lda ldi pad+ma'i spyan gyis mdzes/_/`
- Web line **588**, page marker **25**: `lda ldi pad ma'i spyan gyis mdzes`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-040

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00578**, characters [16984, 17011): འོད་ཀྱིས་ཁེངས་ཤིང་ཙནྡན་དྲི།
  - Exact EWTS: `'od kyis khengs shing tsan+dan dri/`
- Web line **593**, page marker **25**: `'od kyis khengs shing tsan dan dri`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-041

Category: `textual_difference`. Alignment: `replace`.

- Source **U00581**, characters [17071, 17102): རབ་ཏུ་གཞོན་པ་རྣམས་ཀྱིས་བསྐོར། །
  - Exact EWTS: `rab tu gzhon pa rnams kyis bskor/_/`
- Web line **596**, page marker **25**: `rab tu bzhon pa rnams kyis bskor`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-042

Category: `textual_difference`. Alignment: `replace`.

- Source **U00584**, characters [17155, 17186): དད་ཅིང་བསུང་བའི་དྲི་ཡིས་མྱོས། །
  - Exact EWTS: `dad cing bsung ba'i dri yis myos/_/`
- Web line **599**, page marker **25**: `dad cing bsung pa'i dri yis myos`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-043

Category: `textual_difference`. Alignment: `replace`.

- Source **U00596**, characters [17521, 17573): འོད་འབྱུང་ཕྲེང་བ་ཀླུ་ཡི་གླུ་ཡང་གདུང་ཡང་བྱུང་གདོང་། །
  - Exact EWTS: `'od 'byung phreng ba klu yi glu yang gdung yang byung gdong /_/`
- Web line **612**, page marker **26**: `'od 'byung phreng ba klu yi gdong`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-044

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00598**, characters [17601, 17616): དྲིས་ལན་དྲུག་པ།
  - Exact EWTS: `dris lan drug pa/`
- Web: ∅ between lines 613 and 614.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-045

Category: `textual_difference`. Alignment: `replace`.

- Source **U00603**, characters [17724, 17757): སྐྱོན་བསལ་བསྒྲུབ་དང་འགལ་བ་སྤང་། །
  - Exact EWTS: `skyon bsal bsgrub dang 'gal ba spang /_/`
- Web line **618**, page marker **26**: `skyon bsal bsgrub dang 'gal pa spang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-046

Category: `textual_difference`. Alignment: `replace`.

- Source **U00612**, characters [18005, 18038): མཁས་པས་མཚན་ཉིད་རྫོགས་ཀྱིས་སྦྱར། །
  - Exact EWTS: `mkhas pas mtshan nyid rdzogs kyis sbyar/_/`
- Web line **627**, page marker **26**: `mkhas pas mtshan nyid rdzogs gis sbyar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-047

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00624**, characters [18380, 18395): དྲིས་ལན་བདུན་པ།
  - Exact EWTS: `dris lan bdun pa/`
- Web: ∅ between lines 639 and 640.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-048

Category: `textual_difference`. Alignment: `replace`.

- Source **U00626**, characters [18424, 18459): ཚིག་དང་ཟུར་ལ་གཞོན་གཞོག་ཀྱང་པ་དང༌། །
  - Exact EWTS: `tshig dang zur la gzhon gzhog kyang pa dang*/_/`
- Web line **641**, page marker **27**: `tshig dang zur la gzhon pa dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-049

Category: `textual_difference`. Alignment: `replace`.

- Source **U00632**, characters [18613, 18642): མ་དག་པ་ཡིས་ནི་ཡང་ཡེ་ཤེས་སོ། །
  - Exact EWTS: `ma dag pa yis ni yang ye shes so/_/`
- Web line **647**, page marker **27**: `ma dag pa yis ye shes so`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-050

Category: `textual_difference`. Alignment: `replace`.

- Source **U00635**, characters [18709, 18740): དཔེ་ཡིས་ མཚོན་ཏེ་སྦྱོར་བ་གཅིག །
  - Exact EWTS: `dpe yis _mtshon te sbyor ba gcig_/`
- Web line **650**, page marker **27**: `de yis mtshon te sbyor ba gcig`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-051

Category: `textual_difference`. Alignment: `replace`.

- Source **U00651**, characters [19178, 19219): བྱས་ཀྱང་འདུག་གནས་དང་བྱུང་དང་བྱེད་པ་དང་། །
  - Exact EWTS: `byas kyang 'dug gnas dang byung dang byed pa dang /_/`
- Web line **667**, page marker **28**: `gnas dang byung dang byed pa dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-052

Category: `textual_difference`. Alignment: `replace`.

- Source **U00653**, characters [19248, 19282): བསྒྲུབས་པ་རྣམས་དང་སྒྲུབ་པར་བྱེད། །
  - Exact EWTS: `bsgrubs pa rnams dang sgrub par byed/_/`
- Web line **669**, page marker **28**: `bskubs pa rnams dang sgrub par byed`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-053

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00655**, characters [19311, 19327): དྲིས་ལན་བརྒྱད་པ།
  - Exact EWTS: `dris lan brgyad pa/`
- Web: ∅ between lines 670 and 671.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-054

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00676**, characters [19930, 19944): དྲིས་ལན་དགུ་པ།
  - Exact EWTS: `dris lan dgu pa/`
- Web: ∅ between lines 691 and 692.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-055

Category: `textual_difference`. Alignment: `replace`.

- Source **U00684**, characters [20153, 20187): བཀའ་གསང་འབྱུང་ངེས་འགྱུར་ཚད་སྟོན། །
  - Exact EWTS: `bka' gsang 'byung nges 'gyur tshad ston/_/`
- Web line **699**, page marker **29**: `bka' gsang 'byung bas 'gyur tshad ston`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-056

Category: `textual_difference`. Alignment: `replace`.

- Source **U00696**, characters [20502, 20535): དཔལ་གྱི་དགོངས་པ་འབྱུང་བའི་གཏེར། །
  - Exact EWTS: `dpal gyi dgongs pa 'byung ba'i gter/_/`
- Web line **711**, page marker **29**: `dbal gyi dgongs pa 'byung ba'i gter`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-057

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00701**, characters [20653, 20667): དྲིས་ལན་བཅུ་པ།
  - Exact EWTS: `dris lan bcu pa/`
- Web: ∅ between lines 716 and 717.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-058

Category: `textual_difference`. Alignment: `replace`.

- Source **U00710**, characters [20890, 20940): སོ་སོའི་ནུས་པས་བུས་པ་སྦྱར་ཡང་འབྱུང་བསྒྱུར་བ་གང་། །
  - Exact EWTS: `so so'i nus pas bus pa sbyar yang 'byung bsgyur ba gang /_/`
- Web line **725**, page marker **30**: `so so'i nus pas bsgyur ba gang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-059

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00721**, characters [21237, 21256): དྲིས་ལན་བཅུ་གཅིག་པ།
  - Exact EWTS: `dris lan bcu gcig pa/`
- Web: ∅ between lines 735 and 736.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-060

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00756**, characters [22225, 22244): དྲིས་ལན་བཅུ་གཉིས་པ།
  - Exact EWTS: `dris lan bcu gnyis pa/`
- Web: ∅ between lines 771 and 772.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-061

Category: `textual_difference`. Alignment: `replace`.

- Source **U00777**, characters [22806, 22835): དེ་ནས་ལྷོ་ཕྱོགས་ཚལ་བ་སྐྱོབ། །
  - Exact EWTS: `de nas lho phyogs tshal ba skyob/_/`
- Web line **792**, page marker **32**: `de nas lho phyogs tshal pa skyob`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-062

Category: `textual_difference`. Alignment: `replace`.

- Source **U00781**, characters [22922, 22950): ལྕང་ལོ་ཅན་གྱི་རིགས་དག་གིས། །
  - Exact EWTS: `lcang lo can gyi rigs dag gis/_/`
- Web line **797**, page marker **33**: `lcang po can gyi rigs dag gis`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-063

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00792**, characters [23234, 23259): སཱུ་ཏྲ་སྡེ་ཞེས་བྱ་བ་ཡི། །
  - Exact EWTS: `sU tra sde zhes bya ba yi/_/`
- Web line **808**, page marker **33**: `su tra sde zhes bya ba yi`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-064

Category: `textual_difference`. Alignment: `replace`.

- Source **U00795**, characters [23316, 23338): ཛ་ཡ་ཨཱ་ཀར་ཞེས་བྱ་བས། །
  - Exact EWTS: `dza ya A kar zhes bya bas/_/`
- Web line **811**, page marker **33**: `dza ya sa kar zhes bya bas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-065

Category: `textual_difference`. Alignment: `replace`.

- Source **U00800**, characters [23458, 23499): བྷ་ར་བྷ་ཏི་ས་ཡི་ཡང་བྱུང་ས་ལི་ཞེས་བྱ་བར། །
  - Exact EWTS: `b+ha ra b+ha ti sa yi yang byung sa li zhes bya bar/_/`
- Web line **816**, page marker **33**: `bha ra sa li zhes bya bar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-066

Category: `textual_difference`. Alignment: `replace`.

- Source **U00803**, characters [23558, 23590): དགེ་སློང་བདེ་བ་སྐྱོང་གིས་ཀྱང་། །
  - Exact EWTS: `dge slong bde ba skyong gis kyang /_/`
- Web line **819**, page marker **33**: `dge slong bde ba skyod gis kyang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-067

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00822**, characters [24101, 24120): དྲིས་ལན་བཅུ་གསུམ་པ།
  - Exact EWTS: `dris lan bcu gsum pa/`
- Web: ∅ between lines 838 and 839.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-068

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00874**, characters [25582, 25609): ཆུ་བོ་ཆེན་པོ་གངྒཱའི་འགྲམ། །
  - Exact EWTS: `chu bo chen po gang+gA'i 'gram/_/`
- Web line **892**, page marker **36**: `chu bo chen po gang ga'i 'gram`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-069

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00881**, characters [25768, 25796): ཤཱི་ལ་ཞེས་པའི་གཙུག་ལག་ཁང་། །
  - Exact EWTS: `shI la zhes pa'i gtsug lag khang /_/`
- Web line **899**, page marker **36**: `shi la zhes pa'i gtsug lag khang`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-070

Category: `textual_difference`. Alignment: `replace`.

- Source **U00901**, characters [26345, 26371): དགེ་སློང་ཤཱཀྱ་ཛཱི་ཀ་ཡིས། །
  - Exact EWTS: `dge slong shAkya dzI ka yis/_/`
- Web line **920**, page marker **37**: `dge slong sha kya dzi ka yis`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-071

Category: `textual_difference`. Alignment: `replace`.

- Source **U00909**, characters [26571, 26598): འདི་ན་མི་གནས་དེར་སྣང་ངོ་། །
  - Exact EWTS: `'di na mi gnas der snang ngo /_/`
- Source **U00910**, characters [26598, 26616): དྲིས་ལན་བཅུ་བཞི་པ།
  - Exact EWTS: `dris lan bcu bzhi pa/`
- Web line **928**, page marker **37**: `'di nas mi gnas der snang ngo`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-072

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00915**, characters [26736, 26764): ཨུཏྤལ་མེ་ཏོག་མཛེས་ཞེས་པའི། །
  - Exact EWTS: `ut+pal me tog mdzes zhes pa'i/_/`
- Web line **933**, page marker **37**: `ut pal me tog mdzes zhes pa'i`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-073

Category: `textual_difference`. Alignment: `replace`.

- Source **U00934**, characters [27301, 27328): བྱ་བ་བྱས་ཤིང་ཁུར་བོར་བའོ། །
  - Exact EWTS: `bya ba byas shing khur bor ba'o/_/`
- Web line **953**, page marker **38**: `bya ba byas shing khur bor pa'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-074

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U00948**, characters [27704, 27721): དྲིས་ལན་བཅོ་ལྔ་པ།
  - Exact EWTS: `dris lan bco lnga pa/`
- Web: ∅ between lines 966 and 968.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-075

Category: `textual_difference`. Alignment: `replace`.

- Source **U00963**, characters [28128, 28155): གདོན་མི་ཟ་བར་འཚང་རྒྱ་ངེས། །
  - Exact EWTS: `gdon mi za bar 'tshang rgya nges/_/`
- Web line **982**, page marker **39**: `gdon mi za bar 'tshang rgya des`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-076

Category: `textual_difference`. Alignment: `replace`.

- Source **U00988**, characters [28865, 28888): དྷ་ན་ཀོ་ཤའི་ལྷ་ལྕམ་ལ། །
  - Exact EWTS: `d+ha na ko sha'i lha lcam la/_/`
- Source **U00989**, characters [28888, 28909): ཕ་མེད་བུ་ནི་བཛྲ་ཧེ། །
  - Exact EWTS: `pha med bu ni badzra he/_/`
- Web line **1008**, page marker **40**: `dha na ko sha'i lha lcam la`
- Web line **1009**, page marker **40**: `pha med bu ni ba dzra te`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-077

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U00993**, characters [29000, 29022): མན་ཛུ་ཤྲཱི་པ་ཏི་ཞེས། །
  - Exact EWTS: `man dzu shrI pa ti zhes/_/`
- Web line **1013**, page marker **40**: `man dzu shri pa ti zhes`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-078

Category: `textual_difference`. Alignment: `replace`.

- Source **U00997**, characters [29100, 29129): ཁྱིམ་བདག་རིགས་ལ་ཤྲཱི་སིདྷ་། །
  - Exact EWTS: `khyim bdag rigs la shrI sid+ha /_/`
- Web line **1017**, page marker **40**: `khyim bdag rigs la shri sing ha`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-079

Category: `textual_difference`. Alignment: `replace`.

- Source **U01000**, characters [29189, 29218): ཛྙཱ་ན་སཱུ་ཏྲས་འདི་ཉིད་འཛིན། །
  - Exact EWTS: `dz+nyA na sU tras 'di nyid 'dzin/_/`
- Web line **1020**, page marker **40**: `dznya na su tras 'di nyid 'dzin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-080

Category: `textual_difference`. Alignment: `replace`.

- Source **U01007**, characters [29401, 29428): དེ་རྗེས་སེདྷེ་ཤྭ་རས་འཛིན། །
  - Exact EWTS: `de rjes sed+he shwa ras 'dzin/_/`
- Web line **1028**, page marker **41**: `de rjes seng ha shwa ras 'dzin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-081

Category: `textual_difference`. Alignment: `replace`.

- Source **U01011**, characters [29507, 29531): སྤྲུལ་པ་བཛྲ་ཕ་ལས་འཛིན། །
  - Exact EWTS: `sprul pa badzra pha las 'dzin/_/`
- Web line **1032**, page marker **41**: `sprul pa ba dzra pha las 'dzin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-082

Category: `textual_difference`. Alignment: `replace`.

- Source **U01015**, characters [29613, 29640): དེ་འོག་ཡོ་གི་པྲ་བྷས་འཛིན། །
  - Exact EWTS: `de 'og yo gi pra b+has 'dzin/_/`
- Web line **1036**, page marker **41**: `de 'og yo gi pra bhas 'dzin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-083

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01023**, characters [29832, 29851): དྲིས་ལན་བཅུ་དྲུག་པ།
  - Exact EWTS: `dris lan bcu drug pa/`
- Web: ∅ between lines 1043 and 1044.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-084

Category: `textual_difference`. Alignment: `replace`.

- Source **U01028**, characters [29965, 29992): རྡོ་རྗེ་གདན་གྱི་སྤོ་ལ་ནི། །
  - Exact EWTS: `rdo rje gdan gyi spo la ni/_/`
- Web line **1048**, page marker **41**: `rdo rje gdan gyi sbo la ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-085

Category: `textual_difference`. Alignment: `replace`.

- Source **U01033**, characters [30099, 30127): འཁོར་ལོ་གློག་གི་ཕྲེང་བ་ཡི། །
  - Exact EWTS: `'khor lo glog gi phreng ba yi/_/`
- Web line **1054**, page marker **42**: `'khor log glog gi phreng ba yi`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-086

Category: `textual_difference`. Alignment: `replace`.

- Source **U01044**, characters [30408, 30435): འཕགས་པ་ཚངས་པའི་འོད་ཅེས་པ། །
  - Exact EWTS: `'phags pa tshangs pa'i 'od ces pa/_/`
- Web line **1065**, page marker **42**: `'phags pa tshangs pa'i 'od ces ba`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-087

Category: `textual_difference`. Alignment: `replace`.

- Source **U01067**, characters [31089, 31131): བརྒྱ་ཡང་བྱུང་ཐམས་ཅད་ཚེ་གཅིག་འབྲས་བུ་ཐོབ། །
  - Exact EWTS: `brgya yang byung thams cad tshe gcig 'bras bu thob/_/`
- Web line **1089**, page marker **43**: `thams cad tshe gcig 'bras bu thob`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-088

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01083**, characters [31564, 31587): དྲིས་ལན་བཅུ་བདུན་པའོ། །
  - Exact EWTS: `dris lan bcu bdun pa'o/_/`
- Web: ∅ between lines 1105 and 1106.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-089

Category: `textual_difference`. Alignment: `replace`.

- Source **U01086**, characters [31642, 31666): གཉིས་དང་ལྔ་བཅུ་ཐམ་པའོ། །
  - Exact EWTS: `gnyis dang lnga bcu tham pa'o/_/`
- Web line **1108**, page marker **44**: `gnyis dang lnga bcu tha ma pa'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-090

Category: `textual_difference`. Alignment: `replace`.

- Source **U01090**, characters [31738, 31784): ཡན་ལག་བཀོད་པ་བརྒྱ་བཅུ་གཅིག་ཀྱང་བྱུང་གཅིག་གོ། །
  - Exact EWTS: `yan lag bkod pa brgya bcu gcig kyang byung gcig go/_/`
- Web line **1112**, page marker **44**: `yan lag bkod pa brgya gcig go`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-091

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01122**, characters [32646, 32670): དྲིས་ལན་བཅོ་བརྒྱད་པའོ། །
  - Exact EWTS: `dris lan bco brgyad pa'o/_/`
- Web: ∅ between lines 1144 and 1145.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-092

Category: `source_text_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01144**, characters [33301, 33313): ཚིག་ཆད་སོང་།
  - Exact EWTS: `tshig chad song /`
- Web: ∅ between lines 1166 and 1167.

**Provisional comparison disposition and reason:** Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.

### W-C01-093

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01147**, characters [33367, 33385): དྲིས་ལན་བཅུ་དགུ་པ།
  - Exact EWTS: `dris lan bcu dgu pa/`
- Web: ∅ between lines 1168 and 1169.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-094

Category: `textual_difference`. Alignment: `replace`.

- Source **U01152**, characters [33493, 33526): དབྱར་དགུན་སྟོན་དཔྱིད་དུས་བཞི་ལ། །
  - Exact EWTS: `dbyar dgun ston dpyid dus bzhi la/_/`
- Web line **1173**, page marker **46**: `dbyar dgun stod dpyid dus bzhi la`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-095

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U01156**, characters [33616, 33645): འདི་དུས་རླུང་ནི་བརྩེག་མ་འམ། །
  - Exact EWTS: `'di dus rlung ni brtseg ma 'am/_/`
- Web line **1177**, page marker **46**: `'di dus rlung ni brtseg ma'am`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-096

Category: `textual_difference`. Alignment: `replace`.

- Source **U01178**, characters [34229, 34256): སུམ་ཅུ་དག་ཏུ་འགྱུར་བ་ཡིན། །
  - Exact EWTS: `sum cu dag tu 'gyur ba yin/_/`
- Web line **1200**, page marker **47**: `sum cu dag tu 'gyur pa yin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-097

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01186**, characters [34465, 34481): དྲིས་ལན་ཉི་ཤུ་པ།
  - Exact EWTS: `dris lan nyi shu pa/`
- Web: ∅ between lines 1207 and 1208.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-098

Category: `textual_difference`. Alignment: `replace`.

- Source **U01188**, characters [34510, 34538): ནམ་མཁའི་ཁམས་དང་སྦྱར་བ་སྟེ། །
  - Exact EWTS: `nam mkha'i khams dang sbyar ba ste/_/`
- Web line **1209**, page marker **47**: `nam mkha' khams dang sbyar ba ste`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-099

Category: `textual_difference`. Alignment: `replace`.

- Source **U01190**, characters [34562, 34592): རྒྱ་ཁྱོན་ས་ལ་མཐུག་ཁོད་སྙོམས། །
  - Exact EWTS: `rgya khyon sa la mthug khod snyoms/_/`
- Web line **1211**, page marker **47**: `rgya khyon sa ya mthug khong snyoms`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-100

Category: `textual_difference`. Alignment: `replace`.

- Source **U01196**, characters [34733, 34767): རྒྱ་མཚོ་ཆེན་པོའི་ཟབས་ཀྱིས་བསྐོར། །
  - Exact EWTS: `rgya mtsho chen po'i zabs kyis bskor/_/`
- Web line **1218**, page marker **48**: `rgya mtsho chen po'i zab kyis bskor`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-101

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01219**, characters [35388, 35411): དྲིས་ལན་ཉེར་གཅིག་པའོ། །
  - Exact EWTS: `dris lan nyer gcig pa'o/_/`
- Web: ∅ between lines 1241 and 1242.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-102

Category: `textual_difference`. Alignment: `replace`.

- Source **U01225**, characters [35536, 35570): བསྐལ་ཆུང་གསུམ་གྱིས་མཚམས་སྦྱར་ནས། །
  - Exact EWTS: `bskal chung gsum gyis mtshams sbyar nas/_/`
- Web line **1247**, page marker **49**: `bskal chud gsum gyis mtshams sbyar nas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-103

Category: `textual_difference`. Alignment: `replace`.

- Source **U01233**, characters [35767, 35813): དེ་ལྟར་བརྒྱ་དང་བརྒྱད་ཅུ་ཆགས་འཇིག་སྟོངས་པ་ལས། །
  - Exact EWTS: `de ltar brgya dang brgyad cu chags 'jig stongs pa las/_/`
- Web line **1255**, page marker **49**: `de ltar brgya dang brgyad cu las`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-104

Category: `textual_difference`. Alignment: `replace`.

- Source **U01237**, characters [35896, 35939): དེ་ལྟར་སྦྲགས་ཆགས་འཇིག་སྟོངས་པ་པ་དེ་ཙམ་ལས། །
  - Exact EWTS: `de ltar sbrags chags 'jig stongs pa pa de tsam las/_/`
- Web line **1259**, page marker **49**: `de ltar sbrags pa de tsam las`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-105

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01239**, characters [35967, 35986): དྲིས་ལན་ཉེར་གཉིས་པ།
  - Exact EWTS: `dris lan nyer gnyis pa/`
- Web: ∅ between lines 1260 and 1261.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-106

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01257**, characters [36469, 36488): དྲིས་ལན་ཉེར་གསུམ་པ།
  - Exact EWTS: `dris lan nyer gsum pa/`
- Web: ∅ between lines 1278 and 1279.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-107

Category: `textual_difference`. Alignment: `replace`.

- Source **U01259**, characters [36515, 36545): བསྒྲུབ་དང་རྒྱས་པའི་ཆོ་ག་ཉིད། །
  - Exact EWTS: `bsgrub dang rgyas pa'i cho ga nyid/_/`
- Web line **1280**, page marker **50**: `bsgrub dang rgyas ba'i cho ga nyid`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-108

Category: `textual_difference`. Alignment: `replace`.

- Source **U01265**, characters [36690, 36730): རྣལ་འབྱོར་པ་ཡིས་བཀུག་དཀྲུག་ཀྱང་ ཤེས་ན། །
  - Exact EWTS: `rnal 'byor pa yis bkug dkrug kyang _shes na/_/`
- Web line **1286**, page marker **50**: `rnal 'byor pa yis bkug shes na`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-109

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01271**, characters [36872, 36894): དྲིས་ལན་ཉེར་བཞི་པའོ། །
  - Exact EWTS: `dris lan nyer bzhi pa'o/_/`
- Web: ∅ between lines 1291 and 1293.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-110

Category: `web_text_absent_in_source_units`. Alignment: `insert`.

- Source: ∅ between **U01274** and **U01275**.
- Web line **1296**, page marker **51**: `chu yi zug pas dbang po sdud`
- Web line **1297**, page marker **51**: `byer ba yis ni 'khrugs par byed`
- Web line **1298**, page marker **51**: `snyoms pa yis ni 'bras bu 'byin`

**Provisional comparison disposition and reason:** Record W as possible missing source text without inserting it solely on website authority. A subsequent scan-attested intervention may restore it and governs the adopted reading.

### W-C01-111

Category: `source_text_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01286**, characters [37303, 37327): ཆུའི་བྱེར་སྙོམས་གཉིས་ཆད།
  - Exact EWTS: `chu'i byer snyoms gnyis chad/`
- Web: ∅ between lines 1309 and 1310.

**Provisional comparison disposition and reason:** Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.

### W-C01-112

Category: `textual_difference`. Alignment: `replace`.

- Source **U01301**, characters [37746, 37777): བྱེར་བས་དགེ་བའི་ལས་ཀུན་འགྲུབ། །
  - Exact EWTS: `byer bas dge ba'i las kun 'grub/_/`
- Web line **1325**, page marker **52**: `byer pas dge ba'i las kun 'grub`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-113

Category: `textual_difference`. Alignment: `replace`.

- Source **U01305**, characters [37861, 37892): སྙོམས་པས་གཤེད་ཀྱི་ཆོ་ག་འགྲུབ། །
  - Exact EWTS: `snyoms pas gshed kyi cho ga 'grub/_/`
- Web line **1329**, page marker **52**: `snyoms pas gshed kyis cho ga 'grub`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-114

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01308**, characters [37950, 37967): དྲིས་ལན་ཉེར་ལྔ་པ།
  - Exact EWTS: `dris lan nyer lnga pa/`
- Web: ∅ between lines 1331 and 1332.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-115

Category: `textual_difference`. Alignment: `replace`.

- Source **U01311**, characters [38027, 38055): མཐའ་དང་བྲལ་བས་དབུས་མི་གནས། །
  - Exact EWTS: `mtha' dang bral bas dbus mi gnas/_/`
- Web line **1334**, page marker **52**: `mtha' dang bul bas dbus mi gnas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-116

Category: `textual_difference`. Alignment: `replace`.

- Source **U01321**, characters [38315, 38349): གོམས་པའི་སྟོབས་ཀྱིས་འཁྲུལ་པ་འཇིག །
  - Exact EWTS: `goms pa'i stobs kyis 'khrul pa 'jig_/`
- Web line **1344**, page marker **52**: `goms pa'i stobs kyis 'khrul 'jig`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-117

Category: `textual_difference`. Alignment: `replace`.

- Source **U01324**, characters [38406, 38434): རང་སྣང་ཡིན་པས་རྣམ་རྟོག་ཟད། །
  - Exact EWTS: `rang snang yin pas rnam rtog zad/_/`
- Web line **1348**, page marker **53**: `rang snang yin pas rnam rtog zang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-118

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01335**, characters [38721, 38744): དྲིས་ལན་ཉེར་དྲུག་པའོ། །
  - Exact EWTS: `dris lan nyer drug pa'o/_/`
- Web: ∅ between lines 1358 and 1359.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-119

Category: `textual_difference`. Alignment: `replace`.

- Source **U01345**, characters [38998, 39028): མཛད་པ་བཅུ་གཉིས་ཕྲག་གསུམ་གྱི། །
  - Exact EWTS: `mdzad pa bcu gnyis phrag gsum gyi/_/`
- Web line **1368**, page marker **53**: `mdzad pa bcu gnyis phrag gsum kyi`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-120

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01353**, characters [39224, 39243): དྲིས་ལན་ཉེར་བདུན་པ།
  - Exact EWTS: `dris lan nyer bdun pa/`
- Web: ∅ between lines 1376 and 1377.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-121

Category: `textual_difference`. Alignment: `replace`.

- Source **U01358**, characters [39363, 39386): ཆུ་ཡི་སྒྲ་ནི་གཤང་བ་ལ། །
  - Exact EWTS: `chu yi sgra ni gshang ba la/_/`
- Source **U01359**, characters [39386, 39417): མཁའ་འགྲོ་མ་ཡི་སྒྲ་དབྱངས་འཛིན། །
  - Exact EWTS: `mkha' 'gro ma yi sgra dbyangs 'dzin/_/`
- Web line **1381**, page marker **54**: `chu yi sgra ni gshad pa la`
- Web line **1382**, page marker **54**: `mkha' 'gro ma yin sgra dbyangs 'dzin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-122

Category: `textual_difference`. Alignment: `replace`.

- Source **U01367**, characters [39625, 39661): ཁྱབ་འཇུག་ཆེན་པོའི་གསུང་དབྱངས་སྟོན། །
  - Exact EWTS: `khyab 'jug chen po'i gsung dbyangs ston/_/`
- Web line **1390**, page marker **54**: `khyab 'jug chen po'i gsungs dbyangs ston`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-123

Category: `textual_difference`. Alignment: `replace`.

- Source **U01371**, characters [39748, 39783): མཁའ་ལྡིང་རྒྱལ་པོའི་སྦྱོར་བ་གསུང་། །
  - Exact EWTS: `mkha' lding rgyal po'i sbyor ba gsung /_/`
- Web line **1394**, page marker **54**: `mkha' lding rgyal po'i sbyor pa gsung`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-124

Category: `textual_difference`. Alignment: `replace`.

- Source **U01378**, characters [39955, 39982): རིམ་པ་དུས་དང་ངེས་སྦྱར་ཏེ། །
  - Exact EWTS: `rim pa dus dang nges sbyar te/_/`
- Web line **1402**, page marker **55**: `rim pa dus dang des sbyar te`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-125

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01381**, characters [40038, 40062): དྲིས་ལན་ཉེར་བརྒྱད་པའོ། །
  - Exact EWTS: `dris lan nyer brgyad pa'o/_/`
- Web: ∅ between lines 1404 and 1405.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-126

Category: `textual_difference`. Alignment: `replace`.

- Source **U01395**, characters [40440, 40470): ཁྱི་དང་དྲེད་སྤྱང་ལས་རྒྱལ་བར། །
  - Exact EWTS: `khyi dang dred spyang las rgyal bar/_/`
- Web line **1418**, page marker **55**: `khyi dang dred sbyang las rgyal bar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-127

Category: `textual_difference`. Alignment: `replace`.

- Source **U01405**, characters [40737, 40768): ལེགས་པར་སྦྱར་ཏེ་གསལ་བྱེད་ཀྱི། །
  - Exact EWTS: `legs par sbyar te gsal byed kyi/_/`
- Web line **1429**, page marker **56**: `legs par byar te gsal byed kyi`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-128

Category: `textual_difference`. Alignment: `replace`.

- Source **U01414**, characters [41000, 41044): ས་པ་ལ་སེ་ཡི་ཡང་བྱུང་ལ་སེར་པོའི་སྦྱོར་བ་ཡི། །
  - Exact EWTS: `sa pa la se yi yang byung la ser po'i sbyor ba yi/_/`
- Web line **1438**, page marker **56**: `sa la ser po'i sbyor ba yi`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-129

Category: `textual_difference`. Alignment: `replace`.

- Source **U01417**, characters [41104, 41154): འབྱུང་བའི་དུས་ཉིད་རབ་བསྟིམས་ བསྡེབས་ཀྱང་བྱུང་ནས། །
  - Exact EWTS: `'byung ba'i dus nyid rab bstims _bsdebs kyang byung nas/_/`
- Web line **1441**, page marker **56**: `'byung ba'i dus nyid rab bstims nas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-130

Category: `textual_difference`. Alignment: `replace`.

- Source **U01422**, characters [41268, 41315): རིན་པོ་ཆེ་ཡི་རིན་ཆེན་བསེའི་ཡང་བྱུང་སྦྱོར་བ་དག །
  - Exact EWTS: `rin po che yi rin chen bse'i yang byung sbyor ba dag_/`
- Web line **1446**, page marker **56**: `rin po che yi sbyor ba dag`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-131

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U01429**, characters [41495, 41522): ཨ་དང་ཡཾ་གིས་རྣམ་པར་བརྒྱན། །
  - Exact EWTS: `a dang yaM gis rnam par brgyan/_/`
- Web line **1454**, page marker **57**: `a dang yam gis rnam par brgyan`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-132

Category: `textual_difference`. Alignment: `replace`.

- Source **U01432**, characters [41578, 41607): རྐང་པའི་མཐིལ་དུ་ལྡེ་གུས་ནི། །
  - Exact EWTS: `rkang pa'i mthil du lde gus ni/_/`
- Web line **1457**, page marker **57**: `rkang pa'i mthil du sde gus ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-133

Category: `textual_difference`. Alignment: `replace`.

- Source **U01439**, characters [41786, 41832): ལེགས་པར་སྦྱར་ཏེ་ཨ་ ཨ་ལིས་ཀྱང་བྱུང་ཡིས་བསྐོར། །
  - Exact EWTS: `legs par sbyar te a _a lis kyang byung yis bskor/_/`
- Web line **1464**, page marker **57**: `legs par sbyar te a yis bskor`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-134

Category: `textual_difference`. Alignment: `replace`.

- Source **U01446**, characters [42007, 42036): རིན་པོ་ཆེ་ཡི་སྣོད་དུ་བླུགས། །
  - Exact EWTS: `rin po che yi snod du blugs/_/`
- Web line **1471**, page marker **57**: `rin po che'i snod du blugs`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-135

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01454**, characters [42224, 42246): དྲིས་ལན་ཉེར་དགུ་པའོ། །
  - Exact EWTS: `dris lan nyer dgu pa'o/_/`
- Web: ∅ between lines 1479 and 1480.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-136

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U01462**, characters [42445, 42472): པ་ལཱ་ཤ་ཡི་སྦྱོར་ལུགས་དང་། །
  - Exact EWTS: `pa lA sha yi sbyor lugs dang /_/`
- Web line **1487**, page marker **58**: `pa la sha yi sbyor lugs dang`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-137

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01476**, characters [42847, 42864): དྲིས་ལན་སུམ་ཅུ་པ།
  - Exact EWTS: `dris lan sum cu pa/`
- Web: ∅ between lines 1500 and 1501.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-138

Category: `textual_difference`. Alignment: `replace`.

- Source **U01501**, characters [43577, 43608): དཀྲུགས་དང་བཅུད་དང་གནད་ལ་འབོར། །
  - Exact EWTS: `dkrugs dang bcud dang gnad la 'bor/_/`
- Web line **1526**, page marker **59**: `dkrugs dang gcud dang gnad la 'bor`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-139

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01514**, characters [43927, 43949): དྲིས་ལན་སོ་གཅིག་པའོ། །
  - Exact EWTS: `dris lan so gcig pa'o/_/`
- Web: ∅ between lines 1539 and 1540.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-140

Category: `textual_difference`. Alignment: `replace`.

- Source **U01525**, characters [44239, 44265): ངག་ནི་ཧཱུཾ་ཞེས་གནས་པ་ལས། །
  - Exact EWTS: `ngag ni hUM zhes gnas pa las/_/`
- Source **U01526**, characters [44265, 44294): རྒྱས་གདབ་པ་དང་རྩལ་སྦྱང་དང་། །
  - Exact EWTS: `rgyas gdab pa dang rtsal sbyang dang /_/`
- Source **U01527**, characters [44294, 44321): གཉན་བཙལ་ལམ་དུ་ཞུགས་པ་ཡིས། །
  - Exact EWTS: `gnyan btsal lam du zhugs pa yis/_/`
- Web line **1550**, page marker **60**: `ngag ni hum zhes gnas pa las`
- Web line **1551**, page marker **60**: `rgyas gdab pa dang rtsal sbyang dar`
- Web line **1552**, page marker **60**: `gnyen btsal lam du zhugs pa yis`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-141

Category: `textual_difference`. Alignment: `replace`.

- Source **U01529**, characters [44348, 44375): སེམས་ནི་ཐོག་མ་བྱུང་བ་དང་། །
  - Exact EWTS: `sems ni thog ma byung ba dang /_/`
- Source **U01530**, characters [44375, 44399): བར་དུ་གནས་པ་ཐ་མར་འགྲོ། །
  - Exact EWTS: `bar du gnas pa tha mar 'gro/_/`
- Web line **1554**, page marker **60**: `sems ni thog ma byung sa dang`
- Web line **1556**, page marker **60**: `bar du gnas pa tha ma 'gro`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-142

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01540**, characters [44656, 44674): དྲིས་ལན་སོ་གཉིས་པ།
  - Exact EWTS: `dris lan so gnyis pa/`
- Web: ∅ between lines 1567 and 1568.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-143

Category: `textual_difference`. Alignment: `replace`.

- Source **U01550**, characters [44943, 44971): ཡང་ཞིང་སྟོང་དང་གསལ་བར་ཁྱབ། །
  - Exact EWTS: `yang zhing stong dang gsal bar khyab/_/`
- Web line **1577**, page marker **61**: `yang zhing stod dang gsal bar khyab`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-144

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01557**, characters [45140, 45158): དྲིས་ལན་སོ་གསུམ་པ།
  - Exact EWTS: `dris lan so gsum pa/`
- Web: ∅ between lines 1583 and 1584.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-145

Category: `textual_difference`. Alignment: `replace`.

- Source **U01559**, characters [45185, 45212): གནས་དང་བཀོད་པ་འགྱུ་བ་དང་། །
  - Exact EWTS: `gnas dang bkod pa 'gyu ba dang /_/`
- Web line **1585**, page marker **61**: `gnas dang bkod pa 'gyu pa dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-146

Category: `textual_difference`. Alignment: `replace`.

- Source **U01567**, characters [45420, 45467): བསྡམས་པས་གཏེམས་ཀྱང་བྱུང་འགགས་ལ་བཙིར་བས་འཆིང༌། །
  - Exact EWTS: `bsdams pas gtems kyang byung 'gags la btsir bas 'ching*/_/`
- Web line **1594**, page marker **62**: `bsdams pas 'gags la btsir bas 'ching`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-147

Category: `textual_difference`. Alignment: `replace`.

- Source **U01573**, characters [45606, 45634): རྩ་ལ་བརྟེན་པའི་རླུང་དག་ནི། །
  - Exact EWTS: `rtsa la brten pa'i rlung dag ni/_/`
- Web line **1600**, page marker **62**: `tsal brten pa'i rlung dag ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-148

Category: `textual_difference`. Alignment: `replace`.

- Source **U01579**, characters [45776, 45802): ཡང་ན་མཁས་པས་གནད་ཉིད་བཙལ། །
  - Exact EWTS: `yang na mkhas pas gnad nyid btsal/_/`
- Web line **1606**, page marker **62**: `bar na mkhas pas gnad nyid btsal`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-149

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01596**, characters [46264, 46285): དྲིས་ལན་སོ་བཞི་པའོ། །
  - Exact EWTS: `dris lan so bzhi pa'o/_/`
- Web: ∅ between lines 1623 and 1624.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-150

Category: `textual_difference`. Alignment: `replace`.

- Source **U01598**, characters [46317, 46345): དོན་དམ་དང་ནི་ཀུན་རྫོ་བ་ལས། །
  - Exact EWTS: `don dam dang ni kun rdzo ba las/_/`
- Web line **1625**, page marker **63**: `don dam dang ni kun rdzob las`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-151

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01620**, characters [46973, 46993): དྲིས་ལན་སོ་ལྔ་པའོ། །
  - Exact EWTS: `dris lan so lnga pa'o/_/`
- Web: ∅ between lines 1647 and 1648.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-152

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01634**, characters [47371, 47389): དྲིས་ལན་སོ་དྲུག་པ།
  - Exact EWTS: `dris lan so drug pa/`
- Web: ∅ between lines 1660 and 1661.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-153

Category: `textual_difference`. Alignment: `replace`.

- Source **U01651**, characters [47849, 47878): འདི་དག་ངང་དུ་འཛིན་པར་འགྱུར། །
  - Exact EWTS: `'di dag ngang du 'dzin par 'gyur/_/`
- Web line **1678**, page marker **65**: `'di dag rang du 'dzin par 'gyur`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-154

Category: `textual_difference`. Alignment: `replace`.

- Source **U01657**, characters [48020, 48058): འདི་ཡི་ལུས་ཀྱང་ལུགས་ཀྱང་གསུམ་ཡིན་ཏེ། །
  - Exact EWTS: `'di yi lus kyang lugs kyang gsum yin te/_/`
- Web line **1684**, page marker **65**: `'di yi lus kyang gsum yin te`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-155

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01661**, characters [48148, 48166): དྲིས་ལན་སོ་བདུན་པ།
  - Exact EWTS: `dris lan so bdun pa/`
- Web: ∅ between lines 1687 and 1688.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-156

Category: `source_text_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01668**, characters [48348, 48361): བཀང་ཡང་བྱུང་།
  - Exact EWTS: `bkang yang byung /`
- Web: ∅ between lines 1693 and 1695.

**Provisional comparison disposition and reason:** Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.

### W-C01-157

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01689**, characters [48942, 48965): དྲིས་ལན་སོ་བརྒྱད་པའོ། །
  - Exact EWTS: `dris lan so brgyad pa'o/_/`
- Web: ∅ between lines 1714 and 1715.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-158

Category: `textual_difference`. Alignment: `replace`.

- Source **U01691**, characters [48996, 49025): རང་དང་གཞན་གཉིས་རྣམ་པར་སྦྱར། །
  - Exact EWTS: `rang dang gzhan gnyis rnam par sbyar/_/`
- Web line **1716**, page marker **66**: `rang dang gzhan gnyis nyam par sbyar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-159

Category: `textual_difference`. Alignment: `replace`.

- Source **U01693**, characters [49054, 49079): རང་གི་སྤོ་དང་བྱབས་བྱའོ། །
  - Exact EWTS: `rang gi spo dang byabs bya'o/_/`
- Web line **1718**, page marker **66**: `rang gi spo dang bya bas bya'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-160

Category: `textual_difference`. Alignment: `replace`.

- Source **U01696**, characters [49131, 49165): དེ་བཞིན་སེམས་ཀྱི་གནས་ཀྱིས་དགྲོལ། །
  - Exact EWTS: `de bzhin sems kyi gnas kyis dgrol/_/`
- Web line **1722**, page marker **67**: `de bzhin sems kyi gnad kyis dkrol`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-161

Category: `textual_difference`. Alignment: `replace`.

- Source **U01699**, characters [49221, 49250): བྱ་རྒོད་དག་དང་ལུག་གིས་སྤྲུག །
  - Exact EWTS: `bya rgod dag dang lug gis sprug_/`
- Web line **1725**, page marker **67**: `bya rgod dag dang lug gis sbrug`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-162

Category: `textual_difference`. Alignment: `replace`.

- Source **U01703**, characters [49336, 49364): ཕྱི་ནང་སྟོད་སྨད་ཡན་ལག་ལུས། །
  - Exact EWTS: `phyi nang stod smad yan lag lus/_/`
- Web line **1729**, page marker **67**: `phyi nang stod sman yan lag lus`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-163

Category: `textual_difference`. Alignment: `replace`.

- Source **U01706**, characters [49424, 49450): ཚ་དང་གྲང་བས་མཐའ་ཕྱེས་ཏེ། །
  - Exact EWTS: `tsha dang grang bas mtha' phyes te/_/`
- Web line **1732**, page marker **67**: `tsha dang grang bas mthar phyes te`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-164

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U01709**, characters [49503, 49527): ཨཱ་ལི་ཀཱ་ལི་རབ་གསལ་བས། །
  - Exact EWTS: `A li kA li rab gsal bas/_/`
- Web line **1735**, page marker **67**: `a li ka li rab gsal bas`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-165

Category: `textual_difference`. Alignment: `replace`.

- Source **U01711**, characters [49551, 49593): ཡི་གེ་བཟློག་བརྗོད་ཀྱང་ཚུལ་དྲུག་གིས་ཀྱང༌། །
  - Exact EWTS: `yi ge bzlog brjod kyang tshul drug gis kyang*/_/`
- Web line **1737**, page marker **67**: `yi ge bzlog tshul drug gis kyang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-166

Category: `textual_difference`. Alignment: `replace`.

- Source **U01716**, characters [49712, 49760): འདྲེ་དང་རླུང་ལྷ་དག་གི་དག་པའི་སྐད་ཀྱང་བྱུང་སྐད། །
  - Exact EWTS: `'dre dang rlung lha dag gi dag pa'i skad kyang byung skad/_/`
- Web line **1742**, page marker **67**: `'dre dang rlung lha dag gi skad`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-167

Category: `textual_difference`. Alignment: `replace`.

- Source **U01721**, characters [49882, 49912): ཅི་ལྟར་འགྱུས་པའི་མཐའ་ཡི་ཡང་། །
  - Exact EWTS: `ci ltar 'gyus pa'i mtha' yi yang /_/`
- Web line **1747**, page marker **67**: `ci ltar 'gyus ba'i mtha' yi yang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-168

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01727**, characters [50063, 50080): དྲིས་ལན་སོ་དགུ་པ།
  - Exact EWTS: `dris lan so dgu pa/`
- Web: ∅ between lines 1753 and 1754.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-169

Category: `textual_difference`. Alignment: `replace`.

- Source **U01734**, characters [50240, 50285): ཟླ་བ་ལོ་ཡི་འཁྲུལ་འཁྲུགས་ལུགས་ཀྱང་ལུགས་ཀྱིས། །
  - Exact EWTS: `zla ba lo yi 'khrul 'khrugs lugs kyang lugs kyis/_/`
- Source **U01735**, characters [50285, 50314): བཅུ་གཉིས་ཕྲག་དང་སྦོམ་པ་ཡང༌། །
  - Exact EWTS: `bcu gnyis phrag dang sbom pa yang*/_/`
- Web line **1760**, page marker **68**: `zla ba lo yi 'khrul lugs kyis`
- Web line **1761**, page marker **68**: `bcu gnyis phrag dang spom pa yang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-170

Category: `textual_difference`. Alignment: `replace`.

- Source **U01737**, characters [50342, 50372): ངེས་མེད་འཁྲུགས་མར་གནས་པ་བཞི། །
  - Exact EWTS: `nges med 'khrugs mar gnas pa bzhi/_/`
- Source **U01738**, characters [50372, 50400): དུས་ལ་ངེས་ཕྱེ་བཅུ་དྲུག་གི། །
  - Exact EWTS: `dus la nges phye bcu drug gi/_/`
- Web line **1763**, page marker **68**: `ngas med 'khrugs mar gnas pa bzhi`
- Web line **1764**, page marker **68**: `dus la nges phye bcu drug ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-171

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01751**, characters [50735, 50753): དྲིས་ལན་བཞི་བཅུ་པ།
  - Exact EWTS: `dris lan bzhi bcu pa/`
- Web: ∅ between lines 1776 and 1778.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-172

Category: `textual_difference`. Alignment: `replace`.

- Source **U01754**, characters [50809, 50841): ངེས་བཅས་འཇུག་པ་བརྒྱད་ཅུར་སྡུད། །
  - Exact EWTS: `nges bcas 'jug pa brgyad cur sdud/_/`
- Source **U01755**, characters [50841, 50864): དེ་ལས་ཉི་ཤུ་རྩ་བཞིའོ། །
  - Exact EWTS: `de las nyi shu rtsa bzhi'o/_/`
- Web line **1780**, page marker **69**: `des bcas 'jug pa brgyad cur sdud`
- Web line **1781**, page marker **69**: `de las nyi shu rtsa ba zhi'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-173

Category: `textual_difference`. Alignment: `replace`.

- Source **U01763**, characters [51070, 51101): གནད་རྣམས་དག་ཀྱང་ངེས་པར་འགྱུར། །
  - Exact EWTS: `gnad rnams dag kyang nges par 'gyur/_/`
- Source **U01764**, characters [51101, 51119): དྲིས་ལན་ཞེ་གཅིག་པ།
  - Exact EWTS: `dris lan zhe gcig pa/`
- Web line **1789**, page marker **69**: `gnang rnams dag kyang nges par 'gyur`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-174

Category: `textual_difference`. Alignment: `replace`.

- Source **U01774**, characters [51373, 51400): ལྔ་པ་གཅིག་ནི་མ་ནིང་སྟོང༌། །
  - Exact EWTS: `lnga pa gcig ni ma ning stong*/_/`
- Source **U01775**, characters [51400, 51429): ཤེས་ཤིང་བརྩི་བའི་རིམ་པ་ཡིན། །
  - Exact EWTS: `shes shing brtsi ba'i rim pa yin/_/`
- Source **U01776**, characters [51429, 51438): མིན་ཀྱང་།
  - Exact EWTS: `min kyang /`
- Web line **1799**, page marker **69**: `lnga po gcig ni ma ning stong`
- Web line **1800**, page marker **69**: `shes shing bstsi ba'i rim pa yin`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-175

Category: `textual_difference`. Alignment: `replace`.

- Source **U01803**, characters [52226, 52269): ས་གཞི་ཡང་བྱུང་ཡ་བཞི་བཟུང་སྟེ་རང་རང་བསྟུན། །
  - Exact EWTS: `sa gzhi yang byung ya bzhi bzung ste rang rang bstun/_/`
- Web line **1828**, page marker **70**: `ya bzhi bzung ste rang rang bstun`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-176

Category: `source_text_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01806**, characters [52329, 52353): ལྟེབ་དང་གཏུགས་ཀྱང་བྱུང་།
  - Exact EWTS: `lteb dang gtugs kyang byung /`
- Web: ∅ between lines 1831 and 1832.

**Provisional comparison disposition and reason:** Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.

### W-C01-177

Category: `textual_difference`. Alignment: `replace`.

- Source **U01810**, characters [52439, 52472): གསུམ་གྱི་གྲངས་བརྩིས་བཅུ་གཉིས་ལ། །
  - Exact EWTS: `gsum gyi grangs brtsis bcu gnyis la/_/`
- Source **U01811**, characters [52472, 52512): ལོ་སྟོང་ཞག་ལོ་སྟེ་ཞག་ཀྱང་བཅུ་ཕྲག་གསུམ། །
  - Exact EWTS: `lo stong zhag lo ste zhag kyang bcu phrag gsum/_/`
- Source **U01812**, characters [52512, 52540): ཡང་བྱུང་ཀྱང་འབུམ་ཕྲག་གསུམ། །
  - Exact EWTS: `yang byung kyang 'bum phrag gsum/_/`
- Web line **1835**, page marker **71**: `gsum gyi grangs rtsis bcu gnyis la`
- Web line **1836**, page marker **71**: `lo stong zhag kyang 'bum phrag gsum`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-178

Category: `textual_difference`. Alignment: `replace`.

- Source **U01820**, characters [52743, 52769): མར་གྱི་ངོ་ལ་ཉིན་མོ་རིང༌། །
  - Exact EWTS: `mar gyi ngo la nyin mo ring*/_/`
- Web line **1844**, page marker **71**: `mar gyi do la nyin mo ring`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-179

Category: `source_text_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01829**, characters [52994, 53032): གསུམ་སྟེ་དུས་ནི་བཅུ་གཉིས་སྦྱར་ཡང་བྱུང།
  - Exact EWTS: `gsum ste dus ni bcu gnyis sbyar yang byung/`
- Web: ∅ between lines 1852 and 1853.

**Provisional comparison disposition and reason:** Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.

### W-C01-180

Category: `textual_difference`. Alignment: `replace`.

- Source **U01835**, characters [53186, 53219): འབྱུང་བའི་ལོ་རྣམས་དུས་ཚོད་སྦྱར། །
  - Exact EWTS: `'byung ba'i lo rnams dus tshod sbyar/_/`
- Web line **1859**, page marker **72**: `'byung ba'i lo rnams dus chod sbyar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-181

Category: `textual_difference`. Alignment: `replace`.

- Source **U01841**, characters [53361, 53393): སོ་སོའི་ཕྱོགས་དང་ངེས་བསྟུན་ནས། །
  - Exact EWTS: `so so'i phyogs dang nges bstun nas/_/`
- Web line **1865**, page marker **72**: `so so'i phyogs dang des bstun nas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-182

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U01847**, characters [53535, 53560): བཙུན་མོ་བློན་པོ་པཎྜི་ཏ། །
  - Exact EWTS: `btsun mo blon po paN+Di ta/_/`
- Web line **1871**, page marker **72**: `btsun mo blon po pan di ta`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-183

Category: `textual_difference`. Alignment: `replace`.

- Source **U01850**, characters [53630, 53663): སྐྱེས་པ་བུད་མེད་གཟུགས་རྣམས་དང་། །
  - Exact EWTS: `skyes pa bud med gzugs rnams dang /_/`
- Web line **1874**, page marker **72**: `skyes pa bud med gzugs rnams dar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-184

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01854**, characters [53753, 53771): དྲིས་ལན་ཞེ་གཉིས་པ།
  - Exact EWTS: `dris lan zhe gnyis pa/`
- Web: ∅ between lines 1877 and 1878.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-185

Category: `textual_difference`. Alignment: `replace`.

- Source **U01859**, characters [53877, 53902): ལྟ་བུ་སྐལ་ལྡན་ངོ་ཆེ་བས། །
  - Exact EWTS: `lta bu skal ldan ngo che bas/_/`
- Web line **1883**, page marker **73**: `lha bu skal ldan ngo che bas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-186

Category: `textual_difference`. Alignment: `replace`.

- Source **U01872**, characters [54250, 54281): སྒྲ་ནས་བརྩམས་ཏེ་བསླབ་པར་བྱའོ། །
  - Exact EWTS: `sgra nas brtsams te bslab par bya'o/_/`
- Web line **1896**, page marker **73**: `sgra nas brtsam te bslab par bya'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-187

Category: `textual_difference`. Alignment: `replace`.

- Source **U01877**, characters [54405, 54432): དེ་ནས་སོ་སོའི་སྒྲ་ལ་སྦྱར། །
  - Exact EWTS: `de nas so so'i sgra la sbyar/_/`
- Web line **1901**, page marker **73**: `de nas so so'i sgra la sbyang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-188

Category: `web_text_absent_in_source_units`. Alignment: `insert`.

- Source: ∅ between **U01882** and **U01883**.
- Web line **1908**, page marker **74**: `so so'i tshad la rtags kyis 'grub`
- Web line **1909**, page marker **74**: `'di ltar su yi 'grub pa la`
- Web line **1910**, page marker **74**: `sprul pa'i sku dang longs sku dang`

**Provisional comparison disposition and reason:** Record W as possible missing source text without inserting it solely on website authority. A subsequent scan-attested intervention may restore it and governs the adopted reading.

### W-C01-189

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01906**, characters [55250, 55268): དྲིས་ལན་ཞེ་གསུམ་པ།
  - Exact EWTS: `dris lan zhe gsum pa/`
- Web: ∅ between lines 1933 and 1934.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-190

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01937**, characters [56132, 56149): དྲིས་ལན་ཞེ་བཞི་པ།
  - Exact EWTS: `dris lan zhe bzhi pa/`
- Web: ∅ between lines 1965 and 1966.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-191

Category: `textual_difference`. Alignment: `replace`.

- Source **U01946**, characters [56388, 56424): དངོས་པོ་འགྱུར་བའི་རྟེན་འབྲེལ་གྱིས། །
  - Exact EWTS: `dngos po 'gyur ba'i rten 'brel gyis/_/`
- Web line **1974**, page marker **76**: `dngos po 'gyur pa'i rten 'brel gyis`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-192

Category: `textual_difference`. Alignment: `replace`.

- Source **U01948**, characters [56453, 56485): དམིགས་པ་བསྐྱུར་ཏེ་ནད་སོགས་སྤོ། །
  - Exact EWTS: `dmigs pa bskyur te nad sogs spo/_/`
- Web line **1976**, page marker **76**: `dmigs pa bsgyur te nad sogs spo`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-193

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01968**, characters [57035, 57051): དྲིས་ལན་ཞེ་ལྔ་པ།
  - Exact EWTS: `dris lan zhe lnga pa/`
- Web: ∅ between lines 1996 and 1997.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-194

Category: `textual_difference`. Alignment: `replace`.

- Source **U01991**, characters [57704, 57733): དམིགས་པ་སྣ་ཚོགས་ནད་དང་སྦྱར། །
  - Exact EWTS: `dmigs pa sna tshogs nad dang sbyar/_/`
- Web line **2020**, page marker **78**: `dmigs pa sna tshogs nang dang sbyar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-195

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U01999**, characters [57941, 57963): དྲིས་ལན་ཞེ་དྲུག་པའོ། །
  - Exact EWTS: `dris lan zhe drug pa'o/_/`
- Web: ∅ between lines 2027 and 2028.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-196

Category: `web_text_absent_in_source_units`. Alignment: `insert`.

- Source: ∅ between **U02005** and **U02006**.
- Web line **2034**, page marker **78**: `gzhi ni 'jig rten pa yin te`
- Web line **2035**, page marker **78**: `'di las 'dod pa gnyis yin no`
- Web line **2036**, page marker **78**: `'das pa rgyu dang 'bras bu las`

**Provisional comparison disposition and reason:** Record W as possible missing source text without inserting it solely on website authority. A subsequent scan-attested intervention may restore it and governs the adopted reading.

### W-C01-197

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02021**, characters [58558, 58576): དྲིས་ལན་ཞེ་བདུན་པ།
  - Exact EWTS: `dris lan zhe bdun pa/`
- Web: ∅ between lines 2052 and 2053.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-198

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02046**, characters [59233, 59252): དྲིས་ལན་ཞེ་བརྒྱད་པ།
  - Exact EWTS: `dris lan zhe brgyad pa/`
- Web: ∅ between lines 2077 and 2078.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-199

Category: `textual_difference`. Alignment: `replace`.

- Source **U02061**, characters [59665, 59692): སོ་སོའི་ཁ་དོག་གིས་ཕྱི་ནས། །
  - Exact EWTS: `so so'i kha dog gis phyi nas/_/`
- Web line **2092**, page marker **80**: `so so'i kha dog gis phye nas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-200

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U02066**, characters [59819, 59844): ཨཱ་ལི་ཀཱ་ལིའི་ཕྲེང་བ་ལ། །
  - Exact EWTS: `A li kA li'i phreng ba la/_/`
- Web line **2098**, page marker **81**: `a li ka li 'i phreng ba la`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-201

Category: `textual_difference`. Alignment: `replace`.

- Source **U02070**, characters [59939, 59966): ཡང་ནས་ཡང་དུ་གོམས་སྤྱོད་ན། །
  - Exact EWTS: `yang nas yang du goms spyod na/_/`
- Web line **2102**, page marker **81**: `yar nas yang du goms spyod na`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-202

Category: `textual_difference`. Alignment: `replace`.

- Source **U02078**, characters [60175, 60208): དེ་ལ་བསྙེན་བསྒྲུབ་སྔར་དང་མཚུངས། །
  - Exact EWTS: `de la bsnyen bsgrub sngar dang mtshungs/_/`
- Web line **2110**, page marker **81**: `de la bsnyen sgrub sngar dang mtshungs`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-203

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U02109**, characters [61073, 61099): ཨཱ་ལི་ཀཱ་ལི་མཉམ་སྦྱར་བས། །
  - Exact EWTS: `A li kA li mnyam sbyar bas/_/`
- Web line **2142**, page marker **82**: `a li ka li mnyam sbyar bas`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-204

Category: `textual_difference`. Alignment: `replace`.

- Source **U02112**, characters [61159, 61184): ཆོ་གའི་དགོངས་པ་ཚང་བ་ལས། །
  - Exact EWTS: `cho ga'i dgongs pa tshang ba las/_/`
- Web line **2145**, page marker **82**: `cho ga'i dgongs pa tshad pa las`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-205

Category: `textual_difference`. Alignment: `replace`.

- Source **U02115**, characters [61236, 61273): གཤིན་རྗེའི་གཤེད་ཀྱི་རྣལ་འབྱོར་བྱའོ། །
  - Exact EWTS: `gshin rje'i gshed kyi rnal 'byor bya'o/_/`
- Web line **2148**, page marker **82**: `gshin rje'i gshed kyi rnal 'byor ba'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-206

Category: `textual_difference`. Alignment: `replace`.

- Source **U02117**, characters [61303, 61334): ཅི་ལྟར་འདོད་པའི་མོས་པས་བསྟེན། །
  - Exact EWTS: `ci ltar 'dod pa'i mos pas bsten/_/`
- Web line **2150**, page marker **82**: `ci ltar 'dod pa'i mos bas bsten`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-207

Category: `romanization_or_spacing_difference`. Alignment: `replace`.

- Source **U02122**, characters [61449, 61477): ཨཱ་ལི་ཀཱ་ལི་སོ་སོའི་འབྲེལ། །
  - Exact EWTS: `A li kA li so so'i 'brel/_/`
- Web line **2156**, page marker **83**: `a li ka li so so'i 'brel`

**Provisional comparison disposition and reason:** Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.

### W-C01-208

Category: `textual_difference`. Alignment: `replace`.

- Source **U02129**, characters [61648, 61688): དགུག་དང་བསད་དང་བསྐྲད་ཀྱང་བཅིངས་པའི་ལས། །
  - Exact EWTS: `dgug dang bsad dang bskrad kyang bcings pa'i las/_/`
- Source **U02130**, characters [61688, 61716): རང་གིས་ཅི་ལྟར་འདོད་པ་སྤྲོ། །
  - Exact EWTS: `rang gis ci ltar 'dod pa spro/_/`
- Web line **2163**, page marker **83**: `dgug dang bsad dang bcings pa'i las`
- Web line **2164**, page marker **83**: `rang gis ci ltar 'dod pa sbro`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-209

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02142**, characters [62050, 62067): དྲིས་ལན་ཞེ་དགུ་པ།
  - Exact EWTS: `dris lan zhe dgu pa/`
- Web: ∅ between lines 2175 and 2176.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-210

Category: `textual_difference`. Alignment: `replace`.

- Source **U02151**, characters [62294, 62324): གསལ་དང་མུན་པ་སྲིད་འབྱུང་མིན། །
  - Exact EWTS: `gsal dang mun pa srid 'byung min/_/`
- Source **U02152**, characters [62324, 62356): འགྲོ་འོང་སྲིད་མཐའ་མེད་ཕྱིར་རོ། །
  - Exact EWTS: `'gro 'ong srid mtha' med phyir ro/_/`
- Web line **2185**, page marker **84**: `gsal dang mun pa sid 'byung min`
- Web line **2186**, page marker **84**: `'go 'ong srid mtha' med phyir ro`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-211

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02162**, characters [62616, 62633): དྲིས་ལན་ལྔ་བཅུ་པ།
  - Exact EWTS: `dris lan lnga bcu pa/`
- Web: ∅ between lines 2195 and 2196.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-212

Category: `textual_difference`. Alignment: `replace`.

- Source **U02169**, characters [62815, 62848): འཁྲུལ་པའི་དུས་ཚོད་ངེས་བཟུང་སྟེ། །
  - Exact EWTS: `'khrul pa'i dus tshod nges bzung ste/_/`
- Web line **2202**, page marker **84**: `'khrul pa'i dus tshod des bzung ste`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-213

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02180**, characters [63158, 63175): དྲིས་ལན་ང་གཅིག་པ།
  - Exact EWTS: `dris lan nga gcig pa/`
- Web: ∅ between lines 2213 and 2214.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-214

Category: `web_text_absent_in_source_units`. Alignment: `insert`.

- Source: ∅ between **U02187** and **U02188**.
- Web line **2221**, page marker **85**: `'du shes can dag mtha' la 'jog`
- Web line **2222**, page marker **85**: `mngon sum gnad kyi man ngag gis`

**Provisional comparison disposition and reason:** Record W as possible missing source text without inserting it solely on website authority. A subsequent scan-attested intervention may restore it and governs the adopted reading.

### W-C01-215

Category: `textual_difference`. Alignment: `replace`.

- Source **U02190**, characters [63444, 63479): རླུང་སེམས་འབྲེལ་པའི་སྤྲོས་པ་གཅོད། །
  - Exact EWTS: `rlung sems 'brel pa'i spros pa gcod/_/`
- Web line **2225**, page marker **85**: `rlung sems 'brel pa'i spos pa gcod`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-216

Category: `textual_difference`. Alignment: `replace`.

- Source **U02193**, characters [63540, 63557): དྲིས་ལན་ང་གཉིས་པ།
  - Exact EWTS: `dris lan nga gnyis pa/`
- Source **U02194**, characters [63557, 63585): བླ་མ་རྡོ་རྗེ་འཆང་ཆེན་གྱིས། །
  - Exact EWTS: `bla ma rdo rje 'chang chen gyis/_/`
- Web line **2228**, page marker **85**: `bla ma rdo rje 'chad chen gyis`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-217

Category: `textual_difference`. Alignment: `replace`.

- Source **U02208**, characters [63966, 63993): དབང་པོ་གསལ་བས་བླ་མ་བསྟེན། །
  - Exact EWTS: `dbang po gsal bas bla ma bsten/_/`
- Source **U02209**, characters [63993, 64019): བསྟེན་པ་དེ་ལས་ཡོན་ཏན་ནི། །
  - Exact EWTS: `bsten pa de las yon tan ni/_/`
- Web line **2243**, page marker **86**: `dbang po gsal pas bla ma bsten`
- Web line **2244**, page marker **86**: `bstan pa de las yon tan ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-218

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02215**, characters [64163, 64180): དྲིས་ལན་ང་གསུམ་པ།
  - Exact EWTS: `dris lan nga gsum pa/`
- Web: ∅ between lines 2249 and 2250.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-219

Category: `textual_difference`. Alignment: `replace`.

- Source **U02225**, characters [64442, 64491): སྒྲ་དང་གདམས་ངག་སྨྲ་དང་གཏམ་ངན་ཡང་བྱུང་ལ་སོགས་ཏེ། །
  - Exact EWTS: `sgra dang gdams ngag smra dang gtam ngan yang byung la sogs te/_/`
- Web line **2260**, page marker **87**: `sga dang gdams ngag la sogs te`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-220

Category: `textual_difference`. Alignment: `replace`.

- Source **U02228**, characters [64555, 64584): སྐྱོང་བར་བྱེད་པ་བཅུ་གཅིག་ལ། །
  - Exact EWTS: `skyong bar byed pa bcu gcig la/_/`
- Source **U02229**, characters [64584, 64612): ཐན་དུ་ངེས་པར་དམིགས་བྱས་ཏེ། །
  - Exact EWTS: `than du nges par dmigs byas te/_/`
- Web line **2263**, page marker **87**: `skyod par byed pa bcu gcig la`
- Web line **2264**, page marker **87**: `than ngu nges par dmigs byas te`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-221

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02241**, characters [64942, 64958): དྲིས་ལན་ང་བཞི་པ།
  - Exact EWTS: `dris lan nga bzhi pa/`
- Web: ∅ between lines 2275 and 2276.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-222

Category: `textual_difference`. Alignment: `replace`.

- Source **U02246**, characters [65075, 65103): བསྟན་པའི་ཐབ་ནི་སྟོང་པ་དང༌། །
  - Exact EWTS: `bstan pa'i thab ni stong pa dang*/_/`
- Web line **2280**, page marker **87**: `bstan pa'i bab ni stong pa dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-223

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02250**, characters [65186, 65201): དྲིས་ལན་ང་ལྔ་པ།
  - Exact EWTS: `dris lan nga lnga pa/`
- Web: ∅ between lines 2283 and 2284.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-224

Category: `textual_difference`. Alignment: `replace`.

- Source **U02255**, characters [65306, 65332): དབང་བསྐུར་བ་ཡི་ཆོ་ག་བཤད། །
  - Exact EWTS: `dbang bskur ba yi cho ga bshad/_/`
- Web line **2289**, page marker **88**: `dbang bskur pa yi cho ga bshad`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-225

Category: `textual_difference`. Alignment: `replace`.

- Source **U02260**, characters [65442, 65469): རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར། །
  - Exact EWTS: `rnam par dag par bya ba'i phyir/_/`
- Source **U02261**, characters [65469, 65497): དབང་ནི་རྣམ་པ་བཞི་ཡིས་ཀྱང་། །
  - Exact EWTS: `dbang ni rnam pa bzhi yis kyang /_/`
- Web line **2294**, page marker **88**: `rnam par dag pa bya ba'i phyir`
- Web line **2295**, page marker **88**: `dpang ni rnam pa bzhi yis kyang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-226

Category: `textual_difference`. Alignment: `replace`.

- Source **U02268**, characters [65672, 65700): སྤྲོས་པ་ཅན་གྱི་དོན་དུ་ཡང་། །
  - Exact EWTS: `spros pa can gyi don du yang /_/`
- Web line **2302**, page marker **88**: `spos pa can gyi don du yang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-227

Category: `textual_difference`. Alignment: `replace`.

- Source **U02278**, characters [65963, 65991): དེ་དག་སོ་སོའི་དགོངས་པ་དང༌། །
  - Exact EWTS: `de dag so so'i dgongs pa dang*/_/`
- Web line **2312**, page marker **88**: `de dag so so'i dgos pa dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-228

Category: `textual_difference`. Alignment: `replace`.

- Source **U02280**, characters [66021, 66055): སྤྲོས་མེད་དད་ལྡན་འཇུག་སྨིན་ཕྱིར། །
  - Exact EWTS: `spros med dad ldan 'jug smin phyir/_/`
- Web line **2315**, page marker **89**: `spros med dang ldan 'jug smin phyir`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-229

Category: `textual_difference`. Alignment: `replace`.

- Source **U02282**, characters [66085, 66109): མཎྜལ་བུམ་པ་ལ་བརྟེན་ནས། །
  - Exact EWTS: `maN+Dal bum pa la brten nas/_/`
- Web line **2317**, page marker **89**: `man dal bum pa la rten nas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-230

Category: `textual_difference`. Alignment: `replace`.

- Source **U02289**, characters [66284, 66307): གལ་ཏེ་སྤྱོད་པ་མ་དག་ན། །
  - Exact EWTS: `gal te spyod pa ma dag na/_/`
- Web line **2324**, page marker **89**: `gal te spyad pa ma dag na`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-231

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02299**, characters [66570, 66587): དྲིས་ལན་ང་དྲུག་པ།
  - Exact EWTS: `dris lan nga drug pa/`
- Web: ∅ between lines 2333 and 2334.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-232

Category: `textual_difference`. Alignment: `replace`.

- Source **U02309**, characters [66861, 66897): ཚིག་བརྗོད་གྲུབ་མཐའི་རྣམ་གྲངས་ཀྱིས། །
  - Exact EWTS: `tshig brjod grub mtha'i rnam grangs kyis/_/`
- Web line **2344**, page marker **90**: `rdo rje gsang ba'i gnas gzung bya'o`
- Web line **2345**, page marker **90**: `yang ni lha dbang dga' byed nyon`
- Web line **2346**, page marker **90**: `tshig brjod grub mtha' rnam grangs kyis`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-233

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02318**, characters [67128, 67146): དྲིས་ལན་ང་བརྒྱད་པ།
  - Exact EWTS: `dris lan nga brgyad pa/`
- Web: ∅ between lines 2354 and 2355.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-234

Category: `textual_difference`. Alignment: `replace`.

- Source **U02325**, characters [67316, 67346): མཉམ་ཉིད་འདྲེས་པ་མེད་པས་སྤྱད། །
  - Exact EWTS: `mnyam nyid 'dres pa med pas spyad/_/`
- Web line **2361**, page marker **90**: `mnyam nyid 'dres pa med pas sbyang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-235

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02327**, characters [67370, 67386): དྲིས་ལན་ང་དགུ་པ།
  - Exact EWTS: `dris lan nga dgu pa/`
- Web: ∅ between lines 2362 and 2363.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-236

Category: `textual_difference`. Alignment: `replace`.

- Source **U02332**, characters [67501, 67535): ངག་ནི་བསླབ་རླབ་ཀྱང་དང་གནས་པ་དང༌། །
  - Exact EWTS: `ngag ni bslab rlab kyang dang gnas pa dang*/_/`
- Web line **2368**, page marker **91**: `ngag ni bslab dang gnas pa dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-237

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02358**, characters [68262, 68284): དྲིས་ལན་དྲུག་ཅུ་པའོ། །
  - Exact EWTS: `dris lan drug cu pa'o/_/`
- Web: ∅ between lines 2394 and 2395.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-238

Category: `textual_difference`. Alignment: `replace`.

- Source **U02366**, characters [68472, 68506): བཅུད་ཅིང་འཁྲུལ་འཁོར་སྣ་ཚོགས་དང༌། །
  - Exact EWTS: `bcud cing 'khrul 'khor sna tshogs dang*/_/`
- Web line **2402**, page marker **92**: `gcud cing 'khrul 'khor sna tshogs dang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-239

Category: `textual_difference`. Alignment: `replace`.

- Source **U02387**, characters [69108, 69142): མཆོག་དང་ཐུན་མོང་མཐའ་ཡི་དབྱེ་བའོ། །
  - Exact EWTS: `mchog dang thun mong mtha' yi dbye ba'o/_/`
- Web line **2424**, page marker **93**: `mchog dang thun mong mtha' yid bye ba'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-240

Category: `textual_difference`. Alignment: `replace`.

- Source **U02396**, characters [69372, 69403): ཕྱི་ནས་སྐྱེ་རྒྱུན་འཆད་པར་ངེས། །
  - Exact EWTS: `phyi nas skye rgyun 'chad par nges/_/`
- Web line **2433**, page marker **93**: `phyi nas skye rgyun 'chang par nges`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-241

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02402**, characters [69550, 69568): དྲིས་ལན་རེ་གཅིག་པ།
  - Exact EWTS: `dris lan re gcig pa/`
- Web: ∅ between lines 2438 and 2439.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-242

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02413**, characters [69864, 69882): དྲིས་ལན་རེ་གཉིས་པ།
  - Exact EWTS: `dris lan re gnyis pa/`
- Web: ∅ between lines 2449 and 2450.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-243

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02424**, characters [70180, 70198): དྲིས་ལན་རེ་གསུམ་པ།
  - Exact EWTS: `dris lan re gsum pa/`
- Web: ∅ between lines 2459 and 2460.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-244

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02434**, characters [70446, 70463): དྲིས་ལན་རེ་བཞི་པ།
  - Exact EWTS: `dris lan re bzhi pa/`
- Web: ∅ between lines 2468 and 2469.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-245

Category: `textual_difference`. Alignment: `replace`.

- Source **U02455**, characters [71051, 71082): གནད་བཞི་གྲོལ་བའི་གདེང་གིས་ནི། །
  - Exact EWTS: `gnad bzhi grol ba'i gdeng gis ni/_/`
- Web line **2490**, page marker **95**: `gnad bzhi gol ba'i gding gis ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-246

Category: `textual_difference`. Alignment: `replace`.

- Source **U02459**, characters [71158, 71189): ཐོས་མཐོང་གྲོལ་བའི་གནད་ཉིད་ནི། །
  - Exact EWTS: `thos mthong grol ba'i gnad nyid ni/_/`
- Web line **2494**, page marker **95**: `thos mthong gol ba'i gnad nyid ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-247

Category: `textual_difference`. Alignment: `replace`.

- Source **U02461**, characters [71223, 71257): གདེང་ཆེན་བཞི་ཡིས་དབྱིངས་སུ་སྦྱར། །
  - Exact EWTS: `gdeng chen bzhi yis dbyings su sbyar/_/`
- Web line **2496**, page marker **95**: `gding chen bzhi yis dbyings su sbyar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-248

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02463**, characters [71291, 71307): དྲིས་ལན་རེ་ལྔ་པ།
  - Exact EWTS: `dris lan re lnga pa/`
- Web: ∅ between lines 2497 and 2499.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-249

Category: `textual_difference`. Alignment: `replace`.

- Source **U02477**, characters [71699, 71731): སེམས་ཉིད་ཆོས་དང་བསྲེ་བའི་ཕྱིར། །
  - Exact EWTS: `sems nyid chos dang bsre ba'i phyir/_/`
- Web line **2512**, page marker **96**: `sems nyid chos dang sre ba'i phyir`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-250

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02481**, characters [71819, 71837): དྲིས་ལན་རེ་དྲུག་པ།
  - Exact EWTS: `dris lan re drug pa/`
- Web: ∅ between lines 2515 and 2516.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-251

Category: `textual_difference`. Alignment: `replace`.

- Source **U02484**, characters [71900, 71927): རྟག་ཏུ་འདྲིས་ན་སྤྱོད་པ་བདེ།
  - Exact EWTS: `rtag tu 'dris na spyod pa bde/`
- Web line **2518**, page marker **96**: `rtag tu 'dis na spyod pa bde`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-252

Category: `textual_difference`. Alignment: `replace`.

- Source **U02488**, characters [72012, 72042): འཁོར་བའི་གཡང་ས་རྒྱུན་བཅད་པས། །
  - Exact EWTS: `'khor ba'i g.yang sa rgyun bcad pas/_/`
- Source **U02489**, characters [72042, 72089): རྣལ་འབྱོར་ཆེན་པོའི་སྤྱོད་པའི་དྲིས་ལན་རེ་བདུན་པ།
  - Exact EWTS: `rnal 'byor chen po'i spyod pa'i dris lan re bdun pa/`
- Web line **2522**, page marker **96**: `'khor ba'i g.yang rgyun bcad pas`
- Web line **2523**, page marker **96**: `rnal 'byor chen po'i spyod pa'i`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-253

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02500**, characters [72375, 72394): དྲིས་ལན་རེ་བརྒྱད་པ།
  - Exact EWTS: `dris lan re brgyad pa/`
- Web: ∅ between lines 2534 and 2535.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-254

Category: `textual_difference`. Alignment: `replace`.

- Source **U02507**, characters [72578, 72606): ཐུབ་དྲུག་ཚད་དུ་ཕྱིན་པ་ཡིས། །
  - Exact EWTS: `thub drug tshad du phyin pa yis/_/`
- Web line **2541**, page marker **97**: `thub ngug tshad du phyin pa yis`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-255

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02510**, characters [72667, 72684): དྲིས་ལན་རེ་དགུ་པ།
  - Exact EWTS: `dris lan re dgu pa/`
- Web: ∅ between lines 2543 and 2544.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-256

Category: `textual_difference`. Alignment: `replace`.

- Source **U02522**, characters [72994, 73026): གཟི་བརྗིད་ལྡན་ཞིང་གཞོན་པའགྱུར། །
  - Exact EWTS: `gzi brjid ldan zhing gzhon pa'agyur/_/`
- Web line **2556**, page marker **98**: `gzi brjid ldan zhing gzhon par 'gyur`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-257

Category: `textual_difference`. Alignment: `replace`.

- Source **U02529**, characters [73210, 73237): མཁས་པས་རླུང་ནི་གནས་སུ་སླ། །
  - Exact EWTS: `mkhas pas rlung ni gnas su sla/_/`
- Web line **2563**, page marker **98**: `mkhas pas rlung ni gnas su sba`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-258

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02536**, characters [73407, 73425): དྲིས་ལན་བདུན་ཅུ་པ།
  - Exact EWTS: `dris lan bdun cu pa/`
- Web: ∅ between lines 2569 and 2570.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-259

Category: `textual_difference`. Alignment: `replace`.

- Source **U02546**, characters [73701, 73734): ལྟོར་བཏང་བྱུགས་པའི་མཐའ་ཡི་བྱའོ། །
  - Exact EWTS: `ltor btang byugs pa'i mtha' yi bya'o/_/`
- Source **U02547**, characters [73734, 73753): དྲིས་ལན་དོན་གཅིག་པ།
  - Exact EWTS: `dris lan don gcig pa/`
- Web line **2579**, page marker **98**: `stor btad byugs pa'i mtha' yi bya'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-260

Category: `textual_difference`. Alignment: `replace`.

- Source **U02551**, characters [73846, 73868): ཐ་མ་ལུས་ཀྱི་ཟག་པ་ཟད། །
  - Exact EWTS: `tha ma lus kyi zag pa zad/_/`
- Source **U02552**, characters [73868, 73894): ཡང་ན་བཅུད་ཕྱུང་མར་ཁུ་ནི། །
  - Exact EWTS: `yang na bcud phyung mar khu ni/_/`
- Web line **2584**, page marker **99**: `tha ma lus kyi zag pa zang`
- Web line **2585**, page marker **99**: `yang na bcud phyung mar 'khru ni`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-261

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02563**, characters [74189, 74208): དྲིས་ལན་དོན་གཉིས་པ།
  - Exact EWTS: `dris lan don gnyis pa/`
- Web: ∅ between lines 2595 and 2596.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-262

Category: `textual_difference`. Alignment: `replace`.

- Source **U02567**, characters [74294, 74325): ལུས་དང་བསྲེས་ཏེ་རླུང་གིས་སྤར། །
  - Exact EWTS: `lus dang bsres te rlung gis spar/_/`
- Web line **2599**, page marker **99**: `lus dang bsres te rlung gis sbar`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-263

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02576**, characters [74568, 74591): དྲིས་ལན་དོན་གསུམ་པའོ། །
  - Exact EWTS: `dris lan don gsum pa'o/_/`
- Web: ∅ between lines 2608 and 2609.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-264

Category: `textual_difference`. Alignment: `replace`.

- Source **U02582**, characters [74747, 74778): མཛོད་ལ་སྤྱོད་པས་ངེས་པར་འགྲུབ། །
  - Exact EWTS: `mdzod la spyod pas nges par 'grub/_/`
- Web line **2614**, page marker **100**: `mdzod la spyod pas nges pas 'grub`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-265

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02584**, characters [74807, 74825): དྲིས་ལན་དོན་བཞི་པ།
  - Exact EWTS: `dris lan don bzhi pa/`
- Web: ∅ between lines 2615 and 2616.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-266

Category: `textual_difference`. Alignment: `replace`.

- Source **U02596**, characters [75168, 75194): ངེས་པར་འགྲུབ་པར་འགྱུར་བའོ།
  - Exact EWTS: `nges par 'grub par 'gyur ba'o/`
- Source **U02597**, characters [75194, 75206): ལན་དོན་ལྔ་པ།
  - Exact EWTS: `lan don lnga pa/`
- Source **U02598**, characters [75206, 75236): མི་འཛད་གཏེར་ལ་སྤྱོད་འདོད་པས། །
  - Exact EWTS: `mi 'dzad gter la spyod 'dod pas/_/`
- Web line **2627**, page marker **100**: `nges par 'grub par 'gyur pa'o`
- Web line **2628**, page marker **100**: `mi mdzad gter la spyod 'dod pas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-267

Category: `textual_difference`. Alignment: `replace`.

- Source **U02605**, characters [75419, 75452): གང་འདོད་བརྩམ་པའི་ལས་རྣམས་འགྲུབ། །
  - Exact EWTS: `gang 'dod brtsam pa'i las rnams 'grub/_/`
- Web line **2636**, page marker **101**: `gang 'dod brtsams pa'i las rnams 'grub`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-268

Category: `textual_difference`. Alignment: `replace`.

- Source **U02607**, characters [75477, 75510): བསྙེན་བསྒྲུབ་ལས་ཀྱི་མཐའ་ཕྱེ་བས། །
  - Exact EWTS: `bsnyen bsgrub las kyi mtha' phye bas/_/`
- Web line **2638**, page marker **101**: `bsnyen sgrub las kyi mtha' phye bas`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-269

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02610**, characters [75571, 75590): དྲིས་ལན་དོན་དྲུག་པ།
  - Exact EWTS: `dris lan don drug pa/`
- Web: ∅ between lines 2640 and 2641.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-270

Category: `textual_difference`. Alignment: `replace`.

- Source **U02615**, characters [75716, 75733): མདོག་གི་ཡང་བྱུང་།
  - Exact EWTS: `mdog gi yang byung /`
- Source **U02616**, characters [75733, 75765): སྤྲོ་བསྡུ་བསྟིམ་འཁྱིལ་པས་བྱའོ། །
  - Exact EWTS: `spro bsdu bstim 'khyil pas bya'o/_/`
- Web line **2645**, page marker **101**: `ba spro bsdu bstim 'khyil pas bya'o`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-271

Category: `source_heading_or_label_absent_in_web_transcription`. Alignment: `delete`.

- Source **U02620**, characters [75856, 75880): དེ་དག་གི་ཞབས་སྡུད་པའོ། །
  - Exact EWTS: `de dag gi zhabs sdud pa'o/_/`
- Web: ∅ between lines 2648 and 2649.

**Provisional comparison disposition and reason:** Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.

### W-C01-272

Category: `textual_difference`. Alignment: `replace`.

- Source **U02626**, characters [76023, 76050): སྐལ་བ་བཟང་པོ་རྣམས་ལ་སྣང་། །
  - Exact EWTS: `skal ba bzang po rnams la snang /_/`
- Web line **2654**, page marker **101**: `skal pa bzang po rnams la snang`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

### W-C01-273

Category: `textual_difference`. Alignment: `replace`.

- Source **U02629**, characters [76107, 76136): ལུས་གུས་ཐལ་མོ་ལེགས་སྦྱར་ཏེ། །
  - Exact EWTS: `lus gus thal mo legs sbyar te/_/`
- Web line **2657**, page marker **101**: `lus tus thal mo legs sbyar te`

**Provisional comparison disposition and reason:** Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.

## Nonlexical source signs preserved outside alignment

The source `༌`/EWTS `*` occurs in the following 177 chapter units. Its removal from matching strings does not delete it from the source or adopted text. The JSON preserves the complete Tibetan and EWTS for each occurrence.

`U00065`, `U00111`, `U00128`, `U00130`, `U00153`, `U00156`, `U00198`, `U00203`, `U00205`, `U00216`, `U00219`, `U00224`, `U00228`, `U00231`, `U00239`, `U00257`, `U00273`, `U00324`, `U00332`, `U00334`, `U00348`, `U00352`, `U00399`, `U00406`, `U00428`, `U00429`, `U00437`, `U00478`, `U00479`, `U00481`, `U00482`, `U00483`, `U00485`, `U00488`, `U00499`, `U00507`, `U00522`, `U00531`, `U00555`, `U00563`, `U00564`, `U00574`, `U00626`, `U00633`, `U00644`, `U00688`, `U00697`, `U00704`, `U00708`, `U00709`, `U00760`, `U00761`, `U00779`, `U00799`, `U00858`, `U00866`, `U00878`, `U00895`, `U00922`, `U00959`, `U00985`, `U01027`, `U01037`, `U01073`, `U01075`, `U01127`, `U01172`, `U01174`, `U01176`, `U01180`, `U01183`, `U01187`, `U01195`, `U01197`, `U01201`, `U01216`, `U01226`, `U01230`, `U01240`, `U01252`, `U01254`, `U01258`, `U01273`, `U01306`, `U01351`, `U01407`, `U01411`, `U01433`, `U01436`, `U01497`, `U01500`, `U01508`, `U01543`, `U01548`, `U01549`, `U01552`, `U01553`, `U01554`, `U01562`, `U01565`, `U01567`, `U01571`, `U01594`, `U01602`, `U01609`, `U01631`, `U01637`, `U01648`, `U01695`, `U01711`, `U01713`, `U01715`, `U01717`, `U01718`, `U01720`, `U01731`, `U01735`, `U01774`, `U01784`, `U01785`, `U01789`, `U01793`, `U01797`, `U01809`, `U01820`, `U01824`, `U01833`, `U01838`, `U01839`, `U01843`, `U01846`, `U01866`, `U01874`, `U01895`, `U01930`, `U01944`, `U01949`, `U01955`, `U01956`, `U01962`, `U01982`, `U01988`, `U01996`, `U02001`, `U02041`, `U02044`, `U02048`, `U02175`, `U02206`, `U02216`, `U02234`, `U02237`, `U02242`, `U02246`, `U02263`, `U02278`, `U02332`, `U02336`, `U02361`, `U02366`, `U02367`, `U02388`, `U02415`, `U02416`, `U02420`, `U02446`, `U02467`, `U02485`, `U02502`, `U02540`, `U02541`, `U02556`, `U02557`, `U02588`, `U02593`, `U02594`, `U02617`

Ornamental-only source units:

- U00001: `༅།` / EWTS `#/`.
- U00003: `༄༅།` / EWTS `@#/`.

## Input checksums

| File | SHA-256 |
| --- | --- |
| `editions/adzom-wikisource/source.wikitext` | `d2a6e95e8c65d28d7812efa79d65bd397a0796a9e00621430a86b5713b70ede8` |
| `editions/adzom-wikisource/sgra-thal-gyur.wikitext` | `d2a6e95e8c65d28d7812efa79d65bd397a0796a9e00621430a86b5713b70ede8` |
| `source/W1KG11703_7.txt` | `18bd9ce65311e2d6d7c703f053a5c0aac347e899a75f8749a8f9afd891452edc` |
| `translations/2026-09-26-full-draft/data/source-units.json` | `c8f1f0f8b91217a929cb82b0a5bb4544f8d29edddb145687f47218f05f0ceb5b` |

Companion machine-readable files: `wikisource-ch1-diffs.json` has all 273 lexical conflicts; `wikisource-ch1-raw-ledger.json` preserves every exact web line 1–2664 including its newline, all source units U00001–U02635, and the full lexical alignment. All web wrappers, markers, annotations, whitespace and punctuation survive in this ledger. Reproduction scripts: `collate_wikisource_ch1.py` and `make_wikisource_report.py`. Source and edition inputs were not changed by this comparison.
