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

---

Questions 11-20 — 5 pts each

---

**Question 11**

An administrator wants to recursively set permissions on all files in /var/www/html to 644
and all directories in the same tree to 755. Which combination of commands achieves this?

- A) chmod -R 755 /var/www/html
- B) chmod -R 644 /var/www/html && chmod -R 755 /var/www/html
- C) find /var/www/html -type f -exec chmod 644 {} \; && find /var/www/html -type d -exec chmod 755 {} \;
- D) chown -R www-data:www-data /var/www/html && chmod 644 /var/www/html

Correct Answer: C) find /var/www/html -type f -exec chmod 644 {} \; && find /var/www/html -type d -exec chmod 755 {} \;

Distractor Analysis:

- Why A is incorrect: chmod -R 755 applies 755 to all files and directories. Giving execute permission to regular files (rwxr-xr-x) is unnecessary and a hardening concern for web content files.
- Why B is incorrect: The second chmod -R 755 would overwrite the 644 just set on files, giving all files 755. Running chmod -R twice in sequence does not differentiate files from directories.
- Why D is incorrect: chown changes ownership, not permission bits. The chmod 644 in this option only affects /var/www/html itself (the top directory), not its contents.

---

**Question 12**

A file has permissions -rwsr-xr-x and is owned by root. Which statement accurately describes
what happens when a non-root user executes this file?

- A) The process runs with the permissions of the user who launched it.
- B) The process runs with root's effective UID, gaining root-level access for the duration of execution.
- C) The file is blocked from execution because only root can run SUID files.
- D) The process runs with the group permissions of the file's owning group.

Correct Answer: B) The process runs with root's effective UID, gaining root-level access for the duration of execution.

Distractor Analysis:

- Why A is incorrect: Without SUID, the process would run as the launching user. The lowercase s in the owner execute position (rwsr-xr-x) means SUID is set and the execute bit is also set, so the process elevates to the file owner's UID.
- Why C is incorrect: Any user with execute permission can run a SUID binary. The SUID bit does not restrict who can execute the file — it changes whose identity the process runs under.
- Why D is incorrect: Running as the file's owning group is the behavior of the SGID bit, which appears in the group execute position. This scenario describes SUID (owner position).

---

**Question 13**

An administrator checks /etc/shadow and sees the following entry for a user:

bob:!:19500:0:99999:7:::

What does the ! in the second field indicate?

- A) The account has no password set and can be accessed without authentication.
- B) The account password field is locked, preventing password-based authentication for this account.
- C) The account has expired and must be reactivated by an administrator.
- D) The password hash uses an unsupported algorithm and must be regenerated.

Correct Answer: B) The account password field is locked, preventing password-based authentication for this account.

Distractor Analysis:

- Why A is incorrect: An empty password field (literally nothing between the colons) would indicate no password. The ! prefix specifically means the field is locked.
- Why C is incorrect: Account expiration is controlled by the eighth field in /etc/shadow (the account expiry date in days since epoch). The ! in the password field locks the password, not the account expiry.
- Why D is incorrect: The ! is a deliberate lock prefix, not a corrupted or unrecognized hash. Password hashing algorithm identifiers appear at the beginning of valid hashes (e.g., $6$ for SHA-512).

---

**Question 14**

Which command shows the current umask value for the shell session and also allows it to be
changed?

- A) chmod --umask
- B) umask
- C) getfacl --default
- D) cat /etc/umask

Correct Answer: B) umask

Distractor Analysis:

- Why A is incorrect: chmod modifies permissions of existing files and directories. It has no --umask option and cannot display or modify the session umask.
- Why C is incorrect: getfacl displays Access Control List (ACL) information for specific files. While ACLs have a default ACL concept for directories, getfacl --default is not the command for viewing or setting the session umask.
- Why D is incorrect: There is no /etc/umask file. The system-wide default umask is configured in /etc/profile or /etc/login.defs. The umask command reads and sets the per-session value.

---

**Question 15**

An administrator runs ls -la /usr/bin/sudo and sees -rwsr-xr-x 1 root root. A security
auditor flags sudo as having an unnecessary SUID bit. Why would this claim be incorrect?

- A) The SUID bit on sudo is required because sudo must read /etc/shadow to verify passwords.
- B) The SUID bit on sudo is required because sudo needs to run as root to execute privileged commands on behalf of authorized users. Without it, sudo could not elevate privileges.
- C) The SUID bit is unnecessary because sudo uses PAM for authentication instead.
- D) The SUID bit on sudo is actually the SGID bit, which allows group-based elevation.

Correct Answer: B) The SUID bit on sudo is required because sudo needs to run as root to execute privileged commands on behalf of authorized users. Without it, sudo could not elevate privileges.

Distractor Analysis:

- Why A is incorrect: sudo's need for SUID is about running privileged commands, not specifically about reading /etc/shadow. The authentication step (reading shadow) is a secondary effect; the core requirement is running commands as root.
- Why C is incorrect: PAM handles the authentication mechanism (verifying the user's password) but PAM alone cannot grant root privileges to a process. The SUID bit is what allows sudo's process to gain root's UID after authentication succeeds.
- Why D is incorrect: The permission -rwsr-xr-x shows the s in the owner (user) execute position, which is definitively SUID, not SGID. SGID would appear in the group execute position (characters 5-7).

---

**Question 16**

A directory has the sticky bit set with permissions drwxrwxrwt. User alice creates a file
inside. User bob tries to delete alice's file while bob also has write access to the directory.
What happens?

- A) Bob can delete the file because the directory is world-writable.
- B) Bob cannot delete the file because the sticky bit prevents users from deleting or renaming files owned by other users in that directory.
- C) Bob can delete the file only if bob is a member of the directory's owning group.
- D) Bob receives a permission denied error when attempting any operation in the directory.

Correct Answer: B) Bob cannot delete the file because the sticky bit prevents users from deleting or renaming files owned by other users in that directory.

Distractor Analysis:

- Why A is incorrect: Normally, write permission on a directory would allow any user to delete files within it. The sticky bit specifically overrides this behavior, adding the restriction that only the file owner, the directory owner, or root can delete files.
- Why C is incorrect: The sticky bit protection applies regardless of group membership. Bob's inability to delete alice's file is based on file ownership, not group membership.
- Why D is incorrect: The sticky bit does not block all operations in the directory. Users can still create, read, and write their own files. Only deletion and renaming of other users' files is restricted.

---

**Question 17**

An administrator wants to change the owner of /var/app/config to the user appuser and
the group to appgroup in a single command. Which syntax is correct?

- A) chown appuser /var/app/config && chgrp appgroup /var/app/config
- B) chown appuser:appgroup /var/app/config
- C) chmod appuser:appgroup /var/app/config
- D) usermod -d /var/app/config appuser

Correct Answer: B) chown appuser:appgroup /var/app/config

Distractor Analysis:

- Why A is incorrect: While this two-command sequence produces the correct result, a single chown command with the user:group syntax is the standard, more efficient approach.
- Why C is incorrect: chmod changes permission bits (read, write, execute), not ownership. It does not accept user or group names as arguments.
- Why D is incorrect: usermod -d changes a user's home directory, not file ownership. It has no effect on /var/app/config's ownership.

---

**Question 18**

A Linux system's /etc/passwd file shows:

daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

What is the purpose of the x in the second field?

- A) It indicates the account is disabled.
- B) It is a placeholder showing that the actual password hash is stored in /etc/shadow, which is readable only by root.
- C) It means the account uses an X.509 certificate for authentication instead of a password.
- D) It indicates the account has no password and allows passwordless login.

Correct Answer: B) It is a placeholder showing that the actual password hash is stored in /etc/shadow, which is readable only by root.

Distractor Analysis:

- Why A is incorrect: A disabled account in /etc/shadow shows ! or !! in the password field. The x in /etc/passwd is a universal placeholder present for all accounts, active or inactive.
- Why C is incorrect: X.509 certificate authentication is not indicated by the x field. Certificate-based auth is handled by PAM modules and SSH configuration, not /etc/passwd fields.
- Why D is incorrect: An empty second field (no character between the colons) would historically indicate no password. The x means the password data has been shadowed to /etc/shadow.

---

**Question 19**

Which command removes a user account named testuser AND deletes their home directory and
mail spool?

- A) usermod -d /dev/null testuser
- B) passwd -l testuser && rm -rf /home/testuser
- C) userdel -r testuser
- D) deluser testuser --remove-home

Correct Answer: C) userdel -r testuser

Distractor Analysis:

- Why A is incorrect: usermod -d changes the home directory path in /etc/passwd to /dev/null but does not delete the account or any files. The account still exists.
- Why B is incorrect: passwd -l locks the account password but the account persists. While rm -rf /home/testuser removes the home directory manually, this two-step approach is less reliable than userdel -r which also cleans up the mail spool and /etc/passwd, /etc/shadow, /etc/group entries atomically.
- Why D is incorrect: deluser --remove-home is the Debian/Ubuntu-specific high-level wrapper. While it works on Ubuntu, userdel -r is the POSIX-standard command tested on CompTIA Linux+. The question tests knowledge of the standard userdel syntax.

---

**Question 20**

An administrator sets ACL permissions on a directory with the command:
setfacl -m u:webdev:rwx /var/www/html

Which statement best describes what this accomplishes?

- A) It replaces the standard Unix permission bits on /var/www/html with ACL permissions.
- B) It grants the user webdev read, write, and execute access to /var/www/html without modifying the file's standard owner, group, or others permission bits.
- C) It creates a new group called webdev with rwx access to the directory.
- D) It sets the default ACL so all new files created in /var/www/html will have rwx permissions for webdev.

Correct Answer: B) It grants the user webdev read, write, and execute access to /var/www/html without modifying the file's standard owner, group, or others permission bits.

Distractor Analysis:

- Why A is incorrect: ACLs extend standard permissions — they do not replace them. The standard permission bits (visible with ls -l) remain in place. ACL entries are additive.
- Why C is incorrect: setfacl does not create system groups. It applies access control entries to filesystem objects. Group creation requires groupadd.
- Why D is incorrect: The -m flag modifies the ACL for the named object only. To set a default ACL that applies to newly created files inside the directory, the d: prefix is required: setfacl -m d:u:webdev:rwx /var/www/html.
