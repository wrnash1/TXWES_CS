# Reading Guide: Module 01 — Python Basics & Local Environment

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Introduction

Welcome to **Module 01 — Python Basics & Local Environment**. This module lays the foundation for everything you will do in this course. Before you write your first real Python program, you need to understand *how* Python works — not just the syntax, but the underlying execution model that distinguishes Python from other languages. You also need a working local environment so you can practice, experiment, and complete your labs.

This reading guide walks you through the key concepts, vocabulary, exam tips, required resources, and a study checklist. Complete this guide **before** starting the lab. If a term in the glossary is unclear after reading, look it up in the recommended resources before moving on.

---

## 1. High-Yield Glossary

These terms appear on the PCAP exam and throughout this course. Know every one of them cold.

**Python**
A high-level, general-purpose, interpreted programming language created by Guido van Rossum and first released in 1991. Python emphasizes code readability and clean syntax, using indentation rather than curly braces to define code blocks.

**High-Level Language**
A programming language that abstracts away the details of the computer's hardware (registers, memory addresses, machine instructions). Python is high-level — you write human-readable statements, and the interpreter handles the translation to machine operations.

**Interpreted Language**
A language where source code is executed line-by-line by an interpreter at runtime, without a prior compilation step that the developer must trigger. Python is interpreted — you run `python3 myfile.py` and execution begins immediately.

**Compiled Language**
A language where source code is translated entirely into machine code (or bytecode) by a compiler before any execution occurs. Examples: C, C++, Go. The developer runs a compile command first, then runs the resulting binary.

**CPython**
The official, standard implementation of Python, written in C and distributed at python.org. When people say "Python," they mean CPython. It is the implementation targeted by the PCAP exam. Other implementations exist (PyPy, Jython, MicroPython) but are not the default.

**Bytecode**
An intermediate, platform-independent representation of Python source code produced internally by CPython before execution. Bytecode is stored in `.pyc` files inside the `__pycache__` directory. You do not create or manage bytecode manually — Python handles it automatically.

**Python Virtual Machine (PVM)**
The component of CPython that reads and executes bytecode. The PVM is the final step in the execution pipeline: Source Code → Bytecode → PVM → Running Program.

**`__pycache__` Directory**
A folder Python automatically creates inside your project directory to store compiled `.pyc` bytecode files. These speed up subsequent runs of your scripts. You can safely delete this folder — Python will recreate it.

**REPL (Read-Eval-Print Loop)**
An interactive Python session launched by typing `python3` in a terminal. Each statement you type is immediately read, evaluated, and the result printed. The REPL loops back and waits for your next input. Expressions in the REPL are automatically printed without needing `print()`.

**Script Mode**
Running a saved `.py` file through the Python interpreter (`python3 myfile.py`). Python executes the file from top to bottom. Unlike the REPL, script mode does NOT automatically print expression results — you must use `print()` explicitly.

**`.py` File**
A plain text file containing Python source code, saved with a `.py` extension. This is the standard unit of Python programs.

**Indentation**
The use of consistent whitespace at the beginning of lines to define code block structure in Python. Standard is 4 spaces per level (PEP 8). Indentation is syntax in Python — not optional style. Wrong indentation causes `IndentationError`.

**`IndentationError`**
A Python error raised at parse time when indentation is inconsistent or unexpected. Common causes: mixing tabs and spaces, using different indent widths within the same block.

**`SyntaxError`**
A Python error raised when the interpreter cannot parse the source code because it violates Python grammar rules (e.g., missing colon after `if`, unmatched parentheses).

**`print()` Function**
The built-in Python function used to display output to the terminal. Required in script mode to show any value. In the REPL, expressions print automatically, but `print()` still works and is good practice.

**Comment**
A line or portion of a line in Python source code prefixed with `#`. Python ignores everything after `#` on that line. Comments document code for human readers and have no effect on execution.

**PEP 8**
Python Enhancement Proposal 8 — the official Python style guide. Defines conventions for indentation (4 spaces), naming, line length, and more. Professional Python code follows PEP 8.

**`pip`**
Python's package installer. Used to install third-party libraries from PyPI (the Python Package Index). Example: `pip install requests`. On Ubuntu, install via `sudo apt install python3-pip`.

**Virtual Environment (`venv`)**
An isolated Python environment that keeps a project's dependencies separate from system-wide Python packages. Created with `python3 -m venv .venv`. You will use virtual environments in later modules.

**Python 3 vs. Python 2**
Python 2 reached end-of-life on January 1, 2020. It is no longer supported. Python 3 is the current, active version and what this course uses exclusively. Always verify with `python3 --version`.

---

## 2. The Python Execution Pipeline — Visual Reference

Study this diagram until it is automatic:

```text
Your Source Code (.py file)
          |
          v
  CPython Compiler
  (internal — you don't run this manually)
          |
          v
  Bytecode (.pyc file in __pycache__/)
          |
          v
  Python Virtual Machine (PVM)
          |
          v
  Running Program (output, side effects)
```

Key exam point: The **compilation to bytecode is internal and automatic**. You run `python3 script.py` — Python handles everything else.

---

## 3. REPL vs. Script Mode — Side-by-Side Comparison

| Feature | REPL | Script Mode |
|---|---|---|
| How to start | `python3` in terminal | `python3 filename.py` |
| Prompt | `>>>` | None — output only |
| Expression output | Automatic | Requires `print()` |
| Use case | Testing, exploring, debugging | Real programs, automation |
| Multi-line blocks | Possible (continuation prompt `...`) | Natural |
| File needed | No | Yes — a `.py` file |

---

## 4. Certification Exam Tips

**Tip 1 — Know the execution model cold.**
The PCAP exam asks scenario questions about Python's execution pipeline. Be able to answer: What intermediate format does CPython produce? (Bytecode / `.pyc`). Where is it stored? (`__pycache__`). What executes the bytecode? (PVM). What does the developer have to do to trigger compilation? (Nothing — it's automatic).

**Tip 2 — REPL auto-prints; scripts do not.**
A classic PCAP distractor: a code snippet that works differently in the REPL vs. in a script. If you see `2 + 2` alone in a script and the question asks what appears on screen — the answer is **nothing**. You need `print(2 + 2)` in a script.

**Tip 3 — Indentation is syntax, not style.**
Questions will show code with inconsistent indentation and ask what error is raised. The answer is `IndentationError`. Know that this is a parse-time error — Python raises it before any code runs.

**Tip 4 — Python 3 only.**
The PCAP targets Python 3. Any syntax or behavior question assumes Python 3. Do not confuse Python 2 behaviors (e.g., `print` as a statement without parentheses) with Python 3.

**Tip 5 — `python3` vs. `python`.**
On many systems, `python` still points to Python 2. Always use `python3` explicitly. The PCAP exam assumes you know to verify your version with `python3 --version`.

**Tip 6 — Comments do not affect execution.**
A question might show code with `#` comments and ask what the program outputs. Ignore all comment text when tracing execution — Python ignores it too.

---

## 5. Beyond the Exam — Real-World Context

The PCAP tests fundamentals. But as a working professional, here is what this module's content means in the real world:

- **Why interpreted languages dominate web dev and data science:** Python's interpreted nature means rapid iteration — write code, run it, see results, modify. Compiled languages require a build step that slows the feedback loop. For data scientists exploring datasets or web developers testing endpoints, Python's speed of development beats compiled speed of execution for most workloads.

- **Why CPython compiles to bytecode internally:** The `.pyc` bytecode files mean Python only re-parses your source code when it changes. If you run the same script twice, the second run is slightly faster because Python reads the cached bytecode instead of re-parsing the `.py` file. This is a small optimization, but it matters in large projects with hundreds of modules.

- **Why indentation is a feature, not a quirk:** Code is read far more often than it is written. Python's forced indentation means every block of code has visible, consistent structure — you can understand any Python program's flow at a glance without hunting for matching curly braces. This makes code review, debugging, and collaboration easier.

---

## 6. Required Readings & Videos

Complete these **before** starting the lab:

**Required Reading — Chapter 1:**
Read Chapter 1 "Why Program?" in [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book).
This chapter introduces the concept of programming, why Python was chosen as a learning language, and the basic idea of the interpreter. It's a short, readable chapter — do not skip it.

**Required Reading — Python Tutorial Section 2:**
Read [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html) in the Official Python 3 Documentation.
This is the authoritative source on the REPL, script mode, the `-c` flag for one-liners, and how the interpreter reads files. Brief and exact — this is what the PCAP examiners refer to.

**Required Video — Python for Everybody Playlist, Episodes 1–2:**
Watch the first two videos in the [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) by Dr. Charles Severance.
Dr. Severance covers installing Python, using the REPL, and running your first script — live demonstrations that reinforce what you read.

**Additional Resource — PEP 8:**
Skim [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/) at peps.python.org, specifically the Indentation section.
You don't need to memorize PEP 8 for Module 01, but understanding that 4-space indentation is the official standard — not just a suggestion — is important.

---

## 7. Lab & Command Preview

The following commands appear in this module's lab. Review them before you start:

| Command | What It Does |
|---|---|
| `python3 --version` | Displays the installed Python 3 version number |
| `python3` | Launches the interactive REPL |
| `exit()` | Exits the REPL |
| `python3 filename.py` | Runs a Python script file |
| `sudo apt update` | Updates Ubuntu package lists |
| `sudo apt install python3-pip -y` | Installs pip, Python's package manager |
| `mkdir ~/cis1310` | Creates your course working directory |
| `cd ~/cis1310` | Changes into your course working directory |
| `python3 -c "print('hello')"` | Runs a one-line Python program from the terminal |

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 01 topics. Use them to reinforce concepts, explore alternate explanations, or prepare for the PCAP exam.

**1. Official Python 3 Documentation — The Python Tutorial**
[https://docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html)
The authoritative source for all Python behavior. Chapter 2 ("Using the Python Interpreter") and Chapter 3 ("An Informal Introduction to Python") directly cover REPL usage, script mode, and basic expressions. Bookmark this site — you will return to it throughout the course.

**2. Python for Everybody (PY4E) — Full Free Textbook**
[https://www.py4e.com/book](https://www.py4e.com/book)
Dr. Charles Severance's open textbook used by millions of learners worldwide. Chapters 1–2 align directly with Module 01. The site also offers free video lectures, auto-graded exercises, and a browser-based Python interpreter for practice without installing anything.

**3. Real Python — Python Basics: A Practical Introduction**
[https://realpython.com/python-basics/](https://realpython.com/python-basics/)
Real Python's free introductory articles cover the Python interpreter, REPL, and first scripts with clear diagrams and annotated code. Particularly useful: "How to Run Your Python Scripts" and "Interacting With Python."

**4. PEP 8 — Style Guide for Python Code (Official)**
[https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)
The official style guide maintained by the Python Software Foundation. Read the Indentation, Whitespace, and Comments sections. Understanding PEP 8 from day one builds professional habits that will serve you throughout your career.

**5. CS50P — Introduction to Programming with Python (Harvard, Free)**
[https://cs50.harvard.edu/python/](https://cs50.harvard.edu/python/)
Harvard's free Python course available on edX and YouTube. Lecture 0 ("Functions, Variables") covers setting up Python and running first scripts — an excellent companion video with live coding demonstrations.

---

## 8. Study Checklist

Work through this list in order. Check each item off before moving to the next.

- [ ] Watch the Module 01 video lecture by Professor Nash.
- [ ] Read the High-Yield Glossary above — define each term in your own words.
- [ ] Read Chapter 1 of *Python for Everybody* at py4e.com.
- [ ] Read the "Using the Python Interpreter" section of the Official Python 3 Tutorial at docs.python.org.
- [ ] Watch Episodes 1–2 of the Python for Everybody video playlist.
- [ ] Study the Execution Pipeline diagram in Section 2 until you can reproduce it from memory.
- [ ] Study the REPL vs. Script Mode comparison table in Section 3.
- [ ] Review the Certification Exam Tips in Section 4.
- [ ] Preview the lab commands in Section 7.
- [ ] Proceed to the Module 01 Lab Activity.
