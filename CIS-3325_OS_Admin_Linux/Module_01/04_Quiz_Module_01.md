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
