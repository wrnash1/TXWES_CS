# Reading Guide: Module 09 – Risk Management: Identification and Response

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


**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005) | PMBOK 6th and 7th Editions
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Risk Management addresses the systematic identification, analysis, and response to project uncertainty — both threats that could harm project objectives and opportunities that could enhance them. The Project+ exam tests risk response strategies, the Risk Register, probability and impact scoring, and the distinction between known unknowns and unknown unknowns. This reading guide provides the reference tables and exam tips you need.

---

## 1. High-Yield Glossary

### Risk

An uncertain event or condition that, if it occurs, has a positive or negative effect on one or more project objectives. Risk includes both threats (negative) and opportunities (positive).

### Threat

A risk event that would have a negative effect on project objectives if it occurred. Examples: vendor delays, resource turnover, scope creep, regulatory changes.

### Opportunity

A risk event that would have a positive effect on project objectives if it occurred. Examples: early delivery of a component, favorable exchange rate, improved technology becoming available.

### Risk Register

The primary risk management document that records all identified risks, their characteristics, probability and impact assessments, response strategies, risk owners, and monitoring status.

### Probability

The likelihood that a risk event will occur, expressed as a percentage or ordinal scale (low, medium, high).

### Impact

The degree of effect on project objectives if the risk event occurs. Assessed against cost, schedule, scope, and quality dimensions.

### Risk Score

The product of probability multiplied by impact. Used to prioritize risks for response planning. Higher scores indicate higher priority.

### Known Unknown

A risk that has been identified and can be planned for. Contingency reserves are set aside to address known unknowns.

### Unknown Unknown

A risk that has not been anticipated and cannot be specifically planned for. Management reserves are held at the organizational level to address unknown unknowns.

### Contingency Reserve

Budget or time buffer held within the Cost or Schedule Baseline to address identified risks (known unknowns). Controlled by the project manager.

### Management Reserve

Budget or time buffer held outside the Cost Baseline by management for completely unforeseen events (unknown unknowns). Requires management approval to access.

### Residual Risk

The risk that remains after a response has been implemented. The risk was not fully eliminated by the response.

### Secondary Risk

A new risk created as a direct result of implementing a risk response.

### Risk Owner

The team member assigned responsibility for monitoring a specific risk and implementing its response if triggered.

### Trigger Condition

An early warning sign or indicator that a risk event is about to occur or is occurring. Also called a risk trigger or risk symptom.

---

## 2. Risk Management Process Reference

| Process | Process Group | Key Output | Purpose |
|---|---|---|---|
| Plan Risk Management | Planning | Risk Management Plan | Define risk methodology, roles, thresholds |
| Identify Risks | Planning | Risk Register (initial) | Document all known risks and characteristics |
| Perform Qualitative Risk Analysis | Planning | Updated Risk Register (prioritized) | Rank risks by probability and impact |
| Perform Quantitative Risk Analysis | Planning | Quantitative risk assessment | Numerical analysis of combined risk effect |
| Plan Risk Responses | Planning | Risk responses, contingency reserve | Develop strategies for priority risks |
| Implement Risk Responses | Executing | Change requests, risk response actions | Execute approved response plans |
| Monitor Risks | Monitoring and Controlling | Work performance info, change requests | Track risks and evaluate response effectiveness |

---

## 3. Probability and Impact Matrix

| Probability | Low Impact | Medium Impact | High Impact |
|---|---|---|---|
| High (70–100%) | Medium | High | High |
| Medium (30–69%) | Low | Medium | High |
| Low (1–29%) | Low | Low | Medium |

Risk scores in the High category require active response strategies. Medium risks may be monitored or mitigated. Low risks are typically accepted with passive monitoring.

---

## 4. Threat Response Strategies

| Strategy | Definition | When to Use | Effect on Risk |
|---|---|---|---|
| Avoid | Change the plan to eliminate the threat entirely | Threat has high probability and high impact; elimination is feasible | Eliminates the risk |
| Transfer | Shift financial consequences to a third party | Financial risks; vendor or insurance can absorb the impact | Shifts impact; risk still exists |
| Mitigate | Reduce probability or impact to acceptable level | Risk cannot be avoided; partial reduction is achievable | Reduces risk score |
| Accept (Active) | Set aside contingency reserve; no other response | Risk is low priority or too costly to address proactively | Risk unchanged; reserve covers impact |
| Accept (Passive) | Take no action; deal with risk if it occurs | Risk is very low priority | Risk unchanged; no reserve set |
| Escalate | Transfer response authority to a higher level | Risk is outside project scope or resources | Responsibility transferred |

---

## 5. Opportunity Response Strategies

| Strategy | Definition | Threat Counterpart |
|---|---|---|
| Exploit | Ensure the opportunity definitely occurs | Avoid |
| Enhance | Increase probability or positive impact | Mitigate |
| Share | Assign to a party best positioned to capture value | Transfer |
| Accept | Acknowledge but take no proactive action | Accept |

---

## 6. Risk Register Components

A complete Risk Register includes:

- Risk ID — unique identifier
- Risk description — cause, event, effect statement
- Category — technical, external, organizational, project management
- Probability rating
- Impact rating
- Risk score (probability × impact)
- Priority (derived from score)
- Risk owner
- Response strategy selected
- Response action plan
- Residual risk
- Secondary risks created
- Trigger conditions
- Status (open, in progress, closed)

---

## 7. Known Unknown vs. Unknown Unknown

| Type | Description | Reserve Type | Control |
|---|---|---|---|
| Known Unknown | Identified risk with uncertain occurrence | Contingency Reserve | PM |
| Unknown Unknown | Unidentified, unanticipated event | Management Reserve | Management |

---

## 8. Certification Exam Tips

**Tip 1 — Risk includes opportunities:**
PMI's definition of risk is explicitly neutral — it includes events with positive outcomes (opportunities). Questions that describe beneficial uncertainty (early delivery, favorable market conditions) are testing whether you recognize opportunities as a form of risk.

**Tip 2 — Avoid eliminates; Transfer shifts:**
Avoid removes the risk entirely by changing the plan. Transfer moves the financial consequences to another party but does not eliminate the risk. Students confuse these frequently.

**Tip 3 — Mitigate is reduce, not eliminate:**
Mitigate reduces probability or impact to an acceptable level. If the response eliminates the risk, that is Avoid, not Mitigate. Mitigation leaves a residual risk.

**Tip 4 — Contingency vs. Management Reserve:**
Contingency Reserve is for identified risks (known unknowns); it is inside the Cost Baseline and controlled by the PM. Management Reserve is for unidentified risks (unknown unknowns); it is outside the Cost Baseline and requires management approval.

**Tip 5 — Residual vs. Secondary risk:**
Residual risk is what remains after a response — the leftover threat. Secondary risk is a brand-new risk introduced by the response action itself. Both must be documented in the Risk Register.

**Tip 6 — Qualitative before Quantitative:**
Qualitative risk analysis always precedes quantitative analysis. Qualitative uses probability-impact scoring to prioritize. Quantitative uses numerical modeling (Monte Carlo, decision trees) and is applied only to high-priority risks identified through qualitative analysis.

**Tip 7 — Identify Risks is iterative:**
Risk identification is not a one-time event. New risks emerge throughout the project. The PM should continuously scan for new risks and update the Risk Register as they are identified.

**Tip 8 — Risk owner is not necessarily the PM:**
Risk owners are assigned to the team member best positioned to monitor and respond to each specific risk. The PM does not own every risk — subject matter experts often own technical risks.

---

## 9. Study Checklist

- [ ] Name all six Risk Management processes and their process groups
- [ ] Distinguish threat from opportunity and give one example of each
- [ ] List and define all five threat response strategies with one example each
- [ ] List all four opportunity response strategies and match each to its threat counterpart
- [ ] Explain the difference between residual risk and secondary risk
- [ ] Distinguish contingency reserve from management reserve
- [ ] Describe the key fields in a Risk Register
- [ ] Explain what a trigger condition is and how it is used
- [ ] Complete the Module 09 Lab activity
- [ ] Take the Module 09 Quiz
- [ ] Post Module 09 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 11: Risk Management**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 11](https://opentextbc.ca/projectmanagement/chapter/chapter-11-project-risk-management/)
   Covers all six Risk Management processes, the probability-impact matrix, risk response strategies, and the Risk Register structure with IT-sector examples.

2. **PMI — Practice Standard for Project Risk Management (Overview)**
   *Project Management Institute* — [pmi.org/pmbok-guide-standards/practice-guides/risk-management](https://www.pmi.org/pmbok-guide-standards/practice-guides/risk-management)
   PMI's official risk management guidance. Covers threat and opportunity response strategies, risk registers, and quantitative analysis tools tested on PK0-005.

3. **Risk Register Template and Guide — ProjectManager.com (Free)**
   [projectmanager.com/blog/risk-register](https://www.projectmanager.com/blog/risk-register)
   Step-by-step guide to building a Risk Register with downloadable template. Directly supports the Module 09 lab risk register activity.

4. **YouTube — "Risk Management Explained" (Mike Clayton / OnlinePMCourses)**
   [youtube.com/watch?v=IP7aBBSwq3Y](https://www.youtube.com/watch?v=IP7aBBSwq3Y)
   18-minute video covering risk identification, qualitative analysis, probability-impact matrix scoring, and all five threat response strategies with examples.

5. **Probability-Impact Matrix Interactive Tool — PM Study Circle**
   [pmstudycircle.com/probability-impact-matrix](https://pmstudycircle.com/probability-and-impact-matrix/)
   Free interactive tool for practicing risk scoring and prioritization — excellent preparation for calculation-based questions on the Module 09 quiz.
