#!/usr/bin/env python3
"""Mutation tests use in-memory copies only, never editorial originals."""
from pathlib import Path
import argparse, copy, json, sys
sys.dont_write_bytecode=True
from validate_release import check_data
ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo',required=True,type=Path)
a=ap.parse_args(); root=a.repo.resolve(); c=root/'diplomatic/chapter-02-v1'
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
m=load(c/'release/reading.json'); app=load(c/'release/apparatus.json')
inputs=[load(c/'source-units.json'),load(c/'DECISIONS.json'),load(c/'INTERVENTIONS.json')]
check_data(m,app,*inputs)
def segment(x,uid): return next(u for u in x['reading_sequence'] if u['id']==uid)
cases={
    'lost_original_anchor':lambda x,y:x['original_units'].pop(),
    'reordered_sequence':lambda x,y:x['reading_sequence'].reverse(),
    'changed_original_text':lambda x,y:x['original_units'][0].update(tibetan='incorrect'),
    'changed_selected_text':lambda x,y:segment(x,'U02714').update(text='incorrect'),
    'section_note_in_main':lambda x,y:segment(x,'U02680').update(role='main_text'),
    'joined_anchor_duplicated':lambda x,y:segment(x,'U02888').update(text='duplicate'),
    'lost_annotation_component':lambda x,y:x['source_annotations'].pop(),
    'changed_note_wording':lambda x,y:x['source_annotations'][0].update(text='incorrect'),
    'lost_uncertainty_flag':lambda x,y:segment(x,'U03240').update(uncertainty_refs=[]),
    'invented_boundary_reading':lambda x,y:x['transition_graphic'].update(reading='invented'),
    'false_full_proofread':lambda x,y:x.update(full_base_scan_proofread=True),
    'false_exhaustive_collation':lambda x,y:x.update(exhaustive_witness_collation=True),
    'invented_restored_verse':lambda x,y:x['new_main_verse_restorations'].append('invented'),
    'inconsistent_combined_text':lambda x,y:x.update(text_with_headings='incorrect'),
    'lost_intervention':lambda x,y:y['interventions'].pop(),
    'altered_release_rationale':lambda x,y:y['decisions']['loci']['L2-0001'].update(rationale='incorrect'),
    'altered_W_decision':lambda x,y:y['decisions']['W']['W-C02-001'].update(source_units=[]),
}
results=[]
for name,mutate in cases.items():
    x=copy.deepcopy(m); y=copy.deepcopy(app); mutate(x,y)
    try: check_data(x,y,*inputs)
    except (ValueError,KeyError) as error:
        results.append({'case':name,'rejected':True,'reason':str(error)})
    else: raise RuntimeError('Validator accepted corrupted fixture: '+name)
print(json.dumps({'positive_case_passed':True,'negative_cases_rejected':len(results),
    'cases':results,'editorial_files_modified':False},ensure_ascii=False,indent=2))
