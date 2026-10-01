"""Source-based v2 structural decisions and immutable v1 pair lineage.

This module never consults English punctuation. The decision ledger is supporting
editorial evidence; source.md and translation.md remain canonical content.
"""
from collections import Counter
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'paired'
BASELINE = 'aae8883b13ff0f23da2603aecc12a64a15ffe25b'
FORMATS = ('prose', 'verse', 'h1', 'h2', 'h3')
KANAVA = {value: {'type': 'verse' if value == 'verse' else 'prose',
                   'initial_formatting': value if value.startswith('h') else 'body'}
          for value in FORMATS}


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def baseline_file(name):
    return subprocess.check_output(['git', '-C', str(ROOT), 'show', f'{BASELINE}:paired/{name}'])


@lru_cache(maxsize=1)
def baseline_pairs():
    source = baseline_file('source.md').decode()
    translation = baseline_file('translation.md').decode()
    pattern = r'<!-- pair: (DTG-\d{6}) \| golden: ([A-Za-z0-9 -]+) \| roles: ([a-z_ ]+) \| part: ([a-z0-9-]+) -->'
    pairs = [{'id': m[1], 'golden': m[2].split(), 'roles': m[3].split(), 'part': m[4]}
             for m in re.finditer(pattern, source)]
    require(len(pairs) == 2660, 'Incomplete pinned v1 pair inventory')
    require([p['id'] for p in pairs] == re.findall(r'<!-- pair: (DTG-\d{6}) -->', translation),
            'Pinned v1 pair symmetry')
    require([p['id'] for p in pairs] == [f'DTG-{i:06d}' for i in range(1, 2661)],
            'Pinned v1 pair identities')
    return pairs


def decisions():
    data = json.loads((HERE / 'v2/STRUCTURE-DECISIONS.json').read_text(encoding='utf-8'))
    require(data['baseline_commit'] == BASELINE, 'Wrong structural audit baseline')
    require(data['status'] == 'accepted-for-rendering', 'Unresolved structural decisions')
    require(data['unresolved_structural_decisions'] == [], 'Unresolved structural decisions')
    require(set(data['role_formats'].values()) <= set(FORMATS), 'Unsupported role format decision')
    require(all(v['format'] in FORMATS for v in data['object_overrides'].values()),
            'Unsupported object format decision')
    return data


def formats_for(golden, decision_data=None):
    data = decision_data if decision_data is not None else decisions()
    ids = {row['id'] for row in golden}
    require(set(data['object_overrides']) <= ids, 'Unknown object in structural decisions')
    formats = {}
    for row in golden:
        require(row['role'] in data['role_formats'], 'Unclassified golden role: ' + row['role'])
        override = data['object_overrides'].get(row['id'])
        formats[row['id']] = override['format'] if override else data['role_formats'][row['role']]
    return formats


def derive_pairs(golden, decision_data=None):
    """Split only structural boundaries; retain every unaffected v1 ID verbatim."""
    formats = formats_for(golden, decision_data)
    baseline = baseline_pairs()
    require([i for p in baseline for i in p['golden']] == [row['id'] for row in golden],
            'Pinned v1/golden coverage mismatch')
    result, lineage = [], []
    next_id = 2661
    for old in baseline:
        runs = []
        for ident in old['golden']:
            if not runs or formats[ident] != runs[-1]['format']:
                runs.append({'format': formats[ident], 'golden': []})
            runs[-1]['golden'].append(ident)
        changed = len(runs) > 1
        children = []
        for run in runs:
            ident = f'DTG-{next_id:06d}' if changed else old['id']
            next_id += int(changed)
            pair = {'id': ident, 'v1': old['id'], 'part': old['part'], **run}
            result.append(pair)
            children.append({'id': ident, 'format': run['format'], 'golden': run['golden']})
        lineage.append({'v1': old['id'], 'v1_golden': old['golden'],
                        'membership_changed': changed, 'v2': children})
    return result, lineage


def audit_report(golden):
    pairs, lineage = derive_pairs(golden)
    counts = Counter(p['format'] for p in pairs)
    old_count = Counter('mixed' if entry['membership_changed'] else entry['v2'][0]['format']
                        for entry in lineage)
    return {
        'schema': 'paired-structure-audit/1', 'generated': True,
        'basis': 'Pinned Tibetan roles/text and documented editorial hierarchy; no English punctuation classification.',
        'baseline_commit': BASELINE,
        'baseline_sha256': {name: digest(baseline_file(name)) for name in ('source.md', 'translation.md')},
        'v1_pairs_audited': len(lineage), 'v1_pairs_expected': 2660,
        'v1_formats': {name: old_count[name] for name in (*FORMATS, 'mixed')},
        'v2_pairs': len(pairs), 'v2_formats': {name: counts[name] for name in FORMATS},
        'golden_objects': sum(len(p['golden']) for p in pairs),
        'changed_v1_pairs': sum(entry['membership_changed'] for entry in lineage),
        'unchanged_v1_pairs': sum(not entry['membership_changed'] for entry in lineage),
        'new_pair_ids': [p['id'] for p in pairs if p['id'] != p['v1']],
        'split_golden_objects': 0, 'unresolved_structural_decisions': [],
        'lineage': lineage,
    }
