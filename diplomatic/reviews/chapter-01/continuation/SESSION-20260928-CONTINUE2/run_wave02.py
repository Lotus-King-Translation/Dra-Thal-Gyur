"""Capture eight disjoint one-page readers; never adopt their output automatically."""
import concurrent.futures
import json
import subprocess
from pathlib import Path

R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
S = R / 'diplomatic/reviews/chapter-01/continuation/SESSION-20260928-CONTINUE2'
plan = json.loads((S / 'wave02-plan.json').read_text())
assert len(plan['plans']) == 8

def capture(item):
    name = item['task'] + '-' + item['batch']
    print('START', name, flush=True)
    with (S / ('wave02-' + name + '-capture.log')).open('x') as output:
        result = subprocess.run(['python3','diplomatic/tools/reading_batch.py',
            '--repo',str(R),'capture','--specification',item['specification']],
            cwd=R,stdout=output,stderr=subprocess.STDOUT)
    print('FINISH',name,result.returncode,flush=True)
    return result.returncode

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(capture,plan['plans']))
print('RETURN_CODES',results,flush=True)
raise SystemExit(0 if all(x == 0 for x in results) else 1)
