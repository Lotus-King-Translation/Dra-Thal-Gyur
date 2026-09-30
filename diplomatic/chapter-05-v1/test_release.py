"""Negative tests on in-memory copies only; never mutate editorial originals."""
from pathlib import Path
import argparse, copy, json, sys
sys.dont_write_bytecode=True
from validate_release import validate_data
ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo',required=True,type=Path)
a=ap.parse_args(); root=a.repo.resolve(); c=root/'diplomatic/chapter-05-v1'
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
m=load(c/'release/reading.json'); app=load(c/'release/apparatus.json')
base=[load(c/name) for name in ['source-units.json','INTERVENTIONS.json','INSERTIONS.json',
    'DECISIONS.json','collation.json','wikisource.json','SOURCE-REVIEW.json']]
validate_data(m,app,*base)
def seg(x,ident): return next(s for s in x['reading_sequence'] if s['id']==ident)
def anc(x,ident): return next(s for s in x['anchors'] if s['id']==ident)
cases={
 'lost_original_anchor':lambda x,y,z:x['anchors'].pop(),
 'altered_original_source':lambda x,y,z:x['original_units'][0].update(tibetan='incorrect'),
 'changed_selected_word':lambda x,y,z:anc(x,'U05094').update(selected_tibetan='incorrect'),
 'root_moved_to_heading':lambda x,y,z:anc(x,'U05094').update(role='source_heading'),
 'lost_source_note':lambda x,y,z:x['source_annotations'].pop(),
 'duplicated_source_note':lambda x,y,z:x['source_annotations'].append(x['source_annotations'][0]),
 'changed_source_note':lambda x,y,z:x['source_annotations'][0].update(text='incorrect'),
 'lost_restoration':lambda x,y,z:x['reading_sequence'].remove(seg(x,'A2000-C05-S01')),
 'changed_restored_word':lambda x,y,z:seg(x,'A2000-C05-S01').update(text='incorrect'),
 'changed_restored_lines':lambda x,y,z:seg(x,'A2000-C05-S01')['lines'].pop(),
 'restoration_moved_to_note':lambda x,y,z:seg(x,'A2000-C05-S01').update(role='source_annotation'),
 'duplicated_restoration':lambda x,y,z:x['reading_sequence'].append(copy.deepcopy(seg(x,'A2000-C05-S01'))),
 'restoration_reordered':lambda x,y,z:x['reading_sequence'].reverse(),
 'restoration_metadata_lost':lambda x,y,z:x['scan_insertions'].clear(),
 'invented_extra_segment':lambda x,y,z:x['reading_sequence'].append({'id':'invented','text':'invented'}),
 'invented_boundary_text':lambda x,y,z:seg(x,'C5-TRANSITION').update(text='invented'),
 'boundary_counted_as_root':lambda x,y,z:seg(x,'C5-TRANSITION').update(role='main_text'),
 'lost_uncertainty':lambda x,y,z:anc(x,'U04923')['uncertainty_refs'].clear(),
 'changed_combined_reading':lambda x,y,z:x.update(main_and_headings_tibetan='incorrect'),
 'false_full_proofread':lambda x,y,z:x.update(full_base_scan_proofread=True),
 'false_all_witnesses':lambda x,y,z:x.update(exhaustive_witness_collation=True),
 'changed_transcript_quote':lambda x,y,z:y['collation']['loci'][0]['readings'].update(A='incorrect'),
 'lost_W_record':lambda x,y,z:y['wikisource']['conflicts'].pop(),
 'lost_intervention':lambda x,y,z:y['interventions'].pop(),
 'wrong_release_choice':lambda x,y,z:z[3]['loci']['L5-0001']['release_reading'].update(U04793='incorrect'),
 'wrong_choice_anchor':lambda x,y,z:z[3]['loci']['L5-0001'].update(source_units=['U04794']),
 'invalid_choice_status':lambda x,y,z:z[3]['loci']['L5-0001'].update(status='invented'),
 'missing_restoration_link':lambda x,y,z:z[3]['loci']['L5-0019'].update(insertion_ids=[]),
 'summary_notice_moved_to_root':lambda x,y,z:anc(x,'U04951').update(role='main_text'),
 'changed_summary_notice':lambda x,y,z:anc(x,'U04951').update(selected_tibetan='incorrect'),
 'lost_W_restoration_link':lambda x,y,z:z[3]['W']['W-C05-031'].update(insertion_ids=[]),
 'wrong_W_line':lambda x,y,z:z[3]['W']['W-C05-001'].update(W_lines=[1])}
results=[]
for name,mutate in cases.items():
    x=copy.deepcopy(m); y=copy.deepcopy(app); z=copy.deepcopy(base); mutate(x,y,z)
    try: validate_data(x,y,*z)
    except (ValueError,KeyError) as error:
        results.append({'case':name,'rejected':True,'reason':str(error)})
    else: raise RuntimeError('Corruption accepted: '+name)
print(json.dumps({'positive_case_passed':True,'negative_cases_rejected':len(results),
    'cases':results,'editorial_originals_modified':False},indent=2))
