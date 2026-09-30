#!/usr/bin/env python3
"""Read-only meter for the proposed Chapter 1 v1 release; not a quality certificate.

Reports frozen packet and locus denominators separately. Reads identifiers and
acceptance metadata, not source glyphs. It never adopts readings or edits files.
"""
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def inside(repo: Path, value: str) -> Path:
    path = (repo / value).resolve()
    if not path.is_relative_to(repo):
        raise ValueError('Reference leaves repository: ' + value)
    return path


def justified(repo: Path, item: dict) -> bool:
    evidence = item.get('evidence', [])
    return bool(item.get('rationale', '').strip() and evidence
                and all(inside(repo, p.split('#', 1)[0]).is_file()
                        for p in evidence))


def report(repo: Path) -> dict:
    folder = repo / 'diplomatic/release-v1-proposal'
    plan = load(folder / 'PLAN.json')
    decisions = load(folder / 'DECISIONS.json')
    frozen = subprocess.check_output(
        ['git', 'show', plan['audited_commit'] + ':' + plan['locus_source']],
        cwd=repo, text=True)
    locus_ids = {x['id'] for x in json.loads(frozen)}
    if len(locus_ids) != plan['baseline_counts']['transcript_loci']:
        raise ValueError('Frozen locus denominator does not match the plan')
    if set(decisions['loci']) - locus_ids:
        raise ValueError('Unknown release locus; amend scope explicitly')
    accepted = []
    invalid = []
    for ident, item in decisions['loci'].items():
        ok = (item.get('status') in plan['release_locus_dispositions']
              and justified(repo, item))
        (accepted if ok else invalid).append(ident)
    packets = []
    for target in plan['pending_packets']:
        path = repo / ('diplomatic/reviews/chapter-01/continuation/'
                       + target['task'] + '.json')
        matches = [b for b in load(path).get('batches', [])
                   if b['batch_id'] == target['batch']]
        if len(matches) != 1:
            raise ValueError('Missing or duplicate batch: ' + target['batch'])
        batch = matches[0]
        key = target['task'] + '/' + target['batch']
        integrated = batch.get('status') in {
            'review_integrated_with_bounded_uncertainties',
            'target_review_integrated_unresolved'}
        defer = decisions.get('packet_deferrals', {}).get(key)
        deferred = bool(defer and justified(repo, defer))
        packets.append({**target, 'recorded_status': batch.get('status'),
                        'integrated': integrated,
                        'explicitly_deferred_not_collated': deferred,
                        'remaining': not (integrated or deferred)})
    artifacts = {key: inside(repo, value).is_file()
                 for key, value in plan['release_artifacts'].items()}
    return {
        'schema_version': 1,
        'scope': plan['title'],
        'proposal_approved': decisions.get('scope_approved', False),
        'audited_baseline': plan['audited_commit'],
        'packets': {'total': len(packets),
                    'integrated': sum(p['integrated'] for p in packets),
                    'deferred_not_collated': sum(
                        p['explicitly_deferred_not_collated'] for p in packets),
                    'remaining': sum(p['remaining'] for p in packets),
                    'items': packets},
        'release_locus_acceptance': {'total': len(locus_ids),
                                    'documented': len(accepted),
                                    'remaining': len(locus_ids) - len(accepted),
                                    'invalid_entry_ids': invalid,
                                    'not_a_count_of_unread_source_passages': True},
        'release_artifacts': {'total': len(artifacts),
                              'present': sum(artifacts.values()),
                              'items': artifacts},
        'preserved_baseline_counts': plan['baseline_counts'],
        'final_editorial_signoff_recorded': bool(
            decisions.get('final_editorial_signoff')),
        'accuracy_score': None,
        'aggregate_completion_percentage': None,
        'time_estimate': None,
        'certifies_release_or_scholarship': False,
        'caveat': plan['metric_caveat'],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path('.'))
    args = parser.parse_args()
    try:
        result = report(args.repo.resolve())
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, 'Release meter failed; no files changed: ' + str(error) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
