# Video Script: Module 16 — Linux+ XK0-005 Exam Preparation (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 16: Linux+ XK0-005 Exam Preparation.

This is the final module of CIS-3325. You've covered the full breadth of Linux administration — from user management and shell scripting through networking, storage, SSH, and security hardening. Now it's time to consolidate that knowledge, understand the exam's structure and emphasis, and develop a test-taking strategy that positions you for success on exam day.

Part 1 reviews the exam structure, Domain 1 (System Management) and Domain 2 (Security), with targeted coverage of the highest-frequency topic areas. Part 2 covers Domain 3 (Scripting, Containers, and Automation) and Domain 4 (Troubleshooting), plus exam strategy and a full 20-question practice set.

Let's get ready to pass.

---

### Section 1: Exam Overview — XK0-005

**Exam Facts**

- **Exam code**: XK0-005
- **Number of questions**: Maximum 90
- **Question types**: Multiple choice, multiple-response, drag-and-drop, performance-based (simulations)
- **Time limit**: 90 minutes
- **Passing score**: 720 out of 900
- **Exam cost**: $358 USD (voucher discounts available)
- **Validity**: CompTIA certs expire 3 years from date of earn; renew via CE credits or retaking

**Domain Breakdown**

| Domain | Title | Exam Weight |
|--------|-------|-------------|
| 1 | System Management | 32% |
| 2 | Security | 21% |
| 3 | Scripting, Containers, and Automation | 19% |
| 4 | Troubleshooting | 28% |

Domain 1 and Domain 4 together account for 60% of the exam. Master those first.

**Performance-Based Questions**

Performance-based questions (PBQs) present a simulated Linux environment where you must complete actual tasks. You are not selecting from answers — you are typing commands. PBQs appear at the beginning of the exam. They are:

- Worth more points than standard questions
- Time-consuming — budget 10–15 minutes for a single PBQ
- Testing real command syntax, not just conceptual knowledge

Strategy: If a PBQ is unclear, skip it, complete the multiple choice questions, and return. Partial credit is sometimes awarded.

---

### Section 2: Domain 1 — System Management Review

Domain 1 is the largest domain. Let's hit the highest-frequency topics.

**1.1 Linux Filesystem Hierarchy**

The Linux Filesystem Standard (FHS) is tested every exam:

| Directory | Contents |
|-----------|----------|
| `/bin` | Essential user command binaries |
| `/sbin` | Essential system administration binaries |
| `/etc` | Configuration files |
| `/home` | User home directories |
| `/var` | Variable data (logs, mail, spool) |
| `/tmp` | Temporary files |
| `/proc` | Kernel and process virtual filesystem |
| `/sys` | Kernel device and driver virtual filesystem |
| `/dev` | Device files |
| `/usr` | User utilities and applications |
| `/opt` | Optional third-party software |
| `/lib` | Shared libraries |
| `/boot` | Boot loader files and kernel |
| `/mnt` | Temporary mount point |
| `/media` | Removable media mount points |

**1.2 User and Group Management**

High-frequency commands:

```bash
useradd -m -s /bin/bash -G wheel username   # Create user with home dir and group
usermod -aG docker username                  # Add user to additional group
userdel -r username                          # Delete user and home dir
passwd username                              # Set password
id username                                  # View UID, GID, groups
groups username                              # List user's groups
```

Key files:

- `/etc/passwd` — user accounts (colon-delimited, 7 fields)
- `/etc/shadow` — hashed passwords and aging info
- `/etc/group` — group definitions
- `/etc/gshadow` — group passwords

`/etc/passwd` field order: `username:password:UID:GID:GECOS:home:shell`

**1.3 File Permissions and Special Bits**

Permission bits review:

- `4` = read, `2` = write, `1` = execute
- `chmod 755` = `rwxr-xr-x`
- `chmod 644` = `rw-r--r--`

Special permission bits:

- **SUID (4)**: Execute with owner's privileges (`chmod u+s` or `chmod 4755`)
- **SGID (2)**: Execute with group's privileges; on directory = new files inherit group
- **Sticky bit (1)**: On directory = only file owner can delete their files (`chmod +t`)

Find SUID files:

```bash
find / -perm /4000 -type f 2>/dev/null
```

**1.4 Package Management**

| Distribution | Package Manager | Commands |
|-------------|----------------|----------|
| RHEL/Rocky | dnf (rpm) | `dnf install`, `dnf remove`, `dnf update`, `dnf search` |
| Debian/Ubuntu | apt (dpkg) | `apt install`, `apt remove`, `apt update`, `apt upgrade` |

Repository configuration:

- RHEL: `/etc/yum.repos.d/*.repo`
- Debian: `/etc/apt/sources.list` and `/etc/apt/sources.list.d/`

**1.5 Processes and Signals**

Key process commands:

```bash
ps aux                   # All processes, extended format
top / htop               # Interactive process monitor
kill -9 PID              # SIGKILL — unblockable kill
kill -15 PID             # SIGTERM — graceful termination (default)
kill -1 PID              # SIGHUP — reload configuration
kill -2 PID              # SIGINT — keyboard interrupt (Ctrl+C)
pgrep -f processname     # Find process by name pattern
pkill processname        # Kill by name
nice -n 10 command       # Start with priority 10
renice -n 5 -p PID       # Change running process priority
```

**1.6 Storage — LVM and Filesystems**

Key commands and their sequence:

```
pvcreate → vgcreate → lvcreate → mkfs → mount → fstab
```

LVM extension:

```bash
lvextend -L +10G -r /dev/vg0/lv0    # -r auto-resizes filesystem
```

fstab field order: device, mount point, fstype, options, dump, pass

**1.7 systemd**

Must-know systemctl operations:

```bash
systemctl start|stop|restart|reload|enable|disable|mask|status
systemctl is-enabled|is-active|is-failed
systemctl list-units --type=service
systemctl get-default
systemctl set-default multi-user.target
journalctl -u service -f -b -p err
```

Unit file location precedence: `/etc/systemd/system/` > `/lib/systemd/system/`

---

### Section 3: Domain 2 — Security Review

Domain 2 covers 21% of the exam. The Linux+ XK0-005 places significant emphasis on security topics that were lighter in previous versions.

**2.1 File Permissions Security**

Beyond basic permissions, know these security-related permission topics:

```bash
# Find world-writable files (potential security risk):
find / -perm -o+w -type f 2>/dev/null

# Find files with no owner:
find / -nouser -o -nogroup 2>/dev/null

# Set immutable attribute (cannot be modified even by root):
sudo chattr +i /etc/passwd
lsattr /etc/passwd
```

**2.2 SELinux**

High-frequency SELinux exam topics:

- What `getenforce` returns (Enforcing/Permissive/Disabled)
- What `setenforce 0` does (switch to permissive, NOT disable)
- Configuration file: `/etc/selinux/config`
- Context format: `user:role:type:level`
- Fix wrong context: `restorecon -Rv /path`
- Permanent context: `semanage fcontext -a -t type_t /path`
- Booleans: `getsebool -a`, `setsebool -P boolean on`
- Troubleshooting: `ausearch -m avc`, `audit2why`, `audit2allow`

**2.3 SSH Hardening**

Key `sshd_config` directives tested:

- `PermitRootLogin no`
- `PasswordAuthentication no`
- `MaxAuthTries 3`
- `AllowUsers` / `AllowGroups`
- `ClientAliveInterval` / `ClientAliveCountMax`

Key file permissions:

- `~/.ssh/` must be `700`
- `~/.ssh/authorized_keys` must be `600`
- `~/.ssh/id_*` (private key) must be `600`

**2.4 Firewall**

firewalld concepts:

- Zones are trust levels per interface/source
- `--permanent` requires `--reload` to take effect
- `firewall-cmd --list-all` shows current zone rules

iptables chain order: INPUT (incoming), OUTPUT (outgoing), FORWARD (routed)

**2.5 auditd and Logging**

- Audit log: `/var/log/audit/audit.log`
- Watch file: `auditctl -w /path -p wa -k keyname`
- Search: `ausearch -k keyname -ts today`
- Report: `aureport --summary`

**2.6 Password Security**

- `/etc/login.defs` — defaults for new accounts
- `chage` — per-user aging settings
- `pam_pwquality` — password complexity
- `pam_faillock` — account lockout

---

### Summary — Part 1

Part 1 reviewed the exam structure and the two largest content areas:

- Domain 1 (32%): filesystem hierarchy, user management, permissions, package management, processes, storage, systemd
- Domain 2 (21%): SELinux, SSH hardening, firewall management, auditd, password policies

Key exam preparation insight: the Linux+ exam tests command syntax precisely. Know the flags. Know the file paths. Know the output format of common commands.

In Part 2: Domain 3 (scripting, containers, Ansible), Domain 4 (troubleshooting), exam strategy tips, and 20 practice questions.
