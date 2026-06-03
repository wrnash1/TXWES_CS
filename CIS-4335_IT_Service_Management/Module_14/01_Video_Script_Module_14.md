# Video Script: Module 14 — Risk and Compliance in ITSM

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation
**Estimated Duration:** 22–25 minutes
**Recorded by:** Professor Nash

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.
- [PAUSE] cues indicate natural break points for student note-taking.

---

## Section 1: Welcome and Module Overview [00:00 - 02:30]

Welcome to Module 14. I am Professor Nash. Today we are covering Risk and Compliance in ITSM — the practice of identifying, assessing, and managing risk within the IT service environment, and the frameworks that translate legal and regulatory obligations into actionable IT controls.

[SHOW DIAGRAM: Title slide — "Module 14: Risk and Compliance in ITSM" with ITIL 4 SVS label and ITIL 4 Foundation certification badge]

Risk and compliance are often treated as separate concerns — risk feels like a technical discipline, compliance feels like a legal one. In practice, they are deeply connected. An organization's compliance obligations define a floor of required controls. Risk management identifies the threats and vulnerabilities that those controls must address. Together they shape what IT does to protect the organization's people, data, and services.

By the end of this module you will be able to: explain how risk registers are used in IT service management, describe ITIL 4's approach to risk integration, identify the key IT requirements of ISO 27001, explain what SOC 2 is and why it matters, describe how audit evidence is collected, and explain the purpose of gap analysis and compliance dashboards.

---

## Section 2: Risk Management in ITSM [02:30 - 07:30]

[SHOW DIAGRAM: Risk management cycle — Risk Identification → Risk Assessment (Likelihood × Impact) → Risk Response (Avoid/Mitigate/Transfer/Accept) → Monitor and Review → back to Identification]

### What Is Risk?

ITIL 4 defines risk as a possible event that could cause harm or loss, or affect the ability to achieve objectives. Risk is characterized by two dimensions: likelihood — how probable is the event — and impact — how severe would the consequences be. The combination of these two dimensions determines risk exposure.

### The Risk Register

A risk register is a documented record of identified risks, their assessments, and the responses that have been selected to manage them. In ITSM, risk registers are maintained at multiple levels: project-level risk registers for individual initiatives, service-level risk registers for ongoing services, and organizational-level risk registers for enterprise-wide concerns.

[PAUSE]

Each entry in a risk register typically contains:

- A risk description — what could happen
- The risk category — security, availability, compliance, financial, or reputational
- Likelihood rating — often scored on a scale of 1 to 5
- Impact rating — also scored 1 to 5
- Risk score — likelihood multiplied by impact
- Risk owner — the person responsible for managing this risk
- Response strategy — avoid, mitigate, transfer, or accept
- Controls in place — what is already being done
- Residual risk — the risk that remains after controls are applied

### ITIL 4 Risk Integration

ITIL 4 integrates risk thinking throughout the Service Value System. The SVS guiding principle "Focus on Value" connects to risk by asking: what risks threaten value delivery? Change Management includes risk assessment as a core activity — every change is evaluated for its likelihood and impact of failure. Continual Improvement includes risk consideration — improvement initiatives can introduce new risks.

---

## Section 3: ISO 27001 Alignment [07:30 - 12:00]

[SHOW DIAGRAM: ISO 27001 PDCA cycle — Plan (establish ISMS), Do (implement controls), Check (audit and review), Act (improve) — with the 14 Annex A control domains listed around the outside]

### What Is ISO 27001?

ISO 27001 is the international standard for Information Security Management Systems (ISMS). An organization that is ISO 27001 certified has demonstrated that it has established, implemented, maintained, and continuously improved a systematic approach to managing information security risk.

### The ISMS

An Information Security Management System is not a product or technology — it is a management framework. It defines how an organization identifies information security risks, selects controls to address them, and monitors the effectiveness of those controls. The ISMS encompasses people, processes, and technology.

[PAUSE]

### Annex A Controls

ISO 27001 Annex A contains 114 security controls organized into 14 domains. Key domains relevant to ITSM include:

**Access control** — policies and mechanisms that restrict access to information and systems to authorized individuals.

**Operations security** — controls over IT operations including change management, capacity management, protection from malware, backup, and activity logging.

**Incident management** — documented procedures for detecting, reporting, and responding to information security incidents.

**Asset management** — requirements to identify, classify, and protect information assets — directly connected to IT Asset Management practice.

**Supplier relationships** — controls over third-party access to organizational information and systems.

### Risk Assessment Under ISO 27001

ISO 27001 requires a formal risk assessment process. The organization must identify information assets, identify the threats and vulnerabilities that affect each asset, assess the likelihood and impact of each risk, select controls from Annex A (or elsewhere) to address identified risks, and produce a Statement of Applicability documenting which controls are selected and why.

---

## Section 4: SOC 2 [12:00 - 15:30]

[SHOW DIAGRAM: SOC 2 Trust Services Criteria — five categories in boxes: Security (Security is mandatory), Availability, Processing Integrity, Confidentiality, Privacy — with "Type I" and "Type II" labels explained below]

### What Is SOC 2?

SOC 2 — System and Organization Controls 2 — is an auditing framework developed by the American Institute of Certified Public Accountants (AICPA) for service organizations. It evaluates whether an organization's controls meet the Trust Services Criteria in five categories: Security, Availability, Processing Integrity, Confidentiality, and Privacy. Security is the only mandatory category; organizations select additional categories based on their customer commitments.

### Type I vs. Type II

A SOC 2 Type I report evaluates whether controls are suitably designed at a specific point in time. It answers: "Are the right controls in place today?"

A SOC 2 Type II report evaluates whether those controls operated effectively over a period of time — typically six to twelve months. It answers: "Did those controls actually work consistently over this period?"

Type II reports are more valuable to customers and business partners because they demonstrate sustained operational effectiveness, not just design adequacy.

[PAUSE]

### SOC 2 and ITSM

SOC 2's Security criterion maps directly to several ITSM practices. Change Management provides evidence that changes are authorized and tested before deployment. Incident Management provides evidence that security incidents are detected and responded to. IT Asset Management provides evidence that access controls are tied to specific assets. Release and Deployment Management provides evidence that software is tested before reaching production.

Organizations pursuing SOC 2 Type II certification find that mature ITSM practices generate much of the evidence needed for the audit.

---

## Section 5: Audit Evidence Collection [15:30 - 18:30]

[SHOW DIAGRAM: Audit evidence types — four boxes: System-generated logs (change records, access logs), Policy documents (approved policies and procedures), Configuration exports (firewall rules, user access lists), Interview records (notes from auditor discussions with staff)]

An audit is an independent review that assesses whether an organization's controls meet a defined standard. Audit evidence is the documentation that supports the auditor's findings. Collecting audit evidence is an operational discipline that ITSM teams must practice continuously, not just when an audit is scheduled.

### Types of Audit Evidence

**System-generated logs** are the most objective form of evidence. Change Management tickets showing approval history, access logs showing who accessed what and when, deployment records showing what was deployed and by whom — these are system-generated records that are difficult to fabricate and easy to provide.

**Policy documents** demonstrate that required policies exist and have been formally approved. ISO 27001 and SOC 2 both require documented policies for access control, incident response, and change management.

**Configuration exports** show the actual state of systems — firewall rules, user account lists, encryption settings. These demonstrate that technical controls are implemented, not just documented.

**Interview records** capture the auditor's conversations with staff to verify that policies are understood and followed.

### Continuous Evidence Readiness

Organizations with mature compliance programs maintain evidence continuously. When an audit arrives, evidence is already organized and available — not assembled under pressure in the days before the audit window. This approach also makes it easier to identify and remediate compliance gaps before they become audit findings.

---

## Section 6: Gap Analysis and Compliance Dashboards [18:30 - 21:00]

### Gap Analysis

A gap analysis compares the organization's current state of controls against a required standard. The output is a list of identified gaps — areas where required controls are absent, inadequate, or not demonstrably operating.

Gap analysis is the starting point for compliance roadmaps. An organization pursuing ISO 27001 certification will typically conduct a gap analysis against Annex A to identify which controls must be implemented before the certification audit.

[PAUSE]

### Compliance Dashboards

A compliance dashboard provides a visual, real-time view of the organization's compliance posture. Effective compliance dashboards show:

- Which controls are implemented versus required — coverage percentage
- Which controls have passed recent testing versus failed or not been tested
- Outstanding audit findings and their remediation status
- Risk scores for open risks in the risk register
- Upcoming audit and certification deadlines

Compliance dashboards serve multiple audiences: the CISO and IT leadership who need a strategic view, operations teams who need to track specific control remediation tasks, and auditors who benefit from seeing a structured evidence summary.

---

## Section 7: Exam Reminders and Lab Preview [21:00 - End]

Three exam reminders. First: ITIL 4 integrates risk throughout the SVS — risk assessment is not a separate discipline, it is embedded in every practice. Second: ISO 27001 requires an ISMS with formal risk assessment and a Statement of Applicability. Third: SOC 2 Type II demonstrates operational effectiveness over time — it is more valuable than Type I to customers and auditors.

This week's lab puts you in the role of a compliance analyst preparing for a SOC 2 Type II audit. You will complete a gap analysis, identify audit evidence for specific controls, and design a compliance dashboard for an IT leadership team.

---

## Module 14 Complete

Next: Module 15 — DevOps, Agile, and ITIL 4 Integration

### Additional Resources

- axelos.com — ITIL 4 Foundation study materials
- iso.org — ISO 27001:2022 information security standard overview
- aicpa.org — SOC 2 Trust Services Criteria reference
