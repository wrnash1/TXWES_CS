# Video Script: Module 03 — Linux Filesystem Hierarchy Standard (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## [INTRO — 0:00–0:45]

Welcome back to Module 3, Part 2. In Part 1 we mapped the entire Linux directory tree — every major FHS directory, its purpose, and what lives there. Now we work with file content. You need to be able to read files, look at the beginning and end of a file, search for files across the filesystem, filter output, and redirect output from one command to another. These skills are the backbone of Linux command-line work and appear constantly on the Linux+ exam.

Follow along in your VM. Open two terminal windows if you can — one to run commands and one to look at man pages.

---

## [SECTION 1 — Reading File Content — 0:45–3:30]

### cat — Concatenate and Print

`cat` reads file content and prints it to the terminal. It is the simplest way to view a file's contents.

```bash
cat /etc/hostname
cat /etc/os-release
```

`cat` is best for short files. For large files, it floods your terminal with text. Use `less` or `head`/`tail` for large files.

`cat` is also used to concatenate multiple files:

```bash
cat file1.txt file2.txt > combined.txt
```

And to create a quick file with content:

```bash
cat > myfile.txt
```

Type your content, then press `Ctrl+D` to end input. We will cover redirection in detail in a moment.

### less — Page Through a File

`less` is the standard tool for reading large files. It loads the file page by page, so it works instantly even on files that are gigabytes in size.

```bash
less /var/log/syslog
```

Navigation in `less`:

- Arrow keys or `j`/`k` — scroll line by line
- `Space` or `f` — page forward
- `b` — page backward
- `/pattern` — search forward for pattern
- `n` — next match, `N` — previous match
- `G` — jump to end of file
- `g` — jump to beginning
- `q` — quit

`less` is more powerful than the older `more` command and has replaced it in most workflows. The exam may reference both — know that `less` allows both forward and backward navigation while `more` only goes forward.

### head and tail — First and Last Lines

`head` shows the first lines of a file. By default, it shows the first 10 lines.

```bash
head /var/log/syslog
head -n 20 /var/log/syslog
```

`-n 20` shows the first 20 lines.

`tail` shows the last lines of a file — also 10 by default.

```bash
tail /var/log/syslog
tail -n 30 /var/log/syslog
```

`-n 30` shows the last 30 lines.

The most important `tail` flag for system administrators is `-f` — follow. `tail -f /var/log/syslog` keeps the file open and prints new lines as they are added. This is how you watch a log file in real time:

```bash
tail -f /var/log/syslog
```

Press `Ctrl+C` to stop following. In production environments, `tail -f` on service logs is one of the first tools you reach for when debugging.

---

## [SECTION 2 — Finding Files — 3:30–7:00]

### find — Search the Filesystem

`find` searches for files and directories based on criteria you specify. It is one of the most powerful and versatile Linux commands.

Basic syntax: `find [starting-directory] [criteria]`

Find files by name — case-sensitive:

```bash
find /etc -name "sshd_config"
find /home -name "*.txt"
```

Find files by name — case-insensitive:

```bash
find /home -iname "readme*"
```

Find only files (not directories):

```bash
find /tmp -type f
```

Find only directories:

```bash
find /var -type d
```

Find files by size — larger than 10 MB:

```bash
find /var/log -type f -size +10M
```

The `+` before a size means "greater than." `-` means "less than." No sign means "exactly."

Find files modified in the last 7 days:

```bash
find /home -mtime -7
```

`-mtime -7` means modified within the last 7 days. `-mtime +30` means modified more than 30 days ago.

Find and execute a command on results — print the size of each result:

```bash
find /var/log -type f -name "*.log" -exec ls -lh {} \;
```

The `-exec` flag runs the specified command on each found file. `{}` is replaced by the filename. The `\;` terminates the `-exec` expression.

### locate — Fast Database-Driven Search

`locate` searches a pre-built database of filenames rather than scanning the filesystem in real time. It is much faster than `find` for simple name searches.

```bash
locate sshd_config
locate passwd
```

The database is updated by `updatedb` (run as root). On many systems, `updatedb` runs daily via cron. If you have recently created a file and `locate` cannot find it, run `sudo updatedb` to refresh the database.

The limitation: `locate` can only search by filename, not by size, modification time, permissions, or other attributes. For anything beyond name searching, use `find`.

---

## [SECTION 3 — File Globbing and Wildcards — 7:00–9:00]

### Wildcards in Bash

Globbing — also called filename expansion or wildcards — allows you to specify patterns that bash expands to matching filenames before running the command.

The three main glob patterns:

`*` — matches any string of zero or more characters

```bash
ls /etc/*.conf
ls /var/log/*.log
```

`?` — matches exactly one character

```bash
ls /etc/ssh/ssh?.conf
```

`[abc]` — matches any one character inside the brackets

```bash
ls /dev/sd[abc]
ls /etc/rc[0-6].d
```

`[0-9]` matches any single digit. `[a-z]` matches any single lowercase letter.

Globbing is performed by bash before the command executes. The command receives the expanded list of filenames — it never sees the glob pattern itself. This is different from regular expressions, which are processed by the tool receiving them.

### Globbing vs. Regular Expressions

The exam distinguishes between globs and regular expressions. In a glob: `*` means "any string." In a regular expression: `*` means "zero or more of the preceding character." Glob `*.txt` matches all `.txt` files. The same pattern as a regex means something different.

`grep` and `sed` and `awk` use regular expressions. `ls`, `find -name`, and shell expansion use globs. Know which is which.

---

## [SECTION 4 — Redirection and Pipes — 9:00–12:30]

### Standard Streams

Every Linux process has three standard streams:

- **stdin** (file descriptor 0) — standard input. By default, the keyboard.
- **stdout** (file descriptor 1) — standard output. By default, the terminal.
- **stderr** (file descriptor 2) — standard error. By default, also the terminal.

Redirection lets you change where these streams go.

### Output Redirection

`>` redirects stdout to a file, overwriting the file if it exists:

```bash
ls -la /etc > etc_listing.txt
cat etc_listing.txt
```

`>>` appends stdout to a file rather than overwriting:

```bash
date >> timestamps.log
date >> timestamps.log
cat timestamps.log
```

You will see two date entries — the file was not overwritten.

`2>` redirects stderr to a file:

```bash
ls /nonexistent 2> errors.txt
cat errors.txt
```

`2>&1` redirects stderr to the same place as stdout. Used to capture all output together:

```bash
command > output.txt 2>&1
```

`/dev/null` is a common redirection target when you want to discard output completely:

```bash
find / -name "*.log" 2>/dev/null
```

This discards all "Permission denied" errors from `find` so only actual results appear.

### Input Redirection

`<` redirects stdin from a file:

```bash
sort < unsorted.txt
```

### Pipes

The pipe `|` connects the stdout of one command to the stdin of the next command. Pipes are one of the most powerful and frequently used features of the Linux shell.

```bash
ls -la /etc | less
```

This pipes the output of `ls -la /etc` to `less`, so you can scroll through the directory listing page by page instead of having it scroll off your screen.

```bash
cat /var/log/syslog | grep "error" | head -20
```

This reads the syslog, filters to lines containing "error," and shows the first 20 matches.

### tee — Split Output

`tee` reads from stdin and writes to both stdout AND a file simultaneously:

```bash
df -h | tee disk_report.txt
```

The `df -h` output appears on your terminal AND is written to `disk_report.txt` at the same time. This is useful when you want to see command output live and also save it for later review.

---

## [SECTION 5 — Practical FHS + Command Integration — 12:30–14:30]

### Putting It Together

Let's combine what we have learned. Here are three practical scenarios:

**Scenario 1: Find the SSH configuration and view it**

```bash
find /etc -name "sshd_config"
less /etc/ssh/sshd_config
```

**Scenario 2: Watch the authentication log for failed login attempts in real time**

```bash
tail -f /var/log/auth.log | grep -i "failed"
```

This combines `tail -f` (follow the log) with `grep` (filter for failed login lines). Every time a failed login occurs, a new line appears.

**Scenario 3: Find all files in /var/log larger than 50 MB and save the list to a file**

```bash
find /var/log -type f -size +50M > large_logs.txt
cat large_logs.txt
```

**Scenario 4: Count the number of configuration files in /etc**

```bash
find /etc -maxdepth 1 -type f -name "*.conf" | wc -l
```

`wc -l` counts lines — since `find` outputs one line per result, this counts the number of matching files. `-maxdepth 1` limits the search to `/etc` itself, not subdirectories.

These patterns — combining `find`, `grep`, `tail`, `less`, and redirection — represent real-world Linux administration workflows.

---

## [OUTRO — 14:30–15:00]

Module 3 is complete. You now know where everything on a Linux system lives, how to read file contents at any scale, how to find files across the filesystem, and how to chain commands together using pipes and redirection.

The Module 3 lab puts all of this together — you will navigate the FHS directories, use `find` with multiple criteria, practice globbing patterns, and build pipelines using redirection and `tee`.

In Module 4 we cover text processing — `grep`, `sed`, `awk`, and sorting, which build directly on the redirection and piping concepts from today. See you there.

---

## [END OF SCRIPT — PART 2]

---

### Instructor Notes

- Estimated delivery time: 14–15 minutes.
- All command demonstrations should be live terminal recordings, not just text on screen.
- The `tail -f` live follow demo is particularly effective — split the terminal, generate log entries in one pane, watch them appear in the other.
- The globbing vs. regex distinction consistently confuses students — consider a side-by-side comparison on screen.
- Redirect and pipe section benefits from a visual diagram showing the stdin/stdout/stderr streams and how `|` and `>` redirect them.
