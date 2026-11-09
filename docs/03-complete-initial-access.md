# Complete your initial Keycloak access

English | [Français](03-complete-initial-access-fr.md)

[Documentation home](../README.md)

> **Pre-release draft.** Credential retrieval, the initial console address and the exact permanent-administrator procedure for this image are ⚠️ to be validated. Do not guess credentials, copy commands from another image, or treat this page as a tested bootstrap procedure.

## Before you start

- Have [approved administration access](02-secure-azure-access.md).
- Verify the administration address through a trusted deployment record.
- Have trusted HTTPS for that address. If it is not configured, first complete [domain and TLS preparation](04-configure-domain-and-tls.md). Do not enter credentials after bypassing a certificate warning.
- Have an approved place to store credentials and an account-recovery plan.

## Establish permanent administration

The following describes the intended sequence, not image-specific execution instructions.

1. Obtain initial access using the delivery mechanism confirmed for your exact image. Keep the values private. Never include a credential file or its contents in a support request.
2. Sign in only at the verified administration address.
3. Establish a permanent administrator with the privileges required for the intended duties. Follow the [Keycloak administration guide](https://www.keycloak.org/docs/latest/server_admin/index.html) applicable to the installed release. Do not assume that Azure permissions assign Keycloak permissions.
4. Verify the permanent administrator in a separate session before retiring temporary access. Check the required administrative tasks, not merely whether login succeeds. Set up and test your organization's required authentication protection and recovery method.
5. Remove the temporary account using the verified account-management procedure. Keycloak documents that [bootstrap administrator accounts are temporary and require manual removal](https://www.keycloak.org/server/bootstrap-admin-recovery).
6. Confirm the temporary account can no longer be used. Then remove or retire the initial credential material according to the image-specific procedure and your organization's policy. Deleting a credential file alone does not establish that the account has been removed.

**Expected result:** a verified permanent administrator can perform the intended tasks, temporary access no longer works, and initial credential material is handled securely.

**⚠️ To be validated on the target image:** how initial credentials are delivered, the initial username and console address, precise role assignments and UI steps, removal of temporary access and credential cleanup. These details must be verified before executing this sequence against the offer.

## If access fails

Stop if the address or certificate is unexpected, the initial credentials are unavailable, or permanent permissions cannot be verified. Do not delete the only working administrator. Do not rerun initialization or attempt an account-recovery command on the live database based on an example from another release.

Use [support](../SUPPORT.md) for image-specific guidance. Keycloak's [recovery reference](https://www.keycloak.org/server/bootstrap-admin-recovery) includes prerequisites that must be assessed for your deployment before any recovery action.

**Next:** [Configure your domain and trusted HTTPS](04-configure-domain-and-tls.md), or verify its result if already completed.
