# Reading Guide: Module 07 - Security Program Development and Management
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

### Introduction
Welcome to **Module 07 - Security Program Development and Management**! This module covers Business Impact Analysis (BIA) — the systematic process of identifying critical business functions and determining the consequences of disruption. BIA is the foundation of both business continuity planning and the security program's prioritization of protective controls.

BIA bridges CISM Domain 2 (Risk Management) and Domain 4 (Incident Management). Candidates must understand how BIA outputs — RTOs, RPOs, and MTDs — drive recovery planning and resource allocation decisions.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Business Impact Analysis (BIA)**: A systematic process that identifies and evaluates the potential effects of disruptions to critical business functions, quantifying financial, operational, legal, and reputational impacts. BIA outputs establish the priority order for recovering business functions and inform the design of continuity and disaster recovery plans.
*   **Critical business functions**: The subset of organizational processes whose disruption would cause unacceptable harm to the organization's mission, finances, regulatory standing, or reputation if unavailable for more than a defined period. Identifying critical functions is the first and most important step in BIA.
*   **Recovery Time Objective (RTO)**: The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disruption. RTO is defined by business requirements, not technical capability — it represents the business's tolerance for unavailability.
*   **Recovery Point Objective (RPO)**: The maximum acceptable age of data that must be recovered from backup storage to restore normal operations, representing the limit of tolerable data loss. RPO drives backup frequency decisions: an RPO of 4 hours requires backup intervals of 4 hours or less.
*   **Maximum Tolerable Downtime (MTD)**: The absolute longest period a business function can be disrupted before the organization suffers irreparable harm (financial collapse, loss of license, permanent customer loss). MTD is always greater than or equal to RTO; if recovery takes longer than MTD, the organization may not survive the disruption.

---

### 2. Certification Exam Tips
*   **RTO vs. RPO vs. MTD Distinctions:** The CISM exam frequently tests these three metrics in scenario questions. RTO = maximum downtime tolerated; RPO = maximum data loss tolerated; MTD = absolute survival limit. Recovery must occur within RTO, which must be less than MTD.
*   **BIA Is Business-Led, Not IT-Led:** The CISM exam emphasizes that BIA must be driven by business unit managers who understand operational impact — IT staff cannot determine business impact values without input from the business.
*   **BIA Precedes Recovery Planning:** A common exam trap is to present recovery planning before BIA. The correct sequence is BIA → Recovery Strategy → DRP/BCP. Without BIA outputs, recovery plans cannot be properly prioritized.
*   **Study Resource:** [NIST SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final) is a free publication that covers BIA methodology, RTO/RPO development, and their relationship to continuity planning.

---

### Required Readings & Videos
*   **Required Reading:** [NIST SP 800-34 Rev. 1: Contingency Planning Guide](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final) — This free NIST publication covers BIA methodology in Section 3.2, including how to identify critical functions, determine impact, and establish recovery time objectives. This is a ZTC resource.
*   **Required Video:** Watch the video lecture on **Security Program Development and Management** in the official course playlist: [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply BIA methodology through the following activities:
*   **Draft a BIA questionnaire**: Create a 10-question survey designed for business unit managers to identify critical functions, quantify disruption costs per hour/day, and define their maximum tolerable downtime.
*   **Prioritize critical processes and assign MTD scores**: Given a list of 8 business processes, rank them by MTD (shortest to longest) and justify why certain processes have lower tolerance for downtime than others.
*   **Determine RTO and RPO requirements**: For three prioritized processes, derive RTO and RPO values from provided MTD and business impact data, and identify what backup/recovery technologies would be required to meet those objectives.


---

### 3. Study Checklist
- [ ] Be able to define RTO, RPO, and MTD and explain the relationship between them.
- [ ] Read [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final), Section 3.2 on BIA methodology.
- [ ] Watch the video lecture on **Security Program Development and Management** in [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).
- [ ] Complete the lab activity on building a BIA questionnaire and prioritizing recovery objectives.
- [ ] Proceed to the Module 07 quiz.
