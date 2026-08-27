# Reading Guide: Module 12 - Azure Governance and Compliance

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure management and governance (30-35% of exam)

---

## Overview

Cloud governance is how organizations maintain consistent, compliant, and secure cloud environments at scale. Without governance, cloud environments drift — resources appear in wrong regions, required tags are missing, encryption is disabled, and compliance violations accumulate silently. This module covers the Azure tools that prevent drift through policy enforcement, hierarchical organization, data governance, and compliance management.

---

## Section 1: Azure Policy

### What Azure Policy Does

Azure Policy is a governance service that evaluates Azure resource configurations against defined rules and enforces compliance at scale. Policy is distinct from RBAC: RBAC controls who can perform actions; Policy controls what configurations are permitted regardless of who is making the request.

Even a user with the Owner role cannot bypass Azure Policy — if a policy denies creating resources outside East US, even the subscription Owner cannot create a resource in Brazil South.

### Policy Definitions

A policy definition specifies:

1. A condition to evaluate (for example: "is the storage account's HTTPS-only setting disabled?")
2. An effect to apply if the condition is met (for example: Deny the creation)

Policy definitions can be:

- **Built-in:** Hundreds of pre-built definitions provided by Microsoft covering common security, compliance, and operational standards
- **Custom:** Organization-specific definitions created for unique requirements

### Policy Effects

| Effect | Behavior | Use When |
|---|---|---|
| Deny | Block the non-compliant resource creation or update | Configuration absolutely must not exist |
| Audit | Allow the action, flag resource as non-compliant | You want visibility without blocking (initial rollout) |
| AuditIfNotExists | Audit when a related resource is missing | Detect VMs without monitoring extension |
| DeployIfNotExists | Auto-deploy a required resource if missing | Automatically add required extensions, configurations |
| Modify | Add, update, or remove resource properties | Auto-add required tags at resource creation |
| Append | Add additional fields to a resource during creation | Force additional settings that cannot be removed |
| Disabled | Policy definition exists but is not enforced | Testing or temporarily suspending a policy |

### Policy Initiatives (Policy Set Definitions)

An initiative groups multiple related policy definitions into a single assignable unit. Instead of assigning 40 individual security policies one by one, you group them into an initiative and assign it once.

Built-in compliance initiatives:

| Initiative | Standard Addressed |
|---|---|
| Azure Security Benchmark | Microsoft's baseline security best practices |
| NIST SP 800-53 Rev 5 | US federal government security standard |
| CIS Microsoft Azure Foundations Benchmark | Center for Internet Security recommendations |
| HIPAA/HITRUST 9.2 | Healthcare compliance (US) |
| PCI DSS | Payment card industry security standard |
| FedRAMP High | US federal cloud compliance |

### Policy Assignments

An assignment connects a policy definition or initiative to a scope. Assignment scope options:

- Management Group
- Subscription
- Resource Group

An assignment at a higher scope is inherited by all child scopes. A policy assigned at the Root Management Group applies to every subscription, every resource group, and every resource in the entire tenant.

**Exclusions:** You can exclude specific subscriptions, resource groups, or resources from a policy assignment when a legitimate exception exists.

### Policy Compliance View

After assignment, Azure Policy evaluates all existing resources against the policy. New resources are evaluated at creation time. The compliance dashboard shows:

- Overall compliance percentage for each policy or initiative
- Per-resource compliance state (Compliant / Non-compliant / Exempt)
- Resources that triggered Audit findings
- Remediation tasks for DeployIfNotExists and Modify policies

### Azure Policy vs. Azure RBAC

| Dimension | Azure Policy | Azure RBAC |
|---|---|---|
| Answers the question | "Is this configuration allowed?" | "Is this user allowed to do this?" |
| Default stance | All configurations allowed unless a Deny policy exists | All actions denied unless a role assignment allows them |
| Enforcement point | Azure Resource Manager evaluates policy on every create/update | Azure Resource Manager checks RBAC before allowing the action |
| Can override who | No — RBAC and Policy are additive controls | No — Policy still applies after RBAC check passes |
| Example | "VMs must use approved sizes" | "This user can create VMs" |

Both controls must pass for an operation to succeed: the user must be authorized (RBAC) AND the resulting resource must comply with policy (Azure Policy).

---

## Section 2: Management Groups

### Purpose

Management Groups organize Azure subscriptions into a hierarchical container structure. They exist specifically to enable governance (policy and RBAC) at a scope above a single subscription.

### Hierarchy Structure

```text
Tenant Root Group (mandatory, one per tenant)
  ├── Management Group: Production
  │     ├── Subscription: Prod-Finance
  │     ├── Subscription: Prod-HR
  │     └── Subscription: Prod-Operations
  ├── Management Group: Development
  │     ├── Subscription: Dev-Engineering
  │     └── Subscription: Dev-QA
  └── Management Group: IT-SharedServices
        └── Subscription: SharedServices
```

### Key Properties

| Property | Value |
|---|---|
| Tenant Root Group | One per tenant, automatically created, cannot be deleted |
| Maximum depth | 6 levels of management groups below the Tenant Root |
| Maximum groups | 10,000 management groups per directory |
| Subscription membership | Each subscription belongs to exactly one management group |
| Inheritance | Policy and RBAC at a management group cascade to all child management groups, subscriptions, resource groups, and resources |
| Supported by | All Azure subscriptions (regardless of offer type) |

### Why Management Groups Matter for Governance

Without management groups, an organization with 50 subscriptions must:

- Assign every security policy 50 times (once per subscription)
- Remember to configure new subscriptions when they are created
- Manually verify consistent policy application across all subscriptions

With management groups, the organization:

- Assigns the policy once at the management group
- All current and future subscriptions under that group automatically comply
- Compliance reporting is available at the management group level

### Management Groups and Azure Policy

Policy assignments at the Root Management Group apply to the entire tenant. This is the recommended location for enterprise-wide governance policies like "All resources must be in approved regions" or "All resources must have required tags."

Policy assignments at child management groups apply only to subscriptions within that group. This allows Production to have stricter policies than Development.

---

## Section 3: Azure Blueprints

### Blueprints Purpose

Azure Blueprints was a service for packaging the components of a governed Azure environment — ARM templates, Azure Policy assignments, RBAC role assignments, and resource group definitions — into a single deployable artifact.

When a blueprint was deployed (assigned), all components deployed together and remained tracked as a linked set. Blueprint assignments could be protected from modification or deletion.

### Use Case

An enterprise needs to provision 10 new subscriptions for new business units. Each subscription must:

1. Have three standard resource groups (Production, Development, Shared)
2. Have specific RBAC role assignments (DevOps = Contributor, Security = Reader)
3. Have the company's security policies applied
4. Have a standard set of baseline Azure resources (Log Analytics workspace, key vault)

A blueprint could automate all of this in a single deployment.

### Current Status

Microsoft announced the retirement of Azure Blueprints in 2023. The recommended replacement is to use Azure Policy, Azure RBAC, ARM templates (or Bicep), and Management Groups together to accomplish the same goals.

For AZ-900: Know what Blueprints was designed to do and that it is being deprecated. Exam questions about Blueprints may still appear.

---

## Section 4: Microsoft Purview

### Purview Purpose

Microsoft Purview is a unified data governance, risk management, and compliance solution. While Azure Policy governs Azure resource configurations, Purview governs the data itself — where sensitive data lives, how it's classified, who has access to it, and how it flows.

Purview is relevant for organizations subject to data privacy regulations: GDPR, HIPAA, CCPA, Australia's Privacy Act, and similar frameworks.

### Core Capabilities

| Capability | Description |
|---|---|
| Data Map | Discovers and registers data assets from Azure, on-premises, and other clouds; builds a map of all data sources |
| Data Catalog | Searchable inventory of all data assets; business users can find data owners, understand content, request access |
| Data Classification | Automatically identifies sensitive data patterns: credit card numbers, SSNs, health records, financial data |
| Sensitivity Labels | Labels (Public, Internal, Confidential, Highly Confidential) applied to data assets and documents |
| Data Lineage | Traces how data moves from source through transformations to destination (critical for ETL pipeline governance) |
| Policy Management | Data access policies based on sensitivity labels and classification |

### Data Sources Purview Can Scan

- Azure Storage accounts, Azure Data Lake Storage, Azure SQL Database, Azure Synapse, Azure Cosmos DB
- On-premises SQL Server, Oracle, SAP, Teradata
- Amazon S3, multi-cloud sources
- Power BI workspaces
- SharePoint and Microsoft 365 (with compliance integration)

### Purview vs. Azure Policy — What Each Governs

| Service | Governs | Examples |
|---|---|---|
| Azure Policy | Azure resource configurations | Region restrictions, encryption settings, tag requirements |
| Microsoft Purview | Data content and classification | PII identification, data residency compliance, lineage tracking |

These are complementary: Policy ensures resources are configured correctly; Purview ensures data inside those resources is properly identified and protected.

---

## Section 5: Compliance in Azure

### Microsoft's Compliance Commitments

Microsoft maintains compliance certifications for Azure infrastructure. When you build on Azure, the underlying physical infrastructure already meets many compliance standards. Azure has the broadest compliance portfolio of any cloud provider, covering:

- ISO 27001, ISO 27017, ISO 27018
- SOC 1, SOC 2, SOC 3
- PCI DSS Level 1
- HIPAA Business Associate Agreement
- FedRAMP High (US government)
- GDPR data processing agreements
- Country-specific: Australia IRAP, Germany C5, UK Cyber Essentials

### Shared Responsibility for Compliance

Meeting a compliance standard in Azure is a shared responsibility:

- Microsoft is responsible for: physical security, network infrastructure, hypervisor, the compliance of Azure services themselves
- Customer is responsible for: data classification, access control, application security, audit logging, data retention policies

The Defender for Cloud Regulatory Compliance dashboard distinguishes between Microsoft-managed controls (infrastructure you cannot configure) and customer-managed controls (configurations you must set correctly).

### Compliance Manager

Microsoft Purview Compliance Manager is a tool (within the Microsoft Purview compliance portal, separate from the data governance Purview) that helps organizations manage their compliance obligations. It provides:

- Pre-built assessments for common standards (GDPR, HIPAA, ISO 27001)
- Improvement actions mapped to specific controls
- Compliance score
- Evidence collection and documentation

---

## Section 6: Governance Service Selection Summary

| Scenario | Correct Service |
|---|---|
| Prevent VMs from being created outside approved regions | Azure Policy (Deny effect) |
| Apply security policies to all 40 subscriptions simultaneously | Azure Policy assigned at Management Group |
| Require all resources to have a CostCenter tag | Azure Policy (Deny or Modify effect) |
| Organize production and development subscriptions under separate governance | Management Groups |
| Discover what customer data exists in Azure Storage accounts | Microsoft Purview |
| Identify GDPR-relevant personal data in Azure SQL databases | Microsoft Purview (Data Classification) |
| View compliance against PCI DSS across all Azure resources | Defender for Cloud Regulatory Compliance |
| Package policies, roles, and ARM templates for new subscription provisioning | Azure Blueprints (deprecated) |
| Prevent any user (including Owners) from creating resources in China East | Azure Policy (Deny effect — overrides RBAC) |

---

## Section 7: Azure CLI — Policy Commands

```bash
# List all available policy definitions (built-in)
az policy definition list \
  --query "[?policyType=='BuiltIn'].{name:displayName, id:name}" \
  --output table

# Show a specific policy definition
az policy definition show \
  --name "e56962a6-4747-49cd-b67b-bf8b01975c4f"

# Assign a policy to a resource group
az policy assignment create \
  --name "allowed-locations" \
  --display-name "Allowed Locations" \
  --policy "e56962a6-4747-49cd-b67b-bf8b01975c4f" \
  --resource-group "my-rg" \
  --params '{"listOfAllowedLocations": {"value": ["eastus", "westus2"]}}'

# List policy assignments
az policy assignment list \
  --resource-group "my-rg" \
  --output table

# Delete a policy assignment
az policy assignment delete \
  --name "allowed-locations" \
  --resource-group "my-rg"

# List management groups
az account management-group list \
  --output table
```

---

## Section 8: AZ-900 Exam Tips

1. **Policy Deny overrides Owner:** Azure Policy Deny blocks an operation regardless of the user's RBAC role. Even an Owner cannot create a non-compliant resource when a Deny policy is in effect. This is a common trick question.

2. **Management groups are for governance at scale:** When a scenario mentions "apply policy to all subscriptions simultaneously" or "one rule for the entire organization," the answer involves management groups.

3. **Policy vs. RBAC — memorize the distinction:** Policy controls configurations; RBAC controls user actions. Both must pass for an operation to succeed. They are complementary, not alternatives.

4. **Initiatives group policies:** An initiative (policy set) groups related policies for single-assignment governance. Know that Azure Security Benchmark and HIPAA are examples of built-in initiatives.

5. **Purview is for data governance:** When the scenario involves discovering sensitive data, classifying PII, tracking data lineage, or preparing for GDPR/HIPAA data privacy audits, Purview is the answer. It is not about resource configurations.

6. **Azure Blueprints is deprecated:** Know what it did (packaged governance components for environment provisioning) and that it is being replaced by individual component services. Exam questions may still reference it.

7. **Compliance is shared responsibility:** Microsoft secures the platform; customers secure their data and configurations. This distinction matters for the Defender for Cloud regulatory compliance dashboard (Microsoft-managed vs. customer-managed controls).

8. **Policy compliance is not instant:** After assigning a new policy, existing non-compliant resources appear in the compliance dashboard but are not automatically remediated unless the policy uses DeployIfNotExists or Modify effects with a remediation task.

---

Module 12 Reading Guide | CIS-4331 Azure Cloud | Texas Wesleyan University

---

## 9. Supplemental Resources

1. Azure Policy documentation — overview of policy definitions, initiatives, assignments, and compliance evaluation: https://learn.microsoft.com/en-us/azure/governance/policy/overview

2. Management Groups documentation — organizing subscriptions into a hierarchy for unified governance and policy inheritance: https://learn.microsoft.com/en-us/azure/governance/management-groups/overview

3. Microsoft Purview data governance documentation — scanning, classifying, and cataloging data assets across hybrid and multi-cloud environments: https://learn.microsoft.com/en-us/purview/purview
