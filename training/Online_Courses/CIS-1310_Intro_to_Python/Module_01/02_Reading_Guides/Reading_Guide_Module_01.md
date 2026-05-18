# Reading Guide: Module 1 — Introduction to Python Programming

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 1 — Introduction to Python
**Estimated Reading Time:** 45–60 minutes
**OER Resources:** [edube.org](https://edube.org/) | [Python 3 Official Docs](https://docs.python.org/3/tutorial/index.html)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain what Python is, who created it, and why it is widely used in industry
2. Set up a working Python environment using Google Colab or a local installation
3. Write and execute a Python program using the `print()` function
4. Apply correct Python syntax rules including indentation and case sensitivity
5. Write single-line and multi-line comments in Python
6. Distinguish between interactive mode and script mode
7. Identify the purpose of PEP 8 and apply its core naming conventions

---

## Section 1: What Is Python?

Python is a **high-level, interpreted, general-purpose programming language** created by **Guido van Rossum** and first released in **1991**. The name "Python" was not inspired by the snake — van Rossum named it after the British comedy group *Monty Python's Flying Circus*, whose work he was reading during development.

### Python's Key Characteristics

| Characteristic | Explanation |
|---|---|
| **Interpreted** | Python code is executed line-by-line at runtime rather than compiled to machine code ahead of time |
| **High-Level** | Python manages memory and low-level hardware details for you |
| **Dynamically Typed** | You do not declare variable types — Python determines them at runtime |
| **Object-Oriented** | Everything in Python is an object; OOP principles are fully supported |
| **General-Purpose** | Used for web development, data science, AI/ML, automation, cybersecurity, and more |

### Python 2 vs. Python 3

Python 2 and Python 3 are **not fully compatible**. Python 2 officially reached **end-of-life on January 1, 2020**, meaning it no longer receives security updates or bug fixes. All new development, all major libraries, and all certification exams — including PCAP — use **Python 3**.

> **PCAP Exam Tip:** The PCAP exam tests Python 3 exclusively. If you encounter Python 2 syntax such as `print "Hello"` (without parentheses), recognize it as outdated and incorrect in Python 3. In Python 3, `print` is a function and always requires parentheses.

### Where Is Python Used?

- **Data Science & AI:** NumPy, Pandas, TensorFlow, PyTorch, scikit-learn
- **Web Development:** Django, Flask, FastAPI
- **Automation & Scripting:** System administration, DevOps, test automation
- **Cybersecurity:** Penetration testing tools, malware analysis, SIEM scripting
- **Finance:** Algorithmic trading, quantitative modeling

---

## Section 2: How Python Works — The Execution Model

Understanding how Python executes your code is essential for interpreting error messages and debugging.

### Step-by-Step Python Execution

1. You write source code in a `.py` file or interactive session
2. Python compiles your source code to **bytecode** (`.pyc` files stored in `__pycache__/`)
3. The **Python Virtual Machine (PVM)** interprets the bytecode instruction by instruction
4. Results appear in your terminal, browser, or output area

```
Source Code (.py)  →  Bytecode (.pyc)  →  Python VM  →  Output
```

This is why Python is called "interpreted" — evaluation happens at runtime, not before execution begins. This also means errors can appear mid-run if an earlier line succeeds but a later one fails.

> **Key Distinction:** Compiled languages like C or C++ convert all source code to machine-specific binary *before* running. Python's approach trades some speed for portability and faster development cycles.

---

## Section 3: Setting Up Your Python Environment

You have three options for this course. **Google Colab is strongly recommended** for beginners — it requires no installation and works in any modern browser.

### Option A: Google Colab (Recommended for This Course)

Google Colab is a free, cloud-based Python environment provided by Google.

**Setup Steps:**
1. Open a browser and go to [https://colab.research.google.com/](https://colab.research.google.com/)
2. Sign in with your Google account (or your Texas Wesleyan Google Workspace account)
3. Click **"New Notebook"** in the top-left corner
4. Type code in a **cell** and press **Shift + Enter** to run it
5. Your notebook saves automatically to Google Drive

**Why Colab for This Course?**
- Zero installation — runs in the browser
- Free cloud computation
- Easy sharing for instructor review
- Always runs Python 3
- Access from any device

### Option B: Local Python Installation

For students who prefer working offline:

1. Download Python 3 from [https://www.python.org/downloads/](https://www.python.org/downloads/) (choose the latest 3.x version)
2. On Windows: During installation, **check the box that says "Add Python to PATH"** — this is a critical step
3. Click through the installer using defaults
4. Open **IDLE** (Python's built-in editor) from your Start Menu or Applications folder

**Verify your installation** by opening a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and typing:

```bash
python --version
```

You should see output like `Python 3.11.x` or similar.

### Option C: VS Code (Professional Development Environment)

VS Code is the editor used by professional Python developers. It is free and available at [https://code.visualstudio.com/](https://code.visualstudio.com/). After installing VS Code, install the **Python extension** from Microsoft via the Extensions panel (Ctrl+Shift+X). This option is recommended as you advance through later modules.

---

## Section 4: Your First Python Program — The `print()` Function

The `print()` function is Python's primary tool for displaying output. It is a **built-in function**, available without importing any module.

### Basic Syntax

```python
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

The text inside the quotation marks is called a **string literal**. You may use single quotes (`'`) or double quotes (`"`), but they must match.

### `print()` with Multiple Arguments

Pass multiple items separated by commas:

```python
print("Hello", "World", "from", "Python")
```

**Output:**
```
Hello World from Python
```

By default, `print()` separates multiple arguments with a **single space**.

### The `sep` Parameter — Changing the Separator

Use the `sep` keyword argument to define a custom separator:

```python
print("Python", "is", "fun", sep="-")
```

**Output:**
```
Python-is-fun
```

```python
print("2024", "01", "15", sep="/")
```

**Output:**
```
2024/01/15
```

### The `end` Parameter — Changing the Line Ending

By default, `print()` ends with a **newline character** (`\n`), which moves the cursor to the next line. Use `end` to override this:

```python
print("Hello", end=" ")
print("World")
```

**Output:**
```
Hello World
```

Both `print()` calls appear on the same line because the first ends with a space instead of `\n`.

```python
print("A", end="")
print("B", end="")
print("C")
```

**Output:**
```
ABC
```

### Printing Numbers and Expressions

`print()` accepts any data type:

```python
print(42)           # Integer
print(3.14)         # Float
print(2 + 3)        # Expression — Python evaluates first, then prints
print(10 / 3)       # Division — note floating-point result
print(True)         # Boolean
```

**Output:**
```
42
3.14
5
3.3333333333333335
True
```

> **PCAP Exam Tip:** `print()` always **returns `None`**. If you assign `x = print("Hello")`, the string "Hello" is displayed, but `x` is `None`, not a string. This is a frequent exam trick question.

---

## Section 5: Comments in Python

Comments are lines in your code that Python **ignores entirely during execution**. They are essential for documentation, explaining logic, and temporarily disabling code during debugging.

### Single-Line Comments — `#`

The `#` symbol marks everything after it on that line as a comment:

```python
# This entire line is a comment
print("Hello")    # This is an inline comment — code runs, then comment is ignored
# print("This line is disabled and will not run")
```

### Multi-Line Strings Used as Comments — `'''` or `"""`

Python does not have a dedicated multi-line comment syntax. However, triple-quoted strings are commonly used for this purpose:

```python
"""
This block is treated as a string literal.
If not assigned to a variable, Python creates and discards it.
In practice, it functions like a multi-line comment.
"""
print("After the comment block")
```

> **Important Distinction:** Triple-quoted strings (`"""` or `'''`) are technically **string literals** evaluated by Python, not true comments. True comments (`#`) are stripped before the interpreter ever sees the code. For large blocks, using `#` on each line is technically more correct, but triple-quoted strings are widely accepted in practice.

---

## Section 6: Python Syntax Fundamentals

### Case Sensitivity

Python is **case-sensitive**. `print`, `Print`, and `PRINT` are three different identifiers:

```python
print("This works correctly")
Print("This raises a NameError — capital P is not recognized")
```

### Indentation — Python's Most Distinctive Syntax Rule

In Python, **indentation defines code blocks**. Most languages use curly braces `{}` — Python uses whitespace. This is not optional; it is required syntax.

```python
if True:
    print("This line is inside the if block — indented 4 spaces")
print("This line is outside the if block — no indentation")
```

Incorrect indentation raises an `IndentationError`:

```python
if True:
print("This will cause IndentationError — missing indentation")
```

**PEP 8 Standard:** Use **4 spaces** per indentation level. Do not use tabs. Do not mix tabs and spaces (Python 3 will raise a `TabError`).

### Statements

Each statement goes on its own line. Semicolons are not required (though they are technically valid):

```python
x = 5
y = 10
print(x + y)
```

Placing multiple statements on one line with semicolons is allowed but discouraged by PEP 8:

```python
x = 5; y = 10; print(x + y)   # Valid but poor style — avoid this
```

### Line Continuation

For long lines, use a backslash `\` to continue to the next line:

```python
total = 1 + 2 + 3 + \
        4 + 5 + 6
```

---

## Section 7: Interactive Mode vs. Script Mode

### Interactive Mode (REPL)

REPL stands for **Read-Eval-Print Loop**. Python evaluates each line immediately and displays the result. Start REPL by typing `python` or `python3` in your terminal:

```
$ python3
>>> print("Hello")
Hello
>>> 2 + 3
5
>>> type(42)
<class 'int'>
>>> exit()
$
```

**Use REPL for:** Quick experiments, checking syntax, exploring function behavior.

### Script Mode

Save your code in a `.py` file and run the entire file at once:

```bash
python3 my_program.py
```

**Use script mode for:** Complete programs, assignments, anything longer than a few lines.

**Google Colab Notebooks** operate as a hybrid — each cell behaves interactively but cells can run in sequence like a script.

---

## Section 8: Introduction to PEP 8

**PEP 8** (Python Enhancement Proposal #8) is Python's official **coding style guide**, authored by Guido van Rossum. Following PEP 8 makes your code readable, maintainable, and professional. It is a baseline expectation in industry and on the PCAP exam.

**Full PEP 8 Reference:** [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

### Core PEP 8 Naming Conventions (Module 1 Focus)

| Identifier Type | Convention | Example |
|---|---|---|
| Variables and functions | `snake_case` | `first_name`, `calculate_total()` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES = 3` |
| Classes | `PascalCase` (CapWords) | `class StudentRecord:` |
| Modules/files | `lowercase` or `snake_case` | `my_module.py` |
| Private identifiers | `_leading_underscore` | `_internal_value` |

### Other Key PEP 8 Rules

- Maximum line length: **79 characters**
- Two blank lines before and after function/class definitions at the top level
- One blank line between methods inside a class
- No spaces around `=` when used as a keyword argument: `print(end="")` not `print(end = "")`
- Imports go at the top of the file, one per line

> **PCAP Exam Tip:** The exam frequently tests PEP 8 naming conventions. Know that variables and functions use `snake_case`, classes use `PascalCase`, and constants use `UPPER_CASE`. This alone can answer 2–3 exam questions.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **Interpreter** | A program that executes source code directly, line-by-line, at runtime |
| **Bytecode** | Intermediate compiled form of Python source code (`.pyc` files); interpreted by the PVM |
| **PVM** | Python Virtual Machine — the engine that runs Python bytecode |
| **REPL** | Read-Eval-Print Loop — Python's interactive terminal mode |
| **PEP 8** | Python Enhancement Proposal 8 — the official Python style guide |
| **`print()`** | Built-in function that displays output to the console; returns `None` |
| **`#`** | Single-line comment marker — Python ignores everything after `#` on that line |
| **`IndentationError`** | Runtime error raised when code block indentation is missing or inconsistent |
| **`NameError`** | Error raised when a variable or function is referenced before being defined |
| **snake_case** | Naming convention using lowercase letters with underscores between words |
| **PascalCase** | Naming convention where each word begins with a capital letter, no separators |

---

## External Resources

| Resource | Link | What to Read |
|---|---|---|
| Python 3 Official Tutorial | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/index.html) | Sections 1–2 |
| Python Institute Free Training (edube.org) | [edube.org](https://edube.org/) | PE1 Module 1: Introduction to Python |
| Google Colab | [colab.research.google.com](https://colab.research.google.com/) | Your lab environment |
| PEP 8 Style Guide | [peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) | Naming conventions section |
| Python Downloads (local install) | [python.org/downloads/](https://www.python.org/downloads/) | Latest Python 3.x |
| built-in `print()` documentation | [docs.python.org — print()](https://docs.python.org/3/library/functions.html#print) | Full parameter reference |

---

## Self-Check Review Questions

Work through these before attempting the quiz. They mirror the quiz style and difficulty.

1. Guido van Rossum named Python after what, and when did he first release it?
2. Describe the two steps Python takes to execute a `.py` file before producing output.
3. What is the difference between the `sep` and `end` parameters of `print()`?
4. What type of error is raised when a code block has missing or inconsistent indentation?
5. Write a single `print()` statement that produces the output: `TX-WES-2024`
6. Which PEP 8 naming convention applies to class names? To variable names? To constants?
7. Why is triple-quoted text (`"""..."""`) technically different from a `#` comment?

---

*Next Module → Module 2: Variables, Literals, and Data Types*
