# Chapter 4 — related Wikisource reference comparison

**Release candidate — final gate pending**

W is the stored related Wylie transcription, not an independent printing. All 55 non-equal alignment blocks have explicit decisions. Exact original W lines and source Wylie remain quoted; stripped signs and collapsed spaces were used for alignment only.

[Stored provenance](../../../editions/adzom-wikisource/PROVENANCE.json) · [Reading](reading.md) · [Apparatus](apparatus.md)

Attribution: Wikisource revision 439571 and its contributor history, retained in the provenance file. The related text retains its applicable attribution/share-alike terms; this edition grants no additional rights.

<a id="w-c04-001"></a>
## W-C04-001 — U04314

**Original A Tibetan:**
```json
[
  "སངས་རྒྱས་དགོངས་པའི་གདེང་རྙེད་ཀྱང༌། །"
]
```

**Original A Wylie:**
```json
[
  "sangs rgyas dgongs pa'i gdeng rnyed kyang*/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4358,
    "raw": "sangs rgyas dgongs pa'i gding rnyed kyang\n",
    "page_marker": 163,
    "start": 136787,
    "end": 136829
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "gdeng",
    "W": "gding"
  }
]
```

**Decision:** Retain U04314 gdeng rather than W gding. Preserve the vowel distinction without normalizing confidence terminology from the related website.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-002"></a>
## W-C04-002 — U04325

**Original A Tibetan:**
```json
[
  "ཡུལ་ལ་སྣང་བའི་མཚན་ཉིད་གང༌། །"
]
```

**Original A Wylie:**
```json
[
  "yul la snang ba'i mtshan nyid gang*/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4370,
    "raw": "yul la snang ba'i mtshan nyid glang\n",
    "page_marker": 164,
    "start": 137155,
    "end": 137191
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "gang",
    "W": "glang"
  }
]
```

**Decision:** Retain U04325 gang rather than W glang. The added W la is quoted as reference text, not adopted or assumed to appear in a printed exemplar.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-003"></a>
## W-C04-003 — between U04328 and U04329

**Original A Tibetan:**
```json
[]
```

**Original A Wylie:**
```json
[]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4374,
    "raw": "tshad phebs lus ni ci ltar 'gyur\n",
    "page_marker": 164,
    "start": 137288,
    "end": 137321
  },
  {
    "line": 4375,
    "raw": "sems ni gang dang gang lta bu\n",
    "page_marker": 164,
    "start": 137321,
    "end": 137351
  },
  {
    "line": 4376,
    "raw": "'brel ba chod pa'i chos nyid gang\n",
    "page_marker": 164,
    "start": 137351,
    "end": 137385
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "insert",
    "A": "",
    "W": "tshad phebs lus ni ci ltar 'gyur sems ni gang dang gang lta bu 'brel ba chod pa'i chos nyid gang"
  }
]
```

**Decision:** Include A2000-C04-S01, the three scan-supported main question verses after U04328. W corroborates their presence, but its brel ba spelling does not override the adopted source spelling brel pa. The restoration rests on native PDF164, not website authority.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-004"></a>
## W-C04-004 — U04344

**Original A Tibetan:**
```json
[
  " ཞུས་དོན་དང་པོ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus don dang po/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus don dang po",
    "W": ""
  }
]
```

**Decision:** Keep U04344 zhus don dang po as a heading. Its absence in W does not authorize removing the source label; the targeted native boundary supports its separate role.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-005"></a>
## W-C04-005 — U04350

**Original A Tibetan:**
```json
[
  "ཞུས་དོན་གཉིས་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus don gnyis pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus don gnyis pa",
    "W": ""
  }
]
```

**Decision:** Keep the second zhus don heading U04350 although W omits it. Do not count this reference omission as a missing main verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-006"></a>
## W-C04-006 — U04364

**Original A Tibetan:**
```json
[
  "དེ་བསྡོམས་གསུམ་ལ་སྦོམ་པོ་ཉིད། །"
]
```

**Original A Wylie:**
```json
[
  "de bsdoms gsum la sbom po nyid/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4411,
    "raw": "de bsdoms gsum la spom po nyid\n",
    "page_marker": 165,
    "start": 138449,
    "end": 138480
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "sbom",
    "W": "spom"
  }
]
```

**Decision:** Retain U04364 sbom rather than W spom, preserving the root-letter difference in the exact reference quotation without a new glyph claim.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-007"></a>
## W-C04-007 — U04368

**Original A Tibetan:**
```json
[
  "ཞུས་དོན་གསུམ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus don gsum pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus don gsum pa",
    "W": ""
  }
]
```

**Decision:** Keep U04368 as the third zhus don heading. W omission is not evidence that the Adzom printing lacks its label.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-008"></a>
## W-C04-008 — U04378

**Original A Tibetan:**
```json
[
  "ཞུས་དོན་བཞི་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus don bzhi pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus don bzhi pa",
    "W": ""
  }
]
```

**Decision:** Keep U04378 as the fourth source heading; do not delete it solely to match the heading-light website transcription.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-009"></a>
## W-C04-009 — U04390

**Original A Tibetan:**
```json
[
  "ཞུས་དོན་ལྔ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus don lnga pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus don lnga pa",
    "W": ""
  }
]
```

**Decision:** Keep the fifth heading U04390 separately from main verse. The absent W label remains a reference-level omission, not a collated printed-witness omission.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-010"></a>
## W-C04-010 — U04398

**Original A Tibetan:**
```json
[
  "ཟང་མ་ཉིད་དང་ཐལ་བྱུང་དུ། །"
]
```

**Original A Wylie:**
```json
[
  "zang ma nyid dang thal byung du/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4443,
    "raw": "zad ma nyid dang thal byung du\n",
    "page_marker": 166,
    "start": 139398,
    "end": 139429
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "zang",
    "W": "zad"
  }
]
```

**Decision:** Retain U04398 zang ma rather than W zad ma. Do not recast the phrase as a familiar compound or infer a corrected syllable from semantic expectation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-011"></a>
## W-C04-011 — U04406

**Original A Tibetan:**
```json
[
  "ཞུས་དོན་དྲུག་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus don drug pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus don drug pa",
    "W": ""
  }
]
```

**Decision:** Keep U04406 as the sixth zhus don heading. W omission does not convert its source wording into editorial invention.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-012"></a>
## W-C04-012 — U04408

**Original A Tibetan:**
```json
[
  "སྤྱི་དང་ཙིཏྟ་རྩ་ཡི་གནད། །"
]
```

**Original A Wylie:**
```json
[
  "spyi dang tsit+ta rtsa yi gnad/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4453,
    "raw": "spyi dang tsit ta rtsa yi gnad\n",
    "page_marker": 167,
    "start": 139679,
    "end": 139710
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "tsit+ta",
    "W": "tsit ta"
  }
]
```

**Decision:** Retain the original Tibetan tsitta spelling at U04408. EWTS tsit+ta versus plain W tsit ta is a romanization distinction, not proof of a different printed stack.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-013"></a>
## W-C04-013 — U04415

**Original A Tibetan:**
```json
[
  "ཙིཏྟའི་ནང་ན་སྐུར་གནས་ཏེ། །"
]
```

**Original A Wylie:**
```json
[
  "tsit+ta'i nang na skur gnas te/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4460,
    "raw": "tsit ta'i nang na skur gnas te\n",
    "page_marker": 167,
    "start": 139907,
    "end": 139938
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "tsit+ta'i",
    "W": "tsit ta'i"
  }
]
```

**Decision:** Preserve U04415 tsittai; W tsit tai spacing lacks the explicit EWTS stack syntax. Do not back-convert it into a new Tibetan reading.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-014"></a>
## W-C04-014 — U04426

**Original A Tibetan:**
```json
[
  "འཁོར་འདས་འབྲེལ་པའི་ས་བོན་འདེབས། །"
]
```

**Original A Wylie:**
```json
[
  "'khor 'das 'brel pa'i sa bon 'debs/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4471,
    "raw": "'khor 'das 'brel ba'i sa bon 'debs\n",
    "page_marker": 167,
    "start": 140267,
    "end": 140302
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "pa'i",
    "W": "ba'i"
  }
]
```

**Decision:** Retain U04426 brel pai rather than W brel bai. Both exact forms remain; pa/ba is not globally normalized.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-015"></a>
## W-C04-015 — U04428

**Original A Tibetan:**
```json
[
  "རྣལ་འབྱོར་ཉམས་ཀྱི་དཀྱིལ་འཁོར་འཇོག །"
]
```

**Original A Wylie:**
```json
[
  "rnal 'byor nyams kyi dkyil 'khor 'jog_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4473,
    "raw": "rnal 'byor nyams kyis dkyil 'khor 'jog\n",
    "page_marker": 167,
    "start": 140335,
    "end": 140374
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "kyi",
    "W": "kyis"
  }
]
```

**Decision:** Retain U04428 nyams kyi rather than W nyams kyis. The final sa changes grammatical presentation but is not adopted without source evidence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-016"></a>
## W-C04-016 — U04433

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བདུན་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bdun pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bdun pa",
    "W": ""
  }
]
```

**Decision:** Keep U04433 zhus lan bdun pa, preserving the change from earlier zhus don labels. W omission is not a reason to regularize or delete it.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-017"></a>
## W-C04-017 — U04443

**Original A Tibetan:**
```json
[
  "གཡོན་པས་འཛིན་པས་ཁ་དོག་རྫོགས། །"
]
```

**Original A Wylie:**
```json
[
  "g.yon pas 'dzin pas kha dog rdzogs/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4488,
    "raw": "g.yon pas 'dzin pas kha dog dzogs\n",
    "page_marker": 168,
    "start": 140794,
    "end": 140828
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "rdzogs",
    "W": "dzogs"
  }
]
```

**Decision:** Retain U04443 rdzogs, not W dzogs. Preserve the reference spelling without adding its missing prefix to the quotation or removing it from Adzom.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-018"></a>
## W-C04-018 — U04446

**Original A Tibetan:**
```json
[
  "གཡོན་པས་འཇུག་པ་རླུང་གི་ལས། །"
]
```

**Original A Wylie:**
```json
[
  "g.yon pas 'jug pa rlung gi las/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4491,
    "raw": "g.yon pas 'jug pa lung gi las\n",
    "page_marker": 168,
    "start": 140897,
    "end": 140927
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "rlung",
    "W": "lung"
  }
]
```

**Decision:** Retain U04446 rlung against W lung. No independent printed-witness evidence follows from the related website alone.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-019"></a>
## W-C04-019 — U04448

**Original A Tibetan:**
```json
[
  "སྤྱི་གཙུག་ཁྱབ་པར་རྫོགས་པའི་རླུང༌། །"
]
```

**Original A Wylie:**
```json
[
  "spyi gtsug khyab par rdzogs pa'i rlung*/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4493,
    "raw": "spyi gtsug khyab par rdzogs pa'i lung\n",
    "page_marker": 168,
    "start": 140963,
    "end": 141001
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "rlung",
    "W": "lung"
  }
]
```

**Decision:** Keep U04448 rlung, not W lung. The reference omission of the initial ra remains explicit without changing the selected source.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-020"></a>
## W-C04-020 — U04451

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་བརྒྱད་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan brgyad pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan brgyad pa",
    "W": ""
  }
]
```

**Decision:** Keep the eighth zhus lan heading U04451; its absent W counterpart is not a main-text restoration or a reason for deletion.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-021"></a>
## W-C04-021 — U04462

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་དགུ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan dgu pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan dgu pa",
    "W": ""
  }
]
```

**Decision:** Keep the ninth heading U04462. Preserve its source position between the main clauses rather than flattening it into W agreement.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-022"></a>
## W-C04-022 — U04466

**Original A Tibetan:**
```json
[
  "བརྩམས་ཏེ་ལུས་ངག་གནད་གཟིར་བས། །"
]
```

**Original A Wylie:**
```json
[
  "brtsams te lus ngag gnad gzir bas/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4510,
    "raw": "brtsams te lus dga gnad gzir bas\n",
    "page_marker": 169,
    "start": 141484,
    "end": 141517
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "ngag",
    "W": "dga"
  }
]
```

**Decision:** Retain U04466 ngag rather than W dga. Record the whole phrase exactly and make no conjectural reordering of the website letters.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-023"></a>
## W-C04-023 — U04476

**Original A Tibetan:**
```json
[
  "པདྨའི་སྤྱན་གྱིས་མཐོང་བར་འགྱུར། །"
]
```

**Original A Wylie:**
```json
[
  "pad+ma'i spyan gyis mthong bar 'gyur/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4520,
    "raw": "pad ma'i spyan gyis mthong bar 'gyur\n",
    "page_marker": 169,
    "start": 141834,
    "end": 141871
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "pad+ma'i",
    "W": "pad ma'i"
  }
]
```

**Decision:** Retain U04476 padmai. EWTS pad+mai and W pad mai differ in stack notation; neither establishes an independent Sanskrit normalization.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-024"></a>
## W-C04-024 — U04484

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅུ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bcu pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu pa",
    "W": ""
  }
]
```

**Decision:** Keep the tenth reply label U04484 despite its absence in W. The main clause that follows remains separate.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-025"></a>
## W-C04-025 — U04486

**Original A Tibetan:**
```json
[
  "སྣང་བ་འཁྲིད་པའི་ཐབས་ཀྱིས་ཀྱང་། །"
]
```

**Original A Wylie:**
```json
[
  "snang ba 'khrid pa'i thabs kyis kyang /_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4529,
    "raw": "snang ba 'khrid pa'i thabs kyi kyang\n",
    "page_marker": 169,
    "start": 142145,
    "end": 142182
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "kyis",
    "W": "kyi"
  }
]
```

**Decision:** Retain U04486 thabs kyis rather than W thabs kyi; do not silently remove the source suffix to smooth grammar.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-026"></a>
## W-C04-026 — U04492

**Original A Tibetan:**
```json
[
  "ཕྲ་ཞིང་དྲང་ལ་མཉེ་བ་ཡིས། །"
]
```

**Original A Wylie:**
```json
[
  "phra zhing drang la mnye ba yis/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4536,
    "raw": "phra zhing drang lam nye ba yis\n",
    "page_marker": 170,
    "start": 142360,
    "end": 142392
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "la mnye",
    "W": "lam nye"
  }
]
```

**Decision:** Retain U04492 la mnye rather than W lam nye. The different word boundary and prefix allocation remain recorded without a mechanical respelling of Tibetan.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-027"></a>
## W-C04-027 — U04494

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅུ་གཅིག་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bcu gcig pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu gcig pa",
    "W": ""
  }
]
```

**Decision:** Keep the eleventh heading U04494. Its absent website label does not alter the selected root sequence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-028"></a>
## W-C04-028 — U04496

**Original A Tibetan:**
```json
[
  "ཐད་ཀའི་ངོས་སྣང་འགགས་པ་དང་། །"
]
```

**Original A Wylie:**
```json
[
  "thad ka'i ngos snang 'gags pa dang /_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4539,
    "raw": "thad ka'i ngos snang 'gegs pa dang\n",
    "page_marker": 170,
    "start": 142459,
    "end": 142494
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "'gags",
    "W": "'gegs"
  }
]
```

**Decision:** Retain U04496 gags against W gegs. The vowel difference is preserved without claiming it has been settled from a fresh image reading.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-029"></a>
## W-C04-029 — U04503

**Original A Tibetan:**
```json
[
  "དེ་ལ་ཡབ་ཡུམ་འཁྲིལ་པ་དང་། །"
]
```

**Original A Wylie:**
```json
[
  "de la yab yum 'khril pa dang /_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4546,
    "raw": "de la yab yum 'khrul ba dang\n",
    "page_marker": 170,
    "start": 142694,
    "end": 142723
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "'khril pa",
    "W": "'khrul ba"
  }
]
```

**Decision:** Retain U04503 khril pa rather than W khrul ba. Both the vowel and pa/ba difference remain explicit, without selecting a more familiar expression.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-030"></a>
## W-C04-030 — U04509

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅུ་གཉིས་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bcu gnyis pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu gnyis pa",
    "W": ""
  }
]
```

**Decision:** Keep U04509 as the twelfth reply heading; its absence in W does not warrant omitting the Adzom label.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-031"></a>
## W-C04-031 — U04514, U04515

**Original A Tibetan:**
```json
[
  "ཕྲ་ཞིང་འཁྲིལ་པས་སྣང་བ་འཛིན། །",
  "ལུས་ཀྱི་རྡོས་པ་རང་འགགས་ནས། །"
]
```

**Original A Wylie:**
```json
[
  "phra zhing 'khril pas snang ba 'dzin/_/",
  "lus kyi rdos pa rang 'gags nas/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4556,
    "raw": "phra zhing 'khril bas snang ba 'dzin\n",
    "page_marker": 170,
    "start": 143025,
    "end": 143062
  },
  {
    "line": 4557,
    "raw": "lus kyi rdos ba rang 'gags nas\n",
    "page_marker": 170,
    "start": 143062,
    "end": 143093
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "pas",
    "W": "bas"
  },
  {
    "op": "replace",
    "A": "pa",
    "W": "ba"
  }
]
```

**Decision:** Retain U04514 khril pas and U04515 rdos pa rather than the W bas/ba forms. These are preserved orthographic differences, not authority for global normalization.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-032"></a>
## W-C04-032 — U04519

**Original A Tibetan:**
```json
[
  "ཐོར་ཚུགས་རླུང་གིས་འགེག་འདེགས་ཀྱང་བྱུང་པར་སྣང༌། །"
]
```

**Original A Wylie:**
```json
[
  "thor tshugs rlung gis 'geg 'degs kyang byung par snang*/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4562,
    "raw": "thor tshugs rlung gis 'geg par snang\n",
    "page_marker": 171,
    "start": 143191,
    "end": 143228
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "'degs kyang byung",
    "W": ""
  }
]
```

**Decision:** Accept the scan-supported main ageg par snang at U04519 while keeping adegs kyang byung as the separately preserved smaller note. W omits that note; the role decision rests on native layout, and the note-letter uncertainty remains.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-033"></a>
## W-C04-033 — U04521

**Original A Tibetan:**
```json
[
  "འོད་ཀྱི་ཕྲེང་བ་རྣམ་པར་འཁྲིགས། །"
]
```

**Original A Wylie:**
```json
[
  "'od kyi phreng ba rnam par 'khrigs/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4564,
    "raw": "'od kyi phreng bar rnam par 'khrigs\n",
    "page_marker": 171,
    "start": 143256,
    "end": 143292
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "ba",
    "W": "bar"
  }
]
```

**Decision:** Retain U04521 phreng ba rather than W phreng bar. The W suffix remains quoted without being imported into the base.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-034"></a>
## W-C04-034 — U04525

**Original A Tibetan:**
```json
[
  "འདི་དུས་རང་ལུས་ཚད་ལ་ཕབས། །"
]
```

**Original A Wylie:**
```json
[
  "'di dus rang lus tshad la phabs/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4568,
    "raw": "'di dus rang las tshad la phebs\n",
    "page_marker": 171,
    "start": 143386,
    "end": 143418
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "lus",
    "W": "las"
  },
  {
    "op": "replace",
    "A": "phabs",
    "W": "phebs"
  }
]
```

**Decision:** Retain U04525 rang lus and phabs, against W rang las and phebs. The latter shares its vowel with B/S, but transcript agreement is not a source correction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-035"></a>
## W-C04-035 — U04527

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅུ་གསུམ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bcu gsum pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu gsum pa",
    "W": ""
  }
]
```

**Decision:** Keep the thirteenth source heading U04527 although W has no label. Do not count its absence as a missing root clause.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-036"></a>
## W-C04-036 — U04529, U04530

**Original A Tibetan:**
```json
[
  "མངོན་པར་ཤེས་པ་དྲུག་རྣམས་དང༌། །",
  "རིང་དང་དཔག་ཏུ་གྱུར་པ་ཡི། །"
]
```

**Original A Wylie:**
```json
[
  "mngon par shes pa drug rnams dang*/_/",
  "ring dang dpag tu gyur pa yi/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4571,
    "raw": "mngon pa shes pa drug rnams dang\n",
    "page_marker": 171,
    "start": 143484,
    "end": 143517
  },
  {
    "line": 4572,
    "raw": "rang dang dpag tu gyur pa yi\n",
    "page_marker": 171,
    "start": 143517,
    "end": 143546
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "par",
    "W": "pa"
  },
  {
    "op": "replace",
    "A": "ring",
    "W": "rang"
  }
]
```

**Decision:** Retain U04529 mngon par and U04530 ring. W mngon pa and rang remain exact reference readings; neither lost suffix nor changed vowel is adopted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-037"></a>
## W-C04-037 — U04539

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅུ་བཞི་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bcu bzhi pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu bzhi pa",
    "W": ""
  }
]
```

**Decision:** Keep U04539 as the fourteenth heading, without importing its absence in the website into the base.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-038"></a>
## W-C04-038 — U04557

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་བཅོ་ལྔ་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan bco lnga pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bco lnga pa",
    "W": ""
  }
]
```

**Decision:** Keep the fifteenth heading U04557 and its exact source wording. W omission does not prove a printed omission.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-039"></a>
## W-C04-039 — U04562

**Original A Tibetan:**
```json
[
  "རླུ་ལས་བྱུང་བའི་ཆོས་ཉིད་དོ། །"
]
```

**Original A Wylie:**
```json
[
  "rlu las byung ba'i chos nyid do/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4603,
    "raw": "rlung las byung ba'i chos nyid do\n",
    "page_marker": 172,
    "start": 144507,
    "end": 144541
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "rlu",
    "W": "rlung"
  }
]
```

**Decision:** Retain U04562 rlu with its explicit source-reading uncertainty. W supplies rlung, but the bounded native inspection did not securely establish adding nga. Do not convert that reference suggestion into a resolved correction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-040"></a>
## W-C04-040 — U04564

**Original A Tibetan:**
```json
[
  "གཅིག་དང་དུ་མའི་གྲངས་ཟད་དེ། །"
]
```

**Original A Wylie:**
```json
[
  "gcig dang du ma'i grangs zad de/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4605,
    "raw": "gcig dang du ma'i gangs zad de\n",
    "page_marker": 172,
    "start": 144571,
    "end": 144602
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "grangs",
    "W": "gangs"
  }
]
```

**Decision:** Retain U04564 grangs rather than W gangs. Preserve the missing W ra as a reference difference, not a silent change to the number clause.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-041"></a>
## W-C04-041 — U04568

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་བཅུ་དྲུག་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan bcu drug pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu drug pa",
    "W": ""
  }
]
```

**Decision:** Keep the sixteenth heading U04568. It remains a distinct heading despite its absence in the related W transcription.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-042"></a>
## W-C04-042 — U04573

**Original A Tibetan:**
```json
[
  "ཉོན་མོངས་དེངས་པས་འཁྲུལ་པ་དེངས། །"
]
```

**Original A Wylie:**
```json
[
  "nyon mongs dengs pas 'khrul pa dengs/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4613,
    "raw": "nyon mongs dengs pas 'khrul pa dwangs\n",
    "page_marker": 172,
    "start": 144830,
    "end": 144868
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "dengs",
    "W": "dwangs"
  }
]
```

**Decision:** Retain final dengs in U04573 rather than W dwangs or B dangs. Keep all three source-specific forms visible without selecting a more expected predicate.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-043"></a>
## W-C04-043 — U04579

**Original A Tibetan:**
```json
[
  "འབྱུང་བ་བཞི་ཡི་ལུས་ཟད་ནས། །"
]
```

**Original A Wylie:**
```json
[
  "'byung ba bzhi yi lus zad nas/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4620,
    "raw": "'byung ba bzhi yi lus brang nas\n",
    "page_marker": 173,
    "start": 145029,
    "end": 145061
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "zad",
    "W": "brang"
  }
]
```

**Decision:** Retain U04579 zad, not W brang. Do not rewrite the exhausted-body clause from the unrelated-looking reference word or silently repair that quotation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-044"></a>
## W-C04-044 — U04584

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅུ་བདུན་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bcu bdun pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu bdun pa",
    "W": ""
  }
]
```

**Decision:** Keep the seventeenth heading U04584. The absence in W changes neither its source role nor its position.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-045"></a>
## W-C04-045 — U04594

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅོ་བརྒྱད་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bco brgyad pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bco brgyad pa",
    "W": ""
  }
]
```

**Decision:** Keep the eighteenth heading U04594 despite the heading omission in W. The root clause remains separate from the label.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-046"></a>
## W-C04-046 — U04601

**Original A Tibetan:**
```json
[
  "དངོས་གཞི་གནས་ལ་བསྒྱུར་བ་ཡིས། །"
]
```

**Original A Wylie:**
```json
[
  "dngos gzhi gnas la bsgyur ba yis/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4640,
    "raw": "dngos gzhi gnas la sbyar ba yis\n",
    "page_marker": 173,
    "start": 145663,
    "end": 145695
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "bsgyur",
    "W": "sbyar"
  }
]
```

**Decision:** Retain U04601 bsgyur rather than W sbyar. Both readings are recorded, without deciding the source from an interpretive preference for transformation or joining.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-047"></a>
## W-C04-047 — U04608

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཅུ་དགུ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bcu dgu pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu dgu pa",
    "W": ""
  }
]
```

**Decision:** Keep the nineteenth heading U04608. The missing website label is not evidence for removing the printed-source heading.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-048"></a>
## W-C04-048 — U04620

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་ཉི་ཤུ་ཐམ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan nyi shu tham pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan nyi shu tham pa",
    "W": ""
  }
]
```

**Decision:** Preserve the full twentieth heading nyi shu tham pa at U04620. Do not abbreviate it or drop it to match W.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-049"></a>
## W-C04-049 — U04645

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་ཉེར་གཅིག་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan nyer gcig pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan nyer gcig pa",
    "W": ""
  }
]
```

**Decision:** Keep the twenty-first heading U04645 as source structure. W omission is explicitly reference-level evidence, not manuscript collation credit.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-050"></a>
## W-C04-050 — U04669

**Original A Tibetan:**
```json
[
  "ཐག་ཆོད་པས་ནི་གདེང་དུ་ཚུད། །"
]
```

**Original A Wylie:**
```json
[
  "thag chod pas ni gdeng du tshud/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4708,
    "raw": "thag chod pas ni gding du tshud\n",
    "page_marker": 176,
    "start": 147759,
    "end": 147791
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "gdeng",
    "W": "gding"
  }
]
```

**Decision:** Retain U04669 gdeng against W gding, without normalizing its vowel to a preferred terminology spelling.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-051"></a>
## W-C04-051 — U04694

**Original A Tibetan:**
```json
[
  "འཛིན་པ་མེད་པའི་སེམས་ཤར་བ། །"
]
```

**Original A Wylie:**
```json
[
  "'dzin pa med pa'i sems shar ba/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4734,
    "raw": "'dzin pa'i med pa'i sems shar ba\n",
    "page_marker": 177,
    "start": 148565,
    "end": 148598
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "pa",
    "W": "pa'i"
  }
]
```

**Decision:** Retain U04694 dzin pa med pai rather than W dzin pai med pai. The extra W genitive remains quoted; it does not authorize a change to the source syntax.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-052"></a>
## W-C04-052 — U04703

**Original A Tibetan:**
```json
[
  "བྱ་ལམ་ནམ་མཁར་འགྲོ་བ་བཞིན། ། །"
]
```

**Original A Wylie:**
```json
[
  "bya lam nam mkhar 'gro ba bzhin/_/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4743,
    "raw": "bya lam nam mkha' 'gro ba bzhin\n",
    "page_marker": 177,
    "start": 148863,
    "end": 148895
  },
  {
    "line": 4744,
    "raw": "chos\n",
    "page_marker": 177,
    "start": 148895,
    "end": 148900
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "mkhar",
    "W": "mkha'"
  },
  {
    "op": "insert",
    "A": "",
    "W": "chos"
  }
]
```

**Decision:** Retain U04703 nam mkhar and its explicitly qualified supplied punctuation. W has nam mkha and an isolated following line chos. Preserve that W line and its position; do not insert chos as root text or claim it is a source omission without a corresponding scan finding.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-053"></a>
## W-C04-053 — U04706

**Original A Tibetan:**
```json
[
  "འཁྲུལ་པར་སྣང་བའི་རྒྱུ་རྐྱེན་ཟད། །"
]
```

**Original A Wylie:**
```json
[
  "'khrul par snang ba'i rgyu rkyen zad/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4747,
    "raw": "'khrul pa snang ba'i rgyu rkyen thad\n",
    "page_marker": 177,
    "start": 148966,
    "end": 149003
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "par",
    "W": "pa"
  },
  {
    "op": "replace",
    "A": "zad",
    "W": "thad"
  }
]
```

**Decision:** Retain U04706 khrul par and zad rather than W khrul pa and thad. Preserve both reference changes without semantic or orthographic repair.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-054"></a>
## W-C04-054 — U04709

**Original A Tibetan:**
```json
[
  "རིག་པའི་ངོ་བོ་ལུ་གུ་རྒྱུད། །"
]
```

**Original A Wylie:**
```json
[
  "rig pa'i ngo bo lu gu rgyud/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4750,
    "raw": "rig pa'i ro bo lu gu rgyud\n",
    "page_marker": 177,
    "start": 149070,
    "end": 149097
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "ngo",
    "W": "ro"
  }
]
```

**Decision:** Retain U04709 ngo bo, not W ro bo. The reference spelling stays exact and is not used to replace the Adzom initial syllable.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)

<a id="w-c04-055"></a>
## W-C04-055 — U04763

**Original A Tibetan:**
```json
[
  " ཆོས་ཉིད་བཀོད་པ་སེམས་སྣང་གི་རྩ་བ་བསྟན་པའི་ལེའུ་སྟེ་བཞི་པའོ།། །།"
]
```

**Original A Wylie:**
```json
[
  "_chos nyid bkod pa sems snang gi rtsa ba bstan pa'i le'u ste bzhi pa'o//_//"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4806,
    "raw": "chos nyid bkod pa sems snang gi rtsa ba bstan pa'i le'u ste bzhi\n",
    "page_marker": 179,
    "start": 150839,
    "end": 150904
  },
  {
    "line": 4807,
    "raw": "pa'o\n",
    "page_marker": 179,
    "start": 150904,
    "end": 150909
  }
]
```

**Alignment differences:**
```json
[]
```

**Decision:** Keep the Chapter4 colophon and its qualified closing signs. W divides the same normalized wording over two lines; that lineation is not a lexical variant or evidence that all physical punctuation agrees.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json), [INSERTIONS.json](../INSERTIONS.json)
