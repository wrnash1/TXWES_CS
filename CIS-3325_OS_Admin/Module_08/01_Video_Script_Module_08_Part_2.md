# Video Script: Module 08 - Storage Management (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 12 minutes
**Part:** 2 of 2 - LVM and RAID

---

### Opening

Welcome back to Part 2 of Module 08. In Part 1 we covered partitions, filesystems, and fstab.
In Part 2 we cover the Logical Volume Manager and software RAID. LVM is one of those features
that seems complex until you see it in use — then it becomes something you want on every server.
RAID is the foundation of disk redundancy.

---

### Section 1: LVM Architecture

LVM adds a flexible abstraction layer between physical disks and filesystems. The three layers are:

Physical Volume (PV): A disk or partition that has been initialized for use by LVM.

Volume Group (VG): A pool of storage created from one or more physical volumes. Think of it
as a single large disk built from multiple physical disks.

Logical Volume (LV): A slice of a volume group that functions like a partition and holds a
filesystem. Logical volumes can be resized, moved, and snapshotted without unmounting.

[SHOW TERMINAL]

---

### Section 2: Creating LVM Storage

[SHOW TERMINAL]

Step 1: Initialize physical volumes.

```bash
sudo pvcreate /dev/sdb /dev/sdc
sudo pvs
```

pvs shows all physical volumes. Each line shows the PV device, the VG it belongs to (empty
if not yet in a VG), and its size.

Step 2: Create a volume group.

```bash
sudo vgcreate vg_data /dev/sdb /dev/sdc
sudo vgs
```

vgs shows volume groups. Note VFree (free space available for new logical volumes).

Step 3: Create a logical volume.

```bash
sudo lvcreate -L 20G -n lv_data vg_data
sudo lvs
```

-L specifies the size. -n specifies the name. lvs shows all logical volumes.

The logical volume is now available as /dev/vg_data/lv_data (or equivalently
/dev/mapper/vg_data-lv_data).

Step 4: Create a filesystem on the logical volume.

```bash
sudo mkfs.ext4 /dev/vg_data/lv_data
sudo mkdir /data
sudo mount /dev/vg_data/lv_data /data
```

---

### Section 3: Extending LVM Storage

[SHOW TERMINAL]

One of LVM's most powerful features is the ability to resize logical volumes online (without
unmounting) for ext4 filesystems.

Scenario: /data is running out of space. Add a new disk and extend the volume.

Step 1: Add the new disk as a physical volume.

```bash
sudo pvcreate /dev/sdd
sudo vgextend vg_data /dev/sdd
sudo vgs
```

VFree shows additional free space is now available.

Step 2: Extend the logical volume.

```bash
sudo lvextend -L +10G /dev/vg_data/lv_data
```

The -L +10G syntax adds 10 GB to the current size. To use all available free space: -l +100%FREE.

Step 3: Resize the filesystem.

```bash
sudo resize2fs /dev/vg_data/lv_data
```

This is the step that is often forgotten. lvextend grows the logical volume block device, but
the filesystem inside still thinks it is the old size. resize2fs makes the filesystem use the
newly available space. For XFS filesystems use xfs_growfs /data instead.

```bash
df -h /data
```

Now shows the increased capacity.

---

### Section 4: LVM Snapshots

[SHOW TERMINAL]

LVM snapshots capture the state of a logical volume at a point in time. They are useful for
consistent backups of running databases without downtime.

```bash
sudo lvcreate -L 5G -s -n lv_data_snap /dev/vg_data/lv_data
```

-s creates a snapshot. The snapshot size (5G here) should be large enough to hold changes
that occur while the snapshot exists. The snapshot device is /dev/vg_data/lv_data_snap.

```bash
sudo mount /dev/vg_data/lv_data_snap /mnt/snap
```

Mount the snapshot for reading and back up from it.

```bash
sudo umount /mnt/snap
sudo lvremove /dev/vg_data/lv_data_snap
```

Remove the snapshot when done. Snapshots fill up as the original volume changes and must be
removed or they will break.

---

### Section 5: Software RAID with mdadm

[SHOW TERMINAL]

Linux software RAID uses the md (multiple devices) driver. The mdadm command manages it.

RAID levels to know:

| Level | Minimum Disks | Fault Tolerance | Usable Capacity | Use Case |
|-------|--------------|----------------|----------------|----------|
| RAID 0 | 2 | None | 100% | Performance only |
| RAID 1 | 2 | 1 disk | 50% | Boot drive, critical data |
| RAID 5 | 3 | 1 disk | (n-1)/n | General-purpose balance |
| RAID 6 | 4 | 2 disks | (n-2)/n | Higher redundancy |
| RAID 10 | 4 | 1 per mirror pair | 50% | High performance + redundancy |

Creating a RAID 5 array:

```bash
sudo mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb /dev/sdc /dev/sdd
```

Monitoring the initial sync (build):

```bash
cat /proc/mdstat
```

The sync percentage and estimated time are shown. The array is functional immediately but
reaches full performance after sync completes.

Save the RAID configuration so it persists across reboots:

```bash
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
sudo update-initramfs -u
```

Creating a filesystem and mounting:

```bash
sudo mkfs.ext4 /dev/md0
sudo mkdir /raid5
sudo mount /dev/md0 /raid5
```

Add to /etc/fstab using the UUID of /dev/md0.

---

### Section 6: RAID Monitoring and Failure Recovery

[SHOW TERMINAL]

```bash
sudo mdadm --detail /dev/md0
```

Shows the array status, individual disk status (active sync, spare, faulty), rebuild progress.

```bash
cat /proc/mdstat
```

Quick status view. U = active disk, _ = failed or missing disk. [UU_] means one of three
disks has failed in a 3-disk array.

When a disk fails:

1. The array continues operating in degraded mode (for RAID 1, 5, 6, 10 within their fault limits).
2. Replace the failed disk physically.
3. Add the new disk to the array:

```bash
sudo mdadm --manage /dev/md0 --add /dev/sdd
```

4. The array automatically begins rebuilding. Monitor with /proc/mdstat.

---

### Section 7: Exam Tips for Module 08

MBR versus GPT: MBR = legacy, 4 partitions max, 2 TB limit. GPT = modern, 128 partitions,
no practical size limit.

LVM order: PV → VG → LV → filesystem. pvcreate, vgcreate, lvcreate, mkfs, mount.

After lvextend on ext4 you must run resize2fs. After lvextend on XFS you must run xfs_growfs.
This two-step process is the most tested LVM scenario.

RAID 5 requires minimum 3 disks, tolerates 1 failure. RAID 6 requires minimum 4 disks,
tolerates 2 failures. RAID 10 requires minimum 4 disks, tolerates 1 disk per mirror pair.

[UU_] in /proc/mdstat means one disk has failed. Add replacement with mdadm --manage --add.

UUID in /etc/fstab: device names can change, UUIDs do not. Always use UUID in fstab.

---

### Summary

Module 08 covers the complete Linux storage stack: partitions (fdisk/gdisk), filesystems
(mkfs.ext4, mkfs.xfs), persistent mounts (/etc/fstab with UUIDs), LVM (pvcreate/vgcreate/
lvcreate/lvextend/resize2fs), and software RAID (mdadm, RAID levels 0/1/5/6/10).

Module 09 covers networking configuration: interfaces, IP addressing, routing, and DNS.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
