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
