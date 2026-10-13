# Lab Activity: Module 11 – Software Design Patterns

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Points:** 100

---

## Overview

This lab is a design pattern analysis and application exercise. You will identify patterns in existing scenarios, evaluate the technical consequences of design decisions, and connect design quality to Scrum team performance. No running code is required — this is a written analysis lab.

Estimated time: 90–120 minutes

---

## Part 1 — Pattern Identification (30 points)

### Part 1 Instructions

Read each of the following four system descriptions. For each description:

- Identify which Gang of Four design pattern (if any) is being described or implied
- Name the pattern category (Creational, Structural, or Behavioral)
- Write two to three sentences explaining what structural or behavioral clue led you to your identification

Scenario 1: The PaymentService class in an e-commerce application holds a reference to a PaymentProcessor interface. At runtime, the application injects either a CreditCardProcessor, PayPalProcessor, or BankTransferProcessor depending on the user's selection at checkout. The PaymentService code never contains an if/else block to select which processor to use — it simply calls `paymentProcessor.processPayment(amount)`.

Scenario 2: A news application has a NewsSource class that maintains a list of registered objects. Whenever new articles are published, the NewsSource iterates through the list and calls `onNewArticle(article)` on each registered object. Mobile apps, web browsers, and email digest services all register with the NewsSource without the NewsSource knowing anything about them.

Scenario 3: The DatabaseConfig class in a server application has a private constructor and a static method `getInstance()`. The first call to `getInstance()` creates a DatabaseConfig object and stores it in a private static variable. All subsequent calls return the same stored object. The class manages connection strings, timeout settings, and pool sizes for the entire application.

Scenario 4: A legacy reporting system generates reports in an old XML format with a method `generateXmlReport()`. A new analytics dashboard expects a method signature `exportData(format, destination)`. A developer creates a ReportAdapter class that wraps the legacy system and exposes `exportData()` — internally it calls `generateXmlReport()` and transforms the output to the expected format and destination.

---

### Part 1 Grading (30 points)

- Each scenario: 7.5 pts (correct pattern identification 4, correct category 1.5, identification reasoning 2)

---

## Part 2 — Anti-Pattern Analysis (35 points)

### Part 2 Instructions

Read the following scenario and complete the three tasks below.

### The ProjectManager Class

The CampusTech development team has a single class called ProjectManager that currently:

- Handles user authentication and session management
- Reads and writes project data to the database
- Sends email notifications to project stakeholders
- Generates PDF and Excel reports
- Validates all form input from the user interface
- Logs all system events to a file
- Calculates project health scores based on milestone data

The class is 3,400 lines long. Any Sprint that involves email changes, database schema updates, report formatting, or authentication modifications requires changes to ProjectManager. The team's Sprint velocity has dropped from 40 story points to 18 over six Sprints.

Task A — Anti-pattern diagnosis (10 points): Identify which anti-pattern the ProjectManager class represents. Explain in 100–150 words how this anti-pattern is causing the velocity drop. Reference at least two specific technical consequences (coupling, testability, merge conflicts, or understanding complexity).

Task B — Decomposition plan (15 points): Propose a decomposition of the ProjectManager class into separate, single-responsibility classes. For each new class you propose:

- Name the class
- State its single responsibility
- Identify one design pattern from this module that could help manage the relationship between the new class and the rest of the system (you may use different patterns for different classes or the same pattern for multiple)

You must propose at least four new classes.

Task C — Sprint communication (10 points): Write a 100–150 word message from the Scrum Master to the Product Owner explaining why the team needs Sprint capacity to refactor the ProjectManager class. The message should:

- Connect the technical problem to a business outcome (velocity, reliability, or time to market)
- Avoid overly technical language
- Not use any Scrum jargon beyond "Sprint" and "velocity"

---

### Part 2 Grading (35 points)

- Task A — Anti-pattern diagnosis with technical reasoning: 10 pts (correct identification 3, technical consequence explanation 7)
- Task B — Decomposition plan (4+ classes): 15 pts (correct single responsibility 6, pattern application 6, completeness 3)
- Task C — Stakeholder communication: 10 pts (business connection 5, clarity and tone 3, avoids technical jargon 2)

---

## Part 3 — Pattern Application (35 points)

### Part 3 Instructions

Read the following two feature requests and complete the design tasks below.

Feature Request 1: The CampusTech application needs to add a notification system. When a project's status changes to "At Risk," the following should be notified: the project manager's email, the team's Slack channel, the dashboard's status indicator, and the executive summary report. In the future, additional notification channels may be added.

Feature Request 2: The application currently supports only one type of project export (CSV). The product owner wants to add PDF export and JSON export. New export formats may be requested in future Sprints. The current code has a 150-line method with if/else blocks for format selection scattered throughout five different service classes.

Task A — Feature 1 design (15 points): Design the Observer pattern implementation for the notification system. Your design must include:

- The Subject class name and its responsibilities
- At least three Observer class names and what each one does when notified
- A description of how a new notification channel would be added in a future Sprint (one sentence)
- One sentence explaining how this design supports Agile Principle 9

Task B — Feature 2 design (10 points): Design the Strategy pattern implementation for the export system. Your design must include:

- The Strategy interface name and the method signature it declares
- At least three Concrete Strategy class names and what each one does
- A description of how a new export format would be added in a future Sprint (one sentence)
- One sentence connecting this design to the reduction of technical debt

Task C — Pattern comparison (10 points): Write a 100–150 word comparison of Observer and Strategy. Address: what problem each pattern solves, what structural element they share (hint: both rely on a common interface), and under what circumstances you would choose one over the other on a Scrum team.

---

### Part 3 Grading (35 points)

- Task A — Observer design completeness: 15 pts (subject/observer roles clear 6, extensibility description 4, Agile connection 5)
- Task B — Strategy design completeness: 10 pts (interface + strategies clear 5, extensibility description 3, technical debt connection 2)
- Task C — Pattern comparison: 10 pts (accuracy 5, structural insight 3, contextual recommendation 2)

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Four pattern identifications with reasoning
2. Part 2: Anti-pattern diagnosis, decomposition plan, and stakeholder communication
3. Part 3: Observer design, Strategy design, and pattern comparison

Submit to the Canvas assignment portal by the module due date.

---

## Part 9 — Challenge Exercise

### Challenge 1: Pattern Catalog Design

You are a senior developer onboarding a new team member who has never encountered design patterns. Create a personal pattern reference card for the five patterns covered in this module (Singleton, Factory Method, Adapter, Decorator, Observer, Strategy — pick five):

1. For each pattern, write a one-sentence "elevator pitch" that explains what problem it solves in plain language (no technical jargon — pretend you are explaining to a non-developer product manager).
2. For each pattern, invent a real-world non-software analogy that captures its structure (e.g., Singleton = the one official timekeeping clock in a building — everyone checks the same clock).
3. For each pattern, write one "smell" — a code or design symptom that signals this pattern is needed (e.g., for Adapter: "We have two components that both work perfectly but cannot talk to each other because their interfaces don't match").
4. For each pattern, write one "misuse warning" — a situation where teams incorrectly apply this pattern and the consequence (e.g., Singleton misuse: using Singleton for objects that should actually have multiple instances, creating hidden global state).

### Challenge 2: Technical Debt Sprint Planning

The CampusTech team from Part 2 has agreed that the ProjectManager God Object must be refactored. The team has 40 story points of capacity per Sprint. The refactoring work has been estimated at 60 story points total. New feature requests from the Product Owner total 80 story points for the next three Sprints.

1. Design a three-Sprint refactoring plan that delivers both new features and incremental refactoring each Sprint. For each Sprint: list which refactoring work (from your Part 2 decomposition) will be done, which new features will be included, and the total story point allocation. Ensure each Sprint stays at or below 40 points.
2. For the first Sprint of refactoring, write a Sprint Goal that acknowledges both the refactoring work and the feature delivery — the goal should be business-facing, not purely technical.
3. The Product Owner objects: "These refactoring stories have no user-visible value. I want to order them to the bottom of the backlog." Write a two-paragraph response from the Scrum Master that explains why refactoring PBIs have indirect business value and how they should be ordered relative to features that depend on them. Reference the velocity data from the scenario (drop from 40 to 18 points).
4. After the refactoring is complete, what metric would you propose tracking over the next three Sprints to confirm that the refactoring achieved its intended business outcome? Define the metric, describe how it is measured, and state the threshold that would indicate success.

### Reflection Questions

1. The Gang of Four wrote Design Patterns in 1994 — before Agile, before cloud computing, and before modern language features like lambdas and generics. Some patterns (like Strategy) can now be implemented with a single function pointer or lambda instead of a class hierarchy. Does this make the pattern obsolete, or is the pattern still conceptually valuable even if the implementation changes? Defend your position with a specific example.
2. The God Object anti-pattern is rarely created maliciously — teams fall into it because adding to an existing class is faster than designing a new one. This is an example of short-term thinking creating long-term technical debt. Identify two other software development shortcuts that follow the same pattern: fast now, painful later. For each, describe the short-term benefit, the long-term cost, and the design practice that prevents it.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Pattern Identification (4 scenarios) | 30 |
| Part 2 — Anti-Pattern Analysis (Tasks A, B, C) | 35 |
| Part 3 — Pattern Application (Tasks A, B, C) | 35 |
| Total | 100 |

---
