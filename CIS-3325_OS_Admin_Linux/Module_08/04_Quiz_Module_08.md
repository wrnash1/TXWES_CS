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
