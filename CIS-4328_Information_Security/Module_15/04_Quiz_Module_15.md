# Quiz: Module 15 - Governance, Compliance, and Privacy
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
An organization's security team is drafting a document that states: "All endpoints connecting to the corporate network must have endpoint detection and response (EDR) software installed, updated to the latest signature version, and actively reporting to the central management console." Which type of security governance document is this?
A) Security Policy
B) Security Standard
C) Security Guideline
D) Security Procedure
*   **Correct Answer:** B) Security Standard
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A security policy is a high-level statement of management intent and organizational objectives — for example, "All endpoints must be protected against malware." Policies do not specify the particular technology, version requirements, or configuration details. The document described specifies mandatory technical requirements, which is the definition of a standard.
    *   *Why C is incorrect:* A security guideline provides recommended best practices that are not mandatory — organizations may choose to follow them at their discretion. The document described uses mandatory language ("must") and specifies precise requirements, which disqualifies it as a guideline.
    *   *Why D is incorrect:* A security procedure is a step-by-step instruction set for carrying out a specific task (e.g., "How to enroll a new endpoint in the EDR console"). The document described sets a mandatory requirement, not a sequence of operational steps.

---

---

**Question 2**
A U.S.-based e-commerce company discovers that approximately 12% of its customer base consists of residents of European Union member states. The company collects names, email addresses, purchase history, and behavioral tracking data from all customers. A legal advisor informs the company it must comply with a specific privacy regulation due to the EU customer data. Which regulation applies?
A) HIPAA (Health Insurance Portability and Accountability Act)
B) PCI-DSS (Payment Card Industry Data Security Standard)
C) GDPR (General Data Protection Regulation)
D) FERPA (Family Educational Rights and Privacy Act)
*   **Correct Answer:** C) GDPR (General Data Protection Regulation)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* HIPAA regulates the privacy and security of protected health information (PHI) held by covered entities (healthcare providers, insurers) and their business associates — it does not apply to general e-commerce customer data such as purchase history and email addresses.
    *   *Why B is incorrect:* PCI-DSS applies to any organization that processes, stores, or transmits payment card data — it governs cardholder data security, not the broader category of personal data including behavioral tracking and purchase history collected from EU residents.
    *   *Why D is incorrect:* FERPA (Family Educational Rights and Privacy Act) protects the educational records of students at institutions receiving federal funding in the U.S. — it does not apply to commercial e-commerce customer data.

---

---

**Question 3**
A healthcare organization classifies its data into four levels: Public, Internal, Confidential, and Restricted. Patient medical records including diagnoses, treatment plans, and medication lists are classified as Restricted. An employee requests access to Restricted patient records for a research project unrelated to the patient's care. The privacy officer denies the request, citing a specific privacy principle. Which principle is the privacy officer applying?
A) Data minimization — the organization should not have collected the patient records in the first place.
B) Purpose limitation — personal data may only be used for the specific purpose for which it was originally collected.
C) Data sovereignty — the records are subject to the laws of the country where the servers are located.
D) Right to erasure — the patient has requested that their records be deleted.
*   **Correct Answer:** B) Purpose limitation — personal data may only be used for the specific purpose for which it was originally collected.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Data minimization addresses the amount of data collected — it requires collecting only the minimum data necessary for the stated purpose. The records were legitimately collected for patient care, so data minimization is not the applicable principle here.
    *   *Why C is incorrect:* Data sovereignty relates to which country's laws govern data stored in a specific jurisdiction — it does not determine what purposes an employee within the same organization may use patient data for.
    *   *Why D is incorrect:* The right to erasure (GDPR "right to be forgotten") is a data subject right allowing individuals to request deletion of their personal data under certain conditions — it is initiated by the patient, not the privacy officer responding to an internal access request.

---

**Question 4**
A financial services company that processes credit card payments for customers undergoes an annual assessment to validate its security controls. The assessment is conducted by a qualified security assessor (QSA) who is independent of the organization and evaluates compliance against a specific set of technical and operational requirements including network segmentation, access controls, encryption of cardholder data, and vulnerability scanning. Which compliance framework governs this assessment?
A) NIST Cybersecurity Framework (CSF)
B) ISO/IEC 27001
C) PCI-DSS
D) SOC 2 Type II
*   **Correct Answer:** C) PCI-DSS
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The NIST Cybersecurity Framework is a voluntary framework for managing cybersecurity risk, organized around five functions (Identify, Protect, Detect, Respond, Recover). It does not mandate specific assessments by qualified security assessors for payment card processing organizations.
    *   *Why B is incorrect:* ISO/IEC 27001 is an international standard for information security management systems (ISMS) that can apply to any organization — it does not specifically address cardholder data protection requirements or require a qualified security assessor (QSA) for certification.
    *   *Why D is incorrect:* SOC 2 Type II is an auditing framework developed by the AICPA that evaluates a service organization's controls related to security, availability, processing integrity, confidentiality, and privacy over a defined period — it is not the mandatory standard for credit card processing security and does not use the QSA designation.

---

**Question 5**
A company's security team discovers that a software vendor with access to their development environment was compromised. The attackers used the vendor's legitimate credentials to access the company's source code repository and insert malicious code into a software update, which was then distributed to thousands of end customers. Which type of attack does this scenario describe, and which third-party risk control would have most directly reduced the likelihood of this breach?
A) This is a phishing attack; implementing email filtering would have prevented it.
B) This is a supply chain attack; enforcing contractual security requirements and conducting vendor security assessments would have reduced the risk.
C) This is an insider threat; implementing user behavior analytics on internal employees would have detected it.
D) This is a watering hole attack; deploying a web application firewall would have blocked the initial compromise.
*   **Correct Answer:** B) This is a supply chain attack; enforcing contractual security requirements and conducting vendor security assessments would have reduced the risk.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A phishing attack uses deceptive messages to trick users into revealing credentials or clicking malicious links — the scenario describes a vendor's systems being compromised, not an email-based deception. The attacker reached the target through a trusted third-party channel, not through phishing the target directly.
    *   *Why C is incorrect:* An insider threat involves a current or former employee intentionally misusing their access — the attacker here was an external actor who compromised an external vendor, not an insider. User behavior analytics monitoring internal employees would not have detected a compromise of an external vendor's infrastructure.
    *   *Why D is incorrect:* A watering hole attack compromises a website frequently visited by the target's employees to deliver malware — the scenario describes an attacker using compromised vendor credentials to directly access a development environment and tamper with software, which is the definition of a supply chain attack.
