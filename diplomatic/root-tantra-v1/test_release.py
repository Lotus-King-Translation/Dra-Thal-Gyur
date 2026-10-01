#!/usr/bin/env python3
import copy,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2]
m=json.load(open(root/"diplomatic/root-tantra-v1/release/reading.json")); g=json.load(open(root/"translations/2026-09-26-full-draft/data/source-units.json"))
def check(x):
 ids=[q["id"] for q in x["reading_sequence"] if re.fullmatch(r"U\d{5}",q["id"])]
 assert ids==[q["id"] for q in g] and len(ids)==5466
 assert len(x["reading_sequence"])==5484 and len({q["id"] for q in x["reading_sequence"]})==5484
 assert x["counts"]["restored_main_verses"]==23 and x["counts"]["closing_anchors"]==18
 assert not x["full_base_scan_proofread"] and not x["exhaustive_witness_collation"]
 assert sum(q["id"] in {f"U{i:05d}" for i in range(5449,5467)} for q in x["reading_sequence"])==18
check(m)
cases={
 "lost_anchor":lambda x:x["reading_sequence"].pop(0),
 "duplicated_id":lambda x:x["reading_sequence"].append(copy.deepcopy(x["reading_sequence"][0])),
 "reordered":lambda x:x["reading_sequence"].reverse(),
 "wrong_restored_count":lambda x:x["counts"].update(restored_main_verses=22),
 "wrong_closing_count":lambda x:x["counts"].update(closing_anchors=17),
 "false_proofread":lambda x:x.update(full_base_scan_proofread=True),
 "false_exhaustive":lambda x:x.update(exhaustive_witness_collation=True),
 "lost_closing":lambda x:x["reading_sequence"].pop(next(i for i,q in enumerate(x["reading_sequence"]) if q["id"]=="U05449")),
 "invented_anchor":lambda x:x["reading_sequence"].append({"id":"U99999","text":"bad"}),
 "wrong_original_order":lambda x:x["reading_sequence"].insert(0,x["reading_sequence"].pop(1))}
out=[]
for n,f in cases.items():
 x=copy.deepcopy(m); f(x)
 try: check(x)
 except Exception as e: out.append({"case":n,"rejected":True})
 else: raise RuntimeError("accepted "+n)
print(json.dumps({"positive_case_passed":True,"negative_cases_rejected":len(out),"cases":out,"editorial_originals_modified":False},indent=2))
