# Reading Guide: Module 08 - Functions and Parameter Passing
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 08 - Functions and Parameter Passing**! This week's study material focuses on the core foundations and configuration mechanics of **Functions and Parameter Passing** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Function definition (def)**: A function is defined using the `def` keyword followed by the function name, a parenthesized parameter list, and a colon; the indented body executes only when the function is called. Functions are first-class objects in Python — they can be assigned to variables, passed as arguments, and returned from other functions. The PCAP exam tests that you understand the difference between defining a function and calling it.
*   **positional vs keyword arguments**: Positional arguments are passed in the order defined in the function signature and matched by position. Keyword arguments are passed by name (e.g., `func(height=1.8, weight=75)`) and can appear in any order. When mixing both, positional arguments must always come before keyword arguments in the call, which is a PCAP exam rule.
*   **default parameters**: A default parameter is specified in the function definition with `=` (e.g., `def greet(name, greeting="Hello")`), and its value is used if the caller omits that argument. A critical PCAP trap: default values are evaluated once at function definition time, not at each call — using a mutable default like `def func(lst=[])` causes the same list to accumulate values across multiple calls.
*   **return statement**: The `return` statement immediately exits the function and sends a value back to the caller. A function with no `return` (or a bare `return`) implicitly returns `None`. When multiple values are returned separated by commas (`return x, y`), Python automatically packages them as a tuple, which the caller can unpack.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam frequently tests the mutable default argument trap — know that `def func(data=[])` shares the same list across all calls. Also be ready to identify what a function returns when there is no explicit `return`, and to trace calls that use a mix of positional and keyword arguments.
*   **Scenario Trap:** Watch out for functions that call themselves without a base case (accidental recursion), functions whose `return` statement is unreachable due to an earlier `return`, and functions that modify a list argument in place (since lists are passed by reference, the caller's list is affected). These are all classic PCAP exam scenarios.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Functions and Parameter Passing](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance covers function definition and calling conventions; the official Python docs on [defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) provide the authoritative reference for parameter types tested on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 4 covering **Functions and Parameter Passing** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections about defining functions, parameter types, return values, and how Python passes arguments.
*   **Required Video:** Watch the video lecture on **Functions and Parameter Passing** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — pay attention to the examples showing positional vs. keyword arguments and the demonstrations of how `return` transfers a value back to the calling code.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a function `calculate_bmi(weight, height)`**: Write a `def` block with `weight` and `height` as parameters and compute BMI as `weight / (height ** 2)`.
*   **Return calculated BMI value**: Add a `return` statement and assign the function call to a variable; verify that the variable holds the float result, not `None`.
*   **Call the function using both positional and keyword arguments**: Call it as `calculate_bmi(75, 1.8)` and as `calculate_bmi(height=1.8, weight=75)` — both should produce the same result, demonstrating that keyword arguments override positional ordering.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Functions and Parameter Passing** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Functions and Parameter Passing** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
