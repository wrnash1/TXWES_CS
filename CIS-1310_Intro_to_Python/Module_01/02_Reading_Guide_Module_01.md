# Reading Guide: Module 01 - Python Basics & Local Environment
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 01 - Python Basics & Local Environment**! This week's study material focuses on the core foundations and configuration mechanics of **Python Basics & Local Environment** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Interpreted vs Compiled execution**: Python is an interpreted language, meaning the Python interpreter reads and executes source code line by line at runtime without a separate compilation step. This differs from compiled languages (like C) where source code is translated entirely into machine code before execution; the trade-off is flexibility and portability at the cost of some raw speed.
*   **interactive shell (REPL)**: The Python REPL (Read-Eval-Print Loop) is an interactive environment where you type a single expression or statement, the interpreter immediately evaluates it, prints the result, and waits for the next input. It is invaluable for quickly testing snippets of code, exploring built-in functions, and debugging without writing a full script file.
*   **script mode**: Script mode refers to running a `.py` file directly through the Python interpreter (e.g., `python3 myscript.py`), executing all statements from top to bottom in sequence. Unlike the REPL, script mode does not automatically print expression results — you must use explicit `print()` calls to see output.
*   **indentation rules**: Python uses consistent indentation (typically 4 spaces per level) to define code blocks such as the body of loops, conditionals, and functions — there are no curly braces. Mixing tabs and spaces within the same file causes an `IndentationError`, and this is a frequent source of bugs for beginners transitioning from other languages.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam tests your understanding of Python's execution model — know the difference between interpreted and compiled languages and understand what happens when the interpreter reads a script. Also be comfortable navigating the REPL and understanding how `python3 --version` and `python3 -c "..."` work.
*   **Scenario Trap:** Watch out for questions that show code with inconsistent indentation. Python treats indentation as syntax; a block that appears visually similar but uses mixed tabs and spaces will raise an `IndentationError` at runtime — not a `SyntaxError` about the logic.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Python Basics & Local Environment](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — focus on the early episodes covering the Python environment, installing Python, and running your first script.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapters 1–2 covering **Python Basics & Local Environment** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; read the chapters on "Why Program?" and "Variables, Expressions, and Statements" to build your foundation.
*   **Required Video:** Watch the video lecture on **Python Basics & Local Environment** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance's video series mirrors the textbook chapters and includes live REPL demonstrations.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Check python version: `python3 --version`**: Run this command in your terminal to verify Python 3 is installed and note the version number; the PCAP exam targets Python 3.x features.
*   **Start interactive REPL: `python3`**: Launch the interactive shell and experiment with arithmetic expressions to confirm the interpreter is working correctly.
*   **Execute `print('Hello World')`**: Enter this statement in the REPL to confirm basic output; observe that the REPL displays the result without needing `print()` for expressions, but `print()` is required in script mode.
*   **Create `test.py` with print statement and run: `python3 test.py`**: Write a simple script file, save it, and execute it from the terminal to practice the script-mode workflow you will use throughout the course.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Python Basics & Local Environment** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Python Basics & Local Environment** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
