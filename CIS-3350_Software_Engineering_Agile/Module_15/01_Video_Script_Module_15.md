# Video Script: Module 15 — Software Project Metrics and Velocity Tracking

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Estimated Duration:** 20 minutes

**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Charts should show realistic burndown examples including both ideal and actual lines

---

## Section 1 — Welcome and Why Metrics Matter in Scrum [00:00–03:00]

"Welcome to Module 15. We have covered technical practices, scaling frameworks, and process models throughout this course. Today we turn to measurement — how Scrum teams track progress, communicate status, and use data to make better decisions.

Metrics in Scrum serve the empirical process. Empiricism requires transparency, inspection, and adaptation. Metrics support all three: they make progress visible, they give the team something to inspect, and they provide evidence for decisions when adaptation is needed. But metrics also carry risk — the wrong metrics can create perverse incentives, reward the wrong behavior, and give stakeholders false confidence. Knowing which metrics to use, and how to interpret them honestly, is a genuine professional skill.

By the end of this module you will be able to:

- Define velocity and explain how it is calculated and used in Sprint planning
- Read and interpret a Sprint Burndown Chart
- Describe the Release Burndown and how it supports release planning
- Explain lead time and cycle time and connect them to flow efficiency
- Identify the most common metric anti-patterns and explain why they are harmful
- Connect metrics to the Scrum values of transparency and empiricism"

---

## Section 2 — Velocity [03:00–07:00]

"Velocity is the most commonly used metric in Scrum. Let me define it precisely and then address its most common misuses.

Velocity is the sum of story points completed by a Scrum Team during a Sprint. A team that completes five stories estimated at 3, 5, 2, 8, and 5 story points in a Sprint has a velocity of 23 for that Sprint. A team's average velocity over multiple Sprints becomes the basis for Sprint planning — if a team averages 30 points per Sprint, the team and Product Owner can plan Sprints expecting roughly 30 points of completed work.

[SHOW DIAGRAM: Velocity chart — bar chart showing Sprint velocity over 10 Sprints with a moving average line]

Velocity serves three legitimate purposes. First, Sprint planning: the team uses recent velocity to set a realistic Sprint goal. If the team averaged 28 points in the last three Sprints, planning 60 points in the next Sprint is not credible. Second, release forecasting: if the Product Backlog contains 180 story points of remaining work and the team's velocity is 30 points per Sprint, the team can forecast approximately six more Sprints to complete the backlog — subject to scope changes and estimation accuracy. Third, team trend monitoring: the team inspects their own velocity trend in Retrospectives to understand whether their productivity is improving, declining, or stable.

Velocity limitations you must understand. Velocity only measures completed work — stories that met the Definition of Done. Stories that are 90 percent done at Sprint end contribute zero to velocity. This is intentional: partial work has not delivered value. Velocity is not a measure of a developer's effort, skill, or productivity. It is a team-level forecasting tool.

[SHOW DIAGRAM: Velocity misuse — two teams compared on velocity; explanation that story points are relative to the team, not universal]

PSM I Exam Tip: Velocity is team-specific and cannot be compared across teams. A team with velocity 30 is not necessarily more productive than a team with velocity 20. Teams calibrate their own estimates — story points mean different things to different teams."

---

## Section 3 — Burndown Charts [07:00–12:00]

"Burndown charts are the visual representation of remaining work over time. They answer a simple question: are we on track?

[SHOW DIAGRAM: Sprint Burndown Chart — x-axis is Sprint days, y-axis is story points remaining; ideal line descends diagonally; actual line shows realistic variation]

The Sprint Burndown Chart plots remaining story points against Sprint days. The ideal line starts at the Sprint's total planned points and reaches zero at Sprint end. The actual line shows how remaining work is actually declining — or not — each day. Deviations tell stories.

If the actual line is above the ideal line, the team is falling behind. If it drops sharply in the last two days of the Sprint, work was batched rather than completed continuously. If it drops below the ideal line early, the team may have over-estimated or the Sprint scope was reduced.

[SHOW DIAGRAM: Common burndown patterns — flat then sharp drop (batching), consistently above ideal (overcommitment), smooth decline below ideal (undercommitment)]

The Sprint Burndown is a transparency tool for the team. It is inspected daily — ideally at the Daily Scrum — so the team can adapt if they are falling behind. If the burndown shows the team will not complete the Sprint Backlog, they can renegotiate scope with the Product Owner during the Sprint. This is the empirical process working correctly.

[SHOW DIAGRAM: Release Burndown — x-axis is Sprints, y-axis is remaining backlog points; shows adding and removing scope over multiple Sprints]

The Release Burndown Chart operates at a larger scale. It plots remaining Product Backlog points across multiple Sprints. New stories being added to the backlog during the release raise the line; completed work lowers it. The Release Burndown communicates release forecast to stakeholders — if the remaining backlog is not declining at the pace needed to reach a target release date, the Product Owner must reduce scope, extend the timeline, or add capacity.

PSM I Exam Tip: The Sprint Burndown and Release Burndown are both transparency tools. They make the team's progress and the product's remaining work visible — supporting the inspect and adapt cycle. They are not report cards for management; they are team tools for self-management."

---

## Section 4 — Flow Metrics: Lead Time and Cycle Time [12:00–16:00]

"Beyond velocity and burndown, Agile teams increasingly use flow metrics — measures of how efficiently work moves through the development process.

[SHOW DIAGRAM: Flow metric definitions — Lead Time and Cycle Time shown on a timeline from request to delivery]

Lead time is the total elapsed time from when a work item is requested (added to the backlog) to when it is delivered (released to production or accepted as done). Lead time measures the customer's experience of how long it takes for their request to become reality.

Cycle time is the elapsed time from when a team begins actively working on an item to when it is done. Cycle time excludes the waiting time while the item sits in the backlog before work starts. Cycle time measures the team's execution efficiency on work that is in progress.

The gap between lead time and cycle time is queue time — the time an item spent waiting to be picked up. A large queue time gap means the team has more work in the queue than it can process. This is a flow efficiency problem.

[SHOW DIAGRAM: Cumulative Flow Diagram — stacked area chart showing items in each stage (Backlog, In Progress, Testing, Done) over time; widening bands indicate bottlenecks]

The Cumulative Flow Diagram is the primary flow visualization. It shows how many items are in each stage of the workflow over time. A widening band in one stage — say, Testing — indicates a bottleneck: work is arriving into Testing faster than it is leaving. The CFD makes bottlenecks visible before they become Sprint failures.

Little's Law is the mathematical relationship connecting these metrics: Average Cycle Time equals Work in Progress divided by Throughput. This is why Kanban teams apply WIP limits — reducing WIP reduces cycle time, which improves flow. Scrum teams can apply the same insight: maintaining a reasonably sized Sprint Backlog prevents the individual story cycle times from extending across the entire Sprint."

---

## Section 5 — Metric Anti-Patterns and Closing [16:00–20:00]

"Before I close, I want to address the most dangerous metric anti-patterns. Good metrics serve the team. Anti-pattern metrics serve appearances and harm actual performance.

Anti-pattern 1: Comparing velocity across teams. Velocity is calibrated to a team's own estimation scale. Using velocity to rank teams, allocate resources, or justify headcount decisions creates an incentive to inflate estimates. Teams learn to game the metric rather than improve the work.

Anti-pattern 2: Using velocity as a management target. 'The team's velocity should be 50 by next quarter' is a management pressure, not a team goal. When velocity is a management target, teams inflate estimates to hit the number. The metric moves; the work does not.

Anti-pattern 3: 100 percent utilization pressure. Managing for maximum utilization — having every developer busy every hour — eliminates the slack that enables quality, learning, and collaboration. Fully utilized teams have no capacity to address unexpected problems, mentor new members, or improve their practices.

Anti-pattern 4: Lines of code or commits as productivity metrics. These measure activity, not outcomes. A refactoring that removes 500 lines of code improves the codebase but registers as negative productivity in a lines-of-code metric.

[SHOW DIAGRAM: The metric anti-pattern chain — management sets velocity target → team inflates estimates → velocity number increases → actual delivered value flat → management confused]

PSM I Exam Tip: The Scrum Guide does not prescribe specific metrics. It prescribes empiricism. When exam questions describe metrics being used to evaluate individual performance, compare teams, or pressure teams toward targets, the underlying principle being violated is empiricism — the metric has become a management instrument instead of a transparency tool.

In Module 16, our final module, we will prepare for the PSM I exam itself — reviewing the exam format, the most frequently tested concepts, and how to approach certification with confidence. See you there."

---

## End Card

- Next module: Module 16 – Final Exam Prep and PSM I Certification
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
