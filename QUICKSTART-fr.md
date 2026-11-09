---
title: "Démarrage rapide : établir une administration permanente"
lang: fr
---
# Démarrage rapide : établir une administration permanente

[English](QUICKSTART.md) · Français

[Accueil de la documentation](README-fr.md)

> **Brouillon de prépublication.** L’application n’est pas encore publiée sur Microsoft Marketplace. L’image cible n’est pas encore confirmée. La récupération des identifiants, les adresses de service et les commandes propres à l’image sont **⚠️ à valider**. Ce démarrage rapide est un parcours court à travers les guides, pas une procédure de déploiement testée.

## Avant de commencer

Munissez-vous de votre abonnement Azure et de votre groupe de ressources, des autorisations pour inspecter la VM déployée, d’un moyen approuvé d’obtenir l’accès d’administration et des coordonnées des responsables DNS et certificats. Aucune application externe n’est nécessaire pour terminer le jalon administratif. Les instructions propres à l’image doivent toujours être vérifiées avant exécution.

## Atteindre le jalon administratif

1. **Retrouvez votre VM et vérifiez son état Azure.** Dans le portail Azure, repérez la VM prévue et consignez ses états de déploiement et d’alimentation. Laissez la préparation de l’application comme non vérifiée tant que l’accès d’administration n’est pas disponible. Consultez [Vérifier votre déploiement](docs/01-verify-deployment-fr.md).
2. **Confirmez un accès VM restreint, puis vérifiez la préparation de l’application.** Suivez [Sécuriser votre accès d’administration Azure](docs/02-secure-azure-access-fr.md), puis terminez le contrôle de préparation applicative du guide de déploiement avant de poursuivre. Utilisez uniquement une procédure vérifiée pour votre image ; arrêtez-vous si elle est indisponible. Une VM en cours d’exécution ne prouve pas à elle seule que Keycloak est prêt. N’ouvrez pas l’administration à toutes les sources.
3. **Vérifiez l’adresse du service et HTTPS de confiance.** Utilisez l’adresse confirmée par le responsable du déploiement. Avant de saisir des identifiants, accomplissez les contrôles de résultat de [Configurer votre domaine et HTTPS de confiance](docs/04-configure-domain-and-tls-fr.md), même si HTTPS fonctionne déjà : confiance du client, URL prévues, responsable du renouvellement désigné, processus de renouvellement testé et détection de l’expiration ou des échecs de renouvellement. Ne reconfigurez pas inutilement un HTTPS fonctionnel ; appliquez uniquement la configuration manquante avec une procédure vérifiée pour votre image.
4. **Remplacez l’accès administrateur temporaire.** Obtenez les identifiants initiaux uniquement par le mécanisme confirmé pour votre image. Établissez et testez un administrateur permanent dans une session distincte avant de supprimer l’accès temporaire et de retirer les éléments d’authentification associés. Consultez [Finaliser votre premier accès à Keycloak](docs/03-complete-initial-access-fr.md).

**Arrêtez-vous devant une procédure propre à l’image non vérifiée.** Ne devinez ni URL de console, ni emplacement d’identifiants, ni commande, ni valeur de configuration. Demandez les instructions manquantes à l’[assistance](SUPPORT-fr.md) avant de poursuivre. Ne contournez jamais un avertissement de certificat et ne supprimez pas votre seul administrateur fonctionnel.

## Vérifier le résultat administratif

- [ ] L’état de la ressource Azure et l’état de préparation de l’application ont été vérifiés séparément.
- [ ] Les exploitants autorisés disposent d’un accès d’administration restreint et vérifié.
- [ ] L’adresse de service convenue utilise HTTPS avec un certificat approuvé par le client prévu ; le renouvellement du certificat a un responsable, un processus testé et une détection des échecs définie.
- [ ] L’administration permanente fonctionne et l’accès temporaire ne fonctionne plus.

Vous pouvez terminer ce jalon administratif ici sans application externe. Il ne démontre **ni une aptitude à la production**, ni une intégration applicative.

## Poursuivre avec une application lorsque vous êtes prêt

Il s’agit d’une suite facultative distincte du démarrage rapide, pas d’une condition pour terminer l’accès administratif. Associez un responsable applicatif et utilisez des comptes de test sans données de production. Avant que de vrais utilisateurs se connectent à une application, son intégration doit être configurée et testée.

1. Avec le responsable applicatif, configurez un realm, un utilisateur et un client de test adaptés à l’application. Consultez [Configurer Keycloak pour votre organisation](docs/05-configure-keycloak-fr.md).
2. Lancez la connexion depuis cette application et vérifiez la session obtenue.
3. Confirmez qu’un utilisateur non autorisé se voit refuser l’accès prévu.

- [ ] L’application de test accepte l’utilisateur prévu et refuse les accès non autorisés.

Déployer la VM n’intègre pas automatiquement vos applications. Ce test applicatif ne démontre **pas non plus une aptitude à la production**.

## Avant de connecter de vrais utilisateurs

Accomplissez [Exploiter, protéger et restaurer votre déploiement](docs/06-operate-and-recover-fr.md) : organisez et testez la récupération, attribuez les responsabilités de maintenance et de surveillance, puis examinez la disponibilité et les coûts.

En cas d’échec d’un contrôle, consultez [Diagnostiquer un problème et demander de l’aide](docs/07-troubleshoot-and-get-support-fr.md). Ne partagez que des détails d’erreur expurgés, jamais des identifiants, jetons ou clés privées.

## Références primaires

- Microsoft : [états des VM et facturation](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) et [accès Azure à privilèges minimaux](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices).
- Keycloak : [configuration du nom d’hôte](https://www.keycloak.org/server/hostname), [suppression de l’administrateur temporaire](https://www.keycloak.org/server/bootstrap-admin-recovery) et [intégration applicative](https://www.keycloak.org/securing-apps/overview).

Ces références expliquent le comportement général de la plateforme ou du projet amont. Elles ne prouvent pas quelles fonctions sont configurées dans l’image.
