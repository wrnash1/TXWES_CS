# Reading Guide: Module 12 - Exception Handling
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 12 - Exception Handling**! This week's study material focuses on the core foundations and configuration mechanics of **Exception Handling** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Try-except blocks**: A `try` block wraps code that might raise an exception; if an exception occurs, Python jumps immediately to the matching `except` clause instead of crashing the program. The `except` clause can name a specific exception type (e.g., `except ValueError:`) to catch only that error, or use a bare `except:` to catch everything — the PCAP exam strongly favors named exception types as best practice. Code in the `try` block after the line that raised the exception is skipped entirely once the exception is caught.
*   **handling multiple exception types**: A single `try` block can have multiple `except` clauses, each handling a different exception type; Python checks them in order from top to bottom and executes only the first matching clause. You can also catch several types in one clause using a tuple: `except (TypeError, ValueError):`. A common PCAP trap is placing a broad `except Exception:` before a specific handler — the broad clause will always match first, making the specific one unreachable.
*   **else and finally clauses**: The optional `else` clause runs only if the `try` block completed without raising any exception — it is the right place for code that should only execute on success. The `finally` clause always runs regardless of whether an exception was raised, caught, or not caught; it is guaranteed to execute even if the `try` block contains a `return` or `break` statement, making it ideal for cleanup such as closing files or releasing locks.
*   **raising exceptions**: The `raise` statement explicitly triggers an exception: `raise ValueError("age must be positive")` creates and raises a `ValueError` with a descriptive message. You can re-raise the current exception inside an `except` block with a bare `raise` (no argument), which preserves the original traceback. The PCAP exam tests that you can write both `raise ExceptionType(message)` to signal an error condition and use `raise` alone to propagate a caught exception up the call stack.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam tests the exact execution order of try-except-else-finally — know that `else` runs only when no exception occurred, while `finally` always runs. A classic question shows a function with a `return` inside `try` and asks whether `finally` still executes; the answer is yes, `finally` runs before the return value is handed back to the caller.
*   **Scenario Trap:** Watch for code that catches `Exception` (the base class for most built-in exceptions) placed before a specific handler like `except ValueError` — the `Exception` clause matches first and swallows the error before the specific handler can run. Also watch for `except` clauses that silence exceptions by doing nothing (bare `pass`), which hides bugs; the PCAP exam may ask whether a program will crash or silently succeed given such a handler.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Exception Handling](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance demonstrates try-except with file I/O and user input; supplement with the official Python docs on [errors and exceptions](https://docs.python.org/3/tutorial/errors.html) for the full exception hierarchy and `raise` syntax tested on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 7 covering **Exception Handling** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections covering try-except for user input validation, the difference between `else` and `finally`, and how `raise` is used to signal domain-specific errors.
*   **Required Video:** Watch the video lecture on **Exception Handling** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — practice writing try-except-else-finally blocks in the REPL and deliberately trigger each clause by causing and suppressing different exceptions.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a script that takes numbers from user and handles ValueError**: Use a `while True:` loop with `try-except ValueError` to keep prompting until the user enters a valid integer; print a friendly error message on bad input instead of crashing.
*   **Use try-except-finally to ensure database or file connection is closed**: Wrap a simulated file-open operation in `try-except` and add a `finally` block that prints "connection closed"; verify the `finally` block runs even when you force an exception inside `try`.
*   **Raise a custom ValueError if negative values are input**: After successfully parsing an integer, add `if value < 0: raise ValueError("value must be non-negative")` and confirm the `except` clause catches and displays the custom message.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Exception Handling** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Exception Handling** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
