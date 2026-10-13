# Quiz: Module 01 - Linux Installation and VM Setup

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

Which of the following describes a Type 1 hypervisor?

- A) It runs as an application on top of an existing host operating system like Windows 10.
- B) It runs directly on the server's bare-metal hardware.
- C) It cannot run Linux virtual machines.
- D) It requires Oracle VirtualBox to function.

Correct Answer: B) It runs directly on the server's bare-metal hardware.

Distractor Analysis:

- Why A is incorrect: This describes a Type 2 hypervisor (hosted), not Type 1. VirtualBox and VMware Workstation are Type 2 examples.
- Why C is incorrect: Type 1 hypervisors can run almost any supported OS, including Linux.
- Why D is incorrect: VirtualBox is itself a Type 2 hypervisor. Type 1 examples include VMware ESXi and Microsoft Hyper-V Server.

---

**Question 2**

What is the primary function of an operating system's kernel?

- A) To provide a graphical desktop environment and window manager for the user.
- B) To compile source code written in C into executable ELF binaries.
- C) To manage hardware resources and act as a bridge between applications and the underlying hardware.
- D) To store user documents and run web browsers in isolated containers.

Correct Answer: C) To manage hardware resources and act as a bridge between applications and the underlying hardware.

Distractor Analysis:

- Why A is incorrect: The desktop environment (GNOME, KDE) is a user-space application layered on top of the kernel, not part of the kernel itself.
- Why B is incorrect: Compiling source code is the role of a compiler such as GCC, not the OS kernel.
- Why D is incorrect: Web browsers and document storage applications run in user space. The kernel provides them system calls but does not run them directly.

---

**Question 3**

A systems administrator needs to verify which Linux kernel version is currently running on a freshly installed virtual machine. Which command should they use?

- A) uname -r
- B) df -h
- C) lsblk
- D) chmod 600 /etc/os-release

Correct Answer: A) uname -r

Distractor Analysis:

- Why B is incorrect: df -h reports disk space usage on mounted filesystems, not kernel version.
- Why C is incorrect: lsblk lists block devices and partition layout, not kernel information.
- Why D is incorrect: chmod 600 changes file permissions. /etc/os-release contains distro name and version, not the running kernel version.

---

**Question 4**

A student installs Ubuntu in VirtualBox but the screen resolution stays small and copy-paste between the host and guest does not work. What is the most likely solution?

- A) Reinstall the Linux kernel from source.
- B) Install VirtualBox Guest Additions inside the guest VM.
- C) Switch from a Type 2 to a Type 1 hypervisor.
- D) Reformat the virtual disk using GPT instead of MBR.

Correct Answer: B) Install VirtualBox Guest Additions inside the guest VM.

Distractor Analysis:

- Why A is incorrect: Compiling a custom kernel does not add VirtualBox display or clipboard integration drivers.
- Why C is incorrect: VirtualBox is inherently a Type 2 hypervisor. Switching hypervisor type does not resolve guest integration features.
- Why D is incorrect: The partition table format affects boot and storage layout, not screen resolution or clipboard sharing.

---

**Question 5**

When preparing a Linux server for a production environment, a junior administrator installs the full GNOME desktop environment by default. A senior administrator says this violates hardening best practices. Which of the following best explains why?

- A) GNOME is incompatible with the Linux kernel on UEFI systems.
- B) Desktop environments require GPT partition tables, which cannot be used on servers.
- C) Unnecessary software packages increase the attack surface by introducing additional services and potential vulnerabilities.
- D) A graphical interface prevents administrators from using SSH to connect remotely.

Correct Answer: C) Unnecessary software packages increase the attack surface by introducing additional services and potential vulnerabilities.

Distractor Analysis:

- Why A is incorrect: GNOME is fully compatible with UEFI systems. This is a fabricated incompatibility.
- Why B is incorrect: Desktop environments have no dependency on GPT versus MBR.
- Why D is incorrect: SSH operates independently of the graphical environment. The hardening concern is about unneeded software, not SSH access.

---

**Question 6**

An administrator needs to make the GRUB2 bootloader regenerate its configuration file on an Ubuntu 22.04 server after editing /etc/default/grub. Which command is correct?

- A) grub2-mkconfig -o /boot/grub2/grub.cfg
- B) update-grub
- C) grub-install /dev/sda
- D) systemctl restart grub2

Correct Answer: B) update-grub

Distractor Analysis:

- Why A is incorrect: grub2-mkconfig with that exact path is the RHEL/CentOS command. On Ubuntu/Debian systems, update-grub is the correct wrapper command.
- Why C is incorrect: grub-install installs the GRUB bootloader onto a disk's MBR or EFI partition. It is used during initial setup or repair, not for regenerating the config file after editing /etc/default/grub.
- Why D is incorrect: There is no grub2 systemd service. GRUB runs at boot time, before systemd. This command would fail with a unit-not-found error.

---

**Question 7**

A system administrator creates a new 3 TB disk to add storage to a Linux server. Which partition table standard must be used, and why?

- A) MBR, because it is compatible with all Linux distributions.
- B) GPT, because MBR cannot address disks larger than 2 TB.
- C) MBR, because GPT requires a special filesystem format.
- D) GPT, but only if the server uses a GNOME desktop environment.

Correct Answer: B) GPT, because MBR cannot address disks larger than 2 TB.

Distractor Analysis:

- Why A is incorrect: While MBR is compatible with many Linux distributions, it cannot address disks larger than 2 TB due to its 32-bit LBA addressing limitation. Compatibility is irrelevant when the disk size exceeds MBR's ceiling.
- Why C is incorrect: GPT does not require any special filesystem format. ext4, XFS, and other standard Linux filesystems all work on GPT partitions.
- Why D is incorrect: The partition table choice has nothing to do with the desktop environment. GPT is required for any disk larger than 2 TB regardless of whether a GUI is installed.

---

**Question 8**

An administrator runs `cat /proc/cpuinfo` and receives output showing CPU information. Which statement best describes why /proc/cpuinfo exists?

- A) /proc/cpuinfo is a text file written by the CPU manufacturer during hardware assembly.
- B) /proc is a virtual filesystem generated by the kernel in RAM, and cpuinfo is a kernel-generated view of processor information.
- C) /proc/cpuinfo is updated by the package manager whenever the kernel is upgraded.
- D) /proc/cpuinfo is a log file written by the BIOS during the POST sequence.

Correct Answer: B) /proc is a virtual filesystem generated by the kernel in RAM, and cpuinfo is a kernel-generated view of processor information.

Distractor Analysis:

- Why A is incorrect: /proc is generated by the running Linux kernel at runtime. It has nothing to do with CPU manufacturers or hardware assembly.
- Why C is incorrect: The package manager has no involvement with /proc. The package manager installs and removes software packages. /proc content is generated dynamically by the kernel.
- Why D is incorrect: BIOS/UEFI writes no data to /proc. The BIOS performs POST before the kernel even loads. /proc is populated by the kernel after it takes control of the system.

---

**Question 9**

Which directory in the FHS contains the system-wide configuration files for installed services and applications?

- A) /var
- B) /usr/local
- C) /etc
- D) /srv

Correct Answer: C) /etc

Distractor Analysis:

- Why A is incorrect: /var contains variable runtime data such as logs (/var/log), mail spools (/var/spool), and databases. It does not contain configuration files.
- Why B is incorrect: /usr/local contains locally compiled and installed software binaries and libraries, not system-wide configuration files. Configuration for software in /usr/local typically goes in /etc/local or a service-specific /etc subdirectory.
- Why D is incorrect: /srv contains data served by system services such as web content (/srv/www) or FTP data. It is not for configuration files.

---

**Question 10**

After installing Ubuntu Server 22.04 in VirtualBox, an administrator runs `systemctl status ssh` and sees the status as "inactive (dead)." The administrator needs SSH to start automatically on every boot. Which two commands accomplish this?

- A) service ssh start && chkconfig ssh on
- B) systemctl start ssh && systemctl enable ssh
- C) /etc/init.d/ssh start && update-rc.d ssh defaults
- D) systemctl enable ssh && reboot

Correct Answer: B) systemctl start ssh && systemctl enable ssh

Distractor Analysis:

- Why A is incorrect: chkconfig is a legacy SysV init tool not available on modern Ubuntu systems that use systemd. While service ssh start may work as a compatibility wrapper, chkconfig ssh on will fail on Ubuntu 22.04.
- Why C is incorrect: /etc/init.d/ scripts and update-rc.d are SysV init mechanisms. While Ubuntu maintains limited SysV compatibility, the current standard tool for managing services is systemctl. This approach is deprecated and non-standard.
- Why D is incorrect: systemctl enable alone marks the service to start at boot but does not start it immediately. A reboot would start it, but the combination of enable followed by rebooting wastes time unnecessarily. The correct approach is enable (for future boots) plus start (for immediate effect) without rebooting.

---

*Questions 11–20 — 5 pts each*

---

**Question 11**

An administrator needs to display all PCI devices detected by the Linux kernel, such as network adapters and storage controllers, in a human-readable list. Which command is most appropriate?

- A) dmesg | grep PCI
- B) lspci
- C) cat /proc/devices
- D) lsusb

Correct Answer: B) lspci

Distractor Analysis:

- Why A is incorrect: dmesg | grep PCI shows boot-time kernel messages mentioning PCI, but it is a log viewer rather than a structured device listing tool. The output is verbose and difficult to parse compared to lspci.
- Why C is incorrect: /proc/devices lists major device numbers registered with the kernel, not human-readable hardware model names or PCI identifiers.
- Why D is incorrect: lsusb lists USB devices only. PCI devices such as network cards and SATA controllers require lspci.

---

**Question 12**

On a modern Ubuntu 22.04 system, the /bin directory is a symbolic link to /usr/bin. Which initiative introduced this change and why?

- A) The POSIX hardening standard, to prevent PATH hijacking attacks.
- B) The usr-merge initiative, which consolidates essential and non-essential binaries under /usr to simplify filesystem layout and enable atomic system upgrades.
- C) The systemd project, which requires all binaries to reside in /usr/bin for unit file compatibility.
- D) The FHS 4.0 standard, which deprecated /bin to reduce inode usage.

Correct Answer: B) The usr-merge initiative, which consolidates essential and non-essential binaries under /usr to simplify filesystem layout and enable atomic system upgrades.

Distractor Analysis:

- Why A is incorrect: POSIX and PATH hardening are separate topics. The usr-merge has nothing to do with security controls against PATH hijacking.
- Why C is incorrect: systemd unit files reference binaries by absolute path but do not require all binaries to live in /usr/bin. systemd works with both /bin and /usr/bin paths.
- Why D is incorrect: FHS 4.0 does not deprecate /bin. The usr-merge is a distribution-level implementation decision, not an FHS mandate.

---

**Question 13**

Which command displays the UUID and filesystem type of all block devices on the system, which is essential for writing correct /etc/fstab entries?

- A) fdisk -l
- B) lsblk -f
- C) parted -l
- D) mount | column -t

Correct Answer: B) lsblk -f

Distractor Analysis:

- Why A is incorrect: fdisk -l shows partition table details (sectors, sizes, types) but does not display filesystem UUIDs. UUIDs are attributes of the filesystem written on the partition, not of the partition table entry.
- Why C is incorrect: parted -l shows partition layout and filesystem type hints but does not display UUIDs. UUIDs are retrieved by blkid or lsblk -f.
- Why D is incorrect: mount shows currently mounted filesystems and their options, but not the UUID of unmounted partitions. An unmounted partition would not appear in mount output.

---

**Question 14**

An administrator reviews /etc/fstab and finds the following entry:

UUID=dead-beef /scratch ext4 defaults,noexec,nosuid 0 2

What does the nosuid mount option accomplish?

- A) Prevents any user from creating new files in the /scratch directory.
- B) Prevents SUID and SGID bits on files within the mounted filesystem from taking effect, blocking privilege escalation via those files.
- C) Prevents the filesystem from being mounted at boot time.
- D) Prevents root from logging in through the console when /scratch is mounted.

Correct Answer: B) Prevents SUID and SGID bits on files within the mounted filesystem from taking effect, blocking privilege escalation via those files.

Distractor Analysis:

- Why A is incorrect: nosuid has no effect on file creation or write access. The rw/ro mount option or Unix permissions govern whether users can create files.
- Why C is incorrect: The noauto mount option prevents a filesystem from mounting at boot. nosuid is a runtime security option that applies after the filesystem is already mounted.
- Why D is incorrect: nosuid is a per-filesystem mount option affecting SUID/SGID execution. It has no relationship to console login restrictions, which are controlled by PAM and /etc/securetty.

---

**Question 15**

A systems administrator needs to display total and available RAM in megabytes without installing additional tools. Which command provides this output?

- A) free -m
- B) vmstat -m
- C) ps aux --sort=-%mem | head
- D) top -o %MEM

Correct Answer: A) free -m

Distractor Analysis:

- Why A is correct: The -m flag tells free to display memory values in megabytes, showing total, used, free, shared, buff/cache, and available columns.
- Why B is incorrect: vmstat -m on Linux means "display memory slab statistics" in some implementations, not a simple total/free summary. The -m flag behavior differs between vmstat and free.
- Why C is incorrect: ps aux sorts processes by memory percentage. It shows per-process RSS values, not system-wide total/available RAM.
- Why D is incorrect: top -o %MEM sorts the process list by memory usage but does not simply display total and available RAM as a summary. It requires additional navigation to read the memory header line.

---

**Question 16**

Which systemd target is equivalent to the traditional SysV runlevel 5 (multi-user mode with graphical interface)?

- A) multi-user.target
- B) graphical.target
- C) runlevel5.target
- D) Both B and C

Correct Answer: D) Both B and C

Distractor Analysis:

- Why A is incorrect: multi-user.target is equivalent to SysV runlevel 3 (multi-user without graphical interface). It starts all services but not the display manager.
- Why B alone is partially correct: graphical.target is the correct systemd target for runlevel 5. It depends on multi-user.target and adds the display manager.
- Why C alone is partially correct: runlevel5.target is a compatibility symlink that points to graphical.target. Both names resolve to the same target.

---

**Question 17**

An administrator wants to change the system hostname to lab-server-01 on Ubuntu 22.04 so the change survives reboots. Which command is correct?

- A) hostname lab-server-01
- B) sysctl -w kernel.hostname=lab-server-01
- C) hostnamectl set-hostname lab-server-01
- D) echo lab-server-01 > /proc/sys/kernel/hostname

Correct Answer: C) hostnamectl set-hostname lab-server-01

Distractor Analysis:

- Why A is incorrect: The hostname command sets the transient hostname for the current session only. It does not write to /etc/hostname and the change is lost at the next reboot.
- Why B is incorrect: sysctl -w kernel.hostname changes the running kernel's hostname in memory but does not persist across reboots, as /proc/sys/kernel/hostname is not a persistent storage location.
- Why D is incorrect: Writing directly to /proc/sys/kernel/hostname changes the kernel hostname temporarily (same effect as option B or A) but does not persist. /proc is a virtual filesystem in RAM.

---

**Question 18**

After a suspected intrusion, an administrator wants to verify that the ssh binary on a Debian-based system has not been replaced. Which command checks the installed file's checksum against the package manager's database?

- A) sha256sum /usr/bin/ssh
- B) dpkg --verify openssh-client
- C) ls -la /usr/bin/ssh
- D) file /usr/bin/ssh

Correct Answer: B) dpkg --verify openssh-client

Distractor Analysis:

- Why A is incorrect: sha256sum computes a checksum of the file, but without a trusted reference value to compare against, the output alone is meaningless as a verification step. An attacker could replace the binary and its hash baseline simultaneously.
- Why C is incorrect: ls -la shows permissions, ownership, and timestamps. These attributes can be easily forged by an attacker using the touch command. They provide no cryptographic integrity assurance.
- Why D is incorrect: The file command identifies binary type (ELF, shell script, etc.) by magic bytes. A replacement malicious binary would still be an ELF file. This check does not verify content integrity.

---

**Question 19**

The Linux kernel writes messages to an in-memory ring buffer during boot and at runtime. Which command reads the most recent kernel messages from this buffer?

- A) journalctl -k
- B) dmesg
- C) cat /var/log/kern.log
- D) Both A and B

Correct Answer: D) Both A and B

Distractor Analysis:

- Why A alone is partially correct: journalctl -k (or --dmesg) shows kernel messages stored in the systemd journal, which is sourced from the same kernel ring buffer data.
- Why B alone is partially correct: dmesg reads directly from the kernel ring buffer (/dev/kmsg or the ring buffer syscall). Both commands display kernel messages and are correct.
- Why C is incorrect: /var/log/kern.log is a syslog-written log file on Debian/Ubuntu systems. While it contains kernel messages forwarded by rsyslog, it is a secondary copy, not the primary ring buffer. It also does not exist on all distributions.

---

**Question 20**

An administrator runs efibootmgr -v on a server and sees multiple boot entries. What type of firmware is confirmed to be present on this system?

- A) BIOS (Basic Input/Output System) legacy firmware
- B) UEFI (Unified Extensible Firmware Interface) firmware
- C) Coreboot open-source firmware
- D) iPXE network boot firmware

Correct Answer: B) UEFI (Unified Extensible Firmware Interface) firmware

Distractor Analysis:

- Why A is incorrect: BIOS firmware does not support UEFI NVRAM boot variables. The efibootmgr tool communicates with the EFI runtime services interface, which exists only on UEFI systems. Running efibootmgr on a BIOS system returns an error.
- Why C is incorrect: Coreboot is an alternative open-source firmware implementation. Some Coreboot builds do implement UEFI interfaces (via TianoCore payload), but the presence of efibootmgr output specifically confirms UEFI runtime services are available, not Coreboot specifically.
- Why D is incorrect: iPXE is a network boot protocol stack, not system firmware. iPXE operates after the firmware initializes the system and is unrelated to efibootmgr's NVRAM interface.
