---
title: Configure your domain and trusted HTTPS
---
# Configure your domain and trusted HTTPS

English · [Français](04-configure-domain-and-tls-fr.md)

[Documentation home](../README.md)

## Before you start

Have control of the intended DNS name, an authorized network operator, an approved certificate process and a maintenance window if the service is already in use. Preserve existing configuration and recovery access before changing an active deployment.

## Prepare the service address

1. Agree on the address applications and administrators will use. Determine which clients must resolve and reach it.
2. Have the DNS and network owners confirm that the records resolve to the intended service from those client networks. Do not assume a public IP address or public DNS is required for every deployment.
3. Select a certificate trusted by those clients and covering the chosen hostname. Confirm the issuer's validation and renewal requirements before changing network access.
4. Review the [Keycloak hostname guidance](https://www.keycloak.org/server/hostname). Keycloak's advertised service address must match the intended deployment.
5. Have the operator apply only a hostname and certificate procedure verified for the target image. Do not combine examples for direct Keycloak TLS with a TLS-terminating reverse proxy without checking the actual architecture. See Keycloak's [reverse-proxy guidance](https://www.keycloak.org/server/reverseproxy).

**⚠️ To be validated on the target image:** the hostname tool and syntax, certificate installation, affected services, restart behavior, any required network openings and the renewal procedure. Until these are established, this guide does not provide an executable configuration procedure.

## Verify the result

After an approved configuration change:

1. Open the agreed HTTPS address from an intended client network.
2. Verify that the client trusts the certificate without an exception and that the hostname is correct.
3. Verify that Keycloak-generated URLs use the intended service address. Application redirects are checked later during application integration; an external application is not required for this HTTPS milestone.
4. Assign an owner to renewal and test the renewal process in an appropriate test environment. Record how expiry and renewal failures will be detected.

**Expected result:** the agreed hostname is reachable over trusted HTTPS and the certificate lifecycle has an owner. Reaching a page while ignoring certificate errors is not a successful TLS check.

## If a check fails

Separate DNS resolution, network reachability, certificate trust/name errors and incorrect generated URLs. Do not disable hostname checks, expose internal service interfaces or bypass trust verification as a permanent fix. Use [troubleshooting](07-troubleshoot-and-get-support.md).

**Next:** with trusted HTTPS verified, complete [initial administrator setup](03-complete-initial-access.md). If permanent administration is already verified, skip that completed task and continue to [configure Keycloak](05-configure-keycloak.md) when an application owner is ready.
