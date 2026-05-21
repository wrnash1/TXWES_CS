# Reading Guide: Module 08 - Microsoft Entra ID (Azure AD) Basics

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 08 - Microsoft Entra ID (Azure AD) Basics**! This module covers Azure's identity and access management platform as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Microsoft Entra ID (formerly Azure Active Directory) is the cloud-based identity provider that controls authentication and authorization for Azure, Microsoft 365, and third-party applications.

You will learn the structure of an Entra ID tenant, how users and groups are managed, and how hybrid identity scenarios connect on-premises Active Directory to the cloud using Entra Connect. AZ-900 tests your ability to distinguish Entra ID from on-premises Active Directory and understand its role in the shared responsibility model. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Microsoft Entra ID Directory Structure**: The cloud-based directory service that stores and manages identities (users, groups, service principals, and devices). Each organization gets a dedicated Entra ID tenant. Entra ID is not the same as on-premises Windows Server Active Directory — it uses modern protocols (OAuth 2.0, OpenID Connect, SAML) rather than Kerberos and LDAP.

* **Tenant**: A dedicated, isolated instance of Microsoft Entra ID that an organization receives when it signs up for a Microsoft cloud service. A tenant represents the organization's identity boundary. Each tenant has a unique tenant ID (GUID) and a default domain name (e.g., contoso.onmicrosoft.com).

* **Users**: Identity objects in Entra ID representing individuals who can authenticate to cloud services. Users can be cloud-only (created directly in Entra ID) or synced from on-premises Active Directory via Entra Connect. Each user account includes profile information, authentication credentials, and group memberships.

* **Groups**: Collections of user accounts used to manage access to resources at scale. Assigning permissions to a group grants those permissions to all group members, simplifying access management. Entra ID supports Security Groups (for access control) and Microsoft 365 Groups (for collaboration).

* **Hybrid Identity**: A configuration where on-premises Active Directory identities are synchronized to Microsoft Entra ID, allowing users to use a single identity for both on-premises resources and cloud services. This is the most common enterprise deployment model.

* **Azure AD Connect (Entra Connect)**: The Microsoft tool that synchronizes on-premises Active Directory identities to Microsoft Entra ID, enabling hybrid identity. It supports password hash synchronization, pass-through authentication, and federation. Entra Connect is required for any hybrid identity scenario tested on AZ-900.

---

### 2. Certification Exam Tips

* **Entra ID is not on-premises AD**: AZ-900 tests whether you know the difference. On-premises AD uses Kerberos/LDAP. Entra ID uses OAuth/OpenID Connect/SAML. Entra ID does not replace on-premises AD — it works alongside it in hybrid scenarios.
* **Entra ID is PaaS/SaaS**: Microsoft manages the Entra ID service infrastructure. Customers manage their users, groups, and policies. This fits the PaaS/SaaS shared responsibility model.
* **Tenant Isolation**: Each organization's Entra ID tenant is isolated from other tenants. A user in contoso.onmicrosoft.com cannot automatically access fabrikam.onmicrosoft.com — cross-tenant access requires explicit configuration (guest access or B2B).
* **AZ-900 Entra ID Tiers**: Entra ID has Free, P1, and P2 license tiers. The Free tier includes basic user/group management and SSO. P1 adds Conditional Access. P2 adds Privileged Identity Management (PIM) and Identity Protection. AZ-900 may ask which tier enables Conditional Access — the answer is P1 or above.
* **Study Resource**: The Microsoft Learn identity module covers Entra ID concepts with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Microsoft Entra ID including tenant structure, users, groups, and hybrid identity with knowledge checks. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* **Required Video:** This free freeCodeCamp course covers Microsoft Entra ID for AZ-900 — watch the identity and security section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Add a new user to a Microsoft Entra tenant**: Using the Azure portal, create a new cloud-only user account. Observe the required fields (username, display name, password) and the auto-generated user principal name (UPN) in the tenant domain.
* **Create a security group and assign members**: Create a Security Group, add the new user as a member, and observe how group membership enables centralized access management without individual user assignments.
* **Configure basic tenant settings**: Review the tenant's custom domain names, primary contact information, and usage location settings. Understand why usage location must be set before assigning Microsoft 365 licenses.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Microsoft Entra ID unit in [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* [ ] Watch the identity section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for user creation, group management, and tenant settings.
* [ ] Proceed to the weekly hands-on lab activity.
