# Reading Guide: Module 02 - File System Hierarchy and Navigation Commands
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 02 – File System Hierarchy and Navigation Commands**! This week covers the Linux Filesystem Hierarchy Standard (FHS), the purpose of each major top-level directory, and the core navigation and file-management commands every Linux administrator must know. These concepts appear heavily on the CompTIA Linux+ XK0-005 exam across the System Management and Scripting domains.

As you work through this material you will learn how Linux organizes all files under a single root (`/`) tree, how to move through the hierarchy efficiently at the command line, and how to locate, inspect, and manipulate files using standard tools.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Filesystem Hierarchy Standard (FHS)**: A specification maintained by the Linux Foundation that defines the directory structure and directory contents in Linux distributions. It ensures that software and administrators can predict where files are located regardless of the distribution. Key directories tested on Linux+ include `/etc`, `/var`, `/usr`, `/home`, `/boot`, `/dev`, `/proc`, and `/tmp`.
*   **Absolute vs. Relative Paths**: An absolute path always begins at the root of the filesystem with a `/` (e.g., `/var/log/syslog`) and points to the same location regardless of your current directory. A relative path is interpreted starting from your current working directory (e.g., `../log/syslog` moves up one level then into `log`). Confusing these is a common exam trap.
*   **`/etc` directory**: Contains system-wide configuration files and initialization scripts. Examples include `/etc/passwd` (user account info), `/etc/fstab` (filesystem mount table), and `/etc/hostname`. This directory is one of the most exam-tested locations on Linux+.
*   **`/var` directory**: Holds variable data that changes frequently during normal operation — system logs (`/var/log`), mail spools, print queues, and package management databases. When a disk fills up on a production server, `/var/log` is typically the first place to check.
*   **`/proc` directory**: A virtual pseudo-filesystem that exposes kernel and process information as files. It is not stored on disk; the kernel generates it in memory on demand. Files like `/proc/cpuinfo` and `/proc/meminfo` provide real-time hardware statistics.
*   **`man` pages**: Built-in manual pages accessed with the `man` command (e.g., `man ls`). Each page is divided into numbered sections: section 1 = user commands, section 5 = file formats, section 8 = administrative commands. The `man -k keyword` command searches descriptions across all sections (equivalent to `apropos`).

---

### 2. Certification Exam Tips
*   **Domain alignment:** FHS and navigation commands fall under Linux+ Domain 1.0 (System Management). Expect 4–6 questions involving directory purposes and path resolution.
*   **Know every major FHS directory:** The exam tests `/bin` vs `/usr/bin`, `/sbin` vs `/usr/sbin`, the purpose of `/tmp` (world-writable, cleared on reboot), and `/srv` (service data). On modern systemd distros, `/bin`, `/sbin`, and `/lib` are often symlinks into `/usr`.
*   **Absolute path trap:** A question will describe a user "currently in `/home/user/docs`" and ask which command reaches `/var/log`. Only `cd /var/log` is absolute — `cd ../../var/log` is relative and equally valid but the question asks for the absolute form.
*   **Commands to memorize:** `pwd`, `ls -la`, `cd`, `cp`, `mv`, `rm -r`, `mkdir -p`, `touch`, `find / -name filename`, `locate filename`. Know the difference between `find` (real-time search, slower) and `locate` (database-based, faster but requires `updatedb`).
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) is your free OER textbook — chapters 3–5 cover navigation, file manipulation, and working with commands in depth. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) provides video demonstrations of these commands in a live terminal environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 3–5 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), covering navigation, file and directory manipulation, and working with commands.
*   **Required Video:** Watch the filesystem and navigation videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist demonstrating core administration tasks in a live terminal.

---

### Lab & Command Integration
In this week's hands-on lab you will navigate the Linux directory tree using absolute and relative paths, list directory contents with `ls -la`, use `find` to locate files by name and permission, and read manual pages with `man`. Practice using `pwd` after each `cd` to confirm your location.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 3–5 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the filesystem and navigation videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
