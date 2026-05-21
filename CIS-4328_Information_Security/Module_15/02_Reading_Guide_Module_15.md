# Reading Guide: Module 15 - Governance, Compliance, and Privacy
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 15 – Governance, Compliance, and Privacy**! Security governance establishes the policies, frameworks, and accountability structures that guide an organization's security program. Compliance ensures the organization meets legal, regulatory, and contractual obligations. SY0-701 tests governance and compliance concepts in Domain 5 (Security Program Management and Oversight, 20%).

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Security Policy Types**: Organizations maintain a hierarchy of security documentation. Policies are high-level statements of management intent (e.g., "All sensitive data must be encrypted at rest"). Standards define specific mandatory requirements that implement the policy (e.g., "AES-256 must be used for data at rest encryption"). Guidelines are recommended but non-mandatory best practices. Procedures are step-by-step instructions for carrying out specific tasks. SY0-701 tests the correct document type for a given scenario.
*   **Compliance Frameworks and Regulations**: Key frameworks and regulations tested on SY0-701 include: NIST SP 800-53 (U.S. federal agency security controls); ISO/IEC 27001 (international ISMS standard); PCI-DSS (Payment Card Industry Data Security Standard — applies to any organization that processes credit cards); HIPAA (Health Insurance Portability and Accountability Act — protects patient health information in the U.S.); GDPR (General Data Protection Regulation — EU privacy law with global applicability for organizations handling EU resident data).
*   **Data Classification**: The process of categorizing data based on its sensitivity and the impact of unauthorized disclosure. Common classification levels: Public (no harm if disclosed) → Internal/Private → Confidential → Top Secret/Restricted. Data classification drives access controls, encryption requirements, handling procedures, and retention policies. SY0-701 tests classification in scenarios about who can access what data and what protections are required.
*   **Privacy Concepts — PII and PHI**: Personally Identifiable Information (PII) is any data that can identify a specific individual — name, SSN, email address, IP address, biometric data. Protected Health Information (PHI) is a subset of PII that includes medical records, diagnoses, treatment information, and insurance details — regulated specifically by HIPAA in the U.S. Data minimization (collecting only what is necessary) and purpose limitation (using data only for its stated purpose) are key privacy principles.
*   **Security Audits and Assessments**: Organizations use several assessment types to validate their security posture. Internal audit — performed by the organization's own security team. External audit — performed by an independent third party for regulatory compliance verification. Vulnerability assessment — identifies weaknesses but does not exploit them. Penetration test — simulates real attacks to validate exploitability. Bug bounty program — invites external researchers to find vulnerabilities in exchange for rewards.
*   **Third-Party Risk Management**: Organizations face significant risk from vendors, suppliers, and partners who have access to their systems or data. Controls include vendor due diligence reviews, security questionnaires, contractual requirements (SLAs, data processing agreements), and right-to-audit clauses. The supply chain attack vector — where an attacker compromises a trusted vendor to reach the target organization — is a key SY0-701 topic.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Governance, compliance, and privacy fall under **Domain 5 – Security Program Management and Oversight (20%)** of SY0-701. Policy/standard/guideline distinction questions and regulatory applicability scenarios are consistently present on the exam.
*   **Policy vs. Standard vs. Guideline Trap:** Policy = mandatory, high-level intent. Standard = mandatory, specific requirements implementing a policy. Guideline = recommended, non-mandatory. Procedure = step-by-step instructions. If a question describes a document that "recommends but does not require," the answer is guideline. If it defines specific mandatory technical requirements, the answer is standard.
*   **Regulation Applicability:** PCI-DSS applies whenever an organization processes, stores, or transmits credit card data — regardless of size. HIPAA applies to covered entities (healthcare providers, insurers) and their business associates. GDPR applies to any organization that processes data of EU residents — even if the organization is located outside the EU. SY0-701 tests these applicability boundaries.
*   **Data Sovereignty:** Data sovereignty means that data stored in a particular country is subject to that country's laws. Organizations using cloud providers must understand which country's data centers store their data, as this determines which legal jurisdiction applies to law enforcement access requests and breach notification requirements.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include policy hierarchy diagrams, regulation applicability charts, and data classification scenario walkthroughs aligned to SY0-701 exam objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Governance, Compliance, and Privacy" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on the policy document hierarchy, key regulatory frameworks, and data classification principles.
*   **Required Video:** Watch the governance and compliance video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos include regulation applicability scenarios and policy vs. standard vs. guideline comparison walkthroughs.

---

### Lab & Command Integration
In this week's hands-on lab, you will classify a sample dataset according to organizational data classification levels, map a given compliance scenario to the applicable regulation, and evaluate a vendor security questionnaire response for red flags. These skills directly support SY0-701 governance and compliance scenario questions.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to identify the correct policy document type and applicable regulation for any given scenario.
- [ ] Read the "Governance, Compliance, and Privacy" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the governance and compliance video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize: Policy = mandatory intent; Standard = mandatory specifics; Guideline = recommended; PCI-DSS = card data; HIPAA = health data; GDPR = EU resident data.
- [ ] Proceed to the weekly hands-on lab activity.
