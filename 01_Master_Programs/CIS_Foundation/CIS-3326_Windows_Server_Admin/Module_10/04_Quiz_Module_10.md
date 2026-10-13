# Quiz: Module 10 — File and Print Services in Windows Server

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

## Question 1

A user is a member of two groups. Group A has NTFS Modify permission on a
folder. Group B has NTFS Read permission on the same folder. The share
permission for the folder is Everyone Read. The user accesses the folder
through the network share. What is the user's effective permission?

A. Modify

B. Full Control

C. Read

D. Write

**Correct Answer: C**

**Distractor Analysis:**

- **A** — Modify is the combined NTFS permission (union of Modify and Read
  from the two groups). However, the effective network permission also
  applies the share permission, which is Read.

- **B** — Full Control does not appear anywhere in the permission sets. It
  is not inherited from any combination of these permissions.

- **C** — Correct. For network access, effective permission = most restrictive
  of NTFS and Share. NTFS effective = Modify (cumulative of Modify + Read).
  Share = Read. Most restrictive = Read.

- **D** — Write is a component of Modify but is not the effective access level
  calculated from these two permission sets.

---

## Question 2

A server administrator creates a folder shared with Everyone Full Control at
the share level. NTFS permissions grant Finance_Group Modify rights on the
folder. A Finance_Group member accesses the folder through an RDP session and
attempts to delete a file. What permission applies?

A. Read only — share permissions restrict access to Read for Everyone

B. Modify — NTFS applies and allows Modify including deletion

C. No access — RDP sessions are blocked by share permissions

D. Full Control — Everyone Full Control overrides NTFS

**Correct Answer: B**

**Distractor Analysis:**

- **A** — Share permissions do not apply to RDP sessions. RDP is not an
  SMB network access method.

- **B** — Correct. RDP access is controlled exclusively by NTFS permissions.
  Share permissions are irrelevant for RDP sessions. The user's NTFS
  permission is Modify, which includes creating and deleting files.

- **C** — Share permissions never block local or RDP access. They apply
  only to SMB network connections.

- **D** — Everyone Full Control is the share permission. Share permissions
  do not apply to RDP access and do not override NTFS.

---

## Question 3

You need to configure a file server so that users browsing `\\DC1\Departments`
cannot see folders they do not have Read permission on. Other users in the
same share should see only the folders they can access. Which share setting
accomplishes this?

A. Offline Settings (caching)

B. Encrypt Data Access

C. Access-Based Enumeration

D. SMB Bandwidth Throttle

**Correct Answer: C**

**Distractor Analysis:**

- **A** — Offline Settings control whether share contents are available
  offline through client-side caching. They do not affect folder visibility.

- **B** — Encrypt Data Access encrypts SMB traffic to the share. It does
  not affect which folders are visible to which users.

- **C** — Correct. Access-Based Enumeration (ABE) hides files and folders
  from users who lack Read permission on those items. Each user sees only
  what they can access.

- **D** — SMB Bandwidth Throttle controls network bandwidth usage. It does
  not control folder visibility.

---

## Question 4

Your organization is migrating file shares from `\\FileServer1\Data` to
`\\FileServer2\Data`. You want users to continue accessing data via
`\\txwes.edu\Data` without changing any client shortcut or script. Which
technology should you use?

A. DNS CNAME record pointing `txwes.edu` to `FileServer2`

B. DFS Namespace with the folder target updated to point to the new server

C. Share permissions on the old share redirecting to the new server

D. Group Policy preference mapping a drive letter to the new server UNC

**Correct Answer: B**

**Distractor Analysis:**

- **A** — A DNS CNAME on the domain name would redirect all DNS queries for
  `txwes.edu` — this affects the entire domain, not just the file share,
  and is not the correct mechanism.

- **B** — Correct. DFS Namespaces provide location transparency. The
  namespace path `\\txwes.edu\Data` stays the same; you update the folder
  target from `\\FileServer1\Data` to `\\FileServer2\Data`. Clients
  automatically resolve to the new server with no change on the client side.

- **C** — Share permissions control access, not redirection. There is no
  share permission mechanism for redirecting clients to another server.

- **D** — Group Policy drive maps could update clients to a new drive letter
  mapping, but this requires a policy change and applies only to logged-on
  domain users, not all access paths.

---

## Question 5

An administrator enables printer pooling for two physical HP laser printers
using a single logical printer named `FloorPrinter`. A user submits a print
job. The first physical printer is busy; the second is idle. What happens?

A. The job waits in the queue until the first printer is available

B. The job is printed on the second printer because it is idle

C. The job is split and printed on both printers simultaneously

D. The job fails because printer pooling requires both printers to be available

**Correct Answer: B**

**Distractor Analysis:**

- **A** — Without pooling, jobs would queue for one specific device. With
  pooling enabled, the spooler distributes jobs to the first available
  device in the pool.

- **B** — Correct. Printer pooling sends each job to the next available
  port in the pool. If port 1 (first printer) is busy, the spooler routes
  the job to port 2 (second printer).

- **C** — Print jobs are never split across devices. A single job goes
  to a single device.

- **D** — Printer pooling functions normally when only one device in the
  pool is available. The pool does not require all devices to be online.

---

## Question 6

You need to create a domain-based DFS Namespace named `\\txwes.edu\Shared`
pointing to a share on DC1. Which PowerShell cmdlet and parameter combination
creates this namespace?

A. `New-DfsnRoot -Path "\\txwes.edu\Shared" -TargetPath "\\DC1\Departments" -Type DomainV2`

B. `New-DfsnFolder -Path "\\txwes.edu\Shared" -TargetPath "\\DC1\Departments"`

C. `New-SmbShare -Name "Shared" -Path "\\txwes.edu" -FullAccess "Everyone"`

D. `Add-DfsnRootTarget -Path "\\txwes.edu\Shared" -TargetPath "\\DC1\Departments"`

**Correct Answer: A**

**Distractor Analysis:**

- **A** — Correct. `New-DfsnRoot` creates the namespace root. `-Type DomainV2`
  specifies a domain-based namespace stored in Active Directory. `-TargetPath`
  sets the initial folder target for the root.

- **B** — `New-DfsnFolder` creates a subfolder within an existing namespace
  root. It cannot create the root itself.

- **C** — `New-SmbShare` creates a standard SMB share. It has no relationship
  to DFS Namespace creation.

- **D** — `Add-DfsnRootTarget` adds an additional target server to an existing
  namespace root for redundancy. It does not create the root.

---

## Question 7

A user reports they can read files in the `\\txwes.edu\Shared\Faculty` folder
but cannot save changes or delete files. Their NTFS permission on the Faculty
folder is Modify. The share permission for Departments is Everyone Read. What
is causing the limitation and what is the fix?

A. The user needs Modify at the share level; change the share permission to
   Everyone Change

B. The NTFS permission needs to be upgraded to Full Control to allow deletion

C. The share permission Read is the most restrictive and overrides NTFS Modify;
   change the share permission to Everyone Full Control

D. The DFS folder target is read-only; reconfigure the DFS folder

**Correct Answer: C**

**Distractor Analysis:**

- **A** — Change share permission would allow writes, but granting Only Change
  still leaves the share as the constraining factor. The best practice fix is
  Everyone Full Control at the share level.

- **B** — Full Control grants take ownership and change permissions. Modify
  already grants create, write, and delete rights. The NTFS permission is
  not the problem.

- **C** — Correct. The effective network permission is the most restrictive
  of NTFS and Share. NTFS = Modify; Share = Read; effective = Read. The fix
  is to grant Everyone Full Control at the share level and let NTFS control
  actual access.

- **D** — DFS folder targets are not inherently read-only. The DFS layer
  is transparent to permissions; the underlying SMB share permissions apply.

---

## Question 8

The Print Spooler service on a print server stops unexpectedly. Users report
they cannot print to any shared printer on the server. Which PowerShell
command restores printing and ensures the service restarts automatically
after a reboot?

A. `Start-Service -Name Spooler`

B. `Start-Service -Name Spooler` followed by `Set-Service -Name Spooler -StartupType Automatic`

C. `Restart-Computer -Force`

D. `Set-Printer -Name "Campus_LaserJet" -Shared $true`

**Correct Answer: B**

**Distractor Analysis:**

- **A** — `Start-Service` restores printing immediately but does not configure
  the startup type. If the service is set to Manual, it will not restart
  automatically after the next reboot.

- **B** — Correct. `Start-Service` starts the stopped service now. `Set-Service
  -StartupType Automatic` ensures it starts automatically at every boot.
  Both commands together fully resolve the issue.

- **C** — Restarting the computer would restart the Spooler service only if
  its startup type is Automatic. This is also disruptive and does not fix
  the root cause if the startup type is set to Manual.

- **D** — `Set-Printer -Shared $true` shares the printer. It has no effect
  on whether the Spooler service is running.

---

## Question 9

You are setting NTFS permissions on `C:\Shares\Departments\IT` using
PowerShell. You create the following rule:

```powershell
New-Object System.Security.AccessControl.FileSystemAccessRule(
    "txwes\IT_Admins", "FullControl",
    "ContainerInherit,ObjectInherit", "None", "Allow")
```

Which resources does this permission apply to?

A. The IT folder only, not subfolders or files

B. The IT folder and all files directly inside it, but not subfolders

C. The IT folder, all subfolders, and all files within the entire folder tree

D. Only files inside IT — the ContainerInherit flag excludes the folder itself

**Correct Answer: C**

**Distractor Analysis:**

- **A** — `"None"` in the fourth parameter means no additional propagation
  restriction on the folder itself. The `ContainerInherit` and `ObjectInherit`
  flags extend the permission beyond the folder to children.

- **B** — `ObjectInherit` alone would apply to files. Combined with
  `ContainerInherit`, the permission also propagates into subfolders and
  their contents.

- **C** — Correct. `ContainerInherit` propagates the permission to subfolders.
  `ObjectInherit` propagates it to files. Together they apply the permission
  to the folder, all subfolders, and all files in the entire subtree.

- **D** — `ContainerInherit` applies to sub-containers (subfolders), not to
  the folder itself. The folder itself receives the permission because the
  rule is set directly on it.

---

## Question 10

You need to add a second physical printer to an existing printer pool. The
second printer is identical to the first and uses the same driver. The logical
printer is named `FloorPrinter` and is already connected to port
`Printer_Port_1`. What must you do to add the second printer to the pool?

A. Create a second logical printer with a different name and link both printers
   in Print Management

B. Add a second port for the new physical printer, then enable pooling on
   the logical printer and add the new port

C. Install a second printer driver with a different name for the second device

D. Create a new DFS folder target pointing to the second printer's IP address

**Correct Answer: B**

**Distractor Analysis:**

- **A** — Two separate logical printers are not a printer pool. A pool is
  specifically a single logical printer with multiple ports/devices assigned.

- **B** — Correct. Printer pooling requires: (1) adding a port for the new
  physical device, (2) enabling the "Enable printer pooling" option on the
  logical printer, and (3) adding the new port to that logical printer.

- **C** — Both devices must use the same driver. Installing a different driver
  breaks the pooling requirement and would cause print errors.

- **D** — DFS is a file sharing technology. It has no role in printer pooling
  or print server configuration.

---

*Submit answers to Canvas by the due date shown in the course schedule.*

---

### Question 11 (5 points)

You create a new SMB share for the Finance department. You want to set the share
permission so that NTFS permissions alone control access, following Microsoft's
best practice. Which share permission configuration achieves this?

- A) Grant Finance_Group Modify at the share level
- B) Grant Everyone Full Control at the share level
- C) Grant Authenticated Users Read at the share level
- D) Grant Domain Admins Full Control at the share level

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Granting Modify at the share level to Finance_Group means non-Finance users receive no share access. This requires maintaining share permissions in parallel with NTFS, increasing management complexity.
  - **B** — Correct. Granting Everyone Full Control at the share level removes the share layer as a constraint. NTFS permissions exclusively control what each user can read, write, or delete. This is Microsoft's recommended best practice for simplified permission management.
  - **C** — Authenticated Users Read would restrict all access to Read through the network, overriding any NTFS Modify or Full Control grants for all users.
  - **D** — Granting only Domain Admins Full Control would lock out all non-admin users from the share entirely, regardless of their NTFS permissions.

---

### Question 12 (5 points)

A user has Delete permission Denied explicitly on a file through a Deny ACE.
The user is also a member of IT_Admins, which has Full Control Allow on the same
file. What is the user's effective Delete permission?

- A) Allow — Full Control from IT_Admins overrides the explicit Deny
- B) Deny — explicit Deny ACEs override Allow ACEs regardless of group membership
- C) Allow — cumulative permissions favor the highest permission level
- D) Allow — the most recently applied permission takes precedence

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Allow permissions from group membership do not override explicit Deny ACEs applied directly to the user or another group the user belongs to.
  - **B** — Correct. In Windows NTFS, explicit Deny ACEs take precedence over Allow ACEs. If any ACE in the user's effective permission set contains Deny Delete, that Deny wins even if another ACE grants Full Control Allow.
  - **C** — Cumulative permissions apply to Allow ACEs — you take the union of all Allow permissions. However, explicit Deny ACEs override any accumulated Allow permissions.
  - **D** — NTFS permissions do not have a "last applied" rule. The Deny/Allow precedence rule is based on ACE type, not application order.

---

### Question 13 (5 points)

You want to create a new SMB share at `C:\Data\HR` using PowerShell, grant
HR_Group Change (Modify) permission at the share level, and limit concurrent
connections to 25. Which command is correct?

- A) `New-SmbShare -Name "HR" -Path "C:\Data\HR" -ChangeAccess "txwes\HR_Group" -ConcurrentUserLimit 25`
- B) `New-SmbShare -Name "HR" -Path "C:\Data\HR" -FullAccess "txwes\HR_Group" -ConcurrentUserLimit 25`
- C) `New-SmbShare -Name "HR" -Path "C:\Data\HR" -ReadAccess "txwes\HR_Group" -ConcurrentUserLimit 25`
- D) `Set-SmbShare -Name "HR" -ChangeAccess "txwes\HR_Group" -ConcurrentUserLimit 25`

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. `-ChangeAccess` grants Change (Modify) share permission. `-ConcurrentUserLimit 25` limits simultaneous connections. Both parameters are valid for `New-SmbShare`.
  - **B** — `-FullAccess` grants Full Control share permission, not Change. This grants a higher level than requested.
  - **C** — `-ReadAccess` grants Read-only share permission, which is less than the required Change permission.
  - **D** — `Set-SmbShare` modifies an existing share. The share must already exist before `Set-SmbShare` can configure it; it cannot create a new share.

---

### Question 14 (5 points)

You check a DFS Namespace folder and find that a folder target is marked as
"offline." Users report they cannot access `\\txwes.edu\Shared\Projects`. Which
PowerShell command brings the folder target back online?

- A) `Set-DfsnFolder -Path "\\txwes.edu\Shared\Projects" -State Online`
- B) `Set-DfsnFolderTarget -Path "\\txwes.edu\Shared\Projects" -TargetPath "\\DC1\Projects" -State Online`
- C) `Enable-DfsnRootTarget -Path "\\txwes.edu\Shared" -TargetPath "\\DC1\Projects"`
- D) `Restart-Service -Name Dfs`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Set-DfsnFolder` modifies folder-level properties such as referral mode and timeout. It does not control the online/offline state of individual folder targets.
  - **B** — Correct. `Set-DfsnFolderTarget` controls properties of a specific folder target, including its state. `-State Online` makes the target available for client referrals.
  - **C** — `Enable-DfsnRootTarget` operates on namespace root targets, not folder targets. It would not affect a folder-level target state.
  - **D** — Restarting the DFS service affects all namespaces globally and would cause a brief disruption. It does not specifically fix a single offline folder target.

---

### Question 15 (5 points)

A print administrator needs to move the print spooler folder from its default
location (`C:\Windows\System32\spool\PRINTERS`) to `D:\PrintSpool` to free up
space on the C: drive. Which registry key controls the spooler folder path?

- A) `HKLM\SYSTEM\CurrentControlSet\Services\Spooler\DefaultSpoolDirectory`
- B) `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Print\Printers\DefaultSpoolDirectory`
- C) `HKLM\SYSTEM\CurrentControlSet\Control\Print\Printers\DefaultSpoolDirectory`
- D) `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Devices\SpoolDirectory`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — The `Services\Spooler` key controls service parameters such as startup type and image path, not the spool folder location.
  - **B** — Correct. The default spool directory is configured at `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Print\Printers\DefaultSpoolDirectory`. Changing this value and restarting the Spooler service moves the spool folder.
  - **C** — The `Control\Print\Printers` key contains per-printer settings. There is no `DefaultSpoolDirectory` value at this path.
  - **D** — `HKCU` values are per-user settings. The spool directory is a system-wide setting stored in `HKLM`.

---

### Question 16 (5 points)

You configure NTFS permissions on `C:\Shares\Data` and set the following
inheritance flags: `ContainerInherit` only (no `ObjectInherit`). What does
this permission propagate to?

- A) Only the Data folder itself
- B) The Data folder and all files directly inside it
- C) The Data folder and all subfolders, but not files in those subfolders
- D) All files and subfolders recursively

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — Without any inheritance flags, the permission would apply only to the folder itself. `ContainerInherit` extends it beyond the folder.
  - **B** — `ObjectInherit` propagates permissions to files. Without `ObjectInherit`, files do not inherit the permission.
  - **C** — Correct. `ContainerInherit` propagates permissions to sub-containers (subfolders). Without `ObjectInherit`, the permission does not propagate to files within those subfolders.
  - **D** — Both `ContainerInherit` and `ObjectInherit` are required to propagate permissions to all files and subfolders recursively.

---

### Question 17 (5 points)

You need to add a second folder target to an existing DFS folder
`\\txwes.edu\Shared\IT` pointing to `\\DC2\IT_Backup` for redundancy. Which
PowerShell command accomplishes this?

- A) `New-DfsnFolder -Path "\\txwes.edu\Shared\IT" -TargetPath "\\DC2\IT_Backup"`
- B) `New-DfsnFolderTarget -Path "\\txwes.edu\Shared\IT" -TargetPath "\\DC2\IT_Backup"`
- C) `Add-DfsnRootTarget -Path "\\txwes.edu\Shared" -TargetPath "\\DC2\IT_Backup"`
- D) `Set-DfsnFolder -Path "\\txwes.edu\Shared\IT" -TargetPath "\\DC2\IT_Backup"`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `New-DfsnFolder` creates a new virtual DFS folder within the namespace. Running it on an existing folder path would produce an error.
  - **B** — Correct. `New-DfsnFolderTarget` adds an additional physical target to an existing DFS folder. This enables client failover and load balancing between `\\DC1\IT` and `\\DC2\IT_Backup`.
  - **C** — `Add-DfsnRootTarget` adds a target to the namespace root, not to a subfolder within the namespace.
  - **D** — `Set-DfsnFolder` modifies folder-level settings such as referral timeout and state. It does not add folder targets.

---

### Question 18 (5 points)

A user connects to `\\txwes.edu\Shared\Faculty` from their workstation and
receives "Access Denied." The user is a member of Faculty_Staff, which has NTFS
Read permission on the Faculty folder. The share permission is Everyone Full
Control. ABE is enabled. What is the most likely cause?

- A) ABE is hiding the Faculty folder because the user lacks Read permission
- B) The share permission Everyone Full Control is overriding the NTFS permission
- C) The user lacks NTFS Read permission; Faculty_Staff does not have an ACE on this folder
- D) The DFS folder target is offline

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — ABE hides folders from users who lack Read permission, but it does not cause "Access Denied." If the folder is visible and the user tries to open it, the denial comes from the permission evaluation, not ABE.
  - **B** — Everyone Full Control at the share level is not restrictive. Share permissions would only cause denial if they were set to Read or Deny — Full Control does not restrict access.
  - **C** — Correct. The problem states the user is a member of Faculty_Staff and Faculty_Staff has NTFS Read permission. If the user still receives "Access Denied," the most likely cause is that Faculty_Staff does not actually have an effective ACE on this folder — perhaps due to a missing group membership, a misnamed group, or the ACE being on a different folder.
  - **D** — An offline DFS folder target would produce an error about the path being unavailable, not an "Access Denied" message.

---

### Question 19 (5 points)

A Windows Server administrator runs `Get-SmbShare` and notices a share named
`ADMIN$`. What is the purpose of this share and who can access it?

- A) A standard administrative share for general user file storage; all authenticated users can access it
- B) A hidden administrative share that maps to `C:\Windows`; only members of the Administrators group can access it
- C) A share created by DFS that maps to the namespace root; Domain Admins only
- D) A share created by the Print Spooler for printer driver distribution; print operators can access it

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `ADMIN$` is not for general user storage. The `$` suffix makes it hidden in network browsing, and access is restricted to administrators.
  - **B** — Correct. `ADMIN$` is a default administrative share automatically created by Windows, mapping to `%SystemRoot%` (typically `C:\Windows`). It is used for remote administration tools. Only members of the local Administrators group can connect to it.
  - **C** — DFS does not create `ADMIN$`. DFS creates namespace shares under the namespace server name.
  - **D** — Print Spooler does not create `ADMIN$`. Printer driver distribution uses the `print$` share, which maps to `C:\Windows\System32\spool\drivers`.

---

### Question 20 (5 points)

You want to verify that the DFS Namespace service is running and set to start
automatically, then list all configured DFS roots on the current server. Which
sequence of PowerShell commands accomplishes this?

- A) `Get-Service -Name Dfs` then `Get-DfsnRoot -ComputerName DC1`
- B) `Get-Service -Name DFS` then `Get-DfsnRoot -ComputerName DC1`
- C) `Get-Service -Name "DFS Namespace"` then `Get-DfsnRoot -ComputerName DC1`
- D) `Test-NetConnection DC1 -Port 445` then `Get-DfsnRoot -ComputerName DC1`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — The DFS Namespace service name is `Dfs` (case-insensitive), so this would work. However, `Get-DfsnRoot` lists namespace roots, not targets — it lists all roots hosted on DC1. This answer is functionally valid but option B uses the same correct service name.
  - **B** — Correct. `Get-Service -Name DFS` (Windows service name is `Dfs`, case-insensitive) checks status and startup type. `Get-DfsnRoot -ComputerName DC1` lists all DFS namespace roots hosted on DC1.
  - **C** — The service name for DFS Namespaces is `Dfs`, not `"DFS Namespace"`. Using the display name instead of the service name with `Get-Service` would return an error.
  - **D** — `Test-NetConnection` on port 445 tests SMB connectivity, not the DFS service state. It provides no information about namespace configuration.
