# Lab Activity: Module 15 — Software Project Metrics and Velocity Tracking

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Points:** 100

---

## Overview

This lab is a metrics analysis and interpretation exercise. You will analyze velocity data, interpret burndown charts, calculate flow metrics, and identify metric anti-patterns. No running code is required — this is a written analysis lab.

Estimated time: 90–120 minutes

---

## Part 1 — Velocity Analysis (30 points)

### Part 1 Instructions

Use the following Sprint velocity data for the RapidBuild team to complete the three tasks.

### RapidBuild Team Velocity Data

| Sprint | Story Points Planned | Story Points Completed | Notes |
|--------|---------------------|----------------------|-------|
| Sprint 1 | 35 | 22 | Team learning new codebase |
| Sprint 2 | 28 | 25 | — |
| Sprint 3 | 30 | 28 | — |
| Sprint 4 | 35 | 31 | — |
| Sprint 5 | 38 | 36 | — |
| Sprint 6 | 40 | 38 | — |
| Sprint 7 | 45 | 20 | Two developers on leave; major production incident |
| Sprint 8 | 35 | 33 | — |
| Sprint 9 | 38 | 35 | — |
| Sprint 10 | 40 | 38 | — |

Task A — Velocity calculation (10 points): Calculate the team's average velocity for: (1) all 10 Sprints, (2) Sprints 2–6 only, and (3) Sprints 8–10 only. Show your calculations. Which of the three averages would you recommend using for Sprint 11 planning, and why?

Task B — Trend interpretation (10 points): Describe the velocity trend in narrative form. What does the Sprint 7 data point indicate, and should it be included or excluded from planning calculations? What does the gap between planned and completed points in Sprint 7 suggest about how the team set Sprint 7's planned capacity?

Task C — Release forecasting (10 points): After Sprint 10, the Product Backlog contains 190 remaining story points. Using your recommended velocity from Task A, forecast how many Sprints are needed to complete the remaining backlog. Then describe two variables that could make the actual completion date earlier or later than your forecast.

---

### Part 1 Grading (30 points)

- Task A: 10 pts (three correct averages 6, recommendation with reasoning 4)
- Task B: 10 pts (trend described accurately 4, Sprint 7 analysis 4, planned vs. completed observation 2)
- Task C: 10 pts (forecast calculation correct 4, two variables described 6)

---

## Part 2 — Burndown Chart Interpretation (35 points)

### Part 2 Instructions

Read the following burndown chart descriptions and complete the analysis tasks.

### Sprint Burndown Scenario 1 — The DataSync Team

The DataSync team ran a 10-day Sprint with 40 story points in the Sprint Backlog. Their actual remaining points by day were:

| Day | Remaining Points |
|-----|-----------------|
| Day 1 | 40 |
| Day 2 | 40 |
| Day 3 | 38 |
| Day 4 | 38 |
| Day 5 | 37 |
| Day 6 | 36 |
| Day 7 | 35 |
| Day 8 | 35 |
| Day 9 | 12 |
| Day 10 | 4 |

### Sprint Burndown Scenario 2 — The PortalFirst Team

The PortalFirst team ran a 10-day Sprint with 30 story points. Their actual remaining points by day were:

| Day | Remaining Points |
|-----|-----------------|
| Day 1 | 30 |
| Day 2 | 22 |
| Day 3 | 22 |
| Day 4 | 22 |
| Day 5 | 35 |
| Day 6 | 35 |
| Day 7 | 28 |
| Day 8 | 21 |
| Day 9 | 14 |
| Day 10 | 7 |

Task A — DataSync pattern analysis (10 points): Describe the pattern shown in the DataSync burndown. What is the most likely explanation for this pattern? What would the ideal burndown line look like? How far off is the actual trajectory from the ideal at Day 7? What does this pattern indicate about the team's Sprint practices, and what change should the Scrum Master facilitate?

Task B — PortalFirst pattern analysis (10 points): Two unusual events are visible in the PortalFirst burndown. Identify both, describe what likely caused each, and explain what the Scrum Master and team should have done when each event was observed.

Task C — Adaptation response (15 points): For each team (DataSync and PortalFirst), write a brief Sprint Retrospective action item (2–3 sentences each) that addresses the root cause revealed by the burndown pattern. Each action item should be specific enough to implement in the next Sprint — not a vague improvement statement.

---

### Part 2 Grading (35 points)

- Task A: 10 pts (pattern named correctly 3, ideal line described 2, deviation quantified 2, change recommended 3)
- Task B: 10 pts (both events identified 4, cause for each 4, response described 2)
- Task C: 15 pts (DataSync action item specific and actionable 7, PortalFirst action item specific and actionable 8)

---

## Part 3 — Flow Metrics and Anti-Pattern Analysis (35 points)

### Part 3 Instructions

Read the following scenarios and complete the three tasks.

### Flow Scenario — The CloudRoute Team

The CloudRoute team tracks the following data for their last 20 completed stories:

- Average lead time: 34 days
- Average cycle time: 8 days
- Average WIP during the period: 12 stories in progress simultaneously
- Average throughput: 1.5 stories per day

Task A — Flow metric analysis (10 points): Calculate the queue time for the CloudRoute team. What does this metric reveal about the team's workflow? Using Little's Law, verify whether the cycle time data is consistent with the WIP and throughput figures. Show your calculation.

Task B — Bottleneck identification (10 points): The CloudRoute team's Cumulative Flow Diagram shows the following average items in each stage over the measured period:

| Stage | Average Items |
|-------|--------------|
| Backlog | 45 |
| In Progress | 12 |
| Code Review | 8 |
| Testing | 14 |
| Done (closed per week) | 10 |

Identify where the bottleneck is, explain what the data shows, and propose one specific change the team could make to address it.

Task C — Metric anti-pattern diagnosis (15 points): Read the following three organizational scenarios and identify the metric anti-pattern present in each. For each anti-pattern: name it, explain in 2–3 sentences why the metric use is harmful, and describe what the correct use of that metric would be.

Scenario X: A development manager tells three different Scrum Teams: "Team A has velocity 42, Team B has velocity 28, and Team C has velocity 35. Team B needs to improve." At the next Sprint Planning, Team B estimates all their stories 20–30 percent higher than usual.

Scenario Y: A Product Owner tells the team: "We need to ship the analytics dashboard in 6 Sprints no matter what. I'm going to track your velocity every Sprint and if it drops below 35, I need an explanation." In the following Sprint, the team completes 28 points of work but counts two in-progress stories as done to report velocity 37.

Scenario Z: An engineering manager introduces a new dashboard showing each developer's daily commit count and lines of code added per week. Two developers who primarily do refactoring and code review are ranked last every week despite being recognized by peers as the team's strongest contributors.

---

### Part 3 Grading (35 points)

- Task A: 10 pts (queue time calculated correctly 3, interpretation explained 4, Little's Law verification shown 3)
- Task B: 10 pts (bottleneck correctly identified 4, data evidence cited 3, change proposed 3)
- Task C: 15 pts (5 pts per scenario: anti-pattern named 2, harm explained 2, correct use described 1)

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Velocity analysis — Tasks A, B, and C
2. Part 2: Burndown chart interpretation — Tasks A, B, and C
3. Part 3: Flow metrics and anti-pattern analysis — Tasks A, B, and C

Submit to the Canvas assignment portal by the module due date.

---

## Part 9 — Challenge Exercise

### Challenge 1: Velocity Forecasting Model

Using the RapidBuild team's velocity data from Part 1, build a more sophisticated forecast model:

1. In addition to the simple average, calculate a weighted moving average for Sprint 11 planning that gives Sprint 10 a weight of 3, Sprint 9 a weight of 2, and Sprint 8 a weight of 1. Show the calculation and compare it to your simple average from Part 1. Which forecast would you use and why?
2. The Product Backlog currently contains 190 points, but the Product Owner has indicated that: 20 percent of items are "likely to be descoped if timeline pressure increases," 15 percent of items are "likely to expand as more detail is known," and roughly 1 team member hour per day is spent on Sprint ceremonies and coordination that is not reflected in story points. Construct a best-case, most-likely, and worst-case release forecast range. Show all assumptions.
3. A stakeholder asks: "What is the probability we deliver in 5 Sprints? In 6? In 7?" Using the velocity range from Sprints 8–10 (low: 33, average: 35.3, high: 38), calculate the implied number of Sprints under each velocity assumption and express the results as a range. Explain why this is a more useful answer than a single point estimate.
4. The team is considering splitting one developer's role into a dedicated QA/testing specialist to reduce the end-of-Sprint testing crunch that causes the flat-then-drop burndown pattern. Using the velocity data, model the expected impact: Sprint 11–12 will lose 8 points of capacity while the team adjusts; after Sprint 12 the team expects 10 percent higher throughput due to faster story cycle time. Calculate the net Sprint forecast for Sprints 11–15 under this model and determine whether the investment breaks even before Sprint 15.

### Challenge 2: Metric Dashboard Design

You are the Scrum Master for a new product team at a software company. The VP of Engineering has asked you to propose a metrics dashboard that will be shown at the monthly leadership review. Design a dashboard that honestly serves both the team's empirical process and the leadership's need for visibility:

1. Select exactly five metrics for the dashboard. For each metric: name it, define how it is calculated, state the data source, describe what the metric is intended to show, and write one "misuse warning" explaining how this metric could be misused by leadership and how you would prevent that misuse.
2. The VP proposes adding individual developer story point completion and daily commit count to the dashboard. Write a professional 100-150 word response declining these additions and proposing alternatives that meet the VP's underlying need for visibility without the anti-patterns these metrics introduce.
3. For each of your five chosen metrics, design one visual format (table, line chart, bar chart, CFD band, etc.) and write a two-sentence description of what a healthy pattern looks like versus a pattern that should prompt discussion.
4. After three months, the leadership team starts citing your dashboard metrics in performance reviews for individual developers. Write a two-paragraph response addressing: why this creates a metric dysfunction, what the correct use of team metrics is, and what change you propose to the dashboard to prevent future misuse.

### Reflection Questions

1. The Agile Manifesto values "working software over comprehensive documentation." Metrics like burndown charts and CFDs are documentation of team performance — not working software. Does using metrics violate the Agile Manifesto's intent, or are they consistent with it? Construct the argument that metrics serve Agile values and the argument that they can undermine them. Which is stronger?
2. Goodhart's Law states: "When a measure becomes a target, it ceases to be a good measure." Identify a real-world example (from software development, education, healthcare, or government) where Goodhart's Law caused a metric to fail catastrophically. Then describe how the same failure pattern could occur with Sprint velocity if misused, and propose a structural safeguard that would prevent it.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Velocity Analysis (Tasks A, B, C) | 30 |
| Part 2 — Burndown Chart Interpretation (Tasks A, B, C) | 35 |
| Part 3 — Flow Metrics and Anti-Pattern Analysis (Tasks A, B, C) | 35 |
| Total | 100 |

---
