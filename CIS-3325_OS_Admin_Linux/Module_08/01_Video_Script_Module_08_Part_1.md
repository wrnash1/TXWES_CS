# Video Script: Module 08 — File System Permissions and Ownership (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome and Module Overview

Welcome to Module 8. I'm Professor Nash, and today we're covering file system permissions and ownership — the mechanism that controls who can read, write, and execute every file and directory on a Linux system.

This is one of the most heavily tested topics on the CompTIA Linux+ exam. You will encounter permissions questions in multiple contexts: setting up web servers, securing configuration files, troubleshooting access denied errors, and hardening systems.

By the end of both parts, you will be able to read permission strings fluently, change permissions with both symbolic and octal notation, transfer file ownership, set the umask, configure special permission bits (SUID, SGID, and sticky bit), and use Access Control Lists for fine-grained control beyond the traditional model.

---

### Slide 2 — The Traditional Unix Permission Model

Every file and directory in Linux has three permission sets associated with three identity classes:

- **Owner (u)** — the user who owns the file; originally the creator
- **Group (g)** — the group associated with the file
- **Others (o)** — everyone else who is not the owner and not in the group

Each class has three permission bits:

- **Read (r)** — value 4
- **Write (w)** — value 2
- **Execute (x)** — value 1

That gives us nine permission bits total, displayed in the long listing format of `ls -l`.

```bash
# Long listing showing permissions
ls -l /etc/passwd
# -rw-r--r-- 1 root root 2512 Jan 15 2024 /etc/passwd
# [type][owner][group][others]

# Permission string breakdown:
# -  = regular file (d=directory, l=link, b=block, c=char, p=pipe, s=socket)
# rw- = owner can read and write, not execute
# r-- = group can read only
# r-- = others can read only
```

The kernel checks permissions in order: owner first, then group, then others. If you are the file's owner, the owner permissions apply — even if the group permissions would be more permissive. The kernel does not combine permission sets.

---

### Slide 3 — Permission Meanings for Files vs. Directories

This is a critical distinction that trips up students on the exam. The same permission bit means different things for files versus directories.

For **files**:

- `r` — can read the file contents (`cat`, `less`, `head`)
- `w` — can modify the file contents (`vim`, `echo >> file`)
- `x` — can execute the file as a program

For **directories**:

- `r` — can list the directory contents (`ls`)
- `w` — can create, delete, or rename files within the directory
- `x` — can enter the directory and access its contents (`cd`, use pathnames inside it)

```bash
# Demonstrate directory permissions
ls -ld /tmp
# drwxrwxrwt 1 root root 4096 Jan 15 2024 /tmp
# d = directory; rwx for owner; rwx for group; rwt for others (t = sticky bit)

# Without execute on a directory, you cannot cd into it
ls -ld /root
# drwx------ 8 root root 4096 Jan 15 2024 /root
# Only root can enter /root

# Without read on a directory, you cannot ls it
# Without write on a directory, you cannot create/delete files in it
```

The key insight: you need `x` on a directory to traverse it. Even if a file inside has `r--r--r--` for others, if the directory containing it does not have `x` for others, nobody can reach the file. This is how you create private directories even with publicly readable files inside.

---

### Slide 4 — Reading Permission Strings

Let's practice reading permission strings rapidly — you need this skill to answer exam questions in seconds.

```bash
# Example: web server configuration file
-rw-r----- 1 root apache 1024 Jan 15 2024 /etc/httpd/httpd.conf
# Owner (root): rw- = read and write
# Group (apache): r-- = read only
# Others: --- = no access

# Example: executable script
-rwxr-xr-x 1 deploy staff 2048 Jan 15 2024 /usr/local/bin/deploy.sh
# Owner (deploy): rwx = read, write, execute
# Group (staff): r-x = read and execute
# Others: r-x = read and execute

# Example: directory with correct permissions
drwxr-xr-x 3 www-data www-data 4096 Jan 15 2024 /var/www/html
# Owner (www-data): rwx = full access
# Group (www-data): r-x = list and enter, no write
# Others: r-x = list and enter, no write

# List all files showing permissions
ls -la /var/www/html

# Show permissions numerically
stat /etc/passwd
stat --format="%a %n" /etc/passwd    # Shows octal mode and filename
```

---

### Slide 5 — Octal Notation

While symbolic notation uses letters, octal notation uses a three-digit (or four-digit) number. Each digit is the sum of the permission bits for that class.

```
r = 4, w = 2, x = 1

Owner  Group  Others
 rwx    r-x    r--
4+2+1  4+0+1  4+0+0
  7      5      4
```

Therefore `rwxr-xr--` = **754** in octal.

Common octal combinations to memorize:

| Octal | Symbolic | Typical Use |
|---|---|---|
| 777 | rwxrwxrwx | Never use — insecure |
| 755 | rwxr-xr-x | Executables, public directories |
| 644 | rw-r--r-- | Regular files, config files |
| 600 | rw------- | Private files (SSH keys, secrets) |
| 700 | rwx------ | Private executables |
| 664 | rw-rw-r-- | Shared project files |
| 640 | rw-r----- | Group-readable configs |

```bash
# Calculate octal for any permission string:
# -rwxrw-r--
# rwx = 4+2+1 = 7
# rw- = 4+2+0 = 6
# r-- = 4+0+0 = 4
# Result: 764

# Verify with stat
stat --format="%a" /etc/passwd
# Output: 644
```

---

### Slide 6 — chmod — Changing Permissions

`chmod` (change mode) sets file permissions. It accepts both symbolic and octal notation.

### Octal Mode

```bash
# Set exact permissions with octal
chmod 755 /usr/local/bin/myscript.sh    # rwxr-xr-x
chmod 644 /etc/myapp/config.conf        # rw-r--r--
chmod 600 ~/.ssh/id_rsa                 # rw------- (required for SSH)
chmod 700 ~/.ssh                        # rwx------ (SSH dir must be 700)

# Apply recursively to a directory
chmod -R 755 /var/www/html

# Recursively change only files (not directories)
find /var/www/html -type f -exec chmod 644 {} \;

# Recursively change only directories
find /var/www/html -type d -exec chmod 755 {} \;
```

### Symbolic Mode

Symbolic mode uses operators and letters: `u` (user/owner), `g` (group), `o` (others), `a` (all). Operators are `+` (add), `-` (remove), `=` (set exactly).

```bash
# Add execute for owner only
chmod u+x script.sh

# Remove write for group and others
chmod go-w sensitive.conf

# Set exactly (replace, don't add/remove)
chmod u=rw,g=r,o= private.txt    # rw-r-----

# Add read for all classes
chmod a+r public.txt

# Remove execute for others
chmod o-x program

# Multiple operations at once
chmod u+x,g-w,o-r file.txt
```

---

### Slide 7 — chown and chgrp — Changing Ownership

Every file has an owner (user) and an owning group. `chown` changes ownership; `chgrp` changes the group.

```bash
# Change file owner to alice
sudo chown alice file.txt

# Change file owner AND group simultaneously
sudo chown alice:developers file.txt
sudo chown alice.developers file.txt    # Older dot syntax also works

# Change group only using chown
sudo chown :developers file.txt

# Change group using chgrp
sudo chgrp developers file.txt

# Recursive ownership change
sudo chown -R www-data:www-data /var/www/html

# Change owner but preserve symlinks (don't follow them)
sudo chown -h alice symlink.txt

# Verify ownership
ls -l file.txt
stat file.txt
```

Only root can change the owner of a file. Regular users can only change the group — and only to a group they belong to. This prevents privilege escalation through file ownership manipulation.

---

### Slide 8 — The umask

When a new file or directory is created, it does not start with full permissions. The `umask` (user file creation mask) defines which permissions are subtracted from the maximum default.

- Maximum default for **files**: `666` (no execute by default — a security baseline)
- Maximum default for **directories**: `777`

The umask subtracts from these maximums:

```
Default file permissions:  666
Minus umask:              -022
Resulting permissions:     644
```

```bash
# View current umask (octal)
umask
# 0022

# View umask in symbolic form
umask -S
# u=rwx,g=rx,o=rx

# Set umask for the current session
umask 027     # New files: 640 (rw-r-----); new dirs: 750 (rwxr-x---)
umask 077     # New files: 600 (rw-------); new dirs: 700 (rwx------)

# Test the umask effect
touch testfile
mkdir testdir
ls -ld testfile testdir

# Set a permanent umask in shell profile
echo "umask 027" >> ~/.bashrc
```

Common umask values:

| umask | File result | Directory result | Use case |
|---|---|---|---|
| 022 | 644 | 755 | Standard default |
| 027 | 640 | 750 | Security-conscious default |
| 077 | 600 | 700 | Highly private (root's home) |
| 002 | 664 | 775 | Collaborative team environment |

---

### Slide 9 — Special Permission Bits Overview

Beyond the standard nine permission bits, Linux has three special bits that provide additional behavior. These are represented as a fourth octal digit.

| Bit | Name | Octal | Applies To |
|---|---|---|---|
| SUID | Set User ID | 4000 | Executable files |
| SGID | Set Group ID | 2000 | Files and directories |
| Sticky | Sticky Bit | 1000 | Directories |

These appear in the execute position of the permission string:

```bash
# SUID on a file — 's' in owner execute position
-rwsr-xr-x  root root  /usr/bin/passwd

# SGID on a file — 's' in group execute position
-rwxr-sr-x  root mail  /usr/sbin/sendmail

# Sticky bit on directory — 't' in others execute position
drwxrwxrwt  root root  /tmp

# Capital S or T means the underlying execute bit is NOT set
-rwSr--r--  # SUID set but execute bit NOT set (unusual/error state)
drwxrwx--T  # Sticky set but others execute NOT set
```

We will cover each special bit in detail in Part 2, along with Access Control Lists. See you there.

---

### Slide 10 — Module 08 Part 1 Summary

In Part 1 we covered the traditional permission model:

- Three identity classes: owner, group, others
- Three permission bits per class: read, write, execute
- Files vs. directories: `x` means execute for files but traverse for directories
- Reading permission strings and converting between symbolic and octal notation
- `chmod` with both octal and symbolic syntax, including recursive operations
- `chown` and `chgrp` for ownership management
- The `umask` and how it subtracts from default permissions
- Overview of the three special permission bits

In Part 2 we will deep-dive into SUID, SGID, and the sticky bit, then move into ACLs with `setfacl` and `getfacl` — the modern way to handle permissions that the traditional model cannot express.
