# Reading Guide: Module 02 – Agile Manifesto and the 12 Principles

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

The Agile Manifesto is the philosophical foundation of every Agile framework, including Scrum. Written in 2001 by seventeen experienced software practitioners, it distills decades of hard-won lessons about what makes software teams succeed or fail into four concise values and twelve operational principles. The PSM I certification exam tests these values and principles directly — not as trivia, but as the reasoning framework you apply to scenario-based questions. This guide gives you the deep understanding you need.

---

## 1. Historical Context — Why 2001 Mattered

By the late 1990s, the software industry had developed a set of process frameworks — including RUP, CMM, and various ISO standards — that were designed to bring engineering rigor to software development. In practice, many of these processes had become so documentation-heavy and bureaucratic that teams spent more time managing the process than writing software. The Standish Group's CHAOS Report of 1994 had found that only 16 percent of software projects were completed on time and within budget — a damning indictment of the status quo.

Meanwhile, a set of practitioners were independently developing lighter-weight methods — Kent Beck's Extreme Programming (XP), Ken Schwaber and Jeff Sutherland's Scrum, Alistair Cockburn's Crystal methods, and others. These methods shared a common intuition: software development is a creative, collaborative activity that cannot be reduced to a predictable manufacturing process. They arranged a meeting at the Snowbird ski resort in Utah in February 2001 and produced the Agile Manifesto.

The seventeen signatories were not revolutionaries — they were experienced, pragmatic practitioners who had observed what actually works in software teams. The Manifesto is empirical in the best sense: it reflects observed reality, not ideological preference.

---

## 2. The Four Values — Full Analysis

The Manifesto's core statement: "We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value..."

### Value 1: Individuals and Interactions over Processes and Tools

Meaning: The quality of a software team is determined primarily by the quality of its people and communication, not by the sophistication of its tools or the rigor of its processes. A mediocre team using excellent tools produces mediocre software. An excellent team using modest tools can produce excellent software.

In practice: When a Scrum Master sees communication problems on the team, the response is not to add more process or buy better tools — it is to facilitate better human interaction. Daily Scrums are short because they are meant to enable team synchronization, not to generate status reports for management.

Misunderstanding to avoid: This value does not say "ignore processes and tools." It says that when choosing between investing in people/communication versus investing in processes/tools, choose people.

### Value 2: Working Software over Comprehensive Documentation

Meaning: The primary deliverable of a software team is software that works — not specifications, design documents, project plans, or status reports. Documentation has value when it helps teams build, understand, or maintain software; it does not have value when it exists to satisfy a process requirement that nobody actually uses.

In practice: In Scrum, the Definition of Done ensures that each Sprint produces a genuine increment of working, tested software — not partially built features or documentation about features that will be built later.

Misunderstanding to avoid: This value does not prohibit documentation. The Scrum Guide itself requires a Product Backlog (written), Sprint Backlog (written), and Increment (demonstrated). What it prohibits is treating documentation as a substitute for working software.

### Value 3: Customer Collaboration over Contract Negotiation

Meaning: The relationship between a software team and its customer should be collaborative — both parties working together toward a shared goal — rather than adversarial, where the contract defines what is owed and disputes are won by lawyering.

In practice: The Product Owner role in Scrum is the organizational expression of this value. The Product Owner is not a requirements clerk — they are an active collaborator who continuously negotiates value, priorities, and trade-offs with the Developers and stakeholders.

Misunderstanding to avoid: This value does not say "never write contracts." It says that within a contractual relationship, both parties should collaborate rather than fight. Many organizations use Agile-friendly contract structures (time-and-materials, not fixed-price-fixed-scope) to support this value.

### Value 4: Responding to Change over Following a Plan

Meaning: Plans are valuable as current best thinking, but new information should cause plans to change. The cost of following an outdated plan is higher than the cost of updating the plan. Agile teams treat their plans as hypotheses to be tested, not commitments to be honored regardless of new evidence.

In practice: The Product Backlog is never "frozen." Sprint Planning produces a Sprint Goal and Sprint Backlog, but if during the Sprint the team learns something that makes the Sprint Goal obsolete, the Sprint can be cancelled and a new Sprint started. Product Backlog refinement happens continuously.

Misunderstanding to avoid: This value does not say "plans are useless" or "we never plan." Sprint Planning, Release Planning, and Quarterly Planning are all legitimate Agile activities. What this value prohibits is treating plans as immutable once written.

---

## 3. The 12 Principles — Reference Table

| No. | Principle (paraphrased) | PSM I Relevance |
|---|---|---|
| 1 | Highest priority: satisfy customer through early and continuous delivery of valuable software | Justifies short Sprints and the Sprint Goal |
| 2 | Welcome changing requirements, even late in development | Justifies dynamic Product Backlog management |
| 3 | Deliver working software frequently; prefer shorter timescales | Sets the Sprint cadence expectation |
| 4 | Business and developers work together daily | Justifies the Daily Scrum and PO availability |
| 5 | Build around motivated individuals; trust them | Justifies self-managing teams and servant leadership |
| 6 | Face-to-face conversation is most efficient | Justifies co-located teams and real-time collaboration |
| 7 | Working software is the primary measure of progress | Justifies the Increment and Definition of Done |
| 8 | Agile promotes sustainable development at constant pace | Justifies protection from unreasonable overtime demands |
| 9 | Continuous attention to technical excellence enhances agility | Justifies refactoring, clean code, and Definition of Done quality standards |
| 10 | Simplicity — maximize work not done — is essential | Justifies saying no to scope creep and gold-plating |
| 11 | Best architectures emerge from self-organizing teams | Justifies no prescribed technical roles within Scrum team |
| 12 | Teams reflect regularly and tune their behavior | Directly justifies the Sprint Retrospective |

---

## 4. Mapping Manifesto Principles to Scrum Events

Every Scrum event can be traced back to one or more Manifesto principles:

| Scrum Event | Primary Principles |
|---|---|
| Sprint (the container) | 1, 3 — continuous, frequent delivery |
| Sprint Planning | 1, 5 — team-driven commitment to valuable work |
| Daily Scrum | 4, 6 — daily collaboration and face-to-face sync |
| Sprint Review | 1, 7 — demonstrate working software to stakeholders |
| Sprint Retrospective | 12 — regular reflection and adaptation |

Understanding this mapping allows you to answer "why does Scrum do X?" questions from first principles, which is exactly how PSM I scenario questions are framed.

---

## 5. Common Manifesto Misinterpretations

Misinterpretation 1: "Agile means no documentation." The Manifesto says working software is valued over comprehensive documentation, not instead of all documentation. The Scrum Guide requires several written artifacts.

Misinterpretation 2: "Agile means no planning." Agile teams plan constantly — Sprint Planning, backlog refinement, release planning. The difference is that plans are treated as adaptive, not contractual.

Misinterpretation 3: "Agile means the customer can change everything anytime." Scrum protects Sprint integrity. Changes to the current Sprint require a conversation between the Product Owner and Developers, and in extreme cases can cause a Sprint cancellation. Random scope injection into a running Sprint is not Agile — it is chaos.

Misinterpretation 4: "Agile means no processes." Value 1 says individuals and interactions over processes and tools — not no processes. Scrum itself is a process framework. The principle is that people and communication take priority when the two conflict.

---

## 6. The Manifesto's Self-Description — "Uncovering Better Ways"

The opening phrase of the Manifesto — "We are uncovering better ways of developing software by doing it and helping others do it" — is itself significant. The word "uncovering" implies empiricism: you discover truth through experience, not through reasoning from first principles. This is the same epistemological commitment that underlies Scrum's empirical pillars of Transparency, Inspection, and Adaptation.

The Manifesto authors did not claim to have invented a complete, final answer. They claimed to be engaged in an ongoing discovery process. This is why Agile frameworks continue to evolve — Scrum has been revised, XP has been updated, new frameworks have emerged. The Manifesto is a living philosophical commitment, not a closed specification.

---

## 7. PSM I Exam Tips

Tip 1: Memorize all four Agile Manifesto values with exact "over" language. The exam will present slight misquotations as wrong answers. For example, "documentation over working software" is incorrect (the values are reversed); "working software over all documentation" is incorrect (the Manifesto says "comprehensive documentation," not "all documentation").

Tip 2: The twelve principles are not numbered or labeled by the Manifesto itself — they are presented as a continuous list. On the PSM I exam, they will be referenced by content, not number. Study them by meaning, not by memorizing position.

Tip 3: When a PSM I question describes a team ignoring customer feedback because it contradicts the documented requirements, this violates Value 3 (customer collaboration over contract negotiation) and Principle 2 (welcome changing requirements).

Tip 4: When a PSM I question describes a team working overtime consistently to meet deadlines, this violates Principle 8 (sustainable pace). The Scrum Master should address this, not celebrate it.

Tip 5: Principle 11 (best architectures emerge from self-organizing teams) is why Scrum assigns no specific technical roles within the Developer accountability. The team decides how to organize its technical work.

Tip 6: Principle 10 (simplicity — maximize work not done) is the Manifesto's expression of the Lean concept of waste elimination. This principle connects Module 02 directly to Module 09 (Kanban and Lean Principles).

Tip 7: PSM I questions sometimes describe a Scrum Master who is enforcing Agile practices rigidly even when they are not helping. This violates Value 1 (individuals and interactions over processes) and Principle 5 (trust motivated individuals). Scrum is a framework that enables inspection and adaptation — including adaptation of the process itself.

Tip 8: The Manifesto was written specifically about software development. The Scrum Guide notes that Scrum has been used beyond software. PSM I questions focus on software contexts, but the principles apply more broadly.

---

## 8. Study Checklist

- [ ] Write out all four Agile Manifesto values from memory, including the "over" language and the closing sentence about items on the right
- [ ] For each value, write one concrete example of a team behavior that embodies it and one that violates it
- [ ] Write a one-sentence plain-language summary of each of the 12 Principles
- [ ] Complete the Manifesto-to-Scrum event mapping table from memory
- [ ] Identify which principle(s) justify each of the five Scrum events
- [ ] Explain the three most common Manifesto misinterpretations in your own words
- [ ] Read the Agile Manifesto (both values and principles) at the official source referenced in the Scrum Guide
- [ ] Complete this module's Quiz and Discussion Forum

---
