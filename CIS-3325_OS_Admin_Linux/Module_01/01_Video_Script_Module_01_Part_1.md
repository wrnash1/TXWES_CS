# Video Script: Module 01 — Introduction to Linux and Open Source (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## [INTRO — 0:00–1:00]

Welcome to CIS-3325 OS Administration Linux. I am Professor Nash, and this is Module 1. Over the next two parts of this module, we are going to build the foundation that every single other module in this course depends on. Before you can manage users, before you can configure firewalls, before you can write shell scripts — you need to understand what Linux actually is, where it came from, and why it matters enough that a major professional certification — the CompTIA Linux+ — exists to measure expertise in it.

Part 1 of this module covers Linux history, the philosophy behind open-source software, the relationship between the kernel, the shell, and userspace, and how Linux distributions fit together. Part 2 covers the terminal, your lab environment setup, and the Linux+ exam overview.

Let's get started.

---

## [SECTION 1 — The Origins of Linux — 1:00–4:30]

### Unix: The Ancestor

To understand Linux, you have to start with Unix. Unix was developed at AT&T Bell Labs in 1969 by Ken Thompson and Dennis Ritchie. It was a revolutionary operating system for its time — it was portable, written in the C programming language rather than assembly, and designed around a small set of composable tools. Unix became the dominant operating system in universities and research institutions throughout the 1970s and 1980s.

The philosophy Unix established — small programs that do one thing well, connected through pipes and text — is the same philosophy that Linux inherits and that you will practice every single day as a Linux administrator.

### The GNU Project and the Free Software Foundation

In 1983, a programmer named Richard Stallman at MIT launched the GNU Project. His goal was to create a complete free Unix-like operating system — free not in the sense of price, but free in the sense of freedom. He wanted users to have the freedom to run, study, modify, and distribute the software.

Stallman founded the Free Software Foundation in 1985 and wrote the GNU General Public License — the GPL — which is still one of the most important software licenses in existence. The GNU Project produced many of the core tools we use every day on Linux: GCC (the C compiler), bash (the shell), and hundreds of other utilities. By the early 1990s, GNU had almost everything needed for a complete operating system — except a kernel.

### Minix and the Inspiration for Linux

Minix was a small Unix-like operating system written by professor Andrew Tanenbaum in 1987, intended for educational use. It was designed to demonstrate operating system concepts to students, and it ran on the IBM PC. Minix was important not because it was widely deployed, but because it inspired a Finnish university student named Linus Torvalds.

### Linus Torvalds and the Linux Kernel

In 1991, Linus Torvalds was a 21-year-old student at the University of Helsinki. Frustrated by the limitations of Minix and unable to afford a commercial Unix license, he began writing his own Unix-like kernel. On August 25, 1991, he posted the now-famous message to the comp.os.minix newsgroup: "I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386 AT clones."

That hobby became the Linux kernel. Torvalds released the kernel under the GPL license, which meant that anyone could use, study, modify, and distribute it — but modifications had to be shared back under the same license. This decision was transformative. Within months, developers around the world began contributing. Within years, the Linux kernel was running on servers, workstations, and eventually almost every computing platform on Earth.

The combination of the GNU tools and the Linux kernel is what most people mean when they say "Linux." Technically precise people say "GNU/Linux" to credit both projects, but in common usage "Linux" refers to the full system.

---

## [SECTION 2 — Linux vs. Unix vs. Windows — 4:30–7:00]

### Linux and Unix: What Makes Them Related

Linux is not directly descended from the Unix codebase — it was written from scratch by Torvalds. But it is Unix-like: it follows the same design principles, supports the POSIX standard, and uses most of the same commands and conventions. A Unix administrator can sit down at a Linux terminal and feel immediately at home.

True Unix today includes macOS (which is certified Unix), AIX (IBM), and Solaris (Oracle). Linux is the dominant Unix-like system by market share, running the majority of web servers, cloud infrastructure, supercomputers, and Android devices.

### Linux vs. Windows

Windows and Linux represent fundamentally different philosophies of operating system design. Windows is proprietary — Microsoft owns the source code, and you license the right to use it. Linux is open source — the source code is public, auditable, and modifiable. On Windows, most administration is done through graphical interfaces. On Linux, the command line is the primary administrative interface and is far more powerful.

From a market perspective: Windows dominates the desktop. Linux dominates servers, cloud, and embedded systems. As of 2024, over 90 percent of cloud infrastructure runs on Linux. All of the top 500 supercomputers in the world run Linux. Android — the world's most widely used mobile operating system — is built on a Linux kernel.

For you as a system administrator, this means Linux is not optional knowledge. It is the foundation of modern computing infrastructure.

---

## [SECTION 3 — FOSS Philosophy and Licensing — 7:00–10:00]

### Free and Open Source Software

FOSS stands for Free and Open Source Software. The "free" refers to freedom, not price — the four freedoms articulated by Stallman are: the freedom to run the program for any purpose, the freedom to study how it works and modify it, the freedom to redistribute copies, and the freedom to distribute your modified versions. These freedoms require access to source code.

Open source is a related but slightly different concept — it focuses on the practical benefits of publicly available source code rather than the philosophical freedom argument. In practice, FOSS and open source are used almost interchangeably.

### The GPL

The GNU General Public License — the GPL — is a copyleft license. "Copyleft" is a clever inversion of copyright: instead of restricting what you can do with software, it requires that anything you build using GPL code must also be distributed under the GPL. This is called the "viral" or "share-alike" property. The Linux kernel is licensed under GPL version 2.

The GPL has been enormously influential. It ensured that improvements to the Linux kernel had to be shared back with the community rather than privatized.

### MIT and Apache Licenses

Not all open source licenses are copyleft. The MIT License and the Apache License 2.0 are permissive licenses — they allow you to use, modify, and distribute the software in proprietary products without requiring that your modifications be open sourced. Many popular tools — React, jQuery, Python, Go — use permissive licenses.

For the Linux+ exam, you need to know the basic distinction: GPL is copyleft (share-alike), MIT and Apache are permissive (can be used in proprietary software without sharing back).

---

## [SECTION 4 — Kernel, Shell, and Userspace — 10:00–13:00]

### The Three Layers

Understanding the architecture of a Linux system is essential for everything that follows in this course. There are three conceptual layers: the kernel, the shell, and userspace.

### The Kernel

The kernel is the core of the operating system. It is the first program that loads after the bootloader, and it runs with full hardware access. The kernel manages four fundamental resources: memory (allocating and protecting RAM), processes (creating, scheduling, and terminating programs), hardware devices (through drivers), and the filesystem (reading and writing files).

User programs cannot directly access hardware. They must ask the kernel to do it through a mechanism called system calls — or syscalls. When a program wants to read a file, it makes a syscall. When it wants to allocate memory, it makes a syscall. The kernel validates the request and either performs it or denies it. This separation between user mode and kernel mode is a fundamental security boundary.

The Linux kernel is monolithic — most OS services, including device drivers, run inside kernel space. This is different from a microkernel architecture, where those services run in user space. Monolithic kernels are faster; microkernels are theoretically more stable.

### The Shell

The shell is the command interpreter — the program that reads what you type, parses it, and executes commands. The shell sits between you and the kernel. When you type `ls -la`, the shell parses that command, finds the `ls` executable, passes `-la` as an argument, and starts a new process to run it.

There are many shells: `sh` (the original Bourne shell), `bash` (Bourne Again Shell — the most common on Linux), `zsh` (Z shell — the macOS default since Catalina), `ksh` (Korn Shell), and `fish` (Friendly Interactive Shell). For this course and for the Linux+ exam, bash is the standard. Every script we write will use bash.

### Userspace

Userspace is everything that runs outside the kernel — all the applications, services, utilities, and tools. This includes the shell itself, text editors, web servers, databases, and the graphical desktop environment. Userspace programs run with restricted privileges and communicate with the kernel through syscalls.

The distinction matters for administration. When a service fails, you need to understand whether the problem is in the application code, the kernel interaction, or the hardware itself.

---

## [SECTION 5 — Linux Distributions — 13:00–15:00]

### What Is a Distribution?

A Linux distribution — or "distro" — is a complete, packaged operating system built on the Linux kernel plus a collection of software. The kernel alone is not a usable system — you need a package manager, a desktop environment or server tooling, default configuration, and a software repository. Distributions make those choices and package everything together.

There are hundreds of Linux distributions. For the Linux+ exam and for this course, you need to know the major families.

### The Debian Family

Debian is one of the oldest Linux distributions, founded in 1993. Its descendant Ubuntu is the most popular Linux distribution for desktops and cloud servers. Debian-family distributions use the `apt` package manager and `.deb` package files. Ubuntu comes in Server and Desktop editions — we will primarily use Ubuntu Server in this course.

### The RHEL Family

Red Hat Enterprise Linux (RHEL) is the dominant Linux distribution in enterprise environments. It is commercial software — Red Hat (now part of IBM) charges for support subscriptions. CentOS was a free rebuild of RHEL source code; it was discontinued in 2021 and replaced by CentOS Stream (a rolling upstream of RHEL) and Rocky Linux / AlmaLinux (community RHEL rebuilds). RHEL-family distributions use the `dnf` or `yum` package manager and `.rpm` package files.

The CompTIA Linux+ exam tests both Debian-family and RHEL-family commands. You must know both.

### Arch Linux

Arch Linux is a rolling-release distribution targeted at experienced users. It follows a "do it yourself" philosophy — you build the system from the ground up. It uses the `pacman` package manager. Arch's rolling release means you always have the latest software versions rather than waiting for a major release cycle.

### Kali Linux

Kali Linux is a Debian-based distribution built for penetration testing and security research. It comes preinstalled with hundreds of security tools. It is not intended for general-purpose use or as a learning environment for beginners — if you run Kali as your daily driver, you are doing it wrong. Use Ubuntu or a RHEL variant for learning.

### Alpine Linux

Alpine Linux is an extremely lightweight distribution — a minimal Alpine container image is only about 5 megabytes. It is built around the `musl` C library and `busybox` and is widely used as the base image for Docker containers because of its small size and security-focused design.

---

## [OUTRO — 15:00]

That wraps up Part 1 of Module 1. You now have the historical and conceptual foundation: where Linux came from, why open-source licensing matters, how the kernel and shell relate to each other, and how the major distribution families differ.

In Part 2, we move from theory to practice. We will talk about the Linux terminal, set up your lab environment, and look at the CompTIA Linux+ exam structure in detail. See you there.

---

## [END OF SCRIPT — PART 1]

---

### Instructor Notes

- Estimated delivery time: 14–16 minutes at a measured instructional pace.
- Consider showing a timeline graphic during Section 1 — 1969 (Unix), 1983 (GNU), 1991 (Linux kernel).
- The distribution family comparison benefits from a visual table on screen: Family / Package Manager / Package Format / Key Distros.
- This content maps to Linux+ Objective 1.1 (Linux filesystem hierarchy) and general exam prerequisite knowledge.
