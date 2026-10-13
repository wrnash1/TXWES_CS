# Reading Guide: Module 13 — Risk Management for Security+

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports the Module 13 video lectures on risk management. Risk management content permeates the Security+ exam — it appears in scenario questions across all domains, not just Domain 5 (Governance, Risk, and Compliance). Mastery of risk vocabulary and analysis techniques is essential for exam success and professional practice.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Apply the risk formula (Threat × Vulnerability × Impact) to analyze scenarios
2. Distinguish among risk appetite, risk tolerance, risk threshold, inherent risk, and residual risk
3. Apply all four risk response strategies to given scenarios
4. Perform a basic quantitative risk analysis (AV, EF, SLE, ARO, ALE) and cost-benefit analysis
5. Construct a qualitative risk matrix and rate risks using it
6. Describe the components of a risk register and the purpose of risk ownership
7. Explain the Business Impact Analysis and derive MTD, RTO, and RPO requirements
8. Classify security controls by both function (preventive, detective, corrective, deterrent, compensating, directive) and type (technical, administrative, physical)

---

## Assigned Readings (Zero-Cost / Open Access)

### Primary Reading

**NIST SP 800-30 Revision 1 — Guide for Conducting Risk Assessments**

- Publisher: National Institute of Standards and Technology
- Access: [https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final)
- Read: Chapter 2 (Fundamentals of Risk Assessment), Chapter 3 (Process for Conducting Risk Assessments), and Appendix G (Likelihood of Occurrence Values)
- Focus areas: risk assessment components, threat and vulnerability identification, likelihood and impact rating scales

Estimated reading time: 45–60 minutes for assigned sections.

**NIST Cybersecurity Framework v1.1 — Executive Summary and Core**

- Access: [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)
- Read: Executive Summary and Framework Core overview (the five functions)
- Focus areas: Identify, Protect, Detect, Respond, Recover and how they map to security activities

### Supplemental Reading

**NIST SP 800-34 Revision 1 — Contingency Planning Guide for Federal Information Systems**

- Access: [https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
- Read: Chapter 2 (Developing the Contingency Planning Policy Statement and Conducting the Business Impact Analysis)
- Focus areas: BIA process, MTD, RTO, RPO derivation

**ISACA Risk IT Framework Overview**

- Access: [https://www.isaca.org/resources/isaca-journal/issues/2010/volume-2/the-risk-it-framework](https://www.isaca.org/resources/isaca-journal/issues/2010/volume-2/the-risk-it-framework)
- Read: Framework overview section
- Focus areas: risk governance, risk evaluation process

---

## Key Terms and Definitions

**Risk** — The potential for harm resulting from a threat exploiting a vulnerability; commonly expressed as the product of threat likelihood, vulnerability severity, and impact magnitude.

**Threat** — Any circumstance or event with the potential to harm an information system or organization; external to the organization and largely outside direct control.

**Vulnerability** — A weakness in a system, control, or process that a threat can exploit; internal to the organization and within the security team's influence.

**Impact** — The magnitude of harm that would result if a threat successfully exploited a vulnerability; measured in terms of confidentiality, integrity, availability, financial, reputational, and regulatory dimensions.

**Risk Appetite** — The level of risk an organization is prepared to accept in pursuit of its objectives, expressed as a policy statement or threshold.

**Risk Tolerance** — The acceptable variation around the risk appetite; the degree of uncertainty the organization can withstand.

**Risk Threshold** — The point at which a risk level triggers mandatory treatment; risks above the threshold require a response.

**Inherent Risk** — The level of risk present in the absence of any controls.

**Residual Risk** — The risk remaining after controls have been applied; equals inherent risk minus risk reduction from controls.

**Risk Avoidance** — A risk response strategy that eliminates the activity creating the risk.

**Risk Transference** — A risk response strategy that shifts the financial impact of a risk to another party, typically through cyber insurance or contractual provisions.

**Risk Mitigation** — A risk response strategy that applies controls to reduce likelihood, vulnerability, or impact.

**Risk Acceptance** — A risk response strategy that acknowledges a risk and consciously decides not to apply additional controls; must be formally documented.

**Risk Register** — A document that records all identified risks, their assessments, owners, response strategies, and treatment status.

**Risk Owner** — The individual responsible for managing a specific risk; typically the owner of the affected asset or business process.

**AV (Asset Value)** — The monetary value assigned to an asset.

**EF (Exposure Factor)** — The percentage of asset value lost in a specific threat scenario; expressed as a decimal (0.0–1.0).

**SLE (Single Loss Expectancy)** — The expected financial loss from a single occurrence of a threat; calculated as AV × EF.

**ARO (Annual Rate of Occurrence)** — The expected frequency of a threat occurring per year; an ARO of 0.5 means once every two years.

**ALE (Annual Loss Expectancy)** — The expected annual financial loss from a specific threat; calculated as SLE × ARO.

**Risk Matrix** — A qualitative risk analysis tool that maps likelihood against impact to produce a risk rating.

**BIA (Business Impact Analysis)** — A process that identifies critical business functions and determines the impact of disruptions, establishing MTD, RTO, and RPO requirements.

**MTD (Maximum Tolerable Downtime)** — The longest period a business function can be unavailable before catastrophic consequences result.

**RTO (Recovery Time Objective)** — The target time to restore a function after a disruption; must be less than the MTD.

**RPO (Recovery Point Objective)** — The maximum acceptable data loss measured in time; drives backup frequency requirements.

**MTBF (Mean Time Between Failures)** — The average time between system failures; a measure of reliability.

**Preventive Control** — A security control that stops a threat from being realized; reduces likelihood or vulnerability.

**Detective Control** — A security control that identifies a threat event as it occurs or has occurred.

**Corrective Control** — A security control that limits damage and restores normal operations after a threat event.

**Deterrent Control** — A security control that discourages threat actors from attempting an attack.

**Compensating Control** — An alternative control used when the primary control is not feasible; must provide equivalent or acceptable protection.

**Directive Control** — A control implemented through policies and procedures that direct human behavior.

**Technical Control** — A control implemented through technology (firewalls, encryption, access control systems).

**Administrative Control** — A control implemented through management processes (policies, training, background checks).

**Physical Control** — A control implemented through physical security measures (locks, guards, barriers).

**NIST RMF** — NIST Risk Management Framework (SP 800-37); a six-step process for managing risk in information systems: Categorize, Select, Implement, Assess, Authorize, Monitor.

**NIST CSF** — NIST Cybersecurity Framework; organizes cybersecurity activities into five functions: Identify, Protect, Detect, Respond, Recover.

---

## Concept Deep Dives

### Quantitative Risk Analysis — Worked Example

Scenario: A financial services company stores customer credit card data on a database server.

- **Asset Value (AV):** $2,000,000 (estimated value of the data and system)
- **Threat:** SQL injection attack leading to data breach
- **Exposure Factor (EF):** 0.40 (40% of data expected to be compromised)
- **SLE** = AV × EF = $2,000,000 × 0.40 = **$800,000**
- **Annual Rate of Occurrence (ARO):** 0.25 (once every four years based on industry data)
- **ALE** = SLE × ARO = $800,000 × 0.25 = **$200,000**

A Web Application Firewall costs $30,000/year and is expected to reduce ARO from 0.25 to 0.05.

- New ALE after WAF = $800,000 × 0.05 = $40,000
- ALE reduction = $200,000 − $40,000 = $160,000/year
- WAF cost = $30,000/year
- Net annual benefit = $160,000 − $30,000 = **$130,000/year**

The WAF provides a strong positive ROI. This is the quantitative justification for the security investment.

### Security Controls Classification Matrix

Practice classifying controls using both dimensions:

| Control | Function | Type |
|---|---|---|
| Firewall | Preventive | Technical |
| IDS/IPS | Detective | Technical |
| Incident response plan | Corrective | Administrative |
| Security camera | Detective + Deterrent | Physical |
| Acceptable use policy | Directive | Administrative |
| Encryption at rest | Preventive | Technical |
| Backup and restore | Corrective | Technical |
| Badge access control | Preventive | Physical |
| Security awareness training | Preventive + Directive | Administrative |
| Warning banners | Deterrent + Directive | Technical/Administrative |
| Jump server for legacy system | Compensating | Technical |

---

## Security+ Exam Alignment

### Relevant Exam Objectives (SY0-701)

- **5.1** — Summarize elements of effective security governance (risk appetite, risk register, risk tolerance)
- **5.2** — Explain elements of the risk management process (risk identification, analysis, response, monitoring)
- **5.4** — Summarize elements of effective security compliance (third-party risk, agreements)

### High-Probability Exam Topics from This Module

- Calculating ALE from given AV, EF, and ARO values (the arithmetic is consistently tested)
- Identifying the correct risk response strategy for a described scenario
- Distinguishing risk tolerance from risk appetite
- Classifying a described control by both function and type
- Identifying which BIA metric is violated when a described recovery plan fails to meet business requirements
- Knowing that RTO must be less than MTD
- Knowing that RPO drives backup frequency

### Common Exam Traps

- **"Risk avoidance" vs. "risk acceptance"** — Avoidance = don't do the activity. Acceptance = acknowledge and don't treat the risk further. Confusing these is a common error.
- **"Deterrent" vs. "preventive"** — Deterrent discourages; preventive prevents. Security cameras deter; badge readers prevent.
- **Residual vs. inherent risk** — Inherent is before controls; residual is after controls.
- **RTO vs. RPO** — RTO is about time to restore; RPO is about data loss tolerance.

---

## Review Questions (Self-Check — Not Graded)

1. A company's database server holds 100,000 customer records valued at $500 each. A ransomware attack is expected to destroy 30% of the data. This attack occurs approximately once every five years. Calculate: AV, EF, SLE, ARO, and ALE.

2. A security team recommends implementing network segmentation at a cost of $80,000/year. The team estimates it would reduce the ALE from the ransomware scenario in Question 1 by 70%. Calculate whether this control provides a positive ROI.

3. An organization's risk appetite statement says: "We will not accept risks that could result in regulatory fines exceeding $1,000,000." A risk assessment identifies a GDPR compliance gap with an estimated annual risk of $750,000. What is the appropriate risk response and why?

4. A hospital's e-records system has an MTD of 8 hours. Their current disaster recovery plan promises an RTO of 10 hours. What is the problem and what must happen?

5. An organization cannot install security patches on a critical industrial control system because patches require extended downtime that the manufacturing process cannot tolerate. They instead implement a separate monitoring system that alerts on anomalous traffic to the ICS. What type of control (by function and type) has been implemented, and why is it classified this way?

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 13*
