"""Offline safety/preservation tests; no reader or network is invoked."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.dont_write_bytecode = True
import reading_batch as batch


class ReadingBatchTests(unittest.TestCase):
    def test_paths_cannot_escape_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            with self.assertRaises(ValueError):
                batch.inside(root, '../outside')

    def test_capture_is_preserved_and_never_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            reports = root / 'diplomatic/reviews/test'
            reports.mkdir(parents=True)
            request = reports / 'request.txt'
            request.write_text('Offline fixture: inspect supplied images only.')
            image = root / 'fixture.png'
            image.write_bytes(b'not-a-real-image; mocked reader fixture')
            spec = {'source_pages': [1], 'request_path': str(request.relative_to(root)),
                    'output_stem': 'diplomatic/reviews/test/attempt',
                    'images': [{'path': 'fixture.png', 'sha256': batch.digest(image)}]}
            specification = root / 'spec.json'
            batch.dump(specification, spec)
            def fake_reader(args, **kwargs):
                self.assertEqual(args[args.index('--sandbox') + 1], 'read-only')
                Path(args[args.index('-o') + 1]).write_text('{"fixture":true}\n')
                kwargs['stdout'].write('{"item":{"type":"agent_message"}}\n')
                return subprocess.CompletedProcess(args, 0)
            with patch.object(batch.subprocess, 'run', side_effect=fake_reader):
                batch.capture(root, 'spec.json')
            receipt = json.loads((reports / 'attempt-execution.json').read_text())
            self.assertFalse(receipt['editorial_decisions_made_by_wrapper'])
            self.assertEqual(receipt['unexpected_tool_items'], [])
            self.assertEqual(receipt['status'], 'captured_requires_coordinator_review')
            with self.assertRaises(FileExistsError):
                batch.capture(root, 'spec.json')
            spec['output_stem'] += '-bad-hash'
            spec['images'][0]['sha256'] = '0' * 64
            batch.dump(specification, spec)
            with self.assertRaises(ValueError):
                batch.capture(root, 'spec.json')
            spec['source_pages'] = list(range(6))
            batch.dump(specification, spec)
            with self.assertRaises(ValueError):
                batch.capture(root, 'spec.json')

    def test_native_preparation_is_lossless_and_not_inspection(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest('Optional native-evidence test requires Pillow.')
        import io
        import zipfile
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            source = root / 'editions/fixture'
            source.mkdir(parents=True)
            buffer = io.BytesIO()
            Image.new('RGB', (4, 3), (20, 30, 40)).save(buffer, format='PNG')
            payload = buffer.getvalue()
            pdf = source / 'sgra-thal-gyur.pdf'
            pdf.write_bytes(b'%PDF-1.7 synthetic hash fixture, not a manuscript')
            archive = source / 'original-images.zip'
            with zipfile.ZipFile(archive, 'w') as output:
                output.writestr('0003.png', payload)
            manifest = {'pdf_sha256': batch.digest(pdf), 'zip_sha256': batch.digest(archive),
                'images': [{'pdf_page': 1, 'image': 3, 'file': '0003.png',
                            'sha256': hashlib.sha256(payload).hexdigest(),
                            'width': 4, 'height': 3}]}
            batch.dump(source / 'image-manifest.json', manifest)
            destination = 'diplomatic/evidence/test/batch'
            batch.prepare(root, 'fixture', [1], destination)
            result = json.loads((root / destination / 'manifest.json').read_text())
            self.assertEqual(result['status'], 'prepared_not_visually_inspected')
            self.assertEqual((root / result['pages'][0]['path']).read_bytes(), payload)
            self.assertEqual(len(result['tiles']), 1)
            with Image.open(root / result['tiles'][0]['path']) as tile:
                self.assertEqual(tile.tobytes(), Image.open(io.BytesIO(payload)).tobytes())
            with self.assertRaises(FileExistsError):
                batch.prepare(root, 'fixture', [1], destination)
            with self.assertRaises(ValueError):
                batch.prepare(root, 'fixture', [1, 1], destination + '-duplicate')


if __name__ == '__main__':
    unittest.main()
