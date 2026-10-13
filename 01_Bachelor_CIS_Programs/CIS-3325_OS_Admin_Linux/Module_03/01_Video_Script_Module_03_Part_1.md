# Video Script: Module 03 — Linux Filesystem Hierarchy Standard (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## [INTRO — 0:00–0:45]

Welcome to Module 3. This module covers the Linux Filesystem Hierarchy Standard — the FHS — which is the formal specification of the directory structure used by all Linux distributions. If you have ever wondered why Linux puts things where it does — why executables live in `/usr/bin` instead of `/programs`, why configuration files are in `/etc`, why logs are in `/var/log` — the FHS is the answer.

Part 1 walks through the FHS directory by directory, explaining the purpose of each major location and what you will find there. Part 2 shifts to working with files — reading, searching, filtering, and redirecting output.

The FHS is tested directly on the Linux+ exam and is essential practical knowledge. When a service fails and you need to find its configuration file or log, knowing the FHS tells you exactly where to look.

---

## [SECTION 1 — What Is the FHS? — 0:45–2:00]

### The Filesystem Hierarchy Standard

The FHS is maintained by the Linux Foundation and defines the directory structure and directory contents of Linux and other Unix-like operating systems. It ensures that software, administrators, and users know where to find things regardless of which distribution they are using.

The root of the hierarchy is `/` — the root directory. Everything on a Linux system exists somewhere under `/`. Unlike Windows, which uses separate drive letters like `C:\` and `D:\`, Linux mounts everything under a single unified tree. External drives, USB drives, and network filesystems all appear as directories somewhere under `/`.

---

## [SECTION 2 — Core Binary Directories — 2:00–4:30]

### /bin — Essential User Binaries

`/bin` contains essential user-accessible command binaries that must be available even before other filesystems are mounted. This includes fundamental commands like `ls`, `cp`, `mv`, `rm`, `cat`, `echo`, `grep`, `bash`, and `sh`. These are the tools needed to boot the system and enter single-user maintenance mode.

On modern Linux distributions, `/bin` is often a symbolic link to `/usr/bin` — the two have been merged. But the distinction is historically important and tested on the exam.

### /sbin — System Binaries

`/sbin` contains system administration binaries — tools typically run by root for system maintenance. Examples: `fdisk`, `mkfs`, `fsck`, `ip`, `ifconfig`, `shutdown`, `reboot`, `iptables`, `mount`. Regular users generally should not run these commands and may not have them in their PATH by default.

Like `/bin`, modern distributions often symlink `/sbin` to `/usr/sbin`.

### /usr — User System Resources

`/usr` is the largest directory on most systems. It contains the majority of installed user programs and their support files. The key subdirectories:

- `/usr/bin` — The primary location for user command binaries (most of what you run ends up here)
- `/usr/sbin` — System binaries that are not essential at boot
- `/usr/lib` — Libraries for programs in `/usr/bin` and `/usr/sbin`
- `/usr/local` — Locally installed software not managed by the package manager (compiled from source, third-party tools)
- `/usr/share` — Architecture-independent data: documentation, man pages, icons, timezone data
- `/usr/include` — Header files for C development

### /lib and /lib64 — Shared Libraries

`/lib` contains the shared libraries (`.so` files — shared objects) required by the essential binaries in `/bin` and `/sbin`. `/lib64` contains 64-bit variants. These are the Linux equivalent of Windows DLL files — code shared across multiple programs. `ldd binaryname` shows which shared libraries a binary depends on.

---

## [SECTION 3 — Configuration and Variable Data — 4:30–7:30]

### /etc — Configuration Files

`/etc` is one of the most important directories for system administrators. It contains system-wide configuration files for essentially every service and application on the system. The name originally stood for "et cetera" in early Unix, but today it is understood as the configuration directory.

Key files in `/etc`:

- `/etc/passwd` — User account information (username, UID, GID, home dir, shell)
- `/etc/shadow` — Hashed passwords (readable only by root)
- `/etc/group` — Group definitions
- `/etc/hosts` — Local hostname-to-IP mappings
- `/etc/hostname` — The system's hostname
- `/etc/resolv.conf` — DNS server configuration
- `/etc/fstab` — Filesystem mount table (mounts at boot)
- `/etc/crontab` — System-wide cron schedule
- `/etc/ssh/sshd_config` — SSH server configuration
- `/etc/sudoers` — sudo access rules
- `/etc/apt/` (Ubuntu) or `/etc/dnf/` (RHEL) — Package manager configuration

The exam regularly asks which configuration file controls a specific system behavior. Know these paths.

### /var — Variable Data

`/var` contains variable data — files that are expected to grow over time. This is why separating `/var` onto its own partition is a best practice: it prevents growing data from filling the root filesystem.

Key subdirectories:

- `/var/log` — System and application log files
- `/var/log/syslog` (Ubuntu) or `/var/log/messages` (RHEL) — General system messages
- `/var/log/auth.log` (Ubuntu) or `/var/log/secure` (RHEL) — Authentication logs
- `/var/log/dmesg` — Kernel boot messages
- `/var/lib` — Persistent application state data (MySQL databases, package manager state)
- `/var/spool` — Queued data (print jobs, mail queues, cron jobs pending execution)
- `/var/cache` — Application caches (package manager download cache in `/var/cache/apt`)
- `/var/tmp` — Temporary files preserved between reboots (unlike `/tmp`)

---

## [SECTION 4 — Temporary, Home, and Optional Directories — 7:30–10:00]

### /tmp — Temporary Files

`/tmp` holds temporary files created by applications and users. It is writable by all users. The sticky bit is set on `/tmp` (you will learn more about this in the permissions module) — this means users can create files but cannot delete other users' files.

Critical behavior: `/tmp` is typically cleared on reboot. Do not store anything in `/tmp` that you need to persist.

### /home — User Home Directories

`/home` contains a subdirectory for each regular user account. `/home/student` is the home directory for the user "student." User-specific configuration files, personal documents, and shell configuration files (`.bashrc`, `.bash_profile`) live here.

The root user's home directory is NOT `/home/root` — it is `/root` (at the top level), which is a historical distinction that separates root's files from regular user files.

### /root — Root User's Home

`/root` is the home directory for the root superuser. It is separate from `/home` because `/home` may be on a separate partition that is not mounted during early boot. Root needs a home directory during single-user mode and early boot stages.

### /opt — Optional Software

`/opt` is intended for third-party add-on software packages that are not part of the standard distribution. Large commercial applications, self-contained third-party tools, and some vendor software packages install to `/opt`. Google Chrome and many corporate applications install here.

---

## [SECTION 5 — Mount Points and Virtual Filesystems — 10:00–13:30]

### /mnt and /media — Mount Points

`/mnt` is the traditional location for temporarily mounting filesystems — an additional hard drive, a network share, a USB drive that you are mounting manually for administration purposes.

`/media` is used for automatic mounts — when you plug in a USB drive on a desktop Linux system, it appears under `/media/username/drivelabel`. The distinction is: `/mnt` for administrator-managed manual mounts, `/media` for automatically mounted removable devices.

### /dev — Device Files

`/dev` contains device files — special files that represent hardware devices and virtual devices. In Linux, hardware is accessed through these file interfaces. Key device files:

- `/dev/sda`, `/dev/sdb` — SCSI/SATA hard drives (first and second drive)
- `/dev/sda1`, `/dev/sda2` — Partitions on the first drive
- `/dev/nvme0n1` — NVMe SSDs
- `/dev/null` — The "null device" — discards all data written to it; reads return EOF immediately
- `/dev/zero` — Returns an endless stream of null bytes when read
- `/dev/random` and `/dev/urandom` — Random number generators
- `/dev/tty` — Current terminal
- `/dev/pts/` — Pseudo-terminal devices (SSH sessions, terminal emulators)

`/dev/null` appears frequently in shell scripts and exam questions. Redirecting output to `/dev/null` silences it: `command > /dev/null 2>&1` suppresses both stdout and stderr.

### /proc — Process and Kernel Information

`/proc` is a virtual filesystem — nothing in it is stored on disk. It is generated by the kernel at runtime and provides a file interface to kernel data structures and process information.

Key files in `/proc`:

- `/proc/cpuinfo` — CPU information
- `/proc/meminfo` — Memory usage statistics
- `/proc/uptime` — System uptime in seconds
- `/proc/loadavg` — Load average
- `/proc/PID/` — A directory for each running process (PID is the process ID), containing the process's maps, file descriptors, command line, and more

`cat /proc/cpuinfo` is a simple way to see CPU details. `cat /proc/meminfo` shows memory statistics. The `/proc` filesystem is how tools like `top`, `ps`, and `free` get their data.

### /sys — System and Hardware Information

`/sys` is another virtual filesystem — the sysfs filesystem — that exposes kernel objects, device information, and driver parameters. It is more structured than `/proc` and is used by system administration tools and device management. `/sys/class/net/` contains network interface information. `/sys/block/` contains block device information.

---

## [OUTRO — 13:30–15:00]

That is the complete FHS tour. Let me give you the exam-critical summary:

- `/bin` and `/sbin` — essential binaries and system binaries
- `/etc` — system configuration (all of it)
- `/var` — variable data, logs, databases
- `/home` — user home directories
- `/root` — root user's home
- `/tmp` — temporary files, cleared on reboot
- `/opt` — third-party software
- `/dev` — device files including `/dev/null`
- `/proc` — virtual kernel and process information
- `/sys` — virtual hardware and driver information

When the exam asks "where is the SSH server configuration file?" — `/etc/ssh/sshd_config`. "Where are authentication logs on RHEL?" — `/var/log/secure`. "Where do user home directories live?" — `/home`. These are the FHS questions that appear on the Linux+ exam.

In Part 2, we start working with file content — reading files, searching through them, filtering output, and redirecting it. See you there.

---

## [END OF SCRIPT — PART 1]

---

### Instructor Notes

- Estimated delivery time: 14–15 minutes.
- This content is highly visual — use a directory tree diagram throughout showing the FHS structure. Highlight each directory as you discuss it.
- The `/dev/null` concept is frequently confusing for students — consider a live demo: `echo "test" > /dev/null && echo "nothing happened"`.
- The `/proc` virtual filesystem demo is effective: `cat /proc/cpuinfo` and `cat /proc/meminfo` in the VM show real data, making the concept concrete.
