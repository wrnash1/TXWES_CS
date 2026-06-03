# Quiz: Module 08 — Network Security Concepts

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

Instructions: Select the best answer for each question. Each question is worth 10 points (100 points total).

---

### Question 1

A company's e-commerce database server stores customer payment card information. The security team implements AES-256 encryption for all data transmitted between the web application and the database server. Which component of the CIA triad does this encryption primarily address?

A) Availability — encryption ensures the database server remains online and accessible during high-traffic periods.

B) Integrity — AES-256 encryption creates a cryptographic hash of all transmitted data that detects any modification in transit.

C) Confidentiality — AES-256 encryption ensures that payment card data is unreadable to any party that intercepts the traffic without the decryption key.

D) Authentication — AES-256 verifies the identity of the database server before the web application is permitted to connect.

- Correct Answer: C
- Distractor Analysis:
  - Why A is incorrect: Encryption does not affect server uptime or availability. Availability is protected by redundancy, load balancing, and DDoS mitigation — not encryption.
  - Why B is incorrect: AES-256 is a symmetric encryption algorithm, not a hashing algorithm. Integrity is protected by hashing (SHA-256, HMAC) and digital signatures. Encryption provides confidentiality; it does not produce a hash for tamper detection.
  - Why C is correct: Confidentiality means data is readable only by authorized parties. AES-256 encryption ensures that even if an attacker intercepts the data stream between the web app and database, the intercepted ciphertext is unreadable without the encryption key.
  - Why D is incorrect: Authentication (verifying identity) is provided by certificates, passwords, tokens, and MFA — not by the encryption algorithm itself. AES-256 is a symmetric cipher used for data confidentiality, not identity verification.

---

### Question 2

A network administrator is reviewing firewall logs and notices that inbound TCP packets are arriving on port 443 with the ACK flag set but no corresponding SYN packet in the logs. The firewall permits these packets because the inbound policy allows TCP port 443 from any source. What type of firewall is most likely in use, and what firewall type would prevent this anomaly?

A) The firewall is stateful; replacing it with a stateless packet filter would block unsolicited ACK packets.

B) The firewall is stateless (packet filter); it permits the ACK packets because it evaluates each packet in isolation without tracking whether a connection was established. A stateful firewall would block these because no corresponding SYN is in the state table.

C) The firewall is a NGFW; the ACK-only packets are passing because deep packet inspection has not been enabled on port 443.

D) The firewall is stateless; replacing it with a honeypot would redirect these anomalous ACK packets to a decoy server.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: This has the technology backward. A stateless firewall is the one that permits packets without state context. A stateful firewall is more secure, not less. Replacing stateful with stateless would make the problem worse.
  - Why B is correct: A stateless (packet filter) firewall evaluates each packet independently. An inbound rule permitting TCP/443 will match any packet with destination port 443 — including unsolicited ACK packets that are not part of a legitimate connection. A stateful firewall maintains a state table and would only permit inbound ACK packets if a corresponding outbound SYN was recorded, effectively blocking the anomalous traffic.
  - Why C is incorrect: NGFWs include stateful inspection as a baseline — they would not permit unsolicited ACK packets any more than a standard stateful firewall. DPI is for application-layer visibility, not basic connection state tracking.
  - Why D is incorrect: A honeypot is a decoy detection tool, not a firewall replacement. It cannot apply permit/deny rules or redirect traffic based on TCP flag anomalies.

---

### Question 3

A security analyst detects that a monitoring sensor on a SPAN port is generating alerts about suspicious traffic patterns on the network but is not stopping the malicious traffic. After reviewing the configuration, the analyst confirms the sensor receives a copy of all traffic and logs alerts for matched signatures. Which technology is this, and what change would allow it to actively block the detected traffic?

A) This is an IPS in alert-only mode; changing the action to "block" in the IPS policy will enable active blocking.

B) This is an IDS deployed via a SPAN port; to actively block traffic the sensor must be repositioned inline in the traffic path and reconfigured as an IPS.

C) This is a stateless firewall; adding a stateful inspection engine will enable the firewall to detect and block the traffic pattern.

D) This is a NAC sensor in post-admission mode; switching to pre-admission mode will quarantine the offending host before it can communicate.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: A sensor receiving traffic via a SPAN port cannot block traffic regardless of policy configuration. SPAN ports receive a read-only copy of traffic — the sensor has no ability to drop or modify packets in the actual traffic path. Changing the action to "block" has no effect on a SPAN-deployed sensor.
  - Why B is correct: The description precisely matches an IDS: SPAN port deployment, receives a copy of traffic, generates signature-based alerts, does not block. To enable active blocking, the device must be repositioned inline so all traffic physically passes through it, and it must be reconfigured as an IPS with prevention actions enabled.
  - Why C is incorrect: The description does not match a firewall. Firewalls apply permit/deny rules at the network perimeter; they do not receive SPAN copies and do not generate alerts about traffic pattern signatures in the manner described.
  - Why D is incorrect: NAC sensors assess device compliance posture before or after admission — they do not analyze network traffic signatures in real time via SPAN ports. The described behavior is specific to IDS/IPS, not NAC.

---

### Question 4

A company places its public web server in a DMZ using a two-firewall design. The outer firewall permits inbound TCP port 80 and 443 from the internet to the web server. The inner firewall permits only TCP port 3306 from the web server to the internal database server. An attacker successfully exploits a vulnerability in the web server and gains full control of it. What can the attacker access from the compromised web server?

A) The attacker can access any internal host because the web server is fully trusted once it is inside the network perimeter.

B) The attacker can access the internal database server on TCP port 3306 only; all other traffic from the compromised web server to the internal LAN is blocked by the inner firewall.

C) The attacker can access all services on the internal database server because the inner firewall permits the web server's IP address and all ports once a connection is established.

D) The attacker cannot access anything because the outer firewall blocks all outbound traffic from the DMZ.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: The entire purpose of the two-firewall DMZ design is to prevent a compromised DMZ server from reaching the internal network freely. The inner firewall enforces strict rules on DMZ-to-LAN traffic regardless of the DMZ server's compromise status.
  - Why B is correct: The inner firewall permits only TCP 3306 from the web server to the database server. Even with full control of the web server, the attacker can only reach the database on that specific port. All other connections from the DMZ to the internal LAN are blocked by the inner firewall.
  - Why C is incorrect: The inner firewall applies rules based on source IP and destination port. Permitting the web server's IP on port 3306 does not open all ports — the rule is specific to port 3306 only.
  - Why D is incorrect: The outer firewall controls internet-to-DMZ traffic, not DMZ-to-internal traffic. The inner firewall controls DMZ-to-LAN traffic. The outer firewall does not block all DMZ outbound traffic — that would prevent the web server from reaching the database and functioning at all.

---

### Question 5

A network engineer observes 800 Gbps of inbound traffic arriving from tens of thousands of distinct source IP addresses spread across multiple continents. The traffic consists entirely of TCP SYN packets destined for the company's public web server. The web server is unresponsive to legitimate users. Which attack type is this, and what is the most effective enterprise mitigation strategy?

A) This is a DoS TCP SYN flood from a single attacker; the most effective mitigation is to block the attacking IP address at the perimeter firewall.

B) This is a DDoS attack using a botnet; the most effective mitigation is to engage an upstream traffic scrubbing service that absorbs the attack traffic at the provider's distributed network before it reaches the company's infrastructure.

C) This is ARP poisoning; the most effective mitigation is to enable Dynamic ARP Inspection on all access layer switches.

D) This is a DNS poisoning attack; the most effective mitigation is to enable DNSSEC on the company's authoritative DNS servers.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: Traffic from tens of thousands of distinct IP addresses across multiple continents is a distributed attack, not a single-source DoS. There is no single IP to block. Blocking individual source IPs in a DDoS botnet is ineffective — the attacker simply uses other bots.
  - Why B is correct: The described characteristics match DDoS precisely: massive volume, distributed sources across many geographies, botnet-scale traffic. Upstream scrubbing services (Cloudflare, Akamai Prolexic, AWS Shield Advanced) divert attack traffic to the provider's high-capacity scrubbing infrastructure where it is filtered before clean traffic is forwarded to the customer. This is the only practical mitigation for terabit-scale DDoS.
  - Why C is incorrect: ARP poisoning is a Layer 2 attack affecting MAC-to-IP mappings on a local network segment. It does not involve high-volume inbound TCP SYN floods from external internet addresses. DAI is irrelevant to this attack.
  - Why D is incorrect: DNS poisoning targets DNS resolvers with forged cache records. This attack involves TCP SYN packets, not DNS query/response manipulation. DNSSEC would not mitigate a SYN flood.

---

### Question 6

While reviewing the ARP table on a workstation, a security analyst notices that the MAC address for the default gateway (192.168.1.1) matches the MAC address of another host on the same subnet (192.168.1.50). Wireshark captures show that 192.168.1.50 is sending periodic unsolicited ARP Replies claiming to be 192.168.1.1. Which attack is occurring and which switch-level countermeasure prevents it?

A) DNS poisoning is occurring; the countermeasure is DNSSEC on the local DNS resolver.

B) ARP poisoning is occurring; the countermeasure is Dynamic ARP Inspection (DAI), which validates ARP packets against the DHCP snooping binding table and drops forged ARP Replies.

C) VLAN hopping is occurring; the countermeasure is configuring all access ports as `switchport mode access` to prevent trunk negotiation.

D) A TCP SYN flood is occurring; the countermeasure is enabling SYN cookies on the gateway router.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: DNS poisoning involves forged DNS records in a resolver's cache. This attack involves forged ARP packets at Layer 2 — an entirely different protocol and layer. DNSSEC addresses DNS, not ARP.
  - Why B is correct: The scenario precisely describes ARP poisoning: one host (192.168.1.50) sends unsolicited ARP Replies claiming to be the default gateway (192.168.1.1) with its own MAC address. DAI prevents this by checking incoming ARP packets against the DHCP snooping binding table — if 192.168.1.50 was assigned 192.168.1.50 by DHCP, its ARP Reply claiming to be 192.168.1.1 would not match the binding and would be dropped.
  - Why C is incorrect: VLAN hopping exploits trunk negotiation or double-tagged 802.1Q frames to cross VLAN boundaries. This attack is ARP-based and does not involve VLANs or trunk links.
  - Why D is incorrect: SYN cookies address TCP SYN floods by allowing a server to respond to SYN packets without allocating connection state. This is an ARP-level attack, not a TCP flood.

---

### Question 7

A financial services company deploys a decoy system on their internal network configured to look like a domain controller with enticing share names. The system contains no real data. Security logs show three connection attempts to this system over the past month from internal IP addresses. What type of security control is this, and what does each connection attempt indicate?

A) This is a honeypot; each connection attempt is by definition suspicious because no legitimate user or process has a reason to access a system that serves no production function.

B) This is a NAC quarantine server; each connection attempt indicates a non-compliant device attempting to bypass remediation and reach production systems.

C) This is an IDS sensor in honeypot mode; connection attempts are legitimate users accidentally navigating to the wrong server, and the alerts can be safely ignored.

D) This is a DMZ web server; connection attempts from internal IP addresses indicate employees are accessing the public website from within the corporate network, which is normal behavior.

- Correct Answer: A
- Distractor Analysis:
  - Why A is correct: A honeypot is a decoy system with no legitimate users. Any connection to it is inherently suspicious because no authorized user or system has a reason to access a resource that performs no production function. Three internal connection attempts indicate potential insider threat activity, compromised internal hosts, or malware conducting internal reconnaissance.
  - Why B is incorrect: A NAC quarantine server is a remediation resource for non-compliant devices. It is actively communicated to by NAC-directed devices and would receive many legitimate connections from non-compliant endpoints. The key characteristic of a honeypot — that any connection is suspicious — does not apply to a NAC quarantine server.
  - Why C is incorrect: An IDS sensor monitors traffic; it is not a "honeypot mode" of the IDS. And the conclusion that alerts can be safely ignored is the opposite of correct — honeypot connections should be immediately investigated.
  - Why D is incorrect: The scenario describes an internal network system disguised as a domain controller, not a DMZ web server. Web servers in the DMZ do receive legitimate internal access, but the described system has no legitimate purpose — it is specifically designed as a decoy.

---

### Question 8

An organization wants to ensure that every device connecting to the corporate wired network has a current OS patch level and active endpoint protection software before being granted access to production resources. Non-compliant devices should be automatically placed in a restricted segment where they can only reach a patch server. Which technology framework satisfies all three requirements?

A) SNMPv3 polling — the network management system polls each device's OID for OS version and AV status before granting VLAN access.

B) Network Access Control (NAC) using 802.1X port authentication, a RADIUS server for policy enforcement, and a quarantine VLAN for non-compliant devices.

C) A two-firewall DMZ architecture with an outer ACL that checks device certificates before forwarding traffic to the internal LAN.

D) Syslog centralization — all device log messages are forwarded to a SIEM that generates alerts when patch levels are outdated, triggering manual port shutdown by the helpdesk.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: SNMP polling collects device statistics for monitoring purposes. It does not authenticate endpoints, assess posture, or enforce VLAN placement. SNMP cannot place a device in a quarantine VLAN based on a posture check.
  - Why B is correct: NAC with 802.1X precisely matches all three requirements: 802.1X challenges each device at port connection time, the RADIUS server communicates with a NAC engine that assesses posture (patch level, AV status), and non-compliant devices are assigned to a quarantine VLAN with restricted access to only the patch server. Compliant devices receive production VLAN access.
  - Why C is incorrect: A DMZ ACL inspects packet headers at the network layer — it cannot evaluate an endpoint's OS patch level or AV software status. ACLs operate on IP addresses and ports, not device security posture.
  - Why D is incorrect: This approach is entirely manual and reactive. Syslog can collect logs but cannot automatically enforce VLAN placement. The scenario requires automated enforcement — a human-in-the-loop process via the helpdesk would be too slow and unreliable.

---

### Question 9

A junior network administrator is configuring remote management access on a new branch router. She wants to allow the network operations team to manage the router remotely from headquarters. She enables Telnet on the router and creates an ACL allowing Telnet connections from the headquarters management subnet. A senior engineer reviews the configuration and immediately requires a change. What is the security problem and what is the correct remediation?

A) Telnet should not be limited to the management subnet — all subnets should be permitted to use Telnet for troubleshooting purposes.

B) Telnet transmits all data including usernames and passwords in plain text; the remediation is to disable Telnet and enable SSH, which encrypts the entire management session.

C) Telnet uses TCP port 22, which conflicts with SSH; the remediation is to change the Telnet port to 23 to avoid the conflict.

D) The ACL should be applied outbound rather than inbound to prevent unauthorized users from receiving login prompts.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: Expanding Telnet access to all subnets would make the security problem significantly worse, not better. The problem is the protocol itself, not the scope of the ACL.
  - Why B is correct: Telnet (TCP port 23) sends all session data — including the login username and password — in plain text. Any attacker who can capture traffic on the path between headquarters and the branch router can read the credentials. SSH (TCP port 22) encrypts the entire session with symmetric key encryption derived from asymmetric key exchange, making captured traffic unreadable.
  - Why C is incorrect: Telnet uses TCP port 23 and SSH uses TCP port 22. There is no conflict between them. Changing Telnet to port 23 (which it already uses) is meaningless, and the actual problem is the use of Telnet regardless of port.
  - Why D is incorrect: ACL direction (inbound vs. outbound) affects which traffic is filtered but does not change the fact that Telnet transmits credentials in plain text on the wire. The direction of the ACL is a separate concern from the encryption vulnerability.

---

### Question 10

A company is designing its AAA infrastructure for network device management. The security team requires that every command executed on network devices by an administrator is individually authorized and logged — not just the login event — and that the authorization and accounting records be kept separately from authentication records for compliance auditing. Which AAA protocol best satisfies these requirements?

A) RADIUS on UDP 1812 and 1813 — combines authentication, authorization, and accounting into a single transaction with full command-level logging.

B) TACACS+ on TCP 49 — separates authentication, authorization, and accounting into distinct transactions, supports per-command authorization, and encrypts the entire session payload.

C) SNMPv3 with authPriv — provides per-command authentication and authorization for all management operations on network devices.

D) RADIUS on UDP 1812 with syslog on UDP 514 — RADIUS handles authentication while syslog independently logs all executed commands.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: RADIUS combines authentication and authorization into a single response and does not natively support per-command authorization for network device CLI management. RADIUS is better suited for network access authentication (VPN, 802.1X) than for granular device command authorization.
  - Why B is correct: TACACS+ separates the three AAA functions into distinct transactions — authentication, authorization, and accounting are handled independently. This separation is precisely what the compliance requirement demands. TACACS+ supports per-command authorization (each CLI command can be independently permitted or denied) and encrypts the entire session. This is the standard for network device management authorization in Cisco environments.
  - Why C is incorrect: SNMPv3 is a network management protocol for device monitoring (GET, SET operations on MIB OIDs). It does not provide per-command CLI authorization or the AAA framework structure described in the scenario.
  - Why D is incorrect: RADIUS does not natively support per-command authorization. Using syslog for command logging is a workaround that provides logging but not authorization control — the security team's requirement includes individual command authorization (permit or deny specific commands), not just logging.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
