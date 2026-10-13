# Video Script: Module 06 — Storage and Disk Management (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Production Notes

- **Screen recording**: Terminal emulator; use VM with spare physical volumes for LVM demo
- **Demonstrations**: Show complete LVM workflow — pvcreate through lvextend
- **Slide overlays**: LVM architecture diagram (PV → VG → LV); RAID level comparison table
- **Pacing**: LVM commands have verbose output — allow screen to settle before continuing narration

---

## SEGMENT 1 — Opening and Recap (0:00–1:00)

### Narration

Welcome back to Module 06, Part 2. In Part 1 we covered block devices, partitioning, formatting, and persistent mounts. Now we address the advanced storage topics: LVM for flexible volume management, swap space, RAID concepts, and disk health monitoring. These are the tools that make enterprise Linux storage manageable at scale.

---

## SEGMENT 2 — LVM: Logical Volume Manager (1:00–7:30)

### Narration

Physical partitions have a fundamental limitation: you cannot easily resize them after the fact. If you allocate 50GB to `/var` and it fills up, you are stuck unless you have adjacent free space. LVM — the Logical Volume Manager — solves this by adding an abstraction layer between physical storage and the filesystem.

The LVM architecture has three layers:

### Slide Overlay: LVM Architecture

```
Physical Disks/Partitions
         |
   Physical Volumes (PV)
         |
    Volume Group (VG)   <-- pool of storage
         |
   Logical Volumes (LV) <-- what you format and mount
```

- **Physical Volume (PV)** — a disk or partition prepared for LVM use
- **Volume Group (VG)** — one or more PVs combined into a single storage pool
- **Logical Volume (LV)** — a "virtual partition" carved from the VG; this is what you format and mount

The key insight: a logical volume can span multiple physical disks, and you can extend a logical volume by adding more physical volumes to its volume group — online, without unmounting.

### Creating a Physical Volume

### On-Screen Demo

```bash
# Prepare a partition or disk for LVM
sudo pvcreate /dev/sdb1

# Verify
sudo pvdisplay /dev/sdb1
sudo pvs
```

### Narration

`pvcreate` writes the LVM label to the device. `pvs` gives a concise summary; `pvdisplay` gives detailed information.

### Creating a Volume Group

### On-Screen Demo

```bash
# Create a volume group named "datavg" from the physical volume
sudo vgcreate datavg /dev/sdb1

# Verify
sudo vgs
sudo vgdisplay datavg
```

### Narration

The volume group is now the pool. Its total size is the size of all physical volumes assigned to it. You can add more PVs to expand the pool later.

### Creating a Logical Volume

### On-Screen Demo

```bash
# Create a 1GB logical volume named "datalv" in "datavg"
sudo lvcreate -L 1G -n datalv datavg

# Or use a percentage of the VG
sudo lvcreate -l 50%FREE -n datalv datavg

# Verify
sudo lvs
sudo lvdisplay /dev/datavg/datalv
```

### Narration

The logical volume device path is `/dev/VG_NAME/LV_NAME` — in this case `/dev/datavg/datalv`. There is also a symlink at `/dev/mapper/datavg-datalv`.

### Format and Mount

### On-Screen Demo

```bash
sudo mkfs.ext4 /dev/datavg/datalv
sudo mkdir -p /mnt/lvm_data
sudo mount /dev/datavg/datalv /mnt/lvm_data
df -h /mnt/lvm_data
```

### Narration

Now for the real power of LVM: extending an online volume. Suppose `/mnt/lvm_data` is running low on space. We can extend it without unmounting:

### On-Screen Demo

```bash
# First, add another physical volume if the VG is full
# (Assume /dev/sdc1 is another prepared partition)
sudo pvcreate /dev/sdc1
sudo vgextend datavg /dev/sdc1

# Extend the logical volume by 500MB
sudo lvextend -L +500M /dev/datavg/datalv

# The LV is larger but the FILESYSTEM inside it does not know yet
# Resize the ext4 filesystem to fill the LV:
sudo resize2fs /dev/datavg/datalv

# For xfs filesystems, the command is different:
# sudo xfs_growfs /mnt/lvm_data

# Verify
df -h /mnt/lvm_data
```

### Narration

This is the workflow you will perform repeatedly in production: `lvextend` to expand the logical volume, then `resize2fs` (ext4) or `xfs_growfs` (xfs) to expand the filesystem to fill the new space. Both can be done while the filesystem is mounted and in use.

Note: ext4 can also be shrunk offline. xfs cannot be shrunk — xfs is grow-only.

---

## SEGMENT 3 — Swap Space (7:30–9:30)

### Narration

Swap is disk space that the Linux kernel uses as overflow when physical RAM is full. It is much slower than RAM — read/write times on even an SSD are orders of magnitude slower than DRAM — but it prevents the out-of-memory killer from terminating processes unexpectedly.

Creating swap on a partition:

### On-Screen Demo

```bash
# Format a partition as swap
sudo mkswap /dev/sdb2

# Activate it
sudo swapon /dev/sdb2

# Verify
swapon --show
free -h
```

### Narration

You can also create swap as a file rather than a partition — useful on cloud instances where adding partitions requires stopping the VM:

### On-Screen Demo

```bash
# Create a 1GB swap file
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Verify
swapon --show
```

### Narration

To make swap permanent, add it to fstab:

```
UUID=...  none  swap  sw  0  0
# or for a swap file:
/swapfile  none  swap  sw  0  0
```

The mountpoint is `none` for swap, the fstype is `swap`, and both dump and pass are 0.

To deactivate swap:

```bash
sudo swapoff /dev/sdb2
sudo swapoff /swapfile
```

---

## SEGMENT 4 — RAID Concepts (9:30–11:30)

### Narration

RAID — Redundant Array of Independent Disks — combines multiple physical drives for either performance, redundancy, or both. You need to understand the RAID levels conceptually for Linux+ even if you do not configure hardware RAID.

### Slide Overlay: RAID Levels

| Level | Drives | Redundancy | Performance | Notes |
|---|---|---|---|---|
| RAID 0 | 2+ | None | Excellent | Striping; failure of any disk = total loss |
| RAID 1 | 2 | Full mirror | Read fast | Mirroring; 50% usable capacity |
| RAID 5 | 3+ | 1 disk failure | Good | Distributed parity; any single disk can fail |
| RAID 10 | 4 | 1 per mirror | Best | Mirrored stripes; expensive but reliable |

### Narration

Linux supports software RAID through `mdadm` — the Multiple Disk Administration tool. While hardware RAID controllers offload the work to dedicated chips, software RAID is entirely managed by the kernel and works on any disks. The trade-off: software RAID consumes CPU; hardware RAID does not.

A quick conceptual example — creating a RAID 1 mirror with mdadm:

### On-Screen Demo

```bash
# This is a CONCEPTUAL DEMO — do not run in lab without two dedicated spare disks
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc

# Monitor the rebuild
cat /proc/mdstat

# The md device is then used like any block device:
sudo mkfs.ext4 /dev/md0
sudo mount /dev/md0 /mnt/raid1
```

### Narration

`/proc/mdstat` shows the state of all md devices. The rebuild (synchronization) of a new RAID array can take from minutes to hours depending on disk size and speed.

---

## SEGMENT 5 — Filesystem Health: fsck and smartctl (11:30–14:00)

### Narration

Filesystems can become inconsistent due to power failures, kernel bugs, or hardware issues. `fsck` — the filesystem consistency check — inspects and repairs a filesystem.

Critical rule: **never run fsck on a mounted filesystem**. Running fsck on a live mounted filesystem will corrupt it. fsck must run on unmounted filesystems. For the root filesystem, this means running from a rescue environment or allowing boot-time fsck.

### On-Screen Demo

```bash
# Unmount first (never run on mounted filesystems)
sudo umount /mnt/data

# Run fsck — it will ask before fixing each issue
sudo fsck /dev/sdb1

# Run non-interactively, fixing everything automatically (-y = yes to all)
sudo fsck -y /dev/sdb1

# Force a check even if the filesystem is marked clean
sudo fsck -f /dev/sdb1
```

### Narration

For xfs filesystems, use `xfs_repair` instead of fsck.

The fstab "pass" field (the sixth column) controls automatic fsck at boot. Setting it to 2 for non-root partitions enables periodic boot-time checks.

Now for disk hardware health: `smartctl` reads SMART (Self-Monitoring, Analysis and Reporting Technology) data directly from the drive's firmware:

### On-Screen Demo

```bash
# Install smartmontools if needed
sudo apt install smartmontools

# Run a quick health check
sudo smartctl -H /dev/sda

# View all SMART data
sudo smartctl -a /dev/sda | head -40

# Run a short self-test (takes ~2 minutes)
sudo smartctl -t short /dev/sda

# View test results
sudo smartctl -l selftest /dev/sda
```

### Narration

The most important SMART attributes: `Reallocated_Sector_Ct` — a growing count means the drive is remapping bad sectors; `Current_Pending_Sector` — sectors with uncorrectable read errors; `Offline_Uncorrectable` — sectors that failed during offline testing. Any non-zero value in these attributes warrants immediate backup and drive replacement planning.

---

## SEGMENT 6 — df vs. du for Space Analysis (14:00–15:00)

### Narration

A quick but important distinction to close: `df` and `du` measure disk space differently.

`df` — **disk free** — asks the filesystem itself how much space is used and free. It reports at the mounted filesystem level. Fast, but shows the filesystem's bookkeeping, not the actual file sizes.

`du` — **disk usage** — walks the directory tree and sums file sizes. It measures actual data. Slower on large directories, but tells you exactly where space is going.

### On-Screen Demo

```bash
# See overall filesystem usage
df -h

# Find which directory is consuming space
du -sh /var/*  2>/dev/null | sort -hr | head -10

# Find large files
find /var -type f -size +100M 2>/dev/null
```

### Narration

The combination of `df` to identify which filesystem is full and `du` to find what is filling it is the standard troubleshooting pattern for "disk full" incidents — one of the most common sysadmin calls in production.

That completes Module 06. You now have a complete picture of Linux storage management: from raw block devices through partitioning, formatting, mounting, LVM, swap, RAID, and health monitoring. Module 07 moves to user and group administration. See you there.

---

## Summary Slide

### Part 2 Key Concepts

- LVM layers: PV → VG → LV; `pvcreate`, `vgcreate`, `lvcreate`
- Extend LV: `lvextend -L +SIZE`, then `resize2fs` (ext4) or `xfs_growfs` (xfs)
- Swap: `mkswap`, `swapon`/`swapoff`; fstab fstype = `swap`, mountpoint = `none`
- RAID 0 = striping (speed, no redundancy); RAID 1 = mirroring; RAID 5 = distributed parity; RAID 10 = mirrored stripes
- `mdadm` — software RAID management; `/proc/mdstat` — rebuild status
- `fsck /dev/sdXN` — repair filesystem; must be unmounted first
- `smartctl -H /dev/sda` — SMART health check; growing reallocated sectors = replace drive
- `df -h` — filesystem totals; `du -sh dir/*` — per-directory usage

---

*End of Module 06 Part 2 Script*
