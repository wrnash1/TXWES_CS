# Quiz: Module 14 — Risk and Compliance in IT Service Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

An organization decides to purchase cyber insurance to cover the financial costs of a potential data breach rather than investing in additional technical controls. Which risk response strategy does this represent?

A. Risk avoidance

B. Risk mitigation

C. Risk transfer

D. Risk acceptance

**Correct Answer: C**

**Distractor Analysis:**

- **A (Avoidance)** is wrong. Avoidance means eliminating the activity that creates the risk. Purchasing insurance does not eliminate the risk — it shifts the financial burden.
- **B (Mitigation)** is wrong. Mitigation reduces likelihood or impact through active controls. Insurance does not make a breach less likely or less damaging technically.
- **C (Transfer)** is correct. Purchasing insurance transfers the financial consequence of the risk to the insurer. The risk itself still exists — the organization just shares the financial impact with a third party.
- **D (Acceptance)** is wrong. Acceptance means acknowledging the risk and deciding to absorb it without additional action. Purchasing insurance is a deliberate action to manage the financial exposure — not passive acceptance.

---

**Question 2**

Which formula is used to calculate a risk's priority score in a standard risk register?

A. Likelihood + Impact

B. Likelihood × Impact

C. Impact ÷ Likelihood

D. (Likelihood + Impact) ÷ 2

**Correct Answer: B**

**Distractor Analysis:**

- **A (Addition)** produces a score but does not appropriately weight the combined effect. A risk with Likelihood 1 and Impact 5 would score the same as Likelihood 3 and Impact 3 — very different risk profiles.
- **B (Multiplication)** is correct. Risk score = Likelihood × Impact. This is the standard formula used in risk matrices and risk registers. It produces differentiated scores that reflect the compounding nature of high-probability, high-impact events.
- **C (Division)** produces a nonsensical result — a high-likelihood, low-impact risk would score lower than a low-likelihood, high-impact risk in a way that reverses the intended prioritization.
- **D (Average)** partially addresses the weakness of addition but is not the standard methodology for risk scoring.

---

**Question 3**

Which statement best describes the difference between a SOC 2 Type I and SOC 2 Type II report?

A. Type I covers all five Trust Services Criteria; Type II covers only the Security criterion.

B. Type I is an assessment of whether controls are suitably designed at a point in time; Type II is an assessment of whether controls operated effectively over a defined period.

C. Type I is conducted by an external auditor; Type II is conducted by internal audit staff.

D. Type I reports are shared publicly; Type II reports are confidential.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Both Type I and Type II can cover any combination of the five Trust Services Criteria — the number of criteria is determined by scope, not report type.
- **B** is correct. Type I evaluates control design at a specific date — the auditor asks "are these controls appropriate?" Type II evaluates operational effectiveness over a period (typically 6–12 months) — the auditor asks "did these controls actually work, consistently, over time?" Type II is more valuable because it demonstrates sustained compliance.
- **C** is wrong. Both Type I and Type II are conducted by independent third-party auditors (CPAs or licensed firms). Neither is an internal audit product.
- **D** is wrong. Both SOC 2 report types are typically shared under a non-disclosure agreement with customers — neither is public. (SOC 3 reports are public summaries.)

---

**Question 4**

An IT organization discovers that a key network engineer is the only employee with deep knowledge of the organization's routing configuration. If this employee left, the organization could not maintain the network. How should this risk be classified in the risk register?

A. Technology risk — the network configuration is too complex.

B. Operational risk — the process for network management lacks documentation.

C. People risk — key person dependency on a critical technical role.

D. Vendor risk — the network vendor should be held responsible for configuration support.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is wrong. The complexity of the configuration is a characteristic, not the root risk. The risk is about the loss of human knowledge and capability.
- **B** is partially valid — lack of documentation is a contributing factor — but the primary risk classification for this scenario is key person dependency, which is explicitly a people risk category.
- **C** is correct. Key person risk (also called key man risk) is a classic people risk. It represents dependence on specific individuals whose departure would significantly impact operations.
- **D** is wrong. The network vendor's role in ongoing configuration support is a separate concern. The identified risk is about internal knowledge concentration, not vendor capability.

---

**Question 5**

ISO 27001:2022 organizes its Annex A controls into four themes. Which option correctly lists all four?

A. Technical, Administrative, Physical, Legal

B. Organizational, People, Physical, Technological

C. Preventive, Detective, Corrective, Compensating

D. Confidentiality, Integrity, Availability, Privacy

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. "Administrative" and "Legal" are not ISO 27001 themes. "Administrative" is used in HIPAA security rule terminology.
- **B** is correct. ISO 27001:2022 Annex A organizes 93 controls into: Organizational (37), People (8), Physical (14), and Technological (34).
- **C** is wrong. Preventive, Detective, Corrective, and Compensating are control types used in general security frameworks (NIST, COBIT) — they describe function, not ISO 27001 categories.
- **D** is wrong. Confidentiality, Integrity, and Availability are the CIA triad of information security objectives. Privacy is the fifth SOC 2 Trust Services Criterion. None of these are the ISO 27001 Annex A themes.

---

**Question 6**

An organization accepts a risk without implementing additional controls. Which condition is required for this to be a valid, ITIL-aligned risk management decision?

A. The risk must be below the organization's minimum impact threshold (rated 1 on a 5-point scale).

B. The risk must be documented, an appropriate authority must formally approve the acceptance, and a review date must be set.

C. Risk acceptance is only valid for technology risks — not people or regulatory risks.

D. The risk owner must personally guarantee that the risk will not materialize.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Risk acceptance is not limited to low-impact risks. Organizations may accept medium or even high risks when mitigation costs are prohibitive or the activity cannot be avoided. The key is that the acceptance is deliberate and documented.
- **B** is correct. Valid risk acceptance requires: the risk is formally documented in the register, an appropriate authority (risk committee, senior management) explicitly approves the acceptance, and a review date is assigned so the accepted risk does not become permanently forgotten.
- **C** is wrong. Risk acceptance can apply to any risk category — technology, people, regulatory, financial.
- **D** is wrong. No individual can guarantee that a risk will not materialize — that is definitionally impossible and would eliminate the concept of acceptance risk management.

---

**Question 7**

Which ITIL 4 practice is most directly aligned with ISO 27001's requirements for managing confidentiality, integrity, and availability of information?

A. Supplier Management

B. Service Level Management

C. Information Security Management

D. Risk Management

**Correct Answer: C**

**Distractor Analysis:**

- **A (Supplier Management)** addresses third-party relationships — relevant to ISO 27001's supplier security controls but not the primary alignment.
- **B (Service Level Management)** addresses availability commitments in SLAs, which overlaps with availability, but does not address confidentiality or integrity.
- **C (Information Security Management)** is correct. ITIL 4's Information Security Management practice directly corresponds to ISO 27001's ISMS. Both focus on protecting information confidentiality, integrity, and availability through systematic risk management and controls.
- **D (Risk Management)** is a related practice but broader in scope — it addresses all organizational risks, not specifically information security. Information Security Management applies risk management principles specifically to information assets.

---

**Question 8**

A healthcare IT vendor notifies customers that they have detected unauthorized access to a database containing 3,200 patient records. The vendor discovered the breach today. How many hours does the covered entity (the healthcare provider using the vendor) typically have to notify HHS under HIPAA breach notification rules?

A. 24 hours from discovery

B. 48 hours from discovery

C. Up to 60 days from discovery

D. 72 hours from discovery

**Correct Answer: C**

**Distractor Analysis:**

- **A (24 hours)** is wrong. HIPAA does not impose a 24-hour notification requirement. This is more consistent with some state laws and GDPR.
- **B (48 hours)** is wrong. No standard 48-hour HIPAA requirement exists.
- **C (Up to 60 days)** is correct. HIPAA's Breach Notification Rule requires covered entities to notify HHS and affected individuals within 60 days of discovering a breach. For breaches affecting more than 500 individuals in a state, prominent media notice is also required.
- **D (72 hours)** is wrong. 72 hours is the GDPR breach notification deadline (to the supervisory authority) — not HIPAA's requirement. Confusing these two is a common error in international compliance discussions.

---

**Question 9**

What is "compliance theater" as described in ITIL and risk management contexts?

A. A training simulation where employees practice responding to audit requests.

B. A formal compliance performance review presented to the board of directors.

C. A situation where policies and documentation exist on paper but do not reflect actual operational practices.

D. The scheduled quarterly review of the risk register by the risk management committee.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is wrong. Training simulations are legitimate compliance activities — the opposite of compliance theater.
- **B** is wrong. Board presentations are normal governance activities, not compliance theater.
- **C** is correct. Compliance theater describes the appearance of compliance without the substance — elaborate policy documents, audit-ready binders, and polished presentations that do not reflect how work is actually done. It is one of the most dangerous compliance failure patterns because it creates false confidence.
- **D** is wrong. Regular risk register reviews are exactly what good risk governance looks like — they are the substance of compliance, not theater.

---

**Question 10**

A company's risk register shows a risk with Likelihood = 4 and Impact = 5, resulting in a risk score of 20. After implementing two new security controls, the revised assessment shows Likelihood = 2 and Impact = 4. What is this post-control risk level called?

A. Inherent risk

B. Accepted risk

C. Transferred risk

D. Residual risk

**Correct Answer: D**

**Distractor Analysis:**

- **A (Inherent risk)** is wrong — or rather, it is the opposite. Inherent risk is the risk level before any controls are applied. The 4 × 5 = 20 score would be closer to inherent risk.
- **B (Accepted risk)** is wrong. Accepted risk is a risk where the organization has explicitly decided to take no further action. The scenario describes active control implementation, not acceptance.
- **C (Transferred risk)** is wrong. Transfer involves insurance or contractual mechanisms. Controls implemented internally represent mitigation, not transfer.
- **D (Residual risk)** is correct. Residual risk is the risk exposure remaining after controls have been applied. The 2 × 4 = 8 score reflects the risk level that remains after mitigation — what the organization must continue to manage or accept.

---

*End of Module 14 Quiz — 10 questions with distractor analysis*
