# Discussion Forum: Module 11 — Software Design Patterns

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Overview

This discussion asks you to apply design pattern concepts to realistic professional scenarios. Write your initial post responding to one scenario, then respond substantively to at least two classmates who chose different scenarios.

---

## Professor Nash Note

Design patterns become real when you encounter the problems they solve. The best responses in this discussion will go beyond naming the pattern — they will explain what would happen without it, why a team fell into the anti-pattern in the first place, and what the Sprint-level consequences are. Think about patterns not as clever code tricks but as answers to specific recurring questions. If you find yourself asking "how do I add this feature without breaking everything else?" — there is probably a pattern for that.

---

## Scenario A: The Velocity Killer

The CampusConnect development team has been building their application for eighteen months. In the first six months, they shipped features quickly. In the last twelve months, their Sprint velocity has dropped from 38 story points to 14. When a new developer joins and tries to add a feature that sends email notifications when a project status changes to "At Risk," she discovers that email logic, status update logic, database writes, user authentication checks, and audit logging are all tangled together in a single class called ApplicationCore.java — 6,000 lines long. Her change to the email logic accidentally breaks the audit logging because they share a private helper method. The fix for the audit log breaks a database write. The Sprint ends with the feature incomplete and three regressions introduced.

The team's Scrum Master asks: "Why does every feature take longer than it should?" The senior developer answers: "Because everything touches ApplicationCore."

What anti-pattern does ApplicationCore represent? Explain in specific terms how this anti-pattern is causing the velocity decline — name at least two technical mechanisms (not just "it is too long"). Then propose which design patterns the team should apply to begin decomposing ApplicationCore, and explain how the decomposition would affect future Sprint velocity. Your post should be 175–225 words.

### Sample Response — Scenario A

ApplicationCore represents the God Object anti-pattern — a class that has absorbed responsibility for authentication, status logic, email notification, database access, audit logging, and more over eighteen months of incremental addition. The velocity decline has two distinct technical causes. First, high coupling: because email logic and audit logging share private helper methods, any change to one behavior propagates risk to the other. There is no isolation boundary — every change is a system-wide change. Second, testing drag: a developer cannot write a unit test for the new email notification without instantiating ApplicationCore in its entirety, which requires a database connection, an authentication context, and every dependency the class holds. Tests become slow, fragile, and eventually skipped.

The decomposition should apply the Strategy pattern to extract the notification logic — EmailNotificationStrategy, SlackNotificationStrategy — behind a common interface. This isolates future notification channel additions. The Observer pattern should decouple status change events from their consumers: when status changes to "At Risk," ApplicationCore publishes the event, and notification handlers, audit handlers, and reporting handlers each respond independently without knowing about each other. After decomposition, a new notification channel is a new Strategy class added in one Sprint — it does not touch status logic, audit logic, or any existing handler.

---

## Scenario B: The Pattern Debate

A Scrum team is implementing subscription status change notifications for a SaaS billing system. When a customer's subscription changes from Active to Suspended, three things must happen: the customer receives an email, the customer's access is revoked in the permissions service, and the account is flagged in the support dashboard. Two team members disagree on implementation.

The first developer argues for direct calls: the SubscriptionService method that changes status should directly call EmailService.send(), PermissionsService.revoke(), and DashboardService.flagAccount() in sequence. "It is simple, readable, and easy to trace in the debugger," he argues.

The second developer argues for the Observer pattern: SubscriptionService should publish a status change event, and EmailNotifier, PermissionsUpdater, and DashboardFlagging should each be observers that respond independently. "In six months we will have five more things that need to react to a status change," she argues.

Both developers bring the question to the Sprint Retrospective. What would you recommend, and why? Under what specific conditions would the direct-call approach be defensible? What would you tell the team about how Observer affects their ability to meet the Definition of Done in future Sprints? Your post should be 175–225 words.

### Sample Response — Scenario B

The Observer pattern is the right choice for this system given one concrete fact in the scenario: the developer predicts more consumers of the status change event within six months. The direct-call approach makes SubscriptionService responsible for knowing about — and calling — every downstream consumer. Each new consumer requires modifying SubscriptionService, which violates the Open/Closed Principle and forces regression testing of billing logic every time a downstream feature is added.

The direct-call approach is defensible in a narrow case: when the number of consumers is small, known, and stable — and when the team has explicit business reasons to guarantee the execution order of the calls. Observer does not guarantee order of observer notification; if the permissions revocation must complete before the dashboard flag is set, direct calls with explicit sequencing are easier to reason about. But that is an edge case, not the norm.

For the Definition of Done, Observer changes the meaning of "complete" for future status-change features. Adding a new observer — say, a billing adjustment handler for suspensions — is a new class that registers with the existing subject. The feature Story is smaller, the regression surface is smaller, and the test for the new observer tests only its own logic. The team can meet the Definition of Done for each new observer independently, which is exactly the kind of incremental delivery Scrum is designed for.

---

## Scenario C: The Pattern Misapplication

A junior developer on the DataSync team read about the Singleton pattern and applied it enthusiastically. She created a DataManager class as a Singleton: one instance, global access, private constructor, static getInstance() method. Initially DataManager handled only database connection pooling — the correct use case.

Over the next eight Sprints, the team kept adding to DataManager because it was globally accessible and easy to reach from anywhere in the codebase. DataManager now handles database connections, caching, API response transformation, report generation, email templating, and user session state. It is a Singleton with 4,200 lines of code.

A new developer on the team notes: "We started with a correct pattern and ended up with the God Object anti-pattern." The Scrum Master asks: "How did a correct design choice lead to an anti-pattern?"

Explain the mechanism by which the correct Singleton pattern evolved into a God Object. Then explain what design principle the team should have applied at each Sprint to prevent this drift. Finally, identify which two patterns from this module could help decompose the current DataManager — explain what each pattern would extract and why. Your post should be 175–225 words.

### Sample Response — Scenario C

The evolution from correct Singleton to God Object happened through a consistent mechanism: convenience. Because DataManager was globally accessible via getInstance(), it was the path of least resistance for every new feature that needed to share state or access central resources. The Singleton pattern solves one problem — ensuring a class has one instance. It says nothing about how large or responsible that class should be. The team conflated "globally accessible" with "the right place to put things," which is a scope problem, not a pattern problem.

The design principle the team should have applied at every Sprint is the Single Responsibility Principle: each class should have one reason to change. If DataManager is changing because of a report formatting update, a session state fix, and an email template revision in the same Sprint, it already has multiple reasons to change — the warning signal is visible if the team is looking for it.

To decompose the current DataManager, the Strategy pattern should extract the report generation logic — different report formats become interchangeable strategy classes — and the Observer pattern should be applied to any event-driven responsibilities DataManager currently handles inline. The Singleton should remain, but only for the database connection pool, which is the original and only justified use. Each extracted class is independently testable, independently deployable, and independently extensible in future Sprints.

---

## Peer Response Guidelines

Your reply to a classmate must be at least 75 words and should do at least one of the following:

- Challenge an assumption or propose a different pattern with reasoning
- Extend their argument by connecting to a specific Scrum event or artifact they did not address
- Identify a practical risk in their proposed pattern application that they did not mention
- Ask a specific follow-up question about how their proposed decomposition would affect Sprint planning or the Definition of Done

Avoid replies that simply agree or restate the classmate's argument.

---

## Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario understanding | 2 | Response accurately identifies the core anti-pattern or pattern tension in the scenario |
| Module concept application | 2 | At least two specific design patterns or principles correctly named and applied |
| Reasoning quality | 2 | Arguments acknowledge trade-offs and connect pattern choices to Sprint-level outcomes |
| Peer responses | 3 | Two substantive peer replies of 75+ words each that advance the discussion |
| Writing quality | 1 | Complete sentences, organized paragraphs, professional tone |
| **Total** | **10** | |
