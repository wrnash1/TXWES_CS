# Reading Guide: Module 05 - Network Traffic Analysis and Packet Inspection

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4332 &BULL; CYBERSECURITY ANALYST & THREAT HUNTING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Introduction

Network traffic analysis is the discipline of capturing, interpreting, and drawing security conclusions from data moving across a network. Every lateral movement attempt, every C2 beaconing pattern, and every data exfiltration event leaves evidence in network traffic. This guide provides the protocol reference, traffic capture concepts, pattern recognition tables, and query syntax you need to analyze network data and succeed on CySA+ exam questions in this domain.

---

## Section 1: TCP/IP Protocol Reference

### 1.1 TCP/IP Model Layers

| Layer | Name | Protocols | Security Relevance |
|---|---|---|---|
| 4 | Application | HTTP, HTTPS, DNS, FTP, SSH, SMTP, RDP, LDAP | Application-layer attacks, C2 protocols, credential theft |
| 3 | Transport | TCP, UDP | Port scanning, SYN floods, connection analysis |
| 2 | Internet | IP, ICMP, ARP | IP spoofing, ICMP tunneling, ARP poisoning |
| 1 | Network Access | Ethernet, 802.11 Wi-Fi | MAC spoofing, rogue AP, physical layer attacks |

### 1.2 Key Port Numbers

Memorize these. They appear in exam questions when identifying services from traffic data.

| Port | Protocol | Service | Security Notes |
|---|---|---|---|
| 20/21 | TCP | FTP | Cleartext file transfer; often exploited |
| 22 | TCP | SSH | Encrypted remote shell; brute-force target |
| 23 | TCP | Telnet | Cleartext remote shell; should not exist in modern environments |
| 25 | TCP | SMTP | Email relay; open relays enable spam and phishing |
| 53 | TCP/UDP | DNS | DNS tunneling; exfiltration; DGA C2 |
| 80 | TCP | HTTP | Cleartext web; web attacks; C2 over HTTP |
| 110 | TCP | POP3 | Email retrieval; cleartext credentials |
| 143 | TCP | IMAP | Email retrieval; cleartext or STARTTLS |
| 389 | TCP/UDP | LDAP | Directory queries; credential brute-force |
| 443 | TCP | HTTPS | Encrypted web; C2 over TLS; majority of traffic |
| 445 | TCP | SMB | File sharing; lateral movement (EternalBlue, PsExec) |
| 636 | TCP | LDAPS | Encrypted LDAP; preferred over 389 |
| 993 | TCP | IMAPS | Encrypted email retrieval |
| 995 | TCP | POP3S | Encrypted email retrieval |
| 1433 | TCP | MSSQL | Database; SQL injection targets; lateral movement |
| 3306 | TCP | MySQL | Database; injection targets |
| 3389 | TCP | RDP | Remote desktop; lateral movement; brute-force target |
| 5985/5986 | TCP | WinRM | Windows remote management; used in lateral movement |
| 8080 | TCP | HTTP Alt | Proxy, alternate web; used by malware for C2 |
| 8443 | TCP | HTTPS Alt | Alternate HTTPS; sometimes used by management interfaces |

### 1.3 TCP vs. UDP Comparison

| Attribute | TCP | UDP |
|---|---|---|
| Connection type | Connection-oriented (three-way handshake) | Connectionless |
| Reliability | Guaranteed delivery with retransmission | No delivery guarantee |
| Ordering | Ordered delivery | No ordering |
| Speed | Slower due to overhead | Faster |
| Use cases | HTTP, SSH, SMTP, FTP, RDP | DNS, DHCP, VoIP, streaming, NTP |
| Header size | 20 bytes minimum | 8 bytes |

---

## Section 2: TCP Flags and Connection Analysis

### 2.1 TCP Flag Reference

| Flag | Code | Meaning | Security Significance |
|---|---|---|---|
| SYN | S | Synchronize; initiate connection | SYN flood = DoS; port scan indicator |
| SYN-ACK | SA | Server acknowledges connection request | Part of normal handshake |
| ACK | A | Acknowledge received data | Normal ongoing communication |
| FIN | F | Graceful connection termination | Normal; FIN scan = stealth scan technique |
| RST | R | Reset; abrupt termination | Port closed response; attack detection evasion reset |
| PSH | P | Push data to application immediately | Data transfer indicator |
| URG | U | Urgent pointer valid | Rare; used in XMAS scan technique |

### 2.2 Scan Type Signatures

| Scan Type | TCP Flags Sent | Response for Open Port | Response for Closed Port | Detection Evasion |
|---|---|---|---|---|
| Full Connect Scan | SYN | SYN-ACK, then ACK completes | RST | Low — completes handshake; logged |
| SYN (Half-Open) Scan | SYN | SYN-ACK (scanner sends RST) | RST | Medium — does not complete handshake |
| FIN Scan | FIN | No response (Linux) | RST (Windows always RSTs) | Medium — avoids SYN inspection |
| NULL Scan | No flags | No response (Linux) | RST (Windows) | Medium — unusual; may bypass old filters |
| XMAS Scan | FIN, URG, PSH | No response (Linux) | RST (Windows) | Medium — technically malformed; may bypass stateless filters |
| UDP Scan | UDP packet | No response or service reply | ICMP Port Unreachable | High — harder to detect; slower |

### 2.3 TCP Three-Way Handshake

Normal connection sequence:

```text
Client -> Server: SYN (seq=100)
Server -> Client: SYN-ACK (seq=200, ack=101)
Client -> Server: ACK (ack=201)
[Connection established — data transfer begins]
```

SYN flood attack sequence (DoS):

```text
Attacker -> Server: SYN (spoofed src IP)
Server -> Spoofed IP: SYN-ACK [no response ever comes]
Server -> Spoofed IP: SYN-ACK retransmit [no response]
[Server half-open connection queue fills; legitimate connections refused]
```

---

## Section 3: Network Traffic Capture Methods

### 3.1 Capture Method Comparison

| Method | Data Captured | Volume | Use Case |
|---|---|---|---|
| Full Packet Capture (PCAP) | Complete packet including payload | Very high (TB/day on busy links) | Incident investigation, forensics, malware analysis |
| NetFlow / IPFIX | Flow metadata (IPs, ports, bytes, packets, timestamps) | Low (~1% of full capture) | Continuous enterprise-wide monitoring, baseline analysis |
| sFlow | Sampled packet headers (1 in N packets) | Low-medium | Large-scale traffic characterization; less precise than NetFlow |
| SPAN Port / Mirror Port | Copy of traffic to analyzer | Same as full capture | Passive monitoring without network disruption |
| Network TAP | Hardware device tapping physical link | Same as full capture | Highest-fidelity passive capture; no missed packets |

### 3.2 NetFlow Record Fields

| Field | Description |
|---|---|
| Source IP | Originating IP address |
| Destination IP | Target IP address |
| Source Port | Source transport port |
| Destination Port | Destination transport port |
| Protocol | IP protocol number (TCP=6, UDP=17, ICMP=1) |
| Start Time | First packet timestamp |
| End Time | Last packet timestamp |
| Bytes | Total bytes transferred |
| Packets | Total packet count |
| Flags | TCP flags seen across the flow |

---

## Section 4: Suspicious Traffic Pattern Reference

### 4.1 Attack-to-Traffic Pattern Mapping

| Attack Type | Traffic Indicators | Log/Flow Evidence |
|---|---|---|
| Port scan (TCP SYN) | Many SYN packets to different destination ports from one source; many RST responses | High RST rate in firewall logs; many distinct destination ports from one src IP |
| SYN flood (DoS) | Many SYN packets with no corresponding ACK completions | Half-open connections; server resource exhaustion; SYN-ACK retransmits |
| Brute force SSH | Many TCP connections to port 22 from one IP; many RST or reject responses | Firewall: repeated DENY TCP src->dest:22; auth log: failed password entries |
| C2 beaconing | Regular interval outbound connections to same destination; consistent byte counts | Flow: same src-dst pair repeated at regular intervals; timing deviation low |
| DNS tunneling | Long DNS query names (>50 chars); high volume unique subdomains; TXT/NULL queries | DNS log: long query names; base64-encoded subdomains; queries to single domain |
| Data exfiltration | Large outbound flow volumes; large HTTPS POST requests | Flow: src_bytes >> dst_bytes on outbound flows; large single session byte counts |
| SMB lateral movement | Workstation-to-workstation TCP 445 connections | Flow: internal src -> internal dst on port 445; non-server source hosts |
| DGA C2 | Many DNS queries for random-looking domains; NX responses | DNS log: many NXDOMAIN responses; high entropy domain names; short TTLs |
| ICMP tunnel | ICMP echo with large payloads (>64 bytes data field) | Network: large ICMP traffic; data in ICMP payload beyond normal ping size |

### 4.2 Beaconing Detection

Beaconing is identified by regularity in connection timing. Key indicators:

- Low standard deviation in connection intervals (near-zero variance = automated)
- Same source-destination IP pair appearing repeatedly in flow data
- Consistent byte counts per session (automated check-in sends same size request each time)
- Connections occurring during off-hours when no user is expected to be active
- Destination IP not resolving to a known service or CDN

### 4.3 DNS Analysis Indicators

| Indicator | Normal DNS | Suspicious DNS |
|---|---|---|
| Query name length | Short (< 30 characters) | Long (> 50 characters) |
| Domain entropy | Low (real words, numbers) | High (random-looking characters) |
| Query volume per domain | Low-moderate | High volume to one domain |
| Record type | A, AAAA, CNAME | High TXT, NULL, or MX queries |
| TTL values | Standard (hours to days) | Very low (seconds to minutes — fast flux) |
| Response rate | Mix of success and NXDOMAIN | High NXDOMAIN rate (DGA misses) |

---

## Section 5: IDS and IPS

### 5.1 IDS vs. IPS Comparison

| Attribute | Network IDS (NIDS) | Network IPS (NIPS) |
|---|---|---|
| Placement | Passive — SPAN port or TAP | Inline — all traffic passes through |
| Action on detection | Alerts only | Can alert and block |
| Latency impact | None — out of band | Adds processing latency |
| Single point of failure | No — does not affect traffic if it fails | Yes — failure can drop traffic |
| Best for | Detection and visibility | Prevention of known attacks |

### 5.2 Detection Methods

| Method | How It Works | Strengths | Weaknesses |
|---|---|---|---|
| Signature-based | Matches traffic against database of known attack patterns | High accuracy for known attacks; low false positive rate | Zero detection of novel unknown attacks |
| Anomaly-based | Compares traffic to established baseline; alerts on deviation | Can detect zero-day and novel attacks | Requires good baseline; higher false positive rate |
| Behavioral/Heuristic | Detects attack-like patterns (scanning velocity, beaconing regularity) | Detects techniques without specific signatures | Complex to tune; may miss subtle behaviors |

---

## Section 6: Encrypted Traffic Analysis

### 6.1 What Remains Visible in Encrypted Traffic

| Data Element | Visible in Encrypted Traffic? | Method |
|---|---|---|
| Source and destination IP | Yes | IP header (unencrypted) |
| Source and destination port | Yes | Transport header (unencrypted) |
| Packet counts and byte volumes | Yes | Flow metadata |
| Connection timing and intervals | Yes | Flow metadata |
| TLS version and cipher suites | Yes | TLS handshake (cleartext before encryption) |
| SNI (Server Name Indication) | Yes | TLS Client Hello extension |
| Payload content | No | Encrypted |
| HTTP headers and body | No | Encrypted in TLS |

### 6.2 JA3 and JA3S Fingerprinting

JA3 is a method of fingerprinting TLS client behavior by hashing parameters from the TLS Client Hello message including TLS version, cipher suites, extensions, elliptic curves, and elliptic curve point formats. The hash produces a short string that identifies a specific TLS client configuration.

Known malware families often have distinctive JA3 hashes because they use specific, often older TLS configurations. Security tools correlate JA3 hashes against known-malicious fingerprint databases to identify malware C2 traffic even when payload is encrypted.

JA3S fingerprints the TLS Server Hello using the server's response parameters.

---

## Section 7: Wireshark Display Filter Reference

### 7.1 Common Display Filters

| Filter | Purpose |
|---|---|
| `ip.addr == 203.0.113.47` | Show all traffic to or from a specific IP |
| `tcp.port == 443` | Show all TLS traffic |
| `tcp.flags.syn == 1 and tcp.flags.ack == 0` | Show SYN packets only (connection initiations) |
| `tcp.flags.reset == 1` | Show RST packets (port closed, connection refused) |
| `dns` | Show all DNS traffic |
| `http.request.method == "POST"` | Show HTTP POST requests |
| `icmp.type == 8` | Show ICMP echo requests (ping) |
| `frame.len > 1000 and icmp` | Show large ICMP packets (possible ICMP tunnel) |
| `dns.qry.name contains "base64"` | Show DNS queries containing encoded strings |
| `!(arp or dns or icmp)` | Exclude noise to focus on TCP/UDP sessions |

---

## CySA+ Exam Tips

Exam Tip 1: Know key port numbers cold. Exam questions describe a connection to a specific port and ask what service is being targeted or what attack is likely.

Exam Tip 2: NIDS is passive (SPAN port) and alerts only. NIPS is inline and can block. If an exam question says a device generates alerts but does not block, it is an IDS.

Exam Tip 3: SYN flood attacks target Availability. They exhaust the server's half-open connection queue. The defense is SYN cookies or rate limiting.

Exam Tip 4: DNS tunneling indicators: long query names, base64-encoded subdomains, high volume to one domain, TXT/NULL record queries. If a question describes unusual DNS behavior with these characteristics, DNS tunneling is the answer.

Exam Tip 5: Beaconing = regular intervals + same destination. Low standard deviation in connection timing is the key mathematical indicator.

Exam Tip 6: SNI (Server Name Indication) is visible in TLS Client Hello even in encrypted traffic. It reveals the hostname being connected to and is used to detect malicious domains in encrypted C2 traffic.

Exam Tip 7: JA3 hashes fingerprint TLS clients. Known malware has known JA3 hashes. This is tested as a technique for detecting encrypted malware C2 traffic.

Exam Tip 8: Flow data provides scalable monitoring at low storage cost. Full packet capture provides complete visibility but requires enormous storage. The exam tests which is appropriate for which use case.

---

## Glossary

- Anomaly-based Detection: IDS/IPS method that detects deviations from an established traffic baseline
- Beaconing: Regular, automated outbound communication from malware to a C2 server at consistent time intervals
- DGA: Domain Generation Algorithm; malware technique that generates domain names algorithmically to locate C2 servers
- DNS Tunneling: Technique that encodes data in DNS queries to exfiltrate data or maintain C2 covertly
- Full Packet Capture: Capturing complete packet content including payloads for analysis
- IDS: Intrusion Detection System; monitors traffic and generates alerts; does not block
- IPS: Intrusion Prevention System; inline, actively blocks detected threats
- JA3: TLS client fingerprinting method based on Client Hello parameters
- NetFlow: Cisco-developed flow metadata standard capturing connection-level statistics
- NIDS: Network Intrusion Detection System; passive detection on SPAN port or TAP
- NIPS: Network Intrusion Prevention System; inline active detection and blocking
- PCAP: Packet Capture file format; container for full packet capture data
- Signature-based Detection: IDS/IPS method using known attack pattern databases
- SNI: Server Name Indication; TLS extension that reveals the hostname in a TLS Client Hello
- SPAN Port: Switched Port Analyzer; switch port that mirrors traffic to a monitoring device
- SYN Flood: DoS attack overwhelming a server by sending SYN packets without completing the three-way handshake
- TAP: Network Test Access Point; hardware device providing passive full-duplex packet capture
- TCP Three-Way Handshake: SYN, SYN-ACK, ACK sequence establishing a TCP connection

---

## Required Resources

- Official CySA+ CS0-003 exam objectives: comptia.org
- Professor Messer CySA+ CS0-003 free study materials: professormesser.com

---

## Study Checklist

- [ ] Recall all port numbers in Section 1.2 without the table
- [ ] Describe the TCP three-way handshake and identify what SYN flood disrupts
- [ ] Differentiate full packet capture from NetFlow and state the trade-offs
- [ ] Identify all six TCP flags, their codes, and their security significance
- [ ] Describe the traffic signature of five scan types from Section 2.2
- [ ] Complete the attack-to-traffic pattern table (Section 4.1) from memory
- [ ] Explain beaconing detection indicators
- [ ] List DNS tunneling indicators
- [ ] Distinguish NIDS from NIPS on placement, action, and failure impact
- [ ] List three detection methods used by IDS/IPS with strengths and weaknesses
- [ ] Explain what remains visible in encrypted traffic and how JA3 helps
- [ ] Review all eight exam tips
- [ ] Complete the Module 05 Lab
- [ ] Complete the Module 05 Quiz
- [ ] Post initial response to the Module 05 Discussion board by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

**1. Wireshark — Sample Capture Files (Wireshark Wiki)**
<https://wiki.wireshark.org/SampleCaptures>
A large collection of real-world and educational PCAP files covering protocols and attack types including port scans, ARP poisoning, malware traffic, and protocol anomalies. Downloading and opening these captures in Wireshark is the best hands-on way to practice the display filter writing and traffic pattern recognition skills covered in Sections 2 and 3 of this guide.

**2. SANS — Malware Traffic Analysis Practice PCAPs**
<https://www.malware-traffic-analysis.net/>
A practitioner-maintained repository of real malware infection traffic captures used for analyst training. Each entry includes the PCAP, associated IOCs, and a write-up identifying the malware family. Reviewing these captures reinforces C2 beaconing, DNS tunneling, and anomalous traffic pattern identification covered in Section 4.

**3. Suricata — Open-Source IDS/IPS Rule Writing Guide**
<https://docs.suricata.io/en/latest/rules/index.html>
The official Suricata rule documentation, covering rule syntax, options, and writing detection rules for network traffic. Reading through the rule structure examples — especially for content matching, threshold settings, and flowbits — directly reinforces the IDS/IPS detection and rule design concepts in Sections 5 and 6 of this guide.
