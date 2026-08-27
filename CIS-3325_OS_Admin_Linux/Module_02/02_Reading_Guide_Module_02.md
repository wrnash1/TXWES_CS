# Reading Guide: Module 02 — Linux Installation and System Navigation

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Module 2 covers two foundational skill areas: the Linux installation process and the core filesystem navigation commands. Understanding how Linux is installed — and the partitioning and filesystem decisions made during installation — is tested directly on the Linux+ exam. The navigation commands introduced in this module are the ones you will use in every lab and every real-world Linux administration task.

---

### 1. High-Yield Glossary

- **ISO image**: A disk image file containing the complete contents of a CD/DVD or installation media. Used to install operating systems. Verify checksums (SHA-256) before use.
- **BIOS (Basic Input/Output System)**: Legacy firmware that initializes hardware before the OS boots. Uses MBR partitioning. Supports disks up to 2 TB with up to 4 primary partitions.
- **UEFI (Unified Extensible Firmware Interface)**: Modern replacement for BIOS. Uses GPT partitioning. Supports disks larger than 2 TB and up to 128 partitions. Required for Secure Boot.
- **MBR (Master Boot Record)**: Legacy disk partitioning standard. Maximum disk size 2 TB. Maximum 4 primary partitions (or 3 primary + 1 extended containing logical partitions).
- **GPT (GUID Partition Table)**: Modern partitioning standard for UEFI. Supports disks up to 9.4 ZB and up to 128 partitions per disk.
- **ext4**: The Fourth Extended Filesystem. Default filesystem on Ubuntu and Debian. Supports journaling, files up to 16 TB, volumes up to 1 EB. Can be grown and shrunk.
- **XFS**: High-performance journaling filesystem. Default on RHEL-family distributions. Can be grown but NOT shrunk. Use `xfs_growfs` to expand.
- **btrfs**: Modern copy-on-write filesystem with built-in snapshots, RAID, and compression. Default on SUSE and Fedora. More complex to administer.
- **swap**: Disk space used as virtual memory when RAM is full. A swap partition is created during installation.
- **`fdisk`**: Interactive command-line partitioning tool for MBR disks. Run with `sudo fdisk /dev/sdX`.
- **`parted`**: Partitioning tool supporting both MBR and GPT. Can be used non-interactively in scripts.
- **`mkfs.ext4`**: Formats a partition with the ext4 filesystem. Full syntax: `sudo mkfs.ext4 /dev/sdb1`.
- **`mkfs.xfs`**: Formats a partition with the XFS filesystem.
- **`pwd`**: Print Working Directory. Shows your current location in the filesystem.
- **`ls`**: List directory contents. Key flags: `-l` (long format), `-a` (all/hidden files), `-h` (human-readable sizes), `-R` (recursive).
- **`cd`**: Change Directory. `cd ~` or `cd` alone returns to home. `cd ..` moves up one level.
- **Absolute path**: A path that starts from root (`/`). Example: `/home/student/documents`. Always starts with `/`.
- **Relative path**: A path relative to the current directory. Example: `documents` or `./documents` when already in `/home/student`.
- **`mkdir`**: Make Directory. `mkdir -p` creates parent directories as needed.
- **`rmdir`**: Remove empty directory. Fails if directory contains files.
- **`touch`**: Creates an empty file or updates a file's timestamps.
- **`cp`**: Copy files. `cp -r` for directories. `cp -p` preserves permissions and timestamps. `cp -i` prompts before overwriting.
- **`mv`**: Move or rename files and directories. No `-r` flag needed for directories.
- **`rm`**: Remove files permanently. `rm -r` for directories. `rm -i` prompts before deleting. `rm -rf` silently and permanently removes directory trees — use with extreme caution.
- **`file`**: Determines file type by reading file content, not extension. Returns type description like "ASCII text" or "ELF 64-bit executable."
- **`which`**: Searches PATH for the executable that runs when a command name is typed.
- **`whereis`**: Locates the binary, source, and man page for a command.
- **`man`**: Opens the manual page for a command. Navigate with arrow keys, search with `/`, quit with `q`.
- **Man page sections**: Section 1 = user commands. Section 5 = file formats. Section 8 = system administration. Specify with: `man 5 passwd`.

---

### 2. Partition Layout Reference

| Mount Point | Purpose | Typical Size |
|---|---|---|
| `/` (root) | Core OS | 10–20 GB minimum |
| `/boot` | Kernel and boot files | 500 MB – 1 GB |
| `/home` | User home directories | Remaining space |
| `/var` | Logs, databases, caches | 10+ GB for servers |
| `/tmp` | Temporary files | 2–5 GB |
| swap | Virtual memory | Equal to RAM (up to 8 GB RAM) |

---

### 3. ls Long Format Output

When you run `ls -l`, each line has this format:

```
-rw-r--r-- 1 student student 4096 Jun  1 09:23 myfile.txt
```

Reading left to right:

- `-rw-r--r--` — file type and permissions (covered in Module 4)
- `1` — hard link count
- `student` — owner
- `student` — group
- `4096` — size in bytes (use `-h` for human-readable)
- `Jun  1 09:23` — last modification date and time
- `myfile.txt` — filename

The first character of the permissions string identifies the file type: `-` = regular file, `d` = directory, `l` = symbolic link, `b` = block device, `c` = character device.

---

### 4. Path Quick Reference

| Path Expression | Meaning |
|---|---|
| `/` | Root of the filesystem |
| `~` | Current user's home directory |
| `.` | Current directory |
| `..` | Parent directory |
| `/etc/passwd` | Absolute path (starts with `/`) |
| `../config` | Relative path (up one level, then into config) |

---

### Required Readings and Videos

- **Required Reading**: [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) — Chapters 2, 3, and 4. Chapter 2: navigation; Chapter 3: exploring the system; Chapter 4: manipulating files and directories.
- **Required Video**: [LearnLinuxTV — Linux Fundamentals](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), Episodes 4–6. These cover filesystem navigation and file manipulation.

---

### Study Checklist

- [ ] Explain the difference between BIOS/MBR and UEFI/GPT.
- [ ] List the standard partition mount points and the purpose of each.
- [ ] Describe when to use XFS vs. ext4 and what the key difference is between them.
- [ ] Run `ls -lah` and identify all fields in the output.
- [ ] Demonstrate the difference between an absolute path and a relative path.
- [ ] Use `man ls` to look up a flag not covered in the reading guide.
- [ ] Complete the Module 2 lab.
- [ ] Complete the Module 2 quiz.

---

## 9. Supplemental Resources

**1. [Linux Filesystem Hierarchy Standard — The Linux Documentation Project](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/)**
A complete reference to the Linux Filesystem Hierarchy Standard (FHS), explaining the purpose of every top-level directory. Essential background for understanding where configuration files, binaries, logs, and variable data are stored by convention.

**2. [Red Hat — How to Manage Partitions with fdisk](https://www.redhat.com/sysadmin/fdisk-partitioning)**
A practical Red Hat sysadmin article covering `fdisk` for MBR partitioning and `gdisk` for GPT. Includes step-by-step partition creation and the MBR-vs-GPT decision framework used in real enterprise deployments.

**3. [man7.org — ls(1) Manual Page](https://man7.org/linux/man-pages/man1/ls.1.html)**
The online version of the `ls` man page from the Linux man-pages project. Useful for reviewing all available flags and their descriptions when not at a terminal, and for understanding the full output format of `ls -l`.
