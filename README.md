---
title: Operate your Keycloak VM after deployment
permalink: /
---
# Operate your Keycloak VM after deployment

English · [Français](README-fr.md)

**Review date:** 2026-11-10.

This documentation is for the Azure administrator or operator responsible for a VM deployed from the Cotechnoe offer. Start here after deploying your VM. It is not a sign-in guide for people using your organization's applications.

You do not need the publisher's build tools to use these guides. You do need permission to inspect your Azure deployment and an approved way to administer the VM.

## Start with the quick start

**At the Keycloak sign-in screen?** Follow [Retrieve the initial credentials and sign in](docs/03-complete-initial-access.md) for the SSH command, credential fields and administration URL. Your Linux SSH or Azure account is not the initial Keycloak account.

Use the [quick start](QUICKSTART.md) to reach a first milestone: verified permanent administration. A separate, optional continuation covers a first application sign-in when an application owner is ready. Both routes stop at unverified image-specific instructions.

## Follow your post-deployment checklist

| Step | Task | You are ready to continue when |
|---|---|---|
| 1 | [Verify your deployment](docs/01-verify-deployment.md) | You can identify your VM and distinguish Azure provisioning from application readiness. |
| 2 | [Secure your Azure administration access](docs/02-secure-azure-access.md) | Authorized operators have a restricted, tested management connection. |
| 3 | [Configure your domain and trusted HTTPS](docs/04-configure-domain-and-tls.md) | Your intended clients can reach the agreed hostname without a certificate warning. |
| 4 | [Complete your initial Keycloak access](docs/03-complete-initial-access.md) | A permanent administrator works and temporary access has been retired. |
| 5 | [Configure Keycloak for your organization](docs/05-configure-keycloak.md) | A test application and user complete the intended sign-in flow. |
| 6 | [Operate, protect and recover your deployment](docs/06-operate-and-recover.md) | You have owners, monitoring, maintenance and a tested recovery plan. |
| 7 | [Troubleshoot and request help](docs/07-troubleshoot-and-get-support.md) | You can identify the failing layer and prepare a safe support request. |

Use the troubleshooting guide at any step. **If your administration URL does not already have trusted HTTPS, complete the domain and TLS prerequisites before entering Keycloak credentials.** Do not bypass certificate warnings to follow the numbering.

Follow this execution order: Azure resource checks → approved VM access → application-readiness check → trusted HTTPS → permanent administrator. The deployment guide explains when to pause its health check until VM access is available. The file names are stable identifiers, not the execution order. Application integration and production preparation follow as separate tasks.

## Understand what you manage

An Azure VM is an infrastructure-as-a-service resource. Microsoft's [shared responsibility guidance](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) distinguishes the Azure platform from the operating system, applications, identities and data that you manage.

| Area | Your operational action |
|---|---|
| Azure resources and access | Review who can administer the resources and which network connections are allowed. |
| VM and application | Verify readiness, manage administrator access and plan maintenance. |
| Your organization's users and applications | Configure integrations and permissions. Deploying a VM does not establish a working application sign-in flow. |
| Data and continuity | Protect credentials, arrange backups, test recovery and define acceptable downtime. |
| Azure services you choose | Check compatibility, permissions, configuration and charges before enabling them. |

These are operational responsibilities, not a replacement for your agreements with Microsoft or Cotechnoe. Do not assume the image includes managed backups, Azure Monitor guest collection, update management, high availability or a support SLA.

## Know the limits of this documentation

- The initial-access guide identifies the image version used for its sign-in validation; this does not establish validation for other versions. No operating-system version, commercial display name, Marketplace plan, price or supported VM size is established by these guides.
- Keycloak's [official administration guide](https://www.keycloak.org/docs/latest/server_admin/index.html) describes upstream capabilities. A capability is not necessarily configured or verified in this offer.
- Applications, directories and external identity providers must be assessed and integrated separately. This documentation does not promise a bundled integration.
- Sections marked **⚠️ to be validated** are not instructions to execute on a production VM. Stop at that point and [request clarification](SUPPORT.md).
- English is the reference language; a French translation is available. Rendered-site validation and execution on the selected image remain separate delivery steps.

## Protect information when requesting help

Read the [support guidance](SUPPORT.md) and [privacy notice](PRIVACY.md). Never post passwords, private keys, tokens, cookies, administrator credential files or personal data in public issues.
