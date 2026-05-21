# Quiz: Module 06 - Information Security Policies and Standards
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
Which risk treatment option involves completely eliminating the threat by stopping the business activity that creates the risk?
*   A) Mitigation
*   B) Avoidance
*   C) Acceptance
*   D) Transfer
*   **Correct Answer:** B) Risk avoidance eliminates the risk entirely by discontinuing the activity that creates exposure (e.g., not storing payment card data to avoid PCI DSS scope).
*   **Distractor Analysis:**
    *   *Why B is correct:* Avoidance removes the risk at its source by eliminating the risky activity, unlike mitigation which keeps the activity and adds controls.
    *   *Why A is incorrect:* Mitigation reduces risk likelihood or impact through controls but keeps the underlying activity running.
    *   *Why C is incorrect:* Acceptance acknowledges the risk and tolerates it within defined limits without eliminating it.
    *   *Why D is incorrect:* Transfer shifts financial consequences to a third party (insurance, contracts) but does not eliminate the threat.

---

**Question 2**
Which of the following most accurately describes **risk avoidance** as a treatment strategy?
*   A) Purchasing cyber liability insurance to cover the financial cost of a data breach event
*   B) Implementing multi-factor authentication to reduce the likelihood of unauthorized account access
*   C) Formally documenting that a known risk is within the organization's tolerance and requires no additional controls
*   D) Deciding not to pursue a business activity or discontinuing a process because its inherent risk exceeds the organization's acceptable threshold
*   **Correct Answer:** D) Risk avoidance eliminates risk by removing the activity that generates it — the most complete but often least operationally flexible treatment option.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Insurance is risk transfer, not avoidance — it shifts financial consequences but keeps the activity.
    *   *Why B is incorrect:* Implementing MFA is risk mitigation — the activity continues with added controls.
    *   *Why C is incorrect:* Formally accepting a risk within tolerance is risk acceptance, not avoidance.
    *   *Why D is correct:* This precisely captures risk avoidance — the organization eliminates the risk source by not engaging in the risky activity.

---

**Question 3**
A company stores customer credit card numbers to enable recurring billing. A risk assessment determines the storage creates unacceptable PCI DSS compliance risk. The cost to implement required tokenization is prohibitive. Which risk treatment option is most appropriate?
*   A) Accept the risk and document it in the risk register
*   B) Transfer the risk by purchasing additional cyber insurance
*   C) Avoid the risk by eliminating local card storage and using a tokenization service provider
*   D) Mitigate the risk by adding a secondary firewall around the card data environment
*   **Correct Answer:** C) Using a tokenization provider eliminates the organization's direct storage of card data, removing the risk at its source while preserving the business capability.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Accepting a high PCI DSS compliance risk exposes the organization to regulatory penalties and data breach liability — it exceeds acceptable tolerance.
    *   *Why B is incorrect:* Insurance does not eliminate the compliance obligation or prevent a breach; it only helps recover financially afterward.
    *   *Why C is correct:* Outsourcing card storage to a qualified tokenization provider is a form of risk avoidance — the organization no longer holds the risky data.
    *   *Why D is incorrect:* Adding a firewall is mitigation that reduces but does not eliminate the storage risk; it also does not address the root compliance gap.

---

**Question 4**
After implementing controls to mitigate a risk, a security manager determines that some residual risk remains. Who is responsible for formally accepting this residual risk?
*   A) The IT security team that designed and implemented the controls
*   B) The external auditor who reviewed the risk assessment
*   C) Senior management or the designated risk owner with appropriate authority
*   D) The vendor who supplied the security controls used in mitigation
*   **Correct Answer:** C) Residual risk acceptance is a governance decision requiring appropriate business authority — it cannot be delegated to IT staff or auditors.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IT security staff implement controls; they do not have the organizational authority to accept business risk on behalf of the enterprise.
    *   *Why B is incorrect:* External auditors assess and report; they do not make risk acceptance decisions for the organization.
    *   *Why C is correct:* CISM and ISO 27005 establish that risk acceptance must be made by management with appropriate authority and accountability.
    *   *Why D is incorrect:* Vendors supply technology; they bear no accountability for the organization's business risk decisions.

---

**Question 5**
An organization's risk manager is evaluating a low-likelihood, low-impact risk involving minor website content errors. The cost of mitigation controls exceeds the potential loss by a factor of ten. Which treatment option best aligns with sound risk management principles?
*   A) Avoid the risk by shutting down the public website until the content errors are corrected
*   B) Transfer the risk to a third-party vendor through a service-level agreement
*   C) Accept the risk, document it in the risk register, and monitor it during periodic reviews
*   D) Immediately escalate the risk to the board of directors for emergency resource allocation
*   **Correct Answer:** C) When mitigation cost significantly exceeds potential impact and the risk falls within the organization's tolerance, risk acceptance is the cost-effective, governance-appropriate response.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Shutting down the website to avoid a minor content error risk is disproportionate and causes more business harm than the risk itself.
    *   *Why B is incorrect:* Transferring a low-impact risk through an SLA creates unnecessary administrative overhead and cost for a risk that is within tolerance.
    *   *Why C is correct:* Risk acceptance is appropriate for risks within tolerance where control costs exceed expected losses; documentation and monitoring ensure accountability.
    *   *Why D is incorrect:* Board escalation is reserved for high-impact risks requiring executive decision-making; a minor low-likelihood risk does not warrant emergency escalation.
