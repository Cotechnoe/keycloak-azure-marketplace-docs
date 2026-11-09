# Secure your Azure administration access

[Documentation home](../README.md)

> **Pre-release draft.** The image's supported connection method, account details and effective network requirements are ⚠️ to be validated. This guide recommends access-control practices; it does not prescribe an unverified port or Azure role for the offer.

## Before you start

Identify your VM using [Verify your deployment](01-verify-deployment.md). Arrange help from an authorized Azure administrator if you cannot review access or networking. Have a recovery route before modifying an existing connection.

## Review who can administer the deployment

1. In the Azure portal, review role assignments affecting the VM and its related resources with your Azure administrator.
2. Grant operators only the actions and scope their duties require. Do not grant subscription-wide ownership simply to solve a connection problem. Microsoft's [Azure RBAC guidance](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices) explains least-privilege assignments.
3. Identify separately the people allowed to sign in to the guest operating system and those allowed to administer Keycloak. Azure resource permissions are not a substitute for checking either access path.
4. Record the authorized operators and the person responsible for removing access when duties change.

**Expected result:** you can explain who manages Azure resources, who can enter the VM, and who will administer Keycloak.

## Review your management connection

1. Review the existing management route and its source network with your network administrator.
2. Compare Microsoft's [secure VM administration options](https://learn.microsoft.com/en-us/azure/networking/design-guide/developer-admin-access), such as Azure Bastion or a VPN, with your network requirements. These are options to evaluate, not features claimed to be included or enabled in the offer.
3. Review the network security groups affecting the VM. For each required rule, document the purpose, permitted source and destination, protocol and port. Use the actual deployment requirements, not guessed defaults. Microsoft's [NSG reference](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) explains how rules are evaluated.
4. Have the authorized administrator apply any approved changes while preserving a recovery route. Do not expose management access to all sources to troubleshoot.
5. Verify an authorized connection before closing the original session. Verify restrictions using a controlled test that does not risk locking out the only operator.

**Expected result:** approved operators can connect, and the intended access restrictions are verified. No claim is made that choosing a particular Azure service automatically configures access to this image.

**⚠️ To be validated on the target image:** guest login method, account privileges, network requirements and the safe connection verification procedure.

## If access fails

Distinguish Azure permission denial, network timeout and guest authentication failure. Preserve the error type without passwords or private keys. Ask the Azure administrator to inspect effective access and network rules rather than disabling controls. See [troubleshooting](07-troubleshoot-and-get-support.md).

**Next:** [Complete your initial Keycloak access](03-complete-initial-access.md).
