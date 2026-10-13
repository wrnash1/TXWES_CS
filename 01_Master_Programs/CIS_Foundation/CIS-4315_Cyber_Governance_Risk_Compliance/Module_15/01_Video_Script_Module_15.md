# Video Script: Module 15 — Legal, Regulatory, and Compliance Frameworks

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 1 (Information Security Governance) and Domain 3 (Information Security Program Development and Management) — Regulatory Environment and Compliance Program Management

---

### [SLIDE 1] Opening

Welcome back, everyone. I am Professor Nash, and this is Module 15 of CIS-4315 Cyber Governance, Risk, and Compliance.

We have spent the last fourteen modules building your foundation in governance frameworks, risk management, incident response, and security program management. Today we bring all of that together through the lens of law and regulation.

This module is titled Legal, Regulatory, and Compliance Frameworks. By the time we finish, you will be able to explain the major global and domestic regulatory regimes that shape every enterprise security program, map those regulations to organizational controls, and describe what a sustainable compliance management program looks like in practice.

This material is directly tested on the CISM exam, and more importantly, it is the daily operational reality for every information security manager working in an enterprise environment today. Let us get started.

---

### [SLIDE 2] Why Compliance Is the Floor, Not the Ceiling

Before we dive into the alphabet soup of acronyms, I want to set a philosophical stake in the ground: compliance is the floor, not the ceiling.

Many organizations treat legal compliance as the end goal of their security program. If we pass the audit, we are secure. That thinking is dangerous. Compliance tells you the minimum standard that society has agreed to require. It does not tell you whether you are actually safe.

Consider this. The Target breach of 2013 involved a company that was PCI-DSS compliant at the time of the breach. Equifax, whose 2017 breach exposed the personal information of 147 million Americans, was subject to multiple regulatory frameworks and had passed multiple audits.

Compliance matters. It is legally mandatory, contractually required, and ethically important. But our mental model must always be: compliance enables a baseline, security requires judgment. With that in mind, let us walk through the major frameworks.

---

### [SLIDE 3] The Global Regulatory Landscape

Regulations governing information security fall into roughly four categories.

The first category is **privacy and data protection law**. These laws govern how personal information is collected, stored, used, and shared. Examples include GDPR, CCPA, and HIPAA's Privacy Rule.

The second category is **sector-specific security standards**. These apply to specific industries. HIPAA's Security Rule applies to healthcare. PCI-DSS applies to payment card processing. NERC-CIP applies to electric utilities.

The third category is **financial and corporate governance law**. Sarbanes-Oxley, or SOX, governs publicly traded companies. GLBA governs financial institutions. FISMA governs U.S. federal agencies.

The fourth category is **emerging and cross-border regulation**. This includes the EU's NIS2 Directive for critical infrastructure, China's Cybersecurity Law, and the SEC's new cyber disclosure requirements.

For the CISM exam, you are expected to understand which frameworks apply in a given scenario and what their core requirements are. Let us go through the most important ones one by one.

---

### [SLIDE 4] GDPR — The Gold Standard of Privacy Law

The General Data Protection Regulation, GDPR, went into effect in May 2018 and fundamentally changed global data privacy. Even if your organization is based in Texas, if you process personal data of European Union residents, GDPR applies to you. This is called extraterritorial jurisdiction, and it matters enormously for multinational enterprises.

The core principles of GDPR are:

**Lawfulness, fairness, and transparency** — you must have a legal basis for processing data and be transparent about it with data subjects.

**Purpose limitation** — data collected for one purpose cannot be used for a different purpose without renewed consent or a new legal basis.

**Data minimization** — collect only what you need to accomplish your stated purpose.

**Accuracy** — keep data correct and current, and provide mechanisms for correction.

**Storage limitation** — do not keep personal data longer than necessary.

**Integrity and confidentiality** — Article 32 requires appropriate technical and organizational measures to protect personal data. Note that the regulation does not specify particular technologies — it requires appropriateness relative to the risk.

**Accountability** — the data controller must be able to demonstrate compliance, not just assert it.

Key rights granted to individuals include the right to access their data, the right to rectification, the right to erasure — the so-called right to be forgotten — the right to data portability, and the right to object to automated decision-making including profiling.

Article 33 is critical for security professionals: it requires notification of data breaches to the supervisory authority within 72 hours of becoming aware of the breach. Article 34 requires notification to affected individuals when the breach is likely to result in a high risk to their rights and freedoms.

Penalties are severe. Tier 1 violations can result in fines up to 10 million euros or 2% of global annual turnover. Tier 2 violations — the most serious, including violations of core principles and data subject rights — can result in fines up to 20 million euros or 4% of global annual turnover, whichever is higher.

---

### [SLIDE 5] HIPAA — Healthcare Privacy and Security

The Health Insurance Portability and Accountability Act, HIPAA, was enacted in 1996 and has been amended multiple times since. It applies to covered entities — healthcare providers, health plans, and healthcare clearinghouses — and to their business associates, which are third parties that handle protected health information on the covered entity's behalf.

HIPAA has three major security-relevant components.

The **Privacy Rule** governs the use and disclosure of Protected Health Information, or PHI. PHI is any health information tied to an individual's identity. The Privacy Rule establishes the minimum necessary standard — access to PHI should be limited to what is needed to accomplish the purpose — and grants patients rights including the right to access and amend their records.

The **Security Rule** governs Electronic PHI, or ePHI. It requires covered entities to implement administrative safeguards, physical safeguards, and technical safeguards. Unlike GDPR or PCI-DSS, HIPAA does not prescribe specific technologies. It uses the terms "required" for mandatory safeguards and "addressable" for safeguards where an organization may implement an alternative measure that achieves the same result.

The **Breach Notification Rule** requires notification to affected individuals within 60 days of discovery, notification to the HHS Secretary, and for breaches affecting more than 500 residents of a state, notification to prominent media outlets in that state. Large breaches are posted on what practitioners call the HHS "Wall of Shame."

Penalties under HIPAA's tiered structure range from $137 to $68,928 per violation depending on culpability, with annual caps per violation category. The highest tier — willful neglect not corrected — carries penalties up to $2.067 million per year per violation category.

---

### [SLIDE 6] PCI-DSS — Payment Card Security

The Payment Card Industry Data Security Standard, PCI-DSS, is a contractual security standard maintained by the PCI Security Standards Council, which represents Visa, Mastercard, American Express, Discover, and JCB. It applies to any organization that stores, processes, or transmits cardholder data.

PCI-DSS version 4.0 was released in 2022 and introduced two compliance approaches. The defined approach is the traditional checkbox model. The customized approach, new in version 4.0, allows organizations to demonstrate that their controls achieve the stated security objective through an alternative method, providing flexibility for innovative security implementations.

The standard is organized around six goals and twelve requirements. The six goals are:

- Build and maintain a secure network and systems
- Protect cardholder data
- Maintain a vulnerability management program
- Implement strong access control measures
- Regularly monitor and test networks
- Maintain an information security policy

Compliance is assessed through a Report on Compliance, or ROC, conducted by a Qualified Security Assessor, or QSA, for large merchants and service providers. Smaller entities may use a Self-Assessment Questionnaire, or SAQ.

Non-compliance consequences include fines from card brands, increased transaction processing fees, mandatory forensic investigations following breaches, and ultimately loss of the ability to accept card payments — which is existential for many businesses.

---

### [SLIDE 7] SOX — Financial Controls and IT

The Sarbanes-Oxley Act of 2002 was enacted in the wake of the Enron and WorldCom accounting scandals. While it is primarily a financial regulation, it has significant implications for information technology and information security.

Section 302 requires CEOs and CFOs to personally certify the accuracy of financial statements and the effectiveness of internal controls over financial reporting. Personal certification means personal criminal liability if the certification is materially false.

Section 404 requires management to assess and report on the effectiveness of internal controls over financial reporting, abbreviated as ICFR, and requires the external auditor to attest to that management assessment.

For IT and security professionals, SOX compliance translates into what are called IT General Controls, or ITGCs. These cover four areas:

**Logical access controls** — who can access financial systems and data, how access is granted and revoked, and how privileged access is monitored.

**Change management** — how changes to financial systems are reviewed, tested, and approved to prevent unauthorized or erroneous modifications.

**Computer operations** — monitoring, backup, and incident management for financial systems.

**Program development** — how new financial applications are developed, tested, and moved into production.

For security professionals, the SOX relationship is direct. Unauthorized access to financial systems, inadequate audit trails for privileged user activity, or uncontrolled changes to financial applications can all result in material SOX findings and potential restatement of financial results.

---

### [SLIDE 8] CCPA and CPRA — California's Privacy Framework

The California Consumer Privacy Act, CCPA, took effect in January 2020 and was significantly expanded by the California Privacy Rights Act, CPRA, effective January 2023. Together they represent the most comprehensive U.S. state privacy law and function as a de facto national standard because of California's economic size.

CCPA applies to for-profit businesses that collect personal information from California residents and meet at least one of three thresholds: annual gross revenue over $25 million; annual data buying, selling, or sharing involving 100,000 or more consumers or households; or deriving 50% or more of annual revenue from selling or sharing personal information.

Key rights under CCPA and CPRA include:

- The right to know what personal information is collected and how it is used
- The right to delete personal information
- The right to opt out of the sale or sharing of personal information
- The right to non-discrimination for exercising privacy rights
- The right to correct inaccurate personal information (added by CPRA)
- The right to limit the use of sensitive personal information (added by CPRA)

For security professionals, CCPA is notable because it creates a private right of action for individuals when their personal information is exposed in a data breach caused by the business's failure to implement and maintain reasonable security. California courts have referenced the Center for Internet Security Controls as a benchmark for reasonable security practices. This makes security implementation directly tied to civil litigation exposure.

---

### [SLIDE 9] Additional Regulatory Frameworks

Let me briefly address several additional frameworks that appear in the CISM exam and in enterprise practice.

**GLBA — Gramm-Leach-Bliley Act**: Applies to financial institutions. The Safeguards Rule, updated by the FTC in 2023, requires a written comprehensive information security program and now specifies controls including encryption, multi-factor authentication, and continuous monitoring. Financial institutions must designate a qualified individual to oversee the security program and report to the board annually.

**FERPA — Family Educational Rights and Privacy Act**: Applies to educational institutions receiving federal funding. Governs the privacy of student education records. Relevant to universities, K-12 schools, and EdTech companies that process student data.

**FISMA — Federal Information Security Modernization Act**: Applies to U.S. federal agencies and their contractors. Requires risk-based security programs aligned to NIST SP 800-53. Agencies undergo annual assessment and report to OMB and Congress. FedRAMP, the Federal Risk and Authorization Management Program, extends FISMA requirements to cloud service providers hosting federal data.

**NERC-CIP**: North American Electric Reliability Corporation Critical Infrastructure Protection standards. These are highly prescriptive cybersecurity requirements for owners and operators of the bulk electric system. Violations carry significant fines.

**State breach notification laws**: All 50 U.S. states now have breach notification laws. They differ significantly in definitions of personal information, notification timeframes, covered entities, and safe harbors for encrypted data. Managing multi-state notification obligations after a breach requires careful legal coordination.

---

### [SLIDE 10] Fair Information Practice Principles

Despite their differences, most major privacy laws share a common architecture rooted in the Fair Information Practice Principles, or FIPPs, which originate from a 1973 U.S. Department of Health, Education and Welfare report and were formalized in the OECD Privacy Guidelines of 1980.

The FIPPs include:

**Notice** — individuals must be informed about what data is collected, how it is used, and with whom it is shared.

**Choice** — individuals must have meaningful options about the collection and use of their personal information.

**Access** — individuals must be able to review, correct, and update their personal information.

**Security** — personal data must be protected against unauthorized access, disclosure, alteration, and destruction.

**Enforcement** — there must be mechanisms to enforce privacy commitments, including oversight, sanctions, and redress.

When you encounter a new privacy regulation, mapping it to the FIPPs will quickly reveal its structure and priorities. Regulations differ primarily in which FIPPs they emphasize and how strictly they enforce them.

---

### [SLIDE 11] Audit Management — Types and Structure

Now let us turn to compliance audits — what they are, who conducts them, and how to manage them effectively.

An audit is an independent, systematic examination of an organization's controls, processes, and records to assess whether they conform to a defined standard or requirement. The word "independent" is critical — the value of an audit comes from the absence of conflict of interest.

Audits fall into three categories based on who conducts them.

**First-party audits** — also called internal audits — are conducted by the organization's own internal audit function. Their purpose is to identify weaknesses before external parties do, test control effectiveness, and support continuous improvement.

**Second-party audits** are conducted by a customer or business partner assessing your controls as a condition of doing business. These are common in supply chain security relationships. A major retailer auditing a logistics vendor's security controls is a second-party audit.

**Third-party audits** are conducted by independent external parties. Examples include PCI QSA assessments, SOC 2 Type II audits conducted by CPA firms, ISO 27001 certification audits, and HIPAA audits by the HHS Office for Civil Rights. Third-party audit reports are often required by regulators, customers, and investors as evidence of compliance.

---

### [SLIDE 12] The Audit Lifecycle

A well-managed audit follows a defined lifecycle that security managers should understand and plan for.

**Planning phase**: The auditor and auditee agree on scope, objectives, timelines, evidence requirements, and key contacts. Organizations with mature compliance programs use this phase to conduct pre-audit readiness assessments — essentially auditing themselves before the auditor arrives.

**Fieldwork phase**: The auditor reviews documentation, conducts interviews with process owners and technical staff, tests controls to verify they operate as documented, and collects evidence. Auditees should designate a single point of contact — sometimes called an audit liaison — to manage evidence requests, schedule interviews, and track deliverables.

**Reporting phase**: The auditor drafts findings, observations, and recommendations. Auditees typically have an opportunity to review draft findings, correct factual inaccuracies, and provide management responses that acknowledge findings and describe remediation plans.

**Remediation phase**: The auditee implements corrective actions for findings. Follow-up procedures — which may include a formal re-test audit — verify that remediation was completed and effective.

**Continuous monitoring**: Modern compliance programs do not wait for annual audits. They implement ongoing automated monitoring of controls, exception tracking, and evidence collection to maintain audit readiness year-round. This approach, sometimes called continuous compliance monitoring, reduces the scramble before each audit cycle.

---

### [SLIDE 13] Building a Compliance Management Program

A compliance management program is not a project with a start and end date. It is an ongoing operational function that requires governance, resources, and leadership commitment. Let me describe its key components.

**Regulatory inventory**: A documented catalog of all regulations, contractual obligations, and industry standards that apply to the organization, with assigned ownership for each. This inventory must be maintained and updated as the regulatory environment changes.

**Control mapping**: A master control framework that maps individual security controls to multiple regulatory requirements simultaneously. For example, an encryption-at-rest control might simultaneously satisfy HIPAA Security Rule requirements, PCI-DSS Requirement 3, GDPR Article 32, and SOX IT general controls. This is called integrated or unified compliance, and it dramatically reduces the cost and complexity of managing multiple regulatory obligations.

**Evidence management**: A systematic process for collecting, storing, and retrieving compliance evidence. Modern organizations use GRC platforms — Governance, Risk, and Compliance software — to automate evidence collection from technical systems, maintain evidence archives, and produce audit packages on demand.

**Exception management**: A documented process for identifying, approving, tracking, and remediating control gaps and exceptions. Exceptions should have formal approval, defined compensating controls, expiration dates, and executive sign-off for significant exceptions.

**Training and awareness**: All employees must understand their compliance obligations relevant to their roles. This includes annual general compliance training, role-specific training for employees with access to sensitive data, and just-in-time training when new regulatory requirements take effect.

---

### [SLIDE 14] Unified Compliance Strategy

One of the most common challenges security managers face is managing multiple overlapping regulations simultaneously. A company operating in the healthcare payment space might simultaneously face HIPAA, PCI-DSS, SOX, applicable state breach notification laws, and GDPR if they serve European patients. Building separate compliance programs for each regulation is duplicative, expensive, and creates inconsistency.

The solution is the unified control framework. Rather than building parallel compliance programs, you build a single control library and map each control to every applicable regulatory requirement. When a control is tested or evidenced, that evidence satisfies multiple regulatory obligations at once.

Common implementations use NIST CSF or ISO 27001 Annex A as the organizing control catalog, then map regulatory requirements to specific controls. Pre-built crosswalk mappings — provided by HITRUST, the Unified Compliance Framework, NIST, and GRC platform vendors — accelerate this work.

The business case is clear: unified compliance costs significantly less to operate than siloed compliance programs, produces more consistent evidence, and reduces the organizational burden of multiple simultaneous audit preparations.

---

### [SLIDE 15] The CISM Professional's Role in Compliance

From a CISM perspective, the information security manager plays a central role in the organization's compliance program. That role includes:

**Advising executive leadership** on regulatory obligations, their resource implications, and the consequence of non-compliance. The board needs to understand regulatory risk in business terms.

**Designing and implementing controls** that satisfy multiple regulatory requirements efficiently, using the unified compliance approach.

**Managing audits** as both the organizational coordinator and a subject matter expert. Security managers must be able to speak to both technical controls and their governance rationale.

**Reporting compliance posture to leadership** through metrics, dashboards, and periodic briefings. Compliance status should be a standing item in security governance reporting.

**Managing third-party risk** — ensuring vendors, cloud providers, and business partners meet the same compliance obligations the organization faces. Vendor compliance failures become your compliance failures.

**Staying current on regulatory change** through professional association memberships, legal counsel relationships, and regulatory monitoring programs.

---

### [SLIDE 16] Compliance Failures and Their Consequences

Let us examine what happens when compliance programs fail — because understanding consequences drives organizational commitment.

**Regulatory penalties** can be existential. Meta's $1.3 billion GDPR fine in 2023 for unlawful data transfers was the largest GDPR penalty to date. British Airways received an initial GDPR fine of 183 million pounds following a breach affecting 500,000 customers. Uber paid $148 million to settle FTC charges related to a breach the company concealed from regulators.

**Civil liability** following data breaches includes class action lawsuits, individual claims under CCPA's private right of action, and consumer protection claims. Legal costs and settlements following major breaches routinely exceed the cost of the controls that could have prevented them.

**Reputational damage** manifests as customer churn, loss of business partner relationships, difficulty recruiting talent, and depressed stock valuations. The Equifax breach cost the company an estimated $1.4 billion including a $700 million FTC settlement.

**Operational disruption** can include consent decrees that impose operational restrictions, loss of payment processing capability for PCI non-compliance, and federal contract debarment for FISMA failures.

**Criminal liability** for individuals represents an emerging and significant trend. In 2023, the former Uber CISO Joseph Sullivan was sentenced to three years of probation for concealing a data breach from the FTC. The SEC's 2023 cyber disclosure charges against SolarWinds and its CISO established that executives can face personal liability for misleading investors about cybersecurity practices and breaches.

---

### [SLIDE 17] Emerging Regulatory Trends

The regulatory landscape continues to evolve rapidly. Let me highlight trends that will shape compliance practice over the next several years.

**Proliferation of U.S. state privacy laws**: Following California's lead, states including Virginia, Colorado, Connecticut, Utah, Oregon, Texas, Florida, and others have enacted comprehensive privacy laws. Each has different scope, rights, and enforcement mechanisms. Federal comprehensive privacy legislation — the American Privacy Rights Act — continues to be debated in Congress.

**AI governance regulation**: The EU AI Act, which began phasing in during 2024, creates risk-tiered requirements for AI systems. High-risk AI applications face conformity assessments, transparency requirements, and prohibited use cases. U.S. executive orders and agency guidance from NIST and the FTC are establishing AI governance expectations for U.S. organizations.

**Cyber incident reporting mandates**: The SEC's cybersecurity disclosure rules require public companies to report material cybersecurity incidents within four business days of determining materiality and to annually disclose cybersecurity governance and risk management practices. CISA's Cyber Incident Reporting for Critical Infrastructure Act, CIRCIA, will require critical infrastructure operators to report covered incidents within 24 to 72 hours once implementing regulations are finalized.

**Software and supply chain security**: Executive Order 14028 and CISA's Secure Software Development Framework are establishing software security standards for federal contractors. Software Bills of Materials, or SBOMs, are becoming a contractual requirement in government procurement.

---

### [SLIDE 18] Module Summary and Look Ahead

Let me bring this together.

Regulatory compliance is a core responsibility of the information security function — not a compliance department responsibility delegated away from security. The major frameworks we covered today — GDPR, HIPAA, PCI-DSS, SOX, and CCPA — each reflect society's judgment about acceptable risk in their respective domains, and each creates binding obligations that carry significant consequences for non-compliance.

Effective compliance management requires a regulatory inventory, a unified control framework, continuous monitoring, proactive audit management, and executive-level governance oversight.

The CISM professional must understand not just the technical requirements of each framework, but the governance structures, reporting obligations, organizational accountability, and strategic business consequences that make compliance a board-level concern.

In Module 16, our final module, we will review all four CISM domains in preparation for the certification exam, discuss exam strategy, work through practice questions, and talk about career pathways in cybersecurity governance and compliance.

Thank you for your dedication and engagement throughout this course. I will see you in Module 16.

---

*End of Script — Module 15*

*Word count: approximately 2,650 words | Estimated delivery: 20–24 minutes at 110–130 words per minute*
