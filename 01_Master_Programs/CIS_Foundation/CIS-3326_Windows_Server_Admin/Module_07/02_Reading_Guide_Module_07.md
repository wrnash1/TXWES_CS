# Reading Guide: Module 07 — Active Directory User and Group Management

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

Module 07 covers Active Directory user and group management — the daily
operational foundation of every Windows domain. This reading guide provides
reference tables for OU design, group scopes, the AGDLP pattern, PowerShell
command references, exam tips, a glossary, and a study checklist.

---

## 1. Organizational Unit Design Patterns

| Pattern | Top-Level OUs | Best For |
|---|---|---|
| Geography-based | Locations (Dallas, Chicago) | Decentralized IT, multi-site orgs |
| Function-based | Departments (IT, Finance, HR) | Centralized IT, consistent policy |
| Hybrid | Mix of geography and function | Large enterprises |

**Key rule:** OUs — not CN=Users or CN=Computers containers — should hold all
managed objects. Built-in containers cannot have Group Policy linked directly.

---

## 2. User Account Key Attributes

| Attribute | LDAP Name | Notes |
|---|---|---|
| Username (logon) | sAMAccountName | Max 20 chars; unique in domain |
| Email-style logon | userPrincipalName (UPN) | Unique in forest; preferred for modern auth |
| Display name | displayName | Shown in address books and Global Catalog |
| Employee ID | employeeID | Links to HR systems |
| Manager | manager | Distinguished name of the manager object |
| Distinguished name | distinguishedName | Full LDAP path; auto-generated |

---

## 3. Group Types

| Type | Can Assign Permissions | Email Distribution | Use Case |
|---|---|---|---|
| Security | Yes | Yes (in Exchange environments) | File, printer, and resource access control |
| Distribution | No | Yes | Email mailing lists only |

**Rule of thumb:** When in doubt, create a Security group. It does everything a
Distribution group does, plus permission assignment.

---

## 4. Group Scopes Reference

| Scope | Members Can Come From | Can Be Used In | Global Catalog Impact |
|---|---|---|---|
| Domain Local | Same domain, other domains, trusted forests | Same domain only | Not replicated to GC |
| Global | Same domain only | Any domain in forest | Replicated to GC (membership not included) |
| Universal | Any domain in the forest | Any domain in forest | Membership replicated to GC |

**Universal group membership** is replicated to every Global Catalog domain
controller in the forest. Frequent membership changes cause replication traffic.
Use Universal groups only when cross-domain membership is genuinely required.

---

## 5. AGDLP Nesting Strategy

```text
Accounts   → Global group  → Domain Local group  → Permission on Resource
(users)      (role-based)    (resource-based)       (NTFS or share)

Example:
jsmith  ──►  G_IT_Admins  ──►  DL_ITShare_FullControl  ──►  Full Control on \\DC1\IT
```

**In multi-domain forests extend to AGUDLP:**

```text
Accounts → Global → Universal → Domain Local → Permission
```

Benefits of AGDLP:

- Add a user to a Global group once; they inherit all resources that Domain
  Local group controls.

- Change permissions on one Domain Local group; all role-based Global groups
  inside it inherit the change.

- Clear separation between who (Global) and what resource (Domain Local).

---

## 6. New-ADUser Parameter Reference

```powershell
New-ADUser `
    -Name               "First Last" `
    -GivenName          "First" `
    -Surname            "Last" `
    -SamAccountName     "firstlast" `
    -UserPrincipalName  "firstlast@domain.com" `
    -DisplayName        "First Last" `
    -Department         "IT" `
    -Title              "Job Title" `
    -Path               "OU=IT,OU=ROOT,DC=domain,DC=com" `
    -AccountPassword    (ConvertTo-SecureString "P@ss!" -AsPlainText -Force) `
    -ChangePasswordAtLogon $true `
    -Enabled            $true
```

**Critical parameters:**

- `-Path` — omitting this places the user in CN=Users (no GPO support).

- `-AccountPassword` with `ConvertTo-SecureString` — required; cannot pass plain
  text.

- `-Enabled $true` — new accounts are disabled by default without this flag.

---

## 7. New-ADGroup Parameter Reference

```powershell
New-ADGroup `
    -Name          "GroupName" `
    -GroupScope    Global | DomainLocal | Universal `
    -GroupCategory Security | Distribution `
    -Description   "Description text" `
    -Path          "OU=IT,OU=ROOT,DC=domain,DC=com"
```

| GroupScope value | Creates |
|---|---|
| `Global` | Global scope group |
| `DomainLocal` | Domain Local scope group |
| `Universal` | Universal scope group |

---

## 8. Account Management PowerShell Quick Reference

```powershell
# ── Create ───────────────────────────────────────────────────────────
New-ADUser            -Name "..." -SamAccountName "..." -Enabled $true ...
New-ADGroup           -Name "..." -GroupScope Global -GroupCategory Security ...
New-ADOrganizationalUnit -Name "..." -Path "DC=domain,DC=com"

# ── Modify ───────────────────────────────────────────────────────────
Set-ADUser            -Identity "sam" -Department "NewDept" -Title "NewTitle"
Set-ADAccountPassword -Identity "sam" -NewPassword (...) -Reset
Add-ADGroupMember     -Identity "GroupName" -Members "sam1","sam2"
Remove-ADGroupMember  -Identity "GroupName" -Members "sam1" -Confirm:$false
Move-ADObject         -Identity "CN=..." -TargetPath "OU=NewOU,..."

# ── Enable / Disable / Unlock ────────────────────────────────────────
Enable-ADAccount      -Identity "sam"
Disable-ADAccount     -Identity "sam"
Unlock-ADAccount      -Identity "sam"

# ── Query ────────────────────────────────────────────────────────────
Get-ADUser            -Identity "sam" -Properties *
Get-ADUser            -Filter {Department -eq "IT"} -SearchBase "OU=IT,..."
Get-ADGroup           -Identity "GroupName" -Properties Members
Get-ADGroupMember     -Identity "GroupName" -Recursive
Get-ADPrincipalGroupMembership -Identity "sam"
Search-ADAccount      -AccountDisabled
Search-ADAccount      -LockedOut
Search-ADAccount      -AccountExpired

# ── Bulk import ──────────────────────────────────────────────────────
$users = Import-Csv "users.csv"
foreach ($u in $users) { New-ADUser -Name "$($u.First) $($u.Last)" ... }
```

---

## 9. Bulk Provisioning CSV Template

```text
FirstName,LastName,Department,Title,OU
Alice,Johnson,Faculty,Professor,OU=Faculty,OU=TXWES,DC=txwes,DC=edu
Bob,Williams,IT,Help Desk Tech,OU=Helpdesk,OU=IT,OU=TXWES,DC=txwes,DC=edu
Carol,Brown,Students,Student,OU=Students,OU=TXWES,DC=txwes,DC=edu
```

Name convention formula: `$sam = ($row.FirstName[0] + $row.LastName).ToLower()`

---

## 10. Account Lifecycle Reference

| Action | Cmdlet | When to Use |
|---|---|---|
| Create | `New-ADUser` | Onboarding |
| Disable | `Disable-ADAccount` | Termination, leave of absence |
| Enable | `Enable-ADAccount` | Return from leave |
| Unlock | `Unlock-ADAccount` | Lockout after failed logins |
| Reset password | `Set-ADAccountPassword -Reset` | Helpdesk request |
| Move | `Move-ADObject` | Department transfer |
| Delete | `Remove-ADUser` | 30-90 days after disabling |

**Best practice:** Never delete immediately. Disable first, then delete after a
waiting period to allow for audit trail preservation.

---

## 11. Exam Tips

**Exam Tip 1** — Global groups can only contain members from the **same domain**.
This is the most commonly tested scope restriction. If the scenario involves users
from multiple domains, the answer requires Universal or Domain Local groups.

**Exam Tip 2** — AGDLP order is fixed. Accounts go into Global groups. Global
groups go into Domain Local groups. Domain Local groups get the permission.
Reversing any step (e.g., putting Domain Local inside Global) is not allowed.

**Exam Tip 3** — Security groups can be used for both permissions and email
distribution. Distribution groups can only be used for email. If you see a
scenario about assigning NTFS or share permissions, the answer is always a
Security group.

**Exam Tip 4** — `-ProtectedFromAccidentalDeletion $true` is the parameter that
prevents accidental OU deletion. Enabling this is a best practice and exam answer
for "how do you prevent accidental OU removal."

**Exam Tip 5** — `Search-ADAccount` with `-AccountDisabled`, `-LockedOut`, or
`-AccountExpired` is the PowerShell approach to bulk account auditing. Know these
flags for exam scenarios about finding accounts in various states.

**Exam Tip 6** — Universal group membership is replicated to the **Global
Catalog**. Frequent changes to Universal group membership cause excessive GC
replication traffic. The exam may ask which scope to avoid using heavily in a
large multi-site forest.

**Exam Tip 7** — The `-Enabled $true` parameter is required to create an active
account. Without it, `New-ADUser` creates a disabled account even if all other
parameters are correct.

---

## 12. Glossary

| Term | Definition |
|---|---|
| Active Directory (AD) | Microsoft's directory service for managing users, computers, and resources in a Windows domain |
| Organizational Unit (OU) | A container in Active Directory used to organize objects and apply Group Policy |
| Distinguished Name (DN) | The full LDAP path identifying an object's exact location in the directory |
| sAMAccountName | The pre-Windows 2000 logon name; must be unique in the domain; max 20 characters |
| UPN | User Principal Name — email-format logon name; must be unique in the forest |
| Security Group | AD group type used to assign permissions to resources; can also receive email |
| Distribution Group | AD group type for email lists only; cannot be used to assign permissions |
| Domain Local Group | Group scope; can have members from any domain; used for permissions in one domain |
| Global Group | Group scope; members from same domain only; used for role organization |
| Universal Group | Group scope; members from any domain; membership stored in Global Catalog |
| AGDLP | Accounts — Global — Domain Local — Permissions; Microsoft's recommended nesting model |
| Global Catalog | A partial replica of all objects in the forest; stores Universal group membership |
| Bulk Provisioning | Creating multiple user accounts at once, typically from a CSV file using PowerShell |

---

## 13. Study Checklist

- Watch Module 07 Part 1 video (OU design, user attributes, group types and scopes, AGDLP, bulk provisioning overview)

- Watch Module 07 Part 2 video (PowerShell demos: OUs, users, groups, bulk CSV, account management)

- Memorize the three group scopes, their membership rules, and where each can assign permissions

- Draw the AGDLP chain from scratch without looking at notes

- Know every key parameter of `New-ADUser` and `New-ADGroup`

- Know `Search-ADAccount` flags: `-AccountDisabled`, `-LockedOut`, `-AccountExpired`

- Complete Lab 07 and submit required screenshots

---

## Additional Resources

- [Active Directory Users and Groups overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)
- [New-ADUser documentation](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser)
- [New-ADGroup documentation](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup)
- [Best practices for securing Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory)

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 07 topics:

**1. Microsoft Learn — Manage AD DS users and groups**
<https://learn.microsoft.com/en-us/training/modules/manage-active-directory-domain-services-users-groups-computers/>
Interactive module covering user account creation, group scopes, AGDLP implementation, and bulk provisioning techniques with sandbox labs aligned to AZ-800.

**2. Microsoft Docs — Default Active Directory security groups**
<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups>
Full reference for every built-in AD security group, their default rights and memberships. Understanding which built-in groups exist (like Account Operators) is tested on the exam and relevant to Questions 8, 18.

**3. Microsoft Docs — Redirect the Users and Computers default containers**
<https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/redirect-users-computers-default-cn>
Explains how to use `redirusr.exe` and `redircmp.exe` to change the default container for new user and computer accounts — a production best practice that prevents objects from being created in `CN=Users` without OU-level GPO coverage.

**4. Microsoft Docs — Active Directory Recycle Bin step-by-step guide**
<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100->
Covers enabling the AD Recycle Bin, restoring deleted objects with `Restore-ADObject`, and understanding what attributes are preserved — directly relevant to Question 20.

---

*Review all sections before beginning Lab 07, Quiz 07, and Discussion 07.*
