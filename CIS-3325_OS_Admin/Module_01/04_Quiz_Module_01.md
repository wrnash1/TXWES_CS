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
