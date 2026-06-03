# Lab: Module 06 — Storage and Disk Management

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Lab Overview

**Estimated Time:** 75–90 minutes

**Environment:** Linux VM (Ubuntu 22.04 LTS recommended) with at least one additional unpartitioned disk (add a second virtual disk in VirtualBox/VMware before starting); sudo required throughout

**Purpose:** Practice the complete storage management lifecycle — partitioning, formatting, mounting, LVM configuration, swap management, and disk health inspection.

---

## Safety Notice

All destructive operations in this lab target `/dev/sdb` — the second disk in your VM. Before running any partitioning or format command, verify your target device with `lsblk`. Running these commands against `/dev/sda` (your system disk) will destroy your VM installation. When in doubt, stop and ask.

---

## Objectives

By the end of this lab you will be able to:

- Add a virtual disk to a VM and identify it in Linux
- Create MBR and GPT partition tables and partitions with fdisk
- Format partitions with ext4 and xfs
- Configure persistent mounts in /etc/fstab using UUID
- Create a Physical Volume, Volume Group, and Logical Volume with LVM
- Extend a Logical Volume and resize its filesystem online
- Create and activate swap space
- Run fsck on an unmounted filesystem
- Inspect disk health with smartctl

---

## Pre-Lab Setup

### Add a Second Virtual Disk

If using VirtualBox:

1. With the VM powered off, open Settings → Storage
2. Click the + icon next to the SATA controller
3. Add Hard Disk → Create New → VDI → Dynamically allocated → 20 GB
4. Start the VM

Verify the new disk appears:

```bash
lsblk
```

You should see `/dev/sdb` with no partitions listed. If you see `/dev/sdc` instead, substitute `sdc` everywhere `sdb` appears in this lab.

Install required tools:

```bash
sudo apt update
sudo apt install -y lvm2 smartmontools sysstat xfsprogs
```

---

## Part 1 — Disk Exploration (10 minutes)

### Task 1.1 — Survey the Storage Layout

```bash
# View all block devices
lsblk

# View with filesystem information
lsblk -f

# View all UUIDs and labels
blkid

# Show disk geometry for the second disk
sudo fdisk -l /dev/sdb
```

Record:

- Total size of `/dev/sdb`
- Current partition table type (or "unpartitioned")

### Task 1.2 — Verify No Existing Data

```bash
# Confirm the disk has no partition table yet
sudo parted /dev/sdb print
```

Expected output: "unrecognised disk label" — confirming the disk is blank.

---

## Part 2 — Partitioning (20 minutes)

### Task 2.1 — Create a GPT Partition Table and Partitions

```bash
sudo fdisk /dev/sdb
```

Inside fdisk, perform these steps in order:

1. Press `g` — create a new GPT partition table (this wipes any existing data)
2. Press `p` — confirm the table was created (should show no partitions yet)
3. Press `n` — new partition; accept defaults for number and first sector; enter `+5G` for last sector
4. Press `n` — new partition; accept defaults; enter `+5G` for last sector
5. Press `n` — new partition; accept defaults; use remaining space (just press Enter)
6. Press `p` — review: you should see three partitions
7. Press `w` — write and exit

Verify:

```bash
lsblk /dev/sdb
```

Expected: `/dev/sdb1` (5G), `/dev/sdb2` (5G), `/dev/sdb3` (remaining ~10G)

### Task 2.2 — Examine Partition Details

```bash
sudo fdisk -l /dev/sdb
```

Record: What partition type (filesystem type code) does fdisk assign by default to new partitions?

---

## Part 3 — Filesystem Creation and Mounting (20 minutes)

### Task 3.1 — Format Partitions

```bash
# Format sdb1 as ext4 with a label
sudo mkfs.ext4 -L "ext4data" /dev/sdb1

# Format sdb2 as xfs
sudo mkfs.xfs -L "xfsdata" /dev/sdb2

# Note: sdb3 will be used for LVM in Part 4
```

### Task 3.2 — Temporary Mounts

```bash
sudo mkdir -p /mnt/ext4part /mnt/xfspart

sudo mount /dev/sdb1 /mnt/ext4part
sudo mount /dev/sdb2 /mnt/xfspart

# Verify
df -h /mnt/ext4part /mnt/xfspart
lsblk /dev/sdb
```

Create test files:

```bash
echo "test data on ext4" | sudo tee /mnt/ext4part/test.txt
echo "test data on xfs" | sudo tee /mnt/xfspart/test.txt
```

### Task 3.3 — Persistent Mounts in fstab

```bash
# Get UUIDs for both partitions
blkid /dev/sdb1 /dev/sdb2
```

Copy both UUIDs. Now edit fstab:

```bash
sudo cp /etc/fstab /etc/fstab.backup
sudo nano /etc/fstab
```

Add these two lines (substitute your actual UUIDs):

```
UUID=YOUR_SDB1_UUID  /mnt/ext4part  ext4  defaults  0  2
UUID=YOUR_SDB2_UUID  /mnt/xfspart   xfs   defaults,noatime  0  2
```

Save and exit nano.

Test without rebooting:

```bash
sudo umount /mnt/ext4part /mnt/xfspart
sudo mount -a
```

Verify the mounts came back:

```bash
df -h /mnt/ext4part /mnt/xfspart
cat /mnt/ext4part/test.txt
cat /mnt/xfspart/test.txt
```

**Question:** What would happen during boot if you had a typo in the UUID in fstab? What does the `nofail` option do to mitigate this risk?

---

## Part 4 — LVM (20 minutes)

### Task 4.1 — Create a Physical Volume

```bash
# Initialize sdb3 as an LVM physical volume
sudo pvcreate /dev/sdb3

# Verify
sudo pvs
sudo pvdisplay /dev/sdb3
```

### Task 4.2 — Create a Volume Group

```bash
sudo vgcreate labvg /dev/sdb3

sudo vgs
sudo vgdisplay labvg
```

Record: How much free space (VFree) is available in the volume group?

### Task 4.3 — Create and Use a Logical Volume

```bash
# Create a 2GB logical volume
sudo lvcreate -L 2G -n lablv labvg

sudo lvs
sudo lvdisplay /dev/labvg/lablv

# Format as ext4
sudo mkfs.ext4 /dev/labvg/lablv

# Mount it
sudo mkdir -p /mnt/lvm_test
sudo mount /dev/labvg/lablv /mnt/lvm_test

df -h /mnt/lvm_test
```

Create a test file:

```bash
echo "LVM test data" | sudo tee /mnt/lvm_test/lvm_test.txt
```

### Task 4.4 — Extend the Logical Volume Online

```bash
# Extend by 1GB while the filesystem is mounted
sudo lvextend -L +1G /dev/labvg/lablv

# The filesystem does not know about the new space yet
df -h /mnt/lvm_test    # Should still show 2GB

# Resize the filesystem to fill the new LV space
sudo resize2fs /dev/labvg/lablv

# Verify the filesystem expanded
df -h /mnt/lvm_test    # Should now show ~3GB
```

Verify the test file is intact:

```bash
cat /mnt/lvm_test/lvm_test.txt
```

**Question:** What command would you use instead of `resize2fs` if the filesystem on the logical volume were xfs?

### Task 4.5 — Explore LVM Paths

```bash
ls -la /dev/labvg/
ls -la /dev/mapper/
```

Note that both `/dev/labvg/lablv` and `/dev/mapper/labvg-lablv` point to the same device.

---

## Part 5 — Swap Space (10 minutes)

### Task 5.1 — Check Current Swap

```bash
free -h
swapon --show
cat /proc/swaps
```

### Task 5.2 — Create a Swap File

```bash
# Create a 512MB swap file
sudo fallocate -l 512M /swapfile
sudo chmod 600 /swapfile

# Verify permissions (must be 600)
ls -la /swapfile

# Format as swap
sudo mkswap /swapfile

# Activate
sudo swapon /swapfile

# Verify
swapon --show
free -h
```

### Task 5.3 — Make Swap Persistent

```bash
sudo nano /etc/fstab
```

Add this line:

```
/swapfile  none  swap  sw  0  0
```

Save and exit.

### Task 5.4 — Test Deactivation

```bash
sudo swapoff /swapfile
swapon --show
free -h
```

Note the change in available swap. Re-activate:

```bash
sudo swapon /swapfile
```

---

## Part 6 — Filesystem Health (10 minutes)

### Task 6.1 — fsck on ext4

```bash
# Unmount the ext4 partition before running fsck
sudo umount /mnt/ext4part

# Run fsck
sudo fsck /dev/sdb1
```

Expected output: The filesystem should be "clean" (no errors).

```bash
# Force a check even on a clean filesystem
sudo fsck -f /dev/sdb1
```

Remount after fsck:

```bash
sudo mount /mnt/ext4part
```

### Task 6.2 — xfs_repair

```bash
sudo umount /mnt/xfspart

# xfs uses xfs_repair, not fsck
sudo xfs_repair -n /dev/sdb2    # -n = dry run (read-only check)

sudo mount /mnt/xfspart
```

### Task 6.3 — SMART Disk Health

```bash
# Check health of the primary disk
sudo smartctl -H /dev/sda

# View SMART attributes
sudo smartctl -a /dev/sda | head -50
```

Look for the following attributes and record their values:

- `Reallocated_Sector_Ct` (ID 5)
- `Current_Pending_Sector` (ID 197)
- `Offline_Uncorrectable` (ID 198)

**Question:** If `Reallocated_Sector_Ct` is 5 and slowly increasing over several months, what action should you take?

---

## Part 7 — Space Analysis (5 minutes)

```bash
# View all filesystems
df -h

# Find the largest directories under /var
du -sh /var/* 2>/dev/null | sort -hr | head -10

# Find largest individual log files
find /var/log -type f -size +1M 2>/dev/null | xargs du -sh | sort -hr
```

---

## Challenge Tasks (Optional)

### Challenge 1 — fstab with nofail

Modify your fstab entries for the ext4 and xfs partitions to include the `nofail` option. Research what this option does and why it is recommended for non-root, non-critical filesystems in cloud and VM environments. Add your explanation to the submission document.

### Challenge 2 — LVM Snapshot

Research the `lvcreate -s` (snapshot) option for LVM. Create a snapshot of `lablv`, mount it read-only, and verify that it contains the same data as the original. Then remove the snapshot.

### Challenge 3 — Custom SMART Monitoring

Write a shell script that:

1. Runs `smartctl -H` on each disk listed by `lsblk -d`
2. Writes the health status to a log file with a timestamp
3. Exits with a non-zero status code if any disk reports "FAILED"

---

## Cleanup (Optional)

To remove the lab configuration from /etc/fstab before turning in the VM, restore the backup:

```bash
sudo cp /etc/fstab.backup /etc/fstab
sudo umount /mnt/ext4part /mnt/xfspart /mnt/lvm_test
sudo swapoff /swapfile
sudo rm /swapfile
```

---

## Submission Requirements

Submit a text file named `lab06_answers.txt` containing:

1. Output of `lsblk /dev/sdb` after partitioning (Task 2.1)
2. Answer to Task 2.2 question about default fdisk partition type
3. Output of `df -h` showing both ext4 and xfs mounts (Task 3.2)
4. Output of `pvs`, `vgs`, `lvs` after LVM creation (Task 4.3)
5. Output of `df -h /mnt/lvm_test` before and after resize2fs (Task 4.4)
6. Answer to Task 4.4 question about xfs resize command
7. SMART attribute values from Task 6.3
8. Answer to Task 6.3 question about reallocated sectors
9. Answer to Task 3.3 question about fstab errors and nofail

---

## Grading Rubric

| Section | Points |
|---|---|
| Part 1 — Disk exploration | 5 |
| Part 2 — Partitioning | 15 |
| Part 3 — Filesystem and fstab | 20 |
| Part 4 — LVM creation and extension | 25 |
| Part 5 — Swap | 15 |
| Part 6 — fsck and SMART | 10 |
| Written answers | 10 |
| **Total** | **100** |

Challenge tasks are extra credit (up to 15 points).

---

*End of Module 06 Lab*
