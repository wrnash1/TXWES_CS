# Lab Activity: Module 07 - File and Print Services

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Lab Overview

In this lab you will install the File Server and FSRM role services on DC1, create and configure a shared folder with NTFS permissions, set up a 5 GB hard quota, create an Active File Screen blocking executables, enable Shadow Copies on the C: volume, create a DFS namespace, and share a printer through the Print Management console.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 06 lab complete: corp.local domain with DNS and DHCP configured
- DC1 is running at `192.168.10.10`
- PowerShell running as Domain Administrator

**Learning Objectives:**

- Install File Server role services and FSRM using PowerShell
- Create an SMB share and configure Share and NTFS permissions
- Create an FSRM quota and file screen
- Enable Volume Shadow Copies on a volume
- Create a domain-based DFS namespace with a folder target
- Install the Print Services role and share a printer

---

### Part 1 — Install Role Services

#### Step 1.1 — Install File Server, DFS, and FSRM

```powershell
# Install File Server, DFS Namespaces, DFS Replication, and FSRM
Install-WindowsFeature `
    -Name FS-FileServer, FS-DFS-Namespace, FS-DFS-Replication, FS-Resource-Manager `
    -IncludeManagementTools

# Verify installation
Get-WindowsFeature -Name FS-FileServer, FS-DFS-Namespace, FS-DFS-Replication, FS-Resource-Manager |
    Select-Object Name, InstallState
```

All four features should show `InstallState: Installed`.

#### Step 1.2 — Install Print Services

```powershell
# Install Print and Document Services role
Install-WindowsFeature -Name Print-Services -IncludeManagementTools

# Verify
Get-WindowsFeature -Name Print-Services | Select-Object Name, InstallState
```

Take **Screenshot 1** — PowerShell showing all five role services as Installed.

---

### Part 2 — Create a Shared Folder with NTFS and Share Permissions

#### Step 2.1 — Create the Folder and Share

```powershell
# Create the directory
New-Item -Path "C:\Shares\HR_Docs" -ItemType Directory -Force

# Create the SMB share
# Share permissions: Domain Admins = Full Control, HR_Group = Read
New-SmbShare `
    -Name "HR_Docs" `
    -Path "C:\Shares\HR_Docs" `
    -Description "HR Department Documents" `
    -FullAccess "CORP\Domain Admins" `
    -ReadAccess "CORP\HR_Group"

# Verify the share
Get-SmbShare -Name "HR_Docs" | Select-Object Name, Path, Description
Get-SmbShareAccess -Name "HR_Docs"
```

#### Step 2.2 — Configure NTFS Permissions

```powershell
# View current NTFS ACL
(Get-Acl -Path "C:\Shares\HR_Docs").Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType

# Remove inherited permissions and set explicit NTFS ACL
$acl = Get-Acl -Path "C:\Shares\HR_Docs"

# Add HR_Group with Modify rights (inherited through subfolders and files)
$ruleHR = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "CORP\HR_Group",
    "Modify",
    "ContainerInherit,ObjectInherit",
    "None",
    "Allow"
)
$acl.AddAccessRule($ruleHR)

# Add Domain Admins with Full Control
$ruleAdmin = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "CORP\Domain Admins",
    "FullControl",
    "ContainerInherit,ObjectInherit",
    "None",
    "Allow"
)
$acl.AddAccessRule($ruleAdmin)
Set-Acl -Path "C:\Shares\HR_Docs" -AclObject $acl

# Verify NTFS permissions
(Get-Acl -Path "C:\Shares\HR_Docs").Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType
```

**Effective permission analysis:** Share = Read for HR_Group, NTFS = Modify for HR_Group. Most restrictive = Read. HR_Group members accessing `\\DC1\HR_Docs` over the network will have Read access.

Take **Screenshot 2** — NTFS permissions output showing HR_Group with Modify rights.

---

### Part 3 — Configure FSRM Quota and File Screen

#### Step 3.1 — Create a Hard Quota

```powershell
# Create a 5 GB hard quota on the HR_Docs share folder
New-FsrmQuota `
    -Path "C:\Shares\HR_Docs" `
    -Size 5GB `
    -SoftLimit $false `
    -Description "5 GB hard quota — HR Documents"

# Verify the quota
Get-FsrmQuota -Path "C:\Shares\HR_Docs" |
    Select-Object Path, Size, SoftLimit, Description
```

The `-SoftLimit $false` parameter creates a hard quota. Setting it to `$true` would create a soft quota.

#### Step 3.2 — Create an Active File Screen

```powershell
# List available file groups to confirm the group name
Get-FsrmFileGroup | Select-Object Name

# Create an Active File Screen blocking executable files
New-FsrmFileScreen `
    -Path "C:\Shares\HR_Docs" `
    -IncludeGroup "Executable Files" `
    -Active $true

# Verify the file screen
Get-FsrmFileScreen -Path "C:\Shares\HR_Docs" |
    Select-Object Path, Active, IncludeGroup
```

Test the file screen by attempting to copy an `.exe` file to `C:\Shares\HR_Docs`. The copy should fail with an access error.

Take **Screenshot 3** — FSRM console or PowerShell output showing the quota and file screen on HR_Docs.

---

### Part 4 — Enable Volume Shadow Copies

#### Step 4.1 — Enable Shadow Copies via Computer Management

Shadow Copies are typically configured through the GUI. On DC1:

1. Open **Computer Management** (right-click Start > Computer Management)
2. Expand **Storage** > right-click **Disk Management** then navigate to the C: volume
3. Alternatively: right-click **Local Disk (C:)** in File Explorer > Properties > Shadow Copies tab
4. Select volume **C:** and click **Enable**
5. Click **Settings** — verify storage is set to at least 10% of the C: volume
6. Click **Create Now** to take an immediate shadow copy

#### Step 4.2 — Verify with PowerShell

```powershell
# View current shadow copies on C:
vssadmin list shadows /for=C:

# View shadow copy storage allocation
vssadmin list shadowstorage /for=C:
```

#### Step 4.3 — Test Previous Versions Recovery

1. Create a test file: `New-Item -Path "C:\Shares\HR_Docs\test_file.txt" -Value "Original content"`
2. Create another shadow copy: From Computer Management > Shadow Copies > Create Now
3. Delete the test file: `Remove-Item "C:\Shares\HR_Docs\test_file.txt"`
4. Right-click `C:\Shares\HR_Docs` in File Explorer > Properties > Previous Versions tab
5. Select a shadow copy and click Restore

Take **Screenshot 4** — Shadow Copies configuration showing at least one shadow copy of C:.

---

### Part 5 — Create a DFS Namespace

#### Step 5.1 — Create the Namespace Root Folder on DC1

```powershell
# Create the physical folder for the namespace root
New-Item -Path "C:\DFSRoots\Files" -ItemType Directory -Force

# Create an SMB share for the namespace root
New-SmbShare -Name "Files" -Path "C:\DFSRoots\Files" `
    -FullAccess "CORP\Domain Admins" -ReadAccess "Everyone"
```

#### Step 5.2 — Create the Domain-Based Namespace

```powershell
# Create a domain-based DFS namespace
New-DfsnRoot `
    -Path "\\corp.local\Files" `
    -TargetPath "\\DC1\Files" `
    -Type DomainV2 `
    -Description "Corporate file namespace"

# Verify the namespace root
Get-DfsnRoot -Path "\\corp.local\Files"
```

#### Step 5.3 — Add a Folder to the Namespace

```powershell
# Add the HR folder pointing to the HR_Docs share
New-DfsnFolder `
    -Path "\\corp.local\Files\HR" `
    -TargetPath "\\DC1\HR_Docs" `
    -Description "HR Department Documents"

# Verify the folder
Get-DfsnFolder -Path "\\corp.local\Files\*"
```

#### Step 5.4 — Test the Namespace

```powershell
# Test access via the namespace path
Test-Path "\\corp.local\Files\HR"

# List folder contents through the namespace
Get-ChildItem "\\corp.local\Files\HR"
```

Take **Screenshot 5** — `Get-DfsnFolder` output showing the HR folder target in the corp.local\Files namespace.

---

### Part 6 — Share a Printer

#### Step 6.1 — Add a Printer Port and Printer

In a lab environment without a physical printer, we will add a virtual or generic printer to practice the configuration.

```powershell
# Add a generic TCP/IP printer port (the IP may not resolve — this is expected in lab)
Add-PrinterPort -Name "IP_192.168.10.50" -PrinterHostAddress "192.168.10.50"

# Install a generic printer driver (if not already present, use Generic/Text Only)
# First, list available drivers to find one that works in your lab
Get-PrinterDriver | Select-Object Name

# Add a shared, AD-published printer
Add-Printer `
    -Name "Lab_Network_Printer" `
    -DriverName "Generic / Text Only" `
    -PortName "IP_192.168.10.50" `
    -Shared $true `
    -ShareName "LabPrinter" `
    -Published $true

# Verify
Get-Printer -Name "Lab_Network_Printer" | Select-Object Name, ShareName, Published, DriverName
```

Take **Screenshot 6** — `Get-Printer` output showing the shared, published printer.

---

### Part 7 — PowerShell Summary Verification

```powershell
Write-Host "=== SMB Shares ===" -ForegroundColor Cyan
Get-SmbShare | Where-Object { $_.Name -notlike "*$" } | Select-Object Name, Path

Write-Host "=== FSRM Quotas ===" -ForegroundColor Cyan
Get-FsrmQuota | Select-Object Path, Size, SoftLimit

Write-Host "=== FSRM File Screens ===" -ForegroundColor Cyan
Get-FsrmFileScreen | Select-Object Path, Active, IncludeGroup

Write-Host "=== DFS Namespace Folders ===" -ForegroundColor Cyan
Get-DfsnFolder -Path "\\corp.local\Files\*"

Write-Host "=== Printers ===" -ForegroundColor Cyan
Get-Printer | Select-Object Name, ShareName, Published
```

Take **Screenshot 7** — Full PowerShell summary output.

---

### Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1 — Role installation:** PowerShell showing all five role services as Installed.

**Screenshot 2 — NTFS permissions:** PowerShell output showing HR_Group with Modify rights on HR_Docs.

**Screenshot 3 — FSRM quota and file screen:** FSRM console or PowerShell output showing quota and file screen on C:\Shares\HR_Docs.

**Screenshot 4 — Shadow Copies:** Shadow Copy configuration showing at least one shadow copy of C:.

**Screenshot 5 — DFS namespace:** `Get-DfsnFolder` output showing the HR folder target in the namespace.

**Screenshot 6 — Shared printer:** `Get-Printer` output showing the shared, published printer.

**Screenshot 7 — PowerShell summary:** Full summary output from Part 7.

---

### Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| Role services installed | 10 | Screenshot 1 shows all services as Installed |
| Share created with correct permissions | 20 | Screenshot 2 shows HR_Group NTFS Modify rights |
| FSRM quota and file screen configured | 25 | Screenshot 3 shows hard quota and Active file screen |
| Shadow Copies enabled | 15 | Screenshot 4 shows shadow copy of C: |
| DFS namespace with folder target | 20 | Screenshot 5 shows namespace folder mapped to HR_Docs share |
| Printer shared and published | 10 | Screenshot 6 shows shared, published printer |

---

### Troubleshooting Notes

If `New-FsrmFileScreen` fails with "File group not found," list available groups with `Get-FsrmFileGroup` and use an exact group name from that list.

If `New-DfsnRoot` fails with "The namespace already exists," verify whether a namespace was created previously:

```powershell
Get-DfsnRoot | Select-Object Path, State
```

If shadow copies are not visible in the Previous Versions tab, verify that the Volume Shadow Copy service is running:

```powershell
Get-Service -Name VSS | Select-Object Status, StartType
```
