# Video Script: Module 16 — Network+ N10-008 Exam Preparation (Part 2 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome back to Part 2 of Module 16. In Part 1 we reviewed Domains 1 and 2. Now we cover Domains 3, 4, and 5 — and conclude with the exam strategy guidance that will help you perform your best on test day.

---

## Section 1: Domain 3 Review — Network Operations (17%)

Domain 3 covers how networks are monitored, managed, and maintained in production.

### Network Monitoring Tools

Key monitoring tools and their purposes:

- **SNMP (Simple Network Management Protocol)**: Collects performance data and configuration information from managed devices. UDP ports 161 (queries) and 162 (traps). Versions: SNMPv1/v2c (insecure, community strings), SNMPv3 (authentication and encryption — always preferred).
- **Syslog**: Collects log messages from network devices. UDP port 514. Severity levels 0–7 (0=Emergency, 7=Debug).
- **NetFlow/IPFIX**: Collects traffic flow statistics — source/destination IP, port, protocol, byte count. Used for bandwidth analysis and security forensics.
- **NTP (Network Time Protocol)**: Synchronizes clocks across all network devices. UDP port 123. Consistent timestamps are critical for log correlation. Hierarchy: Stratum 0 (atomic clock) → Stratum 1 (primary time server) → Stratum 2 (secondary) and so on.
- **SNMP traps**: Unsolicited notifications from devices to the SNMP manager when a threshold is crossed or an event occurs.

### Network Documentation and Policies

From Module 15 — key exam points:

- Logical diagrams show IP addressing and routing; physical diagrams show ports and cables.
- Change management types: Standard (pre-approved), Normal (CAB review), Emergency (expedited).
- SLA metrics: Availability (99.99% = 52.6 minutes downtime/year), MTBF, MTTR, RTO, RPO.
- IPAM tracks IP address assignments; DDI integrates DNS, DHCP, and IPAM.

### High Availability Concepts

- **Redundancy**: Duplicate components eliminate single points of failure.
- **Load balancing**: Distributes traffic across multiple servers or links for both redundancy and performance.
- **NIC teaming**: Multiple physical NICs aggregated into one logical interface — bandwidth and redundancy.
- **Clustering**: Multiple servers providing the same service; if one fails, others continue.
- **Cold/Warm/Hot standby**: Cold = no readiness, Warm = some readiness, Hot = instant failover.

---

## Section 2: Domain 4 Review — Network Security (20%)

Domain 4 is the second-largest domain. Security topics are woven throughout the exam.

### Common Network Attacks

Know these attack types:

- **DoS (Denial of Service)**: Overwhelms a target to prevent legitimate use. A DDoS uses multiple sources.
- **Man-in-the-Middle (MitM)**: Attacker intercepts communication between two parties. ARP poisoning and rogue Wi-Fi AP are classic MitM setups.
- **ARP Poisoning**: Attacker sends fraudulent ARP replies, associating their MAC address with a legitimate IP, redirecting traffic through the attacker.
- **DNS Poisoning**: Corrupts DNS cache with fraudulent records, redirecting users to attacker-controlled servers.
- **VLAN Hopping**: Attacker gains access to VLANs they should not reach via DTP trunk negotiation or double-tagging.
- **Spoofing**: Forging the source IP, MAC, or other identity field in packets.
- **Replay attack**: Attacker captures and retransmits a previously valid packet.
- **Deauthentication attack**: Wi-Fi attack sending forged deauth frames to disconnect clients. Used to capture the WPA2 handshake for offline cracking.

### Firewalls

- **Packet filter**: Stateless rules based on IP address, port, and protocol. Layer 3/4.
- **Stateful inspection firewall**: Tracks connection state — allows return traffic automatically. Layer 4.
- **Application-aware (NGFW)**: Deep packet inspection at Layer 7 — identifies applications regardless of port. Intrusion prevention, URL filtering, malware inspection.
- **WAF (Web Application Firewall)**: Protects web applications from SQL injection, XSS, and other HTTP-layer attacks.

Network zones: Internet → DMZ → Internal. The DMZ hosts public-facing servers (web, email, DNS). Internal network is not directly reachable from the internet.

### VPNs

- **IPsec**: Suite of protocols for Layer 3 VPN. Two modes: Transport (encrypts payload only) and Tunnel (encrypts entire original packet). Uses AH (authentication) and ESP (encryption).
- **SSL/TLS VPN**: Uses SSL/TLS for encryption. Clientless (web browser) or full-tunnel (client application). HTTPS port 443 — typically traverses firewalls without issues.
- **Split tunneling**: VPN configuration where only corporate-destined traffic goes through the VPN; internet traffic goes directly. Security risk — local network could be a pivot point.

### Authentication Protocols

- **RADIUS**: UDP ports 1812/1813 (or legacy 1645/1646). Centralized authentication for network access (Wi-Fi, VPN, switch/router login). Encrypts only the password in the access-request.
- **TACACS+**: TCP port 49. Cisco proprietary (though open implementations exist). Encrypts entire payload. Separates authentication, authorization, and accounting — preferred for device administration.
- **802.1X**: Port-based Network Access Control. Uses EAP (Extensible Authentication Protocol) with a RADIUS backend. Three components: Supplicant (client), Authenticator (switch/AP), Authentication Server (RADIUS).
- **LDAP/AD**: Directory services for user authentication. LDAP port 389; LDAPS port 636.

### Wireless Security

- **WEP**: Broken. Never use.
- **WPA/TKIP**: Flawed. Do not use for new deployments.
- **WPA2/AES-CCMP**: Current minimum standard. Personal (PSK) and Enterprise (802.1X).
- **WPA3/SAE**: Simultaneous Authentication of Equals — resistant to offline dictionary attacks. Required for Wi-Fi 6 certification.

---

## Section 3: Domain 5 Review — Network Troubleshooting (22%)

Domain 5 is the largest domain by weight. Troubleshooting questions test applied knowledge.

### The CompTIA Seven-Step Model

The seven steps in order:

1. Identify the problem
2. Establish a theory of probable cause
3. Test the theory
4. Establish a plan of action
5. Implement the solution or escalate
6. Verify full system functionality
7. Document findings, actions, and outcomes

Never skip Step 7. The exam tests whether you know the order and purpose of every step.

### Wired Troubleshooting

Common cable faults tested: open circuit, short circuit, crosstalk, split pair, reversed pair, attenuation.

Tools: Basic cable tester (continuity), cable certifier (performance + TDR), tone generator/probe (cable tracing), optical power meter (fiber attenuation), VFL (visual fault locator for fiber).

Key symptom patterns:

- No link = physical layer failure
- Slow speed + late collisions = duplex mismatch
- 169.254.x.x APIPA = DHCP failure
- Can ping by IP, not by name = DNS failure
- All works except one application = firewall/port blocking

### Wireless Troubleshooting

- **Poor signal**: Physical distance, obstacles, antenna orientation. Use a wireless site survey tool to identify coverage gaps.
- **Interference**: Other APs on the same channel, microwave ovens, cordless phones (2.4 GHz). Use Wi-Fi analyzer to identify channel congestion. Move to 5 GHz non-overlapping channels.
- **Authentication failures**: Wrong PSK, expired certificates (802.1X), RADIUS server unreachable.
- **Captive portal issues**: DNS must resolve and HTTP must be accessible before TLS redirect.

### Diagnostic Command Reference

| Symptom | Best Command | What to Look For |
|---|---|---|
| Wrong IP | `ipconfig /all` | 169.254.x.x, wrong subnet, wrong gateway |
| Unreachable host | `ping` | TTL exceeded, Destination Unreachable, Request Timeout |
| Routing issue | `traceroute / tracert` | Where the path dies or shows high latency |
| DNS failure | `nslookup / dig` | No answer, SERVFAIL, wrong server responding |
| Port blocked | `netstat -an` | Expected port not in LISTENING state |
| ARP issue | `arp -a` | Missing or incomplete ARP entry |
| Bandwidth problem | `iperf / speedtest` | Actual vs. expected throughput |

---

## Section 4: Exam Strategy

### Time Management

You have 90 minutes for up to 90 questions — approximately 1 minute per question.

- Performance-based questions (PBQs) appear first and take longer. Many candidates flag them and skip to multiple-choice questions first, then return.
- Multiple-choice questions: read all four options before choosing. Eliminate clearly wrong answers first.
- If unsure, eliminate two options and make your best guess — there is no penalty for wrong answers.

### Scenario Question Approach

The majority of difficult questions on Network+ are scenario-based. The scenario describes a situation, and you must select the best answer.

Steps for scenario questions:

1. Read the question stem first — know what is being asked before reading the scenario.
2. Read the scenario — identify the symptoms, what works, what does not work, and any recent changes.
3. Apply the OSI model — identify the most likely layer of failure given the symptoms.
4. Eliminate impossible answers — if ping by IP works, eliminate physical and routing answers.
5. Choose the best answer — the most specific, correct, and actionable option.

### Memorization Priority

If you have limited study time, prioritize these high-frequency topics:

- Port numbers — the full table from this module
- Subnetting — /24 through /30 host counts by memory
- OSI layer to protocol mapping
- STP port states and convergence times
- VPN types — IPsec modes, SSL VPN, split tunneling
- Wireless standards — 802.11a/b/g/n/ac/ax speeds and bands
- SNMP — ports 161/162, SNMPv3 for security
- CompTIA seven-step troubleshooting model — order and purpose

### What the Exam Does Not Test

Network+ is an entry-level certification. Do not over-study:

- Deep BGP configuration
- MPLS label distribution protocol specifics
- Advanced cryptography mathematics
- Vendor-specific CLI syntax (Cisco commands appear but only at a general level)

### Final Week Preparation

- Take at least two full-length practice exams under timed conditions.
- Review every wrong answer — understand why the correct answer is correct.
- Focus on your weakest domain — not your strongest.
- Get a full night of sleep before the exam. Sleep deprivation impairs test performance more than most people realize.
- Arrive early at the testing center. Bring two forms of ID.

---

## Section 5: Congratulations

You have completed all sixteen modules of CIS-3321 Network Administration. You have covered:

- Physical networking, cabling standards, and the OSI model
- Ethernet switching, VLANs, and Spanning Tree
- IP addressing — IPv4, subnetting, and IPv6
- Routing protocols — static, OSPF, EIGRP, BGP concepts
- Wireless networking — standards, security, and design
- Network security — firewalls, VPNs, authentication, attacks
- Cloud computing, virtualization, and SDN
- Wide area networks — MPLS, SD-WAN, cellular, satellite
- Unified communications and QoS
- Network troubleshooting methodology
- Network documentation and policies

You are prepared for both the CompTIA Network+ N10-008 exam and for entry-level network administration work.

Complete the Reading Guide review, the 20-question practice exam in the Quiz, the Lab self-assessment, and the Discussion to finalize your exam preparation.

Good luck. You have earned it.
