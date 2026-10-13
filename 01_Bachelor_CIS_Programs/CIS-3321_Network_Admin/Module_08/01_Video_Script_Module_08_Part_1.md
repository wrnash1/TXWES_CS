# Video Script: Module 08 — Network Security Concepts (Part 1 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

### SLIDE 1 — Welcome and Overview

Welcome back to CIS-3321 Network Administration. I'm Professor Nash. Module 8 covers Network Security Concepts — the theoretical foundation and practical architecture that every network professional must understand.

In Part 1 we cover the CIA triad, firewalls (stateful vs. stateless), IDS and IPS, and the DMZ architecture. In Part 2 we move to VPN types, honeypots, and the common attack categories that appear on the Network+ exam — DoS, DDoS, man-in-the-middle, and ARP poisoning.

Network security is Domain 4 of the Network+ exam, accounting for 17% of exam content. Let's begin.

---

### SLIDE 2 — The CIA Triad

Every security decision in networking traces back to three fundamental principles collectively called the **CIA triad**:

**Confidentiality** — Information is accessible only to those authorized to access it. Encryption enforces confidentiality — even if an attacker captures the data, they cannot read it without the key. Examples: TLS encrypting web traffic, WPA3 encrypting wireless frames, VPN encrypting site-to-site traffic.

**Integrity** — Data has not been altered in transit or at rest without authorization. Hashing algorithms such as SHA-256 create a fingerprint of data — any alteration changes the hash, revealing tampering. Digital signatures combine hashing with asymmetric encryption to provide integrity and authentication together.

**Availability** — Systems and data are accessible to authorized users when needed. Denial-of-Service attacks target availability. Redundancy, failover, load balancing, and patch management all protect availability.

The CIA triad is the lens through which every security control is evaluated. On the exam, when a question asks "which security property does encryption provide," think CIA — encryption primarily provides confidentiality.

---

### SLIDE 3 — Firewalls: Purpose and Function

A **firewall** is a network security device that monitors and controls traffic based on a defined set of security rules. Firewalls sit at network boundaries — between the internet and a corporate LAN, between network segments, or on individual hosts.

Firewalls operate by examining packets and making permit or deny decisions based on:

- Source and destination IP addresses
- Source and destination port numbers
- Protocol (TCP, UDP, ICMP)
- Direction (inbound vs. outbound)
- Connection state (for stateful firewalls)

Firewalls are the primary tool for enforcing network access policy. They implement the principle of least privilege at the network level — permit only what is explicitly needed, deny everything else.

---

### SLIDE 4 — Stateless Firewalls (Packet Filtering)

A **stateless firewall** (also called a packet filter) examines each packet in isolation, independently of any other packets. It applies rules based solely on the headers of the individual packet — source IP, destination IP, source port, destination port, protocol, and sometimes TCP flags.

Advantages:

- Simple and fast — no state tracking overhead
- Low resource consumption
- Effective for basic network perimeter rules

Limitations:

- Cannot track the relationship between packets — each packet is evaluated independently
- Cannot distinguish whether a packet is part of an established connection or a new, potentially malicious connection
- Vulnerable to IP spoofing — a packet with a forged source address may pass rules that rely on source IP
- Cannot inspect application content

Example stateless rule: "Permit inbound TCP with destination port 80 from any source." This permits all inbound packets destined for port 80 — but also permits any crafted packet with destination port 80, including packets that are not legitimate web requests.

Stateless firewalls are implemented in router ACLs (Access Control Lists) — Cisco's `ip access-list` commands implement stateless packet filtering.

---

### SLIDE 5 — Stateful Firewalls

A **stateful firewall** (also called a stateful inspection firewall or SPI — Stateful Packet Inspection) tracks the state of every active network connection in a state table.

When a client initiates a connection (SYN), the firewall creates an entry in the state table recording the source IP, destination IP, source port, destination port, protocol, and connection state. As the connection progresses (SYN-ACK, ACK), the state table entry is updated. When the connection terminates (FIN or RST), the entry is removed.

The key benefit: the firewall uses the state table to determine whether an incoming packet is part of a known, established connection or an unsolicited new packet attempting to bypass rules.

Example: An internal host initiates a connection to an external web server. The outbound SYN is permitted by policy. The SYN-ACK response from the web server is automatically permitted by the state table — because the firewall knows this is a valid reply to an established outbound connection. You do not need an explicit inbound permit rule for established traffic.

Compared to stateless firewalls:

- More secure — understands connection context
- Can detect and block connection-based attacks like TCP SYN floods (partially)
- Higher resource use due to state table maintenance

Most enterprise firewalls today are stateful. Cisco ASA, Palo Alto, Fortinet FortiGate, and Check Point are all stateful firewall products.

---

### SLIDE 6 — Next-Generation Firewalls (NGFW)

**Next-Generation Firewalls** extend stateful inspection with additional capabilities:

- **Deep Packet Inspection (DPI)**: Inspects the payload of packets, not just headers, to identify applications regardless of port number — for example, identifying Facebook traffic even if it runs on port 443
- **Application awareness**: Can permit or deny specific applications (allow LinkedIn, block TikTok) regardless of protocol or port
- **User identity integration**: Can apply rules based on Active Directory user or group identity, not just IP address
- **Integrated IPS**: Intrusion prevention functionality built into the firewall
- **SSL/TLS inspection**: Can decrypt, inspect, and re-encrypt HTTPS traffic to detect threats hidden in encrypted payloads

NGFWs are the current enterprise standard. The Network+ exam tests NGFW as a concept — know that it extends traditional stateful inspection with application-layer visibility.

---

### SLIDE 7 — IDS: Intrusion Detection System

A **stateful firewall** permits or denies traffic based on rules. An **IDS (Intrusion Detection System)** monitors traffic and alerts administrators when it detects suspicious patterns — but it does not block traffic on its own.

IDS deployment modes:

- **Network IDS (NIDS)**: Placed inline or on a SPAN (mirrored) port to monitor all traffic on a network segment. The NIDS inspects each packet against a signature database and generates alerts for matches.
- **Host IDS (HIDS)**: Software running on an individual host, monitoring system calls, log files, filesystem changes, and network connections on that specific machine.

IDS detection methods:

- **Signature-based detection**: Compares traffic or system events against a database of known attack patterns. Fast and accurate for known threats. Cannot detect zero-day attacks with no existing signature.
- **Anomaly-based detection**: Establishes a baseline of normal behavior and alerts when traffic or behavior deviates from the baseline. Can detect new, unknown attacks. Higher false-positive rate than signature-based detection.

IDS limitation: It detects and alerts — it does not block. An IDS is a passive sensor. An IPS takes it further.

---

### SLIDE 8 — IPS: Intrusion Prevention System

An **IPS (Intrusion Prevention System)** extends IDS by adding the ability to actively block or drop malicious traffic in real time.

IPS deployment: The IPS must be placed **inline** in the traffic path — all traffic passes through the IPS device, giving it the ability to drop packets before they reach the destination. A SPAN port deployment only receives a copy of traffic and cannot block anything.

IPS response actions:

- Drop the offending packet or packet stream
- Reset the TCP connection (send RST to both ends)
- Block all further traffic from the offending source IP (temporarily or permanently)
- Alert the administrator

IPS vs. IDS comparison:

| Feature | IDS | IPS |
|---------|-----|-----|
| Traffic visibility | Passive (SPAN/mirror) or inline | Must be inline |
| Can block traffic | No | Yes |
| Response | Alert only | Alert + block/drop |
| Risk of false positives | Low consequence (only alerts) | High consequence (can block legitimate traffic) |

The exam frequently asks to distinguish IDS (passive, alert-only) from IPS (inline, active blocking). Remember: IDS detects; IPS prevents.

---

### SLIDE 9 — DMZ: Demilitarized Zone

A **DMZ (Demilitarized Zone)** is a network segment that sits between the untrusted external network (internet) and the trusted internal network, hosting services that must be accessible from the internet while isolating the internal network from direct internet exposure.

Why DMZ architecture matters: Without a DMZ, a web server accessed from the internet must either be on the internal network (exposing the internal network to internet threats) or fully exposed to the internet with no internal firewall protection. The DMZ provides a middle ground.

Services commonly placed in a DMZ:

- Public web servers
- Email gateway servers (SMTP relay)
- Public DNS servers
- VPN concentrators
- Remote access gateways

---

### SLIDE 10 — DMZ Architecture: Two-Firewall Design

The most secure DMZ uses a two-firewall design:

- **Outer firewall** (between internet and DMZ): Permits inbound traffic to DMZ services (port 80, 443, 25) and blocks everything else
- **DMZ segment**: Contains public-facing servers
- **Inner firewall** (between DMZ and internal LAN): Permits only specific, necessary traffic from DMZ servers to internal systems (for example, DMZ web server to internal database on port 3306); blocks all unsolicited inbound traffic from DMZ to LAN

Traffic flow:

- Internet user → permitted through outer firewall to DMZ web server → DMZ web server queries internal DB through inner firewall on specific permitted port only
- Even if the DMZ web server is completely compromised, the inner firewall prevents the attacker from directly accessing the internal LAN

Three-legged single-firewall design: Some organizations use a single firewall with three interfaces — one to the internet (WAN), one to the DMZ, and one to the internal LAN. Simpler to manage but single point of failure.

The Network+ exam tests understanding of DMZ purpose and two-firewall architecture.

---

### SLIDE 11 — AAA: Authentication, Authorization, Accounting

Security architecture includes not just firewalls and IDS/IPS but also **AAA** — the framework for controlling who accesses what and tracking what they do.

**Authentication** — Verifying identity. "Who are you?" Authentication factors:

- Something you know: password, PIN
- Something you have: smart card, hardware token, authenticator app
- Something you are: biometrics (fingerprint, facial recognition)

Multi-factor authentication (MFA) requires two or more factors from different categories.

**Authorization** — Determining what an authenticated user is permitted to do. "What are you allowed to do?" Authorization policies enforce least privilege — users receive only the permissions required for their role.

**Accounting** — Recording what authenticated and authorized users actually did. "What did you do?" Accounting creates audit trails: login times, commands executed, files accessed, configuration changes made. Required for forensics and compliance.

AAA is implemented in network environments using protocols:

- **RADIUS** (Remote Authentication Dial-In User Service): UDP 1812 (authentication) and UDP 1813 (accounting). Widely used for network device authentication and wireless 802.1X.
- **TACACS+** (Terminal Access Controller Access-Control System Plus): TCP 49. Cisco proprietary. Separates authentication, authorization, and accounting into distinct steps — provides more granular control than RADIUS for network device command authorization.

---

### SLIDE 12 — Principle of Least Privilege and Defense in Depth

Two foundational security principles appear throughout the Network+ exam:

**Principle of Least Privilege** — Every user, system, and process should have the minimum access required to perform its function and nothing more. Applied to networks: a guest wireless VLAN should not be able to reach internal servers. A web server in the DMZ should not be able to initiate connections to any internal host except its specific database on its specific port.

**Defense in Depth** — Security should be implemented in multiple overlapping layers so that the failure of any single control does not result in a complete breach. Applied to networks: the internet-facing perimeter has a firewall; internal segments are also firewalled; individual hosts run host-based firewalls; IPS monitors traffic; SIEM aggregates logs for correlation. An attacker who bypasses the perimeter firewall still faces additional controls.

These two principles work together: least privilege limits the blast radius of any single compromise; defense in depth ensures multiple barriers must be overcome for a successful attack.

---

### SLIDE 13 — Part 1 Summary

Let's summarize Part 1:

- **CIA triad**: Confidentiality (encryption), Integrity (hashing), Availability (redundancy/uptime)
- **Stateless firewall**: Examines each packet independently; no connection state tracking; fast but limited
- **Stateful firewall**: Tracks connection state in a state table; understands reply traffic; industry standard
- **NGFW**: Extends stateful with application awareness, DPI, user identity, and integrated IPS
- **IDS**: Passive monitoring; alerts only; signature-based or anomaly-based; does NOT block
- **IPS**: Inline placement; actively blocks malicious traffic; extends IDS with prevention capability
- **DMZ**: Isolated segment for internet-facing servers; two-firewall design provides maximum protection
- **AAA**: Authentication (who), Authorization (what), Accounting (audit trail); RADIUS UDP 1812/1813; TACACS+ TCP 49
- **Least privilege and defense in depth**: Foundational principles applied throughout network security design

In Part 2: VPN types, honeypots, and the attack categories you must recognize for the exam — DoS, DDoS, man-in-the-middle, ARP poisoning, and more.

---

*End of Part 1 — Continue to Part 2*
