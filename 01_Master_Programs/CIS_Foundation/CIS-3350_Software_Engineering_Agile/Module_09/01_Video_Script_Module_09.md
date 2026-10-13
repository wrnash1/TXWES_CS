# Video Script: Module 09 – Kanban and Lean Principles

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Estimated Duration:** 20 minutes

**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Kanban board should be shown as a physical or digital board with columns and WIP limits labeled

---

## Section 1 — Welcome and Agile's Broader Family [00:00–03:00]

"Welcome to Module 9. So far in this course we have spent most of our time inside the Scrum framework. Today we step back and look at the broader Agile family — specifically Kanban and the Lean principles from which it draws.

Understanding Kanban and Lean serves you in two ways. First, many teams use Kanban alongside or instead of Scrum, so understanding it makes you a more versatile practitioner. Second, the PSM I exam includes questions about how Scrum compares to other Agile approaches, and Kanban is the most common comparison.

By the end of this module you will be able to:

- Explain Lean's five principles and their origin in the Toyota Production System
- Define Kanban and describe its four core practices
- Explain what WIP limits are and why they improve flow
- Compare and contrast Scrum and Kanban across key dimensions
- Describe Scrumban as a hybrid approach
- Explain Lean waste categories and connect them to software development waste"

---

## Section 2 — Lean Principles: The Foundation [03:00–09:00]

"Kanban is rooted in Lean thinking, which itself comes from the Toyota Production System developed by Taiichi Ohno and Shigeo Shingo at Toyota in the 1950s and 60s.

[SHOW DIAGRAM: Toyota Production System diagram showing Just-in-Time production, pull systems, and waste elimination as pillars]

Lean was adapted for software development by Mary and Tom Poppendieck in their 2003 book 'Lean Software Development.' They translated Toyota's manufacturing principles into software terms.

Lean has five core principles:

Principle 1 — Identify value: Define what is valuable from the customer's perspective. Everything else is potentially waste. In software, value is a working feature that serves a real user need.

Principle 2 — Map the value stream: Understand the entire flow of work from idea to working software in production. Value stream mapping visualizes every step in the process and identifies which steps add value and which create delays.

Principle 3 — Create flow: Eliminate delays, handoffs, and interruptions so that work flows continuously from start to finish. Batching work (building many features simultaneously without releasing any) creates queues that destroy flow.

Principle 4 — Establish pull: Work is pulled into the system only when there is capacity to handle it, not pushed in by a schedule or manager. This prevents overloading and the queuing problems that come with it.

Principle 5 — Seek perfection: Continuously improve. The five principles are not a one-time exercise — they are a continuous cycle of inspection and improvement.

PSM I Exam Tip: Lean's principle of 'pull' maps directly to Scrum's Sprint Planning, where Developers pull work from the Product Backlog rather than having work pushed onto them by managers. This is why Scrum is described as a pull system.

Lean also defines seven categories of waste — called muda in Japanese — that apply directly to software:

Partially done work (code written but not integrated or tested), extra features (building things users did not ask for), relearning (solving the same problem twice because knowledge was not retained), handoffs (passing work between teams or individuals), delays (waiting for approvals, reviews, or dependencies), task switching (working on multiple things at once reduces all of them), and defects (bugs that require rework).

[SHOW DIAGRAM: Seven wastes of Lean mapped to software examples — each waste labeled with a manufacturing analogy and a software analogy]

The PSM I exam connects Lean waste to Agile Manifesto Principle 10 — 'Simplicity — the art of maximizing the amount of work not done — is essential.' Both are about eliminating waste."

---

## Section 3 — Kanban: Core Practices [09:00–15:00]

"Kanban is a method for managing knowledge work that emphasizes visualizing work, limiting work in progress, managing flow, and making process policies explicit.

[SHOW DIAGRAM: Kanban board with columns: Backlog, In Analysis, In Development, In Testing, Done — each column with WIP limit numbers in brackets]

Kanban was adapted for software by David Anderson in the early 2000s at Microsoft and later formalized in his 2010 book. Kanban does not prescribe roles, events, or cadences — it is a method for improving an existing process rather than a framework for replacing it.

The four core Kanban practices:

Practice 1 — Visualize the workflow: Create a board that shows every step in the work process as a column. Each work item is represented as a card moving through the columns from left to right. Visualization makes invisible problems visible: queues, blockers, and bottlenecks all become apparent on a Kanban board.

Practice 2 — Limit Work in Progress (WIP): Assign a maximum number of items allowed in each column at any time. This is the defining practice of Kanban — the WIP limit.

Why do WIP limits improve performance? When there are too many items in progress simultaneously, context-switching costs accumulate, work queues build up, and items take longer to move from start to finish. Limiting WIP forces the team to finish existing work before starting new work, which reduces cycle time and improves quality.

[SHOW DIAGRAM: Little's Law visualization — Average Cycle Time = WIP / Throughput — showing how reducing WIP with same throughput reduces cycle time]

Practice 3 — Manage flow: Monitor how work items move through the board. Common flow metrics include cycle time (how long from work started to work done), throughput (how many items completed per week), and lead time (how long from request made to work done).

Practice 4 — Make policies explicit: Document the rules for how work moves through the board. What does it mean for a card to be 'ready for development'? When can a card move to 'in testing'? Explicit policies prevent confusion and create consistent behavior.

PSM I Exam Tip: Kanban does not have fixed Sprints, mandatory retrospectives, or prescribed roles. PSM I questions that ask about Scrum-specific elements — Sprints, Sprint Goals, Sprint Backlogs — are not asking about Kanban. Know which practices belong to which framework."

---

## Section 4 — Scrum vs. Kanban: Key Comparisons [15:00–18:30]

"Let me compare Scrum and Kanban directly on the dimensions that appear in PSM I questions.

[SHOW DIAGRAM: Side-by-side comparison table — Scrum vs. Kanban across: cadence, roles, planning, WIP management, output commitment, change management]

Cadence: Scrum uses fixed-length Sprints (1–4 weeks). Kanban has no prescribed cadence; work flows continuously.

Roles: Scrum has three defined accountabilities (Product Owner, Scrum Master, Developers). Kanban prescribes no roles.

Iteration commitment: Scrum teams commit to a Sprint Goal. Kanban teams have no Sprint Goal — they pull and complete individual items.

WIP management: Scrum limits WIP implicitly through Sprint length and Sprint Planning. Kanban limits WIP explicitly with WIP limits on board columns.

Changes: In Scrum, new items cannot be added to the current Sprint without affecting the Sprint Goal. In Kanban, new items can be pulled into the process at any time, as long as WIP limits permit.

Output measurement: Scrum uses velocity (story points per Sprint). Kanban uses throughput (items per week) and cycle time (days per item).

When to use each: Scrum works best for product development teams with evolving feature sets and a need for regular stakeholder feedback. Kanban works best for teams with continuous, unpredictable incoming work — like operations, support, or maintenance teams.

PSM I Exam Tip: Scrum and Kanban are complementary, not mutually exclusive. Many teams use Kanban practices within a Scrum framework — this hybrid approach is called Scrumban."

---

## Section 5 — Scrumban and Closing [18:30–20:00]

"Scrumban is an informal term for teams that combine Scrum's structure with Kanban's flow-based practices. A Scrumban team might:

[SHOW DIAGRAM: Scrumban board showing a Sprint Backlog as a Kanban board with WIP limits on Development and Testing columns]

- Run Sprints but use a Kanban board within the Sprint to visualize and limit WIP
- Use Kanban metrics (cycle time, throughput) alongside Scrum metrics (velocity, burndown)
- Hold Scrum events (Daily Scrum, Retrospective) while managing flow with Kanban WIP limits

Scrumban is not an official Scrum.org framework — it is a practical hybrid that teams evolve over time. The Scrum Guide does not mention Kanban or Scrumban, but the Scrum Guide explicitly says Scrum is a framework within which teams can employ various processes and techniques.

PSM I Exam Tip: The PSM I exam tests Scrum. Questions about Kanban test your ability to distinguish Kanban practices from Scrum practices and to recognize that Scrum does not require teams to avoid Kanban tools or techniques.

In Module 10 we move to requirements engineering and use cases — the more traditional software requirements practices that Agile teams have largely replaced with user stories, but which remain important for understanding the full spectrum of software engineering practice. See you there."

---

## End Card

- Next module: Module 10 – Requirements Engineering and Use Cases
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
