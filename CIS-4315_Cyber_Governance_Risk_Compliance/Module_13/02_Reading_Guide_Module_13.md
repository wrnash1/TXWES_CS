# Reading Guide: Module 13 - Data Classification and Privacy Management
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

### Introduction
Welcome to **Module 13 - Data Classification and Privacy Management**! This module covers vendor and third-party risk management — the discipline of identifying, assessing, and managing the security risks introduced when organizations share data or access with external parties. Third-party risk is a growing area of CISM Domain 2 importance as supply chain attacks and vendor breaches increase.

The CISM exam emphasizes that organizations cannot outsource accountability for information security. Even when business processes are delegated to vendors, the originating organization remains responsible for the security of its information.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Third-party risk**: The potential for harm to an organization's information assets, operations, or reputation resulting from activities or failures of external parties (vendors, suppliers, partners, contractors) who access, process, or manage organizational data or systems. Third-party risk is a subset of operational risk that has grown with cloud adoption and outsourcing.
*   **Vendor assessment**: A structured process for evaluating a vendor's security posture, policies, and controls before and during a business relationship. Assessments may include security questionnaires, SOC 2 report reviews, onsite audits, or penetration test results, and are used to determine whether the vendor's security meets the organization's requirements.
*   **SOC 2 reports**: Service Organization Control 2 (SOC 2) reports, defined by the AICPA, provide independent auditor assessments of a service organization's controls related to Security, Availability, Processing Integrity, Confidentiality, and Privacy Trust Services Criteria. SOC 2 Type I evaluates control design at a point in time; SOC 2 Type II evaluates operating effectiveness over a review period (typically 6–12 months).
*   **Service Level Agreements (SLAs)**: Contractual commitments defining the expected performance, availability, and security standards that a vendor must meet, along with the remedies if those standards are not achieved. SLAs provide a contractual mechanism for enforcing security requirements on third parties.
*   **Security questionnaires**: Standardized sets of questions used to assess a vendor's security controls, policies, and practices during the onboarding and periodic review process. Common frameworks include the Standardized Information Gathering (SIG) questionnaire and CAIQ (Cloud Assessment and Information Questionnaire).

---

### 2. Certification Exam Tips
*   **Accountability Cannot Be Outsourced:** A core CISM principle: when an organization contracts with a vendor, it retains accountability for the security of its data. If the vendor breaches data, the organization is still responsible to regulators and customers. The exam tests this accountability concept frequently.
*   **SOC 2 Type I vs. Type II:** The CISM exam tests this distinction. Type I = design at a point in time (snapshot); Type II = operating effectiveness over a period (movie). Type II provides stronger assurance and is generally preferred for ongoing vendor relationships.
*   **Vendor Risk Tiers:** Not all vendors require the same level of scrutiny. Organizations should tier vendors by their access level and data sensitivity: Tier 1 (critical data/access, full assessment), Tier 2 (limited access, questionnaire + SLA), Tier 3 (no data access, minimal review).
*   **Study Resource:** [NIST SP 800-161 Rev. 1: Cybersecurity Supply Chain Risk Management](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) — This free NIST publication provides comprehensive guidance on managing cybersecurity risks in supply chains and vendor relationships, directly relevant to CISM third-party risk management.

---

### Required Readings & Videos
*   **Required Reading:** [NIST SP 800-161 Rev. 1: Cybersecurity Supply Chain Risk Management](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) — This free NIST publication covers supply chain risk identification, vendor assessment practices, contract requirements, and ongoing monitoring. Review Section 2 (Fundamentals of C-SCRM) for exam-relevant vendor risk concepts.
*   **Required Video:** Watch the video lecture on **Data Classification and Privacy Management** in the official course playlist: [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply third-party risk management concepts through the following activities:
*   **Evaluate vendor security disclosures**: Review a provided sample SOC 2 Type II report excerpt and identify: (1) the Trust Services Criteria covered, (2) any exceptions noted by the auditor, and (3) what questions you would ask the vendor about each exception.
*   **Review and interpret control deficiencies in a mock SOC 2 report**: Given a sample SOC 2 Type II report with three noted exceptions, assess the risk each exception poses to your organization and document whether each is acceptable, requires compensating controls, or is grounds for vendor re-evaluation.
*   **Draft vendor SLA security requirements**: Create a security addendum to a cloud services SLA, specifying minimum requirements for incident notification timeline, audit rights, data return/destruction on contract end, and access control standards.


---

### 3. Study Checklist
- [ ] Know the difference between SOC 2 Type I and Type II and when each provides sufficient assurance.
- [ ] Understand that accountability for data security cannot be transferred to vendors.
- [ ] Read [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final), Section 2 on supply chain risk fundamentals.
- [ ] Watch the video lecture on **Data Classification and Privacy Management** in [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).
- [ ] Complete the lab activity on SOC 2 review and vendor SLA security requirements.
- [ ] Proceed to the Module 13 quiz.
