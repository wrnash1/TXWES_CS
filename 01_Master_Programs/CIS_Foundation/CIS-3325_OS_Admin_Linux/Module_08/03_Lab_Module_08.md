# Lab: Module 08 — File System Permissions and Ownership

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Lab Overview

In this lab you will configure a realistic directory structure for a web application team, apply appropriate permissions, work with special bits, and implement ACLs to handle permission scenarios that the traditional model cannot express. By the end you will have hands-on experience with every permission concept covered in the module.

**Estimated Time:** 60–90 minutes

**Required Environment:** Linux VM with sudo access. Both Ubuntu and RHEL-family distributions work. ACL support requires a filesystem with ACLs enabled (ext4 and XFS with default mount options both work on modern distributions).

---

## Prerequisites

- Completion of Module 08 video lectures (Parts 1 and 2)
- Module 07 lab complete (user accounts created, or you will create test users here)
- Basic terminal proficiency

---

## Scenario

You are administering a Linux server for **Ramrod Software**. The server hosts a web application. You need to set up a directory structure with proper permissions for:

- The production web root (Apache/Nginx serves files from here)
- A shared development directory (team members collaborate here)
- An uploads directory (web application writes here; developers can view but not delete others' files)
- A reports directory (only the finance group and the auditor user should read these)

---

## Task 1 — Prepare Test Users and Groups

Create minimal test accounts if not already present from Module 07.

### Step 1.1 — Create Groups

```bash
# Create groups for this lab
sudo groupadd webteam
sudo groupadd finance
sudo groupadd developers

# Verify
getent group webteam finance developers
```

### Step 1.2 — Create Test Users

```bash
# Create test users
sudo useradd -m -s /bin/bash -G webteam,developers alice
sudo useradd -m -s /bin/bash -G webteam bob
sudo useradd -m -s /bin/bash -G finance carol
sudo useradd -m -s /bin/bash auditor1

# Set simple passwords for testing
echo "alice:TestPass1!" | sudo chpasswd
echo "bob:TestPass1!" | sudo chpasswd
echo "carol:TestPass1!" | sudo chpasswd
echo "auditor1:TestPass1!" | sudo chpasswd

# Verify group membership
id alice
id bob
id carol
id auditor1
```

---

## Task 2 — Build the Directory Structure

### Step 2.1 — Create Directories

```bash
# Create the base directory structure
sudo mkdir -p /srv/webapp/html
sudo mkdir -p /srv/webapp/dev
sudo mkdir -p /srv/webapp/uploads
sudo mkdir -p /srv/webapp/reports

# Verify
ls -la /srv/webapp/
```

### Step 2.2 — Create a System Web Server Account

```bash
# Create www-data if it does not exist (it usually does on Ubuntu)
id www-data 2>/dev/null || sudo useradd -r -s /sbin/nologin www-data

# Verify
grep www-data /etc/passwd
```

---

## Task 3 — Configure the Production Web Root

The `/srv/webapp/html` directory should:

- Be owned by root with group `www-data`
- Be readable and executable by everyone (public content)
- Files should be 644; directories should be 755
- New files created by developers should automatically get `www-data` group (SGID)

### Step 3.1 — Set Ownership and Base Permissions

```bash
# Set ownership
sudo chown root:www-data /srv/webapp/html

# Set SGID so new files inherit www-data group
sudo chmod 2755 /srv/webapp/html

# Verify
ls -ld /srv/webapp/html
# Should show: drwxr-sr-x root www-data /srv/webapp/html
```

### Step 3.2 — Create Test Files and Verify SGID Inheritance

```bash
# Add alice to www-data group so she can write
sudo usermod -aG www-data alice

# Create files as alice and verify group inheritance
sudo su -c "touch /srv/webapp/html/index.html" alice
ls -l /srv/webapp/html/index.html
```

**Lab Question 1:** What group owns `index.html`? Is it `alice`'s primary group or `www-data`? Why?

---

## Task 4 — Configure the Shared Development Directory

The `/srv/webapp/dev` directory should:

- Be owned by root with group `developers`
- All developers can read and write; others cannot access
- New files automatically inherit the `developers` group (SGID)
- Users can only delete their own files (sticky bit)

### Step 4.1 — Set Permissions

```bash
# Set ownership
sudo chown root:developers /srv/webapp/dev

# Set SGID + sticky bit + group writable
# 2 = SGID, 1 = sticky, 770 = rwxrwx---
sudo chmod 3770 /srv/webapp/dev

# Verify
ls -ld /srv/webapp/dev
# Should show: drwxrws--T root developers /srv/webapp/dev
# Wait — let's check: 3 = SGID + Sticky, 770
# drwxrws--t  ... the 't' should be lowercase if others has execute
# Actually others has no execute, so it shows capital T
```

**Lab Question 2:** The `t` in the sticky bit position appears as a capital `T`. What does that indicate? Is this correct for a directory with `770` permissions?

### Step 4.2 — Test the Sticky Bit

```bash
# Create a file as alice
sudo su -c "touch /srv/webapp/dev/alice_notes.txt" alice

# Try to delete alice's file as bob (should fail due to sticky bit)
sudo su -c "rm /srv/webapp/dev/alice_notes.txt" bob
echo "Exit code: $?"
```

Record the error message.

---

## Task 5 — Configure the Uploads Directory

The `/srv/webapp/uploads` directory should:

- Be writable by `www-data` (web app writes here)
- Be readable by `developers` (they review uploads)
- Use sticky bit so no one can delete others' uploads
- World-readable so the web server can serve uploaded content

### Step 5.1 — Set Permissions

```bash
# Set ownership
sudo chown www-data:developers /srv/webapp/uploads

# Permissions: rwxrwxr-x plus sticky
sudo chmod 1775 /srv/webapp/uploads

# Verify
ls -ld /srv/webapp/uploads
# drwxrwxr-t www-data developers /srv/webapp/uploads
```

### Step 5.2 — Verify Access

```bash
# Simulate www-data writing a file
sudo su -s /bin/bash -c "touch /srv/webapp/uploads/upload001.jpg" www-data

# Verify alice (developer) can read it
sudo su -c "ls /srv/webapp/uploads/" alice
sudo su -c "cat /srv/webapp/uploads/upload001.jpg" alice

# Verify alice CANNOT delete www-data's file (sticky bit)
sudo su -c "rm /srv/webapp/uploads/upload001.jpg" alice
echo "Exit code: $?"
```

---

## Task 6 — Configure the Reports Directory with ACLs

The `/srv/webapp/reports` directory needs a permission configuration the traditional model cannot express:

- `carol` (finance team) needs full read/write access
- `auditor1` (not in any relevant group) needs read-only access
- Everyone else has no access
- New files created in reports should automatically grant these same permissions

### Step 6.1 — Base Permissions

```bash
# Own by root, group root, nobody else by default
sudo chown root:root /srv/webapp/reports
sudo chmod 700 /srv/webapp/reports

# Verify
ls -ld /srv/webapp/reports
```

### Step 6.2 — Apply ACLs

```bash
# Check if ACL tools are installed
which setfacl getfacl || sudo apt install acl -y

# Grant carol read and write access
sudo setfacl -m u:carol:rwx /srv/webapp/reports

# Grant auditor1 read-only access
sudo setfacl -m u:auditor1:r-x /srv/webapp/reports

# Set default ACLs so new files inherit these permissions
sudo setfacl -d -m u:carol:rwx /srv/webapp/reports
sudo setfacl -d -m u:auditor1:r-- /srv/webapp/reports
sudo setfacl -d -m u:root:rwx /srv/webapp/reports
sudo setfacl -d -m o::--- /srv/webapp/reports

# View all ACLs including defaults
getfacl /srv/webapp/reports
```

### Step 6.3 — Test ACL Access

```bash
# Create a report file as root
sudo touch /srv/webapp/reports/q1_report.txt
sudo echo "Confidential Q1 Data" | sudo tee /srv/webapp/reports/q1_report.txt

# Verify carol can read and write
sudo su -c "cat /srv/webapp/reports/q1_report.txt" carol
sudo su -c "echo 'Carol appended' >> /srv/webapp/reports/q1_report.txt" carol

# Verify auditor1 can only read
sudo su -c "cat /srv/webapp/reports/q1_report.txt" auditor1
sudo su -c "rm /srv/webapp/reports/q1_report.txt" auditor1
echo "auditor1 delete exit code: $?"

# Verify alice (no ACL entry) cannot access
sudo su -c "ls /srv/webapp/reports/" alice
echo "alice ls exit code: $?"
```

**Lab Question 3:** How does the ACL mask affect the permissions you set? Run `getfacl /srv/webapp/reports` and identify the mask entry. What is it set to?

---

## Task 7 — Work with umask

### Step 7.1 — Observe Default umask

```bash
# View current umask
umask
umask -S

# Create test files
touch /tmp/test_default_file.txt
mkdir /tmp/test_default_dir
ls -l /tmp/test_default_file.txt
ls -ld /tmp/test_default_dir
```

### Step 7.2 — Change umask and Observe Effect

```bash
# Set a more restrictive umask
umask 027

# Create new test objects
touch /tmp/test_restricted_file.txt
mkdir /tmp/test_restricted_dir
ls -l /tmp/test_restricted_file.txt
ls -ld /tmp/test_restricted_dir
```

**Lab Question 4:** With umask 027, what octal permissions did the file receive? What did the directory receive? Calculate manually and verify your answer.

### Step 7.3 — Reset umask

```bash
# Restore default umask
umask 022
```

---

## Task 8 — Audit SUID and SGID Files

### Step 8.1 — Find SUID Files

```bash
# Find all SUID files on the system
sudo find / -perm -4000 -type f -ls 2>/dev/null

# Save to a file for review
sudo find / -perm -4000 -type f -ls 2>/dev/null > /tmp/suid_files.txt
wc -l /tmp/suid_files.txt
cat /tmp/suid_files.txt
```

### Step 8.2 — Find SGID Files and Directories

```bash
sudo find / -perm -2000 -type f -ls 2>/dev/null
sudo find / -perm -2000 -type d -ls 2>/dev/null
```

**Lab Question 5:** List three SUID executables you found and explain why each one legitimately needs SUID to function.

---

## Task 9 — Use namei to Trace Permissions

```bash
# Trace the permission chain for a file
namei -l /srv/webapp/reports/q1_report.txt

# Trace another path
namei -l /home/alice/.bashrc
```

Observe how namei shows the permissions at every directory level. A single directory without execute permission anywhere in the path would block access to the file regardless of the file's own permissions.

---

## Task 10 — Cleanup

```bash
# Remove lab directories
sudo rm -rf /srv/webapp

# Remove test users
for user in alice bob carol auditor1; do
  sudo userdel -r "$user" 2>/dev/null
done

# Remove groups
for group in webteam finance developers; do
  sudo groupdel "$group" 2>/dev/null
done

echo "Cleanup complete"
```

---

## Lab Deliverables

Submit a short report covering:

1. Output of `ls -ld /srv/webapp/html` (after Task 3) showing SGID
2. Output of `ls -l /srv/webapp/html/index.html` showing inherited group
3. The error message when bob tried to delete alice's file (Task 4.2)
4. Full output of `getfacl /srv/webapp/reports` (Task 6.2)
5. Answers to Lab Questions 1 through 5

---

## Troubleshooting Guide

| Problem | Solution |
|---|---|
| `Operation not supported` on setfacl | Filesystem may lack ACL support; try `sudo mount -o remount,acl /` |
| `su: Authentication failure` | Use `sudo su -c "command" username` syntax |
| `namei: command not found` | Install with `sudo apt install util-linux` |
| SGID not inherited | Verify directory has SGID set with `ls -ld dir` |
| ACL not taking effect | Check the mask entry with `getfacl`; may be restricting effective permissions |
| `groupdel: cannot remove the primary group of user` | Remove users from primary group first |

---

## Part 9 — Challenge Exercise

### Challenge 1: SUID/SGID Security Audit

Perform a systematic security audit of special permission bits across the running system, establish a baseline, and detect any changes.

1. Generate a baseline inventory of all SUID and SGID binaries on the system and save it to a file: `sudo find / -type f \( -perm -4000 -o -perm -2000 \) -ls 2>/dev/null | sort > ~/suid_baseline.txt`. Count the results with `wc -l ~/suid_baseline.txt`. Review the output and identify at least three SUID binaries whose purpose you can explain (use `man` to research any unfamiliar ones).
2. Create a test binary and apply SUID to it to observe how the kernel enforces it: `cp /bin/cat ~/testcat && chmod u+s ~/testcat && ls -l ~/testcat`. Verify SUID is set. Then confirm that SUID on a file owned by a regular user does not grant elevated privilege — only files owned by root gain meaningful SUID elevation. Check ownership with: `stat --format="%a %U %G" ~/testcat`.
3. Simulate a security event: copy a binary to a temp location, set SUID root on it, then re-run the audit to detect the change: `sudo cp /bin/ls /tmp/suspicious_ls && sudo chmod 4755 /tmp/suspicious_ls`. Re-run the find command and compare against the baseline: `sudo find / -type f -perm -4000 -ls 2>/dev/null | sort > ~/suid_current.txt && diff ~/suid_baseline.txt ~/suid_current.txt`. Observe the diff output, then clean up: `sudo rm /tmp/suspicious_ls`.
4. Audit world-writable files outside `/tmp` and `/proc` as a companion check: `sudo find / -type f -perm -0002 -not -path "/tmp/*" -not -path "/proc/*" -ls 2>/dev/null | head -20`. Any results outside expected system paths warrant investigation.

### Challenge 2: ACL-Based Collaborative Directory

Build a multi-team shared directory structure where fine-grained ACL policies enforce that developers can read and write, QA can read only, and auditors can read a reports subdirectory but nothing else — without changing traditional group memberships.

1. Set up the directory structure: `sudo mkdir -p /srv/collab/{code,reports,private}`. Create three test users if not already present: `sudo useradd -m devuser && sudo useradd -m qauser && sudo useradd -m audituser`. Set ownership and restrictive base permissions: `sudo chown -R root:root /srv/collab && sudo chmod -R 770 /srv/collab`.
2. Apply ACLs to grant `devuser` read/write/execute on `code` and `reports`, `qauser` read/execute on `code` only, and `audituser` read/execute on `reports` only: `sudo setfacl -m u:devuser:rwx /srv/collab/code /srv/collab/reports && sudo setfacl -m u:qauser:r-x /srv/collab/code && sudo setfacl -m u:audituser:r-x /srv/collab/reports`. Verify with `getfacl /srv/collab/code` and `getfacl /srv/collab/reports`.
3. Set a default ACL on the `code` directory so files created there automatically inherit `devuser` read/write: `sudo setfacl -d -m u:devuser:rw- /srv/collab/code`. Test by creating a file as root: `sudo touch /srv/collab/code/newfile.txt && getfacl /srv/collab/code/newfile.txt`. Confirm the default ACL was inherited on the new file.
4. Verify enforcement: confirm `audituser` is denied access to `code`: `sudo -u audituser ls /srv/collab/code 2>&1` — expect `Permission denied`. Confirm `audituser` can read `reports`: `sudo -u audituser ls /srv/collab/reports`. Back up the entire ACL configuration: `getfacl -R /srv/collab > ~/collab_acls_backup.txt`.

### Reflection Questions

1. The kernel permission check is a first-match model — if you are the file owner, owner bits apply exclusively, even if group or other bits are more permissive. Describe a real scenario where this behavior could cause a sysadmin to accidentally lock themselves out of a file they own, and explain the exact sequence of events that would produce the lockout.

2. SUID on an executable causes it to run with the file owner's effective UID. From a security perspective, explain why applying SUID to a shell interpreter (such as `/bin/bash`) is considered one of the most dangerous misconfigurations on a Linux system, and describe what an attacker could do upon discovering a SUID bash binary on a server they have limited access to.
