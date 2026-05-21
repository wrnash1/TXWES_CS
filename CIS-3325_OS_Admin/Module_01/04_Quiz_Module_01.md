# Quiz: Module 01 - Linux Installation and VM Setup
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
Which of the following describes a Type 1 hypervisor?
A) It runs as an application on top of an existing host operating system like Windows 10.
B) It runs directly on the server's bare-metal hardware.
C) It cannot run Linux virtual machines.
D) It requires Oracle VirtualBox to function.
*   **Correct Answer:** B) It runs directly on the server's bare-metal hardware.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a Type 2 hypervisor (hosted), not Type 1.
    *   *Why C is incorrect:* Type 1 hypervisors can run almost any supported OS, including Linux.
    *   *Why D is incorrect:* VirtualBox is a Type 2 hypervisor. Type 1 hypervisors include ESXi and Hyper-V.

---

---

**Question 2**
What is the primary function of an operating system's kernel?
A) To provide a graphical desktop environment and window manager for the user.
B) To compile source code written in C into executable ELF binaries.
C) To manage hardware resources and act as a bridge between applications and the underlying hardware.
D) To store user documents and run web browsers in isolated containers.
*   **Correct Answer:** C) To manage hardware resources and act as a bridge between applications and the underlying hardware.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The desktop environment (e.g., GNOME, KDE) is a user-space application layered on top of the kernel, not part of the kernel itself.
    *   *Why B is incorrect:* Compiling source code is the role of a compiler such as GCC, not the OS kernel.
    *   *Why D is incorrect:* Web browsers and document storage applications run in user space; the kernel provides them system calls and hardware access but does not run them directly.

---

---

**Question 3**
A systems administrator needs to verify which Linux kernel version is currently running on a freshly installed virtual machine. Which command should they use?
A) uname -r
B) df -h
C) lsblk
D) chmod 600 /etc/os-release
*   **Correct Answer:** A) uname -r
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `df -h` reports disk space usage on mounted filesystems, not kernel version.
    *   *Why C is incorrect:* `lsblk` lists block devices and partition layout, not kernel information.
    *   *Why D is incorrect:* `chmod 600` changes file permissions; `/etc/os-release` contains distro name and version, not the running kernel version.

---

**Question 4**
A student installs Ubuntu in VirtualBox but the screen resolution stays small and copy-paste between the host and guest does not work. What is the most likely solution?
A) Reinstall the Linux kernel from source.
B) Install VirtualBox Guest Additions inside the guest VM.
C) Switch from a Type 2 to a Type 1 hypervisor.
D) Reformat the virtual disk using GPT instead of MBR.
*   **Correct Answer:** B) Install VirtualBox Guest Additions inside the guest VM.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Compiling a custom kernel does not add VirtualBox display or clipboard integration drivers.
    *   *Why C is incorrect:* VirtualBox is inherently a Type 2 hypervisor; switching hypervisor type does not resolve guest integration features.
    *   *Why D is incorrect:* The partition table format (GPT vs MBR) affects boot and storage layout, not screen resolution or clipboard sharing.

---

**Question 5**
When preparing a Linux server for a production environment, a junior administrator installs the full GNOME desktop environment by default. A senior administrator says this violates hardening best practices. Which of the following best explains why?
A) GNOME is incompatible with the Linux kernel on UEFI systems.
B) Desktop environments require GPT partition tables, which cannot be used on servers.
C) Unnecessary software packages increase the attack surface by introducing additional services and potential vulnerabilities.
D) A graphical interface prevents administrators from using SSH to connect remotely.
*   **Correct Answer:** C) Unnecessary software packages increase the attack surface by introducing additional services and potential vulnerabilities.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GNOME is fully compatible with UEFI systems; this is a fabricated incompatibility.
    *   *Why B is incorrect:* The desktop environment has no dependency on GPT versus MBR; both work fine with or without a GUI.
    *   *Why D is incorrect:* SSH operates independently of the graphical environment; you can run both simultaneously. The hardening concern is about unneeded software, not SSH access.

