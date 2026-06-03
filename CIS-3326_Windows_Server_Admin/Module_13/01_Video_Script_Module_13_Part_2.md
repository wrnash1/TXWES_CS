# Video Script: Module 13 — Storage Spaces and Advanced Storage (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

### Introduction

Welcome back to Module 13. In Part 1 we built a foundation in Storage Spaces and iSCSI. In Part 2 we cover three more critical storage topics: Storage Replica for disaster recovery replication, the ReFS file system, and BitLocker drive encryption. These topics round out the storage section of Microsoft certification exams.

---

### Section 1: Storage Replica

Storage Replica is a Windows Server feature that replicates volumes between servers or between sites at the block level. Unlike Hyper-V Replica, which replicates virtual machines, Storage Replica replicates raw volumes — any data on those volumes, regardless of what application put it there.

Storage Replica supports two modes.

**Synchronous replication**: Every write to the source volume is also written to the destination volume before the write is acknowledged as complete. This means zero data loss on failover — the destination always has every byte the source has. The trade-off is that write latency increases because the write must travel to the destination and back before being acknowledged. Synchronous mode is practical only when the destination is geographically close (low-latency network link).

**Asynchronous replication**: Writes are acknowledged at the source immediately and replicated to the destination shortly after. This allows replication over high-latency WAN links but introduces a small window of potential data loss equal to the replication lag.

```powershell
# Install Storage Replica (Windows Server 2016 Datacenter and later)
Install-WindowsFeature Storage-Replica -IncludeManagementTools -Restart
```

---

### Section 2: Configuring Storage Replica

Storage Replica requires:

- Two volumes on the source server: a data volume and a log volume
- Two matching volumes on the destination server: a data volume and a log volume
- The log volumes must be dedicated — no other data should be stored on them
- Log volumes should be on fast storage (SSD recommended)

```powershell
# Test that the replication prerequisites are met
Test-SRTopology -SourceComputerName "Server01" `
    -SourceVolumeName "D:" `
    -SourceLogVolumeName "E:" `
    -DestinationComputerName "Server02" `
    -DestinationVolumeName "D:" `
    -DestinationLogVolumeName "E:" `
    -DurationInMinutes 30 `
    -ResultPath "C:\SRTest"
```

Always run `Test-SRTopology` before configuring replication. It validates network bandwidth, latency, disk performance, and other prerequisites.

```powershell
# Configure synchronous replication
New-SRPartnership -SourceComputerName "Server01" `
    -SourceRGName "SourceRG" `
    -SourceVolumeName "D:" `
    -SourceLogVolumeName "E:" `
    -DestinationComputerName "Server02" `
    -DestinationRGName "DestRG" `
    -DestinationVolumeName "D:" `
    -DestinationLogVolumeName "E:" `
    -ReplicationMode Synchronous

# Check replication status
Get-SRPartnership
Get-SRGroup
```

An important operational note: the destination volume is mounted in read-only mode while replication is active. You cannot access the destination data during normal operation — only after a failover.

---

### Section 3: Storage Replica Failover

When the source fails or you initiate a planned failover:

```powershell
# Initiate a failover (run on the destination server)
Set-SRPartnership -NewSourceComputerName "Server02" `
    -SourceRGName "DestRG" `
    -DestinationComputerName "Server01" `
    -DestinationRGName "SourceRG"
```

After failover, Server02 becomes the new source and Server01 (when available) becomes the new destination. Applications that were using Server01's data volume must be redirected to Server02.

---

### Section 4: ReFS — Resilient File System

ReFS (Resilient File System) is a modern file system designed for maximum data integrity and large-scale storage. It was designed as the next step beyond NTFS, though it does not completely replace NTFS in all scenarios.

Key ReFS advantages over NTFS:

- **Integrity streams**: ReFS can optionally store checksums for data and metadata. When combined with Storage Spaces mirroring, ReFS automatically detects and corrects silent data corruption (bit rot) by comparing checksums against the mirror copy.
- **Large volume support**: ReFS supports volumes up to 35 petabytes (compared to NTFS's practical limit of ~256 TB).
- **Resilience to corruption**: ReFS uses a B+ tree structure with copy-on-write for metadata updates. A system crash mid-write leaves the file system in a consistent state without requiring chkdsk.
- **Block clone**: ReFS supports block cloning, allowing fast zero-copy file copies used by Hyper-V checkpoints on ReFS-formatted volumes (instant checkpoint creation).

ReFS limitations — things NTFS can do that ReFS cannot:

- ReFS does not support bootable system volumes (cannot be used for the OS drive)
- ReFS does not support file system compression
- ReFS does not support encrypted file system (EFS)
- ReFS does not support disk quotas
- ReFS does not support named streams (Data Deduplication is limited)

For data volumes hosting Hyper-V VMs or Storage Spaces workloads, ReFS is often the better choice. For OS drives and general purpose file shares requiring all NTFS features, NTFS remains the right choice.

```powershell
# Format a volume with ReFS
Format-Volume -DriveLetter D -FileSystem ReFS `
    -NewFileSystemLabel "VMStorage" -Confirm:$false

# Check file system type
Get-Volume -DriveLetter D | Select-Object FileSystem, FileSystemLabel
```

---

### Section 5: BitLocker Drive Encryption

BitLocker is Windows Server's full-disk encryption feature. It encrypts the entire volume using AES encryption, protecting data from being read if the physical disk is stolen or the server is accessed without authorization.

BitLocker uses a TPM (Trusted Platform Module) chip on the server's motherboard to seal the encryption key. The key is only released if the system boots in an unmodified state — if the boot configuration changes (indicating possible tampering), BitLocker requires a recovery key before allowing access.

```powershell
# Install the BitLocker feature
Install-WindowsFeature BitLocker -IncludeManagementTools -Restart

# Check TPM status
Get-Tpm

# Enable BitLocker on a data drive (D:)
Enable-BitLocker -MountPoint "D:" `
    -EncryptionMethod XtsAes256 `
    -RecoveryPasswordProtector

# Add TPM protector
Add-BitLockerKeyProtector -MountPoint "D:" -TpmProtector
```

BitLocker recovery keys should always be backed up to Active Directory or Azure AD before encrypting drives. If the TPM fails or the key is lost, the recovery key is the only way to access the data.

```powershell
# Back up the recovery key to Active Directory
$blv = Get-BitLockerVolume -MountPoint "D:"
Backup-BitLockerKeyProtector -MountPoint "D:" `
    -KeyProtectorId $blv.KeyProtector[0].KeyProtectorId
```

---

### Section 6: BitLocker Network Unlock

In enterprise environments, requiring administrators to enter a BitLocker PIN on every server reboot is impractical — servers may reboot after patches or power events in unmanned data centers. BitLocker Network Unlock solves this by automatically unlocking BitLocker-encrypted drives during boot if the server is connected to the corporate network.

Network Unlock requires:

- Windows Deployment Services (WDS) server on the network with the Network Unlock feature
- A public key certificate configured on the WDS server
- The BitLocker Network Unlock key protector configured on the encrypted drive

With Network Unlock, servers reboot automatically without PIN entry when on the corporate network. If the server boots outside the corporate network (theft scenario), Network Unlock fails and the physical PIN or recovery key is required.

---

### Section 7: Data Deduplication

Data Deduplication (Dedup) is a volume-level optimization that identifies duplicate chunks of data and stores only one copy, replacing duplicates with references. This can dramatically reduce storage consumption on file servers and VM libraries.

```powershell
# Install Data Deduplication
Install-WindowsFeature FS-Data-Deduplication

# Enable deduplication on a volume
Enable-DedupVolume -Volume "D:" -UsageType Default

# Check deduplication savings
Get-DedupVolume -Volume "D:" | Select-Object Volume, SavingsRate, SavedSpace
```

Typical savings rates:

- General purpose file server: 30–50%
- Virtual machine storage (VHDs/VHDXs): 80–95%
- Backup target: 50–80%

---

### Summary

In this two-part module, we covered the complete storage stack for Windows Server: Storage Spaces pools and resiliency types, iSCSI target/initiator configuration, Storage Replica for block-level replication, ReFS versus NTFS trade-offs, BitLocker encryption, and Data Deduplication.

Storage is a discipline that rewards careful design. Understanding these tools and when to use each one separates competent administrators from exceptional ones.

In Module 14, we move into Windows Server Security — Windows Defender, Windows Firewall with Advanced Security, Just Enough Administration, credential guard, and LAPS. See you there.
