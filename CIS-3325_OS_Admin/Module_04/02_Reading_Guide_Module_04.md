# Reading Guide: Module 04 - User and Group Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 04. User and group management underpins all access control in Linux. Every
file is owned by a user and a group. Every process runs as a user. Every permission decision
references the user's identity and group membership. This reading guide provides the complete
reference for the quiz, lab, and Linux+ exam.

---

### 1. High-Yield Glossary

**UID (User ID):** A numeric identifier assigned to each user account. Root is always UID 0.
System accounts are UIDs 1-999. Regular users are UIDs 1000+. Used internally by the kernel
to identify file ownership and process identity.

**GID (Group ID):** A numeric identifier for a group. Every user has a primary GID (stored in
/etc/passwd) and may belong to multiple supplementary groups (listed in /etc/group).

**Primary Group:** The group assigned to a user in /etc/passwd field 4. New files created by
the user get this group as their default group owner (unless SGID is set on the directory).

**Supplementary Groups:** Additional groups a user belongs to, listed in /etc/group. These
extend the user's access rights beyond their primary group.

**/etc/passwd:** World-readable file with one record per user. Seven colon-separated fields:
username:password_placeholder:UID:GID:GECOS:home_dir:login_shell.

**/etc/shadow:** Root-readable only. Contains hashed passwords and password aging policy.
Fields: username:hash:last_changed:min:max:warn:inactive:expire:reserved.

**/etc/group:** Readable by all. Group definitions: groupname:password:GID:member_list.

**/etc/gshadow:** Root-readable. Group passwords and administrators for the shadow group system.

**/etc/skel:** Template directory. Contents are copied to a new user's home directory when
useradd -m creates it. Add files here to standardize new user environments.

**useradd:** Low-level user creation binary available on all Linux distributions. Requires
explicit flags for most settings.

**adduser:** High-level wrapper (Debian/Ubuntu) that is interactive and creates home directories
by default. The exam tests useradd flags, not adduser.

**usermod:** Modifies existing user accounts. Most critical flag: -aG for appending group
membership without replacing existing memberships.

**userdel:** Removes user accounts. userdel -r also removes the home directory and mail spool.

**passwd:** Sets or changes passwords. Root can change any user's password without knowing the
current one.

**chage:** Manages password aging policy: expiration dates, maximum age, minimum age, and
warning periods.

**sudo:** Allows permitted users to run commands as another user (typically root) according to
/etc/sudoers policy.

**visudo:** The only safe way to edit /etc/sudoers. Validates syntax before saving.

**su:** Switches to another user account. su - username loads a full login environment.

---

### 2. Identity File Reference

#### /etc/passwd Field Layout

```
labadmin:x:1000:1000:Lab Admin,,,:/home/labadmin:/bin/bash
   |      |  |    |      |              |              |
   1      2  3    4      5              6              7
```

| Field | Name | Content |
|-------|------|---------|
| 1 | Username | Login name |
| 2 | Password | x (hash in /etc/shadow) |
| 3 | UID | Numeric user ID |
| 4 | GID | Primary group ID |
| 5 | GECOS | Comment/full name |
| 6 | Home dir | /home/username |
| 7 | Shell | /bin/bash or /usr/sbin/nologin |

#### /etc/shadow Field Layout

```
alice:$6$xyz...:19720:0:90:14:7:20000:
  |       |       |   | |  |  |   |
  1       2       3   4 5  6  7   8
```

| Field | Name | Meaning |
|-------|------|---------|
| 1 | Username | Matches /etc/passwd |
| 2 | Hash | Password hash ($6$=SHA-512) |
| 3 | Last changed | Days since epoch |
| 4 | Min days | Min days before change allowed |
| 5 | Max days | Days before forced change |
| 6 | Warn days | Days warning before expiry |
| 7 | Inactive | Days after expiry before lock |
| 8 | Expire | Account expiration date |

---

### 3. useradd Flag Reference

| Flag | Meaning | Example |
|------|---------|---------|
| -m | Create home directory | useradd -m alice |
| -d path | Set home directory path | useradd -d /data/alice alice |
| -s shell | Set login shell | useradd -s /bin/bash alice |
| -c comment | Set GECOS field | useradd -c "Alice Smith" alice |
| -G groups | Set supplementary groups | useradd -G sudo,docker alice |
| -e date | Set account expiry | useradd -e 2026-12-31 alice |
| -r | Create system account | useradd -r -s /usr/sbin/nologin svc |
| -u uid | Specify UID | useradd -u 1500 alice |
| -g gid | Set primary group | useradd -g staff alice |

---

### 4. usermod Flag Reference

| Flag | Meaning | Caution |
|------|---------|---------|
| -aG group | Append to supplementary group | Use -a with -G always |
| -G group | Set supplementary groups | Replaces all existing supplementary groups |
| -L | Lock account | Prefixes hash with ! |
| -U | Unlock account | Removes ! prefix |
| -s shell | Change login shell | |
| -d path | Change home directory | Does not move files |
| -m | Move home directory | Use with -d |
| -e date | Change account expiry | |
| -l newname | Change username | Does not rename home dir |

---

### 5. chage Password Aging Reference

| Flag | Meaning |
|------|---------|
| chage -l username | List aging info |
| chage -M 90 username | Max password age 90 days |
| chage -m 7 username | Min password age 7 days |
| chage -W 14 username | Warn 14 days before expiry |
| chage -E 2026-12-31 username | Account expires on date |
| chage -d 0 username | Force password change at next login |
| chage -I 30 username | Lock 30 days after password expires |

---

### 6. sudoers File Syntax Reference

The /etc/sudoers file uses the format:

```
who    where=(as_whom) what
```

| Entry | Meaning |
|-------|---------|
| root ALL=(ALL:ALL) ALL | Root can do everything |
| %sudo ALL=(ALL:ALL) ALL | sudo group members can do everything |
| %wheel ALL=(ALL:ALL) ALL | wheel group members can do everything (RHEL) |
| alice ALL=(root) /usr/bin/systemctl | alice can run systemctl as root only |
| alice ALL=(ALL) NOPASSWD: ALL | alice needs no password (use with caution) |
| Defaults logfile=/var/log/sudo.log | Log all sudo activity |
| Defaults !lecture | Disable sudo lecture message |

Include files from /etc/sudoers.d/ directory:
```
#includedir /etc/sudoers.d
```

---

### 7. Shell Types for Service Accounts

| Shell | Effect | Use Case |
|-------|--------|---------|
| /bin/bash | Full interactive shell | Regular users |
| /bin/sh | Minimal POSIX shell | Scripting |
| /usr/sbin/nologin | Prints "account disabled" and exits | Service accounts |
| /bin/false | Exits with code 1, no message | Service accounts |
| /bin/sync | Sync disks and exit | Special legacy accounts |

---

### 8. UID Range Standards

| Range | Purpose | Example |
|-------|---------|---------|
| 0 | Root - never share | root |
| 1-99 | Core system accounts | daemon, bin, sys |
| 100-999 | System/service accounts | www-data, mysql, sshd |
| 1000+ | Regular interactive users | labadmin, alice |

Note: On older RHEL systems, system accounts were UIDs 1-499 and regular users started at 500.
Modern standards use the 1000+ threshold.

---

### 9. Privilege Escalation Methods Comparison

| Method | Password Required | Who Can Use | Audit Log |
|--------|-----------------|-------------|-----------|
| sudo command | Caller's password | Users in /etc/sudoers | /var/log/auth.log |
| sudo -i | Caller's password | Users in /etc/sudoers | /var/log/auth.log |
| su - root | Root's password | Any user who knows root pw | /var/log/auth.log |
| su - username | Target's password | Any user who knows target pw | /var/log/auth.log |

---

### 10. CompTIA Linux+ Exam Tips

**Exam Tip 1:** The usermod -aG question is the most commonly missed item. The -a flag appends
without replacing. Omitting -a with -G replaces all supplementary groups. Memorize: "aG = add
to Group safely."

**Exam Tip 2:** visudo is the ONLY correct answer for editing /etc/sudoers. Any answer that
suggests nano, vi, or any other direct editor is incorrect for the exam.

**Exam Tip 3:** Ubuntu uses the sudo group for sudo access. RHEL uses the wheel group. Both
are tested. The exam may present a scenario on one platform and test whether you know the
correct group name.

**Exam Tip 4:** Service accounts should have /usr/sbin/nologin or /bin/false as their shell.
This is a security best practice and an exam question pattern.

**Exam Tip 5:** userdel without -r leaves the home directory. userdel -r removes the home
directory and mail spool. "Preserve files" = userdel without -r. "Clean removal" = userdel -r.

**Exam Tip 6:** /etc/skel provides template files copied to new home directories. Adding files
to /etc/skel standardizes all new user environments created afterward.

**Exam Tip 7:** chage -d 0 forces a password change at next login. This is the correct
approach for onboarding new users who need to set their own password.

**Exam Tip 8:** The principle of least privilege says accounts should have only the access
they need. Service accounts should not be in sudo. Interactive admin accounts should not own
application files.

---

### 11. Study Checklist

- [ ] Watch both parts of the Module 04 video lecture
- [ ] Memorize all /etc/passwd field positions and meanings
- [ ] Memorize usermod -aG versus -G behavior
- [ ] Know useradd flags: -m, -s, -c, -G, -e, -r
- [ ] Understand visudo and why direct editing of /etc/sudoers is dangerous
- [ ] Know Ubuntu uses sudo group; RHEL uses wheel group
- [ ] Know chage flags for password aging
- [ ] Know usermod -L and -U for locking/unlocking accounts
- [ ] Complete the Module 04 Lab
- [ ] Complete the Module 04 Quiz
- [ ] Post to the Discussion by Wednesday at 11:59 PM
- [ ] Reply to two classmates by Sunday at 11:59 PM

---

### Required Reading

Read chapters 9 and 10 of The Linux Command Line by William Shotts (linuxcommand.org/tlcl.php)
covering user identity, permissions, and process ownership in the context of Linux security.

---

## 9. Supplemental Resources

**1. Linux man pages — useradd(8), usermod(8), userdel(8), chage(1)**
URL: https://man7.org/linux/man-pages/man8/useradd.8.html
Coverage: Authoritative reference for all user management commands. Pay special attention
to the FLAGS section of useradd for -r, -m, -s, -e, and -G, and to chage for -d, -E, -M,
and -l. These flags are directly tested on CompTIA Linux+.

**2. TLDP — Linux System Administrator's Guide: User Management**
URL: https://tldp.org/LDP/sag/html/users.html
Coverage: Explains /etc/passwd, /etc/shadow, and /etc/group field-by-field. Covers the
history of shadow passwords and why splitting the password hash from the user database
was a critical security improvement.

**3. Red Hat Documentation — Configuring sudo access**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/managing-sudo-access_configuring-basic-system-settings
Coverage: Step-by-step guide to granting sudo access, using visudo safely, writing sudoers
rules with host, user, and command restrictions, and understanding the NOPASSWD directive.

**4. Ubuntu Documentation — sudoers file**
URL: https://help.ubuntu.com/community/Sudoers
Coverage: Ubuntu-specific sudoers documentation covering the sudo group, Defaults entries,
per-command NOPASSWD rules, and the difference between Ubuntu and RHEL sudo group conventions.

**5. Linux man pages — pam_pwquality(8)**
URL: https://man7.org/linux/man-pages/man8/pam_pwquality.8.html
Coverage: Documents all password quality parameters including minlen, dcredit, ucredit,
lcredit, and ocredit. Essential for understanding how to enforce enterprise password
complexity policies using PAM on both Debian and Red Hat family systems.
