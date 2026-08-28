# Reading Guide: Module 08 — Group Policy Objects (GPOs)

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3326 &BULL; WINDOWS SERVER ADMINISTRATION & ACTIVE DIRECTORY</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

Module 08 covers Group Policy Objects — the centralized configuration management
engine of every Windows domain. This reading guide provides reference tables for
processing order, inheritance, loopback processing, PowerShell commands, exam
tips, a glossary, and a study checklist.

---

## 1. GPO Architecture: Two Storage Locations

| Component | Location | Contains |
|---|---|---|
| Group Policy Container (GPC) | Active Directory database | Metadata: GUID, version numbers, WMI filter links |
| Group Policy Template (GPT) | SYSVOL share on all DCs | Policy settings files, scripts, security templates |

Both must be present and in sync. SYSVOL is replicated via DFSR in Server 2008 R2+
environments.

---

## 2. GPO Structure: Two Configuration Nodes

| Node | Applied At | Triggered By |
|---|---|---|
| Computer Configuration | Computer startup | Machine boot sequence |
| User Configuration | User logon | User authenticating to the domain |

A single GPO can contain both Computer and User Configuration settings.

---

## 3. GPO Processing Order — LSDOU

```text
1. Local Group Policy     (stored on local machine — applied first)
2. Site GPOs              (linked to AD site)
3. Domain GPOs            (linked to domain root)
4. Parent OU GPOs         (parent first, then child)
5. Child OU GPOs          (applied last — highest priority)
```

**Last writer wins.** When the same setting appears in multiple GPOs, the GPO
processed last (closest to the object) wins. Within a single OU with multiple
GPOs, the GPO with the **lowest link order** (highest in the GPMC list) is
processed last and wins.

---

## 4. Inheritance Modifiers

| Modifier | Applied To | Effect |
|---|---|---|
| Block Inheritance | OU | Prevents GPOs from parent containers from applying to this OU |
| Enforced (No Override) | GPO Link | Forces this GPO to apply regardless of Block Inheritance below it |

**Priority rule:** Enforced > Block Inheritance > Normal processing order.

---

## 5. Resultant Set of Policy (RSoP) Tools

| Tool | Purpose | Mode |
|---|---|---|
| `gpresult /r` | Text summary of applied GPOs | Logging (actual computer) |
| `gpresult /h file.html` | HTML RSoP report | Logging (actual computer) |
| `Get-GPResultantSetOfPolicy` | PowerShell HTML RSoP report | Logging |
| Group Policy Modeling (GPMC) | Simulate policy before applying | Planning |
| Group Policy Results (GPMC) | View applied policy on a specific computer | Logging |

`gpresult /h` is the most complete and readable RSoP output for troubleshooting.

---

## 6. Loopback Processing Modes

| Mode | Behavior | Use Case |
|---|---|---|
| Merge | Computer's User Config added to user's normal User Config; computer wins on conflicts | Lab computers where extra restrictions are needed on top of normal user policy |
| Replace | Computer's User Config completely replaces user's normal User Config | Kiosks, RDS Session Hosts, locked-down public terminals |

**Loopback Processing setting location:**

Computer Configuration > Policies > Administrative Templates > System >
Group Policy > Configure user Group Policy loopback processing mode

---

## 7. Account Policies — Domain-Level Requirement

| Policy | Scope Requirement | Location in GPO |
|---|---|---|
| Password Policy | Must be linked at **domain level** for domain accounts | Computer Config > Windows Settings > Security Settings > Account Policies > Password Policy |
| Account Lockout Policy | Must be linked at **domain level** for domain accounts | Computer Config > Windows Settings > Security Settings > Account Policies > Account Lockout Policy |

**Key rule:** Account Policies in OU-level GPOs affect **local accounts** on
computers in that OU only. To enforce domain account password rules, the GPO
must be linked at the domain root.

---

## 8. Common Administrative Template Settings

| Setting | Node | Registry Key |
|---|---|---|
| Prohibit access to Control Panel | User Config > Admin Templates > Control Panel | `HKCU\...\Explorer\NoControlPanel` |
| Prevent access to command prompt | User Config > Admin Templates > System | `HKCU\...\System\DisableCMD` |
| Remove Run from Start menu | User Config > Admin Templates > Start Menu | `HKCU\...\Explorer\NoRun` |
| Disable Task Manager | User Config > Admin Templates > System > Ctrl+Alt+Del | `HKCU\...\System\DisableTaskMgr` |
| Drive map via Group Policy Preferences | User Config > Preferences > Windows Settings > Drive Maps | N/A (preference, not policy) |

---

## 9. PowerShell GPO Management Reference

```powershell
# ── Create and Link ───────────────────────────────────────────────
New-GPO -Name "GPOName" -Domain "domain.com"
New-GPLink -Name "GPOName" -Target "OU=OUName,DC=domain,DC=com" -LinkEnabled Yes

# ── Modify Links ──────────────────────────────────────────────────
Set-GPLink -Name "GPOName" -Target "DC=domain,DC=com" -Enforced Yes
Set-GPLink -Name "GPOName" -Target "DC=domain,DC=com" -LinkEnabled No
Remove-GPLink -Name "GPOName" -Target "OU=OUName,DC=domain,DC=com"

# ── Configure Registry Values ─────────────────────────────────────
Set-GPRegistryValue -Name "GPOName" `
    -Key "HKCU\Software\Policies\..." `
    -ValueName "SettingName" `
    -Type DWord -Value 1

# ── View and Report ───────────────────────────────────────────────
Get-GPO -All | Select-Object DisplayName, GPOStatus
Get-GPInheritance -Target "OU=Students,OU=ROOT,DC=domain,DC=com"
Get-GPOReport -Name "GPOName" -ReportType Html -Path "C:\report.html"

# ── Backup and Restore ────────────────────────────────────────────
Backup-GPO -Name "GPOName" -Path "C:\GPOBackups"
Backup-GPO -All -Path "C:\GPOBackups"
Restore-GPO -Name "GPOName" -Path "C:\GPOBackups"

# ── RSoP ──────────────────────────────────────────────────────────
gpresult /r
gpresult /h C:\GPOReport.html
gpupdate /force
gpupdate /force /logoff
```

---

## 10. GPO Processing Flow Diagram

```text
Computer starts up:
  1. Local Group Policy applied
  2. Site GPOs applied (if any)
  3. Domain GPOs applied
  4. Parent OU GPOs applied
  5. Child OU (computer's OU) GPOs applied  ← highest priority

User logs on:
  1. Local Group Policy — User Config applied
  2. Site GPOs — User Config applied
  3. Domain GPOs — User Config applied
  4. Parent OU GPOs — User Config applied (user's OU hierarchy)
  5. Child OU — User Config applied  ← highest priority

  *If Loopback Replace mode: step 5 uses the COMPUTER's OU GPO User Config
   instead of the user's OU GPO User Config.
```

---

## 11. GPO Troubleshooting Checklist

When a policy is not applying as expected, check these in order:

1. Run `gpresult /h` — verify the GPO is listed in Applied GPOs.

2. If not applied — check if the GPO link is enabled (`Get-GPLink`).

3. Check if Security Filtering is too restrictive — the user/computer must be
   in the Security Filtering group of the GPO.

4. Check for Block Inheritance on the OU (`Get-GPInheritance`).

5. Check whether a higher-priority GPO is overriding the setting.

6. Run `gpupdate /force` and check again.

7. Verify the SYSVOL folder is replicating between domain controllers.

---

## 12. Exam Tips

**Exam Tip 1** — LSDOU: OU GPOs always override Domain GPOs when settings
conflict because OUs are processed last. This is the single most tested GPO
concept.

**Exam Tip 2** — Password and Account Lockout policies must be configured in
a domain-linked GPO to affect domain accounts. OU-level GPOs affect local
accounts on computers in that OU only.

**Exam Tip 3** — Enforced overrides Block Inheritance. Block Inheritance on an
OU stops parent GPOs — except Enforced ones. "Which GPO cannot be blocked?" is
an Enforced GPO.

**Exam Tip 4** — Loopback Replace replaces all user policy with the computer's
location GPO. Loopback Merge adds the computer's policy to the user's normal
policy. Kiosk/locked-down terminal scenarios = Replace mode.

**Exam Tip 5** — `gpresult /h` is the HTML RSoP report. `gpupdate /force`
forces immediate policy refresh. Both appear in troubleshooting questions.

**Exam Tip 6** — `Backup-GPO -All` and `Restore-GPO` are the correct cmdlets
for GPO disaster recovery. Do not manually copy SYSVOL folders.

**Exam Tip 7** — Security Filtering restricts which users or computers a GPO
applies to within a linked OU. By default all Authenticated Users are included.
Removing a group from Security Filtering prevents that group from receiving the GPO.

---

## 13. Glossary

| Term | Definition |
|---|---|
| GPO | Group Policy Object — a collection of settings applied to users and computers via Active Directory |
| LSDOU | Local-Site-Domain-OU — the processing order for Group Policy application |
| Computer Configuration | GPO node containing settings applied at computer startup |
| User Configuration | GPO node containing settings applied at user logon |
| GPC | Group Policy Container — the AD object storing GPO metadata |
| GPT | Group Policy Template — the SYSVOL folder holding GPO setting files |
| SYSVOL | Shared folder on domain controllers holding GPT data; replicated via DFSR |
| Block Inheritance | OU setting preventing parent container GPOs from applying |
| Enforced | GPO link setting that forces application regardless of Block Inheritance |
| RSoP | Resultant Set of Policy — the combined effective policy after all GPOs are evaluated |
| Loopback Processing | Computer-side setting that overrides user-side OU policy with computer-side OU policy |
| Replace mode | Loopback mode where computer's User Config replaces user's normal User Config |
| Merge mode | Loopback mode where computer's User Config is added to user's normal User Config |
| Administrative Templates | Registry-based GPO settings controlling OS and application behavior |
| Security Filtering | Controls which users/computers within a linked OU receive a GPO |
| WMI Filter | Applies a GPO only to computers matching a WMI query |
| gpresult | Command-line tool for viewing Resultant Set of Policy on a computer |
| gpupdate | Command-line tool for forcing immediate Group Policy refresh |

---

## 14. Study Checklist

- Watch Module 08 Part 1 video (GPO architecture, LSDOU, inheritance, RSoP, loopback, security policies)

- Watch Module 08 Part 2 video (PowerShell GPO creation, linking, configuration, gpresult, exam tips)

- Memorize LSDOU order and the last-writer-wins rule with examples

- Know the domain-level requirement for Account Policies

- Know the difference between Enforced and Block Inheritance

- Know Loopback Replace vs. Merge and the kiosk use case

- Know `gpresult /h` and `gpupdate /force`

- Review all PowerShell commands in Section 9

- Complete Lab 08 and submit required screenshots

---

## Additional Resources

- [Group Policy overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)
- [Group Policy processing and precedence](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785665(v=ws.10))
- [Loopback processing](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/loopback-processing-of-group-policy)
- [Get-GPO cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/grouppolicy/get-gpo)

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 08 topics:

**1. Microsoft Learn — Manage Group Policy in Windows Server**
<https://learn.microsoft.com/en-us/training/modules/manage-group-policy-in-windows-server/>
Hands-on module covering GPO creation, LSDOU processing, Enforced, Block Inheritance, Security Filtering, WMI Filters, and RSoP reporting with sandbox exercises.

**2. Microsoft Docs — Group Policy Software Installation**
<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738858(v=ws.10)>
Detailed reference for deploying and uninstalling software via GPO, including the "Uninstall when out of scope" option discussed in Question 12 — directly applicable to enterprise software lifecycle management.

**3. Microsoft Docs — Understanding Group Policy processing order and precedence**
<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785665(v=ws.10)>
Comprehensive explanation of LSDOU, link order, Enforced, and Block Inheritance interaction with detailed worked examples for scenarios that commonly appear on AZ-800.

**4. Microsoft Docs — Group Policy Operational log reference**
<https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/using-group-policy-events-to-troubleshoot>
Covers how to read Event IDs in the Group Policy operational log under Applications and Services Logs — the advanced troubleshooting path when `gpresult` output alone is insufficient.

---

*Review all sections before beginning Lab 08, Quiz 08, and Discussion 08.*
