"""Mutation tests on in-memory copies only; never modify editorial source files."""
from pathlib import Path
import argparse, copy, json, sys
sys.dont_write_bytecode=True
from validate_release import validate_data
ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo',required=True,type=Path)
a=ap.parse_args(); root=a.repo.resolve(); d=root/'diplomatic/release-v1'; c=root/'diplomatic/collation/chapter-01'
load=lambda p:json.loads(p.read_text())
m=load(d/'reading.json'); app=load(d/'apparatus.json')
args=[load(c/'reading-units.json'),load(c/'ch1-scan-insertions.json'),load(c/'chapter1-loci.json'),
      load(c/'chapter1-conflicts.json'),load(root/'diplomatic/release-v1-proposal/DECISIONS.json'),load(c/'scan-comparison-loci.json')]
validate_data(m,app,*args)
def segment(x,ident): return next(s for s in x['reading_sequence'] if s['id']==ident)
cases={
 'lost_original_anchor':lambda x,y:x['source_anchors'].pop(),
 'invented_sequence_segment':lambda x,y:x['reading_sequence'].append({'id':'invented','text':'invented','role':'main_text'}),
 'lost_restoration':lambda x,y:x['reading_sequence'].remove(segment(x,'A2000-C01-S01')),
 'changed_restored_word':lambda x,y:segment(x,'A2000-C01-S02').update(text='incorrect'),
 'caption_moved_into_main':lambda x,y:segment(x,'A2000-C01-S08').update(role='main_text'),
 'annotation_moved_into_main':lambda x,y:segment(x,'U01286').update(text='incorrect',role='main_text'),
 'duplicate_joined_text':lambda x,y:segment(x,'U01812').update(text='duplicate'),
 'root_misclassified_as_caption':lambda x,y:segment(x,'U00542').update(role='provisional_caption'),
 'altered_transcript_quotation':lambda x,y:y['electronic_loci'][0]['readings'].update(A='incorrect'),
 'lost_comparison_observation':lambda x,y:y['comparison_scan_observations'].pop(),
 'invented_inscription_reading':lambda x,y:segment(x,'A2000-C01-S09').update(text='invented')}
results=[]
for name,mutate in cases.items():
    x=copy.deepcopy(m); y=copy.deepcopy(app); mutate(x,y)
    try: validate_data(x,y,*args)
    except (ValueError,KeyError) as err: results.append({'case':name,'rejected':True,'reason':str(err)})
    else: raise RuntimeError('Validator accepted mutation: '+name)
print(json.dumps({'positive_case_passed':True,'negative_cases_rejected':len(results),'cases':results,'editorial_files_modified':False},indent=2))
