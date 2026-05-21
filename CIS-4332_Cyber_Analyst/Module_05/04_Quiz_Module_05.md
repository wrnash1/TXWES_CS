# Quiz: Module 05 - Network Traffic Analysis and Packet Inspection
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which protocol is the standard carrier for exchanging structured cyber threat intelligence data over HTTP?
*   A) STIX
*   B) TAXII
*   C) JSON-RPC
*   D) Syslog
*   **Correct Answer:** B) TAXII (Trusted Automated Exchange of Intelligence Information) is the transport mechanism. STIX is the language format.
*   **Distractor Analysis:**
    *   *Why correct:* TAXII is the HTTPS-based server/client protocol that carries STIX-formatted intelligence objects between organizations and platforms.
    *   STIX defines the data schema and object types; it does not transport data. JSON-RPC and Syslog are unrelated transport protocols not used for CTI exchange.

---

**Question 2**
In network traffic analysis, which of the following most accurately defines the **Cyber Kill Chain**?
*   A) A seven-stage model describing the phases of a targeted cyberattack from reconnaissance through actions on objectives, used to determine where in an attack lifecycle an observed behavior falls
*   B) A vendor-specific firewall rule format that automatically blocks traffic matching known attack signatures at each network perimeter layer
*   C) A cryptographic chaining mechanism used in TLS to ensure forward secrecy across multiple network sessions
*   D) A log correlation technique that links network flow records from multiple sensors into a single unified event timeline
*   **Correct Answer:** A) A seven-stage model describing the phases of a targeted cyberattack from reconnaissance through actions on objectives, used to determine where in an attack lifecycle an observed behavior falls.
*   **Distractor Analysis:**
    *   *Why A is correct:* The Lockheed Martin Cyber Kill Chain (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, C2, Actions on Objectives) gives analysts a framework to classify observed attacker behaviors and identify at which stage detection or disruption can occur.
    *   *Why B is incorrect:* Firewall signature blocking describes IPS functionality, not a kill chain model.
    *   *Why C is incorrect:* TLS forward secrecy is a cryptographic property; the Cyber Kill Chain has nothing to do with encryption key management.
    *   *Why D is incorrect:* Linking flow records is a SIEM correlation function, not what the Cyber Kill Chain describes.

---

**Question 3**
A network analyst opens a PCAP file and observes outbound TCP connections from an internal host to an external IP every 60 seconds, each carrying only 200 bytes of encrypted payload. Which threat behavior does this pattern most strongly indicate?
*   A) A port scan — the attacker is enumerating open services across the external IP range
*   B) C2 beaconing — the compromised host is maintaining regular check-in communications with a command-and-control server
*   C) DNS tunneling — the attacker is exfiltrating data by encoding it in DNS query strings
*   D) ARP poisoning — the attacker is redirecting internal traffic through a rogue host on the LAN
*   **Correct Answer:** B) C2 beaconing — the compromised host is maintaining regular check-in communications with a command-and-control server.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Port scanning produces many short-lived connections to many destination ports or hosts in rapid succession, not regular fixed-interval connections to a single IP.
    *   *Why B is correct:* Regular interval (jitter-free or low-jitter), small fixed payload size, single external destination, and encryption are the hallmark characteristics of C2 beacon traffic — the compromised host is "phoning home" for instructions.
    *   *Why C is incorrect:* DNS tunneling uses DNS query and response packets as the carrier; the scenario describes TCP connections, not DNS traffic.
    *   *Why D is incorrect:* ARP poisoning is a LAN-layer (Layer 2) attack that redirects traffic within a local subnet; it does not produce regular outbound TCP connections to external IPs.

---

**Question 4**
An analyst wants to filter a PCAP in Wireshark to display only packets where a TCP three-way handshake SYN is sent but no ACK has been received — a pattern associated with SYN scanning. Which Wireshark display filter is correct?
*   A) `tcp.flags == 0x002` — matches packets with only the SYN flag set
*   B) `tcp.analysis.retransmission` — matches TCP retransmission events
*   C) `ip.proto == 6` — matches all IPv4 TCP traffic regardless of flag state
*   D) `dns.qry.name` — matches DNS query name fields in DNS packets
*   **Correct Answer:** A) `tcp.flags == 0x002` — matches packets with only the SYN flag set.
*   **Distractor Analysis:**
    *   *Why A is correct:* The TCP SYN flag is bit 1 in the flags field, giving a hex value of 0x002. Filtering for this value isolates packets where only the SYN is set — the first step of a handshake or a SYN scan probe — which is the pattern being investigated.
    *   *Why B is incorrect:* `tcp.analysis.retransmission` filters for Wireshark-annotated retransmissions due to packet loss; it is unrelated to SYN scan detection.
    *   *Why C is incorrect:* `ip.proto == 6` returns all TCP packets regardless of flag state, making it too broad to isolate SYN-only packets.
    *   *Why D is incorrect:* `dns.qry.name` matches DNS protocol query fields; TCP SYN packets are not DNS traffic.

---

**Question 5**
An organization wants to detect outbound connections to known malicious IP addresses identified in a current threat intelligence feed. Which two controls together best implement this capability?
*   A) Enable full-disk encryption on all endpoints and require VPN for remote access
*   B) Ingest the threat intelligence feed IOCs into the SIEM and create a correlation rule that alerts when any internal host connects to a listed malicious IP
*   C) Deploy a web application firewall and enforce TLS 1.3 for all internal web traffic
*   D) Require multi-factor authentication for all administrative accounts and disable shared local administrator passwords
*   **Correct Answer:** B) Ingest the threat intelligence feed IOCs into the SIEM and create a correlation rule that alerts when any internal host connects to a listed malicious IP.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Disk encryption and VPN protect data confidentiality and remote access security; neither compares live network connections against a threat intelligence IP list.
    *   *Why B is correct:* Loading known-malicious IP indicators into the SIEM enables real-time matching of outbound network connections against the threat feed, and the correlation rule generates an alert when a match occurs — directly addressing the detection requirement.
    *   *Why C is incorrect:* A WAF protects inbound web application traffic; it does not monitor or alert on outbound connections to arbitrary external IPs.
    *   *Why D is incorrect:* MFA and local admin password controls address credential security; they have no effect on detecting outbound connections to malicious IPs.

