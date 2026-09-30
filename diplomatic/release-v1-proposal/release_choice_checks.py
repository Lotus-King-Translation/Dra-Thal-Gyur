"""Cross-check explicit v1 choices against canonical passages and displayed flags.
These checks validate consistency, not the correctness of a manuscript reading.
"""
from collections import defaultdict


def require(test, message):
    if not test:
        raise ValueError(message)


def validate_choices(machine, app, units, insertions, loci, choices):
    byunit = {u['id']: u for u in units}
    bylocus = {l['id']: l for l in loci}
    selected = choices['loci']
    require(set(selected) == set(bylocus), 'Release locus set changed')
    notes = app['scan_interventions']
    known_notes = {n['id'] for n in notes}
    known_insertions = {n['id'] for n in insertions}
    source_anchors = {u['id']: u for u in machine['source_anchors']}
    segments = {s['id']: s for s in machine['reading_sequence']}
    allowed = {'retain_base', 'adopt_evidenced_correction',
               'retain_with_explicit_uncertainty'}
    flagged = defaultdict(set)
    for ident, choice in selected.items():
        locus = bylocus[ident]
        ids = locus['source_units']
        require(choice['status'] in allowed, 'Invalid choice status: ' + ident)
        require(choice['source_units'] == ids, 'Choice anchor mapping changed: ' + ident)
        require(choice['exact_conflicts'] == locus['exact_conflicts'],
                'Choice exact-difference mapping changed: ' + ident)
        require(choice['release_reading'] == {u: byunit[u]['reading_tibetan'] for u in ids},
                'Recorded release reading disagrees with canonical text: ' + ident)
        require(choice['unit_reading_statuses'] == {u: byunit[u]['status'] for u in ids},
                'Canonical reading status lost in choice: ' + ident)
        retained_notes = set(choice.get('retained_intervention_ids', []))
        retained_insertions = set(choice.get('retained_insertion_ids', []))
        require(retained_notes <= known_notes and retained_insertions <= known_insertions,
                'Unknown intervention or restoration in choice: ' + ident)
        require(retained_notes == {n['id'] for n in notes if set(n['units']) & set(ids)},
                'Applicable intervention omitted from choice: ' + ident)
        require(retained_insertions == {n['id'] for n in insertions if n['after_unit'] in ids},
                'Applicable restoration omitted from choice: ' + ident)
        if choice['status'] == 'adopt_evidenced_correction':
            require(retained_notes or retained_insertions,
                    'Correction choice without accepted intervention: ' + ident)
        if choice['status'] == 'retain_with_explicit_uncertainty':
            uncertain = choice.get('uncertain_source_units', [])
            require(uncertain and len(uncertain) == len(set(uncertain)) and set(uncertain) <= set(ids),
                    'Uncertainty lacks exact in-locus anchors: ' + ident)
            for uid in uncertain:
                ref = 'release-choice:' + ident
                require(ref in source_anchors[uid]['uncertainty_refs']
                        and ref in segments[uid]['uncertainty_refs'],
                        'Release uncertainty not displayed: ' + ident + '/' + uid)
                flagged[ident].add(uid)
    return {'release_choices_cross_checked': len(selected),
            'uncertain_release_choices_cross_checked': len(flagged)}
