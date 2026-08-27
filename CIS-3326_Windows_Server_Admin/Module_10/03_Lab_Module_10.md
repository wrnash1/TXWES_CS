# Lab Activity: Module 10 — File and Print Services in Windows Server

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Lab Overview

In this lab you will install the File Server and Print Server roles on DC1,
create SMB shares with NTFS permissions, configure Access-Based Enumeration,
build a domain-based DFS Namespace with three folder targets, install and
share a network printer, and verify everything with PowerShell.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 09 lab complete: DC1 is a domain controller for txwes.edu with DNS
  and DHCP configured

- DC1 IP address: 192.168.10.10

- Security groups exist: Faculty_Staff, IT_Admins, Domain Users

- PowerShell running as Domain Administrator

**Learning Objectives:**

- Install the FS-FileServer and Print-Server roles

- Create SMB shares and configure share permissions

- Apply NTFS permissions using `Get-Acl` and `Set-Acl`

- Enable Access-Based Enumeration on a share

- Create a domain-based DFS Namespace with multiple folder targets

- Install, share, and verify a network printer

---

## Part 1 — Install File and Print Server Roles

### Step 1.1 — Install Roles

```powershell
# Install File Server and DFS roles
Install-WindowsFeature `
    -Name FS-FileServer, FS-DFS-Namespace, FS-DFS-Replication `
    -IncludeManagementTools

# Install Print Server role
Install-WindowsFeature -Name Print-Server -IncludeManagementTools

# Verify installations
Get-WindowsFeature -Name FS-FileServer, FS-DFS-Namespace, Print-Server |
    Select-Object Name, InstallState
```

Take **Screenshot 1** — `Get-WindowsFeature` output showing all three roles
with InstallState: Installed.

---

## Part 2 — Create Folders and SMB Shares

### Step 2.1 — Create the Folder Structure

```powershell
# Create the shared folder hierarchy
New-Item -Path "C:\Shares\Departments" -ItemType Directory
New-Item -Path "C:\Shares\Departments\Faculty" -ItemType Directory
New-Item -Path "C:\Shares\Departments\Students" -ItemType Directory
New-Item -Path "C:\Shares\Departments\IT" -ItemType Directory

# Verify folder structure
Get-ChildItem -Path "C:\Shares\Departments"
```

### Step 2.2 — Create and Configure the SMB Share

```powershell
# Create the share with Everyone Full Control at the share level
New-SmbShare `
    -Name "Departments" `
    -Path "C:\Shares\Departments" `
    -Description "TXWES departmental shared storage" `
    -FullAccess "Everyone"

# Enable Access-Based Enumeration
Set-SmbShare -Name "Departments" -FolderEnumerationMode AccessBased -Force

# Verify the share
Get-SmbShare -Name "Departments" |
    Select-Object Name, Path, Description, FolderEnumerationMode

# View share permissions
Get-SmbShareAccess -Name "Departments"
```

Take **Screenshot 2** — `Get-SmbShare` output showing Departments share with
AccessBased enumeration, and `Get-SmbShareAccess` showing Everyone Full Control.

---

## Part 3 — Configure NTFS Permissions

### Step 3.1 — Set NTFS Permissions on Subfolders

```powershell
# Grant Faculty_Staff Modify on the Faculty subfolder
$ruleF = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "txwes\Faculty_Staff",
    "Modify",
    "ContainerInherit,ObjectInherit",
    "None",
    "Allow"
)
$aclF = Get-Acl -Path "C:\Shares\Departments\Faculty"
$aclF.SetAccessRule($ruleF)
Set-Acl -Path "C:\Shares\Departments\Faculty" -AclObject $aclF

# Grant Domain Users Read on the Students subfolder
$ruleS = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "txwes\Domain Users",
    "ReadAndExecute",
    "ContainerInherit,ObjectInherit",
    "None",
    "Allow"
)
$aclS = Get-Acl -Path "C:\Shares\Departments\Students"
$aclS.SetAccessRule($ruleS)
Set-Acl -Path "C:\Shares\Departments\Students" -AclObject $aclS

# Grant IT_Admins Full Control on the IT subfolder
$ruleI = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "txwes\IT_Admins",
    "FullControl",
    "ContainerInherit,ObjectInherit",
    "None",
    "Allow"
)
$aclI = Get-Acl -Path "C:\Shares\Departments\IT"
$aclI.SetAccessRule($ruleI)
Set-Acl -Path "C:\Shares\Departments\IT" -AclObject $aclI
```

### Step 3.2 — Verify NTFS Permissions

```powershell
# Verify Faculty folder NTFS permissions
Get-Acl -Path "C:\Shares\Departments\Faculty" |
    Select-Object -ExpandProperty Access |
    Where-Object {$_.IdentityReference -like "txwes*"} |
    Select-Object IdentityReference, FileSystemRights, AccessControlType

# Verify Students folder
Get-Acl -Path "C:\Shares\Departments\Students" |
    Select-Object -ExpandProperty Access |
    Where-Object {$_.IdentityReference -like "txwes*"} |
    Select-Object IdentityReference, FileSystemRights, AccessControlType
```

Take **Screenshot 3** — NTFS permission output for Faculty and Students
folders showing correct group assignments and rights levels.

---

## Part 4 — Create a DFS Namespace

### Step 4.1 — Create the Namespace Root

```powershell
# Create a domain-based DFS namespace root
New-DfsnRoot `
    -Path "\\txwes.edu\Shared" `
    -TargetPath "\\DC1\Departments" `
    -Type DomainV2 `
    -Description "TXWES unified shared namespace"

# Verify the namespace root
Get-DfsnRoot -Path "\\txwes.edu\Shared"
```

### Step 4.2 — Add DFS Folders

```powershell
# Add folder targets for each department
New-DfsnFolder `
    -Path "\\txwes.edu\Shared\Faculty" `
    -TargetPath "\\DC1\Departments\Faculty" `
    -Description "Faculty department storage"

New-DfsnFolder `
    -Path "\\txwes.edu\Shared\Students" `
    -TargetPath "\\DC1\Departments\Students" `
    -Description "Student department storage"

New-DfsnFolder `
    -Path "\\txwes.edu\Shared\IT" `
    -TargetPath "\\DC1\Departments\IT" `
    -Description "IT department storage"

# List all DFS folders in the namespace
Get-DfsnFolder -Path "\\txwes.edu\Shared\*"
```

### Step 4.3 — Test DFS Access

```powershell
# Test that DFS namespace resolves
Test-Path -Path "\\txwes.edu\Shared"
Get-ChildItem -Path "\\txwes.edu\Shared"
```

Take **Screenshot 4** — `Get-DfsnRoot` and `Get-DfsnFolder` output showing
the namespace root and all three folder targets configured.

---

## Part 5 — Install and Share a Printer

### Step 5.1 — Add a Printer Port

```powershell
# Add a TCP/IP printer port for the campus printer
Add-PrinterPort -Name "Campus_LaserJet_Port" -PrinterHostAddress "192.168.10.150"

# Verify the port was created
Get-PrinterPort | Where-Object {$_.Name -like "Campus*"}
```

### Step 5.2 — Install a Printer Driver

```powershell
# List available printer drivers in the driver store
Get-PrinterDriver | Select-Object Name

# Install the Microsoft XPS Document Writer driver as a substitute
# (In a real environment, install the vendor driver from media)
Add-PrinterDriver -Name "Microsoft XPS Document Writer v4"

# Verify
Get-PrinterDriver -Name "Microsoft XPS Document Writer v4"
```

### Step 5.3 — Add and Share the Printer

```powershell
# Add the printer
Add-Printer `
    -Name "Campus_LaserJet" `
    -DriverName "Microsoft XPS Document Writer v4" `
    -PortName "Campus_LaserJet_Port"

# Share the printer
Set-Printer `
    -Name "Campus_LaserJet" `
    -Shared $true `
    -ShareName "Campus_LaserJet"

# Verify
Get-Printer -Name "Campus_LaserJet" |
    Select-Object Name, DriverName, PortName, Shared, ShareName
```

Take **Screenshot 5** — `Get-Printer` output showing Campus_LaserJet as
shared with ShareName and PortName confirmed.

---

## Part 6 — Verification Summary

```powershell
Write-Host "=== Installed Roles ===" -ForegroundColor Cyan
Get-WindowsFeature -Name FS-FileServer, FS-DFS-Namespace, Print-Server |
    Select-Object Name, InstallState

Write-Host "=== SMB Shares ===" -ForegroundColor Cyan
Get-SmbShare | Select-Object Name, Path, FolderEnumerationMode

Write-Host "=== Share Permissions: Departments ===" -ForegroundColor Cyan
Get-SmbShareAccess -Name "Departments"

Write-Host "=== NTFS: Faculty folder ===" -ForegroundColor Cyan
Get-Acl "C:\Shares\Departments\Faculty" |
    Select-Object -ExpandProperty Access |
    Where-Object {$_.IdentityReference -notlike "NT*" -and
                  $_.IdentityReference -notlike "BUILTIN*"} |
    Select-Object IdentityReference, FileSystemRights

Write-Host "=== DFS Namespace ===" -ForegroundColor Cyan
Get-DfsnRoot -Path "\\txwes.edu\Shared"
Get-DfsnFolder -Path "\\txwes.edu\Shared\*" |
    Select-Object Path, State

Write-Host "=== Printers ===" -ForegroundColor Cyan
Get-Printer | Select-Object Name, DriverName, Shared, ShareName

Write-Host "=== Spooler Service ===" -ForegroundColor Cyan
Get-Service -Name Spooler | Select-Object Name, Status, StartType
```

Take **Screenshot 6** — Full verification summary output showing all roles,
shares, permissions, DFS folders, and printer active.

---

## Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1** — File Server, DFS Namespace, and Print Server roles
showing InstallState: Installed.

**Screenshot 2** — Departments share with AccessBased enumeration and
Everyone Full Control share permission.

**Screenshot 3** — NTFS permissions showing Faculty_Staff Modify on Faculty
and Domain Users Read on Students.

**Screenshot 4** — DFS namespace root and three DFS folder targets configured.

**Screenshot 5** — Campus_LaserJet printer shared with correct ShareName.

**Screenshot 6** — Full verification summary.

---

## Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| Roles installed | 10 | Screenshot 1 shows all three roles installed |
| Share and ABE configured | 15 | Screenshot 2 shows share and ABE mode |
| NTFS permissions | 20 | Screenshot 3 shows correct NTFS for Faculty and Students |
| DFS Namespace | 25 | Screenshot 4 shows namespace root and all three folders |
| Printer shared | 15 | Screenshot 5 shows printer shared correctly |
| Verification summary | 15 | Screenshot 6 shows all services active |

---

## Troubleshooting Notes

If `New-DfsnRoot` fails with "The namespace already exists," check for an
existing namespace and remove it:

```powershell
Remove-DfsnRoot -Path "\\txwes.edu\Shared" -Force
```

If a user cannot access a shared folder over the network, verify effective
permissions. Share = Read and NTFS = Modify yields Read for network access.

If the Print Spooler service is stopped, no printers will work:

```powershell
Start-Service -Name Spooler
Set-Service -Name Spooler -StartupType Automatic
```

If `Add-PrinterPort` fails because the port already exists, remove it first:

```powershell
Remove-PrinterPort -Name "Campus_LaserJet_Port"
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Configure and Verify NTFS Auditing on a Shared Folder

NTFS auditing records who accessed or attempted to access files and folders.
Enable auditing on the Faculty share and verify that access events appear in
the Security event log.

1. Enable the Object Access audit policy on DC1 so that NTFS audit entries are
   written to the Security log:

   ```powershell
   auditpol /set /subcategory:"File System" /success:enable /failure:enable
   auditpol /get /subcategory:"File System"
   ```

2. Configure a SACL (System Access Control List) on the Faculty folder to audit
   all access attempts by Domain Users:

   ```powershell
   $acl   = Get-Acl -Path "C:\Shares\Departments\Faculty"
   $audit = New-Object System.Security.AccessControl.FileSystemAuditRule(
       "Domain Users",
       "ReadData,WriteData,Delete",
       "ContainerInherit,ObjectInherit",
       "None",
       "Success,Failure"
   )
   $acl.AddAuditRule($audit)
   Set-Acl -Path "C:\Shares\Departments\Faculty" -AclObject $acl
   ```

3. Simulate access by opening a file in the Faculty folder (you can use
   `Get-Content` or `notepad` to trigger a read event), then query the Security
   log for File System audit events:

   ```powershell
   Get-WinEvent -FilterHashtable @{
       LogName   = "Security"
       Id        = 4663
   } | Select-Object TimeCreated, Message -First 10
   ```

   In your lab notes, identify the Subject Account Name, Object Name, and
   Accesses fields from one event. Explain what each field tells you.

4. Verify the audit rule is present on the SACL:

   ```powershell
   (Get-Acl -Path "C:\Shares\Departments\Faculty" -Audit).Audit |
       Select-Object IdentityReference, FileSystemRights, AuditFlags
   ```

### Challenge 2: Configure DFS Replication Between Two Folder Targets

DFS Replication (DFSR) keeps folder targets on multiple servers synchronized.
Configure replication between DC1 and a second server so that changes on either
server propagate to the other.

1. Install the DFS Replication role on DC1 and DC2:

   ```powershell
   Install-WindowsFeature -Name FS-DFS-Replication -IncludeManagementTools -ComputerName DC1
   Install-WindowsFeature -Name FS-DFS-Replication -IncludeManagementTools -ComputerName DC2
   ```

2. Create a replication group named `TXWES_Faculty_Replication` with DC1 as the
   primary member:

   ```powershell
   New-DfsReplicationGroup -GroupName "TXWES_Faculty_Replication"

   Add-DfsrMember -GroupName "TXWES_Faculty_Replication" -ComputerName DC1
   Add-DfsrMember -GroupName "TXWES_Faculty_Replication" -ComputerName DC2

   New-DfsReplicatedFolder -GroupName "TXWES_Faculty_Replication" `
       -FolderName "Faculty"

   Set-DfsrMembership -GroupName   "TXWES_Faculty_Replication" `
       -FolderName   "Faculty" `
       -ComputerName DC1 `
       -ContentPath  "C:\Shares\Departments\Faculty" `
       -PrimaryMember $true

   Set-DfsrMembership -GroupName   "TXWES_Faculty_Replication" `
       -FolderName   "Faculty" `
       -ComputerName DC2 `
       -ContentPath  "C:\Shares\Departments\Faculty"
   ```

3. Create a bidirectional replication connection and trigger initial replication:

   ```powershell
   Add-DfsrConnection -GroupName "TXWES_Faculty_Replication" `
       -SourceComputerName DC1 `
       -DestinationComputerName DC2

   Update-DfsrConfigurationFromAD -ComputerName DC1
   Update-DfsrConfigurationFromAD -ComputerName DC2
   ```

4. Verify replication health and confirm both members are in a healthy state:

   ```powershell
   Get-DfsrState -ComputerName DC1 -Verbose
   Get-DfsrMembership -GroupName "TXWES_Faculty_Replication" |
       Select-Object ComputerName, FolderName, ContentPath, PrimaryMember, State
   ```

   In your lab notes, describe what happens to a file created on DC1 after
   replication completes. What would happen if a user modifies the same file
   on both servers simultaneously before replication runs?

### Reflection Questions

1. You configured NTFS auditing on the Faculty folder to track Delete events.
   After a week, a faculty member reports that a file was deleted by an unknown
   user. Describe the complete process for finding the deletion event in the
   Security log, including which Event ID to search for, which fields identify
   the user who deleted the file, and what information would be missing if the
   Object Access audit policy had not been enabled before the deletion occurred.

2. DFS Replication uses a "last writer wins" conflict resolution model when two
   members modify the same file before replication synchronizes. A file called
   `syllabus.docx` is edited on DC1 at 9:00 AM and on DC2 at 9:05 AM before
   either change replicates. Which version survives, and where does DFSR store
   the losing version? Describe a workflow policy you would implement for shared
   documents to prevent simultaneous edit conflicts in a multi-site DFS
   Replication environment.
