# Lab Activity: Module 14 — Disaster Recovery Management

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

## Lab Overview

In this lab you will apply the Disaster Recovery Management concepts from Module 14 to a realistic scenario. You will evaluate DR site options against defined RTO requirements, design a cloud DR architecture, analyze backup strategies, produce a DR test plan, and draft a DR plan document outline. All deliverables are written artifacts — no cloud account access is required, though students with AWS or Azure free-tier accounts may optionally supplement their analysis with console screenshots.

**Estimated Time:** 90–120 minutes

**Grading Weight:** See Canvas assignment for point value.

---

## Scenario: Apex Distribution Services

Apex Distribution Services operates a regional logistics network with fourteen distribution centers across the southwestern United States. Apex's IT environment consists of a primary data center in Phoenix, Arizona, hosting the following systems:

- **Warehouse Management System (WMS):** Manages real-time inventory across all fourteen facilities. Tier 1. RTO: 1 hour. RPO: 15 minutes.

- **Transportation Management System (TMS):** Coordinates carrier scheduling and route optimization. Tier 1. RTO: 2 hours. RPO: 30 minutes.

- **Customer Order Portal:** Web-facing order entry and tracking for B2B customers. Tier 2. RTO: 6 hours. RPO: 1 hour.

- **Financial ERP System:** General ledger, accounts payable, accounts receivable. Tier 2. RTO: 8 hours. RPO: 4 hours.

- **HR Information System (HRIS):** Payroll processing and employee records. Tier 3. RTO: 48 hours. RPO: 24 hours.

Apex currently has no DR program. The company has suffered two significant outages in the past eighteen months: a fiber cut that caused six hours of downtime for all systems, and a server hardware failure that caused the WMS to be unavailable for eleven hours. The CEO has approved a DR program initiative and has asked you, as the Director of IT Security and Compliance, to design the program architecture and documentation.

---

## Part 1: DR Site Type Analysis

### Task 1.1 — Site Type Recommendation

For each of the five systems listed in the scenario, recommend the most appropriate DR site type from the following options:

- Hot Site

- Warm Site

- Cold Site

- Cloud — Multi-Site Active-Active

- Cloud — Warm Standby

- Cloud — Pilot Light

- Cloud — Backup and Restore

Your recommendation must be architecturally consistent with the RTO listed for each system. A system with a one-hour RTO cannot be assigned a cold site or a backup-and-restore approach.

Present your recommendations in a table with these columns:

- **System**

- **Tier**

- **RTO**

- **Recommended DR Site Type**

- **Justification (2–3 sentences)**

- **Relative Cost Tier (Low / Medium / High / Very High)**

**Deliverable 1:** Completed site type recommendation table. (20 points)

### Task 1.2 — Cost-Benefit Narrative

Write a 200–250 word narrative addressed to Apex's CEO justifying the DR investment recommendations from Task 1.1. Your narrative must:

1. Reference the actual business impact of the two historical outages (make reasonable assumptions about revenue impact based on a regional logistics operation).

2. Explain why different systems receive different site type recommendations rather than a uniform approach.

3. Summarize the cost tiers and explain the risk tradeoff for any system assigned a lower-cost option.

**Deliverable 2:** CEO-addressed cost-benefit narrative. (15 points)

---

## Part 2: Cloud DR Architecture Design

### Task 2.1 — Architecture Diagram Description

Apex's leadership has decided to implement a cloud-based DR strategy using AWS. For the two Tier 1 systems (WMS and TMS), design a cloud DR architecture using the appropriate AWS pattern from Task 1.1.

Write a structured description of the architecture using the following format for each system:

**System:** [name]

**AWS DR Pattern:** [pattern name]

**Primary Region:** US-West-2 (Oregon)

**Recovery Region:** US-East-1 (Northern Virginia)

**Replication Method:** Describe how data is replicated between regions (AWS service name and replication mechanism).

**Compute Recovery:** Describe how EC2 instances or containers are provisioned in the recovery region (pre-launched vs. launched on failover, instance types).

**Database Recovery:** Describe the database replication mechanism (RDS Multi-AZ, cross-region read replica, Aurora Global Database, or equivalent).

**Failover Trigger:** Describe whether failover is automatic or manual and what condition triggers it.

**Estimated RTO Achievement:** Explain in one paragraph why this architecture can achieve the stated RTO.

**Estimated RPO Achievement:** Explain in one paragraph why this architecture can achieve the stated RPO.

Complete this structured description for both WMS and TMS.

**Deliverable 3:** Cloud DR architecture descriptions for WMS and TMS. (25 points)

---

## Part 3: Backup Strategy Analysis

### Task 3.1 — Backup Design

For the Financial ERP System (Tier 2, RTO 8 hours, RPO 4 hours), design a complete backup strategy using the following constraints:

- The backup window must not impact business-hours performance.

- The strategy must use a combination of full and either incremental or differential backups.

- Data must be protected using the 3-2-1-1 rule.

Specify the following for your backup design:

1. Backup schedule (day/time for full backups, day/time for incremental or differential backups).

2. Backup media and storage locations (on-premises, cloud, tape, etc.) mapped to the 3-2-1-1 rule requirements.

3. Immutable storage approach — which copy is immutable and how immutability is enforced.

4. Retention policy — how long each backup type is retained.

5. Restore procedure — describe the steps to restore the ERP to any given point in time within the past 30 days.

**Deliverable 4:** Backup strategy specification for the Financial ERP System. (20 points)

### Task 3.2 — RPO Gap Check

Given the backup schedule you designed in Task 3.1, verify that your backup strategy achieves the 4-hour RPO for the Financial ERP System. Show your reasoning explicitly:

- At what point in your schedule is the maximum time between captures?

- Does that maximum gap equal or exceed the 4-hour RPO?

- If a gap exists, propose a modification to close it.

**Deliverable 5:** RPO gap check calculation and any required backup strategy modification. (10 points)

---

## Part 4: DR Test Plan

### Task 4.1 — Annual DR Testing Schedule

Design a twelve-month DR testing schedule for Apex covering all five systems. Include at minimum:

- Two walkthroughs (different systems).

- One parallel test.

- One full cutover test for a Tier 1 system.

For each scheduled test, specify:

- Test type.

- Target month.

- System or systems in scope.

- Duration estimate.

- Key participants.

- Pre-test requirements.

- Primary success criteria.

Present the schedule in table format.

**Deliverable 6:** Twelve-month DR test schedule table. (20 points)

### Task 4.2 — Full Cutover Test Justification

Write a 150–200 word memo to Apex's CEO requesting authorization for the full cutover test identified in your schedule. The memo must:

1. Explain what a full cutover test is and why it provides value that parallel testing cannot.

2. Acknowledge the risk of the test and explain what safeguards you have put in place.

3. Specify the maintenance window, affected users, and expected duration.

4. State what outcome would be considered a successful test.

**Deliverable 7:** Full cutover test authorization memo. (15 points)

---

## Part 5: DR Plan Document Outline

### Task 5.1 — Produce a DR Plan Outline

Using the six-section DR plan structure from the Module 14 Reading Guide, produce a structured DR plan outline for Apex Distribution Services covering all five systems.

The outline does not need full procedure text, but each section must include:

- The section title.

- A two- to four-sentence description of what that section will contain for Apex specifically.

- **Section 3 (Roles and Responsibilities):** Name at least five specific roles with their DR responsibilities and contact requirements.

- **Section 2 (Activation Criteria):** Define at least three specific events or thresholds that would trigger DR activation for Apex.

- **Section 4 (Recovery Procedures):** For one system of your choice, outline at least five specific procedure steps in the format: Step number → Action → Expected outcome → Error handling.

**Deliverable 8:** Six-section DR plan outline with the enhancements specified above. (20 points)

---

## Submission Requirements

1. Compile all eight deliverables into a single document.

2. Include your name, course number, and module number in the document header.

3. Label each deliverable clearly (Deliverable 1, Deliverable 2, etc.).

4. Minimum total analytical content: 1,400 words (tables and headers do not count toward word count).

5. Submit as PDF or DOCX through the Canvas assignment portal.

---

## Grading Rubric Summary

| Deliverable | Points | Key Criteria |
|---|---|---|
| 1 — Site Type Table | 20 | RTO consistency, justification depth |
| 2 — CEO Narrative | 15 | Business framing, risk tradeoff acknowledgment |
| 3 — Cloud Architecture | 25 | Pattern accuracy, RTO/RPO achievement logic |
| 4 — Backup Strategy | 20 | 3-2-1-1 compliance, schedule completeness |
| 5 — RPO Gap Check | 10 | Correct calculation, gap identification |
| 6 — Test Schedule | 20 | All required test types, realistic schedule |
| 7 — Cutover Memo | 15 | Risk acknowledgment, safeguards, success criteria |
| 8 — DR Plan Outline | 20 | Completeness, specificity to Apex |
| **Total** | **145** | |

---

## Troubleshooting and Common Errors

**Common error — Assigning cold site to Tier 1 systems:** A cold site requires days to weeks for recovery. Any system with an RTO of two hours or less requires a hot site, warm site, or cloud warm-standby equivalent. Review Section 1 of the Reading Guide if your recommendations appear misaligned.

**Common error — Confusing RPO and backup frequency:** If your backup captures data every four hours and the RPO is one hour, you have a three-hour gap. Backup frequency must be equal to or shorter than the RPO target. The RPO is the ceiling, not the target.

**Common error — Omitting failback from the DR test plan:** A DR test is not complete without confirming the ability to return to the primary site. Ensure your test plan includes failback procedures for the full cutover test.

---

## Part 9 — Challenge Exercise

### Challenge 1: Ransomware DR Scenario — End-to-End Recovery Analysis

Apex Logistics discovers at 6:00 AM on a Tuesday that ransomware has encrypted its primary ERP system and three supporting application servers. The DR team declares an incident and initiates the DR plan. Using the DR architecture you designed in the main lab exercises, complete the following tasks.

1. Write a step-by-step failover execution checklist (minimum eight steps) covering the sequence from incident declaration through production traffic redirection to the DR site. For each step include: the action, the responsible role, the expected outcome, the estimated time to complete, and the go/no-go validation criterion before proceeding to the next step.
2. Identify three decisions during the failover sequence that require escalation to a named authority (CISO, CTO, or CEO) rather than being made by the recovery team alone. For each, explain why that specific decision requires executive authorization rather than team-level judgment, and what information the executive needs to make the decision.
3. After forty-eight hours operating from the DR site, the primary environment has been rebuilt. Draft a failback readiness checklist of at least six items that must be verified before traffic is returned to the primary site. Include at least one security validation item (confirming the attack vector is closed), one data integrity item, and one operational validation item.
4. Write a 150-word post-recovery executive briefing summarizing what happened, how long the organization operated from the DR site, what data loss (if any) occurred relative to the RPO, whether the RTO was met, and two lessons learned that will improve the DR program.

### Challenge 2: 3-2-1-1 Backup Architecture Design

Apex Logistics currently backs up all systems to a single NAS device in the primary data center. Following the ransomware incident, the CISO mandates implementation of the 3-2-1-1 backup rule within sixty days.

1. Design a compliant backup architecture for Apex's three most critical systems (ERP, financial reporting, customer database). For each system create a table specifying: backup type (full/incremental/differential), backup frequency, backup medium (disk/tape/cloud), storage location (on-site/off-site/cloud), immutability mechanism, and estimated restoration time.
2. Identify two specific ransomware attack scenarios and explain how the 3-2-1-1 architecture you designed would prevent or limit data loss in each scenario. Be specific about which copies survive each attack vector and why.
3. Calculate the RPO gap for each system's current backup architecture (single NAS, daily full backup at midnight) versus your proposed 3-2-1-1 architecture. Present results in a comparison table showing current RPO exposure, proposed RPO target, and the gap closed by each change.
4. Draft a one-paragraph memo to the CFO justifying the investment in the 3-2-1-1 architecture by quantifying the cost of a full data loss event versus the annual cost of the proposed backup architecture.

### Reflection Questions

1. During a DR test, the recovery team successfully fails over to the warm standby site in ninety minutes — well within the two-hour RTO. The CISO declares the test a complete success and closes the test report. A junior analyst notes that the failback procedure was never executed and that three of the application tier connection strings were updated manually rather than by the documented automated script. Explain why the CISO's declaration of complete success is a governance error, and describe what a properly closed DR test report must contain.
2. An organization operates a hot site for its Tier 1 payment processing system at an annual cost of $400,000. A new CFO proposes replacing the hot site with a warm site costing $80,000 per year to save $320,000 annually. The payment processing system generates $600,000 per hour in revenue and has an RTO of thirty minutes. Using the cost-benefit framework from this module, build the financial argument for or against the CFO's proposal, and describe what governance process should be used to make this risk acceptance decision.
