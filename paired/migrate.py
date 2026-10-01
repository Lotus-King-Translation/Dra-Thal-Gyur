#!/usr/bin/env python3
"""Initialize canonical Markdown once, or check the frozen migration read-only."""
import argparse
import sys
sys.dont_write_bytecode = True
from core import HERE, check_protected, grouping, load_authorities, render, require


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--initialize', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    authorities = load_authorities()
    check_protected(authorities)
    groups = grouping(authorities)
    outputs = {'source.md': render(authorities, groups, 'bo'),
               'translation.md': render(authorities, groups, 'en')}
    if args.initialize:
        require(not any((HERE / name).exists() for name in outputs),
                'Canonical files already exist; initialization never overwrites edits')
        for name, text in outputs.items():
            (HERE / name).write_bytes(text.encode('utf-8'))
    else:
        for name, text in outputs.items():
            require((HERE / name).read_bytes() == text.encode('utf-8'),
                    'Canonical migration differs: ' + name)
    print(f'{len(groups)} pairs; 5484 golden objects; canonical files ' +
          ('initialized' if args.initialize else 'reproduce exactly'))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
