# Video Script: Module 13 — Storage Spaces and Advanced Storage (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

### Introduction

Welcome to Module 13. I'm Professor Nash, and today we're covering storage — one of the most critical and underappreciated areas of Windows Server administration. Poor storage decisions cause data loss, performance bottlenecks, and downtime. Good storage architecture prevents all three.

This module covers Storage Spaces, iSCSI configuration, Storage Replica, the ReFS file system, and BitLocker drive encryption. In Part 1, we focus on Storage Spaces and iSCSI. Part 2 covers Storage Replica, ReFS, and BitLocker.

---

### Section 1: Storage Spaces Overview

Storage Spaces is a Windows Server technology that virtualizes physical disks into resilient, flexible storage pools. Think of it as software-defined RAID built into the operating system — no dedicated RAID controller hardware required.

The architecture has three layers.

**Physical disks**: The actual hard drives or SSDs attached to the server. These can be SATA, SAS, or NVMe. Storage Spaces accepts nearly any disk type.

**Storage pool**: A collection of physical disks grouped together. The pool presents its combined capacity as a single resource to be allocated.

**Virtual disks (Storage Spaces)**: Logical disks carved out of the pool with a specified resiliency layout. This is where you choose Simple, Mirror, or Parity.

```powershell
# View available physical disks that can be added to a pool
Get-PhysicalDisk | Where-Object CanPool -eq $true

# Create a storage pool from three physical disks
$disks = Get-PhysicalDisk | Where-Object CanPool -eq $true | Select-Object -First 3

New-StoragePool -FriendlyName "DataPool" `
    -StorageSubSystemFriendlyName "Windows Storage*" `
    -PhysicalDisks $disks
```

---

### Section 2: Storage Spaces Resiliency Types

Once you have a pool, you create virtual disks with a resiliency setting. There are three main types.

**Simple (no resiliency)**: Data is striped across disks for performance — similar to RAID 0. There is no redundancy. If one physical disk fails, all data on that virtual disk is lost. Use simple spaces only for temporary or easily reproducible data, never for production critical data.

**Mirror**: Data is written to two or more physical disks simultaneously — similar to RAID 1 or RAID 10. A two-way mirror requires at least two disks and can survive one disk failure. A three-way mirror requires at least five disks and can survive two simultaneous disk failures.

**Parity**: Data is striped with parity information — similar to RAID 5 or RAID 6. Single parity requires at least three disks and can survive one failure. Dual parity requires at least seven disks and can survive two failures. Parity spaces use storage more efficiently than mirrors but have higher write overhead.

```powershell
# Create a two-way mirror virtual disk
New-VirtualDisk -StoragePoolFriendlyName "DataPool" `
    -FriendlyName "MirroredData" `
    -Size 500GB `
    -ResiliencySettingName Mirror `
    -NumberOfDataCopies 2

# Create a parity virtual disk
New-VirtualDisk -StoragePoolFriendlyName "DataPool" `
    -FriendlyName "ArchiveData" `
    -Size 1TB `
    -ResiliencySettingName Parity
```

---

### Section 3: Initializing and Using Storage Spaces Virtual Disks

After creating a virtual disk, you follow the standard Windows disk initialization process.

```powershell
# Initialize the new virtual disk
$vDisk = Get-VirtualDisk -FriendlyName "MirroredData"
$disk = $vDisk | Get-Disk
Initialize-Disk -Number $disk.Number -PartitionStyle GPT

# Create a partition and format it
New-Partition -DiskNumber $disk.Number -UseMaximumSize -DriveLetter M |
    Format-Volume -FileSystem NTFS -NewFileSystemLabel "MirroredData" -Confirm:$false
```

From this point, drive letter M: behaves like any other Windows volume — you can create files, share it, back it up, and so on. The resiliency is transparent to applications and users.

---

### Section 4: Storage Spaces Tiers

Storage Spaces Direct (S2D), available in Windows Server Datacenter edition, extends Storage Spaces to hyperconverged infrastructure — where compute and storage run on the same servers. This is the technology behind Azure Stack HCI.

For standard Storage Spaces (not S2D), you can use storage tiers to create a single virtual disk that automatically moves hot (frequently accessed) data to fast SSD storage and cold data to slower HDD storage.

```powershell
# Create an SSD tier and HDD tier in a pool that has both disk types
New-StorageTier -StoragePoolFriendlyName "TieredPool" `
    -FriendlyName "SSDTier" `
    -MediaType SSD

New-StorageTier -StoragePoolFriendlyName "TieredPool" `
    -FriendlyName "HDDTier" `
    -MediaType HDD

# Create a tiered virtual disk
New-VirtualDisk -StoragePoolFriendlyName "TieredPool" `
    -FriendlyName "TieredVolume" `
    -StorageTiers (Get-StorageTier -FriendlyName "SSDTier"),
                 (Get-StorageTier -FriendlyName "HDDTier") `
    -StorageTierSizes 100GB, 900GB `
    -ResiliencySettingName Mirror
```

---

### Section 5: iSCSI — Storage Area Networks Over TCP/IP

iSCSI (Internet Small Computer Systems Interface) is a protocol that transports SCSI storage commands over a standard TCP/IP network. It allows Windows servers to access block-level storage on a remote storage device as if it were a locally attached disk.

This is important because many enterprise storage scenarios — including Hyper-V Live Migration with shared storage and SQL Server database files on a SAN — use iSCSI.

Key iSCSI terminology:

- **iSCSI initiator**: The client — the server that wants to access storage. In Windows, this is the iSCSI Initiator software built into Windows Server.
- **iSCSI target**: The server that provides storage. On Windows Server, this is the iSCSI Target Server role service.
- **LUN (Logical Unit Number)**: A logical unit of storage presented by the target to the initiator. The initiator sees it as a disk.
- **IQN (iSCSI Qualified Name)**: A unique identifier for each iSCSI initiator and target, formatted as `iqn.YYYY-MM.reversedomain:identifier`.

---

### Section 6: Configuring an iSCSI Target (Server Side)

On the server that will provide storage (the target):

```powershell
# Install the iSCSI Target Server role
Install-WindowsFeature FS-iSCSITarget-Server -IncludeManagementTools

# Create an iSCSI virtual disk (the LUN file)
New-IscsiVirtualDisk -Path "C:\iSCSIStorage\LUN1.vhdx" -SizeBytes 100GB

# Create an iSCSI target
New-IscsiServerTarget -TargetName "StorageTarget01" `
    -InitiatorIds "IQN:iqn.1991-05.com.microsoft:initiator01"

# Connect the virtual disk to the target
Add-IscsiVirtualDiskTargetMapping -TargetName "StorageTarget01" `
    -Path "C:\iSCSIStorage\LUN1.vhdx"
```

The `InitiatorIds` parameter restricts which initiators can connect to this target. Limiting access by IQN is a basic access control measure.

---

### Section 7: Configuring an iSCSI Initiator (Client Side)

On the server that will consume the storage (the initiator):

```powershell
# Start and enable the iSCSI Initiator service
Start-Service MSiSCSI
Set-Service MSiSCSI -StartupType Automatic

# Connect to the iSCSI target
New-IscsiTargetPortal -TargetPortalAddress "192.168.1.100"

# Connect to the target
Connect-IscsiTarget -NodeAddress "iqn.2016-02.com.contoso:StorageTarget01" `
    -IsPersistent $true
```

After connecting, the LUN appears in Disk Management as a new disk. You initialize and format it exactly like a local disk.

```powershell
# Verify the iSCSI connection
Get-IscsiConnection
Get-IscsiSession
```

---

### Closing Part 1

In Part 1, we covered Storage Spaces pools, resiliency types (simple, mirror, parity), storage tiers, and iSCSI target/initiator configuration. These are foundational storage technologies that every Windows Server administrator needs to understand.

In Part 2, we move into Storage Replica for synchronous and asynchronous block-level replication, ReFS versus NTFS, and BitLocker drive encryption. See you there.
