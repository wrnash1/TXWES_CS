# Quiz: Module 09 – Kanban and Lean Principles

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

What is the primary mechanism Kanban uses to prevent a team from taking on more work than they can handle?

* A) Sprint timeboxes that reset every two weeks
* B) Work In Progress (WIP) limits that cap the number of active items per workflow stage
* C) A Product Owner who blocks new work from entering the board
* D) Daily Scrum meetings where overloads are detected and reassigned

Correct Answer: B) WIP limits constrain how many items can be in any active workflow column simultaneously, forcing the team to finish existing work before pulling in new items.

Distractor Analysis:

* *Why B is correct:* WIP limits are the defining mechanism in Kanban for controlling flow. When a column reaches its limit, no new work enters until an item exits — creating a natural pull system.
* *Why A is incorrect:* Sprint timeboxes are a Scrum mechanism, not a Kanban one. Kanban has no timeboxed iterations; work flows continuously.
* *Why C is incorrect:* Kanban does not define a Product Owner role. While someone manages the input queue, item blocking is controlled by WIP limits, not a named role authority.
* *Why D is incorrect:* Daily Scrums are a Scrum event. Kanban has no prescribed daily meetings, though teams often hold brief daily standups by convention.

---

### Question 2

Which of the following is the most accurate definition of cycle time in Kanban?

* A) The total duration of a Scrum Sprint, from Sprint Planning to the end of the Sprint Retrospective.
* B) The elapsed time from when a work item enters active development to when it is delivered as complete.
* C) The average number of story points a team completes per Sprint over multiple Sprint periods.
* D) The time budget allocated to each column of a Kanban board before items must be escalated.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* Cycle time measures how long a specific piece of work takes from start (active work begins) to finish (delivered to the customer or end of workflow). It is a core Kanban flow metric for assessing delivery speed.
* *Why A is incorrect:* This describes a Sprint timebox — a Scrum concept. Kanban does not use timeboxed iterations.
* *Why C is incorrect:* This describes velocity — a Scrum estimation planning metric. Cycle time and velocity measure different things with different units.
* *Why D is incorrect:* Kanban does not define time budgets per column. WIP limits (count of items) constrain columns, not time.

---

### Question 3

A software team has a Kanban board where the "In Testing" column consistently contains 8–10 items while the WIP limit is 3. What does this indicate?

* A) The team is extremely productive and should increase their WIP limit to 10.
* B) There is a bottleneck in the testing stage that is slowing overall flow through the system.
* C) The Scrum Master is not attending the Daily Scrum and is failing to reassign test tasks.
* D) The Definition of Done is too strict and should be relaxed to reduce items in testing.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* When a column consistently exceeds its WIP limit, it signals a bottleneck — testing cannot keep pace with the rate of upstream development work arriving. The team should investigate and address the testing constraint.
* *Why A is incorrect:* A consistently overwhelmed column is a problem signal, not a sign of productivity. Raising the WIP limit masks the bottleneck rather than resolving it.
* *Why C is incorrect:* Kanban does not prescribe a Scrum Master role or a Daily Scrum. The issue is systemic flow, not a meeting attendance problem.
* *Why D is incorrect:* Relaxing the Definition of Done to reduce work in testing would lower quality and produce defective Increments. The bottleneck requires a capacity or process fix, not a quality compromise.

---

### Question 4

Which Lean concept most directly describes the waste created by software features that are built but never used by customers?

* A) Partially done work — work started but not yet delivered
* B) Extra features — building functionality beyond what the customer needs now
* C) Task switching — developers working on multiple items simultaneously
* D) Defects — bugs that must be found and fixed after the feature is delivered

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* "Extra features" (also called over-production in Lean manufacturing) is the waste of building functionality that customers do not need or use — consuming development capacity that could deliver actual value.
* *Why A is incorrect:* Partially done work describes items stuck mid-process that cannot yet deliver value — not features delivered but unused.
* *Why C is incorrect:* Task switching is the cognitive and productivity cost of context-switching between multiple active work items — distinct from over-building features.
* *Why D is incorrect:* Defects represent the waste of rework required to fix bugs after delivery — a quality failure, not an over-production problem.

---

### Question 5

A team currently doing Scrum wants to adopt some Kanban practices. According to the Kanban Guide for Scrum Teams (Scrum.org), which Kanban practice can be most directly added to Scrum without replacing any Scrum events or accountabilities?

* A) Replacing Sprint timeboxes with a continuous flow model and removing Sprint Planning
* B) Eliminating the Product Owner role and using a shared backlog managed by the full team
* C) Visualizing the Sprint Backlog as a Kanban board with WIP limits to improve flow within the Sprint
* D) Replacing the Sprint Retrospective with a weekly Kanban metrics review meeting

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* Visualizing Sprint Backlog work on a Kanban board and applying WIP limits within the Sprint are additive practices that improve flow without changing any Scrum events, roles, or artifacts — exactly what the Kanban Guide for Scrum Teams endorses.
* *Why A is incorrect:* Removing Sprint timeboxes and Sprint Planning dismantles core Scrum structure. This would no longer be Scrum — it would be pure Kanban.
* *Why B is incorrect:* Eliminating the Product Owner removes a core Scrum accountability defined in the Scrum Guide. This violates Scrum rules and is not endorsed by the Kanban Guide for Scrum Teams.
* *Why D is incorrect:* Replacing the Sprint Retrospective removes a prescribed Scrum event. Adding Kanban metrics should supplement Scrum practices, not replace them.
