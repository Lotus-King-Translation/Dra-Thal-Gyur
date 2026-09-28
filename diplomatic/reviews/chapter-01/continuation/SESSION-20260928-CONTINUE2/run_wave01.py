"""Capture four separately bounded readers; coordinator alone reviews/publishes."""
import concurrent.futures
import json
import subprocess
from pathlib import Path

R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
S = R / 'diplomatic/reviews/chapter-01/continuation/SESSION-20260928-CONTINUE2'
plans = json.loads((S / 'session-plan.json').read_text())['plans']

def run(plan):
    name = plan['task'] + '-' + plan['batch']
    print('START', name, flush=True)
    log = S / (name + '-capture.log')
    with log.open('x') as output:
        result = subprocess.run(['python3', 'diplomatic/tools/reading_batch.py',
            '--repo', str(R), 'capture', '--specification', plan['specification']],
            cwd=R, stdout=output, stderr=subprocess.STDOUT)
    print('FINISH', name, result.returncode, flush=True)
    return result.returncode

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(run, plans))
print('RETURN_CODES', results, flush=True)
raise SystemExit(0 if all(code == 0 for code in results) else 1)
