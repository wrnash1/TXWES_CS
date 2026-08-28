# Reading Guide: Module 04 — Risk Assessment and Analysis Techniques

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4315 &BULL; CYBERSECURITY GOVERNANCE, RISK & COMPLIANCE (GRC)</text>
    
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


## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

---

## Introduction

Module 04 covers the analytical techniques security professionals use to assess and measure risk. Where Module 03 established the frameworks that organize risk management programs, this module focuses on the methods practitioners apply within those frameworks to actually evaluate risk. Mastery of these techniques — particularly the ALE formula chain and the BIA metrics — is essential for the CISM exam and for practical risk management work.

---

## Section 1 — The Risk Assessment Process

Risk assessment is the activity within a risk management program that evaluates specific risks: their likelihood, their potential impact, and their overall significance. Most risk management frameworks — NIST RMF, ISO 31000, OCTAVE — include a risk assessment phase as a core component.

NIST SP 800-30 Revision 1 defines risk assessment as a process with four core activities.

First, prepare for the assessment: establish the purpose, scope, assumptions, and constraints. Second, conduct the assessment: identify threats and vulnerabilities, determine likelihood and impact, and calculate overall risk. Third, communicate results: share findings with decision makers in a format they can use. Fourth, maintain the assessment: keep it current as the environment changes.

The two primary analytical methods used within the assessment are qualitative and quantitative analysis.

---

## Section 2 — Qualitative Risk Analysis

### 2.1 Definition and Purpose

Qualitative risk analysis assigns descriptive ratings to likelihood and impact rather than numerical values. The output is a prioritized risk list using categories such as High, Medium, and Low — or similar ordinal scales. The primary tool is the risk matrix (also called a heat map or likelihood-impact matrix).

Qualitative analysis is appropriate when:

- Financial asset data is unavailable or unreliable
- The assessment scope is broad and a rapid initial prioritization is needed
- Stakeholders lack the statistical expertise needed to interpret quantitative outputs
- The organization is conducting a first-pass assessment to identify which risks warrant deeper quantitative analysis

### 2.2 The Risk Matrix

A risk matrix plots likelihood on one axis and impact on the other. The most common formats are 3×3 (Low/Medium/High for each axis) or 5×5 (five levels for each axis). Each cell in the matrix is assigned a risk priority.

| | Negligible Impact | Minor Impact | Moderate Impact | Major Impact | Critical Impact |
|---|---|---|---|---|---|
| Almost Certain | Medium | High | High | Critical | Critical |
| Likely | Low | Medium | High | High | Critical |
| Possible | Low | Low | Medium | High | High |
| Unlikely | Low | Low | Low | Medium | High |
| Rare | Low | Low | Low | Low | Medium |

Risks plotting in the upper-right (high likelihood, high impact) are the highest priority for treatment. Risks in the lower-left are candidates for acceptance with monitoring.

### 2.3 Assigning Ratings

The most common method for assigning qualitative ratings is facilitated expert elicitation — bringing together knowledgeable subject matter experts to discuss and agree on ratings through structured workshops. Common inputs include historical incident data, threat intelligence reports, industry benchmarks, and subject matter expert judgment.

A key quality control practice is calibration: ensuring that participants share a common understanding of what "Likely" or "Major" means in the organization's specific context. Without calibration, the same risk may receive different ratings from different analysts.

### 2.4 Strengths and Limitations

Strengths of qualitative analysis:

- Fast to complete — assessments can be conducted in days
- No financial data required
- Easy to communicate — heat maps are widely understood
- Accessible to non-technical stakeholders
- Suitable for broad initial assessment

Limitations of qualitative analysis:

- Subjective — ratings vary by analyst
- Ordinal scales cannot be mathematically compared (High is not "twice as bad" as Medium)
- Cannot directly justify financial investment in controls
- May not satisfy regulatory requirements for documented financial risk exposure

---

## Section 3 — Quantitative Risk Analysis

### 3.1 The ALE Formula Chain

Quantitative risk analysis expresses risk as an expected financial loss. The standard formula chain used in information security risk analysis is built on four variables.

**Asset Value (AV):** The monetary value assigned to the information asset at risk. This may represent replacement cost, revenue dependency, regulatory fine exposure, or a composite measure. Determining AV accurately is often the most challenging part of quantitative analysis.

**Exposure Factor (EF):** The percentage of the asset's value that would be lost if a specific risk event occurred. EF is expressed as a decimal between 0 and 1. An EF of 0.40 means 40% of the asset's value would be destroyed or compromised in the event.

**Single Loss Expectancy (SLE):** The expected monetary loss from a single occurrence of the risk event.

SLE = AV × EF

**Annualized Rate of Occurrence (ARO):** The estimated number of times the risk event is expected to occur in one year. This may be derived from historical data, threat intelligence, or expert estimation. An event expected once every five years has an ARO of 0.2. An event expected three times per year has an ARO of 3.

**Annualized Loss Expectancy (ALE):** The expected annual financial loss from this specific risk.

ALE = SLE × ARO

### 3.2 Worked Examples

**Example 1 — Server Theft:**

An organization has a laptop fleet valued at $2,000,000. Historical data shows that laptop theft affects approximately 5% of the fleet per incident (EF = 0.05). Theft incidents occur approximately four times per year (ARO = 4).

SLE = $2,000,000 × 0.05 = $100,000

ALE = $100,000 × 4 = $400,000 per year

A mobile device management and encryption solution costs $80,000 per year and would reduce the EF from 0.05 to 0.01 (because stolen encrypted laptops have minimal data exposure). The new ALE would be:

SLE (new) = $2,000,000 × 0.01 = $20,000

ALE (new) = $20,000 × 4 = $80,000

ALE reduction = $400,000 - $80,000 = $320,000 per year

Control cost = $80,000 per year

Net benefit = $320,000 - $80,000 = $240,000 per year — a clear investment justification.

**Example 2 — Ransomware:**

A database server has an asset value of $1,500,000. A ransomware attack would destroy 70% of the data (EF = 0.70). The organization estimates ransomware attacks occur once every two years (ARO = 0.5).

SLE = $1,500,000 × 0.70 = $1,050,000

ALE = $1,050,000 × 0.5 = $525,000 per year

### 3.3 Control Cost-Benefit Analysis

The ALE formula enables a straightforward control investment decision rule. A security control is cost-justified if the annual cost of the control is less than the ALE reduction it produces.

Formally: if (ALE before control) minus (ALE after control) is greater than the annual cost of the control, then the control investment is financially justified.

This calculation is called the Control Value Analysis or sometimes the Risk-Adjusted Return on Security Investment.

### 3.4 Strengths and Limitations

Strengths of quantitative analysis:

- Produces objective, defensible financial outputs
- Directly enables cost-benefit analysis for control investments
- Supports executive communication with dollar-denominated risk language
- Enables cross-risk prioritization on a common financial scale

Limitations of quantitative analysis:

- Requires accurate financial data that may be unavailable
- ARO estimates for rare events are uncertain and can be misleading
- Time-intensive — impractical for broad initial assessments
- False precision: precise dollar figures may imply more certainty than the underlying estimates warrant

> Exam Tip: The CISM exam frequently tests the ALE formula chain with calculation questions. Memorize SLE = AV × EF and ALE = SLE × ARO. Also know the control justification rule: invest if annual control cost is less than the reduction in ALE.

---

## Section 4 — Business Impact Analysis

### 4.1 Purpose and Scope

A Business Impact Analysis (BIA) is a systematic process for determining the operational and financial effects of disrupting critical business processes and the systems that support them. The BIA is the analytical foundation for business continuity planning (BCP) and disaster recovery planning (DRP).

The BIA shifts the focus of risk analysis from "what threats exist?" to "what would happen to the business if a critical function were unavailable?" This business-outcome orientation makes the BIA one of the most important communication tools between the security team and executive leadership.

### 4.2 Key BIA Metrics

**Maximum Tolerable Downtime (MTD):** The longest period a business function can be unavailable before the organization suffers unacceptable consequences — such as regulatory non-compliance, customer loss, financial insolvency, or mission failure. MTD is determined by business owners based on business impact, not by IT.

Also referred to as Maximum Tolerable Period of Disruption (MTPD) in ISO 22301 (Business Continuity Management).

**Recovery Time Objective (RTO):** The maximum time allowed to restore a business function or system following a disruption. RTO is a target, not a guarantee. RTO must always be set below MTD to allow a safety margin. If MTD is 24 hours, a prudent RTO might be 12 hours.

**Recovery Point Objective (RPO):** The maximum amount of data loss the organization can tolerate, measured in time. An RPO of 4 hours means that the organization can afford to lose at most 4 hours of transaction data. RPO drives backup frequency requirements — backups must occur at least as frequently as the RPO.

### 4.3 Metric Relationships Table

| Metric | Question It Answers | Set By | Drives |
|--------|-------------------|--------|--------|
| MTD | How long can we be down before we cannot recover? | Business owner | RTO and RPO targets |
| RTO | How fast must we restore service? | Business owner with IT input | Recovery architecture, failover strategy |
| RPO | How much data can we afford to lose? | Business owner with IT input | Backup frequency, replication strategy |

A critical relationship: RTO must be less than MTD. If the recovery target exceeds the maximum tolerable downtime, the organization will fail before it recovers.

### 4.4 BIA Process Steps

Step 1 — Identify business functions: Document all critical business processes, not just IT systems. Include operational, financial, regulatory, and customer-facing functions.

Step 2 — Identify dependencies: For each function, map the systems, data, personnel, facilities, and vendors it depends on to operate.

Step 3 — Assess disruption impact over time: Evaluate the impact of disruption at multiple time horizons — after 1 hour, 4 hours, 24 hours, 72 hours, 1 week. Many functions are tolerant of brief outages but catastrophically impacted by extended ones.

Step 4 — Assign MTD, RTO, and RPO: Based on the impact analysis, set formal recovery targets for each function. These targets become requirements.

Step 5 — Validate with business owners: Recovery targets must be reviewed and approved by the business owners who will be held accountable for them.

Step 6 — Document and maintain: BIA results are documented formally and reviewed annually or whenever significant business changes occur.

### 4.5 BIA Output Example

| Business Function | MTD | RTO | RPO | Priority |
|------------------|-----|-----|-----|----------|
| Online order processing | 4 hours | 1 hour | 15 minutes | Critical |
| Customer support call center | 24 hours | 8 hours | 4 hours | High |
| Accounts payable processing | 72 hours | 24 hours | 24 hours | Medium |
| Employee training portal | 2 weeks | 5 days | 24 hours | Low |

This table tells a clear story: the online order processing system requires the most robust recovery infrastructure because the business cannot tolerate more than four hours of downtime and can afford to lose only 15 minutes of transaction data.

---

## Section 5 — Threat Modeling

### 5.1 Purpose and Timing

Threat modeling is a structured technique for identifying, enumerating, and prioritizing potential threats to a system — particularly during the design phase. The core insight of threat modeling is that it is far less expensive to address security threats during design than to remediate them after deployment.

Threat modeling answers four questions: What are we building? What can go wrong? What are we going to do about it? Did we do a good enough job?

### 5.2 STRIDE

STRIDE is the most widely used threat modeling framework in practice, developed at Microsoft. It provides six categories of threats that can be systematically applied to any system element.

| Letter | Threat Category | Description | Violated Security Property |
|--------|----------------|-------------|---------------------------|
| S | Spoofing | Impersonating a user, system, or component | Authentication |
| T | Tampering | Unauthorized data modification | Integrity |
| R | Repudiation | Denying an action due to insufficient audit trail | Non-repudiation |
| I | Information Disclosure | Unauthorized data exposure | Confidentiality |
| D | Denial of Service | Disrupting system availability | Availability |
| E | Elevation of Privilege | Gaining unauthorized access level | Authorization |

### 5.3 STRIDE Application Process

The standard STRIDE process follows four steps.

First, create a Data Flow Diagram (DFD) that maps the system's data flows, processes, data stores, trust boundaries, and external entities.

Second, decompose the diagram into elements: external entities, processes, data flows, data stores.

Third, for each element, apply the STRIDE categories: which STRIDE threats apply to this element?

Fourth, for each identified threat, document the threat, its severity, and potential mitigations.

### 5.4 PASTA

PASTA — Process for Attack Simulation and Threat Analysis — is a seven-stage, risk-centric threat modeling methodology. Unlike STRIDE, which focuses on system design elements, PASTA takes a business-risk perspective, connecting technical threats to business impact.

The seven stages are:

1. Define objectives — understand the business and security objectives
2. Define technical scope — document the system architecture
3. Application decomposition — identify application components and data flows
4. Threat analysis — identify realistic threats using threat intelligence
5. Vulnerability and weakness analysis — identify vulnerabilities the threats could exploit
6. Attack enumeration and modeling — simulate attack paths
7. Risk and impact analysis — evaluate business impact and prioritize treatment

PASTA is more resource-intensive than STRIDE but produces more business-aligned outputs, making it suitable for high-value systems where detailed threat analysis is warranted.

### 5.5 Threat Modeling Output Integration

Threat modeling outputs — threat lists, attack scenarios, data flow diagrams — feed directly into the broader risk assessment process. Each identified threat becomes a risk scenario subject to qualitative or quantitative analysis. Threat model outputs also serve as inputs to security requirements definition, control selection, and penetration testing scope definition.

---

## Section 6 — Integrating the Techniques

In practice, organizations use all three analytical approaches in combination, applying each where its strengths are greatest.

Threat modeling is applied early, during system design, to ensure comprehensive threat identification.

Qualitative analysis is used for broad initial risk assessments, rapid prioritization, and communication with non-technical stakeholders.

Quantitative analysis (ALE) is applied to high-priority risks where investment justification is needed and financial data is available.

BIA is conducted for continuity and recovery planning, grounding all risk analysis in business impact.

The results of all four feed into the risk register — the organization's authoritative catalog of identified risks, their assessments, treatment decisions, and owners.

---

## Section 7 — Glossary

**ALE (Annualized Loss Expectancy):** Expected annual financial loss from a specific risk. ALE = SLE × ARO.

**ARO (Annualized Rate of Occurrence):** Estimated number of times a risk event will occur per year.

**BIA (Business Impact Analysis):** A process for determining the operational and financial effects of disrupting critical business functions.

**EF (Exposure Factor):** Percentage of asset value lost in a single risk event occurrence.

**MTD (Maximum Tolerable Downtime):** The longest a business function can be unavailable before suffering unacceptable consequences.

**PASTA:** Process for Attack Simulation and Threat Analysis — a seven-stage, risk-centric threat modeling methodology.

**Qualitative risk analysis:** Risk analysis using descriptive ratings (High/Medium/Low) rather than financial values.

**Quantitative risk analysis:** Risk analysis using financial values to estimate expected monetary loss.

**RPO (Recovery Point Objective):** Maximum acceptable data loss measured in time.

**RTO (Recovery Time Objective):** Maximum time allowed to restore a business function after disruption.

**SLE (Single Loss Expectancy):** Expected monetary loss from a single occurrence of a risk event. SLE = AV × EF.

**STRIDE:** A threat modeling framework categorizing threats as Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.

**Threat modeling:** A structured process for identifying and prioritizing potential threats to a system, especially during the design phase.

---

## Required Reading

- NIST SP 800-30 Rev. 1 — Chapter 3 (Core Risk Assessment Activities) and Appendix D (Threat Sources). Free at csrc.nist.gov.
- NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems, Chapter 3 (Business Impact Analysis). Free at csrc.nist.gov.
- Microsoft STRIDE Threat Modeling documentation — available free through Microsoft Security documentation.

---

## Study Checklist

- [ ] Write out the ALE formula chain from memory: AV, EF, SLE, ARO, ALE
- [ ] Work through both ALE calculation examples without looking at the solutions
- [ ] Define MTD, RTO, and RPO and explain the relationship between them
- [ ] List all six STRIDE threat categories and the security property each violates
- [ ] Explain in one paragraph when qualitative analysis is preferable to quantitative
- [ ] Proceed to the Module 04 Lab Activity

---

## 9. Supplemental Resources

**NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments**
URL: https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final
Description: Free NIST publication providing comprehensive guidance on risk assessment methodology including threat source and event catalogs, likelihood and impact determination, and risk determination. Appendix D contains a detailed threat source catalog directly applicable to the qualitative and quantitative techniques covered in this module.

**Microsoft STRIDE Threat Modeling Documentation**
URL: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
Description: Microsoft's free documentation on the STRIDE threat modeling methodology, including descriptions of each threat category, the security property each violates, and examples of STRIDE applied to modern application architectures. The Microsoft Threat Modeling Tool is available as a free download for hands-on practice.

**NIST SP 800-34 Rev. 1 — Contingency Planning Guide, Chapter 3: Business Impact Analysis**
URL: https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final
Description: Free NIST publication with the most comprehensive government-published guidance on Business Impact Analysis methodology. Chapter 3 covers BIA planning, data collection, critical resource identification, and the establishment of MTD, RTO, and RPO values — directly aligned with the BIA content in this module.
