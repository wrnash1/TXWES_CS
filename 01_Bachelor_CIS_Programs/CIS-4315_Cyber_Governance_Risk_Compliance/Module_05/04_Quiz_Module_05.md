# Quiz: Module 05 — Risk Treatment and Control Selection

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

**Instructions:** Choose the single best answer for each question.

---

### Question 1

An organization's risk assessment reveals that a proposed new business service would create an information security risk with an ALE of $4.2 million annually. After evaluating all available controls, the security team determines that no feasible combination of controls can reduce the ALE below $1.8 million — well above the organization's risk tolerance threshold. The organization decides not to launch the service. Which risk treatment option has the organization chosen?

- A) Risk acceptance
- B) Risk transfer
- C) Risk avoidance
- D) Risk mitigation

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The organization eliminated the risk entirely by deciding not to pursue the activity that would have created it. This is the definition of risk avoidance — the risk no longer exists because the organization chose not to engage in the risky activity.
- Why A is incorrect: Risk acceptance means deciding to tolerate a known risk without additional treatment. The organization did not accept this risk — it eliminated the activity that would have created it.
- Why B is incorrect: Risk transfer shifts the financial consequences to a third party through insurance or contract, but the activity continues. The organization in this scenario stopped the activity entirely.
- Why D is incorrect: Risk mitigation reduces the risk through controls. The scenario explicitly states no feasible controls could reduce the risk to an acceptable level, and the organization's response was to stop the activity — not to implement partial controls.

---

### Question 2

A security manager formally documents that a low-severity risk affecting an internal file-sharing service has been reviewed, assessed, and determined to fall within the organization's risk appetite. An authorized manager has signed the acceptance record. The risk is entered in the risk register with a documented acceptance decision. Which statement best describes this situation?

- A) This is informal risk acceptance and represents a governance failure
- B) This is formal risk acceptance and represents appropriate risk governance
- C) This is risk avoidance because the organization chose not to mitigate the risk
- D) This is risk transfer because the manager's signature shifts accountability to that individual

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Formal risk acceptance requires that the risk be identified, assessed, documented, reviewed by an authorized decision-maker, and explicitly accepted with the decision recorded. All of these elements are present. This is exemplary risk governance practice.
- Why A is incorrect: Informal risk acceptance (negligence) means a risk was never identified, reviewed, or decided upon. The scenario describes the opposite — a structured, documented process with appropriate authorization.
- Why C is incorrect: Avoidance eliminates the risk by stopping the associated activity. The organization continued operating the file-sharing service — they accepted the residual risk, not avoided the activity.
- Why D is incorrect: Risk transfer shifts financial consequences to a third party through insurance or contract. A manager signing an acceptance record does not constitute risk transfer — it constitutes documented risk acceptance within the organization's governance framework.

---

### Question 3

A manufacturing company implements a strict visitor badge policy requiring all non-employees to wear visible identification badges at all times and display them to security personnel upon request. Guards are stationed at all facility entrances. Which combination of control functional types do these measures represent?

- A) Preventive and corrective
- B) Deterrent and detective
- C) Preventive and detective
- D) Corrective and deterrent

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The visitor badge policy and security personnel at entrances serve as preventive controls — they physically stop unauthorized individuals from entering without proper identification. The visible badge requirement and guard checks are also detective — guards actively identify visitors and can detect unauthorized individuals or badge violations. Both functional types are present.
- Why A is incorrect: Corrective controls restore normal operations after a security event. Neither the badge policy nor the guard presence restores anything — they prevent and detect unauthorized access.
- Why B is incorrect: Deterrent controls discourage harmful actions through the perception of consequences (like warning signs or visible cameras). The described controls go beyond deterrence — they actively prevent unauthorized access (preventive) and identify visitors (detective). Deterrence alone would be insufficient to describe security personnel who physically verify credentials.
- Why D is incorrect: Corrective controls address recovery after an incident — none of the described controls restore systems or operations. The deterrent element is partially present (visible security presence discourages unauthorized attempts) but preventive and detective are more precise characterizations of these specific controls.

---

### Question 4

An organization's firewall rules prevent unauthorized inbound traffic (preventive), the SIEM alerts on anomalous outbound connections (detective), and the incident response team can isolate affected systems within 15 minutes of an alert (corrective). This arrangement best exemplifies which security strategy?

- A) Risk transfer through technology
- B) Formal risk acceptance with compensating controls
- C) Defense in depth using layered controls of different functional types
- D) Risk avoidance through technical enforcement

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Defense in depth means applying multiple overlapping layers of controls so that if one layer fails, others compensate. The scenario explicitly combines preventive (firewall), detective (SIEM), and corrective (incident response isolation) controls — the classic description of a layered, defense-in-depth architecture.
- Why A is incorrect: Risk transfer shifts financial consequences to a third party through insurance or contracts — technology does not constitute risk transfer regardless of how sophisticated it is.
- Why B is incorrect: Formal risk acceptance means a decision-maker has decided to tolerate a risk without additional controls. The scenario describes active, layered controls being implemented — the opposite of risk acceptance.
- Why D is incorrect: Risk avoidance eliminates the activity creating the risk. The organization in this scenario is actively operating systems and implementing controls — it has not avoided any activity.

---

### Question 5

An organization discovers that an employee has been accessing financial records outside their normal work hours and job responsibilities. Management responds by issuing a written warning and reminding all staff of the acceptable use policy. Which control functional type does the acceptable use policy reminder represent?

- A) Preventive
- B) Corrective
- C) Detective
- D) Deterrent

**Correct Answer:** D

**Distractor Analysis:**

- Why D is correct: Publishing and reinforcing an acceptable use policy discourages future violations by making employees aware that the behavior is prohibited and that violations have consequences. This is the definition of a deterrent control — it influences behavior through perceived consequences rather than technically preventing or detecting actions.
- Why A is incorrect: A preventive control technically stops an action from occurring — for example, an access control system that blocks the employee from accessing unauthorized records. Reminding employees of a policy does not technically prevent future access violations.
- Why B is incorrect: Corrective controls restore normal operations after an incident. The acceptable use policy reminder does not restore anything — it is forward-looking behavioral guidance.
- Why C is incorrect: A detective control identifies that a security event has occurred. The access monitoring that revealed the unusual behavior is the detective control in this scenario. The policy reminder that follows is a response aimed at deterring future violations, not detecting current ones.

---

### Question 6

An organization purchases a cyber liability insurance policy that covers breach notification costs, forensic investigation expenses, and regulatory fines resulting from a data breach. Three months later, the organization suffers a breach. The insurance covers $1.8 million of the $2.4 million total cost. Which statement most accurately describes the risk treatment outcome?

- A) The insurance policy was an example of risk avoidance because it prevented $1.8 million in losses
- B) The insurance policy successfully transferred the entire risk, but the organization still owed $600,000 due to a deductible
- C) The risk transfer partially succeeded in shifting financial impact, but operational disruption and reputational damage remained with the organization
- D) The risk was fully mitigated because the financial impact was substantially reduced by the insurance payout

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Insurance is a risk transfer mechanism — it shifts financial consequences to a third party. However, transfer is never complete: operational disruption (systems were still breached, operations still impacted), reputational damage, and regulatory scrutiny remained with the organization regardless of the insurance payout. The $600,000 gap is also evidence that transfer was only partial even financially.
- Why A is incorrect: Avoidance eliminates the risk by eliminating the activity. The organization experienced the breach — the risk event occurred. Insurance did not prevent anything; it only transferred some of the financial consequences after the fact.
- Why B is incorrect: The scenario does not mention a deductible — the $600,000 gap may reflect policy limits, excluded coverages, or uncovered categories of loss. More importantly, framing the outcome purely in financial terms misses the key CISM insight: even complete financial coverage does not transfer operational and reputational consequences.
- Why D is incorrect: Mitigation reduces the likelihood or impact of a risk through controls. Insurance is transfer, not mitigation. Controls (like encryption, access management, incident response) would constitute mitigation. Insurance does not reduce the likelihood of a breach or improve the organization's technical security posture.

---

### Question 7

A security team is selecting controls to address the risk of unauthorized access to a cloud-hosted database containing customer personally identifiable information (PII). They are evaluating three options: database activity monitoring (logs all queries and alerts on unusual patterns), role-based access control (restricts database access to authorized roles only), and a data classification policy (defines PII handling requirements for all staff). Using the correct control categories, how should these three controls be classified?

- A) All three are technical controls
- B) Database activity monitoring is detective/technical; role-based access control is preventive/technical; data classification policy is administrative
- C) Database activity monitoring is corrective; role-based access control is deterrent; data classification policy is detective
- D) All three are preventive controls implemented through different methods

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Database activity monitoring identifies unauthorized or anomalous access after it occurs (detective) and is implemented in software (technical). Role-based access control stops unauthorized users from accessing the database (preventive) and is implemented in the database management system (technical). A data classification policy governs how employees handle data through documented requirements (administrative). Each control is correctly classified on both dimensions.
- Why A is incorrect: The data classification policy is not a technical control — it is a policy document governing human behavior, which makes it administrative. Only the database activity monitoring and role-based access control are technical controls.
- Why C is incorrect: Database activity monitoring is detective, not corrective — it identifies events rather than restoring operations. Role-based access control is preventive, not deterrent — it technically blocks unauthorized access rather than merely discouraging it. The data classification policy is administrative, not detective.
- Why D is incorrect: Database activity monitoring is detective, not preventive — it identifies events that have already occurred or are occurring. Controls cannot all be preventive simply because they all address the same risk.

---

### Question 8

An organization has calculated that a proposed security control would cost $120,000 per year to operate and would reduce the ALE for a specific risk from $310,000 to $85,000. What is the net annual benefit of implementing this control, and is the investment cost-justified?

- A) Net benefit is $225,000; the investment is cost-justified
- B) Net benefit is $105,000; the investment is cost-justified
- C) Net benefit is -$120,000; the investment is not cost-justified because it adds cost
- D) Net benefit is $190,000; the investment is not cost-justified because residual ALE exceeds $50,000

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: ALE reduction = $310,000 - $85,000 = $225,000. Net benefit = $225,000 - $120,000 (annual control cost) = $105,000. Since net benefit is positive, the investment is cost-justified under standard ALE analysis. The control produces $1.875 in risk reduction for every $1 spent.
- Why A is incorrect: $225,000 is the ALE reduction — the gross benefit before subtracting the control's annual cost. The net benefit calculation must subtract the $120,000 annual cost: $225,000 - $120,000 = $105,000.
- Why C is incorrect: The control does add cost, but the cost is offset by the ALE reduction it provides. A negative net benefit would only occur if the annual control cost exceeded the ALE reduction — which is not the case here ($120,000 cost vs. $225,000 reduction).
- Why D is incorrect: $190,000 is neither the ALE reduction nor the net benefit — it appears to result from an incorrect calculation. Additionally, whether the residual ALE meets a specific risk appetite threshold is a separate question from whether the investment is cost-justified. Cost justification is determined solely by the net benefit calculation.

---

### Question 9

Which of the following most accurately describes residual risk?

- A) The risk that remains after all possible controls have been implemented, regardless of cost
- B) The risk that an organization decides to transfer to a third party through insurance
- C) The risk that remains after selected controls have been implemented and risk treatment actions completed
- D) The risk that existed before any controls were implemented, representing the organization's maximum exposure

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Residual risk is the risk level remaining after the organization's selected risk treatment actions — including implemented controls — have been applied. It is the "leftover" risk that the organization must formally accept or continue treating. Critically, it is defined relative to the controls actually implemented, not all theoretically possible controls.
- Why A is incorrect: Residual risk is not calculated after all possible controls — it is calculated after the controls the organization has chosen to implement. Organizations select controls based on cost-benefit analysis and risk appetite, not by implementing every conceivable safeguard.
- Why B is incorrect: Risk transferred through insurance reduces the financial exposure associated with residual risk, but residual risk itself refers to the total remaining risk level — not just the financial portion being transferred. Operational and reputational residual risk remains even after financial transfer.
- Why D is incorrect: Risk before any controls are implemented is sometimes called inherent risk — the natural risk level without any safeguards. Residual risk is always calculated after treatment, not before.

---

### Question 10

A CISO presents the following scenario to the board of directors: "We have identified a critical vulnerability in our payment processing system. Exploiting it requires specialized knowledge and would require the attacker to already have network access. We have implemented network segmentation and 24/7 monitoring. The residual ALE is $42,000 annually, which falls within our $50,000 risk appetite threshold. I recommend formal acceptance of the residual risk pending our planned system replacement in 18 months." Which element of this presentation is most essential to complete proper formal risk acceptance governance?

- A) The CISO must upgrade all controls to eliminate the vulnerability before any acceptance can occur
- B) A board member or authorized executive must formally sign the acceptance decision with the residual risk level and rationale documented in the risk register
- C) The organization must purchase cyber insurance coverage for at least $42,000 to cover the accepted residual risk
- D) The CISO's verbal recommendation to the board is sufficient to constitute formal risk acceptance

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Formal risk acceptance requires a documented decision made by an accountable decision-maker with appropriate authority. The CISO has provided analysis and a recommendation — but formal acceptance requires that an authorized official (board member, executive, or designated risk acceptance authority) review and sign the acceptance, and that the decision with its rationale be recorded in the risk register. The presentation is excellent preparation; the signature and documentation complete the governance requirement.
- Why A is incorrect: Formal acceptance is specifically the mechanism for tolerating residual risk that cannot be fully eliminated within available resources. Requiring elimination before acceptance would make acceptance meaningless as a governance concept. The scenario describes residual risk within appetite — acceptance is the appropriate and complete response.
- Why C is incorrect: Insurance is risk transfer, not a prerequisite for risk acceptance. Organizations may choose to transfer financial exposure from accepted residual risk, but it is not required for the acceptance decision itself. The scenario's $42,000 ALE is within appetite, and whether to insure it is a separate business decision.
- Why D is incorrect: Formal risk acceptance must be documented in writing and signed by an authorized decision-maker. Verbal recommendations — even to the board — do not constitute formal acceptance. Without written documentation, the organization cannot demonstrate in an audit or regulatory review that a deliberate, authorized decision was made.

---

*End of Module 05 Quiz*

---

### Question 11

A security team is assessing controls for a payment processing system and finds that the primary access control (role-based access) cannot be implemented for a legacy application that does not support modern authentication. The team recommends monitoring all user sessions on that application and limiting access to named individuals via a firewall rule. In the context of control frameworks, this approach is best described as:

- A) Risk avoidance, because the team is restricting who can access the system
- B) Defense in depth, because two separate controls address the same risk
- C) A compensating control arrangement, because substitute controls are used where the primary control cannot be implemented
- D) Administrative control selection, because session monitoring is a policy-based measure

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: PCI DSS and NIST SP 800-53 both recognize the concept of compensating controls — alternate measures used when the preferred or required control cannot be applied due to technical or business constraints. The firewall restriction and session monitoring together serve as substitutes for the role-based access control that the legacy application cannot support. Compensating controls must be documented, approved, and reviewed for adequacy.
- Why A is incorrect: Risk avoidance would mean eliminating the activity or system that creates the risk. The team is not recommending that the application be decommissioned; they are accepting continued use while applying substitute controls.
- Why B is incorrect: Defense in depth describes layering multiple controls around the same asset to reduce the likelihood that a single control failure creates a breach. While the two controls are layered, the defining characteristic here is that they are substitutes for an unavailable primary control — which is the compensating control concept, not simply defense in depth.
- Why D is incorrect: Session monitoring is a technical detective control, not an administrative one. Administrative controls include policies, procedures, training, and background checks — not software-based monitoring tools.

---

### Question 12

An organization's risk manager is reviewing the risk register and notices that 14 of the 40 logged risks have had no status update in more than 12 months. The risk owners have not been reassigned and the treatment plans have not been executed. Which governance deficiency does this situation most directly illustrate?

- A) Failure to perform a threat and vulnerability assessment
- B) Absence of a risk appetite statement
- C) Inadequate risk treatment execution and risk register maintenance
- D) Lack of an approved information security policy

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: A risk register is a living governance document that must be actively maintained. ISO 31000 and NIST SP 800-39 both emphasize that identified risks must be assigned owners, that treatment plans must be executed and tracked, and that the register must be reviewed regularly to reflect current status. Stale entries indicate that the monitoring and review phase of the risk management process has broken down — a governance failure in risk register maintenance and treatment accountability.
- Why A is incorrect: Threat and vulnerability assessments produce inputs to the risk register; the problem here is not identification of risks but failure to act on already-identified risks. The register exists — it is just not being maintained or executed against.
- Why B is incorrect: A missing risk appetite statement would cause problems in risk evaluation and acceptance decisions, but it would not directly cause treatment plans to go unexecuted for 12 months. The register entries already exist, implying prior assessment was conducted.
- Why D is incorrect: A missing information security policy is a governance gap, but it does not explain why specific, logged risk treatment actions are not being implemented. Treatment plan execution is a management accountability issue, not a policy existence issue.

---

### Question 13

After implementing a new set of technical controls, a CISO conducts a control effectiveness review and finds that the residual risk for three assets remains above the organization's stated risk appetite. The risk treatment budget has been exhausted for the fiscal year. Which of the following is the most appropriate governance action?

- A) Accept the residual risk informally and address it in the next budget cycle
- B) Escalate the residual risk exceedances to the risk committee or board for formal review and decision
- C) Remove the affected assets from the risk register until budget is available
- D) Implement additional technical controls on a best-effort basis without formal approval

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: When residual risk exceeds risk appetite and available controls are insufficient, the organization faces a situation that requires a formal governance decision — not a technical one. The risk committee or board must decide whether to accept the exceedance temporarily (with documentation), increase the budget, reduce scope, or transfer the risk. ISO 31000 and ISACA guidance are explicit that risk appetite exceedances must be escalated to the level of authority that set the appetite in the first place.
- Why A is incorrect: Informal acceptance is not acceptable when residual risk exceeds the stated risk appetite. Informal acceptance creates an undocumented liability — if the risk materializes, the organization cannot demonstrate that a deliberate, authorized decision was made. It also violates the governance principle that risk acceptance must be documented and authorized.
- Why C is incorrect: Removing risks from the register because they are inconvenient to address is a critical governance failure. Risk registers must accurately reflect the organization's actual risk posture. Removing entries creates an inaccurate record and hides the exceedance from oversight.
- Why D is incorrect: Implementing controls without formal approval bypasses authorization processes and may create new risks (e.g., system instability, compliance gaps) without corresponding governance oversight. Best-effort technical actions without approved scope and budget are not a substitute for formal risk governance decisions.

---

### Question 14

A risk analyst is documenting the treatment decisions for the organization's top-ten risks. For each risk, the analyst must record the treatment option selected, the rationale, the residual risk level after treatment, the risk owner, and the scheduled review date. This documentation is most commonly stored in:

- A) The information security policy
- B) The system security plan (SSP)
- C) The risk register
- D) The business impact analysis report

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: The risk register is the authoritative governance document that tracks identified risks, their assessed likelihood and impact, treatment decisions, owners, residual risk levels, and review schedules. NIST SP 800-39, ISO 31000, and ISACA frameworks all identify the risk register as the primary artifact for recording and tracking risk treatment decisions. It serves as the audit trail for the organization's risk management program.
- Why A is incorrect: Information security policies establish rules, requirements, and standards for behavior and control implementation. They do not track individual risk treatment decisions, owners, or residual risk levels for specific identified risks.
- Why B is incorrect: The system security plan documents the security controls implemented in a specific information system and their implementation status under the NIST RMF. It is system-specific and does not serve as the enterprise-wide risk treatment tracking document.
- Why D is incorrect: The business impact analysis report documents the operational consequences of disrupting specific business functions and establishes MTD, RTO, and RPO targets. It is an input to continuity and recovery planning, not the document that records risk treatment decisions and residual risk levels.

---

### Question 15

The board of directors has approved an information security risk appetite statement that defines "high" risk as any risk with an ALE exceeding $500,000. A risk assessment reveals that an unpatched critical vulnerability in a revenue-generating application has an estimated ALE of $720,000. The security team patches the vulnerability, reducing the estimated ALE to $180,000. Which statement best describes the governance outcome?

- A) The risk has been eliminated and no further governance action is required
- B) The residual risk now falls within the stated risk appetite, satisfying the governance requirement
- C) The risk must still be escalated to the board because a critical vulnerability was identified
- D) The ALE reduction must be verified by an external auditor before the risk can be closed

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Risk appetite is the threshold above which risks require escalation or additional treatment. By reducing the ALE from $720,000 to $180,000, the treatment action has brought the residual risk below the board-approved $500,000 threshold. The risk now falls within appetite, which means the organization can accept the residual risk without further escalation. The treatment outcome should be documented in the risk register, the residual risk recorded, and the entry scheduled for periodic review.
- Why A is incorrect: The risk has not been eliminated — patching a vulnerability reduces likelihood and/or impact but does not guarantee that the same or a similar vulnerability will never reappear. Residual risk remains. Describing the outcome as elimination is technically inaccurate and creates a false sense of security.
- Why C is incorrect: The risk appetite threshold, not the label of the vulnerability, determines whether escalation is required. The board delegated escalation authority to risks above $500,000 ALE. With residual ALE at $180,000, the decision authority appropriately rests with the operational security team — escalation to the board is not required unless internal policy specifies otherwise.
- Why D is incorrect: External auditor verification is not a standard requirement for closing or accepting a treated risk in most risk management frameworks. While external assessors play a role in control effectiveness assessments (e.g., NIST RMF Assess step), routine risk treatment closure does not require external audit sign-off. The risk owner and documentation in the risk register are sufficient for governance purposes.

---

### Question 16

A security manager is reviewing the organization's cyber liability insurance policy as part of the annual risk treatment review. The policy covers first-party losses from ransomware attacks up to $5 million but excludes losses resulting from failure to maintain basic security hygiene controls (e.g., unpatched systems, no MFA on administrative accounts). A ransomware incident occurs, and the insurer denies the claim because administrative accounts lacked MFA. Which risk treatment lesson does this scenario most directly illustrate?

- A) Cyber insurance is an unreliable risk treatment option and should be replaced with additional technical controls
- B) Risk transfer through insurance does not eliminate the organization's responsibility to maintain the controls required to keep the transfer effective — failure to satisfy policy conditions converts a transfer into an unintended acceptance
- C) The insurance policy should have been reviewed by the legal team before purchase to identify exclusion clauses
- D) MFA is a preventive control that eliminates ransomware risk and should always be implemented before purchasing insurance

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: Risk transfer via insurance is conditional — the insurer's obligation to pay depends on the insured maintaining the baseline controls and conditions specified in the policy. When an organization fails to satisfy those conditions, the financial loss reverts to the organization as unintended risk acceptance. This scenario illustrates that risk transfer must be actively maintained, not treated as a permanent transfer that requires no ongoing management.
- Why A is incorrect: Cyber insurance remains a valid risk treatment option for many organizations. The failure here was not the tool itself but the organization's failure to maintain the conditions required for the transfer to remain effective. Discarding insurance entirely because of a preventable claim denial is an overreaction that misidentifies the root cause.
- Why C is incorrect: Legal review of policy terms is a sound procurement practice, but the lesson in this scenario is about ongoing control maintenance, not about the initial purchase decision. Even if legal had flagged the MFA exclusion at purchase, the organization still failed to implement MFA — the governance failure is operational, not contractual.
- Why D is incorrect: MFA significantly reduces the attack surface for credential-based ransomware deployment but does not eliminate ransomware risk entirely. Framing MFA as an eliminator of ransomware risk overstates its effect and mischaracterizes risk treatment. MFA is a mitigation control that reduces likelihood; it does not constitute risk avoidance.

---

### Question 17

An organization's security team identifies a risk that falls into the risk avoidance treatment category. The business unit that owns the process generating the risk objects, arguing that avoiding the activity would eliminate a $3.2 million annual revenue stream. The security team and business unit cannot reach agreement. Who should make the final risk treatment decision, and why?

- A) The security team, because information security risk treatment decisions are within the CISO's authority
- B) The business unit owner, because revenue-generating activities take precedence over security concerns
- C) The appropriate governance authority — typically the risk committee, executive sponsor, or board — because risk avoidance decisions that eliminate significant revenue streams are business decisions with strategic consequences that exceed the security team's or business unit's individual authority
- D) An external auditor, because disputed risk decisions require independent resolution

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Risk treatment decisions with material business consequences — particularly risk avoidance, which eliminates an activity entirely — are governance decisions, not security or business unit decisions in isolation. The CISO provides risk analysis and recommendations; the business unit provides business context; but the decision to forgo $3.2 million in revenue belongs to the level of authority empowered to make strategic business trade-offs. This is a core CISM governance principle: risk acceptance and avoidance decisions at significant thresholds must be escalated to the appropriate governance authority.
- Why A is incorrect: The CISO's authority covers security program direction and risk analysis, not unilateral decisions to eliminate business activities. Risk avoidance decisions of this magnitude require business leadership involvement and governance-level approval.
- Why B is incorrect: Revenue generation does not automatically override security risk concerns — especially if the risk threatens regulatory compliance, customer data, or the organization's license to operate. Business unit owners do not have unilateral authority to override risk governance processes.
- Why D is incorrect: External auditors assess whether governance processes are followed; they do not make operational or strategic risk treatment decisions for the organization. Referring a disputed internal governance decision to an external auditor is not a recognized risk treatment escalation path.

---

### Question 18

A security analyst classifies the following controls implemented in a cloud environment: (1) automated alerts when privileged account activity occurs outside business hours; (2) quarterly access reviews requiring managers to certify their team's permissions; (3) automatic session termination after 15 minutes of inactivity. Which classification correctly identifies the functional type and implementation category for each control?

- A) (1) Detective/Technical; (2) Preventive/Administrative; (3) Preventive/Technical
- B) (1) Detective/Technical; (2) Detective/Administrative; (3) Corrective/Technical
- C) (1) Preventive/Technical; (2) Detective/Administrative; (3) Deterrent/Technical
- D) (1) Corrective/Technical; (2) Preventive/Administrative; (3) Detective/Technical

**Correct Answer:** A

**Distractor Analysis:**

- Why A is correct: Control (1) — automated alerts on anomalous privileged activity — identifies security events after they occur without stopping them; it is Detective and implemented by automated software (Technical). Control (2) — access certification reviews — is a human-managed process (Administrative) that prevents accumulation of excessive permissions by periodically removing unneeded access; it is Preventive. Control (3) — automatic session termination — proactively ends sessions before they can be hijacked; it is Preventive and enforced by software (Technical).
- Why B is incorrect: Classifying control (2) as Detective is imprecise. Access reviews do detect inappropriate access that may have accumulated, but their primary function is to prevent ongoing unauthorized access by certifying and removing it — making Preventive a more accurate primary classification. Classifying control (3) as Corrective is incorrect; session termination stops an active session to prevent harm, which is Preventive, not a recovery action after an incident has occurred.
- Why C is incorrect: Classifying control (1) as Preventive is incorrect — an alert does not stop the activity; it identifies it after the fact (Detective). Classifying control (3) as Deterrent is incorrect; automatic termination is a software-enforced action, not a warning or psychological discouragement mechanism.
- Why D is incorrect: Classifying control (1) as Corrective is incorrect — corrective controls restore normal operations after an incident. An alert notifying security of anomalous activity is a detection action. Classifying control (3) as Detective is incorrect; session termination is an automated enforcement action (Preventive), not a monitoring or identification activity.

---

### Question 19

A company purchases a cyber liability insurance policy with a $2 million limit and a $100,000 deductible to cover data breach costs. Separately, the security team implements encryption, access controls, and network segmentation that collectively reduce the estimated breach probability by 60%. Which statement most accurately describes the combined risk treatment strategy?

- A) The organization has chosen risk transfer as its sole treatment strategy
- B) The organization has avoided the risk by implementing technical controls
- C) The organization has applied a combined treatment strategy: risk mitigation (technical controls reducing likelihood) and risk transfer (insurance covering residual financial exposure above the deductible)
- D) The insurance policy constitutes risk acceptance because the deductible represents an amount the organization is willing to absorb

**Correct Answer:** C

**Distractor Analysis:**

- Why C is correct: Risk treatment strategies are not mutually exclusive. The technical controls (encryption, access controls, segmentation) represent risk mitigation — they reduce the probability and potential impact of a breach. The insurance policy transfers the residual financial exposure beyond the deductible to the insurer. Using both simultaneously is a standard, recognized combined treatment approach in which mitigation reduces the likelihood and impact, and transfer handles the financial consequences of residual events that occur despite mitigation.
- Why A is incorrect: Describing the strategy as solely risk transfer ignores the substantial mitigation investment in technical controls. The organization is actively reducing risk through controls, not only transferring the residual financial exposure.
- Why B is incorrect: Risk avoidance requires eliminating the activity that generates the risk. The organization continues to operate its data systems — it has reduced risk through controls, not avoided the risk by stopping the activity.
- Why D is incorrect: The deductible represents the retained portion of a transferred risk — it is a cost condition of the transfer mechanism, not a separate acceptance decision. The overall treatment strategy for the financial exposure above the deductible is transfer; the deductible is simply the cost of accessing that transfer.

---

### Question 20

An organization's risk register contains 45 entries. After completing a control implementation cycle, the security team recalculates residual risk for each entry. For 38 entries, residual risk now falls within the board-approved risk appetite. For 7 entries, residual risk remains above appetite despite available controls having been applied. The CISO documents all residual risk levels and presents the 7 exceedances to the risk committee. The risk committee formally reviews each entry, acknowledges the residual exposure, and signs acceptance records for all 7. Which statement best evaluates this outcome from a risk governance perspective?

- A) This is a governance failure because the risk committee should have required additional controls rather than accepting residual risk above appetite
- B) This is appropriate formal risk acceptance governance — the organization has exhausted available controls, escalated the exceedances to the authority that set the appetite, and obtained documented authorization, which satisfies the governance requirement
- C) The risk committee's acceptance decisions are invalid because risk appetite exceedances can only be accepted by the board of directors, not a committee
- D) Documenting 7 accepted risks above appetite in the risk register creates audit liability and the entries should be removed after the acceptance decision

**Correct Answer:** B

**Distractor Analysis:**

- Why B is correct: This scenario describes exemplary risk acceptance governance. The treatment cycle was completed, residual risk was honestly assessed, exceedances were identified, the appropriate governance authority (risk committee) was engaged, the exposures were formally reviewed, and acceptance decisions were documented. ISO 31000, NIST SP 800-39, and ISACA frameworks all recognize that residual risk above appetite can be formally accepted when treatment options are exhausted — provided the acceptance is authorized, documented, and subject to periodic review. The documented acceptance records satisfy the governance requirement.
- Why A is incorrect: Formal risk acceptance of residual risk above appetite — after available controls are applied — is a legitimate and necessary governance mechanism. Governance frameworks do not require organizations to achieve zero residual risk or to endlessly pursue additional controls. The risk committee exists precisely to make these authorized acceptance decisions.
- Why C is incorrect: Whether the risk committee or the full board accepts residual risk above appetite depends on the organization's governance charter and delegated authority structure. Many organizations explicitly delegate residual risk acceptance authority to a risk committee for entries below a specific threshold. The scenario does not indicate that committee authority was exceeded.
- Why D is incorrect: Removing documented risk entries from the register after a formal acceptance decision is a governance failure — the opposite of sound practice. Risk registers must retain records of accepted risks, including the rationale, the acceptance authority, and the scheduled review date. These records are essential for audit trails, regulatory demonstrations, and future risk management decision-making.
