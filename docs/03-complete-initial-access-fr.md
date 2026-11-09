# Finaliser votre premier accès à Keycloak

[English](03-complete-initial-access.md) | Français

[Accueil de la documentation](../README-fr.md)

> **Brouillon de prépublication.** La récupération des identifiants, l’adresse initiale de la console et la procédure exacte de création d’un administrateur permanent pour cette image sont ⚠️ à valider. Ne devinez pas les identifiants, ne copiez pas les commandes d’une autre image et ne considérez pas cette page comme une procédure d’initialisation testée.

## Avant de commencer

- Disposez d’un [accès d’administration approuvé](02-secure-azure-access-fr.md).
- Vérifiez l’adresse d’administration dans un dossier de déploiement fiable.
- Disposez de HTTPS de confiance pour cette adresse. Sinon, accomplissez d’abord la [préparation domaine et TLS](04-configure-domain-and-tls-fr.md). Ne saisissez pas d’identifiants après avoir contourné un avertissement de certificat.
- Prévoyez un emplacement approuvé pour conserver les identifiants et un plan de récupération de compte.

## Établir une administration permanente

La séquence suivante décrit le parcours prévu, pas des instructions d’exécution propres à l’image.

1. Obtenez l’accès initial par le mécanisme de remise confirmé pour votre image exacte. Gardez les valeurs privées. N’incluez jamais un fichier d’identifiants ou son contenu dans une demande d’assistance.
2. Connectez-vous uniquement à l’adresse d’administration vérifiée.
3. Établissez un administrateur permanent disposant des privilèges nécessaires aux tâches prévues. Suivez le [guide d’administration Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html) applicable à la version installée. Ne supposez pas que les autorisations Azure attribuent des autorisations Keycloak.
4. Vérifiez l’administrateur permanent dans une session distincte avant de retirer l’accès temporaire. Contrôlez les tâches administratives nécessaires, pas seulement la réussite de la connexion. Configurez et testez la protection d’authentification et la méthode de récupération exigées par votre organisation.
5. Supprimez le compte temporaire avec la procédure vérifiée de gestion des comptes. Keycloak précise que les [comptes administrateurs d’amorçage sont temporaires et doivent être supprimés manuellement](https://www.keycloak.org/server/bootstrap-admin-recovery).
6. Confirmez que le compte temporaire ne peut plus être utilisé. Supprimez ou retirez ensuite les éléments d’authentification initiaux selon la procédure propre à l’image et la politique de votre organisation. La suppression d’un fichier d’identifiants ne prouve pas à elle seule que le compte a été supprimé.

**Résultat attendu :** un administrateur permanent vérifié accomplit les tâches prévues, l’accès temporaire ne fonctionne plus et les éléments d’authentification initiaux sont traités de manière sécurisée.

**⚠️ À valider sur l’image cible :** mode de remise des identifiants initiaux, nom d’utilisateur et adresse initiale de la console, attributions précises de rôles et étapes d’interface, suppression de l’accès temporaire et nettoyage des identifiants. Ces détails doivent être vérifiés avant d’exécuter cette séquence sur l’offre.

## En cas d’échec d’accès

Arrêtez-vous si l’adresse ou le certificat est inattendu, si les identifiants initiaux sont indisponibles ou si les autorisations permanentes ne peuvent pas être vérifiées. Ne supprimez pas le seul administrateur fonctionnel. Ne relancez pas l’initialisation et ne tentez pas de commande de récupération de compte sur la base de données en service à partir d’un exemple d’une autre version.

Contactez l’[assistance](../SUPPORT-fr.md) pour les précisions propres à l’image. La [référence Keycloak sur la récupération](https://www.keycloak.org/server/bootstrap-admin-recovery) contient des prérequis à évaluer pour votre déploiement avant toute récupération.

**Suite :** [Configurer votre domaine et HTTPS de confiance](04-configure-domain-and-tls-fr.md), ou vérifier le résultat si cette tâche est déjà accomplie.
