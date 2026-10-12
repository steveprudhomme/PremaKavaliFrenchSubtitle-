# Reproduire la correction textuelle de 932 blocs

Le script `scripts/reproduire_correction_hi.py` contient les règles lexicales, les remplacements propres à chaque bloc, la ponctuation retenue et la liste des passages à écouter. Il reproduit la passe assistée par IA; il ne constitue pas un correcteur général du hindi et n'utilise pas l'audio.

Depuis la racine du dépôt avec Python 3.10+ :

```powershell
python scripts/reproduire_correction_hi.py
python scripts/validate_srt.py subtitles/hi/revised/prema-kavali.hi.revised.srt --json work/validation-revision.json
```

**La première commande réécrit** le SRT révisé, les CSV `corrections-hi-v1.csv` et `a-verifier-audio-hi.csv`, ainsi que `reports/correction-summary.json`. Sauvegarder toute nouvelle correction manuelle avant de la relancer. Elle refuse une source dont l'empreinte diffère de l'original attendu.

Résultat attendu : 932 blocs, 604 modifiés, 1 011 opérations consignées et 607 blocs à écouter. Les numéros et temps restent identiques. Le SHA-256 du SRT révisé est `d33c21f70ef44023792299964e28a4714efeb89345a4c6eddf15039bd568425a`.

Le validateur termine avec le code 1 : les 17 erreurs de durée initiales restent présentes. Les 567 avertissements ne doivent pas être présentés comme une validation audio. Les écritures du rapport et les noms de fichiers sont propres à cette version; ne pas appliquer cette table de numéros au V7 de 1 597 blocs.
