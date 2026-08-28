# Reading Guide: Module 04 — Text Processing and Editors

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

---

## 9. Supplemental Resources

**1. [Vim Adventures — Interactive vim Tutorial](https://vim-adventures.com/)**
A browser-based game that teaches vim navigation and commands through puzzle levels. Particularly effective for building muscle memory for `h/j/k/l`, `w/b`, `gg/G`, and mode-switching without the cognitive overhead of a text document.

**2. [The GNU awk (gawk) User's Guide](https://www.gnu.org/software/gawk/manual/gawk.html)**
The official reference manual for GNU awk. Covers all built-in variables (`NR`, `NF`, `FS`, `OFS`, `RS`), built-in functions, arrays, and the `BEGIN`/`END` block structure. Use the pattern-action sections when building complex log analysis pipelines.

**3. [man7.org — sed(1) Manual Page](https://man7.org/linux/man-pages/man1/sed.1.html)**
The complete sed manual page from the Linux man-pages project. Covers all sed commands (`s`, `d`, `p`, `i`, `a`, `c`, `y`, `=`), address forms (line numbers, regex, ranges), and the critical `-i` in-place editing behavior including the backup-extension variant (`-i.bak`).

---

*End of Module 04 Reading Guide*
