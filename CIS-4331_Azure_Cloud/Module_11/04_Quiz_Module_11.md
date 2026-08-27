# Quiz: Module 11 — Azure Identity, Security, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure identity, access, and security + Describe Azure management and governance

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. Total: 100 points.

---

### Question 1

A company wants to require MFA for all users accessing the Azure Portal only when they are connecting from IP addresses outside the corporate network. Security Defaults are currently enabled. Which change is required to implement this policy?

A. Upgrade to Microsoft Entra ID P2 and configure Identity Protection

B. Disable Security Defaults and create a Conditional Access Policy — requiring P1 licensing

C. Enable the MFA per-user setting in the Azure Portal for all user accounts

D. Add the Azure Portal URL to the list of restricted applications in Security Defaults

**Correct Answer: B**

**Distractor Analysis:**

- **A (Entra ID P2 + Identity Protection):** P2 and Identity Protection provide risk-based Conditional Access policies. The described policy uses a location-based condition, not risk detection. P1 with Conditional Access is sufficient. P2 is more than needed. Incorrect.
- **B — CORRECT:** Security Defaults apply blanket MFA and cannot be customized by location. To apply MFA conditionally from outside the corporate network, Security Defaults must be disabled and replaced with Conditional Access Policies. Conditional Access requires Entra ID P1 licensing.
- **C (Per-user MFA):** Per-user MFA forces MFA on every sign-in regardless of location. It cannot apply MFA only from outside the corporate network. Incorrect.
- **D:** Security Defaults do not have a configuration interface for application URL restrictions or location conditions. They are a fixed policy set. Incorrect.

---

### Question 2

A junior developer has been assigned the Contributor role on an Azure subscription. They need to grant a colleague access to a specific virtual machine to help with debugging. Can the junior developer grant this access?

A. Yes — Contributor can manage all Azure resources including access control

B. Yes — but only if the colleague has an existing Entra ID account in the same tenant

C. No — Contributor cannot assign roles; only Owner or User Access Administrator can assign roles

D. No — role assignments require Global Administrator privileges in Microsoft Entra ID

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Incorrect. Contributor can create and manage resources but explicitly cannot manage access. Assigning roles is not included in the Contributor role definition.
- **B:** Incorrect. Having an Entra ID account is a prerequisite to receive a role assignment, but a Contributor still cannot assign roles regardless of the target user's account.
- **C — CORRECT:** Contributor grants permissions to create and manage resources but specifically excludes role assignment. Only Owner, User Access Administrator, or a custom role with `Microsoft.Authorization/roleAssignments/write` can assign roles.
- **D:** Incorrect. Global Administrator is an Entra ID directory role, not an Azure RBAC role. Global Administrators do not automatically have Azure RBAC permissions. Also, role assignment requires Owner or User Access Administrator — not Global Administrator.

---

### Question 3

An organization wants to prevent its development team from creating Azure resources in any region outside of the United States. Which service enforces this governance requirement?

A. Azure RBAC with a custom role that limits allowed regions

B. Microsoft Entra ID Conditional Access with a location policy

C. Azure Policy with a Deny effect on non-US regions

D. Azure Firewall with geographic IP filtering

**Correct Answer: C**

**Distractor Analysis:**

- **A (Azure RBAC):** Azure RBAC controls who can take actions, not what configurations are allowed. RBAC does not have a built-in mechanism to restrict resource creation to specific regions. Incorrect.
- **B (Conditional Access with location policy):** Conditional Access controls authentication conditions for Entra ID sign-ins. It does not govern Azure resource configurations or restrict which regions resources can be created in. Incorrect.
- **C (Azure Policy with Deny) — CORRECT:** Azure Policy is the governance tool for enforcing resource configuration requirements. The built-in "Allowed locations" policy can be assigned with a Deny effect to block resource creation in non-US regions.
- **D (Azure Firewall):** Azure Firewall controls network traffic within VNets. It does not govern Azure resource management plane operations like which regions resources are created in. Incorrect.

---

### Question 4

A security team needs to store database connection strings, API keys, and TLS certificates for a web application in a secure, centralized location. Application code must not contain any hardcoded credentials. Which Azure service best addresses this requirement?

A. Azure Storage Account with Private access

B. Azure Key Vault

C. Microsoft Entra ID application registration secrets

D. Azure App Service application settings

**Correct Answer: B**

**Distractor Analysis:**

- **A (Azure Storage):** Azure Storage can store files securely but does not provide a managed secrets API with fine-grained access control, audit logging, HSM key support, or managed identity authentication for secret retrieval. Incorrect.
- **B (Azure Key Vault) — CORRECT:** Azure Key Vault stores secrets, keys, and certificates. It provides fine-grained RBAC access control, complete audit logging, managed identity integration (applications authenticate with no stored password), and HSM-backed key storage. This is the correct answer for "store credentials securely, no hardcoded secrets."
- **C (Entra ID application registration secrets):** Application registration client secrets are used for app-to-app authentication (OAuth 2.0 flows). They do not serve as a general-purpose secret store for database connection strings or TLS certificates. Incorrect.
- **D (App Service application settings):** App Service application settings store configuration values but are not encrypted at the Key Vault level, do not support certificate storage, provide less audit logging, and expose secrets to anyone with App Service management access. Incorrect.

---

### Question 5

A company's Azure Secure Score in Microsoft Defender for Cloud is 42%. A security recommendation states: "Enable MFA for all accounts with write permissions on your subscription." What would implementing this recommendation do to the Secure Score?

A. It would have no effect because MFA is controlled by Entra ID, not Defender for Cloud

B. It would reduce the Secure Score because adding MFA requirements is a restrictive change

C. It would increase the Secure Score because the recommendation represents a security control gap

D. It would reset the Secure Score to 0 because changing MFA settings requires a full re-evaluation

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Incorrect. Defender for Cloud evaluates security posture across Azure services, including Entra ID MFA configuration. Implementing MFA directly addresses a Defender for Cloud recommendation and improves the Secure Score.
- **B:** Incorrect. The Secure Score increases as you implement security recommendations. Implementing security controls reduces the risk measured by the score.
- **C — CORRECT:** Defender for Cloud Secure Score is calculated based on how many security controls are satisfied. The MFA recommendation is a control gap. Implementing it satisfies that control and increases the Secure Score by the weighted points assigned to that recommendation.
- **D:** Incorrect. Changing MFA settings triggers a re-evaluation of that specific control — it does not reset the entire Secure Score.

---

### Question 6

An organization has three Azure subscriptions: Production, Development, and Testing. The security team wants to apply an Azure Policy that requires all resources to have a "CostCenter" tag. How can they apply this policy once and have it automatically enforce across all three subscriptions?

A. Assign the policy to each subscription individually using the Azure Portal

B. Use Management Groups to create a parent group containing all three subscriptions and assign the policy at the Management Group level

C. Create an Entra ID group containing all subscription owners and assign the policy to the group

D. Use Azure Blueprints to deploy the policy across all subscriptions simultaneously

**Correct Answer: B**

**Distractor Analysis:**

- **A (Assign to each subscription individually):** This works but requires three separate assignments. If a fourth subscription is added, the team must assign the policy again manually. This does not scale and is error-prone. Not the best answer for "apply once."
- **B (Management Groups) — CORRECT:** Management Groups allow organizing subscriptions into a hierarchy. Assigning a policy at the Management Group level automatically applies it to all subscriptions within that group — current and future. This is the correct, scalable governance pattern.
- **C (Entra ID group):** Azure Policy is assigned to scopes (management groups, subscriptions, resource groups) — not to Entra ID groups or users. Policy assignment is a governance action, not an identity action. Incorrect.
- **D (Azure Blueprints):** Blueprints can deploy policies across subscriptions but are typically used for initial environment setup. Management Groups with Policy assignment is the standard ongoing compliance pattern. Also, Blueprints is being deprecated. Incorrect.

---

### Question 7

Which of the following correctly describes the difference between Azure RBAC and Microsoft Entra ID roles?

A. Azure RBAC controls who can sign in to Azure; Entra ID roles control what resources users can access

B. Azure RBAC controls access to Azure resources such as VMs and storage; Entra ID roles control access to directory objects such as users, groups, and tenant settings

C. Azure RBAC is only for subscription-level access; Entra ID roles are only for resource-level access

D. They are the same system — an Entra ID Global Administrator automatically has Owner access to all Azure resources

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. Authentication (who can sign in) is controlled by Entra ID user accounts and Conditional Access — not by RBAC. RBAC controls resource access after authentication.
- **B — CORRECT:** Azure RBAC governs operations on Azure resources (create/read/update/delete on VMs, storage, databases, etc.). Entra ID roles govern operations on directory objects (creating users, resetting passwords, managing applications, configuring tenant settings). They are separate, parallel systems.
- **C:** Incorrect. Azure RBAC can be applied at management group, subscription, resource group, or individual resource scope — not only subscription level.
- **D:** Incorrect. Entra ID Global Administrator is a directory role. It does not grant Azure subscription Owner rights by default. Elevating to User Access Administrator on the root management group is a separate, manual, explicit action.

---

### Question 8

A company wants to ensure all Azure SQL Databases created in their subscription automatically have Transparent Data Encryption (TDE) enabled, and that any SQL Database found without TDE is automatically remediated. Which Azure Policy effect should be used?

A. Deny

B. Audit

C. DeployIfNotExists

D. Append

**Correct Answer: C**

**Distractor Analysis:**

- **A (Deny):** Deny would block the creation of SQL Databases without TDE. However, it blocks the deployment entirely rather than deploying the database and automatically enabling TDE. It also would not remediate existing non-compliant databases. Does not meet the "automatically remediated" requirement. Incorrect.
- **B (Audit):** Audit flags non-compliant databases in the compliance dashboard but does not prevent the misconfiguration or automatically fix it. Incorrect for automatic remediation.
- **C (DeployIfNotExists) — CORRECT:** DeployIfNotExists checks whether a required related resource or setting exists and automatically deploys or configures it if missing. This is the correct effect for "automatically enable TDE if it is not present" — it both flags non-compliance and triggers remediation.
- **D (Append):** Append adds additional properties to a resource during creation (such as adding a required tag). It does not trigger deployment of related resources or enable existing settings. Incorrect.

---

### Question 9

A DevOps team wants to give a third-party monitoring tool access to read log data from an Azure Storage Account. The tool runs on an external server outside of Azure. They do not want to create a permanent service account or manage passwords. Which option provides secure, time-limited access?

A. Create a new user in Entra ID for the monitoring tool

B. Assign the Reader role to the storage account for the tool's IP address

C. Generate a Shared Access Signature (SAS) token from Key Vault

D. Generate a Shared Access Signature (SAS) token from the Storage Account with limited permissions and an expiry date

**Correct Answer: D**

**Distractor Analysis:**

- **A (New Entra ID user):** Creating a user account for an external tool creates a persistent identity that requires password management, rotation, and eventual deprovisioning. It also typically grants broader permissions than needed. Incorrect.
- **B (Reader role for IP address):** Azure RBAC role assignments are applied to security principals (users, groups, service principals) — not to IP addresses. There is no native mechanism to assign RBAC permissions based on IP. Incorrect.
- **C (SAS from Key Vault):** Azure Key Vault stores secrets and keys but does not generate SAS tokens. SAS tokens are generated from the Azure Storage service itself. Incorrect.
- **D (Storage SAS token) — CORRECT:** A Shared Access Signature (SAS) token is a URI that grants restricted, time-limited access to Azure Storage resources without requiring a full account key or Azure RBAC assignment. You define the allowed permissions (read-only), specific resources, and an expiry date. This is the correct approach for temporary, scoped external access.

---

### Question 10

When using Microsoft Entra Conditional Access, a policy is configured with these settings: Users = All users; Target app = Microsoft Azure Management; Conditions = Sign-in risk = High (requires P2); Grant = Block access. What is the effect of this policy?

A. All users are blocked from the Azure Portal regardless of sign-in risk

B. Users with a high-risk sign-in attempt to the Azure Portal are blocked from accessing it

C. Users are blocked from the Azure Portal until they complete MFA, after which access is granted

D. The policy has no effect because Sign-in risk conditions require Azure Firewall integration

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. The policy has a condition: Sign-in risk = High. Users signing in with normal, low-risk signals are not affected by this policy.
- **B — CORRECT:** This Conditional Access policy targets Microsoft Azure Management. When a user's sign-in risk is evaluated as High by Identity Protection (indicating potentially compromised credentials), the Block access Grant control is applied — preventing access to the Azure Portal for that risky sign-in attempt.
- **C:** Incorrect. The Grant control is Block access, not Require MFA. Block access denies the session entirely. If the intent was to allow access after MFA, the Grant control would be Require MFA.
- **D:** Incorrect. Sign-in risk conditions are evaluated by Entra Identity Protection using machine learning signals (unfamiliar location, leaked credentials, anonymous IP, etc.). They do not require Azure Firewall. Sign-in risk conditions require Entra ID P2.

---

*Quiz 11 — Module 11: Azure Identity, Security, and Governance | CIS-4331 | Texas Wesleyan University*

---

### Question 11 (5 points)

A company has both on-premises Active Directory and Microsoft Entra ID. Users must sign in once and access both on-premises applications (SharePoint on-premises) and cloud applications (Microsoft 365, Salesforce) without being prompted for credentials again. Which Microsoft feature enables this hybrid single sign-on experience?

- A) Microsoft Entra ID External Identities (B2B)
- B) Microsoft Entra Connect with Password Hash Synchronization or Pass-through Authentication
- C) Azure AD Domain Services (ADDS)
- D) Microsoft Entra ID B2C (Business-to-Consumer)

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Microsoft Entra Connect synchronizes on-premises Active Directory identities to Entra ID. With Password Hash Synchronization or Pass-through Authentication, users authenticate once with their on-premises credentials and get SSO to both on-premises and cloud applications through seamless SSO. This is the standard hybrid identity architecture for organizations bridging on-premises AD and cloud.
  - *Why A is incorrect:* Entra ID External Identities (B2B) is for inviting external users from partner organizations to access your tenant's resources. It is not for synchronizing your own on-premises employees to the cloud.
  - *Why C is incorrect:* Azure AD Domain Services provides managed domain services (LDAP, Kerberos, NTLM) in the cloud for legacy applications. It is not the tool for synchronizing on-premises AD users to Entra ID or enabling hybrid SSO.
  - *Why D is incorrect:* Entra ID B2C is for customer-facing applications that allow consumers to sign in with social identities (Google, Facebook) or local accounts. It is unrelated to hybrid employee identity synchronization.

---

### Question 12 (5 points)

A security administrator reviews an Azure Policy compliance report and finds that 15 storage accounts are non-compliant because they allow public blob access. The policy uses an Audit effect. What action must the administrator take to remediate the non-compliant resources?

- A) Nothing — Audit policies automatically remediate non-compliant resources within 24 hours
- B) Change the policy effect from Audit to Deny to prevent future non-compliance, and manually remediate the 15 existing non-compliant storage accounts
- C) Delete and recreate all 15 storage accounts with the correct configuration
- D) Assign the policy with a Modify effect, which will automatically disable public blob access on all non-compliant resources

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Audit effect only logs non-compliance — it does not automatically fix existing resources. To prevent future violations, the administrator should consider changing to Deny (which blocks new non-compliant deployments). Existing 15 accounts must be manually remediated (or remediated via a remediation task if using DeployIfNotExists/Modify effects). Changing to Audit alone does not remediate.
  - *Why A is incorrect:* Audit effect never automatically remediates resources. It only records non-compliance in the policy compliance report. Automatic remediation requires DeployIfNotExists or Modify effects with a remediation task.
  - *Why C is incorrect:* Deleting and recreating 15 storage accounts would cause data loss and service disruption. The correct remediation is to change the public blob access setting on existing accounts — a non-destructive configuration change.
  - *Why D is incorrect:* The Modify effect can automatically add, update, or remove resource properties on existing resources (via remediation tasks). However, Modify is used for tagging and specific property changes. For disabling public blob access, the administrator would need to use an Azure Policy with Modify effect specifically designed for that property — not simply changing the existing Audit policy to Modify.

---

### Question 13 (5 points)

A company deploys an Azure App Service web application and wants the application to authenticate to Azure Key Vault to retrieve database secrets — without storing any credentials in the application code or configuration files. Which authentication mechanism should be used?

- A) Store the Key Vault access key in the App Service application settings
- B) Create a service principal with a client secret and store the secret in the app's code
- C) Enable a System-assigned Managed Identity on the App Service and grant it Key Vault Secrets User role
- D) Use the storage account key to access Key Vault through a connection string

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* A System-assigned Managed Identity creates an automatically managed identity in Entra ID for the App Service instance. This identity can be granted RBAC roles (like Key Vault Secrets User) on Key Vault. The application code uses the Azure SDK to request a token for the managed identity — no credentials are stored anywhere. When the App Service is deleted, the managed identity is automatically removed.
  - *Why A is incorrect:* Key Vault does not have an "access key" like a storage account. Key Vault access is controlled via RBAC or access policies authenticated with Entra ID tokens. There is no connection string or access key mechanism for Key Vault.
  - *Why B is incorrect:* Storing a client secret in application code or configuration is exactly the pattern Key Vault is designed to avoid — it creates the same secrets-in-code problem. Managed Identity eliminates the need for any stored credentials.
  - *Why D is incorrect:* Storage account keys are for Azure Storage authentication, not Azure Key Vault. Key Vault uses Entra ID token-based authentication exclusively.

---

### Question 14 (5 points)

An organization assigns the built-in Reader role to a user at the subscription scope. The same user is also assigned the Contributor role at a specific resource group scope within the subscription. What is the user's effective access to resources in that resource group?

- A) Reader only — the subscription-level assignment takes precedence over resource group assignments
- B) Contributor — the most permissive role at the narrowest scope takes precedence
- C) Contributor — Azure RBAC is additive; the user has the union of permissions from both role assignments
- D) No access — conflicting role assignments cancel each other out

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure RBAC is additive — a user's effective permissions are the union of all role assignments across all applicable scopes. The user has Reader permissions at the subscription scope (applies everywhere) plus Contributor permissions at the resource group scope. For resources in that resource group, the effective permissions are Reader + Contributor = Contributor capabilities (since Contributor is a superset of Reader for resource management).
  - *Why A is incorrect:* Azure RBAC does not have a "subscription-level takes precedence" rule. Permissions are additive — broader scope assignments do not override narrower ones.
  - *Why B is incorrect:* While the result is effectively Contributor access in the resource group, the reason is not "narrowest scope takes precedence." Azure RBAC does not have scope precedence — it has additive combination. The most-permissive result is correct but for the wrong stated reason.
  - *Why D is incorrect:* Azure RBAC has no concept of conflicting assignments canceling out. Deny assignments are a separate, explicit mechanism. Without a Deny assignment, all permissions from all role assignments are combined additively.

---

### Question 15 (5 points)

A company's Azure subscription contains resources in multiple regions. The compliance team wants to generate a report showing which resources are missing the required "Environment" tag (values: Production, Development, or Testing). They do not want to block any deployments — only identify gaps. Which Azure Policy effect should be used?

- A) Deny — blocks creation of resources without the required tag
- B) Append — automatically adds the tag with a default value if missing
- C) Modify — automatically updates resources to add the required tag
- D) Audit — logs non-compliance but allows resource creation to proceed

- **Correct Answer:** D
- **Distractor Analysis:**
  - *Why D is correct:* Audit effect evaluates resource compliance and logs non-compliant resources in the Azure Policy compliance dashboard without blocking any operations. This is exactly the requirement: identify gaps without blocking deployments. Compliance teams can use the Audit report to track and remediate tag gaps over time.
  - *Why A is incorrect:* Deny would prevent creating any resource without the required tag — this contradicts the stated requirement to not block deployments. It is appropriate when enforcement is needed, not when the goal is only visibility.
  - *Why B is incorrect:* Append adds the tag to resources at creation time but does not flag existing non-compliant resources. It also adds a tag automatically rather than requiring users to provide the correct value (Production, Development, Testing). It does not generate a compliance report.
  - *Why C is incorrect:* Modify automatically updates resources to add or change tags on existing resources. While this achieves remediation, it does not match the requirement to only report on gaps without making changes. The team wants visibility, not automated modification.

---

### Question 16 (5 points)

Microsoft Defender for Cloud provides a Secure Score to organizations. Which statement correctly describes how the Secure Score is calculated?

- A) The Secure Score is calculated based on the total number of Azure resources in the subscription — more resources means a lower score
- B) The Secure Score is the percentage of security controls that are fully satisfied out of all applicable controls, weighted by the potential score of each control
- C) The Secure Score is a letter grade (A through F) assigned by Microsoft based on monthly security audits
- D) The Secure Score is only calculated for subscriptions with Microsoft Defender plans enabled on all resource types

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The Secure Score is a percentage calculated as: (current score) / (maximum possible score) × 100. Each security control (a group of related recommendations) has a maximum point value. A control is fully satisfied when all its recommendations are completed. The score reflects how many controls are satisfied relative to how many are applicable, weighted by the point value of each control.
  - *Why A is incorrect:* Resource count does not determine the Secure Score. More resources may create more recommendations (since more resources need to be evaluated), but the score is a ratio of satisfied controls to total applicable controls — not an absolute number.
  - *Why C is incorrect:* The Secure Score is a numeric percentage (0–100%), not a letter grade. It is continuously updated as resources are created or modified and as recommendations are implemented — not assigned through periodic audits.
  - *Why D is incorrect:* The Secure Score is available in all Azure subscriptions with Defender for Cloud enabled (including the free foundational tier). Enhanced protections from paid Defender plans improve the recommendations available but are not required to see or improve the Secure Score.

---

### Question 17 (5 points)

A company has a Management Group hierarchy: Root Management Group → "CORP" Management Group → "Production" subscription. A policy with Deny effect is assigned at the "CORP" Management Group level. A developer tries to create a resource that violates this policy in the "Production" subscription. What happens?

- A) The resource is created successfully because subscription-level deployments cannot be blocked by Management Group policies
- B) The resource creation is blocked because the Deny policy assigned at the Management Group level is inherited by all subscriptions within that group
- C) The developer receives a warning but the resource is created with a non-compliant flag
- D) The policy only applies to resources in the Management Group's own resource groups, not to child subscriptions

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Policy assignments at a Management Group scope are inherited by all child management groups, subscriptions, resource groups, and resources within the hierarchy. A Deny effect policy assigned at the CORP Management Group applies to the Production subscription (which is a child of CORP), and the resource creation attempt will be blocked with an error.
  - *Why A is incorrect:* This is factually incorrect — Management Group policy assignments do cascade down to child subscriptions. That is one of the primary reasons for using Management Groups.
  - *Why C is incorrect:* Deny effect blocks the operation entirely. It does not issue a warning and proceed. Warning behavior is characteristic of Audit effect, not Deny.
  - *Why D is incorrect:* Management Groups do not have their own resource groups. They are organizational containers for subscriptions. Policy assigned at a Management Group level applies to all resources within all subscriptions in that group, not to a special "Management Group resource group."

---

### Question 18 (5 points)

An organization wants to use Microsoft Entra ID Privileged Identity Management (PIM) for their Azure subscription Owner role. Which behavior does PIM provide that standard RBAC role assignment does not?

- A) PIM allows users to hold the Owner role permanently without any audit logging
- B) PIM enables just-in-time role activation — users are eligible for the Owner role but must explicitly activate it for a limited time window, with justification and optional approval
- C) PIM prevents users from being assigned the Owner role entirely, replacing it with a custom read-only role
- D) PIM automatically rotates Owner role holders every 30 days to different users

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure AD Privileged Identity Management (PIM) introduces just-in-time (JIT) privileged access. Instead of permanently holding a powerful role like Owner, users are made "eligible" — they must explicitly activate the role for a configurable time window (e.g., 1–8 hours), provide a justification, and optionally obtain approval. After the window expires, the activation lapses and the user loses elevated access automatically. This minimizes standing privilege.
  - *Why A is incorrect:* PIM provides more audit logging, not less. Every activation request, approval, and deactivation is logged. Standard RBAC also logs role assignments but does not log time-limited activation events.
  - *Why C is incorrect:* PIM manages access to existing roles (including Owner) — it does not prevent assignment of roles or replace them with custom roles. Its purpose is to control when and how long users hold elevated permissions.
  - *Why D is incorrect:* PIM does not automatically rotate role holders. It provides time-limited activation for users who are eligible. Rotation of who is eligible is a manual governance decision.

---

### Question 19 (5 points)

A company stores a TLS certificate in Azure Key Vault and wants to ensure the certificate is automatically renewed 30 days before expiry without any manual intervention. Which Azure Key Vault feature provides this automation?

- A) Key Vault soft delete — automatically replaces deleted certificates with renewed versions
- B) Key Vault certificate lifecycle management with auto-renewal policy configured at certificate creation
- C) Azure Policy with a DeployIfNotExists effect that triggers certificate renewal
- D) Microsoft Defender for Key Vault, which monitors certificate expiry and triggers renewal

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Key Vault has built-in certificate lifecycle management. When creating or updating a certificate in Key Vault, you can configure an auto-renewal policy specifying the number of days before expiry to trigger renewal and the certificate authority (integrated CAs like DigiCert/GlobalSign, or self-signed). Key Vault then automatically renews the certificate and stores the new version — no manual intervention required.
  - *Why A is incorrect:* Soft delete is a data protection feature that retains deleted objects in a recoverable state for 7–90 days. It is a deletion recovery mechanism, not a certificate renewal mechanism.
  - *Why C is incorrect:* Azure Policy DeployIfNotExists is for deploying Azure resources and configurations, not for managing certificate content within Key Vault. There is no built-in Azure Policy that triggers Key Vault certificate renewals.
  - *Why D is incorrect:* Microsoft Defender for Key Vault monitors for suspicious access patterns and anomalous operations. It provides threat detection, not certificate lifecycle management or auto-renewal.

---

### Question 20 (5 points)

An organization needs to meet a compliance requirement that states: "All privileged administrative actions on Azure resources must be logged, and logs must be retained for at least 1 year and be tamper-evident." Which combination of Azure services satisfies this requirement?

- A) Azure Monitor Activity Log (retained indefinitely by default) with Azure Policy to enforce logging
- B) Azure Activity Log exported to an Azure Storage Account with immutability policy, combined with Log Analytics workspace with 1-year retention
- C) Microsoft Defender for Cloud Secure Score with a compliance standard assigned
- D) Azure Advisor recommendations with compliance tracking enabled

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Activity Log records all management plane operations (create, update, delete) on Azure resources — these are the privileged administrative actions. By default, Activity Log is only retained for 90 days. Exporting to an Azure Storage Account with an immutability policy (WORM) ensures tamper-evident storage. A Log Analytics workspace with a 1-year retention period satisfies the retention requirement. Together these components fulfill all three requirements: logging, 1-year retention, and tamper-evidence.
  - *Why A is incorrect:* Azure Activity Log is not retained indefinitely by default — the default retention is 90 days. Without export to a storage account or Log Analytics with extended retention, logs are lost after 90 days.
  - *Why C is incorrect:* Defender for Cloud Secure Score measures security posture through control satisfaction. Assigning a compliance standard (like ISO 27001 or PCI DSS) tracks policy compliance, but it does not capture or retain individual administrative action logs.
  - *Why D is incorrect:* Azure Advisor provides cost, security, and reliability recommendations based on current configuration. It does not log administrative actions or provide an audit trail of operations performed on Azure resources.
