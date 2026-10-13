# Video Script: Module 16 — Linux+ XK0-005 Exam Preparation

## Course: CIS-3325 OS Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## [INTRO — 0:00–1:00]

Welcome back, everyone — this is Module 16, and this is a big one. This is your final module of CIS-3325, and today we are doing something different from every other module in this course. We are not learning new commands. We are not setting up a new service. Today we are going to step back, look at everything we have covered across fifteen weeks, map it directly to the CompTIA Linux+ XK0-005 certification exam domains, and build a strategy so that when you sit down for that exam — whether it is this semester or later — you know exactly what to expect and how to approach every question type.

Here is what we are going to cover today. We will walk through all four exam domains with their weights, hit the highest-yield commands in each domain, talk through performance-based questions and why they require a different strategy than multiple choice, identify the most common exam traps, and give you a distractor-elimination framework you can use on any question you are unsure about.

Grab a notepad. There will be a lot to write down.

---

## [SECTION 1 — Exam Overview — 1:00–3:30]

### The XK0-005 Exam at a Glance

Let's orient ourselves before we go domain by domain. The CompTIA Linux+ XK0-005 exam has up to 90 questions and is 90 minutes long. That works out to exactly one minute per question — which feels fine until you hit a performance-based question that requires you to type commands into a simulated terminal. Those take significantly longer.

The passing score is 720 on a 900-point scale. That is approximately 80 percent. CompTIA does not penalize for guessing, so there is absolutely no reason to leave any question blank. If you run out of time, guess on everything remaining.

The four domains and their weights are as follows:

- Domain 1 — System Management: 32 percent
- Domain 2 — Security: 21 percent
- Domain 3 — Scripting, Containers, and Automation: 19 percent
- Domain 4 — Troubleshooting: 28 percent

Add Domain 1 and Domain 4 together and you get 60 percent of the exam. If you are short on study time, those two domains give you the highest return on investment.

### Performance-Based Questions

Performance-based questions — PBQs — are the most important strategic element of this exam. They appear at the beginning of the exam and simulate a real Linux environment. You might be dropped into a terminal and asked to configure a firewall rule, fix a broken fstab entry, write a crontab line, or correct file permissions.

Here is my strong recommendation: do not start with the PBQs. Skip them, flag them, and work through all the multiple-choice questions first. Come back to PBQs with your remaining time. There are two reasons for this. First, multiple-choice questions are faster and you will build confidence and momentum. Second, some of the multiple-choice questions may contain hints that help you answer the PBQs.

When you do get to a PBQ, read the entire scenario before you type a single character. Many students lose points by solving the wrong problem because they started typing immediately.

---

## [SECTION 2 — Domain 1: System Management — 3:30–9:00]

### Domain 1 Overview (32%)

Domain 1 is the largest single domain and covers everything you need to run a Linux system day to day. That includes installation, storage management, process management, service management, networking configuration, and scheduling. Let's walk through the major topics.

### Installation and Partitioning

The exam will test your knowledge of the Linux boot process — BIOS versus UEFI, the role of GRUB2 as the bootloader, and how the kernel hands control to systemd as PID 1. Know that `/etc/default/grub` is where you configure GRUB options and that `grub2-mkconfig` regenerates the configuration file.

For partitioning, know `fdisk` for MBR disks and `parted` or `gdisk` for GPT disks. Know the difference: MBR supports disks up to 2 TB and up to four primary partitions. GPT supports disks larger than 2 TB and up to 128 partitions. After partitioning, you format with `mkfs.ext4`, `mkfs.xfs`, or `mkfs.btrfs`. Remember that XFS is the default filesystem on RHEL-family distributions.

The `/etc/fstab` file is a frequent exam topic and a common PBQ. Know the six fields: device (preferably UUID), mount point, filesystem type, mount options, dump frequency, and fsck pass order. The command `blkid` gives you the UUID of any block device. Mounting with UUID instead of device name — like `sdb1` — is best practice because device names can change after reboot.

### LVM — Logical Volume Management

LVM comes up heavily on this exam. The workflow is: physical volumes first, then volume groups, then logical volumes. The commands follow that same order:

- `pvcreate /dev/sdb` creates a physical volume
- `vgcreate myvg /dev/sdb` creates a volume group
- `lvcreate -L 10G -n mylv myvg` creates a logical volume
- `mkfs.ext4 /dev/myvg/mylv` formats it
- `mount /dev/myvg/mylv /data` mounts it

To extend a logical volume: `lvextend -L +5G /dev/myvg/mylv`, then `resize2fs /dev/myvg/mylv` for ext4, or `xfs_growfs /data` for XFS. Note that you use the mount point with `xfs_growfs`, not the device path. That distinction is a common exam trap.

### RAID

Know the four RAID levels tested: RAID 0 (striping, no redundancy, best performance), RAID 1 (mirroring, full redundancy, requires 2 disks), RAID 5 (striping with parity, requires 3 disks minimum, can survive one disk failure), and RAID 10 (mirrored stripes, requires 4 disks). The command for software RAID is `mdadm`. Know `mdadm --create`, `mdadm --detail`, and `/proc/mdstat` for checking RAID status.

### Process and Service Management

For processes, the key commands are `ps aux` for a snapshot of all running processes, `top` and `htop` for interactive monitoring, and `kill` with signal numbers. Signal 15 — SIGTERM — is a graceful shutdown request. Signal 9 — SIGKILL — forces immediate termination with no cleanup. Always try SIGTERM before SIGKILL.

`nice` sets the priority when starting a process — values range from -20 (highest priority) to 19 (lowest). `renice` changes the priority of a running process.

For services, everything goes through `systemctl`. The six commands you must know cold: `systemctl start`, `systemctl stop`, `systemctl enable`, `systemctl disable`, `systemctl status`, and `systemctl daemon-reload`. The difference between `start` and `enable` is critical — `start` runs the service now, `enable` makes it start automatically at boot. These are not the same thing.

`journalctl` is the log viewer for systemd journals. Key flags: `-u servicename` filters by unit, `-b` shows logs since last boot, `-p err` filters by priority, and `-f` follows the log in real time like `tail -f`.

### Networking

For networking, the primary tool is `ip`. Know `ip addr show` to display IP addresses, `ip link set eth0 up` to bring an interface up, and `ip route show` to display the routing table. On RHEL systems, `nmcli` is the NetworkManager command-line tool — know `nmcli con show` and `nmcli con mod` for making persistent changes.

Key configuration files: `/etc/hostname` for the system hostname, `/etc/hosts` for local DNS resolution, `/etc/resolv.conf` for DNS server configuration, and `/etc/nsswitch.conf` for name resolution order.

### Scheduling

`crontab -e` opens the crontab editor for the current user. The five fields are: minute, hour, day of month, month, day of week — in that order. A common memory trick is "minute hour dom month dow." The `@reboot` special string runs a command once at boot. The `at` command schedules a one-time job.

---

## [SECTION 3 — Domain 2: Security — 9:00–13:30]

### Domain 2 Overview (21%)

Domain 2 covers everything security-related. This includes file permissions, user and group management, sudo configuration, SSH hardening, firewall configuration, SELinux, and AppArmor.

### File Permissions and Ownership

Know the octal permission system thoroughly. Read is 4, write is 2, execute is 1. So 755 means owner gets 7 (rwx), group gets 5 (r-x), others get 5 (r-x). Common values to memorize: 600 (owner read/write only — private key files), 644 (owner read/write, everyone reads), 755 (executable script or directory), 700 (owner only, private directory).

`chmod` changes permissions. `chown user:group file` changes both owner and group. `umask` sets the default permission mask — a umask of 022 on a file creation mode of 666 gives 644. Know how to calculate this.

Special permissions: the setuid bit (4000) runs a file as the owner. The setgid bit (2000) runs a file as the group or forces group inheritance in a directory. The sticky bit (1000) on a directory prevents users from deleting files they do not own — the classic example is `/tmp`.

### User and Group Management

`useradd -m -s /bin/bash username` creates a user with a home directory and bash shell. `usermod -aG groupname username` adds a user to a supplementary group — note the lowercase `-a` for append; without it you replace all groups. `userdel -r username` removes a user and their home directory.

`/etc/passwd` stores user account information. `/etc/shadow` stores hashed passwords — readable only by root. `/etc/group` stores group membership. Know which file contains what.

For sudo, `/etc/sudoers` is edited with `visudo` — never edit it directly because syntax errors lock you out. Know the syntax: `username ALL=(ALL) ALL` grants full sudo. `%groupname ALL=(ALL) ALL` grants sudo to a group.

### SSH Hardening

`/etc/ssh/sshd_config` is the server configuration file. The three most important hardening directives: `PermitRootLogin no` disables direct root login, `PasswordAuthentication no` forces key-based auth only, and `Port 22` (change this to a non-standard port to reduce automated attacks in production).

`ssh-keygen -t ed25519` generates an Ed25519 key pair — the modern preferred algorithm. `ssh-copy-id username@host` copies the public key to the remote server's `~/.ssh/authorized_keys`. After copying, test key-based login before disabling password auth or you will lock yourself out.

### Firewall Configuration

The exam covers both `firewalld` (RHEL-family) and `ufw` (Ubuntu). For firewalld: `firewall-cmd --permanent --add-service=http` adds a service permanently, `firewall-cmd --reload` applies changes, and `firewall-cmd --list-all` shows the current configuration. The `--permanent` flag is critical — without it changes are lost at next reload.

For ufw: `ufw enable` activates the firewall, `ufw allow 22/tcp` opens SSH, `ufw deny 23/tcp` blocks Telnet, and `ufw status verbose` shows all rules.

`iptables` is the lower-level tool. Know the three main chains: INPUT (incoming traffic), OUTPUT (outgoing traffic), FORWARD (traffic being routed through the system). `-A` appends a rule, `-I` inserts at the top, `-j ACCEPT` or `-j DROP` is the target action.

### SELinux and AppArmor

SELinux is the mandatory access control system on RHEL-family distributions. `getenforce` shows the current mode: Enforcing, Permissive, or Disabled. `setenforce 0` switches to Permissive temporarily. `sestatus` shows full status. When a service is blocked by SELinux, `ausearch -m avc -ts recent` searches the audit log for recent AVC denials. `restorecon -Rv /path` restores default SELinux file contexts. `setsebool -P boolean_name on` sets a boolean persistently.

AppArmor is the equivalent on Ubuntu/Debian. `aa-status` shows the current state, profiles, and which are in enforce versus complain mode. Profiles live in `/etc/apparmor.d/`.

---

## [SECTION 4 — Domain 3: Scripting, Containers, and Automation — 13:30–17:00]

### Domain 3 Overview (19%)

Domain 3 covers bash scripting, Git basics, Docker containers, and introductory automation concepts. This domain is worth 19 percent but students consistently underestimate it.

### Bash Scripting Fundamentals

Every script starts with a shebang: `#!/bin/bash`. Variables are assigned with no spaces around the equals sign — `NAME="Alice"` — and referenced with a dollar sign: `echo $NAME` or `echo ${NAME}`. The curly braces are required when the variable name is followed immediately by other characters.

Special variables to memorize: `$0` is the script name, `$1` through `$9` are positional arguments, `$#` is the count of arguments, `$@` is all arguments as separate words, and `$?` is the exit code of the last command. Zero means success. Non-zero means failure.

Conditionals use double brackets for safety: `[[ -f /etc/passwd ]]` tests if a file exists, `[[ -d /tmp ]]` tests for a directory, `[[ -z "$VAR" ]]` tests if a variable is empty, `[[ -n "$VAR" ]]` tests if it is non-empty. Numeric comparisons use `-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`.

Loops: a `for` loop iterates over a list or a range. A `while` loop runs while a condition is true. An `until` loop runs until a condition becomes true. Always use `break` to exit a loop early and `continue` to skip to the next iteration.

`sed` and `awk` are text processing tools that appear heavily on Domain 3 and Domain 4. `sed 's/old/new/g' file` replaces all occurrences of "old" with "new." `awk '{print $1, $3}' file` prints the first and third fields of each line. `grep -r "pattern" /dir` searches recursively.

### Git Basics

The exam tests basic Git operations. `git init` initializes a repository. `git clone URL` clones a remote repo. `git add filename` stages changes. `git commit -m "message"` commits staged changes. `git status` shows the current state. `git log` shows commit history. `git push` and `git pull` sync with the remote. `git branch` lists branches and `git checkout -b branchname` creates and switches to a new branch.

### Docker and Containers

Docker is the container platform tested on the exam. Key commands: `docker pull imagename` downloads an image, `docker run -d -p 8080:80 nginx` runs a container in detached mode with port mapping, `docker ps` lists running containers, `docker ps -a` includes stopped containers, `docker stop containerid` stops a container, `docker rm containerid` removes it, `docker logs containerid` shows output, and `docker exec -it containerid bash` opens an interactive shell.

Dockerfile directives: `FROM` specifies the base image, `RUN` executes a command during build, `COPY` copies files into the image, `CMD` specifies the default command when the container starts, and `EXPOSE` documents which port the container listens on. Know the difference between `CMD` and `ENTRYPOINT` — `CMD` provides defaults that can be overridden; `ENTRYPOINT` sets the fixed executable.

### Ansible Introduction

The exam introduces Ansible at a conceptual level. Know that Ansible is an agentless automation tool — it pushes configuration via SSH with no daemon required on managed nodes. Playbooks are YAML files that define automation tasks. The inventory file lists managed hosts. A play maps hosts to tasks, and a task calls a module. Common modules include `apt`, `yum`, `copy`, `template`, `service`, and `user`.

---

## [SECTION 5 — Domain 4: Troubleshooting — 17:00–20:30]

### Domain 4 Overview (28%)

Domain 4 is worth 28 percent and it is entirely scenario-based — you read a problem description and identify the correct diagnostic or remediation command. Let's go subsystem by subsystem.

### Boot Troubleshooting

If a system fails to boot, the first places to check are the GRUB menu and the boot logs. Editing a GRUB entry temporarily to add `rd.break` (RHEL) or `init=/bin/bash` (generic) drops you to a rescue shell. From there you can remount the root filesystem read-write and make repairs.

`systemctl list-units --state=failed` shows all failed units. `journalctl -b -p err` shows all errors from the current boot. `journalctl -b -1 -p err` shows errors from the previous boot — very useful when the system rebooted due to a failure.

### Log Analysis

Know where the important log files are. On RHEL-family: `/var/log/messages` for general system messages, `/var/log/secure` for authentication events, `/var/log/audit/audit.log` for SELinux/audit events. On Ubuntu/Debian: `/var/log/syslog` for system messages, `/var/log/auth.log` for authentication. `/var/log/dmesg` contains kernel ring buffer messages from boot on both families. `dmesg | tail -20` shows the most recent kernel messages.

### Network Troubleshooting

The systematic approach: layer by layer from physical to application. Check interface status with `ip link show`. Check IP address assignment with `ip addr show`. Test local connectivity with `ping localhost`. Test gateway with `ping defaultgateway`. Test DNS with `dig` or `nslookup`. Test a remote host with `traceroute` or `tracepath`.

`ss -tuln` shows all listening sockets — TCP and UDP, with port numbers, without resolving names. This replaces the older `netstat`. If a service should be listening on port 443 but nothing appears in `ss -tuln`, the service is not running or is misconfigured.

`dig @8.8.8.8 example.com A` queries Google's DNS for the A record of example.com — useful for testing DNS resolution against a specific server.

### Disk and Storage Troubleshooting

`df -h` shows filesystem usage in human-readable format. When `/var` is 100 percent full, services fail — check this first on any service failure. `du -sh /var/log/*` identifies which logs are consuming space. `lsblk` shows all block devices and their mount points in a tree format.

`fsck` checks filesystem integrity. It must be run on unmounted filesystems — running fsck on a mounted filesystem will corrupt it. Boot to a rescue mode to run fsck on the root filesystem.

`vmstat 1 5` shows system statistics five times at one-second intervals. The `wa` column (I/O wait) indicates the percentage of time the CPU is waiting for disk I/O. High I/O wait means a disk bottleneck, not a CPU bottleneck.

### Package Integrity Verification

`rpm -V packagename` verifies the integrity of an installed RPM package, comparing installed files against the original package database. An `S` in the output means size mismatch — a sign of modification or corruption. On Debian systems, `dpkg --verify packagename` performs the same function.

`strace -p PID` attaches to a running process and shows all system calls — useful for diagnosing processes that are hung or failing silently.

---

## [SECTION 6 — Exam Strategy and Distractor Elimination — 20:30–23:00]

### Exam Strategy

Here is the complete exam day strategy in order:

First, when the exam starts, do a brain dump. Write down on scratch paper any commands, file paths, or syntax you are afraid of forgetting. Get it out of your head and onto paper in the first two minutes.

Second, skip PBQs on the first pass. Flag them and move to multiple-choice questions. Work through all multiple choice, flagging anything uncertain.

Third, go back to PBQs with remaining time. Read the full scenario. Identify the exact task being asked. Think about the command before you type it. Use any available man pages within the simulation.

Fourth, before time expires, answer every remaining flagged question — guess if necessary. There is no penalty for wrong answers.

### Common Exam Traps

Trap one: confusing `start` with `enable`. "Start" runs the service now. "Enable" makes it start at boot. A question asking how to ensure a service starts after reboot wants `enable`, not `start`.

Trap two: `lvextend` without resizing the filesystem. Extending the logical volume does not automatically extend the filesystem. You must follow `lvextend` with `resize2fs` (ext4) or `xfs_growfs` (xfs).

Trap three: `firewall-cmd` without `--permanent`. Changes without `--permanent` are lost at next reload. A question asking for a "persistent" rule requires both the `--permanent` flag and `--reload`.

Trap four: editing `/etc/sudoers` directly instead of with `visudo`. The exam will present both as options. Always use `visudo`.

Trap five: confusing the RHEL and Ubuntu log paths. `/var/log/secure` is RHEL. `/var/log/auth.log` is Ubuntu. If the scenario mentions Ubuntu, pick the Ubuntu path.

### Distractor Elimination Framework

When you see a question with four answers, eliminate using these rules:

Rule 1: Eliminate any answer that would cause data loss without being explicitly asked about data loss.

Rule 2: Eliminate any answer that uses a command for the wrong distribution — if the scenario says Ubuntu, eliminate RHEL-specific commands.

Rule 3: Eliminate any answer that omits a required flag for a persistent change — particularly `--permanent` for firewalld.

Rule 4: When two answers look almost identical except for one flag, that flag is the key — figure out what the flag does and choose accordingly.

Rule 5: If you genuinely do not know, choose the answer that is most conservative, most complete, or most reversible.

---

## [OUTRO — 23:00–24:00]

And that is our complete Linux+ XK0-005 exam preparation review. You have covered over fifteen weeks of Linux administration content — installation, filesystems, permissions, users, packages, processes, services, storage, networking, SSH, firewalls, logging, scripting, containers, and troubleshooting. That is the full domain map of the Linux+ exam.

Use the reading guide for your final command-by-command review. Complete the practice quiz and look up the reasoning behind every question you get wrong — not just the right answer, but why the other options are wrong. Review the CompTIA exam objectives document from comptia.org and make sure you can explain every single objective in your own words.

Your final lab this week is a comprehensive command review — work through every command recap in the reading guide in a live VM. Muscle memory matters on PBQs.

This has been a great semester. The work you have done in this course is real Linux administration skill. Good luck on the exam, and I will see you in the final course discussions.

---

## [END OF SCRIPT]

---

### Instructor Notes

- Total estimated duration: 21–23 minutes at a measured instructional pace.
- Recommend pausing after each domain for a 30-second summary card on screen listing 3–5 key commands from that domain.
- The distractor elimination section works best if delivered conversationally — consider ad-libbing examples from the course labs.
- Supplement this script with the companion reading guide (02_Reading_Guide_Module_16.md) and lab (03_Lab_Module_16.md).
