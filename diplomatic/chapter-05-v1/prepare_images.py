#!/usr/bin/env python3
"""Preserve verified native Adzom images and lossless viewing crops, not OCR."""
from pathlib import Path
import argparse, hashlib, io, json, zipfile
from PIL import Image

def sha(p):
    with p.open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()
def prepare(root,pages,label):
    assert 1<=len(pages)<=5 and len(set(pages))==len(pages)
    src=root/'editions/adzom-2000'; out=root/'diplomatic/chapter-05-v1/evidence'/label
    m=json.loads((src/'image-manifest.json').read_text())
    assert sha(src/'original-images.zip')==m['zip_sha256']
    out.mkdir(parents=True,exist_ok=False); images={i['pdf_page']:i for i in m['images']}
    record={'source_manifest_sha256':sha(src/'image-manifest.json'),'zip_sha256':m['zip_sha256'],
        'status':'prepared_not_read','coordinate_convention':'Native half-open x0,y0,x1,y1','pages':[],'views':[]}
    def save(): (out/'manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    save()
    with zipfile.ZipFile(src/'original-images.zip') as z:
        for page in pages:
            e=images[page]; payload=z.read(e['file'])
            assert hashlib.sha256(payload).hexdigest()==e['sha256']
            im=Image.open(io.BytesIO(payload)); im.load(); assert im.size==(e['width'],e['height'])
            path=out/f'p{page:03d}-native.png'; path.write_bytes(payload)
            record['pages'].append({'pdf_page':page,'bdrc_image':e['image'],'member':e['file'],
                'sha256':e['sha256'],'dimensions':list(im.size),'path':str(path.relative_to(root))}); save()
            width=min(2000,im.width); xs=sorted({0,max(0,(im.width-width)//2),im.width-width})
            for x in xs:
                bounds=[x,0,x+width,im.height]; tile=im.crop(bounds)
                target=out/f'p{page:03d}-x{x:04d}.png'; tile.save(target)
                assert Image.open(target).tobytes()==tile.tobytes()
                record['views'].append({'pdf_page':page,'path':str(target.relative_to(root)),
                    'bounds':bounds,'sha256':sha(target),'derivation':'Unscaled lossless native crop; not another witness'})
            save()
    print(json.dumps({'manifest':str((out/'manifest.json').relative_to(root)),'pages':pages,'images':len(record['pages'])+len(record['views'])}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--pages',nargs='+',type=int,required=True); p.add_argument('--label',required=True)
    a=p.parse_args(); assert a.label.isalnum(); prepare(a.repo.resolve(),a.pages,a.label)
