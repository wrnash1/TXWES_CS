# Video Script: Module 02 — Linux Installation and System Navigation (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## [INTRO — 0:00–0:45]

Welcome to Module 2, Part 2. In Part 1 we covered the installation process — ISO creation, BIOS/UEFI, partitioning, and filesystem types. Now we navigate. The commands in this part are the ones you will use every single day as a Linux administrator. They are also heavily tested on the Linux+ exam. We will cover `pwd`, `ls`, `cd`, `mkdir`, `rmdir`, `touch`, `cp`, `mv`, `rm`, `file`, `which`, `whereis`, and how to use `man` pages.

Open your VM and follow along. Typing these commands yourself, not just watching, is what builds the muscle memory you need for performance-based exam questions.

---

## [SECTION 1 — pwd, ls, and cd — 0:45–4:00]

### pwd — Print Working Directory

`pwd` tells you where you are in the filesystem. When you log in, you start in your home directory. Run `pwd` and it will show `/home/student` (or whatever your username is).

```bash
pwd
```

Output: `/home/student`

The tilde (`~`) in your prompt is shorthand for your home directory. `cd ~` always takes you home.

### ls — List Directory Contents

`ls` is one of the most used commands in Linux. By itself it lists files and directories in the current location, excluding hidden files.

```bash
ls
```

The most important flags:

`-l` — long format. Shows permissions, link count, owner, group, size, modification date, and name. Know this format cold for the exam.

`-a` — all files. Shows hidden files — those whose names start with a dot. Your home directory contains several hidden configuration files like `.bashrc` and `.bash_history`.

`-h` — human-readable. When used with `-l`, shows file sizes in KB, MB, or GB instead of raw bytes.

`-R` — recursive. Lists the contents of the current directory and all subdirectories. Useful for getting a full picture of a directory tree.

Combine flags: `ls -lah` gives you long format, all files, human-readable sizes. `ls -la` is the most commonly used combination.

```bash
ls -la
ls -lah /var/log
ls -R /etc
```

In the long format output, the first character of the permissions string tells you the file type: `-` is a regular file, `d` is a directory, `l` is a symbolic link. We cover the full permissions column in Module 4.

### cd — Change Directory

`cd` moves you to a different directory.

```bash
cd /etc
pwd
```

Now you are in `/etc`. To go back to your home directory:

```bash
cd ~
```

Or simply:

```bash
cd
```

Running `cd` with no argument always takes you home.

To go up one level in the directory tree:

```bash
cd ..
```

Two dots (`..`) always refers to the parent directory. One dot (`.`) refers to the current directory. You will see `.` used frequently in commands like `./script.sh` to run a script in the current directory.

**Absolute vs. relative paths**: An absolute path starts from the root — it always starts with `/`. Example: `/home/student/documents`. A relative path starts from the current directory. If you are in `/home/student`, then `documents` and `./documents` both refer to `/home/student/documents`. The exam tests this distinction directly.

---

## [SECTION 2 — mkdir, rmdir, touch — 4:00–6:30]

### mkdir — Make Directory

```bash
mkdir testdir
ls
```

`mkdir -p` creates parent directories as needed — it does not fail if the directory already exists:

```bash
mkdir -p projects/webserver/config
```

This creates `projects`, `projects/webserver`, and `projects/webserver/config` all at once. Without `-p`, you would need to create each directory separately.

### rmdir — Remove Directory

`rmdir` removes empty directories:

```bash
rmdir testdir
```

`rmdir` will fail if the directory contains files. To remove a directory and all its contents, use `rm -rf` — but use that with extreme caution. We cover `rm` next.

### touch — Create Empty Files

`touch` creates an empty file if the file does not exist, or updates the modification timestamp if it does:

```bash
touch myfile.txt
ls -l myfile.txt
```

You will use `touch` frequently in labs to create test files quickly without needing to put any content in them.

---

## [SECTION 3 — cp, mv, rm — 6:30–9:30]

### cp — Copy Files and Directories

Basic copy: `cp source destination`

```bash
cp myfile.txt myfile_backup.txt
```

Copy to a directory:

```bash
cp myfile.txt /tmp/
```

Copy a directory and all its contents recursively — the `-r` flag is required for directories:

```bash
cp -r projects/ projects_backup/
```

Other useful flags: `-p` preserves file attributes (timestamps, permissions), `-i` prompts before overwriting.

### mv — Move or Rename

`mv` moves a file to a different location or renames it:

```bash
mv myfile.txt renamed.txt
mv renamed.txt /tmp/
```

`mv` also works on directories without needing a `-r` flag — this is different from `cp`. If the destination is a directory, the file is moved inside it. If the destination is a new name in the same directory, the file is renamed.

### rm — Remove Files

`rm filename` deletes a file permanently. There is no trash or recycle bin. The file is gone.

```bash
rm myfile_backup.txt
```

Key flags:

`-i` — interactive mode. Prompts you to confirm before deleting each file. A good habit when working as root.

`-r` — recursive. Required to delete a directory and its contents.

`-f` — force. Suppresses prompts and does not fail on missing files.

`rm -rf` — the most dangerous common Linux command. It silently and permanently deletes a directory and everything inside it. Used with an accidental wildcard or the wrong path, it can delete your entire system. Always double-check the path before running `rm -rf`.

The exam commonly presents `rm -rf` questions where you need to identify what would be deleted or what flag is needed for a particular operation.

---

## [SECTION 4 — file, which, whereis — 9:30–11:30]

### file — Determine File Type

Linux does not rely on file extensions to determine file type — extensions are just part of the name. The `file` command reads the file's content to determine its actual type:

```bash
file /bin/bash
file /etc/passwd
file /usr/share/doc/bash/changelog.Debian.gz
```

You will see output like "ELF 64-bit LSB pie executable" (a binary), "ASCII text" (a text file), or "gzip compressed data" (a compressed file). This is useful when you encounter a file with an unfamiliar or missing extension.

### which — Find the Location of a Command

`which` searches your PATH for the executable that will be run when you type a command name:

```bash
which bash
which python3
which ls
```

Output for `which bash` is typically `/usr/bin/bash` or `/bin/bash`. If the command is not found, `which` returns nothing. This is useful for confirming which version of a tool will run — important when multiple versions are installed.

### whereis — Find Binary, Source, and Man Page

`whereis` goes further than `which` — it finds the binary, the source files, and the manual page for a command:

```bash
whereis ls
whereis bash
```

Example output: `ls: /usr/bin/ls /usr/share/man/man1/ls.1.gz` — showing both the binary location and the man page location.

---

## [SECTION 5 — man Pages and --help — 11:30–14:00]

### man — The Manual

Every command on Linux has a manual page. `man commandname` opens the full documentation for that command. This is your primary reference and it is available in the simulated environment of Linux+ performance-based questions.

```bash
man ls
man chmod
man cp
```

Navigate with the arrow keys or Page Up/Page Down. Press `/` and type a search term to search within the man page. Press `n` to jump to the next match. Press `q` to quit.

Man pages are organized into numbered sections. Section 1 covers user commands, section 5 covers file formats (like `/etc/fstab`), and section 8 covers system administration commands. If multiple sections contain a topic, specify the section: `man 5 passwd` opens the man page for the password file format rather than the `passwd` command.

### --help

Most commands accept `--help` or `-h` as a flag to print a short usage summary:

```bash
ls --help
cp --help
```

The `--help` output is faster to scan than a full man page when you just need a quick flag reference. Use man for comprehensive understanding and `--help` for quick lookups.

### Linux+ Domain Mapping for This Module

The navigation commands in this part map primarily to Linux+ Domain 1 (System Management). Specifically:

- File and directory management: `cp`, `mv`, `rm`, `mkdir`
- Filesystem navigation: `pwd`, `ls`, `cd`
- File information: `file`, `which`, `whereis`
- Documentation: `man`, `--help`

These commands appear in performance-based questions. Practice them until you can type them without thinking.

---

## [OUTRO — 14:00–15:00]

Module 2 is complete. You can now install Linux, understand the partitioning decisions made during installation, navigate the filesystem with confidence, and manage files and directories using the core set of commands that every Linux administrator uses daily.

Your Module 2 lab focuses on hands-on practice with all of these navigation commands in your VM. Do not skip it — typing these commands yourself twenty or thirty times is worth more than watching the video twice.

In Module 3, we dive deep into the Linux Filesystem Hierarchy Standard — the map of the entire Linux directory tree and what lives where. Understanding FHS will help you find configuration files, logs, and system resources without guessing. See you in Module 3.

---

## [END OF SCRIPT — PART 2]

---

### Instructor Notes

- Estimated delivery time: 14–16 minutes.
- Strongly recommend screen recording with live terminal for all command demonstrations in Sections 1–4.
- The absolute vs. relative path distinction is a frequent exam question and student confusion point — consider drawing a directory tree on screen.
- Emphasize `rm -rf` safety multiple times. Students who do not grasp this early can destroy their VMs in later labs.
