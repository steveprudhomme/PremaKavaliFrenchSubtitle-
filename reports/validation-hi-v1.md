# Validation de la version hindi initiale

Contrôle du 10 octobre 2026, effectué sur le fichier archivé sans modification.

- Encodage : UTF-8 avec BOM.
- Taille : 162935 octets.
- Nombre de blocs : 932.
- Dernière fin de sous-titre : 01:52:17,012. Cela ne prouve pas la durée ni la couverture complète du film.
- Erreurs : **17 blocs de durée non positive : 6 nuls et 11 négatifs (−12 ms)**, tous confirmés par comparaison de leurs horodatages.
- Avertissements : **555 occurrences**, pouvant se cumuler dans un même bloc.
- SHA-256 : `ae46c4d9c95ffdbdb12f5df07c1d5867227caf0d87cb4305e220a0b7851e8682`.

| Bloc | Début | Fin | Constat |
| --- | --- | --- | --- |
| 178 | 00:21:58,600 | 00:21:58,588 | Durée négative (−12 ms) |
| 179 | 00:21:58,612 | 00:21:58,612 | Durée nulle |
| 182 | 00:22:05,600 | 00:22:05,588 | Durée négative (−12 ms) |
| 205 | 00:26:52,600 | 00:26:52,588 | Durée négative (−12 ms) |
| 206 | 00:26:52,612 | 00:26:52,612 | Durée nulle |
| 249 | 00:31:49,660 | 00:31:49,648 | Durée négative (−12 ms) |
| 250 | 00:31:49,672 | 00:31:49,672 | Durée nulle |
| 317 | 00:39:06,200 | 00:39:06,188 | Durée négative (−12 ms) |
| 472 | 00:54:14,740 | 00:54:14,728 | Durée négative (−12 ms) |
| 514 | 01:00:45,820 | 01:00:45,808 | Durée négative (−12 ms) |
| 515 | 01:00:45,832 | 01:00:45,832 | Durée nulle |
| 518 | 01:00:53,540 | 01:00:53,528 | Durée négative (−12 ms) |
| 519 | 01:00:53,552 | 01:00:53,552 | Durée nulle |
| 738 | 01:25:52,860 | 01:25:52,848 | Durée négative (−12 ms) |
| 739 | 01:25:52,872 | 01:25:52,872 | Durée nulle |
| 781 | 01:30:14,040 | 01:30:14,028 | Durée négative (−12 ms) |
| 913 | 01:49:50,960 | 01:49:50,948 | Durée négative (−12 ms) |

| Avertissement | Occurrences |
| --- | --- |
| Durée hors repère 1–7 secondes | 126 |
| Ligne de plus de 42 caractères | 263 |
| Répétition possible : vérifier à l'écoute | 56 |
| Vitesse supérieure à 20 caractères/seconde | 110 |

Les répétitions sont des indices à écouter, pas des erreurs linguistiques confirmées. Les seuils de longueur et de vitesse sont indicatifs, surtout en devanagari. Aucune vérification audio, traduction ou révision linguistique complète n'a été effectuée; la vidéo n'est pas jointe.

Le validateur termine donc avec le code **1**, ce qui est attendu pour cette archive. Le SRT initial n'a pas été corrigé. Les corrections devront être conservées dans une nouvelle version sous `subtitles/hi/revised/`.

Voir les [détails par bloc](validation-hi-v1.json) et les [commandes de validation](../docs/validation.md).
