---
title: Configurer votre domaine et HTTPS de confiance
lang: fr
---
# Configurer votre domaine et HTTPS de confiance

[English](04-configure-domain-and-tls.md) · Français

[Accueil de la documentation](../README-fr.md)

> **Brouillon de prépublication.** La procédure de nom d’hôte et de certificat propre à l’image est ⚠️ à valider. Aucune commande, autorité de certification, méthode de validation ou mécanisme de renouvellement n’est supposé fonctionner sur l’image cible.

## Avant de commencer

Disposez du contrôle du nom DNS prévu, d’un exploitant réseau autorisé, d’un processus de certification approuvé et d’une fenêtre de maintenance si le service est déjà utilisé. Préservez la configuration existante et l’accès de secours avant de modifier un déploiement actif.

## Préparer l’adresse du service

1. Convenez de l’adresse qu’utiliseront les applications et les administrateurs. Déterminez quels clients doivent la résoudre et l’atteindre.
2. Faites confirmer par les responsables DNS et réseau que les enregistrements se résolvent vers le service prévu depuis ces réseaux clients. Ne supposez pas que chaque déploiement nécessite une adresse IP publique ou un DNS public.
3. Choisissez un certificat approuvé par ces clients et couvrant le nom d’hôte retenu. Confirmez les exigences de validation et de renouvellement de l’autorité avant de modifier les accès réseau.
4. Consultez les [recommandations Keycloak sur le nom d’hôte](https://www.keycloak.org/server/hostname). L’adresse de service annoncée par Keycloak doit correspondre au déploiement prévu.
5. Faites appliquer par l’exploitant uniquement une procédure de nom d’hôte et de certificat vérifiée pour l’image cible. Ne combinez pas des exemples de TLS directement dans Keycloak avec un proxy inverse terminant TLS sans vérifier l’architecture réelle. Consultez les [recommandations Keycloak sur le proxy inverse](https://www.keycloak.org/server/reverseproxy).

**⚠️ À valider sur l’image cible :** outil et syntaxe du nom d’hôte, installation du certificat, services affectés, comportement au redémarrage, éventuelles ouvertures réseau et procédure de renouvellement. Tant que ces éléments ne sont pas établis, ce brouillon ne fournit pas de procédure de configuration exécutable.

## Vérifier le résultat

Après une modification de configuration approuvée :

1. Ouvrez l’adresse HTTPS convenue depuis un réseau client prévu.
2. Vérifiez que le client approuve le certificat sans exception et que le nom d’hôte est correct.
3. Vérifiez que les URL générées par Keycloak et les redirections applicatives utilisent l’adresse de service prévue.
4. Attribuez la responsabilité du renouvellement et testez le processus dans un environnement de test approprié. Consignez comment l’expiration et les échecs de renouvellement seront détectés.

**Résultat attendu :** le nom d’hôte convenu est accessible par HTTPS de confiance et le cycle de vie du certificat a un responsable. Accéder à une page en ignorant les erreurs de certificat n’est pas un contrôle TLS réussi.

## En cas d’échec d’un contrôle

Distinguez la résolution DNS, l’accessibilité réseau, les erreurs de confiance ou de nom du certificat et les URL générées incorrectes. Ne désactivez pas les contrôles de nom d’hôte, n’exposez pas les interfaces internes et ne contournez pas la vérification de confiance comme correction permanente. Consultez le [dépannage](07-troubleshoot-and-get-support-fr.md).

**Suite :** accomplir la [configuration de l’administrateur initial](03-complete-initial-access-fr.md) si elle reste à faire, puis [configurer Keycloak](05-configure-keycloak-fr.md).
