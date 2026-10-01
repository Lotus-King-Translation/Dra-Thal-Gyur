#!/usr/bin/env python3
"""Deterministic stdlib acceptance/corruption checks; never mutate the corpus."""
from __future__ import annotations

from collections import Counter
import dataclasses
import io
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

import core
import structure
import validate
from validate import validate_texts


REJECTIONS = {}


def block(text, ident):
    return next(m for m in core.PAIR_RE.finditer(text) if m[1] == ident)


def replace_block(text, ident, transform):
    match = block(text, ident)
    return text[:match.start()] + transform(match[0]) + text[match.end():]


def replace_payload(text, ident, transform):
    match = block(text, ident)
    start, end = match.span(3)
    return text[:start] + transform(match[3]) + text[end:]


def unit(text, ident):
    match = block(text, ident)
    start = text.rfind('\n<a id=', 0, match.start())
    assert start >= 0 and text[start:match.start()] == f'\n<a id="{ident.lower()}"></a>\n\n'
    return text[start:match.end() + 1]


def drop(text, ident):
    return text.replace(unit(text, ident), '', 1)


def duplicate(text, ident):
    value = unit(text, ident)
    return text.replace(value, value + value, 1)


def swap(text, first, second):
    one, two = unit(text, first), unit(text, second)
    return text.replace(one, '\0PAIR-SWAP\0', 1).replace(two, one, 1).replace('\0PAIR-SWAP\0', two, 1)


def source_comment(ident, rows, format):
    """Construct corruption fixtures independently of the production renderer."""
    return (f"<!-- pair: {ident} | golden: {' '.join(row['id'] for row in rows)}"
            f" | roles: {' '.join(row['golden_role'] for row in rows)}"
            f" | part: {core.part(rows[0])} | format: {format} -->")


class PairedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.authorities = core.load_authorities()
        cls.source = (core.HERE / 'source.md').read_bytes().decode('utf-8')
        cls.translation = (core.HERE / 'translation.md').read_bytes().decode('utf-8')
        cls.segments = core.parse(cls.source, 'bo')
        cls.owners = {golden: segment for segment in cls.segments for golden in segment.golden}

    def reject(self, source=None, translation=None, reason=r'.+'):
        with self.assertRaisesRegex(ValueError, reason) as caught:
            validate_texts(self.source if source is None else source,
                           self.translation if translation is None else translation,
                           self.authorities)
        REJECTIONS[self._testMethodName] = str(caught.exception)

    def source_change(self, golden, old, new):
        ident = self.owners[golden].ident
        self.assertIn(old, block(self.source, ident)[0])
        return replace_block(self.source, ident, lambda value: value.replace(old, new, 1))

    def test_positive_released_corpus(self):
        manifest = validate_texts(self.source, self.translation, self.authorities)
        self.assertIsInstance(manifest, dict)
        core.check_protected(self.authorities)
        source_ids = [segment.ident for segment in self.segments]
        target_ids = [segment.ident for segment in core.parse(self.translation, 'en')]
        self.assertEqual(source_ids, target_ids)
        self.assertEqual(len(source_ids), 2667)
        golden = [golden for segment in self.segments for golden in segment.golden]
        self.assertEqual(golden, [row['id'] for row in self.authorities.golden['reading_sequence']])
        self.assertEqual(len(golden), 5484)
        self.assertEqual(len(set(golden)), 5484)

    def test_positive_grouping_examples(self):
        # Independent, reviewed examples, not expectations rerendered by grouping().
        expected = [
            ['U00315', 'U00316'],
            ['U00317', 'U00318'],
            ['U01191', 'U01192'],
            ['U01193', 'U01194', 'U01195', 'U01196'],
            ['U01880', 'U01881', 'U01882', 'A2000-C01-S02', 'U01883', 'U01884'],
            ['U02488', 'U02489'],
            ['SCAN-CH1-LAYER-02489'],
            ['U02490', 'U02491', 'U02492'],
            ['U02613', 'U02614'],
            ['U02615'],
            ['U02616'],
            ['A2000-C03-S01', 'U03716'],
            ['U01449', 'U01450', 'U01451', 'U01452', 'U01453'],
            ['U01899', 'U01900'],
            ['U02700', 'U02701', 'U02702'],
            ['U02721', 'U02722', 'U02723'],
            ['U03439', 'U03440', 'U03441'],
        ]
        for membership in expected:
            with self.subTest(golden=membership[0]):
                self.assertEqual(self.owners[membership[0]].golden, membership)
        self.assertEqual(self.owners['U02743'].golden, ['U02743'])
        self.assertEqual(self.owners['U00317'].roles[-2:],
                         ['source_annotation_anchor', 'source_annotation_anchor'])
        self.assertEqual(self.owners['SCAN-CH1-LAYER-02489'].roles[0], 'source_heading')
        self.assertEqual(self.owners['U01880'].roles[3], 'restored_main_text')

    def test_positive_false_terminal_notices(self):
        for ident in ['U01449', 'U01899', 'U02700', 'U02722', 'U03440']:
            row = next(row for row in self.authorities.english['reading_sequence'] if row['id'] == ident)
            with self.subTest(golden=ident):
                self.assertFalse(core.ends_sentence(row['english']))
        row = next(row for row in self.authorities.english['reading_sequence'] if row['id'] == 'U02743')
        self.assertTrue(core.ends_sentence(row['english']))

    def test_positive_structural_formats(self):
        examples = {'U00005': 'prose', 'U00013': 'verse', 'U00004': 'h1', 'U00011': 'h3'}
        for golden, expected in examples.items():
            with self.subTest(golden=golden):
                self.assertEqual(self.owners[golden].format, expected)
        counts = Counter(segment.format for segment in self.segments)
        self.assertEqual({name: counts[name] for name in ('prose', 'verse', 'h1', 'h2', 'h3')},
                         {'prose': 48, 'verse': 2448, 'h1': 2, 'h2': 0, 'h3': 169})
        manifest = validate_texts(self.source, self.translation, self.authorities)
        for name in ('prose', 'verse', 'h1', 'h2', 'h3'):
            self.assertEqual(manifest['counts'][name + '_pairs'], counts[name])
        self.assertEqual(structure.KANAVA, {
            'prose': {'type': 'prose', 'initial_formatting': 'body'},
            'verse': {'type': 'verse', 'initial_formatting': 'body'},
            'h1': {'type': 'prose', 'initial_formatting': 'h1'},
            'h2': {'type': 'prose', 'initial_formatting': 'h2'},
            'h3': {'type': 'prose', 'initial_formatting': 'h3'},
        })

    def test_positive_translation_inherits_formats(self):
        for match in core.PAIR_RE.finditer(self.translation):
            self.assertEqual(match[2], '', match[1])
        self.assertEqual([segment.ident for segment in core.parse(self.translation, 'en')],
                         [segment.ident for segment in self.segments])

    def test_positive_complete_v1_v2_lineage(self):
        audit = json.loads((core.HERE / 'v2/PAIR-AUDIT.json').read_text(encoding='utf-8'))
        lineage = audit['lineage']
        baseline = structure.baseline_pairs()
        self.assertEqual(len(lineage), 2660)
        self.assertEqual([entry['v1'] for entry in lineage], [row['id'] for row in baseline])
        self.assertEqual([entry['v1_golden'] for entry in lineage], [row['golden'] for row in baseline])
        children = [child for entry in lineage for child in entry['v2']]
        self.assertEqual([(row['id'], row['golden'], row['format']) for row in children],
                         [(segment.ident, segment.golden, segment.format) for segment in self.segments])
        changed = {entry['v1']: [(child['id'], child['format'], child['golden'])
                               for child in entry['v2']]
                   for entry in lineage if entry['membership_changed']}
        self.assertEqual(changed, {
            'DTG-000010': [('DTG-002661', 'prose', ['U00012']),
                           ('DTG-002662', 'verse', ['U00013', 'U00014', 'U00015', 'U00016', 'U00017'])],
            'DTG-000017': [('DTG-002663', 'prose', ['U00030']),
                           ('DTG-002664', 'verse', ['U00031', 'U00032'])],
            'DTG-000165': [('DTG-002665', 'verse', ['U00315', 'U00316']),
                           ('DTG-002666', 'prose', ['U00317', 'U00318'])],
            'DTG-001124': [('DTG-002667', 'verse', ['U02488', 'U02489']),
                           ('DTG-002668', 'h3', ['SCAN-CH1-LAYER-02489']),
                           ('DTG-002669', 'verse', ['U02490', 'U02491', 'U02492'])],
            'DTG-001185': [('DTG-002670', 'verse', ['U02613', 'U02614']),
                           ('DTG-002671', 'prose', ['U02615']),
                           ('DTG-002672', 'verse', ['U02616'])],
        })
        current_ids = {segment.ident for segment in self.segments}
        self.assertTrue(set(changed).isdisjoint(current_ids))
        unchanged = [entry for entry in lineage if not entry['membership_changed']]
        self.assertEqual(len(unchanged), 2655)
        for entry in unchanged:
            self.assertEqual(len(entry['v2']), 1)
            self.assertEqual(entry['v2'][0]['id'], entry['v1'])
            self.assertEqual(entry['v2'][0]['golden'], entry['v1_golden'])
        self.assertEqual([child['id'] for entry in lineage if entry['membership_changed']
                          for child in entry['v2']], [f'DTG-{number:06d}' for number in range(2661, 2673)])
        self.assertNotEqual([segment.ident for segment in self.segments], sorted(current_ids))

    def test_reject_missing_format(self):
        self.reject(source=self.source_change('U00005', ' | format: prose', ''),
                    reason=r'(?i)format|metadata')

    def test_reject_unsupported_format(self):
        self.reject(source=self.source_change('U00005', 'format: prose', 'format: stanza'),
                    reason=r'(?i)format')

    def test_reject_duplicate_source_format(self):
        self.reject(source=self.source_change('U00005', 'format: prose', 'format: prose | format: verse'),
                    reason=r'(?i)format|metadata')

    def test_reject_format_only_on_english(self):
        ident = self.owners['U00005'].ident
        source = self.source_change('U00005', ' | format: prose', '')
        translation = replace_block(self.translation, ident,
                                    lambda text: text.replace(' -->', ' | format: prose -->', 1))
        self.reject(source, translation, reason=r'(?i)format|metadata')

    def test_reject_format_duplicated_on_english(self):
        ident = self.owners['U00005'].ident
        translation = replace_block(self.translation, ident,
                                    lambda text: text.replace(' -->', ' | format: prose -->', 1))
        self.reject(translation=translation, reason=r'(?i)format|metadata')

    def test_reject_multiple_english_format_fields(self):
        ident = self.owners['U00005'].ident
        translation = replace_block(self.translation, ident,
                    lambda text: text.replace(' -->', ' | format: prose | format: prose -->', 1))
        self.reject(translation=translation, reason=r'(?i)format|metadata')

    def test_reject_all_format_metadata_lost(self):
        self.reject(source=re.sub(r' \| format: (?:prose|verse|h1|h2|h3)', '', self.source),
                    reason=r'(?i)format|metadata')

    def test_reject_format_changed(self):
        self.reject(source=self.source_change('U00013', 'format: verse', 'format: prose'),
                    reason=r'(?i)format')

    def test_reject_heading_rank_changed(self):
        self.reject(source=self.source_change('U00011', 'format: h3', 'format: h2'),
                    reason=r'(?i)format')

    def test_reject_rejoined_mixed_format_pair(self):
        # Restore the former prose+verse pair without losing or changing source words.
        rows = {row['id']: row for row in self.authorities.english['reading_sequence']}
        first, second = self.owners['U00012'].ident, self.owners['U00013'].ident
        membership = self.owners['U00012'].golden + self.owners['U00013'].golden
        selected = [rows[golden] for golden in membership]
        source = replace_block(self.source, first, lambda _:
                               source_comment(first, selected, 'prose') + '\n' +
                               core.source_payload(selected) + '\n<!-- /pair -->')
        translation = replace_payload(self.translation, first, lambda _: core.english_payload(selected))
        source, translation = drop(source, second), drop(translation, second)
        self.assertEqual([golden for segment in core.parse(source, 'bo') for golden in segment.golden],
                         [golden for segment in self.segments for golden in segment.golden])
        self.reject(source, translation, reason=r'(?i)format boundary')

    def test_reject_missing_source_pair(self):
        self.reject(source=drop(self.source, 'DTG-000002'), reason=r'(?i)pair')

    def test_reject_missing_translation_pair(self):
        self.reject(translation=drop(self.translation, 'DTG-000002'), reason=r'(?i)pair')

    def test_reject_missing_both_pairs(self):
        self.reject(drop(self.source, 'DTG-000002'), drop(self.translation, 'DTG-000002'))

    def test_reject_duplicate_source_pair(self):
        self.reject(source=duplicate(self.source, 'DTG-000002'), reason=r'(?i)duplicate.*pair')

    def test_reject_duplicate_translation_pair(self):
        self.reject(translation=duplicate(self.translation, 'DTG-000002'), reason=r'(?i)duplicate.*pair')

    def test_reject_duplicate_both_pairs(self):
        self.reject(duplicate(self.source, 'DTG-000002'), duplicate(self.translation, 'DTG-000002'),
                    reason=r'(?i)duplicate.*pair')

    def test_reject_reordered_source_pairs(self):
        self.reject(source=swap(self.source, 'DTG-000002', 'DTG-000003'), reason=r'(?i)order|identity')

    def test_reject_reordered_translation_pairs(self):
        self.reject(translation=swap(self.translation, 'DTG-000002', 'DTG-000003'), reason=r'(?i)order|identity')

    def test_reject_reordered_both_pairs(self):
        self.reject(swap(self.source, 'DTG-000002', 'DTG-000003'),
                    swap(self.translation, 'DTG-000002', 'DTG-000003'), reason=r'(?i)order|identity')

    def test_reject_unknown_golden_reference(self):
        self.reject(source=self.source_change('U00007', 'golden: U00007', 'golden: U99999'),
                    reason=r'(?i)unknown.*golden|golden.*unknown')

    def test_reject_duplicate_golden_reference(self):
        self.reject(source=self.source_change('U00007', 'golden: U00007 U00008', 'golden: U00007 U00007'),
                    reason=r'(?i)duplicat|covered.*once')

    def test_reject_omitted_golden_reference(self):
        value = self.source_change('U00007', 'golden: U00007 U00008', 'golden: U00007')
        value = replace_block(value, self.owners['U00007'].ident,
                              lambda text: text.replace('roles: main_text main_text', 'roles: main_text', 1))
        self.reject(source=value, reason=r'(?i)omitt|missing|coverage|count')

    def test_reject_reordered_golden_references(self):
        self.reject(source=self.source_change('U00007', 'golden: U00007 U00008', 'golden: U00008 U00007'),
                    reason=r'(?i)order')

    def test_reject_tibetan_whitespace_trimmed(self):
        ident = self.owners['U00004'].ident
        self.reject(source=replace_payload(self.source, ident, str.lstrip), reason=r'(?i)source|Tibetan')

    def test_reject_tibetan_join_newline_changed(self):
        ident = self.owners['U00007'].ident
        self.reject(source=replace_payload(self.source, ident, lambda value: value.replace('\n', '\n\n', 1)),
                    reason=r'(?i)source|Tibetan')

    def test_reject_tibetan_word_mutated(self):
        ident = self.owners['U00004'].ident
        self.reject(source=replace_payload(self.source, ident, lambda value: value.replace('རིན་', 'རིམ་', 1)),
                    reason=r'(?i)source|Tibetan')

    def test_reject_english_word_mutated(self):
        ident = self.owners['U00008'].ident
        self.reject(translation=replace_payload(self.translation, ident,
                    lambda value: value.replace('Jewels', 'Diamonds', 1)), reason=r'(?i)English|translation')

    def test_reject_wrong_source_pin(self):
        self.reject(source=self.source.replace('source-edition: root-tantra-v1.0.0',
                    'source-edition: root-tantra-v2.0.0', 1), reason=r'(?i)front matter|edition|pin')

    def test_reject_wrong_translation_source_pin(self):
        self.reject(translation=self.translation.replace('source-edition: root-tantra-v1.0.0',
                    'source-edition: root-tantra-v2.0.0', 1), reason=r'(?i)front matter|edition|pin')

    def test_reject_wrong_translation_pin(self):
        self.reject(translation=self.translation.replace('translation-edition: translation-golden-aligned-v1.0.0',
                    'translation-edition: translation-golden-aligned-v2.0.0', 1), reason=r'(?i)front matter|edition|pin')

    def test_reject_wrong_paired_edition(self):
        self.reject(source=self.source.replace(core.EDITION, 'dra-thal-gyur-paired-v3.0.0', 1),
                    reason=r'(?i)front matter|edition|pin')

    def test_reject_dropped_restored_object(self):
        ident = self.owners['A2000-C01-S01'].ident
        self.reject(drop(self.source, ident), drop(self.translation, ident))

    def test_reject_dropped_restored_verse_line(self):
        ident = self.owners['A2000-C01-S01'].ident
        value = block(self.source, ident)[3]
        self.assertGreater(len(value.splitlines()), 1)
        self.reject(source=replace_payload(self.source, ident, lambda text: text.split('\n', 1)[1]),
                    reason=r'(?i)source|Tibetan')

    def test_reject_lost_closing_material(self):
        source, translation = self.source, self.translation
        for segment in self.segments:
            if segment.part == 'closing-material':
                source, translation = drop(source, segment.ident), drop(translation, segment.ident)
        self.reject(source, translation)

    def test_reject_closing_as_seventh_chapter(self):
        self.reject(source=self.source.replace('## Full-work colophon and closing material', '## Chapter 7', 1),
                    reason=r'(?i)structure|layout|heading|canonical')

    def test_reject_closing_role_changed(self):
        self.reject(source=self.source_change('U05449', 'roles: work_colophon', 'roles: main_text'),
                    reason=r'(?i)role')

    def test_reject_endnote_definition_lost(self):
        match = re.search(r'^\[\^G-[^\]]+\]: .*?(?=^\[\^G-[^\]]+\]: |\Z)', self.translation, re.M | re.S)
        self.assertIsNotNone(match)
        self.reject(translation=self.translation[:match.start()] + self.translation[match.end():],
                    reason=r'(?i)note|footer')

    def test_reject_endnote_definition_changed(self):
        match = re.search(r'^\[\^G-[^\]]+\]: ', self.translation, re.M)
        self.assertIsNotNone(match)
        self.reject(translation=self.translation[:match.end()] + 'Altered note. ' + self.translation[match.end():],
                    reason=r'(?i)note|footer')

    def test_reject_endnote_reference_lost(self):
        self.reject(translation=replace_payload(self.translation, 'DTG-000001',
                    lambda value: value.replace('[^G-U00001]', '', 1)), reason=r'(?i)note|English|translation')

    def test_reject_endnote_reference_wrong(self):
        self.reject(translation=replace_payload(self.translation, 'DTG-000001',
                    lambda value: value.replace('[^G-U00001]', '[^G-U00002]', 1)),
                    reason=r'(?i)note|English|translation')

    def test_reject_endnote_reference_misplaced(self):
        value = replace_payload(self.translation, 'DTG-000001', lambda text: text.replace('[^G-U00001]', '', 1))
        value = replace_payload(value, 'DTG-000002', lambda text: text + '[^G-U00001]')
        self.reject(translation=value, reason=r'(?i)note|English|translation')

    def test_reject_inline_legacy_note_lost(self):
        self.reject(translation=replace_payload(self.translation, 'DTG-000002',
                    lambda value: value.replace(core.legacy_link('N-001'), '', 1)),
                    reason=r'(?i)note|English|translation')

    def test_reject_noninline_legacy_note_lost(self):
        ident = self.owners['U00008'].ident
        self.assertNotIn('[N-T01]', next(row['english'] for row in self.authorities.english['reading_sequence']
                                      if row['id'] == 'U00008'))
        self.reject(translation=replace_payload(self.translation, ident,
                    lambda value: value.replace(core.legacy_link('N-T01'), '', 1)),
                    reason=r'(?i)note|English|translation')

    def test_reject_empty_annotation_marker_lost(self):
        ident = self.owners['U02615'].ident
        self.reject(translation=replace_payload(self.translation, ident,
                    lambda value: re.sub(r'\[Source annotation at U02615;[^\]]+\]', '', value)),
                    reason=r'(?i)English|translation|marker')

    def test_reject_joined_marker_as_annotation(self):
        ident = self.owners['U01812'].ident
        self.reject(translation=replace_payload(self.translation, ident,
                    lambda value: value.replace('Joined source fragment', 'Source annotation', 1)),
                    reason=r'(?i)English|translation|marker')

    def test_reject_source_heading_hidden(self):
        self.reject(source=self.source_change('U00011', 'roles: source_heading', 'roles: main_text'),
                    reason=r'(?i)role')

    def test_reject_extraneous_source_text(self):
        self.reject(source=self.source + '\nUnassigned source content.\n',
                    reason=r'(?i)structure|layout|outside|canonical')

    def test_reject_extraneous_translation_text(self):
        self.reject(translation=self.translation + '\nUnassigned translation content.\n',
                    reason=r'(?i)structure|layout|outside|note|footer|canonical')

    def test_reject_resegmentation_with_all_source_intact(self):
        # Shift U00008 into the next pair; preserve every golden object and word.
        rows = {row['id']: row for row in self.authorities.english['reading_sequence']}
        before, after = self.owners['U00007'].ident, self.owners['U00009'].ident
        source, translation = self.source, self.translation
        for ident, membership in [(before, ['U00007']), (after, ['U00008', 'U00009', 'U00010'])]:
            selected = [rows[golden] for golden in membership]
            source = replace_block(source, ident, lambda _, selected=selected, ident=ident:
                                   source_comment(ident, selected, self.owners[selected[0]['id']].format) + '\n' +
                                   core.source_payload(selected) + '\n<!-- /pair -->')
            translation = replace_payload(translation, ident, lambda _, selected=selected:
                                          core.english_payload(selected))
        self.assertEqual([golden for segment in core.parse(source, 'bo') for golden in segment.golden],
                         [golden for segment in self.segments for golden in segment.golden])
        self.reject(source, translation, reason=r'(?i)identity|membership|segment|stable')

    def test_positive_accepted_final_signoff(self):
        binding = {'edition': core.EDITION, 'input_sha256': {'fixture.txt': core.sha(b'fixture')}}
        record = {'status': 'accepted', 'binding': binding, 'blocking_findings': 0,
                  'fresh_semantic_qc': False}
        with patch.object(validate, 'signoff_binding', return_value=binding):
            self.assertIsNone(validate.validate_signoff({}, record))

    def test_reject_alternate_repository_root(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(ValueError, 'Alternate repository root is unsupported') as caught:
                validate.validate_repo(Path(temporary))
            REJECTIONS[self._testMethodName] = str(caught.exception)

    def test_reject_missing_final_signoff_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'paired').mkdir()
            (root / 'paired/source.md').write_text(self.source, encoding='utf-8')
            (root / 'paired/translation.md').write_text(self.translation, encoding='utf-8')
            # Isolate the filesystem gate from Git and linked-evidence setup;
            # real pair/content validation still runs against the pinned corpus.
            with patch.multiple(validate, ROOT=root, check_tags=Mock(), check_protected=Mock(),
                                check_links=Mock(return_value=0),
                                load_authorities=Mock(return_value=self.authorities)):
                with self.assertRaisesRegex(ValueError, 'requires saved signoff') as caught:
                    validate.validate_repo(root=root, require_final=True)
            REJECTIONS[self._testMethodName] = str(caught.exception)

    def test_reject_unaccepted_final_signoff(self):
        with self.assertRaisesRegex(ValueError, 'requires accepted signoff') as caught:
            validate.validate_signoff({}, {'status': 'pending'})
        REJECTIONS[self._testMethodName] = str(caught.exception)

    def test_reject_stale_final_signoff(self):
        report = {'counts': {'total_pairs': 2667}, 'pins': core.PINS,
                  'identity_sha256': 'fixture-identity', 'format_sha256': 'fixture-format'}
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'fixture.txt').write_bytes(b'reviewed content')
            with patch.object(validate, 'SIGNOFF_FILES', ['fixture.txt']):
                record = {'status': 'accepted', 'binding': validate.signoff_binding(report, root),
                          'blocking_findings': 0, 'fresh_semantic_qc': False}
                validate.validate_signoff(report, record, root)
                (root / 'fixture.txt').write_bytes(b'changed after review')
                with self.assertRaisesRegex(ValueError, 'signoff is stale') as caught:
                    validate.validate_signoff(report, record, root)
            REJECTIONS[self._testMethodName] = str(caught.exception)

    def test_reject_blocking_final_review(self):
        binding = {'edition': core.EDITION}
        record = {'status': 'accepted', 'binding': binding, 'blocking_findings': 1,
                  'fresh_semantic_qc': False}
        with patch.object(validate, 'signoff_binding', return_value=binding):
            with self.assertRaisesRegex(ValueError, 'Blocking final-review findings') as caught:
                validate.validate_signoff({}, record)
        REJECTIONS[self._testMethodName] = str(caught.exception)

    def test_reject_semantic_qc_claim_in_signoff(self):
        binding = {'edition': core.EDITION}
        record = {'status': 'accepted', 'binding': binding, 'blocking_findings': 0,
                  'fresh_semantic_qc': True}
        with patch.object(validate, 'signoff_binding', return_value=binding):
            with self.assertRaisesRegex(ValueError, 'Unsupported semantic QC claim') as caught:
                validate.validate_signoff({}, record)
        REJECTIONS[self._testMethodName] = str(caught.exception)

    def test_reject_changed_protected_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'protected.txt').write_bytes(b'changed')
            authorities = dataclasses.replace(self.authorities, protected={'protected.txt': core.sha(b'original')})
            with self.assertRaisesRegex(ValueError, 'Protected input changed or missing') as caught:
                core.check_protected(authorities, root=root)
            REJECTIONS[self._testMethodName] = str(caught.exception)

    def test_reject_missing_protected_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            authorities = dataclasses.replace(self.authorities, protected={'protected.txt': core.sha(b'original')})
            with self.assertRaisesRegex(ValueError, 'Protected input changed or missing') as caught:
                core.check_protected(authorities, root=Path(temporary))
            REJECTIONS[self._testMethodName] = str(caught.exception)


def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(PairedTests)
    names = [test._testMethodName for test in suite]
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    failed = {}
    for test, detail in result.failures + result.errors:
        parent = getattr(test, 'test_case', test)
        if hasattr(parent, '_testMethodName'):
            failed[parent._testMethodName] = detail
    report = {
        'schema': 'paired-negative-tests/2',
        'paired_edition': core.EDITION,
        'status': 'pass' if result.wasSuccessful() else 'fail',
        'tests_run': result.testsRun,
        'positive_tests': sum(name.startswith('test_positive_') for name in names),
        'negative_tests': sum(name.startswith('test_reject_') for name in names),
        'failures': len(result.failures),
        'errors': len(result.errors),
        'checks': [{'name': name.removeprefix('test_'),
                    'status': 'not-run' if result.testsRun == 0 else 'fail' if name in failed else 'pass',
                    **({'rejection': REJECTIONS[name]} if name in REJECTIONS else {}),
                    **({'detail': failed[name]} if name in failed else {})} for name in names],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not result.wasSuccessful():
        print(stream.getvalue(), file=sys.stderr)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
