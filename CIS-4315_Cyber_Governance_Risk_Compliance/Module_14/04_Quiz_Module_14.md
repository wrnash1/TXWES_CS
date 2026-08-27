# Quiz: Module 14 — Disaster Recovery Management

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

### Question 1

An organization's customer-facing web application has an RTO of ninety minutes. The DR team is evaluating alternate site options. Which option is most consistent with this RTO requirement?

- A) Cold site with pre-negotiated hardware delivery within seventy-two hours.
- B) Warm site requiring four to eight hours to restore from the most recent backup.
- C) Hot site with real-time data replication and pre-staged servers capable of accepting traffic within thirty minutes of failover.
- D) Cloud backup-and-restore approach with an estimated two to four hour restore window.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** A ninety-minute RTO requires near-instantaneous recovery capability. A hot site with real-time replication and pre-staged infrastructure can achieve failover in thirty minutes — within the ninety-minute window. This is the only option that is architecturally capable of meeting the stated RTO.

- **Why A is incorrect:** A cold site with seventy-two-hour hardware delivery is architecturally incapable of a ninety-minute RTO. Cold sites are appropriate only for systems with RTOs of days to weeks.

- **Why B is incorrect:** A warm site requiring four to eight hours to restore exceeds the ninety-minute RTO. Warm sites are appropriate for systems with RTOs of two to twenty-four hours.

- **Why D is incorrect:** Cloud backup-and-restore has an estimated RTO of two to four hours, which also exceeds the ninety-minute requirement. Backup-and-restore is equivalent to a cold site approach.

---

### Question 2

During a DR failover procedure, the recovery team has completed site notification and assembled the team. The next step in the sequence is to verify whether the available data at the DR site meets the RPO target before redirecting production traffic. The team discovers the most recent replication snapshot is six hours old, while the RPO is two hours. What is the most appropriate action?

- A) Proceed immediately with network redirection because any data is better than none.
- B) Escalate to the decision authority and document the out-of-RPO condition before deciding whether to proceed.
- C) Cancel the failover and wait until the primary site is restored.
- D) Restore from the six-hour snapshot without notifying anyone, since users will not notice missing transactions.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Proceeding with data that is outside the RPO window may expose the organization to additional business impact, legal liability, or regulatory non-compliance. The decision to accept the out-of-RPO condition must be made by an authorized decision-maker, documented, and managed consciously — not unilaterally by the recovery team.

- **Why A is incorrect:** Proceeding without escalation removes the decision authority from the appropriate level. The recovery team does not have unilateral authorization to accept an RPO violation.

- **Why C is incorrect:** Canceling the failover entirely may cause the organization to exceed its MTPD while waiting for primary site recovery. The decision to cancel requires the same escalation as the decision to proceed with out-of-RPO data.

- **Why D is incorrect:** Concealing a known RPO violation from management is a governance failure and potentially a compliance violation. Missing transactions may have financial, legal, or operational consequences that management must address.

---

### Question 3

An organization conducts a DR test in which the recovery environment is fully activated and validated while the primary production environment remains live and operational. Users are not affected. Which test type is this?

- A) Full cutover test.
- B) Document review.
- C) Parallel test.
- D) Walkthrough test.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** A parallel test activates the recovery environment simultaneously with the live production environment. Both run at the same time, allowing the team to validate DR procedures and environment readiness without any risk to production availability.

- **Why A is incorrect:** A full cutover test redirects production traffic to the DR environment and takes the primary environment offline. Users are affected during a full cutover test.

- **Why B is incorrect:** A document review involves reading and evaluating the DR plan without activating any systems. No recovery environment is launched during a document review.

- **Why D is incorrect:** A walkthrough (structured walkthrough) has team members step through procedures verbally without executing them. No systems are activated.

---

### Question 4

A company migrates to AWS and implements the following DR architecture: a minimal set of core database replicas always running in a secondary AWS region, with EC2 launch templates configured but no running instances. On failover, the team launches instances from the templates and scales the database replicas to production capacity. Which AWS DR pattern does this describe?

- A) Multi-site active-active.
- B) Backup and restore.
- C) Warm standby.
- D) Pilot light.

Correct Answer: D

Distractor Analysis:

- **Why D is correct:** Pilot light keeps only the critical core — typically databases — running continuously in a secondary region. Compute instances are not pre-launched but can be started quickly from pre-configured templates. This distinguishes pilot light from warm standby (which has compute running at reduced scale) and from backup-and-restore (which provisions everything on demand).

- **Why A is incorrect:** Multi-site active-active runs full production capacity simultaneously in multiple regions. There are no standby or scaled-down components — both regions actively handle traffic.

- **Why B is incorrect:** Backup and restore provisions everything from scratch on failover — no compute or database infrastructure is pre-running in the recovery region. Pilot light is more capable than backup-and-restore because the database core is already running.

- **Why C is incorrect:** Warm standby runs a fully functional scaled-down replica — including compute instances — in the secondary region at all times. Pilot light does not run compute instances continuously; it only keeps the minimal database core running.

---

### Question 5

A company takes weekly full backups on Sunday and daily incremental backups Monday through Saturday. A server failure occurs on Friday afternoon. Describe the restore procedure.

- A) Restore only the most recent Saturday incremental, which contains all data since the prior Sunday.
- B) Restore the Sunday full backup, then apply Monday, Tuesday, Wednesday, Thursday, and Friday incrementals in sequence.
- C) Restore the Sunday full backup and then apply only the most recent differential backup.
- D) Restore only the Sunday full backup; incremental backups are not needed if the full backup is recent.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Incremental backup recovery requires the full backup plus every incremental in the chain from the last full backup to the most recent incremental before the failure. Each incremental captures only changes since the previous backup — they must be applied in order to reconstruct the complete data set.

- **Why A is incorrect:** Each incremental backup captures only the changes made since the previous day's backup, not all changes since the last full backup. The Friday incremental alone contains only Friday's changes — not the accumulated changes from Monday through Thursday.

- **Why C is incorrect:** Differential backups are not the same as incremental backups. The scenario specifies daily incrementals. Differential backups capture all changes since the last full backup — incrementals do not. Applying differential restore logic to incremental backups produces an incorrect restore.

- **Why D is incorrect:** A full backup alone recovers the state as of the last full backup — Sunday in this case. Any data created or changed Monday through Friday would be lost. The incrementals are essential to recovering the intervening changes.

---

### Question 6

An organization's DR plan specifies a two-hour RTO for its critical ERP system. During a full cutover test, the recovery team spends forty-five minutes waiting for authorization from the CTO, who was traveling and difficult to reach. The actual technical recovery took fifty minutes. Total elapsed time was ninety-five minutes, which technically meets the two-hour RTO. Which improvement addresses the most significant risk revealed by this test?

- A) Upgrade the ERP server hardware at the DR site to reduce the technical recovery time to thirty minutes.
- B) Define pre-authorization criteria that allow the recovery team to begin failover without waiting for the CTO's explicit approval.
- C) Reduce the RTO to ninety minutes to match the actual observed recovery time.
- D) Require the CTO to carry a dedicated emergency communication device at all times.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The authorization delay consumed nearly half the available RTO window. Pre-authorization criteria — defining specific conditions under which the team can declare and begin recovery without waiting for executive approval — eliminates this bottleneck entirely. The technical recovery was efficient; the process bottleneck was authorization latency.

- **Why A is incorrect:** The technical recovery time of fifty minutes is already well within the two-hour RTO. Investing in hardware to reduce it further does not address the actual risk — authorization delay could easily exceed the entire RTO window in a more serious incident.

- **Why C is incorrect:** Reducing the RTO to match observed performance does not improve actual recovery capability and incorrectly classifies the authorization latency as acceptable baseline performance. The RTO should be set by business impact, not by current process inefficiency.

- **Why D is incorrect:** While communication device redundancy helps, it does not solve the structural problem. If the CTO is in a meeting, asleep, or in a different time zone, waiting for their approval will always introduce unpredictable delay. Pre-authorization removes the dependency on real-time executive contact.

---

### Question 7

An organization applies the 3-2-1-1 backup rule. Which of the following scenarios is compliant with this rule?

- A) Three backup copies all stored on the same NAS device in the primary data center.
- B) One on-premises tape backup, one cloud backup on AWS S3, and one copy in AWS S3 with Object Lock enabled for immutability.
- C) Two copies on-premises (one on disk, one on tape) and one copy in a cloud storage bucket without versioning or immutability controls.
- D) One copy on-premises, one copy at a partner organization's office, and one copy in a cloud storage bucket accessible from the primary environment with the same credentials.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** This scenario provides three copies (on-premises tape, cloud S3, immutable S3), two media types (tape and cloud object storage), one off-site copy (cloud), and one immutable copy (S3 Object Lock). All four criteria of the 3-2-1-1 rule are satisfied.

- **Why A is incorrect:** Three copies on the same NAS device satisfies the "three copies" criterion only. It fails the two-media-type requirement, the off-site requirement, and the immutable storage requirement.

- **Why C is incorrect:** This scenario has two on-premises copies on different media and one cloud copy — satisfying 3-2-1 but not 3-2-1-1. The cloud copy lacks immutability, leaving all backups potentially vulnerable to ransomware if the cloud account is compromised.

- **Why D is incorrect:** If the third copy in the cloud is accessible from the primary environment using the same credentials, a ransomware attack that compromises the primary environment can also delete or encrypt the cloud copy. The immutability requirement exists precisely to prevent this.

---

### Question 8

Which of the following statements about DNS TTL values and RTO achievement is correct?

- A) Longer DNS TTL values improve RTO because they reduce the frequency of DNS lookup requests during a disaster.
- B) DNS TTL values have no impact on RTO because IP routing automatically redirects traffic without DNS changes.
- C) Short DNS TTL values — typically sixty to three hundred seconds — are required for critical production records because they allow traffic redirection to propagate rapidly during failover.
- D) DNS TTL is relevant only for external user traffic; internal application dependencies are not affected by TTL values.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** When failover requires changing DNS records to redirect traffic to the DR site, DNS propagation time is bounded by the TTL of the original record. If the TTL is twenty-four hours, cached resolvers worldwide will continue directing traffic to the failed primary site for up to twenty-four hours. Short TTLs (sixty to three hundred seconds) allow propagation within minutes.

- **Why A is incorrect:** Longer TTLs reduce DNS lookup traffic during normal operations, but they dramatically increase the time required to redirect traffic during a failover event. They are counterproductive for RTO achievement.

- **Why B is incorrect:** IP routing does not automatically redirect user traffic to a different server when a failure occurs — DNS-based redirection is a primary failover mechanism, and its propagation speed is directly constrained by TTL.

- **Why D is incorrect:** Internal application dependencies — microservices, APIs, databases accessed by FQDN — are also subject to DNS TTL. Long TTLs on internal service records can prevent application-layer failover even after the primary server changes have been made.

---

### Question 9

An organization's DR plan was last updated two years ago. Since then, the company has migrated from on-premises infrastructure to a hybrid cloud architecture, replaced its primary database platform, and promoted a new IT Director. Which DR plan section presents the highest immediate compliance risk if not updated?

- A) Section 6 — Test Schedule and Results.
- B) Section 1 — Scope and Purpose.
- C) Sections 3 and 4 — Roles and Responsibilities, and Recovery Procedures.
- D) Section 5 — Vendor and Support Contacts.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** The technology migration has rendered Section 4 recovery procedures obsolete — procedures written for on-premises infrastructure will not work in a hybrid cloud environment. The personnel change means Section 3 names an IT Director who may no longer hold that role. Both gaps pose immediate execution risk if the plan must be activated.

- **Why A is incorrect:** An outdated test schedule is a compliance concern but does not create immediate execution failure. The plan can still be executed even if the test schedule is stale.

- **Why B is incorrect:** Scope and purpose statements describe organizational intent; they are less likely to create execution failures than outdated procedures and roles, even if they need updating.

- **Why D is incorrect:** While outdated vendor contacts create challenges during recovery, the immediate execution failures come from incorrect procedures (Section 4) and wrong personnel designations (Section 3). Vendor contacts can often be located even if the listed number is outdated; following a procedure designed for a different infrastructure cannot be improvised.

---

### Question 10

Azure Site Recovery (ASR) is configured to replicate virtual machines from an organization's primary Azure region to a secondary Azure region. The organization's RTO for the replicated workloads is thirty minutes. During a planned failover test, ASR successfully brought the VMs online in the secondary region in eighteen minutes. The application validation checks passed. What is the appropriate next step?

- A) Decommission the primary region since the DR environment has proven its capability.
- B) Document the test results, perform failback to the primary region, and update the DR plan to reflect the validated eighteen-minute recovery time.
- C) Extend the RTO to sixty minutes since eighteen minutes provides adequate safety margin.
- D) No action is required; the test success confirms the DR program is complete.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** A successful DR test must be documented with results and lessons learned. Failback — returning to the primary region — must be executed as part of the test cycle, since failback is a separate operation with its own risks. The DR plan must be updated to reflect validated recovery times and any observations from the test.

- **Why A is incorrect:** Decommissioning the primary region based on a single successful DR test ignores the purpose of the primary environment and the test itself. The DR environment is a recovery option, not a replacement for the primary infrastructure.

- **Why C is incorrect:** RTO is set by business impact analysis, not by the recovery team's preference to create margin. Relaxing the RTO without a business impact justification disconnects the technical program from its organizational purpose.

- **Why D is incorrect:** A DR program is never complete — it requires continuous maintenance, regular retesting, and plan updates. A single successful test validates one point in time; the program must be sustained to remain valid.

---

### Question 11 (5 points)

An organization's DR plan requires that the recovery team receive an automated alert within five minutes of primary site unavailability. During a surprise failover drill, the automated monitoring system fails to trigger an alert, and the recovery team learns of the outage forty minutes later when a customer calls. Which DR plan component failed, and what is the primary governance action required?

- A) The failover procedure failed because the network was not redirected quickly enough.
- B) The detection and notification mechanism failed; the primary governance action is to document the gap, assign an owner, and remediate the monitoring and alerting configuration before the next test.
- C) The DR plan should be revised to remove the five-minute alert requirement since it proved unachievable.
- D) The customer call constitutes an adequate detection mechanism; no DR plan changes are required.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** DR plans must include detection and notification capabilities as a prerequisite to failover execution. A forty-minute detection gap in a plan requiring five-minute alerts is a critical finding. The governance action is to document the failure, assign a specific owner responsible for remediating the monitoring gap, and validate the fix before relying on that detection mechanism in a real disaster.

- **Why A is incorrect:** The failover procedure itself was not described as failing — the problem was that no one knew a failover was needed for forty minutes. The detection and notification component is what failed, not the failover execution steps.

- **Why C is incorrect:** Removing an RTO-supporting requirement to match a failed control is the wrong response. The five-minute alert target is derived from the overall RTO requirement. Relaxing it without a business impact justification allows a critical monitoring gap to persist as policy.

- **Why D is incorrect:** Customer-reported outages are not a reliable or acceptable DR detection mechanism. By the time customers call, significant business impact has already occurred, and the detection latency far exceeds any reasonable RTO. DR plans require proactive automated detection, not reactive customer notifications.

---

### Question 12 (5 points)

A company using on-premises infrastructure wants to implement a DR strategy for its financial reporting system with an RPO of thirty minutes and an RTO of two hours. The system processes 500 financial transactions per hour. Which combination of technologies best satisfies both objectives?

- A) Weekly tape backup stored off-site with manual restore procedure.
- B) Daily full backup to cloud storage with four-hour incremental backups.
- C) Synchronous replication to a warm standby server with pre-configured failover scripts that activate within ninety minutes.
- D) Manual data entry from printed reports at an alternate facility within forty-eight hours.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** Synchronous replication ensures zero data loss, satisfying the thirty-minute RPO (and exceeding it with zero-loss protection). Pre-configured failover scripts that activate within ninety minutes satisfy the two-hour RTO. This combination addresses both objectives with appropriate architecture.

- **Why A is incorrect:** Weekly tape backup leaves up to seven days of transactions at risk — catastrophically exceeding a thirty-minute RPO. Manual restore from tape also cannot achieve a two-hour RTO for a complex financial system. Both objectives are violated by orders of magnitude.

- **Why B is incorrect:** Four-hour incremental backups leave up to four hours of financial transactions at risk, exceeding the thirty-minute RPO by 3.5 hours. While cloud storage may eventually support RTO goals, the backup frequency makes this architecture non-compliant with the RPO requirement.

- **Why D is incorrect:** Manual data entry from printed reports cannot reconstruct 500 transactions per hour reliably or within two hours. This approach satisfies neither the RPO (data currency) nor the RTO (recovery speed), and introduces significant data integrity risk for a financial reporting system.

---

### Question 13 (5 points)

An organization conducts a DR test and activates its warm standby site. After completing the test, the team attempts failback to the primary site and discovers that the failback procedure has never been documented or tested. It takes eleven hours to return to the primary site. What does this scenario most directly reveal about the organization's DR program?

- A) The warm standby was inadequate and should be upgraded to a hot site.
- B) The DR program is incomplete — failback is a separate, equally critical operation from failover, and both must be documented, tested, and validated.
- C) Eleven-hour failback is acceptable because the RTO only applies to failover, not failback.
- D) The DR program should focus exclusively on preventing failover events rather than planning failback procedures.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** A complete DR program must address both failover (primary to DR) and failback (DR to primary). Failback carries its own risks — data synchronization gaps, replication conflicts, application re-registration, and user redirection — that require careful planning and testing. An undocumented, untested failback that requires eleven hours is a program gap that could extend total disruption time significantly beyond the planned RTO window.

- **Why A is incorrect:** The site type is not the problem here. The warm site performed as designed during failover. The gap is in failback planning, not in the site tier. Upgrading to a hot site would not automatically resolve an undocumented failback procedure.

- **Why C is incorrect:** RTO measures the total recovery time from disruption to return to normal operations. If failback is required to return to full production capability and takes eleven hours, that time is part of the overall disruption. RTO cannot be selectively applied only to the failover direction.

- **Why D is incorrect:** Preventing all failover events is not a feasible or complete DR strategy. Disasters, cyberattacks, and infrastructure failures cannot always be prevented. The DR program must plan for successful recovery in both directions — prevention is a risk reduction measure, not a substitute for recovery planning.

---

### Question 14 (5 points)

A company's DR plan includes a recovery time objective of four hours for its ERP system. During an annual review, the DR team discovers that the ERP vendor has end-of-lifed the version running at the DR site, meaning the DR environment can no longer receive security patches. Running the unpatched ERP at the DR site would violate the company's security policy. What is the most appropriate action?

- A) Accept the risk and proceed with the DR plan as written since the DR site is only used during disasters.
- B) Update the DR site to a supported ERP version, validate that the updated environment still achieves the four-hour RTO, and document the change in the DR plan.
- C) Remove the ERP from DR scope since security policy compliance cannot be achieved at the DR site.
- D) Reduce the RTO for the ERP to two hours to compensate for the security risk created by the unpatched DR environment.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The DR environment is a production environment during a disaster — it must meet the same security standards as the primary site. An unpatched, end-of-life application at the DR site creates security and compliance risk that is unacceptable even in a recovery scenario. The correct action is to update the DR site software, re-validate the RTO achievement with the updated version, and document the change. This maintains both security compliance and recovery capability.

- **Why A is incorrect:** Risk acceptance is a valid risk management tool, but accepting a known security policy violation at the DR site is not appropriate without explicit senior management approval, documentation, and compensating controls. "Only used during disasters" does not exempt the environment from security requirements — disasters can last days, during which the unpatched DR environment is the production environment.

- **Why C is incorrect:** Removing a critical system from DR scope creates a recovery gap that will directly impact RTO achievement during a real disaster. The solution is to update the DR environment, not to exclude the system from coverage.

- **Why D is incorrect:** Changing the RTO has no effect on the underlying security compliance problem. RTO is derived from business impact, not from technical debt management. This option neither resolves the compliance violation nor improves recovery capability.

---

### Question 15 (5 points)

An organization uses continuous data protection (CDP) for its order management database. Following a ransomware attack that began encrypting files at 14:23, the DR team determines that 14:15 was the last clean recovery point before encryption artifacts began appearing in the data stream. The organization's RPO is fifteen minutes. What does this scenario confirm about CDP relative to the RPO requirement?

- A) CDP failed because the ransomware was not blocked before it reached the database.
- B) CDP satisfied the fifteen-minute RPO — the clean recovery point at 14:15 is eight minutes before the corruption point at 14:23, which is within the RPO window.
- C) CDP is not suitable for ransomware scenarios because it replicates malicious changes in real time.
- D) The fifteen-minute RPO was exceeded because eight minutes is too close to the RPO boundary to be considered compliant.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** RPO measures maximum acceptable data loss. The clean recovery point at 14:15 means the organization can recover all data up to eight minutes before the ransomware began encrypting. The gap between the last clean point (14:15) and the corruption event (14:23) is eight minutes — within the fifteen-minute RPO. CDP satisfied the RPO requirement in this scenario.

- **Why A is incorrect:** CDP is a data protection technology, not a threat prevention control. CDP does not block malware; it provides granular recovery points. The ransomware reaching the database is a security control failure in prevention layers — separate from CDP's data protection function, which performed correctly.

- **Why C is incorrect:** While CDP does capture all changes in real time — including malicious ones — the ability to recover to a specific point-in-time before corruption occurred is precisely the advantage CDP provides over interval-based backups. The real-time capture enables identifying and recovering to the last clean point, which traditional backups cannot achieve with the same granularity.

- **Why D is incorrect:** RPO compliance is binary: either the recovery point is within the RPO window or it is not. Eight minutes is within fifteen minutes — the RPO is satisfied. There is no "too close to the boundary" concept in RPO compliance. The RPO is not a target to beat by a comfortable margin; it is a maximum threshold.

---

### Question 16 (5 points)

An organization is drafting its DR plan and must define activation criteria — the specific conditions under which the plan will be declared and failover initiated. Which set of criteria best demonstrates sound DR governance?

- A) The plan activates automatically whenever any server becomes unreachable for more than five minutes.
- B) Activation criteria are defined by IT staff at the time of an incident, based on their judgment of severity.
- C) Activation is triggered by pre-defined, documented thresholds such as primary site unavailability exceeding thirty minutes, data center power failure with generator failure, or CISO declaration following a confirmed cyberattack — with a named authority empowered to declare activation.
- D) The plan activates only when the CEO personally approves in writing, regardless of time of day or incident severity.

Correct Answer: C

Distractor Analysis:

- **Why C is correct:** Activation criteria must be specific, pre-documented, and tied to a named decision authority. Specific thresholds eliminate ambiguity and prevent both under-reaction (not activating when needed) and over-reaction (activating unnecessarily). A named authority with pre-authorization ensures activation can occur at any hour without requiring improvised judgment under stress.

- **Why A is incorrect:** Automatic activation on any five-minute server outage is far too sensitive. Normal maintenance windows, patching reboots, and brief network hiccups would trigger unnecessary DR activations, causing disruption and eroding staff confidence in the plan. Activation criteria must distinguish between routine outages and actual disasters.

- **Why B is incorrect:** Leaving activation criteria to ad-hoc judgment during an incident is a governance failure. Under stress, teams may disagree, delay, or make inconsistent decisions. Pre-documented criteria exist precisely to remove ambiguity from high-pressure decision points.

- **Why D is incorrect:** Requiring CEO personal written approval for every activation creates an unacceptable bottleneck — particularly for incidents occurring outside business hours or when the CEO is unavailable. Pre-authorization levels that allow delegated activation are essential for achieving RTO targets.

---

### Question 17 (5 points)

A company runs a multi-tier web application: a load-balanced web tier, an application tier, and a backend database cluster. The DR strategy calls for replicating all three tiers to an alternate region. During a failover test, the web and application tiers come online successfully, but the database fails to accept connections because the application tier is still pointing to the primary region's database endpoint. Which DR planning component was missing?

- A) Sufficient bandwidth between the primary and DR regions.
- B) A documented application dependency map and corresponding configuration update procedure ensuring all application tier connection strings are updated to the DR database endpoint during failover.
- C) A longer RTO that would give the team more time to manually locate and update the connection strings.
- D) A redundant copy of the web tier to handle increased traffic during the failover.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** A complete DR plan must document all application dependencies — including database connection strings, API endpoints, service discovery registrations, and load balancer targets — and include specific steps to update each during failover. Without a dependency map and corresponding update procedures, application tiers will attempt to reach primary-region services that are unavailable, exactly as observed. This is a documentation and planning gap, not a technology gap.

- **Why A is incorrect:** Bandwidth between regions would affect replication latency and data currency, but it does not explain why the application tier pointed to the wrong database endpoint. The failure was a configuration update problem, not a bandwidth problem.

- **Why C is incorrect:** A longer RTO does not address the root cause. Even with unlimited time, the team would not know which configuration items to update without a documented dependency map. The gap is documentation and process, not time allocation.

- **Why D is incorrect:** Web tier redundancy addresses availability and load distribution — it has no bearing on the application tier's inability to connect to the correct database endpoint. The failure is an application configuration issue, not a web tier capacity issue.

---

### Question 18 (5 points)

An organization's backup administrator proposes eliminating the off-site tape rotation in favor of a single cloud backup because "cloud storage is inherently redundant." From a 3-2-1-1 backup rule perspective, what is the flaw in this reasoning?

- A) Cloud storage cannot be used as a backup medium because it is not a physical tape.
- B) Cloud storage may provide geographic redundancy within the cloud provider's infrastructure, but it does not satisfy the "one off-site" requirement independently if the cloud account is accessible from the primary environment using the same credentials — and it does not satisfy the "one immutable" requirement unless object lock or equivalent is configured.
- C) The 3-2-1-1 rule requires physical tape as one of the media types; cloud alone is insufficient regardless of redundancy features.
- D) Eliminating tape is acceptable as long as the organization has two separate cloud backup accounts at different providers.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** The 3-2-1-1 rule's "off-site" requirement is about logical and physical separation from the primary environment — not just geographic distance within a cloud provider's availability zones. If the same credentials used to access the primary environment can also delete the cloud backups, a ransomware attack or credential compromise can destroy both. The rule also requires one immutable copy, which requires explicit configuration of object lock or write-once storage — cloud storage is not immutable by default.

- **Why A is incorrect:** The 3-2-1-1 rule does not specify physical tape as a required medium. Cloud storage is a valid medium under the rule. The issue is whether the cloud implementation satisfies the off-site and immutability requirements, not whether it is tape.

- **Why C is incorrect:** The rule specifies two different media types, but it does not mandate tape specifically. A disk-based on-premises backup and a cloud backup constitute two different media types. The medium type requirement is about diversification, not tape-specificity.

- **Why D is incorrect:** Two cloud accounts at different providers may satisfy the off-site and media diversity requirements, but only if the immutability requirement is also addressed. Without immutable storage in at least one copy, the 3-2-1-1 rule's fourth criterion is not met regardless of provider diversity.

---

### Question 19 (5 points)

An organization is designing its DR test program for the coming year. The CISO proposes the following schedule: a tabletop exercise in Q1, a parallel test in Q2, and a full cutover test in Q4. A board member asks why the organization does not perform a full cutover test every quarter. Which response best addresses the question from a risk and governance perspective?

- A) Full cutover tests are prohibited by most regulatory frameworks and cannot be performed more than once per year.
- B) Full cutover tests carry production risk — redirecting live traffic to the DR environment and taking the primary offline — and are resource-intensive. A tiered testing program uses lower-disruption tests to validate plan elements continuously while reserving full cutover for annual validation of the complete recovery capability.
- C) Full cutover tests are unnecessary once a tabletop exercise has confirmed the team understands the plan.
- D) The cost of full cutover tests is prohibitive for organizations of any size, making quarterly testing economically impossible.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** A tiered DR test program is the recognized best practice. Tabletop exercises test understanding without risk. Parallel tests validate technical recovery without production exposure. Full cutover tests provide the highest assurance but carry real production risk and require significant coordination and downtime windows. Quarterly full cutover testing for most organizations would impose unacceptable production risk and resource burden while providing diminishing returns relative to the tiered approach.

- **Why A is incorrect:** No major regulatory framework prohibits full cutover tests or limits their frequency. Some frameworks require annual testing, but the frequency ceiling is not a prohibition on more frequent testing. The decision is based on risk and resource management, not regulatory restriction.

- **Why C is incorrect:** Tabletop exercises confirm conceptual understanding — they do not validate that technical systems, configurations, and procedures will work under real conditions. Full cutover tests are required to achieve that level of assurance and cannot be replaced by tabletops.

- **Why D is incorrect:** Cost is a factor in DR test program design, but it is not uniformly prohibitive. Large organizations with stable DR environments may conduct full cutover tests more frequently. The governance rationale for the tiered approach is production risk management and resource efficiency — not an absolute cost barrier.

---

### Question 20 (5 points)

An organization's DR plan was activated following a confirmed ransomware outbreak. After forty-eight hours of operating from the DR site, the primary environment has been rebuilt and re-secured. The DR team prepares to execute failback. Which action must occur before production traffic is redirected back to the primary site?

- A) Inform all customers that the organization experienced a ransomware incident and is returning to the primary site.
- B) Validate that the rebuilt primary environment is clean, patched, and tested; that data synchronized from the DR site to the primary is complete and verified; and that the security team has confirmed the initial attack vector is remediated.
- C) Immediately redirect traffic back to the primary site to minimize time operating from the less capable DR environment.
- D) File an insurance claim for the ransomware incident before initiating failback, as insurance companies require notification before normal operations resume.

Correct Answer: B

Distractor Analysis:

- **Why B is correct:** Failback to a primary environment that has not been fully validated creates serious risk of re-infection, data loss, or operational failure. The rebuilt environment must be confirmed clean and secured, data synchronization from DR to primary must be verified for completeness and integrity, and the attack vector must be closed before returning to production. Rushing failback to exit the DR environment is a governance error that can re-trigger the incident.

- **Why A is incorrect:** Stakeholder communication is an important incident management responsibility, but it is not a technical prerequisite to failback execution. Communication decisions are made in parallel with technical recovery activities, not as a gate before failback.

- **Why C is incorrect:** Speed of failback should not override validation completeness. Operating from a less capable DR environment for additional time while validation is completed is preferable to failing back to a primary site that may still be compromised or incompletely rebuilt.

- **Why D is incorrect:** Insurance notification requirements vary by policy and do not typically require completion before technical recovery operations resume. This answer conflates insurance administration with technical recovery sequencing. The technical prerequisite for failback is environment validation, not insurance filing.
