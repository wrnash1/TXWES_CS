# Video Script: Module 08 — File System Permissions and Ownership (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome Back

Welcome back to Module 8. In Part 1 we covered the traditional permission model, `chmod`, `chown`, `chgrp`, and `umask`. In Part 2 we tackle the three special permission bits — SUID, SGID, and sticky bit — and then move into Access Control Lists, which extend the permission model beyond what the traditional three-class system can express.

These topics appear on every Linux+ exam. Let's get into them.

---

### Slide 2 — SUID: Set User ID

The SUID (Set User ID) bit, when set on an executable file, causes the file to run with the permissions of the file's **owner** rather than the user executing it.

The classic example is `/usr/bin/passwd`. Regular users can change their own passwords, but passwords are stored in `/etc/shadow` which is only writable by root. How does `passwd` write to a file the user cannot directly touch?

```bash
# Check passwd's permissions
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root 68208 Jan 15 2024 /usr/bin/passwd
# The 's' in the owner execute position = SUID

# Other common SUID binaries
ls -l /usr/bin/su
ls -l /usr/bin/sudo
ls -l /usr/bin/ping

# Set SUID on a file
sudo chmod u+s /path/to/executable
# or in octal (4 = SUID digit):
sudo chmod 4755 /path/to/executable

# Remove SUID
sudo chmod u-s /path/to/executable
sudo chmod 0755 /path/to/executable

# Find all SUID files on the system (security audit)
sudo find / -perm -4000 -type f -ls 2>/dev/null
```

SUID is powerful and dangerous. An attacker who can exploit a SUID binary owned by root gains root privileges for the duration of that process. This is why SUID programs are scrutinized carefully and why you should audit your SUID file list regularly.

---

### Slide 3 — SGID: Set Group ID

SGID (Set Group ID) works differently depending on whether it is set on a file or a directory.

**SGID on a file:** The file runs with the permissions of the file's **group** rather than the executing user's group.

```bash
# Find SGID executables
ls -l /usr/bin/write
# -rwxr-sr-x 1 root tty 34K Jan 15 2024 /usr/bin/write
# The 's' in the group execute position = SGID

# Set SGID on a file (2 = SGID digit)
sudo chmod g+s /path/to/executable
sudo chmod 2755 /path/to/executable
```

**SGID on a directory:** This is the more commonly used case. When SGID is set on a directory, all new files and subdirectories created within it inherit the directory's group ownership instead of the creator's primary group. This is extremely useful for shared project directories.

```bash
# SGID on a directory
ls -ld /shared/project
# drwxrwsr-x 2 root developers 4096 Jan 15 2024 /shared/project

# Set SGID on a directory
sudo chmod g+s /shared/project
sudo chmod 2775 /shared/project

# Demonstrate: files created by alice (primary group: staff) will be owned by developers
# Because the directory has SGID set
su - alice
touch /shared/project/newfile.txt
ls -l /shared/project/newfile.txt
# -rw-r--r-- 1 alice developers ...
# Group is 'developers', not 'staff'

# Find all SGID directories
sudo find / -perm -2000 -type d -ls 2>/dev/null
```

---

### Slide 4 — The Sticky Bit

The sticky bit on a **directory** prevents users from deleting or renaming files they do not own, even if they have write permission on the directory.

The prototypical example is `/tmp`:

```bash
# /tmp has sticky bit set
ls -ld /tmp
# drwxrwxrwt 8 root root 4096 Jan 15 2024 /tmp
# The 't' in the others execute position = sticky bit

# Without sticky bit, anyone with write on /tmp could delete anyone's files
# With sticky bit, you can only delete files YOU own

# Set sticky bit on a directory
sudo chmod +t /shared/uploads
sudo chmod 1777 /shared/uploads

# Remove sticky bit
sudo chmod -t /shared/uploads
sudo chmod 0777 /shared/uploads

# Find directories with sticky bit
find / -perm -1000 -type d -ls 2>/dev/null
```

Capital `T` vs lowercase `t`: lowercase `t` means the sticky bit is set AND the execute bit is set for others. Capital `T` means sticky is set but the execute bit is NOT set (unusual; typically an error for directories that need to be accessible).

---

### Slide 5 — Setting Special Bits in Octal

When using four-digit octal, the leftmost digit encodes the special bits:

```
4000 = SUID
2000 = SGID
1000 = Sticky

# Examples:
chmod 4755 /usr/bin/myprog    # SUID + rwxr-xr-x
chmod 2775 /shared/project    # SGID + rwxrwxr-x
chmod 1777 /tmp               # Sticky + rwxrwxrwx
chmod 6755 /usr/bin/special   # SUID + SGID + rwxr-xr-x

# You can also combine them:
# 4+2+1 = 7 = SUID+SGID+Sticky (rare; for specific use cases)
```

```bash
# Verify special bits with stat
stat --format="%a %n" /usr/bin/passwd
# Output: 4755 /usr/bin/passwd

stat --format="%a %n" /tmp
# Output: 1777 /tmp

# Symbolic view showing special bits
ls -l /usr/bin/passwd
ls -l /tmp
```

---

### Slide 6 — Introduction to Access Control Lists

Traditional Unix permissions have a fundamental limitation: you can only specify permissions for one owner, one group, and everyone else. What if you need file `report.pdf` to be readable by Alice (owner), readable by the `finance` group, AND also readable by Bob from the `audit` group — but not by anyone else?

The traditional model cannot express this. That is where ACLs come in.

ACLs (Access Control Lists) let you define permissions for arbitrary users and groups on any file or directory.

```bash
# Check if ACLs are supported/enabled
# A '+' at the end of the permission string indicates an ACL is set
ls -l /path/to/file
# -rw-r--r--+ 1 alice alice 1024 Jan 15 2024 report.pdf
# The '+' means an ACL is present

# Check if the filesystem is mounted with ACL support
grep acl /etc/fstab
mount | grep acl

# On modern ext4 and XFS, ACLs are enabled by default
# For older systems, add 'acl' option in /etc/fstab
```

---

### Slide 7 — getfacl — Reading ACLs

```bash
# View ACL of a file
getfacl report.pdf

# Sample output:
# # file: report.pdf
# # owner: alice
# # group: finance
# user::rw-          <- owner Alice
# user:bob:r--       <- specific user Bob
# group::r--         <- owning group finance
# group:audit:r--    <- specific group audit
# mask::r--          <- effective permissions mask
# other::---         <- all others

# View ACL of a directory
getfacl /shared/project

# View ACL in compact format
getfacl -c report.pdf

# View ACL in a format suitable for backup/restore
getfacl --omit-header report.pdf
```

The **mask** entry is important: it defines the maximum effective permissions for named users and groups (not the owner, not "other"). Even if `user:bob:rwx` is set, if the mask is `r--`, Bob's effective permission is `r--`.

---

### Slide 8 — setfacl — Setting ACLs

```bash
# Grant read permission to user bob
setfacl -m u:bob:r-- report.pdf

# Grant read-write to group audit
setfacl -m g:audit:rw- /shared/reports/

# Set multiple entries at once
setfacl -m u:bob:r--,g:audit:rw- report.pdf

# Set default ACL on a directory (inherited by new files)
setfacl -d -m g:developers:rw- /shared/project/
setfacl -d -m u:alice:rwx /shared/project/

# Remove a specific ACL entry
setfacl -x u:bob report.pdf

# Remove all ACL entries (revert to standard permissions)
setfacl -b report.pdf

# Copy ACL from one file to another
getfacl file1.txt | setfacl --set-file=- file2.txt

# Apply ACL recursively
setfacl -R -m g:developers:rw- /shared/project/

# Verify with getfacl
getfacl report.pdf
```

Default ACLs (set with `-d`) apply to a directory and are inherited by newly created files and subdirectories within it. This is the cleanest way to ensure consistent ACL policy across a shared directory tree.

---

### Slide 9 — Practical Scenarios and Exam Tips

Let's walk through scenarios that combine everything from both parts.

**Scenario 1: Web server directory setup**

```bash
# The web content directory should be:
# - Owned by root, group www-data
# - Directories: 755 (world-readable and traversable)
# - Files: 644 (world-readable, owner-writable)
# - New files created by developers should inherit www-data group

sudo chown -R root:www-data /var/www/html
sudo find /var/www/html -type d -exec chmod 755 {} \;
sudo find /var/www/html -type f -exec chmod 644 {} \;
sudo chmod g+s /var/www/html     # SGID so new files get www-data group
```

**Scenario 2: Shared development directory**

```bash
# Team project directory:
# - Developers group can read and write
# - Sticky bit prevents deletion of others' files
# - SGID ensures all files inherit 'developers' group

sudo mkdir /projects/teamapp
sudo chown root:developers /projects/teamapp
sudo chmod 2775 /projects/teamapp    # SGID + rwxrwxr-x
sudo chmod +t /projects/teamapp      # Add sticky bit
# Final: 3775 = SGID+Sticky + rwxrwxr-x
```

**Scenario 3: Adding specific user access with ACL**

```bash
# Consultant 'contractor1' needs read access to /etc/nginx/nginx.conf
# Without changing the file's owner or group
sudo setfacl -m u:contractor1:r-- /etc/nginx/nginx.conf
getfacl /etc/nginx/nginx.conf
```

---

### Slide 10 — CompTIA Linux+ Exam Tips for Permissions

The highest-yield exam points for this module:

- Know the octal values cold: r=4, w=2, x=1. Calculate any combination in seconds.
- `chmod 755`, `644`, `600`, `700` — know what each looks like symbolically
- SUID shows as `s` in owner execute position; SGID shows as `s` in group execute position; sticky shows as `t` in others execute position
- Capital `S` or `T` means the bit is set but execute is not (unusual/error condition)
- SUID on a directory is generally ignored by most modern kernels
- `find / -perm -4000` finds SUID files; `-perm -2000` finds SGID; `-perm -1000` finds sticky
- The `+` at end of `ls -l` output means an ACL is set — use `getfacl` to view it
- Default ACLs (setfacl `-d`) are inherited by new files in a directory
- The ACL mask limits effective permissions for named entries
- umask 022 → new files get 644, new dirs get 755
- umask 027 → new files get 640, new dirs get 750

```bash
# Quick permission calculation practice commands
stat --format="%a" filename    # Show octal permissions
find / -perm /6000 -type f 2>/dev/null  # Find SUID or SGID files
ls -l | grep "^-.*s"           # Find SUID files in current directory
getfacl -R /directory          # Show all ACLs recursively
```

---

### Slide 11 — Module 08 Wrap-Up

Excellent work. You can now:

- Read any permission string and convert between symbolic and octal notation
- Use `chmod` with both symbolic and octal modes
- Change ownership with `chown` and `chgrp`
- Understand and configure `umask`
- Explain and set SUID, SGID, and sticky bit
- Create, view, and modify ACLs with `setfacl` and `getfacl`
- Set default ACLs on directories for inherited permissions

Head to the Reading Guide for detailed reference tables and additional practice. The Lab walks you through building a complete permission structure for a simulated web server environment. The quiz covers both traditional permissions and ACLs.

Module 9 covers Shell Scripting Fundamentals — see you there.
