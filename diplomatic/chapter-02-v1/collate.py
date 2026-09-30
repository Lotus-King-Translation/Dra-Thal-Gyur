#!/usr/bin/env python3
"""Lossless Chapter 2 electronic collation; makes no source-reading decisions."""
from pathlib import Path
import argparse, collections, difflib, hashlib, json, re, sys, unicodedata
sys.dont_write_bytecode = True

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def digest(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
def make(root):
    folder=root/'diplomatic/chapter-02-v1'; plan=load(folder/'PLAN.json')
    sys.path.insert(0,str(root/'diplomatic/tools'))
    from collate_chapter1 import align, boundary_map
    full={k:(root/m['path']).read_bytes().decode('utf-8') for k,m in plan['sources'].items()}
    for k,t in full.items():
        assert digest(t)==plan['sources'][k]['full_sha256'], 'Changed source '+k
    streams={k:t[plan['sources'][k]['start']:plan['sources'][k]['end']] for k,t in full.items()}
    for k,t in streams.items(): assert digest(t)==plan['sources'][k]['chapter_sha256']
    units=load(folder/'source-units.json'); offset=plan['sources']['A']['start']
    assert len(units)==987 and ''.join(u['tibetan'] for u in units)==streams['A']
    local=[dict(u,start=u['start']-offset,end=u['end']-offset) for u in units]
    pairs={}; maps={}; intervals=[]; stats={}
    for k in ['B','S']:
        ops,count=align(streams['A'],streams[k]); pairs[k]=ops
        maps[k]=boundary_map(ops,len(streams['A']))
        stats[k]={'exact_alignment_anchors':count,'operations':dict(collections.Counter(o[0] for o in ops))}
        intervals.extend((x,y) for op,x,y,a,b in ops if op!='equal')
    components=[]
    for x,y in sorted(intervals):
        if components and x<=components[-1][1]: components[-1][1]=max(y,components[-1][1])
        else: components.append([x,y])
    def record(ident,x,y,ids):
        spans={'A':[x,y],**{k:[maps[k][0][x],maps[k][1][y]] for k in ['B','S']}}
        assert all(v is not None for ab in spans.values() for v in ab), ident
        vals={k:streams[k][a:b] for k,(a,b) in spans.items()}
        return {'id':ident,'source_units':ids,'chapter_offsets':spans,
                'full_source_offsets':{k:[a+plan['sources'][k]['start'],b+plan['sources'][k]['start']] for k,(a,b) in spans.items()},
                'readings':vals,'evidence_scope':'Exact supplied transcripts, not verified print variants.'}
    diffs=[]; groups=[]; uid={u['id']:u for u in local}
    for i,(x,y) in enumerate(components,1):
        ids=[u['id'] for u in local if (u['start']<y and u['end']>x) or (x==y and u['start']<=x<u['end'])]
        if not ids and x==len(streams['A']): ids=[local[-1]['id']]
        r=record(f'C2-{i:04d}',x,y,ids)
        punct=all(all(c.isspace() or '\u0f00'<=c<='\u0f3f' or unicodedata.category(c).startswith('P') for c in t) for t in r['readings'].values())
        r['classification']='presentation' if punct else 'textual'
        r['structural_candidate']=max(map(len,r['readings'].values()))>=20
        r['A_context']=[streams['A'][max(0,x-40):x],streams['A'][y:y+40]]
        diffs.append(r)
        a=min(uid[n]['start'] for n in ids); b=max(uid[n]['end'] for n in ids)
        if groups and a<=groups[-1]['end']:
            groups[-1]['end']=max(b,groups[-1]['end']); groups[-1]['conflicts'].append(r['id'])
        else: groups.append({'start':a,'end':b,'conflicts':[r['id']]})
    loci=[]
    for i,g in enumerate(groups,1):
        r=record(f'L2-{i:04d}',g['start'],g['end'],[u['id'] for u in local if g['start']<=u['start'] and u['end']<=g['end']])
        r['exact_conflicts']=g['conflicts']; loci.append(r)
    for layer in [diffs,loci]:
        for k in ['B','S']:
            parts=[]; at=0
            for r in layer:
                x,y=r['chapter_offsets']['A']; parts.extend([streams['A'][at:x],r['readings'][k]]); at=y
            parts.append(streams['A'][at:]); assert ''.join(parts)==streams[k], 'Reconstruction failed '+k
    raw=(root/plan['W']['path']).read_bytes().decode('utf-8')
    assert digest(raw)==plan['W']['sha256']
    lines=raw.splitlines(keepends=True); lo,hi=plan['W']['lines_inclusive']
    assert lines[lo-1].strip()=='@2' and lines[hi].strip()=='@3'
    ledger=[]; w=[]; page=None; at=0
    norm=lambda t:re.sub(r'\s+',' ',re.sub(r'[/_*#@]+',' ',t)).strip()
    for number,line in enumerate(lines,1):
        start=at; at+=len(line); s=line.rstrip('\r\n')
        if number>hi: break
        if re.fullmatch(r'\d+',s): page=int(s)
        if number<lo: continue
        role=('page_marker' if re.fullmatch(r'\d+',s) else 'website_annotation' if s.startswith('[') else 'wrapper' if s.startswith('<') else 'chapter_marker' if s.startswith('@') else 'blank' if not s.strip() else 'reference_text')
        item={'line':number,'start':start,'end':at,'raw':line,'role':role,'page_marker':page}; ledger.append(item)
        if role=='reference_text': w.append({**item,'normalized':norm(s)})
    assert ''.join(x['raw'] for x in ledger)==''.join(lines[lo-1:hi])
    a=[dict(u,normalized=norm(u['wylie'])) for u in units if norm(u['wylie'])]
    alignment=[]; wc=[]
    for op,i,j,k,l in difflib.SequenceMatcher(None,[u['normalized'] for u in a],[q['normalized'] for q in w],autojunk=False).get_opcodes():
        au=a[i:j]; wu=w[k:l]
        alignment.append({'op':op,'units':[u['id'] for u in au],'lines':[q['line'] for q in wu]})
        if op=='equal': continue
        aa=' '.join(u['normalized'] for u in au); ww=' '.join(q['normalized'] for q in wu)
        wc.append({'id':f'W-C02-{len(wc)+1:03d}','operation':op,'source_units':[u['id'] for u in au],
            'source_before':a[i-1]['id'] if i else None,'source_after':a[j]['id'] if j<len(a) else None,
            'A_tibetan':[u['tibetan'] for u in au],'A_wylie':[u['wylie'] for u in au],
            'W_lines':[{key:q[key] for key in ['line','raw','page_marker','start','end']} for q in wu],
            'token_differences':[{'op':t,'A':' '.join(aa.split()[x:y]),'W':' '.join(ww.split()[v:z])} for t,x,y,v,z in difflib.SequenceMatcher(None,aa.split(),ww.split(),autojunk=False).get_opcodes() if t!='equal']})
    assert [u for r in alignment for u in r['units']]==[u['id'] for u in a]
    assert [n for r in alignment for n in r['lines']]==[q['line'] for q in w]
    summary={'source_units':len(units),'exact_differences':len(diffs),'readable_loci':len(loci),
        'difference_classes':dict(collections.Counter(r['classification'] for r in diffs)),
        'structural_candidates':[r['id'] for r in diffs if r['structural_candidate']],
        'pairwise_alignment':stats,'minimal_and_whole_locus_reconstruction_passed':True,
        'W_lines_accounted':len(ledger),'W_reference_lines':len(w),'W_conflict_blocks':len(wc),
        'W_equal_normalized_units':sum(len(q['units']) for q in alignment if q['op']=='equal'),
        'caveat':'Exact data coverage and monotonic alignment are not source-glyph verification or automatic variant decisions.'}
    outputs={'collation.json':{'summary':summary,'loci':loci,'differences':diffs,'pairwise':pairs},
        'wikisource.json':{'summary':{k:v for k,v in summary.items() if k.startswith('W_')},'provenance':load(root/plan['W']['provenance']),
        'normalization_for_alignment_only':'Strip / _ * # @ and collapse whitespace in stored Wylie; exact originals retained. No Unicode conversion or adopted W reading.',
        'line_ledger':ledger,'alignment':alignment,'conflicts':wc}}
    result={n:json.dumps(v,ensure_ascii=False,indent=2)+'\n' for n,v in outputs.items()}
    result.update({f'source-{k}.txt':t for k,t in streams.items()})
    return result,summary

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--check',action='store_true'); args=ap.parse_args(); root=args.repo.resolve()
    outputs,summary=make(root); folder=root/'diplomatic/chapter-02-v1'
    for name,value in outputs.items():
        target=folder/name
        if args.check: assert target.read_bytes()==value.encode('utf-8'), 'Stale output '+name
        else: target.write_bytes(value.encode('utf-8'))
    print(json.dumps({'reproducible':bool(args.check),**summary},indent=2))

if __name__=='__main__': main()
