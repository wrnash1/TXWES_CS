# Lab 07: Shell Scripting Fundamentals

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 90-120 minutes

---

### Overview

In this lab you will write and execute a series of bash scripts that demonstrate variables,
conditionals, loops, functions, error handling, and production script patterns. You will
build toward a complete backup and cleanup script in the final part.

**What you will practice:**

- Shebang line, chmod +x, and script execution methods
- Variables, positional parameters, and command substitution
- File test and comparison operators in if/then/else blocks
- for and while loops, including line-by-line file reading
- Functions with local variables and return codes
- set -euo pipefail and trap for error handling
- Logging with timestamped output
- Here documents and the read command

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running
- You are logged in as labadmin
- You have a directory for your scripts: mkdir -p ~/lab07 && cd ~/lab07
- You have watched both parts of the Module 07 video lecture

---

### Part 1 - Script Basics

**Step 1.1 - Write and run your first script**

Create the file:

```bash
cat > ~/lab07/hello.sh << 'EOF'
#!/bin/bash
echo "Hello from $0"
echo "Running as user: $(whoami)"
echo "Current date: $(date)"
EOF
```

Set execute permission and run:

```bash
chmod +x ~/lab07/hello.sh
~/lab07/hello.sh
```

Expected output:

```
Hello from /home/labadmin/lab07/hello.sh
Running as user: labadmin
Current date: Mon Jan 15 10:23:45 UTC 2026
```

**Step 1.2 - Demonstrate sourcing versus executing**

```bash
cat > ~/lab07/set_var.sh << 'EOF'
#!/bin/bash
MY_LAB_VAR="set by script"
echo "Inside script: MY_LAB_VAR=$MY_LAB_VAR"
EOF
chmod +x ~/lab07/set_var.sh
```

Execute in a subshell:

```bash
~/lab07/set_var.sh
echo "After execution: MY_LAB_VAR='$MY_LAB_VAR'"
```

The variable is not set in the current shell.

Source the script:

```bash
source ~/lab07/set_var.sh
echo "After source: MY_LAB_VAR='$MY_LAB_VAR'"
```

MY_LAB_VAR is now set in the current shell. This demonstrates why source is used for
configuration files but not operational scripts.

**Step 1.3 - Positional parameters**

```bash
cat > ~/lab07/args.sh << 'EOF'
#!/bin/bash
echo "Script name: $0"
echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Total arguments: $#"
echo "All arguments: $@"
EOF
chmod +x ~/lab07/args.sh
~/lab07/args.sh alpha beta gamma
```

---

### Part 2 - Variables and Conditionals

**Step 2.1 - Write a service check script**

```bash
cat > ~/lab07/check_service.sh << 'EOF'
#!/bin/bash
SERVICE="${1:-ssh}"

if systemctl is-active "$SERVICE" > /dev/null 2>&1; then
    echo "$SERVICE is running"
    exit 0
else
    echo "$SERVICE is NOT running"
    exit 1
fi
EOF
chmod +x ~/lab07/check_service.sh
```

Test with a running service:

```bash
~/lab07/check_service.sh ssh
echo "Exit code: $?"
```

Test with a non-existent service:

```bash
~/lab07/check_service.sh fakesvc
echo "Exit code: $?"
```

Test the default argument:

```bash
~/lab07/check_service.sh
```

**Step 2.2 - File and directory tests**

```bash
cat > ~/lab07/file_checks.sh << 'EOF'
#!/bin/bash
TARGET="${1}"

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <path>"
    exit 1
fi

if [ -e "$TARGET" ]; then
    echo "$TARGET exists"
    if [ -f "$TARGET" ]; then
        echo "  Type: regular file"
        echo "  Size: $(du -sh "$TARGET" | cut -f1)"
        [ -r "$TARGET" ] && echo "  Readable: yes" || echo "  Readable: no"
        [ -w "$TARGET" ] && echo "  Writable: yes" || echo "  Writable: no"
        [ -x "$TARGET" ] && echo "  Executable: yes" || echo "  Executable: no"
    elif [ -d "$TARGET" ]; then
        echo "  Type: directory"
        echo "  Contents: $(ls "$TARGET" | wc -l) items"
    elif [ -L "$TARGET" ]; then
        echo "  Type: symbolic link"
        echo "  Points to: $(readlink "$TARGET")"
    fi
else
    echo "$TARGET does not exist"
fi
EOF
chmod +x ~/lab07/file_checks.sh
~/lab07/file_checks.sh /etc/hosts
~/lab07/file_checks.sh /var/log
~/lab07/file_checks.sh /nonexistent
```

---

### Part 3 - Loops

**Step 3.1 - For loop over a list**

```bash
cat > ~/lab07/check_services.sh << 'EOF'
#!/bin/bash
SERVICES="ssh cron rsyslog"

for SERVICE in $SERVICES; do
    if systemctl is-active "$SERVICE" > /dev/null 2>&1; then
        STATUS="RUNNING"
    else
        STATUS="STOPPED"
    fi
    printf "%-20s %s\n" "$SERVICE" "$STATUS"
done
EOF
chmod +x ~/lab07/check_services.sh
~/lab07/check_services.sh
```

**Step 3.2 - For loop over files**

```bash
cat > ~/lab07/count_logs.sh << 'EOF'
#!/bin/bash
echo "Log files in /var/log:"
echo "--------------------"
for LOGFILE in /var/log/*.log; do
    if [ -f "$LOGFILE" ]; then
        LINES=$(wc -l < "$LOGFILE")
        printf "%-40s %d lines\n" "$(basename $LOGFILE)" "$LINES"
    fi
done
EOF
chmod +x ~/lab07/count_logs.sh
~/lab07/count_logs.sh
```

**Step 3.3 - While loop with counter**

```bash
cat > ~/lab07/countdown.sh << 'EOF'
#!/bin/bash
COUNT="${1:-5}"

while [ "$COUNT" -gt 0 ]; do
    echo "Countdown: $COUNT"
    COUNT=$(( COUNT - 1 ))
done
echo "Launch!"
EOF
chmod +x ~/lab07/countdown.sh
~/lab07/countdown.sh 3
```

**Step 3.4 - While read loop (process a file line by line)**

```bash
cat > ~/lab07/parse_hosts.sh << 'EOF'
#!/bin/bash
echo "Non-comment lines in /etc/hosts:"
while IFS= read -r LINE; do
    if [[ -n "$LINE" && "$LINE" != \#* ]]; then
        echo "  $LINE"
    fi
done < /etc/hosts
EOF
chmod +x ~/lab07/parse_hosts.sh
~/lab07/parse_hosts.sh
```

---

### Part 4 - Functions and Error Handling

**Step 4.1 - Functions with local variables**

```bash
cat > ~/lab07/functions_demo.sh << 'EOF'
#!/bin/bash

log() {
    local LEVEL="$1"
    local MESSAGE="$2"
    local TIMESTAMP
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$TIMESTAMP] [$LEVEL] $MESSAGE"
}

check_free_space() {
    local MOUNT_POINT="${1:-/}"
    local THRESHOLD="${2:-90}"
    local USE_PCT
    USE_PCT=$(df "$MOUNT_POINT" | awk 'NR==2 {print $5}' | tr -d '%')

    if [ "$USE_PCT" -ge "$THRESHOLD" ]; then
        log "WARN" "$MOUNT_POINT is ${USE_PCT}% full (threshold: ${THRESHOLD}%)"
        return 1
    else
        log "INFO" "$MOUNT_POINT is ${USE_PCT}% full — OK"
        return 0
    fi
}

check_free_space /
check_free_space /tmp 95
RESULT=$?
log "INFO" "Last check exit code: $RESULT"
EOF
chmod +x ~/lab07/functions_demo.sh
~/lab07/functions_demo.sh
```

**Step 4.2 - Error handling with set and trap**

```bash
cat > ~/lab07/error_handling.sh << 'EOF'
#!/bin/bash
set -euo pipefail

trap 'echo "ERROR on line $LINENO. Exit code: $?" >&2' ERR
trap 'echo "Script finished (exit $?)" >&2' EXIT

log() {
    echo "$(date '+%H:%M:%S') $*"
}

log "Step 1: Creating temp directory"
TMPDIR=$(mktemp -d)
log "Temp dir: $TMPDIR"

log "Step 2: Creating a test file"
echo "test content" > "$TMPDIR/testfile"

log "Step 3: This command will succeed"
ls "$TMPDIR"

log "Step 4: Cleaning up"
rm -rf "$TMPDIR"

log "Done"
EOF
chmod +x ~/lab07/error_handling.sh
~/lab07/error_handling.sh
```

Now test the ERR trap by triggering a failure:

```bash
cat > ~/lab07/trigger_error.sh << 'EOF'
#!/bin/bash
set -euo pipefail
trap 'echo "ERROR on line $LINENO" >&2' ERR

echo "Step 1: OK"
echo "Step 2: About to fail..."
ls /nonexistent_path_that_does_not_exist
echo "Step 3: This line should NOT appear"
EOF
chmod +x ~/lab07/trigger_error.sh
~/lab07/trigger_error.sh
echo "Script exit code: $?"
```

---

### Part 5 - Complete Backup Script

**Step 5.1 - Write the backup script**

```bash
cat > ~/lab07/backup.sh << 'EOF'
#!/bin/bash
set -euo pipefail

SOURCE_DIR="${1:-/etc}"
BACKUP_BASE="${2:-/tmp/lab07_backups}"
RETENTION_DAYS=3
TODAY=$(date +%Y-%m-%d_%H%M%S)
BACKUP_FILE="${BACKUP_BASE}/backup_${TODAY}.tar.gz"
LOG="${BACKUP_BASE}/backup.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $*" | tee -a "$LOG"
}

trap 'log "FAILED at line $LINENO"' ERR

mkdir -p "$BACKUP_BASE"

if [ ! -d "$SOURCE_DIR" ]; then
    log "ERROR: Source $SOURCE_DIR does not exist"
    exit 1
fi

log "Starting backup: $SOURCE_DIR -> $BACKUP_FILE"
tar -czf "$BACKUP_FILE" "$SOURCE_DIR" 2>/dev/null
SIZE=$(du -sh "$BACKUP_FILE" | cut -f1)
log "Backup complete. Size: $SIZE"

log "Removing backups older than $RETENTION_DAYS days"
REMOVED=0
for OLD_FILE in "$BACKUP_BASE"/backup_*.tar.gz; do
    if [ -f "$OLD_FILE" ] && [ "$OLD_FILE" -ot "$BACKUP_FILE" ]; then
        DAYS_OLD=$(( ( $(date +%s) - $(stat -c %Y "$OLD_FILE") ) / 86400 ))
        if [ "$DAYS_OLD" -gt "$RETENTION_DAYS" ]; then
            rm "$OLD_FILE"
            REMOVED=$(( REMOVED + 1 ))
            log "Removed old backup: $(basename $OLD_FILE)"
        fi
    fi
done
log "Removed $REMOVED old backup(s)"

log "Backup process complete"
EOF
chmod +x ~/lab07/backup.sh
```

**Step 5.2 - Run the backup script**

```bash
~/lab07/backup.sh /etc /tmp/lab07_backups
```

**Step 5.3 - Verify the output**

```bash
ls -lh /tmp/lab07_backups/
cat /tmp/lab07_backups/backup.log
```

**Step 5.4 - Test error handling**

```bash
~/lab07/backup.sh /nonexistent_directory /tmp/lab07_backups
echo "Exit code: $?"
```

---

### Part 6 - Analysis Questions

**Question 1:** Explain the difference between `exit 1` and `return 1` in a bash script. In what context is each used? What happens if you use `return 1` at the top level of a script (outside any function)?

**Question 2:** A colleague writes a script that begins with `#!/bin/bash` but forgets to run `chmod +x` on it. They try to run it with `./myscript.sh` and get "Permission denied." They then try `bash myscript.sh` and it works. Explain the technical difference between these two execution methods and why the second one bypasses the permission check.

**Question 3:** Examine this script fragment:

```bash
BACKUP_DIR=/var/backups
BACKUP_FILE=$BACKUP_DIR/backup_$TODAY.tar.gz
```

If TODAY is an unset variable, what value does BACKUP_FILE get without `set -u`? What happens with `set -u` active? Rewrite the BACKUP_FILE assignment using parameter expansion with a default value so it never produces an empty path segment.

**Question 4:** Explain why the following while loop is dangerous for parsing /etc/passwd and write the corrected version:

```bash
while read LINE; do
    echo $LINE
done < /etc/passwd
```

Two specific problems exist: one with the read command itself and one with the echo command. Identify and fix both.

**Question 5:** You need a script that checks free disk space on three mount points (/, /home, /var) and sends an alert if any is above 85% full. Write the complete script using a for loop and a function that checks a single mount point and returns 0 if OK and 1 if over the threshold. The script should exit with code 1 if any check fails.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.2 showing the difference between execute and source
2. Screenshot of Part 2, Step 2.1 showing the service check script with both running and stopped service outputs and exit codes
3. Screenshot of Part 3, Step 3.4 showing the while read loop output
4. Screenshot of Part 4, Step 4.2 showing the ERR trap output when trigger_error.sh fails
5. Screenshot of Part 5, Step 5.3 showing the backup file listing and log output
6. Screenshot of Part 5, Step 5.4 showing the error handling when source directory does not exist
7. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| Source vs execute demonstration screenshot | 10 |
| Service check script with exit codes screenshot | 10 |
| While read loop screenshot | 10 |
| ERR trap screenshot | 10 |
| Backup script output screenshot | 10 |
| Backup error handling screenshot | 10 |
| Analysis Question 1 (exit vs return) | 5 |
| Analysis Question 2 (chmod and execution methods) | 5 |
| Analysis Question 3 (set -u and default values) | 5 |
| Analysis Question 4 (while read correction) | 10 |
| Analysis Question 5 (disk space check script) | 15 |
| **Total** | **100** |
