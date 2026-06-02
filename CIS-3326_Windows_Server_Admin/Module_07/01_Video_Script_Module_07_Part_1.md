# Video Script: Module 07 - File and Print Services (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 07 - File and Print Services

**Part:** 1 of 2 — Concepts, Theory, and Architecture

**Estimated Duration:** 13 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Introduction]

**[SHOW SCREEN: Course title slide — Module 07]**

Welcome to Module 07. I am Professor Nash. File and Print Services are the server roles that most end users interact with every single day, even when they do not realize it. Every time someone opens a file from a mapped drive, saves a document to a shared folder, or sends a job to a network printer — they are using the services covered in this module.

This module maps to AZ-800 objectives: "Configure and manage file services" and "Configure and manage print services." We will cover SMB and NTFS permissions, DFS Namespaces, DFS Replication, File Server Resource Manager, Shadow Copies, and Windows Server print management.

---

### [SEGMENT 2 — SMB File Sharing and the File and Storage Services Role]

**[SHOW SCREEN: Server Manager — File and Storage Services role services tree]**

[Alt-text: Server Manager showing the File and Storage Services role expanded to reveal role services including File Server, DFS Namespaces, DFS Replication, File Server Resource Manager, and Work Folders.]

Windows Server file sharing uses the SMB protocol — Server Message Block. SMB 3.x is the current version, with SMB 3.1.1 used in Windows Server 2022. It supports encryption, multichannel (multiple NICs simultaneously), and SMB Direct (RDMA — remote direct memory access for extremely fast transfers between servers).

The **File and Storage Services** role umbrella contains:

- **File Server** — the base role for creating and managing SMB shares
- **DFS Namespaces** — virtual namespace for aggregating shares
- **DFS Replication** — multi-master folder replication engine
- **File Server Resource Manager** — quotas, file screening, reports
- **Work Folders** — sync solution for bringing server-stored files to devices

For the exam, know which role service provides which capability.

---

### [SEGMENT 3 — Creating SMB Shares: New Technology File System and Share Permissions]

**[SHOW SCREEN: Windows Explorer — Share properties with Security (NTFS) and Sharing tabs side by side]**

[Alt-text: Windows Explorer showing two tabs: the Sharing tab with Share permissions (Read, Change, Full Control) and the Security tab with NTFS permissions (Full Control, Modify, Read and Execute, Read, Write, Special Permissions).]

When you share a folder on Windows Server, two permission systems apply simultaneously:

**Share Permissions** — apply only to network access through the share path. Three settings:

- **Read** — view files, run programs, read attributes
- **Change** — Read plus create, modify, and delete files
- **Full Control** — Change plus change permissions and take ownership

**NTFS Permissions** — apply to all access, both local and remote, with much finer granularity:

- Full Control, Modify, Read and Execute, List Folder Contents, Read, Write
- Applied per user or group through Access Control Lists (ACLs)
- Inherited from parent folders by default; can be overridden

**The critical rule for network access:** The effective permission is the most restrictive combination of Share and NTFS permissions evaluated separately. If Share says Read and NTFS says Full Control — the user gets Read over the network. If Share says Full Control and NTFS says Read — the user still gets Read.

**Local access** bypasses Share permissions entirely. Only NTFS permissions apply when sitting at the console.

**Best practice:** Set Share permissions to Full Control for Everyone or Authenticated Users, then use NTFS permissions to enforce granular access control. This is simpler to manage and avoids double-permission conflicts.

---

### [SEGMENT 4 — DFS Namespaces]

**[SHOW SCREEN: DFS Management console showing a domain-based namespace with multiple folder targets]**

[Alt-text: DFS Management console showing a namespace \\corp.local\Files with three folders: HR, IT, and Finance, each pointing to a different server share as the folder target.]

**DFS Namespaces (DFSN)** creates a virtual folder hierarchy accessible through a single UNC path, regardless of where the actual data lives on the network.

Example: Instead of users needing to know `\\FS-NYC-01\HR`, `\\FS-LA-01\Finance`, and `\\FS-CHICAGO-01\IT`, they access everything through `\\corp.local\Files\HR`, `\\corp.local\Files\Finance`, and `\\corp.local\Files\IT`. The namespace server redirects them transparently.

Two types of namespaces:

**Domain-Based Namespace** (recommended): Stored in AD DS. Highly available — any domain member with the Namespace Server role can host it. The path starts with the domain name: `\\corp.local\Files`.

**Stand-alone Namespace**: Stored on a single server. The path starts with the server name: `\\SRV-FS-01\Files`. Not fault-tolerant if the server fails.

Each folder in a namespace has one or more **Folder Targets** — the actual UNC paths to server shares. If multiple folder targets point to the same folder on different servers, DFS can load-balance and provide site affinity (users in NYC go to the NYC server automatically).

---

### [SEGMENT 5 — DFS Replication]

**[SHOW SCREEN: DFS Management showing a replication group with two members and a replicated folder]**

[Alt-text: DFS Management console showing a replication group named Corp-Files-RG with two members FS-NYC-01 and FS-LA-01, both listed as Primary and Secondary for the HR folder.]

**DFS Replication (DFSR)** is a multi-master replication engine that keeps folder contents synchronized across multiple servers.

Key DFSR concepts:

**Replication Group:** A group of servers (members) that participate in replicating one or more folders.

**Replicated Folder:** The folder being kept in sync. Each member has a local path for the replicated folder.

**Remote Differential Compression (RDC):** DFSR does not send entire files when a change occurs. It identifies only the changed blocks within a file and sends just those blocks. This dramatically reduces replication bandwidth.

**Staging Folder:** A temporary area where DFSR stages outgoing replication data before transmission and incoming data before applying changes. The staging folder must be large enough for the largest files being replicated.

**Conflict resolution:** DFSR uses a last-writer-wins algorithm for conflicting changes. The losing version is moved to the `DfsrPrivate\ConflictAndDeleted` folder on the member that received the conflict.

DFSR is commonly used together with DFSN to both provide a unified namespace AND keep the data behind that namespace synchronized across sites.

---

### [SEGMENT 6 — File Server Resource Manager]

**[SHOW SCREEN: FSRM console showing Quota Management and File Screening Management]**

[Alt-text: File Server Resource Manager console tree showing Quota Management with a 5 GB hard quota on the HR share, and File Screening Management showing an Active Screen blocking Audio and Video file groups.]

**File Server Resource Manager (FSRM)** is a role service that provides three major capabilities:

**Quota Management:**

- Sets limits on how much disk space a folder (or user's home folder) can consume
- **Hard quota:** Prevents writes when the limit is reached — the save fails
- **Soft quota:** Logs an event and can send a notification, but does not block writes
- Quota templates allow consistent quota policies across many folders

**File Screening:**

- **Active Screen:** Actively blocks files matching defined file groups (e.g., Audio and Video, Executables)
- **Passive Screen:** Logs events but does not block — useful for auditing before enforcement
- File groups are predefined collections of file extensions that can be customized

**Storage Reports:**

- Generates reports on disk usage, file type distribution, large files, duplicate files
- Can be scheduled to run automatically and emailed to administrators

---

### [SEGMENT 7 — Volume Shadow Copies (Previous Versions)]

**[SHOW SCREEN: Volume Shadow Copy settings on a volume, and Previous Versions tab on a shared folder]**

[Alt-text: The Volume Shadow Copy Service settings dialog showing a schedule of twice-daily snapshots, and the Previous Versions tab of a shared folder showing three restore points from the past week.]

**Shadow Copies of Shared Folders** — also called Previous Versions — are point-in-time snapshots of the data on a volume. When enabled, Windows Server takes snapshots of the entire volume on a schedule.

Shadow Copies enable:

- End users to restore their own accidentally deleted or overwritten files by right-clicking a folder and selecting "Restore previous versions"
- Administrators to recover files without a full backup restoration
- Self-service recovery without IT involvement for common accidental deletions

Key shadow copy facts:

- Shadow copies are stored on the same volume or a separate volume
- Recommended minimum storage: 10% of the volume size
- Maximum of 64 shadow copies per volume; oldest copies are deleted when the limit is reached
- Shadow copies are not a substitute for backup — they protect only against accidental deletion or modification, not hardware failure

---

### [SEGMENT 8 — Print Services Overview]

**[SHOW SCREEN: Print Management console showing print servers, printers, and drivers]**

[Alt-text: Print Management console showing a print server with four shared printers listed, each with a driver name and status column showing Ready or Error.]

**Print Management** is a Windows Server role service (under Print and Document Services) that provides centralized management of all printers and print servers in the domain from a single console.

Key print services concepts:

**Print Server:** A Windows Server (or role on an existing server) that hosts shared printers. Clients connect to the print server share rather than directly to the physical printer. The server handles spooling, driver distribution, and print queue management.

**Printer Driver Distribution:** When a client first connects to a shared printer on a Windows print server, the correct driver is automatically downloaded and installed on the client. This eliminates per-workstation driver installation.

**Publishing printers to AD DS:** Shared printers can be published to Active Directory so users can search for printers by name, location, or capability rather than needing to know the print server name.

**Print Queue Management:** The print queue shows all pending, printing, and error jobs. Administrators can pause, resume, cancel, and reorder jobs from Print Management.

**Printer Pooling:** Multiple physical printers presented as a single shared printer. Jobs are distributed to whichever physical printer is available first.

---

### [SEGMENT 9 — Summary and Part 2 Preview]

**[SHOW SCREEN: Summary slide]**

Part 1 covered SMB file sharing, the critical Share + NTFS permission interaction, DFS Namespaces for unified paths, DFS Replication for content synchronization, File Server Resource Manager for quotas and file screening, Shadow Copies for self-service file recovery, and the Print Management role for centralized printer administration.

In Part 2 we will install and configure a file share using PowerShell, set NTFS permissions, install FSRM, configure a quota and file screen, enable shadow copies, and share a printer through the Print Management console.

---

### Additional Resources

- [SMB file sharing overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview)
- [DFS Namespaces overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview)
- [DFS Replication overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/dfsr-overview)
- [File Server Resource Manager](https://learn.microsoft.com/en-us/windows-server/storage/fsrm/fsrm-overview)
- [Shadow copies of shared folders](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service)

---

*End of Part 1. Continue to Part 2 for demonstrations, PowerShell commands, exam tips, and lab preview.*
