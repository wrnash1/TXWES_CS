# Reading Guide: Module 04 - User, Group, and Computer Accounts in AD

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 04 – User, Group, and Computer Accounts in Active Directory**! This week's study material covers how to create, manage, and organize the three core object types in AD DS: user accounts, security groups, and computer accounts. Managing these objects correctly is both an everyday administrative task and a core competency on the AZ-800 exam.

As a student, you will learn the difference between security groups and distribution groups, how group scope affects permission assignment across domains, and how to automate account management with PowerShell. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **User Account (AD)**: A directory object that represents a person or service and contains credentials (username/password hash), profile settings, and group memberships. User accounts are authenticated by Kerberos during logon and are the foundation of access control in a Windows domain.
* **Group Scope — Domain Local, Global, Universal**: Domain Local groups are used to assign permissions to resources within the same domain; they can contain members from any domain. Global groups contain members only from the same domain and are used to organize users by role. Universal groups can contain members from any domain in the forest and are used to assign permissions across domains — their membership is stored in the Global Catalog.
* **Security Group vs. Distribution Group**: Security groups are used to assign permissions to resources (NTFS, Share, etc.) and can also be used as email distribution lists. Distribution groups are mail-only and cannot be used to assign permissions.
* **Managed Service Account (MSA) / Group Managed Service Account (gMSA)**: Special account types for running Windows services. gMSAs automatically rotate their passwords and can be used across multiple servers, eliminating the need to manually manage service account passwords.
* **Computer Account**: A directory object representing a domain-joined machine. It has its own password (rotated automatically every 30 days by default) and is used to apply Computer Configuration GPO settings and enforce machine-level security policies.
* **New-ADUser / Get-ADUser**: Core Active Directory PowerShell cmdlets for creating and querying user accounts. Part of the RSAT ActiveDirectory module, these cmdlets are essential for bulk account creation and automation.

---

### 2. Certification Exam Tips

* **Group scope nesting (AGDLP)**: The recommended Microsoft best practice for assigning permissions is Accounts → Global groups → Domain Local groups → Permissions (AGDLP). AZ-800 scenario questions often describe a permission problem that is solved by correctly nesting groups in this order.
* **Universal groups and the Global Catalog**: Because universal group membership is cached in the Global Catalog, placing many user accounts directly in a universal group causes GC replication traffic every time membership changes. Best practice is to put global groups inside universal groups.
* **Stale computer accounts**: A computer account that has not contacted the DC in 30+ days may have a broken secure channel. Use `Test-ComputerSecureChannel` and `Reset-ComputerMachinePassword` to diagnose and repair this. This is a common AZ-800 troubleshooting scenario.
* **Microsoft Learn Reference**: Review account management documentation at [Microsoft Learn – Active Directory Accounts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/active-directory-domain-services-component-updates) and the [AD PowerShell module reference](https://learn.microsoft.com/en-us/powershell/module/activedirectory/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Review the user and group management documentation at [Microsoft Learn: Windows Server Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/how-to-configure-protected-accounts) and the AD PowerShell cmdlet reference at [Microsoft Learn: ActiveDirectory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/).
* **Required Video:** Watch the video lecture on **User, Group, and Computer Accounts** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will create user accounts and security groups using both Active Directory Users and Computers (ADUC) and PowerShell (`New-ADUser`, `New-ADGroup`, `Add-ADGroupMember`). You will also join a workstation to the domain and verify the resulting computer account object.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the user and group documentation at [Microsoft Learn: ActiveDirectory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/).
* [ ] Watch the video lecture on **User, Group, and Computer Accounts** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
