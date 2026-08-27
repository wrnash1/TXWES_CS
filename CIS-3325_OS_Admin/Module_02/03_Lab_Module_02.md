# Lab 02: File System Hierarchy and Navigation Commands

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will navigate the Linux filesystem from root to deep subdirectories, examine key
system directories, create a structured directory tree, manipulate files with copy, move, and
delete commands, search for files using both find and locate, and search file contents with grep.

Every command you run here is a skill tested on the CompTIA Linux+ exam. You will run each command,
observe the output, and answer analysis questions based on what you see.

**What you will practice:**

- Navigating with cd using both absolute and relative paths
- Inspecting directory contents with ls and its options
- Creating and removing directories and files
- Searching with find and locate
- Searching file contents with grep
- Using output redirection and pipes
- Reading manual pages

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running
- You are logged in as labadmin
- You have watched both parts of the Module 02 video lecture
- You have read the Module 02 Reading Guide

---

### Part 1 - Filesystem Exploration

**Step 1.1 - Confirm your starting location**

```bash
pwd
whoami
```

Expected output:

```
/home/labadmin
labadmin
```

**Step 1.2 - Explore the root directory**

```bash
cd /
ls -la
```

Record how many items are listed in the root directory.

**Step 1.3 - Explore /etc**

```bash
cd /etc
ls -la | head -30
```

The head -30 limits the output to the first 30 lines. /etc contains hundreds of files on a
standard Ubuntu installation.

```bash
ls -la | wc -l
```

This counts the total number of lines in the ls output, giving you a count of items in /etc.
Record this number.

**Step 1.4 - Explore /var/log**

```bash
cd /var/log
ls -lah
```

The -h flag shows file sizes in human-readable format (K, M, G). Note the sizes of syslog and
any other large log files.

```bash
tail -20 syslog
```

Review the last 20 lines of the system log. Note the timestamps and message types you see.

**Step 1.5 - Explore /proc**

```bash
cd /proc
ls | head -20
```

The numbered directories represent running process IDs. Let us look at process 1.

```bash
cat /proc/1/status | head -15
```

This shows the status of process 1 (systemd), including its name and memory usage.

```bash
cat /proc/cpuinfo | grep "model name"
```

This shows your CPU model. On a virtual machine, VirtualBox exposes the host CPU information.

```bash
cat /proc/meminfo | head -10
```

This shows memory information. MemTotal is your VM's total RAM allocation.

**Step 1.6 - Return home and verify location**

```bash
cd ~
pwd
```

---

### Part 2 - Directory and File Operations

**Step 2.1 - Create a directory structure**

```bash
mkdir -p ~/lab02/configs
mkdir -p ~/lab02/logs
mkdir -p ~/lab02/backups/archive
ls -R ~/lab02/
```

The -R flag on ls shows subdirectories recursively. Verify all four directories were created.

**Step 2.2 - Create test files**

```bash
touch ~/lab02/configs/app.conf
touch ~/lab02/configs/network.conf
touch ~/lab02/logs/app.log
touch ~/lab02/logs/error.log
ls -la ~/lab02/configs/
ls -la ~/lab02/logs/
```

**Step 2.3 - Write content to files**

```bash
echo "# Application Configuration" > ~/lab02/configs/app.conf
echo "port=8080" >> ~/lab02/configs/app.conf
echo "debug=false" >> ~/lab02/configs/app.conf
cat ~/lab02/configs/app.conf
```

Note that the first echo uses > (overwrite) and the second and third use >> (append). After three
commands, the file has three lines.

**Step 2.4 - Copy files**

```bash
cp ~/lab02/configs/app.conf ~/lab02/backups/app.conf.backup
ls -l ~/lab02/backups/
```

Verify the backup was created.

**Step 2.5 - Move and rename a file**

```bash
mv ~/lab02/configs/network.conf ~/lab02/configs/network.conf.old
ls -l ~/lab02/configs/
```

The file is now renamed. The original name no longer exists.

**Step 2.6 - Create a symbolic link**

```bash
ln -s ~/lab02/configs/app.conf ~/lab02/app_link
ls -la ~/lab02/app_link
cat ~/lab02/app_link
```

The ls -la output shows the link with -> pointing to the target. Reading the link reads the
target file's content.

**Step 2.7 - Remove files and directories**

```bash
rm ~/lab02/logs/error.log
ls -la ~/lab02/logs/
```

Verify error.log is gone. Only app.log should remain.

```bash
rm -r ~/lab02/backups/archive/
ls -R ~/lab02/
```

The archive directory is removed. All other directories remain.

---

### Part 3 - Searching the Filesystem

**Step 3.1 - Use find to search by name**

```bash
find /etc -name "hostname" 2>/dev/null
```

Find the hostname configuration file in /etc. The 2>/dev/null suppresses permission errors.

```bash
find /etc -name "*.conf" 2>/dev/null | head -20
```

Find the first 20 .conf files in /etc.

**Step 3.2 - Use find to search by type**

```bash
find /etc -type d 2>/dev/null | head -10
```

Find the first 10 directories under /etc.

```bash
find /etc -type l 2>/dev/null | head -10
```

Find symbolic links in /etc.

**Step 3.3 - Use find to search by size**

```bash
find /var/log -type f -size +100k 2>/dev/null
```

Find log files larger than 100 kilobytes.

**Step 3.4 - Use find to search recently modified files**

```bash
find ~/lab02 -mmin -60
```

-mmin -60 means "modified within the last 60 minutes." All your lab02 files should appear
since you just created them.

**Step 3.5 - Use locate (if available)**

```bash
which locate
```

If locate is not installed, install it:

```bash
sudo apt install mlocate -y
sudo updatedb
```

Now search:

```bash
locate sshd_config
locate passwd
```

Compare the speed of locate to the find commands above.

**Step 3.6 - Use grep to search file contents**

```bash
grep "port" ~/lab02/configs/app.conf
grep -n "port" ~/lab02/configs/app.conf
grep -v "^#" ~/lab02/configs/app.conf
```

The first grep finds lines containing "port". The -n version shows line numbers. The -v version
excludes comment lines (lines starting with #).

```bash
grep -r "root" /etc/ssh/ 2>/dev/null
```

Search recursively for the word "root" in all SSH configuration files.

---

### Part 4 - Pipes and Redirection

**Step 4.1 - Pipe commands together**

```bash
ls /etc | grep "ssh"
```

Find SSH-related files in /etc.

```bash
ps aux | grep "systemd" | head -5
```

List processes, filter for systemd, show first 5.

```bash
cat /etc/passwd | cut -d: -f1 | sort
```

Extract just the usernames from /etc/passwd and sort them alphabetically.

**Step 4.2 - Capture output to a file**

```bash
ls -la /etc > ~/lab02/logs/etc_listing.txt
wc -l ~/lab02/logs/etc_listing.txt
head -5 ~/lab02/logs/etc_listing.txt
```

Redirect the /etc listing to a file, count lines, and preview the first 5.

**Step 4.3 - Append to a file**

```bash
echo "--- /var/log listing ---" >> ~/lab02/logs/etc_listing.txt
ls -la /var/log >> ~/lab02/logs/etc_listing.txt
wc -l ~/lab02/logs/etc_listing.txt
```

The file now contains both listings. The line count increased.

**Step 4.4 - Redirect stderr**

```bash
find / -name "shadow" 2>/dev/null
find / -name "shadow" 2>>~/lab02/logs/find_errors.txt
cat ~/lab02/logs/find_errors.txt | head -5
```

The first command discards errors. The second captures them to a file. Review the captured
permission-denied errors.

---

### Part 5 - Manual Pages

**Step 5.1 - Read man pages**

```bash
man ls
```

Press q to quit. Press / to search, then type -la to search for the -l and -a option descriptions.

```bash
man find | grep -A2 "\-mtime"
```

This uses grep -A2 (show 2 lines after match) to find the -mtime documentation in the find
man page without entering the interactive viewer.

```bash
man -k "list files"
```

Search man page descriptions for the phrase "list files." This uses the apropos functionality.

---

### Part 6 - Analysis Questions

Answer each question in 2 to 4 complete sentences.

**Question 1:** You ran find /var/log -type f -size +100k and found several large log files.
What is the security or operational concern when a log file grows very large? Name two ways to
manage log file sizes in production.

**Question 2:** You used both find and locate to search for files. Describe a scenario where
find would give you a correct result but locate would fail to find the same file. What command
do you run to fix locate's database?

**Question 3:** You created a symbolic link to app.conf. When you edited the link's target later,
the changes showed up when you read the link. Explain why this happens and identify one scenario
where a hard link would be more appropriate than a symlink.

**Question 4:** You used grep -v "^#" to filter out comment lines from a config file. Explain
what the ^ character means in a grep pattern. What would happen if you used grep -v "#" instead?

**Question 5:** Explain the difference between > and >> when redirecting output. Write the exact
command you would use to append the output of ps aux to a file called processes.log without
overwriting its current contents.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.3 showing ls -la | wc -l output in /etc
2. Screenshot of Part 1, Step 1.5 showing cat /proc/cpuinfo output
3. Screenshot of Part 2, Step 2.3 showing cat ~/lab02/configs/app.conf output
4. Screenshot of Part 2, Step 2.6 showing the symbolic link in ls -la output
5. Screenshot of Part 3, Step 3.4 showing find ~/lab02 -mmin -60 results
6. Screenshot of Part 3, Step 3.6 showing grep results in app.conf
7. Screenshot of Part 4, Step 4.2 showing wc -l and head -5 output
8. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| /etc item count screenshot | 10 |
| /proc/cpuinfo screenshot | 10 |
| app.conf content screenshot | 10 |
| Symbolic link ls -la screenshot | 10 |
| find -mmin -60 screenshot | 10 |
| grep results screenshot | 10 |
| Redirection output screenshot | 10 |
| Analysis Question 1 (log management) | 5 |
| Analysis Question 2 (find vs locate) | 5 |
| Analysis Question 3 (links) | 5 |
| Analysis Question 4 (grep patterns) | 5 |
| Analysis Question 5 (redirection) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

**Challenge Step 1 — Build and traverse a deep directory tree with relative paths**

Create a multi-level directory structure and practice navigating it using only relative paths
and the special directory references . and ..:

```bash
mkdir -p ~/challenge/level1/level2/level3/level4
cd ~/challenge/level1/level2/level3/level4
pwd
ls ../../../
cd ../../
pwd
ls -la
```

Now create files at multiple levels and practice using tab completion to navigate:

```bash
touch ~/challenge/level1/alpha.txt
touch ~/challenge/level1/level2/beta.conf
touch ~/challenge/level1/level2/level3/gamma.log
find ~/challenge -type f -ls
```

Document the inode numbers shown in the find output. Explain in two sentences what an inode
is and why two hard-linked files share the same inode number.

**Challenge Step 2 — Advanced grep: multi-pattern search and context output**

Use grep to perform forensic-style log analysis on the system authentication log:

```bash
sudo grep -E "Failed|Invalid|refused" /var/log/auth.log | wc -l
sudo grep -E "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn | head -10
sudo grep -n "sudo" /var/log/auth.log | tail -20
sudo grep -B2 -A2 "session opened" /var/log/auth.log | head -30
```

The second command extracts the source IP address of failed password attempts, counts
occurrences, and sorts them by frequency. If /var/log/auth.log does not exist, use
/var/log/syslog as a substitute. Document your output and explain in two sentences how this
grep pipeline could be incorporated into a daily security monitoring script.

**Challenge Step 3 — Redirection chaining and tee**

Demonstrate mastery of output redirection by capturing both a command's output and errors
while simultaneously displaying them on screen:

```bash
find /etc -name "*.conf" 2>/dev/null | tee /tmp/conf_list.txt | wc -l
cat /tmp/conf_list.txt | head -10

find / -name "shadow" 2>/dev/null | tee /tmp/shadow_search.txt
cat /tmp/shadow_search.txt

(echo "=== Disk Usage ===" && df -h && echo "=== Memory ===" && free -h) > /tmp/system_report.txt 2>&1
cat /tmp/system_report.txt
```

Explain in three sentences the difference between > (overwrite), >> (append), and tee in
terms of where output goes and when you would choose each one in a production environment.
