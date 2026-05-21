# Quiz: Module 10 - Incident Response – Containment, Eradication, Recovery
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
What is the primary focus of the General Data Protection Regulation (GDPR)?
*   A) Securing financial reporting systems for publicly traded companies in the European Union
*   B) Protecting the privacy rights and personal data of European Union residents, regardless of where the processing organization is located
*   C) Regulating cybersecurity standards for critical infrastructure operators in EU member states
*   D) Setting minimum software security development standards for applications sold within the EU
*   **Correct Answer:** B) GDPR grants EU residents rights over their personal data and applies to any organization worldwide that processes personal data of EU residents.
*   **Distractor Analysis:**
    *   *Why B is correct:* GDPR's scope is defined by the data subject's location, not the organization's location — any company processing EU residents' data must comply.
    *   *Why A is incorrect:* SOX covers financial reporting systems; GDPR does not address financial reporting requirements.
    *   *Why C is incorrect:* The EU NIS Directive (and NIS2) addresses critical infrastructure cybersecurity; GDPR focuses specifically on personal data privacy.
    *   *Why D is incorrect:* Software security development standards are not within GDPR's scope; GDPR addresses personal data processing practices.

---

**Question 2**
Which of the following most accurately describes **Personally Identifiable Information (PII)**?
*   A) All data stored within an organization's databases, regardless of its content or sensitivity
*   B) Information that is exclusively contained in government-issued identity documents such as passports
*   C) Any data that can identify, locate, or contact a specific individual, either alone or in combination with other information
*   D) Encrypted data that has been anonymized using approved cryptographic techniques
*   **Correct Answer:** C) PII is broadly defined as data that enables the identification of a specific individual — it includes names, addresses, SSNs, email addresses, IP addresses, and combinations of data that together enable identification.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Not all organizational data is PII; confidential business information, public data, and anonymized data are not PII.
    *   *Why B is incorrect:* PII is not limited to government documents; it includes any identifying data regardless of source.
    *   *Why C is correct:* This captures both direct identifiers (SSN, name) and indirect identifiers (combinations of data) that regulatory definitions of PII encompass.
    *   *Why D is incorrect:* Properly anonymized data no longer constitutes PII because it cannot be re-linked to an individual; encryption alone does not anonymize data.

---

**Question 3**
A U.S.-based e-commerce company processes orders from customers in Germany, France, and Spain. Which privacy regulation most directly governs the company's handling of those customers' personal data?
*   A) CCPA (California Consumer Privacy Act)
*   B) HIPAA (Health Insurance Portability and Accountability Act)
*   C) GDPR (General Data Protection Regulation)
*   D) GLBA (Gramm-Leach-Bliley Act)
*   **Correct Answer:** C) GDPR applies based on the location of the data subjects — EU residents in Germany, France, and Spain are protected by GDPR regardless of where the processing organization is headquartered.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CCPA applies to California residents' data; it does not govern EU residents' personal data.
    *   *Why B is incorrect:* HIPAA governs protected health information in the healthcare industry; it does not apply to e-commerce customer purchase data.
    *   *Why C is correct:* GDPR's extraterritorial reach (Article 3) explicitly covers data processing of EU residents by organizations outside the EU.
    *   *Why D is incorrect:* GLBA governs U.S. financial institutions' handling of customer financial information; it does not apply to EU residents' data.

---

**Question 4**
Under GDPR, within how many hours of discovering a personal data breach must an organization notify the relevant supervisory authority?
*   A) 24 hours
*   B) 48 hours
*   C) 72 hours
*   D) 7 days
*   **Correct Answer:** C) GDPR Article 33 requires notification to the supervisory authority within 72 hours of the organization becoming aware of the breach, where feasible.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A 24-hour timeline is not the GDPR standard; 72 hours is the requirement.
    *   *Why B is incorrect:* 48 hours is a common distractor; the correct GDPR requirement is 72 hours.
    *   *Why C is correct:* This is the explicit GDPR requirement — 72 hours to the supervisory authority, with notification to affected individuals when the breach is likely to result in high risk to their rights and freedoms.
    *   *Why D is incorrect:* A 7-day timeline would violate GDPR's notification requirement; this matches some older, less stringent breach laws but not GDPR.

---

**Question 5**
An EU resident submits a request to a company demanding permanent deletion of all personal data the company holds about them, citing GDPR Article 17. The company's marketing team argues the data is still needed for targeting future campaigns. Under GDPR, which response is most appropriate?
*   A) Retain the data indefinitely since legitimate business interest overrides all erasure requests
*   B) Delete the data within the required timeframe unless a specific legal basis (legal obligation, legitimate interest override, or ongoing legal proceedings) exists to retain it
*   C) Anonymize the data and continue using it for marketing, satisfying the erasure request
*   D) Transfer the data to a third-party processor to remove it from the company's own systems without deleting it
*   **Correct Answer:** B) GDPR's right to erasure is not absolute — organizations must delete data unless a specific enumerated exception applies; "we want to keep using it for marketing" is not a valid exception once consent is withdrawn.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* "Legitimate business interest" does not automatically override a valid erasure request when consent was the legal basis for processing; GDPR provides specific, limited exceptions.
    *   *Why B is correct:* The right to erasure requires deletion unless one of GDPR Article 17(3)'s specific exceptions applies — continued marketing use is not an exception after an erasure request.
    *   *Why C is incorrect:* True anonymization (which severs all re-identification possibility) would technically satisfy the request, but incomplete anonymization that preserves targeting ability does not.
    *   *Why D is incorrect:* Transferring data to a processor does not constitute deletion and would violate the erasure request; the data controller remains responsible for data processing by its processors.
