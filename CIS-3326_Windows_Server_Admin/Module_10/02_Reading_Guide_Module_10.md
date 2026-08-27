# Reading Guide: Module 10 — File and Print Services in Windows Server

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

Module 10 covers File and Print Services — two foundational Windows Server
roles used in every enterprise environment. This reading guide provides
reference tables for NTFS permissions, share permissions, effective permissions,
SMB versions, DFS Namespace components, print server architecture, PowerShell
commands, exam tips, a glossary, and a study checklist.

---

## 1. SMB Version Reference

| Version | Windows Version | Key Features |
|---|---|---|
| SMB 1.0 | Windows NT/2000/XP | Original file sharing protocol; do not use |
| SMB 2.0 | Windows Vista/Server 2008 | Reduced chatiness, pipelining, larger reads |
| SMB 2.1 | Windows 7/Server 2008 R2 | Improved caching, BranchCache support |
| SMB 3.0 | Windows 8/Server 2012 | SMB Direct, Multichannel, end-to-end encryption |
| SMB 3.1.1 | Windows 10/Server 2016+ | Pre-auth integrity, AES-128-GCM encryption |

**SMB 1 must be disabled in all modern environments.** It is the protocol
exploited by EternalBlue/WannaCry and has been removed from Windows Server
2022 by default.

---

## 2. NTFS Standard Permissions Reference

| Permission | Read | Write | Execute | Delete | Change Permissions | Take Ownership |
|---|---|---|---|---|---|---|
| Full Control | Yes | Yes | Yes | Yes | Yes | Yes |
| Modify | Yes | Yes | Yes | Yes | No | No |
| Read and Execute | Yes | No | Yes | No | No | No |
| List Folder Contents | Yes (folder) | No | No | No | No | No |
| Read | Yes | No | No | No | No | No |
| Write | No | Yes | No | No | No | No |

**Key rules:**

- Permissions are cumulative across groups.
- Deny always overrides Allow, regardless of group membership.
- Permissions are inherited from parent folders by default.
- Inheritance can be disabled; inherited permissions can be converted to
  explicit permissions.

---

## 3. Share Permissions Reference

| Permission | Can Read | Can Change | Can Manage Permissions |
|---|---|---|---|
| Read | Yes | No | No |
| Change | Yes | Yes | No |
| Full Control | Yes | Yes | Yes |

Share permissions apply **only** to SMB network access. They do not apply to
local access or Remote Desktop sessions.

---

## 4. Effective Permissions — Access Method Matrix

| Access Method | NTFS Applies | Share Applies | Effective Permission |
|---|---|---|---|
| Local logon | Yes | No | NTFS permissions |
| Remote Desktop (RDP) | Yes | No | NTFS permissions |
| Network (SMB share) | Yes | Yes | Most restrictive of NTFS and Share |

**Best practice:** Grant Everyone Full Control at the share level. Use NTFS
permissions exclusively to control access. This avoids double-maintenance
of two permission sets.

---

## 5. NTFS Inheritance and Propagation Flags

When creating NTFS rules programmatically, the propagation flags determine
where the permission applies:

| Flag | Effect |
|---|---|
| `ContainerInherit` | Applies to subfolders |
| `ObjectInherit` | Applies to files |
| `ContainerInherit,ObjectInherit` | Applies to subfolders and files (full inheritance) |
| `None` | Applies to this folder only |
| `InheritOnly` | Propagates to children but does not apply to this folder |

---

## 6. DFS Namespace Component Reference

| Component | Description | Example |
|---|---|---|
| Namespace server | Hosts the DFS namespace metadata | DC1.txwes.edu |
| Namespace root | Top-level virtual folder | `\\txwes.edu\Shared` |
| DFS folder | Virtual subfolder within the namespace | `\\txwes.edu\Shared\Faculty` |
| Folder target | Physical UNC path the DFS folder points to | `\\DC1\Departments\Faculty` |

| Namespace Type | Storage | Availability | UNC Path Format |
|---|---|---|---|
| Domain-based (DomainV2) | Active Directory | Highly available (AD-backed) | `\\domain\namespace` |
| Stand-alone | Single server | Single server only | `\\server\namespace` |

---

## 7. Print Server Component Reference

| Component | Description |
|---|---|
| Print device | Physical printer hardware |
| Logical printer | Software representation in Windows; what users connect to |
| Print spooler | Windows service (Spooler) that queues and routes print jobs |
| Printer driver | Translates print data to device-specific language |
| Printer port | Network or local connection endpoint for the print device |

### Printer Permissions

| Permission | Capabilities |
|---|---|
| Print | Submit print jobs; manage own documents |
| Manage Documents | Pause, resume, restart, cancel any queued document |
| Manage Printers | Change printer settings, driver, share, and permissions |

---

## 8. Printer Pooling Requirements

- All physical print devices in the pool must use the **same driver**.
- Devices should be **physically co-located** (users cannot predict which
  device prints their job).
- Pooling is configured by adding multiple ports to a single logical printer
  and enabling the pooling option.

---

## 9. File Services PowerShell Quick Reference

```powershell
# ── Role Installation ──────────────────────────────────────────────
Install-WindowsFeature -Name FS-FileServer -IncludeManagementTools
Install-WindowsFeature -Name FS-DFS-Namespace, FS-DFS-Replication -IncludeManagementTools

# ── Share Management ──────────────────────────────────────────────
New-SmbShare -Name "Departments" -Path "C:\Shares\Departments" -FullAccess "Everyone"
Get-SmbShare
Get-SmbShare -Name "Departments"
Set-SmbShare -Name "Departments" -FolderEnumerationMode AccessBased -Force
Remove-SmbShare -Name "Departments" -Force

# ── Share Permissions ─────────────────────────────────────────────
Get-SmbShareAccess -Name "Departments"
Grant-SmbShareAccess -Name "Departments" -AccountName "txwes\Domain Users" `
    -AccessRight Change -Force
Revoke-SmbShareAccess -Name "Departments" -AccountName "Everyone" -Force

# ── NTFS Permissions ──────────────────────────────────────────────
Get-Acl -Path "C:\Shares\Departments\Faculty" | Format-List
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "txwes\Faculty_Staff", "Modify",
    "ContainerInherit,ObjectInherit", "None", "Allow")
$acl = Get-Acl -Path "C:\Shares\Departments\Faculty"
$acl.SetAccessRule($rule)
Set-Acl -Path "C:\Shares\Departments\Faculty" -AclObject $acl

# ── DFS Namespaces ────────────────────────────────────────────────
New-DfsnRoot -Path "\\txwes.edu\Shared" -TargetPath "\\DC1\Departments" `
    -Type DomainV2
New-DfsnFolder -Path "\\txwes.edu\Shared\Faculty" `
    -TargetPath "\\DC1\Departments\Faculty"
Get-DfsnRoot -Path "\\txwes.edu\Shared"
Get-DfsnFolder -Path "\\txwes.edu\Shared\*"
Remove-DfsnFolder -Path "\\txwes.edu\Shared\Faculty" -Force

# ── Session and File Monitoring ────────────────────────────────────
Get-SmbSession
Get-SmbOpenFile
Close-SmbSession -SessionId <id> -Force
```

---

## 10. Print Services PowerShell Quick Reference

```powershell
# ── Role Installation ──────────────────────────────────────────────
Install-WindowsFeature -Name Print-Server -IncludeManagementTools

# ── Printer Ports ─────────────────────────────────────────────────
Add-PrinterPort -Name "Campus_Printer_Port" -PrinterHostAddress "192.168.10.150"
Get-PrinterPort

# ── Printer Drivers ───────────────────────────────────────────────
Add-PrinterDriver -Name "HP Universal Printing PCL 6"
Get-PrinterDriver

# ── Printers ──────────────────────────────────────────────────────
Add-Printer -Name "Campus_LaserJet" -DriverName "HP Universal Printing PCL 6" `
    -PortName "Campus_Printer_Port"
Set-Printer -Name "Campus_LaserJet" -Shared $true -ShareName "Campus_LaserJet"
Get-Printer | Select-Object Name, DriverName, PortName, Shared, ShareName
Remove-Printer -Name "Campus_LaserJet"

# ── Print Queue Management ─────────────────────────────────────────
Get-PrintJob -PrinterName "Campus_LaserJet"
Remove-PrintJob -PrinterName "Campus_LaserJet" -ID <id>

# ── Spooler Service ───────────────────────────────────────────────
Get-Service -Name Spooler
Restart-Service -Name Spooler
```

---

## 11. Architecture Overview

```text
Client (\\txwes.edu\Shared\Faculty)
    │
    │ DFS Namespace lookup → DC1 → folder target: \\DC1\Departments\Faculty
    │
    ▼
DC1 (192.168.10.10)
    ├── File Server
    │     ├── Share: Departments (C:\Shares\Departments)
    │     │     ├── Faculty (NTFS: Faculty_Staff = Modify)
    │     │     ├── Students (NTFS: Domain Users = Read)
    │     │     └── IT (NTFS: IT_Admins = Full Control)
    │     └── ABE enabled on Departments share
    │
    ├── DFS Namespace Server
    │     └── Root: \\txwes.edu\Shared
    │           ├── \\txwes.edu\Shared\Faculty → \\DC1\Departments\Faculty
    │           ├── \\txwes.edu\Shared\Students → \\DC1\Departments\Students
    │           └── \\txwes.edu\Shared\IT → \\DC1\Departments\IT
    │
    └── Print Server
          └── Logical Printer: Campus_LaserJet (shared)
                ├── Port 1: 192.168.10.150 (physical device 1)
                └── Port 2: 192.168.10.151 (physical device 2) [pooling]
```

---

## 12. Exam Tips

**Exam Tip 1** — Effective network permission = most restrictive of NTFS and
Share. The exam will describe both permission sets and ask what the user can
do. Always apply both and take the lower of the two.

**Exam Tip 2** — Share permissions do not affect local or RDP access. If a
scenario describes a user accessing a file locally who is blocked, the issue
is NTFS, not share permissions.

**Exam Tip 3** — Best practice is Everyone Full Control at the share level with
NTFS controlling access. If the exam asks for best practice share configuration,
this is the expected answer.

**Exam Tip 4** — DFS Namespaces provide location transparency. When a server
is retired or shares move, the folder target is updated in DFS and client UNC
paths remain unchanged.

**Exam Tip 5** — Printer pooling requires identical drivers across all pooled
devices. If the exam describes uneven print output or driver errors, the cause
is mismatched drivers in a printer pool.

**Exam Tip 6** — ABE is a share property. It hides items the user cannot read.
Without ABE, all items are visible even if the user lacks access. Enable ABE
by setting `FolderEnumerationMode AccessBased` on the share.

**Exam Tip 7** — The Spooler service (`Spooler`) must be running on the print
server. If no print jobs process, check `Get-Service -Name Spooler`. Restarting
the Spooler clears stuck jobs.

---

## 13. Glossary

| Term | Definition |
|---|---|
| SMB | Server Message Block — the network protocol for Windows file sharing |
| NTFS permissions | File system-level access controls applied regardless of access method |
| Share permissions | Network-level access controls that apply only when accessing via SMB |
| Effective permission | The resulting access level after combining NTFS and share permissions |
| Access-Based Enumeration | Share feature that hides items users cannot read |
| DFS Namespace | Virtual folder structure mapping UNC paths to physical shares on multiple servers |
| Namespace root | Top-level virtual folder of a DFS namespace |
| DFS folder | Virtual subfolder within a DFS namespace |
| Folder target | The physical UNC path a DFS folder resolves to |
| Domain-based namespace | DFS namespace stored in AD; highly available |
| Stand-alone namespace | DFS namespace stored on one server; single point of failure |
| Print server | Server that hosts shared printers and manages print queues |
| Logical printer | Software representation of a printer that clients connect to |
| Print spooler | Windows service that queues and routes print jobs |
| Printer pooling | Multiple physical devices sharing a single logical printer |
| Printer port | Network or local connection endpoint for the physical print device |

---

## 14. Study Checklist

- Watch Module 10 Part 1 video (SMB versions, NTFS permissions, share
  permissions, effective permissions, DFS Namespaces, print server architecture)

- Watch Module 10 Part 2 video (PowerShell installation, share creation, NTFS
  configuration, DFS Namespace, printer installation, pooling, verification)

- Know all NTFS standard permissions and their capabilities

- Know the effective permission rule for SMB network access

- Know when share permissions apply and when they do not

- Know DFS Namespace component types and the difference between domain-based
  and stand-alone namespaces

- Know print server components (logical printer vs. print device vs. driver)

- Know printer pooling requirements

- Review all PowerShell commands in Sections 9 and 10

- Complete Lab 10 and submit required screenshots

---

## Additional Resources

- [File Server overview for Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/fsrm/fsrm-overview)
- [DFS Namespaces overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview)
- [Print and Document Services overview](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/print-and-document-services)
- [SMB security enhancements](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security)

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 10 topics:

**1. Microsoft Learn — Implement and manage file server high availability**
<https://learn.microsoft.com/en-us/training/modules/implement-manage-file-server-high-availability/>
Covers DFS Namespaces, DFS Replication, File Server failover clustering, and storage redundancy strategies with sandbox exercises aligned to the AZ-800 exam.

**2. Microsoft Docs — Access-Based Enumeration**
<https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/enable-access-based-enumeration-on-a-namespace>
Step-by-step guide to enabling ABE at the namespace level and the share level, explaining how enumeration filtering interacts with NTFS permissions and DFS referrals.

**3. Microsoft Docs — DFS Namespaces overview**
<https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview>
Full architecture reference for DFS Namespaces including namespace types (domain-based vs. stand-alone), namespace server roles, folder targets, referral ordering, and site costing.

**4. Microsoft Docs — Print and Document Services**
<https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/print-and-document-services>
Reference for Print Server role installation, shared printer configuration, printer pooling, driver management, and the Print Spooler service including command-line and PowerShell management tools.

---

*Review all sections before beginning Lab 10, Quiz 10, and Discussion 10.*
