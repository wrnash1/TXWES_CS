# Reading Guide: Module 16 — Network+ N10-008 Exam Preparation

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Purpose

This reading guide consolidates key facts, tables, and reference material across all five N10-008 exam domains. Use it as your primary study reference during the final week before your exam. Highlight anything you cannot immediately recall and return to those items daily.

---

## Domain 1: Networking Concepts (23%)

### OSI Model — Layer to Protocol Mapping

| Layer | Name | Protocols and Technologies |
|---|---|---|
| 7 | Application | HTTP, HTTPS, FTP, SFTP, SSH, DNS, DHCP, SMTP, SNMP, NTP, SIP, H.323, RDP |
| 6 | Presentation | SSL/TLS, JPEG, MPEG, ASCII — data formatting and encryption negotiation |
| 5 | Session | NetBIOS, RPC — session establishment and teardown |
| 4 | Transport | TCP (connection-oriented), UDP (connectionless) |
| 3 | Network | IP (v4 and v6), ICMP, OSPF, EIGRP, BGP |
| 2 | Data Link | Ethernet (802.3), Wi-Fi (802.11), ARP, STP, 802.1Q VLANs |
| 1 | Physical | Ethernet physical, fiber, coaxial, DSL — the medium itself |

### TCP vs. UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed delivery, acknowledgments | No guarantee |
| Ordering | Ordered delivery | No ordering |
| Speed | Slower — overhead for reliability | Faster — no overhead |
| Use cases | HTTP, FTP, SSH, SMTP, DNS (large) | DNS (small), DHCP, VoIP, streaming |

### IPv4 Subnetting Reference

| CIDR | Subnet Mask | Usable Hosts | Notes |
|---|---|---|---|
| /24 | 255.255.255.0 | 254 | Standard LAN subnet |
| /25 | 255.255.255.128 | 126 | Splits /24 into 2 |
| /26 | 255.255.255.192 | 62 | Splits /24 into 4 |
| /27 | 255.255.255.224 | 30 | Splits /24 into 8 |
| /28 | 255.255.255.240 | 14 | Small department subnet |
| /29 | 255.255.255.248 | 6 | Very small subnet |
| /30 | 255.255.255.252 | 2 | Point-to-point links |

Formula: usable hosts = 2^(32 - prefix) - 2

### Special IPv4 Addresses

| Range | Purpose |
|---|---|
| 10.0.0.0/8 | RFC 1918 private |
| 172.16.0.0/12 | RFC 1918 private |
| 192.168.0.0/16 | RFC 1918 private |
| 169.254.0.0/16 | APIPA — DHCP failure |
| 127.0.0.0/8 | Loopback (127.0.0.1 standard) |

### IPv6 Address Types

| Type | Prefix | Description |
|---|---|---|
| Global unicast | 2000::/3 | Publicly routable — equivalent to public IPv4 |
| Link-local | fe80::/10 | Non-routable — auto-assigned on each interface |
| Loopback | ::1/128 | Equivalent to 127.0.0.1 |
| Unspecified | ::/128 | Source address during DAD |
| Multicast | ff00::/8 | Replaces broadcast in IPv6 |

### Well-Known Port Numbers

| Port | Protocol | Service |
|---|---|---|
| 20 | TCP | FTP Data |
| 21 | TCP | FTP Control |
| 22 | TCP | SSH, SFTP, SCP |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP (server/client) |
| 69 | UDP | TFTP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 119 | TCP | NNTP |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 161/162 | UDP | SNMP (queries/traps) |
| 389 | TCP/UDP | LDAP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 465/587 | TCP | SMTPS / SMTP Submission |
| 514 | UDP | Syslog |
| 636 | TCP | LDAPS |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 1433 | TCP | MS SQL Server |
| 1521 | TCP | Oracle Database |
| 3306 | TCP | MySQL |
| 3389 | TCP | RDP |
| 5060 | TCP/UDP | SIP |
| 5061 | TCP | SIP over TLS |

### Routing Protocols and Administrative Distance

| Route Source | Administrative Distance |
|---|---|
| Connected interface | 0 |
| Static route | 1 |
| EIGRP (internal) | 90 |
| OSPF | 110 |
| RIP | 120 |
| EIGRP (external) | 170 |

Lower administrative distance = more trusted. When two routes to the same destination exist, the lower-AD route wins.

### Routing Protocol Classifications

- Static: manually configured, no overhead, no automatic failover
- Dynamic IGP (within AS): RIP (distance vector), OSPF (link state), EIGRP (hybrid)
- Dynamic EGP (between AS): BGP — the internet routing protocol
- Distance vector: routing by rumor — each router only knows what neighbors report
- Link state: each router builds a complete topology map via LSA flooding

---

## Domain 2: Infrastructure (18%)

### Switching Concepts

| Concept | Key Points |
|---|---|
| MAC address table (CAM) | Maps MAC address to port. Entries age out at 300 seconds (Cisco default). |
| Unicast forwarding | Frame sent only to the port where destination MAC was learned. |
| Flooding | Used when destination MAC is unknown or destination is broadcast (FF:FF:FF:FF:FF:FF). |
| VLAN | Logical Layer 2 segmentation. Each VLAN is a separate broadcast domain. |
| 802.1Q trunk | Carries multiple VLANs on one link. Tags frames with 4-byte header containing 12-bit VLAN ID. |
| Native VLAN | Untagged VLAN on a trunk. Default is VLAN 1. Best practice: change to unused VLAN ID. |
| STP (802.1D) | Prevents Layer 2 loops by blocking redundant paths. Convergence time: up to 50 seconds. |
| RSTP (802.1w) | Rapid STP — sub-second convergence via direct negotiation. Replaces 802.1D. |
| PortFast | Bypasses STP listening/learning on access ports. For end devices only. |
| BPDU Guard | Err-disables a PortFast port if a BPDU is received. Protects against rogue switches. |
| EtherChannel | Bundles 2–8 physical links into one logical link. STP sees one link. LACP (802.3ad) or PAgP. |

### STP Port States (802.1D)

| State | Forwards Frames | Learns MACs | Duration |
|---|---|---|---|
| Blocking | No | No | Up to 20 seconds (Max Age) |
| Listening | No | No | 15 seconds (Forward Delay) |
| Learning | No | Yes | 15 seconds (Forward Delay) |
| Forwarding | Yes | Yes | Indefinite |

### Wireless Standards

| Standard | Band | Max Speed | Notes |
|---|---|---|---|
| 802.11a | 5 GHz | 54 Mbps | Legacy; less 2.4 GHz interference |
| 802.11b | 2.4 GHz | 11 Mbps | Legacy; widely adopted |
| 802.11g | 2.4 GHz | 54 Mbps | Backward compatible with b |
| 802.11n | 2.4/5 GHz | 600 Mbps | MIMO; dual-band |
| 802.11ac | 5 GHz | 3.5 Gbps | MU-MIMO; beamforming; Wave 2 |
| 802.11ax | 2.4/5/6 GHz | 9.6 Gbps | Wi-Fi 6; OFDMA; high-density environments |

Non-overlapping 2.4 GHz channels (North America): 1, 6, 11. 5 GHz has many more non-overlapping channels.

### WAN Technologies

| Technology | Speed | Key Characteristics |
|---|---|---|
| T1 | 1.544 Mbps | Legacy leased line; 24 DS0 channels |
| T3 | 44.736 Mbps | Legacy leased line; 28 T1s |
| MPLS | Varies | Label-switched; any-to-any VPN; traffic engineering; carrier-managed |
| SD-WAN | Varies | App-aware routing; multiple transports; ZTP; policy-based path selection |
| Metro E-Line | Varies | Point-to-point Ethernet service |
| Metro E-LAN | Varies | Multipoint-to-multipoint Ethernet service |
| DSL (ADSL) | Asymmetric | Copper local loop; higher download than upload |
| Cable (DOCSIS) | Up to 10 Gbps | Shared coaxial medium; DOCSIS 3.1 |
| GEO Satellite | Varies | 35,000 km altitude; 600+ ms latency; not for real-time |
| LEO Satellite | Varies | ~550 km altitude; 20–40 ms latency; viable for remote sites |

---

## Domain 3: Network Operations (17%)

### Network Monitoring Protocols

| Protocol | Port | Purpose | Key Details |
|---|---|---|---|
| SNMP | UDP 161/162 | Device monitoring and management | 161 = queries; 162 = traps. SNMPv3 adds authentication and encryption. |
| Syslog | UDP 514 | Log collection from network devices | Severity levels 0–7 (0=Emergency, 7=Debug) |
| NetFlow/IPFIX | Varies | Traffic flow statistics | Source/dest IP, port, protocol, byte count. Used for bandwidth analysis. |
| NTP | UDP 123 | Clock synchronization | Stratum 0 = atomic clock; Stratum 1 = primary server; Stratum 2 = secondary. |

### Syslog Severity Levels

| Level | Name | Meaning |
|---|---|---|
| 0 | Emergency | System unusable |
| 1 | Alert | Immediate action required |
| 2 | Critical | Critical condition |
| 3 | Error | Error condition |
| 4 | Warning | Warning condition |
| 5 | Notice | Normal but significant |
| 6 | Informational | Informational messages |
| 7 | Debug | Debug-level messages |

### Documentation Types

| Document | Contents |
|---|---|
| Logical diagram | IP addressing, subnets, VLANs, routing, Layer 3 topology |
| Physical diagram | Device locations, port connections, cable paths, rack layouts |
| IPAM | IP address assignments, subnet allocations, DHCP ranges, DNS mappings |
| Change request | Description, risk assessment, rollback plan, maintenance window, approvals |
| Baseline | Normal performance metrics used to identify deviations |

### Change Management Types

| Type | Description | Approval |
|---|---|---|
| Standard | Pre-approved, routine, low-risk | Pre-approved — no CAB review needed |
| Normal | Non-urgent change to production | CAB review required |
| Emergency | Critical fix for outage or security incident | Expedited approval; documented after |

### SLA Metrics

| Metric | Definition |
|---|---|
| Availability | Percentage of time a service is operational. 99.9% = 8.7 hours downtime/year. |
| MTBF | Mean Time Between Failures — average operating time between failures. |
| MTTR | Mean Time To Repair — average time to restore after a failure. |
| RTO | Recovery Time Objective — maximum acceptable time to restore after a disaster. |
| RPO | Recovery Point Objective — maximum acceptable data loss measured in time. |

### Availability Reference

| Availability | Annual Downtime |
|---|---|
| 99% | 87.6 hours |
| 99.9% | 8.76 hours |
| 99.99% (four nines) | 52.6 minutes |
| 99.999% (five nines) | 5.26 minutes |

### High Availability Concepts

- Redundancy: duplicate components eliminate single points of failure
- Load balancing: distributes traffic across multiple servers or links
- NIC teaming: multiple physical NICs aggregated into one logical interface
- Clustering: multiple servers providing the same service with failover
- Hot standby: instant failover, no data loss; Warm standby: some delay; Cold standby: manual restore

---

## Domain 4: Network Security (20%)

### Common Network Attacks

| Attack | Description |
|---|---|
| DoS/DDoS | Overwhelms a target to prevent legitimate use. DDoS uses multiple sources. |
| Man-in-the-Middle | Attacker intercepts communication between two parties. |
| ARP Poisoning | Fraudulent ARP replies associate attacker MAC with legitimate IP — redirects traffic. |
| DNS Poisoning | Corrupts DNS cache with fraudulent records — redirects users to attacker servers. |
| VLAN Hopping | Gains access to unauthorized VLANs via DTP trunk negotiation or double-tagging. |
| IP/MAC Spoofing | Forges source IP, MAC, or identity fields in packets. |
| Replay Attack | Captures and retransmits a previously valid packet. |
| Deauthentication | Wi-Fi attack sending forged deauth frames — disconnects clients, captures handshake for cracking. |

### Firewall Types

| Type | Layer | Description |
|---|---|---|
| Packet filter | 3/4 | Stateless rules based on IP, port, protocol |
| Stateful inspection | 4 | Tracks connection state — allows return traffic automatically |
| NGFW (Application-aware) | 7 | Deep packet inspection — identifies apps regardless of port |
| WAF | 7 | Protects web applications from SQL injection, XSS, HTTP-layer attacks |

Network zones (outside to inside): Internet → DMZ → Internal. DMZ hosts public-facing servers.

### VPN Types

| Type | Protocol | Key Details |
|---|---|---|
| IPsec Transport | Layer 3 | Encrypts payload only; original IP header intact |
| IPsec Tunnel | Layer 3 | Encrypts entire original packet; new IP header added |
| SSL/TLS VPN | SSL/TLS | Port 443; clientless or full-tunnel; traverses most firewalls |
| Split tunneling | N/A | Only corporate traffic goes through VPN; internet traffic bypasses |

IPsec protocols: AH (authentication only) and ESP (authentication + encryption). ESP preferred.

### Authentication Protocols

| Protocol | Transport | Port | Key Details |
|---|---|---|---|
| RADIUS | UDP | 1812/1813 | Network access AAA. Encrypts only the password. |
| TACACS+ | TCP | 49 | Cisco-preferred for device administration. Encrypts entire payload. |
| 802.1X | N/A | N/A | Port-based NAC. Supplicant → Authenticator → RADIUS server. Uses EAP. |
| LDAP | TCP/UDP | 389 | Directory service queries. LDAPS (encrypted) = port 636. |

### Wireless Security Standards

| Standard | Encryption | Status |
|---|---|---|
| WEP | RC4 (broken) | Never use |
| WPA/TKIP | TKIP (flawed) | Do not use for new deployments |
| WPA2/AES-CCMP | AES-CCMP | Current enterprise minimum standard |
| WPA3/SAE | SAE | Resistant to offline dictionary attacks; required for Wi-Fi 6 certification |

---

## Domain 5: Network Troubleshooting (22%)

### CompTIA Seven-Step Troubleshooting Model

| Step | Action |
|---|---|
| 1 | Identify the problem — gather information, observe symptoms, define scope |
| 2 | Establish a theory of probable cause — apply OSI model, generate hypotheses |
| 3 | Test the theory — confirm or disprove with minimal targeted action |
| 4 | Establish a plan of action — plan the fix with a rollback strategy |
| 5 | Implement the solution or escalate — apply fix; escalate if beyond expertise |
| 6 | Verify full system functionality — confirm the problem is resolved end-to-end |
| 7 | Document findings, actions, and outcomes — close the change record |

Never skip Step 7. The exam tests the order and purpose of every step.

### OSI Troubleshooting — Layer to Symptom Mapping

| OSI Layer | Symptoms | Tools/Commands |
|---|---|---|
| 1 Physical | No link light, cable faults, attenuation | Cable tester, TDR, optical power meter, VFL |
| 2 Data Link | Wrong VLAN, trunk issues, duplex mismatch, STP issues | show vlan, show interfaces trunk, show spanning-tree |
| 3 Network | Wrong IP, no route, APIPA address, wrong gateway | ping, traceroute, ipconfig, route print |
| 4 Transport | Port blocked, firewall drop, connection refused | netstat -an, telnet to port |
| 7 Application | DNS failure, service error, SSL certificate | nslookup, dig, browser error messages |

### Diagnostic Commands

| Symptom | Command | What to Look For |
|---|---|---|
| Wrong IP configuration | `ipconfig /all` | 169.254.x.x, wrong subnet, wrong gateway |
| Host unreachable | `ping` | TTL exceeded, Destination Unreachable, Request Timeout |
| Routing problem | `traceroute` / `tracert` | Where the path fails or shows high latency |
| DNS failure | `nslookup` / `dig` | No answer, SERVFAIL, wrong server responding |
| Port blocked | `netstat -an` | Expected port not in LISTENING state |
| ARP problem | `arp -a` | Missing or incomplete ARP entry |
| Bandwidth problem | `iperf` / speedtest | Actual vs. expected throughput |

### Common Symptom Patterns

| Symptom | Likely Cause |
|---|---|
| No link light | Physical layer failure (cable, NIC, port) |
| Slow speed + late collisions | Duplex mismatch |
| 169.254.x.x address | DHCP failure (APIPA assigned) |
| Can ping by IP, not by name | DNS failure |
| All apps work except one | Firewall or port blocking |
| Intermittent drops on 2.4 GHz Wi-Fi | Channel interference |
| Authentication failure on Wi-Fi | Wrong PSK, expired certificate, RADIUS unavailable |

### Cable Faults

| Fault | Description |
|---|---|
| Open circuit | Break in conductor — no continuity |
| Short circuit | Two conductors touching — unintended path |
| Crosstalk | Signal from one pair induces interference in adjacent pair |
| Split pair | Wires from different pairs twisted together — passes continuity, fails data |
| Reversed pair | Both wires in a pair swapped end-to-end |
| Attenuation | Signal loss over distance — exceeds cable specifications |

### Cable Testing Tools

| Tool | Tests For |
|---|---|
| Basic cable tester | Continuity only — opens, shorts, reversed pairs |
| Cable certifier | Full performance test including TDR, attenuation, crosstalk, length |
| Tone generator and probe | Traces cable path without labeling |
| Optical power meter | Measures fiber signal strength — identifies attenuation |
| Visual fault locator (VFL) | Red laser for fiber — identifies breaks and bends visually |

---

## Memorization Priority List

If study time is limited, master these in order:

1. Port numbers — the full table above
2. Subnetting — /24 through /30 host counts from memory
3. OSI layer to protocol mapping
4. STP port states and convergence times (802.1D vs RSTP)
5. VPN types — IPsec modes (Transport vs Tunnel), SSL VPN, split tunneling
6. Wireless standards — speeds, bands, and security (WPA2/WPA3)
7. SNMP — ports 161/162, SNMPv3 for security, traps vs. polling
8. CompTIA seven-step troubleshooting model — order and purpose of each step
9. Administrative distance values — Connected 0, Static 1, EIGRP 90, OSPF 110, RIP 120
10. Authentication protocols — RADIUS vs TACACS+, 802.1X components

---

## Exam Format Reference

| Item | Detail |
|---|---|
| Questions | Up to 90 (multiple choice + performance-based) |
| Time | 90 minutes |
| Passing score | 720 out of 900 |
| Domain 1 | Networking Concepts — 23% |
| Domain 2 | Infrastructure — 18% |
| Domain 3 | Network Operations — 17% |
| Domain 4 | Network Security — 20% |
| Domain 5 | Network Troubleshooting — 22% |

Performance-based questions (PBQs) appear at the beginning. Many candidates skip PBQs and return to them after completing multiple-choice questions.

---

---

## 9. Supplemental Resources

The following free resources support final exam preparation and CompTIA Network+ N10-008 certification study across all five exam domains.

**1. Professor Messer — CompTIA Network+ N10-008 Full Course (Free)**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer provides a complete free video course covering all five Network+ N10-008 exam domains — Networking Concepts, Infrastructure, Network Operations, Network Security, and Network Troubleshooting. His practice exams and study groups are highly rated by certification candidates. Essential final review resource.

**2. CompTIA Network+ N10-008 Official Exam Objectives (Free PDF)**
URL: https://www.comptia.org/training/resources/exam-objectives
Relevance: CompTIA's free published exam objectives document is the definitive checklist of every topic that can appear on the N10-008 exam. Use it as a final self-assessment: go through each objective and confirm you can explain or demonstrate it. Any objective you cannot confidently explain is a study gap.

**3. Jason Dion — Network+ Practice Questions (Free samples)**
URL: https://diontraining.com/
Relevance: Jason Dion (CompTIA-certified trainer) provides free sample practice questions and study resources for Network+. His performance-based question (PBQ) walkthroughs are particularly useful for the simulation questions that appear at the start of the real exam.

**4. SubnettingPractice.com — Subnetting Drills (Free)**
URL: https://www.subnettingpractice.com/
Relevance: Subnetting is consistently one of the most common failure points on the Network+ exam. This free tool provides unlimited subnetting practice with instant feedback, covering CIDR notation, host counts, network addresses, broadcast addresses, and VLSM — directly mapped to the exam's subnetting question types.

**5. Wireshark — Free Protocol Analysis and Sample Captures**
URL: https://www.wireshark.org/
Relevance: Wireshark provides hands-on familiarity with protocol behavior tested on the exam — DNS queries, DHCP DORA, TCP handshakes, ARP requests, ICMP, and RTP. The free sample capture library at wiki.wireshark.org/SampleCaptures provides pre-captured traces for every protocol covered in this course.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
