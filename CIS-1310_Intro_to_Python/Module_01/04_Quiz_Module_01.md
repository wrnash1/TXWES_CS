# Quiz: Module 01 — Python Basics & Local Environment

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. These questions are written at or above the difficulty level of the PCAP exam. Read every answer choice carefully before selecting.

---

### Question 1

What correctly describes the internal execution pipeline of CPython when you run `python3 script.py`?

- A) The source code is passed directly to the CPU as machine code with no intermediate step
- B) The source code is compiled to bytecode, which is then interpreted by the Python Virtual Machine
- C) The source code is compiled to a native binary executable, which runs without needing Python installed
- D) The source code is translated line-by-line to machine code and executed simultaneously

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python source code is never passed directly to the CPU. It goes through a compilation step to bytecode first.
- *Why B is correct:* CPython compiles your `.py` source code to `.pyc` bytecode (stored in `__pycache__`), then the Python Virtual Machine (PVM) interprets and executes that bytecode.
- *Why C is incorrect:* Python does not produce a native binary executable. The `.pyc` bytecode still requires Python to be installed and running the PVM to execute.
- *Why D is incorrect:* That describes a pure interpreter with no compilation step. CPython does compile to bytecode first — it does not translate to machine code line-by-line simultaneously.

---

### Question 2

Which of the following best describes **script mode** in Python?

- A) Running Python statements one at a time in an interactive session that immediately prints results
- B) Executing a saved `.py` file from top to bottom through the interpreter
- C) A special debugging mode that pauses execution after every line
- D) A mode that compiles Python code into bytecode and stores it as a standalone executable

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That describes the REPL (interactive shell). In script mode you run a complete file, not one statement at a time.
- *Why B is correct:* Script mode means passing a `.py` file to the interpreter (`python3 myscript.py`), which executes all statements sequentially from top to bottom.
- *Why C is incorrect:* Python has no built-in "pause after every line" mode. That would require an explicit debugger such as `pdb`.
- *Why D is incorrect:* Python compiles to `.pyc` bytecode internally, but that bytecode is not a standalone executable — it still requires the PVM to run.

---

### Question 3

A student opens a terminal and types `python3` then presses Enter. They then type `100 / 4` and press Enter. What appears on the screen?

- A) Nothing — expressions are not printed in the REPL without a `print()` call
- B) `25`
- C) `25.0`
- D) `SyntaxError: invalid syntax`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* In the REPL, expressions are automatically evaluated and their results displayed — no `print()` is needed.
- *Why B is incorrect:* The `/` operator in Python 3 always performs true (float) division, not integer division. `100 / 4` returns `25.0`, not `25`.
- *Why C is correct:* Python 3's `/` operator always returns a `float`. `100 / 4 = 25.0`. To get the integer `25`, you would use `//` (floor division): `100 // 4`.
- *Why D is incorrect:* `100 / 4` is valid Python 3 syntax. No error occurs.

---

### Question 4

Examine the following Python script saved as `output.py`:

```python
name = 'Alice'
name
print('Done')
```

What is displayed when you run `python3 output.py`?

- A) `Alice` followed by `Done`
- B) `Done` only
- C) `name` followed by `Done`
- D) Nothing — the script has a syntax error

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The line `name` alone in a script file does NOT print anything. In the REPL it would display `'Alice'`, but in script mode, expressions must be wrapped in `print()` to produce output.
- *Why B is correct:* In script mode, bare expressions produce no output. Only `print('Done')` generates visible output.
- *Why C is incorrect:* `name` on a line by itself evaluates the variable — it does not print the literal string `'name'`. And even the evaluation produces no output in script mode.
- *Why D is incorrect:* `name` on a line by itself is syntactically valid Python — it is an expression statement. It simply has no side effects.

---

### Question 5

What error does Python raise when it encounters inconsistent indentation in a source file?

- A) `SyntaxError`
- B) `ValueError`
- C) `IndentationError`
- D) `RuntimeError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A `SyntaxError` covers general grammar violations (missing colons, unmatched parentheses, etc.), but inconsistent indentation specifically raises `IndentationError`, which is actually a subclass of `SyntaxError`.
- *Why B is incorrect:* `ValueError` is raised when a function receives an argument of the correct type but an inappropriate value (e.g., `int('hello')`). It has nothing to do with code structure.
- *Why C is correct:* `IndentationError` is the specific exception Python raises when indentation is inconsistent — such as mixing tabs and spaces, or changing indent levels in a way that doesn't match any enclosing block.
- *Why D is incorrect:* `RuntimeError` is a generic exception raised during execution, not during parsing. Indentation is checked at parse time — before any code runs.

---

### Question 6

Which of the following statements about Python's indentation rules is **FALSE**?

- A) Python uses indentation to define code blocks instead of curly braces
- B) The PEP 8 style guide recommends 4 spaces per indentation level
- C) Mixing tabs and spaces in the same Python 3 file causes a `TabError`
- D) Indentation in Python is optional and only affects code readability

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is true (not the answer):* Python definitively uses indentation to define blocks. This is core language syntax, not a style choice.
- *Why B is true (not the answer):* PEP 8 — the official Python style guide — explicitly recommends 4 spaces per indentation level. This is the universal standard in professional Python code.
- *Why C is true (not the answer):* Python 3 raises a `TabError` (a subclass of `IndentationError`) specifically when tabs and spaces are mixed inconsistently.
- *Why D is FALSE and is the correct answer:* Indentation in Python is **mandatory syntax**, not optional. A block with incorrect indentation causes an `IndentationError` and the program will not run. This is the opposite of languages like C or JavaScript where indentation is purely cosmetic.

---

### Question 7

Where does CPython store compiled bytecode files after running a Python script?

- A) In the same directory as the `.py` file, with a `.pyc` extension and the same base name
- B) In a directory called `__pycache__` inside the project folder
- C) In the system's temporary files directory (e.g., `/tmp` on Linux)
- D) In the Python installation directory under `lib/bytecode/`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* In Python 3, `.pyc` files are not placed in the same directory as the source file. They are organized inside `__pycache__` with a naming convention that includes the Python version (e.g., `script.cpython-310.pyc`).
- *Why B is correct:* CPython creates a `__pycache__` subdirectory in the same folder as the source file and stores all `.pyc` bytecode files there. The filename includes the CPython version to allow multiple Python versions to coexist.
- *Why C is incorrect:* Bytecode files are project-specific and stored alongside the source files, not in system temp directories.
- *Why D is incorrect:* Bytecode files for user scripts are never stored in the Python installation directory. They are stored relative to the project's source location.

---

### Question 8

Which command verifies that Python 3 is installed and shows the version number in a Linux or macOS terminal?

- A) `python --version`
- B) `python3 --version`
- C) `py3 -version`
- D) `python3 -v`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* On many Linux systems, `python` still points to Python 2.x. Always use `python3` to target Python 3 explicitly.
- *Why B is correct:* `python3 --version` prints the Python 3 version string (e.g., `Python 3.10.12`) and is the standard command on Linux and macOS.
- *Why C is incorrect:* `py3` is not a standard command on Linux or macOS. `py` (without `3`) is a Windows-specific Python Launcher utility.
- *Why D is incorrect:* `python3 -v` runs Python in verbose mode, which prints a flood of import messages — it does not simply display the version number cleanly.

---

### Question 9

A classmate tells you they installed Python on their computer, but when they type `print 'Hello'` in the REPL, they get a `SyntaxError`. What is the most likely cause?

- A) They have Python 2 installed, not Python 3 — `print` is a statement in Python 2 but a function in Python 3
- B) They forgot to launch the REPL first — this command must be run from a `.py` file
- C) They used single quotes instead of double quotes, which Python 3 does not allow
- D) The `print` function must be imported before it can be used in Python 3

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* In Python 2, `print` was a statement: `print 'Hello'`. In Python 3, `print` is a built-in function and requires parentheses: `print('Hello')`. The `SyntaxError` is the classic symptom of accidentally running Python 2 syntax in a Python 3 interpreter.
- *Why B is incorrect:* The REPL executes statements — there is no requirement that `print` be in a `.py` file. The REPL is a perfectly valid place to use `print()`.
- *Why C is incorrect:* Python 3 accepts both single quotes and double quotes for strings interchangeably. `print('Hello')` and `print("Hello")` are both valid.
- *Why D is incorrect:* `print` is a Python 3 built-in function — it is always available without any import statement.

---

### Question 10

What is the correct way to exit the Python interactive REPL on a Linux system?

- A) Type `quit` and press Enter
- B) Press `Ctrl+C`
- C) Type `exit()` and press Enter, or press `Ctrl+D`
- D) Close the terminal window — there is no graceful exit command

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Typing `quit` alone (without parentheses) in Python 3 displays a hint message saying to use `quit()`, but does not actually exit. The parentheses are required.
- *Why B is incorrect:* `Ctrl+C` sends a `KeyboardInterrupt` signal, which interrupts the current operation and drops back to the `>>>` prompt — it does not exit the REPL.
- *Why C is correct:* Both `exit()` (with parentheses) and `Ctrl+D` (end-of-file signal on Linux/macOS) are correct ways to gracefully exit the Python REPL. On Windows, `Ctrl+Z` followed by Enter also works.
- *Why D is incorrect:* There are multiple graceful ways to exit the REPL. Closing the terminal window is unnecessary and would also terminate any other work in that terminal session.

---

### Question 11

What is the output of the following code when executed as a Python **script** (not in the REPL)?

```python
x = 10
y = 3
x // y
x % y
print(x ** y)
```

- A) `3`, `1`, and `1000` on separate lines
- B) `3` and `1` on separate lines, then `1000`
- C) `1000` only
- D) `SyntaxError` because bare expressions are not allowed in scripts

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `x // y` and `x % y` are bare expression statements in script mode. They are evaluated but produce no output — only `print()` causes output to appear.
- *Why B is incorrect:* Same reasoning — bare expressions in scripts have no output side effect, regardless of their value.
- *Why C is correct:* Only `print(x ** y)` produces output. `10 ** 3 = 1000`. The other two lines are evaluated silently.
- *Why D is incorrect:* Bare expression statements are syntactically valid in Python scripts. They simply do nothing visible. This is a legal no-op pattern.

---

### Question 12

Which Python implementation is specifically targeted by the PCAP certification exam?

- A) PyPy — because it is the fastest Python implementation
- B) Jython — because it runs on the Java Virtual Machine
- C) CPython — the reference implementation distributed at python.org
- D) MicroPython — because it is the most widely deployed version

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* PyPy is a JIT-compiled alternative to CPython known for speed, but it is not the reference implementation and is not the target of the PCAP exam.
- *Why B is incorrect:* Jython compiles Python to Java bytecode and runs on the JVM. It is a niche implementation for Java integration, not the exam target.
- *Why C is correct:* The PCAP exam is explicitly based on CPython — the standard implementation written in C, maintained by the Python Software Foundation, and distributed at python.org. All standard behaviors described in the exam assume CPython.
- *Why D is incorrect:* MicroPython is a lean implementation for embedded systems and microcontrollers (e.g., Raspberry Pi Pico). It is not the exam target and lacks many standard library modules.

---

### Question 13

Examine this sequence of REPL interactions:

```python
>>> message = 'Python is fun'
>>> message
>>> print(message)
```

What is the difference between the output of line 2 (`message`) and line 3 (`print(message)`)?

- A) Line 2 raises a `NameError`; line 3 prints the string value
- B) Line 2 displays `'Python is fun'` (with quotes); line 3 displays `Python is fun` (without quotes)
- C) Both lines display `Python is fun` identically — there is no difference in the REPL
- D) Line 2 displays nothing because bare variable names require `print()`; line 3 displays the value

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `message` was assigned on line 1, so it is defined. No `NameError` occurs on line 2.
- *Why B is correct:* In the REPL, a bare expression displays the `repr()` of the object — for strings, this includes the surrounding quotes. `print()` calls `str()` on its argument and outputs the human-readable value without quotes.
- *Why C is incorrect:* They are subtly different. REPL auto-display shows `'Python is fun'` (repr), while `print()` shows `Python is fun` (str).
- *Why D is incorrect:* This describes script mode behavior. In the REPL, bare variable names absolutely produce output — this is the entire point of the REPL.

---

### Question 14

A Python file named `utils.py` is run with `python3 utils.py`. After execution, which of the following files might be found in the `__pycache__` directory?

- A) `utils.py.cache`
- B) `utils.pyc`
- C) `utils.cpython-311.pyc`
- D) `cache_utils.bin`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `.cache` is not a Python bytecode extension. Python uses `.pyc` for compiled bytecode files.
- *Why B is incorrect:* In Python 2, `.pyc` files were placed directly alongside the `.py` file with the same base name. Python 3 changed this — bytecode files now live in `__pycache__` and include the CPython version in the filename.
- *Why C is correct:* Python 3 bytecode files follow the naming convention `modulename.cpython-XYZ.pyc` where `XYZ` is the Python version (e.g., `311` for Python 3.11). They are stored inside `__pycache__`, not next to the source file.
- *Why D is incorrect:* Python never creates `.bin` files for bytecode. This is an invented filename format.

---

### Question 15

What does the `#` character do in Python source code?

- A) It marks the beginning of a block, similar to `{` in Java or C
- B) It starts a single-line comment — everything after `#` on that line is ignored by the interpreter
- C) It is used to define preprocessor directives, similar to C's `#include`
- D) It causes a `SyntaxError` unless it appears on the very first line of the file

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python uses indentation (not `#` or `{}`) to define code blocks. `#` has no structural role.
- *Why B is correct:* In Python, `#` begins a comment. The interpreter ignores everything from `#` to the end of the line. Comments can appear on their own line or after code on the same line (inline comments).
- *Why C is incorrect:* Python has no preprocessor. C-style `#include` or `#define` directives do not exist in Python.
- *Why D is incorrect:* `#` can appear on any line in a Python file. The first line is sometimes `#!/usr/bin/env python3` (a shebang line, also starting with `#`), but `#` is valid anywhere.

---

### Question 16

Consider the following command run in a Linux terminal:

```bash
python3 -c "print('Hello'); print(2 + 2)"
```

What is the output?

- A) `Hello; print(2 + 2)` — the semicolon is treated as part of the string
- B) `Hello` on one line and `4` on the next line
- C) `SyntaxError` — you cannot use semicolons inside `-c` strings
- D) `Hello4` — both outputs are placed on the same line with no space

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The `"..."` surrounding the entire argument is the shell quoting, not Python. Inside the Python string, `;` separates two Python statements. The `print('Hello')` call creates a separate string — the semicolon is not part of it.
- *Why B is correct:* The `-c` flag allows multiple statements separated by semicolons. `print('Hello')` outputs `Hello` followed by a newline, then `print(2 + 2)` outputs `4` on a new line.
- *Why C is incorrect:* Semicolons are valid Python statement separators. They work in scripts, the REPL, and `-c` strings alike.
- *Why D is incorrect:* Each `print()` call ends with a newline by default (`end='\n'`). Output from two separate `print()` calls appears on separate lines.

---

### Question 17

Which of the following best describes the purpose of a **virtual environment** (`venv`) in Python development?

- A) It runs your Python scripts inside a sandboxed process that cannot access the filesystem
- B) It creates an isolated Python environment with its own packages, separate from the system Python installation
- C) It is a special mode in the Python REPL that prevents variables from being shared between sessions
- D) It is a VirtualBox configuration specifically designed to run Python programs

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A `venv` does not sandbox filesystem access or restrict system calls. It only isolates the Python package environment.
- *Why B is correct:* `python3 -m venv .venv` creates a directory containing a local Python interpreter, `pip`, and a `site-packages` folder. Packages installed inside the venv do not affect the global Python installation and vice versa. This is essential for managing different project dependencies.
- *Why C is incorrect:* `venv` has nothing to do with the REPL or variable scope. It is a project-level tool for dependency isolation.
- *Why D is incorrect:* A Python virtual environment is a directory-based Python tool — it has no connection to VirtualBox or virtual machines.

---

### Question 18

What happens if you run the following file that has a mix of tabs and spaces for indentation under Python 3?

```python
def greet():
    print('Hello')
    print('World')   # NOTE: in the actual file, this line is indented with a TAB, not spaces
```

- A) Python 3 silently normalizes all tabs to spaces and runs successfully
- B) Python 3 raises a `TabError: inconsistent use of tabs and spaces in indentation`
- C) Python 3 raises a `SyntaxError` because functions cannot contain more than one `print()` statement
- D) Python 3 raises a `RuntimeError` when `greet()` is called

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python 3 does NOT silently convert tabs to spaces. Python 2 had this behavior but it caused hard-to-find bugs. Python 3 explicitly forbids mixing tabs and spaces and raises an error.
- *Why B is correct:* Python 3 raises `TabError: inconsistent use of tabs and spaces in indentation` — a subclass of `IndentationError` — when the same block mixes tab and space indentation. This is a parse-time error.
- *Why C is incorrect:* There is no limit on the number of `print()` calls in a function. This is not a Python restriction.
- *Why D is incorrect:* A `TabError` is raised at parse time when the file is loaded — before any function is defined or called. It would not wait until `greet()` is executed.

---

### Question 19

A student writes the following Python script and is surprised by the output. Explain what happens:

```python
name = 'Jordan'
print('My name is', name)
print('Length:', len(name))
print('Uppercase:', name.upper())
```

What is the complete output?

- A) `My name is Jordan`, `Length: 6`, `Uppercase: JORDAN`
- B) `My name is 'Jordan'`, `Length: 6`, `Uppercase: JORDAN`
- C) `My name is Jordan`, `Length: Jordan`, `Uppercase: jordan`
- D) `My name is Jordan` only — `len()` and `.upper()` are not valid on string variables in Python 3

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `print()` with multiple arguments separated by commas adds a space between each. `len('Jordan') = 6`. `'Jordan'.upper() = 'JORDAN'`. All three lines produce exactly the output in option A.
- *Why B is incorrect:* `print('My name is', name)` passes `name` as a separate argument to `print()` — it uses `str(name)` which gives `Jordan` without quotes. Only the REPL's auto-display adds quotes.
- *Why C is incorrect:* `len()` returns an integer (the count of characters), not the string itself. `.upper()` returns the uppercase version, not lowercase.
- *Why D is incorrect:* `len()` is a built-in function that works on any sequence including strings. `.upper()` is a standard string method. Both are always available without any import.

---

### Question 20

What is the correct term for the `>>>` symbol shown in a Python terminal session?

- A) The Python shebang — it tells the OS to use Python 3 to run the file
- B) The REPL prompt — it indicates that the Python interpreter is ready for input
- C) A heredoc marker — it signals that a multi-line string follows
- D) The Python comment prefix used for documentation strings

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The shebang is `#!/usr/bin/env python3` and appears on the first line of a script file — it has no connection to `>>>`.
- *Why B is correct:* `>>>` is the primary prompt of the Python REPL (Read-Eval-Print Loop). When you see `>>>`, Python is waiting for you to type a statement or expression. A secondary continuation prompt (`...`) appears when a multi-line block is open.
- *Why C is incorrect:* Heredocs (`<<<` in bash, `"""` in Python for multi-line strings) are unrelated to `>>>`. The triple `>` prompt is unique to the Python REPL.
- *Why D is incorrect:* Python comments use `#`. Docstrings use triple-quoted strings (`"""..."""`). Neither uses `>>>`.
