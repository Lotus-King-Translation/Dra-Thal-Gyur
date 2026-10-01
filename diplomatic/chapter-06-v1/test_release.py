#!/usr/bin/env python3
"""Negative in-memory release tests; editorial originals are never mutated."""
from pathlib import Path
import argparse, copy, json, sys
sys.dont_write_bytecode=True
from validate_release import validate_data
ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True,type=Path)
a=ap.parse_args(); c=a.repo.resolve()/'diplomatic/chapter-06-v1'
load=lambda n:json.loads((c/n).read_text())
m=load('release/reading.json'); app=load('release/apparatus.json')
base=[load(n) for n in ['source-units.json','INTERVENTIONS.json','INSERTIONS.json','DECISIONS.json','collation.json','wikisource.json','SOURCE-REVIEW.json']]
validate_data(m,app,*base)
def anc(x,i): return next(a for a in x['anchors'] if a['id']==i)
def seg(x,i): return next(a for a in x['reading_sequence'] if a['id']==i)
cases={
'lost_anchor':lambda x,y,z:x['anchors'].pop(),
'changed_source_unit':lambda x,y,z:x['original_units'][0].update(tibetan='bad'),
'changed_selected':lambda x,y,z:anc(x,'U05411').update(selected_tibetan='bad'),
'changed_role':lambda x,y,z:anc(x,'U05452').update(role='main_text'),
'lost_uncertainty':lambda x,y,z:anc(x,'U05411')['uncertainty_refs'].clear(),
'lost_intervention_link':lambda x,y,z:anc(x,'U05411')['intervention_ids'].clear(),
'lost_locus_link':lambda x,y,z:anc(x,'U05248')['locus_ids'].clear(),
'lost_W_link':lambda x,y,z:anc(x,'U05460')['W_ids'].clear(),
'invented_annotation':lambda x,y,z:x['source_annotations'].append({'bad':1}),
'lost_restoration':lambda x,y,z:x['reading_sequence'].remove(seg(x,'A2000-C06-S01')),
'changed_restoration':lambda x,y,z:seg(x,'A2000-C06-S01').update(text='bad'),
'reordered_sequence':lambda x,y,z:x['reading_sequence'].reverse(),
'lost_insertion_metadata':lambda x,y,z:x['scan_insertions'].clear(),
'changed_combined':lambda x,y,z:x.update(main_and_closing_tibetan='bad'),
'false_full_proofread':lambda x,y,z:x.update(full_base_scan_proofread=True),
'false_exhaustive':lambda x,y,z:x.update(exhaustive_witness_collation=True),
'lost_locus_decision':lambda x,y,z:z[3]['loci'].pop('L6-0001'),
'wrong_locus_reading':lambda x,y,z:z[3]['loci']['L6-0001']['release_reading'].update(U05225='bad'),
'lost_W_decision':lambda x,y,z:z[3]['W'].pop('W-C06-001'),
'wrong_W_line':lambda x,y,z:z[3]['W']['W-C06-001'].update(W_lines=[1]),
'missing_ABS_restoration_link':lambda x,y,z:z[3]['loci']['L6-0011'].update(insertion_ids=[]),
'missing_W_restoration_link':lambda x,y,z:z[3]['W']['W-C06-021'].update(insertion_ids=[]),
'lost_closing_unit':lambda x,y,z:z[3]['closing_units'].pop('U05466'),
'changed_closing_selected':lambda x,y,z:z[3]['closing_units']['U05459'].update(selected_tibetan='bad'),
'changed_closing_role':lambda x,y,z:z[3]['closing_units']['U05452'].update(role='main_text'),
'lost_intervention':lambda x,y,z:z[1].pop(),
}
out=[]
for name,fn in cases.items():
    x=copy.deepcopy(m); y=copy.deepcopy(app); z=copy.deepcopy(base); fn(x,y,z)
    try: validate_data(x,y,*z)
    except (ValueError,KeyError,AssertionError) as e: out.append({'case':name,'rejected':True,'reason':str(e)})
    else: raise RuntimeError('Corruption accepted: '+name)
print(json.dumps({'positive_case_passed':True,'negative_cases_rejected':len(out),'cases':out,'editorial_originals_modified':False},indent=2))
