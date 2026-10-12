# Feuille de route — Prema Kavali en français québécois

Mise à jour : 12 octobre 2026. Cette feuille de route décrit le travail restant; une case non cochée n'est pas une action déjà réalisée. Les étapes sont ordonnées selon leurs dépendances, sans date de livraison promise.

**Prochaine action : tester le moteur Whisper GPU retrouvé sur un extrait connu, puis comparer les versions hindi sur les 25 passages prioritaires avant de choisir une base de travail.**

## Point de départ

- [x] Préserver le SRT hindi initial de 932 blocs et la capture des réglages.
- [x] Documenter les outils, procédures, droits et limites.
- [x] Produire une première correction textuelle : 604 blocs modifiés, sans validation à l'écoute.
- [x] Ajouter le validateur SRT, les journaux avant/après et les contrôles d'intégrité.
- [x] Récupérer l'audio, le hindi V7 de 1 597 blocs, les résultats de comparaison et 143 blocs français.
- [x] Publier les documents et fichiers textuels récupérés sur la branche `correction-srt-hindi` et dans la [proposition no 1](https://github.com/steveprudhomme/PremaKavaliFrenchSubtitle-/pull/1).

À résoudre : 607 blocs signalés pour écoute dans la première révision; 17 durées nulles ou négatives dans cette version; 48 caractères de remplacement et une erreur de chronologie dans V7. Les 143 blocs français s'arrêtent à `00:11:04,930`. Ces chiffres appartiennent à des versions distinctes : ils ne s'additionnent pas et ne donnent pas un pourcentage de traduction achevée.

## 1. Confirmer les sources et le fonctionnement des outils — priorité immédiate

- [ ] Fixer la copie audio/vidéo de référence : URL, empreinte, durée et éventuelles différences de montage; vérifier la correspondance au début, au milieu et à la fin.
- [ ] Relever les versions réellement installées de Subtitle Edit, Whisper CPP, FFmpeg et du modèle large-v2; conserver les paramètres et journaux.
- [ ] Tester le binaire Whisper cuBLAS déjà présent sur un des 25 extraits connus; confirmer l'usage du GPU et le résultat produit. La présence des fichiers ne prouve pas leur bon fonctionnement actuel.
- [ ] Employer les options acceptées par ce binaire, notamment `--max-context`; ne pas réintroduire `--no-context`, qui a échoué dans l'essai historique.
- [ ] Faire écrire les nouveaux essais dans un dossier distinct des archives, avec possibilité de reprise sans écrasement.

**Critère de fin :** une référence audiovisuelle identifiée et un essai de transcription reproductible, avec résultat et journal conservés. Le texte généré reste une hypothèse, à confronter à l'audio.

## 2. Comparer les versions et choisir la base hindi

Prérequis : étape 1.

- [ ] Comparer l'original, sa correction textuelle, V7 et les transcriptions de comparaison sur les 25 passages prioritaires, ainsi que sur des scènes calmes, chansons et changements de locuteur.
- [ ] Aligner par **horodatage et contenu**, jamais par numéro de bloc : les découpages de 932 et 1 597 blocs sont différents.
- [ ] Construire un tableau de correspondance indiquant source, temps, texte proposé, divergence et décision à l'écoute.
- [ ] Choisir une base de travail en fonction de la fidélité aux paroles, de la couverture et de la synchronisation; ne pas choisir uniquement selon le nombre de blocs ou d'erreurs techniques.
- [ ] Créer une nouvelle version de travail et documenter ce choix, sans modifier les sources archivées.

**Critère de fin :** base choisie avec justification, correspondances établies et divergences conservées pour la révision. Les 25 passages servent au diagnostic; ils ne valident pas le film entier.

## 3. Réviser le hindi avec l'audio et vérifier la couverture complète

Prérequis : étape 2. Procéder par lots temporels, avec un point de reprise et un journal pour chacun.

- [ ] Traiter en priorité les mots tronqués, caractères `�`, répétitions suspectes et passages incompréhensibles; rapprocher les 607 signalements du découpage retenu.
- [ ] Retranscrire les extraits douteux avec un peu de contexte avant/après, puis arbitrer les divergences à l'écoute; ne pas accepter automatiquement une seconde sortie Whisper.
- [ ] Faire contrôler les paroles par une personne comprenant le hindi; préserver les accents et tournures dialectales justifiés.
- [ ] Réviser orthographe, grammaire, ponctuation, noms propres, locuteurs et phrases réparties sur plusieurs blocs.
- [ ] Examiner toute la durée du film, y compris les zones sans sous-titre, et distinguer dialogues manquants, chansons, musique et silence.
- [ ] Définir et appliquer une convention pour les chansons, voix hors champ et indications sonores utiles.
- [ ] Consigner les passages non résolus sans inventer de dialogue; retirer les marqueurs provisoires uniquement lorsqu'ils sont résolus ou remplacés par une indication éditoriale justifiée.

**Critère de fin :** toute la durée a été examinée, les dialogues et chansons retenus sont couverts, chaque anomalie a une décision documentée et aucun passage n'est présenté comme confirmé sans preuve d'écoute.

## 4. Corriger la synchronisation et la lisibilité du hindi

À effectuer au fil de l'étape 3, puis vérifier sur le fichier assemblé.

- [ ] Résoudre les durées nulles/négatives présentes dans la base retenue; les 17 erreurs du fichier initial doivent être rapprochées des scènes, sans allongement arbitraire.
- [ ] Résoudre l'anomalie de chronologie du bloc 926 de V7 si ce passage est repris; conserver sa référence historique dans le journal.
- [ ] Supprimer ou fusionner les doublons confirmés, corriger les chevauchements non intentionnels et vérifier les frontières entre lots.
- [ ] Ajuster entrées/sorties et coupures de lignes; examiner les avertissements de longueur, durée et vitesse en tenant compte du devanagari.
- [ ] Renuméroter seulement la version de travail assemblée et conserver les correspondances avec les sources.
- [ ] Exécuter le validateur sur le fichier entier, puis vérifier la synchronisation au visionnement.

**Critère de fin :** zéro erreur structurelle sur la version de travail, avertissements résolus ou justifiés, et synchronisation vérifiée. Les archives conservent leurs défauts historiques.

## 5. Produire la traduction complète en français québécois

Prérequis : hindi validé pour chaque lot des étapes 3–4. Des lots validés peuvent être traduits avant la fin de la révision du film, mais la traduction finale attend la validation de l'ensemble.

- [ ] Réviser les 143 blocs français récupérés contre le hindi retenu et l'audio; rétablir les correspondances après tout changement de découpage.
- [ ] Compléter le [glossaire](subtitles/fr-CA/glossaire.csv) et le [suivi](subtitles/fr-CA/suivi.csv) : noms, parenté, tutoiement/vouvoiement, termes culturels et choix récurrents.
- [ ] Traduire les passages restants par lots, dans un français naturel au Québec, sans effacer le contexte culturel indien.
- [ ] Faire relire le sens par une personne comprenant le hindi, puis le registre et la fluidité par une personne maîtrisant le français québécois.
- [ ] Assembler les lots dans `subtitles/fr-CA/prema-kavali.fr-CA.draft.srt`; contrôler oublis, doublons et continuité aux raccords.

**Option seulement si une traduction automatique locale est retenue :**

- [ ] Corriger l'installateur historique : sélectionner explicitement Python 3.11 ou 3.12 selon les dépendances retenues, vérifier les codes de sortie et les imports, arrêter sur échec.
- [ ] Valider l'installation sur un petit lot avant de lancer tout le film; conserver la progression et vérifier la reprise après interruption.
- [ ] Vérifier les conditions d'utilisation et la licence du modèle choisi. Traiter toute sortie NLLB comme un brouillon en français à réviser et à adapter au Québec.

L'automatisation n'est pas un préalable à la traduction manuelle et ne résout pas un hindi source incertain. Le journal historique montre un échec sous Python 3.13; il ne justifie pas de relancer l'ancien installateur tel quel.

**Critère de fin :** tous les passages retenus sont traduits et relus, le glossaire est cohérent, et aucune portion non traduite n'est dissimulée derrière des marqueurs provisoires.

## 6. Contrôle final sur le film entier

Prérequis : étapes 3–5 terminées.

- [ ] Contrôler le SRT français : UTF-8, numérotation, horodatages, ordre, durée et texte non vide.
- [ ] Ajuster les retours à la ligne et la vitesse de lecture; appliquer les repères du [guide fr-CA](docs/traduction-fr-CA.md), avec exceptions motivées si nécessaire.
- [ ] Visionner le film entier avec le SRT français sur la copie de référence, puis tester son ouverture dans Subtitle Edit et un lecteur vidéo.
- [ ] Vérifier noms, accents, apostrophes, ponctuation, locuteurs et chansons; résoudre tous les points du suivi.
- [ ] Produire un rapport final précisant la copie compatible, les contrôles réalisés, les personnes ayant révisé et les limites éventuelles.

**Critère de fin :** zéro erreur technique, avertissements examinés, aucun doute éditorial non résolu, et visionnement intégral effectué. Un validateur sans erreur ne remplace pas ce visionnement.

## 7. Finaliser et publier une version identifiée

Prérequis : étape 6.

- [ ] Vérifier les conditions de diffusion applicables aux sous-titres et à la traduction; la licence du dépôt ne confère pas de droits sur le film.
- [ ] Mettre à jour README, provenance, documentation, inventaires et journal des changements pour refléter les fichiers réellement validés.
- [ ] Garder les archives immuables; adapter les contrôles d'intégrité pour distinguer les anciennes références de la nouvelle version finale.
- [ ] Finaliser la proposition GitHub, la faire relire et la fusionner lorsque le périmètre est prêt. La documentation peut être intégrée séparément si son statut provisoire reste explicite.
- [ ] Publier un SRT français identifié et un rapport de validation avec une version/tag, sans joindre l'audio, la vidéo ou les modèles.
- [ ] Mettre en place le signalement des corrections ultérieures avec horodatage, version concernée et description du problème.

**Critère de fin :** version téléchargeable, documentation concordante et historique traçable. Le terme « complet » exige la couverture vérifiée du film, pas simplement un fichier qui atteint son dernier horodatage.

## Suivi de l'avancement

Pour chaque lot, consigner début/fin, version source, statut de l'écoute, validation hindi, traduction, relecture française et problèmes restants. Les pourcentages éventuels doivent mesurer séparément ces étapes sur une durée de référence fixe; un pourcentage unique fondé sur les blocs serait trompeur lorsque le découpage change.

Cocher une tâche uniquement après sa réalisation et l'ajout de sa preuve : rapport, journal, fichier révisé ou commit. L'[historique des étapes réalisées](docs/etapes-realisees.md) décrit les actions passées; cette feuille de route décrit la suite.
