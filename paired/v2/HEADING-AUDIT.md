# Heading audit — paired-text/2

Status: source-based recommendation for the coordinator's classification/signoff; no source or translation changes. Heading level is an editorial rendering assignment, not a claim that the printing encodes HTML levels.

## Scope and authorities

Read all 169 released `source_heading` strings, U00001–U00010, every chapter's first/last heading context, the exceptional rubrics and title context, and relevant released apparatus/accepted decisions. Searched all 5,484 golden strings for title, chapter and reply expressions outside `source_heading`; the additional matches are naming formulas, body references and colophons, not additional opening section headings. This is not full body-format review, new scan inspection, or semantic QC.

Inputs: `root-tantra-v1.0.0` (`b83051912977268b97615bd382d82e51c3406d61`) reading sequence and `translation-golden-aligned-v1.0.0` (`e24e97ddad9cefa339b5583a38389179dba7a365`) edition/notes, loaded via `paired/core.py` pins. Read `AGENTS.md`, `paired/v2/PLAN.md`, both `paired/v2/reference/template-*.md`, `paired/README.md` and `paired/MIGRATION.md`.

## Recommended hierarchy

Retain the existing document hierarchy: work/title `h1`, six explicit chapter wrappers `h2`, chapter-internal section headings `h3`. The distinct closing-material wrapper also remains `h2`, outside the chapter sequence. These wrappers are existing editorial Markdown, not golden objects: do not fabricate golden IDs, paired chapter-title content or new chapters. Report paired heading counts separately from wrapper counts.

| Golden objects | v1 pairs | Proposed format | Source/editorial basis |
| --- | --- | --- | --- |
| U00002; U00004 | DTG-000002; DTG-000004 | h1 | Foreign-title and Tibetan-title rows of PDF1 title leaf; work-level variants, not chapter/subsection labels. Retain lettering uncertainties. |
| U00001; U00003 | DTG-000001; DTG-000003 | prose | Ornamental opening scaffolds, not lexical headings; prose is the five-value schema's body-rendering fallback. Preserve `opening_title_or_sign` role. |
| U00005 U00006; U00007 U00008 | DTG-000005; DTG-000006 | prose | Language/title naming formulas in the continuous PDF2 opening. U00005 includes the unresolved invocation and `རྒྱ་གར་སྐད་དུ།`; U00007 is ` བོད་སྐད་དུ།`. The repeated title contents do not themselves introduce a nested section. No split is required within these two formula pairs. |
| U00011; U00029 | DTG-000009; DTG-000016 | h3 | Separate uncommon/common introductory-setting rubrics within chapter 1, immediately preceding U00012 and U00030 respectively. Their differing subject is not evidence of differing rank. |
| 166 numbered reply rubrics, exact IDs below | All listed headings map by golden ID; SCAN-CH1-LAYER-02489 currently lies inside DTG-001124 | h3 | The numbered replies are chapter-internal sections. Chapters 1/2/3 use `དྲིས་ལན`; chapter 4 begins with six `ཞུས་དོན` labels then `ཞུས་ལན`; chapters 5/6 use `ཞུས་ལན`. Wording differences do not establish hierarchy. |
| U04951 | DTG-002405 | h3 | `འདི་མན་ཆད་བསྡུས་དོན་བཤད།` introduces the chapter 5 summary after the twelfth reply and before U04952 `གཞན་ཡང་ཆོས་ཉིད་འཁོར་ལོ་བཤད། །`. It is a sibling chapter-internal section, not a new chapter. |

Expected paired heading counts under this convention: **h1 2; h2 0; h3 169**. The seven external `##` part wrappers are not included in pair-format counts. No heading level is created solely to populate a count.

## Exact h3 inventory

The following lists include all 169 objects exactly once. Chapter 1 includes 76 reply headings and two introductory rubrics; chapter 5 includes 12 reply headings and one summary rubric. Other lists contain only reply headings. These are exact object sets, not continuous ranges.

- Chapter 1: 78 h3 objects, within v1 DTG-000001–DTG-001192: `U00011`, `U00029`, `SCAN-CH1-LAYER-00318`, `U00344`, `U00373`, `U00394`, `U00492`, `U00598`, `U00624`, `U00655`, `U00676`, `U00701`, `U00721`, `U00756`, `U00822`, `U00910`, `U00948`, `U01023`, `U01083`, `U01122`, `U01147`, `U01186`, `U01219`, `U01239`, `U01257`, `U01271`, `U01308`, `U01335`, `U01353`, `U01381`, `U01454`, `U01476`, `U01514`, `U01540`, `U01557`, `U01596`, `U01620`, `U01634`, `U01661`, `U01689`, `U01727`, `U01751`, `U01764`, `U01854`, `U01906`, `U01937`, `U01968`, `U01999`, `U02021`, `U02046`, `U02142`, `U02162`, `U02180`, `U02193`, `U02215`, `U02241`, `U02250`, `U02299`, `A2000-C01-S06`, `U02318`, `U02327`, `U02358`, `U02402`, `U02413`, `U02424`, `U02434`, `U02463`, `U02481`, `SCAN-CH1-LAYER-02489`, `U02500`, `U02510`, `U02536`, `U02547`, `U02563`, `U02576`, `U02584`, `U02597`, `U02610`.

- Chapter 2: 27 h3 objects, within v1 DTG-001193–DTG-001735: `U02767`, `U02781`, `U02813`, `U02857`, `U02894`, `U02943`, `U02986`, `U03018`, `U03056`, `U03093`, `U03134`, `U03192`, `U03217`, `U03227`, `U03242`, `U03259`, `U03291`, `U03319`, `U03339`, `U03353`, `U03373`, `U03395`, `U03432`, `U03454`, `U03487`, `U03511`, `U03529`.

- Chapter 3: 23 h3 objects, within v1 DTG-001736–DTG-002089: `U03657`, `U03710`, `U03736`, `U03763`, `U03793`, `U03827`, `U03859`, `U03898`, `U03929`, `U03959`, `U03984`, `U03997`, `U04014`, `U04030`, `U04046`, `U04058`, `U04072`, `U04084`, `U04099`, `U04112`, `U04130`, `U04143`, `U04156`.

- Chapter 4: 21 h3 objects, within v1 DTG-002090–DTG-002326: `U04344`, `U04350`, `U04368`, `U04378`, `U04390`, `U04406`, `U04433`, `U04451`, `U04462`, `U04484`, `U04494`, `U04509`, `U04527`, `U04539`, `U04557`, `U04568`, `U04584`, `U04594`, `U04608`, `U04620`, `U04645`.

- Chapter 5: 13 h3 objects, within v1 DTG-002327–DTG-002537: `U04793`, `U04804`, `U04824`, `U04850`, `U04860`, `U04865`, `U04873`, `U04885`, `U04900`, `U04909`, `U04926`, `U04939`, `U04951`.

- Chapter 6: 7 h3 objects, within v1 DTG-002538–DTG-002645: `U05225`, `U05245`, `U05275`, `U05292`, `U05305`, `U05317`, `U05328`.


## Structural exceptions and evidence

- U00011 is `ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞི་བཀོད་པ།`; U00029 is `ཐུན་མོང་གི་གླེང་གཞི་བཀོད་པ།`. Both introduce their own settings. Neither released decision establishes that one contains the other, nor that a setting rubric encloses all later numbered replies. Assigning a higher rank solely because “setting” sounds broad would invent hierarchy.
- U03657 announces ten subdivisions (`དྲིས་ལན་དང་པོ་ལ་ནང་གསེས་བཅུས་བསྟན།`); U03710–U03959 similarly announce point counts. They remain single reply headings. The numbered points inside their body are not separately released heading objects; do not create h4 or extra h3 headings from the announced counts. See `diplomatic/chapter-03-v1/DECISIONS.json`, L3-0002 and the subsequent heading decisions.
- SCAN-CH1-LAYER-02489 (`དྲིས་ལན་རེ་བདུན་པ`) lies between U02489 and U02490 in DTG-001124. The chapter 1 released apparatus preserves this printed cross-page position. Split the v1 pair at both heading boundaries; grammatical continuation is not permission to suppress its h3 boundary. Do not move it to a sentence boundary.
- Retain numbering gaps as released: chapter 2's first explicit rubric is reply two; chapter 6 has reply one, two, then four through eight. Do not invent absent reply labels.
- The chapter-ending colophons at U02635, U03622, U04305, U04763, U05197 and U05448 close their chapters; they do not become opening h2 headings or move ahead of their text. The full-work colophon also remains closing material.

Evidence consulted: `diplomatic/release-v1/apparatus.json` (L1-0001, L1-0005, SCAN-CH1-TITLE-UNCERTAINTY); `diplomatic/release-v1-proposal/DECISIONS.json` (L1-0001/L1-0005); `diplomatic/reviews/chapter-01/continuation/C1-BASE-UNCERTAINTIES.json` (B04 PDF1 title rows versus PDF2 language/title and main rows); `diplomatic/release-v1/apparatus.md` (SCAN-CH1-LAYER-00318 and SCAN-CH1-LAYER-02489); chapter 3 released apparatus/decisions; `diplomatic/chapter-05-v1/release/apparatus.md` and `DECISIONS.json` (C5-I-U04951/L5-0018); fixed English endnotes G-U00001 through G-U00006, G-U00029 and both scan-heading notes. Existing source-image findings are cited, not claimed as new inspections.

## Decision boundary

The five format values do not stipulate an absolute work/chapter numbering convention. The recommendation above adopts the already-present `#` work / `##` chapter wrappers and makes no unsupported nesting claim. Under that retained convention, no heading-rank question remains genuinely indeterminate: the special rubrics and numbered replies are all chapter-internal siblings, after separate examination rather than a mechanical role lookup.

Promoting U00011/U00029/U04951 to h2, or promoting the embedded naming formulas U00006/U00008 to h1, would instead be a new editorial presentation choice. The inspected sources do not require those promotions. If desired, the coordinator must record the reason and any resulting lineage rather than claim the sources settled it. No fresh user decision is needed merely to preserve the established wrapper hierarchy; existing letter-level uncertainties remain in their notes.
