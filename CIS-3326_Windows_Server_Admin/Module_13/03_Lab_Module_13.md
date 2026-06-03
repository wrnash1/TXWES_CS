# Lab Activity: Module 13 — Storage Spaces and Advanced Storage

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Overview

In this lab, you create a Storage Spaces pool and virtual disks with different resiliency settings, configure iSCSI target and initiator, compare ReFS and NTFS volumes, and enable BitLocker on a data drive. These exercises cover the core storage skills tested on Microsoft certification exams.

---

## Lab Environment Requirements

- Windows Server 2019 or 2022 virtual machine
- At least four additional virtual disks attached (each at least 10 GB) — add these via your hypervisor settings before starting the lab
- Administrator credentials
- TPM (virtual TPM must be enabled in hypervisor settings for BitLocker exercises)

---

## Part 1: Storage Spaces — Create a Pool and Virtual Disks

### Step 1.1 — Verify Available Disks

```powershell
# List all physical disks eligible for pooling
Get-PhysicalDisk | Where-Object CanPool -eq $true |
    Select-Object FriendlyName, Size, MediaType, OperationalStatus
```

You should see the additional virtual disks you attached. If no disks show as poolable, verify they are attached and unformatted.

### Step 1.2 — Create a Storage Pool

```powershell
# Select three disks for the pool
$poolDisks = Get-PhysicalDisk | Where-Object CanPool -eq $true | Select-Object -First 3

# Create the pool
New-StoragePool -FriendlyName "LabPool" `
    -StorageSubSystemFriendlyName "Windows Storage*" `
    -PhysicalDisks $poolDisks

# Verify the pool
Get-StoragePool -FriendlyName "LabPool" | Select-Object FriendlyName, Size, AllocatedSize
```

### Step 1.3 — Create a Mirror Virtual Disk

```powershell
New-VirtualDisk -StoragePoolFriendlyName "LabPool" `
    -FriendlyName "MirrorVDisk" `
    -Size 5GB `
    -ResiliencySettingName Mirror `
    -NumberOfDataCopies 2

Get-VirtualDisk -FriendlyName "MirrorVDisk" |
    Select-Object FriendlyName, ResiliencySettingName, Size, OperationalStatus
```

### Step 1.4 — Initialize and Format the Mirror Virtual Disk

```powershell
$vdisk = Get-VirtualDisk -FriendlyName "MirrorVDisk"
$disk = $vdisk | Get-Disk
Initialize-Disk -Number $disk.Number -PartitionStyle GPT -PassThru |
    New-Partition -UseMaximumSize -DriveLetter M |
    Format-Volume -FileSystem NTFS -NewFileSystemLabel "MirrorData" -Confirm:$false
```

Verify drive M: is visible in File Explorer and accessible.

### Step 1.5 — Create a Simple Virtual Disk (No Resiliency)

```powershell
New-VirtualDisk -StoragePoolFriendlyName "LabPool" `
    -FriendlyName "SimpleVDisk" `
    -Size 3GB `
    -ResiliencySettingName Simple

$vdisk2 = Get-VirtualDisk -FriendlyName "SimpleVDisk"
$disk2 = $vdisk2 | Get-Disk
Initialize-Disk -Number $disk2.Number -PartitionStyle GPT -PassThru |
    New-Partition -UseMaximumSize -DriveLetter S |
    Format-Volume -FileSystem NTFS -NewFileSystemLabel "SimpleData" -Confirm:$false
```

---

## Part 2: iSCSI Target Server Configuration

### Step 2.1 — Install iSCSI Target Server

```powershell
Install-WindowsFeature FS-iSCSITarget-Server -IncludeManagementTools
```

### Step 2.2 — Create Storage for the iSCSI LUN

```powershell
# Create a directory for iSCSI virtual disk files
New-Item -ItemType Directory -Path "C:\iSCSIVDisks" -Force

# Create a 2 GB iSCSI virtual disk
New-IscsiVirtualDisk -Path "C:\iSCSIVDisks\LUN1.vhdx" -SizeBytes 2GB
```

### Step 2.3 — Discover Your Initiator IQN

```powershell
# Start the iSCSI Initiator service (needed to get the IQN)
Start-Service MSiSCSI
Set-Service MSiSCSI -StartupType Automatic

# Get the local initiator IQN
(Get-InitiatorPort).NodeAddress
```

Record the IQN — it will look like `iqn.1991-05.com.microsoft:servername`.

### Step 2.4 — Create an iSCSI Target

```powershell
# Replace the IQN below with your actual initiator IQN from Step 2.3
$initiatorIQN = "iqn.1991-05.com.microsoft:your-server-name"

New-IscsiServerTarget -TargetName "LabTarget01" `
    -InitiatorIds "IQN:$initiatorIQN"

# Map the virtual disk to the target
Add-IscsiVirtualDiskTargetMapping -TargetName "LabTarget01" `
    -Path "C:\iSCSIVDisks\LUN1.vhdx"
```

---

## Part 3: iSCSI Initiator — Connect to the Target

### Step 3.1 — Discover the Target Portal

```powershell
# Connect to the local server as the iSCSI target (loopback for lab)
New-IscsiTargetPortal -TargetPortalAddress "127.0.0.1"

# Discover available targets
Get-IscsiTarget
```

### Step 3.2 — Connect to the Target

```powershell
# Connect to the target (replace NodeAddress with your target's IQN)
$targetIQN = (Get-IscsiTarget).NodeAddress
Connect-IscsiTarget -NodeAddress $targetIQN -IsPersistent $true

# Verify the connection
Get-IscsiConnection
Get-IscsiSession
```

### Step 3.3 — Initialize and Format the iSCSI LUN

The iSCSI LUN now appears as a new disk. Initialize and format it.

```powershell
# Find the new disk (it will show as RAW)
Get-Disk | Where-Object PartitionStyle -eq RAW

# Initialize and format (adjust disk number as needed)
$iscsiDisk = Get-Disk | Where-Object PartitionStyle -eq RAW | Select-Object -First 1
Initialize-Disk -Number $iscsiDisk.Number -PartitionStyle GPT -PassThru |
    New-Partition -UseMaximumSize -DriveLetter I |
    Format-Volume -FileSystem NTFS -NewFileSystemLabel "iSCSIData" -Confirm:$false
```

Verify drive I: is accessible and you can create files on it.

---

## Part 4: ReFS vs. NTFS Comparison

### Step 4.1 — Format a Volume with ReFS

Use the fourth additional disk for this exercise.

```powershell
# Find an available unformatted disk
$refsDisk = Get-Disk | Where-Object PartitionStyle -eq RAW | Select-Object -Last 1

Initialize-Disk -Number $refsDisk.Number -PartitionStyle GPT -PassThru |
    New-Partition -UseMaximumSize -DriveLetter R |
    Format-Volume -FileSystem ReFS `
        -NewFileSystemLabel "ReFSVolume" -Confirm:$false
```

### Step 4.2 — Compare Features

Run the following on both volumes and note the differences.

```powershell
# Check file system type on both volumes
Get-Volume -DriveLetter M | Select-Object DriveLetter, FileSystem, FileSystemLabel, SizeRemaining, Size
Get-Volume -DriveLetter R | Select-Object DriveLetter, FileSystem, FileSystemLabel, SizeRemaining, Size

# Attempt to enable compression on ReFS (this should fail)
compact /c /s R:\
```

Document: Does the ReFS volume support compression? What error message do you receive?

---

## Part 5: BitLocker on a Data Drive

### Step 5.1 — Verify TPM Is Available

```powershell
Get-Tpm | Select-Object TpmPresent, TpmReady, TpmEnabled, TpmActivated
```

If TpmPresent is False, BitLocker can still be used without TPM by using a password protector only.

### Step 5.2 — Enable BitLocker on Drive S

```powershell
# Enable BitLocker with a recovery password protector
Enable-BitLocker -MountPoint "S:" `
    -EncryptionMethod XtsAes256 `
    -RecoveryPasswordProtector

# Check encryption status and record the recovery key
Get-BitLockerVolume -MountPoint "S:" |
    Select-Object MountPoint, VolumeStatus, EncryptionPercentage,
        EncryptionMethod, ProtectionStatus
```

### Step 5.3 — Retrieve and Record the Recovery Password

```powershell
$blv = Get-BitLockerVolume -MountPoint "S:"
$blv.KeyProtector | Where-Object KeyProtectorType -eq RecoveryPassword |
    Select-Object KeyProtectorId, RecoveryPassword
```

Record the 48-digit recovery password in your lab report. This is what you would use to unlock the drive if the system is rebuilt.

### Step 5.4 — Verify Encryption Completes

```powershell
# Poll until encryption reaches 100%
do {
    $pct = (Get-BitLockerVolume -MountPoint "S:").EncryptionPercentage
    Write-Host "Encryption: $pct%"
    Start-Sleep -Seconds 5
} while ($pct -lt 100)
Write-Host "Encryption complete."
```

---

## Lab Deliverables

Answer the following questions in your lab report.

1. Paste the output of `Get-VirtualDisk` showing both the MirrorVDisk and SimpleVDisk with their resiliency settings.

2. How many physical disks were in your pool? What would happen to the data on MirrorVDisk if one of those disks failed?

3. Paste the output of `Get-IscsiConnection` after successfully connecting the iSCSI initiator to the target.

4. What happened when you attempted to enable compression on the ReFS volume in Step 4.2?

5. Paste the BitLocker volume status output from Step 5.2 showing encryption percentage and protection status.

6. Record your 48-digit BitLocker recovery password (first 8 digits only for the lab report — do not share the full key).

---

## Troubleshooting Tips

**No poolable disks found**: Ensure the additional virtual disks are attached in the hypervisor and are not initialized. Initialized disks with existing partitions cannot be added to a storage pool.

**iSCSI connection refused**: Verify the iSCSI Initiator service is running (`Get-Service MSiSCSI`). Also verify the IQN in the target's allowed initiators list matches exactly.

**ReFS format option not shown in GUI**: ReFS is available via PowerShell formatting. The Windows Server GUI (Disk Management) may not list ReFS for all disk types. Use `Format-Volume` in PowerShell.

**BitLocker fails with "no TPM"**: Use `-PasswordProtector` instead of `-TpmProtector` for lab environments without a virtual TPM.
