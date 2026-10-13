# Video Script: Module 07 - Shell Scripting Fundamentals (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 14 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 07. Shell scripting is how administrators stop doing things manually and start
doing things reliably. Every command you have typed in the last six modules can become a line in
a script. Once it is a script, it can run on a schedule, run on 50 servers, and produce a log
of what it did. By the end of both parts you will be able to write scripts that use variables,
conditionals, loops, and functions, and you will understand how to handle errors and write output
that is useful for monitoring.

---

### Section 1: The Shebang Line and Script Execution

Every bash script starts with a shebang line — the characters #! followed by the path to the
interpreter that should run the file.

[SHOW TERMINAL]

```bash
#!/bin/bash
```

When you execute a script with ./myscript.sh, the kernel reads the first two bytes. If it sees
#!, it passes the file to the interpreter listed on that line. Without the shebang, the kernel
tries to interpret the file itself and usually fails.

```bash
#!/usr/bin/env bash
```

This alternative form uses env to find bash in the PATH. It is more portable — useful when
writing scripts that may run on systems where bash is not at /bin/bash.

To run a script, you need execute permission:

```bash
chmod +x myscript.sh
./myscript.sh
```

Alternatively, you can pass the script to bash directly:

```bash
bash myscript.sh
```

This bypasses the execute permission requirement but ignores the shebang line.

The source command is different:

```bash
source myscript.sh
. myscript.sh
```

source runs the script in the current shell's environment. Variables set inside the script
persist in your current session. Use source for configuration files like .bashrc. Do not use
source for operational scripts that should be isolated.

---

### Section 2: Variables

[SHOW TERMINAL]

```bash
#!/bin/bash
BACKUP_DIR=/var/backups
LOG_FILE=/var/log/backup.log
SERVER_NAME=webserver01
```

Variable names are conventionally uppercase. No spaces around the equal sign — spaces would
cause a syntax error because bash would interpret BACKUP_DIR as a command.

```bash
echo $BACKUP_DIR
echo ${BACKUP_DIR}/today
```

Reference a variable with $NAME or ${NAME}. The curly braces are required when you append
characters immediately after the variable name, as in ${BACKUP_DIR}/today — without braces,
bash would try to expand $BACKUP_DIRtoday which is undefined.

```bash
USER_COUNT=$(who | wc -l)
echo "Current users: $USER_COUNT"
```

Command substitution: $() captures the output of a command and assigns it to a variable.
This is the modern syntax. You may see backticks in older scripts — they do the same thing
but are harder to nest.

```bash
TODAY=$(date +%Y-%m-%d)
BACKUP_NAME="backup_${TODAY}.tar.gz"
echo $BACKUP_NAME
```

Variables can include other variables in double-quoted strings. Single quotes suppress
all substitution.

Special variables:

- $0: The name of the script itself
- $1, $2, ...: Positional parameters (command-line arguments)
- $#: The count of positional parameters
- $@: All positional parameters as separate words
- $?: Exit code of the last command (0 = success)
- $$: PID of the current script

---

### Section 3: Script Arguments

[SHOW TERMINAL]

```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Total arguments: $#"
```

Save this as args_demo.sh, make it executable, and run:

```bash
./args_demo.sh alpha beta gamma
```

$0 = ./args_demo.sh, $1 = alpha, $2 = beta, $# = 3.

Validate that required arguments were provided:

```bash
if [ $# -lt 2 ]; then
    echo "Usage: $0 <source_dir> <dest_dir>"
    exit 1
fi
```

exit 1 stops the script with a non-zero exit code, indicating failure. exit 0 indicates success.
Any exit code other than 0 signals an error to the calling process or script.

---

### Section 4: Conditionals

[SHOW TERMINAL]

```bash
if [ -d /var/backups ]; then
    echo "Backup directory exists"
else
    echo "Creating backup directory"
    mkdir -p /var/backups
fi
```

The [ ] syntax is the test command. The spaces inside the brackets are mandatory — without them
the syntax is invalid.

The [[ ]] syntax is a bash built-in that offers additional features and is less strict about
quoting.

Common test operators:

File tests:
- -f FILE: exists and is a regular file
- -d DIR: exists and is a directory
- -e PATH: exists (file or directory)
- -r FILE: exists and is readable
- -w FILE: exists and is writable
- -x FILE: exists and is executable
- -s FILE: exists and is not empty

String tests:
- -z STRING: string is empty (zero length)
- -n STRING: string is not empty
- STRING1 = STRING2: strings are equal
- STRING1 != STRING2: strings are not equal

Integer comparison:
- -eq: equal
- -ne: not equal
- -lt: less than
- -gt: greater than
- -le: less than or equal
- -ge: greater than or equal

```bash
if [ $? -ne 0 ]; then
    echo "Previous command failed"
    exit 1
fi
```

$? captures the exit code of the last command. This pattern is fundamental to error handling.

---

### Section 5: Loops

[SHOW TERMINAL]

```bash
for SERVER in web01 web02 web03 db01; do
    echo "Checking $SERVER"
    ping -c 1 $SERVER
done
```

The for loop iterates over a list of values. Each iteration assigns the next value to the
loop variable (SERVER here).

```bash
for FILE in /var/log/*.log; do
    echo "Processing $FILE"
    gzip "$FILE"
done
```

Globbing works inside the for list. The loop processes all .log files in /var/log.

```bash
COUNT=1
while [ $COUNT -le 5 ]; do
    echo "Iteration $COUNT"
    COUNT=$((COUNT + 1))
done
```

The while loop continues as long as the condition is true. $((expression)) is bash arithmetic
expansion.

```bash
while read LINE; do
    echo "Processing: $LINE"
done < /etc/hosts
```

Reading a file line by line with a while read loop. The redirection < /etc/hosts feeds the file
into stdin for the while loop.

---

### Section 6: Functions

[SHOW TERMINAL]

```bash
#!/bin/bash

log_message() {
    local TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$TIMESTAMP] $1" | tee -a /var/log/myscript.log
}

check_service() {
    local SERVICE=$1
    if systemctl is-active "$SERVICE" > /dev/null 2>&1; then
        log_message "$SERVICE is running"
        return 0
    else
        log_message "WARNING: $SERVICE is not running"
        return 1
    fi
}

check_service ssh
check_service nginx
```

Functions are defined before they are called. The local keyword limits variable scope to the
function — without local, variables are global to the entire script.

Functions accept arguments the same way scripts do: $1, $2, etc., relative to the function call.

return 0 and return 1 signal success or failure from a function. $? captures the function's
return code just like a command's exit code.

---

### Certification Connection

Shell scripting maps to Linux+ Domain 1.0 (System Management) and Domain 4.0 (Automation and
Scripting). Key exam objectives:

Understand the shebang line and why it matters for script portability.

Know the difference between executing a script directly (./script.sh) and sourcing it (source
script.sh).

Know how to reference variables with $VAR and ${VAR}, and when braces are required.

Know the test flags for files (-f, -d, -e, -r, -w, -x) and the comparison operators for strings
and integers.

Know the difference between break (exit loop) and continue (skip to next iteration).

---

### Transition to Part 2

In Part 2 we cover input/output, error handling, logging patterns, here documents, and practical
script structure. These are the techniques that separate a script that works from a script that
you can trust in production.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
