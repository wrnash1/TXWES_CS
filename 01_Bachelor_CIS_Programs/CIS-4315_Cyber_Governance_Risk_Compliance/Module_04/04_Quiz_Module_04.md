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

End of Module 04 Quiz

---

### Question 11

A hospital's patient data system has an asset value of $3,000,000. A ransomware attack is expected to destroy 40% of the asset value per occurrence. The hospital's threat intelligence team estimates ransomware incidents of this type occur approximately once every four years. What is the ALE for this risk?

- A) $300,000
- B) $1,200,000
- C) $3,000,000
- D) $480,000

**Correct Answer:** A

**Distractor Analysis:**

- Why A is correct: SLE = AV × EF = $3,000,000 × 0.40 = $1,200,000. ARO = 1 ÷ 4 = 0.25 (once every four years). ALE = SLE × ARO = $1,200,000 × 0.25 = $300,000.
- Why B is incorrect: $1,200,000 is the SLE — the expected loss per single occurrence — before applying the annualized rate of occurrence. Stopping at SLE without applying ARO omits the frequency factor.
- Why C is incorrect: $3,000,000 is the full asset value, which would only be the correct answer if EF were 100% and ARO were 1.0. Neither condition is true in this scenario.
- Why D is incorrect: $480,000 does not correspond to any step in the ALE formula chain. It may result from multiplying AV × ARO without applying EF, which is not a recognized calculation in the ALE methodology.

---

### Question 12

A Business Impact Analysis conducted for a retail company's online order processing system reveals the following: revenue loss begins immediately upon outage; regulatory penalties begin at the 24-hour mark; customer attrition becomes significant at 48 hours; and recovery from the most recent backup takes approximately six hours. Which BIA outputs should be established for this system?

- A) MTD = 6 hours; RTO = 48 hours; RPO = 24 hours
- B) MTD = 48 hours; RTO = 6 hours; RPO should be set based on backup frequency assessment
- C) MTD = 24 hours; RTO = 48 hours; RPO = 6 hours
- D) MTD = 48 hours; RTO = 24 hours; RPO = 6 hours

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: MTD is the maximum tolerable downtime — the point at which consequences become irreversible. Customer attrition at 48 hours represents the most serious lasting consequence, so MTD is 48 hours. RTO must be less than or equal to MTD; given that recovery from backup takes 6 hours and this is within the 48-hour MTD, 6 hours is a reasonable RTO ceiling. RPO must be determined by backup frequency analysis — the scenario does not specify backup interval, so this cannot be definitively set without additional information.
- Why A is incorrect: Setting MTD equal to the recovery time (6 hours) conflates a technical capability with a business impact threshold. MTD is derived from business consequence analysis, not from IT recovery capability.
- Why C is incorrect: Setting RTO to 48 hours — the full MTD — eliminates any recovery safety margin. The RTO should provide buffer within the MTD, not consume it entirely.
- Why D is incorrect: A 24-hour RTO would cut deeply into the 48-hour MTD window and is not justified by the scenario's data. The recovery time from backup is 6 hours, suggesting that a much shorter RTO is technically achievable.

---

### Question 13

A STRIDE analysis of a new web application identifies that the session management component is vulnerable to an attack in which an adversary captures a valid session token and replays it to gain unauthorized access without providing credentials. Which STRIDE category does this threat fall into?

- A) Tampering — because the attacker modifies the session token
- B) Repudiation — because the attacker denies performing the action
- C) Spoofing — because the attacker uses the captured token to impersonate an authenticated user
- D) Elevation of Privilege — because the attacker gains access beyond their authorization level

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: A session replay attack involves an attacker impersonating a legitimate authenticated user by replaying their valid credentials (the session token). The attacker presents themselves as someone they are not — which is the definition of spoofing. The spoofing target is the user identity, not the server.
- Why A is incorrect: Tampering involves unauthorized modification of data. In a session replay attack, the token is captured and reused intact, not modified. No data tampering occurs.
- Why B is incorrect: Repudiation involves an actor denying that they performed an action. The scenario describes gaining unauthorized access, not denying responsibility for a legitimate action.
- Why D is incorrect: Elevation of Privilege involves gaining capabilities beyond what is authorized. While the attacker does gain unauthorized access, the specific mechanism is identity impersonation (spoofing), not a privilege escalation attack on authorization controls.

---

### Question 14

A risk assessment team is analyzing a new cloud-hosted ERP system using PASTA (Process for Attack Simulation and Threat Analysis). The team has completed the first three stages: defining objectives, defining technical scope, and decomposing the application. Which stage comes next in the PASTA methodology?

- A) Threat analysis — identifying the specific threat actors and their objectives that could exploit the application
- B) Control implementation — selecting and deploying security controls for identified vulnerabilities
- C) Risk scoring — assigning quantitative risk scores to each identified scenario
- D) Regression testing — verifying that previously identified vulnerabilities have been remediated

**Correct Answer:** A

**Distractor Analysis:**

- Why A is correct: PASTA's seven stages in order are: (1) Define Objectives, (2) Define Technical Scope, (3) Decompose Application, (4) Threat Analysis, (5) Vulnerability and Weakness Analysis, (6) Attack Modeling and Simulation, (7) Risk and Impact Analysis. After decomposing the application, Stage 4 involves identifying threat agents, their capabilities, and their objectives.
- Why B is incorrect: Control implementation is not a PASTA stage. PASTA is a risk assessment and threat modeling methodology; control selection follows the methodology's outputs but is not part of the PASTA process itself.
- Why C is incorrect: Risk scoring occurs in Stage 7 (Risk and Impact Analysis), which is the final PASTA stage, not the stage immediately following decomposition.
- Why D is incorrect: Regression testing is a software development quality assurance activity, not a PASTA methodology stage. PASTA does not include a regression testing phase.

---

### Question 15

An analyst constructs a qualitative risk matrix for a manufacturing company. A vendor dependency risk is rated Likelihood: High, Impact: Medium. A cyberattack on production control systems is rated Likelihood: Low, Impact: Critical. The security manager must decide which risk to prioritize for treatment. Which analytical consideration should guide this decision?

- A) Always prioritize the higher-likelihood risk because frequency determines actual exposure
- B) Always prioritize the higher-impact risk because catastrophic outcomes are always worse than frequent moderate ones
- C) Apply the organization's risk appetite and the specific business consequences of each risk — a Critical-impact event may justify priority treatment even with Low likelihood if the potential consequence is irreversible
- D) Prioritize the risk that can be treated most inexpensively to demonstrate early program ROI

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Risk prioritization is not a mechanical exercise of always choosing higher likelihood or higher impact. The organization's risk appetite must be applied. For risks with Critical impact (production system shutdown, safety events, catastrophic financial loss), the potential irreversibility justifies elevated treatment priority even at Low likelihood. The business consequence of the event — not just the matrix cell — drives the decision.
- Why A is incorrect: Always prioritizing likelihood ignores impact severity. A Low-likelihood/Critical-impact risk may pose far greater organizational exposure than a High-likelihood/Medium-impact risk because the worst-case outcome is catastrophic.
- Why B is incorrect: Always prioritizing impact ignores the role of likelihood and risk appetite. A Critical-impact risk with near-zero likelihood may rank below a High-likelihood/High-impact risk in practice, depending on the organization's tolerance and the cost of treatment.
- Why D is incorrect: Treatment cost is a consideration in control selection (cost-benefit analysis), not in risk prioritization. Prioritizing cheap-to-treat risks regardless of their risk level produces a program that addresses low-value exposures while ignoring serious ones.

---

### Question 16

A security analyst is building a risk register for an e-commerce platform. For a SQL injection vulnerability, the analyst estimates a 60% probability that the vulnerability will be exploited within the next 12 months and a potential business impact of $500,000 per exploitation event. The analyst wants to calculate a simple quantitative risk score for prioritization purposes. What is the expected annual loss for this risk entry?

- A) $500,000, because the impact value represents the worst-case annual exposure
- B) $300,000, derived by multiplying the probability (0.60) by the impact ($500,000)
- C) $200,000, derived by subtracting the probability from the impact
- D) $830,000, derived by adding the probability percentage to the impact value

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: The expected loss calculation multiplies probability of occurrence by the magnitude of loss: 0.60 × $500,000 = $300,000. This is the standard expected value formula used in quantitative risk analysis to produce a probability-weighted annual loss estimate for prioritization purposes. It is equivalent to applying the ALE formula where ARO is expressed as an annual probability.
- Why A is incorrect: $500,000 is the impact magnitude without probability weighting — it represents the worst-case loss if the event occurs, not the expected annual loss. Using unweighted impact overstates expected loss for events with sub-100% probability.
- Why C is incorrect: Subtracting probability from impact has no basis in risk analysis methodology. Risk calculations multiply probability by impact; subtraction produces a meaningless number with no interpretable risk meaning.
- Why D is incorrect: Adding a percentage figure to a dollar figure is a dimensional error — the two values are not in the same units and cannot be summed. This calculation has no valid risk analysis basis.

---

### Question 17

An organization's BIA identifies three critical systems with the following MTD values: payroll processing (MTD = 72 hours), customer order management (MTD = 4 hours), and regulatory reporting (MTD = 24 hours). The disaster recovery team must sequence system recovery priorities. Which order correctly reflects the BIA-driven recovery sequence?

- A) Payroll → Regulatory Reporting → Customer Order Management
- B) Customer Order Management → Regulatory Reporting → Payroll Processing
- C) Regulatory Reporting → Customer Order Management → Payroll Processing
- D) All three systems have equal priority because all have defined MTD values

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: BIA-driven recovery prioritization sequences systems from lowest MTD to highest MTD — the system that will sustain irreversible harm soonest must be recovered first. Customer order management (MTD = 4 hours) is most urgent, followed by regulatory reporting (MTD = 24 hours), and payroll processing (MTD = 72 hours) last. Recovery priority is inversely proportional to MTD.
- Why A is incorrect: This sequence prioritizes the system with the longest MTD (payroll at 72 hours) first, which is the opposite of correct BIA-driven prioritization. Payroll has the most recovery time available and should be addressed last among the three.
- Why C is incorrect: While regulatory reporting (24 hours) and customer order management (4 hours) are correctly sequenced relative to each other, this option places them after each other incorrectly — the 4-hour MTD system must be first, not second.
- Why D is incorrect: Having a defined MTD does not confer equal priority. The entire purpose of MTD analysis is to differentiate recovery urgency. Systems with shorter MTDs have less tolerance for downtime and must be prioritized accordingly.

---

### Question 18

A threat analyst is performing a STRIDE analysis on a microservices architecture in which services communicate via an internal API gateway. The analyst identifies a scenario in which a compromised internal service could make API calls to other services using its legitimate service account credentials, accessing data and functions beyond its intended scope. Which STRIDE category does this threat fall into?

- A) Spoofing — because the compromised service is misrepresenting its identity
- B) Tampering — because the service is accessing data it was not designed to handle
- C) Elevation of Privilege — because the service is using legitimate credentials to access resources and functions beyond its authorized scope
- D) Information Disclosure — because data may be exfiltrated through the API calls

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Elevation of Privilege in STRIDE occurs when a component gains access to capabilities or resources beyond its authorized authorization boundary — even if it uses legitimate credentials to do so. The service is operating within its authenticated identity but exceeding its authorized scope of access. The violated security property is Authorization. This is a lateral movement scenario in a microservices context and is classified as privilege escalation even without a credential compromise.
- Why A is incorrect: Spoofing involves impersonating a different identity. The compromised service is using its own legitimate service account — it is not pretending to be a different service. The identity is authentic; the authorization boundary is being exceeded.
- Why B is incorrect: Tampering involves unauthorized modification of data. The scenario describes unauthorized access and function invocation, not unauthorized data modification. If the service were writing or altering records beyond its scope, tampering would also apply, but the primary STRIDE category for the described access pattern is Elevation of Privilege.
- Why D is incorrect: Information Disclosure describes unauthorized exposure of data to unintended parties. While data exfiltration could be a consequence of this scenario, the mechanism being analyzed — a service exceeding its authorized access scope — is an authorization failure (Elevation of Privilege), not an information disclosure event. STRIDE analysis categorizes the threat mechanism, not the potential downstream outcome.

---

### Question 19

During a risk assessment workshop, a senior engineer argues that qualitative risk ratings are useless because two assessors rating the same risk independently will often assign different likelihood and impact scores. A junior analyst suggests that this subjectivity problem can be solved by always using ALE-based quantitative analysis instead. Which response best addresses both arguments?

- A) The senior engineer is correct — qualitative analysis should be abandoned in favor of quantitative methods in all professional security programs
- B) The junior analyst is correct — ALE calculations eliminate subjectivity because they use financial figures rather than descriptive ratings
- C) Both have valid points, but neither position is absolute: qualitative analysis is appropriate for broad, rapid assessments and can be improved by calibration workshops and defined rating criteria; quantitative analysis reduces but does not eliminate subjectivity because input estimates (AV, EF, ARO) are themselves subjective judgments, particularly for rare events
- D) The subjectivity problem only exists in qualitative analysis conducted by inexperienced analysts; experienced practitioners produce identical qualitative ratings

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Both methods involve subjectivity, just at different points. Qualitative analysis embeds subjectivity in the descriptive rating scale. Quantitative ALE analysis embeds subjectivity in the input estimates — asset value, exposure factor, and annual rate of occurrence are all human judgments, particularly for rare or novel threats. Neither method is objectively superior in all contexts; the choice depends on available data, time, scope, and the decision being supported. Improving qualitative consistency through calibration is a recognized practice.
- Why A is incorrect: Discarding qualitative analysis entirely is not viable or recommended. Qualitative methods are appropriate and sufficient for many risk assessment contexts, particularly broad portfolio assessments, early-stage program development, and situations where financial asset data is unavailable.
- Why B is incorrect: ALE calculations do not eliminate subjectivity. The financial figures used as inputs — especially ARO for rare events like a nation-state attack — are expert estimates, not objective measurements. Converting a subjective probability estimate to a dollar figure does not make it objective; it only changes the form of the subjectivity.
- Why D is incorrect: Even highly experienced practitioners will assign different qualitative ratings to ambiguous risks without structured calibration. Interrater reliability in qualitative risk assessment is a documented challenge that experience alone does not eliminate.

---

### Question 20

A retail organization completes a BIA for its loyalty rewards platform. The analysis reveals: Revenue Impact = $12,000/hour; Customer Impact = begins degrading loyalty program trust after 6 hours; Recovery from backup = 3 hours. The recovery team proposes an RTO of 8 hours and an RPO of 4 hours. The CISO reviews the proposal and rejects the RTO. Which reasoning best supports the CISO's rejection?

- A) The proposed RTO of 8 hours is shorter than the recovery time from backup, making it technically unachievable
- B) The proposed RTO of 8 hours exceeds the 6-hour customer impact threshold, meaning the organization would tolerate the onset of irreversible customer trust damage before achieving recovery — the RTO must be set below this threshold to provide a meaningful safety margin
- C) The proposed RPO of 4 hours is too aggressive given the 3-hour backup recovery time
- D) BIA outputs do not constrain RTO values — RTO is set by the IT department based on technical recovery capabilities

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: The RTO must be set below the business impact threshold that defines the MTD — in this scenario, the 6-hour customer trust degradation point. An RTO of 8 hours means the organization plans to recover after customer harm has already begun, eliminating any recovery safety margin. The correct RTO should be less than 6 hours so that recovery is achieved before irreversible customer impact occurs. With a 3-hour backup recovery time, an RTO of 4–5 hours is technically achievable and provides appropriate buffer.
- Why A is incorrect: The proposed RTO of 8 hours is actually longer than the 3-hour backup recovery time, not shorter — meaning it is technically achievable. The CISO's objection is business-driven (the RTO exceeds the customer impact threshold), not technically motivated.
- Why C is incorrect: The RPO of 4 hours is not addressed in the CISO's rejection. RPO concerns the maximum acceptable data loss, not the recovery timeline. With a 3-hour backup recovery time, an RPO of 4 hours means the organization may lose up to 4 hours of loyalty data — a separate business decision unrelated to the RTO issue.
- Why D is incorrect: BIA outputs are specifically designed to constrain RTO and RPO by establishing the business impact thresholds (MTD and MTDL) within which recovery must occur. IT-defined RTOs that exceed business impact thresholds are not acceptable governance outcomes — the BIA exists precisely to prevent this.
