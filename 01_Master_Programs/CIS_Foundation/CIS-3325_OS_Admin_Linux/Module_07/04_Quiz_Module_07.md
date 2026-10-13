# Quiz: Module 07 — User and Group Administration

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. A score of 80 or higher is required to advance to Module 08.

---

**Question 1**

A Linux administrator needs to create a new user named `devuser` with a home directory, the bash shell, and membership in the `developers` group as a supplementary group. Which command accomplishes all of this correctly?

A. `useradd -d /home/devuser -s /bin/bash -G developers devuser`

B. `useradd -m -s /bin/bash -G developers devuser`

C. `useradd -m -s /bin/bash -g developers devuser`

D. `adduser -home /home/devuser -shell bash -group developers devuser`

**Correct Answer:** B

**Explanation:** Option B uses `-m` to create the home directory, `-s` to set the shell, and `-G` to assign `developers` as a supplementary group. Option A is missing `-m` (required on Debian systems and good practice everywhere). Option C uses `-g` which sets the primary group, not supplementary. Option D uses invalid flag syntax.

---

**Question 2**

An administrator examines `/etc/shadow` and finds this entry for a user account:

```
jdoe:!$6$salt$hash:19500:0:99999:7:::
```

What does the `!` at the beginning of the password field indicate?

A. The account has no password set.

B. The account password uses an incompatible hashing algorithm.

C. The account is locked.

D. The account requires a password change at next login.

**Correct Answer:** C

**Explanation:** A `!` (or `!!`) prepended to the password hash in `/etc/shadow` indicates the account is locked. This is the result of `passwd -l username` or `usermod -L username`. Option A would show an empty field or `*`. Option D would show the last-changed date field set to 0.

---

**Question 3**

A junior administrator needs to add user `alice` to the `docker` group without removing her from any other groups. Which command is correct?

A. `usermod -G docker alice`

B. `usermod -g docker alice`

C. `usermod -aG docker alice`

D. `groupmod -a alice docker`

**Correct Answer:** C

**Explanation:** `usermod -aG` appends to the supplementary groups list. Without `-a`, the `-G` flag replaces all existing supplementary groups. Option B changes the primary group. Option D is not a valid `groupmod` syntax for adding members.

---

**Question 4**

Which file should NEVER be edited directly with a standard text editor?

A. `/etc/passwd`

B. `/etc/group`

C. `/etc/sudoers`

D. `/etc/shadow`

**Correct Answer:** C

**Explanation:** `/etc/sudoers` must only be edited with `visudo`, which locks the file and validates syntax before saving. A syntax error in `/etc/sudoers` can make sudo completely unusable, potentially locking administrators out. The other files can technically be edited directly, though it is safer to use the appropriate tools.

---

**Question 5**

An administrator wants to force user `newstaff` to change their password at their very first login. Which command accomplishes this?

A. `passwd -e newstaff`

B. `chage -d 0 newstaff`

C. `usermod --expire-password newstaff`

D. Both A and B are correct.

**Correct Answer:** D

**Explanation:** Both `passwd -e newstaff` and `chage -d 0 newstaff` expire the password immediately, forcing a change at next login. `passwd -e` sets the expiration flag; `chage -d 0` sets the last-changed date to epoch day 0, which is treated as immediately expired. Option C is not a valid flag.

---

**Question 6**

An administrator is reviewing the `/etc/passwd` file and sees this line:

```
webserver:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

What is the purpose of `/usr/sbin/nologin` in this entry?

A. It is a placeholder indicating the account has no shell configured.

B. It prevents interactive login for this service account.

C. It causes the account to be automatically locked after creation.

D. It is an error; service accounts should use `/bin/false`.

**Correct Answer:** B

**Explanation:** `/usr/sbin/nologin` (or `/sbin/nologin`) prevents interactive logins by immediately exiting with a message. This is the correct way to configure service accounts. Both `/sbin/nologin` and `/bin/false` are acceptable for this purpose, making option D incorrect.

---

**Question 7**

Which of the following sudoers rules allows members of the `webteam` group to restart the Apache service without entering a password?

A. `webteam ALL=(ALL) /bin/systemctl restart httpd`

B. `%webteam ALL=(ALL) NOPASSWD: /bin/systemctl restart httpd`

C. `@webteam ALL=(root) NOPASSWD: /bin/systemctl restart httpd`

D. `+webteam ALL=(ALL) /bin/systemctl restart httpd NOPASSWD`

**Correct Answer:** B

**Explanation:** In sudoers syntax, group names are prefixed with `%`. The `NOPASSWD:` tag must precede the command list. Option A is missing the `%` prefix and `NOPASSWD`. Option C uses an incorrect `@` prefix. Option D places `NOPASSWD` at the wrong position.

---

**Question 8**

In a PAM configuration file, a module is marked with the `requisite` control flag. What happens if this module fails?

A. Evaluation continues with the next module in the stack.

B. The failure is logged but the user is still permitted access.

C. Evaluation stops immediately and access is denied.

D. The module is skipped and results are ignored.

**Correct Answer:** C

**Explanation:** The `requisite` control flag causes immediate failure — if the module fails, PAM stops processing immediately and returns failure. This is different from `required`, which records the failure but continues evaluating remaining modules. `optional` ignores results. There is no built-in "log but permit" control flag.

---

**Question 9**

An administrator deletes user `olddev` without using the `-r` flag. What is the most likely consequence, and what command would help identify it?

A. The user's processes will be killed; use `ps aux | grep olddev`

B. The user's home directory and files remain, owned by the old UID; use `find / -nouser`

C. All files owned by the user are automatically deleted; no cleanup is needed

D. The account is moved to an archive in `/etc/passwd.d/`

**Correct Answer:** B

**Explanation:** Without `-r`, `userdel` removes the account from `/etc/passwd` and `/etc/shadow` but leaves the home directory and any files intact. These files become "orphaned" — owned by a UID with no corresponding account entry. `find / -nouser` locates files with no valid owner. Option C is incorrect; Linux does not auto-delete files. Option D does not exist.

---

**Question 10**

An administrator needs to configure a password policy requiring users to change passwords every 60 days, with a 10-day warning and a minimum of 2 days before they can change it again. Which `chage` command is correct for user `tsmith`?

A. `chage -M 60 -W 10 -m 2 tsmith`

B. `chage -x 60 -w 10 -n 2 tsmith`

C. `chage --max 60 --warn 10 --min 2 tsmith`

D. `passwd -x 60 -w 10 -n 2 tsmith`

**Correct Answer:** A

**Explanation:** `chage -M` sets maximum days (60), `-W` sets warning days (10), and `-m` sets minimum days (2). Option B uses lowercase flags that `chage` does not support (those are `passwd` flags). Option C shows long-option syntax that does not match `chage`'s actual options. Option D uses `passwd` which does support `-x`, `-w`, and `-n`, but only options A correctly uses `chage` with the right flag cases.

---

### Question 11 (5 points)

An administrator runs `id jsmith` and gets the output: `uid=1001(jsmith) gid=1001(jsmith) groups=1001(jsmith),2000(developers),2002(devops)`. Which group is jsmith's primary group?

A. `developers`
B. `devops`
C. `jsmith`
D. The first group listed in `/etc/group`

**Correct Answer:** C

**Distractor Analysis:**

- **A** is incorrect. `developers` (GID 2000) is a supplementary group — it appears after the `groups=` section along with other supplementary groups.
- **B** is incorrect. `devops` (GID 2002) is also a supplementary group.
- **C** is correct. In `id` output, the `gid=` field identifies the primary group. `gid=1001(jsmith)` means the primary group is `jsmith`. On Linux, each user account typically has a private primary group with the same name as the user.
- **D** is incorrect. Primary group is determined by field 4 of `/etc/passwd`, not by position in `/etc/group`.

---

### Question 12 (5 points)

What is the purpose of the `/etc/skel` directory?

A. It stores skeleton (compressed) copies of user home directories for backup.
B. It contains template files that are copied into a new user's home directory when the account is created with `-m`.
C. It holds default system-wide shell configuration that cannot be overridden by users.
D. It is the home directory for the `skel` system service account.

**Correct Answer:** B

**Distractor Analysis:**

- **A** is incorrect. `/etc/skel` does not contain compressed or archived home directories. The name "skel" comes from "skeleton" meaning template, not compressed backup.
- **B** is correct. When `useradd -m` creates a home directory, the contents of `/etc/skel` are copied into it. Administrators can add default `.bashrc`, `.profile`, README files, or configuration templates to `/etc/skel` to ensure all new users start with a standard environment.
- **C** is incorrect. While files like `.bashrc` in `/etc/skel` do influence shell behavior, users can override them. `/etc/skel` files are copied once at account creation — they are not enforced persistently.
- **D** is incorrect. There is no `skel` service account. `/etc/skel` is an administrative directory, not a home directory.

---

### Question 13 (5 points)

An administrator needs to rename user `jdoe` to `johndoe` and move their home directory from `/home/jdoe` to `/home/johndoe`. Which command accomplishes both tasks?

A. `usermod -l johndoe jdoe`
B. `usermod -l johndoe -d /home/johndoe jdoe`
C. `usermod -l johndoe -d /home/johndoe -m jdoe`
D. `mv /home/jdoe /home/johndoe && usermod -l johndoe jdoe`

**Correct Answer:** C

**Distractor Analysis:**

- **A** is incorrect. `-l` alone changes the login name but does not update the home directory path. The home directory entry in `/etc/passwd` would still show `/home/jdoe`.
- **B** is incorrect. `-d` updates the home directory path in `/etc/passwd` but does not physically move the directory contents. The new path would be recorded but the files would still be at `/home/jdoe`.
- **C** is correct. `-l johndoe` renames the account, `-d /home/johndoe` sets the new home directory path in `/etc/passwd`, and `-m` moves (renames) the actual directory on disk from the old path to the new path. All three flags together complete the rename.
- **D** is incorrect as the best answer. While manually moving the directory and then renaming the account would work technically, it is not atomic and the order matters. Using `usermod -m` is the correct single-command approach that ensures consistency.

---

### Question 14 (5 points)

Which command lists all of the password aging information for user `mlopez` including last changed date, expiration, and warning period?

A. `passwd -S mlopez`
B. `chage -l mlopez`
C. `grep mlopez /etc/shadow`
D. `id -a mlopez`

**Correct Answer:** B

**Distractor Analysis:**

- **A** is incorrect. `passwd -S mlopez` shows a brief one-line status (locked, password set, or no password) and the current password age settings. It is much less readable than `chage -l` and does not show the friendly date format.
- **B** is correct. `chage -l` (lowercase L for "list") displays all password aging information in a human-readable format: last changed date, password expiration date, password inactive date, account expiration date, and warning days.
- **C** is partially correct but requires root access and returns raw epoch-day numbers rather than human-readable dates. `chage -l` is the appropriate tool for readable aging information.
- **D** is incorrect. `id` shows UID, GID, and group memberships. It has no flags for password aging and `-a` is not a valid `id` option.

---

### Question 15 (5 points)

An administrator wants to prevent root from logging in directly via SSH without disabling the root account. Which configuration file should be modified?

A. `/etc/passwd` — change root's shell to `/sbin/nologin`
B. `/etc/shadow` — prepend `!` to root's password hash
C. `/etc/ssh/sshd_config` — set `PermitRootLogin no`
D. `/etc/security/access.conf` — add a deny rule for root

**Correct Answer:** C

**Distractor Analysis:**

- **A** is incorrect and dangerous. Changing root's shell to `/sbin/nologin` would prevent local console root login as well, not just SSH. This could lock administrators out of emergency console recovery.
- **B** is incorrect and dangerous. Locking the root account by prepending `!` to its hash would break all forms of root authentication including `su -` from sudoers. This is far too broad and could leave no escalation path.
- **C** is correct. The `PermitRootLogin no` directive in `/etc/ssh/sshd_config` specifically prevents SSH root login while leaving all other authentication methods (console, `su -`) unaffected. After changing the file, `sudo systemctl reload sshd` applies the setting.
- **D** is partially valid as a PAM-based approach but is more complex and less standard than the SSH configuration option. For the Linux+ exam and standard practice, the SSH config file is the correct answer for SSH-specific restrictions.

---

### Question 16 (5 points)

An administrator discovers a user account with UID 0 that is not the `root` account. What is the security implication?

A. It is normal — UID 0 can be assigned to multiple accounts safely.
B. The account has the same privileges as root regardless of its username.
C. The account can only read root-owned files, not write to them.
D. The kernel blocks UID 0 accounts with non-root usernames automatically.

**Correct Answer:** B

**Distractor Analysis:**

- **A** is incorrect. Having multiple UID 0 accounts is a serious security finding — it means there are multiple accounts with full root privileges. This should never be present except in very specific documented circumstances.
- **B** is correct. The Linux kernel makes access decisions based on UIDs, not usernames. Any process running as UID 0 has superuser privileges, regardless of whether the account is named `root`, `toor`, or anything else. This is a common backdoor technique.
- **C** is incorrect. UID 0 grants full read AND write access to all files. There is no partial privilege for UID 0.
- **D** is incorrect. The kernel does not block UID 0 from being assigned to accounts with non-root names. The system administrator can create UID 0 accounts. This is why security auditing tools specifically check for this condition.

---

### Question 17 (5 points)

What does the `getent passwd` command retrieve that `cat /etc/passwd` does not?

A. It decrypts the password hashes for display.
B. It shows only accounts that have logged in recently.
C. It queries all configured Name Service Switch (NSS) sources, including LDAP or NIS entries not in local files.
D. It filters out system accounts and shows only regular users.

**Correct Answer:** C

**Distractor Analysis:**

- **A** is incorrect. Neither command decrypts password hashes. Hashes are one-way and cannot be reversed. `getent` has no special access to hash contents.
- **B** is incorrect. Neither `getent passwd` nor `cat /etc/passwd` filters by login recency. Login history is tracked in `/var/log/wtmp` and shown with the `last` command.
- **C** is correct. `getent` uses the Name Service Switch (NSS) configuration in `/etc/nsswitch.conf` to query all configured identity sources. In enterprise environments with LDAP, Active Directory, or NIS integration, `cat /etc/passwd` shows only local accounts while `getent passwd` shows all accounts from all sources.
- **D** is incorrect. `getent passwd` shows all accounts from all sources, including system accounts. It does not filter by UID range. To filter regular users, you would pipe through `awk -F: '$3 >= 1000'`.

---

### Question 18 (5 points)

An administrator runs `sudo visudo` and accidentally introduces a syntax error in `/etc/sudoers`. What happens when they try to save and exit?

A. The file is saved with the error and sudo stops working immediately.
B. `visudo` detects the syntax error, warns the administrator, and offers options to re-edit or quit without saving.
C. `visudo` automatically corrects common syntax errors before saving.
D. The file is saved to a `.bak` backup and then overwritten, preserving the previous working configuration.

**Correct Answer:** B

**Distractor Analysis:**

- **A** is incorrect. This is specifically what `visudo` is designed to prevent. Direct editing with a regular text editor would create this dangerous situation — which is why `visudo` exists.
- **B** is correct. Before writing the file, `visudo` parses the content for syntax errors. If errors are found, it reports them and presents three options: return to the editor to fix the error, quit without saving (preserving the current working sudoers), or save despite the error (very strongly discouraged).
- **C** is incorrect. `visudo` does not automatically correct errors. It validates and warns but requires the administrator to manually fix any problems.
- **D** is incorrect. `visudo` does not create a `.bak` backup as part of its standard operation. The protection it provides is refusing to save invalid configurations, not backup creation.

---

### Question 19 (5 points)

Which PAM module enforces resource limits such as maximum open files, maximum processes, and memory limits for user sessions?

A. `pam_unix.so`
B. `pam_limits.so`
C. `pam_deny.so`
D. `pam_pwquality.so`

**Correct Answer:** B

**Distractor Analysis:**

- **A** is incorrect. `pam_unix.so` handles standard Unix password authentication against `/etc/shadow`. It does not manage resource limits.
- **B** is correct. `pam_limits.so` reads `/etc/security/limits.conf` (and files in `/etc/security/limits.d/`) and applies resource limits to user sessions when they log in. Common limits include `nofile` (open file descriptors), `nproc` (number of processes), `memlock`, and `core` (core dump size).
- **C** is incorrect. `pam_deny.so` unconditionally denies access — it is used to block a service entirely or as a catch-all denial rule. It has no resource limiting capability.
- **D** is incorrect. `pam_pwquality.so` enforces password complexity rules (minimum length, character classes, dictionary checks) during password changes. It is not related to session resource limits.

---

### Question 20 (5 points)

An administrator runs `find / -nouser 2>/dev/null` on a system. What is the administrator looking for?

A. Files with world-writable permissions that have no owner username assigned.
B. Files that have no associated user in the NSS database — typically orphaned files from deleted accounts.
C. Files that are owned by the `nouser` service account.
D. Files where the permission field shows no user read access.

**Correct Answer:** B

**Distractor Analysis:**

- **A** is incorrect. World-writable files are found with `find / -perm -002`. The `-nouser` predicate has nothing to do with file permissions.
- **B** is correct. `-nouser` matches files whose UID has no corresponding entry in the user database (as resolved via NSS). When a user account is deleted without using the `-r` flag, their files remain on disk with the old UID. If that UID is later assigned to a new user, those old files become that new user's property — a potential security risk.
- **C** is incorrect. There is no `nouser` service account on standard Linux systems. The `-nouser` option in `find` is a search predicate, not a username.
- **D** is incorrect. File permission read access for the owner field is found using `-perm` predicates. `-nouser` exclusively tests whether the file's owner UID resolves to a valid account in the user database.

---

## Answer Key

| Question | Answer |
|---|---|
| 1 | B |
| 2 | C |
| 3 | C |
| 4 | C |
| 5 | D |
| 6 | B |
| 7 | B |
| 8 | C |
| 9 | B |
| 10 | A |
| 11 | C |
| 12 | B |
| 13 | C |
| 14 | B |
| 15 | C |
| 16 | B |
| 17 | C |
| 18 | B |
| 19 | B |
| 20 | B |
