# Quiz: Module 07 - File and Print Services

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

An administrator shares a folder named `HR_Docs` on the network. The Share permissions give the `HR_Group` Read-Only access. The NTFS permissions on the folder give `HR_Group` Full Control. When a member of `HR_Group` accesses the folder over the network, what is their effective permission?

A) Full Control, because NTFS permissions are always more granular and take precedence over Share permissions.
B) Read-Only, because when accessing a share over the network, the most restrictive combination of Share and NTFS permissions applies.
C) Write-Only, because the Write component of Full Control combines with Read to produce Write-Only over the network.
D) No Access, because conflicting permissions between Share and NTFS result in a deny condition.

* **Correct Answer:** B) Read-Only, because when accessing a share over the network, the most restrictive combination of Share and NTFS permissions applies.
* **Distractor Analysis:**
  * *Why A is incorrect:* NTFS permissions do not unconditionally override Share permissions for network access. The effective network permission is the most restrictive result of both permission sets evaluated independently.
  * *Why C is incorrect:* There is no "Write-Only" effective permission in Windows; permissions are not arithmetically combined. The restrictive rule produces Read (from Share) as the effective network permission.
  * *Why D is incorrect:* There is no conflict resulting in denial here. Both permissions grant access — Share grants Read and NTFS grants Full Control. The most restrictive result is Read, not No Access.

---

### Question 2

A company has two file servers in different cities. Users must access both servers' content under a single unified path without knowing which physical server hosts each folder. Which Windows Server technology creates this unified namespace?

A) DFS Replication (DFSR), which synchronizes folder contents across servers and presents them under a single path.
B) File Server Resource Manager (FSRM), which consolidates multiple server shares into a single browsable folder structure.
C) DFS Namespaces (DFSN), which creates a virtual folder hierarchy that maps a single UNC path to shares hosted on multiple underlying servers.
D) Storage Replica, which mirrors storage volumes between servers and publishes them under a single share path.

* **Correct Answer:** C) DFS Namespaces (DFSN), which creates a virtual folder hierarchy that maps a single UNC path to shares hosted on multiple underlying servers.
* **Distractor Analysis:**
  * *Why A is incorrect:* DFSR replicates folder contents to keep servers synchronized but does not create a unified namespace. Users would still see separate server share paths without DFSN providing the virtual namespace layer.
  * *Why B is incorrect:* FSRM manages storage quotas and file screening policies on individual file servers. It has no capability to aggregate or abstract share paths across multiple servers.
  * *Why D is incorrect:* Storage Replica performs block-level volume replication for disaster recovery and high availability — it does not create or manage SMB namespace paths that abstract underlying server locations from users.

---

### Question 3

An administrator wants to prevent users from saving MP3 and MP4 media files to a departmental file share, while still allowing all other file types. Which File Server Resource Manager (FSRM) feature accomplishes this?

A) FSRM Quota Management configured with a hard quota that limits the maximum file size to prevent large media files.
B) FSRM File Screening configured with an Active Screen that blocks files matching the Audio and Video file group.
C) NTFS permissions configured to deny Write access to files with .mp3 and .mp4 extensions.
D) A Group Policy Software Restriction Policy that prevents media players from running on the file server.

* **Correct Answer:** B) FSRM File Screening configured with an Active Screen that blocks files matching the Audio and Video file group.
* **Distractor Analysis:**
  * *Why A is incorrect:* Quota Management limits the total amount of disk space consumed by a folder or user — it does not filter by file type or extension. A quota would not prevent a small MP3 file from being saved if the quota limit had not been reached.
  * *Why C is incorrect:* NTFS permissions operate on security principals (users/groups) and inheritance — they cannot be applied conditionally based on file extension. There is no NTFS mechanism to deny Write specifically for files ending in .mp3.
  * *Why D is incorrect:* A Software Restriction Policy controls which applications can run on a computer. Restricting media players from running on the file server does not prevent users from copying media files to a share from their own workstations.

---

### Question 4

An organization's print server hosts a high-volume shared printer. Users frequently complain that print jobs submitted during peak hours are lost or never complete. Which Print Management action should the administrator take to investigate the issue?

A) Increase the printer's port speed settings in Device Manager to allow faster data transfer to the physical printer.
B) Open Print Management, navigate to the shared printer, and examine the print queue for stalled or error-state jobs that are blocking the queue.
C) Reinstall the printer driver on every client workstation to ensure they are submitting jobs in the correct format.
D) Enable the "Keep printed documents" option on the printer properties so that completed jobs remain in the queue for review.

* **Correct Answer:** B) Open Print Management, navigate to the shared printer, and examine the print queue for stalled or error-state jobs that are blocking the queue.
* **Distractor Analysis:**
  * *Why A is incorrect:* Printer port speed in Device Manager applies to physical local port communication speeds (such as parallel ports) — it has no relevance for a network-connected print server where jobs are spooled and transmitted over TCP/IP.
  * *Why C is incorrect:* Reinstalling drivers on all client workstations is a broad, disruptive action that does not address the root cause. A stalled print queue on the server affects all clients regardless of their local driver version.
  * *Why D is incorrect:* "Keep printed documents" retains completed jobs in the queue for resubmission — it is a useful feature but does not diagnose or resolve a stalled queue caused by an error-state job blocking subsequent submissions.

---

### Question 5

A junior administrator accidentally deleted all files from a shared folder on a Windows Server file server. The server has Shadow Copies (Previous Versions) enabled on the volume. What is the fastest method to restore the deleted files without involving a full backup restoration?

A) Run Windows Server Backup and perform a bare-metal recovery of the entire server to restore the folder.
B) Right-click the shared folder in Windows Explorer, select "Restore previous versions," and choose a shadow copy taken before the deletion to restore the files.
C) Use `Robocopy` with the `/MIR` flag to mirror the folder contents from a second file server that was not affected.
D) Contact Microsoft Support to recover the deleted files from the server's transaction log.

* **Correct Answer:** B) Right-click the shared folder in Windows Explorer, select "Restore previous versions," and choose a shadow copy taken before the deletion to restore the files.
* **Distractor Analysis:**
  * *Why A is incorrect:* Bare-metal recovery restores the entire server OS and all volumes — an extreme action for recovering a deleted folder on a running server. Shadow Copies provide a targeted, fast recovery path that does not require taking the server offline.
  * *Why C is incorrect:* Robocopy with `/MIR` mirrors a source to a destination by making them identical, including deletions — running `/MIR` from a second server would replicate the deletion to the second server if they are in sync, not restore the deleted files.
  * *Why D is incorrect:* Microsoft Support does not recover deleted files from Windows Server transaction logs (NTFS does not expose a user-accessible undo log for deleted files). Shadow Copies are the correct first-response tool when enabled.
