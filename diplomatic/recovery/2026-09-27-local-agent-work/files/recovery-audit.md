# Recovery audit — 2026-09-27

**Original later apparatus remains missing.** All 54 pending report basenames in the recovery packet are absent from the working tree and reachable Git history; the current canonical list has 107 observations, against a historical 1,016 validated and later 1,024-record audit snapshot.
All 687 archived evidence files pass Git blob hash and size checks; A/B/S complete-file and Chapter1 hashes match. Chapter Markdown matches STATUS. Existing 2,635-anchor/359-conflict/183-locus foundation survives.
Scratch archive: parts 000–009 pass; 010–084 missing (157,252,187 bytes). Full archive must be 178,223,707 bytes, SHA256 `9475b82b7dae79239437f22f5d7cc408bae699867d25eb5b9b8b582f5dea4cd3`.
Even all 85 parts contain only 173 scratch files: 169 rasters, crop-map.json, map_crops.py, ch1-ewts.txt and tingkye-qc-read.txt. They do not contain the missing 54 reports. Preserve zero-byte gcn-464-view.png and gcn-481-view.png.

1. Recover missing archive parts from cloud filesystem or uploads; verify each part, joined hash, then every extracted path/size/hash against scratch-manifest.json. Keep original bytes.
2. Preserve retained scripts as text. Gcn initial report is self-contained; Tingkye audit needs missing metadata and claim snapshots; Tharpaling append scripts need missing prior JSON; integration audit needs absent 1,024-record canonical data.
3. Extract literal report fragments with provenance into distinct derivatives: 3 Tingkye audits, 4 saved Tharpaling pages + TH-LATE-003, 4 unsaved Tharpaling pages, Gcn 7 attempted-page records/5 findings, integration audit static findings. Do not manufacture dynamic fields.
4. Salvage packet records independently: 9 mandatory corrections, 10 guided omission audits, 4 Gcn notes, 4 Tharpaling notes, punctuation candidates, 11 restoration crossrefs and 2 mapping updates. Later qualifications supersede retained stale claims.
5. Current recovered-base-signs.json is a 41-unit scaffold with no completed changes. recovered-tharpaling.json has 5 pages/8 loci. Recovered raster p052.png is empty; preserve it as interrupted output.
6. Expose recovered material through chapter anchors with explicit recovered-history/uncertain status; read native evidence before upgrading any observation. Neither available archive nor scripts can recreate all 1,016 observations.
7. Keep archival originals untouched. Validator needs archival path handling: 30 relative links break solely in relocated byte-for-byte dzongsar-late.md; live copy exists and archived hash matches. validate_chapter1.py writes VALIDATION.json.
8. Rebuild and validate after integration; commit/push each substantive evidence/report batch. Chapter1 completion remains gated by continuous reliable witness collation and physical-sign review; remaining uncollated/unreadable ranges cannot become agreement.

Exact missing names, retained paths/dependencies and integrity results: `recovery-audit.json`. No repository changes or reconstruction scripts executed.
