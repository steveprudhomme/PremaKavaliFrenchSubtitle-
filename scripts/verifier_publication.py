"""Vérifie l'intégrité et les liens de la publication sans modifier les fichiers."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def blocks(path):
    return [b.splitlines() for b in re.split(r'\n\s*\n', path.read_text(encoding='utf-8-sig').strip())]


def main():
    failures = []
    def check(condition, message):
        if not condition:
            failures.append(message)
    original = ROOT/'subtitles/hi/original/prema-kavali.hi.v1.srt'
    revised = ROOT/'subtitles/hi/revised/prema-kavali.hi.revised.srt'
    check(digest(original) == 'ae46c4d9c95ffdbdb12f5df07c1d5867227caf0d87cb4305e220a0b7851e8682', 'Original modifié')
    check(digest(revised) == 'd33c21f70ef44023792299964e28a4714efeb89345a4c6eddf15039bd568425a', 'Révision différente de la passe documentée')
    a,b = blocks(original), blocks(revised)
    check(len(a) == len(b) == 932, 'Nombre de blocs de la première révision')
    check([x[:2] for x in a] == [x[:2] for x in b], 'Numéros ou temps modifiés')
    with (ROOT/'reports/corrections-hi-v1.csv').open(encoding='utf-8-sig',newline='') as f:
        rows = list(csv.DictReader(f))
    check(len(rows)==604, 'Nombre de corrections')
    for row in rows:
        i=int(row['bloc'])-1
        check(row['avant']=='\n'.join(a[i][2:]) and row['apres']=='\n'.join(b[i][2:]), f'Journal différent du SRT au bloc {i+1}')
    v7=blocks(ROOT/'subtitles/hi/recovered/prema-kavali.hi.v7.srt')
    fr=blocks(ROOT/'subtitles/fr-CA/recovered/prema-kavali.fr.001-143.draft.srt')
    check(len(v7)==1597 and len(fr)==143,'Comptage V7 ou français partiel')
    check([x[:2] for x in v7[:143]]==[x[:2] for x in fr],'Alignement des 143 blocs français avec V7')
    with (ROOT/'archives/recuperation/inventaire-publication.csv').open(encoding='utf-8-sig',newline='') as f:
        inventory=list(csv.DictReader(f))
    for row in inventory:
        if row['fichier_depot']:
            path=ROOT/row['fichier_depot']
            check(path.is_file(), f'Archive absente : {path}')
            if path.is_file():
                check(digest(path)==row['sha256_publie'], f'Empreinte archive différente : {path}')
    # Les documents archivés gardent leur texte historique; leurs chemins
    # internes ne définissent pas la navigation actuelle du dépôt.
    for md in ROOT.rglob('*.md'):
        if 'archives' in md.relative_to(ROOT).parts and md.parent.name=='fichiers':
            continue
        for target in re.findall(r'\]\(([^)]+)\)', md.read_text(encoding='utf-8-sig')):
            if '://' not in target and not target.startswith('#'):
                check((md.parent/target.split('#')[0]).exists(), f'Lien introuvable : {md.relative_to(ROOT)} -> {target}')
    report = {'archives_referencees':len(inventory), 'blocs_revises':len(b), 'corrections':len(rows), 'erreurs_verification':failures}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(bool(failures))


if __name__=='__main__':
    raise SystemExit(main())
