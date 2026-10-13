# Video Script: Module 11 – Software Design Patterns

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Estimated Duration:** 20 minutes

**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Pattern diagrams should show class relationships with UML-style arrows; code examples in pseudocode

---

## Section 1 — Welcome and Why Patterns Matter for Agile Teams [00:00–03:00]

"Welcome to Module 11. We are shifting now from requirements and process into the technical practices that make Agile teams sustainable over time. Today's topic is software design patterns — a set of reusable solutions to recurring design problems that every serious software engineer should know.

You might wonder why design patterns appear in an Agile and Scrum course. The answer is Agile Manifesto Principle 9: 'Continuous attention to technical excellence and good design enhances agility.' Teams that build on solid design patterns can add new features in future Sprints without constantly reworking the foundation. Teams that ignore patterns accumulate technical debt that eventually slows every Sprint to a crawl.

By the end of this module you will be able to:

- Identify the three Gang of Four pattern categories and give examples of each
- Explain the Singleton, Factory Method, Observer, Strategy, Adapter, and Decorator patterns
- Connect specific patterns to common Agile team technical challenges
- Recognize the God Object anti-pattern and explain why it undermines Sprint velocity
- Describe where design pattern work fits within a Sprint"

---

## Section 2 — The Gang of Four and Three Pattern Categories [03:00–07:00]

"Design patterns were systematically catalogued in 1994 by four authors — Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides — in a book called Design Patterns: Elements of Reusable Object-Oriented Software. They are universally called the Gang of Four, and their 23 patterns remain the foundational vocabulary of object-oriented design.

[SHOW DIAGRAM: Three-category taxonomy — Creational (object creation), Structural (composition), Behavioral (communication and responsibility)]

The Gang of Four organized patterns into three categories based on what they solve.

Creational patterns deal with object creation. They abstract the instantiation process so the system is independent of how objects are created, composed, and represented. Examples include Singleton, Factory Method, Abstract Factory, Builder, and Prototype.

Structural patterns deal with how classes and objects are composed to form larger structures. They identify simple ways to realize relationships between entities. Examples include Adapter, Decorator, Facade, Proxy, Bridge, and Composite.

Behavioral patterns deal with how objects communicate and how responsibility is distributed. They define the protocols for interaction between objects. Examples include Observer, Strategy, Command, Iterator, Template Method, and Chain of Responsibility.

PSM I Exam Tip: The PSM I does not test specific pattern implementations in code. It tests whether you understand why technical excellence matters in Scrum — Agile Principle 9 is the connection. When exam questions describe technical debt slowing Sprint velocity, the underlying concept is that poor design choices compound over time."

---

## Section 3 — Creational Patterns: Singleton and Factory Method [07:00–11:00]

"Let me walk through two of the most commonly used creational patterns.

[SHOW DIAGRAM: Singleton pattern — class diagram showing single instance + static accessor method]

The Singleton pattern restricts a class to a single instance and provides a global access point to it. The canonical use case is a shared resource that should only exist once: a configuration manager, a logging service, a database connection pool. Every component that needs to log to the same file gets the same logger instance. You do not want 50 separate logger objects all writing to different places.

The key implementation concern with Singleton is thread safety. In a multi-threaded application, two threads could simultaneously check 'does an instance exist?' both get 'no,' and both create instances — resulting in two singletons. Thread-safe Singleton implementations use locking mechanisms to prevent this race condition.

[SHOW DIAGRAM: Factory Method pattern — abstract Creator class with abstract factoryMethod() → concrete creators override to return specific product types]

The Factory Method pattern defines an interface for creating an object but lets subclasses decide which class to instantiate. The client code calls a factory method rather than using 'new ConcreteClass()' directly. This means you can introduce new product types — new classes that implement the product interface — without changing any client code. The factory method is extended, not modified. This is the Open/Closed Principle in practice.

A common example: a document editor might have a factory method that creates 'Document' objects. A 'WordDocument' subclass creates Word documents; a 'PDFDocument' subclass creates PDFs. The editor code that calls 'createDocument()' does not need to change when you add a new document type.

PSM I Exam Tip: Factory Method is about extensibility — new types can be added without touching existing code, which means new Sprints can add features without destabilizing the system."

---

## Section 4 — Structural and Behavioral Patterns [11:00–16:00]

"Now let me cover two structural and two behavioral patterns.

[SHOW DIAGRAM: Adapter pattern — Target interface ← Adapter class (wraps Adaptee) — shows incompatible interfaces being bridged]

The Adapter pattern converts the interface of a class into another interface that clients expect. It allows classes to work together that could not otherwise because of incompatible interfaces. Think of a power adapter: your laptop has a three-prong plug but the hotel wall has a two-prong socket. The adapter bridges the gap. In software, this appears when integrating a third-party library whose API does not match what your code expects.

[SHOW DIAGRAM: Decorator pattern — Component interface ← ConcreteComponent; Decorator wraps Component and adds behavior]

The Decorator pattern attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality. A classic example is text formatting: a plain text object can be wrapped by a BoldDecorator, then by an ItalicsDecorator, then by a BorderDecorator — each adding behavior without modifying the original class.

Now for behavioral patterns.

[SHOW DIAGRAM: Observer pattern — Subject with list of observers; notifyObservers() calls update() on each; ConcreteObserver implements update()]

The Observer pattern defines a one-to-many dependency between objects. When one object (the subject) changes state, all its dependents (observers) are notified and updated automatically. This is publish-subscribe. User interface frameworks use Observer extensively — when a data model changes, all views that display that data update automatically.

[SHOW DIAGRAM: Strategy pattern — Context has a Strategy reference; ConcreteStrategyA and ConcreteStrategyB implement the Strategy interface]

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. The algorithm can vary independently from the clients that use it. A payment processing system might support credit card, PayPal, and bank transfer — each implemented as a separate strategy class. The checkout process selects the appropriate strategy at runtime without any conditional logic in the checkout code.

PSM I Exam Tip: Observer and Strategy both reduce coupling between components — which directly supports Scrum's goal of sustainable delivery. When components are loosely coupled, changes in one Sprint are less likely to break work done in previous Sprints."

---

## Section 5 — Anti-Patterns, Technical Debt, and Closing [16:00–20:00]

"Before we close, I want to address anti-patterns — specifically the God Object.

[SHOW DIAGRAM: God Object anti-pattern — large class in center with arrows pointing to every other class in the system]

A God Object is a class that knows too much and does too much. It has hundreds or thousands of lines of code, handles authentication, business logic, data access, logging, and error handling all in one place. Teams fall into this pattern incrementally — it starts small and grows with each Sprint because adding to the existing class is easier than designing a new one.

The problem is that a God Object violates the Single Responsibility Principle. When everything is in one place, any change risks breaking everything. Sprint work slows down because developers spend more time understanding and testing the God Object than writing new features. This is technical debt becoming technical drag.

Design patterns are one of the primary tools for escaping the God Object: Factory Method to separate creation, Strategy to separate algorithms, Facade to provide a clean interface while the internals are refactored.

Where does design pattern work fit in a Sprint? Pattern implementation is legitimate Sprint work when it is part of meeting the Definition of Done — code quality standards — or when technical debt from poor design is directly blocking feature development. The Scrum Master helps the team make this work visible to the Product Owner by connecting it to future Sprint capacity.

In Module 12 we move to Test-Driven Development and Behavior-Driven Development — practices that work hand-in-hand with good design. When your code is well-designed with patterns, it is also more testable. See you there."

---

## End Card

- Next module: Module 12 – Test-Driven Development and BDD
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
