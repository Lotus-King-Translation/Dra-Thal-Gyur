#!/usr/bin/env python3
"""Serialize Chapter 6 plus the full-work closing material without new editorial decisions."""
from pathlib import Path
import argparse, collections, hashlib, json, os

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def js(v): return json.dumps(v,ensure_ascii=False,indent=2)+'\n'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ph(v): return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def anchor(i): return '<a id="'+i.lower()+'"></a>'
def fence(v):
    if not isinstance(v,str): return '\n```json\n'+js(v).rstrip()+'\n```\n'
    return '\n```json\n'+json.dumps(v,ensure_ascii=False)+'\n```\n' if any(x!=x.rstrip(' \t') for x in v.split('\n')) else '\n```text\n'+v+'\n```\n'

def make(root):
    c=root/'diplomatic/chapter-06-v1'; dest=c/'release'
    p=load(c/'PLAN.json'); d=load(c/'DECISIONS.json'); state=load(c/'STATE.json')
    units=load(c/'source-units.json'); col=load(c/'collation.json'); w=load(c/'wikisource.json')
    ints=load(c/'INTERVENTIONS.json'); ins=load(c/'INSERTIONS.json'); review=load(c/'SOURCE-REVIEW.json')
    assert len(units)==p['original_anchor_count']==269
    assert set(d['loci'])==set(p['frozen_locus_ids'])
    assert set(d['W'])==set(p['frozen_W_ids'])
    assert set(d['source_checks'])=={x['id'] for x in p['source_check_targets']}
    assert len(d['closing_units'])==18
    for n,h in p['collation_hashes'].items(): assert sha(c/n)==h
    for s in p['sources'].values(): assert sha(root/s['path'])==s['full_sha256']
    assert sha(root/p['W']['path'])==p['W']['sha256']
    payload={k:v for k,v in d.items() if k!='final_signoff'}
    if state['status']=='released_bounded_v1':
        sig=d['final_signoff']; assert sig['scope']=='bounded_chapter_6_v1'
        assert sig['decision_payload_sha256']==ph(payload)
        for path,h in sig['input_hashes'].items(): assert sha(root/path)==h
    byid={u['id']:u for u in units}; flags=collections.defaultdict(list)
    byunit=collections.defaultdict(list); locusmap=collections.defaultdict(list); wmap=collections.defaultdict(list)
    for rec in ints:
        assert not rec['replacement_units']
        for uid,t in rec['original_units'].items(): assert byid[uid]['tibetan']==t
        for uid in rec['units']: byunit[uid].append(rec['id'])
        for uid in rec.get('uncertain_units',[]): flags[uid].append(rec['id'])
    for l in col['loci']:
        dec=d['loci'][l['id']]
        assert dec['source_units']==l['source_units']
        assert dec['release_reading']=={u:byid[u]['tibetan'] for u in l['source_units']}
        for uid in l['source_units']: locusmap[uid].append(l['id'])
        for uid in dec.get('uncertain_units',[]): flags[uid].append(l['id'])
    for b in w['conflicts']:
        for uid in b['source_units']: wmap[uid].append(b['id'])
    after=collections.defaultdict(list)
    for x in ins: after[x['after_unit']].append(x)
    anchors=[]; seq=[]
    for u in units:
        uid=u['id']; text=u['tibetan']
        if uid in d['closing_units']: role=d['closing_units'][uid]['role']
        elif uid in {'U05447','U05448'}: role='chapter_colophon'
        elif text.lstrip().startswith('ཞུས་ལན་'): role='source_heading'
        else: role='main_text'
        a={'id':uid,'source_tibetan':text,'selected_tibetan':text,'source_wylie':u['wylie'],'role':role,
           'uncertainty_refs':flags[uid],'intervention_ids':byunit[uid],'locus_ids':locusmap[uid],'W_ids':wmap[uid]}
        anchors.append(a)
        seq.append({'id':uid,'anchor_id':uid,'role':role,'text':text,'uncertainty_refs':flags[uid]})
        for x in sorted(after[uid],key=lambda q:q['anchor_sequence']):
            seq.append({'id':x['id'],'anchor_id':uid,'role':'restored_main_text','text':'\n'.join(x['tibetan_lines']),
                        'lines':x['tibetan_lines'],'uncertainty_refs':[],'punctuation_policy':x['punctuation_policy']})
    machine={'schema_version':1,'chapter':6,'release_state':state['status'],'original_units':units,'anchors':anchors,
      'reading_sequence':seq,'source_annotations':[],'scan_insertions':ins,
      'main_and_closing_tibetan':'\n'.join(x['text'] for x in seq if x['text']),
      'original_sources_preserved':True,'unicode_normalization':'none','full_base_scan_proofread':False,
      'exhaustive_witness_collation':False,'closing_material_included':True,
      'scope':'Corrected Adzom-based Chapter 6 plus full-work closing material; untargeted wording remains supplied Adzom.'}
    label='Released bounded v1' if state['status']=='released_bounded_v1' else 'Release candidate — final gate pending'
    reading=['# Chapter 6 and full-work closing material','', '**'+label+'**','',
      'All 269 original anchors U05198–U05466 are retained. Two scan-attested main verses are restored after U05382. The 18 closing anchors remain distinct from Chapter 6 root text.','',
      '[Apparatus](apparatus.md) · [W reference](wikisource.md) · [Changes](CHANGES.md) · [Coverage](COVERAGE.md) · [Machine edition](reading.json)','']
    for x in seq:
        reading += [anchor(x['id']),'']
        ref='[note](apparatus.md#'+x['id'].lower()+')'
        flag=' **[uncertain](COVERAGE.md#questions)**' if x['uncertainty_refs'] else ''
        if x['role']=='source_heading':
            reading += ['### '+x['text'].strip(),'',ref+flag,'']
        elif x['role']=='restored_main_text':
            reading += ['**Scan-restored main verses**','',x['text'],'',ref,'']
        elif x['role']=='chapter_colophon':
            reading += ['**'+x['text'].strip()+'** '+ref+flag,'']
        elif x['role'] not in {'main_text'}:
            reading += ['*'+x['text'].strip()+'* '+ref+flag,'']
        else:
            needed=byunit[x['id']] or locusmap[x['id']] or wmap[x['id']] or flag
            reading += [x['text'].strip()+(' '+ref if needed else '')+flag,'']
    def link(path,label=None):
        f,sep,frag=path.partition('#')
        return '['+(label or Path(f).name)+']('+os.path.relpath(root/f,dest).replace(os.sep,'/')+(sep+frag if sep else '')+')'
    def ev(paths): return ', '.join(link(x) for x in paths)
    app=['# Chapter 6 — comparative apparatus and closing record','', '**'+label+'**','',
      'A/B/S quote exact supplied transcripts. All 21 exact differences are represented in 13 readable loci. W is a related reference transcript, not an independent printing.','',
      '[Reading](reading.md) · [W reference](wikisource.md) · [Coverage](COVERAGE.md) · [Structured apparatus](apparatus.json)','', '## Source-supported uncertainties','']
    for rec in ints:
        app += [anchor(rec['id']),'### '+rec['id'],'','**Original:**'+fence(rec['original_units']),
                '**Reason:** '+rec['rationale'],'','**Limits:** '+rec['remaining_uncertainty'],'','**Evidence:** '+ev(rec['evidence']),'']
    app += ['## Restored main text','']
    for x in ins:
        app += [anchor(x['id']),'### '+x['id'],'','After '+x['after_unit']+'; before '+x['before_unit']+'.',
                fence('\n'.join(x['tibetan_lines'])),'**Reason:** '+x['rationale'],'','**Punctuation:** '+x['punctuation_policy'],
                '','**Limits:** '+x['remaining_uncertainty'],'','**Evidence:** '+ev(x['evidence']),'']
    app += ['## The 13 A/B/S release choices','']
    for l in col['loci']:
        dec=d['loci'][l['id']]
        app += [anchor(l['id']),'### '+l['id'],'','Anchors: '+', '.join(l['source_units'])+'.',
                'Exact differences: '+', '.join(l['exact_conflicts'])+'.','',
                '**Disposition:** '+dec['status'],'','**Reason:** '+dec['rationale'],'',
                '**Selected anchor strings:**'+fence(dec['release_reading'])]
        if dec.get('insertion_ids'): app += ['**Also include:** '+', '.join(dec['insertion_ids'])+'.','']
        for sig in ['A','B','S']: app += ['**'+sig+' '+str(l['full_source_offsets'][sig])+':**'+fence(l['readings'][sig])]
        app += ['**Evidence:** '+ev(dec['evidence']),'']
    app += ['## Full-work closing material','']
    for uid,dec in d['closing_units'].items():
        app += [anchor(uid),'### '+uid+' — '+dec['role'],'',dec['rationale'],'','**Exact selected text:**'+fence(dec['selected_tibetan']),
                '**Evidence:** '+ev(dec['evidence']),'']
    wm=['# Chapter 6 — related Wikisource reference comparison','', '**'+label+'**','',
        'All 28 non-equal alignment blocks have explicit decisions. Exact A Wylie and W lines are preserved; W does not override the governing Adzom scan.','']
    for b in w['conflicts']:
        dec=d['W'][b['id']]; loc=', '.join(b['source_units']) or 'between '+str(b['source_before'])+' and '+str(b['source_after'])
        wm += [anchor(b['id']),'## '+b['id']+' — '+loc,'','**A Tibetan:**'+fence(b['A_tibetan']),
               '**A Wylie:**'+fence(b['A_wylie']),'**W lines:**'+fence(b['W_lines']),
               '**Differences:**'+fence(b['token_differences']),'**Decision:** '+dec['rationale'],'']
    change=['# Chapter 6 — changes from the supplied Adzom e-text','',
       '**Two main verses are restored; no original anchor string is changed.**','',
       'The restoration follows U05382 and precedes U05383. Seven original anchors retain visible uncertainty without conjectural replacement. The 18 closing anchors are preserved and layered as closing material rather than treated as a seventh chapter.','']
    for x in ins: change += ['## '+x['id'],'',fence('\n'.join(x['tibetan_lines'])),'[Evidence](apparatus.md#'+x['id'].lower()+')','']
    cov=['# Chapter 6 v1 — coverage and retained uncertainty','', '**'+label+'**','',
      'Bounded scope: 269 original anchors, 21 A/B/S differences in 13 loci, 28 W reference blocks, 13 targeted Adzom source checks and 18 closing-material dispositions.','',
      'Two main verses after U05382 are restored from PDF202. The full closing through PDF205 is included. Untargeted wording remains the supplied Adzom transcript.','',
      anchor('questions'),'## Explicit reading qualifications','']
    for a in anchors:
        if a['uncertainty_refs']: cov += ['- ['+a['id']+'](reading.md#'+a['id'].lower()+'): '+', '.join(a['uncertainty_refs'])]
    cov += ['','## Deferred research, not a release prerequisite','',
      'This bounded v1 does not claim complete physical-sign transcription or exhaustive comparison of all acquired manuscript witnesses. W remains a related website reference; B and S remain supplied transcripts.','']
    readme=['# Chapter 6 and closing material — bounded v1','', '**'+label+'**','',p['title'],'',
      '| Deliverable | Contents |','|---|---|','| [Reading](reading.md) | Chapter 6 plus all closing material |',
      '| [Apparatus](apparatus.md) | Exact transcript quotations, source checks and closing dispositions |',
      '| [Machine edition](reading.json) | All 269 original anchors plus restorations and roles |',
      '| [Changes](CHANGES.md) | Restored material and unchanged-anchor policy |',
      '| [Coverage](COVERAGE.md) | Scope, uncertainty and deferred research |','',
      '[W reference](wikisource.md) · [Structured apparatus](apparatus.json)','',
      'This is a corrected Adzom-based bounded v1, not a complete scan proofread or reconstructed original.','']
    if state['status']=='released_bounded_v1': readme += ['Version: **chapter-06-v1.0.0**. [Final validation](VALIDATION.json) records the scoped checks.','']
    structured={'schema_version':1,'scope':p['scope'],'collation':col,'wikisource':w,'release_decisions':d,
                'interventions':ints,'insertions':ins,'source_review':review}
    outputs={'reading.md':'\n'.join(reading),'apparatus.md':'\n'.join(app),'wikisource.md':'\n'.join(wm),
             'reading.json':js(machine),'apparatus.json':js(structured),'CHANGES.md':'\n'.join(change),
             'COVERAGE.md':'\n'.join(cov),'README.md':'\n'.join(readme)}
    inputs=[c/n for n in ['PLAN.json','DECISIONS.json','source-units.json','collation.json','wikisource.json','INTERVENTIONS.json','INSERTIONS.json','SOURCE-REVIEW.json','STATE.json','W-REVIEW.md']]
    inputs += [root/s['path'] for s in p['sources'].values()]+[root/p['W']['path'],root/'translations/2026-09-26-full-draft/data/source-units.json']
    inputs += sorted((c/'evidence').glob('E*/manifest.json'))
    if (c/'evidence/focused/manifest.json').exists(): inputs.append(c/'evidence/focused/manifest.json')
    if (c/'FINAL-REVIEW.md').exists(): inputs.append(c/'FINAL-REVIEW.md')
    counts={'source_anchors':269,'transcript_loci':13,'exact_differences':21,'W_blocks':28,'source_checks':13,
      'closing_anchors':18,'interventions':len(ints),'changed_anchor_strings':0,
      'source_annotations':0,'restored_main_verses':sum(len(x['tibetan_lines']) for x in ins),'reading_sequence_items':len(seq)}
    manifest={'schema_version':1,'chapter':6,'state':state['status'],'baseline_commit':p['baseline_commit'],
      'input_hashes':{str(x.relative_to(root)):sha(x) for x in inputs},'output_hashes':{n:hashlib.sha256(t.encode()).hexdigest() for n,t in outputs.items()},
      'generator_sha256':sha(Path(__file__)),'counts':counts,'full_base_scan_proofread':False,'exhaustive_witness_collation':False,
      'final_signoff_recorded':bool(d['final_signoff'])}
    outputs['MANIFEST.json']=js(manifest)
    return outputs,manifest

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True,type=Path); ap.add_argument('--check',action='store_true')
    a=ap.parse_args(); root=a.repo.resolve(); out,m=make(root); dest=root/'diplomatic/chapter-06-v1/release'
    if a.check:
        bad=[n for n,t in out.items() if not (dest/n).is_file() or (dest/n).read_bytes()!=t.encode()]
        if bad: raise SystemExit('Stale release outputs: '+', '.join(bad))
    else:
        dest.mkdir(exist_ok=True)
        for n,t in out.items(): (dest/n).write_text(t,encoding='utf-8')
    print(js({'reproducible':a.check,'files':len(out),'state':m['state'],'counts':m['counts']}))
