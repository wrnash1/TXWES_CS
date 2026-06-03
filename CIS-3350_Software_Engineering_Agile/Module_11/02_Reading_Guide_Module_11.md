# Reading Guide: Module 11 – Software Design Patterns

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Software design patterns are reusable solutions to commonly recurring problems in software design. They were systematically catalogued by Gamma, Helm, Johnson, and Vlissides — the "Gang of Four" — in their 1994 book. Patterns provide a shared vocabulary that lets developers communicate architectural decisions efficiently. In Agile contexts, patterns are critical because they directly support Principle 9 of the Agile Manifesto: continuous attention to technical excellence and good design enhances agility. Teams that use patterns build systems that can absorb Sprint-over-Sprint change without accumulating paralyzing technical debt.

---

## 1. The Three Pattern Categories

The Gang of Four organized their 23 patterns into three categories:

| Category | Concern | Examples |
|---|---|---|
| Creational | How objects are created and instantiated | Singleton, Factory Method, Abstract Factory, Builder, Prototype |
| Structural | How classes and objects are composed into larger structures | Adapter, Decorator, Facade, Proxy, Bridge, Composite |
| Behavioral | How objects communicate and distribute responsibility | Observer, Strategy, Command, Iterator, Template Method |

---

## 2. Creational Patterns

### Singleton

Problem it solves: A class must have exactly one instance shared across the entire application.

How it works: The class stores its single instance as a private static variable. The constructor is private. A static method (often called `getInstance()`) checks whether the instance exists — creates it if not, returns it if it does.

Classic use cases: Configuration manager, logging service, database connection pool, thread pool.

Key concern: Thread safety. In multi-threaded environments, two threads may simultaneously enter `getInstance()`, both find the instance null, and both create instances — resulting in two Singletons. Thread-safe implementations use locking (double-checked locking pattern) or language-level mechanisms to prevent this race condition.

### Factory Method

Problem it solves: Code should be able to create objects without knowing the exact class to instantiate. New object types should be addable without modifying existing code.

How it works: An abstract Creator class declares a factory method that returns a Product object. Concrete subclasses override the factory method to return specific concrete product types. Client code calls the factory method and works with the Product interface — it never directly uses `new ConcreteProduct()`.

Classic use cases: Document editors supporting multiple formats, UI framework components that differ by platform, payment processors supporting multiple payment methods.

Connection to Open/Closed Principle: New product types extend the factory without modifying existing client code — the system is open for extension, closed for modification.

---

## 3. Structural Patterns

### Adapter

Problem it solves: Two classes need to work together but have incompatible interfaces.

How it works: An Adapter class wraps the Adaptee (the class with the incompatible interface) and exposes the Target interface that the client expects. The client calls the target interface; the adapter translates those calls to the adaptee's interface.

Classic use cases: Integrating a third-party library whose API does not match your code's expectations, making old legacy code work with a new system, plugging two independently developed components together.

### Decorator

Problem it solves: Additional behaviors need to be added to an object at runtime without modifying its class or using subclassing.

How it works: A Decorator class wraps a Component object and adds behavior before or after delegating to the component. Multiple decorators can be stacked — each adding a layer of behavior.

Classic use cases: Text formatting (bold + italic + border applied to the same text object), I/O streams (buffering + compression + encryption applied to a file stream), UI component enhancements.

### Facade

Problem it solves: A complex subsystem needs to be made accessible through a simple interface.

How it works: A Facade class provides a single simplified interface to a set of interfaces in a subsystem. The facade does not add new functionality — it reduces complexity for the caller.

Classic use cases: Startup sequences (one `startSystem()` call internally handles database connection, cache warming, service registration), API gateways, library wrappers.

---

## 4. Behavioral Patterns

### Observer

Problem it solves: When one object changes state, other objects that depend on it need to be notified and updated automatically, without tight coupling between the subject and its dependents.

How it works: The Subject maintains a list of Observer objects. When the Subject's state changes, it calls `notifyObservers()`, which iterates through the list and calls `update()` on each observer. Observers can be added or removed at runtime.

Classic use cases: UI frameworks (model changes trigger view updates), event systems, message queues, real-time dashboards.

Agile connection: Observer decouples components — the subject does not know anything about who is observing it. This loose coupling means new observers (new features) can be added in future Sprints without modifying the subject.

### Strategy

Problem it solves: A class needs to perform a function that can be implemented in multiple ways, and the implementation should be swappable at runtime without conditionals in the client code.

How it works: The Strategy interface defines the algorithm signature. Concrete Strategy classes each implement one version of the algorithm. The Context class holds a reference to a Strategy object and delegates algorithm execution to it. Strategies can be swapped at runtime.

Classic use cases: Sorting algorithms (bubble, merge, quick — all implement a Sorter interface), payment processing (credit card, PayPal, bank transfer — all implement a PaymentStrategy interface), compression algorithms.

Agile connection: Adding a new algorithm variant is a new Strategy class — the Context class and existing strategies are untouched. New Sprint feature = new class, not a modified class.

---

## 5. Anti-Patterns: The God Object

An anti-pattern is a commonly seen but counterproductive approach to a recurring problem — the opposite of a design pattern.

The God Object (also called God Class) is a class that centralizes too much responsibility. It handles data access, business logic, authentication, logging, and error handling in a single file. Teams fall into this incrementally: the first version is small, but every Sprint adds a little more to the existing class because it is faster than designing a new one.

Why the God Object destroys Sprint velocity:

- Any change to any part of the system requires modifying the God Object — high coupling
- Testing requires setting up the entire God Object even to test a small behavior — slow test cycles
- Multiple developers cannot work on the God Object simultaneously without merge conflicts
- Understanding the class requires understanding everything at once — new developers are slowed

Escape patterns: Use Factory Method to separate creation logic from business logic. Use Strategy to extract swappable algorithms. Use Facade to provide a clean interface while the internals are refactored. Use Single Responsibility as the design principle guiding the decomposition.

---

## 6. Patterns and the Sprint

| Design Concern | Pattern | Sprint Benefit |
|---|---|---|
| Shared resource management | Singleton | Prevents resource conflicts in multi-threaded features |
| Adding new object types | Factory Method | New Sprint features extend without modifying existing code |
| Third-party integration | Adapter | New integrations do not require refactoring existing code |
| Adding behaviors without subclassing | Decorator | Feature combinations grow without class explosion |
| Decoupling event notification | Observer | New subscribers (features) added without touching the subject |
| Swappable algorithms | Strategy | Behavior variants added as new classes, not branching conditionals |

Where pattern work belongs in a Sprint: Introducing or refactoring to a design pattern is legitimate Sprint work when it is directly needed to meet the Definition of Done, reduce technical debt that is actively blocking feature delivery, or enable the next Sprint's planned features.

---

## 7. PSM I Exam Tips

Tip 1: The PSM I does not test pattern syntax or code. It tests why technical excellence matters in Scrum. The connection is Agile Principle 9: continuous attention to technical excellence and good design enhances agility.

Tip 2: Technical debt is the accumulated cost of poor design choices. Scrum's Retrospective is the prescribed event for surfacing and planning technical debt reduction. The Definition of Done is the mechanism for preventing new technical debt.

Tip 3: The Scrum Master's role with design patterns is to make technical work visible to the Product Owner — connecting refactoring work to business value (faster future Sprints, fewer bugs, more reliable releases).

Tip 4: The God Object anti-pattern is the exam's most common example of poor design creating Scrum problems. When exam questions describe a codebase where every change affects everything else, the underlying problem is high coupling and low cohesion — the God Object in disguise.

Tip 5: Agile Principle 9 (technical excellence) and Principle 10 (simplicity — maximizing work not done) together describe the design philosophy behind patterns: solve the problem with the right structure, not the most complex one.

Tip 6: Observer is the most Agile-relevant behavioral pattern because it enables loose coupling between components — a new feature (observer) can be added without modifying existing code (the subject).

Tip 7: The Open/Closed Principle (open for extension, closed for modification) is embodied by Factory Method and Strategy — both allow new variants to be added as new classes without touching existing ones.

Tip 8: Design pattern work does not violate Scrum's principle of working software over comprehensive documentation. Patterns are implemented in code, not documented separately. The documentation is the code.

---

## 8. Study Checklist

- [ ] State the three Gang of Four pattern categories and give two pattern examples for each
- [ ] Explain the Singleton pattern and identify its thread-safety concern
- [ ] Explain the Factory Method pattern and connect it to the Open/Closed Principle
- [ ] Explain the Adapter and Decorator structural patterns with a use case for each
- [ ] Explain the Observer and Strategy behavioral patterns and describe why each reduces coupling
- [ ] Describe the God Object anti-pattern and explain why it slows Sprint velocity
- [ ] Connect Agile Manifesto Principle 9 to the business value of design patterns in Scrum
- [ ] Complete this module's Lab and Quiz

---
