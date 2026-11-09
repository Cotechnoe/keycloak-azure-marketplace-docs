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

1. In the Azure portal, locate the VM in the intended subscription and resource group.
2. Record the VM identity, deployment time and available image reference in a protected operations record. Record the image actually used, not a version guessed from a VM name.
3. Check the provisioning state and power state separately. Use Microsoft's [VM states guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) to interpret them.
4. If provisioning failed, preserve the error code and operation details, remove sensitive values before sharing them, and use [troubleshooting](07-troubleshoot-and-get-support.md). Do not delete the VM or its disks as a first diagnostic step.
5. Identify the attached storage and network resources. Ask your deployment owner to explain unexpected resources or missing data storage before adding organization data.

**Expected result:** you know which VM you deployed, its reported Azure state and where to find the deployment error if there is one. A successful provisioning operation or a running VM is **not** a Keycloak sign-in test.

## Check application readiness separately

Once you have [approved management access](02-secure-azure-access.md), check the application initialization and service health using the procedure validated for the exact image.

**⚠️ To be validated on the target image:** the initialization service, health-check address, diagnostic commands, success indicators and expected initialization duration. No file path, port or waiting-time guarantee is supplied here.

Record application readiness separately from the Azure state. If the image-specific check is unavailable, the application-readiness result is **not verified**. Do not proceed to connect real users on that basis.

This distinction follows Microsoft's [VM reliability guidance](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/virtual-machines): the workload depends on more than the VM resource alone.

## If a check fails

- **Cannot locate the VM:** verify the subscription, resource group and your read permissions with the deployment owner.
- **Provisioning failed:** retain the error and contact the appropriate Azure or image support channel.
- **VM running but application unavailable:** keep the Azure state as evidence; do not treat it as proof that application initialization succeeded.

See [Troubleshoot and request help](07-troubleshoot-and-get-support.md) for what to include without exposing secrets.

**Next:** [Secure your Azure administration access](02-secure-azure-access.md).
