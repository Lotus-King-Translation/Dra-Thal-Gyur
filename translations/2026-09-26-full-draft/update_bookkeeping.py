"""Recompute draft progress and coverage; never certify semantic correctness."""
from pathlib import Path
import csv, hashlib, json, re
B = Path(__file__).resolve().parent
R = B.parents[1]
def load_lines(p):
    return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines() if s.strip()]
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name, obj):
    (B / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
U = json.loads((B / 'data/source-units.json').read_text())
source = (R / 'source/W1KG11703_7.txt').read_text(encoding='utf-8')
assert all(source[u['start']:u['end']] == u['tibetan'] for u in U)
assert ''.join(u['tibetan'] for u in U) == source
for x in json.loads((R / 'GUIDANCE-PROVENANCE.json').read_text())['files']:
    assert digest(R / x['path']) == x['sha256'], x['path']
for x in json.loads((R / 'source/SOURCE.json').read_text())['files']:
    assert digest(R / 'source' / x['path']) == x['sha256'], x['path']
E, batches = {}, {}
for p in sorted((B / 'data').glob('english-*.jsonl')):
    for row in load_lines(p):
        for n, text in enumerate(row['en'], row['start']):
            assert n not in E and 1 <= n <= len(U) and isinstance(text, str) and text.strip(), (p, n)
            E[n], batches[n] = text, p.name
for name in ('scan-decisions.jsonl', 'translation-decisions.jsonl'):
    for row in load_lines(B / 'notes' / name):
        if 'english' in row:
            assert row['unit'] in E, (name, row['unit'])
            E[row['unit']] = row['english']
notes = [r for p in sorted((B / 'notes').glob('review-input-*.jsonl')) for r in load_lines(p)]
terms = load_lines(B / 'notes/terminology-input.jsonl')
by_unit = {}
for row in notes + terms:
    for n in row.get('units', []):
        by_unit.setdefault(n, set()).add(row['id'])
known = {r['id'] for r in notes + terms}
missing_refs = sorted({x for s in E.values() for x in re.findall(r'\[(N-[A-Za-z0-9-]+)\]', s)} - known)
S = load_lines(B / 'data/scan-only-units.jsonl')
pending = [u['id'] for n, u in enumerate(U, 1) if n not in E]
ends = [2635, 3622, 4305, 4763, 5197, 5448]
starts = [1] + [n + 1 for n in ends[:-1]]
chapters = [{'chapter': i, 'first_unit': f'U{a:05}', 'last_unit': f'U{z:05}', 'units': z-a+1, 'represented': sum(n in E for n in range(a,z+1)), 'drafted_through_end': all(n in E for n in range(a,z+1))} for i,(a,z) in enumerate(zip(starts,ends),1)]
with (B / 'COVERAGE.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['unit','source_start','source_end','state','english_batch','note_ids'])
    for n,u in enumerate(U,1):
        refs = sorted(by_unit.get(n,set()) | set(re.findall(r'\[(N-[A-Za-z0-9-]+)\]', E.get(n,''))))
        state = 'represented_with_review_flags' if n in E and refs else 'represented_draft' if n in E else 'not_processed'
        w.writerow([u['id'],u['start'],u['end'],state,batches.get(n,''),';'.join(refs)])
contiguous = 0
while contiguous + 1 in E:
    contiguous += 1
save('CONTINUATION.json', {'status': 'full draft represented; unresolved readings remain' if not pending else 'in progress; translator self-check, not independent QC', 'represented_etext_units': len(E), 'translated_units': len(E), 'count_qualification': 'Legacy translated_units counts represented draft units, not fully resolved translations.', 'total_etext_units': len(U), 'last_contiguous_unit': f'U{contiguous:05}', 'next_unit': pending[0] if pending else None, 'remaining_etext_units': len(pending), 'chapters_drafted': sum(c['drafted_through_end'] for c in chapters), 'source_unchanged': True, 'glossary_unchanged': True, 'scan_only_units': len(S), 'scan_only_unresolved_units': [s['id'] for s in S if 'unresolved' in s['status']], 'assembly_note': 'Apply explicit English overrides in scan-decisions.jsonl first, then translation-decisions.jsonl in file order. Other scan decisions document readings already used or unresolved; do not rewrite from them automatically.', 'independent_qc': 'not performed'})
save('PROGRESS.json', {'chapters': chapters, 'closing_material': {'first_unit': 'U05449', 'last_unit': 'U05466', 'represented': sum(n in E for n in range(5449,5467))}, 'missing_note_definitions': missing_refs, 'review_note_records': len(notes), 'terminology_records': len(terms), 'semantic_resolution': 'Not certified by these mechanical counts.'})
save('RUN.json', {'task': 'TRANSLATE', 'source': 'Adzom W1KG11703 volume 1; selected facsimile governs', 'source_text': 'source/W1KG11703_7.txt', 'source_sha256': digest(R/'source/W1KG11703_7.txt'), 'glossary_sha256': digest(R/'glossary/expanded_tibetan_english_glossary.csv'), 'guidance_sha256': digest(R/'guidelines/tibetan_translation_standard_v2.md'), 'unitization': 'Exact contiguous Unicode-character slices of unchanged e-text; punctuation, headings and source annotations included.', 'checks': ['all source slices equal supplied source', 'source slices reconstruct complete e-text', 'source assets and guidance/glossary hashes match provenance', 'JSONL valid', 'English unit IDs unique and nonempty', 'coverage and chapter counts rebuilt'], 'limitations': ['Mechanical checks are not semantic or independent QC.', 'Scan consultation and unresolved readings are separately recorded.', 'Source e-text has not received full diplomatic proofreading.', 'Provisional terminology has not been approved.']})
print(json.dumps({'represented':len(E),'total':len(U),'next':pending[0] if pending else None,'chapters_drafted':sum(c['drafted_through_end'] for c in chapters),'missing_note_definitions':missing_refs},ensure_ascii=False))
