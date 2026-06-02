# Reading Guide: Module 02 - File System Hierarchy and Navigation Commands

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 02. This reading guide expands on both video parts and provides the reference
material you need for the quiz, lab, and certification exam. The Linux filesystem hierarchy and
navigation commands form the foundation that every subsequent module builds on. If you cannot
move around the filesystem confidently, everything else becomes harder.

---

### 1. High-Yield Glossary

**Filesystem Hierarchy Standard (FHS):** A specification defining the directory structure and
directory contents in Linux distributions. Maintained by the Linux Foundation. Ensures that
software and administrators can predict where files are located regardless of the distribution.

**Absolute Path:** A path that begins with a forward slash (/) and describes the complete route
from the root of the filesystem to the target. Absolute paths work from any current directory.
Example: /var/log/syslog

**Relative Path:** A path that does not begin with a slash and is interpreted starting from the
current working directory. Example: from /var, the relative path log/syslog reaches /var/log/syslog.

**Working Directory:** The directory you are currently positioned in. Shown by the pwd command.
Referenced as a dot (.) in paths. Parent directory is referenced as two dots (..).

**Inode:** A data structure on disk storing metadata about a file: permissions, ownership,
timestamps, and the disk block locations of the file's data. Every file and directory has an inode.
File names are actually just directory entries pointing to inodes.

**Hard Link:** A second directory entry pointing to the same inode as an existing file. Both
directory entries are equally valid paths to the same data. Deleting one does not remove the data
until all hard links are removed. Hard links cannot span filesystems.

**Symbolic Link (Symlink):** A file that contains the path to another file or directory. It is
a pointer, not a duplicate. If the target is deleted, the symlink becomes broken. Symlinks can
span filesystems and can point to directories.

**File Descriptor:** An integer handle the kernel assigns when a file is opened. Standard input
is fd 0, standard output is fd 1, standard error is fd 2. Redirection operators work with these
numbers.

**Pipe:** The | character sends stdout from one command as stdin to the next. Enables command
chaining where each command filters or transforms the data stream.

**Globbing:** Shell expansion of wildcard patterns (* ? []) into matching filenames before a
command is executed. The shell does the expansion, not the command itself.

**man Page:** Built-in manual page for a command, file format, or system call. Section 1 = user
commands, section 5 = file formats, section 8 = administrative commands. Access with man command.
Search all sections with man -k keyword or the apropos command.

---

### 2. FHS Directory Quick Reference

| Directory | Purpose | Critical Files or Subdirs |
|-----------|---------|--------------------------|
| / | Filesystem root | All paths begin here |
| /bin | Essential user binaries | ls, cp, mv, cat, bash |
| /sbin | System admin binaries | fdisk, iptables, fsck |
| /etc | System-wide configuration | /etc/passwd, /etc/fstab, /etc/ssh/ |
| /home | User home directories | /home/username |
| /root | Root user home | Not in /home |
| /var | Variable runtime data | /var/log, /var/spool, /var/lib |
| /var/log | System and service logs | syslog, auth.log, secure |
| /tmp | Temporary files | World-writable; may clear on reboot |
| /proc | Virtual: kernel/process info | /proc/cpuinfo, /proc/meminfo |
| /sys | Virtual: hardware/driver info | /sys/class/net, /sys/block |
| /dev | Device files | /dev/sda, /dev/null, /dev/tty |
| /boot | Kernel and bootloader | vmlinuz, initrd, grub.cfg |
| /lib | Shared libraries | .so files for /bin and /sbin |
| /usr | Secondary hierarchy | /usr/bin, /usr/lib, /usr/share |
| /usr/local | Locally installed software | Admin-compiled programs |
| /opt | Optional third-party software | /opt/splunk, /opt/java |
| /mnt | Manual temporary mounts | Admin-chosen mount points |
| /media | Auto-mounted removable media | USB drives, CD-ROMs |
| /srv | Service data | Web content, FTP data |
| /run | Runtime data since boot | PID files, lock files |

---

### 3. Navigation and File Management Command Reference

| Command | Syntax | Purpose |
|---------|--------|---------|
| pwd | pwd | Print working directory (absolute path) |
| cd | cd /path | Change directory to absolute path |
| cd | cd ../ | Move up one directory level |
| cd | cd ~ | Go to current user's home directory |
| cd | cd - | Go to previous directory |
| ls | ls -l | Long format listing |
| ls | ls -a | Include hidden (dot) files |
| ls | ls -lah | Long, all, human-readable sizes |
| ls | ls -lt | Sort by modification time |
| ls | ls -lS | Sort by file size |
| mkdir | mkdir dirname | Create directory |
| mkdir | mkdir -p path/to/dir | Create full path, no error if exists |
| touch | touch file.txt | Create empty file or update timestamp |
| cp | cp src dest | Copy file |
| cp | cp -r src/ dest/ | Copy directory recursively |
| mv | mv src dest | Move or rename |
| rm | rm file | Remove file |
| rm | rm -r dir/ | Remove directory recursively |
| rm | rm -f file | Force remove without prompt |
| cat | cat file | Print entire file to stdout |
| less | less file | Page through file (q to quit) |
| head | head -n 20 file | Show first 20 lines |
| tail | tail -n 20 file | Show last 20 lines |
| tail | tail -f file | Follow file in real time |
| file | file filename | Determine file type |
| stat | stat filename | Detailed inode metadata |
| wc | wc -l file | Count lines in file |

---

### 4. Search Command Reference

| Command | Syntax | Notes |
|---------|--------|-------|
| find | find /path -name "pattern" | Real-time search by name |
| find | find / -type f -name "*.conf" | Find only regular files |
| find | find / -type d -name "log" | Find only directories |
| find | find /home -size +10M | Files larger than 10 MB |
| find | find /var -mtime -7 | Modified within 7 days |
| find | find /tmp -type f -exec rm {} \; | Execute command on results |
| find | find / -perm 777 | Files with permission 777 |
| locate | locate filename | Fast database search |
| updatedb | sudo updatedb | Rebuild locate database |
| grep | grep "pattern" file | Search file contents |
| grep | grep -i "pattern" file | Case-insensitive search |
| grep | grep -r "pattern" /dir/ | Recursive directory search |
| grep | grep -n "pattern" file | Show line numbers |
| grep | grep -v "pattern" file | Show non-matching lines |
| grep | grep -c "pattern" file | Count matching lines |
| which | which command | Show full path of command |
| whereis | whereis command | Show binary, source, man paths |

---

### 5. Redirection and Pipe Reference

| Operator | Meaning | Example |
|----------|---------|---------|
| > | Redirect stdout, overwrite | ls > list.txt |
| >> | Redirect stdout, append | ls >> list.txt |
| < | Redirect file to stdin | sort < unsorted.txt |
| 2> | Redirect stderr, overwrite | find / -name x 2> /dev/null |
| 2>> | Redirect stderr, append | command 2>> error.log |
| 2>&1 | Redirect stderr to stdout destination | cmd > out.log 2>&1 |
| &> | Redirect both stdout and stderr | cmd &> all.log |
| pipe | Send stdout to next command stdin | ps aux \| grep nginx |

---

### 6. Log File Locations by Distribution

| Log File | Debian/Ubuntu Path | RHEL/CentOS Path |
|----------|-------------------|-----------------|
| Authentication events | /var/log/auth.log | /var/log/secure |
| General system messages | /var/log/syslog | /var/log/messages |
| Kernel messages | /var/log/kern.log | /var/log/messages |
| Boot log | /var/log/boot.log | /var/log/boot.log |
| Package manager | /var/log/dpkg.log | /var/log/dnf.log |
| Cron jobs | /var/log/cron.log | /var/log/cron |

---

### 7. Wildcard Globbing Reference

| Pattern | Matches |
|---------|---------|
| * | Any sequence of zero or more characters |
| ? | Any single character |
| [abc] | Any single character from the set: a, b, or c |
| [a-z] | Any single lowercase letter |
| [0-9] | Any single digit |
| [^abc] | Any single character NOT in the set |
| {a,b,c} | Brace expansion: generates each item separately |

---

### 8. CompTIA Linux+ Exam Tips

**Exam Tip 1:** The exam distinguishes between find and locate. If the question asks for real-time
accuracy or searching for a recently created file, the answer is find. If the question asks for
the fastest search tool or mentions a pre-built index, the answer is locate.

**Exam Tip 2:** Know the path difference: /var/log/secure is RHEL. /var/log/auth.log is Ubuntu.
Questions may present one as a wrong answer for the other platform.

**Exam Tip 3:** The /proc directory is virtual, held entirely in RAM. Nothing in /proc is written
to disk. It is created fresh at each boot by the kernel.

**Exam Tip 4:** The root user's home directory is /root. It is NOT /home/root. This is a tested
distractor.

**Exam Tip 5:** 2>&1 is a common exam question. It means "redirect file descriptor 2 (stderr)
to the same destination as file descriptor 1 (stdout)." The order matters: stdout must be
redirected first.

**Exam Tip 6:** grep -v inverts the match. grep -c counts matches. grep -n shows line numbers.
grep -r searches recursively. grep -i is case-insensitive. Know all of these flags.

**Exam Tip 7:** find -type f finds regular files. find -type d finds directories. find -type l
finds symbolic links. find -mtime -1 means "within the last day." find -size +1M means "larger
than 1 megabyte."

**Exam Tip 8:** mkdir -p creates parent directories as needed. Without -p, if you try
mkdir /a/b/c and /a/b does not exist, the command fails.

---

### 9. Study Checklist

- [ ] Watch both parts of the Module 02 video lecture
- [ ] Memorize all glossary terms and their definitions
- [ ] Review the FHS directory reference table and understand each directory's purpose
- [ ] Practice all navigation commands in your Ubuntu Server VM
- [ ] Practice find with -name, -type, -size, -mtime, and -exec options
- [ ] Practice grep with -i, -r, -n, -v, and -c options
- [ ] Practice output redirection with >, >>, 2>, and 2>&1
- [ ] Complete the Module 02 Lab
- [ ] Complete the Module 02 Quiz
- [ ] Post to the Discussion by Wednesday at 11:59 PM
- [ ] Reply to two classmates by Sunday at 11:59 PM

---

### Required Reading

Read chapters 3 through 7 of The Linux Command Line by William Shotts, available at
linuxcommand.org/tlcl.php. These chapters cover navigation, file manipulation, working with
commands, redirections, and keyboard shortcuts.
