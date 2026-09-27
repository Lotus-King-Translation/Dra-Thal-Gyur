from pathlib import Path
import json, re, time, hashlib, urllib.request, urllib.error, concurrent.futures, zipfile
from PIL import Image
from io import BytesIO
import img2pdf, pikepdf
R=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur'); E=R/'editions'; D=Path(__file__).parent
CACHE=D/'images'; CACHE.mkdir(exist_ok=True)
def sha(b): return hashlib.sha256(b).hexdigest()
def get(url):
 for attempt in range(3):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'DraThalGyur-research/1.0'}),timeout=60) as response: return response.read()
  except urllib.error.HTTPError as err:
   if err.code in (401,403,404): raise
   if attempt==2: raise
  except (TimeoutError,OSError):
   if attempt==2: raise
  time.sleep(2+attempt*2)
def canvases(ed,group):
 folder=E/ed/'metadata'; folder.mkdir(parents=True,exist_ok=True)
 p=folder/'volume-manifest.json'; url=f'https://iiifpres.bdrc.io/vo:bdr:{group}/manifest'
 if p.exists(): data=json.loads(p.read_text())
 else: b=get(url); p.write_bytes(b); data=json.loads(b)
 cs=data.get('sequences',[{}])[0].get('canvases',data.get('items',[])); result={}
 for c in cs:
  label=str(c.get('label')); match=re.search(r'img\. (\d+)',label)
  if match and c.get('images'): result[int(match[1])]=c
 return result
def image(job):
 ed,n,c=job; resource=c['images'][0]['resource']; url=resource['@id']
 if '.tif/' in url.lower(): url=url.rsplit('/',1)[0]+'/default.png'
 folder=CACHE/ed; folder.mkdir(exist_ok=True)
 ext='.png' if url.endswith('.png') else '.jpg'; p=folder/f'{n:04d}{ext}'
 if p.exists(): b=p.read_bytes()
 else: b=get(url); p.write_bytes(b)
 with Image.open(BytesIO(b)) as im:
  im.load(); dims=im.size; fmt=im.format
  if dims!=(resource['width'],resource['height']): raise RuntimeError(f'Unexpected dimensions {ed}:{n}: {dims}')
 return {'image':n,'file':p.name,'url':url,'canvas':c['@id'],'bytes':len(b),'sha256':sha(b),'width':dims[0],'height':dims[1],'format':fmt}
SPECS=[('adzom-2000','I1KG11710',3,207),('dege-W1ER7','I1ER175',647,757),('tsamdrak-1982','I0615',3,175),('tharpaling-1983','I4448',5,151),('tingkye-1973','I1765',394,538),('dzongsar-manuscript','I3PD1345',4,252),('langtang-manuscript','I1ER800',2,213),('seventeen-tantras-W1ER119','I1ER794',2,201),('khams-zhichen-manuscript','I1KG81308',31,231),('gadkar-manuscript','I1ER907',441,617)]
def sample():
 jobs=[]
 for ed,group,a,b in SPECS:
  cs=canvases(ed,group)
  for n in sorted(set([a,a+1,b,b+1])):
   if n in cs: jobs.append((ed,n,cs[n]))
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for job,record in zip(jobs,pool.map(image,jobs)):
   print('SAMPLE',job[0],record['image'],record['width'],record['height'],flush=True)
if __name__=='__main__':
 import sys
 if '--sample' in sys.argv: sample()
def acquire(ed,group,a,b):
 cs=canvases(ed,group); chosen=[n for n in sorted(cs) if a<=n<=b]
 if not chosen or chosen[0]!=a or chosen[-1]!=b: raise RuntimeError('Boundary canvases absent: '+ed)
 jobs=[(ed,n,cs[n]) for n in chosen]; records=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for record in pool.map(image,jobs):
   record['pdf_page']=len(records)+1;records.append(record)
   if len(records)%50==0: print(ed,len(records),'/',len(jobs),flush=True)
 folder=E/ed; zp=folder/'original-images.zip'; pdf=folder/'sgra-thal-gyur.pdf'
 with zipfile.ZipFile(zp,'w',compression=zipfile.ZIP_STORED) as z:
  for record in records: z.write(CACHE/ed/record['file'],record['file'])
  assert z.testzip() is None
 with pdf.open('wb') as f: f.write(img2pdf.convert([str(CACHE/ed/r['file']) for r in records]))
 with pikepdf.open(pdf) as doc:
  assert len(doc.pages)==len(records)
  for page,record in zip(doc.pages,records):
   imgs=page.get_images(); assert len(imgs)==1
   obj=next(iter(imgs.values())); assert (int(obj.Width),int(obj.Height))==(record['width'],record['height'])
  for i in sorted(set([0,1,len(records)//2,len(records)-1])):
   rendered=pikepdf.PdfImage(next(iter(doc.pages[i].get_images().values()))).as_pil_image().convert('RGB')
   with Image.open(CACHE/ed/records[i]['file']) as original: assert original.convert('RGB').tobytes()==rendered.tobytes()
 report={'edition':ed,'manifest_url':f'https://iiifpres.bdrc.io/vo:bdr:{group}/manifest','bdrc_image_start':a,'bdrc_image_end':b,'pages':len(records),'skipped_indices_not_in_manifest':[n for n in range(a,b+1) if n not in cs],'images':records,'pdf_sha256':sha(pdf.read_bytes()),'zip_sha256':sha(zp.read_bytes()),'dimensions_preserved_every_page':True,'pixel_identity_checked_pdf_pages':[i+1 for i in sorted(set([0,1,len(records)//2,len(records)-1]))],'new_ocr':False}
 (folder/'image-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print('DONE',ed,len(records),pdf.stat().st_size,flush=True)
if __name__=='__main__' and '--all' in sys.argv:
 for ed,g,a,b in SPECS:
  if ed=='langtang-manuscript':b=221
  if ed=='tsamdrak-1982':a=4
  if ed=='dzongsar-manuscript':a=5
  try: acquire(ed,g,a,b)
  except Exception as err: print('FAILED',ed,type(err).__name__,str(err),flush=True)
