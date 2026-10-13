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

---

Questions 11-20 — 5 pts each

---

**Question 11**

A bash script contains the line #!/usr/bin/env bash as the first line. What is the
advantage of this shebang over #!/bin/bash?

- A) /usr/bin/env bash runs the script in a more secure sandboxed environment.
- B) /usr/bin/env bash searches PATH for the bash executable, making the script portable across systems where bash may not be at /bin/bash.
- C) /usr/bin/env bash enables bash strict mode automatically without needing set -euo pipefail.
- D) /usr/bin/env bash is required for scripts that use arrays and associative arrays.

Correct Answer: B) /usr/bin/env bash searches PATH for the bash executable, making the script portable across systems where bash may not be at /bin/bash.

Distractor Analysis:

- Why A is incorrect: env does not provide sandboxing. Both shebangs run the script with identical permissions. Security is determined by the executing user and file permissions, not the shebang.
- Why C is incorrect: Neither shebang automatically enables strict mode. set -euo pipefail must be explicitly added to the script body regardless of which shebang is used.
- Why D is incorrect: Bash arrays and associative arrays work identically with both shebangs. The array feature availability depends on the bash version, not the shebang path.

---

**Question 12**

What is the output of the following bash snippet?

```bash
X=5
if [ $X -gt 3 ] && [ $X -lt 10 ]; then
  echo "in range"
else
  echo "out of range"
fi
```

- A) out of range
- B) in range
- C) The script errors because -gt and -lt require double brackets [[ ]].
- D) No output — the condition is ambiguous.

Correct Answer: B) in range

Distractor Analysis:

- Why A is incorrect: 5 is greater than 3 (true) AND less than 10 (true), so both conditions are met and the if branch executes, printing "in range".
- Why C is incorrect: -gt and -lt are arithmetic comparison operators that work correctly in both single brackets [ ] and double brackets [[ ]]. Single brackets are POSIX-compliant and work in bash, sh, and dash.
- Why D is incorrect: The condition evaluates cleanly. 5 -gt 3 is true and 5 -lt 10 is true. The && requires both to be true, which they are. The output is unambiguous.

---

**Question 13**

A bash script uses the construct ${VARNAME:-default_value}. What does this parameter
expansion do?

- A) It sets VARNAME to default_value permanently if it is not already set.
- B) It uses default_value if VARNAME is unset or empty, but does not modify VARNAME itself.
- C) It removes the value of VARNAME and replaces it with default_value.
- D) It exports VARNAME as an environment variable with a fallback of default_value.

Correct Answer: B) It uses default_value if VARNAME is unset or empty, but does not modify VARNAME itself.

Distractor Analysis:

- Why A is incorrect: The :- operator does not assign to the variable. It only substitutes the default in the current expression. To assign a default, use the := operator: ${VARNAME:=default_value}.
- Why C is incorrect: :- never removes or replaces the stored value. If VARNAME is set to a non-empty value, that value is used. Only if it is unset or empty does the expansion produce default_value.
- Why D is incorrect: Parameter expansion has no effect on environment variable export status. export VARNAME is the explicit mechanism for that. :- only affects the value used in the current expansion context.

---

**Question 14**

A bash script function is defined as follows:

```bash
check_file() {
  local FILE="$1"
  [ -f "$FILE" ] && return 0 || return 1
}
```

The script calls check_file /etc/passwd. What does the local keyword accomplish?

- A) It marks FILE as read-only so it cannot be modified inside the function.
- B) It limits FILE's scope to within the function, preventing it from overwriting a variable named FILE in the calling script.
- C) It exports FILE to all child processes spawned by the function.
- D) It makes FILE persistent across multiple calls to check_file.

Correct Answer: B) It limits FILE's scope to within the function, preventing it from overwriting a variable named FILE in the calling script.

Distractor Analysis:

- Why A is incorrect: local does not make a variable read-only. readonly FILE=value would make it immutable. local only restricts scope.
- Why C is incorrect: local does the opposite — it restricts the variable to the current function scope and prevents it from being seen by child processes. Exporting requires the export keyword.
- Why D is incorrect: local variables are destroyed when the function returns. Each call to check_file creates a fresh FILE variable initialized to $1. There is no persistence between calls.

---

**Question 15**

Which bash construct is used to iterate over every line in a file named servers.txt and
print each line with a prefix?

- A) for line in servers.txt; do echo "Server: $line"; done
- B) while IFS= read -r line; do echo "Server: $line"; done < servers.txt
- C) read -a line < servers.txt; for s in "${line[@]}"; do echo "Server: $s"; done
- D) cat servers.txt | for line; do echo "Server: $line"; done

Correct Answer: B) while IFS= read -r line; do echo "Server: $line"; done < servers.txt

Distractor Analysis:

- Why A is incorrect: for line in servers.txt iterates over the string "servers.txt" as a single word — it does not read the file's contents. To iterate over file content with for, you would need $(cat servers.txt), which has word-splitting issues with lines containing spaces.
- Why C is incorrect: read -a reads a single line and splits it into array elements. This reads only the first line of servers.txt and splits it on whitespace, not line by line.
- Why D is incorrect: A pipe to a for loop is not valid bash syntax. Pipes feed stdin, and for does not read from stdin in this pattern. The while read idiom with input redirection is the correct approach.

---

**Question 16**

A script uses set -e at the top. The following command is in the script:

grep "ERROR" /var/log/app.log

If no ERROR lines are found, grep exits with code 1. What happens to the script?

- A) The script continues normally because grep is not a critical command.
- B) The script exits immediately because set -e causes the script to terminate on any non-zero exit code.
- C) The script prints a warning and continues because set -e only applies to the last command before exit.
- D) The script retries the grep command up to three times before exiting.

Correct Answer: B) The script exits immediately because set -e causes the script to terminate on any non-zero exit code.

Distractor Analysis:

- Why A is incorrect: set -e treats any non-zero exit code as a fatal error. grep returning 1 (no matches found) is a non-zero exit code and will cause the script to exit, even though it is not an error in the traditional sense.
- Why C is incorrect: set -e applies to every command in the script, not just the last one before explicit exits. To allow a command to fail without triggering set -e, append || true to the command.
- Why D is incorrect: Bash has no automatic retry mechanism. set -e simply exits the script on the first non-zero return code. Retry logic must be explicitly coded.

---

**Question 17**

What does the following bash arithmetic expansion evaluate to?

```bash
echo $((10 % 3))
```

- A) 3
- B) 1
- C) 0
- D) 3.33

Correct Answer: B) 1

Distractor Analysis:

- Why A is incorrect: 10 divided by 3 is 3 remainder 1. The % operator returns the remainder (modulo), not the quotient. The quotient 3 would be the result of $((10 / 3)).
- Why C is incorrect: 0 would result from a number evenly divisible by the divisor (e.g., 9 % 3 = 0). 10 is not evenly divisible by 3.
- Why D is incorrect: Bash integer arithmetic truncates results. Floating point (3.33) is not produced by $(( )). Bash arithmetic only works with integers. For decimal results, use bc or awk.

---

**Question 18**

A bash script must process exactly two command-line arguments. Which check correctly
validates the argument count and exits with an error message if the requirement is not met?

- A) if [ "$#" != 2 ]; then echo "Usage: $0 arg1 arg2" >&2; exit 1; fi
- B) if [ $ARGS -ne 2 ]; then echo "Usage: $0 arg1 arg2"; exit; fi
- C) if [ "$@" -lt 2 ]; then echo "Usage: $0 arg1 arg2" >&2; exit 1; fi
- D) test $1 $2 || exit 1

Correct Answer: A) if [ "$#" != 2 ]; then echo "Usage: $0 arg1 arg2" >&2; exit 1; fi

Distractor Analysis:

- Why B is incorrect: $ARGS is not a special bash variable. The built-in variable for argument count is $#. Also, exit without a code exits with the last command's return value, which may not be 1, and the error message goes to stdout rather than stderr (&2).
- Why C is incorrect: "$@" expands to the list of all arguments. Using -lt (a numeric comparison) on a word list is invalid and will produce an error. $# is the correct variable for counting arguments.
- Why D is incorrect: test $1 $2 with no operator between them is ambiguous and unreliable. Without an explicit comparison operator, this does not reliably check whether exactly two arguments were provided.

---

**Question 19**

A bash script must create a temporary file securely and ensure it is always deleted when
the script exits, even if an error occurs. Which pattern achieves this?

- A) TMPFILE=/tmp/myapp.tmp; trap "rm -f $TMPFILE" EXIT
- B) TMPFILE=$(mktemp); trap "rm -f $TMPFILE" EXIT
- C) TMPFILE=$(mktemp /tmp/myapp.XXXXXX); trap "rm -f $TMPFILE" EXIT
- D) Both B and C are correct

Correct Answer: D) Both B and C are correct

Distractor Analysis:

- Why A is incorrect: Using a predictable filename like /tmp/myapp.tmp is vulnerable to symlink attacks (TOCTOU). An attacker could pre-create that filename as a symlink to a sensitive file, causing the script to overwrite it. mktemp generates a uniquely named temp file atomically.
- Why B alone is partially correct: mktemp without arguments creates a file in /tmp with a random name (e.g., /tmp/tmp.XXXXXXXXXX). Combined with the EXIT trap, this is secure.
- Why C alone is partially correct: mktemp /tmp/myapp.XXXXXX creates a file with a custom prefix and a random suffix. The X characters are replaced with random characters. Both B and C use mktemp securely.

---

**Question 20**

A bash script uses the following here-document to create a configuration file:

```bash
cat > /etc/app/config.conf << 'EOF'
HOST=localhost
PORT=$APP_PORT
LOGDIR=/var/log/app
EOF
```

The single quotes around EOF have a specific effect. What is it?

- A) They prevent the heredoc from being written to the file.
- B) They prevent variable expansion inside the heredoc, so $APP_PORT is written literally as the string "$APP_PORT" rather than being expanded to its value.
- C) They make the heredoc append to the file rather than overwrite it.
- D) They require the EOF delimiter to be on a line with exactly zero leading spaces.

Correct Answer: B) They prevent variable expansion inside the heredoc, so $APP_PORT is written literally as the string "$APP_PORT" rather than being expanded to its value.

Distractor Analysis:

- Why A is incorrect: Quoting the delimiter does not prevent the heredoc from being written. The content is always sent to the command (cat in this case). Quoting only affects variable and command substitution within the body.
- Why C is incorrect: Appending to a file is controlled by >> versus >. The heredoc delimiter quoting has no effect on whether the file is overwritten or appended to.
- Why D is incorrect: Indentation sensitivity is controlled by the <<- operator (which strips leading tabs). The quoted << 'EOF' form does not affect indentation handling. A non-quoted EOF also does not require zero indentation — the delimiter just must match exactly.
