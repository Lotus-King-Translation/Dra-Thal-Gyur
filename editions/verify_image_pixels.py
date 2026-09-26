#!/usr/bin/env python3
"""Check every assembled PDF page against its preserved IIIF response image."""
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO
import hashlib,json,datetime,sys
import pikepdf
from PIL import Image
ROOT=Path(__file__).resolve().parent.parent
results=[]
for path in sorted((ROOT/'editions').glob('*/image-manifest.json')):
    m=json.loads(path.read_text()); folder=path.parent
    errors=[]
    with ZipFile(folder/'original-images.zip') as z, pikepdf.open(folder/'sgra-thal-gyur.pdf') as pdf:
        assert len(pdf.pages)==len(m['images'])==len(z.namelist())==m['pages']
        for row in m['images']:
            raw=z.read(row['file'])
            assert hashlib.sha256(raw).hexdigest()==row['sha256']
            im=Image.open(BytesIO(raw)).convert('RGB')
            images=list(pdf.pages[row['pdf_page']-1].get_images().values())
            assert len(images)==1
            actual=pikepdf.PdfImage(images[0]).as_pil_image().convert('RGB')
            if actual.size!=im.size or actual.tobytes()!=im.tobytes(): errors.append(row['file'])
    results.append({'edition':folder.name,'pages_checked':m['pages'],'pixel_mismatches':errors})
    print(folder.name,m['pages'],'pages:', 'PASS' if not errors else errors,flush=True)
report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'results':results,
        'scope':'All archived image hashes and decoded RGB pixels of each corresponding PDF image. Not textual proofreading or a foliation audit.'}
if '--write-report' in sys.argv:
    (ROOT/'editions/PIXEL-VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
sys.exit(1 if any(x['pixel_mismatches'] for x in results) else 0)
