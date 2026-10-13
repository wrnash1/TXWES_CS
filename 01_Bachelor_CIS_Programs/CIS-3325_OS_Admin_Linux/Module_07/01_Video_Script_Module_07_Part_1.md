# Video Script: Module 07 — User and Group Administration (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome and Module Overview

Hello and welcome to Module 7 of CIS-3325, OS Administration Linux. I'm Professor Nash, and today we're covering one of the most foundational skills for any Linux administrator: User and Group Administration.

By the end of this two-part video you will be able to create, modify, and delete user accounts; manage groups; understand the critical configuration files that store identity information; configure sudo access; and explain the basics of Pluggable Authentication Modules.

This topic maps directly to CompTIA Linux+ domain objective 2.4 — Given a scenario, manage users and groups.

Let's begin with why user management matters so much.

---

### Slide 2 — Why User Management Is Central to Linux Security

Linux is a multi-user operating system. Every process, every file, and every resource is owned by an identity. That identity is either a user account or a system account, and it belongs to one or more groups.

When you get user administration wrong, the consequences are serious:

- A misconfigured account can grant someone root-level access they were never supposed to have.
- An orphaned account — one belonging to an employee who left the company — becomes an attack surface.
- Incorrect group membership can let a developer read payroll files or let a junior admin modify system binaries.

On the CompTIA Linux+ exam, user and group administration questions appear in multiple domains. Master this topic and you earn points in security, operations, and troubleshooting sections simultaneously.

---

### Slide 3 — The /etc/passwd File

Every user account on a Linux system is defined in `/etc/passwd`. Despite the name, this file does not store passwords in modern systems — it stores account metadata.

Each line in `/etc/passwd` contains seven colon-delimited fields:

```bash
# View the passwd file
cat /etc/passwd

# Example line:
# jsmith:x:1001:1001:John Smith:/home/jsmith:/bin/bash
# Fields: username:password_placeholder:UID:GID:GECOS:home_dir:shell
```

Let's walk through each field:

- **username** — the login name, case-sensitive, typically lowercase
- **x** — a literal `x` meaning the actual password hash is in `/etc/shadow`
- **UID** — User ID number; root is always 0; system accounts typically 1–999; regular users start at 1000
- **GID** — the primary group ID
- **GECOS** — General Electric Comprehensive Operating System — a legacy field now used for the full name and optional contact info
- **home directory** — absolute path to the user's home folder
- **shell** — the login shell; use `/sbin/nologin` or `/bin/false` for service accounts that should never log in interactively

---

### Slide 4 — The /etc/shadow File

`/etc/shadow` stores the actual password hashes along with password aging policy. Only root can read this file — that is intentional.

```bash
# View shadow (requires root or sudo)
sudo cat /etc/shadow

# Example line:
# jsmith:$6$rounds=5000$salt$hash:19500:0:99999:7:::
# Fields: username:hash:lastchg:min:max:warn:inactive:expire:reserved
```

Field-by-field explanation:

- **hash** — the password hash; `$6$` prefix means SHA-512; `$y$` means yescrypt (modern systems); `!` or `*` means the account is locked
- **lastchg** — days since January 1, 1970 that the password was last changed
- **min** — minimum days before password can be changed again
- **max** — maximum days before password must be changed; 99999 means effectively never
- **warn** — days before expiration to warn the user
- **inactive** — days after expiration before account is disabled
- **expire** — absolute date (in epoch days) when the account expires; empty means never

This aging information is what `chage` reads and writes. We will use `chage` heavily in the lab.

---

### Slide 5 — The /etc/group File

Groups in Linux provide a second layer of access control. Every user has a primary group and can belong to many supplementary groups.

```bash
# View group definitions
cat /etc/group

# Example line:
# developers:x:1050:jsmith,awilson,mthompson
# Fields: groupname:password:GID:member_list
```

Key points:

- **group password** — rarely used; the `x` is a placeholder; `gpasswd` can set group passwords for `newgrp`
- **GID** — Group ID; root group is GID 0
- **member list** — comma-separated list of users for whom this is a supplementary group; users whose primary GID matches do not need to appear here

The companion file `/etc/gshadow` stores group passwords and administrator lists, analogous to how `/etc/shadow` relates to `/etc/passwd`.

---

### Slide 6 — Creating Users with useradd

`useradd` is the standard command for creating user accounts. It writes to `/etc/passwd`, `/etc/shadow`, `/etc/group`, and optionally creates a home directory.

```bash
# Basic user creation (creates home directory by default on RHEL)
sudo useradd jsmith

# Specify full name, shell, home directory, and primary group
sudo useradd -c "John Smith" -s /bin/bash -d /home/jsmith -g staff jsmith

# Create user with a specific UID
sudo useradd -u 1500 jsmith

# Create a system account (no home dir, UID below 1000)
sudo useradd -r apache_worker

# Add user to supplementary groups at creation time
sudo useradd -G developers,qa jsmith

# Verify the account was created
grep jsmith /etc/passwd
id jsmith
```

Important defaults are controlled by `/etc/login.defs` and `/etc/default/useradd`. On Debian/Ubuntu systems, `useradd` does NOT create a home directory by default — you must add the `-m` flag. On RHEL/CentOS/Fedora, `-m` is the default behavior.

```bash
# Force home directory creation (needed on Debian)
sudo useradd -m jsmith

# View useradd defaults
useradd -D
cat /etc/default/useradd
```

---

### Slide 7 — The /etc/skel Directory

When `useradd` creates a home directory, it populates it with copies of files from `/etc/skel`. This is the skeleton directory — a template for new home directories.

```bash
# View skeleton contents
ls -la /etc/skel

# Common files:
# .bash_logout
# .bash_profile
# .bashrc

# Add a custom file for all new users
sudo cp /path/to/company_welcome.txt /etc/skel/README_WELCOME.txt
```

Any file you place in `/etc/skel` will be copied to every new user's home directory at creation time. This is an elegant way to pre-configure shell aliases, editor settings, or required configuration files for new employees.

---

### Slide 8 — Setting Passwords with passwd

A newly created account has no password and is therefore locked. You must set a password before the user can log in.

```bash
# Set or change your own password
passwd

# Root sets another user's password
sudo passwd jsmith

# Lock an account (prepends ! to the hash in shadow)
sudo passwd -l jsmith

# Unlock an account
sudo passwd -u jsmith

# Check password status
sudo passwd -S jsmith
# Output: jsmith PS 2024-01-15 0 99999 7 -1
# PS = password set; LK = locked; NP = no password

# Force a password change at next login
sudo passwd -e jsmith

# Set password expiration policy
sudo chage -M 90 -W 14 -I 30 jsmith
# -M 90 = max 90 days; -W 14 = warn 14 days before; -I 30 = inactive after 30 days

# View password aging details
sudo chage -l jsmith
```

The `chage` command — change age — is the primary tool for managing password aging policy. It reads and writes the shadow file fields we discussed on the previous slide.

---

### Slide 9 — Modifying Users with usermod

After an account exists, `usermod` handles all modifications. Most `usermod` flags mirror their `useradd` equivalents, which makes both commands easy to remember together.

```bash
# Change the user's login name
sudo usermod -l jsmith_new jsmith

# Change the home directory and move contents
sudo usermod -d /home/newdir -m jsmith

# Change the default shell
sudo usermod -s /bin/zsh jsmith

# Add user to a supplementary group (APPEND — critical flag!)
sudo usermod -aG docker jsmith
sudo usermod -aG sudo jsmith

# Lock the account
sudo usermod -L jsmith

# Unlock the account
sudo usermod -U jsmith

# Set account expiration date
sudo usermod -e 2025-12-31 jsmith

# Change the comment/GECOS field
sudo usermod -c "John Smith, Engineering" jsmith
```

The `-aG` flag combination is critically important on the exam. Without `-a` (append), `-G` replaces ALL existing supplementary groups. If you type `sudo usermod -G docker jsmith` without `-a`, John loses every other group he belonged to. Always use `-aG` when adding to groups.

---

### Slide 10 — Deleting Users with userdel

`userdel` removes user accounts. Use it with caution in production.

```bash
# Remove account but leave home directory and mail spool intact
sudo userdel jsmith

# Remove account AND home directory AND mail spool
sudo userdel -r jsmith

# Force removal even if the user is currently logged in
sudo userdel -f jsmith

# Find files owned by a deleted user (orphaned files)
sudo find / -nouser -print 2>/dev/null

# Find files by the old UID after deletion
sudo find / -uid 1001 -print 2>/dev/null
```

Best practice in enterprise environments is to lock an account with `passwd -l` or `usermod -L` rather than immediately deleting it. This preserves file ownership and audit trails. After a retention period — typically 30 to 90 days — you can safely remove the account and archive the home directory.

---

### Slide 11 — Group Management Commands

```bash
# Create a new group
sudo groupadd developers
sudo groupadd -g 1050 developers    # Specify GID

# Modify a group
sudo groupmod -n devteam developers  # Rename group
sudo groupmod -g 1051 developers    # Change GID

# Delete a group
sudo groupdel developers

# Add a user to a group (alternative to usermod -aG)
sudo gpasswd -a jsmith developers

# Remove a user from a group
sudo gpasswd -d jsmith developers

# Set a group administrator
sudo gpasswd -A jsmith developers

# List groups a user belongs to
groups jsmith
id jsmith

# List all members of a group
getent group developers
```

`getent` — get entries — is a powerful command that queries NSS (Name Service Switch) sources. It works whether accounts are stored locally in `/etc/passwd` or in LDAP/Active Directory. Use `getent` instead of `grep /etc/passwd` when your environment may use centralized identity management.

---

### Slide 12 — Module 07 Part 1 Summary

In Part 1 we covered the conceptual and structural foundations of Linux user and group administration:

- `/etc/passwd` — account metadata with seven fields
- `/etc/shadow` — password hashes and aging policy
- `/etc/group` — group definitions and membership
- `useradd` — creating accounts with key flags: `-m`, `-s`, `-G`, `-u`, `-r`
- `passwd` and `chage` — setting passwords and aging policy
- `usermod` — modifying accounts; critical `-aG` append behavior
- `userdel` — removing accounts safely
- `groupadd`, `groupmod`, `groupdel`, `gpasswd` — group lifecycle commands

In Part 2 we will move to privilege escalation with `sudo` and `visudo`, explore PAM basics, and walk through complete lab-style scenarios that mirror what you will encounter on the CompTIA Linux+ exam.

See you in Part 2.
