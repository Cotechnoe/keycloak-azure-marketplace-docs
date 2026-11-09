---
title: Exploiter, protéger et restaurer votre déploiement
lang: fr
---
# Exploiter, protéger et restaurer votre déploiement

[English](06-operate-and-recover.md) · Français

[Accueil de la documentation](../README-fr.md)

> **Brouillon de prépublication.** Les procédures de sauvegarde, restauration, mise à jour et récupération pour l’image cible sont ⚠️ à valider. Cette page fournit une liste de contrôle d’exploitation, pas des commandes de récupération exécutables. Aucun service Azure cité n’est déclaré activé ou inclus dans l’offre.

## Avant de commencer

Identifiez le responsable du service, l’exploitant Azure, l’administrateur Keycloak et les responsables applicatifs. Convenez d’un délai de récupération acceptable, d’une perte de données acceptable et d’une fenêtre de maintenance. Les [recommandations Microsoft sur l’architecture des VM](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/virtual-machines) couvrent la fiabilité et les dépendances ; elles ne rendent pas une VM unique hautement disponible.

## Établir et tester votre plan de sauvegarde

1. Inventoriez les données d’identité, la configuration applicative, les personnalisations, les certificats et les autres éléments nécessaires à la reconstruction du service. Conservez les éléments de récupération protégés séparément des diagnostics ordinaires d’assistance.
2. Choisissez une approche de sauvegarde avec les exploitants de la base de données et d’Azure. Consultez les [recommandations PostgreSQL sur la sauvegarde](https://www.postgresql.org/docs/current/backup.html) et le [fonctionnement de la sauvegarde des VM Azure](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction).
3. Vérifiez ce que protège réellement la sauvegarde choisie. Ne supposez pas qu’un point de récupération de VM permet une restauration de base de données cohérente au niveau applicatif uniquement parce que la tâche a réussi. Microsoft distingue les niveaux de cohérence et explique que la cohérence applicative sous Linux exige une coordination supplémentaire.
4. Définissez la planification, la conservation, les accès au stockage, la protection contre les suppressions accidentelles et le responsable des alertes d’échec. Confirmez la compatibilité et le coût avant d’activer un service.
5. Restaurez dans un environnement isolé avec la procédure validée pour votre image. Empêchez l’envoi de courriels de test, la synchronisation d’annuaires et tout autre contact involontaire avec la production.
6. Vérifiez l’accès d’administration, les données attendues et un parcours de connexion applicative. Consignez le délai de récupération observé et les données récupérées.

**Résultat attendu :** vous disposez de la preuve d’une récupération utilisable, pas seulement d’une tâche de sauvegarde réussie.

**⚠️ À valider :** cohérence de la base de données, commandes de sauvegarde, ordre de récupération, identifiants et configuration restaurés, et utilisation sûre des disques restaurés. Ne rattachez pas des données en service à une nouvelle initialisation et n’écrasez pas de données de production à l’aide de cette liste.

## Planifier la maintenance et les mises à jour

1. Inventoriez les logiciels et la configuration réellement installés avec une procédure vérifiée en lecture seule.
2. Examinez les mises à jour prises en charge et les recommandations de version avec les exploitants responsables. [Azure Update Manager](https://learn.microsoft.com/en-us/azure/update-manager/overview) concerne les mises à jour des machines ; ne supposez pas qu’il met à niveau l’application Keycloak distribuée séparément.
3. Pour les changements Keycloak, examinez le [guide officiel de mise à niveau](https://www.keycloak.org/docs/latest/upgrading/index.html) pour les versions installée et envisagée. Ne choisissez pas une cible de mise à niveau uniquement parce qu’elle est présentée comme la plus récente.
4. Testez le changement et le plan de récupération sur une copie isolée avant de planifier la maintenance en production. Ne supposez pas qu’un retour à une version applicative antérieure annule les modifications de la base de données.
5. Après la maintenance approuvée, vérifiez l’état de préparation du service et le parcours de connexion applicative, puis consignez le résultat.

**⚠️ À valider :** chemins de mise à jour pris en charge du système et de l’application, stratégie de remplacement de l’image, commandes exactes, interruption attendue et méthode de récupération.

## Surveiller le service et ses dépendances

1. Examinez les métriques hôte disponibles dans Azure Monitor. Le [guide Microsoft de surveillance des VM](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/monitor-vm) distingue les métriques hôte des données du système invité qui nécessitent une configuration.
2. Déterminez les signaux du système invité et de l’application nécessaires. Confirmez la compatibilité de l’agent et du système, la collecte, les accès, la conservation et les coûts avant d’activer la collecte.
3. Attribuez des alertes de disponibilité applicative, de saturation des ressources, d’expiration de certificat et d’échec des sauvegardes selon vos exigences.
4. Testez qu’une alerte atteint le responsable d’astreinte. Incluez un contrôle sûr de connexion applicative ; les seules métriques hôte ne prouvent pas que l’authentification fonctionne.

**Résultat attendu :** un exploitant désigné reçoit des alertes exploitables et connaît la procédure d’intervention. Les contrôles de santé et paramètres de collecte propres à l’image restent ⚠️ à valider.

## Examiner la disponibilité et les coûts

- Documentez l’effet des défaillances de VM, base de données, réseau, DNS et certificat. Ne supposez aucune redondance, récupération automatique ou garantie de niveau de service de la charge de travail.
- Examinez toutes les ressources et tous les services consommés par votre déploiement, ainsi que les conditions commerciales Marketplace réelles. Aucun prix logiciel n’est établi ici.
- Utilisez les [budgets Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) pour les notifications lorsqu’ils sont disponibles. Les alertes budgétaires n’arrêtent pas à elles seules la consommation.
- Consultez les [états des VM et la facturation](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) avant d’arrêter des ressources de test. Une VM arrêtée mais allouée diffère d’une VM désallouée ; d’autres ressources peuvent continuer à générer des frais.

Ne supprimez pas la VM, les disques ou les points de récupération tant que leurs responsables n’ont pas confirmé les exigences de protection et de conservation des données.

**Suite :** utilisez [Diagnostiquer un problème et demander de l’aide](07-troubleshoot-and-get-support-fr.md) à chaque échec d’un contrôle d’exploitation.
