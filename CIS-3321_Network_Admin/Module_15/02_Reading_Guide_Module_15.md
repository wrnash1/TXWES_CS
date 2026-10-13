# Reading Guide: Module 15 — Network Documentation and Policies

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Overview

This reading guide supports Module 15 video lectures and prepares you for the quiz and the CompTIA Network+ N10-008 exam. Documentation and operational policies are tested throughout Domain 3 (Network Operations). Understanding SLA metrics, change management, and DR terminology requires precise definition — do not paraphrase these terms on the exam.

**Estimated Reading Time:** 55–65 minutes

---

## Part 1: Network Diagrams

### 1.1 Diagram Types and Content

#### Logical Network Diagram

Purpose: Shows how the network is organized logically — IP addressing, routing, VLANs, traffic flows.

Content includes:

- Device hostnames and types (using standardized icons)
- IP addresses on all interfaces
- Subnet boundaries and VLAN IDs
- Routing protocol indicators (OSPF areas, EIGRP AS numbers)
- WAN circuit identifiers and bandwidth
- Demarcation points
- Cloud and internet boundaries
- Security zones (DMZ, internal, external)

Use cases: Network design planning, troubleshooting, security reviews, new staff orientation

#### Physical Network Diagram

Purpose: Shows actual physical connections, hardware locations, and cable plant.

Content includes:

- Device make/model and serial numbers
- Physical port connections (e.g., "Switch1 Fa0/1 → Server1 NIC1")
- Cable types and lengths
- Patch panel locations and port assignments
- Rack diagrams (U-position of each device)
- Building floor plans showing wiring closet locations
- External demarcation points

Use cases: Cable management, hardware replacement, physical security, data center layout

#### Rack Diagram

A specialized physical diagram showing the front-face layout of a rack:

- Each device shown at its actual height in rack units (U)
- Device name, model, and power consumption
- Cable management panels and patch panels
- Blank panels and power distribution units (PDUs)

### 1.2 Diagram Maintenance

| Practice | Rationale |
|---|---|
| Update after every physical change | Stale diagrams mislead troubleshooters |
| Version control with dates | Enables rollback to previous topology understanding |
| Shared team access | All team members need current diagrams |
| Periodic review | Catches undocumented drift — quarterly recommended |

### 1.3 Diagram Tools

- Microsoft Visio — industry-standard diagramming tool
- draw.io (diagrams.net) — free browser-based; Visio-compatible
- Lucidchart — cloud-based collaborative diagramming
- NetBox — open-source network documentation platform with auto-generated diagrams
- SolarWinds Network Topology Mapper — auto-discovers and maps physical topology

---

## Part 2: IP Address Management (IPAM)

### 2.1 IPAM Concepts

IP Address Management is the planning, tracking, and management of IP address space.

Core IPAM components:

- **Subnet planning**: Allocating address space to network segments with correct prefix lengths
- **IP assignment tracking**: Recording which device has each address (hostname, MAC, location, purpose)
- **Conflict detection**: Identifying duplicate IP addresses before or after assignment
- **Utilization reporting**: Tracking how much of each subnet is in use

### 2.2 IPAM Documentation Fields

For each managed subnet, document:

- Network address and prefix (e.g., 192.168.20.0/24)
- VLAN association (e.g., VLAN 20 — Finance)
- Gateway address
- DHCP scope range (start to end)
- DHCP exclusions (statically assigned addresses to reserve)
- Physical/logical location
- Purpose description

For each statically assigned address, document:

- IP address
- Hostname (DNS name)
- MAC address
- Device type and model
- Physical location
- Owner/contact
- Date assigned

### 2.3 DDI — DNS, DHCP, IPAM Integration

Enterprise IPAM integrates three services (DDI):

- **DNS**: Automatically creates and removes A records and PTR records as devices are added or removed
- **DHCP**: Records all dynamic leases; flags conflicts; manages scope utilization
- **IPAM**: Unified view of all address allocations — static and dynamic

DDI platforms: Infoblox, BlueCat, SolarWinds IPAM, phpIPAM (open source), NetBox (open source)

---

## Part 3: Change Management

### 3.1 Change Management Process

| Step | Description |
|---|---|
| Change Request submitted | Requestor documents change, justification, risk, rollback plan |
| Change reviewed | Technical review by peers for completeness and accuracy |
| CAB approval | Change Advisory Board approves scheduling and authorizes implementation |
| Pre-change communication | Stakeholders notified of planned maintenance window |
| Implementation | Change implemented during approved window |
| Verification | Requestor confirms change success; tests affected systems |
| Post-change documentation | Change record updated with actual steps, outcome, and any deviations |

### 3.2 Change Types

#### Standard Change

- Pre-approved procedure for routine, low-risk activities
- No individual CAB review required per occurrence
- Examples: Adding a workstation to a VLAN, rebooting a switch per scheduled maintenance
- Must follow a documented and previously approved procedure exactly

#### Normal Change

- Requires CAB review and approval before implementation
- Submitted at least 24–72 hours before planned implementation (varies by organization)
- Examples: Firewall rule changes, router configuration updates, VLAN redesign, firmware upgrades

#### Emergency Change

- Unplanned, urgent change required immediately to restore service or address a security threat
- Expedited or verbal approval from authority (CTO, IT manager, security officer)
- Full documentation must be completed after the fact — never skip documentation even for emergencies
- Subject to post-incident review

### 3.3 Change Request Contents

A complete Change Request includes:

- Change title and reference number
- Submitter and assigned implementer
- Date/time submitted and proposed implementation window
- Description of the change (what exactly will be done)
- Business justification (why is this needed?)
- Impact assessment (who/what is affected, expected outage duration)
- Risk rating (Low / Medium / High) with rationale
- Rollback plan (step-by-step instructions to undo the change)
- Test plan (how success will be verified)
- Required approvals

### 3.4 Configuration Baseline and Drift

A configuration baseline is the documented, approved configuration state for a device or system type.

Configuration drift occurs when a device's running configuration diverges from the baseline — through unauthorized changes, ad-hoc fixes, or accumulated temporary changes that were never formalized.

Tools that detect drift:

- RANCID (free) — backs up device configs; alerts on changes
- Oxidized (free) — modern RANCID replacement
- SolarWinds NCM — enterprise configuration management
- Cisco DNA Center — Cisco-specific intent-based policy enforcement

---

## Part 4: Service Level Agreements

### 4.1 SLA Metrics Reference

#### Availability (Uptime)

| SLA Level | Downtime per Year | Downtime per Month |
|---|---|---|
| 99% | 87.6 hours | 7.3 hours |
| 99.9% | 8.76 hours | 43.8 minutes |
| 99.99% | 52.6 minutes | 4.38 minutes |
| 99.999% | 5.26 minutes | 26.3 seconds |

Calculate allowed downtime: (1 - availability%) × period in minutes

Example: 99.9% monthly = (0.001) × 43,800 minutes/month = 43.8 minutes per month allowed.

#### MTBF — Mean Time Between Failures

MTBF = Total uptime / Number of failures

Used for hardware reliability comparisons. Higher MTBF = more reliable.

Example: A switch runs for 100,000 hours and fails 4 times → MTBF = 25,000 hours

#### MTTR — Mean Time to Repair

MTTR = Total repair time / Number of repairs

Measures how quickly the team restores service. Lower MTTR = faster recovery.

#### RTO — Recovery Time Objective

Maximum tolerable downtime before business impact becomes unacceptable. Defined per system or process.

Example: "ERP system RTO = 4 hours" — the ERP must be restored within 4 hours of any failure.

#### RPO — Recovery Point Objective

Maximum acceptable data loss measured in time. Defines backup/replication frequency needed.

Example: "RPO = 1 hour" — backups must occur at least hourly so no more than 1 hour of data can be lost.

### 4.2 RTO vs. RPO Relationship

| RTO | RPO | Implication |
|---|---|---|
| Low (minutes) | Low (minutes) | Hot site + real-time replication required |
| Low (hours) | Low (hours) | Warm site + frequent backups |
| High (days) | High (days) | Cold site + daily backups acceptable |

Lower RTO/RPO = higher cost. Organizations must match DR investment to business impact.

---

## Part 5: Acceptable Use Policies

### 5.1 AUP Core Elements

| Section | Content |
|---|---|
| Permitted use | Business use; limited personal use if authorized |
| Prohibited activities | Illegal downloads, adult content, gambling, circumventing security controls |
| Privacy notice | Organization monitors network; no expectation of privacy |
| Security responsibilities | Password management, clean desk, workstation locking |
| BYOD rules | Personal device requirements for corporate network access |
| Remote access rules | VPN requirements, home network security |
| Consequences | Disciplinary action, termination, legal action |

### 5.2 AUP Enforcement Technical Controls

Network administrators implement technical controls that enforce AUP provisions:

- Content filtering (web proxy, DNS filtering) — blocks prohibited websites
- Application control (firewall/NGFW DPI) — blocks unauthorized applications
- Bandwidth management — throttles non-business traffic during business hours
- Network access control (NAC) — enforces device compliance before allowing access
- Monitoring and logging — captures network activity for audit and investigation

---

## Part 6: Disaster Recovery Documentation

### 6.1 DR Site Types

| Site Type | State | Failover Time | Cost |
|---|---|---|---|
| Hot site | Fully operational; data replicated in real time | Minutes | Very high |
| Warm site | Hardware ready; data must be restored | Hours to 1 day | Moderate |
| Cold site | Facility only; hardware must be procured/installed | Days to weeks | Low |

### 6.2 DR Plan Structure

1. Purpose, scope, and objectives
2. Recovery team — roles and 24/7 contact information
3. Activation criteria — conditions that trigger the plan
4. System inventory — critical systems with RTO/RPO targets
5. Recovery procedures — step-by-step per system (must be usable under stress)
6. Communication plan — internal and external notifications
7. Vendor/carrier contacts — emergency numbers for ISP, hardware vendors
8. Testing schedule and results history
9. Plan review and approval signatures

### 6.3 DR Testing Methods

| Method | Description | Disruption | Cost |
|---|---|---|---|
| Tabletop exercise | Verbal walkthrough of scenario | None | Low |
| Walkthrough test | Perform procedures without actual failover | Minimal | Low–moderate |
| Simulation test | Declare disaster; activate DR in controlled environment | Low | Moderate |
| Full interruption test | Actually fail over production to DR site | Significant | High |

Annual testing is standard. Mission-critical systems should test more frequently.

---

## Key Terms Glossary

- **AUP**: Acceptable Use Policy — defines permitted and prohibited network use.
- **BIA**: Business Impact Analysis — identifies critical processes and their recovery requirements.
- **CAB**: Change Advisory Board — group that reviews and approves changes.
- **Change Request**: Formal document proposing a change to a production system.
- **Cold site**: DR facility with space and power; no pre-installed equipment.
- **Configuration baseline**: Documented approved configuration state for a device.
- **Configuration drift**: Deviation of a running configuration from the baseline.
- **DDI**: DNS, DHCP, IPAM — integrated address management suite.
- **Emergency change**: Urgent, expedited change to restore service or address a security threat.
- **Hot site**: Fully operational DR facility with real-time data replication.
- **IPAM**: IP Address Management.
- **MTBF**: Mean Time Between Failures.
- **MTTR**: Mean Time to Repair.
- **Normal change**: Standard change requiring CAB approval.
- **RPO**: Recovery Point Objective — maximum acceptable data loss in time.
- **RTO**: Recovery Time Objective — maximum acceptable system downtime.
- **SLA**: Service Level Agreement.
- **Standard change**: Pre-approved routine change not requiring individual CAB review.
- **Warm site**: DR facility with pre-installed hardware; data must be restored.

---

## Review Questions

1. What is the difference between a logical network diagram and a physical network diagram? Give two examples of information found in each.

2. Calculate the maximum monthly downtime allowed by a 99.99% availability SLA.

3. What is the difference between RTO and RPO? Give an example of each.

4. A company has an RPO of 15 minutes for its transaction database. What backup or replication strategy does this require?

5. List the three change management types and describe one scenario that would fall into each category.

6. What must a Change Request include in addition to the description of the change?

7. What is the difference between a hot site and a warm site for disaster recovery?

8. What is configuration drift and how can it be detected automatically?

9. Name three technical controls that network administrators implement to enforce AUP provisions.

10. What is the purpose of a tabletop exercise in disaster recovery testing, and what are its limitations compared to a full interruption test?

---

## 9. Supplemental Resources

The following free resources extend Module 15 content on network documentation, change management, IPAM, and disaster recovery planning.

**1. Professor Messer — Network Management and Documentation Free Videos (N10-008)**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer covers network documentation (logical/physical diagrams, baseline), change management procedures, IPAM concepts, and disaster recovery terminology (RTO, RPO, hot/warm/cold sites) in videos directly aligned to Network+ Domain 3.0 and Domain 4.0 exam objectives.

**2. NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems (Free)**
URL: https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final
Relevance: NIST's free authoritative guide on IT contingency planning covers BIA methodology, RTO/RPO target-setting, DR site types, backup strategies, and DR testing methods. Directly applicable to the disaster recovery content in this module and frequently referenced in enterprise DR planning.

**3. ITIL Foundation — Change Management Overview (Free Summary)**
URL: https://www.axelos.com/certifications/itil-service-management/itil-4-foundation
Relevance: ITIL (IT Infrastructure Library) defines the industry-standard change management framework used by enterprise IT organizations — normal, standard, and emergency change types, CAB structure, and change request documentation requirements match Module 15 change management content.

**4. Men & Mice — IPAM Best Practices Guide (Free)**
URL: https://www.menandmice.com/resources/
Relevance: Men & Mice (now part of BlueCat) provides free IPAM educational resources covering subnet allocation planning, address utilization monitoring, DDI integration (DNS+DHCP+IPAM), and IPAM database design — directly applicable to the IPAM spreadsheet and management concepts in this module.

**5. draw.io — Free Network Diagramming Tool**
URL: https://app.diagrams.net/
Relevance: draw.io is a completely free, browser-based diagramming tool with built-in network shape libraries (Cisco, AWS, Azure icons). It can export to PNG, PDF, and Visio formats — the recommended free alternative for creating the logical and physical network diagrams required in the Module 15 lab.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
