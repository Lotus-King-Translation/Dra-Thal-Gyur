"""Load authored metadata without allowing it to override edition measurements."""
import json


STATUS_FIELDS = {
    'canonical_branch', 'current_handoff', 'current_work_status', 'work_queue',
    'recovery_checkpoint', 'sign_review_adoption_audit',
    'missing_later_original_reports', 'recovery_scope', 'recovery_progress',
}


def load_continuation(out):
    metadata = json.loads((out / 'CONTINUATION.json').read_text())
    assert metadata['schema_version'] == 1, 'Unsupported continuation schema'
    fields = metadata['status_fields']
    assert set(fields) == STATUS_FIELDS, 'Unexpected or missing authored status fields'
    for key in ('current_handoff', 'current_work_status', 'work_queue',
                'recovery_checkpoint', 'sign_review_adoption_audit'):
        target = (out / fields[key]).resolve()
        assert target.is_relative_to(out.resolve()) and target.is_file(), (key, target)
    recovery = fields['recovery_progress']
    assert fields['missing_later_original_reports'] == recovery['original_missing_report_identities']
    assert (recovery['complete_transcript_replay_bodies'] + recovery['incomplete_report_bodies']
            == recovery['original_missing_report_identities'])
    assert 0 <= recovery['original_pre_loss_byte_identity_verified'] <= recovery['original_missing_report_identities']
    return fields
