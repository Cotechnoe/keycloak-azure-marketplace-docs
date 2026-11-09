# Review privacy considerations for your deployment

English | [Français](PRIVACY-fr.md)

[Documentation home](README.md)

> **Pre-release draft — not a finalized Marketplace privacy policy.** The application has not been released on Microsoft Marketplace. The target image and its data flows are ⚠️ to be validated. This page must not be used as evidence of a legal or technical compliance review.

## Review the data your identity service handles

Keycloak's [administration guide](https://www.keycloak.org/docs/latest/server_admin/index.html) describes users, credentials, attributes, roles and sessions. Review which information your own configuration collects and exposes to applications.

Identify who can administer the service, which systems receive identity information, how logs and backups are protected, and how your organization handles access, retention and deletion. The deployment does not by itself establish regulatory compliance or data residency.

**⚠️ To be validated for the target image:** actual stored data and log locations, default logging, credential handling, outbound connections, telemetry and any publisher access. This draft does not assert that a review of those behaviors has been completed.

## Review Azure and connected-service terms

Microsoft's [shared responsibility guidance](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) describes the distinction between the platform and the systems and data you operate. Review the [Microsoft Privacy Statement](https://www.microsoft.com/en-us/privacy/privacystatement) and the terms applicable to your Azure subscription.

For each application, directory, identity provider, certificate authority, DNS provider, monitoring service or backup destination you configure, review its data flows and privacy terms separately. Do not assume those services are part of the image or subject to a single privacy notice.

## Limit information in support requests

If you send a support request, share only the contact and diagnostic information necessary to investigate it. Public GitHub issues are visible to everyone.

Never share passwords, private keys, tokens, session cookies, credential files or unnecessary personal data. Redact logs before sharing them. Do not grant VM access simply to make a public report reproducible. See [support guidance](SUPPORT.md).

## Confirm the publisher notice before release

For a privacy question, contact Cotechnoe at [support@cotechnoe.com](mailto:support@cotechnoe.com). Do not include personal records or diagnostic archives in an initial message.

**⚠️ To be validated before publication:** the publisher-approved privacy notice, support-information handling and the correspondence between that notice and the image actually delivered.

Until that review is complete, this page is privacy guidance for a draft deployment journey, not the final Marketplace policy.
