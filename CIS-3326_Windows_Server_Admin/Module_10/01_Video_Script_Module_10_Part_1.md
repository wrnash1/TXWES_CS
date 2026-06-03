# Video Script: Module 10 — File and Print Services in Windows Server (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back to CIS-3326 Windows Server Administration.

I am Professor Nash. Module 10 covers File and Print Services — the two most
frequently used server roles in any Windows environment. Every organization
shares files and printers. Understanding how Windows Server controls access to
both is essential for administration and for certification.

Part 1 covers the concepts and architecture: SMB, NTFS permissions, share
permissions, effective permissions, DFS Namespaces, print server architecture,
and printer pooling. Part 2 covers installation, configuration, and
troubleshooting with PowerShell.

---

## Section 1: SMB and the File Server Role

Windows file sharing is built on the **Server Message Block (SMB)** protocol,
also known as **CIFS** (Common Internet File System) in older documentation.
SMB is the protocol that allows clients to connect to shared folders on a
Windows server over the network.

Windows Server 2022 uses SMB 3.1.1 by default. Key SMB versions and their
significance:

- **SMB 1** — Legacy protocol, removed from modern Windows Server. Exploited
  by the WannaCry ransomware attack. Never enable SMB 1 in production.

- **SMB 2** — Introduced with Windows Server 2008. Significantly reduced
  chattiness and added pipelining.

- **SMB 3** — Introduced with Windows Server 2012. Added SMB Direct, SMB
  Multichannel, and end-to-end encryption.

The **File Server** role is installed via the File and Storage Services feature.
Once a share is created, clients connect using a UNC path:
`\\ServerName\ShareName`.

---

## Section 2: NTFS Permissions

**NTFS permissions** control access to files and folders at the file system
level. They apply regardless of how a user accesses the resource — locally,
over the network, or through a Remote Desktop session.

NTFS standard permissions:

- **Full Control** — read, write, modify, delete, take ownership, change
  permissions.

- **Modify** — read, write, delete files and folders. Cannot change permissions
  or take ownership.

- **Read and Execute** — view folder contents and run programs.

- **List Folder Contents** — list folder contents only (folders, not files).

- **Read** — view file contents and attributes.

- **Write** — create files, write data, append data.

NTFS permissions are cumulative across group memberships — a user receives the
union of all NTFS permissions from all groups they belong to. The exception is
**Deny**: an explicit Deny on any permission overrides any Allow for the same
permission, regardless of group membership.

NTFS permissions are inherited by default. A child folder inherits permissions
from its parent. You can disable inheritance and convert inherited permissions
to explicit permissions on any folder.

---

## Section 3: Share Permissions

**Share permissions** apply only when a user accesses the resource over the
network through a share. They do not apply to local access or RDP sessions.

Share permissions are simpler than NTFS permissions — only three options:

- **Full Control** — read, change, and take ownership of files.

- **Change** — read and modify files. Cannot change permissions or take
  ownership.

- **Read** — view files and run programs.

Share permissions are also cumulative. Deny overrides Allow, same as NTFS.

---

## Section 4: Effective Permissions — The Most Restrictive Rule

When a user accesses a shared folder over the network, **both** NTFS
permissions and Share permissions apply. The effective permission is the
**most restrictive** combination of the two.

```text
Access Method      Permissions Applied
─────────────────────────────────────────
Local access       NTFS only
RDP (Remote)       NTFS only
Network (SMB)      NTFS AND Share — most restrictive wins
```

Example:

- Share permission: Full Control
- NTFS permission: Read

Effective network access = Read (most restrictive wins).

Best practice: grant **Everyone Full Control** at the share level and control
access exclusively through NTFS permissions. This simplifies management — you
only manage one permission set rather than two.

---

## Section 5: Access-Based Enumeration

**Access-Based Enumeration (ABE)** is a share setting that hides files and
folders from users who do not have Read permission on them. Without ABE, a
user browsing a share sees all files and folders even if they cannot open them.
With ABE, they only see what they can access.

ABE is configured per-share when creating or modifying a share. It is
particularly useful for department shares where multiple teams store data in
subfolders under a shared root.

---

## Section 6: DFS Namespaces

**Distributed File System (DFS) Namespaces** allow you to create a virtual
folder structure that points to shares on multiple servers. From the client's
perspective, all files appear to live under one unified path such as
`\\txwes.edu\Shared`.

DFS Namespace components:

- **Namespace server** — the server hosting the DFS namespace. In a domain,
  this is typically a domain controller or member server.

- **Namespace root** — the top-level virtual folder. Example: `\\txwes.edu\Shared`.

- **DFS folder** — a virtual subfolder within the namespace.

- **Folder target** — the actual UNC path to the physical share that the
  DFS folder points to. Example: `\\DC1\Departments`.

Two namespace types:

- **Domain-based** — the namespace is stored in Active Directory and is highly
  available. Clients access it via the domain name: `\\txwes.edu\Shared`.

- **Stand-alone** — stored on a single server. Less resilient. Used for
  simpler environments or workgroup networks.

DFS also supports **DFS Replication (DFSR)**, which replicates the contents of
shared folders between servers for redundancy and load distribution. DFS
Namespaces and DFS Replication are independent features — you can use one
without the other.

---

## Section 7: Print Server Architecture

A **Print Server** hosts shared printers and manages print jobs for network
clients. Centralizing print management on a server offers key advantages:

- Drivers are installed once on the server. Clients connect to the shared
  printer and the driver is automatically deployed.

- The print queue is visible and manageable from one console.

- Printer permissions (Print, Manage Printers, Manage Documents) are
  configured centrally.

Windows print architecture components:

- **Print device** — the physical hardware (the actual printer).

- **Logical printer** — the software representation in Windows. This is what
  users see and connect to.

- **Print spooler** — the Windows service that queues and manages print jobs.
  Service name: `Spooler`.

- **Printer driver** — software that translates print data into a format the
  print device understands.

---

## Section 8: Printer Permissions

Printer permissions control who can print, who can manage jobs, and who can
manage the printer configuration:

| Permission | Capabilities |
|---|---|
| Print | Submit print jobs, manage own documents |
| Manage Documents | Pause, resume, restart, cancel any document in the queue |
| Manage Printers | Change printer properties, share settings, permissions |

By default, the Everyone group has Print permission. The Creator Owner group
has Manage Documents (users can manage their own jobs). Administrators have
Full Control.

---

## Section 9: Printer Pooling

**Printer pooling** allows multiple identical physical print devices to share
a single logical printer. The print spooler sends each job to the next
available physical device in the pool, distributing the print load.

Requirements for printer pooling:

- All physical printers in the pool must use the same driver.

- Printers in the pool should be physically near each other because the user
  does not know which device will print their job.

Printer pooling is configured by enabling the pool option in the printer's
port settings and adding the port for each physical device.

---

## Wrap-Up: Part 1 Summary

Let us review what we covered in Part 1:

- SMB is the protocol for Windows file sharing. SMB 1 is retired and dangerous.
  SMB 3 provides encryption and high-performance features.

- NTFS permissions apply at the file system level for all access methods. They
  are cumulative; Deny overrides Allow.

- Share permissions apply only to network access. Best practice is Everyone
  Full Control at the share level with NTFS controlling the actual access.

- Effective network permissions are the most restrictive intersection of NTFS
  and Share permissions.

- DFS Namespaces create a unified virtual path to shares distributed across
  multiple servers. Domain-based namespaces are stored in AD.

- Print servers centralize driver management, queuing, and permissions.

- Printer pooling distributes print jobs across multiple identical devices
  sharing one logical printer.

In Part 2 we install the File Server and Print Server roles, create shares,
configure NTFS permissions, build a DFS Namespace, install a printer, and
verify everything with PowerShell.

See you in Part 2.
