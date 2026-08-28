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

---

## Question 11

A security manager calculates the ALE for a web application vulnerability as $320,000 per year. A web application firewall (WAF) costs $45,000 per year and is expected to reduce the ALE to $80,000. What is the Value of Safeguard for the WAF?

- A) $195,000
- B) $240,000
- C) $275,000
- D) $320,000

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: $240,000 is the ALE reduction ($320,000 − $80,000) without subtracting the annual control cost. The value of safeguard formula requires subtracting the safeguard's cost: $240,000 − $45,000 = $195,000.
- Why C is incorrect: $275,000 results from subtracting only the post-control ALE from the pre-control ALE without the correct formula application. The annual cost of the safeguard must also be deducted.
- Why D is incorrect: $320,000 is the pre-control ALE — the baseline risk value before any control is applied. The value of safeguard formula compares the benefit of the control against its cost, not the pre-control ALE in isolation.

---

## Question 12

A CISO presents risk findings to the board and uses descriptive labels such as "High," "Medium," and "Low" to classify risks based on probability and impact. The board asks why the CISO did not provide specific dollar figures for each risk. The CISO explains that the available data does not support precise financial estimates. What analysis method is being used and what is its primary limitation in this context?

- A) Quantitative analysis; the limitation is that it requires too many personnel to complete
- B) Qualitative analysis; the limitation is that it cannot directly support cost-benefit comparison of specific controls
- C) Semi-quantitative analysis; the limitation is that it produces too many false positives
- D) Quantitative analysis; the limitation is that it produces subjective results that vary by analyst

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The analysis described — descriptive labels without dollar figures — is qualitative, not quantitative. Quantitative analysis produces financial values like ALE.
- Why C is incorrect: Semi-quantitative analysis assigns numerical scores to qualitative categories to allow limited mathematical operations. The scenario describes pure descriptive ratings without numerical scoring, which is qualitative analysis.
- Why D is incorrect: Quantitative analysis uses financial data and formulas (AV, EF, ARO) to produce monetary values. The scenario explicitly describes non-financial descriptive labels, which is the defining characteristic of qualitative analysis.

---

## Question 13

An organization's risk appetite statement reads: "We will not accept any residual risk above Medium on our 5×5 matrix for systems containing PHI." A newly identified risk affecting the EMR system scores 16 on the risk matrix and no controls have been applied yet. What must the organization do to comply with its risk appetite statement?

- A) Nothing — a score of 16 is within the acceptable range since it falls below 25
- B) Apply controls to reduce the risk score to Medium (score 9 or below) before formal risk acceptance
- C) Transfer the risk to cyber insurance and document the transfer as acceptance
- D) Formally accept the risk and document it with the CISO's signature

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: A score of 16 on a 5×5 matrix corresponds to a High risk level (typically scores of 12 and above represent High on standard matrices). The organization's risk appetite statement prohibits residual risk above Medium for PHI systems, so a score of 16 requires treatment.
- Why C is incorrect: Risk transference (insurance) reduces financial exposure but does not eliminate the operational risk. The risk appetite statement restricts residual risk scores — a transferred risk still exists with the same likelihood and impact. Transferring and then accepting still results in residual risk above the stated tolerance.
- Why D is incorrect: Formal acceptance is only appropriate when residual risk is within tolerance. The risk appetite statement explicitly prohibits accepting residual risk above Medium for PHI systems, making acceptance a compliance violation.

---

## Question 14

A company's BIA identifies that its point-of-sale system has an RTO of 1 hour and an RPO of 15 minutes. Which backup and recovery configuration meets BOTH requirements?

- A) Daily full backups to offsite storage with 24-hour tape delivery
- B) Continuous database replication to a hot standby with automated failover in under 5 minutes and transaction logs every 10 minutes
- C) Weekly full backups with 4-hour restoration time and 6-hour transaction log shipping
- D) Daily incremental backups with 2-hour restoration from last night's backup

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Daily backups with 24-hour tape delivery fails both requirements. The RPO would be up to 24 hours of data loss (exceeds 15-minute RPO), and the RTO of delivering and restoring from tape far exceeds 1 hour.
- Why C is incorrect: Weekly full backups with 4-hour restoration fails the 1-hour RTO. Six-hour transaction log shipping also fails the 15-minute RPO, which requires transaction capture intervals of 15 minutes or less.
- Why D is incorrect: Daily incremental backups fail the 15-minute RPO since up to 24 hours of transactions may be at risk. A 2-hour restoration also fails the 1-hour RTO.

---

## Question 15

An organization discovers a zero-day vulnerability in its ERP system. The vendor has not yet released a patch. The security team implements network segmentation to isolate the ERP system from the rest of the internal network, reducing the attack surface. Which risk response strategy is being applied and why?

- A) Risk avoidance — the organization has stopped using the ERP system
- B) Risk acceptance — no patch is available so the organization has decided to do nothing
- C) Risk mitigation — the segmentation reduces the likelihood or impact of exploitation without eliminating the activity
- D) Risk transference — the organization has contracted with the ERP vendor to assume liability

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Risk avoidance would require the organization to shut down the ERP system entirely. Implementing network segmentation allows the system to continue operating — the organization has not eliminated the activity.
- Why B is incorrect: Risk acceptance is a deliberate, documented decision not to apply additional controls. Installing network segmentation is an active control action that reduces exposure — this is mitigation, not acceptance.
- Why D is incorrect: No contractual transfer to the vendor is described. The organization is implementing an internal technical control. Risk transference requires shifting financial exposure to a third party through insurance or contract.

---

## Question 16

A financial services firm uses MTBF data to plan hardware replacement cycles. A server model has an MTBF of 50,000 hours. The firm has 20 servers of this model in continuous operation. Approximately how many servers would be expected to fail in a given year?

- A) 1
- B) 2
- C) 4
- D) 20

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: One failure per year would correspond to an MTBF of approximately 175,200 hours (8,760 hours/year × 20 servers ÷ 1 failure). The actual MTBF is 50,000 hours, which predicts approximately 3.5 failures per year across 20 servers.
- Why B is incorrect: Two failures per year would correspond to an MTBF of approximately 87,600 hours per server. The MTBF of 50,000 hours predicts more frequent failures than this.
- Why D is incorrect: 20 failures per year would mean every server fails annually, requiring an MTBF of 8,760 hours. At 50,000 hours MTBF, each server is expected to fail approximately every 5.7 years, not every year.

---

## Question 17

During a risk assessment, an analyst notes that a critical application server has no redundant power supply and is connected to a single uninterruptible power supply (UPS). The building experiences brief power flickers approximately 12 times per year, each lasting under 2 seconds. The UPS protects the server from these events but has a 15% chance of failing to hold power for the full duration of any given flicker. What is the ARO for a power-related server failure?

- A) 0.15
- B) 1.8
- C) 12
- D) 0.012

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: 0.15 is the probability of UPS failure per individual flicker event. It is not the annual rate of occurrence. The ARO must account for the frequency of flickers multiplied by the probability of UPS failure.
- Why C is incorrect: 12 is the number of flicker events per year. This would only be the ARO if the UPS provided no protection. Because the UPS fails only 15% of the time, the actual ARO is 12 × 0.15 = 1.8 failures per year.
- Why D is incorrect: 0.012 is a nonsensical result that does not follow from the given data. It may result from dividing 0.15 by 12 rather than multiplying.

---

## Question 18

A risk manager is constructing a risk register entry for a SQL injection vulnerability in the company's customer portal. The portal stores 500,000 customer records including credit card data. The manager notes that SQL injection is listed on the OWASP Top 10 and that the CVSS score for the specific vulnerability is 9.1. Which risk register field is BEST populated by the CVSS score?

- A) Risk Response
- B) Risk Owner
- C) Likelihood
- D) Impact (or used to inform the combined Risk Score)

**Correct Answer:** D

**Distractor Analysis:**

- Why A is incorrect: Risk Response is the treatment strategy selected (avoid, transfer, mitigate, accept). It is determined after the risk is assessed, not populated with a CVSS score.
- Why B is incorrect: Risk Owner is the organizational role accountable for the risk. CVSS scores describe vulnerability severity, not organizational accountability.
- Why C is incorrect: CVSS scores measure the severity of a vulnerability if successfully exploited, with components including Attack Vector, Attack Complexity, and Privileges Required. While CVSS includes exploitability metrics, the score as a whole is more representative of combined severity (impact and exploitability together). A high CVSS score means the vulnerability is severe if exploited — it primarily informs impact assessment rather than independently representing likelihood of exploitation in the organization's specific environment.

---

## Question 19

An organization's security team identifies a risk related to third-party SaaS vendor access to sensitive customer data. The team recommends requiring the vendor to maintain ISO 27001 certification, undergo annual penetration testing, and carry its own cyber liability insurance. Which risk response strategy do these requirements primarily represent?

- A) Risk avoidance
- B) Risk mitigation through contractual controls
- C) Risk acceptance
- D) Risk elimination

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Risk avoidance would mean not using the SaaS vendor at all. The organization continues to use the vendor but imposes security requirements — this is management of the risk through controls, not elimination of the activity.
- Why C is incorrect: Risk acceptance means acknowledging a risk and deciding not to apply additional controls. Requiring certifications, penetration testing, and insurance are all active control requirements — the opposite of acceptance.
- Why D is incorrect: Risk elimination is not a standard NIST risk response category. It is sometimes informally used to describe avoidance, but no standard framework lists it as a distinct strategy. The controls described actively reduce the risk rather than eliminating the vendor relationship.

---

## Question 20

A healthcare organization completes a Business Impact Analysis for its telehealth platform. The BIA finds that if the platform is unavailable, physicians can use telephone consultations as a workaround indefinitely. Patient safety is not compromised by the outage. The revenue impact becomes significant only after 5 days of outage. How should the BIA team set the MTD and RTO for the telehealth platform?

- A) MTD = 1 hour, RTO = 30 minutes because patient-facing systems must always have tight recovery targets
- B) MTD = 5 business days, RTO = significantly less than 5 days (e.g., 24 to 48 hours) to provide recovery buffer before business viability is threatened
- C) MTD = unlimited because a telephone workaround exists
- D) RTO = 0 hours because healthcare systems cannot have any downtime

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: MTD is determined by the actual business and operational impact of the outage, not a generic rule about patient-facing systems. The BIA specifically found that patient safety is not compromised and business impact only occurs after 5 days. Setting MTD at 1 hour is not justified by the findings and would drive unnecessary investment in high-availability infrastructure.
- Why C is incorrect: MTD is never truly unlimited. Even with a telephone workaround, prolonged outage of the telehealth platform has cumulative impacts on patient experience, physician workflow, and eventually revenue. The BIA establishes that significant business impact begins at 5 days, which is the appropriate basis for MTD.
- Why D is incorrect: Zero RTO means instantaneous recovery with no downtime — this is technically achievable only with fully redundant active-active architectures and is extremely expensive. The BIA findings do not justify this investment level. RTO must be grounded in actual business requirements from the BIA.

---

*End of Quiz — Module 13*
