# Quiz: Module 11 – Software Design Patterns

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A logging service must ensure that only one instance exists across an entire application and all components share the same log output stream. Which design pattern is most appropriate?

- A) Factory Method — to create different logger types based on runtime configuration
- B) Observer — to notify all components when a new log entry is written
- C) Singleton — to restrict instantiation to a single shared logger instance
- D) Decorator — to add log formatting behavior dynamically at runtime

Correct Answer: C — The Singleton pattern restricts a class to a single instance and provides a global access point to it. This is ideal for shared resources like a logging service where all callers must write to the same output stream.

Distractor Analysis:

- Why A is incorrect: Factory Method creates objects of different types based on context — it does not prevent multiple instances of the same class from being created.
- Why B is incorrect: Observer defines a publish-subscribe notification relationship — a behavioral pattern for event propagation, not for controlling the number of instances.
- Why D is incorrect: Decorator adds behavior to an object dynamically — a structural pattern for extending functionality, not for limiting instance count.

---

## Question 2

Which of the following best describes the Strategy design pattern?

- A) A pattern that ensures a class has only one instance and provides a global access point to it
- B) A pattern that defines a family of interchangeable algorithms, encapsulates each one, and makes them swappable at runtime without changing the client code
- C) A pattern that converts the interface of a class into another interface that clients expect, resolving incompatibility between existing classes
- D) A pattern that composes objects into tree structures to represent part-whole hierarchies, treating individual objects and compositions uniformly

Correct Answer: B — The Strategy pattern defines a set of algorithms that can be swapped independently of the clients that use them — for example, swapping one sorting algorithm for another without changing the code that calls the sort.

Distractor Analysis:

- Why A is incorrect: This describes the Singleton pattern, which controls instance creation, not algorithm selection.
- Why C is incorrect: This describes the Adapter pattern, which resolves interface incompatibilities — a structural pattern.
- Why D is incorrect: This describes the Composite pattern, which manages tree-structured object hierarchies — a structural pattern.

---

## Question 3

Which category does the Observer pattern belong to in the Gang of Four classification?

- A) Creational — because it creates subscriber objects dynamically
- B) Structural — because it defines the structure of the subject-observer relationship
- C) Behavioral — because it defines communication and responsibility distribution between objects
- D) Architectural — because it implements the Model-View-Controller separation of concerns

Correct Answer: C — Behavioral patterns define how objects communicate and assign responsibilities. Observer defines the publish-subscribe communication protocol between a subject and its dependents — a behavioral concern.

Distractor Analysis:

- Why A is incorrect: Creational patterns address object creation mechanisms. Observer does not create subscriber objects — it registers existing objects with a subject.
- Why B is incorrect: Structural patterns describe how classes and objects are composed into larger structures. Observer is about communication flow, not static structural composition.
- Why D is incorrect: MVC is an architectural pattern; it is conceptually related to Observer but Observer itself is classified as Behavioral in the Gang of Four taxonomy.

---

## Question 4

A Scrum Team is experiencing slow Sprint velocity because every new feature requires changes to a central class that handles authentication, data access, business rules, and email notifications in a single 2,500-line file. Which design anti-pattern does this describe?

- A) Singleton — because only one instance of the class exists
- B) God Object — a class that violates Single Responsibility by centralizing too many concerns
- C) Facade — because the class provides a simplified interface to many subsystems
- D) Decorator — because the class wraps many different behaviors around a core object

Correct Answer: B — The God Object anti-pattern describes a class that knows too much and does too much. It violates the Single Responsibility Principle and creates high coupling — every feature change risks breaking something else, and developers must understand the entire class to change any part of it.

Distractor Analysis:

- Why A is incorrect: Singleton is a valid creational pattern for shared resources. The scenario describes a class that is problematic because of its scope of responsibility, not because of how many instances exist.
- Why C is incorrect: Facade is a structural pattern that intentionally provides a simplified interface to a complex subsystem — the subsystem itself remains well-organized behind the facade.
- Why D is incorrect: Decorator adds behavior dynamically without modifying a class — a well-designed structural pattern. The scenario describes uncontrolled growth of a single class's responsibilities.

---

## Question 5

The Factory Method pattern differs from directly instantiating objects with `new ClassName()` in what key way?

- A) Factory Method prevents the same class from being instantiated more than once per program execution
- B) Factory Method delegates the decision of which concrete class to instantiate to subclasses, allowing the code to remain open for extension without modification
- C) Factory Method automatically registers all created objects with an Observer subject for event notification
- D) Factory Method eliminates the need for constructors by building objects entirely from configuration files

Correct Answer: B — Factory Method defines an interface for creating an object but lets subclasses decide which class to instantiate. New product types can be added by creating new subclasses without modifying existing client code — this is the Open/Closed Principle in practice.

Distractor Analysis:

- Why A is incorrect: Preventing multiple instances is the Singleton pattern's purpose. Factory Method does not constrain instance count.
- Why C is incorrect: Factory Method has no inherent connection to Observer. Object registration with subjects is a separate design concern.
- Why D is incorrect: Factory Method is a code-level pattern that still uses constructors internally. It does not eliminate constructors or replace them with configuration files.

---

## Question 6

Which Agile Manifesto principle most directly justifies why Scrum teams should invest time in learning and applying design patterns?

- A) Principle 4 — Business people and developers must work together daily throughout the project
- B) Principle 9 — Continuous attention to technical excellence and good design enhances agility
- C) Principle 11 — The best architectures emerge from self-organizing teams
- D) Principle 7 — Working software is the primary measure of progress

Correct Answer: B — Agile Manifesto Principle 9 explicitly states that technical excellence and good design enhance agility. Design patterns are tools for achieving good design. Teams that use patterns build software that can be extended and modified across future Sprints without accumulating velocity-destroying technical debt.

Distractor Analysis:

- Why A is incorrect: Principle 4 concerns collaboration between business and technical stakeholders, not the quality of technical design choices.
- Why C is incorrect: The Agile Manifesto does not have a Principle 11. The twelfth principle is about regular reflection and adjustment.
- Why D is incorrect: Working software as the primary measure of progress relates to how progress is measured, not to the technical quality of how the software is built.

---

## Question 7

A developer needs to add encryption, buffering, and compression to a file output stream. Each combination of these behaviors should work independently and be stackable in any order. Which design pattern best solves this?

- A) Singleton — to ensure only one stream instance is active at a time
- B) Observer — to notify compression and encryption components when data is written
- C) Decorator — to wrap the stream with additional behaviors dynamically and stackably
- D) Facade — to provide a single interface that handles all three behaviors together

Correct Answer: C — The Decorator pattern attaches additional responsibilities to an object dynamically. Multiple decorators can be stacked — each wrapping the previous — to combine behaviors without subclassing or modifying the original class. Java's I/O library is the canonical real-world example.

Distractor Analysis:

- Why A is incorrect: Singleton controls instance count, not behavior stacking. A Singleton stream cannot have behaviors added dynamically.
- Why B is incorrect: Observer defines event notification between objects — it does not add processing behavior to a data stream.
- Why D is incorrect: Facade provides a simplified interface to existing complexity but does not enable runtime-composable behavior stacking.

---

## Question 8

A third-party payment library exposes a method called `executeTransaction(transactionData)` but your application code expects a method called `processPayment(amount, currency, cardToken)`. Without modifying either the library or the application code, which pattern resolves this incompatibility?

- A) Strategy — by defining a family of payment algorithms and making them interchangeable
- B) Adapter — by creating a wrapper class that translates the expected method signature into the library's method signature
- C) Factory Method — by creating a factory that produces different payment processor objects at runtime
- D) Singleton — by ensuring only one payment service instance manages all transactions

Correct Answer: B — The Adapter pattern converts one interface into another that the client expects. An Adapter class would expose `processPayment(amount, currency, cardToken)`, internally construct the `transactionData` object, and delegate to `executeTransaction(transactionData)` — bridging the two incompatible interfaces.

Distractor Analysis:

- Why A is incorrect: Strategy handles algorithm swapping where both algorithms implement the same interface. The problem here is an interface mismatch, not algorithm selection.
- Why C is incorrect: Factory Method creates objects of different types — it does not solve an interface incompatibility between an existing caller and an existing library.
- Why D is incorrect: Singleton controls instance count. Having one payment service does not resolve the method signature incompatibility between the application and the library.

---

## Question 9

A Scrum team wants to refactor a God Object class. The Product Owner asks: "Why should we spend Sprint capacity on code cleanup instead of new features?" What is the most effective Scrum Master response?

- A) "The Scrum Guide requires a Definition of Done that prohibits God Objects, so we must fix it."
- B) "Refactoring this class will reduce the coupling and risk that currently causes every new feature to break existing functionality — directly increasing our Sprint velocity and ability to deliver features faster."
- C) "Technical debt is the developer's responsibility to fix in their own time outside of Sprints."
- D) "We should not include refactoring in Sprints — it should be done during Sprint 0."

Correct Answer: B — The Scrum Master's role includes helping the Product Owner understand the value of technical work. Connecting the refactoring to business outcomes — faster velocity, fewer bugs, reduced risk per feature — frames it in terms the Product Owner cares about.

Distractor Analysis:

- Why A is incorrect: The Scrum Guide does not prohibit specific code patterns or mandate specific refactoring. This claim is false and would undermine the Scrum Master's credibility.
- Why C is incorrect: Technical debt is the team's shared responsibility and is legitimate Sprint work when it directly affects the team's ability to deliver value.
- Why D is incorrect: "Sprint 0" is not a Scrum concept. The Scrum Guide describes only Sprints — there is no prescribed pre-Sprint phase. Technical work belongs in regular Sprints.

---

## Question 10

Which of the following best describes how the Observer pattern supports Scrum's goal of sustainable delivery?

- A) It enables the Scrum Team to observe the Product Owner's decisions and respond immediately
- B) It decouples the subject from its observers, so new features (new observers) can be added in future Sprints without modifying existing code
- C) It ensures that all team members observe the Definition of Done before marking a story complete
- D) It provides a mechanism for the Scrum Master to observe team performance metrics

Correct Answer: B — Observer reduces coupling: the subject knows nothing about the specific types of its observers, only that they implement the observer interface. New Sprint features that need to react to an event (new observers) are added as new classes without touching the subject or existing observers.

Distractor Analysis:

- Why A is incorrect: "Observe" in Observer refers to software objects subscribing to another object's state changes — not human observers watching people.
- Why C is incorrect: The Definition of Done is a Scrum artifact — a quality standard for Increments. It has no connection to the Observer design pattern.
- Why D is incorrect: Performance metrics observation is a Scrum Master coaching concern. The Observer pattern is a software design structure, not a management tool.

---
