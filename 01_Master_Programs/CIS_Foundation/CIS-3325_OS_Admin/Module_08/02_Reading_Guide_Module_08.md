# Reading Guide: Module 08 - Storage Management: Partitions, LVM, RAID

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


## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 1.0 - System Management

---

### Glossary

**Block Device** - A hardware device (disk, partition, RAID array, logical volume) that stores data in fixed-size blocks and supports random access. Represented in /dev as /dev/sda, /dev/md0, etc.

**Partition Table** - Metadata at the start of a disk that describes the number, type, start, and end positions of partitions. Two formats: MBR (legacy) and GPT (modern).

**MBR (Master Boot Record)** - Legacy partition table format. Maximum 4 primary partitions, maximum disk size 2 TB. Used with BIOS firmware.

**GPT (GUID Partition Table)** - Modern partition table format. Up to 128 partitions, no practical size limit. Required for UEFI systems and disks larger than 2 TB.

**Filesystem** - A data structure that organizes files and directories on a partition. Common types: ext4 (standard Linux), XFS (RHEL default, large files), vfat (compatibility).

**UUID (Universally Unique Identifier)** - A 128-bit identifier assigned to a filesystem when it is formatted. Stable across disk additions and removals. Used in /etc/fstab.

**Physical Volume (PV)** - A disk or partition initialized for LVM use with pvcreate.

**Volume Group (VG)** - A storage pool created from one or more physical volumes. The fundamental LVM allocation unit.

**Logical Volume (LV)** - A virtual partition carved from a volume group. Holds a filesystem and can be resized online.

**RAID (Redundant Array of Independent Disks)** - A technique that combines multiple disks for performance, redundancy, or both.

**Degraded Mode** - A RAID array state where one or more member disks have failed but the array continues operating within its fault tolerance limits.

---

### Partition Table Comparison

| Feature | MBR | GPT |
|---------|-----|-----|
| Maximum partitions | 4 primary (or 3+1 extended) | 128 |
| Maximum disk size | 2 TB | 9.4 ZB (practical: no limit) |
| Firmware compatibility | BIOS | UEFI (also works with BIOS on modern systems) |
| Redundancy | Single copy at sector 0 | Backup copy at end of disk |
| Linux tool | fdisk | gdisk or parted |

---

### Filesystem Comparison

| Feature | ext4 | XFS |
|---------|------|-----|
| Default on | Debian/Ubuntu | RHEL/CentOS |
| Shrinkable | Yes (resize2fs) | No |
| Growable | Yes (resize2fs) | Yes (xfs_growfs) |
| Maximum file size | 16 TB | 8 EB |
| Journaling | Yes | Yes |
| Best for | General purpose | Large files, high throughput |

---

### Key Storage Commands

| Command | Purpose |
|---------|---------|
| lsblk | List all block devices and their partitions |
| lsblk -f | List block devices with filesystem type and UUID |
| blkid | Show UUID, label, and filesystem type of block devices |
| fdisk /dev/sdX | Interactive MBR partition editor |
| gdisk /dev/sdX | Interactive GPT partition editor |
| parted /dev/sdX | GPT and MBR partition editor with scripting support |
| partprobe /dev/sdX | Notify kernel of partition table changes |
| mkfs.ext4 /dev/sdX1 | Format partition with ext4 filesystem |
| mkfs.xfs /dev/sdX1 | Format partition with XFS filesystem |
| mount /dev/sdX1 /mnt | Mount a filesystem at a mount point |
| umount /mnt | Unmount a filesystem |
| mount -a | Mount all entries in /etc/fstab |
| df -h | Show disk usage of mounted filesystems |
| du -sh /path | Show disk usage of a specific directory |
| e2label /dev/sdX1 NAME | Set a label on an ext4 filesystem |

---

### /etc/fstab Field Reference

```
DEVICE          MOUNT_POINT    FSTYPE    OPTIONS     DUMP   PASS
UUID=a1b2c3d4   /mnt/data      ext4      defaults    0      2
```

| Field | Values | Notes |
|-------|--------|-------|
| DEVICE | UUID=, LABEL=, /dev/name | UUID strongly preferred |
| MOUNT_POINT | Directory path | Must exist before mounting |
| FSTYPE | ext4, xfs, vfat, nfs, swap | |
| OPTIONS | defaults, ro, noexec, nosuid, nofail | Comma-separated |
| DUMP | 0 or 1 | Almost always 0 |
| PASS | 0, 1, or 2 | 1=root, 2=others, 0=skip fsck |

---

### LVM Command Reference

| Command | Purpose |
|---------|---------|
| pvcreate /dev/sdX | Initialize a disk or partition as a physical volume |
| pvs | List all physical volumes |
| pvdisplay /dev/sdX | Detailed PV information |
| vgcreate NAME PV... | Create a volume group from one or more PVs |
| vgs | List all volume groups |
| vgdisplay NAME | Detailed VG information |
| vgextend NAME /dev/sdX | Add a new PV to an existing VG |
| lvcreate -L SIZE -n NAME VG | Create a logical volume |
| lvs | List all logical volumes |
| lvdisplay /dev/VG/LV | Detailed LV information |
| lvextend -L +SIZE /dev/VG/LV | Extend an LV by SIZE |
| lvextend -l +100%FREE /dev/VG/LV | Extend an LV using all VG free space |
| resize2fs /dev/VG/LV | Grow an ext4 filesystem to fill the LV |
| xfs_growfs /mount/point | Grow an XFS filesystem to fill the LV |
| lvcreate -L SIZE -s -n SNAP /dev/VG/LV | Create a snapshot of an LV |
| lvremove /dev/VG/LV | Remove a logical volume |

LVM workflow:
1. pvcreate on raw devices
2. vgcreate to pool them
3. lvcreate to carve logical volumes
4. mkfs to create filesystem
5. mount and add to /etc/fstab

---

### RAID Level Reference

| Level | Min Disks | Disk Failures Tolerated | Usable Space | Read Performance | Write Performance |
|-------|-----------|------------------------|-------------|-----------------|------------------|
| RAID 0 | 2 | 0 | 100% | High | High |
| RAID 1 | 2 | 1 | 50% | Good | Moderate |
| RAID 5 | 3 | 1 | (n-1)/n | Good | Moderate |
| RAID 6 | 4 | 2 | (n-2)/n | Good | Lower |
| RAID 10 | 4 | 1 per mirror pair | 50% | High | High |

---

### mdadm Command Reference

| Command | Purpose |
|---------|---------|
| mdadm --create /dev/md0 --level=N --raid-devices=N /dev/sdX... | Create a new RAID array |
| mdadm --detail /dev/md0 | Show detailed array status |
| cat /proc/mdstat | Quick array status (U=active, _=failed) |
| mdadm --manage /dev/md0 --add /dev/sdX | Add a disk to an existing array (rebuild trigger) |
| mdadm --manage /dev/md0 --fail /dev/sdX | Mark a disk as failed (for testing) |
| mdadm --manage /dev/md0 --remove /dev/sdX | Remove a disk from the array |
| mdadm --detail --scan >> /etc/mdadm/mdadm.conf | Save array config for persistence |
| update-initramfs -u | Rebuild initrd to include RAID configuration |

---

### LV Extension Workflow (Most Tested Scenario)

The complete workflow to extend a logical volume and its filesystem:

```bash
# Step 1: Add new disk to VG (if needed)
sudo pvcreate /dev/sdd
sudo vgextend vg_data /dev/sdd

# Step 2: Extend the logical volume
sudo lvextend -L +10G /dev/vg_data/lv_data

# Step 3: Resize the filesystem (ext4)
sudo resize2fs /dev/vg_data/lv_data

# Step 3 (alternative for XFS):
sudo xfs_growfs /data
```

Common mistake: stopping after lvextend. The filesystem is still the old size until resize2fs
or xfs_growfs is run.

---

### Exam Tips

1. MBR supports maximum 4 primary partitions and 2 TB disks. GPT supports 128 partitions and has no practical size limit.

2. After lvextend, always run resize2fs (ext4) or xfs_growfs (XFS) to grow the filesystem into the new space. This is the most tested LVM scenario.

3. XFS cannot be shrunk; it can only grow. ext4 can be both grown and shrunk.

4. RAID 5 needs exactly n-1 disks worth of usable space (one disk of space is used for parity distributed across all disks). Minimum 3 disks.

5. In /proc/mdstat, U = active array member, _ = failed or missing member. [UU_] means one disk in a 3-disk array has failed.

6. UUID in /etc/fstab is mandatory best practice. Device names like /dev/sdb1 can change when disks are added, causing boot failures.

7. mount -a tests all fstab entries. Always run it after editing fstab before rebooting.

8. PASS value of 1 = root filesystem (checked first at boot). PASS 2 = other filesystems. PASS 0 = skip fsck.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Explain the difference between MBR and GPT partition tables
- List the steps to create a partition, format it with ext4, and mount it persistently
- Explain all six fields in an /etc/fstab entry
- Explain why UUID is preferred over device names in /etc/fstab
- Use blkid to find a partition's UUID
- Explain the LVM three-layer hierarchy: PV, VG, LV
- Execute the full LVM creation workflow (pvcreate through mount)
- Extend a logical volume and resize the filesystem (two-step process)
- Compare RAID 0, 1, 5, 6, and 10 by minimum disks and fault tolerance
- Create a RAID 5 array with mdadm
- Interpret /proc/mdstat output and identify a failed disk
- Add a replacement disk to a degraded RAID array

---

## 9. Supplemental Resources

**1. Linux man pages — fdisk(8), lsblk(8), blkid(8), mkfs.ext4(8)**
URL: https://man7.org/linux/man-pages/man8/fdisk.8.html
Coverage: The fdisk man page covers all interactive commands for MBR partition management.
The lsblk man page explains output columns including TYPE, FSTYPE, MOUNTPOINT, and UUID. The
blkid man page describes device attribute scanning. Essential for understanding the disk
inspection commands used in the lab.

**2. LVM2 Administration — Red Hat Enterprise Linux 9**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/index
Coverage: The authoritative LVM administration guide covering pvcreate, vgcreate, lvcreate,
lvextend, lvreduce, pvmove, vgreduce, and snapshot management. Includes worked examples for
the full LVM lifecycle, thin provisioning, and cache volumes. Directly maps to all LVM topics
in this module.

**3. mdadm RAID Administration — Linux RAID Wiki**
URL: https://raid.wiki.kernel.org/index.php/Linux_Raid
Coverage: The kernel.org RAID wiki covers software RAID configuration with mdadm, RAID level
comparison (0, 1, 4, 5, 6, 10), /proc/mdstat interpretation, adding and removing devices,
growing arrays, and recovering from drive failures. Includes a quick-start guide and a
troubleshooting section for degraded array recovery.

**4. fstab(5) and mount(8) Man Pages — man7.org**
URL: https://man7.org/linux/man-pages/man5/fstab.5.html
Coverage: The fstab man page documents every field including the filesystem type, mount
options (defaults, noatime, nofail, ro, noexec, nosuid), dump flag, and fsck pass order.
The mount man page lists all supported options by filesystem type. Required reading for
understanding persistent mount configuration.

**5. Arch Wiki — LVM and RAID**
URL: https://wiki.archlinux.org/title/LVM
Coverage: The Arch Wiki LVM article provides a practical walkthrough of the full LVM stack
with commands and expected output at each step. The companion RAID article at
wiki.archlinux.org/title/RAID covers mdadm configuration, monitoring, and scheduled scrubs.
Both articles are maintained with current kernel and tool versions and include common
troubleshooting scenarios.
