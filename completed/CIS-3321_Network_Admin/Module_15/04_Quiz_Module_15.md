# Quiz: Module 15 — Network Documentation and Policies

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. This quiz covers Module 15 video lectures and reading guide material.

---

## Questions

### Question 1

A network diagram shows IP addressing schemes, VLAN assignments, routing protocols, and traffic flows, but does not show cable routes or physical port connections. Which type of diagram is this?

- A) Physical network diagram
- B) Rack diagram
- C) Logical network diagram
- D) Topology map

Correct Answer: C

Explanation: A logical network diagram shows how the network is organized logically — IP addressing, VLANs, routing, traffic flows — without necessarily depicting physical locations or cable runs. A physical diagram shows actual device locations, port connections, and cable plant.

---

### Question 2

A 99.99% availability SLA allows how much maximum annual downtime?

- A) 8.76 hours
- B) 87.6 hours
- C) 52.6 minutes
- D) 5.26 minutes

Correct Answer: C

Explanation: 99.99% availability means 0.01% downtime allowed. 0.0001 × 525,600 minutes/year = 52.56 minutes per year. This is the "four nines" SLA level. 8.76 hours corresponds to 99.9% (three nines); 87.6 hours to 99% (two nines); 5.26 minutes to 99.999% (five nines).

---

### Question 3

An organization's business continuity plan states that the ERP system must be restored within 2 hours of any failure, and no more than 30 minutes of transaction data may be lost. Which terms correctly describe these two requirements?

- A) RTO = 30 minutes, RPO = 2 hours
- B) MTTR = 2 hours, MTBF = 30 minutes
- C) RTO = 2 hours, RPO = 30 minutes
- D) RPO = 2 hours, SLA = 30 minutes

Correct Answer: C

Explanation: RTO (Recovery Time Objective) is the maximum acceptable downtime — 2 hours here. RPO (Recovery Point Objective) is the maximum acceptable data loss measured in time — 30 minutes here, meaning backups must occur at least every 30 minutes.

---

### Question 4

An administrator discovers that a router's running configuration has been modified from the organization's approved baseline without any corresponding change request. What has occurred?

- A) An emergency change that was properly expedited
- B) Configuration drift — an unauthorized deviation from the baseline
- C) A standard change that did not require CAB approval
- D) A normal change that was approved verbally

Correct Answer: B

Explanation: When a device's running configuration diverges from the approved baseline without a documented change, this is called configuration drift. It indicates an unauthorized change — potentially a security incident. Configuration management tools (RANCID, Oxidized, SolarWinds NCM) detect and alert on such deviations.

---

### Question 5

A network engineer needs to push a critical security patch to a core router at 11 PM to address an actively exploited vulnerability. No scheduled maintenance window exists. Which change type is most appropriate?

- A) Standard change — follows a pre-approved procedure
- B) Normal change — requires full CAB review and scheduling
- C) Emergency change — urgent, expedited approval required
- D) Unauthorized change — no process exists for unscheduled changes

Correct Answer: C

Explanation: An actively exploited vulnerability requiring immediate patching qualifies as an emergency change — urgent action is needed to prevent security harm. Emergency changes receive expedited (often verbal) approval from appropriate authority and must be fully documented after implementation.

---

### Question 6

A new employee connects to the company Wi-Fi and is redirected to a page requiring them to read and click "I Accept" before accessing the network. This is the primary mechanism for which document?

- A) Service Level Agreement
- B) Acceptable Use Policy acknowledgment
- C) Change Request approval
- D) Network diagram access authorization

Correct Answer: B

Explanation: The captive portal requiring acknowledgment before network access is the delivery mechanism for the Acceptable Use Policy (AUP). This electronic acknowledgment creates a record that the user has read and accepted the AUP — giving the organization recourse if the policy is later violated.

---

### Question 7

An organization's primary data center is destroyed by flooding. At its disaster recovery site, all network hardware is pre-installed, powered on, and running. Data is replicated to this site in real time. Failover can be completed within 15 minutes. Which DR site type is this?

- A) Cold site
- B) Warm site
- C) Hot site
- D) Mirrored site

Correct Answer: C

Explanation: A hot site is fully operational with real-time data replication — failover takes minutes. A warm site has pre-installed hardware but data must be restored from backup (hours). A cold site has only facility infrastructure — no pre-installed hardware (days to weeks).

---

### Question 8

What is the primary purpose of including a rollback plan in a Change Request?

- A) To satisfy regulatory documentation requirements
- B) To provide step-by-step instructions to restore the previous configuration if the change causes problems
- C) To document what the change accomplished after it is complete
- D) To identify which team member implemented the change

Correct Answer: B

Explanation: The rollback plan defines exactly how to undo the change and restore the previous working state if the implementation causes problems. Without a rollback plan, a failed change can extend an outage significantly while the team figures out how to reverse what was done.

---

### Question 9

An organization runs full interruption disaster recovery testing annually. During the test, production systems are actually failed over to the DR site. What is the main benefit of this test type compared to a tabletop exercise?

- A) It requires less time and causes no disruption
- B) It provides the highest confidence that DR procedures actually work in a real failure scenario
- C) It satisfies all regulatory testing requirements without any risk
- D) It eliminates the need for a DR plan update afterward

Correct Answer: B

Explanation: Full interruption testing is the only method that proves the DR site and procedures work under real conditions — including actual failover and system operation from the DR site. Tabletop exercises identify plan gaps through discussion but cannot reveal technical issues that only appear during actual failover.

---

### Question 10

Which IPAM tool integrates DNS, DHCP, and IP address management into a unified platform, allowing automatic DNS record creation when addresses are assigned?

- A) Wireshark
- B) Packet Tracer
- C) DDI platform (e.g., Infoblox, BlueCat)
- D) Nmap

Correct Answer: C

Explanation: DDI stands for DNS, DHCP, and IPAM — an integrated platform that manages all three services together. DDI platforms like Infoblox and BlueCat automatically create DNS records when DHCP leases are issued and remove them when leases expire, maintaining accurate DNS-to-IP mappings without manual intervention.

---

### Question 11

A network diagram shows the physical location of all devices, cable runs, rack positions, and patch panel port assignments. Which type of diagram is this?

- A) Logical network diagram
- B) Physical network diagram
- C) Layer 3 topology diagram
- D) Application dependency map

**Correct Answer:** B

**Distractor Analysis:**
- *Why A is incorrect:* A logical network diagram shows IP addressing, VLANs, routing domains, and protocol relationships — it does not depict physical locations, rack positions, or cable runs.
- *Why B is correct:* A physical network diagram documents the real-world placement of devices — floor plans, rack diagrams, cable paths, and patch panel connections. It is used by facilities and cabling teams.
- *Why C is incorrect:* A Layer 3 topology diagram is a type of logical diagram showing routing relationships and IP addressing — it does not include physical location detail.
- *Why D is incorrect:* An application dependency map shows which systems depend on each other — it is an application-layer view, not a physical infrastructure diagram.

---

### Question 12

An organization's financial database has an RPO of 15 minutes. Which backup or replication strategy is required to meet this objective?

- A) Daily full backup at midnight
- B) Incremental backup every 4 hours
- C) Real-time or near-real-time replication with transaction log shipping every 15 minutes or less
- D) Weekly full backup with daily differential backups

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* A nightly full backup would allow up to 24 hours of data loss — far exceeding a 15-minute RPO.
- *Why B is incorrect:* A 4-hour incremental backup interval means up to 4 hours of data could be lost — this violates the 15-minute RPO by a factor of 16.
- *Why C is correct:* RPO of 15 minutes means no more than 15 minutes of data can be lost. This requires continuous replication or transaction log shipping at intervals of 15 minutes or less.
- *Why D is incorrect:* Weekly full with daily differential could mean up to 24 hours of data loss — completely incompatible with a 15-minute RPO.

---

### Question 13

During a change management process, a technician plans to upgrade the firmware on all core switches at 2 AM Sunday. The change was reviewed by the CAB, approved, and has a documented rollback procedure. Which change type is this?

- A) Emergency change
- B) Standard change
- C) Normal change
- D) Unauthorized change

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* An emergency change is an expedited change to restore service or address an active security threat — it bypasses normal CAB review because of urgency. A planned maintenance window is not an emergency.
- *Why B is incorrect:* A standard change is a pre-approved, routine, low-risk change (like adding a VLAN or creating a user account) that does not require individual CAB review each time.
- *Why C is correct:* A normal change follows the full change management process — change request submitted, reviewed by the CAB, approved, scheduled, implemented with a documented rollback plan. A core switch firmware upgrade in a maintenance window is a normal change.
- *Why D is incorrect:* An unauthorized change is one implemented without following the change management process — this change went through full CAB review.

---

### Question 14

An organization's SLA guarantees 99.9% monthly uptime. What is the maximum downtime allowed per month?

- A) 8.76 hours
- B) 43.8 minutes
- C) 4.38 minutes
- D) 5.26 minutes

**Correct Answer:** B

**Distractor Analysis:**
- *Why A is incorrect:* 8.76 hours is the maximum annual downtime for 99.9% availability — not monthly. Monthly = 8.76/12 = 43.8 minutes.
- *Why B is correct:* 99.9% monthly availability = 0.1% downtime. A 30-day month has 43,200 minutes. 0.001 × 43,200 = 43.2 minutes ≈ 43.8 minutes (using 30.5-day average month).
- *Why C is incorrect:* 4.38 minutes per month corresponds to 99.99% availability — one additional nine of uptime.
- *Why D is incorrect:* 5.26 minutes is the annual downtime for 99.999% (five nines) availability — not 99.9% monthly.

---

### Question 15

A network administrator discovers that a router's running configuration has been manually modified directly on the device without a change request, bypassing the change management process. This is an example of which problem?

- A) Configuration baseline
- B) Configuration drift
- C) SLA violation
- D) Emergency change

**Correct Answer:** B

**Distractor Analysis:**
- *Why A is incorrect:* A configuration baseline is the documented approved state of the device — it is the standard being violated here, not the problem itself.
- *Why B is correct:* Configuration drift occurs when a device's running configuration diverges from its approved baseline. Unauthorized direct modifications are a common cause of drift, which can introduce security vulnerabilities and instability.
- *Why C is incorrect:* An SLA violation refers to failing to meet uptime or performance guarantees — not an unauthorized configuration change.
- *Why D is incorrect:* An emergency change is an authorized expedited change following an abbreviated process — the scenario describes an unauthorized change that bypassed all process.

---

### Question 16

What metric measures the average time elapsed from when a failure occurs to when the system is fully restored to service?

- A) MTBF
- B) RTO
- C) MTTR
- D) RPO

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* MTBF (Mean Time Between Failures) measures the average interval between failures — it indicates how often failures occur, not how long repairs take.
- *Why B is incorrect:* RTO (Recovery Time Objective) is the maximum tolerable downtime — it is a target or business requirement, not a measured operational metric.
- *Why C is correct:* MTTR (Mean Time to Repair) = Total repair time / Number of repairs. It measures the team's actual average restoration speed — a lower MTTR indicates faster recovery capability.
- *Why D is incorrect:* RPO (Recovery Point Objective) defines maximum acceptable data loss in time — it is related to backup frequency, not repair time.

---

### Question 17

A company's DR plan specifies that in the event of a datacenter failure, the backup site has pre-installed servers and networking equipment but requires restoration of data from the most recent backup tape, which takes 6–8 hours. Which DR site type is this?

- A) Hot site
- B) Cold site
- C) Warm site
- D) Mirror site

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* A hot site is fully operational with real-time data replication — failover takes minutes, not hours. There is no tape restoration step.
- *Why B is incorrect:* A cold site provides only physical facility space and power — hardware must be procured or shipped and installed, which takes days to weeks.
- *Why C is correct:* A warm site has hardware pre-installed and ready but requires data restoration from recent backups. Failover typically takes hours to one day — matching the 6–8 hour tape restoration scenario.
- *Why D is incorrect:* A mirror site is effectively a hot site with continuous synchronization — failover is near-instantaneous. "Mirror site" is not a standard CompTIA DR tier term.

---

### Question 18

An organization's IPAM system sends an alert indicating that a subnet has reached 90% address utilization. Which action should the network administrator take FIRST?

- A) Immediately expand the subnet by renumbering all devices to a larger CIDR block
- B) Investigate which addresses are actively in use versus expired or ghost entries, and clean up stale records
- C) Block all new DHCP leases to prevent address exhaustion
- D) Migrate all devices in the subnet to IPv6

**Correct Answer:** B

**Distractor Analysis:**
- *Why A is incorrect:* Renumbering all devices is a major disruptive change that should only follow investigation — many apparent address shortages are caused by stale IPAM records for decommissioned devices.
- *Why B is correct:* Before any drastic action, the administrator should audit current usage — reconcile IPAM records against active DHCP leases and ARP tables. Stale entries for removed devices often inflate utilization figures. Cleaning up ghost records may resolve the problem without any infrastructure change.
- *Why C is incorrect:* Blocking new leases would cause immediate user-facing outages — this is not an appropriate first response to an alert.
- *Why D is incorrect:* IPv6 migration is a long-term strategic project — it does not resolve an immediate IPv4 subnet exhaustion situation.

---

### Question 19

Which type of DR test actually fails production systems over to the disaster recovery site, providing the highest confidence in recovery procedures but also the highest risk and cost?

- A) Tabletop exercise
- B) Walkthrough test
- C) Simulation test
- D) Full interruption test

**Correct Answer:** D

**Distractor Analysis:**
- *Why A is incorrect:* A tabletop exercise is a verbal discussion walkthrough — no systems are touched and no failover occurs. It tests plan knowledge, not technical execution.
- *Why B is incorrect:* A walkthrough test has teams physically go through DR procedures step-by-step without actually failing over production — it verifies process without production risk.
- *Why C is incorrect:* A simulation test activates DR procedures in a controlled environment while production continues running — it does not actually fail over production traffic.
- *Why D is correct:* A full interruption test is the only method that actually shuts down production systems and operates from the DR site, exactly replicating a real disaster. It has the highest confidence value but also the highest risk of extended downtime if the DR site has undiscovered issues.

---

### Question 20

A network administrator is creating a change request for replacing a failed UPS in the server room during a Sunday maintenance window. The replacement procedure is identical to the last four UPS replacements, which all went smoothly. Which change type most efficiently handles this situation?

- A) Emergency change — UPS failure is an infrastructure emergency requiring immediate bypass of normal process
- B) Normal change — requires full CAB review and approval for each individual UPS replacement
- C) Standard change — a pre-approved routine change with documented procedure that does not require individual CAB review
- D) Unauthorized change — hardware replacements do not require change management documentation

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* An emergency change is for urgent situations requiring expedited approval — a planned Sunday maintenance window is not an emergency, even if the UPS has failed.
- *Why B is incorrect:* A normal change requires individual CAB review each time — this is appropriate for complex or higher-risk changes, not for a routine replacement with a proven procedure performed multiple times.
- *Why C is correct:* A standard change is a pre-approved, low-risk, frequently performed change with a documented and tested procedure. UPS replacement following a proven procedure that has been performed successfully four times qualifies — it is added to the standard change catalog and executed without individual CAB review.
- *Why D is incorrect:* Hardware replacements do require change management documentation — skipping the process entirely creates configuration drift, audit gaps, and accountability issues.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
