"""Independent preview-preservation tests; cannot certify a final release."""
from pathlib import Path
import argparse, copy, hashlib, json, re, subprocess, sys
sys.dont_write_bytecode=True
from inventory import load, require, digest

def validate(root,m):
    base=root/'diplomatic'; c6=base/'chapter-06-v1'
    original=load(root/'translations/2026-09-26-full-draft/data/source-units.json')
    require(m['status']=='whole_work_preview_not_released','Preview misrepresented as final')
    require(m['original_units']==original,'Original source changed')
    seq=m['reading_sequence']; ids=[s['id'] for s in seq]
    require(len(ids)==len(set(ids)),'Duplicated sequence item')
    require([i for i in ids if re.fullmatch(r'U\d{5}',i)]==[u['id'] for u in original],'Original anchors missing or reordered')
    expected=[]; count_restored=0
    for n in range(1,6):
        folder=base/('release-v1' if n==1 else f'chapter-{n:02d}-v1/release')
        old=load(folder/'reading.json'); current=[s for s in seq if s['chapter']==n]
        stripped=[{k:v for k,v in s.items() if k not in ['chapter','source_record']} for s in current]
        require(stripped==old['reading_sequence'],'Released chapter sequence changed')
        layer=next(x for x in m['source_annotation_layers'] if x['chapter']==n)
        require(layer['annotations']==old.get('source_annotations',[]),'Released source notes changed')
        extra=next(x for x in m['additional_preserved_metadata'] if x['chapter']==n)
        require(extra['transition_graphic']==old.get('transition_graphic'),'Boundary metadata lost')
        ins=old['insertions'] if n==1 else (old.get('scan_insertions',[]))
        count_restored+=sum(len(i['tibetan_lines']) for i in ins if i['kind']=='main_text_restoration')
        expected.extend(current)
    d=load(c6/'DECISIONS.json'); p=load(c6/'PLAN.json'); ins=load(c6/'INSERTIONS.json')
    ints=load(c6/'INTERVENTIONS.json'); replacements={}; flags={}
    for rec in ints:
        replacements.update(rec['replacement_units'])
        for uid in rec.get('uncertain_units',[]): flags.setdefault(uid,[]).append(rec['id'])
    for uid,dec in d['closing_units'].items():
        if dec['status']=='retain_with_explicit_uncertainty': flags.setdefault(uid,[]).append('closing:'+uid)
    for u in load(c6/'source-units.json'):
        s=next(x for x in seq if x['id']==u['id']); uid=u['id']
        require(s['chapter']==6 and s['text']==replacements.get(uid,u['tibetan']),'Chapter6 selected text changed')
        require(s['uncertainty_refs']==flags.get(uid,[]),'Uncertainty hidden or inflated')
        role='source_heading' if s['text'].lstrip().startswith('ཞུས་ལན་') else 'main_text'
        if uid in {'U05447','U05448'}: role='chapter_colophon'
        if uid in d['closing_units']: role=d['closing_units'][uid]['role']
        require(s['role']==role,'Closing/source role changed'); expected.append(s)
        for i in sorted([x for x in ins if x['after_unit']==uid],key=lambda x:x['anchor_sequence']):
            t=next(x for x in seq if x['id']==i['id'])
            require(t['role']=='restored_main_text' and t['text']=='\n'.join(i['tibetan_lines']),'Restored verse changed')
            require(t['lines']==i['tibetan_lines'] and t['punctuation_policy']==i['punctuation_policy'],'Restoration policy lost')
            require(ids.index(uid)<ids.index(t['id'])<ids.index(i['before_unit']),'Restoration misplaced')
            expected.append(t); count_restored+=len(i['tibetan_lines'])
    require(seq==expected,'Extra, misplaced or missing sequence item')
    require(count_restored==m['counts']['restored_main_verses']==23,'Wrong restoration count')
    require(m['chapter6_pending']=={'transcript_loci':len(p['frozen_locus_ids'])-len(d['loci']),
        'W_blocks':len(p['frozen_W_ids'])-len(d['W']),'final_signoff':not bool(d['final_signoff'])},'Unfinished gate hidden')
    require(not m['full_base_scan_proofread'] and not m['exhaustive_witness_collation'],'False coverage')
    require(len(seq)==5484 and len(original)==5466,'Incorrect assembly counts')
    return {'original_anchors':len(original),'sequence_objects':len(seq),'restored_main_verses':count_restored,'closing_anchors':len(d['closing_units'])}
