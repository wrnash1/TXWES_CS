# Video Script: Module 04 - User, Group, and Computer Accounts in AD (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 04 - User, Group, and Computer Accounts in AD

**Part:** 1 of 2 — Concepts, Theory, and Architecture

**Estimated Duration:** 13 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Introduction]

**[SHOW SCREEN: Course title slide — Module 04]**

Welcome to Module 04. I am Professor Nash. We have a functioning two-DC domain from the previous labs. Now we need to populate it with objects. The three foundational object types in Active Directory are user accounts, group accounts, and computer accounts. Understanding how to create and manage them — and especially how groups work — is one of the highest-tested areas on the AZ-800 exam.

This module covers user account properties and lifecycle, the four group scopes and two group types, the AGDLP nesting best practice, computer accounts and secure channel management, service accounts including Managed Service Accounts and Group Managed Service Accounts, and the PowerShell cmdlets for all of these operations.

---

### [SEGMENT 2 — User Accounts]

**[SHOW SCREEN: Active Directory Users and Computers — New User dialog]**

[Alt-text: The New User creation wizard in Active Directory Users and Computers showing fields for first name, last name, user logon name, and password options.]

A user account in Active Directory is the object that represents a person or service identity in the directory. Every user account has two key identifiers: the **User Logon Name** (UPN format: `jdoe@corp.local`) and the **SAM Account Name** (pre-Windows 2000 format: `CORP\jdoe`). Both can be used to log in.

The key account properties you must understand for the exam and for daily administration:

**Account expiration:** You can set a date after which the account automatically becomes disabled. Useful for contractors, temporary workers, or accounts tied to project durations.

**Password policy:** The account is subject to the domain's default password policy or, if configured, a Fine-Grained Password Policy that targets specific groups.

**Logon hours:** You can restrict which hours of the day and days of the week a user account can log in. Accounts outside of logon hours will have active sessions disconnected (configurable) and new logon attempts will be denied.

**Logon workstations:** You can restrict which specific workstations a user is allowed to log in from. Up to 10 workstations can be listed. A blank list means the user can log in from any workstation.

**Account is disabled vs. Account is locked out:** These are different states. A disabled account has been manually or policy-disabled. A locked-out account has exceeded the account lockout threshold from too many bad password attempts. Both prevent logon. Disabled accounts must be manually enabled. Locked-out accounts automatically unlock after the lockout duration or can be manually unlocked.

---

### [SEGMENT 3 — Group Types and Scopes]

**[SHOW SCREEN: Diagram showing two group types (Security and Distribution) and four group scopes (Local, Domain Local, Global, Universal)]**

[Alt-text: A matrix diagram with Group Types on the x-axis (Security and Distribution) and Group Scopes on the y-axis (Local Machine, Domain Local, Global, Universal), with icons showing typical membership and resource assignment patterns.]

Groups are the most nuanced topic in this module. There are two dimensions to every group: **type** and **scope**.

**Group Type** determines what the group is used for.

A **Security Group** is used to assign permissions to resources. You add users to a security group and then grant that group access to a file share, a printer, a GPO, or any other resource. Security groups can also be used as email distribution lists.

A **Distribution Group** is used only for email distribution lists (Microsoft Exchange/Outlook). Distribution groups cannot be used to assign permissions to resources. If someone asks you "should this group be security or distribution," the answer is almost always security — security groups are more flexible.

**Group Scope** determines membership rules and where the group can be used to assign permissions.

A **Domain Local Group** can contain members from any domain in the forest (or even from trusted forests), but it can only be used to assign permissions to resources within the domain where the group exists. Think of it as the "permission holder" that lives next to the resource.

A **Global Group** can only contain members from the same domain where the group was created. However, it can be used to assign permissions to resources in any domain in the forest. Think of it as the "role holder" that represents a job function.

A **Universal Group** can contain members from any domain and can be used to assign permissions in any domain. The catch: Universal Group membership is stored in the Global Catalog, so large Universal Groups with frequent membership changes can generate significant replication traffic. Use Universal Groups sparingly.

A **Local Group** (also called Machine Local) exists in the SAM database of a specific computer. It cannot be managed from a DC and only controls access to resources on that one machine. The built-in Administrators and Users groups on workstations are examples.

---

### [SEGMENT 4 — AGDLP Nesting Strategy]

**[SHOW SCREEN: Diagram showing AGDLP nesting — Account inside Global Group inside Domain Local Group with Permissions assigned to Domain Local Group]**

[Alt-text: A four-layer diagram showing: A (user Account) is a member of G (Global group), G is nested inside DL (Domain Local group), and P (Permissions) are assigned to the Domain Local group on the resource.]

AGDLP stands for **Accounts into Global groups into Domain Local groups, then assign Permissions**. This is the Microsoft-recommended best practice for organizing group membership and resource permissions.

Here is why it works so well. You create Global groups that represent job functions or roles — `G_Accountants`, `G_Managers`, `G_IT_Admins`. You place user accounts into these role-based Global groups. Then you create Domain Local groups that are named for the resource they control access to — `DL_FinanceDrive_Read`, `DL_FinanceDrive_Write`. You nest the role-based Global group into the appropriate Domain Local group. Finally, you assign permissions on the resource (file share, printer, etc.) to the Domain Local group.

The benefit: when a new person joins Accounting, you add them to the `G_Accountants` group. They automatically inherit access to every resource that `G_Accountants` has been nested into. When they leave Accounting, you remove them from one group and access is revoked everywhere simultaneously.

In a multi-domain forest, you extend this to **AGUDLP** — Account, Global group, Universal group, Domain Local group, Permissions — to enable cross-domain role assignment.

---

### [SEGMENT 5 — Computer Accounts]

**[SHOW SCREEN: ADUC showing a computer object in the Computers container and its properties]**

[Alt-text: Active Directory Users and Computers showing a computer object with its Distinguished Name, Operating System, and DNS Hostname properties visible.]

Every Windows computer that joins a domain gets a computer account in Active Directory. Computer accounts are security principals just like user accounts — they have a SID, can be members of groups, and are subject to Group Policy.

Computer accounts have a password too, even though users never see it. Every 30 days, a domain-joined computer automatically changes its machine account password with the Domain Controller. This password is stored locally and in AD. If these passwords get out of sync — which can happen if a computer is offline for more than 30 days — the machine account password becomes stale and domain logon fails with the error "trust relationship failed."

**Resetting a stale computer account secure channel** can be done two ways.

The disruptive way: remove the computer from the domain, reboot, and rejoin. This works but changes the computer's SID, which breaks local profile associations and group memberships.

The non-disruptive way: run `Test-ComputerSecureChannel -Repair` from an elevated PowerShell prompt on the affected machine while logged in with a local Administrator account. This resets the machine account password without rejoining.

```powershell
Test-ComputerSecureChannel -Repair -Credential (Get-Credential "CORP\Administrator")
```

---

### [SEGMENT 6 — Service Accounts]

**[SHOW SCREEN: Diagram comparing standard user service account vs. Managed Service Account vs. Group Managed Service Account]**

[Alt-text: Three-column comparison showing standard user service account with manual password rotation, MSA with automatic rotation on one server, and gMSA with automatic rotation on multiple servers.]

Services running on Windows — SQL Server, IIS application pools, scheduled tasks — often need to run under a domain account so they can access domain resources. The traditional approach is to create a standard user account, set a very long password, and set it to never expire. The problem: if the password ever does need to change, someone has to manually update every service that uses that account.

**Managed Service Accounts (MSAs)** solve this. An MSA is a special account type that automatically rotates its password every 30 days. No human manages the password — it is handled entirely by the OS and AD. The limitation: an MSA can only be used on one specific server. You install it on that server and it is bound to it.

```powershell
# Create an MSA
New-ADServiceAccount -Name "SVC_SQLAgent" -RestrictToSingleComputer

# Install the MSA on the target server
Install-ADServiceAccount -Identity "SVC_SQLAgent"
```

**Group Managed Service Accounts (gMSAs)** extend the MSA concept to multiple servers — perfect for load-balanced web farms or clustered services. Multiple servers can use the same gMSA. Password rotation is still automatic.

```powershell
# Require a KDS root key first (only needed once per forest)
Add-KdsRootKey -EffectiveImmediately

# Create a gMSA
New-ADServiceAccount -Name "SVC_WebApp" `
    -PrincipalsAllowedToRetrieveManagedPassword "WebServers_Group" `
    -DNSHostName "webapp.corp.local"
```

For the AZ-800 exam: MSA for single server, gMSA for multiple servers. Both rotate passwords automatically. Neither requires password management by an administrator.

---

### [SEGMENT 7 — User Account Lifecycle Management]

**[SHOW SCREEN: Diagram showing user lifecycle — Create, Modify, Disable, Archive, Delete]**

[Alt-text: A lifecycle flow diagram showing user account stages from Create through Active Employment through Disable on departure through Archive after retention period through Delete.]

A user account has a lifecycle in AD: creation on hire, modification as roles change, and eventual deprovisioning when the employee leaves.

Best practice for departing employees: **disable the account, do not delete it**. Deleting an account immediately removes the SID. Any resource that had permissions assigned to that SID loses the assignment. If the employee returns or if there is a dispute about their access history, a deleted account cannot be restored without AD Recycle Bin (which we cover in Module 13).

Disabling an account prevents logon, preserves all group memberships and permissions, and keeps the account available for reference or reactivation. After a defined retention period (typically 30-90 days), you can delete the account safely.

```powershell
# Disable an account
Disable-ADAccount -Identity "jdoe"

# Move to a Disabled Users OU to keep things organized
Move-ADObject -Identity "CN=John Doe,OU=HR,DC=corp,DC=local" `
    -TargetPath "OU=Disabled_Users,DC=corp,DC=local"
```

---

### [SEGMENT 8 — Summary and Part 2 Preview]

**[SHOW SCREEN: Summary slide]**

To summarize Part 1: user accounts have properties including account expiration, logon hours, and lockout state. Groups have two dimensions — type (security vs. distribution) and scope (domain local, global, universal). AGDLP is the best-practice nesting strategy. Computer accounts have machine passwords that can go stale after 30 days. Managed Service Accounts and Group Managed Service Accounts provide automatic password rotation for service identities.

In Part 2, we will demonstrate all of these concepts in ADUC and PowerShell, show the cmdlets for bulk operations, and walk through exam tips.

---

### Additional Resources

- [Active Directory user accounts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-user-accounts)
- [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)
- [Managed Service Accounts](https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview)
- [Computer accounts in AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/computer-accounts)

---

*End of Part 1. Continue to Part 2 for demonstrations, PowerShell commands, exam tips, and lab preview.*
