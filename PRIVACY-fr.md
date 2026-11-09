# Examiner les aspects de confidentialité de votre déploiement

[English](PRIVACY.md) | Français

[Accueil de la documentation](README-fr.md)

> **Brouillon de prépublication — pas une politique de confidentialité Marketplace définitive.** L’application n’est pas encore publiée sur Microsoft Marketplace. L’image cible et ses flux de données sont ⚠️ à valider. Cette page ne doit pas servir de preuve d’un examen de conformité juridique ou technique.

## Examiner les données traitées par votre service d’identité

Le [guide d’administration Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html) décrit les utilisateurs, éléments d’authentification, attributs, rôles et sessions. Examinez les informations que votre propre configuration collecte et expose aux applications.

Identifiez qui peut administrer le service, quels systèmes reçoivent des informations d’identité, comment les journaux et sauvegardes sont protégés, et comment votre organisation gère l’accès, la conservation et la suppression. Le déploiement n’établit pas à lui seul la conformité réglementaire ou la résidence des données.

**⚠️ À valider pour l’image cible :** emplacements réels des données et journaux, journalisation par défaut, traitement des éléments d’authentification, connexions sortantes, télémétrie et tout accès de l’éditeur. Ce brouillon n’affirme pas que l’examen de ces comportements est terminé.

## Examiner les conditions Azure et des services connectés

Les [recommandations Microsoft sur la responsabilité partagée](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) distinguent la plateforme des systèmes et données que vous exploitez. Consultez la [Déclaration de confidentialité Microsoft](https://www.microsoft.com/en-us/privacy/privacystatement) et les conditions applicables à votre abonnement Azure.

Pour chaque application, annuaire, fournisseur d’identité, autorité de certification, fournisseur DNS, service de surveillance ou destination de sauvegarde que vous configurez, examinez séparément ses flux de données et ses conditions de confidentialité. Ne supposez pas que ces services font partie de l’image ou relèvent d’une notice unique.

## Limiter les informations dans les demandes d’assistance

Dans une demande d’assistance, ne partagez que les informations de contact et de diagnostic nécessaires à l’examen. Les issues GitHub publiques sont visibles de tous.

Ne partagez jamais de mots de passe, clés privées, jetons, cookies de session, fichiers d’identifiants ou données personnelles inutiles. Expurgez les journaux avant de les partager. N’accordez pas d’accès à la VM uniquement pour rendre reproductible un signalement public. Consultez les [consignes d’assistance](SUPPORT-fr.md).

## Confirmer la notice de l’éditeur avant publication

Pour une question de confidentialité, contactez Cotechnoe à [support@cotechnoe.com](mailto:support@cotechnoe.com). N’incluez pas de dossiers personnels ou d’archives de diagnostic dans un premier message.

**⚠️ À valider avant publication :** notice de confidentialité approuvée par l’éditeur, traitement des informations d’assistance et correspondance entre cette notice et l’image effectivement livrée.

Avant la fin de cet examen, cette page reste un guide de confidentialité pour un parcours de déploiement en brouillon, pas la politique Marketplace définitive.
