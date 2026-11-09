# Issue #3 — Étape 2 : parcours et architecture de l’information

**Statut :** parcours approuvé par le demandeur ; identification de l’image cible explicitement reportée

Cette architecture cible la personne responsable de l’abonnement Azure et de la VM après son instanciation depuis Microsoft Marketplace. Le parcours suppose que le client a terminé l’action de déploiement dans Azure ; il ne présume ni que l’offre est actuellement publiée, ni d’un titre Marketplace, plan, SKU, version d’image, choix réseau ou service Azure déjà activé.

La documentation sera bilingue anglais-français. Les noms de fichiers ci-dessous définissent la structure approuvée ; leur présence dans la branche de travail ne constitue pas une publication. Tout comportement particulier à l’offre doit être vérifié sur l’image Marketplace retenue avant de devenir une instruction.

## Parcours approuvé

À la demande du lecteur, un quick-start anglais (`QUICKSTART.md`) complète l’accueil : cinq étapes synthétiques jusqu’au premier test de connexion applicative, liens vers les guides détaillés et arrêt explicite devant une procédure propre à l’image non vérifiée. Il ne remplace ni les sept guides ni la préparation à la production. Sa traduction fait partie de l’étape 4.

| Ordre | Question de l’opérateur | Sujet et résultat attendu | Page proposée | Critères couverts |
|---|---|---|---|---|
| 1 | Le déploiement Azure est-il terminé et la VM est-elle prête ? | Vérifier les informations de déploiement visibles dans Azure, distinguer état de la ressource et état du service, relever les données de l’instance sans exposer de secrets, reconnaître un échec et savoir quoi collecter. Les indicateurs et chemins propres à l’image restent à vérifier. | `docs/01-verify-deployment.md` | Structure et tâches actionnables ; responsabilités distinctes ; vérification des faits et dépannages |
| 2 | Comment administrer la VM sans exposer inutilement l’accès ? | Expliquer les rôles et accès Azure, les principes d’accès réseau restreint et la vérification des règles effectives. Ne recommander ni port, ni source autorisée spécifique au produit avant confirmation du plan et de l’image publiés. | `docs/02-secure-azure-access.md` | Responsabilités ; sources Microsoft ; aucune valeur non vérifiée |
| 3 | Comment effectuer le premier accès Keycloak et retirer l’accès temporaire ? | Présenter les identifiants initiaux, le changement vers un accès administrateur durable, la suppression de l’accès temporaire et le traitement sûr des secrets, uniquement selon le parcours confirmé sur l’image cible. | `docs/03-complete-initial-access.md` | Procédure vérifiée ; sécurité ; dépannage |
| 4 | Comment donner une adresse stable et activer TLS de confiance ? | Guider la préparation DNS, la configuration du nom d’hôte, le certificat, les prérequis réseau et la vérification HTTPS. Séparer le comportement intégré à l’image des dépendances DNS/autorité de certification gérées par le client. | `docs/04-configure-domain-and-tls.md` | Mise en service ; responsabilités ; sources officielles |
| 5 | Comment préparer Keycloak pour l’organisation ? | Expliquer les concepts et décisions de configuration nécessaires (realm, comptes ou fédération selon le besoin, clients et URI de redirection), ainsi que le test d’une intégration. Dire explicitement que les applications, annuaires et intégrations ne sont pas inclus dans la VM, sauf preuve commerciale/technique contraire. | `docs/05-configure-keycloak.md` | Limites de l’offre ; tâches opérateur ; documentation officielle Keycloak |
| 6 | Comment exploiter et récupérer l’instance ? | Regrouper les responsabilités courantes : sauvegarde et restauration testée, mises à jour OS et application, surveillance, disponibilité et dépendances, coûts. Distinguer les conseils Azure génériques des options nécessitant une configuration ou un coût client ; ne pas assimiler mise à jour OS et mise à niveau Keycloak/image. | `docs/06-operate-and-recover.md` | Exploitation Azure ; sources Microsoft ; responsabilités et limites |
| 7 | Que faire quand un contrôle échoue, et à qui s’adresser ? | Organiser les symptômes par étape, indiquer les vérifications non destructives, les éléments expurgés à joindre et l’escalade appropriée. Les symptômes, commandes et journaux propres à l’image seront testés avant publication. | `docs/07-troubleshoot-and-get-support.md` | Dépannage ; support ; confidentialité et caviardage |
| Transversal | Quelles sont les limites et précautions de la documentation ? | Conserver une notice de confidentialité et une page de support distinctes, accessibles depuis chaque étape pertinente ; afficher la langue, la date de révision et les avertissements de prépublication selon l’état réel. | `PRIVACY.md`, `PRIVACY-fr.md`, `SUPPORT.md`, `SUPPORT-fr.md` | Bilinguisme ; références publiques ; traitement prudent des données |

L’accueil (`README.md` et `README-fr.md`) devient le point d’entrée : il identifie clairement l’administrateur Azure qui vient de déployer la VM, indique que les pages décrivent le parcours post-déploiement, et renvoie aux sept étapes dans l’ordre. Le contenu ne doit pas présenter une installation Azure ou une intégration d’applications comme déjà réalisée par l’éditeur.

## Principes de navigation et de rédaction

- Organiser les pages par tâche et dans l’ordre réel d’usage, avec titres à l’impératif.
- Si HTTPS de confiance n’est pas encore établi, accomplir les prérequis DNS/TLS de l’étape 4 avant toute saisie d’identifiants à l’étape 3 ; la numérotation n’autorise pas à contourner une alerte de certificat.
- Dans chaque procédure, présenter : objectif, prérequis, étapes, résultat attendu, dépannage/escalade et références applicables.
- Indiquer qui agit : client dans Azure, opérateur de la VM/Keycloak, éditeur ou Microsoft. Ne pas promettre de SLA ou de responsabilité contractuelle non vérifiés.
- Séparer les instructions Azure applicables en général des comportements réellement fournis ou préconfigurés par l’offre.
- Ne pas inscrire de version, nom d’affichage, plan, port, chemin, valeur par défaut, commande client ou fonction d’intégration avant vérification de sa pertinence pour l’image et le parcours de déploiement retenus.
- Maintenir une paire anglaise/française par page, des liens de langue réciproques et des blocs de commandes identiques ; les commandes seront exécutées avant d’être documentées.
- Toute opération pouvant provoquer une perte de données ou une indisponibilité est signalée comme telle et vérifiée uniquement dans un environnement isolé avant publication.

## Correspondance avec les critères d’acceptation

| Critère de l’issue #3 | Réponse prévue dans l’architecture | Preuve attendue aux étapes suivantes |
|---|---|---|
| Nouvelle structure orientée administrateur post-déploiement | Accueil + parcours ordonné en sept pages opérationnelles | Revue de la navigation et des pages finales |
| Prérequis, actions, résultat, dépannage et responsabilités | Modèle de tâche commun à chaque guide ; attribution du responsable dans chaque étape | Relecture opérateur des guides et résolution des ambiguïtés |
| Recommandations reliées à des sources primaires | Références Azure/Keycloak ci-dessous, attachées aux thèmes pertinents | Vérification des liens et de la justesse de chaque recommandation à la rédaction |
| Aucun fait produit supposé | Les valeurs inconnues et les comportements à tester restent des points de validation, pas des instructions | Inventaire d’étape 1, code/configuration et rejeu sur l’image cible |
| Anglais et français cohérents | Une paire de pages EN/FR pour chaque page publiée | Contrôles de liens réciproques et de parité des commandes |
| Procédures rejouées sur l’image retenue | La documentation réserve les instructions propres à l’image jusqu’à la sélection de la cible | Compte rendu avec référence d’image confirmée, date et résultats ; tests isolés pour récupération |
| Sources, rendu et liens vérifiés | Validation prévue après rédaction, sans confondre contrôles sources et rendu publié | Sortie des contrôles, build HTML et vérification des URL après publication autorisée |
| Revue par un opérateur non historique | Parcours sans dépendance aux ADR, Packer ou noms de fichiers internes | Revue de lisibilité et d’exécution par un opérateur Azure |

## Références de conception

Les pages suivantes sont des sources primaires consultées pour cadrer les thèmes. Leur existence ne signifie pas que les services correspondants sont activés, inclus ou configurés dans l’offre.

- Microsoft, [architecture best practices for Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/virtual-machines) : fiabilité, dépendances, séparation des données, disponibilité.
- Microsoft, [writing step-by-step instructions](https://learn.microsoft.com/en-us/style-guide/procedures-instructions/writing-step-by-step-instructions) : titres orientés tâche, instructions numérotées courtes, contexte d’exécution et verbes d’action.
- Microsoft, [Network Security Groups overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) : filtrage Azure par règles réseau.
- Microsoft, [About Azure VM backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction) : périmètre et fonctionnement de la sauvegarde de VM ; ne démontre pas une sauvegarde applicativement cohérente de Keycloak/PostgreSQL pour cette offre.
- Microsoft, [Azure Update Manager overview](https://learn.microsoft.com/en-us/azure/update-manager/overview) : gestion des mises à jour de machines ; la stratégie de mise à niveau du logiciel applicatif demeure à établir séparément.
- Microsoft, [Monitor virtual machines in Azure](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/monitor-vm) : métriques hôte et capacités de surveillance invitée, dont la configuration peut être requise.
- Keycloak, [temporary admin account and recovery](https://www.keycloak.org/server/bootstrap-admin-recovery) : caractère temporaire du compte bootstrap et retrait manuel après acquisition d’un accès administrateur durable.
- Keycloak, [hostname](https://www.keycloak.org/server/hostname) et [reverse proxy](https://www.keycloak.org/server/reverseproxy) : hostname explicite, en-têtes proxy de confiance et risques d’une configuration erronée.

## Limites et dépendances

- Le demandeur indique que l’application n’est pas encore livrée sur Marketplace et que le déploiement est en cours. Les détails de l’offre et la cible d’image restent à confirmer par des données de déploiement effectives.
- Le dépôt documentaire est distinct du dépôt d’ingénierie. Les preuves techniques internes restent dans l’inventaire d’étape 1 et ne deviennent pas des liens client.
- Cette architecture ne constitue pas un parcours exécutable. Aucune commande, valeur de configuration ni procédure de récupération n’est validée par ce document.
- Étape 3 : rédaction anglaise neuve sur cette structure, autorisée par le demandeur sans attendre la sélection d’image. Les comportements propres à l’image restent des points de validation explicites, pas des procédures exécutables.

## Livraison rédactionnelle de l’étape 3 — 2026-11-09

- Dix pages anglaises rédigées à neuf : accueil, sept guides, support et confidentialité. Le français reste l’étape 4.
- Consignes Azure génériques sourcées à proximité des passages concernés ; fonctionnalités amont Keycloak distinguées des capacités réellement configurées dans l’offre.
- Aucun numéro de version, nom commercial final, port, chemin système ou commande propre à l’image ajouté aux guides. Les prérequis, contrôles et critères d’escalade sont rédigés ; les procédures exécutables propres à l’image restent à établir.
- Les noms de services Azure décrivent des options documentées par Microsoft, pas des services déclarés inclus ou actifs.
- Le contact `support@cotechnoe.com` est conservé depuis le cadrage documentaire approuvé et consigné dans le contexte du dépôt d’ingénierie ; aucun SLA, délai de réponse ou mécanisme de transfert confidentiel n’est promis.
- Contrôle ponctuel Python en lecture seule : **réussi**, dix pages, 49 liens relatifs résolus, 28 références HTTPS (19 URL distinctes), sections de prérequis/résultats et listes numérotées présentes dans les sept guides. Aucun exemple de commande exécutable. Ce contrôle ne teste ni le statut HTTP externe, ni le HTML, ni la VM.
- Le dépôt documentaire ne possède pas de Makefile ni de générateur de site sur cette base. Aucun `make check`, build HTML ou test VM n’est revendiqué.
- Aucune modification du code d’image ou des contrôles de certification ; aucun test de certification requis pour qualifier ces changements exclusivement documentaires.
- Ce livrable clôt la rédaction anglaise du brouillon, pas sa qualification opérationnelle ni la publication. La cible reportée empêche encore la validation des procédures propres à l’image ; les étapes 5 à 7 restent ouvertes.

## Livraison de l’étape 4 — 2026-11-09

- Onze traductions françaises ajoutées : accueil, démarrage rapide, confidentialité, assistance et sept guides. Suffixe `-fr.md` ; anglais conservé comme référence.
- Chaque paire possède des liens EN/FR réciproques. Tous les liens de parcours, d’accueil, d’assistance et de confidentialité restent dans la langue choisie. Les URL des sources primaires sont identiques dans les deux langues.
- L’accueil anglais ne présente plus la traduction comme indisponible. Les avertissements de prépublication et les réserves sur les procédures propres à l’image sont conservés ; la traduction ne les qualifie pas.
- Relecture de traduction effectuée contre les pages anglaises : responsabilités, conditions d’arrêt, protection des identifiants, prérequis HTTPS, maintien d’un administrateur fonctionnel et isolement de la restauration conservés. Le terme Keycloak `realm` et les noms de services ne sont pas renommés.
- Contrôle Python ponctuel en lecture seule : **réussi** — onze paires EN/FR, 22 pages publiques, 142 liens locaux résolus ; sélecteurs de langue réciproques, liens internes dans la langue choisie, correspondance ordonnée des liens et sources, parité structurelle des titres, listes, tableaux et avertissements, et numérotation identique.
- Parité des blocs de commandes vérifiée : aucun exemple exécutable dans l’une ou l’autre langue. Aucun contrôle HTTP externe, rendu HTML ou test VM effectué à cette étape.
- Aucun changement du code d’image ou des contrôles de certification. Les étapes 5 à 7 restent ouvertes ; aucun choix d’image ni publication n’est impliqué par cette livraison.

## Validation locale du rendu — étape 6 partielle, 2026-11-09

### Périmètre et méthode

Le demandeur a autorisé la validation du rendu documentaire sans publication. La branche ne contient ni Makefile, ni configuration de site, ni moteur de publication. Le moteur Pandoc déjà installé sur le poste a donc produit un aperçu HTML autonome des 22 pages publiques, hors du dépôt, dans les fichiers de session.

Le lecteur utilisé est `gfm-autolink_bare_uris` : tous les liens documentaires sont explicites ; désactiver les liens automatiques évite que Pandoc imbrique deux liens pour une adresse courriel déjà liée. La sortie est en HTML5 autonome avec langue `en` ou `fr`, titre de page sans duplication du titre principal et liens courriel sans masquage JavaScript. Les destinations `.md` sont remplacées par `.html` uniquement dans l’aperçu. Les sources ne sont pas modifiées.

Un script Python ponctuel a contrôlé l’arbre documentaire Pandoc et le HTML produit. Les ajustements initiaux du validateur concernaient le traitement des courriels, le titre généré et les cases à cocher de Pandoc ; ils n’ont révélé aucun défaut à corriger dans les pages Markdown.

### Résultats

| Contrôle | Résultat et portée |
|---|---|
| Génération HTML locale | **Réussie :** 22 pages, onze paires EN/FR. Ce n’est pas le build du futur site. |
| Structure | **Réussie :** langue HTML correcte, un titre principal par page, identifiants uniques, titres de section et tableaux conservés ; structure HTML des paires EN/FR identique. |
| Tableaux et listes de contrôle | **Réussie :** dix tableaux et dix cases non cochées rendus, en correspondance avec les sources. |
| Liens locaux dans le rendu | **Réussie :** 142 liens résolus vers les fichiers HTML générés ; ordre et destinations conservés après transformation des extensions. |
| Navigation bilingue | **Réussie :** sélecteurs de langue réciproques et navigation dans la langue choisie, sauf changement volontaire de langue. |
| Avertissements | **Réussie :** avertissement de validation conservé dans chacune des 22 pages. Ce contrôle ne qualifie pas les procédures. |
| Liens externes | **Réussie :** GET avec `curl --location`, délai maximal 25 secondes par URL ; les 19 URL HTTPS distinctes donnent HTTP 200. Aucun contenu local ni identifiant transmis. Une réponse HTTP valide ne remplace pas une revue du fond. |
| Accès HTTP à l’aperçu sur le poste | **Réussi :** HTTP 200 pour le démarrage rapide français, serveur lié uniquement à la boucle locale puis arrêté. |
| Inspection visuelle dans le navigateur intégré | **Bloquée :** fichier de session hors des dossiers approuvés ; tentative HTTP locale non joignable depuis ce navigateur. Aucune capture, vérification visuelle ou mesure de mise en page mobile n’est revendiquée. |

Les 19 URL contrôlées sont les références publiques des pages : les dix pages Microsoft Learn, les six pages Keycloak, la déclaration de confidentialité Microsoft et le chapitre de sauvegarde PostgreSQL, ainsi que le lien d’issues du dépôt public. Le détail exact fait foi dans les pages et dans la preuve locale de contrôle ; aucune URL du dépôt d’ingénierie n’est ajoutée.

### Limites avant clôture de l’étape 6

- L’aperçu et les résultats techniques sont conservés dans les fichiers de session, pas dans les sources publiables. Aucun moteur de site ni dépendance n’a été ajouté au dépôt.
- Le choix de configuration du site et la validation de son rendu réel restent à faire ; cet aperçu n’établit ni les URL publiques, ni le thème, ni les réécritures de liens du futur hébergement.
- Les liens requis par le listing Marketplace ne sont pas qualifiés par un contrôle de fichiers locaux ; aucune publication ou vérification Partner Center n’est réalisée.
- Aucun test VM ou choix d’image ; l’étape 5 reste en attente de la cible. Aucune revue indépendante par un exploitant ni PR ; l’étape 7 reste ouverte.
- L’étape 6 reste **non cochée** : le sous-ensemble local est validé, pas l’ensemble du critère de livraison.

## Configuration du site Jekyll et validation réelle locale — 2026-11-09

Le demandeur autorise la configuration locale du site sans publication et choisit explicitement Jekyll.

### Livraison

- Gemfile et verrou de dépendances, configuration Jekyll, gabarit bilingue et CSS local ; les versions directes de rendu sont vérifiées dans la [matrice GitHub Pages](https://pages.github.com/versions/).
- Conteneur Ruby vérifié depuis les tags officiels et fixé par empreinte ; aucune modification du Ruby système. Gems et sortie `_site/` ignorées par Git.
- Métadonnées sur les 22 sources canoniques, accueil anglais sous `/` et français sous `/fr/`, sous-chemin projet conservé. Les liens source `.md` restent lisibles sur GitHub et sont résolus vers les URL HTML par `jekyll-relative-links`.
- Navigation persistante dans la langue choisie, lien d’évitement vers le contenu, mise en page adaptable et tableaux défilant dans leur propre conteneur sur écran étroit.
- Interface `make setup`, `make build`, `make check`, `make serve` ; guides contributeurs EN/FR exclus du site. Aucun workflow, push, changement des paramètres Pages ou déploiement.
- Validateur Python sans dépendance supplémentaire et six tests de régression sur copies isolées : site valide, traduction absente, lien erroné, navigation dans la mauvaise langue, exposition d’un fichier interne et cible du lien d’évitement absente.

### Vérifications exécutées

| Commande ou contrôle | Résultat |
|---|---|
| `make -C docs/keycloak-azure-marketplace-docs setup` depuis le dépôt d’ingénierie | **Réussi :** conteneur récupéré, gems installées, verrou généré. |
| `make -C docs/keycloak-azure-marketplace-docs check` | **Réussi :** 22 pages, onze paires EN/FR ; 274 liens locaux HTML/CSS/fragments, dix tableaux et dix cases non cochées ; sources/rendu, titres, langues, avertissements, sélecteurs et navigation contrôlés ; six tests de régression réussis. |
| `bash -n docs/keycloak-azure-marketplace-docs/scripts/site.sh` | **Réussi.** Shellcheck n’est pas installé sur le poste ; aucun résultat Shellcheck revendiqué. |
| `make -C docs/keycloak-azure-marketplace-docs serve` | **Démarrage réussi :** page d’accueil servie en HTTP 200 au sous-chemin configuré, publication du port liée seulement à `127.0.0.1`. Conteneur arrêté volontairement après les tests ; l’arrêt explicite remonte un code non nul à Make, pas un échec du build. |
| Firefox local isolé, piloté par WebDriver BiDi | **Réussi :** accueils EN/FR, démarrage rapide FR et dépannage FR, chacun à 1280 et 390 pixels ; langue et titre principal, CSS chargé, retour à la ligne du menu, absence de débordement horizontal du document, tableaux contenus, avertissement et cinq cases du démarrage rapide vérifiés. Aller-retour réel via les liens de langue FR → EN → FR réussi. |
| Captures Firefox | Huit captures locales conservées dans les fichiers de session ; inspection visuelle de l’accueil FR large, du démarrage rapide FR étroit et du dépannage FR étroit : titres lisibles, navigation visible, avertissements distincts. Pas de certification d’accessibilité ni test de tous les navigateurs. |

Le build initial a détecté un écart réel de moteur : Kramdown interprétait la ligne de langue avec `|` comme un tableau. Un point médian remplace ce séparateur dans les deux langues. Les tests isolés ont aussi conduit à canonicaliser le chemin temporaire macOS dans leur préparation ; les sources opérateur n’ont pas changé de sens.

### Réserves et état du suivi

- L’installation signale Ruby Sass en fin de vie, dépendance de cette branche Jekyll ; le site emploie du CSS simple. Ruby signale également des changements futurs de bibliothèque standard. Ces avertissements sont consignés dans les guides contributeurs ; ils n’empêchent pas les tests exécutés et ne constituent pas une qualification de sécurité du moteur.
- Le navigateur intégré ne pouvait pas inspecter l’aperçu précédent ; Firefox local isolé a permis de tester le site Jekyll réel sans contourner ses restrictions de dossiers.
- Serveur et navigateur de test arrêtés ; aucune écoute de prévisualisation laissée active. Aucun contenu envoyé à un service de capture externe.
- Le contrôle HTTP 19/19 des références publiques provient du contrôle précédent de cette session ; il n’est pas intégré au validateur local et n’a pas été rejoué ici.
- L’étape 6 reste ouverte pour les URL publiques et les liens requis par le listing, impossibles à qualifier par un site seulement local. La partie build/rendu local est maintenant réalisée. Étape 5 toujours en attente de l’image, étape 7 encore ouverte.
