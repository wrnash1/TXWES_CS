# Reading Guide: Module 07 - File and Print Services

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

Module 07 covers the File and Storage Services and Print and Document Services roles — the two roles most end users interact with daily. This reading guide provides reference tables, permission interaction diagrams, PowerShell command references, exam tips, a glossary, and a study checklist.

**Certification Alignment:** AZ-800 — "Configure and manage file services" and "Configure and manage print services"

---

### 1. File and Storage Services Role Services

| Role Service | Purpose |
|---|---|
| File Server | Base role for creating and managing SMB shares |
| DFS Namespaces | Virtual namespace aggregating shares under a single UNC path |
| DFS Replication | Multi-master folder replication engine (uses RDC) |
| File Server Resource Manager | Quota management, file screening, storage reports |
| Work Folders | Sync server-stored files to user devices |
| iSCSI Target Server | Provides iSCSI block storage targets |
| Storage Replica | Block-level volume replication for DR and HA |

---

### 2. SMB Protocol Versions

| Version | Windows Version | Key Features |
|---|---|---|
| SMB 1.0 | Windows XP/Server 2003 | Legacy; disabled by default in Server 2019/2022 |
| SMB 2.0 | Windows Vista/Server 2008 | Reduced command count, larger reads |
| SMB 2.1 | Windows 7/Server 2008 R2 | Opportunistic locking improvements |
| SMB 3.0 | Windows 8/Server 2012 | Encryption, multichannel, SMB Direct (RDMA) |
| SMB 3.1.1 | Windows 10/Server 2016+ | Pre-auth integrity checks, AES-128-GCM encryption |

**Key point:** SMB 1.0 should be disabled in all modern environments due to security vulnerabilities (exploited by WannaCry ransomware). SMB 3.x encryption provides in-transit protection without a VPN.

---

### 3. Share Permissions vs. NTFS Permissions

| Attribute | Share Permissions | NTFS Permissions |
|---|---|---|
| Applies to | Network access only | Local AND network access |
| Granularity | Three levels: Read, Change, Full Control | Six standard levels plus Special Permissions |
| Set in | Sharing tab / `New-SmbShare` | Security tab / `Set-Acl` |
| Inheritance | Not inherited | Inherited from parent folders |
| Effective permission | Most restrictive of both | Most restrictive of both |

**Effective permission rule for network access:**

```text
Effective = Most Restrictive of (Share Permission AND NTFS Permission)

Example 1:  Share = Read,         NTFS = Full Control  →  Effective = Read
Example 2:  Share = Full Control, NTFS = Read          →  Effective = Read
Example 3:  Share = Change,       NTFS = Modify        →  Effective = Change (Change ≈ Modify)
Example 4:  Share = Full Control, NTFS = Full Control  →  Effective = Full Control
```

**Best practice:** Set Share permissions to Full Control for Authenticated Users. Use NTFS permissions exclusively for access control. This eliminates double-permission management.

---

### 4. NTFS Permission Levels Reference

| Permission | Files | Folders |
|---|---|---|
| Full Control | Read, write, execute, delete, change permissions, take ownership | All file permissions plus delete subfolders |
| Modify | Read, write, execute, delete | Read, write, create, delete (not change permissions) |
| Read and Execute | Read file contents, run executables | List contents, read attributes, run programs |
| List Folder Contents | N/A | List folder contents only |
| Read | Read file contents and attributes | Read folder attributes and list contents |
| Write | Write to existing files | Create files and subfolders |

---

### 5. DFS Namespace Types

| Type | Storage | Path Format | Fault Tolerance |
|---|---|---|---|
| Domain-Based (v2) | AD DS | `\\corp.local\Files` | Yes — multiple namespace servers |
| Stand-alone | Single server | `\\SRV-FS-01\Files` | No — single point of failure |

**Domain-Based namespaces** are stored in AD DS and replicated to all servers hosting the namespace. Recommended for production environments.

**Folder Targets** are the actual UNC share paths that a DFS folder maps to. Multiple targets for the same folder provide site affinity (clients are directed to the nearest server) and redundancy.

---

### 6. DFS Replication Key Concepts

| Concept | Description |
|---|---|
| Replication Group | A set of servers that replicate one or more folders |
| Replicated Folder | The folder being kept in sync across members |
| Remote Differential Compression (RDC) | Sends only changed file blocks, not entire files |
| Staging Folder | Temporary area for outgoing and incoming replication data |
| Conflict Resolution | Last-writer-wins; losing version moved to ConflictAndDeleted |
| Initial Sync | First full replication can be seeded from a backup to avoid large transfers |

---

### 7. FSRM Feature Summary

| Feature | Types | Effect |
|---|---|---|
| Quota Management | Hard (blocks writes), Soft (notification only) | Limits disk space per folder or user |
| File Screening | Active (blocks file types), Passive (logs only) | Controls file types that can be saved |
| Storage Reports | Automated or manual | Reports on disk usage, large files, duplicates |

**FSRM PowerShell quick reference:**

```powershell
# Create a hard quota
New-FsrmQuota -Path "C:\Shares\HR" -Size 5GB -SoftLimit $false

# Create an active file screen blocking executables
New-FsrmFileScreen -Path "C:\Shares\HR" -IncludeGroup "Executable Files" -Active $true

# List available file groups
Get-FsrmFileGroup | Select-Object Name

# Generate a storage report
New-FsrmStorageReport -Name "LargeFiles" -Namespace "C:\Shares" -ReportType LargeFiles
```

---

### 8. Shadow Copies (Previous Versions)

| Parameter | Default / Recommendation |
|---|---|
| Maximum shadow copies per volume | 64 |
| Recommended storage allocation | 10% of volume size |
| Default schedule | 7:00 AM and 12:00 PM daily |
| Storage location | Same volume or separate volume |

**Shadow Copies protect against:** Accidental file deletion, accidental overwrites, corruption of individual files.

**Shadow Copies do NOT protect against:** Volume-level hardware failure, server loss, ransomware that targets shadow copies, data corruption below the volume level.

**Key point:** Shadow Copies are not a backup. They are a self-service recovery mechanism for common accidental changes.

---

### 9. Print Services Reference

| Concept | Description |
|---|---|
| Print Server | Windows Server hosting shared printers; handles spooling and driver distribution |
| Print Spooler | Windows service that queues and manages print jobs |
| Printer Driver | Software that converts print data to printer-specific language |
| Driver Distribution | Clients automatically download the correct driver when connecting to a shared printer |
| AD Publishing | Printers published to AD can be searched by name, location, or capability |
| Printer Pooling | Multiple physical printers presented as one shared printer; jobs distributed to first available |
| Branch Office Printing | Enables clients to spool directly to a local printer when WAN to print server is slow |

---

### 10. File and Print Services PowerShell Reference

```powershell
# ── SMB Shares ──────────────────────────────────────────────────────
# Create a share
New-SmbShare -Name "Data" -Path "C:\Shares\Data" -FullAccess "Domain Admins" -ReadAccess "Authenticated Users"

# List all shares
Get-SmbShare | Select-Object Name, Path, Description

# Remove a share
Remove-SmbShare -Name "Data" -Force

# View share permissions
Get-SmbShareAccess -Name "Data"

# ── NTFS Permissions ─────────────────────────────────────────────────
# View NTFS permissions
(Get-Acl -Path "C:\Shares\Data").Access | Select-Object IdentityReference, FileSystemRights

# Add an NTFS permission
$acl = Get-Acl -Path "C:\Shares\Data"
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("CORP\G_HRReaders","ReadAndExecute","ContainerInherit,ObjectInherit","None","Allow")
$acl.AddAccessRule($rule)
Set-Acl -Path "C:\Shares\Data" -AclObject $acl

# ── DFS ──────────────────────────────────────────────────────────────
# Create a domain-based namespace
New-DfsnRoot -Path "\\corp.local\Files" -TargetPath "\\DC1\Files" -Type DomainV2

# Add a folder to the namespace
New-DfsnFolder -Path "\\corp.local\Files\HR" -TargetPath "\\DC1\HR_Docs"

# List namespace folders
Get-DfsnFolder -Path "\\corp.local\Files\*"

# ── Print Services ───────────────────────────────────────────────────
# Add a printer port for a TCP/IP network printer
Add-PrinterPort -Name "IP_192.168.10.50" -PrinterHostAddress "192.168.10.50"

# Add and share a printer
Add-Printer -Name "HR_Printer" -DriverName "HP Universal Printing PCL 6" `
    -PortName "IP_192.168.10.50" -Shared $true -ShareName "HR_Print" -Published $true

# List all printers
Get-Printer | Select-Object Name, ShareName, Published, DriverName
```

---

### 11. File Services Architecture Reference

```text
\\corp.local\Files          ← DFS Namespace root (Domain-Based)
    │
    ├── \HR                 ← DFS Folder → \\DC1\HR_Docs    (Folder Target)
    │                                   → \\FS2\HR_Docs     (Alternate Target)
    │
    ├── \Finance            ← DFS Folder → \\DC1\Finance_Docs
    │
    └── \IT                 ← DFS Folder → \\DC1\IT_Docs

Each Folder Target is an SMB Share on a physical server.
NTFS permissions on the physical folder control actual access.
Share permissions on the SMB share apply at the network boundary.
DFSR can keep \\DC1\HR_Docs and \\FS2\HR_Docs synchronized.
```

---

### 12. Exam Tips

**Exam Tip 1:** The most restrictive permission applies for network access. Always evaluate Share and NTFS permissions separately, then take the most restrictive result. Local console access is NTFS only.

**Exam Tip 2:** DFS Namespaces vs. DFS Replication. DFSN = the virtual path (namespace). DFSR = the content synchronization engine. You can use each independently. The exam will test whether you know which one provides the unified path and which one keeps data in sync.

**Exam Tip 3:** FSRM quota hard vs. soft. Hard = blocks writes when limit reached. Soft = notifications only. The scenario will describe whether writes should be blocked or just alerted — use that to select the type.

**Exam Tip 4:** FSRM Active vs. Passive file screen. Active blocks the file. Passive logs it. If the scenario says "prevent users from saving," use Active. If it says "audit" or "report on," use Passive.

**Exam Tip 5:** Shadow Copies are not a replacement for backup. They are an adjunct for self-service recovery. A question about recovering from a failed RAID array or a ransomware attack requires a proper backup, not Shadow Copies.

**Exam Tip 6:** SMB 1.0 is a security vulnerability and should be disabled. The exam may present a scenario where legacy SMB 1.0 is enabled and ask how to harden the server — the answer is to disable SMB 1.0.

**Exam Tip 7:** Printer driver distribution. When a Windows client connects to a shared printer on a Windows print server, the driver is downloaded automatically. This is the key advantage of a central print server over direct-IP printing.

**Exam Tip 8:** DFS Folder Targets with multiple targets support site affinity. Clients in a site are directed to the folder target on a server in the same AD site, reducing WAN traffic for file access.

---

### 13. Glossary

| Term | Definition |
|---|---|
| SMB | Server Message Block — network file sharing protocol used by all Windows file and print sharing |
| NTFS | New Technology File System — the Windows file system providing ACL-based permissions |
| ACL | Access Control List — the list of permissions on an NTFS object |
| Share Permission | Permission applied at the network share boundary — applies to remote access only |
| NTFS Permission | Permission applied to the file system object — applies to local and remote access |
| DFS | Distributed File System — umbrella term for DFS Namespaces and DFS Replication |
| DFSN | DFS Namespaces — creates a virtual folder hierarchy mapping to physical share paths |
| DFSR | DFS Replication — keeps folder contents synchronized across multiple servers using RDC |
| RDC | Remote Differential Compression — sends only changed file blocks to reduce replication bandwidth |
| Folder Target | The actual UNC path to a physical share that a DFS folder maps to |
| FSRM | File Server Resource Manager — manages quotas, file screening, and storage reports |
| Hard Quota | FSRM quota type that blocks writes when the limit is reached |
| Soft Quota | FSRM quota type that sends notifications but does not block writes |
| Active Screen | FSRM file screen that actively blocks files matching the defined file groups |
| Passive Screen | FSRM file screen that logs events but does not block files |
| Shadow Copy | Point-in-time snapshot of a volume used for Previous Versions file recovery |
| Print Server | A Windows Server hosting shared printers, handling spooling and driver distribution |
| Print Spooler | Windows service that queues and manages print jobs |
| Printer Pooling | Multiple physical printers presented as a single shared printer |

---

### 14. Study Checklist

- Watch Module 07 Part 1 video (concepts: SMB, permissions, DFS, FSRM, Shadow Copies, Print Services)
- Watch Module 07 Part 2 video (PowerShell demos, exam tips, lab preview)
- Memorize the Share + NTFS effective permission rule and practice the four examples in Section 3
- Know the difference between DFSN and DFSR and when each is used
- Know the four FSRM combinations: Hard/Soft quota, Active/Passive file screen
- Understand what Shadow Copies protect against and what they do not
- Review all PowerShell commands in Section 10
- Complete Lab 07 and submit required screenshots

---

### Additional Resources

- [SMB file sharing overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview)
- [DFS Namespaces overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview)
- [DFS Replication overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/dfsr-overview)
- [File Server Resource Manager](https://learn.microsoft.com/en-us/windows-server/storage/fsrm/fsrm-overview)
- [Print and Document Services](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-roles-features/print-and-document-services-overview)

---

*Review all sections before beginning Lab 07, Quiz 07, and Discussion 07.*
