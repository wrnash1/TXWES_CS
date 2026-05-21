# Reading Guide: Module 03 - Variables and Basic I/O
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 03 - Variables and Basic I/O**! This week's study material focuses on the core foundations and configuration mechanics of **Variables and Basic I/O** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Variable naming rules**: In Python, variable names must start with a letter or underscore, can contain letters, digits, and underscores, and are case-sensitive (`age` and `Age` are different variables). Reserved keywords like `if`, `for`, `return`, and `class` cannot be used as variable names. The PCAP exam tests whether you can identify valid vs. invalid identifiers.
*   **dynamic typing**: Python is dynamically typed, meaning a variable's type is determined at runtime by the value assigned to it, not by a declared type. The same variable can hold an `int` and later be reassigned a `str` — Python will not raise an error until an incompatible operation is attempted. This is distinct from statically typed languages like Java where types are declared at compile time.
*   **input() function**: The built-in `input()` function pauses program execution, displays an optional prompt string to the user, reads one line of text from standard input, and always returns that text as a `str`. If you need to perform arithmetic with the result, you must explicitly convert it with `int()` or `float()`.
*   **type casting (int, float, str)**: Type casting is the explicit conversion of a value from one type to another using constructor functions: `int()` converts a string of digits or a float to an integer (truncating the decimal part), `float()` converts an integer or numeric string to a float, and `str()` converts any value to its string representation. Passing a non-numeric string to `int()` raises a `ValueError`, which is a common PCAP exam scenario.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam frequently presents code that reads input, performs arithmetic, and prints output — you must know that `input()` always returns a string. A classic trap is code like `result = input("Enter a number: ") + 5`, which raises a `TypeError` because you cannot add `str` and `int` without casting.
*   **Scenario Trap:** Watch out for `int()` vs. `float()` conversion traps. `int("3.14")` raises a `ValueError` because `int()` does not accept a string with a decimal point; you would need `int(float("3.14"))` to convert it safely. Know the order of these conversions.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Variables and Basic I/O](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — pay special attention to the segments on `input()` and type conversion, which Dr. Severance demonstrates with live interactive examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapters 2–3 covering **Variables and Basic I/O** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on naming rules, variable assignment, and the sections explaining how `input()` works with type conversion.
*   **Required Video:** Watch the video lecture on **Variables and Basic I/O** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance demonstrates building interactive programs that prompt users and process their input.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a script to prompt the user for their name and age**: Use `input()` with descriptive prompt strings; observe that both values are returned as strings before any conversion.
*   **Convert age from string to integer using `int()`**: Apply `age = int(input("Enter your age: "))` and verify you can now perform arithmetic with `age`; test what happens if you type a non-numeric value.
*   **Output a formatted string: f'Hello {name}, you are {age} years old'**: Practice f-string syntax, which embeds variable values directly inside curly braces within a string literal — this is tested on the PCAP exam.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Variables and Basic I/O** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Variables and Basic I/O** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
