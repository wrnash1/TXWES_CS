# Reading Guide: Module 14 — Risk and Compliance in ITSM

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

Risk and compliance are not separate disciplines layered on top of IT service management — they are woven into it. Every change request includes a risk assessment. Every incident has a compliance dimension when sensitive data is involved. Every asset that is deployed or disposed of creates audit evidence. This module connects the risk and compliance frameworks that govern real-world IT organizations to the ITIL 4 practices you have been studying throughout this course.

Use this guide alongside the Module 14 video lecture and ITIL 4 Foundation study resources.

---

## Risk in ITSM

### ITIL 4 Definition of Risk

ITIL 4 defines risk as a possible event that could cause harm or loss, or affect the ability to achieve objectives. Risk has two defining characteristics:

- **Likelihood** — how probable is the event
- **Impact** — how severe would the consequences be

Risk exposure is typically expressed as the product of likelihood and impact. A low-likelihood, high-impact risk may warrant more attention than a high-likelihood, low-impact risk, depending on the specific nature of the impact.

### Risk Responses

When a risk is identified and assessed, the organization must decide how to respond. ITIL 4 recognizes four risk response strategies:

| Response | Description | When to Use |
|---|---|---|
| Avoid | Eliminate the activity or condition that creates the risk | When the risk exceeds acceptable tolerance and the activity is not essential |
| Mitigate | Implement controls that reduce likelihood, impact, or both | Most common response — reduces risk to an acceptable level |
| Transfer | Shift the financial consequences to another party (e.g., insurance, contracts) | When financial impact is the primary concern and the risk cannot be eliminated |
| Accept | Acknowledge the risk and take no further action | When the cost of control exceeds the value of risk reduction and risk is within tolerance |

### The Risk Register

A risk register is the central management tool for tracking identified risks. In ITSM, risk registers exist at multiple levels:

- **Service-level registers** track risks specific to individual services — availability risks, capacity risks, security risks
- **Project-level registers** track risks in change and improvement initiatives
- **Organizational registers** aggregate high-level strategic and operational risks for executive review

A risk register entry contains: risk description, category, likelihood score, impact score, risk score, risk owner, response strategy, controls in place, and residual risk level.

**Residual risk** is the risk that remains after controls are applied. No set of controls eliminates all risk — residual risk is what the organization accepts after implementing its chosen response.

### ITIL 4 Risk Integration

ITIL 4 does not treat risk as a standalone practice separate from service management — it embeds risk consideration throughout the Service Value System.

**Change Enablement** requires that every change be assessed for risk before authorization. The change model for each change type (standard, normal, emergency) defines the level of risk assessment required.

**Problem Management** analyzes the root causes of incidents and identifies the risks that vulnerabilities create if not addressed.

**Continual Improvement** evaluates the risk of proposed improvements — an improvement initiative can introduce new dependencies, temporary instability, or resource constraints.

**Service Level Management** identifies the risks to meeting SLA commitments — availability risks, capacity risks, third-party dependency risks.

---

## ISO 27001

### What Is ISO 27001?

ISO 27001 is the international standard for Information Security Management Systems (ISMS). It is published by the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC). An organization certified to ISO 27001 has demonstrated to an independent auditor that it has established, implemented, maintained, and continually improved an ISMS that meets the standard's requirements.

### The ISMS

An Information Security Management System is a management framework that defines how an organization:

- Identifies and assesses information security risks
- Selects and implements controls to address those risks
- Monitors and measures the effectiveness of those controls
- Continually improves the system based on measurement and review

The ISMS is not a technology product — it is a set of policies, processes, roles, and records that together constitute a systematic approach to managing information security.

### ISO 27001 Structure

ISO 27001 has two parts: the main body (Clauses 4–10) and Annex A.

**Clauses 4–10** contain the mandatory requirements for the ISMS — context, leadership, planning, support, operation, performance evaluation, and improvement. These clauses apply to every organization regardless of size or industry.

**Annex A** contains 114 controls organized into 14 domains. Organizations do not need to implement every control — they must document which controls they have selected and why in a document called the Statement of Applicability (SoA). Controls that are excluded must have a documented justification.

### Key Annex A Domains for ITSM

| Domain | Relevant ITSM Connection |
|---|---|
| A.8 — Asset Management | Maps to IT Asset Management practice |
| A.9 — Access Control | User account management, privileged access, access reviews |
| A.12 — Operations Security | Change management, malware protection, backup, logging |
| A.16 — Incident Management | Aligns with ITIL 4 Incident Management practice |
| A.15 — Supplier Relationships | Third-party access controls, vendor assessments |

### Risk Assessment Under ISO 27001

ISO 27001 requires a formal, documented risk assessment process. The key steps are:

1. Identify information assets and their owners
2. Identify threats to each asset (unauthorized access, data loss, system failure, natural disaster)
3. Identify vulnerabilities that each threat could exploit
4. Assess likelihood and impact for each threat-vulnerability combination
5. Calculate risk scores
6. Select controls from Annex A (or other sources) to address risks exceeding the organization's tolerance
7. Document all decisions in the risk treatment plan and Statement of Applicability

---

## SOC 2

### What Is SOC 2?

SOC 2 — System and Organization Controls 2 — is an auditing framework developed by the American Institute of Certified Public Accountants (AICPA). It is used by service organizations — cloud providers, SaaS companies, managed service providers, data processing firms — to demonstrate that their controls meet defined standards for protecting customer data.

SOC 2 evaluates controls against five Trust Services Criteria:

| Criterion | Description | Mandatory? |
|---|---|---|
| Security | Protection against unauthorized access | Yes |
| Availability | System availability for operation and use | No |
| Processing Integrity | Completeness and accuracy of processing | No |
| Confidentiality | Protection of confidential information | No |
| Privacy | Collection and use of personal information | No |

Security is the only mandatory criterion. Organizations select additional criteria based on their customer agreements and business context. A cloud infrastructure provider might include Availability; a company handling personal health data might include Privacy.

### Type I vs. Type II Reports

**SOC 2 Type I** evaluates whether the described controls are suitably designed at a specific point in time. It is a point-in-time snapshot.

**SOC 2 Type II** evaluates whether the controls operated effectively over a defined period — typically six to twelve months. It demonstrates sustained operational performance, not just design adequacy.

Most enterprise customers require SOC 2 Type II reports from their service providers because it provides evidence of consistent operation, not just design intent.

### SOC 2 and ITSM Evidence

SOC 2 auditors look for evidence that controls are operating consistently. ITIL 4 practices generate much of this evidence:

- **Change Management tickets** — evidence that changes are authorized before deployment (Security criterion)
- **Incident records** — evidence that security incidents are detected, logged, and resolved (Security criterion)
- **Deployment records** — evidence that software testing and approval gates are followed (Processing Integrity criterion)
- **Asset inventories** — evidence that systems processing customer data are identified and controlled (Security criterion)
- **User access reviews** — evidence that access to systems is regularly reviewed and revoked for departed users (Security criterion)

---

## Audit Evidence Collection

### What Auditors Look For

An audit is an independent assessment of whether controls meet a defined standard. Auditors look for evidence that:

1. Required policies and procedures exist and are formally approved
2. Controls described in policies are actually implemented
3. Controls are operating consistently — not just at audit time
4. Exceptions are identified, documented, and remediated

### Types of Audit Evidence

**System-generated logs** are the most credible evidence type because they are created automatically during operations. Examples include: change management ticket history showing approvals, access logs showing authentication events, deployment logs showing what was deployed and when, and backup completion records.

**Policy documents** demonstrate that required governance structures exist. Auditors verify that policies are current, formally approved, and distributed to relevant staff.

**Configuration exports** show the actual technical state of systems. A firewall rule export, a user account list, or an encryption setting report demonstrates that technical controls are implemented and not just documented.

**Staff interviews** verify that employees understand and follow policies. If a policy says all changes require CAB approval but staff consistently bypass the CAB for urgent changes, the interview will reveal the gap between policy and practice.

### Continuous Evidence Readiness

Organizations with mature compliance programs collect evidence continuously as a byproduct of normal operations. ITSM ticketing systems that record all changes, incidents, and service requests are continuously generating audit evidence. When an audit arrives, the evidence is organized and accessible — not assembled under pressure. This approach also enables proactive identification of control failures before they become audit findings.

---

## Gap Analysis

A gap analysis compares the organization's current control state against the requirements of a target standard. The output is a structured inventory of gaps — where required controls are absent, inadequately designed, or not demonstrably operating.

### Gap Analysis Process

1. Define the target standard (ISO 27001, SOC 2, PCI-DSS, HIPAA, or internal policy)
2. Document the organization's current controls for each requirement
3. For each requirement, assess: Is the required control present? Is it adequately designed? Is there evidence it is operating?
4. Record gaps — requirements where the answer to any assessment question is "no"
5. Prioritize gaps by risk — high-impact gaps with no compensating control are the highest priority
6. Build a remediation roadmap — assigning owners, timelines, and success criteria to each gap

### Gap Analysis Output

The gap analysis produces a report that includes: total number of requirements assessed, number and percentage of requirements met, list of identified gaps with descriptions, risk ratings for each gap, and recommended remediation actions. For ISO 27001 certification, the gap analysis output directly shapes the implementation roadmap and the initial Statement of Applicability.

---

## Compliance Dashboards

A compliance dashboard provides a visual, consolidated view of the organization's compliance posture. Dashboards serve multiple stakeholders simultaneously:

**IT Leadership** needs a strategic summary: What percentage of controls are implemented? How many open audit findings exist? What are the most significant risks? When are upcoming certification renewals?

**Operations Teams** need tactical visibility: Which specific controls are failing? What remediation tasks are overdue? Which systems are out of compliance on a specific control?

**Auditors** benefit from structured evidence summaries that reduce the time required to locate and verify evidence during an audit engagement.

Effective compliance dashboards show control coverage percentage, control testing results (passed/failed/untested), open risk register items with scores and owners, outstanding audit findings with remediation timelines, and upcoming compliance milestones and deadlines.

---

## Key Terms for the ITIL 4 Foundation Exam

| Term | Definition |
|---|---|
| Risk | A possible event that could cause harm or loss, or affect the ability to achieve objectives |
| Risk register | A documented record of identified risks, their assessments, and response strategies |
| Residual risk | The risk that remains after controls are applied |
| ISMS | Information Security Management System — a management framework for systematically managing information security risk |
| ISO 27001 | International standard for ISMS — requires formal risk assessment, control selection, and continual improvement |
| Statement of Applicability | Document listing which ISO 27001 Annex A controls are selected, implemented, or excluded with justification |
| SOC 2 | AICPA auditing framework evaluating controls against Trust Services Criteria |
| SOC 2 Type I | Point-in-time assessment of control design adequacy |
| SOC 2 Type II | Assessment of control operating effectiveness over a defined period |
| Gap analysis | Comparison of current controls against a target standard to identify missing or inadequate controls |

---

## Study Questions

1. What are the four risk response strategies in ITIL 4, and when is each appropriate?

2. What is the difference between risk likelihood, risk impact, and residual risk?

3. What is the Statement of Applicability in ISO 27001, and why does it matter?

4. What is the difference between a SOC 2 Type I and Type II report? Which do enterprise customers typically require and why?

5. How do ITSM ticketing systems generate SOC 2 audit evidence as a byproduct of normal operations?

6. An organization is preparing for ISO 27001 certification. Describe the five steps of a risk assessment process under ISO 27001.

7. What is the purpose of a compliance dashboard, and what three stakeholder groups does it serve?
