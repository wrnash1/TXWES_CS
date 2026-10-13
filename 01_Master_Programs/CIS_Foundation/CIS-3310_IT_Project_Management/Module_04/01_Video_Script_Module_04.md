# Video Script: Module 04 – Schedule Management: Gantt Charts and CPM

**Course:** CIS-3310 IT Project Management
**Estimated Duration:** 23 minutes
**Certification Alignment:** CompTIA Project+ (PK0-005) | PMBOK 6th and 7th Editions
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

**Key exam traps to address in this lecture:**

- Lag vs. lead time — students reverse these; lag delays the successor, lead accelerates it
- Float (slack) = LS - ES or LF - EF, not a buffer added to task duration
- Critical path has ZERO float — any delay to a critical path task delays the project end date
- Crashing adds resources (increases cost); fast-tracking overlaps tasks (increases risk) — exam distinguishes these
- Milestones have zero duration — they are points in time, not tasks

**Visual aid cues:**

- [SHOW SLIDE] Sample Gantt chart for a network upgrade project
- [SHOW SLIDE] Network diagram (PDM) with forward and backward pass calculations
- [SHOW SLIDE] Critical path highlighted in red through the network diagram
- [SHOW SLIDE] Crashing vs. fast-tracking comparison table

---

## Section 1: Welcome and Module Overview [00:00 – 03:30]

Welcome back to CIS-3310. I am Professor Nash, and this is Module 04: Schedule Management. After defining what we will build in Module 03, we now focus on when we will build it.

Schedule management is one of the most calculation-intensive topics on the CompTIA Project+ exam. You will need to calculate float, find the critical path, work with lead and lag time, and understand schedule compression techniques. I will walk you through all of it step by step.

[SHOW SLIDE] Module 04 title: "Schedule Management — Gantt Charts and CPM"

Today we cover five topics: the schedule management process flow; Gantt charts; dependency types and network diagrams; the Critical Path Method with forward and backward pass calculations; and schedule compression techniques.

---

## Section 2: Schedule Management Process Flow [03:30 – 07:00]

PMI defines six processes in Schedule Management:

The first is Plan Schedule Management — developing the schedule management plan that establishes how the schedule will be created, maintained, and controlled.

The second is Define Activities — decomposing work packages from the WBS into individual schedule activities. This is where verbs appear: "Configure firewall," "Conduct user testing."

The third is Sequence Activities — identifying the logical dependencies between activities and building the network diagram.

The fourth is Estimate Activity Durations — determining how long each activity will take.

The fifth is Develop Schedule — analyzing activity sequences, durations, resource requirements, and constraints to build the project schedule model. The Schedule Baseline is the output.

The sixth is Control Schedule — monitoring schedule status, comparing to the baseline, and managing changes.

[SHOW SLIDE] Schedule management process chain diagram

---

## Section 3: Gantt Charts and Milestones [07:00 – 11:00]

[SHOW SLIDE] Sample Gantt chart for a network upgrade project

The Gantt chart is the most widely used schedule visualization tool. A Gantt chart displays project activities as horizontal bars on a timeline. The length of each bar represents the activity's duration. Dependencies between activities can be shown with connecting arrows.

Key Gantt chart elements:

Activities are shown as horizontal bars. The bar's starting position corresponds to the planned start date; the bar's ending position corresponds to the planned finish date.

Milestones are shown as diamond shapes with zero duration. A milestone marks a significant event — not work, but a point in time. Examples: "Requirements approved," "System go-live."

Dependencies link activities with arrows. An arrow from Task A to Task B means Task B depends on Task A in some way.

Summary bars group related activities into a single parent bar showing the combined timeframe.

> **Project+ Exam Tip:** Milestones have zero duration. If an exam question asks what symbol represents a milestone on a Gantt chart, the answer is a diamond. If it asks the duration of a milestone, the answer is zero.

Gantt charts are easy to read but have a limitation: they do not explicitly show which activities are critical. For that, we need the Critical Path Method.

---

## Section 4: Dependency Types, Lead, and Lag [11:00 – 15:00]

[SHOW SLIDE] Four dependency types diagram (FS, SS, FF, SF)

Activities in a schedule are connected by logical dependencies. PMI defines four dependency types.

Finish-to-Start (FS): Task B cannot start until Task A finishes. This is the most common type. Example: Testing cannot start until Development finishes.

Start-to-Start (SS): Task B cannot start until Task A starts. Both may run in parallel after A begins. Example: Documentation cannot start until Design starts.

Finish-to-Finish (FF): Task B cannot finish until Task A finishes. Both may run concurrently but B waits for A to complete. Example: User Acceptance Testing cannot finish until all defect fixes are finished.

Start-to-Finish (SF): Task B cannot finish until Task A starts. This is the rarest type — almost never used in practice.

Lead time allows a successor activity to start before its predecessor finishes. Lead accelerates the schedule. Example: Testing starts two days before Development officially finishes (Lead = -2 days).

Lag time inserts a deliberate delay after a predecessor activity finishes. Lag extends the schedule. Example: After pouring concrete, you must wait three days before tiling (Lag = +3 days).

> **Project+ Exam Tip:** Lead and lag are often tested together. Lead compresses the schedule (negative lag). Lag delays the successor (positive wait). Remember: Lag = wait; Lead = head start.

---

## Section 5: Critical Path Method — Forward and Backward Pass [15:00 – 20:30]

[SHOW SLIDE] Network diagram with forward and backward pass calculations

The Critical Path Method (CPM) is the analytical technique for determining the shortest possible project duration and identifying which activities have no scheduling flexibility.

The critical path is the longest path of dependent activities through the network diagram. Any delay to a critical path activity delays the entire project end date. Critical path activities have zero total float.

Let me walk through a simple example. Suppose we have five activities:

- Activity A: 3 days (no predecessor)
- Activity B: 4 days (depends on A)
- Activity C: 6 days (depends on A)
- Activity D: 2 days (depends on B)
- Activity E: 3 days (depends on C and D)

Path 1: A → B → D → E = 3 + 4 + 2 + 3 = 12 days
Path 2: A → C → E = 3 + 6 + 3 = 12 days

Both paths are 12 days. Both are critical paths. The project cannot be completed in less than 12 days.

[SHOW SLIDE] Forward pass calculation — Early Start and Early Finish

The forward pass moves left to right through the network to calculate Early Start (ES) and Early Finish (EF) for each activity.

ES = the earliest an activity can start, given its predecessors.
EF = ES + Duration - 1 (in day-based calculations).

The backward pass moves right to left to calculate Late Start (LS) and Late Finish (LF).

LS = LF - Duration + 1.

Total Float = LS - ES (or LF - EF). Activities on the critical path have zero total float.

Free Float = the amount an activity can be delayed without delaying the Early Start of any successor.

> **Project+ Exam Tip:** Total float belongs to the path, not just the activity. If two non-critical activities share a path, delaying one reduces the float available to the other. The exam tests this with scenario questions about delaying a non-critical task.

---

## Section 6: Schedule Compression Techniques [20:30 – 22:00]

[SHOW SLIDE] Crashing vs. fast-tracking comparison table

When the schedule needs to be shortened, the PM has two primary compression techniques.

Crashing adds resources to critical path activities to shorten their duration. More people, more machines, overtime. Effect: schedule shortens, cost increases. Risk: diminishing returns as team size grows.

Fast-tracking overlaps activities that were planned sequentially. Example: starting design work while requirements are still being finalized. Effect: schedule shortens, risk increases. Risk: rework if earlier work changes after the later work has begun.

Resource leveling adjusts the schedule to resolve resource over-allocation — it typically extends the schedule and is not a compression technique.

---

## End Card [22:00 – 23:00]

Module 04 is complete. Your assignments: complete the Reading Guide which includes a CPM reference table; complete the Lab with hands-on CPM calculation exercises; take the Quiz; and post your Discussion initial response by Wednesday.

Study resources for schedule management calculations: professormesser.com and comptia.org.

Module 05 covers Cost Management — budgeting, Earned Value Management, and the key EVM formulas. See you there.

---

## Additional Resources

- CompTIA Project+ exam objectives and study resources: comptia.org
- Free study notes and practice materials: professormesser.com
