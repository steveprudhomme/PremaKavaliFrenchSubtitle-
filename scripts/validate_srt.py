"""Validation SRT en lecture seule, sans dépendance externe (Python 3.10+)."""
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path

TIMING = re.compile(r"^(\d{2,}):([0-5]\d):([0-5]\d),(\d{3}) --> (\d{2,}):([0-5]\d):([0-5]\d),(\d{3})$")


def validate(path):
    raw = path.read_bytes()
    result = {"file": path.as_posix(), "bytes": len(raw),
              "sha256": hashlib.sha256(raw).hexdigest(), "errors": [], "warnings": []}
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        result["errors"].append({"cue": None, "message": "Encodage UTF-8 invalide"})
        return result
    result["encoding"] = "UTF-8 avec BOM" if raw.startswith(b"\xef\xbb\xbf") else "UTF-8"
    blocks = re.split(r"\n[ \t]*\n", text.replace("\r\n", "\n").replace("\r", "\n").strip())
    blocks = [b for b in blocks if b.strip()]
    result["cues"] = len(blocks)
    previous_start, max_end = -1, -1
    for expected, block in enumerate(blocks, 1):
        lines = block.splitlines()
        def issue(kind, message):
            result[kind].append({"cue": expected, "message": message})
        if len(lines) < 3:
            issue("errors", "Bloc incomplet ou texte absent")
            continue
        if lines[0] != str(expected):
            issue("errors", "Numérotation non séquentielle")
        match = TIMING.fullmatch(lines[1])
        if not match:
            issue("errors", "Horodatage SRT invalide")
            continue
        n = list(map(int, match.groups()))
        start = ((n[0] * 60 + n[1]) * 60 + n[2]) * 1000 + n[3]
        end = ((n[4] * 60 + n[5]) * 60 + n[6]) * 1000 + n[7]
        if end <= start:
            issue("errors", "Durée nulle ou négative")
        if start < previous_start:
            issue("errors", "Début antérieur au bloc précédent")
        if start < max_end:
            issue("warnings", "Chevauchement avec un bloc antérieur")
        previous_start, max_end = start, max(max_end, end)
        body = lines[2:]
        plain = re.sub(r"<[^>]*>", "", " ".join(body)).strip()
        if not plain:
            issue("errors", "Texte vide")
        if len(body) > 2:
            issue("warnings", "Plus de deux lignes")
        if any(len(line) > 42 for line in body):
            issue("warnings", "Ligne de plus de 42 caractères")
        duration = (end - start) / 1000
        if duration > 7 or 0 < duration < 1:
            issue("warnings", "Durée hors repère 1–7 secondes")
        if duration > 0 and len(plain) / duration > 20:
            issue("warnings", "Vitesse supérieure à 20 caractères/seconde")
        words = plain.split()
        if len(words) >= 8 and len(set(words)) <= len(words) / 3:
            issue("warnings", "Répétition possible : vérifier à l'écoute")
    if not blocks:
        result["errors"].append({"cue": None, "message": "Fichier vide"})
    result["last_end_ms"] = max_end if max_end >= 0 else None
    result["warning_counts"] = dict(collections.Counter(w["message"] for w in result["warnings"]))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--json", type=Path, help="Enregistrer le rapport détaillé")
    parser.add_argument("--strict", action="store_true", help="Échouer aussi sur les avertissements")
    args = parser.parse_args()
    if args.json and args.file.resolve() == args.json.resolve():
        parser.error("Le rapport ne doit pas remplacer le SRT")
    try:
        result = validate(args.file)
    except OSError as exc:
        parser.exit(2, f"Lecture impossible : {exc}\n")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{result.get('cues', 0)} blocs | {len(result['errors'])} erreurs | {len(result['warnings'])} avertissements")
    print(f"SHA-256 : {result['sha256']}")
    for message, count in result.get("warning_counts", {}).items():
        print(f"  {count} : {message}")
    for error in result["errors"]:
        print(f"  ERREUR bloc {error['cue']} : {error['message']}")
    return int(bool(result["errors"] or (args.strict and result["warnings"])))


if __name__ == "__main__":
    raise SystemExit(main())
