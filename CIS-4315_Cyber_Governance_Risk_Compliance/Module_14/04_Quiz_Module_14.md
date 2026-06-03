# Quiz: Module 14 — Disaster Recovery Management

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

**Question 1**

An organization's customer-facing web application has an RTO of ninety minutes. The DR team is evaluating alternate site options. Which option is most consistent with this RTO requirement?

- A) Cold site with pre-negotiated hardware delivery within seventy-two hours.
- B) Warm site requiring four to eight hours to restore from the most recent backup.
- C) Hot site with real-time data replication and pre-staged servers capable of accepting traffic within thirty minutes of failover.
- D) Cloud backup-and-restore approach with an estimated two to four hour restore window.

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A ninety-minute RTO requires near-instantaneous recovery capability. A hot site with real-time replication and pre-staged infrastructure can achieve failover in thirty minutes — within the ninety-minute window. This is the only option that is architecturally capable of meeting the stated RTO.

- **Why A is incorrect:** A cold site with seventy-two-hour hardware delivery is architecturally incapable of a ninety-minute RTO. Cold sites are appropriate only for systems with RTOs of days to weeks.

- **Why B is incorrect:** A warm site requiring four to eight hours to restore exceeds the ninety-minute RTO. Warm sites are appropriate for systems with RTOs of two to twenty-four hours.

- **Why D is incorrect:** Cloud backup-and-restore has an estimated RTO of two to four hours, which also exceeds the ninety-minute requirement. Backup-and-restore is equivalent to a cold site approach.

---

**Question 2**

During a DR failover procedure, the recovery team has completed site notification and assembled the team. The next step in the sequence is to verify whether the available data at the DR site meets the RPO target before redirecting production traffic. The team discovers the most recent replication snapshot is six hours old, while the RPO is two hours. What is the most appropriate action?

- A) Proceed immediately with network redirection because any data is better than none.
- B) Escalate to the decision authority and document the out-of-RPO condition before deciding whether to proceed.
- C) Cancel the failover and wait until the primary site is restored.
- D) Restore from the six-hour snapshot without notifying anyone, since users will not notice missing transactions.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Proceeding with data that is outside the RPO window may expose the organization to additional business impact, legal liability, or regulatory non-compliance. The decision to accept the out-of-RPO condition must be made by an authorized decision-maker, documented, and managed consciously — not unilaterally by the recovery team.

- **Why A is incorrect:** Proceeding without escalation removes the decision authority from the appropriate level. The recovery team does not have unilateral authorization to accept an RPO violation.

- **Why C is incorrect:** Canceling the failover entirely may cause the organization to exceed its MTPD while waiting for primary site recovery. The decision to cancel requires the same escalation as the decision to proceed with out-of-RPO data.

- **Why D is incorrect:** Concealing a known RPO violation from management is a governance failure and potentially a compliance violation. Missing transactions may have financial, legal, or operational consequences that management must address.

---

**Question 3**

An organization conducts a DR test in which the recovery environment is fully activated and validated while the primary production environment remains live and operational. Users are not affected. Which test type is this?

- A) Full cutover test.
- B) Document review.
- C) Parallel test.
- D) Walkthrough test.

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A parallel test activates the recovery environment simultaneously with the live production environment. Both run at the same time, allowing the team to validate DR procedures and environment readiness without any risk to production availability.

- **Why A is incorrect:** A full cutover test redirects production traffic to the DR environment and takes the primary environment offline. Users are affected during a full cutover test.

- **Why B is incorrect:** A document review involves reading and evaluating the DR plan without activating any systems. No recovery environment is launched during a document review.

- **Why D is incorrect:** A walkthrough (structured walkthrough) has team members step through procedures verbally without executing them. No systems are activated.

---

**Question 4**

A company migrates to AWS and implements the following DR architecture: a minimal set of core database replicas always running in a secondary AWS region, with EC2 launch templates configured but no running instances. On failover, the team launches instances from the templates and scales the database replicas to production capacity. Which AWS DR pattern does this describe?

- A) Multi-site active-active.
- B) Backup and restore.
- C) Warm standby.
- D) Pilot light.

**Correct Answer:** D

**Distractor Analysis:**

- **Why D is correct:** Pilot light keeps only the critical core — typically databases — running continuously in a secondary region. Compute instances are not pre-launched but can be started quickly from pre-configured templates. This distinguishes pilot light from warm standby (which has compute running at reduced scale) and from backup-and-restore (which provisions everything on demand).

- **Why A is incorrect:** Multi-site active-active runs full production capacity simultaneously in multiple regions. There are no standby or scaled-down components — both regions actively handle traffic.

- **Why B is incorrect:** Backup and restore provisions everything from scratch on failover — no compute or database infrastructure is pre-running in the recovery region. Pilot light is more capable than backup-and-restore because the database core is already running.

- **Why C is incorrect:** Warm standby runs a fully functional scaled-down replica — including compute instances — in the secondary region at all times. Pilot light does not run compute instances continuously; it only keeps the minimal database core running.

---

**Question 5**

A company takes weekly full backups on Sunday and daily incremental backups Monday through Saturday. A server failure occurs on Friday afternoon. Describe the restore procedure.

- A) Restore only the most recent Saturday incremental, which contains all data since the prior Sunday.
- B) Restore the Sunday full backup, then apply Monday, Tuesday, Wednesday, Thursday, and Friday incrementals in sequence.
- C) Restore the Sunday full backup and then apply only the most recent differential backup.
- D) Restore only the Sunday full backup; incremental backups are not needed if the full backup is recent.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Incremental backup recovery requires the full backup plus every incremental in the chain from the last full backup to the most recent incremental before the failure. Each incremental captures only changes since the previous backup — they must be applied in order to reconstruct the complete data set.

- **Why A is incorrect:** Each incremental backup captures only the changes made since the previous day's backup, not all changes since the last full backup. The Friday incremental alone contains only Friday's changes — not the accumulated changes from Monday through Thursday.

- **Why C is incorrect:** Differential backups are not the same as incremental backups. The scenario specifies daily incrementals. Differential backups capture all changes since the last full backup — incrementals do not. Applying differential restore logic to incremental backups produces an incorrect restore.

- **Why D is incorrect:** A full backup alone recovers the state as of the last full backup — Sunday in this case. Any data created or changed Monday through Friday would be lost. The incrementals are essential to recovering the intervening changes.

---

**Question 6**

An organization's DR plan specifies a two-hour RTO for its critical ERP system. During a full cutover test, the recovery team spends forty-five minutes waiting for authorization from the CTO, who was traveling and difficult to reach. The actual technical recovery took fifty minutes. Total elapsed time was ninety-five minutes, which technically meets the two-hour RTO. Which improvement addresses the most significant risk revealed by this test?

- A) Upgrade the ERP server hardware at the DR site to reduce the technical recovery time to thirty minutes.
- B) Define pre-authorization criteria that allow the recovery team to begin failover without waiting for the CTO's explicit approval.
- C) Reduce the RTO to ninety minutes to match the actual observed recovery time.
- D) Require the CTO to carry a dedicated emergency communication device at all times.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The authorization delay consumed nearly half the available RTO window. Pre-authorization criteria — defining specific conditions under which the team can declare and begin recovery without waiting for executive approval — eliminates this bottleneck entirely. The technical recovery was efficient; the process bottleneck was authorization latency.

- **Why A is incorrect:** The technical recovery time of fifty minutes is already well within the two-hour RTO. Investing in hardware to reduce it further does not address the actual risk — authorization delay could easily exceed the entire RTO window in a more serious incident.

- **Why C is incorrect:** Reducing the RTO to match observed performance does not improve actual recovery capability and incorrectly classifies the authorization latency as acceptable baseline performance. The RTO should be set by business impact, not by current process inefficiency.

- **Why D is incorrect:** While communication device redundancy helps, it does not solve the structural problem. If the CTO is in a meeting, asleep, or in a different time zone, waiting for their approval will always introduce unpredictable delay. Pre-authorization removes the dependency on real-time executive contact.

---

**Question 7**

An organization applies the 3-2-1-1 backup rule. Which of the following scenarios is compliant with this rule?

- A) Three backup copies all stored on the same NAS device in the primary data center.
- B) One on-premises tape backup, one cloud backup on AWS S3, and one copy in AWS S3 with Object Lock enabled for immutability.
- C) Two copies on-premises (one on disk, one on tape) and one copy in a cloud storage bucket without versioning or immutability controls.
- D) One copy on-premises, one copy at a partner organization's office, and one copy in a cloud storage bucket accessible from the primary environment with the same credentials.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** This scenario provides three copies (on-premises tape, cloud S3, immutable S3), two media types (tape and cloud object storage), one off-site copy (cloud), and one immutable copy (S3 Object Lock). All four criteria of the 3-2-1-1 rule are satisfied.

- **Why A is incorrect:** Three copies on the same NAS device satisfies the "three copies" criterion only. It fails the two-media-type requirement, the off-site requirement, and the immutable storage requirement.

- **Why C is incorrect:** This scenario has two on-premises copies on different media and one cloud copy — satisfying 3-2-1 but not 3-2-1-1. The cloud copy lacks immutability, leaving all backups potentially vulnerable to ransomware if the cloud account is compromised.

- **Why D is incorrect:** If the third copy in the cloud is accessible from the primary environment using the same credentials, a ransomware attack that compromises the primary environment can also delete or encrypt the cloud copy. The immutability requirement exists precisely to prevent this.

---

**Question 8**

Which of the following statements about DNS TTL values and RTO achievement is correct?

- A) Longer DNS TTL values improve RTO because they reduce the frequency of DNS lookup requests during a disaster.
- B) DNS TTL values have no impact on RTO because IP routing automatically redirects traffic without DNS changes.
- C) Short DNS TTL values — typically sixty to three hundred seconds — are required for critical production records because they allow traffic redirection to propagate rapidly during failover.
- D) DNS TTL is relevant only for external user traffic; internal application dependencies are not affected by TTL values.

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** When failover requires changing DNS records to redirect traffic to the DR site, DNS propagation time is bounded by the TTL of the original record. If the TTL is twenty-four hours, cached resolvers worldwide will continue directing traffic to the failed primary site for up to twenty-four hours. Short TTLs (sixty to three hundred seconds) allow propagation within minutes.

- **Why A is incorrect:** Longer TTLs reduce DNS lookup traffic during normal operations, but they dramatically increase the time required to redirect traffic during a failover event. They are counterproductive for RTO achievement.

- **Why B is incorrect:** IP routing does not automatically redirect user traffic to a different server when a failure occurs — DNS-based redirection is a primary failover mechanism, and its propagation speed is directly constrained by TTL.

- **Why D is incorrect:** Internal application dependencies — microservices, APIs, databases accessed by FQDN — are also subject to DNS TTL. Long TTLs on internal service records can prevent application-layer failover even after the primary server changes have been made.

---

**Question 9**

An organization's DR plan was last updated two years ago. Since then, the company has migrated from on-premises infrastructure to a hybrid cloud architecture, replaced its primary database platform, and promoted a new IT Director. Which DR plan section presents the highest immediate compliance risk if not updated?

- A) Section 6 — Test Schedule and Results.
- B) Section 1 — Scope and Purpose.
- C) Sections 3 and 4 — Roles and Responsibilities, and Recovery Procedures.
- D) Section 5 — Vendor and Support Contacts.

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The technology migration has rendered Section 4 recovery procedures obsolete — procedures written for on-premises infrastructure will not work in a hybrid cloud environment. The personnel change means Section 3 names an IT Director who may no longer hold that role. Both gaps pose immediate execution risk if the plan must be activated.

- **Why A is incorrect:** An outdated test schedule is a compliance concern but does not create immediate execution failure. The plan can still be executed even if the test schedule is stale.

- **Why B is incorrect:** Scope and purpose statements describe organizational intent; they are less likely to create execution failures than outdated procedures and roles, even if they need updating.

- **Why D is incorrect:** While outdated vendor contacts create challenges during recovery, the immediate execution failures come from incorrect procedures (Section 4) and wrong personnel designations (Section 3). Vendor contacts can often be located even if the listed number is outdated; following a procedure designed for a different infrastructure cannot be improvised.

---

**Question 10**

Azure Site Recovery (ASR) is configured to replicate virtual machines from an organization's primary Azure region to a secondary Azure region. The organization's RTO for the replicated workloads is thirty minutes. During a planned failover test, ASR successfully brought the VMs online in the secondary region in eighteen minutes. The application validation checks passed. What is the appropriate next step?

- A) Decommission the primary region since the DR environment has proven its capability.
- B) Document the test results, perform failback to the primary region, and update the DR plan to reflect the validated eighteen-minute recovery time.
- C) Extend the RTO to sixty minutes since eighteen minutes provides adequate safety margin.
- D) No action is required; the test success confirms the DR program is complete.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A successful DR test must be documented with results and lessons learned. Failback — returning to the primary region — must be executed as part of the test cycle, since failback is a separate operation with its own risks. The DR plan must be updated to reflect validated recovery times and any observations from the test.

- **Why A is incorrect:** Decommissioning the primary region based on a single successful DR test ignores the purpose of the primary environment and the test itself. The DR environment is a recovery option, not a replacement for the primary infrastructure.

- **Why C is incorrect:** RTO is set by business impact analysis, not by the recovery team's preference to create margin. Relaxing the RTO without a business impact justification disconnects the technical program from its organizational purpose.

- **Why D is incorrect:** A DR program is never complete — it requires continuous maintenance, regular retesting, and plan updates. A single successful test validates one point in time; the program must be sustained to remain valid.
