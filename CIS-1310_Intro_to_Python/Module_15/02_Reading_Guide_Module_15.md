# Reading Guide: Module 15 - Advanced OOP: Inheritance and Polymorphism
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 15 - Advanced OOP: Inheritance and Polymorphism**! This week's study material focuses on the core foundations and configuration mechanics of **Advanced OOP: Inheritance and Polymorphism** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Single and multiple inheritance**: Single inheritance means a child class inherits from exactly one parent class; the child gains all the parent's attributes and methods automatically. Multiple inheritance means a class can inherit from more than one parent, e.g., `class C(A, B):` — Python resolves name conflicts using the Method Resolution Order (MRO), which can be inspected with `ClassName.__mro__`. The PCAP exam tests that you can read a simple class hierarchy and identify which method is called when a child inherits from multiple parents that both define the same method name.
*   **method overriding**: Method overriding occurs when a subclass defines a method with the same name as a method in its parent class, replacing the parent's behavior for instances of the subclass. Python's dynamic dispatch always calls the most derived version of a method — when you call `obj.method()`, Python looks up the MRO and uses the first definition it finds. The PCAP exam may show a class hierarchy and ask which version of an overridden method executes for a given object.
*   **super() function**: `super()` returns a proxy object that delegates method calls to the next class in the MRO, most commonly used as `super().__init__(...)` in a subclass `__init__` to call the parent's initializer without naming the parent class explicitly. Using `super()` is preferred over `ParentClass.__init__(self, ...)` because it cooperates correctly with multiple inheritance and avoids hardcoding the parent name. The PCAP exam tests that `super()` does not necessarily call the immediate parent — it calls the next in the MRO.
*   **checking types**: `isinstance(obj, ClassName)` returns `True` if `obj` is an instance of `ClassName` or any subclass of it, making it the preferred way to check types in polymorphic code. `type(obj) is ClassName` returns `True` only for the exact class, not subclasses — the PCAP exam tests this distinction. `issubclass(Child, Parent)` checks the class hierarchy without needing an instance.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam tests method resolution order in inheritance hierarchies — given a class `C` that inherits from both `A` and `B`, and both define `speak()`, Python calls `A`'s version first (left-to-right MRO). Also know that `isinstance(obj, ParentClass)` returns `True` for instances of child classes, which is the intended behavior for polymorphic type checks — using `type(obj) ==` breaks polymorphism.
*   **Scenario Trap:** Watch for subclass `__init__` methods that forget to call `super().__init__()` — the parent's initialization code is skipped, leaving instance variables undefined and causing `AttributeError` when those attributes are later accessed. Also watch for `super()` being called with arguments `super(ClassName, self)` (the Python 2 style) versus the bare `super()` (Python 3 style); the PCAP exam uses Python 3 syntax.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Advanced OOP: Inheritance and Polymorphism](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — supplement with the official Python docs on [inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance) and the `super()` built-in for the authoritative MRO and cooperative multiple inheritance description tested on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 14 covering **Advanced OOP: Inheritance and Polymorphism** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections covering how subclasses extend and override parent behavior, how `super()` chains initialization, and how `isinstance()` enables writing polymorphic functions that work correctly with any subclass.
*   **Required Video:** Watch the video lecture on **Advanced OOP: Inheritance and Polymorphism** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — build the `Vehicle`/`Car` hierarchy from the lab yourself, then extend it with a third subclass (e.g., `ElectricCar`) to practice overriding methods at multiple levels of the hierarchy.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a base class `Vehicle` and subclass `Car`**: Define `class Vehicle:` with an `__init__(self, make, model)` and a `start_engine(self)` method that prints a generic message; then define `class Car(Vehicle):` to verify `Car` inherits `start_engine` without redefining it.
*   **Override a method `start_engine` in `Car`**: Add `start_engine(self)` to `Car` with a more specific message; create both a `Vehicle` instance and a `Car` instance and call `start_engine()` on each to confirm each uses its own version.
*   **Use `super().__init__()` to inherit initialization attributes**: Inside `Car.__init__(self, make, model, num_doors)`, call `super().__init__(make, model)` to initialize the inherited attributes, then add `self.num_doors = num_doors`; confirm that a `Car` instance has all three attributes.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Advanced OOP: Inheritance and Polymorphism** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Advanced OOP: Inheritance and Polymorphism** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
