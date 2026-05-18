# Video Resources: Module 4 — Type Conversion and User Input

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Module Topic:** `int()`, `float()`, `str()`, `bool()`, `input()`, f-strings, `round()`, TypeError vs ValueError

> Choose the resources that best fit your learning style. All are free.

---

## Primary Video Resources

### 1. Python Type Conversion — Programming with Mosh
**Channel:** Programming with Mosh
**Search:** `"Python Type Conversion" Programming with Mosh`
**Direct Link:** [https://www.youtube.com/watch?v=kqtD5dpn9C8](https://www.youtube.com/watch?v=kqtD5dpn9C8) (jump to type conversion segment ~35:00)
**Covers for Module 4:** `int()`, `float()`, `str()`, implicit conversion, `input()` basics
**Why Watch:** Mosh demonstrates each conversion function live in code with visual output. His coverage of common mistakes (like forgetting to convert `input()`) directly addresses the Lab Part 2 concepts.

---

### 2. Python f-Strings — Corey Schafer
**Channel:** Corey Schafer
**Search:** `"Python f-strings tutorial" Corey Schafer`
**Direct Link:** [https://www.youtube.com/watch?v=nghuHvKLhJA](https://www.youtube.com/watch?v=nghuHvKLhJA)
**Covers for Module 4:** f-string syntax, format specifiers (`.2f`, `,`, `>`, `<`, `^`), expressions inside f-strings
**Why Watch:** One of the most thorough f-string tutorials available. Corey covers the format mini-language that controls decimal places, alignment, and thousands separators — all of which appear on the PCAP exam and in the Lab Part 3.

---

### 3. Python `input()` Function — Full Explanation
**Channel:** CS Dojo / Tech With Tim
**Search:** `"Python input function tutorial beginners"`
**Why Watch:** Explains why `input()` returns a string, how to convert it, and demonstrates the common `int(input(...))` pattern. Also shows what happens when the user enters invalid data — a preview of error handling you will learn in Module 14.

---

### 4. CS50P Lecture 0 — Variables and Type Conversion
**Channel:** Harvard CS50
**Search:** `"CS50P 2022 Lecture 0 Python variables input"`
**Direct Link:** [https://cs50.harvard.edu/python/](https://cs50.harvard.edu/python/)
**Covers for Module 4:** The first problem set in CS50P requires user input, type conversion, and string formatting — essentially this module's lab. David Malan's approach to debugging type errors is excellent.
**Why Watch:** Harvard-level explanation of why types matter and how to trace a `TypeError` through your code. Very relevant to Part 1 of the lab.

---

## Supplemental Resources

### 5. Python `round()` and Banker's Rounding
**Search:** `"Python round function banker's rounding explained"`
**Why Watch:** Demonstrates the counterintuitive results of banker's rounding (`round(2.5) == 2`) and explains why statistical applications and financial software prefer it. This is a guaranteed PCAP exam question.

### 6. Python String Formatting — `.format()` vs f-strings
**Search:** `"Python string formatting f-strings vs format method"`
**Why Watch:** Compares the three string formatting methods (concatenation, `.format()`, f-strings) with examples of when each is appropriate. Solidifies f-string knowledge from Part 3 of the lab.

### 7. Python TypeError vs ValueError — What's the Difference?
**Search:** `"Python TypeError ValueError difference explained"`
**Why Watch:** Clarifies the critical distinction: `TypeError` = wrong type, `ValueError` = right type but invalid value. This appears in Part 1 of the lab and on the PCAP exam.

---

## Official Documentation

### Python Built-in Functions Reference
**Link:** [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
**Functions to Read:** `int()`, `float()`, `str()`, `bool()`, `input()`, `round()`
**Why Read:** The official documentation describes exactly what each function accepts and what it raises — which is precisely what the PCAP exam tests. Focus on the "Raises" sections.

### Python f-Strings (PEP 498)
**Link:** [https://peps.python.org/pep-0498/](https://peps.python.org/pep-0498/)
**Why Read:** The original Python Enhancement Proposal for f-strings. The format mini-language reference explains every format specifier you can use.

### edube.org PE1 — Input/Output and Type Conversion
**Link:** [https://edube.org/](https://edube.org/)
**Section:** PE1 Module 2 — I/O operations and type casting
**Why Use:** Interactive exercises directly preparing you for the PCAP exam. The edube environment mirrors the exam's coding challenges.

---

## Video Watching Guide

| Video | Estimated Time | Best For |
|---|---|---|
| Programming with Mosh — type conversion | 20 min | Quick overview of all conversion functions |
| Corey Schafer — f-strings | 25 min | Lab Part 3, format specifiers |
| CS50P Lecture 0 continuation | 30–40 min | Deep understanding + debugging |
| Banker's rounding video | 10 min | PCAP `round()` question prep |
| edube.org exercises | 45–60 min | Exam practice |

**Total suggested time:** 2–3 hours

---

> **Unit Test 1 Reminder:** After completing this module, you will take Unit Test 1 covering Modules 1–4. The test includes 30 harder questions synthesizing concepts from all four modules. Review the quiz answer keys for Modules 1–4 before attempting the test. The `Unit_Test_1.md` file in this module's Assessments folder contains the test questions.
>
> **Note for Instructor:** When recording your own Module 4 lecture, recommended demonstration order: (1) implicit vs explicit conversion — show `"Score: " + 95` crashing, (2) `int()` truncation vs rounding demo, (3) `bool()` edge cases — especially `bool("False")`, (4) `input()` returning a string — show the bug, then the fix, (5) f-string format specifiers with a live grade report. Place your Canvas Media link here when ready.
