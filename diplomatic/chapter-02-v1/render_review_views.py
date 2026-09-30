"""Readable, exact review views of the frozen electronic collation; no choices."""
from pathlib import Path
import json
c=Path(__file__).resolve().parent
load=lambda name:json.loads((c/name).read_text())
lines=['# Chapter 2 — exact W comparison review view','',
       'Exact source Wylie and website lines follow. Difference labels are alignment aids, not accepted corrections.','']
for b in load('wikisource.json')['conflicts']:
    lines += ['## '+b['id']+' — '+', '.join(b['source_units']),
              'A: '+json.dumps(b['A_wylie'],ensure_ascii=False),
              'W: '+json.dumps([w['raw'] for w in b['W_lines']],ensure_ascii=False),
              'Differences: '+json.dumps(b['token_differences'],ensure_ascii=False),'']
(c/'W-REVIEW.md').write_text('\n'.join(lines).rstrip('\n')+'\n',encoding='utf-8')
print('W review blocks:',len(load('wikisource.json')['conflicts']))
