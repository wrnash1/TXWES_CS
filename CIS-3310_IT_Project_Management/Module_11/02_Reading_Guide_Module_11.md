# Reading Guide: Module 11 — Risk Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Introduction

Risk Management is one of the most heavily tested knowledge areas on the CompTIA Project+ exam. Questions appear in two forms: process identification (which risk management step does this activity belong to?) and concept application (which response strategy is most appropriate for this risk?). This reading guide provides the complete reference framework for both question types.

---

## Section 1 — High-Yield Glossary

### Risk

An uncertain event or condition that, if it occurs, has a positive or negative effect on one or more project objectives. Note that risks include both threats (negative) and opportunities (positive).

### Risk Appetite

The degree of uncertainty an organization or stakeholder is willing to accept in pursuit of project value. High risk appetite = willingness to accept more uncertainty.

### Risk Tolerance

The specific range of acceptable variation in outcomes that a stakeholder or organization will permit. Risk tolerance operationalizes risk appetite.

### Risk Threshold

The level at which a risk becomes unacceptable and triggers an escalation or active response.

### Risk Register

The primary risk management document. Records all identified risks, their analysis (probability, impact, score), risk owners, response strategies, and current status. Updated throughout the project lifecycle.

### Risk Breakdown Structure (RBS)

A hierarchical categorization of risk sources used to organize risk identification. Common top-level categories for IT projects include technical, organizational, external, and project management risks.

### Probability and Impact Matrix

A grid that maps each risk's probability rating against its impact rating to produce a prioritized risk score. Also called a heat map or P-I matrix.

### Expected Monetary Value (EMV)

A quantitative risk analysis technique. Formula: `EMV = Probability × Impact`. Threats use negative impact values; opportunities use positive impact values.

### Contingency Reserve

Budget or schedule buffer set aside for identified risks. Controlled by the project manager and used when an identified risk materializes.

### Management Reserve

Budget or schedule buffer set aside for unknown unknowns — unidentified risks. Requires authorization from above the project manager to access.

### Residual Risk

The risk remaining after a planned response strategy has been applied. Even mitigation leaves some residual risk.

### Secondary Risk

A new risk created by implementing a risk response strategy. Must be identified, analyzed, and managed like any primary risk.

### Workaround

An unplanned response to a risk event that was either not identified or not anticipated to occur. Distinguished from a contingency plan, which is pre-planned.

### Risk Trigger

A warning sign or precursor event that indicates a risk is about to materialize. Also called a risk symptom.

### Watchlist

A list of low-priority risks that do not require active response but are monitored periodically for changes in status or priority.

### Risk Audit

A structured examination of the effectiveness of risk response activities and the Risk Register's accuracy. Typically performed by someone external to the immediate project team.

---

## Section 2 — Risk Management Process Reference

| Process | Process Group | Key Inputs | Key Outputs |
|---------|--------------|------------|-------------|
| Plan Risk Management | Planning | Project charter, stakeholder register, organizational process assets | Risk Management Plan |
| Identify Risks | Planning | Risk Management Plan, scope baseline, assumption log | Risk Register (initial) |
| Qualitative Risk Analysis | Planning | Risk register, Risk Management Plan, probability-impact scales | Updated Risk Register (prioritized) |
| Quantitative Risk Analysis | Planning | Updated risk register, cost/schedule models, historical data | Quantitative risk report, updated forecasts |
| Plan Risk Responses | Planning | Updated risk register, Risk Management Plan | Risk responses, contingency/management reserves, updated project plan |
| Monitor and Control Risks | Monitoring and Controlling | Work performance data, risk register, risk reports | Workarounds, change requests, updated risk register |

---

## Section 3 — Risk Identification Techniques

| Technique | How It Works | Best Used When |
|-----------|-------------|----------------|
| Brainstorming | Team generates risks in facilitated open session | Early identification; broad coverage needed |
| Delphi Technique | Anonymous expert opinions gathered, aggregated, and refined iteratively | Expert input needed without groupthink or authority bias |
| Interviews | One-on-one discussions with stakeholders and SMEs | Surfacing privately held concerns or specialized domain risks |
| SWOT Analysis | Examines internal strengths/weaknesses and external opportunities/threats | Connecting organizational context to project risk |
| Assumption Analysis | Challenges each documented project assumption | Identifying risks from planning-phase uncertainties |
| Checklist Analysis | Reviews risk lists from similar past projects | Ensuring common risks are not overlooked |
| Root Cause Analysis | Works backward from potential impacts to identify causes | Deep technical or organizational risk investigation |

---

## Section 4 — Risk Response Strategies

### Strategies for Threats (Negative Risks)

| Strategy | Definition | Example |
|----------|-----------|---------|
| Avoid | Eliminate the risk by changing the plan | Remove a risky feature from scope |
| Transfer | Shift financial consequence to a third party | Purchase insurance; use fixed-price contract |
| Mitigate | Reduce probability or impact before occurrence | Add testing phases; build schedule buffer |
| Accept (Active) | Acknowledge risk; create contingency plan | Set aside reserve funds for identified risk |
| Accept (Passive) | Acknowledge risk; take no action unless it occurs | Monitor low-priority risk on watchlist |
| Escalate | Pass risk to higher authority due to scope/authority limits | Elevate strategic regulatory risk to portfolio level |

### Strategies for Opportunities (Positive Risks)

| Strategy | Definition | Example |
|----------|-----------|---------|
| Exploit | Ensure opportunity definitely occurs | Assign best resources to guarantee early delivery |
| Share | Partner with another party to capture opportunity | Joint venture to leverage combined technology |
| Enhance | Increase probability or impact of opportunity | Add senior developer to accelerate innovation |
| Accept | Take no specific action; capture if it occurs naturally | Accept minor schedule improvement if it happens |

---

## Section 5 — Probability and Impact Matrix

### Standard Probability Scale

| Label | Probability Value |
|-------|-------------------|
| Very High | 0.90 |
| High | 0.70 |
| Medium | 0.50 |
| Low | 0.30 |
| Very Low | 0.10 |

### Standard Impact Scale (Cost/Schedule)

| Label | Impact Value |
|-------|-------------|
| Very High | 0.80 |
| High | 0.40 |
| Medium | 0.20 |
| Low | 0.10 |
| Very Low | 0.05 |

### Risk Score Calculation

`Risk Score = Probability × Impact`

A risk with probability 0.70 and impact 0.40 has a risk score of `0.70 × 0.40 = 0.28` — a high-priority risk requiring active response planning.

### Heat Map Zones

| Score Range | Zone | Response Priority |
|-------------|------|-------------------|
| 0.18 – 0.72 | Red (High) | Immediate active response required |
| 0.05 – 0.17 | Yellow (Medium) | Contingency planning; regular monitoring |
| 0.01 – 0.04 | Green (Low) | Watchlist; periodic review |

---

## Section 6 — Expected Monetary Value Practice

### EMV Formula

`EMV = Probability × Impact`

For threats: Impact is expressed as a negative value (cost to the project).
For opportunities: Impact is expressed as a positive value (benefit to the project).

### Decision Tree Example

A project team is deciding whether to use an established vendor (Option A) or a newer vendor with better pricing (Option B).

Option A: 20% probability of a $40,000 delay cost. EMV = `0.20 × (-$40,000) = -$8,000`

Option B: 50% probability of a $60,000 delay cost, plus a 30% probability of a $15,000 savings opportunity. EMV = `(0.50 × -$60,000) + (0.30 × +$15,000) = -$30,000 + $4,500 = -$25,500`

Option A has a better EMV (-$8,000 vs. -$25,500), so the risk-adjusted choice is Option A.

---

## Section 7 — Reserve Analysis

| Reserve Type | Covers | Who Controls | Basis |
|-------------|--------|-------------|-------|
| Contingency Reserve | Identified risks (known unknowns) | Project Manager | EMV of risk register items; percentage of budget |
| Management Reserve | Unidentified risks (unknown unknowns) | Senior Management / Sponsor | Organization policy; percentage of total budget |

---

## Section 8 — Project+ Exam Tips

**Tip 1 — Know all five threat strategies and four opportunity strategies:**
The exam presents scenarios and asks which strategy is being used. Avoidance eliminates the risk. Transfer shifts financial consequence. Mitigation reduces probability or impact. Escalation passes authority upward. Exploit ensures opportunity occurs. Enhance increases its probability or impact.

**Tip 2 — Distinguish residual risk from secondary risk:**
Residual risk is what remains after a response. Secondary risk is a new risk caused by the response. Both must be added to the Risk Register.

**Tip 3 — Contingency vs. management reserves:**
Contingency covers identified risks — the PM controls access. Management reserve covers unidentified risks — higher authorization is required. The exam tests this distinction directly.

**Tip 4 — Qualitative analysis is priority-ranking, not statistical:**
Qualitative analysis uses scales and scoring (subjective judgment). Quantitative analysis uses statistical models and numerical data. You do qualitative first, then quantitative (and only for high-priority risks).

**Tip 5 — Delphi Technique prevents groupthink:**
When the exam describes a need for expert input without dominant voices influencing results, Delphi is the answer. Brainstorming allows vocal participants to dominate; Delphi uses anonymous, iterative expert polling.

**Tip 6 — Workaround vs. contingency plan:**
A contingency plan is pre-planned for an identified risk. A workaround is improvised for an unplanned or unexpected event. If the risk was in the register and the response was pre-planned, it is a contingency plan. If not, it is a workaround.

**Tip 7 — EMV: negative for threats, positive for opportunities:**
When calculating EMV for a risk portfolio, threats contribute negative values and opportunities contribute positive values. The sum gives the net expected risk impact to the project.

**Tip 8 — Risk Register is updated at every risk management step:**
Initial entries come from identification. Probability and impact scores come from qualitative analysis. Response strategies, owners, and reserves come from response planning. Status updates come from monitoring. The register is never "done."

---

## Section 9 — Study Checklist

- [ ] Name all six risk management processes and their process groups
- [ ] List five risk identification techniques and describe when each is appropriate
- [ ] Describe how to calculate a risk score using the P-I matrix
- [ ] Name five threat response strategies and four opportunity response strategies
- [ ] Distinguish residual risk from secondary risk with an example
- [ ] Explain the difference between contingency reserves and management reserves
- [ ] Calculate EMV for a sample risk with probability and impact values
- [ ] Describe the Delphi Technique and explain why it reduces groupthink
- [ ] Define workaround and distinguish it from a contingency plan
- [ ] Complete the Module 11 Lab risk register activity
- [ ] Take the Module 11 Quiz (10 questions)
- [ ] Post Module 11 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 11: Risk Management (Advanced)**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 11](https://opentextbc.ca/projectmanagement/chapter/chapter-11-project-risk-management/)
   In-depth coverage of risk identification techniques, quantitative analysis tools (Monte Carlo, EMV), and the full risk response strategy matrix.

2. **PMI — Risk Management Practice Standard (Overview)**
   *Project Management Institute* — [pmi.org/pmbok-guide-standards/practice-guides/risk-management](https://www.pmi.org/pmbok-guide-standards/practice-guides/risk-management)
   Official PMI guidance on the Risk Register structure, qualitative vs. quantitative analysis, EMV calculations, and Monte Carlo simulation applications.

3. **EMV and Decision Tree Tutorial — PM Study Circle (Free)**
   [pmstudycircle.com/expected-monetary-value](https://pmstudycircle.com/expected-monetary-value-emv-in-risk-management/)
   Step-by-step EMV calculation guide with decision tree examples. Directly supports the Module 11 lab quantitative risk analysis exercise.

4. **YouTube — "Monte Carlo Simulation for Risk" (Practical PM)**
   [youtube.com/watch?v=GtXJ9kI-pLI](https://www.youtube.com/watch?v=GtXJ9kI-pLI)
   Clear explanation of how Monte Carlo simulation generates cost probability distributions. Aligned with Module 11 quantitative analysis content.

5. **Risk Register Template — ProjectManager.com (Free Download)**
   [projectmanager.com/templates/risk-register-template](https://www.projectmanager.com/templates/risk-register-template)
   Professional Risk Register template with all standard fields: ID, description, probability, impact, score, owner, trigger, response strategy, and status. Usable directly in the Module 11 lab.
