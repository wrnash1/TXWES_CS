# Lab Activity: Module 10 — Earned Value Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

## Total Points: 100

---

## Lab Overview

In this lab you will apply all EVM formulas to a realistic IT project scenario. The lab has three parts: calculating base EVM metrics, generating performance forecasts, and writing a management status report based on your findings. You will use a spreadsheet for calculations and submit a written deliverable interpreting the results.

Submit your completed spreadsheet and written report as a single PDF or zipped file to the Canvas Module 10 Lab assignment.

---

## Scenario Background

Pinnacle Healthcare is implementing a new electronic health records (EHR) integration platform across 14 hospital locations. You are the project manager. The project has a total approved budget of $1,200,000 and a planned 12-month schedule beginning January 1.

The project has been divided into four phases. The table below shows each phase's budgeted cost and the planned completion percentage for each phase by the end of month 6 (the midpoint status review date).

| Phase | Phase Budget | Planned % Complete by Month 6 |
|-------|-------------|-------------------------------|
| Phase 1 — Infrastructure Setup | $300,000 | 100% |
| Phase 2 — Data Migration | $400,000 | 75% |
| Phase 3 — Integration Development | $350,000 | 50% |
| Phase 4 — Training and Go-Live | $150,000 | 0% |
| **Total** | **$1,200,000** | |

At the month 6 status review, your project coordinator has collected the following actual data:

| Phase | Actual % Complete | Actual Cost Spent |
|-------|------------------|-------------------|
| Phase 1 — Infrastructure Setup | 100% | $315,000 |
| Phase 2 — Data Migration | 60% | $265,000 |
| Phase 3 — Integration Development | 40% | $160,000 |
| Phase 4 — Training and Go-Live | 0% | $0 |
| **Total** | | **$740,000** |

---

## Part 1 — Calculate Base EVM Metrics

### Part 1 Objective

Calculate PV, EV, and AC for each phase and for the total project.

### Part 1 Instructions

Complete the table below for each project phase and the total row. Show all calculations in your spreadsheet. For each phase, PV = Phase Budget × Planned % Complete and EV = Phase Budget × Actual % Complete.

| Phase | PV | EV | AC |
|-------|----|----|----|
| Phase 1 — Infrastructure Setup | | | |
| Phase 2 — Data Migration | | | |
| Phase 3 — Integration Development | | | |
| Phase 4 — Training and Go-Live | | | |
| **Project Total** | | | |

After completing the table, answer the following:

**Question 1-A:** Why is the Earned Value for Phase 4 zero even though the project is halfway through its schedule? What does this tell you about the relationship between EV and calendar time?

**Part 1 Point Value:** 20 points

- Phase-level PV calculations (8 pts — 2 pts each, correct use of percentage)
- Phase-level EV calculations (8 pts — 2 pts each, correct use of actual completion)
- AC values correctly transferred from scenario (2 pts)
- Question 1-A: 2–3 sentences showing understanding of EV concept (2 pts)

---

## Part 2 — Calculate Variance and Index Metrics

### Part 2 Objective

Calculate SV, CV, SPI, and CPI for each phase and for the total project.

### Part 2 Instructions

Using the PV, EV, and AC values from Part 1, complete the variance and index table below. Show formulas in your spreadsheet cells. Round all index values to two decimal places.

| Phase | SV (`EV-PV`) | CV (`EV-AC`) | SPI (`EV/PV`) | CPI (`EV/AC`) |
|-------|--------------|--------------|---------------|---------------|
| Phase 1 — Infrastructure Setup | | | |  |
| Phase 2 — Data Migration | | | | |
| Phase 3 — Integration Development | | | | |
| Phase 4 — Training and Go-Live | N/A | N/A | N/A | N/A |
| **Project Total** | | | | |

Note: Phase 4 variances and indices are not applicable because both PV and EV are zero — no work was planned or performed.

After completing the table, answer the following:

**Question 2-A:** Identify which phase has the worst schedule performance and which has the worst cost performance. For each, explain in one to two sentences what the data tells you about what happened during execution.

**Question 2-B:** The project total SPI is below 1.0 and the total CPI is also below 1.0. Using the EVM Status Interpretation Matrix from the reading guide, characterize the overall project status and identify the greater concern — schedule or cost.

**Part 2 Point Value:** 30 points

- Phase-level SV calculations (6 pts)
- Phase-level CV calculations (6 pts)
- Phase-level SPI calculations (6 pts)
- Phase-level CPI calculations (6 pts)
- Question 2-A response: identifies correct worst phases with evidence (4 pts)
- Question 2-B response: correct matrix quadrant identification and prioritization (2 pts)

---

## Part 3 — Forecasting Metrics

### Part 3 Objective

Calculate EAC, ETC, and VAC for the total project using three EAC methods.

### Part 3 Instructions

Using the project total PV, EV, AC, and BAC values, calculate EAC three ways. Show all formulas in your spreadsheet.

| EAC Method | Formula | Calculation | Result |
|------------|---------|-------------|--------|
| Method 1: Current CPI trend | `BAC / CPI` | | |
| Method 2: New estimate (assume $580,000 remains) | `AC + ETC` | | |
| Method 3: Remaining work at planned rate | `AC + (BAC - EV)` | | |

For Method 2, the project team has provided a new bottom-up estimate of $580,000 for all remaining work.

After completing the EAC table, calculate ETC and VAC for Method 1 only.

| Metric | Formula | Calculation | Result |
|--------|---------|-------------|--------|
| ETC (Method 1) | `EAC - AC` | | |
| VAC (Method 1) | `BAC - EAC` | | |

**Question 3-A:** The three EAC methods produce different forecasted totals. Which method should you present to the project sponsor as the primary forecast, and why? Under what circumstances would Method 3 (planned rate) be the most appropriate choice?

**Question 3-B:** The VAC from Method 1 is negative. Translate this number into a plain-English sentence a non-technical project sponsor would understand. Do not use acronyms in your answer to Question 3-B.

**Part 3 Point Value:** 30 points

- Three EAC calculations correct (15 pts — 5 pts each)
- ETC and VAC calculations (5 pts)
- Question 3-A: Correct method selection with reasoning (5 pts)
- Question 3-B: Plain-language translation without jargon (5 pts)

---

## Part 4 — Management Status Report

### Part 4 Objective

Synthesize all EVM findings into a one-page written status report for the project sponsor.

### Part 4 Instructions

Write a status report addressed to the Pinnacle Healthcare project sponsor. Your report must be 200–300 words and must address all of the following points in flowing prose (not bullets):

1. Overall project status as of month 6 (use SPI and CPI values to characterize performance)
2. Which phase is performing best and which is performing worst, with specific data references
3. The forecasted total project cost at completion (cite Method 1 EAC) and the projected variance
4. One specific recommendation for corrective action to improve the worst-performing phase
5. A closing statement on whether the project remains achievable within the original budget and schedule, with your professional judgment

Format: Write as a professional memo with a subject line, date, and your name as project manager. Use plain language — translate all EVM terms into business language. Do not use abbreviations like SPI or EV in the memo body.

**Part 4 Point Value:** 20 points

| Criterion | Points | Description |
|-----------|--------|-------------|
| Completeness | 8 | All five required points addressed |
| Accuracy | 6 | EVM values cited match Part 1–3 calculations |
| Professional tone | 3 | Memo format, plain language, no unexplained jargon |
| Recommendation quality | 3 | Specific, actionable, tied to scenario data |

---

## Deliverables Summary

Submit the following as a single PDF or zipped package:

1. Spreadsheet showing all calculations for Parts 1, 2, and 3 with visible formulas
2. Written responses to Questions 1-A, 2-A, 2-B, 3-A, and 3-B (may be embedded in spreadsheet or in a separate document)
3. Management status report memo (Part 4)

---

## Grading Rubric Summary

| Section | Points | Key Criteria |
|---------|--------|--------------|
| Part 1: Base Metrics | 20 | Correct PV and EV by phase; AC transferred accurately |
| Part 2: Variances and Indices | 30 | All formulas correct; worst-phase identification accurate |
| Part 3: Forecasting | 30 | Three EAC methods correct; plain-language translation |
| Part 4: Status Report | 20 | Five required points; professional tone; actionable recommendation |
| **Total** | **100** | |
