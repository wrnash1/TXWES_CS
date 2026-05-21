# Quiz: Module 08 - Microsoft Entra ID (Azure AD) Basics

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What is the primary function of Microsoft Entra ID?

* A) Network routing and DNS
* B) Identity and Access Management
* C) Database storage
* D) Host virtualization
* **Correct Answer:** B) Entra ID (formerly Azure Active Directory) handles authentication and access management for cloud identities.
* **Distractor Analysis:**
  * *Why correct:* Entra ID is Microsoft's cloud-based identity provider — it authenticates users and controls access to Azure, Microsoft 365, and third-party applications.
  * *Why A/C/D are incorrect:* Entra ID is not a network routing, database, or virtualization service.

---

**Question 2**
Which of the following most accurately describes **groups** in Microsoft Entra ID?

* A) Collections of user accounts used to manage access to Azure resources at scale — assigning permissions to a group grants those permissions to all members, simplifying administration compared to per-user assignments.
* B) Isolated directory instances that represent separate organizations, each with its own tenant ID and domain name.
* C) Authentication tokens issued to users after successful sign-in, containing claims about the user's identity and permissions.
* D) Physical server clusters that host the Microsoft Entra ID directory service within a specific Azure region.
* **Correct Answer:** A) Groups are collections of users that enable centralized access management — permissions assigned to the group apply to all members.
* **Distractor Analysis:**
  * *Why A is correct:* Groups are the standard mechanism for scaling access management in Entra ID rather than assigning permissions to individual users.
  * *Why B is incorrect:* That describes an Entra ID Tenant, not a group.
  * *Why C is incorrect:* That describes an access token or JWT claim — not a group object.
  * *Why D is incorrect:* Microsoft Entra ID is a cloud service; customers do not manage or see the physical server infrastructure.

---

**Question 3**
A company has on-premises Windows Server Active Directory and wants employees to use the same username and password for both on-premises resources and Microsoft 365 in the cloud. Which tool enables this hybrid identity scenario?

* A) Azure Active Directory Domain Services (AADDS)
* B) Microsoft Entra Connect (Azure AD Connect)
* C) Azure Virtual Network DNS
* D) Microsoft Entra External Identities (B2C)
* **Correct Answer:** B) Microsoft Entra Connect synchronizes on-premises Active Directory identities to Entra ID, enabling a single identity for both on-premises and cloud services.
* **Distractor Analysis:**
  * *Why B is correct:* Entra Connect (formerly Azure AD Connect) is the specific tool for directory synchronization between on-premises AD and Entra ID.
  * *Why A is incorrect:* Azure AD Domain Services provides managed domain services in the cloud (Kerberos, LDAP) but is not the synchronization tool for hybrid identity.
  * *Why C is incorrect:* Azure Virtual Network DNS handles name resolution for Azure resources — it does not sync identities.
  * *Why D is incorrect:* External Identities (B2C) is for customer-facing applications with consumer account authentication — not for enterprise hybrid identity.

---

**Question 4**
Which Microsoft Entra ID license tier is required to use Conditional Access policies?

* A) Free tier — included with all Azure subscriptions
* B) Microsoft Entra ID P1 or P2
* C) Microsoft 365 E3 only
* D) Azure AD B2C consumer tier
* **Correct Answer:** B) Conditional Access is an Entra ID P1 feature and is included in Microsoft 365 plans that include Entra ID P1 or P2 licensing.
* **Distractor Analysis:**
  * *Why B is correct:* Conditional Access requires at minimum Entra ID P1 (or equivalent Microsoft 365 plans like E3/E5). The Free tier does not include Conditional Access.
  * *Why A is incorrect:* The Free tier provides basic user/group management and limited SSO but does not include Conditional Access.
  * *Why C is incorrect:* While M365 E3 does include Entra ID P1, Conditional Access is tied to the P1 license level, not exclusively to E3.
  * *Why D is incorrect:* Azure AD B2C is for external consumer identity — it has separate licensing and does not map to Conditional Access for employee identities.

---

**Question 5**
An external contractor needs temporary access to a company's Azure portal resources. The contractor has their own Microsoft account. Which Entra ID feature enables this without creating a full internal user account?

* A) Microsoft Entra ID P2 Privileged Identity Management
* B) Microsoft Entra B2B guest access
* C) Entra Connect password hash synchronization
* D) Azure AD Domain Services Kerberos delegation
* **Correct Answer:** B) Microsoft Entra B2B guest access allows external users with their own Microsoft or organizational accounts to be invited as guests with specific resource permissions.
* **Distractor Analysis:**
  * *Why B is correct:* B2B guest access lets you invite external identities using their existing accounts — no need to create or manage separate credentials in your tenant.
  * *Why A is incorrect:* PIM manages just-in-time elevation of privileged roles for existing internal users — it is not for external identity access.
  * *Why C is incorrect:* Password hash sync is for synchronizing on-premises AD users to Entra ID — it does not address external contractor access.
  * *Why D is incorrect:* Kerberos delegation is an on-premises authentication protocol — it does not apply to external contractor Azure portal access.
