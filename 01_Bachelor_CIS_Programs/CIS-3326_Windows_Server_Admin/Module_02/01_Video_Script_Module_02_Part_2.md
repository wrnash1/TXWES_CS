# Video Script: Module 02 - Active Directory Domain Services Overview (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 02 - Active Directory Domain Services (AD DS) Overview

**Part:** 2 of 2 — Demonstrations, PowerShell Commands, Exam Tips, and Lab Preview

**Estimated Duration:** 11 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Recap and Demo Overview]

Welcome back to Module 02. In Part 1 we covered the AD DS logical hierarchy, Domain Controllers, FSMO roles, the Global Catalog, Kerberos, and trusts. In Part 2 I am going to demonstrate these concepts using Active Directory Users and Computers, explore the default OU structure created during domain promotion, and show you how to query FSMO role holders with PowerShell. I will close with exam tips and a lab preview.

---

### [SEGMENT 2 — Demo: Active Directory Users and Computers]

**[SHOW SCREEN: Server Manager — Tools menu — Active Directory Users and Computers]**

[Alt-text: Server Manager with the Tools dropdown menu open showing Active Directory Users and Computers selected.]

From Server Manager, click Tools in the top-right menu and select Active Directory Users and Computers. This is the primary GUI tool for managing objects within a domain — users, groups, computers, and OUs.

**[SHOW SCREEN: ADUC main window showing the domain tree in the left panel]**

[Alt-text: Active Directory Users and Computers window showing the domain corp.local expanded in the left panel with default containers Builtin, Computers, Domain Controllers, ForeignSecurityPrincipals, and Users visible.]

The left panel shows your domain in a tree view. Notice the default containers that exist immediately after domain promotion:

- **Builtin** — contains built-in local groups like Administrators and Users
- **Computers** — the default container where new computer accounts land when joining the domain without specifying an OU
- **Domain Controllers** — the OU (not a container) where Domain Controller computer accounts are placed automatically
- **ForeignSecurityPrincipals** — holds references to security principals from trusted external domains
- **Users** — the default container for user accounts and some default security groups

Notice that Domain Controllers is an OU, while Builtin, Computers, and Users are containers. The distinction matters: you can link a Group Policy Object to an OU but not to a default container. If you want to apply Group Policy to computer accounts in the Computers container, you either move them to a real OU or use Block Inheritance workarounds. Best practice is always to place objects in descriptive OUs, not in default containers.

---

### [SEGMENT 3 — Demo: Creating an Organizational Unit]

**[SHOW SCREEN: ADUC — right-click on domain name — New — Organizational Unit]**

[Alt-text: ADUC with the domain name corp.local right-clicked showing a context menu with New highlighted and Organizational Unit in the submenu.]

To create a new OU, right-click the domain name — or a parent OU — choose New, and then Organizational Unit. I will type `Departments` as the name. Leave "Protect container from accidental deletion" checked — this prevents an administrator from deleting the entire OU hierarchy with a single click.

Click OK. The Departments OU appears in the tree.

**[SHOW SCREEN: ADUC — right-click Departments OU — New — Organizational Unit — name it "HR"]**

[Alt-text: ADUC showing the Departments OU with a context menu creating a nested OU named HR.]

Now I will right-click Departments and create a child OU named `HR`. And another named `IT`. And another named `Finance`.

Now I have a structure: `corp.local > Departments > HR`, `Departments > IT`, `Departments > Finance`. Each of these OUs can have its own Group Policy Objects linked to it and can have administrative access delegated independently.

---

### [SEGMENT 4 — Demo: Querying FSMO Roles with PowerShell]

**[SHOW SCREEN: PowerShell console on the Domain Controller]**

[Alt-text: A PowerShell console on the Domain Controller showing the Get-ADDomain command and its output.]

Let us move to PowerShell to query our domain and find FSMO role holders.

```powershell
# Query domain information
Get-ADDomain
```

This returns a wealth of information: the domain name, forest name, domain functional level, domain SID, the PDC Emulator, RID Master, and Infrastructure Master role holders.

```powershell
# Query forest information
Get-ADForest
```

This shows forest-level information including the Schema Master and Domain Naming Master role holders.

```powershell
# Query all five FSMO roles in one command
netdom query fsmo
```

The `netdom query fsmo` command is a legacy tool but remains valid and is commonly used in the field and on exams. It lists all five FSMO role holders by server name.

**[SHOW SCREEN: Output of netdom query fsmo showing all five roles held by DC1.corp.local]**

[Alt-text: PowerShell console showing netdom query fsmo output listing Schema Master, Domain Naming Master, PDC, RID Master, and Infrastructure Master all assigned to DC1.corp.local.]

In a single-DC lab environment, all five roles are on the same DC. In production with multiple DCs, best practice is to distribute roles: keep the PDC Emulator and RID Master together on the same well-connected DC, keep the Schema Master and Domain Naming Master on a secure, rarely accessed DC, and place the Infrastructure Master on a DC that is not a Global Catalog server (in a multi-domain forest).

---

### [SEGMENT 5 — Demo: Exploring the AD DS Database]

**[SHOW SCREEN: PowerShell showing NTDS.dit file location and Active Directory Administrative Center]**

[Alt-text: PowerShell showing the directory listing of C:\Windows\NTDS showing NTDS.dit and related log files.]

```powershell
# View the NTDS directory
Get-ChildItem -Path "C:\Windows\NTDS"
```

The NTDS folder contains `NTDS.dit` — the AD DS database file — and its transaction log files (`.log`). The database is shared with all DCs through replication, not by sharing the file directly.

```powershell
# View domain controllers in the domain
Get-ADDomainController -Filter *
```

This lists all Domain Controllers and their properties including site, roles, IP address, and whether they are Global Catalog servers.

```powershell
# Check Global Catalog designation
Get-ADDomainController -Filter { IsGlobalCatalog -eq $true }
```

In a single-domain environment, all DCs are typically also Global Catalog servers. In a multi-domain environment, you designate specific DCs as GC servers based on site topology.

---

### [SEGMENT 6 — Demo: Active Directory Administrative Center]

**[SHOW SCREEN: Active Directory Administrative Center launched from Server Manager Tools]**

[Alt-text: Active Directory Administrative Center main window showing the navigation panel on the left with the domain listed and the overview panel on the right.]

Active Directory Administrative Center, or ADAC, is the newer GUI tool introduced in Windows Server 2008 R2. It is built on PowerShell under the hood — every action you take in ADAC generates equivalent PowerShell cmdlets, which you can view in the Windows PowerShell History pane at the bottom.

This is a powerful learning tool. If you do not know the PowerShell syntax for an operation, perform it in ADAC and then copy the generated cmdlet from the history pane.

ADAC also provides the Active Directory Recycle Bin management interface — we will cover that in Module 13. For now, note that it is the preferred GUI for advanced AD tasks while ADUC remains common for day-to-day user and computer account management.

---

### [SEGMENT 7 — Exam Tips]

**[SHOW SCREEN: Slide listing exam tips for Module 02]**

Six exam tips for AD DS architecture topics.

**Exam Tip 1:** The PDC Emulator is the most tested FSMO role. When a scenario describes password change failures, account lockout inconsistencies, or time synchronization errors, the PDC Emulator is the answer.

**Exam Tip 2:** OUs are not security boundaries. If a question says "create a security boundary between two departments," the answer involves domains or forests — not OUs.

**Exam Tip 3:** The Infrastructure Master restriction — not on a GC server — only applies in multi-domain forests. In a single-domain forest, the restriction does not apply because all DCs are GC servers and all objects are local.

**Exam Tip 4:** A forest trust is transitive across the entire forest on each side. An external trust is non-transitive and connects one specific domain to another. Shortcut trusts are manual optimizations for authentication speed.

**Exam Tip 5:** The Global Catalog is required for Universal Group membership lookups at logon. If a GC is unavailable and Universal Groups are in use, users may experience logon failures or delays.

**Exam Tip 6:** Read-Only Domain Controllers are for locations with limited physical security. They cache a subset of passwords defined by the Password Replication Policy. If an RODC is compromised, only cached credentials are exposed — not the entire domain.

---

### [SEGMENT 8 — Lab Preview]

**[SHOW SCREEN: Lab 02 instructions document]**

This week's lab builds on the server you deployed in Module 01. You will install the AD DS role using PowerShell, promote the server to a Domain Controller for a new forest named `corp.local`, and then explore the resulting AD structure using ADUC and PowerShell cmdlets.

The key deliverables are a screenshot of `Get-ADDomain` output confirming your domain is running, and a screenshot of `netdom query fsmo` showing the five FSMO role holders.

Keep this VM — we will continue using it in Module 03 when we add a second DC and configure AD DS replication.

---

### [SEGMENT 9 — Module 02 Summary]

**[SHOW SCREEN: Summary slide]**

Module 02 covered the conceptual foundation of AD DS. The four-level logical hierarchy — Forest, Tree, Domain, OU — organizes every object in your directory. Domain Controllers host and replicate the AD database. The five FSMO roles prevent multi-master conflicts for schema changes, domain naming, time synchronization, SID allocation, and cross-domain object references. The Global Catalog enables cross-domain searches and universal group membership lookups. Kerberos provides ticket-based authentication, and trust relationships enable cross-domain resource access.

In Module 03, we will move from theory to implementation — installing AD DS, promoting a server, and configuring a multi-DC environment. See you there.

---

### Additional Resources

- [Deploy a new Windows Server Active Directory forest](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-)
- [Active Directory Users and Computers overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731866(v=ws.11))
- [FSMO roles in Active Directory](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/fsmo-roles)
- [Read-Only Domain Controllers](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/rodc/read-only-domain-controller-updates)

---

*End of Part 2. Proceed to the Reading Guide, Lab, Quiz, and Discussion for Module 02.*
