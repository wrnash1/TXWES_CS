# Lab: Module 13 — Storage and Logical Volume Management

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Lab Overview

**Estimated Time:** 75–90 minutes

**Environment:** Linux VM with at least one additional unformatted disk attached (10–20 GB recommended). On VirtualBox or VMware, add a second virtual disk before starting.

**Objectives:**

- Create and manage LVM physical volumes, volume groups, and logical volumes
- Create ext4 and XFS filesystems
- Configure persistent mounts via `/etc/fstab`
- Extend a logical volume and filesystem online
- Analyze disk usage with `df` and `du`
- Interpret RAID level characteristics

---

### Lab Environment Setup

**Verify your additional disk is visible:**

```bash
lsblk
fdisk -l
```

You should see your primary disk (likely `/dev/sda`) and the additional disk (likely `/dev/sdb`). If no second disk is visible, add one in your hypervisor settings before proceeding.

Record the device name of your additional disk: `/dev/___`

**Important:** Do NOT run these commands on `/dev/sda` (your primary/boot disk). Always verify you are targeting the correct device.

---

### Part 1: Physical Volume and Volume Group Creation

**Task 1.1 — Initialize a Physical Volume**

```bash
sudo pvcreate /dev/<your-disk>
pvs
pvdisplay /dev/<your-disk>
```

From `pvdisplay` output, record:

- PV Size
- PE Size (Physical Extent size)
- Total PE count
- Free PE count

**Task 1.2 — Create a Volume Group**

```bash
sudo vgcreate labvg /dev/<your-disk>
vgs
vgdisplay labvg
```

Record:

- VG Size
- Free PE / Size

**Task 1.3 — Create Logical Volumes**

Create two logical volumes from the VG:

```bash
sudo lvcreate -L 2G -n lv_data labvg
sudo lvcreate -L 1G -n lv_logs labvg
lvs
```

Verify both volumes appear with the correct sizes.

**Task 1.4 — View LVM Device Paths**

```bash
ls -la /dev/labvg/
ls -la /dev/mapper/ | grep labvg
```

Record both device paths for `lv_data`. Confirm they are symlinks to the same device.

---

### Part 2: Filesystem Creation

**Task 2.1 — Create an ext4 Filesystem**

```bash
sudo mkfs.ext4 -L "lab-data" /dev/labvg/lv_data
```

Record the output values:

- Block size
- Number of inodes
- UUID assigned

**Task 2.2 — Create an XFS Filesystem**

```bash
sudo mkfs.xfs /dev/labvg/lv_logs
```

Record the filesystem UUID.

**Task 2.3 — Confirm Filesystem Types**

```bash
blkid /dev/labvg/lv_data
blkid /dev/labvg/lv_logs
lsblk -f
```

Confirm the TYPE field shows `ext4` and `xfs` respectively.

---

### Part 3: Mounting Filesystems

**Task 3.1 — Create Mount Points**

```bash
sudo mkdir -p /mnt/lab-data /mnt/lab-logs
```

**Task 3.2 — Mount Manually**

```bash
sudo mount /dev/labvg/lv_data /mnt/lab-data
sudo mount /dev/labvg/lv_logs /mnt/lab-logs
findmnt /mnt/lab-data
findmnt /mnt/lab-logs
df -h /mnt/lab-data /mnt/lab-logs
```

Record the available space on each mounted volume.

**Task 3.3 — Create Test Files**

```bash
echo "Data volume test" | sudo tee /mnt/lab-data/testfile.txt
echo "Logs volume test" | sudo tee /mnt/lab-logs/testfile.txt
ls -la /mnt/lab-data/ /mnt/lab-logs/
```

**Task 3.4 — Unmount and Remount**

```bash
sudo umount /mnt/lab-data
findmnt /mnt/lab-data
```

Confirm it is no longer mounted. Remount:

```bash
sudo mount /dev/labvg/lv_data /mnt/lab-data
cat /mnt/lab-data/testfile.txt
```

Confirm the file persists after remount.

---

### Part 4: Persistent /etc/fstab Configuration

**Task 4.1 — Get the UUIDs**

```bash
blkid /dev/labvg/lv_data
blkid /dev/labvg/lv_logs
```

Copy the UUID values (without quotes) for use in the next step.

**Task 4.2 — Backup fstab**

Always back up fstab before editing:

```bash
sudo cp /etc/fstab /etc/fstab.backup
```

**Task 4.3 — Add fstab Entries**

Unmount the volumes first:

```bash
sudo umount /mnt/lab-data /mnt/lab-logs
```

Open fstab for editing:

```bash
sudo nano /etc/fstab
```

Add these lines at the end (replace UUID values with yours):

```
UUID=<lv_data-uuid>   /mnt/lab-data  ext4  defaults,noatime  0  2
UUID=<lv_logs-uuid>   /mnt/lab-logs  xfs   defaults           0  2
```

Save and exit.

**Task 4.4 — Test the fstab Entries**

```bash
sudo mount -a
findmnt /mnt/lab-data
findmnt /mnt/lab-logs
```

If both volumes mount successfully, your fstab entries are correct. If `mount -a` fails, there is a syntax error — fix it before continuing.

Verify files still exist:

```bash
cat /mnt/lab-data/testfile.txt
cat /mnt/lab-logs/testfile.txt
```

---

### Part 5: Extending a Logical Volume Online

**Task 5.1 — Check Current Size**

```bash
df -h /mnt/lab-data
lvdisplay /dev/labvg/lv_data
```

Record current size.

**Task 5.2 — Extend the Logical Volume and Filesystem**

Extend the LV by 500 MB and resize the filesystem in one command:

```bash
sudo lvextend -L +500M -r /dev/labvg/lv_data
```

**Task 5.3 — Verify the Extension**

```bash
df -h /mnt/lab-data
lvdisplay /dev/labvg/lv_data
```

Confirm that both the LV size and the mounted filesystem size increased. The filesystem must be extended and accessible — no remounting required.

**Task 5.4 — Verify Data Integrity**

```bash
cat /mnt/lab-data/testfile.txt
```

The file must still be readable. Extension operations must not damage existing data.

---

### Part 6: Disk Usage Analysis

**Task 6.1 — df Analysis**

```bash
df -hT
df -i
```

From the output:

- What filesystem is `/` mounted on?
- What is the inode usage percentage for each filesystem?
- Which mounted filesystem has the most free space?

**Task 6.2 — du Analysis**

Analyze the `/var` directory:

```bash
sudo du -h --max-depth=1 /var 2>/dev/null | sort -rh | head -10
```

- Which subdirectory of `/var` uses the most space?

Analyze `/var/log` specifically:

```bash
sudo du -sh /var/log/*  2>/dev/null | sort -rh | head -5
```

**Task 6.3 — Find Large Files**

```bash
sudo find /var -type f -size +10M -exec ls -lh {} \; 2>/dev/null
```

List any files found over 10 MB.

---

### Part 7: RAID Level Analysis (Written Exercise)

No commands required for this section — answer based on reading guide knowledge.

**Scenario:**

A server has four identical 4 TB drives available. Calculate the following:

| RAID Level | Usable Capacity | Fault Tolerance | Write Performance | Best Use Case |
|-----------|----------------|-----------------|-------------------|--------------|
| RAID 0 | | | | |
| RAID 1 | | | | |
| RAID 5 | | | | |
| RAID 6 | | | | |
| RAID 10 | | | | |

Fill in all cells. For "Fault Tolerance," specify how many drives can fail simultaneously without data loss.

---

### Part 8: Lab Cleanup

Remove fstab entries and clean up:

```bash
# Unmount
sudo umount /mnt/lab-data /mnt/lab-logs

# Remove fstab entries (edit and delete the lines you added)
sudo nano /etc/fstab

# Remove logical volumes
sudo lvremove /dev/labvg/lv_data
sudo lvremove /dev/labvg/lv_logs

# Remove volume group
sudo vgremove labvg

# Remove physical volume
sudo pvremove /dev/<your-disk>

# Verify cleanup
pvs; vgs; lvs

# Remove mount points
sudo rmdir /mnt/lab-data /mnt/lab-logs
```

---

### Lab Submission Requirements

Submit a lab report in PDF format containing:

1. Completed RAID analysis table (Part 7)
2. Recorded values from each verification step
3. Screenshot or pasted terminal output for tasks 2.3, 4.4, and 5.3
4. Brief paragraph (3–5 sentences) explaining why `lvextend -r` is preferred over running `lvextend` and `resize2fs` separately
5. Brief paragraph explaining why UUIDs are preferred over device paths in `/etc/fstab`

---

### Grading Rubric

| Section | Points |
|---------|--------|
| Part 1: PV and VG creation | 15 |
| Part 2: Filesystem creation | 10 |
| Part 3: Mounting and unmounting | 15 |
| Part 4: /etc/fstab configuration | 20 |
| Part 5: Online LV extension | 20 |
| Part 6: Disk usage analysis | 10 |
| Part 7: RAID analysis table | 5 |
| Written explanations | 5 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: LVM Thin Provisioning

Implement LVM thin provisioning to create a pool that can be over-committed and observe how thin volumes behave differently from thick volumes.

1. On the VM's second disk (ensure `/dev/sdb` has free space or an available partition), create a new volume group `thinvg`: `sudo pvcreate /dev/sdbX && sudo vgcreate thinvg /dev/sdbX`. Create a thin pool named `thinpool` consuming all free space: `sudo lvcreate -l 100%FREE --thinpool thinpool thinvg`. Verify with `sudo lvs thinvg` and note the `ThinPool` attribute in the `Attr` column.
2. Create two thin logical volumes of 5 GB each from the pool, even if the pool itself is smaller than 10 GB total: `sudo lvcreate -V 5G --thin -n thin1 thinvg/thinpool && sudo lvcreate -V 5G --thin -n thin2 thinvg/thinpool`. Format and mount them: `sudo mkfs.ext4 /dev/thinvg/thin1 && sudo mkdir -p /mnt/thin1 && sudo mount /dev/thinvg/thin1 /mnt/thin1`. Run `df -h /mnt/thin1` — it should report 5 GB despite the pool being smaller.
3. Write data to observe pool consumption: `sudo dd if=/dev/urandom of=/mnt/thin1/testdata bs=1M count=200`. After writing, run `sudo lvs thinvg` and observe the `Data%` column of the pool increasing. Calculate: at what fill percentage would the pool become full? What happens to mounted thin volumes when the pool fills completely?
4. Create an LVM snapshot of `thin1` (thin snapshots have different syntax): `sudo lvcreate -s --name thin1_snap thinvg/thin1`. Write more data to the original: `sudo dd if=/dev/urandom of=/mnt/thin1/postsnap bs=1M count=50`. Mount the snapshot read-only and verify it does NOT contain `postsnap`: `sudo mkdir /mnt/snap && sudo mount -o ro /dev/thinvg/thin1_snap /mnt/snap && ls /mnt/snap`. Clean up: `sudo umount /mnt/snap && sudo lvremove thinvg/thin1_snap`.

### Challenge 2: Automated Storage Health Monitor

Write a comprehensive storage health monitoring script that combines LVM status, filesystem usage, SMART data, and RAID status into a single report.

1. Create `~/storage_health.sh`. The script should collect four categories of data: (1) LVM status — run `sudo pvs`, `sudo vgs`, `sudo lvs` and flag any VG with less than 10% free space; (2) filesystem usage — parse `df -h --output=target,pcent` and flag any filesystem over 80% full; (3) RAID status — check `cat /proc/mdstat 2>/dev/null` and flag any array not showing `[UU]` (active healthy disks) in its status line; (4) SMART health — loop over disks from `lsblk -d -o NAME -n` and run `sudo smartctl -H /dev/$DISK 2>/dev/null | grep "SMART overall"`.
2. Implement output formatting: print a section header for each category, print GREEN/PASS for healthy items (use `echo -e "\e[32mPASS\e[0m"`) and RED/FAIL for problems (use `echo -e "\e[31mFAIL\e[0m"`). Add a final summary line showing total checks run and total failures found.
3. Add a `--quiet` flag: when passed, suppress all PASS output and show only FAILures and the summary. Implement this by checking `[ "$1" = "--quiet" ]` and conditionally calling a `verbose_pass()` function that only prints if not in quiet mode.
4. Schedule the script to run daily at 6 AM: add a cron entry with `crontab -e`: `0 6 * * * /bin/bash ~/storage_health.sh --quiet >> /var/log/storage_health.log 2>&1`. Verify the crontab entry and simulate a run: `bash ~/storage_health.sh --quiet`.

### Reflection Questions

1. LVM allows logical volumes to be extended online without unmounting. However, shrinking an ext4 logical volume requires the filesystem to be unmounted first. Describe what would physically happen to a mounted ext4 filesystem's data structures if `lvreduce` were run without first shrinking the filesystem — at which layer does the corruption first occur, and why does the filesystem not detect it until the next mount?

2. A common recommendation is to use RAID 10 for database servers rather than RAID 5, even though RAID 10 provides only 50% space efficiency compared to RAID 5's (N-1)/N efficiency. Explain the specific I/O characteristics of database workloads that make RAID 5's parity-calculation overhead problematic, and describe the concrete performance scenario where this difference would be measurable in production.
