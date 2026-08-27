# Quiz: Module 08 — File System Permissions and Ownership

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. A score of 80 or higher is required to advance to Module 09.

---

**Question 1**

What is the octal representation of the permission string `rwxr-x---`?

A. 754

B. 750

C. 741

D. 640

**Correct Answer:** B

**Explanation:** Owner: rwx = 4+2+1 = 7. Group: r-x = 4+0+1 = 5. Others: --- = 0+0+0 = 0. Result: 750. Option A (754) incorrectly assigns 4 to others, which would be r--, not ---.

---

**Question 2**

A file has permissions `-rw-r-----` with owner `root` and group `apache`. User `bob` belongs to the `apache` group. What access does bob have to this file?

A. Read and write access

B. Read-only access

C. No access

D. Execute access only

**Correct Answer:** B

**Explanation:** Bob is a member of the `apache` group, so group permissions apply: `r--` = read-only. Bob is not the owner, so owner `rw-` does not apply. He is not "other" because he matched on the group check first.

---

**Question 3**

An administrator runs `chmod 2775 /shared/project`. What is the result?

A. The directory has SUID + rwxrwxr-x

B. The directory has SGID + rwxrwxr-x

C. The directory has sticky bit + rwxrwxr-x

D. The directory has SUID + SGID + rwxrwxr-x

**Correct Answer:** B

**Explanation:** The leading `2` sets SGID (2000). `775` = rwxrwxr-x. SUID would be `4`, sticky would be `1`. SUID+SGID would be `6`.

---

**Question 4**

A user's current `umask` is `027`. They create a new file with `touch newfile.txt`. What permissions will the file have?

A. 750 (rwxr-x---)

B. 640 (rw-r-----)

C. 644 (rw-r--r--)

D. 600 (rw-------)

**Correct Answer:** B

**Explanation:** Files default to 666 (rw-rw-rw-). Subtracting umask 027: 666 - 027 = 640. Owner keeps rw- (6-0=6), group gets r-- (6-2=4), others get --- (6-7=0, but umask only removes bits — others gets 0). Result: 640 = rw-r-----.

---

**Question 5**

An administrator sees this output from `ls -l`:

```
-rwsr-xr-x 1 root root 68208 Jan 15 2024 /usr/bin/passwd
```

What does the `s` in the owner execute position indicate?

A. The sticky bit is set on this file.

B. SGID is set, causing the file to run with the group's permissions.

C. SUID is set, causing the file to run with root's permissions regardless of who executes it.

D. The file is a symbolic link to another executable.

**Correct Answer:** C

**Explanation:** An `s` in the owner (user) execute position indicates SUID. When any user executes `/usr/bin/passwd`, it runs with root's effective UID, allowing it to write to `/etc/shadow`. Option A would show `t` in the others position. Option B would show `s` in the group execute position.

---

**Question 6**

An administrator runs `ls -l /etc/config.conf` and sees:

```
-rw-r--r--+ 1 admin admin 512 Jan 15 2024 /etc/config.conf
```

What does the `+` at the end of the permission string indicate?

A. The file has extended attributes set.

B. The file has an Access Control List (ACL) defined.

C. The file is immutable and cannot be deleted.

D. The file has a mandatory access control label.

**Correct Answer:** B

**Explanation:** A `+` appended to the permission string in `ls -l` output indicates that an ACL is defined on the file. Use `getfacl /etc/config.conf` to view the ACL entries. Extended attributes use the `e` notation; immutable files are a different concept entirely.

---

**Question 7**

A developer needs to set up a shared directory where all team members (in the `devteam` group) can create and delete their own files, but cannot delete each other's files. The directory should be accessible to everyone. Which command creates this configuration?

A. `chmod 755 /shared`

B. `chmod 777 /shared`

C. `chmod 1777 /shared`

D. `chmod 3777 /shared`

**Correct Answer:** C

**Explanation:** `1777` = sticky bit (1) + rwxrwxrwx (777). The sticky bit prevents users from deleting files they do not own. Option B (777) allows unrestricted deletion. Option D (3777) adds SGID which would change group ownership of new files — not required here.

---

**Question 8**

An administrator wants to grant user `auditor` read-only access to `/var/log/app.log` without changing the file's owner, group, or standard permissions. Which command accomplishes this?

A. `chmod o+r /var/log/app.log`

B. `chown auditor /var/log/app.log`

C. `setfacl -m u:auditor:r-- /var/log/app.log`

D. `usermod -aG $(stat -c %G /var/log/app.log) auditor`

**Correct Answer:** C

**Explanation:** `setfacl -m u:auditor:r--` adds an ACL entry for a specific named user without modifying existing ownership or standard permissions. Option A grants read to ALL others. Option B changes ownership. Option D adds auditor to the file's group, which may grant unintended access to other group-protected files.

---

**Question 9**

After creating a SGID directory `/projects/app` owned by `root:developers`, an engineer named `alice` (whose primary group is `staff`) creates a file in the directory. What will the file's group owner be?

A. `staff` (alice's primary group)

B. `root` (the directory's owner)

C. `developers` (inherited from the SGID directory)

D. `alice` (same as the file owner)

**Correct Answer:** C

**Explanation:** SGID on a directory causes all new files created within it to inherit the directory's group (`developers`) rather than the creator's primary group (`staff`). This is the core purpose of SGID on directories — enabling consistent group ownership for shared project spaces.

---

**Question 10**

An administrator needs to set permissions so that:
- The file owner can read and write
- The owning group can read only
- All others have no access

Which `chmod` command using symbolic notation achieves this?

A. `chmod u=rw,g=r,o= filename`

B. `chmod u+rw,g+r,o-rwx filename`

C. `chmod 640 filename`

D. Both A and C are correct.

**Correct Answer:** D

**Explanation:** Both A and C achieve the same result: owner rw- (6), group r-- (4), others --- (0) = mode 640. Option A uses symbolic `=` to set exactly. Option C uses octal 640. Option B uses `+` and `-` which are additive/subtractive and may not produce the exact result if the file currently has other bits set (e.g., execute).

---

---

**Question 11**

A shared `/tmp/uploads` directory has permissions `drwxrwxrwt`. A user named `carol` created the file `/tmp/uploads/report.txt`. Another user `dave` (who is not root) attempts to delete `report.txt` using `rm /tmp/uploads/report.txt`. What happens?

A. The deletion succeeds because `/tmp/uploads` is world-writable.

B. The deletion fails because the sticky bit prevents users from deleting files they do not own in that directory.

C. The deletion succeeds because dave has write permission on the directory.

D. The deletion fails because execute permission on the directory is required to delete files.

**Correct Answer:** B

**Explanation:** The sticky bit (`t` in the others execute position, octal 1000) on a directory restricts file deletion so that only the file owner, the directory owner, or root can remove a file — even if the directory is world-writable. Dave does not own `report.txt`, so the kernel denies the unlink operation.

---

**Question 12**

A user's `umask` is `022`. They create a new directory with `mkdir newdir`. What permissions will the directory have?

A. 644 (rw-r--r--)

B. 755 (rwxr-xr-x)

C. 777 (rwxrwxrwx)

D. 700 (rwx------)

**Correct Answer:** B

**Explanation:** Directories default to 777. Applying umask 022: 777 − 022 = 755. Owner gets rwx (7), group gets r-x (5), others get r-x (5). Files default to 666 (not 777), which is why the same umask produces 644 for files — directories need execute permission to be traversable.

---

**Question 13**

An administrator finds an executable `/usr/local/bin/backup` owned by `root:backupadm` with permissions `-rwxr-sr-x`. A member of the `backupadm` group runs the executable. Which statement correctly describes the effective privileges during execution?

A. The process runs with the user's UID and the `backupadm` GID — SGID has no effect on executables.

B. The process runs with root's UID because SUID is set in the owner position.

C. The process runs with the user's UID but with `backupadm` as the effective GID, regardless of the user's actual group memberships.

D. The process runs with root's UID and `backupadm` GID because both SUID and SGID are set.

**Correct Answer:** C

**Explanation:** The `s` in the group execute position indicates SGID on an executable. When any user runs this binary, the process adopts the file's group (`backupadm`) as its effective GID. SUID (owner `s`) is not set here — there is no `s` in the owner execute position — so the user's own UID is unchanged.

---

**Question 14**

An administrator runs `getfacl /data/project.conf` and sees the following output:

```
# file: data/project.conf
# owner: root
# group: ops
user::rw-
user:jenkins:r--
group::r--
mask::r--
other::---
```

What access does the user `jenkins` have to this file, and why does the `mask` entry matter?

A. `jenkins` has read-write access because ACL user entries always override the mask.

B. `jenkins` has read-only access; the mask limits the effective permissions of all named users and named groups — `jenkins:r--` ANDed with `mask::r--` yields `r--`.

C. `jenkins` has no access because the `other::---` entry applies to all non-owner users not explicitly listed.

D. `jenkins` has read-only access regardless of the mask because named user ACL entries are never affected by the mask.

**Correct Answer:** B

**Explanation:** The ACL mask defines the maximum effective permission for all named users, named groups, and the owning group. Effective permission = (ACL entry) AND (mask). Here `jenkins:r--` AND `mask::r--` = `r--`. If the mask were `---`, jenkins would have no effective access even with `r--` in their entry. The `other` entry only applies to users with no matching owner, named-user, group, or named-group ACL entry.

---

**Question 15**

An administrator needs to recursively change ownership of `/var/www/html` and all its contents to user `www-data` and group `www-data`. Which command is correct?

A. `chown www-data /var/www/html`

B. `chown -R www-data:www-data /var/www/html`

C. `chmod -R www-data:www-data /var/www/html`

D. `chown www-data:www-data /var/www/html/*`

**Correct Answer:** B

**Explanation:** `chown -R user:group path` recursively changes the owner and group of the target directory and all files and subdirectories within it. Option A changes only the top-level directory and omits the group. Option C uses `chmod`, which sets permissions, not ownership. Option D uses a glob (`*`) that misses hidden files and does not descend into nested subdirectories.

---

**Question 16**

An administrator wants to find all files under `/usr/bin` that have the SUID bit set. Which `find` command is correct?

A. `find /usr/bin -perm 4000`

B. `find /usr/bin -perm /4000`

C. `find /usr/bin -perm -4000`

D. `find /usr/bin -type f -perm -4000`

**Correct Answer:** D

**Explanation:** `-perm -4000` means "match if the SUID bit is set, regardless of other permission bits" (bitwise AND). Adding `-type f` restricts results to regular files, excluding directories that may also have SUID (rare but possible). Option A (`-perm 4000`) requires an exact permission match of `---S------` — files with any additional bits set would be excluded. Option B uses `/` (OR mode) which is equivalent to `-` for a single bit, so it works but omits `-type f`. Option C is functionally correct but also omits `-type f`, which is best practice.

---

**Question 17**

A file currently has permissions `rw-rw-rw-` (666). An administrator runs `chmod g-w,o-rw filename`. What is the resulting octal permission value?

A. 664

B. 640

C. 600

D. 620

**Correct Answer:** B

**Explanation:** Starting from `rw-rw-rw-` (666): `g-w` removes write from the group (`rw-` → `r--`), and `o-rw` removes both read and write from others (`rw-` → `---`). Result: owner `rw-` (6), group `r--` (4), others `---` (0) = **640**.

---

**Question 18**

A directory `/shared/docs` has permissions `drwxrwxr-x` with group `writers`. When a new file is created inside by a `writers` group member, the file has permissions `rw-rw-r--`. A new project requirement states that all files created in `/shared/docs` must automatically be owned by the `writers` group, regardless of each user's primary group. No changes to individual user accounts should be required. What single command achieves this?

A. `chmod 3775 /shared/docs`

B. `chmod 2775 /shared/docs`

C. `chmod 1775 /shared/docs`

D. `setfacl -d -m g:writers:rwx /shared/docs`

**Correct Answer:** B

**Explanation:** `chmod 2775` sets the SGID bit (2) on the directory. SGID on a directory causes all newly created files and subdirectories to inherit the directory's group (`writers`) instead of each creator's primary group. Option A (3775) adds both SGID and sticky bit — sticky bit is unnecessary here and prevents users from deleting each other's files, which is not a stated requirement. Option C (1775) sets only the sticky bit, which restricts deletion but does not affect group inheritance. Option D sets a default ACL entry for group permissions but does not change the owning group of new files.

---

**Question 19**

A non-root user `alice` attempts to read a file owned by `root` with permissions `-rw-------` (600). The read attempt fails with "Permission denied." Alice then runs `sudo cat /etc/secretfile` successfully. Which statement best explains why root's normal file permission rules do not apply when using `sudo`?

A. `sudo` changes the file's permissions temporarily to allow the read, then restores them after the command exits.

B. `sudo` executes the command with root's effective UID (0); the kernel bypasses DAC permission checks for UID 0 on read and write operations.

C. `sudo` grants the user permanent root privileges for the duration of the session after the first successful authentication.

D. Root can read any file because the sticky bit on `/etc` is automatically cleared when root accesses files.

**Correct Answer:** B

**Explanation:** Linux's Discretionary Access Control (DAC) kernel check grants UID 0 (root) unconditional read and write access to all files regardless of permission bits — only execute permission is still checked for root on non-SUID files. `sudo` launches a new process with effective UID 0 for the duration of that single command only; it does not modify file permissions, does not grant persistent root login, and the sticky bit on directories has nothing to do with per-file read access.

---

**Question 20**

An administrator runs `chmod o-rx /projects/reports`. A user `eve` (who is not the owner and not in the owning group) attempts to run `ls /projects/reports`. What happens, and which missing permission causes it?

A. The listing succeeds because read permission on the directory is sufficient for `ls`.

B. The listing fails; without execute (x) permission on the directory, eve cannot traverse into it to read its contents — even if read permission were granted separately.

C. The listing fails; without read (r) permission on the directory, eve cannot see the filenames, but execute permission alone would allow traversal.

D. The listing fails because both read and execute permission on the directory have been removed; execute is required to enter the directory and read is required to list filenames.

**Correct Answer:** D

**Explanation:** `chmod o-rx` removes both read and execute from the "others" category. On a directory: execute (`x`) permission is the "search" bit — required to traverse into the directory or access any path through it. Read (`r`) permission is required to obtain a listing of filenames with `ls`. Removing both means eve can neither enter the directory nor list its contents. Option B is partially correct about execute but ignores that read was also removed. Option C correctly describes the roles of each bit but incorrectly implies only read was removed.

---

**Answer Key Summary**

| Question | Answer |
|---|---|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | C |
| 8 | C |
| 9 | C |
| 10 | D |
| 11 | B |
| 12 | B |
| 13 | C |
| 14 | B |
| 15 | B |
| 16 | D |
| 17 | B |
| 18 | B |
| 19 | B |
| 20 | D |
