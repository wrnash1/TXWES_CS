# Video Script: Module 04 - User and Group Management (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 14 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 04. In Module 03 we learned that every file has an owner and a group. Now
we learn how to create those owners and groups. User and group management is one of the most
fundamental administrative tasks in Linux. Every person who logs in, every service that runs,
every automated process that executes - all of these are represented as users on the system.
Understanding how Linux tracks identity and controls access through user accounts is essential
for both daily administration and the Linux+ exam.

---

### Section 1: Linux Identity Files

Linux stores user identity in a small set of plain text files. Understanding these files is
critical for both administration and exam preparation.

[SHOW TERMINAL]

```bash
cat /etc/passwd | head -5
```

The /etc/passwd file has one record per user with seven colon-separated fields:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
labadmin:x:1000:1000:,,,:/home/labadmin:/bin/bash
```

Let us decode each field:

Field 1 - username: the login name
Field 2 - x: password placeholder (actual hash is in /etc/shadow)
Field 3 - UID: User ID number. Root is always 0. System accounts typically 1-999. Regular users 1000+.
Field 4 - GID: Primary group ID number
Field 5 - GECOS: Comment field, often the user's full name
Field 6 - home directory: where the user lands after login
Field 7 - login shell: the shell program launched at login. /usr/sbin/nologin prevents login.

```bash
sudo cat /etc/shadow | grep labadmin
```

The shadow file is readable only by root. The password field contains a hash string starting
with $6$ (SHA-512) or $y$ (yescrypt on newer Ubuntu systems). The remaining fields control
password aging: minimum days, maximum days, warning period, and account expiration.

```bash
cat /etc/group | grep labadmin
```

The /etc/group file has four fields: groupname:password:GID:members
Members listed here are supplementary group members (users whose primary group is different
but who are also in this group).

---

### Section 2: UID Ranges and Service Accounts

[SHOW TERMINAL]

```bash
cat /etc/passwd | awk -F: '$3 < 1000 {print $1, $3, $7}' | head -15
```

This command shows all system accounts (UID below 1000) and their login shells. Notice most
have /usr/sbin/nologin or /bin/false as their shell. This is intentional: service accounts
like www-data (Apache), mysql, and sshd should never be able to log in interactively. They
exist only to run processes with limited privileges.

UID 0 is root and must never be assigned to any other account.
UIDs 1-999 are reserved for system accounts on modern Linux systems.
UIDs 1000+ are for regular interactive user accounts.

This design means that if the web server process is compromised, the attacker gets the www-data
identity, which has very limited permissions. If the web server ran as root, a compromise would
give the attacker full system control.

---

### Section 3: Creating User Accounts with useradd

[SHOW TERMINAL]

The low-level command for creating users is useradd. It is available on all Linux distributions.

```bash
sudo useradd alice
```

This creates the user alice with no home directory, no password, and /bin/sh as the shell.
Bare useradd is rarely what you want.

```bash
sudo useradd -m -s /bin/bash alice2
ls -la /home/
```

The -m flag creates the home directory at /home/alice2. The -s flag specifies the login shell.
Now alice2 has a proper home directory.

```bash
sudo useradd -m -s /bin/bash -c "Application Service Account" -r appservice
id appservice
```

The -c flag sets the GECOS comment. The -r flag creates a system account (UID below 1000).
This is appropriate for service accounts that run daemons.

```bash
sudo useradd -m -s /bin/bash -e 2025-12-31 -G sudo temporaryadmin
```

The -e flag sets an account expiration date. The -G flag specifies supplementary groups.
This is useful for contract workers or temporary access.

On Ubuntu/Debian, adduser is a friendlier wrapper:

```bash
sudo adduser bob
```

adduser is interactive: it prompts for password, full name, and other information. The lab
uses useradd with explicit flags because that is what the exam tests.

---

### Section 4: Setting and Managing Passwords

[SHOW TERMINAL]

```bash
sudo passwd alice
```

This prompts for a new password for alice. As root using sudo, there is no requirement to
know the current password.

```bash
passwd
```

Without an argument, passwd changes your own password. It requires the current password first.

Password aging controls:

```bash
sudo chage -l alice
```

chage displays or modifies password aging policy for a user.

```bash
sudo chage -M 90 -W 14 alice
```

-M 90 sets the maximum password age to 90 days.
-W 14 sets a 14-day warning before expiration.

```bash
sudo chage -E 2026-06-01 alice
```

-E sets the account expiration date. On this date, alice's account will be locked.

---

### Section 5: Modifying User Accounts with usermod

usermod modifies existing user accounts without creating or deleting.

[SHOW TERMINAL]

```bash
sudo usermod -aG developers alice
id alice
```

-aG means append (a) the user to the supplementary Group (G) named developers. This is the
critically important flag combination. Without the -a:

```bash
sudo usermod -G sudo alice
```

WARNING: This replaces ALL of alice's supplementary groups with only sudo. If alice was in
developers, docker, and backup groups, she is now only in sudo. The -a flag is what makes
usermod -G safe.

Always use -aG when adding a user to a group.

```bash
sudo usermod -L alice
sudo cat /etc/shadow | grep alice
```

-L locks the account. In the shadow file, the password hash is prefixed with ! making it
invalid. Alice cannot log in but the account and files are preserved.

```bash
sudo usermod -U alice
```

-U unlocks the account by removing the ! prefix.

```bash
sudo usermod -s /bin/sh alice
```

Change alice's login shell to /bin/sh.

```bash
sudo usermod -d /home/newdir alice
```

Change alice's home directory. Note this does not move files; it just updates the record.

---

### Section 6: Deleting User Accounts with userdel

[SHOW TERMINAL]

```bash
sudo userdel alice2
ls /home/
```

userdel removes the user account entry from /etc/passwd, /etc/shadow, and /etc/group.
But the home directory /home/alice2 still exists.

```bash
sudo userdel -r alice
ls /home/
```

The -r flag also removes the home directory and mail spool. Use this when you are certain
the files are no longer needed.

Important: Never run userdel -r on an account that might have files scattered across the
filesystem. The -r flag only removes the home directory and mail spool, not files owned by
the user in other locations. Those files will become "orphaned" with a deleted UID.

---

### Section 7: Group Management

[SHOW TERMINAL]

```bash
sudo groupadd developers
sudo groupadd -g 1500 networking
cat /etc/group | grep -E "developers|networking"
```

groupadd creates a new group. The -g flag specifies a specific GID.

```bash
sudo groupmod -n devteam developers
cat /etc/group | grep devteam
```

groupmod -n renames a group. All group membership records are updated automatically.

```bash
sudo groupdel devteam
```

groupdel removes a group. It fails if any user has devteam as their primary group.

---

### Section 8: Viewing Group Membership

[SHOW TERMINAL]

```bash
id labadmin
```

Shows UID, primary GID, and all supplementary groups.

```bash
groups labadmin
```

Shows just the group names for the user.

```bash
cat /etc/group | grep labadmin
```

Shows all groups in the /etc/group file that list labadmin as a member.

After running usermod -aG, the user must log out and log back in for the new group membership
to take effect in their shell session. The id command updates immediately but the effective
groups in an already-running shell do not change until a new login.

---

### Certification Connection

User and group management maps to Linux+ Domain 2.0 (Security) and Domain 1.0 (System Management).
Key tested items:

useradd flags: -m, -s, -c, -G, -e, -r
usermod flags: -aG vs -G distinction (the most commonly missed question)
userdel vs userdel -r
UID ranges and service account design
/etc/passwd field layout
/etc/shadow field layout and password aging

---

### Transition to Part 2

In Part 2 we cover sudo configuration, the /etc/sudoers file, and visudo. We also cover
account security best practices, the principle of least privilege, and practical scenarios.
Take a break and continue.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
