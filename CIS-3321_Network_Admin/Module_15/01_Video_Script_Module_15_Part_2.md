# Video Script: Module 15 — Network Documentation and Policies (Part 2 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome back. This is Part 2 of Module 15 on Network Documentation and Policies. In Part 1 we covered network diagrams, IP address management, and change management. Now we cover the policy framework that governs how networks are used and protected: acceptable use policies, service level agreements, and disaster recovery documentation.

---

## Section 1: Acceptable Use Policies

An Acceptable Use Policy, or AUP, is a formal document that defines how an organization's network, systems, and internet access may and may not be used. Every organization with network-connected users should have an AUP.

### Why AUPs Matter for Network Administrators

As a network administrator, you are frequently asked to implement technical controls that enforce AUP provisions — content filters, application controls, bandwidth throttling, and monitoring systems. Understanding what the AUP requires is essential for configuring these systems correctly.

AUPs also establish the legal and organizational framework for taking action when users violate policy — accessing prohibited content, downloading unauthorized software, or misusing company bandwidth. Without a signed AUP, organizations have limited recourse against policy violators.

### Typical AUP Provisions

An AUP typically addresses:

- **Permitted use**: What the network is for — business use, authorized personal use within specified limits.
- **Prohibited activities**: What is explicitly not allowed. Common examples: illegal downloads, accessing adult or gambling content on company resources, running personal businesses on company equipment, bypassing security controls (VPN split tunneling, personal hotspots to avoid content filters).
- **Privacy notice**: A statement that the organization monitors network activity and that users should have no expectation of privacy on company systems.
- **Consequences**: What happens if the policy is violated — disciplinary action up to and including termination; potential legal action for illegal activity.
- **Security responsibilities**: User obligations — keeping passwords secure, locking workstations, not installing unauthorized software.
- **BYOD provisions**: Rules for personally-owned devices connecting to the corporate network (if permitted).
- **Remote access**: Policies governing VPN use, home network security requirements for remote workers.

### AUP Acknowledgment

The AUP has legal value only if users have signed or acknowledged it. Best practice: require employees to sign the AUP on hire, and re-sign annually when the policy is updated. Electronic acknowledgment (clicking "I Accept" on a captive portal during onboarding) is also valid and often more practical.

---

## Section 2: Service Level Agreements

A Service Level Agreement, or SLA, is a contract between a service provider and a customer defining the expected level of service. Network administrators work with SLAs in two contexts:

- As a consumer of carrier SLAs (guarantees from your ISP, MPLS provider, or cloud provider)
- As a provider of internal SLAs (commitments to internal business units)

### Key SLA Metrics

#### Availability

Availability is the percentage of time a service is operational. Expressed as a percentage — typically called "nines."

| Availability | Annual Downtime |
|---|---|
| 99% (two nines) | 87.6 hours |
| 99.9% (three nines) | 8.76 hours |
| 99.99% (four nines) | 52.6 minutes |
| 99.999% (five nines) | 5.26 minutes |

Most enterprise SLAs target 99.99% or better for critical systems. Five-nines (99.999%) is the gold standard for carrier-grade services.

#### Mean Time Between Failures (MTBF)

MTBF is the average time between failure events for a system or component. Higher MTBF means more reliable hardware. Used when selecting hardware for critical deployments.

MTBF = Total operational time / Number of failures

For example, if a switch operates for 50,000 hours before failing once, its MTBF is 50,000 hours. This does not mean the switch will definitely last 50,000 hours — it is a statistical average.

#### Mean Time to Repair (MTTR)

MTTR is the average time to restore a failed system. Includes detection, diagnosis, repair, and restoration time.

MTTR = Total repair time / Number of repairs

Reducing MTTR requires: rapid detection (monitoring and alerting), effective troubleshooting procedures, available spare parts, and skilled personnel.

#### Recovery Time Objective (RTO)

RTO is the maximum acceptable time for a system to be restored after a failure or disaster. Defined in the organization's business continuity plan.

For example: "The payroll system must be restored within 4 hours of any failure." That 4 hours is the RTO.

Network design must support the RTO — if the RTO is 4 hours, WAN failover must be achievable within that window.

#### Recovery Point Objective (RPO)

RPO is the maximum acceptable amount of data loss measured in time. Defined in the business continuity plan alongside RTO.

For example: "We can tolerate losing at most 15 minutes of transaction data." That 15 minutes is the RPO — backups must occur at least every 15 minutes to meet this objective.

RPO drives backup frequency and replication requirements.

### Carrier SLA Provisions

When evaluating a carrier WAN or internet service SLA, look for:

- Availability guarantee (e.g., 99.99% uptime)
- Latency commitment (e.g., average latency under 50 ms)
- Packet loss commitment (e.g., less than 0.1%)
- Jitter commitment (e.g., less than 10 ms average)
- Mean Time to Repair (e.g., 4-hour MTTR for major circuit outages)
- Service credits: What compensation the carrier provides if they miss SLA metrics. Typically a percentage of monthly recurring charges.

---

## Section 3: Disaster Recovery Documentation

Disaster Recovery (DR) documentation defines how the organization responds to and recovers from major failures — extended power outages, natural disasters, ransomware attacks, or catastrophic hardware failures.

### Business Impact Analysis

Before writing a DR plan, organizations conduct a Business Impact Analysis (BIA). The BIA identifies:

- Which business processes are most critical
- What happens to the business if each process fails
- How long each process can be interrupted before causing unacceptable business impact
- The RTO and RPO for each process

The BIA output drives the DR design — high-impact, low-tolerance processes get the most investment in redundancy and rapid recovery.

### DR Site Types

#### Hot Site

A hot site is a fully equipped, operational facility that mirrors the production environment. All hardware is running; data is replicated in real time. Failover can happen within minutes.

Cost: Very high — you are running duplicate production infrastructure.

Use case: Financial services, healthcare, any organization where downtime costs are catastrophic.

#### Warm Site

A warm site has hardware pre-installed and configured but data must be restored from backup or synchronization. Failover takes hours to a day.

Cost: Moderate — hardware is maintained but not fully operational.

Use case: Organizations with RTO measured in hours rather than minutes.

#### Cold Site

A cold site is a facility with power, space, and network connectivity but no pre-installed hardware. Equipment must be procured and installed during the disaster. Failover takes days to weeks.

Cost: Low — minimal infrastructure maintained.

Use case: Organizations with RPOs and RTOs measured in days; non-critical workloads.

### DR Plan Components

A complete DR plan includes:

- **Purpose and scope**: What scenarios the plan covers.
- **Recovery team and roles**: Who is responsible for what during a disaster. Contact list with 24/7 phone numbers.
- **Activation criteria**: What conditions trigger the DR plan (e.g., primary data center inaccessible for more than X hours).
- **Recovery procedures**: Step-by-step technical procedures for each critical system. Written clearly enough for someone who did not design the system.
- **Communication plan**: How the team communicates during a disaster. What information is provided to stakeholders and when.
- **Vendor and carrier contacts**: Critical contacts for hardware vendors, ISPs, and carrier circuits.
- **Testing schedule**: DR plans that are never tested are not real DR plans. Annual or semi-annual tests are standard practice.
- **Plan maintenance**: Who reviews and updates the plan, and when.

### DR Testing Methods

- **Tabletop exercise**: The team walks through the DR plan verbally, discussing what each person would do during a hypothetical scenario. Low cost, no system disruption. Good for identifying gaps in the plan.
- **Walkthrough test**: Team members perform their assigned tasks up to the point of actual failover. Verifies procedures without actual production impact.
- **Simulation test**: A simulated disaster is declared and the team activates DR procedures in a controlled environment. Actual failover may be tested.
- **Full interruption test**: Production systems are actually failed over to the DR site. Highest confidence but highest risk and cost. Requires careful scheduling and stakeholder approval.

---

## Section 4: Network Policies Reference

Several additional policies are important for network administrators. These may appear on the Network+ exam.

### Password Policy

Defines requirements for user and administrator passwords:

- Minimum length (typically 12+ characters for network device credentials)
- Complexity requirements (uppercase, lowercase, numbers, special characters)
- Expiration interval
- Account lockout after failed attempts
- Prohibition on password reuse

Network device default passwords must always be changed before deployment.

### Remote Access Policy

Defines how users and administrators connect to the network remotely:

- Approved VPN clients and protocols
- Multi-factor authentication requirements
- Split tunneling — permitted or prohibited
- Device health requirements (endpoint must have current antivirus, OS patches)
- Acceptable use restrictions while connected remotely

### Incident Response Policy

Defines how the organization responds to security incidents:

- Incident classification (severity levels)
- Incident response team and contact information
- Escalation procedures
- Evidence preservation requirements
- Reporting obligations (regulatory, legal)
- Post-incident review requirements

### Physical Security Policy

Addresses physical access to network infrastructure:

- Server room and data center access controls (key cards, biometrics)
- Visitor escort requirements
- Hardware removal authorization
- Clean desk requirements
- Equipment disposal procedures

---

## Summary of Part 2

Key points from Part 2:

- AUPs define permitted and prohibited network use, establish privacy expectations, and must be signed by users.
- SLA metrics: Availability (nines), MTBF, MTTR, RTO, and RPO. Know the downtime equivalents for 99%, 99.9%, 99.99%, and 99.999% availability.
- Disaster recovery sites: Hot (real-time, expensive), Warm (hours, moderate cost), Cold (days, low cost). DR plans must be tested — tabletop, walkthrough, simulation, full interruption.
- Additional policies: Password policy, remote access policy, incident response policy, physical security policy.

Module 15 is complete. Work through the Reading Guide, Lab, Quiz, and Discussion. Module 16 is our final module — a comprehensive Network+ exam preparation session covering all domains.
