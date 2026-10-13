# Reading Guide: Module 10 — Earned Value Management

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3310 &BULL; IT PROJECT MANAGEMENT & AGILE METHODOLOGIES</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Introduction

Earned Value Management (EVM) is the Project+ exam's most calculation-intensive topic. This reading guide provides every formula, interpretation rule, and worked example you need to master the material. Study the formula table, work through the practice problems, and use the exam tips to recognize question types before reading the answer choices.

---

## Section 1 — High-Yield Glossary

### Budget at Completion (BAC)

The total authorized budget for the entire project. Established during planning and used as the denominator in EAC calculations. BAC does not change unless a formal approved scope change is processed.

### Planned Value (PV)

Also called Budgeted Cost of Work Scheduled (BCWS). The approved budget for the work that was scheduled to be accomplished by the measurement date. Calculated as `BAC × planned % complete`.

### Earned Value (EV)

Also called Budgeted Cost of Work Performed (BCWP). The approved budget for the work that has actually been completed as of the measurement date. Calculated as `BAC × actual % complete`. EV is not the same as AC — it is the budgeted value of completed work, not the money spent.

### Actual Cost (AC)

Also called Actual Cost of Work Performed (ACWP). The total cost actually incurred for work accomplished during a given time period. Sourced from accounting records.

### Schedule Variance (SV)

The difference between earned value and planned value. Formula: `SV = EV - PV`. Positive = ahead of schedule; negative = behind schedule.

### Cost Variance (CV)

The difference between earned value and actual cost. Formula: `CV = EV - AC`. Positive = under budget; negative = over budget.

### Schedule Performance Index (SPI)

A ratio measuring schedule efficiency. Formula: `SPI = EV / PV`. Values above 1.0 indicate ahead-of-schedule performance; below 1.0 indicates behind-schedule performance.

### Cost Performance Index (CPI)

A ratio measuring cost efficiency. Formula: `CPI = EV / AC`. Values above 1.0 indicate under-budget performance; below 1.0 indicates over-budget performance. CPI is the most predictive single EVM metric.

### Estimate at Completion (EAC)

A forecast of the total project cost at completion. Multiple calculation methods exist depending on the assumption about future performance.

### Estimate to Complete (ETC)

The expected cost needed to finish all remaining project work. Formula: `ETC = EAC - AC`.

### Variance at Completion (VAC)

The projected budget surplus or deficit at project completion. Formula: `VAC = BAC - EAC`. Negative VAC indicates a projected overrun.

### To-Complete Performance Index (TCPI)

The cost efficiency ratio that must be achieved on remaining work to meet a budget target. Formula: `TCPI = (BAC - EV) / (BAC - AC)` (to meet BAC) or `(BAC - EV) / (EAC - AC)` (to meet EAC). Values above 1.0 indicate an increasingly difficult target.

---

## Section 2 — Complete EVM Formula Reference

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| PV | `BAC × Planned % Complete` | Budgeted value of planned work |
| EV | `BAC × Actual % Complete` | Budgeted value of completed work |
| SV | `EV - PV` | (+) ahead of schedule; (–) behind schedule |
| CV | `EV - AC` | (+) under budget; (–) over budget |
| SPI | `EV / PV` | (>1.0) ahead; (<1.0) behind; (=1.0) on track |
| CPI | `EV / AC` | (>1.0) under budget; (<1.0) over budget |
| EAC (CPI trend) | `BAC / CPI` | Forecast assuming current efficiency continues |
| EAC (new estimate) | `AC + ETC` | Forecast using fresh bottom-up estimate |
| EAC (planned rate) | `AC + (BAC - EV)` | Optimistic forecast; assumes remaining work at planned rate |
| ETC | `EAC - AC` | Remaining cost to finish |
| VAC | `BAC - EAC` | (+) projected savings; (–) projected overrun |
| TCPI (to BAC) | `(BAC - EV) / (BAC - AC)` | Efficiency needed to finish within original budget |

---

## Section 3 — Sign Rules and Index Interpretation

### The Universal Sign Rule

All EVM variances use the same sign convention: negative is bad, positive is good.

- Negative SV: behind schedule (EV < PV — you accomplished less than planned)
- Negative CV: over budget (EV < AC — you spent more than the work is worth)
- Negative VAC: projected cost overrun at completion

### The Index Threshold Rule

All EVM indices use the same threshold: below 1.0 is bad, above 1.0 is good, exactly 1.0 is on target.

| SPI Value | Schedule Status | CPI Value | Cost Status |
|-----------|-----------------|-----------|-------------|
| > 1.0 | Ahead of schedule | > 1.0 | Under budget |
| = 1.0 | On schedule | = 1.0 | On budget |
| < 1.0 | Behind schedule | < 1.0 | Over budget |

### Why CPI Matters Most

Research on completed projects consistently shows that CPI stabilizes after approximately 20% of the project is complete. A CPI of 0.80 at 20% completion almost never recovers to 1.0 by project end. This makes early CPI readings the most reliable single predictor of final project cost.

---

## Section 4 — EAC Formula Selection Guide

The Project+ exam frequently tests which EAC formula to use based on stated assumptions. Use this decision table.

| Exam Language | EAC Formula | Assumption |
|---------------|-------------|------------|
| "Assuming current performance continues" | `BAC / CPI` | Future efficiency equals past efficiency |
| "Using a new bottom-up estimate" | `AC + ETC` | Past overruns are sunk; fresh estimate for remaining |
| "Assuming remaining work at planned rate" | `AC + (BAC - EV)` | Past overruns are sunk; future work as originally planned |
| No assumption stated | `BAC / CPI` | Default — most commonly tested |

---

## Section 5 — Worked Practice Problem

### Problem Setup

The Clearwater Network Modernization project has the following data at the end of month 4:

- Total project budget: $800,000
- Planned completion at month 4: 35%
- Actual completion at month 4: 28%
- Actual spending at month 4: $230,000

### Step 1 — Calculate Base Values

- BAC = $800,000
- `PV = $800,000 × 0.35 = $280,000`
- `EV = $800,000 × 0.28 = $224,000`
- AC = $230,000

### Step 2 — Calculate Variances

- `SV = EV - PV = $224,000 - $280,000 = -$56,000` — behind schedule
- `CV = EV - AC = $224,000 - $230,000 = -$6,000` — over budget

### Step 3 — Calculate Indices

- `SPI = EV / PV = $224,000 / $280,000 = 0.80`
- `CPI = EV / AC = $224,000 / $230,000 = 0.974` (approximately 0.97)

### Step 4 — Forecast

- `EAC = BAC / CPI = $800,000 / 0.974 = $821,355`
- `ETC = EAC - AC = $821,355 - $230,000 = $591,355`
- `VAC = BAC - EAC = $800,000 - $821,355 = -$21,355`

### Interpretation

The project is significantly behind schedule (SPI 0.80 — only 80% of planned work accomplished). Cost efficiency is slightly below target (CPI 0.97 — getting 97 cents of value per dollar spent). The schedule problem is more severe than the cost problem. Forecasted overrun at completion is approximately $21,355 if current cost efficiency continues.

---

## Section 6 — EVM Status Interpretation Matrix

| SPI | CPI | Project Status |
|-----|-----|----------------|
| > 1.0 | > 1.0 | Ahead of schedule and under budget — ideal |
| > 1.0 | < 1.0 | Ahead of schedule but over budget — cost problem |
| < 1.0 | > 1.0 | Behind schedule but under budget — schedule problem |
| < 1.0 | < 1.0 | Behind schedule and over budget — serious concern |
| = 1.0 | = 1.0 | Perfectly on track — uncommon in practice |

---

## Section 7 — Project+ Exam Tips

**Tip 1 — EV is the key variable in every formula:**
EV appears in SV, CV, SPI, and CPI. If you can identify EV correctly, you can calculate every other metric. EV = `BAC × actual % complete` — always convert percentage to dollars using BAC.

**Tip 2 — Negative variance equals bad; index below 1.0 equals bad:**
This single rule applies to every EVM metric without exception. Memorize it and apply it mechanically when checking your answer's reasonableness.

**Tip 3 — AC is just spending — it has no "earned" component:**
Students frequently confuse EV and AC. AC comes from the accounting system and reflects money paid out. EV is a calculated value based on completed scope. They are equal only when cost efficiency is exactly 1.0.

**Tip 4 — Match the EAC formula to the stated assumption:**
"Current performance continues" = `BAC / CPI`. "New estimate provided" = `AC + ETC`. "Remaining work at original planned rate" = `AC + (BAC - EV)`. The exam will specify the assumption — read carefully.

**Tip 5 — SV and CV both start with EV minus something:**
`SV = EV - PV` (EV minus Planned Value). `CV = EV - AC` (EV minus Actual Cost). Keep EV in the first position always.

**Tip 6 — SPI and CPI both start with EV divided by something:**
`SPI = EV / PV`. `CPI = EV / AC`. EV is always the numerator.

**Tip 7 — TCPI above 1.0 means difficult remaining target:**
A TCPI of 1.20 means you need to work 20% more efficiently than you have been to meet the budget target. A TCPI well above 1.0 late in the project is often a signal that the budget target is unrealistic.

**Tip 8 — VAC is BAC minus EAC, not the other way around:**
`VAC = BAC - EAC`. If EAC > BAC, VAC is negative (overrun). Students sometimes reverse this and get the wrong sign.

---

## Section 8 — Study Checklist

- [ ] Define PV, EV, and AC in your own words without using abbreviations
- [ ] Write the formulas for SV, CV, SPI, and CPI from memory
- [ ] State the sign rule for all variances and the threshold rule for all indices
- [ ] List three EAC formulas and identify when each applies
- [ ] Write the formulas for ETC and VAC from memory
- [ ] Work through the Clearwater practice problem without looking at the solution
- [ ] Interpret the four SPI/CPI combinations from the status matrix
- [ ] Complete the Module 10 Lab spreadsheet exercise
- [ ] Take the Module 10 Quiz (10 questions, EVM focus)
- [ ] Post Module 10 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **PMI — Practice Standard for Earned Value Management (2nd Edition Overview)**
   *Project Management Institute* — [pmi.org/pmbok-guide-standards/practice-guides/earned-value-management](https://www.pmi.org/pmbok-guide-standards/practice-guides/earned-value-management)
   The authoritative PMI reference for all EVM formulas, measurement baselines, and reporting guidance. Essential for students targeting CAPM or PMP after Project+.

2. **EVM Formula Reference Sheet — PM PrepCast (Free)**
   [project-management-prepcast.com/evm-formulas](https://www.project-management-prepcast.com/free/evm-formulas)
   One-page formula card covering all nine EVM metrics with sign interpretation rules — ideal as a desk reference while completing the Module 10 lab spreadsheet.

3. **YouTube — "Earned Value Management: Full Deep Dive" (Joseph Phillips)**
   [youtube.com/watch?v=wEby_-MVXQM](https://www.youtube.com/watch?v=wEby_-MVXQM)
   Detailed 25-minute lecture on EVM calculations including all three EAC variants and TCPI interpretation. Highly aligned with Module 10 content and the Project+ exam.

4. **Khan Academy — EVM Practice Problems (free)**
   [khanacademy.org — Project Management EVM](https://www.khanacademy.org/computing/computers-and-internet/x1bacd820c5e4194d:program-your-device/x1bacd820c5e4194d:project-management/a/earned-value-management)
   Interactive EVM calculation practice with immediate feedback — suitable for students who want additional drill before the Module 10 quiz.

5. **EVM Explained — ClearlyAgile (Free Article)**
   [clearlyagile.com/agile-blog/earned-value-management](https://www.clearlyagile.com/agile-blog/earned-value-management)
   Plain-language EVM explainer that covers how EVM applies in both predictive and hybrid agile contexts — useful for students heading into Module 12 (Agile) after mastering EVM.
