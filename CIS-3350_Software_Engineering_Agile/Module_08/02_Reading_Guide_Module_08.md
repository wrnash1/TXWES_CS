# Reading Guide: Module 08 – Estimation: Story Points and Planning Poker

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Introduction

Welcome to **Module 08 – Estimation: Story Points and Planning Poker**! Estimation is one of the most practical skills in Agile and Scrum, and it is regularly tested on the PSM I through scenario questions about how teams should forecast Sprint capacity and backlog item size.

This module covers relative estimation using story points, the Fibonacci scale, and Planning Poker — the most widely used consensus-based estimation technique. The key insight is that Agile estimation is about *relative size and complexity*, not about committing to a specific number of hours. This distinction drives the entire approach.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Story points:** A unit of relative estimation used to express the overall size of a user story in terms of effort, complexity, and uncertainty — not hours. Because story points are relative, the same team is consistent across estimates even if their absolute effort varies. Story points are not comparable across different teams.

* **Planning Poker:** A consensus-based estimation technique where each Developer independently selects a card representing their estimate, all cards are revealed simultaneously, and the team discusses outliers until consensus is reached. The simultaneous reveal prevents anchoring bias — the tendency to be influenced by hearing someone else's estimate first.

* **Fibonacci sequence in estimation:** Story point scales typically use a modified Fibonacci sequence (1, 2, 3, 5, 8, 13, 20, 40, 100) rather than a linear scale, because the gaps between numbers grow as stories grow larger — reflecting the increasing uncertainty in estimating bigger items. A 13-point story has more uncertainty relative to an 8-point story than a 2-point story has relative to a 1-point story.

* **Velocity:** The average number of story points a Scrum Team completes per Sprint over recent Sprints. Velocity is a planning tool — used by the team to forecast what they can take on in future Sprints. It is not a performance metric and should not be compared across teams or used by management to rank teams.

* **Relative estimation:** The practice of sizing backlog items in relation to each other rather than in absolute time units. For example, a story rated 8 points is roughly twice the size of a 4-point story for this team, even if the 4-point story takes 2 days and the 8-point story takes 5 days in reality. The ratio matters more than the absolute number.

---

### 2. Certification Exam Tips

* **PSM I Focus — Story points are not hours:** Questions that ask whether story points should be converted to hours or used to measure individual Developer productivity are testing this principle. Story points measure relative complexity for the team — they are not a time commitment and should not be used to evaluate individuals.
* **Scenario Trap — Velocity as a performance standard:** A common trap presents management using velocity to compare two teams or reward the highest-velocity team. This misuses velocity. Velocity is a planning tool internal to the team, not a cross-team performance benchmark.
* **Planning Poker and anchoring:** PSM I questions sometimes describe a scenario where the senior Developer announces their estimate before the team votes. This introduces anchoring bias and defeats the purpose of Planning Poker. Cards must be revealed simultaneously.
* **Estimates belong to the Developers:** Only the people doing the work estimate the work. The Product Owner can provide clarification but does not set or override story point estimates. The Scrum Master facilitates but does not estimate.
* **Study Resource:** [The Scrum Guide (2020)](https://scrumguides.org/) does not cover story points or Planning Poker specifically — these are complementary practices. Supplement with the [Agile Alliance glossary on story points](https://www.agilealliance.org/glossary/story-points/) and [Mike Cohn's Planning Poker guide](https://www.mountaingoatsoftware.com/agile/planning-poker).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** [Story Points — Agile Alliance Glossary](https://www.agilealliance.org/glossary/story-points/) — free overview of relative estimation, the origins of story points, and common misuses. Also read [Planning Poker — Mountain Goat Software](https://www.mountaingoatsoftware.com/agile/planning-poker).
* **Required Video:** [Story Points and Velocity Explained – Agile Coach](https://www.youtube.com/watch?v=VsSaolMtkKU) — practical walkthrough of Planning Poker, Fibonacci scale selection, and how to use velocity for Sprint forecasting. (~10 min)

---

### Lab & Command Integration

In this week's hands-on lab, you will:

* **Run a Planning Poker session:** Using a provided set of five user stories and a reference story rated at 5 points, conduct Planning Poker — assign individual estimates, identify outliers, discuss, and reach consensus on each story's point value.
* **Calculate team velocity:** Given three Sprints of completed story point totals, calculate the team's average velocity and use it to forecast how many items from a provided backlog can be committed to in the next Sprint.
* **Identify estimation anti-patterns:** Review three provided estimation scenarios and identify which anti-pattern each represents (anchoring, individual performance tracking, cross-team velocity comparison), and state how each should be corrected.

---

### 3. Study Checklist

* [ ] Read the Agile Alliance glossary entries on story points and Planning Poker.
* [ ] Be able to explain why story points use a Fibonacci scale rather than a linear 1–10 scale.
* [ ] Understand that velocity is a planning tool, not a performance metric.
* [ ] Watch the required video and confirm your understanding of the simultaneous card reveal in Planning Poker.
* [ ] Proceed to the weekly hands-on lab activity.
