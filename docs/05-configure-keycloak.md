# Configure Keycloak for your organization

[Documentation home](../README.md)

> **Pre-release draft.** This is an organization-configuration checklist based on upstream Keycloak guidance, not a tested integration for this offer. Console labels, supported integrations and the target release are ⚠️ to be validated.

## Before you start

Have a verified [permanent administrator](03-complete-initial-access.md), [trusted service address](04-configure-domain-and-tls.md), an application owner and a test environment or approved test realm. Do not test new authentication settings on the only working administration path.

## Choose your configuration

The [Keycloak administration guide](https://www.keycloak.org/docs/latest/server_admin/index.html) describes realms, users, roles, clients, identity brokering and federation. These are upstream capabilities, not a statement that your VM has configured any of them.

| Decision | Agree with the responsible owner |
|---|---|
| Realm | Which users, applications and policies belong together, and who administers them. |
| User source | Whether accounts are managed locally or depend on a separately configured directory or identity provider. |
| Application | Which protocol and client type the application supports, its approved redirect locations and any credentials it needs. |
| Access policy | Which users can access the application, which roles it consumes and what authentication protection is required. |
| Account assistance | Who handles onboarding, lost access and authentication problems. |

Do not announce self-registration, password recovery or email-based flows to users until the required configuration and dependencies have been tested.

## Validate one application before expanding

1. Agree on a test realm and user with no access to production data.
2. Have the Keycloak administrator and application owner configure the integration using the documentation for their actual software releases. Keycloak's [application integration overview](https://www.keycloak.org/securing-apps/overview) explains the role of standards-compatible application libraries.
3. Restrict redirect locations and permissions to the intended application needs. Protect any client credentials through your approved secret-management process.
4. Start sign-in from the test application. Verify the intended service address, successful authentication and the returned application session.
5. Test an unauthorized user as well as an authorized user. Agree on expected sign-out and session behavior and test it.
6. Record the configuration decisions, test results and support owner before planning production access.

**Expected result:** the application owner and Keycloak operator can demonstrate the intended access behavior. Seeing the Keycloak administration console alone does not demonstrate application integration.

**⚠️ To be validated on the target image:** the exact realm/client procedure, supported release-specific settings and complete integration test. Applications, directories and identity providers are separate systems; no bundled integration is promised here.

## If a check fails

Verify the intended realm, application registration, service address, redirect settings and permissions together with the application owner. Share only redacted error details; tokens and session cookies must not appear in public reports. See [troubleshooting](07-troubleshoot-and-get-support.md).

**Next:** [Operate, protect and recover your deployment](06-operate-and-recover.md).
