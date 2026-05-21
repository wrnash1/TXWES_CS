# Quiz: Module 03 - File Permissions and Ownership
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator executes the command `chmod 644 confidential.txt`. What permissions does this command assign to the file?
A) The owner has read and write access, while the group and others have read-only access.
B) The owner has full access (read, write, execute), while the group has read-only access.
C) The owner has read-only access, while the group and others have read and write access.
D) The owner and the group have read and write access, while others have no access.
*   **Correct Answer:** A) The owner has read and write access, while the group and others have read-only access.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Full access is represented by a 7 (4+2+1=rwx). The first digit here is 6 (4+2=rw-), which is read and write only, not execute.
    *   *Why C is incorrect:* This describes a permission string like 466, where only the group and others can write — an insecure and non-standard configuration.
    *   *Why D is incorrect:* This describes octal 660 (rw-rw----), not 644. The digit 4 represents read-only (r--), not read-write.

---

---

**Question 2**
Which file in a standard Linux system contains the securely hashed passwords for local user accounts?
A) /etc/passwd
B) /etc/shadow
C) /etc/group
D) /var/log/auth.log
*   **Correct Answer:** B) /etc/shadow
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Historically passwords were stored in `/etc/passwd`, but modern systems store only an `x` placeholder there. The actual hashed passwords are in `/etc/shadow`, which is readable only by root.
    *   *Why C is incorrect:* `/etc/group` defines local groups and their member lists, not password hashes.
    *   *Why D is incorrect:* `/var/log/auth.log` records authentication events such as login attempts and sudo usage; it does not store password hashes.

---

---

**Question 3**
A systems administrator needs to restrict a configuration file so that only the file owner can read and write it, and no other users have any access at all. Which command achieves this?
A) chmod 600 config.conf
B) chmod 644 config.conf
C) chmod 755 config.conf
D) chmod 777 config.conf
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `chmod 644` gives the owner read+write but grants read access to the group and others (r--), which violates the requirement of no access for other users.
    *   *Why C is incorrect:* `chmod 755` gives the owner full access and grants read+execute to the group and others — far too permissive for a sensitive configuration file.
    *   *Why D is incorrect:* `chmod 777` grants read, write, and execute to everyone on the system, which is the least secure option possible.

---

**Question 4**
A Linux system has a `umask` value of `027`. When a standard user creates a new text file, what will the file's permissions be?
A) 640 (rw-r-----)
B) 644 (rw-r--r--)
C) 750 (rwxr-x---)
D) 600 (rw-------)
*   **Correct Answer:** A) 640 (rw-r-----)
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `644` results from a `umask` of `022` (666 − 022 = 644), not `027`.
    *   *Why C is incorrect:* `750` is a directory permission pattern. New regular files use a base of 666, not 777; even with `umask 027`, files do not receive execute bits.
    *   *Why D is incorrect:* `600` would result from a `umask` of `066` (666 − 066 = 600), not `027`.

---

**Question 5**
The `/usr/bin/passwd` command is owned by root but can be run by any user to change their own password. It must write to `/etc/shadow`, which is only readable by root. Which special permission bit enables this behavior?
A) The sticky bit set on `/usr/bin/passwd`
B) The SGID bit set on `/etc/shadow`
C) The SUID bit set on `/usr/bin/passwd`
D) The SGID bit set on `/usr/bin/passwd`
*   **Correct Answer:** C) The SUID bit set on `/usr/bin/passwd`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The sticky bit on a file is rarely used in modern Linux and does not cause a process to run with elevated privileges. The sticky bit is meaningful on directories (like `/tmp`), not on executables.
    *   *Why B is incorrect:* SGID on a file causes the process to run with the file's group privileges, not owner privileges. Setting SGID on `/etc/shadow` itself would not help `passwd` write to it as root.
    *   *Why D is incorrect:* SGID on an executable causes it to run with the file's group identity, not as the root user. `/usr/bin/passwd` needs to run as root (the owner), which requires SUID, not SGID.

