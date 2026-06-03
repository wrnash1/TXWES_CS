# Reading Guide: Module 04 — Text Processing and Editors

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Overview

This reading guide supports Module 04. Text processing is a foundational sysadmin skill because nearly every Linux configuration, log, and data file is plain text. Master these tools and you can inspect, transform, and report on system state without installing any additional software.

---

## Section 1 — Text Editors

### 1.1 Why Two Editors?

Linux systems typically have both nano and vim (or its ancestor vi) available. You need both because:

- Minimal server images often ship with vi/vim but not nano
- Recovery environments and containers may have only one editor
- Some tasks are genuinely faster in vim due to its command language
- Collaborative documentation often assumes nano for beginners

The Linux+ exam tests vim specifically. Know the modes and commands cold.

### 1.2 nano Quick Reference

| Action | Keystroke |
|---|---|
| Save (write) | Control+O |
| Exit | Control+X |
| Cut line | Control+K |
| Paste (uncut) | Control+U |
| Search | Control+W |
| Go to line | Control+_ |
| Show line numbers | Launch with `nano -l` |

### 1.3 vim Modal Design

vim operates in distinct modes. The mode you are in determines what keystrokes do.

**Normal mode** — the default; keystrokes are commands, not text input.

**Insert mode** — keystrokes type text. Enter with: `i` (before cursor), `a` (after cursor), `o` (new line below), `O` (new line above).

**Command-line mode** — entered from Normal mode by pressing `:`. Used for save, quit, substitute, and other file-level operations.

**Visual mode** — entered from Normal mode by pressing `v`. Allows character-by-character selection, `V` for line selection.

### 1.4 vim Normal Mode Commands

| Command | Action |
|---|---|
| `h` `j` `k` `l` | Left / Down / Up / Right |
| `gg` | Jump to first line |
| `G` | Jump to last line |
| `0` | Jump to start of line |
| `$` | Jump to end of line |
| `dd` | Delete (cut) current line |
| `D` | Delete from cursor to end of line |
| `yy` | Yank (copy) current line |
| `p` | Paste after cursor |
| `u` | Undo |
| Control+R | Redo |
| `/pattern` | Search forward |
| `n` | Next match |
| `N` | Previous match |

### 1.5 vim Command-Line Mode Operations

| Command | Action |
|---|---|
| `:w` | Save |
| `:q` | Quit (fails if unsaved changes exist) |
| `:wq` or `:x` | Save and quit |
| `:q!` | Quit without saving (force) |
| `:%s/old/new/g` | Replace all occurrences in file |
| `:%s/old/new/gc` | Replace with confirmation |
| `:set number` | Show line numbers |
| `:set nonumber` | Hide line numbers |
| `:10` | Jump to line 10 |

---

## Section 2 — grep

### 2.1 Fundamentals

grep (Global Regular Expression Print) prints lines from a file or stdin that match a pattern.

```
grep [options] pattern [file...]
```

When no file is given, grep reads from standard input — making it a natural pipeline filter.

### 2.2 Essential Flags

| Flag | Meaning |
|---|---|
| `-i` | Case-insensitive matching |
| `-n` | Show line numbers |
| `-v` | Invert — show non-matching lines |
| `-r` | Recursive — search directory tree |
| `-l` | List filenames only (not matching lines) |
| `-c` | Count matching lines per file |
| `-F` | Fixed string (disable regex) |
| `-E` | Extended regex (same as egrep) |
| `-A N` | Show N lines after match |
| `-B N` | Show N lines before match |
| `-C N` | Show N lines before and after match |

### 2.3 Common Patterns

```bash
# Find all failed SSH logins
grep "Failed password" /var/log/auth.log

# Case-insensitive search
grep -i "error" /var/log/syslog

# Search all config files recursively
grep -r "Listen 80" /etc/apache2/

# Count 404 errors
grep -c "404" /var/log/nginx/access.log

# Show context around an error
grep -C 3 "segfault" /var/log/kern.log
```

---

## Section 3 — sed

### 3.1 Stream Editor Model

sed processes input line by line. Each line is loaded into a pattern space, instructions are applied, and the result is printed. sed does not modify the original file unless `-i` is used.

### 3.2 Substitution Syntax

```
sed 's/regex/replacement/flags' file
```

Common flags after the closing delimiter:

- `g` — replace all occurrences on each line (not just first)
- `I` — case-insensitive (GNU sed)
- `2` — replace only the second occurrence

### 3.3 Key Operations

| Operation | Example |
|---|---|
| Substitute | `sed 's/foo/bar/g' file` |
| In-place edit | `sed -i 's/foo/bar/g' file` |
| Delete lines matching | `sed '/pattern/d' file` |
| Delete line range | `sed '5,10d' file` |
| Delete blank lines | `sed '/^$/d' file` |
| Delete comment lines | `sed '/^#/d' file` |
| Print specific line | `sed -n '5p' file` |
| Print line range | `sed -n '5,10p' file` |

### 3.4 Multiple Instructions

Separate multiple instructions with `-e` or a semicolon:

```bash
sed -e '/^#/d' -e '/^$/d' /etc/ssh/sshd_config
sed '/^#/d; /^$/d' /etc/ssh/sshd_config
```

---

## Section 4 — awk

### 4.1 Record and Field Model

awk treats each input line as a record. Fields within each record are numbered $1, $2, ... $NF. Built-in variables:

| Variable | Meaning |
|---|---|
| `$0` | Entire current line |
| `$1` ... `$NF` | Field 1 through last field |
| `NF` | Number of fields on current line |
| `NR` | Number of records (lines) processed so far |
| `FS` | Field separator (default: whitespace) |
| `OFS` | Output field separator |

### 4.2 Program Structure

```
awk 'BEGIN { setup } pattern { action } END { teardown }' file
```

All three blocks are optional. The pattern can be a regex (`/error/`) or a comparison (`$3 > 500`).

### 4.3 Common Patterns

```bash
# Print username and shell from /etc/passwd
awk -F: '{ print $1, $7 }' /etc/passwd

# Sum a numeric column
awk '{ total += $5 } END { print "Total:", total }' data.txt

# Print lines where field 3 exceeds 1000
awk '$3 > 1000 { print }' data.txt

# Count lines matching a pattern
awk '/error/ { count++ } END { print count }' logfile.txt

# Add line numbers
awk '{ print NR, $0 }' file.txt
```

---

## Section 5 — Pipeline Utilities

### 5.1 sort

```bash
sort file.txt          # Alphabetical
sort -n file.txt       # Numeric
sort -r file.txt       # Reverse
sort -k2 file.txt      # Sort by second field
sort -k2 -n file.txt   # Sort by second field numerically
sort -u file.txt       # Remove duplicate lines
```

### 5.2 uniq

uniq requires sorted input. Always pipe through sort first.

```bash
sort file.txt | uniq          # Remove duplicates
sort file.txt | uniq -c       # Count occurrences
sort file.txt | uniq -d       # Show only duplicates
sort file.txt | uniq -u       # Show only unique lines
```

### 5.3 cut

```bash
cut -d: -f1 /etc/passwd          # First colon-delimited field
cut -d, -f2,4 data.csv           # Fields 2 and 4 from CSV
cut -c1-10 file.txt              # Characters 1 through 10
```

### 5.4 wc

```bash
wc -l file.txt     # Line count
wc -w file.txt     # Word count
wc -c file.txt     # Byte count
```

### 5.5 tr

```bash
echo "hello" | tr 'a-z' 'A-Z'        # Uppercase
echo "a:b:c" | tr ':' '\n'           # Replace colons with newlines
echo "hello   world" | tr -s ' '     # Squeeze repeated spaces
echo "hello" | tr -d 'aeiou'         # Delete vowels
```

### 5.6 xargs

xargs reads newline-separated items from stdin and passes them as arguments to a command:

```bash
find /tmp -name "*.tmp" | xargs rm
grep -l "old_hostname" /etc/*.conf | xargs sed -i 's/old_hostname/new_hostname/g'
```

---

## Section 6 — Combining Tools: Pipeline Patterns

### The Frequency Table Pattern

```bash
command_that_produces_lines | sort | uniq -c | sort -nr | head -N
```

Used for: top IP addresses, most common error codes, most active users, most referenced files.

### The Report Generation Pattern

```bash
awk 'BEGIN { printf "%-20s %s\n", "IP", "Count" }
     { count[$1]++ }
     END { for (ip in count) printf "%-20s %d\n", ip, count[ip] }' file \
  | sort -k2 -nr
```

### The Config Cleaning Pattern

```bash
grep -v '^#' /etc/some.conf | grep -v '^$'
# Equivalent:
sed '/^#/d; /^$/d' /etc/some.conf
```

---

## CompTIA Linux+ Exam Relevance

The following objective areas map to this module:

- **1.3** — File manipulation and text stream processing
- **2.1** — System service configuration (editing config files)
- **4.2** — Scripting and automation (pipelines, awk, sed)

Expect exam questions on:

- vim mode names and how to switch between them
- The difference between `:q` and `:q!`
- What `grep -v` does
- The purpose of the `g` flag in sed substitution
- How `sort | uniq -c` produces a frequency count

---

## Key Terms

- **Modal editor** — an editor with distinct modes where the same keystroke performs different actions depending on the current mode
- **Pattern space** — the working buffer sed uses to hold the current line during processing
- **Field** — in awk, a whitespace-delimited segment of a record; accessed as $1, $2, etc.
- **Pipeline** — a sequence of commands connected by `|` where stdout of each command feeds stdin of the next
- **Regular expression** — a pattern syntax for matching text; used by grep, sed, awk, and vim search
- **In-place editing** — modifying a file directly rather than writing to stdout; enabled in sed by the `-i` flag

---

*End of Module 04 Reading Guide*
