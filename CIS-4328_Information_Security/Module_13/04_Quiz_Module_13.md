# Quiz: Module 13 — Risk Management

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. This quiz is open-note but must reflect your own work. Questions are written to match the difficulty and style of the CompTIA Security+ SY0-701 exam.

---

## Question 1

A security analyst is asked to calculate the Annual Loss Expectancy for a web server. The server has an asset value of $600,000. A successful DDoS attack would cause 30% of its value in damage. Such attacks occur approximately twice per year. What is the ALE?

A) $36,000

B) $180,000

C) $360,000

D) $120,000

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: This result would come from multiplying the AV × EF without applying the ARO, then dividing incorrectly. SLE = $600,000 × 0.30 = $180,000. Multiplying by ARO of 2: ALE = $360,000.
- Why B is incorrect: $180,000 is the SLE — the Single Loss Expectancy from one attack. The question asks for ALE, which multiplies SLE by the Annual Rate of Occurrence: $180,000 × 2 = $360,000.
- Why D is incorrect: $120,000 would result from multiplying AV × ARO without using EF. This conflates different parts of the formula and produces a meaningless result.

---

## Question 2

An organization discovers that it has an unpatched vulnerability in its public-facing web server. No attack has yet exploited this vulnerability. From a risk management perspective, what is the current state of this situation?

A) A threat exists but no risk, because no attack has occurred

B) A vulnerability exists, and if a threat actor exploits it, the organization is at risk

C) Risk exists because both a vulnerability and the potential for a threat to exploit it are present

D) No risk exists until the organization quantifies the financial impact with an ALE calculation

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Risk is not contingent on an attack having occurred. Risk is the combination of threat potential, vulnerability, and impact. The unpatched vulnerability, combined with the existence of threat actors who exploit web server vulnerabilities, creates risk even before exploitation.
- Why B is incorrect: This answer correctly identifies that risk depends on both a vulnerability and a threat, but presents it as a conditional future state. The risk already exists — it does not require waiting to see if exploitation occurs.
- Why D is incorrect: While quantitative analysis is valuable, risk does not cease to exist in the absence of an ALE calculation. Qualitative risk assessment is equally valid. Risk is an organizational reality that exists whether or not it has been formally quantified.

---

## Question 3

A company purchases cyber insurance that covers financial losses up to $5 million in the event of a ransomware attack. The insurance does not prevent the attack or reduce the likelihood of it occurring. Which risk management strategy does this represent?

A) Risk avoidance

B) Risk mitigation

C) Risk acceptance

D) Risk transference

**Correct Answer:** D

**Distractor Analysis:**

- Why A is incorrect: Risk avoidance eliminates the risk by stopping the activity that creates it. Purchasing insurance does not stop the company from operating internet-connected systems or change any aspect of the threat landscape — it only addresses the financial aftermath.
- Why B is incorrect: Risk mitigation reduces the likelihood or impact of the risk through controls. Cyber insurance does not reduce the likelihood of attack or the operational impact — it compensates the financial loss after the fact.
- Why C is incorrect: Risk acceptance means acknowledging the risk and deciding not to take additional action. Purchasing insurance is an active risk treatment — the organization is paying money to shift financial exposure to the insurer, which is the definition of transference.

---

## Question 4

A security team has mitigated a risk by implementing multiple controls. The risk has been reduced significantly, but the team acknowledges that some risk remains even with all controls in place. What is the term for the risk that remains after all controls have been applied?

A) Inherent risk

B) Control risk

C) Residual risk

D) Acceptable risk

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Inherent risk is the risk level before any controls are applied — raw exposure. The question describes risk after controls have been applied, which is the opposite.
- Why B is incorrect: Control risk is the risk that a control fails to operate as intended. It is not the term for overall remaining risk after controls are implemented.
- Why D is incorrect: "Acceptable risk" describes whether remaining risk is within tolerance — it is a judgment about the level of residual risk, not a term for the risk itself. The technical term for remaining risk after controls is residual risk.

---

## Question 5

A hospital's Business Impact Analysis determines that the electronic health record system has a Maximum Tolerable Downtime of 4 hours. The hospital's IT team sets a Recovery Time Objective of 6 hours for the EHR system. What is the problem with this configuration?

A) The RTO is set too low, causing unnecessary costs to achieve fast recovery

B) The RTO exceeds the MTD, meaning the target recovery time would occur after unacceptable harm has already begun

C) The RTO and MTD should be equal — setting them at different values is a configuration error

D) MTD is not a BIA concept; it is a network availability metric

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: An RTO of 6 hours is not low — it is higher than the MTD. The problem is that the RTO extends beyond the MTD, not that the RTO is set too low.
- Why C is incorrect: RTO and MTD serve different purposes and are designed to be different values. RTO must be less than MTD — setting them equal provides no buffer. A well-designed system sets RTO significantly shorter than MTD to account for unexpected delays in recovery.
- Why D is incorrect: MTD (Maximum Tolerable Downtime) is a core BIA concept defined in NIST SP 800-34. It is specifically used in contingency and business continuity planning, not network availability metrics.

---

## Question 6

An organization reviews a risk in its risk register. The risk owner is the VP of Finance. The risk score is 18 out of 25 on the qualitative matrix. The organization decides that the cost of treating the risk exceeds the value of the asset it protects and formally documents the decision with the VP of Finance's signature. Which risk response strategy is being applied?

A) Risk mitigation

B) Risk transference

C) Risk avoidance

D) Risk acceptance

**Correct Answer:** D

**Distractor Analysis:**

- Why A is incorrect: Risk mitigation involves implementing controls to reduce likelihood or impact. No controls are being implemented — the organization is deciding not to act.
- Why B is incorrect: Risk transference shifts financial liability to a third party. No insurance, contract, or third-party arrangement is described — the organization is internally absorbing the risk.
- Why C is incorrect: Risk avoidance eliminates the risk by stopping the activity. The scenario describes documentation of a decision to live with the risk, not discontinuation of the activity.

---

## Question 7

A security analyst is comparing qualitative and quantitative risk analysis methods to recommend an approach to the CISO. The CISO wants to be able to directly compare the cost of a specific security control to the financial benefit of reducing the risk. Which analysis method meets this requirement?

A) Qualitative analysis, because risk matrices produce relative scores that can be compared to budget items

B) Quantitative analysis, because ALE provides a dollar value for risk that can be directly compared to control costs

C) Both methods equally — qualitative and quantitative provide equivalent financial outputs

D) Neither method — financial comparison of controls requires a separate ROI analysis framework

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Qualitative analysis produces relative scores (e.g., High/Medium/Low or 1–25 on a matrix). These scores do not have monetary units and cannot be directly compared to a dollar cost of a control. ALE, from quantitative analysis, produces a dollar value.
- Why C is incorrect: The methods produce fundamentally different outputs. Qualitative analysis produces relative priority scores. Quantitative analysis produces monetary values that can be subtracted from control costs to compute net benefit.
- Why D is incorrect: Quantitative risk analysis (ALE) is specifically designed for this purpose. The Value of Safeguard formula = (pre-control ALE) − (post-control ALE) − (annual control cost) directly quantifies the economic benefit of a security investment.

---

## Question 8

A company's database server has an ARO of 0.25 for a specific threat. What does an ARO of 0.25 mean?

A) There is a 25% likelihood per day that the threat will occur

B) The threat is expected to occur once every four years

C) The threat will cause 25% of the asset's value in damage per occurrence

D) There is a 75% likelihood that the threat will not occur this year

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: ARO is an annual rate, not a daily rate. An ARO of 0.25 means 0.25 occurrences per year — which equals once every 4 years (1 ÷ 0.25 = 4).
- Why C is incorrect: The percentage of asset value damaged per occurrence is the Exposure Factor (EF), not the Annual Rate of Occurrence. ARO is a frequency metric, not a damage severity metric.
- Why D is incorrect: While it is true that there is a 75% chance the event does not occur in any given year (since the expected occurrence is 0.25 per year), this is not the definition of ARO. ARO is the expected number of occurrences per year, not a complementary probability statement.

---

## Question 9

A risk register entry reads: "Risk: Unauthorized physical access to the server room. Category: Physical. Likelihood: Low. Impact: High. Response: Biometric lock installed, access log maintained, security cameras added." After implementing these controls, the residual risk is rated Medium-Low. What does "residual risk" mean in this context?

A) The original risk before any controls were applied

B) The risk that remains after the biometric lock, access log, and cameras have been implemented

C) The risk that the biometric lock will fail to function as intended

D) The risk that was transferred to the physical security vendor

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The original risk before controls is inherent risk, not residual risk. The scenario explicitly states that controls have been implemented, and residual risk is what remains after those controls.
- Why C is incorrect: The risk that a control fails is control risk, not residual risk. Residual risk is the overall remaining exposure to the original threat after all controls are in place.
- Why D is incorrect: No risk transfer is described in the scenario. Risk transfer would involve insurance or a contractual shift of liability to the vendor, which is not mentioned. The controls described are all mitigation actions.

---

## Question 10

A company's RPO for its customer order database is 2 hours. The IT team currently performs daily database backups at 11:00 PM. A system failure occurs at 4:00 PM. Which statement is true about the data loss the company will experience?

A) No data will be lost because the database can be recovered from the 11:00 PM backup

B) Up to 17 hours of data will be lost, which exceeds the 2-hour RPO

C) Exactly 2 hours of data will be lost, matching the RPO threshold

D) Up to 2 hours of data will be lost because the RPO provides automatic backup protection at that interval

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The 11:00 PM backup captured data as of 11:00 PM the previous night. The failure occurred at 4:00 PM the next day — 17 hours after the last backup. All 17 hours of transactions since the 11:00 PM backup are potentially lost.
- Why C is incorrect: Exactly 2 hours of data loss would only occur if the backup ran at 2:00 PM that day. The backup runs daily at 11:00 PM, not every 2 hours.
- Why D is incorrect: RPO is a target, not an automatic mechanism. An RPO of 2 hours means the organization requires that no more than 2 hours of data can be lost — which means backups must run at least every 2 hours. The current daily backup system does not meet the 2-hour RPO.

---

*End of Quiz — Module 13*
