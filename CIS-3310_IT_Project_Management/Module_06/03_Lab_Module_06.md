# Lab Activity: Module 06 – Quality Management

**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005)
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Lab Overview

In this lab you will apply Module 06 quality management concepts by completing three activities: classifying quality activities and costs, analyzing defect data using quality tools, and developing a Quality Management Plan excerpt. All deliverables are written documents — no software installation is required.

Submit all work as a single PDF or Word document to the Canvas assignment portal.

---

## Scenario Background

Meridian Software (a fictional company) has just completed a major release of its cloud-based accounting application. The QA and QC team has been tracking defect data for the past 90 days. You are the IT Project Manager responsible for quality on the next release cycle and must analyze the current data and plan improvements.

Defect data from the 90-day period:

| Defect Category | Number of Defects Reported |
|---|---|
| Database timeout errors | 87 |
| UI rendering issues (mobile) | 43 |
| Incorrect tax calculation | 112 |
| Authentication failures | 29 |
| Export to PDF errors | 18 |
| Session timeout warnings | 11 |
| API response formatting | 7 |

Total defects: 307

Additional context:

- The team has been skipping the formal code review process to meet sprint deadlines
- Post-release customer complaint calls have increased 35% compared to the previous release
- Three enterprise clients have threatened to cancel contracts due to the tax calculation errors
- The development team estimates it would cost $45,000 to fix all identified defects
- Two clients have already requested $12,000 in credits for downtime caused by the defects

---

## Part 1: Quality Activity and Cost Classification

### Part 1 Objective

Classify quality-related activities and costs from the Meridian Software scenario using the correct PMI terminology.

### Part 1 Instructions

Complete Part 1-A and Part 1-B below.

#### Part 1-A: QA vs. QC Classification

For each activity below, write whether it is a Quality Assurance (QA) or Quality Control (QC) activity. Then write a one-sentence justification using the process orientation (process-focused vs. product-focused) to support your answer.

| Activity | QA or QC | Justification |
|---|---|---|
| 1. Running automated regression tests on completed modules | | |
| 2. Auditing the team's adherence to the formal code review process | | |
| 3. Inspecting a PDF export function against acceptance criteria | | |
| 4. Reviewing the development process flow to identify steps where tax calculation errors are most likely to be introduced | | |
| 5. Comparing defect rates across sprint teams to identify which team's process produces the fewest errors | | |
| 6. Testing completed authentication workflows against documented security requirements | | |

#### Part 1-B: Cost of Quality Classification

For each cost item below, identify whether it is a Prevention, Appraisal, Internal Failure, or External Failure cost. Then write a one-sentence explanation.

| Cost Item | COQ Category | Explanation |
|---|---|---|
| 1. $45,000 in developer time to fix the identified defects before the next release | | |
| 2. $12,000 in credits paid to clients for downtime caused by released defects | | |
| 3. $8,000 investment in an automated testing platform that catches bugs before deployment | | |
| 4. Staff time spent in a 4-hour quality process improvement workshop | | |
| 5. Time spent by QA engineers reviewing completed features against acceptance criteria | | |
| 6. Three enterprise clients threatening contract cancellation due to the tax calculation errors | | |

**Part 1 Point Value:** 30 points (2.5 pts per row across both tables)

---

## Part 2: Quality Tool Application

### Part 2 Objective

Apply two quality tools — the Pareto Chart and the Fishbone Diagram — to analyze the Meridian Software defect data and identify a corrective action focus.

### Part 2 Instructions

#### Part 2-A: Pareto Analysis

Using the defect data table above, complete the following Pareto analysis.

Step 1: Calculate the percentage of total defects each category represents. Round to one decimal place.

| Defect Category | Defects | Percentage of Total |
|---|---|---|
| Database timeout errors | 87 | |
| UI rendering issues (mobile) | 43 | |
| Incorrect tax calculation | 112 | |
| Authentication failures | 29 | |
| Export to PDF errors | 18 | |
| Session timeout warnings | 11 | |
| API response formatting | 7 | |
| Total | 307 | 100% |

Step 2: Sort the categories from highest to lowest defect count. Then calculate the cumulative percentage.

| Rank | Defect Category | Defects | Cumulative % |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |

Step 3: Answer these questions in 2–3 sentences each.

Question A: Based on the 80/20 rule, which defect categories should the team focus on first? What percentage of all defects do these top categories represent?

Question B: A developer suggests fixing the API response formatting errors first because they are "easy wins." Using Pareto analysis logic, explain why this is the wrong prioritization strategy.

#### Part 2-B: Fishbone Diagram for Tax Calculation Errors

Draw or describe a Fishbone (Ishikawa) Cause-and-Effect Diagram for the "Incorrect tax calculation" defect category. Your diagram must:

- Identify the problem (effect) at the fish's head
- Include at least five potential causes organized into at least three of these six categories: People, Process, Equipment/Technology, Materials/Data, Environment, Measurement

You may draw the diagram by hand and photograph it, or describe it in a structured text format using indentation to show category and cause hierarchy.

After completing the diagram, write a 2–3 sentence explanation of which cause you believe is most likely given the scenario context (the team skipping code reviews), and what corrective action you would recommend first.

**Part 2 Point Value:** 40 points

Grading breakdown:

- Pareto percentage calculation (10 pts): Correct percentages; correct rank order
- Cumulative percentage column (10 pts): Correct cumulative totals
- Question A response (5 pts): Correct identification of top categories; correct 80/20 interpretation
- Question B response (5 pts): Correct rejection of "easy win" logic with Pareto justification
- Fishbone diagram (10 pts): Problem at head; at least 5 causes; at least 3 categories; causes are realistic given the scenario

---

## Part 3: Quality Management Plan Excerpt

### Part 3 Objective

Draft the Quality Assurance and Quality Control sections of a Quality Management Plan for Meridian Software's next release cycle.

### Part 3 Instructions

Write a Quality Management Plan excerpt containing the following four components. Each component should be 3–5 sentences or a structured list. Be specific to the Meridian Software scenario — do not write generic statements.

#### Component A: Quality Standards

State at least three measurable quality standards the next release must meet. Each standard must be specific and testable (include a threshold or numeric target).

#### Component B: Quality Assurance Activities

Describe at least three specific QA activities the team will perform during the next development cycle. For each activity, state who is responsible and when it will occur.

#### Component C: Quality Control Activities

Describe at least three specific QC activities the team will perform before releasing the next version. For each activity, state what is being inspected and what the acceptance criterion is.

#### Component D: Defect Reporting Process

Describe how defects found during QC will be documented, assigned, tracked, and resolved. Include at minimum: the tool or document used to track defects, who reviews and prioritizes them, and what determines when a defect is "resolved."

**Part 3 Point Value:** 30 points

Grading breakdown:

- Quality Standards (8 pts): Three measurable, testable standards specific to a software accounting application
- QA Activities (8 pts): Three process-focused activities with owner and timing
- QC Activities (8 pts): Three product-focused activities with inspection target and acceptance criterion
- Defect Reporting Process (6 pts): Complete workflow from discovery to resolution

---

## Deliverables Summary

Compile the following into one submission document:

1. Part 1-A classification table (QA vs. QC) and Part 1-B classification table (COQ)
2. Part 2-A Pareto analysis tables with Question A and B responses
3. Part 2-B Fishbone diagram with corrective action explanation
4. Part 3 Quality Management Plan excerpt (four components)

Submit as a single PDF or Word document to the Canvas Module 06 Lab assignment.

---

## Grading Rubric Summary

| Section | Points | Key Criteria |
|---|---|---|
| Part 1: Activity and Cost Classification | 30 | Correct QA/QC and COQ classifications with PMI-aligned justifications |
| Part 2: Quality Tool Application | 40 | Correct Pareto math and prioritization; complete fishbone with realistic causes |
| Part 3: Quality Management Plan | 30 | Measurable standards; specific QA and QC activities; complete defect workflow |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

This section is optional for students seeking additional depth and exam preparation. It is not graded as part of the standard 100-point lab but may be used for extra credit at the instructor's discretion.

### Challenge Step 1: Control Chart Interpretation

Using the following 12 weeks of defect counts from the CityBuild GIS rollout — 4, 7, 5, 6, 3, 8, 9, 11, 14, 12, 13, 15 — calculate the mean and estimate the Upper Control Limit (UCL) and Lower Control Limit (LCL) using ±3 units as a simplified approximation. Plot the values in a simple table. Identify any data points outside the control limits and any Rule of Seven violations (7 consecutive points on the same side of the mean or trending in one direction). Write two sentences explaining what corrective action the PM should take based on your findings.

### Challenge Step 2: COQ Trade-Off Analysis

The project sponsor asks whether investing an additional $8,000 in developer training (prevention) is justified given the project's current defect rate. Using the COQ framework, estimate how much the current defect rate is costing the project in internal failure costs (assume each defect costs $500 to fix and the project averages 20 defects per month). Calculate how many months it would take the prevention investment to break even, assuming training reduces the defect rate by 60%. Show your calculation and write a three-sentence recommendation for the sponsor.

### Challenge Step 3: Process Audit Checklist

Design a brief Quality Assurance process audit checklist (8–10 items) that could be used to verify whether the CityBuild project team is following its approved Quality Management Plan. Items should cover: testing procedures, defect logging discipline, review gate compliance, and documentation standards. Frame each item as a yes/no auditable question. This exercise mirrors the type of QA audit documented in PMI's Manage Quality process.
