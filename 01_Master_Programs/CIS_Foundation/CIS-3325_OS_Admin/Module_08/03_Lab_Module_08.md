# Lab 08: Storage Management - Partitions, LVM, and RAID

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 90-120 minutes

---

### Overview

In this lab you will add virtual disks to your Ubuntu Server VM, create partitions with fdisk,
format filesystems, configure persistent mounts in /etc/fstab, build an LVM stack from scratch,
extend a logical volume and resize the filesystem, and examine RAID concepts.

**What you will practice:**

- lsblk and blkid for disk inspection
- fdisk for MBR partition creation
- mkfs.ext4 and mkfs.xfs for filesystem creation
- /etc/fstab UUID-based persistent mounting
- pvcreate, vgcreate, lvcreate for LVM setup
- lvextend and resize2fs for online LVM expansion
- mdadm for RAID array creation and monitoring

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running
- You are logged in as labadmin
- VirtualBox: Add two additional virtual hard disks (5 GB each) before starting the lab
  - Settings > Storage > Add Hard Disk > Create Disk > VDI > Fixed > 5 GB
  - Add a second 5 GB disk using the same process
- After adding disks, boot the VM and verify they appear as /dev/sdb and /dev/sdc with lsblk

---

### Part 1 - Disk and Partition Inspection

**Step 1.1 - List all block devices**

```bash
lsblk
```

Record all device names, sizes, and mount points. The new disks should appear as sdb and sdc.

```bash
lsblk -f
```

Note the FSTYPE and UUID columns. The new disks show blank FSTYPE because they are unformatted.

**Step 1.2 - Inspect the existing partition table**

```bash
sudo fdisk -l /dev/sda
```

Note the "Disklabel type" line. Record whether it shows dos (MBR) or gpt (GPT). Record the
partition count and sizes.

**Step 1.3 - View block device identifiers**

```bash
sudo blkid
```

Lists all devices with their UUIDs and filesystem types. The new disks (sdb, sdc) will not
appear yet because they have no filesystem.

---

### Part 2 - Partitioning and Filesystem Creation

**Step 2.1 - Create a partition on sdb**

```bash
sudo fdisk /dev/sdb
```

In fdisk, run these commands in order:
- p (print current table — should be empty)
- n (new partition)
- p (primary)
- 1 (partition number 1)
- Enter (accept default first sector)
- +3G (set size to 3 GB)
- p (print to confirm)
- w (write and exit)

**Step 2.2 - Notify the kernel**

```bash
sudo partprobe /dev/sdb
lsblk /dev/sdb
```

The partition sdb1 should now appear.

**Step 2.3 - Format the partition with ext4**

```bash
sudo mkfs.ext4 -L "lab08data" /dev/sdb1
```

Note the UUID output in the mkfs output. Record it.

**Step 2.4 - Verify the filesystem**

```bash
sudo blkid /dev/sdb1
```

The UUID and LABEL should now appear.

---

### Part 3 - Mounting and /etc/fstab

**Step 3.1 - Create a mount point and mount**

```bash
sudo mkdir /mnt/lab08data
sudo mount /dev/sdb1 /mnt/lab08data
df -h /mnt/lab08data
```

**Step 3.2 - Verify the mount**

```bash
mount | grep lab08data
```

**Step 3.3 - Write a test file**

```bash
echo "Lab 08 test data" | sudo tee /mnt/lab08data/testfile.txt
cat /mnt/lab08data/testfile.txt
```

**Step 3.4 - Unmount and remount**

```bash
sudo umount /mnt/lab08data
ls /mnt/lab08data
```

The mount point is now empty. The filesystem data is safe on the disk.

**Step 3.5 - Add to /etc/fstab for persistent mounting**

Get the UUID:

```bash
UUID=$(sudo blkid -s UUID -o value /dev/sdb1)
echo $UUID
```

Make a backup of fstab before editing:

```bash
sudo cp /etc/fstab /etc/fstab.bak
```

Add the fstab entry:

```bash
echo "UUID=$UUID  /mnt/lab08data  ext4  defaults  0  2" | sudo tee -a /etc/fstab
```

Test without rebooting:

```bash
sudo mount -a
df -h /mnt/lab08data
```

Verify the test file is still present:

```bash
cat /mnt/lab08data/testfile.txt
```

---

### Part 4 - LVM

**Step 4.1 - Initialize a physical volume**

```bash
sudo pvcreate /dev/sdc
sudo pvs
```

sdc is now a physical volume. Note the PSize and PFree values.

**Step 4.2 - Create a volume group**

```bash
sudo vgcreate vg_lab08 /dev/sdc
sudo vgs
```

Note VFree — this is the space available for logical volumes.

**Step 4.3 - Create a logical volume**

```bash
sudo lvcreate -L 2G -n lv_app vg_lab08
sudo lvs
```

The logical volume /dev/vg_lab08/lv_app is now available.

**Step 4.4 - Create a filesystem on the logical volume**

```bash
sudo mkfs.ext4 /dev/vg_lab08/lv_app
sudo mkdir /app
sudo mount /dev/vg_lab08/lv_app /app
df -h /app
```

**Step 4.5 - Write data to the logical volume**

```bash
echo "Application data" | sudo tee /app/app_data.txt
```

**Step 4.6 - Extend the logical volume**

```bash
sudo lvextend -L +1G /dev/vg_lab08/lv_app
sudo lvs
```

Note that lv_app is now 3 GB, but df -h /app still shows 2 GB. The filesystem has not yet
been resized.

**Step 4.7 - Resize the filesystem**

```bash
sudo resize2fs /dev/vg_lab08/lv_app
df -h /app
```

Now df -h /app shows approximately 3 GB. The data is intact:

```bash
cat /app/app_data.txt
```

**Step 4.8 - Add a second logical volume**

```bash
sudo lvcreate -L 1G -n lv_logs vg_lab08
sudo mkfs.ext4 /dev/vg_lab08/lv_logs
sudo mkdir /applogs
sudo mount /dev/vg_lab08/lv_logs /applogs
```

**Step 4.9 - Show the complete LVM view**

```bash
sudo pvdisplay
sudo vgdisplay
sudo lvdisplay
```

---

### Part 5 - RAID Concepts (Observation and Configuration)

**Step 5.1 - Install mdadm**

```bash
sudo apt install -y mdadm
```

**Step 5.2 - Review /proc/mdstat**

```bash
cat /proc/mdstat
```

On a system with no RAID arrays configured, this shows: "Personalities:" with no array entries.

**Step 5.3 - Examine RAID level calculations**

Answer the following based on the RAID reference table in the Reading Guide:

For a RAID 5 array with 4 disks of 500 GB each:
- How many disks can fail before data loss?
- What is the usable storage capacity?

For a RAID 10 array with 4 disks of 1 TB each:
- How many disks can fail before data loss?
- What is the usable storage capacity?

**Step 5.4 - (Optional, if three disks available) Create a RAID 1 array**

If VirtualBox allows adding a third extra disk (/dev/sdd), create a RAID 1 mirror for
practice. Skip this step and document the RAID concepts if a third disk is not available.

```bash
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdd /dev/sde
cat /proc/mdstat
sudo mdadm --detail /dev/md0
```

---

### Part 6 - Analysis Questions

**Question 1:** An administrator adds a 4 TB NVMe disk to a server with an older BIOS. They
run fdisk on the new disk and see "Disklabel type: dos." Explain why this is a problem for a
4 TB disk and what the administrator should do instead. What command creates a GPT partition
table on the disk?

**Question 2:** After successfully running lvextend -L +20G /dev/vg_prod/lv_database, the
administrator runs df -h and sees the filesystem size has not changed. Write the exact
command needed to complete the operation for both ext4 and XFS filesystems. Explain in one
sentence why this two-step process exists.

**Question 3:** You are configuring /etc/fstab to mount a data partition. A colleague suggests
using /dev/sdb1 as the device identifier. Explain the specific failure scenario that makes
this dangerous and write the correct entry using UUID for a partition with UUID
b1c2d3e4-f5a6-7890-bcde-f12345678901 that should mount at /data with ext4, defaults options,
and checked at boot.

**Question 4:** Compare RAID 5 and RAID 10 for a database server workload that requires
high write performance and can afford to use 6 disks. Which RAID level is more appropriate
for this workload? Justify your answer using usable capacity, fault tolerance, and write
performance characteristics.

**Question 5:** An administrator monitors a production RAID 5 array and sees [UU_] in
/proc/mdstat. The array has 3 disks total. Describe the current state of the array: is data
at risk? Can the array be read and written? Write the exact mdadm command sequence to replace
the failed disk with /dev/sdd and initiate a rebuild. How would you monitor the rebuild progress?

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.2 showing fdisk -l output for the main system disk
2. Screenshot of Part 2, Step 2.3 showing mkfs.ext4 output with UUID
3. Screenshot of Part 3, Step 3.5 showing the fstab entry added and mount -a successful
4. Screenshot of Part 4, Step 4.6 showing lvextend output and df still showing old size
5. Screenshot of Part 4, Step 4.7 showing resize2fs output and df showing new size
6. Screenshot of Part 4, Step 4.9 showing lvdisplay output for both logical volumes
7. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| fdisk -l system disk screenshot | 10 |
| mkfs.ext4 with UUID screenshot | 10 |
| fstab entry and mount -a screenshot | 10 |
| lvextend before resize screenshot | 10 |
| resize2fs and df showing new size screenshot | 10 |
| lvdisplay both LVs screenshot | 10 |
| Analysis Question 1 (MBR vs GPT) | 5 |
| Analysis Question 2 (lvextend + resize2fs) | 5 |
| Analysis Question 3 (UUID in fstab) | 5 |
| Analysis Question 4 (RAID comparison) | 10 |
| Analysis Question 5 (RAID recovery) | 15 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

**Challenge Step 1 — LVM snapshot, rollback, and thin provisioning exploration**

Create a logical volume, populate it with test data, take a snapshot, modify the data, and
then roll back to the snapshot state:

```bash
sudo lvcreate -L 500M -n lv_snap_demo vg_lab
sudo mkfs.ext4 /dev/vg_lab/lv_snap_demo
sudo mkdir -p /mnt/snap_demo
sudo mount /dev/vg_lab/lv_snap_demo /mnt/snap_demo

sudo bash -c 'for i in {1..5}; do echo "original file $i" > /mnt/snap_demo/file_$i.txt; done'
ls /mnt/snap_demo/
cat /mnt/snap_demo/file_1.txt

sudo lvcreate -s -n lv_snap_demo_snap -L 200M /dev/vg_lab/lv_snap_demo
sudo lvs
```

Modify the original volume to simulate data changes:

```bash
sudo bash -c 'echo "MODIFIED" > /mnt/snap_demo/file_1.txt'
sudo bash -c 'echo "new unwanted file" > /mnt/snap_demo/file_new.txt'
cat /mnt/snap_demo/file_1.txt
ls /mnt/snap_demo/
```

Mount the snapshot read-only to verify the original state is preserved:

```bash
sudo mkdir -p /mnt/snap_verify
sudo mount -o ro /dev/vg_lab/lv_snap_demo_snap /mnt/snap_verify
cat /mnt/snap_verify/file_1.txt
ls /mnt/snap_verify/
sudo umount /mnt/snap_verify
```

Perform a merge (rollback) to restore the original volume from the snapshot:

```bash
sudo umount /mnt/snap_demo
sudo lvconvert --merge /dev/vg_lab/lv_snap_demo_snap
sudo lvs
sudo mount /dev/vg_lab/lv_snap_demo /mnt/snap_demo
cat /mnt/snap_demo/file_1.txt
ls /mnt/snap_demo/
```

Document whether file_1.txt shows "original file 1" and whether file_new.txt is absent after
the merge. Explain in two sentences why LVM snapshots are useful for pre-upgrade checkpoints
and why snapshot size must be monitored — what happens if a snapshot runs out of space before
the merge is performed.

**Challenge Step 2 — Disk performance benchmarking and I/O scheduler inspection**

Measure raw disk throughput and I/O latency on your VM disks and compare different I/O
schedulers:

```bash
lsblk -d -o NAME,ROTA,SCHED
cat /sys/block/sdb/queue/scheduler

ls /sys/block/sdb/queue/
cat /sys/block/sdb/queue/rotational
cat /sys/block/sdb/queue/nr_requests
```

Run a sequential write benchmark using dd to measure raw throughput:

```bash
sudo dd if=/dev/zero of=/dev/sdb bs=1M count=512 oflag=direct 2>&1
```

Run a sequential read benchmark:

```bash
sudo dd if=/dev/sdb of=/dev/null bs=1M count=512 iflag=direct 2>&1
```

If hdparm is available, run an additional read benchmark:

```bash
sudo apt install -y hdparm 2>/dev/null
sudo hdparm -tT /dev/sdb
```

Now inspect whether changing the I/O scheduler affects throughput on a virtual disk:

```bash
cat /sys/block/sdb/queue/scheduler
echo mq-deadline | sudo tee /sys/block/sdb/queue/scheduler
cat /sys/block/sdb/queue/scheduler
sudo dd if=/dev/zero of=/dev/sdb bs=1M count=512 oflag=direct 2>&1
echo none | sudo tee /sys/block/sdb/queue/scheduler
sudo dd if=/dev/zero of=/dev/sdb bs=1M count=512 oflag=direct 2>&1
```

Document the throughput in MB/s for each scheduler. Explain in two sentences why the I/O
scheduler matters more on spinning hard disks than on SSDs, and why virtual machine disks
often show less scheduler variation than physical hardware.

**Challenge Step 3 — RAID array monitoring, scrubbing, and failure simulation**

Build a RAID 5 array from loop devices (no additional physical disks required) and simulate
a drive failure and recovery:

```bash
for i in 1 2 3 4; do
    sudo dd if=/dev/zero of=/tmp/raid_disk_$i.img bs=1M count=256
    sudo losetup /dev/loop$i /tmp/raid_disk_$i.img
done
sudo losetup -l | grep raid

sudo mdadm --create /dev/md10 --level=5 --raid-devices=3 \
    /dev/loop1 /dev/loop2 /dev/loop3 --spare-devices=1 \
    --spare /dev/loop4 --run

watch -n 2 cat /proc/mdstat
```

Wait for the initial sync to complete (watch until [===] shows 100%), then inspect the array:

```bash
sudo mdadm --detail /dev/md10
cat /proc/mdstat
```

Create a filesystem and test data:

```bash
sudo mkfs.ext4 /dev/md10
sudo mkdir /mnt/raid10_test
sudo mount /dev/md10 /mnt/raid10_test
sudo bash -c 'for i in {1..10}; do echo "raid test data $i" > /mnt/raid10_test/data_$i.txt; done'
ls /mnt/raid10_test/
```

Simulate a drive failure by marking loop1 as failed:

```bash
sudo mdadm --fail /dev/md10 /dev/loop1
cat /proc/mdstat
sudo mdadm --detail /dev/md10
ls /mnt/raid10_test/
cat /mnt/raid10_test/data_1.txt
```

Observe that the hot spare (loop4) automatically begins rebuilding. Then remove the failed
device and confirm final state:

```bash
sudo mdadm --remove /dev/md10 /dev/loop1
sudo mdadm --detail /dev/md10
cat /proc/mdstat
```

Trigger a manual scrub and check for errors:

```bash
echo check | sudo tee /sys/block/md10/md/sync_action
cat /sys/block/md10/md/sync_action
cat /proc/mdstat
sudo mdadm --detail /dev/md10 | grep "Checksum Errors\|Mismatch"
```

Clean up after the lab:

```bash
sudo umount /mnt/raid10_test
sudo mdadm --stop /dev/md10
for i in 1 2 3 4; do sudo losetup -d /dev/loop$i; done
sudo rm /tmp/raid_disk_*.img
```

Document: (1) the array state shown in /proc/mdstat immediately after marking loop1 as failed,
(2) whether the hot spare started rebuilding automatically, and (3) the final state after the
rebuild completed. Explain in three sentences why RAID is not a substitute for backups, why
scheduled scrubs are important for data integrity, and what "RAID write hole" means for RAID 5
arrays without a write-intent bitmap.
