# Cotechnoe Keycloak IAM for Azure

> **Under construction:** Cotechnoe is actively developing this solution and its documentation.
> The Azure Marketplace offer is not yet publicly available. Features and instructions may change
> before release; the content below describes the solution being prepared.

Deploy and operate a self-managed Keycloak™ identity and access management server using the Cotechnoe
virtual machine image for Azure Marketplace. This repository contains customer-facing documentation;
it is not the Keycloak source code repository.

## An identity layer for open ecosystems

Use Keycloak to centralize sign-in for compatible web applications and APIs. It can serve as the identity
layer for open-source knowledge bases, repositories, semantic data platforms and collaboration tools,
including [other solutions offered by Cotechnoe](https://www.cotechnoe.com/marketplace/).
Those solutions are deployed separately and are not included in this image. Application integrations
require configuration; they are not automatically provided by deploying the VM.

## What the image provides

- Keycloak with OpenJDK, a local PostgreSQL database and an Nginx HTTPS reverse proxy.
- Single sign-on using OpenID Connect, OAuth 2.0 and SAML 2.0.
- Identity brokering and user federation with LDAP or Active Directory.
- Instance-specific initial administrator and database credentials, with no shared credentials embedded
  in the image.
- An optional data disk for database storage.

For Keycloak product capabilities and configuration, see the
[official Keycloak documentation](https://www.keycloak.org/documentation).

## Get started after deployment

1. Connect to the VM over SSH using the Azure administrator account configured during deployment.
2. Retrieve the initial Keycloak administrator credentials:

   ```bash
   sudo cat /root/keycloak-initial-admin.txt
   ```

3. Open the console URL recorded in that file.
4. Sign in, create a permanent administrator and delete the temporary administrator account.
5. Configure a DNS name and a trusted HTTPS certificate before connecting users and applications.

Do not share the credentials file or include its contents in support requests.

## Digital sovereignty and data control

Keycloak and PostgreSQL run on the VM in your Azure subscription. You manage the service, administrators,
network exposure, connected applications, backups and data retention. Open identity protocols let you
connect compatible applications without requiring a Cotechnoe-hosted identity service.

These choices support control over your identity infrastructure, but the image alone does not guarantee
data residency, regulatory compliance or digital sovereignty. Outcomes depend on your Azure configuration,
operating practices and connected services.

## Operate your deployment

This is a single-node deployment. High availability, clustering, backups, updates and recovery planning
are your responsibility. An optional data disk separates database storage from the operating-system disk;
it is not a substitute for backups.

Deployment, HTTPS configuration, backup, upgrade and troubleshooting guides will be added to this repository.

## Privacy

Read the [Privacy Notice](./PRIVACY.md) for information about data handled by the VM, Azure, connected services
and support requests.

**Documentation status:** the privacy notice is a draft. The publisher's legal entity, privacy contact and
support-data retention process must be confirmed before using it as the Marketplace privacy policy.

## Support and documentation feedback

For questions about the Cotechnoe image or corrections to this documentation,
[open an issue](https://github.com/Cotechnoe/keycloak-azure-marketplace-docs/issues).
Issues are public: do not include passwords, tokens, private keys or personal data. Redact diagnostic logs
before sharing them.

Cotechnoe's support scope covers the packaging and deployment of this image. For Keycloak product
documentation and community resources, use the [Keycloak website](https://www.keycloak.org/documentation).

## Trademarks

Keycloak is a trademark of The Linux Foundation. Cotechnoe is not affiliated with, sponsored by or endorsed
by The Linux Foundation, the Cloud Native Computing Foundation or the Keycloak project.
