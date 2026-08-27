# Reading Guide: Module 05 – Cost Management: Budgeting and EVM

**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005) | PMBOK 6th and 7th Editions
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Cost Management is the discipline of planning, estimating, budgeting, and controlling project costs so that the project can be completed within the approved budget. The most calculation-intensive component — Earned Value Management (EVM) — integrates scope, schedule, and cost into a single performance measurement system and is among the most heavily tested topics on the CompTIA Project+ exam. Memorize every formula in this guide before sitting for the quiz.

---

## 1. High-Yield Glossary

### Budget at Completion (BAC)

The total approved budget for the project. BAC is the baseline against which all EVM calculations are made. BAC does not change unless a formal change request is approved.

### Cost Baseline

The approved, time-phased project budget used as the reference for measuring cost performance. The Cost Baseline includes contingency reserves but excludes management reserves. Changes to the Cost Baseline require a formal change request and CCB approval.

### Contingency Reserve

Budget set aside within the Cost Baseline to address identified risks documented in the Risk Register (known unknowns). Controlled by the project manager — the PM can release contingency funds when a documented risk occurs.

### Management Reserve

Budget held outside the Cost Baseline by senior management to address completely unforeseen events (unknown unknowns). The PM must request management reserve from leadership. Management reserve is NOT part of the Cost Baseline.

### Planned Value (PV)

The authorized budget assigned to the scheduled work as of the status date. PV comes from the Cost Baseline (the time-phased plan). Also called BCWS — Budgeted Cost of Work Scheduled.

### Earned Value (EV)

The budgeted value of work actually completed as of the status date. EV = Percent Complete × BAC. Also called BCWP — Budgeted Cost of Work Performed.

### Actual Cost (AC)

The total cost actually incurred to accomplish the work performed as of the status date. Also called ACWP — Actual Cost of Work Performed.

### Cost Variance (CV)

The difference between earned value and actual cost. CV = EV - AC. Negative CV = over budget. Positive CV = under budget.

### Schedule Variance (SV)

The difference between earned value and planned value. SV = EV - PV. Negative SV = behind schedule. Positive SV = ahead of schedule. Note: SV is expressed in dollar terms, not time.

### Cost Performance Index (CPI)

A ratio measuring cost efficiency. CPI = EV / AC. CPI < 1.0 = over budget (getting less than $1.00 of value for every $1.00 spent). CPI > 1.0 = under budget.

### Schedule Performance Index (SPI)

A ratio measuring schedule efficiency. SPI = EV / PV. SPI < 1.0 = behind schedule. SPI > 1.0 = ahead of schedule.

### Estimate at Completion (EAC)

The expected total cost of the project based on current performance. Most common formula: EAC = BAC / CPI. Alternative: EAC = AC + ETC.

### Estimate to Complete (ETC)

The expected cost of remaining work. ETC = EAC - AC.

### Variance at Completion (VAC)

The projected over/under budget at project completion. VAC = BAC - EAC. Positive VAC = projected to finish under budget. Negative VAC = projected to finish over budget.

### To-Complete Performance Index (TCPI)

The cost efficiency required for the remainder of the project to meet a cost objective. TCPI = (BAC - EV) / (BAC - AC) (to meet original BAC).

---

## 2. Complete EVM Formula Reference

| Metric | Formula | Interpretation |
|---|---|---|
| Cost Variance | CV = EV - AC | Negative = over budget |
| Schedule Variance | SV = EV - PV | Negative = behind schedule |
| Cost Performance Index | CPI = EV / AC | < 1.0 = over budget |
| Schedule Performance Index | SPI = EV / PV | < 1.0 = behind schedule |
| Estimate at Completion (CPI-based) | EAC = BAC / CPI | Total projected cost |
| Estimate at Completion (AC-based) | EAC = AC + ETC | When remaining work re-estimated |
| Estimate to Complete | ETC = EAC - AC | Remaining cost |
| Variance at Completion | VAC = BAC - EAC | Projected final over/under |
| To-Complete Performance Index | TCPI = (BAC - EV) / (BAC - AC) | Efficiency needed to finish on budget |

---

## 3. Cost Estimating Techniques Comparison

| Technique | Data Needed | Accuracy | Best Used When |
|---|---|---|---|
| Analogous (Top-down) | Historical project costs | Low-Moderate (ROM) | Early phases; limited scope detail |
| Parametric | Unit rate data (cost per unit) | Moderate | Reliable unit rates exist; partial detail |
| Bottom-Up | Complete WBS with work packages | High | WBS complete; accuracy required |
| Three-Point (PERT) | O, M, P estimates per item | Moderate-High | High uncertainty in individual estimates |

ROM (Rough Order of Magnitude) accuracy: -25% to +75%.
Budget estimate accuracy: -10% to +25%.
Definitive estimate accuracy: -5% to +10%.

---

## 4. Cost Baseline vs. Project Budget

Understanding what is and is not in the Cost Baseline is directly tested on the exam.

| Component | Included in Cost Baseline? | Controlled By |
|---|---|---|
| Work package cost estimates | Yes | Project Manager |
| Contingency reserves (known unknowns) | Yes | Project Manager |
| Management reserves (unknown unknowns) | No | Senior Management |
| Cost Baseline | Yes (this IS the baseline) | Project Manager |
| Project Budget = Cost Baseline + Mgmt Reserve | N/A (total funding) | Organization |

---

## 5. Worked EVM Example

A data center migration project has the following status at the end of Month 3:

- BAC = $500,000
- Work planned to be done by now = 40% of total (PV = 0.40 × $500,000 = $200,000)
- Work actually completed = 35% of total (EV = 0.35 × $500,000 = $175,000)
- Actual spending to date = $190,000 (AC = $190,000)

Calculations:

- CV = EV - AC = $175,000 - $190,000 = -$15,000 (over budget)
- SV = EV - PV = $175,000 - $200,000 = -$25,000 (behind schedule)
- CPI = EV / AC = $175,000 / $190,000 = 0.921 (over budget — getting $0.92 of work per $1.00 spent)
- SPI = EV / PV = $175,000 / $200,000 = 0.875 (behind schedule — completing 87.5% of planned work)
- EAC = BAC / CPI = $500,000 / 0.921 = $542,900 (projected to overspend by ~$42,900)
- VAC = BAC - EAC = $500,000 - $542,900 = -$42,900 (projected over budget)

Status summary: The project is both over budget and behind schedule. The PM should investigate root causes and consider corrective action.

---

## 6. Certification Exam Tips

**Tip 1 — EV is always the starting point:**
Every EVM formula uses EV. If you are uncertain which formula to use, ask: "Am I measuring cost performance (use AC) or schedule performance (use PV)?" CV and CPI use AC. SV and SPI use PV.

**Tip 2 — Negative variance is always bad:**
Negative CV = over budget. Negative SV = behind schedule. Index below 1.0 = same bad condition. Positive = favorable.

**Tip 3 — Cost Baseline excludes management reserves:**
This is one of the most tested distinctions. The Cost Baseline = work package estimates + contingency reserves. Management reserves sit above and outside the baseline.

**Tip 4 — SV is in dollars, not time:**
SV = EV - PV is expressed in dollars. A negative SV does not tell you how many days behind schedule the project is — it tells you how much dollar-value of work is behind plan. Students sometimes confuse this with schedule delay in days.

**Tip 5 — EAC = BAC/CPI assumes current performance continues:**
The most common EAC formula assumes the project will continue spending at the current CPI. If the PM has identified a specific corrective action and expects future efficiency to differ, the EAC = AC + ETC formula is more appropriate.

**Tip 6 — TCPI above 1.0 means more efficiency is needed:**
TCPI = (BAC - EV) / (BAC - AC). A TCPI of 1.20 means the team must work 20% more efficiently for the rest of the project to hit the original budget. Values well above 1.0 may indicate the original budget is no longer achievable.

**Tip 7 — ROM vs. definitive estimates:**
A ROM estimate (-25% to +75%) is used during Initiating for feasibility. A definitive estimate (-5% to +10%) requires a complete WBS and detailed analysis. The exam tests whether you can identify which estimate is appropriate given the project stage.

**Tip 8 — Contingency vs. management reserve in scenario questions:**
If a question says the PM "releases reserve for a risk that materialized" or "uses reserve for an identified risk," that is contingency reserve. If a question says management "allocates additional budget for an unexpected situation," that is management reserve.

---

## 7. Required Reading and Study Resources

Complete the following before the lab and quiz:

- Read the cost management chapter in the course OER textbook (linked in Canvas), focusing on EVM formulas and cost reserve structures.
- Review the CompTIA Project+ PK0-005 exam objectives at comptia.org for the cost management domain.
- For supplemental EVM practice, visit professormesser.com for Project+ cost management coverage.

---

## 8. Study Checklist

- [ ] Write all nine EVM formulas from memory (CV, SV, CPI, SPI, EAC, ETC, VAC, TCPI, EV)
- [ ] Explain what a CPI of 0.85 means in plain English
- [ ] Explain what an SPI of 1.12 means in plain English
- [ ] State the difference between contingency reserve and management reserve
- [ ] State whether management reserve is included in the Cost Baseline
- [ ] List the four estimating techniques and identify when each is most appropriate
- [ ] Complete the EVM worked example in Section 5 without looking at the answers
- [ ] Complete the Module 05 Lab EVM calculation exercises
- [ ] Take the Module 05 Quiz
- [ ] Post Module 05 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 7: Cost Management**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 7](https://opentextbc.ca/projectmanagement/chapter/chapter-7-project-cost-management/)
   Covers cost estimating techniques, budget baseline development, and Earned Value Management with step-by-step worked examples.

2. **PMI — Practice Standard for Earned Value Management (Overview)**
   *Project Management Institute* — [pmi.org/pmbok-guide-standards/practice-guides/evm](https://www.pmi.org/pmbok-guide-standards/practice-guides/earned-value-management)
   Official PMI EVM guidance covering all nine EVM formulas, including EAC variants and TCPI interpretation.

3. **YouTube — "Earned Value Management in 15 Minutes" (PM PrepCast)**
   [youtube.com/watch?v=xHLfEY8GFOQ](https://www.youtube.com/watch?v=xHLfEY8GFOQ)
   Concise video covering CPI, SPI, EAC, ETC, and VAC with numeric examples — highly recommended as a pre-quiz review.

4. **EVM Formula Sheet — PM Study Circle (Free Download)**
   [pmstudycircle.com/earned-value-management-formulas](https://pmstudycircle.com/earned-value-management-formulas/)
   One-page reference card with all EVM formulas and their interpretive rules (when values are > 1, < 1, or = 1). Print-friendly.

5. **Cost Estimating Techniques — Simplilearn (Free Article)**
   [simplilearn.com/cost-estimation-in-project-management](https://www.simplilearn.com/cost-estimation-in-project-management-article)
   Compares analogous, parametric, and bottom-up estimating with accuracy ranges and use-case guidance aligned to PK0-005 objectives.
