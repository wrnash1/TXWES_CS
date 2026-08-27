# Lab: Module 01 — Linux VM Setup and First Login

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Lab Overview

This lab guides you through downloading, installing, and configuring your Linux virtual machine — the lab environment you will use for every remaining module in this course. By the end of this lab, you will have a working Ubuntu Server 22.04 LTS VM, have taken your first snapshot, and have explored the bash prompt with a handful of introductory commands.

**Estimated time**: 45–60 minutes (most of this is installation wait time)

**Prerequisites**: A host computer with at least 8 GB RAM and 30 GB free disk space. Windows 10/11, macOS 12+, or a Linux desktop.

---

## Part 1 — Install VirtualBox

### Step 1: Download VirtualBox

Navigate to [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads) and download the installer for your host operating system.

Also download the **VirtualBox Extension Pack** from the same page — it adds USB 3.0 support and improved guest integration.

### Step 2: Install VirtualBox

Run the installer with default settings. Accept the network interface warning (it will briefly disconnect your network adapter). After installation, open VirtualBox.

### Step 3: Install the Extension Pack

In VirtualBox, go to File → Tools → Extension Pack Manager. Click the Install button and select the Extension Pack file you downloaded. Accept the license agreement.

---

## Part 2 — Download Ubuntu Server 22.04 LTS

Navigate to [https://ubuntu.com/download/server](https://ubuntu.com/download/server) and download the Ubuntu Server 22.04.3 LTS ISO (approximately 1.4 GB). Save it to a location you can find easily — your Downloads folder works fine.

---

## Part 3 — Create the Virtual Machine

### Step 1: New VM

In VirtualBox, click **New**. Fill in the following:

- **Name**: UbuntuServer2204
- **Machine Folder**: Default (or choose a location with at least 25 GB free)
- **Type**: Linux
- **Version**: Ubuntu (64-bit)

Click Next.

### Step 2: Memory

Set RAM to **2048 MB (2 GB)**. If your host has 16 GB or more, set it to **4096 MB (4 GB)** for better performance.

### Step 3: Hard Disk

Select **Create a virtual hard disk now**. On the next screen, leave the format as **VDI (VirtualBox Disk Image)** and select **Dynamically allocated**. Set the size to **20 GB**. Click Create.

### Step 4: Attach the ISO

Before starting the VM, select it in the VirtualBox list, click **Settings**, and go to **Storage**. Under the Controller: IDE tree, click the empty optical disk icon. Click the disk icon on the right and select **Choose a disk file**. Browse to your downloaded Ubuntu Server ISO and select it. Click OK.

---

## Part 4 — Install Ubuntu Server

### Step 1: Start the VM

Click Start. The VM boots from the ISO.

### Step 2: Work Through the Installer

When the Ubuntu Server installer loads:

1. **Language**: English
2. **Installer update**: If prompted, choose "Continue without updating" to save time.
3. **Keyboard**: Your keyboard layout (default US English is fine for most students).
4. **Network**: Leave as is — the default DHCP configuration will work in most home and lab environments.
5. **Proxy**: Leave blank.
6. **Mirror**: Default Ubuntu mirror is fine.
7. **Storage**: Choose **Use an entire disk**. Select the 20 GB virtual disk. Confirm the partition layout (you will see the installer create `/boot`, `/`, and swap partitions).
8. **Profile setup**:
   - Your name: your actual name
   - Server name: `ubuntu-lab` (or any hostname you prefer — no spaces)
   - Username: `student` (use this throughout the course for consistency)
   - Password: choose something you will remember — it does not need to be complex for a lab VM
9. **SSH Setup**: Check **Install OpenSSH server**. This allows you to connect from your host machine's terminal to the VM.
10. **Featured snaps**: Uncheck everything. Click Done.

The installer will now copy files and complete the installation. This takes approximately 5–10 minutes.

### Step 3: Reboot

When the installer says "Installation complete!", press Enter to reboot. The VM will attempt to eject the ISO — if it reboots back into the installer, go to VirtualBox Devices → Optical Drives → Remove disk from virtual drive, then reset the VM (Machine → Reset).

---

## Part 5 — First Login

When the VM boots to the login prompt, you will see something like:

```
ubuntu-lab login:
```

Type your username (`student`) and press Enter. Type your password and press Enter. (Note: the password does not display as you type — this is normal Linux behavior.)

You should see the bash prompt:

```
student@ubuntu-lab:~$
```

You are now logged into a Linux server.

---

## Part 6 — Take a Snapshot

Before doing anything else, take a snapshot of your clean installation. In VirtualBox, go to **Machine → Take Snapshot**. Name it **"Clean Install"** and add a brief description: "Fresh Ubuntu Server 22.04 install, no changes made." Click OK.

This snapshot is your safety net. If you ever break the VM beyond repair, you can restore to this snapshot and start fresh.

---

## Part 7 — Introductory Commands

Run each of the following commands in your VM and record the output in your lab notes.

### Command 1: Who am I?

```bash
whoami
```

This prints your current username.

### Command 2: What is the hostname?

```bash
hostname
```

This prints the system's hostname.

### Command 3: What Linux is running?

```bash
uname -a
```

This prints the kernel version, architecture, and other system information. Find the kernel version in the output.

### Command 4: What distribution is this?

```bash
cat /etc/os-release
```

This prints distribution information. Find the `NAME`, `VERSION`, and `ID` fields.

### Command 5: Where am I in the filesystem?

```bash
pwd
```

This prints the current working directory. Since you just logged in, it should show `/home/student`.

### Command 6: What is in my home directory?

```bash
ls -la
```

This lists all files, including hidden ones, in long format. You will see a few hidden configuration files (starting with `.`). We cover this command in detail in Module 2.

### Command 7: What is today's date and time?

```bash
date
```

### Command 8: How long has the system been running?

```bash
uptime
```

### Command 9: How much disk space is available?

```bash
df -h
```

This shows filesystem usage. Find the `/` (root) filesystem and note the total size and percentage used.

### Command 10: Exit gracefully

```bash
exit
```

This logs you out and returns to the login prompt. Log back in and verify your prompt reappears.

---

## Deliverables

Submit a screenshot showing:

1. Your bash prompt after login (showing your username and hostname).
2. The output of `uname -a`.
3. The output of `cat /etc/os-release` (or at least the `NAME` and `VERSION` lines).
4. The VirtualBox Snapshots list showing your "Clean Install" snapshot.

---

## Troubleshooting

**VM boots back to the installer instead of the installed system**: Go to VirtualBox Devices → Optical Drives → Remove disk from virtual drive. Reset the VM.

**Cannot log in**: Passwords are case-sensitive. The password field does not show characters as you type — type carefully and press Enter.

**Network is not working (no internet access from VM)**: Check VirtualBox Network settings for the VM. The default "NAT" adapter should provide outbound internet access. If the adapter shows "Not attached," change it to NAT.

**VM is very slow**: Increase RAM in VirtualBox Settings → System → Motherboard. Also enable VT-x/AMD-V in your host BIOS if virtualization is not available.

---

## Part 9 — Challenge Exercise

### Challenge 1: Kernel and Distribution Deep Dive

Explore your running system to collect detailed version and hardware information using only command-line tools.

1. Run `uname -r` to get just the kernel release string, then run `uname -a` to get the full output. Record what each field in the full output means (kernel name, hostname, kernel release, kernel version, machine hardware, processor, hardware platform, OS).
2. Run `cat /proc/version` and compare its output to `uname -a`. Identify which compiler was used to build your running kernel.
3. Run `lscpu` to display CPU architecture details. Record the number of CPUs, threads per core, and whether virtualization is shown as active.
4. Run `free -h` to display memory usage. Calculate the percentage of RAM currently in use by the system at idle.

### Challenge 2: Exploring the Filesystem Root

Without using the internet, discover what is in the top-level Linux directory structure entirely from within your VM.

1. Run `ls /` to list all top-level directories. For at least five directories (e.g., `/bin`, `/etc`, `/var`, `/tmp`, `/home`), run `ls` inside each and describe in one sentence what type of content you find.
2. Run `man hier` to read the official manual page describing the Linux filesystem hierarchy. Identify three directories you did not expect to find described there.
3. Run `df -h` and `du -sh /*` (note: `du -sh /*` may produce some permission errors — that is expected). Compare the output to understand which top-level directories consume the most space on a fresh install.

### Reflection Questions

1. The Linux kernel is described as "monolithic." Based on what you observed with `lscpu` and `uname`, what are the potential tradeoffs of running all device drivers inside the kernel versus running them in userspace (as a microkernel would)?
2. If you were deploying this Ubuntu Server VM in a real enterprise environment, which of the introductory commands from Part 7 would you run immediately after first login to verify the system is healthy, and why?
