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
