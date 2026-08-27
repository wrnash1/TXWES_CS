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

**Question 11** (5 points)

A script contains:

```bash
#!/bin/bash
shift
echo "$1"
```

It is called with `./script.sh alpha beta gamma`. What is the output?

A. `alpha`

B. `beta`

C. `gamma`

D. The script exits with an error because shift is called before any positional parameters are used.

**Correct Answer:** B

**Explanation:** `shift` removes the first positional parameter and renumbers the rest. After `shift`, `$1` becomes the original `$2`, which is `beta`. The original `$1` (`alpha`) is discarded. `$3` (`gamma`) becomes the new `$2`. `shift` never causes an error unless you shift more arguments than exist and use `set -e`.

---

**Question 12** (5 points)

Which `while` loop reads each line of a file without splitting on spaces?

A.

```bash
while read line; do echo "$line"; done < file.txt
```

B.

```bash
for line in $(cat file.txt); do echo "$line"; done
```

C.

```bash
while [ $(cat file.txt) ]; do read line; done
```

D.

```bash
read line < file.txt; while [ "$line" ]; do echo "$line"; done
```

**Correct Answer:** A

**Explanation:** The `while read line; done < file.txt` pattern reads one complete line per iteration using redirection. Option B uses command substitution which splits on any whitespace (spaces, tabs, newlines), breaking multi-word lines into separate loop iterations. Option C is syntactically incorrect. Option D reads only the first line. Option A is the standard idiom for line-by-line file processing.

---

**Question 13** (5 points)

A script contains:

```bash
case "$STATUS" in
  running) echo "OK" ;;
  stopped|failed) echo "ALERT" ;;
  *) echo "UNKNOWN" ;;
esac
```

If `STATUS="failed"`, what is the output?

A. `OK`

B. `ALERT`

C. `UNKNOWN`

D. Nothing — the `|` separator is not valid in case patterns.

**Correct Answer:** B

**Explanation:** The `case` statement matches patterns against the variable. The `stopped|failed` pattern uses `|` to specify multiple alternatives — either `stopped` OR `failed` will match this branch. Since `STATUS="failed"` matches `stopped|failed`, the output is `ALERT`. The `*` is a catch-all that only matches if no earlier pattern matched.

---

**Question 14** (5 points)

What does the following test evaluate to when `X=5`?

```bash
[ "$X" -gt 3 ] && [ "$X" -lt 10 ]
```

A. True — both conditions are met.

B. False — `-gt` and `-lt` cannot be used together.

C. True — but only because `-lt 10` is always true when `-gt 3` is true.

D. It depends on whether X is an integer or string.

**Correct Answer:** A

**Explanation:** `-gt` (greater than) and `-lt` (less than) are arithmetic comparison operators used within `[ ]`. When `X=5`, `5 -gt 3` is true AND `5 -lt 10` is true, so the entire compound expression is true. The `&&` short-circuits: if the first `[ ]` were false, the second would not be evaluated. These operators work on integer values; using them with non-numeric strings would produce an error.

---

**Question 15** (5 points)

A script uses `"$@"` to pass arguments to another command. How does `"$@"` differ from `"$*"`?

A. `"$@"` expands to all arguments as a single quoted string; `"$*"` expands each argument as a separate word.

B. `"$@"` expands each argument as a separate quoted word; `"$*"` joins all arguments into one string separated by the first character of `IFS`.

C. There is no difference — `"$@"` and `"$*"` are identical in all contexts.

D. `"$@"` includes the script name as `$0`; `"$*"` does not.

**Correct Answer:** B

**Explanation:** `"$@"` preserves each argument as a separate quoted word — an argument containing spaces remains a single token. `"$*"` joins all arguments into one string using the first character of `IFS` (usually a space) as a separator. When passing arguments to another command, `"$@"` is almost always the correct choice because it preserves argument boundaries. Example: if called with `script.sh "hello world" "foo"`, `"$@"` produces two arguments; `"$*"` produces one string.

---

**Question 16** (5 points)

A script performs cleanup and must run even if the script exits due to an error. Which construct achieves this?

A.

```bash
cleanup() { rm -f /tmp/lockfile; }
set -e
cleanup
```

B.

```bash
cleanup() { rm -f /tmp/lockfile; }
trap cleanup EXIT
```

C.

```bash
cleanup() { rm -f /tmp/lockfile; }
on_exit cleanup
```

D.

```bash
atexit cleanup
```

**Correct Answer:** B

**Explanation:** `trap cleanup EXIT` registers the `cleanup` function to run whenever the script exits, regardless of the reason — normal completion, `exit` command, or `set -e` triggered failure. This is the standard pattern for cleanup in bash scripts. Option A runs cleanup before any other code and before set -e could trigger. `on_exit` and `atexit` are not built-in bash constructs.

---

**Question 17** (5 points)

Which parameter expansion returns a default value of `"production"` if `ENVIRONMENT` is unset or empty, without modifying the variable itself?

A. `${ENVIRONMENT=production}`

B. `${ENVIRONMENT:=production}`

C. `${ENVIRONMENT:-production}`

D. `${ENVIRONMENT:?production}`

**Correct Answer:** C

**Explanation:** `${VAR:-default}` returns the default value if `VAR` is unset or empty, but does NOT modify `VAR`. `${VAR:=default}` also returns the default but additionally assigns it to `VAR`. `${VAR=default}` assigns but only if unset (not if empty). `${VAR:?message}` exits with an error message if `VAR` is unset or empty. For a read-only substitution that leaves the variable unchanged, `:-` is the correct form.

---

**Question 18** (5 points)

A script contains `set -u` at the top. What happens when it references an undefined variable?

A. The undefined variable evaluates to an empty string.

B. The script prints a warning but continues executing.

C. The script exits immediately with an error message.

D. The variable is automatically initialized to 0.

**Correct Answer:** C

**Explanation:** `set -u` (also written as `set -o nounset`) causes bash to treat any reference to an undefined variable as an error, immediately exiting the script with a message like `bash: VARNAME: unbound variable`. Without `set -u`, undefined variables silently expand to an empty string, which can cause subtle bugs. This is one of the recommended "strict mode" settings along with `set -e` and `set -o pipefail`.

---

**Question 19** (5 points)

A script contains:

```bash
OUTPUT=$(grep "ERROR" /var/log/app.log | wc -l)
```

What does `OUTPUT` contain if the command succeeds and finds 7 matching lines?

A. The string `grep "ERROR" /var/log/app.log | wc -l`

B. The integer `7`

C. The full text of the 7 matching lines

D. The exit code of the last command in the pipeline

**Correct Answer:** B

**Explanation:** Command substitution `$(...)` captures the standard output of the enclosed command. The pipeline counts lines matching "ERROR" with `wc -l`, which outputs the count — in this case `7`. The number is stored as the string `"7"` in `OUTPUT` (bash variables are untyped strings). Arithmetic comparisons like `[ "$OUTPUT" -gt 5 ]` will treat it as an integer.

---

**Question 20** (5 points)

Which statement about bash arrays is correct?

A. Bash arrays are declared with `array = (item1 item2)` — spaces are optional around the `=`.

B. Accessing an undefined array index returns an error with `set -u`.

C. `${#ARRAY[@]}` returns the number of elements in the array.

D. Bash arrays can only hold integer values.

**Correct Answer:** C

**Explanation:** `${#ARRAY[@]}` expands to the count of elements in the array. The `#` prefix with `[@]` means "count all elements." Array declaration uses `array=(item1 item2)` with NO spaces around `=` (spaces would cause a syntax error). With `set -u`, accessing an undefined array index typically returns empty rather than an error. Bash arrays hold strings; they do not enforce a type.

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
| 11 | B |
| 12 | A |
| 13 | B |
| 14 | A |
| 15 | B |
| 16 | B |
| 17 | C |
| 18 | C |
| 19 | B |
| 20 | C |
