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
