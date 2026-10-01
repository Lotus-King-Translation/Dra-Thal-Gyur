#!/usr/bin/env python3
"""Project validated canonical Markdown into generated supporting reports."""
import argparse
import sys
sys.dont_write_bytecode = True
from core import HERE, js, require, load_authorities
from structure import audit_report
from validate import validate_repo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    report = validate_repo()
    outputs = {'MANIFEST.json': js(report),
               'v2/PAIR-AUDIT.json': js(audit_report(load_authorities().golden['reading_sequence']))}
    for name, text in outputs.items():
        path = HERE / name
        if args.check:
            require(path.is_file() and path.read_bytes() == text.encode(), 'Stale generated report: ' + name)
        else:
            path.write_bytes(text.encode())
    print('Generated manifest ' + ('reproduces exactly' if args.check else 'saved from canonical Markdown'))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
