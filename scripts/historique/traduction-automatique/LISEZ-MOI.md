# Prema Kavali — sous-titres français intégralement automatisés (brouillon)

Ce paquet contient le SRT hindi V7 du film entier (1 597 blocs), ainsi que les 143 premières traductions françaises déjà produites. Il **ne contient pas de sous-titres français intégraux prématurément présentés comme traduits**.

## Windows / PowerShell

1. Installer **Python 3.11 ou 3.12**, avec le lanceur `py` disponible.
2. Décompresser tous les fichiers dans un même dossier Windows (éviter OneDrive si possible).
3. Ouvrir PowerShell dans ce dossier.
4. Exécuter `powershell -NoProfile -ExecutionPolicy Bypass -File .\Installer.ps1` (une seule fois).
5. Exécuter `powershell -NoProfile -ExecutionPolicy Bypass -File .\Traduire-Tout.ps1`.
6. Patienter. Lors de la première exécution, le modèle open source `facebook/nllb-200-distilled-600M` est téléchargé (~2.5 Go de poids, plus d'espace requis pour l'installation). Une connexion Internet est nécessaire pour cette étape.
7. Le fichier final est `Prema_Kavali_FR_CA_COMPLET_AUTOMATIQUE_A_REVISER.srt`. Ouvrez-le dans Subtitle Edit.

Le script utilise le GPU NVIDIA avec CUDA si disponible, sinon le CPU. Si le GPU échoue par manque de mémoire, exécuter `powershell -NoProfile -ExecutionPolicy Bypass -File .\Traduire-Tout.ps1 --cpu --batch-size 1` (plus lent). Si CUDA n'est pas disponible, vérifier les pilotes NVIDIA et la version de PyTorch installée.

En cas d'interruption, relancer exactement la même commande : la progression est conservée dans `traduction_progression.tsv` et seuls les blocs restants sont traduits.

**Limites :** la traduction NLLB est automatique, pas de niveau éditorial. Le texte hindi V7 contient des erreurs de reconnaissance, du mélange hindi/anglais, des caractères invalides et des sous-titres extrêmement courts. Le résultat garde leurs timecodes; aucune validation audio n'est implicite. Le résultat nécessite une relecture humaine, une adaptation québécoise, et une vérification des chevauchements/temps d'exposition. Le script marque les textes illisibles plutôt que d'inventer le dialogue. Le rapport CSV indique les sous-titres suspects.

**Politique de droits d'auteur :** vérifiez l'autorisation nécessaire avant de diffuser les sous-titres ou tout extrait du film.
