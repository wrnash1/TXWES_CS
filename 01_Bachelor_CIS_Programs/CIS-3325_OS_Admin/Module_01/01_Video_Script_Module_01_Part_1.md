# Video Script: Module 01 - Linux Installation and VM Setup (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to CIS-3325, Operating System Administration. I am Professor Nash, and this is Module 01.
Before we touch a single command, we need to build the mental model that everything else in this
course rests on. This module covers why Linux exists, how it differs from other operating systems,
and how we will use virtual machines as a safe sandbox for every lab in this course.

By the end of both parts of this module you will understand what an operating system kernel does,
how Linux distributions are structured, how to choose and install a distribution, and how to verify
a working installation at the terminal.

---

### Section 1: What an Operating System Actually Does

[SHOW TERMINAL]
Let us start at the bottom.

Your computer is a collection of hardware: a CPU that executes instructions, RAM that holds data
temporarily, storage drives that hold data permanently, a network card, and input-output devices.
None of that hardware knows anything about your word processor or your web browser. Something has
to sit in the middle and translate between application requests and hardware actions. That something
is the operating system kernel.

The kernel performs four primary jobs.

First, process management. Every program you run becomes a process. The kernel decides which process
gets CPU time, for how long, and in what order. This is called scheduling.

Second, memory management. The kernel gives each process its own protected region of RAM and
prevents processes from reading or writing each other's memory. This isolation is why one crashed
program does not crash your entire system.

Third, device management. The kernel includes device drivers that translate generic read and write
calls into the specific commands each hardware device understands. When your browser writes a file,
it does not know or care whether the storage device is a spinning hard drive or an NVMe SSD. The
kernel handles that translation.

Fourth, filesystem management. The kernel presents a unified view of all storage as a tree of
directories and files, regardless of what physical devices or partitions sit underneath.

[SHOW TERMINAL]

```bash
uname -r
```

This command asks the running kernel to report its version number. We will use it in our lab to
confirm a successful installation. Anything you type at a terminal is handled by the kernel through
a system call interface.

---

### Section 2: The Linux Kernel and the GNU Project

Linux is often called an operating system, but technically the name Linux refers only to the kernel,
which was created by Linus Torvalds in 1991 while he was a university student in Finland. Torvalds
released the kernel source code publicly under the GNU General Public License, meaning anyone can
view it, modify it, and distribute their changes.

The commands you actually type at a terminal, tools like ls, cp, mv, and the bash shell itself,
are not part of the Linux kernel. They come from the GNU project, which Richard Stallman began in
1983 with the goal of creating a completely free Unix-like operating system. When you combine the
Linux kernel with GNU utilities and a package manager and a desktop environment, you get what we
properly call a Linux distribution, or distro.

[SHOW TERMINAL]

```bash
ls /usr/bin | head -20
```

Every binary you see here is a GNU utility or third-party application. They call into the Linux
kernel via system calls. The kernel itself lives in /boot.

```bash
ls /boot
```

You will see files like vmlinuz, which is the compressed kernel image, and initrd, the initial RAM
disk used during boot.

---

### Section 3: Linux Distribution Landscape

The exam and the real world both require you to distinguish between major distribution families.

The Debian family is built around the dpkg package format and the apt package manager. Ubuntu,
the most popular desktop Linux distribution, is built on Debian. Ubuntu Server is our primary
lab environment in this course.

The Red Hat family uses RPM packages and the dnf package manager on modern versions. Red Hat
Enterprise Linux, or RHEL, is the dominant enterprise Linux in corporate data centers. CentOS
Stream and Rocky Linux are community rebuilds of RHEL. Fedora is Red Hat's upstream testing ground.

The SUSE family uses the zypper package manager and is common in European enterprises. openSUSE
Leap is the community edition.

For the CompTIA Linux+ exam, you must understand the package management differences between
Debian-based and Red Hat-based systems. We will cover package management in depth in Module 05,
but know now that apt and dnf are the two primary package managers you will be tested on.

---

### Section 4: The Filesystem Hierarchy Standard

One of Linux's most important concepts is the Filesystem Hierarchy Standard, or FHS. Unlike
Windows, which assigns drive letters like C: and D:, Linux presents the entire system as a single
tree rooted at forward slash, which we call root.

[SHOW TERMINAL]

```bash
ls /
```

Let us walk through the most important top-level directories.

The /bin and /usr/bin directories contain executable programs available to all users.

The /sbin and /usr/sbin directories contain system administration binaries typically used by root.

The /etc directory contains all system-wide configuration files. If you change system behavior,
you are almost certainly editing something in /etc.

The /home directory contains personal directories for each user account.

The /var directory contains variable data, meaning data that changes during normal operation.
Log files live in /var/log. Mail spools live in /var/spool.

The /tmp directory holds temporary files that may be cleared on reboot.

The /proc directory is a virtual filesystem generated entirely in memory by the kernel. It contains
real-time information about running processes and hardware configuration. Nothing in /proc is stored
on disk.

The /dev directory contains device files. In Linux, hardware devices are represented as files.
/dev/sda is your first SATA or SCSI disk. /dev/null discards everything written to it.

The /boot directory contains the kernel image and bootloader configuration.

The /mnt and /media directories are conventional mount points for temporarily attached filesystems
like USB drives.

---

### Section 5: Bootloaders and the Boot Process

When you power on a Linux system, a specific sequence of events happens before you see a login
prompt.

The system firmware, either legacy BIOS or modern UEFI, performs a power-on self-test and then
hands control to the bootloader.

GRUB2, the Grand Unified Bootloader version 2, is the standard bootloader on nearly all Linux
distributions. GRUB2 presents a menu if configured to do so, then loads the kernel image from /boot
and the initial RAM disk, called initrd or initramfs.

The kernel initializes hardware, mounts the root filesystem, and then hands control to the init
system. Modern Linux distributions use systemd as the init system. systemd reads unit files and
brings up services in parallel, which is why modern Linux systems boot much faster than older
SysV init systems.

[SHOW TERMINAL]

```bash
systemctl list-units --type=service --state=running | head -20
```

This command shows all currently running systemd services. The entire boot-up sequence brought
each of these services from stopped to running.

---

### Section 6: Partition Schemes - MBR vs GPT

When you install Linux, one of the first decisions is how to partition your disk. There are two
partition table standards.

MBR, the Master Boot Record, is the legacy standard from the early days of IBM PCs. It supports
disks up to 2 terabytes in size and allows a maximum of four primary partitions. If you need more
than four partitions, one must be designated as an extended partition containing logical partitions.
BIOS firmware systems use MBR.

GPT, the GUID Partition Table, is the modern standard. It supports disks up to 9.4 zettabytes,
allows up to 128 primary partitions on Linux, and stores redundant copies of the partition table
at the beginning and end of the disk for reliability. UEFI firmware systems use GPT.

For any new installation on modern hardware, you should use GPT.

[SHOW TERMINAL]

```bash
lsblk
```

This command lists block devices and their partition layout. After installation you will see your
disk divided into partitions. We will run this in the lab to verify our setup.

---

### Section 7: Why Virtual Machines Matter for This Course

Every lab in this course runs inside a virtual machine. There are several important reasons for this
approach.

Safety. If you accidentally delete a system file or corrupt the filesystem, the damage is contained
entirely within the virtual machine. Your host operating system and all your personal files are
completely safe.

Repeatability. Virtual machines can be snapshotted before each major lab exercise. If an exercise
goes wrong, you can restore to a known-good state in seconds rather than reinstalling from scratch.

Real-world skill. The ability to provision, configure, and manage virtual machines is itself a
production skill. Enterprise environments run thousands of virtual machines. Knowing how to work
with them is as important as knowing Linux commands.

---

### Certification Connection

The CompTIA Linux+ XK0-005 exam tests these Module 01 concepts under Domain 1.0, System Management.
Key objectives include:

Understanding Linux architecture including kernel space and user space.

Identifying major distribution families and their associated package managers.

Describing the FHS directory structure and the purpose of key directories.

Understanding the difference between MBR and GPT partition tables.

Describing the role of GRUB2 in the boot process.

---

### Transition to Part 2

In Part 2 we will move into hands-on application. We will walk through setting up VirtualBox,
creating a virtual machine, and performing a full Ubuntu Server installation. I will show you the
exact commands to verify a successful install, and we will preview the lab you will complete this
week.

Take a short break, then continue to Part 2.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
