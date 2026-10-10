# Validation SRT

Le script lit le SRT sans le modifier. Python 3.10+ suffit. Exécuter les commandes depuis la racine du dépôt.

```powershell
# Archive initiale : sortie 1 attendue à cause des durées nulles
python scripts/validate_srt.py subtitles/hi/original/prema-kavali.hi.v1.srt

# Nouveau rapport local, sans écraser le rapport de référence
python scripts/validate_srt.py subtitles/hi/original/prema-kavali.hi.v1.srt --json work/validation-hi.json

# Après création de la traduction : avertissements également bloquants
python scripts/validate_srt.py subtitles/fr-CA/prema-kavali.fr-CA.draft.srt --strict --json work/validation-fr-CA.json

# Vérifier l'empreinte de l'archive initiale
Get-FileHash subtitles/hi/original/prema-kavali.hi.v1.srt -Algorithm SHA256
```

SHA-256 attendu : `ae46c4d9c95ffdbdb12f5df07c1d5867227caf0d87cb4305e220a0b7851e8682`.

Codes de sortie : `0` = aucun problème bloquant; `1` = erreurs (ou avertissements avec `--strict`); `2` = commande ou lecture impossible. Les erreurs sont les blocs vides/incomplets, l'UTF-8 invalide, la numérotation non séquentielle, les horodatages invalides, les durées non positives et les débuts non chronologiques.

Les avertissements portent sur les chevauchements, les lignes longues, plus de deux lignes, la durée, la vitesse de lecture et certaines répétitions. Plusieurs peuvent concerner le même bloc. Les caractères sont comptés en points de code Unicode, pas en glyphes : les seuils sont surtout des repères pour le français et ne constituent pas une mesure linguistique fiable du hindi.

Le script ne vérifie ni la traduction, ni la langue réelle, ni les hallucinations, ni la couverture du film, ni la synchronisation audio. Il n'a pas accès à la vidéo. Les répétitions signalées peuvent être intentionnelles, notamment dans les chansons. Un résultat sans erreur ne suffit pas pour publier une traduction finale.
