# Reading Guide: Module 06 — Storage and Disk Management

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Overview

This reading guide supports Module 06. Storage management is one of the most hands-on skills in Linux administration. Understanding the layered model — from physical hardware through partitions, filesystems, and mount points — allows you to confidently provision, expand, and troubleshoot storage on any Linux system.

---

## Section 1 — Block Devices

### 1.1 Device File Naming

| Device Type | Pattern | Example |
|---|---|---|
| SATA/SAS disk | `/dev/sdX` | `/dev/sda`, `/dev/sdb` |
| NVMe SSD | `/dev/nvmeXnY` | `/dev/nvme0n1` |
| VirtIO (VM) | `/dev/vdX` | `/dev/vda` |
| IDE (legacy) | `/dev/hdX` | `/dev/hda` |
| SCSI CD-ROM | `/dev/srX` | `/dev/sr0` |

Partitions are numbered: `/dev/sda1`, `/dev/sda2`. NVMe uses `p` prefix: `/dev/nvme0n1p1`.

### 1.2 Essential Discovery Commands

```bash
lsblk              # Tree view: device → partitions → mountpoints
lsblk -f           # Add filesystem type and UUID
blkid              # Show UUID, label, and filesystem type per device
blkid /dev/sda1    # Specific device
```

---

## Section 2 — Partition Tables

### 2.1 MBR vs GPT

| Feature | MBR | GPT |
|---|---|---|
| Max partitions | 4 primary | 128 (default) |
| Max disk size | 2 TB | 9.4 ZB |
| Boot system | BIOS | UEFI (+ legacy BIOS) |
| Backup table | None | Yes, at end of disk |
| Year introduced | 1983 | 2010 |

### 2.2 When to Use Each

Use MBR only when working with older hardware that requires BIOS boot, or when the disk is under 2 TB on a legacy system. Use GPT for all new deployments — it is more flexible and more reliable.

---

## Section 3 — Partitioning with fdisk and gdisk

### 3.1 fdisk Interactive Commands

```
p   — print partition table
n   — new partition
d   — delete partition
t   — change partition type
g   — create new GPT partition table
o   — create new MBR partition table
w   — write changes (commits — no undo)
q   — quit without saving
```

### 3.2 gdisk Partition Type Codes

| Hex Code | Partition Type |
|---|---|
| 8300 | Linux filesystem |
| 8200 | Linux swap |
| 8e00 | Linux LVM |
| ef00 | EFI System Partition |
| fd00 | Linux RAID |

### 3.3 Size Specifiers

When creating a partition, specify the last sector using:

- `+2G` — 2 gigabytes
- `+500M` — 500 megabytes
- `+10G` — 10 gigabytes
- (blank) — use remaining space

---

## Section 4 — Filesystem Creation (mkfs)

### 4.1 Common Filesystem Types

| Filesystem | Command | Notes |
|---|---|---|
| ext4 | `mkfs.ext4` or `mkfs -t ext4` | Default on Debian/Ubuntu; resize both ways |
| xfs | `mkfs.xfs` | Default on RHEL/CentOS; grow only |
| btrfs | `mkfs.btrfs` | Copy-on-write; snapshots; SUSE default |
| vfat | `mkfs.vfat` | FAT32; used for EFI partition |
| swap | `mkswap` | Swap space (not really a filesystem) |

### 4.2 mkfs Options

```bash
mkfs.ext4 /dev/sdb1                     # Basic
mkfs.ext4 -L "backups" /dev/sdb1        # With label
mkfs.ext4 -m 1 /dev/sdb1               # Reserved blocks: 1% instead of default 5%
mkfs.xfs /dev/sdb1
mkfs.xfs -L "xfsdata" /dev/sdb1
```

---

## Section 5 — Mounting

### 5.1 Temporary Mount

```bash
sudo mount /dev/sdb1 /mnt/data          # Device path
sudo mount -t ext4 /dev/sdb1 /mnt/data  # Explicit type
sudo mount UUID=xxxx-xxxx /mnt/data     # By UUID
sudo mount LABEL=backups /mnt/data      # By label
sudo mount -o ro /dev/sdb1 /mnt/data    # Read-only
sudo umount /mnt/data                   # By mountpoint
sudo umount /dev/sdb1                   # By device
```

### 5.2 /etc/fstab Fields

```
DEVICE  MOUNTPOINT  FSTYPE  OPTIONS  DUMP  PASS
```

| Field | Description |
|---|---|
| Device | Path, UUID, or LABEL |
| Mountpoint | Directory where mounted; `none` for swap |
| FStype | ext4, xfs, btrfs, swap, nfs, tmpfs |
| Options | Comma-separated; `defaults` = rw,suid,dev,exec,auto,nouser,async |
| Dump | 0 = no backup tool inclusion; 1 = include |
| Pass | 0 = no fsck; 1 = root filesystem; 2 = other filesystems |

### 5.3 Common fstab Options

| Option | Meaning |
|---|---|
| `defaults` | Standard read-write with standard options |
| `ro` | Read-only |
| `noexec` | Prevent execution of binaries on this filesystem |
| `nosuid` | Ignore setuid/setgid bits |
| `noatime` | Do not update access time on read (performance gain) |
| `nofail` | Do not fail boot if device is absent |
| `x-systemd.automount` | Automount on first access |

### 5.4 fstab Entry Examples

```
# ext4 partition by UUID
UUID=abc123  /data  ext4  defaults  0  2

# xfs partition by label
LABEL=xfsdata  /storage  xfs  defaults,noatime  0  2

# Swap partition
UUID=def456  none  swap  sw  0  0

# Swap file
/swapfile  none  swap  sw  0  0

# NFS share
192.168.1.10:/exports/home  /home/remote  nfs  defaults  0  0
```

### 5.5 Testing fstab Without Rebooting

```bash
sudo mount -a      # Mount everything in fstab not already mounted
```

If an error occurs, the problem entry is printed. Fix it before rebooting.

---

## Section 6 — LVM

### 6.1 Architecture

```
Physical Volumes (pvcreate) → Volume Group (vgcreate) → Logical Volumes (lvcreate)
```

### 6.2 Physical Volume Commands

```bash
pvcreate /dev/sdb1          # Initialize PV
pvs                         # Summary
pvdisplay /dev/sdb1         # Detailed
pvremove /dev/sdb1          # Remove PV label (must not be in a VG)
```

### 6.3 Volume Group Commands

```bash
vgcreate myvg /dev/sdb1            # Create VG
vgextend myvg /dev/sdc1            # Add PV to VG
vgs                                # Summary
vgdisplay myvg                     # Detailed
vgreduce myvg /dev/sdc1            # Remove PV from VG (if space allows)
```

### 6.4 Logical Volume Commands

```bash
lvcreate -L 5G -n mylv myvg          # Fixed size
lvcreate -l 100%FREE -n mylv myvg    # All free space
lvcreate -l 50%VG -n mylv myvg       # Percent of VG
lvs                                   # Summary
lvdisplay /dev/myvg/mylv             # Detailed
lvextend -L +2G /dev/myvg/mylv       # Extend by 2G
lvextend -l +100%FREE /dev/myvg/mylv # Use all free space
lvremove /dev/myvg/mylv              # Delete LV (unmount first)
```

### 6.5 Filesystem Extension After lvextend

```bash
# ext4 — can resize online (mounted)
resize2fs /dev/myvg/mylv

# xfs — can resize online (mounted); requires mount point, not device
xfs_growfs /mountpoint
```

### 6.6 Device Path Aliases

LVM creates two equivalent paths for every logical volume:

- `/dev/VG_NAME/LV_NAME` — symlink (user-friendly)
- `/dev/mapper/VG_NAME-LV_NAME` — mapper device (replace hyphens with double-hyphens if names contain them)

---

## Section 7 — Swap Space

### 7.1 Creating Swap on a Partition

```bash
sudo mkswap /dev/sdb2           # Format as swap
sudo swapon /dev/sdb2           # Activate
sudo swapoff /dev/sdb2          # Deactivate
swapon --show                   # List active swap areas
```

### 7.2 Creating a Swap File

```bash
sudo fallocate -l 2G /swapfile     # Create file (fallocate is fastest)
# OR: sudo dd if=/dev/zero of=/swapfile bs=1M count=2048
sudo chmod 600 /swapfile           # Restrict permissions (required)
sudo mkswap /swapfile
sudo swapon /swapfile
```

### 7.3 Swappiness

The `vm.swappiness` kernel parameter (0–100) controls how aggressively Linux uses swap. Default is 60. Setting it to 10 makes Linux prefer keeping data in RAM longer.

```bash
cat /proc/sys/vm/swappiness         # Current value
sudo sysctl vm.swappiness=10        # Temporary change
# For permanent: add "vm.swappiness=10" to /etc/sysctl.conf
```

---

## Section 8 — RAID

### 8.1 RAID Levels

| Level | Min Disks | Redundancy | Usable Space | Use Case |
|---|---|---|---|---|
| RAID 0 | 2 | None | 100% | Maximum performance, no fault tolerance |
| RAID 1 | 2 | 1 disk failure | 50% | Boot/OS volumes requiring high availability |
| RAID 5 | 3 | 1 disk failure | (N-1)/N | Balanced performance and redundancy |
| RAID 6 | 4 | 2 disk failures | (N-2)/N | Large arrays where dual failure is a risk |
| RAID 10 | 4 | 1 per mirror set | 50% | High performance + redundancy for databases |

### 8.2 mdadm Quick Reference

```bash
# Create RAID 1
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc

# Monitor rebuild
cat /proc/mdstat
watch cat /proc/mdstat

# Save RAID configuration
sudo mdadm --detail --scan >> /etc/mdadm/mdadm.conf

# Check RAID status
sudo mdadm --detail /dev/md0

# Stop array
sudo mdadm --stop /dev/md0
```

---

## Section 9 — Filesystem Health

### 9.1 fsck

```bash
sudo fsck /dev/sdb1           # Interactive repair
sudo fsck -y /dev/sdb1        # Auto-fix everything (yes to all)
sudo fsck -f /dev/sdb1        # Force check (even if marked clean)
sudo fsck -n /dev/sdb1        # Dry run (read-only check, no repair)
```

Rules:

- NEVER run fsck on a mounted filesystem
- For root filesystem, boot from rescue media or use single-user mode
- xfs uses `xfs_repair /dev/sdb1` instead of fsck

### 9.2 SMART Monitoring with smartctl

```bash
sudo smartctl -H /dev/sda             # Quick health status
sudo smartctl -a /dev/sda             # All SMART attributes
sudo smartctl -t short /dev/sda       # Short self-test (~2 min)
sudo smartctl -t long /dev/sda        # Extended self-test (~hours)
sudo smartctl -l selftest /dev/sda    # Test results log
```

### Critical SMART Attributes

| Attribute | ID | Concern |
|---|---|---|
| Reallocated_Sector_Ct | 5 | Growing count = dying drive |
| Spin_Retry_Count | 10 | NZ on SSD = concerning |
| Current_Pending_Sector | 197 | Unstable sectors pending reallocation |
| Offline_Uncorrectable | 198 | Unrecoverable read errors |
| UDMA_CRC_Error_Count | 199 | Cable/interface errors |

---

## Section 10 — df vs. du

| Tool | Measures | Speed | Use For |
|---|---|---|---|
| `df -h` | Filesystem reported usage | Fast | How full is the filesystem? |
| `du -sh dir` | Sum of file sizes in directory | Slow (walks tree) | What is using the space? |

```bash
# Identify full filesystem
df -h

# Find the directory consuming space (start at top)
du -sh /var/*  2>/dev/null | sort -hr | head -10

# Drill down
du -sh /var/log/* | sort -hr | head -10

# Find individual large files
find / -type f -size +100M 2>/dev/null
```

---

## CompTIA Linux+ Exam Relevance

- **1.4** — Given a scenario, configure and manage storage
- **2.5** — Given a scenario, implement storage management

Expect exam questions on:

- MBR vs GPT limitations and when to use each
- The six fields of /etc/fstab and what each controls
- Why UUID is preferred over device name in fstab
- LVM command sequence: pvcreate → vgcreate → lvcreate
- RAID level redundancy characteristics
- Why fsck must not run on mounted filesystems
- The difference between `resize2fs` (ext4) and `xfs_growfs` (xfs)

---

## Key Terms

- **Block device** — hardware abstraction that allows random read/write access in fixed-size blocks; represented as files in `/dev`
- **Partition table** — data structure at the start of a disk describing partition boundaries; either MBR or GPT
- **UUID** — Universally Unique Identifier; stable 128-bit identifier for a formatted partition; preferred for fstab
- **Physical Volume (PV)** — a disk or partition initialized for LVM
- **Volume Group (VG)** — storage pool combining one or more PVs
- **Logical Volume (LV)** — virtual partition carved from a VG; formatted and mounted like a regular partition
- **Swap space** — disk area used as RAM overflow; much slower than physical RAM
- **RAID** — Redundant Array of Independent Disks; combines multiple disks for performance and/or redundancy
- **fsck** — filesystem consistency check; must run only on unmounted filesystems
- **SMART** — Self-Monitoring, Analysis and Reporting Technology; disk firmware self-diagnostics

---

*End of Module 06 Reading Guide*
