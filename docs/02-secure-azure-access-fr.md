---
title: Sécuriser votre accès d’administration Azure
lang: fr
---
# Sécuriser votre accès d’administration Azure

[English](02-secure-azure-access.md) · Français

[Accueil de la documentation](../README-fr.md)

> **Brouillon de prépublication.** La méthode de connexion prise en charge par l’image, les détails des comptes et les besoins réseau effectifs sont ⚠️ à valider. Ce guide recommande des pratiques de contrôle d’accès ; il ne prescrit aucun port ou rôle Azure non vérifié pour l’offre.

## Avant de commencer

Identifiez votre VM avec [Vérifier votre déploiement](01-verify-deployment-fr.md). Sollicitez un administrateur Azure autorisé si vous ne pouvez pas examiner les accès ou le réseau. Prévoyez un accès de secours avant de modifier une connexion existante.

## Examiner qui peut administrer le déploiement

Les libellés du portail ci-dessous suivent la documentation Microsoft anglaise ; leur traduction peut différer. Ces contrôles sont en lecture seule et n’accordent aucun accès.

1. Dans le portail Azure, ouvrez la VM et sélectionnez **Access control (IAM)** → **Check access**. Utilisez **View my access** si proposé ; avec l’intégration PIM, examinez directement les attributions dans **Check access**. Consignez les attributions sur cette ressource et celles héritées des périmètres parents. Suivez la [procédure Microsoft de vérification des accès](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access).
2. N’accordez aux exploitants que les actions et le périmètre nécessaires à leurs tâches. N’accordez pas la propriété de tout l’abonnement simplement pour résoudre un problème de connexion. Les [recommandations Microsoft sur Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices) expliquent les attributions à privilèges minimaux.
3. Identifiez séparément les personnes autorisées à se connecter au système d’exploitation invité et celles autorisées à administrer Keycloak. Les autorisations sur les ressources Azure ne dispensent pas de vérifier chacun de ces accès.
4. Consignez les exploitants autorisés et la personne chargée de retirer les accès lors d’un changement de responsabilités.

Pour examiner un exploitant précis, utilisez **Check access** → **Check access**, sélectionnez **User, group, or service principal**, recherchez l’identité et ouvrez ses attributions. Pour une revue de périmètre, utilisez **Access control (IAM)** → **Role assignments** sur la VM, puis répétez au groupe de ressources ou à une autre ressource pertinente avec votre administrateur Azure. La [procédure Microsoft de liste des attributions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal) décrit l’autorisation de lecture nécessaire. Ces vues ne listent pas les attributions aux périmètres enfants ; les attributions éligibles ne sont pas nécessairement actives.

**Résultat attendu :** vous avez consigné chaque identité examinée, son rôle, le périmètre d’attribution et si l’accès est hérité ou nécessite une activation. Vous pouvez expliquer qui gère les ressources Azure, qui peut accéder à la VM et qui administrera Keycloak. Si la vue est indisponible, consignez le contrôle comme bloqué et sollicitez un administrateur autorisé ; ne vous attribuez pas un rôle plus large pour le terminer.

## Examiner votre connexion d’administration

1. Examinez l’accès d’administration existant et son réseau source avec votre administrateur réseau.
2. Comparez les [options Microsoft d’administration sécurisée des VM](https://learn.microsoft.com/en-us/azure/networking/design-guide/developer-admin-access), telles qu’Azure Bastion ou un VPN, à vos besoins réseau. Ce sont des options à évaluer, pas des fonctions déclarées incluses ou activées dans l’offre.
3. Examinez les groupes de sécurité réseau qui affectent la VM. Pour chaque règle nécessaire, documentez son objectif, les sources et destinations autorisées, le protocole et le port. Utilisez les besoins réels du déploiement, pas des valeurs par défaut supposées. La [référence Microsoft sur les NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) explique l’évaluation des règles.
4. Faites appliquer les modifications approuvées par l’administrateur autorisé en préservant un accès de secours. N’exposez pas l’administration à toutes les sources pour diagnostiquer un problème.
5. Vérifiez une connexion autorisée avant de fermer la session initiale. Vérifiez les restrictions par un test contrôlé qui ne risque pas de bloquer le seul exploitant.

**Résultat attendu :** les exploitants approuvés peuvent se connecter et les restrictions prévues sont vérifiées. Il n’est pas affirmé que le choix d’un service Azure configure automatiquement l’accès à cette image.

**⚠️ À valider sur l’image cible :** méthode de connexion au système invité, privilèges des comptes, besoins réseau et procédure sûre de vérification de la connexion.

## En cas d’échec d’accès

Distinguez un refus d’autorisation Azure, une expiration du délai réseau et un échec d’authentification sur le système invité. Conservez le type d’erreur sans mots de passe ni clés privées. Demandez à l’administrateur Azure d’inspecter les accès effectifs et les règles réseau plutôt que de désactiver les contrôles. Consultez le [dépannage](07-troubleshoot-and-get-support-fr.md).

**Suite :** revenez à la section de préparation applicative de [Vérifier votre déploiement](01-verify-deployment-fr.md). Après la réussite de ce contrôle, poursuivez avec [Configurer votre domaine et HTTPS de confiance](04-configure-domain-and-tls-fr.md), puis l’administration permanente. Ne recommencez pas la préparation d’accès si elle est déjà vérifiée.
