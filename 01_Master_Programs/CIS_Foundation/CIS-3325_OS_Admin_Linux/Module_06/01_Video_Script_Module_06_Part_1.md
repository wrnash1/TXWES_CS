# Video Script: Module 06 — Storage and Disk Management (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Production Notes

- **Screen recording**: Terminal emulator (dark theme, 18pt font); use a VM with an unpartitioned spare disk for live demos
- **Demonstrations**: Use /dev/sdb (the second disk in the VM) as the demo target; narrate all destructive operations clearly before executing
- **Slide overlays**: MBR vs GPT comparison table; fstab field diagram
- **Safety warning**: Display a red "DEMO DISK ONLY" banner during fdisk/mkfs/mount demos

---

## SEGMENT 1 — Opening and Context (0:00–1:30)

### Narration

Welcome to Module 06, Part 1: Storage and Disk Management. I'm Professor Nash.

Storage is where data lives. If you manage Linux systems, you will provision storage for new servers, expand volumes that are running out of space, replace failed disks, and troubleshoot mount failures. Getting storage wrong can mean data loss, system instability, or a server that will not boot.

This module covers the complete lifecycle: understanding the hardware abstraction, partitioning, formatting, mounting, and making mounts persistent. Part 2 adds LVM for flexible volume management, swap space, RAID concepts, and disk health monitoring.

The CompTIA Linux+ objectives this module addresses are 1.4 (disk partitions, file systems, and mounting) and 2.5 (storage management).

---

## SEGMENT 2 — Block Devices and Device Files (1:30–3:30)

### Narration

Linux represents storage devices as block device files in the `/dev` directory. The naming convention tells you the type and order of the device.

Traditional SATA and SAS drives: `/dev/sda`, `/dev/sdb`, `/dev/sdc` — alphabetical order of detection.

NVMe drives — the modern high-speed protocol: `/dev/nvme0n1`, `/dev/nvme1n1`. The `nvme0` is the controller number, `n1` is the namespace.

Virtual machine disks (VirtIO): `/dev/vda`, `/dev/vdb`.

Partitions within a drive are numbered: `/dev/sda1`, `/dev/sda2`, `/dev/sda3`. For NVMe: `/dev/nvme0n1p1`, `/dev/nvme0n1p2`.

### On-Screen Demo

```bash
# List block devices
lsblk

# Show detailed device information
lsblk -f

# List devices with their UUIDs and filesystem types
blkid
```

### Narration

`lsblk` is your first command when orienting yourself to a system's storage layout. It shows a tree: device, then partitions, then where they are mounted. The `-f` flag adds filesystem type and UUID — essential for fstab configuration.

`blkid` shows the block ID — specifically the UUID of each formatted partition. You will use this when writing persistent mount entries.

---

## SEGMENT 3 — Partition Tables: MBR vs GPT (3:30–5:30)

### Narration

Before you can create partitions, you need to understand the partition table — the data structure at the beginning of a disk that describes the partition layout.

There are two standards:

**MBR** — Master Boot Record. The original IBM PC standard. Located in the first 512 bytes of the disk. Limitations: maximum 4 primary partitions (or 3 primary + 1 extended with logical partitions inside), and maximum disk size of 2 TB. Still found on older systems and 32-bit hardware.

**GPT** — GUID Partition Table. The modern standard, part of the UEFI specification. Supports up to 128 partitions by default, supports disks larger than 2 TB (up to 9.4 ZB theoretically), and includes a backup partition table at the end of the disk for resilience. GPT is what you should use for all new installations on modern hardware.

### Slide Overlay: MBR vs GPT

| Feature | MBR | GPT |
|---|---|---|
| Max partitions | 4 primary | 128 (default) |
| Max disk size | 2 TB | 9.4 ZB |
| Boot system | BIOS | UEFI (also legacy BIOS) |
| Redundancy | None | Backup table at disk end |
| Age | 1983 | 2010 |

### Narration

The partitioning tools map to the partition table type: `fdisk` works with both MBR and GPT (modern versions), and `gdisk` is a GPT-specific tool modeled on fdisk's interface.

---

## SEGMENT 4 — fdisk and gdisk: Partitioning (5:30–9:00)

### Narration

Let's partition a disk. I am working with `/dev/sdb` — a blank second disk in my VM. In your lab, substitute the correct device for your environment. Never run these commands against your system disk — verify the target with `lsblk` first.

### On-Screen Demo

```bash
# Always verify the target first
lsblk
```

### Narration

fdisk is interactive. Launch it with the device as an argument:

### On-Screen Demo

```bash
sudo fdisk /dev/sdb
```

### Narration

Inside fdisk, the key commands:

- `p` — print (display) the current partition table
- `n` — new partition
- `d` — delete a partition
- `t` — change partition type
- `g` — create a new GPT partition table (wipes existing partitions!)
- `o` — create a new MBR partition table
- `w` — write changes and exit (this commits your changes — no undo)
- `q` — quit without saving

### On-Screen Demo

*Inside fdisk: press p, then n, accept defaults for first sector, enter +2G for last sector, press p again to confirm, then w to write*

```
Command (m for help): p
Command (m for help): n
Partition number: [Enter for 1]
First sector: [Enter for default]
Last sector: +2G
Command (m for help): p
Command (m for help): w
```

### Narration

The `+2G` notation for the last sector tells fdisk to make the partition 2 gigabytes. You can also use `+500M`, `+10G`, etc.

For GPT disks, `gdisk` provides the same interface with GPT-specific behavior. The commands are nearly identical:

### On-Screen Demo

```bash
sudo gdisk /dev/sdb
```

```
Command: p
Command: n
Partition number: 1
First sector: [Enter]
Last sector: +2G
Hex code: [Enter for 8300 = Linux filesystem]
Command: w
```

### Narration

The hex code in gdisk specifies the partition type. `8300` is "Linux filesystem." Other common types: `8200` is Linux swap, `ef00` is EFI System Partition, `8e00` is Linux LVM.

After writing, verify the partition was created:

### On-Screen Demo

```bash
lsblk /dev/sdb
```

---

## SEGMENT 5 — mkfs: Creating Filesystems (9:00–11:00)

### Narration

A partition is just a region of a disk. To store files, you must format it with a filesystem. This is the `mkfs` command family.

The three filesystems you need to know for Linux+:

**ext4** — the dominant Linux filesystem. Mature, stable, journaled, widely supported. The safe default choice.

**xfs** — default on RHEL/CentOS/Fedora. High performance, especially for large files. Journaled. Can be grown online but cannot be shrunk.

**btrfs** — modern copy-on-write filesystem with built-in snapshots, RAID, and subvolumes. Still maturing in production environments but used in SUSE and some Fedora configurations.

### On-Screen Demo

```bash
# Format the partition we just created as ext4
sudo mkfs.ext4 /dev/sdb1

# Format as xfs
sudo mkfs.xfs /dev/sdb1   # Would need to wipe ext4 first

# Format with a label (human-readable name)
sudo mkfs.ext4 -L "datastore" /dev/sdb1
```

### Narration

`mkfs.ext4` is a symlink to `mke2fs` with ext4 options. There is also `mkfs -t ext4` — all equivalent.

The label (`-L`) is optional but useful — you can reference a labeled partition in fstab as `LABEL=datastore` instead of by device path.

After formatting, verify:

### On-Screen Demo

```bash
blkid /dev/sdb1
```

---

## SEGMENT 6 — mount, umount, and /etc/fstab (11:00–15:00)

### Narration

Formatting creates the filesystem. Mounting makes it accessible at a path in the Linux directory tree.

### On-Screen Demo

```bash
# Create a mountpoint
sudo mkdir -p /mnt/data

# Mount the filesystem
sudo mount /dev/sdb1 /mnt/data

# Verify it is mounted
mount | grep sdb1
df -h /mnt/data
lsblk
```

### Narration

The mount is now active, but it is not persistent — if you reboot, `/mnt/data` will be empty again because the mount entry was not saved anywhere. To make it persistent, we need `/etc/fstab`.

### Slide Overlay: /etc/fstab Fields

```
Device   Mountpoint   FStype   Options   Dump   Pass
/dev/sdb1  /mnt/data  ext4    defaults   0      2
```

Field meanings:

1. **Device** — the device, label, or UUID
2. **Mountpoint** — where to attach in the directory tree
3. **FStype** — filesystem type (ext4, xfs, nfs, tmpfs, etc.)
4. **Options** — mount options; `defaults` means rw, suid, dev, exec, auto, nouser, async
5. **Dump** — backup tool flag; 0 = skip, 1 = include. Almost always 0 in modern systems.
6. **Pass** — fsck order; 0 = skip, 1 = check first (root only), 2 = check after root. Root partition = 1, others = 2.

### Narration

Using device paths like `/dev/sdb1` in fstab is risky because device names can change if you add or remove drives. The preferred approach is to use the UUID, which is stable:

### On-Screen Demo

```bash
# Get the UUID
blkid /dev/sdb1
```

### Narration

Copy that UUID and add an entry to fstab:

### On-Screen Demo

```bash
sudo vim /etc/fstab

# Add this line (substituting your actual UUID):
# UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /mnt/data  ext4  defaults  0  2
```

### Narration

Before rebooting, always test your fstab entry:

### On-Screen Demo

```bash
# Unmount first
sudo umount /mnt/data

# Use mount -a to mount everything in fstab that is not already mounted
sudo mount -a

# Verify
df -h /mnt/data
```

### Narration

If `mount -a` shows an error, fix the fstab entry before rebooting. A corrupted fstab entry for a non-root filesystem causes boot to pause at a recovery prompt. For the root filesystem, a bad fstab can prevent the system from booting entirely.

To unmount a filesystem: `umount /mnt/data` or `umount /dev/sdb1`. If the filesystem is busy (files open on it), umount will refuse. Use `lsof /mnt/data` to find what has files open there.

That completes Part 1. You can now identify block devices, create partitions, format filesystems, and make mounts persistent. In Part 2 we cover LVM, swap, RAID concepts, and disk health tools. See you there.

---

## Summary Slide

### Part 1 Key Concepts

- Block devices: `/dev/sda` (SATA), `/dev/nvme0n1` (NVMe); partitions add numbers
- `lsblk` — tree view of devices and mounts; `blkid` — UUIDs and filesystem types
- MBR: 4 partitions max, 2 TB max; GPT: 128 partitions, any modern size
- `fdisk /dev/sdX` — interactive partitioning (MBR/GPT); `gdisk` — GPT-focused
- `mkfs.ext4`, `mkfs.xfs` — format partitions
- `mount /dev/sdb1 /mountpoint` — attach filesystem; `umount` — detach
- `/etc/fstab` — 6 fields: device, mountpoint, fstype, options, dump, pass
- Use UUID (from `blkid`) in fstab, not device names

---

*End of Module 06 Part 1 Script*
