# Prévisualiser et valider la documentation localement

[English](CONTRIBUTING.md)

Ce guide de contribution est exclu du site généré. Les guides opérateur restent les fichiers Markdown à la racine et dans `docs/` ; ne maintenez pas un second exemplaire de leur contenu.

## Prérequis

- Docker avec un moteur en cours d’exécution.
- Make et Bash (le script est compatible Bash 3.2).
- Python 3 pour le validateur utilisant uniquement la bibliothèque standard.

Exécutez toutes les commandes depuis ce dépôt documentaire, pas le dépôt d’ingénierie :

```sh
make setup
make check
make serve
```

Ouvrez <http://127.0.0.1:4000/keycloak-azure-marketplace-docs/>. Arrêtez l’aperçu au premier plan avec Ctrl+C. `make build` construit sans servir. Aucune commande ne pousse, ne déploie ou ne modifie les paramètres GitHub Pages.

`make setup` télécharge un conteneur Ruby fixé par empreinte et installe les dépendances du Gemfile dans `vendor/bundle/`, ignoré par Git. Il ne modifie pas le Ruby du poste. Commitez le `Gemfile.lock` généré ; les builds suivants l’utilisent. Toute modification des versions exige de relancer l’installation et la validation.

## Fonctionnement du site

- Jekyll lit les fichiers Markdown existants, leur en-tête de métadonnées, `_config.yml` et `_layouts/default.html`.
- L’accueil anglais se trouve sous `/` et l’accueil français sous `/fr/`, après le `baseurl` du projet.
- `jekyll-relative-links` résout les liens Markdown vers les URL des pages générées, y compris les deux accueils. Les liens Markdown restent utilisables dans les sources GitHub.
- Le gabarit utilise uniquement du CSS local, sans police distante, JavaScript, analyse d’audience ou téléchargement de thème.
- `_work/`, les scripts, les fichiers de dépendances et ce guide sont exclus de `_site/`. Ne placez jamais de secrets dans les sources documentaires.
- Le site en brouillon porte `noindex, nofollow`. Ce n’est pas un contrôle d’accès. Aucun workflow de déploiement n’est ajouté.

`make check` reconstruit et contrôle l’ensemble des pages publiques, les liens locaux du rendu et leurs fragments, la navigation de langue, la structure source/rendu et la parité EN/FR. Il exécute aussi six tests de régression du validateur sur des copies temporaires isolées du build. Il n’exécute pas les procédures VM, ne contrôle pas les réponses HTTP externes et ne certifie pas l’accessibilité visuelle. Inspectez séparément la mise en page dans un navigateur sur écran large et étroit.

La branche Jekyll compatible avec GitHub Pages dépend de Ruby Sass, dont l’installation signale la fin de vie ; le site utilise du CSS simple et n’emploie pas Sass pour ses propres ressources. Ruby signale également des changements futurs de dépendances de bibliothèque standard. Ces avertissements n’empêchent pas le build testé, mais doivent être pris en compte lors des mises à jour de l’outillage.

Le build local utilise le moteur configuré pour le site ; il ne prouve pas l’existence d’un déploiement GitHub Pages. La publication et les contrôles des URL publiques finales nécessitent une autorisation distincte.

## Références primaires d’implémentation

- [GitHub : tester un site Jekyll localement](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).
- [Versions des dépendances GitHub Pages](https://pages.github.com/versions/) : les versions directes de Jekyll, relative-links et des gems Markdown dans le Gemfile suivent cette matrice publiée ; il ne s’agit pas du bundle `github-pages` complet.
- [Métadonnées Jekyll](https://jekyllrb.com/docs/front-matter/), [valeurs par défaut](https://jekyllrb.com/docs/configuration/front-matter-defaults/) et [filtre d’URL relative](https://jekyllrb.com/docs/liquid/filters/).
- [Tags officiels du conteneur Ruby](https://github.com/docker-library/official-images/blob/master/library/ruby) : le tag d’exécution du script a été vérifié ici. Ce moteur documentaire est indépendant de la version de l’image VM.
