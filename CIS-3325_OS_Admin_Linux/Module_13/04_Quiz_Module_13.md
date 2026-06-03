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
