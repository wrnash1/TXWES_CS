# Reading Guide: Module 14 - Object-Oriented Programming (OOP) Basics
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 14 - Object-Oriented Programming (OOP) Basics**! This week's study material focuses on the core foundations and configuration mechanics of **Object-Oriented Programming (OOP) Basics** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Classes and objects**: A class is a blueprint that defines the structure and behavior shared by all objects of that type; an object (also called an instance) is a concrete realization of the class created with the class call syntax, e.g., `s = Student()`. Each object has its own independent namespace for instance variables, so changing `s1.name` does not affect `s2.name`. The PCAP exam tests that you understand the difference between the class definition (the blueprint) and instantiation (creating an object from it).
*   **constructors (__init__)**: The `__init__` method is called automatically when a new object is created; it receives the new instance as its first argument (`self`) followed by any arguments passed to the class call. Use `__init__` to initialize instance variables: `self.name = name` binds the attribute to the specific object being constructed. If `__init__` is omitted, Python uses the inherited version from `object`, which does nothing — the PCAP exam may ask what happens when a class has no `__init__`.
*   **instance variables vs class variables**: An instance variable is defined by assigning to `self.attribute` inside a method — each object gets its own copy. A class variable is defined in the class body outside any method — it is shared by all instances until overridden on a specific object. The PCAP exam presents code where a class variable is mutated through an instance (`obj.class_var = new_value`) and asks whether the class-level variable changed — the answer is no; the assignment creates a new instance variable that shadows the class variable for that object only.
*   **methods**: A method is a function defined inside a class body; instance methods receive the object as the first parameter conventionally named `self`, which Python passes automatically when called on an instance (`obj.method()` is equivalent to `ClassName.method(obj)`). The PCAP exam tests that `self` is a convention, not a keyword, and that omitting it as the first parameter causes a `TypeError` when the method is called on an instance.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam tests the distinction between instance variables and class variables — know that modifying a mutable class variable (like a list) through one instance affects all instances, but reassigning the name on an instance creates a shadow variable and leaves the class variable unchanged. Also know that `__init__` is not called a "constructor" in all Python documentation but functions as one; it does not return a value (returning anything other than `None` raises `TypeError`).
*   **Scenario Trap:** Watch for code that defines a class variable as a mutable default (e.g., `class Foo: items = []`) and then calls `foo.items.append(x)` on an instance — this mutates the shared class-level list, so all instances see the change. This is the OOP equivalent of the mutable default argument trap from Module 08. Also watch for calls that forget `self` in the method signature — the error message (`takes 0 positional arguments but 1 was given`) is a classic PCAP distractor.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Object-Oriented Programming (OOP) Basics](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Dr. Severance introduces classes through practical examples; supplement with the official Python docs on [classes](https://docs.python.org/3/tutorial/classes.html) for the authoritative treatment of instance vs class variables and method binding tested on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 14 covering **Object-Oriented Programming (OOP) Basics** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections covering class definition syntax, `__init__`, the role of `self`, and the difference between instance and class variables with examples showing what changes when you modify one versus the other.
*   **Required Video:** Watch the video lecture on **Object-Oriented Programming (OOP) Basics** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — build the `Student` class from the lab yourself, adding attributes and methods step by step, and use `print(vars(obj))` to inspect an instance's namespace after each change.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Define a class `Student` with attributes name and grade**: Write `class Student:` with an `__init__(self, name, grade)` method that assigns `self.name = name` and `self.grade = grade`; confirm that the class definition does not print anything on its own.
*   **Create multiple instances of the class**: Instantiate at least two students, e.g., `s1 = Student("Alice", 92)` and `s2 = Student("Bob", 85)`; verify that `s1.name` and `s2.name` hold independent values by printing both.
*   **Implement a method to print student details**: Add a `display(self)` method that prints the student's name and grade; call `s1.display()` and `s2.display()` and confirm each prints its own data.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Object-Oriented Programming (OOP) Basics** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Object-Oriented Programming (OOP) Basics** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
