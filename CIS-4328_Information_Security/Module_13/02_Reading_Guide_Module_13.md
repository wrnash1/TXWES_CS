# Reading Guide: Module 13 — Risk Management

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports Module 13: Risk Management. You will study the risk vocabulary, qualitative and quantitative risk analysis frameworks, risk response strategies, the risk register, and Business Impact Analysis. These topics map to Security+ Domain 5 (Governance, Risk, and Compliance) and are essential for any security role that involves advising leadership, managing a security program, or producing documentation for audits or compliance.

**Estimated reading and study time:** 2.5 to 3 hours

---

## Learning Objectives

By the end of this module you should be able to:

- Define and distinguish threat, vulnerability, exploit, risk, likelihood, and impact.
- Perform quantitative risk calculations using the AV/EF/SLE/ARO/ALE formulas.
- Apply a qualitative risk matrix to prioritize risks.
- Identify and select the appropriate risk response strategy for a given scenario.
- Describe the structure and purpose of a risk register.
- Explain what a Business Impact Analysis produces and how it supports continuity planning.
- Distinguish between inherent risk and residual risk.

---

## Required Reading

- **NIST SP 800-30 Revision 1** — Guide for Conducting Risk Assessments (free at csrc.nist.gov)
- **NIST SP 800-34 Revision 1** — Contingency Planning Guide, Section 3 (BIA)
- **ISO/IEC 27005** — Information security risk management overview (summary available via free NIST summaries)
- **Professor Messer Security+ SY0-701 Study Guide** — Domain 5 sections on risk management

---

## Section A — Risk Vocabulary

### Core Terms

**Threat**

Any potential event or action that could cause harm to an organizational asset. Threats are classified by source:

- **Environmental**: Natural disasters, power outages, HVAC failure.
- **Human — unintentional**: Employee error, accidental deletion, misconfiguration.
- **Human — intentional**: Cyberattacks, insider theft, sabotage.

**Vulnerability**

A weakness in a system, process, or control that reduces its ability to withstand a threat. Vulnerabilities exist in software (unpatched code), configurations (default passwords), processes (no MFA requirement), and physical controls (unlocked server rooms).

A vulnerability does not cause harm by itself. It requires a threat to exploit it.

**Exploit**

The mechanism by which a threat actor takes advantage of a vulnerability. Exploits may be publicly known (listed in CVE databases) or zero-day (unknown to the vendor).

**Risk**

The probability that a threat will exploit a vulnerability to cause harm to an asset, combined with the magnitude of that harm. Risk is not the threat itself, not the vulnerability itself — it is the intersection of both with their potential impact.

**Asset**

Anything of organizational value that requires protection. The Security+ exam tests five asset categories:

- **Tangible**: Hardware, infrastructure.
- **Intangible**: Intellectual property, brand, customer trust.
- **Data**: Customer records, financial data, proprietary algorithms.
- **People**: Employees with specialized knowledge.
- **Processes**: Business operations and workflows.

**Impact**

The consequence of a successful threat exploitation. Impact dimensions include:

- **Financial**: Direct losses, fines, remediation costs, litigation.
- **Reputational**: Customer trust loss, brand damage.
- **Operational**: Downtime, productivity loss.
- **Regulatory**: Compliance penalties, license revocation.
- **Safety**: Physical harm to people or critical infrastructure.

**Likelihood**

The probability that a given threat will successfully exploit a given vulnerability in a defined time period. In qualitative analysis, expressed as High/Medium/Low. In quantitative analysis, expressed as Annual Rate of Occurrence (ARO).

---

## Section B — Qualitative Risk Analysis

Qualitative risk analysis uses descriptive scales rather than financial figures. It is faster, requires less data, and is more accessible to non-technical stakeholders.

### Risk Matrix

A risk matrix plots likelihood against impact. A 5×5 matrix is common.

| Likelihood / Impact | Negligible (1) | Minor (2) | Moderate (3) | Major (4) | Catastrophic (5) |
|---|---|---|---|---|---|
| Almost Certain (5) | 5 | 10 | 15 | 20 | 25 |
| Likely (4) | 4 | 8 | 12 | 16 | 20 |
| Possible (3) | 3 | 6 | 9 | 12 | 15 |
| Unlikely (2) | 2 | 4 | 6 | 8 | 10 |
| Rare (1) | 1 | 2 | 3 | 4 | 5 |

Scores above a defined threshold (e.g., 15) receive priority treatment. Scores below a lower threshold (e.g., 5) may be accepted without treatment.

**Advantages**: Fast, no financial data required, communicates relative priority.

**Disadvantages**: Subjective, does not support cost-benefit analysis for specific controls.

---

## Section C — Quantitative Risk Analysis

Quantitative risk analysis expresses risk in monetary terms, enabling direct comparison of control cost to risk reduction value.

### Formulas

**Asset Value (AV)**: Total value of the asset, including replacement cost, revenue impact of loss, and regulatory/reputational consequences.

**Exposure Factor (EF)**: The percentage of asset value lost if the threat occurs. Expressed as a decimal (0.0 to 1.0).

**Single Loss Expectancy (SLE)**: Expected loss from one occurrence.

```
SLE = AV × EF
```

**Annual Rate of Occurrence (ARO)**: Expected number of occurrences per year.

**Annual Loss Expectancy (ALE)**: Expected annual loss from the threat.

```
ALE = SLE × ARO
```

### Worked Example

A healthcare organization has a database of patient records with an asset value of $2,000,000. A ransomware attack would render 70% of the data inaccessible until recovered. The organization estimates ransomware attacks occur approximately once every two years.

- AV = $2,000,000
- EF = 0.70
- SLE = $2,000,000 × 0.70 = $1,400,000
- ARO = 0.5 (once every two years)
- ALE = $1,400,000 × 0.5 = $700,000

If an immutable backup solution costs $80,000 per year and would reduce EF from 70% to 10%:

- New SLE = $2,000,000 × 0.10 = $200,000
- New ALE = $200,000 × 0.5 = $100,000
- ALE reduction = $700,000 − $100,000 = $600,000 per year
- Annual control cost = $80,000
- Net benefit = $520,000 per year

The control is strongly justified.

### Value of a Safeguard Formula

```
Value of Safeguard = (Pre-control ALE) − (Post-control ALE) − (Annual cost of safeguard)
```

A positive value means the safeguard is economically justified.

---

## Section D — Risk Response Strategies

The four NIST-defined risk response strategies are tested extensively on Security+.

### Risk Avoidance

Eliminating the activity that creates the risk. The risk is removed entirely because the organization stops doing whatever creates the exposure.

- **Example**: Discontinuing an unencrypted FTP server and replacing it with SFTP.
- **Trade-off**: Losing the business capability the activity provided.
- **When to use**: When no treatment can reduce residual risk to within tolerance and the activity is not essential.

### Risk Transference

Shifting the financial consequence of a risk to a third party.

- **Cyber insurance**: Pays out in the event of covered incidents. Does not prevent the incident — only compensates the financial loss.
- **Contractual transfer**: Contracts that assign liability to vendors for breaches resulting from their negligence.
- **When to use**: When the risk cannot be fully mitigated but financial exposure can be shared or shifted.

### Risk Mitigation

Reducing the likelihood and/or impact of a risk through the application of controls.

- **Reducing likelihood**: Patching vulnerabilities, implementing MFA, network segmentation.
- **Reducing impact**: Backups, incident response plan, data encryption (reduces impact of exfiltration).
- **Residual risk**: Mitigation never eliminates all risk. The remaining risk after controls are applied is residual risk.
- **When to use**: The most common response — applied to risks within the control of the organization.

### Risk Acceptance

Acknowledging a risk and deciding not to take additional action.

- **Formal acceptance**: Documented decision by an authorized executive that the residual risk is within tolerance.
- **When to use**: When the cost of treatment exceeds the value of the asset or when risk is within tolerance.
- **Risk acceptance is not ignorance**: Acceptance requires awareness. Undocumented tolerance of risk is not acceptance — it is a control failure.

---

## Section E — Inherent Risk vs. Residual Risk

**Inherent risk**: The risk level before any controls are applied. Raw exposure.

**Residual risk**: The risk level remaining after controls are applied.

```
Residual Risk = Inherent Risk − Risk Reduction from Controls
```

The goal of a security program is to reduce inherent risk to residual risk that falls within the organization's risk tolerance through appropriate mitigation, with formal acceptance of whatever remains.

**Control risk** is the additional risk introduced when a control fails. A backup that has never been tested has control risk — it may not work when needed.

---

## Section F — Risk Register

A risk register is the central artifact of a risk management program.

### Key Fields

- **Risk ID**: Unique identifier.
- **Risk Description**: What could happen and why.
- **Category**: Technical, operational, regulatory, reputational.
- **Likelihood**: H/M/L or ARO value.
- **Impact**: H/M/L or ALE value.
- **Risk Score**: Likelihood × Impact.
- **Risk Response**: Avoid/Transfer/Mitigate/Accept.
- **Controls in Place**: Existing mitigating controls.
- **Residual Risk Score**: After-control risk level.
- **Risk Owner**: Accountable person.
- **Treatment Deadline**: When treatment is due.
- **Status**: Open/In Progress/Closed.

The risk register enables consistent tracking, executive reporting, and audit evidence. It is reviewed and updated on a defined schedule.

---

## Section G — Business Impact Analysis

The BIA identifies critical business functions and determines the impact of their disruption. It produces the input parameters for business continuity and disaster recovery planning.

### BIA Key Terms

**MTD (Maximum Tolerable Downtime)**: The maximum time a business function can be disrupted before the organization suffers unacceptable harm. Recovery targets must be set shorter than MTD.

**RTO (Recovery Time Objective)**: The target time to restore a function after a disruption. RTO must be less than MTD.

**RPO (Recovery Point Objective)**: The maximum acceptable data loss measured in time. If RPO is 2 hours, backups must occur at least every 2 hours.

**MTBF (Mean Time Between Failures)**: Average time between system failures.

**MTTF (Mean Time to Failure)**: Average lifespan of a non-repairable component.

**MTTR (Mean Time to Repair/Recover)**: Average time to restore a failed system.

### BIA Process

1. Identify business functions and supporting systems.
2. Assign criticality ratings.
3. Establish MTD, RTO, and RPO for each critical function.
4. Identify dependencies and single points of failure.
5. Document minimum resource requirements for each function during disruption.

---

## Key Terms

- **Threat**: Potential event causing harm to assets
- **Vulnerability**: Weakness exploitable by a threat
- **Exploit**: Mechanism that takes advantage of a vulnerability
- **Risk**: Probability of harm × magnitude of harm
- **Asset Value (AV)**: Dollar value of an asset
- **Exposure Factor (EF)**: Percentage of asset value lost per incident
- **SLE (Single Loss Expectancy)**: AV × EF
- **ARO (Annual Rate of Occurrence)**: Expected incidents per year
- **ALE (Annual Loss Expectancy)**: SLE × ARO
- **Risk matrix**: Qualitative grid of likelihood vs. impact
- **Risk avoidance**: Eliminating the risky activity
- **Risk transference**: Shifting financial impact (e.g., cyber insurance)
- **Risk mitigation**: Reducing likelihood or impact with controls
- **Risk acceptance**: Formal decision to accept residual risk
- **Inherent risk**: Risk before controls
- **Residual risk**: Risk remaining after controls
- **Risk register**: Central document tracking all identified risks
- **BIA (Business Impact Analysis)**: Analysis of business function criticality
- **MTD**: Maximum Tolerable Downtime
- **RTO**: Recovery Time Objective
- **RPO**: Recovery Point Objective

---

## Review Questions

1. What is the formula for ALE, and what does each variable represent?
2. An asset is worth $400,000. A flood would destroy 40% of its value. Floods occur on average once every five years. Calculate SLE and ALE.
3. A $50,000 per year flood control system would reduce EF from 40% to 5%. Using your ALE from Question 2, calculate the value of the safeguard.
4. What is the difference between qualitative and quantitative risk analysis? Give one advantage of each.
5. Describe the four risk response strategies. Give a real-world example of each.
6. What is the difference between inherent risk and residual risk?
7. What is the purpose of formal risk acceptance documentation?
8. What is the relationship between MTD and RTO?
9. What does a risk register contain, and how often should it be updated?
10. What is the difference between risk tolerance and risk appetite?

---

## Certification Exam Tip

Security+ SY0-701 heavily tests risk calculations. You must be able to compute SLE, ALE, and value of a safeguard from provided values without a formula sheet. Practice working through calculation scenarios until the formulas are automatic. For risk response, expect scenario questions like "The organization purchases cyber insurance to cover financial losses from a data breach — which risk strategy is this?" (transference). Know the specific definitions cold.

---

*End of Reading Guide — Module 13*
