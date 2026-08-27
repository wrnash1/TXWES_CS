# Reading Guide: Module 16 — Linux+ XK0-005 Exam Preparation

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This guide is your comprehensive exam preparation reference. It consolidates key facts, commands, and concepts from all 16 modules, organized by exam domain. Use it as a study guide in the final days before your exam. Estimated review time: 3–4 hours.

---

### How to Use This Guide

1. Read each section and check your recall without looking at the answers
2. Mark items you are unsure of with a star
3. Return to the original module material for starred items
4. Complete the 20 practice questions at the end of the quiz file
5. Review your weak areas 24 hours before the exam

---

### Domain 1: System Management (32%)

**Objective 1.1 — Summarize Linux Fundamentals**

Key items:

- Linux kernel version: `uname -r`
- Distribution info: `cat /etc/os-release`
- System uptime: `uptime`
- Running processes: `ps aux`, `top`
- Hardware info: `lscpu`, `lsmem`, `lsblk`, `lspci`, `lsusb`

Kernel ring buffer:

```bash
dmesg
dmesg | grep -i error
journalctl -k
```

**Objective 1.2 — Manage Files and Directories**

Filesystem hierarchy — commit this to memory:

| Path | Contents |
|------|----------|
| `/etc` | System-wide configuration files |
| `/var/log` | Log files |
| `/tmp` | Temporary files (cleared on boot) |
| `/proc` | Virtual filesystem for kernel/process info |
| `/sys` | Virtual filesystem for kernel/hardware info |
| `/dev` | Device files (block, character, special) |

File operations:

```bash
cp -a src dest        # Archive copy (preserves all attributes)
mv file newname       # Move or rename
ln file hardlink      # Hard link
ln -s target symlink  # Symbolic link
find / -name "*.conf" -type f
find / -mtime -7      # Modified in last 7 days
find / -size +100M    # Larger than 100 MB
```

Archive and compression:

```bash
tar -czf archive.tar.gz directory/   # Create gzipped tar
tar -xzf archive.tar.gz              # Extract gzipped tar
tar -cjf archive.tar.bz2 directory/  # bzip2 compression
tar -tf archive.tar.gz               # List contents
gzip file.txt                        # Compress to file.txt.gz
gunzip file.txt.gz                   # Decompress
```

**Objective 1.3 — Configure and Manage Storage**

LVM command sequence: `pvcreate` → `vgcreate` → `lvcreate` → `mkfs` → `mount`

Critical LVM exam syntax:

```bash
pvcreate /dev/sdb
vgcreate vgname /dev/sdb
lvcreate -L 10G -n lvname vgname
lvcreate -l 100%FREE -n lvname vgname
lvextend -L +5G -r /dev/vgname/lvname    # -r resizes filesystem
mkfs.ext4 /dev/vgname/lvname
mkfs.xfs /dev/vgname/lvname
```

fstab fields: `device mountpoint fstype options dump pass`

RAID usable capacity:

- RAID 0: N × disk (no redundancy)
- RAID 1: 1 × disk (mirror)
- RAID 5: (N-1) × disk (1 disk parity)
- RAID 6: (N-2) × disk (2 disk parity)
- RAID 10: N/2 × disk (mirror + stripe)

**Objective 1.4 — Configure and Manage Network Interfaces**

Network commands:

```bash
ip addr show
ip route show
ip link set eth0 up
nmcli connection show
nmcli connection add type ethernet ...
hostnamectl set-hostname newname
```

DNS files:

- `/etc/hosts` — local name resolution
- `/etc/resolv.conf` — DNS server config
- `/etc/nsswitch.conf` — resolution order (`hosts: files dns`)

**Objective 1.5 — Manage Packages and Software**

| Task | RHEL/Rocky | Debian/Ubuntu |
|------|-----------|---------------|
| Install | `dnf install` | `apt install` |
| Remove | `dnf remove` | `apt remove` |
| Update | `dnf update` | `apt update && apt upgrade` |
| Search | `dnf search` | `apt search` |
| Info | `dnf info` | `apt show` |
| List installed | `rpm -qa` | `dpkg -l` |
| Query file owner | `rpm -qf /path` | `dpkg -S /path` |
| List package files | `rpm -ql package` | `dpkg -L package` |

**Objective 1.6 — Identify and Configure User and Group Accounts**

```bash
useradd -m -s /bin/bash -G sudo username
usermod -aG groupname username    # APPEND to groups
userdel -r username
passwd -l username                # Lock account
passwd -u username                # Unlock account
chage -l username                 # View aging settings
su - username                     # Switch user (login shell)
sudo -u username command          # Run as another user
```

/etc/passwd field order: `username:x:UID:GID:comment:home:shell`

**Objective 1.7 — Manage Services**

```bash
systemctl start|stop|restart|reload service
systemctl enable|disable|mask|unmask service
systemctl enable --now service        # Start AND enable
systemctl is-enabled|is-active service
systemctl list-units --type=service --state=running
systemctl --failed
journalctl -u service -f             # Follow service logs
journalctl -u service -b             # Current boot
journalctl -u service -p err         # Errors only
journalctl -u service --since "1h ago"
```

Target equivalents:

- `multi-user.target` = runlevel 3
- `graphical.target` = runlevel 5
- `rescue.target` = runlevel 1
- `poweroff.target` = runlevel 0
- `reboot.target` = runlevel 6

---

### Domain 2: Security (21%)

**Objective 2.1 — Implement and Configure Linux OS Security**

File permission commands:

```bash
chmod 755 file        # rwxr-xr-x
chmod u+s file        # Add SUID
chmod g+s directory   # Add SGID (new files inherit group)
chmod +t directory    # Set sticky bit
chown user:group file
chgrp group file
getfacl file          # View ACL
setfacl -m u:user:rw file   # Add ACL entry
```

**Objective 2.2 — Configure Linux Security Controls**

SELinux quick reference:

```bash
getenforce
setenforce 0|1
sestatus
ls -Z /path
ps -Z
restorecon -Rv /path
semanage fcontext -a -t type_t "/path(/.*)?"
getsebool -a | grep httpd
setsebool -P boolean on
ausearch -m avc -ts recent
audit2why < /var/log/audit/audit.log
```

**Objective 2.3 — Implement Identity Management**

LDAP/Kerberos are tested conceptually:

- LDAP (Lightweight Directory Access Protocol) — centralized user authentication
- Kerberos — ticket-based authentication for network services
- SSSD (System Security Services Daemon) — integrates Linux with LDAP/Kerberos
- PAM — authentication framework; modules in `/etc/pam.d/`

**Objective 2.4 — Configure SSH**

```bash
ssh-keygen -t ed25519 -C "comment"
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host
ssh -L local:remotehost:remote user@sshserver   # Local forward
ssh -R remote:localhost:local user@sshserver    # Remote forward
ssh -D 1080 user@sshserver                      # Dynamic (SOCKS)
scp -P 2222 file user@host:/path               # Note uppercase -P
```

---

### Domain 3: Scripting, Containers, and Automation (19%)

**Objective 3.1 — Create Simple Shell Scripts**

Script skeleton:

```bash
#!/bin/bash
set -euo pipefail    # Exit on error, unset var, pipe failure

VARIABLE="value"
RESULT=$(command)

if [ condition ]; then
    action
fi

for item in list; do
    action
done

function name() {
    local var="$1"
}
```

Environment variables:

- `$HOME` — home directory
- `$PATH` — command search path
- `$USER` — current username
- `$SHELL` — current shell
- `$?` — last exit code
- `$$` — current PID
- `$#` — number of arguments
- `$@` — all arguments
- `$1`, `$2`... — positional parameters

**Objective 3.2 — Perform Version Control Using Git**

```bash
git init
git clone url
git status
git add file
git commit -m "message"
git push origin main
git pull
git branch
git checkout -b newbranch
git merge branch
```

**Objective 3.3 — Use Docker and Containers**

```bash
docker pull image:tag
docker run -d -p hostport:containerport --name name image
docker exec -it container bash
docker logs container
docker stop container && docker rm container
docker images && docker rmi image
docker build -t name:tag .
docker-compose up -d
docker-compose down
```

**Objective 3.4 — Summarize Orchestration Concepts**

- Kubernetes (K8s): container orchestration platform
- Pod: smallest K8s unit (one or more containers)
- Deployment: manages pod replicas
- Service: exposes pods to network traffic
- kubectl: Kubernetes CLI

---

### Domain 4: Troubleshooting (28%)

**Objective 4.1 — Analyze and Troubleshoot Storage Issues**

```bash
lsblk                             # Block device overview
df -hT                            # Filesystem usage with type
df -i                             # Inode usage
du -sh /var/log                   # Directory size
find / -size +100M -type f        # Large files
smartctl -a /dev/sda              # Disk health
fsck /dev/sdb1                    # Filesystem check (unmounted!)
```

Common storage errors:

- "No space left on device" + `df -h` shows space: check `df -i` (inodes full)
- "Read-only file system": filesystem mounted ro due to errors; `dmesg` for details
- "Input/output error": hardware failure; check SMART data immediately

**Objective 4.2 — Analyze and Troubleshoot Network Issues**

Troubleshooting sequence:

```bash
ip link show                     # Interface state
ip addr show                     # IP assignment
ip route show                    # Routing table
ping -c 3 <gateway>              # L3 reachability
ping -c 3 8.8.8.8                # Internet routing
ping -c 3 google.com             # DNS resolution
ss -tlnp                         # What's listening
sudo tcpdump -i eth0 host target # Packet capture
```

**Objective 4.3 — Analyze and Troubleshoot CPU and Memory Issues**

```bash
uptime                            # Load averages
top                               # Real-time overview
vmstat 1 5                        # CPU/memory stats
free -h                           # Memory usage
sar -u 5 3                        # CPU stats (5-sec interval, 3 samples)
sar -r 5 3                        # Memory stats
ps aux --sort=-%cpu | head -10    # Top CPU consumers
ps aux --sort=-%mem | head -10    # Top memory consumers
```

**Objective 4.4 — Analyze and Troubleshoot User and File Issues**

```bash
ls -la /path                     # Permissions and ownership
getfacl /path                    # ACL entries
ls -Z /path                      # SELinux context
ausearch -m avc -ts recent       # SELinux denials
id username                       # User's UID/GID/groups
last                             # Login history
lastb                            # Failed login history
who                              # Currently logged in users
```

---

### High-Value Flash Card Topics

These are frequently tested on Linux+ exams. Know them cold:

- The 7 fields of `/etc/passwd` in order
- The crontab field order: `minute hour day-of-month month day-of-week`
- fstab field order: `device mountpoint fstype options dump pass`
- `useradd -G` replaces groups; `usermod -aG` appends to groups
- `scp` uses uppercase `-P` for port
- `lvextend -r` resizes both LV and filesystem
- `setenforce 0` = permissive; it does NOT disable SELinux
- `--permanent` in firewall-cmd requires `--reload`
- `systemctl enable` ≠ `systemctl start`
- RAID 5 minimum 3 disks; RAID 10 minimum 4 disks

---

### Additional Resources

- CompTIA Linux+ XK0-005 Exam Objectives: [comptia.org](https://comptia.org)
- Professor Messer's CompTIA Linux+ video series (free)
- Linux+ Study Guide by Richard Blum and Christine Bresnahan
- `man` pages for every command covered in this course
- The Linux Documentation Project: [tldp.org](https://www.tldp.org)
- Linux Journey: [linuxjourney.com](https://linuxjourney.com)

---

### Final Encouragement

The Linux+ XK0-005 is a challenging but achievable certification. Students who complete CIS-3325 have covered every major topic area tested on the exam. The students who pass are the ones who:

1. Actually practice the commands in a lab environment
2. Can type the syntax without looking it up
3. Have a systematic troubleshooting approach they can apply under pressure

You have done the work. Trust your preparation.

---

## 9. Supplemental Resources

**1. [CompTIA Linux+ XK0-005 Exam Objectives — CompTIA.org](https://www.comptia.org/certifications/linux)**
The official exam objectives document from CompTIA. This is the authoritative blueprint for the XK0-005 exam, listing all four domains (System Management, Security, Scripting, Automation and Containers, and Troubleshooting), their percentage weights, and the specific skill areas tested. Reading this document before your final review session helps you identify gaps between what you have studied and what the exam specifically covers. Available as a free PDF download.

**2. [Professor Messer's CompTIA Linux+ Course Notes — professormesser.com](https://www.professormesser.com/linux-plus/xk0-005/xk0-005-video/comptia-linux-plus-course-notes/)**
Professor Messer's free Linux+ course notes companion to his video series. Organized by exam domain and objective, these notes provide concise summaries of key concepts in a format designed for exam review. Particularly useful in the final week before the exam when reviewing breadth rather than depth. The video series (available free on YouTube) is the most-recommended supplemental resource among Linux+ candidates.

**3. [Linux Journey — linuxjourney.com](https://linuxjourney.com/)**
An interactive, self-paced Linux learning platform covering all core administration topics: command line, text processing, user management, filesystems, networking, processes, and more. Each lesson includes exercises and quizzes. Linux Journey is especially useful for reinforcing the hands-on command syntax that the Linux+ performance-based questions test — the questions that require you to type actual commands rather than select from multiple choice options.
