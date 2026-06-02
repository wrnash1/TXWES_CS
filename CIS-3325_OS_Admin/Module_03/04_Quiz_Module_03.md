# Quiz: Module 03 - File Permissions and Ownership

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

An administrator executes the command `chmod 644 confidential.txt`. What permissions does this
command assign to the file?

- A) The owner has read and write access, while the group and others have read-only access.
- B) The owner has full access (read, write, execute), while the group has read-only access.
- C) The owner has read-only access, while the group and others have read and write access.
- D) The owner and the group have read and write access, while others have no access.

Correct Answer: A) The owner has read and write access, while the group and others have read-only access.

Distractor Analysis:

- Why B is incorrect: Full access is represented by a 7 (4+2+1=rwx). The first digit here is 6 (4+2=rw-), which is read and write only, not execute.
- Why C is incorrect: This describes a permission string like 466, where only the group and others can write - an insecure and non-standard configuration.
- Why D is incorrect: This describes octal 660 (rw-rw----), not 644. The digit 4 represents read-only (r--), not read-write.

---

**Question 2**

Which file in a standard Linux system contains the securely hashed passwords for local user
accounts?

- A) /etc/passwd
- B) /etc/shadow
- C) /etc/group
- D) /var/log/auth.log

Correct Answer: B) /etc/shadow

Distractor Analysis:

- Why A is incorrect: Historically passwords were stored in /etc/passwd, but modern systems store only an x placeholder there. The actual hashed passwords are in /etc/shadow, which is readable only by root.
- Why C is incorrect: /etc/group defines local groups and their member lists, not password hashes.
- Why D is incorrect: /var/log/auth.log records authentication events such as login attempts and sudo usage. It does not store password hashes.

---

**Question 3**

A systems administrator needs to restrict a configuration file so that only the file owner can
read and write it, and no other users have any access at all. Which command achieves this?

- A) chmod 600 config.conf
- B) chmod 644 config.conf
- C) chmod 755 config.conf
- D) chmod 777 config.conf

Correct Answer: A) chmod 600 config.conf

Distractor Analysis:

- Why B is incorrect: chmod 644 gives the owner read+write but grants read access to the group and others (r--), which violates the requirement of no access for other users.
- Why C is incorrect: chmod 755 gives the owner full access and grants read+execute to the group and others - far too permissive for a sensitive configuration file.
- Why D is incorrect: chmod 777 grants read, write, and execute to everyone on the system, which is the least secure option possible.

---

**Question 4**

A Linux system has a umask value of 027. When a standard user creates a new text file, what
will the file's permissions be?

- A) 640 (rw-r-----)
- B) 644 (rw-r--r--)
- C) 750 (rwxr-x---)
- D) 600 (rw-------)

Correct Answer: A) 640 (rw-r-----)

Distractor Analysis:

- Why B is incorrect: 644 results from a umask of 022 (666 - 022 = 644), not 027.
- Why C is incorrect: 750 is a directory permission pattern. New regular files use a base of 666, not 777. Even with umask 027, files do not receive execute bits.
- Why D is incorrect: 600 would result from a umask of 066 (666 - 066 = 600), not 027.

---

**Question 5**

The /usr/bin/passwd command is owned by root but can be run by any user to change their own
password. It must write to /etc/shadow, which is only readable by root. Which special permission
bit enables this behavior?

- A) The sticky bit set on /usr/bin/passwd
- B) The SGID bit set on /etc/shadow
- C) The SUID bit set on /usr/bin/passwd
- D) The SGID bit set on /usr/bin/passwd

Correct Answer: C) The SUID bit set on /usr/bin/passwd

Distractor Analysis:

- Why A is incorrect: The sticky bit on a file is rarely used in modern Linux and does not cause a process to run with elevated privileges. The sticky bit is meaningful on directories (like /tmp), not on executables.
- Why B is incorrect: SGID on a file causes the process to run with the file's group privileges, not owner privileges. Setting SGID on /etc/shadow itself would not help passwd write to it as root.
- Why D is incorrect: SGID on an executable causes it to run with the file's group identity, not as the root user. /usr/bin/passwd needs to run as root (the owner), which requires SUID, not SGID.

---

**Question 6**

An administrator uses the command `ls -la /tmp` and sees the output showing permissions of
drwxrwxrwt for the /tmp directory. What does the t in the permissions string indicate?

- A) The directory is owned by a temporary user account.
- B) The sticky bit is set, preventing users from deleting or renaming files they do not own.
- C) The directory is mounted as a tmpfs filesystem and is cleared on reboot.
- D) The directory has the SGID bit set, causing files created inside to inherit the group.

Correct Answer: B) The sticky bit is set, preventing users from deleting or renaming files they do not own.

Distractor Analysis:

- Why A is incorrect: The t character in the permission string is a standard permission bit indicator, not related to user account types. There is no "temporary user" designation in Linux permissions.
- Why C is incorrect: Whether /tmp uses tmpfs storage (cleared on reboot) is a mount option configured in /etc/fstab. The t in permissions is the sticky bit, which is a separate concept from the filesystem type.
- Why D is incorrect: SGID is shown as s in the group execute position (characters 5-7), not as t. The t character specifically represents the sticky bit, which appears in the others execute position (character 10).

---

**Question 7**

An administrator runs `chmod 2770 /opt/teamshared` to set up a shared directory. What do the
permissions 2770 accomplish?

- A) Sets the directory as world-writable with SUID for automatic ownership elevation.
- B) Sets SGID so files created in the directory inherit its group, and gives owner and group full access while blocking others.
- C) Sets the sticky bit so only file owners can delete their own files in the directory.
- D) Creates a read-only directory for the group with execute permission for others.

Correct Answer: B) Sets SGID so files created in the directory inherit its group, and gives owner and group full access while blocking others.

Distractor Analysis:

- Why A is incorrect: World-writable means others have write access (chmod 777 or similar). The digit 0 in the others position means no access for others. The leading 2 is SGID, not SUID (which would be 4).
- Why C is incorrect: The sticky bit is represented by the digit 1 in the special bits position, not 2. The leading 2 is the SGID bit. chmod 1770 would set the sticky bit instead.
- Why D is incorrect: The octal 770 gives owner and group rwx and others no access (---). Read-only for group would be 740 or similar. No part of 2770 is read-only for the group.

---

**Question 8**

A junior administrator wants to change the group ownership of /var/app/data to the appgroup
group without changing the file owner. Which command is correct?

- A) chown appgroup /var/app/data
- B) chown :appgroup /var/app/data
- C) chmod appgroup /var/app/data
- D) useradd -g appgroup /var/app/data

Correct Answer: B) chown :appgroup /var/app/data

Distractor Analysis:

- Why A is incorrect: chown appgroup /var/app/data would attempt to change the owner to a user named appgroup. The colon separator is required to indicate group ownership. Without the colon, chown interprets the argument as a username.
- Why C is incorrect: chmod changes permission bits (read, write, execute), not ownership. The chmod command does not accept group names as arguments.
- Why D is incorrect: useradd creates a new user account. It has no ability to change file ownership. Using it this way would produce an error or unexpected behavior.

---

**Question 9**

A security audit finds a file at /usr/local/bin/cleanup with the SUID bit set and the owner is
root. The file has an uppercase S in the owner execute position (shown as -rwSr-xr-x). What
security concern does the uppercase S indicate?

- A) The file is encrypted and cannot be executed by any user.
- B) SUID is set but the execute bit is not set for the owner. The file cannot run, making SUID effectively inactive, but the misconfigured special bit should be investigated.
- C) The uppercase S means SGID is set instead of SUID, causing the file to run as its group.
- D) The uppercase S indicates the file was recently modified and has not been verified by the package manager.

Correct Answer: B) SUID is set but the execute bit is not set for the owner. The file cannot run, making SUID effectively inactive, but the misconfigured special bit should be investigated.

Distractor Analysis:

- Why A is incorrect: Encryption is not indicated by permission bits in ls output. An uppercase S is strictly a permission notation for "SUID set, execute bit not set." Encryption would require separate tooling to detect.
- Why C is incorrect: SGID is shown in the group execute position (character 6 in the permission string), not the owner execute position (character 3). An s or S in the owner execute position always indicates SUID. SGID appears in the group execute position.
- Why D is incorrect: ls permission strings have no mechanism for indicating file modification status. Modification time is shown in a separate column. Package integrity is verified with rpm -V or dpkg --verify, not permission bits.

---

**Question 10**

An administrator needs to find all world-writable files on a Linux system as part of a security
hardening review. Which find command is most appropriate?

- A) find / -perm 777 2>/dev/null
- B) find / -perm -o+w -type f 2>/dev/null
- C) find / -perm /4000 2>/dev/null
- D) find / -writable -user others 2>/dev/null

Correct Answer: B) find / -perm -o+w -type f 2>/dev/null

Distractor Analysis:

- Why A is incorrect: find / -perm 777 finds only files with the exact permissions 777 (all three levels fully open). A file with permissions 776, 675, or 664 would have the others write bit set but would not match 777 exactly. The -o+w approach catches any file where others has write, regardless of other bits.
- Why C is incorrect: find / -perm /4000 finds SUID files, not world-writable files. The /4000 pattern tests for the SUID special bit, which is a completely different security concern.
- Why D is incorrect: find does not support -user others as a valid expression. -user takes a username or UID. The others permission category is not a user. The -perm -o+w syntax is the correct approach for testing the others write bit.
