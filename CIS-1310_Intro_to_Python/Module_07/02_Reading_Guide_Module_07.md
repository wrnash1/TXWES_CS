# Reading Guide: Module 07 - Advanced List Operations
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 07 - Advanced List Operations**! This week's study material focuses on the core foundations and configuration mechanics of **Advanced List Operations** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **List methods (append, insert, remove, pop)**: `append(x)` adds a single element `x` to the end of the list in O(1) time. `insert(i, x)` inserts `x` before index `i`, shifting all subsequent elements right. `remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if it is absent. `pop(i)` removes and returns the element at index `i` (default: last element); these four methods are frequently tested together on the PCAP exam.
*   **list sorting**: `list.sort()` sorts the list in place using Timsort and returns `None`; `sorted(iterable)` returns a new sorted list leaving the original unchanged. Both accept a `key` parameter for custom sort criteria and a `reverse=True` argument for descending order. A very common PCAP trap is assigning `my_list.sort()` to a variable and expecting a sorted list — the result is `None`.
*   **list copying vs referencing**: Assigning one list variable to another (`b = a`) creates a reference, not a copy — both names point to the same list object, so changes through `b` affect `a`. A shallow copy is made with `a.copy()`, `list(a)`, or `a[:]`, producing a new list object with independent references. The PCAP exam tests this distinction with code that modifies one list and asks what happens to another.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam tests list method return values: `append()`, `sort()`, `reverse()`, and `extend()` all return `None` because they mutate in place. This is the most common list-related trap — expect questions showing code like `result = my_list.append(5)` and asking the value of `result`.
*   **Scenario Trap:** Know the difference between `remove(x)` and `pop(i)`. `remove()` takes a value and finds the first match; `pop()` takes an index and returns the removed element. Calling `remove()` with a value not in the list raises `ValueError`; calling `pop()` with an out-of-range index raises `IndexError`. The PCAP exam may swap these in code traces.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Advanced List Operations](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — supplement with the official Python documentation at [docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html) which provides the complete list method reference used on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 8 covering **Advanced List Operations** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; pay close attention to the sections on list mutability, the difference between methods that return values versus those that modify in place, and list aliasing vs. copying.
*   **Required Video:** Watch the video lecture on **Advanced List Operations** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — work through the list manipulation examples yourself in the REPL to build muscle memory for the method names and their behaviors.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a script to manage a shopping list using append() and pop()**: Build a list by appending items one at a time, then use `pop()` to remove and display the last added item; confirm the list length decreases.
*   **Sort the list alphabetically**: Call `.sort()` on the list and print the result; then try `sorted_copy = sorted(my_list)` and verify the original is unchanged while `sorted_copy` holds the sorted version.
*   **Demonstrate the difference between list copy `list.copy()` and reference assignment**: Create `a = [1, 2, 3]`, then `b = a` and `c = a.copy()`; modify `b[0]` and observe that `a` changes while `c` remains unaffected.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Advanced List Operations** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Advanced List Operations** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
