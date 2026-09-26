#!/usr/bin/env python3
"""Extract supplied DOCX text without correcting or normalizing Tibetan."""
from pathlib import Path
from zipfile import ZipFile
import hashlib, json, shutil, xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parent.parent
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
INPUTS = [('adzom-2000', 'W1KG11703_7.docx', '1LLpqKSMtbiafuriq9uc2QAvZGtDoWaxD'),
          ('tharpaling-1983', 'W27491_7.docx', '1EF6ItGNGVXlLecm3RiYIyAYoUCl8swzz'),
          ('sichuan-2016', 'W3CN7084_7.docx', '1vIne9MXb0UW5tDRAR53Ixoi4VVmkH8-f')]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def extract(path):
    with ZipFile(path) as archive:
        doc = ET.fromstring(archive.read('word/document.xml'))
    paragraphs = []
    for p in doc.findall(f'{NS}body/{NS}p'):
        parts = []
        for node in p.iter():
            if node.tag == NS+'t': parts.append(node.text or '')
            elif node.tag in (NS+'br', NS+'cr'): parts.append('\n')
            elif node.tag == NS+'tab': parts.append('\t')
        paragraphs.append(''.join(parts))
    return '\n'.join(paragraphs)
if __name__ == '__main__':
    records = []
    for edition, filename, drive_id in INPUTS:
        original = ROOT/'editions'/edition/filename
        target = original.with_suffix('.txt')
        text = extract(original)
        target.write_bytes(text.encode('utf-8'))
        record = {'edition': edition, 'original': str(original.relative_to(ROOT)),
                  'text': str(target.relative_to(ROOT)), 'characters': len(text),
                  'original_sha256': digest(original), 'text_sha256': digest(target),
                  'source_url': 'https://drive.google.com/file/d/'+drive_id,
                  'provider_status': 'Cleaned e-text marked finished in shared worksheet',
                  'project_proofreading': 'Not yet checked line by line against the scan',
                  'transformation': 'w:t text; w:br/w:cr newline; w:tab tab; paragraphs joined with newline; no normalization'}
        records.append(record)
        (original.parent/'etext-provenance.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
        print(edition, len(text), 'characters', digest(original))
        if edition == 'adzom-2000':
            shutil.copy2(target, ROOT/'source'/target.name)
    (ROOT/'editions'/'etext-inventory.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
