# Reading Guide: Module 11 – Software Design Patterns

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3350 &BULL; SOFTWARE ENGINEERING & AGILE METHODOLOGIES</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Scrum Alliance / Agile Alliance &bull; CIS-3350 Module 11</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=LzMnsfqjzkA" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/LzMnsfqjzkA" title="Agile Software Engineering & Scrum Sprint Masterclass" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Agile Software Engineering & Scrum Sprint Masterclass</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

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

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 11 topics:

**1. "Design Patterns: Elements of Reusable Object-Oriented Software" — Gang of Four Overview (Refactoring.Guru)**
<https://refactoring.guru/design-patterns>
A comprehensive free reference for all 23 Gang of Four design patterns with diagrams, code examples in multiple languages, and real-world use cases. Covers Creational, Structural, and Behavioral categories with clear explanations of the problem each pattern solves. The site also includes an anti-pattern catalog.

**2. "Software Design Patterns" — SourceMaking**
<https://sourcemaking.com/design_patterns>
Free in-depth pattern descriptions with UML diagrams and implementation guidance. Particularly strong on showing when NOT to use a pattern — helping developers avoid over-engineering. Includes the full Gang of Four catalog plus architectural patterns.

**3. "Catalog of Refactoring" — Martin Fowler**
<https://refactoring.guru/refactoring/catalog>
A free catalog of code refactoring techniques closely related to design patterns. Covers how to move from a God Object to well-structured classes using specific named refactoring operations. Directly supports the anti-pattern decomposition work in this module.

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

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 11 – Software Design Patterns** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 11 – Software Design Patterns**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 11 – Software Design Patterns**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 11 – Software Design Patterns**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
