"""Verify generated source links, unit coverage and package hashes; no semantic QC."""
from pathlib import Path
import hashlib, json, re
B = Path(__file__).resolve().parent
files = [B/n for n in ['README.md','HANDOFF.md','Dra-Thal-Gyur-English.md','REVIEW-NOTES.md','SCAN-ONLY.md','USAGE-README.md']]
files += sorted((B/'draft').glob('*.md')) + sorted((B/'alignment').glob('*.md'))
errors, checked, cache = [], 0, {}
for p in files:
    text = p.read_text(encoding='utf-8')
    for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if '://' in dest or dest.startswith('mailto:'):
            continue
        filename, sep, anchor = dest.partition('#')
        target = (p.parent/filename).resolve() if filename else p
        checked += 1
        if not target.exists():
            errors.append([str(p.relative_to(B)),dest,'missing target']); continue
        if sep and anchor and target.is_file():
            if target not in cache:
                cache[target] = set(re.findall(r'<a id="([^"]+)"',target.read_text(encoding='utf-8')))
            if anchor not in cache[target]:
                errors.append([str(p.relative_to(B)),dest,'missing explicit anchor'])
assert not errors, errors[:20]
records = [json.loads(s) for s in (B/'ALIGNED.jsonl').read_text().splitlines() if s.strip()]
assert [r['id'] for r in records] == [f'U{n:05}' for n in range(1,5467)]
manifest_count = 0
for line in (B/'SHA256SUMS').read_text().splitlines():
    expected, name = line.split('  ',1)
    path = B/name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
    manifest_count += 1
for n,record in enumerate(records,1):
    part = next(i for i,(a,z) in enumerate([(1,2635),(2636,3622),(3623,4305),(4306,4763),(4764,5197),(5198,5448),(5449,5466)],1) if a <= n <= z)
    name = f'chapter-{part:02}' if part < 7 else 'closing-material'
    assert f'u{n:05}' in cache.get((B/'alignment'/f'{name}.md').resolve(),set())
print(json.dumps({'generated_markdown_files_checked':len(files),'local_links_checked':checked,'link_errors':errors,'aligned_units':len(records),'package_hashes_verified':manifest_count,'semantic_qc':False}))
