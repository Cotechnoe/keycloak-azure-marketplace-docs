---
title: Troubleshoot and request help
---
# Troubleshoot and request help

English · [Français](07-troubleshoot-and-get-support-fr.md)

[Documentation home](../README.md)

> **Pre-release draft.** Image-specific diagnostic commands, log paths and recovery actions are ⚠️ to be validated. This guide provides non-destructive triage and escalation, not a tested repair procedure.

## Before you start

Confirm the affected VM with its owner. Record when the problem began and the most recent change. If production is affected, follow your incident process and preserve relevant evidence before attempting a repair.

## Identify the failing layer

| Observation | First check | Involve |
|---|---|---|
| Deployment reports an Azure error | Correct subscription, resource and operation error; see [deployment checks](01-verify-deployment.md). | Azure administrator; Microsoft for Azure platform issues, or Cotechnoe for an apparent image problem. |
| Management connection fails | Whether the failure is an Azure authorization error, network timeout or guest login error; see [access checks](02-secure-azure-access.md). | Azure, network or VM administrator, depending on the failing layer. |
| Administration URL is unreachable or reports a certificate error | Intended DNS name, network reachability and certificate trust; see [domain and TLS](04-configure-domain-and-tls.md). | DNS/network/certificate owner and VM operator. |
| Initial administrator access is unavailable | The verified credential-delivery procedure for the exact image; see [initial access](03-complete-initial-access.md). | VM operator and Cotechnoe for image-specific clarification. |
| Console works but application sign-in fails | Realm, client registration, redirects and permissions; see [application configuration](05-configure-keycloak.md). | Keycloak administrator and application owner. |
| Backup, update or monitoring check fails | Selected tool's error and last change; see [operations](06-operate-and-recover.md). | The operator responsible for that tool and the workload. |

Microsoft's [shared responsibility guidance](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) helps distinguish platform and workload concerns. An Azure VM state alone does not establish which application component failed.

## Prepare a safe request

1. State the task you were performing, expected result and actual result.
2. Include the incident time and timezone, whether the VM is a fresh deployment, and the last relevant change.
3. Include the image reference only if verified from your deployment. If unknown, say it is unknown; do not guess a version from a name.
4. Provide only a short, redacted error excerpt. Review the excerpt before posting.
5. State which checks succeeded and failed, and whether users are affected.
6. Choose the [appropriate support channel](../SUPPORT.md) and read the [privacy notice](../PRIVACY.md).

Never include passwords, private keys, tokens, authorization headers, cookies, connection strings or credential files. Redact personal data and confidential resource names, hostnames, addresses and realm/client identifiers. Do not send complete diagnostic archives through public issues.

**Expected result:** the recipient can identify the failing task and next safe check without receiving secrets or unnecessary customer data.

## Avoid turning a diagnosis into data loss

Do not rerun initialization, reset the database, remove the only working administrator, disable network restrictions or delete a VM/disk as an exploratory fix. Recovery actions require an approved, tested procedure for the actual image and a suitable backup or isolated test target.

If this draft does not contain the needed image-specific check, report the gap. A missing procedure is not permission to improvise one on production data.
