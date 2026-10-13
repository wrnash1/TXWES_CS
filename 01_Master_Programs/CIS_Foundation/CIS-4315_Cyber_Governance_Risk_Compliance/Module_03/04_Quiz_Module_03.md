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

End of Module 03 Quiz

---

### Question 11

The NIST Risk Management Framework Step 3 is "Select." What is the primary output of this step?

- A) A completed risk assessment identifying all threats and vulnerabilities affecting the system
- B) A set of security controls chosen from NIST SP 800-53 that are tailored to the system's impact level and organizational requirements
- C) A formal authorization to operate (ATO) signed by the authorizing official
- D) A system security plan describing the overall security posture of the system

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Step 3 Select involves choosing the appropriate security controls from the NIST SP 800-53 catalog based on the system's FIPS 199 impact level (Low, Moderate, High), applying organization-defined parameters, and documenting the selection in a System Security Plan. The output is the tailored control set, not the plan itself.
- Why A is incorrect: Risk assessment occurs in Step 5 (Assess), after controls are selected and implemented. The Assess step evaluates whether the selected controls are operating as intended.
- Why C is incorrect: The ATO is the output of Step 5 (Authorize), the culminating governance decision made after controls are assessed and risk is evaluated by the authorizing official.
- Why D is incorrect: The System Security Plan is the documentation artifact that records the control selections, but it is initiated during Step 2 (Categorize) and finalized in Step 3. The plan itself is not the "primary output" — the tailored control selection documented within it is.

---

### Question 12

ISO 31000:2018 describes risk as the "effect of uncertainty on objectives." Which statement best reflects the implications of this definition for information security risk management?

- A) Risk is defined solely by the probability of a negative event occurring, independent of the organization's objectives
- B) Risk must be understood in the context of what the organization is trying to achieve — controls and risk decisions should be calibrated to protect those objectives specifically
- C) All uncertainty represents risk; therefore organizations should eliminate all uncertain conditions before proceeding with business activities
- D) ISO 31000 defines risk only in terms of negative consequences and does not account for the possibility that uncertainty may produce positive outcomes

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: ISO 31000's definition ties risk directly to objectives. This means the same threat event may be high-risk to one organization (if it threatens a core objective) and low-risk to another (if the threatened function is not critical). Security risk management must start with understanding organizational objectives, not just threat lists.
- Why A is incorrect: ISO 31000 explicitly links risk to objectives, not just probability. The definition is not a pure probability statement.
- Why C is incorrect: ISO 31000 does not advocate eliminating all uncertainty. Risk management involves making conscious decisions about which uncertainties to accept, treat, transfer, or avoid based on their potential effect on objectives.
- Why D is incorrect: ISO 31000 explicitly acknowledges that uncertainty can have positive as well as negative effects on objectives. The "effect of uncertainty" can include upside risk (opportunities) as well as downside risk (threats).

---

### Question 13

An information security analyst is using OCTAVE Allegro to assess risks for a university's student records system. During Phase 1, the team creates an information asset profile. What is the purpose of this profile?

- A) To identify all threat actors who have historically targeted university systems
- B) To document the asset's value, security requirements, and the containers in which it resides, creating the foundation for threat scenario development
- C) To select the security controls that will protect the asset from identified threats
- D) To calculate the probability and financial impact of each identified risk scenario

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: OCTAVE Allegro Phase 1 establishes information asset profiles that capture what the asset is, why it matters, what security properties are most important (confidentiality, integrity, availability), and where the asset exists across technical and non-technical environments (containers). This profile is the foundation from which threat scenarios are built in Phase 2.
- Why A is incorrect: Historical threat actor identification is threat intelligence work, not part of Phase 1 asset profiling. OCTAVE Allegro Phase 2 develops threat scenarios that may reference threat actors, but the Phase 1 activity is asset-focused.
- Why C is incorrect: Control selection is not part of OCTAVE Allegro's methodology. OCTAVE is a risk assessment framework, not a control selection framework. Control selection follows the risk assessment.
- Why D is incorrect: Financial impact calculation is characteristic of FAIR, not OCTAVE Allegro. OCTAVE uses a qualitative risk scoring approach, not quantitative financial impact calculation.

---

### Question 14

FAIR (Factor Analysis of Information Risk) decomposes risk into two top-level components. What are they?

- A) Threat likelihood and vulnerability severity
- B) Loss Event Frequency and Loss Magnitude
- C) Inherent risk and residual risk
- D) Probability of occurrence and impact rating

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: FAIR's foundational decomposition separates risk into Loss Event Frequency (how often a loss event is likely to occur) and Loss Magnitude (how much loss results when it does). Each top-level factor is further decomposed — frequency into threat event frequency and vulnerability; magnitude into primary and secondary loss. This decomposition enables quantitative financial estimation.
- Why A is incorrect: Threat likelihood and vulnerability severity are components of qualitative risk matrices, not FAIR's specific decomposition. FAIR uses more precisely defined terms derived from its ontology.
- Why C is incorrect: Inherent risk versus residual risk is a risk treatment concept describing the before-control and after-control risk states. It is not FAIR's primary decomposition.
- Why D is incorrect: Probability and impact are generic qualitative risk matrix terms. FAIR uses specific terms (Loss Event Frequency and Loss Magnitude) to enable quantitative, financially expressed risk analysis.

---

### Question 15

A federal agency uses NIST RMF for its information systems. The agency's authorizing official reviews the security assessment report and finds that three moderate-severity control deficiencies exist but decides to grant an ATO with conditions rather than deny authorization. Which NIST RMF concept does this decision illustrate?

- A) That NIST RMF requires all controls to be fully effective before an ATO can be granted
- B) Risk acceptance — the authorizing official acknowledges the residual risk from the deficiencies and accepts it as within acceptable limits for mission purposes
- C) Risk avoidance — the authorizing official has chosen to avoid the risk by requiring the system to operate under restricted conditions
- D) That the security assessment was conducted incorrectly because deficiencies should have been remediated before assessment

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: The ATO with conditions is one of the three possible Step 6 (Authorize) outcomes in NIST RMF. It reflects a formal risk acceptance decision by the authorizing official — an acknowledgment that the residual risk from the identified deficiencies is acceptable for the system's mission context and operational period. Risk acceptance under NIST RMF requires documentation and periodic review.
- Why A is incorrect: NIST RMF does not require all controls to be fully effective before an ATO can be issued. The framework explicitly recognizes that real operational systems have deficiencies and provides the ATO-with-conditions mechanism for exactly this scenario.
- Why C is incorrect: Risk avoidance would mean not operating the system at all. Granting an ATO — even with conditions — means accepting that the system will operate, which is acceptance, not avoidance.
- Why D is incorrect: Assessment is not dependent on prior remediation. The assessment reveals the current control state, which may include deficiencies. The authorizing official then decides whether to authorize, conditionally authorize, or deny — the process does not require pre-assessment remediation.

---

### Question 16

An organization uses ISO 31000:2018 as its enterprise risk management framework. A business unit manager argues that because a new product launch has only a 15% probability of triggering a regulatory penalty, it does not constitute a significant risk. The risk manager disagrees. Which ISO 31000 principle best supports the risk manager's position?

- A) Risk management should be transparent and inclusive of all stakeholder views
- B) Risk is the effect of uncertainty on objectives — a 15% probability of a regulatory penalty may represent a significant effect on the organization's strategic and financial objectives regardless of its likelihood
- C) Risk management should create value, and low-probability events do not create value concerns
- D) Risk management should be dynamic, iterative, and responsive to change

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: ISO 31000 defines risk as the "effect of uncertainty on objectives," not as a function of probability alone. A 15% chance of a material regulatory penalty — with its associated financial, reputational, and operational consequences — may represent a significant effect on objectives depending on the penalty's magnitude. Risk significance is determined by the combined consideration of likelihood and consequence relative to organizational objectives, not by likelihood alone.
- Why A is incorrect: Stakeholder inclusivity is an ISO 31000 principle, but it does not directly address the question of how to evaluate the significance of a low-probability event. The argument being made is about how to define and measure risk magnitude, not about who participates in the process.
- Why C is incorrect: This statement misrepresents the ISO 31000 value principle. ISO 31000 states that risk management should create and protect value — it does not suggest that low-probability events are exempt from risk management consideration.
- Why D is incorrect: The dynamic and iterative principle addresses how risk management should respond to changing conditions over time. While relevant to ongoing risk monitoring, it does not resolve the dispute about whether a 15% probability event is significant.

---

### Question 17

A cybersecurity analyst at a defense contractor is using the NIST RMF. The system being assessed processes Controlled Unclassified Information (CUI). During the Categorize step, the team must determine the system's impact level. Which NIST publication provides the authoritative impact level determination methodology used in Step 2 of the RMF?

- A) NIST SP 800-53, which provides the security control catalog organized by impact level
- B) NIST SP 800-137, which defines continuous monitoring strategies for federal information systems
- C) FIPS 199, which establishes security categories based on the potential impact to confidentiality, integrity, and availability across three levels: Low, Moderate, and High
- D) NIST SP 800-30, which provides guidance for conducting risk assessments

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: FIPS Publication 199, "Standards for Security Categorization of Federal Information and Information Systems," is the authoritative standard for the Categorize step. It defines impact levels (Low, Moderate, High) for confidentiality, integrity, and availability, and the overall system category is determined by the "high-water mark" — the highest impact level across all three security objectives.
- Why A is incorrect: NIST SP 800-53 is the security control catalog used in the Select step (Step 3). It references impact levels determined by FIPS 199 to guide control baseline selection, but it does not define the impact level determination methodology used in the Categorize step.
- Why B is incorrect: NIST SP 800-137 addresses Information Security Continuous Monitoring (ISCM) — it supports the Monitor step of the RMF, not the Categorize step. It has no role in impact level determination.
- Why D is incorrect: NIST SP 800-30 provides risk assessment guidance used in the Assess step and as a companion to the broader RMF process. It does not define the security categorization methodology used in the Categorize step; that function belongs to FIPS 199.

---

### Question 18

A financial services company is adopting FAIR to improve its communication of cybersecurity risk to the board. The initial FAIR analysis of a third-party data breach scenario produces a range of $1.2M to $8.4M in expected annual loss. The board treasurer asks why FAIR produces a range rather than a single number. Which explanation is most accurate?

- A) FAIR has not been calibrated for financial services organizations, so the wide range reflects framework immaturity
- B) FAIR uses Monte Carlo simulation to model the probability distributions of its input variables, producing a range of probable outcomes that reflects the genuine uncertainty in the underlying estimates rather than false precision
- C) The range indicates that the FAIR analysis was performed incorrectly and needs to be rerun with more precise input data
- D) FAIR ranges are generated by averaging the results of multiple separate risk assessment teams

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: FAIR's quantitative approach intentionally uses probability distributions rather than point estimates for key input variables (threat event frequency, vulnerability, primary loss magnitude, secondary loss). These distributions are then processed through Monte Carlo simulation to produce a range of probable loss outcomes — typically expressed as a 10th to 90th percentile range. This range is a feature, not a defect; it accurately represents the inherent uncertainty in risk estimation rather than implying false precision through a single number.
- Why A is incorrect: FAIR is specifically well-suited to financial services organizations and is widely adopted by banks and insurers. The range does not reflect framework immaturity — it reflects the correct application of probabilistic modeling.
- Why C is incorrect: A wide range does not indicate incorrect analysis. FAIR analyses produce wide ranges when the underlying input variables have high uncertainty, which is common in cybersecurity risk scenarios. A narrow range with limited data would actually be more suspect, not less.
- Why D is incorrect: Monte Carlo simulation is a mathematical modeling technique, not an averaging process across multiple teams. FAIR does not require parallel teams to generate its output range.

---

### Question 19

An organization is selecting a risk management framework for its information security program. The security director lists the following requirements: the framework must be internationally recognized, applicable across all risk types (not only cybersecurity), non-prescriptive (providing principles and guidelines rather than mandatory steps), and suitable for integration with the organization's existing ISO 9001 quality management system. Which framework best satisfies all four requirements?

- A) NIST SP 800-37 RMF
- B) OCTAVE Allegro
- C) ISO 31000:2018
- D) FAIR

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: ISO 31000:2018 is an international standard (ISO), applicable to all risk types across all sectors, explicitly non-prescriptive (it provides principles, a framework, and a process — not a mandatory step sequence), and designed to integrate with other ISO management system standards including ISO 9001. It satisfies all four stated requirements simultaneously.
- Why A is incorrect: NIST SP 800-37 RMF is a prescriptive, step-based framework designed for U.S. federal information systems. It is specific to information systems risk, not enterprise-wide risk management, and is not designed for integration with ISO management systems.
- Why B is incorrect: OCTAVE Allegro is a self-directed information asset risk assessment methodology, not an enterprise risk framework. It addresses only information security risk, not all risk types, and is not internationally standardized in the same way as ISO 31000.
- Why D is incorrect: FAIR is a quantitative risk analysis model for information and operational risk in financial terms. It is not a risk management framework providing governance principles and process guidance, and it does not address non-information risk types or ISO management system integration.

---

### Question 20

A healthcare network has completed its first enterprise risk assessment using OCTAVE Allegro. The risk team has developed 23 threat scenarios across 8 critical information assets and scored each using the OCTAVE Allegro risk scoring criteria. The CISO now needs to determine which risks to address first. Which OCTAVE Allegro output directly supports this prioritization decision?

- A) The asset-based threat profiles created in Phase 1, which describe the assets' security requirements
- B) The risk scores calculated for each threat scenario, ranked against the organization's risk measurement criteria to identify which scenarios require immediate treatment
- C) The list of threat actors and their capabilities identified during the threat community analysis
- D) The containers (technical and non-technical environments) where each asset resides

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: OCTAVE Allegro produces a risk score for each threat scenario based on the organization's risk measurement criteria — a set of weighted impact areas (financial, reputation, productivity, safety, legal/regulatory, etc.) that the organization defines at the start of the assessment. Scenarios are ranked by total score, providing the prioritization order for risk treatment decisions. The ranked risk scores are the direct output that answers the question "which risks should we address first?"
- Why A is incorrect: Asset-based threat profiles (Phase 1 output) describe what assets exist, why they matter, and their security requirements. They are inputs to the threat scenario development phase, not the prioritization output. They tell the team what to protect, not which scenarios are most urgent.
- Why C is incorrect: Threat actor and community analysis is an intermediate analytical step that informs threat scenario development. It identifies who could threaten the assets, but it does not produce prioritized risk scores — the output needed for treatment prioritization.
- Why D is incorrect: Container analysis identifies the environments where assets reside (databases, servers, portable media, people, etc.) and is used to develop threat scenarios grounded in realistic attack paths. Like threat actor analysis, it is an input to scenario development, not a prioritization output.
