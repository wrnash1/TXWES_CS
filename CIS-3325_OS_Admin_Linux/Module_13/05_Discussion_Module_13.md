# Discussion: Module 13 — Storage and Logical Volume Management

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This discussion is worth 50 points. Post an original response AND reply substantively to at least two classmates.

**Due Date:** By end of day Sunday of the current module week.

---

### Discussion Prompt

**Scenario:**

You are a Linux systems administrator at a mid-size e-commerce company. The development team has deployed a new application that stores product images and customer order files. Three weeks after launch, you receive this alert from your monitoring system:

```
CRITICAL: /opt/appdata is 92% full (45.3 GB / 49.2 GB used)
```

The server is a production Rocky Linux 9 system. You SSH in and begin investigating:

```bash
df -h /opt/appdata
Filesystem              Size  Used Avail Use% Mounted on
/dev/mapper/appvg-data   50G   46G  753M  99%  /opt/appdata
```

```bash
vgs
  VG    #PV #LV #SN Attr   VSize   VFree
  appvg   1   2   0 wz--n- 100.00g 45.00g
```

```bash
pvs
  PV         VG    Fmt  Attr PSize   PFree
  /dev/sdb   appvg lvm2 a--  100.00g 45.00g
```

The development team tells you the application's image storage is growing at about 2 GB per day. A new 200 GB SAN disk (`/dev/sdc`) has been provisioned and is visible on the server.

---

### Discussion Questions

Address ALL of the following in your initial post:

**Question 1 — Immediate Mitigation**

The filesystem is at 99% and the application is starting to fail writes. You have 45 GB free in the VG right now. Walk through the exact commands, in order, that you would run to immediately give the application more space. How much would you add for now, and why? Your answer should include every command from the LV extension to confirming the filesystem has grown.

**Question 2 — Long-term Expansion Plan**

The existing VG will also eventually fill up. Describe the complete procedure to integrate the new `/dev/sdc` disk into the `appvg` volume group and use that space. Write each command and explain what it does.

**Question 3 — Snapshot Before Maintenance**

The development team wants a pre-maintenance snapshot taken before you perform the expansion, so they can roll back if something goes wrong. Write the commands to create a snapshot of `/dev/appvg/data`. How large should you make the snapshot, and why? What are the limitations of LVM snapshots that the team should understand?

**Question 4 — fstab Audit**

While you are on the server, you notice the current `/etc/fstab` entry for `/opt/appdata` uses a device path instead of a UUID:

```
/dev/mapper/appvg-data  /opt/appdata  xfs  defaults  0  0
```

Evaluate this entry: are there any problems? The sixth field is `0` — is that appropriate for this filesystem? Write a corrected fstab entry and explain each change you made.

**Question 5 — RAID Recommendation**

The operations team is planning the next generation of storage infrastructure. They need to store 50 TB of active data with the following requirements: no more than 25% overhead for redundancy, survive the simultaneous failure of two drives, and use commodity 10 TB drives. Which RAID level would you recommend? Show the math on drive count and usable capacity. What are the tradeoffs of your recommendation vs. RAID 10?

---

### Reply Requirements

When responding to classmates:

- Evaluate their extension commands — did they verify the filesystem expanded (not just the LV)?
- Challenge or support their snapshot size recommendation with specific reasoning
- Provide an alternative RAID recommendation if you disagree, with supporting math

---

### Grading Rubric

| Criterion | Points |
|-----------|--------|
| Immediate mitigation: correct commands and reasoning | 12 |
| VG expansion procedure is complete and in correct order | 10 |
| Snapshot creation is correct with size justification | 10 |
| fstab audit identifies issues and provides corrected entry | 8 |
| RAID recommendation includes correct math and tradeoff analysis | 10 |
| **Total** | **50** |

---

### Instructor Notes

The most common gap in responses to Question 1 is forgetting to verify the filesystem grew. Extending the LV without the `-r` flag and not running `xfs_growfs` leaves the filesystem the same size even though the LV is larger. The disk usage alert will not clear until the filesystem actually expands.

For Question 4, note that the sixth field being `0` means fsck is skipped. For XFS, this is actually acceptable (XFS uses its own journal-based recovery and does not rely on fsck at boot), but students should explain their reasoning rather than blindly copying the field.

Strong posts will also note that snapshot performance degrades as the copy-on-write cache fills up, and that a snapshot larger than the expected change rate is critical to avoid a "broken snapshot" scenario.
