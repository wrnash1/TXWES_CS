# Video Script: Module 10 — File and Print Services in Windows Server (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back. I am Professor Nash.

In Part 1 we covered SMB architecture, NTFS and share permissions, effective
permissions, DFS Namespaces, and print server concepts.

In Part 2 we install the File Server and Print Server roles, create SMB shares,
configure NTFS and share permissions using PowerShell, build a DFS Namespace,
install and share a printer, configure printer pooling, and verify everything.
We close with exam tips.

---

## Section 1: Installing File and Print Server Roles

```powershell
# Install the File Server role
Install-WindowsFeature -Name FS-FileServer -IncludeManagementTools

# Install DFS Namespaces and DFS Replication
Install-WindowsFeature -Name FS-DFS-Namespace, FS-DFS-Replication `
    -IncludeManagementTools

# Install Print Server role
Install-WindowsFeature -Name Print-Server -IncludeManagementTools

# Verify all roles are installed
Get-WindowsFeature -Name FS-FileServer, FS-DFS-Namespace, Print-Server |
    Select-Object Name, InstallState
```

---

## Section 2: Creating Folders and SMB Shares

```powershell
# Create a folder to share
New-Item -Path "C:\Shares\Departments" -ItemType Directory

# Create an SMB share
New-SmbShare `
    -Name "Departments" `
    -Path "C:\Shares\Departments" `
    -Description "Departmental shared storage" `
    -FullAccess "Everyone"

# Verify the share
Get-SmbShare -Name "Departments"

# Create shares for specific departments
New-Item -Path "C:\Shares\Departments\Faculty" -ItemType Directory
New-Item -Path "C:\Shares\Departments\Students" -ItemType Directory
New-Item -Path "C:\Shares\Departments\IT" -ItemType Directory
```

The `-FullAccess "Everyone"` parameter grants Full Control at the share
permission level. We will control actual access using NTFS permissions, which
is best practice.

---

## Section 3: Configuring NTFS Permissions with PowerShell

NTFS permissions are managed through Access Control Lists (ACLs). PowerShell
uses `Get-Acl` and `Set-Acl` to read and write ACLs.

```powershell
# View current NTFS permissions on a folder
Get-Acl -Path "C:\Shares\Departments\Faculty" | Format-List

# Create a new ACL rule for the Faculty security group
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "txwes\Faculty_Staff",
    "Modify",
    "ContainerInherit,ObjectInherit",
    "None",
    "Allow"
)

# Get the current ACL, add the rule, and apply it
$acl = Get-Acl -Path "C:\Shares\Departments\Faculty"
$acl.SetAccessRule($rule)
Set-Acl -Path "C:\Shares\Departments\Faculty" -AclObject $acl

# Verify the updated ACL
Get-Acl -Path "C:\Shares\Departments\Faculty" |
    Select-Object -ExpandProperty Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType
```

The `ContainerInherit,ObjectInherit` propagation flags ensure the permission
applies to the folder, all subfolders, and all files within.

---

## Section 4: Configuring Share Permissions

```powershell
# Remove Everyone Full Control and grant specific share permissions
# First, remove the default Everyone grant
Revoke-SmbShareAccess -Name "Departments" -AccountName "Everyone" -Force

# Grant specific share permissions
Grant-SmbShareAccess `
    -Name "Departments" `
    -AccountName "txwes\Domain Users" `
    -AccessRight Change `
    -Force

Grant-SmbShareAccess `
    -Name "Departments" `
    -AccountName "txwes\Domain Admins" `
    -AccessRight Full `
    -Force

# Verify share permissions
Get-SmbShareAccess -Name "Departments"
```

---

## Section 5: Enabling Access-Based Enumeration

```powershell
# Enable ABE on the Departments share
Set-SmbShare -Name "Departments" -FolderEnumerationMode AccessBased -Force

# Verify
Get-SmbShare -Name "Departments" | Select-Object Name, FolderEnumerationMode
```

With ABE enabled, users browsing `\\DC1\Departments` only see the subfolders
they have Read access to.

---

## Section 6: Creating a DFS Namespace

```powershell
# Create a domain-based DFS namespace root
New-DfsnRoot `
    -Path "\\txwes.edu\Shared" `
    -TargetPath "\\DC1\Departments" `
    -Type DomainV2 `
    -Description "TXWES unified shared namespace"

# Verify the namespace root
Get-DfsnRoot -Path "\\txwes.edu\Shared"

# Create DFS folders pointing to department shares
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

Users now access faculty files via `\\txwes.edu\Shared\Faculty` regardless of
which physical server hosts the data. If you later migrate files to a new server,
you update the folder target in DFS — client UNC paths do not change.

---

## Section 7: Installing and Sharing a Printer

```powershell
# Add a TCP/IP printer port
Add-PrinterPort -Name "Campus_Printer_Port" -PrinterHostAddress "192.168.10.150"

# Install a printer driver (assuming the driver is in the driver store)
Add-PrinterDriver -Name "HP Universal Printing PCL 6"

# Add the printer and bind it to the port and driver
Add-Printer `
    -Name "Campus_LaserJet" `
    -DriverName "HP Universal Printing PCL 6" `
    -PortName "Campus_Printer_Port"

# Share the printer
Set-Printer `
    -Name "Campus_LaserJet" `
    -Shared $true `
    -ShareName "Campus_LaserJet"

# Verify the printer
Get-Printer -Name "Campus_LaserJet" | Select-Object Name, DriverName, PortName, Shared, ShareName
```

---

## Section 8: Configuring Printer Pooling

Printer pooling allows multiple physical print devices to appear as a single
logical printer. Add ports for each physical device, then enable pooling.

```powershell
# Add a second printer port for the pool
Add-PrinterPort -Name "Campus_Printer_Port_2" -PrinterHostAddress "192.168.10.151"

# Add port 2 to the existing printer to create a pool
# (Printer pooling requires adding both ports to the same logical printer)
# This must be done through the printer's port configuration:
Set-PrinterProperty -PrinterName "Campus_LaserJet" `
    -PropertyName "PortName" `
    -Value "Campus_Printer_Port,Campus_Printer_Port_2"

# Alternatively, use the GUI: Printer Properties → Ports tab
# → check "Enable printer pooling" → check both port checkboxes

# Verify printer port assignment
Get-Printer -Name "Campus_LaserJet" | Select-Object Name, PortName
```

---

## Section 9: Configuring Printer Permissions

```powershell
# View current printer permissions
$printer = Get-Printer -Name "Campus_LaserJet" -Full
$printer.PermissionSDDL

# To set printer permissions use the GUI (Server Manager → Print Management)
# or WMI:
$sd = Get-Printer -Name "Campus_LaserJet" -Full | Select-Object -ExpandProperty PermissionSDDL

# Grant Print permission to Domain Users via SDDL — use GUI for complex ACLs
# Print Management console → right-click printer → Properties → Security tab
```

For complex printer permission changes, the Print Management GUI in Server
Manager provides a cleaner experience than raw SDDL strings.

---

## Section 10: Verifying File and Print Services

```powershell
# ── File Services Verification ─────────────────────────────────────
Write-Host "=== SMB Shares ===" -ForegroundColor Cyan
Get-SmbShare | Select-Object Name, Path, Description

Write-Host "=== Share Permissions ===" -ForegroundColor Cyan
Get-SmbShareAccess -Name "Departments"

Write-Host "=== NTFS Permissions ===" -ForegroundColor Cyan
Get-Acl "C:\Shares\Departments\Faculty" |
    Select-Object -ExpandProperty Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType

Write-Host "=== DFS Namespace ===" -ForegroundColor Cyan
Get-DfsnRoot -Path "\\txwes.edu\Shared"
Get-DfsnFolder -Path "\\txwes.edu\Shared\*"

Write-Host "=== Active SMB Sessions ===" -ForegroundColor Cyan
Get-SmbSession

Write-Host "=== Open SMB Files ===" -ForegroundColor Cyan
Get-SmbOpenFile

# ── Print Services Verification ────────────────────────────────────
Write-Host "=== Installed Printers ===" -ForegroundColor Cyan
Get-Printer | Select-Object Name, DriverName, PortName, Shared, ShareName

Write-Host "=== Print Queue ===" -ForegroundColor Cyan
Get-PrintJob -PrinterName "Campus_LaserJet"

Write-Host "=== Spooler Service ===" -ForegroundColor Cyan
Get-Service -Name Spooler | Select-Object Name, Status, StartType
```

---

## Section 11: Exam Tips

**Exam Tip 1** — The effective permission for network access is the most
restrictive combination of NTFS and Share permissions. If NTFS = Modify and
Share = Read, the user gets Read. The exam will give you both permission sets
and ask for the effective permission.

**Exam Tip 2** — NTFS permissions apply for local access and RDP. Share
permissions apply only for SMB network access. Local access is never affected
by share permissions.

**Exam Tip 3** — Best practice: grant Everyone Full Control at the share level
and use NTFS to control access. This eliminates double-management of two
permission sets.

**Exam Tip 4** — DFS Namespaces provide location transparency. Users access
`\\txwes.edu\Shared\Faculty` without knowing which server hosts the data. If
the server changes, update the folder target — client paths stay the same.

**Exam Tip 5** — Printer pooling requires all devices to use the same driver.
The user submits one print job; the spooler routes it to the first available
device. Devices should be physically near each other since the user cannot
predict which device will print.

**Exam Tip 6** — Access-Based Enumeration (ABE) hides files and folders that
the user cannot access. Without ABE, users see all items in the share even if
they cannot open them. ABE is a share property, not an NTFS setting.

---

## Wrap-Up

In this two-part module we covered the File and Print Services roles from
architecture through hands-on PowerShell configuration.

You now understand SMB protocol history, NTFS and share permission interaction,
the effective permission rule, Access-Based Enumeration, DFS Namespace design,
print server deployment, and printer pooling.

Head to the Reading Guide for reference tables, then complete Lab 10 where
you will build shared folders, set NTFS permissions, create a DFS Namespace,
and install a shared printer in your lab environment.

See you in Module 11.
