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
