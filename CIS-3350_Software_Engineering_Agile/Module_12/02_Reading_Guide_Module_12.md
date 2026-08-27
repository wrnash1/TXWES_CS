# Reading Guide: Module 12 — Software Design Patterns

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Overview

This reading guide supports the Module 12 video lecture on software design patterns. Use it to study pattern structures, compare patterns in the same category, review code examples, and prepare for the module quiz.

**Core Learning Objectives:**

- Identify all nine module patterns by name, category, and core intent
- Compare patterns within each category based on problem solved and structural approach
- Apply pattern selection criteria to realistic design scenarios
- Connect design patterns to Agile Manifesto principles and Scrum team sustainability

---

## Part 1: Pattern Category Overview

### 1.1 The Three Categories at a Glance

| Category | Core Concern | Patterns in This Module |
|----------|-------------|-------------------------|
| Creational | How objects are created; decoupling instantiation from usage | Singleton, Factory Method, Builder |
| Structural | How classes and objects compose into larger structures | Adapter, Decorator, Facade |
| Behavioral | How objects communicate and distribute responsibility | Observer, Strategy, Command |

### 1.2 When to Reach for Each Category

- Use a **Creational** pattern when object construction is complex, involves decision logic about which type to create, or must be controlled (single instance, optional parts, step-by-step assembly)
- Use a **Structural** pattern when two things that should work together don't fit — either because of interface mismatch, needed behavior addition, or complexity hiding
- Use a **Behavioral** pattern when you need to control how objects interact over time — notifications, interchangeable logic, or reversible operations

---

## Part 2: Creational Patterns

### 2.1 Singleton

**Intent:** Ensure a class has exactly one instance; provide a global access point.

**Structure:**

```text
AppConfig
  - _instance: AppConfig (static, private)
  + getInstance(): AppConfig (static)
  - constructor() (private by convention)
  + theme: string
  + apiUrl: string
```

**Key implementation elements:**

- Private or convention-guarded constructor
- Static `_instance` variable initialized to null
- Static `getInstance()` method: create on first call, return stored reference on all subsequent calls

**Thread-safety concern:** In multi-threaded environments, two threads can simultaneously pass the `_instance === null` check and both create instances. Solutions include eager initialization (create at class load time) or synchronized access with a lock.

**When to use Singleton:**

- Shared logging service
- Configuration or settings manager
- Database connection pool
- Application-wide cache

**When NOT to use Singleton:**

- When unit testing — Singleton state persists between tests unless explicitly reset, creating test isolation problems
- When multiple instances would be valid — don't use Singleton just to avoid passing arguments

### 2.2 Factory Method

**Intent:** Define an interface for creating an object but let subclasses or a factory function decide which class to instantiate.

**Structure:**

```text
createPaymentProcessor(method: string): PaymentProcessor
  ↓
  processors map: { creditCard → CreditCardProcessor, paypal → PayPalProcessor, ... }
  ↓
  returns: new ProcessorClass()

PaymentProcessor (abstract base)
  └── CreditCardProcessor
  └── PayPalProcessor
  └── BankTransferProcessor
```

**Key benefit:** Adding a new product type requires adding a new class and one registry entry. No existing code changes. This is the Open/Closed Principle: open for extension, closed for modification.

**When to use Factory Method:**

- Payment processors, shipping providers, document formats — any situation where you need an object whose type depends on runtime context
- When you want to centralize object creation logic so caller code stays clean

### 2.3 Builder

**Intent:** Construct a complex object step-by-step, allowing different representations using the same construction process.

**Structure:**

```text
QueryBuilder
  + select(...columns): QueryBuilder   ← returns this (chaining)
  + where(condition): QueryBuilder     ← returns this (chaining)
  + orderBy(column): QueryBuilder      ← returns this (chaining)
  + limit(n): QueryBuilder             ← returns this (chaining)
  + build(): string                    ← produces the final object
```

**Method chaining:** Each setter returns `this`, enabling fluent API style:

```javascript
const query = new QueryBuilder('users')
  .select('id', 'email')
  .where('active = true')
  .limit(100)
  .build();
```

**When to use Builder:**

- SQL query construction
- HTML/PDF/email template generation
- Configuration objects with many optional parameters
- HTTP request construction

### 2.4 Creational Pattern Comparison

| Pattern | Problem Solved | Key Structure | Returns |
|---------|---------------|---------------|---------|
| Singleton | Too many instances of a shared resource | Static instance check | Always the same object |
| Factory Method | Caller shouldn't know which class to instantiate | Registry or subclass override | New object of chosen type |
| Builder | Complex objects with many optional parts | Fluent setters + `build()` | Assembled object |

---

## Part 3: Structural Patterns

### 3.1 Adapter

**Intent:** Convert one interface into another that clients expect.

**Analogy:** A power adapter converts a European plug to a US socket without changing either the plug or the socket.

**Structure:**

```text
Client → [Target Interface: info(), warn(), error()]
              ↓
         ModernLoggerAdapter (implements Target)
              ↓ delegates to
         LegacyLogger (Adaptee: writeLog(severity, message))
```

**Key rule:** The Adapter is the only class that knows about both the target interface and the adaptee. Client code is fully decoupled from the legacy system.

**When to use Adapter:**

- Integrating third-party libraries whose APIs don't match your codebase
- Migrating from old to new interfaces incrementally
- Making independently developed components work together

### 3.2 Decorator

**Intent:** Attach additional responsibilities to an object dynamically without subclassing.

**Structure:**

```text
Component interface: send(url)
BaseRequest (ConcreteComponent)
LoggingDecorator (wraps Component, adds logging before delegating)
RetryDecorator (wraps Component, adds retry logic around delegation)

Stacked: RetryDecorator → LoggingDecorator → BaseRequest
```

**Why not subclassing?** If you have 3 behaviors (logging, retry, caching) and want all 7 combinations, subclassing requires 7 subclasses. Decorator requires 3 decorator classes that can be combined freely.

**When to use Decorator:**

- HTTP request middleware (logging, retry, auth headers, caching)
- I/O stream processing (buffering, compression, encryption)
- UI component enhancement (borders, shadows, scroll behavior)
- Any situation where behaviors need to be mixed and matched

### 3.3 Facade

**Intent:** Provide a simple interface to a complex or large subsystem.

**Key distinction from Adapter:** Adapter makes two incompatible things work together. Facade simplifies access to something that already works but is too complex for most use cases.

**When to use Facade:**

- System startup sequences involving many subsystems
- API gateways and service aggregators
- Library wrappers that expose the 20% of functionality used 80% of the time

### 3.4 Structural Pattern Comparison

| Pattern | Problem Solved | Relationship to Wrapped Class |
|---------|---------------|-------------------------------|
| Adapter | Interface incompatibility between two existing classes | Wraps Adaptee, exposes Target interface |
| Decorator | Add behaviors dynamically without modifying class | Wraps Component, adds behavior before/after delegation |
| Facade | Complex subsystem is hard to use | Wraps multiple subsystem classes in one simplified interface |

---

## Part 4: Behavioral Patterns

### 4.1 Observer

**Intent:** Define a one-to-many dependency so when one object changes state, all dependents are notified automatically.

**Structure:**

```text
StockTicker (Subject)
  - observers: Observer[]
  + subscribe(observer)
  + unsubscribe(observer)
  + setPrice(price)       ← triggers _notify()
  - _notify()             ← calls observer.update() on all observers

Observer interface
  + update(symbol, price)
  └── PriceAlertObserver
  └── PortfolioObserver
  └── ChartObserver (future Sprint — no Subject changes needed)
```

**Loose coupling benefit:** The Subject knows only that observers have an `update()` method. New observer types can be added in future Sprints without any change to the Subject.

**When to use Observer:**

- UI frameworks (model-view synchronization)
- Event systems and message buses
- Real-time data feeds and dashboards
- Any situation where one state change must propagate to an unknown number of dependents

### 4.2 Strategy

**Intent:** Define a family of algorithms, encapsulate each, and make them interchangeable.

**Structure:**

```text
DataSorter (Context)
  - strategy: SortStrategy
  + setStrategy(strategy)
  + sort(data): calls this.strategy.sort(data)

SortStrategy interface
  + sort(data): data[]
  └── BubbleSortStrategy
  └── QuickSortStrategy
  └── MergeSortStrategy (new Sprint — no Context changes needed)
```

**When to use Strategy:**

- Algorithm selection at runtime (sorting, searching, compression)
- Interchangeable business rules (tax calculation by region, pricing by customer tier)
- Payment processing (multiple payment methods behind a common interface)
- Validation strategies (different validation rules per form type)

### 4.3 Command

**Intent:** Encapsulate a request as an object, allowing it to be queued, logged, or undone.

**Structure:**

```text
Command interface
  + execute()
  + undo()
  └── InsertCommand
  └── DeleteCommand
  └── FormatCommand

CommandHistory
  - history: Command[]
  + execute(command)  ← calls command.execute(), pushes to history
  + undo()           ← pops last command, calls command.undo()
```

**When to use Command:**

- Undo/redo functionality (text editors, graphics tools, IDEs)
- Transaction management (database operations that must roll back)
- Task queuing and scheduling
- Macro recording (a sequence of commands saved and replayed)

### 4.4 Behavioral Pattern Comparison

| Pattern | Problem Solved | Key Structural Feature | Scrum Benefit |
|---------|---------------|------------------------|---------------|
| Observer | One change must notify many dependents | Subject holds a list of observers; all implement update() | New features (observers) added in future Sprints without touching Subject |
| Strategy | Algorithm must be swappable at runtime | Context holds a Strategy reference; delegates to it | New algorithms added as new Strategy classes, no Context changes |
| Command | Operations need to be reversible, queued, or logged | Command interface with execute() and undo() | Undo functionality, transaction support, and audit logging implemented consistently |

---

## Part 5: Pattern Selection Guide

### 5.1 Decision Questions

Work through these questions when deciding which pattern to apply:

1. Is the problem about creating objects? → Creational category
   - Need exactly one? → Singleton
   - Need to choose the right type? → Factory Method
   - Building something complex step-by-step? → Builder

2. Is the problem about how things connect or compose? → Structural category
   - Incompatible interfaces? → Adapter
   - Adding behavior without subclassing? → Decorator
   - Hiding complexity behind a simple interface? → Facade

3. Is the problem about how objects communicate or behave over time? → Behavioral category
   - Need to notify many things when something changes? → Observer
   - Need swappable algorithms? → Strategy
   - Need reversible or queued operations? → Command

### 5.2 Patterns and the Open/Closed Principle

Several patterns directly implement the Open/Closed Principle (open for extension, closed for modification):

| Pattern | How It Implements Open/Closed |
|---------|-------------------------------|
| Factory Method | New product types = new class + registry entry; no existing code changes |
| Observer | New event listeners = new observer class; Subject unchanged |
| Strategy | New algorithms = new Strategy class; Context unchanged |
| Decorator | New behaviors = new Decorator class; Component unchanged |

This is the core Agile benefit of design patterns: new Sprint features extend the system rather than modifying it.

---

## Part 6: Exam Tips and Scrum Connections

### PSM I Connections

| Pattern Concept | PSM I Connection |
|-----------------|-----------------|
| Agile Principle 9 | Technical excellence and good design enhance agility — the core justification for pattern adoption |
| Definition of Done | Code quality standards (including design quality) are encoded in the DoD |
| Sprint Retrospective | Right forum to surface that poor design is slowing velocity and plan refactoring work |
| Sprint Backlog | Refactoring to patterns is legitimate Sprint work when it enables feature delivery |

### Common Exam Traps

- Confusing Adapter (interface bridge) with Facade (complexity simplifier) — they both wrap things but for different reasons
- Confusing Observer (event notification) with Strategy (algorithm swapping) — both use interfaces but solve completely different problems
- Thinking Singleton is always a good idea — it creates testing problems and should be used only for genuinely shared resources
- Stating that design pattern work doesn't belong in Sprints — it does, when connected to business value

---

## Key Terms

| Term | Definition |
|------|-----------|
| Design pattern | A reusable solution to a commonly recurring software design problem |
| Gang of Four | The four authors (Gamma, Helm, Johnson, Vlissides) who catalogued the 23 foundational OO design patterns |
| Creational pattern | Pattern category addressing how objects are created and instantiated |
| Structural pattern | Pattern category addressing how classes and objects compose into larger structures |
| Behavioral pattern | Pattern category addressing how objects communicate and distribute responsibility |
| Singleton | Pattern ensuring a class has exactly one instance with a global access point |
| Factory Method | Pattern delegating object creation to subclasses or a factory function |
| Builder | Pattern assembling complex objects step-by-step using method chaining |
| Adapter | Pattern converting one interface into another expected by clients |
| Decorator | Pattern adding behaviors to objects dynamically without subclassing |
| Facade | Pattern providing a simplified interface to a complex subsystem |
| Observer | Pattern notifying multiple dependents automatically when a subject's state changes |
| Strategy | Pattern making algorithms interchangeable at runtime |
| Command | Pattern encapsulating requests as objects supporting undo and queuing |
| Open/Closed Principle | Design principle: classes should be open for extension but closed for modification |

---

## Supplemental Resources

The following free, open-access resources go deeper on Module 12 topics:

**1. "Refactoring.Guru — Design Patterns" — Alexander Shvets**
<https://refactoring.guru/design-patterns>
A comprehensive free reference for all 23 Gang of Four design patterns with UML diagrams, pseudocode, and real-world analogies. The site organizes patterns by category and includes a pattern comparison tool. Particularly strong on Builder, Command, and Observer with step-by-step structural explanations.

**2. "Design Patterns: Elements of Reusable Object-Oriented Software" — Summary (O'Reilly)**
<https://www.oreilly.com/library/view/design-patterns-elements/0201633612/>
The original Gang of Four book table of contents and sample chapters are freely accessible via O'Reilly's preview. The introduction and pattern catalog overview give the full context for why patterns were catalogued and how to apply them in practice.

**3. "The Command Pattern" — SourceMaking**
<https://sourcemaking.com/design_patterns/command>
A free deep dive into the Command pattern with diagrams, multiple implementation examples, and a clear explanation of how CommandHistory enables undo/redo. Particularly useful for the lab's Command implementation tasks. Covers the pattern's connection to transaction management and macro recording.
