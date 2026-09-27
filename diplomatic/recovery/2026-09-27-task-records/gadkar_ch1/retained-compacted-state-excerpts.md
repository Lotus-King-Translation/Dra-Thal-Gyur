# Retained compacted state: excerpts

Provenance: copied from the agent's pre-recovery compacted context summary. This is retained summary text, not the missing original report files, not a new transcription, and not independent evidence for a reading. Formatting and compressed wording below are retained. The earlier summary was itself based on prior work; it does not provide original file bytes or original file hashes.

---

Tasks completed:
1. **Gadkar bounded report** `gadkar-ch1.json/.md`; no exhaustive reading capability of dbu-med. Do not claim source unreadable, just reader limitation. Has boundary PDF91. Root has report.
2. **Langtang PDF79–104 scoped comparison** completed, `langtang-late.json/.md`; root imported and independently checked three gaps. 26 pages, 34 findings, local unresolved queries. Report partial lexical certification not absolute. Source hashes in report.
   - Includes U2459–2462, U2498, U2521–2524 local gaps; U2525 alternative; restored S03/S04/S05–S07 present.
   - Focused correction U2320=`rgyud 'di yis`, not preliminary yang.
   - U2518 only terminal mi yin vs min secure, preceding verb/pa unresolved.
3. **Tharpaling PDF17–43 partial lexical comparison** completed `tharpaling-middle.json/.md`; 27 pages all 6 main rows traversed with bounded unresolved regions. Root notified.
   - 4 positive findings:
     TH-MID-001 p26row4 U940 terminal `kun du gnas` vs Adzom `skur thim nas`
     TH-MID-002 p28row1 U996 scan `so sha'i`, B omits so
     TH-MID-003 p28row2 U1001 scan final rigs, B omits rigs; partly merged but identified in focused crop
     TH-MID-004 correction: S01 three water verses **present** PDF35 row2right→row3left before U1275. Supersedes old false absence TH-C1-CONT-003.
   - No transposition established, many unresolved glyphs. Root requires reliability, incomplete lexical status retained.
   - IMPORTANT TWO PROVISIONAL LOCATOR ERRORS explicitly withdrawn in report:
     a) PDF36 ends **U1334 partial**, PDF37 begins `'gag go` completing it, then small reply26 heading/U1336; earlier end/start U1343 was wrong.
     b) Quick nonsequential PDF43/44 guessed U1631 then U1630 boundary. **Wrong.** Sequential reading gives PDF43 **U1563–U1598**, PDF44 begins **U1599**. Other reader initially agreed based on cue; root notified explicitly to discard. Report preserves withdrawal. Source crops valid but old label interpretations invalid.

Source Tharpaling:
- `editions/tharpaling-1983/sgra-thal-gyur.pdf`
- PDF SHA `db895ffc9850a728e25add92491341039547f999fff80d7e73e9521ada10b550`
- `image-manifest.json`; PDF n → provider n+4
- Native images scratch `tharpaling-ch1/native/pNNN.png`, normally2198×454, some2211wide; **some extracted native images reverse polarity**. Apply display inversion based on mean gray<100, originals untouched.
- All images not equal quality; many faded/broken/merged letters but readable islands.
- Old report `tharpaling-continuation.json/.md` covered p4–16 partial and17–71 reconnaissance plus targeted checks. **Its three absence claims003/004/005 all disproved and now withdrawn.** Some remaining positive S04/S05 claims may have wrong page locators too—need sequential verification, do NOT assume correct.
- Old source findings:
  001p6row5 U166beforeU165 (local phrase order)
  002p11row2U337 scan omits sogs (`lus grub pa'i rgyu byas te`)
  003S01 falseabsence withdrawn
  004S02 falseabsence withdrawn
  005S03 falseabsence withdrawn
  006S04 claimedpresentPDF59row6 (might locator wrong! needs actual sequential verification)
  007S05/S06/S07 claimedpresentPDF63row1 (might locator wrong! needs actual sequential verification)
- Chapter1 boundary prior report PDF71row5 provider75. Must eventually verify actual from sequence/colophon again; don't blindly inherit.

S01 correction history:
- `tharpaling-s01-correction.json` TH-MID-004.
- Correct p35row2right→row3left afterU1274 beforeU1275:
  chu yi zug pas dbang po sdud
  byer ba yis ni 'khrugs par byed
  snyoms pa yis ni 'bras bu 'byin
- Some letters thin/merged; group presence/order secure, not every stroke.
- Expanded crop `tharpaling-middle-crops/p035-s01-row2.png` native `[1050,135,1950,200]`, scale3
  `p035-s01-row3.png` `[270,180,920,245]`, scale3
- Old report003 active fields now say withdrawn and currentpresence; old claim only `prior_claim_snapshot`; full old report snapshots `tharpaling-continuation.before-s01-correction.json/.md`.
- Do NOT rerun correction scripts idempotently; they append duplicate history/overwrite backups.
- `tharpaling-s01-correct.py` generator already run once.
- Root explicitly asked currentactive description/scope_limit/rationale not contain oldabsence; fixed.

S02/S03 corrections completed NOW, root notified:
- `tharpaling-s02-s03-corrections.json` array of TH-LATE-001/002
- `tharpaling-late-notes.json` checkpoint starts `{pages:[], findings:[those two corrections], scope_note:"Targeted restoration checks only ...full traversal pending"}`
- `tharpaling-late-crops/`
- TH-LATE-001 supersedes TH-C1-CONT-004:
  **Actual S02 at PDF51 row3right→row4left/middle/right**, **NOT PDF50**.
  Sequence U1882 `zhag dang zla ba lo rnams kyis`
  `so so'i tshad la rtags kyis 'grub`
  `'di ltar sku yi 'grub pa la`
  `sprul pa'i sku dang longs sku dang`
  U1883 `chos sku ngo bo nyid kyi sku`
  First verse faded localletters; presence/order asserted with qualifications.
  Evidence `p051-s02-right-rows3-4.png` native `[1090,164,1940,290]`,scale2
  `p051-s02-left-row4.png` `[200,211,1510,302]`,scale2
- TH-LATE-002 supersedes TH-C1-CONT-005:
  **Actual S03 PDF54row6→PDF55row1**, **NOT53→54**.
  U2005 `theg pa dag ni gnyis su 'dod`
  `gzhi ni 'jig rten pa yin te`
  `'di las 'dod pa gnyis yin no`
  `'das pa rgyu dang` ends54row6, `'bras bu las` opens55row1
  thenU2006 `rgyu la gsum la 'bras bur gnyis`.
  Evidence `p054-s03-row6.png` `[740,298,1940,385]`,scale2
  `p055-s03-row1.png` `[455,77,1505,157]`,scale2
- `tharpaling-s02-s03-correct.py` run ONCE. Not idempotent. Later adjustedS02bounds manually in allJSONs.
- Old continuation004/005 active status withdrawn,currentdescription,scope,rationale; `prior_claim_snapshot` retainsfalseclaim.
- Snapshots `tharpaling-continuation.before-s02-s03-correction.json/.md`.
- MD prominent correction banner, historicaloldtext retained labeledfalse.
- Root message latest:
  “TH-LATE-001/002 correction records saved ... Current late checkpoint contains restoration checks only; ...proceeding sequential44–71 ...”
- Root already integrated S01, nowhasS02S03files.

Helpers/current rendering:
- `tharpaling-middle-render.py` args page numbers. Reads native PNG, creates L/R in `tharpaling-middle-crops/`, at2×, automatically display-inverts if mean gray<100.
- Current bounds (for pages33onward including44+):
  L `[0,50,1160,410]`
  R `[1030,50,native_width,410]`
- Earlier17–32crops bound L `[130,65,1160,375]`, R `[1030,65,width-150,375]`.
  p20 initialcropsreversepolarity, extra `p020-L-inv.png`,`p020-R-inv.png` inspected.
- Native fullpageskeeporiginal.
- `tharpaling-middle-loci.py LO HI` outputs EWTS A/B electronic conflict queries only lexicalnormalized. Useful to target differences but **B includes conflated interlinear notes and can mislead; not evidence.**
- `sed -n '1599,1640p' gadkar-base-ewts.txt` yieldsbaseunits.
- Croppingandimageviewvia functions. Be careful don't requesttoo manyimages+longtext once; lastoutputtruncated.
- `tharpaling-middle-finalize.py` already wrote finalmiddle. It readsnotes and APPENDS37–43 internally, so rerunwithoutmodifyingnotes okay but not afterappendingnewpages notes; betterdon'trerununlessintentional.
- `tharpaling-middle-notes.json` originalcheckpoint has17–36 only; finalmiddle37–43addedatgenerator. Active44+use late-notes separate.

Middle confirmed page endpoints:
17U568partial–600partial
18U600partial–639partial
19U639partial–675
20U676heading–722
21U723–756heading
22U756headingcontinuation/757–796
23U797–835partial
24U835partial–875partial
25U875partial–917partial
26U917partial–956
27U957–993
28U994–1034
29U1035–1069
30U1070–1107
31U1108–1143
32U1145–1184partial
33U1184partial–1225
34U1226–1264
35U1265–1304partial
36U1304partial–1334partial **corrected**
37U1334partial–1373partial
38U1373partial–1409
39U1410–1449partial
40U1449partial–1485
41U1486–1523partial
42U1523partial–1562
43U1563–1598 **correctedsequential**
43row anchors:
r1U1563–1567
r2U1568–1573
r3U1574–1580partial
r4continues1580–1585
r5U1586 onward
r6U1591 onward, smallreply34heading,1597thiglechosnyidbrtan'dodpas,1598dondamdangnikunrdzoblas.

Important reliability lesson:
Expectedformulae causedfalsealignment. Always anchor frompreviouspage+multiple consecutiveactualvisiblephrases, thenlastpage boundarycheck. If unclear, marklocatoruncertain, do not assumeagreement. We must explicitly preserveanynewwithdrawals. No claims of exhaustive completion to helpuseradvance.

Useful sourcecorrectionsfiles rootmightuse:
`tharpaling-middle.json/.md`
`tharpaling-s01-correction.json`
`tharpaling-s02-s03-corrections.json`
`tharpaling-continuation.json/.md` current withallwithdrawals
`langtang-late.json/.md`
Allscratchroot absolute `/workspace/scratch/a117ee885aff/...`.

---

Recovery note: the compacted state also included an early, nonsequential guess that PDF50 began U1817. That guess was corrected in the later retained failed checkpoint text to U1827. The earlier guess is not promoted here. The scripts and original status messages identify PDF52–71 as pending; no completed late report should be inferred from the existence of targeted later-page checks.
