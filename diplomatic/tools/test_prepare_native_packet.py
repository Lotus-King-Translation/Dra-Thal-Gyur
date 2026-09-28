"""Synthetic tests only: no research source is changed or removed."""
import hashlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from PIL import Image, ImageDraw
import prepare_native_packet as packet


class PacketTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='native-packet-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = self.root / 'editions/fixture'
        source.mkdir(parents=True)
        images = []
        archive = source / 'original-images.zip'
        with zipfile.ZipFile(archive, 'w') as output:
            for number, size in [(1, (2100, 1500)), (2, (4100, 100))]:
                image = Image.new('RGB', size, (250, 245, 230))
                ImageDraw.Draw(image).line((0, 0, size[0]-1, size[1]-1), fill=0, width=7)
                data = io.BytesIO(); image.save(data, format='PNG')
                payload = data.getvalue(); name = f'{number:04d}.png'
                output.writestr(name, payload)
                images.append({'pdf_page': number, 'image': number+2, 'file': name,
                               'sha256': hashlib.sha256(payload).hexdigest(),
                               'width': size[0], 'height': size[1]})
        pdf = source / 'sgra-thal-gyur.pdf'
        pdf.write_bytes(b'%PDF-1.7\nsynthetic fixture, not a source scan\n')
        metadata = {'images': images, 'zip_sha256': packet.sha256(archive),
                    'pdf_sha256': packet.sha256(pdf)}
        (source / 'image-manifest.json').write_text(json.dumps(metadata))
        data = self.root / 'diplomatic/collation/chapter-01'
        data.mkdir(parents=True)
        units = [{'id': f'U{n:05d}', 'source_tibetan': 'ཀ།',
                  'reading_tibetan': 'ཀ།', 'status': 'synthetic'} for n in (1, 2)]
        self.committed = {}
        for name, value in [('reading-units.json', units),
                            ('ch1-scan-insertions.json', []),
                            ('additional-interventions.json', [])]:
            path = data / name
            path.write_text(json.dumps(value, ensure_ascii=False))
            self.committed[str(path.relative_to(self.root))] = path.read_bytes()
        self.script = self.root / 'diplomatic/tools/prepare_native_packet.py'
        self.script.parent.mkdir(parents=True)
        self.script.write_bytes(Path(packet.__file__).read_bytes())

    def fake_git(self, args, cwd=None, text=False):
        if args[1:] == ['rev-parse', 'HEAD']:
            return 'a' * 40 + '\n'
        if args[1] == 'show':
            return self.committed[args[2].split(':', 1)[1]]
        raise AssertionError(f'Unexpected external command: {args}')

    def run_packet(self, pages=None, **overrides):
        options = dict(repo=self.root, edition='fixture', task='C1-TEST',
                       batch='B01', pages=pages or [1, 2], start_unit=1, end_unit=2)
        options.update(overrides)
        with patch.object(packet, '__file__', str(self.script)), \
             patch.object(packet.subprocess, 'check_output', self.fake_git):
            return packet.prepare(**options)

    def test_complete_pixel_accounting(self):
        path = self.run_packet()
        record = json.loads(path.read_text())
        self.assertEqual(record['status'], 'ready_for_visual_review_not_collated')
        self.assertEqual(len(record['pages']), 2)
        self.assertEqual(len(record['views']), 7)
        natives = {p['pdf_page']: Image.open(self.root / p['path']) for p in record['pages']}
        for view in record['views']:
            output = self.root / view['path']
            expected = natives[view['pdf_page']].crop(view['native_bounds'])
            self.assertEqual(packet.sha256(output), view['sha256'])
            self.assertEqual(Image.open(output).tobytes(), expected.tobytes())
        reference = json.loads((self.root / record['base_reference']['path']).read_text())
        self.assertEqual(len(reference['base_units']), 2)
        self.assertIn('never evidence', reference['warning'])

    def test_existing_packet_is_not_overwritten(self):
        path = self.run_packet()
        original = path.read_bytes()
        with self.assertRaises(FileExistsError):
            self.run_packet()
        self.assertEqual(path.read_bytes(), original)

    def test_source_hash_mismatch_stops_before_packet(self):
        path = self.root / 'editions/fixture/original-images.zip'
        with path.open('ab') as output:
            output.write(b'changed')
        with self.assertRaisesRegex(ValueError, 'Source hash mismatch'):
            self.run_packet()
        self.assertFalse((self.root / 'diplomatic/evidence').exists())

    def test_unpublished_reference_stops_before_packet(self):
        path = self.root / 'diplomatic/collation/chapter-01/reading-units.json'
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'Publish canonical inputs'):
            self.run_packet()
        self.assertFalse((self.root / 'diplomatic/evidence').exists())

    def test_bounded_inputs(self):
        for options in ({'pages': [1, 2, 3, 4, 5, 6]}, {'pages': [2, 1]},
                        {'task': '../ESCAPE'}, {'edition': '../escape'},
                        {'start_unit': 0}, {'end_unit': 2636}, {'pages': [3]}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                self.run_packet(**options)

    def test_tile_geometry_covers_every_pixel(self):
        for size in [1, 100, 1400, 1500, 2000, 2100, 4100, 5696, 10001]:
            for limit in [1400, 2000]:
                starts = packet.tile_origins(size, limit)
                self.assertEqual(starts, sorted(set(starts)))
                self.assertEqual(starts[0], 0)
                self.assertGreaterEqual(starts[-1] + limit, size)
                self.assertTrue(all(b <= a + limit for a, b in zip(starts, starts[1:])))
        with self.assertRaises(ValueError):
            packet.tile_origins(100, 100)


if __name__ == '__main__':
    unittest.main()
