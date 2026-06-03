# Video Script: Module 13 — Storage and Logical Volume Management (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome back to Module 13, Part 2.

In Part 1, we built and managed LVM storage. Now we need to put filesystems on those volumes and make them accessible to the operating system. We'll cover `mkfs`, `mount`, and the critical `/etc/fstab` file that makes mounts persistent. Then we'll examine disk usage tools `df` and `du`, and close with RAID levels — a topic the Linux+ exam tests consistently.

---

### Section 7: Creating Filesystems

A logical volume (or partition) is just raw block storage. Before it can hold files, it needs a filesystem — a data structure that organizes how files are stored and retrieved.

**Common Linux Filesystems**

- **ext4** — the most widely used Linux filesystem. Mature, reliable, supports journaling. Maximum file size: 16 TB. Maximum volume size: 1 EB.
- **XFS** — high-performance, excellent for large files and high throughput. Default on RHEL 7+. Maximum volume size: 8 EB. Cannot be shrunk.
- **Btrfs** — modern filesystem with built-in snapshotting, RAID, and compression. Growing adoption.
- **vfat / exFAT** — for removable media and compatibility with Windows.

**mkfs Command**

```bash
sudo mkfs.ext4 /dev/myvg/appdata
sudo mkfs.xfs /dev/myvg/applogs
sudo mkfs.ext4 -L "data-volume" /dev/myvg/appdata
```

The `-L` flag sets a filesystem label, which can be used in `/etc/fstab` instead of device paths.

**mkfs Options for ext4**

```bash
sudo mkfs.ext4 -b 4096 -m 1 /dev/sdb1
```

- `-b 4096` — block size of 4096 bytes
- `-m 1` — reserve 1% of space for root (default is 5%; reducing saves space on large volumes)

**Filesystem Check — fsck**

Before mounting or resizing an unmounted filesystem:

```bash
sudo fsck /dev/myvg/appdata
sudo fsck -f /dev/myvg/appdata   # Force check even if "clean"
```

Never run `fsck` on a mounted filesystem.

---

### Section 8: Mounting Filesystems

**The mount Command**

Mount a filesystem to a directory (mount point):

```bash
sudo mount /dev/myvg/appdata /opt/appdata
```

Mount with specific options:

```bash
sudo mount -o rw,noexec,nosuid /dev/myvg/appdata /opt/appdata
```

**Common Mount Options**

| Option | Effect |
|--------|--------|
| `rw` | Read-write (default) |
| `ro` | Read-only |
| `noexec` | Prevent execution of binaries |
| `nosuid` | Ignore SUID/SGID bits |
| `nodev` | Prevent device file creation |
| `relatime` | Update access time only when modified (performance) |
| `defaults` | Equivalent to `rw,suid,dev,exec,auto,nouser,async` |

**Viewing Mounted Filesystems**

```bash
mount
mount | grep "/opt"
findmnt
findmnt --target /opt/appdata
```

`findmnt` is cleaner than parsing `mount` output.

**Unmounting**

```bash
sudo umount /opt/appdata
sudo umount /dev/myvg/appdata    # Same result, by device
```

If the filesystem is busy, `umount` will fail:

```bash
# Find what's using it:
sudo lsof +D /opt/appdata
sudo fuser -m /opt/appdata
```

For an emergency unmount (use carefully):

```bash
sudo umount -l /opt/appdata      # Lazy unmount — detaches when no longer busy
```

---

### Section 9: /etc/fstab — Persistent Mounts

Entries in `/etc/fstab` tell the system which filesystems to mount at boot and where.

**Format**

```
<device>  <mount-point>  <filesystem-type>  <options>  <dump>  <pass>
```

Example:

```
/dev/myvg/appdata  /opt/appdata  xfs  defaults  0  2
UUID=abc123...     /data         ext4 defaults,noatime  0  2
LABEL=data-volume  /data         ext4 defaults  0  2
```

**The Six Fields**

1. **Device** — block device, UUID, or label. Using UUID is preferred because it does not change if disks are added or reordered.
2. **Mount Point** — directory where the filesystem will be accessible
3. **Filesystem Type** — ext4, xfs, nfs, swap, etc.
4. **Options** — comma-separated mount options
5. **Dump** — whether `dump` utility backs this up (0=no, 1=yes). Almost always 0.
6. **Pass** — order for `fsck` at boot. 0=skip, 1=root filesystem only, 2=check after root

**Getting the UUID**

```bash
blkid /dev/myvg/appdata
lsblk -f
```

Use the UUID value from `blkid` output in your fstab entry.

**Testing fstab Without Rebooting**

```bash
sudo mount -a
```

This command mounts all entries in `/etc/fstab` that are not already mounted. Run this immediately after editing fstab to catch errors before reboot.

**A Bad fstab Can Prevent Boot**

If you write a bad `/etc/fstab` entry and reboot, the system may drop to emergency mode. Always:

1. Run `sudo mount -a` to test before rebooting
2. Use UUIDs or labels instead of device paths
3. Keep a backup of the working fstab before editing

---

### Section 10: Disk Usage — df and du

**df — Disk Free (Filesystem Level)**

Show disk space for all mounted filesystems:

```bash
df -h
```

- `-h` — human-readable sizes (GB, MB)

Show only a specific filesystem:

```bash
df -h /opt/appdata
```

Include filesystem type:

```bash
df -hT
```

Exclude tmpfs and devtmpfs (cleaner output):

```bash
df -hT --exclude-type=tmpfs --exclude-type=devtmpfs
```

**df Output Columns**

| Column | Meaning |
|--------|---------|
| Filesystem | Device or filesystem name |
| Size | Total capacity |
| Used | Space used by files |
| Avail | Space available (excludes reserved blocks) |
| Use% | Percentage used |
| Mounted on | Mount point |

**du — Disk Usage (Directory Level)**

Show space used by a directory and its contents:

```bash
du -sh /var/log
```

- `-s` — summary (only top-level total, not each subdirectory)
- `-h` — human-readable

Show sizes of all subdirectories in `/var/log`:

```bash
du -h --max-depth=1 /var/log
```

Find the top 10 largest directories under `/`:

```bash
du -h / --max-depth=2 2>/dev/null | sort -rh | head -10
```

This is a powerful troubleshooting command when a filesystem is filling up.

**Finding Large Files**

```bash
find /var -type f -size +100M -exec ls -lh {} \;
```

---

### Section 11: RAID — Redundant Array of Independent Disks

RAID combines multiple physical disks to provide redundancy, performance, or both. Linux implements software RAID through the `mdadm` utility (Multiple Device Administrator).

The Linux+ exam requires you to know RAID levels 0, 1, 5, and 10. Let's go through each.

**RAID 0 — Striping (No Redundancy)**

Data is split across all disks in alternating stripes.

- **Minimum disks**: 2
- **Capacity**: Sum of all disks (2 × 1 TB = 2 TB usable)
- **Redundancy**: None — if any disk fails, ALL data is lost
- **Performance**: Excellent read and write (parallel I/O)
- **Use case**: Temporary scratch space, video editing, cache

**RAID 1 — Mirroring**

Every write is written to all disks simultaneously (mirroring).

- **Minimum disks**: 2
- **Capacity**: Size of ONE disk (2 × 1 TB = 1 TB usable; 50% overhead)
- **Redundancy**: Can lose all but one disk and survive
- **Performance**: Excellent reads (can read from any disk), normal writes
- **Use case**: Boot drives, OS volumes, critical small datasets

**RAID 5 — Striping with Distributed Parity**

Data is striped across all disks, with parity information distributed across all disks (not on a dedicated parity disk).

- **Minimum disks**: 3
- **Capacity**: (N-1) × smallest disk size (3 × 1 TB = 2 TB usable)
- **Redundancy**: Can lose 1 disk; data is rebuilt from parity
- **Performance**: Good reads; writes have parity calculation overhead
- **Use case**: NAS devices, general-purpose server storage

**RAID 6 — Striping with Double Parity**

Like RAID 5 but with two sets of parity.

- **Minimum disks**: 4
- **Capacity**: (N-2) × smallest disk size
- **Redundancy**: Can lose 2 disks simultaneously
- **Use case**: Large arrays where simultaneous dual disk failure is a concern

**RAID 10 (1+0) — Mirrored Stripes**

RAID 10 combines RAID 1 (mirroring) and RAID 0 (striping). Disks are first mirrored in pairs, then the mirrors are striped together.

- **Minimum disks**: 4 (even number)
- **Capacity**: 50% of total (4 × 1 TB = 2 TB usable)
- **Redundancy**: Can lose one disk from each mirrored pair
- **Performance**: Excellent reads and writes
- **Use case**: Databases, high-transaction systems, best of both worlds

**RAID Level Summary Table**

| RAID | Min Disks | Usable Capacity | Can Lose | Performance | Use Case |
|------|-----------|-----------------|----------|-------------|---------|
| 0 | 2 | 100% | 0 disks | Excellent | Scratch/cache |
| 1 | 2 | 50% | N-1 disks | Good | Boot/OS |
| 5 | 3 | (N-1)/N | 1 disk | Good | NAS/storage |
| 6 | 4 | (N-2)/N | 2 disks | Moderate write | Large arrays |
| 10 | 4 | 50% | 1 per pair | Excellent | Databases |

**Creating a Software RAID Array**

```bash
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc
sudo mkfs.ext4 /dev/md0
sudo mdadm --detail /dev/md0
```

View RAID status:

```bash
cat /proc/mdstat
```

---

### Summary — Module 13

Module 13 covered the complete Linux storage stack:

**Part 1:**

- LVM architecture: Physical Volumes → Volume Groups → Logical Volumes
- Creating and managing PVs, VGs, and LVs
- Online volume extension with `lvextend` and `-r`
- LVM snapshots for backup and testing

**Part 2:**

- Filesystem creation: `mkfs.ext4`, `mkfs.xfs`, and filesystem options
- Mounting: `mount`, `umount`, `findmnt`, `fuser`
- `/etc/fstab`: the six fields, UUID-based entries, testing with `mount -a`
- Disk usage: `df` for filesystem-level, `du` for directory-level analysis
- RAID levels 0, 1, 5, 6, and 10: capacity, redundancy, and use cases

Storage management is tested heavily on Linux+. Know the LVM command sequence, the fstab field format, and the RAID level comparison table cold.

Next: Module 14 — SSH and Remote Administration.
