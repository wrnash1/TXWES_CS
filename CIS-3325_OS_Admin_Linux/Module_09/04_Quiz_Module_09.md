# Quiz: Module 09 — Shell Scripting Fundamentals

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. A score of 80 or higher is required to advance to Module 10.

---

**Question 1**

A script begins with the following line:

```bash
#!/usr/bin/env bash
```

What is the purpose of this line?

A. It is a comment that documents the script's interpreter.

B. It tells the kernel which program to use to interpret the script when it is executed directly.

C. It sets environment variables required by the script.

D. It is required for the script to be recognized as executable.

**Correct Answer:** B

**Explanation:** The shebang (`#!`) followed by a path tells the kernel which interpreter to invoke when the script is executed directly (e.g., `./script.sh`). `/usr/bin/env bash` is preferred over `/bin/bash` because it finds bash in the PATH, which is more portable across systems where bash may not be at `/bin/bash`. It is NOT a comment (even though it starts with `#`), and it does not set environment variables or control file permissions.

---

**Question 2**

A script contains these lines:

```bash
NAME="Alice"
echo 'Hello, $NAME'
```

What is the output?

A. `Hello, Alice`

B. `Hello, $NAME`

C. An error — single quotes are not valid in bash

D. `Hello, ` (empty — $NAME is not expanded in single quotes)

**Correct Answer:** B

**Explanation:** Single quotes in bash prevent ALL expansion. The `$NAME` inside single quotes is treated as literal text, not a variable reference. The output is the string `Hello, $NAME` exactly as written. Double quotes `"Hello, $NAME"` would produce `Hello, Alice`.

---

**Question 3**

A script includes:

```bash
RESULT=$((7 * 3 + 2))
echo "$RESULT"
```

What is the output?

A. `7 * 3 + 2`

B. `21`

C. `23`

D. `213`

**Correct Answer:** C

**Explanation:** The `$(( ))` syntax performs integer arithmetic. `7 * 3 = 21`, then `21 + 2 = 23`. Standard mathematical operator precedence applies: multiplication before addition.

---

**Question 4**

Which `if` condition correctly checks whether the variable `FILE` refers to a readable regular file?

A. `if [ -r -f "$FILE" ]; then`

B. `if [ -rf "$FILE" ]; then`

C. `if [ -f "$FILE" ] && [ -r "$FILE" ]; then`

D. `if [ -fr "$FILE" ]; then`

**Correct Answer:** C

**Explanation:** File test operators cannot be combined with a dash (e.g., `-rf` is not valid for test). Compound conditions require separate test expressions connected with `&&`. With `[[ ]]` syntax you could write `[[ -f "$FILE" && -r "$FILE" ]]` as a single expression, but with single brackets you need separate tests.

---

**Question 5**

A script contains:

```bash
for FILE in /var/log/*.log; do
  echo "$FILE"
done
```

The `/var/log/` directory contains no `.log` files. What happens?

A. The loop body never executes.

B. The loop runs once with `FILE` set to the literal string `/var/log/*.log`.

C. The script exits with an error.

D. The loop runs once with `FILE` set to an empty string.

**Correct Answer:** B

**Explanation:** In bash, when a glob pattern matches nothing and the `nullglob` option is not set (the default), the pattern is passed literally as a string. The loop runs once with `FILE="/var/log/*.log"`. To prevent this behavior, use `shopt -s nullglob` before the loop, which makes the loop skip entirely when there are no matches.

---

**Question 6**

What does `$?` contain after this code runs?

```bash
ls /nonexistent_path 2>/dev/null
```

A. The PID of the `ls` process

B. The string "No such file or directory"

C. A non-zero integer indicating the command failed

D. 0 because the error was redirected to `/dev/null`

**Correct Answer:** C

**Explanation:** `$?` holds the exit code of the last command. Redirecting stderr to `/dev/null` silences the error message but does not change the exit code. `ls` returns a non-zero exit code (typically 2) when it cannot find the specified path. Exit codes are about the result of the operation, not where the output went.

---

**Question 7**

A bash function contains:

```bash
process() {
  COUNT=0
  local TEMP="working"
  # ...
}
```

What is the scope of `COUNT` and `TEMP` after `process` returns?

A. Both `COUNT` and `TEMP` are accessible globally.

B. `COUNT` is accessible globally; `TEMP` is not accessible outside the function.

C. Neither `COUNT` nor `TEMP` is accessible outside the function.

D. Both variables are destroyed immediately when the function starts.

**Correct Answer:** B

**Explanation:** In bash, variables without `local` are global by default. `COUNT=0` modifies (or creates) a global variable. `local TEMP="working"` scopes `TEMP` to the function — it is destroyed when the function returns. This is why using `local` for all function-internal variables is a best practice.

---

**Question 8**

Which command would a script use to redirect an error message to stderr rather than stdout?

A. `echo "ERROR: File not found" 1>/dev/null`

B. `echo "ERROR: File not found" 2>&1`

C. `echo "ERROR: File not found" >&2`

D. `stderr "ERROR: File not found"`

**Correct Answer:** C

**Explanation:** `>&2` redirects stdout (file descriptor 1) to file descriptor 2 (stderr). The full form `1>&2` means the same thing; the `1` is implicit. Option A discards the message entirely. Option B redirects stderr to where stdout currently goes (the reverse). Option D is not a valid bash command.

---

**Question 9**

A script has `set -e` at the top. Which code block will cause the script to exit unexpectedly?

A.

```bash
if grep -q "root" /etc/passwd; then
  echo "found"
fi
```

B.

```bash
grep "nobody_matches" /etc/passwd
echo "after grep"
```

C.

```bash
ls /nonexistent 2>/dev/null || true
```

D.

```bash
count=$(wc -l < /etc/passwd)
```

**Correct Answer:** B

**Explanation:** With `set -e`, any command that returns a non-zero exit code causes immediate exit unless it is in a conditional context or followed by `|| true`. In option B, `grep "nobody_matches"` returns exit code 1 (no match), and with `set -e` the script exits before reaching `echo`. Option A is safe because grep is in an `if` condition. Option C is safe because `|| true` prevents non-zero exit from propagating. Option D succeeds.

---

**Question 10**

How do you run a bash script in debug trace mode to see each command as it executes, without modifying the script file?

A. `debug ./script.sh`

B. `bash --debug script.sh`

C. `bash -x script.sh`

D. `./script.sh --trace`

**Correct Answer:** C

**Explanation:** `bash -x script.sh` enables the xtrace option, which prints each command with a `+` prefix before executing it. This is the standard way to trace script execution without modifying the script. `--debug` and `--trace` are not valid bash flags. The xtrace behavior can also be enabled inside a script with `set -x`.

---

**Answer Key Summary**

| Question | Answer |
|---|---|
| 1 | B |
| 2 | B |
| 3 | C |
| 4 | C |
| 5 | B |
| 6 | C |
| 7 | B |
| 8 | C |
| 9 | B |
| 10 | C |
