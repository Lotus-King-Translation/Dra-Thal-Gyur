# Chapter 1 continuation after the second reading

The requested golden edition is **not complete**. The [comparison progress report](reviews/chapter-01/comparison-extension.md) supersedes earlier statements about witness progress. No chapter has passed the complete-witness gate. Chapter 1 is the only chapter under work; Chapters 2–6 and the closing material have not been started. The remote branch is `diplomatic/chapter-01-collation`.

## What is preserved

- All 2,635 original Chapter 1 anchors, exact A/B/S collation (359 minimal differences; 183 readable loci), and the defined 273-block W comparison. The original source strings remain unchanged.
- A continuous main-Tibetan lexical comparison through the Chapter 1 end: PDF5–50 and PDF51–101 have page-by-page ledgers; opening/boundary inspection covers the adjacent material. This is not a complete punctuation, typography, title-script or ornamental-sign certification.
- Thirteen restored main verses and one restored reply heading, checked again in the focused second reading and the continuous late pass.
- Five local transcription corrections: U00039 `stod` → `stong`; U00542 `smras` → `spras`; U01598 `rdzo ba` → `rdzob`; U02522 `gzhon pa'gyur` → `gzhon par 'gyur`; U02597 restored initial `dris` in the reply heading.
- A 41-record targeted annotation audit and additional interventions. The separately printed numerical notes at U01067/U01090/U01811–12 were found one physical line below the earlier narrow checks. Their previous non-observations are superseded explicitly. The printed U01811–12 alternative lacks the transcript's extra `kyang`.
- The repeated transcript gloss in U01233/U01237 represents one observed printed note within U01238. Its two original occurrences are preserved; its physical record appears once.
- Focused and partial comparison findings for Degé, Tingkye, Tsamdrak, Tharpaling and Dzongsar, plus the earlier Langtang opening continuity check. The current chapter links supported findings and unresolved candidates individually.

## Why the chapter is still blocked

The second comparison readings did not establish reliable continuous all-variant collation. In Tsamdrak, the images are largely sharp, but the reader could not reliably distinguish recurring Tibetan stacks and suffixes; this is a capability limit, not a general claim of source illegibility. Tingkye has analogous unresolved reading judgments. Tharpaling adds concrete obscured regions; its alternative provider PDF contains the same image detail. The exact reports retain examples, inspection bounds and what remains uncollated.

Dzongsar now has opening, middle and late main-lexical ledgers covering PDF2–121 through the Chapter1 colophon. The 13 restored base verses are corroborated. Local uncertain words, exact Sanskrit and small-note wording remain explicitly qualified; this is not all-punctuation certification. See the [current comparison extension](reviews/chapter-01/comparison-extension.md) for newly incorporated reports and ongoing ranges. No uninspected comparison span is treated as agreement. The other mapped witnesses and unresolved containers still require collation or root mapping.

The Adzom base itself retains explicit uncertainty at the title material, portrait caption, U01522 fused cluster, U02615 note, inked U02620 cluster, and compressed PDF102 inscription. These require qualified reading or explicitly maintained uncertainty. Physical punctuation/sign review also remains unfinished.

## Next required work

1. Obtain a qualified Tibetan manuscript/print reading or independently verified transcripts for the comparison witnesses. Resolve or precisely mark each uncertain span and collate the full Chapter 1 ranges. Do not supply expected wording where glyphs cannot be established.
2. Complete the remaining comparison witnesses and physical punctuation/paratext checks. Keep unavailable Sichuan print, unmapped containers and catalogue-only leads distinct from collated evidence.
3. Review the curated scan interventions against their evidence, run the validator and renderer, and make a completed-chapter commit only once its coverage declaration is true. Then proceed to Chapter 2, repeating the user's chapter-by-chapter commit sequence.

## Reproduction

From the repository root:

```bash
python3 diplomatic/tools/build_chapter1.py --repo .
python3 diplomatic/tools/validate_chapter1.py --repo .
```

The raw electronic collation can be reproduced separately with `collate_chapter1.py`, `collate_wikisource_ch1.py`, and `make_wikisource_report.py`; each accepts `--repo` and `--out`. Optional `--pyewts PATH` enables diagnostic conversion for W, never automatic adoption.

The machine-readable reading combines `reading-units.json` and `ch1-scan-insertions.json`. Curated changes are in `ch1-opening-corrections.json`, `ch1-key-scan-checks.json`, and `additional-interventions.json`. The renderer preserves all original U anchors, including anchors whose text is separated as source annotation or joined across an e-text split. `scan-comparison-loci.json` retains local comparison evidence and its uncertainty independently of the electronic patch apparatus.

Source baseline: `e17a496ad7532cc627f9ba288b541f7a53efd002`. Source hashes and offsets are in `chapter1-summary.json`. Do not regenerate against altered source files without first reviewing and recording the new baseline. Intentional trailing spaces inside exact source quotations are evidence, not formatting defects to normalize away.
