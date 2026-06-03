# Lab Activity: Module 13 — Continuous Integration and DevOps Basics

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Points:** 100

---

## Overview

This lab is a CI/CD analysis and design exercise. You will evaluate pipeline configurations, recommend deployment strategies, and connect CI/CD practices to Scrum team effectiveness. No running code or pipeline setup is required — this is a written analysis lab.

Estimated time: 90–120 minutes

---

## Part 1 — Pipeline Analysis (30 points)

### Part 1 Instructions

Read the following description of a Scrum team's current CI pipeline and answer the three analysis tasks.

### The NovaBuild Team Pipeline

The NovaBuild team has a six-person Scrum development team working on a customer-facing web application. Their current CI process works as follows:

- Developers push code to feature branches. They merge to the main branch at the end of each Sprint.
- When code is merged to main, a pipeline runs automatically: compile → run all tests → deploy to staging.
- The pipeline takes 55 minutes to complete.
- Tests include 2,400 unit tests, 180 integration tests, and 22 end-to-end (E2E) browser tests.
- The E2E tests account for 40 of the 55 minutes.
- In the last three Sprints, the team discovered significant integration defects only during Sprint Review — after the end-of-Sprint merge.
- The pipeline is currently red 20 percent of the time due to two flaky E2E tests that fail intermittently without any code changes causing them.

Task A — Defect discovery timing (10 points): Explain why defects are being discovered at Sprint Review rather than earlier in the Sprint. What fundamental CI practice is the team not following, and what specific change to their development workflow would address this? Your response should be 100–150 words.

Task B — Pipeline performance (10 points): The team wants to reduce pipeline feedback time from 55 minutes to under 15 minutes. Propose a specific pipeline restructuring strategy. Explain what stages would run in which order, how the E2E tests would be handled, and what trade-off the team accepts with your proposed structure.

Task C — Flaky test response (10 points): The team has two flaky E2E tests causing a 20 percent pipeline red rate. Explain what a flaky test is and why it is damaging to CI culture — reference the specific behavioral consequence described in the module. What is the recommended immediate action for a flaky test, and what is the longer-term resolution?

---

### Part 1 Grading (30 points)

- Task A — Defect timing diagnosis: 10 pts (correct CI practice identified 4, specific workflow change described 6)
- Task B — Pipeline restructuring proposal: 10 pts (correct staging strategy 5, E2E handling 3, trade-off acknowledged 2)
- Task C — Flaky test analysis: 10 pts (definition + cultural consequence 5, immediate action 3, long-term resolution 2)

---

## Part 2 — Deployment Strategy Decision (35 points)

### Part 2 Instructions

Read the following release scenario and complete the three tasks below.

### The DataVault Release

DataVault is a cloud-based data management platform. The engineering team is preparing to release version 3.0, which includes:

- A redesigned user dashboard with significantly different UI layout
- A new data export feature supporting three new file formats
- A database schema change: two new columns added to the primary data table; one legacy column deprecated (but not yet removed)
- A performance improvement to the main data query that changes the query execution path

The team has strong monitoring on error rates, query execution times, and user session length. The team's operations practice follows DevOps principles — the development team monitors production behavior and responds to incidents.

The release is considered high-risk because: (1) the new dashboard layout may confuse longtime users, (2) the performance improvement is new and untested under real production load, (3) the legacy column is still used by a batch reporting process that runs weekly.

Task A — Deployment strategy recommendation (15 points): Recommend either blue-green or canary deployment for this release. Justify your recommendation by connecting the specific risks in the scenario to the strengths of your chosen strategy. Address the database schema change specifically — what makes it compatible or incompatible with your chosen strategy?

Task B — Rollback plan (10 points): Write a brief rollback plan for your recommended deployment strategy. Your plan should address: what triggers the rollback decision, what the rollback mechanism is, and how the database schema change affects the rollback options. Your response should be 100–150 words.

Task C — Definition of Done criteria (10 points): The DataVault team is updating their Definition of Done to include CI/CD-related criteria for this release. Propose four specific, verifiable DoD criteria related to the deployment. For each criterion, write one sentence explaining why it belongs in the DoD rather than in a separate release checklist.

---

### Part 2 Grading (35 points)

- Task A — Strategy recommendation with risk justification: 15 pts (correct strategy for risks 6, risk-to-strategy connection 6, database schema addressed 3)
- Task B — Rollback plan: 10 pts (trigger described 3, mechanism described 4, schema impact addressed 3)
- Task C — DoD criteria: 10 pts (four specific criteria 6, DoD vs. release checklist reasoning 4)

---

## Part 3 — Scrum and CI/CD Integration (35 points)

### Part 3 Instructions

Read the following team scenario and complete the three tasks below.

### The FastPath Team

FastPath is a Scrum team that has been operating for twelve Sprints. Their velocity has been declining for the last four Sprints. In the Sprint Retrospective, the team identified the following:

- Two developers spent an average of 8 hours each in the last Sprint debugging merge conflicts because everyone pushed to main on the last day of the Sprint
- The team has a CI pipeline, but the integration test stage is bypassed every Sprint because "it always fails and we know the code is fine"
- The Definition of Done says "CI pipeline green" but this is effectively ignored
- Two defects introduced in Sprint 10 were not discovered until Sprint 13 because there was no automated integration testing catching regressions
- The team estimates they spend 30 percent of each Sprint on activities that would be eliminated by functional CI: manual testing, merge conflict resolution, and regression investigation

Task A — Root cause analysis (10 points): Identify the three root causes behind FastPath's velocity decline. For each root cause, name the CI/CD concept or practice that directly addresses it. Explain in 2–3 sentences per root cause why the practice addresses it.

Task B — Improvement roadmap (15 points): Write a three-Sprint improvement roadmap for FastPath. For each Sprint in your roadmap:

- State the primary CI/CD improvement the team will implement
- Describe the expected effect on the team's behavior or workflow
- Identify one metric the team will inspect at the Sprint Retrospective to evaluate whether the improvement worked

Task C — Scrum Master communication (10 points): Write a 100–150 word message from the Scrum Master to the Product Owner explaining why two Sprints of the team's capacity need to be partially invested in CI/CD improvements rather than features. The message should:

- Connect the CI/CD investment to a business outcome (velocity, reliability, or delivery predictability)
- Avoid pipeline implementation details
- Reference the velocity decline using specific numbers from the scenario

---

### Part 3 Grading (35 points)

- Task A — Root cause analysis: 10 pts (three causes identified 3, CI/CD concept named for each 3, explanation quality 4)
- Task B — Improvement roadmap: 15 pts (three Sprints with improvements 6, behavioral effects described 6, metrics identified 3)
- Task C — Scrum Master communication: 10 pts (business outcome connection 5, clarity and tone 3, velocity reference 2)

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Pipeline analysis — Tasks A, B, and C
2. Part 2: Deployment strategy decision — Tasks A, B, and C
3. Part 3: Scrum and CI/CD integration — Tasks A, B, and C

Submit to the Canvas assignment portal by the module due date.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Pipeline Analysis (Tasks A, B, C) | 30 |
| Part 2 — Deployment Strategy Decision (Tasks A, B, C) | 35 |
| Part 3 — Scrum and CI/CD Integration (Tasks A, B, C) | 35 |
| Total | 100 |

---
