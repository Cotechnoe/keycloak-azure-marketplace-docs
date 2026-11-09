# Configurer Keycloak pour votre organisation

[English](05-configure-keycloak.md) | Français

[Accueil de la documentation](../README-fr.md)

> **Brouillon de prépublication.** Cette liste de contrôle de configuration organisationnelle repose sur les recommandations du projet Keycloak, pas sur une intégration testée pour cette offre. Les libellés de console, intégrations prises en charge et version cible sont ⚠️ à valider.

## Avant de commencer

Disposez d’un [administrateur permanent](03-complete-initial-access-fr.md) vérifié, d’une [adresse de service de confiance](04-configure-domain-and-tls-fr.md), d’un responsable applicatif et d’un environnement de test ou realm de test approuvé. Ne testez pas de nouveaux paramètres d’authentification sur le seul accès d’administration fonctionnel.

## Choisir votre configuration

Le [guide d’administration Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html) décrit les realms, utilisateurs, rôles, clients, l’intermédiation d’identité et la fédération. Ce sont des capacités du projet amont, pas une affirmation que votre VM les a configurées.

| Décision | À convenir avec le responsable concerné |
|---|---|
| Realm | Quels utilisateurs, applications et politiques vont ensemble et qui les administre. |
| Source des utilisateurs | Si les comptes sont gérés localement ou dépendent d’un annuaire ou fournisseur d’identité configuré séparément. |
| Application | Quel protocole et type de client l’application prend en charge, ses destinations de redirection approuvées et les éléments d’authentification nécessaires. |
| Politique d’accès | Quels utilisateurs peuvent accéder à l’application, quels rôles elle utilise et quelle protection d’authentification est requise. |
| Assistance aux comptes | Qui gère l’intégration des utilisateurs, les pertes d’accès et les problèmes d’authentification. |

N’annoncez pas l’auto-inscription, la récupération de mot de passe ou les parcours par courriel aux utilisateurs avant d’avoir testé la configuration et les dépendances nécessaires.

## Valider une application avant d’étendre le périmètre

1. Convenez d’un realm et d’un utilisateur de test sans accès aux données de production.
2. Faites configurer l’intégration par l’administrateur Keycloak et le responsable applicatif avec la documentation de leurs versions logicielles réelles. La [présentation Keycloak de l’intégration applicative](https://www.keycloak.org/securing-apps/overview) explique le rôle des bibliothèques applicatives compatibles avec les standards.
3. Limitez les destinations de redirection et les autorisations aux besoins prévus de l’application. Protégez les éléments d’authentification du client avec votre processus approuvé de gestion des secrets.
4. Lancez la connexion depuis l’application de test. Vérifiez l’adresse de service prévue, la réussite de l’authentification et la session applicative obtenue.
5. Testez un utilisateur non autorisé ainsi qu’un utilisateur autorisé. Convenez du comportement attendu de déconnexion et de session, puis testez-le.
6. Consignez les décisions de configuration, résultats des tests et responsable de l’assistance avant de planifier l’accès en production.

**Résultat attendu :** le responsable applicatif et l’exploitant Keycloak démontrent le comportement d’accès prévu. Afficher la console d’administration Keycloak ne démontre pas à lui seul l’intégration applicative.

**⚠️ À valider sur l’image cible :** procédure exacte de realm et de client, paramètres pris en charge selon la version et test d’intégration complet. Les applications, annuaires et fournisseurs d’identité sont des systèmes distincts ; aucune intégration incluse n’est promise ici.

## En cas d’échec d’un contrôle

Vérifiez avec le responsable applicatif le realm prévu, l’enregistrement de l’application, l’adresse de service, les paramètres de redirection et les autorisations. Ne partagez que des détails d’erreur expurgés ; les jetons et cookies de session ne doivent pas apparaître dans des signalements publics. Consultez le [dépannage](07-troubleshoot-and-get-support-fr.md).

**Suite :** [Exploiter, protéger et restaurer votre déploiement](06-operate-and-recover-fr.md).
