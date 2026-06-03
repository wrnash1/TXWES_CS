# Lab: Module 15 — DevOps, Agile, and ITIL Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Lab Overview

**Title:** Value Stream Mapping, Error Budget Design, and Integration Assessment

**Duration:** 90–120 minutes

**Format:** Individual written deliverables

**Submission:** Upload completed documents to the LMS by the module deadline.

In this lab you will perform a value stream mapping analysis, design an SLO and error budget for a fictional service, evaluate an organization's DevOps/ITIL integration maturity, and recommend improvements.

---

## Scenario

**Organization:** NorthPoint Logistics Technology (NPT)

**Context:** NPT is a mid-size logistics software company with approximately 280 engineers. They provide a shipment tracking platform used by regional freight carriers. The platform handles approximately 12 million API calls per day.

**Current state:**

- Software is delivered using Agile sprints (2-week cycles). Teams use Jira for backlog management.
- A CI/CD pipeline (Jenkins) exists and runs automated unit and integration tests on every commit.
- All deployments to production require a change request submitted in ServiceNow. Normal changes require CAB approval. The CAB meets every Tuesday at 2:00 PM.
- Average time from code merge to production deployment: 9 days.
- The operations team (12 engineers) is separate from development (220 engineers). The operations team handles all incidents and is responsible for production deployments.
- Post-incident reviews occur occasionally but are not formal or documented consistently.
- The company has two major customers (freight carriers) who require 99.7% monthly availability in their contracts (SLA).

**Recent incidents:**

- Last month: a deployment caused a 4-hour outage affecting 100% of API traffic.
- The month before: a dependency update caused intermittent errors for 6 hours affecting approximately 30% of API requests.
- Total downtime last quarter: 11 hours 40 minutes unplanned.

---

## Part 1: Value Stream Map and Waste Analysis (35 minutes)

Using the information provided in the scenario, create a value stream map for NPT's feature delivery process — from the moment a developer merges a code change to the moment it is live in production.

### Step 1 — Build the Current State Map

Represent the following steps in your VSM. For each step, estimate a realistic cycle time and wait time based on the scenario context (use your judgment where specific times are not given):

1. Code merged to main branch (triggers CI pipeline).
2. Automated unit and integration tests run.
3. Code review in Jira (developer assigns a peer reviewer).
4. Change request submitted in ServiceNow.
5. Change request reviewed by the change manager for completeness.
6. CAB meeting — change approved.
7. Operations team schedules and executes deployment to staging.
8. Operations team validates deployment in staging.
9. Operations team executes production deployment.
10. Post-deployment monitoring and validation.

**Format:** Present as a table with columns: Step, Description, Cycle Time (estimated), Wait Time (estimated), Notes.

### Step 2 — Calculate Totals

Sum the total cycle time and total wait time. Calculate the **process efficiency** = Total Cycle Time ÷ (Total Cycle Time + Total Wait Time) × 100%.

### Step 3 — Identify Waste

Identify the three biggest sources of waste in the current value stream. For each, name the Lean waste category (DOWNTIME), estimate the time impact, and explain why this waste exists.

### Step 4 — Future State Recommendations

For each identified waste source, recommend a specific change that would eliminate or significantly reduce it. Each recommendation should reference an ITIL 4 principle or practice. The recommendations should be realistic for an organization at NPT's maturity level — not assume they can achieve 50 deployments per day overnight.

**Written summary (100–150 words):** If all three improvements were implemented, what would the new total lead time be? What organizational changes (not just technical changes) would be required to make these improvements sustainable?

---

## Part 2: SLO and Error Budget Design (25 minutes)

NPT's SLA requires 99.7% monthly availability. You have been asked to design an internal SLO and error budget that protects the SLA while giving the engineering team a rational framework for deployment decisions.

**Task 2a — Define the SLI:**

Define a Service Level Indicator for the shipment tracking API. Your SLI must specify:

- What is being measured (exact metric).
- How it is measured (what data source or method).
- The time window for measurement.

**Task 2b — Define the SLO:**

Set an internal SLO that is stricter than the SLA. Justify your choice. (Hint: if the SLA is 99.7%, what SLO gives you enough buffer to catch issues before SLA breach? Consider that detection and remediation take time.)

**Task 2c — Calculate the Monthly Error Budget:**

Given your SLO and a 30-day month (43,200 minutes):

- What is the error budget in minutes per month?
- What is it in percentage terms?
- Based on last quarter's incident data (11 hours 40 minutes of unplanned downtime), was the error budget exceeded? By how much, in minutes?

**Task 2d — Error Budget Policy:**

Write a brief error budget policy (5–7 bullet points) defining:

- What happens when the budget is healthy (> 75% remaining).
- What happens when the budget is at 50%.
- What happens when the budget is nearly exhausted (< 10% remaining).
- What happens when the budget is fully consumed.
- Who reviews error budget status and how often.

**Task 2e — Incident Review:**

Last month's 4-hour outage was caused by a deployment. Under your SLO, how much of the monthly error budget did this single incident consume (as a percentage)? What does this tell you about the deployment process?

---

## Part 3: Integration Maturity Assessment (30 minutes)

Assess NPT's current DevOps/ITIL integration maturity and recommend a path forward.

### Maturity Scale

For each dimension below, rate NPT's current maturity on a 1–4 scale:

- **1 — Initial:** Ad hoc, no defined process.
- **2 — Developing:** Process exists but inconsistently applied.
- **3 — Defined:** Consistent, documented process with measurable outcomes.
- **4 — Optimizing:** Process continuously improved using data and feedback.

### Dimensions to Assess

Complete the assessment table:

| Dimension | Current Maturity (1–4) | Evidence from Scenario | Gap to Level 4 |
|---|---|---|---|
| CI/CD Pipeline Automation | | | |
| Change Enablement Integration with CI/CD | | | |
| Incident and Problem Management | | | |
| Dev/Ops Collaboration (silo vs. shared ownership) | | | |
| Reliability Measurement (SLO/SLI/error budget) | | | |
| Post-Incident Learning (postmortems) | | | |
| Continual Improvement (structured, data-driven) | | | |

### Prioritized Improvement Roadmap

Based on your assessment, identify the two dimensions with the largest gaps that would have the greatest business impact if improved.

For each of the two dimensions:

- Current state (from your assessment).
- Target state (Level 3 or 4 — describe specifically what this looks like for NPT).
- Three concrete actions to move from current to target state.
- Which ITIL 4 practice is most relevant.
- Estimated timeline to reach target state.

**Written reflection (100–150 words):** The operations team at NPT has been performing all production deployments independently for years. If NPT moves toward a model where development teams own their own deployments (shared ownership), how might the operations team react? What change management approach would you use to gain their support and address their concerns?

---

## Submission Requirements

Submit one document (PDF or Word) containing:

- Part 1: VSM table, process efficiency calculation, waste analysis, future state recommendations, and written summary.
- Part 2: SLI definition, SLO justification, error budget calculation, error budget policy, and incident analysis.
- Part 3: Completed maturity assessment table, improvement roadmap, and written reflection.

**Minimum length:** 1,000 words across written sections.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| VSM accuracy and waste identification quality | 30 |
| SLO/error budget design accuracy and reasoning | 30 |
| Maturity assessment depth and improvement roadmap quality | 30 |
| Professional writing and formatting | 10 |
| **Total** | **100** |

---

*End of Module 15 Lab — approximately 175 lines*
