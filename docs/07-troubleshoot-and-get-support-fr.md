---
title: Diagnostiquer un problème et demander de l’aide
lang: fr
---
# Diagnostiquer un problème et demander de l’aide

[English](07-troubleshoot-and-get-support.md) · Français

[Accueil de la documentation](../README-fr.md)

## Avant de commencer

Confirmez la VM concernée avec son responsable. Consignez le début du problème et le changement le plus récent. Si la production est affectée, suivez votre processus d’incident et préservez les éléments utiles avant de tenter une réparation.

## Identifier la couche en échec

| Observation | Premier contrôle | Personnes à solliciter |
|---|---|---|
| Le déploiement signale une erreur Azure | Abonnement et ressource corrects, erreur de l’opération ; consultez les [contrôles de déploiement](01-verify-deployment-fr.md). | Administrateur Azure ; Microsoft pour les problèmes de plateforme Azure, ou Cotechnoe pour un problème apparent de l’image. |
| La connexion d’administration échoue | Erreur d’autorisation Azure, expiration du délai réseau ou erreur de connexion au système invité ; consultez les [contrôles d’accès](02-secure-azure-access-fr.md). | Administrateur Azure, réseau ou VM selon la couche en échec. |
| L’URL d’administration est inaccessible ou signale une erreur de certificat | Nom DNS prévu, accessibilité réseau et confiance dans le certificat ; consultez [domaine et TLS](04-configure-domain-and-tls-fr.md). | Responsables DNS, réseau et certificats, et exploitant VM. |
| L’accès administrateur initial est indisponible | Procédure vérifiée de remise des identifiants pour l’image exacte ; consultez le [premier accès](03-complete-initial-access-fr.md). | Exploitant VM et Cotechnoe pour les précisions propres à l’image. |
| La console fonctionne mais la connexion applicative échoue | Realm, enregistrement du client, redirections et autorisations ; consultez la [configuration applicative](05-configure-keycloak-fr.md). | Administrateur Keycloak et responsable applicatif. |
| Un contrôle de sauvegarde, mise à jour ou surveillance échoue | Erreur de l’outil choisi et dernier changement ; consultez l’[exploitation](06-operate-and-recover-fr.md). | Exploitant responsable de cet outil et de la charge de travail. |

Les [recommandations Microsoft sur la responsabilité partagée](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) aident à distinguer les problèmes de plateforme et de charge de travail. L’état d’une VM Azure ne permet pas à lui seul d’identifier le composant applicatif défaillant.

## Préparer une demande sans données sensibles

1. Décrivez la tâche effectuée, le résultat attendu et le résultat obtenu.
2. Indiquez l’heure de l’incident et le fuseau horaire, si la VM vient d’être déployée et le dernier changement pertinent.
3. Incluez la référence d’image uniquement si elle a été vérifiée dans votre déploiement. Si elle est inconnue, dites-le ; ne déduisez pas une version d’un nom.
4. Ne fournissez qu’un court extrait d’erreur expurgé. Relisez-le avant publication.
5. Précisez quels contrôles ont réussi ou échoué et si des utilisateurs sont affectés.
6. Choisissez le [canal d’assistance approprié](../SUPPORT-fr.md) et lisez la [notice de confidentialité](../PRIVACY-fr.md).

N’incluez jamais de mots de passe, clés privées, jetons, en-têtes d’autorisation, cookies, chaînes de connexion ou fichiers d’identifiants. Masquez les données personnelles et les noms de ressources, noms d’hôtes, adresses et identifiants de realms ou clients confidentiels. N’envoyez pas d’archives complètes de diagnostic dans des issues publiques.

**Résultat attendu :** le destinataire identifie la tâche en échec et le prochain contrôle sûr sans recevoir de secrets ou de données client inutiles.

## Éviter qu’un diagnostic entraîne une perte de données

Ne relancez pas l’initialisation, ne réinitialisez pas la base de données, ne supprimez pas le seul administrateur fonctionnel, ne désactivez pas les restrictions réseau et ne supprimez pas une VM ou un disque comme essai de correction. Les actions de récupération nécessitent une procédure approuvée et testée pour l’image réelle, ainsi qu’une sauvegarde adaptée ou une cible de test isolée.

Si ce guide ne contient pas le contrôle propre à l’image nécessaire, signalez ce manque. L’absence de procédure n’autorise pas à en improviser une sur les données de production.
