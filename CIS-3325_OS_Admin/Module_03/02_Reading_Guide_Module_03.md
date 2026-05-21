# Reading Guide: Module 03 - File Permissions and Ownership
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 03 – File Permissions and Ownership**! This week covers the Linux discretionary access control model: how every file and directory carries permission bits and ownership metadata, how to read and change them, and how the `umask` shapes defaults at file creation time. Permission management is one of the most heavily tested topics on the CompTIA Linux+ XK0-005 exam.

As you work through this material you will learn to decode octal and symbolic permission notation, apply `chmod` and `chown` correctly, and understand the special permission bits (SUID, SGID, sticky bit) that appear in both lab scenarios and exam questions.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Permission Triplets (rwx)**: Every file has three permission sets — owner (user), group, and others — each containing read (r=4), write (w=2), and execute (x=1) bits. The octal value for each set is the sum of its active bits (e.g., `rwx`=7, `rw-`=6, `r--`=4). The command `ls -l` displays them as a 10-character string like `-rwxr-xr--`.
*   **`chmod`**: Changes file or directory permission bits. Accepts both symbolic notation (`chmod u+x script.sh`, `chmod g-w file`) and octal notation (`chmod 644 file`, `chmod 755 dir`). With `-R` it applies recursively. On the exam, always translate the octal digits individually: `chmod 644` = owner rw- (6), group r-- (4), others r-- (4).
*   **`chown`**: Changes the user owner and/or group owner of a file. Syntax: `chown user:group filename`. To change only the group, use `chown :groupname file` or `chgrp groupname file`. Requires root or sudo for files you do not own.
*   **`umask`**: A four-digit octal mask subtracted from the system default permissions when a new file (default 666) or directory (default 777) is created. A `umask` of `022` produces files with `644` (666 − 022) and directories with `755` (777 − 022). Set persistently in `~/.bashrc` or `/etc/profile`.
*   **SUID (Set User ID)**: When set on an executable, the process runs with the file owner's privileges rather than the caller's. Represented as `s` in the owner execute field (`-rwsr-xr-x`). The classic example is `/usr/bin/passwd`, which must write to `/etc/shadow` (root-owned) on behalf of any user.
*   **Sticky Bit**: When set on a directory (shown as `t` in the others execute field), only the file's owner, the directory's owner, or root can delete or rename files within it. Used on `/tmp` to prevent users from deleting each other's temporary files.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Permissions fall under Linux+ Domain 1.0 (System Management) and Domain 2.0 (Security). Expect 5–8 questions involving `chmod`, `chown`, `umask`, and special bits.
*   **Octal math is essential:** Practice converting `chmod 755`, `chmod 644`, `chmod 600`, and `chmod 777` by hand. The exam presents symbolic `ls -l` output and asks what octal command produced it, and vice versa.
*   **SUID/SGID trap:** Questions describe a script that must run as root regardless of who executes it — the answer is SUID, not `sudo`. Questions about a shared group directory where new files should inherit the group — the answer is SGID on the directory, not `chown -R`.
*   **umask direction:** A common trap asks what permissions a file gets with `umask 027`. Subtract: 666 − 027 = 640 (owner rw-, group r--, others ---). Remember umask subtracts from the *default*, not the requested value.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers permissions in depth in chapters 9–10. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of `chmod`, `chown`, and `umask` in live terminal sessions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 9–10 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), which cover permissions, ownership, and process management as they relate to access control.
*   **Required Video:** Watch the permissions and ownership videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free playlist demonstrating real administrative scenarios involving `chmod`, `chown`, and special bits.

---

### Lab & Command Integration
In this week's hands-on lab you will create files with various permissions using `chmod` in both symbolic and octal form, change file ownership with `chown`, test `umask` values, and identify SUID/SGID files on the system with `find / -perm /4000`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 9–10 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the permissions videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
