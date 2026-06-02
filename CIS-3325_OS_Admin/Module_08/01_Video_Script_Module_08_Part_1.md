# Video Script: Module 08 - Storage Management (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Partitions and Filesystems

---

### Opening

Welcome to Module 08. Storage management is one of the most consequential skills in Linux
administration because mistakes here can cause permanent data loss. We cover three major topics
across both parts: disk partitioning, the Logical Volume Manager (LVM), and software RAID.
In Part 1 we cover partitions, partition tables, filesystems, and the /etc/fstab mount
configuration file. In Part 2 we cover LVM and RAID.

---

### Section 1: Disk and Partition Concepts

[SHOW TERMINAL]

```bash
lsblk
```

lsblk lists all block devices: disks and their partitions. The output shows device names,
sizes, and mount points. sda is the first SCSI/SATA disk. sda1, sda2 are its partitions.
nvme0n1 is an NVMe SSD; its partitions are nvme0n1p1, nvme0n1p2.

```bash
lsblk -f
```

The -f flag adds filesystem type and UUID information.

A partition table is metadata stored at the beginning of a disk that describes where partitions
start and end. There are two partition table formats:

MBR (Master Boot Record): Legacy format. Maximum 4 primary partitions (or 3 primary + 1
extended with logical partitions inside). Maximum disk size 2 TB. Supports BIOS boot.

GPT (GUID Partition Table): Modern format. Up to 128 partitions. Supports disks larger than
2 TB. Required for UEFI systems. Strongly preferred for new deployments.

```bash
sudo fdisk -l /dev/sda
```

fdisk -l shows the partition table. Note whether it says "Disklabel type: dos" (MBR) or
"Disklabel type: gpt" (GPT).

---

### Section 2: Creating Partitions with fdisk and gdisk

[SHOW TERMINAL]

For MBR disks use fdisk. For GPT disks use gdisk (or parted, which handles both).

```bash
sudo fdisk /dev/sdb
```

fdisk enters interactive mode. Key commands:
- p: print the current partition table
- n: create a new partition
- d: delete a partition
- t: change the partition type
- w: write the table and exit (this commits the changes)
- q: quit without saving

When creating a partition, fdisk asks for: partition number, first sector (accept the default
to use the next available sector), and last sector (use +10G format to specify size).

```bash
sudo gdisk /dev/sdb
```

gdisk works identically for GPT disks. Same keystrokes: p, n, d, w, q.

After creating partitions:

```bash
sudo partprobe /dev/sdb
```

partprobe tells the kernel to re-read the partition table without rebooting. Required after
fdisk or gdisk when the disk is already in use.

---

### Section 3: Creating Filesystems

[SHOW TERMINAL]

A partition is just raw space until you format it with a filesystem. The filesystem provides
the structure for storing files: directory entries, inode tables, data blocks.

```bash
sudo mkfs.ext4 /dev/sdb1
```

Creates an ext4 filesystem on partition sdb1. ext4 is the standard Linux filesystem: journaled
(crash recovery), mature, widely supported.

```bash
sudo mkfs.xfs /dev/sdb2
```

Creates an XFS filesystem. XFS is the default on RHEL and is optimized for large files and
high-throughput workloads. XFS cannot be shrunk (only grown).

```bash
sudo mkfs.ext4 -L "datastore" /dev/sdb1
```

The -L flag sets a filesystem label. Labels are used in /etc/fstab as LABEL=datastore instead
of device names.

```bash
sudo blkid /dev/sdb1
```

blkid shows the UUID and filesystem type of a partition. UUIDs are the preferred way to
identify partitions in /etc/fstab because they do not change when disks are added or removed.

---

### Section 4: Mounting Filesystems

[SHOW TERMINAL]

```bash
sudo mkdir /mnt/data
sudo mount /dev/sdb1 /mnt/data
```

Mount the filesystem at the mount point /mnt/data. The mount point must exist before mounting.

```bash
mount | grep sdb1
df -h /mnt/data
```

Verify the mount. df -h shows total, used, and available space.

```bash
sudo umount /mnt/data
```

Unmount the filesystem. You must not be inside the mount point directory when you unmount.

---

### Section 5: Persistent Mounts with /etc/fstab

[SHOW TERMINAL]

```bash
cat /etc/fstab
```

fstab defines which filesystems are mounted at boot. Each line has six fields:

```
DEVICE  MOUNT_POINT  FSTYPE  OPTIONS  DUMP  PASS
```

Fields:
- DEVICE: UUID=, LABEL=, or /dev/name (UUID preferred)
- MOUNT_POINT: The directory to mount to
- FSTYPE: ext4, xfs, vfat, nfs, etc.
- OPTIONS: defaults, ro, noexec, user, etc.
- DUMP: 0 (backup utility — nearly always 0)
- PASS: 0 (no fsck), 1 (root partition), 2 (other partitions — checked after root)

A correct fstab entry for a data partition:

```
UUID=a1b2c3d4-e5f6-7890-abcd-ef1234567890  /mnt/data  ext4  defaults  0  2
```

Never use device names like /dev/sdb1 in fstab. Device names can change when disks are
added or removed, causing boot failures.

After editing fstab:

```bash
sudo mount -a
```

mount -a attempts to mount all entries in fstab. If it fails, your fstab has an error. Fix
the error before rebooting — a bad fstab can prevent the system from booting.

```bash
sudo systemd-analyze verify /etc/fstab
```

Validates the fstab syntax before you commit to rebooting.

---

### Section 6: Common Mount Options

| Option | Effect |
|--------|--------|
| defaults | rw, suid, dev, exec, auto, nouser, async |
| ro | Read-only mount |
| noexec | Prevent executing files on this filesystem |
| nosuid | Ignore SUID/SGID bits on this filesystem |
| nodev | Do not interpret character or block device files |
| user | Allow any user to mount (automount) |
| nofail | Boot continues even if this mount fails (useful for optional drives) |

noexec, nosuid, and nodev together provide strong security hardening for filesystem mounts
that hold user data or temporary files.

---

### Certification Connection

Partitioning and filesystems map to Linux+ Domain 1.0 (System Management). Key exam objectives:

Know MBR versus GPT: MBR max 4 primary partitions, 2 TB limit; GPT max 128 partitions, no
practical size limit.

Know mkfs commands: mkfs.ext4 for ext4, mkfs.xfs for XFS.

Know fstab fields in order: device, mount point, fstype, options, dump, pass.

Know why UUIDs are preferred over device names in fstab.

Know mount -a to test fstab entries without rebooting.

---

### Transition to Part 2

In Part 2 we cover LVM and software RAID. LVM adds a flexible management layer above raw
partitions. RAID protects against disk failure.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
