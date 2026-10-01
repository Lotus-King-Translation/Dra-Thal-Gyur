# Chapter 6 — related Wikisource reference comparison

**Release candidate — final gate pending**

All 28 non-equal alignment blocks have explicit decisions. Exact A Wylie and W lines are preserved; W does not override the governing Adzom scan.

<a id="w-c06-001"></a>
## W-C06-001 — U05199

**A Tibetan:**
```json
[
  "སེམས་ཅན་འཁྲུལ་རྟོག་དུ་མ་ལས། །"
]
```

**A Wylie:**
```json
[
  "sems can 'khrul rtog du ma las/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5250,
    "raw": "sems can 'phrul rtog du ma las\n",
    "page_marker": 195,
    "start": 164956,
    "end": 164987
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "'khrul",
    "W": "'phrul"
  }
]
```

**Decision:** Retain Adzom 'khrul. W 'phrul is a related-reference lexical difference and is not source verification.

<a id="w-c06-002"></a>
## W-C06-002 — U05203

**A Tibetan:**
```json
[
  "པདྨ་ལས་བྱུང་སངས་རྒྱས་ལ། །"
]
```

**A Wylie:**
```json
[
  "pad+ma las byung sangs rgyas la/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5254,
    "raw": "pad ma las byung sangs rgyas la\n",
    "page_marker": 195,
    "start": 165093,
    "end": 165125
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "pad+ma",
    "W": "pad ma"
  }
]
```

**Decision:** Retain the supplied pad+ma transliteration convention; W pad ma is presentation, not a source correction.

<a id="w-c06-003"></a>
## W-C06-003 — U05205, U05206

**A Tibetan:**
```json
[
  "ཀྱེ་ཀྱེ་པདྨའི་དབུས་ན་བཞུགས་པ་ཉིད། །",
  "འདི་ལྟར་ནམ་མཁའི་དཀྱིལ་འཁོར་ལ། །"
]
```

**A Wylie:**
```json
[
  "kye kye pad+ma'i dbus na bzhugs pa nyid/_/",
  "'di ltar nam mkha'i dkyil 'khor la/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5256,
    "raw": "kye kye pad ma'i dbus na bzhugs pa nyid\n",
    "page_marker": 195,
    "start": 165157,
    "end": 165197
  },
  {
    "line": 5257,
    "raw": "'di ltar nam mkha' dkyil 'khor la\n",
    "page_marker": 195,
    "start": 165197,
    "end": 165231
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "pad+ma'i",
    "W": "pad ma'i"
  },
  {
    "op": "replace",
    "A": "mkha'i",
    "W": "mkha'"
  }
]
```

**Decision:** Retain the supplied pad+ma form and nam mkha’i wording. W spacing and particle differences are recorded without normalizing the base.

<a id="w-c06-004"></a>
## W-C06-004 — U05212

**A Tibetan:**
```json
[
  "སྤྲུལ་པའི་སྐུ་ནི་གང་ཙམ་ཞིག །"
]
```

**A Wylie:**
```json
[
  "sprul pa'i sku ni gang tsam zhig_/"
]
```

**W lines:**
```json
[
  {
    "line": 5264,
    "raw": "sprul pa'i sku ni gad tsam zhig\n",
    "page_marker": 196,
    "start": 165385,
    "end": 165417
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "gang",
    "W": "gad"
  }
]
```

**Decision:** Retain Adzom gang tsam. W gad tsam is a lexical reference difference without source evidence sufficient to replace the governing witness.

<a id="w-c06-005"></a>
## W-C06-005 — U05218

**A Tibetan:**
```json
[
  "པདྨའི་དབུས་ནས་བཞེངས་ནས་ནི། །"
]
```

**A Wylie:**
```json
[
  "pad+ma'i dbus nas bzhengs nas ni/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5270,
    "raw": "pad ma'i dbus nas bzhengs nas ni\n",
    "page_marker": 196,
    "start": 165581,
    "end": 165614
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "pad+ma'i",
    "W": "pad ma'i"
  }
]
```

**Decision:** Retain pad+ma source transliteration; W pad ma is a reference presentation difference.

<a id="w-c06-006"></a>
## W-C06-006 — U05225

**A Tibetan:**
```json
[
  "ཞུས་ལན་དང་པོ།"
]
```

**A Wylie:**
```json
[
  "zhus lan dang po/"
]
```

**W lines:**
```json
[]
```

**Differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan dang po",
    "W": ""
  }
]
```

**Decision:** Retain the first-reply heading. Its absence in the related website does not establish absence from Adzom; the native source check supports the separate heading role.

<a id="w-c06-007"></a>
## W-C06-007 — U05232

**A Tibetan:**
```json
[
  "ཚིག་བསྡུས་པ་ལས་ཤློ་ཀ །"
]
```

**A Wylie:**
```json
[
  "tshig bsdus pa las sh+lo ka_/"
]
```

**W lines:**
```json
[
  {
    "line": 5283,
    "raw": "tshig bsdus pa las sho la ka\n",
    "page_marker": 196,
    "start": 166007,
    "end": 166036
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "sh+lo",
    "W": "sho la"
  }
]
```

**Decision:** Retain supplied sh+lo ka exactly in the source layer; W sho la ka is a related-reference spelling or segmentation and is not adopted here.

<a id="w-c06-008"></a>
## W-C06-008 — U05234

**A Tibetan:**
```json
[
  "ལེའུ་སྟོང་ཕྲག་སུམ་ཅུ་ལྔ། །"
]
```

**A Wylie:**
```json
[
  "le'u stong phrag sum cu lnga/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5285,
    "raw": "le'u sdong phrag sum cu lnga\n",
    "page_marker": 196,
    "start": 166069,
    "end": 166098
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "stong",
    "W": "sdong"
  }
]
```

**Decision:** Retain Adzom stong phrag. W sdong phrag is recorded as a lexical reference difference; no correction is inferred.

<a id="w-c06-009"></a>
## W-C06-009 — U05245

**A Tibetan:**
```json
[
  "ཞུས་ལན་གཉིས་པ།"
]
```

**A Wylie:**
```json
[
  "zhus lan gnyis pa/"
]
```

**W lines:**
```json
[]
```

**Differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan gnyis pa",
    "W": ""
  }
]
```

**Decision:** Retain the second-reply heading. W omits the heading, but the Adzom-based edition preserves the source heading rather than adopting website layout.

<a id="w-c06-010"></a>
## W-C06-010 — U05247, U05248

**A Tibetan:**
```json
[
  "རང་ཤར་བ་དང་རང་གྲོལ་དང་། །",
  "རང་བྱུང་ཉིད་དང་རྩ་ལ་རྫོགས་དང་། །"
]
```

**A Wylie:**
```json
[
  "rang shar ba dang rang grol dang /_/",
  "rang byung nyid dang rtsa la rdzogs dang /_/"
]
```

**W lines:**
```json
[
  {
    "line": 5298,
    "raw": "rang shar ba rang rang grol dang\n",
    "page_marker": 197,
    "start": 166476,
    "end": 166509
  },
  {
    "line": 5299,
    "raw": "rang byung nyid dang rtsal rdzogs dang\n",
    "page_marker": 197,
    "start": 166509,
    "end": 166548
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "dang",
    "W": "rang"
  },
  {
    "op": "replace",
    "A": "rtsa la",
    "W": "rtsal"
  }
]
```

**Decision:** Retain the source-qualified rtsa la reading with explicit uncertainty. W rtsal is recorded as reference evidence, but the native check did not justify replacing the governing base.

<a id="w-c06-011"></a>
## W-C06-011 — U05266

**A Tibetan:**
```json
[
  "བརྗོད་ཅིང་གླེང་བ་ཉིད་བྲལ་ལོ། །"
]
```

**A Wylie:**
```json
[
  "brjod cing gleng ba nyid bral lo/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5317,
    "raw": "brjod cing gleng pa nyid bral lo\n",
    "page_marker": 197,
    "start": 167113,
    "end": 167146
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "ba",
    "W": "pa"
  }
]
```

**Decision:** Retain gleng ba. W gleng pa is a reference spelling difference and does not warrant changing the base.

<a id="w-c06-012"></a>
## W-C06-012 — U05275

**A Tibetan:**
```json
[
  "ཞུས་ལན་བཞི་པ།"
]
```

**A Wylie:**
```json
[
  "zhus lan bzhi pa/"
]
```

**W lines:**
```json
[]
```

**Differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bzhi pa",
    "W": ""
  }
]
```

**Decision:** Retain the fourth-reply heading. Its absence in W is a reference-layout difference, not evidence for deletion from Adzom.

<a id="w-c06-013"></a>
## W-C06-013 — U05284

**A Tibetan:**
```json
[
  "ཡོན་ཏན་མཚན་དཔེ་རྫོགས་པ་ལས། །"
]
```

**A Wylie:**
```json
[
  "yon tan mtshan dpe rdzogs pa las/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5335,
    "raw": "yon tan mtshan dpe rdzogs la las\n",
    "page_marker": 198,
    "start": 167692,
    "end": 167725
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "pa",
    "W": "la"
  }
]
```

**Decision:** Retain mtshan dpe rdzogs pa las. W la las is recorded but not adopted absent source evidence.

<a id="w-c06-014"></a>
## W-C06-014 — U05292

**A Tibetan:**
```json
[
  "ཞུས་ལན་ལྔ་པ།"
]
```

**A Wylie:**
```json
[
  "zhus lan lnga pa/"
]
```

**W lines:**
```json
[]
```

**Differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan lnga pa",
    "W": ""
  }
]
```

**Decision:** Retain the fifth-reply heading. Its absence in W is recorded without deleting the Adzom heading.

<a id="w-c06-015"></a>
## W-C06-015 — U05305

**A Tibetan:**
```json
[
  " ཞུས་ལན་དྲུག་པ།"
]
```

**A Wylie:**
```json
[
  "_zhus lan drug pa/"
]
```

**W lines:**
```json
[]
```

**Differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan drug pa",
    "W": ""
  }
]
```

**Decision:** Retain the sixth-reply heading. W omission is a reference difference, not a source correction.

<a id="w-c06-016"></a>
## W-C06-016 — U05317

**A Tibetan:**
```json
[
  " ཞུས་ལན་བདུན་པ།"
]
```

**A Wylie:**
```json
[
  "_zhus lan bdun pa/"
]
```

**W lines:**
```json
[]
```

**Differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bdun pa",
    "W": ""
  }
]
```

**Decision:** Retain the seventh-reply heading. W omission does not override the Adzom heading.

<a id="w-c06-017"></a>
## W-C06-017 — U05328

**A Tibetan:**
```json
[
  " ཞུས་ལན་བརྒྱད་པ།"
]
```

**A Wylie:**
```json
[
  "_zhus lan brgyad pa/"
]
```

**W lines:**
```json
[]
```

**Differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan brgyad pa",
    "W": ""
  }
]
```

**Decision:** Retain the eighth-reply heading. W omission is preserved as a reference-layout difference.

<a id="w-c06-018"></a>
## W-C06-018 — U05333

**A Tibetan:**
```json
[
  "ཕྱིར་མི་ལྡོག་དང་འགྲོ་འོང་མེད། །"
]
```

**A Wylie:**
```json
[
  "phyir mi ldog dang 'gro 'ong med/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5382,
    "raw": "phyir mi ldog dang 'gro 'ang med\n",
    "page_marker": 200,
    "start": 169211,
    "end": 169244
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "'ong",
    "W": "'ang"
  }
]
```

**Decision:** Retain 'gro 'ong med. W 'gro 'ang med is a related-reference difference without source verification.

<a id="w-c06-019"></a>
## W-C06-019 — U05351, U05352

**A Tibetan:**
```json
[
  "དམར་དྭངས་འཕྲོ་བ་དབང་གི་ལས། །",
  "སྔོ་ཞིང་གནག་ཐུང་དྲག་པོ་འགྲུབ། །"
]
```

**A Wylie:**
```json
[
  "dmar dwangs 'phro ba dbang gi las/_/",
  "sngo zhing gnag thung drag po 'grub/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5400,
    "raw": "dmar dangs 'phro ba dbang gi las\n",
    "page_marker": 200,
    "start": 169778,
    "end": 169811
  },
  {
    "line": 5401,
    "raw": "sngo zhing gnag thub drag po 'grub\n",
    "page_marker": 200,
    "start": 169811,
    "end": 169846
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "dwangs",
    "W": "dangs"
  },
  {
    "op": "replace",
    "A": "thung",
    "W": "thub"
  }
]
```

**Decision:** Retain Adzom dwangs and thung forms. W dangs and thub are exact reference differences, not automatic corrections.

<a id="w-c06-020"></a>
## W-C06-020 — U05360

**A Tibetan:**
```json
[
  "ལྷབ་ལྷབ་གསུམ་བཏུད་སྤར་སྤར་མང༌། །"
]
```

**A Wylie:**
```json
[
  "lhab lhab gsum btud spar spar mang*/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5410,
    "raw": "lhab lhab gsum btud sbar sbar mang\n",
    "page_marker": 201,
    "start": 170071,
    "end": 170106
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "spar spar",
    "W": "sbar sbar"
  }
]
```

**Decision:** Retain the onomatopoeic source form spar spar with its unresolved acoustic value. W sbar sbar is recorded, not normalized into the base.

<a id="w-c06-021"></a>
## W-C06-021 — U05382

**A Tibetan:**
```json
[
  "སྒྲ་ནི་ཤག་དང་སྡིག་པ་དང༌། །"
]
```

**A Wylie:**
```json
[
  "sgra ni shag dang sdig pa dang*/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5433,
    "raw": "sgra ni shag dang sdid pa dang\n",
    "page_marker": 202,
    "start": 170796,
    "end": 170827
  },
  {
    "line": 5434,
    "raw": "tog dang sing bas sna tshogs las\n",
    "page_marker": 202,
    "start": 170827,
    "end": 170860
  },
  {
    "line": 5435,
    "raw": "'ur zhing sing bas mchog thob pa'o\n",
    "page_marker": 202,
    "start": 170860,
    "end": 170895
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "sdig",
    "W": "sdid"
  },
  {
    "op": "insert",
    "A": "",
    "W": "tog dang sing bas sna tshogs las 'ur zhing sing bas mchog thob pa'o"
  }
]
```

**Decision:** Retain Adzom shag/sdig and include the two scan-restored main verses after U05382. W contains the two lines and differs at sdig/sdid; restoration is adopted from the governing scan, not from W authority.

<a id="w-c06-022"></a>
## W-C06-022 — U05391

**A Tibetan:**
```json
[
  "ཟླ་གསུམ་དང་ནི་ཟླ་དྲུག་ནས། །"
]
```

**A Wylie:**
```json
[
  "zla gsum dang ni zla drug nas/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5444,
    "raw": "zla sum dang ni zla drug nas\n",
    "page_marker": 202,
    "start": 171172,
    "end": 171201
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "gsum",
    "W": "sum"
  }
]
```

**Decision:** Retain zla gsum. W zla sum is a reference spelling form and does not change the base.

<a id="w-c06-023"></a>
## W-C06-023 — U05398

**A Tibetan:**
```json
[
  "ལོངས་སྐུ་དག་གིས་རྣམ་པར་ཐོབ། །"
]
```

**A Wylie:**
```json
[
  "longs sku dag gis rnam par thob/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5451,
    "raw": "longs sku ngag gis rnam par thob\n",
    "page_marker": 202,
    "start": 171395,
    "end": 171428
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "dag",
    "W": "ngag"
  }
]
```

**Decision:** Retain supplied dag gis with explicit uncertainty. W ngag gis fits a possible parallel reading, but the native check did not justify silently supplying ngag.

<a id="w-c06-024"></a>
## W-C06-024 — U05402

**A Tibetan:**
```json
[
  "ངག་གི་ཨཱ་ལི་ཀ་ལཱིར་སྦྱོར། །"
]
```

**A Wylie:**
```json
[
  "ngag gi A li ka lIr sbyor/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5455,
    "raw": "ngag ni a li ka lir sbyor\n",
    "page_marker": 202,
    "start": 171516,
    "end": 171542
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "gi A",
    "W": "ni a"
  },
  {
    "op": "replace",
    "A": "lIr",
    "W": "lir"
  }
]
```

**Decision:** Retain the supplied ngag gi A li ka lIr wording and source transliteration. W ni, a, and lir differences remain reference evidence only.

<a id="w-c06-025"></a>
## W-C06-025 — U05414

**A Tibetan:**
```json
[
  "དེ་དག་གིས་ནི་རང་གྲོལ་གདེང༌། །"
]
```

**A Wylie:**
```json
[
  "de dag gis ni rang grol gdeng*/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5468,
    "raw": "de dag gis ni rang grol gding\n",
    "page_marker": 203,
    "start": 171897,
    "end": 171927
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "gdeng",
    "W": "gding"
  }
]
```

**Decision:** Retain gdeng. W gding is recorded as a related-reference spelling difference.

<a id="w-c06-026"></a>
## W-C06-026 — U05443

**A Tibetan:**
```json
[
  "པདྨ་ལས་སྐྱེས་བཅོམ་ལྡན་འདས། །"
]
```

**A Wylie:**
```json
[
  "pad+ma las skyes bcom ldan 'das/_/"
]
```

**W lines:**
```json
[
  {
    "line": 5498,
    "raw": "pad ma las skyes bcom ldan 'das\n",
    "page_marker": 204,
    "start": 172835,
    "end": 172867
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "pad+ma",
    "W": "pad ma"
  }
]
```

**Decision:** Retain pad+ma source transliteration; W pad ma is presentation only.

<a id="w-c06-027"></a>
## W-C06-027 — U05460

**A Tibetan:**
```json
[
  "ཨག་ཐམ།"
]
```

**A Wylie:**
```json
[
  "ag tham/"
]
```

**W lines:**
```json
[
  {
    "line": 5516,
    "raw": "a ga tha ma\n",
    "page_marker": 205,
    "start": 173471,
    "end": 173483
  }
]
```

**Differences:**
```json
[
  {
    "op": "replace",
    "A": "ag tham",
    "W": "a ga tha ma"
  }
]
```

**Decision:** Retain the Adzom ritual string ag tham with explicit segmentation uncertainty. W a ga tha ma is preserved as a related-reference form, not silently substituted.

<a id="w-c06-028"></a>
## W-C06-028 — U05466

**A Tibetan:**
```json
[
  " དགེའོ་དགེའོ་དགེའོ།།"
]
```

**A Wylie:**
```json
[
  "_dge'o dge'o dge'o//"
]
```

**W lines:**
```json
[
  {
    "line": 5522,
    "raw": "dge'o\n",
    "page_marker": 205,
    "start": 173630,
    "end": 173636
  },
  {
    "line": 5523,
    "raw": "dge'o\n",
    "page_marker": 205,
    "start": 173636,
    "end": 173642
  },
  {
    "line": 5524,
    "raw": "dge'o\n",
    "page_marker": 205,
    "start": 173642,
    "end": 173648
  }
]
```

**Differences:**
```json
[]
```

**Decision:** Retain all three final dge’o formulas. W has the same lexical sequence on three lines; lineation and punctuation differences do not alter the Adzom closing.
