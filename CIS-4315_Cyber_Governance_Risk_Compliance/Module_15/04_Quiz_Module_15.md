# Quiz: Module 15 — Legal, Regulatory, and Compliance Frameworks

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 1 (Information Security Governance) and Domain 3 (Information Security Program Development and Management)

---

**Question 1**

A U.S.-based e-commerce company collects shipping addresses and purchase histories from customers across the European Union. The company has no physical presence in Europe. Which statement best describes the company's GDPR obligations?

- A) GDPR does not apply because the company has no physical presence or establishment in the EU
- B) GDPR applies because the company monitors the behavior of or offers goods and services to EU residents, regardless of where the company is established
- C) GDPR applies only if the company's annual EU revenue exceeds €10 million
- D) GDPR applies only to the EU-resident data that is physically stored on servers located within the EU

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: GDPR's extraterritorial scope under Article 3 explicitly applies to organizations outside the EU when they offer goods or services to EU residents or monitor their behavior. Physical presence is not required for GDPR to apply.
- Why B is correct: Article 3(2) of GDPR establishes that the regulation applies to processing of EU residents' data by controllers not established in the EU when the processing relates to offering goods or services to those data subjects. An e-commerce company selling to EU customers meets this criterion.
- Why C is incorrect: GDPR has no revenue threshold for applicability. Penalty calculations may reference revenue, but the threshold for the regulation to apply is based on data processing activity, not revenue size.
- Why D is incorrect: GDPR's application is based on the residency of the data subject and the nature of the processing relationship, not the physical location of servers. Data stored anywhere in the world is subject to GDPR if the controller-subject relationship triggers applicability.

---

**Question 2**

A covered healthcare entity discovers on a Monday that a ransomware attack has encrypted servers containing electronic PHI for 12,000 patients. The breach also involved personal data for approximately 800 EU residents who received telehealth services. What are the two most time-sensitive regulatory notification deadlines the organization faces?

- A) HIPAA individual notification within 30 days; GDPR supervisory notification within 7 days
- B) GDPR supervisory authority notification within 72 hours; HIPAA individual notification within 60 days of discovery
- C) HIPAA individual notification within 72 hours; GDPR individual notification within 30 days
- D) Both GDPR and HIPAA require notification within 72 hours of discovery

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: GDPR's supervisory authority deadline is 72 hours, not 7 days. HIPAA's individual notification deadline is 60 days, not 30 days.
- Why B is correct: GDPR Article 33 requires notification to the relevant supervisory authority within 72 hours of becoming aware of a personal data breach. HIPAA's Breach Notification Rule (45 CFR § 164.404) requires notification to affected individuals within 60 days of discovery. These are the two correctly stated timelines.
- Why C is incorrect: HIPAA does not require individual notification within 72 hours; GDPR's 72-hour requirement is for supervisory authority notification, not necessarily for individual notification.
- Why D is incorrect: HIPAA's timeline is 60 days for individual notification, not 72 hours. Only GDPR imposes the 72-hour supervisory notification window.

---

**Question 3**

An organization subject to PCI-DSS v4.0 currently requires passwords of at least 8 characters for all user accounts accessing the cardholder data environment. A security manager reviewing PCI-DSS v4.0 Requirement 8 notes that this falls short of the updated standard. What is the correct minimum password length under PCI-DSS v4.0, and how should the security manager document this gap?

- A) PCI-DSS v4.0 requires a minimum of 10 characters; document as a finding in the risk register with a target remediation date
- B) PCI-DSS v4.0 requires a minimum of 12 characters; document as a control gap with a formal exception or remediation plan approved by management
- C) PCI-DSS v4.0 requires a minimum of 16 characters; document as a critical finding requiring immediate remediation before any audit
- D) PCI-DSS v4.0 did not change the minimum password length from v3.2.1; the existing 8-character policy remains compliant

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: PCI-DSS v4.0 specifies a minimum of 12 characters, not 10. While documentation in the risk register is appropriate, a formal exception or remediation plan with management approval is the proper gap management approach.
- Why B is correct: PCI-DSS v4.0 Requirement 8.3.6 raised the minimum password length from 7 characters to 12 characters for user accounts. A control gap must be formally documented with either a compensating control or a time-bound remediation plan approved by management and the QSA.
- Why C is incorrect: PCI-DSS v4.0 requires 12 characters, not 16. Requiring immediate remediation before any audit is not the standard gap management process; formal documentation and a remediation timeline are the appropriate response.
- Why D is incorrect: PCI-DSS v4.0 did change the minimum password requirement. Version 3.2.1 required a minimum of 7 characters; version 4.0 requires 12 characters for user passwords when used as an authentication factor.

---

**Question 4**

The Sarbanes-Oxley Act Section 404 requires management to assess and report on the effectiveness of internal controls over financial reporting. For an IT security manager at a publicly traded company, which of the following activities is most directly driven by SOX Section 404 compliance?

- A) Conducting annual penetration tests of the company's public-facing web applications
- B) Reviewing and certifying the access control lists for the company's financial systems, ensuring only authorized personnel can modify financial records
- C) Implementing a security information and event management (SIEM) platform for real-time threat detection
- D) Encrypting all employee laptop hard drives with full-disk encryption

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Penetration testing is a security best practice and may be required by other frameworks such as PCI-DSS, but it is not specifically driven by SOX Section 404. SOX focuses on controls over the integrity of financial reporting data.
- Why B is correct: SOX Section 404 directly requires effective internal controls over financial reporting. The IT General Controls domain of logical access — specifically controlling who can access and modify financial systems and data — is a primary SOX ITGC requirement. Access control reviews for financial systems are a core SOX compliance activity.
- Why C is incorrect: SIEM implementation supports security monitoring broadly and may generate evidence for various compliance frameworks, but it is not specifically a SOX Section 404 requirement. SOX ITGCs focus on logical access, change management, computer operations, and program development for financial systems.
- Why D is incorrect: Full-disk encryption for laptops is a security control relevant to data protection regulations such as HIPAA and GLBA, but it is not a primary driver of SOX Section 404 compliance. SOX focuses on financial data integrity, not endpoint protection broadly.

---

**Question 5**

A California resident submits a request to a for-profit business covered by CCPA asking the company to delete all personal information the company holds about them. The company's legal team states that the customer's information must be retained for three more years to comply with a federal tax records retention requirement. What is the correct response under CCPA?

- A) The company must honor the deletion request within 45 days regardless of any conflicting legal obligation
- B) The company may decline the deletion request to the extent necessary to comply with a legal obligation, such as a tax records retention requirement, and must inform the consumer of the legal obligation basis for the refusal
- C) The company must delete all data except that specifically required by the tax retention law, and must provide the consumer with the retained data in a portable format
- D) The company must seek a court order before declining any CCPA deletion request based on a conflicting legal obligation

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: CCPA provides several exceptions to the right to delete, including when retaining data is necessary to comply with a legal obligation. Honoring the deletion request unconditionally when a legal retention obligation exists would put the company in violation of that obligation.
- Why B is correct: CCPA's right to delete is subject to several exceptions enumerated in Civil Code § 1798.105(d), including the exception for retaining data necessary to comply with a legal obligation. The company must inform the consumer of the basis for declining the request. This is the legally correct and CISM-aligned response.
- Why C is incorrect: While deleting data not covered by the retention exception and offering portability reflects good privacy practice, CCPA does not require the company to offer portability as a condition of invoking the legal obligation exception for deletion. The portability right is a separate CCPA right with its own conditions.
- Why D is incorrect: No court order is required to invoke a statutory exception to the CCPA right to delete. The exceptions are self-executing when the specified conditions are met; the company must document its basis and inform the consumer, but does not need judicial approval.

---

**Question 6**

An information security manager is building a compliance program for an organization subject to HIPAA, PCI-DSS, and the GLBA Safeguards Rule. The manager proposes implementing a single encryption control — AES-256 encryption for all data at rest — and documenting it once rather than creating separate encryption policies for each framework. What best describes this approach?

- A) This approach is non-compliant because each regulatory framework requires a separate, independently documented encryption policy
- B) This approach reflects unified compliance management, where a single well-designed control and its documentation can simultaneously satisfy overlapping requirements across multiple frameworks
- C) This approach is acceptable only if the organization obtains written waivers from each regulatory body confirming that shared documentation satisfies each framework's requirements
- D) This approach is acceptable for HIPAA and GLBA but not for PCI-DSS, which requires controls to be documented separately in a Report on Compliance

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: No major regulatory framework requires that compliance controls be documented separately from controls serving other frameworks. The principle of integrated or unified compliance is widely accepted and explicitly supported by frameworks such as HITRUST, which provides crosswalk mappings for exactly this purpose.
- Why B is correct: Unified compliance management is a recognized best practice in which a single control library is mapped to multiple regulatory requirements. A single AES-256 encryption control at rest can simultaneously satisfy HIPAA Security Rule addressable safeguards, PCI-DSS Requirement 3.5, and the GLBA Safeguards Rule encryption requirement. One documented control, one testing event, multiple obligations satisfied.
- Why C is incorrect: No regulatory framework requires organizations to seek a waiver before using a unified control to satisfy multiple obligations. The frameworks do not create exclusive claims on the controls designed to meet them.
- Why D is incorrect: PCI-DSS does not prohibit controls from also satisfying other frameworks. The QSA documents the control's compliance with PCI-DSS requirements in the ROC regardless of whether the same control serves additional purposes. There is no PCI-DSS prohibition against unified compliance documentation.

---

**Question 7**

An organization's security manager learns that a state attorney general has opened an investigation into a data breach that occurred eight months ago. The breach involved unencrypted personal information of 6,000 state residents. The state's breach notification law requires notification within 30 days of discovery. The organization notified affected individuals 52 days after discovery, citing the complexity of the investigation. What is the most significant compliance risk the organization faces?

- A) The organization faces risk only from the underlying breach, not from the notification timing, because the delay was caused by a good-faith investigation
- B) The organization faces regulatory liability for the breach itself and a separate, independent regulatory violation for failing to notify within the required 30-day timeframe
- C) The 22-day delay is within the common law "reasonable delay" standard and is unlikely to result in regulatory action
- D) The organization's only risk is civil lawsuits from affected individuals, not regulatory enforcement action from the attorney general

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Good faith investigation complexity does not automatically excuse a notification timeline violation. Most state notification laws specify a firm deadline, and failure to meet it constitutes a separate violation from the underlying breach event. Regulators may consider mitigating factors in determining penalties, but the violation itself exists independently.
- Why B is correct: Under most state breach notification laws, failure to notify within the specified deadline is a separate and independent violation from the breach itself. The organization may face regulatory action for both the breach (if negligence is found) and for the late notification. Regulators treat notification timeline compliance as a standalone obligation.
- Why C is incorrect: There is no general common law "reasonable delay" safe harbor for state breach notification violations. The 30-day statutory deadline is the applicable standard, not a general reasonableness test. Some laws allow extensions for law enforcement coordination, but that must be specifically invoked with documentation.
- Why D is incorrect: State attorneys general have broad enforcement authority under consumer protection and breach notification statutes. Regulatory enforcement from the AG's office is both legally available and commonly pursued in significant breach cases. Civil suits and regulatory action are not mutually exclusive.

---

**Question 8**

A security manager is preparing an organization for its first SOC 2 Type II audit. A colleague asks what the difference is between a SOC 2 Type I report and a SOC 2 Type II report. What is the accurate distinction?

- A) Type I covers security controls only; Type II covers all five Trust Services Criteria including security, availability, processing integrity, confidentiality, and privacy
- B) Type I assesses whether controls are suitably designed as of a specific point in time; Type II assesses whether controls are suitably designed and operated effectively over a defined period, typically six to twelve months
- C) Type I is conducted by an internal auditor; Type II is conducted by an independent external CPA firm
- D) Type I is required for organizations processing fewer than 10,000 records; Type II is required for larger organizations

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Both Type I and Type II reports can cover any combination of the five Trust Services Criteria. The scope of criteria covered is not what distinguishes Type I from Type II.
- Why B is correct: This is the accurate and standard definition. A SOC 2 Type I report attests that controls are suitably designed as of a point-in-time observation date. A SOC 2 Type II report attests that controls are suitably designed and that they operated effectively throughout the audit period (typically six to twelve months). Type II provides significantly more assurance to users of the report.
- Why C is incorrect: Both Type I and Type II SOC 2 reports are conducted by independent external CPA firms. Internal auditors do not issue SOC 2 reports; SOC 2 is a third-party attestation standard governed by the AICPA.
- Why D is incorrect: There is no record count threshold that determines whether Type I or Type II applies. The choice between report types is based on what level of assurance the organization's clients require, not on the size of the organization's data processing volume.

---

**Question 9**

The FTC's updated GLBA Safeguards Rule, effective 2023, requires financial institutions to designate a qualified individual responsible for the information security program and to provide annual written reports to the board. What does this requirement most directly reflect in terms of information security governance principles?

- A) It establishes a technical security baseline by specifying the encryption algorithms financial institutions must use
- B) It elevates information security to a board-level governance concern by requiring executive accountability, designated ownership, and board oversight of the security program
- C) It creates a new financial institution licensing requirement administered by the FTC for information security professionals
- D) It primarily addresses consumer rights to opt out of information sharing, which the security program must technically support

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: The qualified individual and board reporting requirements are governance requirements, not technical specifications. While the updated Safeguards Rule does specify certain technical controls such as encryption and MFA, the designated individual and board reporting provisions specifically address governance accountability structures.
- Why B is correct: Requiring a designated qualified individual (a named security program owner with board access) and mandating annual board reporting reflects core information security governance principles. These requirements ensure that security is owned at the executive level, that the board exercises oversight, and that accountability is formally assigned — all hallmarks of sound governance as defined in CISM Domain 1.
- Why C is incorrect: The GLBA Safeguards Rule does not create a licensing or certification requirement for security professionals. It requires financial institutions to designate a qualified individual; qualification criteria are determined by the institution, not imposed as a professional license by the FTC.
- Why D is incorrect: Consumer opt-out rights are addressed in GLBA's Privacy Rule, not the Safeguards Rule. The Safeguards Rule governs the security of nonpublic personal information, not consumer choice regarding information sharing. These are separate regulatory components with different obligations.

---

**Question 10**

An organization has completed its annual compliance review and identified 23 control gaps across HIPAA, PCI-DSS, and GDPR. The CISO presents the gaps to the board and recommends addressing all 23 gaps within the next 90 days. The board questions whether a 90-day timeline is realistic given resource constraints. What is the most appropriate CISM-aligned approach to prioritizing the remediation effort?

- A) Address gaps in alphabetical order by framework name to ensure all frameworks receive equal attention within the available timeline
- B) Prioritize gaps based on residual risk — the likelihood and potential impact of exploitation or regulatory action — ensuring the highest-risk gaps receive immediate attention regardless of which framework they come from
- C) Prioritize gaps from whichever framework carries the highest maximum penalty, completing all gaps in that framework before addressing others
- D) Delegate all 23 gaps to the affected system owners simultaneously so that all gaps are addressed in parallel within the 90-day window

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Alphabetical ordering by framework name has no relationship to risk or business impact. It would result in arbitrary prioritization that fails to protect the organization from its most significant exposures first.
- Why B is correct: CISM Domain 2 establishes risk-based prioritization as the foundational principle for resource allocation decisions. Residual risk — the remaining risk after existing controls are considered — should drive remediation sequencing. Gaps with high likelihood of exploitation and severe business impact (operational disruption, regulatory penalty, reputational damage) must be addressed before lower-risk gaps, regardless of which framework they fall under.
- Why C is incorrect: Maximum penalty framework prioritization is a common but flawed approach. A high-penalty framework's low-risk gaps may be far less urgent than a lower-penalty framework's critical gaps. Risk to the organization, not the headline penalty figure, should drive prioritization.
- Why D is incorrect: Delegating all gaps simultaneously without prioritization guidance or resource coordination may result in the most critical gaps receiving insufficient attention while resources are spread across low-priority items. Parallel execution without risk-based sequencing is not a management approach — it is an absence of management.

---

*End of Quiz — Module 15*
