# Prérequis et installation

Guide orienté Windows, comme la capture fournie. Les versions exactes utilisées pour la première transcription ne sont pas connues. Les pages officielles ci-dessous ont été consultées le 10 octobre 2026; conserver les numéros des versions installées pour les prochains essais.

| Outil | Installation et usage |
| --- | --- |
| JDownloader 2 | Télécharger l'installateur Windows depuis la [page officielle](https://jdownloader.org/download/index), de préférence le lien sans offres logicielles facultatives, puis suivre l'assistant. Lancer et laisser terminer les mises à jour. |
| Subtitle Edit | Choisir un paquet Windows adapté à l'ordinateur dans les [versions officielles](https://github.com/SubtitleEdit/subtitleedit/releases). Installer ou extraire le paquet selon son format. Suivre les exigences du paquet sélectionné et vérifier la lecture d'une vidéo. |
| Whisper CPP et modèle multilingue | Dans la fenêtre de transcription de Subtitle Edit, sélectionner Whisper CPP et télécharger le moteur/modèle lorsque proposé. Le modèle `large` de la capture occupe environ 3,1 Go sur disque. Il ne faut pas choisir un modèle anglais uniquement. |
| Lecture et extraction audio | Utiliser les composants proposés par Subtitle Edit pour la vidéo et FFmpeg si l'application les demande. [FFmpeg officiel](https://ffmpeg.org/download.html) propose des liens vers les compilations Windows. Si une installation manuelle est nécessaire, extraire l'archive et ajouter son dossier `bin` au PATH; vérifier avec `ffmpeg -version`. |
| Python 3.10+ | Installer depuis [python.org](https://www.python.org/downloads/windows/), activer l'accès en ligne de commande selon l'installateur, rouvrir PowerShell et exécuter `python --version`. Le validateur n'utilise que la bibliothèque standard : aucun `pip install` requis. |
| Git (pour contribuer) | Installer [Git pour Windows](https://git-scm.com/downloads/win), puis vérifier `git --version`. Un compte et des droits GitHub sont nécessaires pour pousser directement. |

Le projet Subtitle Edit indique actuellement Windows 10 22H2 ou plus récent et des distributions autonomes ne nécessitant pas d'installation .NET séparée. Vérifier les exigences de la version choisie dans son [README officiel](https://github.com/SubtitleEdit/subtitleedit).

Prévoir un processeur 64 bits, de l'espace pour la vidéo, les extractions temporaires et le modèle, ainsi que de la mémoire au-delà de la seule taille du modèle. **16 Go de RAM constituent un repère pratique proposé ici, pas un minimum garanti par l'éditeur.** Le CPU suffit pour reproduire la capture; le traitement d'un long film peut être lent. Ne pas promettre une durée d'exécution. Si le modèle est trop lourd, essayer un modèle multilingue plus petit dans un nouvel essai documenté.

Pour obtenir le dépôt :

```powershell
git clone https://github.com/steveprudhomme/PremaKavaliFrenchSubtitle-.git
cd PremaKavaliFrenchSubtitle-
python --version
```

Aucune installation ni retranscription n'est nécessaire pour consulter le SRT fourni.
