# Operate, protect and recover your deployment

[Documentation home](../README.md)

> **Pre-release draft.** Backup, restoration, update and recovery procedures for the target image are ⚠️ to be validated. This page provides an operations checklist, not executable recovery commands. No Azure service mentioned here is claimed to be enabled or bundled with the offer.

## Before you start

Identify the service owner, Azure operator, Keycloak administrator and application owners. Agree on an acceptable recovery time, acceptable data loss and a maintenance window. Microsoft's [VM architecture guidance](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/virtual-machines) covers reliability and dependencies; it does not make a single VM highly available.

## Establish and test your backup plan

1. Inventory identity data, application configuration, customizations, certificates and other material required to rebuild the service. Store protected recovery material separately from ordinary support diagnostics.
2. Choose a backup approach with the database and Azure operators. Review both [PostgreSQL backup guidance](https://www.postgresql.org/docs/current/backup.html) and [Azure VM backup behavior](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction).
3. Verify what the chosen backup actually protects. A VM recovery point must not be assumed to provide application-consistent database recovery merely because its job succeeded. Microsoft distinguishes consistency levels and explains that Linux application consistency needs additional coordination.
4. Define the schedule, retention, storage access, protection against accidental deletion and ownership of failure alerts. Confirm compatibility and cost before enabling a service.
5. Restore into an isolated environment using the procedure validated for your image. Prevent test email, directory synchronization and other unintended contact with production systems.
6. Verify administrative access, expected data and an application sign-in flow. Record the observed recovery time and data recovered.

**Expected result:** you have evidence of a usable recovery, not just a successful backup job.

**⚠️ To be validated:** database consistency, backup commands, recovery ordering, restored credentials and configuration, and the safe use of any restored disks. Do not attach live data to a new initialization flow or overwrite production data using this checklist.

## Plan maintenance and updates

1. Inventory the actual installed software and configuration using a verified read-only procedure.
2. Review supported updates and release guidance with the responsible operators. [Azure Update Manager](https://learn.microsoft.com/en-us/azure/update-manager/overview) concerns machine updates; do not assume it upgrades the separately packaged Keycloak application.
3. For Keycloak changes, assess the [official upgrading guide](https://www.keycloak.org/docs/latest/upgrading/index.html) for the installed and intended releases. Do not choose an upgrade target solely because it is described as the latest.
4. Test the change and recovery plan on an isolated copy before scheduling production maintenance. Do not assume that an application downgrade reverses database changes.
5. After approved maintenance, verify service readiness and the application sign-in flow, then record the outcome.

**⚠️ To be validated:** supported OS and application update paths, image replacement strategy, exact commands, expected downtime and recovery method.

## Monitor the service and its dependencies

1. Review available host metrics in Azure Monitor. Microsoft's [VM monitoring guide](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/monitor-vm) distinguishes host metrics from guest data that requires configuration.
2. Decide which guest and application signals you need. Confirm agent and OS compatibility, data collection, access, retention and charges before enabling collection.
3. Assign alerts for application availability, resource pressure, certificate expiry and backup failures according to your requirements.
4. Test that an alert reaches the on-call owner. Include a safe application sign-in check; host metrics alone do not prove authentication works.

**Expected result:** a named operator receives actionable alerts and knows the response procedure. Image-specific health checks and collection settings remain ⚠️ to be validated.

## Review availability and costs

- Document the effect of VM, database, network, DNS and certificate failures. Do not assume redundancy, automated recovery or a workload SLA.
- Review all resources and services your deployment consumes, along with the actual Marketplace commercial terms. No software price is established here.
- Use [Cost Management budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) for notifications where available. Budget alerts do not by themselves stop consumption.
- Review [VM states and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing) before stopping test resources. A stopped allocated VM and a deallocated VM are different; other resources can continue to incur charges.

Do not delete the VM, disks or recovery points until their owners have confirmed data-protection and retention requirements.

**Next:** use [Troubleshoot and request help](07-troubleshoot-and-get-support.md) whenever an operational check fails.
