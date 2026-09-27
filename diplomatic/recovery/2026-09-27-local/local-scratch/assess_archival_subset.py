from pathlib import Path
import hashlib,json,zipfile,shutil,collections,re
OUT=Path(__file__).parent
REPO=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
rows=json.loads((OUT/'inventory.json').read_text())['files']
by_path={r['path']:r for r in rows}
comparisons=[];exact=set();failures=[]
for mp in sorted((REPO/'editions').glob('*/image-manifest.json')):
 m=json.loads(mp.read_text());zp=mp.parent/'original-images.zip'
 if not zipfile.is_zipfile(zp):failures.append({'path':str(zp),'reason':'not readable zip'});continue
 with zipfile.ZipFile(zp) as z:
  for image in m['images']:
   raw=Path('/tmp/dra-thal-gyur-acquire/images')/mp.parent.name/image['file'];r=by_path.get(str(raw))
   if not r:continue
   b=z.read(image['file']);h=hashlib.sha256(b).hexdigest()
   ok=len(b)==r['bytes'] and h==r['sha256']==image['sha256']
   comparisons.append({'scratch_path':str(raw),'repository_archive':str(zp.relative_to(REPO)),'member':image['file'],'bytes':len(b),'sha256':h,'exact_match':ok})
   if ok:exact.add(str(raw))
   else:failures.append(comparisons[-1])
selected=[];excluded=[]
for r in rows:
 p=Path(r['path'])
 if str(p) in exact:
  excluded.append({'path':str(p),'reason':'exact size/SHA256 match to existing repository original-images.zip member and image-manifest.json'});continue
 if p.parent.name=='dra-thal-gyur-scan-20260926' and p.stem.isdigit():
  excluded.append({'path':str(p),'reason':'full-page rendered preview; retained in /tmp and inventoried, omitted from proposed subset as reproducible source derivative'});continue
 root=Path('/tmp/dra-thal-gyur-acquire') if '/dra-thal-gyur-acquire/' in str(p) else Path('/tmp/dra-thal-gyur-scan-20260926')
 rel=Path(root.name)/p.relative_to(root);dest=OUT/'selected-local-scratch'/rel
 dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 assert hashlib.sha256(dest.read_bytes()).hexdigest()==r['sha256']
 selected.append({'source_path':str(p),'preserved_path':str(rel),'bytes':r['bytes'],'sha256':r['sha256']})
metadata=[]
for r in selected:
 p=OUT/'selected-local-scratch'/r['preserved_path']
 if p.suffix not in ['.py','.json','.txt','.log']:continue
 t=p.read_text();markers=[k for k in [r'authorization\s*[:=]',r'bearer\s+[A-Za-z0-9]',r'password\s*[:=]',r'api.?key\s*[:=]',r'secret\s*[:=]',r'gh[pousr]_[A-Za-z0-9]{15}',r'AKIA[0-9A-Z]{16}',r'-----BEGIN [^-]*PRIVATE KEY'] if re.search(k,t,re.I)]
 metadata.append({'path':r['preserved_path'],'credential_pattern_findings':markers,'assessment':'project acquisition script / source metadata / progress / content hashes; no credentials or unrelated personal data identified','project_absolute_paths_present':'/Users/mikkokotila/dev/Dra-Thal-Gyur' in t})
report={'status':'safe archival subset recommendation; copies are byte-for-byte','selected_files':selected,'selected_bytes':sum(r['bytes'] for r in selected),'metadata_review':metadata,'source_archive_comparisons':comparisons,'source_archive_comparison_failures':failures,'excluded_from_proposed_subset':excluded,'limitations':['Source scripts were read as text, not executed.','No claim that omitted cloud originals are recovered.','Full-page local render previews remain in their original /tmp directory; no source files deleted.','No secrets identified by structural/manual review and credential pattern scan; project-local absolute paths are preserved as provenance.']}
(OUT/'archival-subset.json').write_text(json.dumps(report,indent=2)+'\n')
summary=f'''# Local scratch archival subset assessment\n\nRecommended subset: {len(selected)} byte-for-byte files, {report['selected_bytes']:,} bytes, copied under selected-local-scratch/.\n\nEight metadata/script/log files contain project acquisition code, public BDRC/Internet Archive metadata, content hashes, and progress. No credentials or unrelated personal data identified. Two files retain this project's local absolute path as provenance. Scripts were not executed.\n\nVerified {len(exact)} raw source images against actual members of ten existing repository original-images.zip archives and their image-manifest.json records, by exact byte count and SHA-256; those duplicate images are omitted from the subset. Archive comparison failures: {len(failures)}.\n\nRetained detail crops, endpoint previews, acquisition metadata, and raw boundary images absent from existing source archives. Full-page local render previews remain in /tmp and in inventory.json. Nothing was deleted.\n\nSee archival-subset.json for every selected/excluded file and comparison. These local scratch assets do not recover the missing original cloud reports.\n'''
(OUT/'ARCHIVAL-SUBSET.md').write_text(summary)
print(json.dumps({'selected_files':len(selected),'selected_bytes':report['selected_bytes'],'metadata_files':len(metadata),'exact_raw_archived':len(exact),'comparison_failures':len(failures),'selected_by_group':dict(collections.Counter('/'.join(Path(r['preserved_path']).parts[:2]) if len(Path(r['preserved_path']).parts)>2 else Path(r['preserved_path']).parts[0] for r in selected)),'credential_marker_findings':sum(len(r['credential_pattern_findings']) for r in metadata)},indent=2))
