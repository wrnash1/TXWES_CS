# Quiz: Module 08 - Storage Management – Partitions, LVM, RAID
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator has just created a new logical volume `/dev/vg_data/lv_data` and wants to extend it by 10 gigabytes. After running `lvextend -L +10G /dev/vg_data/lv_data`, the `df -h` output shows the filesystem size has not changed. What additional step is required for an ext4 filesystem?
A) Run `vgextend vg_data /dev/sdc` to add space to the volume group.
B) Run `resize2fs /dev/vg_data/lv_data` to resize the filesystem to match the new logical volume size.
C) Unmount the filesystem and recreate it with `mkfs.ext4`.
D) Run `partprobe` to notify the kernel of the size change.
*   **Correct Answer:** B) Run `resize2fs /dev/vg_data/lv_data` to resize the filesystem to match the new logical volume size.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `vgextend` adds a new physical volume to an existing volume group to increase the VG's total capacity. In this scenario the LV has already been extended; the remaining issue is that the *filesystem* on the LV does not yet know about the extra space.
    *   *Why C is incorrect:* Recreating the filesystem with `mkfs.ext4` would destroy all data on the volume. `resize2fs` can grow an ext4 filesystem non-destructively.
    *   *Why D is incorrect:* `partprobe` informs the kernel about partition table changes on a disk device. It has no effect on LVM logical volumes, which are not partitions.

---

---

**Question 2**
A storage administrator needs to configure software RAID across three disks (`/dev/sdb`, `/dev/sdc`, `/dev/sdd`) to maximize available capacity while tolerating a single disk failure. Which RAID level is most appropriate?
A) RAID 0
B) RAID 1
C) RAID 5
D) RAID 10
*   **Correct Answer:** C) RAID 5
*   **Distractor Analysis:**
    *   *Why A is incorrect:* RAID 0 (striping) distributes data across all disks for maximum performance and capacity, but provides zero fault tolerance. A single disk failure destroys all data.
    *   *Why B is incorrect:* RAID 1 (mirroring) requires an even number of disks and uses half the total capacity for redundancy. With three disks, RAID 1 is inefficient and wastes one disk's worth of capacity compared to RAID 5.
    *   *Why D is incorrect:* RAID 10 requires a minimum of four disks (two mirrored pairs). It cannot be created with only three disks.

---

---

**Question 3**
An administrator needs to restrict a configuration file so only the file owner can read and write it, with no access for group or others. Which command achieves this?
A) chmod 600 config.conf
B) chmod 640 config.conf
C) chmod 644 config.conf
D) chmod 660 config.conf
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `chmod 640` gives the owner rw- (read+write) but gives the group r-- (read-only). The requirement specifies no group access.
    *   *Why C is incorrect:* `chmod 644` gives owner rw- and both group and others r-- (read-only). This does not meet the requirement of no access for group or others.
    *   *Why D is incorrect:* `chmod 660` gives both owner and group rw- (read+write), with no access for others. This still grants group access, violating the requirement.

---

**Question 4**
An administrator needs to make a filesystem mount persist across reboots. They add an entry to `/etc/fstab`. Which device identifier is most reliable to use in the fstab entry for a partition on an additional data disk?
A) /dev/sdb1
B) The device's UUID (e.g., UUID=a1b2c3d4-...)
C) The disk's model name from `lshw`
D) The partition label if one was set during mkfs
*   **Correct Answer:** B) The device's UUID (e.g., UUID=a1b2c3d4-...)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Device names like `/dev/sdb1` are assigned by the kernel at boot based on detection order. Adding a new disk or changing a disk's physical port can change these names, causing boot failures if fstab uses them.
    *   *Why C is incorrect:* Model names from hardware inventory tools are not valid fstab device identifiers. The kernel does not use model names to locate block devices during the mount process.
    *   *Why D is incorrect:* Partition labels (set with `e2label` or `xfs_admin -L`) can also be used in fstab with the `LABEL=` syntax, and they are more stable than device names. However, UUID is the most universally reliable identifier because it is guaranteed to be globally unique and does not require the administrator to manually set a label.

---

**Question 5**
A systems administrator runs `cat /proc/mdstat` and sees the array listed as `[UU_]`, indicating one drive has failed in a RAID 5 array. What does the underscore `_` represent, and what is the correct next step?
A) The underscore means the array is performing a rebuild. Wait for it to complete automatically.
B) The underscore represents a failed or missing disk. Replace the failed drive and add it back to the array with `mdadm --manage /dev/md0 --add /dev/sdd`.
C) The underscore means the array is in read-only mode. Run `mdadm --readwrite /dev/md0` to restore write access.
D) The underscore indicates the array needs defragmentation. Run `e2fsck -f /dev/md0` to repair it.
*   **Correct Answer:** B) The underscore represents a failed or missing disk. Replace the failed drive and add it back to the array with `mdadm --manage /dev/md0 --add /dev/sdd`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* During a rebuild (resync), `mdstat` shows `_` for the missing disk and a rebuild progress percentage. The `_` itself represents a failed/missing device; a rebuild only begins after a replacement drive is added with `--add`.
    *   *Why C is incorrect:* There is no `--readwrite` option for `mdadm`. Read-only state is a separate condition shown differently in `mdstat`. A `_` specifically indicates a missing or failed array member.
    *   *Why D is incorrect:* `e2fsck` checks ext2/3/4 filesystem integrity on a device. It is not a RAID-level tool and does not repair missing RAID members. Running `e2fsck` on a degraded array without replacing the failed disk would not restore redundancy.

