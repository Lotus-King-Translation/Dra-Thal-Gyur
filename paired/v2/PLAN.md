# paired-text/2 structural migration — issue #4

Status: audit in progress. Publication is not yet authorized by a passed gate.
The user-requested scope includes final signoff, annotated immutable v2 tag,
remote verification, and a later publication receipt committed on main.

## Fixed scope

Audit all 2,660 v1 pairs and their 5,484 released golden objects, classify from
Tibetan/editorial structure as prose, verse, h1, h2 or h3, and split every actual
format boundary. Preserve all words, notes, roles and source order. The only
canonical paired content remains source.md and translation.md.

Baseline main: `aae8883b13ff0f23da2603aecc12a64a15ffe25b` (merged PR #3).
Template: Lotus-King-Translation/tibetan-text-project-template at
`f6431c25c7c9fa852c404b8cd3e0e3cdeae1178f`; immutable reference copies of its
FORMAT.md and AGENTS.md are under reference/. They document the schema read
for this migration and are supporting evidence, not new canonical content.
The governing source and English release pins remain those in paired/core.py.

Startup: clean tree, main fast-forwarded to the exact baseline; both remote tag
objects and peeled commits verified unchanged. Existing corpus validation and
canonical/manifest reproducibility checks pass before edits.

## Batches and gate

1. Source-based structural audit: all existing pairs, heading hierarchy,
   explicit treatment of paratext and empty source layers, uncertain decisions.
2. Canonical v2 schema/segmentation with complete v1-to-v2 lineage; parser,
   validator, generated manifest, tests and documentation.
3. Independent structural and implementation review, final validation,
   corruption tests and saved signoff.
4. Annotated `dra-thal-gyur-paired-v2.0.0` tag, verified remote tag object and
   peeled commit; publication receipt on main; remote main and clean-tree check.

No new translation, source correction, glossary assignment or semantic QC.
The 23 restored verses, 173 reconciliation endnotes, 340 earlier-note IDs,
65 source-annotation components and 18 closing anchors must survive.
Every substantive batch is committed/pushed and its remote SHA verified.
