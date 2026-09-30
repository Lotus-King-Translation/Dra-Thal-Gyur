"""Apply one explicitly reviewed v1 packet through the existing integration API.
No image reading or editorial selection is performed by this command.
"""
from pathlib import Path
import argparse, json, subprocess, sys
sys.dont_write_bytecode = True
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo', type=Path, required=True)
parser.add_argument('--request', required=True)
args = parser.parse_args(); root = args.repo.resolve()
request_path = (root / args.request).resolve()
assert request_path.is_relative_to(root / 'diplomatic/release-v1-proposal')
request = json.loads(request_path.read_text())
assert request['parent_commit'] == subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
review = root / 'diplomatic/reviews/chapter-01/continuation'
sys.path.insert(0, str(review / 'SESSION-20260929-CLOSE-INTEGRATION'))
import integrate_reviewed_batch as integration
integration.R = root; integration.D = root / 'diplomatic'
integration.C = integration.D / 'collation/chapter-01'; integration.V = review
result = integration.integrate(request['plan'], request['decisions'])
result['request'] = args.request
result['parent_commit'] = request['parent_commit']
result['scope'] = 'Bounded v1 integration; existing exhaustive gate remains unfinished.'
result_path = request_path.with_name(request_path.stem + '-result.json')
assert not result_path.exists()
result_path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
