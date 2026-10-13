# Video Script: Module 12 - Azure Governance and Compliance

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure management and governance (30-35% of exam)
**Estimated Duration:** 20-24 minutes

---

## Learning Objectives

By the end of this video you will be able to:

- Explain what Azure Policy does and how policies, initiatives, and assignments work together
- Describe the purpose and structure of Management Groups in Azure governance
- Differentiate between Azure Policy (configuration enforcement) and Azure RBAC (access control)
- Explain the purpose of Microsoft Purview in data governance
- Describe what Azure Blueprints was and how it mapped to compliance standards
- Apply governance service selection to real organizational compliance scenarios

---

## Section 1: Introduction — Why Cloud Governance Matters (0:00-2:00)

[INSTRUCTOR ON CAMERA]

Imagine you are the cloud administrator for a company that has 500 employees using Azure. You have 30 subscriptions across multiple departments. Each department creates their own resources. Some of those resources are misconfigured — databases without encryption, storage accounts with public access, virtual machines in regions that violate your data residency policy.

You didn't know about any of these misconfigurations because there was no systematic enforcement. Resources were created freely, and each team made their own configuration decisions.

This is what cloud environments look like without governance. And governance problems lead to compliance violations, security incidents, and audit failures.

[SLIDE: "Governance vs. Access Control — Two Different Questions"]

Let me be clear about what governance means in Azure, because students often confuse governance with access control.

Azure RBAC answers the question: "Who is allowed to perform this action?" Can this user create a virtual machine? Can they delete a storage account?

Azure governance answers a different question: "Even if you're allowed to do it, does it comply with our policies?" You might be allowed to create a virtual machine — you have the Contributor role. But are you allowed to create it in China East? Are you allowed to create it without a required cost center tag? Does the VM need to use a specific VM size to control cost?

RBAC is about permission. Governance is about compliance.

Today we cover three governance tools: Azure Policy, Management Groups, and Microsoft Purview. We'll also briefly cover Azure Blueprints, which still appears on the AZ-900 exam.

---

## Section 2: Azure Policy (2:00-8:00)

[SLIDE: "What Is Azure Policy?"]

[INSTRUCTOR ON CAMERA]

Azure Policy is Azure's configuration governance service. It allows you to define rules about what Azure resources can be created, where they can be created, and how they must be configured.

Here's how to think about it: Azure Policy is a set of rules that Azure Resource Manager enforces on every resource creation, update, or read request. Before a resource can be created, Azure Policy evaluates whether the resource configuration complies with all applicable policies. If it doesn't comply, the policy effect determines what happens.

[SLIDE: "Policy Structure: Definition, Initiative, Assignment"]

Azure Policy has three core concepts.

First: A Policy Definition. This is a single rule. For example: "Virtual machines must use approved VM sizes." A policy definition specifies the condition to evaluate and the effect if the condition is or isn't met.

Second: An Initiative. An initiative — also called a Policy Set Definition — is a collection of related policy definitions grouped together. Instead of assigning 40 individual policies to enforce your security baseline, you group them into one initiative called "Enterprise Security Baseline" and assign the initiative once. All 40 policies are now enforced together. Initiatives make governance at scale manageable.

Third: An Assignment. An assignment connects a policy definition or initiative to a scope — a management group, subscription, or resource group. You can have the same policy definition assigned at multiple scopes.

[SLIDE: "Policy Effects"]

When a resource violates a policy, what happens? That depends on the policy effect. There are several effects, and AZ-900 expects you to know the most important ones.

Deny — The resource creation or update is blocked. The user gets an error message explaining which policy was violated. This is the strictest effect and is used when you need to absolutely prevent certain configurations.

Audit — The resource creation is allowed, but the violation is flagged as a non-compliance finding in the Defender for Cloud compliance dashboard and Azure Policy compliance view. Use Audit when you want visibility without blocking.

DeployIfNotExists — If a resource exists without a required configuration, Azure Policy automatically deploys a companion resource to remediate it. For example: "If a VM exists without endpoint protection, automatically deploy endpoint protection." The policy engine does the remediation automatically.

Append — Automatically adds fields to a resource at creation time without blocking. Used for adding required tags to resources.

Modify — Changes properties of an existing resource to bring it into compliance.

[SLIDE: "Common Policy Scenarios"]

Let me walk through four common policy scenarios.

"All resources must be created in East US or West US 2 only." Effect: Deny. If someone tries to create a resource in Brazil South, the deployment fails with a policy violation.

"All storage accounts must use HTTPS-only transfers." Effect: Deny. Any storage account created without HTTPS-only enabled is blocked.

"All Azure SQL Databases must have Transparent Data Encryption enabled." Effect: Audit initially, then DeployIfNotExists for automated remediation.

"All resources must have a CostCenter tag." Effect: Deny or Append, depending on whether you want to force the creator to add it or have the policy add it automatically.

[SHOW PORTAL: Azure Policy > Definitions — show built-in policy list, search for "allowed locations"]

In the Azure Policy blade, you can see hundreds of built-in policy definitions that Microsoft provides. You can also create custom definitions for organization-specific requirements. The Compliance view shows all resources across your environment and their current compliance state against each assigned policy.

[SLIDE: "Scope and Inheritance in Policy"]

Policy assignments work exactly like RBAC scope — a policy assigned at a higher scope is inherited by everything below it.

A policy assigned at a Management Group applies to all subscriptions in that group, all resource groups in those subscriptions, and all resources in those resource groups. This is the primary reason management groups exist — to apply governance uniformly across many subscriptions.

Important note: unlike RBAC, you cannot override a policy assigned at a higher scope by assigning a different policy at a lower scope. The higher-scope policy wins, and you can use exclusions to exempt specific resources if needed.

---

## Section 3: Management Groups (8:00-12:00)

[SLIDE: "What Are Management Groups?"]

[INSTRUCTOR ON CAMERA]

Management Groups are containers that organize subscriptions into a hierarchical structure for governance at enterprise scale.

Here's the problem they solve. An enterprise might have 50 Azure subscriptions — one per department, or one per application, or one per business unit. If you want to apply a security policy across all 50 subscriptions, you would have to assign that policy 50 times, once per subscription. And if you add a new subscription, you'd have to remember to assign it there too.

Management Groups eliminate this problem. Organize your 50 subscriptions into management groups. Apply the policy once at the management group level. It automatically applies to all subscriptions within it.

[SLIDE: "Management Group Hierarchy"]

Every Azure tenant has one Root Management Group at the top. All other management groups and subscriptions live under this root.

A typical enterprise hierarchy looks like this.

Root Management Group at the top. Under the root, you might have management groups for Production, Development, and Shared Services. Under Production, you might have individual subscriptions for each application or business unit. Under Development, you might have subscriptions for each team's dev/test environment.

You can nest management groups up to six levels deep below the root. The root itself counts as level one, so you can have up to six levels of child management groups.

[SLIDE: "Management Group Facts for AZ-900"]

Know these facts for the exam.

A single Azure Active Directory tenant has exactly one Root Management Group. You cannot delete the root. Subscriptions and management groups can only have one parent at a time. RBAC and Policy assigned at a management group scope are inherited by all subscriptions below. Management groups support up to six levels of depth. There can be up to 10,000 management groups in a single directory.

[SHOW PORTAL: Azure Portal > Management Groups — show hierarchy view]

In the portal, the Management Groups blade shows your hierarchy. You can move subscriptions between management groups, view policies applied at each level, and see the inheritance chain.

[SLIDE: "Subscriptions as Governance Boundaries"]

Subscriptions are the direct container that organizations use for billing and access control. But there are scenarios where subscriptions are used specifically for governance isolation. For example, an organization might use separate subscriptions for production and development workloads to prevent development activity from affecting production resources — not just for access control, but for policy isolation and billing clarity.

Azure Policy can have exceptions — you can exclude a specific subscription or resource group from a management group policy. This gives you flexibility when you need a subset of resources governed differently.

---

## Section 4: Azure Policy vs. Azure RBAC (12:00-14:00)

[SLIDE: "Policy vs. RBAC — The Clear Distinction"]

[INSTRUCTOR ON CAMERA]

This is one of the most commonly tested distinctions on AZ-900, and it's worth being very explicit.

Azure RBAC defines what you are allowed to do. If you have the Contributor role on a subscription, you are allowed to create resources. If you don't have the Contributor role, you can't create resources. RBAC is identity-based authorization.

Azure Policy defines what configurations are permitted. Even if RBAC says you're allowed to create a virtual machine, Azure Policy might say "you cannot create a virtual machine with a public IP address in the Production subscription." RBAC granted the permission; Policy enforces the configuration standard.

They work together, not instead of each other. A complete governance model uses both: RBAC to control who can do things, and Policy to control what configurations those actions are allowed to produce.

Here's a test-friendly way to remember the distinction. RBAC controls the actor. Policy controls the outcome.

[SLIDE: "RBAC vs. Policy — Side by Side"]

| Aspect | Azure RBAC | Azure Policy |
|---|---|---|
| Controls | Who can take actions | What configurations are allowed |
| Example | "This user can create VMs" | "VMs must be created in East US only" |
| Enforcement | Authorization check | Configuration compliance check |
| Effect when violated | Access denied | Deny, Audit, or auto-remediate |

---

## Section 5: Microsoft Purview (14:00-17:30)

[SLIDE: "What Is Microsoft Purview?"]

[INSTRUCTOR ON CAMERA]

Microsoft Purview is Microsoft's unified data governance solution. Where Azure Policy governs Azure resource configurations, Purview governs data — what data you have, where it lives, who has access to it, and whether it complies with data privacy regulations.

Purview is important for organizations subject to data privacy laws like GDPR, HIPAA, CCPA, and similar regulations. These laws require organizations to know what personal data they hold, how it's classified, and how it flows through their systems.

[SLIDE: "Purview Core Capabilities"]

Purview has three main areas of capability.

Data Map — Purview scans your data sources — Azure Storage, Azure SQL, on-premises SQL Server, Salesforce, Power BI, and many others — and automatically discovers and catalogs the data assets. The data map gives you a complete picture of where your data lives.

Data Catalog — A searchable catalog of all your organization's data assets. Business users can search for data, understand what it contains, and find the owner. Data stewards can classify data and add business glossary terms. The catalog democratizes access to data knowledge across the organization.

Data Insights and Classification — Purview automatically classifies sensitive data using built-in classification rules. It can identify patterns that look like credit card numbers, Social Security numbers, health records, and other sensitive data categories. This classification is the foundation for data protection policies and privacy compliance reporting.

[SLIDE: "Purview and Compliance"]

For compliance purposes, Purview provides:

Sensitivity labels — Labels like Confidential, Highly Confidential, or Public that are applied to data assets based on classification. These labels can be the same labels used in Microsoft 365 for email and document protection.

Data lineage — Traces how data moves from its source through transformations to its destination. This is critical for understanding how personal data flows through ETL pipelines and report systems.

Policy management — Purview policies control who can access what data based on sensitivity classifications.

[SLIDE: "Purview for AZ-900"]

For the AZ-900 exam, know that:

Microsoft Purview is a unified data governance and compliance solution. It scans, catalogs, and classifies data across your Azure and on-premises environment. It is primarily relevant for data privacy compliance (GDPR, HIPAA). It is distinct from Azure Policy, which governs resource configurations rather than data.

---

## Section 6: Azure Blueprints (17:30-19:30)

[SLIDE: "What Is Azure Blueprints?"]

[INSTRUCTOR ON CAMERA]

Azure Blueprints is a service that packages together the elements needed to create a compliant, governed Azure environment and deploys them as a unit. Think of it as an environment template that includes not just resources, but also policies, role assignments, and resource group structures.

A blueprint can contain: ARM templates (resource definitions), Azure Policy assignments, RBAC role assignments, and resource group scaffolding. When you deploy a blueprint, all of these components are deployed together and tracked as a single managed package.

[SLIDE: "Blueprint Use Cases"]

Why would you use Blueprints? Here's the scenario: a large enterprise needs to provision new Azure environments that are compliant with their security standards from day one. Instead of manually creating the subscription, assigning policies, setting up resource groups, and assigning roles — and hoping nothing gets missed — a blueprint automates all of that in a single deployment.

Blueprints also maintain a link between the blueprint definition and the deployed environment. Changes to the blueprint can be pushed to existing deployments. And blueprint assignments are protected — you can prevent certain resources from being deleted if they're part of a blueprint assignment.

[SLIDE: "Azure Blueprints — Current Status"]

An important note for context: Microsoft announced in 2023 that Azure Blueprints is being retired in favor of using ARM templates (Bicep), Azure Policy, and Management Groups together to accomplish the same governance goals. The Azure Blueprints service is being deprecated over time.

For the AZ-900 exam, you should understand what Blueprints was designed to do — package governance components together for environment deployment — and know that it is being retired in favor of the component services. But exam questions about Blueprints may still appear since exam content lags real-world service changes.

---

## Section 7: Putting Governance Together (19:30-23:00)

[SLIDE: "The Azure Governance Stack"]

[INSTRUCTOR ON CAMERA]

Let me summarize how these tools work together in a real enterprise.

The Management Group hierarchy provides the organizational structure. Your subscriptions are organized into a tree: Production under one group, Development under another, Shared Services under a third.

Azure Policy provides the rules. Policies are assigned at the management group level so they cascade to all subscriptions and resources. Common policies: allowed regions, required tags, required encryption, approved resource types.

Azure RBAC provides access control. Different teams have different roles at different scopes. The DevOps team has Contributor on production subscriptions. Developers have Contributor on development subscriptions. The compliance team has Reader everywhere.

Microsoft Purview provides data governance. Across all the storage accounts and databases in all those subscriptions, Purview discovers and classifies the sensitive data to support privacy compliance.

And Defender for Cloud sits on top of all of it — assessing whether your Policy enforcement is working, whether resources have drifted out of compliance, and what security gaps remain.

[SLIDE: "Governance Scenario Practice"]

Let me test your governance service selection with a quick scenario.

Scenario: "A financial services company with 40 Azure subscriptions wants to ensure that no resources outside of the United States are ever provisioned in any subscription, and wants to apply this rule once rather than 40 times."

The answer is: Azure Policy with an "Allowed locations" policy definition assigned at the Root Management Group or a company-level management group. Policy + Management Group = single assignment covers all subscriptions through inheritance.

Scenario: "A healthcare company wants to find all the data stores in their Azure environment that contain patient health information to prepare for a HIPAA compliance audit."

The answer is: Microsoft Purview. Purview scans data sources and uses classification rules to identify protected health information, giving the compliance team the inventory they need.

---

## Section 8: Closing (23:00-24:00)

[INSTRUCTOR ON CAMERA]

Let's recap. Azure Policy defines configuration rules that enforce governance — what resources can be created, where, and with what settings. Policy effects include Deny, Audit, and DeployIfNotExists. Initiatives group related policies for scale. Assignments connect policies to scopes.

Management Groups organize subscriptions into a hierarchy, enabling single-assignment governance through scope inheritance.

Azure Policy and RBAC are complementary: RBAC controls who, Policy controls what configurations.

Microsoft Purview governs data — discovering, classifying, and protecting sensitive data across your environment for privacy compliance.

Azure Blueprints packaged governance components together for environment deployment and is being retired.

In the lab, you will create and assign an Azure Policy and observe its compliance effect. See you in the reading guide.

---

Module 12 Video Script | CIS-4331 Azure Cloud | Texas Wesleyan University
