# Reading Guide: Module 08 — File System Permissions and Ownership

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Overview

This reading guide provides complete reference material for Linux file system permissions. Work through all sections and use the command references when practicing in your lab. The exam tests both recognition (reading permission output) and application (choosing the correct command to achieve a stated result).

**Estimated Reading Time:** 45–60 minutes

---

## Section 1 — The Permission Model Foundation

### 1.1 How the Kernel Checks Permissions

When a process attempts to access a file, the kernel performs these checks in order:

1. Is the process running as root (UID 0)? If yes, bypass permission checks entirely (with minor exceptions for execute).
2. Is the process's effective UID the same as the file's owner UID? If yes, apply owner permission bits.
3. Is the process's effective GID (or any supplementary GID) the same as the file's group GID? If yes, apply group permission bits.
4. Apply the "other" permission bits.

This is a first-match model. If you are the owner, owner permissions apply — even if the group or other permissions are more permissive. The kernel stops checking after the first match.

### 1.2 Effective vs. Real UID

A process has both a real UID (who actually ran the process) and an effective UID (what UID the process is running as for permission checks). Normally these are the same. SUID and SGID programs create a difference between them — a topic we cover in Section 5.

### 1.3 Viewing Permissions

```bash
# Long listing format — most common way to view permissions
ls -l file.txt
# -rw-r--r-- 1 alice developers 1024 Jan 15 2024 file.txt

# Long listing for a directory itself (not its contents)
ls -ld /var/www/html

# Show all files including hidden (dot files)
ls -la /home/alice

# Show octal permissions with stat
stat file.txt
stat --format="%a %U %G %n" file.txt    # octal, owner, group, name

# Show permissions as numbers with find
find /var/www -ls
```

---

## Section 2 — Permission Bit Reference Tables

### 2.1 File Permission Effects

| Bit | On Files | On Directories |
|---|---|---|
| r (4) | Read file contents | List directory contents (ls) |
| w (2) | Modify file contents | Create/delete/rename files within |
| x (1) | Execute as program | Enter directory and access contents |

### 2.2 Octal Conversion Table

| Octal | Binary | Symbolic | Permissions |
|---|---|---|---|
| 0 | 000 | --- | None |
| 1 | 001 | --x | Execute only |
| 2 | 010 | -w- | Write only |
| 3 | 011 | -wx | Write and execute |
| 4 | 100 | r-- | Read only |
| 5 | 101 | r-x | Read and execute |
| 6 | 110 | rw- | Read and write |
| 7 | 111 | rwx | Read, write, and execute |

### 2.3 Common Permission Patterns

| Mode | Symbolic | Typical File Use | Typical Directory Use |
|---|---|---|---|
| 700 | rwx------ | Private executable | Private directory |
| 750 | rwxr-x--- | Group-executable | Group-accessible |
| 755 | rwxr-xr-x | Public executable, script | Public directory |
| 777 | rwxrwxrwx | Avoid — insecure | Avoid — insecure |
| 600 | rw------- | Private data, SSH keys | N/A |
| 640 | rw-r----- | Group-readable config | N/A |
| 644 | rw-r--r-- | Standard config/data | N/A |
| 664 | rw-rw-r-- | Shared team files | N/A |
| 666 | rw-rw-rw- | Avoid — world writable | N/A |

---

## Section 3 — chmod Complete Reference

### 3.1 Octal Mode

```bash
# Four-digit form (recommended to avoid ambiguity with special bits)
chmod 0755 script.sh     # Explicit: no special bits + rwxr-xr-x
chmod 4755 setuid_prog   # SUID + rwxr-xr-x
chmod 2775 shared_dir    # SGID + rwxrwxr-x
chmod 1777 upload_dir    # Sticky + rwxrwxrwx
chmod 6750 special       # SUID+SGID + rwxr-x---

# Three-digit form (implies 0 for special bits unless adding)
chmod 755 script.sh
```

### 3.2 Symbolic Mode Reference

| Symbol | Meaning |
|---|---|
| u | User (owner) |
| g | Group |
| o | Others |
| a | All (u+g+o) |
| + | Add permission |
| - | Remove permission |
| = | Set exactly (replaces current) |

```bash
# Add/remove examples
chmod u+x file           # Add execute for owner
chmod o-r file           # Remove read for others
chmod go-wx file         # Remove write and execute for group and others
chmod a+r file           # Add read for everyone
chmod a-x file           # Remove execute for everyone

# Set exactly (= replaces current bits for that class)
chmod u=rw file          # Owner: rw-
chmod g=r file           # Group: r--
chmod o= file            # Others: --- (removes all)
chmod u=rwx,g=rx,o= dir  # Complete specification

# Special bit symbols
chmod u+s file           # Set SUID
chmod g+s dir            # Set SGID
chmod o+t dir            # Set sticky
chmod u-s file           # Remove SUID
```

### 3.3 Recursive chmod Patterns

```bash
# Recursive — applies to everything under the path
chmod -R 755 /var/www/html     # Applies 755 to ALL files AND directories

# Better approach: different modes for files vs directories
find /var/www/html -type f -exec chmod 644 {} \;
find /var/www/html -type d -exec chmod 755 {} \;

# Using find with -perm to fix only incorrect permissions
find /var/www -type f -perm /o+w -exec chmod o-w {} \;
```

---

## Section 4 — Ownership Management

### 4.1 chown Reference

```bash
# Syntax: chown [OPTIONS] [OWNER[:GROUP]] FILE...

# Change owner only
sudo chown alice file.txt

# Change owner and group
sudo chown alice:developers file.txt
sudo chown alice.developers file.txt    # Deprecated dot syntax

# Change group only
sudo chown :developers file.txt

# Recursive
sudo chown -R www-data:www-data /var/www/html

# Do not follow symbolic links (change symlink itself, not target)
sudo chown -h alice symlink

# Use a reference file's ownership
sudo chown --reference=sourcefile targetfile

# Verbose output
sudo chown -v alice:developers file.txt
```

### 4.2 chgrp Reference

```bash
# Syntax: chgrp [OPTIONS] GROUP FILE...

# Change group
sudo chgrp developers file.txt

# Recursive
sudo chgrp -R developers /projects/app/

# Do not follow symlinks
sudo chgrp -h developers symlink

# Verbose
sudo chgrp -v developers file.txt
```

### 4.3 Ownership Rules

- Only root can change the owner of a file.
- A user can change a file's group only if they own the file AND are a member of the target group.
- `chown user:group` requires root to change the owner; the group part can be done by the owner if they are a member.

---

## Section 5 — Special Permission Bits Deep Dive

### 5.1 SUID Security Implications

SUID enables privilege escalation by design. The security impact is severe if SUID is applied to an inappropriate program.

```bash
# List of typical legitimate SUID programs
sudo find / -perm -4000 -type f -ls 2>/dev/null

# Common legitimate SUID binaries:
# /usr/bin/passwd    — write to /etc/shadow
# /usr/bin/su        — switch user
# /usr/bin/sudo      — privilege escalation
# /usr/bin/pkexec    — PolicyKit elevation
# /usr/bin/newgrp    — change active group
# /usr/sbin/mount.nfs — mount NFS filesystems

# Security audit: any unexpected SUID binary is a red flag
# Compare against a known-good baseline
```

### 5.2 SGID on Directories — Practical Use

SGID on directories is one of the most useful features for collaborative environments:

```bash
# Create a shared project directory
sudo mkdir -p /projects/website
sudo chown root:webteam /projects/website
sudo chmod 2775 /projects/website

# All new files get 'webteam' as their group, regardless of creator's primary group
# This means all team members can modify each other's files (if they are in webteam)

# Verify SGID effect:
id alice          # alice's primary group is 'staff'
sudo su alice
touch /projects/website/index.html
ls -l /projects/website/index.html
# -rw-r--r-- 1 alice webteam ...   <-- group is webteam, not staff
```

### 5.3 Sticky Bit — Real-World Examples

```bash
# /tmp always has sticky bit — verify
ls -ld /tmp
# drwxrwxrwt ...

# /var/tmp also typically has sticky bit
ls -ld /var/tmp

# Custom shared upload directory
sudo mkdir /var/uploads
sudo chmod 1777 /var/uploads

# Test: user alice creates a file; user bob cannot delete it
su alice
touch /var/uploads/alice_file.txt

su bob
rm /var/uploads/alice_file.txt
# rm: cannot remove '/var/uploads/alice_file.txt': Operation not permitted
```

### 5.4 Special Bit Numeric Summary

| Octal | Binary | Name |
|---|---|---|
| 4000 | 100 000 000 000 | SUID |
| 2000 | 010 000 000 000 | SGID |
| 1000 | 001 000 000 000 | Sticky |

---

## Section 6 — umask Deep Dive

### 6.1 How umask Is Applied

The umask works by **masking out** bits from the default permissions:

```
File creation default:  666  (rw-rw-rw-)
umask:                  022  (-w--w-)
Bitwise AND of NOT:     644  (rw-r--r--)

Directory creation default:  777  (rwxrwxrwx)
umask:                       022  (-w--w-)
Result:                      755  (rwxr-xr-x)
```

A bit that is set in the umask is REMOVED from the resulting permissions. A bit that is 0 in the umask is ALLOWED through.

### 6.2 Setting umask Persistently

```bash
# For a single user — add to ~/.bashrc or ~/.bash_profile
echo "umask 027" >> ~/.bashrc

# System-wide default — /etc/profile or /etc/bashrc
sudo echo "umask 022" >> /etc/profile

# PAM-based default (per-user, more sophisticated)
# /etc/pam.d/common-session or /etc/pam.d/system-auth:
# session optional pam_umask.so umask=027

# Check current umask
umask         # Octal form (e.g., 0022)
umask -S      # Symbolic form (e.g., u=rwx,g=rx,o=rx)
```

---

## Section 7 — ACLs Complete Reference

### 7.1 ACL Entry Types

| Entry Type | Format | Description |
|---|---|---|
| Owner | `user::perms` | Traditional owner permissions |
| Named user | `user:name:perms` | Specific user |
| Owning group | `group::perms` | Traditional group permissions |
| Named group | `group:name:perms` | Specific group |
| Mask | `mask::perms` | Maximum for named entries |
| Other | `other::perms` | Traditional other permissions |

### 7.2 The ACL Mask

The mask entry controls the maximum effective permissions for all named user and named group entries (not the owner, not other). It is automatically calculated as the union of all named entries when you set ACLs.

```bash
# Example of mask limiting effective permissions
setfacl -m u:bob:rwx file.txt    # Set Bob to rwx
setfacl -m m::r-- file.txt      # Set mask to r--

getfacl file.txt
# user:bob:rwx          #effective:r--
# mask::r--

# Bob's effective permission is r-- even though ACL says rwx
# The mask acts as a ceiling
```

### 7.3 Default ACLs

Default ACLs are set with the `-d` flag and apply to a directory. New files and subdirectories created in that directory inherit the default ACL.

```bash
# Set default ACL: group developers gets rw- on all new files
setfacl -d -m g:developers:rw- /shared/project/

# Set default ACL: group developers gets rwx on all new directories
setfacl -d -m g:developers:rwx /shared/project/

# View default ACLs
getfacl /shared/project/
# default:user::rwx
# default:group::r-x
# default:group:developers:rw-
# default:mask::rwx
# default:other::r-x

# Remove all default ACLs
setfacl -k /shared/project/

# Copy ACL including defaults from one directory to another
getfacl --access /source/dir | setfacl --set-file=- /target/dir
```

### 7.4 Backing Up and Restoring ACLs

```bash
# Backup ACLs for a directory tree
getfacl -R /shared/project > /backup/project_acls.txt

# Restore ACLs
setfacl --restore=/backup/project_acls.txt
```

---

## Section 8 — Troubleshooting Permissions

### 8.1 Common Permission Errors and Causes

| Error Message | Likely Cause | Solution |
|---|---|---|
| `Permission denied` on file read | Missing `r` for user class | `chmod a+r` or fix ownership |
| `Permission denied` on `cd` | Missing `x` on directory | `chmod a+x dir` |
| `Permission denied` on file delete | Missing `w` on parent directory | `chmod u+w parentdir` |
| `Permission denied` on script execution | Missing `x` on file | `chmod u+x script.sh` |
| ACL set but still denied | ACL mask blocking | Check `getfacl`; adjust mask |
| SUID/SGID not working | Filesystem mounted `nosuid` | Check mount options |

### 8.2 Debugging Permission Problems

```bash
# Step 1: Check the file's permissions and ownership
ls -l /path/to/file
stat /path/to/file

# Step 2: Check the current user's identity and groups
id
groups

# Step 3: Check all directories in the path
namei -l /path/to/file    # Shows permissions at each level of the path

# Step 4: Check for ACLs
getfacl /path/to/file

# Step 5: Check if filesystem has ACL/nosuid restrictions
mount | grep "$(df -P /path/to/file | tail -1 | cut -d' ' -f1)"
```

---

## Section 9 — Key Terms Glossary

| Term | Definition |
|---|---|
| DAC | Discretionary Access Control — file owner controls permissions |
| octal notation | Base-8 numeric permission representation (0–7 per class) |
| symbolic notation | Letter-based permission notation (r, w, x, u, g, o) |
| umask | User file creation mask — bits subtracted from default permissions |
| SUID | Set User ID — file runs with owner's effective UID |
| SGID | Set Group ID — file runs with owner's effective GID; dir inherits group |
| sticky bit | Directory protection — users can only delete their own files |
| ACL | Access Control List — extends permissions beyond owner/group/other |
| mask | ACL entry limiting effective permissions for named entries |
| default ACL | ACL inherited by new files created in a directory |
| effective UID | The UID used for permission checks (may differ from real UID with SUID) |
| `namei` | Utility to trace path components and show permissions at each level |

---

## Section 10 — Review Questions

1. What is the octal representation of `rwxr-x---`?

2. A file has permissions `rw-rw-r--`. The owner is `alice` and the group is `developers`. Bob is a member of `developers`. Can Bob write to the file?

3. What is the effect of `chmod o-r,g-w config.conf`?

4. If the current umask is `027`, what permissions will a newly created file have? A newly created directory?

5. What does the `s` in `-rwsr-xr-x` indicate, and what does it cause the program to do?

6. What is the difference between SGID on a file and SGID on a directory?

7. What does the `+` at the end of `ls -l` output indicate?

8. How do you remove all ACL entries from a file?

9. What is the ACL mask and how does it affect named user and group entries?

10. What command would you use to trace the permissions of every directory component in the path `/var/www/html/index.html`?

---

## Additional Resources

- `man 1 chmod` — chmod command reference
- `man 1 chown` — chown command reference
- `man 1 getfacl` — getfacl command reference
- `man 1 setfacl` — setfacl command reference
- `man 5 acl` — ACL format documentation
- `man 1 namei` — namei path permission tracer
- Linux+ Study Guide (CompTIA XK0-005) — Domain 2: Security, File Permissions section

---

## 9. Supplemental Resources

**1. [Linux File Permissions Explained — Red Hat Enable Sysadmin](https://www.redhat.com/sysadmin/linux-file-permissions-explained)**
A practical Red Hat sysadmin article covering standard Unix permission bits, octal notation, the SUID/SGID/sticky bit, and real-world scenarios where each special bit applies. Includes worked examples with `chmod`, `chown`, and `ls -l` output interpretation — directly aligned with the Module 08 lab tasks on special bit configuration and permission debugging.

**2. [Arch Linux Wiki — Access Control Lists](https://wiki.archlinux.org/title/Access_Control_Lists)**
The definitive community reference for POSIX ACLs on Linux. Covers `setfacl` and `getfacl` syntax in depth, the ACL mask and its effect on effective permissions, default ACLs for directories, and how ACLs interact with standard Unix permissions. Includes examples for both named-user and named-group ACL entries and how to back up and restore complete ACL trees with `getfacl -R` and `setfacl --restore`.

**3. [Understanding Linux File Permissions — TLDP](https://tldp.org/HOWTO/Security-HOWTO/file-security.html)**
The Linux Documentation Project's security HOWTO chapter on file security. Provides accessible coverage of umask calculation, the implications of world-writable directories, SUID/SGID security risks, and the principle of least privilege applied to file ownership. A useful complement to the lab's security audit challenges and the exam's Domain 2 security objectives.
