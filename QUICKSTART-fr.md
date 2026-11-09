---
title: "Démarrage rapide : réussir votre première connexion applicative"
lang: fr
---
# Démarrage rapide : réussir votre première connexion applicative

[English](QUICKSTART.md) · Français

[Accueil de la documentation](README-fr.md)

> **Brouillon de prépublication.** L’application n’est pas encore publiée sur Microsoft Marketplace. L’image cible n’est pas encore confirmée. La récupération des identifiants, les adresses de service et les commandes propres à l’image sont **⚠️ à valider**. Ce démarrage rapide est un parcours court à travers les guides, pas une procédure de déploiement testée.

## Avant de commencer

Munissez-vous de votre abonnement Azure et de votre groupe de ressources, des autorisations pour inspecter la VM déployée, d’un accès d’administration approuvé et des coordonnées des responsables DNS et certificats. Pour le contrôle final, associez un responsable applicatif et utilisez des comptes de test sans données de production.

## Suivre ces cinq étapes

1. **Retrouvez votre VM et vérifiez son état de préparation.** Dans le portail Azure, repérez la VM prévue et consultez ses états de provisionnement et d’alimentation. Vérifiez séparément l’état de préparation de l’application avec la procédure validée pour votre image ; une VM en cours d’exécution ne prouve pas à elle seule que Keycloak est prêt. Consultez [Vérifier votre déploiement](docs/01-verify-deployment-fr.md).
2. **Confirmez un accès d’administration restreint.** Vérifiez qu’un exploitant autorisé peut gérer la VM par le moyen approuvé. Examinez les autorisations et restrictions réseau ; n’ouvrez pas l’administration à toutes les sources pour démarrer. Consultez [Sécuriser votre accès d’administration Azure](docs/02-secure-azure-access-fr.md).
3. **Vérifiez l’adresse du service et HTTPS de confiance.** Utilisez l’adresse confirmée par le responsable du déploiement. Vérifiez que le client prévu l’atteint sans avertissement de certificat. Sinon, accomplissez [Configurer votre domaine et HTTPS de confiance](docs/04-configure-domain-and-tls-fr.md) avant de saisir des identifiants.
4. **Remplacez l’accès administrateur temporaire.** Obtenez les identifiants initiaux uniquement par le mécanisme confirmé pour votre image. Établissez et testez un administrateur permanent dans une session distincte avant de supprimer l’accès temporaire et de retirer les éléments d’authentification associés. Consultez [Finaliser votre premier accès à Keycloak](docs/03-complete-initial-access-fr.md).
5. **Testez une connexion applicative.** Avec le responsable applicatif, configurez un realm, un utilisateur et un client de test adaptés à l’application. Lancez la connexion depuis cette application, vérifiez la session obtenue et confirmez qu’un utilisateur non autorisé se voit refuser l’accès prévu. Consultez [Configurer Keycloak pour votre organisation](docs/05-configure-keycloak-fr.md).

**Arrêtez-vous devant une procédure propre à l’image non vérifiée.** Ne devinez ni URL de console, ni emplacement d’identifiants, ni commande, ni valeur de configuration. Demandez les instructions manquantes à l’[assistance](SUPPORT-fr.md) avant de poursuivre. Ne contournez jamais un avertissement de certificat et ne supprimez pas votre seul administrateur fonctionnel.

## Vérifier votre résultat

- [ ] L’état de la ressource Azure et l’état de préparation de l’application ont été vérifiés séparément.
- [ ] Les exploitants autorisés disposent d’un accès d’administration restreint et vérifié.
- [ ] L’adresse de service convenue utilise HTTPS avec un certificat approuvé par le client prévu.
- [ ] L’administration permanente fonctionne et l’accès temporaire ne fonctionne plus.
- [ ] L’application de test accepte l’utilisateur prévu et refuse les accès non autorisés.

Ce résultat démontre un test initial, **pas une aptitude à la production**. Déployer la VM n’intègre pas automatiquement vos applications.

## Avant de connecter de vrais utilisateurs

Accomplissez [Exploiter, protéger et restaurer votre déploiement](docs/06-operate-and-recover-fr.md) : organisez et testez la récupération, attribuez les responsabilités de maintenance et de surveillance, puis examinez la disponibilité et les coûts.

En cas d’échec d’un contrôle, consultez [Diagnostiquer un problème et demander de l’aide](docs/07-troubleshoot-and-get-support-fr.md). Ne partagez que des détails d’erreur expurgés, jamais des identifiants, jetons ou clés privées.

## Références primaires

- Microsoft : [états des VM et facturation](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) et [accès Azure à privilèges minimaux](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices).
- Keycloak : [configuration du nom d’hôte](https://www.keycloak.org/server/hostname), [suppression de l’administrateur temporaire](https://www.keycloak.org/server/bootstrap-admin-recovery) et [intégration applicative](https://www.keycloak.org/securing-apps/overview).

Ces références expliquent le comportement général de la plateforme ou du projet amont. Elles ne prouvent pas quelles fonctions sont configurées dans l’image.
