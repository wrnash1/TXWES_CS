# Lab Activity: Module 09 – Kanban and Lean Principles

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Points:** 100

---

## Overview

This lab is a Kanban board design and Lean waste analysis exercise. You will design a Kanban board for a hypothetical team, set WIP limits with justification, analyze a value stream for waste, and compare Scrum and Kanban for a specific organizational context. No programming is required.

Estimated time: 90–120 minutes

---

## Part 1 — Kanban Board Design (35 points)

### Part 1 Instructions

You are the team lead for the IT Operations team at a university. Your team handles incoming service requests (password resets, equipment provisioning, network troubleshooting, software licensing) continuously throughout the week. The team has six members: two technicians handle Tier 1 requests, three technicians handle Tier 2, and one senior engineer handles Tier 3 escalations. At any given time the team has 15–25 open requests.

Design a Kanban board for this team by completing the four tasks below.

Task A — Board columns (10 points): Define the columns of your Kanban board. Each column must reflect a real stage of work in this team's process. You must have at least 5 columns. For each column:

- Name the column
- Write one sentence describing what it means for a request card to be in this column
- Specify whether this column is a "work-in-progress" column (someone is actively working) or a "queue" column (items are waiting)

Task B — WIP limits (15 points): Assign a WIP limit to each work-in-progress column. For each limit:

- State the WIP limit number
- Explain your reasoning (consider team capacity and the risk of bottlenecks)
- Explain what the team should do when a column reaches its WIP limit

Task C — Card design (10 points): Design the fields that appear on each request card. Include at least five fields that would help the team manage flow and prioritization. For each field, state: field name, data type (text/date/number/dropdown), and why it supports flow management.

### Part 1 Grading (35 points)

- Task A — Board columns (at least 5): 10 pts (completeness 4, work-vs-queue distinction 3, clarity 3)
- Task B — WIP limits with reasoning: 15 pts (5 pts per column up to 3 columns graded)
- Task C — Card design (5+ fields): 10 pts (field relevance 6, flow support reasoning 4)

---

## Part 2 — Value Stream Mapping and Waste Analysis (40 points)

### Part 2 Instructions

Read the following process description and complete the analysis tasks below.

### Current State Process — Software Feature Request at DevCorp

A new feature request at DevCorp follows this process:

1. Business analyst writes a requirements document (3 days average)
2. Requirements document reviewed and approved by product committee (5-day wait for next committee meeting, then 1 day review)
3. Developer assigned and reads requirements document (1 day)
4. Developer asks BA 8–12 clarifying questions over email (3 days average to resolve all questions)
5. Developer codes the feature (6 days average)
6. Developer submits pull request for code review (2-day wait for reviewer availability)
7. Code review and revisions (1 day average)
8. Feature deployed to staging environment (1-day wait for DevOps team availability)
9. QA team tests feature in staging (2 days)
10. QA writes a test report and sends to product committee (3-day wait for next committee meeting)
11. Product committee approves release (1 day)
12. Feature deployed to production (1 day)

Task A — Value stream map (15 points): Create a simplified value stream map for this process. For each step, classify it as: Value-Adding (VA) — a customer would pay for this step, Non-Value-Adding but Necessary (NVAN) — required by regulations or infrastructure, or Waste (W) — adds no value and could be eliminated or reduced. Present your classification as a table with columns: Step, Description, Classification (VA/NVAN/W), Reasoning.

Task B — Waste identification (15 points): Identify the three most significant waste items in this process. For each:

- Name the Lean waste category it falls under (from the seven wastes)
- Explain why it is waste rather than necessary delay
- Propose a specific, actionable improvement that would reduce or eliminate this waste
- Estimate the days of cycle time that could be saved by this improvement

Task C — Lean principle application (10 points): Write 150–200 words explaining how applying Lean Principle 3 (Create Flow) and Lean Principle 4 (Establish Pull) would change this process. Be specific about which steps would change and how.

### Part 2 Grading (40 points)

- Task A — Value stream map classification: 15 pts (accuracy of VA/NVAN/W classification 10, reasoning quality 5)
- Task B — Top three waste items: 15 pts (5 pts each: category identification 1, waste justification 2, improvement proposal 2)
- Task C — Lean principle application: 10 pts (Principle 3 application 5, Principle 4 application 5)

---

## Part 3 — Scrum vs. Kanban Context Analysis (25 points)

### Part 3 Instructions

Read the two team profiles below. For each team, recommend either Scrum or Kanban (not both) as the primary working method, and write a 150–200 word justification. Your justification must reference specific characteristics of your chosen method and specific characteristics of the team profile that make it appropriate.

### Team Profile A — CloudStore Product Team

CloudStore is building a new e-commerce platform. The six-person team is creating new features based on a product roadmap that changes quarterly as market research informs priorities. Stakeholders want to see new features demonstrated every two weeks and provide feedback that influences subsequent development. The team has a dedicated Product Owner who writes user stories and a technical lead who coordinates architecture decisions. Features require significant coordination between frontend, backend, and data engineering work.

### Team Profile B — HelpdeskFirst Support Team

HelpdeskFirst is a seven-person IT support team that handles incoming tickets from 500 employees across five office locations. Tickets arrive unpredictably throughout the day — an average of 35 per day ranging from simple password resets (15 minutes) to complex server issues (multiple hours). Tickets cannot be batched into two-week cycles; most tickets have a service level agreement requiring resolution within 4 hours. The team values visibility into who is working on what and wants to prevent individuals from being overloaded.

Then write a 100–150 word comparison paragraph addressing: under what circumstances would a team that currently uses Scrum benefit from adding Kanban practices? Give two specific examples.

### Part 3 Grading (25 points)

- Team Profile A recommendation and justification: 10 pts (correct recommendation 3, method characteristics 4, team profile fit 3)
- Team Profile B recommendation and justification: 10 pts (same breakdown)
- Scrum + Kanban hybrid paragraph: 5 pts

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Kanban board design (Tasks A, B, C)
2. Part 2: Value stream map, waste analysis, and Lean principle application
3. Part 3: Two team profile recommendations and hybrid paragraph

Submit to the Canvas assignment portal by the module due date.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Kanban Board Design (Tasks A, B, C) | 35 |
| Part 2 — Value Stream Mapping and Waste Analysis (Tasks A, B, C) | 40 |
| Part 3 — Scrum vs. Kanban Context Analysis | 25 |
| Total | 100 |

---
