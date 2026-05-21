# Quiz: Module 07 - Security Program Development and Management
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
Which metric defines the maximum acceptable age of data that must be recovered from backup storage after a system failure?
*   A) Recovery Time Objective (RTO)
*   B) Recovery Point Objective (RPO)
*   C) Maximum Tolerable Downtime (MTD)
*   D) Mean Time to Repair (MTTR)
*   **Correct Answer:** B) RPO measures data loss tolerance — an RPO of 4 hours means backups must run at least every 4 hours to ensure no more than 4 hours of data can be lost.
*   **Distractor Analysis:**
    *   *Why B is correct:* RPO defines how far back in time recovery must be able to reach; it drives backup frequency and replication strategy decisions.
    *   *Why A is incorrect:* RTO measures how long the system can be offline before recovery is required — it measures time duration, not data age.
    *   *Why C is incorrect:* MTD is the absolute maximum survival limit for downtime; it is always greater than or equal to RTO.
    *   *Why D is incorrect:* MTTR is an operational metric measuring average time to repair a failed component; it is not a business continuity planning metric.

---

**Question 2**
Which of the following most accurately describes **critical business functions** in the context of BIA?
*   A) The IT systems designated as high-availability by the network engineering team
*   B) The set of automated tasks scheduled in a company's job scheduling system
*   C) The organizational processes whose unavailability for more than a defined period would cause unacceptable harm to the organization's mission, finances, regulatory standing, or reputation
*   D) All functions performed by the information security team during a security incident
*   **Correct Answer:** C) Critical business functions are defined by their operational impact on the organization — not by IT systems or security team activities.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* High-availability IT designations are technical infrastructure decisions; business criticality is determined by business impact, not system redundancy.
    *   *Why B is incorrect:* Scheduled jobs are an IT operations concern; criticality is a business judgment about operational continuity.
    *   *Why C is correct:* BIA methodology identifies functions where disruption causes unacceptable business harm — these drive all subsequent recovery planning priorities.
    *   *Why D is incorrect:* Security incident response activities are important but distinct from the operational business functions that BIA is designed to protect.

---

**Question 3**
A healthcare organization's billing system has an RTO of 4 hours and an MTD of 8 hours. The current disaster recovery plan provides a recovery capability of 6 hours. What risk does this situation present?
*   A) No risk — the recovery time of 6 hours falls within the MTD of 8 hours
*   B) A governance risk — the RTO and MTD values have not been approved by senior management
*   C) An unacceptable recovery gap — the 6-hour recovery time exceeds the 4-hour RTO, violating the business requirement even though it is within MTD
*   D) A compliance risk — the 8-hour MTD exceeds HIPAA-required availability standards
*   **Correct Answer:** C) The DRP must meet or beat the RTO to satisfy the business requirement; a 6-hour recovery time violates the 4-hour RTO even though MTD has not yet been breached.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Meeting MTD is the survival threshold, not the target; the RTO is the operational requirement that must be met for acceptable business continuity.
    *   *Why B is incorrect:* The scenario describes an operational gap, not a governance approval issue; the values are presumably approved.
    *   *Why C is correct:* RTO is the designed target for recovery; falling between RTO and MTD means operations are disrupted beyond acceptable limits even if the organization survives.
    *   *Why D is incorrect:* HIPAA does not prescribe specific numeric availability windows; this distractor introduces a false compliance claim.

---

**Question 4**
Who should take the primary lead in conducting a Business Impact Analysis?
*   A) The CISO and security team, because BIA is a security risk assessment function
*   B) External auditors, because they provide an objective assessment free from internal bias
*   C) Business unit managers and process owners, with support from the security team to facilitate data collection
*   D) The IT operations team, because they have detailed knowledge of system dependencies
*   **Correct Answer:** C) BIA requires business unit managers to quantify the impact of disruption to their processes — only they can assess the true business consequence; the security team facilitates but does not drive the analysis.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Security teams facilitate BIA but cannot independently determine business impact values without input from process owners.
    *   *Why B is incorrect:* External auditors assess existing processes; they do not lead BIA, which requires intimate organizational knowledge.
    *   *Why C is correct:* CISM emphasizes that BIA is a business exercise — operational managers who live with the processes must provide the impact data.
    *   *Why D is incorrect:* IT operations understands system infrastructure but cannot substitute for business judgment on operational impact.

---

**Question 5**
An organization's payroll system has an RTO of 2 hours, an RPO of 30 minutes, and an MTD of 6 hours. A hurricane disrupts operations and the system is restored after 5 hours and 45 minutes. Which statement best characterizes this recovery outcome?
*   A) Recovery was fully successful because the MTD of 6 hours was not exceeded
*   B) Recovery met the RTO requirement because the system was restored before MTD
*   C) Recovery failed to meet the RTO of 2 hours, indicating the disaster recovery plan needs improvement even though the organization survived the disruption
*   D) The RPO was violated because more than 30 minutes of data was likely lost during the 5-hour 45-minute outage
*   **Correct Answer:** C) The 5 hour 45-minute recovery far exceeded the 2-hour RTO — the organization survived (MTD not breached) but the recovery plan clearly failed to deliver on its designed business commitment.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Not exceeding MTD means the organization survived, but survival is the minimum threshold — the RTO was massively violated, indicating an unacceptable recovery performance.
    *   *Why B is incorrect:* Restoring before MTD is not the same as meeting RTO; the 2-hour RTO was the operational target.
    *   *Why C is correct:* RTO is the business's required recovery speed; a nearly 6-hour recovery against a 2-hour RTO indicates serious gaps in the disaster recovery plan.
    *   *Why D is incorrect:* Option D is also factually true but is a secondary concern; the primary finding is the RTO failure. Option C is the "best characterization" because it identifies the most significant planning failure.
