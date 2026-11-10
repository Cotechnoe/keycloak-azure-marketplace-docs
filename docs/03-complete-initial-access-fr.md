---
title: Finaliser votre premier accès à Keycloak
lang: fr
---
# Finaliser votre premier accès à Keycloak

[English](03-complete-initial-access.md) · Français

[Accueil de la documentation](../README-fr.md)

## Avant de commencer

- Disposez d’un [accès d’administration approuvé](02-secure-azure-access-fr.md).
- Vérifiez l’adresse d’administration dans un dossier de déploiement fiable.
- Disposez de HTTPS de confiance pour cette adresse. Sinon, accomplissez d’abord la [préparation domaine et TLS](04-configure-domain-and-tls-fr.md). Ne saisissez pas d’identifiants après avoir contourné un avertissement de certificat.
- Prévoyez un emplacement approuvé pour conserver les identifiants et un plan de récupération de compte.

## Récupérer les identifiants initiaux et se connecter

La récupération des identifiants par SSH et la connexion dans le navigateur ont été vérifiées le 2026-11-10 sur une VM déployée depuis l’image `26.8.20261108`, exécutant Keycloak `26.8.2`. Les autres versions d’image nécessitent une vérification distincte.

1. Dans votre propre terminal, remplacez les valeurs d’exemple ci-dessous par le chemin de votre clé privée SSH, le nom de l’administrateur Linux choisi au déploiement et l’adresse de la VM :

   ```sh
   ssh -i /path/to/private-key linux-admin@vm-address \
     'sudo cat /root/keycloak-initial-admin.txt'
   ```

   La commande affiche des identifiants sensibles. Exécutez-la uniquement dans un terminal privé ; ne copiez pas la sortie dans une conversation, une capture d’écran, un journal ou une demande d’assistance. Si le fichier est absent, arrêtez-vous et suivez les consignes ci-dessous en cas d’échec d’accès.
2. Relevez `KC_ADMIN_USERNAME` et `KC_ADMIN_PASSWORD` dans la sortie. Ce sont les identifiants Keycloak, pas votre compte Linux SSH ni votre compte Azure. Copiez uniquement chaque valeur, sans le préfixe `KEY=`.
3. Ouvrez `https://<verified-hostname>/admin/` avec le nom d’hôte d’administration configuré pour votre VM. Une adresse IP a servi à la validation isolée ; cela ne démontre pas un HTTPS de confiance pour votre déploiement. Accomplissez les prérequis domaine et TLS ci-dessus avant de saisir les identifiants.
4. Saisissez la valeur de `KC_ADMIN_USERNAME` dans **Username or email**, celle de `KC_ADMIN_PASSWORD` dans **Password**, puis sélectionnez **Sign In**.

Le compte initial est temporaire. Une connexion réussie ne termine pas la mise en place de l’administration permanente.

## Établir une administration permanente

La séquence suivante décrit le parcours prévu. Les attributions précises de rôles et les étapes d’interface pour créer et retirer les administrateurs restent à valider sur votre image.

1. Récupérez les identifiants initiaux avec la procédure ci-dessus et gardez les valeurs privées.
2. Connectez-vous uniquement à l’adresse d’administration vérifiée.
3. Établissez un administrateur permanent disposant des privilèges nécessaires aux tâches prévues. Suivez le [guide d’administration Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html) applicable à la version installée. Ne supposez pas que les autorisations Azure attribuent des autorisations Keycloak.
4. Vérifiez l’administrateur permanent dans une session distincte avant de retirer l’accès temporaire. Contrôlez les tâches administratives nécessaires, pas seulement la réussite de la connexion. Configurez et testez la protection d’authentification et la méthode de récupération exigées par votre organisation.
5. Supprimez le compte temporaire avec la procédure vérifiée de gestion des comptes. Keycloak précise que les [comptes administrateurs d’amorçage sont temporaires et doivent être supprimés manuellement](https://www.keycloak.org/server/bootstrap-admin-recovery).
6. Confirmez que le compte temporaire ne peut plus être utilisé. Supprimez ou retirez ensuite les éléments d’authentification initiaux selon la procédure propre à l’image et la politique de votre organisation. La suppression d’un fichier d’identifiants ne prouve pas à elle seule que le compte a été supprimé.

**Résultat attendu :** un administrateur permanent vérifié accomplit les tâches prévues, l’accès temporaire ne fonctionne plus et les éléments d’authentification initiaux sont traités de manière sécurisée.

**⚠️ À valider sur l’image cible :** attributions précises de rôles et étapes d’interface pour l’administration permanente, suppression de l’accès temporaire et nettoyage des identifiants. Ces opérations n’étaient pas couvertes par la validation de la connexion initiale ci-dessus.

## En cas d’échec d’accès

Arrêtez-vous si l’adresse ou le certificat est inattendu, si les identifiants initiaux sont indisponibles ou si les autorisations permanentes ne peuvent pas être vérifiées. Ne supprimez pas le seul administrateur fonctionnel. Ne relancez pas l’initialisation et ne tentez pas de commande de récupération de compte sur la base de données en service à partir d’un exemple d’une autre version.

Contactez l’[assistance](../SUPPORT-fr.md) pour les précisions propres à l’image. La [référence Keycloak sur la récupération](https://www.keycloak.org/server/bootstrap-admin-recovery) contient des prérequis à évaluer pour votre déploiement avant toute récupération.

**Suite :** le jalon d’administration permanente est terminé uniquement si les contrôles ci-dessus réussissent. Vous pouvez arrêter cette session de mise en service ici sans application externe. Lorsqu’un responsable applicatif est prêt, poursuivez avec [Configurer Keycloak pour votre organisation](05-configure-keycloak-fr.md). Avant de vrais utilisateurs, accomplissez [Exploiter, protéger et restaurer votre déploiement](06-operate-and-recover-fr.md) ; l’accès administratif seul ne démontre pas une aptitude à la production.
