# Issue #3 — Étape 1 : inventaire factuel

**Statut :** étape de cadrage interne, non destinée aux clients

**Date de l’inventaire :** 2026-11-09

**Branche :** `docs/issue-3-step-1-fact-inventory`

Cet inventaire prépare l’architecture et la rédaction de la documentation client. Il ne constitue ni une procédure d’exploitation validée, ni une déclaration de disponibilité Marketplace. Les chemins de sources d’implémentation ci-dessous désignent le checkout local distinct du dépôt public de documentation ; aucun lien vers ce dépôt d’ingénierie n’est publié.

## État de livraison

| Élément | Fait établi | Source / limite |
|---|---|---|
| Disponibilité Marketplace | Le demandeur confirme que l’application n’est pas encore livrée sur Marketplace et que le déploiement est en cours. | Confirmation du demandeur le 2026-11-09. L’état du portail Partner Center n’a pas été vérifié indépendamment dans ce travail. |
| Identifiant technique | La configuration d’ingénierie utilise `keycloak-iam` comme identifiant d’offre. | `env/.env.dev`, lignes 29 et 45, du checkout d’ingénierie. Cet identifiant ne démontre pas le nom d’affichage ou le titre commercial final. |
| Nom d’affichage | Un champ de titre est configuré localement, mais sa valeur n’a pas été confirmée dans une fiche Marketplace publiée. | `env/.env.dev`, ligne 46, du checkout d’ingénierie. Ne pas reprendre le titre candidat dans le contenu client avant confirmation dans Partner Center. |
| Image à documenter | Aucune version d’image n’est retenue comme cible de la documentation à ce stade. | `env/.env.dev`, ligne 34, comporte une modification locale non commitée ; `CONTEXT.md`, lignes 15 et 19, décrit séparément un build récent et l’état de l’entrée Partner Center. Ces sources ne désignent pas une cible unique et approuvée. Ne pas recopier une version provenant de ces états sans confirmation. |
| Produit et plan commercial | Le nom d’affichage, le plan, les régions et les tailles VM effectivement proposés au client ne sont pas confirmés par une publication Marketplace. | À confirmer dans la fiche finale Partner Center après la fin du déploiement et avant d’écrire des instructions dépendantes de ces choix. |

## Faits d’implémentation démontrés par les sources locales

Ces éléments décrivent le comportement implémenté dans les sources examinées. Ils ne prouvent pas à eux seuls que la version correspondante est celle qui sera publiée, ni que le parcours a été rejoué sur l’image Marketplace.

| Domaine | Fait démontré | Source d’implémentation |
|---|---|---|
| Architecture réseau | Nginx écoute sur HTTP et HTTPS ; HTTP est redirigé vers HTTPS. Le modèle TLS configuré accepte TLS 1.2 et 1.3. | `packer/files/nginx-keycloak.conf`, lignes 8–37 |
| Accès Keycloak | Le modèle de configuration lie l’interface HTTP de Keycloak à `127.0.0.1`. Nginx sert de proxy local. | `packer/files/keycloak.conf.template`, lignes 18–29 ; `packer/files/nginx-keycloak.conf`, lignes 55–63 |
| Santé et gestion | Le modèle lie l’interface de gestion à `127.0.0.1`; le script de premier démarrage attend `/health/ready` avant de déclarer la configuration initiale terminée. | `packer/files/keycloak.conf.template`, lignes 23–25 ; `packer/files/keycloak-firstboot.sh`, lignes 329–340 |
| Démarrage | Keycloak est lancé par systemd en mode `start --optimized`. Un service distinct exécute la configuration de premier démarrage et utilise une sentinelle d’achèvement. | `packer/files/keycloak.service`, lignes 7–15 ; `packer/files/keycloak-firstboot.service`, lignes 1–12 ; `packer/files/keycloak-firstboot.sh`, lignes 20–24 |
| Compte initial | Le script de premier démarrage accepte des paramètres d’installation ou génère le mot de passe si aucun n’est fourni. Le fichier d’accès initial est écrit avec des permissions `0600` et son contenu le décrit comme temporaire. | `packer/files/keycloak-firstboot.sh`, lignes 99–145 et 284–297 |
| Données de base | PostgreSQL est configuré localement. Le script utilise le disque de données Azure sur LUN 0 lorsqu’il est présent ; en son absence, il choisit le disque OS et journalise un avertissement. Il génère le mot de passe de base sur la VM et ne le journalise pas. | `packer/files/keycloak.conf.template`, lignes 13–16 ; `packer/files/keycloak-firstboot.sh`, lignes 150–163 et 197–229 |
| Nom d’hôte et certificat | Le premier démarrage génère un certificat autosigné. L’outil `keycloak-set-hostname` permet de configurer un FQDN et un certificat autosigné ou de demander un certificat Let’s Encrypt ; son exécution redémarre Keycloak. | `packer/files/keycloak-firstboot.sh`, lignes 264–283 ; `packer/files/keycloak-set-hostname.sh`, lignes 5–12 et 61–101 |
| Vérifications présentes | Les tests de certification vérifient notamment l’écoute locale des services internes, la redirection HTTP→HTTPS, l’état des services et le endpoint de santé. | `tests/image-validation/certification-checks.sh`, lignes 72–102 |
| Déploiement mono-VM | Les sources examinées décrivent un ensemble local Nginx, Keycloak et PostgreSQL dans la VM. Elles ne démontrent pas une architecture haute disponibilité ou une réplication entre plusieurs VM. | `packer/files/keycloak.service`, lignes 1–5 ; `packer/files/keycloak.conf.template`, lignes 13–25 ; `packer/files/nginx-keycloak.conf` |

## Informations à confirmer avant rédaction client

- L’identifiant d’image Marketplace exact retenu pour la livraison, son système d’exploitation, sa version et la preuve qu’il correspond à l’image déployée.
- Le titre commercial final, le plan, les régions, les tailles VM et les paramètres réellement exposés au client dans le parcours Partner Center.
- L’état final de publication et les liens Marketplace que le client verra ; aucune URL d’achat ou disponibilité publique n’est attestée ici.
- Le premier accès réellement présenté au client, le nom d’utilisateur par défaut éventuel, la manière sécurisée de lire les identifiants et les étapes exactes pour remplacer l’administrateur temporaire.
- Les paramètres réseau effectifs du plan publié, notamment les règles NSG et les ports exposés au client ; les tests ou fichiers d’infrastructure locaux ne remplacent pas la vérification de la configuration finale du Marketplace.
- Les responsabilités et options effectivement activées pour sauvegarde, restauration, surveillance, mises à jour, alertes, coûts et support. Aucune intégration Azure correspondante n’est considérée comme incluse sans preuve.
- Le parcours de configuration initiale Keycloak et d’intégration des applications, à confirmer sur l’image et dans l’interface réellement livrées.
- Le comportement réel du certificat et du nom d’hôte après le déploiement, ainsi que les prérequis DNS/réseau associés au plan publié.
- Les procédures de reprise et de mise à niveau sur une cible isolée, avant de les documenter comme sûres.

## Références Microsoft Learn à utiliser pour les recommandations Azure

Ces pages sont des références primaires pour préparer les recommandations des étapes suivantes. Elles ne prouvent pas qu’une fonctionnalité Azure est activée ou incluse dans l’offre.

- [Architecture best practices for Azure Virtual Machines — Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/virtual-machines) — fiabilité, état, résilience et exploitation des VM.
- [Network security groups overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) — filtrage du trafic réseau Azure.
- [About Azure VM backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction) — capacités et fonctionnement d’Azure Backup pour les VM.
- [Azure Update Manager overview](https://learn.microsoft.com/en-us/azure/update-manager/overview) — évaluation et gestion des mises à jour.
- [Monitor virtual machines with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/monitor-vm) — supervision des VM.

## Portée de cette vérification

- Sources locales d’implémentation et de validation inspectées ; les affirmations ci-dessus sont limitées à ce qu’elles montrent.
- Aucun accès au portail Partner Center ni à une VM Marketplace en cours de déploiement n’a été utilisé pour cet inventaire.
- Aucune commande opérationnelle n’a été exécutée sur une VM et aucun parcours de déploiement, de sauvegarde ou de restauration n’a été rejoué.
- Aucune version n’est désignée comme version testée ou version de livraison.
- La prochaine étape est de valider la cible d’image et les points en attente, puis de proposer l’architecture de l’information. Aucune page client n’est rédigée dans cette étape.
