# Issue #3 — Étape 2 : parcours et architecture de l’information

**Statut :** proposition d’architecture, à confirmer avant rédaction client

Cette architecture cible la personne responsable de l’abonnement Azure et de la VM après son instanciation depuis Microsoft Marketplace. Le parcours suppose que le client a terminé l’action de déploiement dans Azure ; il ne présume ni que l’offre est actuellement publiée, ni d’un titre Marketplace, plan, SKU, version d’image, choix réseau ou service Azure déjà activé.

La documentation sera bilingue anglais-français. Les noms de fichiers ci-dessous sont des slugs proposés, pas des pages déjà publiées. Tout comportement particulier à l’offre doit être vérifié sur l’image Marketplace retenue avant de devenir une instruction.

## Parcours proposé

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
- Étape 3 : rédaction neuve à partir de cette structure, après validation des faits et confirmation de la cible lorsqu’elle sera disponible.
