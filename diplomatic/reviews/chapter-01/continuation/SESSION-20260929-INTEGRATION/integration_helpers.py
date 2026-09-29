"""Record coordinator-reviewed saved page reports; never infer editorial adoption.

The caller supplies all dispositions. Originals are hash-checked and untouched.
This helper does not commit, push, change a reading, or complete any task.
"""
from pathlib import Path
import copy
import hashlib
import json
import subprocess


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sha(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def verify_report(repo, plan):
    stem = repo / plan['output_stem']
    receipt = load(Path(str(stem) + '-execution.json'))
    assert receipt['returncode'] == 0, 'Incomplete reader process'
    assert not receipt.get('unexpected_tool_items'), 'Unexpected reader actions'
    assert not receipt.get('unparseable_event_lines'), 'Malformed reader log'
    for path, digest in receipt['output_hashes'].items():
        assert sha(repo / path) == digest, path
    for image in receipt['images']:
        assert sha(repo / image['path']) == image['sha256'], image['path']
    raw_path = Path(str(stem) + '-reading.txt')
    raw = load(raw_path)
    assert (raw['task_id'], raw['batch_id']) == (plan['task'], plan['batch'])
    return raw, {'raw_report': str(raw_path.relative_to(repo)),
                 'sha256': sha(raw_path), 'images_hash_verified': len(receipt['images']),
                 'execution_receipt': plan['output_stem'] + '-execution.json'}


def integrate_page(repo, plan, coordinator, canonical_ids=()):
    """Integrate one inspected page with explicit limits, not a completion claim."""
    assert coordinator.get('summary') and coordinator.get('next_step')
    assert 'observation_dispositions' in coordinator
    raw, verified = verify_report(repo, plan)
    dip = repo / 'diplomatic'
    review_path = dip / 'reviews/chapter-01/continuation' / (plan['task'] + '.json')
    report = load(review_path)
    matching = [b for b in report['batches'] if b['batch_id'] == plan['batch']]
    assert len(matching) == 1, 'Missing or duplicate batch identity'
    batch = matching[0]
    assert not batch.get('integration_20260929'), 'Batch already integrated'
    observed_ids = {str(o.get('id')) for o in raw.get('observations', [])}
    assert observed_ids == set(coordinator['observation_dispositions']), 'Every observation needs a disposition'
    observations = copy.deepcopy(raw.get('observations', []))
    for observation in observations:
        observation['coordinator_disposition'] = coordinator['observation_dispositions'][str(observation['id'])]
    batch.update({'status': 'review_integrated_with_bounded_uncertainties',
                  'rows_actually_compared': copy.deepcopy(raw.get('rows', [])),
                  'observations': observations,
                  'source_layers_and_non_main_regions': copy.deepcopy(raw.get('non_main_regions', [])),
                  'unread_or_uncertain_spans': copy.deepcopy(raw.get('unread_after_inspection', [])),
                  'unexamined_spans': copy.deepcopy(raw.get('unexamined_spans', [])),
                  'canonical_record_ids': list(canonical_ids),
                  'next_physical_span': coordinator['next_step'],
                  'integration_20260929': {'verified_inputs': verified,
                      'baseline_commit': subprocess.check_output(
                          ['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip(),
                      'coordinator': coordinator,
                      'reader_claims_not_automatically_certified': True}})
    if 'legend' in raw:
        batch['graphic_legend'] = copy.deepcopy(raw['legend'])
    if 'transcription_legend' in raw:
        batch['graphic_legend'] = copy.deepcopy(raw['transcription_legend'])
    batch['independent_review'] = {**batch.get('independent_review', {}), **verified,
                                  'scope': raw.get('coverage_assessment'),
                                  'proposals_adopted': False}
    coverage_path = dip / 'collation/chapter-01/scan-coverage.json'
    coverage = load(coverage_path)
    entries = coverage.setdefault('continuation_bounded_reviews', [])
    assert not any(e['task_id'] == plan['task'] and e['batch_id'] == plan['batch'] for e in entries)
    entries.append({'task_id': plan['task'], 'batch_id': plan['batch'],
                    'target_page': plan['target_page'],
                    'report': str(review_path.relative_to(dip)),
                    'summary': coordinator['summary'],
                    'rows_reported': len(raw.get('rows', [])),
                    'canonical_record_ids': list(canonical_ids),
                    'whole_pages_newly_certified': [],
                    'coverage_assessment': raw.get('coverage_assessment'),
                    'unread_after_inspection': copy.deepcopy(raw.get('unread_after_inspection', [])),
                    'unexamined_spans': copy.deepcopy(raw.get('unexamined_spans', [])),
                    'next_physical_span': coordinator['next_step'],
                    'reader_claims_require_coordinator_dispositions': True})
    markdown = review_path.with_suffix('.md')
    addition = '\n## ' + plan['batch'] + ' — preserved review integrated\n\n'
    addition += coordinator['summary'] + '\n\n'
    addition += '[Unchanged raw report](' + Path(verified['raw_report']).name + ') · '
    addition += '[Exact source and rows](' + review_path.name + ').\n\n'
    addition += coordinator.get('detail', '') + '\n\n'
    addition += '**Remaining:** ' + coordinator['next_step'] + '\n\n'
    addition += 'The full unresolved-component list and unexamined spans remain in the structured batch. This integration does not certify every glyph or the whole chapter.\n'
    assert '## ' + plan['batch'] + ' — preserved review integrated' not in markdown.read_text()
    dump(review_path, report)
    dump(coverage_path, coverage)
    with markdown.open('a', encoding='utf-8') as handle:
        handle.write(addition)
    return verified


def as_text(value):
    return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)


def comparison_record(repo, plan, observation, record_id, witness, status,
                      decision, coordinator_scope, comparison=None):
    """Build one explicitly selected, qualified apparatus record; no file writes."""
    anchors = observation.get('anchors', [])
    assert anchors and all(len(a) == 6 and a[0] == 'U' and a[1:].isdigit() for a in anchors)
    manifest = load(repo / plan['manifest'])
    page = plan['target_page']
    images = [item for item in manifest['pages'] + manifest['views'] if item['pdf_page'] == page]
    evidence = [item['path'].removeprefix('diplomatic/') for item in images]
    raw_path = plan['output_stem'] + '-reading.txt'
    evidence.append(raw_path.removeprefix('diplomatic/'))
    source = observation.get('source_span', observation.get('source_spans'))
    base = observation.get('base_span', observation.get('base_spans'))
    bounds = observation.get('approximate_native_bounds', observation.get('approx_native_bounds'))
    confidence = observation.get('confidence', observation.get('confidence_by_dimension', 'qualified'))
    return {'id': record_id, 'witness': witness, 'units': list(anchors),
            'base_snippet_at_review': as_text(base),
            'comparison_reading': as_text(source) if comparison is None else comparison,
            'status': status, 'confidence': as_text(confidence),
            'locator': f'PDF {page}; source-member and native bounds in linked packet; bounds: {as_text(bounds)}',
            'rationale': observation.get('rationale', '') + ' Reading scope and uncertainty are confined to the stated component; graphic/Q codes are defined in the linked raw report.',
            'decision': decision, 'evidence': evidence,
            'review': f'reviews/chapter-01/continuation/{plan["task"]}.md',
            'continuation_provenance': {'batch_id': plan['batch'],
                'baseline_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip(),
                'raw_report': {'path': raw_path, 'sha256': sha(repo / raw_path)},
                'observation': copy.deepcopy(observation),
                'coordinator_scope': coordinator_scope}}
