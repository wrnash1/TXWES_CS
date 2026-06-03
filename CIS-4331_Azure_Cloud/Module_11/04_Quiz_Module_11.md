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
