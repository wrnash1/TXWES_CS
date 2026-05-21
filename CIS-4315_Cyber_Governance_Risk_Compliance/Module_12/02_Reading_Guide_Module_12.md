# Reading Guide: Module 12 - Third-Party Risk and Vendor Management
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

### Introduction
Welcome to **Module 12 - Third-Party Risk and Vendor Management**! This module covers IT security auditing — the independent examination of security controls to verify that they operate effectively and align with organizational policies, regulatory requirements, and design objectives. Audit and assurance skills span CISM Domains 1 and 2.

The CISM exam tests audit from the security manager's perspective: understanding audit scope, interpreting findings, and remediating control deficiencies — not performing detailed audit procedures.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **IT audit**: A systematic, independent examination of an organization's IT systems, controls, and processes to determine whether they adequately protect information assets, operate reliably, and comply with applicable policies and regulations. IT auditors evaluate design effectiveness (are controls designed correctly?) and operating effectiveness (are controls functioning as intended?).
*   **Internal audit vs. external audit**: Internal audits are conducted by the organization's own audit function (or co-sourced auditors) and report to the audit committee or board; they provide ongoing assurance and identify issues before external review. External audits are conducted by independent third-party firms and provide assurance to regulators, investors, and customers — they carry greater independence and credibility.
*   **Audit evidence**: The information collected by auditors to support audit findings and conclusions, including documentation, system logs, interview responses, observations, and re-performance of control procedures. The quality and sufficiency of evidence determines the strength of audit conclusions.
*   **Audit trail logs**: Chronological records of system events, user activities, and access transactions that enable reconstruction of what occurred within an information system. Audit trail logs are essential for both security monitoring and audit evidence; they must be protected from unauthorized modification (tamper-evident).
*   **Control testing**: The audit procedures used to evaluate whether security controls are operating as designed, including inquiry, observation, inspection of documentation, and re-performance. Control testing produces findings that are rated by severity (critical, significant, minor) based on the risk created by any gaps.

---

### 2. Certification Exam Tips
*   **Auditor Independence:** CISM exam scenarios frequently test the importance of auditor independence. Security managers who also perform the functions being audited cannot provide objective assurance — an audit function must be organizationally separate from the functions it reviews.
*   **Design vs. Operating Effectiveness:** Know the difference. A control may be well-designed on paper but fail to operate effectively in practice (e.g., a password policy requiring 90-day changes that no one enforces). Both dimensions must be assessed.
*   **Audit Findings Require Remediation Plans:** When an audit identifies a control deficiency, the security manager is responsible for developing a corrective action plan with timeline and owner — not disputing the finding. The CISM exam may test this response.
*   **Study Resource:** [ISACA IT Audit Framework (ITAF)](https://www.isaca.org/resources/it-audit) — ISACA provides free overview materials on IT audit standards. The ITAF is the authoritative standard for IT audits aligned with CISM competencies.

---

### Required Readings & Videos
*   **Required Reading:** [NIST SP 800-53A Rev. 5: Assessing Security and Privacy Controls](https://csrc.nist.gov/publications/detail/sp/800-53a/rev-5/final) — This free NIST publication provides the methodology for assessing security controls, including testing procedures (examine, interview, test) for each control family. Review Chapter 2 (Assessing Security Controls) for exam-relevant assurance concepts.
*   **Required Video:** Watch the video lecture on **Third-Party Risk and Vendor Management** in the official course playlist: [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply security auditing concepts through the following activities:
*   **Draft an audit evidence request list**: Create a sample information request list (PBC — Prepared by Client list) for an access control audit, specifying which documents, system reports, and personnel you would need to assess access management controls.
*   **Analyze system login logs for audit trail completeness**: Given a sample log extract, identify which required audit trail fields are present (timestamp, user ID, event type, source IP, result) and note any gaps that would reduce the logs' value as evidence.
*   **Write an audit finding memo**: Draft a two-paragraph finding memo documenting a sample control deficiency (e.g., shared administrative credentials found on a production server), including condition, criteria, cause, effect, and recommendation.


---

### 3. Study Checklist
- [ ] Be able to distinguish design effectiveness from operating effectiveness.
- [ ] Understand the difference between internal and external audits and when each is appropriate.
- [ ] Read [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53a/rev-5/final), Chapter 2 on assessment methodology.
- [ ] Watch the video lecture on **Third-Party Risk and Vendor Management** in [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).
- [ ] Complete the lab activity on audit evidence requests and finding documentation.
- [ ] Proceed to the Module 12 quiz.
