# Video Script: Module 03 - File Permissions and Ownership (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - Special Permissions and Exam Application

---

### Opening

Welcome back. In Part 1 we covered the core permission system, octal notation, chmod, chown,
and umask. In Part 2 we tackle the special permission bits that trip up almost every student
on the Linux+ exam, and then we work through practical scenarios that mirror real exam questions.

---

### Section 1: SUID - Set User ID

SUID is one of the most important special permission bits in Linux. When SUID is set on an
executable file, that program runs with the file owner's privileges, not the privileges of
the user who launched it.

Why does this exist? Consider the passwd command. Every user needs to be able to change their
own password. Changing a password means writing to /etc/shadow, which is owned by root and
readable only by root. Without SUID, only root could run passwd. With SUID set on /usr/bin/passwd
(which is owned by root), any user who runs passwd gets temporary root privileges for the
duration of that specific program's execution.

[SHOW TERMINAL]

```bash
ls -l /usr/bin/passwd
```

You should see: -rwsr-xr-x 1 root root

The s in the owner execute position (where x would normally be) indicates SUID is set. If the
owner execute bit were off and SUID were still set, you would see a capital S there instead.
Lowercase s means execute is also set. Uppercase S means execute is not set.

```bash
find / -perm /4000 2>/dev/null
```

This finds all SUID files on the system. On a freshly installed Ubuntu server you should see a
modest list of well-known system utilities. A large or unexpected list is a red flag for a
security audit.

To set SUID in octal notation, use a leading 4:

```bash
chmod 4755 myprog
```

4 is the SUID bit. 755 is the normal permission. So 4755 = SUID + owner:rwx + group:r-x + others:r-x.

To remove SUID:

```bash
chmod 0755 myprog
```

---

### Section 2: SGID - Set Group ID

SGID behaves differently depending on whether it is on a file or a directory.

On a file: the process runs with the group privileges of the file's group owner (similar to
how SUID works for users). This is less common but tested on the exam.

On a directory: any file created inside that directory automatically inherits the directory's
group rather than the creating user's primary group. This is extremely useful for shared project
directories.

[SHOW TERMINAL]

```bash
sudo mkdir /opt/project
sudo chown root:developers /opt/project
sudo chmod 2775 /opt/project
ls -la /opt/
```

The 2 in 2775 sets SGID. The 775 gives owner and group full control with read+execute for others.

Now when any member of the developers group creates a file in /opt/project, that file gets the
developers group automatically, even if the user's primary group is something else.

SGID on a directory is shown as s in the group execute position:

```
drwxrwsr-x 2 root developers 4096 Jan 15 10:30 project
```

To find all SGID files:

```bash
find / -perm /2000 2>/dev/null
```

---

### Section 3: The Sticky Bit

The sticky bit on a directory prevents users from deleting or renaming files they do not own,
even if they have write permission on the directory itself.

The classic example is /tmp. /tmp is world-writable (anyone can create files there), but users
should not be able to delete each other's temporary files.

[SHOW TERMINAL]

```bash
ls -la / | grep tmp
```

You should see: drwxrwxrwt 13 root root ...

The t in the others execute position indicates the sticky bit is set. Lowercase t means the
others execute bit is also set. Uppercase T means execute is not set for others.

To set the sticky bit in octal notation, use a leading 1:

```bash
chmod 1777 /tmp
```

1 is the sticky bit, 777 is full access for everyone.

For a shared directory where you want both SGID (group inheritance) and sticky bit (delete
protection), combine them:

```bash
chmod 3775 /opt/shared
```

3 = SGID (2) + sticky bit (1). 775 = normal permissions.

---

### Section 4: Special Permission Summary Table

| Bit | Octal | Effect on File | Effect on Directory |
|-----|-------|---------------|---------------------|
| SUID | 4 | Process runs as file owner | No standard effect |
| SGID | 2 | Process runs as file group | New files inherit directory group |
| Sticky | 1 | Rarely used on files | Only owner/root can delete files |
| ls symbol for set+exec | s (lowercase) | Owner-exec or group-exec set | Same |
| ls symbol for set, no exec | S (uppercase) | No execute, bit still set | Same |
| Sticky symbol for set+exec | t (lowercase) | Others-exec set | Most common case |
| Sticky symbol for set, no exec | T (uppercase) | No others-execute | Unusual |

---

### Section 5: Access Control Lists (ACLs) - Introduction

Standard Linux permissions are limited: you can only define permissions for one user (the owner),
one group, and everyone else. Access Control Lists (ACLs) extend this to allow any number of
users and groups to have specific permissions on a single file.

[SHOW TERMINAL]

```bash
getfacl /etc/hosts
```

A file without ACLs shows just the standard permissions. A file with ACLs shows additional
entries.

```bash
setfacl -m u:alice:rw /etc/hosts
getfacl /etc/hosts
```

This adds read+write permission for alice specifically, without changing the file's standard
owner, group, or others permissions.

When a file has an ACL, ls -l shows a + at the end of the permission string:

```
-rw-r--r--+ 1 root root 215 Jan 15 hosts
```

The exam tests basic ACL awareness. Know that getfacl reads ACLs and setfacl sets them.

---

### Section 6: Practical Exam Scenarios

Let me walk through the types of permission scenarios you will see on the exam.

[SHOW TERMINAL]

Scenario 1: A web server needs to serve files from /var/www/html. The Apache process runs as
the www-data user and group. What permissions should the web files have?

```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

Owner (www-data): rwx - can read, write, and traverse
Group (www-data): r-x - can read and traverse
Others (everyone): r-x - world-readable for web serving

Scenario 2: A configuration file contains database passwords and should be readable only by
the application owner.

```bash
chmod 600 /etc/myapp/database.conf
```

Only the owner can read or write it. Group and others have no access.

Scenario 3: A shared development directory where all developers need to write and any files
created should belong to the team group.

```bash
sudo chown root:devteam /opt/devshared
sudo chmod 2775 /opt/devshared
```

SGID (2) ensures group inheritance. 775 gives owner and group full access.

Scenario 4: /tmp must be world-writable but users should not delete each other's files.

```bash
sudo chmod 1777 /tmp
```

Sticky bit (1) + 777 = world-writable with deletion protection.

---

### Section 7: Exam Tips

The s versus S distinction is tested. Lowercase s means the execute bit AND the special bit are
both set. Uppercase S means the special bit is set but execute is NOT set. An uppercase SUID S
is potentially dangerous - the program is supposed to run as root but is not executable.

The exam always tests umask direction: umask subtracts from the default, not from 777. Files
default to 666, not 777. Files never get execute bits from umask because 666 has no execute bits
to start with.

SUID on directories is not standard and has no defined behavior in the Linux+ objectives. Focus
on SUID on files.

find -perm /4000 finds SUID files. find -perm /2000 finds SGID files. find -perm /1000 finds
sticky bit directories. The /N syntax means "files that have any of these bits set."

The passwd command is the canonical SUID example. Know it.

---

### Lab Preview

This week's lab has you creating files and directories with specific permissions using both
octal and symbolic chmod notation, verifying with ls -l, using chown to assign ownership, setting
a umask, and finding SUID files on the system. The lab requires you to predict what ls -l will
show before you run it. Practicing that calculation is the single most effective way to prepare
for exam permission questions.

---

### Summary

Module 03 covers the complete Linux permissions system: the three permission layers, octal and
symbolic notation, chmod, chown, umask, and the special bits SUID, SGID, and sticky. Every
one of these concepts appears on the Linux+ exam.

Module 04 covers user and group management - the tools that create the users and groups that
permissions are applied to.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
