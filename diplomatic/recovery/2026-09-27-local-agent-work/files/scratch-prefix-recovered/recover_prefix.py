from pathlib import Path, PurePosixPath
import hashlib, io, json, tarfile, zlib
BASE=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur/diplomatic/recovery/2026-09-27-preservation')
OUT=Path(__file__).parent
archive=json.loads((BASE/'archive.json').read_text())
expected={r['path']:r for r in json.loads((BASE/'scratch-manifest.json').read_text())['files']}
parts=[]; compressed=[]
for r in archive['parts']:
 p=BASE/r['path']
 if not p.exists():break
 b=p.read_bytes();h=hashlib.sha256(b).hexdigest()
 assert len(b)==r['bytes'] and h==r['sha256'],r['path']
 compressed.append(b);parts.append(r)
z=zlib.decompressobj(16+zlib.MAX_WBITS)
raw=z.decompress(b''.join(compressed))
recovered=[];skipped=[];stop=None
with tarfile.open(fileobj=io.BytesIO(raw),mode='r:') as tf:
 while True:
  try:t=tf.next()
  except (tarfile.ReadError,EOFError) as e:stop={'reason':str(e),'tar_offset':tf.offset};break
  if t is None:break
  if not t.isfile():
   skipped.append({'path':t.name,'reason':'not regular file','type':str(t.type)});continue
  name=str(PurePosixPath(t.name))
  if name.startswith('/') or '..' in PurePosixPath(name).parts:
   skipped.append({'path':name,'reason':'unsafe path'});continue
  if name not in expected:
   skipped.append({'path':name,'reason':'not in expected scratch manifest'});continue
  e=expected[name]
  if t.offset_data+t.size>len(raw):
   stop={'path':name,'reason':'incomplete member payload','expected_bytes':t.size,'available_bytes':max(0,len(raw)-t.offset_data)};break
  b=raw[t.offset_data:t.offset_data+t.size];h=hashlib.sha256(b).hexdigest()
  if len(b)!=e['bytes'] or h!=e['sha256']:
   skipped.append({'path':name,'reason':'size or SHA256 mismatch','actual_bytes':len(b),'actual_sha256':h,'expected':e});continue
  dest=OUT/'files'/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
  recovered.append({'path':name,'bytes':len(b),'sha256':h,'verification':'exact size and SHA256 match published scratch-manifest.json'})
report={'status':'verified complete members from incomplete archive only','source_manifest':'diplomatic/recovery/2026-09-27-preservation/scratch-manifest.json','source_archive':'diplomatic/recovery/2026-09-27-preservation/archive.json','source_parts_verified':parts,'compressed_prefix_bytes':sum(len(x) for x in compressed),'decompressed_prefix_bytes':len(raw),'gzip_end_marker_present':z.eof,'recovered_files':recovered,'skipped_members':skipped,'stopped_at':stop,'not_recovered':[r for name,r in expected.items() if name not in {x['path'] for x in recovered}],'provenance_limit':'Scratch manifest identifies these as later reconstruction files, not recovered earlier originals. Complete archive integrity cannot be checked without remaining parts. No embedded script was executed.'}
(OUT/'manifest.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'README.md').write_text('# Verified members recovered from partial scratch archive\n\n'+f"Recovered {len(recovered)} complete regular files ({sum(x['bytes'] for x in recovered):,} bytes), each independently matched to the published scratch manifest by exact size and SHA-256.\n\nOnly parts 000–009 are available; gzip end marker and complete archive verification remain unavailable. No incomplete member was saved. See manifest.json for stop point and unrecovered files.\n\nThese are later reconstruction scratch files, not the missing earlier diplomatic originals. Embedded scripts were not executed. Original parts were not modified.\n")
print(json.dumps({'files':len(recovered),'bytes':sum(x['bytes'] for x in recovered),'stop':stop,'nonimages':[x['path'] for x in recovered if Path(x['path']).suffix not in ['.png','.jpg','.jpeg']],'skipped':skipped},indent=2))
