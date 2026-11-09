---
title: Verify your deployment
---
# Verify your deployment

English · [Français](01-verify-deployment-fr.md)

[Documentation home](../README.md)

> **Pre-release draft.** No target image has been selected for these guides. Application-readiness commands and image-specific completion indicators are ⚠️ to be validated. This page does not certify your VM as ready.

## Before you start

Have the Azure subscription and resource group used for your deployment, permission to read the resources, and access to your organization's deployment record. If somebody else deployed the VM, ask them to identify it rather than selecting a resource by a similar name.

## Inspect the Azure deployment

Portal labels below follow Microsoft's English documentation; localized labels can differ. These are inspection steps, not instructions to create, restart or delete resources.

1. In the Azure portal, search for **Virtual machines**, select the intended VM and check the subscription and resource group on its **Overview** page. If you have just completed deployment, **Go to resource** opens the resource. These entry points are described in Microsoft's [portal quickstart](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal); do not follow its resource-creation or deletion steps for an existing deployment.
2. Open the resource group, select the link under **Deployments**, then select the deployment corresponding to your VM. Record its reported status, deployment time and correlation ID in a protected operations record. Microsoft documents this path in [deployment history](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history). Review the error details if it failed; do not assume the newest deployment is yours.
3. Record the VM's reported power state separately from deployment status. Use Microsoft's [VM states guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing): `Running` describes power state; provisioning `Succeeded` means the last VM resource operation succeeded. Neither proves Keycloak is ready. If a state is not visible with your permissions, record it as unknown and ask the Azure administrator; do not infer success.
4. If provisioning failed, preserve the error code and operation details, remove sensitive values before sharing them, and use [troubleshooting](07-troubleshoot-and-get-support.md). Do not delete the VM or its disks as a first diagnostic step.
5. Identify the attached storage and network resources. Ask your deployment owner to explain unexpected resources or missing data storage before adding organization data.

**Expected result:** your protected record identifies the VM, subscription, resource group, deployment status/time/correlation ID, separately observed VM power state, and any error. Record the image reference from the deployment owner's verified record when available; otherwise mark it unknown. A successful provisioning operation or a running VM is **not** a Keycloak sign-in test.

## Check application readiness separately

If you do not yet have approved VM access, pause here and complete [Secure your Azure administration access](02-secure-azure-access.md). That guide explicitly returns you to this check. Do not mark the application ready while arranging access.

With approved VM access, check application initialization and service health using the procedure validated for the exact image.

**⚠️ To be validated on the target image:** the initialization service, health-check address, diagnostic commands, success indicators and expected initialization duration. No file path, port or waiting-time guarantee is supplied here.

Record application readiness separately from the Azure state. If the image-specific check is unavailable, the application-readiness result is **not verified**. Do not proceed to connect real users on that basis.

This distinction follows Microsoft's [VM reliability guidance](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/virtual-machines): the workload depends on more than the VM resource alone.

## If a check fails

- **Cannot locate the VM:** verify the subscription, resource group and your read permissions with the deployment owner.
- **Provisioning failed:** retain the error and contact the appropriate Azure or image support channel.
- **VM running but application unavailable:** keep the Azure state as evidence; do not treat it as proof that application initialization succeeded.

See [Troubleshoot and request help](07-troubleshoot-and-get-support.md) for what to include without exposing secrets.

**Next:** only after approved VM access and a successful application-readiness check, continue to [Configure your domain and trusted HTTPS](04-configure-domain-and-tls.md). If either is missing or unverified, stop and request clarification rather than proceeding to credentials.
