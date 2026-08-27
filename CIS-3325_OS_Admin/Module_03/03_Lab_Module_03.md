# Lab 03: File Permissions and Ownership

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will create files and directories with specific permissions using both octal and
symbolic chmod notation, verify permissions with ls -l, change file ownership with chown and
chgrp, test how umask affects newly created files, set SGID on a shared directory, and use find
to locate SUID files on the system.

The core skill this lab builds is the ability to look at an ls -l output and understand exactly
what it means - and to predict what ls -l will show before you run chmod. Practice predicting
before you verify.

**What you will practice:**

- chmod with octal notation
- chmod with symbolic notation
- chown and chgrp
- umask testing
- SUID and SGID identification and setting
- find with permission filters

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running
- You are logged in as labadmin
- You have watched both parts of the Module 03 video lecture
- You have read the Module 03 Reading Guide

---

### Part 1 - Reading Permissions with ls -l

**Step 1.1 - Inspect key system files**

```bash
ls -l /etc/passwd /etc/shadow /usr/bin/passwd
```

Expected output (approximate):

```
-rw-r--r-- 1 root root   2345 Jan 15 10:30 /etc/passwd
-rw-r----- 1 root shadow 1456 Jan 15 10:30 /etc/shadow
-rwsr-xr-x 1 root root  59640 Mar 22  2023 /usr/bin/passwd
```

Record the permissions, owner, and group for each file.

**Step 1.2 - Analyze the permissions**

For each of the three files, calculate the octal permission value from the symbolic output.
Write your calculations before moving on.

For /etc/passwd: rw-r--r-- = ? + ? + ? = ???
For /etc/shadow: rw-r----- = ? + ? + ? = ???
For /usr/bin/passwd: rwsr-xr-x = ??? (the s means SUID is set and execute is also set)

---

### Part 2 - Creating Files with Specific Permissions

**Step 2.1 - Create a working directory**

```bash
mkdir ~/lab03
cd ~/lab03
```

**Step 2.2 - Create files and set permissions with octal notation**

```bash
touch public.txt
touch private.txt
touch groupfile.txt
touch script.sh
echo '#!/bin/bash' > script.sh
echo 'echo "Script running"' >> script.sh
```

Now set specific permissions:

```bash
chmod 644 public.txt
chmod 600 private.txt
chmod 640 groupfile.txt
chmod 755 script.sh
```

**Step 2.3 - Verify with ls -l**

```bash
ls -la ~/lab03/
```

Before looking at the output, predict what you should see for each file:

- public.txt: should show -rw-r--r--
- private.txt: should show -rw-------
- groupfile.txt: should show -rw-r-----
- script.sh: should show -rwxr-xr-x

Does your actual output match?

**Step 2.4 - Test running the script**

```bash
./script.sh
```

Expected output: Script running

Now remove execute permission and try again:

```bash
chmod 644 script.sh
./script.sh
```

Expected output: bash: ./script.sh: Permission denied

Restore execute permission:

```bash
chmod 755 script.sh
```

---

### Part 3 - Symbolic chmod Notation

**Step 3.1 - Add permissions with symbolic notation**

```bash
ls -la public.txt
chmod g+w public.txt
ls -la public.txt
```

The group write bit was added. Permissions changed from 644 (rw-r--r--) to 664 (rw-rw-r--).

**Step 3.2 - Remove permissions with symbolic notation**

```bash
chmod o-r public.txt
ls -la public.txt
```

Others read bit removed. Permissions changed to 660 (rw-rw----).

**Step 3.3 - Set permissions exactly with symbolic notation**

```bash
chmod u=rw,g=r,o= groupfile.txt
ls -la groupfile.txt
```

This sets owner to rw-, group to r--, others to nothing. Same as octal 640.

**Step 3.4 - Add execute for all**

```bash
touch deploy.sh
echo '#!/bin/bash' > deploy.sh
chmod a+x deploy.sh
ls -la deploy.sh
```

a+x adds execute for all three levels simultaneously.

---

### Part 4 - Changing Ownership

**Step 4.1 - Create a user and group for testing**

```bash
sudo useradd -m devuser
sudo groupadd devteam
sudo usermod -aG devteam devuser
```

**Step 4.2 - Change file ownership**

```bash
sudo chown devuser:devteam groupfile.txt
ls -l groupfile.txt
```

The file owner is now devuser and the group is devteam.

**Step 4.3 - Change only the group**

```bash
sudo chgrp devteam public.txt
ls -l public.txt
```

Only the group changed. The owner remains labadmin.

**Step 4.4 - Set up a shared directory with SGID**

```bash
sudo mkdir /opt/devshared
sudo chown labadmin:devteam /opt/devshared
sudo chmod 2775 /opt/devshared
ls -la /opt/ | grep devshared
```

Expected output excerpt:

```
drwxrwsr-x 2 labadmin devteam 4096 Jan 15 10:30 devshared
```

The s in the group execute position indicates SGID is set.

**Step 4.5 - Test SGID group inheritance**

```bash
touch /opt/devshared/testfile.txt
ls -l /opt/devshared/testfile.txt
```

The file should be owned by labadmin but have devteam as its group, even though your primary
group is labadmin. This is SGID group inheritance in action.

---

### Part 5 - Testing umask

**Step 5.1 - Check current umask**

```bash
umask
```

Record the current umask value. On Ubuntu it should be 0022.

**Step 5.2 - Create files with default umask**

```bash
touch default_file.txt
mkdir default_dir
ls -la
```

Verify: default_file.txt should be 644 (666 - 022 = 644) and default_dir should be 755
(777 - 022 = 755).

**Step 5.3 - Change the umask and test**

```bash
umask 027
touch private_file.txt
mkdir private_dir
ls -la
```

With umask 027:
- private_file.txt should be 640 (666 - 027 = 640)
- private_dir should be 750 (777 - 027 = 750)

**Step 5.4 - Restore the original umask**

```bash
umask 022
```

Note: This umask change only lasts for the current session. It resets when you log out.

---

### Part 6 - Finding SUID and SGID Files

**Step 6.1 - Find all SUID files on the system**

```bash
find / -perm /4000 -type f 2>/dev/null
```

Record the list of SUID files found. These are executables that run as their owner (typically root).

**Step 6.2 - Find all SGID files and directories**

```bash
find / -perm /2000 2>/dev/null | head -20
```

Show the first 20 SGID files and directories on the system.

**Step 6.3 - Find world-writable files (security audit)**

```bash
find / -perm -o+w -type f 2>/dev/null | grep -v "^/proc" | head -20
```

World-writable files can be modified by any user, which is a security concern outside of /tmp.

---

### Part 7 - Analysis Questions

Answer each question in 2 to 4 complete sentences.

**Question 1:** You ran ls -l /usr/bin/passwd and saw -rwsr-xr-x. Explain what the s means in
the owner execute position. Why is SUID necessary for the passwd command to work? What security
risk does SUID introduce and how is that risk mitigated for /usr/bin/passwd?

**Question 2:** You set umask 027 and created a file. The file got permissions 640, not 750. Why
does the execute bit not appear in file permissions even though 777 - 027 = 750? What base value
does the umask apply to for regular files versus directories?

**Question 3:** You created /opt/devshared with SGID (chmod 2775). When devuser created a file
inside it, the file inherited the devteam group automatically. Explain why SGID on a directory
is useful in a team development environment. What would happen without the SGID bit?

**Question 4:** You ran find / -perm -o+w -type f and found unexpected world-writable files
outside /tmp. Why is a world-writable file a security concern? What command would you use to
fix the permissions on a world-writable file to restrict it to owner read+write only?

**Question 5:** The permissions on /etc/shadow are rw-r-----. The owner is root and the group is
shadow. This means root and members of the shadow group can read it, but nobody else can. Why is
this more secure than storing password hashes in /etc/passwd, which is world-readable?

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.1 showing ls -l output for all three system files
2. Screenshot of Part 2, Step 2.3 showing ls -la ~/lab03/ with all four files and permissions
3. Screenshot of Part 2, Step 2.4 showing the Permission denied error then successful execution
4. Screenshot of Part 4, Step 4.4 showing ls -la /opt/ with devshared and SGID s visible
5. Screenshot of Part 4, Step 4.5 showing testfile.txt with devteam group
6. Screenshot of Part 5, Step 5.3 showing private_file.txt (640) and private_dir (750)
7. Screenshot of Part 6, Step 6.1 showing the SUID file list
8. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| System files ls -l screenshot | 10 |
| lab03 files with correct permissions screenshot | 15 |
| Permission denied + success screenshot | 10 |
| SGID devshared directory screenshot | 10 |
| SGID group inheritance screenshot | 10 |
| umask 027 file/dir permissions screenshot | 10 |
| SUID files list screenshot | 5 |
| Analysis Question 1 (SUID explanation) | 5 |
| Analysis Question 2 (umask and execute) | 5 |
| Analysis Question 3 (SGID directory) | 5 |
| Analysis Question 4 (world-writable) | 5 |
| Analysis Question 5 (shadow file) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

**Challenge Step 1 — Audit SUID and SGID binaries system-wide**

Run a full system scan for all SUID and SGID files and save the results for comparison:

```bash
find / -perm /4000 -type f 2>/dev/null | sort > /tmp/suid_list.txt
find / -perm /2000 -type f 2>/dev/null | sort > /tmp/sgid_list.txt
wc -l /tmp/suid_list.txt /tmp/sgid_list.txt
cat /tmp/suid_list.txt
```

Install a new package that contains a SUID binary, then re-run the scan and diff the results:

```bash
sudo apt install -y sudo 2>/dev/null || true
find / -perm /4000 -type f 2>/dev/null | sort > /tmp/suid_list_new.txt
diff /tmp/suid_list.txt /tmp/suid_list_new.txt
```

Explain in two sentences why maintaining a baseline SUID file list and comparing it regularly
is a critical security hardening practice on production Linux servers.

**Challenge Step 2 — Implement and test ACLs on a shared directory**

Create a realistic shared project directory with fine-grained ACL permissions:

```bash
sudo groupadd projectteam
sudo useradd -m -s /bin/bash alice
sudo useradd -m -s /bin/bash bob
sudo usermod -aG projectteam alice
sudo usermod -aG projectteam bob

sudo mkdir -p /opt/project/shared
sudo chown root:projectteam /opt/project/shared
sudo chmod 2770 /opt/project/shared

sudo setfacl -m u:alice:rwx /opt/project/shared
sudo setfacl -m u:bob:rx /opt/project/shared
sudo setfacl -m d:u:alice:rwx /opt/project/shared
sudo setfacl -m d:u:bob:rx /opt/project/shared
getfacl /opt/project/shared
```

Switch to alice and create a file, then switch to bob and attempt to write to it:

```bash
sudo -u alice touch /opt/project/shared/alice_file.txt
sudo -u bob echo "test" >> /opt/project/shared/alice_file.txt
```

Document the permission denied output and explain in three sentences how ACLs extend beyond
standard Unix permission bits to enable per-user access control on shared resources.

**Challenge Step 3 — Explore umask interaction with SGID directories**

Observe how umask affects files created inside an SGID directory and how default ACLs
override the umask for inherited permissions:

```bash
umask
sudo -u alice bash -c 'umask 027; touch /opt/project/shared/umask_test.txt'
ls -la /opt/project/shared/umask_test.txt
getfacl /opt/project/shared/umask_test.txt

sudo setfacl -m d:o::r /opt/project/shared
sudo -u alice bash -c 'touch /opt/project/shared/acl_test.txt'
getfacl /opt/project/shared/acl_test.txt
ls -la /opt/project/shared/acl_test.txt
```

Compare the two files' effective permissions. Explain in two sentences how default ACLs
on a parent directory interact with the creating user's umask when determining the
permissions of newly created files inside that directory.
