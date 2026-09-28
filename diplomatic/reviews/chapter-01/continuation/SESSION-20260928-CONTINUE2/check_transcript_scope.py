"""Verify exact acquired transcript provenance; do not infer unseen print readings."""
import hashlib
import json
import subprocess
from pathlib import Path

R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
D = R / 'diplomatic'
C = D / 'collation/chapter-01'
V = D / 'reviews/chapter-01/continuation'
E = D / 'evidence/chapter-01/continuation/C1-TRANSCRIPT-SCOPE'
load = lambda p: json.loads(p.read_text())
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p, x):
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

summary = load(C / 'chapter1-summary.json')
checks = {'scope':'Preserved electronic-source identity, exact quotation accounting and acquired-file inventory; not visual proofreading',
          'sources':[], 'unicode_normalization':'none'}
texts = {}
for siglum, rec in summary['sources'].items():
    path = R / rec['path']
    assert sha(path) == rec['full_file_sha256'], siglum
    text = path.read_text()
    chapter = text[rec['start']:rec['end']]
    assert hashlib.sha256(chapter.encode()).hexdigest() == rec['chapter_sha256']
    assert len(chapter.encode()) == rec['chapter_utf8_bytes']
    texts[siglum] = text
    checks['sources'].append({'siglum':siglum, 'path':rec['path'],
        'full_file_sha256':rec['full_file_sha256'], 'chapter_offsets':[rec['start'],rec['end']],
        'chapter_sha256':rec['chapter_sha256'], 'chapter_bytes':len(chapter.encode())})
sp = R / 'editions/sichuan-2016'
prov = load(sp / 'etext-provenance.json')
assert sha(R / prov['original']) == prov['original_sha256']
assert sha(R / prov['text']) == prov['text_sha256']
assert (sp / 's.txt').read_text(encoding='utf-8-sig').strip() == (sp / 'W3CN7084_7.txt').read_text().strip()
checks['sichuan_family'] = {'original_docx_hash_verified':True,
    'extracted_txt_hash_verified':True, 'separate_txt_matches_after_BOM_decode_and_outer_whitespace':True,
    'independent_witnesses_from_these_three_files':1,
    'docx_extraction_reperformed':False,
    'inventory':[{'path':str(p.relative_to(R)), 'bytes':p.stat().st_size, 'sha256':sha(p)} for p in sp.rglob('*') if p.is_file()],
    'full_scan_pdf_or_image_archive_acquired':bool(list(sp.glob('*.pdf')) + list(sp.glob('*.zip'))),
    'limitation':'No acquired full facsimile in this source directory; supplied S strings are transcript evidence only. Historical remote restrictions are not asserted as fresh global availability findings.'}
assert not checks['sichuan_family']['full_scan_pdf_or_image_archive_acquired']
wp = R / 'editions/adzom-wikisource'
wprov = load(wp / 'PROVENANCE.json')
assert sha(wp / 'source.wikitext') == wprov['raw_wikitext_sha256']
assert (wp / 'source.wikitext').read_bytes() == (wp / 'sgra-thal-gyur.wikitext').read_bytes()
lines = (wp / 'source.wikitext').read_text().splitlines()
assert lines[2664].strip() == '@2'
assert 'dang po' in lines[2663]
wd = load(C / 'wikisource-diffs.json')
assert wd['provenance'] == wprov
assert len(wd['conflicts']) == wd['stats']['conflict_blocks'] == 273
assert len({x['id'] for x in wd['conflicts']}) == 273
witness_quotations = source_quotations = 0
for conflict in wd['conflicts']:
    for unit in conflict['source_units']:
        assert texts['A'][unit['start']:unit['end']] == unit['tibetan'], unit['id']
        source_quotations += 1
    for line in conflict['wikisource_lines']:
        assert 1 <= line['line'] <= 2664
        assert lines[line['line']-1] == line['raw'], (conflict['id'],line['line'])
        witness_quotations += 1
checks['wikisource'] = {'revision_id':wprov['revision_id'],
    'revision_timestamp':wprov['revision_timestamp'], 'source_sha256':wprov['raw_wikitext_sha256'],
    'duplicate_files_identical':True, 'chapter_file_lines':[1,2664], 'next_chapter_marker_line':2665,
    'conflict_blocks':273, 'exact_source_quotations_checked':source_quotations,
    'exact_website_quotations_checked':witness_quotations,
    'alignment_only_normalization':wd['normalization_for_alignment_only'],
    'status':'Related digital reference, not an additional independently certified print; diagnostic Unicode conversion is not adopted.'}
result = subprocess.run(['python3','diplomatic/tools/validate_chapter1.py','--repo','.','--check'],
    cwd=R, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
(E / 'structural-reconstruction-check.stdout').write_text(result.stdout)
(E / 'structural-reconstruction-check.stderr').write_text(result.stderr)
assert result.returncode == 0
validation = json.loads(result.stdout)
assert validation['exact_reconstruction_checks'] == ['minimal_B_exact','minimal_S_exact','whole_unit_B_exact','whole_unit_S_exact']
checks['exact_reconstruction_checks'] = validation['exact_reconstruction_checks']
checks['all_checks_passed'] = True
checks['chapter_complete'] = False
checks['publication_status'] = 'Not yet published; coordinator must verify the remote checkpoint.'
dump(E / 'exact-transcript-scope-checks.json', checks)
print(json.dumps({'all_checks_passed':True,'W_exact_source_quotations':source_quotations,
    'W_exact_website_quotations':witness_quotations,'no_unseen_print_certification':True}, indent=2))
