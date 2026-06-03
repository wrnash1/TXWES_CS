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
