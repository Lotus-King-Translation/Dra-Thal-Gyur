"""Build explicit review records from fixed inputs and the authored English decisions."""
from pathlib import Path
import collections, hashlib, json, re, sys
sys.dont_write_bytecode = True
from authored import REVISIONS, SPECIAL, LAYER_MAIN, EXTRA, ANNOTATION_EN, UNCERTAINTY, USAGES
ROOT = Path(__file__).resolve().parents[3]
B = ROOT/'translations/2026-09-26-full-draft'
R = B/'golden-review'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def source_brackets(text):
    result=[]; removed=[]; i=0
    while i<len(text):
        if text.startswith('[Source',i) or text.startswith('[Small-print source',i):
            start=i; depth=0
            while i<len(text):
                if text[i]=='[': depth+=1
                elif text[i]==']':
                    depth-=1
                    if depth==0: i+=1; break
                i+=1
            if depth: raise ValueError('Unbalanced source note: '+text)
            removed.append(text[start:i])
        else: result.append(text[i]); i+=1
    cleaned=re.sub(r' +',' ',''.join(result)).strip()
    cleaned=re.sub(r'\s+([,.;:])',r'\1',cleaned)
    return cleaned,removed
def prepare():
    for path,h in load(R/'INPUTS.json')['input_hashes'].items():
        assert sha(ROOT/path)==h, 'Protected input changed: '+path
    audit=load(R/'AUDIT.json'); golden=load(ROOT/'diplomatic/root-tantra-v1/release/reading.json')
    english={r['id']:r for r in (json.loads(l) for l in (B/'ALIGNED.jsonl').read_text().splitlines() if l.strip())}
    units={u['id']:u for u in golden['original_units']}; seq={s['id']:s for s in golden['reading_sequence']}
    assert len(units)==len(english)==5466
    actual={i for i,u in units.items() if seq[i]['text']!=u['tibetan']}
    assert actual=={r['id'] for r in audit['records']} and len(actual)==110
    assert set(EXTRA)=={x['id'] for x in audit['extra_objects']} and len(EXTRA)==18
    annotations=[]; ann_by_unit=collections.defaultdict(list)
    for layer in golden['source_annotation_layers']:
        for source in layer['annotations']:
            aid=source.get('id',source.get('record_id'))
            assert aid in ANNOTATION_EN, aid
            owners=[u for u in source['units'] if u in actual]
            assert owners, aid
            row={'id':aid,'chapter':layer['chapter'],'golden_record':source,'english':ANNOTATION_EN[aid],
                 'endnote_owner':'G-'+owners[0],'translation_status':'source-note rendering; source qualifications retained'}
            annotations.append(row)
            for u in source['units']: ann_by_unit[u].append(aid)
    assert len(annotations)==65 and {a['id'] for a in annotations}==set(ANNOTATION_EN)
    decisions=[]
    for r in audit['records']:
        uid=r['id']; old=english[uid]['english']; assert old==r['english_current']
        classification='word-division-correction' if uid in ['U01598','U03851'] else r['classification']
        cleaned,moved=(old,[]) if r['golden_role']=='source_heading' else source_brackets(old)
        selected=LAYER_MAIN.get(uid,cleaned); confidence='High for documented source difference; not a general translation score'
        if uid in REVISIONS: selected,reason,confidence=REVISIONS[uid]
        elif classification=='punctuation-spacing': reason='The difference is a boundary delimiter or spacing change. Retain the existing English; record both exact Tibetan strings so the change is not hidden.'
        elif uid in SPECIAL: reason=SPECIAL[uid]
        elif r['golden_role']=='source_annotation_anchor': reason='The golden edition classifies this as a source annotation, not a root verse. Preserve the old English and the separate source-note rendering in endnotes, rather than inside the root translation.'
        elif r['golden_role']=='joined_anchor': reason='The golden edition joins this fragment into the preceding main anchor. Preserve the original fragment and former English in the endnote; do not duplicate the joined main text.'
        elif ann_by_unit[uid]: reason='The golden main clause excludes a smaller source annotation. The existing English already distinguishes its main reading; move the annotation into the endnote and retain its exact source wording and source qualifications.'
        else: reason='The golden edition corrects the supplied Tibetan transcription or heading wording. The existing English already expresses the selected reading; retain it and document the exact textual difference.'
        if r['golden_role'] in ['source_annotation_anchor','joined_anchor']: selected=''
        if uid in SPECIAL and uid in REVISIONS: reason+=' '+SPECIAL[uid]
        action='non_main_or_joined_anchor' if selected=='' else 'semantic_or_context_revision' if uid in REVISIONS else 'source_note_relocated' if selected!=old else 'retain_english_and_annotate'
        decisions.append({**r,'classification':classification,'note_id':'G-'+uid,'english_selected':selected,
            'action':action,'reason':reason,'confidence':confidence,'removed_inline_notes':moved,
            'annotation_ids':ann_by_unit[uid],'review_status':'reviewed_for_golden_source_reconciliation'})
    extras=[]
    for x in audit['extra_objects']:
        en,reason,confidence=EXTRA[x['id']]
        extras.append({**x,'note_id':'G-'+x['id'],'english_selected':en,'reason':reason,'confidence':confidence,
                       'review_status':'reviewed; unresolved components remain explicit'})
    supplemental=[]
    for uid in load(R/'PLAN.json')['uncertainty_only_ids']:
        assert uid in UNCERTAINTY,uid
        supplemental.append({'id':uid,'note_id':'G-'+uid,'chapter':seq[uid]['chapter'],'kind':'inherited_golden_uncertainty',
          'adzom_tibetan':units[uid]['tibetan'],'golden_tibetan':seq[uid]['text'],'english_current':english[uid]['english'],
          'english_selected':english[uid]['english'],'reason':UNCERTAINTY[uid],'golden_uncertainty_refs':seq[uid]['uncertainty_refs'],
          'confidence':'Unresolved component retained, not deciphered'})
    for uid in load(R/'PLAN.json')['adjacent_context_ids']:
        en,reason,confidence=REVISIONS[uid]
        supplemental.append({'id':uid,'note_id':'G-'+uid,'chapter':seq[uid]['chapter'],'kind':'restoration_context_revision',
          'adzom_tibetan':units[uid]['tibetan'],'golden_tibetan':seq[uid]['text'],'english_current':english[uid]['english'],
          'english_selected':en,'reason':reason,'confidence':confidence,'golden_uncertainty_refs':seq[uid].get('uncertainty_refs',[])})
    graphic=next(x['transition_graphic'] for x in golden['additional_preserved_metadata'] if x['chapter']==2)
    supplemental.append({'id':'C2-BOUNDARY-METADATA','note_id':'G-C2-BOUNDARY-METADATA','chapter':2,
       'kind':'non_main_graphic_metadata','attach_to':'U03622','golden_metadata':graphic,
       'reason':'The golden Chapter 2 metadata preserves a compact boundary graphic with no decoded reading. Retain it in an endnote, not as an invented seventh line or a new main-text object.',
       'confidence':'Unresolved source graphic; no invented wording'})
    result={'schema_version':1,'golden_release':'root-tantra-v1.0.0','translation_baseline':load(R/'INPUTS.json')['baseline_commit'],
        'anchor_decisions':decisions,'extra_decisions':extras,'supplemental_notes':supplemental,
        'source_annotation_components':annotations,'provisional_usages':USAGES,
        'scope':load(R/'PLAN.json')['scope'],'independent_human_qc':False,'new_scan_reading':False}
    notes=decisions+extras+supplemental
    assert len(notes)==len({n['note_id'] for n in notes})==173
    result['counts']={'original_anchors_compared':5466,'changed_anchors_reviewed':len(decisions),
       'extra_objects_reviewed':len(extras),'restored_main_verses':23,'uncertainty_only_notes':42,
       'adjacent_context_revisions':2,'boundary_metadata_notes':1,'source_annotations_accounted':65,
       'distinct_new_endnotes':len(notes),'classification_counts':dict(collections.Counter(r['classification'] for r in decisions)),
       'action_counts':dict(collections.Counter(r['action'] for r in decisions))}
    save(R/'DECISIONS.json',result)
    save(R/'PROGRESS.json',{'state':'editorial_records_complete_rendering_pending','counts':result['counts'],
         'remaining_changed_anchor_reviews':0,'remaining_extra_object_reviews':0,'remaining_uncertainty_carryovers':0,
         'endnotes_rendered':False,'translation_rendered':False,'validation_passed':False,'publication_verified':False})
    print(json.dumps(result['counts'],indent=2))
if __name__=='__main__': prepare()
