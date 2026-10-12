# Comment le projet a été constitué, étape par étape

Ce journal documente le travail effectué dans la conversation courante et les travaux antérieurs récupérés. Il distingue les actions réalisées, les déclarations de provenance, les essais historiques et ce qui reste à faire.

## 1. Récupération de la demande initiale et des pièces jointes

La conversation « Créer dépôt Github subtitles » a fourni le SRT hindi de 932 blocs et la capture de Subtitle Edit. Le créateur déclare avoir obtenu sa copie YouTube avec JDownloader et transcrit le hindi dans Subtitle Edit. Aucun téléchargement du film n'a été refait pendant la création du dépôt.

Le SRT et la capture ont été copiés sans modification; leurs empreintes figurent dans `docs/provenance.json`. Le nom du SRT a été simplifié pour le dépôt. `.gitattributes` empêche Git de convertir les fins de ligne des SRT archivés.

## 2. Examen des réglages initiaux

La capture initiale indique Whisper CPP, CPU, Hindi, `large (3.1 GB)`, traduction anglaise désactivée, post-traitement activé et `--max-context 0 --suppress-nst --no-speech-thold 0.70`. La variante précise de large et les versions logicielles ne sont pas visibles. Voir la [procédure](procedure.md).

## 3. Construction du dépôt documenté

Le dépôt GitHub existant a été cloné. Sa licence GPL-3.0 a été conservée. README, prérequis, procédure JDownloader/Subtitle Edit, droits, guide de traduction québécoise et règles de contribution ont été créés. Les répertoires distinguent original, révision hindi et traduction française.

Les sites officiels de JDownloader, Subtitle Edit et whisper.cpp ont servi aux liens et aux prérequis; les paramètres du projet proviennent des captures et journaux, sans prétendre identifier une version logicielle absente.

## 4. Validation de l'original

Un [validateur Python](../scripts/validate_srt.py) sans dépendance a été ajouté : UTF-8, numérotation, syntaxe des temps, durées, ordre chronologique, chevauchements et repères de lisibilité. Il ne modifie pas le fichier. Huit cas de contrôle ciblés ont été exécutés : fichier valide, fichier vide, UTF-8 invalide, durée nulle, mauvais numéro, mauvais horodatage, chevauchement et BOM avec fins de ligne Windows.

Résultat : 932 blocs, 17 erreurs (6 durées nulles, 11 négatives de 12 ms), 555 avertissements. Les rapports conservent les numéros concernés. Les comptages en points de code Unicode ne mesurent pas précisément la lisibilité du devanagari. La publication initiale est le commit `9b48c67` sur `main`.

## 5. Première correction textuelle

Le texte des 932 blocs a été examiné. Les corrections proposées portent sur orthographe, formes grammaticales évidentes, typographie, mots reconnaissables dans le contexte et ponctuation de phrases suffisamment claires. Les dialogues indéchiffrables n'ont pas été reconstruits. Les répétitions et caractères tronqués restent signalés lorsqu'une correction fiable exige l'audio.

Résultat : 604 blocs modifiés, 1 011 opérations consignées. L'original, les numéros et les horodatages sont conservés. Le journal avant/après et la liste de 607 blocs à écouter ont été vérifiés contre les fichiers. La correction conserve 17 erreurs temporelles et présente 567 avertissements. Voir le [bilan](../reports/revision-hi.md) et la [reproduction](reproduire-correction.md).

## 6. Vérification de la référence YouTube

L'utilisateur a donné [cette vidéo](https://www.youtube.com/watch?v=q6oDYStjuI4). Ses métadonnées indiquent RKD Studios, publication le 8 mai 2020, durée de 6 737 secondes. Un outil temporaire yt-dlp a permis de récupérer les métadonnées et les pistes automatiques hindi, sans téléchargement de la vidéo.

La piste `hi-orig` a été examinée sur plusieurs passages : elle présente aussi des erreurs manifestes. Elle n'a pas remplacé le SRT. Elle a servi d'indice supplémentaire au bloc 45, avec une correction contextuelle proposée. Aucun contrôle intégral par écoute n'a été effectué. Le service Pinokio n'était pas accessible lors de cette recherche d'outils.

## 7. Publication de la première révision

Une branche `correction-srt-hindi` et la [proposition GitHub no 1](https://github.com/steveprudhomme/PremaKavaliFrenchSubtitle-/pull/1) en brouillon ont été créées. Le commit `744716a` contient la première correction et ses rapports. Le connecteur GitHub refusait la création de la proposition; l'authentification Git déjà autorisée a permis de la créer via l'API. Aucun identifiant n'a été enregistré dans le dépôt.

## 8. Récupération de « Vérifier le sous-titrage »

Les cinq pages du connecteur ont livré 48 tours accessibles et 10 pièces jointes. Les réponses de l'assistant n'étaient pas exposées en clair. Les dossiers locaux explicitement liés aux journaux ont été inspectés, puis leurs documents et résultats copiés dans une archive locale : 134 fichiers vérifiés par empreinte; 25 SRT supplémentaires extraits du ZIP Whisper; 88 références SRT inventoriées, doublons inclus.

L'audio M4A retrouvé a été identifié par FFmpeg : 1 h 52 min 17,04 s, AAC stéréo à 44,1 kHz. Cela confirme la présence du fichier, pas une écoute du contenu. Le binaire Whisper cuBLAS et le modèle `large-v2.bin` indiqués dans les journaux sont présents. Leur fonctionnement actuel sur GPU n'a pas été retesté.

Voir le [récit détaillé](historique/reprise-verifier-sous-titrage.md) pour le passage au GPU, l'erreur `--no-context`, les essais de 15 minutes, le contrôle de 25 extraits et l'échec d'installation de la traduction automatique.

## 9. Intégration des travaux récupérés

À la demande de l'utilisateur, les documents, scripts, journaux et SRT sont ajoutés à la même branche. L'inventaire fait correspondre 159 références locales à 99 fichiers d'archive distincts (104 références publiées); les 55 autres références concernent l'audio et les archives binaires conservés localement. Les SRT et images sont intacts; certains documents textuels sont normalisés et leurs chemins personnels neutralisés.

Les versions utiles sont aussi placées à des emplacements lisibles : hindi V7 sous `subtitles/hi/recovered/`, français partiel sous `subtitles/fr-CA/recovered/`, anciens paquets sous `scripts/historique/`. Les copies doublonnées sont intentionnelles pour préserver les noms attendus par les scripts historiques. Leurs limitations sont documentées; aucun installateur ancien n'a été relancé.

Le script de reproduction a été exécuté et reproduit exactement l'empreinte de la correction déjà publiée. Pour contrôler les empreintes d'archives, les 604 changements avant/après, l'alignement des 143 blocs français et les liens documentaires :

```powershell
python scripts/verifier_publication.py
```

Ce contrôle d'intégrité ne remplace ni le validateur SRT ni la révision audio. Il attend les versions archivées précises; après une nouvelle révision éditoriale, mettre à jour les références attendues de manière explicite.

## 10. État réel et prochaines étapes

Le projet contient une correction textuelle de 932 blocs, un V7 distinct de 1 597 blocs, plusieurs transcriptions de comparaison et 143 blocs français. **Aucune version n'est certifiée fidèle à l'audio; aucune traduction française intégrale n'a été trouvée ou produite.**

Il reste à aligner les versions par temps et contenu, utiliser l'audio pour résoudre les passages douteux et les paroles manquantes, corriger la synchronisation, comparer les 143 traductions au hindi retenu, compléter le français québécois et visionner l'ensemble. Ne pas fusionner les variantes en se basant sur les seuls numéros de blocs.
