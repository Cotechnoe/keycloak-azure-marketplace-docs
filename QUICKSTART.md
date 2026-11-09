---
title: "Quick start: establish permanent administration"
---
# Quick start: establish permanent administration

English · [Français](QUICKSTART-fr.md)

[Documentation home](README.md)

> **Pre-release draft.** The application has not been released on Microsoft Marketplace. The target image is not yet confirmed. Credential retrieval, service addresses and image-specific commands are **⚠️ to be validated**. This quick start is a short route through the guides, not a tested deployment procedure.

## Before you start

Have your Azure subscription and resource group, permission to inspect the deployed VM, an approved way to obtain management access, and access to the DNS and certificate owners. You do not need an external application to complete the administrative milestone. Image-specific instructions must still be verified before execution.

## Reach the administrative milestone

1. **Find your VM and check its Azure state.** In the Azure portal, locate the intended VM and record its deployment and power states. Leave application readiness marked as not verified until management access is available. See [Verify your deployment](docs/01-verify-deployment.md).
2. **Confirm restricted VM access, then check application readiness.** Follow [Secure your Azure administration access](docs/02-secure-azure-access.md), then complete the application-readiness check in the deployment guide before continuing. Use only a procedure verified for your image; stop if it is unavailable. A running VM alone does not establish that Keycloak is ready. Do not open management access to all sources.
3. **Verify the service address and trusted HTTPS.** Use the address confirmed by your deployment owner. Before entering credentials, complete the result checks in [Configure your domain and trusted HTTPS](docs/04-configure-domain-and-tls.md), even if HTTPS already works: client trust, intended URLs, a named renewal owner, a tested renewal process and detection of expiry or renewal failures. Do not reconfigure working HTTPS unnecessarily; apply only missing configuration through a procedure verified for your image.
4. **Replace temporary administrator access.** Obtain initial credentials only through the mechanism confirmed for your image. Establish and test a permanent administrator in a separate session before removing temporary access and retiring its credential material. See [Complete your initial Keycloak access](docs/03-complete-initial-access.md).

**Stop at an unverified image-specific procedure.** Do not guess a console URL, credential location, command or configuration value. Ask for the missing instructions through [support](SUPPORT.md) before continuing. Never bypass a certificate warning or remove your only working administrator.

## Check the administrative result

- [ ] Azure resource state and application readiness have been checked separately.
- [ ] Authorized operators have a verified, restricted management connection.
- [ ] The agreed service address uses HTTPS trusted by the intended client; certificate renewal has an owner, a tested process and defined failure detection.
- [ ] Permanent administration works and temporary access no longer works.

You may finish this administrative milestone here without an external application. It is **not production readiness** and does not demonstrate application integration.

## Continue with an application when ready

This is a separate, optional continuation of the quick start, not a requirement for completing administrative access. Involve an application owner and use test accounts without production data. Before real users can sign in to an application, its integration must be configured and tested.

1. With the application owner, configure a test realm, user and client appropriate to the application. See [Configure Keycloak for your organization](docs/05-configure-keycloak.md).
2. Start sign-in from that application and verify the resulting session.
3. Check that an unauthorized user is denied the intended access.

- [ ] The test application accepts the intended user and rejects unauthorized access.

Deploying the VM does not automatically integrate your applications. This application test is also **not production readiness**.

## Before you connect real users

Complete [Operate, protect and recover your deployment](docs/06-operate-and-recover.md): arrange and test recovery, assign maintenance and monitoring owners, and review availability and costs.

If a check fails, use [Troubleshoot and request help](docs/07-troubleshoot-and-get-support.md). Share only redacted error details, never credentials, tokens or private keys.

## Primary references

- Microsoft: [VM states and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) and [least-privilege Azure access](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices).
- Keycloak: [hostname configuration](https://www.keycloak.org/server/hostname), [temporary administrator removal](https://www.keycloak.org/server/bootstrap-admin-recovery) and [application integration](https://www.keycloak.org/securing-apps/overview).

These references explain general platform or upstream behavior. They do not prove which features are configured in the image.
