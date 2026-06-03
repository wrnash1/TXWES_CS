# Reading Guide: Module 11 — Azure Identity, Security, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domains: Describe Azure Architecture and Services + Describe Azure management and governance

---

## Introduction

Identity, security, and governance are foundational to responsible cloud adoption. Azure's security services control who can authenticate (identity), what they can do (authorization), how resources are protected (security posture), and what configurations are enforced across the organization (governance). This module covers the most heavily tested AZ-900 security topics: Microsoft Entra ID, MFA, Conditional Access, RBAC, Azure Policy, Management Groups, Defender for Cloud, and Key Vault.

---

## Section 1: Microsoft Entra ID (Azure Active Directory)

### 1.1 Overview

Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's cloud-based identity and access management (IAM) service. It serves as the identity backbone for Azure, Microsoft 365, and thousands of third-party SaaS applications.

### 1.2 Entra ID vs. Windows Server Active Directory

| Feature | Microsoft Entra ID | Windows Server Active Directory |
|---|---|---|
| Deployment | Cloud-based (SaaS) | On-premises server |
| Primary protocols | OAuth 2.0, OpenID Connect, SAML | Kerberos, NTLM, LDAP |
| Organizational unit | Tenant | Domain / Forest |
| Computer management | Via Microsoft Intune (MDM) | Group Policy (GPO) |
| Use case | Cloud apps, SaaS, Azure | On-premises corporate resources |
| Federation | Supports B2B and B2C | Forest trusts |

For AZ-900: Entra ID is NOT just a cloud version of Windows Server AD. They are different products serving different purposes but can be synchronized via Microsoft Entra Connect.

### 1.3 Core Concepts

| Concept | Description |
|---|---|
| Tenant | An organization's dedicated instance of Entra ID; created when subscribing to Azure or M365 |
| User | An identity representing a person; authenticated by Entra ID |
| Group | A collection of users; permissions can be assigned to groups |
| Application Registration | Registers an app with Entra ID for authentication |
| Service Principal | Application identity in a tenant |
| Managed Identity | Azure-managed service principal for Azure resources (no credential management) |

### 1.4 Entra ID License Tiers

| Tier | Key Features | Included With |
|---|---|---|
| Free | User/group management, SSO, basic security reports | Azure subscription |
| Microsoft 365 Apps | Same as Free + some additional features | Microsoft 365 Business subscriptions |
| P1 | + Conditional Access, self-service password reset, hybrid identity | Microsoft 365 E3 or standalone |
| P2 | + Identity Protection (risk-based), Privileged Identity Management (PIM) | Microsoft 365 E5 or standalone |

### 1.5 Hybrid Identity

Organizations with both on-premises AD and Azure use Microsoft Entra Connect to synchronize on-premises user accounts to Entra ID. Users sign in with the same credentials on-premises and in the cloud (single sign-on across environments).

---

## Section 2: Multi-Factor Authentication

### 2.1 Authentication Factors

MFA requires two or more verification factors from different categories:

| Category | Examples |
|---|---|
| Something you know | Password, PIN, security question |
| Something you have | Phone (SMS/app), hardware token, smart card, FIDO2 key |
| Something you are | Fingerprint, facial recognition, retina scan |

MFA requires factors from at least two different categories.

### 2.2 MFA Methods in Entra ID

| Method | Description | Security Level |
|---|---|---|
| Microsoft Authenticator app (push) | Approve/deny push notification | High |
| Microsoft Authenticator (OTP) | 6-digit time-based one-time code | High |
| FIDO2 security key | Physical hardware key (YubiKey, etc.) | Highest |
| SMS text code | One-time code via SMS | Medium (SIM swap risk) |
| Voice call | Automated phone call for approval | Medium |
| Windows Hello for Business | Biometric or PIN tied to device | High |

### 2.3 Security Defaults

Security Defaults is a free set of security configurations Microsoft provides to all Entra ID tenants:

- Requires MFA registration for all users
- Enforces MFA for administrators on every sign-in
- Blocks legacy authentication protocols (basic auth)
- Requires MFA when accessing the Azure Portal

Security Defaults are enabled by default on new tenants created after October 2019. Organizations that need custom control (specific exemptions, location-based rules) should disable Security Defaults and use Conditional Access Policies instead (requires P1).

---

## Section 3: Conditional Access

### 3.1 Overview

Conditional Access is an Entra ID P1 feature that evaluates access requests against a set of conditions and applies access controls. It implements the Zero Trust security model: verify explicitly, use least privilege, assume breach.

### 3.2 Policy Structure

A Conditional Access policy has three parts:

**When this happens (Assignments):**

- Users/groups targeted
- Cloud apps or actions
- Conditions: device platform, location, sign-in risk, client app

**Then do this (Access controls):**

- Grant (with or without MFA, device compliance, etc.)
- Block access
- Session control (token lifetime, continuous access evaluation)

### 3.3 Common Conditional Access Scenarios

| Scenario | Policy Configuration |
|---|---|
| Require MFA for Azure Portal access from outside corporate network | Target: Azure Portal app; Condition: IP location not in corporate range; Grant: Require MFA |
| Block access from high-risk countries | Target: All apps; Condition: Named location = blocked countries; Grant: Block |
| Require compliant device for email access | Target: Exchange Online; Condition: Any; Grant: Require compliant device |
| Allow legacy apps from corporate network only | Target: Exchange ActiveSync clients; Condition: Location = corporate network; Block all others |

### 3.4 Named Locations

Named locations are labeled IP ranges or countries used in Conditional Access conditions. Administrators define corporate network IP ranges as a named location to distinguish trusted on-site access from untrusted remote or foreign access.

---

## Section 4: Role-Based Access Control

### 4.1 RBAC Fundamentals

Azure RBAC is the authorization system for Azure resources. Every action on an Azure resource (create VM, read storage, delete database) is controlled by RBAC.

Three elements of every RBAC assignment:

| Element | Description |
|---|---|
| Security principal | Who: user, group, service principal, managed identity |
| Role definition | What: a named set of allowed operations (actions, notActions, dataActions) |
| Scope | Where: management group, subscription, resource group, or resource |

### 4.2 Scope Hierarchy and Inheritance

```
Management Group
  └── Subscription
        └── Resource Group
              └── Resource
```

RBAC assignments at a higher scope are inherited by all lower scopes. A Reader assignment at the Subscription scope gives read access to every resource group and every resource within that subscription.

### 4.3 Built-In Roles

| Role | Permissions | Cannot Do |
|---|---|---|
| Owner | Full control; manage access | — |
| Contributor | Create/manage resources | Manage access; assign roles |
| Reader | View resources | Any modification |
| User Access Administrator | Manage user access | Create/manage resources |

Resource-specific built-in roles (examples):

| Role | Target Resource |
|---|---|
| Virtual Machine Contributor | VMs — create/manage, but not networking or storage |
| Storage Blob Data Reader | Blob containers — read blob data |
| Key Vault Secrets Officer | Key Vault — manage secrets |
| SQL DB Contributor | SQL Databases — manage databases |
| Network Contributor | Virtual Networks, NSGs, Load Balancers |

### 4.4 Custom Roles

When built-in roles are too permissive or too restrictive, administrators can create custom roles by defining specific lists of allowed and denied actions. Custom roles are defined at the tenant scope and can be assigned at any scope.

### 4.5 Azure RBAC vs. Entra ID Roles

| System | Controls Access To | Example Roles |
|---|---|---|
| Azure RBAC | Azure resources (VMs, storage, databases) | Owner, Contributor, Reader |
| Entra ID roles | Directory objects (users, groups, apps, tenant settings) | Global Administrator, User Administrator |

A user can have Azure RBAC roles without Entra ID admin roles, and vice versa. They are completely separate role systems.

---

## Section 5: Azure Policy

### 5.1 Overview

Azure Policy evaluates Azure resource configurations against defined rules and enforces compliance. RBAC controls who can take actions; Policy controls what configurations are allowed.

### 5.2 Policy Effects

| Effect | Behavior |
|---|---|
| Deny | Block the operation if the resource violates the policy |
| Audit | Allow the operation but flag the resource as non-compliant |
| AuditIfNotExists | Audit resources that lack a related resource (e.g., VMs without monitoring agent) |
| DeployIfNotExists | Automatically deploy a required resource if it is missing |
| Modify | Automatically add/change/remove resource tags or properties |
| Append | Add additional settings to a resource during creation |

### 5.3 Policy Assignment Scope

Policies can be assigned at:

- Management Group (applies to all subscriptions in the group)
- Subscription (applies to all resource groups and resources in the subscription)
- Resource Group (applies to all resources in the group)

### 5.4 Policy Initiatives (Policy Sets)

An Initiative groups multiple related policies into a single assignment unit. Examples of built-in initiatives:

| Initiative Name | Purpose |
|---|---|
| Azure Security Benchmark | Comprehensive security best practices |
| NIST SP 800-53 Rev 5 | US government security standard compliance |
| CIS Microsoft Azure Foundations Benchmark | CIS security recommendations |
| HIPAA/HITRUST | Healthcare data compliance |
| PCI DSS | Payment card industry compliance |

### 5.5 Azure Policy vs. Azure RBAC

| Feature | Azure Policy | Azure RBAC |
|---|---|---|
| Controls | Resource configurations | User actions |
| Question answered | "Can this configuration exist?" | "Can this user do this action?" |
| Default behavior | All configurations allowed unless denied | All actions denied unless explicitly allowed |
| Example | "Storage must use HTTPS" | "User can read storage accounts" |

---

## Section 6: Management Groups

### 6.1 Management Group Hierarchy

Management groups provide a container for organizing Azure subscriptions into a governance hierarchy.

Default hierarchy:

```
Tenant Root Group
  ├── Production Management Group
  │     ├── Prod Subscription A
  │     └── Prod Subscription B
  ├── Development Management Group
  │     └── Dev Subscription C
  └── IT Management Group
        └── Shared Services Subscription D
```

### 6.2 Key Properties

| Property | Detail |
|---|---|
| Max depth | 6 levels of management groups below Root |
| Max groups | 10,000 management groups per directory |
| Subscriptions | Each subscription belongs to exactly one management group |
| Inheritance | Policy and RBAC assignments cascade down to all child subscriptions, resource groups, and resources |
| Root management group | All subscriptions ultimately belong to the Tenant Root Group |

### 6.3 Benefits of Management Groups

- Apply Azure Policy once at the management group — all child subscriptions comply automatically
- Assign RBAC roles at the management group — all child resources inherit the assignment
- View compliance across all subscriptions in a management group
- Separate Dev/Test and Production workloads with different policy sets

---

## Section 7: Microsoft Defender for Cloud

### 7.1 Overview

Microsoft Defender for Cloud is a Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP) service. It continuously assesses your Azure, AWS, GCP, and on-premises resources for security risks.

### 7.2 Core Capabilities

| Capability | Description |
|---|---|
| Secure Score | Percentage indicating how closely your environment follows security recommendations (0–100%) |
| Security Recommendations | Prioritized list of specific improvements with remediation steps |
| Regulatory Compliance | Dashboard showing compliance against standards (PCI DSS, ISO 27001, NIST, SOC 2) |
| Security Alerts | Real-time threat detection alerts for anomalous activity |
| Workload Protections | Enhanced plans for VMs, SQL, Storage, Kubernetes, Key Vault, etc. |
| Multi-cloud | Connects to AWS and GCP for unified security posture view |

### 7.3 Defender for Cloud Plans

| Plan Tier | Cost | Features |
|---|---|---|
| Free (CSPM) | Free | Secure Score, basic recommendations, limited policies |
| Defender for Cloud (enhanced) | Per resource/hour | Advanced threat detection, workload-specific protections, compliance dashboards |

### 7.4 Secure Score

The Secure Score is a single metric summarizing your current security posture. It is calculated by:

- Evaluating your resources against security controls
- Calculating what percentage of controls you have satisfied
- Weighted by the severity of each control

Higher Secure Score = Better security posture. A score above 70% is generally considered good.

---

## Section 8: Azure Key Vault

### 8.1 Overview

Azure Key Vault is a managed service for securely storing and controlling access to:

- **Secrets** — Passwords, connection strings, API keys, certificates
- **Keys** — Cryptographic keys for encryption operations
- **Certificates** — TLS/SSL certificates with auto-renewal capability

### 8.2 Key Vault Access Models

| Access Model | Description |
|---|---|
| Vault access policy | Legacy model; permissions set per principal per secret/key/certificate type |
| Azure RBAC | Recommended model; uses Azure RBAC roles for fine-grained data plane access |

Recommended Key Vault RBAC roles:

| Role | Permissions |
|---|---|
| Key Vault Administrator | Full management and data access |
| Key Vault Secrets Officer | Get, set, delete secrets; no keys or certificates |
| Key Vault Reader | Read metadata; no secret values |
| Key Vault Secrets User | Read secret values only |

### 8.3 Key Vault Benefits

| Benefit | Detail |
|---|---|
| Centralized secret management | All secrets in one place; no scattered config files |
| Access control | RBAC + access policies; every access is audited |
| Audit logging | Every read and write is logged in Azure Monitor |
| HSM-backed keys | Premium tier uses FIPS 140-2 Level 2/3 Hardware Security Modules |
| Soft delete | Deleted secrets/keys are recoverable within 7–90 days |
| Managed identities | Apps authenticate to Key Vault using managed identity — no passwords |

### 8.4 Key Vault Use Pattern

```
Application deployed on App Service
    │
    │ (authenticates via Managed Identity — no password needed)
    ▼
Azure Key Vault
    │
    │ (returns secret value at runtime)
    ▼
Secret: "Server=sql.database.windows.net;..."
    │
    ▼
Application uses secret to connect to Azure SQL Database
```

---

## Section 9: Identity and Security Service Summary

| Service | Controls | AZ-900 Signal Keywords |
|---|---|---|
| Microsoft Entra ID | Cloud identity; who can sign in | "Cloud identity," "SSO," "directory service," "user management" |
| MFA | Authentication strength | "Multi-factor," "second factor," "authenticator app," "prevent stolen passwords" |
| Conditional Access | Context-based access control | "MFA only from outside office," "block risky sign-ins," "require compliant device" |
| Azure RBAC | Authorization for Azure resources | "Who can manage VMs," "least privilege," "role assignment" |
| Azure Policy | Configuration governance | "Enforce standards," "require tags," "restrict regions," "compliance" |
| Management Groups | Subscription hierarchy and governance | "Organize subscriptions," "apply policy across all subs," "hierarchy" |
| Defender for Cloud | Security posture + threat detection | "Secure Score," "security recommendations," "cloud threat protection" |
| Azure Key Vault | Secret, key, and certificate management | "Store passwords safely," "no secrets in code," "encryption keys," "certificates" |

---

## Section 10: AZ-900 Exam Tips

1. **Entra ID vs. Windows Server AD:** Entra ID is cloud-based and uses OAuth/OIDC/SAML. Windows Server AD is on-premises and uses Kerberos/NTLM/LDAP. They are different products. Entra Connect synchronizes on-premises AD users to Entra ID.

2. **Conditional Access requires Entra ID P1.** Security Defaults are free but less granular. If a scenario describes nuanced access control (MFA only from outside the office), Conditional Access is the answer and requires P1.

3. **RBAC inheritance direction:** Permissions flow down the hierarchy. An assignment at Subscription level applies to all resource groups and resources within that subscription. An assignment at Resource Group level does not apply to other resource groups.

4. **RBAC vs. Entra ID roles:** Azure RBAC controls Azure resource access. Entra ID roles control directory operations. A Global Administrator in Entra ID does not automatically have Owner rights over Azure resources.

5. **Contributor cannot assign roles.** Only Owner and User Access Administrator can assign RBAC roles. If a scenario requires someone to manage resources AND grant access to others, the answer is Owner, not Contributor.

6. **Policy Deny vs. Audit:** Policy Deny blocks non-compliant resource creation. Policy Audit logs non-compliance but allows the action. If a scenario says "prevent," use Deny. If it says "monitor" or "flag," use Audit.

7. **Secure Score is not 100% = failure.** Secure Score represents progress toward best practices. Not every recommendation applies to every organization. Aim high but understand the context of each recommendation.

8. **Key Vault eliminates secrets in code.** The primary value proposition of Key Vault is removing secrets from application code and configuration files, replacing them with managed identity-authenticated API calls.

---

## Section 11: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the Entra ID license tier table (Section 1.4)
- [ ] Understand the Conditional Access policy structure (Section 3.2)
- [ ] Memorize the RBAC built-in roles and their permissions (Section 4.3)
- [ ] Understand the difference between Azure RBAC and Entra ID roles (Section 4.5)
- [ ] Memorize the Azure Policy effects table (Section 5.2)
- [ ] Understand the Management Group hierarchy and inheritance (Section 6.1 and 6.2)
- [ ] Understand what Defender for Cloud Secure Score represents (Section 7.4)
- [ ] Understand the three Key Vault object types and the use pattern (Section 8.1 and 8.4)
- [ ] Memorize the identity and security service summary table (Section 9)
- [ ] Complete the Microsoft Learn AZ-900 identity and governance modules
- [ ] Complete Lab Module 11
- [ ] Take Quiz Module 11
- [ ] Post Discussion Module 11 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## Required Reading Resources

- Microsoft Entra ID overview: learn.microsoft.com/en-us/entra/fundamentals/whatis
- Azure MFA overview: learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks
- Conditional Access overview: learn.microsoft.com/en-us/entra/identity/conditional-access/overview
- Azure RBAC overview: learn.microsoft.com/en-us/azure/role-based-access-control/overview
- Azure Policy overview: learn.microsoft.com/en-us/azure/governance/policy/overview
- Management Groups: learn.microsoft.com/en-us/azure/governance/management-groups/overview
- Microsoft Defender for Cloud: learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction
- Azure Key Vault: learn.microsoft.com/en-us/azure/key-vault/general/overview
