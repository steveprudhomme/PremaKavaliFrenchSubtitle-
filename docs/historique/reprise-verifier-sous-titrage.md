# Reprise de « Vérifier le sous-titrage »

Récupération du 12 octobre 2026 pour poursuivre le projet Prema Kavali. Conversation source : `6aca67d1-30ec-83ea-b90a-c57d59756787`.

## Ce qui a été récupéré

- Les **48 tours accessibles**, du premier message au dernier, lus sur cinq pages du connecteur; [messages accessibles](verifier-sous-titrage-messages.md) (les données brutes restent dans l’archive locale).
- **10 pièces jointes**, dont l'audio M4A du film, des versions SRT, deux résultats de transcription des 15 premières minutes, un ZIP de résultats Whisper, un CSV de comparaison sur 25 passages, une capture et un journal d'installation.
- Les fichiers associés retrouvés dans trois dossiers du projet sous Téléchargements et trois archives ZIP : scripts de transcription, résultats, 25 extraits audio, SRT hindi V7 et première traduction française.
- **134 fichiers copiés**, avec vérification d'intégrité SHA-256. Voir le [inventaire de publication](../../archives/recuperation/inventaire-publication.csv). L'extraction des SRT du ZIP Whisper est distincte de ce nombre.
- **88 fichiers SRT inventoriés**, doublons inclus; voir [inventaire SRT](../../archives/recuperation/inventaire-srt.csv).

L’archive locale complète reste conservée séparément. À la demande de l’utilisateur, les documents, scripts, SRT et messages accessibles ont ensuite été intégrés au dépôt; les chemins personnels des messages et journaux sont neutralisés. L’audio et les archives susceptibles de contenir des médias restent locaux et sont inventoriés. Aucun script historique n’a été exécuté pendant la récupération ou la publication.

## Limite de récupération de la conversation

Le connecteur expose le texte des messages utilisateur, mais les réponses de l'assistant sont représentées par des références opaques. Le navigateur intégré n'a pas de session ChatGPT connectée et ne permet pas de lire ces réponses. L'export n'est donc **pas une transcription intégrale des échanges**. Les réponses manquantes ne sont ni inventées ni déduites comme des faits établis.

Les conclusions ci-dessous reposent sur les messages lisibles, les journaux, les fichiers effectivement retrouvés et les contrôles faits ici. Les fichiers produits dans les réponses mais absents des pièces jointes et des dossiers inspectés ne sont pas récupérés.

## Étapes reconstituées et preuves

1. **Évaluer la transcription initiale.** Demande de vérification des sous-titres Subtitle Edit et d'amélioration des paramètres. Le fichier initial de 932 blocs reste la source archivée du dépôt actuel.
2. **Passer du CPU au GPU.** Discussion de CPU, cuBLAS et Vulkan. L'utilisateur choisit `large-v2`, faute de `large-v3`. La capture récupérée montre Whisper CPP, cuBLAS, Hindi, large-v2 (3,09 Go), traduction anglaise désactivée.
3. **Corriger une option incompatible.** Le journal montre `unknown argument: --no-context`. L'aide du moteur indique `--max-context N`; le script ultérieur utilise `--max-context 0`. Ne pas réutiliser `--no-context` avec ce binaire.
4. **Comparer de nouvelles versions.** Plusieurs SRT sont fournis, dont un essai très dégradé de 36 208 blocs et une version de 1 604 blocs. Les noms `(1)` et `(2)` sont conservés comme provenance; ils ne prouvent pas à eux seuls un niveau de qualité.
5. **Ajouter des références.** L'utilisateur fournit la même URL YouTube `q6oDYStjuI4`, accepte le M4A et joint l'audio, puis la transcription YouTube. La piste YouTube contient elle aussi des erreurs.
6. **Automatiser en ligne de commande.** `Transcrire-PremaKavali.ps1` extrait l'audio avec FFmpeg, lance Whisper et recale les temps du résultat sur le film. Deux profils figurent dans le script : comparaison (`--max-context 64 --beam-size 8`) et référence (`--max-context 0 --temperature-inc 0 --beam-size 5`). Le premier extrait couvre 0–900 secondes; les SRT relatifs et recalés sont identiques pour ce départ à zéro.
7. **Vérifier 25 passages prioritaires.** `Verifier-25-Passages.ps1` convertit les extraits en WAV mono 16 kHz, transcrit en hindi, recale les temps et produit un CSV. Un journal utilisateur confirme un essai GPU réussi sur 12,2 secondes en environ 7,5 secondes de traitement total, avec une NVIDIA GeForce RTX 4070 et `large-v2.bin`. Ce résultat ponctuel ne garantit pas le temps nécessaire pour tout le film.
8. **Récupérer les résultats de comparaison.** Le CSV joint contient bien 25 lignes; toutes portent `A_VERIFIER_AVEC_AUDIO`. Une nouvelle transcription est donc une hypothèse à comparer, pas une preuve de correction.
9. **Commencer la traduction française.** Le dossier local contient le hindi V7 (1 597 blocs) et le français `FR_001-143` (143 blocs). Le dernier bloc français finit à `00:11:04,930`. Le film entier n'est pas traduit dans ce fichier.
10. **Tenter une traduction automatisée intégrale.** Le paquet local prévoit NLLB, des reprises via `traduction_progression.tsv` et un résultat intitulé `Prema_Kavali_FR_CA_COMPLET_AUTOMATIQUE_A_REVISER.srt`. Le journal joint montre un échec de compilation de `tokenizers` : le composant PyO3 utilisé accepte au plus Python 3.12, alors que Python 3.13 est utilisé. Malgré cela, l'installateur affiche « Installation complete »; ce message ne prouve pas la réussite. Aucun SRT français complet n'a été trouvé dans les dossiers inspectés.
11. **Demander l'achèvement.** Les derniers messages demandent de poursuivre par morceaux et de réunir un SRT complet, jusqu'à 100 %. Ce sont les demandes historiques de l'utilisateur; les pièces récupérées ne permettent pas de confirmer que ce résultat a été obtenu.

## État vérifié des fichiers principaux

Les chiffres sont calculés avec le validateur du dépôt actuel; ils ne mesurent pas l'exactitude linguistique.

| Version | Blocs | Erreurs techniques | Avertissements | Observation |
| --- | ---: | ---: | ---: | --- |
| Original du dépôt actuel | 932 | 17 | 555 | Toujours préservé |
| Correction textuelle de la branche actuelle | 932 | 17 | 567 | 604 blocs modifiés, sans validation audio |
| Pièce jointe `(1).srt` | 36 208 | 6 360 | 75 094 | Essai fortement dégradé; ne pas choisir comme base |
| Pièce jointe `(2).srt` | 1 604 | 16 | 789 | Autre découpage du film |
| Hindi V7 local | 1 597 | 1 | 785 | 48 caractères de remplacement; bloc 926 non chronologique |
| Piste `.hindi.srt` | 1 695 | 0 | 2 009 | Format valide, mais nombreuses incohérences possibles |
| Comparaison 0–900 s | 232 | 0 | 238 | Extrait seulement |
| Français `001-143` | 143 | 0 | 109 | Traduction partielle et non validée |

Les 1 597 blocs de V7 ne correspondent pas aux numéros des 932 blocs du dépôt actuel. Par exemple, le bloc 485 du contrôle sur 25 passages se situe vers 35 min, alors que le bloc 485 du SRT actuel se situe vers 57 min. Il faudra rapprocher les versions par **horodatage et contenu**, jamais par numéro seul. Plus de blocs ou moins d'erreurs de format ne suffit pas à établir qu'une version transcrit mieux les dialogues.

## Ce que cela change pour la suite

L'audio et les outils locaux retrouvés lèvent le manque de sources de la première passe textuelle. Les chemins du binaire Whisper cuBLAS et du modèle large-v2 mentionnés dans les journaux ont été vérifiés : les deux fichiers sont présents. Le fonctionnement actuel du GPU n'a pas été retesté pendant cet import.

La suite utile consiste à comparer le V7, le SRT corrigé de 932 blocs et les résultats des 25 extraits, à partir des temps du film; utiliser l'audio pour retranscrire les passages douteux; corriger les durées et doublons; puis reprendre les 143 blocs français existants et compléter la traduction. Une vérification complète doit aussi examiner les portions sans sous-titre et distinguer dialogues, chansons et silence.

La correction actuelle du dépôt et la proposition GitHub n'ont pas été remplacées pendant cette récupération. Les 143 blocs français retrouvés sont maintenant archivés dans la branche, sous `subtitles/fr-CA/recovered/`; ils ne constituent pas une traduction complète.
