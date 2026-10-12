# Archives récupérées

Ce dossier conserve les éléments retrouvés dans la conversation « Vérifier le sous-titrage », ses pièces jointes et les dossiers locaux associés. Ils documentent les essais antérieurs, y compris leurs échecs; ils ne sont pas tous de bonne qualité.

- [Inventaire de publication](inventaire-publication.csv) : 159 références, dont 104 références publiées sous **99 fichiers distincts**, et 55 références conservées uniquement en local (audio et archives binaires).
- [Inventaire des SRT](inventaire-srt.csv) : 88 références, doublons inclus, avec nombre de blocs, erreurs, avertissements, premiers/derniers temps et empreintes.
- [Récit de la récupération](../../docs/historique/reprise-verifier-sous-titrage.md).

Les noms sous `fichiers/` commencent par une partie du SHA-256 source. Les copies de même contenu et de même nom simplifié sont dédupliquées; des fichiers de noms différents peuvent encore avoir la même empreinte. Pour retrouver un fichier, chercher son nom historique dans la colonne `source_archive_locale`, puis ouvrir `fichier_depot`. Le numéro de version dans un nom n'est pas une garantie de qualité.

Les SRT et les images sont conservés octet pour octet. Les chemins de profil Windows dans les documents textuels utilisent maintenant `C:\Users\UTILISATEUR`; le BOM et les fins de ligne de ces documents peuvent aussi changer. Les deux empreintes sont indiquées. Aucun contenu manquant n'a été reconstruit.

Les scripts de ce dossier sont des copies d'archive : les noms et voisins nécessaires à leur exécution peuvent avoir changé. Des paquets avec leur structure utile sont conservés sous [scripts/historique](../../scripts/historique/README.md), avec leurs avertissements. Ne pas lancer les fichiers d'archive au hasard.

Les fichiers audio, modèles et ZIP contenant potentiellement des médias ne sont pas distribués. Leurs empreintes dans l'inventaire documentent ce qui a été retrouvé. L'archive locale complète reste disponible dans le dossier de travail de l'utilisateur.
