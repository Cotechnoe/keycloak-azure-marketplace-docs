# Preview and validate the documentation locally

[Français](CONTRIBUTING-fr.md)

This contributor guide is excluded from the generated site. The operator guides remain the Markdown files at the root and in `docs/`; do not maintain a second copy of their content.

## Requirements

- Docker with a running engine.
- Make and Bash (the wrapper supports Bash 3.2).
- Python 3 for the standard-library-only validator.

Run all commands from this documentation repository, not the engineering repository:

```sh
make setup
make check
make serve
```

Open <http://127.0.0.1:4000/keycloak-azure-marketplace-docs/>. Stop the foreground preview with Ctrl+C. `make build` builds without serving. No command pushes, deploys or changes GitHub Pages settings.

`make setup` downloads a Ruby container pinned by digest and installs the Gemfile dependencies under ignored `vendor/bundle/`. It does not modify the host Ruby installation. Commit the generated `Gemfile.lock`; subsequent builds use it. Changing dependency versions requires rerunning setup and validation.

## Site behavior

- Jekyll reads the existing Markdown files, their front matter, `_config.yml` and `_layouts/default.html`.
- English home is `/`; French home is `/fr/`, below the configured project `baseurl`.
- `jekyll-relative-links` resolves Markdown links to the generated page URLs, including both home pages. Markdown links still work when reading the source on GitHub.
- The layout uses local CSS only, with no remote fonts, JavaScript, analytics or theme download.
- `_work/`, scripts, dependency files and this contributor guide are excluded from `_site/`. Never put secrets in documentation sources.
- The draft site carries `noindex, nofollow`. This is not access control. There is deliberately no deployment workflow.

`make check` rebuilds and checks the public page set, local rendered links and fragments, language navigation, source/rendered structure and EN/FR parity. It also runs six validator regression tests on isolated temporary copies of the build. It does not execute VM procedures, validate external HTTP responses or perform visual accessibility certification. Inspect the browser layout separately on desktop and a narrow viewport.

The GitHub Pages-compatible Jekyll line pulls in Ruby Sass, whose installer reports end-of-life; the site uses plain CSS and does not invoke Sass for its own assets. Ruby also reports future standard-library dependency changes. These warnings do not prevent the tested build, but must be considered when updating the toolchain.

The local build is the configured site renderer, not proof of an existing GitHub Pages deployment. Publication and the final public URL checks require separate authorization.

## Primary implementation references

- [GitHub: test a Jekyll site locally](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).
- [GitHub Pages dependency versions](https://pages.github.com/versions/): the direct Jekyll, relative-links and Markdown gem versions in the Gemfile follow this published matrix; this is not the entire `github-pages` bundle.
- [Jekyll front matter](https://jekyllrb.com/docs/front-matter/), [defaults](https://jekyllrb.com/docs/configuration/front-matter-defaults/) and [relative URL filter](https://jekyllrb.com/docs/liquid/filters/).
- [Official Ruby container tags](https://github.com/docker-library/official-images/blob/master/library/ruby): the runtime tag in the wrapper was verified here. This documentation runtime is unrelated to the VM image version.
