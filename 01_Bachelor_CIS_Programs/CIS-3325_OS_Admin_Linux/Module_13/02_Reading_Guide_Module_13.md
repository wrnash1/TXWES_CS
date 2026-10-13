# Reading Guide: Module 13 — Storage and Logical Volume Management

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
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


## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This guide accompanies the Module 13 video lectures on LVM, filesystems, and RAID. Estimated reading and review time: 90 minutes.

---

### Learning Objectives

After completing this module, you will be able to:

- Explain the three-layer LVM architecture and the role of each component
- Create, extend, and remove physical volumes, volume groups, and logical volumes
- Create LVM snapshots for backup and rollback scenarios
- Create ext4 and XFS filesystems using `mkfs`
- Mount filesystems manually and configure persistent mounts in `/etc/fstab`
- Analyze disk usage with `df` and `du`
- Compare RAID levels 0, 1, 5, 6, and 10 by capacity, redundancy, and performance

---

### Key Terms

**Physical Volume (PV)**
A disk or partition initialized for LVM use with `pvcreate`. PVs are divided into physical extents (PEs).

**Volume Group (VG)**
A pool of storage composed of one or more physical volumes. The VG is the allocation unit from which logical volumes are carved.

**Logical Volume (LV)**
A virtual block device created from space in a volume group. An LV behaves like a partition and holds a filesystem.

**Physical Extent (PE)**
The smallest unit of allocation in LVM (default 4 MB). A logical volume's size is always a multiple of the PE size.

**Filesystem**
A data structure written onto a block device that organizes how files are stored. Common Linux filesystems: ext4, XFS, Btrfs.

**Mount Point**
A directory in the filesystem tree where another filesystem is attached and made accessible.

**UUID**
Universally Unique Identifier — a 128-bit identifier assigned to a filesystem by `mkfs`. Preferred over device paths in `/etc/fstab` because it does not change when disk order changes.

**RAID**
Redundant Array of Independent Disks — combines multiple physical disks into a logical storage unit with enhanced performance, redundancy, or both.

**Parity**
Mathematical redundancy data in RAID 5/6. If one disk fails, parity data on remaining disks allows reconstruction of the lost data.

---

### Section 1: LVM Architecture Reference

**Command Overview**

| Layer | Create | View (short) | View (detailed) | Remove |
|-------|--------|-------------|-----------------|--------|
| PV | `pvcreate` | `pvs` | `pvdisplay` | `pvremove` |
| VG | `vgcreate` | `vgs` | `vgdisplay` | `vgremove` |
| LV | `lvcreate` | `lvs` | `lvdisplay` | `lvremove` |

**Physical Extent Calculation**

If a VG has a PE size of 4 MB and you allocate a 10 GB logical volume:

```
10 GB ÷ 4 MB = 2560 physical extents
```

To create a volume of exactly 2560 PEs:

```bash
sudo lvcreate -l 2560 -n mydata myvg
```

**LVM Thin Provisioning**

Standard LVM allocates extents immediately (thick provisioning). Thin provisioning allows logical volumes to be larger than the physical space available, with actual storage allocated on write. This is useful for virtualization environments.

Creating a thin pool:

```bash
sudo lvcreate -L 100G --thinpool thinpool myvg
sudo lvcreate -V 200G --thin -n thinlv myvg/thinpool
```

The LV appears as 200 GB to the guest but only uses space as data is written.

---

### Section 2: Filesystem Selection Guide

**ext4 vs. XFS Decision Criteria**

| Factor | ext4 | XFS |
|--------|------|-----|
| Default on RHEL 7+ | No | Yes |
| Default on Ubuntu | Yes | No |
| Can shrink | Yes | No |
| Large file performance | Good | Excellent |
| Small file performance | Excellent | Good |
| fsck time on large volumes | Slow | Fast |
| Snapshot support | Via LVM | Via LVM |
| Max volume size | 1 EB | 8 EB |

**When to Choose ext4**

- Boot partitions (wide tool support)
- Volumes you might need to shrink later
- General-purpose use on Ubuntu/Debian

**When to Choose XFS**

- High-throughput workloads: databases, media storage, log aggregation
- Large volumes (>2 TB)
- RHEL/CentOS/Rocky Linux environments where XFS is the default

**Btrfs Overview**

Btrfs provides built-in snapshotting, RAID, online defragmentation, and transparent compression. While not yet the default on major enterprise distributions, it is default on SUSE and gaining adoption. Key concepts:

- Subvolumes — independent filesystem namespaces within a Btrfs volume
- Send/receive — efficient data transfer between Btrfs volumes
- Compression: `compress=zstd` mount option

---

### Section 3: /etc/fstab Deep Dive

**UUID vs. Device Path vs. Label**

Why UUIDs are strongly preferred:

- Device paths (`/dev/sdb1`) can change if you add or remove disks
- Labels are human-set and can conflict if you clone a disk
- UUIDs are assigned by the filesystem at `mkfs` time and are globally unique

**fstab for Network Filesystems**

NFS mount in fstab:

```
server:/export/data  /mnt/nfs  nfs  defaults,_netdev  0  0
```

The `_netdev` option tells systemd to wait for network availability before mounting. Without it, a server boot without network access can hang.

**fstab for Swap**

```
/dev/myvg/swap  none  swap  sw  0  0
UUID=abc123...  none  swap  sw  0  0
```

**The systemd-fstab-generator**

On systemd systems, `/etc/fstab` entries are automatically converted to `.mount` and `.automount` units by `systemd-fstab-generator` at boot. This means each fstab entry has a corresponding systemd unit:

```bash
systemctl list-units --type=mount
systemctl status opt-appdata.mount
```

The unit name is derived from the mount path with `/` replaced by `-`.

---

### Section 4: Monitoring and Alerting on Disk Usage

**Checking Inode Usage**

Filesystems have a finite number of inodes (file metadata structures). Even with free space, you can run out of inodes:

```bash
df -i
```

This is a common issue on mail servers or systems with many small files.

**Disk Quota**

For multi-user systems, disk quotas limit per-user or per-group storage:

```bash
sudo quotacheck -cum /home    # Initialize quota database
sudo quotaon /home
sudo edquota -u username      # Set per-user limits
sudo repquota /home           # Report on quota usage
```

Enable quotas in fstab by adding `usrquota` or `grpquota` to mount options.

**Monitoring Scripts**

A common monitoring cron job that alerts when disk usage exceeds 80%:

```bash
#!/bin/bash
df -h | awk 'NR>1 {gsub(/%/,"",$5); if($5>80) print "ALERT: "$6" is "$5"% full"}'
```

---

### Section 5: RAID Deep Dive

**Hardware vs. Software RAID**

- **Hardware RAID**: Implemented on a dedicated RAID controller card with its own CPU and cache. Transparent to the OS — the OS sees only the logical volume. Faster for write-heavy workloads due to battery-backed write cache.
- **Software RAID (mdadm)**: Implemented in the Linux kernel's MD (Multiple Device) layer. Uses CPU resources. No dedicated cache. More transparent, portable, and free.

**mdadm Command Reference**

Create RAID 1:

```bash
sudo mdadm --create /dev/md0 \
  --level=1 \
  --raid-devices=2 \
  /dev/sdb /dev/sdc
```

Create RAID 5:

```bash
sudo mdadm --create /dev/md0 \
  --level=5 \
  --raid-devices=3 \
  /dev/sdb /dev/sdc /dev/sdd
```

Check array status:

```bash
cat /proc/mdstat
sudo mdadm --detail /dev/md0
```

Save RAID configuration (required for boot):

```bash
sudo mdadm --detail --scan >> /etc/mdadm/mdadm.conf
sudo update-initramfs -u    # Debian/Ubuntu
```

**RAID Rebuild Process**

When a disk fails in a RAID 1 or RAID 5 array:

1. The array degrades but continues operating
2. Replace the failed disk
3. Add the new disk to the array:

```bash
sudo mdadm /dev/md0 --add /dev/sdd
```

4. The array automatically rebuilds (visible in `/proc/mdstat`)
5. Rebuild time for large arrays can take hours

**RAID Write Hole**

RAID 5 has a known vulnerability called the "write hole": if a system crashes during a write, the data and parity can become inconsistent. Solutions include:

- Write-intent bitmap: tracks which stripes need resync after a crash
- RAID 6: double parity provides additional protection
- Journal device (mdadm 4.1+)

---

### Section 6: Partition Types Reference

**Partition Table Types**

- **MBR (Master Boot Record)**: Legacy format. Maximum disk size: 2 TB. Maximum 4 primary partitions.
- **GPT (GUID Partition Table)**: Modern format. Supports disks >2 TB. Up to 128 partitions. Required for UEFI boot.

**Partitioning Tools**

| Tool | Interface | Supports GPT | Notes |
|------|-----------|-------------|-------|
| `fdisk` | Interactive CLI | Partial | Use for MBR; newer versions support GPT |
| `gdisk` | Interactive CLI | Yes | GPT equivalent of fdisk |
| `parted` | CLI/interactive | Yes | Supports both MBR and GPT |
| `cfdisk` | Curses UI | Yes | Menu-driven, beginner-friendly |

**LVM Partition Type**

When creating partitions for LVM, set the partition type to "Linux LVM" (type code `8e` in `fdisk`, `8300` in `gdisk`). This is not strictly required but is a best practice.

---

### Practice Review Questions

Answer these before taking the quiz:

1. What is the command to initialize `/dev/sdc` as a physical volume?

2. A volume group `datavg` is full. You add a new 500 GB disk `/dev/sdd`. What two commands do you run?

3. You need to extend the logical volume `/dev/datavg/logs` by 10 GB AND resize the filesystem in a single command. What is the command?

4. What is the difference between `df` and `du`?

5. Write a complete fstab entry for mounting `/dev/appvg/data` (ext4, UUID=`abc123`) at `/opt/data` with `noexec` and `nosuid` options.

6. What does the sixth field (pass) in an fstab entry control?

7. You have 4 disks of 2 TB each. Compare the usable capacity of RAID 5, RAID 6, and RAID 10.

8. Why can XFS not be shrunk?

---

### Additional Resources

- `man lvm` — LVM overview
- `man 8 mdadm` — software RAID management
- `man 5 fstab` — filesystem table format
- `man mkfs.ext4` and `man mkfs.xfs` — filesystem creation options
- Red Hat Storage Administration Guide: access.redhat.com/documentation
- CompTIA Linux+ XK0-005 Objective 1.3 (Storage) and 1.6 (Filesystems)

---

### Key Takeaways

- LVM provides a flexible abstraction layer: Physical Volumes → Volume Groups → Logical Volumes.
- Use `lvextend -r` to extend an LV and resize the filesystem in one command.
- `/etc/fstab` must be tested with `mount -a` after every edit before rebooting.
- Always use UUIDs in `/etc/fstab` entries — device paths change; UUIDs do not.
- RAID 0 = performance only. RAID 1 = full redundancy. RAID 5 = space-efficient parity. RAID 10 = performance + redundancy.
- XFS is the RHEL default; ext4 is the Debian/Ubuntu default. Know both.

---

## 9. Supplemental Resources

**1. [Red Hat — A Practical Guide to LVM](https://www.redhat.com/sysadmin/lvm-vs-partitioning)**
A Red Hat sysadmin article comparing LVM to traditional partitioning with practical guidance on when to use each. Covers the complete LVM creation workflow from `pvcreate` through `lvcreate`, online resize operations for both ext4 and XFS, and real-world use cases for snapshots and `pvmove`. The most direct online resource for the LVM portions of the Module 13 lab.

**2. [Linux RAID Wiki — The Linux MDADM Documentation](https://raid.wiki.kernel.org/index.php/Linux_Raid)**
The official Linux software RAID documentation. Covers all RAID levels supported by `mdadm`, the creation and management lifecycle of arrays, rebuild monitoring via `/proc/mdstat`, spare disk configuration, and the `/etc/mdadm/mdadm.conf` configuration file. Essential reading for understanding how `mdadm` arrays survive reboots and what happens during degraded operation.

**3. [Arch Linux Wiki — LVM](https://wiki.archlinux.org/title/LVM)**
A comprehensive, distribution-agnostic LVM reference maintained by the Arch Linux community. Covers advanced topics including thinly provisioned volumes, LVM on top of RAID, LVM cache (SSD caching of HDD volumes), and the `lvs`/`pvs`/`vgs` display attribute columns. The "Snapshots" section is particularly useful for understanding LVM snapshot mechanics and the copy-on-write behavior that makes snapshots efficient.
