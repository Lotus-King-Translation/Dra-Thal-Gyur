"""Apply explicit coordinator dispositions; preserve every raw report and question.
No automatic acceptance of glyphs or chapter completion. Publication is separate.
"""
from pathlib import Path
import copy, json, re, subprocess, sys
R=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur'); D=R/'diplomatic'
C=D/'collation/chapter-01'; V=D/'reviews/chapter-01/continuation'
S=Path(__file__).parent
sys.path.insert(0,str(V/'SESSION-20260929-CLOSE-INTEGRATION'))
import integrate_reviewed_batch as ib
load=ib.load; dump=ib.dump

def apply(plan, decisions):
    name=plan['task']+'-'+plan['batch']
    decision_path=S/(name+'-decisions.json')
    assert not decision_path.exists(), 'Preserve previous decisions; do not overwrite'
    before={p.name:p.read_bytes() for p in [C/'reading-units.json',C/'ch1-scan-insertions.json',C/'additional-interventions.json']}
    dump(decision_path, decisions)
    plan={**plan,'target_page':plan['target_pages'][0]}
    result=ib.integrate(plan,decisions)
    for filename,payload in before.items():
        assert (C/filename).read_bytes()==payload, filename
    dump(S/(name+'-integration.json'),result)
    return result

def validate_and_record(label, summary):
    for tool,suffix,args in [('build_chapter1.py','build',[]),('validate_chapter1.py','validation',[]),('build_chapter1.py','reproducibility',['--check'])]:
        result=subprocess.run(['python3','diplomatic/tools/'+tool,'--repo','.',*args],cwd=R,text=True,capture_output=True)
        (S/(label+'-'+suffix+'.stdout')).write_text(result.stdout)
        (S/(label+'-'+suffix+'.stderr')).write_text(result.stderr)
        if result.returncode:
            raise RuntimeError(tool+': '+result.stderr)
    validation=json.loads((S/(label+'-validation.stdout')).read_text())
    assert validation['base_units_accounted_for']==2635
    assert validation['restored_main_verses']==13
    assert not validation['chapter_complete'] and not validation['next_chapter_started']
    path=D/'WORK-STATUS.md'; text=path.read_text()
    text=re.sub(r'Current \[Chapter 1\]\(chapter-01.md\) SHA-256: `[0-9a-f]+`', 'Current [Chapter 1](chapter-01.md) SHA-256: `'+validation['markdown_sha256']+'`',text,count=1)
    from collections import Counter
    counts=Counter(r['witness'] for r in load(C/'scan-comparison-loci.json'))
    line='- **'+str(sum(counts.values()))+' comparison records**, including qualified observations and uncertainty: '+', '.join(k+' '+str(v) for k,v in sorted(counts.items()))+'. These are not a count of confirmed variants or a coverage percentage.'
    text=re.sub(r'^- \*\*\d+ comparison records\*\*.*$',line,text,count=1,flags=re.M)
    path.write_text(text+'\n'+summary+'\n')
    subprocess.run(['git','diff','--check'],cwd=R,check=True)
    return validation
