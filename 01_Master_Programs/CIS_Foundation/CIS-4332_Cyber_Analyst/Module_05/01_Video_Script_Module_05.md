# Video Script: Module 05 - Network Traffic Analysis and Packet Inspection

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20-24 minutes

## CySA+ CS0-003 Domain Alignment: Domain 1 - Security Operations (33%)

---

### [00:00 - 01:30] Introduction

Professor Nash on camera. Title card: Module 05 — Network Traffic Analysis and Packet Inspection.

"Welcome to Module 05. If log analysis is reading what happened in a system's journal, then network traffic analysis is watching what actually crossed the wire. These two disciplines complement each other — logs tell you what the system reported; network data tells you what actually traveled across the network.

In this module we cover the TCP/IP model and key protocols, the tools used for traffic capture and analysis, how to interpret NetFlow and packet data, and the most important traffic patterns that indicate malicious activity. This content maps to Domain 1 of the CySA+ exam and requires a solid foundation in networking fundamentals. Let's get into it."

---

### [01:30 - 05:00] TCP/IP Protocol Stack Review

"Before we analyze traffic, we need to review the TCP/IP model, because every traffic analysis technique maps to a specific layer.

The TCP/IP model has four layers. The Network Access layer — sometimes called the Link layer — handles physical addressing, Ethernet frames, and local network delivery. The Internet layer handles IP addressing and routing between networks. Key protocols here are IPv4, IPv6, ICMP, and ARP.

The Transport layer handles end-to-end communication and session management. TCP provides reliable, ordered, connection-oriented communication with three-way handshake (SYN, SYN-ACK, ACK). UDP provides fast, connectionless communication with no reliability guarantees. TCP is used for applications where completeness matters — HTTP, SMTP, SSH. UDP is used where speed matters — DNS queries, DHCP, VoIP, streaming.

The Application layer is where end-user protocols live: HTTP, HTTPS, DNS, FTP, SSH, SMTP, and hundreds of others.

Understanding which layer a protocol operates at tells you what a traffic analyzer can see and what it cannot. An IDS operating at the network layer can see IP headers. One operating at the application layer can see HTTP requests and response bodies.

Key ports to memorize for the exam: FTP 21, SSH 22, Telnet 23, SMTP 25, DNS 53, HTTP 80, HTTPS 443, IMAP 143, LDAP 389, SMTPS 465, HTTPS Alternate 8443, RDP 3389. Non-standard port usage is a significant indicator — malware communicating on port 4444 or 8080 instead of 443 is a red flag."

---

### [05:00 - 09:00] Network Traffic Capture and Analysis Tools

"There are two fundamental approaches to capturing and analyzing network data: full packet capture and flow data analysis.

Full packet capture uses tools like Wireshark, tcpdump, or network TAPs to capture every byte of every packet on a network segment. This gives you complete visibility — you can see every payload, every header, reconstruct sessions, and extract files transferred over unencrypted protocols. The limitation is storage. A busy network generates terabytes of packet data per day. Full packet capture is usually reserved for targeted segments or triggered captures during incident investigation.

Flow data — also called NetFlow, sFlow, or IPFIX depending on the vendor — captures metadata about network connections rather than the full payload. Flow records contain source IP, destination IP, source port, destination port, protocol, byte count, packet count, start time, and end time. Flow data is much smaller than full packet data — typically 1/100th or less of the storage requirement — and can be collected at scale across an entire enterprise network.

The tradeoff: flow data cannot show you what was in the payload of an encrypted connection. Full packet capture can reconstruct the session content for unencrypted traffic but requires enormous storage and cannot decrypt TLS.

For most enterprise SOCs, the practical approach is: flow data for all network segments continuously, plus targeted full packet capture on high-value segments (DMZ, database tier) and triggered captures when an investigation warrants it.

Wireshark is the standard tool for packet analysis and appears on the CySA+ exam by name. Key Wireshark skills: display filters to isolate specific traffic, follow stream to reconstruct a TCP session, statistics menus for traffic summary, and the ability to read a packet dissection showing each protocol layer's fields."

[SHOW SCREEN: Wireshark interface with labeled panels: top panel showing packet list with columns for No., Time, Source, Destination, Protocol, Length, Info. Middle panel showing selected packet decomposition with Ethernet frame, IP header, TCP header, and HTTP payload layers expanded. Bottom panel showing hex dump. Display filter bar showing "ip.addr==203.0.113.47 and tcp.port==80" entered.]

---

### [09:00 - 13:00] Interpreting TCP Flags and Packet Behavior

"TCP flag analysis is a critical skill for network traffic investigation. The six TCP flags you need to know are:

SYN — Synchronize. Initiates a connection. A SYN packet without a corresponding SYN-ACK may indicate a port scan or a half-open scan.

SYN-ACK — Server acknowledges the client's SYN and sends its own. Part of the normal three-way handshake.

ACK — Acknowledge. Confirms receipt of data. Present in most packets after the handshake is complete.

FIN — Finish. Gracefully terminates a connection from one side.

RST — Reset. Abruptly terminates a connection, often sent by the server to indicate a port is closed or access is refused.

PSH — Push. Tells the receiving TCP stack to pass data to the application immediately.

Attack signatures in TCP flags:

A SYN flood attack involves sending thousands of SYN packets without completing the handshake. The target system allocates memory for each half-open connection, eventually exhausting resources. This is a Denial of Service attack targeting Availability.

A stealth scan (Nmap SYN scan) sends SYN packets and waits for RST (port closed) or SYN-ACK (port open) responses without completing the handshake. It is quieter than a full connect scan but still detectable by intrusion detection systems.

An XMAS scan sends packets with FIN, URG, and PSH flags set simultaneously — technically invalid per RFC 793. This technique can bypass some older packet filter implementations that only watch for SYN packets.

ICMP is used for network diagnostics. ICMP echo requests and replies are ping. ICMP type 3 (Destination Unreachable) fires when a port is closed. Excessive ICMP traffic, especially ICMP with unusually large payloads, can indicate reconnaissance or data exfiltration over covert channels."

---

### [13:00 - 16:30] Key Traffic Patterns and Malicious Indicators

"Let me walk through the traffic patterns that indicate specific attack types. These patterns appear in CySA+ scenario questions where you are given traffic data and asked to identify the attack.

Pattern 1: Port scanning. A single external IP generating RST responses from dozens to hundreds of different destination ports on one target, or SYN packets to many ports in rapid sequence. Port scanners like Nmap generate distinctive traffic signatures.

Pattern 2: C2 beaconing. As we discussed in Module 04, regular outbound connections at consistent intervals to the same external IP — especially over HTTP, HTTPS, or DNS. The consistency is the tell.

Pattern 3: DNS tunneling. An attacker using DNS queries to exfiltrate data or maintain C2 communication by encoding data in DNS query subdomains. Indicators include extremely long DNS query names, high volume of TXT or NULL record queries, and queries to unusual or newly registered domains. DNS tunneling traffic looks like DNS traffic but the query content is abnormal.

Pattern 4: Data exfiltration. Large outbound transfers, especially over HTTPS POST requests (where payload cannot be inspected) or to cloud storage services. Flow data shows large byte counts outbound; full packet capture shows the volume but not the content if encrypted.

Pattern 5: Lateral movement via SMB. SMB connections (TCP 445) from a workstation to other workstations — not the file server. Workstation-to-workstation SMB is unusual in most environments and indicates lateral movement attempts using tools like PsExec or ransomware spreading.

Pattern 6: Abnormal DNS queries. A host querying thousands of unique domains in a short period — possible Domain Generation Algorithm malware trying to reach its active C2 server by cycling through algorithmically generated domain names."

[SHOW DIAGRAM: Network diagram showing: External attacker IP on left with arrows to DMZ server. Four labeled traffic pattern examples positioned around the diagram: SYN flood showing many SYN arrows with no ACK responses; Beaconing showing regular timed arrows from internal host to external IP; DNS tunneling showing DNS queries with encoded data in subdomains; SMB lateral movement showing workstation-to-workstation port 445 connections.]

---

### [16:30 - 19:30] Intrusion Detection and Prevention Systems

"Network traffic analysis in a SOC relies on two categories of sensors: Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS).

A Network IDS, or NIDS, monitors network traffic and generates alerts when it detects signatures matching known attacks or anomalies. It is passive — it watches traffic on a SPAN port or network TAP but does not block anything. NIDS is valuable because it generates no latency and cannot be used as a chokepoint for denial of service. The limitation is that it detects but cannot block.

A Network IPS, or NIPS, is inline — all traffic passes through it. It can detect AND block malicious traffic in real time. The tradeoff is that the IPS is a single point of failure: if it crashes or experiences high load, it can disrupt network traffic. IPS tuning is critical — false positives that trigger blocks cause legitimate service disruptions.

Detection methods used by IDS and IPS:

Signature-based detection compares traffic against a database of known attack signatures. High precision for known attacks, zero visibility for novel unknown attacks.

Anomaly-based detection builds a baseline of normal traffic and alerts on deviations. It can detect zero-day attacks and novel techniques, but it requires a good baseline and generates more false positives.

Behavioral detection (sometimes called heuristic detection) looks for behavioral patterns characteristic of attacks — beaconing regularity, scanning velocity, lateral movement patterns — rather than specific byte sequences.

Exam tip: NIDS alerts but does not block. NIPS is inline and can block. If an exam question describes a device that monitors traffic and generates alerts on a SPAN port, it is a NIDS. If it is inline and prevents traffic, it is a NIPS."

---

### [19:30 - 22:00] Encrypted Traffic Challenges

"One of the most significant challenges in modern network traffic analysis is encryption. The majority of internet traffic today is encrypted — HTTPS accounts for most web traffic, and many malware C2 channels now use TLS to blend in.

This means full packet capture cannot show you the payload of most traffic. What can you still see?

Connection metadata: source and destination IP, ports, timestamps, and data volume are all visible in flow data even for encrypted connections.

TLS handshake metadata: the Client Hello and Server Hello of a TLS handshake occur in the clear before encryption begins. This reveals the TLS version, cipher suites offered, and — critically — the Server Name Indication (SNI) field, which shows the hostname the client is trying to reach. This is invaluable for detecting malicious domains even when the payload is encrypted.

JA3 and JA3S fingerprints: tools that hash the TLS Client Hello and Server Hello parameters to create fingerprints of TLS clients and servers. Known malware families often have distinctive JA3 fingerprints because they use specific TLS configurations.

Behavioral indicators: even with payload encryption, beaconing regularity, transfer volumes, and connection timing remain visible in flow data and provide strong indicators.

SSL inspection (TLS decryption): some enterprise security architectures use man-in-the-middle SSL inspection to decrypt, inspect, and re-encrypt traffic. This provides full visibility but introduces privacy implications, compliance considerations, and introduces a new attack surface."

---

### [22:00 - 24:00] Module Summary and Lab Preview

"Let's summarize Module 05.

The TCP/IP model has four layers. TCP provides reliable connection-oriented communication; UDP provides fast connectionless communication. Know key port numbers.

Full packet capture provides complete visibility; flow data provides scalable metadata. Both have important roles.

Key TCP flags: SYN, SYN-ACK, ACK, FIN, RST, PSH. SYN flood = DoS. SYN scan = reconnaissance.

Key malicious traffic patterns: port scanning, C2 beaconing, DNS tunneling, data exfiltration, SMB lateral movement, DGA traffic.

NIDS alerts but does not block (passive, SPAN port). NIPS blocks inline (active, in-band).

Detection methods: signature-based (known threats), anomaly-based (baseline deviation), behavioral (pattern detection).

Encrypted traffic is analyzed through metadata, TLS SNI, JA3 fingerprinting, and flow behavior.

In the Module 05 lab, you will analyze network traffic scenarios and identify suspicious patterns using flow data and packet-level detail. Read the Reading Guide for the protocol reference tables and traffic pattern descriptions before starting the lab.

Study resources: professormesser.com and comptia.org. See you in Module 06."

---

End of Module 05 Video Script

Study Resources: comptia.org | professormesser.com
