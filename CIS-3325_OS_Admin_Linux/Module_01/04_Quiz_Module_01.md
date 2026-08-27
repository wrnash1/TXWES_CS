# Quiz: Module 01 — Introduction to Linux and Open Source

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question has one correct answer unless otherwise noted. After selecting your answer, read the distractor analysis to understand why the other options are incorrect — this analysis is a core part of exam preparation.

---

### Question 1

Linus Torvalds released the first version of the Linux kernel in which year?

A. 1983
B. 1987
C. 1991
D. 1995

**Correct Answer: C**

**Distractor Analysis**:

- **A (1983)** is the year Richard Stallman launched the GNU Project — a common confusion since GNU and Linux are closely linked. Stallman started GNU eight years before Torvalds wrote the kernel.
- **B (1987)** is the year Andrew Tanenbaum released Minix, which inspired Torvalds but is a completely separate project.
- **C (1991)** is correct. Torvalds' famous comp.os.minix newsgroup post was dated August 25, 1991.
- **D (1995)** is a distractor representing a later date. By 1995 the Linux kernel was already in widespread use.

---

### Question 2

A software license that requires all derivative works to be distributed under the same license is best described as which type?

A. Permissive
B. Proprietary
C. Copyleft
D. Freeware

**Correct Answer: C**

**Distractor Analysis**:

- **A (Permissive)** is incorrect — permissive licenses (MIT, Apache) explicitly allow derivative works to be closed-source proprietary products. No share-alike requirement.
- **B (Proprietary)** is incorrect — proprietary software restricts use, modification, and redistribution entirely. It is the opposite of open source.
- **C (Copyleft)** is correct. The GPL is the most important copyleft license. Copyleft uses copyright law to ensure software freedom is preserved in derivative works.
- **D (Freeware)** is incorrect — freeware means software distributed at no cost, but the source code may not be available and the license may restrict modification. Price and freedom are separate concepts.

---

### Question 3

Which component of a Linux system is responsible for managing memory, hardware devices, and scheduling processes?

A. The shell
B. The terminal emulator
C. The bootloader
D. The kernel

**Correct Answer: D**

**Distractor Analysis**:

- **A (The shell)** is incorrect — the shell is the command interpreter running in userspace. It does not manage hardware or memory directly.
- **B (The terminal emulator)** is incorrect — the terminal emulator is a graphical application that provides a text window. It has no hardware management role.
- **C (The bootloader)** is incorrect — the bootloader (GRUB2) loads the kernel from disk and hands it control. After that, the bootloader is done.
- **D (The kernel)** is correct. The kernel runs in privileged kernel space and manages all hardware resources, memory allocation, process scheduling, and device drivers.

---

### Question 4

You are setting up a new Linux server for enterprise use and need a distribution that uses the `dnf` package manager and `.rpm` package format. Which of the following distributions should you choose?

A. Ubuntu Server
B. Debian
C. Rocky Linux
D. Kali Linux

**Correct Answer: C**

**Distractor Analysis**:

- **A (Ubuntu Server)** is incorrect — Ubuntu is Debian-based and uses `apt` with `.deb` packages.
- **B (Debian)** is incorrect — Debian also uses `apt` and `.deb` packages.
- **C (Rocky Linux)** is correct. Rocky Linux is a RHEL-compatible rebuild that uses `dnf` and `.rpm` packages — appropriate for enterprise environments that require RHEL compatibility without a subscription cost.
- **D (Kali Linux)** is incorrect — Kali is Debian-based (uses `apt`) and is designed for penetration testing, not enterprise server use.

---

### Question 5

A system administrator needs to run a command on a remote server over an encrypted connection. Which protocol should be used?

A. Telnet
B. FTP
C. SSH
D. HTTP

**Correct Answer: C**

**Distractor Analysis**:

- **A (Telnet)** is incorrect — Telnet transmits all data including passwords in plain text. It is insecure and obsolete for production use.
- **B (FTP)** is incorrect — FTP is a file transfer protocol. It does not provide an interactive command shell and also transmits credentials in plain text.
- **C (SSH)** is correct. SSH — Secure Shell — provides an encrypted interactive session for remote administration. It is the standard protocol for remote Linux server management.
- **D (HTTP)** is incorrect — HTTP is the web protocol for transferring hypertext documents. It does not provide interactive command-line access.

---

### Question 6

Which of the following best describes the difference between the shell and the terminal emulator?

A. The shell is a graphical application; the terminal emulator is a text interpreter.
B. The terminal emulator provides the text window; the shell interprets and executes commands.
C. They are two names for the same program.
D. The terminal emulator manages hardware; the shell manages files.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect — this reverses the relationship. The terminal emulator is the graphical application; the shell is the text interpreter running inside it.
- **B** is correct. The terminal emulator (GNOME Terminal, Windows Terminal) provides the text window UI. The shell (bash, zsh) runs inside that window and processes commands.
- **C** is incorrect — they are distinct programs. GNOME Terminal starts a bash process inside itself, but they are separate.
- **D** is incorrect — neither the terminal emulator nor the shell manages hardware. Hardware management is the kernel's job.

---

### Question 7

The GNU Project was started by which individual with the goal of creating a free Unix-like operating system?

A. Linus Torvalds
B. Andrew Tanenbaum
C. Richard Stallman
D. Dennis Ritchie

**Correct Answer: C**

**Distractor Analysis**:

- **A (Linus Torvalds)** is incorrect — Torvalds wrote the Linux kernel in 1991, eight years after the GNU Project began. His work completed the GNU system by providing the missing kernel.
- **B (Andrew Tanenbaum)** is incorrect — Tanenbaum wrote Minix, an educational Unix-like system, but he did not start the GNU Project.
- **C (Richard Stallman)** is correct. Stallman founded the GNU Project in 1983, established the Free Software Foundation in 1985, and wrote the GPL.
- **D (Dennis Ritchie)** is incorrect — Ritchie co-created Unix at Bell Labs in 1969 with Ken Thompson. He is the inspiration for much of Linux's design but did not start the GNU Project.

---

### Question 8

Which Linux distribution is specifically designed for penetration testing and security research, and is NOT recommended as a general-purpose learning environment?

A. Ubuntu Server
B. Alpine Linux
C. Arch Linux
D. Kali Linux

**Correct Answer: D**

**Distractor Analysis**:

- **A (Ubuntu Server)** is incorrect — Ubuntu Server is an excellent general-purpose learning environment and is the recommended distribution for this course.
- **B (Alpine Linux)** is incorrect — Alpine is a minimal distribution used primarily for Docker containers. It is not a penetration testing tool.
- **C (Arch Linux)** is incorrect — Arch is targeted at experienced users who want full control over their system. It is not a security research platform.
- **D (Kali Linux)** is correct. Kali is pre-loaded with penetration testing tools and is designed for security professionals. Using it as a daily driver or primary learning environment is inappropriate and potentially problematic.

---

### Question 9

A developer writes a program using code licensed under GPL v2. Under the terms of the GPL, what is required when distributing the program?

A. The developer must pay a licensing fee to the Free Software Foundation.
B. The source code must be made available under the same GPL license.
C. The developer must obtain written permission from Linus Torvalds.
D. The program can only be distributed at no cost.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect — the GPL charges no licensing fees. It is a free license in both senses of the word.
- **B** is correct. This is the core copyleft requirement: distributing GPL-licensed software (or derivatives) requires making the source code available under the same GPL terms.
- **C** is incorrect — Linus Torvalds holds the copyright to the Linux kernel but does not control the GPL license terms. The Free Software Foundation manages the GPL, and no individual approval is required.
- **D** is incorrect — GPL software can be sold. The requirement is source code availability and GPL licensing for derivatives, not free distribution. Red Hat charges for RHEL support despite GPL licensing.

---

### Question 10

Which VirtualBox feature allows you to save the exact state of a VM so you can return to that state if changes go wrong?

A. Cloning
B. Shared folders
C. Snapshots
D. Guest Additions

**Correct Answer: C**

**Distractor Analysis**:

- **A (Cloning)** is incorrect — cloning creates a full copy of a VM. It is useful for creating multiple VMs from the same base, but does not provide a quick restore point during active work.
- **B (Shared folders)** is incorrect — shared folders enable file sharing between the host and guest OS. They have no role in saving or restoring VM state.
- **C (Snapshots)** is correct. Snapshots capture the complete state of a VM — disk, memory, and settings — at a moment in time. You can restore a snapshot in seconds, making it ideal for protecting against destructive lab mistakes.
- **D (Guest Additions)** is incorrect — Guest Additions is a package of drivers and tools installed inside the VM to improve performance and host-guest integration (clipboard sharing, drag-and-drop, better screen resolution). It does not save state.

---

### Question 11 (5 points)

Which of the following is NOT one of the four essential freedoms defined by the Free Software Foundation?

A. The freedom to run the program for any purpose.
B. The freedom to study and modify the source code.
C. The freedom to charge any price for the software.
D. The freedom to distribute copies of your modified versions.

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect as a "not" question — Freedom 0 is explicitly the freedom to run the program for any purpose.
- **B** is incorrect as a "not" question — Freedom 1 is the freedom to study and change the source code, which requires access to the source.
- **C** is correct as a "not" question. The four freedoms (0–3) cover running, studying, redistributing, and distributing modifications. Setting a price is permitted but is not itself one of the four defined freedoms.
- **D** is incorrect as a "not" question — Freedom 3 is the freedom to distribute copies of your modified versions to others.

---

### Question 12 (5 points)

What is the primary purpose of the `/etc/os-release` file on a Linux system?

A. To store the root user's password hash.
B. To define default environment variables for all users.
C. To provide machine-readable distribution identification information.
D. To list all installed packages and their versions.

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect — password hashes are stored in `/etc/shadow` (or `/etc/passwd` on very old systems). `/etc/os-release` has nothing to do with authentication.
- **B** is incorrect — system-wide environment variables are typically set in `/etc/environment` or `/etc/profile`. `/etc/os-release` contains only distribution metadata.
- **C** is correct. `/etc/os-release` contains key=value pairs identifying the distribution name, version, and ID. It is the standard way for scripts to detect which Linux distribution they are running on.
- **D** is incorrect — installed package lists are managed by the package manager (dpkg, rpm). You would use `dpkg -l` or `rpm -qa` to list packages, not read `/etc/os-release`.

---

### Question 13 (5 points)

The `uname -a` command is run on a Linux system and returns output that includes `x86_64`. What does this indicate?

A. The system is running a 32-bit operating system.
B. The processor architecture is 64-bit AMD/Intel compatible.
C. The kernel version is 64 bits long as a binary number.
D. The system has 64 GB of installed RAM.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect — `x86_64` specifically indicates a 64-bit architecture, not 32-bit. A 32-bit x86 system would show `i386` or `i686`.
- **B** is correct. `x86_64` (also written as `amd64`) is the 64-bit extension of the x86 instruction set. It is the dominant architecture for modern servers and desktops.
- **C** is incorrect — the kernel version is expressed as a text string (e.g., `6.5.0-21-generic`), not a binary number. The architecture field is separate.
- **D** is incorrect — `uname -a` does not report RAM. The `free -h` or `cat /proc/meminfo` commands show memory information.

---

### Question 14 (5 points)

Which of the following commands displays only the username of the currently logged-in user?

A. `id`
B. `whoami`
C. `hostname`
D. `pwd`

**Correct Answer: B**

**Distractor Analysis**:

- **A (id)** is incorrect — the `id` command displays the user ID (UID), group ID (GID), and all group memberships. It includes more information than just the username.
- **B (whoami)** is correct. The `whoami` command prints only the effective username of the current user — nothing else.
- **C (hostname)** is incorrect — `hostname` prints the system's hostname, not the logged-in username.
- **D (pwd)** is incorrect — `pwd` prints the current working directory path, not any user information.

---

### Question 15 (5 points)

A student wants to understand what a Linux command does before running it. Which command should they use first?

A. `info`
B. `man`
C. `help`
D. `explain`

**Correct Answer: B**

**Distractor Analysis**:

- **A (info)** is incorrect as the primary answer — `info` is the GNU documentation reader and provides more verbose documentation for some commands. However, `man` (the manual) is the standard, universally available first resource and is tested on the Linux+ exam.
- **B (man)** is correct. `man <command>` opens the manual page for a command. Man pages are available on every Linux system and are the authoritative reference for command syntax, options, and behavior.
- **C (help)** is incorrect — `help` only works for bash built-in commands (like `cd`, `echo`, `export`). It does not provide documentation for external programs.
- **D (explain)** is incorrect — there is no standard Linux command named `explain`. This is a distractor.

---

### Question 16 (5 points)

In the context of Linux virtualization labs, what is the primary advantage of taking a VirtualBox snapshot BEFORE making major system changes?

A. It compresses the VM's virtual disk to save space.
B. It allows you to restore the VM to a known-good state if changes cause problems.
C. It automatically backs up the VM to cloud storage.
D. It speeds up the VM by caching its current memory state.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect — snapshots actually consume additional disk space because they store the delta (changes) from the previous state. They do not compress the virtual disk.
- **B** is correct. The primary purpose of a pre-change snapshot is recovery. If a configuration change breaks the system, you can restore the snapshot in seconds and return to the working state.
- **C** is incorrect — VirtualBox snapshots are stored locally on the host filesystem. They do not sync to any cloud service unless you separately back up the VM folder.
- **D** is incorrect — snapshots do not improve VM performance. Saving a snapshot pauses the VM briefly and increases overall disk usage.

---

### Question 17 (5 points)

Which of the following best describes the role of a bootloader such as GRUB2?

A. It manages running processes after the operating system has started.
B. It provides a graphical desktop environment for the user.
C. It locates the kernel on disk, loads it into memory, and passes control to it.
D. It handles network configuration during the boot process.

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect — managing running processes is the kernel's job, assisted by init systems like systemd. GRUB2 exits after handing off to the kernel.
- **B** is incorrect — graphical desktop environments (GNOME, KDE) are userspace applications. GRUB2 typically displays a text menu and has no desktop role.
- **C** is correct. GRUB2 (Grand Unified Bootloader version 2) reads the filesystem, locates the Linux kernel image, loads it into RAM, and transfers execution to it. GRUB2 also allows selecting different kernels or boot parameters.
- **D** is incorrect — network configuration during a running system is handled by systemd-networkd, NetworkManager, or netplan. GRUB2 does not configure networking.

---

### Question 18 (5 points)

A sysadmin checks the output of `df -h` and sees that the root filesystem (`/`) is at 94% usage. What is the most immediate concern?

A. The kernel will automatically compress old files to reclaim space.
B. The system may become unstable or services may fail if the filesystem fills completely.
C. The system will automatically delete the oldest log files.
D. The `/tmp` directory will be automatically cleared by the OS.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect — Linux does not automatically compress files to reclaim space. Compression must be explicitly configured (e.g., via filesystem-level compression with Btrfs or ZFS, which is not the default).
- **B** is correct. A full root filesystem is a critical emergency. Many services (databases, web servers, logging daemons) write to disk and will fail or crash if they cannot write. SSH may even refuse new connections if certain log or lock files cannot be created.
- **C** is incorrect — Linux does not automatically delete old log files in response to disk pressure. `logrotate` can be configured to manage log rotation on a schedule, but it does not trigger automatically when the disk is full.
- **D** is incorrect — while `/tmp` is often mounted as `tmpfs` (RAM-backed) on modern systems, it is a separate filesystem from `/`. Even if `/tmp` is automatically cleaned (some systems clean it at boot), that does not affect the root filesystem's usage.

---

### Question 19 (5 points)

What command would you run to display how long a Linux system has been running since its last boot?

A. `ps aux`
B. `top`
C. `uptime`
D. `last`

**Correct Answer: C**

**Distractor Analysis**:

- **A (ps aux)** is incorrect — `ps aux` lists all currently running processes. It does not report system uptime directly.
- **B (top)** is incorrect — while the `top` command does display uptime in its header, the dedicated command for displaying uptime is `uptime`. On the Linux+ exam, use the most specific command.
- **C (uptime)** is correct. The `uptime` command prints the current time, how long the system has been running, the number of logged-in users, and the 1-, 5-, and 15-minute load averages.
- **D (last)** is incorrect — `last` shows a history of user logins and system reboots by reading `/var/log/wtmp`. It can show when the system was last rebooted but does not directly report current uptime.

---

### Question 20 (5 points)

Which of the following statements about the Linux kernel is TRUE?

A. The Linux kernel is licensed under the MIT License, allowing proprietary forks.
B. The Linux kernel is a monolithic kernel that includes drivers and system call handling.
C. The Linux kernel runs entirely in userspace for security isolation.
D. The Linux kernel was first released in 2001 by the Linux Foundation.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect — the Linux kernel is licensed under GPL v2, which is a copyleft license. It cannot be incorporated into proprietary software without releasing derivative source code.
- **B** is correct. Linux is a monolithic kernel — the core kernel, device drivers, and filesystem code run together in kernel space as a single large program. This contrasts with microkernels (like Mach) that run drivers in userspace.
- **C** is incorrect — the kernel runs in privileged kernel space, not userspace. User programs run in userspace and must use system calls to request kernel services. Running the kernel in userspace would defeat the purpose of kernel privilege separation.
- **D** is incorrect — the Linux kernel was first released in 1991 by Linus Torvalds, a Finnish university student. The Linux Foundation was not founded until 2000 and does not own the kernel.

---

### Answer Key

| Question | Answer |
|---|---|
| 1 | C |
| 2 | C |
| 3 | D |
| 4 | C |
| 5 | C |
| 6 | B |
| 7 | C |
| 8 | D |
| 9 | B |
| 10 | C |
| 11 | C |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | B |
| 16 | B |
| 17 | C |
| 18 | B |
| 19 | C |
| 20 | B |
