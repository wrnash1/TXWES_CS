# Quiz: Module 13 — Business Continuity Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

### Question 1

An organization conducts a Business Impact Analysis and determines that its order management system generates $45,000 in revenue per hour. Regulatory penalties for service unavailability begin accruing at the six-hour mark. Reputational harm becomes significant at twelve hours. Which metric does this timeline analysis most directly establish?

- A) Recovery Point Objective (RPO)
- B) Maximum Tolerable Period of Disruption (MTPD)
- C) Work Recovery Time (WRT)
- D) Service Level Agreement (SLA) threshold

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The impact timeline identifies the point at which consequences become unacceptable — that is the definition of MTPD. The analysis reveals the absolute ceiling on downtime, which sets MTPD.

- **Why A is incorrect:** RPO concerns maximum acceptable data loss, not the duration of service unavailability. The impact timeline described measures downtime impact, not data freshness requirements.

- **Why C is incorrect:** WRT is the time needed to reconcile data after systems are restored — a post-recovery metric, not derived from financial/regulatory impact analysis.

- **Why D is incorrect:** SLA thresholds are contractual commitments to external parties. MTPD is an internal business analysis metric derived from operational and financial impact.

---

### Question 2

A hospital's EHR system has an RPO of thirty minutes. The current backup architecture performs full backups nightly and transaction log backups every four hours. Which statement accurately describes the gap?

- A) There is no gap; nightly backups plus four-hour log backups satisfy any RPO under eight hours.
- B) The current backup frequency creates a gap of up to three hours and thirty minutes relative to the thirty-minute RPO.
- C) The nightly full backup satisfies the RPO because it captures all data from the prior day.
- D) The RPO gap only matters if the organization also has a short RTO for the same system.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The most recent transaction log backup could be up to four hours old at the time of failure. With an RPO of thirty minutes, the gap is four hours minus thirty minutes, or three hours and thirty minutes of unprotected transaction data.

- **Why A is incorrect:** Four-hour log backup intervals leave up to four hours of data at risk. An RPO of thirty minutes requires backup intervals no longer than thirty minutes.

- **Why C is incorrect:** Nightly full backups leave an entire day's worth of transactions potentially unrecoverable. That is far outside a thirty-minute RPO.

- **Why D is incorrect:** RPO is an independent metric from RTO. A gap in RPO is a problem regardless of the RTO value for the same system.

---

### Question 3

During a BCP tabletop exercise, a facilitator presents an inject: the organization's primary data center has lost power and the generator has failed to start. The team discusses their response procedures. What is the primary limitation of this testing approach compared to a simulation exercise?

- A) Tabletop exercises cannot use realistic scenarios because they might alarm participants.
- B) Tabletop exercises do not validate whether procedures actually work in practice — they only test the team's conceptual understanding of the plan.
- C) Tabletop exercises are too expensive for most organizations to conduct regularly.
- D) Tabletop exercises require production systems to be taken offline, making them high-risk.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Tabletop exercises are discussion-based. They reveal whether the team understands the plan and can identify logical gaps, but they do not confirm that recovery tools, communication systems, or procedures will function as expected when actually executed.

- **Why A is incorrect:** Realistic scenarios are precisely the point of tabletop exercises. Facilitators routinely use scenarios involving major failures, ransomware, and physical disasters.

- **Why C is incorrect:** Tabletop exercises are among the least expensive BCP tests. Their low cost is one of the primary reasons they are recommended for quarterly or semi-annual frequency.

- **Why D is incorrect:** Tabletop exercises explicitly do not require activating or taking down production systems. That characteristic is what distinguishes them from simulation and full-interruption tests.

---

### Question 4

A financial services firm's wire transfer system has an RTO of two hours and an MTPD of eight hours. During a full-interruption test, the team requires five hours to complete recovery. Which conclusion is most appropriate?

- A) The test is a success because recovery was completed within the MTPD of eight hours.
- B) The test reveals a gap — the actual recovery time exceeds the RTO, and the strategy requires remediation.
- C) The RTO should be revised upward to five hours to match actual capability.
- D) No action is required because RTO is a target, not a hard requirement.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** RTO is the maximum acceptable recovery time as defined by the business. Achieving recovery in five hours when the RTO is two hours means the current strategy fails to meet business requirements. The gap must be investigated and closed.

- **Why A is incorrect:** Completing recovery within MTPD does not mean the RTO was met. RTO is the primary objective; MTPD is the absolute ceiling. A recovery between RTO and MTPD still represents a failed RTO.

- **Why C is incorrect:** RTO is set by business impact, not by current technical capability. Adjusting the RTO to match a failing architecture avoids the real problem. The architecture must improve to meet the business-defined RTO.

- **Why D is incorrect:** RTO is a binding business requirement derived from the BIA. Treating it as optional defeats the purpose of the entire BIA and BCP process.

---

### Question 5

An organization's BIA assigns the customer relationship management (CRM) system to Tier 3 — Important. Which continuity strategy is most appropriate for this classification?

- A) Active-active high availability with real-time synchronous replication.
- B) Hot standby alternate site with pre-staged hardware and live data mirroring.
- C) Manual workarounds supplemented by cloud-based backup and restore.
- D) No recovery strategy; Tier 3 systems are excluded from BCP scope.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** Tier 3 systems can tolerate one to several days of downtime. Manual workarounds bridge the gap during recovery, and cloud backup-and-restore brings the system back within the extended RTO. This approach is proportionate to the tier's risk level and cost constraints.

- **Why A is incorrect:** Active-active HA is appropriate for Tier 1 mission-critical systems with RTOs measured in seconds to minutes. Applying it to Tier 3 would be a significant overinvestment that misallocates security resources.

- **Why B is incorrect:** Hot standby is appropriate for Tier 1 or high-end Tier 2 systems. A Tier 3 system does not warrant the cost of maintained hot site infrastructure.

- **Why D is incorrect:** Tier 3 systems are in BCP scope — they simply receive lower-priority recovery strategies. Excluding them entirely would leave a gap for processes that, while not critical, still have value.

---

### Question 6

Which of the following is a correct statement about the relationship between RTO and MTPD?

- A) RTO and MTPD are interchangeable terms for the same metric.
- B) MTPD is always less than RTO because it represents the minimum recovery threshold.
- C) RTO must be less than or equal to MTPD; the difference between them is the recovery safety margin.
- D) MTPD applies only to data systems, while RTO applies to business processes.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** RTO is the planned recovery time objective. MTPD is the absolute maximum. RTO must not exceed MTPD, and the gap between them gives the organization a buffer if recovery takes longer than planned.

- **Why A is incorrect:** RTO and MTPD are distinct metrics. RTO is the target; MTPD is the ceiling. Conflating them is a common exam error.

- **Why B is incorrect:** MTPD is always greater than or equal to RTO, not less than. An MTPD shorter than RTO would mean the organization plans to recover after the point at which consequences are already irreversible.

- **Why D is incorrect:** Both RTO and MTPD apply to business processes, not just data systems. They are process-level metrics established through BIA, regardless of whether the process depends on technology.

---

### Question 7

A retail company conducts its annual BCP review and discovers that the manager named as the alternate Business Continuity Coordinator left the company six months ago. No replacement has been named. Under which BCP maintenance category does this finding fall, and what is the appropriate corrective action?

- A) This is a test finding; the corrective action is to schedule a tabletop exercise to identify new candidates.
- B) This is a plan maintenance gap triggered by a personnel change; the corrective action is to name and document a replacement alternate coordinator immediately.
- C) This is acceptable because alternates are optional for non-critical roles.
- D) This is a technology gap; the corrective action is to update the identity management system to reflect the personnel change.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Changes in key personnel are a defined trigger for BCP review and update. Leaving a critical BCP role without a named alternate is a gap in the plan's roles and responsibilities section. The immediate corrective action is to name a replacement.

- **Why A is incorrect:** This is not a test finding — no test was conducted. It is a maintenance failure discovered during the annual review. A tabletop would not address the gap; updating the plan with a named alternate does.

- **Why C is incorrect:** Alternate designations for named BCP roles are not optional. Every key role must have a named backup precisely to handle situations where the primary is unavailable — including resignation.

- **Why D is incorrect:** While identity management may need updating, this is fundamentally a BCP document maintenance issue, not a technology gap. The primary corrective action is plan document update, not a system change.

---

### Question 8

An organization is selecting a continuity strategy for its public-facing e-commerce website, which has an RTO of thirty minutes and generates $120,000 per hour in revenue. The annual cost of a hot standby architecture is $200,000. Which analysis framework best supports the investment decision?

- A) The hot standby cost exceeds annual IT budgets; decline the investment.
- B) Compare the annualized cost of the hot standby ($200,000) to the potential loss from exceeding the RTO. If one incident per year is plausible, the $120,000-per-hour revenue loss justifies the investment.
- C) Use MTPD to determine whether the cold site option could achieve the RTO instead.
- D) Escalate to legal to evaluate regulatory exposure before making any investment decision.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Strategy selection is a cost-benefit decision. At $120,000 per hour, even a two-hour outage costs $240,000 — exceeding the annual hot standby cost. The BIA-based business case supports the investment.

- **Why A is incorrect:** Budget constraints are a real consideration, but the decision must be risk-informed. Declining the investment without a cost-benefit analysis ignores the quantified financial impact from the BIA.

- **Why C is incorrect:** Cold sites typically require 24–72 hours to activate, which cannot achieve a thirty-minute RTO. MTPD does not change this constraint — the cold site strategy is architecturally incapable of meeting the RTO.

- **Why D is incorrect:** Regulatory exposure is one input to the decision, not the primary framework. The BIA cost-benefit analysis is the appropriate tool for strategy investment decisions.

---

### Question 9

Which of the following events does NOT typically trigger an immediate unscheduled BCP review?

- A) The organization completes a major acquisition that doubles its employee count and adds three new data centers.
- B) A key vendor providing hosted backup services is acquired by a competitor.
- C) A new intern joins the IT help desk.
- D) A post-incident review reveals that the emergency notification system failed to reach thirty percent of staff during a drill.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** Routine personnel additions at non-critical levels do not trigger BCP review. An intern joining the help desk has no material impact on BCP assumptions, dependencies, or named roles.

- **Why A is incorrect:** A major acquisition fundamentally changes the organization's scope, systems, and personnel — all of which are BCP triggers. An immediate review is required.

- **Why B is incorrect:** A vendor acquisition may affect the service terms, reliability, and contractual protections associated with the backup service. This change in vendor status triggers a review of the relevant BCP dependencies and contracts.

- **Why D is incorrect:** A post-incident review that reveals a thirty-percent failure rate in emergency notifications is a critical finding that requires immediate plan update. Communication procedure failures are among the most serious BCP gaps.

---

### Question 10

A manufacturing company is documenting its BCP for the first time. The team has completed the BIA and established RTOs. The project manager suggests that once the plan is written and approved, it can be filed and only reviewed if an incident occurs. What is the fundamental flaw in this approach?

- A) BCP documents should never be filed — they must be memorized by all staff.
- B) A plan that is not tested and not regularly reviewed will contain gaps and outdated information that may cause the plan to fail during an actual incident.
- C) Plans approved by senior management do not require subsequent review because approval implies ongoing accuracy.
- D) Once established, RTOs do not change, so the plan remains accurate without maintenance.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** BCP is a living program, not a one-time document. Organizations change — technology changes, personnel change, processes change, regulations change. A plan last reviewed at inception will almost certainly contain errors, omissions, and outdated contacts by the time of an actual incident.

- **Why A is incorrect:** Filing and distributing BCP documents is appropriate. The issue is not filing — it is the absence of regular review, testing, and update cycles.

- **Why C is incorrect:** Management approval at a point in time does not confer ongoing accuracy. Approval authorizes the current version; it imposes no guarantee about future accuracy.

- **Why D is incorrect:** RTOs are set by business impact, and business impact changes as revenue, regulatory requirements, and customer expectations evolve. RTOs should be reassessed during each annual BIA review.

---

### Question 11 (5 points)

An organization's BIA identifies that its payroll processing system must be restored within four hours of a disruption to avoid employee payment failures and regulatory penalties. The organization currently relies on a single on-premises server with no redundancy. Which single statement best describes the relationship between this BIA finding and the required continuity strategy?

- A) The four-hour RTO is aspirational; actual recovery time is dictated by the available technology budget, not the BIA finding.
- B) The BIA finding establishes a binding RTO of four hours that the continuity strategy must be architecturally capable of meeting — any strategy with a typical recovery time exceeding four hours is disqualified.
- C) The BIA finding only applies when the disruption is caused by a natural disaster; for hardware failures, a different RTO applies.
- D) Because the system is on-premises, cloud-based continuity strategies cannot be considered regardless of cost or recovery speed.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The BIA establishes RTOs as business requirements — not aspirational targets. The continuity strategy selected must be architecturally capable of meeting the RTO under the assumed failure scenarios. Any architecture that cannot reliably recover within four hours fails to satisfy the BIA requirement.

- **Why A is incorrect:** The BIA derives RTOs from business impact — financial loss, regulatory exposure, and operational consequence — not from technology budgets. Budget constraints may require risk acceptance or staged investment, but they do not change the RTO as a business requirement.

- **Why C is incorrect:** RTOs are not scoped to specific disruption causes. The RTO represents the maximum tolerable downtime regardless of why the system is unavailable. An RTO of four hours applies whether the disruption is a hardware failure, cyberattack, or natural disaster.

- **Why D is incorrect:** Physical location of existing infrastructure does not restrict continuity strategy options. Cloud-based recovery options — backup-and-restore, pilot light, warm standby — are all viable considerations for on-premises systems and are frequently used in hybrid continuity architectures.

---

### Question 12 (5 points)

A business continuity coordinator is building the BCP document for a regional insurance company. She is completing the "Dependencies and Single Points of Failure" section. Which of the following most accurately describes the purpose of this section?

- A) To list all vendors the organization uses, ranked by annual spend.
- B) To document all technical systems and external services that critical business processes depend on, and identify where a single failure would interrupt multiple processes simultaneously.
- C) To catalog the organization's IT asset inventory for use in hardware refresh planning.
- D) To identify regulatory requirements that apply to each critical business process.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The dependencies section maps the upstream inputs and downstream consumers of each critical process. Single points of failure — a single internet provider serving all branches, a single authentication server shared by fifteen applications — represent concentrated risk where one failure cascades across multiple processes. Identifying them is essential to strategy selection and gap remediation.

- **Why A is incorrect:** Vendor spend ranking is a procurement management function, not a BCP dependency analysis. The relevance of a vendor to the BCP is determined by the criticality of the services they provide to recovery, not by spend amount.

- **Why C is incorrect:** IT asset inventory is a configuration management and IT service management function. While asset data may feed the BCP, the dependencies section specifically focuses on process-level input-output relationships and failure cascades, not hardware cataloging.

- **Why D is incorrect:** Regulatory requirements are captured elsewhere in the BCP, typically in the scope and compliance section. The dependencies section focuses on operational and technical interdependencies that affect recovery execution.

---

### Question 13 (5 points)

An organization running an e-commerce platform completes a BIA and establishes an RPO of fifteen minutes for its order database. The current architecture uses asynchronous replication to a warm standby with a five-minute replication lag. A brief network interruption during peak traffic causes the replication to fall thirty minutes behind before the network recovers. What is the most accurate assessment of this situation?

- A) There is no RPO risk because replication eventually caught up and no failover occurred.
- B) The thirty-minute replication lag during the network interruption constitutes a transient RPO violation — if a failover had been triggered during that window, up to thirty minutes of orders could have been lost, exceeding the fifteen-minute RPO.
- C) The five-minute normal replication lag already satisfies the fifteen-minute RPO, making any transient lag irrelevant.
- D) Asynchronous replication cannot satisfy any RPO under sixty minutes and should be replaced with synchronous replication.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** RPO is the maximum acceptable data loss at the time of failover. During the network interruption, replication lag reached thirty minutes — double the fifteen-minute RPO. If a catastrophic failure had forced failover during that window, the organization would have lost thirty minutes of order data. The transient violation is a real and reportable risk event, even though no failover occurred.

- **Why A is incorrect:** The RPO risk existed during the entire period when lag exceeded fifteen minutes. Whether a failover was triggered is separate from whether the RPO was in jeopardy. Risk management requires recognizing the exposure window, not just whether harm materialized.

- **Why C is incorrect:** Normal operating lag is not the same as maximum lag under stress. The architecture must be evaluated against worst-case lag during degraded conditions, not just typical performance. An RPO analysis that only considers normal operations is incomplete.

- **Why D is incorrect:** Asynchronous replication can satisfy short RPOs when network latency is low and replication lag is well-managed. Synchronous replication guarantees zero data loss but introduces write latency and is not universally required for all RPO targets. The appropriate solution here is monitoring and alerting on replication lag, not necessarily switching to synchronous replication.

---

### Question 14 (5 points)

NIST SP 800-34 Rev. 1 defines several plan types within an organization's continuity framework. Which statement correctly distinguishes a Business Continuity Plan (BCP) from a Disaster Recovery Plan (DRP)?

- A) The BCP covers only IT systems; the DRP covers all business processes including manual operations.
- B) The BCP focuses on sustaining critical business functions during a disruption; the DRP focuses specifically on restoring IT systems and technical infrastructure after a disruption.
- C) The BCP and DRP are interchangeable terms for the same document under NIST guidance.
- D) The DRP is approved by the board; the BCP is approved by the CISO.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** NIST SP 800-34 defines the BCP as the overarching plan for maintaining critical mission-essential functions during any disruption, while the DRP addresses recovery of IT systems, networks, and data after a disruption. The BCP is business-process-focused and broader; the DRP is IT-focused and more technical. The DRP is typically a component or subordinate plan within the overall BCP framework.

- **Why A is incorrect:** This reverses the correct relationship. The BCP is the broader business-oriented plan that may include manual workarounds, alternate work locations, and human resource procedures — not limited to IT. The DRP is the IT-focused subset.

- **Why C is incorrect:** BCP and DRP are distinct plan types with different scopes and owners. NIST SP 800-34 explicitly defines them separately. Treating them as interchangeable creates governance gaps — particularly for non-IT business processes that require continuity planning but are not addressed in a purely technical DRP.

- **Why D is incorrect:** Approval authority for BCP and DRP documents is not defined by whether they are a BCP or DRP — it is determined by the organization's governance structure. Both typically require senior management or executive approval. The CISO is typically responsible for the DRP, while the BCP may have broader business ownership.

---

### Question 15 (5 points)

A healthcare organization's BCP designates the cafeteria as an alternate work location for the medical records department in the event the main office building is unavailable. During an exercise, the team discovers that the cafeteria has no wired network connections, no computers, and no phone lines. What BCP planning failure does this scenario most directly represent?

- A) A failure in the scope and purpose section — the cafeteria was not listed as an approved facility.
- B) A failure in the continuity strategy — the alternate work location was selected without validating that it has the infrastructure and resources required to support the designated functions.
- C) A failure in the test schedule — the organization should have tested the alternate location monthly.
- D) A failure in the emergency communication plan — staff were not notified of the cafeteria designation early enough.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Selecting an alternate work location requires validating that the location has the physical infrastructure, technology, communications, and access controls needed to support the critical functions assigned to it. Naming a location without conducting a site assessment is a strategy failure — the location exists on paper but cannot support recovery in practice.

- **Why A is incorrect:** The scope and purpose section describes what the BCP covers at a high level. Whether the cafeteria is listed in a scope section is not the core failure — the core failure is that the strategy designated a location that cannot support the required operations.

- **Why C is incorrect:** Monthly testing would have revealed the gap sooner, but the underlying failure is the strategy — not the test frequency. Even with more frequent testing, the root cause would remain the same: an alternate location was designated without infrastructure validation.

- **Why D is incorrect:** Communication failures relate to notifying staff during an incident. The scenario describes an infrastructure gap at the designated site, not a communication timing issue. Even with perfect communication, staff arriving at the cafeteria would find they cannot perform their work.

---

### Question 16 (5 points)

An organization's senior management decides to accept the risk of not investing in a hot standby site for its secondary billing system, which has an established RTO of six hours. Management documents the decision and signs off on the risk acceptance. From a BCP governance perspective, which statement best characterizes this decision?

- A) This is a governance failure because management should never accept risk above a defined RTO.
- B) This is an appropriate risk management decision provided it is documented, approved at the correct authority level, and the residual risk is communicated to all affected stakeholders.
- C) Risk acceptance is not a valid BCP option — the organization must invest in a recovery strategy for all systems with a defined RTO.
- D) The signed risk acceptance eliminates any regulatory liability for failing to recover within the RTO.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Risk acceptance is a legitimate risk treatment option when the cost of a control exceeds the expected loss from the risk being accepted, or when resource constraints require prioritization. The CISM framework recognizes risk acceptance as valid — but it must be documented, approved at the appropriate authority level (typically senior management or above), and communicated to affected stakeholders so they can plan accordingly.

- **Why A is incorrect:** Management has both the authority and the responsibility to make risk acceptance decisions. Not every BCP gap must be remediated — organizations operate under resource constraints and must make trade-off decisions. The governance requirement is that such decisions be made explicitly, documented, and owned.

- **Why C is incorrect:** Risk acceptance is explicitly recognized as one of four risk treatment strategies (accept, avoid, mitigate, transfer) in both CISM and ISO 31000. Requiring investment in a recovery strategy for every system regardless of cost-benefit analysis would be operationally unsustainable.

- **Why D is incorrect:** Documented risk acceptance does not eliminate regulatory liability. Regulators evaluate whether the organization met its legal obligations — not whether it documented a decision. A regulatory requirement to recover within a defined timeframe cannot be waived by internal risk acceptance documentation.

---

### Question 17 (5 points)

A company's BCP states that its emergency notification system will reach all 2,400 employees within thirty minutes of a declared crisis event. During an unannounced drill, the system successfully contacts only 1,850 employees within thirty minutes; 550 employees are not reached due to outdated phone numbers and deactivated email addresses in the notification system. What is the most appropriate corrective action?

- A) Accept the 77% notification rate as adequate because most employees were reached.
- B) Conduct a quarterly review of the emergency notification contact database to remove departed employees and update changed contact details, and validate the thirty-minute target against the corrected roster.
- C) Replace the emergency notification system with a newer platform that has a higher delivery success rate.
- D) Reduce the notification target from thirty minutes to sixty minutes to make the target more achievable with the current contact data quality.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The root cause of the notification failure is data quality — outdated contact information for departed or changed employees. The correct fix is a process to maintain the notification database with current records tied to the HR offboarding and change process. Quarterly reconciliation against active employee records is the standard approach. The thirty-minute target should be revalidated after the database is corrected.

- **Why A is incorrect:** A 77% notification rate means more than one in five employees was not reached during an emergency. Accepting this rate creates risk that critical staff — including those with BCP roles — may not be notified in time to execute their responsibilities. The BCP target of 100% contact attempt within thirty minutes is a governance requirement, not a suggestion.

- **Why C is incorrect:** The failure is not caused by platform limitations — it is caused by data quality. Replacing the platform without fixing the contact database would reproduce the same failure on a new system. Technology cannot compensate for a data governance gap.

- **Why D is incorrect:** Reducing the target to match current poor performance normalizes the data quality failure rather than fixing it. Notification targets should be set by what the business requires — how quickly employees need to be mobilized — not by what the current process can achieve with degraded data.

---

### Question 18 (5 points)

An organization's BCP calls for relocation to an alternate site within four hours of a disaster declaration. The plan specifies that employees will drive to the alternate site, which is located forty-five miles from the primary location. Which risk to this strategy is most likely to go unaddressed if the BCP team does not conduct a realistic exercise?

- A) The risk that employees will not know their assigned roles at the alternate site.
- B) The risk that a large-scale regional disaster — the type most likely to trigger site relocation — may make roads impassable or create traffic conditions that prevent employees from reaching the alternate site within four hours.
- C) The risk that the alternate site's internet connection will be slower than the primary site.
- D) The risk that employees will forget their login credentials when working from an unfamiliar location.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** A regional disaster severe enough to render the primary site unusable — such as a major hurricane, earthquake, or regional flooding — is also likely to affect roads, create mass evacuation traffic, or prevent travel entirely. A BCP that assumes employees can individually drive forty-five miles within four hours during a regional disaster has not been stress-tested against the scenarios most likely to trigger it. This assumption failure is a classic gap revealed only through realistic scenario exercises.

- **Why A is incorrect:** Role clarity is an important training concern and would likely surface during any tabletop or simulation exercise. It is not specifically a transportation or logistics assumption gap.

- **Why C is incorrect:** Bandwidth at the alternate site is an infrastructure validation issue that should be addressed during site setup and periodic technical testing — not a scenario-specific exercise finding unique to regional disaster scenarios.

- **Why D is incorrect:** Credential management for alternate site access is a technical control issue — typically addressed through documented access provisioning procedures and credential vaulting — not a scenario-specific exercise finding tied to the transportation assumption.

---

### Question 19 (5 points)

An organization conducts a Business Impact Analysis and identifies that its customer service call center generates $8,000 per hour in revenue, but the BIA team assigns the call center an RTO of seventy-two hours. The BIA facilitator notes this seems inconsistent. Which BIA factor was most likely overlooked or underweighted that would justify a much shorter RTO?

- A) The cost of the BCP strategy needed to achieve a shorter RTO.
- B) The cumulative financial impact over the seventy-two-hour window — at $8,000 per hour, the organization would lose $576,000 before recovery — plus potential regulatory, contractual, and reputational impacts that compound over time.
- C) The number of employees in the call center who would need to be relocated during a disruption.
- D) The difficulty of implementing a hot standby strategy for telephony systems.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The BIA must quantify the cumulative financial impact over the recovery window, not just the hourly rate. At $8,000 per hour over seventy-two hours, the total direct loss would be $576,000 — before accounting for regulatory penalties, SLA breach penalties, reputational damage, and customer churn. When these factors are fully quantified, a seventy-two-hour RTO for an $8,000-per-hour process is extremely difficult to justify. The BIA team likely analyzed the hourly rate in isolation without accumulating total impact.

- **Why A is incorrect:** Strategy cost is a factor in strategy selection after the RTO is established — it is not a factor in determining the RTO itself. The RTO must be set by business impact, not by what the organization is willing to spend. Budget constraints affect strategy choice, not the business requirement.

- **Why C is incorrect:** Staffing requirements affect alternate work location planning and are an important BCP consideration, but they do not determine the RTO. The RTO is set by the financial, regulatory, and operational consequences of downtime.

- **Why D is incorrect:** Implementation difficulty is a strategy consideration, not a BIA factor. The BIA identifies requirements; strategy selection later addresses how to meet them within technical and budget constraints. If telephony recovery is difficult, that may affect strategy selection, but it should not inflate the RTO beyond what the business can tolerate.

---

### Question 20 (5 points)

A manufacturing company's BCP includes a mutual aid agreement with a competitor, under which each company agrees to share production capacity during a disaster. Six months after the BCP is finalized, the competitor acquires a new product line that is now in direct competition with the manufacturing company's core business. Which BCP maintenance action is most appropriate?

- A) No action is required because the mutual aid agreement was legally executed and remains binding regardless of competitive changes.
- B) The manufacturing company should review whether the competitive change creates intellectual property, confidentiality, or conflict-of-interest risks that would make the mutual aid arrangement untenable, and update or terminate the agreement accordingly.
- C) The manufacturing company should immediately terminate the mutual aid agreement without review because sharing facilities with a direct competitor is always inappropriate.
- D) The mutual aid agreement should be renegotiated only at the next scheduled annual BCP review, as competitive changes do not constitute an unscheduled review trigger.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** A significant change in the competitive relationship between the parties is a material change to the assumptions under which the mutual aid agreement was formed. The BCP team must assess whether sharing production capacity now creates risks — exposure of proprietary processes, access to trade secrets, conflict of interest — that did not exist when the agreement was established. This review may result in the agreement being amended, supplemented with confidentiality protections, or terminated and replaced with an alternative continuity strategy.

- **Why A is incorrect:** Legal enforceability and operational advisability are separate questions. A binding agreement may still be inadvisable to exercise if doing so creates business harm. The BCP must be updated to reflect changed circumstances, even if the legal document remains technically valid.

- **Why C is incorrect:** Immediate termination without review is an overreaction. The appropriate action is analysis — the competitive overlap may be limited enough that the agreement remains viable with added confidentiality controls. Terminating without analysis and a replacement strategy could leave the organization without a viable continuity option.

- **Why D is incorrect:** A material change in a key third-party relationship — particularly one that affects the viability of a core continuity strategy — is a recognized trigger for an unscheduled BCP review. Waiting for the annual review cycle when a strategy may now be untenable is a governance failure.
