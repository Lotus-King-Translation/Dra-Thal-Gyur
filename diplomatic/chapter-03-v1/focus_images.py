"""Lossless bounded views of already preserved images; no OCR or new testimony."""
from pathlib import Path
import json, hashlib
from PIL import Image
root=Path(__file__).resolve().parent
plan=json.loads((root/'evidence/focus-plan.json').read_text())
folder=root/'evidence/focused'; folder.mkdir(exist_ok=True)
records=[]
for item in plan:
    source=root/'evidence'/item['source']; im=Image.open(source); im.load()
    bounds=item['bounds']; assert 0<=bounds[0]<bounds[2]<=im.width and 0<=bounds[1]<bounds[3]<=im.height
    crop=im.crop(bounds); target=folder/(item['label']+'.png')
    if target.exists(): assert Image.open(target).tobytes()==crop.tobytes()
    else: crop.save(target)
    records.append({**item,'path':str(target.relative_to(root)),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
        'derivation':'Exact unscaled native pixel crop; same source, not independent evidence'})
(folder/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Verified focused views:',len(records))
