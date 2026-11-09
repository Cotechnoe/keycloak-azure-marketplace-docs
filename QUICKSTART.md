# Quick start: reach your first application sign-in

English | [Français](QUICKSTART-fr.md)

[Documentation home](README.md)

> **Pre-release draft.** The application has not been released on Microsoft Marketplace. The target image is not yet confirmed. Credential retrieval, service addresses and image-specific commands are **⚠️ to be validated**. This quick start is a short route through the guides, not a tested deployment procedure.

## Before you start

Have your Azure subscription and resource group, permission to inspect the deployed VM, an approved management connection, and access to the DNS and certificate owners. For the final check, involve an application owner and use test accounts without production data.

## Follow these five steps

1. **Find your VM and check readiness.** In the Azure portal, locate the intended VM and review its provisioning and power states. Check application readiness separately using the procedure verified for your image; a running VM alone does not establish that Keycloak is ready. See [Verify your deployment](docs/01-verify-deployment.md).
2. **Confirm restricted administration access.** Verify that an authorized operator can manage the VM through your approved route. Review permissions and network restrictions; do not open management access to all sources to get started. See [Secure your Azure administration access](docs/02-secure-azure-access.md).
3. **Verify the service address and trusted HTTPS.** Use the address confirmed by your deployment owner. Check that the intended client can reach it without a certificate warning. If not, complete [Configure your domain and trusted HTTPS](docs/04-configure-domain-and-tls.md) before entering credentials.
4. **Replace temporary administrator access.** Obtain initial credentials only through the mechanism confirmed for your image. Establish and test a permanent administrator in a separate session before removing temporary access and retiring its credential material. See [Complete your initial Keycloak access](docs/03-complete-initial-access.md).
5. **Test one application sign-in.** With the application owner, configure a test realm, user and client appropriate to the application. Start sign-in from that application, verify the resulting session, and check that an unauthorized user is denied the intended access. See [Configure Keycloak for your organization](docs/05-configure-keycloak.md).

**Stop at an unverified image-specific procedure.** Do not guess a console URL, credential location, command or configuration value. Ask for the missing instructions through [support](SUPPORT.md) before continuing. Never bypass a certificate warning or remove your only working administrator.

## Check your result

- [ ] Azure resource state and application readiness have been checked separately.
- [ ] Authorized operators have a verified, restricted management connection.
- [ ] The agreed service address uses HTTPS trusted by the intended client.
- [ ] Permanent administration works and temporary access no longer works.
- [ ] The test application accepts the intended user and rejects unauthorized access.

This result demonstrates an initial test, **not production readiness**. Deploying the VM does not automatically integrate your applications.

## Before you connect real users

Complete [Operate, protect and recover your deployment](docs/06-operate-and-recover.md): arrange and test recovery, assign maintenance and monitoring owners, and review availability and costs.

If a check fails, use [Troubleshoot and request help](docs/07-troubleshoot-and-get-support.md). Share only redacted error details, never credentials, tokens or private keys.

## Primary references

- Microsoft: [VM states and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) and [least-privilege Azure access](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices).
- Keycloak: [hostname configuration](https://www.keycloak.org/server/hostname), [temporary administrator removal](https://www.keycloak.org/server/bootstrap-admin-recovery) and [application integration](https://www.keycloak.org/securing-apps/overview).

These references explain general platform or upstream behavior. They do not prove which features are configured in the image.
