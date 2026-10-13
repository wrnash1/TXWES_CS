# Quiz: Module 12 — Software Design Patterns

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

## Question 1

A developer is building a SQL query construction library. Users need to combine optional clauses — WHERE, ORDER BY, LIMIT, JOIN — in any combination. The final SQL string should only be produced when all clauses have been specified. Which creational pattern best fits this requirement?

- A) Singleton — to ensure only one query object is active per database connection
- B) Builder — to construct the complex query object step-by-step using method chaining, producing the final string with a `build()` call
- C) Factory Method — to create different types of queries (SELECT, INSERT, UPDATE) at runtime
- D) Adapter — to convert the query object into a format compatible with the database driver

Correct Answer: B — Builder is designed for constructing complex objects with many optional parts. Method chaining allows each optional clause to be added independently, and `build()` produces the final result only when construction is complete. The user can add any combination of clauses without affecting others.

Distractor Analysis:

- A is incorrect — Singleton controls instance count; it does not manage construction of complex objects with optional parts
- C is incorrect — Factory Method handles choosing which type to create, not assembling a single complex object from optional parts
- D is incorrect — Adapter resolves interface incompatibilities between existing classes; it is not a construction pattern

---

## Question 2

In the Observer pattern, what is the primary structural advantage of storing observers as objects implementing a common interface rather than storing references to specific observer classes?

- A) It makes the notify loop run faster because interface dispatch is more efficient than direct method calls
- B) The subject can notify any number of observer types added in future development without any change to the subject class
- C) It prevents observers from unsubscribing, ensuring all notifications are always delivered
- D) It limits the pattern to exactly one observer per subject, maintaining the one-to-many relationship

Correct Answer: B — By depending on an observer interface rather than concrete observer types, the subject is decoupled from specific implementations. New observer types (new features in future Sprints) can be added without touching the subject at all. This is the Open/Closed Principle applied to the Observer pattern.

Distractor Analysis:

- A is incorrect — interface dispatch has no meaningful performance advantage over direct method calls in this context; performance is not the reason for the interface
- C is incorrect — Observer implementations always include unsubscribe functionality; the interface does not prevent removal
- D is incorrect — Observer is explicitly a one-to-many pattern — the subject can have any number of observers; the interface does not limit this

---

## Question 3

The Decorator pattern and the Facade pattern both "wrap" other objects. What is the fundamental difference between them?

- A) Decorator is a Creational pattern; Facade is a Structural pattern
- B) Decorator adds behavior to an existing object without changing its interface; Facade provides a new simplified interface to a complex subsystem
- C) Facade can only wrap one class at a time; Decorator can wrap many classes simultaneously
- D) Decorator requires subclassing; Facade uses composition exclusively

Correct Answer: B — The key distinction is intent and interface. Decorator preserves the original interface while adding behavior (the client sees the same interface, just with more functionality). Facade introduces a new, simpler interface that hides the complexity of multiple subsystem classes from the caller.

Distractor Analysis:

- A is incorrect — both Decorator and Facade are Structural patterns; they are in the same Gang of Four category
- C is incorrect — both patterns can wrap multiple classes; Facade typically aggregates several subsystem classes, while Decorators chain multiple wrappers
- D is incorrect — Decorator uses composition (wrapping), not subclassing, which is explicitly its advantage over inheritance; Facade also uses composition

---

## Question 4

A Command object in the Command pattern must implement which two methods to support undo functionality?

- A) `run()` and `rollback()`
- B) `execute()` and `undo()`
- C) `send()` and `cancel()`
- D) `process()` and `revert()`

Correct Answer: B — The standard Command pattern interface defines `execute()` to perform the operation and `undo()` to reverse it. The CommandHistory stores executed commands and calls `undo()` on them in reverse order. While naming conventions vary in practice, `execute()` and `undo()` are the canonical names from the Gang of Four.

Distractor Analysis:

- A names `run()` and `rollback()` — these are used in some frameworks but are not the canonical Gang of Four names; `rollback()` is more commonly associated with database transaction patterns
- C names `send()` and `cancel()` — these might be used in a specific messaging domain but are not the Command pattern's standard interface
- D names `process()` and `revert()` — non-standard naming not associated with the Gang of Four Command pattern definition

---

## Question 5

A new team member asks why the Factory Method pattern is used in the payment processing module instead of directly calling `new CreditCardProcessor()` or `new PayPalProcessor()` in the checkout code. What is the best explanation?

- A) Factory Method prevents more than one payment processor from running simultaneously, avoiding double charges
- B) Factory Method centralizes the creation logic so that adding a new payment method requires adding only a new class and a registry entry — no changes to checkout code that calls the factory
- C) Factory Method automatically validates payment data before creating the processor object, replacing input validation code
- D) Factory Method is required to satisfy the Observer pattern, which cannot function without a factory to create subscriber objects

Correct Answer: B — Factory Method embodies the Open/Closed Principle. Adding a new payment provider (a new Sprint feature) means adding a new class that extends the base and one entry in the factory's registry. The checkout code that calls `createPaymentProcessor(method)` never changes. Without the factory, every new payment method would require finding and modifying all places that call `new SpecificProcessor()`.

Distractor Analysis:

- A is incorrect — Factory Method has no instance-limiting behavior; that is Singleton's purpose
- C is incorrect — Factory Method creates objects; input validation is a separate responsibility that should not be embedded in object creation
- D is incorrect — Observer and Factory Method are independent patterns; Observer does not require a factory

---

## Question 6

The Strategy pattern and the Command pattern both encapsulate behavior. What is the most important distinction between them?

- A) Strategy patterns can only be used in JavaScript; Command patterns work in all languages
- B) Strategy encapsulates interchangeable algorithms selected at runtime; Command encapsulates a specific request as an object that can be stored, queued, or reversed
- C) Strategy requires the Observer pattern to function; Command does not
- D) Command objects are always synchronous; Strategy objects always run asynchronously

Correct Answer: B — Strategy is about choosing between alternative algorithms that accomplish the same goal differently (sort this data with algorithm A or B). Command is about treating a specific operation as a first-class object that can be scheduled, logged, or undone (execute this action now or later, and be able to reverse it).

Distractor Analysis:

- A is incorrect — both patterns work in any object-oriented language; they are language-agnostic design solutions
- C is incorrect — Strategy and Command are independent patterns with no structural dependency on each other or on Observer
- D is incorrect — both patterns can be used synchronously or asynchronously depending on implementation; synchronicity is not a definitional property of either

---

## Question 7

Which creational pattern is most appropriate when a class represents a shared application-wide resource — such as a thread pool or global event bus — that must have exactly one instance, regardless of how many modules request it?

- A) Builder — to assemble the resource from configurable parts
- B) Factory Method — to create the right type of resource based on the runtime environment
- C) Singleton — to ensure only one instance is ever created and shared across all callers
- D) Prototype — to create new instances by cloning an existing configured instance

Correct Answer: C — Singleton is specifically designed for exactly this use case: a shared resource that must exist as a single instance. All callers get the same object via a static `getInstance()` method. The first call creates the instance; subsequent calls return the same reference.

Distractor Analysis:

- A is incorrect — Builder handles construction of complex objects with optional parts; it creates new objects, not single shared instances
- B is incorrect — Factory Method handles choosing the type to create; it can create many instances of many types, the opposite of Singleton's constraint
- D is incorrect — Prototype creates new instances by cloning; it produces multiple copies, which is the opposite of Singleton's single-instance guarantee

---

## Question 8

A legacy API uses `getCustomerInfo(customerId)` but the new application code expects `fetchUser(userId)`. Without modifying either the legacy API or the new application code, which pattern creates a bridge?

- A) Strategy — by defining `getCustomerInfo` and `fetchUser` as interchangeable algorithms
- B) Facade — by wrapping both the legacy API and the new code in a single simplified interface
- C) Adapter — by wrapping the legacy API in a class that exposes `fetchUser(userId)` and internally calls `getCustomerInfo(userId)`
- D) Command — by encapsulating both method calls as reversible command objects

Correct Answer: C — The Adapter pattern is the canonical solution for interface incompatibility. An Adapter class exposes the interface the new code expects (`fetchUser(userId)`) and internally translates that call to the legacy API's method (`getCustomerInfo(customerId)`). Neither the caller nor the legacy API needs to change.

Distractor Analysis:

- A is incorrect — Strategy defines interchangeable algorithms for the same purpose; it does not bridge different method signatures
- B is incorrect — Facade simplifies access to a complex subsystem; it does not specifically solve an interface naming mismatch between two existing APIs
- D is incorrect — Command encapsulates operations for scheduling and reversibility; it does not resolve interface incompatibility

---

## Question 9

A Scrum team notices that every new notification type added in a Sprint requires modifying the `EventNotifier` class. The Product Owner is frustrated because "simple" features take multiple days. After reviewing the code, the architect recommends refactoring to the Observer pattern. How does the Observer pattern directly solve this problem?

- A) Observer replaces the EventNotifier class entirely, removing the need for a notification system
- B) Observer allows new notification types to be added as new observer classes that subscribe to the subject — the EventNotifier subject class never needs to change for new notification types
- C) Observer automatically generates notification classes using a code generation tool, reducing developer effort
- D) Observer limits each event to one notification type, preventing the system from growing too complex

Correct Answer: B — With Observer, `EventNotifier` (the Subject) holds a list of objects implementing a Notifier interface. Adding a new notification type means adding a new class that implements the interface and subscribing it to the subject. The subject class is closed for modification — it never changes when new notification types are added.

Distractor Analysis:

- A is incorrect — Observer does not remove the need for a notification subject; it restructures how subjects and observers relate to each other
- C is incorrect — Observer is a design pattern, not a code generation tool; it requires manual implementation of observer classes
- D is incorrect — Observer is a one-to-many pattern designed to support many observers; it does not limit the system to one notification type

---

## Question 10

Which of the following correctly maps the Facade pattern to its primary benefit in a Scrum team context?

- A) Facade allows multiple algorithms to be swapped at runtime, enabling the team to ship different sorting behaviors in the same Sprint
- B) Facade simplifies a complex subsystem into one clean interface, reducing the cognitive load for developers adding features in future Sprints
- C) Facade ensures only one instance of the subsystem exists, preventing resource conflicts between Sprint features
- D) Facade records all operations performed on the subsystem, enabling the team to audit and undo previous Sprint work

Correct Answer: B — Facade provides a simplified interface to a complex subsystem. For a Scrum team, this means developers working on new Sprint features interact with a small, understandable API rather than navigating the full complexity of the subsystem. This reduces onboarding time, minimizes mistakes, and makes new features faster to implement.

Distractor Analysis:

- A is incorrect — swapping algorithms at runtime describes the Strategy pattern, not Facade
- C is incorrect — ensuring one instance is the Singleton pattern's purpose; Facade does not control instance count
- D is incorrect — recording operations for audit and undo describes the Command pattern, not Facade

---

### Question 11 (5 points)

A text editor needs to support undo and redo for insert, delete, and format operations. Each operation should be reversible and stored in a history stack. Which pattern is most appropriate?

- A) Observer — to notify all UI components when the document changes
- B) Strategy — to make insert, delete, and format interchangeable algorithms
- C) Command — to encapsulate each operation as an object with execute() and undo() methods stored in a history stack
- D) Builder — to construct the document state step-by-step using method chaining

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Observer handles event notification to multiple dependents; it does not encapsulate operations for reversal or queuing.
  - Why B is incorrect: Strategy defines interchangeable algorithms for the same task; it does not provide a mechanism for storing and reversing past operations.
  - Why D is incorrect: Builder constructs complex objects incrementally; it does not represent executable, reversible operations.

---

### Question 12 (5 points)

The Builder pattern's method chaining (fluent interface) returns `this` from each setter method. What is the primary design reason for this?

- A) It prevents other objects from modifying the builder's internal state during construction
- B) It allows each configuration step to be called in sequence on the same object without storing intermediate variables
- C) It ensures the builder's `build()` method is called last by making it the only method that does not return `this`
- D) It restricts the builder to creating exactly one type of output object per chain

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Method chaining does not provide immutability or access protection; it is purely a usability convenience for calling multiple setters.
  - Why C is incorrect: While `build()` typically produces the final object and may not return `this`, this is a convention — the primary reason for chaining is readability and convenience, not to enforce call ordering.
  - Why D is incorrect: Method chaining does not restrict output types; a builder can produce different object representations based on how it is configured.

---

### Question 13 (5 points)

A team is choosing between the Adapter pattern and the Facade pattern to resolve a problem. The existing code has three complex subsystems (authentication, database, cache) that each work correctly individually but require a developer to coordinate all three with many setup steps every time a new feature is written. Which pattern is more appropriate and why?

- A) Adapter — because the three subsystems have incompatible interfaces that need to be bridged
- B) Facade — because the subsystems work correctly but exposing a single simplified method hides the multi-step coordination from feature developers
- C) Adapter — because wrapping each subsystem with a common interface allows them to be used interchangeably
- D) Facade — because it converts the interfaces of the three subsystems into a new format expected by the calling code

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The scenario does not describe an interface incompatibility — the subsystems work fine. The problem is coordination complexity, not interface mismatch.
  - Why C is incorrect: Making the three subsystems interchangeable describes Strategy; the scenario needs a single initialization point, not swappability.
  - Why D is incorrect: Converting interfaces describes Adapter. Facade does not convert interfaces — it hides complexity behind a new simpler interface.

---

### Question 14 (5 points)

Which of the following correctly identifies a risk of overusing the Singleton pattern in a codebase?

- A) Singleton prevents polymorphism because it uses a private constructor
- B) Singleton creates hidden global state that is shared across all tests, making it difficult to isolate test cases
- C) Singleton increases coupling by requiring all callers to implement the Observer interface
- D) Singleton violates the Open/Closed Principle because adding new behavior always requires modifying the Singleton class

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Singleton does restrict subclassing via a private constructor, but this is not the most significant practical risk in most codebases.
  - Why C is incorrect: Singleton has no connection to the Observer interface; callers simply call `getInstance()` — no interface implementation is required.
  - Why D is incorrect: The Open/Closed Principle concern for Singleton is relevant but minor compared to test isolation issues; it is also not inherent to the pattern structure.

---

### Question 15 (5 points)

A developer has both an Observer pattern and a Strategy pattern in the same module. A colleague says: "Both patterns use an interface — they must solve the same problem." What is the correct distinction?

- A) Observer's interface has only one method (update); Strategy's interface always has many methods
- B) Observer's interface defines how subjects push state changes to passive dependents; Strategy's interface defines how a context delegates active algorithm execution
- C) Observer is a Creational pattern; Strategy is a Structural pattern — their categories define their different purposes
- D) Observer requires more memory than Strategy because it stores a list of objects

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The number of methods in an interface is not the defining distinction; both can have interfaces with one or multiple methods depending on implementation.
  - Why C is incorrect: Both Observer and Strategy are Behavioral patterns — this answer is factually incorrect.
  - Why D is incorrect: Memory characteristics are an implementation detail, not a design-level distinction between the patterns' purposes.

---

### Question 16 (5 points)

The Command pattern's `CommandHistory` class stores executed commands. When `undo()` is called, what is the correct behavior?

- A) The history is cleared and all commands are re-executed in the original order
- B) The most recently executed command's `undo()` method is called, and the command is removed from the history stack
- C) All commands in the history are undone simultaneously in a batch operation
- D) The history is sent to a remote logging service before the undo operation begins

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Clearing and re-executing all commands would not undo the last operation — it would replay the entire history.
  - Why C is incorrect: Batch undo is not the standard Command pattern behavior; undo applies to one command at a time (the most recent), which is why a stack is used.
  - Why D is incorrect: Remote logging is a valid additional feature some systems add, but it is not part of the Command pattern's definition or its `undo()` behavior.

---

### Question 17 (5 points)

A Product Owner asks a developer: "Why does adding a new payment method take three days? It should be a simple dropdown change." The developer responds: "Because there's no Factory — every place in the code that processes payments has hard-coded conditionals for each payment type." Which pattern would directly fix this problem?

- A) Observer — to notify all payment processing screens when a new payment type is added
- B) Singleton — to ensure only one payment processor instance handles all transactions
- C) Factory Method — to centralize payment processor creation so new types require only a new class and one registry entry
- D) Command — to encapsulate each payment as a reversible operation

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Observer handles event notifications between components; it does not eliminate scattered conditional logic about which class to instantiate.
  - Why B is incorrect: Singleton controls instance count; it does not address the proliferation of type-selection conditionals across the codebase.
  - Why D is incorrect: Command handles reversibility and scheduling of operations; it does not address the problem of type selection during object creation.

---

### Question 18 (5 points)

In the Decorator pattern, each decorator holds a reference to a Component object (the thing it is wrapping). What happens when the decorator's own method is called?

- A) The decorator replaces the component entirely and executes its own logic without calling the wrapped component
- B) The decorator adds its own behavior before or after delegating the same method call to the wrapped component
- C) The decorator calls all registered observers and then executes the component's method
- D) The decorator uses a factory to create a new component each time its method is called

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: If the decorator replaced the component, the original behavior would be lost — this defeats the purpose of Decorator, which extends rather than replaces.
  - Why C is incorrect: Observer is a separate pattern; Decorator does not notify registered observers as part of its delegation mechanism.
  - Why D is incorrect: Decorator holds a fixed reference to its wrapped component; it does not use a factory to create new instances during method calls.

---

### Question 19 (5 points)

Which of the following scenarios describes correct use of the Builder pattern rather than a Factory Method or Singleton?

- A) Ensuring only one global event bus handles all application events throughout the session
- B) Creating the correct report generator (PDF, CSV, or Excel) based on a user's file format selection
- C) Constructing an HTTP request object with optional headers, query parameters, timeout settings, and body content using fluent method calls
- D) Wrapping a legacy XML parser so that it can be used with a modern JSON-based application

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: One shared global object describes Singleton — not a step-by-step construction scenario.
  - Why B is incorrect: Choosing which class to create based on runtime input describes Factory Method — type selection, not incremental construction.
  - Why D is incorrect: Wrapping a legacy interface for compatibility describes Adapter — interface bridging, not step-by-step object assembly.

---

### Question 20 (5 points)

A Scrum team's velocity drops because every Sprint that adds a new report type requires modifying five existing classes. Which design pattern would most directly prevent this from recurring?

- A) Singleton — to ensure only one ReportManager instance handles all report generation
- B) Observer — to notify all existing report classes when a new report type is added
- C) Strategy — to define each report type as a separate class implementing a common ReportStrategy interface, so new types are added without modifying existing code
- D) Facade — to hide the five existing report classes behind a single simplified interface

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Singleton controls instance count; it does not prevent modifications to existing code when new variants are added.
  - Why B is incorrect: Observer handles state-change notification; it does not address the structural problem of type selection and modification coupling.
  - Why D is incorrect: Facade simplifies access to existing complexity but does not prevent modification of the subsystem classes when new types are added.

---
