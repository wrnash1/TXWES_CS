# Quiz: Module 07 - File and Print Services

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. Review your Reading Guide and video notes before beginning.

---

### Question 1

An administrator shares a folder named `HR_Docs` on the network. The Share permissions give the `HR_Group` Read-Only access. The NTFS permissions on the folder give `HR_Group` Full Control. When a member of `HR_Group` accesses the folder over the network, what is their effective permission?

A) Full Control, because NTFS permissions are always more granular and take precedence over Share permissions.

B) Read-Only, because when accessing a share over the network, the most restrictive combination of Share and NTFS permissions applies.

C) Write-Only, because the Write component of Full Control combines with Read to produce Write-Only over the network.

D) No Access, because conflicting permissions between Share and NTFS result in a deny condition.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: NTFS permissions do not unconditionally override Share permissions for network access. The effective network permission is the most restrictive result of both permission sets evaluated independently.
  - Why C is incorrect: There is no "Write-Only" effective permission in Windows. Permissions are not arithmetically combined. The restrictive rule produces Read (from Share) as the effective network permission.
  - Why D is incorrect: There is no conflict resulting in denial here. Both permissions grant access — Share grants Read and NTFS grants Full Control. The most restrictive result is Read, not No Access.

---

### Question 2

A company has two file servers in different cities. Users must access both servers' content under a single unified path without knowing which physical server hosts each folder. Which Windows Server technology creates this unified namespace?

A) DFS Replication (DFSR), which synchronizes folder contents across servers and presents them under a single path.

B) File Server Resource Manager (FSRM), which consolidates multiple server shares into a single browsable folder structure.

C) DFS Namespaces (DFSN), which creates a virtual folder hierarchy that maps a single UNC path to shares hosted on multiple underlying servers.

D) Storage Replica, which mirrors storage volumes between servers and publishes them under a single share path.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: DFSR replicates folder contents to keep servers synchronized but does not create a unified namespace. Users would still see separate server share paths without DFSN providing the virtual namespace layer.
  - Why B is incorrect: FSRM manages storage quotas and file screening policies on individual file servers. It has no capability to aggregate or abstract share paths across multiple servers.
  - Why D is incorrect: Storage Replica performs block-level volume replication for disaster recovery and high availability. It does not create or manage SMB namespace paths.

---

### Question 3

An administrator wants to prevent users from saving MP3 and MP4 media files to a departmental file share, while still allowing all other file types. Which File Server Resource Manager (FSRM) feature accomplishes this?

A) FSRM Quota Management configured with a hard quota that limits the maximum file size to prevent large media files.

B) FSRM File Screening configured with an Active Screen that blocks files matching the Audio and Video file group.

C) NTFS permissions configured to deny Write access to files with .mp3 and .mp4 extensions.

D) A Group Policy Software Restriction Policy that prevents media players from running on the file server.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Quota Management limits the total amount of disk space consumed — it does not filter by file type or extension. A small MP3 file would still be saved if the quota limit had not been reached.
  - Why C is incorrect: NTFS permissions operate on security principals (users/groups) and cannot be applied conditionally based on file extension. There is no NTFS mechanism to deny Write specifically for `.mp3` files.
  - Why D is incorrect: A Software Restriction Policy controls which applications can run on a computer. Restricting media players from the file server does not prevent users from copying media files to a share from their workstations.

---

### Question 4

An organization's print server hosts a high-volume shared printer. Users frequently complain that print jobs submitted during peak hours are lost or never complete. Which Print Management action should the administrator take to investigate the issue?

A) Increase the printer's port speed settings in Device Manager to allow faster data transfer to the physical printer.

B) Open Print Management, navigate to the shared printer, and examine the print queue for stalled or error-state jobs that are blocking the queue.

C) Reinstall the printer driver on every client workstation to ensure they are submitting jobs in the correct format.

D) Enable the "Keep printed documents" option on the printer properties so that completed jobs remain in the queue for review.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Printer port speed in Device Manager applies to physical local port communication speeds. It has no relevance for a network-connected print server where jobs are spooled and transmitted over TCP/IP.
  - Why C is incorrect: Reinstalling drivers on all client workstations is a broad, disruptive action that does not address the root cause. A stalled print queue on the server affects all clients regardless of their local driver version.
  - Why D is incorrect: "Keep printed documents" retains completed jobs for resubmission — it is a useful feature but does not diagnose or resolve a stalled queue caused by an error-state job.

---

### Question 5

A junior administrator accidentally deleted all files from a shared folder on a Windows Server file server. The server has Shadow Copies (Previous Versions) enabled on the volume. What is the fastest method to restore the deleted files without involving a full backup restoration?

A) Run Windows Server Backup and perform a bare-metal recovery of the entire server to restore the folder.

B) Right-click the shared folder in Windows Explorer, select "Restore previous versions," and choose a shadow copy taken before the deletion to restore the files.

C) Use `Robocopy` with the `/MIR` flag to mirror the folder contents from a second file server that was not affected.

D) Contact Microsoft Support to recover the deleted files from the server's transaction log.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Bare-metal recovery restores the entire server OS and all volumes — an extreme action for recovering a deleted folder on a running server. Shadow Copies provide a targeted, fast recovery path.
  - Why C is incorrect: Robocopy with `/MIR` mirrors a source to a destination by making them identical, including deletions. Running `/MIR` from a second server in sync would replicate the deletion, not restore the deleted files.
  - Why D is incorrect: Microsoft Support does not recover deleted files from Windows Server transaction logs. NTFS does not expose a user-accessible undo log for deleted files. Shadow Copies are the correct first-response tool.

---

### Question 6

An administrator sets Share permissions on a folder to Full Control for Authenticated Users and configures NTFS permissions giving `G_Finance` the Read right and `G_FinanceManagers` the Modify right. A Finance Manager accesses the folder over the network. What is their effective permission?

A) Full Control, because the Share permission grants Full Control to all authenticated users.

B) Read, because NTFS Read is more restrictive than Share Full Control for all Finance users.

C) Modify, because the NTFS Modify right for G_FinanceManagers takes effect against Share Full Control, and Modify is the most restrictive of the two.

D) No Access, because the conflicting group memberships in G_Finance and G_FinanceManagers create a permission conflict.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Share Full Control is evaluated against the NTFS permission. The most restrictive of the two applies. The Finance Manager's NTFS right is Modify, which is more restrictive than Full Control, so Modify is the effective permission.
  - Why B is incorrect: The Finance Manager is a member of `G_FinanceManagers`, which has NTFS Modify — not just `G_Finance` with Read. NTFS permissions for multiple group memberships are cumulative (Read + Modify = Modify). The effective NTFS right is Modify, which is the most restrictive against Share Full Control.
  - Why D is incorrect: Multiple group memberships in NTFS do not create a conflict. NTFS cumulates the allow permissions across group memberships unless there is an explicit Deny. Read + Modify = Modify for NTFS.

---

### Question 7

A company stores HR files on `\\FS-NYC\HR` and Finance files on `\\FS-LA\Finance`. After implementing DFS Namespaces with a domain-based root at `\\corp.local\Files`, users report that they can still reach the old paths directly. What does this indicate?

A) DFS Namespaces replaced the original share paths, and users are receiving cached referrals to old paths.

B) DFS Namespaces creates an additional access path (the namespace path) without removing or blocking the original share paths.

C) The DFS Replication engine has not yet synchronized the files to the namespace server, so users fall back to the old paths.

D) The domain-based namespace requires users to update their mapped drives before the old paths become inaccessible.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: DFS Namespaces does not remove or disable the underlying share paths. Both the namespace path and the original share path remain accessible.
  - Why C is incorrect: DFS Replication synchronizes folder content — it does not affect whether original share paths are accessible. DFSN and DFSR are independent components.
  - Why D is incorrect: Users do not need to update mapped drives for the original paths to work. The original share paths continue to function regardless of the DFS namespace configuration.

---

### Question 8

An administrator creates an FSRM quota with a 10 GB limit and `-SoftLimit $true`. A user saves files that bring the folder to 11 GB. What happens?

A) The write fails and the user receives an "insufficient disk space" error once the 10 GB limit is reached.

B) The write succeeds and the user's file is saved. The FSRM quota logs an event and can send a notification, but does not block the write.

C) The folder is automatically taken offline until the administrator manually removes files to bring it below 10 GB.

D) Windows compresses existing files automatically to make room for the new file without exceeding the quota.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A soft quota (SoftLimit $true) does not block writes. Only a hard quota (SoftLimit $false) prevents writes when the limit is reached.
  - Why C is incorrect: FSRM never takes a folder offline. A soft quota can trigger notifications or reports but has no mechanism to restrict access to the folder itself.
  - Why D is incorrect: FSRM quota management does not trigger file compression. Windows file system compression is a separate, unrelated feature and is not invoked by FSRM quota activity.

---

### Question 9

When a Windows client first connects to a shared printer hosted on a Windows Server print server, which process occurs automatically that eliminates the need for per-workstation printer driver installation?

A) The client downloads and installs the printer driver from the print server's driver store.

B) The client connects directly to the physical printer's embedded web server to retrieve the driver.

C) Windows Update automatically pushes the correct driver to the client based on the printer model detected in AD DS.

D) The client uses the Generic/Text Only driver that is installed with Windows by default for all network printers.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: The client connects to the print server share, not the physical printer's embedded web server. Driver distribution is a function of the Windows print server role.
  - Why C is incorrect: Windows Update can deliver drivers, but that is not the mechanism used for print server driver distribution. The print server's local driver store is the source, not Windows Update.
  - Why D is incorrect: While a Generic driver exists, Windows print servers distribute the specific driver for the shared printer model — not a generic fallback. The correct model-specific driver is downloaded automatically.

---

### Question 10

An administrator needs to create a DFS Namespace that remains available even if one of the namespace servers fails. The namespace path should be `\\corp.local\CompanyFiles`. Which namespace type and PowerShell parameter combination is correct?

A) `New-DfsnRoot -Path "\\corp.local\CompanyFiles" -TargetPath "\\DC1\CompanyFiles" -Type Standalone`

B) `New-DfsnRoot -Path "\\corp.local\CompanyFiles" -TargetPath "\\DC1\CompanyFiles" -Type DomainV2`

C) `New-DfsnRoot -Path "\\SRV-FS-01\CompanyFiles" -TargetPath "\\DC1\CompanyFiles" -Type DomainV2`

D) `New-DfsnRoot -Path "\\corp.local\CompanyFiles" -TargetPath "\\DC1\CompanyFiles" -Type Domain`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `-Type Standalone` creates a stand-alone namespace stored on a single server — it is not fault-tolerant. The namespace path starts with the server name, not the domain name.
  - Why C is incorrect: A domain-based namespace path must start with the domain name (`\\corp.local`), not a server name. Using `\\SRV-FS-01` would create a stand-alone path format, not a domain-based one.
  - Why D is incorrect: `-Type Domain` creates a domain-based namespace using the older DFS Namespace v1 format. `-Type DomainV2` is the current recommended type for Windows Server 2008 R2 and later domains, providing improved performance and scalability.
