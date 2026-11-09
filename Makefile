SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help setup build check serve

help: ## Afficher les commandes locales
	@printf '%s\n' 'make setup  Installer les gems dans vendor/bundle via Docker' 'make build  Construire le site Jekyll dans _site/' 'make check  Construire et verifier les sources et le rendu' 'make serve  Previsualiser sur http://127.0.0.1:4000/keycloak-azure-marketplace-docs/'

setup: ## Installer les dependances sans modifier Ruby sur le poste
	@bash scripts/site.sh setup

build: ## Construire le site sans le publier
	@bash scripts/site.sh build

check: ## Verifier les sources et les liens du site genere
	@bash scripts/site.sh check

serve: ## Servir localement sans publication
	@bash scripts/site.sh serve
