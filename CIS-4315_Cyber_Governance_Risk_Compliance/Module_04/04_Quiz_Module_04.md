# Quiz: Module 04 — Risk Assessment and Analysis Techniques

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

**Instructions:** Choose the single best answer for each question.

---

### Question 1

An organization's database server is valued at $600,000. A malware attack would destroy approximately 50% of the data stored on it. The organization estimates malware attacks of this severity occur once every five years. What is the Annualized Loss Expectancy (ALE)?

- A) $300,000
- B) $60,000
- C) $3,000,000
- D) $120,000

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: SLE = $600,000 × 0.50 = $300,000. ARO = 1/5 = 0.20. ALE = $300,000 × 0.20 = $60,000. This is the correct application of the full formula chain.
- Why A is incorrect: $300,000 is the SLE — the single-event loss — not the annualized loss. It fails to account for how infrequently the event occurs (ARO = 0.20).
- Why C is incorrect: $3,000,000 results from multiplying the asset value by 5 rather than by ARO (0.20). This inverts the relationship between frequency and annualized loss.
- Why D is incorrect: $120,000 would result from applying an ARO of 0.40 (once every 2.5 years) rather than 0.20. The scenario specifies once every five years, which yields ARO = 0.20.

---

### Question 2

A security manager needs to assess risk across 80 business applications within a three-week window. The organization does not have complete financial valuations for all applications. Which risk analysis method is most appropriate for this initial assessment?

- A) Quantitative analysis using the ALE formula for all 80 applications
- B) Qualitative analysis using a likelihood-impact matrix with descriptive ratings
- C) FAIR analysis using Monte Carlo simulation for each application
- D) Penetration testing to determine the actual exploitability of each application

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Qualitative analysis using a risk matrix is explicitly designed for broad, rapid assessments when financial data is unavailable and time is constrained. It allows the team to prioritize the highest-risk applications for deeper quantitative analysis later.
- Why A is incorrect: Quantitative ALE analysis requires financial asset valuations that the scenario states are unavailable. It is also far too time-intensive for 80 applications in three weeks.
- Why C is incorrect: FAIR analysis with Monte Carlo simulation requires probability distribution estimates for each risk factor — an even more data-intensive and time-consuming approach than standard ALE calculation, making it completely impractical for this scope and timeline.
- Why D is incorrect: Penetration testing identifies technical exploitability but does not produce a risk assessment across business functions and processes. It also would not complete 80 applications in three weeks.

---

### Question 3

In the context of a Business Impact Analysis, what is the correct relationship between Maximum Tolerable Downtime (MTD) and Recovery Time Objective (RTO)?

- A) RTO and MTD are independent metrics and have no required relationship to each other
- B) MTD must always be less than RTO to ensure the system is recovered before deadlines
- C) RTO must always be set below MTD to provide a safety margin before irreversible harm occurs
- D) RTO and MTD are interchangeable terms that describe the same recovery requirement

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: If RTO equals or exceeds MTD, the organization will exhaust its tolerance for downtime before the recovery target is met — meaning the system may not be restored in time to prevent catastrophic consequences. RTO must be set below MTD to provide a buffer.
- Why A is incorrect: MTD and RTO have a direct and critical relationship. Setting RTO without reference to MTD is a fundamental business continuity planning error.
- Why B is incorrect: This reverses the correct relationship. MTD is the outer boundary — the deadline. RTO must be less than MTD, not the other way around.
- Why D is incorrect: MTD and RTO are distinct concepts. MTD is the maximum time before irreversible organizational harm occurs (a business limit). RTO is the target recovery time (an operational commitment). They measure different things at different levels of the continuity hierarchy.

---

### Question 4

Which STRIDE threat category is violated when an attacker sends emails appearing to come from a legitimate executive to trick employees into transferring funds?

- A) Tampering
- B) Repudiation
- C) Spoofing
- D) Elevation of Privilege

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Spoofing involves impersonating a legitimate entity — in this case, impersonating an executive's identity to deceive recipients. Business email compromise (BEC) attacks are a classic example of spoofing. The violated security property is Authentication.
- Why A is incorrect: Tampering involves unauthorized modification of data in transit or at rest. The attacker in this scenario is not modifying data — they are impersonating an identity.
- Why B is incorrect: Repudiation involves denying that an action was taken, typically due to insufficient logging. The described attack is about impersonation, not about denying accountability for one's own actions.
- Why D is incorrect: Elevation of Privilege involves gaining access or permissions beyond what is authorized. The described attack does not involve escalating system privileges — it is a social engineering impersonation attack.

---

### Question 5

An organization currently has an ALE of $480,000 for a specific network intrusion risk. A proposed intrusion detection and prevention system costs $75,000 annually to operate and would reduce the ALE to $180,000. Is this investment financially justified according to quantitative risk analysis principles?

- A) No, because $75,000 is more than 10% of the current ALE, making it disproportionate
- B) Yes, because the annual control cost of $75,000 is less than the ALE reduction of $300,000
- C) No, because quantitative analysis alone cannot justify security investments — qualitative confirmation is also required
- D) Yes, because any reduction in ALE, regardless of control cost, justifies the investment

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: The ALE reduction is $480,000 - $180,000 = $300,000 per year. The control costs $75,000 per year. Since $75,000 is less than $300,000, the investment produces a net benefit of $225,000 annually. This is the standard ALE-based control justification rule: invest if annual control cost is less than the reduction in ALE.
- Why A is incorrect: There is no "10% of ALE" threshold in quantitative risk analysis. The correct rule is simply: control cost versus ALE reduction. A cost of $75,000 against a reduction of $300,000 is a 4:1 return — clearly justified.
- Why C is incorrect: Quantitative analysis is specifically designed to justify security investments in financial terms without requiring qualitative confirmation. The purpose of ALE-based analysis is precisely to enable stand-alone financial justification.
- Why D is incorrect: Not every ALE reduction justifies investment. If the control cost exceeded the ALE reduction — for example, spending $400,000 to reduce ALE by $50,000 — the investment would be financially unjustified. The cost-benefit comparison is always required.

---

### Question 6

A Recovery Point Objective (RPO) of 2 hours for a financial transaction database means that the organization:

- A) Must restore the database within 2 hours following any disruption
- B) Can tolerate losing at most 2 hours of transaction data in a recovery scenario
- C) Must test its backup and recovery procedures every 2 hours
- D) Must notify regulators within 2 hours of any database outage

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: RPO defines the maximum acceptable data loss measured in time. An RPO of 2 hours means that in any recovery scenario, the organization cannot afford to lose more than 2 hours of transaction data. This drives the requirement to back up or replicate data at least every 2 hours.
- Why A is incorrect: That definition describes the Recovery Time Objective (RTO) — which governs how quickly the system must be restored, not how much data can be lost.
- Why C is incorrect: RPO drives backup frequency requirements but does not itself define a testing schedule. Testing frequency is governed by continuity plan governance requirements, not by the RPO metric directly.
- Why D is incorrect: Regulatory notification timeframes are defined by applicable laws and regulations (such as breach notification statutes), not by an organization's internally defined RPO.

---

### Question 7

During a threat modeling session using STRIDE, the team identifies that the web application logs user actions but does not store them with tamper-proof timestamps and cannot prove what specific actions a user performed. Which STRIDE category does this threat fall under?

- A) Spoofing
- B) Information Disclosure
- C) Repudiation
- D) Denial of Service

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Repudiation is the STRIDE category covering the ability of a user to deny having performed an action — typically due to insufficient or untrustworthy audit logging. Without tamper-proof audit trails, users can claim they did not perform actions the system cannot disprove. The violated security property is Non-repudiation.
- Why A is incorrect: Spoofing concerns identity impersonation, not the ability to deny actions after the fact. The scenario describes a logging deficiency, not an authentication weakness.
- Why B is incorrect: Information Disclosure concerns unauthorized exposure of data to parties who should not have access. The scenario describes a failure to capture accountable evidence of user actions, which is a non-repudiation problem.
- Why D is incorrect: Denial of Service concerns availability disruption. The scenario involves an audit trail weakness with no connection to availability.

---

### Question 8

What is the primary purpose of a Business Impact Analysis (BIA) in the context of risk management?

- A) To identify the root cause of past security incidents and prevent their recurrence
- B) To determine the operational and financial consequences of disrupting critical business functions and set recovery targets
- C) To assign monetary values to information assets for insurance premium calculations
- D) To evaluate the technical security controls protecting each information system

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: The BIA determines what would happen to the business if critical functions were unavailable, quantifies the impact over time, and produces MTD, RTO, and RPO targets that drive recovery architecture and business continuity planning.
- Why A is incorrect: Root cause analysis of past incidents is a post-incident review activity, not a BIA. The BIA is a forward-looking analysis of potential disruption impact, not a retrospective on historical events.
- Why C is incorrect: Asset valuation for insurance purposes is a financial risk management or asset management activity. While BIA may inform insurance decisions, it is not its primary purpose. The BIA focuses on operational impact, not insurance premium optimization.
- Why D is incorrect: Technical security control evaluation is a security assessment or audit activity — conducted in NIST RMF Step 5 (Assess) or as part of compliance reviews. The BIA focuses on business function criticality and recovery requirements, not on evaluating controls.

---

### Question 9

An organization conducts a qualitative risk assessment and identifies a risk as "Possible Likelihood / Major Impact." According to the standard risk matrix, what priority level would this risk receive?

- A) Low
- B) Medium
- C) High
- D) Critical

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Using the standard 5×5 risk matrix, the intersection of Possible (middle likelihood row) and Major (second-highest impact column) produces a High risk priority. This reflects that major impacts are significant enough to warrant elevated priority even when occurrence is only possible rather than likely.
- Why A is incorrect: Low priority is assigned to low-likelihood and low-to-moderate impact combinations. A Major impact rating — representing significant operational or financial harm — rules out a Low priority designation.
- Why B is incorrect: Medium priority reflects combinations where both likelihood and impact are moderate, or where low likelihood somewhat offsets high impact. Possible Likelihood combined with Major Impact crosses into High territory on the standard matrix.
- Why D is incorrect: Critical priority is reserved for risks where both likelihood and impact are at the highest levels — Almost Certain/Critical or Likely/Critical. Possible Likelihood with Major Impact does not reach the Critical threshold.

---

### Question 10

A CISO wants to quantify the financial risk of a data breach affecting the organization's customer database and present the expected annual loss range to the board. Which analytical approach is most appropriate for this goal?

- A) Qualitative risk matrix analysis using High/Medium/Low ratings on a heat map
- B) STRIDE threat modeling to enumerate the specific attack paths threatening the database
- C) Business Impact Analysis to determine the MTD and RTO for the customer database system
- D) Quantitative risk analysis using the ALE formula or FAIR model to produce a dollar-denominated risk estimate

**Correct Answer:** D

**Distractor Analysis:**

- Why D is correct: The CISO's stated goal is to quantify financial risk in dollar terms for board communication. This is precisely the purpose of quantitative analysis — whether using the ALE formula chain or the FAIR model. Both produce financial estimates that enable business-level risk conversations.
- Why A is incorrect: A qualitative heat map produces a High/Medium/Low rating, not a financial estimate. The scenario specifically requires a dollar-denominated expected annual loss range, which qualitative analysis cannot provide.
- Why B is incorrect: STRIDE threat modeling identifies what threats exist and how they could attack the system — it does not quantify the financial impact of those threats. Threat modeling outputs are inputs to risk assessment, not financial risk estimates.
- Why C is incorrect: A BIA determines how long the system can be unavailable and how much data loss is acceptable. It does not quantify the annual financial exposure from a specific threat scenario like a data breach. BIA addresses continuity planning, not financial risk estimation.

---

*End of Module 04 Quiz*
