# Quiz: Module 13 — Business Continuity Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

**Question 1**

An organization conducts a Business Impact Analysis and determines that its order management system generates $45,000 in revenue per hour. Regulatory penalties for service unavailability begin accruing at the six-hour mark. Reputational harm becomes significant at twelve hours. Which metric does this timeline analysis most directly establish?

- A) Recovery Point Objective (RPO)
- B) Maximum Tolerable Period of Disruption (MTPD)
- C) Work Recovery Time (WRT)
- D) Service Level Agreement (SLA) threshold

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The impact timeline identifies the point at which consequences become unacceptable — that is the definition of MTPD. The analysis reveals the absolute ceiling on downtime, which sets MTPD.

- **Why A is incorrect:** RPO concerns maximum acceptable data loss, not the duration of service unavailability. The impact timeline described measures downtime impact, not data freshness requirements.

- **Why C is incorrect:** WRT is the time needed to reconcile data after systems are restored — a post-recovery metric, not derived from financial/regulatory impact analysis.

- **Why D is incorrect:** SLA thresholds are contractual commitments to external parties. MTPD is an internal business analysis metric derived from operational and financial impact.

---

**Question 2**

A hospital's EHR system has an RPO of thirty minutes. The current backup architecture performs full backups nightly and transaction log backups every four hours. Which statement accurately describes the gap?

- A) There is no gap; nightly backups plus four-hour log backups satisfy any RPO under eight hours.
- B) The current backup frequency creates a gap of up to three hours and thirty minutes relative to the thirty-minute RPO.
- C) The nightly full backup satisfies the RPO because it captures all data from the prior day.
- D) The RPO gap only matters if the organization also has a short RTO for the same system.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The most recent transaction log backup could be up to four hours old at the time of failure. With an RPO of thirty minutes, the gap is four hours minus thirty minutes, or three hours and thirty minutes of unprotected transaction data.

- **Why A is incorrect:** Four-hour log backup intervals leave up to four hours of data at risk. An RPO of thirty minutes requires backup intervals no longer than thirty minutes.

- **Why C is incorrect:** Nightly full backups leave an entire day's worth of transactions potentially unrecoverable. That is far outside a thirty-minute RPO.

- **Why D is incorrect:** RPO is an independent metric from RTO. A gap in RPO is a problem regardless of the RTO value for the same system.

---

**Question 3**

During a BCP tabletop exercise, a facilitator presents an inject: the organization's primary data center has lost power and the generator has failed to start. The team discusses their response procedures. What is the primary limitation of this testing approach compared to a simulation exercise?

- A) Tabletop exercises cannot use realistic scenarios because they might alarm participants.
- B) Tabletop exercises do not validate whether procedures actually work in practice — they only test the team's conceptual understanding of the plan.
- C) Tabletop exercises are too expensive for most organizations to conduct regularly.
- D) Tabletop exercises require production systems to be taken offline, making them high-risk.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Tabletop exercises are discussion-based. They reveal whether the team understands the plan and can identify logical gaps, but they do not confirm that recovery tools, communication systems, or procedures will function as expected when actually executed.

- **Why A is incorrect:** Realistic scenarios are precisely the point of tabletop exercises. Facilitators routinely use scenarios involving major failures, ransomware, and physical disasters.

- **Why C is incorrect:** Tabletop exercises are among the least expensive BCP tests. Their low cost is one of the primary reasons they are recommended for quarterly or semi-annual frequency.

- **Why D is incorrect:** Tabletop exercises explicitly do not require activating or taking down production systems. That characteristic is what distinguishes them from simulation and full-interruption tests.

---

**Question 4**

A financial services firm's wire transfer system has an RTO of two hours and an MTPD of eight hours. During a full-interruption test, the team requires five hours to complete recovery. Which conclusion is most appropriate?

- A) The test is a success because recovery was completed within the MTPD of eight hours.
- B) The test reveals a gap — the actual recovery time exceeds the RTO, and the strategy requires remediation.
- C) The RTO should be revised upward to five hours to match actual capability.
- D) No action is required because RTO is a target, not a hard requirement.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** RTO is the maximum acceptable recovery time as defined by the business. Achieving recovery in five hours when the RTO is two hours means the current strategy fails to meet business requirements. The gap must be investigated and closed.

- **Why A is incorrect:** Completing recovery within MTPD does not mean the RTO was met. RTO is the primary objective; MTPD is the absolute ceiling. A recovery between RTO and MTPD still represents a failed RTO.

- **Why C is incorrect:** RTO is set by business impact, not by current technical capability. Adjusting the RTO to match a failing architecture avoids the real problem. The architecture must improve to meet the business-defined RTO.

- **Why D is incorrect:** RTO is a binding business requirement derived from the BIA. Treating it as optional defeats the purpose of the entire BIA and BCP process.

---

**Question 5**

An organization's BIA assigns the customer relationship management (CRM) system to Tier 3 — Important. Which continuity strategy is most appropriate for this classification?

- A) Active-active high availability with real-time synchronous replication.
- B) Hot standby alternate site with pre-staged hardware and live data mirroring.
- C) Manual workarounds supplemented by cloud-based backup and restore.
- D) No recovery strategy; Tier 3 systems are excluded from BCP scope.

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Tier 3 systems can tolerate one to several days of downtime. Manual workarounds bridge the gap during recovery, and cloud backup-and-restore brings the system back within the extended RTO. This approach is proportionate to the tier's risk level and cost constraints.

- **Why A is incorrect:** Active-active HA is appropriate for Tier 1 mission-critical systems with RTOs measured in seconds to minutes. Applying it to Tier 3 would be a significant overinvestment that misallocates security resources.

- **Why B is incorrect:** Hot standby is appropriate for Tier 1 or high-end Tier 2 systems. A Tier 3 system does not warrant the cost of maintained hot site infrastructure.

- **Why D is incorrect:** Tier 3 systems are in BCP scope — they simply receive lower-priority recovery strategies. Excluding them entirely would leave a gap for processes that, while not critical, still have value.

---

**Question 6**

Which of the following is a correct statement about the relationship between RTO and MTPD?

- A) RTO and MTPD are interchangeable terms for the same metric.
- B) MTPD is always less than RTO because it represents the minimum recovery threshold.
- C) RTO must be less than or equal to MTPD; the difference between them is the recovery safety margin.
- D) MTPD applies only to data systems, while RTO applies to business processes.

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** RTO is the planned recovery time objective. MTPD is the absolute maximum. RTO must not exceed MTPD, and the gap between them gives the organization a buffer if recovery takes longer than planned.

- **Why A is incorrect:** RTO and MTPD are distinct metrics. RTO is the target; MTPD is the ceiling. Conflating them is a common exam error.

- **Why B is incorrect:** MTPD is always greater than or equal to RTO, not less than. An MTPD shorter than RTO would mean the organization plans to recover after the point at which consequences are already irreversible.

- **Why D is incorrect:** Both RTO and MTPD apply to business processes, not just data systems. They are process-level metrics established through BIA, regardless of whether the process depends on technology.

---

**Question 7**

A retail company conducts its annual BCP review and discovers that the manager named as the alternate Business Continuity Coordinator left the company six months ago. No replacement has been named. Under which BCP maintenance category does this finding fall, and what is the appropriate corrective action?

- A) This is a test finding; the corrective action is to schedule a tabletop exercise to identify new candidates.
- B) This is a plan maintenance gap triggered by a personnel change; the corrective action is to name and document a replacement alternate coordinator immediately.
- C) This is acceptable because alternates are optional for non-critical roles.
- D) This is a technology gap; the corrective action is to update the identity management system to reflect the personnel change.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Changes in key personnel are a defined trigger for BCP review and update. Leaving a critical BCP role without a named alternate is a gap in the plan's roles and responsibilities section. The immediate corrective action is to name a replacement.

- **Why A is incorrect:** This is not a test finding — no test was conducted. It is a maintenance failure discovered during the annual review. A tabletop would not address the gap; updating the plan with a named alternate does.

- **Why C is incorrect:** Alternate designations for named BCP roles are not optional. Every key role must have a named backup precisely to handle situations where the primary is unavailable — including resignation.

- **Why D is incorrect:** While identity management may need updating, this is fundamentally a BCP document maintenance issue, not a technology gap. The primary corrective action is plan document update, not a system change.

---

**Question 8**

An organization is selecting a continuity strategy for its public-facing e-commerce website, which has an RTO of thirty minutes and generates $120,000 per hour in revenue. The annual cost of a hot standby architecture is $200,000. Which analysis framework best supports the investment decision?

- A) The hot standby cost exceeds annual IT budgets; decline the investment.
- B) Compare the annualized cost of the hot standby ($200,000) to the potential loss from exceeding the RTO. If one incident per year is plausible, the $120,000-per-hour revenue loss justifies the investment.
- C) Use MTPD to determine whether the cold site option could achieve the RTO instead.
- D) Escalate to legal to evaluate regulatory exposure before making any investment decision.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Strategy selection is a cost-benefit decision. At $120,000 per hour, even a two-hour outage costs $240,000 — exceeding the annual hot standby cost. The BIA-based business case supports the investment.

- **Why A is incorrect:** Budget constraints are a real consideration, but the decision must be risk-informed. Declining the investment without a cost-benefit analysis ignores the quantified financial impact from the BIA.

- **Why C is incorrect:** Cold sites typically require 24–72 hours to activate, which cannot achieve a thirty-minute RTO. MTPD does not change this constraint — the cold site strategy is architecturally incapable of meeting the RTO.

- **Why D is incorrect:** Regulatory exposure is one input to the decision, not the primary framework. The BIA cost-benefit analysis is the appropriate tool for strategy investment decisions.

---

**Question 9**

Which of the following events does NOT typically trigger an immediate unscheduled BCP review?

- A) The organization completes a major acquisition that doubles its employee count and adds three new data centers.
- B) A key vendor providing hosted backup services is acquired by a competitor.
- C) A new intern joins the IT help desk.
- D) A post-incident review reveals that the emergency notification system failed to reach thirty percent of staff during a drill.

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Routine personnel additions at non-critical levels do not trigger BCP review. An intern joining the help desk has no material impact on BCP assumptions, dependencies, or named roles.

- **Why A is incorrect:** A major acquisition fundamentally changes the organization's scope, systems, and personnel — all of which are BCP triggers. An immediate review is required.

- **Why B is incorrect:** A vendor acquisition may affect the service terms, reliability, and contractual protections associated with the backup service. This change in vendor status triggers a review of the relevant BCP dependencies and contracts.

- **Why D is incorrect:** A post-incident review that reveals a thirty-percent failure rate in emergency notifications is a critical finding that requires immediate plan update. Communication procedure failures are among the most serious BCP gaps.

---

**Question 10**

A manufacturing company is documenting its BCP for the first time. The team has completed the BIA and established RTOs. The project manager suggests that once the plan is written and approved, it can be filed and only reviewed if an incident occurs. What is the fundamental flaw in this approach?

- A) BCP documents should never be filed — they must be memorized by all staff.
- B) A plan that is not tested and not regularly reviewed will contain gaps and outdated information that may cause the plan to fail during an actual incident.
- C) Plans approved by senior management do not require subsequent review because approval implies ongoing accuracy.
- D) Once established, RTOs do not change, so the plan remains accurate without maintenance.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** BCP is a living program, not a one-time document. Organizations change — technology changes, personnel change, processes change, regulations change. A plan last reviewed at inception will almost certainly contain errors, omissions, and outdated contacts by the time of an actual incident.

- **Why A is incorrect:** Filing and distributing BCP documents is appropriate. The issue is not filing — it is the absence of regular review, testing, and update cycles.

- **Why C is incorrect:** Management approval at a point in time does not confer ongoing accuracy. Approval authorizes the current version; it imposes no guarantee about future accuracy.

- **Why D is incorrect:** RTOs are set by business impact, and business impact changes as revenue, regulatory requirements, and customer expectations evolve. RTOs should be reassessed during each annual BIA review.
