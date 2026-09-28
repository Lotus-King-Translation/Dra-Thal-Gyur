# Compacted summary excerpts — secondary recovery evidence

The text between the excerpt markers below is copied from the retained compaction summary. It is not an original report, original file bytes, or a new reading. The U01803 dispute described here was subsequently resolved by the retained correction patch and final verification excerpt in this directory. Crops and original scratch artifacts mentioned here were not reread or regenerated during recovery.

--- BEGIN RETAINED COMPACTED SUMMARY EXCERPT: assignment and artifacts ---
We are subagent `/root/base_ch1_annotation_audit` working under parent `/root` on Tibetan diplomatic edition in `/workspace/scratch/a117ee885aff/Dra-Thal-Gyur`. User authorized sequential chapter commits to remote, but our task is **scratch-only review, no repo edits or commits**. Root coordinates other agents.

Original assignment:
- Audit all Chapter 1 annotation/layer claims in `translations/2026-09-26-full-draft/notes/scan-decisions.jsonl` for units <=2635, originally except 542,1067,1090,1811–1812 (later parent asked to include all except lexical U542).
- Inspect native facsimile `source/Dra-Thal-Gyur-Adzom-2000.pdf`, preserve exact original units, proposed main, separate annotation, confidence, crops/locators.
- No full-page proofreading claim. We did targeted annotation review.
- Read AGENTS.md, METHOD.md, source README, PDF skill, combined translation standard (tool output truncated some), glossary initial entries. No English translation or terminology changes.
- PDF is 205 pages; native embedded image size usually 5696x1344, page N => BDRC image N+2. Main consists 6 physical rows. Most small notes are **displaced one or two rows below target**, often dotted leaders.
- Python fitz installed; `pyewts` at `/workspace/scratch/a117ee885aff/python-deps`.

Artifacts created, current:
1. `/workspace/scratch/a117ee885aff/build_annotation_audit.py` — scratch script with manual obs dict, generates reports from unchanged ALIGNED original strings.
2. `/workspace/scratch/a117ee885aff/ch1-annotation-audit.json`
3. `/workspace/scratch/a117ee885aff/ch1-annotation-audit.md`
   - **41 records currently**.
   - Includes all 30 annotation records from old scan-decisions <=2635 except U542 lexical correction, +11 candidates U187,U192,U272,U317,U318,U328,U534,U626,U710,U800,U1144.
   - U1811 jointly includes U1812 originals.
4. `/workspace/scratch/a117ee885aff/ch1-early-annotation-reconciliation.json`
   - Checks all U IDs named in early reader’s 14 uncertainty/delegation entries are represented; `all_delegated_identifiers_accounted_for: true`.
5. `/workspace/scratch/a117ee885aff/title-blind-reading.md`
   - Separate requested uncued title read, no confident discrepancy with U00004. Explicit qualification that U00004 had incidentally been printed earlier in task, so not memory-free blind experiment.
6. Native/crop folder `/workspace/scratch/a117ee885aff/ch1-annotation-crops/`
   - Full native pages `pNNN-full.png`, left/right overlapping half crops `pNNN-left.png`, `pNNN-right.png` (some pages also `-L.png`, `-R.png`).
   - Focus details names below.
   - PIL `.save(path)` sometimes produced empty/corrupt file despite no errors; fixed by saving to io.BytesIO and Path.write_bytes. Referenced crop files verified with PIL after41? Last explicit verification was37; added p13/p46 via BytesIO valid and details viewed.

Root has already **integrated41 audit records** to repo and other changes, so scratch corrections must be communicated explicitly and root applies.
--- END RETAINED COMPACTED SUMMARY EXCERPT ---

--- BEGIN RETAINED COMPACTED SUMMARY EXCERPT: findings ---
Important audit findings (current unless corrected next):
- U180 main `de nas gcig dang tha mi dad/`, small `sdud pa po zhu ba rang byung gi bkod pa` p10 line2 below main line1.
- U187 main `'byung bzhi'i dgongs pa ji lta bu/`, small `dgos pa yang byung` p10line5, dotted from mainline3.
- U192 main `'gyur dang 'gyur byed gang dang gang/`, full smaller note on p10line4:
  `'di mtshams 'og gi rang dang gzhan gyi dam bca'i zhes pa dang 'phen pa rlung ste zhes pa gnyis kyi dri ba ma byung`
  crops `U192-note.png`, `U192-main.png`.
- U272 main `de nas khyab bdag sems dpa' ni/`, small `rgyud kyi che ba rnam par bkod pa'i bkod pa` p13line6. Detail `U272-detail.png`.
- U317 entire `dri ba bdun cu zer kyang don drug par yod/` is smaller source structural statement p15line4. Preserve 70/76 discrepancy, no main.
- U318 `dris lan dang po/` separate heading p15line4.
- U328 main `mes ni 'byung ba sel ba dang/`, smaller `spel yang byung` inline p15line6.
- U534 main `ljongs rab tu rdzogs te nyams dga' bar/`, small `bde yang byung` p23line5far-right, main p23line4right toline5left.
- U596 main `'od 'byung phreng ba klu yi gdong/`, small `glu yang gdung yang byung` p26line2left-middle.
- U626 main `tshig dang zur la gzhon pa dang/`, small `gzhog kyang` p27line3middle with dotted leader. `U626-detail.png`.
- U632 main `ma dag pa yis ye shes so/` spanning p27line3far-right toline4far-left, small `ni yang` p27line4far-right.
- U651 main `gnas dang byung dang byed pa dang/`, small `byas kyang 'dug` p28line3middle.
- U710 **corrected main** `so so'i nus pas bsgyur ba gang/`; small **whole** `bus pa sbyar yang 'byung` p30line4. bus pa belongs note, not main.
- U800 main `b+ha ra b+ha ti sa li zhes bya bar/`, small `sa yi yang byung` p33line6.
- U1067 main `thams cad tshe gcig 'bras bu thob/`, small `brgya yang byung` p43line4middle, mainline3. `U1067-detail.png`.
- U1090 main `yan lag bkod pa brgya gcig go/`, small `bcu gcig kyang byung` p44line3far-right, mainline2. `U1090-detail.png`.
  These two overturn prior provisional scan non-observations in `diplomatic/reviews/chapter-01/key-scan-checks.md`; notes were displaced.
- U1144 `tshig chad song/` small p46line3left-middle between1143 and1145. Witness omission query, no conjectural missing text. `U1144-detail.png`.
- U1233 main `de ltar brgya dang brgyad cu las/`; U1237 main `de ltar sbrags pa de tsam las/`. Same note `chags 'jig stongs pa` appears twice in transcript, **one observed small scan occurrence** inside U1238 p49line5 between `bskal pa` and `chen po`. Both records include unique shared key `A-p049-l5-chags-jig-stongs-pa`, display once. `renderer_annotation_anchor` fields specify U01238, inline after exact prefix Tibetan `བསྐལ་པ་`, computed codepoints, suffix `chen po gcig yin no/`. Root rendering one scan note + both unchanged transcript quotes.
- U1265 main `rnal 'byor pa yis bkug shes na/`, small `dkrug kyang` p50line6middle-right.
- U1414 main `sa pa la ser po'i sbyor ba yi/`, small `se yi yang byung` p56line4right.
- U1417 main `'byung ba'i dus nyid rab bstims nas/`, small `bsdebs kyang byung` p56line5middle-right before phyin nas.
- U1422 main `rin po che yi sbyor ba dag/`, small `rin chen bse'i yang byung` p56line6far-right.
- U1439 main `legs par sbyar te a yis bskor/`, small `a lis kyang byung` p57line4far-right.
- U1567 main `bsdams pas 'gags la btsir bas 'ching/`, small `gtems kyang byung` p62line3left-middle.
- U1657 main `'di yi lus kyang gsum yin te/`, small `lugs kyang` p65line5right.
- U1668 annotation-only `bkang yang byung`, p66line2left-middle. Related U1667 `rgyu dang mi rgyu rlung gis bskor/` across65/66.
- U1711 main `yi ge bzlog tshul drug gis kyang/`, small `brjod kyang` p67line5middle.
- U1716 main `'dre dang rlung lha dag gi skad/`, small `dag pa'i skad kyang byung` p67line6middle-right.
- U1734 main `zla ba lo yi 'khrul lugs kyis/`, small `'khrugs lugs kyang` p68line4middle.
- U1776 note-only `min kyang/` after mainU1775 affirmative yin, p69line6.
- **U1803 CURRENT DISPUTE — NEXT ACTION REQUIRED, see below.** Current scratch audit says main `sa ya bzhi bzung ste rang rang bstun/`, small `gzhi yang byung`; root+late now see main **ya bzhi...**, small **sa gzhi yang byung**. Must recheck and correct scratch promptly.
- U1806 small `lteb dang gtugs kyang byung` p70 belowline6far-left in bottomframe extension, precise target unsettled.
- U1811/1812 main `lo stong zhag kyang 'bum phrag gsum/` acrossp71line2end->line3left. Smaller exact scan `lo ste zhag bcu phrag gsum yang byung` p71line3right, **without kyang after zhag**. Preserve exact original units separately (flattened original has extra-looking kyang in branch).
  `original_units`, `original_units_joined_exact_tibetan`, `proposed_main_distribution` U1811combined/U1812empty, `exact_scan_annotation_wylie/tibetan` fields.
- U1829 annotation-only `gsum ste dus ni bcu gnyis sbyar yang byung`, p71line6far-right continues yang byung p72line1far-left. Related mainU1830 `rten 'brel dus te bcu gnyis sbyar/`, split rten atp71end + 'brel...p72start.
- U2129 main `dgug dang bsad dang bcings pa'i las/`, small `bskrad kyang` p83line4right, mainline3. Late independently agrees dotted from bsad.
- U2225 **main correction** `sgra dang gdams ngag la sogs te/`; smaller **whole** `smra dang gtam ngan yang byung` p87line2. Prior note wrongly left smra dang in main. Root independently confirmed.
- U2332 main `ngag ni bslab dang gnas pa dang/`, small `rlab kyang` p91line2middle.
- U2489 main `rnal 'byor chen po'i spyod pa'i` ends p96line6right; heading `dris lan re bdun pa/` starts p97line1 before 'brasbu. Late confirms genitive pa'i, not pa'o.
- **U2615 & U2620 CURRENT weaker uncertainty and latest late message**:
  Our41 audit says displaced p101line4 small-note cluster heavily inked, exact allocation unresolved. U2614 main `'bru bzhi lnga dang gzugs 'dogs kyis/` clear. Retain U2615 mdog gi yang byung separately with qualified scan provenance; U2620 `de dag gi zhabs sdud pa'o/` smaller cluster before stonpa, glyph-by-glyph not certified.
  Root independently said `p101-summary.png` too inked for exact certification, agreed lower confidence.
  Latest late message now says: “full six rows plus margins inspected; U2615 མདོག་གི་ཡང་བྱུང་། not located. U2614mainclear; U2616 follows directlyrow3. Smallrow4 before stonpa is U2620 དེ་དག་གི་ཞབས་སྡུད་པའོ།.” Could relay and preserve local non-observation confidence; do not alter without root request beyond next urgentU1803.
- Late also sent **new U2597 correction** p100:
  transcript `ལན་དོན་ལྔ་པ།` vs scan `དྲིས་ལན་དོན་ལྔ་པ།` row5near-right, crop `/workspace/scratch/a117ee885aff/late-crops/100-u2597.png`.
  Not yet handled by us; root likely received too? late sent only us text, so relay.

IMPORTANT history:
At first we wrongly called 596,632,651,1265 not seen; focused following-row crops found all. We corrected artifacts and explicitly toldroot. Current41 has **no incorrect non-observation for those**. No broad claim allnotesinallwitnesses. Most remarks physicalprovenance ratherthan exactglyphtranscription; allarekept separate. Script retains older obs assignments then `obs.update(...)` overrides them; updating final overrides easier.
--- END RETAINED COMPACTED SUMMARY EXCERPT ---
