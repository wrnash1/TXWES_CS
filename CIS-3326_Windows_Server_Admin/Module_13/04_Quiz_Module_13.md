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

End of Quiz — Module 13
