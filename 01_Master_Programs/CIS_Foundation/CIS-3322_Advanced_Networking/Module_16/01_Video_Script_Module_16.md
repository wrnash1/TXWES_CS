# Video Script: Module 16 — CCNA 200-301 Exam Preparation and Capstone

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Estimated Duration: 24 Minutes

---

## Segment 1: Introduction (0:00–2:00)

Welcome to Module 16 — your final module in CIS-3322 Advanced Networking and your capstone preparation session for the Cisco CCNA 200-301 exam. I'm Professor Nash, and over the next 24 minutes we are going to do something different. Instead of introducing new material, we are going to synthesize everything you have learned across all 16 modules, review the exam domains, and walk through exam strategy so that you are fully prepared to sit for CCNA.

By the end of this session you will be able to:

* Summarize all six CCNA 200-301 exam domains and their weighting
* Identify which topics require the deepest review based on exam domain weight
* Apply a proven exam strategy to eliminate distractors and select correct answers under time pressure
* Understand the capstone lab expectations for this course

Let's begin with a look at what the exam actually tests.

---

## Segment 2: CCNA 200-301 Exam Domain Review (2:00–8:00)

The CCNA 200-301 exam covers six domains. Each domain has a specific percentage weight, which tells you how much of the exam is drawn from that topic area. Here are all six:

### Domain 1.0 — Network Fundamentals (20%)

This is the largest single domain. It covers the OSI and TCP/IP models, IP addressing and subnetting, IPv6, routing concepts, switching fundamentals, and basic network topology understanding. If you are going to invest extra review time, start here.

Key topics: IPv4 and IPv6 addressing, subnetting with VLSM, OSI layer functions, TCP vs. UDP, Ethernet frame structure, MAC addresses, and basic router/switch operation.

### Domain 2.0 — Network Access (20%)

Equal weight to fundamentals. Covers VLANs, trunking (802.1Q), inter-VLAN routing, Spanning Tree Protocol (STP), EtherChannel, wireless 802.11 standards, WLC architecture, and CAPWAP.

Key topics: VLAN configuration, trunk port configuration, STP port states, RSTP enhancements, wireless 802.11 amendment characteristics, WPA2 vs. WPA3.

### Domain 3.0 — IP Connectivity (25%)

The largest domain by weight. Covers static routing, dynamic routing (OSPF), first-hop redundancy protocols (HSRP), and IPv6 routing.

Key topics: OSPF neighbor formation, OSPF DR/BDR election, static routes including default routes, HSRP states and priorities, floating static routes.

### Domain 4.0 — IP Services (10%)

Covers NAT (Static, Dynamic, PAT), NTP, SNMP, Syslog, DHCP, DNS, QoS concepts, SSH configuration, and FTP/TFTP.

Key topics: PAT configuration, NTP stratum levels, syslog severity levels (0–7), DHCP snooping, SNMP versions (v2c vs. v3).

### Domain 5.0 — Security Fundamentals (15%)

Covers AAA, RADIUS, TACACS+, port security, DHCP snooping, Dynamic ARP Inspection, 802.1X, and VPN concepts.

Key topics: RADIUS vs. TACACS+ differences, port security violation modes, DHCP snooping trusted/untrusted ports, 802.1X authenticator role, IPsec vs. SSL VPN.

### Domain 6.0 — Automation and Programmability (15%)

Covers SDN architecture, northbound/southbound APIs, REST API methods, JSON/XML, NETCONF/RESTCONF, and automation tools.

Key topics: API directions from the controller, HTTP CRUD mapping, Ansible agentless push model, NETCONF on SSH port 830, DNA Center role.

---

## Segment 3: Top Tested Topics Per Domain (8:00–13:00)

Based on community reports and Cisco's published exam topics, here are the highest-frequency topics in each domain.

### Network Fundamentals — Highest Frequency

Subnetting questions appear on every sitting of the CCNA exam. You must be able to calculate network address, broadcast address, usable host range, and subnet mask — within 30–45 seconds. Practice until these calculations are automatic.

IPv6 address types — link-local, global unicast, unique local, multicast — appear frequently. Know the prefix ranges: FE80::/10 for link-local, 2000::/3 for global unicast, FC00::/7 for unique local.

OSI layer identification — given a protocol or device, identify its layer — is tested in almost every scenario question.

### Network Access — Highest Frequency

VLAN and trunking configuration syntax appears in scenario questions. Know the difference between `switchport mode access`, `switchport mode trunk`, and `switchport nonegotiate`. Know the native VLAN security risk.

STP port states and the difference between STP and RSTP. RSTP reduces convergence time by pre-negotiating port roles. Know the five STP port states: blocking, listening, learning, forwarding, disabled.

### IP Connectivity — Highest Frequency

OSPF is heavily tested. Know the DR/BDR election process — highest router ID wins, or highest priority (default 1). Know OSPF neighbor states from down through full. Know that OSPF uses cost based on bandwidth.

Static routes — including default routes with `ip route 0.0.0.0 0.0.0.0` and floating static routes with higher administrative distance — appear in every exam. Know the administrative distance for all major protocols.

### IP Services — Highest Frequency

NAT and PAT configuration and verification. Know the difference between inside local, inside global, outside local, and outside global address types. Know the `show ip nat translations` command output format.

NTP stratum levels. A stratum 0 source is an atomic clock. A stratum 1 server connects directly to stratum 0. Each hop adds one stratum. The maximum useful stratum is 15; stratum 16 means unreachable.

---

## Segment 4: Exam Strategy (13:00–17:00)

The CCNA 200-301 exam has 100–120 questions to complete in 120 minutes. That is approximately one minute per question. You cannot afford to spend five minutes on one question. Here is a proven strategy.

### First Pass — Answer Everything You Know

On your first pass through the exam, answer every question you are confident about immediately. Mark uncertain questions for review. Never leave a question blank — there is no penalty for guessing on the CCNA exam.

### Eliminating Distractors

Most CCNA questions have one obviously wrong answer, one answer that sounds plausible but contains a factual error, one very close answer, and one correct answer. Train yourself to eliminate the obviously wrong answers first. Then use your elimination of the close-but-wrong answer to identify the correct one.

Common distractor patterns:

* Reversed protocol-to-transport mappings (RADIUS uses UDP, not TCP; TACACS+ uses TCP, not UDP)
* Reversed API directions (northbound vs. southbound)
* Correct concept applied to wrong protocol (e.g., OSPF described as distance-vector)
* Port numbers swapped (HTTP is 80, HTTPS is 443, RADIUS auth is 1812, not 1813)

### Scenario Questions

Scenario questions present a network diagram or configuration output and ask you to identify a problem or select the correct next step. For these:

1. Read the question first, then examine the diagram
2. Identify what is working and what is not
3. Match the symptoms to the technology domain
4. Eliminate answers that would affect unrelated technologies

### Drag-and-Drop and Simulation Items

Some CCNA exams include drag-and-drop topology labeling or simulated CLI configuration items. These cannot be skipped or returned to in some versions. For simulation items, type the most important commands first — `show` commands to verify state, configuration commands to fix the issue.

---

## Segment 5: Domain Quick-Reference Summary (17:00–21:00)

Let me give you the most important single fact from each major topic area — the fact most likely to appear on your exam.

For **subnetting**: A /27 mask gives you 32 addresses, 30 usable hosts. A /30 gives 4 addresses, 2 usable hosts. Memorize the CIDR table from /24 through /30.

For **VLANs**: The native VLAN on a trunk carries untagged frames. Changing the native VLAN to an unused VLAN (not VLAN 1) is a security best practice.

For **STP**: The root bridge has the lowest bridge ID. Bridge ID = Priority (default 32768) + VLAN ID + MAC. The port with the lowest cost to the root is the root port.

For **OSPF**: OSPF uses cost = 100 Mbps / interface bandwidth. A FastEthernet interface has cost 1; a T1 (1.544 Mbps) has cost 64. DR election uses highest priority then highest router ID.

For **HSRP**: The active router has the highest priority (default 100). Priority 0 causes immediate resignation. Preempt must be configured for a higher-priority router to take over.

For **NAT**: Inside local is the private IP of the inside host. Inside global is the public IP seen from the outside. These are the two most commonly confused NAT terms.

For **AAA**: RADIUS encrypts only the password; TACACS+ encrypts the entire packet. TACACS+ supports command authorization; RADIUS does not.

For **802.1X**: The authenticator is the switch. The supplicant is the end device. The authentication server is RADIUS.

For **REST APIs**: GET=Read, POST=Create, PUT=Update, DELETE=Delete. 200=OK, 201=Created, 401=Unauthorized, 404=Not Found.

For **Ansible**: Agentless. Push model. YAML playbooks. No software needed on managed devices.

---

## Segment 6: Capstone Lab and Course Closing (21:00–24:00)

Your Module 16 lab is a capstone challenge that brings together the major topics from across the course into a single multi-topology Packet Tracer environment. You will configure VLANs, inter-VLAN routing, OSPF, DHCP, NAT, port security, DHCP snooping, and basic AAA on a three-tier network that includes both a campus and a branch site.

This capstone lab simulates what you would encounter in a real network engineering role — not isolated feature configuration, but integrated system design where every decision affects multiple other components.

Take your time. Work systematically. Verify each section before moving to the next. The rubric awards partial credit for each correctly configured component.

To all of you — congratulations on completing CIS-3322 Advanced Networking. You have covered the full breadth of the CCNA 200-301 exam topics. You understand how packets move, how networks are secured, how wireless systems are architected, and how modern networks are automated. That knowledge is real, practical, and immediately applicable in the field.

Schedule your CCNA exam through Pearson VUE at certiport.pearsonvue.com. Study the official Cisco exam topics list at cisco.com/c/en/us/training-events. Supplement with Professor Messer's CCNA course and practice exams.

You are ready. Good luck.

---

Script End — Module 16 | Approximate runtime: 24 minutes
