# Prema Kavali — sous-titres en français québécois

Projet communautaire de préparation de sous-titres **français québécois (`fr-CA`)** pour la version doublée en hindi de *Prema Kavali*. Selon le créateur du projet, aucune version française correspondant à sa copie n'a été trouvée; ce dépôt ne prétend pas établir leur inexistence.

## Origine et état du projet

Steve Prud'Homme indique avoir téléchargé sa copie YouTube avec **JDownloader**, puis produit une première transcription hindi dans **Subtitle Edit**, avec **Whisper CPP**. Le SRT et la capture fournis sont archivés ici. La vidéo n'est pas distribuée.

**Version initiale automatique : 932 blocs, 17 erreurs de durée et 555 avertissements techniques.** Une [première correction textuelle du hindi](subtitles/hi/revised/prema-kavali.hi.revised.srt) est disponible : orthographe, syntaxe locale, typographie et corrections de transcription déduites du contexte. **Elle n'est pas validée à l'écoute et n'est pas une version finale.** La récupération de la conversation « Vérifier le sous-titrage » a ensuite apporté un [hindi V7 de 1 597 blocs](subtitles/hi/recovered/prema-kavali.hi.v7.srt) et une [traduction française partielle de 143 blocs](subtitles/fr-CA/recovered/prema-kavali.fr.001-143.draft.srt), jusqu'à `00:11:04,930`. Aucune traduction française complète n'est disponible. Le contrôle du format ne garantit ni l'exactitude du hindi ni la synchronisation avec le film.

- [SRT hindi initial — copie exacte](subtitles/hi/original/prema-kavali.hi.v1.srt)
- [Capture des réglages](docs/images/subtitle-edit-whisper-cpp.png)
- [Provenance et empreintes](docs/provenance.json)
- [Rapport lisible de validation](reports/validation-hi-v1.md) et [détails JSON](reports/validation-hi-v1.json)
- [Bilan de correction textuelle](reports/revision-hi.md), [modifications avant/après](reports/corrections-hi-v1.csv) et [passages à vérifier à l'écoute](reports/a-verifier-audio-hi.csv)
- [Toutes les étapes réalisées, méthodes et limites](docs/etapes-realisees.md)
- [Reprise de « Vérifier le sous-titrage »](docs/historique/reprise-verifier-sous-titrage.md) et [messages accessibles](docs/historique/verifier-sous-titrage-messages.md)
- [Archives récupérées et inventaire](archives/recuperation/README.md), [scripts historiques](scripts/historique/README.md) et [reproduction de la correction](docs/reproduire-correction.md)

## Parcours recommandé

1. Installer les outils : [prérequis Windows](docs/prerequis.md).
2. Préparer une copie autorisée et reproduire la transcription : [JDownloader et Subtitle Edit](docs/procedure.md).
3. Réviser une copie du hindi à l'écoute, sans modifier l'archive initiale.
4. Traduire selon le [guide français québécois](docs/traduction-fr-CA.md).
5. Exécuter les [contrôles SRT](docs/validation.md), puis visionner le film avec les sous-titres.

```text
docs/                         Prérequis, procédure, provenance et capture
docs/historique/               Reprise et messages accessibles de l'autre conversation
archives/recuperation/         Documents et résultats historiques, avec inventaires
scripts/validate_srt.py        Contrôle local sans dépendances Python
scripts/reproduire_correction_hi.py  Reproduction de la correction textuelle
scripts/historique/            Anciens scripts conservés, limitations documentées
subtitles/hi/original/         Source initiale immuable
subtitles/hi/revised/          Première correction textuelle, à vérifier à l'écoute
subtitles/hi/recovered/        Hindi V7 récupéré; découpage différent de l'original
subtitles/fr-CA/               Glossaire, suivi et 143 blocs français récupérés
reports/                      Constats sur le fichier initial
media/                        Vidéo locale seulement (ignorée par Git)
```

## Validation rapide

Depuis la racine du dépôt, avec Python 3.10 ou plus récent :

```powershell
python scripts/validate_srt.py subtitles/hi/original/prema-kavali.hi.v1.srt
```

Le code de sortie **1 est attendu sur l'archive initiale**, car elle contient 17 blocs de durée nulle ou négative. Voir la documentation pour les rapports et le mode strict. L'archive est protégée contre la conversion automatique des fins de ligne par `.gitattributes`.

## Contributions et droits

Consulter [CONTRIBUTING.md](CONTRIBUTING.md) avant de proposer une correction. Ne pas ajouter de vidéo, piste audio ou modèle Whisper au dépôt.

La [licence GPL-3.0 déjà présente](LICENSE) est conservée. Elle ne concède aucun droit sur le film, ses dialogues, la musique ou les autres éléments de tiers. Consulter [les précisions sur les droits](docs/droits.md). La publication de cette transcription ne prouve pas l'autorisation des ayants droit.

L'audio du film, les extraits, les modèles et les archives binaires contenant potentiellement des médias restent locaux. Leur présence est consignée dans l'inventaire; les documents et résultats textuels utiles sont publiés séparément. Les chemins personnels des historiques publiés ont été neutralisés.
