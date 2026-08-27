# Reading Guide: Module 01 - Linux Installation and VM Setup

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 01. This reading guide expands on the video lecture and provides the reference
material you will need for the quiz, the lab, and the CompTIA Linux+ exam. Read this guide after
watching both video parts and before starting the lab.

This module covers Linux architecture, distribution selection, virtual machine setup, disk
partitioning, and post-installation verification. These foundational topics appear throughout the
entire Linux+ exam, not just in the installation objectives.

---

### 1. High-Yield Glossary

Study these definitions carefully. Each term has appeared on the Linux+ exam.

**Kernel:** The core component of the operating system that runs in privileged mode and manages
hardware resources, process scheduling, memory allocation, and device drivers. All user programs
communicate with hardware through kernel system calls.

**User Space:** The memory region where application processes run. User-space programs cannot
directly access hardware. They must request hardware access through kernel system calls.

**Kernel Space:** The protected memory region where the kernel runs. Code in kernel space has
unrestricted access to hardware. A kernel panic occurs when kernel-space code encounters an
unrecoverable error.

**Type 1 Hypervisor (Bare-Metal):** A hypervisor that runs directly on physical server hardware
without an underlying host OS. Examples include VMware ESXi, Microsoft Hyper-V (Server), and
KVM when used as the primary host. Type 1 provides lower latency and better performance than
Type 2 in production environments.

**Type 2 Hypervisor (Hosted):** A hypervisor that runs as an application on top of an existing
host operating system. VirtualBox and VMware Workstation are Type 2. Because the host OS mediates
all hardware access, Type 2 hypervisors have higher overhead but are simpler to set up on a
personal laptop.

**Linux Distribution (Distro):** A packaged combination of the Linux kernel, GNU utilities, a
package manager, an init system, and bundled software assembled by a community or company. Each
distro makes different choices about default software, release cadence, and support model.

**Debian Family:** Distributions using the dpkg/.deb package format and the apt package manager.
Includes Debian, Ubuntu, Linux Mint, and Kali Linux. Ubuntu 22.04 LTS is the lab environment
for this course.

**Red Hat Family:** Distributions using the RPM package format and the dnf (or yum) package
manager. Includes RHEL, CentOS Stream, Rocky Linux, AlmaLinux, and Fedora.

**SUSE Family:** Distributions using RPM packages and the zypper package manager. Includes
SUSE Linux Enterprise Server (SLES) and openSUSE.

**Filesystem Hierarchy Standard (FHS):** The standard defining the directory structure and
directory contents in Linux and Unix-like operating systems. All Linux distributions follow
the FHS, ensuring consistent paths for system files across distros.

**MBR (Master Boot Record):** Legacy partition table format. Supports disks up to 2 TB and
a maximum of 4 primary partitions. Used with legacy BIOS firmware.

**GPT (GUID Partition Table):** Modern partition table format. Supports disks up to 9.4 ZB
and up to 128 partitions on Linux. Stores redundant partition tables at disk beginning and end.
Required for UEFI firmware and for disks larger than 2 TB.

**GRUB2 (Grand Unified Bootloader version 2):** The standard Linux bootloader. Presents a boot
menu, loads the selected kernel and initramfs from /boot, and transfers control to the kernel.
Configuration file: /boot/grub/grub.cfg (auto-generated; do not edit directly).

**initramfs / initrd:** A temporary root filesystem loaded into RAM during boot before the
actual root filesystem is mounted. Contains the minimum drivers and tools needed to mount the
real root filesystem.

**systemd:** The modern init system used by all major Linux distributions. PID 1 on a systemd
system. Manages service startup, dependencies, and system state targets in parallel.

**VirtualBox Guest Additions:** A package installed inside a guest VM that enables enhanced
host-guest integration: shared clipboard, dynamic screen resolution, shared folders, and
seamless mouse integration.

---

### 2. FHS Directory Reference

| Directory | Purpose | Exam Notes |
|-----------|---------|------------|
| / | Root of the entire filesystem tree | Everything mounts under root |
| /bin | Essential user binaries (ls, cp, mv) | Symlinked to /usr/bin on modern distros |
| /sbin | System binaries for root (fdisk, iptables) | Symlinked to /usr/sbin on modern distros |
| /etc | System-wide configuration files | Never holds executables or data |
| /home | User home directories | One subdirectory per user account |
| /root | Home directory for the root user | NOT inside /home |
| /var | Variable data: logs, spools, databases | /var/log for logs; /var/spool for queues |
| /tmp | Temporary files; may be cleared on reboot | World-writable with sticky bit |
| /proc | Virtual FS: running processes and kernel data | Nothing stored on disk |
| /sys | Virtual FS: kernel hardware/driver info | Newer than /proc; structured hierarchy |
| /dev | Device files (disks, terminals, null) | /dev/sda = first SCSI/SATA disk |
| /boot | Kernel image, initramfs, GRUB config | Required to be accessible at boot |
| /lib | Shared libraries for /bin and /sbin | /lib64 for 64-bit libraries |
| /usr | Secondary hierarchy: most user programs | /usr/bin, /usr/lib, /usr/share |
| /usr/local | Locally installed software (not from package manager) | Admin-managed software |
| /opt | Optional add-on application packages | Third-party apps (e.g., /opt/splunk) |
| /mnt | Manual mount points for temporary filesystems | Admin-chosen; not auto-mounted |
| /media | Auto-mount points for removable media | USB drives, DVDs |
| /srv | Data served by system services | Web content, FTP data |
| /run | Runtime data for current boot | Cleared on reboot; PID files |

---

### 3. Key Commands - Installation Verification

| Command | Purpose | Example Output |
|---------|---------|----------------|
| `uname -r` | Show kernel version | 5.15.0-91-generic |
| `uname -a` | Show all system information | Linux hostname 5.15.0... x86_64 GNU/Linux |
| `cat /etc/os-release` | Show distro name and version | Ubuntu 22.04 LTS |
| `lsblk` | List block devices and partitions | sda, sda1, sda2 with mount points |
| `df -h` | Show disk space usage per filesystem | /, /boot/efi with sizes |
| `ip addr show` | Show network interface addresses | lo and ens33 with IP addresses |
| `systemctl status ssh` | Show SSH service status | active (running) |
| `hostname` | Show the system hostname | ubuntu-server |
| `whoami` | Show current username | labadmin |
| `id` | Show current user UID, GID, and groups | uid=1000(labadmin) gid=1000(labadmin) |

---

### 4. Hypervisor Comparison

| Feature | Type 1 (Bare-Metal) | Type 2 (Hosted) |
|---------|---------------------|-----------------|
| Runs on | Physical hardware directly | On top of a host OS |
| Examples | VMware ESXi, Hyper-V Server, KVM | VirtualBox, VMware Workstation |
| Performance | Higher (less overhead) | Lower (host OS mediates hardware) |
| Setup complexity | Higher (dedicated server) | Lower (install like any application) |
| Use case | Production data centers | Development, learning, testing |
| Isolation | Complete hardware isolation | Shares host OS resources |

---

### 5. Partition Table Comparison

| Feature | MBR | GPT |
|---------|-----|-----|
| Max disk size | 2 TB | 9.4 ZB |
| Max primary partitions | 4 | 128 (Linux) |
| Firmware type | BIOS | UEFI |
| Redundancy | None | Backup table at disk end |
| Boot partition | Boot code in MBR sector | EFI System Partition (ESP) |
| 2 TB+ disks | Not supported | Supported |
| Modern recommendation | Legacy only | Yes, for all new installs |

---

### 6. Distribution Family Quick Reference

| Family | Package Format | Package Manager | Config Tool | Example Distros |
|--------|---------------|-----------------|-------------|-----------------|
| Debian | .deb | apt, dpkg | dpkg-reconfigure | Ubuntu, Debian, Kali |
| Red Hat | .rpm | dnf (yum legacy) | system-config-* | RHEL, Rocky, Fedora |
| SUSE | .rpm | zypper | YaST | SLES, openSUSE |
| Arch | .pkg.tar.zst | pacman | - | Arch Linux, Manjaro |
| Alpine | .apk | apk | - | Alpine Linux (containers) |

---

### 7. GRUB2 Key Facts

The GRUB2 configuration file is /boot/grub/grub.cfg on Debian/Ubuntu systems and
/boot/grub2/grub.cfg on RHEL-based systems. Never edit this file directly. It is auto-generated.

To regenerate GRUB configuration on Ubuntu/Debian:

```bash
sudo update-grub
```

To regenerate GRUB configuration on RHEL/CentOS:

```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

The source file that update-grub and grub2-mkconfig read is /etc/default/grub. Edit this file
to change GRUB timeout, default boot entry, or kernel parameters.

---

### 8. Minimal Install Security Rationale

CompTIA Linux+ exam questions frequently ask why a minimal server install is preferred over a
full desktop install. The answer is attack surface reduction.

Every installed package is a potential vector for:

- Known vulnerabilities in that software's code
- Misconfigured services that open unexpected network ports
- Unnecessary processes consuming CPU and memory
- Additional files that could be modified by an attacker

A minimal Ubuntu Server install with only OpenSSH installed has far fewer running processes and
listening ports than a full GNOME desktop install. Hardening documentation from CIS (Center for
Internet Security) and DISA (Defense Information Systems Agency) explicitly recommends minimal
installs as a baseline security control.

---

### 9. CompTIA Linux+ Exam Tips

**Exam Tip 1:** Hypervisor type questions are among the most frequently tested installation topics.
Remember the mnemonic: "Bare metal = Type 1." VirtualBox is always Type 2 because you install it
on Windows or macOS first.

**Exam Tip 2:** Know both GRUB2 config commands. Ubuntu uses update-grub. RHEL uses
grub2-mkconfig. If the question mentions /etc/default/grub, both platforms read that file as
the source of GRUB settings.

**Exam Tip 3:** MBR versus GPT: if the question mentions a disk larger than 2 TB, the answer is
always GPT. If the question mentions UEFI firmware, the answer is GPT.

**Exam Tip 4:** The /proc filesystem is virtual and held entirely in RAM. Nothing in /proc is
written to disk. This is a common distractor on questions about where log files or configuration
files are stored.

**Exam Tip 5:** uname -r reports the kernel release version. uname -a reports all information.
cat /etc/os-release reports the distribution version. Know which command answers which question.

**Exam Tip 6:** The exam distinguishes between a minimal install (CLI only) and a full desktop
install. For a hardened production server, the correct answer is always a minimal install with
only required packages added afterward.

**Exam Tip 7:** VirtualBox Guest Additions are installed inside the guest VM, not on the host.
They require a compatible kernel version; the package is virtualbox-guest-additions-iso on Ubuntu.

**Exam Tip 8:** Partitioning for security means separate partitions for /home, /var, /tmp, and
sometimes /boot. Separate /tmp prevents a tmp-fill attack from crashing other services. Separate
/var prevents log flooding from filling the root partition.

---

### 10. Study Checklist

- [ ] Watch both parts of the Module 01 video lecture
- [ ] Memorize all glossary terms and their definitions
- [ ] Review the FHS directory reference table and understand each directory's purpose
- [ ] Understand Type 1 vs Type 2 hypervisor differences
- [ ] Understand MBR vs GPT partition table differences
- [ ] Know the GRUB2 config regeneration command for both Ubuntu and RHEL
- [ ] Know all six post-installation verification commands and what each one shows
- [ ] Complete the Module 01 Lab (VirtualBox VM creation and Ubuntu Server installation)
- [ ] Complete the Module 01 Quiz (10 questions)
- [ ] Post your initial response to the Module 01 Discussion by Wednesday at 11:59 PM
- [ ] Reply to at least two classmates in the Discussion by Sunday at 11:59 PM

---

### Required Reading

Read chapters 1 through 2 of the free OER textbook The Linux Command Line by William Shotts,
available at linuxcommand.org/tlcl.php. These chapters cover shell basics and how the Linux
environment is structured after installation.

---

### Required Video Supplement

Review CompTIA Linux+ study materials at professormesser.com for additional coverage of
installation and hardware topics aligned to the XK0-005 exam objectives.

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts covered in this module. All
links are Zero Textbook Cost (ZTC) and do not require login or purchase.

**1. The Linux Command Line — William Shotts (Chapter 1 & 2)**
URL: https://linuxcommand.org/tlcl.php
Coverage: Shell basics, filesystem navigation, and Linux environment overview. Read after
completing the lab to reinforce the FHS directory structure and command-line fundamentals.

**2. Linux man pages online — kernel.org**
URL: https://www.kernel.org/doc/man-pages/
Coverage: Authoritative reference for every system call, library function, and standard
command described in this module. Key pages: man 1 uname, man 8 fdisk, man 8 grub-install,
man 5 fstab. Use this as your primary reference when lab commands produce unexpected output.

**3. The Linux Documentation Project (TLDP) — Linux Installation HOWTO**
URL: https://tldp.org/HOWTO/Installation-HOWTO/
Coverage: Detailed walkthrough of Linux installation scenarios including disk partitioning
decisions, bootloader configuration, and post-install verification steps. Complements the
lab procedures in this module.

**4. Red Hat Customer Portal — Understanding systemd targets**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/working-with-systemd-targets_configuring-basic-system-settings
Coverage: Explains systemd targets and their SysV runlevel equivalents. Essential background
for understanding why modern Linux systems no longer use /etc/inittab.

**5. ArchWiki — GRUB**
URL: https://wiki.archlinux.org/title/GRUB
Coverage: The most comprehensive freely available GRUB2 reference. Covers BIOS vs UEFI
installation, grub.cfg generation, kernel parameters, and rescue procedures. Distribution-
agnostic and kept current by the Arch Linux community.
