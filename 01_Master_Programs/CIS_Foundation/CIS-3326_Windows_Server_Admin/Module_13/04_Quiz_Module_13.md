# Quiz: Module 13 — Storage Spaces and Advanced Storage

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Microsoft Windows Server Administration

---

Instructions: Select the best answer for each question. Each question is worth 10 points.

---

### Question 1

You need to create a storage solution that can survive two simultaneous disk failures. Which Storage Spaces resiliency type and minimum disk count should you choose?

- A) Two-way mirror with 2 disks
- B) Three-way mirror with 5 disks
- C) Single parity with 3 disks
- D) Simple space with 4 disks

**Answer**: B

**Explanation**: A three-way mirror writes three copies of all data and requires a minimum of five disks. It can survive two simultaneous disk failures. Single parity can only survive one failure. Simple spaces provide no redundancy.

---

### Question 2

In an iSCSI configuration, which component is the client that connects to and consumes block storage?

- A) iSCSI target
- B) iSCSI LUN
- C) iSCSI initiator
- D) iSCSI portal

**Answer**: C

**Explanation**: The iSCSI initiator is the client — the server that connects to the storage. The iSCSI target is the storage server that presents LUNs. A LUN is the logical unit of storage presented by the target. A portal is a network endpoint (IP address and port) used to discover targets.

---

### Question 3

You are configuring Storage Replica between two servers. The destination volume is accessible during normal replication. A colleague wants to use it for read-only backups. Is this possible?

- A) Yes — the destination volume is accessible read-write during replication
- B) Yes — the destination volume is accessible read-only during replication
- C) No — the destination volume is mounted as read-only and inaccessible while replication is active
- D) No — the destination volume must be offline during replication

**Answer**: C

**Explanation**: While Storage Replica is actively replicating, the destination volume is mounted in a read-only state that is inaccessible to file system operations. The volume can only be accessed after a failover, when it becomes the new source.

---

### Question 4

Which file system supports automatic detection and correction of silent data corruption (bit rot) when used with Storage Spaces mirroring?

- A) NTFS
- B) FAT32
- C) exFAT
- D) ReFS

**Answer**: D

**Explanation**: ReFS stores integrity checksums for data and metadata. When used with Storage Spaces mirroring, if a checksum mismatch is detected (indicating bit rot), ReFS automatically uses the mirror copy to correct the corrupted data. NTFS does not store checksums and cannot perform self-healing.

---

### Question 5

An administrator needs to format a new volume to host Hyper-V virtual machine files and wants the fastest possible Hyper-V checkpoint creation. Which file system should be used?

- A) NTFS with compression enabled
- B) FAT32 for maximum compatibility
- C) ReFS to take advantage of block clone technology
- D) exFAT for large file support

**Answer**: C

**Explanation**: ReFS supports block clone, which allows Hyper-V to create checkpoints almost instantly by creating metadata-only references to disk blocks rather than copying data. On NTFS, checkpoint creation requires physically copying differencing disk data, which is slower.

---

### Question 6

A server administrator wants to use BitLocker on a server that will reboot automatically overnight for patching. Manual PIN entry is not feasible. Which BitLocker configuration should be used?

- A) TPM + PIN protector
- B) TPM + USB key protector
- C) TPM with Network Unlock
- D) Recovery password only

**Answer**: C

**Explanation**: BitLocker Network Unlock automatically unlocks a TPM-protected drive during boot when the server is connected to the corporate network. No PIN or USB key entry is required. If the server boots outside the corporate network (theft scenario), the auto-unlock fails and a PIN or recovery key is required.

---

### Question 7

What is the primary purpose of the log volume in a Storage Replica partnership?

- A) To store a backup copy of all replicated data
- B) To track changes and ensure write-order fidelity during replication
- C) To cache reads from the destination volume
- D) To store Storage Replica configuration and policy files

**Answer**: B

**Explanation**: The Storage Replica log volume records write operations in order, ensuring that the destination volume receives changes in the correct sequence. It acts as a write-ahead log. Microsoft recommends placing the log volume on fast SSD or NVMe storage to avoid becoming a bottleneck.

---

### Question 8

Which of the following is a limitation of ReFS compared to NTFS?

- A) ReFS cannot store files larger than 256 TB
- B) ReFS cannot be used on volumes larger than 1 TB
- C) ReFS does not support being used as the operating system boot volume
- D) ReFS does not support files larger than 4 GB

**Answer**: C

**Explanation**: ReFS cannot be used for the Windows operating system boot volume. This is one of its key limitations compared to NTFS. ReFS supports very large files (up to 35 PB) and very large volumes, but it cannot host a bootable Windows installation.

---

### Question 9

You have a Storage Spaces pool with three 1 TB disks and create a two-way mirror virtual disk. Approximately how much usable storage is available for data?

- A) 3 TB — all disks used for data
- B) 2 TB — one disk holds parity
- C) 1.5 TB — data is split across all three disks with one copy
- D) 1 TB — each write is stored on two disks, leaving one disk worth of usable capacity

**Answer**: C

**Explanation**: A two-way mirror stores two copies of data across available disks. With 3 TB of raw capacity split into two copies, approximately 1.5 TB of usable space is available. The storage efficiency of a two-way mirror is roughly 50%, but with three disks, the third disk provides additional resilience beyond a strict 1:1 mirror.

---

### Question 10

You need to secure sensitive files on a shared file server so that even the local administrator cannot read them, while allowing the specific user who created them transparent access. Which technology provides this protection?

- A) BitLocker Drive Encryption
- B) NTFS permissions
- C) Encrypting File System (EFS)
- D) Storage Spaces parity

**Answer**: C

**Explanation**: EFS encrypts files using the user's certificate-based key. The encryption is transparent to the user who encrypted the file. Even local administrators cannot read EFS-encrypted files without the correct private key. BitLocker protects the entire volume but does not restrict per-user access to individual files.

---

---

### Question 11 (5 points)

An administrator creates a Storage Spaces pool with five 2 TB disks and creates
a dual parity (RAID-6 equivalent) virtual disk. What is the minimum usable
capacity and how many simultaneous disk failures can the pool survive?

- A) 6 TB usable; can survive 1 disk failure
- B) 6 TB usable; can survive 2 simultaneous disk failures
- C) 4 TB usable; can survive 2 simultaneous disk failures
- D) 8 TB usable; can survive 1 disk failure

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Dual parity (RAID-6 equivalent) can survive 2 simultaneous disk failures, not just 1.
  - **B** — Correct. Dual parity uses 2 disks worth of capacity for parity across 5 disks (5 × 2 TB = 10 TB raw; 10 TB − 4 TB parity overhead = 6 TB usable). It can tolerate 2 simultaneous disk failures.
  - **C** — With 5 × 2 TB disks and dual parity, the usable capacity is 6 TB, not 4 TB. Single parity with 3 disks would give roughly 4 TB, but with 5 disks the efficiency is higher.
  - **D** — 8 TB usable with 1 failure tolerance describes single parity across 5 disks (1 parity disk equivalent), which provides 8 TB usable but only 1-failure tolerance.

---

### Question 12 (5 points)

A Windows Server administrator adds a new physical disk to an existing Storage
Spaces pool. The pool currently has three disks and a two-way mirror virtual disk.
What happens to the existing virtual disk after the new disk is added?

- A) The virtual disk automatically rebalances data across all four disks to optimize performance
- B) The new disk becomes available for new virtual disk allocations but existing virtual disks do not use it automatically
- C) Storage Spaces immediately rebuilds the mirror using the new disk as the second copy
- D) The virtual disk expands to use the additional capacity automatically

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Storage Spaces does not automatically rebalance existing data across new disks. The new disk is added to the pool's capacity but existing virtual disks do not automatically redistribute data to it.
  - **B** — Correct. Adding a disk to a pool increases the pool's raw capacity. Existing virtual disks continue to use the disks they are already allocated on. The new disk becomes available for new virtual disk allocations or when existing virtual disks are extended.
  - **C** — Storage Spaces does not use new pool disks to rebuild existing mirrors. The mirror was already complete across the existing disks. New disks expand the pool's available space.
  - **D** — Virtual disks do not automatically expand when disks are added to the pool. An administrator must explicitly extend a virtual disk with `Resize-VirtualDisk` if more space is needed.

---

### Question 13 (5 points)

You configure iSCSI between a Windows Server target and a Windows Server
initiator. Which TCP port must be open on the target server's firewall for iSCSI
traffic?

- A) Port 445 (SMB)
- B) Port 3260 (iSCSI)
- C) Port 2049 (NFS)
- D) Port 8080 (HTTP alternate)

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Port 445 is used for SMB file sharing. iSCSI does not use SMB.
  - **B** — Correct. iSCSI uses TCP port 3260 as its well-known port for target connections. The Windows Server iSCSI Target firewall rule must allow inbound TCP 3260 from initiators.
  - **C** — Port 2049 is used for NFS (Network File System), a different storage protocol. NFS is file-level storage; iSCSI is block-level storage.
  - **D** — Port 8080 is typically used for HTTP proxy or alternate web services and has no role in iSCSI.

---

### Question 14 (5 points)

An administrator runs `Get-PhysicalDisk | Where-Object CanPool -eq $true` and
receives no results, even though four new drives are installed. What is the most
likely cause?

- A) The disks are too large for the storage pool
- B) The Storage Spaces feature is not installed on the server
- C) The disks are already initialized with a partition table (MBR or GPT)
- D) The disks are attached via USB and Storage Spaces does not support USB disks

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — Storage Spaces supports very large disks. Disk size is not a factor in pool eligibility.
  - **B** — Storage Spaces is a built-in feature of Windows Server and does not require separate installation. However, if the Storage Spaces Direct feature is not installed, that would be a separate issue.
  - **C** — Correct. `CanPool = $false` typically means the disks have already been initialized with a partition table or contain existing data. Storage Spaces requires uninitialized disks (raw disks). The fix is to clear the disk with `Clear-Disk -Number X -RemoveData -Confirm:$false`.
  - **D** — While USB disks have limitations with Storage Spaces, the `CanPool` property being false is most commonly caused by an initialized disk, not the connection type.

---

### Question 15 (5 points)

An administrator enables Data Deduplication on a volume and runs
`Get-DedupStatus` one week later. The output shows `SavedSpace: 120 GB` and
`SavingsRate: 40%`. What does `SavingsRate: 40%` indicate?

- A) 40% of files on the volume have been deduplicated
- B) The deduplication process is 40% complete
- C) 40% of the logical data size was eliminated through deduplication, leaving 60% as unique data
- D) The volume is 40% full after deduplication

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — SavingsRate does not measure the percentage of files processed; it measures the storage efficiency gained. Some files may be entirely unique while others share many identical chunks.
  - **B** — Deduplication runs as a background optimization job. `SavingsRate` is not a progress indicator for the current job; it is the cumulative storage savings ratio.
  - **C** — Correct. `SavingsRate: 40%` means that 40% of the logical data footprint was duplicate content that was eliminated. If the logical size before dedup was 200 GB, dedup saved 80 GB (40%), leaving 120 GB of unique data on disk.
  - **D** — Volume fill percentage is reported by `Get-Volume`, not `Get-DedupStatus`. `SavingsRate` measures data reduction, not volume utilization.

---

### Question 16 (5 points)

You need to extend an existing virtual disk in a Storage Spaces pool from 500 GB
to 800 GB. The pool has sufficient unallocated raw capacity. Which PowerShell
command resizes the virtual disk?

- A) `Expand-VirtualDisk -FriendlyName "DataVDisk" -Size 800GB`
- B) `Resize-VirtualDisk -FriendlyName "DataVDisk" -Size 800GB`
- C) `Set-VirtualDisk -FriendlyName "DataVDisk" -Size 800GB`
- D) `Extend-VirtualDisk -FriendlyName "DataVDisk" -AddSize 300GB`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Expand-VirtualDisk` is not a valid Storage Spaces cmdlet. The correct cmdlet is `Resize-VirtualDisk`.
  - **B** — Correct. `Resize-VirtualDisk -FriendlyName "DataVDisk" -Size 800GB` expands the virtual disk to 800 GB. After the virtual disk is resized, the administrator must also resize the partition and volume using `Resize-Partition` and `Resize-Volume` to make the additional space available to the file system.
  - **C** — `Set-VirtualDisk` modifies virtual disk attributes such as usage and allocation policy. It does not resize the virtual disk's storage capacity.
  - **D** — `Extend-VirtualDisk` is not a valid cmdlet. There is no `-AddSize` parameter for incremental extension.

---

### Question 17 (5 points)

Storage Replica is configured in synchronous mode between Server A (source) and
Server B (destination). A network outage occurs between the two servers. What
happens to write operations on Server A during the outage?

- A) Write operations on Server A continue normally; changes are queued in the log and replicated when connectivity is restored
- B) Write operations on Server A pause and block until network connectivity to Server B is restored
- C) Server A automatically fails over to asynchronous mode to continue serving writes
- D) Server A marks the replication as degraded but continues writes; Server B is updated with a full resync after the outage

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — This describes asynchronous replication behavior. In asynchronous mode, writes complete on the source and are queued for later delivery. Synchronous mode requires destination acknowledgment before writes complete.
  - **B** — Correct. Synchronous Storage Replica requires the destination to acknowledge each write before the write is considered complete on the source. If the network is unavailable, source writes pause (I/O blocks) until connectivity is restored or replication is switched to asynchronous mode.
  - **C** — Storage Replica does not automatically switch between synchronous and asynchronous modes. The mode must be changed manually by an administrator.
  - **D** — This describes degraded RAID behavior, not Storage Replica. Storage Replica in synchronous mode blocks writes; it does not continue with a deferred full resync.

---

### Question 18 (5 points)

An administrator needs to verify the health of all physical disks in a Storage
Spaces pool and identify any disks with a `HealthStatus` of "Warning" or
"Unhealthy." Which PowerShell command retrieves this information?

- A) `Get-StoragePool | Select-Object FriendlyName, HealthStatus`
- B) `Get-PhysicalDisk | Where-Object {$_.HealthStatus -ne "Healthy"} | Select-Object FriendlyName, HealthStatus, OperationalStatus`
- C) `Get-VirtualDisk | Select-Object FriendlyName, HealthStatus, ResiliencySettingName`
- D) `Get-Disk | Where-Object {$_.HealthStatus -ne "Healthy"}`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Get-StoragePool` reports pool-level health, not individual physical disk health. A pool can show Healthy while a member disk is Warning.
  - **B** — Correct. `Get-PhysicalDisk` returns individual disk objects with `HealthStatus` and `OperationalStatus` properties. Filtering for non-Healthy disks identifies Warning or Unhealthy members that require attention before a failure occurs.
  - **C** — `Get-VirtualDisk` reports virtual disk health, not physical disk health. A virtual disk may still show Healthy while a physical disk is degraded (protected by mirror redundancy).
  - **D** — `Get-Disk` returns disk partition/volume information from the Disk Management layer. Its `HealthStatus` property may not reflect the Storage Spaces physical disk health status visible through `Get-PhysicalDisk`.

---

### Question 19 (5 points)

An administrator creates a thin-provisioned virtual disk of 2 TB in a Storage
Spaces pool that has only 1 TB of raw capacity. The virtual disk initially uses
200 GB. What risk does this configuration create?

- A) No risk — thin provisioning automatically compresses data to fit within the physical pool
- B) If actual data consumption reaches the pool's raw capacity (1 TB), writes will fail because there is no physical space to allocate
- C) The 2 TB virtual disk immediately reserves all 2 TB of pool space, leaving only 800 GB available for other virtual disks
- D) Thin provisioning is not supported when pool capacity is less than the virtual disk size

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Thin provisioning does not compress data. It defers physical space allocation until data is actually written. If more data is written than physical space exists, writes fail.
  - **B** — Correct. Thin provisioning allows a virtual disk to be larger than the current physical pool capacity. As long as actual data usage stays below 1 TB (the pool's raw capacity), everything works. But if total actual data across all virtual disks exceeds the pool's physical capacity, new writes fail. This is called overprovisioning risk.
  - **C** — This describes fixed (thick) provisioning behavior. Thin provisioning specifically avoids pre-allocating physical space; it only consumes physical space as data is written.
  - **D** — Thin provisioning is explicitly designed to allow virtual disks larger than current physical capacity. It is a supported and intentional feature, not an error condition.

---

### Question 20 (5 points)

An administrator needs to configure iSCSI Multipath I/O (MPIO) to provide
redundant paths between a Windows Server initiator and an iSCSI target. Which
Windows feature must be installed to support MPIO, and which PowerShell cmdlet
configures iSCSI as a supported hardware?

- A) Install `Multipath-IO` feature; run `New-MSDSMSupportedHW -VendorId "MSFT2005" -ProductId "iSCSIBusType_0x9"`
- B) Install `iSCSI-Target-Server` feature; run `Enable-MSDSMAutomaticClaim -BusType iSCSI`
- C) Install `Multipath-IO` feature; run `Enable-MSDSMAutomaticClaim -BusType iSCSI`
- D) Install `FS-iSCSITarget-Server` feature; run `Set-MSDSMGlobalDefaultLoadBalancePolicy -Policy RR`

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — `New-MSDSMSupportedHW` adds a specific hardware vendor/product ID to the MPIO supported hardware list. For iSCSI, `Enable-MSDSMAutomaticClaim -BusType iSCSI` is the correct cmdlet that automatically claims all iSCSI devices for MPIO management.
  - **B** — `iSCSI-Target-Server` is the server-side target feature, not the initiator/MPIO feature. MPIO is configured on the initiator side and requires the `Multipath-IO` feature.
  - **C** — Correct. The `Multipath-IO` Windows feature installs the Microsoft DSM (Device Specific Module) for MPIO. `Enable-MSDSMAutomaticClaim -BusType iSCSI` configures MPIO to automatically claim all iSCSI devices, enabling multipath load balancing and failover.
  - **D** — `FS-iSCSITarget-Server` is the File Services role for the iSCSI target, not MPIO. `Set-MSDSMGlobalDefaultLoadBalancePolicy` sets the load balance policy for existing MPIO paths but does not install or configure the MPIO feature itself.

End of Quiz — Module 13
