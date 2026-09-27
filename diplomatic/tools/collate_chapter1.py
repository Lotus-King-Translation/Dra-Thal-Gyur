#!/usr/bin/env python3
"""Exact, reversible collation of three supplied e-texts, Chapter 1 only.

No Unicode normalization, whitespace cleanup, spelling correction, or claim
that an e-text difference represents a printed-witness difference is made.
Offsets are zero-based Unicode code points in the original UTF-8 extraction.
"""
import bisect
import argparse
import collections
import difflib
import hashlib
import json
import pathlib
import re
import unicodedata

PATHS = {
    'A': 'editions/adzom-2000/W1KG11703_7.txt',
    'B': 'editions/tharpaling-1983/W27491_7.txt',
    'S': 'editions/sichuan-2016/W3CN7084_7.txt',
}
NEXT = 'དེ་ནས་ལྷ་དབང་རྟོག་པ་མེད།།'


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def exact_anchors(a, b, width=32):
    """LIS of unique exact 32-code-point windows; retain nonoverlap.

    These are merely computational alignment anchors. Exact differences
    remain unnormalized and can always reconstruct the input streams.
    """
    da, db = {}, {}
    for seq, dest in ((a, da), (b, db)):
        for i in range(len(seq) - width + 1):
            k = seq[i:i+width]
            dest[k] = i if k not in dest else -1
    candidates = sorted((i, db[k]) for k, i in da.items()
                        if i >= 0 and db.get(k, -1) >= 0)
    tails, indices, previous = [], [], []
    for n, (_, j) in enumerate(candidates):
        pos = bisect.bisect_left(tails, j)
        previous.append(indices[pos-1] if pos else -1)
        if pos == len(tails):
            tails.append(j); indices.append(n)
        else:
            tails[pos] = j; indices[pos] = n
    selected = []
    n = indices[-1] if indices else -1
    while n >= 0:
        selected.append(candidates[n]); n = previous[n]
    selected.reverse()
    anchors = []
    enda = endb = 0
    for i, j in selected:
        if i >= enda and j >= endb:
            anchors.append((i, j, width)); enda, endb = i+width, j+width
    return anchors


def align(a, b):
    anchors = exact_anchors(a, b)
    ops = []
    ai = bi = 0
    for i, j, size in anchors + [(len(a), len(b), 0)]:
        if i > ai or j > bi:
            matcher = difflib.SequenceMatcher(None, a[ai:i], b[bi:j], autojunk=False)
            ops.extend((tag, ai+x, ai+y, bi+u, bi+v)
                       for tag, x, y, u, v in matcher.get_opcodes())
        if size:
            ops.append(('equal', i, i+size, j, j+size))
        ai, bi = i+size, j+size
    merged = []
    for tag, x, y, u, v in ops:
        if merged and merged[-1][0] == tag and merged[-1][2] == x and merged[-1][4] == u:
            old = merged.pop(); merged.append((tag, old[1], y, old[3], v))
        else:
            merged.append((tag, x, y, u, v))
    assert ''.join(a[x:y] for _, x,y,u,v in merged) == a
    assert ''.join(b[u:v] for _, x,y,u,v in merged) == b
    assert all(a[x:y] == b[u:v] for t,x,y,u,v in merged if t == 'equal')
    return merged, len(anchors)


def boundary_map(ops, length):
    """Return before/after insertion coordinates for aligned A boundaries."""
    low = [None] * (length+1)
    high = [None] * (length+1)
    def put(x,y):
        low[x] = min(low[x],y) if low[x] is not None else y
        high[x] = max(high[x],y) if high[x] is not None else y
    for t,x,y,u,v in ops:
        put(x,u); put(y,v)
        if t == 'equal':
            for p in range(x+1,y): put(p,u+p-x)
    return low, high


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',required=True,type=pathlib.Path,help='Repository root containing editions/ and translations/.')
    parser.add_argument('--out',required=True,type=pathlib.Path,help='Output directory; no files outside it are modified.')
    args = parser.parse_args()
    ROOT, OUT = args.repo.resolve(),args.out.resolve()
    OUT.mkdir(parents=True,exist_ok=True)
    units = json.loads((ROOT/'translations/2026-09-26-full-draft/data/source-units.json').read_text())[:2635]
    full = {k:(ROOT/p).read_bytes().decode('utf-8') for k,p in PATHS.items()}
    ends = {k:v.index(NEXT) for k,v in full.items()}
    assert ends['A'] == units[-1]['end'] == 76376
    streams = {k:v[:ends[k]] for k,v in full.items()}
    assert ''.join(u['tibetan'] for u in units) == streams['A']
    meta = {k:{'path':PATHS[k], 'status':'unverified supplied e-text extraction',
               'full_file_sha256':digest(full[k]),'start':0,'end':ends[k],
               'chapter_sha256':digest(streams[k]),
               'chapter_utf8_bytes':len(streams[k].encode('utf-8'))}
            for k in PATHS}
    pairs, stats, mappings = {}, {}, {}
    intervals = []
    for k in ('B','S'):
        ops, anchor_count = align(streams['A'],streams[k])
        pairs[k] = [{'op':t,'A_start':x,'A_end':y,k+'_start':u,k+'_end':v,
                     'A':streams['A'][x:y],k:streams[k][u:v]}
                    for t,x,y,u,v in ops]
        stats[k] = {'exact_anchor_count':anchor_count,
                    'op_counts':dict(collections.Counter(t for t,*_ in ops))}
        mappings[k] = boundary_map(ops,len(streams['A']))
        intervals.extend((x,y) for t,x,y,u,v in ops if t != 'equal')
    # Union touching difference intervals: component boundaries never cut
    # through a non-equal pairwise span, including empty insertion spans.
    components = []
    for x,y in sorted(intervals):
        if components and x <= components[-1][1]:
            components[-1][1] = max(components[-1][1],y)
        else: components.append([x,y])
    records = []
    cursor = {'A':0,'B':0,'S':0}
    unit_starts = [u['start'] for u in units]
    for n,(x,y) in enumerate(components,1):
        lows = {'A':x, **{k:mappings[k][0][x] for k in ('B','S')}}
        highs = {'A':y, **{k:mappings[k][1][y] for k in ('B','S')}}
        assert all(z is not None for z in list(lows.values())+list(highs.values()))
        equal = {k:streams[k][cursor[k]:lows[k]] for k in PATHS}
        assert len(set(equal.values())) == 1, (n,x,y,equal)
        relevant = [u['id'] for u in units
                    if (u['start'] < y and u['end'] > x)
                    or (x==y and u['start'] <= x < u['end'])]
        if not relevant and x == len(streams['A']): relevant = [units[-1]['id']]
        vals = {k:streams[k][lows[k]:highs[k]] for k in PATHS}
        punctuation = all(all(c.isspace() or '\u0f00' <= c <= '\u0f3f' or unicodedata.category(c).startswith('P') for c in v)
                          for v in vals.values())
        flags = []
        if max(map(len,vals.values())) >= 20: flags.append('larger_or_structural_difference_review')
        if x == 0: flags.append('opening_boundary')
        if y == len(streams['A']): flags.append('closing_boundary')
        # Display context is deliberately separate from the exact patch spans.
        records.append({'id':f'C1-{n:04d}','source_units':relevant,
                        'offsets':{k:[lows[k],highs[k]] for k in PATHS},
                        'readings':vals,'classification':('editorial_bracket_or_spacing' if any('{' in v or '}' in v for v in vals.values()) else 'punctuation_or_spacing') if punctuation else 'textual',
                        'A_context_before':streams['A'][max(0,x-35):x],
                        'A_context_after':streams['A'][y:y+35],
                        'flags':flags,
                        'status':'e-text difference; print verification required'})
        cursor = highs
    tails = {k:streams[k][cursor[k]:] for k in PATHS}
    assert len(set(tails.values())) == 1
    # A reader-facing second layer groups differences by complete A source
    # units, with adjacent affected units merged. It preserves all raw IDs.
    by_id = {u['id']:u for u in units}
    grouped_intervals = []
    for r in records:
        us = [by_id[i] for i in r['source_units']]
        x,y = min(u['start'] for u in us),max(u['end'] for u in us)
        if grouped_intervals and x <= grouped_intervals[-1]['end']:
            grouped_intervals[-1]['end'] = max(grouped_intervals[-1]['end'],y)
            grouped_intervals[-1]['conflicts'].append(r)
        else:
            grouped_intervals.append({'start':x,'end':y,'conflicts':[r]})
    loci = []
    for n,g in enumerate(grouped_intervals,1):
        x,y = g['start'],g['end']
        spans = {'A':[x,y], **{k:[mappings[k][0][x],mappings[k][1][y]] for k in ('B','S')}}
        assert all(v is not None for span in spans.values() for v in span)
        loci.append({'id':f'L1-{n:04d}', 'source_units':[u['id'] for u in units if u['start']>=x and u['end']<=y],
                     'exact_conflicts':[r['id'] for r in g['conflicts']],
                     'offsets':spans, 'readings':{k:streams[k][a:b] for k,(a,b) in spans.items()},
                     'status':'e-text difference; print verification required'})
    for k in ('B','S'):
        rebuilt=[];pos=0
        for r in loci:
            x,y=r['offsets']['A'];rebuilt += [streams['A'][pos:x],r['readings'][k]];pos=y
        rebuilt.append(streams['A'][pos:])
        assert ''.join(rebuilt)==streams[k], k+' readable loci'
    # Reconstruct each witness using only A and exact difference records.
    for k in ('B','S'):
        rebuilt=[]; pos=0
        for r in records:
            x,y=r['offsets']['A'];rebuilt += [streams['A'][pos:x],r['readings'][k]];pos=y
        rebuilt.append(streams['A'][pos:])
        assert ''.join(rebuilt)==streams[k], k
    summary = {'scope':'Chapter 1 including opening and witness-specific material before the identical Chapter 2 incipit',
               'unicode_normalization':'none', 'offset_convention':'zero-based half-open Unicode code points',
               'sources':meta, 'pairwise_alignment':stats, 'conflict_groups':len(records),
               'classifications':dict(collections.Counter(r['classification'] for r in records)),
               'larger_or_structural_groups':[r['id'] for r in records if 'larger_or_structural_difference_review' in r['flags']],
               'source_units_with_differences':len(set(i for r in records for i in r['source_units'])),
               'readable_full_unit_loci':len(loci),
               'reconstruction_validation':{'A_source_units_exact':True,'B_from_A_and_apparatus_exact':True,'S_from_A_and_apparatus_exact':True},
               'alignment_caveat':'The monotonic computational alignment is lossless but not a certification of philological correspondence. Moved headings, omissions, and structural differences require manual review.'}
    for filename, data in [('chapter1-pairwise.json',pairs),('chapter1-conflicts.json',records),('chapter1-loci.json',loci),('chapter1-summary.json',summary)]:
        (OUT/filename).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for k,s in streams.items(): (OUT/f'chapter1-{k}.txt').write_bytes(s.encode('utf-8'))
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
