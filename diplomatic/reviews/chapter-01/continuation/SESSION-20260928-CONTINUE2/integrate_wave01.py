"""Integrate this captured wave's bounded findings; no inferred completion."""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
D = R / 'diplomatic'
C = D / 'collation/chapter-01'
V = D / 'reviews/chapter-01/continuation'
S = V / 'SESSION-20260928-CONTINUE2'
load = lambda p: json.loads(p.read_text())
def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

plans = load(S / 'session-plan.json')['plans']
inputs = {}
for plan in plans:
    stem = R / plan['output_stem']
    er = load(Path(str(stem) + '-execution.json'))
    assert er['returncode'] == 0 and not er['unexpected_tool_items']
    assert er['unparseable_event_lines'] == 0
    for path, digest in er['output_hashes'].items():
        assert sha(R / path) == digest, path
    inputs[plan['task']] = (plan, load(Path(str(stem) + '-reading.txt')))
additional = load(C / 'additional-interventions.json')
comparisons = load(C / 'scan-comparison-loci.json')
coverage = load(C / 'scan-coverage.json')
queue = load(D / 'WORK-QUEUE.json')
tasks = {t['id']: t for t in queue['tasks']}
old_additional = copy.deepcopy(additional)
old_comparisons = copy.deepcopy(comparisons)
new_ids = {p['task']: [] for p in plans}
BASE = subprocess.check_output(['git','rev-parse','HEAD'], cwd=R, text=True).strip()
units = {x['id']: x for x in load(C / 'reading-units.json')}

def evidence(plan, target_page):
    manifest = load(R / plan['manifest'])
    views = manifest['pages'] + manifest['views']
    views += load((R / plan['manifest']).parent / 'focused-views.json')['views']
    result = []
    for item in views:
        if item['pdf_page'] != target_page:
            continue
        assert sha(R / item['path']) == item['sha256']
        result.append(str((R / item['path']).relative_to(D)))
    return result

def append_observation(task, prefix, observation, target_page, selected_units=None):
    plan, raw = inputs[task]
    ident = prefix + '-' + observation['id']
    assert not any(x['id'] == ident for x in comparisons), ident
    anchors = selected_units or observation['anchors']
    assert all(x in units for x in anchors), anchors
    kind = observation.get('category', 'bounded_uncertainty')
    source = observation.get('source_span')
    confidence = observation.get('confidence', observation.get('confidence_by_dimension', {}))
    question = observation.get('question', '')
    reason = observation.get('rationale', question)
    if source is None:
        source = '[Unresolved inspected source interval: ' + question + ']'
    elif not isinstance(source, str):
        source = json.dumps(source, ensure_ascii=False)
    uncertain = 'uncertain' in kind or 'unresolved' in kind or '⟦Q' in source
    entry = {'id': ident, 'witness': 'Tingkye' if task == 'C1-TINGKYE' else 'Tsamdrak',
        'units': anchors, 'base_snippet_at_review': observation.get('base_span'),
        'comparison_reading': source,
        'status': 'bounded_uncertainty' if uncertain else 'qualified_local_observation',
        'confidence': json.dumps(confidence, ensure_ascii=False) if isinstance(confidence, dict) else str(confidence),
        'locator': 'PDF ' + str(target_page) + '; native bounds and row context: ' + json.dumps(observation.get('approximate_native_bounds'), ensure_ascii=False),
        'rationale': reason + ' Scope is the stated local observation, not unqualified certification of every neighboring glyph. Editorial Q markers and sign codes are defined in the raw report.',
        'decision': 'Retain governing Adzom unchanged. Preserve this comparison-witness observation and its uncertainty; no global absence or reconstructed history is inferred.',
        'evidence': evidence(plan, target_page),
        'review': 'reviews/chapter-01/continuation/' + task + '.md',
        'continuation_provenance': {'batch_id': plan['batch'], 'baseline_commit': BASE,
            'raw_report': {'path': plan['output_stem'] + '-reading.txt', 'sha256': sha(R / (plan['output_stem'] + '-reading.txt'))},
            'observation': observation,
            'coordinator_scope': 'Target native overview and all target row bands inspected; reported local distinctions retained within their stated confidence, not promoted to blanket agreement.'}}
    comparisons.append(entry)
    new_ids[task].append(ident)
    return ident

# Source rows and all uncertainties remain in the raw ledger. Apparatus is localized.
for task, prefix, page, selected in [
    ('C1-TINGKYE', 'TK-CONT2', 4, set('B02-O%02d' % i for i in range(2, 12))),
    ('C1-TSAMDRAK', 'TS-CONT2', 14, set('B02-O%02d' % i for i in range(2, 15)))] :
    plan, raw = inputs[task]
    for obs in raw['observations']:
        if obs['id'] not in selected:
            continue
        expanded = ['U%05d' % i for i in range(106, 127)] if task == 'C1-TINGKYE' and obs['id'] == 'B02-O11' else None
        append_observation(task, prefix, obs, page, expanded)
    qids = {'Q01','Q02','Q03','Q04','Q05','Q06'} if task == 'C1-TINGKYE' else {'Q01'}
    for q in raw['unread_after_inspection']:
        if q['id'] not in qids:
            continue
        assert q.get('anchor') in units
        obs = {'id':'B02-' + q['id'], 'anchors':[q['anchor']],
            'source_span': None, 'base_span': units[q['anchor']]['reading_tibetan'],
            'category':'bounded_glyph_uncertainty', 'question':q['question'],
            'neighboring_context':q.get('resolved_context', q.get('scope')),
            'approximate_native_bounds':q.get('bounds', q.get('approximate_native_bounds')),
            'confidence':{'location':'source-based local correspondence', 'exact_reading':'unresolved'},
            'rationale':q['question']}
        append_observation(task, prefix, obs, page)

# New page101 search evidence extends existing notes, without doubling the ink.
plan, raw = inputs['C1-BASE-UNCERTAINTIES']
for rec in additional:
    if rec['id'] not in {'SCAN-CH1-LAYER-02615', 'SCAN-CH1-LAYER-02620'}:
        continue
    assert 'continuation_review_20260928_p101' not in rec
    rec['continuation_review_20260928_p101'] = {
        'batch_id':plan['batch'], 'previous_rationale':rec['rationale'],
        'raw_report':plan['output_stem'] + '-reading.txt',
        'raw_report_sha256':sha(R / (plan['output_stem'] + '-reading.txt')),
        'source_search':raw['coverage_assessment'],
        'bounded_questions':raw['unread_after_inspection'],
        'coordinator_disposition':'The dense fourth-row locus is inventoried once. No exact phrase is supplied from transcript expectations; source-note strings and earlier qualified layer separation remain unchanged.'}
    rec['reading_uncertainty'] = True
    rec['rationale'] += ' The later B02-P0101 all-row phrase search again leaves the two transcript-note wordings unverified. One dense fourth-row locus is inventoried once with four bounded component questions; it is not used twice to manufacture two attestations. Non-identification is not historical absence.'
    rec['evidence'] = list(dict.fromkeys(rec['evidence'] + evidence(plan, 101)))
    new_ids[plan['task']].append(rec['id'])

# A separate detail reader clarifies the PDF3 marginal text and graphic limits.
p3_plan, p3_raw = inputs['C1-BASE-PHYSICAL']
adj_stem = V / 'C1-BASE-PHYSICAL-B02-P0003-detail-adjudication'
adj_path = Path(str(adj_stem) + '-reading.txt')
adj = load(adj_path)
adj_receipt = load(Path(str(adj_stem) + '-execution.json'))
assert adj_receipt['returncode'] == 0 and not adj_receipt['unexpected_tool_items']
for path, digest in adj_receipt['output_hashes'].items():
    assert sha(R / path) == digest
assert not any(r['id'] == 'SCAN-CH1-SIGN-00014-UNCERTAIN' for r in additional)
original = units['U00014']['source_tibetan']
p3_dir = (R / p3_plan['manifest']).parent
p3_ev = evidence(p3_plan, 3)
p3_ev += [str((p3_dir / n).relative_to(D)) for n in ['U00014-incoming-boundary-detail.png', 'margin-inscription-extended-rotated90.png']]
additional.append({'id':'SCAN-CH1-SIGN-00014-UNCERTAIN', 'units':['U00014'],
    'original_units':{'U00014':original}, 'replacement_units':{}, 'old':original,
    'new':original, 'reading_label':'Unchanged transcript scaffold; first terminal sign graphically unresolved',
    'reading_uncertainty':True,
    'rationale':'At PDF3 row1 after the incoming las, the source has a tiered punctuation-like graph followed by a separate ordinary shad. Two informed image readings and the coordinator distinguish it from a plain upright. U+0F11 is a moderate encoding hypothesis only, not adopted. The lower curl entering the detail belongs to neighboring-row vowel material and is not an extra punctuation tier. Retain the transcript string provisionally with this visible qualification rather than assert that both printed marks are ordinary shads. The coordinator initial two-ordinary-shad inventory is superseded at this boundary; its earlier draft is retained.',
    'locator':'Adzom PDF3 / BDRC5 / member0005.png / row1 incoming U00014 terminal; exact detail bounds [1720,365,2110,615]',
    'evidence':p3_ev + [str(adj_path.relative_to(D))],
    'confidence':{'physical_correspondence':'high', 'tiered_graph_presence':'high', 'exact_Unicode_encoding':'unresolved; U+0F11 moderate hypothesis'},
    'continuation_review':{'batch_id':'B02-P0003', 'raw_report':p3_plan['output_stem'] + '-reading.txt', 'adjudication':str(adj_path.relative_to(R)), 'adjudication_sha256':sha(adj_path), 'source_component_record':adj}})
new_ids['C1-BASE-PHYSICAL'].append('SCAN-CH1-SIGN-00014-UNCERTAIN')

summaries = {
 'C1-BASE-UNCERTAINTIES':'PDF101 all six rows searched; U02615 wording not identified and U02620 candidate locus remains unread in bounded components. No source phrase or spelling changed.',
 'C1-BASE-PHYSICAL':'All four PDF3 main rows, twelve unit boundaries, internal row/page turns and non-main regions inventoried. Eleven ordinary double-shad boundaries retained. U00014 tiered graphic remains encoding-uncertain; marginal components now read in their physical order. No lexical correction.',
 'C1-TINGKYE':'PDF4 rows4-7 followed in full, continuing U00106 to the outgoing U00127 fragment. Twenty-one graphic delimiters and bounded glyph questions recorded. PDF5 row1 is context only; new frontier is PDF5 row1, not the older isolated PDF6 check.',
 'C1-TSAMDRAK':'PDF14 all seven rows followed from incoming U00350 to U00383, with source additions, lexical variants, numeral-like annotation and graphic boundaries preserved. Local unread glyphs/signs remain explicit; next full-page comparison is PDF15.'}
next_spans = {
 'C1-BASE-UNCERTAINTIES':'PDF102 S09 boundary inscription, then title/portrait scopes; preserve the unresolved PDF60/PDF101 findings without endlessly repeating identical evidence.',
 'C1-BASE-PHYSICAL':'PDF4 full physical inventory and remaining page1/2/5 scopes; PDF3 has explicitly bounded remaining graphic questions, not unread whole rows.',
 'C1-TINGKYE':'PDF5 row1, U00127 outgoing join and U00128 onward; PDF4 targeted glyph and marginal questions remain visible.',
 'C1-TSAMDRAK':'PDF15 row1, expected following U00383 but exact source correspondence must be established; preserve PDF14 bounded questions.'}
coverage.setdefault('continuation_bounded_reviews', [])
for task, (plan, raw) in inputs.items():
    report_path = V / (task + '.json')
    report = load(report_path)
    b = next(x for x in report['batches'] if x['batch_id'] == plan['batch'])
    b.update(status='review_integrated_with_bounded_uncertainties',
        rows_actually_compared=raw['rows'], observations=raw['observations'],
        unread_or_uncertain_spans=raw['unread_after_inspection'],
        unexamined_spans=raw['unexamined_spans'], canonical_record_ids=new_ids[task],
        next_physical_span=next_spans[task], summary=summaries[task],
        reader_findings=raw, whole_pages_newly_certified=[],
        prior_verified_raw_report_commit='66076df0a746baeab74630407e6bcbb4059db2de')
    if task == 'C1-BASE-PHYSICAL':
        b['detail_adjudication'] = {'path':str(adj_path.relative_to(R)), 'sha256':sha(adj_path), 'findings':adj}
        b['marginal_physical_order'] = ['ཀ','སྒྲ་','གཉིས་','ཐལ་འགྱུར']
        b['marginal_limits'] = 'The gnyis reading has moderate-high support; its foliation function remains probable. No terminal shad established. Components remain outside main text.'
        b['superseded_coordinator_proposal'] = 'Initial draft treated U00014 as two ordinary shads; the source tiered graph plus one shad replaces that overly broad interpretation. Original draft preserved in session folder.'
    report['next_physical_span'] = next_spans[task]
    report['coverage_complete'] = False
    dump(report_path, report)
    tasks[task].update(owner='ChatGPT-coordinator-20260928-continue2', status='in_progress', next_physical_span=next_spans[task])
    coverage['continuation_bounded_reviews'].append({'task_id':task, 'batch_id':plan['batch'],
        'report':'reviews/chapter-01/continuation/' + task + '.json',
        'summary':summaries[task], 'rows_reported':len(raw['rows']),
        'canonical_record_ids':new_ids[task], 'whole_pages_newly_certified':[],
        'coverage_assessment':raw['coverage_assessment'], 'next_physical_span':next_spans[task]})
    md_path = V / (task + '.md')
    heading = '\n\n## ' + plan['batch'] + ' — continued source inspection\n'
    assert heading not in md_path.read_text()
    md = heading + '\n' + summaries[task] + '\n\n[Raw reading](' + Path(plan['output_stem']).name + '-reading.txt). The complete row ledger and sign legend are retained in the structured report.\n'
    for row in raw['rows']:
        md += '\n### Physical row ' + str(row.get('physical_row', '?')) + '\n\n```text\n' + row.get('observed_sequence', '[No continuous transcription adopted.]') + '\n```\n'
    md += '\n### Bounded questions retained\n\n'
    for question in raw['unread_after_inspection']:
        md += '**' + str(question.get('id', 'Unresolved')) + ':** ' + question.get('question', str(question)) + '\n\n'
    if task == 'C1-BASE-PHYSICAL':
        md += 'The subsequent [detail reading](C1-BASE-PHYSICAL-B02-P0003-detail-adjudication-reading.txt) reads marginal components in physical order as `ཀ | སྒྲ་ | གཉིས་ | ཐལ་འགྱུར`. The possible foliation interrupts the title physically. The tiered U00014 boundary is not normalized to an ordinary shad; its exact encoding remains open. Neighboring-row vowel ink is excluded.\n\n'
    md += 'Next: ' + next_spans[task] + '\n\nThis completed bounded inspection does not certify unexamined portions of the chapter. Unresolved glyphs are not agreement, missing text, or source unavailability.\n'
    md_path.write_text(md_path.read_text() + md)

assert comparisons[:len(old_comparisons)] == old_comparisons
assert len(additional) == len(old_additional) + 1
assert all(a == b for a,b in zip(old_additional,additional) if a['id'] not in {'SCAN-CH1-LAYER-02615','SCAN-CH1-LAYER-02620'})
dump(C / 'additional-interventions.json', additional)
dump(C / 'scan-comparison-loci.json', comparisons)
dump(C / 'scan-coverage.json', coverage)
dump(D / 'WORK-QUEUE.json', queue)
dump(S / 'wave01-integration-authored.json', {'baseline_commit':BASE,
    'new_comparison_records':len(comparisons)-len(old_comparisons),
    'new_ids':new_ids, 'base_lexical_readings_changed':False,
    'expected_reading_status_changes':['U00014','U02620'],
    'scope':'Authored changes; build, validation and verified publication still required.'})
print('AUTHORED', len(comparisons)-len(old_comparisons), 'comparison observations; no base lexical change.')
