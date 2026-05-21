# Reading Guide: Module 04 - Control Flow - Conditional Statements
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 04 - Control Flow - Conditional Statements**! This week's study material focuses on the core foundations and configuration mechanics of **Control Flow - Conditional Statements** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Boolean algebra**: Boolean algebra is the branch of mathematics dealing with values that are either `True` or `False`, combined using logical operators `and`, `or`, and `not`. In Python, `and` returns the first falsy operand or the last operand if all are truthy; `or` returns the first truthy operand or the last if all are falsy — these "short-circuit" evaluation rules are specifically tested on the PCAP exam.
*   **relational operators**: Relational operators compare two values and return a boolean result: `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`. Python also allows chained comparisons like `0 < x < 10`, which is equivalent to `0 < x and x < 10` and is a syntactic feature unique to Python that the PCAP exam tests.
*   **if-elif-else syntax**: Python's conditional branching structure uses `if` to test a primary condition, one or more `elif` ("else if") clauses to test additional conditions in order, and an optional `else` clause that runs only when all preceding conditions are `False`. Only one branch executes — the first one whose condition evaluates to truthy — and the rest are skipped entirely.
*   **nested conditionals**: Nested conditionals are `if` statements placed inside the body of another `if`, `elif`, or `else` block. While they allow fine-grained branching logic, deep nesting quickly makes code hard to read; the PCAP exam may show nested structures and ask you to trace which branch executes for a given set of input values.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam frequently presents code traces where you must determine which `elif` or `else` branch executes. Remember that Python evaluates conditions top-to-bottom and stops at the first truthy match — if a number is 85 and your first condition is `grade >= 70`, that branch fires even if a later `elif grade >= 80` would also be true.
*   **Scenario Trap:** Watch out for the difference between `=` (assignment) and `==` (equality comparison) inside conditionals. Using `=` where `==` is intended is a `SyntaxError` in Python, unlike in some other languages. Also be aware that `None`, `0`, `""`, `[]`, and `{}` are all falsy — conditions like `if x:` will not execute if `x` holds any of these values.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Control Flow - Conditional Statements](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — focus on the episodes covering conditional execution and the "Guardian Pattern" that Dr. Severance explains for safe boolean evaluation.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 3 covering **Control Flow - Conditional Statements** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections about boolean expressions, logical operators, and conditional execution with `if`, `elif`, and `else`.
*   **Required Video:** Watch the video lecture on **Control Flow - Conditional Statements** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance walks through real grading-logic examples that mirror the kind of scenarios you will see on the PCAP exam.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a program that takes a score (0-100) and prints the letter grade**: Use `input()` and `int()` to read the score, then construct `if-elif-else` branches for A (90+), B (80+), C (70+), D (60+), and F (below 60).
*   **Use if-elif-else statements to check grade boundaries**: Deliberately order the conditions correctly — if you check `>= 60` before `>= 70`, the D branch will incorrectly catch B and C scores; trace through each case to verify.
*   **Handle invalid inputs (greater than 100 or less than 0)**: Add an outer `if` to check the valid range first, demonstrating the "Guardian Pattern" where you reject bad input before processing good input.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Control Flow - Conditional Statements** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Control Flow - Conditional Statements** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
