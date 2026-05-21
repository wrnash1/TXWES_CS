# Reading Guide: Module 10 - Tuples and Dictionaries
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 10 - Tuples and Dictionaries**! This week's study material focuses on the core foundations and configuration mechanics of **Tuples and Dictionaries** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Tuple immutability**: A tuple is an ordered, immutable sequence created with parentheses (e.g., `(1, 2, 3)`) or by separating values with commas; once created, its elements cannot be reassigned, appended, or removed. Because tuples are immutable, they are hashable and can be used as dictionary keys or set members, unlike lists. A frequent PCAP trap is a single-element tuple — `(5,)` is a tuple but `(5)` is just an integer in parentheses; the trailing comma is required.
*   **key-value pairs in dictionaries**: A dictionary (`dict`) stores data as unordered key-value pairs enclosed in curly braces, e.g., `{"name": "Alice", "score": 95}`; keys must be unique and of a hashable type (strings, numbers, tuples), while values can be any object. Accessing a key that does not exist raises a `KeyError`; use `dict.get(key, default)` to return a fallback value safely instead. The PCAP exam tests whether you can read and write dictionary literals correctly and distinguish `keys()`, `values()`, and `items()` views.
*   **dictionary methods**: The primary dictionary methods tested on the PCAP exam are `.keys()` (returns all keys), `.values()` (returns all values), `.items()` (returns key-value pairs as tuples), `.get(key, default)` (safe lookup), `.update(other)` (merges another dict), and `.pop(key)` (removes and returns a value). All three view objects — `keys()`, `values()`, `items()` — are dynamic: they reflect changes made to the dictionary after they were created.
*   **iterating over dicts**: Iterating over a dictionary with a plain `for k in d:` loop yields only the keys. To iterate over values use `for v in d.values():`, and to iterate over key-value pairs together use `for k, v in d.items():` — the PCAP exam frequently asks which loop variable pattern is needed for each type of iteration.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam heavily tests dictionary access patterns — know that `d[key]` raises `KeyError` for a missing key while `d.get(key)` returns `None` and `d.get(key, default)` returns the specified default. Also expect questions on tuple packing and unpacking: `a, b = (1, 2)` assigns 1 to `a` and 2 to `b`, and function return values that look like multiple values are actually tuples.
*   **Scenario Trap:** Watch out for code that assigns a single-element tuple without the trailing comma — `t = (42)` makes `t` an integer, not a tuple. Also watch for code that tries to modify a tuple element (e.g., `t[0] = 99`), which raises `TypeError: 'tuple' object does not support item assignment` — a classic PCAP exception question.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Tuples and Dictionaries](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance covers dictionary iteration patterns extensively; supplement with the official Python docs on [data structures — dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) for the complete method reference used on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapters 9 and 10 covering **Tuples and Dictionaries** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections covering dictionary creation and lookup, how to iterate over keys versus key-value pairs, and the distinction between mutable lists and immutable tuples.
*   **Required Video:** Watch the video lecture on **Tuples and Dictionaries** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — work through the dictionary-counting examples (word frequency counters) in the REPL; these patterns are the most common dictionary application on the PCAP exam.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a dictionary storing student names and grades**: Build `grades = {"Alice": 92, "Bob": 85, "Carol": 78}` and use bracket notation to retrieve individual grades; then add a new student with `grades["Dave"] = 90` and confirm the dictionary length.
*   **Retrieve grades using student names**: Use `grades.get("Eve", "Not found")` to safely look up a student who does not exist; verify the result is the default string rather than a `KeyError`.
*   **Iterate through keys and values using `.items()`**: Write a `for name, score in grades.items():` loop that prints each student's name and grade; then rewrite using only `.keys()` to show the difference.
*   **Verify tuples cannot be modified**: Create `point = (3, 7)`, then attempt `point[0] = 10` inside a try-except block; confirm a `TypeError` is raised and explain why.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Tuples and Dictionaries** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Tuples and Dictionaries** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
