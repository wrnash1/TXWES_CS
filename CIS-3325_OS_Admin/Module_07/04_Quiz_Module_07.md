# Quiz: Module 07 - Shell Scripting Fundamentals

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

A bash script begins with #!/bin/bash and contains a variable assignment BACKUP_DIR=/var/backups. Later, the script references the variable in a command: mkdir $BACKUP_DIR/today. What is the correct way to make this script executable and run it?

- A) bash script.sh (no execute permission needed)
- B) chmod +x script.sh then ./script.sh
- C) sh -c script.sh
- D) source script.sh

Correct Answer: B) chmod +x script.sh then ./script.sh

Distractor Analysis:

- Why A is incorrect: While bash script.sh does work and bypasses the execute permission, it is not the standard production method. The question asks about making the script executable, which requires chmod +x and running it as ./script.sh to honor the shebang line.
- Why C is incorrect: sh -c takes a command string as an argument, not a script filename. This syntax is used to pass a shell command inline, not to run a file.
- Why D is incorrect: source script.sh (or . script.sh) executes the script in the current shell's environment, inheriting and modifying the current session's variables. This is used for configuration files like .bashrc, not for standalone administrative scripts.

---

**Question 2**

A script needs to check whether a directory /data/exports exists before attempting to write files into it. Which bash conditional correctly tests for a directory?

- A) if [ -f /data/exports ]; then
- B) if [[ -d /data/exports ]]; then
- C) if [ /data/exports exists ]; then
- D) if test --directory /data/exports; then

Correct Answer: B) if [[ -d /data/exports ]]; then

Distractor Analysis:

- Why A is incorrect: The -f flag tests whether a path exists and is a regular file, not a directory. If /data/exports is a directory, this test will return false.
- Why C is incorrect: exists is not a valid bash test operator. This statement is a syntax error and will cause the script to abort.
- Why D is incorrect: The test command uses single-dash flags, not double-dash long options. The correct form would be test -d /data/exports. --directory is not a valid flag for the test command.

---

**Question 3**

A systems administrator needs to list all currently running processes with CPU and memory statistics. Which command is appropriate?

- A) jobs -l
- B) ps aux
- C) lsof -i
- D) top -H

Correct Answer: B) ps aux

Distractor Analysis:

- Why A is incorrect: jobs -l lists background jobs started in the current shell session, not all system processes. It shows only processes spawned by the current terminal.
- Why C is incorrect: lsof -i lists open network files and connections. It does not show CPU/memory usage for all running processes.
- Why D is incorrect: top -H displays threads rather than processes and is an interactive monitor rather than a one-shot process listing. ps aux is the standard non-interactive snapshot command.

---

**Question 4**

A bash script is designed to back up a directory. After the cp -r command, the script should check whether the copy succeeded and print an error message if it failed. Which construct correctly checks the exit code of the previous command?

- A) if [ $PIPESTATUS -eq 0 ]; then echo "Success"; fi
- B) if [ $? -ne 0 ]; then echo "Backup failed"; exit 1; fi
- C) if [ $EXIT -eq 1 ]; then echo "Backup failed"; fi
- D) if [ $STATUS != "ok" ]; then echo "Backup failed"; fi

Correct Answer: B) if [ $? -ne 0 ]; then echo "Backup failed"; exit 1; fi

Distractor Analysis:

- Why A is incorrect: $PIPESTATUS is an array that holds exit codes of commands in the most recent pipeline. A standalone cp command does not use a pipeline, so $PIPESTATUS is not the appropriate variable; $? is.
- Why C is incorrect: $EXIT is not a special bash variable. There is no automatic variable named $EXIT; the correct variable for the last command's exit code is $?.
- Why D is incorrect: $? contains an integer exit code, not a string like "ok". Comparing it with a string will never produce a useful result and is a type mismatch.

---

**Question 5**

A script loops through a list of hostnames and attempts to ping each one. When a ping fails, the script should log the failure and continue to the next hostname rather than stopping. Which loop control statement achieves this?

- A) break
- B) exit 1
- C) continue
- D) return

Correct Answer: C) continue

Distractor Analysis:

- Why A is incorrect: break exits the entire loop immediately, stopping iteration over all remaining hostnames. The requirement is to skip the current failing hostname and proceed to the next one.
- Why B is incorrect: exit 1 terminates the entire script with an error exit code. This stops all processing, the opposite of what is needed.
- Why D is incorrect: return exits the current function and passes a return value to the caller. It is not used for loop control in a top-level script context and will produce unexpected behavior outside a function.

---

**Question 6**

A systems administrator adds set -euo pipefail to the top of a script. The script runs a command and then continues processing. The command fails silently and the script stops unexpectedly. Which of these three options is the direct cause of the script stopping?

- A) set -u caused the script to stop because an undefined variable was referenced after the failed command.
- B) set -e caused the script to stop because the failed command returned a non-zero exit code.
- C) set -o pipefail caused the script to stop because the command was inside a pipeline.
- D) The script stopped because the trap ERR handler was defined along with set -euo pipefail.

Correct Answer: B) set -e caused the script to stop because the failed command returned a non-zero exit code.

Distractor Analysis:

- Why A is incorrect: set -u causes an exit when a script references a variable that has never been assigned. A failed command producing no output does not trigger set -u unless the failure involves an unset variable.
- Why C is incorrect: set -o pipefail only affects pipeline constructs (cmd1 | cmd2). A standalone command not in a pipeline does not trigger pipefail behavior.
- Why D is incorrect: trap ERR does not cause an exit by itself — it runs a specified command when a non-zero exit code is encountered, but the exit is caused by set -e. Without set -e, the trap ERR fires but the script continues.

---

**Question 7**

A script contains the following function:

```bash
greet() {
    NAME="World"
    echo "Hello, $NAME"
}
NAME="Alice"
greet
echo "After function: $NAME"
```

What does the line After function: print, and how would you fix the function to prevent it from overwriting the global NAME variable?

- A) It prints After function: Alice because functions cannot modify global variables.
- B) It prints After function: World because NAME is global; adding local NAME="World" inside the function would fix it.
- C) It prints After function: because NAME is unset after the function exits.
- D) It prints After function: Alice because the function creates a separate copy of NAME.

Correct Answer: B) It prints After function: World because NAME is global; adding local NAME="World" inside the function would fix it.

Distractor Analysis:

- Why A is incorrect: Functions can and do modify global variables in bash. Without the local keyword, variables inside a function share scope with the rest of the script.
- Why C is incorrect: bash does not unset variables when a function exits unless explicitly coded to do so. The function sets NAME to "World" globally, so it persists after the function returns.
- Why D is incorrect: bash does not create separate variable copies for functions by default. Variables inside functions are global unless declared with the local keyword.

---

**Question 8**

A script needs to accept a directory path as $1 but should use /var/backups as the default if no argument is provided. Which variable assignment correctly implements this default value?

- A) BACKUP_DIR=$1 || /var/backups
- B) BACKUP_DIR="${1:-/var/backups}"
- C) BACKUP_DIR=$(if [ -z $1 ]; then echo /var/backups; fi)
- D) BACKUP_DIR="$1" -d /var/backups

Correct Answer: B) BACKUP_DIR="${1:-/var/backups}"

Distractor Analysis:

- Why A is incorrect: The || operator in a variable assignment is not valid bash syntax for default values. This line would produce a syntax error or incorrect behavior.
- Why C is incorrect: While this would technically work for some cases, it is unnecessarily complex and fragile. The if block inside $() does not handle the case where $1 is set but empty. The parameter expansion ${1:-/var/backups} is the idiomatic and correct approach.
- Why D is incorrect: This is not valid bash syntax. The -d flag after the assignment is interpreted as a separate command argument, not as conditional logic.

---

**Question 9**

An administrator writes a script that includes the line:

```bash
trap 'rm -rf "$TMPDIR"' EXIT
```

Why is the EXIT trap preferable to placing the rm command at the end of the script?

- A) The EXIT trap runs with root privileges, allowing it to delete files the script could not delete otherwise.
- B) The EXIT trap fires when the script exits for any reason — including errors and signals — ensuring cleanup happens even if the script fails partway through.
- C) Commands placed at the end of a script are not guaranteed to run on all Linux distributions, but trap EXIT is portable.
- D) The EXIT trap runs before the last line of the script, ensuring the temp directory is removed before any final log messages.

Correct Answer: B) The EXIT trap fires when the script exits for any reason — including errors and signals — ensuring cleanup happens even if the script fails partway through.

Distractor Analysis:

- Why A is incorrect: trap does not change the privilege level of the commands it runs. The cleanup command runs with the same user permissions as the rest of the script.
- Why C is incorrect: Commands at the end of a script are completely portable and will run on all Linux distributions. The issue is not portability but rather that end-of-script commands are skipped when the script exits early due to an error or set -e.
- Why D is incorrect: The EXIT trap fires after all script code completes, not before the last line. Log messages at the end of the script appear before the EXIT trap runs.

---

**Question 10**

A bash script reads user input with the following command:

```bash
read -sp "Enter password: " USER_PASS
```

What does the -s flag do, and what additional step is required after this command to maintain good terminal usability?

- A) The -s flag saves the input to a secure file. No additional step is needed.
- B) The -s flag enables silent mode so the password is not echoed to the terminal. An echo command should follow to advance the terminal cursor to a new line.
- C) The -s flag requires the user to confirm the password by typing it twice. The script handles the double-entry automatically.
- D) The -s flag sets a 30-second timeout. A check of $? should follow to verify the user responded in time.

Correct Answer: B) The -s flag enables silent mode so the password is not echoed to the terminal. An echo command should follow to advance the terminal cursor to a new line.

Distractor Analysis:

- Why A is incorrect: The -s flag in read does not save anything to a file. It suppresses terminal echo so the typed characters are not displayed. The value is stored in the variable (USER_PASS) in memory.
- Why C is incorrect: read -s does not handle double-entry confirmation. If a script needs password confirmation, the administrator must read the password twice into two separate variables and compare them manually.
- Why D is incorrect: A timeout is set with the -t flag, not -s. For example, read -t 30 sets a 30-second timeout. The -s flag is specifically for suppressing terminal echo.
