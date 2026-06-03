# Video Script: Module 13 — Risk Management (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 13 | Texas Wesleyan University"]**

---

## Opening — Part 2

**[INSTRUCTOR ON CAMERA]**

Welcome back to Module 13. In Part 1 we built the risk vocabulary and covered qualitative and quantitative analysis. In Part 2 we cover what you do with the analysis: risk response strategies, the risk register, and Business Impact Analysis.

---

## Section 1 — Risk Response Strategies

**[SHOW SLIDE: Four risk response strategies — quadrant diagram]**

Once you have identified and analyzed a risk, you must decide what to do about it. The Security+ exam tests four risk response strategies, and you need to be able to identify which strategy is being described in a scenario question.

**Risk Avoidance**

Risk avoidance means eliminating the risk by discontinuing the activity that creates it. If an organization runs a legacy application with unacceptable vulnerability to ransomware, retiring the application removes the risk entirely.

Avoidance is the most complete risk response — it eliminates the threat rather than reducing it. The cost is losing the business capability the activity provided. Avoidance is appropriate when the residual risk after other treatment exceeds the organization's risk tolerance and the activity is not essential.

**Risk Transference**

Risk transference shifts the financial impact of a risk to a third party. Cyber insurance is the most common form of risk transference in cybersecurity. The organization still bears the operational impact of an incident, but insurance compensates the financial loss.

Outsourcing is another form of transference — if a third-party cloud provider hosts data, the contract may transfer some liability for breaches to the provider.

Risk transference does not eliminate the risk — it redistributes the financial consequence.

**Risk Mitigation**

Risk mitigation reduces the likelihood or impact of a risk to an acceptable level. Installing a firewall, deploying MFA, encrypting data, and patching vulnerabilities are all mitigation controls.

Mitigation is the most common response in a functioning security program. It accepts that some risk remains — called residual risk — but reduces it to within the organization's risk tolerance.

**Risk Acceptance**

Risk acceptance means acknowledging that a risk exists and deciding not to take additional action to address it, either because the cost of treatment exceeds the value of the asset, or because the risk is within the organization's risk tolerance.

Acceptance should always be a documented, conscious decision — not the default outcome of not having a risk program. Formal acceptance documents the risk, the rationale for acceptance, and the executive who approved the decision. This is important for audit and compliance purposes.

A special form of acceptance is **risk ignorance** — the organization is unaware of the risk. This is not acceptance — it is a failure of the risk identification process.

---

## Section 2 — Residual Risk and Control Risk

**[SHOW SLIDE: Risk reduction layers diagram]**

After applying controls, some risk remains. This is called **residual risk**. No control eliminates risk completely. The security program's goal is to reduce risk to within the organization's risk tolerance through a combination of avoidance, transference, and mitigation, with formal acceptance of whatever remains.

**Inherent risk** is the risk that exists before any controls are applied. A company with an internet-facing database has inherent risk of SQL injection. After implementing a WAF, parameterized queries, and least-privilege database accounts, the residual risk is much lower.

**Control risk** is the risk that a control fails to operate as intended. A backup system that has never been tested introduces control risk — the backup may exist, but there is no evidence it would successfully restore data. Control effectiveness must be periodically tested and verified.

---

## Section 3 — The Risk Register

**[SHOW SLIDE: Sample risk register table]**

A risk register is the central document of the risk management program. It is a structured record of all identified risks, their analysis, their assigned owners, and their treatment status.

A risk register typically contains these fields for each identified risk:

- **Risk ID**: A unique identifier for each risk entry.
- **Risk Description**: A clear statement of the risk — what could happen, due to what cause.
- **Category**: Operational, technical, financial, regulatory, reputational.
- **Asset(s) Affected**: Which systems, data, or processes are at risk.
- **Threat Source**: The threat actor or event type.
- **Vulnerability**: The weakness being exploited.
- **Likelihood**: Qualitative (H/M/L) or quantitative (ARO).
- **Impact**: Qualitative or quantitative (ALE).
- **Risk Score**: Likelihood × Impact.
- **Risk Response**: Avoid, transfer, mitigate, or accept.
- **Controls in Place**: Existing controls already reducing this risk.
- **Residual Risk**: Risk remaining after existing controls.
- **Risk Owner**: The person accountable for managing this risk.
- **Due Date**: When the treatment is expected to be implemented.
- **Status**: Open, in progress, closed.

The risk register is reviewed and updated on a regular cycle — quarterly for most organizations, more frequently in high-risk environments. It is the primary tool for risk communication with leadership.

---

## Section 4 — Business Impact Analysis

**[SHOW SLIDE: BIA process diagram — criticality and dependency mapping]**

A Business Impact Analysis (BIA) identifies the critical business functions and processes that must be maintained during a disruption, and determines the impact if those functions are unavailable.

The BIA is the foundation of business continuity and disaster recovery planning. It answers: which systems and processes are most critical to the organization's survival, and how long can each be offline before the impact becomes catastrophic?

**BIA Process**

Step 1 — Identify business functions and processes. Every major business activity that the organization depends on.

Step 2 — Identify the IT systems and resources each function depends on. A customer payment process may depend on a payment gateway, a database, a web server, and a network connection.

Step 3 — Determine criticality for each function. Which functions, if disrupted, would immediately threaten revenue, safety, or compliance?

Step 4 — Establish maximum tolerable downtime (MTD) for each critical function. MTD is the maximum time a function can be offline before the organization suffers unacceptable harm. MTD feeds into RTO — the recovery target must be shorter than the MTD.

Step 5 — Establish RPO for each function. How much data loss is acceptable?

Step 6 — Identify dependencies and single points of failure. A system with no redundancy and a 1-hour MTD needs a very robust availability architecture.

**BIA Outputs**

The BIA outputs feed directly into continuity and recovery planning:

- A prioritized list of critical systems and processes.
- MTD, RTO, and RPO for each.
- Minimum resource requirements to sustain each critical function during a disruption.

---

## Section 5 — Privacy and Data Classification

**[SHOW SLIDE: Data classification levels — Confidential, Internal, Public]**

Risk management in security extends to data governance. Data classification is the process of categorizing data by sensitivity and assigning handling requirements.

Common classification levels in government: Top Secret, Secret, Confidential, Unclassified.

Common classification levels in commercial organizations: Confidential, Internal Use, Public. Some organizations add Restricted or Highly Confidential for the most sensitive data (PII, PHI, trade secrets, financial data).

Data classification drives risk decisions: confidential data requires stronger access controls, encryption, and audit logging than public data. The BIA should incorporate data classification — a database containing highly confidential customer PII will have a higher impact score and lower tolerance for downtime than a database containing marketing brochures.

---

## Section 6 — Third-Party Risk

**[SHOW SLIDE: Supply chain risk diagram — vendor, contractor, partner connections]**

Third-party risk is risk arising from the organization's relationships with vendors, partners, contractors, and service providers. Supply chain attacks — which we discussed in Module 10 — exploit this risk.

Third-party risk management involves:

- **Vendor risk assessments**: Evaluating the security posture of vendors before contracting and periodically afterward.
- **Contractual requirements**: Including security requirements, breach notification obligations, and audit rights in vendor contracts.
- **Right to audit**: Reserving the right to assess a vendor's security controls.
- **Due diligence**: Reviewing a vendor's certifications (SOC 2, ISO 27001), penetration test reports, and incident history.

The Security+ exam tests third-party risk in the context of supply chain security and vendor management.

---

## Closing

**[INSTRUCTOR ON CAMERA]**

Risk management is the language that connects technical security to business decision-making. Threats and vulnerabilities are technical realities — but their business significance is measured in likelihood, impact, ALE, and risk tolerance.

For Security+: know all four risk response strategies and be able to select the right one for a given scenario. Know the AV, EF, SLE, ARO, ALE formulas cold. Understand what a risk register contains and what a BIA produces. Know the difference between inherent and residual risk.

Complete the Reading Guide, Lab, Quiz, and Discussion for Module 13. You are approaching the end of this course — strong work. I'll see you in the next module.

---

*End of Part 2*
