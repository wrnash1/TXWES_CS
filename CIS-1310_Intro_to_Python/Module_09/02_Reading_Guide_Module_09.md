# Reading Guide: Module 09 - Scopes, Namespaces, and Recursion
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 09 - Scopes, Namespaces, and Recursion**! This week's study material focuses on the core foundations and configuration mechanics of **Scopes, Namespaces, and Recursion** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Global vs local scope**: Python resolves names using the LEGB rule — Local, Enclosing, Global, Built-in — searching each layer in order until the name is found or a `NameError` is raised. A variable assigned inside a function is local by default and is invisible outside that function; a variable assigned at module level is global and visible everywhere in the module. The PCAP exam tests whether you can trace which binding is used when a local variable shadows a global one with the same name.
*   **global keyword**: The `global` statement inside a function tells Python that a specific name refers to the module-level binding rather than creating a new local variable. Without `global x`, assigning `x = value` inside a function creates a brand-new local `x` that disappears when the function returns, leaving the module-level `x` unchanged. Overusing `global` is considered bad practice because it creates hidden dependencies between functions and module state.
*   **recursive functions**: A recursive function is one that calls itself as part of its own body, breaking a problem into a smaller version of the same problem until it reaches a base case that returns a value directly without another recursive call. Every recursive solution must have at least one base case; a function with no base case will recurse infinitely until Python raises a `RecursionError`. Classic PCAP examples include computing factorials (`n * factorial(n-1)`) and Fibonacci numbers.
*   **call stack and recursion limits**: Each function call — including a recursive one — pushes a new frame onto the call stack; when the function returns, its frame is popped. Because memory is finite, Python enforces a default recursion limit of 1000 frames (`sys.getrecursionlimit()`), and exceeding it raises `RecursionError: maximum recursion depth exceeded`. The PCAP exam may ask you to identify code that will hit this limit or to recognize that `sys.setrecursionlimit()` can raise it, though deep recursion is usually better replaced with an iterative loop.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam heavily tests the LEGB scope resolution order — know that Python looks up Local before Enclosing before Global before Built-in. A common question shows a function that assigns a variable with the same name as a global; be ready to identify that the local assignment creates a new binding and leaves the global unchanged unless `global` is declared.
*   **Scenario Trap:** Watch out for recursive functions where the base case is missing or unreachable — Python will raise `RecursionError`, not loop forever. Also expect code traces that ask what a recursive function returns when `n=0` or `n=1`; trace the call stack step by step and watch for off-by-one errors in the base case condition.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Scopes, Namespaces, and Recursion](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance covers function scope and variable lifetime; supplement with the official Python docs on [the execution model and namespaces](https://docs.python.org/3/reference/executionmodel.html) for the authoritative LEGB description tested on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 4 covering **Scopes, Namespaces, and Recursion** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; pay close attention to the sections on how Python searches for variable names, how the `global` keyword changes that search, and how recursive functions build and unwind the call stack.
*   **Required Video:** Watch the video lecture on **Scopes, Namespaces, and Recursion** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — trace the recursive factorial and Fibonacci examples yourself in the REPL, printing each call's argument so you can visualize the call stack growing and shrinking.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a recursive function to calculate factorial of a number**: Define `factorial(n)` with a base case of `n <= 1` returning `1` and a recursive case returning `n * factorial(n - 1)`; call it for values 0 through 5 and verify the output matches the expected sequence 1, 1, 2, 6, 24, 120.
*   **Demonstrate local scope variable shadow**: Create a module-level variable `x = 10`, then define a function that assigns `x = 99` without the `global` keyword; print `x` inside and outside the function to confirm the local binding does not change the global.
*   **Modify a global variable from inside a function using `global`**: Repeat the exercise above but add `global x` inside the function; confirm that after the function call the module-level `x` is now `99`, demonstrating the effect of the `global` statement.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Scopes, Namespaces, and Recursion** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Scopes, Namespaces, and Recursion** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
