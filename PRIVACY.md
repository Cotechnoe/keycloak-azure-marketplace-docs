# Privacy notice — Cotechnoe Keycloak™ IAM for Azure

**Last updated:** 2026-11-07

This notice describes privacy aspects of the Cotechnoe Keycloak virtual machine image offered through Azure
Marketplace. It does not replace Microsoft's privacy terms for Azure or the privacy notices of services that you
connect to the VM.

## Data handled by the VM

Keycloak and its local PostgreSQL database run on the virtual machine deployed in your Azure subscription. They
process the identity, account, authentication, configuration and audit data that you or your users provide or
generate while using Keycloak. You administer this data and are responsible for configuring access, retention,
backups and any legal notices required for your users.

The image generates instance-specific administrator and database credentials during first boot. It does not
include shared credentials. The image is designed not to send Keycloak identity data, application data or usage
telemetry to Cotechnoe during normal operation. Cotechnoe does not receive access to your VM or its data by
default.

## Azure and connected services

Microsoft operates the Azure infrastructure and may process account, subscription, billing, diagnostic and
service data under the terms and privacy notices applicable to your Azure services. Review the
[Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement) and the terms for your Azure
subscription.

Your VM may communicate with Azure platform endpoints and with services you configure. For example, requesting
an optional Let's Encrypt certificate contacts the certificate authority. Identity providers, applications,
directory services, DNS providers, backup destinations and other integrations you connect may receive data
according to their own configuration and privacy terms. These services are not operated by Cotechnoe as part of
this image.

## Information you send to Cotechnoe

If you contact Cotechnoe for support, Cotechnoe will use the contact details and diagnostic information you
choose to provide to respond to and manage your request. Do not send passwords, private keys, access tokens or
unnecessary personal data. Cotechnoe does not have access to VM logs or customer data unless you choose to share
them or separately grant access.

## Your responsibilities and choices

You control the Azure region and network configuration for the VM, who can administer it, how Keycloak is
configured, and how its data is protected, retained, backed up or deleted. You are responsible for informing
your users about your identity service and for meeting privacy and data-protection obligations that apply to
your deployment. The image alone does not guarantee data residency, regulatory compliance or digital sovereignty.

## Contact

For privacy questions about this Marketplace image, contact:

**Cotechnoe privacy contact:** ⚠️ To be confirmed before publication.

## Publisher publication checklist

Before publishing this notice, confirm the publisher's legal entity and privacy contact, and document the
retention and handling process for support requests. Also confirm that the statements above still match the
released image and its configured integrations.
