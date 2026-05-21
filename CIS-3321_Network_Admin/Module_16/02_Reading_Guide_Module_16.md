# Reading Guide: Module 16 - Final Exam Preparation
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 16 – Final Exam Preparation**! This is the final module of CIS-3321 Network Administration. The CompTIA Network+ N10-009 exam tests five domains across 90 questions (maximum) in 90 minutes, including multiple-choice and performance-based questions (PBQs). This module consolidates everything covered in the course — from OSI/TCP-IP models and IP addressing through routing, switching, virtualization, security, and troubleshooting — and provides a structured review strategy to ensure you are fully prepared for both the course final exam and the CompTIA certification exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **CompTIA Network+ N10-009 Exam Domains**: Five domains tested: Domain 1.0 Networking Concepts (23%), Domain 2.0 Network Implementations (20%), Domain 3.0 Network Operations (19%), Domain 4.0 Network Security (19%), Domain 5.0 Network Troubleshooting (23%). Domains 1 and 5 together account for 46% of the exam.
*   **Performance-Based Questions (PBQs)**: Interactive exam questions that require you to perform a task — such as configuring a firewall ACL, wiring a patch panel using T568B, reading a routing table, or placing network devices in a topology diagram. PBQs appear early in the exam and require applied knowledge, not just definition recall.
*   **OSI Model (7 Layers)**: Physical (1), Data Link (2), Network (3), Transport (4), Session (5), Presentation (6), Application (7). Mnemonic: "Please Do Not Throw Sausage Pizza Away." Troubleshooting follows the OSI model bottom-up (start at Physical) or top-down (start at Application) depending on the scenario.
*   **TCP vs. UDP**: TCP (Transmission Control Protocol) is connection-oriented, provides guaranteed delivery via three-way handshake (SYN/SYN-ACK/ACK), sequencing, and error correction. UDP (User Datagram Protocol) is connectionless, no guaranteed delivery, lower overhead — used for real-time applications (VoIP, DNS queries, streaming) where speed matters more than reliability.
*   **Subnetting**: The process of dividing an IP address space into smaller logical networks using a subnet mask. CIDR notation (e.g., /24) specifies the number of network bits. Key values: /24 = 256 addresses (254 usable), /25 = 128 (126 usable), /26 = 64 (62 usable), /27 = 32 (30 usable), /28 = 16 (14 usable), /30 = 4 (2 usable — point-to-point links).
*   **IPv4 vs. IPv6**: IPv4 uses 32-bit addresses (4.3 billion total); IPv6 uses 128-bit addresses. IPv6 eliminates NAT by providing globally routable addresses. IPv6 link-local addresses begin with FE80::/10. IPv6 uses NDP (Neighbor Discovery Protocol) instead of ARP. Dual-stack allows both IPv4 and IPv6 to run simultaneously.
*   **Default Gateway**: The router interface address that a host sends traffic to when the destination is not on the local subnet. A missing or incorrect default gateway allows local communication but prevents access to remote networks. Verified with `ipconfig /all` (Windows) or `ip route` (Linux).
*   **DHCP DORA**: The four-step DHCP lease process: Discover (client broadcasts for DHCP server) → Offer (server offers IP lease) → Request (client requests the offered IP) → Acknowledge (server confirms the lease). A DHCP relay agent (IP helper address) forwards DHCP broadcasts across routed network boundaries.
*   **DNS Record Types**: A (IPv4 address), AAAA (IPv6 address), CNAME (alias to another hostname), MX (mail exchanger, with priority value), PTR (reverse DNS, IP to hostname), SOA (Start of Authority — zone metadata), TXT (text records, used for SPF/DKIM email authentication). DNS uses UDP port 53 (standard queries) and TCP port 53 (zone transfers and large responses).
*   **Firewall Types**: Stateless firewall filters individual packets by IP/port using ACLs with no session awareness. Stateful firewall tracks the state of TCP/UDP sessions and allows return traffic automatically. Application-layer (proxy) firewall inspects Layer 7 content. Next-Generation Firewall (NGFW) combines stateful inspection with application identification, IPS, and SSL inspection.
*   **VPN Types**: IPsec Tunnel mode encapsulates the entire original IP packet — used for site-to-site VPNs. IPsec Transport mode encrypts only the payload — used for host-to-host. SSL/TLS VPN uses TCP port 443 and passes through most firewalls — used for remote access (clientless browser-based or client-based). GRE tunnels carry multicast/broadcast but have no encryption.
*   **Wireless Standards**: 802.11a (5 GHz, 54 Mbps), 802.11b (2.4 GHz, 11 Mbps), 802.11g (2.4 GHz, 54 Mbps), 802.11n/Wi-Fi 4 (2.4/5 GHz, up to 600 Mbps, MIMO), 802.11ac/Wi-Fi 5 (5 GHz, multi-user MIMO), 802.11ax/Wi-Fi 6 (2.4/5/6 GHz, OFDMA, highest density performance). Non-overlapping 2.4 GHz channels: 1, 6, 11.
*   **CompTIA Troubleshooting Methodology**: Seven steps in order: (1) Identify the problem, (2) Establish a theory of probable cause, (3) Test the theory, (4) Establish an action plan, (5) Implement the solution, (6) Verify full functionality, (7) Document findings. The exam tests step order — especially distinguishing Step 3 (test theory) from Step 5 (implement solution).
*   **High Availability Concepts**: MTTR (Mean Time to Repair) — average time to restore a failed component. MTBF (Mean Time Between Failures) — average operational time between failures. RTO (Recovery Time Objective) — maximum acceptable downtime after a disaster. RPO (Recovery Point Objective) — maximum acceptable data loss measured in time. Lower RTO/RPO = higher cost infrastructure.
*   **Common Port Numbers (Final Review)**: FTP=20/21, SSH=22, Telnet=23, SMTP=25, DNS=53, DHCP=67/68, HTTP=80, POP3=110, NTP=123, IMAP=143, SNMP=161/162, LDAP=389, HTTPS=443, SMB=445, RDP=3389, BGP=179, LDAPS=636, RADIUS=1812/1813, TACACS+=49.

---

### 2. Certification Exam Tips
*   **Domain weighting — prioritize your study time**: Domains 1 (Networking Concepts, 23%) and 5 (Network Troubleshooting, 23%) together make up nearly half the exam. If you are short on review time, focus on these two domains. Domain 3 (Network Operations, 19%) and Domain 4 (Network Security, 19%) are equal weight and critically important for the modern exam.
*   **Performance-Based Questions appear first**: PBQs are typically presented at the beginning of the exam. They take more time than standard multiple-choice questions. If you are stuck on a PBQ, flag it, skip to the multiple-choice questions, and return at the end. Do not let one PBQ consume all your available time.
*   **Subnetting is non-negotiable**: You will see subnetting questions on every Network+ exam. Practice quickly identifying the network address, broadcast address, first usable host, and last usable host for common prefix lengths (/24 through /30). The exam does not allow calculators — you must be able to subnet mentally.
*   **OSI layer identification in troubleshooting scenarios**: The exam describes a symptom and asks which OSI layer is affected. Physical layer = cable, NIC, port light. Data Link = MAC address, switch, VLAN, STP. Network = IP address, routing, subnet mask. Transport = TCP/UDP, ports, sessions. Know where each protocol and problem lives.
*   **Know your "always" answers**: SNMPv3 is always the answer when security is required. Type 1 hypervisor is always the answer for enterprise production VMs. OSPF always wins over RIP (lower AD=110 vs 120). T568B is the most common commercial wiring standard. Auto-MDIX makes crossover cables obsolete on modern switches.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) provides full coverage of all five exam domains, including a comprehensive exam review. CompTIA also provides an [official exam objectives document](https://www.comptia.org/certifications/network) that lists every testable topic — reviewing this document against your notes is one of the most effective final-review strategies.

---

### Required Readings & Videos
*   **Required Reading:** Review all module reading guides from Modules 01–15 in this course. Pay particular attention to the High-Yield Glossary terms and Study Checklists from each module. Consult the OER Textbook [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/) for any topics where you need deeper review.
*   **Required Video:** Watch Professor Messer's **Network+ Exam Review** videos and any domain sections where you identified gaps, available in the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/). Completing at least one full Professor Messer practice exam before the course final is strongly recommended.

---

### Lab & Command Integration
In this week's final review activity, you will complete a timed full-length practice exam covering all five N10-009 domains, review every missed question to identify the correct concept and why the distractor was wrong, perform a final subnetting drill calculating network/broadcast/host ranges for at least 10 CIDR prefixes from /24 to /30, and review the complete port number reference table until all required ports can be recalled from memory without reference materials.

---

### 3. Study Checklist
*   [ ] Know all five N10-009 exam domain names and their percentage weights.
*   [ ] Know the OSI 7-layer model and which protocols/problems belong at each layer.
*   [ ] Know TCP vs. UDP — connection-oriented vs. connectionless, use cases for each.
*   [ ] Know subnetting for /24 through /30 prefixes — network, broadcast, first/last host.
*   [ ] Know the DHCP DORA process and the role of the DHCP relay agent (IP helper).
*   [ ] Know all DNS record types: A, AAAA, CNAME, MX, PTR, SOA, TXT.
*   [ ] Know the CompTIA 7-step troubleshooting methodology in order.
*   [ ] Know all required port numbers from memory (see glossary above).
*   [ ] Know IPsec Tunnel vs. Transport mode and SSL/TLS VPN use cases.
*   [ ] Know wireless standards: 802.11a/b/g/n/ac/ax frequencies and key features.
*   [ ] Know MTTR, MTBF, RTO, RPO — definitions and which direction means higher availability.
*   [ ] Review all module reading guides from Modules 01–15 for remaining glossary gaps.
*   [ ] Complete a full-length practice exam from [Professor Messer's N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Review the official [CompTIA Network+ N10-009 Exam Objectives](https://www.comptia.org/certifications/network) document.
*   [ ] Proceed to the course final exam.
