# Quiz: Module 11 - Business Continuity and Disaster Recovery Planning
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
Which standard is mandatory for any organization processing, storing, or transmitting credit card information?
*   A) ISO/IEC 27001
*   B) PCI DSS
*   C) NIST SP 800-53
*   D) SOC 2
*   **Correct Answer:** B) PCI DSS is contractually required by major card brands (Visa, Mastercard, Amex, Discover, JCB) for any entity in the cardholder data environment.
*   **Distractor Analysis:**
    *   *Why B is correct:* PCI DSS compliance is not optional for entities that handle cardholder data — non-compliance can result in fines, card processing suspension, and breach liability.
    *   *Why A is incorrect:* ISO/IEC 27001 is a voluntary international standard; organizations may choose to pursue it but are not compelled to do so.
    *   *Why C is incorrect:* NIST SP 800-53 is a control catalog primarily used by U.S. federal agencies; it is not mandatory for private sector payment card entities.
    *   *Why D is incorrect:* SOC 2 is a voluntary assurance report used for service organizations; it is not a payment card industry requirement.

---

**Question 2**
Which of the following most accurately describes **PCI DSS** and its compliance obligation?
*   A) A voluntary international standard that organizations can certify against to demonstrate information security management system maturity
*   B) A U.S. federal law requiring organizations to report payment card breaches to the Federal Trade Commission within 30 days
*   C) A set of security requirements established by card brands that any organization processing, storing, or transmitting cardholder data must comply with to maintain card acceptance privileges
*   D) A technical specification defining approved encryption algorithms for protecting payment card transactions in transit
*   **Correct Answer:** C) PCI DSS defines the mandatory security requirements for all entities in the payment card ecosystem, enforced through card brand contractual agreements.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes ISO/IEC 27001 — voluntary, with third-party certification. PCI DSS is mandatory for cardholder data handlers.
    *   *Why B is incorrect:* PCI DSS is not a U.S. federal law; it is an industry standard. There is no 30-day FTC reporting requirement under PCI DSS.
    *   *Why C is correct:* PCI DSS is an industry-mandated standard enforced through card brand merchant agreements — organizations must comply or lose card processing privileges.
    *   *Why D is incorrect:* PCI DSS covers a broad set of 12 security requirements beyond encryption; it is not a narrow technical specification for encryption algorithms.

---

**Question 3**
A retail company achieves ISO/IEC 27001 certification for its headquarters operations. A security incident then occurs at a regional warehouse that was not included in the certification scope. What is the most accurate statement about the impact on the company's ISO 27001 status?
*   A) The company immediately loses its ISO 27001 certification for all operations
*   B) The incident has no effect on certification since the warehouse is outside the certified scope
*   C) The company must expand its ISMS scope to include all locations before the next audit cycle
*   D) The certification becomes invalid until the incident is fully resolved
*   **Correct Answer:** B) ISO 27001 certification applies only to the defined ISMS scope; incidents outside the scope do not automatically invalidate the certification, though they may prompt a scope review.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Certification is scope-specific; events outside the certified scope do not automatically revoke certification.
    *   *Why B is correct:* This reflects how ISO 27001 scoping works — the certification covers only the operations explicitly included in the ISMS scope definition.
    *   *Why C is incorrect:* Scope expansion is a strategic decision; it is not automatically required following an out-of-scope incident, though it may be advisable.
    *   *Why D is incorrect:* Certification is not suspended pending incident resolution unless the incident reveals that the ISMS itself (within scope) is deficient.

---

**Question 4**
An organization that processes credit card transactions discovers a breach of cardholder data. Under PCI DSS, what is the first required action?
*   A) Obtain a new Qualified Security Assessor (QSA) for an emergency recertification audit
*   B) Immediately delete all cardholder data from affected systems to prevent further compromise
*   C) Contain the breach, preserve evidence, and notify the relevant card brands and acquiring bank immediately
*   D) Publish a public disclosure statement on the company website within 24 hours of discovery
*   **Correct Answer:** C) PCI DSS Requirement 12.10 mandates an incident response plan that includes immediate containment and notification to card brands and the acquiring bank upon breach discovery.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Emergency QSA recertification is not a breach response step; containment and notification come first.
    *   *Why B is incorrect:* Deleting data before notification and forensic investigation could destroy evidence required for the breach investigation.
    *   *Why C is correct:* PCI DSS breach response requirements include immediate containment, evidence preservation, and notification to payment brands and acquirer.
    *   *Why D is incorrect:* Public disclosure timelines are governed by state breach laws, not PCI DSS; PCI DSS requires notification to card brands, not immediate public disclosure.

---

**Question 5**
An organization is deciding whether to pursue ISO/IEC 27001 certification or focus solely on PCI DSS compliance. Which statement best captures the strategic value of ISO 27001 for an organization that already complies with PCI DSS?
*   A) ISO 27001 replaces the need for PCI DSS compliance once the certification is obtained
*   B) ISO 27001 provides a comprehensive ISMS framework that strengthens the overall security program beyond cardholder data, demonstrating enterprise-wide security maturity to customers and partners
*   C) ISO 27001 is only relevant for organizations outside the United States where PCI DSS does not apply
*   D) ISO 27001 certification automatically satisfies all PCI DSS requirements, eliminating the need for separate PCI assessments
*   **Correct Answer:** B) ISO 27001 addresses the entire ISMS, while PCI DSS is scoped to cardholder data environments — the two frameworks complement each other and serve different assurance purposes.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ISO 27001 does not replace PCI DSS; they have different scopes and different enforcement mechanisms.
    *   *Why B is correct:* ISO 27001 provides a broader governance framework that signals enterprise security maturity; it complements but does not replace PCI DSS.
    *   *Why C is incorrect:* PCI DSS applies globally wherever cards are processed; ISO 27001 is also globally applicable. Neither is geographically restricted.
    *   *Why D is incorrect:* ISO 27001 certification does not satisfy PCI DSS; they have different control sets, scoping rules, and assessment processes.
