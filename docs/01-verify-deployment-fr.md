---
title: Vérifier votre déploiement
lang: fr
---
# Vérifier votre déploiement

[English](01-verify-deployment.md) · Français

[Accueil de la documentation](../README-fr.md)

## Avant de commencer

Munissez-vous de l’abonnement Azure et du groupe de ressources utilisés pour le déploiement, des autorisations de lecture des ressources et du dossier de déploiement de votre organisation. Si une autre personne a déployé la VM, demandez-lui de l’identifier plutôt que de sélectionner une ressource au nom similaire.

## Inspecter le déploiement Azure

Les libellés du portail ci-dessous suivent la documentation Microsoft anglaise ; leur traduction peut différer. Il s’agit d’inspection, pas d’instructions de création, de redémarrage ou de suppression de ressources.

1. Dans le portail Azure, recherchez **Virtual machines**, sélectionnez la VM prévue et vérifiez l’abonnement et le groupe de ressources sur sa page **Overview**. Si vous venez de terminer le déploiement, **Go to resource** ouvre la ressource. Ces points d’entrée sont décrits dans le [démarrage rapide Microsoft du portail](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal) ; ne suivez pas ses étapes de création ou de suppression pour un déploiement existant.
2. Ouvrez le groupe de ressources, sélectionnez le lien sous **Deployments**, puis le déploiement correspondant à votre VM. Consignez son état signalé, l’heure du déploiement et l’identifiant de corrélation dans un dossier d’exploitation protégé. Microsoft documente ce chemin dans l’[historique des déploiements](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history). Examinez les détails d’erreur en cas d’échec ; ne supposez pas que le déploiement le plus récent est le vôtre.
3. Consignez l’état d’alimentation signalé de la VM séparément de l’état du déploiement. Utilisez les [explications Microsoft sur les états des VM](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) : `Running` décrit l’alimentation ; le provisionnement `Succeeded` signifie que la dernière opération sur la ressource VM a réussi. Aucun des deux ne prouve que Keycloak est prêt. Si un état n’est pas visible avec vos autorisations, consignez-le comme inconnu et sollicitez l’administrateur Azure ; ne déduisez pas une réussite.
4. Si le provisionnement a échoué, conservez le code d’erreur et les détails de l’opération, retirez les valeurs sensibles avant tout partage et consultez le [dépannage](07-troubleshoot-and-get-support-fr.md). Ne supprimez pas la VM ou ses disques comme première action de diagnostic.
5. Identifiez les ressources de stockage et de réseau rattachées. Demandez au responsable du déploiement d’expliquer toute ressource inattendue ou absence de stockage de données avant d’ajouter des données de votre organisation.

**Résultat attendu :** votre dossier protégé identifie la VM, l’abonnement, le groupe de ressources, l’état, l’heure et l’identifiant de corrélation du déploiement, l’état d’alimentation observé séparément et toute erreur. Consignez la référence d’image provenant du dossier vérifié du responsable du déploiement lorsqu’elle est disponible ; sinon, marquez-la inconnue. Un provisionnement réussi ou une VM en cours d’exécution n’est **pas** un test de connexion à Keycloak.

## Vérifier séparément l’état de préparation de l’application

Si vous ne disposez pas encore d’un accès VM approuvé, suspendez cette tâche et accomplissez [Sécuriser votre accès d’administration Azure](02-secure-azure-access-fr.md). Ce guide vous ramène explicitement au présent contrôle. Ne déclarez pas l’application prête pendant la préparation de l’accès.

Avec l’accès VM approuvé, vérifiez l’initialisation de l’application et la santé du service avec la procédure validée pour l’image exacte.

**⚠️ À valider sur l’image cible :** service d’initialisation, adresse du contrôle de santé, commandes de diagnostic, indicateurs de réussite et durée d’initialisation attendue. Aucun chemin de fichier, port ou délai garanti n’est fourni ici.

Consignez l’état de préparation de l’application séparément de l’état Azure. Si le contrôle propre à l’image n’est pas disponible, le résultat de préparation de l’application est **non vérifié**. Ne connectez pas de vrais utilisateurs sur cette base.

Cette distinction suit les [recommandations Microsoft sur la fiabilité des VM](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/virtual-machines) : la charge de travail dépend d’autres éléments que la seule ressource VM.

## En cas d’échec d’un contrôle

- **VM introuvable :** vérifiez l’abonnement, le groupe de ressources et vos autorisations de lecture avec le responsable du déploiement.
- **Échec du provisionnement :** conservez l’erreur et contactez le canal d’assistance Azure ou de l’image approprié.
- **VM en cours d’exécution mais application indisponible :** conservez l’état Azure comme élément de diagnostic ; ne le considérez pas comme une preuve de réussite de l’initialisation applicative.

Consultez [Diagnostiquer un problème et demander de l’aide](07-troubleshoot-and-get-support-fr.md) pour préparer les informations sans exposer de secrets.

**Suite :** uniquement après l’accès VM approuvé et la réussite du contrôle de préparation applicative, poursuivez avec [Configurer votre domaine et HTTPS de confiance](04-configure-domain-and-tls-fr.md). Si l’un des deux manque ou reste non vérifié, arrêtez-vous et demandez des précisions plutôt que de passer aux identifiants.
