# Video Script: Module 02 — Linux Installation and System Navigation (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## [INTRO — 0:00–0:45]

Welcome back. This is Module 2, Part 1 — Linux Installation and System Navigation. In Module 1 we covered the history, philosophy, and architecture of Linux. Now we get hands-on. Part 1 of this module walks you through the full Linux installation process — from downloading the ISO to partitioning the disk to your first boot. Part 2 covers post-install navigation: the commands you will use every day to move through the filesystem and manage files.

If you already completed the Module 1 lab and have a working Ubuntu Server VM, you have already done much of what we describe in Part 1. That is fine — follow along to understand the decisions that were made during installation, particularly around partitioning.

---

## [SECTION 1 — Getting the ISO and Creating Bootable Media — 0:45–3:00]

### Downloading the ISO

A Linux distribution is distributed as an ISO file — a disk image that contains the complete installer. For this course we use Ubuntu Server 22.04 LTS. Download it from ubuntu.com/download/server. The file is approximately 1.4 gigabytes.

For any ISO you download, verify the checksum before using it. Ubuntu provides SHA-256 checksums on the download page. On Linux: `sha256sum ubuntu-22.04.3-live-server-amd64.iso`. On Windows: `Get-FileHash` in PowerShell. Compare the output to the published checksum. A mismatch means the file is corrupted or tampered with.

### Creating Bootable Media

If you are installing on physical hardware — not a VM — you need to write the ISO to a USB drive. On Windows, use **Rufus** (free, at rufus.ie). Select your USB drive, select the ISO, and click Start. Rufus will warn you that the USB drive will be erased — that is expected.

On Linux, you can use `dd` directly: `sudo dd if=ubuntu-22.04.3-live-server-amd64.iso of=/dev/sdb bs=4M status=progress`. Replace `/dev/sdb` with your actual USB device — double-check this with `lsblk` before running `dd`, because writing to the wrong device will destroy data. There is no undo for `dd`.

For our VM lab, we attach the ISO directly to the virtual optical drive, so no USB creation is needed.

---

## [SECTION 2 — BIOS/UEFI and Boot Order — 3:00–5:00]

### BIOS vs. UEFI

All modern computers have firmware — software that runs before the operating system and initializes hardware. There are two firmware types you need to know for the Linux+ exam.

BIOS — Basic Input/Output System — is the legacy firmware standard, dating back to the late 1970s. It uses MBR (Master Boot Record) partitioning and supports disks up to 2 TB with up to four primary partitions.

UEFI — Unified Extensible Firmware Interface — is the modern replacement for BIOS. It supports GPT (GUID Partition Table) partitioning, disks larger than 2 TB, up to 128 partitions, faster boot times, and Secure Boot. UEFI has been the standard on new hardware since roughly 2011.

For the exam: know that MBR goes with BIOS, GPT goes with UEFI, and GPT is required for disks larger than 2 TB.

### Setting Boot Order

To boot from an installation media — USB or ISO in a VM — you must set the boot order so the optical drive or USB is checked before the hard disk. On physical hardware, press the firmware key at startup (commonly F2, F10, F12, or Delete — it varies by manufacturer) to enter the BIOS/UEFI setup. Navigate to the boot order settings and move your installation media to the top.

In VirtualBox, the boot order is set in VM Settings → System → Motherboard. With an ISO attached to the virtual optical drive, the VM will boot the installer automatically on first start.

---

## [SECTION 3 — Installation Steps — 5:00–8:30]

### Ubuntu Server Installation Walkthrough

The Ubuntu Server installer is a text-based interactive installer. Let's walk through the key decisions.

**Language and keyboard**: Choose your language and keyboard layout. US English defaults are appropriate for this course.

**Network configuration**: The installer detects your network interfaces. In a VM on NAT, DHCP configures automatically. Note the IP address assigned — you will use it for SSH connections from your host.

**Mirror configuration**: Ubuntu offers a regional mirror. The default works for most locations. The installer tests the mirror connection — if it fails, you can continue without an updated mirror and update packages later.

**Storage configuration**: This is the most important step. Choose "Use an entire disk" for simplicity. The installer will propose a partition layout. For a VM, accept the defaults. On physical hardware, you may want to customize.

**Profile setup**: Set your username and password. The server hostname becomes important later when managing multiple servers. Choose something descriptive.

**SSH**: Select "Install OpenSSH server." This is mandatory for our labs — you will SSH from your host terminal to the VM in every subsequent module.

**Featured snaps**: Skip all snap packages. We install software through `apt` in this course.

After confirming, the installer copies files and configures the system. The final step is a reboot.

### First Boot

After rebooting and removing the installation media, the system boots to a login prompt. Log in with the credentials you created. The bash prompt confirms a successful installation.

---

## [SECTION 4 — Partitioning Schemes — 8:30–12:00]

### Why Partitioning Matters

Partitioning divides a physical disk into independent logical sections. Each partition has its own filesystem and mount point. Good partitioning is a security and reliability practice — a filesystem that fills up can only affect processes using that filesystem, not the entire system.

For the Linux+ exam, you need to know the standard partition layout and why each partition exists.

### Standard Linux Partition Layout

The simplest possible layout has one partition: the root filesystem mounted at `/`. Everything lives on that one partition. This is fine for VMs and simple servers.

A more robust layout separates key directories into their own partitions:

- **`/`** (root): The root filesystem. Contains the core operating system. Typically 10–20 GB minimum.
- **`/boot`**: Holds the kernel and boot files. Separate because some bootloaders cannot read advanced filesystems or LVM. Typically 500 MB–1 GB.
- **`/home`**: User home directories. Separating `/home` means the root filesystem cannot be filled by user data. Size depends on user count and storage needs.
- **`/var`**: Variable data — logs, databases, mail queues, package caches. Separating `/var` prevents a runaway log file from filling the root filesystem. Critical for servers.
- **`/tmp`**: Temporary files. Some security standards require `/tmp` to be a separate partition mounted with `noexec` to prevent executing temporary files.
- **swap**: Virtual memory space on disk. Used when RAM is full. General guidance: equal to RAM for systems with 8 GB or less, half of RAM for larger systems.

### Partitioning Tools

`fdisk` is the classic partitioning tool for MBR disks. Run `sudo fdisk /dev/sda` to enter the interactive partitioning interface. Key commands inside fdisk: `p` prints the current partition table, `n` creates a new partition, `d` deletes a partition, `t` changes the partition type, `w` writes changes and exits, `q` quits without saving.

`parted` handles both MBR and GPT disks and can be used non-interactively in scripts. `gdisk` is specifically for GPT disks.

For the exam, know that `fdisk` works with MBR and that `parted` or `gdisk` is needed for GPT/UEFI systems.

---

## [SECTION 5 — Filesystem Types — 12:00–14:30]

### ext4 — Extended Filesystem 4

ext4 is the most widely used Linux filesystem, introduced in 2008. It is the default on Debian and Ubuntu. Key characteristics: supports files up to 16 TB, volumes up to 1 EB, journaling (tracks changes before writing to prevent corruption), and backward compatibility with ext3 and ext2.

Format a partition with ext4: `sudo mkfs.ext4 /dev/sdb1`

### XFS

XFS is the default filesystem on RHEL-family distributions. It was originally developed by SGI and is designed for high-performance large-file workloads. Key feature: XFS filesystems can be expanded (grown) but cannot be shrunk — this is a critical exam distinction. `xfs_growfs` expands a mounted XFS filesystem; there is no equivalent shrink command.

Format with XFS: `sudo mkfs.xfs /dev/sdb1`

### Btrfs

Btrfs (B-tree filesystem) is a modern copy-on-write filesystem with built-in features including snapshots, compression, RAID, and subvolumes. It is the default filesystem on SUSE Linux and Fedora (for root). It is more complex to administer but offers capabilities not available in ext4 or XFS.

### Comparing Filesystems for the Exam

| Filesystem | Default On | Grow | Shrink | Journaling | Notes |
|---|---|---|---|---|---|
| ext4 | Ubuntu/Debian | Yes | Yes | Yes | Most widely used |
| XFS | RHEL/CentOS | Yes | No | Yes | Cannot shrink |
| btrfs | SUSE/Fedora | Yes | Yes | CoW | Built-in snapshots |

---

## [OUTRO — 14:30–15:00]

That covers the full installation process — from ISO download through partitioning decisions and filesystem selection. These concepts appear heavily in Domain 1 of the Linux+ exam.

In Part 2, we pivot to everyday navigation. You will learn the essential commands for moving through the filesystem, creating and manipulating files and directories, and reading documentation. Every command you learn in Part 2 will be used in every lab for the rest of this course. See you there.

---

## [END OF SCRIPT — PART 1]

---

### Instructor Notes

- Estimated delivery time: 14–16 minutes.
- The partitioning section benefits significantly from a diagram — show a disk divided into labeled partition blocks.
- Filesystem comparison table should appear as a visual slide, not just spoken.
- Emphasize the XFS cannot-shrink rule — it is a frequent exam distractor.
