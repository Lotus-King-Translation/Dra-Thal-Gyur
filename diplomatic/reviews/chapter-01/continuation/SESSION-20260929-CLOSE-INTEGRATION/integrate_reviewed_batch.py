"""Integrate explicitly selected coordinator decisions, never infer acceptance.
Raw reports and source strings remain unchanged. No commit or automatic completion.
"""
from pathlib import Path
import copy, importlib.util, json, re, subprocess, sys
R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
D = R / 'diplomatic'; C = D / 'collation/chapter-01'
V = D / 'reviews/chapter-01/continuation'
S = V / 'SESSION-20260929-INTEGRATION'
sys.path.insert(0, str(S))
import integration_helpers as ih
load = ih.load; dump = ih.dump

def integrate(plan, decisions):
    raw, receipt = ih.verify_report(R, plan)
    before_units = load(C / 'reading-units.json')
    before_insertions = load(C / 'ch1-scan-insertions.json')
    before_interventions = load(C / 'additional-interventions.json')
    obs = {o['id']: copy.deepcopy(o) for o in raw['observations']}
    supplements = decisions.get('supplementary_observations', [])
    assert not set(obs) & {o['id'] for o in supplements}
    obs.update({o['id']: copy.deepcopy(o) for o in supplements})
    questions = {x['id']: x for x in raw.get('unread_after_inspection', [])}
    selected = decisions['selected_observations']
    assert set(selected) <= obs.keys()
    assert set(decisions['coordinator']['observation_dispositions']) == {o['id'] for o in raw['observations']}
    units = {x['id']: x for x in before_units}
    records = load(C / 'scan-comparison-loci.json')
    old_records = copy.deepcopy(records)
    statuses = decisions['record_statuses']
    assert set(statuses) == set(selected)
    new_records = []
    for oid in selected:
        item = obs[oid]
        item.update(copy.deepcopy(decisions.get('observation_overrides', {}).get(oid, {})))
        page = item.get('pdf_page', plan['target_page'])
        assert page in plan.get('target_pages', [plan['target_page']])
        local_plan = {**plan, 'target_page': page}
        rid = decisions['record_prefix'] + '-' + oid
        new_records.append(ih.comparison_record(R, local_plan, item, rid,
            decisions['witness'], statuses[oid], decisions['base_disposition'],
            decisions['coordinator']['coordinator_scope']))
    for qid in decisions.get('separate_unrepresented_lexical_questions', []):
        item = questions[qid]
        anchor = item['anchor']; assert anchor in units
        page = item.get('pdf_page', plan['target_page'])
        description = item.get('exact_question', item.get('question', item.get('scope')))
        observation = {'id': qid, 'pdf_page': page, 'anchors': [anchor],
            'category': 'bounded_unresolved_component',
            'source_span': '[' + qid + '] ' + description,
            'base_span': units[anchor]['reading_tibetan'],
            'approximate_native_bounds': item.get('native_bounds', item.get('approximate_native_bounds')),
            'confidence': 'Unresolved; base quotation is a locator, not supplied witness text.',
            'rationale': description}
        new_records.append(ih.comparison_record(R, {**plan, 'target_page': page},
            observation, decisions['record_prefix'] + '-' + qid, decisions['witness'],
            'bounded_uncertainty', decisions['base_disposition'],
            decisions['coordinator']['coordinator_scope']))
    assert len(new_records) == decisions['planned_new_records']
    assert len({x['id'] for x in old_records + new_records}) == len(old_records) + len(new_records)
    ids = [x['id'] for x in new_records]
    ih.integrate_page(R, plan, decisions['coordinator'], ids)
    if supplements:
        rp = V / (plan['task'] + '.json'); report = load(rp)
        batch = next(b for b in report['batches'] if b['batch_id'] == plan['batch'])
        batch['supplementary_observations'] = supplements
        batch['supplementary_dispositions'] = decisions['supplementary_dispositions']
        dump(rp, report)
    dump(C / 'scan-comparison-loci.json', old_records + new_records)
    queue = load(D / 'WORK-QUEUE.json')
    task = next(t for t in queue['tasks'] if t['id'] == plan['task'])
    task.update(status='in_progress', owner='ChatGPT-coordinator-20260929-integration', current_batch_id=None,
                next_step=decisions['coordinator']['next_step'],
                last_integrated_batch_id=plan['batch'])
    queue['next_task_id'] = decisions['next_task_id']
    dump(D / 'WORK-QUEUE.json', queue)
    assert load(C / 'reading-units.json') == before_units
    assert load(C / 'ch1-scan-insertions.json') == before_insertions
    assert load(C / 'additional-interventions.json') == before_interventions
    assert load(C / 'scan-comparison-loci.json')[:len(old_records)] == old_records
    return {'verified_reader': receipt, 'new_record_ids': ids,
            'previous_records_unchanged': len(old_records),
            'all_2635_source_and_reading_strings_unchanged': True,
            'all_insertions_and_interventions_unchanged': True,
            'chapter_complete': False}
