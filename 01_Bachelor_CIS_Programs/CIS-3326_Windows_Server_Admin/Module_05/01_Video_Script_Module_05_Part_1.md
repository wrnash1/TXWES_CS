# Video Script: Module 05 - Group Policy Objects: Creation and Management (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 05 - Group Policy Objects (GPOs): Creation and Management

**Part:** 1 of 2 — Concepts, Theory, and Architecture

**Estimated Duration:** 14 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Introduction]

**[SHOW SCREEN: Course title slide — Module 05]**

Welcome to Module 05. I am Professor Nash. In Module 04 we created users, groups, and computer accounts. Now we need to manage those objects at scale — enforcing security settings, deploying software, configuring desktops, and restricting capabilities across thousands of machines. The mechanism for all of this in a Windows domain is Group Policy.

Group Policy is one of the most powerful and most frequently misconfigured tools in Windows administration. Getting it right requires understanding the processing order, the filtering mechanisms, the inheritance model, and the troubleshooting commands. All of these are heavily tested on the AZ-800 exam.

---

### [SEGMENT 2 — What a GPO Is]

**[SHOW SCREEN: Diagram showing a GPO composed of a GPC in AD and a GPT in SYSVOL]**

[Alt-text: A diagram showing a Group Policy Object split into two components: the Group Policy Container (GPC) stored in AD DS, and the Group Policy Template (GPT) folder stored in SYSVOL, with arrows showing both components are needed for GPO processing.]

A Group Policy Object, or GPO, is a collection of settings that can be applied to users and computers in a Windows domain. Every GPO consists of two components that must both be healthy for policy to apply.

The **Group Policy Container (GPC)** lives in Active Directory. It stores metadata about the GPO: its name, GUID, version number, and the settings that can be stored in AD.

The **Group Policy Template (GPT)** lives in SYSVOL, under `SYSVOL\sysvol\<domain>\Policies\{GUID}\`. This folder stores the actual policy settings in INF, ADM, ADMX, and REG.POL files, as well as scripts. The GPT is replicated between DCs using DFSR, just like the rest of SYSVOL.

When a client processes Group Policy, it reads the GPO from the DC's SYSVOL share — specifically the `\\<domain>\SYSVOL` path, which all DCs serve. If SYSVOL replication is broken, clients on different DCs get different policy results. This is why healthy SYSVOL replication is critical.

---

### [SEGMENT 3 — GPO Scope: Where GPOs Are Linked]

**[SHOW SCREEN: Diagram showing GPOs linked to a site, domain, and OU]**

[Alt-text: A tree diagram showing GPO links at three levels: a GPO linked to a site (Site Policy), a GPO linked to the domain root (Domain Policy), and a GPO linked to the HR OU (HR OU Policy).]

GPOs are applied based on where they are linked in the AD hierarchy. A GPO can be linked to a **Site**, a **Domain**, or an **Organizational Unit (OU)**.

Site-linked GPOs apply to all computers in that Active Directory site, regardless of domain. They are used for network infrastructure settings that depend on physical location (like print queue mappings that differ by office).

Domain-linked GPOs apply to all users and computers in the domain. The default domain policy is linked here and typically contains password policy and account lockout settings.

OU-linked GPOs apply to users and computers within that specific OU and all nested child OUs unless Block Inheritance is configured. This is where most day-to-day configuration happens — HR OU gets HR policies, IT OU gets IT policies.

---

### [SEGMENT 4 — LSDOU Processing Order]

**[SHOW SCREEN: Inverted pyramid showing LSDOU order from top to bottom: Local, Site, Domain, OU]**

[Alt-text: An inverted pyramid diagram with four layers labeled from top to bottom: Local Policy, Site Policy, Domain Policy, and Organizational Unit Policy. An arrow on the side points downward labeled Processing Order and another upward labeled Precedence — Last Applied Wins.]

GPOs are applied in a specific order known by the acronym LSDOU: **Local**, **Site**, **Domain**, **OU**.

Each layer's settings override the previous layer when they configure the same setting — because the last policy applied wins. So OU-linked GPOs have the highest effective precedence in normal processing.

For nested OUs, policies are applied from the outermost OU to the innermost. A policy linked to `Departments` OU is applied before a policy linked to `Departments\HR`, so the HR OU policy wins when they conflict.

Within the same OU with multiple linked GPOs, the **Link Order** determines precedence. Lower link order number = higher precedence. If GPO A has link order 1 and GPO B has link order 2, GPO A is applied last (highest precedence) because policies with lower link order numbers are applied last.

---

### [SEGMENT 5 — Enforced and Block Inheritance]

**[SHOW SCREEN: GPMC showing Enforced flag on a GPO and Block Inheritance on an OU]**

[Alt-text: Group Policy Management Console showing a GPO with Enforced checked in its link properties, and an OU with Block Inheritance icon visible in the tree.]

Two special flags modify the normal LSDOU inheritance model.

**Enforced** (also called "No Override" in older documentation): Setting a GPO link to Enforced means that the settings in that GPO cannot be overridden by GPOs linked lower in the hierarchy. Even if a child OU has conflicting settings, the Enforced GPO wins. This is used for security baselines and compliance settings that must apply everywhere.

**Block Inheritance:** Applying this to an OU prevents GPOs linked above it (at the site or domain level) from flowing into it. Only locally-linked GPOs and Enforced GPOs at higher levels take effect. Block Inheritance is useful for test OUs or OUs that need isolation from domain-level policies.

Critical rule: **Enforced always beats Block Inheritance**. If a domain-level GPO is set to Enforced and an OU has Block Inheritance, the Enforced GPO still applies to the OU. Enforced cannot be blocked.

---

### [SEGMENT 6 — Computer Configuration vs. User Configuration]

**[SHOW SCREEN: GPME showing Computer Configuration and User Configuration tree nodes]**

[Alt-text: Group Policy Management Editor with the left tree showing Computer Configuration and User Configuration as top-level nodes, each with sub-nodes for Policies and Preferences.]

Every GPO has two sections.

**Computer Configuration** settings are applied when the computer starts, before any user logs in. They apply to the computer object regardless of which user logs in. If you want to configure screensaver lock times, disable USB storage, or deploy software to all machines in an OU — use Computer Configuration.

**User Configuration** settings are applied when a user logs in, based on where the user's account lives in AD (not where the computer is). If you want to redirect My Documents, configure Internet Explorer proxy settings, or restrict access to Control Panel — use User Configuration.

This distinction matters enormously for troubleshooting. If a user-based setting is not applying as expected on a specific computer, check whether the user's account OU has the right GPO linked to it. Computer-based settings not applying means checking the computer's OU.

---

### [SEGMENT 7 — Security Filtering]

**[SHOW SCREEN: GPMC Scope tab showing Security Filtering section with Authenticated Users]**

[Alt-text: GPMC Scope tab showing the Security Filtering section with Authenticated Users as the default entry, and an Add and Remove button below it.]

By default, every new GPO has "Authenticated Users" in its Security Filtering list. This means any authenticated user or computer that falls within the GPO's linked scope will receive the policy.

Security Filtering allows you to narrow this down. If you want a GPO to apply only to members of the `G_ITAdmins` group:

1. Remove "Authenticated Users" from Security Filtering
2. Add the `G_ITAdmins` group
3. The GPO now only applies to IT Admin group members, even if other users are in the same OU

Important caveat: Removing "Authenticated Users" without adding the computer account or "Domain Computers" group will cause Computer Configuration settings to stop applying, because the computer needs Read permission to even process the GPO. Always ensure computers retain at least Read permission when modifying Security Filtering.

The recommended approach for user-targeted filtering: keep "Authenticated Users" with Read-only permission, and add a Deny "Apply Group Policy" ACE for the group you want to exclude. This ensures computers can still read the GPO while specific user groups are excluded from applying settings.

---

### [SEGMENT 8 — WMI Filters]

**[SHOW SCREEN: GPO properties showing WMI Filter section with a Windows 11 query example]**

[Alt-text: GPO properties window showing the WMI Filter section with a custom WMI filter attached, and the filter query text visible showing a Win32_OperatingSystem query for a specific OS version.]

WMI Filters attach a WMI query to a GPO. When the GPO is evaluated at a client, the WMI query runs. If it returns TRUE, the GPO applies. If it returns FALSE, the GPO is skipped.

A common WMI filter example — apply only to Windows 11 machines:

```text
SELECT * FROM Win32_OperatingSystem
WHERE Caption LIKE "%Windows 11%"
```

And for Windows Server 2022 only:

```text
SELECT * FROM Win32_OperatingSystem
WHERE Caption LIKE "%Windows Server 2022%"
```

WMI Filters are evaluated per machine at policy processing time. They are dynamic — if a computer is upgraded, the filter result changes automatically without any AD changes. This makes WMI Filters more maintainable than creating separate OUs for different OS versions.

WMI Filter evaluation does add a small processing overhead at Group Policy refresh. In very large environments, keep WMI queries efficient.

---

### [SEGMENT 9 — Loopback Processing]

**[SHOW SCREEN: GPME showing the Loopback Processing setting under Computer Configuration]**

[Alt-text: Group Policy Management Editor showing Computer Configuration > Administrative Templates > System > Group Policy > Configure user Group Policy loopback processing mode, with options Merge and Replace visible.]

Loopback Processing solves a specific problem: what do you do when the same User Configuration settings should apply to all users who log into computers in a specific OU, regardless of where those users live in AD?

Scenario: A hospital has a Kiosk OU for shared workstations. Every user who logs into these kiosks should get a locked-down desktop — no task manager, no run dialog, specific screensaver timeout. But the user accounts live in department OUs that have normal User Configuration policies.

Without Loopback: the user's department OU policy applies. The kiosk environment is not enforced.

With Loopback in Replace mode: the computer's OU GPO User Configuration settings replace whatever user OU settings the user would normally get. All users on kiosk machines get the kiosk user settings.

With Loopback in Merge mode: both the user's own OU policies and the computer's OU user policies apply. In conflicts, the computer's OU policy wins. Useful when users need their own settings plus the machine's settings.

Loopback is configured under: Computer Configuration > Administrative Templates > System > Group Policy > Configure user Group Policy Loopback Processing Mode.

---

### [SEGMENT 10 — Summary and Part 2 Preview]

**[SHOW SCREEN: Summary slide]**

To summarize Part 1: GPOs consist of a GPC in AD and a GPT in SYSVOL. They are linked to sites, domains, and OUs. LSDOU processing order means OU policies win in normal processing. Enforced overrides lower OUs; Block Inheritance blocks higher OUs; Enforced beats Block Inheritance. Computer vs. User Configuration determines when and to whom settings apply. Security Filtering targets GPOs to specific groups. WMI Filters target GPOs to machines meeting a query condition. Loopback Processing applies computer-OU user settings to all users logging into those machines.

In Part 2, we will demonstrate GPO creation, linking, Security Filtering, and troubleshooting with gpresult and gpupdate.

---

### Additional Resources

- [Group Policy overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11))
- [Group Policy Management Console](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc753298(v=ws.11))
- [gpresult command reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)
- [Loopback Processing](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/loopback-processing-of-group-policy)

---

*End of Part 1. Continue to Part 2 for demonstrations, PowerShell commands, exam tips, and lab preview.*
