# Video Script: Module 14 — Disaster Recovery Management

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Additional Coverage — Business Continuity and Disaster Recovery

---

### [00:00 – 01:30] Opening and Learning Objectives

**Visual:** Instructor on camera with title card: "Module 14 — Disaster Recovery Management."

**Audio:**

"Welcome to Module 14. I'm Professor Nash, and we are now moving from Business Continuity Planning to Disaster Recovery Management. In Module 13 we built the foundation — BIA, RTO, BCP structure. In this module we get into the technical and operational mechanics of how organizations actually recover.

Here are your learning objectives. First, you will compare hot, warm, and cold disaster recovery site types. Second, you will describe failover procedures in sequence. Third, you will distinguish DR testing approaches and explain when each is appropriate. Fourth, you will evaluate cloud DR architectures on AWS and Azure. Fifth, you will analyze backup strategies by recovery capability. And sixth, you will explain what belongs in a DR plan document.

Let's start with the most fundamental DR decision you will make: site type."

---

### [01:30 – 05:00] DR Site Types

**Visual:** Three-panel comparison graphic — Hot Site, Warm Site, Cold Site — with attributes listed under each.

**Alt-text:** Three side-by-side panels. The Hot Site panel shows a fully equipped data center with active servers and live data feeds, labeled: Always running, real-time data, highest cost, RTO minutes to hours. The Warm Site panel shows powered-on servers awaiting data restore, labeled: Partially configured, data restore required, moderate cost, RTO hours to days. The Cold Site panel shows an empty facility with power and network infrastructure only, labeled: No pre-staged hardware, build from scratch, lowest cost, RTO days to weeks.

**Audio:**

"Disaster recovery relies on having a place — a facility, a cloud environment, or both — where operations can resume when the primary site is unavailable. The three classic site types define how ready that alternate environment is before you need it.

A **hot site** is a fully operational duplicate of your primary environment. Servers are running, network connections are active, and data is replicated in near-real-time. When your primary site fails, failover to the hot site can be completed in minutes to a few hours. Hot sites are the most expensive because you are paying for full infrastructure that sits in standby around the clock. They are appropriate for Tier 1 systems with RTOs of minutes to two hours.

A **warm site** is a partially equipped environment. Hardware is installed and powered on, software may be pre-installed, but current production data is not continuously replicated. When you activate a warm site, you restore from the most recent backup and resume operations. Recovery typically takes hours to days. Warm sites balance cost against recovery speed and are appropriate for Tier 1 and Tier 2 systems with RTOs of two to twenty-four hours.

A **cold site** is a facility with power, physical space, network connectivity, and physical infrastructure — but no pre-staged servers or data. When you need it, you acquire hardware, install software, restore data from backup, and build the environment from scratch. Recovery takes days to weeks. Cold sites are the least expensive but provide the slowest recovery. They are appropriate for lower-priority systems or for organizations where the cost of a warm or hot site is prohibitive.

On the CISM exam, the key differentiator between site types is recovery speed versus cost. Remember: hot is fastest and most expensive; cold is slowest and least expensive; warm is the middle option."

---

### [05:00 – 08:00] Failover Procedures

**Visual:** Sequential flowchart showing failover steps from incident declaration through full operations resumption at the DR site.

**Alt-text:** A vertical flowchart with seven labeled steps: (1) Incident Declaration → (2) Crisis Management Team Activation → (3) DR Site Notification → (4) Data Verification and Cutover Decision → (5) Network and DNS Redirection → (6) Application Validation → (7) Business Operations Resumption.

**Audio:**

"Having a DR site means nothing if you cannot execute failover correctly under pressure. Failover is the process of transferring operations from the primary environment to the recovery environment. It must be documented, tested, and repeatable.

Step one is incident declaration. Someone with authority — the IT Director, CISO, or their designated alternate — formally declares that a disaster has occurred and that DR procedures are activated. Without a formal declaration, teams may hesitate or take conflicting actions.

Step two is crisis management team activation. The DR team assembles — physically or virtually. Roles are confirmed. The incident commander takes command.

Step three is DR site notification. If using a colocation warm or cold site, the facility operator is notified. If using cloud DR, the automated runbook begins. Staff assigned to the DR site are mobilized.

Step four is data verification and the cutover decision. Before redirecting production traffic, the team verifies that the recovery environment has data that meets the RPO target. If the most recent restore point is outside the RPO window, the team must escalate before proceeding.

Step five is network and DNS redirection. Production traffic is redirected to the recovery environment. DNS TTLs must have been pre-configured for rapid propagation. Firewall rules and load balancer configurations at the DR site must mirror production.

Step six is application validation. The recovery team runs smoke tests — basic functional checks — to confirm that applications are operating correctly at the recovery site before opening access to users.

Step seven is business operations resumption. Users are notified that systems are available. The business resumes operations. The DR team begins planning for failback to the primary site once it is restored.

Two important notes: failback — returning to the primary site after recovery — is a separate procedure with its own risks and must also be documented and tested. And throughout the entire process, communication with stakeholders must be continuous and structured."

---

### [08:00 – 11:00] DR Testing

**Visual:** Table comparing four DR testing approaches — Document Review, Walkthrough, Parallel Test, Full Cutover — across four attributes: description, risk to production, cost, and frequency.

**Audio:**

"DR testing parallels BCP testing but focuses on technical recovery validation. There are four primary approaches.

**Document review** is the most basic. Team members read through the DR plan and identify errors, outdated information, and logical gaps. No systems are involved. This should be a continuous activity, not a periodic event. Every time a significant infrastructure change is made, the corresponding DR documentation should be reviewed.

**Walkthrough testing** — also called a structured walkthrough — has recovery teams review the DR procedures step-by-step without executing them. Similar to a BCP tabletop, this validates procedure logic and team familiarity. It is low-risk and should be performed semi-annually or when the plan changes significantly.

**Parallel testing** activates the DR environment while the primary environment remains fully operational. Both environments run simultaneously. The team validates that the DR environment can process workloads without disrupting production. This is the most common approach for organizations that cannot afford production risk. Parallel tests provide high confidence at manageable risk.

**Full cutover testing** — the highest-fidelity approach — actually redirects production traffic to the DR environment. Primary systems are taken offline. This is the only test that truly validates end-to-end recovery capability including network redirection, application performance under real load, and failback procedures. Full cutover tests carry the highest risk: if DR fails, the organization has real downtime. Executive sponsorship and formal risk acceptance are required before conducting a full cutover test.

On the CISM exam: parallel testing is often the correct answer when the question asks which DR test validates the recovery environment without risking production. Full cutover is the correct answer when the question asks which test provides the highest assurance of actual recovery capability."

---

### [11:00 – 15:00] Cloud DR — AWS and Azure

**Visual:** Split screen — AWS DR architecture diagram on left (showing primary region, S3 replication, and recovery region), Azure DR diagram on right (showing Azure Site Recovery architecture).

**Alt-text:** Left panel: AWS architecture diagram. Primary region contains EC2 instances and RDS databases. Arrows show S3 Cross-Region Replication and RDS read replica replication flowing to Recovery Region. Recovery region shows EC2 launch templates and RDS restore targets. Right panel: Azure architecture diagram. Primary Azure region contains Virtual Machines and Azure SQL. Azure Site Recovery arrows point to secondary Azure region showing VM replicas and SQL geo-replication.

**Audio:**

"Cloud platforms have transformed disaster recovery. Where organizations once needed to own or contract physical alternate sites, they can now provision on-demand recovery environments in a different geographic region. Let's look at both major platforms.

On **AWS**, the four cloud DR patterns are important for the exam. Backup and restore is the simplest: data is backed up to S3 or another storage service and restored to EC2 instances when needed. RTO is hours; this is the equivalent of a cold site approach. Pilot light keeps a minimal core environment always running — databases replicated, core services active — with the ability to scale out rapidly on failover. Warm standby maintains a scaled-down but fully functional replica in a secondary region. RTO is minutes to an hour. Multi-site active-active runs production workloads in multiple regions simultaneously with zero planned downtime. RTO approaches zero; cost is highest.

AWS services that support DR include **AWS Backup** for centralized backup policy management, **S3 Cross-Region Replication** for data durability, **RDS Multi-AZ** and **read replicas** for database redundancy, and **AWS Elastic Disaster Recovery** — formerly known as CloudEndure — for continuous block-level replication of on-premises or cloud servers.

On **Azure**, the primary DR service is **Azure Site Recovery** (ASR). ASR replicates virtual machines from a primary region to a secondary region, continuously capturing changes. On failover, ASR can bring replicated VMs online in the secondary region within the RTO window. Azure also offers **Azure Backup** for centralized backup management and **Azure SQL Geo-Replication** for database-level geographic redundancy.

A critical point on cloud DR: your cloud provider's SLA for service availability is not your RTO. The provider guarantees their platform uptime — it does not guarantee your application recovery time. You must architect, test, and validate your cloud DR solution independently of the provider's SLA."

---

### [15:00 – 17:30] Backup Strategies

**Visual:** Comparison diagram showing full, incremental, and differential backup types with a one-week timeline and restore paths.

**Alt-text:** A horizontal calendar showing Monday through Sunday. Monday shows a Full Backup arrow covering all data. Tuesday through Sunday show Incremental Backup arrows each covering only new changes since the previous day. A second row shows Monday Full Backup followed by Wednesday Differential Backup covering all changes since Monday. Restore path annotations indicate: Incremental restore requires Full plus each daily incremental; Differential restore requires Full plus only the most recent differential.

**Audio:**

"Backup strategy is how you achieve your RPO target. The three primary approaches are full, incremental, and differential backup.

A **full backup** captures a complete copy of all protected data. It is the most comprehensive but requires the most storage and the longest backup window. Full backups are typically performed weekly or on a set schedule because of the resource requirements.

An **incremental backup** captures only the data that has changed since the last backup of any type — whether that was a full or a previous incremental. Incrementals are fast and storage-efficient, but restoration requires the last full backup plus every incremental since then. Restore time increases with the number of incrementals to apply.

A **differential backup** captures all data that has changed since the last full backup. Differentials grow larger each day as more changes accumulate, but restoration requires only the last full backup plus the single most recent differential. Restore is faster than incremental chains.

For achieving aggressive RPOs, modern organizations use **continuous data protection (CDP)** — capturing every write at the block level with near-zero RPO. CDP is used for Tier 1 systems where data loss of even a few minutes is unacceptable.

The **3-2-1 backup rule** is a foundational principle you must know: three copies of data, on two different media types, with one copy off-site. Cloud storage has modified this to 3-2-1-1: the same plus one copy in immutable storage — critical for ransomware defense, because attackers who compromise the primary environment may also target connected backup systems."

---

### [17:30 – 20:30] RTO Achievement

**Visual:** Graph showing RTO achievement curve — strategies plotted by cost (x-axis) and RTO capability (y-axis).

**Alt-text:** A line graph. The x-axis is labeled Cost, ranging from Low to High. The y-axis is labeled RTO, ranging from Days (top) to Seconds (bottom). Points on the curve are labeled from top-left to bottom-right: Cold Site / Backup and Restore (low cost, days RTO), Warm Site (moderate cost, hours RTO), Pilot Light (moderate-high cost, one hour RTO), Hot Site / Warm Standby (high cost, minutes RTO), Active-Active (highest cost, seconds RTO).

**Audio:**

"Achieving an RTO is not simply a matter of having good documentation. It requires architectural choices, automation, tested procedures, and pre-positioned resources. Let me walk through the key factors.

**Pre-staged infrastructure** reduces recovery time by eliminating provisioning delays. Hot sites and cloud warm standby environments keep infrastructure ready to receive production load immediately. Cold sites and backup-and-restore approaches require provisioning time that must be counted against the RTO.

**Automation** is the single largest factor in achieving aggressive RTOs. Manual failover procedures are error-prone and time-consuming under pressure. Runbook automation — using AWS Systems Manager, Azure Automation, Ansible, or similar tools — allows failover steps to execute in minutes rather than hours.

**Data replication lag** affects the achievable RPO, which in turn affects where in the failover sequence the team can proceed. Synchronous replication (zero data loss, higher latency) is used for the most critical databases. Asynchronous replication (potential data loss measured in seconds to minutes, lower latency) is used for less critical systems.

**DNS time-to-live values** must be pre-configured. If your DNS TTL is twenty-four hours, traffic redirection will take twenty-four hours to propagate globally — far exceeding most RTOs. Production DNS records for critical services should have TTLs of sixty to three hundred seconds.

**Communication and authorization latency** is often the largest hidden contributor to RTO failures. The time to reach a decision maker, get authorization to declare, and mobilize the team can be thirty minutes to two hours. BCP and DR plans must define pre-authorization conditions so teams can act without waiting for a chain of approval under pressure."

---

### [20:30 – 22:30] DR Plan Documentation

**Visual:** Document outline on screen showing six numbered DR plan sections.

**Audio:**

"A DR plan is distinct from the broader BCP document. Where the BCP addresses the full organizational response to a disruption, the DR plan is a technical document that tells recovery teams exactly what to do to restore IT systems.

Section one is scope and purpose — which systems, services, and facilities are covered by this plan, and what disaster scenarios it addresses.

Section two is activation criteria — the specific thresholds that trigger DR plan execution and the authority chain for declaration.

Section three is roles and responsibilities — who is on the DR team, what each person's responsibilities are, and how they are contacted. This section must include alternates for every role.

Section four is recovery procedures — the step-by-step technical runbooks for each covered system. These must be specific enough for a qualified technician unfamiliar with the environment to execute. Procedures should include commands, expected outputs, and error-handling steps.

Section five is vendor and support contacts — numbers for hardware vendors, software vendors, colocation providers, cloud support, telecom carriers, and any other external parties required during recovery.

Section six is test schedule and results — documentation of when the plan was last tested, what type of test was conducted, what gaps were found, and what corrective actions were taken.

DR plan documentation must be versioned, dated, and stored in locations accessible when primary systems are unavailable. Printed copies at off-site locations and cloud-hosted copies both serve this purpose."

---

### [22:30 – 24:00] Summary and Exam Tips

**Visual:** Bullet summary slide with six key takeaways.

**Audio:**

"Here are the Module 14 key takeaways.

First, site type determines recovery speed and cost. Hot equals fast and expensive; cold equals slow and inexpensive; warm is the middle ground.

Second, failover is a structured, sequenced process. Each step must be documented and tested.

Third, parallel testing validates the DR environment without production risk; full cutover testing provides the highest assurance but carries real risk.

Fourth, cloud DR patterns range from backup-and-restore (cold equivalent) to active-active (zero planned RTO). Match the pattern to the RTO requirement.

Fifth, the 3-2-1-1 backup rule — three copies, two media types, one off-site, one immutable — is the modern baseline.

Sixth, RTO achievement requires architecture plus automation plus pre-authorization. Documentation alone does not create recovery capability.

For the CISM exam, focus on the cost-versus-speed tradeoffs among site types, the difference between parallel and full cutover testing, and how cloud DR patterns map to traditional site classifications. These areas are heavily tested.

This concludes Module 14. Together, Modules 13 and 14 give you the complete Business Continuity and Disaster Recovery framework you need for the CISM exam. I'll see you in Module 15."

---

### Production Notes

- **Slides:** Minimum 18-point font. All diagrams need alt-text as scripted.

- **On-screen timers:** Display elapsed time in lower-left corner.

- **Caption file:** SRT format required for LMS upload.

- **B-roll suggestions:** Data center failover footage, AWS and Azure console screenshots (with test accounts), backup progress bar animations.

- **Exam callout graphic:** Use a distinct gold banner for all CISM exam tips.
