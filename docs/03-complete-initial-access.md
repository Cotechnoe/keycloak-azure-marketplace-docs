---
title: Complete your initial Keycloak access
---
# Complete your initial Keycloak access

English · [Français](03-complete-initial-access-fr.md)

[Documentation home](../README.md)

## Before you start

- Have [approved administration access](02-secure-azure-access.md).
- Verify the administration address through a trusted deployment record.
- Have trusted HTTPS for that address. If it is not configured, first complete [domain and TLS preparation](04-configure-domain-and-tls.md). Do not enter credentials after bypassing a certificate warning.
- Have an approved place to store credentials and an account-recovery plan.

## Retrieve the initial credentials and sign in

Credential retrieval over SSH and browser sign-in were verified on 2026-11-10 on a VM deployed from image `26.8.20261108`, running Keycloak `26.8.2`. Other image versions require separate verification.

1. In your own terminal, replace the example values below with your SSH private-key path, the Linux administrator username selected during deployment and the VM address:

   ```sh
   ssh -i /path/to/private-key linux-admin@vm-address \
     'sudo cat /root/keycloak-initial-admin.txt'
   ```

   The command displays sensitive credentials. Run it only in a private terminal; do not copy the output into a chat, screenshot, log or support request. If the file is missing, stop and follow the access-failure guidance below.
2. Read `KC_ADMIN_USERNAME` and `KC_ADMIN_PASSWORD` from the output. These are the Keycloak credentials, not your Linux SSH account or Azure account. Copy only each value, without the `KEY=` prefix.
3. Open `https://<verified-hostname>/admin/`, using the administration hostname configured for your VM. An IP address was used for the isolated validation; that does not establish trusted HTTPS for your deployment. Complete the domain and TLS prerequisites above before entering credentials.
4. Enter the `KC_ADMIN_USERNAME` value in **Username or email**, the `KC_ADMIN_PASSWORD` value in **Password**, then select **Sign In**.

The initial account is temporary. A successful sign-in does not complete the permanent-administration setup.

## Establish permanent administration

The following describes the intended sequence. Exact role assignments and UI steps for creating and retiring administrators still require validation on your image.

1. Retrieve the initial credentials using the procedure above and keep the values private.
2. Sign in only at the verified administration address.
3. Establish a permanent administrator with the privileges required for the intended duties. Follow the [Keycloak administration guide](https://www.keycloak.org/docs/latest/server_admin/index.html) applicable to the installed release. Do not assume that Azure permissions assign Keycloak permissions.
4. Verify the permanent administrator in a separate session before retiring temporary access. Check the required administrative tasks, not merely whether login succeeds. Set up and test your organization's required authentication protection and recovery method.
5. Remove the temporary account using the verified account-management procedure. Keycloak documents that [bootstrap administrator accounts are temporary and require manual removal](https://www.keycloak.org/server/bootstrap-admin-recovery).
6. Confirm the temporary account can no longer be used. Then remove or retire the initial credential material according to the image-specific procedure and your organization's policy. Deleting a credential file alone does not establish that the account has been removed.

**Expected result:** a verified permanent administrator can perform the intended tasks, temporary access no longer works, and initial credential material is handled securely.

**⚠️ To be validated on the target image:** precise role assignments and UI steps for permanent administration, removal of temporary access and credential cleanup. These operations were not covered by the initial sign-in validation above.

## If access fails

Stop if the address or certificate is unexpected, the initial credentials are unavailable, or permanent permissions cannot be verified. Do not delete the only working administrator. Do not rerun initialization or attempt an account-recovery command on the live database based on an example from another release.

Use [support](../SUPPORT.md) for image-specific guidance. Keycloak's [recovery reference](https://www.keycloak.org/server/bootstrap-admin-recovery) includes prerequisites that must be assessed for your deployment before any recovery action.

**Next:** the permanent-administration milestone is complete only when the checks above succeed. You may stop this setup session here without an external application. When an application owner is ready, continue to [Configure Keycloak for your organization](05-configure-keycloak.md). Before real users, complete [Operate, protect and recover your deployment](06-operate-and-recover.md); administrative access alone is not production readiness.
