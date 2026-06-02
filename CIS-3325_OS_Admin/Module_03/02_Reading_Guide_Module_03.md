# Reading Guide: Module 03 - File Permissions and Ownership

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 03. File permissions and ownership form the primary access control mechanism
in Linux. This reading guide provides the complete reference material for the quiz, lab, and
Linux+ exam. Permissions are one of the most heavily tested topics on the XK0-005 exam, appearing
in both direct questions and scenario-based questions.

---

### 1. High-Yield Glossary

**Discretionary Access Control (DAC):** The standard Linux permission model where the file owner
decides who can access the file. Contrast with Mandatory Access Control (MAC), which is enforced
by the kernel regardless of owner choices (covered in Module 14 with SELinux/AppArmor).

**Permission Triplets (rwx):** Every file has three permission sets: owner (user), group, and
others. Each set contains three bits: read (r=4), write (w=2), execute (x=1).

**Octal Notation:** Representing permission sets as single digits 0-7 by summing active bit values.
rwx=7, rw-=6, r-x=5, r--=4, -wx=3, -w-=2, --x=1, ---=0.

**chmod:** Command to change file permission bits. Accepts octal notation (chmod 644 file) or
symbolic notation (chmod u+x file). Use -R for recursive application.

**chown:** Command to change file owner and/or group. Syntax: chown user:group filename. Requires
root or sudo for files you do not own.

**chgrp:** Command to change group ownership only. Equivalent to chown :group filename.

**umask:** A process attribute that masks out bits from the default permissions when new files
(base 666) and directories (base 777) are created. Subtracted from the base.

**SUID (Set User ID):** Special bit on an executable file causing the process to run as the file's
owner, not the invoking user. Shown as s in the owner execute position. Classic example:
/usr/bin/passwd running as root.

**SGID (Set Group ID):** Special bit on an executable or directory. On executables: process runs
as file's group. On directories: new files created inside inherit the directory's group.

**Sticky Bit:** Special bit on a directory preventing users from deleting or renaming files they
do not own, even with write permission on the directory. Used on /tmp.

**Access Control List (ACL):** Extension to standard DAC allowing specific permissions for any
number of users and groups on a single file. Managed with getfacl and setfacl.

**inode:** Data structure storing file metadata: permissions, ownership, timestamps, and block
locations. The permission bits are stored in the inode, not in the directory entry.

---

### 2. Permission Notation Reference

#### Octal Permission Values

| Octal | Binary | Symbolic | Meaning |
|-------|--------|----------|---------|
| 7 | 111 | rwx | Read, write, execute |
| 6 | 110 | rw- | Read and write |
| 5 | 101 | r-x | Read and execute |
| 4 | 100 | r-- | Read only |
| 3 | 011 | -wx | Write and execute |
| 2 | 010 | -w- | Write only |
| 1 | 001 | --x | Execute only |
| 0 | 000 | --- | No permissions |

#### Common Permission Combinations

| Octal | Symbolic | Typical Use |
|-------|----------|-------------|
| 755 | rwxr-xr-x | Executable scripts, directories |
| 644 | rw-r--r-- | Regular files, config files |
| 600 | rw------- | Private keys, sensitive configs |
| 640 | rw-r----- | Config readable by group only |
| 700 | rwx------ | Private executable |
| 777 | rwxrwxrwx | World-writable (avoid in prod) |
| 664 | rw-rw-r-- | Group-editable files |
| 750 | rwxr-x--- | Executable for owner and group |

#### Special Permission Bits

| Bit | Octal Prefix | ls Symbol (exec set) | ls Symbol (exec not set) |
|-----|-------------|---------------------|--------------------------|
| SUID | 4 | s (in owner exec position) | S |
| SGID | 2 | s (in group exec position) | S |
| Sticky | 1 | t (in others exec position) | T |

Combined: 4755 = SUID + rwxr-xr-x, 2775 = SGID + rwxrwxr-x, 1777 = Sticky + rwxrwxrwx

---

### 3. chmod Command Reference

| Command | Result |
|---------|--------|
| chmod 644 file | Owner rw-, group r--, others r-- |
| chmod 755 file | Owner rwx, group r-x, others r-x |
| chmod 600 file | Owner rw-, group ---, others --- |
| chmod 777 file | All: rwx |
| chmod 4755 file | SUID + 755 |
| chmod 2775 dir | SGID + 775 |
| chmod 1777 dir | Sticky + 777 |
| chmod u+x file | Add execute for owner only |
| chmod g-w file | Remove write from group |
| chmod o= file | Clear all permissions for others |
| chmod a+r file | Add read for all (user, group, others) |
| chmod u=rw,g=r,o= file | Set all three levels explicitly |
| chmod -R 755 /dir | Apply 755 recursively to all contents |

---

### 4. chown and chgrp Reference

| Command | Result |
|---------|--------|
| chown alice file | Change owner to alice |
| chown alice:devs file | Change owner to alice, group to devs |
| chown :devs file | Change group to devs only |
| chgrp devs file | Change group to devs only |
| chown -R alice:devs /dir | Recursively change owner and group |
| ls -l file | Verify owner and group |
| stat file | Show detailed ownership and permission info |

---

### 5. umask Calculation Reference

| umask | File permissions | Directory permissions |
|-------|-----------------|----------------------|
| 000 | 666 (rw-rw-rw-) | 777 (rwxrwxrwx) |
| 022 | 644 (rw-r--r--) | 755 (rwxr-xr-x) |
| 027 | 640 (rw-r-----) | 750 (rwxr-x---) |
| 077 | 600 (rw-------) | 700 (rwx------) |
| 002 | 664 (rw-rw-r--) | 775 (rwxrwxr-x) |

To check current umask: `umask`
To set umask for session: `umask 027`
To set umask permanently: add `umask 027` to ~/.bashrc or /etc/profile

---

### 6. Special File Indicators in ls -l

| First Character | Meaning |
|-----------------|---------|
| - | Regular file |
| d | Directory |
| l | Symbolic link |
| c | Character device file |
| b | Block device file |
| p | Named pipe (FIFO) |
| s | Socket file |

---

### 7. find Commands for Permission Searches

| Command | Purpose |
|---------|---------|
| find / -perm /4000 2>/dev/null | Find all SUID files |
| find / -perm /2000 2>/dev/null | Find all SGID files |
| find / -perm /1000 2>/dev/null | Find all sticky-bit directories |
| find / -perm 777 2>/dev/null | Find world-writable files |
| find /home -perm 600 | Find files with exactly 600 in /home |
| find / -user alice 2>/dev/null | Find files owned by alice |
| find / -group devs 2>/dev/null | Find files owned by group devs |

---

### 8. ACL Quick Reference

| Command | Purpose |
|---------|---------|
| getfacl filename | Display ACL entries for a file |
| setfacl -m u:alice:rw file | Add/modify ACL: alice gets rw |
| setfacl -m g:devs:r file | Add/modify ACL: devs group gets r |
| setfacl -x u:alice file | Remove ACL entry for alice |
| setfacl -b file | Remove all ACL entries |
| setfacl -d -m g:devs:rwx /dir | Set default ACL for new files in directory |

When a file has an ACL, ls -l shows a + after the permission string: -rw-r--r--+

---

### 9. CompTIA Linux+ Exam Tips

**Exam Tip 1:** Know the octal math cold. Practice converting these pairs instantly: 755 = rwxr-xr-x,
644 = rw-r--r--, 600 = rw-------, 640 = rw-r-----, 750 = rwxr-x---.

**Exam Tip 2:** SUID, SGID, and sticky bit questions are common. Remember: SUID on executables
runs as file owner. SGID on directories inherits group. Sticky on /tmp protects deletion.

**Exam Tip 3:** Lowercase s and t in ls output means the corresponding execute bit is ALSO set.
Uppercase S and T means the special bit is set but execute is NOT. Uppercase S is suspicious on
SUID executables.

**Exam Tip 4:** umask subtracts from 666 for files and 777 for directories. Files cannot get
execute bits from umask because the base for files is 666 (no execute). A umask of 027 gives
files 640, not 750.

**Exam Tip 5:** chown requires root. Regular users can only chown files they own, and even then
only if the target username is themselves (which is trivial). In practice, always use sudo chown.

**Exam Tip 6:** /etc/passwd is world-readable. /etc/shadow is root-readable only. This split
is intentional security design that the exam tests directly.

**Exam Tip 7:** To prevent a user from deleting another user's files in a shared directory,
set the sticky bit (chmod 1777 or chmod +t). Do not use chmod to remove write permission from
others because that breaks the shared-write purpose.

**Exam Tip 8:** The find / -perm /4000 command finds SUID files. This is a standard security
audit procedure. On a clean system you should see only well-known utilities like passwd, sudo,
and su. Unexpected SUID files can indicate compromise.

---

### 10. Study Checklist

- [ ] Watch both parts of the Module 03 video lecture
- [ ] Memorize the octal permission values (r=4, w=2, x=1)
- [ ] Practice calculating permissions for 20 different octal values without notes
- [ ] Understand chmod symbolic notation (u+x, g-w, o=r, a+r)
- [ ] Understand chown syntax for user, group, and both
- [ ] Understand umask subtraction for files and directories
- [ ] Understand SUID, SGID, and sticky bit behavior and use cases
- [ ] Know the ls symbol representations (s, S, t, T) for special bits
- [ ] Complete the Module 03 Lab
- [ ] Complete the Module 03 Quiz
- [ ] Post to the Discussion by Wednesday at 11:59 PM
- [ ] Reply to two classmates by Sunday at 11:59 PM

---

### Required Reading

Read chapters 9 and 10 of The Linux Command Line by William Shotts (linuxcommand.org/tlcl.php),
covering permissions, ownership, and the special permission bits in depth.
