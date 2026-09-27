#!/usr/bin/env python3
"""Render the explicitly provisional Chapter 1 and its source-controlled apparatus."""
import argparse
import collections
import hashlib
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', required=True, type=Path)
    args = p.parse_args()
    root = args.repo.resolve()
    out = root / 'diplomatic'
    data = out / 'collation/chapter-01'
    read = lambda name: json.loads((data / name).read_text())
    for meta in read('chapter1-summary.json')['sources'].values():
        observed = hashlib.sha256((root / meta['path']).read_bytes()).hexdigest()
        assert observed == meta['full_file_sha256'], 'Source changed: ' + meta['path']
    units = json.loads((root / 'translations/2026-09-26-full-draft/data/source-units.json').read_text())[:2635]
    by_id = {u['id']: u for u in units}
    original = (root / 'editions/adzom-2000/W1KG11703_7.txt').read_text()[:76376]
    assert ''.join(u['tibetan'] for u in units) == original
    loci = read('chapter1-loci.json')
    raw = {x['id']: x for x in read('chapter1-conflicts.json')}
    web = read('wikisource-diffs.json')
    insertions = read('ch1-scan-insertions.json')
    opening = read('ch1-opening-corrections.json')
    checks = read('ch1-key-scan-checks.json')['items']
    notes = []
    replacements = {}
    consumed = set()
    annotation_links = collections.defaultdict(list)
    insert_after = collections.defaultdict(list)

    def link(ident):
        return f'[{ident}](#{ident.lower()})'

    def evidence(paths):
        for path in paths:
            assert (out / path).is_file(), path
        return ', '.join(f'[{Path(x).name}]({x})' for x in paths)

    for rec in opening:
        uid = rec['unit']
        assert by_id[uid]['tibetan'] == rec['old']
        replacements[uid] = rec['new']
        notes.append({'id': rec['id'], 'units': [uid], 'old': rec['old'], 'new': rec['new'],
                      'rationale': rec['rationale'], 'locator': f"PDF {rec['pdf_page']}; BDRC image {rec['bdrc_image']}; {rec['scan_location']}",
                      'evidence': rec['evidence_images'], 'confidence': rec['confidence']})

    for rec in checks:
        for uid, text in rec['original_units'].items():
            assert by_id[uid]['tibetan'] == text
        first, *rest = rec['units']
        assert not (set(rec['units']) & set(replacements))
        replacements[first] = rec['adopted_tibetan']
        consumed.update(rest)
        for uid in rest:
            replacements[uid] = ''
        loc = rec['scan_locator']
        notes.append({'id': rec['id'], 'units': rec['units'], 'old': rec['original_tibetan'],
                      'new': rec['adopted_tibetan'], 'rationale': rec['rationale'],
                      'locator': f"PDF {loc['pages']}; BDRC images {loc['bdrc_images']}; {loc['location']}",
                      'evidence': rec['evidence_crop'], 'confidence': rec['confidence'],
                      'annotation': rec['separate_unchanged_transcript_annotation'],
                      'prior_report': rec['conflict_with_existing_report']})

    for rec in notes:
        for uid in rec['units']:
            annotation_links[uid].append(link(rec['id']))
    for rec in insertions:
        assert rec['after_unit'] in by_id
        insert_after[rec['after_unit']].append(rec)
        annotation_links[rec['after_unit']].append(link(rec['id']))
    for group in insert_after.values():
        group.sort(key=lambda x: x['anchor_sequence'])
    for rec in loci:
        for uid in rec['source_units']:
            annotation_links[uid].append(link(rec['id']))
    for rec in web['conflicts']:
        us = rec['source_units']
        if us:
            for u in us:
                annotation_links[u['id']].append(f"[{rec['id']}](reviews/chapter-01/wikisource.md#{rec['id'].lower()})")
        elif rec.get('source_before') in by_id:
            annotation_links[rec['source_before']].append(f"[{rec['id']}](reviews/chapter-01/wikisource.md#{rec['id'].lower()})")
    for uid in ['U00013', 'U00014', 'U00022', 'U00023', 'U00027']:
        annotation_links[uid].append('[Tingkye/Degé scan variant](reviews/chapter-01/independent-openings.md#conflicts-that-can-be-reported-conservatively)')
    for uid in ['U00012', 'U00018', 'U00019', 'U00026']:
        annotation_links[uid].append('[Comparison-scan uncertainty](reviews/chapter-01/independent-openings.md#other-observations-and-uncertainties)')

    doc = ['# Chapter 1 — provisional diplomatic reading and apparatus', '',
           '**IN PROGRESS: this chapter has not passed the complete-witness collation gate.**', '',
           'The reading text represents all 2,635 supplied Adzom e-text units, with individually documented scan corrections and restorations. Most base text has not yet been proofread against the facsimile. The apparatus covers every exact A/B/S transcript difference and the separately defined W comparison; it does not cover every conflict in the scan-only editions.', '',
           '[Editorial method](METHOD.md) · [Source inventory](SOURCES.md) · [Status](STATUS.json) · [W apparatus](reviews/chapter-01/wikisource.md)', '',
           '## Coverage and notation', '',
           '- A: Adzom supplied transcript; B: Tharpaling supplied transcript; S: Sichuan supplied transcript; W: related Wikisource Wylie transcription. These are transcript sigla, not independent print attestations.',
           '- The A-scan governs adopted corrections. U identifiers locate the unchanged e-text; A2000-C01-S identifiers locate additional scan text. Neither set represents physical verse numbering.',
           '- Blank lines and trimmed boundary whitespace are editorial display choices. Exact quotations and offsets remain in the apparatus ledger. Scan restorations use readable Unicode punctuation, not a reproduction of variable physical spaces or fill marks.',
           '- Source headings, the provisional portrait caption, and the unread chapter-boundary inscription are explicitly distinguished. Other interleaved annotations remain unseparated where inspection is still outstanding.',
           '- The five observed Tingkye/Degé comparison loci are in the [limited scan report](reviews/chapter-01/independent-openings.md). [Langtang opening continuity](reviews/chapter-01/langtang-opening-gap.md) is a boundary inspection only.', '',
           '## Reading text', '']
    output_units = []
    for u in units:
        uid = u['id']
        doc += [f'<a id="{uid.lower()}"></a>', '']
        if uid in consumed:
            text = '[Main text joined with the preceding unit by the linked scan decision; the original unit is retained in the apparatus.]'
        else:
            text = replacements.get(uid, u['tibetan'])
        refs = ' '.join(dict.fromkeys(annotation_links[uid]))
        source_role = '**[Source structural heading]** ' if uid in ['U00011', 'U00029'] else ''
        doc += [f'**{uid}** {source_role}{text.strip()}' + (f' {refs}' if refs else ''), '']
        output_units.append({'id': uid, 'source_tibetan': u['tibetan'], 'reading_tibetan': replacements.get(uid, u['tibetan']),
                             'status': 'scan_intervention' if uid in replacements else 'unverified_transcription_scaffold'})
        for ins in insert_after[uid]:
            label = {'main_text_restoration': 'Restored main text', 'source_heading_restoration': 'Restored source heading',
                     'source_caption_provisional': 'Portrait caption — provisional reading; editorial placement',
                     'scan_only_unresolved': 'Scan-only inscription — unread'}[ins['kind']]
            body = '\n\n'.join(ins['tibetan_lines']) if ins['tibetan_lines'] else '[Reading unresolved; see the facsimile evidence in the note.]'
            doc += [f'**{label} — {link(ins["id"])}**', '', body, '']

    doc += ['## Scan interventions', '',
            'These decisions supersede provisional e-text retention in the comparative apparatus. Quoted A remains the unchanged transcript; the reading text follows the individually inspected scan locus.', '']
    for rec in notes:
        doc += [f'<a id="{rec["id"].lower()}"></a>', '', f'### {rec["id"]}', '',
                'Units: ' + ', '.join(f'[{u}](#{u.lower()})' for u in rec['units']) + '.', '',
                f'**A transcript:** {rec["old"]}', '', f'**Adopted reading:** {rec["new"]}', '',
                f'**Scan locator:** {rec["locator"]}.', '', f'**Decision and reason:** {rec["rationale"]}', '']
        if rec.get('annotation'):
            doc += [f'**Transcript annotation retained separately; provenance unresolved:** {rec["annotation"]}', '']
        if rec.get('prior_report'):
            doc += [f'**Earlier report cross-check:** {rec["prior_report"]}', '']
        confidence = json.dumps(rec['confidence'], ensure_ascii=False) if isinstance(rec['confidence'], dict) else rec['confidence']
        doc += [f'**Confidence and limits:** {confidence}', '', '**Evidence:** ' + evidence(rec['evidence']), '']
    for rec in insertions:
        doc += [f'<a id="{rec["id"].lower()}"></a>', '', f'### {rec["id"]}', '',
                f'After [{rec["after_unit"]}](#{rec["after_unit"].lower()}); before {rec["before_unit"]}. **{rec["kind"]}**.', '',
                '**Reading:** ' + (' / '.join(rec['tibetan_lines']) or '[Unresolved inscription; no transcription adopted.]'), '',
                f'**Locator:** PDF {rec["pdf_page"]}; BDRC image {rec["bdrc_image"]}; {rec["scan_location"]}', '',
                f'**Decision and reason:** {rec["rationale"]}', '',
                f'**Confidence:** {rec["confidence"]}. **Remaining uncertainty:** {rec["remaining_uncertainty"]}', '',
                f'**Punctuation:** {rec["punctuation_policy"]}', '', '**Evidence:** ' + evidence(rec['evidence_images']), '']

    doc += ['## A/B/S transcript apparatus', '',
            'All 359 exact differences are represented once in the following 183 readable loci. Complete source-unit quotations avoid splitting Tibetan combining sequences. A/B/S offsets are zero-based half-open Unicode-character ranges in the original full files. Empty readings, where present, are transcript absences only. These quotations preserve exact strings, including delimiters; fenced presentation protects punctuation from Markdown.', '',
            '[Exact patches](collation/chapter-01/chapter1-conflicts.json) · [Whole-unit loci](collation/chapter-01/chapter1-loci.json) · [Input hashes and scope](collation/chapter-01/chapter1-summary.json) · [Reconstruction verification](collation/chapter-01/validation.json)', '']
    decisions = []
    for rec in loci:
        involved = [n for n in notes if set(n['units']) & set(rec['source_units'])]
        added = [n for n in insertions if n['after_unit'] in rec['source_units']]
        classes = collections.Counter(raw[i]['classification'] for i in rec['exact_conflicts'])
        if involved or added:
            reason = 'The reading text follows the linked scan intervention(s) for the inspected material: ' + ', '.join(link(n['id']) for n in involved + added) + '. Elsewhere within this locus A is retained provisionally. The raw A/B/S quotations remain unchanged to preserve the transcript evidence.'
        elif set(classes) == {'punctuation_or_spacing'}:
            reason = 'Retain A’s punctuation/spacing provisionally under the base-transcription policy. Do not silently normalize the B/S delimiters into A; their exact forms remain quoted. Print punctuation is not yet verified at this locus.'
        elif set(classes) <= {'punctuation_or_spacing', 'editorial_bracket_or_spacing'}:
            reason = 'Retain A’s wording provisionally and record the alternative brackets/delimiters as transcript presentation evidence. S’s braces do not, by themselves, establish the position or status of an annotation in the Adzom printing. Scan-layout verification remains outstanding.'
        else:
            reason = 'Retain A provisionally because the selected diplomatic base is Adzom. B/S disagreement is preserved, but unverified transcripts, majority agreement, grammatical preference, and doctrinal expectations do not authorize changing the base witness. This is a pending scan decision, not a finding that A is the original or superior reading.'
        decisions.append({'locus': rec['id'], 'adopted_basis': 'A-scan at explicitly linked interventions; A scaffold elsewhere',
                          'decision': reason, 'status': 'provisional; complete print collation outstanding',
                          'scan_intervention_ids': [n['id'] for n in involved + added]})
        doc += [f'<a id="{rec["id"].lower()}"></a>', '', f'### {rec["id"]}', '',
                'Units: ' + ', '.join(f'[{u}](#{u.lower()})' for u in rec['source_units']) + '.', '',
                'Exact differences: ' + ', '.join(rec['exact_conflicts']) + '.', '']
        for k in ('A', 'B', 'S'):
            doc += [f'**{k} [{rec["offsets"][k][0]}, {rec["offsets"][k][1]}):**', '', '```text', rec['readings'][k], '```', '']
        doc += ['**Disposition and reason:** ' + reason, '']
    doc += ['## Remaining work before a completed-chapter commit', '',
            'Chapter 1 requires full Adzom scan proofreading, continuous collation of the acquired comparison scans, and resolution or explicit treatment of their unreadable spans. Degé’s faint main-line endings and small interlinear material could not be read reliably in the tested continuous span; the [scan report](reviews/chapter-01/independent-openings.md) gives exact limits. The title’s ornamental/Sanskrit material and the compressed inscription after the chapter colophon remain unresolved. The supplied e-text’s other interleaved annotation layers also require verification; earlier scan-review claims are not automatically authoritative.', '',
            'Sichuan can currently be cited only as its supplied transcript where no full scan is available. Adzom 1973–1977 and Gcn need verified root mappings before collation. Catalogue-only leads are recorded in SOURCES.md and are not counted as collated witnesses. Chapters 2–6 have not been started in this edition.', '']
    (out / 'chapter-01.md').write_text('\n'.join(doc))
    (data / 'editorial-decisions.json').write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + '\n')
    (data / 'reading-units.json').write_text(json.dumps(output_units, ensure_ascii=False, indent=2) + '\n')
    status = {
        'source_commit': 'e17a496ad7532cc627f9ba288b541f7a53efd002',
        'current_chapter': 1, 'complete_chapters': [], 'next_chapter_started': False,
        'chapter_1_status': 'in_progress_not_ready_for_completed_chapter_commit',
        'base_units_accounted_for': len(units), 'exact_transcript_conflicts': len(raw),
        'readable_loci': len(loci), 'wikisource_lexical_blocks': len(web['conflicts']),
        'scan_restored_main_verse_lines': sum(len(x['tibetan_lines']) for x in insertions if x['kind'] == 'main_text_restoration'),
        'scan_restored_source_headings': sum(len(x['tibetan_lines']) for x in insertions if x['kind'] == 'source_heading_restoration'),
        'scan_correction_or_layer_separation_records': len(notes),
        'base_scan_fully_proofread': False, 'all_acquired_witnesses_fully_collated': False,
        'complete_every_conflict_claim': False,
        'unresolved': ['Continuous base-scan proofreading', 'Continuous comparison-scan collation',
                       'Faint Degé endings and interlinear material need reliable reading',
                       'Adzom title ornamental/Sanskrit text', 'Adzom PDF102 inscription',
                       'Origin and physical status of transcript-inserted alternatives',
                       'Root mapping of Adzom1973 and Gcn containers', 'Sichuan full scan unavailable'],
        'chapter_markdown_sha256': hashlib.sha256((out / 'chapter-01.md').read_bytes()).hexdigest(),
    }
    (out / 'STATUS.json').write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(status, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
