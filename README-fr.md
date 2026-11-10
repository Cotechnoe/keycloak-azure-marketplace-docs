---
title: Exploiter votre VM Keycloak après le déploiement
lang: fr
permalink: /fr/
---
# Exploiter votre VM Keycloak après le déploiement

[English](README.md) · Français

**Date de révision :** 2026-11-10.

Cette documentation s’adresse à l’administrateur Azure ou à l’exploitant responsable d’une VM déployée depuis l’offre Cotechnoe. Commencez ici après le déploiement de votre VM. Il ne s’agit pas d’un guide de connexion destiné aux utilisateurs des applications de votre organisation.

Les outils de construction de l’éditeur ne sont pas nécessaires pour suivre ces guides. Vous devez disposer des autorisations nécessaires pour inspecter votre déploiement Azure et d’un moyen approuvé pour administrer la VM.

## Commencer par le démarrage rapide

Suivez le [démarrage rapide](QUICKSTART-fr.md) jusqu’au premier jalon : une administration permanente vérifiée. Une suite facultative distincte couvre la première connexion applicative lorsqu’un responsable applicatif est prêt. Les deux parcours s’arrêtent devant une instruction propre à l’image non vérifiée.

## Suivre votre liste de contrôle après déploiement

| Étape | Tâche | Vous pouvez poursuivre lorsque |
|---|---|---|
| 1 | [Vérifier votre déploiement](docs/01-verify-deployment-fr.md) | Vous identifiez votre VM et distinguez le provisionnement Azure de l’état de préparation de l’application. |
| 2 | [Sécuriser votre accès d’administration Azure](docs/02-secure-azure-access-fr.md) | Les exploitants autorisés disposent d’un accès d’administration restreint et testé. |
| 3 | [Configurer votre domaine et HTTPS de confiance](docs/04-configure-domain-and-tls-fr.md) | Les clients prévus atteignent le nom d’hôte convenu sans avertissement de certificat. |
| 4 | [Finaliser votre premier accès à Keycloak](docs/03-complete-initial-access-fr.md) | Un administrateur permanent fonctionne et l’accès temporaire a été retiré. |
| 5 | [Configurer Keycloak pour votre organisation](docs/05-configure-keycloak-fr.md) | Une application et un utilisateur de test accomplissent le parcours de connexion prévu. |
| 6 | [Exploiter, protéger et restaurer votre déploiement](docs/06-operate-and-recover-fr.md) | Les responsables, la surveillance, la maintenance et un plan de récupération testé sont en place. |
| 7 | [Diagnostiquer un problème et demander de l’aide](docs/07-troubleshoot-and-get-support-fr.md) | Vous identifiez la couche en échec et préparez une demande d’assistance sans données sensibles. |

Utilisez le guide de dépannage à n’importe quelle étape. **Si votre URL d’administration ne dispose pas déjà de HTTPS de confiance, accomplissez les prérequis domaine et TLS avant de saisir des identifiants Keycloak.** Ne contournez pas les avertissements de certificat pour respecter la numérotation.

Suivez cet ordre d’exécution : contrôles de la ressource Azure → accès VM approuvé → contrôle de préparation de l’application → HTTPS de confiance → administrateur permanent. Le guide de déploiement indique quand suspendre son contrôle de santé jusqu’à l’obtention de l’accès VM. Les noms de fichiers sont des identifiants stables, pas l’ordre d’exécution. L’intégration applicative et la préparation à la production sont des tâches distinctes à poursuivre ensuite.

## Comprendre ce que vous gérez

Une VM Azure est une ressource d’infrastructure en tant que service. Les [recommandations Microsoft sur la responsabilité partagée](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) distinguent la plateforme Azure du système d’exploitation, des applications, des identités et des données que vous gérez.

| Domaine | Votre action d’exploitation |
|---|---|
| Ressources et accès Azure | Vérifier qui peut administrer les ressources et quelles connexions réseau sont autorisées. |
| VM et application | Vérifier l’état de préparation, gérer les accès administrateurs et planifier la maintenance. |
| Utilisateurs et applications de votre organisation | Configurer les intégrations et les autorisations. Déployer une VM ne met pas en place un parcours de connexion applicative fonctionnel. |
| Données et continuité | Protéger les identifiants, organiser les sauvegardes, tester la récupération et définir l’interruption acceptable. |
| Services Azure que vous choisissez | Vérifier la compatibilité, les autorisations, la configuration et les coûts avant de les activer. |

Il s’agit de responsabilités d’exploitation, pas d’un remplacement de vos accords avec Microsoft ou Cotechnoe. Ne supposez pas que l’image comprend des sauvegardes gérées, une collecte de données du système invité par Azure Monitor, la gestion des mises à jour, la haute disponibilité ou un accord de niveau de service (SLA) d’assistance.

## Connaître les limites de cette documentation

- Ces guides n’établissent aucune version d’image ou de système d’exploitation, aucun nom commercial affiché, plan Marketplace, prix ou taille de VM prise en charge.
- Le [guide officiel d’administration Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html) décrit les capacités du projet amont. Une capacité n’est pas nécessairement configurée ou vérifiée dans cette offre.
- Les applications, annuaires et fournisseurs d’identité externes doivent être évalués et intégrés séparément. Cette documentation ne promet aucune intégration incluse.
- Les sections marquées **⚠️ à valider** ne sont pas des instructions à exécuter sur une VM de production. Arrêtez-vous à cet endroit et [demandez des précisions](SUPPORT-fr.md).
- L’anglais est la langue de référence ; une traduction française est disponible. La validation du rendu du site et l’exécution sur l’image retenue restent des étapes de livraison distinctes.

## Protéger les informations dans une demande d’aide

Lisez les [consignes d’assistance](SUPPORT-fr.md) et la [notice de confidentialité](PRIVACY-fr.md). Ne publiez jamais de mots de passe, clés privées, jetons, cookies, fichiers d’identifiants administrateurs ou données personnelles dans des issues publiques.
