# Reading Guide: Module 15 - CompTIA Network+ Acronym Mastery
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 15 – CompTIA Network+ Acronym Mastery**! The CompTIA Network+ N10-009 exam uses hundreds of acronyms throughout every domain, and exam questions frequently use acronym confusion as a distraction technique. A question about a wireless collision avoidance protocol may include CSMA/CD as a plausible-looking wrong answer — CSMA/CD is correct for wired Ethernet, not Wi-Fi. This module rapid-fires the most-tested acronyms across all five N10-009 domains so you can recognize them instantly under exam pressure without hesitation.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**: The media access control method used by wired Ethernet (IEEE 802.3). Devices listen before transmitting (carrier sense), transmit simultaneously if the medium is idle, detect collisions, and retransmit after a random back-off delay. Used on half-duplex Ethernet segments; modern full-duplex switched Ethernet eliminates collisions.
*   **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)**: The media access control method used by Wi-Fi (IEEE 802.11). Devices listen, then wait a random back-off interval before transmitting to avoid (not detect) collisions. Used because wireless collisions cannot be reliably detected. Distinguishing CSMA/CD from CSMA/CA is a common exam trap.
*   **OSPF (Open Shortest Path First)**: A link-state interior gateway routing protocol (IGP) that uses Dijkstra's algorithm to calculate the lowest-cost path. Administrative Distance = 110. Supports VLSM, classless routing, and multiple areas. Cost is calculated as 100 Mbps / interface bandwidth.
*   **BGP (Border Gateway Protocol)**: The exterior gateway protocol (EGP) that routes traffic between autonomous systems on the Internet. Uses path-vector routing. eBGP (External BGP) connects different ASes; iBGP (Internal BGP) connects routers within the same AS. Administrative Distance: eBGP = 20, iBGP = 200.
*   **VXLAN (Virtual Extensible LAN)**: An overlay encapsulation protocol that extends Layer 2 Ethernet segments across Layer 3 networks. Uses a 24-bit VNID (Virtual Network Identifier) supporting over 16 million virtual networks. Encapsulated in UDP on port 4789. Overcomes the 4,094 VLAN limit of 802.1Q.
*   **LACP (Link Aggregation Control Protocol)**: The IEEE 802.3ad protocol for dynamically negotiating EtherChannel bundles between switches or between a switch and a server. LACP modes: Active (initiates negotiation) and Passive (responds to negotiation). Two Passive ports will not form an EtherChannel.
*   **BPDU (Bridge Protocol Data Unit)**: Control frames transmitted by switches running STP/RSTP to elect the Root Bridge, determine port roles, and prevent Layer 2 loops. BPDU Guard shuts down a port that receives a BPDU on a PortFast-enabled access port, preventing rogue switches from being connected.
*   **ACL (Access Control List)**: A numbered or named set of permit/deny rules applied to a router or firewall interface to filter traffic based on source IP, destination IP, protocol, and port. Standard ACLs filter on source IP only; extended ACLs filter on source IP, destination IP, protocol, and port numbers.
*   **NAT (Network Address Translation)**: The process of translating private IP addresses to a public IP address (or pool) for outbound Internet communication. PAT (Port Address Translation), also called NAT Overload, maps multiple private hosts to a single public IP using unique source port numbers.
*   **IDS / IPS (Intrusion Detection System / Intrusion Prevention System)**: IDS passively monitors a copy of network traffic and alerts on detected threats — it does not block traffic. IPS sits inline in the traffic path and can actively block malicious traffic in real time. IDS generates alerts; IPS generates alerts and takes action.
*   **DMZ (Demilitarized Zone)**: A screened network segment between the Internet and the internal trusted network, typically created by placing public-facing servers (web, email, DNS) between two firewall interfaces. Internal hosts cannot be reached directly from the Internet; DMZ servers can be reached from both.
*   **SNMP (Simple Network Management Protocol)**: A protocol for monitoring and managing network devices. Uses UDP 161 (agent polling) and UDP 162 (traps). SNMPv1/v2c use plaintext community strings. SNMPv3 adds authentication (MD5/SHA) and encryption (AES/DES) — always choose SNMPv3 for secure management.
*   **QoS (Quality of Service)**: A set of techniques used to prioritize specific types of network traffic (VoIP, video) over lower-priority traffic (bulk file transfers). Mechanisms include traffic marking (DSCP/CoS), queuing (WFQ, CBWFQ), and traffic shaping/policing. MPLS networks use QoS labels to guarantee bandwidth for real-time traffic.
*   **STP / RSTP (Spanning Tree Protocol / Rapid Spanning Tree Protocol)**: IEEE 802.1D (STP) and 802.1w (RSTP) protocols that prevent Layer 2 loops in switched networks by blocking redundant ports. RSTP converges significantly faster than STP (seconds vs. up to 50 seconds). Root Bridge is elected by lowest Bridge ID (priority + MAC address).
*   **MTU (Maximum Transmission Unit)**: The largest IP packet size that can be transmitted on a network segment without fragmentation. Standard Ethernet MTU = 1500 bytes. Jumbo frames extend this to 9000 bytes for high-throughput storage/server networks. MTU mismatches cause intermittent large-packet failures.
*   **ARP (Address Resolution Protocol)**: The Layer 2/3 protocol that resolves an IPv4 address to a MAC address on the local segment. A host broadcasts an ARP Request; the host with the matching IP responds with an ARP Reply containing its MAC address. ARP cache poisoning exploits this unauthenticated process.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** Acronym recognition spans all five domains. The most acronym-dense domains are **Domain 1.0 – Networking Concepts (23%)** and **Domain 5.0 – Network Troubleshooting (23%)**. Acronym confusion is a primary distractor technique throughout the entire exam.
*   **CSMA/CD vs. CSMA/CA — the most common trap**: Any question about wireless (Wi-Fi, 802.11) media access = CSMA/CA. Any question about wired Ethernet collision handling = CSMA/CD. These two appear together as distractors on almost every exam. Never confuse them.
*   **IDS vs. IPS — active vs. passive**: IDS = passive, out-of-band, alerts only. IPS = inline, active, blocks traffic. A question describing a device that "detected but did not stop" an attack = IDS. A device that "blocked" traffic = IPS. The distinction is whether the device is in the traffic path.
*   **SNMP version for security**: Any scenario requiring encrypted or authenticated SNMP management = SNMPv3. SNMPv1 and v2c are never the right answer when security is a requirement. SNMPv3 in authPriv mode provides both authentication and privacy (encryption).
*   **Protocol port numbers you must know cold**: DNS = UDP/TCP 53; DHCP = UDP 67 (server), 68 (client); HTTP = TCP 80; HTTPS = TCP 443; FTP = TCP 20/21; SSH = TCP 22; Telnet = TCP 23; SMTP = TCP 25; SNMP = UDP 161/162; RDP = TCP 3389; NTP = UDP 123; BGP = TCP 179; LDAP = TCP/UDP 389; LDAPS = TCP 636.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) includes a dedicated acronym and port reference section. Professor Messer also provides a free [Network+ Study Group](https://www.professormesser.com/network-plus/n10-009/n10-009-study-groups/) with additional acronym drills.

---

### Required Readings & Videos
*   **Required Reading:** Review the **Acronym Reference** appendix and any protocol/port summary tables in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Revisit any chapters where you encounter unfamiliar acronyms.
*   **Required Video:** Watch Professor Messer's **Network+ Acronyms** and **Ports and Protocols** reference videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's activity, you will build a personal acronym reference card covering at minimum 50 CompTIA Network+ acronyms organized by domain, create a port-and-protocol reference table with all ports listed in the certification exam objectives, practice CSMA/CD vs. CSMA/CA, IDS vs. IPS, and SNMP version identification in scenario-based practice questions, and take at least one full-length practice exam to identify remaining acronym gaps.

---

### 3. Study Checklist
*   [ ] Know CSMA/CD (wired Ethernet) vs. CSMA/CA (Wi-Fi 802.11) — do not confuse them.
*   [ ] Know IDS (passive, out-of-band) vs. IPS (inline, active blocking).
*   [ ] Know SNMPv1/v2c (plaintext community strings) vs. SNMPv3 (auth + encryption).
*   [ ] Know OSPF (AD=110), BGP (eBGP=20, iBGP=200), RIP (AD=120), Static (AD=1).
*   [ ] Know VXLAN (24-bit VNID, UDP 4789) vs. 802.1Q (4,094 VLAN limit).
*   [ ] Know LACP Active/Passive modes and which combinations form an EtherChannel.
*   [ ] Memorize all required port numbers: DNS 53, DHCP 67/68, HTTP 80, HTTPS 443, SSH 22, Telnet 23, SMTP 25, SNMP 161/162, RDP 3389, NTP 123, BGP 179, LDAP 389, LDAPS 636.
*   [ ] Read the **Acronym Reference** sections in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's acronyms and ports/protocols videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
