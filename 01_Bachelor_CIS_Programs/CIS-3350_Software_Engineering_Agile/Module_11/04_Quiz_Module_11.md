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

### Question 11 (5 points)

A team is building a UI component library that needs to support dark mode, large-text mode, and high-contrast mode. Each mode adds styling behavior on top of the base component, and modes must be combinable. Which pattern is most appropriate?

- A) Singleton — ensure only one theme instance is active per session
- B) Factory Method — create different component types for each mode
- C) Decorator — wrap the base component with each mode's styling behavior, stackably
- D) Adapter — convert the component's interface to match the theme system's expectations

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Singleton controls instance creation, not behavior stacking or visual styling composition.
  - Why B is incorrect: Factory Method creates different object types at construction time; it does not enable runtime-composable behavior layering on an existing object.
  - Why D is incorrect: Adapter resolves interface incompatibility between two existing systems; it does not add new behavior to an object dynamically.

---

### Question 12 (5 points)

The Gang of Four's Factory Method pattern adheres to which SOLID principle?

- A) Single Responsibility Principle — the factory has one job: creating objects
- B) Liskov Substitution Principle — factory subclasses must be substitutable for the parent factory
- C) Open/Closed Principle — new product types can be added by extending the factory without modifying existing client code
- D) Interface Segregation Principle — clients depend only on the narrow factory interface they use

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: While factories do focus on creation, the primary SOLID connection for Factory Method is extensibility without modification — the Open/Closed Principle.
  - Why B is incorrect: Liskov Substitution governs inheritance substitutability in general; it is not the defining principle embodied by Factory Method's design benefit.
  - Why D is incorrect: Interface Segregation concerns splitting large interfaces into smaller, focused ones — not the factory extension mechanism.

---

### Question 13 (5 points)

A Scrum team notices that their test suite runs for 45 minutes and that most of the time is spent setting up the God Object class for each test. Which technical consequence of the God Object does this illustrate?

- A) Thread-safety violations — the God Object creates race conditions in the test runner
- B) Poor testability — testing any small behavior requires constructing the entire class with all its dependencies
- C) Observer overloading — the God Object publishes too many events during test execution
- D) Adapter failure — the God Object cannot be adapted to the testing framework's interface

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Thread safety is a concern for Singleton in concurrent environments; the scenario describes slow test setup, not race conditions.
  - Why C is incorrect: Observer pattern overloading is not a property of the God Object anti-pattern; the God Object accumulates responsibilities, not event subscriptions.
  - Why D is incorrect: Adapter incompatibility is about interface mismatches between components, not the cost of setting up a large class for testing.

---

### Question 14 (5 points)

Which statement best describes the Facade pattern's relationship to the Scrum principle of simplicity?

- A) Facade eliminates all complexity in the subsystem, making simple code even simpler
- B) Facade hides complex subsystem interactions behind a simple interface, reducing cognitive load for callers without removing the underlying complexity
- C) Facade replaces the subsystem with a simpler implementation in every Sprint
- D) Facade is a behavioral pattern that simplifies communication between observers and subjects

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Facade does not eliminate subsystem complexity — the subsystem remains fully intact. It only provides a simpler access point.
  - Why C is incorrect: Facade does not replace or rewrite the subsystem each Sprint; it wraps existing complexity with a stable interface.
  - Why D is incorrect: Facade is a structural pattern, not a behavioral one; it concerns composition and interface exposure, not object communication.

---

### Question 15 (5 points)

A developer proposes adding a new sort algorithm as an additional `else if` branch inside an existing 200-line `sortData()` method. A colleague suggests using the Strategy pattern instead. What is the primary advantage of the Strategy approach?

- A) Strategy prevents other developers from calling `sortData()` directly, enforcing encapsulation
- B) Strategy extracts each algorithm into its own class, so new algorithms are added without modifying existing code, reducing regression risk
- C) Strategy ensures only one sorting algorithm can be active per application session
- D) Strategy automatically selects the best algorithm at compile time based on data size

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Strategy does not restrict access to methods; it is about algorithm interchangeability, not access control.
  - Why C is incorrect: Restricting to one instance is Singleton's concern; Strategy allows any algorithm to be active and swapped at runtime.
  - Why D is incorrect: Strategy is a runtime pattern that requires explicit selection by the context; it does not perform automatic compile-time optimization.

---

### Question 16 (5 points)

In the Observer pattern, what is the purpose of the `update()` method on the Observer interface?

- A) It allows the Subject to push new state data to each Observer when the Subject's state changes
- B) It allows the Observer to change the Subject's state on behalf of the user
- C) It creates a new Observer instance whenever the Subject receives an update
- D) It removes the Observer from the Subject's subscriber list after it receives a notification

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: Observers react to Subject state changes; they do not modify the Subject's state (doing so would create circular coupling).
  - Why C is incorrect: `update()` is called on existing Observer instances; it does not instantiate new objects.
  - Why D is incorrect: `update()` delivers the notification; removal from the subscriber list is a separate operation (typically `unsubscribe()` or `removeObserver()`).

---

### Question 17 (5 points)

Which of the following is a valid Scrum team action when a design pattern refactoring task is identified as necessary for the next Sprint's features?

- A) Defer the refactoring indefinitely because design work should be completed before Sprint 1 in a dedicated design Sprint
- B) Add the refactoring as a Product Backlog Item, let the Product Owner order it relative to other items, and include it in Sprint Planning when the team agrees it unblocks upcoming work
- C) Have developers refactor the code after Sprint hours to avoid using Sprint capacity
- D) Require the Scrum Master to approve all design pattern changes before implementation begins

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Scrum Guide does not prescribe a design Sprint. All work — including technical refactoring — is managed through the Product Backlog and Sprint cycle.
  - Why C is incorrect: Asking developers to work after hours violates sustainable pace, one of Scrum's implicit values. Technical work is legitimate Sprint work.
  - Why D is incorrect: The Scrum Master facilitates but does not approve or disapprove technical decisions; that authority belongs to the Developers.

---

### Question 18 (5 points)

A Singleton class in a multi-threaded web application creates a new instance for each user request because the `getInstance()` method is not synchronized. Which Singleton characteristic is violated?

- A) Single responsibility — the class is doing more than managing its own instance
- B) Thread safety — simultaneous calls to `getInstance()` bypass the null check and create multiple instances
- C) Open/Closed — adding new users requires modifying the Singleton class
- D) Substitutability — subclasses of the Singleton cannot be used in place of the parent class

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Single Responsibility relates to what a class does, not how many instances are created; this scenario is about concurrency, not scope of responsibility.
  - Why C is incorrect: Open/Closed governs class modification for new behavior; adding users to a web application does not require modifying the Singleton class.
  - Why D is incorrect: Liskov Substitution concerns subclass behavior compatibility; Singleton classically restricts subclassing, but the issue here is concurrent instance creation.

---

### Question 19 (5 points)

Which of the following scenarios best demonstrates the Adapter pattern rather than the Decorator pattern?

- A) Adding caching behavior to an existing database query object without modifying its class
- B) Wrapping a legacy SOAP web service client with a method signature that the modern REST-based application expects
- C) Stacking compression, encryption, and buffering on a network output stream
- D) Providing a single startup method that initializes a complex set of interdependent services

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Adding caching to an existing object without modifying it describes Decorator — new behavior wrapping an existing interface.
  - Why C is incorrect: Stacking multiple behaviors on a stream object describes Decorator — composable, stackable behavioral additions.
  - Why D is incorrect: A single startup method hiding internal complexity describes Facade — simplifying access to a complex subsystem.

---

### Question 20 (5 points)

A Scrum Master says: "Our design patterns directly support the Agile Manifesto." Which Manifesto principle provides the strongest direct support for this claim?

- A) Principle 1 — our highest priority is to satisfy the customer through early and continuous delivery of valuable software
- B) Principle 6 — the most efficient method of conveying information is face-to-face conversation
- C) Principle 9 — continuous attention to technical excellence and good design enhances agility
- D) Principle 12 — at regular intervals, the team reflects on how to become more effective

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Principle 1 is about delivery cadence and customer satisfaction — it supports Agile broadly but does not specifically mention design quality or technical practices.
  - Why B is incorrect: Principle 6 concerns communication methods within the team — it is unrelated to software design quality or patterns.
  - Why D is incorrect: Principle 12 supports the Retrospective as an improvement mechanism — it relates to process improvement, not specifically to the technical quality of design choices.

---
