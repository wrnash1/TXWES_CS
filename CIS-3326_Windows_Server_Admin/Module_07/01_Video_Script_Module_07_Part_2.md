# Video Script: Module 07 - File and Print Services (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 07 - File and Print Services

**Part:** 2 of 2 — Demonstrations, PowerShell Commands, Exam Tips, and Lab Preview

**Estimated Duration:** 11 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Recap and Demo Overview]

Welcome back to Module 07. In Part 1 we covered SMB file sharing, the Share + NTFS permission interaction, DFS Namespaces and Replication, FSRM quotas and file screening, Shadow Copies, and Print Management. In Part 2 I will demonstrate creating and configuring a file share with PowerShell, setting NTFS permissions, installing FSRM, configuring a quota and file screen, enabling shadow copies, and walking through Print Management.

---

### [SEGMENT 2 — Demo: Install File Services Role and Create a Share]

**[SHOW SCREEN: PowerShell console on Windows Server]**

[Alt-text: PowerShell console showing Install-WindowsFeature and New-SmbShare commands with output confirming share creation.]

```powershell
# Install File Server role with management tools
Install-WindowsFeature -Name FS-FileServer -IncludeManagementTools

# Install DFS Namespaces and DFS Replication
Install-WindowsFeature -Name FS-DFS-Namespace, FS-DFS-Replication -IncludeManagementTools

# Install File Server Resource Manager
Install-WindowsFeature -Name FS-Resource-Manager -IncludeManagementTools

# Verify installation
Get-WindowsFeature -Name FS-FileServer, FS-DFS-Namespace, FS-DFS-Replication, FS-Resource-Manager |
    Select-Object Name, InstallState

# Create the share directory
New-Item -Path "C:\Shares\HR_Docs" -ItemType Directory -Force

# Create an SMB share
New-SmbShare `
    -Name "HR_Docs" `
    -Path "C:\Shares\HR_Docs" `
    -Description "HR Department Documents" `
    -FullAccess "CORP\Domain Admins" `
    -ReadAccess "CORP\HR_Group"

# Verify the share
Get-SmbShare -Name "HR_Docs" | Select-Object Name, Path, Description
```

---

### [SEGMENT 3 — Demo: Configure NTFS Permissions]

**[SHOW SCREEN: PowerShell showing NTFS ACL configuration]**

[Alt-text: PowerShell console showing Get-Acl and Set-Acl commands setting NTFS permissions on the HR_Docs folder.]

```powershell
# Get the current NTFS ACL
$acl = Get-Acl -Path "C:\Shares\HR_Docs"

# Create a new access rule: HR_Group gets Modify rights, inherited
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "CORP\HR_Group",
    "Modify",
    "ContainerInherit,ObjectInherit",
    "None",
    "Allow"
)

# Add the rule and apply it
$acl.SetAccessRule($rule)
Set-Acl -Path "C:\Shares\HR_Docs" -AclObject $acl

# Verify NTFS permissions
(Get-Acl -Path "C:\Shares\HR_Docs").Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType
```

With Share permissions set to Read for HR_Group and NTFS permissions set to Modify, the effective network permission is Read — the most restrictive of the two.

---

### [SEGMENT 4 — Demo: FSRM Quota and File Screen]

**[SHOW SCREEN: PowerShell showing FSRM quota and file screen commands]**

[Alt-text: PowerShell console showing New-FsrmQuota and New-FsrmFileScreen commands with confirmation output.]

```powershell
# Create a 5 GB hard quota on the HR share
New-FsrmQuota `
    -Path "C:\Shares\HR_Docs" `
    -Size 5GB `
    -SoftLimit $false `
    -Description "5 GB hard quota for HR Documents share"

# Verify quota
Get-FsrmQuota -Path "C:\Shares\HR_Docs"

# Create a file screen blocking audio and video files (Active screen)
New-FsrmFileScreen `
    -Path "C:\Shares\HR_Docs" `
    -IncludeGroup "Audio and Video Files" `
    -Active $true

# Verify file screen
Get-FsrmFileScreen -Path "C:\Shares\HR_Docs"
```

The `-Active $true` parameter creates an Active Screen that blocks the file types. Setting `-Active $false` would create a Passive Screen that only logs events without blocking.

---

### [SEGMENT 5 — Demo: Enable Volume Shadow Copies]

**[SHOW SCREEN: PowerShell showing shadow copy configuration]**

[Alt-text: PowerShell console showing vssadmin and New-ScheduledTask commands for configuring Volume Shadow Copy Service on a volume.]

```powershell
# Enable shadow copies on C: volume
# This is typically done through the GUI, but can be scripted:
$volume = "C:"

# Check current shadow copy status
vssadmin list shadows /for=$volume

# Create a shadow copy immediately
vssadmin create shadow /for=$volume

# To configure scheduled shadow copies via GUI:
# Right-click the volume in Computer Management > Configure Shadow Copies
# Set schedule (default: 7:00 AM and 12:00 PM daily)
# Set storage limit (recommended: 10% of volume size)

# View all shadow copies
vssadmin list shadows

# Restore from shadow copy — from the client side
# Right-click folder > Properties > Previous Versions tab
```

---

### [SEGMENT 6 — Demo: Create a DFS Namespace]

**[SHOW SCREEN: PowerShell showing DFS namespace creation commands]**

[Alt-text: PowerShell console showing New-DfsnRoot and New-DfsnFolder commands creating a domain-based DFS namespace.]

```powershell
# Create a domain-based DFS namespace root
New-DfsnRoot `
    -Path "\\corp.local\Files" `
    -TargetPath "\\DC1\Files" `
    -Type DomainV2 `
    -Description "Corporate file namespace"

# Add a folder to the namespace pointing to the HR share
New-DfsnFolder `
    -Path "\\corp.local\Files\HR" `
    -TargetPath "\\DC1\HR_Docs" `
    -Description "HR Department Documents"

# Verify the namespace
Get-DfsnRoot -Path "\\corp.local\Files"
Get-DfsnFolder -Path "\\corp.local\Files\*"
```

Users can now access `\\corp.local\Files\HR` and be transparently redirected to `\\DC1\HR_Docs`.

---

### [SEGMENT 7 — Demo: Print Management]

**[SHOW SCREEN: Print Management console showing adding a printer and sharing it]**

[Alt-text: Print Management console with the Add Printer Wizard open, showing a network printer being added and its share name configured as HR_Printer.]

```powershell
# Install Print and Document Services role
Install-WindowsFeature -Name Print-Services -IncludeManagementTools

# Add a local printer port (for a network printer connected via TCP/IP)
Add-PrinterPort -Name "IP_192.168.10.50" -PrinterHostAddress "192.168.10.50"

# Add a printer using the port
Add-Printer `
    -Name "HR_HP_LaserJet" `
    -DriverName "HP LaserJet Universal Printing PCL 6" `
    -PortName "IP_192.168.10.50" `
    -Shared $true `
    -ShareName "HR_Printer" `
    -Published $true

# Verify the printer
Get-Printer -Name "HR_HP_LaserJet" | Select-Object Name, ShareName, Published, DriverName
```

The `-Published $true` parameter publishes the printer to Active Directory so users can search for it in ADUC.

---

### [SEGMENT 8 — Exam Tips]

**[SHOW SCREEN: Exam tips slide for Module 07]**

**Exam Tip 1:** The most restrictive permission rule. When a user accesses a share over the network, evaluate Share and NTFS permissions separately, then take the most restrictive. Share=Read + NTFS=Full Control = Read over the network. Share=Full Control + NTFS=Read = Read over the network.

**Exam Tip 2:** DFSN vs. DFSR. DFS Namespaces creates the unified virtual path. DFS Replication keeps the content synchronized. They are complementary but independent — you can have one without the other.

**Exam Tip 3:** FSRM quota types. Hard quota blocks writes when the limit is reached. Soft quota sends a notification but allows writes to continue. Match the type to the scenario: "prevent" = hard, "notify" = soft.

**Exam Tip 4:** FSRM Active vs. Passive file screen. Active Screen blocks the file types entirely. Passive Screen logs the event but allows the file. Match to the scenario: "block executables" = Active, "audit for media files" = Passive.

**Exam Tip 5:** Shadow Copies are not a backup. They protect against accidental deletion or modification on a running server. They do not protect against hardware failure, ransomware that encrypts the shadow copies, or server loss.

**Exam Tip 6:** Best practice for share permissions is Full Control for Everyone or Authenticated Users at the Share level, then restrict with NTFS permissions. This avoids the double-permission management problem and leverages NTFS's superior granularity.

---

### [SEGMENT 9 — Lab Preview]

**[SHOW SCREEN: Lab 07 instructions document]**

This week's lab walks you through installing the File Server role and FSRM on DC1, creating a share with correct NTFS permissions, creating a 5 GB hard quota, configuring an Active File Screen for executables, enabling shadow copies on the C: volume, and creating a DFS namespace with one folder target.

Your deliverables are screenshots of the share permissions, the FSRM quota, the file screen, and the DFS namespace folder.

---

### [SEGMENT 10 — Module 07 Summary]

**[SHOW SCREEN: Summary slide]**

File services in Windows Server use SMB for sharing. NTFS and Share permissions both apply to network access, with the most restrictive combination being effective. DFS Namespaces creates a unified virtual path hiding the underlying server topology. DFS Replication keeps content synchronized across servers. FSRM manages quotas and blocks unwanted file types. Shadow Copies enable self-service recovery. Print Management centralizes printer deployment and driver distribution.

Module 08 covers Remote Desktop Services — the role that enables session-based desktop delivery and application publishing. See you there.

---

### Additional Resources

- [SMB file sharing overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview)
- [DFS Namespaces overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview)
- [File Server Resource Manager](https://learn.microsoft.com/en-us/windows-server/storage/fsrm/fsrm-overview)
- [Print and Document Services](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-roles-features/print-and-document-services-overview)

---

*End of Part 2. Proceed to the Reading Guide, Lab, Quiz, and Discussion for Module 07.*
