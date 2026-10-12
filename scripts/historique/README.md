# Scripts des essais antérieurs

Ces fichiers ont été retrouvés et lus, mais **n'ont pas été exécutés pendant la récupération ou la publication**. Ils servent à documenter le travail et à préparer sa reprise. Les README et commentaires historiques peuvent contenir des affirmations non vérifiées; le présent document précise leur statut.

## Transcription par morceaux

`Transcrire-PremaKavali.ps1` utilise le Whisper cuBLAS et le modèle large-v2 installés par Subtitle Edit. Il extrait un WAV mono à 16 kHz, transcrit en hindi et ajoute le décalage du début de l'extrait aux temps SRT.

Depuis la racine du dépôt, avec un audio local autorisé :

```powershell
powershell -NoProfile -File scripts/historique/Transcrire-PremaKavali.ps1 -AudioPath 'C:\chemin\film.m4a' -StartSeconds 0 -DurationSeconds 900 -Mode comparaison
```

Le script écrit dans `scripts/historique/resultats/` (ignoré par Git). Il possède deux modes : comparaison avec contexte 64 et faisceau 8; référence avec contexte 0, température 0, incrément 0 et faisceau 5. Ce sont les profils retrouvés, pas des réglages certifiés optimaux. `--no-context` est refusé par le moteur de l'essai; le script utilise `--max-context`.

## Contrôle de 25 passages

Le dossier `controle-25/` conserve le script, la liste CSV et les instructions retrouvés. Reconstituer son sous-dossier `audio/` avec les extraits locaux nommés dans le CSV. Ils ne sont pas inclus dans Git.

```powershell
powershell -NoProfile -File scripts/historique/controle-25/Verifier-25-Passages.ps1 -TestPremierSeulement
```

Retirer `-TestPremierSeulement` pour traiter les 25 extraits. Le script crée des résultats relatifs et recalés. Chaque sortie reste à comparer à l'audio. Il peut ignorer un extrait absent et produire un rapport incomplet : vérifier le nombre de lignes obtenu.

## Ancien paquet de traduction intégrale

Le dossier `traduction-automatique/` conserve les fichiers dans leur disposition d'origine, y compris V7 et les 143 blocs français. **Ne pas considérer son installateur comme corrigé ou validé.**

Le journal récupéré montre un échec de `tokenizers`/PyO3 avec Python 3.13. Le README recommande 3.11 ou 3.12, mais `Installer.ps1` appelle `py -3`, ce qui ne fixe pas cette version. Il ne contrôle pas tous les codes de sortie et peut afficher « Installation complete » après un échec. Un futur correctif doit sélectionner explicitement un interpréteur compatible, arrêter sur échec et vérifier les imports avant de lancer la traduction.

Le script Python prévoit NLLB `hin_Deva` → `fra_Latn`, un cache TSV et un fichier français complet automatiquement généré. Le français NLLB n'est pas une adaptation québécoise éditoriale. Son commentaire « human-reviewed » n'est pas étayé par les fichiers récupérés. Aucun résultat français complet ni succès de cette chaîne n'a été confirmé. Les textes illisibles peuvent être remplacés par des marqueurs, ce qui ne résout pas la transcription source.
