# Reading Guide: Module 02 - Literals, Operators, and Expressions
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 02 - Literals, Operators, and Expressions**! This week's study material focuses on the core foundations and configuration mechanics of **Literals, Operators, and Expressions** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Data types (int, float, string, boolean)**: Python has four fundamental scalar data types: `int` (whole numbers with no fractional part, e.g., `42`), `float` (real numbers stored in IEEE 754 double precision, e.g., `3.14`), `str` (an immutable sequence of Unicode characters enclosed in single or double quotes), and `bool` (`True` or `False`, a subclass of `int`). The PCAP exam requires you to recognize which type is produced by a given literal or operation.
*   **float**: A numeric type representing real numbers with a decimal point, stored internally in binary floating-point format. Because of this binary representation, certain decimals like `0.1` cannot be represented exactly, which can produce small rounding errors (e.g., `0.1 + 0.2 != 0.3`); this is a classic PCAP exam trap.
*   **string**: An immutable sequence of Unicode characters delimited by single quotes, double quotes, or triple quotes. String literals support escape sequences (e.g., `\n` for newline, `\t` for tab) and can be concatenated with `+` or repeated with `*`. They are zero-indexed and support slicing just like lists.
*   **boolean**: A subtype of `int` in Python where `True` equals `1` and `False` equals `0`. Booleans are produced by comparison operators and logical expressions; because they inherit from `int`, expressions like `True + True` evaluate to `2`, which is frequently tested on the PCAP exam.
*   **arithmetic operators**: Python's arithmetic operators are `+` (addition), `-` (subtraction), `*` (multiplication), `/` (true division, always returns float), `//` (floor division, truncates toward negative infinity), `%` (modulo, remainder), and `**` (exponentiation). The PCAP exam frequently tests the distinction between `/` and `//` and the sign behavior of `%` with negative operands.
*   **precedence and associativity**: Operator precedence determines which operation is performed first when multiple operators appear in an expression; Python follows PEMDAS with `**` at the top, then unary `-`, then `*`, `/`, `//`, `%`, then `+` and `-`. Most binary operators are left-associative (evaluated left to right), but `**` is right-associative (`2 ** 3 ** 2` evaluates as `2 ** 9`, not `8 ** 2`).

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam heavily tests expression evaluation — be able to manually trace through expressions like `2 + 3 * 4 - 1` or `10 % 3 ** 2` step by step. Memorize that `**` has higher precedence than unary minus, so `-2 ** 2` evaluates to `-4`, not `4`.
*   **Scenario Trap:** Watch out for questions mixing integer and float arithmetic. Dividing two integers with `/` always returns a `float` in Python 3 (e.g., `4 / 2` is `2.0`, not `2`). Students who learned Python 2 may expect integer division — Python 3 changed this behavior deliberately.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Literals, Operators, and Expressions](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — focus on the episodes covering expressions and variables; work through all example evaluations by hand before checking results in the REPL.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 2 covering **Literals, Operators, and Expressions** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections about values, types, operators, and expressions, paying special attention to the operator precedence table.
*   **Required Video:** Watch the video lecture on **Literals, Operators, and Expressions** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance demonstrates how Python evaluates expressions step by step, making it easy to follow precedence rules.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a script to compute area of a circle**: Use `import math` and `math.pi` along with the formula `area = math.pi * radius ** 2`; observe that `**` evaluates before `*` due to precedence.
*   **Experiment with integer division `//` and modulo `%`**: Try positive and negative operands (e.g., `-7 // 2` and `-7 % 2`) to see how Python floors toward negative infinity, which differs from truncation in other languages.
*   **Examine operator precedence rules: print(2 + 3 * 4)**: Predict the output before running; then use parentheses to override precedence and observe how `print((2 + 3) * 4)` produces a different result.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Literals, Operators, and Expressions** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Literals, Operators, and Expressions** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
