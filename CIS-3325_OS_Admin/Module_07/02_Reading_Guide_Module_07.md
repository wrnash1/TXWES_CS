# Reading Guide: Module 07 - Shell Scripting Fundamentals

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


## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 4.0 - Automation and Scripting

---

### Glossary

**Shebang** - The #! character sequence at the very first line of a script that specifies the interpreter path (e.g., #!/bin/bash).

**Positional Parameter** - A variable that holds a command-line argument passed to a script or function. $1 is the first argument, $2 is the second, and so on.

**Exit Code** - An integer returned by every command and script. 0 means success. Any non-zero value indicates an error. Captured in the special variable $?.

**Command Substitution** - Capturing the output of a command into a variable using the $() syntax (e.g., TODAY=$(date +%Y-%m-%d)).

**Here Document** - A multi-line string literal embedded in a script, delimited by a user-chosen word (typically EOF), used to pass multi-line input to commands.

**set -e** - A shell option that causes a script to exit immediately when any command returns a non-zero exit code.

**set -u** - A shell option that causes a script to exit when an undefined variable is referenced.

**trap** - A bash built-in that defines a command to run when the script receives a specified signal or reaches a predefined condition (ERR, EXIT).

**local** - A keyword used inside a function to restrict a variable's scope to that function. Without local, all script variables are global.

**IFS (Internal Field Separator)** - A shell variable that determines how bash splits input into words. Default is whitespace. Changing it affects how read and loops parse input.

---

### Special Variables Reference

| Variable | Meaning |
|----------|---------|
| $0 | Name of the script |
| $1 to $9 | Positional parameters (command-line arguments) |
| $# | Count of positional parameters |
| $@ | All positional parameters as separate quoted words |
| $* | All positional parameters as a single word |
| $? | Exit code of the most recently executed command |
| $$ | PID of the current shell or script |
| $! | PID of the most recently backgrounded process |
| $LINENO | Current line number in the script |

---

### File Test Operators

| Operator | Meaning |
|----------|---------|
| -f FILE | True if FILE exists and is a regular file |
| -d DIR | True if DIR exists and is a directory |
| -e PATH | True if PATH exists (file or directory) |
| -r FILE | True if FILE is readable |
| -w FILE | True if FILE is writable |
| -x FILE | True if FILE is executable |
| -s FILE | True if FILE exists and has size greater than zero |
| -L FILE | True if FILE is a symbolic link |
| -z STRING | True if STRING is empty (zero length) |
| -n STRING | True if STRING is not empty |

---

### Comparison Operators

Integer comparisons (used inside [ ] or [[ ]]):

| Operator | Meaning |
|----------|---------|
| -eq | Equal to |
| -ne | Not equal to |
| -lt | Less than |
| -le | Less than or equal to |
| -gt | Greater than |
| -ge | Greater than or equal to |

String comparisons:

| Operator | Meaning |
|----------|---------|
| = or == | Strings are equal |
| != | Strings are not equal |
| < | String is less than (alphabetical, inside [[]]) |
| > | String is greater than (alphabetical, inside [[]]) |

---

### Loop Control

| Statement | Effect |
|-----------|--------|
| break | Exit the current loop immediately |
| continue | Skip the rest of the current iteration; go to the next |
| exit N | Exit the entire script with exit code N |
| return N | Exit the current function with return code N |

---

### set Options for Robust Scripts

| Option | Effect |
|--------|--------|
| set -e | Exit immediately on any command failure |
| set -u | Exit on reference to an undefined variable |
| set -o pipefail | Pipeline returns exit code of first failing command |
| set -x | Print each command before executing (debug mode) |
| set -euo pipefail | Combined best-practice line for production scripts |

---

### trap Syntax Reference

```bash
trap 'COMMAND' SIGNAL
trap 'COMMAND' ERR
trap 'COMMAND' EXIT
trap 'COMMAND' INT
```

Common trap targets:

| Target | When it fires |
|--------|--------------|
| ERR | Any command exits with non-zero code (when set -e is active) |
| EXIT | Script exits for any reason (normal, error, or signal) |
| INT | User presses Ctrl+C (SIGINT) |
| TERM | Process receives SIGTERM |

---

### Parameter Expansion Reference

| Expression | Result |
|------------|--------|
| ${VAR} | Value of VAR |
| ${VAR:-default} | Value of VAR, or default if VAR is unset or empty |
| ${VAR:=default} | Value of VAR; sets VAR to default if unset or empty |
| ${#VAR} | Length of VAR's value |
| ${VAR#pattern} | Remove shortest prefix matching pattern |
| ${VAR##pattern} | Remove longest prefix matching pattern |
| ${VAR%pattern} | Remove shortest suffix matching pattern |
| ${VAR%%pattern} | Remove longest suffix matching pattern |
| ${VAR/old/new} | Replace first occurrence of old with new |
| ${VAR//old/new} | Replace all occurrences of old with new |
| ${VAR^^} | Convert to uppercase |
| ${VAR,,} | Convert to lowercase |

---

### Script Execution Methods Compared

| Method | Uses shebang | Execute permission needed | Runs in subshell | Variables persist to calling shell |
|--------|-------------|--------------------------|-----------------|-----------------------------------|
| ./script.sh | Yes | Yes | Yes | No |
| bash script.sh | No | No | Yes | No |
| source script.sh | No | No | No (same shell) | Yes |
| . script.sh | No | No | No (same shell) | Yes |

---

### Logging Pattern

A reliable logging function for production scripts:

```bash
LOG=/var/log/myscript.log

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$1] ${*:2}" | tee -a "$LOG"
}

log INFO  "Starting backup"
log ERROR "Backup failed: disk full"
```

tee -a writes to both stdout and the log file simultaneously. The -a flag appends.

---

### Cron Integration

Scripts intended for cron should redirect all output to a log file. Cron emails uncaptured
output to root, which fills inboxes on busy servers.

```bash
#!/bin/bash
exec >> /var/log/myscript.log 2>&1
```

The exec redirection at the top of the script captures all subsequent stdout and stderr
into the log file for the lifetime of the script execution.

---

### Exam Tips

1. The shebang line must be on line 1, column 1 of the script. A blank line before it breaks it.

2. $? must be checked immediately after the command whose exit code you want. Running any other command between the target command and the $? check will overwrite $? with the new command's exit code.

3. set -e exits on error, but set -u exits on undefined variables. Both are recommended for production scripts. Combine with set -o pipefail.

4. source (or .) runs the script in the current shell. Variables set inside the script affect the current session. Do not source scripts that cd or set variables you do not want to inherit.

5. break exits the loop. continue skips to the next iteration. exit exits the script entirely. return exits only the current function.

6. local in a function limits the variable to that function's scope. Without local, functions can accidentally modify global variables.

7. $@ preserves argument quoting (each argument as a separate word). $* combines all arguments into one word. Use $@ when forwarding arguments to other commands.

8. Use double quotes around variable references in test conditions: [ "$VAR" = "value" ]. Unquoted variables with spaces cause syntax errors in tests.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Write a correct shebang line
- Explain the difference between ./script.sh and source script.sh
- Assign and reference a variable correctly (no spaces around =)
- Use $() for command substitution
- List all special variables ($0, $1, $#, $@, $?, $$)
- Write a complete if/then/else/fi block with file test and string comparison operators
- Write a for loop over a list and over files with a glob pattern
- Write a while loop with an arithmetic condition
- Write a while read loop that processes a file line by line
- Define a function with local variables and a return value
- Use set -euo pipefail and explain what each flag does
- Write a trap for ERR and EXIT
- Use read with -p (prompt), -s (silent), and -t (timeout)
- Write a here document that feeds multi-line input to a command
- Use at least three parameter expansion operators from the reference table
- Construct a logging function that writes timestamped output to a file and stdout

---

## 9. Supplemental Resources

**1. The Linux Command Line (TLCL) — Chapters 24–36: Shell Scripting**
URL: https://linuxcommand.org/tlcl.php
Coverage: William Shotts' free book covers everything in this module: writing scripts, flow control,
reading keyboard input, functions, and string/number operations. Chapters 24–36 map directly to the
Module 07 objectives. Download the PDF for offline use.

**2. GNU Bash Manual — Official Reference**
URL: https://www.gnu.org/software/bash/manual/bash.html
Coverage: The authoritative reference for all bash syntax. Key sections for this module: 3.2 (shell
commands), 3.4 (shell parameters and variables), 3.5 (parameter expansion), 4.1 (set built-in and
flags including -e, -u, -o pipefail), 3.7 (redirections), and 6.1 (invoking bash). Use as a lookup
reference when the man page summary is insufficient.

**3. Advanced Bash-Scripting Guide (TLDP)**
URL: https://tldp.org/LDP/abs/html/
Coverage: Comprehensive community guide covering parameter substitution, string operations, arrays,
process substitution, here documents, and debugging techniques. Chapter 10 covers parameter expansion
operators in depth. Chapter 20 covers I/O redirection. Useful as a supplement to the GNU manual for
worked examples.

**4. bash(1) Man Page — man7.org**
URL: https://man7.org/linux/man-pages/man1/bash.1.html
Coverage: The full bash man page in searchable web format. Search for SPECIAL PARAMETERS ($0, $#,
$@, $*, $?), PARAMETER EXPANSION (:-, :=, :+, :?), SHELL BUILTIN COMMANDS (set, trap, read,
local, return), and HEREDOC (here-document) syntax. Essential for exam-level command accuracy.

**5. Bash Pitfalls — Greg's Wiki (wooledge.org)**
URL: https://mywiki.wooledge.org/BashPitfalls
Coverage: A curated list of common bash scripting errors and how to avoid them. Covers word splitting
with unquoted variables, pitfalls with for loops over ls output, the read -r flag requirement, IFS
handling, and why set -e does not behave as expected with certain constructs. Directly relevant to
the set -euo pipefail and while read loop content in this module.
