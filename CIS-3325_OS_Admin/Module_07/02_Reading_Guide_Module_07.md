# Reading Guide: Module 07 - Shell Scripting Fundamentals
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 07 – Shell Scripting Fundamentals**! This week covers the essentials of bash scripting: variables, control flow, functions, and automation patterns used daily by Linux system administrators. Shell scripting is tested under CompTIA Linux+ XK0-005 Domain 4.0 (Scripting, Containers, and Automation) and appears in scenario-based questions throughout the exam.

As you work through this material you will learn how to write scripts that automate repetitive tasks, validate input with conditionals, iterate with loops, and produce reusable functions — skills that directly translate to real-world administration.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Shebang line (`#!/bin/bash`)**: The first line of a bash script, telling the kernel which interpreter to use. Without it, the script may execute under the default shell (which could be `sh`, `dash`, or another shell with different syntax). Always include `#!/bin/bash` for scripts that use bash-specific syntax. Make the script executable with `chmod +x script.sh` before running it as `./script.sh`.
*   **Variables and quoting**: Variables are assigned without spaces: `NAME="Alice"`. Referenced with `$NAME` or `${NAME}`. Double quotes preserve whitespace and allow variable expansion: `"Hello $NAME"`. Single quotes treat everything literally: `'Hello $NAME'` prints `$NAME` as text. Always quote variable references in conditionals to avoid word-splitting errors when the variable is empty.
*   **Conditionals (`if`/`elif`/`else`)**: Bash conditionals test exit codes. The `[[ ]]` construct is bash-specific and safer than `[ ]`. Common tests: `-f file` (file exists and is a regular file), `-d dir` (directory exists), `-z "$VAR"` (string is empty), `-n "$VAR"` (string is non-empty), `-eq`, `-ne`, `-lt`, `-gt` (integer comparisons). String comparisons use `==` and `!=` inside `[[ ]]`.
*   **Loops (`for`, `while`, `until`)**: `for item in list; do ... done` iterates over a list. `while [ condition ]; do ... done` runs while condition is true. `until [ condition ]; do ... done` runs until condition is true. Use `break` to exit a loop early and `continue` to skip to the next iteration.
*   **Exit codes and `$?`**: Every command returns an exit code. `0` means success; any non-zero value means failure. `$?` holds the exit code of the last command. Proper scripts check exit codes: `if ! cp file dest; then echo "Copy failed"; exit 1; fi`. The `set -e` option causes a script to exit immediately if any command returns a non-zero exit code.
*   **Functions**: Defined with `function_name() { commands; }` or `function function_name { commands; }`. Called by name without parentheses. Arguments passed to functions are accessed as `$1`, `$2`, etc. — just like script arguments. Local variables inside functions should use the `local` keyword to avoid polluting the global scope.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Scripting falls under Linux+ Domain 4.0 (Scripting, Containers, and Automation), worth approximately 15% of the exam. Expect 6–8 questions involving script reading, syntax identification, and debugging.
*   **Know the special variables:** `$0` = script name, `$1`–`$9` = positional parameters, `$#` = number of arguments, `$@` = all arguments as separate words, `$*` = all arguments as a single word, `$$` = current PID, `$?` = last exit code. These appear directly in exam questions.
*   **`test` vs `[[ ]]` trap:** The exam may show `[ $VAR == "value" ]` — this works but fails when `$VAR` is empty due to word-splitting. The exam-safe form is `[[ "$VAR" == "value" ]]`. Know the difference between `-eq` (integer) and `==` (string) comparisons.
*   **`#!/bin/bash` vs `#!/bin/sh`:** `sh` scripts must avoid bash-specific syntax like `[[ ]]`, arrays, and `$( )` process substitution in some implementations. The exam tests whether you know that a script with `#!/bin/sh` that uses bash arrays will fail on systems where `/bin/sh` is `dash`.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers shell scripting comprehensively in chapters 24–36 — these are the most important chapters for this module. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes scripting walkthrough videos demonstrating variables, loops, and functions in practical automation examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 24–27 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), which introduce the concepts of writing, testing, and debugging bash scripts for system administration tasks.
*   **Required Video:** Watch the shell scripting videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates practical bash scripting from basic variable use through loops and functions.

---

### Lab & Command Integration
In this week's hands-on lab you will write a bash script that accepts command-line arguments, uses an if/else conditional to validate input, iterates over a list with a for loop, defines and calls a function, and exits with an appropriate code. Use `bash -x script.sh` to enable trace debugging.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 24–27 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the shell scripting videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
