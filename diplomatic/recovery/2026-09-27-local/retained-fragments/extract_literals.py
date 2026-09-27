"""Extract literal historical records without executing retained recovery scripts."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
AGENTS = ROOT / 'recovery/agent-originals'


def write(name, source, records, limits):
    result = {'source': str(source.relative_to(ROOT)), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'method': 'Python AST literal extraction only; source script never executed.',
              'status': 'historical retained content; not a recovered original output or fresh visual certification',
              'limits': limits, 'records': records}
    (OUT/name).write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')


for name, filename, executed in [('tharpaling-44-47.json','retained-successful-checkpoint-44-47.py',True),
                                  ('tharpaling-48-51-unsaved.json','retained-failed-checkpoint-48-51.py',False)]:
    source = AGENTS/'gadkar_ch1'/filename
    tree = ast.parse(source.read_text())
    page_rows = None
    finding = []
    for node in tree.body:
        if isinstance(node, ast.For) and isinstance(node.iter, ast.List):
            page_rows = ast.literal_eval(node.iter)
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'entries' for t in node.targets):
            page_rows = ast.literal_eval(node.value)
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Attribute) and call.func.attr == 'append' and isinstance(call.args[0], ast.Dict):
                finding.append(ast.literal_eval(call.args[0]))
    assert page_rows and len(page_rows) == 4
    write(name, source, {'page_rows_fields':['pdf_page','start_unit','end_unit','row_anchors','unresolved'],
                        'page_rows':page_rows,'literal_findings':finding,'historical_save_succeeded':executed},
          ['Earlier report body is missing. Tuple fields retain original wording.',
           'PDF48–51 save failed before execution; submitted text is not a recovered saved report.' if not executed else
           'The append operation reportedly succeeded historically; its complete output is missing.',
           'No scan inspection performed by this extraction.'])

source = AGENTS/'zhichen_ch1/transcript-files/gcn_late_report.initial.py'
tree = ast.parse(source.read_text())
variables={}
class LiteralNames(ast.NodeTransformer):
    def visit_Name(self,node):
        if node.id not in variables: raise ValueError('Nonliteral variable: '+node.id)
        return ast.copy_location(ast.Constant(variables[node.id]),node)
for node in tree.body:
    if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
        name=node.targets[0].id
        if name=='source': variables[name]=ast.literal_eval(node.value)
        if name=='d':
            original=ast.literal_eval(LiteralNames().visit(node.value))
            write('gcn-initial-report-literal.json',source,original,[
                'Superseded: PDF449 U1427 locator is wrong; retained packet says U1253. PDF451 U1511 candidate is wrong; retained packet says U1331.',
                'Historical report explicitly failed continuous lexical comparison; no new exact witness reading is certified.',
                'Original stale values are retained verbatim as historical evidence; do not activate them.'])
            break
else: raise AssertionError('Gcn literal report missing')
print('Extracted 8 historical page tuples, 1 Tharpaling finding, 7 Gcn attempts and 5 Gcn findings; no scripts executed')
