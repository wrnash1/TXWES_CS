# Quiz: Module 06 — Information Security Program Development

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points (100 points total). Questions reflect CISM Domain 3 exam-style scenarios.

---

## Question 1

A newly appointed CISO at a regional bank discovers there is no formal document granting the security team authority to enforce policies or conduct audits. Which document should the CISO develop first to address this gap?

- A) An Acceptable Use Policy signed by all employees
- B) A security program charter approved by executive leadership
- C) A detailed incident response procedure
- D) A risk register documenting all identified threats

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. An Acceptable Use Policy is a Tier 1 policy document. Policies derive their enforceability from an authority grant, which the charter provides. Creating a policy first without the charter leaves it without organizational backing.
- B — Correct. The charter is the foundational governance document that grants the security program authority to enforce policies, conduct audits, and take corrective action. It must exist before any enforcement activity is meaningful.
- C — Incorrect. An incident response procedure is a Tier 3 operational document. It addresses how to respond to events, not who has the authority to govern security across the organization.
- D — Incorrect. A risk register is a valuable management tool, but it documents risks — it does not establish organizational authority for the security function.

---

## Question 2

Which of the following statements most accurately describes the relationship between a security policy and a security standard?

- A) A standard is a higher-authority document than a policy and must be approved by the board
- B) A policy states what must be done; a standard specifies how it must be done technically
- C) Policies and standards are interchangeable terms for mandatory security requirements
- D) A standard is advisory only; a policy is the sole mandatory document in the hierarchy

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Policies sit above standards in the hierarchy. Policies are approved at the executive or board level; standards are typically approved by security architecture or IT leadership.
- B — Correct. This is the defining distinction. Policies are technology-neutral statements of what is required. Standards provide the specific, mandatory technical or operational specifications that implement the policy intent.
- C — Incorrect. They serve different purposes and operate at different levels of the hierarchy. Conflating them leads to policies that become outdated whenever technology changes.
- D — Incorrect. Standards are mandatory, not advisory. Guidelines are the non-mandatory tier in the four-tier hierarchy.

---

## Question 3

A security manager reviews an organization's "Encryption Requirements" document. It states: "All laptops must use BitLocker with AES-256 encryption. The recovery key must be stored in Azure Active Directory." Based on the four-tier policy hierarchy, this document is best classified as a:

- A) Policy, because it addresses a critical security requirement
- B) Guideline, because it provides technical recommendations
- C) Standard, because it specifies mandatory technical methods and configurations
- D) Procedure, because it references specific products by name

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. A policy would state "all data at rest must be encrypted" without naming BitLocker or AES-256. The specificity of this document places it in the standards tier, not the policy tier.
- B — Incorrect. Guidelines are non-mandatory advisory documents. This document uses prescriptive language ("must use," "must be stored") indicating mandatory requirements.
- C — Correct. Standards are mandatory technical specifications that implement policy requirements. Naming a specific technology (BitLocker), algorithm (AES-256), and key storage method (Azure AD) is characteristic of a standard.
- D — Incorrect. A procedure would provide numbered step-by-step instructions for enabling BitLocker on a specific device. Referencing product names alone does not make a document a procedure.

---

## Question 4

An information security manager is preparing a three-year security strategy for presentation to the board. Which of the following best represents the correct approach to strategy development?

- A) Base the strategy on the most severe threats identified in recent vulnerability scans
- B) Mirror the strategy of a peer organization in the same industry that has experienced no breaches
- C) Derive security objectives from the organization's business strategy and critical asset priorities
- D) Focus the strategy exclusively on achieving the lowest possible risk ratings across all categories

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. Vulnerability scans identify technical weaknesses but do not reflect business priorities. A strategy built solely on technical threat data may over-invest in areas of low business impact and neglect critical business risks.
- B — Incorrect. Peer organizations have different risk appetites, assets, and threat profiles. Absence of known breaches does not mean their strategy is appropriate for your organization.
- C — Correct. CISM principle: security strategy must be derived from and support business strategy. Critical asset identification ensures security investment is proportional to business value at risk.
- D — Incorrect. The goal of risk management is not to eliminate all risk but to manage risk within the organization's appetite. Pursuing the lowest possible ratings regardless of cost is neither feasible nor aligned with business objectives.

---

## Question 5

A security manager calculates that a successful phishing attack against the payroll system has an SLE of $500,000 and an ARO of 0.4. What is the current ALE, and how should this figure be used?

- A) ALE = $200,000; this figure should be used to compare against the cost of anti-phishing controls
- B) ALE = $1,250,000; this represents the maximum the organization should ever spend on phishing controls
- C) ALE = $200,000; this figure represents the amount that must be spent on controls immediately
- D) ALE = $500,000; the ARO is irrelevant when the SLE exceeds tolerance thresholds

**Correct Answer:** A

**Distractor Analysis:**

- A — Correct. ALE = SLE × ARO = $500,000 × 0.4 = $200,000. ALE represents expected annual loss and is used to evaluate whether control costs are financially justified. A control costing less than $200,000 per year that eliminates the risk provides a positive return.
- B — Incorrect. The calculation $500,000 / 0.4 = $1,250,000 is not the ALE formula. ALE = SLE × ARO, not SLE / ARO. Misapplying the formula is a common exam error.
- C — Incorrect. ALE informs investment decisions but does not mandate spending an equivalent amount. It provides a ceiling for justified control investment, not a required expenditure.
- D — Incorrect. ARO is central to the ALE calculation. Ignoring it removes the time dimension from risk quantification and produces an inflated, misleading figure.

---

## Question 6

The CISO of a manufacturing company wants to demonstrate that the information security program directly supports business objectives. Which of the following actions best demonstrates this alignment?

- A) Publishing the organization's vulnerability count reduction metrics in the annual report
- B) Mapping each security initiative in the roadmap to a specific business objective or regulatory requirement
- C) Achieving the highest possible maturity score across all NIST CSF categories simultaneously
- D) Ensuring that security team certifications are listed prominently in board presentations

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Vulnerability counts are a technical metric. Publishing them does not inherently demonstrate alignment to business outcomes; they may mean nothing to a board member without business context.
- B — Correct. Explicit mapping of security initiatives to business objectives is the definitive way to demonstrate alignment. It shows that every security investment has a business rationale, not just a technical one.
- C — Incorrect. Achieving the highest maturity score in all categories simultaneously is neither realistic nor necessarily aligned to business priorities. Some domains may warrant lower maturity if business risk does not justify investment.
- D — Incorrect. Team certifications demonstrate professional competence but do not demonstrate program alignment to business strategy.

---

## Question 7

Which document in the four-tier policy hierarchy is most appropriate for providing developers with recommended secure coding practices that are not subject to disciplinary enforcement?

- A) Policy
- B) Standard
- C) Procedure
- D) Guideline

**Correct Answer:** D

**Distractor Analysis:**

- A — Incorrect. Policies are mandatory. Placing recommended developer practices in a policy would make violations subject to disciplinary action, which is inappropriate for advisory content.
- B — Incorrect. Standards are mandatory technical specifications. Recommended practices that are not enforced do not belong in this tier.
- C — Incorrect. Procedures are step-by-step mandatory operational instructions. Non-mandatory recommendations do not belong in the procedures tier.
- D — Correct. Guidelines are the only non-mandatory tier in the hierarchy. They are ideal for recommended practices, developer tips, and best-practice documentation where the intent is to encourage rather than enforce.

---

## Question 8

A security program charter specifies that the CISO reports to the Chief Technology Officer (CTO). A board member raises concerns about the independence of the security function. What is the primary governance concern with this reporting structure?

- A) The CTO may not understand technical security requirements well enough to provide oversight
- B) Reporting to the CTO creates a potential conflict of interest when security requirements slow technology delivery
- C) The charter is invalid unless the CISO reports directly to the board of directors
- D) This structure violates GLBA and PCI DSS reporting requirements

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. CTOs typically have strong technical backgrounds. The concern is not competence but independence and competing priorities.
- B — Correct. When the CISO reports to the CTO, security decisions may be subordinated to technology delivery schedules. The CTO has incentive to deprioritize security when it creates friction for IT projects. This conflict of interest is the governance concern the board member is raising.
- C — Incorrect. There is no universal requirement for the CISO to report directly to the board. Reporting to the CEO, General Counsel, or CFO are also independence-preserving options. The charter is not invalid — the reporting structure is simply suboptimal.
- D — Incorrect. Neither GLBA nor PCI DSS prescribes a specific CISO reporting structure. This answer invents a compliance requirement that does not exist.

---

## Question 9

An information security manager is drafting the organization's first formal Acceptable Use Policy. Which of the following elements is MOST important to include to ensure the policy is enforceable?

- A) A detailed list of all approved software applications and their version numbers
- B) A statement of scope defining who is covered, a prohibition section, and a consequences-of-violation statement
- C) Step-by-step instructions for reporting a policy violation through the ticketing system
- D) A glossary of technical terms used by the security operations team

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. A specific software list belongs in a standard, not a policy. Including version numbers in a policy would require frequent policy revisions and makes the document fragile.
- B — Correct. An enforceable policy must define who it applies to (scope), what is prohibited, and what happens when violations occur (consequences). Without these three elements, enforcement is legally and operationally questionable.
- C — Incorrect. Violation reporting procedures belong in a procedure document, not the policy itself. The policy states what is required; procedures describe how to operationalize requirements.
- D — Incorrect. Technical glossaries support understanding but do not contribute to enforceability. Policy language should be accessible to all employees without requiring technical definitions.

---

## Question 10

A security manager presents a business case to the CFO for a new endpoint detection and response (EDR) solution. The CFO asks for financial justification. The manager states: "The current ALE for endpoint compromise is $320,000 per year. The EDR solution costs $90,000 annually and is expected to reduce the ARO by 70 percent." What is the net annual benefit of the investment?

- A) The investment is not justified because the control cost exceeds the ALE reduction
- B) Net annual benefit is $224,000 — the investment reduces ALE by $224,000 against a $90,000 cost
- C) Net annual benefit is $134,000 — calculated as ALE reduction minus annual control cost
- D) Net annual benefit cannot be calculated without knowing the SLE and asset value separately

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. This conclusion is wrong. ALE reduction = $320,000 × 0.70 = $224,000. The control cost is $90,000. The net benefit is $224,000 − $90,000 = $134,000, which is positive.
- B — Incorrect. The $224,000 is the gross ALE reduction, not the net benefit. Net benefit requires subtracting the annual control cost ($90,000), yielding $134,000.
- C — Correct. ALE reduction = $320,000 × 0.70 = $224,000. Net benefit = $224,000 − $90,000 = $134,000. The investment generates $134,000 in annual risk reduction value above its cost — clearly justified.
- D — Incorrect. The net benefit calculation requires only the current ALE, the risk reduction percentage, and the control cost — all of which are provided. Separate SLE and asset value figures are not needed for this calculation.

---

## Question 11

An organization's information security policy states: "All employees must protect confidential information from unauthorized disclosure." Which characteristic of an effective policy does this statement most clearly lack?

- A) Executive sponsorship
- B) Measurability and specificity
- C) Legal language
- D) Alignment with business objectives

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Executive sponsorship is demonstrated through the approving signature on the policy document, not the text of individual policy statements. The statement may well be in a policy with appropriate sponsorship.
- B — Correct. An effective policy statement must be specific enough to be measurable and auditable. "Protect confidential information" provides no actionable guidance — it does not define what constitutes confidential information, what protection measures are required, or how compliance can be verified. Auditors cannot test compliance against a statement this vague.
- C — Incorrect. Policies do not need to read like legal contracts; overly legalistic language can actually undermine comprehension and adoption. The problem with this statement is not its tone but its lack of specificity.
- D — Incorrect. The statement is general enough that it could plausibly align with any business objective. The deficiency is not about alignment but about the absence of concrete, verifiable requirements.

---

## Question 12

Which of the following best describes the relationship between an information security strategy and an information security program?

- A) The strategy and program are synonymous — both refer to the complete set of security activities an organization conducts
- B) The strategy defines the multi-year direction and objectives; the program is the operational structure that executes the strategy
- C) The program is developed first and the strategy is derived from it once the program's capabilities are known
- D) The strategy is produced by the security team; the program is produced by executive leadership

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Strategy and program are distinct concepts. The strategy is a directional document defining long-term goals aligned with business objectives. The program is the organizational and operational structure (people, processes, technologies, budgets) that implements those goals.
- B — Correct. CISM guidance distinguishes clearly between strategy (the what and why — multi-year goals, priorities, and direction) and program (the how — the implemented structure of policies, controls, resources, and processes that achieves the strategic goals). Strategy precedes program design; the program operationalizes the strategy.
- C — Incorrect. This reverses the correct sequence. Strategy must be established first to provide direction for the program. Building a program without a strategy results in ad hoc activity without coherent objectives.
- D — Incorrect. Both the strategy and the program involve collaboration between the security team and executive leadership. The CISO typically develops the strategy proposal, which is approved by executive leadership or the board. The program is then built and managed by the security team.

---

## Question 13

A security program charter is presented to the board of directors for approval. A board member objects that the charter grants the CISO authority to "suspend access to any system found to pose an immediate risk to the organization." The board member argues this authority is too broad. How should the CISO respond?

- A) Remove the clause — the CISO should not have authority to act without board approval in all cases
- B) Explain that this authority is necessary for the security program to respond to active threats and is a standard element of security charters
- C) Replace the charter with a policy that defines the specific conditions under which access may be suspended
- D) Accept the objection and limit suspension authority to systems classified below High impact

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. Security program charters must grant emergency response authority so the security team can act in real time during incidents without waiting for board approval. Requiring board approval before suspending access to a compromised system would make effective incident response impossible. The CISO should explain that this authority is standard, typically includes oversight mechanisms (e.g., notification requirements, post-action review), and is aligned with industry practice and governance frameworks.
- A — Incorrect. Requiring board approval for every access suspension would paralyze incident response. Governance frameworks distinguish between strategic decisions (requiring board input) and operational emergency actions (delegated to the CISO with accountability mechanisms). Removing this authority would create a significant operational gap.
- C — Incorrect. Replacing the charter with a policy does not solve the governance problem — the CISO needs a charter that grants authority. A policy can supplement the charter by defining procedures, but the charter-level authority grant is what provides the foundation for enforcement.
- D — Incorrect. Limiting suspension authority to lower-impact systems would be counterproductive — the most critical need for emergency access suspension arises in High-impact systems during active incidents. Impact classification should not limit the authority to respond to active threats.

---

## Question 14

An organization's information security strategy document lists the following objective: "Achieve and maintain compliance with all applicable regulatory requirements." Which criticism of this objective is most valid from a strategy development perspective?

- A) The objective is too technical and should be rephrased in business language
- B) The objective is reactive rather than forward-looking
- C) The objective is unmeasurable and provides no actionable direction for resource allocation
- D) The objective conflicts with the organization's risk appetite

**Correct Answer:** C

**Distractor Analysis:**

- C — Correct. Effective strategic objectives must be measurable and specific enough to drive resource allocation and prioritization decisions. "Achieve and maintain compliance with all applicable regulatory requirements" provides no way to measure progress, no specificity about which regulations, no timeline, and no indication of the current gap. It cannot be broken down into actionable program initiatives or used to justify specific budget requests.
- A — Incorrect. The statement is already in non-technical business language. The problem is not the language register but the lack of measurability and specificity.
- B — Incorrect. Compliance maintenance is a legitimate strategic objective even if it has a reactive component. The primary failure of this objective is not that it is reactive but that it is unmeasurable. Many sound security objectives include compliance components.
- D — Incorrect. Regulatory compliance is typically non-discretionary and does not conflict with risk appetite — organizations must comply regardless of their appetite for risk. There is no information in the scenario to suggest a conflict with risk appetite.

---

## Question 15

A CISO is developing a three-year security program roadmap. Year 1 focuses on foundational controls (MFA, patch management, endpoint protection). Year 2 adds detection and response capabilities (SIEM, SOC). Year 3 targets advanced capabilities (zero trust architecture, threat intelligence integration). This approach is best described as:

- A) A risk-based program development strategy, because controls are selected based on ALE calculations
- B) A maturity-based program development strategy, building foundational capabilities before advanced ones
- C) A compliance-driven program development strategy, implementing controls in regulatory priority order
- D) A technology-first program development strategy, because the roadmap is organized around tools

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. The roadmap describes a maturity-based progression — building essential foundational capabilities first (identity and endpoint protection), then detection and response, then advanced architectural capabilities. This approach mirrors the CMMI and security maturity frameworks that sequence capability development from basic to optimized. It ensures that advanced capabilities are built on a stable foundation rather than deployed into an immature environment.
- A — Incorrect. A risk-based program development strategy would select and prioritize initiatives based on calculated risk reduction per dollar invested, not a sequential maturity progression. The roadmap does not mention ALE calculations or risk-based prioritization criteria.
- C — Incorrect. A compliance-driven strategy would organize the roadmap around the specific control requirements of applicable regulations (e.g., PCI DSS controls first, then HIPAA controls). The roadmap as described is organized around capability maturity stages, not regulatory requirements.
- D — Incorrect. While the roadmap mentions tools (SIEM, MFA), the organizing principle is capability maturity progression — from foundational to advanced — not technology acquisition. A technology-first strategy would prioritize tools based on vendor capability or cost, not on building sequenced operational capabilities.

---

## Question 16

A newly hired security manager inherits a program with no documented performance metrics. Senior management asks whether the program is "working." Which of the following represents the most appropriate first step toward answering that question?

- A) Commission a third-party penetration test to identify remaining vulnerabilities
- B) Define measurable security objectives tied to business risk, then select metrics that indicate progress toward each objective
- C) Benchmark the organization's security spending against industry peers to determine whether the budget is sufficient
- D) Survey employees to assess their satisfaction with the security team's responsiveness

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. A penetration test identifies exploitable vulnerabilities at a point in time but does not measure program performance against defined objectives. A test result cannot answer "is the program working" without established objectives to measure against.
- B — Correct. Before any metric can be interpreted, the program must have defined objectives against which performance is measured. The correct sequence is: define objectives → select metrics that indicate progress → collect and report. This is the foundational step described in CISM Domain 3 guidance for program management.
- C — Incorrect. Benchmarking security spending tells you whether the budget is above or below peers, but does not measure whether the program is achieving its risk reduction goals. A program can be underfunded but effective, or well-funded but ineffective. Spend comparisons are an input to planning, not a program performance measure.
- D — Incorrect. Employee satisfaction surveys measure perception of the security team, not security program effectiveness. A security team can be popular and still fail to reduce risk; conversely, a highly effective program may be unpopular because it enforces controls users find inconvenient.

---

## Question 17

An information security program charter has been approved by the board, but after six months, the security team is still unable to enforce patch management requirements on the IT operations team. The IT operations director claims the security team has no authority over his department. What is the most likely cause of this situation?

- A) The charter was approved at too low an organizational level to carry enforcement authority
- B) The charter lacks explicit language delegating authority to the security program over cross-functional enforcement activities
- C) The security team has not yet developed a formal policy to accompany the charter
- D) The IT operations director is correct — security programs do not have authority over other departments

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Board-level approval is the highest organizational level available. The problem is not the approval level but the specificity of the authority language within the charter. A board-approved charter with vague authority language still produces enforcement gaps.
- B — Correct. A program charter approved by the board grants the security program authority, but that authority must be specific enough to be actionable. If the charter does not explicitly address the security team's right to mandate compliance with standards across all departments — including IT operations — the operations director can plausibly dispute the authority scope. Charters must include explicit cross-functional enforcement language to prevent this ambiguity.
- C — Incorrect. A supporting policy is important for specifying requirements, but the immediate problem is an authority dispute — the operations director claims the security team has no authority, not that there is no documented requirement. The charter must establish authority before a policy can be enforced.
- D — Incorrect. Security programs appropriately established by organizational governance do have cross-functional authority for security requirements. The CISM framework is explicit that the security program must have the authority to establish and enforce standards enterprise-wide. The dispute reflects a charter deficiency, not a correct statement of organizational authority.

---

## Question 18

An organization uses the Capability Maturity Model Integration (CMMI) to assess its security program. The assessment finds that security processes are "performed informally and depend on individual heroics rather than documented procedures." Which maturity level does this finding describe?

- A) Level 0 — Incomplete
- B) Level 1 — Initial (Performed)
- C) Level 2 — Managed
- D) Level 3 — Defined

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Level 0 (Incomplete) describes processes that are not performed or are only partially performed with no consistent output. The scenario describes processes that are performed — just informally and inconsistently. The presence of informal activity places the finding at Level 1, not Level 0.
- B — Correct. CMMI Level 1 (Initial/Performed) is characterized by processes that succeed due to individual competence and effort rather than institutional structure. "Individual heroics" and the absence of documented procedures are the defining markers of Level 1. Outcomes are unpredictable and cannot be replicated when key individuals leave.
- C — Incorrect. Level 2 (Managed) requires that processes are planned, monitored, and controlled using project management practices. At Level 2, basic documentation exists and management can track status. The scenario explicitly states that documentation is absent.
- D — Incorrect. Level 3 (Defined) requires that processes are standardized across the organization and tailored from a defined set of organizational process assets. Level 3 processes are explicitly documented, consistent, and organization-wide. This is the opposite of the finding described.

---

## Question 19

A CISO is proposing a new threat intelligence program to the CFO. The CFO asks: "What is the business justification for this investment?" Which of the following responses most effectively makes the business case?

- A) "Threat intelligence is an industry best practice recommended by NIST and ISO 27001, and peer organizations have implemented similar programs."
- B) "This program will reduce the mean time to detect relevant threats targeting our sector from an estimated 17 days to under 72 hours, protecting $4.2M in assets currently exposed to those threats."
- C) "Our security team needs better information to do their jobs effectively, and threat intelligence provides that information."
- D) "Without threat intelligence, we cannot achieve Level 4 maturity on our security capability assessment."

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Citing industry best practices and peer adoption does not answer the CFO's question about this organization's specific business justification. "Others are doing it" is not a business case — it is an appeal to conformity that does not quantify value or connect to the organization's own risk profile.
- B — Correct. An effective business case connects the investment to a quantified business outcome — specifically, reduced risk exposure expressed in terms of assets protected and improved detection performance. The CFO's question is fundamentally about return on investment and risk reduction value. Framing the investment in terms of MTTD improvement and dollar exposure gives the CFO a decision-relevant value proposition.
- C — Incorrect. "Better information for the security team" describes an operational benefit to the security department, not a business outcome. The CFO is not asking whether the security team will benefit — they are asking what business risk or loss the investment prevents or reduces.
- D — Incorrect. Maturity level improvement is an internal security program metric, not a business outcome. The CFO's question requires an answer in terms of business risk, financial exposure, or operational impact — not a program assessment score.

---

## Question 20

An organization's security program has operated for three years under a charter that was never formally reviewed or updated. During that period, the organization acquired two companies, expanded to three new regulatory jurisdictions, and migrated 80% of its infrastructure to a cloud environment. What is the MOST significant risk created by the outdated charter?

- A) The charter may no longer reflect the organization's current risk environment, leaving authority gaps for new assets, jurisdictions, and operating models
- B) The security team's authority may have been legally invalidated by the passage of time
- C) Regulatory bodies may penalize the organization for having an unreviewed charter
- D) The charter's technology references may be outdated, requiring a full rewrite rather than an update

**Correct Answer:** A

**Distractor Analysis:**

- A — Correct. A charter written before acquisitions, geographic expansion, and cloud migration may not address authority over acquired systems, compliance obligations in new jurisdictions, or security responsibilities in a shared-responsibility cloud model. These gaps leave the security program without formal authority in areas that now represent significant risk. Charters must be reviewed and updated when material changes occur to the organization's operating environment.
- B — Incorrect. A charter's authority does not expire through the passage of time alone. Authority derived from executive or board approval remains in effect until formally revised or revoked. The risk is not legal invalidation but scope mismatch — the charter may not cover the new environment, not that it is legally void.
- C — Incorrect. Regulatory bodies do not typically audit internal governance documents like program charters. They audit compliance with regulatory requirements. The risk from an outdated charter is internal governance inadequacy, not a direct regulatory penalty for charter age.
- D — Incorrect. Technology references in a charter, if any, are a documentation quality concern but not the most significant risk. Charters should be written at a level of abstraction that does not require rewriting with every technology change. The critical risk is the authority and scope gaps created by organizational changes, not outdated tool references.
