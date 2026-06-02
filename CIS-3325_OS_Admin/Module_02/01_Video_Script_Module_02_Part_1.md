# Video Script: Module 02 - File System Hierarchy and Navigation Commands (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 14 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 02. If Module 01 was about getting Linux running, Module 02 is about learning
to move around inside it. The Linux filesystem is the map of your entire system. Every file,
every configuration, every log, every device is somewhere on this map. If you do not understand
the map, you will be lost every time something goes wrong.

By the end of both parts you will be able to navigate the full Linux filesystem hierarchy, use
absolute and relative paths, find files using multiple tools, and understand why Linux structures
its directories the way it does.

---

### Section 1: The Linux Filesystem as a Single Tree

The most important mental model shift for students coming from Windows is this: Linux has one
tree. There are no drive letters. Everything attaches to a single root.

In Windows you have C:\, D:\, E:\ - each drive is its own separate tree. In Linux the root
is a forward slash. Everything hangs below it. Additional disks, network shares, USB drives -
they all attach (mount) to a directory within the single tree.

[SHOW TERMINAL]

```bash
ls /
```

What you see here is the top level of the entire filesystem. Every single file on this system
is reachable from this point. When you plug in a USB drive, it might appear at /media/labadmin/
or /mnt/usb. When the system mounts a network share, it appears at /mnt/nfs or wherever the
administrator chose to mount it.

This design has major advantages. Scripts that reference /var/log/syslog work on every Linux
system regardless of what physical disk that log is on. The path is stable even if the storage
changes underneath.

---

### Section 2: Why Each Directory Exists

The Filesystem Hierarchy Standard defines the purpose of each top-level directory. Understanding
why each one exists helps you know where to look when something goes wrong.

[SHOW TERMINAL]

Let us walk through the critical ones.

```bash
ls /bin
```

/bin contains essential user binaries. These are the programs every user needs, like ls, cp, mv,
cat, and echo. On modern Ubuntu systems /bin is actually a symbolic link to /usr/bin, which is
the primary location for user commands on current systems.

```bash
ls /etc
```

/etc contains all system-wide configuration files. When you configure the SSH daemon, you edit
/etc/ssh/sshd_config. When you configure the network, you might edit files in /etc/netplan/ on
Ubuntu. Nothing in /etc is an executable. It is pure configuration.

```bash
ls /var/log
```

/var stands for variable. This directory holds data that changes during normal system operation.
The most important subdirectory is /var/log, which contains system log files. When you are
troubleshooting a service failure, /var/log is where you look first.

```bash
ls /home
```

/home contains one subdirectory per user account. When you create a user account for alice, the
system creates /home/alice. That is alice's personal space where she owns all her files.

```bash
ls /proc
```

/proc is special. It looks like a directory full of files but nothing here is stored on disk.
The kernel generates this content entirely in RAM at runtime. Each running process has a numbered
directory here. /proc/1 is the init process. /proc/cpuinfo shows processor details. /proc/meminfo
shows memory statistics.

---

### Section 3: Absolute Paths vs Relative Paths

This is one of the most tested concepts on the Linux+ exam.

An absolute path always starts with a forward slash. It describes the complete route from the
root of the filesystem to the target file or directory. Absolute paths work from anywhere.

A relative path does not start with a forward slash. It describes the route from your current
directory to the target. Relative paths only make sense in context.

[SHOW TERMINAL]

```bash
pwd
```

pwd stands for print working directory. It always gives you an absolute path showing exactly
where you are right now. If this shows /home/labadmin, then:

The absolute path to your bash history file is /home/labadmin/.bash_history

The relative path from your current location is just .bash_history (or ./.bash_history)

Let us practice navigating.

```bash
cd /var/log
pwd
ls
```

We used an absolute path to jump directly to /var/log regardless of where we were before.

```bash
cd ..
pwd
```

Two dots (..) means the parent directory. We just moved up one level to /var.

```bash
cd ../etc
pwd
```

This relative path means: go up one level (to /) then descend into etc. Now we are at /etc.

---

### Section 4: The Home Directory Shortcut

[SHOW TERMINAL]

The tilde character (~) is a special shortcut in bash. It always expands to the current user's
home directory.

```bash
cd ~
pwd
```

This takes you to /home/labadmin (or whatever your home directory is).

```bash
cd ~/Documents
```

This is equivalent to typing the full absolute path /home/labadmin/Documents.

When you open a new terminal, the shell always starts you in your home directory. That is why
the prompt often shows a tilde - you are at home.

The root user's home directory is /root, not /home/root. This is a common exam distractor.

---

### Section 5: Creating, Moving, Copying, and Deleting Files

[SHOW TERMINAL]

Let us build some working vocabulary with file manipulation commands.

```bash
mkdir practice
cd practice
touch file1.txt file2.txt file3.txt
ls -l
```

mkdir creates a directory. touch creates an empty file if it does not exist (or updates the
timestamp if it does). ls -l shows the long listing with permissions, owner, size, and date.

```bash
cp file1.txt backup_file1.txt
ls -l
```

cp copies a file. The syntax is cp source destination. The original file remains.

```bash
mv file2.txt renamed_file2.txt
ls -l
```

mv moves or renames a file. If source and destination are in the same directory, it renames.
If destination is a different path, it moves the file there.

```bash
rm file3.txt
ls -l
```

rm removes (deletes) a file. There is no Recycle Bin in Linux. When you rm a file at the
terminal, it is gone. Be careful.

```bash
rm -r practice/
```

The -r flag means recursive. You need it to remove a directory and everything inside it.
Use rm -r with caution.

---

### Section 6: Viewing File Contents

[SHOW TERMINAL]

Several commands display file contents. Each has a different use case.

```bash
cat /etc/os-release
```

cat (concatenate) outputs the entire file to the terminal at once. Best for short files.

```bash
less /var/log/syslog
```

less opens a file in a pager that lets you scroll up and down. Press q to quit, / to search
forward, n to jump to the next match, and G to jump to the end. Use less for large log files.

```bash
head -20 /var/log/syslog
```

head shows the first 20 lines. Default without the -n flag is 10 lines.

```bash
tail -20 /var/log/syslog
```

tail shows the last 20 lines. The most powerful use of tail is:

```bash
tail -f /var/log/syslog
```

The -f flag follows the file in real time, printing new lines as they are written. This is
invaluable for watching a service log as you troubleshoot a connection issue. Press Ctrl+C to stop.

---

### Section 7: Hidden Files and the ls Command

[SHOW TERMINAL]

Files in Linux are hidden when their name starts with a dot. The dot at the beginning of the
name is the only mechanism for hiding a file. There is no hidden attribute like Windows.

```bash
ls ~
ls -a ~
```

The -a flag in ls shows all files including hidden ones. You will now see files like
.bashrc, .bash_history, .profile, and .ssh. These are configuration files for the shell and
other applications, kept out of the way in your home directory.

```bash
ls -la ~
```

Combining -l and -a gives you the long listing showing all files including hidden ones.
This is one of the most commonly used forms of ls in real administration work.

---

### Section 8: Key ls Options Reference

The ls command has many useful options. Know these for the exam.

| Option | Meaning |
|--------|---------|
| -l | Long format: permissions, owner, size, date |
| -a | All files including hidden dot-files |
| -h | Human-readable sizes (1K, 5M, 2G) |
| -R | Recursive: list subdirectories too |
| -t | Sort by modification time, newest first |
| -r | Reverse sort order |
| -S | Sort by file size, largest first |
| -i | Show inode number |

Combining these: ls -lah shows a long listing of all files with human-readable sizes.

---

### Certification Connection

Module 02 topics appear throughout the Linux+ exam. File navigation questions are the most
common scenario type. Key objectives tested include:

Understanding the FHS and the purpose of each major directory.

Distinguishing absolute from relative paths.

Using ls, cd, pwd, cp, mv, rm, mkdir, cat, less, head, and tail.

Understanding dot-file naming convention for hidden files.

---

### Transition to Part 2

In Part 2 we will cover the find and locate commands for searching the filesystem, grep for
searching inside files, file links, and the exam-critical topic of piping commands together.
Take a break and continue to Part 2.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
