# Quiz: Module 08 - Storage Management: Partitions, LVM, RAID

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

An administrator has just created a new logical volume /dev/vg_data/lv_data and wants to extend
it by 10 gigabytes. After running lvextend -L +10G /dev/vg_data/lv_data, the df -h output shows
the filesystem size has not changed. What additional step is required for an ext4 filesystem?

- A) Run vgextend vg_data /dev/sdc to add space to the volume group.
- B) Run resize2fs /dev/vg_data/lv_data to resize the filesystem to match the new logical volume size.
- C) Unmount the filesystem and recreate it with mkfs.ext4.
- D) Run partprobe to notify the kernel of the size change.

Correct Answer: B) Run resize2fs /dev/vg_data/lv_data to resize the filesystem to match the new logical volume size.

Distractor Analysis:

- Why A is incorrect: vgextend adds a new physical volume to an existing volume group to increase the VG's total capacity. In this scenario the LV has already been extended; the remaining issue is that the filesystem inside still thinks it is the old size.
- Why C is incorrect: Recreating the filesystem with mkfs.ext4 would destroy all data on the volume. resize2fs can grow an ext4 filesystem non-destructively.
- Why D is incorrect: partprobe informs the kernel about partition table changes on a disk device. It has no effect on LVM logical volumes, which are not partitions.

---

**Question 2**

A storage administrator needs to configure software RAID across three disks (/dev/sdb, /dev/sdc,
/dev/sdd) to maximize available capacity while tolerating a single disk failure. Which RAID level
is most appropriate?

- A) RAID 0
- B) RAID 1
- C) RAID 5
- D) RAID 10

Correct Answer: C) RAID 5

Distractor Analysis:

- Why A is incorrect: RAID 0 (striping) distributes data across all disks for maximum performance and capacity, but provides zero fault tolerance. A single disk failure destroys all data.
- Why B is incorrect: RAID 1 (mirroring) requires an even number of disks and uses half the total capacity for redundancy. With three disks, RAID 1 is inefficient and wastes one disk's worth of capacity compared to RAID 5.
- Why D is incorrect: RAID 10 requires a minimum of four disks (two mirrored pairs). It cannot be created with only three disks.

---

**Question 3**

An administrator needs to restrict a configuration file so only the file owner can read and write
it, with no access for group or others. Which command achieves this?

- A) chmod 600 config.conf
- B) chmod 640 config.conf
- C) chmod 644 config.conf
- D) chmod 660 config.conf

Correct Answer: A) chmod 600 config.conf

Distractor Analysis:

- Why B is incorrect: chmod 640 gives the owner rw- (read+write) but gives the group r-- (read-only). The requirement specifies no group access.
- Why C is incorrect: chmod 644 gives owner rw- and both group and others r-- (read-only). This does not meet the requirement of no access for group or others.
- Why D is incorrect: chmod 660 gives both owner and group rw- (read+write), with no access for others. This still grants group access, violating the requirement.

---

**Question 4**

An administrator needs to make a filesystem mount persist across reboots. They add an entry to
/etc/fstab. Which device identifier is most reliable to use in the fstab entry for a partition
on an additional data disk?

- A) /dev/sdb1
- B) The device's UUID (e.g., UUID=a1b2c3d4-...)
- C) The disk's model name from lshw
- D) The partition label if one was set during mkfs

Correct Answer: B) The device's UUID (e.g., UUID=a1b2c3d4-...)

Distractor Analysis:

- Why A is incorrect: Device names like /dev/sdb1 are assigned by the kernel at boot based on detection order. Adding a new disk or changing a disk's physical port can change these names, causing boot failures if fstab uses them.
- Why C is incorrect: Model names from hardware inventory tools are not valid fstab device identifiers. The kernel does not use model names to locate block devices during the mount process.
- Why D is incorrect: Partition labels can also be used in fstab with the LABEL= syntax and are more stable than device names. However, UUID is the most universally reliable identifier because it is guaranteed to be globally unique and does not require the administrator to manually set a label.

---

**Question 5**

A systems administrator runs cat /proc/mdstat and sees the array listed as [UU_], indicating one
drive has failed in a RAID 5 array. What does the underscore represent, and what is the correct
next step?

- A) The underscore means the array is performing a rebuild. Wait for it to complete automatically.
- B) The underscore represents a failed or missing disk. Replace the failed drive and add it back to the array with mdadm --manage /dev/md0 --add /dev/sdd.
- C) The underscore means the array is in read-only mode. Run mdadm --readwrite /dev/md0 to restore write access.
- D) The underscore indicates the array needs defragmentation. Run e2fsck -f /dev/md0 to repair it.

Correct Answer: B) The underscore represents a failed or missing disk. Replace the failed drive and add it back to the array with mdadm --manage /dev/md0 --add /dev/sdd.

Distractor Analysis:

- Why A is incorrect: During a rebuild, mdstat shows _ for the missing disk and a rebuild progress percentage. The _ itself represents a failed/missing device; a rebuild only begins after a replacement drive is added with --add.
- Why C is incorrect: There is no --readwrite option for mdadm. Read-only state is a separate condition shown differently in mdstat. A _ specifically indicates a missing or failed array member.
- Why D is incorrect: e2fsck checks ext4 filesystem integrity on a device. It is not a RAID-level tool and does not repair missing RAID members. Running e2fsck on a degraded array without replacing the failed disk would not restore redundancy.

---

**Question 6**

An administrator wants to create a new logical volume using all remaining free space in the volume
group vg_prod. Which lvextend flag correctly uses all available free space rather than specifying
a fixed size?

- A) lvextend -L 100% /dev/vg_prod/lv_data
- B) lvextend -l +100%FREE /dev/vg_prod/lv_data
- C) lvextend --all /dev/vg_prod/lv_data
- D) lvextend -L +0 /dev/vg_prod/lv_data

Correct Answer: B) lvextend -l +100%FREE /dev/vg_prod/lv_data

Distractor Analysis:

- Why A is incorrect: -L 100% is not valid lvextend syntax. The -L flag expects an absolute size like -L 20G or a relative size with +, not a percentage without the +FREE suffix.
- Why C is incorrect: --all is not a valid lvextend flag. There is no single flag that automatically uses all VG free space; the correct syntax is -l +100%FREE.
- Why D is incorrect: -L +0 would attempt to extend by zero bytes, which is effectively a no-op (or an error depending on the LVM version). It does not allocate any free space.

---

**Question 7**

A system administrator creates an XFS filesystem on a logical volume that fills the volume. Later,
the volume group has additional space added. The administrator extends the logical volume with
lvextend. Which command must be run next to make the additional space usable on an XFS filesystem?

- A) resize2fs /dev/vg_data/lv_data
- B) xfs_repair /dev/vg_data/lv_data
- C) xfs_growfs /data
- D) mkfs.xfs -f /dev/vg_data/lv_data

Correct Answer: C) xfs_growfs /data

Distractor Analysis:

- Why A is incorrect: resize2fs is the filesystem resize tool for ext2, ext3, and ext4 filesystems. It does not understand XFS and will not work on an XFS filesystem.
- Why B is incorrect: xfs_repair is used to fix a corrupt XFS filesystem. It is not used for resizing. Running xfs_repair on a healthy filesystem is not recommended.
- Why D is incorrect: mkfs.xfs -f would reformat the partition, destroying all existing data on the filesystem. The goal is to grow the existing filesystem, not recreate it.

---

**Question 8**

An administrator needs to create a new LVM logical volume. The system already has an LVM volume
group named vg_storage. What is the correct sequence of commands to create a 15 GB logical volume
named lv_archive, format it with ext4, and mount it at /archive?

- A) mkfs.ext4 /dev/sdc → lvcreate -L 15G -n lv_archive vg_storage → mount /dev/sdc /archive
- B) lvcreate -L 15G -n lv_archive vg_storage → mkfs.ext4 /dev/vg_storage/lv_archive → mount /dev/vg_storage/lv_archive /archive
- C) vgcreate vg_storage /dev/sdc → lvcreate -L 15G lv_archive → mkfs.ext4 /dev/lv_archive
- D) pvcreate /dev/sdc → lvcreate -L 15G -n lv_archive → mount -t ext4 /dev/sdc /archive

Correct Answer: B) lvcreate -L 15G -n lv_archive vg_storage → mkfs.ext4 /dev/vg_storage/lv_archive → mount /dev/vg_storage/lv_archive /archive

Distractor Analysis:

- Why A is incorrect: This sequence runs mkfs.ext4 on a raw disk device rather than on the logical volume, bypasses LVM entirely, and mounts the wrong device. LVM devices are accessed through /dev/VG_NAME/LV_NAME.
- Why C is incorrect: vgcreate creates a new volume group but the question states the VG already exists. The lvcreate command is also missing the -n flag and volume group name. This sequence is incomplete and incorrect.
- Why D is incorrect: pvcreate initializes a raw disk as a physical volume and would be needed before vgcreate, not as part of the LV creation process when the VG already exists. The lvcreate command is also missing the VG name.

---

**Question 9**

What is the primary difference between a Physical Volume, a Volume Group, and a Logical Volume in LVM?

- A) A Physical Volume holds the data, a Volume Group is the filesystem, and a Logical Volume is the mount point.
- B) A Physical Volume is an initialized disk or partition, a Volume Group is a storage pool made from one or more PVs, and a Logical Volume is a flexible virtual partition carved from the VG.
- C) A Physical Volume is the RAID array, a Volume Group manages partitions, and a Logical Volume is equivalent to a disk sector.
- D) A Physical Volume is a filesystem, a Volume Group groups filesystems together, and a Logical Volume is a backup copy of the VG.

Correct Answer: B) A Physical Volume is an initialized disk or partition, a Volume Group is a storage pool made from one or more PVs, and a Logical Volume is a flexible virtual partition carved from the VG.

Distractor Analysis:

- Why A is incorrect: This description confuses the role of each LVM layer. The filesystem is created on the logical volume after lvcreate, not as part of the volume group. Mount points are assigned when mounting, not at the VG level.
- Why C is incorrect: LVM and RAID are separate technologies. A physical volume is not a RAID array. RAID can be combined with LVM (RAID providing the PV), but the two are not equivalent terms.
- Why D is incorrect: None of the three LVM layers are filesystems by themselves. A filesystem is created on a logical volume using mkfs. Volume groups do not group filesystems; they pool raw storage from physical volumes.

---

**Question 10**

An administrator runs fdisk -l /dev/sda on a new server and sees "Disklabel type: dos." The disk
is 6 TB. Which statement best describes the implication and the corrective action?

- A) dos means the disk uses FAT32. Run mkfs.fat on the disk to initialize it correctly for Linux.
- B) dos (MBR) partition table cannot address the full 6 TB disk since MBR supports a maximum of 2 TB. The disk should be converted to GPT using gdisk or parted before creating partitions.
- C) dos is the correct partition table type for Linux systems. No action is needed.
- D) The disk is reporting an error. Run fsck /dev/sda to repair the partition table.

Correct Answer: B) dos (MBR) partition table cannot address the full 6 TB disk since MBR supports a maximum of 2 TB. The disk should be converted to GPT using gdisk or parted before creating partitions.

Distractor Analysis:

- Why A is incorrect: dos in the fdisk output refers to the MBR (Master Boot Record) partition table format used by MS-DOS and early PCs, not a FAT32 filesystem. The filesystem type and the partition table type are different concepts.
- Why C is incorrect: While MBR partition tables do work on Linux, they are not correct for disks larger than 2 TB. Partitions on the portion of the disk beyond 2 TB would be inaccessible with an MBR partition table.
- Why D is incorrect: The output is not an error — it is a description of the partition table type. fsck is a filesystem check tool, not a partition table repair tool, and running fsck on a raw disk device with no filesystem would not accomplish anything useful.

---

**Question 11**

An administrator runs `lsblk` and sees that `/dev/sdb` has no partitions listed beneath it. They
want to initialize it as a single Physical Volume for LVM. Which sequence of commands is correct?

- A) mkfs.ext4 /dev/sdb → pvcreate /dev/sdb → vgcreate vg01 /dev/sdb
- B) fdisk /dev/sdb (create partition sdb1) → pvcreate /dev/sdb1 → vgcreate vg01 /dev/sdb1
- C) pvcreate /dev/sdb → vgcreate vg01 /dev/sdb (using the whole disk directly, no partition needed)
- D) gdisk /dev/sdb → mkfs.xfs /dev/sdb1 → pvcreate /dev/sdb1

Correct Answer: C) pvcreate /dev/sdb → vgcreate vg01 /dev/sdb (using the whole disk directly, no partition needed)

Distractor Analysis:

- Why A is incorrect: Running mkfs.ext4 on the raw disk before pvcreate writes an ext4 superblock to the device, which is unnecessary and misleading. LVM does not require a filesystem to be created first; pvcreate writes its own metadata (the PV label) directly to the device.
- Why B is incorrect: While partitioning before LVM is a common practice, it is not required when using a whole disk. pvcreate can be run directly on /dev/sdb without creating a partition first. The sequence described is valid but not the only correct approach — option C is also correct and simpler.
- Why D is incorrect: Creating a GPT partition with gdisk and then running mkfs.xfs would create a standalone filesystem, not an LVM physical volume. pvcreate must be used to initialize a device for LVM use.

---

**Question 12**

A volume group named `vg_data` has 20 GB of free space. An administrator runs:

```
lvcreate -L 15G -n lv_logs vg_data
mkfs.xfs /dev/vg_data/lv_logs
```

They then add the following line to `/etc/fstab`:

```
/dev/vg_data/lv_logs  /var/log/app  xfs  defaults  0  2
```

After rebooting, the mount fails with "special device does not exist." What is the most likely cause?

- A) XFS filesystems cannot be mounted via /etc/fstab entries that use logical volume paths.
- B) The logical volume name lv_logs contains an underscore, which is not allowed in LVM names.
- C) The /var/log/app mount point directory does not exist and was not created before the reboot.
- D) The lvcreate command requires the -n flag to come before the -L flag.

Correct Answer: C) The /var/log/app mount point directory does not exist and was not created before the reboot.

Distractor Analysis:

- Why A is incorrect: XFS filesystems can be mounted via /etc/fstab using logical volume device paths. The path /dev/vg_data/lv_logs is a valid device node created by the device mapper subsystem.
- Why B is incorrect: LVM names may contain underscores. The naming rules for LVM objects (VGs, LVs, PVs) permit alphanumeric characters, hyphens, underscores, and dots.
- Why D is incorrect: The -n and -L flags in lvcreate are not order-dependent. Both orders are syntactically valid. The problem is not with the lvcreate command.

---

**Question 13**

An administrator needs to reduce the size of an XFS logical volume from 50 GB to 30 GB because
space is needed elsewhere in the volume group. They run `lvreduce -L 30G /dev/vg01/lv_data`.
What is the result?

- A) The logical volume is safely shrunk to 30 GB and the filesystem adjusts automatically.
- B) The lvreduce command refuses to proceed because the XFS filesystem must be shrunk first.
- C) The logical volume metadata is resized to 30 GB but the XFS filesystem is now larger than the device, causing filesystem corruption.
- D) The command fails with "permission denied" because only root can reduce logical volumes.

Correct Answer: C) The logical volume metadata is resized to 30 GB but the XFS filesystem is now larger than the device, causing filesystem corruption.

Distractor Analysis:

- Why A is incorrect: XFS does not support shrinking. There is no xfs_shrink tool. Running lvreduce on a logical volume containing an XFS filesystem without first backing up and recreating the filesystem will cause data corruption.
- Why B is incorrect: lvreduce does not automatically check filesystem size before reducing. It will proceed with the reduction even if the filesystem is larger than the target size, resulting in the corruption described in option C. The administrator is responsible for verifying that the filesystem is smaller than the new LV size before running lvreduce.
- Why D is incorrect: The command would be run as root and would not produce a permission denied error for a root user. The fundamental problem is the incompatibility between XFS and volume shrink operations.

---

**Question 14**

A RAID 5 array is built from four 2 TB drives. How much usable storage capacity does this
array provide, and what is the minimum number of drive failures it can tolerate?

- A) 8 TB usable; tolerates 2 simultaneous drive failures.
- B) 6 TB usable; tolerates 1 drive failure.
- C) 4 TB usable; tolerates 2 drive failures.
- D) 2 TB usable; tolerates 3 drive failures.

Correct Answer: B) 6 TB usable; tolerates 1 drive failure.

Distractor Analysis:

- Why A is incorrect: RAID 5 uses distributed parity that consumes the equivalent of one drive's capacity for parity data. With four 2 TB drives the usable space is (4-1) × 2 TB = 6 TB, not 8 TB. RAID 5 also tolerates only one simultaneous drive failure, not two.
- Why C is incorrect: 4 TB usable would correspond to a RAID 6 array (two parity drives) built from four 2 TB drives: (4-2) × 2 TB = 4 TB. RAID 6 also tolerates two simultaneous failures, not RAID 5.
- Why D is incorrect: 2 TB usable with three-failure tolerance would describe a configuration with an extreme redundancy overhead that does not match any standard RAID level for four drives.

---

**Question 15**

An administrator examines `/etc/fstab` and finds this entry:

```
UUID=a1b2c3d4  /data  ext4  defaults,noatime,nofail  0  2
```

What is the purpose of the `nofail` mount option?

- A) It prevents the filesystem from being checked with fsck during boot.
- B) It allows the system to complete the boot process even if the device with the specified UUID is not found.
- C) It disables journaling on the ext4 filesystem to improve write performance.
- D) It prevents the mount from appearing in the output of the `mount` command.

Correct Answer: B) It allows the system to complete the boot process even if the device with the specified UUID is not found.

Distractor Analysis:

- Why A is incorrect: The fsck pass order is controlled by the last numeric field in /etc/fstab (0 = skip, 1 = check first, 2 = check after root). The nofail option does not affect fsck execution.
- Why C is incorrect: Disabling the ext4 journal would require the noload or data=writeback mount options, not nofail. The nofail option has no effect on filesystem journaling behavior.
- Why D is incorrect: The mount command shows all currently mounted filesystems regardless of the /etc/fstab options used. nofail affects boot behavior only, not the visibility of a successfully mounted filesystem.

---

**Question 16**

A system administrator runs `pvs` and sees the following output:

```
  PV         VG      Fmt  Attr PSize  PFree
  /dev/sdb1  vg_web  lvm2 a--  20.00g  0
  /dev/sdc1  vg_web  lvm2 a--  20.00g  5.00g
```

They want to remove `/dev/sdb1` from the volume group without losing data. Which command
must be run before `vgreduce vg_web /dev/sdb1`?

- A) pvremove /dev/sdb1
- B) lvremove /dev/vg_web/lv_data
- C) pvmove /dev/sdb1
- D) vgscan /dev/sdb1

Correct Answer: C) pvmove /dev/sdb1

Distractor Analysis:

- Why A is incorrect: pvremove removes the LVM metadata from a physical volume, making it no longer part of any volume group. Running pvremove before moving data off /dev/sdb1 would corrupt or destroy the data stored on that PV.
- Why B is incorrect: Removing the logical volume would destroy the data. The goal is to move the data off /dev/sdb1 and keep it intact on the remaining PV, not delete it.
- Why D is incorrect: vgscan scans for volume groups and updates the LVM cache. It does not move data between physical volumes. The data on /dev/sdb1 must be migrated to /dev/sdc1 before the PV can be removed from the volume group.

---

**Question 17**

An administrator needs to create a snapshot of a logical volume `/dev/vg01/lv_prod` before
applying a software update. Which command creates a 5 GB snapshot named `lv_snap`?

- A) lvcreate -s -n lv_snap -L 5G /dev/vg01/lv_prod
- B) lvcreate -n lv_snap -L 5G /dev/vg01/vg01
- C) lvsnap -n lv_snap -L 5G /dev/vg01/lv_prod
- D) cp -a /dev/vg01/lv_prod /dev/vg01/lv_snap

Correct Answer: A) lvcreate -s -n lv_snap -L 5G /dev/vg01/lv_prod

Distractor Analysis:

- Why B is incorrect: The -s flag (snapshot) is missing. Without -s, lvcreate creates a regular new logical volume, not a snapshot of an existing one. The device path at the end must be the source LV, not the VG.
- Why C is incorrect: There is no lvsnap command in LVM. Snapshots are created with lvcreate -s. This answer tests whether students know the actual LVM command set.
- Why D is incorrect: cp copies file data; it cannot be used to create an LVM snapshot. An LVM snapshot is a block-level copy-on-write structure managed by the kernel device mapper, not a file copy.

---

**Question 18**

A system has a software RAID 1 array `/dev/md0` managed by mdadm. One drive fails and is
replaced. An administrator runs `mdadm --add /dev/md0 /dev/sdc1` to add the new drive. What
process begins immediately after this command?

- A) The RAID array is rebuilt — the data from the surviving drive is copied to the new drive in the background.
- B) The new drive becomes a hot spare but is not added to the array until the next reboot.
- C) The array switches to degraded mode and the administrator must run mdadm --assemble to begin the rebuild.
- D) mdadm formats /dev/sdc1 with ext4 before adding it to the array.

Correct Answer: A) The RAID array is rebuilt — the data from the surviving drive is copied to the new drive in the background.

Distractor Analysis:

- Why B is incorrect: mdadm --add immediately begins the resync/rebuild process for a degraded RAID 1 array. Hot spare behavior is a configuration option; without that configuration the drive is added as a full member and rebuild starts immediately.
- Why C is incorrect: The array is already in degraded mode due to the failed drive. Running mdadm --add triggers the rebuild automatically — no separate assemble command is needed.
- Why D is incorrect: mdadm does not format drives with a filesystem. RAID members are raw block devices used by the RAID layer; the filesystem (if any) sits on top of /dev/md0, not on the individual RAID member devices.

---

**Question 19**

An administrator adds a second disk `/dev/sdb` to a VM and wants to mount it persistently at
`/mnt/data`. They create a partition `/dev/sdb1`, format it with ext4, and add the following
line to `/etc/fstab`:

```
/dev/sdb1  /mnt/data  ext4  defaults  0  2
```

A colleague says this entry should use the UUID instead of the device path. Why?

- A) UUID-based entries are required by systemd; device path entries are silently ignored.
- B) Device paths like /dev/sdb1 can change between reboots if disks are added or removed, causing the wrong device to be mounted. UUIDs are permanently tied to the filesystem and do not change.
- C) /dev/sdb1 is a symbolic link that expires after 24 hours; UUIDs are permanent entries in the kernel.
- D) ext4 filesystems cannot be mounted using device paths; only UUIDs, labels, or loop devices are supported.

Correct Answer: B) Device paths like /dev/sdb1 can change between reboots if disks are added or removed, causing the wrong device to be mounted. UUIDs are permanently tied to the filesystem and do not change.

Distractor Analysis:

- Why A is incorrect: systemd does accept device path entries in /etc/fstab. Both device paths and UUIDs are valid. The preference for UUIDs is about reliability and correctness, not a hard requirement.
- Why C is incorrect: /dev/sdb1 is a device node managed by udev, not a symbolic link with an expiration. However, udev can assign a different device node name to the same physical disk on the next boot if another disk is present, which is why UUIDs are preferred.
- Why D is incorrect: ext4 filesystems can be mounted by device path, UUID, or filesystem label. The fstab entry using /dev/sdb1 would work; it is simply less reliable than a UUID entry.

---

**Question 20**

An administrator runs `vgextend vg_data /dev/sdd1` and receives the error:

```
Device /dev/sdd1 not found (or ignored by filtering).
```

What is the most likely cause?

- A) /dev/sdd1 is already a member of another volume group.
- B) /dev/sdd1 has not been initialized as an LVM Physical Volume with pvcreate.
- C) The volume group vg_data is full and cannot accept additional physical volumes.
- D) vgextend requires the -f flag when adding partitions (as opposed to whole disks).

Correct Answer: B) /dev/sdd1 has not been initialized as an LVM Physical Volume with pvcreate.

Distractor Analysis:

- Why A is incorrect: If the device were already a member of another VG, the error message would typically indicate "Device already in use" or reference the existing VG. The "not found or ignored by filtering" message specifically indicates the device lacks a valid PV label.
- Why C is incorrect: A volume group has no limit on the number of physical volumes it can contain. Adding PVs to a VG always increases capacity; it cannot fail because the VG is "full" in this sense.
- Why D is incorrect: vgextend does not require a -f flag for partitions. The command syntax is the same regardless of whether the device is a whole disk or a partition. The -f flag in some LVM commands forces operations to proceed despite warnings but is not required for normal vgextend usage.
