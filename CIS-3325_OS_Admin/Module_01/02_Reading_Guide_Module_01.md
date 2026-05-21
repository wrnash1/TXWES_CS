# Reading Guide: Module 01 - Linux Installation and VM Setup
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 01 – Linux Installation and VM Setup**! This week covers the foundational skills of selecting a Linux distribution, performing an installation, and working inside a virtual machine environment using VirtualBox. These skills underpin every subsequent module and align directly with the CompTIA Linux+ XK0-005 domain covering system management and hardware configuration.

As you work through this material you will learn how virtual machines isolate operating system instances from host hardware, how disk partitioning decisions made at install time affect long-term administration, and how to confirm a working installation through the terminal.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Type 1 Hypervisor (Bare-Metal)**: A hypervisor that runs directly on the physical server hardware with no underlying host OS, giving it full control over hardware resources. Examples include VMware ESXi and Microsoft Hyper-V. Type 1 hypervisors provide lower latency and better performance than Type 2 in production environments.
*   **Type 2 Hypervisor (Hosted)**: A hypervisor that runs as an application on top of an existing operating system such as Windows or macOS. VirtualBox and VMware Workstation are Type 2 hypervisors. Because the host OS mediates hardware access, Type 2 solutions are slower but far easier to set up on a personal laptop.
*   **Linux Distribution (Distro)**: A packaged combination of the Linux kernel, a package manager, init system, and default software, assembled by a community or company. Common exam-relevant distros include Debian/Ubuntu (apt-based), RHEL/CentOS/Fedora (dnf/rpm-based), and SUSE (zypper-based). The exam tests distro-specific tool differences.
*   **Partition Table (MBR vs GPT)**: MBR (Master Boot Record) supports disks up to 2 TB and a maximum of 4 primary partitions. GPT (GUID Partition Table) supports disks larger than 2 TB and up to 128 primary partitions on Linux. Modern Linux installs on UEFI systems require GPT.
*   **GRUB2 (Grand Unified Bootloader version 2)**: The default bootloader for most Linux distributions. It presents a menu during boot allowing the user to select the kernel or recovery mode. Its configuration file is `/boot/grub/grub.cfg` (generated from `/etc/default/grub`); editing it directly is discouraged — use `update-grub` or `grub2-mkconfig` instead.
*   **VirtualBox Guest Additions**: A software package installed inside the guest Linux VM that enables enhanced features such as shared clipboard, dynamic screen resolution, and shared folders between the host and guest. Install via `sudo apt install virtualbox-guest-additions-iso` or mount the ISO from the VirtualBox Devices menu.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Linux installation topics fall under Linux+ Domain 1.0 (System Management) and Domain 2.0 (Security). Know how partition choices affect security (separate `/home`, `/var`, `/tmp` partitions reduce blast radius from disk-fill attacks).
*   **Know your bootloaders:** The exam expects you to know that `grub2-mkconfig -o /boot/grub2/grub.cfg` regenerates the GRUB config on RHEL-family systems, while `update-grub` is the Debian/Ubuntu equivalent. Both are tested in scenario questions.
*   **Hypervisor trap:** A very common exam distractor confuses Type 1 and Type 2 hypervisors. Remember: "bare metal = Type 1". VirtualBox is always Type 2 because you install it on Windows or macOS first.
*   **Installation method differences:** Know the difference between a minimal install (CLI only, used for servers) and a full desktop install. The exam often asks which install type is more appropriate for a hardened production server.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) is your primary free OER textbook — an authoritative guide to command-line Linux written by a professional sysadmin and freely available online. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) provides video walkthroughs of core Linux administration tasks that complement the textbook reading.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 1–2 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), covering shell basics and how the Linux environment is structured after installation.
*   **Required Video:** Watch the introductory Linux installation and navigation videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a comprehensive YouTube playlist covering foundational Linux administration from installation through scripting.

---

### Lab & Command Integration
In this week's hands-on lab you will install a Linux distribution inside VirtualBox, partition the disk using the guided installer, verify the installation by logging in at the terminal, and confirm the kernel version with `uname -r`. Use `lsblk` to verify partition layout and `df -h` to confirm mounted filesystems.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 1–2 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the installation and navigation videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
