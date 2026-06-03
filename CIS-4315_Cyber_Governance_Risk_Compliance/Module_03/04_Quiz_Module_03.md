# Quiz: Module 03 — Risk Management Frameworks

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

**Instructions:** Choose the single best answer for each question.

---

### Question 1

Which step was added to the NIST Risk Management Framework in Special Publication 800-37, Revision 2, that did not exist in the original framework?

- A) Categorize
- B) Monitor
- C) Prepare
- D) Authorize

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: NIST SP 800-37 Revision 2 introduced the Prepare step as Step 1 to establish organizational and system-level context before risk management activities begin. It was added to improve efficiency by ensuring foundational work — identifying risk executives, establishing risk tolerance, identifying common controls — is completed before system-level steps start.
- Why A is incorrect: Categorize existed in the original RMF as the first step; Revision 2 made it Step 2 after adding Prepare.
- Why B is incorrect: Monitor was part of the original RMF as the final ongoing step; it was not introduced in Revision 2.
- Why D is incorrect: Authorize was part of the original RMF; it is the formal risk acceptance decision step and predates Revision 2.

---

### Question 2

An organization's CISO wants to implement a risk management approach that applies equally to financial risk, cybersecurity risk, operational risk, and reputational risk across all global business units without requiring certification. Which framework best meets this need?

- A) NIST SP 800-37 RMF
- B) ISO 31000:2018
- C) OCTAVE Allegro
- D) FAIR

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: ISO 31000 is sector-agnostic, risk-type-agnostic, and internationally applicable. It is a guidance standard (not certifiable) designed for enterprise-wide risk management across any risk type, making it the ideal choice for a global, multi-risk-type program.
- Why A is incorrect: NIST RMF is specific to information systems, prescriptive in its steps, and primarily designed for U.S. federal agencies and federal contractors — not for broad enterprise risk across all risk categories globally.
- Why C is incorrect: OCTAVE Allegro is a self-directed methodology focused specifically on information asset risk assessment — not a framework for enterprise-wide, multi-category risk management.
- Why D is incorrect: FAIR is a quantitative model for expressing information risk in financial terms. It does not define an enterprise risk management process or address non-information risk categories.

---

### Question 3

A federal agency's Authorizing Official has reviewed the Security Assessment Report and Plan of Action and Milestones for a new grants management system. The residual risk is within the agency's established tolerance. What is the correct next action under the NIST RMF?

- A) Return the system to the Categorize step to confirm the impact level
- B) Issue a formal Authorization to Operate and begin continuous monitoring
- C) Require the security team to remediate all findings before any authorization decision
- D) Transfer the system to the cloud provider and restart the RMF process

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: When the AO determines residual risk is acceptable, the correct RMF action is to issue an Authorization to Operate (Step 6 — Authorize) and transition to ongoing monitoring (Step 7 — Monitor). This is the intended outcome of the authorization process.
- Why A is incorrect: Re-categorization is triggered by significant changes to the system or its environment, not by a routine authorization review with acceptable residual risk.
- Why C is incorrect: While serious deficiencies may delay authorization, requiring zero deficiencies before any ATO decision is not NIST RMF policy. ATOs can be issued with a POA&M documenting how remaining items will be remediated.
- Why D is incorrect: Migrating to a different environment would trigger a new system change requiring updated documentation and potentially re-authorization, but there is no basis for this action in the scenario as described.

---

### Question 4

In the FAIR risk model, what two top-level components combine to produce a risk estimate?

- A) Threat Event Frequency and Vulnerability
- B) Asset Value and Exposure Factor
- C) Probable Frequency and Probable Magnitude of Future Loss
- D) Single Loss Expectancy and Annualized Rate of Occurrence

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: FAIR defines risk as Probable Frequency multiplied by Probable Magnitude of Future Loss. This is the top-level decomposition in the FAIR ontology from which all other factors derive.
- Why A is incorrect: Threat Event Frequency and Vulnerability are sub-components of the Frequency branch in FAIR, not the two top-level components. Their product gives Loss Event Frequency, which feeds into the Frequency side of the top-level equation.
- Why B is incorrect: Asset Value and Exposure Factor are inputs to the Single Loss Expectancy (SLE) calculation in the traditional qualitative/quantitative model — they are not part of the FAIR ontology's top-level decomposition.
- Why D is incorrect: SLE and ARO are inputs to the Annualized Loss Expectancy (ALE) formula from traditional quantitative risk analysis, not the FAIR model's risk definition.

---

### Question 5

OCTAVE Allegro Phase 1 produces "asset-based threat profiles." What is the primary purpose of these profiles?

- A) To document all open vulnerabilities discovered by an automated vulnerability scanner
- B) To assign a dollar value to each critical information asset for insurance purposes
- C) To create structured descriptions of threats, threat actors, and potential outcomes for each critical information asset
- D) To generate a list of NIST SP 800-53 controls that should be applied to each system

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: OCTAVE Allegro Phase 1 builds threat profiles by identifying critical information assets, documenting their security requirements, identifying the containers where they reside, and developing structured threat scenarios. The output is an asset-centric threat profile — not a control list or a vulnerability scan result.
- Why A is incorrect: OCTAVE Allegro does not use automated vulnerability scanners in Phase 1. Technical vulnerability analysis is conducted in Phase 2 (Identify Infrastructure Vulnerabilities), and even then it is focused on infrastructure supporting the asset, not automated scanning results.
- Why B is incorrect: OCTAVE Allegro does not produce dollar valuations of assets. Financial quantification of risk is the domain of the FAIR model, not OCTAVE.
- Why D is incorrect: NIST SP 800-53 control selection is specific to the NIST RMF Select step. OCTAVE does not reference or produce control baselines from NIST publications.

---

### Question 6

An organization is deciding whether to use NIST RMF or ISO 31000 as its primary risk framework. The organization is a multinational manufacturing company with no U.S. federal contracts, operating in 14 countries across three regulatory regimes. Which framework is more appropriate and why?

- A) NIST RMF, because it provides the most comprehensive set of security controls
- B) ISO 31000, because it is principles-based, internationally applicable, and not tied to any single regulatory regime
- C) NIST RMF, because its seven-step process is more detailed than ISO 31000's guidance
- D) ISO 31000, because it requires organizational certification, providing external assurance to regulators

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: ISO 31000 was designed for exactly this use case — any organization, any sector, any country. Its principles-based approach allows the company to adapt the framework to each of its 14 operating environments without being bound to U.S. regulatory requirements.
- Why A is incorrect: NIST RMF's comprehensive control catalog (SP 800-53) is valuable for U.S. federal-aligned organizations, but it is not the most appropriate choice for a multinational manufacturer with no U.S. federal obligations. The framework's prescriptive, U.S.-centric nature would create unnecessary compliance burden.
- Why C is incorrect: The NIST RMF's detailed steps are an asset for federal system authorization but a liability for a broad enterprise risk management program across multiple international regulatory environments. More detail is not always more appropriate.
- Why D is incorrect: ISO 31000 is explicitly not a certifiable standard. Organizations cannot receive ISO 31000 certification. ISO 27001 is the certifiable information security management standard; these are frequently confused on the exam.

---

### Question 7

A small nonprofit organization with eight IT staff members needs to conduct a risk assessment of its donor database. The organization has no previous risk assessment experience and cannot afford external consultants. Which framework is most appropriate?

- A) NIST RMF, because it provides step-by-step guidance
- B) FAIR, because it produces financial outputs the board will understand
- C) OCTAVE-S, because it is designed for small organizations conducting self-directed internal assessments
- D) ISO 31000, because it applies to any organization size

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: OCTAVE-S was specifically designed for small organizations (fewer than 100 employees) to conduct self-directed risk assessments with their own staff without external consultants. It is the only framework among the options explicitly designed for this combination of small size, internal team, and no prior experience.
- Why A is incorrect: NIST RMF is prescriptive and resource-intensive. It requires independent assessors, formal authorization packages, and ongoing monitoring infrastructure — all beyond the capability of an eight-person IT team at a nonprofit.
- Why B is incorrect: FAIR requires statistical analysis, probability distribution estimation, and often Monte Carlo simulation software. It has a steep learning curve that makes it inappropriate for an organization with no prior risk assessment experience.
- Why D is incorrect: While ISO 31000 is scalable in theory, it is highly abstract and principles-based. Without experienced practitioners, a small organization following ISO 31000 alone would struggle to produce actionable outputs.

---

### Question 8

In the NIST RMF, what document serves as the primary repository describing a system's security controls, implementation details, and overall security posture?

- A) Plan of Action and Milestones (POA&M)
- B) Security Assessment Report (SAR)
- C) System Security Plan (SSP)
- D) Authorization Decision Document (ADD)

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The System Security Plan is the central RMF artifact. It documents the system's mission, environment, security categorization, implemented controls (with implementation details), and inherited controls. All other authorization package documents reference the SSP.
- Why A is incorrect: The POA&M documents known security deficiencies, planned remediation actions, and target completion dates. It is part of the authorization package alongside the SSP and SAR but does not describe the overall security posture.
- Why B is incorrect: The SAR documents the results of the security control assessment — what the assessor found when evaluating controls. It is an assessment output, not a description of intended security posture.
- Why D is incorrect: The Authorization Decision Document records the AO's formal risk acceptance decision and ATO conditions. It is the output of the Authorize step, not a security posture description.

---

### Question 9

ISO 31000 defines eight principles of effective risk management. Which of the following is one of those principles?

- A) Organizations must achieve ISO 31000 certification before conducting risk assessments
- B) Risk management must be integrated into all organizational activities, not treated as a separate program
- C) Risk assessments must be conducted by external consultants to ensure objectivity
- D) All risks must be quantified in financial terms before treatment decisions can be made

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Integration is one of the eight ISO 31000:2018 principles. It states that risk management should be embedded throughout the organization — in strategy setting, operations, and decision-making — rather than existing as an isolated compliance function.
- Why A is incorrect: ISO 31000 is a guidance standard, not a certifiable standard. There is no ISO 31000 certification. This is a common distractor on the CISM exam.
- Why C is incorrect: ISO 31000 does not require external consultants. OCTAVE is explicitly designed for internal, self-directed assessment. ISO 31000 encourages inclusive stakeholder participation, which can include external parties but does not require them.
- Why D is incorrect: ISO 31000 does not require financial quantification. It supports both qualitative and quantitative risk analysis and does not prescribe which method must be used.

---

### Question 10

A CISO needs to present the cybersecurity risk of an unpatched critical server to the organization's board of directors. The board is composed primarily of business executives with no technical background. Which framework's output would be most effective for this communication?

- A) NIST RMF, because the authorization status (ATO or no ATO) is a clear binary result
- B) OCTAVE, because the threat profile narrative is descriptive and non-technical
- C) ISO 31000, because its principles-based approach gives the board strategic context
- D) FAIR, because it expresses the risk as a range of probable annual financial loss in dollars

**Correct Answer:** D

**Distractor Analysis:**

- Why D is correct: FAIR produces a financial quantification of risk — for example, "This unpatched server has an expected annual loss exposure between $800,000 and $3.2M." Business executives make investment decisions in financial terms, and FAIR's dollar-denominated output directly enables that conversation.
- Why A is incorrect: An ATO status tells the board whether a system meets compliance requirements, not what the financial exposure is. Business leaders need to understand the cost of inaction, which a binary authorization status does not convey.
- Why B is incorrect: OCTAVE threat narrative profiles describe scenarios well but do not translate risk into financial terms. Boards typically require financial context to approve remediation budgets.
- Why C is incorrect: ISO 31000's principles and process guidance provide strategic context for building a risk management program, but do not produce specific risk outputs suitable for a board briefing on a particular server's risk exposure.

---

*End of Module 03 Quiz*
