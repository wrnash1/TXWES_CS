# Reading Guide: Module 09 — Shell Scripting Fundamentals

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

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Overview

This reading guide provides a comprehensive reference for bash shell scripting. It supplements the video lectures with syntax tables, complete patterns, and additional examples. Use it as a reference during the lab and as a study guide before the quiz.

**Estimated Reading Time:** 50–65 minutes

---

## Section 1 — Script Structure and Best Practices

### 1.1 Standard Script Template

Every professional bash script should follow a consistent structure:

```bash
#!/usr/bin/env bash
# Script name: scriptname.sh
# Description: Brief description of what this script does
# Author: Your Name
# Date: YYYY-MM-DD
# Usage: ./scriptname.sh [options] [arguments]

# Strict mode: exit on error, undefined variables, pipe failures
set -euo pipefail

# ==============================================================================
# Constants and Configuration
# ==============================================================================
readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
readonly LOG_FILE="/var/log/${SCRIPT_NAME%.sh}.log"

# ==============================================================================
# Functions
# ==============================================================================
usage() {
  cat << EOF
Usage: $SCRIPT_NAME [OPTIONS] ARGUMENT

Description of what the script does.

Options:
  -h, --help     Show this help message
  -v, --verbose  Enable verbose output
  -n, --dry-run  Show what would be done without doing it

Examples:
  $SCRIPT_NAME --verbose username
  $SCRIPT_NAME --dry-run

EOF
}

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

die() {
  echo "ERROR: $*" >&2
  exit 1
}

# ==============================================================================
# Argument Parsing
# ==============================================================================
VERBOSE=false
DRY_RUN=false

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    -h|--help)    usage; exit 0 ;;
    -v|--verbose) VERBOSE=true; shift ;;
    -n|--dry-run) DRY_RUN=true; shift ;;
    --)           shift; break ;;
    -*)           die "Unknown option: $1" ;;
    *)            break ;;
  esac
done

# ==============================================================================
# Main
# ==============================================================================
main() {
  log "Script started"
  # Main logic here
  log "Script completed"
}

main "$@"
```

### 1.2 The `set` Options

| Option | Effect |
|---|---|
| `set -e` | Exit immediately on error |
| `set -u` | Treat unset variables as errors |
| `set -o pipefail` | Pipeline fails if any command fails |
| `set -x` | Print each command before executing (debug) |
| `set -v` | Print each line before executing |
| `set -n` | Parse but do not execute (syntax check) |

Combining: `set -euo pipefail` is the standard strict mode header for production scripts.

---

## Section 2 — Variables Complete Reference

### 2.1 Variable Types

```bash
# String (default)
NAME="Alice Smith"

# Integer (declare restricts to integers)
declare -i COUNT=0
COUNT="not a number"    # Silently becomes 0 with declare -i

# Read-only (cannot be changed)
readonly MAX_RETRIES=3
declare -r VERSION="2.1.0"

# Array
FRUITS=("apple" "banana" "cherry")
echo "${FRUITS[0]}"        # apple
echo "${FRUITS[@]}"        # all elements
echo "${#FRUITS[@]}"       # number of elements

# Associative array (bash 4+)
declare -A COLORS
COLORS["red"]="#FF0000"
COLORS["green"]="#00FF00"
echo "${COLORS[red]}"

# Environment variables (exported to child processes)
export DATABASE_URL="postgresql://localhost/mydb"
```

### 2.2 Parameter Expansion

These are critical for writing robust scripts:

```bash
# Default value if unset or empty
NAME="${1:-default_name}"         # Use "default_name" if $1 is unset/empty
PORT="${PORT:-8080}"               # Use 8080 if $PORT not in environment

# Default value only if unset (not if empty)
NAME="${1-default_name}"

# Assign default and store it
NAME="${NAME:=default}"

# Error if unset or empty
VALUE="${VARNAME:?Variable VARNAME must be set}"

# Substring extraction
FULL_PATH="/var/log/app/error.log"
FILENAME="${FULL_PATH##*/}"        # error.log  (remove longest prefix match)
DIRECTORY="${FULL_PATH%/*}"        # /var/log/app  (remove shortest suffix match)
EXTENSION="${FULL_PATH##*.}"       # log

# String length
echo "${#NAME}"

# String replacement
PATH_FIXED="${OLD_PATH/old/new}"    # Replace first occurrence
PATH_FIXED="${OLD_PATH//old/new}"   # Replace all occurrences

# Convert case (bash 4+)
UPPER="${NAME^^}"
LOWER="${NAME,,}"
```

### 2.3 Special Variables Reference

| Variable | Meaning |
|---|---|
| `$0` | Script name |
| `$1` – `$9` | Positional parameters 1–9 |
| `${10}` | Positional parameter 10+ (braces required) |
| `$#` | Number of positional parameters |
| `$@` | All positional parameters as separate words |
| `$*` | All positional parameters as one word |
| `$?` | Exit status of last command |
| `$$` | PID of current shell |
| `$!` | PID of last background command |
| `$-` | Current shell option flags |
| `$_` | Last argument of last command |
| `$IFS` | Internal Field Separator (default: space, tab, newline) |

---

## Section 3 — Conditional Expressions

### 3.1 File Test Operators

| Operator | True If |
|---|---|
| `-e FILE` | FILE exists |
| `-f FILE` | FILE is a regular file |
| `-d DIR` | DIR is a directory |
| `-l FILE` | FILE is a symbolic link |
| `-r FILE` | FILE is readable |
| `-w FILE` | FILE is writable |
| `-x FILE` | FILE is executable |
| `-s FILE` | FILE has size greater than zero |
| `-b FILE` | FILE is block device |
| `-c FILE` | FILE is character device |
| `-p FILE` | FILE is a named pipe |
| `-S FILE` | FILE is a socket |
| `-N FILE` | FILE was modified since last read |
| `FILE1 -nt FILE2` | FILE1 is newer than FILE2 |
| `FILE1 -ot FILE2` | FILE1 is older than FILE2 |

### 3.2 String Test Operators

| Operator | True If |
|---|---|
| `-z STRING` | STRING is empty (zero length) |
| `-n STRING` | STRING is not empty |
| `STR1 = STR2` | Strings are equal (single `[`) |
| `STR1 == STR2` | Strings are equal (double `[[`) |
| `STR1 != STR2` | Strings are not equal |
| `STR1 < STR2` | STR1 sorts before STR2 (lexicographic) |
| `STR1 > STR2` | STR1 sorts after STR2 |
| `STR =~ PATTERN` | STR matches regex PATTERN (`[[` only) |

### 3.3 Integer Test Operators

| Operator | Meaning |
|---|---|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-lt` | Less than |
| `-le` | Less than or equal |
| `-gt` | Greater than |
| `-ge` | Greater than or equal |

### 3.4 [ ] vs [[ ]] vs (( ))

```bash
# [ ] — POSIX test command; use in sh-compatible scripts
[ -f "$FILE" ]
[ "$A" = "$B" ]

# [[ ]] — bash keyword; safer with strings; supports regex and &&/||
[[ -f "$FILE" ]]
[[ "$A" == "$B" ]]
[[ "$STR" =~ ^[0-9]+$ ]]    # Regex match
[[ -f "$FILE" && -r "$FILE" ]]

# (( )) — arithmetic context; integers only; no $ needed for variables
COUNT=5
if (( COUNT > 3 )); then echo "Greater"; fi
(( COUNT++ ))
(( RESULT = COUNT * 2 ))
```

---

## Section 4 — Loops Complete Reference

### 4.1 for Loop Patterns

```bash
# List loop
for ITEM in one two three; do
  echo "$ITEM"
done

# Array loop
ITEMS=("one" "two" "three")
for ITEM in "${ITEMS[@]}"; do
  echo "$ITEM"
done

# C-style loop
for ((i=0; i<10; i++)); do
  echo "$i"
done

# File glob loop
for F in /etc/*.conf; do
  echo "Config: $F"
done

# Command output loop (process substitution — avoids subshell)
while IFS= read -r LINE; do
  echo "$LINE"
done < <(command_that_produces_output)

# Read file line by line
while IFS= read -r LINE; do
  echo "$LINE"
done < /path/to/file
```

### 4.2 Loop Control

```bash
# break — exit the loop immediately
for i in $(seq 1 100); do
  if [ "$i" -eq 10 ]; then
    break
  fi
  echo "$i"
done

# continue — skip to the next iteration
for i in $(seq 1 10); do
  if (( i % 2 == 0 )); then
    continue
  fi
  echo "Odd: $i"
done

# Break outer loop from inner loop
FOUND=false
for DIR in /etc /var /opt; do
  for FILE in "$DIR"/*.conf; do
    if [[ -f "$FILE" ]]; then
      FOUND=true
      break 2    # Break 2 levels up
    fi
  done
done
```

---

## Section 5 — Functions Complete Reference

### 5.1 Function Definition and Calling

```bash
# Standard function definition
my_function() {
  # function body
  local result="done"
  echo "$result"    # "Return" a value by printing to stdout
}

# Alternative syntax
function my_function() {
  :    # colon is the null command; does nothing
}

# Calling
my_function                     # Call with no arguments
my_function arg1 arg2          # Call with arguments
OUTPUT=$(my_function arg1)     # Capture output
my_function && echo "success"  # Use return code
```

### 5.2 Function Return Values

```bash
# Return codes (0-255 only)
check_file() {
  local file="$1"
  [ -f "$file" ] && return 0 || return 1
}

if check_file "/etc/passwd"; then
  echo "File exists"
fi

# Return strings via stdout
get_username() {
  echo "$(id -un)"
}
USER=$(get_username)

# Return strings via nameref (bash 4.3+)
get_value() {
  local -n result_var="$1"
  result_var="computed value"
}

get_value MY_RESULT
echo "$MY_RESULT"    # computed value
```

---

## Section 6 — I/O and Redirection Reference

### 6.1 Redirection Operators

| Operator | Action |
|---|---|
| `> file` | Redirect stdout to file (overwrite) |
| `>> file` | Redirect stdout to file (append) |
| `2> file` | Redirect stderr to file |
| `2>> file` | Append stderr to file |
| `2>&1` | Redirect stderr to same destination as stdout |
| `&> file` | Redirect both stdout and stderr to file |
| `< file` | Redirect file to stdin |
| `<< EOF` | Here-document (multi-line stdin) |
| `<<< string` | Here-string (single string as stdin) |
| `|` | Pipe stdout of one command to stdin of next |
| `|&` | Pipe both stdout and stderr |

### 6.2 read Command Reference

```bash
# Basic read
read -r VARIABLE

# Read with prompt
read -r -p "Enter name: " NAME

# Silent read (for passwords)
read -r -s -p "Password: " PASS

# Read with timeout
read -r -t 5 -p "Input (5s): " INPUT

# Read into array (splits on IFS)
read -r -a ITEMS <<< "one two three"

# Read specific number of characters
read -r -n 1 -p "Continue? [y/n]: " ANSWER

# Read an entire file into a variable
FILE_CONTENT=$(< /etc/hostname)
```

---

## Section 7 — Debugging Reference

### 7.1 Debugging Techniques

```bash
# Method 1: bash -x (traces every command)
bash -x script.sh

# Method 2: set -x inside the script
set -x
# ... section to debug ...
set +x

# Method 3: Custom debug function
DEBUG="${DEBUG:-false}"
debug() {
  if "$DEBUG"; then
    echo "DEBUG: $*" >&2
  fi
}
# Run with: DEBUG=true ./script.sh

# Method 4: Syntax check only (does not execute)
bash -n script.sh

# Method 5: shellcheck (static analysis)
shellcheck script.sh
# Common findings:
# SC2086: Double quote to prevent word splitting
# SC2154: Variable referenced but not assigned
# SC2164: Use 'cd ... || exit' to handle failure

# Method 6: trap for debugging
trap 'echo "Line $LINENO: $BASH_COMMAND" >&2' DEBUG
```

---

## Section 8 — Common Script Patterns

### 8.1 Argument Validation

```bash
# Require exact number of arguments
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <source> <destination>" >&2
  exit 1
fi

# Require at least one argument
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <file...>" >&2
  exit 1
fi
```

### 8.2 Locking (Prevent Concurrent Execution)

```bash
LOCKFILE="/var/run/myscript.lock"

# Using flock (requires util-linux)
exec 200>"$LOCKFILE"
flock -n 200 || { echo "Another instance is running" >&2; exit 1; }

# Simple PID-file lock
if [ -f "$LOCKFILE" ]; then
  PID=$(cat "$LOCKFILE")
  if kill -0 "$PID" 2>/dev/null; then
    echo "Script already running (PID: $PID)" >&2
    exit 1
  fi
fi
echo $$ > "$LOCKFILE"
trap "rm -f $LOCKFILE" EXIT
```

### 8.3 Logging Pattern

```bash
# Structured logging
LOG_FILE="/var/log/myscript.log"
LOG_LEVEL="${LOG_LEVEL:-INFO}"

_log() {
  local level="$1"
  shift
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $*" | tee -a "$LOG_FILE"
}

info()  { _log "INFO"  "$@"; }
warn()  { _log "WARN"  "$@" >&2; }
error() { _log "ERROR" "$@" >&2; }
debug() { [[ "$LOG_LEVEL" == "DEBUG" ]] && _log "DEBUG" "$@"; }

info "Script started"
warn "Low disk space"
error "Failed to connect"
```

---

## Section 9 — Key Terms Glossary

| Term | Definition |
|---|---|
| shebang | `#!` line specifying the script interpreter |
| variable expansion | Replacing `$VAR` with its value |
| command substitution | `$(command)` — replaces with command output |
| positional parameter | `$1`, `$2`, etc. — script arguments |
| exit code | 0–255 integer returned by commands; 0 = success |
| stderr | Standard error stream (file descriptor 2) |
| here-document | Multi-line text passed to a command using `<<` |
| here-string | Single string passed to a command using `<<<` |
| IFS | Internal Field Separator — controls word splitting |
| subshell | Child process created by `()`, pipe, or `$()` |
| `local` | Keyword to scope variables inside functions |
| `trap` | Register commands to run on signals or script exit |
| `set -e` | Exit immediately on error |
| `set -u` | Error on undefined variable |
| `shellcheck` | Static analysis tool for shell scripts |

---

## Section 10 — Review Questions

1. What is the difference between `$@` and `$*` when they are quoted?

2. What does `set -u` do and why is it useful?

3. A script contains `NAME=$1`. If the script is called without arguments, what happens? How do you provide a safe default?

4. What is the purpose of the `local` keyword in a bash function?

5. How do you redirect both stdout and stderr to a file?

6. What is the difference between `>` and `>>` redirection?

7. Write the one-line `if` test to check that a variable `FILE` refers to an existing regular file.

8. What does `trap cleanup EXIT` do?

9. How would you run a script in debug trace mode without modifying the script file?

10. What does `$?` contain, and when should you check it?

---

## 9. Supplemental Resources

**1. [Bash Scripting Guide — The Linux Documentation Project](https://tldp.org/LDP/abs/html/index.html)**
The Advanced Bash-Scripting Guide (ABS) is one of the most comprehensive free references for bash scripting available. Covers all topics in this module in depth: variable types, quoting rules, arithmetic expansion, loops, functions, I/O redirection, process substitution, and trap. Particularly useful chapters include "Special Characters," "Tests," and "Here Documents." Essential bookmark for anyone working through the lab exercises.

**2. [ShellCheck — Shell Script Static Analysis Tool](https://www.shellcheck.net/)**
ShellCheck is an online and command-line linter for shell scripts that identifies common mistakes: unquoted variables, improper `[ ]` vs `[[ ]]` usage, unsafe glob expansion, portability issues, and more. Every script written in this module's lab should be run through ShellCheck before submission. The companion GitHub repository at `github.com/koalaman/shellcheck` includes the full list of checks with explanations, making it an excellent learning resource alongside the linter.

**3. [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)**
Google's internal shell scripting style guide, published publicly. Provides opinionated but well-reasoned guidance on when to use bash vs other tools, function naming conventions, variable quoting, error handling patterns, and script structure. The section on "When to use Shell" is particularly relevant for understanding the limits of shell scripting. Following a consistent style guide is a key professional skill assessed in the CompTIA Linux+ exam objectives for scripting.
