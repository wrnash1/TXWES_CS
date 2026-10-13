# Discussion Forum: Module 08 - Storage Management: Partitions, LVM, RAID

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Points:** 10
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

### Instructions

Choose one of the three scenarios below. Write an initial post of 175 to 225 words that addresses
all three sub-questions for your chosen scenario. After posting, respond to at least two classmates
who chose different scenarios. Each response should be at least 75 words and add substantive
technical content.

---

### Scenario A - Emergency Disk Space Expansion

A production database server has a /var/lib/mysql filesystem that is 95% full. The database
will stop accepting writes when it reaches 100%. The LVM volume group vg_db has 50 GB of free
space available. A new 500 GB disk has also been allocated by the SAN team and is visible as
/dev/sdc. The database cannot be taken offline during business hours.

1. Write the exact command sequence to first use the existing free space in vg_db to extend
   the lv_mysql logical volume by 40 GB and resize the filesystem online. Then write the
   sequence to add /dev/sdc as an additional physical volume, extend the VG, and perform
   another LV and filesystem expansion. Explain which step requires resize2fs versus xfs_growfs
   and how you would determine which applies to this system.
2. The database team asks you to take a consistent snapshot before expanding so they can roll
   back if there is a problem. Write the LVM snapshot creation command, explain how large the
   snapshot volume should be, and describe the process to mount and use the snapshot for
   verification.
3. After the expansion, the operations team wants monitoring to alert when any filesystem
   reaches 85% capacity. Write a short bash script (using df and a while read loop) that
   checks all mounted filesystems and prints an alert for any that exceed the threshold.

---

### Scenario B - RAID Selection for New File Server

Your company is deploying a new file server. The storage team has allocated 6 identical 4 TB
disks. The server will host home directories for 200 users and must remain online if a single
disk fails. The operations team has three competing proposals: RAID 5, RAID 6, and RAID 10.

1. For each of the three proposed RAID levels, calculate: the total usable capacity with 6
   disks of 4 TB each, the number of simultaneous disk failures the array can tolerate, and
   the read/write performance characteristics. Show your calculations for usable capacity.
2. The operations manager asks: "If a disk fails and we do not notice for 3 days, and then a
   second disk fails during the rebuild, which RAID levels lose data?" Answer this question for
   each of the three proposals and use it to make a recommendation for the user home directory
   workload.
3. Write the mdadm command to create your recommended array using all six disks as /dev/sd{b,c,d,e,f,g}
   and the two commands needed to ensure the RAID configuration persists across reboots.

---

### Scenario C - Boot Failure from fstab Error

A junior administrator edits /etc/fstab on a production server to add a new data disk. They
use the device name /dev/sdb1 instead of the UUID. After rebooting for an unrelated kernel
update, the server drops to an emergency recovery shell. Investigation shows that a second
disk was added to the server by the hardware team during the maintenance window, changing the
device enumeration so that what was /dev/sdb is now /dev/sdc.

1. Explain in technical terms exactly why the device name change caused the boot failure and
   what the kernel does when an fstab entry cannot be mounted. Describe what the emergency
   shell prompt indicates about the system's mount state.
2. Write the exact commands an administrator would run from the emergency recovery shell to
   identify the correct UUID of the data partition, fix the /etc/fstab entry to use that UUID,
   and complete the boot. The administrator has root access from the recovery shell.
3. Write the correct fstab line for a data partition with UUID 7f8g9h0i-1j2k-3l4m-5n6o-7p8q9r0s1t2u
   that should mount at /data as ext4 with default options and an nofail flag (so the system
   boots even if the disk is unavailable). Explain what the nofail option does and when it is
   appropriate to use it.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 08 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Storage failures are not if events — they are when events. The question is whether your storage
architecture gives you time to respond. A single-disk setup with no RAID means data loss at
the first disk failure. RAID without monitoring means eventual catastrophic failure when a
second disk fails in a degraded array that nobody noticed. LVM without snapshots means no
rollback when an expansion goes wrong. The tools in this module are all about building margins:
space margins, time margins, and recovery margins. The administrator who plans for failure is
the one who does not lose data when it happens.
