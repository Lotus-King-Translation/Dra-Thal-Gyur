#!/usr/bin/env python3
"""Fail closed on pair, source, translation, note, identity or input corruption."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote
sys.dont_write_bytecode = True
from core import (ENGLISH, HERE, PARTS, PINS, ROOT, EDITION, SOURCE_TAG,
                  TRANSLATION_TAG, LINK_RE, check_protected, check_tags,
                  english_payload, js, load_authorities, parse, part,
                  render, require, sha, source_payload, unique)

# Published edition identity lock, independent of the migration grouping code.
# A changed segmentation needs a new edition with explicit old/new ID lineage.
IDENTITY_SHA256 = '44a3c8c5b50e932ec08e40d72a4075889521a189aaf40245e815e6a2f024fc0f'


def check_links(source, translation, root=ROOT):
    checked = set()
    for current, text in [('source.md', source), ('translation.md', translation)]:
        for match in LINK_RE.finditer(text):
            target = match[2]
            if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            path, sep, fragment = target.partition('#')
            if not path:
                content = text
            else:
                file = (root / 'paired' / unquote(path)).resolve()
                require(file.is_relative_to(root.resolve()), 'Link escapes repository: ' + target)
                require(file.is_file(), 'Missing linked evidence: ' + target)
                content = file.read_text(encoding='utf-8') if sep else ''
            if sep:
                require(f'id="{fragment}"' in content, 'Missing note/pair link anchor: ' + target)
            checked.add((current, target))
    return len(checked)


def validate_texts(source: str, translation: str, authorities):
    sources, translations = parse(source, 'bo'), parse(translation, 'en')
    source_ids = [s.ident for s in sources]
    translation_ids = [s.ident for s in translations]
    require(source_ids == translation_ids, 'Source/translation pair set or order mismatch')
    require(source_ids == [f'DTG-{i:06d}' for i in range(1, len(sources) + 1)],
            'Missing, reordered or renamed stable pair ID')
    gold = authorities.golden['reading_sequence']
    english = authorities.english['reading_sequence']
    golden_ids = [r['id'] for r in gold]
    by_golden = {r['id']: r for r in gold}
    by_english = {r['id']: r for r in english}
    flat = [ident for segment in sources for ident in segment.golden]
    counts = Counter(flat)
    require(not set(flat) - set(golden_ids), 'Unknown golden object reference')
    require(all(count == 1 for count in counts.values()), 'Golden object covered more than once')
    require(set(flat) == set(golden_ids), 'Golden object omitted (including restored/closing material)')
    require(flat == golden_ids, 'Golden object order changed')
    require(len(flat) == 5484, 'Golden object count is not 5484')
    identity = sha(js([[s.ident, s.golden] for s in sources]).encode())
    require(identity == IDENTITY_SHA256,
            'Published pair membership changed; new edition and explicit lineage required')
    groups = []
    for s, t in zip(sources, translations):
        rows = [by_english[i] for i in s.golden]
        groups.append(rows)
        require(s.roles == [by_golden[i]['role'] for i in s.golden], 'Golden role changed: ' + s.ident)
        require(all(part(r) == s.part for r in rows), 'Chapter/closing part changed: ' + s.ident)
        expected_source = '\n'.join(by_golden[i]['text'] for i in s.golden)
        require(s.text == expected_source, 'Selected Tibetan text/join differs: ' + s.ident)
        require(t.text == english_payload(rows), 'Released English/notes/markers differ: ' + s.ident)
    note_ids = [n['note_id'] for n in authorities.english['endnotes']]
    definitions = re.findall(r'^\[\^(G-[^\]]+)\]:', translation, re.M)
    references = re.findall(r'\[\^(G-[^\]]+)\](?!:)', '\n'.join(s.text for s in translations))
    require(len(definitions) == len(set(definitions)), 'Duplicate reconciliation endnote')
    require(set(definitions) == set(references) == set(note_ids) and len(definitions) == 173,
            'Lost, orphaned or unknown reconciliation endnote/reference')
    # Full-envelope comparison also catches text outside blocks, missing headings,
    # broken anchors, and mutations to exact carried note bodies/backlinks.
    require(source == render(authorities, groups, 'bo'),
            'Source structure/heading/anchor or extra unaccounted text differs')
    require(translation == render(authorities, groups, 'en'),
            'Translation structure/endnote text/backlink or extra unaccounted text differs')
    lookup = {i: segment.ident for segment in sources for i in segment.golden}
    restored = [g for g in gold if g['role'] == 'restored_main_text']
    require(sum(len(g['lines']) for g in restored) == 23, 'Restored verse count differs')
    closing = [r['id'] for r in english if part(r) == 'closing-material']
    require(closing == [f'U{i:05d}' for i in range(5449, 5467)], 'Closing anchor coverage differs')
    legacy_ids = unique(n for row in english for n in row['legacy_note_ids'])
    parts = []
    for name in PARTS:
        selected = [s for s in sources if s.part == name]
        parts.append({'part': name, 'pairs': len(selected),
                      'golden_objects': sum(len(s.golden) for s in selected),
                      'first_pair': selected[0].ident, 'last_pair': selected[-1].ident})
    endnotes = []
    for note in note_ids:
        anchors = [row['id'] for row in english if note in row['endnote_ids']]
        endnotes.append({'note': note, 'pairs': unique(lookup[i] for i in anchors), 'golden': anchors})
    return {
        'schema': 'paired-text-manifest/1', 'generated': True,
        'canonical_content': ['paired/source.md', 'paired/translation.md'],
        'paired_edition': EDITION, 'checks_passed': True,
        'pins': {tag: {'tag_object': v[0], 'commit': v[1]} for tag, v in PINS.items()},
        'canonical_sha256': {'source.md': sha(source.encode()), 'translation.md': sha(translation.encode())},
        'identity_sha256': identity,
        'projection_sha256': {
            'golden_ordered_id_text_records': sha(js([[g['id'], g['text']] for g in gold]).encode()),
            'english_ordered_id_text_records': sha(js([[r['id'], r['english']] for r in english]).encode()),
        },
        'counts': {
            'total_pairs': len(sources), 'expected_pairs': 2660,
            'original_source_anchors': sum(bool(re.fullmatch(r'U\d{5}', i)) for i in flat),
            'golden_objects_covered': len(flat), 'golden_objects_expected': 5484,
            'added_golden_objects': sum(not bool(re.fullmatch(r'U\d{5}', i)) for i in flat),
            'restored_objects': len(restored), 'restored_verses_retained': 23,
            'reconciliation_endnotes_retained': len(definitions),
            'legacy_note_ids_retained': len(legacy_ids),
            'legacy_object_note_associations_retained': sum(len(r['legacy_note_ids']) for r in english),
            'source_annotation_components_retained_in_notes': len(authorities.english['source_annotations']),
            'closing_anchors_retained': len(closing),
            'chapters': 6, 'closing_material_parts': 1,
            'unmatched_source_pairs': 0, 'unmatched_translation_pairs': 0,
            'duplicated_golden_objects': 0, 'omitted_golden_objects': 0,
            'split_golden_objects': 0,
            'grouped_pairs': sum(len(s.golden) > 1 for s in sources),
            'largest_pair_objects': max(len(s.golden) for s in sources),
        },
        'parts': parts,
        'roles': dict(sorted(Counter(g['role'] for g in gold).items())),
        'restored': [{'golden': g['id'], 'pair': lookup[g['id']], 'verses': len(g['lines'])}
                     for g in restored],
        'closing': [{'golden': i, 'pair': lookup[i]} for i in closing],
        'endnotes': endnotes,
        'protected_input_files': len(authorities.protected),
        'english_preservation': 'Exact released strings; only documented regrouping/markup/editorial empty-layer markers.',
        'semantic_retranslation': False, 'fresh_semantic_qc': False,
    }


def validate_repo(root=ROOT):
    root = Path(root)
    check_tags(root)
    authorities = load_authorities()
    check_protected(authorities, root)
    source = (root / 'paired/source.md').read_bytes().decode('utf-8')
    translation = (root / 'paired/translation.md').read_bytes().decode('utf-8')
    result = validate_texts(source, translation, authorities)
    result['local_links_checked'] = check_links(source, translation, root)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--full', action='store_true', help='Print the complete generated manifest')
    args = parser.parse_args()
    report = validate_repo(args.repo)
    print(js(report if args.full else {'checks_passed': True, 'counts': report['counts'],
          'protected_input_files': report['protected_input_files'],
          'local_links_checked': report['local_links_checked']}), end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit('PAIRED VALIDATION FAILED: ' + str(exc))
