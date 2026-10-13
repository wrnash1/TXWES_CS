# Video Script: CIS-1310 — Introduction to Python
## Module 01 — Python Basics & Local Environment
**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
> - Record in segments matching the timestamps below.
> - Use a screen-share or split-screen for all [DEMO] and [SHOW SCREEN] sections.
> - Slides referenced below should match the section headings.
> - [PAUSE] markers = hold 2 seconds of silence before continuing.
> - [DEMO] markers = switch to live terminal or VS Code screen share.

---

## [00:00 – 00:50] Opening — Welcome & Course Overview

**[INSTRUCTOR ON CAMERA — Title card: "Module 01 | Python Basics & Local Environment | CIS-1310"]**

"Hey everyone — welcome to CIS-1310, Introduction to Python Programming. I'm Professor Nash, and I want to start by telling you something important up front: this is not just a class about writing Python scripts.

This course is built around getting you to a real, industry-recognized certification — the PCAP, which stands for Certified Associate in Python Programming, issued by the Python Institute. That certification exam is your final in Module 16. So everything we do — every module, every lab, every quiz — is building toward that goal.

In this first module, we're going to cover what Python actually is, how it works under the hood, how to set up your development environment using VirtualBox and Ubuntu Linux, and how to write and run your first Python programs.

This is your launchpad. Let's get into it."

---

## [00:50 – 02:30] What Is Python?

**[SHOW SLIDE: "What Is Python? — History & Why It Matters"]**

"Python is a high-level, general-purpose programming language created by a Dutch programmer named Guido van Rossum. He started working on it in the late 1980s, and Python 1.0 was officially released in 1991. And yes — the name comes from Monty Python's Flying Circus. Guido is a fan. The language has absolutely nothing to do with snakes.

What made Python different from day one was its core design philosophy. The guiding principle, written in a document called PEP 20 — also known as 'The Zen of Python' — is this: **readability counts**. Guido believed that code is read far more often than it is written, so Python was designed to look almost like plain English. Fewer symbols. Consistent structure. Clean formatting.

Fast forward to today — Python is consistently ranked as the **number one most popular programming language in the world** on every major industry survey: the TIOBE Index, the Stack Overflow Developer Survey, the GitHub Octoverse. You name it, Python is at or near the top.

It powers Netflix's recommendation engine, NASA's spacecraft data processing pipelines, Instagram's backend servers, and nearly every AI and machine learning project you'll hear about. When you learn Python, you're learning the language of the modern tech industry.

Now — before you write a single line of code, you need to understand **how Python actually runs**. This is directly tested on the PCAP exam."

---

## [02:30 – 05:30] Interpreted vs. Compiled Languages — The Full Picture

**[SHOW SLIDE: "Interpreted vs. Compiled Languages"]**

"Every programming language has to solve one fundamental problem: your computer doesn't understand Python. Your processor only understands machine code — binary instructions. So how do we get from a readable Python file to a running program? There are two main approaches: **compiled** and **interpreted**.

Let me give you an analogy that actually sticks.

Imagine you have a recipe written entirely in French, and you don't speak French.

A **compiled language** is like hiring a professional translator *before* you ever walk into the kitchen. You hand them the entire French recipe. They read the whole thing, translate it completely into English, print it out, and hand it back to you. That translation is done once — ahead of time. You can now cook from that English document anytime, anywhere, without the translator present. This is how languages like C, C++, and Go work. You run a **compiler** — a separate tool — that reads your entire source code and produces a machine-code executable. That executable runs directly on your hardware. Fast. Self-contained.

An **interpreted language** is like having a French-speaking chef standing next to you *in the kitchen*, translating in real time. You point to the first instruction — they read it — you execute that step — you point to the next line. It happens **line by line, as the program runs**. That is Python.

**[PAUSE]**

The Python **interpreter** reads your `.py` source file line by line and executes each statement immediately — no separate compile step from your perspective.

Now — here's where it gets more nuanced, and the PCAP exam will absolutely test this:

Python doesn't *only* interpret. When you run a Python script, a two-step process happens internally:

**Step 1 — Compilation to Bytecode:** Python first compiles your source code into an intermediate format called **bytecode** — a lower-level, platform-independent representation. These files have a `.pyc` extension and are stored automatically in a folder called `__pycache__` inside your project directory.

**Step 2 — Interpretation by the PVM:** The **Python Virtual Machine** — the PVM — then reads that bytecode and executes it instruction by instruction.

**[SHOW DIAGRAM on screen]**
```
Source Code (.py)  →  Python Compiler  →  Bytecode (.pyc)  →  PVM  →  Running Program
```

You never manually run the compiler. You never manage `.pyc` files. Python handles all of this transparently the moment you type `python3 yourfile.py`. But understanding this pipeline is a core PCAP exam topic.

**[PAUSE]**

Practical takeaways:
- Python code is **portable** — the same `.py` file runs on Windows, Mac, and Linux.
- Python is **flexible** — test one line at a time in the REPL without a build step.
- Python is **somewhat slower** than fully compiled languages for raw math — but libraries like NumPy use compiled C code under the hood, making numerical work fast.

Lock in the execution model: Source → Bytecode → PVM → Output."

---

## [05:30 – 07:00] Python Versions — Python 2 vs. Python 3

**[SHOW SLIDE: "Python 2 vs. Python 3 — Use Python 3. Always."]**

"Let's handle versions quickly because this trips people up.

Python 2 was released in 2000. Python 3 came in 2008. They are **not** backward compatible — some syntax is different between them.

Python 2 reached **official end of life on January 1, 2020**. It no longer receives security updates. It is dead. Do not use it.

**This course and the PCAP exam cover Python 3 exclusively.**

When you install Python, install **Python 3**. When you run commands, use `python3` — not `python` — because on some systems the bare `python` command still points to Python 2. Always verify:

```
python3 --version
```

Ubuntu 22.04 LTS — which we're using in all our labs — ships with Python 3.10 or higher pre-installed.

One more thing: the standard Python implementation is called **CPython**. It's the official interpreter, written in C, downloaded from python.org. There are other implementations — PyPy for speed, Jython for Java environments, MicroPython for tiny microcontrollers — but when anyone says 'Python,' they mean CPython. That's what the PCAP targets."

---

## [07:00 – 09:00] The Python REPL — Your Interactive Sandbox

**[SHOW SLIDE: "The Python REPL — Read, Eval, Print, Loop"]**

**[TRANSITION TO SCREEN SHARE — Terminal window, Ubuntu or macOS]**

"One of the best features Python gives you right out of the box is the **REPL**.

REPL stands for **Read-Eval-Print Loop**:
- **Read** — Python reads a statement you type
- **Eval** — Python evaluates it immediately
- **Print** — Python prints the result
- **Loop** — Python waits for your next input

Launch it by opening a terminal and typing:

```
python3
```

You'll see a version banner and then three angle brackets: `>>>` — that's your prompt.

**[DEMO — type the following in the terminal]**

```python
>>> 2 + 2
4
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 10 % 3
1
>>> 'Texas' + ' Wesleyan'
'Texas Wesleyan'
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type('hello')
<class 'str'>
>>> type(True)
<class 'bool'>
```

Python immediately evaluates every expression and shows the result. The REPL is perfect for:
- Testing a code snippet before putting it in a script
- Exploring what a built-in function does
- Debugging a single expression
- Learning Python interactively

**Critical exam point — REPL vs. Script behavior:**

In the REPL, expressions are **automatically printed**. Type `2 + 2` and you see `4` with no `print()` needed.

Put that same line in a `.py` file and run it — **nothing appears on screen**. Script files only show output when you explicitly call `print()`.

This REPL vs. script mode distinction is a high-frequency PCAP exam question.

To exit the REPL:
- Type `exit()` and press Enter
- Or press **Ctrl+D** on Mac/Linux
- Or press **Ctrl+Z** then Enter on Windows"

---

## [09:00 – 10:30] Script Mode — Writing Real Programs

**[SHOW SLIDE: "Script Mode — Writing .py Files"]**

**[CONTINUE SCREEN SHARE — VS Code or nano + terminal]**

"The REPL is your sandbox. Real programs live in **script files** — plain text files saved with a `.py` extension.

Workflow:

**1.** Open any text editor — VS Code, nano, Notepad — whatever you have.

**2.** Write your Python code.

**3.** Save with a `.py` extension: `hello.py`

**4.** Open a terminal in the same directory and run:
```
python3 hello.py
```

**[DEMO — create hello.py and run it]**

```python
# hello.py
# Comments start with the pound symbol — Python ignores them
# Use comments to explain what your code does

print('Hello, Texas Wesleyan!')
print('Welcome to CIS-1310 — Introduction to Python')

name = 'Professor Nash'
print('Instructor:', name)
```

Run it:
```
python3 hello.py
```

Output:
```
Hello, Texas Wesleyan!
Welcome to CIS-1310 — Introduction to Python
Instructor: Professor Nash
```

Two things to notice:

First — the `#` symbol starts a **comment**. Python ignores everything on a line after `#`. Comments are for human readers. Use them generously.

Second — `print()` is required in script mode. The REPL automatically shows expression results. Scripts do not. Always use `print()` when you need to display something."

---

## [10:30 – 12:30] Python's Indentation Rules — This Is Syntax, Not Style

**[SHOW SLIDE: "Indentation — Python's Block Structure"]**

"Now here's something that confuses almost every programmer coming from another language: Python uses **indentation** to define code blocks. This is **not** a style preference. It is literal syntax.

In JavaScript, C, or Java, code blocks are surrounded by curly braces:

```javascript
// JavaScript — curly braces define the block
if (5 > 3) {
    console.log('Five is greater');
}
```

In Python, **there are no curly braces**. The indentation level **IS** the block structure:

```python
# Python — indentation defines the block
if 5 > 3:
    print('Five is greater')     # 4 spaces — INSIDE the if block
    print('Still inside')        # 4 spaces — still INSIDE
print('This always runs')        # 0 spaces — OUTSIDE the if block
```

**[PAUSE]**

The standard Python convention — defined in PEP 8, the official Python style guide — is **4 spaces per indentation level**. You can technically use 2 spaces, but 4 is universal in professional Python code. Do **NOT** mix tabs and spaces. Python 3 will raise an error if you do.

**[DEMO — show IndentationError]**

```python
# This is broken code — DO NOT do this
if 5 > 3:
  print('two spaces')      # 2 spaces
    print('four spaces')   # 4 spaces — IndentationError!
```

When you run this:
```
IndentationError: unexpected indent
```

Python saw the first line of the block at 2 spaces, then the second line at 4 spaces — different levels — it can't figure out the block structure.

**Nested blocks** require additional levels:

```python
# Nested indentation — each level adds 4 spaces
for i in range(3):              # level 0 — no indent
    print('Outer loop:', i)     # level 1 — 4 spaces
    if i == 1:                  # level 1 — 4 spaces
        print('Found it!')      # level 2 — 8 spaces
```

**PCAP exam facts to memorize for this topic:**
- Python uses indentation to define blocks — there are NO curly braces
- Standard is 4 spaces per level (PEP 8)
- Mixing tabs and spaces causes `IndentationError`
- `IndentationError` is raised at parse time — before the program executes
- Nested blocks add 4 more spaces per nesting level"

---

## [12:30 – 14:30] VirtualBox Setup Overview & Lab Prep

**[SHOW SLIDE: "Your Lab Environment — VirtualBox + Ubuntu 22.04"]**

"For every hands-on lab in this course, you'll work inside a **virtual machine** running Ubuntu Linux inside VirtualBox. Let me explain the setup.

**VirtualBox** is free, open-source virtualization software from Oracle. It creates a completely isolated 'guest' computer running inside a window on your real 'host' computer. Anything you do inside the VM — install packages, break things, experiment — doesn't affect your real machine.

We're using **Ubuntu 22.04 LTS** — the standard, professional Linux distribution for Python development. LTS means Long-Term Support — it's stable and gets security patches for years. This is what you'd see on a development server at a real tech company.

Here's the Module 01 lab setup in overview:

**Step 1 — Download VirtualBox:** Go to virtualbox.org, download the free version for your host operating system (Windows, Mac, or Linux). Install it.

**Step 2 — Download Ubuntu 22.04 ISO:** Go to ubuntu.com/download/desktop, download Ubuntu 22.04 LTS. It's approximately 1.4 GB. This is a disk image of the Ubuntu installer.

**Step 3 — Create a new VM in VirtualBox:**
- Name: `Ubuntu-CIS1310`
- Type: Linux, Version: Ubuntu (64-bit)
- RAM: 2 GB minimum — 4 GB recommended if your computer has it
- Storage: 20 GB virtual hard disk

**Step 4 — Install Ubuntu:** Boot the VM from the ISO, follow the installer. Choose 'Normal installation.' When it asks about disk partitioning, choose 'Erase disk and install Ubuntu' — this only erases the **virtual disk**, not your real computer.

**Step 5 — Verify Python 3:**
```
python3 --version
```
Ubuntu 22.04 includes Python 3.10+ pre-installed.

**Step 6 — Install pip** (Python's package manager):
```
sudo apt update
sudo apt install python3-pip -y
```

**Step 7 — Create your course working folder:**
```
mkdir ~/cis1310
cd ~/cis1310
```

Every lab this semester lives in that folder.

The full step-by-step with expected output, screenshots, and troubleshooting is in your **Lab document**. Follow it exactly."

---

## [14:30 – 15:30] PCAP Exam Alignment & Closing

**[SHOW SLIDE: "Module 01 — PCAP Exam Alignment"]**

"Let me close by tying everything back to the PCAP.

The PCAP exam from the Python Institute tests Python 3 across five sections. Module 01 aligns with **Section 1: Computer Programming and Python Fundamentals** — specifically, understanding Python's execution model, the interpreter, the REPL vs. script mode, and basic syntax including indentation.

These are not easy warm-up questions on the exam. They ask specific scenario-based items:

*'What happens when Python encounters a file with mixed tabs and spaces?'*
Answer: `IndentationError`

*'Where does CPython store compiled bytecode files?'*
Answer: The `__pycache__` directory as `.pyc` files

*'What is the difference between expression output in REPL mode vs. script mode?'*
Answer: REPL auto-prints; script mode requires explicit `print()`

**For additional study beyond this video, I recommend:**
- **Python for Everybody** by Dr. Charles Severance — free at py4e.com. Start with Chapter 1 'Why Program?' Conversational, approachable, excellent companion.
- **The Official Python Tutorial** at docs.python.org → Tutorial → Using the Python Interpreter.

Complete your Module 01 lab, post to the discussion board by Wednesday, and respond to two classmates by Sunday.

In **Module 02**, we're diving into actual Python code — literals, data types, operators, and expressions. That's where programming really begins.

See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 01 — Python Basics & Local Environment]**

---

## Additional Resources Referenced in This Module
- **Python for Everybody (py4e.com):** https://www.py4e.com/book — Chapter 1: Why Program?
- **Official Python Tutorial:** https://docs.python.org/3/tutorial/interpreter.html
- **PEP 8 — Python Style Guide:** https://peps.python.org/pep-0008/
- **PEP 20 — The Zen of Python:** https://peps.python.org/pep-0020/
- **VirtualBox Download:** https://www.virtualbox.org/
- **Ubuntu 22.04 LTS Download:** https://ubuntu.com/download/desktop
- **Python Institute PCAP Exam:** https://pythoninstitute.org/pcap
