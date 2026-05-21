# Reading Guide: Module 08 - Network Security – Firewalls, IDS/IPS, and VPNs
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 08 – Network Security: Firewalls, IDS/IPS, and VPNs**! Network security is one of the most heavily tested areas of the CompTIA Network+ N10-009 exam. You must understand how firewalls filter traffic at different OSI layers, the critical difference between intrusion detection and intrusion prevention systems, how VPNs secure communications, and common network attacks. This module builds directly on the VPN concepts from Module 07 and adds the defensive infrastructure that surrounds enterprise networks.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Firewall**: A network security device or software that monitors and controls inbound and outbound traffic based on a defined ruleset. Firewalls operate at different OSI layers depending on their type — packet filter (Layer 3/4), stateful (Layer 4), or application (Layer 7).
*   **Packet-Filtering Firewall (Stateless)**: The simplest firewall type. Examines each packet independently based on source/destination IP address, port numbers, and protocol. Has no memory of previous packets — does not track connection state. Operates at Layer 3/4.
*   **Stateful Firewall**: Tracks the state of active connections (SYN, SYN-ACK, established, closed) in a state table. Can distinguish legitimate return traffic from unsolicited inbound packets. More secure than stateless filtering. Operates at Layer 4.
*   **Application-Layer Firewall (NGFW/WAF)**: Inspects traffic up to Layer 7, including application payload content. A Next-Generation Firewall (NGFW) adds deep packet inspection, IPS, and application identification. A Web Application Firewall (WAF) specifically protects HTTP/HTTPS applications.
*   **ACL (Access Control List)**: An ordered list of permit/deny rules applied to a router or switch interface to filter traffic by source/destination IP, port, or protocol. Standard ACLs filter by source IP only; extended ACLs filter by source, destination, port, and protocol.
*   **IDS (Intrusion Detection System)**: A passive security system that monitors network traffic or host activity for signatures of known attacks and anomalies, then generates alerts. An IDS does NOT block traffic — it only detects and reports. Can be network-based (NIDS) or host-based (HIDS).
*   **IPS (Intrusion Prevention System)**: An active, inline security system that monitors traffic for attack signatures and anomalies and can automatically block, drop, or quarantine malicious traffic in real time. Unlike IDS, IPS sits inline in the traffic path and takes preventive action.
*   **Signature-Based Detection**: IDS/IPS detection method that matches traffic patterns against a database of known attack signatures. Effective against known threats but cannot detect zero-day attacks not in the signature database.
*   **Anomaly-Based Detection**: IDS/IPS detection method that compares current traffic behavior against a baseline of normal activity. Can detect novel/zero-day attacks but generates more false positives than signature-based detection.
*   **DMZ (Demilitarized Zone)**: A network segment positioned between the public internet and the internal private network, separated by two firewalls. Hosts publicly accessible servers (web, email, DNS) while protecting the internal network. Traffic from the internet reaches the DMZ but not the internal LAN directly.
*   **NAT (Network Address Translation)**: Translates private RFC 1918 IP addresses to a public routable IP address for internet communication. PAT (Port Address Translation) — also called NAT Overload — maps multiple internal hosts to a single public IP using unique port numbers.
*   **DoS/DDoS (Denial of Service / Distributed Denial of Service)**: An attack that overwhelms a target system or network with traffic or requests, rendering it unavailable. DoS comes from a single source; DDoS uses a botnet of many compromised systems to amplify the attack.
*   **Man-in-the-Middle (MitM) Attack**: An attack where the attacker secretly intercepts and potentially modifies communications between two parties who believe they are communicating directly. Requires the attacker to intercept traffic, often via ARP poisoning or rogue access points.
*   **ARP Poisoning (ARP Spoofing)**: An attack where the attacker sends forged ARP replies to associate their MAC address with a legitimate IP address, redirecting traffic through the attacker's device. Enables MitM attacks on local network segments.
*   **VLAN Hopping**: An attack technique that exploits switch trunking or double-tagging to send traffic to a VLAN the attacker should not have access to. Mitigated by disabling DTP, using dedicated native VLANs, and ensuring proper trunk port configuration.
*   **Zero-Day Vulnerability**: A software vulnerability that is unknown to the vendor and has no available patch. Exploits targeting zero-day vulnerabilities cannot be detected by signature-based systems until a signature is developed.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** Network security falls under **Domain 4.0 – Network Security (19%)**. Firewall types, IDS vs IPS, and attack recognition are the most-tested security topics on N10-009.
*   **IDS vs IPS — the most-tested security distinction**: IDS = passive, monitors and alerts only, out-of-band. IPS = active, inline, blocks traffic. Any question asking which system "prevents" or "drops" attacks = IPS. Any question asking which system "detects" or "alerts" only = IDS.
*   **Stateless vs stateful firewall trap**: A stateless (packet-filter) firewall cannot distinguish a legitimate TCP reply from an unsolicited inbound packet — it must have an explicit permit rule for return traffic. A stateful firewall automatically allows return traffic for established connections.
*   **DMZ architecture**: The DMZ is always a third network segment with its own interface on the firewall — not just a VLAN. Public servers go in the DMZ; internal servers stay in the LAN. The exam may describe a scenario and ask where a web server should be placed.
*   **ARP poisoning mitigation**: Dynamic ARP Inspection (DAI) on managed switches validates ARP packets against the DHCP snooping binding table — stops ARP poisoning at the switch level. The exam tests DAI as the correct Layer 2 mitigation.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers firewalls, IDS/IPS, common attacks, and network hardening in the Network Security domain section.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **Network Security, Firewalls, and Attack Types** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the firewall type comparison, DMZ architecture diagrams, and the IDS/IPS operational differences.
*   **Required Video:** Watch Professor Messer's **Firewalls**, **IDS and IPS**, and **Common Network Attacks** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will configure ACL rules on a Cisco router in Packet Tracer — both standard and extended ACLs — verify their operation using `show access-lists`, and simulate a DMZ architecture with a three-interface firewall separating the internet, DMZ web server, and internal LAN.

---

### 3. Study Checklist
*   [ ] Know the three firewall types: stateless (packet filter), stateful, and application-layer/NGFW.
*   [ ] Understand the critical difference between IDS (passive, alerts only) and IPS (active, blocks traffic).
*   [ ] Know signature-based vs anomaly-based detection and when each is appropriate.
*   [ ] Understand DMZ architecture — where to place public-facing servers and why.
*   [ ] Know common attacks: DoS/DDoS, MitM, ARP poisoning, VLAN hopping, zero-day.
*   [ ] Know NAT/PAT — how private addresses are translated to public addresses.
*   [ ] Read the **Network Security** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's security videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
