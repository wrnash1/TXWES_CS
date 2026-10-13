# Video Script: Module 02 - File System Hierarchy and Navigation Commands (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 12 minutes
**Part:** 2 of 2 - Hands-On Application

---

### Opening

Welcome back to Part 2 of Module 02. In Part 1 we built the conceptual foundation: the single-tree
filesystem, why each directory exists, absolute versus relative paths, and basic file manipulation.
Now we go hands-on with the power tools: find, locate, grep, pipes, and redirection. These are
the commands you will use every single day as a Linux administrator.

---

### Section 1: The find Command

find searches the live filesystem in real time. It does not rely on an index database. This means
it is always accurate but can be slow on very large filesystems.

The basic syntax is: find [path] [options] [expression]

[SHOW TERMINAL]

```bash
find /etc -name "sshd_config"
```

This searches the /etc directory for any file named exactly sshd_config. Notice we use quotes
around the name to prevent the shell from interpreting special characters.

```bash
find /home -name "*.txt"
```

The asterisk is a wildcard. This finds all files ending in .txt anywhere under /home.

```bash
find / -name "sshd_config" 2>/dev/null
```

The 2>/dev/null redirects error messages (stderr) to /dev/null, which discards them. You will
see this pattern constantly when running find as a non-root user because you get many
"Permission denied" errors for directories you cannot read.

```bash
find /var/log -mtime -1
```

-mtime -1 means "modified within the last 1 day." This is useful for finding recently changed
log files after an incident.

```bash
find /home -size +1M
```

-size +1M finds files larger than 1 megabyte. Capital M is megabytes. Lowercase k is kilobytes.
Capital G is gigabytes. The plus sign means "greater than." A minus sign means "less than."

```bash
find /etc -type f -name "*.conf"
```

-type f restricts the search to regular files. -type d finds directories. -type l finds
symbolic links.

```bash
find /tmp -type f -exec rm {} \;
```

The -exec flag executes a command on each result. The {} is replaced by the filename found.
The \; ends the -exec expression. This command finds all files in /tmp and deletes them.
Use -exec with caution.

---

### Section 2: The locate Command

locate searches a pre-built database index of filenames. It is dramatically faster than find
but can be out of date.

[SHOW TERMINAL]

```bash
locate sshd_config
```

This returns results in milliseconds because it searches a cached database file, not the live
filesystem. The database is stored at /var/lib/mlocate/mlocate.db or a similar path.

The critical limitation: if a file was created after the database was last updated, locate
will not find it.

```bash
sudo updatedb
```

updatedb rebuilds the database. On most systems it runs automatically via cron once a day.
If you just created a file and locate cannot find it, run updatedb first.

Key exam point: find searches the live filesystem in real time. locate searches a database.
Questions asking about real-time accuracy versus speed are testing this difference.

---

### Section 3: The grep Command

grep searches inside file contents for a pattern. While find locates files by name or attribute,
grep locates files by what is inside them.

[SHOW TERMINAL]

```bash
grep "root" /etc/passwd
```

This searches /etc/passwd for lines containing the word root and prints them.

```bash
grep -i "ubuntu" /etc/os-release
```

-i makes the search case-insensitive. This matches "ubuntu", "Ubuntu", and "UBUNTU".

```bash
grep -n "error" /var/log/syslog
```

-n shows the line number before each matching line. Useful when you need to find the exact
location in a long file.

```bash
grep -r "PermitRootLogin" /etc/ssh/
```

-r searches recursively through all files in a directory.

```bash
grep -v "^#" /etc/ssh/sshd_config
```

-v inverts the match, showing only lines that do NOT match. The pattern ^# matches lines
starting with #. So this command shows all non-comment lines in sshd_config.

```bash
grep -c "Failed" /var/log/auth.log
```

-c shows a count of matching lines instead of the lines themselves. Useful for quantifying
failed login attempts.

---

### Section 4: Pipes - Connecting Commands

The pipe character (|) takes the output of one command and sends it as input to the next command.

[SHOW TERMINAL]

```bash
ls /etc | grep "ssh"
```

List all files in /etc, then filter for lines containing ssh.

```bash
ps aux | grep "nginx"
```

List all running processes, then filter for nginx.

```bash
cat /var/log/syslog | grep "error" | tail -20
```

Three commands chained: read syslog, keep only error lines, show the last 20 of those lines.

```bash
ls -la /etc | sort -k5 -n | tail -10
```

List all files in /etc, sort by column 5 (file size) numerically, show the 10 largest.

---

### Section 5: Input and Output Redirection

Linux uses three standard file descriptors: stdin (fd 0), stdout (fd 1), and stderr (fd 2).

[SHOW TERMINAL]

```bash
ls /etc > etc_listing.txt
```

The > operator redirects stdout to a file, overwriting it.

```bash
ls /etc >> etc_listing.txt
```

The >> operator appends to an existing file instead of overwriting it.

```bash
ls /nonexistent 2> errors.txt
```

The 2> redirects stderr to a file. Error messages go to the file, not the terminal.

```bash
./some_script.sh > output.log 2>&1
```

This is the critical exam pattern: redirect stdout to output.log, then redirect stderr to
wherever stdout is currently going. Both stdout and stderr end up in the same file.

---

### Section 6: Hard Links and Symbolic Links

[SHOW TERMINAL]

```bash
ln /etc/hostname hostname_hardlink
```

A hard link creates a second directory entry pointing to the same inode. Hard links cannot
cross filesystem boundaries. If you delete the original file, the data remains accessible
through the hard link.

```bash
ln -s /etc/hostname hostname_symlink
ls -la hostname_symlink
```

A symbolic link contains the path to the target file. If you delete the target, the symlink
becomes broken. Symlinks can cross filesystem boundaries and can point to directories.

```bash
ls -l /bin
```

On modern Ubuntu, /bin is itself a symlink to /usr/bin. This is the FHS modernization common
across current distributions.

---

### Section 7: Wildcards and Globbing

[SHOW TERMINAL]

```bash
ls /etc/*.conf
```

The * matches any sequence of characters. Lists all .conf files in /etc.

```bash
ls /etc/s??.conf
```

The ? matches exactly one character.

```bash
ls /etc/[abc]*
```

Square brackets match any single character from the list.

---

### Section 8: Exam Tips for Module 02

The exam frequently uses /var/log/secure versus /var/log/auth.log as a distractor. /var/log/secure
is the RHEL/CentOS authentication log. /var/log/auth.log is the Debian/Ubuntu equivalent. Know both.

For find versus locate: if the question says "real time" or "most up to date," the answer is find.
If the question says "fastest" or "pre-built index," the answer is locate.

For output redirection: > overwrites, >> appends, 2> captures stderr, 2>&1 merges stderr into
stdout.

The /proc filesystem is virtual with no disk storage. Questions about where to find CPU
information or memory statistics in real time point to /proc.

The root user's home directory is /root, not /home/root. This is a common exam distractor.

---

### Lab Preview

This week's lab walks you through the entire filesystem, practicing ls, cd, pwd, mkdir, cp, mv,
rm, find, locate, and grep. You will navigate from the root to deep subdirectories, create and
manipulate files, and answer analysis questions about what you observe. Read the lab instructions
fully before you begin.

---

### Summary

Module 02 has given you the full navigation toolkit: the FHS directory tree, absolute and relative
paths, file creation and manipulation, file searching with find and locate, content searching with
grep, output redirection, pipes, links, and wildcards.

Module 03 covers file permissions and ownership - the security layer that determines who can do
what with every file we just learned to navigate.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
