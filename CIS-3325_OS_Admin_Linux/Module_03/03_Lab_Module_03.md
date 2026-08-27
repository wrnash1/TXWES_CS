# Lab: Module 03 — FHS Exploration and File Content Commands

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Lab Overview

In this lab you will explore the Linux Filesystem Hierarchy Standard directories, practice reading and viewing file content, use `find` and `locate` for file searches, work with file globbing, and build pipelines using redirection and `tee`. This lab builds directly on Module 3 lecture content and prepares you for the navigation tasks expected in Linux+ performance-based questions.

**Estimated time**: 40–55 minutes

**Prerequisites**: Ubuntu Server 22.04 VM from Module 1 lab. SSH or direct console access working.

---

## Pre-Lab

Take a VirtualBox snapshot before starting: Machine → Take Snapshot → "Pre-Lab Module 03."

---

## Part 1 — FHS Exploration

### Step 1: Explore Key Directories

Run the following commands and record what you find. For each, note two to three interesting files or subdirectories you did not expect:

```bash
ls /etc | head -30
ls /var/log
ls /dev | head -30
ls /proc
ls /usr/bin | wc -l
```

The last command counts how many files are in `/usr/bin`. Record the number.

### Step 2: Examine Virtual Filesystem Content

```bash
cat /proc/cpuinfo
cat /proc/meminfo | head -20
cat /proc/uptime
```

For `/proc/uptime`, the first number is seconds since boot. Divide by 60 to get minutes. How long has your VM been running?

### Step 3: Check Key Configuration Files

View the first 10 lines of each file:

```bash
head /etc/passwd
head /etc/group
head -5 /etc/os-release
cat /etc/hostname
```

In `/etc/passwd`, identify the fields separated by colons. The format is: `username:password_placeholder:UID:GID:comment:home_dir:shell`. Find the entry for your student user and record the UID (should be 1000 for the first regular user).

### Step 4: Examine /dev/null

```bash
echo "This text will disappear" > /dev/null
echo $?
ls -la /dev/null
```

What does `echo $?` show? What does `ls -la /dev/null` tell you about the file type? (Look at the first character of the permissions string — it will be `c` for a character device.)

---

## Part 2 — Reading File Content

### Step 5: Practice cat, less, head, and tail

Create a test file with 100 lines:

```bash
for i in $(seq 1 100); do echo "Line $i of the test file" >> /tmp/testfile.txt; done
wc -l /tmp/testfile.txt
```

Now view it different ways:

```bash
head /tmp/testfile.txt
head -n 15 /tmp/testfile.txt
tail /tmp/testfile.txt
tail -n 5 /tmp/testfile.txt
less /tmp/testfile.txt
```

In `less`: search for "Line 50" by pressing `/` and typing `Line 50`. Press `q` to quit.

### Step 6: Follow a Log File

Open a second terminal (or a second SSH session to the VM). In the first terminal, follow the system log:

```bash
tail -f /var/log/syslog
```

In the second terminal, run a command that generates a log entry:

```bash
sudo systemctl restart systemd-journald
```

Watch for new lines to appear in the first terminal. Press `Ctrl+C` in the first terminal to stop following.

If you cannot open a second terminal, skip the second-terminal step and just observe `tail -f /var/log/syslog` for 30 seconds before pressing `Ctrl+C`.

---

## Part 3 — Finding Files

### Step 7: Use find with Multiple Criteria

Find all regular files in `/etc` that have `.conf` extension:

```bash
find /etc -type f -name "*.conf"
```

Count how many there are:

```bash
find /etc -type f -name "*.conf" | wc -l
```

Find all files in `/var/log` larger than 100 KB:

```bash
find /var/log -type f -size +100k
```

Find all directories in `/usr` that start with "lib":

```bash
find /usr -maxdepth 1 -type d -name "lib*"
```

`-maxdepth 1` limits the search to one level deep under `/usr`.

Find all files modified in the last 24 hours in your home directory:

```bash
find ~ -type f -mtime 0
```

`-mtime 0` means modified today (within the last 24 hours).

### Step 8: Use locate

First, update the locate database:

```bash
sudo updatedb
```

Then search for the SSH server config:

```bash
locate sshd_config
```

Search for all files with "shadow" in the name:

```bash
locate shadow
```

Note the difference in speed between `locate` and `find`. Which was faster?

---

## Part 4 — Globbing

### Step 9: Practice File Globbing

Create a set of test files:

```bash
mkdir ~/glob_practice
cd ~/glob_practice
touch file1.txt file2.txt file3.log file4.log config.conf server.conf readme.md notes.md
ls
```

Now use globs to list subsets:

```bash
ls *.txt
ls *.log
ls *.conf
ls file*.txt
ls file[12].txt
ls file?.txt
```

What does `file[12].txt` match? What does `file?.txt` match? Are they the same?

Create a file named `file10.txt`:

```bash
touch file10.txt
ls file?.txt
ls file*.txt
```

What is the difference in output between `file?.txt` and `file*.txt` now that `file10.txt` exists?

---

## Part 5 — Redirection and Pipes

### Step 10: Output Redirection

```bash
cd ~
ls -la /etc > etc_snapshot.txt
wc -l etc_snapshot.txt
```

Append a second directory listing:

```bash
ls -la /var/log >> etc_snapshot.txt
wc -l etc_snapshot.txt
```

The line count should be higher now. The file was appended, not overwritten.

Redirect stderr to suppress permission errors:

```bash
find / -name "*.conf" 2>/dev/null | wc -l
```

Run the same command without the `2>/dev/null` and compare the output. The error suppression version shows only results.

### Step 11: Pipes

Count the number of running processes:

```bash
ps aux | wc -l
```

Find lines in `/etc/passwd` that contain "bash" (users with bash as their shell):

```bash
cat /etc/passwd | grep bash
```

List the 5 largest files in `/var/log`:

```bash
ls -lhS /var/log | head -6
```

`-S` sorts by file size, largest first. `head -6` includes the header line plus 5 files.

### Step 12: tee

Run `df -h` and save the output to a file while also displaying it on screen:

```bash
df -h | tee disk_report.txt
cat disk_report.txt
```

Confirm the file contains the same output that was displayed on screen.

---

## Part 6 — Cleanup

Remove lab files:

```bash
rm /tmp/testfile.txt
rm -rf ~/glob_practice
rm ~/etc_snapshot.txt ~/disk_report.txt 2>/dev/null
```

---

## Deliverables

Submit a document containing:

1. Screenshot showing the output of `find /etc -type f -name "*.conf" | wc -l` — include the count.
2. Screenshot showing the glob comparison from Step 9 (`file?.txt` vs `file*.txt` after creating `file10.txt`).
3. Screenshot showing `df -h | tee disk_report.txt` output.
4. Written answer (3–5 sentences): Explain the difference between `>` and `>>` for output redirection, and describe a real-world scenario where you would use `>>` instead of `>`.
5. Written answer (2–3 sentences): What is the difference between `find` and `locate`? When would you choose each?

---

## Grading Criteria

| Item | Points |
|---|---|
| Screenshots with correct command outputs (3 screenshots) | 45 |
| Redirection explanation with real-world scenario | 25 |
| find vs. locate explanation | 20 |
| Lab completed in VM | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Log Analysis Pipeline

Build a multi-stage pipeline to extract and summarize useful data from a live system log file.

1. Run `sudo grep -i "error\|fail\|warn" /var/log/syslog 2>/dev/null | tee ~/log_issues.txt | wc -l`. Record the count of lines matching error, failure, or warning patterns. Then open `~/log_issues.txt` with `less` and identify the most common source process in those lines.
2. Run `sudo grep -i "error\|fail\|warn" /var/log/syslog 2>/dev/null | awk '{print $5}' | sort | uniq -c | sort -rn | head -10`. This extracts the fifth field (process name), counts occurrences, and shows the top 10. Record which process generates the most warnings or errors.
3. Run `find /var/log -type f -name "*.log" -size +0c 2>/dev/null -exec wc -l {} \; | sort -rn | head -5`. This finds all non-empty `.log` files and shows the five with the most lines. Record the results.

### Challenge 2: Advanced find with Dangerous-File Hunting

Use `find` with permission predicates to identify potentially risky files on the system.

1. Run `find / -perm -4000 -type f 2>/dev/null`. These are SUID (Set User ID) files — executables that run with the file owner's privileges (often root). List all results and look up one unfamiliar entry using `man` or `file`.
2. Run `find /tmp /var/tmp -type f -mtime -1 2>/dev/null`. List all files created or modified in the last 24 hours in temporary directories. On a production server, unexpected files here can indicate malicious activity.
3. Run `find /home -type f -name "*.sh" 2>/dev/null`. List all shell scripts in home directories. For each found, run `head -3 <filename>` to view the first three lines.

### Reflection Questions

1. The `-exec` option in `find` runs a command on every matched file individually, while `| xargs rm` passes all results to `rm` at once. What are the practical tradeoffs between these two approaches for large result sets involving thousands of files?
2. You used `2>/dev/null` throughout this lab to suppress permission errors. In a real security audit, would suppressing those errors be appropriate? What information might you lose by hiding them, and when would it be better to capture them with `2>errors.txt` instead?
