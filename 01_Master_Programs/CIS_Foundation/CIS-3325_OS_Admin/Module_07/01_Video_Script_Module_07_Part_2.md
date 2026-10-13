# Video Script: Module 07 - Shell Scripting Fundamentals (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 12 minutes
**Part:** 2 of 2 - Hands-On Application

---

### Opening

Welcome back to Part 2 of Module 07. In Part 1 we covered the shebang, variables, positional
parameters, conditionals, loops, and functions. In Part 2 we cover output and logging, error
handling with set -e and trap, here documents, input with read, and we build a complete working
backup script that demonstrates production script structure.

---

### Section 1: Output and Logging

[SHOW TERMINAL]

Scripts should write output that is useful for monitoring. There are two output streams: stdout
(file descriptor 1) and stderr (file descriptor 2).

```bash
echo "Normal message"           # goes to stdout
echo "Error message" >&2        # redirect to stderr
```

For logging to a file:

```bash
LOG=/var/log/myscript.log
echo "$(date) - Starting backup" >> $LOG
```

The >> operator appends. A single > would overwrite the log each run, destroying history.

```bash
exec >> /var/log/myscript.log 2>&1
echo "This and all subsequent output goes to the log"
```

exec redirects all subsequent stdout and stderr in the script to the log file. This is useful
for scripts that run in cron — without output redirection, cron will email the output to root.

---

### Section 2: Error Handling

[SHOW TERMINAL]

```bash
#!/bin/bash
set -e
```

set -e causes the script to exit immediately if any command returns a non-zero exit code.
This prevents scripts from continuing after a failure and making things worse.

```bash
set -u
```

set -u causes the script to exit if you reference an undefined variable. This catches typos
like $BACKUP_DRI instead of $BACKUP_DIR.

```bash
set -o pipefail
```

By default, a pipe returns the exit code of the last command. pipefail makes it return the
exit code of the first command that fails in a pipeline.

Combining these is a best practice:

```bash
#!/bin/bash
set -euo pipefail
```

```bash
trap 'echo "Script failed at line $LINENO" >&2' ERR
```

trap catches a signal or condition and runs a command when it occurs. The ERR trap fires
whenever a command exits with a non-zero code. $LINENO is a special variable containing the
current line number — this makes it easy to find where a script failed.

```bash
trap 'cleanup' EXIT

cleanup() {
    echo "Cleaning up temporary files"
    rm -f /tmp/myscript_$$_temp
}
```

The EXIT trap fires whenever the script exits, whether normally or due to an error. This
guarantees cleanup code always runs.

---

### Section 3: The read Command and User Input

[SHOW TERMINAL]

```bash
read -p "Enter your name: " USERNAME
echo "Hello, $USERNAME"
```

read waits for input from stdin and assigns it to the named variable. -p displays a prompt.

```bash
read -s -p "Enter password: " PASSWORD
echo ""
echo "Password received (not displayed)"
```

-s is silent mode — input is not echoed to the terminal. Essential for password prompts.

```bash
read -t 10 -p "Confirm deletion? (y/n): " CONFIRM
if [ $? -ne 0 ]; then
    echo "Timed out. Aborting."
    exit 1
fi
```

-t sets a timeout in seconds. If the user does not respond, read exits with a non-zero code.

---

### Section 4: Here Documents

[SHOW TERMINAL]

A here document allows you to embed multi-line text in a script without creating a separate file.

```bash
cat << EOF
This is a multi-line
message that will be
sent to the output
EOF
```

The word after << is the delimiter. The document ends when the delimiter appears alone on a line.
The delimiter is case-sensitive and by convention uses EOF (End Of File).

```bash
cat << 'EOF'
This text is NOT expanded: $HOME $USER
Variable substitution is suppressed by quoting the delimiter
EOF
```

Quoting the delimiter with single quotes suppresses variable expansion inside the document.

```bash
mysql -u root -p"$DB_PASS" mydatabase << EOF
SELECT user, host FROM mysql.user;
SHOW DATABASES;
EOF
```

Here documents are commonly used to pass multi-line input to commands like mysql, ssh, or
mail that read from stdin.

---

### Section 5: String Operations

[SHOW TERMINAL]

```bash
FILENAME="backup_2026-01-15.tar.gz"

echo ${#FILENAME}             # Length of string: 24
echo ${FILENAME%%.*}          # Remove longest suffix match: backup_2026-01-15
echo ${FILENAME%.*}           # Remove shortest suffix match: backup_2026-01-15.tar
echo ${FILENAME#backup_}      # Remove shortest prefix match: 2026-01-15.tar.gz
echo ${FILENAME/tar/TAR}      # Replace first occurrence: backup_2026-01-15.TAR.gz
echo ${FILENAME//a/A}         # Replace all occurrences
```

These parameter expansion operators avoid needing external commands like sed for simple
string operations.

```bash
FILE=/var/log/nginx/access.log
echo ${FILE##*/}              # Basename: access.log
echo ${FILE%/*}               # Dirname: /var/log/nginx
```

${VAR##*/} extracts the filename from a path (like basename). ${VAR%/*} extracts the
directory (like dirname). These are frequently used in backup and log rotation scripts.

---

### Section 6: A Complete Backup Script

[SHOW TERMINAL]

Let us put everything together in a production-quality backup script.

```bash
#!/bin/bash
set -euo pipefail

# ---- Configuration ----
SOURCE_DIR="${1:-/home}"
BACKUP_DIR="/var/backups/daily"
LOG="/var/log/backup.log"
RETENTION_DAYS=7
TODAY=$(date +%Y-%m-%d)
BACKUP_FILE="${BACKUP_DIR}/backup_${TODAY}.tar.gz"

# ---- Logging function ----
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $*" | tee -a "$LOG"
}

# ---- Cleanup trap ----
trap 'log "ERROR: Script failed at line $LINENO"' ERR

# ---- Validate source directory ----
if [ ! -d "$SOURCE_DIR" ]; then
    log "ERROR: Source directory $SOURCE_DIR does not exist"
    exit 1
fi

# ---- Create backup directory if needed ----
mkdir -p "$BACKUP_DIR"

# ---- Run the backup ----
log "Starting backup of $SOURCE_DIR to $BACKUP_FILE"
tar -czf "$BACKUP_FILE" "$SOURCE_DIR"
log "Backup completed: $(du -sh $BACKUP_FILE | cut -f1)"

# ---- Remove backups older than retention period ----
log "Removing backups older than $RETENTION_DAYS days"
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime "+$RETENTION_DAYS" -delete

log "Backup process complete"
```

Walk through what each section does:

set -euo pipefail: the safety net — exits on errors, undefined variables, and pipe failures.

${1:-/home}: parameter expansion with default. If $1 is not provided, use /home.

The log function: writes a timestamped line to both stdout and the log file using tee.

trap: if any command fails, logs the line number before the script exits.

-d test: validates the source directory before doing anything destructive.

mkdir -p: creates the backup directory and any missing parent directories. The -p flag
makes it succeed even if the directory already exists.

tar -czf: c=create, z=gzip compress, f=filename.

find with -mtime +7 -delete: removes files older than 7 days as part of retention cleanup.

This script can be called directly or added to cron without modification.

---

### Section 7: Exam Tips for Module 07

Know the difference between chmod +x script.sh (makes executable) and bash script.sh
(runs without execute permission but ignores the shebang).

Know the difference between $@ (all arguments, separate words) and $* (all arguments, one word).

$? is the exit code of the last command. 0 = success. Anything else = failure.

set -e exits the script on the first error. Without it, scripts continue after failures.

break exits the current loop. continue skips to the next iteration. exit exits the script.

local in a function creates a variable scoped to the function. Without local, all variables
in a script are global.

The [ ] and [[ ]] test syntaxes both work. [[ ]] is bash-specific and more forgiving.

---

### Lab Preview

This week's lab has you writing five scripts that demonstrate variables, conditionals, a
for loop, a while loop, a function, error handling with set -e and trap, and a complete
backup script with logging and retention.

---

### Summary

Module 07 covers the complete shell scripting toolkit: shebang, variables, positional parameters,
conditionals, loops, functions, error handling, and production script patterns. Every command
you have learned in the course can now be automated.

Module 08 covers storage management: disk partitioning, LVM (Logical Volume Manager), and RAID.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
