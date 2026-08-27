# Reading Guide: Module 16 — Capstone Review

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Microsoft Windows Server Administration

---

## Overview

This reading guide consolidates the highest-yield concepts from all 15 modules.
Use it as your comprehensive review checklist before the final exam. Topics
are organized by domain, mirroring the structure of Microsoft certification
exam objectives for Windows Server Administration.

---

## Part 1: Remote Desktop Services and Remote Administration

### 1.1 RDS Role Services Reference

| Role Service | Function | Port |
|---|---|---|
| RD Session Host | Hosts user sessions and applications | 3389 (RDP) |
| RD Gateway | Proxies RDP over HTTPS; bypasses port 3389 restrictions | 443 |
| RD Web Access | Web portal for RemoteApp and desktop connections | 443 |
| RD Connection Broker | Session reconnection and load balancing | 3389 |
| RD Licensing | Issues Client Access Licenses (120-day grace) | 135, 49152+ |
| RD Virtualization Host | Hosts personal session desktops on Hyper-V | 3389 |

### 1.2 PSRemoting Command Reference

```powershell
# Interactive one-to-one session
Enter-PSSession -ComputerName "Server01"

# Fan-out command to multiple servers simultaneously
Invoke-Command -ComputerName "Server01","Server02","Server03" -ScriptBlock {
    Get-Service -Name "W32Time"
}

# Create a reusable persistent session
$session = New-PSSession -ComputerName "Server01"
Invoke-Command -Session $session -ScriptBlock { Get-Process }
Remove-PSSession $session

# Enable WinRM if not active
Enable-PSRemoting -Force
```

---

## Part 2: Hyper-V Virtualization

### 2.1 Generation Comparison

| Feature | Generation 1 | Generation 2 |
|---|---|---|
| Firmware | BIOS | UEFI |
| Secure Boot | Not supported | Supported |
| Boot from | IDE, legacy network | NVMe, synthetic network |
| Guest OS | Windows Server 2003+ | Windows Server 2012 R2+ |
| Recommendation | Legacy VMs only | All new deployments |

### 2.2 Checkpoint Types

```powershell
# Create a production checkpoint (VSS-consistent, recommended for VMs with databases)
Checkpoint-VM -Name "WebVM" -SnapshotName "PrePatch" -CheckpointType Production

# Restore to a checkpoint
Restore-VMCheckpoint -Name "WebVM" -SnapshotName "PrePatch" -Confirm:$false

# Remove a checkpoint
Remove-VMCheckpoint -VMName "WebVM" -SnapshotName "PrePatch"
```

### 2.3 Hyper-V Replica Failover Types

| Failover Type | When Used | Effect on Replication |
|---|---|---|
| Planned Failover | Deliberate switchover (maintenance) | Replication continues reversed |
| Unplanned Failover | Primary site failure | Replication must be resumed manually |
| Test Failover | DR testing | No impact on production replication |

---

## Part 3: Storage

### 3.1 Storage Spaces Resiliency Comparison

| Type | Minimum Disks | Fault Tolerance | Use Case |
|---|---|---|---|
| Simple | 1 | None | Temp data, scratch space |
| Mirror (2-way) | 2 | 1 disk failure | OS volumes, databases |
| Mirror (3-way) | 5 | 2 disk failures | High-availability data |
| Parity | 3 | 1 disk failure | Archival, sequential workloads |
| Dual Parity | 7 | 2 disk failures | Archival with higher protection |

### 3.2 BitLocker Key Protectors

| Protector | Description | Use Case |
|---|---|---|
| TPM | Hardware-bound; auto-unlocks on trusted hardware | Server volumes |
| TPM + PIN | TPM plus a PIN typed at boot | High-security servers with console access |
| TPM + Startup Key | TPM plus USB key at boot | Servers without TPM PIN UI |
| Recovery Key | 48-digit numeric key; emergency access | Always configure as backup |
| Network Unlock | Auto-decrypts when server boots on trusted network | Headless servers in secured datacenters |

```powershell
# Enable BitLocker and back up recovery key to AD
Enable-BitLocker -MountPoint "C:" -TpmProtector
Add-BitLockerKeyProtector -MountPoint "C:" -RecoveryPasswordProtector
Backup-BitLockerKeyProtector -MountPoint "C:" `
    -KeyProtectorId (Get-BitLockerVolume "C:").KeyProtector[1].KeyProtectorId
```

---

## Part 4: Security

### 4.1 Windows Firewall Rule Evaluation

Windows Firewall evaluates rules in the following order. The first match wins,
with Block rules taking precedence over Allow rules.

1. Authenticated bypass rules
2. Block connection rules
3. Allow connection rules

```powershell
# Verify Defender protection status
Get-MpComputerStatus | Select-Object AMRunningMode, RealTimeProtectionEnabled

# Create an inbound Allow rule
New-NetFirewallRule -DisplayName "Allow HTTPS In" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 443 `
    -Action Allow `
    -Profile Domain

# Create an inbound Block rule (overrides any Allow for the same traffic)
New-NetFirewallRule -DisplayName "Block Telnet In" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 23 `
    -Action Block
```

### 4.2 JEA Configuration Summary

```powershell
# Create the Role Capability File
New-PSRoleCapabilityFile -Path "C:\JEA\RoleCapabilities\HelpDesk.psrc" `
    -VisibleCmdlets @(
        "Get-Service",
        "Restart-Service",
        @{Name="Set-Service"; Parameters=@{Name="Name"; ValidateSet=@("DNS","W32Time")}}
    )

# Create the Session Configuration File
New-PSSessionConfigurationFile -Path "C:\JEA\HelpDeskEndpoint.pssc" `
    -SessionType RestrictedRemoteServer `
    -RunAsVirtualAccount `
    -RoleDefinitions @{ "CONTOSO\HelpDesk" = @{ RoleCapabilities = "HelpDesk" } }

# Register the endpoint
Register-PSSessionConfiguration -Name "HelpDeskJEA" `
    -Path "C:\JEA\HelpDeskEndpoint.pssc" `
    -Force
```

### 4.3 LAPS Command Reference

```powershell
# Extend the AD schema (run once as Schema Admin)
Update-LapsADSchema

# Configure permissions for an OU
Set-LapsADComputerSelfPermission -Identity "OU=Servers,DC=contoso,DC=com"

# Retrieve a computer's current LAPS password
Get-LapsADPassword -Identity "Server01" -AsPlainText
```

---

## Part 5: PowerShell and DSC

### 5.1 Event Log Efficiency Reference

```powershell
# Less efficient — retrieves all events then filters in memory
Get-EventLog -LogName Security | Where-Object { $_.InstanceId -eq 4625 }

# Most efficient — server-side filter at source
Get-WinEvent -FilterHashtable @{
    LogName   = "Security"
    Id        = 4625
    StartTime = (Get-Date).AddDays(-1)
}
```

### 5.2 DSC Quick Reference

```powershell
# Compile a configuration to MOF
. "C:\DSC\MyConfig.ps1"
MyConfig -OutputPath "C:\DSC\MOF"

# Apply the configuration
Start-DscConfiguration -Path "C:\DSC\MOF" -Wait -Verbose -Force

# Test compliance (read-only)
Test-DscConfiguration -Verbose

# Configure LCM for auto-correction
[DSCLocalConfigurationManager()]
Configuration AutoCorrectLCM {
    Node "localhost" {
        Settings {
            ConfigurationMode  = "ApplyAndAutoCorrect"
            RefreshMode        = "Push"
            RebootNodeIfNeeded = $false
        }
    }
}
```

### 5.3 LCM Configuration Modes

| Mode | Behavior |
|---|---|
| ApplyOnly | Applies once; no monitoring |
| ApplyAndMonitor | Applies and logs drift; does not correct |
| ApplyAndAutoCorrect | Applies, monitors, and corrects drift automatically |

---

## Part 6: Active Directory and Group Policy Review

### 6.1 GPO Processing Order

LSDOU: Local → Site → Domain → OU (last applied wins for conflicting settings).

Enforced GPOs win regardless of Block Inheritance. Block Inheritance at an OU
prevents higher-level GPOs from applying — except Enforced GPOs, which bypass
the block.

```powershell
# Force Group Policy refresh
Invoke-GPUpdate -Computer "Workstation01" -Force

# Generate HTML GPO report for a user
gpresult /h "C:\Reports\gpreport.html" /user "CONTOSO\jsmith"
```

### 6.2 AD Object Recovery

```powershell
# Restore deleted objects using AD Recycle Bin (requires Recycle Bin to be enabled)
Get-ADObject -Filter {isDeleted -eq $true -and ObjectClass -eq "user"} `
    -IncludeDeletedObjects | Restore-ADObject

# Enable AD Recycle Bin (one-time; requires Forest Functional Level 2008 R2+)
Enable-ADOptionalFeature -Identity "Recycle Bin Feature" `
    -Scope ForestOrConfigurationSet `
    -Target "contoso.com"
```

---

## Part 7: Hybrid Identity Reference

| Authentication Method | Password in Azure AD | On-Premises DC Required | Best For |
|---|---|---|---|
| Password Hash Sync (PHS) | Yes (hash) | No (for cloud auth) | Simplicity and cloud resilience |
| Pass-Through Auth (PTA) | No | Yes (always) | Compliance; passwords never leave on-prem |
| AD FS Federation | No | Yes (always) | Complex claims; conditional access policies |

---

## Key Terms Consolidated

- **FSMO roles** — Five single-master roles; two forest-wide (Schema Master,
  Domain Naming Master), three domain-wide (PDC Emulator, RID Master,
  Infrastructure Master)
- **DSRM** — Directory Services Restore Mode; offline DC maintenance mode
  for AD recovery
- **MOF file** — Managed Object Format; DSC configuration compiled output
- **LCM** — Local Configuration Manager; DSC engine on every managed node
- **JEA** — Just Enough Administration; PowerShell session with constrained
  command set
- **IQN** — iSCSI Qualified Name; unique identifier for iSCSI targets and
  initiators
- **VBS** — Virtualization-Based Security; hardware isolation used by
  Credential Guard and Device Guard
- **RemoteApp** — RDS feature that publishes individual applications rather
  than full desktops
- **GPO** — Group Policy Object; AD object that defines user and computer
  configuration settings
- **CAL** — Client Access License; required for each user or device connecting
  to RDS Session Host

---

## Exam Preparation Checklist

- Review GPO LSDOU processing, Enforced, and Block Inheritance
- Know all five FSMO roles and their functions
- Know the difference between PHS, PTA, and AD FS federation
- Know the three DSC ConfigurationMode options
- Know the RDS role services and their ports
- Know BitLocker key protectors and when to use each
- Know JEA file types (.pssc vs .psrc) and their purposes
- Know Storage Spaces resiliency types and minimum disk requirements
- Know Hyper-V checkpoint types (Standard vs Production)
- Know the difference between Push and Pull mode DSC
- Practice reading scenario questions by identifying the constraint first

---

## Supplemental Resources

The following free, open-access resources support capstone review across all modules:

**1. Microsoft Learn — Administer Windows Server hybrid core infrastructure**
<https://learn.microsoft.com/en-us/training/paths/administer-windows-server-hybrid-core-infrastructure/>
The full AZ-800 learning path covering all capstone topics: AD DS, Group Policy, DNS, DHCP, Hyper-V, Storage, File Services, and hybrid identity. Recommended for end-of-course review before the certification exam.

**2. Microsoft Docs — Windows Server documentation hub**
<https://learn.microsoft.com/en-us/windows-server/>
The central documentation portal for all Windows Server roles and features covered in this course. Use the search and left navigation to quickly locate reference material for any specific topic.

**3. Microsoft Learn — AZ-800 Administering Windows Server Hybrid Core Infrastructure exam skills outline**
<https://learn.microsoft.com/en-us/certifications/exams/az-800>
The official exam skills outline listing every tested topic area with relative weighting. Use this to identify which module topics receive the most exam coverage and prioritize study time accordingly.

**4. Microsoft Q&A — Windows Server Administration community**
<https://learn.microsoft.com/en-us/answers/topics/windows-server.html>
Community Q&A forum for Windows Server administration questions. Useful for reviewing real-world troubleshooting scenarios that mirror the applied reasoning tested on the AZ-800 exam.
