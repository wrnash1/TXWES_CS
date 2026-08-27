# Lab 01: Linux Installation and VM Setup

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 90-120 minutes

---

### Overview

In this lab you will install Ubuntu Server 22.04 LTS inside Oracle VirtualBox, configure basic
virtual machine settings, perform a guided disk partitioning, and run a series of terminal commands
to verify the installation is complete and functioning correctly.

These steps mirror real-world server provisioning workflows. Every subsequent lab in this course
builds on the Ubuntu Server VM you create today. Take a snapshot when you finish so you can
restore it if needed.

**What you will practice:**

- Creating and configuring a virtual machine in VirtualBox
- Installing Ubuntu Server 22.04 LTS from an ISO
- Navigating the installer's partition configuration screen
- Running post-installation verification commands at the terminal
- Taking a VirtualBox snapshot for rollback protection

---

### Prerequisites

Before beginning, ensure the following are complete:

- Oracle VirtualBox is installed on your host machine (download from virtualbox.org)
- Ubuntu Server 22.04 LTS ISO is downloaded (ubuntu.com/download/server)
- Your host machine has at least 8 GB of RAM and 40 GB of free disk space
- You have watched both parts of the Module 01 video lecture
- You have read the Module 01 Reading Guide

---

### Part 1 - Create the Virtual Machine

**Step 1.1 - Open VirtualBox and start the New VM wizard**

Launch VirtualBox. Click the blue New button in the toolbar.

Enter the following settings:

```
Name:   Ubuntu_Server_22
Type:   Linux
Version: Ubuntu (64-bit)
```

Click Next.

**Step 1.2 - Allocate RAM**

Set the memory size to 2048 MB (2 GB). Do not allocate more than half of your host machine's
total physical RAM.

Click Next.

**Step 1.3 - Create a virtual hard disk**

Select "Create a virtual hard disk now." Click Create.

Choose VDI (VirtualBox Disk Image) as the file type. Click Next.

Choose "Dynamically allocated." Click Next.

Set the disk size to 25 GB. Click Create.

**Step 1.4 - Attach the Ubuntu ISO**

In the VirtualBox main window, select your new VM and click Settings.

Navigate to Storage. Click the empty optical drive under Controller: IDE.

Click the small disk icon on the right side and select "Choose a disk file." Navigate to and
select your downloaded Ubuntu Server ISO.

Click OK to close Settings.

---

### Part 2 - Install Ubuntu Server

**Step 2.1 - Start the VM and boot the installer**

Select Ubuntu_Server_22 in the VirtualBox Manager and click Start.

The VM will boot from the ISO. At the GNU GRUB menu, press Enter or wait for the timeout.

You will arrive at the Ubuntu Server installer.

**Step 2.2 - Language and keyboard**

Select English as the installer language. Press Enter.

Select your keyboard layout. For most students this is English (US). Press Enter.

**Step 2.3 - Installation type**

Select "Ubuntu Server" (not the minimized version). Press Enter.

**Step 2.4 - Network configuration**

The installer will attempt DHCP on your virtual network adapter. Wait for it to complete.
You should see an IP address assigned to ens33 or similar interface. Press Done.

**Step 2.5 - Storage configuration**

Select "Use an entire disk." This configures one root partition and a boot partition automatically.

On the storage layout confirmation screen, review the proposed layout. You should see:
- A small partition for the EFI system partition (if UEFI)
- A root partition using the remaining space

Select Done and confirm when prompted. This will erase the virtual disk.

**Step 2.6 - Profile configuration**

Fill in the profile screen:

```
Your name:         Lab Admin
Server's name:     ubuntu-lab
Username:          labadmin
Password:          (choose a strong password you will remember)
Confirm password:  (repeat)
```

Press Done.

**Step 2.7 - SSH configuration**

On the SSH Setup screen, press the spacebar to select "Install OpenSSH server." This enables
remote terminal access. Press Done.

**Step 2.8 - Featured Snaps**

Do not select any additional snaps. Press Done to proceed with a minimal install.

**Step 2.9 - Installation**

The installer will copy files and configure the system. This takes 5 to 15 minutes.

When you see "Installation complete!" and the option to reboot, select "Reboot Now."

When the reboot sequence starts, the installer will ask you to remove the installation medium.
Press Enter. VirtualBox will automatically detach the ISO.

---

### Part 3 - Post-Installation Verification

After the system reboots you will see a login prompt. Log in with the username labadmin and the
password you set during installation.

Run each of the following commands and record the output. You will include screenshots of this
terminal output in your deliverable.

**Step 3.1 - Kernel version**

```bash
uname -r
```

Expected output example:

```
5.15.0-91-generic
```

Write down the exact kernel version number shown on your system.

**Step 3.2 - Operating system details**

```bash
cat /etc/os-release
```

Expected output excerpt:

```
NAME="Ubuntu"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
ID=ubuntu
ID_LIKE=debian
```

**Step 3.3 - Disk layout verification**

```bash
lsblk
```

Expected output example:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0   25G  0 disk
├─sda1   8:1    0    1M  0 part
├─sda2   8:2    0  513M  0 part /boot/efi
└─sda3   8:3    0 24.5G  0 part /
```

Note: Your exact partition names and sizes may vary slightly.

**Step 3.4 - Filesystem usage**

```bash
df -h
```

Expected output excerpt:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda3        24G  5.2G   17G  24% /
tmpfs           969M     0  969M   0% /dev/shm
/dev/sda2       512M  6.1M  506M   2% /boot/efi
```

**Step 3.5 - Network interface**

```bash
ip addr show
```

Expected output excerpt:

```
1: lo: <LOOPBACK,UP,LOWER_UP>
    inet 127.0.0.1/8 scope host lo
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic ens33
```

Note: Your interface name and IP address will differ based on VirtualBox network settings.

**Step 3.6 - SSH service status**

```bash
systemctl status ssh
```

Expected output excerpt:

```
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service)
     Active: active (running)
```

---

### Part 4 - Take a Snapshot

Taking a snapshot before making further changes protects your clean installation.

In VirtualBox Manager, right-click Ubuntu_Server_22 and select Snapshots. If the VM is running,
shut it down first:

```bash
sudo shutdown -h now
```

In the Snapshots view, click Take. Enter the following details:

```
Name:        Clean Install - Module 01
Description: Freshly installed Ubuntu Server 22.04 LTS, labadmin user, OpenSSH enabled
```

Click OK. The snapshot is saved.

---

### Part 5 - Analysis Questions

Answer each question in 2 to 4 complete sentences. These answers are part of your submission.

**Question 1:** Your lsblk output shows three partitions on the virtual disk. What is the purpose
of each partition you see? Why does Ubuntu create a separate /boot/efi partition?

**Question 2:** Your df -h output shows a tmpfs filesystem. What is tmpfs, and how does it differ
from a partition on the virtual hard disk?

**Question 3:** The uname -r command shows a version number like 5.15.0-91-generic. What does the
word "generic" indicate about this kernel build? How would the name differ on a RHEL system?

**Question 4:** You ran systemctl status ssh and saw "active (running)." What would you do if
it showed "inactive (dead)"? Write the exact command you would use to start and enable the service.

**Question 5:** Explain the security reason for not installing the GNOME desktop environment on
a server. Reference the concept of attack surface in your answer.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of the VirtualBox Manager showing your Ubuntu_Server_22 VM
2. Screenshot of your terminal showing the output of uname -r
3. Screenshot of your terminal showing the output of cat /etc/os-release
4. Screenshot of your terminal showing the output of lsblk
5. Screenshot of your terminal showing the output of df -h
6. Screenshot of your terminal showing the output of ip addr show
7. Screenshot of your terminal showing the output of systemctl status ssh
8. Written answers to all five analysis questions (Part 5)

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| VirtualBox VM screenshot showing VM listed | 10 |
| uname -r screenshot showing kernel version | 10 |
| cat /etc/os-release screenshot | 10 |
| lsblk screenshot showing partition layout | 10 |
| df -h screenshot showing mounted filesystems | 10 |
| ip addr show screenshot showing network interface | 10 |
| systemctl status ssh screenshot showing active state | 10 |
| Analysis Question 1 (partition purposes) | 5 |
| Analysis Question 2 (tmpfs explanation) | 5 |
| Analysis Question 3 (kernel naming) | 5 |
| Analysis Question 4 (service management) | 5 |
| Analysis Question 5 (attack surface) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

These steps go beyond the standard lab and are designed for students who want to deepen their
skills. Challenge exercises are not graded but are strongly recommended for exam preparation.

**Challenge Step 1 — Explore the /proc virtual filesystem**

The /proc filesystem exposes live kernel data. Run the following commands and record what each
file contains:

```bash
cat /proc/version
cat /proc/cpuinfo | grep "model name" | head -1
cat /proc/meminfo | grep -E "^MemTotal|^MemFree|^MemAvailable"
cat /proc/uptime
ls /proc/ | grep -E "^[0-9]+" | wc -l
```

For the last command, the number displayed is the count of running processes (each numbered
directory in /proc corresponds to one PID). Document what you observe and explain in two
sentences why /proc does not consume disk space even though it appears as files.

**Challenge Step 2 — Inspect EFI boot entries and partition layout**

If your VM was installed in UEFI mode, run the following commands to examine the boot
configuration:

```bash
sudo efibootmgr -v
sudo blkid
sudo lsblk -f
sudo parted /dev/sda print
```

Compare the UUID shown by blkid for your /boot/efi partition against the entry in /etc/fstab:

```bash
cat /etc/fstab
```

Confirm that the UUID in /etc/fstab matches the UUID reported by blkid. Explain in two
sentences why /etc/fstab uses UUIDs rather than device names like /dev/sda2 to identify
partitions.

**Challenge Step 3 — Verify system integrity using package manager checksums**

Use the package manager to verify that key system binaries have not been altered since
installation. Run:

```bash
sudo dpkg --verify bash
sudo dpkg --verify coreutils
sudo dpkg --verify openssh-server
sudo dpkg --verify sudo
```

If any command produces output, a file has been modified from its packaged state. No output
means all files match. Next, deliberately test the verification:

```bash
sudo touch /usr/bin/ls
sudo dpkg --verify coreutils
```

Observe that dpkg now reports a timestamp discrepancy for ls. Restore it:

```bash
sudo apt install --reinstall coreutils
sudo dpkg --verify coreutils
```

Document the output at each stage and explain in three sentences why relying on ls -la
timestamps alone is insufficient for detecting a binary replacement by a sophisticated attacker.
