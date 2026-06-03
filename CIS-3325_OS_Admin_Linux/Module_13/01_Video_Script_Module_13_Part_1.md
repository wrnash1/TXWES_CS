# Video Script: Module 13 — Storage and Logical Volume Management (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 13: Storage and Logical Volume Management.

Storage management is one of the most consequential skills in Linux administration. Getting it right means reliable data, expandable capacity, and minimal downtime. Getting it wrong can mean data loss. The Linux+ exam tests storage extensively — LVM, filesystems, mount configuration, and RAID.

Part 1 covers the Logical Volume Manager: the architecture, the workflow for creating LVM storage, and the commands for extending volumes online. Part 2 covers filesystem creation, mounting, `/etc/fstab`, disk usage tools, and RAID concepts.

Let's start with the foundation.

---

### Section 1: Traditional Partitioning vs. LVM

**The Problem with Fixed Partitions**

Traditional disk partitioning is static. You create partitions at installation, assign sizes, and live with those decisions. When a filesystem fills up, your options are limited: resize the partition (risky, often requires unmounting), add a new disk and manually migrate data, or reorganize everything from scratch.

Logical Volume Management solves this by adding an abstraction layer between physical storage and filesystems. With LVM, you can:

- Combine multiple physical disks into a single pool of storage
- Create volumes of any size from that pool
- Extend a volume while it is mounted and in use
- Shrink volumes (carefully) when space is freed
- Take snapshots for backup or testing

**The Three Layers of LVM**

LVM has exactly three layers:

1. **Physical Volumes (PV)** — physical disks or partitions initialized for LVM use
2. **Volume Groups (VG)** — pools of storage composed of one or more physical volumes
3. **Logical Volumes (LV)** — virtual partitions carved from a volume group, where filesystems live

The analogy: physical volumes are like bricks, volume groups are like the pile of bricks, and logical volumes are like the walls you build from those bricks.

---

### Section 2: Physical Volumes

**Creating a Physical Volume**

First, verify your disk is visible:

```bash
lsblk
fdisk -l /dev/sdb
```

Initialize the disk as an LVM physical volume:

```bash
sudo pvcreate /dev/sdb
```

For a partition (as opposed to a whole disk):

```bash
sudo pvcreate /dev/sdb1
```

**Viewing Physical Volumes**

```bash
pvs
```

Short form — shows PV name, VG it belongs to, size, and free space.

```bash
pvdisplay
pvdisplay /dev/sdb
```

Detailed form — shows all PV metadata including PE (physical extent) size and count.

**Physical Extents**

LVM divides physical volumes into fixed-size chunks called **physical extents** (PE). The default PE size is 4 MB. When you create a logical volume, you allocate extents from the volume group. Understanding PE size matters when calculating exact sizes.

---

### Section 3: Volume Groups

**Creating a Volume Group**

```bash
sudo vgcreate myvg /dev/sdb
```

Create a VG named `myvg` using `/dev/sdb`.

To add multiple physical volumes to one VG at creation:

```bash
sudo vgcreate datavg /dev/sdb /dev/sdc /dev/sdd
```

**Viewing Volume Groups**

```bash
vgs
```

Shows VG name, number of PVs, number of LVs, size, and free space.

```bash
vgdisplay
vgdisplay myvg
```

**Extending a Volume Group**

When you need more capacity, add another physical disk:

```bash
sudo pvcreate /dev/sdc
sudo vgextend myvg /dev/sdc
vgs
```

The VG now has the combined capacity of both disks.

**Reducing a Volume Group**

To remove a physical volume from a VG (the PV must be empty first):

```bash
sudo pvmove /dev/sdb     # Move data off /dev/sdb
sudo vgreduce myvg /dev/sdb
```

---

### Section 4: Logical Volumes

**Creating a Logical Volume**

Create a 10 GB logical volume named `appdata` in `myvg`:

```bash
sudo lvcreate -L 10G -n appdata myvg
```

- `-L 10G` — size: 10 gigabytes
- `-n appdata` — name for the logical volume

Create using percentage of VG free space:

```bash
sudo lvcreate -l 100%FREE -n backup myvg
```

Create using a specific number of extents:

```bash
sudo lvcreate -l 2560 -n appdata myvg
```

**Viewing Logical Volumes**

```bash
lvs
lvdisplay
lvdisplay /dev/myvg/appdata
```

The logical volume device path follows this pattern:

```
/dev/<vgname>/<lvname>
/dev/mapper/<vgname>-<lvname>
```

Both paths refer to the same device.

**Extending a Logical Volume**

This is where LVM truly shines — extending a volume while it is live:

```bash
sudo lvextend -L +5G /dev/myvg/appdata
```

Add 5 GB to the existing logical volume. Or extend to a specific total size:

```bash
sudo lvextend -L 20G /dev/myvg/appdata
```

**Extend the Filesystem After lvextend**

Extending the LV only expands the block device — the filesystem must also be extended to use the new space.

For ext4:

```bash
sudo resize2fs /dev/myvg/appdata
```

For XFS (can only grow, not shrink):

```bash
sudo xfs_growfs /mount/point
```

Or combine both steps in one command:

```bash
sudo lvextend -L +5G -r /dev/myvg/appdata
```

The `-r` flag resizes the filesystem automatically after extending the LV.

**Reducing a Logical Volume**

Shrinking is more dangerous — you must shrink the filesystem BEFORE shrinking the LV:

1. Unmount the filesystem
2. Check filesystem: `sudo fsck -f /dev/myvg/appdata`
3. Shrink filesystem: `sudo resize2fs /dev/myvg/appdata 8G`
4. Shrink LV: `sudo lvreduce -L 8G /dev/myvg/appdata`
5. Remount

XFS cannot be shrunk — only extended.

---

### Section 5: LVM Snapshots

Snapshots capture the state of a logical volume at a point in time. They are used for:

- Pre-upgrade backups (snapshot before patching, roll back if needed)
- Database backups (snapshot freezes the volume while backup runs)
- Testing (snapshot, make changes, discard and revert)

**Creating a Snapshot**

```bash
sudo lvcreate -L 2G -s -n appdata_snap /dev/myvg/appdata
```

- `-s` — create a snapshot
- `-n appdata_snap` — name for the snapshot
- `2G` — the snapshot's copy-on-write cache size (not the data size)

The snapshot only stores blocks that change after creation. If the source LV changes significantly, the snapshot can run out of space.

**Mounting a Snapshot**

```bash
sudo mount -o ro /dev/myvg/appdata_snap /mnt/snap
```

Mount as read-only to examine the state at snapshot time.

**Removing a Snapshot**

```bash
sudo lvremove /dev/myvg/appdata_snap
```

---

### Section 6: Complete LVM Workflow Example

Let's put it all together with a real scenario: you've received a new 50 GB disk (`/dev/sdc`) and need to provision storage for a new application.

```bash
# Step 1: Initialize the physical volume
sudo pvcreate /dev/sdc

# Step 2: Create a volume group
sudo vgcreate appvg /dev/sdc

# Step 3: Create logical volumes
sudo lvcreate -L 20G -n appdata appvg
sudo lvcreate -L 10G -n applogs appvg

# Step 4: Create filesystems (covered in Part 2)
sudo mkfs.xfs /dev/appvg/appdata
sudo mkfs.ext4 /dev/appvg/applogs

# Step 5: Create mount points and mount (covered in Part 2)
sudo mkdir -p /opt/appdata /opt/applogs
sudo mount /dev/appvg/appdata /opt/appdata
sudo mount /dev/appvg/applogs /opt/applogs

# Step 6: Verify
pvs && vgs && lvs
df -h /opt/appdata /opt/applogs
```

---

### Summary — Part 1

In Part 1 we covered:

- The three-layer LVM architecture: Physical Volumes, Volume Groups, Logical Volumes
- Creating and managing PVs with `pvcreate`, `pvs`, `pvdisplay`
- Creating and extending VGs with `vgcreate`, `vgextend`, `vgs`
- Creating, extending, and removing LVs with `lvcreate`, `lvextend`, `lvs`
- Extending filesystems online after LV extension
- LVM snapshots for backup and testing workflows

In Part 2: filesystem creation with `mkfs`, mounting filesystems, persistent configuration in `/etc/fstab`, disk usage analysis with `df` and `du`, and RAID levels 0, 1, 5, and 10.

See you in Part 2.
