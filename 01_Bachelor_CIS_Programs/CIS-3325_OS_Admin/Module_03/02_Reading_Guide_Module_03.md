# Reading Guide: Module 03 - File Permissions and Ownership

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

## 9. Supplemental Resources

**1. The Linux Command Line — William Shotts (Chapter 9: Permissions)**
URL: https://linuxcommand.org/tlcl.php
Coverage: Covers chmod, chown, umask, and special bits with worked examples. The chapter
explains the octal notation system and symbolic notation side by side.

**2. Linux man pages online — chmod(1), chown(1), umask(2)**
URL: https://man7.org/linux/man-pages/man1/chmod.1.html
Coverage: Authoritative reference for chmod symbolic and numeric modes, chown user:group
syntax, and the umask system call. Read the DESCRIPTION and EXAMPLES sections for both
chmod and chown.

**3. TLDP — Linux Security HOWTO: File Permissions**
URL: https://tldp.org/HOWTO/Security-HOWTO/file-security.html
Coverage: Explains SUID/SGID/sticky bit security implications in production environments.
Covers how attackers exploit misconfigured SUID binaries and best practices for auditing.

**4. Red Hat Documentation — Managing file permissions**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/managing-file-permissions_configuring-basic-system-settings
Coverage: RHEL 9 guide covering standard permissions, ACLs with setfacl/getfacl, and
default ACL inheritance for shared directories. Directly relevant to the SGID shared
directory pattern used in the lab.

**5. ArchWiki — Access Control Lists**
URL: https://wiki.archlinux.org/title/Access_Control_Lists
Coverage: Comprehensive guide to POSIX ACLs including setfacl, getfacl, default ACLs,
mask entries, and how ACLs interact with standard Unix permissions. Covers the ACL mask
concept which determines the effective permissions for named users and groups.

### Required Reading

Read chapters 9 and 10 of The Linux Command Line by William Shotts (linuxcommand.org/tlcl.php),
covering permissions, ownership, and the special permission bits in depth.
