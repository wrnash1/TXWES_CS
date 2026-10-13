# Lab: Module 02 — Filesystem Navigation and File Management

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Lab Overview

In this lab you will practice the core filesystem navigation and file management commands introduced in Module 2. You will create a structured directory hierarchy, manipulate files using `cp`, `mv`, `rm`, and `touch`, use `ls` with multiple flag combinations, and practice both absolute and relative path navigation. All work takes place inside your Ubuntu Server VM.

**Estimated time**: 30–45 minutes

**Prerequisites**: Ubuntu Server 22.04 VM running (from Module 1 lab). Login credentials working.

---

## Safety Note

Before starting this lab, take a VirtualBox snapshot: Machine → Take Snapshot → name it "Pre-Lab Module 02." You will not make any destructive changes in this lab, but snapshotting is a habit that protects you in later labs.

---

## Part 1 — Navigation Basics

### Step 1: Log In and Confirm Your Location

Log in to your VM. Run `pwd` to confirm your starting location.

Expected output: `/home/student` (or your username)

### Step 2: List Your Home Directory

```bash
ls
ls -l
ls -la
ls -lah
```

For each command, note what additional information is shown compared to the previous command. Which files are visible with `-a` that were not visible without it? What do the files starting with `.` represent?

### Step 3: Navigate and Explore

Navigate to the `/etc` directory using an absolute path:

```bash
cd /etc
pwd
ls | head -20
```

Note: `head -20` limits the output to the first 20 lines — `/etc` has many files.

Navigate to `/var/log` using an absolute path:

```bash
cd /var/log
ls -lh
```

Note the file sizes. Which log files are largest?

Navigate back to your home directory using two different methods:

```bash
cd ~
pwd
cd /var/log
cd
pwd
```

Confirm both methods return you to `/home/student`.

---

## Part 2 — Relative Paths

### Step 4: Practice Relative Navigation

Start in your home directory. Navigate to `/etc` using an absolute path, then navigate to `/etc/apt` using a relative path:

```bash
cd /etc
cd apt
pwd
```

Navigate up two levels using relative paths:

```bash
cd ../..
pwd
```

You should now be in `/`. Navigate to `/home/student` using relative paths starting from `/`:

```bash
cd home/student
pwd
```

---

## Part 3 — Creating Directory Structure

### Step 5: Create a Project Directory Tree

From your home directory, create the following structure using a single `mkdir -p` command:

```
~/labwork/
    module02/
        notes/
        files/
        backup/
```

```bash
cd ~
mkdir -p labwork/module02/notes labwork/module02/files labwork/module02/backup
```

Verify the structure was created:

```bash
ls -R labwork/
```

---

## Part 4 — File Creation and Manipulation

### Step 6: Create Test Files

Navigate into `~/labwork/module02/files/`:

```bash
cd ~/labwork/module02/files
```

Create five empty files:

```bash
touch file1.txt file2.txt file3.txt config.conf script.sh
ls -l
```

### Step 7: Copy Files

Copy `file1.txt` to the backup directory:

```bash
cp file1.txt ../backup/file1_backup.txt
ls ../backup/
```

Copy `config.conf` to the notes directory with a new name:

```bash
cp config.conf ../notes/config_original.conf
```

### Step 8: Move and Rename Files

Rename `file2.txt` to `renamed.txt`:

```bash
mv file2.txt renamed.txt
ls
```

Move `renamed.txt` to the backup directory:

```bash
mv renamed.txt ../backup/
ls ../backup/
```

### Step 9: Remove Files

Remove `file3.txt` with confirmation prompt:

```bash
rm -i file3.txt
```

Type `y` and press Enter to confirm.

Remove the entire `notes` directory and its contents (it has a file inside):

```bash
rm -r ../notes/
ls ../
```

The `notes` directory should be gone.

### Step 10: Recreate the Notes Directory

```bash
mkdir ../notes
ls ../
```

---

## Part 5 — File Information Commands

### Step 11: Use the file Command

Run `file` on several different types of files:

```bash
file /bin/bash
file /etc/passwd
file ~/labwork/module02/files/script.sh
file /usr/share/doc/bash/changelog.Debian.gz
```

Record the type reported for each. What is the difference between a text file and an executable?

### Step 12: Locate Commands

```bash
which bash
which ls
which python3
whereis bash
whereis ls
```

Note the difference between `which` (just the binary path) and `whereis` (binary, source, and man page).

---

## Part 6 — Man Pages

### Step 13: Explore man Pages

```bash
man ls
```

Inside the man page:

1. Press `/` and type `-R` to search for the recursive flag description.
2. Press `n` to find the next occurrence.
3. Press `q` to quit.

```bash
man cp
```

Find the flag that preserves file attributes (hint: it is `-p`). Read the description.

```bash
man rm
```

Find the description of `-f` (force). Note the warning about `rm -rf /`.

---

## Part 7 — Cleanup and Reflection

### Step 14: Remove the Lab Directory

When the lab is complete, remove the entire lab directory:

```bash
cd ~
rm -rf labwork/
ls
```

Confirm the `labwork` directory is gone.

---

## Deliverables

Submit a document containing:

1. Screenshot of your terminal after completing Step 5 showing the `ls -R labwork/` output.
2. Screenshot after Step 11 showing the `file` command output for all four paths.
3. Written answer (3–5 sentences): Explain the difference between an absolute path and a relative path. Give one example of each from the commands you ran in this lab.
4. Written answer (2–3 sentences): What is the practical risk of using `rm -rf` without the `-i` flag? What habit can you build to reduce this risk?

---

## Grading Criteria

| Item | Points |
|---|---|
| Screenshots showing correct command outputs | 40 |
| Absolute vs. relative path explanation with examples | 30 |
| rm -rf risk explanation | 20 |
| Lab completed in VM (not just described) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Filesystem Archaeology

Explore the Linux Filesystem Hierarchy Standard by investigating directories that typical users never visit.

1. Run `ls /proc` and notice that these are not real files — they are kernel data structures exposed as a virtual filesystem. Read `/proc/cpuinfo` with `cat /proc/cpuinfo` and `/proc/meminfo` with `cat /proc/meminfo`. Identify the CPU model name and the total memory in kB.
2. Run `ls /dev` and then run `file /dev/sda` (or `file /dev/vda` if that is your disk). Note that `file` reports it as a "block special" file. Run `ls -l /dev/null` and `ls -l /dev/zero`. What do the `c` and `b` file type characters mean in those outputs?
3. Run `stat /etc/passwd` and record the Inode number, number of hard links, and all three timestamps (Access, Modify, Change). Then run `touch /etc/passwd` and `stat /etc/passwd` again. Which timestamp changed and which did not?

### Challenge 2: Efficient Tree Navigation

Build and navigate a complex directory structure using only relative paths from a single starting point.

1. From your home directory, create this entire structure in one `mkdir -p` command: `projects/alpha/src projects/alpha/docs projects/beta/src projects/beta/docs projects/shared/lib`.
2. Using only relative path navigation (no absolute paths starting with `/`), navigate from `~/projects/alpha/src` to `~/projects/beta/docs` in a single `cd` command. Verify with `pwd`.
3. From `~/projects/shared/lib`, create a file named `README.txt` in `~/projects/alpha/docs` using a relative path in the `touch` command — without changing your current directory. Verify with `ls ~/projects/alpha/docs`.

### Reflection Questions

1. The `/proc` filesystem contains no actual files on disk — its contents are generated dynamically by the kernel. What does this tell you about the Linux design philosophy of "everything is a file"? Give one practical benefit this approach provides to sysadmins.
2. You used both `cp -r` and `mv` to handle directories in this lab. In a real backup scenario, when would you choose `cp` over `mv`, and what would be the consequence of accidentally using `mv` instead of `cp` when backing up critical configuration files?
