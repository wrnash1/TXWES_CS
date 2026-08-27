# Quiz: Module 05 - Network Traffic Analysis and Packet Inspection

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer.

---

## Question 1

An analyst reviews network flow data and observes an internal host making outbound TCP connections to the same external IP address on port 443 every 300 seconds for 6 hours, with consistent byte counts of approximately 1,200-1,250 bytes per session. What does this pattern most likely indicate?

- A) A legitimate HTTPS browsing session with a web application that refreshes content automatically
- B) A software update agent checking for patches on a regular schedule
- C) Beaconing behavior consistent with malware communicating with a command-and-control server
- D) A VPN client maintaining keepalive packets to prevent connection timeout

Correct Answer: C

Distractor Analysis:

- A is incorrect. Human-driven web browsing is irregular — refresh intervals vary with user activity. Precise 300-second intervals with consistent byte counts are characteristic of automated, programmatic communication, not user-driven browsing.
- B is incorrect. Software update agents typically check on daily or weekly schedules, not every 5 minutes for 6 hours. They also connect to known vendor domains, not arbitrary external IPs, and their intervals are not this precise.
- C is correct. Malware C2 communication uses sleep timers between check-ins, producing highly regular intervals. Consistent 300-second intervals with consistent session sizes over 6 hours is a textbook beaconing signature, mapping to ATT&CK T1071 Command and Control.
- D is incorrect. VPN keepalive traffic uses very small packets at irregular intervals and would not generate 1,200-byte sessions at precisely regular times.

---

## Question 2

A network analyst captures traffic and observes thousands of SYN packets sent from a single external IP address to hundreds of different destination ports on one target server within 60 seconds. Most responses from the server are RST packets, with a few SYN-ACK responses. Which action from the analyst side is most accurate about what is happening?

- A) The target server is experiencing a SYN flood denial-of-service attack
- B) The source IP is conducting a port scan to identify open services on the target
- C) The target server is sending RST packets to terminate established connections
- D) A network device is performing an ARP sweep to resolve MAC addresses

Correct Answer: B

Distractor Analysis:

- A is incorrect. A SYN flood sends SYN packets to overwhelm a single port (or a small set of ports) with the goal of exhausting the server's half-open connection queue. The distinguishing feature here is that the SYNs are targeting hundreds of different ports — characteristic of port scanning, not flooding.
- B is correct. Sending SYN packets to sequential or varied ports and observing whether the response is SYN-ACK (port open) or RST (port closed) is the signature of a TCP SYN (half-open) port scan. The attacker is mapping the server's attack surface.
- C is incorrect. The RST packets are coming from the server, not the external IP. The server is responding to SYN probes for closed ports with RST — normal behavior when a port is not listening.
- D is incorrect. ARP sweeps use ARP request frames at Layer 2 to resolve IP-to-MAC mappings. They do not use TCP SYN packets.

---

## Question 3

Which of the following is the most significant limitation of using full packet capture for continuous, enterprise-wide network monitoring?

- A) Full packet capture cannot detect malicious traffic because it only records packet headers
- B) Full packet capture cannot be used on encrypted HTTPS traffic without SSL inspection
- C) Full packet capture generates extremely large data volumes that make continuous enterprise-wide storage impractical
- D) Full packet capture is illegal in most jurisdictions without explicit employee consent

Correct Answer: C

Distractor Analysis:

- A is incorrect. Full packet capture records complete packets including payloads, not just headers. It is the most comprehensive traffic collection method available.
- B is incorrect. While it is true that full packet capture cannot decrypt TLS payload without SSL inspection, this is a limitation of visibility into encrypted content — not the reason enterprise-wide deployment is impractical.
- C is correct. A busy enterprise network can generate terabytes of packet data per day. Storing full packet captures at scale across all network segments continuously is prohibitively expensive and operationally complex. This is why NetFlow (metadata only) is used for enterprise-wide continuous monitoring, with full packet capture reserved for targeted segments or triggered investigations.
- D is incorrect. Passive network monitoring of corporate network traffic by the network owner is generally permitted within an organization's own network, particularly with appropriate acceptable use policies.

---

## Question 4

A security analyst is analyzing TLS traffic from a workstation and extracts a JA3 fingerprint from the TLS Client Hello. The threat intelligence platform returns a match indicating that this JA3 hash is associated with a known remote access trojan. The destination is an IP address on port 443. Which statement best describes the significance of this finding?

- A) The finding is inconclusive because HTTPS traffic on port 443 is encrypted and the payload cannot be verified
- B) The JA3 match indicates that the TLS client configuration on this workstation matches a known malware family, making this a high-confidence C2 detection candidate
- C) The finding is a false positive because JA3 hashes only apply to server-side certificates, not client connections
- D) The analyst should ignore this alert because port 443 is normal HTTPS traffic that does not warrant investigation

Correct Answer: B

Distractor Analysis:

- A is incorrect. While the payload is encrypted, the JA3 fingerprint does not require payload decryption — it is derived from the TLS Client Hello, which is transmitted in the clear before encryption begins. A TI match is actionable regardless of payload visibility.
- B is correct. JA3 fingerprints the TLS Client Hello parameters. Known malware families often use specific, distinctive TLS configurations. A JA3 match against a known RAT fingerprint is a high-confidence signal that the workstation is running malware that matches that family's TLS behavior, even without payload decryption.
- C is incorrect. JA3 fingerprints the client (workstation) TLS Client Hello. JA3S fingerprints the server response. Both are client/server-side respectively; neither is limited to certificates.
- D is incorrect. The port number alone does not determine whether traffic is benign. Malware specifically uses port 443 to blend into legitimate web traffic. The JA3 match provides a behavioral fingerprint that distinguishes malicious TLS from legitimate browsing.

---

## Question 5

An analyst wants to monitor all network traffic to and from the organization's DMZ without affecting network availability. The DMZ handles 25 Gbps of peak traffic. Which deployment option is most appropriate?

- A) Deploy a NIPS inline between the internet router and the DMZ firewall
- B) Deploy a NIDS using a SPAN port on the DMZ switch to mirror traffic to a monitoring interface
- C) Deploy a host-based IPS on each DMZ server to monitor their individual traffic
- D) Deploy packet-filtering rules on the DMZ firewall to log all allowed connections

Correct Answer: B

Distractor Analysis:

- A is incorrect. A NIPS inline between the router and firewall would process all 25 Gbps of traffic. At this volume, the NIPS could introduce latency or become a bottleneck. More critically, if the NIPS fails, it would disrupt all DMZ connectivity — not acceptable for a high-availability requirement.
- B is correct. A NIDS deployed on a SPAN port (or network TAP) receives a mirror of all DMZ traffic but does not sit in the traffic path. If the NIDS fails, it simply stops monitoring — network availability is not affected. This is the correct choice when monitoring without impact to availability is the requirement.
- C is incorrect. Host-based IPS monitors traffic at the individual host level. It would miss traffic between DMZ hosts and would not provide the comprehensive segment-level visibility the question requires.
- D is incorrect. Firewall connection logs record allowed and denied connections but do not capture packet content or provide the deep traffic analysis capabilities of an IDS.

---

## Question 6

An analyst notices that an internal DNS server is generating thousands of DNS NXDOMAIN (non-existent domain) responses per minute. Most of the queries are for domains with names that appear to be random strings of 12-20 characters followed by common TLDs. What does this pattern most likely indicate?

- A) The DNS server is under a DNS amplification DDoS attack
- B) Malware on an internal host is using a Domain Generation Algorithm to locate its active C2 server
- C) A legitimate application is performing bulk DNS pre-resolution of a large URL list
- D) An administrator is running a DNS zone transfer, which produces NXDOMAIN responses for missing records

Correct Answer: B

Distractor Analysis:

- A is incorrect. A DNS amplification attack involves an external attacker sending DNS queries with a spoofed victim IP to cause the DNS server to flood the victim with large DNS responses. The pattern here involves queries originating from inside the network, not externally crafted amplification traffic.
- B is correct. Domain Generation Algorithms (DGA) are a technique used by malware to generate many potential C2 domain names. The malware queries each one; most return NXDOMAIN (the domain is not registered or active). When the attacker registers or activates one of these domains, the malware connects. High-volume NXDOMAIN responses for random-looking domain names is the definitive DGA signature.
- C is incorrect. Bulk DNS pre-resolution would query real domain names from a known URL list, not random-character strings. The randomness of the domain names is the key distinguishing indicator.
- D is incorrect. DNS zone transfers are a server-to-server operation that replicates DNS records. They do not produce the kind of high-volume NXDOMAIN query pattern described.

---

## Question 7

Which TCP flag combination, when observed in a packet to a target system, is technically malformed according to RFC 793 and may be used in certain scan techniques to evade packet filters that only inspect for SYN flags?

- A) SYN + ACK (SYN-ACK — normal handshake response)
- B) FIN + URG + PSH (XMAS scan configuration)
- C) SYN + RST (connection reset during initiation)
- D) FIN + ACK (normal connection close acknowledgement)

Correct Answer: B

Distractor Analysis:

- A is incorrect. SYN-ACK is the standard server response to a client SYN in a normal three-way handshake. It is not malformed and is not a scan technique.
- B is correct. The XMAS scan sets FIN, URG, and PSH flags simultaneously — a combination that is technically invalid per RFC 793 because URG and PSH have no meaning without data. This malformed flag combination can bypass older, stateless packet filters that only watch for SYN flags. RFC-compliant systems respond with RST for closed ports and no response for open ports.
- C is incorrect. SYN+RST is not a defined scan technique and is not a meaningful combination — RST terminates a connection, which contradicts the initiation intent of SYN.
- D is incorrect. FIN+ACK is the standard acknowledgement response to a FIN during graceful connection closure. It is not malformed and is part of the normal TCP connection teardown sequence.

---

## Question 8

An analyst investigates DNS traffic from an internal host and finds the following patterns: queries averaging 847 bytes each, queries including long subdomains that appear to be base64-encoded strings, and all queries directed to a single external domain. What attack technique does this evidence most directly indicate?

- A) Fast-flux DNS — frequently changing IP addresses to evade blocklists
- B) DNS cache poisoning — injecting malicious records into the DNS resolver cache
- C) DNS tunneling — encoding data in DNS queries to exfiltrate information or maintain C2 communication
- D) DNS amplification — using DNS queries to generate large responses for DDoS reflection

Correct Answer: C

Distractor Analysis:

- A is incorrect. Fast-flux DNS involves rapidly changing DNS records to keep malicious infrastructure from being blocked. It does not produce large queries with encoded subdomains.
- B is incorrect. DNS cache poisoning involves injecting forged DNS responses into a resolver's cache. It is an attack against the DNS infrastructure, not a data exfiltration technique, and it does not produce large outbound DNS queries.
- C is correct. DNS tunneling encodes data in DNS query subdomains (base64-encoded content is a classic indicator). Query sizes of 847 bytes are far larger than legitimate DNS queries (typically under 100 bytes). Directing all queries to a single domain is characteristic of communicating with a DNS tunneling server. This maps to ATT&CK T1071.004 (DNS).
- D is incorrect. DNS amplification is an outbound DDoS technique that sends small DNS queries to public resolvers, which respond with large answers directed at a spoofed victim IP. It does not involve large outbound queries from the attacker's network.

---

## Question 9

A SOC analyst is investigating potential lateral movement. NetFlow records show internal workstation 10.0.5.14 connecting to TCP port 445 on internal hosts 10.0.5.20, 10.0.5.21, 10.0.5.22, 10.0.5.23, and 10.0.5.24 in rapid succession over 90 seconds. Which statement most accurately describes the significance of this traffic?

- A) Port 445 is used for HTTPS traffic; this is normal secure web browsing on the internal network
- B) Workstation-to-workstation SMB connections are normal in environments that use mapped network drives
- C) Sequential SMB connections from a single workstation to multiple other workstations in rapid succession is a strong indicator of lateral movement or ransomware propagation
- D) This pattern represents normal Active Directory Group Policy propagation from the domain controller

Correct Answer: C

Distractor Analysis:

- A is incorrect. TCP port 445 is the SMB (Server Message Block) file sharing protocol — not HTTPS. HTTPS uses port 443.
- B is incorrect. Mapped network drives connect from workstations to file servers, not from one workstation to other workstations. Normal SMB traffic from workstations targets designated file servers, not peer workstations.
- C is correct. Workstation-to-workstation SMB connections (port 445) in rapid sequential succession from one source are a strong indicator of either lateral movement using SMB-based tools (PsExec, WMI) or ransomware spreading by scanning adjacent systems. This maps to ATT&CK T1021 Remote Services (SMB/Windows Admin Shares).
- D is incorrect. Group Policy is distributed from domain controllers, not from workstations. GPO traffic uses LDAP, Kerberos, and SMB to DCs — not workstation-to-workstation.

---

## Question 10

Which of the following correctly differentiates signature-based IDS detection from anomaly-based IDS detection?

- A) Signature-based detection requires network access to a threat intelligence cloud; anomaly-based detection works offline
- B) Signature-based detection identifies known attacks with high precision but cannot detect novel unknown threats; anomaly-based detection can detect novel threats but requires an established baseline and generates more false positives
- C) Signature-based detection is only effective at Layer 7 (Application); anomaly-based detection works at all layers equally
- D) Signature-based detection is used only by NIPS; anomaly-based detection is used only by NIDS

Correct Answer: B

Distractor Analysis:

- A is incorrect. Signature-based detection uses a locally stored signature database and does not require real-time cloud connectivity during detection. The database is updated periodically.
- B is correct. Signature-based detection compares traffic against known attack patterns — high precision, low false positives, zero visibility into unknown attacks. Anomaly-based detection compares traffic against an established normal-behavior baseline and alerts on deviations — can detect novel techniques but requires a good baseline and produces more false positives due to baseline drift and legitimate behavioral changes.
- C is incorrect. Both signature-based and anomaly-based detection can operate across network layers. Signature-based detection works at any layer where signatures can be defined; anomaly-based detection can monitor traffic volumes, connection patterns, and behavioral metrics at any layer.
- D is incorrect. Both IDS and IPS systems can use either signature-based or anomaly-based detection. The IDS/IPS distinction is about placement and response action (alert vs. block), not detection method.

---

## Question 11 (5 points)

A Wireshark capture shows a host sending TCP SYN packets to 1,024 consecutive ports on a target IP within 2 seconds, with no three-way handshake completions. Which scan type does this represent and what is its purpose?

- A) Idle scan — used to anonymously map open ports using a zombie host
- B) TCP SYN scan (half-open scan) — used to enumerate open ports by sending SYN packets and observing responses without completing the handshake
- C) UDP scan — used to discover UDP services by sending empty datagrams
- D) XMAS scan — used to evade stateful firewalls by setting URG, PSH, and FIN flags simultaneously

Correct Answer: B

Distractor Analysis:

- A is incorrect. An idle scan uses a third-party "zombie" host to probe the target, making the attacker's IP invisible in the scan traffic. The scenario shows a direct host-to-target SYN flood with no third party.
- B is correct. A TCP SYN scan sends SYN packets to each port. An open port responds with SYN-ACK; the scanner sends RST rather than completing the handshake (making it "half-open"). Closed ports respond RST. Consecutive ports hit in rapid succession with no completed handshakes is the definitive traffic signature.
- C is incorrect. UDP scans send UDP datagrams and look for ICMP Port Unreachable responses to identify closed ports. The captured traffic shows TCP SYN packets, not UDP.
- D is incorrect. An XMAS scan sets the URG, PSH, and FIN flags simultaneously — creating a recognizably abnormal TCP flag combination. The scenario describes SYN-only packets.

---

## Question 12 (5 points)

An analyst reviewing NetFlow data sees a host transmitting 4.2 GB of data outbound to a single external IP over a 20-minute window during business hours. The external IP resolves to a cloud storage provider. What is the most significant security concern this traffic pattern raises?

- A) The host is performing a normal Windows backup to an authorized cloud endpoint
- B) The volume and destination are consistent with data exfiltration — large outbound data transfers to cloud storage are a recognized exfiltration technique (ATT&CK T1567)
- C) The NetFlow data is unreliable for security analysis because it does not contain full packet content
- D) The cloud storage IP should be blocked at the firewall immediately because all external cloud connections are unauthorized

Correct Answer: B

Distractor Analysis:

- A is incorrect. While cloud backups do occur, 4.2 GB in 20 minutes to an unverified external IP during business hours requires investigation. The assumption of legitimacy without verification violates triage principles.
- B is correct. ATT&CK T1567 (Exfiltration Over Web Service) documents the use of cloud storage services for data exfiltration. Large outbound transfers to generic cloud storage providers are a known exfiltration pattern. The analyst should correlate with DLP alerts, endpoint activity, and authorized backup documentation.
- C is incorrect. NetFlow metadata (bytes transferred, duration, source/destination) is highly valuable for behavioral analysis even without full packet content. The 4.2 GB volume itself is the key indicator.
- D is incorrect. Immediately blocking without investigation could disrupt authorized backup operations and violates the triage-before-action principle.

---

## Question 13 (5 points)

Which TCP flag combination in a captured packet header most strongly indicates that a host is conducting an OS fingerprinting or evasion scan designed to elicit abnormal stack responses from the target?

- A) SYN only (S)
- B) SYN-ACK (SA)
- C) All flags set simultaneously (UAPRSF — URG, ACK, PSH, RST, SYN, FIN)
- D) ACK only (A)

Correct Answer: C

Distractor Analysis:

- A is incorrect. SYN-only is the standard first step of a normal TCP connection and of a SYN scan. It is not an abnormal evasion combination.
- B is incorrect. SYN-ACK is the standard server response to a SYN. It indicates a listening service's normal response, not a malformed probe.
- C is correct. Setting all six TCP flags simultaneously (sometimes called a "Christmas tree" or "FULL" packet) is not a valid TCP state in normal communication. This crafted packet is designed to elicit response differences across operating system TCP implementations for fingerprinting purposes, and to potentially evade simple stateless rule-based detection.
- D is incorrect. ACK-only scans are used for firewall rule mapping — they can determine whether a port is filtered. While useful in scanning, ACK-only is not the most evasion-focused combination.

---

## Question 14 (5 points)

An analyst is reviewing DNS logs and observes an internal host making queries for subdomains that follow the pattern: `4a7b2c.exfildata.com`, `e9f1a3.exfildata.com`, `3b8d2f.exfildata.com` — 340 queries in one hour. What attack technique does this most likely represent?

- A) Domain generation algorithm (DGA) traffic
- B) DNS tunneling used for data exfiltration or C2 communication
- C) Normal CDN load balancing using geographically distributed subdomains
- D) DNS cache poisoning attack targeting the internal DNS resolver

Correct Answer: B

Distractor Analysis:

- A is incorrect. DGA traffic also produces high volumes of unusual subdomain queries, but DGA domains are typically random-looking apex domains from different TLDs. Here, all queries are for subdomains under the same apex domain (`exfildata.com`), which is the defining structural characteristic of DNS tunneling.
- B is correct. DNS tunneling encodes data into subdomain labels of DNS queries. The data is sent to an attacker-controlled authoritative name server for `exfildata.com`. The high volume of queries under a single apex domain with hex-encoded subdomain labels is the textbook DNS tunneling signature (ATT&CK T1071.004).
- C is incorrect. CDN load balancing subdomains use human-readable geographic or node identifiers (e.g., `us-east-1.cdn.com`), not random hex strings. Legitimate CDN subdomains do not number in the hundreds per hour from a single client.
- D is incorrect. DNS cache poisoning involves injecting malicious records into a resolver's cache — it does not produce high-volume query traffic from a single internal host.

---

## Question 15 (5 points)

A Wireshark display filter is applied: `tcp.flags.syn == 1 and tcp.flags.ack == 0`. What type of traffic does this filter capture?

- A) Completed TCP connections (both SYN and SYN-ACK present)
- B) Only the initial SYN packet of TCP connection attempts, used to identify connection initiations and potential scanning activity
- C) All TCP traffic regardless of flag state
- D) TCP RST packets indicating rejected or terminated connections

Correct Answer: B

Distractor Analysis:

- A is incorrect. A completed TCP handshake includes SYN (client), SYN-ACK (server), and ACK (client). The filter `tcp.flags.syn == 1 and tcp.flags.ack == 0` specifically excludes the SYN-ACK (which has both SYN and ACK set) by requiring ACK to be 0.
- B is correct. `tcp.flags.syn == 1 and tcp.flags.ack == 0` matches only the initial client SYN packet — the first step of a TCP handshake. Applying this filter and sorting by destination port is a fast way to identify port scanning activity or enumerate which services are being targeted.
- C is incorrect. This filter is specific — it requires SYN=1 and ACK=0. Packets with any other flag combination are excluded.
- D is incorrect. RST packets would be captured by `tcp.flags.reset == 1`. SYN and RST flags are distinct.

---

## Question 16 (5 points)

What is the primary limitation of full packet capture (PCAP) compared to NetFlow analysis for long-term network security monitoring?

- A) PCAP cannot capture encrypted traffic whereas NetFlow can
- B) PCAP is not supported by open-source tools; NetFlow requires expensive commercial hardware
- C) PCAP generates extremely large data volumes that are costly to store for extended periods, whereas NetFlow captures only traffic metadata at a fraction of the storage cost
- D) PCAP is limited to monitoring Layer 3 traffic and cannot inspect application-layer protocols

Correct Answer: C

Distractor Analysis:

- A is incorrect. Both PCAP and NetFlow can capture encrypted traffic. PCAP captures the encrypted payload bytes (though content is unreadable without decryption). NetFlow captures metadata (IPs, ports, volumes) for encrypted sessions as well.
- B is incorrect. PCAP is widely supported by open-source tools (Wireshark, tcpdump, Zeek). NetFlow is supported by both open-source and commercial platforms.
- C is correct. Full packet capture preserves every byte of every packet — generating roughly 80–120 GB per hour on a 1 Gbps link running at moderate utilization. This makes long-term PCAP storage extremely expensive. NetFlow records only session metadata (flow records), which is typically 1/1000th the volume, making it practical for months of retention.
- D is incorrect. PCAP captures packets at all network layers, including complete Layer 7 (application) content, which is one of its primary advantages over flow-only data.

---

## Question 17 (5 points)

A JA3 hash value is extracted from TLS handshake metadata in a network capture. What does this hash represent and how is it used in threat detection?

- A) A hash of the encrypted payload content used to verify file integrity
- B) A fingerprint of the TLS client's negotiation parameters (cipher suites, extensions, elliptic curves) that can identify specific client applications or malware families regardless of encryption
- C) A hash of the SSL/TLS certificate presented by the server, used to detect certificate impersonation
- D) A vendor-specific hash algorithm used only by commercial IDS products

Correct Answer: B

Distractor Analysis:

- A is incorrect. JA3 hashes are derived from TLS handshake parameters (cipher suites offered by the client, supported extensions, elliptic curves), not from encrypted payload content. The payload remains encrypted and unreadable.
- B is correct. JA3 creates a fingerprint of the unique combination of TLS negotiation parameters that a specific application presents during the TLS handshake. Because different client software (browsers, malware, legitimate tools) makes different TLS negotiation choices, JA3 can identify application types even in encrypted traffic — including specific malware C2 clients.
- C is incorrect. Server certificate fingerprinting is a different technique, sometimes called JA3S or handled separately. JA3 (client-side) fingerprints the client's hello message, not the server certificate.
- D is incorrect. JA3 is an open-source community standard, not a proprietary commercial hash. It was developed by Salesforce researchers and is widely implemented in open-source tools including Zeek and Suricata.

---

## Question 18 (5 points)

Which protocol and port combination is associated with the greatest risk when observed as inbound traffic to an internal server that the organization has not intentionally exposed to the internet?

- A) HTTPS on port 443 inbound from external IPs
- B) RDP on port 3389 inbound from any external IP
- C) DNS on port 53 inbound from external recursive resolvers
- D) SMTP on port 25 inbound from mail servers listed in the recipient domain's SPF record

Correct Answer: B

Distractor Analysis:

- A is incorrect. HTTPS on 443 is the expected protocol for public-facing web services. Inbound HTTPS from external IPs is normal for web servers and does not represent the highest unexpected-exposure risk.
- B is correct. RDP on port 3389 exposed to the internet is consistently among the most exploited attack surfaces. It enables full interactive remote desktop access; credential brute force and known RDP vulnerabilities (BlueKeep, DejaBlue) have caused significant breaches. Inbound RDP from the internet on a server not intentionally exposed is a critical finding.
- C is incorrect. Inbound DNS on port 53 from external recursive resolvers is expected behavior for organizations hosting authoritative DNS servers for their domains.
- D is incorrect. Inbound SMTP on port 25 from legitimate external mail servers (verified by SPF) is expected and required for receiving email. SPF verification reduces the risk from unauthorized senders.

---

## Question 19 (5 points)

An analyst reviews NetFlow data and observes an internal host making outbound connections to 14 different external IP addresses on port 6667 over a 2-hour period, with each session lasting approximately 45 minutes. What does this traffic pattern most likely indicate?

- A) The host is performing normal DNS lookups for high-traffic web applications
- B) The host is connected to an IRC-based botnet command-and-control infrastructure
- C) The host is conducting a port scan of external IP addresses using port 6667 as the source port
- D) The host is running a legitimate voice-over-IP application that uses dynamic server IPs

Correct Answer: B

Distractor Analysis:

- A is incorrect. DNS lookups use UDP/TCP port 53, not port 6667, and DNS sessions are measured in milliseconds, not 45-minute persistent connections.
- B is correct. Port 6667 is the default IRC (Internet Relay Chat) port. IRC-based botnets use IRC channels as C2 infrastructure. An internal host maintaining long-duration IRC sessions to multiple external IPs over hours is a textbook IRC botnet infection indicator (ATT&CK T1071.003).
- C is incorrect. In a port scan, the source port would be ephemeral (randomly assigned above 1024). Connecting to port 6667 as the destination indicates the host is connecting to IRC servers, not scanning using that port as a source.
- D is incorrect. Legitimate VoIP applications (SIP, WebRTC) use specific protocols on well-documented ports. Port 6667 is not used by any mainstream VoIP application.

---

## Question 20 (5 points)

When an analyst places a NIDS sensor in "tap" mode (passive, out-of-band) versus inline mode, what is the primary operational difference?

- A) Tap mode can block malicious traffic in real time; inline mode can only generate alerts
- B) Tap mode receives a copy of traffic for analysis only and cannot block anything; inline mode sits in the traffic path and can block malicious packets in real time but introduces latency and a single point of failure risk
- C) Tap mode requires more processing power than inline mode because it must inspect all traffic simultaneously
- D) Tap mode is only suitable for encrypted traffic inspection; inline mode works on unencrypted traffic only

Correct Answer: B

Distractor Analysis:

- A is incorrect. This reverses the operational characteristics. Tap mode is passive — it can only alert, never block. Inline mode (used by NIPS) can actively block or drop malicious traffic.
- B is correct. Tap mode places the sensor out-of-band — it receives a mirrored copy of traffic and generates alerts but cannot modify or block traffic. Inline mode places the sensor in the traffic path, enabling real-time blocking but introducing latency into traffic flow and creating a chokepoint that could become a single point of failure if the device fails.
- C is incorrect. Processing requirements depend on traffic volume and inspection depth, not placement mode. Inline sensors may actually have stricter latency requirements than tap sensors.
- D is incorrect. Both tap and inline sensors can inspect encrypted or unencrypted traffic, subject to their decryption capabilities. Placement mode is independent of protocol support.
