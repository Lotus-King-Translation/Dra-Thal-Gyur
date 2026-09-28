#!/usr/bin/env python3
"""Replay only retained Markdown constructors, never their surrounding scripts.

Usage: replay_markdown.py SOURCES OUTPUT
Unrecovered historical metadata is represented explicitly by placeholders.
The script refuses to execute or evaluate arbitrary Python source.
"""
import ast
import hashlib
import json
import pathlib
import sys


def value(node, names):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return names[node.id]
    if isinstance(node, ast.List):
        return [value(x, names) for x in node.elts]
    if isinstance(node, ast.Dict):
        return {value(k, names): value(v, names) for k, v in zip(node.keys, node.values)}
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        a, b = value(node.left, names), value(node.right, names)
        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError('Only string concatenation permitted')
        return a + b
    if isinstance(node, ast.Subscript):
        return value(node.value, names)[value(node.slice, names)]
    if isinstance(node, ast.JoinedStr):
        return ''.join(str(value(x, names)) for x in node.values)
    if isinstance(node, ast.FormattedValue) and node.conversion == -1 and node.format_spec is None:
        return str(value(node.value, names))
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr == 'replace' and not node.keywords and len(node.args) == 2):
        original = value(node.func.value, names)
        old, new = [value(x, names) for x in node.args]
        if not all(isinstance(x, str) for x in [original, old, new]):
            raise ValueError('Only string replacement permitted')
        if original.count(old) != 1:
            raise ValueError('Historical replacement must match once')
        return original.replace(old, new)
    raise ValueError('Unsupported expression: ' + ast.dump(node))


def assignments(tree, name):
    return [n.value for n in ast.walk(tree) if isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)]


def main():
    source_dir, output_dir = map(pathlib.Path, sys.argv[1:])
    expected_sources = {
        'save-tingkye-early-audit.py.retained-source': 'ea8407a101ac4065edb4dce77c4bd6a40b36b063',
        'tharpaling-late-attempt.stage1-saved-construction.py.txt': '680bb3bed2c442058c4d4d80518208ecd73841de',
        'tharpaling-late-attempt.stage3-saved-withdrawal.py.txt': '26dce263a3d8d7f0ca4215f549aa83a35c0c64e3',
    }
    for filename, expected in expected_sources.items():
        b = (source_dir / filename).read_bytes()
        actual = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
        if actual != expected:
            raise ValueError('Retained source blob mismatch: ' + filename)
    output_dir.mkdir(parents=True, exist_ok=True)
    names = {
        'tingkye-early-omission-audit.md': 'save-tingkye-early-audit.py.retained-source',
        'tharpaling-late-attempt.md': 'tharpaling-late-attempt.stage1-saved-construction.py.txt',
    }
    records = []
    for report, filename in names.items():
        raw = (source_dir / filename).read_bytes()
        tree = ast.parse(raw.decode())
        fields = {'source_pdf': '{{UNRECOVERED_SOURCE_PDF}}', 'pdf_sha256': '{{UNRECOVERED_PDF_SHA256}}'}
        env = {'meta': fields, 'd': fields}
        lines, = assignments(tree, 'lines')
        text_lines = value(lines, env)
        if report == 'tharpaling-late-attempt.md':
            note_node, = assignments(tree, 'notes')
            notes = value(note_node, {})
            assert set(notes) == set(range(44, 49))
            loops = [x for x in tree.body if isinstance(x, ast.For)
                     and isinstance(x.target, ast.Name) and x.target.id == 'n'
                     and isinstance(x.iter, ast.Call) and isinstance(x.iter.func, ast.Name)
                     and x.iter.func.id == 'range']
            loop, = loops
            assert [ast.literal_eval(x) for x in loop.iter.args] == [44, 49]
            append = loop.body[0].value
            assert isinstance(append, ast.Call) and append.func.attr == 'append'
            assert append.func.value.id == 'lines' and len(append.args) == 1
            for n in range(44, 49):
                text_lines.append(value(append.args[0], {'n': n, 'notes': notes}))
        result = '\n'.join(text_lines) + '\n'
        if report == 'tharpaling-late-attempt.md':
            withdrawal = source_dir / 'tharpaling-late-attempt.stage3-saved-withdrawal.py.txt'
            replacements = [x for x in assignments(ast.parse(withdrawal.read_text()), 's')
                            if isinstance(x, ast.Call) and isinstance(x.func, ast.Attribute)
                            and x.func.attr == 'replace']
            replacement, = replacements
            result = value(replacement, {'s': result})
            assert 'No positive unit mapping is retained here' in result
            assert 'After the preceding-page reader corrected the boundary' not in result
        result = '> Partial transcript-derived template. The original source-path and PDF-hash metadata values are unavailable. Placeholders are deliberate. This is not a complete recovered report or a new scan assessment.\n\n' + result
        data = result.encode()
        report = report.replace('.md', '.partial-template.md')
        (output_dir / report).write_bytes(data)
        records.append({'path': report, 'bytes': len(data),
                        'sha256': hashlib.sha256(data).hexdigest(),
                        'git_blob_sha': hashlib.sha1(b'blob ' + str(len(data)).encode()
                                                    + b'\0' + data).hexdigest(),
                        'source_sha256': hashlib.sha256(raw).hexdigest(),
                        'original_byte_identity_established': False,
                        'complete_report_recovered': False,
                        'unrecovered_fields': ['source_pdf', 'pdf_sha256']})
    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    main()
