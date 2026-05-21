# Reading Guide: Module 08 - Security Architecture and Design
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

### Introduction
Welcome to **Module 08 - Security Architecture and Design**! This module focuses on Business Continuity Planning (BCP) and Disaster Recovery Planning (DRP) — the disciplines that ensure an organization can survive and recover from disruptive events. These topics appear throughout CISM Domain 4 (Incident Management) and are closely linked to BIA concepts from Module 07.

The CISM exam distinguishes between BCP (maintaining business operations during a disruption) and DRP (restoring IT systems and data after a disaster). Candidates must understand both the strategic and operational dimensions of continuity planning.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Business Continuity Plan (BCP)**: A comprehensive, documented set of procedures and resources designed to enable an organization to maintain or rapidly resume critical business functions during and after a disruptive event. BCPs address the full scope of business operations, including manual workarounds, communication plans, and alternate work arrangements.
*   **Disaster Recovery Plan (DRP)**: A subset of the BCP that specifically addresses the procedures for restoring IT systems, applications, data, and infrastructure following a disaster. DRP focuses on the technology recovery aspects of continuity, guided by the RTO and RPO requirements established by the BIA.
*   **Hot/warm/cold recovery sites**: A spectrum of alternate facility options for continuing operations after a primary site is lost. A hot site is a fully operational, real-time replica ready for immediate failover. A warm site has infrastructure and partial data but requires some setup time (hours to days). A cold site provides only physical space and utilities, requiring full equipment setup and data restoration before use.
*   **DRP testing methods (tabletop, walkthrough, simulation, parallel, full interruption)**: Structured exercises used to validate DRP effectiveness. A tabletop exercise is a discussion-based review where team members talk through their response to a scenario. A walkthrough verifies that participants understand their roles. Simulation, parallel testing, and full interruption tests progressively increase operational realism and cost.

---

### 2. Certification Exam Tips
*   **BCP vs. DRP Scope:** CISM distinguishes these two plans. BCP is broader (business operations continuity); DRP is specific to IT systems recovery. Both are required; neither alone is sufficient.
*   **Hot/Warm/Cold Site Trade-offs:** The CISM exam tests the cost-vs-recovery speed trade-off. Hot sites = fastest recovery, highest cost; cold sites = slowest recovery, lowest cost. The appropriate choice depends on the RTO established in the BIA.
*   **Test Before You Need It:** The exam emphasizes that untested plans cannot be relied upon. Tabletop exercises are the least disruptive testing method and are a starting point; they do not replace functional testing.
*   **Study Resource:** [NIST SP 800-34 Rev. 1: Contingency Planning Guide](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final) — Section 3.5 covers alternate site strategies (hot/warm/cold) and Section 3.6 covers plan testing, training, and exercises. This is a free ZTC resource.

---

### Required Readings & Videos
*   **Required Reading:** [NIST SP 800-34 Rev. 1: Contingency Planning Guide](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final) — Sections 3.5 (Alternate Sites) and 3.6 (Plan Testing). This free publication provides the authoritative guidance on recovery site selection and DRP testing methodologies.
*   **Required Video:** Watch the video lecture on **Security Architecture and Design** in the official course playlist: [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply BCP/DRP concepts through the following activities:
*   **Design a tabletop exercise scenario**: Write a realistic disaster scenario (ransomware attack, datacenter fire, or regional power outage) and develop 5 inject questions that test participants' knowledge of DRP activation procedures, communication protocols, and recovery priorities.
*   **Compare hot, warm, and cold site parameters**: Using a provided scenario with stated RTO requirements, evaluate which recovery site type is appropriate and calculate the estimated annual cost of each option against the business risk it mitigates.
*   **Draft an emergency activation checklist**: Create a 15-step activation procedure for a fictional organization's DRP, covering declaration authority, initial notification contacts, site activation steps, and status reporting requirements.


---

### 3. Study Checklist
- [ ] Be able to distinguish BCP from DRP in scope and purpose.
- [ ] Know the hot/warm/cold site characteristics and the cost-vs-speed trade-off for each.
- [ ] Read [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final), Sections 3.5 and 3.6 on alternate sites and plan testing.
- [ ] Watch the video lecture on **Security Architecture and Design** in [ISACA CISM / Cyber GRC Course Playlist](https://www.youtube.com/playlist?list=PLbnu8t2G_vG0V7kC0V3n_nU9Y3S-4K178).
- [ ] Complete the lab activity on tabletop exercise design and recovery site comparison.
- [ ] Proceed to the Module 08 quiz.
