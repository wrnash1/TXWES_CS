# Video Script: Module 09 — Shell Scripting Fundamentals (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome Back

Welcome back to Module 9. In Part 1 we built the foundations: shebang, variables, conditionals, loops, and case statements.

In Part 2 we add the professional-level elements that make scripts reliable, maintainable, and debuggable: functions, input and output handling, exit codes, error handling best practices, and debugging techniques.

---

### Slide 2 — Functions

Functions in bash allow you to group commands, name them, and call them multiple times. They improve readability and enable code reuse.

```bash
#!/usr/bin/env bash

# Function definition syntax (both forms are valid)
greet() {
  echo "Hello, $1"
}

function log_message() {
  local LEVEL="$1"
  local MSG="$2"
  echo "[$(date +%H:%M:%S)] [$LEVEL] $MSG"
}

# Call functions just like commands
greet "Alice"
log_message "INFO" "Script started"
log_message "ERROR" "Configuration file not found"

# Functions receive arguments via $1, $2 etc. — NOT the script's arguments
# Inside a function, $@ refers to the function's arguments, not the script's

# Functions can return a status code (0-255) with 'return'
# They cannot return strings — use echo or global variables for that
is_root() {
  if [ "$(id -u)" -eq 0 ]; then
    return 0    # True — caller sees $? = 0
  else
    return 1    # False — caller sees $? = 1
  fi
}

if is_root; then
  echo "Running as root"
else
  echo "Not root — please run with sudo"
  exit 1
fi
```

---

### Slide 3 — Local Variables in Functions

One of the most important function habits: use `local` to scope variables inside functions. Without `local`, function variables pollute the global namespace.

```bash
#!/usr/bin/env bash

# Without local — BAD PRACTICE
bad_function() {
  RESULT="computed value"    # This modifies the global $RESULT
}

# With local — GOOD PRACTICE
good_function() {
  local result="computed value"  # Scoped to this function
  local temp_file="/tmp/func_$$.tmp"
  echo "$result"   # Return by printing; caller uses $()
}

OUTPUT=$(good_function)
echo "Function returned: $OUTPUT"

# Real-world function pattern: process a file
process_user_list() {
  local input_file="$1"
  local count=0

  while IFS=: read -r username _ uid _; do
    if [ "$uid" -ge 1000 ]; then
      echo "Regular user: $username (UID: $uid)"
      count=$((count + 1))
    fi
  done < "$input_file"

  echo "Total regular users: $count"
}

process_user_list /etc/passwd
```

---

### Slide 4 — Input/Output and Redirection in Scripts

Scripts need to handle input from multiple sources and direct output appropriately.

```bash
#!/usr/bin/env bash

# Reading user input
echo -n "Enter your name: "
read -r USERNAME
echo "Hello, $USERNAME"

# Read with a timeout and default value
read -t 10 -r -p "Continue? [Y/n]: " ANSWER
ANSWER="${ANSWER:-Y}"    # Default to Y if empty

# Read silently (for passwords)
read -s -r -p "Enter password: " PASSWORD
echo ""    # Newline after silent read

# Standard streams:
# stdin  = file descriptor 0 (keyboard by default)
# stdout = file descriptor 1 (terminal by default)
# stderr = file descriptor 2 (terminal by default)

# Redirect stdout to file
ls /var/log > /tmp/loglist.txt

# Append stdout to file
echo "New entry" >> /tmp/loglist.txt

# Redirect stderr to file
ls /nonexistent 2> /tmp/errors.txt

# Redirect both stdout and stderr to same file
ls /var/log /nonexistent > /tmp/output.txt 2>&1

# Redirect stdout to stderr (for error messages in scripts)
echo "ERROR: Something went wrong" >&2

# Discard output
ls /nonexistent 2>/dev/null

# Pipe output to another command
ps aux | grep nginx | grep -v grep
```

---

### Slide 5 — Exit Codes

Exit codes are how commands and scripts communicate success or failure to the calling process or user. Every command returns an exit code between 0 and 255.

- **0** = success
- **Non-zero** = failure (specific code meaning varies by program)

```bash
#!/usr/bin/env bash

# Check exit code of last command
ls /tmp
echo "$?"    # 0 = success

ls /nonexistent 2>/dev/null
echo "$?"    # 2 = No such file or directory

# Exit a script with a specific code
exit 0       # Success
exit 1       # General error
exit 2       # Misuse of shell builtin

# Common exit code conventions:
# 0    — success
# 1    — general error
# 2    — misuse of shell command
# 126  — command invoked cannot execute
# 127  — command not found
# 128  — invalid exit argument
# 128+N — terminated by signal N
# 130  — terminated by Ctrl+C (128 + 2 for SIGINT)

# Script with proper exit codes
check_service() {
  local service="$1"
  if systemctl is-active "$service" &>/dev/null; then
    echo "$service is running"
    return 0
  else
    echo "$service is NOT running" >&2
    return 1
  fi
}

check_service nginx
STATUS=$?
if [ "$STATUS" -ne 0 ]; then
  echo "Alerting on-call team..." >&2
  exit 1
fi
```

---

### Slide 6 — Error Handling Best Practices

Professional scripts fail loudly and early rather than silently continuing after an error.

```bash
#!/usr/bin/env bash

# set -e — exit immediately if any command returns non-zero
set -e

# set -u — treat unset variables as errors (prevents typo bugs)
set -u

# set -o pipefail — pipe fails if any command in the pipe fails
# Without this: cmd1 | cmd2 exits 0 even if cmd1 fails
set -o pipefail

# Combined (standard best practice header for scripts):
set -euo pipefail

# Custom error handler with trap
cleanup() {
  echo "Script exiting. Cleaning up..."
  rm -f /tmp/myscript_$$.tmp
}
trap cleanup EXIT    # Runs cleanup on any exit

# Error reporting function
die() {
  echo "ERROR: $1" >&2
  exit "${2:-1}"    # Exit with provided code, or 1 by default
}

# Usage with die
CONFIG="/etc/myapp/config.conf"
[ -f "$CONFIG" ] || die "Config file not found: $CONFIG" 2

# Handling expected failures (prevent set -e from catching them)
if grep -q "pattern" /etc/passwd 2>/dev/null; then
  echo "Found pattern"
fi
# grep returns 1 if not found — without the 'if', set -e would exit

# Or use || to handle the error case inline
grep "root" /etc/passwd || echo "root not found (unexpected)"
```

---

### Slide 7 — Practical Script: System Health Check

Let's put everything together into a real script.

```bash
#!/usr/bin/env bash
# system_health.sh — Basic system health report
# Usage: ./system_health.sh [--email address]

set -euo pipefail

# Configuration
REPORT_FILE="/tmp/health_report_$$.txt"
EMAIL=""

# Parse arguments
while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --email)
      EMAIL="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

# Functions
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

check_disk() {
  log "Disk usage:"
  df -h / | tail -1 | awk '{print "  Root FS: " $5 " used (" $3 " of " $2 ")"}'
}

check_memory() {
  log "Memory usage:"
  free -h | grep Mem | awk '{print "  RAM: " $3 " used of " $2}'
}

check_load() {
  log "System load:"
  uptime | awk -F'load average:' '{print "  Load avg:" $2}'
}

check_services() {
  log "Critical service status:"
  for svc in sshd cron; do
    if systemctl is-active "$svc" &>/dev/null; then
      echo "  $svc: RUNNING"
    else
      echo "  $svc: STOPPED (ALERT)"
    fi
  done
}

# Main
{
  echo "=========================================="
  echo " System Health Report — $(hostname)"
  echo " Generated: $(date)"
  echo "=========================================="
  check_disk
  check_memory
  check_load
  check_services
} | tee "$REPORT_FILE"

if [[ -n "$EMAIL" ]]; then
  mail -s "Health Report: $(hostname)" "$EMAIL" < "$REPORT_FILE"
  log "Report emailed to $EMAIL"
fi

log "Report saved to $REPORT_FILE"
```

---

### Slide 8 — Script Debugging

Debugging is an essential skill. Bash provides several built-in debugging mechanisms.

```bash
#!/usr/bin/env bash

# Run a script with debug output (prints each command before executing)
bash -x myscript.sh

# Enable debug mode inside the script
set -x    # Turn on debug trace
set +x    # Turn off debug trace

# Debug a specific section
set -x
problematic_function
set +x

# Verbose mode (prints each line before executing)
bash -v myscript.sh
set -v    # Enable inside script

# Dry run — see what would happen (works for scripts that check flags)
# Many scripts support a --dry-run flag by convention

# Use echo to trace variable values
DEBUG=true
if $DEBUG; then
  echo "DEBUG: VARNAME=$VARNAME" >&2
fi

# shellcheck — static analysis tool (not built-in, but standard)
# Finds common bugs and style issues before you run the script
shellcheck myscript.sh

# Add PS4 for better debug output formatting
export PS4='+(${BASH_SOURCE}:${LINENO}): ${FUNCNAME[0]:+${FUNCNAME[0]}(): }'
set -x
```

---

### Slide 9 — Exam Tips — Shell Scripting

The Linux+ exam tests both reading and writing scripts. Key areas:

```bash
# Know these tests:
# [ -f FILE ]  — regular file
# [ -d DIR ]   — directory
# [ -z STR ]   — empty string
# [ -n STR ]   — non-empty string
# [ NUM -eq NUM ] — integer equality
# [ NUM -gt NUM ] — integer greater than

# Know the difference:
# [ ] = test command (POSIX, works in sh)
# [[ ]] = bash keyword (more features, safer with strings)
# (( )) = arithmetic test (use for numeric comparisons too)

# if (( COUNT > 5 )); then ...  # Arithmetic test
# if [[ "$VAR" =~ ^[0-9]+$ ]]; then ...  # Regex match in [[]]

# Exit code usage in conditionals
if command_that_might_fail; then
  echo "Success"
fi
# is equivalent to:
command_that_might_fail
if [ $? -eq 0 ]; then
  echo "Success"
fi
# The first form is cleaner and preferred

# Common script pattern the exam tests:
#!/usr/bin/env bash
# Check for required argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <username>" >&2
  exit 1
fi
USERNAME="$1"
if ! id "$USERNAME" &>/dev/null; then
  echo "User $USERNAME does not exist" >&2
  exit 2
fi
echo "User $USERNAME found"
```

---

### Slide 10 — Input Validation Pattern

One of the most important scripting patterns: validate all input before using it.

```bash
#!/usr/bin/env bash

# Validate a username argument
validate_username() {
  local username="$1"

  # Check not empty
  [[ -n "$username" ]] || { echo "ERROR: Username cannot be empty" >&2; return 1; }

  # Check valid characters (alphanumeric, underscore, hyphen)
  [[ "$username" =~ ^[a-zA-Z0-9_-]+$ ]] || {
    echo "ERROR: Invalid username characters" >&2
    return 1
  }

  # Check length
  [[ "${#username}" -le 32 ]] || {
    echo "ERROR: Username too long (max 32 chars)" >&2
    return 1
  }

  return 0
}

# Validate a port number
validate_port() {
  local port="$1"
  if [[ "$port" =~ ^[0-9]+$ ]] && [ "$port" -ge 1 ] && [ "$port" -le 65535 ]; then
    return 0
  else
    echo "ERROR: Invalid port number: $port" >&2
    return 1
  fi
}

# Usage
USERNAME="${1:-}"
validate_username "$USERNAME" || exit 1
echo "Valid username: $USERNAME"
```

---

### Slide 11 — Module 09 Wrap-Up

You now have a complete bash scripting toolkit:

- Shebang, variables, quoting — the foundations
- `if/elif/else`, `case` — decision making
- `for`, `while`, `until` — iteration
- Functions with `local` variables — code organization
- Stdin/stdout/stderr, redirection, pipes — I/O handling
- Exit codes — communicating success and failure
- `set -euo pipefail` and `trap` — robust error handling
- `bash -x` and `shellcheck` — debugging

Head to the Reading Guide for a complete syntax reference, then complete the Lab where you will write several scripts of increasing complexity, culminating in a complete system administration script.

Module 10 covers Package Management — see you there.
