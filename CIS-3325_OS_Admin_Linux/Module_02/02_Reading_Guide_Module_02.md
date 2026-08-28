# Reading Guide: Module 02 — Linux Installation and System Navigation

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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
