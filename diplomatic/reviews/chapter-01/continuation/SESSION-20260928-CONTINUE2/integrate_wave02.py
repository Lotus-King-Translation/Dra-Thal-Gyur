"""Integrate reviewed one-page ledgers, rejecting the page7 deletion proposal."""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
D = R/'diplomatic'; C = D/'collation/chapter-01'; V = D/'reviews/chapter-01/continuation'
S = V/'SESSION-20260928-CONTINUE2'
load = lambda p: json.loads(p.read_text())
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def text(x): return x if isinstance(x,str) else json.dumps(x,ensure_ascii=False)
BASE = subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
plans = load(S/'wave02-plan.json')['plans']
records = {}
for p in plans:
    stem = R/p['output_stem']; er = load(Path(str(stem)+'-execution.json'))
    assert er['returncode']==0 and not er['unexpected_tool_items'] and not er['unparseable_event_lines']
    for path,h in er['output_hashes'].items(): assert sha(R/path)==h,path
    records[(p['task'],p['batch'])] = (p,load(Path(str(stem)+'-reading.txt')))
AD=load(C/'additional-interventions.json'); SC=load(C/'scan-comparison-loci.json')
CV=load(C/'scan-coverage.json'); INS=load(C/'ch1-scan-insertions.json'); Q=load(D/'WORK-QUEUE.json')
T={t['id']:t for t in Q['tasks']}; U={u['id']:u for u in load(C/'reading-units.json')}
oldAD=copy.deepcopy(AD); oldSC=copy.deepcopy(SC); oldINS=copy.deepcopy(INS)
new_ids={key:[] for key in records}
