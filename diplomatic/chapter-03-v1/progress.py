#!/usr/bin/env python3
"""Read-only Chapter 3 release counters. Decisions are not accuracy scores."""
from pathlib import Path
import argparse, hashlib, json

def report(root):
    c=root/'diplomatic/chapter-03-v1'; load=lambda p:json.loads(p.read_text())
    p=load(c/'PLAN.json'); d=load(c/'DECISIONS.json')
    def justified(x):
        return bool(x.get('status') and x.get('rationale') and x.get('evidence') and
                    all((root/e.split('#')[0]).is_file() for e in x['evidence']))
    def count(key,ids):
        assert not set(d[key])-set(ids), 'Out-of-scope decisions'
        bad=[i for i,x in d[key].items() if not justified(x)]
        return {'total':len(ids),'documented':len(d[key])-len(bad),
                'remaining':len(ids)-len(d[key])+len(bad),'invalid':bad}
    for name,h in p['collation_hashes'].items():
        assert hashlib.sha256((c/name).read_bytes()).hexdigest()==h, 'Frozen comparison changed'
    paths=['reading.md','apparatus.md','reading.json','CHANGES.md','COVERAGE.md']
    return {'chapter':3,'state':p['status'],'source_anchors':p['original_anchor_count'],
        'electronic_representations_verified':4,'transcript_loci':count('loci',p['frozen_locus_ids']),
        'W_blocks':count('W',p['frozen_W_ids']),
        'source_checks':count('source_checks',[x['id'] for x in p['source_check_targets']]),
        'interventions':len(load(c/'INTERVENTIONS.json')),
        'restored_main_verses':sum(len(i['tibetan_lines']) for i in load(c/'INSERTIONS.json')),
        'deliverables':{'total':5,'present':sum((c/'release'/s).is_file() for s in paths)},
        'final_signoff':bool(d.get('final_signoff')),'exhaustive_witness_collation':False,
        'accuracy_score':None,'time_estimate':None}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',required=True,type=Path); args=ap.parse_args()
    print(json.dumps(report(args.repo.resolve()),ensure_ascii=False,indent=2))

if __name__=='__main__': main()
