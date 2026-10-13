# Video Script: Module 14 — Governance, Compliance, and Regulatory Frameworks (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00–0:45]

Welcome back. This is Module 14, Part 2. In Part 1 we covered the major regulatory frameworks — GDPR, HIPAA, PCI-DSS, and SOX. Now we shift to the frameworks organizations use to *build* their security programs: NIST CSF and ISO 27001. We will also cover data classification, core privacy principles, and how organizations prepare for compliance audits.

These topics appear heavily in the Security+ SY0-701 exam domain on Security Program Management and Oversight — so take notes.

---

### [SECTION 1: NIST Cybersecurity Framework — 0:45–4:00]

The NIST Cybersecurity Framework, or NIST CSF, was originally developed at the direction of a 2013 executive order to improve cybersecurity for critical infrastructure. It has since become the most widely used voluntary security framework in the United States. Version 2.0 was released in 2024 and added a new "Govern" function.

The NIST CSF is organized around **six core functions**. Think of them as the lifecycle of managing cybersecurity risk.

**Govern (new in v2.0)** — establishes and monitors cybersecurity risk management strategy, expectations, and policy. This function acknowledges that governance is foundational to all other functions.

**Identify** — develop an understanding of organizational assets, risks, and context. You cannot protect what you do not know you have. Asset management, risk assessment, and supply chain risk management live here.

**Protect** — implement safeguards to ensure delivery of critical services. Access control, awareness training, data security, and protective technology all fall under Protect.

**Detect** — implement activities to identify the occurrence of a cybersecurity event. Continuous monitoring, anomaly detection, and security logging belong here.

**Respond** — implement activities to take action regarding a detected cybersecurity incident. Response planning, communications, analysis, and mitigation are the sub-categories.

**Recover** — implement activities to maintain resilience and restore capabilities impaired by a cybersecurity incident. Recovery planning and improvements are in this function.

Each function breaks down into **Categories** and **Subcategories** — over 100 specific outcomes in total. Organizations use the framework by creating a **Current Profile** (where you are today), a **Target Profile** (where you want to be), and then identifying gaps to prioritize investments.

The NIST CSF is not a compliance checklist — it is a *risk-based* management tool. That distinction matters on the exam.

**Tiers** describe how mature an organization's risk management practices are:

- Tier 1: Partial — reactive, ad hoc
- Tier 2: Risk Informed — risk management practices exist but are not organization-wide
- Tier 3: Repeatable — formal policies in place, consistently applied
- Tier 4: Adaptive — continuously improving based on lessons learned and threat intelligence

---

### [SECTION 2: ISO/IEC 27001 — 4:00–6:30]

ISO 27001 is an international standard for Information Security Management Systems, or ISMS. It is published by the International Organization for Standardization and provides a framework for establishing, implementing, maintaining, and continually improving information security within an organization.

Unlike NIST CSF, ISO 27001 is **certifiable** — organizations can be audited by an accredited third party and receive formal ISO 27001 certification. This certification is often required to do business with European partners or government entities.

The core of ISO 27001 is the **Plan-Do-Check-Act (PDCA) cycle**:

- **Plan** — establish the ISMS scope, policy, and risk treatment plan
- **Do** — implement and operate the ISMS
- **Check** — monitor, measure, and audit the ISMS
- **Act** — take corrective and preventive actions; continually improve

ISO 27001 is organized into **clauses 4 through 10**, which are mandatory requirements, plus **Annex A**, which contains 93 controls organized into 4 themes: Organizational, People, Physical, and Technological.

Key concepts for the exam:

**Statement of Applicability (SoA)** — a document listing all Annex A controls, indicating which are applicable to the organization and why others were excluded. This is a required deliverable for certification.

**Risk treatment options** — organizations can accept, avoid, transfer, or mitigate identified risks. All treatment decisions must be documented.

**Internal audit** — organizations must conduct internal audits of the ISMS at planned intervals before pursuing external certification.

The comparison to remember: NIST CSF is a *voluntary framework* used widely in the US; ISO 27001 is a *certifiable standard* used globally. Both are risk-based and compatible with each other.

---

### [SECTION 3: Data Classification — 6:30–9:00]

Data classification is the process of organizing data into categories based on sensitivity and the impact of unauthorized disclosure. Classification drives how data must be handled, stored, transmitted, and destroyed.

**Government classification levels** (US federal, from most to least sensitive):

- Top Secret — unauthorized disclosure could cause exceptionally grave damage to national security
- Secret — serious damage
- Confidential — damage
- Controlled Unclassified Information (CUI) — sensitive but unclassified; governed by NIST SP 800-171
- Unclassified

**Commercial classification levels** (typical private sector):

- Restricted / Confidential — highest sensitivity; trade secrets, PII, PHI, cardholder data
- Internal / Private — internal business information not for public release
- Public — approved for external release

Classification must be assigned by the **data owner** — typically a business manager or executive who is accountable for the data. The **data custodian** implements controls on behalf of the owner. The **data steward** manages data quality and governance.

**Data handling requirements** by classification level typically include:

- Labeling requirements — documents and files must be marked with their classification
- Storage requirements — restricted data may require encryption at rest and limited locations
- Transmission requirements — restricted data may require encrypted channels
- Retention requirements — how long data must be kept (often driven by regulation)
- Destruction requirements — how data must be disposed of (shredding, wiping, degaussing)

For the Security+ exam, the distinction between data owner, custodian, and steward is tested frequently. Know the roles clearly.

---

### [SECTION 4: Privacy Principles — 9:00–11:30]

Privacy and security are related but distinct. **Security** is about protecting data from unauthorized access. **Privacy** is about ensuring data is collected and used appropriately, with respect for individual rights.

The foundational privacy principles appear across multiple frameworks — GDPR, HIPAA, and NIST Privacy Framework all draw from a common set.

**Fair Information Practice Principles (FIPPs):**

- Notice/Awareness — individuals must be informed about data collection practices
- Choice/Consent — individuals must have options about how their data is used
- Access/Participation — individuals can view and correct their own data
- Integrity/Security — data must be accurate and protected
- Enforcement/Redress — mechanisms must exist to hold organizations accountable

**Privacy by Design** (from Ann Cavoukian's principles, now embedded in GDPR):

- Proactive, not reactive — build privacy in from the start
- Privacy as the default — maximum privacy without any action required by the user
- Privacy embedded into design — not bolted on as an add-on feature
- Full functionality — privacy does not require sacrificing functionality
- End-to-end security — strong security throughout the data lifecycle
- Visibility and transparency — keep practices open
- Respect for user privacy — keep it user-centric

**Data minimization** — collect only the data you actually need. This is both a GDPR requirement and a fundamental privacy principle that limits breach impact.

**Purpose limitation** — data collected for one purpose must not be used for a different purpose without re-obtaining consent.

For the exam: Privacy by Design, data minimization, and purpose limitation are all testable concepts under the SY0-701 domain on Privacy.

---

### [SECTION 5: Audit Preparation — 11:30–13:30]

Compliance audits are formal assessments of whether an organization meets the requirements of a specific regulation or framework. Audit preparation is an ongoing process, not a sprint before the audit date.

**Types of audits:**

- **Internal audit** — performed by the organization's own audit team; identifies gaps before external auditors arrive
- **External audit** — performed by an independent third party; results carry legal or certification weight
- **Regulatory examination** — performed by a government agency (e.g., HHS for HIPAA, OCC for banking)

**Key audit preparation activities:**

- Maintain a **control inventory** — document every security control in place and map it to the applicable requirement
- Conduct **gap assessments** — regularly compare current state to required state
- Gather **evidence continuously** — screenshots, logs, signed policies, training records
- Conduct **tabletop exercises** — simulate scenarios to test whether controls work as documented
- Perform **internal audits** before external ones

**Common audit artifacts:**

- Policy documents with version control and approval signatures
- Risk assessment reports
- Vulnerability scan and penetration test results
- Access control reviews (who has access to what)
- Change management records
- Incident response records
- Employee security training completion records

**Audit findings** typically fall into three categories: findings (non-compliances requiring corrective action), observations (areas for improvement), and recommendations (best practices not required but suggested).

---

### [CLOSING — 13:30–15:00]

Here is your Part 2 summary:

- NIST CSF v2.0 has six functions: Govern, Identify, Protect, Detect, Respond, Recover — used to build and mature a security program
- ISO 27001 is a certifiable ISMS standard using PDCA; the Statement of Applicability is a required deliverable
- Data classification uses levels (Top Secret → Unclassified for government; Restricted → Public for commercial); data owners assign classification, custodians implement controls
- Privacy principles include Fair Information Practices, Privacy by Design, data minimization, and purpose limitation
- Audit preparation is continuous: maintain control inventories, gather evidence, conduct internal audits, and document everything

Together Parts 1 and 2 give you the complete governance and compliance picture. The lab for this module will walk you through mapping an organization's controls to a real framework. The quiz will test both regulatory specifics and framework concepts.

Good luck, and I will see you in Module 15.

---

*End of Part 2 Script*
