# Reading Guide: Module 11 – Software Design Patterns

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Introduction

Welcome to **Module 11 – Software Design Patterns**! Design patterns are reusable solutions to commonly occurring software design problems. First systematically catalogued in the "Gang of Four" book (Gamma, Helm, Johnson, Vlissides, 1994), they provide a shared vocabulary for software engineers to communicate architectural decisions efficiently.

This module covers the three classic pattern categories — Creational, Structural, and Behavioral — with emphasis on the patterns most frequently applied in modern Agile team codebases. Understanding design patterns supports Scrum's focus on technical excellence as a prerequisite for sustainable delivery.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Design pattern:** A general, reusable solution to a recurring problem in a given software design context. Patterns are not finished designs that can be directly transformed into code — they are descriptions or templates for how to solve a problem that can be used in many different situations.

* **Creational patterns:** Design patterns that deal with object creation mechanisms, aiming to create objects in a manner suitable to the situation. They abstract the instantiation process, making systems independent of how objects are created. Key examples: Singleton, Factory Method, Abstract Factory, Builder, Prototype.

* **Structural patterns:** Patterns that describe how to compose classes and objects to form larger, more flexible structures. They identify simple ways to realize relationships between entities. Key examples: Adapter, Bridge, Composite, Decorator, Facade, Proxy.

* **Behavioral patterns:** Patterns that characterize the ways in which classes and objects interact and distribute responsibility. They define the communication patterns between objects. Key examples: Observer, Strategy, Command, Iterator, Template Method, Chain of Responsibility.

* **Singleton pattern:** A creational design pattern that restricts instantiation of a class to a single object and provides a global access point to that instance. Used for shared resources like configuration managers, logging services, and database connection pools. Care must be taken in multi-threaded environments to implement thread-safe Singletons.

---

### 2. Certification Exam Tips

* **PSM I Focus — Design patterns support technical excellence:** While the PSM I does not test specific pattern implementations, it does test understanding of Scrum's expectation for technical practices. Scrum's value of "technical excellence and good design" (from Agile Principle 9) underpins why developers should use patterns to keep code maintainable and adaptable.
* **Pattern vocabulary matters:** Exam questions in software engineering contexts use pattern names as shorthand. Knowing that "Observer" means a publish-subscribe notification mechanism, and "Strategy" means a swappable algorithm family, allows you to quickly parse scenario-based questions.
* **Patterns and the Sprint:** Refactoring code to introduce a design pattern is valid Sprint work if it is part of meeting the Definition of Done or resolves technical debt that blocks future feature delivery. The Product Owner should understand the value — patterns enable future Sprints to proceed faster.
* **Anti-patterns to know:** The most common anti-pattern in Scrum contexts is "God Object" (a class that knows too much and does too much), which violates Single Responsibility and creates high coupling — making Sprint work slow and risky over time.
* **Study Resource:** [Refactoring.Guru — Design Patterns](https://refactoring.guru/design-patterns) provides free, detailed explanations of all 23 Gang of Four patterns with code examples in multiple languages. This is the recommended reference for this module.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** [Design Patterns — Refactoring.Guru](https://refactoring.guru/design-patterns) — free web reference covering all three pattern categories. Focus on reading the Singleton, Factory Method, Observer, and Strategy pattern pages this week, as these are most commonly applied in Agile team contexts.
* **Required Video:** [Design Patterns in Plain English – Programming with Mosh](https://www.youtube.com/watch?v=NU_1StN5Tkk) — visual explanation of key Creational, Structural, and Behavioral patterns with code walkthroughs. (~8 min excerpt; full video is ~2 hrs — watch first 30 min for this module)

---

### Lab & Command Integration

In this week's hands-on lab, you will:

* **Identify patterns in provided code:** Review three provided Python code samples and identify which design pattern (if any) each implements, citing the structural or behavioral characteristic that identifies it.
* **Implement a Singleton:** Write a thread-safe Singleton class in Python that provides a single shared configuration object, demonstrating that repeated instantiation returns the same object.
* **Implement an Observer:** Write a simple event notification system using the Observer pattern where a subject class notifies multiple listener objects when its state changes.

---

### 3. Study Checklist

* [ ] Read the Refactoring.Guru pages for Singleton, Factory Method, Observer, and Strategy patterns.
* [ ] Be able to name at least two patterns from each of the three categories (Creational, Structural, Behavioral).
* [ ] Understand why patterns like Observer and Strategy reduce coupling and improve Sprint velocity over time.
* [ ] Watch the first 30 minutes of the required video and confirm your mental model of each pattern demonstrated.
* [ ] Proceed to the weekly hands-on lab activity.
