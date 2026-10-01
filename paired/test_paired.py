#!/usr/bin/env python3
"""Deterministic stdlib acceptance/corruption checks; never mutate the corpus."""
from __future__ import annotations

import dataclasses
import io
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

import core
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
        self.assertEqual(len(source_ids), 2660)
        golden = [golden for segment in self.segments for golden in segment.golden]
        self.assertEqual(golden, [row['id'] for row in self.authorities.golden['reading_sequence']])
        self.assertEqual(len(golden), 5484)
        self.assertEqual(len(set(golden)), 5484)

    def test_positive_grouping_examples(self):
        # Independent, reviewed examples, not expectations rerendered by grouping().
        expected = [
            ['U00315', 'U00316', 'U00317', 'U00318'],
            ['U01191', 'U01192'],
            ['U01193', 'U01194', 'U01195', 'U01196'],
            ['U01880', 'U01881', 'U01882', 'A2000-C01-S02', 'U01883', 'U01884'],
            ['U02488', 'U02489', 'SCAN-CH1-LAYER-02489', 'U02490', 'U02491', 'U02492'],
            ['U02613', 'U02614', 'U02615', 'U02616'],
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
        self.assertEqual(self.owners['U02488'].roles[2], 'source_heading')
        self.assertEqual(self.owners['U01880'].roles[3], 'restored_main_text')

    def test_positive_false_terminal_notices(self):
        for ident in ['U01449', 'U01899', 'U02700', 'U02722', 'U03440']:
            row = next(row for row in self.authorities.english['reading_sequence'] if row['id'] == ident)
            with self.subTest(golden=ident):
                self.assertFalse(core.ends_sentence(row['english']))
        row = next(row for row in self.authorities.english['reading_sequence'] if row['id'] == 'U02743')
        self.assertTrue(core.ends_sentence(row['english']))

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
        self.reject(source=self.source.replace(core.EDITION, 'dra-thal-gyur-paired-v2.0.0', 1),
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
                                   core.pair_comment(ident, selected, 'bo') + '\n' +
                                   core.source_payload(selected) + '\n<!-- /pair -->')
            translation = replace_payload(translation, ident, lambda _, selected=selected:
                                          core.english_payload(selected))
        self.assertEqual([golden for segment in core.parse(source, 'bo') for golden in segment.golden],
                         [golden for segment in self.segments for golden in segment.golden])
        self.reject(source, translation, reason=r'(?i)identity|membership|segment|stable')

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
    failed = {test._testMethodName: detail for test, detail in result.failures + result.errors
              if hasattr(test, '_testMethodName')}
    report = {
        'schema': 'paired-negative-tests/1',
        'status': 'pass' if result.wasSuccessful() else 'fail',
        'tests_run': result.testsRun,
        'positive_tests': sum(name.startswith('test_positive_') for name in names),
        'negative_tests': sum(name.startswith('test_reject_') for name in names),
        'failures': len(result.failures),
        'errors': len(result.errors),
        'checks': [{'name': name.removeprefix('test_'),
                    'status': 'fail' if name in failed else 'pass',
                    **({'rejection': REJECTIONS[name]} if name in REJECTIONS else {}),
                    **({'detail': failed[name]} if name in failed else {})} for name in names],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not result.wasSuccessful():
        print(stream.getvalue(), file=sys.stderr)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
