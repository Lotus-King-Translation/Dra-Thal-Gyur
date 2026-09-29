"""Run one explicitly reviewed, bounded integration in a real Git checkout.

No glyph selection is made here. The coordinator provides the complete decision
file. The existing integration and validation tools retain their own checks.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import re
import subprocess
import sys
from collections import Counter


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--request', type=Path, required=True)
    args = parser.parse_args()
    root = args.repo.resolve()
    def inside(relative: str) -> Path:
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise ValueError('Path leaves checkout')
        return path
    request = load(inside(str(args.request)))
    plan_file = inside(request['plan_path'])
    decision_file = inside(request['decision_path'])
    assert digest(plan_file) == request['plan_sha256']
    assert digest(decision_file) == request['decision_sha256']
    plans = load(plan_file)['plans']
    plan = next(p for p in plans if (p['task'],p['batch']) == (request['task_id'],request['batch_id']))
    plan = {**plan, 'target_page': plan['target_pages'][0]}
    decisions = load(decision_file)
    dip = root / 'diplomatic'; review = dip / 'reviews/chapter-01/continuation'
    assert request['task_id'] == decisions['task_id'] and request['batch_id'] == decisions['batch_id']
    for tool in ['validate_chapter1.py','build_chapter1.py']:
        subprocess.run([sys.executable,str(dip/'tools'/tool),'--repo',str(root),'--check'],cwd=root,check=True)
    output = inside(request['audit_directory'])
    assert output.is_relative_to(review) and not output.exists()
    output.mkdir(parents=True)
    audit = {'baseline_commit': subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),
             'request': str(args.request), 'request_sha256': digest(inside(str(args.request))),
             'status': 'integration_started_not_validated', 'chapter_complete': False}
    def save():
        (output/'receipt.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    save()
    try:
        repair_ref = request.get('serialization_repair_receipt')
        if repair_ref:
            repair_path = inside(repair_ref)
            assert repair_path.is_relative_to(review)
            assert digest(repair_path) == request['serialization_repair_sha256']
            repair = load(repair_path)
            assert repair['original_report'] == plan['output_stem'] + '-reading.txt'
            original_path = inside(repair['original_report'])
            sidecar_path = inside(repair['parsed_sidecar'])
            assert original_path.is_relative_to(review) and sidecar_path.is_relative_to(review)
            assert original_path != sidecar_path and sidecar_path.suffix == '.json'
            original = original_path.read_text(encoding='utf-8')
            assert digest(original_path) == repair['original_sha256']
            count = repair['occurrences']
            assert type(count) is int and count > 0
            assert original.count(repair['old_exact_fragment']) == count
            expected = original.replace(repair['old_exact_fragment'], repair['new_exact_fragment'], count)
            assert re.findall(r'[\u0f00-\u0fff]+', original) == re.findall(r'[\u0f00-\u0fff]+', expected)
            payload = expected.encode('utf-8')
            assert hashlib.sha256(payload).hexdigest() == repair['parsed_sha256']
            parsed = json.loads(expected)
            assert (parsed['task_id'], parsed['batch_id']) == (plan['task'], plan['batch'])
            if sidecar_path.exists():
                assert sidecar_path.read_bytes() == payload
            else:
                with sidecar_path.open('xb') as handle:
                    handle.write(payload)
            plan['serialization_repair_receipt'] = repair_ref
            audit['serialization_repair'] = {'receipt': repair_ref,
                'receipt_sha256': digest(repair_path), 'original_unchanged': True,
                'sidecar': repair['parsed_sidecar'], 'sidecar_sha256': digest(sidecar_path)}
            save()
        sys.path.insert(0,str(review/'SESSION-20260929-INTEGRATION'))
        sys.path.insert(0,str(review/'SESSION-20260929-CLOSE-INTEGRATION'))
        module = importlib.import_module('integrate_reviewed_batch')
        # Bind the helper's checkout paths explicitly; no historical script is run.
        module.R=root; module.D=dip; module.C=dip/'collation/chapter-01'; module.V=review
        if 'record_statuses' not in decisions:
            raw, _ = module.ih.verify_report(root,plan)
            selected = decisions['selected_observations']
            uncertain = decisions['bounded_uncertainty']
            localized = decisions['localized_observation']
            assert set(uncertain).isdisjoint(localized)
            assert set(uncertain + localized) <= set(selected)
            dispositions = {o['id']: (decisions['uncertain_disposition'] if o['id'] in uncertain else decisions['default_selected_disposition'] if o['id'] in selected else decisions['unselected_disposition']) for o in raw['observations']}
            dispositions.update(decisions['special_dispositions'])
            questions = {q['id']: q for q in raw['unread_after_inspection']}
            overrides = {o['id']: {'approximate_native_bounds': questions[o['approximate_native_bounds']['question_ref']]['native_bounds']} for o in raw['observations'] if o['id'] in selected and isinstance(o.get('approximate_native_bounds'),dict) and 'question_ref' in o['approximate_native_bounds']}
            coordinator = dict(decisions['coordinator'])
            coordinator.update(summary=request['summary'],next_step=request['next_step'],observation_dispositions=dispositions)
            decisions = {key: decisions[key] for key in ['selected_observations','record_prefix','witness','base_disposition','planned_new_records','next_task_id']}
            decisions.update(record_statuses={oid: 'bounded_uncertainty' if oid in uncertain else 'localized_observation' if oid in localized else 'provisional_visual_observation' for oid in selected},observation_overrides=overrides,coordinator=coordinator)
        (output/'expanded-decisions.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
        audit['integration'] = module.integrate(plan,decisions)
        for tool,label,extra in [('build_chapter1.py','build',[]),('validate_chapter1.py','validation',[]),('build_chapter1.py','reproducibility',['--check'])]:
            result=subprocess.run([sys.executable,str(dip/'tools'/tool),'--repo',str(root),*extra],cwd=root,text=True,capture_output=True)
            (output/(label+'.stdout')).write_text(result.stdout)
            (output/(label+'.stderr')).write_text(result.stderr)
            if result.returncode:
                raise RuntimeError(tool+': '+result.stderr)
        validation=load(output/'validation.stdout')
        assert validation['base_units_accounted_for']==2635 and validation['restored_main_verses']==13
        assert not validation['chapter_complete'] and not validation['next_chapter_started']
        records=load(dip/'collation/chapter-01/scan-comparison-loci.json')
        counts=Counter(rec['witness'] for rec in records)
        status_path=dip/'WORK-STATUS.md'; text=status_path.read_text()
        text=re.sub(r'Current \[Chapter 1\]\(chapter-01.md\) SHA-256: `[0-9a-f]+`','Current [Chapter 1](chapter-01.md) SHA-256: `'+validation['markdown_sha256']+'`',text,count=1)
        line='- **'+str(len(records))+' comparison records**, including qualified observations and uncertainty: '+', '.join(k+' '+str(v) for k,v in sorted(counts.items()))+'. Not a confirmed-variant count or a coverage percentage.'
        text=re.sub(r'^- \*\*\d+ comparison records\*\*.*$',line,text,count=1,flags=re.M)
        text+='\n'+decisions['coordinator']['summary']+' '+decisions['coordinator']['next_step']+'\n'
        status_path.write_text(text)
        subprocess.run(['git','diff','--check'],cwd=root,check=True)
        audit.update(status='integrated_and_structurally_validated_publication_pending',validation=validation)
    except Exception as exc:
        audit.update(status='failed_or_partial_integration_requires_review',error=type(exc).__name__+': '+str(exc))
        raise
    finally:
        save()


if __name__=='__main__':
    main()
