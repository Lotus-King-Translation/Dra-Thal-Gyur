"""paired-text/1 grammar and pinned, read-only migration support (stdlib only)."""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'paired'
GOLD = 'diplomatic/root-tantra-v1/release'
ENGLISH = 'translations/2026-10-01-golden-aligned'
REVIEW = 'translations/2026-09-26-full-draft/golden-review'
SOURCE_TAG = 'root-tantra-v1.0.0'
TRANSLATION_TAG = 'translation-golden-aligned-v1.0.0'
EDITION = 'dra-thal-gyur-paired-v1.0.0'
PINS = {
    SOURCE_TAG: ('97379615d268149eee768c9c1ec99b7be2f993b4',
                 'b83051912977268b97615bd382d82e51c3406d61'),
    TRANSLATION_TAG: ('ed0783c6a394d4ace736a09d812f0666c6743848',
                      'e24e97ddad9cefa339b5583a38389179dba7a365'),
}
PAIR_RE = re.compile(r'<!-- pair: (DTG-\d{6})(.*?) -->\n(.*?)\n<!-- /pair -->', re.S)
NOTE_RE = re.compile(r'\[(N-[A-Za-z0-9-]+)\]')
LINK_RE = re.compile(r'\[([^\]\n]*)\]\(([^\s)]+)\)')
PARTS = [f'chapter-{n:02d}' for n in range(1, 7)] + ['closing-material']
TITLES = [f'Chapter {n}' for n in range(1, 7)] + ['Full-work colophon and closing material']
EMPTY_ROLES = {'source_annotation_anchor', 'joined_anchor'}
BARRIERS = {'source_heading', 'provisional_caption', 'unresolved_inscription',
            'unresolved_source_graphic'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def js(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def git(*args, root=ROOT):
    return subprocess.check_output(['git', '-C', str(root), *args])


def pinned(path, tag=TRANSLATION_TAG):
    return git('show', f'{PINS[tag][1]}:{path}')


def check_tags(root=ROOT):
    for tag, (obj, commit) in PINS.items():
        require(git('rev-parse', f'refs/tags/{tag}', root=root).decode().strip() == obj,
                f'Changed pinned tag object: {tag}')
        require(git('rev-parse', f'refs/tags/{tag}^{{}}', root=root).decode().strip() == commit,
                f'Changed pinned release commit: {tag}')


@dataclass
class Authorities:
    golden: dict
    english: dict
    footnotes: str
    protected: dict[str, str]


def load_authorities():
    check_tags()
    golden = json.loads(pinned(GOLD + '/reading.json', SOURCE_TAG))
    english = json.loads(pinned(ENGLISH + '/edition.json'))
    protected = json.loads(pinned(REVIEW + '/INPUTS.json'))['input_hashes'].copy()
    # Every released file is protected, including machine/human versions and notes.
    for tag, directory in [(SOURCE_TAG, GOLD), (TRANSLATION_TAG, ENGLISH)]:
        files = git('ls-tree', '-r', '--name-only', PINS[tag][1], '--', directory).decode().splitlines()
        for path in files:
            protected[path] = sha(pinned(path, tag))
    reader = pinned(ENGLISH + '/Dra-Thal-Gyur-English.md').decode()
    footnotes = reader.split('## Golden-source footnotes and endnotes\n\n', 1)[1]
    require(len(golden['reading_sequence']) == len(english['reading_sequence']) == 5484,
            'Pinned authority count')
    require([s['id'] for s in golden['reading_sequence']] ==
            [s['id'] for s in english['reading_sequence']], 'Pinned authority order')
    for g, e in zip(golden['reading_sequence'], english['reading_sequence']):
        require((g['text'], g['role']) == (e['golden_tibetan'], e['golden_role']),
                'Pinned authority disagreement: ' + g['id'])
    return Authorities(golden, english, footnotes, protected)


def check_protected(authorities, root=ROOT):
    for path, digest in authorities.protected.items():
        file = root / path
        require(file.is_file() and sha(file.read_bytes()) == digest,
                'Protected input changed or missing: ' + path)


def unique(items):
    return list(dict.fromkeys(items))


def part(row):
    return PARTS[row['part'] - 1]


def boundary_text(english):
    # These trailing notices carry their own periods, not the verse's predicate.
    text = NOTE_RE.sub('', english).rstrip()
    while True:
        shorter = re.sub(r'\s*\[(?:Editorial|Numerical grouping unresolved)[^\]]*\]\s*$', '', text)
        if shorter == text:
            return text.rstrip(' \t\n”’"\')')
        text = shorter.rstrip()


def ends_sentence(english):
    return bool(re.search(r'[.!?]$', boundary_text(english)))


def grouping(authorities):
    """Initial migration only: contiguous sentence blocks, with explicit layers."""
    rows = authorities.english['reading_sequence']
    groups, current = [], []

    def flush():
        if current:
            groups.append(current.copy())
            current.clear()

    for row in rows:
        role = row['golden_role']
        if current and part(current[-1]) != part(row):
            flush()
        # This heading interrupts an inherited sentence; keep its role visible.
        barrier = role in BARRIERS and row['id'] != 'SCAN-CH1-LAYER-02489'
        if barrier or row['id'] in {'U00001', 'U00003'}:
            flush()
            groups.append([row])
            continue
        if role in EMPTY_ROLES:
            if current:
                current.append(row)
            else:
                groups.append([row])
            continue
        current.append(row)
        if ends_sentence(row['english']):
            flush()
    flush()
    return groups


def rebase_links(text, from_file):
    def replace(match):
        label, target = match.groups()
        if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
            return match[0]
        path, sep, fragment = target.partition('#')
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(from_file), path)) if path else from_file
        local = posixpath.relpath(resolved, 'paired')
        return '[' + label + '](' + local + sep + fragment + ')'
    return LINK_RE.sub(replace, text)


def legacy_link(note):
    return f'[{note}](../{ENGLISH}/LEGACY-NOTES.md#{note.lower()})'


def source_payload(rows):
    # No normalization, strip, escape, hard-break insertion or loss of empty objects.
    return '\n'.join(row['golden_tibetan'] for row in rows)


def english_payload(rows):
    content = []
    for row in rows:
        value = NOTE_RE.sub(lambda m: legacy_link(m[1]), row['english'])
        if row['golden_role'] == 'source_annotation_anchor':
            require(value == '', 'Unexpected source annotation English')
            value = f"[Source annotation at {row['id']}; no additional root text. See attached endnotes.]"
        elif row['golden_role'] == 'joined_anchor':
            require(value == '', 'Unexpected joined English')
            value = f"[Joined source fragment at {row['id']}; no additional root text. See attached endnotes.]"
        content.append(value)
    notes = unique(n for row in rows for n in row['endnote_ids'])
    legacy = unique(n for row in rows for n in row['legacy_note_ids'])
    # The inline links preserve inherited placement; this adds coverage for
    # inherited note associations stored only in edition.json.
    text = '\n'.join(content)
    if notes:
        text += '\n\n' + ''.join(f'[^{n}]' for n in notes)
    if legacy:
        text += '\n\nEarlier notes: ' + ', '.join(legacy_link(n) for n in legacy) + '.'
    return text


def frontmatter(language):
    common = {'schema': 'paired-text/1', 'text-id': 'dra-thal-gyur',
              'paired-edition': EDITION, 'source-edition': SOURCE_TAG}
    if language == 'en':
        common['translation-edition'] = TRANSLATION_TAG
    common['language'] = language
    return '---\n' + ''.join(f'{k}: {v}\n' for k, v in common.items()) + '---\n'


def pair_comment(ident, rows, language):
    if language == 'en':
        return f'<!-- pair: {ident} -->'
    ids = ' '.join(row['id'] for row in rows)
    roles = ' '.join(row['golden_role'] for row in rows)
    return f'<!-- pair: {ident} | golden: {ids} | roles: {roles} | part: {part(rows[0])} -->'


def preamble(language):
    return frontmatter(language) + '\n# Dra Thal Gyur — ' + ('Tibetan source' if language == 'bo' else 'English translation') + '\n'


def note_footer(authorities, groups):
    owners = {}
    for index, rows in enumerate(groups, 1):
        for row in rows:
            for note in row['endnote_ids']:
                owners.setdefault(note, {}).setdefault(f'DTG-{index:06d}', []).append(row['id'])
    notes = rebase_links(authorities.footnotes, ENGLISH + '/Dra-Thal-Gyur-English.md').rstrip('\n')
    blocks = re.split(r'(?=^\[\^G-[^\]]+\]: )', notes, flags=re.M)
    out = []
    for block in blocks:
        if not block:
            continue
        note = re.match(r'\[\^(G-[^\]]+)\]: ', block)[1]
        links = '; '.join(f'[{ident}](#{ident.lower()}) (golden: {" ".join(ids)})'
                          for ident, ids in owners[note].items())
        out.append(block.rstrip('\n') + '\n\n    **Paired locations:** ' + links)
    return '\n\n## Golden-source footnotes and endnotes\n\n' + '\n\n'.join(out) + '\n'


def render(authorities, groups, language):
    out = preamble(language)
    current = None
    for index, rows in enumerate(groups, 1):
        this_part = part(rows[0])
        if this_part != current:
            current = this_part
            out += '\n## ' + TITLES[PARTS.index(current)] + '\n'
        ident = f'DTG-{index:06d}'
        out += f'\n<a id="{ident.lower()}"></a>\n\n'
        payload = source_payload(rows) if language == 'bo' else english_payload(rows)
        out += pair_comment(ident, rows, language) + '\n' + payload + '\n<!-- /pair -->\n'
    if language == 'en':
        out += note_footer(authorities, groups)
    return out


@dataclass
class Segment:
    ident: str
    golden: list[str]
    roles: list[str]
    part: str
    text: str


def parse(text, language):
    require(text.startswith(frontmatter(language)), f'Wrong or malformed pinned {language} front matter')
    matches = list(PAIR_RE.finditer(text))
    require(matches, 'No pair blocks')
    require(len(matches) == text.count('<!-- pair:') == text.count('<!-- /pair -->'),
            'Malformed or unclosed pair block')
    result = []
    for match in matches:
        ident, metadata, payload = match.groups()
        if language == 'bo':
            m = re.fullmatch(r' \| golden: ([A-Za-z0-9 -]+) \| roles: ([a-z_ ]+) \| part: ([a-z0-9-]+)', metadata)
            require(m is not None, 'Malformed source metadata: ' + ident)
            golden, roles, section = m.groups()
            result.append(Segment(ident, golden.split(), roles.split(), section, payload))
        else:
            require(metadata == '', 'Unexpected translation metadata: ' + ident)
            result.append(Segment(ident, [], [], '', payload))
    ids = [s.ident for s in result]
    require(len(ids) == len(set(ids)), 'Duplicate pair ID on ' + language + ' side')
    return result
