# Quiz: Module 12 - Azure Governance and Compliance

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure management and governance (30-35% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A company has 30 Azure subscriptions across multiple business units. They want to apply an "Allowed locations = East US only" Azure Policy across all subscriptions simultaneously without creating 30 separate policy assignments. What is the most efficient solution?

- A) Create an Entra ID group containing all subscription contributors and assign the policy to the group
- B) Assign the policy at the Root Management Group level so it inherits to all subscriptions
- C) Write an Azure PowerShell script that assigns the policy to each subscription in a loop
- D) Use Azure Blueprints to deploy the policy to each subscription at provisioning time

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Assigning Azure Policy at a Management Group level causes the policy to be inherited by all child management groups, subscriptions, resource groups, and resources. A single assignment at the Root Management Group — or at a company-level management group containing all subscriptions — is the correct, scalable, and low-maintenance solution. New subscriptions added to the management group automatically inherit the policy.
- *Why A is incorrect:* Azure Policy assignments are applied to resource scopes (management groups, subscriptions, resource groups) — not to Entra ID groups. Policy is about resource configuration governance, not identity.
- *Why C is incorrect:* A script that assigns the policy to each subscription individually works, but it is operationally inefficient, requires re-running when new subscriptions are added, and does not represent the Azure governance best practice. Management group-level assignment is the correct architectural answer.
- *Why D is incorrect:* Azure Blueprints is used for initial environment provisioning — deploying a set of governance components when a new subscription is created. It is not designed for applying ongoing governance policies to existing subscriptions, and it is being deprecated.

---

## Question 2

An Azure Policy is assigned with the Deny effect to a resource group. A user with the Owner role on the subscription tries to create a resource that violates this policy. What happens?

- A) The Owner role overrides the policy Deny because Owner is the highest privilege role
- B) The resource creation is blocked because Azure Policy Deny takes precedence over RBAC role assignments
- C) The resource creation succeeds but is flagged as non-compliant in the compliance dashboard
- D) The policy Deny only applies to users with the Contributor role, not Owner

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Policy Deny blocks a resource creation or update regardless of the user's RBAC role — including Owner. RBAC and Azure Policy are evaluated independently. The RBAC check determines if the user is authorized to take the action; the Policy check determines if the resulting resource configuration is permitted. Both must pass. A Deny policy blocks the configuration even if RBAC would allow the action.
- *Why A is incorrect:* The Owner role does not override Azure Policy. RBAC and Policy are separate evaluation systems with no precedence relationship between roles. Policy Deny always blocks, regardless of role.
- *Why C is incorrect:* This describes the Audit effect, not the Deny effect. Deny blocks the operation entirely — the resource is not created. Audit allows the creation but logs the violation.
- *Why D is incorrect:* Azure Policy Deny applies to all principals regardless of role. It is not role-selective. Owner, Contributor, and even service principals are all subject to Policy Deny.

---

## Question 3

A company is subject to GDPR and needs to identify all data stores in their Azure environment that contain personal data, including customer names, email addresses, and passport numbers. Which Azure service addresses this requirement?

- A) Microsoft Defender for Cloud with regulatory compliance dashboard
- B) Azure Policy with Audit effect on storage accounts
- C) Microsoft Purview with data classification and scanning
- D) Azure Monitor with custom log queries

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Microsoft Purview is the data governance solution that scans data stores — Azure Storage, Azure SQL, Data Lake, and others — and applies built-in classification rules to identify sensitive data patterns including personal data categories (names, email addresses, passport numbers, Social Security numbers, credit card numbers). This data map and classification is precisely what GDPR compliance discovery requires.
- *Why A is incorrect:* Defender for Cloud's regulatory compliance dashboard maps Azure resource configurations against compliance framework controls. It does not scan data content inside storage accounts or databases to identify sensitive data.
- *Why B is incorrect:* Azure Policy governs resource configurations — whether encryption is enabled, whether public access is disabled, whether resources are in approved regions. It does not inspect data content to classify personally identifiable information.
- *Why D is incorrect:* Azure Monitor collects logs and metrics about resource behavior (performance, errors, activity). It does not scan data content stored in blobs or databases for sensitive data classification.

---

## Question 4

What is the difference between an Azure Policy Definition and a Policy Initiative?

- A) A Policy Definition is assigned at the subscription level; a Policy Initiative is assigned at the management group level
- B) A Policy Definition is a single governance rule; a Policy Initiative is a collection of related Policy Definitions assigned together as a group
- C) A Policy Definition enforces compliance; a Policy Initiative only reports compliance without enforcement
- D) A Policy Initiative is a custom policy; a Policy Definition is always a Microsoft-provided built-in policy

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A Policy Definition (or Policy Set Definition used as a standalone) is a single rule with a condition and effect. A Policy Initiative (also called a Policy Set Definition when combined) groups multiple related policy definitions into a single assignable unit. For example, the "Azure Security Benchmark" initiative contains dozens of individual policy definitions that together implement security best practices — assigned as one initiative rather than dozens of individual assignments.
- *Why A is incorrect:* Both Policy Definitions and Policy Initiatives can be assigned at any scope — management group, subscription, or resource group. The scope of assignment is independent of whether it is a definition or initiative.
- *Why C is incorrect:* Both Policy Definitions and Policy Initiatives can enforce compliance (using Deny, DeployIfNotExists, Modify effects) or report compliance (using Audit effect). The enforcement vs. reporting distinction is determined by the policy effect, not whether it is a definition or initiative.
- *Why D is incorrect:* Both Policy Definitions and Policy Initiatives can be Microsoft-provided built-in or customer-created custom. The built-in vs. custom distinction is independent of the definition vs. initiative distinction.

---

## Question 5

Which Azure Policy effect should be used when an organization wants to see which storage accounts have public blob access enabled, but does not want to block the configuration or automatically fix it yet?

- A) Deny
- B) DeployIfNotExists
- C) Audit
- D) Modify

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The Audit effect evaluates resources against the policy condition and marks non-compliant resources in the compliance dashboard without blocking the action or automatically remediating it. This is the appropriate starting point when an organization wants visibility into non-compliant configurations before committing to enforcement — commonly used when initially rolling out a new governance standard.
- *Why A is incorrect:* Deny blocks the resource creation or update if it violates the policy. The scenario explicitly states the organization does not want to block the configuration. Incorrect.
- *Why B is incorrect:* DeployIfNotExists automatically deploys a remediation resource when the policy condition is met. The scenario states they do not want automatic fixes. Incorrect.
- *Why D is incorrect:* Modify automatically changes resource properties to bring them into compliance. Again, the scenario states they do not want automatic remediation. Incorrect.

---

## Question 6

A management group contains three subscriptions. An Azure Policy is assigned at the management group with an Allowed Locations = East US only rule. A Subscription Administrator for one of the three subscriptions wants to allow resources to be created in West Europe specifically for their subscription. What can the Subscription Administrator do?

- A) Create a new Azure Policy at the subscription scope that allows West Europe — the subscription-level policy overrides the management group policy
- B) Remove the management group policy assignment entirely and recreate it with West Europe included
- C) Request an exclusion for their subscription from the management group policy assignment, or request that West Europe be added to the allowed locations list
- D) Assign themselves the Owner role at the management group level to modify the policy

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Policy assignments at higher scopes cannot be overridden by lower-scope policy assignments — the management group policy takes precedence. The correct approach is either (1) requesting the management group administrator to add an exclusion for the specific subscription or specific resources, or (2) requesting the allowed locations list be updated to include West Europe. Policy governance requires working through the proper governance hierarchy.
- *Why A is incorrect:* Unlike RBAC (which is additive), Azure Policy assignments at higher scopes cannot be overridden at lower scopes. A subscription-level policy allowing West Europe does not override the management group Deny policy for West Europe. Both policies are evaluated, and the Deny from the management group wins.
- *Why B is incorrect:* Removing the management group policy would remove governance from all three subscriptions — a disproportionate change that breaks the governance model for the other two subscriptions. This is not the correct approach.
- *Why D is incorrect:* Having Owner at the management group level would allow modifying the policy assignment, but the Subscription Administrator does not have that role and should not be granted it just to add a policy exclusion. The correct process is a governance request to the management group administrator.

---

## Question 7

An organization runs 8 hospital campuses, each with their own Azure subscription. The central IT team wants to apply a HIPAA-related Azure Policy initiative across all campus subscriptions. How should the hierarchy be structured for maximum governance efficiency?

- A) Assign the policy initiative to each campus subscription individually
- B) Create a Management Group containing all 8 campus subscriptions and assign the policy initiative at the management group level
- C) Create an Entra ID security group with all subscription owners and assign the policy to the group
- D) Use Azure Blueprints to deploy the policy to each campus subscription

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Management Groups are designed exactly for this scenario — organizing multiple subscriptions for unified governance. Assigning the HIPAA policy initiative at the management group level applies it to all 8 subscriptions through scope inheritance. When a 9th campus is added to the management group, the policy automatically applies.
- *Why A is incorrect:* Assigning to each subscription individually requires 8 separate assignments (not 1), and any new campus subscription requires a manual assignment. This approach is operationally inefficient and error-prone at scale.
- *Why C is incorrect:* Azure Policy assignments are applied to resource scopes, not to identity groups. Policy governance is a scope-based model.
- *Why D is incorrect:* Blueprints are for provisioning-time governance, not ongoing compliance policy application across existing subscriptions. Blueprints is also being deprecated.

---

## Question 8

Microsoft Purview's Data Map capability discovers and catalogs data assets from Azure and other sources. What must happen before Purview can classify data in an Azure Data Lake Storage account?

- A) The storage account must be migrated to Azure Blob Storage before Purview can scan it
- B) Purview requires an Azure Policy to first tag the storage account as a data source
- C) A scan must be configured in Purview that authenticates to the storage account and runs the classification scan
- D) The storage account must be moved into the same resource group as the Purview account

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Microsoft Purview uses configured scans to discover and classify data. To scan an Azure Data Lake Storage account, you register the storage account as a data source in Purview, configure authentication (managed identity or service principal with appropriate storage permissions), and run or schedule the scan. The scan reads the data and applies classification rules to identify sensitive data patterns.
- *Why A is incorrect:* Purview can scan Azure Data Lake Storage directly. Migration to Blob Storage is not required. Purview supports Azure Data Lake Storage Gen2 as a native scan target.
- *Why B is incorrect:* Azure Policy and Purview are independent services. Tagging a storage account with Azure Policy has nothing to do with enabling Purview to scan it. Purview scanning requires Purview-specific authentication and scan configuration.
- *Why D is incorrect:* Purview scans resources across subscriptions and resource groups. The storage account and Purview account do not need to be in the same resource group. Purview is a tenant-wide governance service, not resource-group-scoped.

---

## Question 9

Azure Blueprints is being deprecated. What combination of Azure services is Microsoft recommending as the replacement for Blueprints' governance provisioning capabilities?

- A) Azure DevOps pipelines and GitHub Actions
- B) Azure Policy, Azure RBAC, ARM templates (or Bicep), and Management Groups
- C) Microsoft Purview compliance assessments and Defender for Cloud
- D) Azure Automation runbooks and Log Analytics workspaces

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Blueprints packaged together ARM templates (for resource deployment), Azure Policy assignments, RBAC role assignments, and resource group scaffolding. Microsoft's recommendation is to use those component services directly: ARM templates or Bicep for infrastructure as code, Azure Policy for governance rules, RBAC for access control, and Management Groups for hierarchical scope. These services are more capable individually than Blueprints was as an orchestration layer.
- *Why A is incorrect:* Azure DevOps and GitHub Actions are CI/CD pipeline tools. While they can deploy infrastructure, they are not replacements for Azure governance services. They do not provide native Policy or RBAC management capabilities.
- *Why C is incorrect:* Purview and Defender for Cloud address data governance and security posture, respectively. They do not replace Blueprints' environment provisioning capabilities (deploying resources, assigning policies at scale, setting RBAC).
- *Why D is incorrect:* Azure Automation and Log Analytics are operations and monitoring tools. They do not provide the governance provisioning capabilities that Blueprints offered.

---

## Question 10

A governance team at a financial services company wants to audit which Azure resources across all their subscriptions do NOT have a required "DataClassification" tag. They want a report showing all non-tagged resources without blocking any operations. Which Azure Policy configuration achieves this?

- A) Create a custom Deny policy for resources missing the DataClassification tag and assign it at the Root Management Group
- B) Create a custom Audit policy for resources missing the DataClassification tag and assign it at the Root Management Group
- C) Use Microsoft Purview to scan all subscriptions for resources missing the tag
- D) Use Azure Monitor alerts to detect resource creation events that do not include the DataClassification tag

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* An Azure Policy with the Audit effect evaluates resources against the condition (missing the DataClassification tag), marks non-compliant resources in the policy compliance dashboard, and does not block any operations. Assigning it at the Root Management Group (or an appropriate parent management group) ensures all subscriptions are covered through scope inheritance. The compliance dashboard provides the audit report the team needs.
- *Why A is incorrect:* A Deny policy would block the creation of any new resource missing the tag. The scenario says the team wants to audit without blocking operations. Deny is not appropriate here.
- *Why C is incorrect:* Microsoft Purview scans data content inside storage resources for data classification. It does not scan Azure resource metadata (like resource tags) for governance compliance reporting. That is Azure Policy's function.
- *Why D is incorrect:* Azure Monitor can alert on resource creation events, but it does not provide a compliance dashboard that tracks non-tagged resources over time or integrates with Azure Policy compliance reporting. Azure Policy Audit is the designed solution for this compliance reporting use case.

---

Quiz 12 | CIS-4331 Azure Cloud | Texas Wesleyan University
