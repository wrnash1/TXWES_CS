# Reading Guide: Module 14 — Risk and Compliance in IT Service Management

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4335 &BULL; IT SERVICE MANAGEMENT & ITIL FRAMEWORKS</text>
    
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


## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

This reading guide accompanies Module 14 on Risk and Compliance. Risk management is woven throughout ITIL 4 — it is not a standalone practice but a lens applied across every other practice. This guide builds your understanding of risk concepts, regulatory frameworks, and the operational discipline of maintaining compliance.

**Estimated reading and reflection time:** 90–120 minutes

---

## Learning Objectives

After completing this module, you will be able to:

1. Define risk within the ITIL 4 context and distinguish threat risks from opportunity risks.
2. Build and maintain a risk register with all required components.
3. Apply the four risk response strategies appropriately to given scenarios.
4. Explain how ISO 27001 structures an ISMS and its key requirements.
5. Describe SOC 2 Trust Services Criteria and the difference between Type I and Type II reports.
6. Prepare a compliance audit evidence package using ITIL practice outputs.
7. Identify failure patterns in compliance programs and describe sustainable alternatives.

---

## Section 1: Foundations of Risk Management

### 1.1 ITIL 4 Risk Definition and Scope

ITIL 4 defines risk as "a possible event that could cause harm or loss, or make it more difficult to achieve objectives." This is deliberately broad.

**Upside risks vs. downside risks:**

Most people instinctively associate risk with negative outcomes — a server fails, data is stolen, a deployment causes an outage. These are **threat risks** (downside risks). But risk management frameworks, including those aligned with ISO 31000 (the international risk management standard), also recognize **opportunity risks** (upside risks) — situations where uncertainty could produce unexpected positive outcomes.

Example: Adopting a new cloud platform carries both threat risks (migration failure, cost overrun) and opportunity risks (faster provisioning, global reach, elastic scaling beyond what the current infrastructure allows). A complete risk assessment considers both.

**Why organizations under-invest in risk management:**

Risk management requires investing resources today to prevent costs that might occur in the future — and might not occur at all. This creates a classic under-investment dynamic: organizations that successfully manage risks see no disasters, and leaders may question why they are spending on "prevention" that appears to produce nothing visible. Effective risk communication must make invisible protection visible.

### 1.2 Risk Management Standards

ITIL 4 does not prescribe a specific risk management methodology. Organizations can adopt:

- **ISO 31000:** International risk management standard providing principles and guidelines.
- **NIST Risk Management Framework (RMF):** U.S. federal standard, widely adopted in regulated industries.
- **FAIR (Factor Analysis of Information Risk):** Quantitative risk modeling methodology that translates risk into financial terms.
- **COBIT:** Governance framework that includes risk management components.
- **COSO ERM:** Enterprise risk management framework widely used in finance and accounting.

The specific framework matters less than having a consistent, documented, and enforced approach.

---

## Section 2: The Risk Register

### 2.1 Risk Identification

Before risks can be managed, they must be identified. Risk identification techniques include:

**Brainstorming sessions:** Cross-functional teams explore potential risks using "what could go wrong?" prompts. Diverse participants surface risks that siloed experts miss.

**Risk workshops:** Structured facilitated sessions using risk taxonomy frameworks (categories like technology risk, people risk, regulatory risk) to ensure comprehensive coverage.

**Incident analysis:** Past incidents are rich sources of future risk intelligence. What happened once can happen again — and known failure modes should be documented as risks to prevent recurrence.

**Threat intelligence:** External threat data (industry security reports, government advisories, vendor vulnerability disclosures) identifies emerging risks before they materialize internally.

**Audit findings:** Internal and external audit findings identify control gaps — control gaps are risks.

**Process analysis:** Mapping value streams and processes often reveals single points of failure, manual handoffs prone to error, or dependencies on specific individuals (key person risk).

### 2.2 Risk Assessment

After identification, each risk is assessed for two dimensions:

**Likelihood assessment:** How probable is it that this risk will materialize in a given time period? Qualitative scales (Low/Medium/High) are simpler to apply; quantitative scales (1–5 or percentage probabilities) enable more precise prioritization.

**Impact assessment:** If the risk materializes, how severe will the consequences be? Consider financial impact, reputational damage, regulatory penalty, service disruption, and safety implications.

**Risk score = Likelihood × Impact.** A risk with Medium likelihood (3) and High impact (5) scores 15. A risk with High likelihood (5) and Low impact (1) scores 5. This allows the risk register to be sorted and prioritized.

**Risk heat map:** Organizations often visualize the risk portfolio on a 5×5 matrix plotting likelihood (Y axis) against impact (X axis). Risks in the upper-right quadrant (high likelihood, high impact) are the highest priority.

### 2.3 Risk Register Components

A complete risk register entry contains:

| Field | Description |
|---|---|
| Risk ID | Unique identifier (e.g., RISK-2024-0042) |
| Risk statement | If [event], then [consequence], which affects [objective] |
| Category | Technology / Operational / Regulatory / Financial / Reputational / People |
| Likelihood | 1 (Very Low) to 5 (Very High) |
| Impact | 1 (Negligible) to 5 (Catastrophic) |
| Risk score | Likelihood × Impact |
| Risk owner | Named accountable individual |
| Existing controls | Controls currently in place |
| Control effectiveness | Are current controls working? (Strong / Moderate / Weak) |
| Residual risk score | Risk score after current controls applied |
| Response strategy | Avoid / Transfer / Mitigate / Accept |
| Action plan | Specific steps, owners, due dates |
| Target residual score | Desired risk level after mitigation actions |
| Review date | Next scheduled reassessment |
| Status | Open / In Progress / Accepted / Closed |

**Risk statement format:** The "if/then/affects" format is recommended because it forces specificity. Vague risk descriptions like "cybersecurity risk" are unactionable. A well-formed statement: "If an employee clicks a phishing link and credentials are stolen, then an attacker could gain unauthorized access to the financial system, which affects the confidentiality and integrity of customer financial data."

### 2.4 Risk Response Strategies in Depth

**Avoid:**

Risk avoidance means eliminating the activity that creates the risk. This is the most complete response but not always feasible — some risks are intrinsic to operating a business.

Example: A company decides not to store customer credit card numbers at all — they use a tokenization service so the actual card data never touches their systems. This avoids PCI DSS scope for card data storage entirely.

**Transfer:**

Risk transfer shifts the financial consequence to a third party. Common transfer mechanisms:

- **Cyber insurance:** Provides financial coverage for breach costs, regulatory fines, and incident response.
- **Contractual transfer:** Agreements that make a vendor or partner liable for incidents caused by their systems or services.
- **Outsourcing:** Moving a function to a managed service provider who contractually accepts responsibility for service levels and security.

Note: Risk transfer does not eliminate the risk — it changes who bears the financial consequence. Reputational damage from a data breach remains with the organization even if the financial costs are insured.

**Mitigate:**

Mitigation reduces likelihood, reduces impact, or both. Most security and operational controls are mitigation strategies.

- **Likelihood reduction:** Multi-factor authentication reduces the likelihood of account compromise.
- **Impact reduction:** Regular backups reduce the impact of ransomware attacks (data can be restored).
- **Both:** Incident response plans reduce the time to detect and contain a breach, reducing both likelihood of extended exposure and impact magnitude.

**Accept:**

Risk acceptance is not negligence — it is a deliberate, documented decision that the cost of mitigation exceeds the risk's expected impact. Requirements for valid risk acceptance:

- The risk is formally documented in the register.
- The residual risk level is explicitly stated.
- An appropriate authority (typically management or the risk committee) reviews and signs off on the acceptance.
- An acceptance expiry date is set — accepted risks must be periodically re-evaluated.

---

## Section 3: ISO 27001

### 3.1 Structure and Scope

ISO/IEC 27001 uses the same high-level structure (Annex SL) as other ISO management system standards (ISO 9001 for quality, ISO 22301 for business continuity), making it easier to integrate into organizations that hold multiple ISO certifications.

**Core requirements (Clauses 4–10):**

- **Clause 4:** Context — understand the organization, its stakeholders, and the ISMS scope.
- **Clause 5:** Leadership — management commitment, security policy, and assigned roles.
- **Clause 6:** Planning — risk assessment, risk treatment, and security objectives.
- **Clause 7:** Support — resources, competence, awareness, communication, and documented information.
- **Clause 8:** Operation — executing risk treatment plans and operational security controls.
- **Clause 9:** Performance evaluation — monitoring, measurement, internal audit, and management review.
- **Clause 10:** Improvement — corrective actions and continual improvement.

### 3.2 Risk Assessment and Treatment in ISO 27001

ISO 27001 requires organizations to conduct a documented information security risk assessment that:

- Defines criteria for acceptable risk levels.
- Identifies information assets and the threats and vulnerabilities applicable to each.
- Analyzes likelihood and consequence of identified risks.
- Evaluates risk against the acceptance criteria.

The risk treatment plan must document which Annex A controls were selected for each risk and why. Controls not selected must be justified in a "Statement of Applicability" (SoA).

### 3.3 Annex A Controls (2022 Edition)

ISO 27001:2022 contains 93 controls across four themes:

- **Organizational (37 controls):** Policies, roles, responsibilities, asset management, supplier security, incident management.
- **People (8 controls):** Screening, training, disciplinary process, remote working security.
- **Physical (14 controls):** Physical perimeter security, equipment maintenance, secure disposal.
- **Technological (34 controls):** Access control, endpoint security, cryptography, network security, application security, monitoring.

### 3.4 Certification Process

1. **Gap assessment:** Current state vs. ISO 27001 requirements.
2. **Remediation:** Address identified gaps.
3. **Stage 1 audit (document review):** Certification body reviews documentation for completeness.
4. **Stage 2 audit (on-site):** Auditors verify that documented processes are operating in practice.
5. **Certification granted:** Valid for 3 years.
6. **Surveillance audits:** Annual audits in years 1 and 2 verify continued compliance.
7. **Recertification:** Full audit in year 3.

---

## Section 4: SOC 2

### 4.1 Purpose and Applicability

SOC 2 was developed specifically for technology service providers who store, process, or transmit customer data. The SOC 2 framework addresses the risk that a service provider's systems could compromise customer data security, availability, or privacy.

**Who needs SOC 2:**

- Cloud infrastructure providers (IaaS, PaaS, SaaS).
- Managed service providers with access to customer systems.
- Data centers co-locating customer hardware.
- Healthcare IT vendors processing protected health information.
- Financial technology companies processing payment or account data.

### 4.2 Trust Services Criteria Deep Dive

**Security (CC — Common Criteria):** All SOC 2 reports must include Security. Controls cover: logical and physical access controls, system monitoring, change management, risk assessment, and incident response.

**Availability:** Focuses on whether the system is available for use as committed. Controls include: performance monitoring, capacity planning, disaster recovery, and backup/restore testing.

**Processing Integrity:** Ensures transactions are complete, accurate, timely, and authorized. Critical for financial transaction processors, e-commerce platforms, and data pipelines.

**Confidentiality:** Protects information designated as confidential throughout its lifecycle. Controls include: encryption, access restrictions, NDA enforcement with vendors, and secure data deletion.

**Privacy:** Based on AICPA's Generally Accepted Privacy Principles (GAPP). Covers notice, choice and consent, collection, use and retention, access, disclosure, security, quality, and monitoring.

### 4.3 SOC 2 vs. ISO 27001

| Dimension | ISO 27001 | SOC 2 |
|---|---|---|
| Geographic focus | Global | Primarily U.S. and global B2B |
| Issuing body | ISO / IEC | AICPA |
| Output | Certification | Attestation report |
| Scope | Organization-wide ISMS | Specific system/service |
| Audit frequency | Annual surveillance + triennial recert | Typically annual (Type II) |
| Report sharing | Public certification status | Report shared under NDA with customers |
| Primary use case | General security credentialing | B2B vendor assurance |

---

## Section 5: Audit Preparation

### 5.1 Evidence Collection Strategy

The best audit preparation is continuous — organizations that run well-governed ITIL processes are always audit-ready. Evidence collection should not be a pre-audit scramble.

**Automated evidence collection:** Configure systems to automatically capture and retain logs, access reports, change records, and configuration states. Many ITSM platforms generate audit trails natively.

**Evidence repository:** Maintain a structured repository (often a shared drive or GRC platform) organized by control domain. When an auditor requests evidence, the response should take hours, not weeks.

**Control mapping:** For each regulatory requirement, document which technical or process control satisfies it and where the evidence can be found. This mapping is the foundation of the compliance program.

### 5.2 Common Audit Requests

When preparing for a SOC 2 or ISO 27001 audit, expect requests for:

- Last 12 months of change management records with approvals.
- Access control reviews (periodic reviews of who has access to what).
- Vulnerability scan results and remediation evidence.
- Incident log with response timelines.
- Training completion records.
- Vendor security assessment documentation.
- Business continuity and disaster recovery test results.
- Management review minutes documenting risk register reviews.

### 5.3 Internal Audit Practice

Internal audits are dry runs — they identify gaps before external auditors do. An effective internal audit program:

- Follows a documented audit schedule covering all controls at defined frequencies.
- Uses objective internal auditors (not the team whose work is being audited).
- Produces formal findings with severity ratings and remediation deadlines.
- Tracks corrective action completion.
- Reports results to senior management.

---

## Key Vocabulary

- **Risk** — possible event causing harm, loss, or difficulty achieving objectives.
- **Risk register** — documented record of risks, scores, owners, responses, and actions.
- **Likelihood** — probability of risk occurrence.
- **Impact** — severity of consequences if risk occurs.
- **Risk exposure** — likelihood × impact score.
- **Risk response** — Avoid, Transfer, Mitigate, Accept.
- **Residual risk** — risk level remaining after controls applied.
- **ISO 27001** — international ISMS standard.
- **ISMS** — Information Security Management System.
- **Annex A controls** — 93 security controls in ISO 27001:2022.
- **SOC 2** — AICPA service organization control standard.
- **Trust Services Criteria** — Security, Availability, Processing Integrity, Confidentiality, Privacy.
- **SOC 2 Type I** — point-in-time control design assessment.
- **SOC 2 Type II** — period operational effectiveness assessment.
- **Statement of Applicability (SoA)** — ISO 27001 document justifying control selections.
- **Control mapping** — linking regulatory requirements to controls and evidence.
- **Compliance theater** — appearance of compliance without operational reality.

---

## Self-Check Questions

1. What is the difference between a threat risk and an opportunity risk? Give one IT example of each.
2. Write a well-formed risk statement using the if/then/affects format for a risk of your choice.
3. When is risk acceptance appropriate? What conditions must be met for valid acceptance?
4. What is the difference between SOC 2 Type I and Type II? Which provides stronger assurance to a customer?
5. How do ITIL practices naturally generate audit evidence? Give three specific examples.

---

*End of Module 14 Reading Guide — approximately 265 lines*
