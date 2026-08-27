# Reading Guide: Module 03 - Installing and Configuring AD DS

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 03 translates the AD DS architecture knowledge from Module 02 into hands-on deployment skills. This module covers the complete AD DS installation and promotion process, functional level management, DNS integration requirements, replication verification, and post-promotion health checks. These operational tasks are heavily tested on the AZ-800 exam and are core daily-administration skills.

---

### 1. The Two-Step AD DS Deployment Process

The single most common exam mistake in this topic area is conflating these two steps.

#### Step 1: Install the AD DS Role

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -Verbose
```

This copies binaries to the server. After this step the server is still a member server or standalone server. It cannot authenticate domain users. No domain exists. No NTDS.dit file has been created. The server simply has the software needed to become a DC.

#### Step 2: Promote the Server

Promotion is performed by one of these cmdlets:

| Scenario | PowerShell Cmdlet | GUI |
|---|---|---|
| New forest | `Install-ADDSForest` | Server Manager promotion wizard |
| New child domain | `Install-ADDSDomain` | Server Manager promotion wizard |
| Additional DC in existing domain | `Install-ADDSDomainController` | Server Manager promotion wizard |

After promotion, the server reboots as a Domain Controller. The NTDS.dit database file is created at `C:\Windows\NTDS\`. The DNS Server role is installed if `-InstallDns` was specified. SYSVOL is created at `C:\Windows\SYSVOL\`.

---

### 2. Promotion Scenarios

#### 2.1 New Forest: Install-ADDSForest

```powershell
$dsrmPwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

Install-ADDSForest `
    -DomainName "corp.local" `
    -DomainNetBIOSName "CORP" `
    -ForestMode "WinThreshold" `
    -DomainMode "WinThreshold" `
    -InstallDns `
    -SafeModeAdministratorPassword $dsrmPwd `
    -Force
```

Use when: building AD DS from scratch with no existing forest.

#### 2.2 New Child Domain: Install-ADDSDomain

```powershell
$credential = Get-Credential "CORP\Administrator"
$dsrmPwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

Install-ADDSDomain `
    -NewDomainName "east" `
    -ParentDomainName "corp.local" `
    -DomainType "ChildDomain" `
    -Credential $credential `
    -InstallDns `
    -SafeModeAdministratorPassword $dsrmPwd `
    -Force
```

Use when: adding a child domain to an existing forest. Requires Enterprise Admins credentials in the parent domain.

#### 2.3 Additional DC: Install-ADDSDomainController

```powershell
$credential = Get-Credential "CORP\Administrator"
$dsrmPwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

Install-ADDSDomainController `
    -DomainName "corp.local" `
    -Credential $credential `
    -InstallDns `
    -SafeModeAdministratorPassword $dsrmPwd `
    -Force
```

Use when: adding a second or subsequent DC to an existing domain for redundancy or load distribution. Most common day-to-day operation.

---

### 3. Prerequisites for DC Promotion

| Prerequisite | Requirement | Why It Matters |
|---|---|---|
| Static IP | Server must not use DHCP | DNS SRV records require a stable address |
| DNS configuration | Point to existing DC for domain join; self (127.0.0.1) for new forest | AD DS uses DNS to find other DCs |
| Time synchronization | Within 5 minutes of domain | Kerberos 5-minute clock skew tolerance |
| Account permissions | Domain Admins for additional DC; local Admin for new forest | Authentication against existing domain |
| OS version | Must meet minimum for target functional level | Lower-OS DCs are rejected at target DFL |
| AD DS role installed | Role installation before promotion | Promotion requires installed binaries |

---

### 4. Functional Levels

#### 4.1 What Functional Levels Control

Functional levels determine which AD DS features are enabled based on the oldest DC in the environment.

| Functional Level | Key Features Enabled |
|---|---|
| Windows Server 2008 | Fine-Grained Password Policies (domain), Auditing improvements |
| Windows Server 2008 R2 | Active Directory Recycle Bin (forest), Managed Service Accounts |
| Windows Server 2012 | Dynamic Access Control, Kerberos armoring (FAST) |
| Windows Server 2012 R2 | Protected Users security group, Authentication Policies and Silos |
| Windows Server 2016 (WinThreshold) | PAM (Privileged Access Management) trust, Azure AD join support |

#### 4.2 Raising Functional Levels

```powershell
# Check current levels
(Get-ADDomain).DomainMode
(Get-ADForest).ForestMode

# Verify all DCs are at required OS version
Get-ADDomainController -Filter * | Select-Object Name, OperatingSystem

# Raise domain functional level
Set-ADDomainMode -Identity "corp.local" -DomainMode Windows2016Domain

# Raise forest functional level
Set-ADForestMode -Identity "corp.local" -ForestMode Windows2016Forest
```

#### 4.3 Rules

- Functional level raising is irreversible
- Forest functional level cannot be higher than the lowest domain functional level
- A DC running an OS version lower than the domain's DFL will be rejected during promotion
- Always verify all DC OS versions before raising

---

### 5. DNS Integration

#### 5.1 Why DNS is Required

AD DS clients use DNS SRV records to locate Domain Controllers. Without correct DNS, no client can authenticate.

#### 5.2 Critical SRV Records

| SRV Record | Port | Purpose |
|---|---|---|
| `_ldap._tcp.corp.local` | 389 | DC discovery for LDAP queries |
| `_kerberos._tcp.corp.local` | 88 | Kerberos authentication |
| `_gc._tcp.corp.local` | 3268 | Global Catalog queries |
| `_kpasswd._tcp.corp.local` | 464 | Kerberos password changes |
| `_ldap._tcp.dc._msdcs.corp.local` | 389 | DC-specific LDAP discovery |

These records are registered automatically by the Netlogon service when the DC starts. If they are missing, restart Netlogon:

```powershell
Restart-Service Netlogon
```

#### 5.3 AD-Integrated DNS Zones

DNS zones configured as AD-integrated store their data in the AD DS database rather than flat zone files. Benefits:

- Zone data replicates to all DCs automatically via AD replication
- No primary/secondary zone management required
- Secure dynamic updates — only domain-joined computers can update their DNS records
- Eliminating DNS single points of failure

```powershell
# Check zone type
Get-DnsServerZone -Name "corp.local" | Select-Object ZoneName, ZoneType, DynamicUpdate, ReplicationScope
```

The `ReplicationScope` field should show `Forest` or `Domain` for AD-integrated zones.

---

### 6. SYSVOL and NETLOGON

#### 6.1 SYSVOL

SYSVOL is a shared folder on every Domain Controller that stores:

- Group Policy template files (in the `Policies` subfolder)
- Logon scripts
- Other domain-wide scripts and files

SYSVOL is replicated between all DCs using DFSR (DFS Replication), which replaced the older FRS (File Replication Service) in Windows Server 2008. SYSVOL must be healthy for Group Policy to function.

#### 6.2 NETLOGON

NETLOGON is a subfolder within SYSVOL that clients access during the authentication process. It traditionally hosts logon scripts. The NETLOGON share is automatically published by the Netlogon service.

```powershell
# Verify SYSVOL and NETLOGON shares are present
Get-SmbShare | Where-Object { $_.Name -in "SYSVOL","NETLOGON" }
```

---

### 7. Post-Promotion Verification

#### 7.1 dcdiag Tests

```powershell
# Full diagnostic run
dcdiag /v

# Targeted tests
dcdiag /test:Advertising /v
dcdiag /test:Replications /v
dcdiag /test:SysVolCheck /v
dcdiag /test:DNS /v
```

| Test | What It Checks |
|---|---|
| Advertising | DC is advertising in DNS |
| Replications | Replication with all partners is working |
| SysVolCheck | SYSVOL is shared and published |
| KccEvent | KCC ran without errors |
| DNS | SRV record registration |

#### 7.2 repadmin Commands

```powershell
# Summary of replication health
repadmin /replsummary

# Detailed per-partner replication status
repadmin /showrepl

# Show only failures
repadmin /showrepl * /errorsonly

# Force immediate replication from all partners
repadmin /syncall /AdeP

# Show replication queue
repadmin /queue
```

#### 7.3 DNS Verification

```powershell
# Verify LDAP SRV record
nslookup -type=SRV _ldap._tcp.corp.local

# Verify Kerberos SRV record
nslookup -type=SRV _kerberos._tcp.corp.local

# Verify A record for DC
nslookup DC1.corp.local
```

---

### 8. Read-Only Domain Controllers (RODCs)

#### 8.1 Deployment Scenario

RODCs are used in locations with limited physical security (branch offices, remote sites). If an RODC is stolen:

- The attacker cannot modify the AD database (read-only)
- Only passwords that were cached by the Password Replication Policy are exposed
- Domain Admin credentials should always be in the Denied List

#### 8.2 RODC Deployment

```powershell
Install-ADDSDomainController `
    -DomainName "corp.local" `
    -Credential $credential `
    -ReadOnlyReplica `
    -SiteName "BranchOffice" `
    -SafeModeAdministratorPassword $dsrmPwd `
    -Force
```

#### 8.3 Password Replication Policy

The Password Replication Policy (PRP) controls which account passwords are cached on the RODC:

- Allowed Replication Group — accounts whose passwords may be cached
- Denied RODC Password Replication Group — accounts whose passwords must never be cached (Domain Admins, Enterprise Admins, Schema Admins are members by default)

---

### 9. AD DS Architecture — Deployment Flow

```text
DECISION: New Forest or Existing Forest?
              |
    +---------+---------+
    |                   |
New Forest         Existing Forest
    |                   |
    |            New Domain or Add DC?
    |                   |
    |           +-------+-------+
    |           |               |
    |        New Domain      Add DC
    |           |               |
    v           v               v
Install-     Install-      Install-
ADDSForest   ADDSDomain    ADDSDomainController
    |           |               |
    v           v               v
           REBOOT -> Login as Domain Admin
                |
                v
     POST-PROMOTION VERIFICATION
     dcdiag /v
     repadmin /replsummary
     nslookup -type=SRV _ldap._tcp.<domain>
```

---

### 10. Exam Tips for Module 03

**Tip 1 — Two-step process:** Installing the role and promoting are separate. Installing `AD-Domain-Services` does not create a DC. `Install-ADDSForest` (or the wizard) creates the DC.

**Tip 2 — dcpromo is gone:** `dcpromo.exe` was removed in Windows Server 2012. Current tools are Server Manager wizard or PowerShell cmdlets. Any answer listing `dcpromo` for current Windows Server is a distractor.

**Tip 3 — Functional levels are one-way:** Once raised, they cannot be lowered. Verify all DC OS versions before raising. A DC with a lower OS than the DFL will be rejected during promotion.

**Tip 4 — DSRM password:** Local to each DC. Not the domain Administrator password. Required for offline AD DS maintenance (ntdsutil, authoritative restore). Store it securely.

**Tip 5 — SRV records for DC discovery:** If clients cannot find the DC, check DNS SRV records first. `nslookup -type=SRV _ldap._tcp.<domain>` confirms DC discoverability. Restarting Netlogon re-registers SRV records.

**Tip 6 — AD-integrated zones:** DNS zones should be AD-integrated to replicate with AD and support secure dynamic updates. File-based zones on DCs require separate management and are a single point of failure.

**Tip 7 — RODC Password Replication Policy:** The Denied RODC Password Replication Group blocks privileged account passwords from being cached. Verify sensitive accounts are in the Denied group before deploying RODCs.

**Tip 8 — repadmin /replsummary:** The quickest replication health check. Zero failures = healthy. Any non-zero failure count needs immediate investigation.

---

### 11. Key Terms Glossary

| Term | Definition |
|---|---|
| Install-ADDSForest | PowerShell cmdlet to promote a server as the first DC in a new forest |
| Install-ADDSDomainController | PowerShell cmdlet to add a DC to an existing domain |
| DFL | Domain Functional Level — controls domain-specific AD features |
| FFL | Forest Functional Level — controls forest-wide AD features |
| DSRM | Directory Services Restore Mode — offline recovery boot mode with its own password |
| NTDS.dit | The AD DS database file stored in C:\Windows\NTDS\ on every DC |
| SYSVOL | Replicated folder on all DCs storing Group Policy templates and logon scripts |
| DFSR | DFS Replication — current SYSVOL replication mechanism (replaced FRS in 2008) |
| dcdiag | Domain Controller diagnostic tool running a suite of health tests |
| repadmin | Replication administration tool for monitoring and troubleshooting AD replication |
| KCC | Knowledge Consistency Checker — service that builds and maintains replication topology |
| SRV record | DNS Service Locator record used by AD clients to find Domain Controllers |
| PRP | Password Replication Policy — controls which passwords are cached on an RODC |

---

### 12. Study Checklist

- Read Section 1 (Two-Step Process) and understand the distinction between role install and promotion
- Read Section 2 (Promotion Scenarios) and memorize the three cmdlets and their use cases
- Read Section 3 (Prerequisites) and understand why each prerequisite matters
- Read Section 4 (Functional Levels) and memorize the one-way rule
- Read Section 5 (DNS Integration) and memorize the critical SRV records
- Read Section 6 (SYSVOL and NETLOGON) and understand DFSR
- Read Section 7 (Post-Promotion Verification) and understand dcdiag and repadmin commands
- Read Section 8 (RODCs) and understand Password Replication Policy
- Review the Deployment Flow diagram in Section 9
- Review all 8 Exam Tips in Section 10
- Complete the Lab for Module 03
- Complete the Quiz for Module 03
- Post your initial Discussion response by Wednesday 11:59 PM

---

### Additional Reading

- [Install Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-)
- [AD DS deployment with PowerShell](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-200-)
- [AD DS replication concepts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts)
- [Read-Only Domain Controllers](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/rodc/read-only-domain-controller-updates)

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 03 topics:

**1. Microsoft Learn — Install and configure Active Directory Domain Services**
<https://learn.microsoft.com/en-us/training/modules/install-configure-active-directory-domain-services/>
Step-by-step module covering both GUI and PowerShell promotion workflows, DSRM password management, and post-promotion verification. Includes sandbox exercises.

**2. Microsoft Docs — Troubleshoot AD DS replication with repadmin**
<https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/replication-error-8606>
Comprehensive repadmin reference with error code explanations and resolution steps for the most common replication failures encountered in production and lab environments.

**3. Microsoft Docs — Active Directory functional levels**
<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels>
Complete functional level feature matrix from Windows Server 2003 through current. Essential reference for identifying which feature unlocks at which level before raising your environment.

**4. Microsoft Docs — Deploy a Read-Only Domain Controller**
<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/rodc/install-a-windows-server-2012-active-directory-read-only-domain-controller--rodc---level-200->
Detailed RODC deployment guide covering Password Replication Policy configuration, pre-staging, and branch office security considerations aligned to AZ-800 exam scenarios.
