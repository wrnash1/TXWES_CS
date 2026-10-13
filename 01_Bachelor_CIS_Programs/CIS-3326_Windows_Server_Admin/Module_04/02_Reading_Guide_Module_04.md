# Reading Guide: Module 04 - User, Group, and Computer Accounts in AD

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

---

### Introduction

Module 04 covers the day-to-day administrative objects in Active Directory: user accounts, group accounts, and computer accounts. These three object types are foundational to everything else in a Windows domain — Group Policy applies to them, permissions are assigned through them, and authentication depends on them. This module is heavily tested on AZ-800 both conceptually and through PowerShell syntax questions.

---

### 1. User Accounts

#### 1.1 Account Identifiers

Every AD user account has two login identifiers:

| Identifier | Format | Example | Usage |
|---|---|---|---|
| User Principal Name (UPN) | `username@domain` | `jdoe@corp.local` | Modern logon, Azure AD, email |
| SAM Account Name | `DOMAIN\username` | `CORP\jdoe` | Legacy logon, pre-Windows 2000 apps |

Both can be used at the Windows login screen. UPN is preferred for modern environments.

#### 1.2 Key Account Properties

| Property | Description | Common Use |
|---|---|---|
| Account Expiration | Date after which account auto-disables | Contractors, temporary workers |
| Logon Hours | Days/hours during which logon is permitted | Shift workers, security restrictions |
| Logon Workstations | Specific computers user can log in from | Kiosk accounts, restricted users |
| Account Disabled | Manually disabled; no logon allowed | Departing employees, pre-provisioned accounts |
| Account Locked Out | Disabled after exceeding lockout threshold | Password attacks, forgotten passwords |
| Must Change Password | Forces password change at next logon | New accounts, reset accounts |
| Password Never Expires | Override domain password policy | Service accounts (prefer MSA instead) |

#### 1.3 Disabled vs. Locked Out

These are different conditions and require different remediation:

- Disabled: manually set by an administrator. Remedy: `Enable-ADAccount`
- Locked out: automatic after exceeding lockout threshold. Remedy: `Unlock-ADAccount`

```powershell
# Unlock a locked-out account
Unlock-ADAccount -Identity "jdoe"

# Find all locked-out accounts
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName

# Enable a disabled account
Enable-ADAccount -Identity "jdoe"

# Find all disabled accounts
Search-ADAccount -AccountDisabled | Select-Object Name, SamAccountName
```

#### 1.4 Core User Management Cmdlets

| Cmdlet | Purpose |
|---|---|
| `New-ADUser` | Create a user account |
| `Get-ADUser` | Query user accounts and properties |
| `Set-ADUser` | Modify user properties |
| `Remove-ADUser` | Delete a user account |
| `Disable-ADAccount` | Disable a user or computer account |
| `Enable-ADAccount` | Enable a disabled account |
| `Unlock-ADAccount` | Unlock a locked-out account |
| `Set-ADAccountExpiration` | Set or clear account expiration |
| `Search-ADAccount` | Find accounts by state (locked, disabled, expired) |

---

### 2. Group Accounts

#### 2.1 Group Types

| Type | Can Assign Permissions | Email-Capable | Use Case |
|---|---|---|---|
| Security | Yes | Yes | Resource permission assignment |
| Distribution | No | Yes | Email distribution lists only |

Default choice: always Security. Security groups are more flexible — they work for both permissions and email.

#### 2.2 Group Scopes

| Scope | Who Can Be Members | Where Permissions Apply | GC Stored |
|---|---|---|---|
| Domain Local | Any domain, any forest | Same domain only | No |
| Global | Same domain only | Any domain in forest | No |
| Universal | Any domain in forest | Any domain in forest | Yes |
| Local (Machine) | Domain users, global groups | Single computer | No |

#### 2.3 Group Scope Nesting Rules

```text
Valid nesting (within same forest):
  Universal can contain: Universal, Global
  Global can contain: Global (same domain only)
  Domain Local can contain: Universal, Global, Domain Local (any domain)

Invalid nesting:
  Global cannot contain members from other domains
  Domain Local cannot be nested inside Global
```

#### 2.4 AGDLP Best Practice

AGDLP = Accounts → Global → Domain Local → Permissions

The pattern in practice:

1. Create Global groups named for job roles: `G_Accountants`, `G_FinanceMgrs`
2. Add user accounts to the appropriate Global group
3. Create Domain Local groups named for resource access: `DL_Finance_Read`, `DL_Finance_Write`
4. Nest the Global groups into Domain Local groups
5. Assign NTFS or Share permissions to the Domain Local groups

Benefits:

- Adding a new employee: add to one Global group → inherits all resource access
- Removing an employee: remove from one Global group → loses all resource access
- Adding a new resource: create a Domain Local group → nest existing role groups → done
- Multi-domain: use AGUDLP — Universal group layer enables cross-domain role assignment

#### 2.5 Group Management Cmdlets

| Cmdlet | Purpose |
|---|---|
| `New-ADGroup` | Create a group |
| `Get-ADGroup` | Query groups |
| `Add-ADGroupMember` | Add members to a group |
| `Remove-ADGroupMember` | Remove members from a group |
| `Get-ADGroupMember` | List members of a group |
| `Get-ADPrincipalGroupMembership` | List all groups a user or computer belongs to |

---

### 3. Computer Accounts

#### 3.1 What a Computer Account Is

Every domain-joined Windows computer has a computer account in AD. It:

- Has its own SID and password (rotated every 30 days automatically)
- Is subject to Computer Configuration Group Policy
- Can be a member of security groups
- Has a Distinguished Name in the directory (e.g., `CN=WS-IT-001,OU=Workstations,DC=corp,DC=local`)

#### 3.2 Machine Account Password Rotation

The computer account password is negotiated between the workstation and the DC every 30 days. If a computer is offline for more than 30 days:

- The DC's copy of the password may advance while the computer's local copy stays at the old value
- Result: "The trust relationship between this workstation and the primary domain failed" error on logon

Fix options:

```powershell
# Non-destructive: reset the secure channel without rejoining
# Run on the affected workstation with local admin rights
Test-ComputerSecureChannel -Repair -Credential (Get-Credential "CORP\Administrator")

# Alternative: reset machine password directly
Reset-ComputerMachinePassword -Server "DC1.corp.local" -Credential (Get-Credential "CORP\Administrator")
```

Rejoining the domain also fixes it but changes the computer's SID, which can break user profile associations and break local group memberships. Avoid rejoining unless `Test-ComputerSecureChannel -Repair` fails.

#### 3.3 Pre-staging Computer Accounts

Administrators can create computer accounts in advance before a machine is joined, placing them in the correct OU:

```powershell
New-ADComputer -Name "WS-IT-001" `
    -Path "OU=Workstations,DC=corp,DC=local" `
    -Enabled $true
```

When the computer is later joined, it claims the pre-staged account and inherits any GPO links already targeting that OU.

#### 3.4 Computer Account Cmdlets

| Cmdlet | Purpose |
|---|---|
| `New-ADComputer` | Pre-stage a computer account |
| `Get-ADComputer` | Query computer accounts |
| `Set-ADComputer` | Modify computer account properties |
| `Remove-ADComputer` | Delete a computer account |
| `Test-ComputerSecureChannel` | Test and repair the machine account secure channel |
| `Reset-ComputerMachinePassword` | Reset the machine account password |

---

### 4. Service Accounts

#### 4.1 Why Managed Service Accounts Exist

Traditional service accounts are standard user accounts configured with non-expiring passwords. Problems:

- Password changes require manual updates to every service using the account
- Forgotten password changes cause service outages
- Privileged credentials stored in service configurations create security risk

#### 4.2 Managed Service Account (MSA)

- Tied to a single computer — cannot be used on multiple machines
- Password rotates automatically every 30 days (managed by AD and the OS)
- No administrator manages the password
- Requires Windows Server 2008 R2+ DC

```powershell
# Create an MSA
New-ADServiceAccount -Name "SVC_SQLAgent" -RestrictToSingleComputer

# Install the MSA on the target server (run on target server)
Install-ADServiceAccount -Identity "SVC_SQLAgent"

# Verify the MSA is installed correctly
Test-ADServiceAccount -Identity "SVC_SQLAgent"
```

#### 4.3 Group Managed Service Account (gMSA)

- Can be used on multiple servers simultaneously (web farms, clusters)
- Password rotates automatically
- Requires a KDS Root Key to exist in the forest (created once)
- Requires Windows Server 2012+ DC

```powershell
# Create KDS Root Key (one time per forest)
# -EffectiveImmediately waits 10 hours in production; use for lab only
Add-KdsRootKey -EffectiveImmediately

# Create a gMSA
New-ADServiceAccount -Name "SVC_WebApp" `
    -DNSHostName "webapp.corp.local" `
    -PrincipalsAllowedToRetrieveManagedPassword "WebServers_Group"

# Install the gMSA on each web server (run on each server)
Install-ADServiceAccount -Identity "SVC_WebApp"
```

#### 4.4 MSA vs. gMSA Decision

| Feature | MSA | gMSA |
|---|---|---|
| Servers | Single server only | Multiple servers |
| Auto password rotation | Yes | Yes |
| KDS Root Key required | No | Yes |
| Minimum DC version | 2008 R2 | 2012 |
| Multi-server load balance | No | Yes |

---

### 5. Fine-Grained Password Policies

By default, a domain has one password policy that applies to all users. Fine-Grained Password Policies (FGPPs) allow different password policies for different groups. They were introduced with Windows Server 2008 DFL.

```powershell
# Create a strict password policy for IT Admins
New-ADFineGrainedPasswordPolicy `
    -Name "IT_Admin_Policy" `
    -Precedence 10 `
    -MinPasswordLength 16 `
    -PasswordHistoryCount 24 `
    -LockoutThreshold 3 `
    -LockoutDuration "00:30:00" `
    -ComplexityEnabled $true

# Apply the policy to a group
Add-ADFineGrainedPasswordPolicySubject `
    -Identity "IT_Admin_Policy" `
    -Subjects "G_ITAdmins"
```

Lower `Precedence` number = higher priority. If a user belongs to multiple groups with FGPPs, the lowest-precedence-number policy wins.

---

### 6. AGDLP Architecture Reference

```text
RESOURCE: \\SRV-FS01\HR_Files (NTFS + Share permissions)
    |
    +-- DL_HR_Read (Domain Local, Security) [NTFS: Read]
    |       |
    |       +-- G_HRUsers (Global, Security)
    |               |
    |               +-- jsmith (User Account)
    |               +-- cevans (User Account)
    |
    +-- DL_HR_Write (Domain Local, Security) [NTFS: Modify]
            |
            +-- G_HRManagers (Global, Security)
                    |
                    +-- mjones (User Account)

MANAGEMENT OPERATION:
  New HR employee hired → Add-ADGroupMember G_HRUsers → auto-inherits Read access
  HR employee promoted → Add-ADGroupMember G_HRManagers → gains Write access
  HR employee leaves → Disable-ADAccount → Remove-ADGroupMember (all groups) → loses all access
```

---

### 7. Exam Tips for Module 04

**Tip 1 — Group scope rules:** Domain Local = can hold members from anywhere, assigns permissions locally. Global = holds only local-domain members, assigns permissions anywhere. Universal = both — at GC replication cost.

**Tip 2 — AGDLP nesting order:** Accounts inside Global groups, Global groups inside Domain Local groups, permissions on Domain Local groups. Reversing the nesting (DL inside Global) is a common exam distractor.

**Tip 3 — Secure channel repair:** "Trust relationship failed" = stale machine account. Use `Test-ComputerSecureChannel -Repair` first. Rejoin only as a last resort — it changes the SID.

**Tip 4 — MSA vs. gMSA:** Single server = MSA. Multiple servers = gMSA. gMSA requires `Add-KdsRootKey` first. Both rotate passwords automatically.

**Tip 5 — Disable vs. delete:** Always disable departing employee accounts. Deletion loses the SID and all associated permissions. Disabling preserves everything for audits and potential reactivation.

**Tip 6 — Fine-Grained Password Policies:** Applied to groups (or specific users) via PSOs. Lower precedence number = wins. Requires 2008 DFL minimum.

**Tip 7 — Distribution groups:** Cannot be used to assign permissions. Security groups can be used for both permissions and distribution. If in doubt, create a Security group.

**Tip 8 — Universal groups and GC:** Universal Group membership is stored in the Global Catalog. Putting large numbers of users directly in Universal Groups creates high GC replication volume when membership changes. Nest Global groups into Universal groups to minimize GC replication traffic.

---

### 8. Key Terms Glossary

| Term | Definition |
|---|---|
| UPN | User Principal Name — modern domain account login in email format |
| SAM Account Name | Legacy logon name, max 20 characters, `DOMAIN\username` format |
| Domain Local Group | Group scope for resource permission assignment within one domain |
| Global Group | Group scope for role membership, usable for permissions across domains |
| Universal Group | Group scope for cross-domain membership and permissions; stored in GC |
| AGDLP | Account, Global, Domain Local, Permissions — best-practice nesting model |
| MSA | Managed Service Account — auto-rotating password, single-server scope |
| gMSA | Group Managed Service Account — auto-rotating password, multi-server scope |
| KDS Root Key | Key Distribution Services root key required for gMSA password distribution |
| FGPP | Fine-Grained Password Policy — per-group password policy |
| PSO | Password Settings Object — the AD object that stores an FGPP |
| Secure Channel | The machine account trust relationship between a workstation and DC |

---

### 9. Study Checklist

- Read Section 1 (User Accounts) and memorize all account property types and cmdlets
- Read Section 2 (Groups) and memorize the scope matrix and AGDLP pattern
- Read Section 3 (Computer Accounts) and understand machine password rotation and repair
- Read Section 4 (Service Accounts) and distinguish MSA from gMSA
- Read Section 5 (Fine-Grained Password Policies) and understand PSO application
- Review the AGDLP Architecture Reference in Section 6
- Review all 8 Exam Tips in Section 7
- Complete the Lab for Module 04
- Complete the Quiz for Module 04
- Post your initial Discussion response by Wednesday 11:59 PM

---

### Additional Reading

- [ActiveDirectory PowerShell module reference](https://learn.microsoft.com/en-us/powershell/module/activedirectory/)
- [Understanding AD security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)
- [Group Managed Service Accounts overview](https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview)
- [Fine-Grained Password Policies](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt)

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 04 topics:

**1. Microsoft Learn — Manage AD DS users, groups, and computers**
<https://learn.microsoft.com/en-us/training/modules/manage-active-directory-domain-services-users-groups-computers/>
Guided module with sandbox exercises covering user account creation, group scope selection, AGDLP nesting, and account lifecycle operations using both GUI and PowerShell.

**2. Microsoft Docs — Active Directory security groups reference**
<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups>
Complete reference for all built-in AD security groups (Domain Admins, Enterprise Admins, etc.), their default rights, and membership rules. Essential for understanding privilege boundaries tested on AZ-800.

**3. Microsoft Learn — Implement Group Managed Service Accounts**
<https://learn.microsoft.com/en-us/training/modules/implement-group-managed-service-accounts/>
Step-by-step coverage of KDS Root Key creation, gMSA deployment, and multi-server password retrieval configuration — directly supporting Questions 5 and 10 in this module.

**4. Microsoft Docs — Fine-Grained Password Policy step-by-step guide**
<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100->
Shows how to create and apply Password Settings Objects using Active Directory Administrative Center and PowerShell, including precedence conflict resolution examples.
