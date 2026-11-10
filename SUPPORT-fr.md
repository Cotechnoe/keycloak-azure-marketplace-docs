---
title: Demander de l’aide pour votre déploiement
lang: fr
---
# Demander de l’aide pour votre déploiement

[English](SUPPORT.md) · Français

[Accueil de la documentation](README-fr.md)

Pour les premiers contrôles de mise en service, commencez par le [démarrage rapide](QUICKSTART-fr.md).

## Choisir le bon point de contact

| Besoin | Point de contact |
|---|---|
| Problème présumé de préparation de l’image ou d’initialisation ; correction documentaire | Contactez Cotechnoe à [support@cotechnoe.com](mailto:support@cotechnoe.com), ou utilisez les issues publiques du dépôt documentaire ci-dessous sans données sensibles. |
| Problème Azure de provisionnement, d’accès, d’infrastructure ou de facturation | L’administrateur Azure de votre organisation et son canal d’assistance Microsoft autorisé. |
| Realm, utilisateurs, politique d’authentification ou intégration applicative | Votre administrateur Keycloak et le responsable applicatif ; consultez le [guide officiel d’administration](https://www.keycloak.org/docs/latest/server_admin/index.html). |
| Problème de connexion d’un utilisateur final à une application | Le service d’assistance de votre organisation ou le responsable applicatif, pas une issue d’infrastructure publique contenant des détails de compte. |

Ces indications d’orientation ne créent aucun droit contractuel à l’assistance. Si plusieurs couches interviennent, maintenez le responsable du déploiement impliqué plutôt que de supposer qu’un fournisseur exploite l’ensemble du service.

## Signaler un problème d’image ou de documentation sans données sensibles

1. Utilisez [Diagnostiquer un problème et demander de l’aide](docs/07-troubleshoot-and-get-support-fr.md) pour préparer un signalement minimal.
2. Relisez-le et retirez les secrets, données personnelles et détails d’infrastructure confidentiels.
3. [Ouvrez une issue dans le dépôt documentaire public](https://github.com/Cotechnoe/keycloak-azure-marketplace-docs/issues).

Les issues publiques sont visibles de tous. Ne joignez pas de fichiers d’identifiants, configuration de base de données, jetons, clés privées, cookies de session ou journaux complets.

Pour une première demande privée, écrivez à [support@cotechnoe.com](mailto:support@cotechnoe.com) avec une description minimale, sans secrets ni archives de diagnostic. Si l’examen nécessite des informations sensibles, convenez d’abord d’un moyen de transfert sécurisé avec le destinataire. Cette documentation n’établit aucun dispositif privé de dépôt de diagnostics.

Lisez la [notice de confidentialité](PRIVACY-fr.md) avant de partager des informations.
