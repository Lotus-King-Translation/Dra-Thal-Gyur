"""Assemble saved readings only; never fill pending editorial decisions."""
from pathlib import Path
import argparse, collections, hashlib, json, os, re, sys
sys.dont_write_bytecode=True
from inventory import audit, require, load, digest

def js(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def make(root):
    base=root/'diplomatic'; out=base/'root-tantra-v1/preview'; c6=base/'chapter-06-v1'
    original=load(root/'translations/2026-09-26-full-draft/data/source-units.json')
    inv=audit(root); sequences=[]; notes=[]; sources=[]; extras=[]; hashes={}
    for n in range(1,6):
        folder=base/('release-v1' if n==1 else f'chapter-{n:02d}-v1/release')
        path=folder/'reading.json'; m=load(path)
        seq=json.loads(json.dumps(m['reading_sequence']))
        for s in seq: s['chapter']=n; s['source_record']=str(path.relative_to(root))
        sequences.extend(seq)
        notes.append({'chapter':n,'source_record':str(path.relative_to(root)),
                      'annotations':m.get('source_annotations',[])})
        extras.append({'chapter':n,'transition_graphic':m.get('transition_graphic'),
                       'source_sequence_semantics':m.get('sequence_semantics')})
        sources.append({'chapter':n,'release_tag':f'chapter-{n:02d}-v1.0.0',
                        'reading':str((folder/'reading.md').relative_to(root)),
                        'apparatus':str((folder/'apparatus.md').relative_to(root)),
                        'coverage':str((folder/'COVERAGE.md').relative_to(root))})
        hashes[str(path.relative_to(root))]=digest(path)
    u6=load(c6/'source-units.json'); decisions=load(c6/'DECISIONS.json')
    interventions=load(c6/'INTERVENTIONS.json'); insertions=load(c6/'INSERTIONS.json')
    replacements={}; flags=collections.defaultdict(list)
    for rec in interventions:
        for uid,text in rec['replacement_units'].items():
            require(uid not in replacements,'Overlapping changes'); replacements[uid]=text
        for uid in rec.get('uncertain_units',[]): flags[uid].append(rec['id'])
    for uid,dec in decisions['closing_units'].items():
        if dec['status']=='retain_with_explicit_uncertainty': flags[uid].append('closing:'+uid)
    for u in u6:
        uid=u['id']; text=replacements.get(uid,u['tibetan'])
        role='source_heading' if text.lstrip().startswith('ཞུས་ལན་') else 'main_text'
        if uid in {'U05447','U05448'}: role='chapter_colophon'
        if uid in decisions['closing_units']: role=decisions['closing_units'][uid]['role']
        sequences.append({'id':uid,'anchor_id':uid,'role':role,'text':text,
            'uncertainty_refs':flags[uid],'chapter':6,'source_record':str((c6/'source-units.json').relative_to(root)),
            'editorial_state':'saved_working_reading_not_final_release'})
        for item in sorted([i for i in insertions if i['after_unit']==uid],key=lambda i:i['anchor_sequence']):
            sequences.append({'id':item['id'],'anchor_id':uid,'role':'restored_main_text',
                'text':'\n'.join(item['tibetan_lines']),'lines':item['tibetan_lines'],'chapter':6,
                'uncertainty_refs':[],'punctuation_policy':item['punctuation_policy'],
                'source_record':str((c6/'INSERTIONS.json').relative_to(root)),
                'editorial_state':'saved_restoration_not_final_release'})
    sources.append({'chapter':6,'release_tag':None,'source_review':str((c6/'SOURCE-REVIEW.json').relative_to(root)),
        'decisions':str((c6/'DECISIONS.json').relative_to(root)),
        'exact_collation':str((c6/'collation.json').relative_to(root)),
        'stored_W_comparison':str((c6/'wikisource.json').relative_to(root))})
    ids=[s['id'] for s in sequences]; require(len(ids)==len(set(ids)),'Duplicated sequence identifier')
    require([i for i in ids if re.fullmatch(r'U\d{5}',i)]==[u['id'] for u in original],'Original anchor order or coverage')
    for i in insertions:
        require(ids.index(i['after_unit'])<ids.index(i['id'])<ids.index(i['before_unit']),'Restoration flanks')
    for n in ['PLAN.json','source-units.json','DECISIONS.json','INTERVENTIONS.json','INSERTIONS.json','SOURCE-REVIEW.json']:
        hashes[str((c6/n).relative_to(root))]=digest(c6/n)
    pending={'transcript_loci':len(load(c6/'PLAN.json')['frozen_locus_ids'])-len(decisions['loci']),
             'W_blocks':len(load(c6/'PLAN.json')['frozen_W_ids'])-len(decisions['W']),
             'final_signoff':not bool(decisions['final_signoff'])}
    original_byid={u['id']:u for u in original}
    changed=[{'id':s['id'],'chapter':s['chapter'],'original':original_byid[s['id']]['tibetan'],
              'selected':s['text']} for s in sequences if s['id'] in original_byid
             and s['text']!=original_byid[s['id']]['tibetan']]
    counts={'original_anchors':len(original),'sequence_objects':len(sequences),
            'restored_main_verses':inv['restored_main_verses'],'closing_anchors':18,
            'changed_original_anchor_strings':len(changed),
            'uncertainty_bearing_objects':sum(bool(s.get('uncertainty_refs')) for s in sequences)}
    machine={'schema_version':1,'status':'whole_work_preview_not_released',
        'original_units':original,'reading_sequence':sequences,'source_annotation_layers':notes,
        'additional_preserved_metadata':extras,'parts':sources,'counts':counts,'chapter6_pending':pending,
        'original_transcript_accounting':inv['source_spans'],'input_hashes':hashes,
        'full_base_scan_proofread':False,'exhaustive_witness_collation':False,
        'scope':'All saved root-text parts assembled, but Chapter6 editorial decisions and versioned publication remain pending.'}
    def link(path,label): return '['+label+']('+os.path.relpath(root/path,out).replace(os.sep,'/')+')'
    md=['# Dra Thal Gyur — whole-text reading preview','',
        '**NOT A FINAL RELEASE.** Chapters 1–5 are fixed released editions; Chapter 6 and closing material are saved working readings. '+str(pending['transcript_loci'])+' passage decisions and '+str(pending['W_blocks'])+' reference decisions remain open.','',
        'All 5,466 original anchors are represented, with 23 scan-restored main verses. Root text, headings, source notes, captions, ritual formulas and unresolved signs retain their distinctions.','',
        'Editorial line breaks and whitespace display are not facsimile physical lineation. Uncertainty flags preserve the chapter records and are not a measured error rate.','',
        '[Inventory](../INVENTORY.json) · [Machine reading](reading.json) · [Uncertainties](UNCERTAINTIES.md) · [Annotations](annotations.json) · [Change index](changes.json)','']
    um=['# Preserved uncertainty and remaining work','',
        'The flags below are copied from the chapter readings or saved Chapter 6 uncertainty records. They include source-layer and punctuation qualifications; they are not all unreadable words.','',
        '**Chapter 6 remains unfinished:** '+str(pending['transcript_loci'])+' passage decisions, '+str(pending['W_blocks'])+' reference decisions, final signoff, validation and versioned publication. No open decision has been filled automatically.','']
    current=None
    for s in sequences:
        n=s['chapter']
        if n!=current:
            current=n; md+=['## Chapter '+str(n),'']
            refs=sources[n-1]
            md += [' · '.join(link(v,k.replace('_',' ')) for k,v in refs.items() if k not in ['chapter','release_tag']),'']
        if s['id']=='U05449': md+=['## Full-work colophon and closing material','']
        md+=['<a id="'+s['id'].lower()+'"></a>','']
        text=s.get('text','').strip(); role=s['role']
        if role=='source_heading': md+=['### '+text,'']
        elif role=='restored_main_text': md+=['**Scan-restored main text**','',text,'']
        elif role in ['provisional_caption','unresolved_inscription','unresolved_source_graphic']:
            md+=['*'+role.replace('_',' ')+':* '+(text or '[No invented transcription supplied.]'),'']
        elif text: md+=[text,'']
        else: md+=['*Preserved '+role.replace('_',' ')+'; see the source apparatus.*','']
        if s.get('uncertainty_refs'):
            md+=['**[Uncertain: '+s['id']+'](UNCERTAINTIES.md#'+s['id'].lower()+')**','']
            um+=['<a id="'+s['id'].lower()+'"></a>','### '+s['id'],'',
                 'Chapter '+str(n)+'; '+', '.join(s['uncertainty_refs'])+'.','',
                 '[Reading](reading.md#'+s['id'].lower()+') · '+link(s['source_record'],'Source record'),'']
    outputs={'reading.json':js(machine),'reading.md':'\n'.join(md),'UNCERTAINTIES.md':'\n'.join(um),
             'annotations.json':js({'source_annotation_layers':notes,'additional_preserved_metadata':extras}),
             'changes.json':js({'status':'preview','anchor_changes':changed,'restorations':inv['restorations']})}
    combined='\n'.join(md)
    banner='**WORKING PREVIEW — NOT A FINAL RELEASE. Chapter 6 decisions and publication remain pending.**\n\n[Whole text](reading.md) · [Uncertainties](UNCERTAINTIES.md)\n\n'
    outputs['chapter-06.md']='# Chapter 6 and closing material\n\n'+banner+combined.split('## Chapter 6\n',1)[1]
    outputs['closing-material.md']='# Full-work colophon and closing material\n\n'+banner+combined.split('## Full-work colophon and closing material\n',1)[1]
    outputs['MANIFEST.json']=js({'schema_version':1,'status':'preview_not_release','counts':counts,
        'chapter6_pending':pending,'input_hashes':hashes,'builder_sha256':digest(Path(__file__)),
        'output_hashes':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in outputs.items()}})
    return outputs,counts

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo',required=True,type=Path)
    p.add_argument('--check',action='store_true'); a=p.parse_args(); root=a.repo.resolve()
    outputs,counts=make(root); folder=root/'diplomatic/root-tantra-v1/preview'
    if a.check:
        for name,text in outputs.items(): require((folder/name).read_bytes()==text.encode(),'Stale preview: '+name)
    else:
        folder.mkdir(exist_ok=True)
        for name,text in outputs.items(): (folder/name).write_text(text,encoding='utf-8')
    print(js({'reproducible':a.check,'status':'preview_not_release','counts':counts}))

if __name__=='__main__': main()
