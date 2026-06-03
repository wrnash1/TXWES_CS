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
