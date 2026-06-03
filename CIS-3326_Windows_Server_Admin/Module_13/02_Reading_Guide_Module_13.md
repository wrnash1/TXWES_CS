# Reading Guide: Module 13 — Storage Spaces and Advanced Storage

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Microsoft Windows Server Administration

---

## Overview

This reading guide covers Storage Spaces, iSCSI, Storage Replica, ReFS, and BitLocker. Storage is one of the most exam-heavy areas in Windows Server administration. Pay close attention to the comparison tables — they are directly exam-relevant.

---

## Part 1: Storage Spaces Architecture

### 1.1 Storage Pool Concepts

A storage pool abstracts physical disk hardware into a managed resource. Key properties of a storage pool include:

- **Friendly name**: A human-readable label for the pool
- **Primordial pool**: The Windows-managed pool containing all unallocated physical disks; disks must be moved out of the primordial pool into a named pool to be used
- **Write-back cache**: An optional SSD cache layer that accelerates writes to HDD-based pools

```powershell
# View all storage pools including the primordial pool
Get-StoragePool

# View physical disks in a specific pool
Get-StoragePool -FriendlyName "DataPool" | Get-PhysicalDisk

# Add a new disk to an existing pool (hot-add capacity)
$newDisk = Get-PhysicalDisk | Where-Object FriendlyName -eq "PhysicalDisk4"
Add-PhysicalDisk -StoragePoolFriendlyName "DataPool" -PhysicalDisks $newDisk
```

### 1.2 Resiliency Comparison Table

| Resiliency Type | Minimum Disks | Can Tolerate Failures | Storage Efficiency | Use Case |
|---|---|---|---|---|
| Simple | 1 | 0 | 100% | Temp/scratch data only |
| Two-way Mirror | 2 | 1 | 50% | General purpose data |
| Three-way Mirror | 5 | 2 | 33% | Mission-critical data |
| Single Parity | 3 | 1 | 67%+ | Archive/sequential read |
| Dual Parity | 7 | 2 | 50%+ | High-capacity archive |

Storage efficiency for parity improves as more disks are added to the pool, because the parity overhead is spread across more data disks.

### 1.3 Virtual Disk Provisioning

Virtual disks can be thin-provisioned (size reported to OS is larger than actual pool allocation) or fixed-provisioned.

```powershell
# Create a thin-provisioned virtual disk
New-VirtualDisk -StoragePoolFriendlyName "DataPool" `
    -FriendlyName "ThinDisk" `
    -Size 1TB `
    -ProvisioningType Thin `
    -ResiliencySettingName Mirror

# Create a fixed virtual disk
New-VirtualDisk -StoragePoolFriendlyName "DataPool" `
    -FriendlyName "FixedDisk" `
    -Size 500GB `
    -ProvisioningType Fixed `
    -ResiliencySettingName Mirror
```

With thin provisioning, the virtual disk reports 1 TB to the operating system but only consumes pool capacity as data is written. This allows overprovisioning — creating more virtual disk space than physically exists — with the expectation that not all disks will fill simultaneously.

---

## Part 2: iSCSI Deep Dive

### 2.1 iSCSI Architecture

iSCSI runs over TCP/IP using standard Ethernet infrastructure. Unlike Fibre Channel SANs that require dedicated hardware (HBAs, FC switches), iSCSI works on existing network infrastructure.

In production, iSCSI storage networks are typically isolated on dedicated VLANs or dedicated NICs with jumbo frames enabled (9000 MTU) to improve throughput and reduce CPU overhead from packet fragmentation.

### 2.2 CHAP Authentication

iSCSI supports CHAP (Challenge Handshake Authentication Protocol) to authenticate the initiator to the target and optionally the target back to the initiator (mutual CHAP).

```powershell
# Configure CHAP on the initiator for a specific target
Set-IscsiChapSecret -NewChapSecret "Str0ngS3cr3t!"

# Connect with CHAP authentication
Connect-IscsiTarget `
    -NodeAddress "iqn.2016-02.com.contoso:target01" `
    -AuthenticationType ONEWAYCHAP `
    -ChapUsername "initiator01" `
    -ChapSecret "Str0ngS3cr3t!" `
    -IsPersistent $true
```

### 2.3 Multipath I/O

Enterprise iSCSI deployments use Multipath I/O (MPIO) to provide redundant paths between the initiator and target. If one network path fails, traffic automatically fails over to another path without interruption.

```powershell
# Install MPIO feature
Install-WindowsFeature MultiPath-IO

# Add iSCSI support to MPIO
Enable-MSDSMAutomaticClaim -BusType iSCSI

# Check MPIO paths
Get-MSDSMSupportedHW
```

---

## Part 3: Storage Replica

### 3.1 Synchronous vs. Asynchronous Comparison

| Feature | Synchronous | Asynchronous |
|---|---|---|
| Data loss on failover | Zero (RPO = 0) | Up to replication lag (RPO > 0) |
| Write latency impact | Higher (round-trip to destination) | Minimal (write acknowledged locally) |
| Maximum practical distance | ~5 ms RTT (~500 km) | No distance limit |
| Use case | Campus or metro replication | Wide-area disaster recovery |

### 3.2 Log Volume Sizing

The log volume is critical for Storage Replica performance. Microsoft recommends:

- Log volume should be at least 9 GB but sized to your write workload
- Log volume should be on the fastest available storage (NVMe or SSD)
- Log volumes must be dedicated — never store user data on the log volume

```powershell
# Check current replication status and log usage
Get-SRGroup | Select-Object Name, ReplicationMode, ReplicationStatus
Get-SRPartnership
```

### 3.3 Storage Replica Editions

Storage Replica availability varies by Windows Server edition.

- **Windows Server 2016/2019/2022 Datacenter**: Full Storage Replica, unlimited volume size
- **Windows Server 2016/2019/2022 Standard**: Storage Replica limited to 2 TB volumes per partnership
- **Windows Server Essentials**: Storage Replica not available

---

## Part 4: ReFS vs. NTFS

### 4.1 Feature Comparison

| Feature | NTFS | ReFS |
|---|---|---|
| Maximum volume size | ~256 TB (practical) | 35 PB |
| Maximum file size | 256 TB | 35 PB |
| Bootable (OS volume) | Yes | No |
| File compression | Yes | No |
| EFS (file encryption) | Yes | No |
| Disk quotas | Yes | No |
| Hard links | Yes | Limited |
| Data integrity checksums | No | Yes (with Storage Spaces) |
| Block clone (Hyper-V) | No | Yes |
| Self-healing corruption | No | Yes (with mirrored Storage Spaces) |
| Data Deduplication | Full support | Limited (Hyper-V workloads only) |

### 4.2 When to Use ReFS

Use ReFS when:

- The volume hosts Hyper-V virtual machine files — block clone makes checkpoints nearly instantaneous
- The volume is part of a Storage Spaces mirror — integrity checksums enable self-healing
- You need maximum resilience against silent data corruption (bit rot)
- The volume stores large files where NTFS metadata overhead matters

Use NTFS when:

- The volume is the OS system drive
- You need file compression, EFS, disk quotas, or full deduplication support
- You are using Storage Spaces with simple (no resiliency) layouts — ReFS integrity only helps with mirrors

---

## Part 5: BitLocker

### 5.1 BitLocker Key Protectors

BitLocker can use multiple key protectors to unlock an encrypted volume. Using more than one protector provides redundancy.

| Protector Type | Description | Use Case |
|---|---|---|
| TPM | Sealed to hardware, unlocks on normal boot | Server OS drives (transparent unlock) |
| TPM + PIN | Requires PIN entry at each boot | High-security servers, requires physical access |
| TPM + Network Unlock | Unlocks when connected to corporate network | Data center servers with automated reboots |
| Recovery Password | 48-digit numeric key | Emergency access, always configured as backup |
| Recovery Key | File-based key | Backup to USB or AD |

### 5.2 BitLocker and Active Directory

Storing BitLocker recovery keys in Active Directory ensures keys are available if a server's TPM fails or is replaced.

```powershell
# Verify AD BitLocker recovery key storage is configured
# This GPO path configures automatic AD backup:
# Computer Configuration > Administrative Templates >
# Windows Components > BitLocker Drive Encryption >
# Store BitLocker recovery information in Active Directory

# Manually back up an existing key to AD
$BLV = Get-BitLockerVolume -MountPoint "C:"
Backup-BitLockerKeyProtector -MountPoint "C:" `
    -KeyProtectorId ($BLV.KeyProtector |
        Where-Object KeyProtectorType -eq RecoveryPassword).KeyProtectorId
```

### 5.3 BitLocker Status Monitoring

```powershell
# Check BitLocker status on all volumes
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus,
    EncryptionMethod, ProtectionStatus, LockStatus

# Check encryption percentage on a drive being encrypted
(Get-BitLockerVolume -MountPoint "D:").EncryptionPercentage
```

---

## Key Terms to Know

- **Storage pool** — collection of physical disks managed as a unit
- **Virtual disk / Storage Space** — logical disk carved from a pool with a resiliency setting
- **Simple / Mirror / Parity** — Storage Spaces resiliency types
- **iSCSI initiator** — the client that consumes block storage
- **iSCSI target** — the server that provides block storage
- **LUN** — Logical Unit Number, the logical storage unit presented to an initiator
- **IQN** — iSCSI Qualified Name, unique identifier for initiators and targets
- **MPIO** — Multipath I/O, redundant network paths to iSCSI storage
- **Storage Replica** — block-level volume replication feature
- **Synchronous replication** — zero data loss, higher write latency
- **Asynchronous replication** — some data loss risk, usable over WAN
- **ReFS** — Resilient File System, data integrity-focused, no OS boot support
- **BitLocker** — full volume encryption built into Windows Server
- **TPM** — Trusted Platform Module, hardware chip that seals BitLocker keys
- **Network Unlock** — auto-unlock BitLocker on reboot when on corporate network
- **Data Deduplication** — eliminating duplicate data chunks to reduce storage usage

---

## Review Questions

1. How many physical disks are required for a three-way mirror Storage Space, and how many disk failures can it survive?

2. What is the difference between an iSCSI initiator and an iSCSI target?

3. Why should the iSCSI log volume in Storage Replica be placed on fast SSD storage?

4. Explain the trade-off between synchronous and asynchronous Storage Replica replication.

5. List three features that NTFS supports but ReFS does not.

6. What is block clone in ReFS, and why does it benefit Hyper-V checkpoint performance?

7. What happens if a server with a BitLocker TPM protector has its motherboard replaced?

8. What is BitLocker Network Unlock, and what security scenario does it defend against?

9. What is thin provisioning in Storage Spaces, and what risk does overprovisioning create?

10. A volume is using Data Deduplication and shows a 75% savings rate. Explain what this means for storage consumption.
