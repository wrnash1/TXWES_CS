# Online Course Map: CIS-3325 — OS Administration (Linux Track)
**Target Certification:** CompTIA Linux+ (XK0-005)
**Course Format:** 100% Online Asynchronous | Canvas LMS | Texas Wesleyan University

## Overview
This online course map outlines the modular structure of CIS-3325 OS Administration (Linux Track) as a 16-module asynchronous course. The curriculum is fully aligned to the CompTIA Linux+ XK0-005 exam blueprint across four domains: System Management, Security, Scripting/Containers/Automation, and Troubleshooting. Each module delivers micro-learning video content, targeted OER reading guides, hands-on Linux terminal labs, a certification-aligned practice quiz, and a graded discussion forum.

---

## Module Architecture

### Module 01: Linux Installation & VM Setup
- **Learning Objectives:** Install and configure a Linux virtual machine using VirtualBox or VMware. Navigate the Linux boot process, identify key installation partitions, and connect to a Linux system via the terminal.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (Hardware and OS Concepts)
- **Micro-Learning Video Assets (5-7 mins):**
  - *Video 1.1: What is Linux? Open Source Philosophy & Distributions*
  - *Video 1.2: Installing Ubuntu Server in VirtualBox — Step by Step* (Includes alt-text for VM configuration screens)
- **Reading Guide:** The Linux Command Line (Shotts) — Introduction & Chapter 1; LearnLinuxTV Playlist Episodes 1–3
- **Lab Assignment:** Install Ubuntu Server 24.04 LTS in VirtualBox. Verify the install by logging in and running `uname -a`, `lsb_release -a`, and `df -h`. Submit screenshots of all three command outputs.
- **Assessment:** Module 01 Practice Quiz — Linux history, distributions, VM hypervisor concepts, boot process (GRUB2, BIOS vs. UEFI).
- **Discussion Prompt:** Describe the difference between a Linux distribution and the Linux kernel. Why are there so many distributions, and what factors would guide your choice of distro for a production server?

---

### Module 02: Filesystem Navigation & File Management
- **Learning Objectives:** Navigate the Linux Filesystem Hierarchy Standard (FHS). Create, copy, move, delete, and find files. Understand absolute vs. relative paths and use essential navigation commands.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (File and Directory Operations)
- **Micro-Learning Video Assets:**
  - *Video 2.1: The Linux Filesystem Hierarchy Standard (FHS) — Where Everything Lives*
  - *Video 2.2: Essential File Management Commands — ls, cp, mv, rm, find, locate*
- **Reading Guide:** The Linux Command Line Chapters 1–4 (The Shell, Navigation, Exploring the System, Manipulating Files and Directories)
- **Lab Assignment:** Navigate to `/var/log`, list all `.log` files sorted by modification date. Create a directory structure `~/labs/module02/`. Copy the `syslog` file to that directory, rename it, then delete it. Use `find` to locate all files modified in the last 24 hours under `/etc`. Submit screenshots of each operation.
- **Assessment:** Module 02 Practice Quiz — FHS directories (/etc, /var, /home, /usr, /tmp, /proc), `ls` flags, `find` syntax, path types, `ln` hard vs. symbolic links.
- **Discussion Prompt:** Explain the purpose of at least four top-level directories in the Linux FHS (e.g., `/etc`, `/var`, `/usr`, `/proc`). Why is keeping `/` and `/home` on separate partitions considered a best practice for servers?

---

### Module 03: Text Processing (grep, awk, sed)
- **Learning Objectives:** Filter and transform text output using `grep`, `awk`, and `sed`. Construct pipelines using `|`, `>`, and `>>`. Use regular expressions for pattern matching.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (Text Manipulation); Domain 4 — Troubleshooting (Log Analysis)
- **Micro-Learning Video Assets:**
  - *Video 3.1: Searching with grep — Basic and Extended Regular Expressions*
  - *Video 3.2: Text Transformation with awk and sed — Field Extraction and In-place Editing*
- **Reading Guide:** The Linux Command Line Chapters 19–20 (Regular Expressions, Text Processing)
- **Lab Assignment:** Use `grep` to find all lines containing "error" (case-insensitive) in `/var/log/syslog`. Use `awk` to print only the timestamp and message fields from that output. Use `sed` to replace all occurrences of your hostname with the string "MYHOST" in a text file. Use `wc -l` to count matching lines. Submit screenshots of each pipeline.
- **Assessment:** Module 03 Practice Quiz — `grep -i`, `-v`, `-r`, `-E`, `awk` field separators (`$1`, `$NF`, `-F`), `sed` substitution syntax (`s/old/new/g`), pipe chaining.
- **Discussion Prompt:** A sysadmin receives a 50,000-line log file and needs to extract all lines from a specific IP address during a 2-hour window. Walk through the `grep` and `awk` pipeline you would build to accomplish this. What flags and options would you use and why?

---

### Module 04: Vim & Text Editors
- **Learning Objectives:** Open, edit, save, and quit files using Vim. Switch between Normal, Insert, and Command modes. Use Vim's search, replace, and navigation shortcuts for efficient editing.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (File Editing)
- **Micro-Learning Video Assets:**
  - *Video 4.1: Vim Survival Guide — Modes, Navigation, and Basic Editing*
  - *Video 4.2: Vim Efficiency — Search, Replace, Visual Mode, and .vimrc Basics*
- **Reading Guide:** The Linux Command Line Chapter 12 (A Gentle Introduction to vi); run `vimtutor` in your terminal (built-in interactive tutorial, ~30 minutes)
- **Lab Assignment:** Open a new file with Vim. Enter Insert mode and type a 10-line configuration block (provided in the lab). Save and quit. Re-open the file, navigate to line 5 using `5G`, change a word using `cw`, search for a string with `/`, and replace all occurrences of "old" with "new" using `:%s/old/new/g`. Save and quit. Submit screenshots of the before and after file states using `cat`.
- **Assessment:** Module 04 Practice Quiz — Vim mode switching (i, Esc, :), navigation (hjkl, G, gg, $, 0), save/quit (:w, :q, :wq, :q!), search (/), substitution (:%s).
- **Discussion Prompt:** Why is Vim (or another terminal text editor like nano) a critical skill for Linux system administrators, even when GUI text editors exist? Describe a scenario where only a terminal-based editor would be available and explain what you would do.

---

### Module 05: Process Management
- **Learning Objectives:** List, monitor, and control Linux processes. Use `ps`, `top`, `htop`, `kill`, `nice`, and `jobs`. Understand foreground/background execution, process states, and signals.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (Process Management)
- **Micro-Learning Video Assets:**
  - *Video 5.1: Monitoring Processes — ps, top, and htop Deep Dive*
  - *Video 5.2: Controlling Processes — kill, nice, renice, nohup, and Job Control*
- **Reading Guide:** The Linux Command Line Chapter 10 (Processes)
- **Lab Assignment:** Run `ps aux` and pipe the output to `grep` to find a specific process (e.g., `sshd`). Start a long-running process (`sleep 300 &`) in the background. Use `jobs` to list background jobs. Use `kill` with the process PID to terminate it. Use `nice -n 10` to launch a command with adjusted priority. Submit screenshots of each step with PID numbers visible.
- **Assessment:** Module 05 Practice Quiz — `ps aux` column meanings (PID, TTY, STAT, %CPU, %MEM), signal numbers (SIGTERM=15, SIGKILL=9, SIGHUP=1), `kill` vs. `killall`, `nice` vs. `renice`, process states (R, S, Z, D).
- **Discussion Prompt:** Explain the difference between `SIGTERM` and `SIGKILL`. In what situation would you use each? Why is it generally preferable to try `SIGTERM` before resorting to `SIGKILL`?

---

### Module 06: Storage & Filesystems
- **Learning Objectives:** Identify and manage disk partitions using `fdisk` and `parted`. Format partitions with `mkfs`. Mount and unmount filesystems. Configure persistent mounts in `/etc/fstab`.
- **XK0-005 Domain Alignment:** Domain 2 — Security (Storage Management)
- **Micro-Learning Video Assets:**
  - *Video 6.1: Understanding Disks, Partitions, and the Linux Device File System (/dev/sda, /dev/nvme)*
  - *Video 6.2: Creating Filesystems with mkfs and Configuring /etc/fstab for Persistent Mounts*
- **Reading Guide:** The Linux Command Line Chapter 15 (Storage Media)
- **Lab Assignment:** Attach a second virtual disk to your VM (instructions provided). Use `lsblk` and `fdisk -l` to identify it. Create a partition with `fdisk`, format it as ext4 with `mkfs.ext4`, create a mount point at `/mnt/data`, and mount it. Add a persistent entry to `/etc/fstab`. Verify with `mount -a` and `df -h`. Submit screenshots of each step.
- **Assessment:** Module 06 Practice Quiz — `lsblk`, `fdisk`, `parted`, `mkfs` variants (ext4, xfs, btrfs), mount points, `/etc/fstab` fields (device, mount point, type, options, dump, pass), `df -h` vs. `du -sh`.
- **Discussion Prompt:** Explain the purpose of the `/etc/fstab` file. What happens if a device listed in `/etc/fstab` is unavailable at boot? What entry option would you use to prevent a missing external drive from causing a boot failure?

---

### Module 07: User & Group Administration
- **Learning Objectives:** Create, modify, and delete user accounts and groups. Manage passwords, account expiration, and the `/etc/passwd`, `/etc/shadow`, and `/etc/group` files. Use `sudo` for privilege management.
- **XK0-005 Domain Alignment:** Domain 2 — Security (Identity and Access Management)
- **Micro-Learning Video Assets:**
  - *Video 7.1: User Management — useradd, usermod, userdel, passwd, and the /etc/passwd File*
  - *Video 7.2: Group Management and sudo — groupadd, gpasswd, visudo, and the sudoers File*
- **Reading Guide:** The Linux Command Line Chapter 9 (Permissions) — User and Group sections; LPI Learning Portal — User Administration
- **Lab Assignment:** Create three new users (`alice`, `bob`, `carol`). Create a group called `devteam`. Add all three users to the group. Set a password expiration policy for `alice` using `chage`. Grant `bob` limited sudo access to run `/usr/bin/apt` only by editing the sudoers file with `visudo`. Verify by switching to each user with `su`. Submit screenshots of `/etc/passwd` entries, `id` output for each user, and the sudoers addition.
- **Assessment:** Module 07 Practice Quiz — `useradd` vs. `adduser`, `usermod -aG`, `/etc/passwd` field meanings (username, x, UID, GID, GECOS, home, shell), `/etc/shadow` fields, `chage` flags, `sudo` vs `su`, `visudo` syntax.
- **Discussion Prompt:** Explain the principle of least privilege and how it applies to Linux user account administration. Give two specific examples of how you would configure a Linux system to minimize privilege exposure for a new junior sysadmin account.

---

### Module 08: File Permissions & ACLs
- **Learning Objectives:** Interpret and modify standard Linux file permissions (rwx) using both symbolic and octal notation. Set the umask. Configure Access Control Lists (ACLs) using `getfacl` and `setfacl` for granular permission management.
- **XK0-005 Domain Alignment:** Domain 2 — Security (File Permissions and ACLs)
- **Micro-Learning Video Assets:**
  - *Video 8.1: Linux Permissions Deep Dive — chmod, chown, chgrp, and Octal Notation*
  - *Video 8.2: Access Control Lists (ACLs) — setfacl, getfacl, and When Standard Permissions Are Not Enough*
- **Reading Guide:** The Linux Command Line Chapter 9 (Permissions) — full chapter
- **Lab Assignment:** Create a directory `/shared/project`. Set permissions so that the owner has full access, the group has read/write, and others have no access (`chmod 760`). Verify with `ls -la`. Use `setfacl` to grant user `carol` read-only access to the directory without changing the group. Verify with `getfacl`. Demonstrate the `umask` value and change it to `027`. Submit screenshots of each step and explain the resulting permission set.
- **Assessment:** Module 08 Practice Quiz — Permission notation (rwxr-xr--, 754, 640), SUID/SGID/sticky bit, `chmod` symbolic vs. octal, `chown user:group`, `umask` calculation, `setfacl -m u:user:rw`, `getfacl` output interpretation, the `+` flag in `ls -la` indicating an ACL.
- **Discussion Prompt:** A file has permissions `rwsr-xr-x` and is owned by root. What does the `s` in the owner execute position mean? Give a real-world example of why the SUID bit exists and what security risks it poses.

---

### Module 09: Shell Scripting (Bash)
- **Learning Objectives:** Write functional Bash scripts using variables, conditional statements, loops, functions, and command substitution. Make scripts executable and schedule them. Handle input arguments and exit codes.
- **XK0-005 Domain Alignment:** Domain 3 — Scripting, Containers, and Automation
- **Micro-Learning Video Assets:**
  - *Video 9.1: Bash Scripting Fundamentals — Variables, Conditionals (if/else), and Loops (for, while)*
  - *Video 9.2: Functions, Arguments, Exit Codes, and Writing Production-Ready Scripts*
- **Reading Guide:** The Linux Command Line Chapters 24–36 (Writing Shell Scripts — full section); LearnLinuxTV Bash Scripting Series
- **Lab Assignment:** Write a Bash script that: (1) accepts a directory path as an argument `$1`, (2) checks if the directory exists using an `if` statement, (3) lists all `.log` files in the directory older than 7 days using `find`, (4) moves them to a `/tmp/archive/` directory, and (5) outputs a summary count of files moved. Make the script executable with `chmod +x`. Test it against your `/var/log` directory. Submit the script file and screenshots of execution.
- **Assessment:** Module 09 Practice Quiz — Shebang line (`#!/bin/bash`), `$1`/`$2`/`$#`/`$@` positional parameters, `[ ]` vs `[[ ]]` test syntax, `if/then/elif/else/fi`, `for var in list; do`, `while [ condition ]; do`, `$(command)` command substitution, `$?` exit code, `chmod +x`.
- **Discussion Prompt:** You are a Linux sysadmin responsible for 50 servers. Describe a practical Bash script you would write to automate a recurring administrative task (e.g., disk space monitoring, log rotation, user account auditing). What specific Bash constructs would you use and why?

---

### Module 10: Package Management (apt/dnf)
- **Learning Objectives:** Install, update, remove, and search for software packages using `apt` (Debian/Ubuntu) and `dnf` (RHEL/Fedora). Manage repositories and understand the difference between source vs. binary packages.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (Software Management)
- **Micro-Learning Video Assets:**
  - *Video 10.1: Package Management with apt — install, update, upgrade, remove, autoremove, and Sources*
  - *Video 10.2: Package Management with dnf — install, update, search, groupinstall, and Repository Management*
- **Reading Guide:** The Linux Command Line Chapter 14 (Package Management)
- **Lab Assignment:** Using `apt` on your Ubuntu VM: install `htop` and `tree`. Verify installation with `which htop`. Show the installed package info with `apt show htop`. Remove `htop` and verify removal. Add the `universe` repository with `add-apt-repository universe`. If using a Fedora VM: replicate the exercise using `dnf install`, `dnf info`, `dnf remove`. Submit screenshots of each command and its output.
- **Assessment:** Module 10 Practice Quiz — `apt update` vs. `apt upgrade` vs. `apt dist-upgrade`, `apt install -y`, `apt purge` vs `apt remove`, `/etc/apt/sources.list`, `dpkg -l`, `dnf install`, `dnf search`, `rpm -qa`, repository configuration files in `/etc/yum.repos.d/`.
- **Discussion Prompt:** Explain the difference between `apt remove` and `apt purge`. Why does `apt update` not install any new software? Describe a scenario where adding a third-party repository could pose a security risk and how you would mitigate it.

---

### Module 11: Networking (ip, nmcli, SSH)
- **Learning Objectives:** Configure and troubleshoot network interfaces using `ip` and `nmcli`. Verify connectivity with `ping`, `traceroute`, `netstat`, and `ss`. Connect to remote systems with SSH and manage SSH keys.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (Networking); Domain 4 — Troubleshooting
- **Micro-Learning Video Assets:**
  - *Video 11.1: Linux Networking Commands — ip addr, ip route, nmcli, ping, ss, and netstat*
  - *Video 11.2: SSH Fundamentals — Connecting, Key-Based Authentication, and the ~/.ssh/config File*
- **Reading Guide:** The Linux Command Line Chapter 16 (Networking)
- **Lab Assignment:** Run `ip addr` and document your VM's IP address and subnet. Use `ip route` to display the routing table and identify the default gateway. Use `ss -tulpn` to list all listening ports. Generate an SSH key pair with `ssh-keygen -t ed25519`. Copy the public key to a second user account with `ssh-copy-id`. Test passwordless SSH login. Submit screenshots of all command outputs and the successful SSH login.
- **Assessment:** Module 11 Practice Quiz — `ip addr` vs. `ifconfig`, `ip route`, `nmcli con show`, `ping`, `traceroute`, `ss -tulpn` flag meanings, SSH default port (22), `ssh-keygen` key types (RSA, Ed25519), `~/.ssh/authorized_keys`, `~/.ssh/config` syntax.
- **Discussion Prompt:** Explain the difference between `netstat` and `ss`. Why is `ss` preferred on modern Linux systems? Describe what you would look for in `ss -tulpn` output when troubleshooting why a web server is not accepting connections on port 443.

---

### Module 12: Systemd & Services
- **Learning Objectives:** Manage Linux services using `systemctl`. Enable, disable, start, stop, and reload services. View service logs with `journalctl`. Create a basic custom systemd unit file.
- **XK0-005 Domain Alignment:** Domain 1 — System Management (Service Management and Boot)
- **Micro-Learning Video Assets:**
  - *Video 12.1: systemctl Mastery — start, stop, restart, enable, disable, status, and the Boot Process*
  - *Video 12.2: journalctl Deep Dive — Filtering Logs by Time, Service, and Priority Level*
- **Reading Guide:** The Linux Command Line Chapter 17 (System Processes); `man systemctl`, `man journalctl`
- **Lab Assignment:** Install `nginx` (`sudo apt install nginx`). Check its status with `systemctl status nginx`. Stop it, verify it stopped, then start it again. Enable it to start at boot and verify with `systemctl is-enabled nginx`. Use `journalctl -u nginx --since "1 hour ago"` to view recent logs. Create a custom unit file at `/etc/systemd/system/myscript.service` that runs a simple bash script at startup. Reload systemd and enable your service. Submit screenshots of all steps.
- **Assessment:** Module 12 Practice Quiz — `systemctl start/stop/restart/reload/status/enable/disable/mask`, `systemctl list-units --type=service`, unit file sections ([Unit], [Service], [Install]), `ExecStart=`, `WantedBy=multi-user.target`, `journalctl -u`, `-b` (current boot), `--since`, `--priority`.
- **Discussion Prompt:** What is the difference between `systemctl restart` and `systemctl reload`? In what scenario would you use `reload` instead of `restart` for a production web server? Describe what happens to running connections during each operation.

---

### Module 13: LVM & RAID Storage
- **Learning Objectives:** Create and manage Logical Volume Manager (LVM) volumes including physical volumes (PVs), volume groups (VGs), and logical volumes (LVs). Configure software RAID using `mdadm`. Extend and shrink logical volumes.
- **XK0-005 Domain Alignment:** Domain 2 — Security (Advanced Storage Management)
- **Micro-Learning Video Assets:**
  - *Video 13.1: LVM Explained — Physical Volumes, Volume Groups, Logical Volumes, and Why LVM Matters*
  - *Video 13.2: Software RAID with mdadm — RAID 0, RAID 1, RAID 5, and Monitoring Arrays*
- **Reading Guide:** The Linux Command Line Chapter 15 (Storage Media) — RAID/LVM sections; CompTIA Linux+ XK0-005 Domain 2 storage objectives
- **Lab Assignment:** Add two additional virtual disks to your VM. Initialize both as PVs with `pvcreate`. Create a VG named `datavg`. Create a 5GB LV named `datalv`. Format it as xfs and mount it at `/mnt/lvm`. Extend `datalv` by 2GB using `lvextend` and grow the filesystem with `xfs_growfs`. For RAID: initialize a RAID 1 array with `mdadm --create`. Monitor array status with `cat /proc/mdstat`. Submit screenshots of all `pvdisplay`, `vgdisplay`, `lvdisplay`, and `mdstat` outputs.
- **Assessment:** Module 13 Practice Quiz — `pvcreate`, `vgcreate`, `lvcreate -L -n`, `lvextend -L +2G`, `resize2fs` (ext4) vs. `xfs_growfs` (xfs), RAID levels (0=striping, 1=mirroring, 5=striping+parity, 6=dual-parity, 10=stripe of mirrors), `mdadm --create --level=1 --raid-devices=2`, `/proc/mdstat`.
- **Discussion Prompt:** A company stores critical customer data on a Linux server. Compare RAID 1 and RAID 5 in terms of redundancy, performance, storage efficiency, and rebuild complexity. Which would you recommend for a database server and why?

---

### Module 14: SSH Hardening & Ansible
- **Learning Objectives:** Harden the SSH server configuration (`/etc/ssh/sshd_config`) against common attacks. Disable root login, enforce key-based authentication, and change the default port. Use Ansible to automate configuration across multiple hosts.
- **XK0-005 Domain Alignment:** Domain 2 — Security (SSH Hardening); Domain 3 — Scripting, Containers, and Automation (Ansible)
- **Micro-Learning Video Assets:**
  - *Video 14.1: SSH Hardening Best Practices — sshd_config, Fail2Ban, and Key-Only Authentication*
  - *Video 14.2: Introduction to Ansible — Inventory Files, Ad-Hoc Commands, and Your First Playbook*
- **Reading Guide:** The Linux Command Line Chapter 16 (Networking — SSH sections); Ansible Documentation — Getting Started (docs.ansible.com)
- **Lab Assignment:** Edit `/etc/ssh/sshd_config` to: disable root login (`PermitRootLogin no`), disable password authentication (`PasswordAuthentication no`), change the port to 2222. Restart `sshd` and verify the changes. Install Ansible. Create an inventory file with your VM listed as `localhost`. Write a playbook that installs `htop` and ensures `nginx` is started and enabled. Run the playbook and submit the output showing `ok`, `changed`, and `failed` task counts. Submit screenshots of the hardened sshd_config and the Ansible playbook run.
- **Assessment:** Module 14 Practice Quiz — Key `sshd_config` directives (PermitRootLogin, PasswordAuthentication, Port, AllowUsers, MaxAuthTries), Ansible inventory file syntax (INI format), `ansible -m ping all`, playbook YAML structure (hosts, tasks, name, module), `ansible-playbook` output colors (green=ok, yellow=changed, red=failed), `become: yes` for privilege escalation.
- **Discussion Prompt:** Your company's public-facing Linux servers are experiencing brute-force SSH login attempts. Describe at least four specific hardening measures you would implement in `/etc/ssh/sshd_config` and at the firewall level to mitigate this risk. Explain the security rationale for each measure.

---

### Module 15: SELinux/AppArmor & Security
- **Learning Objectives:** Understand Mandatory Access Control (MAC) frameworks. Configure SELinux modes (enforcing, permissive, disabled) on RHEL-based systems. Configure AppArmor profiles on Ubuntu/Debian systems. Interpret audit logs and troubleshoot MAC denials.
- **XK0-005 Domain Alignment:** Domain 2 — Security (SELinux/AppArmor, Hardening)
- **Micro-Learning Video Assets:**
  - *Video 15.1: SELinux Fundamentals — Enforcing vs. Permissive, Contexts, Booleans, and semanage*
  - *Video 15.2: AppArmor on Ubuntu — Profiles, Modes (enforce/complain), aa-status, and Troubleshooting*
- **Reading Guide:** LPI Learning Portal — Linux Security Modules section; CompTIA Linux+ XK0-005 Domain 2 (Security) objectives
- **Lab Assignment (Ubuntu — AppArmor):** Run `sudo aa-status` to list AppArmor profiles. Set the `nginx` profile to complain mode with `sudo aa-complain /etc/apparmor.d/usr.sbin.nginx`. Trigger a denied operation by attempting to access a file outside the profile's allowed paths. Review `/var/log/syslog` for AppArmor denial messages. Return the profile to enforce mode. **Lab Assignment (Fedora/RHEL — SELinux):** Run `getenforce` to confirm SELinux status. Set to permissive with `setenforce 0`. Use `ausearch -m AVC` to view recent SELinux denials. Restore contexts with `restorecon -Rv /var/www/html`. Submit screenshots of SELinux/AppArmor status outputs and at least one denial log entry.
- **Assessment:** Module 15 Practice Quiz — SELinux modes (enforcing/permissive/disabled), `getenforce`, `setenforce`, `/etc/selinux/config`, SELinux contexts (`ls -Z`), `chcon`, `restorecon`, `setsebool`, AppArmor profiles, `aa-status`, `aa-enforce`, `aa-complain`, `aa-disable`, `/var/log/audit/audit.log` AVC messages.
- **Discussion Prompt:** A junior sysadmin suggests disabling SELinux on a production web server because it is causing access denial errors for the Apache web server. How would you respond? Describe the proper approach to diagnosing and resolving SELinux denials without disabling the security module entirely.

---

### Module 16: Final Exam Prep & CompTIA Linux+ Certification
- **Learning Objectives:** Review all XK0-005 exam domains. Practice performance-based question scenarios. Identify knowledge gaps and apply targeted remediation. Schedule and complete the CompTIA Linux+ (XK0-005) certification exam.
- **XK0-005 Domain Alignment:** All four domains — comprehensive review
- **Micro-Learning Video Assets:**
  - *Video 16.1: CompTIA Linux+ XK0-005 Exam Blueprint Review — Domain Breakdown and High-Weight Topics*
  - *Video 16.2: Performance-Based Question Strategies — What to Expect and How to Approach Scenario Questions*
- **Reading Guide:** Review the official CompTIA Linux+ XK0-005 Exam Objectives PDF (free download from comptia.org). Review your personal command cheat sheets from Modules 01–15. LearnLinuxTV — Full Certification Review videos.
- **Lab Assignment (Final Review Lab):** Complete a 10-task cumulative lab scenario covering: user creation with expiration, setting ACLs, writing and executing a Bash script with arguments, managing an LVM volume, configuring a systemd service, hardening sshd_config, and interpreting an AppArmor denial. Submit a comprehensive documented report with screenshots of all 10 tasks.
- **Assessment:** Final Certification Exam — CompTIA Linux+ (XK0-005). 90 questions, 90 minutes, passing score 720/900. Submit official CompTIA score report to Canvas Module 16 assignment.
- **Discussion Prompt:** Reflect on your experience in this course. Identify one Linux skill or concept that was more challenging than expected. Describe the specific steps you took to understand it and how you would apply it in a real system administration role.

---

## Pedagogical Standards Check
- [x] **Micro-Learning:** All videos capped at 5-7 minutes per segment.
- [x] **Question Banks:** All quizzes map directly to CompTIA Linux+ XK0-005 domains and use distractor analysis.
- [x] **Accessibility:** All video scripts include alt-text descriptions for visual elements (terminal screenshots, diagrams).
- [x] **Labs:** Designed for local execution via VirtualBox VM or WSL2.
- [x] **ZTC Compliance:** All required reading materials are freely available OER resources.
- [x] **Coverage:** All 16 modules map to at least one XK0-005 exam domain.
