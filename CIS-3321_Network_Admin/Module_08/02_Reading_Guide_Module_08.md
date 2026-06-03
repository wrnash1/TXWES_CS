# Reading Guide: Module 08 — Network Security Concepts

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

### Introduction

Module 08 covers the security concepts that form Domain 4 of the CompTIA Network+ exam — 17% of exam content. You must be able to identify the correct security control for a given scenario, distinguish between attack types, and describe the architecture of a secure network perimeter. This reading guide organizes all vocabulary, comparison tables, and exam tips for the Module 08 lectures.

---

### 1. Core Vocabulary

**CIA triad** — The three foundational information security principles: Confidentiality, Integrity, and Availability.

**Confidentiality** — The principle that information is accessible only to those authorized to access it. Enforced by encryption.

**Integrity** — The principle that data has not been altered in transit or at rest without authorization. Enforced by hashing (SHA-256, MD5) and digital signatures.

**Availability** — The principle that systems and data are accessible to authorized users when needed. Protected by redundancy, failover, patching, and DoS mitigation.

**Firewall** — A network security device that monitors and controls traffic based on defined rules. Operates at the network perimeter or between internal segments.

**Stateless firewall (packet filter)** — Examines each packet independently without tracking connection state. Applies rules based on source/destination IP, port, and protocol in the individual packet header. Fast but cannot distinguish legitimate reply traffic from unsolicited traffic.

**Stateful firewall (SPI — Stateful Packet Inspection)** — Tracks the state of every active connection in a state table. Understands whether an incoming packet is part of an established, permitted connection or an unsolicited new connection. The industry standard for enterprise firewalls.

**State table** — The data structure maintained by a stateful firewall that records active connections: source IP, destination IP, source port, destination port, protocol, and connection state.

**Next-Generation Firewall (NGFW)** — Extends stateful inspection with deep packet inspection, application awareness, user identity integration, integrated IPS, and SSL/TLS inspection.

**Deep Packet Inspection (DPI)** — Inspection of the payload content of packets, not just header fields, to identify applications and detect threats regardless of port number.

**ACL (Access Control List)** — A list of permit and deny rules applied to a router interface or firewall policy. Used to implement stateless packet filtering.

**IDS (Intrusion Detection System)** — A passive monitoring system that analyzes traffic against known attack signatures or behavioral baselines and generates alerts. Does not block traffic.

**IPS (Intrusion Prevention System)** — An inline active security device that analyzes traffic and can drop, reset, or block malicious traffic in real time.

**NIDS (Network IDS)** — An IDS deployed to monitor all traffic on a network segment, typically via a SPAN (mirrored) port.

**HIDS (Host IDS)** — IDS software deployed on an individual host, monitoring system calls, log files, and local network connections.

**Signature-based detection** — Compares observed traffic or system events against a database of known attack patterns. Accurate for known threats; cannot detect zero-day attacks.

**Anomaly-based detection** — Establishes a baseline of normal behavior and alerts when deviations occur. Can detect novel attacks; higher false-positive rate.

**SPAN port** — A switch port configured to receive a mirrored copy of traffic from one or more other ports. Used to connect IDS sensors and packet analyzers to monitor traffic without being inline.

**DMZ (Demilitarized Zone)** — A network segment positioned between the untrusted internet and the trusted internal LAN, hosting services that must be publicly accessible (web servers, email gateways, public DNS, VPN concentrators).

**Two-firewall DMZ design** — An outer firewall separates the internet from the DMZ; an inner firewall separates the DMZ from the internal LAN. Provides maximum isolation.

**Three-legged firewall design** — A single firewall with three interfaces: one to the internet (WAN), one to the DMZ, and one to the internal LAN. Simpler but a single point of failure.

**AAA (Authentication, Authorization, Accounting)** — The framework for controlling and auditing network access. Authentication = who are you; Authorization = what are you allowed to do; Accounting = what did you do.

**RADIUS (Remote Authentication Dial-In User Service)** — An AAA protocol using UDP port 1812 for authentication and UDP port 1813 for accounting. Widely used for network device authentication and 802.1X wireless.

**TACACS+ (Terminal Access Controller Access-Control System Plus)** — A Cisco-developed AAA protocol using TCP port 49 that separates authentication, authorization, and accounting into distinct transactions. More granular than RADIUS for network device command authorization.

**MFA (Multi-Factor Authentication)** — Authentication requiring two or more factors from different categories: something you know, something you have, and something you are.

**Least privilege** — The security principle that every user, process, and system should have only the minimum access required for its function.

**Defense in depth** — The security principle of layering multiple overlapping security controls so that the failure of any single control does not result in a complete breach.

**DoS (Denial of Service)** — An attack that makes a system or service unavailable by exhausting resources. Originates from a single source.

**DDoS (Distributed Denial of Service)** — A DoS attack launched simultaneously from a distributed botnet of thousands or millions of compromised hosts.

**Botnet** — A network of compromised systems (bots/zombies) controlled by a command-and-control server, used to conduct DDoS attacks and other malicious activities.

**TCP SYN flood** — A DoS attack that exploits the TCP handshake by sending large volumes of SYN packets with forged source IPs, filling the target server's half-open connection table.

**MITM (Man-in-the-Middle)** — An attack where an adversary secretly intercepts and potentially modifies communication between two parties who believe they are communicating directly.

**ARP Poisoning (ARP Spoofing)** — A LAN-based MITM attack where the attacker sends forged ARP Replies to redirect traffic through the attacker's device by associating a legitimate IP address with the attacker's MAC address.

**Gratuitous ARP** — An unsolicited ARP Reply sent by a host to update others' ARP caches. Exploited in ARP poisoning attacks.

**Dynamic ARP Inspection (DAI)** — A Cisco switch security feature that validates ARP packets against the DHCP snooping binding table, dropping forged ARP Replies that do not match known IP-to-MAC bindings.

**DNS Poisoning (DNS Spoofing)** — An attack that injects forged DNS records into a resolver's cache to redirect users from legitimate domains to attacker-controlled IP addresses.

**DNSSEC** — DNS Security Extensions. Cryptographically signs DNS records to prevent unauthorized modification and protect against DNS poisoning.

**VLAN Hopping** — An attack that exploits trunk negotiation (switch spoofing) or double-tagged 802.1Q frames (double tagging) to send traffic onto VLANs the attacker is not authorized to access.

**Social engineering** — Manipulating people rather than exploiting technology. Includes phishing (email), spear-phishing (targeted email), vishing (voice).

**Honeypot** — A decoy system intentionally deployed to attract attackers, detect intrusions, and gather intelligence on attacker techniques. Any access to a honeypot is inherently suspicious.

**Honeynet** — A network of honeypots designed to simulate an entire enterprise environment for richer threat intelligence.

**NAC (Network Access Control)** — A security approach that assesses a device's compliance posture before granting full network access.

**Posture assessment** — The evaluation of a device's security compliance state (OS patch level, AV status, encryption) performed by NAC before granting network admission.

**Quarantine VLAN** — A restricted network segment where non-compliant devices are placed by NAC until they achieve compliance, with access only to remediation resources.

**802.1X** — An IEEE standard for port-based Network Access Control. Requires devices to authenticate via EAP before being granted network access. Used with RADIUS for both wired and wireless NAC.

**Mantrap (airlock)** — A physical security control consisting of two consecutive controlled doors. The first door must close and authenticate before the second opens, preventing tailgating.

**Tailgating (piggybacking)** — An unauthorized person physically following an authorized person through a controlled entry point.

---

### 2. Firewall Type Comparison

| Feature | Stateless (Packet Filter) | Stateful (SPI) | NGFW |
|---------|--------------------------|----------------|------|
| Examines | Individual packets in isolation | Packets + connection state | Packets + state + application payload |
| State tracking | None | Connection state table | Connection state table |
| Application visibility | No | No | Yes (DPI) |
| Reply traffic handling | Requires explicit inbound permit rule | Automatic via state table | Automatic + policy-based |
| Performance overhead | Low | Moderate | High |
| Detects | Header-based threats | Connection-based threats | Application-layer threats |
| Example implementation | Router ACL | Cisco ASA, pfSense | Palo Alto, Fortinet FortiGate |

---

### 3. IDS vs. IPS Comparison

| Feature | IDS | IPS |
|---------|-----|-----|
| Deployment position | Passive (SPAN port) or inline | Must be inline |
| Traffic blocking | Cannot block | Can block, drop, reset |
| Response | Alert only | Alert + active prevention |
| Impact of false positive | Unnecessary alert | Blocks legitimate traffic |
| Impact of false negative | Missed attack (alert only) | Attack succeeds and is not blocked |
| Use case | Monitor and audit | Real-time threat prevention |

---

### 4. Attack Type Reference Table

| Attack | Target | Mechanism | Countermeasure |
|--------|--------|-----------|----------------|
| DoS | Availability | Single-source traffic flood or exploit | Rate limiting, firewall block |
| DDoS | Availability | Botnet distributed flood | Scrubbing services, rate limiting |
| TCP SYN flood | Availability | Half-open connection table exhaustion | SYN cookies, rate limiting |
| MITM | Confidentiality, Integrity | Intercept A-to-B traffic path | TLS encryption, certificate validation |
| ARP Poisoning | Confidentiality | Forged ARP Replies on LAN | Dynamic ARP Inspection (DAI) |
| DNS Poisoning | Confidentiality | Forged DNS cache records | DNSSEC |
| VLAN Hopping | Confidentiality | Switch spoofing or double-tagging | Disable auto-trunk, set access mode |
| Brute Force | Authentication | Exhaustive credential enumeration | Account lockout, MFA |
| Social Engineering | Authentication | Human manipulation | Security awareness training |

---

### 5. AAA Protocol Comparison

| Feature | RADIUS | TACACS+ |
|---------|--------|---------|
| Protocol / Port | UDP 1812 (auth), UDP 1813 (acct) | TCP 49 |
| Developer | Open standard (RFC 2865) | Cisco proprietary |
| Encryption | Encrypts password only | Encrypts entire payload |
| AAA separation | Combined auth/authz | Fully separated auth, authz, acct |
| Best for | Network device auth, 802.1X wireless | Granular Cisco device command authorization |

---

### 6. DMZ Architecture Summary

Two-firewall DMZ design provides maximum security:

- Outer firewall: Permits inbound traffic from internet to DMZ (ports 80, 443, 25 as needed). Denies direct internet access to internal LAN.
- DMZ segment: Contains public-facing servers only. No internal resources.
- Inner firewall: Permits only specific required traffic from DMZ servers to internal systems (e.g., web server to database on port 3306). Denies all unsolicited DMZ-to-LAN traffic.

Result: Even a fully compromised DMZ server cannot reach internal systems beyond what the inner firewall permits.

---

### 7. Certification Exam Tips

Tip 1: The CIA triad question is asked in multiple forms. When the exam asks "which property does encryption provide?" the answer is Confidentiality. When it asks about hashing, the answer is Integrity. When it asks about redundancy and uptime, the answer is Availability.

Tip 2: IDS is always passive — it uses a SPAN port and can only alert. IPS must be inline and can block. If the scenario says the device can drop traffic, it is IPS. If it only sends alerts, it is IDS.

Tip 3: ARP poisoning occurs on the LAN (Layer 2). The countermeasure is Dynamic ARP Inspection (DAI), which is a switch feature. TLS encryption is a secondary defense — it protects the payload even if ARP poisoning succeeds.

Tip 4: RADIUS uses UDP. TACACS+ uses TCP. RADIUS encrypts the password only. TACACS+ encrypts the entire session. TACACS+ separates authentication from authorization — this is the key advantage for granular device command authorization.

Tip 5: The DMZ exam question usually asks which type of servers belong in a DMZ. The answer is internet-facing servers: web servers, mail gateways, public DNS, VPN concentrators. Internal database servers and domain controllers belong inside the LAN, not the DMZ.

Tip 6: DoS vs. DDoS — the distinguishing characteristic is source count. DoS = single source. DDoS = multiple sources (botnet). When the exam describes traffic from thousands of different IP addresses, it is always DDoS.

Tip 7: A honeypot does not prevent attacks. It detects them and provides intelligence. Do not confuse honeypot with IPS. Honeypot = decoy. IPS = active blocking.

Tip 8: VLAN hopping countermeasure: explicitly configure all access ports as `switchport mode access` on Cisco switches. This prevents trunk negotiation with attacking hosts.

Tip 9: NAC quarantine VLAN: non-compliant devices are placed in a restricted VLAN where they can only reach patching and AV update servers. After remediation, the switch reassigns them to the production VLAN.

---

### 8. Required Reading and Viewing

Required Reading: Computer Networking: Principles, Protocols and Practice — read the chapters on network security, firewalls, and common attack types.

Required Viewing: Professor Messer's Network+ N10-008 video series — watch all Domain 4 security segments including firewalls, IDS/IPS, common threats, and physical security. Available free at professormesser.com.

Supplemental Reference: CompTIA official N10-008 exam objectives — Domain 4.0 Network Security. Focus on sections 4.1 (attack types), 4.2 (network hardening), 4.3 (physical security), and 4.4 (access management).

---

### 9. Study Checklist

- [ ] Explain each component of the CIA triad and give a network security example of each
- [ ] Describe the difference between a stateless and stateful firewall in terms of what each tracks
- [ ] Explain what a state table is and why it allows stateful firewalls to automatically permit reply traffic
- [ ] Describe NGFW capabilities beyond stateful inspection
- [ ] Distinguish IDS from IPS by deployment method, capability, and consequence of false positives
- [ ] Explain the purpose and architecture of a two-firewall DMZ design
- [ ] Identify which server types belong in a DMZ vs. inside the internal LAN
- [ ] State the protocols and port numbers for RADIUS and TACACS+
- [ ] Explain the difference between DoS (single source) and DDoS (botnet)
- [ ] Describe how a TCP SYN flood works and why it exhausts server resources
- [ ] Explain how ARP poisoning enables a MITM attack and how DAI prevents it
- [ ] Describe DNS poisoning and the role of DNSSEC in preventing it
- [ ] Explain two methods of VLAN hopping and the switch configuration that prevents each
- [ ] Describe what a honeypot is, how it works, and what security function it serves
- [ ] Explain how NAC uses 802.1X and RADIUS to enforce device posture before network admission
- [ ] List five network security hardening practices from the lecture
- [ ] Complete Lab 08 and answer all lab questions
- [ ] Post your Module 08 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 08 Quiz

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
