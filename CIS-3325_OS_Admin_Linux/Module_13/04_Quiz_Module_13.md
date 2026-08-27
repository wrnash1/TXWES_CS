# Quiz: Module 13 — Storage and Logical Volume Management

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Instructions

Select the best answer for each question. Each question is worth 10 points.

---

### Questions

**Question 1**

An administrator needs to extend the logical volume `/dev/vg0/data` by 10 GB and automatically resize the XFS filesystem without unmounting it. Which command accomplishes this in a single step?

- A) `lvresize -L +10G /dev/vg0/data && xfs_growfs /dev/vg0/data`
- B) `lvextend -L +10G -r /dev/vg0/data`
- C) `lvextend -L +10G /dev/vg0/data && resize2fs /dev/vg0/data`
- D) `vgextend vg0 +10G && lvextend /dev/vg0/data`

**Correct Answer: B**

*Explanation: `lvextend -L +10G -r /dev/vg0/data` extends the logical volume AND resizes the filesystem automatically using the `-r` flag. For XFS, it calls `xfs_growfs`; for ext4, it calls `resize2fs`. Option C uses `resize2fs` which does not work with XFS.*

---

**Question 2**

Which field in an `/etc/fstab` entry controls the order in which `fsck` checks filesystems at boot?

- A) Field 4 (options)
- B) Field 5 (dump)
- C) Field 6 (pass)
- D) Field 3 (filesystem type)

**Correct Answer: C**

*Explanation: The sixth field (pass) controls fsck order. `0` = skip fsck, `1` = check first (root filesystem), `2` = check after root. The fifth field (dump) controls whether the `dump` backup utility includes this filesystem.*

---

**Question 3**

A system has four 3 TB drives configured as RAID 5. What is the total usable storage capacity?

- A) 12 TB
- B) 9 TB
- C) 6 TB
- D) 3 TB

**Correct Answer: B**

*Explanation: RAID 5 usable capacity = (N-1) × disk size = (4-1) × 3 TB = 9 TB. One disk equivalent is used for distributed parity. With 4 disks, RAID 5 can tolerate 1 disk failure.*

---

**Question 4**

An administrator creates a new 20 GB logical volume and runs `mkfs.ext4` on it, but then realizes the volume group did not have 20 GB free. Which scenario is most accurate?

- A) `lvcreate` would have failed before `mkfs.ext4` was reached
- B) `mkfs.ext4` would have silently created a smaller filesystem
- C) `lvcreate` would have succeeded but `mkfs.ext4` would fail
- D) Both commands would succeed but data writes would fail later

**Correct Answer: A**

*Explanation: `lvcreate` checks VG free space before allocating. If insufficient space is available, `lvcreate` fails with an error before any filesystem is created. You would never reach the `mkfs` step.*

---

**Question 5**

After editing `/etc/fstab` to add a new mount entry, an administrator wants to verify the entry is correct without rebooting. Which command tests all fstab entries?

- A) `mount --verify-fstab`
- B) `systemctl reload fstab`
- C) `mount -a`
- D) `fstab --test`

**Correct Answer: C**

*Explanation: `mount -a` mounts all entries in `/etc/fstab` that are not already mounted. If an entry has a syntax error or references a non-existent device or mount point, it will fail with an error message. This is the standard way to test fstab changes before rebooting.*

---

**Question 6**

A storage administrator needs RAID that can survive the failure of two disks simultaneously, using four 6 TB drives. Which RAID level is the MOST space-efficient option that meets this requirement?

- A) RAID 10
- B) RAID 6
- C) RAID 5
- D) RAID 1

**Correct Answer: B**

*Explanation: RAID 6 uses double parity and can tolerate 2 simultaneous disk failures. With 4 × 6 TB drives: (4-2) × 6 TB = 12 TB usable. RAID 10 also tolerates 2 failures (one per mirrored pair) but only provides 12 TB usable with the same 4 drives, with identical capacity. However, RAID 6 scales better with more drives and is generally considered more space-efficient for >4 disk arrays.*

---

**Question 7**

What is the correct sequence to add a second physical disk to an existing LVM volume group named `datavg`?

- A) `vgextend datavg /dev/sdc` → `pvcreate /dev/sdc`
- B) `pvcreate /dev/sdc` → `vgextend datavg /dev/sdc`
- C) `vgcreate datavg /dev/sdc` → `pvmove /dev/sdc`
- D) `lvcreate -d /dev/sdc datavg` → `vgextend datavg`

**Correct Answer: B**

*Explanation: The correct sequence is always: (1) initialize the new disk as a physical volume with `pvcreate`, then (2) add it to the volume group with `vgextend`. `vgextend` requires the device to already be a PV.*

---

**Question 8**

An administrator runs `df -h` and notices a filesystem at `/var/log` shows 95% usage. They then run `du -sh /var/log/*` and the total from `du` is only 2 GB, but `df` shows 18 GB used on an 20 GB filesystem. What is the most likely explanation?

- A) `du` does not include subdirectories in its calculation
- B) A process has open file handles on deleted log files, holding the space
- C) The filesystem has a 90% reserved blocks setting configured
- D) `df` is reporting inode usage, not block usage

**Correct Answer: B**

*Explanation: When a file is deleted but a process still has an open file descriptor to it, the inode is unlinked but the blocks are not freed until the file descriptor is closed. `du` only counts linked files; `df` counts all allocated blocks. Restarting the process (e.g., `systemctl restart rsyslog`) releases the open handle and frees the space.*

---

**Question 9**

Which tool should an administrator use to check and repair an unmounted ext4 filesystem on `/dev/vg0/data`?

- A) `xfs_repair /dev/vg0/data`
- B) `fsck /dev/vg0/data`
- C) `e2fsck /dev/vg0/data`
- D) Both B and C are correct

**Correct Answer: D**

*Explanation: `fsck` is a front-end that calls the appropriate filesystem-specific tool. `fsck /dev/vg0/data` will detect it is ext4 and call `e2fsck` automatically. Running `e2fsck` directly is equally valid. `xfs_repair` is only for XFS filesystems.*

---

**Question 10**

An administrator needs to shrink an ext4 logical volume from 20 GB to 15 GB. The filesystem is currently mounted. What is the correct first step?

- A) Run `lvreduce -L 15G -r /dev/vg0/data`
- B) Run `resize2fs /dev/vg0/data 15G` while the filesystem is mounted
- C) Unmount the filesystem
- D) Run `fsck -f /dev/vg0/data` while the filesystem is mounted

**Correct Answer: C**

*Explanation: Shrinking an ext4 filesystem requires it to be unmounted first. The correct sequence is: (1) unmount, (2) run fsck, (3) shrink the filesystem with resize2fs, (4) shrink the LV with lvreduce, (5) remount. Attempting to resize a mounted filesystem can cause data corruption.*

---

**Question 11** (5 points)

An administrator wants to move all physical extents from `/dev/sdb1` to other PVs in the same volume group so that `/dev/sdb1` can be safely removed. Which command initiates this data migration?

- A) `pvremove /dev/sdb1`
- B) `vgreduce vg0 /dev/sdb1`
- C) `pvmove /dev/sdb1`
- D) `lv migrate /dev/sdb1`

**Correct Answer: C**

*Explanation: `pvmove /dev/sdb1` migrates all physical extents (and thus the data) from `/dev/sdb1` to other PVs in the volume group while the LV remains online and mounted. After `pvmove` completes, `vgreduce vg0 /dev/sdb1` removes it from the VG, and `pvremove /dev/sdb1` clears the PV label. Running `pvremove` or `vgreduce` before `pvmove` would destroy data.*

---

**Question 12** (5 points)

A RAID 5 array with 5 drives experiences two simultaneous disk failures. What is the result?

- A) The array degrades to a reduced capacity but remains operational.
- B) The array enters read-only mode to prevent further data loss.
- C) The array fails and data is lost because RAID 5 tolerates only one disk failure.
- D) The array automatically rebuilds using a hot spare.

**Correct Answer: C**

*Explanation: RAID 5 uses single distributed parity and can tolerate exactly one simultaneous disk failure. With two failed drives, there is insufficient parity information to reconstruct the data — the array fails and data is unrecoverable without backups. RAID 6 is required to tolerate two simultaneous failures. Hot spare behavior is a configuration option, not a RAID 5 inherent feature, and it would not help after two simultaneous failures.*

---

**Question 13** (5 points)

Which command displays the status of a software RAID array `/dev/md0` including whether it is degraded and how many drives are active?

- A) `mdadm --status /dev/md0`
- B) `mdadm --detail /dev/md0`
- C) `cat /proc/mdstat`
- D) Both B and C provide this information

**Correct Answer: D**

*Explanation: Both `mdadm --detail /dev/md0` and `cat /proc/mdstat` show RAID array status including active/degraded state and drive count. `mdadm --detail` provides structured output with drive roles, UUIDs, and rebuild progress. `/proc/mdstat` provides a quick kernel-level summary. Option A uses invalid syntax.*

---

**Question 14** (5 points)

What does the `noatime` mount option accomplish, and in what scenario would it provide the most benefit?

- A) It prevents the filesystem from recording access times on reads, which reduces write I/O on read-heavy workloads.
- B) It disables all timestamp recording to make the filesystem read-only.
- C) It prevents the system clock from updating atime fields during NFS operations.
- D) It causes access time to be recorded only when the file is opened, not when it is read.

**Correct Answer: A**

*Explanation: Every file read normally triggers a metadata write to update the `atime` (access time) field. The `noatime` option disables this write, reducing I/O and improving performance particularly on read-heavy workloads like web server document roots or database directories. A related option, `relatime`, updates atime only when it is older than mtime — a compromise between `atime` and `noatime`.*

---

**Question 15** (5 points)

An administrator uses `blkid` to find the UUID of `/dev/sdb1` and records it as `1a2b3c4d-...`. Later, the drive is removed and a new drive is installed and partitioned. The new `/dev/sdb1` has a different UUID. An fstab entry that uses `UUID=1a2b3c4d-...` will behave in which way?

- A) The mount will succeed using the new drive because device names override UUIDs.
- B) The mount will fail at boot because no device has the recorded UUID.
- C) The system will prompt for a new UUID during boot.
- D) The mount will succeed because `/dev/sdb1` is implicitly used as a fallback.

**Correct Answer: B**

*Explanation: fstab entries using UUID are tied to that specific UUID, not to a device name. If no device with that UUID exists (because the old drive was replaced), the mount fails at boot. With `nofail` in the mount options, the failure is non-fatal. Without it, the system may enter emergency mode. This illustrates why changing drives requires updating fstab with the new device's UUID.*

---

**Question 16** (5 points)

Which `lvcreate` command creates a 500 MB LVM snapshot named `data_snap` of the logical volume `/dev/vg0/data`?

- A) `lvcreate -L 500M --snapshot -n data_snap /dev/vg0/data`
- B) `lvcreate -s -L 500M -n data_snap /dev/vg0/data`
- C) `lvcreate -S 500M -n data_snap /dev/vg0/data`
- D) Both A and B are correct

**Correct Answer: D**

*Explanation: Both `--snapshot` (long form) and `-s` (short form) are valid flags for creating an LVM snapshot. Both option A and option B specify the snapshot size (500M), snapshot name (`data_snap`), and source volume (`/dev/vg0/data`). The snapshot size determines how much change data can be recorded before the snapshot becomes invalid.*

---

**Question 17** (5 points)

A volume group has 30 GB free. An administrator wants to create a logical volume using all remaining free space. Which command is correct?

- A) `lvcreate -L 30G -n newvol vg0`
- B) `lvcreate -l 100%FREE -n newvol vg0`
- C) `lvcreate -L 100% -n newvol vg0`
- D) `lvcreate --all-free -n newvol vg0`

**Correct Answer: B**

*Explanation: Lowercase `-l` (extents) allows special size specifiers like `100%FREE`, `100%VG`, and `100%PVS`. Uppercase `-L` (size) requires an absolute size in bytes, MB, GB, etc. `100%FREE` allocates all free extents in the VG. `100%VG` would try to use all VG space including already-allocated space and would fail.*

---

**Question 18** (5 points)

After a hard power failure, an XFS filesystem mounted at `/data` shows corruption. The correct repair command is:

- A) `fsck -y /dev/vg0/data` while the filesystem is mounted
- B) `xfs_repair /dev/vg0/data` after unmounting the filesystem
- C) `e2fsck -f /dev/vg0/data` after unmounting the filesystem
- D) `mount -o remount,repair /data`

**Correct Answer: B**

*Explanation: XFS filesystems are repaired with `xfs_repair`, not `fsck` or `e2fsck` (which are for ext2/3/4). The filesystem MUST be unmounted before running `xfs_repair`. Running repair on a mounted filesystem will cause data corruption. `mount -o remount,repair` is not a valid option.*

---

**Question 19** (5 points)

What is the purpose of the `discard` (also written as `trim`) mount option for an SSD-backed filesystem?

- A) It enables the OS to inform the SSD controller which blocks are no longer in use, allowing the drive to optimize storage internally.
- B) It discards all journal entries to improve write performance.
- C) It prevents files from being recovered after deletion.
- D) It enables write-back caching for improved sequential write speed.

**Correct Answer: A**

*Explanation: The TRIM/discard operation tells the SSD controller that certain logical blocks are no longer allocated (after file deletion or filesystem operations). This allows the SSD to perform garbage collection more efficiently, maintaining write performance over time. The `discard` option enables this passively (on every delete). The alternative is `fstrim`, run periodically (weekly via cron or systemd timer) to batch-process TRIM commands.*

---

**Question 20** (5 points)

An administrator runs `pvdisplay /dev/sdc1` and sees `Allocatable: YES (but full)`. What does this mean?

- A) The PV can accept new physical extents from a vgextend operation.
- B) The PV is part of a volume group and all of its physical extents have been allocated to logical volumes.
- C) The PV is being used by a snapshot that is consuming all available space.
- D) The PV has no more room for filesystem data but metadata can still be written.

**Correct Answer: B**

*Explanation: `Allocatable: YES (but full)` means the PV is a member of a volume group (YES = allocatable) and all of its Physical Extents (PEs) have been allocated to one or more logical volumes. To use this PV for new logical volumes, you would first need to free space by shrinking or removing an existing LV, or by adding a new PV to the VG.*

---

### Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | C |
| 3 | B |
| 4 | A |
| 5 | C |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | D |
| 10 | C |
| 11 | C |
| 12 | C |
| 13 | D |
| 14 | A |
| 15 | B |
| 16 | D |
| 17 | B |
| 18 | B |
| 19 | A |
| 20 | B |
