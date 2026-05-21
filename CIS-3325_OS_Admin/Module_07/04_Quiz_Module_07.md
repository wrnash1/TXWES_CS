# Quiz: Module 07 - Shell Scripting Fundamentals
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
A bash script begins with `#!/bin/bash` and contains a variable assignment `BACKUP_DIR=/var/backups`. Later, the script references the variable in a command: `mkdir $BACKUP_DIR/today`. What is the correct way to make this script executable and run it?
A) bash script.sh (no execute permission needed)
B) chmod +x script.sh then ./script.sh
C) sh -c script.sh
D) source script.sh
*   **Correct Answer:** B) chmod +x script.sh then ./script.sh
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While `bash script.sh` does work and bypasses the execute permission, it is not the standard production method. The question asks about making the script executable, which requires `chmod +x` and running it as `./script.sh` to use the shebang line.
    *   *Why C is incorrect:* `sh -c` takes a command string as an argument, not a script filename. This syntax is used to pass a shell command inline, not to run a file.
    *   *Why D is incorrect:* `source script.sh` (or `. script.sh`) executes the script in the current shell's environment, inheriting and modifying the current session's variables. This is used for configuration files like `.bashrc`, not for standalone administrative scripts.

---

---

**Question 2**
A script needs to check whether a directory `/data/exports` exists before attempting to write files into it. Which bash conditional correctly tests for a directory?
A) if [ -f /data/exports ]; then
B) if [[ -d /data/exports ]]; then
C) if [ /data/exports exists ]; then
D) if test --directory /data/exports; then
*   **Correct Answer:** B) if [[ -d /data/exports ]]; then
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The `-f` flag tests whether a path exists and is a regular *file*, not a directory. If `/data/exports` is a directory, this test will return false.
    *   *Why C is incorrect:* `exists` is not a valid bash test operator. This statement is a syntax error and will cause the script to abort.
    *   *Why D is incorrect:* The `test` command uses single-dash flags, not double-dash long options. The correct form would be `test -d /data/exports`. `--directory` is not a valid flag for the `test` command.

---

---

**Question 3**
A systems administrator needs to list all currently running processes with CPU and memory statistics. Which command is appropriate?
A) jobs -l
B) ps aux
C) lsof -i
D) top -H
*   **Correct Answer:** B) ps aux
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `jobs -l` lists background jobs started in the current shell session, not all system processes. It shows only processes spawned by the current terminal.
    *   *Why C is incorrect:* `lsof -i` lists open network files and connections. It does not show CPU/memory usage for all running processes.
    *   *Why D is incorrect:* `top -H` displays threads rather than processes and is an interactive monitor rather than a one-shot process listing. `ps aux` is the standard non-interactive snapshot command.

---

**Question 4**
A bash script is designed to back up a directory. After the `cp -r` command, the script should check whether the copy succeeded and print an error message if it failed. Which construct correctly checks the exit code of the previous command?
A) if [ $PIPESTATUS -eq 0 ]; then echo "Success"; fi
B) if [ $? -ne 0 ]; then echo "Backup failed"; exit 1; fi
C) if [ $EXIT -eq 1 ]; then echo "Backup failed"; fi
D) if [ $STATUS != "ok" ]; then echo "Backup failed"; fi
*   **Correct Answer:** B) if [ $? -ne 0 ]; then echo "Backup failed"; exit 1; fi
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `$PIPESTATUS` is an array that holds exit codes of commands in the most recent pipeline (e.g., `cmd1 | cmd2`). A standalone `cp` command does not use a pipeline, so `$PIPESTATUS` is not the appropriate variable here; `$?` is.
    *   *Why C is incorrect:* `$EXIT` is not a special bash variable. There is no automatic variable named `$EXIT`; the correct variable for the last command's exit code is `$?`.
    *   *Why D is incorrect:* `$?` contains an integer exit code, not a string like `"ok"`. Comparing it with a string like `"ok"` will never produce a useful result and is a type mismatch.

---

**Question 5**
A script loops through a list of hostnames and attempts to ping each one. When a ping fails, the script should log the failure and continue to the next hostname rather than stopping. Which loop control statement achieves this?
A) break
B) exit 1
C) continue
D) return
*   **Correct Answer:** C) continue
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `break` exits the entire loop immediately, stopping iteration over all remaining hostnames. The requirement is to skip the current failing hostname and proceed to the next one.
    *   *Why B is incorrect:* `exit 1` terminates the entire script with an error exit code. This stops all processing, the opposite of what is needed.
    *   *Why D is incorrect:* `return` exits the current *function* and passes a return value to the caller. It is not used for loop control in a top-level script context and will produce unexpected behavior outside a function.

