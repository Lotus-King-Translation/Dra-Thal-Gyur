#!/usr/bin/env python3
"""Chapter-1-only mechanical comparison; no repository mutation.
Use --pyewts to enable installed pyewts, or --pyewts PATH for a dependency directory.
"""
from pathlib import Path
import json,re,difflib,hashlib,collections,argparse,sys
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo',required=True,type=Path,help='Repository root containing source/, editions/ and translations/.')
parser.add_argument('--out',required=True,type=Path,help='Output directory; only files in this directory are written.')
parser.add_argument('--pyewts',nargs='?',const='',default=None,metavar='PATH',help='Enable diagnostic Unicode conversion; optionally add PATH to Python module search.')
args=parser.parse_args()
ROOT=args.repo.resolve()
OUT=args.out.resolve()
OUT.mkdir(parents=True,exist_ok=True)
units_all=json.loads((ROOT/'translations/2026-09-26-full-draft/data/source-units.json').read_text())
us=units_all[:2635]
assert ''.join(u['tibetan'] for u in units_all)==(ROOT/'source/W1KG11703_7.txt').read_text()
assert us[-1]['id']=='U02635' and us[-1]['end']==76376
raw=(ROOT/'editions/adzom-wikisource/source.wikitext').read_bytes().decode('utf-8')
assert raw.splitlines()[2664]=='@2'
def norm(s): return re.sub(r'\s+',' ',re.sub(r'[/_*#@]+',' ',s)).strip()
w=[];annotations=[];page=None;ledger=[];offset=0
converter=None
if args.pyewts is not None:
 if args.pyewts:sys.path.insert(0,str(Path(args.pyewts).resolve()))
 try:
  import pyewts
 except ImportError as err:
  parser.error('--pyewts was requested but pyewts could not be imported: '+str(err))
 converter=pyewts.pyewts()
for ln,line in enumerate(raw.splitlines(keepends=True),1):
 if ln>2664:break
 s=line.rstrip('\n')
 rec=dict(line=ln,start=offset,end=offset+len(line),raw_with_line_ending=line)
 offset+=len(line)
 if re.fullmatch(r'\d+',s):
  page=int(s);rec['role']='page_marker'
 elif s.startswith('['):rec['role']='website_editorial_annotation'
 elif s.startswith('<'):rec['role']='wrapper'
 elif s.startswith('@'):rec['role']='chapter_marker'
 elif not s.strip():rec['role']='blank'
 else:rec['role']='transcribed_root_text_line'
 rec['page_marker']=page
 ledger.append(rec)
 if rec['role']=='website_editorial_annotation':annotations.append(dict(line=ln,page_marker=page,raw=s))
 if rec['role']!='transcribed_root_text_line':continue
 z=dict(line=ln,page_marker=page,raw=s,normalized=norm(s))
 if converter:
  warnings=[]
  z['diagnostic_unicode']=converter.toUnicode(s,warnings)
  z['conversion_warnings']=warnings
  rec['diagnostic_unicode']=z['diagnostic_unicode'];rec['conversion_warnings']=warnings
 w.append(z)
a=[dict(u,normalized=norm(u['wylie'])) for u in us if norm(u['wylie'])]
sm=difflib.SequenceMatcher(None,[x['normalized'] for x in a],[x['normalized'] for x in w],autojunk=False)
ops=sm.get_opcodes();data=[];alignment=[]
reasons={
 'textual_difference':'Retain A as supplied provisionally until the governing print is checked. W is a related digital transcription; this disagreement alone cannot justify emendation.',
 'source_heading_or_label_absent_in_web_transcription':'Preserve the source label as evidence provisionally. Verify its printed status and placement before assigning it to root text or editorial apparatus; its absence in W does not decide the matter.',
 'source_text_absent_in_web_transcription':'Retain the source string as evidence provisionally. Its absence in the related website does not authorize deletion; it may be an opening formula or a source annotation whose printed status requires checking.',
 'web_text_absent_in_source_units':'Record W as possible missing source text without inserting it solely on website authority. A subsequent scan-attested intervention may restore it and governs the adopted reading.',
 'romanization_or_spacing_difference':'Preserve exact A and W spellings provisionally. Do not infer different Tibetan solely from transliteration conventions; check the print if stack, vowel or spacing affects the adopted reading.'
}
for t,i,j,k,l in ops:
 sa=a[i:j];sw=w[k:l]
 alignment.append(dict(operation=t,source_units=[u['id'] for u in sa],web_lines=[u['line'] for u in sw]))
 if t=='equal':continue
 aa=' '.join(x['normalized'] for x in sa);ww=' '.join(x['normalized'] for x in sw)
 def norm_roman(z):
  z=z.lower().replace('+',' ')
  z=re.sub(r'\s+',' ',z)
  return re.sub(r"\s+'(o|am|i)\b",r"'\1",z)
 cat='textual_difference'
 if not sw and all(re.match(r'(dris lan |lan don |thun mong .*gleng gzhi|de dag gi zhabs sdud)',x['normalized']) for x in sa):cat='source_heading_or_label_absent_in_web_transcription'
 elif norm_roman(aa)==norm_roman(ww):cat='romanization_or_spacing_difference'
 elif not sa:cat='web_text_absent_in_source_units'
 elif not sw:cat='source_text_absent_in_web_transcription'
 data.append(dict(id=f'W-C01-{len(data)+1:03}',operation=t,category=cat,decision_stage='pre-scan digital comparison; chapter scan interventions supersede this provisional disposition',rationale=reasons[cat],source_units=sa,wikisource_lines=sw,source_before=a[i-1]['id'] if i else None,source_after=a[j]['id'] if j<len(a) else None,wikisource_before=w[k-1]['line'] if k else None,wikisource_after=w[l]['line'] if l<len(w) else None,token_differences=[dict(operation=q,source=' '.join(aa.split()[ai:aj]),wikisource=' '.join(ww.split()[wi:wj])) for q,ai,aj,wi,wj in difflib.SequenceMatcher(None,aa.split(),ww.split(),autojunk=False).get_opcodes() if q!='equal']))
signs=[dict(id=u['id'],wylie=u['wylie'],tibetan=u['tibetan']) for u in us if '*' in u['wylie']]
source_only_signs=[dict(u) for u in us if not norm(u['wylie'])]
stats={'source_units_total':len(us),'source_units_with_lexical_content':len(a),'wikisource_root_text_lines':len(w),'exact_normalized_equal_lines':sum(j-i for t,i,j,k,l in ops if t=='equal'),'conflict_blocks':len(data),'categories':dict(collections.Counter(d['category'] for d in data)),'source_units_containing_asterisk':len(signs),'source_only_sign_units':len(source_only_signs),'website_editorial_annotation_lines':len(annotations)}
res={'scope':'Chapter 1 including preliminary opening material; U00001-U02635; Wiki file lines1-2664. No future chapters collated.','normalization_for_alignment_only':'Strip EWTS / _ * # @ signs, collapse whitespace. Apparatus retains complete exact source Tibetan/Wylie and exact website lines. Romanization category lowercases/removes stack + spacing for classification only; it is not proof of Tibetan equivalence.','stats':stats,'provenance':json.loads((ROOT/'editions/adzom-wikisource/PROVENANCE.json').read_text()),'conflicts':data,'website_editorial_annotations':annotations,'source_units_containing_asterisk':signs,'source_only_sign_units':source_only_signs}
(OUT/'wikisource-ch1-diffs.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
assert ''.join(x['raw_with_line_ending'] for x in ledger)==''.join(raw.splitlines(keepends=True)[:2664])
assert [u for q in alignment for u in q['source_units']]==[u['id'] for u in a]
assert [u for q in alignment for u in q['web_lines']]==[u['line'] for u in w]
raw_ledger={'scope':'All exact raw Wikisource lines1-2664, all exact source units U00001-U02635, with full lexical alignment. This includes punctuation, whitespace, wrappers, notes and page/chapter markers without deleting them.','diagnostic_conversion':'pyewts toUnicode default sloppy=True when --pyewts is requested; no conversion text is an adopted reading and warnings are preserved. Sanskrit and non-EWTS plain Wylie may not recover print orthography.','pyewts_available':converter is not None,'website_line_count':len(ledger),'website_raw_scope_sha256':hashlib.sha256(''.join(q['raw_with_line_ending'] for q in ledger).encode()).hexdigest(),'source_unit_count':len(us),'source_units':us,'website_lines':ledger,'lexical_alignment':alignment,'conversion_warning_lines':[q['line'] for q in ledger if q.get('conversion_warnings')]}
(OUT/'wikisource-ch1-raw-ledger.json').write_text(json.dumps(raw_ledger,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'stats':stats,'raw_ledger_lines':len(ledger),'pyewts_available':converter is not None,'conversion_warning_lines':raw_ledger['conversion_warning_lines']},indent=2))
