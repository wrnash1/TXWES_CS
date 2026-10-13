# Video Script: Module 14 — Risk and Compliance in IT Service Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Slide 1: Introduction (0:00–0:45)

Welcome to Module 14 of CIS-4335. I'm Professor Nash. This module addresses one of the most strategically important intersections in modern IT: risk management and compliance.

Every organization that provides IT services operates in a landscape of threats, regulatory requirements, and audit obligations. Understanding how ITIL 4 approaches risk, and how it connects to frameworks like ISO 27001 and SOC 2, is critical for any IT professional moving into leadership roles.

By the end of this video you'll understand risk registers, ITIL's risk management approach, key regulatory frameworks, and how to prepare for an IT audit.

---

## Slide 2: What Is Risk in IT Service Management? (0:45–2:15)

ITIL 4 defines risk as "a possible event that could cause harm or loss, or make it more difficult to achieve objectives." This definition has two dimensions:

- **Negative risks (threats):** Events that could damage services, data, or the organization.
- **Positive risks (opportunities):** Events that could deliver unexpected benefit.

In practice, IT risk management focuses heavily on threats, but a complete risk program acknowledges both.

Every IT service introduces risk. A new deployment might fail. A database might be compromised. A key vendor might go out of business. A compliance deadline might be missed. The question is not whether risks exist — they always do — but whether the organization has identified, assessed, and responded to them appropriately.

ITIL 4 does not prescribe a specific risk management methodology. Instead, it encourages organizations to adopt and adapt established frameworks. In larger organizations, ITIL risk management activities align with enterprise risk management (ERM) programs.

---

## Slide 3: The Risk Register (2:15–4:30)

A **risk register** is the primary tool for documenting, tracking, and managing identified risks. It is a living document — not a one-time snapshot.

### Core Risk Register Fields

- **Risk ID:** Unique identifier for tracking.
- **Risk description:** Clear statement of what might happen and its consequence.
- **Risk category:** Technology, operational, regulatory, financial, reputational, etc.
- **Likelihood:** Probability that the risk will materialize. Commonly rated 1–5 or as Low/Medium/High.
- **Impact:** Severity of consequence if the risk occurs. Also rated 1–5 or Low/Medium/High.
- **Risk score (exposure):** Likelihood × Impact = risk priority score.
- **Risk owner:** The person accountable for managing this risk.
- **Current controls:** Existing safeguards that already reduce likelihood or impact.
- **Residual risk:** The remaining risk level after current controls are applied.
- **Response strategy:** How the organization will treat the risk.
- **Action plan:** Specific steps to implement the chosen response.
- **Review date:** When the risk will be reassessed.

### Risk Response Strategies

There are four standard risk response strategies:

**1. Avoid:** Eliminate the risk by not undertaking the risky activity. Example: decide not to deploy a new untested technology that poses unacceptable security risks.

**2. Transfer:** Shift the financial impact of the risk to a third party. Example: purchase cyber insurance; outsource a function to a managed service provider who contractually assumes responsibility.

**3. Mitigate (Reduce):** Take actions to reduce likelihood or impact. This is the most common strategy. Example: implement multi-factor authentication to reduce the likelihood of account compromise.

**4. Accept:** Acknowledge the risk and decide not to take action, typically because the cost of mitigation exceeds the potential impact. Acceptance must be documented and formally approved by an appropriate authority.

---

## Slide 4: ITIL 4 Risk Management Integration (4:30–6:30)

ITIL 4 integrates risk thinking throughout the Service Value System, not just in a dedicated "risk management" silo.

### Risk in the Guiding Principles

The principle **"Start where you are"** includes understanding current risks before designing improvements. The principle **"Progress iteratively with feedback"** reduces risk by making small, reversible changes rather than large, uncertain ones.

### Risk in Key Practices

- **Change Enablement:** Every change request includes a risk assessment. The change authority evaluates whether the risk of implementing the change outweighs the benefit.
- **Problem Management:** Identifies risks from recurring incidents before they cause further harm.
- **Service Level Management:** SLAs include availability and performance commitments — shortfalls represent operational risk.
- **Continual Improvement:** Risk identification is part of assessing the current state before proposing improvements.
- **Information Security Management:** Manages information risk specifically — the risk that confidentiality, integrity, or availability of information is compromised.

### The Four Dimensions and Risk

Each of the Four Dimensions of Service Management carries specific risks:

- **Organizations and People:** Key person dependencies, skills gaps, culture resistance to change.
- **Information and Technology:** Cybersecurity threats, data loss, technology obsolescence.
- **Partners and Suppliers:** Vendor failure, supply chain disruption, third-party data breaches.
- **Value Streams and Processes:** Process failures, compliance gaps, inefficient workflows.

---

## Slide 5: ISO 27001 — Information Security Management (6:30–8:30)

**ISO/IEC 27001** is the international standard for information security management systems (ISMS). It provides a systematic approach to managing sensitive organizational information and ensuring its confidentiality, integrity, and availability.

### Key Concepts

**ISMS (Information Security Management System):** A framework of policies, procedures, and controls to manage information security risks. ISO 27001 specifies the requirements for establishing, implementing, maintaining, and continually improving an ISMS.

**Risk Assessment and Treatment:** ISO 27001 requires organizations to conduct formal risk assessments to identify information security risks and select appropriate treatment options. This directly parallels the ITIL risk register approach.

**Annex A Controls:** ISO 27001:2022 contains 93 controls organized into four categories: Organizational, People, Physical, and Technological. These controls address areas like access control, cryptography, physical security, incident management, and supplier security.

**Certification:** Organizations can be formally certified to ISO 27001 by an accredited certification body. Certification demonstrates to customers, partners, and regulators that the organization manages information security systematically.

### ITIL-ISO 27001 Alignment

ITIL's Information Security Management practice aligns closely with ISO 27001. Both require:

- Documented security policies.
- Risk assessment and treatment processes.
- Security incident management procedures.
- Continual improvement of security posture.
- Stakeholder communication about security.

---

## Slide 6: SOC 2 — Service Organization Controls (8:30–10:30)

**SOC 2** (System and Organization Controls 2) is an auditing standard developed by the American Institute of Certified Public Accountants (AICPA). It is specifically relevant for technology service providers — cloud companies, SaaS vendors, data centers, and managed service providers.

### Trust Services Criteria

SOC 2 is based on five Trust Services Criteria:

- **Security (required):** Protection against unauthorized access, both physical and logical.
- **Availability:** System availability for operation and use as committed.
- **Processing Integrity:** System processing is complete, valid, accurate, timely, and authorized.
- **Confidentiality:** Information designated as confidential is protected.
- **Privacy:** Personal information is collected, used, retained, and disclosed in accordance with privacy commitments.

### SOC 2 Type I vs. Type II

- **Type I:** Point-in-time assessment — the auditor evaluates whether controls are appropriately designed at a specific date.
- **Type II:** Period assessment — the auditor evaluates whether controls operated effectively over a defined period (typically 6–12 months).

Type II reports are more valuable to customers because they demonstrate sustained operational effectiveness, not just the existence of controls on one day.

### Why SOC 2 Matters for ITSM

For organizations that provide IT services to other organizations (B2B), SOC 2 Type II reports are increasingly required by customers and procurement teams. An IT service provider without a SOC 2 report may be disqualified from enterprise contracts.

From an ITSM perspective, SOC 2 compliance reinforces many practices: incident logging, change management documentation, access control reviews, and availability monitoring.

---

## Slide 7: Audit Preparation (10:30–12:30)

Regulatory compliance is not demonstrated by having policies — it is demonstrated by evidence. Audit preparation is the process of organizing, validating, and presenting that evidence to an auditor.

### Types of Audits

- **Internal audit:** Conducted by the organization's own audit team (or internal audit function) to assess controls before an external audit.
- **External audit:** Conducted by an independent third party (certification body, public accounting firm, regulatory agency).
- **Regulatory examination:** Conducted by a government agency (e.g., HIPAA audits by HHS OCR, PCI DSS assessments by Qualified Security Assessors).
- **Customer audit:** A customer or prospect requests the right to audit the service provider's controls as part of a contract.

### Evidence Categories

Auditors typically request evidence in several categories:

- **Policies and procedures:** Written documentation of how processes work.
- **Technical configurations:** Screenshots, configuration exports, or automated scan results.
- **Logs:** System logs, access logs, change records — typically covering the audit period.
- **Training records:** Evidence that staff completed required security or compliance training.
- **Testing results:** Penetration test reports, vulnerability scan results, disaster recovery test documentation.
- **Management review records:** Documentation of risk register reviews, exception approvals, and corrective action tracking.

### ITIL Practices as Audit Evidence

ITIL-aligned processes generate natural audit evidence:

- Change records with approvals support change management control evidence.
- Incident records demonstrate incident response capability.
- Release notes and post-implementation reviews support deployment control evidence.
- Risk register entries with review dates demonstrate active risk management.

Organizations that run mature ITIL processes are better prepared for audits because the documentation already exists.

---

## Slide 8: Building a Compliance Culture (12:30–14:00)

Compliance is not just a documentation exercise — it requires a culture where risk and control thinking are embedded in daily operations.

### Common Failure Patterns

- **Compliance theater:** Policies exist on paper but are not followed in practice. Auditors are skilled at detecting the gap between documented policy and operational reality.
- **Point-in-time compliance:** The organization prepares intensively for audits and then relaxes between cycles. This is inefficient and creates real exposure during non-audit periods.
- **Siloed compliance:** Each department manages its own compliance in isolation. Risk is not aggregated, and cross-functional dependencies are missed.

### Sustainable Compliance Practices

- Embed compliance checkpoints in standard processes — change requests require risk assessment; new projects require security review.
- Automate evidence collection where possible — logging, configuration compliance scanning, access certification workflows.
- Conduct regular internal audits to identify gaps before external auditors do.
- Treat the risk register as a living document reviewed at least quarterly.
- Train all staff, not just IT — humans are the most common vector for security incidents.

---

## Slide 9: Key Terms Summary (14:00–15:15)

Key vocabulary for this module:

- **Risk** — possible event causing harm or loss.
- **Risk register** — documented record of identified risks, scores, owners, and responses.
- **Risk likelihood** — probability that a risk event will occur.
- **Risk impact** — severity of consequences if the risk occurs.
- **Risk exposure** — likelihood × impact score.
- **Risk response strategies** — Avoid, Transfer, Mitigate, Accept.
- **ISO 27001** — international standard for information security management systems.
- **ISMS** — Information Security Management System.
- **SOC 2** — AICPA auditing standard for technology service providers.
- **Trust Services Criteria** — Security, Availability, Processing Integrity, Confidentiality, Privacy.
- **SOC 2 Type I / Type II** — point-in-time vs. period operational effectiveness audit.
- **Audit evidence** — documentation proving controls exist and operate effectively.
- **Compliance theater** — appearance of compliance without operational reality.

---

## Slide 10: Closing and Preview (15:15–16:00)

That concludes Module 14. You now understand how ITIL 4 approaches risk management, how the risk register works as a practical tool, and how ISO 27001 and SOC 2 connect to ITSM practices. You also have a framework for thinking about audit preparation as an ongoing operational discipline rather than a periodic scramble.

In Module 15 we bring together DevOps, Agile, and ITIL 4 — exploring how modern software delivery practices and IT service management principles reinforce rather than contradict each other.

Complete the reading guide, lab, and quiz before moving on. See you in Module 15.

---

*End of Module 14 Video Script — approximately 235 lines*
