# Première correction textuelle du hindi

Date : 12 octobre 2026. Source : SRT hindi initial fourni par l'utilisateur. La [vidéo de référence](https://www.youtube.com/watch?v=q6oDYStjuI4) a été identifiée, mais aucune écoute complète ni nouvelle reconnaissance vocale n'a été effectuée.

## Résultat

- **604 blocs modifiés sur 932**, avec **1 011 modifications consignées** (remplacements lexicaux/contextuels et opérations de ponctuation; une même opération peut remplacer plusieurs occurrences dans un bloc).
- Orthographe et signes nasaux, formes verbales locales, accords évidents, mots anglais transcrits en devanagari, certains noms récurrents et ponctuation de phrases suffisamment claires.
- Exemple : `कॉलेज में बढ़ता` devient `कॉलेज में पढ़ता` (bloc 36), `शुप चिंतक` devient `शुभचिंतक` (bloc 76), et `ग्रह मंत्री` devient `गृह मंत्री` (bloc 862).
- Les **932 numéros et horodatages** sont inchangés. L'original est préservé octet pour octet. Aucun bloc n'est supprimé.
- Le fichier corrigé utilise UTF-8 avec BOM et des fins de ligne Windows pour Subtitle Edit.

Le [journal CSV](corrections-hi-v1.csv) donne le texte avant/après, les changements et les horodatages de chaque bloc modifié. Il s'agit d'une révision assistée par IA; une correction plausible dans le contexte ne prouve pas les mots réellement prononcés.

## Limites et travail restant

**607 blocs sont inscrits dans la [liste de contrôle audio](a-verifier-audio-hi.csv).** Cette liste inclut des blocs déjà corrigés : les ensembles se recoupent. Elle couvre les mots tronqués, répétitions, segments incohérents, coupures, changements de locuteur et corrections contextuelles à confirmer. Les autres blocs ne sont pas pour autant certifiés exacts.

Les répétitions de `कर दो`, `लुट` et `सब्सक्राइब`, les caractères `�` et les dialogues incomplets restent présents lorsqu'aucune correction textuelle suffisamment sûre n'est possible. Ils ne sont remplacés ni par des paroles inventées ni par des indications musicales supposées. L'épellation du mot de passe au bloc 698 reste inchangée malgré sa différence avec « daughter » : le contenu sonore doit trancher.

La piste automatique hindi originale de YouTube a été consultée sur plusieurs passages. Elle présente elle aussi des erreurs manifestes et des répétitions similaires; elle n'a pas été substituée au SRT. Elle a seulement servi d'indice supplémentaire pour la correction `इंफेक्शन` → `इनफैचुएशन` au bloc 45. Les sous-titres YouTube et les fichiers de travail ne sont pas redistribués ici. L'outil local de transcription Pinokio n'était pas accessible pendant cette passe.

## Contrôle technique

Le [rapport JSON](validation-hi-revised.json) signale toujours **17 erreurs de durée : 6 durées nulles et 11 négatives**, inchangées par rapport à l'original. Les **567 avertissements** comprennent 126 durées hors repères, 267 lignes longues, 56 répétitions possibles et 118 vitesses de lecture élevées. La hausse par rapport aux 555 avertissements de l'original vient des changements de longueur du texte corrigé; aucune amélioration de synchronisation n'est revendiquée.

Le code de sortie 1 du validateur est donc attendu. Aucun allongement arbitraire des durées ou déplacement des répliques n'a été appliqué. Une reprise à l'écoute doit résoudre le texte, les doublons et les durées avant toute publication finale ou traduction française.

```powershell
python scripts/validate_srt.py subtitles/hi/revised/prema-kavali.hi.revised.srt --json work/validation-revision.json
```
