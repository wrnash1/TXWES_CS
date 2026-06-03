# Video Script: Module 11 — Azure Identity, Security, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure Fundamentals (AZ-900)

---

## Opening (0:00–1:00)

Welcome to Module 11 of CIS-4331 Azure Cloud Computing. I'm Professor Nash. Today we are covering Azure Identity, Security, and Governance — the services and features that control who can access your Azure resources, how they authenticate, what actions they can take, and how your organization enforces cloud governance policies.

This is one of the highest-weighted topic areas on AZ-900, appearing in both the "Describe Azure Architecture and Services" domain and the "Describe Azure management and governance" domain. You need to understand Microsoft Entra ID (formerly Azure Active Directory), multi-factor authentication, Conditional Access, Role-Based Access Control, Azure Policy, Management Groups, Microsoft Defender for Cloud, and Azure Key Vault.

Let's get into it.

---

## Section 1: Microsoft Entra ID (Azure Active Directory) (1:00–5:00)

### What Is Microsoft Entra ID?

Microsoft Entra ID — formerly known as Azure Active Directory or Azure AD — is Microsoft's cloud-based identity and access management service. It is the directory service for Azure, Microsoft 365, and thousands of SaaS applications.

Entra ID is what allows users to sign in once and access Azure resources, Outlook, Teams, SharePoint, Salesforce, and any application integrated with the platform. It is the foundation of identity in the Microsoft cloud.

Important distinction for AZ-900: Microsoft Entra ID is NOT the same as Windows Server Active Directory. Windows Server AD uses the Kerberos and NTLM protocols and is designed for on-premises infrastructure. Entra ID uses modern protocols like OAuth 2.0, OpenID Connect, and SAML for cloud identity federation.

### Key Entra ID Concepts

**Tenant** — An instance of Entra ID that represents an organization. When a company signs up for Microsoft 365 or Azure, an Entra ID tenant is created. The tenant has a default domain like `contoso.onmicrosoft.com`.

**User** — An identity in the directory. Users have attributes (email, display name, job title) and can be assigned to groups, roles, and applications.

**Group** — A collection of users. Groups simplify permission management — assign permissions to the group, and all members inherit those permissions.

**Application Registration** — Registers an application with Entra ID so it can use Entra ID for authentication and authorization.

**Service Principal** — The identity used by an application or service to authenticate to Azure. When a VM or App Service needs to access Key Vault or Storage, it uses a managed identity — a form of service principal managed automatically by Azure.

### Entra ID Tiers

**Free tier** — Included with Azure subscriptions. Core identity features: user and group management, SSO, basic security reports.

**Microsoft Entra ID P1** — Adds Conditional Access, self-service password reset, Hybrid Identity support.

**Microsoft Entra ID P2** — Adds Identity Protection (risk-based sign-in detection) and Privileged Identity Management (just-in-time admin access).

[SHOW AZURE PORTAL] Navigate to Microsoft Entra ID > Overview. Show the tenant information, user count, and license tier. Navigate to Users > All users. Show how to create a new user and assign them to a group.

---

## Section 2: Multi-Factor Authentication (5:00–7:30)

### What Is MFA?

Multi-Factor Authentication, or MFA, requires users to provide two or more verification factors to sign in. The three authentication factor categories are:

**Something you know** — A password or PIN.

**Something you have** — A phone (SMS code or authenticator app), a hardware token, or a smart card.

**Something you are** — Biometrics: fingerprint, facial recognition.

MFA requires at least two of these three categories. Even if a password is stolen, an attacker cannot authenticate without also possessing the second factor.

### MFA in Entra ID

Microsoft Entra MFA is built into Entra ID. Users can register additional verification methods:

- Microsoft Authenticator app (push notification or one-time code)
- SMS text message code
- Phone call
- Hardware FIDO2 security key

**Security Defaults** — Microsoft provides free Security Defaults for all Entra ID tenants that enforces MFA for all users, blocks legacy authentication protocols, and requires MFA for admin roles. Enabled by default on new tenants.

For organizations needing more granular MFA control — requiring MFA only from certain locations, for certain apps, or for high-risk users — Conditional Access Policies provide that level of control.

---

## Section 3: Conditional Access (7:30–9:30)

### What Is Conditional Access?

Conditional Access is an Entra ID P1 feature that applies access control policies based on conditions. Instead of a blanket MFA requirement for all users on all devices from all locations, Conditional Access lets you define: "IF a user is signing in from outside our corporate network AND accessing a sensitive application, THEN require MFA."

Conditional Access policies evaluate signals — conditions — and apply access controls.

**Common signals (conditions):**

- User or group membership
- IP address or named location (on-premises network vs. unknown location)
- Device platform and compliance state
- Application being accessed
- Sign-in risk level (requires Entra ID P2 Identity Protection)

**Access controls (actions):**

- Require MFA
- Require compliant device
- Block access entirely
- Limit session duration

Example policy: "Require MFA for all users accessing the Azure Portal from outside our corporate IP range."

Example policy: "Block access to all corporate apps from countries where we have no employees."

[SHOW AZURE PORTAL] Navigate to Microsoft Entra ID > Security > Conditional Access > Policies. Show an existing policy. Walk through the "Users," "Target resources," "Conditions," and "Grant" configuration sections. Show how to set a location condition.

---

## Section 4: Role-Based Access Control (9:30–13:00)

### What Is RBAC?

Role-Based Access Control, or RBAC, is Azure's authorization system for controlling who has access to Azure resources, what they can do, and what scope those permissions apply to. RBAC enforces the principle of least privilege — granting only the permissions needed for a specific job function.

### RBAC Components

Three core components work together in every RBAC assignment.

**Security Principal** — Who gets the permission. This can be a user, a group, a service principal, or a managed identity.

**Role Definition** — What permissions are granted. A role is a collection of operations (actions) like read, write, delete, and start. Azure provides hundreds of built-in roles.

**Scope** — Where the permissions apply. Scope can be set at four levels: Management Group > Subscription > Resource Group > Individual Resource.

### Built-In Roles

These four built-in roles apply to almost all Azure resource types:

**Owner** — Full access to all resources and can grant access to others. The Owner role can delegate permissions to other users.

**Contributor** — Can create and manage all types of Azure resources but cannot grant access to others. Cannot modify role assignments.

**Reader** — Can view resources but cannot make any changes.

**User Access Administrator** — Can manage user access to Azure resources. Cannot create or manage resources.

There are also resource-specific built-in roles: Virtual Machine Contributor, Storage Blob Data Reader, Key Vault Secrets Officer, and many more.

### RBAC Inheritance

RBAC assignments inherit downward through the scope hierarchy. If you assign the Reader role to a user at the Subscription scope, that user has Reader access to every resource group and every resource within that subscription.

This is both powerful and something to watch carefully — a broad scope assignment cascades to all child resources.

[SHOW AZURE PORTAL] Navigate to a Resource Group > Access control (IAM). Show the Role assignments tab. Show the Add role assignment workflow — selecting a role, then a security principal. Show the Check access button to verify a user's effective permissions.

### RBAC vs. Entra ID Roles

Important distinction: Azure RBAC controls access to Azure resources (VMs, Storage, Databases). Entra ID roles (like Global Administrator, User Administrator) control access to the Entra ID directory itself — creating users, managing groups, and configuring tenant settings.

These are two separate role systems. A user can have the Azure Owner role at the subscription level but not be a Global Administrator in Entra ID — and vice versa.

---

## Section 5: Azure Policy (13:00–15:30)

### What Is Azure Policy?

Azure Policy is a governance service that creates, assigns, and enforces rules about Azure resource configurations. While RBAC controls who can do what, Azure Policy controls what types of resources can be created and what configurations are required or prohibited.

Examples of what Azure Policy can enforce:

- "All storage accounts must use HTTPS-only and TLS 1.2 minimum"
- "Virtual machines may only be created in East US or West US 2 regions"
- "All resources must have a specific cost center tag"
- "Azure SQL Databases must have Transparent Data Encryption enabled"

### Policy Effects

Policies can have different effects:

**Deny** — Prevent the resource creation or configuration change from completing.

**Audit** — Allow the action but log a compliance warning. Does not block anything.

**DeployIfNotExists** — If a resource does not have a required configuration, automatically deploy a remediation resource.

**Modify** — Automatically add or change resource properties at creation time (like adding tags).

### Policy Initiatives

An Initiative (also called a Policy Set Definition) is a collection of related policies grouped together and assigned as a single unit. For example, the "Enable Monitoring in Azure Security Center" initiative contains dozens of individual policies that together implement security monitoring best practices.

---

## Section 6: Management Groups (15:30–17:00)

### What Are Management Groups?

Management Groups allow you to organize multiple Azure subscriptions into a hierarchy for unified governance. Policies and RBAC assignments applied at a Management Group level cascade down to all subscriptions, resource groups, and resources within that group.

A typical enterprise hierarchy:

- Root Management Group (top of hierarchy)
  - Production Management Group → contains production subscriptions
  - Development Management Group → contains dev/test subscriptions
  - IT Management Group → contains shared services subscriptions

This hierarchy allows an enterprise to assign a policy once at the "Production" management group and have it automatically apply to all production subscriptions — without repeating the assignment on each subscription individually.

[SHOW AZURE PORTAL] Navigate to Management Groups. Show the hierarchy view. Show how to move a subscription under a management group. Show a policy assignment at the management group level.

---

## Section 7: Microsoft Defender for Cloud (17:00–19:30)

### What Is Defender for Cloud?

Microsoft Defender for Cloud is a Cloud Security Posture Management (CSPM) and cloud workload protection service. It continuously monitors your Azure, multi-cloud (AWS, GCP), and on-premises resources for security misconfigurations and vulnerabilities.

Two primary functions:

**Security posture assessment** — Defender for Cloud evaluates your resources against security best practices and provides a Secure Score — a percentage indicating how well your environment follows security recommendations. The higher the score, the lower your risk exposure.

**Workload protection** — Extended protection plans for specific resource types: VMs, SQL databases, storage accounts, Kubernetes, Key Vault, and more. These plans provide advanced threat detection and alerts.

Key features:

- Security recommendations with step-by-step remediation guidance
- Secure Score with improvement recommendations
- Security alerts for detected threats
- Regulatory compliance view (shows compliance against frameworks like PCI DSS, ISO 27001, SOC 2)
- Integration with Microsoft Sentinel (SIEM) for security event correlation

[SHOW AZURE PORTAL] Navigate to Microsoft Defender for Cloud > Overview. Show the Secure Score. Show the Recommendations list. Show the regulatory compliance view. Point out the workload protections available for different resource types.

---

## Section 8: Azure Key Vault (19:30–21:30)

### What Is Azure Key Vault?

Azure Key Vault is a managed service for storing and controlling access to secrets, encryption keys, and certificates. It keeps sensitive information out of application code and configuration files.

Three types of objects stored in Key Vault:

**Secrets** — Passwords, connection strings, API keys, and any sensitive string value. Applications retrieve secrets via API call rather than embedding them in code.

**Keys** — Cryptographic keys used for encryption and decryption. Key Vault can store and use keys for Azure Storage encryption, Azure SQL Transparent Data Encryption, and custom application encryption operations.

**Certificates** — TLS/SSL certificates for HTTPS endpoints. Key Vault can auto-renew certificates from public certificate authorities.

Key Vault benefits:

- Secrets are never in application code or config files
- Access is controlled via Azure RBAC and Key Vault access policies
- All access to secrets is logged in Azure Monitor
- Hardware Security Module (HSM) backed storage available for keys requiring the highest security level

Example workflow: An App Service reads its database connection string from Key Vault at startup using a managed identity — no password is ever stored in the application.

---

## Closing (21:30–22:30)

Today we covered the full Azure identity, security, and governance stack. Microsoft Entra ID is the cloud identity foundation. MFA and Conditional Access add authentication security. RBAC enforces least-privilege access to Azure resources. Azure Policy governs what can be created and how it must be configured. Management Groups organize subscriptions into a governance hierarchy. Defender for Cloud monitors security posture and provides threat protection. Key Vault keeps secrets, keys, and certificates secure and out of application code.

These services work together to form a defense-in-depth security strategy in Azure. In your lab this week, you will explore RBAC assignments and create an Azure Key Vault secret. In Module 12, we cover Azure monitoring and cost management. Take care.

---

*End of Script — Module 11*
