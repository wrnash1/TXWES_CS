# Reading Guide: Module 14 — Disaster Recovery Management

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4315 &BULL; CYBERSECURITY GOVERNANCE, RISK & COMPLIANCE (GRC)</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

## Overview

This reading guide supports Module 14 and builds directly on the Business Continuity Planning foundations established in Module 13. Disaster Recovery Management is the technical discipline of restoring IT systems, data, and infrastructure following a disruptive event. Where BCP addresses the full organizational response, DR focuses on the technology recovery component — the site architectures, backup strategies, failover procedures, testing methods, and documentation practices that make recovery achievable within defined RTO and RPO targets.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Compare and contrast hot, warm, and cold DR site types by cost, recovery speed, and appropriate use cases.

2. Describe the seven-step failover procedure sequence and identify common points of failure.

3. Distinguish among document review, walkthrough, parallel, and full cutover DR testing approaches.

4. Evaluate cloud DR architectures on AWS and Azure and map them to traditional site type equivalents.

5. Compare full, incremental, and differential backup strategies by recovery complexity and RPO capability.

6. Explain the factors that determine whether an RTO target is achievable in practice.

7. Describe the six sections of a complete DR plan document.

---

## Section 1: DR Site Types

### 1.1 The Site Type Decision

The choice of DR site type is the most consequential architectural decision in a DR program. It establishes the baseline for achievable RTO and drives the majority of DR capital and operating expense. Site type selection must be driven by the RTO established in the BIA — not by budget preference or technical convenience.

### 1.2 Hot Site

A hot site is a fully operational duplicate of the primary production environment. Key characteristics include:

- Active hardware running continuously.

- Software installed, configured, and current.

- Data replicated in near-real-time from the primary site (synchronous or near-synchronous replication).

- Network connectivity pre-established and tested.

- Staff either co-located or on immediate call.

Recovery time at a hot site is measured in minutes to a few hours — primarily the time required to execute the failover procedure, redirect network traffic, and validate application functionality. Data loss is minimal or zero depending on replication method.

Hot sites are justified for Tier 1 systems where RTOs are two hours or less and where downtime costs exceed the ongoing expense of maintaining parallel infrastructure.

### 1.3 Warm Site

A warm site is a partially equipped recovery environment. Key characteristics include:

- Hardware installed and powered on.

- Software typically pre-installed and configured.

- Data not continuously replicated — restore from most recent backup required on activation.

- Network connectivity pre-established but not carrying live traffic.

Recovery time at a warm site is hours to one or two days, depending on the volume of data to be restored and the complexity of the application stack. Warm sites require the organization to transport or electronically deliver recent backup media upon activation.

Warm sites are appropriate for Tier 1 and Tier 2 systems with RTOs of two to twenty-four hours. They offer a balance between the high cost of a hot site and the very slow recovery of a cold site.

### 1.4 Cold Site

A cold site provides only the physical and infrastructure shell: power, physical space, climate control, and network connectivity. No hardware is pre-staged. No software is pre-installed. No data is stored there.

Recovery at a cold site requires acquiring hardware (either purchased, leased, or delivered from a vendor), installing and configuring operating systems and applications, and restoring data from backup. Recovery times are typically one to several weeks.

Cold sites are appropriate only for lower-priority systems with long MTPs, or as a last-resort fallback when budget prohibits a warmer alternative. Organizations that designate critical systems to cold sites are accepting that recovery will take far longer than most business processes can tolerate.

### 1.5 Mobile and Cloud Equivalents

Beyond the three traditional site types, two additional options are relevant:

**Mobile recovery units** are trailer-mounted or modular data center environments that can be deployed to any location with power and connectivity. They function as deployable warm or hot sites. They are used primarily by organizations with geographic flexibility requirements or in situations where a fixed alternate site may itself be affected by the disaster.

**Cloud DR environments** are the modern equivalent of traditional site types. Backup-and-restore in cloud storage is equivalent to cold. Pilot light (minimal core running, scale-out on demand) is equivalent to warm. Warm standby (fully functional scaled-down replica) is equivalent to a traditional warm site. Multi-site active-active is equivalent to — and exceeds — a hot site.

---

## Section 2: Failover Procedures

### 2.1 Failover Defined

Failover is the controlled transfer of processing responsibility from the primary environment to the recovery environment. It is a structured, sequenced procedure executed by trained personnel following a formal disaster declaration.

### 2.2 Failover Sequence

The standard failover sequence has seven steps:

**Step 1 — Incident Declaration:** An authorized individual formally declares that a disaster event has occurred and activates DR procedures. Pre-defined criteria and authorization levels prevent both premature activation and delayed response.

**Step 2 — Crisis Management Team Activation:** The DR team assembles. Roles are confirmed. Alternates are activated for any unavailable primary team members. Communication channels are established.

**Step 3 — DR Site Notification:** The recovery facility operator (colocation provider, cloud platform, or internal DR team) is notified and begins pre-activation steps. Transportation of backup media may begin for warm or cold sites.

**Step 4 — Data Verification and Cutover Decision:** The team verifies that data at the recovery site meets the RPO target. If the available restore point is outside the RPO window, the decision authority must be informed before proceeding. Proceeding with out-of-RPO data may be required in some scenarios, but it must be a conscious decision.

**Step 5 — Network and DNS Redirection:** Production traffic is redirected to the recovery environment. DNS changes propagate based on pre-configured TTL values. Firewall rule sets and load balancer configurations at the DR site are activated and verified.

**Step 6 — Application Validation:** The recovery team executes smoke tests — lightweight functional checks confirming that each application is operational. Validation criteria should be documented in advance so the team knows what success looks like.

**Step 7 — Business Operations Resumption:** Users and business teams are notified that systems are available at the recovery site. The DR team shifts to monitoring and support mode. Planning for failback — return to the primary site — begins.

### 2.3 Failback

Failback is the process of returning operations from the DR site to the restored primary site. Failback carries its own risks: data generated during DR operations at the recovery site must be synchronized back to the primary environment without loss. A separate failback runbook, tested independently, is required.

### 2.4 Common Points of Failure in Failover

Research into DR incident postmortems consistently identifies several recurring failure categories:

- **Stale documentation:** Procedures reference decommissioned systems or outdated IP addresses.

- **Authorization delays:** Decision makers are unavailable, and pre-authorization criteria are undefined.

- **DNS TTL misconfiguration:** Long TTL values prevent timely traffic redirection.

- **Replication lag or failure:** Data at the DR site is older than expected or corrupted.

- **Untested automation:** Runbook scripts fail in the recovery environment due to configuration differences.

- **Communication failure:** Team members cannot be reached through primary communication channels that may be unavailable during the incident.

---

## Section 3: DR Testing

### 3.1 Testing Philosophy

The purpose of DR testing is to discover failures under controlled conditions rather than during an actual disaster. Every test — regardless of the gaps it reveals — is a success, because identified gaps can be fixed. The only failed test is the test that was never conducted.

### 3.2 Document Review

Document review involves team members reading through DR procedures to identify errors, omissions, outdated information, and logical inconsistencies. Document review should be triggered by any significant infrastructure change and conducted as a continuous activity. It requires no system involvement and carries no risk to production.

### 3.3 Walkthrough Testing

A structured walkthrough has recovery team members step through DR procedures verbally and logically, confirming that each step makes sense and that required resources exist. Similar to a BCP tabletop, this is low-risk and low-cost. It is effective for onboarding new team members and for identifying logical gaps before a more expensive test.

### 3.4 Parallel Testing

A parallel test activates the DR environment completely while the primary environment remains live and fully operational. Both environments process workloads simultaneously. This validates that the DR environment can handle production workloads, that replication has been successful, and that application configurations are correct — all without any risk to production availability.

Parallel testing is the most commonly recommended DR test for organizations with production continuity requirements. It provides high confidence at manageable risk and can be performed annually for Tier 1 systems.

### 3.5 Full Cutover Testing

A full cutover test — also called a live failover test — redirects actual production traffic to the DR environment and takes the primary environment offline. This is the only test that validates the complete failover procedure including DNS redirection, network failover, and production load handling at the DR site.

Full cutover testing carries material risk: if DR fails during the test, the organization has a real outage. Pre-requisites include executive authorization, a tested fallback plan, a scheduled maintenance window, and advance notification to affected users.

Full cutover tests should be performed at least annually for Tier 1 systems in mature DR programs.

---

## Section 4: Cloud Disaster Recovery

### 4.1 Cloud DR Value Proposition

Cloud platforms offer on-demand infrastructure provisioning, geographic redundancy, and consumption-based pricing. These characteristics make cloud DR architectures economically viable for organizations that could not justify the capital cost of traditional alternate sites.

The fundamental tradeoff in cloud DR is identical to traditional DR: more recovery speed requires more pre-provisioned infrastructure, which costs more.

### 4.2 AWS DR Patterns

**Backup and Restore:** Data is backed up to Amazon S3. On activation, EC2 instances are launched and data is restored. This is the lowest-cost AWS DR option. RTO is typically two to four hours or more. This is a cold-equivalent approach.

**Pilot Light:** Core infrastructure elements — typically databases and critical application servers — run continuously in a secondary AWS region at minimal scale. On failover, additional instances are launched and the environment scales to production capacity. RTO is thirty minutes to two hours. This is a warm-equivalent approach.

**Warm Standby:** A fully functional replica of the production environment runs continuously in a secondary region at reduced scale. On failover, the replica scales to full production capacity. RTO is minutes to thirty minutes.

**Multi-Site Active-Active:** Full production capacity runs simultaneously in multiple AWS regions. No failover is required — traffic routes to the nearest healthy region. RTO approaches zero. This is the highest-cost option.

Key AWS services for DR include AWS Backup (centralized policy management), S3 Cross-Region Replication, RDS Multi-AZ and cross-region read replicas, and AWS Elastic Disaster Recovery for server-level replication.

### 4.3 Azure DR Patterns

**Azure Site Recovery (ASR):** ASR is Azure's primary DR service. It continuously replicates virtual machines from a primary Azure region to a secondary region. On failover, replicated VMs are brought online in the secondary region within the configured RTO window. ASR supports both Azure-to-Azure replication and on-premises-to-Azure replication.

**Azure Backup:** Centralized backup management for VMs, databases, and file shares with geo-redundant storage options.

**Azure SQL Geo-Replication and Failover Groups:** Maintains readable secondary database replicas in secondary Azure regions. Automatic failover groups allow database failover without application connection string changes.

### 4.4 Cloud DR Contractual Considerations

Cloud provider SLAs guarantee platform availability — they do not guarantee your application's recovery time. Organizations must validate that their cloud DR architecture can achieve the required RTO and RPO through testing, not through assumption. Cloud DR contracts should address data residency, compliance obligations in the recovery region, and the provider's notification obligations for platform-level incidents.

---

## Section 5: Backup Strategies

### 5.1 Full Backup

A full backup captures a complete copy of all designated data at a point in time. Full backups provide the simplest restore path — a single backup set contains everything needed for recovery. Disadvantages include long backup windows, high storage consumption, and network bandwidth impact during the backup process.

Full backups are typically performed weekly and serve as the anchor point for incremental and differential backup chains.

### 5.2 Incremental Backup

An incremental backup captures only data changed since the last backup of any type. Day-one incremental captures changes since the full backup. Day-two incremental captures changes since day-one incremental. Each incremental is small and fast. However, restoring from an incremental chain requires the full backup plus every subsequent incremental in sequence. The more incremental backups in the chain, the longer the restore process.

### 5.3 Differential Backup

A differential backup captures all data changed since the last full backup — regardless of how many differentials have been taken since. Day-two differential captures everything changed since the full backup. Day-five differential captures all changes since the full backup (a superset of day-two). Differentials grow in size over the week but provide a faster restore path than incremental chains: restore requires only the full backup plus the single most recent differential.

### 5.4 Continuous Data Protection

Continuous Data Protection (CDP) captures every data write at the block level, maintaining a real-time replica and a journal of all changes. CDP enables recovery to any point in time, not just to the last scheduled backup interval. CDP is appropriate for Tier 1 systems where RPOs of minutes or less are required.

### 5.5 The 3-2-1-1 Rule

The classic 3-2-1 backup rule specifies: three copies of data, stored on two different media types, with one copy stored off-site. The modern extension adds a fourth criterion: one copy stored in immutable (write-once, read-many) or air-gapped storage. Immutable backups cannot be deleted or encrypted by ransomware, making them the essential defense against backup destruction attacks.

---

## Section 6: RTO Achievement Factors

### 6.1 Why RTO Targets Are Missed

Organizations frequently discover during testing — or during actual incidents — that their achieved recovery time significantly exceeds their RTO target. The gap typically results from one or more of the following factors.

**Pre-staging gaps:** Infrastructure that must be provisioned, delivered, or configured during recovery adds time that is not accounted for in the RTO analysis.

**Manual procedure complexity:** Step-by-step manual procedures executed under stress by unfamiliar personnel take far longer than documented estimates suggest.

**Data volume:** Restoring large data sets over constrained bandwidth takes longer than expected. Data volume growth must be factored into RTO calculations at least annually.

**Authorization and communication latency:** The time to reach decision makers, obtain authorization, and mobilize distributed teams is consistently underestimated.

**DNS propagation delays:** Long DNS TTL values prevent timely redirection of user traffic to the recovery site.

**Undocumented dependencies:** Applications often have undocumented dependencies on auxiliary services (authentication systems, certificate authorities, monitoring platforms) that are not in the DR plan.

### 6.2 Strategies for Reliable RTO Achievement

- Automate recovery runbooks using orchestration tools.

- Pre-authorize declaration criteria so teams can act without waiting for an approval chain.

- Configure DNS TTL values of sixty to three hundred seconds for critical production records.

- Test at realistic data volumes, not reduced test datasets.

- Include all dependencies — including auxiliary services — in DR scope.

- Conduct full recovery time measurements during every test and compare against RTO targets.

---

## Section 7: DR Plan Documentation

### 7.1 DR Plan versus BCP Document

The DR plan is a technical document. Where the BCP addresses organizational-level response, the DR plan focuses on IT system recovery. The DR plan must be specific enough for a qualified technician who is unfamiliar with the system to execute recovery procedures correctly.

### 7.2 Standard DR Plan Sections

**Section 1 — Scope and Purpose:** Identifies the systems, services, and scenarios covered by the plan.

**Section 2 — Activation Criteria:** Defines the specific thresholds that trigger DR plan execution and who holds activation authority.

**Section 3 — Roles and Responsibilities:** Documents the DR team, each member's responsibilities, contact information, and named alternates for every role.

**Section 4 — Recovery Procedures:** Step-by-step technical runbooks for each covered system. Procedures must include expected outputs and error-handling steps, not just commands.

**Section 5 — Vendor and Support Contacts:** Contact information for hardware vendors, software vendors, colocation providers, cloud support tiers, and telecommunications carriers.

**Section 6 — Test Schedule and Results:** Records of when the plan was tested, the test type, findings, corrective actions, and completion status.

---

## Key Terms

- **Hot Site:** Fully operational DR environment with real-time data replication; fastest recovery, highest cost.

- **Warm Site:** Partially equipped DR environment requiring data restore on activation; moderate cost and recovery time.

- **Cold Site:** Facility infrastructure only; no pre-staged hardware or data; slowest recovery, lowest cost.

- **Failover:** Controlled transfer of processing from the primary environment to the recovery environment.

- **Failback:** Return of operations from the DR site to the restored primary environment.

- **Parallel Test:** DR test in which the recovery environment is activated alongside the live primary environment.

- **Full Cutover Test:** DR test in which production traffic is redirected to the DR environment and primary systems are taken offline.

- **Pilot Light:** AWS DR pattern equivalent to a warm site; minimal core environment runs continuously and scales on failover.

- **Azure Site Recovery (ASR):** Azure's primary VM replication and DR orchestration service.

- **3-2-1-1 Backup Rule:** Three copies, two media types, one off-site, one immutable.

- **Continuous Data Protection (CDP):** Real-time block-level capture enabling point-in-time recovery with near-zero RPO.

---

## Review Questions

1. A company has an RTO of ninety minutes for its order management system. Which DR site type is most consistent with this requirement, and why is a cold site architecturally incompatible?

2. In the failover sequence, what is the purpose of the data verification step before network redirection? What should the team do if the available data is outside the RPO window?

3. What is the key distinction between parallel testing and full cutover testing in terms of production risk?

4. Map each of the four AWS DR patterns (backup-and-restore, pilot light, warm standby, multi-site active-active) to the corresponding traditional site type equivalent.

5. A company takes full backups on Sunday and incremental backups Monday through Saturday. A failure occurs Saturday afternoon. Describe the restore procedure and identify the risk inherent in this backup strategy compared to a differential approach.

6. Why are DNS TTL values a critical factor in achieving RTO targets? What is the recommended TTL range for critical production DNS records?

---

## Study Checklist

- [ ] Define hot, warm, and cold site types and describe the appropriate use case for each.

- [ ] Describe the seven-step failover sequence from declaration through operations resumption.

- [ ] Compare parallel testing and full cutover testing by risk, cost, and assurance value.

- [ ] Map AWS and Azure cloud DR patterns to traditional site type equivalents.

- [ ] Explain full, incremental, and differential backup strategies and compare restore complexity.

- [ ] State the 3-2-1-1 backup rule and explain why immutable storage matters.

- [ ] Watch the Module 14 video lecture.

- [ ] Complete the Module 14 Lab.

- [ ] Proceed to the Module 14 Quiz and Discussion.

---

## Alignment to CISM Exam Domains

This module supports CISM Domain 4: Information Security Incident Management, which requires knowledge of recovery site alternatives, backup and recovery strategies, and disaster recovery testing. Students should review the ISACA CISM Review Manual sections covering DR strategy selection, testing approaches, and cloud-based recovery architectures.

---

## 9. Supplemental Resources

**1. AWS Disaster Recovery Whitepaper — Disaster Recovery of Workloads on AWS**
<https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html>
AWS's authoritative guide to the four DR patterns (backup-and-restore, pilot light, warm standby, multi-site active-active) with architecture diagrams, RTO/RPO guidance, and cost considerations. Essential reading for understanding cloud-native DR strategies covered in this module.

**2. NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems**
<https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final>
Covers the full spectrum of IT contingency planning including alternate site selection, backup strategies, plan testing types, and maintenance requirements. Chapters 4 and 5 are most directly relevant to DR site strategy and testing covered in this module.

**3. SANS Institute — Disaster Recovery Plan Strategies and Processes**
<https://www.sans.org/reading-room/whitepapers/recovery/disaster-recovery-plan-strategies-processes-564>
A practitioner-focused SANS whitepaper covering DR plan components, activation criteria, failover and failback sequencing, and lessons learned integration. Useful for understanding how DR governance principles translate to operational plan design.
