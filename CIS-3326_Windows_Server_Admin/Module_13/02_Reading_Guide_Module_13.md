# Reading Guide: Module 13 — Storage Spaces and Advanced Storage

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3326 &BULL; WINDOWS SERVER ADMINISTRATION & ACTIVE DIRECTORY</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

---

## Supplemental Resources

The following free, open-access resources go deeper on Module 13 topics:

**1. Microsoft Learn — Implement Storage Spaces and Storage Spaces Direct**
<https://learn.microsoft.com/en-us/training/modules/implement-storage-spaces-storage-spaces-direct/>
Hands-on module covering Storage Spaces pool creation, resiliency types (mirror, parity, dual parity), thin provisioning, and virtual disk management with sandbox exercises aligned to AZ-800.

**2. Microsoft Docs — Storage Replica overview**
<https://learn.microsoft.com/en-us/windows-server/storage/storage-replica/storage-replica-overview>
Complete architecture reference for Storage Replica including synchronous vs. asynchronous modes, log volume requirements, partnership configuration, and failover procedures.

**3. Microsoft Docs — Resilient File System (ReFS) overview**
<https://learn.microsoft.com/en-us/windows-server/storage/refs/refs-overview>
Covers ReFS features including integrity checksums, block clone for Hyper-V, allocate on write, and limitations compared to NTFS (no boot volume support, no EFS, no compression).

**4. Microsoft Docs — Data Deduplication overview**
<https://learn.microsoft.com/en-us/windows-server/storage/data-deduplication/overview>
Full reference for Data Deduplication including supported workloads, savings rate calculations, optimization job scheduling, and integration with Storage Spaces and iSCSI volumes.
