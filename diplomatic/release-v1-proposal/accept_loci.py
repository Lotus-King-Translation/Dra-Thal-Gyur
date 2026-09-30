"""Record explicit coordinator v1 choices without changing canonical readings.
Every accepted locus needs an authored, locus-specific rationale. The command
adds exact identifiers, reference readings and linked intervention metadata;
it does not choose text, normalize Tibetan, or claim new scan inspection.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys
sys.dont_write_bytecode = True
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--repo', type=Path, required=True)
ap.add_argument('--request', required=True)
a = ap.parse_args(); root = a.repo.resolve()
folder = root/'diplomatic/release-v1-proposal'; col = root/'diplomatic/collation/chapter-01'
def read(p): return json.loads(p.read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
request_path = (root/a.request).resolve()
assert request_path.is_relative_to(folder)
request = read(request_path); plan = read(folder/'PLAN.json')
assert request['parent_commit'] == subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
decisions = read(folder/'DECISIONS.json'); assert decisions['scope_approved']
loci = {x['id']:x for x in read(col/'chapter1-loci.json')}
units = {x['id']:x for x in read(col/'reading-units.json')}
notes = read(col/'additional-interventions.json')
assert set(request['choices']).isdisjoint(decisions['loci']), 'Do not overwrite earlier release choices'
assert set(request['choices']) <= loci.keys()
accepted = []
for ident, choice in request['choices'].items():
    assert choice['status'] in ['retain_base','adopt_evidenced_correction','retain_with_explicit_uncertainty']
    assert len(choice['rationale'].strip()) >= 40
    locus = loci[ident]; ids = locus['source_units']
    linked = [n for n in notes if set(n['units']) & set(ids)]
    evidence = ['diplomatic/collation/chapter-01/chapter1-loci.json#'+ident,
                'diplomatic/collation/chapter-01/reading-units.json']
    evidence += choice.get('evidence', [])
    if linked:
        evidence += ['diplomatic/collation/chapter-01/additional-interventions.json']
        evidence += ['diplomatic/'+p for n in linked for p in n.get('evidence', [])]
    evidence = list(dict.fromkeys(evidence))
    assert all((root/p.split('#')[0]).is_file() for p in evidence)
    decisions['loci'][ident] = {**choice,'source_units':ids,
        'exact_conflicts':locus['exact_conflicts'],
        'release_reading':{uid:units[uid]['reading_tibetan'] for uid in ids},
        'unit_reading_statuses':{uid:units[uid]['status'] for uid in ids},
        'retained_intervention_ids':[n['id'] for n in linked],
        'evidence':evidence,'review_method':request['review_method'],
        'fresh_scan_reading_performed':False,
        'acceptance_scope':'Release choice only; neither original-text reconstruction nor exhaustive witness agreement.',
        'canonical_source_sha256':digest(col/'chapter1-loci.json')}
    accepted.append(ident)
(folder/'DECISIONS.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
receipt = {'request':a.request,'request_sha256':digest(request_path),'accepted_ids':accepted,
           'total_accepted':len(decisions['loci']),'remaining':len(loci)-len(decisions['loci']),
           'canonical_reading_changed':False}
output = request_path.with_name(request_path.stem+'-result.json'); assert not output.exists()
output.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt))
