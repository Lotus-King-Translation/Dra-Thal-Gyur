#!/usr/bin/env python3
"""Inventory acquired assets; document limitations without altering source bytes."""
from pathlib import Path
import hashlib, json, datetime
ROOT = Path(__file__).resolve().parent.parent
E = ROOT/'editions'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
CAT = [
('adzom-2000','Adzom Chögar, 2000','W1KG11703','1','Active source. The title through the final colophon are included. Cleaned e-text awaits project proofreading.'),
('adzom-1973-1977','Adzom / Sanje Dorje, 1973–1977','W1KG892','1','Original full container-volume PDF; root commonly cited at printed pp. 1–205. Related to the Adzom printing tradition; not assumed independent.'),
('dege-W1ER7','Degé xylograph','W1ER7','I1ER175','Root range supplied in the shared worksheet and inspected in the images. The actual impression date is not established here.'),
('tsamdrak-1982','Tsamdrak manuscript facsimile, 1982','W21521','12','Printed pp. 2–173. Last image is shared with the next work; no cropping has been performed.'),
('tharpaling-1983','Tharpaling woodblock printing, 1983','W27491','2','Full root image range plus original container PDF and cleaned e-text. Print quality is uneven; e-text readings require scan checks.'),
('tingkye-1973','Tingkye manuscript facsimile, 1973','W21518','10','Printed pp. 386–530. Observed opening at image 394, line 5, is one image earlier than the structured catalogue start 395. Boundary pages retain neighbouring text.'),
('dzongsar-manuscript','Dzongsar old collection','W3PD988','147','Catalogued root range 5–252 acquired. Source images are very dark. Material description differs between worksheet and collection metadata; do not infer printing method solely from the folder name.'),
('langtang-manuscript','Langtang manuscript','W1ER124','3','All available canvases from title through closing material acquired. Eight image indices are absent from the provider manifest; no claim of complete foliation.'),
('seventeen-tantras-W1ER119','Unspecified-provenance manuscript','W1ER119','5','32 image indices are absent from the provider manifest within the selected range; treat as incomplete pending foliation audit.'),
('gadkar-manuscript','Gadkar manuscript','W1BL6 / W1ER156','32','Root record MW1BL6_0032_003 points to the W1ER156 virtual volume. Preserve virtual indices and actual image service identities separately.'),
('khams-zhichen-manuscript','Khams / Zhichen manuscript','W2PD17382','36','Catalogued root plus title leaf. Source record MW2PD17382_0036_003.'),
('gcn-manuscript','W1ER128 / rKTs Gcn collection','W1ER128','Unresolved digital packaging','Full first container PDF acquired. rKTs describes 19 logical texts; current BDRC packaging has three volumes. Do not identify digital volume 3 with Gcn3 merely by number. Root range remains unverified.'),
('sichuan-2016','Sichuan typeset edition, 2016','W3CN7084','2','Original cleaned e-text acquired. Internet Archive currently marks the scan access-restricted/copyright; no complete scan is stored here.'),
('paltseg-2009','Paltség compilation, 2009','W1KG14783','5 (bibliographic)','Catalogue metadata only. The structured root location contains volume 0; do not use that field as a verified scan-volume mapping.'),
('ctrc-49-volume','China Tibetology Research Centre, 49-volume edition','W3CN3207','3','Catalogue metadata and limited manifest only. Verified root record: MW3CN3207_O3CN3207_NAKR4R; the worksheet links a different part. No full root facsimile acquired.'),
('gangteng-EAP','Gangteng cursive Seventeen Tantras collection','WEAP039-1-4-259','Unresolved','Archival collection lead, not yet an isolated or downloaded root-tantra witness.')]
def main():
    entries = []
    for folder, label, wid, volume, note in CAT:
        d = E/folder; d.mkdir(exist_ok=True)
        manifest = d/'image-manifest.json'
        images = json.loads(manifest.read_text()) if manifest.exists() else None
        files = sorted(p for p in d.iterdir() if p.is_file() and p.suffix in ('.pdf','.zip','.docx','.txt'))
        status = 'Catalogue / lead only'
        if images: status = 'Facsimile with image-index gaps' if images['skipped_indices_not_in_manifest'] else 'Catalogued facsimile range acquired'
        elif any(p.suffix=='.pdf' for p in files): status = 'Container PDF acquired; root mapping pending'
        elif files: status = 'E-text acquired; full scan not acquired'
        record = {'folder':folder,'label':label,'bdrc':wid,'volume':volume,'status':status,'note':note}
        lines = ['# '+label, '', '**Status:** '+status, '', '**Catalogue:** '+wid+'; volume '+volume+'.', '', note, '', '## Stored files', '']
        lines += ['- ['+p.name+']('+p.name+')' for p in files]
        if images:
            record.update({'pages':images['pages'],'range':[images['bdrc_image_start'],images['bdrc_image_end']], 'missing_image_indices':images['skipped_indices_not_in_manifest']})
            lines += ['', 'The PDF and image archive preserve the available full-resolution IIIF responses. They are not a corrected text. [Image manifest](image-manifest.json) records every PDF page, source URL, image dimensions, checksum, and any skipped index. No new OCR was performed.']
            if record['missing_image_indices']: lines += ['', '**Missing image indices:** '+', '.join(map(str,record['missing_image_indices']))+'. These are provider-manifest gaps, not silently removed pages. Their textual significance is not resolved.']
        if (d/'metadata').exists(): lines += ['', '[Provider metadata](metadata/) is preserved as retrieved.']
        if (d/'etext-provenance.json').exists(): lines += ['', '[E-text provenance](etext-provenance.json). The provider marks cleaning finished; project proofreading is not complete.']
        lines += ['', '[Return to edition inventory](../README.md).', '']
        (d/'README.md').write_text('\n'.join(lines))
        entries.append(record)
    table = ['# Edition catalogue and remaining leads', '', 'Acquisition status as of '+datetime.date.today().isoformat()+'. Not a census of independent recensions.', '', '| Edition / record | BDRC | Volume | Actual holdings |', '| --- | --- | --- | --- |']
    table += [f"| [{x['label']}]({x['folder']}/README.md) | {x['bdrc']} | {x['volume']} | {x['status']} |" for x in entries]
    table += ['', '## Remaining bibliographic leads', '',
              'Not acquired in this setup: the Spiti 1977 publication; the Rig’dzin Tshewang Norbu manuscript; the Barber 1991 facsimile publication; published or announced translations. These remain leads from the earlier survey, not downloaded editions.', '',
              'The similar short-titled twelve-page W21727 item is not counted as a complete root witness. The worksheet is preserved separately; its claims are not silently substituted for this acquisition audit.', '']
    (E/'CATALOGUE.md').write_text('\n'.join(table))
    asset_types = {'.pdf','.zip','.docx','.txt','.xlsx','.json','.wikitext','.html'}
    assets = []
    for p in sorted(E.rglob('*')):
        if p.is_file() and p.suffix in asset_types and p.name not in ('ACQUISITION.json','VALIDATION.json'):
            assets.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
    audit = {'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'editions':entries, 'files':assets,
             'scope':'Acquisition and integrity audit, not textual collation or full foliation audit', 'new_ocr_performed':False}
    (E/'ACQUISITION.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    (E/'SHA256SUMS').write_text(''.join(x['sha256']+'  '+x['path']+'\n' for x in assets))
    source_files = []
    for name in ['Dra-Thal-Gyur-Adzom-2000.pdf','W1KG11703_7.docx','W1KG11703_7.txt']:
        p = ROOT/'source'/name
        source_files.append({'name':name,'bytes':p.stat().st_size,'sha256':sha(p)})
    source = {'edition':'Adzom 2000', 'bdrc':'W1KG11703', 'volume':1,
              'image_group':'I1KG11710', 'image_range':[3,207], 'pdf_pages':205,
              'image_manifest':'../editions/adzom-2000/image-manifest.json',
              'files':source_files, 'new_ocr_performed':False,
              'status':'Scan governs readings; cleaned e-text is not project-proofread'}
    (ROOT/'source'/'SOURCE.json').write_text(json.dumps(source,indent=2)+'\n')
    (ROOT/'source'/'SHA256SUMS').write_text(''.join(x['sha256']+'  '+x['name']+'\n' for x in source_files))
    print('Inventoried',len(assets),'assets;',sum(x['bytes'] for x in assets),'bytes')
    print('Image packets',sum('pages' in x for x in entries),'images',sum(x.get('pages',0) for x in entries))
if __name__ == '__main__': main()
