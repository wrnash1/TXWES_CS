# Video Script: Module 01 - Linux Installation and VM Setup (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA Linux+ / Linux Foundation &bull; Operating System Administration &bull; Module 01</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ / Linux Foundation &bull; Operating System Administration" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ / Linux Foundation &bull; Operating System Administration</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 12 minutes
**Part:** 2 of 2 - Hands-On Application

---

### Opening

Welcome back. This is Part 2 of Module 01. We are moving from conceptual foundation into
hands-on setup. By the end of this part you will have watched a full VirtualBox installation
walkthrough, understand how to configure a new VM for Ubuntu Server, and know exactly which
terminal commands confirm a successful installation. This directly prepares you for this week's lab.

---

### Section 1: Installing VirtualBox

VirtualBox is a Type 2 hypervisor made by Oracle. It runs as an application on top of your
existing host OS, whether that is Windows, macOS, or another Linux installation. We use it because
it is free, widely supported, and the skills transfer directly to VMware and other enterprise
hypervisors.

[SHOW TERMINAL]

Download VirtualBox from virtualbox.org. The installer is straightforward on both Windows and
macOS. On Windows you will also install the VirtualBox Extension Pack, which adds USB 3.0 support
and other features.

After installation, launch the Oracle VM VirtualBox Manager. The main window shows a panel on the
left listing your virtual machines and a details panel on the right.

---

### Section 2: Creating the Virtual Machine

Click the New button to start the VM creation wizard.

Name: Ubuntu_Server_22
Type: Linux
Version: Ubuntu (64-bit)

Allocate RAM. For Ubuntu Server, 2048 MB is sufficient for lab work. Do not allocate more than
half of your physical host RAM, or your host OS will slow down significantly.

Create a virtual hard disk. Select VDI format and dynamically allocated. Set the size to 25 GB.
Dynamically allocated means the file on your host only grows as data is written inside the VM,
so a 25 GB virtual disk might only consume 4 GB of your host's actual storage initially.

Before starting the VM, configure the optical drive. In Settings, under Storage, click the empty
optical drive icon and attach the Ubuntu Server 22.04 LTS ISO file you downloaded. This simulates
inserting a DVD into a physical machine.

---

### Section 3: Ubuntu Server Installation Walkthrough

[SHOW TERMINAL]

Start the VM. The Ubuntu installer will load. You will be presented with a series of configuration
screens.

Language selection: English.

Keyboard layout: match your physical keyboard.

Network configuration: the installer will attempt to configure DHCP automatically. Accept it.

Storage configuration: This is the critical screen for partition planning.

For our lab, select "Use an entire disk." The installer will create:
- A small EFI boot partition (for UEFI systems)
- A root partition using the remaining space

In production environments you would create separate partitions for /home, /var, and /tmp to limit
the blast radius of a disk-fill event. The exam tests this knowledge.

Profile setup: Create your username, server name, and password. Use a strong password. I recommend
creating a user called labadmin for consistency across all labs in this course.

SSH configuration: Select "Install OpenSSH server." This is critical. It allows us to connect to
the VM from our host machine rather than always using the VirtualBox console window.

Package selection: Deselect everything. We want a minimal server install. Unnecessary packages
increase the attack surface.

The installation will take 5 to 15 minutes depending on your hardware and internet connection.
When it completes, select Reboot Now.

---

### Section 4: Post-Installation Verification Commands

[SHOW TERMINAL]

Once the system reboots and you see the login prompt, log in with the username and password you
created. You will land at the bash shell prompt.

Run these verification commands one by one.

First, confirm the kernel version:

```bash
uname -r
```

You should see something like 5.15.0-91-generic. The number identifies the exact kernel build.

Second, confirm the distribution version:

```bash
cat /etc/os-release
```

This shows the distribution name, version, and codename. For Ubuntu 22.04 you should see
VERSION="22.04 LTS (Jammy Jellyfish)".

Third, confirm disk layout:

```bash
lsblk
```

You will see your virtual disk (likely sda or vda) divided into partitions. Note the mount point
for the root partition.

Fourth, confirm mounted filesystems and available space:

```bash
df -h
```

The -h flag means human-readable. You should see the root filesystem / mounted with approximately
22 to 24 GB available.

Fifth, confirm network connectivity:

```bash
ip addr show
```

You should see a loopback interface (lo) and an ethernet interface (typically named ens33 or
enp0s3) with an IP address assigned by DHCP.

Sixth, confirm systemd is managing services:

```bash
systemctl status ssh
```

If you installed OpenSSH during setup, this should show the service as active (running).

---

### Section 5: VirtualBox Guest Additions

After confirming the base installation works, install VirtualBox Guest Additions. This is a
software package that enhances integration between the VM and your host.

Guest Additions provides shared clipboard between host and VM, dynamic screen resolution
adjustment when you resize the window, and shared folders to transfer files between host and VM.

[SHOW TERMINAL]

```bash
sudo apt update
sudo apt install virtualbox-guest-additions-iso
```

After installation, reboot the VM. You should notice the screen resolution adjusts automatically
when you resize the VirtualBox window.

---

### Section 6: Taking a Snapshot

Before you make any significant changes to your VM, take a snapshot. This is one of the most
valuable features of working with virtual machines.

In the VirtualBox Manager, with your VM selected (but not running, or in a saved state), click
the Snapshots button. Click Take and name the snapshot "Clean Install - Module 01.

Now if anything goes wrong in a future lab, you can right-click the snapshot and choose Restore
to go back to this exact state.

I strongly recommend taking a fresh snapshot at the start of each module's lab.

---

### Section 7: Exam Tips

Let us connect what we just did to the CompTIA Linux+ exam.

The exam frequently tests the difference between Type 1 and Type 2 hypervisors. VirtualBox is
always Type 2 because it installs on top of an existing OS. VMware ESXi and Microsoft Hyper-V
(server edition) are Type 1.

The exam tests GRUB2 configuration. On Ubuntu, the command to regenerate GRUB configuration is
update-grub. On RHEL-based systems it is grub2-mkconfig -o /boot/grub2/grub.cfg.

The exam tests why minimal server installations are preferred. The answer is attack surface
reduction. Every installed package is potential vulnerability surface. Production servers run
only what they need.

The exam tests uname flags. uname -r shows kernel release. uname -a shows all system information
including the kernel version, hostname, and architecture.

---

### Lab Preview

This week's lab has you perform exactly what we just walked through. You will install Ubuntu Server
in VirtualBox, run all six verification commands, and submit screenshots of your terminal output.

Read the lab instructions carefully before you start. Pay special attention to the partition
configuration section, the post-install verification commands, and the deliverable requirements.

---

### Summary

In Part 1 we covered what the kernel does, the structure of Linux distributions, the FHS directory
tree, the MBR versus GPT partition choice, and why we use virtual machines.

In Part 2 we walked through VirtualBox setup, Ubuntu Server installation, and post-install
verification commands. You now have everything you need to complete the lab.

See you in Module 02, where we go deep into the filesystem hierarchy and navigation commands.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
