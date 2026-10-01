# Chapter 1 structural audit — paired-text/2

Scope: all 2,646 Chapter 1 golden objects and 1,192 v1 pairs (DTG-000001–DTG-001192), using the fixed source and English releases pinned in `paired/core.py`. Read `PLAN.md`, both template reference files, paired documentation, the active translation standard and relevant eight-column glossary records. `core.load_authorities()` and `core.check_protected()` pass. This is structure/presentation review, without translation, lexical adoption, new scan reading or semantic QC.

Coverage method: whole-object role, ordering, delimiter and tsheg/space-token inventory; direct Tibetan review of every exceptional inventory class, opening/closing material, all 78 heading boundaries with their first/last body lines, all restored blocks, empty layers and unusual-length body lines. The remaining regular body sequence is classified by its sustained metrical structure. This does not claim fresh semantic reading of every line or exhaustive scan proofreading. Raw main-text token counts are 3:1, 6:106, 7:2,422, 8:4, 9:6, 11:1, 13:1, 16:1; these are a screening inventory, not certified syllable counts (vocalic endings and Sanskrit clusters defeat a simple splitter).

| Exact objects | Recommended format | Source-based decision and evidence |
| --- | --- | --- |
| U00001, U00003 | prose | Ornamental opening signs: neutral non-heading display; prose does not assert a linguistic genre. Retain `opening_title_or_sign`. |
| U00002, U00004, U00006, U00008 | heading; level delegated | Sanskrit/Tibetan titles; retain exact source strings and released roles. U00008 is a title despite its `main_text` role. This report does not choose hierarchy. |
| U00005, U00007 | prose | Language announcements (`རྒྱ་གར་སྐད་དུ།`, `བོད་སྐད་དུ།`); U00005 also preserves the unresolved prefatory transliteration. They introduce titles, without belonging to those headings. |
| U00009–U00010 | prose | One homage construction: U00009 gives the object with eleven raw syllabic groups, and U00010 completes it with `ལ་ཕྱག་འཚལ་ལོ། །` (nine groups). Its extended nominal invocation and unequal units precede the sustained seven-syllable body. Homage function alone is not decisive; here the construction plus rhythm support prose. Do not split their existing pair or treat U00010 as verse merely because it has nine groups. |
| U00012, U00030 | prose | Repeated hearing formula `འདི་སྐད་བདག་གིས་ཐོས་པའི་དུས་གཅིག་ན། །` introduces each setting; the regular seven-syllable narrative starts at U00013/U00031. Deliberate presentation decision, moderate confidence: the nine-syllable formula can look like a verse line, but formula function and the following rhythmic reset support a distinct prose opener. Neither English colons nor double shad determine the choice. G-U00030 documents delimiter correction only, not a genre verdict. |
| U02634–U02635 | prose | U02634 begins the concluding attribution `ཞེས་…རྩ་བ་ལས།`; U02635 completes the chapter identification `…ལེའུ་སྟེ་དང་པོའོ།།`. Together they are a colophon sentence, not a new heading. The released `main_text` role of U02634 does not make it verse. |
| A2000-C01-S08 | prose | Caption with partial readings Q16/Q17/Q18 and detached-sign notation D D; neutral caption presentation. Unread fragments prevent certifying poetic metre. Preserve its internal source line break, `provisional_caption` role, and all uncertainty; do not infer a heading or restore missing words. |
| U00317, U00318, U01144, U01286, U01668, U01776, U01806, U01829, U02615, U02620 | prose | All ten are empty `source_annotation_anchor` objects. Prose is the presentation carrier for the disclosed English annotation markers, not an assertion about missing root text. Source annotations remain in notes. |
| U01812 | prose | Empty `joined_anchor`; neutral carrier for the disclosed joined-fragment marker. Its surviving root words occur in the joined reading, not as a second verse at this empty object. |
| A2000-C01-S09 | prose | Empty unresolved boundary inscription, retained as its own non-heading carrier. Character identities/script remain unresolved; this assignment does not resolve the inscription's genre. |
| All 78 `source_heading` objects | heading; level delegated | Two setting headings and 76 numbered replies, including SCAN-CH1-LAYER-00318, A2000-C01-S06 and SCAN-CH1-LAYER-02489. Their source layer remains visible even within a continuing sentence. |
| All remaining 2,541 Chapter 1 objects | verse | 2,535 `main_text` objects plus six `restored_main_text` objects. Short irregularities, fused vocalic endings and Sanskrit names do not create prose boundaries within the sustained verse sequence. All six restored objects remain intact. |

The 23 prose objects are exactly: U00001, U00003, U00005, U00007, U00009, U00010, U00012, U00030, U00317, U00318, U01144, U01286, U01668, U01776, U01806, U01812, U01829, U02615, U02620, U02634, U02635, A2000-C01-S08, A2000-C01-S09. With the four title candidates treated as headings, the exhaustive object accounting is 23 prose + 82 headings + 2,541 verse = 2,646.

Required splits of existing v1 pairs (no golden object needs subdivision):

| v1 pair | Ordered v2 structural groups |
| --- | --- |
| DTG-000005 | U00005 prose / U00006 title heading |
| DTG-000006 | U00007 prose / U00008 title heading |
| DTG-000010 | U00012 prose / U00013–U00017 verse |
| DTG-000017 | U00030 prose / U00031–U00032 verse |
| DTG-000165 | U00315–U00316 verse / U00317–U00318 prose |
| DTG-001124 | U02488–U02489 verse / SCAN-CH1-LAYER-02489 heading / U02490–U02492 verse |
| DTG-001185 | U02613–U02614 verse / U02615 prose / U02616 verse |

Rejected false boundaries: U00315–U00316 are two seven-syllable lines (`ངང་གཞི་བབ་ཀྱིས་གྲུབ་པ་ཡི། །` / `ཚིག་བྱུང་གཞི་ལ་འདི་ལྟར་སྣང་།`), despite their introductory function and English colon. Retain verse. U00534, U01414, U02387, U02499 (eight raw groups), U00800, U01778, U01849 (nine), and the 106 six-group candidates remain verse in their Tibetan contexts; do not repair wording or infer prose from raw count. The 13 restored lines in A2000-C01-S01/S02/S03/S04/S05/S07 remain verse.

Evidence: `diplomatic/root-tantra-v1/release/reading.json` and `reading.md`; `translations/2026-10-01-golden-aligned/edition.json`, `ENDNOTES.md` (especially G-U00030), and `SOURCE-ANNOTATIONS.json`; v1 grouping and exact-source reconstruction in `paired/core.py`. Caption/inscription uncertainty and other source qualifications remain unchanged. Heading hierarchy and final integration/signoff belong to the coordinator; no canonical files were edited here.
