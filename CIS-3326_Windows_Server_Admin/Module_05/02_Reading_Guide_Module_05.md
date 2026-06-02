# Reading Guide: Module 05 - Group Policy Objects: Creation and Management

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 05 covers Group Policy — the primary mechanism for enforcing settings, security configurations, and software deployments across all domain-joined users and computers. GPO processing order, filtering, troubleshooting commands, and PowerShell management are all tested on the AZ-800 exam and are essential daily-administration skills.

---

### 1. GPO Architecture

#### 1.1 Components of a GPO

Every GPO has two components that must both function for policy to apply:

| Component | Location | Contains |
|---|---|---|
| Group Policy Container (GPC) | Active Directory (CN=Policies,CN=System,DC=...) | Metadata, GUID, version, settings stored in AD |
| Group Policy Template (GPT) | SYSVOL\sysvol\domain\Policies\{GUID}\ | INF, ADMX, REG.POL files, scripts |

The GPT is replicated between DCs using DFSR. If SYSVOL replication is broken, clients on different DCs may receive different or outdated policy settings.

#### 1.2 GPO Identification

Every GPO has a GUID (globally unique identifier) such as `{31B2F340-016D-11D2-945F-00C04FB984F9}`. The Default Domain Policy has a well-known GUID. GPO names are human-readable labels in GPMC; the underlying folder in SYSVOL uses the GUID.

---

### 2. GPO Linking and Scope

GPOs do not apply unless they are linked to a container.

| Link Target | Who It Applies To | Common Use |
|---|---|---|
| Site | All computers in the AD site (physical location) | Location-based settings |
| Domain | All users and computers in the domain | Password policy, auditing baseline |
| Organizational Unit | Users and computers in the OU and child OUs | Department-specific settings |

A GPO can be linked to multiple containers simultaneously. One link can be enabled/disabled independently without affecting other links. Multiple GPOs can be linked to the same container.

---

### 3. LSDOU Processing Order

#### 3.1 The Order

GPOs are applied in this order:

1. Local Policy (stored on the machine, not in AD)
2. Site-linked GPOs
3. Domain-linked GPOs
4. OU-linked GPOs (outermost OU first, innermost OU last)

**Last applied wins** for any conflicting setting. OU-linked GPOs have the highest default precedence.

#### 3.2 Example

```text
Domain GPO: Minimum Password Length = 12
HR OU GPO: Minimum Password Length = 15

Result for users in HR OU: Minimum Password Length = 15
Reason: HR OU GPO is applied after Domain GPO
```

#### 3.3 Multiple GPOs at the Same Level

When multiple GPOs are linked to the same OU, **Link Order** determines precedence. Lower link order number = applied last = higher precedence.

```text
OU: IT
  GPO A - Link Order 1 (processed last = wins)
  GPO B - Link Order 2 (processed first = loses to GPO A)
```

---

### 4. Enforced and Block Inheritance

#### 4.1 Enforced

Setting a GPO link to Enforced causes its settings to override anything configured by GPOs lower in the hierarchy. Even an OU-linked GPO cannot override an Enforced domain-level GPO.

Use cases: Security baselines, compliance requirements, audit settings that must apply to all objects regardless of local OU policy.

#### 4.2 Block Inheritance

Applied to an OU (not to a GPO), Block Inheritance prevents GPOs linked above the OU (at domain or site level) from flowing down to the OU. Only policies linked directly to the OU and Enforced policies from higher levels still apply.

Use cases: Test OUs, development environments that should not receive production policies.

#### 4.3 Enforced vs. Block Inheritance — The Priority Rule

Enforced always wins over Block Inheritance. An Enforced GPO at the domain level will still apply to an OU that has Block Inheritance set. This is intentional — it prevents OU administrators from circumventing domain-level security requirements.

| Scenario | Result |
|---|---|
| Domain GPO (normal) + OU Block Inheritance | Domain GPO blocked |
| Domain GPO (Enforced) + OU Block Inheritance | Domain GPO still applies |
| OU GPO (normal) + Domain GPO (normal) | OU GPO wins |
| OU GPO (normal) + Domain GPO (Enforced) | Domain GPO wins |

---

### 5. Computer Configuration vs. User Configuration

| Section | Applied When | Applied Based On | Examples |
|---|---|---|---|
| Computer Configuration | At machine startup | Computer's OU | Password policy, screensaver, software deployment |
| User Configuration | At user logon | User's OU | Drive mappings, printer connections, desktop restrictions |

If you configure a setting in Computer Configuration and it is not applying, check the computer account's OU for a linked GPO. If it is not applying for users, check the user account's OU.

---

### 6. Security Filtering

By default, the "Authenticated Users" group is in Security Filtering, meaning all authenticated domain objects receive the GPO if it is linked to their containing OU.

#### 6.1 Restricting GPO to a Specific Group

1. Remove "Authenticated Users" from Security Filtering
2. Add the specific security group
3. Add "Domain Computers" with Read (no Apply) to preserve Computer Configuration processing

#### 6.2 Excluding a Group

Use the Delegation tab to add a Deny "Apply Group Policy" ACE for the group to exclude. Keep "Authenticated Users" with Read permission. The Deny overrides Allow for members of the denied group.

#### 6.3 Security Filtering vs. Block Inheritance

Security Filtering is more granular — it targets specific users or computers within an OU without affecting other objects in the same OU. Block Inheritance affects the entire OU.

---

### 7. WMI Filters

WMI Filters attach a WMI (Windows Management Instrumentation) query to a GPO. At each policy refresh, the query runs on the client. If it returns TRUE, the GPO applies. If FALSE, the GPO is skipped.

#### 7.1 Common WMI Filter Examples

```text
Windows 11 only:
SELECT * FROM Win32_OperatingSystem
WHERE Caption LIKE "%Windows 11%"

Windows Server 2022 only:
SELECT * FROM Win32_OperatingSystem
WHERE Caption LIKE "%Windows Server 2022%"

64-bit OS only:
SELECT * FROM Win32_OperatingSystem
WHERE OSArchitecture = "64-bit"

More than 8 GB RAM:
SELECT * FROM Win32_ComputerSystem
WHERE TotalPhysicalMemory > 8589934592
```

#### 7.2 WMI Filter Properties

- One WMI Filter per GPO maximum (but one filter can have multiple conditions)
- Filters run in the WMI namespace `root\CIMv2`
- Filter evaluation failure (WMI error) causes the GPO to not apply
- Processing overhead: adds latency to GPO refresh on large environments

---

### 8. Loopback Processing

Loopback Processing makes User Configuration settings apply based on the computer's OU, not the user's OU.

| Mode | Behavior |
|---|---|
| Replace | Computer OU's User Configuration replaces the user OU's User Configuration entirely |
| Merge | Both sets apply; computer OU's User Configuration wins on conflicts |

Configure at: Computer Configuration > Administrative Templates > System > Group Policy > Configure user Group Policy loopback processing mode.

Use cases:

- Kiosk computers (Replace) — all users get the kiosk restricted desktop
- Public terminal rooms (Replace) — no personal settings carried over
- Lab computers (Merge) — students get both their own policies and lab restrictions

---

### 9. GPO Troubleshooting Commands

#### 9.1 gpresult

```cmd
# Quick text summary — current user and computer
gpresult /r

# HTML RSoP report
gpresult /h C:\GPReport.html

# For a specific user and computer
gpresult /user CORP\jdoe /r

# Run with verbose output
gpresult /v
```

Key sections in gpresult output:

- Applied Group Policy Objects — GPOs that applied successfully
- Denied GPOs — GPOs in scope that were not applied, with reason codes

Common reason codes:

| Reason Code | Meaning | Remediation |
|---|---|---|
| Inaccessible | Cannot read GPO — ACL or SYSVOL issue | Check Security Filtering; check SYSVOL replication |
| Disabled | GPO link is disabled | Enable the link in GPMC |
| Empty | No settings in the GPO | Configure at least one setting |
| Inaccessible WMI filter | WMI query returned FALSE or error | Verify WMI filter query syntax and namespace |

#### 9.2 gpupdate

```cmd
# Refresh both Computer and User Configuration immediately
gpupdate /force

# Refresh only Computer Configuration
gpupdate /target:computer /force

# Refresh only User Configuration
gpupdate /target:user /force
```

#### 9.3 PowerShell GPO Management

```powershell
# List all GPOs
Get-GPO -All | Select-Object DisplayName, GpoStatus, CreationTime

# Create a GPO
New-GPO -Name "NewPolicy" -Domain "corp.local"

# Link a GPO to an OU
New-GPLink -Name "NewPolicy" `
    -Target "OU=IT,OU=Departments,DC=corp,DC=local" `
    -LinkEnabled Yes

# Get full GPO report as HTML
Get-GPOReport -Name "NewPolicy" -ReportType HTML -Path "C:\Report.html"

# Remote GPO refresh — single computer
Invoke-GPUpdate -Computer "WS-IT-001" -Force

# Remote GPO refresh — all computers in an OU
Get-ADComputer -Filter * -SearchBase "OU=IT,OU=Departments,DC=corp,DC=local" |
    ForEach-Object { Invoke-GPUpdate -Computer $_.Name -Force }

# Get RSoP for specific user/computer
Get-GPResultantSetOfPolicy -Computer "WS-IT-001" `
    -User "CORP\dprince" -ReportType HTML -Path "C:\RSoP.html"
```

---

### 10. Default Domain Policies

Two GPOs are created automatically during domain promotion:

| GPO | Linked To | Purpose |
|---|---|---|
| Default Domain Policy | Domain | Password policy, account lockout policy, Kerberos settings |
| Default Domain Controllers Policy | Domain Controllers OU | Audit policy, user rights assignments for DCs |

Best practice: do not modify these default GPOs. Create new GPOs for additional settings. This preserves a clean default baseline for troubleshooting and allows roll-back by simply deleting the custom GPO.

---

### 11. GPO Architecture Reference Diagram

```text
DOMAIN: corp.local
  |
  +-- GPO: Default Domain Policy (linked to domain)
  |     Computer Config: Password Policy, Account Lockout, Kerberos
  |
  +-- GPO: CORP_Security_Baseline (linked to domain, ENFORCED)
  |     Computer Config: Audit settings, screensaver lock
  |
  +-- OU: Departments
  |     |
  |     +-- OU: IT
  |     |     +-- GPO: CORP_IT_Security_Baseline (Security Filtering: G_ITAdmins)
  |     |           Computer Config: 14-char passwords, screen lock
  |     |
  |     +-- OU: HR
  |           +-- GPO: CORP_HR_UserPolicy
  |                 User Config: Drive mappings, printer connections
  |
  +-- OU: Kiosks
        +-- GPO: CORP_Kiosk_Restrictions (Loopback: Replace)
              User Config: No task manager, no run dialog, 10-min screensaver
```

---

### 12. Exam Tips for Module 05

**Tip 1 — Last applied wins:** OU beats Domain beats Site beats Local in normal LSDOU order. If the same setting is in both a Domain GPO and an OU GPO, the OU setting applies — unless Enforced.

**Tip 2 — Enforced is absolute:** Enforced GPO wins over all lower OUs, even those with Block Inheritance. Enforced cannot be blocked.

**Tip 3 — gpresult reason codes:** "Inaccessible" = permission/ACL issue or SYSVOL problem. "Disabled" = link is off. "Empty" = no settings. "Inaccessible WMI filter" = WMI query failed.

**Tip 4 — Security Filtering vs. Delegation tab:** Filtering controls who receives the GPO. Delegation controls who has Read, Edit, or Manage permissions on the GPO object itself.

**Tip 5 — Computer Config needs computer Read rights:** When you remove Authenticated Users from Security Filtering, add "Domain Computers" with Read (not Apply) to preserve Computer Configuration processing.

**Tip 6 — Loopback Replace for kiosks:** Any scenario involving "apply the same User Configuration to all users logging into specific computers" is solved with Loopback Processing in Replace mode.

**Tip 7 — Invoke-GPUpdate:** The remote PowerShell equivalent of `gpupdate /force`. Know this cmdlet — it is the correct answer for remotely refreshing Group Policy on multiple machines.

**Tip 8 — Default GPO modification:** Best practice is to never modify the Default Domain Policy or Default Domain Controllers Policy. Create new GPOs for additional settings.

---

### 13. Key Terms Glossary

| Term | Definition |
|---|---|
| GPO | Group Policy Object — collection of settings applied to users and computers |
| GPC | Group Policy Container — AD portion of a GPO |
| GPT | Group Policy Template — SYSVOL folder portion of a GPO |
| LSDOU | Local, Site, Domain, OU — the GPO processing order |
| Enforced | GPO link property forcing settings to override lower-level OUs |
| Block Inheritance | OU property preventing higher-level GPOs from flowing in |
| Security Filtering | Mechanism to restrict which users/computers a GPO applies to |
| WMI Filter | Dynamic machine query that determines whether a GPO applies |
| Loopback Processing | Computer Configuration feature applying computer-OU user settings to all logons |
| gpresult | Command showing applied and denied GPOs with RSoP data |
| gpupdate | Command forcing immediate GPO refresh on a machine |
| Invoke-GPUpdate | PowerShell cmdlet for remote GPO refresh |
| RSoP | Resultant Set of Policy — the computed effective policy for a user/computer combination |

---

### 14. Study Checklist

- Read Section 1 (Architecture) and understand the GPC + GPT two-component structure
- Read Section 2 (Linking) and understand link targets and their scope
- Read Section 3 (LSDOU) and memorize the processing order and last-applied-wins rule
- Read Section 4 (Enforced and Block Inheritance) and memorize the priority table
- Read Section 5 (Computer vs. User Configuration) and understand the timing and scope difference
- Read Section 6 (Security Filtering) and understand the group restriction approach
- Read Section 7 (WMI Filters) and review filter query examples
- Read Section 8 (Loopback Processing) and understand Replace vs. Merge
- Read Section 9 (Troubleshooting) and memorize gpresult reason codes
- Review the Architecture Reference Diagram in Section 11
- Review all 8 Exam Tips in Section 12
- Complete the Lab for Module 05
- Complete the Quiz for Module 05
- Post your initial Discussion response by Wednesday 11:59 PM

---

### Additional Reading

- [Group Policy overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11))
- [gpresult command reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)
- [Invoke-GPUpdate cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/grouppolicy/invoke-gpupdate)
- [Loopback Processing reference](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/loopback-processing-of-group-policy)
