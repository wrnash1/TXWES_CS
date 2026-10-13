# Video Script: Module 01 — Introduction to Linux and Open Source (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## [INTRO — 0:00–0:45]

Welcome back to Module 1. In Part 1 we covered the history of Linux, the GNU project, FOSS licensing, the kernel-shell-userspace architecture, and the major distribution families. In Part 2 we are going to get practical. We will talk about why the command line is the essential tool for system administrators, set up the virtual machine lab environment you will use throughout this course, introduce the SSH client, and finish with a walkthrough of the CompTIA Linux+ XK0-005 exam structure.

By the end of this part, you should have a running Linux virtual machine and understand exactly what you are working toward with this certification.

---

## [SECTION 1 — Why the CLI Matters for Admins — 0:45–3:30]

### The Command Line Is Not Optional

Many students come into this course hoping they will be able to get away with using graphical interfaces for everything. I want to address that directly: for system administration, the command line is not a relic of the past. It is the primary tool of the profession, and for very good reasons.

First, most Linux servers do not have a graphical desktop installed. A server exists to run services efficiently — running a desktop environment wastes CPU, RAM, and attack surface. When you connect to a production server, you get a terminal, period.

Second, automation requires the command line. You cannot script a GUI interaction reliably. Everything repeatable, automated, and scalable in Linux administration — from cron jobs to Ansible playbooks — is built on command-line tools.

Third, the command line is consistent. Graphical interfaces change between distributions, versions, and software updates. The `chmod` command has worked the same way since the 1970s. Skills built on the command line transfer across every Linux distribution and version you will ever use.

Fourth, and most directly relevant to this course: the CompTIA Linux+ exam tests command-line knowledge. Performance-based questions simulate a real terminal. You cannot pass this exam without command-line fluency.

### What Is the Terminal?

The terminal — or terminal emulator — is the application that provides a text interface to the shell. On a Linux desktop, common terminal emulators include GNOME Terminal, Konsole, xterm, and Alacritty. On macOS, the default is Terminal.app. On Windows, you can use Windows Terminal, PuTTY, or the Windows Subsystem for Linux.

When you open a terminal, you are presented with a command prompt. The default bash prompt looks something like this: `username@hostname:~$`. The tilde (`~`) represents your home directory. The dollar sign indicates you are a regular user — a pound sign (`#`) means you are root.

The shell sits inside the terminal and processes everything you type.

---

## [SECTION 2 — Bash as the Default Shell — 3:30–5:30]

### Why Bash

Bash — the Bourne Again Shell — was written by Brian Fox for the GNU Project in 1989. It is the default login shell on most Linux distributions, including Ubuntu and historically RHEL. (Modern RHEL and Fedora default to bash for regular users as well.) Bash is backward-compatible with the original Bourne shell (`sh`) while adding significantly more features.

For this course, every script you write starts with `#!/bin/bash` — the shebang line that tells the kernel which interpreter to use. Every command you run in the terminal will be interpreted by bash.

### Tab Completion and Command History

Two bash features will immediately make you more productive. Tab completion: when you start typing a command or file path and press Tab, bash attempts to complete it. Press Tab twice to see all possible completions. This saves time and prevents typos.

Command history: bash keeps a history of everything you have typed. Press the up arrow to cycle through previous commands. `history` lists your command history with line numbers. `!42` re-runs command number 42. `Ctrl+R` starts a reverse history search — start typing part of a previous command and bash finds it.

These are not optional tricks — they are core productivity skills that you will use in every lab in this course.

---

## [SECTION 3 — SSH Client Basics — 5:30–7:30]

### What Is SSH?

SSH — Secure Shell — is the protocol you will use to connect to remote Linux servers. Before SSH, remote administration was done over Telnet, which transmitted everything including passwords in plain text. SSH encrypts the entire session using public-key cryptography.

From a Linux or macOS terminal, the SSH client is built in. From Windows, the Windows SSH client (built into Windows 10 and later) or PuTTY works well. Windows Terminal with the built-in SSH client is recommended.

### Basic SSH Usage

The basic syntax is: `ssh username@hostname`. For example, `ssh student@192.168.1.100` connects as the user "student" to the machine at that IP address. The first time you connect to a new host, SSH asks you to verify the host's fingerprint — type `yes` to add it to your `~/.ssh/known_hosts` file.

You will need SSH for nearly every lab in this course once we move past the initial VM setup. We cover SSH in depth in a later module, including key-based authentication, which eliminates the need for passwords entirely.

---

## [SECTION 4 — Virtual Machines for Practice — 7:30–11:00]

### Why Virtual Machines

A virtual machine — or VM — is software that simulates a complete computer inside your existing computer. VMs are the standard tool for learning system administration because you can safely experiment, break things, and start over without any risk to your real system or any cost for physical hardware.

For this course, you need a Linux VM. We will use VirtualBox because it is free, cross-platform, and widely supported. VMware Workstation Player is a commercial alternative that also has a free tier for personal use.

### Installing VirtualBox

Download VirtualBox from virtualbox.org — it is free and runs on Windows, macOS, and Linux. The current version as of this course is VirtualBox 7. Install it with default settings. You will also want the VirtualBox Extension Pack for USB 3.0 support and better host-guest integration.

### Downloading Ubuntu Server

For this course we will use Ubuntu Server 22.04 LTS — the Long Term Support release is supported with security updates through 2027. Download the ISO file from ubuntu.com/server. The ISO is approximately 1.4 gigabytes.

### Creating the VM

In VirtualBox, click New. Give the VM a name — "UbuntuServer22" works well. Set the type to Linux and the version to Ubuntu (64-bit). Allocate at least 2 GB of RAM — 4 GB is better if your host machine has 8 GB or more. Create a new virtual hard disk — 20 GB is sufficient for lab work, use the default VDI format.

Before starting the VM, go to Settings → Storage and attach your downloaded Ubuntu Server ISO to the virtual optical drive. Start the VM and it will boot from the ISO.

### Installing Ubuntu Server

The Ubuntu Server installer is text-based. Work through the screens: choose your language, configure the network (DHCP works for most setups), choose the default storage layout (use the entire disk, which is your 20 GB virtual disk), set your username and password, and when offered, install the OpenSSH Server. Let the installation complete — it typically takes 5 to 10 minutes.

After the reboot, remove the ISO from the virtual optical drive and boot from the virtual disk. Log in with the username and password you created.

### Taking Snapshots

One of the most valuable VM features is snapshots. A snapshot saves the exact state of your VM at a moment in time. Before any lab where you might make destructive changes, take a snapshot in VirtualBox: Machine → Take Snapshot. If the lab goes sideways, you can restore the snapshot and start over in seconds. Use snapshots aggressively throughout this course.

---

## [SECTION 5 — CompTIA Linux+ XK0-005 Overview — 11:00–14:00]

### Why This Certification

CompTIA Linux+ is a vendor-neutral Linux administration certification that validates practical, hands-on skills rather than just theoretical knowledge. It is recognized by employers in IT operations, DevOps, cloud administration, and cybersecurity. It serves as both a standalone credential and a stepping stone to more advanced certifications.

### The Four Domains

The XK0-005 exam is organized into four domains:

Domain 1 is System Management, worth 32 percent of the exam. It covers installation, filesystem management, storage (partitioning, LVM, RAID), hardware configuration, process management, service management with systemd, networking, and job scheduling.

Domain 2 is Security, worth 21 percent. It covers file permissions, user and group management, sudo, SSH hardening, firewall configuration (both firewalld and ufw), SELinux and AppArmor, and basic cryptography concepts.

Domain 3 is Scripting, Containers, and Automation, worth 19 percent. It covers bash scripting from variables through functions, text processing with sed and awk, Git basics, Docker containers, and an introduction to Ansible.

Domain 4 is Troubleshooting, worth 28 percent. It covers diagnosing and resolving issues with the boot process, storage, networking, permissions, services, and system performance.

### Exam Format

The exam contains up to 90 questions and is 90 minutes long. Questions are either multiple choice — single or multiple correct answers — or performance-based. Performance-based questions simulate a real terminal environment where you type actual commands to solve problems.

The passing score is 720 out of 900. There is no penalty for guessing.

### How This Course Maps to the Exam

Every module in this course directly covers exam objectives. Module 1 and 2 cover installation and basic navigation (Domain 1). Module 3 covers the filesystem hierarchy (Domain 1). Modules 4 through 6 cover core administration tasks. Modules 7 through 10 cover security topics (Domain 2). Modules 11 and 12 cover scripting and containers (Domain 3). Modules 13 and 14 cover troubleshooting (Domain 4). Module 15 covers storage and advanced administration. Module 16 is dedicated exam preparation and final review.

By the end of this course, you will have covered every major exam objective through hands-on lab work. The certification exam tests the same skills you practice in every lab.

---

## [OUTRO — 14:00–15:00]

You have completed Module 1. Here is your action list before Module 2:

First, download and install VirtualBox from virtualbox.org. Second, download the Ubuntu Server 22.04 LTS ISO from ubuntu.com. Third, create a virtual machine with at least 2 GB RAM and 20 GB disk. Fourth, complete the Ubuntu Server installation and verify you can log in at the command prompt. Fifth, read the Module 1 reading guide and complete the quiz.

The VM you set up today is your lab environment for the entire course. Every command you learn, you will practice in that VM. Take care of it — take snapshots before labs, do not delete it, and treat it like a real server.

In Module 2 we cover the full Linux installation process in depth and start navigating the filesystem. See you there.

---

## [END OF SCRIPT — PART 2]

---

### Instructor Notes

- Estimated delivery time: 14–16 minutes at a measured instructional pace.
- Recommend screen recording the VirtualBox setup and Ubuntu installation rather than describing it verbally — students follow along more effectively with visual demonstration.
- Emphasize snapshot workflow early — students who do not use snapshots struggle with later destructive labs.
- Linux+ exam domain table benefits from a visual slide showing the four domains, weights, and brief descriptions.
