# Video Script: Module 13 — Risk Management (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 13 | Texas Wesleyan University"]**

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome to Module 13 — Risk Management.

Every security decision is ultimately a risk decision. Should we spend $200,000 on a new firewall? Should we accept the risk of running an unpatched system for another 30 days? Should we encrypt this data tier or is the cost not justified by the likelihood of exposure? These are not purely technical questions. They are risk questions — and they require a framework.

Risk management is the discipline that gives security professionals a vocabulary and a methodology for quantifying, prioritizing, and responding to threats and vulnerabilities in a way that business leadership can understand and act on. It is the bridge between the technical world of security controls and the business world of costs, priorities, and trade-offs.

The Security+ exam gives significant weight to risk management concepts in Domain 5 (Governance, Risk, and Compliance). This module gives you the vocabulary, the analysis frameworks, and the response strategies that you will need on the exam and in the field.

In Part 1 we build the vocabulary and work through risk analysis — qualitative and quantitative. In Part 2 we cover risk response strategies, the risk register, Business Impact Analysis, and how it all connects.

---

## Section 1 — The Risk Vocabulary

**[SHOW SLIDE: Risk vocabulary hierarchy diagram]**

Before we can analyze risk, we need precise definitions. These terms are tested individually and in combination on Security+.

**Threat**: Any potential event or action that could cause harm to an asset. Threats include natural disasters, hardware failure, cyberattacks, and human error. A threat is not inherently malicious — a power outage is a threat to availability even without an attacker.

**Threat actor**: The entity that carries out a threat. Nation-states, cybercriminals, hacktivists, insiders, and script kiddies are all threat actors.

**Vulnerability**: A weakness in a system, process, or control that could be exploited by a threat to cause harm. A vulnerability alone does not cause harm — it requires a threat to exploit it. An unpatched web server has a vulnerability. Without an attacker trying to exploit it, no harm occurs.

**Exploit**: The action or code that takes advantage of a vulnerability. The relationship is: threat actor uses an exploit to exploit a vulnerability.

**Risk**: The probability that a threat will exploit a vulnerability and cause harm, combined with the magnitude of that harm. Risk is the intersection of threat, vulnerability, and impact.

The classic risk formula is: **Risk = Threat × Vulnerability × Impact**

Some frameworks simplify to: **Risk = Likelihood × Impact**

**Asset**: Anything of value that requires protection — hardware, software, data, people, processes, intellectual property, and reputation.

**Impact**: The magnitude of harm that would result if a threat successfully exploits a vulnerability. Impact is measured in terms of business consequence: financial loss, regulatory penalty, operational downtime, reputational damage.

**Likelihood (Probability)**: How probable it is that a given threat will exploit a given vulnerability within a defined time period.

---

## Section 2 — Qualitative Risk Analysis

**[SHOW SLIDE: 5x5 risk matrix — likelihood vs. impact]**

Risk analysis methods fall into two categories: qualitative and quantitative.

**Qualitative analysis** uses descriptive scales rather than precise numbers. Likelihood might be rated as Low, Medium, or High. Impact might be rated as Minor, Moderate, Major, or Critical. The results are plotted on a risk matrix.

A common qualitative matrix uses a 5x5 grid. The X-axis is likelihood (1 = Rare, 5 = Almost Certain). The Y-axis is impact (1 = Negligible, 5 = Catastrophic). Each cell in the matrix gets a risk score from 1 to 25. Risks scoring above a defined threshold are prioritized for treatment.

Qualitative analysis is faster and requires less data than quantitative analysis. It is useful for initial risk assessments, for communicating risk to non-technical stakeholders, and for comparing risks relative to each other when precise financial data is unavailable.

Its limitation is subjectivity — two people may rate the same risk differently. It also does not produce a dollar value, making it harder to build a cost-benefit case for specific controls.

---

## Section 3 — Quantitative Risk Analysis

**[SHOW SLIDE: Quantitative risk formula diagram — AV, EF, SLE, ARO, ALE]**

**Quantitative analysis** expresses risk in financial terms. This gives organizations a basis for comparing the cost of a control to the cost of the risk it reduces. The Security+ exam tests specific formulas.

**Asset Value (AV)**: The monetary value of the asset. For a database containing customer records, this might include the cost of data recovery, regulatory fines, customer notification, litigation, and reputational damage.

**Exposure Factor (EF)**: The percentage of the asset's value that would be lost if the threat occurred. If a ransomware attack would encrypt all data and cost 60 percent of the asset value to recover, the EF is 0.60 (60%).

**Single Loss Expectancy (SLE)**: The expected dollar loss from a single occurrence of the threat. The formula is:

```
SLE = AV × EF
```

If AV is $500,000 and EF is 0.60, then SLE = $300,000.

**Annual Rate of Occurrence (ARO)**: How many times per year the threat is expected to occur. If ransomware attacks on organizations of this type occur approximately once every two years, the ARO is 0.5.

**Annual Loss Expectancy (ALE)**: The expected annual dollar loss from the threat. The formula is:

```
ALE = SLE × ARO
```

If SLE is $300,000 and ARO is 0.5, then ALE = $150,000.

**Using ALE for Control Decisions**

ALE provides the basis for a cost-benefit analysis. If a security control costs $40,000 per year and reduces the ALE from $150,000 to $30,000, the control saves $120,000 in expected annual loss — far more than its cost. The control is economically justified.

If the control costs $160,000 per year and only reduces ALE by $120,000, it is not economically justified based on quantitative analysis alone.

---

## Section 4 — Mean Time Metrics

**[SHOW SLIDE: Mean time metrics diagram — MTBF, MTTF, MTTR, RTO, RPO]**

Two mean time metrics appear on Security+ in the context of risk and availability.

**MTBF (Mean Time Between Failures)**: For repairable systems, the average time between one failure and the next. A server with an MTBF of 8,760 hours is expected to fail once per year (8,760 hours = one year).

**MTTF (Mean Time to Failure)**: For non-repairable components (like hard drives), the expected lifespan before failure. After failure, the component is replaced rather than repaired.

**MTTR (Mean Time to Repair/Recover)**: The average time required to restore a failed system to operational status after a failure occurs.

These metrics feed into availability calculations and business continuity planning.

**RTO (Recovery Time Objective)**: The maximum acceptable time to restore a system or service after a disruption. Defined by business requirements, not technical capability.

**RPO (Recovery Point Objective)**: The maximum acceptable amount of data loss measured in time. If RPO is 4 hours, backups must occur at least every 4 hours so that no more than 4 hours of data is lost in a failure.

---

## Section 5 — Risk Appetite and Tolerance

**[SHOW SLIDE: Risk appetite vs. risk tolerance diagram]**

Two related terms define how much risk an organization is willing to accept.

**Risk appetite**: The broad-level amount and type of risk an organization is willing to accept in pursuit of its objectives. Risk appetite is a strategic decision made by leadership. A startup may have high risk appetite in technology adoption to move fast. A bank may have very low risk appetite for data breaches due to regulatory consequences.

**Risk tolerance**: The acceptable variation around the risk appetite. If a company's risk appetite accepts up to $500,000 in potential annual cyber loss, its risk tolerance might extend to $600,000 before response is required.

**Risk threshold**: The point at which risk becomes unacceptable and must be treated regardless of cost.

---

## Closing — Part 1

**[INSTRUCTOR ON CAMERA]**

We have covered the foundational vocabulary — threat, vulnerability, exploit, risk, impact, likelihood — and the two analysis approaches: qualitative with the risk matrix and quantitative with the AV/EF/SLE/ARO/ALE formulas.

The quantitative formulas are heavily tested on Security+. Make sure you can calculate SLE and ALE from given values and use ALE to justify a security control investment.

In Part 2 we cover risk response strategies — avoid, transfer, mitigate, and accept — the risk register, and Business Impact Analysis. See you in Part 2.

---

*End of Part 1*
