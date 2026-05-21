# Quiz: Module 14 - Risk Management and Business Continuity
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A risk analyst is evaluating the threat of a ransomware attack against a file server valued at $500,000. The analyst estimates that a successful attack would render 40% of the server's value unrecoverable. Historical data suggests ransomware attacks of this type occur approximately twice per year at similar organizations. What is the Annualized Loss Expectancy (ALE) for this threat?
A) $200,000
B) $400,000
C) $100,000
D) $500,000
*   **Correct Answer:** B) $400,000
*   **Distractor Analysis:**
    *   *Why A is incorrect:* $200,000 represents only the Single Loss Expectancy (SLE = $500,000 × 0.40). The ALE requires multiplying the SLE by the Annualized Rate of Occurrence (ARO): ALE = $200,000 × 2 = $400,000.
    *   *Why C is incorrect:* $100,000 does not correspond to any correct step in the ALE calculation. It may result from incorrectly applying the exposure factor to the ARO rather than to the asset value first.
    *   *Why D is incorrect:* $500,000 is the full asset value with no adjustment for the exposure factor or frequency. The ALE accounts for the percentage of value lost per event and the expected frequency of events — it is not simply the total asset value.

---

---

**Question 2**
A company's security team has identified that their customer-facing web portal uses an end-of-life web framework with multiple known vulnerabilities. The vendor no longer provides patches. Replacing the framework requires a six-month development effort. As an interim measure, the team deploys a web application firewall (WAF) to filter known exploit patterns targeting the vulnerable framework. Which risk response strategy does the WAF deployment represent?
A) Risk Avoidance
B) Risk Transference
C) Risk Acceptance
D) Risk Mitigation
*   **Correct Answer:** D) Risk Mitigation
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Risk avoidance would mean taking the vulnerable web portal completely offline or discontinuing the service to eliminate the risk entirely — the organization is not doing that here; they are continuing to operate the portal while reducing the risk.
    *   *Why B is incorrect:* Risk transference shifts the financial impact of the risk to a third party (e.g., cyber insurance or a managed security service contract) — deploying an internal WAF is a technical control that reduces the organization's own exposure, not a transfer of liability.
    *   *Why C is incorrect:* Risk acceptance means acknowledging the risk and choosing to take no action — deploying a WAF is an active control implementation, which is the opposite of accepting the risk without response.

---

---

**Question 3**
A hospital's IT disaster recovery plan specifies that the Electronic Health Record (EHR) system must be restored within 2 hours of a failure, and no more than 15 minutes of patient data can be lost in the event of a disaster. Which statements correctly identify the Recovery Time Objective (RTO) and Recovery Point Objective (RPO)?
A) RTO = 15 minutes; RPO = 2 hours
B) RTO = 2 hours; RPO = 15 minutes
C) Both 2 hours and 15 minutes are RTO values; RPO is not specified.
D) RTO = 2 hours; RPO = 0 minutes, because patient safety requires no data loss.
*   **Correct Answer:** B) RTO = 2 hours; RPO = 15 minutes
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the definitions. RTO defines the maximum acceptable downtime (how long the system can be unavailable) — that is the 2-hour requirement. RPO defines the maximum acceptable data loss measured in time (how old the backup can be) — that is the 15-minute requirement.
    *   *Why C is incorrect:* The two values represent different recovery metrics, not two RTO values. The 15-minute requirement specifically describes data loss tolerance, which is the definition of RPO, not RTO.
    *   *Why D is incorrect:* The RPO is explicitly stated as 15 minutes — this is the maximum data loss the organization has defined as acceptable. Assuming RPO is zero is an interpretation not supported by the scenario and would require continuous synchronous replication, which is a significantly higher infrastructure investment.

---

**Question 4**
A retail company's disaster recovery plan calls for an alternate processing site that must be capable of resuming full e-commerce operations within 30 minutes of a primary site failure. The site must have all hardware pre-provisioned, all software pre-installed, and data continuously replicated from the production environment. Which disaster recovery site type meets this requirement?
A) Cold site
B) Warm site
C) Hot site
D) Mobile site
*   **Correct Answer:** C) Hot site
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A cold site provides only physical space, power, and connectivity — no hardware or software is pre-installed. Recovery requires procuring, shipping, and configuring equipment, which typically takes days to weeks. This cannot meet a 30-minute RTO.
    *   *Why B is incorrect:* A warm site has some hardware and connectivity pre-installed but requires data restoration and system configuration before operations can resume — recovery typically takes hours to days. A 30-minute RTO is beyond what a warm site can reliably deliver.
    *   *Why D is incorrect:* A mobile site is a portable unit (truck or trailer) with computing equipment that can be deployed to a disaster location — it is used when the organization needs temporary on-site processing capability, not for rapid failover with pre-replicated data.

---

**Question 5**
A small software company identifies a low-severity risk: the risk that a single employee's unencrypted USB drive could be lost, potentially exposing draft marketing materials that are not yet publicly released. The security team estimates the likelihood is low and the financial impact of exposure is minimal — the materials contain no PII, financial data, or trade secrets. After reviewing the cost of deploying USB encryption software company-wide ($8,000 annually) versus the estimated ALE ($500), the CISO decides to document the risk and take no further action. Which risk response strategy is the CISO applying?
A) Risk Mitigation
B) Risk Avoidance
C) Risk Transference
D) Risk Acceptance
*   **Correct Answer:** D) Risk Acceptance
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Risk mitigation involves implementing a control to reduce the likelihood or impact of the risk — deploying USB encryption would be mitigation. The CISO explicitly decided not to deploy the control.
    *   *Why B is incorrect:* Risk avoidance would mean prohibiting USB drives entirely to eliminate the risk — the company is not doing that. They are continuing the activity that creates the risk while choosing not to invest in controls.
    *   *Why C is incorrect:* Risk transference would involve purchasing insurance or contracting with a third party to absorb the financial impact — no such transfer mechanism is mentioned. The company is simply acknowledging and documenting the risk without action.
