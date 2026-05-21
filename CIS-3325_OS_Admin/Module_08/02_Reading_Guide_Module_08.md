# Reading Guide: Module 08 - Storage Management – Partitions, LVM, RAID
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 08 – Storage Management: Partitions, LVM, and RAID**! This week covers the full Linux storage stack — from raw disk partitioning with `fdisk` and `parted`, through filesystem creation with `mkfs`, to Logical Volume Management (LVM) and software RAID with `mdadm`. Storage management is one of the most exam-dense topics on CompTIA Linux+ XK0-005, appearing in Domain 1.0 (System Management).

As you work through this material you will learn how to partition disks, create and mount filesystems, manage volume groups and logical volumes, and configure RAID arrays for redundancy and performance.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **`fdisk` and `parted`**: Command-line tools for creating and managing disk partitions. `fdisk` works with MBR (legacy) partition tables and is interactive. `parted` supports both MBR and GPT and can be scripted non-interactively. `gdisk` is the GPT-specific equivalent of `fdisk`. After partitioning, run `partprobe` to notify the kernel of partition table changes without rebooting.
*   **`mkfs` (make filesystem)**: Creates a filesystem on a partition or logical volume. Common variants: `mkfs.ext4 /dev/sdb1`, `mkfs.xfs /dev/sdb1`, `mkfs.vfat /dev/sdb1`. XFS is the default on RHEL; ext4 is common on Debian/Ubuntu. Filesystem type affects performance, maximum file size, and journaling behavior.
*   **`/etc/fstab`**: The filesystem table — controls what gets mounted at boot and where. Each line contains: device (UUID or path), mount point, filesystem type, mount options, dump field, fsck order. Using UUID instead of device names (`/dev/sdb1`) prevents mount failures when disk device names change. The `mount -a` command mounts all entries in fstab that are not currently mounted.
*   **LVM (Logical Volume Manager)**: A three-layer abstraction for flexible storage management. Physical Volumes (PVs) → Volume Groups (VGs) → Logical Volumes (LVs). Key commands: `pvcreate`, `vgcreate`, `lvcreate -L 10G -n lv_data vg_data`, `lvextend -L +5G /dev/vg_data/lv_data`, then `resize2fs` (ext4) or `xfs_growfs` (XFS) to resize the filesystem to match. LVM allows resizing volumes without unmounting (on most filesystems).
*   **RAID levels**: RAID 0 (striping — performance, no redundancy), RAID 1 (mirroring — full redundancy, 50% capacity), RAID 5 (striping with distributed parity — requires 3+ disks, tolerates 1 disk failure), RAID 6 (tolerates 2 disk failures), RAID 10 (mirror of stripes — performance + redundancy, requires 4+ disks). Software RAID on Linux uses `mdadm`. Check array status with `cat /proc/mdstat`.
*   **`mount` and `umount`**: `mount /dev/sdb1 /mnt/data` mounts a partition at a directory. `mount -t ext4` specifies filesystem type. `umount /mnt/data` unmounts (device must not be busy — check with `lsof +D /mnt/data`). `df -h` shows mounted filesystems and their usage. `lsblk` shows the block device hierarchy including mount points.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Storage management maps to Linux+ Domain 1.0 (System Management). Expect 6–8 questions covering partitioning, LVM operations, filesystem creation, and fstab syntax.
*   **LVM sequence to memorize:** The exam tests the correct order: `pvcreate` → `vgcreate` → `lvcreate` → `mkfs` → `mount`. Reversing any step causes failure. After `lvextend`, you must still run `resize2fs` or `xfs_growfs` or the filesystem will not see the new space.
*   **RAID level trap:** RAID 0 provides *no* redundancy — a common distractor. Questions describe "maximum read/write performance with no fault tolerance" — answer is RAID 0. "Fault tolerance with minimum capacity loss using 3 disks" — answer is RAID 5.
*   **`/etc/fstab` UUID vs device name:** The exam presents fstab entries and asks which form is most reliable after adding a new disk. Always answer UUID — device names like `/dev/sdb` can change when disks are added or removed.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers storage and filesystems in chapters 15–16. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of disk partitioning, LVM setup, and filesystem management in a live environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 15–16 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), covering storage media, filesystems, and device management on Linux.
*   **Required Video:** Watch the storage and LVM videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist with live demonstrations of partitioning, filesystem creation, and LVM configuration.

---

### Lab & Command Integration
In this week's hands-on lab you will partition a virtual disk with `fdisk`, create an ext4 filesystem with `mkfs.ext4`, mount it and add a persistent entry to `/etc/fstab` using UUID, then create an LVM volume group and logical volume, format it, and extend it.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 15–16 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the storage management videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
