# Lab Activity: Module 01 – Software Engineering Overview and SDLC Models

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University
**Points:** 100

---

## Overview

This lab is a documentation and analysis exercise — no programming is required. You will build a structured comparison of SDLC models, apply model selection logic to real project scenarios, and practice the risk analysis thinking that separates good software engineers from novice ones.

The skills you practice here map directly to PSM I exam scenarios that ask you to evaluate project contexts and identify appropriate development approaches.

**Estimated time:** 90–120 minutes

---

## Part 1 — SDLC Model Characteristics Matrix (35 points)

### Instructions

Complete the comparison matrix below by filling in each cell with accurate, specific information. Write in complete sentences where requested. You may use the Reading Guide, the Scrum Guide (scrum.org), and your course notes. Do not copy definitions verbatim — paraphrase in your own words to demonstrate understanding.

### Matrix Template

Create this table in your submission document:

| Attribute | Waterfall | Spiral | Iterative | Agile/Scrum |
|---|---|---|---|---|
| Phase structure | | | | |
| Customer involvement frequency | | | | |
| When requirements are locked | | | | |
| Risk management approach | | | | |
| How changes are handled | | | | |
| Documentation intensity | | | | |
| Best-fit project type | | | | |
| Primary weakness | | | | |

### Grading (35 points)

- 4–5 points per row (8 rows): accuracy, completeness, and use of course terminology
- Partial credit for incomplete rows

---

## Part 2 — Project Scenario Analysis (40 points)

### Part 2 Instructions

Read each of the two project briefs below. For each brief, write a recommendation paragraph (150–200 words) that:

1. Names the SDLC model you recommend
2. Identifies three specific characteristics of the project brief that support your choice
3. Explains why an alternative model would be less appropriate

### Scenario A — Medical Device Firmware

A medical device manufacturer is developing firmware for an implantable cardiac monitor. The device must be certified by the FDA before release. The FDA requires documented evidence that every requirement was formally approved before implementation began, that testing was conducted against those approved requirements, and that a complete audit trail exists from requirement to test result. The requirements have been finalized by a team of cardiologists and biomedical engineers after an 18-month research phase. No requirement changes are expected after sign-off, and the development team has deep expertise in embedded C programming for this hardware platform.

### Scenario B — Consumer Mobile App

A startup is building a social fitness app for iOS and Android. The founding team has a rough product vision but limited market research. They have secured 12 months of seed funding and need to demonstrate traction to investors within 6 months. The target users — recreational runners aged 18–35 — have never seen the product. The team expects to learn what features users actually value only after releasing early versions and watching how users behave. The three-person development team will grow to eight people over the next six months as funding allows.

### Grading (40 points)

- Scenario A recommendation (20 points): correct model identification (5), three valid supporting characteristics (10), one valid argument against an alternative (5)
- Scenario B recommendation (20 points): same breakdown

---

## Part 3 — Risk Identification Exercise (25 points)

### Part 3 Instructions

Using the project scenario below, identify five distinct risks. For each risk, complete the risk register entry described in the template.

### Project Scenario — University Course Registration System

A state university is replacing its 1990s-era course registration system with a modern web application. 25,000 students will use the system simultaneously during peak registration periods. The university's IT department has limited experience with cloud infrastructure. The project timeline is 18 months. The system must integrate with the existing student information system (Banner) via an API that the Banner vendor charges $50,000 per year to maintain. Two key developers are contractors whose contracts expire in 8 months.

### Risk Register Template

For each risk, fill in:

- **Risk ID:** R-01 through R-05
- **Risk Description:** One sentence describing the risk event and its potential consequence
- **Category:** Technical / Resource / Schedule / External / Requirements
- **Likelihood:** Low / Medium / High
- **Impact:** Low / Medium / High
- **Risk Level:** Multiply likelihood score (Low=1, Medium=2, High=3) by impact score — yields 1–9
- **Mitigation Strategy:** One or two sentences describing a specific action to reduce likelihood or impact

### Grading (25 points)

- 5 points per risk register entry
- Full credit requires all six fields completed with plausible, specific content
- Generic mitigations ("test more," "hire better people") earn partial credit

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Completed SDLC Characteristics Matrix (Part 1)
2. Two project scenario recommendation paragraphs (Part 2)
3. Five completed risk register entries (Part 3)

Submit to the Canvas assignment portal by the module due date.

---

## Part 9 — Challenge Exercise

### Challenge 1: SDLC Model Decision Tree

Build a one-page decision tree (hand-drawn or using a free tool such as draw.io) that a project manager could use to select the most appropriate SDLC model. Your tree must:

1. Start with the question "Are requirements fully known and stable?" and branch from there.
2. Include at least six decision nodes covering requirement stability, regulatory compliance needs, team size, and acceptable risk tolerance.
3. Terminate each branch at one of the four models covered in this module (Waterfall, Spiral, Iterative, Agile/Scrum) with a one-sentence justification.
4. Export or photograph the tree and include it in your submission document.

### Challenge 2: Cost-of-Change Estimation Exercise

Using the University Course Registration System scenario from Part 3, estimate how the cost of fixing each of your five identified risks would change depending on when the risk is discovered. For each risk:

1. Assign a base cost (in relative units, e.g., 1 = discovered in requirements phase) to fixing the risk if caught during requirements.
2. Apply Boehm's cost-of-change multipliers to estimate the cost if the same risk is discovered during testing and again during post-deployment maintenance.
3. Write two to three sentences explaining which of your five risks has the highest total cost exposure if discovered late and why.
4. Conclude with a recommendation: would Waterfall or Scrum reduce overall cost-of-change exposure for this project, and why?

### Reflection Questions

1. After building the decision tree, did any of the four models end up with no valid paths leading to it? If so, what does that reveal about that model's practical applicability compared to the others?
2. Real projects rarely fit a single SDLC model perfectly. Identify one hybrid approach you observed in the Reading Guide or lecture content and describe which two models it combines and under what conditions that hybrid might outperform either pure model.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — SDLC Characteristics Matrix | 35 |
| Part 2 — Scenario A Recommendation | 20 |
| Part 2 — Scenario B Recommendation | 20 |
| Part 3 — Risk Register (5 entries × 5 pts) | 25 |
| **Total** | **100** |

---
