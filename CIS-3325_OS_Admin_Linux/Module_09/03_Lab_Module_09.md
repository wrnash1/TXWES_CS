# Lab: Module 09 — Shell Scripting Fundamentals

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Lab Overview

In this lab you will write a series of shell scripts of increasing complexity. You will progress from simple variable and loop exercises to a complete system administration script that incorporates all module concepts. Each script must be saved as a file and tested by running it in your Linux VM.

**Estimated Time:** 90–120 minutes

**Required Environment:** Linux VM with bash installed (any modern distribution). A text editor (nano, vim, or VS Code with SSH extension all work).

---

## Prerequisites

- Completion of Module 09 video lectures (Parts 1 and 2)
- Basic terminal familiarity from previous modules
- A working Linux VM with sudo access

---

## Setup — Create a Lab Working Directory

```bash
mkdir -p ~/scripts_lab/mod09
cd ~/scripts_lab/mod09
```

All scripts in this lab should be created in this directory.

---

## Exercise 1 — Variables and Basic Output

Create a script that demonstrates variable use, command substitution, and special variables.

### Step 1.1 — Create the Script

Create a file named `01_variables.sh`:

```bash
#!/usr/bin/env bash
# 01_variables.sh — Variable demonstration script

set -euo pipefail

# Basic variable assignment
STUDENT_NAME="Your Name Here"    # Change this to your actual name
COURSE="CIS-3325"
MODULE=9

# Command substitution
CURRENT_USER=$(whoami)
CURRENT_DATE=$(date '+%Y-%m-%d')
HOSTNAME_VAR=$(hostname)

# Arithmetic
TOTAL_MODULES=16
REMAINING=$((TOTAL_MODULES - MODULE))

# Output
echo "====================================="
echo "Lab Report"
echo "====================================="
echo "Student:    $STUDENT_NAME"
echo "Course:     $COURSE"
echo "Module:     $MODULE of $TOTAL_MODULES"
echo "Remaining:  $REMAINING modules"
echo "Run by:     $CURRENT_USER"
echo "Date:       $CURRENT_DATE"
echo "Hostname:   $HOSTNAME_VAR"
echo ""
echo "Script name:      $0"
echo "Arguments passed: $#"
echo "Arguments:        $*"
```

### Step 1.2 — Make Executable and Test

```bash
chmod +x 01_variables.sh
./01_variables.sh
./01_variables.sh arg1 arg2
```

**Lab Question 1:** What is the difference between the output of `./01_variables.sh` and `./01_variables.sh arg1 arg2`? Which special variable changed?

---

## Exercise 2 — Conditionals and File Tests

Create a script that accepts a file path as an argument and reports on it.

### Step 2.1 — Create the Script

Create `02_file_check.sh`:

```bash
#!/usr/bin/env bash
# 02_file_check.sh — File inspection script
# Usage: ./02_file_check.sh <path>

set -euo pipefail

# Validate argument count
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <path>" >&2
  echo "Example: $0 /etc/passwd" >&2
  exit 1
fi

TARGET="$1"

echo "Inspecting: $TARGET"
echo "-----------------------------------"

# Check existence
if [ ! -e "$TARGET" ]; then
  echo "RESULT: Path does not exist" >&2
  exit 2
fi

# Check type
if [ -f "$TARGET" ]; then
  echo "Type:       Regular file"
elif [ -d "$TARGET" ]; then
  echo "Type:       Directory"
elif [ -L "$TARGET" ]; then
  echo "Type:       Symbolic link"
else
  echo "Type:       Other (block/char/pipe/socket)"
fi

# Check permissions
if [ -r "$TARGET" ]; then
  echo "Readable:   Yes"
else
  echo "Readable:   No"
fi

if [ -w "$TARGET" ]; then
  echo "Writable:   Yes"
else
  echo "Writable:   No"
fi

if [ -x "$TARGET" ]; then
  echo "Executable: Yes"
else
  echo "Executable: No"
fi

# Ownership
OWNER=$(stat --format="%U" "$TARGET")
GROUP=$(stat --format="%G" "$TARGET")
PERMS=$(stat --format="%a" "$TARGET")

echo "Owner:      $OWNER"
echo "Group:      $GROUP"
echo "Octal mode: $PERMS"

# Size (files only)
if [ -f "$TARGET" ]; then
  SIZE=$(stat --format="%s" "$TARGET")
  echo "Size:       $SIZE bytes"
fi
```

### Step 2.2 — Test with Multiple Paths

```bash
chmod +x 02_file_check.sh
./02_file_check.sh /etc/passwd
./02_file_check.sh /var/log
./02_file_check.sh /nonexistent
./02_file_check.sh /bin/ls
```

**Lab Question 2:** What exit code does the script return when the path does not exist? How could you check this without looking at the script code?

---

## Exercise 3 — Loops and Iteration

Write a script that processes user accounts from the system.

### Step 3.1 — Create the Script

Create `03_user_report.sh`:

```bash
#!/usr/bin/env bash
# 03_user_report.sh — List regular user accounts with details

set -euo pipefail

echo "================================================"
echo " Regular User Account Report"
echo " Generated: $(date)"
echo "================================================"
echo ""
printf "%-20s %-8s %-25s %s\n" "USERNAME" "UID" "HOME DIR" "SHELL"
printf "%-20s %-8s %-25s %s\n" "--------" "---" "--------" "-----"

# Loop through /etc/passwd and process regular users
COUNT=0

while IFS=: read -r username _ uid gid gecos home shell; do
  # Only process regular user accounts (UID >= 1000, exclude nobody)
  if [ "$uid" -ge 1000 ] && [ "$uid" -lt 65534 ]; then
    printf "%-20s %-8s %-25s %s\n" "$username" "$uid" "$home" "$shell"
    COUNT=$((COUNT + 1))
  fi
done < /etc/passwd

echo ""
echo "Total regular users: $COUNT"

# Check for locked accounts
echo ""
echo "Locked accounts (if any):"
LOCKED=0

while IFS=: read -r username password _; do
  if [[ "$password" == !* ]]; then
    echo "  LOCKED: $username"
    LOCKED=$((LOCKED + 1))
  fi
done < /etc/shadow 2>/dev/null || echo "  (Cannot read /etc/shadow — run as root for locked account check)"

if [ "$LOCKED" -eq 0 ]; then
  echo "  None found"
fi
```

### Step 3.2 — Test

```bash
chmod +x 03_user_report.sh
./03_user_report.sh
sudo ./03_user_report.sh    # Run as root to check shadow file
```

---

## Exercise 4 — Functions and Error Handling

Write a script that demonstrates functions, local variables, and proper error handling.

### Step 4.1 — Create the Script

Create `04_service_check.sh`:

```bash
#!/usr/bin/env bash
# 04_service_check.sh — Check status of multiple services
# Usage: ./04_service_check.sh [service1 service2 ...]

set -uo pipefail
# Note: -e is intentionally NOT set here because we check service status
# which returns non-zero for stopped services

# Configuration
SERVICES=("${@:-sshd cron rsyslog}")    # Use args or defaults
REPORT_FILE="/tmp/service_report_$$.txt"
ERROR_COUNT=0

# Logging functions
log() {
  echo "[$(date '+%H:%M:%S')] $*"
}

log_to_file() {
  echo "$*" >> "$REPORT_FILE"
}

# Cleanup on exit
cleanup() {
  log "Cleaning up..."
  rm -f "$REPORT_FILE"
}
trap cleanup EXIT

# Check if systemctl is available
check_systemctl() {
  if ! command -v systemctl &>/dev/null; then
    echo "ERROR: systemctl not found — this script requires systemd" >&2
    exit 1
  fi
}

# Check a single service
check_service() {
  local service_name="$1"
  local status

  if systemctl is-active "$service_name" &>/dev/null; then
    status="RUNNING"
  elif systemctl is-enabled "$service_name" &>/dev/null; then
    status="STOPPED (enabled)"
    ERROR_COUNT=$((ERROR_COUNT + 1))
  else
    status="STOPPED (disabled)"
  fi

  printf "  %-30s %s\n" "$service_name" "$status"
  log_to_file "$service_name: $status"
}

# Main
check_systemctl

log "Service Health Check Started"
echo "=============================="
echo " Service Status Report"
echo " $(date)"
echo "=============================="
echo ""

for SERVICE in "${SERVICES[@]}"; do
  check_service "$SERVICE"
done

echo ""
echo "Errors found: $ERROR_COUNT"
log "Check complete. Errors: $ERROR_COUNT"

# Exit with error count (0 = all good; >0 = some services down)
exit "$ERROR_COUNT"
```

### Step 4.2 — Test

```bash
chmod +x 04_service_check.sh
./04_service_check.sh
echo "Exit code: $?"

# Test with specific services
./04_service_check.sh sshd nginx cron
echo "Exit code: $?"
```

**Lab Question 3:** What does `trap cleanup EXIT` accomplish? What would happen to the temporary report file if the script crashed midway without this trap?

---

## Exercise 5 — Capstone Script: User Onboarding Tool

Write a complete, production-quality user onboarding script that creates a new user account with validation and logging.

### Step 5.1 — Create the Script

Create `05_onboard_user.sh`:

```bash
#!/usr/bin/env bash
# 05_onboard_user.sh — Automated user onboarding
# Usage: sudo ./05_onboard_user.sh <username> <fullname> <group>
# Example: sudo ./05_onboard_user.sh jsmith "John Smith" developers

set -euo pipefail

# ==============================================================================
# Configuration
# ==============================================================================
readonly SCRIPT_NAME="$(basename "$0")"
readonly LOG_FILE="/var/log/user_onboarding.log"
readonly DEFAULT_SHELL="/bin/bash"
readonly MAX_PASS_AGE=90
readonly WARN_DAYS=14
readonly MIN_PASS_AGE=1

# ==============================================================================
# Functions
# ==============================================================================
usage() {
  cat << EOF
Usage: sudo $SCRIPT_NAME <username> <fullname> <group>

Creates a new user account with standard onboarding policy.

Arguments:
  username   Login name (alphanumeric, underscore, hyphen; max 32 chars)
  fullname   Full name in quotes (e.g., "John Smith")
  group      Primary group (must exist)

Example:
  sudo $SCRIPT_NAME jsmith "John Smith" developers

EOF
  exit 1
}

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

die() {
  echo "ERROR: $*" >&2
  log "ERROR: $*"
  exit 1
}

require_root() {
  if [ "$(id -u)" -ne 0 ]; then
    die "This script must be run as root or with sudo"
  fi
}

validate_username() {
  local username="$1"
  [[ -n "$username" ]] || die "Username cannot be empty"
  [[ "$username" =~ ^[a-z][a-z0-9_-]*$ ]] || die "Invalid username: $username (lowercase letters, digits, underscore, hyphen)"
  [[ "${#username}" -le 32 ]] || die "Username too long (max 32 characters)"
  ! id "$username" &>/dev/null || die "User $username already exists"
}

validate_group() {
  local group="$1"
  getent group "$group" &>/dev/null || die "Group does not exist: $group"
}

generate_temp_password() {
  # Generate a random temporary password
  tr -dc 'A-Za-z0-9!@#$' < /dev/urandom | head -c 12
}

create_user() {
  local username="$1"
  local fullname="$2"
  local group="$3"
  local temp_pass

  log "Creating user: $username (Full name: $fullname, Group: $group)"

  # Create the account
  useradd \
    -m \
    -c "$fullname" \
    -s "$DEFAULT_SHELL" \
    -g "$group" \
    "$username"

  # Set temporary password
  temp_pass=$(generate_temp_password)
  echo "$username:$temp_pass" | chpasswd

  # Apply password policy
  chage -m "$MIN_PASS_AGE" -M "$MAX_PASS_AGE" -W "$WARN_DAYS" "$username"

  # Force password change at first login
  chage -d 0 "$username"

  log "User created successfully: $username"
  echo ""
  echo "======================================"
  echo " User Onboarding Complete"
  echo "======================================"
  echo " Username:      $username"
  echo " Full Name:     $fullname"
  echo " Primary Group: $group"
  echo " Home Dir:      /home/$username"
  echo " Shell:         $DEFAULT_SHELL"
  echo " Temp Password: $temp_pass"
  echo " Password expires: Must change at first login"
  echo "======================================"
  echo " IMPORTANT: Communicate temp password securely"
  echo "======================================"
}

# ==============================================================================
# Main
# ==============================================================================
require_root

[ "$#" -eq 3 ] || usage

USERNAME="$1"
FULLNAME="$2"
GROUP="$3"

validate_username "$USERNAME"
validate_group "$GROUP"

create_user "$USERNAME" "$FULLNAME" "$GROUP"

log "Onboarding complete for $USERNAME"
exit 0
```

### Step 5.2 — Test the Script

```bash
chmod +x 05_onboard_user.sh

# Test without root (should fail gracefully)
./05_onboard_user.sh testuser "Test User" developers
echo "Exit code: $?"

# Create a test group first
sudo groupadd testgroup

# Test with valid arguments
sudo ./05_onboard_user.sh testuser "Test User" testgroup
echo "Exit code: $?"

# Verify the account was created
id testuser
sudo chage -l testuser
grep testuser /etc/passwd

# Test duplicate prevention
sudo ./05_onboard_user.sh testuser "Test User" testgroup
echo "Exit code: $?"

# Cleanup
sudo userdel -r testuser
sudo groupdel testgroup
```

---

## Exercise 6 — Debugging Practice

Practice using bash debugging tools on a broken script.

### Step 6.1 — Create a Buggy Script

Create `06_buggy.sh`:

```bash
#!/usr/bin/env bash
# This script has intentional bugs — find and fix them

CONFIG_DIR=/etc/myapp
LOG_DIR=/var/log/myapp

# Bug 1: What happens if the directories don't exist?
for f in $CONFIG_DIR/*.conf; do
  echo Processing: $f
done

# Bug 2: What is wrong with this condition?
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | tr -d '%')
if [ $DISK_USAGE > 80 ]; then
  echo "Disk usage high: $DISK_USAGE%"
fi

# Bug 3: What is wrong here?
backup_file() {
  BACKUP_NAME="$1.bak"
  cp $1 $BACKUP_NAME
  echo "Backed up $1 to $BACKUP_NAME"
}

backup_file /etc/hostname
```

### Step 6.2 — Debug and Fix

```bash
# First, find syntax errors
bash -n 06_buggy.sh

# Run with shellcheck (install if needed)
which shellcheck || sudo apt install shellcheck -y
shellcheck 06_buggy.sh

# Run with debug trace
bash -x 06_buggy.sh 2>&1 | head -30
```

**Lab Question 4:** Identify at least three bugs in `06_buggy.sh` and explain each one. Write the corrected version as `06_fixed.sh`.

---

## Lab Deliverables

Submit the following:

1. Source code of all five scripts (01–05)
2. Terminal output showing successful execution of each script
3. The fixed version of `06_buggy.sh` (named `06_fixed.sh`)
4. Answers to Lab Questions 1–4

---

## Troubleshooting Guide

| Problem | Solution |
|---|---|
| `bash: ./script.sh: Permission denied` | Run `chmod +x script.sh` |
| `bash: ./script.sh: /usr/bin/env: bad interpreter` | Check for Windows line endings: `dos2unix script.sh` |
| `unbound variable` error | Variable used before assignment; add a default with `${VAR:-default}` |
| Script exits immediately | `set -e` is active; a command returned non-zero; add error handling |
| `command not found` in loop | Check variable quoting; an empty variable expands to nothing |
| `shellcheck` not installed | `sudo apt install shellcheck` or `sudo dnf install ShellCheck` |
