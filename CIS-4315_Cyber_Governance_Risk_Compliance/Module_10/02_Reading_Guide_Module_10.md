# Reading Guide: Module 10 - Incident Response – Containment, Eradication, Recovery
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

### Introduction
Welcome to **Module 10 - Incident Response: Containment, Eradication, Recovery**! This module covers global privacy regulations — specifically GDPR and CCPA — that define individual data rights and impose obligations on organizations that collect, process, and store personal information. Privacy regulation compliance is increasingly critical for information security managers as privacy and security programs converge.

The CISM exam treats privacy regulations as a governance and risk management obligation. Candidates must understand what each regulation protects, which organizations it applies to, and what security controls it requires.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **General Data Protection Regulation (GDPR)**: A comprehensive European Union privacy regulation that came into effect in 2018, applying to any organization worldwide that processes personal data of EU residents. GDPR grants individuals rights over their personal data, requires explicit consent for data processing, mandates breach notification within 72 hours of discovery, and authorizes fines of up to 4% of global annual revenue for violations.
*   **California Consumer Privacy Act (CCPA)**: A California state law that grants California residents rights to know what personal information is collected about them, request deletion of their data, and opt out of the sale of their personal information. CCPA applies to for-profit businesses meeting certain size or revenue thresholds that collect California residents' personal information.
*   **Personally Identifiable Information (PII)**: Any data that can be used to identify, locate, or contact a specific individual, either alone or in combination with other information. PII includes names, social security numbers, email addresses, IP addresses, biometric data, and health records. Different regulations define PII scope differently — GDPR uses the broader term "personal data."
*   **Right to be forgotten (Right to Erasure)**: A GDPR right (Article 17) that allows individuals to request that an organization permanently delete their personal data when it is no longer necessary for the original purpose, when consent is withdrawn, or when the data has been unlawfully processed. Organizations must implement technical processes to fulfill erasure requests within specified timeframes.

---

### 2. Certification Exam Tips
*   **GDPR's Extraterritorial Reach:** CISM exam scenarios may involve a U.S. company with EU customers. Remember that GDPR applies based on the **data subject's location** (EU resident), not the organization's location. Any organization processing EU residents' data must comply.
*   **72-Hour Breach Notification:** GDPR requires breach notification to supervisory authorities within 72 hours of discovery — much faster than HIPAA's 60-day window. This distinction is frequently tested.
*   **Privacy by Design:** GDPR requires organizations to incorporate privacy protections into systems from the design stage, not as an afterthought. Security managers must ensure new system designs include privacy impact assessments (PIAs/DPIAs).
*   **Study Resource:** [EUR-Lex GDPR Full Text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) — The official GDPR regulation text is publicly available. For exam preparation, focus on Articles 5 (Principles), 17 (Erasure), 25 (Privacy by Design), and 33–34 (Breach Notification).

---

### Required Readings & Videos
*   **Required Reading:** [NIST Privacy Framework Version 1.0](https://www.nist.gov/privacy-framework/privacy-framework) — This free NIST publication provides a voluntary framework for managing privacy risk that complements GDPR and CCPA compliance. Review the Core (Identify-P, Govern-P, Control-P, Communicate-P, Protect-P) structure.
*   **Required Video:** Watch the video lecture on **Incident Response Containment, Eradication, and Recovery** in the official course playlist: [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply privacy regulation concepts through the following activities:
*   **Map PII data flows**: Given a sample e-commerce application architecture, identify all locations where PII is collected, stored, processed, and transmitted, and document whether each location is in scope for GDPR or CCPA obligations.
*   **Draft a GDPR Right to Erasure workflow**: Design a step-by-step process describing how an organization would receive, verify, execute, and confirm a data deletion request under GDPR Article 17, including system touchpoints and response timeline requirements.
*   **Compare GDPR vs. CCPA breach notification requirements**: Create a side-by-side comparison of notification timelines, notification recipients, and required notification content under GDPR and CCPA.


---

### 3. Study Checklist
- [ ] Know GDPR's 72-hour breach notification requirement and how it differs from HIPAA.
- [ ] Understand the right to erasure and what it requires technically.
- [ ] Review the [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework).
- [ ] Watch the video lecture on **Incident Response** in [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).
- [ ] Complete the lab activity on PII mapping and GDPR erasure workflow.
- [ ] Proceed to the Module 10 quiz.
