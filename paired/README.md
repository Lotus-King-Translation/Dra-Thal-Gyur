# Paired Tibetan and English — paired-text/1

[Source](source.md) · [Translation](translation.md) · [Provenance](MIGRATION.md)

2,660 pairs cover all 5,484 golden objects, with 23 restored verses,
173 reconciliation endnotes and 18 closing anchors. [Coverage](MANIFEST.json).

`source.md` and `translation.md` are the only canonical paired content files.
Python helpers and generated reports support them; they are not editorial authorities.
The immutable input editions remain authoritative for this migration's wording.

## Format

UTF-8, LF, minimal `key: value` front matter, followed by ordinary Markdown.
Both files declare `schema: paired-text/1`, `text-id: dra-thal-gyur`,
`paired-edition: dra-thal-gyur-paired-v1.0.0`, and
`source-edition: root-tantra-v1.0.0`. The English file also declares
`translation-edition: translation-golden-aligned-v1.0.0`; languages are `bo`/`en`.

```markdown
<!-- pair: DTG-000001 | golden: U00001 | roles: opening_title_or_sign | part: chapter-01 -->
༅།
<!-- /pair -->
```

The English opening comment is simply `<!-- pair: DTG-000001 -->`.
Each shared pair ID is defined once per side, in the same order; note links
may reference it repeatedly.
`golden` and `roles` are space-separated, positionally aligned lists; `part`
is `chapter-01` through `chapter-06` or `closing-material`. Roles retain the
released values, including mixed-role pairs. IDs do not depend on headings.
Explicit lowercase HTML anchors make pair links work in rendered Markdown.

Payload is everything after the opening comment's LF and before the LF
preceding `<!-- /pair -->`. The source payload is the exact selected strings
joined by **one LF**, including original whitespace, internal LFs and empty
strings. Do not trim, normalize Unicode, or add hard-break spaces to it.
Empty source strings are represented by their golden ID and explicit role.
English empty annotation/joined strings receive disclosed editorial markers;
no additional translated root text is invented.

English words, punctuation and order remain unchanged. `[N-*]` tokens become
links to preserved earlier notes; paragraph separators, explicit empty-layer
markers and attached note references are presentation additions. Every pair
also links the union of its machine-recorded earlier-note IDs. Reconciliation
footnotes are carried in full in `translation.md`, with rebased relative links
and pair backlinks that retain the underlying golden IDs. Source annotations,
uncertainties, prior scan records and boundary metadata remain in those notes
and their preserved linked evidence.

## Segmentation and identity

Initial migration groups adjacent objects through the inherited English's
sentence-ending punctuation; semicolons, colons, dashes and comma continuations
stay together. Trailing note tokens and the known bracketed editorial/number
notices do not manufacture sentence endings. Restored blocks are never split.
Source headings, graphics, captions and ornamental signs normally form separate
pairs. Empty source layers inside a sentence remain within its mixed-role pair.
The heading `SCAN-CH1-LAYER-02489` interrupts a sentence and remains inside that
pair; `U00315–U00318` is an introduction ending in a colon before “First reply”.
No group crosses a chapter/closing boundary.

These are translation units derived from existing syntax, not new semantic QC.
The published ID-to-object membership is fixed. Changed segmentation requires
a new paired edition with explicit old/new ID lineage; never rerun numbering
silently. A later translation revision must identify its pinned source edition.

## Commands

Run from the repository root with Python 3.11+ and the fixed Git tags available:

```sh
python3 -B paired/validate.py
python3 -B paired/test_paired.py
python3 -B paired/migrate.py --check
python3 -B paired/project.py --check
```

`migrate.py --initialize` is the one-time importer and refuses to overwrite
existing canonical files. `project.py` reads the canonical Markdown, validates
it, and writes only generated coverage/provenance reports. No third content
file or source/target alignment table is required to edit or consume a pair.
