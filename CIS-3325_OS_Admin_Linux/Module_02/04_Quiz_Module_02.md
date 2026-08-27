# Quiz: Module 02 — Linux Installation and System Navigation

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question has one correct answer. Read the distractor analysis after each question to understand why the incorrect options fail — this analysis directly supports your Linux+ exam preparation.

---

### Question 1

A system administrator needs to install Linux on a server with a 4 TB hard drive. Which firmware type and partitioning scheme is required?

A. BIOS with MBR
B. BIOS with GPT
C. UEFI with MBR
D. UEFI with GPT

**Correct Answer: D**

**Distractor Analysis**:

- **A (BIOS with MBR)** is incorrect. MBR supports a maximum disk size of 2 TB. A 4 TB disk cannot be fully used with MBR.
- **B (BIOS with GPT)** is incorrect. While GPT supports large disks, BIOS systems have limited GPT support and the combination is not standard for new installations. The correct pairing is UEFI with GPT.
- **C (UEFI with MBR)** is incorrect. UEFI can technically boot from MBR, but MBR's 2 TB disk size limit still applies. This combination does not solve the problem.
- **D (UEFI with GPT)** is correct. UEFI is the modern firmware standard, and GPT supports disks up to 9.4 ZB. This is the required combination for disks larger than 2 TB.

---

### Question 2

A Linux administrator wants to see all files in the current directory, including hidden files, with detailed information and human-readable file sizes. Which command should be used?

A. `ls -l`
B. `ls -la`
C. `ls -lah`
D. `ls -R`

**Correct Answer: C**

**Distractor Analysis**:

- **A (`ls -l`)** is incorrect. Long format shows detailed information but does not show hidden files and shows sizes in bytes, not human-readable format.
- **B (`ls -la`)** is incorrect. This shows hidden files and long format, but sizes are still in bytes, not human-readable.
- **C (`ls -lah`)** is correct. `-l` gives long format, `-a` includes hidden files, and `-h` converts sizes to KB/MB/GB.
- **D (`ls -R`)** is incorrect. `-R` is recursive listing — it shows all files in all subdirectories. It does not affect hidden file visibility or size formatting.

---

### Question 3

An administrator's current directory is `/home/student`. They run the command `cd ../..`. What is the new working directory?

A. `/home`
B. `/home/student`
C. `/`
D. `/home/student/..`

**Correct Answer: C**

**Distractor Analysis**:

- **A (`/home`)** is incorrect. `cd ..` once would take you to `/home`. The command uses `../..` — two levels up.
- **B (`/home/student`)** is incorrect. Running `cd ../..` from the home directory moves up two levels, not zero.
- **C (`/`)** is correct. From `/home/student`, `..` is `/home`, and `../..` is `/` (the root). Running `cd ../..` moves up two directory levels to the filesystem root.
- **D (`/home/student/..`)** is a malformed path representation, not a valid answer. Path components are resolved before navigation — `..` is always the parent directory.

---

### Question 4

Which of the following is an absolute path?

A. `./config`
B. `../etc/passwd`
C. `documents/notes.txt`
D. `/var/log/syslog`

**Correct Answer: D**

**Distractor Analysis**:

- **A (`./config`)** is incorrect. The leading `./` means "current directory" — this is a relative path.
- **B (`../etc/passwd`)** is incorrect. Starting with `../` means "parent directory" — this is a relative path.
- **C (`documents/notes.txt`)** is incorrect. This has no leading `/` — it is relative to wherever you currently are.
- **D (`/var/log/syslog`)** is correct. An absolute path always starts with `/` (the root). This path is unambiguous regardless of the current working directory.

---

### Question 5

An administrator needs to copy the directory `/home/student/project` and all of its contents to `/backup/project`. Which command accomplishes this?

A. `cp /home/student/project /backup/project`
B. `cp -r /home/student/project /backup/project`
C. `mv /home/student/project /backup/project`
D. `cp -p /home/student/project /backup/project`

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect. Without `-r`, `cp` only copies individual files — it will fail or skip the directory and its contents.
- **B** is correct. The `-r` (recursive) flag is required to copy a directory and all files within it to a new location.
- **C** is incorrect. `mv` moves (cuts) the directory rather than copying it. The original would no longer exist at `/home/student/project`.
- **D** is incorrect. `-p` preserves file attributes (timestamps, permissions) during copy, but without `-r` it still will not copy directory contents.

---

### Question 6

A system administrator needs to create the directory structure `/data/projects/2024/reports` where no parent directories currently exist. Which command creates the entire structure in one step?

A. `mkdir /data/projects/2024/reports`
B. `mkdir -p /data/projects/2024/reports`
C. `mkdir -r /data/projects/2024/reports`
D. `mkdirs /data/projects/2024/reports`

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect. Without `-p`, `mkdir` fails if any parent directory in the path does not already exist. Since `/data` does not exist, this command would error.
- **B** is correct. The `-p` flag creates all necessary parent directories and does not fail if they already exist.
- **C** is incorrect. There is no `-r` flag for `mkdir`. This command would fail with an invalid option error.
- **D** is incorrect. `mkdirs` is not a standard Linux command. The correct command is `mkdir`.

---

### Question 7

An administrator runs `rm -rf /var/log/oldlogs/`. What is the result?

A. The command fails because `rm` requires confirmation for directories.
B. The command prompts for confirmation before deleting each file.
C. The entire `oldlogs` directory and all of its contents are permanently deleted without prompting.
D. The files are moved to the system trash for later review.

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect. With `-r` (recursive), `rm` can delete directories. Without `-r` it would fail, but `-r` is provided here.
- **B** is incorrect. The `-i` flag triggers prompting. The `-f` (force) flag explicitly suppresses all prompts and does the opposite.
- **C** is correct. `-r` enables recursive deletion of directory contents. `-f` suppresses all prompts and does not fail on missing files. Together they silently and permanently delete everything.
- **D** is incorrect. Linux does not have a system trash for command-line `rm` operations. Files deleted with `rm` are immediately unlinked from the filesystem and cannot be recovered without specialized forensic tools.

---

### Question 8

Which command determines the type of the file `/usr/bin/grep` based on its content rather than its name?

A. `which /usr/bin/grep`
B. `whereis grep`
C. `type grep`
D. `file /usr/bin/grep`

**Correct Answer: D**

**Distractor Analysis**:

- **A (`which`)** is incorrect. `which grep` returns the path to the grep executable in your PATH. It does not examine file content to determine file type.
- **B (`whereis grep`)** is incorrect. `whereis` locates the binary, source, and man page. It does not examine file content to determine type.
- **C (`type grep`)** is partially useful — it tells you whether grep is a built-in, alias, or external command — but it does not read file content to determine file type the way `file` does.
- **D (`file /usr/bin/grep`)** is correct. `file` reads the content (magic bytes) of a file and reports its type — for a binary like grep it would output something like "ELF 64-bit LSB pie executable."

---

### Question 9

A server is being configured with a separate `/var` partition. What is the primary administrative benefit of this partition layout decision?

A. It prevents users from accessing system log files.
B. It allows the `/var` partition to use a different filesystem type than `/`.
C. It prevents log files and application data from filling the root filesystem and crashing system services.
D. It improves the read performance of the root filesystem.

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect. Partitioning `/var` separately does not change file permissions or user access to log files. Access control is separate from partition layout.
- **B** is technically possible but not the primary reason — and in practice the same filesystem type is typically used for all partitions.
- **C** is correct. `/var` holds logs, databases, package caches, and mail queues — all of which can grow unpredictably. If these fill up the root filesystem, system services that need to write to `/` will fail. Isolating `/var` on its own partition means a runaway log only fills `/var`, not root.
- **D** is incorrect. Partitioning does not inherently improve read performance. The same physical disk is still used.

---

### Question 10

An administrator wants to look at the manual page for the `/etc/fstab` file format (not the `fstab` command). Which command opens the correct man page section?

A. `man fstab`
B. `man 1 fstab`
C. `man 5 fstab`
D. `man 8 fstab`

**Correct Answer: C**

**Distractor Analysis**:

- **A (`man fstab`)** opens the default man page for fstab. On most systems this defaults to section 5 — but specifying the section explicitly is correct practice and is what the exam expects.
- **B (`man 1 fstab`)** is incorrect. Section 1 covers user commands. `fstab` is a file format, not a user command.
- **C (`man 5 fstab`)** is correct. Man page section 5 covers file formats and configuration files. `/etc/fstab` is a configuration file, so its format documentation lives in section 5.
- **D (`man 8 fstab`)** is incorrect. Section 8 covers system administration commands (like `mount`, `fdisk`). `fstab` is not a command.

---

### Question 11 (5 points)

Which of the following commands renames the file `report.txt` to `report_final.txt` in the same directory?

A. `cp report.txt report_final.txt`
B. `mv report.txt report_final.txt`
C. `rename report.txt report_final.txt`
D. `ln report.txt report_final.txt`

**Correct Answer: B**

**Distractor Analysis**:

- **A (cp)** is incorrect. `cp` creates a copy — both `report.txt` and `report_final.txt` would exist afterward. This is not a rename.
- **B (mv)** is correct. `mv` is used both to move files to different locations and to rename files within the same directory. After this command, only `report_final.txt` exists.
- **C (rename)** is a valid utility on some systems but is not the standard command for a simple single-file rename. The `rename` utility uses regex patterns and is not universally available. `mv` is the standard answer.
- **D (ln)** is incorrect. `ln` creates hard links, not renames. Both the original and the new name would point to the same file data — no rename occurs.

---

### Question 12 (5 points)

A sysadmin runs `ls -l /home/student` and sees a file entry beginning with `l`. What type of file is this?

A. A locked file that cannot be read.
B. A large file exceeding 1 GB.
C. A symbolic link.
D. A Linux kernel module.

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect. There is no "locked" file type indicator in Linux permissions. File locking is handled through `flock` or application-level mechanisms, not indicated by the file type character.
- **B** is incorrect. File size is shown as a number in the fifth column of `ls -l` output, not as a letter in the permissions string.
- **C** is correct. In `ls -l` output, the first character of the permissions string indicates file type: `-` = regular file, `d` = directory, `l` = symbolic link, `b` = block device, `c` = character device.
- **D** is incorrect. Kernel modules have a `.ko` extension and are regular files (shown as `-`). There is no distinct file type indicator for kernel modules in `ls -l`.

---

### Question 13 (5 points)

What is the purpose of `touch filename.txt` when `filename.txt` does not already exist?

A. It verifies the file is accessible and prints its metadata.
B. It creates an empty file with the specified name.
C. It sets the file's content to a single newline character.
D. It locks the file to prevent modification.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect. The `stat` command displays file metadata. `touch` does not display information — it creates or modifies.
- **B** is correct. When used on a non-existent file, `touch` creates an empty file (zero bytes) with the current timestamp. When used on an existing file, it updates the access and modification timestamps.
- **C** is incorrect. `touch` creates a truly empty file — zero bytes. It does not write any content, not even a newline.
- **D** is incorrect. `touch` has no locking capability. File locking is a separate operating system mechanism.

---

### Question 14 (5 points)

An administrator needs to determine whether the disk partition `/dev/sdb1` has been formatted with ext4 or XFS. Which command provides this information?

A. `file /dev/sdb1`
B. `blkid /dev/sdb1`
C. `ls -l /dev/sdb1`
D. `cat /dev/sdb1`

**Correct Answer: B**

**Distractor Analysis**:

- **A** is partially useful but not optimal — `file /dev/sdb1` may return "block special" without the filesystem type. `blkid` is the correct specialized tool for this purpose.
- **B** is correct. `blkid` reads the filesystem superblock and reports the UUID, filesystem type (`TYPE=`), and other block device attributes. It is the standard command for identifying what filesystem is on a partition.
- **C** is incorrect. `ls -l /dev/sdb1` shows the device node metadata (permissions, major/minor numbers) but not the filesystem type.
- **D** is incorrect and dangerous. `cat /dev/sdb1` reads raw binary data from the partition and would produce garbage output on the terminal. It does not identify filesystem type.

---

### Question 15 (5 points)

Which of the following partitioning schemes supports Secure Boot and is required for disks larger than 2 TB?

A. MBR
B. GPT with BIOS
C. GPT with UEFI
D. LVM with MBR

**Correct Answer: C**

**Distractor Analysis**:

- **A (MBR)** is incorrect. MBR is limited to 2 TB disks and 4 primary partitions. It does not support Secure Boot.
- **B (GPT with BIOS)** is incorrect. While technically possible, this combination does not support Secure Boot. Secure Boot is a UEFI feature.
- **C (GPT with UEFI)** is correct. UEFI is required for Secure Boot support, and GPT is required for disks larger than 2 TB. This combination is the modern standard for new server deployments.
- **D (LVM with MBR)** is incorrect. LVM (Logical Volume Manager) is a disk abstraction layer, not a partitioning scheme. MBR still cannot address disks larger than 2 TB regardless of LVM.

---

### Question 16 (5 points)

A Linux administrator runs `cp -rp /etc/nginx /backup/nginx_backup`. What does the `-p` flag add to this operation?

A. It creates parent directories if they do not exist.
B. It copies the directory recursively.
C. It preserves the original file permissions, ownership, and timestamps.
D. It prints each file name as it is copied.

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect. Creating parent directories is the function of `mkdir -p`. In `cp`, `-p` means "preserve."
- **B** is incorrect. Recursive copying is done by `-r`. In this command, `-r` is already handling the recursive copy.
- **C** is correct. The `-p` flag in `cp` preserves file attributes: mode (permissions), ownership, and timestamps. This is important for backups where you need the copied files to retain their original metadata.
- **D** is incorrect. Verbose output (printing each file) is done with the `-v` flag in `cp`.

---

### Question 17 (5 points)

An administrator wants to list all files under `/var/log` and all of its subdirectories in a single command. Which flag enables this?

A. `ls -a /var/log`
B. `ls -l /var/log`
C. `ls -R /var/log`
D. `ls -h /var/log`

**Correct Answer: C**

**Distractor Analysis**:

- **A (`-a`)** is incorrect. The `-a` flag shows hidden files (those starting with `.`) in the current directory listing. It does not recurse into subdirectories.
- **B (`-l`)** is incorrect. The `-l` flag produces long-format output with metadata. It does not recurse into subdirectories.
- **C (`-R`)** is correct. The `-R` (uppercase) flag makes `ls` recursive — it lists the contents of all subdirectories within the target path.
- **D (`-h`)** is incorrect. The `-h` flag makes file sizes human-readable (KB, MB, GB). It does not enable directory recursion.

---

### Question 18 (5 points)

Which directory contains configuration files for system-wide services and applications on a Linux system?

A. `/bin`
B. `/var`
C. `/etc`
D. `/usr`

**Correct Answer: C**

**Distractor Analysis**:

- **A (`/bin`)** is incorrect. `/bin` (or `/usr/bin` on modern systems) contains essential user command binaries like `ls`, `cp`, and `bash`. Configuration files are not stored here.
- **B (`/var`)** is incorrect. `/var` contains variable data that changes during system operation: logs (`/var/log`), mail, databases, and package manager caches. Not static configuration files.
- **C (`/etc`)** is correct. By the Filesystem Hierarchy Standard, `/etc` is the directory for all system-wide configuration files and startup scripts. Examples include `/etc/fstab`, `/etc/hosts`, `/etc/passwd`, and `/etc/nginx/nginx.conf`.
- **D (`/usr`)** is incorrect. `/usr` contains read-only user programs and data — binaries, libraries, and documentation. Application configuration generally lives in `/etc`.

---

### Question 19 (5 points)

A sysadmin wants to remove the directory `/tmp/testdir` which is empty. Which command is the most appropriate?

A. `rm /tmp/testdir`
B. `rm -r /tmp/testdir`
C. `rmdir /tmp/testdir`
D. `rm -rf /tmp/testdir`

**Correct Answer: C**

**Distractor Analysis**:

- **A** is incorrect. `rm` without flags cannot remove directories — it will return an error.
- **B** is technically correct for removing directories but `rmdir` is the more appropriate and safer command when the directory is known to be empty.
- **C** is correct. `rmdir` removes an empty directory. It will fail with an error if the directory contains any files, providing a built-in safety check. It is the appropriate tool when you know the directory is empty.
- **D** is incorrect as the best answer. While `rm -rf` would work, it is dangerous and excessive for removing a known-empty directory. Using `rmdir` is the safe, specific-purpose command.

---

### Question 20 (5 points)

What does the command `man 5 passwd` open?

A. The manual page for the `passwd` command used to change passwords.
B. The manual page section describing the format of the `/etc/passwd` file.
C. The fifth page of the `passwd` manual entry.
D. A list of the five most important flags for the `passwd` command.

**Correct Answer: B**

**Distractor Analysis**:

- **A** is incorrect. `man passwd` or `man 1 passwd` opens the documentation for the `passwd` command. Section 1 covers user commands.
- **B** is correct. Man page section 5 documents file formats and configuration files. `/etc/passwd` is a configuration file, so `man 5 passwd` describes its format: field separators, field meanings, and the structure of each line.
- **C** is incorrect. The number in `man <section> <topic>` is a section number, not a page number. There is no "page 5" concept.
- **D** is incorrect. The section number does not filter or count flags. Man pages for commands include all flags in section 1.

---

### Answer Key

| Question | Answer |
|---|---|
| 1 | D |
| 2 | C |
| 3 | C |
| 4 | D |
| 5 | B |
| 6 | B |
| 7 | C |
| 8 | D |
| 9 | C |
| 10 | C |
| 11 | B |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | C |
| 16 | C |
| 17 | C |
| 18 | C |
| 19 | C |
| 20 | B |
