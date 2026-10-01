"""Adversarial in-memory preservation tests; never modifies editorial inputs."""
import copy, json, sys
sys.dont_write_bytecode=True
from validate_translation import ROOT,B,R,OUT,load,validate_data,footnote_check
m=load(OUT/'edition.json'); g=load(ROOT/'diplomatic/root-tantra-v1/release/reading.json')
d=load(R/'DECISIONS.json'); plan=load(R/'PLAN.json')
e={r['id']:r for r in (json.loads(l) for l in (B/'ALIGNED.jsonl').read_text().splitlines() if l.strip())}
validate_data(m,g,e,d,plan)
def row(x,uid): return next(r for r in x['reading_sequence'] if r['id']==uid)
cases={
'lost_original_anchor':lambda x:x['reading_sequence'].pop(0),
'duplicate_original_anchor':lambda x:x['reading_sequence'].append(copy.deepcopy(x['reading_sequence'][0])),
'reordered_sequence':lambda x:x['reading_sequence'].reverse(),
'changed_golden_Tibetan':lambda x:row(x,'U00187').update(golden_tibetan='wrong'),
'changed_golden_role':lambda x:row(x,'U00317').update(golden_role='main_text'),
'changed_original_English':lambda x:row(x,'U00187').update(original_english='wrong'),
'changed_original_Tibetan':lambda x:row(x,'U00187').update(original_tibetan='wrong'),
'changed_reviewed_English':lambda x:row(x,'U00187').update(english='wrong'),
'changed_inherited_English':lambda x:row(x,'U00040').update(english='wrong'),
'lost_provenance':lambda x:row(x,'U00187').update(legacy_english_provenance=[]),
'lost_legacy_note':lambda x:row(x,'U00187').update(legacy_note_ids=[]),
'lost_uncertainty':lambda x:row(x,'U05411').update(golden_uncertainty_refs=[]),
'lost_uncertainty_endnote':lambda x:row(x,'U05411').update(endnote_ids=[]),
'wrong_note_location':lambda x:row(x,'U00187').update(endnote_ids=['G-U00039']),
'lost_extra_object':lambda x:x['reading_sequence'].remove(row(x,'A2000-C06-S01')),
'lost_restored_English_line':lambda x:row(x,'A2000-C06-S01').update(english=row(x,'A2000-C06-S01')['english'].splitlines()[0]),
'annotation_returned_to_root':lambda x:row(x,'U00317').update(english='source annotation disguised as root'),
'joined_fragment_duplicated':lambda x:row(x,'U01812').update(english='three hundred thousand'),
'lost_source_annotation':lambda x:x['source_annotations'].pop(),
'changed_source_annotation':lambda x:x['source_annotations'][0].update(english='invented note'),
'changed_annotation_source_record':lambda x:x['source_annotations'][0]['golden_record'].update(annotation='wrong'),
'changed_annotation_owner':lambda x:x['source_annotations'][0].update(endnote_owner='G-U00039'),
'lost_endnote':lambda x:x['endnotes'].pop(),
'changed_endnote_quotation':lambda x:x['endnotes'][0].update(english_current='wrong'),
'duplicate_endnote':lambda x:x['endnotes'].append(copy.deepcopy(x['endnotes'][0])),
'lost_boundary_metadata':lambda x:x.update(additional_golden_metadata=[]),
'closing_as_root_chapter':lambda x:row(x,'U05449').update(part=6),
'lost_closing_anchor':lambda x:x['reading_sequence'].remove(row(x,'U05466')),
'false_human_QC':lambda x:x.update(independent_human_qc=True),
'false_unchanged_semantic_QC':lambda x:x.update(unchanged_passages_fresh_semantic_qc=True),
'wrong_golden_version':lambda x:x.update(golden_release='invented-release'),
'changed_provisional_usage':lambda x:x.update(provisional_usages=[])
}
results=[]
for name,fn in cases.items():
    broken=copy.deepcopy(m); fn(broken)
    try: validate_data(broken,g,e,d,plan)
    except ValueError as exc: results.append({'case':name,'rejected':True,'reason':str(exc)})
    else: raise RuntimeError('Corruption accepted: '+name)
valid='Passage[^G-U00187]\n\n[^G-U00187]: Note.\n'
footnote_check(valid,{'G-U00187'})
for name,text in {'undefined_footnote':'Passage[^G-U00187]','orphan_footnote':'[^G-U00187]: Note.','duplicate_footnote':valid+'[^G-U00187]: Duplicate.','wrong_footnote_reference':valid.replace('Passage[^G-U00187]','Passage[^G-U99999]')}.items():
    try: footnote_check(text,{'G-U00187'})
    except ValueError as exc: results.append({'case':name,'rejected':True,'reason':str(exc)})
    else: raise RuntimeError('Footnote corruption accepted: '+name)
print(json.dumps({'positive_case_passed':True,'negative_cases_rejected':len(results),'cases':results,'editorial_inputs_modified':False},indent=2))
