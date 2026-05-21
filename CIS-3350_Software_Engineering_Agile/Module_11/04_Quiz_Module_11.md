# Quiz: Module 11 – Software Design Patterns

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

A logging service must ensure that only one instance exists across an entire application, and all components share the same log output stream. Which design pattern is most appropriate?

* A) Factory Method — to create different logger types based on runtime configuration
* B) Observer — to notify all components when a new log entry is written
* C) Singleton — to restrict instantiation to a single shared logger instance
* D) Decorator — to add log formatting behavior dynamically at runtime

Correct Answer: C) The Singleton pattern restricts a class to a single instance and provides a global access point — ideal for shared resources like a logging service.

Distractor Analysis:

* *Why C is correct:* The Singleton pattern ensures only one logger object is ever created; all callers receive a reference to the same instance, guaranteeing a single shared log stream.
* *Why A is incorrect:* Factory Method creates objects of different types based on context — it does not prevent multiple instances of the same class from being created.
* *Why B is incorrect:* Observer defines a one-to-many notification relationship between objects — it is a behavioral pattern for event propagation, not for controlling instantiation count.
* *Why D is incorrect:* Decorator adds behavior to an object dynamically without changing its class — it is a structural pattern for extending functionality, not for limiting instance count.

---

### Question 2

Which of the following is the most accurate definition of the Strategy design pattern?

* A) A pattern that ensures a class has only one instance and provides a global access point to it.
* B) A pattern that defines a family of interchangeable algorithms, encapsulates each one, and makes them swappable at runtime without changing the client code.
* C) A pattern that converts the interface of a class into another interface that clients expect, resolving incompatibility between existing classes.
* D) A pattern that composes objects into tree structures to represent part-whole hierarchies, treating individual objects and compositions uniformly.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* The Strategy pattern defines a set of algorithms that can be swapped independently of the clients that use them — for example, swapping a bubble sort for a merge sort without changing the code that calls the sort.
* *Why A is incorrect:* This describes the Singleton pattern, which controls instance creation — not algorithm swapping.
* *Why C is incorrect:* This describes the Adapter pattern, which resolves interface incompatibilities between classes — a structural pattern, not a behavioral one.
* *Why D is incorrect:* This describes the Composite pattern, which treats individual objects and tree-structured groups of objects uniformly — a structural pattern.

---

### Question 3

Which category does the Observer pattern belong to in the Gang of Four classification?

* A) Creational — because it creates subscriber objects dynamically
* B) Structural — because it defines the structure of the subject-observer relationship
* C) Behavioral — because it defines communication and responsibility distribution between objects
* D) Architectural — because it implements the Model-View-Controller separation of concerns

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* Behavioral patterns define how objects communicate and assign responsibilities. Observer defines the publish-subscribe communication protocol between a subject and its dependents — a behavioral concern.
* *Why A is incorrect:* Creational patterns address object creation mechanisms. Observer does not create subscriber objects — it registers them with a subject.
* *Why B is incorrect:* Structural patterns describe how classes and objects are composed. Observer is about communication flow, not static structural composition.
* *Why D is incorrect:* MVC is an architectural pattern; it is related to Observer conceptually but the Observer pattern itself is classified as Behavioral in the GoF taxonomy.

---

### Question 4

A Scrum Team is experiencing slow Sprint velocity because every new feature requires changes to a central "Manager" class that handles authentication, data access, and business rules in a single 2,000-line file. Which software design principle and pattern would best resolve this?

* A) Apply the Singleton pattern so only one Manager instance exists, reducing memory usage.
* B) Apply the Facade pattern so external classes interact with the Manager through a simplified interface.
* C) Decompose the Manager class according to the Single Responsibility Principle, separating concerns into distinct classes.
* D) Apply the Decorator pattern to add new behaviors to the Manager class without modifying it.

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* The "God Object" anti-pattern (one class doing everything) violates Single Responsibility and creates tight coupling — every feature change risks breaking other features. Decomposing into focused, single-responsibility classes makes the codebase safer to extend in each Sprint.
* *Why A is incorrect:* Singleton controls instance count, not class responsibility scope. A Singleton God Object is still a God Object.
* *Why B is incorrect:* Facade provides a simplified interface to a subsystem but does not fix the underlying architectural problem of one class carrying too many responsibilities.
* *Why D is incorrect:* Decorator adds behaviors to objects dynamically but does not resolve the structural problem of a class with mixed, tightly coupled responsibilities.

---

### Question 5

The Factory Method pattern differs from directly instantiating objects with `new ClassName()` in what key way?

* A) Factory Method prevents the same class from being instantiated more than once per program execution.
* B) Factory Method delegates the decision of which concrete class to instantiate to subclasses, allowing the code to remain open for extension without modification.
* C) Factory Method automatically registers all created objects with an Observer subject for event notification.
* D) Factory Method eliminates the need for constructors by building objects entirely from configuration files.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* The Factory Method pattern defines an interface for creating an object but lets subclasses decide which class to instantiate — enabling new object types to be added without modifying existing client code (Open/Closed Principle).
* *Why A is incorrect:* Preventing multiple instances is the Singleton pattern's purpose. Factory Method does not constrain instance count.
* *Why C is incorrect:* Factory Method has no inherent connection to the Observer pattern. Object registration with subjects is a separate design concern.
* *Why D is incorrect:* Factory Method is a code-level pattern that still uses constructors internally. It does not eliminate constructors or replace them with configuration files.
