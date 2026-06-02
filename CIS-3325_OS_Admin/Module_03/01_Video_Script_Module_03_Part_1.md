# Video Script: Module 03 - File Permissions and Ownership (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 03. We have learned to navigate the filesystem and work with files. Now we ask
the fundamental security question: who is allowed to do what with each file? File permissions are
the primary access control mechanism in Linux. They determine whether a user can read a
configuration file, execute a script, or write to a directory. Get them wrong and you either lock
legitimate users out or leave sensitive data exposed.

By the end of both parts you will be able to read any ls -l permission string, calculate octal
permission values, use chmod and chown correctly, understand umask, and explain the special
permission bits that appear on every Linux+ exam.

---

### Section 1: The Three Permission Layers

Every file and directory in Linux has three permission sets associated with three types of users.

The owner (also called the user, abbreviated u) is the account that created the file or was
assigned ownership with chown. The owner has the highest priority when permissions are evaluated.

The group (abbreviated g) is a named collection of user accounts. When a file's group is set to
"developers," every user in the developers group gets the group permissions for that file.

Others (abbreviated o) means everyone else - any user on the system who is neither the owner nor
a member of the file's assigned group. Others permissions are the most restrictive layer.

[SHOW TERMINAL]

```bash
ls -l /etc/passwd
```

You should see output like:

```
-rw-r--r-- 1 root root 2345 Jan 15 10:30 /etc/passwd
```

Let us decode this string character by character.

The first character: dash (-) means it is a regular file. A d here would mean directory. An l
would mean symbolic link.

Characters 2-4: rw- - These are the owner permissions. The owner (root) can read (r) and write
(w) but not execute (- where x would be).

Characters 5-7: r-- - These are the group permissions. The group (root) can only read. No write,
no execute.

Characters 8-10: r-- - These are the others permissions. Everyone else can only read. No write,
no execute.

This makes sense: /etc/passwd is a system file. Everyone needs to read it (programs look up
user accounts). But only root should be able to modify it.

---

### Section 2: The Octal Permission System

The exam heavily tests octal notation. Here is the math.

Each permission bit has a value:
- Read (r) = 4
- Write (w) = 2
- Execute (x) = 1

To calculate the octal value for a permission set, add the values of active bits.

rwx = 4 + 2 + 1 = 7
rw- = 4 + 2 + 0 = 6
r-x = 4 + 0 + 1 = 5
r-- = 4 + 0 + 0 = 4
--- = 0 + 0 + 0 = 0

A three-digit octal like 644 represents:
- First digit (6): owner permissions = rw-
- Second digit (4): group permissions = r--
- Third digit (4): others permissions = r--

So chmod 644 file.txt gives the owner read+write and gives group and others read-only.

[SHOW TERMINAL]

```bash
chmod 644 /etc/passwd
ls -l /etc/passwd
```

The ls output now shows -rw-r--r-- which matches our calculation.

Let us do another one. chmod 755:
- 7 = rwx (owner: full control)
- 5 = r-x (group: read and execute)
- 5 = r-x (others: read and execute)

This is the standard permission for executable scripts and most directories.

chmod 600:
- 6 = rw- (owner: read and write)
- 0 = --- (group: no access)
- 0 = --- (others: no access)

This is used for private SSH keys and sensitive configuration files.

chmod 777:
- 7 = rwx (everyone: full control)

chmod 777 is almost never appropriate on a production system. It means anyone on the system
can read, modify, or execute the file.

---

### Section 3: Execute Permission and Why It Matters

Execute permission means something different for files and directories.

For a regular file, the execute bit allows running the file as a program or script. Without x,
you cannot run a script no matter how it is written. This is a security feature: simply copying
a file to a server does not make it executable.

[SHOW TERMINAL]

```bash
touch myscript.sh
echo '#!/bin/bash' > myscript.sh
echo 'echo Hello World' >> myscript.sh
ls -l myscript.sh
./myscript.sh
```

You get "Permission denied" because the execute bit is not set.

```bash
chmod +x myscript.sh
ls -l myscript.sh
./myscript.sh
```

Now it runs. The +x added execute permission for all three layers (user, group, others). A more
precise way is chmod u+x which adds execute only for the owner.

For a directory, the execute bit is called the search bit. Without execute on a directory, you
cannot cd into it or access any files inside it, even if you have read permission on the
directory itself.

---

### Section 4: Symbolic vs Octal chmod Notation

chmod accepts both octal notation (numbers) and symbolic notation (letters).

Symbolic notation syntax: chmod [who][operator][permissions] file

Who: u (user/owner), g (group), o (others), a (all three)
Operator: + (add), - (remove), = (set exactly)
Permissions: r, w, x

[SHOW TERMINAL]

```bash
chmod u+x script.sh
```

Adds execute permission for the owner only.

```bash
chmod g-w sensitive.conf
```

Removes write permission from the group.

```bash
chmod o= sensitive.conf
```

Sets others permissions to nothing (removes all).

```bash
chmod a+r public.txt
```

Adds read permission for everyone (all).

Symbolic notation is useful when you want to add or remove a single bit without knowing or
changing the other bits. Octal notation is precise and sets all nine bits at once.

---

### Section 5: Changing Ownership with chown and chgrp

[SHOW TERMINAL]

```bash
sudo chown alice file.txt
```

Changes the owner of file.txt to alice. Group ownership is unchanged.

```bash
sudo chown alice:developers file.txt
```

Changes both owner (alice) and group (developers) simultaneously.

```bash
sudo chown :developers file.txt
```

Changes only the group to developers. Owner is unchanged.

```bash
sudo chgrp developers file.txt
```

chgrp is an alternative command for changing group ownership only.

```bash
sudo chown -R labadmin:labadmin /home/labadmin/
```

The -R flag applies the ownership change recursively to all files and directories inside.
Use this carefully - applying it to the wrong path can break system-wide file ownership.

```bash
ls -l file.txt
```

After all changes, ls -l shows the current owner and group.

---

### Section 6: The umask - Default Permissions at Creation

When you create a new file or directory, what permissions does it get by default? That is
controlled by umask.

[SHOW TERMINAL]

```bash
umask
```

On Ubuntu, the default umask for regular users is 0022.

The umask is subtracted from the maximum default permissions:
- Files default maximum: 666 (rw-rw-rw-)
- Directories default maximum: 777 (rwxrwxrwx)

With umask 022:
- Files: 666 - 022 = 644 (rw-r--r--)
- Directories: 777 - 022 = 755 (rwxr-xr-x)

```bash
touch testfile.txt
mkdir testdir
ls -la
```

The new file has 644 and the new directory has 755, exactly as predicted by umask 022.

```bash
umask 027
touch private.txt
mkdir privatedir
ls -la
```

With umask 027:
- Files: 666 - 027 = 640 (rw-r-----)
- Directories: 777 - 027 = 750 (rwxr-x---)

The group can still read but others have zero access. This is a common security-hardened umask.

To make a umask permanent, add it to ~/.bashrc or /etc/profile.

---

### Section 7: The /etc/passwd and /etc/shadow Files

These two files are critical to understanding Linux permission security.

[SHOW TERMINAL]

```bash
cat /etc/passwd | head -5
```

Each line has seven colon-separated fields:
username:x:UID:GID:GECOS:home_directory:login_shell

The x in field 2 is a placeholder. Historically, passwords were stored here in plain text (yes,
really). Modern systems moved passwords to /etc/shadow.

```bash
sudo cat /etc/shadow | head -3
```

The shadow file is readable only by root. Each line contains the username and a hashed password.
The hash algorithm is indicated by the prefix: $6$ is SHA-512, $y$ is yescrypt (modern Ubuntu).

This separation is critical security design. /etc/passwd must be world-readable because many
programs look up user account information. /etc/shadow can be root-only because only the
authentication system needs to check passwords.

---

### Certification Connection

File permissions and ownership is one of the most heavily tested areas on the Linux+ exam.
Key objectives include:

Interpreting the 10-character permission string from ls -l.

Calculating octal permission values and applying them with chmod.

Understanding chown and chgrp syntax including the -R recursive flag.

Understanding how umask interacts with file and directory creation defaults.

Understanding the difference between /etc/passwd and /etc/shadow.

---

### Transition to Part 2

In Part 2 we cover the special permission bits: SUID, SGID, and the sticky bit. These appear
on every Linux+ exam and have significant security implications. We will also practice a series
of exam-style scenarios to solidify your octal math. Take a break and continue.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
