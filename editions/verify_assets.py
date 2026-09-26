#!/usr/bin/env python3
"""Verify archived bytes, PDF structure, active-source copies, and guidance."""
from pathlib import Path
import hashlib, json, zipfile, datetime
import pikepdf
ROOT = Path(__file__).resolve().parent.parent
E = ROOT/'editions'
def digest(path):
    with path.open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()
def main():
    inventory = json.loads((E/'ACQUISITION.json').read_text())
    for record in inventory['files']:
        p = ROOT/record['path']
        assert p.stat().st_size == record['bytes'], str(p)
        assert digest(p) == record['sha256'], str(p)
    packet_count = image_count = 0
    for manifest_path in sorted(E.glob('*/image-manifest.json')):
        d = json.loads(manifest_path.read_text()); folder = manifest_path.parent
        assert digest(folder/'sgra-thal-gyur.pdf') == d['pdf_sha256']
        assert digest(folder/'original-images.zip') == d['zip_sha256']
        with zipfile.ZipFile(folder/'original-images.zip') as z:
            assert len(z.namelist()) == len(d['images'])
            for image in d['images']:
                assert hashlib.sha256(z.read(image['file'])).hexdigest() == image['sha256']
        with pikepdf.open(folder/'sgra-thal-gyur.pdf') as pdf:
            assert len(pdf.pages) == d['pages']
            for page, image in zip(pdf.pages,d['images']):
                objects = page.get_images(); assert len(objects) == 1
                obj = next(iter(objects.values()))
                assert (int(obj.Width),int(obj.Height)) == (image['width'],image['height'])
        packet_count += 1; image_count += d['pages']
    guidance = json.loads((ROOT/'GUIDANCE-PROVENANCE.json').read_text())
    for item in guidance['files']: assert digest(ROOT/item['path']) == item['sha256']
    source = json.loads((ROOT/'source'/'SOURCE.json').read_text())
    for item in source['files']: assert digest(ROOT/'source'/item['name']) == item['sha256']
    for archive, active in [('sgra-thal-gyur.pdf','Dra-Thal-Gyur-Adzom-2000.pdf'),('W1KG11703_7.docx','W1KG11703_7.docx'),('W1KG11703_7.txt','W1KG11703_7.txt')]:
        assert digest(E/'adzom-2000'/archive) == digest(ROOT/'source'/active)
    base = json.loads((E/'adzom-2000'/'image-manifest.json').read_text())
    assert [x['image'] for x in base['images']] == list(range(3,208))
    report = {'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'asset_files_verified':len(inventory['files']), 'image_packets_verified':packet_count,
              'archived_image_hashes_verified':image_count, 'all_pdf_image_dimensions_verified':True,
              'unchanged_guidance_files':len(guidance['files']), 'active_source_matches_archive':True,
              'active_source_missing_image_indices':[], 'new_ocr':False,
              'text_proofread':False, 'complete_foliation_audit':False}
    (E/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2)); print('PASS')
if __name__ == '__main__': main()
