# Quiz: Module 06 — Storage and Disk Management

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

An administrator needs to add a 6TB hard drive to a Linux server and create multiple partitions on it. Which partition table format must be used, and why?

A. MBR, because it is more compatible with older Linux kernels

B. GPT, because MBR cannot address disks larger than 2TB

C. MBR, because GPT requires UEFI and the server uses BIOS

D. Either format works for 6TB disks; the choice is a matter of preference

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. MBR compatibility with older kernels is not relevant here. The hard limitation is MBR's maximum addressable disk size of 2TB — a 6TB disk cannot be fully utilized with MBR.
- **B** is correct. MBR uses 32-bit addressing for sectors, which caps addressable capacity at 2TB (2^32 × 512 bytes). A 6TB disk requires GPT, which uses 64-bit LBA addressing and supports disks up to 9.4 ZB.
- **C** is incorrect. While GPT is associated with UEFI, modern Linux supports GPT on both UEFI and traditional BIOS systems. BIOS is not a disqualifier for GPT on Linux servers.
- **D** is incorrect. For a 6TB disk, preference is irrelevant — MBR will fail to see the full disk. GPT is the only valid choice.

---

### Question 2

An administrator runs `blkid` and notes the UUID of a partition. They want to add this partition to `/etc/fstab` to be mounted at `/mnt/archive` on boot. Which fstab entry is correct?

A. `/dev/sdb1  /mnt/archive  ext4  defaults  0  2`

B. `UUID=abc123  /mnt/archive  ext4  defaults  0  2`

C. `UUID=abc123  /mnt/archive  ext4  defaults  2  0`

D. `UUID=abc123  ext4  /mnt/archive  defaults  0  2`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Using `/dev/sdb1` is not wrong syntactically, but it is poor practice. Device names are assigned by kernel detection order and can change if disks are added or removed, potentially mounting the wrong partition. UUID is the recommended stable identifier.
- **B** is correct. The six fstab fields in correct order: device (UUID=abc123), mountpoint (/mnt/archive), filesystem type (ext4), options (defaults), dump (0), pass (2). Pass=2 means fsck checks this partition after the root filesystem.
- **C** is incorrect. The dump and pass fields are reversed. `2 0` would mean dump=2 (back up this filesystem — unusual) and pass=0 (skip fsck). Correct is `0 2` for a non-root filesystem.
- **D** is incorrect. The filesystem type and mountpoint are swapped. fstab field order is fixed: device, mountpoint, fstype, options, dump, pass. Swapping them causes mount failures.

---

### Question 3

An administrator creates a new partition, formats it with ext4, and mounts it. After rebooting, the partition is not mounted. What is the most likely cause?

A. The ext4 filesystem needs to be re-created after every reboot

B. The partition was not added to `/etc/fstab`

C. The UUID changed after the reboot

D. The `mount -a` command needs to be run after every reboot

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Filesystems persist across reboots — their data is on disk. Re-creating the filesystem would destroy all data, which is obviously not the intended behavior.
- **B** is correct. `mount` commands issued at the command line are not persistent. `/etc/fstab` is the configuration file that systemd/init reads during boot to mount filesystems automatically. Without an fstab entry, the mount does not survive a reboot.
- **C** is incorrect. UUIDs are assigned when a filesystem is created with `mkfs` and do not change across reboots. A UUID changes only if the filesystem is reformatted.
- **D** is incorrect. `mount -a` is a manual command that mounts all fstab entries. It is not run automatically at each boot as a standalone command — systemd processes fstab directly. Even if `mount -a` needed to be run manually, the root cause is still the missing fstab entry.

---

### Question 4

A sysadmin has a Volume Group with 10GB of free space. They run `lvextend -L +3G /dev/myvg/datalv` successfully. However, `df -h` still shows the same available space on the `/data` mount point. What must be done next?

A. Unmount and remount the filesystem

B. Run `resize2fs /dev/myvg/datalv` to expand the filesystem

C. Run `vgextend myvg` to make the new space available

D. Reboot the server to apply the LVM changes

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Remounting does not resize a filesystem. The filesystem's internal metadata still describes the original size — remounting does not change that. (Note: for xfs specifically, xfs_growfs requires the filesystem to be mounted, but the repair command itself is still needed.)
- **B** is correct. `lvextend` expands the logical volume (the block device). The filesystem inside it is unchanged and does not automatically know about the additional space. `resize2fs` reads the new LV size and expands the ext4 filesystem to use all available space. This can be done while the filesystem is mounted.
- **C** is incorrect. `vgextend` adds more physical volumes to a volume group to increase its total capacity. The volume group already has sufficient free space in this scenario — the problem is that the filesystem has not been told about the newly extended logical volume.
- **D** is incorrect. LVM and filesystem resize operations do not require a reboot. The entire value of LVM for operations teams is the ability to perform these changes live, without service interruption.

---

### Question 5

An administrator formatted `/dev/sdb3` as ext4 and wants to run `fsck` to check its integrity. The partition is currently mounted at `/mnt/archive`. What must happen before running fsck?

A. Nothing — modern fsck can safely check mounted ext4 filesystems

B. The filesystem must be unmounted before running fsck

C. The partition must be remounted as read-only before running fsck

D. The data must be backed up before running fsck

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. This is false and dangerous. Running fsck on a mounted filesystem will corrupt the filesystem. fsck modifies metadata structures while the filesystem is live, conflicting with the kernel's own filesystem operations.
- **B** is correct. fsck must only run on unmounted filesystems. `sudo umount /mnt/archive` must be executed first. For the root filesystem, this means using rescue media or single-user mode.
- **C** is incorrect. Read-only mounting (`mount -o remount,ro`) reduces write activity but does not make fsck safe. The kernel still has internal state about the filesystem that conflicts with fsck's analysis. Unmounting is the only safe approach.
- **D** is incorrect. While backing up before any potentially destructive operation is good practice, it is not a prerequisite for running fsck. The required action is unmounting the filesystem.

---

### Question 6

A Linux administrator needs to set up a RAID configuration that can tolerate the failure of any single disk while using exactly four 2TB drives. They also need the best possible read and write performance. Which RAID level best meets these requirements?

A. RAID 0

B. RAID 1

C. RAID 5

D. RAID 10

**Correct Answer: D**

**Distractor Analysis:**

- **A** is incorrect. RAID 0 provides excellent performance but offers no redundancy whatsoever. The failure of any single disk in a RAID 0 array results in complete data loss. This directly violates the requirement to tolerate a single disk failure.
- **B** is incorrect. RAID 1 (mirroring) can only use two disks in a mirror pair. With four disks, you would need two separate RAID 1 pairs. RAID 10 is the correct name for the combination, and RAID 1 alone does not achieve the best performance across four drives.
- **C** is incorrect. RAID 5 can tolerate one disk failure and uses four drives efficiently (3/4 = 75% usable). However, RAID 5 write performance suffers from parity calculation overhead. RAID 10 provides superior write performance.
- **D** is correct. RAID 10 (mirrored stripes) creates two mirror pairs and stripes data across them. It provides the performance of striping (RAID 0) combined with the redundancy of mirroring (RAID 1). With four 2TB drives, you get 4TB usable. Any single disk can fail (one from each mirror pair can fail in the best case). Performance is the best available for a redundant configuration.

---

### Question 7

An administrator checks SMART data and sees that the `Reallocated_Sector_Ct` attribute has a value of 47 and has increased by 12 over the past two weeks. What action is appropriate?

A. This is normal wear — no action is required

B. Run `fsck -y` on the disk to repair the bad sectors

C. Plan an immediate disk replacement and restore from backup

D. Increase the disk's priority in the RAID array to rebuild the bad sectors

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. A growing `Reallocated_Sector_Ct` is a serious warning sign. The drive is finding sectors that can no longer reliably store data and remapping them to spare sectors. A growing count means the drive is actively degrading and spare sectors will eventually be exhausted.
- **B** is incorrect. `fsck` repairs filesystem metadata — it cannot repair bad physical sectors on a hard drive. SMART reallocated sectors are a hardware problem that software filesystem tools cannot address.
- **C** is correct. An increasing `Reallocated_Sector_Ct` indicates a failing drive. The appropriate response is to restore from backup (to verify backup integrity) and plan replacement before the drive fails completely. Drives do not "recover" from bad sector accumulation.
- **D** is incorrect. There is no mechanism to increase a disk's "priority" in RAID or to rebuild bad sectors via RAID operations. If the disk is part of a RAID array, the correct action is still to replace the failing drive and allow the array to rebuild onto the new disk.

---

### Question 8

What command correctly creates an LVM Logical Volume named `applv` with a size of 8GB inside the Volume Group named `appvg`?

A. `lvcreate -n 8G -L applv appvg`

B. `lvcreate -L 8G -n applv appvg`

C. `vgcreate appvg -L 8G applv`

D. `lvcreate appvg applv 8G`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. The `-n` and `-L` flags are switched. `-n` takes the logical volume name as its argument; `-L` takes the size. In option A, `-n 8G` would try to name the LV "8G" and `-L applv` would fail because "applv" is not a valid size specification.
- **B** is correct. `lvcreate -L 8G -n applv appvg` — `-L 8G` sets the size to 8 gigabytes, `-n applv` sets the name, and `appvg` is the Volume Group to allocate from.
- **C** is incorrect. `vgcreate` creates a Volume Group, not a Logical Volume. Additionally, the syntax is entirely wrong. Volume groups are created with `vgcreate NAME PHYSICAL_VOLUMES`.
- **D** is incorrect. `lvcreate` does not accept positional arguments in this order. The VG name, LV name, and size must all be specified with their respective flags.

---

### Question 9

An administrator adds a new 10GB disk to a server. They run `pvcreate /dev/sdc`, then `vgextend datavg /dev/sdc`. What is the result?

A. A new Volume Group named `datavg` was created with 10GB capacity

B. The existing Volume Group `datavg` now has 10GB more free space available

C. A new 10GB Logical Volume was created in `datavg`

D. The disk `/dev/sdc` was formatted with ext4 and added to `datavg`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. `vgcreate` creates a new Volume Group. `vgextend` adds to an existing one. The command shown uses `vgextend`, which requires that `datavg` already exists.
- **B** is correct. `pvcreate /dev/sdc` initializes the disk as a Physical Volume. `vgextend datavg /dev/sdc` adds that PV to the existing Volume Group `datavg`, increasing the pool of available storage by 10GB. Logical Volumes can then be created from or extended into this space.
- **C** is incorrect. `lvcreate` creates a Logical Volume. Neither `pvcreate` nor `vgextend` creates an LV — they operate at the PV and VG layers respectively.
- **D** is incorrect. `pvcreate` writes an LVM metadata label, not a filesystem. The disk is not formatted with ext4. Filesystems are created on Logical Volumes (with `mkfs`), not on Physical Volumes directly.

---

### Question 10

An administrator runs `sudo swapoff /swapfile` and observes that the system's available memory immediately increases by 512MB. What does this indicate?

A. The system was using the swap file to store active process data

B. The swap file contained 512MB of rarely accessed process memory that was paged in

C. The swapoff command freed filesystem space by deleting the swapfile

D. The system allocated 512MB of RAM to replace the deactivated swap

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect (partially). The statement is true in direction but inaccurate in implication. swapoff moves pages from swap back to RAM, and this uses RAM. The RAM "increase" actually reflects previously swapped pages that could not be accounted as usable while in swap.
- **B** is correct. When `swapoff` is executed, the kernel moves all pages currently stored in the swap file back into physical RAM. If 512MB of process memory was paged out to swap, swapoff reads it back into RAM. If there is not enough RAM to hold all swapped pages, swapoff will fail. The apparent increase in used RAM is the swap content being returned to memory.
- **C** is incorrect. `swapoff` deactivates swap — it does not delete the file. The file still exists on disk. Deleting it would be done with `rm /swapfile` as a separate step. Filesystem space is not freed by swapoff alone.
- **D** is incorrect. RAM is not "allocated" as a replacement for swap — RAM capacity is fixed by the physical hardware. What happens is that pages from swap are moved back into existing RAM. If RAM is nearly full, swapoff may fail or cause the OOM killer to activate.

---

## Answer Key

| Question | Answer |
|---|---|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | B |
| 6 | D |
| 7 | C |
| 8 | B |
| 9 | B |
| 10 | B |

---

*End of Module 06 Quiz*
