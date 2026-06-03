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
