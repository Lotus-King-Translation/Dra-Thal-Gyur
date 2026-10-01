# Paired Tibetan and English — paired-text/2

[Source](source.md) · [Translation](translation.md) · [Manifest](MANIFEST.json)
· [Migration and lineage](MIGRATION.md) · [Handoff](HANDOFF.md)

**Edition:** `dra-thal-gyur-paired-v2.0.0`. Exactly two canonical content files:
`source.md` and `translation.md`. Code, decisions, audits and JSON reports are
supporting material. The immutable source/English releases govern wording.

| Pairs | prose | verse | h1 | h2 | h3 | Golden objects |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2,667 | 48 | 2,448 | 2 | 0 | 169 | 5,484 |

All 23 restored verses, 173 reconciliation endnotes, 340 earlier-note IDs,
65 source-annotation components and 18 closing anchors remain represented.

## Format and rendering

UTF-8, LF, `schema: paired-text/2`, `text-id: dra-thal-gyur`, and
`paired-edition: dra-thal-gyur-paired-v2.0.0` occur in both front matters.
The source declares `edition: root-tantra-v1.0.0`; both files also declare
`source-edition: root-tantra-v1.0.0`. English declares
`translation-edition: translation-golden-aligned-v1.0.0`. Languages are `bo`/`en`.

```markdown
<!-- pair: DTG-000839 | golden: U01880 U01881 U01882 A2000-C01-S02 U01883 U01884 | roles: main_text main_text main_text restored_main_text main_text main_text | part: chapter-01 | format: verse -->
[exact Tibetan payload]
<!-- /pair -->
```

The English opening comment is only `<!-- pair: DTG-000839 -->`.
Each pair is defined once per file, in identical source order. Note links may
reference it repeatedly. Source `golden` and `roles` lists align positionally;
`part` is `chapter-01` through `chapter-06`, or `closing-material`.
Exactly one **source-only** `format` is required; English inherits it by ID.

| format | Kanava type | initial_formatting |
| --- | --- | --- |
| prose | prose | body |
| verse | verse | body |
| h1 | prose | h1 |
| h2 | prose | h2 |
| h3 | prose | h3 |

The two title-leaf headings are h1; all 169 individually audited chapter-internal
rubrics are h3. The existing six chapter wrappers and separate closing wrapper
remain Markdown h2 outside pairs; no h2 golden object is invented. Naming formulas
inside the opening are prose, not repeated section headings. Neutral prose
carries empty/graphic editorial objects without claiming their unknown genre.
[The structural decisions](v2/STRUCTURE-DECISIONS.json) retain the evidence and
confidence limits for narrative formulas, captions and closing paratext.

Payload is everything after the opening comment's LF and before the LF
preceding `<!-- /pair -->`. Tibetan payloads are the exact selected strings
joined by one LF, including original whitespace, internal LFs and empty strings.
Do not trim, normalize Unicode or insert display markup into them. A renderer
uses `format` to choose body/verse/heading presentation, preserving verse line
breaks. Neither golden objects nor restored blocks are subdivided.

English words, punctuation and order remain unchanged. Presentation adds legacy
note links, explicit empty-layer markers, attached reconciliation references and
pair backlinks. Full endnotes remain in `translation.md`; underlying golden IDs,
annotations, uncertainties and earlier records stay reachable.

## Identity and lineage

V1 is pinned at `aae8883b13ff0f23da2603aecc12a64a15ffe25b`. Its complete
2,660-pair audit and v1-to-v2 lineage are in [PAIR-AUDIT.json](v2/PAIR-AUDIT.json).
Five pairs split at source-based format changes. Their old IDs retire; twelve
new children use DTG-002661–DTG-002672. All 2,655 unaffected IDs/memberships
remain unchanged. Numeric ID order is not source order; file order is authoritative.
A sentence may continue across structural boundaries. Do not move a heading
or combine prose/verse to conceal that continuation.

Tagged membership and formats are immutable. Later changes require a new paired
edition, explicit lineage where membership changes, and a new final gate.
No source or translation accuracy certification follows from these checks.

## Validation and publication

```sh
python3 -B paired/validate.py --require-final
python3 -B paired/test_paired.py
python3 -B paired/migrate.py --check
python3 -B paired/project.py --check
```

`migrate.py --upgrade-v2` accepts only the exact v1 canonical baseline;
`--initialize` refuses existing canonical files. Neither silently overwrites
edits. `project.py` validates canonical Markdown before generating the manifest
and full audit/lineage. `--require-final` demands saved hash-bound signoff.
The annotated tag is fixed before its verified publication receipt is committed
on main; the receipt must never move that tag. See [handoff](HANDOFF.md).

Run the validator belonging to the checkout being validated. `--repo` accepts
only that same resolved checkout; alternate roots are rejected so a corpus
cannot accidentally use another checkout’s structural decisions.
