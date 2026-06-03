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
