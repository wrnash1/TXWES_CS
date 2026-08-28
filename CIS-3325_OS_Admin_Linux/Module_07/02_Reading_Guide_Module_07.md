# Reading Guide: Module 07 — User and Group Administration

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Overview

This reading guide expands on the video lecture content for Module 7. It provides reference material, deeper explanations, and additional context you will need for the lab, quiz, and exam. Work through each section carefully and use the command references when practicing in your lab environment.

**Estimated Reading Time:** 45–60 minutes

---

## Section 1 — Linux Identity Architecture

### 1.1 Users and the Principle of Least Privilege

Linux implements the Principle of Least Privilege at its core. Every process runs with the minimum permissions needed to do its job. A web server process should not run as root; it should run as `www-data` or `apache` — a dedicated low-privilege system account.

This design means that if a web server process is compromised by an attacker, the damage is limited to what the `www-data` user can access. If it ran as root, a single exploit would give an attacker full control of the system.

### 1.2 UID and GID Ranges

UID (User ID) and GID (Group ID) are the numbers the kernel actually uses for access control. Usernames and group names are human-readable labels that the system resolves to these numbers.

Standard ranges (defined in `/etc/login.defs`):

| Range | Purpose |
|---|---|
| 0 | Root (superuser) |
| 1–199 | System accounts (distro-controlled) |
| 200–499 | System accounts (admin-assigned) |
| 500–999 | Service accounts (varies by distro) |
| 1000+ | Regular user accounts |

On older RHEL systems, regular users started at UID 500. Modern RHEL/Debian systems start at 1000. The `UID_MIN` and `UID_MAX` values in `/etc/login.defs` control where `useradd` assigns UIDs automatically.

### 1.3 The Name Service Switch

Linux does not require users to be defined in local files. The Name Service Switch (NSS), configured in `/etc/nsswitch.conf`, defines the order in which identity sources are consulted.

```bash
# View NSS configuration
cat /etc/nsswitch.conf

# Typical passwd line:
# passwd:  files systemd
# or in an LDAP environment:
# passwd:  files ldap
```

The `getent` command respects NSS configuration. Using `getent passwd` shows all users from all configured sources, while `grep /etc/passwd` only shows local users. In enterprise environments, always use `getent`.

---

## Section 2 — Core Configuration Files

### 2.1 /etc/passwd — Detailed Field Reference

```
jsmith:x:1001:1001:John Smith,Engineering,555-1234:/home/jsmith:/bin/bash
  [1]  [2] [3] [4]        [5]                       [6]          [7]
```

| Field | Name | Notes |
|---|---|---|
| 1 | Username | Max 32 characters; lowercase convention |
| 2 | Password | `x` = hash in shadow; `*` = no login |
| 3 | UID | Kernel identity number |
| 4 | GID | Primary group ID |
| 5 | GECOS | Name, office, phone (comma-separated) |
| 6 | Home Directory | Created by `useradd -m` |
| 7 | Shell | `/sbin/nologin` for service accounts |

The GECOS field is parsed by programs like `finger` and `chfn`. The `chfn` command (change finger information) allows users to update their own GECOS data.

### 2.2 /etc/shadow — Detailed Field Reference

```
jsmith:$6$salt$hash:19500:0:90:14:30:20000:
  [1]     [2]         [3]  [4][5][6] [7] [8] [9]
```

| Field | Name | Value Meaning |
|---|---|---|
| 1 | Username | Must match /etc/passwd |
| 2 | Hash | `$6$`=SHA-512; `!`=locked; `*`=disabled |
| 3 | Last Changed | Days since epoch (Jan 1, 1970) |
| 4 | Minimum Age | Days before user can change password |
| 5 | Maximum Age | Days before password must change |
| 6 | Warning Period | Days before expiration to warn user |
| 7 | Inactive Period | Days after expiration to disable account |
| 8 | Expiration Date | Absolute date in epoch days; empty=never |
| 9 | Reserved | Unused; must be blank |

Hash algorithm prefixes:

- `$1$` — MD5 (obsolete, insecure)
- `$5$` — SHA-256
- `$6$` — SHA-512 (widely used)
- `$y$` — yescrypt (default on Fedora 35+, Ubuntu 22.04+)
- `$2b$` — bcrypt (some configurations)

The epoch day calculation: divide UNIX timestamp by 86400 (seconds per day). For example, January 15, 2024 is day 19737.

### 2.3 /etc/group — Detailed Field Reference

```
developers:x:1050:jsmith,awilson,mthompson
    [1]    [2] [3]       [4]
```

| Field | Name | Notes |
|---|---|---|
| 1 | Group Name | Follows same naming rules as usernames |
| 2 | Password | `x` = check /etc/gshadow |
| 3 | GID | Group ID number |
| 4 | Members | Users for whom this is supplementary |

A user's primary group is recorded in field 4 of `/etc/passwd`. That user does not need to appear in the member list of `/etc/group` for their primary group. They are members implicitly.

### 2.4 /etc/gshadow

`/etc/gshadow` stores group passwords and group administrator lists. This file is rarely used in modern environments but appears on the exam.

```bash
# Format: groupname:password:admins:members
# developers:!:jsmith:awilson,mthompson

# Set a group password (allows non-members to join temporarily with 'newgrp')
sudo gpasswd developers

# Set a group administrator
sudo gpasswd -A jsmith developers

# Join a group temporarily (prompts for group password)
newgrp developers
```

### 2.5 /etc/login.defs

This file controls system-wide defaults for user account creation:

```bash
cat /etc/login.defs

# Key parameters:
# UID_MIN           1000    — Minimum UID for regular users
# UID_MAX           60000   — Maximum UID for regular users
# GID_MIN           1000    — Minimum GID for regular groups
# GID_MAX           60000   — Maximum GID for regular groups
# PASS_MAX_DAYS     99999   — Maximum password age
# PASS_MIN_DAYS     0       — Minimum password age
# PASS_WARN_AGE     7       — Warning days before expiration
# CREATE_HOME       yes     — Create home dir by default (RHEL)
# ENCRYPT_METHOD    SHA512  — Hash algorithm
# UMASK             022     — Default file creation mask
```

---

## Section 3 — User Account Management Commands

### 3.1 useradd Complete Reference

```bash
# Common flags:
# -m, --create-home     Create home directory
# -M, --no-create-home  Do not create home directory
# -d, --home-dir DIR    Set home directory path
# -s, --shell SHELL     Set login shell
# -u, --uid UID         Set specific UID
# -g, --gid GROUP       Set primary group
# -G, --groups GROUPS   Set supplementary groups (comma-separated)
# -c, --comment TEXT    Set GECOS field
# -e, --expiredate DATE Set account expiration (YYYY-MM-DD)
# -f, --inactive DAYS   Set inactive period
# -r, --system          Create system account
# -k, --skel DIR        Use alternate skeleton directory
# -p, --password HASH   Set encrypted password (use passwd instead)

# Create a complete user account
sudo useradd \
  -m \
  -c "Alice Wilson, DevOps Engineer" \
  -s /bin/bash \
  -G developers,docker,sudo \
  -e 2026-12-31 \
  awilson

# View useradd defaults
useradd -D

# Change useradd defaults
sudo useradd -D -s /bin/bash    # Change default shell
sudo useradd -D -b /home        # Change default base directory
```

### 3.2 passwd and chage Complete Reference

```bash
# passwd flags:
# -l, --lock       Lock account
# -u, --unlock     Unlock account
# -d, --delete     Delete password (account becomes passwordless)
# -e, --expire     Force password change at next login
# -n DAYS          Set minimum password age
# -x DAYS          Set maximum password age
# -w DAYS          Set warning days
# -i DAYS          Set inactive days
# -S, --status     Show status summary

# chage flags (the exam heavily tests these):
# -l, --list       Show aging info
# -d DATE          Set last password change date
# -m DAYS          Set minimum age
# -M DAYS          Set maximum age
# -W DAYS          Set warning days
# -I DAYS          Set inactive days
# -E DATE          Set account expiration date

# Set full aging policy for a new employee
sudo chage -m 1 -M 90 -W 14 -I 30 -E 2026-12-31 jsmith

# Expire password immediately (force change at next login)
sudo chage -d 0 jsmith

# Remove account expiration
sudo chage -E -1 jsmith

# Interactive mode
sudo chage jsmith
```

### 3.3 usermod Complete Reference

```bash
# usermod flags (mirror useradd flags):
# -l, --login NEW_NAME  Change login name
# -d, --home DIR        Change home directory
# -m, --move-home       Move home directory contents (use with -d)
# -s, --shell SHELL     Change login shell
# -u, --uid UID         Change UID
# -g, --gid GROUP       Change primary group
# -G, --groups GROUPS   Set supplementary groups (replaces existing!)
# -a, --append          Append to supplementary groups (ALWAYS use with -G)
# -c, --comment TEXT    Change GECOS field
# -e, --expiredate DATE Change expiration
# -f, --inactive DAYS   Change inactive days
# -L, --lock            Lock account
# -U, --unlock          Unlock account
# -p HASH               Change password (use passwd instead)

# CRITICAL EXAM TRAP: -G without -a REPLACES all supplementary groups
# Safe: add to docker group without losing other groups
sudo usermod -aG docker jsmith

# Dangerous: removes ALL existing supplementary groups
sudo usermod -G docker jsmith    # DO NOT DO THIS accidentally
```

---

## Section 4 — Group Management Commands

### 4.1 Group Lifecycle

```bash
# Create group with auto-assigned GID
sudo groupadd webteam

# Create group with specific GID
sudo groupadd -g 2000 webteam

# Create a system group
sudo groupadd -r webserver

# Rename a group
sudo groupmod -n webdevelopers webteam

# Change group GID
sudo groupmod -g 2001 webteam

# Delete a group
# WARNING: cannot delete a group that is a user's primary group
sudo groupdel webteam

# Manage group membership with gpasswd
sudo gpasswd -a jsmith webteam          # Add user
sudo gpasswd -d jsmith webteam          # Remove user
sudo gpasswd -A jsmith webteam          # Make jsmith group admin
sudo gpasswd -M jsmith,awilson webteam  # Set complete member list

# Temporary group switch in a session
newgrp webteam    # Opens a new shell with webteam as primary group
```

### 4.2 Identifying Group Membership

```bash
# Show all groups for the current user
groups

# Show all groups for a specific user
groups jsmith
id jsmith

# Show detailed ID info
id -u jsmith        # UID only
id -g jsmith        # Primary GID only
id -G jsmith        # All GIDs (numbers)
id -Gn jsmith       # All group names

# List all members of a group
getent group developers
grep "^developers:" /etc/group

# Find all users in the wheel group
getent group wheel
```

---

## Section 5 — The sudo System

### 5.1 How sudo Works

When you run `sudo command`:

1. sudo reads `/etc/sudoers` (and files in `/etc/sudoers.d/`)
2. sudo checks whether the current user is listed and whether the requested command is permitted
3. sudo prompts for the user's own password (not root's password)
4. sudo checks the timestamp cache — if the user authenticated within the `timestamp_timeout` window (default 15 minutes), no password is required
5. sudo logs the command to syslog (typically `/var/log/auth.log` or `/var/log/secure`)
6. sudo executes the command with the requested privileges

### 5.2 Sudoers File Deep Dive

```bash
# Defaults section — controls sudo behavior
Defaults    env_reset              # Reset environment when running sudo
Defaults    mail_badpass           # Email root on bad sudo passwords
Defaults    secure_path="..."     # Safe PATH for sudo commands
Defaults    timestamp_timeout=15  # Cache credentials for 15 minutes
Defaults    logfile=/var/log/sudo.log  # Log to custom file
Defaults    log_output             # Log all output (requires log_dir)

# Aliases for cleaner policy
User_Alias   DBADMINS  = alice, bob
User_Alias   NETADMINS = carol, dave
Host_Alias   DBSERVERS = db01, db02, 192.168.1.0/24
Cmnd_Alias   DBCMDS    = /usr/bin/psql, /bin/systemctl restart postgresql
Cmnd_Alias   NETCMDS   = /sbin/ip, /sbin/ifconfig, /usr/sbin/tcpdump

# Rules
DBADMINS   DBSERVERS=(ALL)  DBCMDS
NETADMINS  ALL=(ALL)        NOPASSWD: NETCMDS

# The #includedir directive (note: # is NOT a comment here)
#includedir /etc/sudoers.d
```

### 5.3 sudo Log Analysis

```bash
# View sudo log on RHEL/CentOS
sudo tail -f /var/log/secure | grep sudo

# View sudo log on Debian/Ubuntu
sudo tail -f /var/log/auth.log | grep sudo

# Using journald (modern systems)
sudo journalctl -u sudo
sudo journalctl | grep sudo | tail -20
```

---

## Section 6 — PAM In Depth

### 6.1 PAM Module Types Expanded

The four PAM management groups work in stacks. For a login attempt, the system processes the `auth` stack (verify identity), then the `account` stack (check account validity), then the `session` stack (set up the session). For password changes, the `password` stack is used.

Each group has its own stack of modules. Every module in the stack is evaluated according to its control flag.

### 6.2 Control Flags Explained

The control flag behavior can be summarized as:

- **required**: Failure is noted internally, but evaluation continues. The user is told about failure only at the end. This prevents attackers from knowing which specific check failed.
- **requisite**: Failure stops evaluation immediately and reports failure. Use this for checks that are so fundamental there is no point continuing.
- **sufficient**: Success here (with no prior required failures) is enough to grant access. Skip remaining modules.
- **optional**: Module result is used only if no other module in this stack provides a definitive result.

Modern PAM also supports a complex bracket notation like `[success=2 default=ignore]` which allows jumping over a number of modules on success, but this is beyond the scope of the Linux+ exam.

### 6.3 Common PAM Modules Reference

| Module | Purpose |
|---|---|
| `pam_unix.so` | Standard Unix password authentication |
| `pam_deny.so` | Always denies; used to block a service |
| `pam_permit.so` | Always permits; use with extreme caution |
| `pam_env.so` | Sets environment variables |
| `pam_limits.so` | Enforces `/etc/security/limits.conf` |
| `pam_pwquality.so` | Enforces password complexity |
| `pam_faillock.so` | Account lockout after failures |
| `pam_tally2.so` | Account lockout (older, deprecated) |
| `pam_time.so` | Time-based access control |
| `pam_access.so` | Network-based access control |
| `pam_motd.so` | Display message of the day |
| `pam_lastlog.so` | Show last login information |
| `pam_nologin.so` | Block logins when /etc/nologin exists |
| `pam_securetty.so` | Restrict root login to secure TTYs |
| `pam_wheel.so` | Restrict su to wheel group members |

### 6.4 Account Lockout Configuration

```bash
# pam_faillock configuration (RHEL 8+ / modern systems)
# In /etc/pam.d/system-auth and /etc/pam.d/password-auth

# auth section — add before pam_unix:
auth    required    pam_faillock.so preauth silent audit deny=5 unlock_time=900

# auth section — add after pam_unix:
auth    [default=die] pam_faillock.so authfail audit deny=5

# account section — add near top:
account required    pam_faillock.so

# Check failed attempt count
sudo faillock --user jsmith

# Reset a locked account
sudo faillock --user jsmith --reset

# Configuration file alternative: /etc/security/faillock.conf
# deny = 5
# unlock_time = 900
# audit
# silent
```

---

## Section 7 — Account Security Best Practices

### 7.1 Service Account Hardening

Service accounts — those created for applications like Apache, PostgreSQL, or Nginx — should be hardened:

```bash
# Create a service account with no home directory and no shell
sudo useradd -r -s /sbin/nologin -d /var/lib/myapp myapp

# Lock the account as an additional measure
sudo passwd -l myapp

# Verify the account cannot be used for login
grep myapp /etc/passwd
# myapp:x:998:998::/var/lib/myapp:/sbin/nologin
```

### 7.2 Auditing User Accounts

```bash
# Find accounts with UID 0 (should only be root)
awk -F: '($3 == 0) {print}' /etc/passwd

# Find accounts with empty passwords (security risk)
sudo awk -F: '($2 == "") {print $1}' /etc/shadow

# Find accounts with no expiration (review periodically)
sudo chage -l username    # Review each account

# List all accounts sorted by UID
sort -t: -k3 -n /etc/passwd

# Find recently created accounts
sudo last | head -20
sudo lastlog | grep -v "Never logged"
```

### 7.3 The /etc/nologin File

When `/etc/nologin` exists, all non-root login attempts are blocked. The file's contents are displayed to the user as an error message. This is useful during system maintenance.

```bash
# Block all logins (maintenance mode)
echo "System maintenance in progress. Try again in 30 minutes." | sudo tee /etc/nologin

# Restore normal login
sudo rm /etc/nologin
```

---

## Section 8 — Key Terms Glossary

| Term | Definition |
|---|---|
| UID | User ID — numeric kernel identifier for a user |
| GID | Group ID — numeric kernel identifier for a group |
| Primary Group | The group assigned at creation; appears in /etc/passwd |
| Supplementary Group | Additional groups a user belongs to |
| GECOS | General Electric Comprehensive OS — legacy field for user info |
| PAM | Pluggable Authentication Modules — authentication framework |
| NSS | Name Service Switch — configures identity lookup order |
| sudo | Superuser do — execute commands with elevated privileges |
| visudo | Safe sudoers editor with syntax validation |
| chage | Change age — manage password aging policy |
| epoch | January 1, 1970 — the Unix time reference point |
| shadow password | Password hash stored in /etc/shadow, not /etc/passwd |
| wheel group | Conventional sudo-access group on RHEL systems |

---

## Section 9 — Review Questions

Answer these questions before taking the quiz:

1. What are the seven fields of `/etc/passwd` in order?

2. A user's hash in `/etc/shadow` begins with `!`. What does this mean?

3. What is the difference between `usermod -G docker jsmith` and `usermod -aG docker jsmith`?

4. Why must you always use `visudo` instead of editing `/etc/sudoers` directly?

5. What does `chage -d 0 jsmith` accomplish?

6. In a PAM configuration file, what is the difference between a `required` and a `requisite` control flag?

7. Which file controls default UID and GID ranges for new user accounts?

8. What command would you use to find all files owned by a user who has been deleted?

9. What is the purpose of `/etc/skel`?

10. On a RHEL system, what group membership grants a user full sudo access?

---

## Additional Resources

- `man 5 passwd` — /etc/passwd format documentation
- `man 5 shadow` — /etc/shadow format documentation
- `man 8 useradd` — useradd command reference
- `man 8 usermod` — usermod command reference
- `man 5 sudoers` — sudoers file syntax reference
- `man 8 pam` — PAM overview
- Linux+ Study Guide (CompTIA XK0-005) — Chapter covering Domain 2: Security

---

## 9. Supplemental Resources

**1. [Linux PAM Documentation — The Linux-PAM System Administrator's Guide](https://www.linux-pam.org/Linux-PAM-html/Linux-PAM_SAG.html)**
The official Linux-PAM system administrator's guide. Covers the configuration file format, all four PAM management groups (auth, account, password, session), control flag semantics, and the full module reference. Essential for understanding how PAM stacks are evaluated and how to configure account lockout with `pam_faillock`.

**2. [man7.org — sudoers(5)](https://man7.org/linux/man-pages/man5/sudoers.5.html)**
The complete sudoers manual page online. Covers the full syntax including User_Alias, Host_Alias, Cmnd_Alias, Runas_Alias, the `NOPASSWD` tag, `Defaults` settings, and the `#includedir` directive. This is the definitive reference for writing complex sudo policies for the Linux+ exam.

**3. [Ubuntu Server Guide — User Management](https://ubuntu.com/server/docs/user-management)**
Canonical's official Ubuntu Server documentation for user management. Covers `adduser` vs `useradd`, group management, password aging with `chage`, and the `/etc/adduser.conf` configuration file. Includes Ubuntu-specific conventions that differ from RHEL, which is important context for understanding cross-distribution portability.
