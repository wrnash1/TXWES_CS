# Video Script: Module 09 — Shell Scripting Fundamentals (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome and Module Overview

Welcome to Module 9. I'm Professor Nash. This module is about shell scripting — the skill that transforms a competent Linux user into a genuine systems administrator.

Manual commands are essential. But real administration means automating repetitive tasks, writing deployment procedures that run consistently without human error, and building tools that other administrators can use. Shell scripting is how all of that gets done in the Linux world.

By the end of both parts you will be able to write complete bash scripts with variables, conditional logic, loops, functions, and proper error handling. You will understand how to debug scripts and how to write scripts that behave predictably — including when things go wrong.

This topic maps to CompTIA Linux+ domain objective 4.1 — Given a scenario, create simple shell scripts.

---

### Slide 2 — The Shebang Line

Every shell script should begin with a shebang (also called a hashbang) — the `#!` characters followed by the path to the interpreter.

```bash
#!/bin/bash
# This tells the kernel: use /bin/bash to interpret this file

#!/usr/bin/env bash
# Better practice on systems where bash may not be at /bin/bash
# /usr/bin/env finds bash wherever it is in the PATH

#!/bin/sh
# POSIX-compliant sh — more portable but fewer features

#!/usr/bin/python3
# Shebangs work for any interpreter, not just bash
```

Without a shebang, the kernel does not know which interpreter to use and will attempt to run the file as a shell script using the current shell — which may or may not be bash, leading to unpredictable behavior.

```bash
# Make a script executable
chmod +x myscript.sh

# Run it by path
./myscript.sh

# Run it by passing to bash directly (shebang not required)
bash myscript.sh

# Run it as a command (if in PATH)
myscript.sh
```

---

### Slide 3 — Variables

Variables in bash store strings and numbers. Bash is untyped — everything is a string unless you use arithmetic context.

```bash
#!/usr/bin/env bash

# Variable assignment (NO spaces around =)
NAME="Alice"
COUNT=0
CONFIG_FILE="/etc/myapp/config.conf"

# Wrong (spaces cause errors):
# NAME = "Alice"   <- ERROR: bash tries to run 'NAME' as a command

# Variable expansion (use $VARNAME or ${VARNAME})
echo "Hello, $NAME"
echo "Config: ${CONFIG_FILE}"

# Braces required when adjacent to characters:
PREFIX="web"
echo "${PREFIX}server"    # webserver (not $PREFIXserver)

# Command substitution — capture output of a command
TODAY=$(date +%Y-%m-%d)
HOSTNAME=$(hostname)
USER_COUNT=$(wc -l < /etc/passwd)
echo "Today: $TODAY, Host: $HOSTNAME, Users: $USER_COUNT"

# Arithmetic expansion
X=5
Y=3
RESULT=$((X + Y))
echo "Sum: $RESULT"
echo "Product: $((X * Y))"
echo "Division: $((X / Y))"    # Integer division only
```

---

### Slide 4 — Special Variables

Bash provides several built-in variables that are essential for writing robust scripts.

```bash
#!/usr/bin/env bash

# $0 — the name of the script
echo "Script name: $0"

# $1, $2, $3... — positional parameters (command-line arguments)
echo "First argument: $1"
echo "Second argument: $2"

# $# — number of arguments
echo "Argument count: $#"

# $@ — all arguments as separate quoted strings
for arg in "$@"; do
  echo "Argument: $arg"
done

# $* — all arguments as a single string
echo "All args: $*"

# $? — exit status of the last command
ls /tmp
echo "ls exit code: $?"

ls /nonexistent 2>/dev/null
echo "ls exit code: $?"    # 2 = file not found

# $$ — PID of the current script (useful for temp files)
TMPFILE="/tmp/myscript_$$.tmp"

# $! — PID of the last background command
sleep 60 &
BG_PID=$!
echo "Background PID: $BG_PID"
kill "$BG_PID"
```

---

### Slide 5 — Quoting Rules

Quoting is one of the most important — and most misunderstood — aspects of bash scripting. Get quoting wrong and your scripts will behave unpredictably.

```bash
#!/usr/bin/env bash

# Double quotes: allow variable expansion and command substitution
NAME="Alice Smith"
echo "Hello, $NAME"       # Hello, Alice Smith
echo "Files: $(ls /tmp)"  # Shows file listing

# Single quotes: literal — NO expansion whatsoever
echo 'Hello, $NAME'       # Hello, $NAME (literal dollar sign)
echo 'Today: $(date)'     # Today: $(date) (literal)

# Always quote variables that may contain spaces
FILE="my document.txt"
ls "$FILE"      # Correct: treats as one argument
ls $FILE        # Wrong: splits on space — looks for 'my' and 'document.txt'

# The golden rule: quote every variable expansion unless you specifically
# need word splitting or glob expansion

# Here-doc: multi-line string
cat << 'EOF'
This text uses single-quoted EOF so $VARIABLES are not expanded.
EOF

cat << EOF
This text uses double-quoted EOF so $NAME is expanded to $NAME.
EOF
```

---

### Slide 6 — Conditional Statements — if/elif/else

```bash
#!/usr/bin/env bash

# Basic if syntax
if [ condition ]; then
  commands
elif [ condition ]; then
  commands
else
  commands
fi

# File test operators
FILE="/etc/passwd"

if [ -f "$FILE" ]; then
  echo "$FILE exists and is a regular file"
fi

if [ -d /var/log ]; then
  echo "/var/log is a directory"
fi

if [ ! -e /tmp/lockfile ]; then
  echo "Lock file does not exist"
fi

# Common file test operators:
# -e FILE   — FILE exists (any type)
# -f FILE   — FILE is a regular file
# -d DIR    — DIR is a directory
# -r FILE   — FILE is readable
# -w FILE   — FILE is writable
# -x FILE   — FILE is executable
# -s FILE   — FILE is not empty (size > 0)
# -L FILE   — FILE is a symbolic link
```

---

### Slide 7 — Test Operators for Strings and Numbers

```bash
#!/usr/bin/env bash

# String comparisons (use double brackets [[ ]] for safety)
NAME="alice"

if [[ "$NAME" == "alice" ]]; then
  echo "Name is alice"
fi

if [[ "$NAME" != "bob" ]]; then
  echo "Name is not bob"
fi

if [[ -z "$NAME" ]]; then    # -z = zero length (empty)
  echo "Name is empty"
fi

if [[ -n "$NAME" ]]; then    # -n = non-zero length (not empty)
  echo "Name is not empty"
fi

# String comparison in double brackets supports glob patterns
if [[ "$NAME" == a* ]]; then
  echo "Name starts with 'a'"
fi

# Integer comparisons (use -eq, -ne, -lt, -le, -gt, -ge)
COUNT=5

if [ "$COUNT" -gt 3 ]; then
  echo "Count is greater than 3"
fi

if [ "$COUNT" -eq 5 ]; then
  echo "Count equals 5"
fi

# Compound conditions
AGE=25

if [[ "$NAME" == "alice" && "$AGE" -ge 18 ]]; then
  echo "Alice is an adult"
fi

if [[ "$COUNT" -lt 0 || "$COUNT" -gt 100 ]]; then
  echo "Count is out of range"
fi
```

---

### Slide 8 — The for Loop

```bash
#!/usr/bin/env bash

# Loop over a list of values
for FRUIT in apple banana cherry; do
  echo "Processing: $FRUIT"
done

# Loop over files in a directory
for FILE in /var/log/*.log; do
  echo "Log file: $FILE"
  echo "Size: $(du -sh "$FILE" | cut -f1)"
done

# C-style numeric loop
for ((i = 1; i <= 5; i++)); do
  echo "Iteration: $i"
done

# Loop using seq
for i in $(seq 1 10); do
  echo "Item $i"
done

# Loop over command-line arguments
for ARG in "$@"; do
  echo "Processing argument: $ARG"
done

# Loop over lines in a file
while IFS= read -r LINE; do
  echo "Line: $LINE"
done < /etc/passwd

# Loop over lines of command output
while IFS= read -r USER; do
  echo "Checking user: $USER"
  id "$USER"
done < <(getent passwd | awk -F: '$3 >= 1000 {print $1}')
```

---

### Slide 9 — The while Loop and until

```bash
#!/usr/bin/env bash

# while loop — runs while condition is TRUE
COUNT=1
while [ "$COUNT" -le 5 ]; do
  echo "Count: $COUNT"
  COUNT=$((COUNT + 1))
done

# until loop — runs while condition is FALSE (opposite of while)
N=10
until [ "$N" -eq 0 ]; do
  echo "Countdown: $N"
  N=$((N - 1))
done
echo "Liftoff!"

# Read from stdin until EOF
while read -r LINE; do
  process_line "$LINE"
done

# Infinite loop with break
while true; do
  echo "Checking service..."
  if systemctl is-active myservice &>/dev/null; then
    echo "Service is running"
    break
  fi
  sleep 5
done

# continue — skip rest of loop body for current iteration
for i in $(seq 1 10); do
  if [ $((i % 2)) -eq 0 ]; then
    continue    # Skip even numbers
  fi
  echo "Odd: $i"
done
```

---

### Slide 10 — The case Statement

`case` is bash's equivalent of a switch statement. It is cleaner than a series of `elif` conditions when matching a variable against multiple patterns.

```bash
#!/usr/bin/env bash

# Basic case syntax
case "$1" in
  start)
    echo "Starting service..."
    systemctl start myservice
    ;;
  stop)
    echo "Stopping service..."
    systemctl stop myservice
    ;;
  restart)
    echo "Restarting service..."
    systemctl restart myservice
    ;;
  status)
    systemctl status myservice
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status}"
    exit 1
    ;;
esac

# Pattern matching in case
OS=$(uname -s)
case "$OS" in
  Linux*)
    echo "Running on Linux"
    ;;
  Darwin*)
    echo "Running on macOS"
    ;;
  CYGWIN*|MINGW*)
    echo "Running on Windows"
    ;;
  *)
    echo "Unknown OS: $OS"
    ;;
esac
```

The double semicolons `;;` are required after each block. The `*)` pattern matches anything — use it as the default case.

---

### Slide 11 — Module 09 Part 1 Summary

In Part 1 we covered the foundations of bash scripting:

- The shebang line and its role in script interpretation
- Variable assignment and expansion — including `${}` braces and `$()` command substitution
- Special variables: `$0`, `$1–$9`, `$#`, `$@`, `$?`, `$$`
- Quoting rules: double quotes allow expansion; single quotes are literal
- `if/elif/else` with file tests, string tests, and numeric tests
- `[ ]` vs `[[ ]]` — prefer `[[ ]]` for string tests in bash
- `for` loops over lists, files, and numeric ranges
- `while` and `until` loops
- `case` statements for multi-way branching

In Part 2 we will cover functions, input/output redirection, exit codes, error handling, and script debugging — completing your toolkit for writing professional-grade bash scripts.
