"""Smoke-check the initial proposed-release meter without editing project data."""
import importlib.util
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('release_progress', root / 'diplomatic/tools/release_progress.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result = module.report(root)
assert result['packets']['total'] == 8
assert result['release_locus_acceptance']['total'] == 183
assert result['accuracy_score'] is None
assert result['aggregate_completion_percentage'] is None
assert result['certifies_release_or_scholarship'] is False
assert not module.justified(root, {'rationale': 'No evidence'})
assert not module.justified(root, {'rationale': '', 'evidence': ['diplomatic/METHOD.md']})
assert module.justified(root, {'rationale': 'Reference exists, not proof of a glyph.', 'evidence': ['diplomatic/METHOD.md']})
try:
    module.inside(root, '../outside-repository')
except ValueError:
    pass
else:
    raise AssertionError('Path escape was not rejected')
print(json.dumps({'checks_passed': True, 'frozen_packets': 8, 'frozen_loci': 183, 'no_editorial_adoption_performed': True}))
