# Lab Activity: Module 08 – Estimation: Story Points and Planning Poker

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Points:** 100

---

## Overview

This lab is a Planning Poker estimation simulation. You are given five user stories and will play the role of multiple team members, assign story points using the Fibonacci scale, simulate the Planning Poker process, and justify your estimates. You will also calculate velocity and analyze estimation quality. No programming is required.

Estimated time: 90–120 minutes

---

## Scenario Setup

You are the Scrum Master facilitating a Planning Poker session for the HealthTrack team — a 5-Developer team building a personal health monitoring app. The team has completed three Sprints. Their velocity over those Sprints was: Sprint 1: 24 pts, Sprint 2: 31 pts, Sprint 3: 29 pts.

The team uses the Fibonacci scale: 1, 2, 3, 5, 8, 13, 21.

The team has a reference story calibrated at 3 points: "As a user, I can view my step count for today on the dashboard." Everyone agrees this represents a simple display feature with no complex logic.

---

## Part 1 — Planning Poker Simulation (50 points)

### Part 1 Instructions

For each of the five user stories below, simulate a Planning Poker estimation round. You are playing the role of five team members: Alex (backend), Jordan (frontend), Morgan (QA), Taylor (full-stack), and Riley (UX).

For each story, complete the four steps below.

Step A — Initial estimates: Assign a Fibonacci estimate for each team member. Vary the estimates realistically — not all five should agree on the first round. Consider what each team member's perspective might highlight about the work.

Step B — Divergence analysis: If any estimates are more than one Fibonacci step apart (e.g., one person said 3 and another said 8), write a brief note (2–3 sentences) explaining why those team members might disagree and what technical or domain knowledge each perspective reflects.

Step C — Discussion outcome: After the "discussion," assign a final consensus estimate for each story. The consensus estimate may differ from any individual's initial estimate.

Step D — Justification: Write 3–5 sentences explaining your final consensus estimate relative to the 3-point reference story. Why is this story larger or smaller? What factors drove the estimate?

### Stories to Estimate

Story 1 — Daily step count history graph:
As a user, I can view a 7-day graph of my daily step counts so that I can track my activity trends over the past week.

Story 2 — Heart rate monitoring alert:
As a user, I receive a push notification when my resting heart rate exceeds a threshold I have set so that I can seek medical attention if needed.

Story 3 — Meal logging:
As a user, I can log a meal by searching a food database and selecting serving sizes so that I can track my daily caloric intake.

Story 4 — Weekly health summary report:
As a user, I can view a weekly summary of my steps, sleep, heart rate, and calories in a single dashboard view so that I can assess my overall health at a glance.

Story 5 — Share health data with my doctor:
As a user, I can export my health data for a specified date range as a PDF and email it directly to my doctor so that my physician can review trends during appointments.

### Part 1 Grading (50 points)

Each story (5 stories × 10 pts):

- Initial estimates for all 5 team members with realistic variation: 2 pts
- Divergence analysis when estimates diverge: 3 pts
- Final consensus estimate on Fibonacci scale: 2 pts
- Justification relative to reference story: 3 pts

---

## Part 2 — Velocity and Sprint Planning (25 points)

### Part 2 Instructions

Using the five consensus estimates from Part 1, answer the three planning tasks below.

Task A — Velocity baseline (5 points): Calculate the team's average velocity over Sprints 1–3. Show your calculation. What range of story points would you recommend selecting for Sprint 4 based on this velocity? Explain why you would not select exactly the average.

Task B — Sprint 4 selection (10 points): Assume the full Product Backlog for Sprint 4 (in priority order) is: Story 3, Story 1, Story 5, Story 2, Story 4, and an additional item "As a user, I can set and edit my daily step goal" estimated at 3 points. Using your velocity recommendation from Task A, select the items you would take into Sprint 4. Present your selection as a table showing Story ID, Estimate, and Running Total. Explain your cutoff decision.

Task C — Velocity gaming concern (10 points): After Sprint 4, the VP of Engineering says: "Your velocity has been flat at around 28–31 points. I need you to hit 45 points per Sprint by Q4." Write a 150–200 word response from the perspective of the Scrum Master addressing this request. Use specific concepts from this module.

### Part 2 Grading (25 points)

- Task A — Velocity calculation and range recommendation: 5 pts
- Task B — Sprint 4 selection table and cutoff justification: 10 pts
- Task C — Scrum Master response to velocity pressure: 10 pts

---

## Part 3 — Estimation Quality Reflection (25 points)

### Part 3 Instructions

Answer the following three reflection questions in 100–150 words each.

Reflection 1: In your Planning Poker simulation, which story produced the most realistic divergence between team members? Explain what the divergent estimates revealed about the team's understanding of the story, and how the subsequent discussion would improve team alignment.

Reflection 2: Your estimation used relative sizing against a 3-point reference story. Explain how this reference story approach works in practice. What would happen to the team's velocity measurement if the team changed their reference story to a different item midway through product development?

Reflection 3: The Scrum Guide does not mandate story points or Planning Poker. Given this, why do you think these techniques have become nearly universal in Scrum teams? What specific problems do they solve that the Scrum Guide's minimal prescription does not address?

### Part 3 Grading (25 points)

- Reflection 1 — Divergence insight: 8 pts
- Reflection 2 — Reference story mechanism and velocity impact: 9 pts
- Reflection 3 — Why these practices emerged: 8 pts

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Five Planning Poker simulation results (Steps A–D for each story)
2. Part 2: Velocity calculation, Sprint 4 selection table, and Scrum Master response
3. Part 3: Three reflection question responses

Submit to the Canvas assignment portal by the module due date.

---

## Part 9 — Challenge Exercise

### Challenge 1: Estimation Scale Comparison

The HealthTrack team is considering switching from Fibonacci story points to T-shirt sizes for a new product vision workshop with non-technical executives. Evaluate this decision:

1. Estimate the five stories from Part 1 using T-shirt sizes (XS, S, M, L, XL). Map each T-shirt size to a Fibonacci equivalent (e.g., XS=1, S=3, M=5, L=8, XL=13) and show both representations.
2. Calculate what the team's velocity would look like using this T-shirt scale for Sprints 1–3 (using the original point velocities of 24, 31, 29 and your mapping).
3. Identify one type of conversation where T-shirt sizes are genuinely superior to Fibonacci points, and one where Fibonacci points are superior. Justify each in two to three sentences.
4. Write a two-paragraph recommendation to the Product Owner on whether to switch, covering short-term planning accuracy and long-term velocity tracking implications.

### Challenge 2: Velocity Normalization Analysis

The HealthTrack team has experienced two disrupted Sprints in their history: Sprint 4 (velocity=18, two developers out sick) and Sprint 7 (velocity=15, major production incident required team attention). Their remaining Sprints had velocities of 28, 31, 29, 32, 30, 33.

1. Calculate the team's average velocity two ways: including all eight Sprints, and excluding the two disrupted Sprints. Show both calculations.
2. Write a three-to-five sentence analysis explaining which average is more useful for Sprint 9 planning and why. Consider whether disrupted Sprints reflect the team's true capacity.
3. Propose a formal policy for the team's velocity calculation: under what conditions (if any) should a Sprint's velocity be excluded from the rolling average? Write the policy as three to four bullet points that the team could agree to in a Retrospective.
4. Explain how this policy connects to the Scrum value of Transparency and the empirical pillar of Inspection.

### Reflection Questions

1. Story points were designed to capture complexity, effort, and uncertainty together in one number. In practice, teams often conflate story points with hours. What specific team behaviors or management requests cause this conflation, and what is the Scrum Master's role in preventing it?
2. The "#NoEstimates" movement argues that teams should stop estimating story points and instead count stories completed per Sprint as their velocity. What are the strongest arguments for and against this approach? Under what team maturity conditions might counting stories be more accurate than story points?

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Planning Poker Simulation (5 stories × 10 pts) | 50 |
| Part 2 — Velocity and Sprint Planning (3 tasks) | 25 |
| Part 3 — Estimation Quality Reflection (3 questions) | 25 |
| Total | 100 |

---
