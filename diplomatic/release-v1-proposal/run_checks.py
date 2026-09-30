"""Run real chapter checks and save a compact, per-checkpoint status report."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys
sys.dont_write_bytecode = True
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--repo', required=True, type=Path)
ap.add_argument('--step', required=True)
ap.add_argument('--rebuild', action='store_true')
a = ap.parse_args(); root = a.repo.resolve(); folder = root/'diplomatic/release-v1-proposal'
assert a.step.replace('-', '').isalnum()
results = {'parent_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(), 'checks':{}}
def run(tool, extra):
    r = subprocess.run([sys.executable,str(root/'diplomatic/tools'/tool),'--repo',str(root),*extra],cwd=root,text=True,capture_output=True)
    if r.returncode:
        (folder/'checkpoints'/(a.step+'-failure.txt')).write_text(r.stdout+'\n'+r.stderr)
        raise RuntimeError(tool+' failed; output preserved')
    return json.loads(r.stdout)
if a.rebuild:
    b = run('build_chapter1.py', [])
    results['checks']['build'] = {k:b[k] for k in ['base_units_accounted_for','scan_restored_main_verse_lines','scan_correction_or_layer_separation_records','local_comparison_scan_findings_including_candidates','chapter_markdown_sha256']}
results['checks']['validation'] = run('validate_chapter1.py', [] if a.rebuild else ['--check'])
results['checks']['reproducibility'] = run('build_chapter1.py', ['--check'])
progress = run('release_progress.py', [])
(folder/'PROGRESS.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n')
results['progress'] = progress
plan = json.loads((folder/'PLAN.json').read_text())
for name in ['reading-units.json','ch1-scan-insertions.json']:
    relative = 'diplomatic/collation/chapter-01/'+name
    old = json.loads(subprocess.check_output(['git','show',plan['audited_commit']+':'+relative],cwd=root,text=True))
    current = json.loads((root/relative).read_text())
    if name == 'reading-units.json':
        fields = ['id','source_tibetan','reading_tibetan']
        assert [{k:x[k] for k in fields} for x in old] == [{k:x[k] for k in fields} for x in current]
    else:
        assert old == current
results['accepted_readings_and_insertions_preserved_from_audited_baseline'] = True
results['validation_is_not_exhaustive_scholarly_certification'] = True
output = folder/'checkpoints'/(a.step+'-checks.json')
assert not output.exists(), 'Use a new step name; do not overwrite a checkpoint receipt'
output.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks_passed':True,'packets':{k:progress['packets'][k] for k in ['integrated','deferred_not_collated','remaining']},'loci':progress['release_locus_acceptance'],'deliverables':progress['release_artifacts'],'restored_main_verses':results['checks']['validation']['restored_main_verses']},ensure_ascii=False))
