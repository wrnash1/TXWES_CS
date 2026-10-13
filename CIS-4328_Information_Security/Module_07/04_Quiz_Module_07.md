# Quiz: Module 07 — Network Security Architecture

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Questions mirror the style and difficulty of CompTIA Security+ SY0-701 exam items.

---

### Question 1

A security engineer needs to deploy a solution that can automatically block malicious traffic in real time as it passes through the network perimeter. Which control BEST meets this requirement?

A. Network IDS with a SPAN port connection

B. Host-based IDS on each endpoint

C. Network IPS deployed inline

D. SIEM with automated alerting

**Correct Answer:** C

**Explanation:** An IPS deployed inline sits directly in the traffic path and can inspect and block malicious traffic in real time. An IDS (whether network or host-based) is a passive detection tool — it generates alerts but cannot block traffic. A SIEM aggregates and correlates log data for analysis; it does not inspect or block live traffic.

---

### Question 2

An organization's web application is being targeted by SQL injection attacks. The perimeter NGFW has not detected the attacks because they arrive over HTTPS on port 443. Which additional control would MOST effectively mitigate this specific threat?

A. Deploy a second NGFW in tandem with the existing one

B. Implement a Web Application Firewall (WAF) in front of the web application

C. Enable the IPS signatures for port 443 on the NGFW

D. Switch the web application from HTTPS to HTTP so the NGFW can inspect it

**Correct Answer:** B

**Explanation:** A WAF is specifically designed to inspect HTTP/HTTPS application traffic and protect against OWASP Top 10 attacks including SQL injection and XSS. It understands the HTTP protocol semantics needed to detect injection patterns. A second NGFW does not add application-layer web inspection. An IPS on port 443 cannot inspect the content of TLS-encrypted payloads without decryption. Switching to HTTP removes encryption and is not an acceptable security tradeoff.

---

### Question 3

A company runs a customer-facing web server that must be accessible from the internet, and an internal database server containing customer financial records. Which placement BEST represents a secure architecture?

A. Both servers on the internal network, accessible via port forwarding

B. Web server in the DMZ; database server on the internal network

C. Both servers in the DMZ for simplified firewall management

D. Web server on the internet with a direct connection to the database

**Correct Answer:** B

**Explanation:** The DMZ is designed specifically for servers that must accept connections from untrusted external networks. Placing the web server in the DMZ and the database server on the internal network ensures that if the web server is compromised, the attacker cannot directly reach the database — they must cross the inner firewall, which permits only the specific query traffic needed. Placing the database in the DMZ or using direct port forwarding exposes it to unnecessary risk.

---

### Question 4

An IPS deployed inline at a healthcare facility fails during a software update. Patient monitoring systems lose network connectivity. Which fail behavior was configured, and which would have been MORE appropriate for this environment?

A. Fail-open was configured; fail-closed would be more appropriate

B. Fail-closed was configured; fail-open would be more appropriate

C. Fail-closed was configured; fail-closed remains appropriate for healthcare

D. Fail-open was configured; fail-open remains appropriate for healthcare

**Correct Answer:** B

**Explanation:** Fail-closed blocks all traffic when the device fails — this is what caused the loss of connectivity to patient monitoring systems. In a healthcare environment where patient care depends on network availability, fail-open is more appropriate: when the device fails, traffic passes through uninspected rather than being blocked. The security risk of uninspected traffic during a brief failure is more acceptable than blocking clinical communications.

---

### Question 5

An organization wants to replace their remote access VPN with a solution where authenticated users can only access the specific application they are authorized for, rather than gaining access to the entire corporate subnet. Which solution BEST meets this requirement?

A. Site-to-site IPsec VPN with split tunneling

B. Zero Trust Network Access (ZTNA)

C. Full-tunnel SSL VPN

D. Network Access Control (NAC)

**Correct Answer:** B

**Explanation:** ZTNA provides application-specific access based on verified identity and device posture. Unlike traditional VPN, which grants network-level access to a broad subnet, ZTNA grants access only to the specific application the user is authorized for. Site-to-site VPN connects entire networks. Full-tunnel SSL VPN provides broad network access, not application-specific access. NAC verifies device posture before network access but does not limit access to specific applications.

---

### Question 6

A firewall policy contains the following rules in order: (1) PERMIT TCP from 10.0.0.0/8 to ANY on port 443; (2) DENY TCP from 10.0.1.50 to ANY on port 443; (3) DENY ALL. A workstation at 10.0.1.50 attempts to connect to an external HTTPS server. What is the result?

A. The connection is permitted by Rule 1

B. The connection is denied by Rule 2

C. The connection is denied by Rule 3

D. The connection is permitted because HTTPS is allowed by default

**Correct Answer:** A

**Explanation:** Firewall rules are evaluated top to bottom, and the first matching rule wins. Rule 1 matches the traffic from 10.0.1.50 (which is within 10.0.0.0/8) on port 443 and permits it. Rule 2, which would deny that specific host on port 443, is never reached because Rule 1 already matched. To achieve the intended behavior of denying 10.0.1.50, Rule 2 would need to be placed above Rule 1.

---

### Question 7

A security analyst notices that workstations on the internal network are making frequent DNS queries for domain names that follow a random-looking pattern: `xkqprzalbf3927.example.com`, `mzqtbnaldf7421.example.com`. What attack technique do these patterns suggest?

A. DNS cache poisoning

B. Domain Generation Algorithm (DGA) beaconing

C. DNS zone transfer

D. Pharming

**Correct Answer:** B

**Explanation:** Domain Generation Algorithms (DGAs) are used by malware to generate a large number of pseudo-random domain names that the malware's command-and-control infrastructure rotates through. This makes it difficult to block C2 communication by blacklisting domains. The random-looking patterns are the characteristic indicator. DNS cache poisoning modifies DNS responses. DNS zone transfer requests a copy of all DNS records. Pharming redirects legitimate URLs.

---

### Question 8

Which network segmentation technology enforces access policies between individual workloads running in the same subnet, preventing east-west lateral movement between workloads that share a VLAN?

A. VLAN tagging

B. Stateful perimeter firewall

C. Microsegmentation

D. DMZ

**Correct Answer:** C

**Explanation:** Microsegmentation applies access policies at the workload level — individual virtual machines, containers, or processes — regardless of whether they share a network segment. Traditional VLAN segmentation only separates traffic at the subnet level; workloads within the same VLAN can communicate freely. A perimeter firewall controls traffic entering or leaving the network, not east-west traffic within the network. A DMZ isolates publicly accessible servers but does not enforce workload-level policies.

---

### Question 9

A company configures their remote access VPN with split tunneling enabled. What is the PRIMARY security concern with this configuration?

A. Split tunneling increases VPN gateway load beyond capacity

B. Users' internet traffic bypasses corporate security controls, reducing visibility and protection

C. Split tunneling prevents access to internal resources

D. Encrypted tunnels cannot be established when split tunneling is active

**Correct Answer:** B

**Explanation:** With split tunneling, only traffic destined for corporate resources is routed through the VPN. Internet-bound traffic goes directly from the user's device to the internet, bypassing corporate proxy servers, web filtering, IPS, and DLP controls. This creates a gap where malware on the user's device can communicate with external C2 servers or exfiltrate data without inspection. Full tunneling routes all traffic through the corporate gateway, maintaining visibility and control.

---

### Question 10

An organization implements Network Access Control (NAC). A device connecting to the network fails the posture assessment because its antivirus definitions are 45 days old. What should NAC do with this device?

A. Permit full network access since the device is owned by the organization

B. Deny all network access and require the user to contact IT support

C. Place the device in a quarantine VLAN where it can only access remediation resources

D. Alert the SIEM and permit the connection pending manual review

**Correct Answer:** C

**Explanation:** A quarantine VLAN provides a restricted network environment where the non-compliant device can access only the resources it needs to remediate the compliance failure — in this case, an AV definition update server. This approach is more appropriate than a full deny (which creates a bad user experience and may require IT intervention for a self-correctable issue) while ensuring the non-compliant device does not gain access to the trusted network.

---

---

### Question 11

A stateful firewall differs from a packet-filtering firewall primarily because a stateful firewall:

A. Operates at OSI Layer 7 and inspects application content

B. Tracks the state of network connections and allows return traffic for established sessions

C. Uses signature matching to detect known attack patterns

D. Authenticates users before permitting traffic

**Correct Answer:** B

**Explanation:** A stateful firewall maintains a connection state table and automatically permits return traffic for established, legitimate sessions — without requiring an explicit permit rule for inbound return packets. A packet-filtering firewall evaluates each packet individually with no memory of prior packets, often requiring bidirectional permit rules. Layer 7 inspection describes an application-layer gateway or NGFW. Signature matching describes IDS/IPS. User authentication describes a proxy or identity-aware firewall.

---

### Question 12

An organization wants to detect unauthorized devices connecting to network switch ports using 802.1X. When a device connects that cannot provide valid credentials, the switch should deny network access but allow the device to request a certificate from an internal PKI server. Which NAC configuration achieves this?

A. Place non-compliant devices in a quarantine VLAN with access only to the certificate enrollment server

B. Configure the switch to drop all traffic from unauthenticated devices

C. Deploy a host-based agent on every device to verify 802.1X credentials

D. Enable dynamic ARP inspection on all switch ports

**Correct Answer:** A

**Explanation:** A quarantine VLAN provides restricted network access for devices that fail 802.1X authentication, allowing them to reach only specific remediation or enrollment resources — in this case, the PKI certificate server. Simply dropping all traffic (option B) would prevent the device from obtaining the certificate it needs to authenticate. Host-based agents require software installation, which is not possible before network access is granted. Dynamic ARP inspection protects against ARP spoofing, not 802.1X authentication failures.

---

### Question 13

A security engineer is designing a honeypot. The engineer wants the honeypot to be convincing enough to keep an attacker engaged while real systems are monitored. Which deployment consideration is MOST critical for ensuring the honeypot does not create additional risk?

A. The honeypot must use the same operating system version as production systems

B. The honeypot must be isolated so that an attacker who compromises it cannot pivot to production systems

C. The honeypot should generate alerts only for critical-severity events to reduce analyst fatigue

D. The honeypot must be placed in the DMZ for maximum exposure to attackers

**Correct Answer:** B

**Explanation:** The primary risk of a honeypot is that it becomes a staging point for attacking production systems. Strict network isolation — ensuring the honeypot cannot reach or be used to reach internal production resources — is the most critical control. If the honeypot is compromised and has connectivity to production, it creates a foothold rather than a detection tool. OS version matching may make it more convincing but is secondary. Alert tuning is an operational concern. DMZ placement is one option but not universally required.

---

### Question 14

An organization uses OSPF to exchange routing information between its routers. A security analyst discovers that an unauthorized router has been injecting false route advertisements, causing traffic to be redirected through an attacker-controlled device. Which control would have prevented this routing attack?

A. DNSSEC to validate DNS responses

B. OSPF neighbor authentication using MD5 or SHA

C. Deploying a reverse proxy in front of the routers

D. Enabling VLAN tagging on all router interfaces

**Correct Answer:** B

**Explanation:** OSPF supports neighbor authentication, requiring routers to authenticate with each other before exchanging routing updates. Using MD5 or SHA-based authentication ensures that only authorized routers can participate in the OSPF domain and inject routes. An attacker without the authentication key cannot inject false route advertisements. DNSSEC protects DNS, not routing protocols. A reverse proxy manages client-to-server web traffic. VLAN tagging is a Layer 2 segmentation mechanism and does not affect routing protocol security.

---

### Question 15

A network engineer configures a switch port with port security to allow only one MAC address. An attacker uses a technique that forges the MAC address of a legitimate device. Which attack is the attacker using, and which control MOST effectively detects it?

A. ARP spoofing; detected by IDS signature for ARP packet anomalies

B. MAC spoofing; detected by dynamic ARP inspection correlating IP-to-MAC bindings from DHCP snooping

C. MAC flooding; mitigated by 802.1X authentication on switch ports

D. VLAN hopping; prevented by disabling dynamic trunking protocol

**Correct Answer:** B

**Explanation:** MAC spoofing involves forging the source MAC address of a network frame to impersonate a known, authorized device. Dynamic ARP inspection (DAI) works with DHCP snooping to build a binding table of legitimate IP-to-MAC-to-port mappings and drops ARP packets that do not match. This detects impersonation even when the attacker correctly spoofs a MAC. MAC flooding overwhelms the switch's CAM table to force broadcast behavior. VLAN hopping exploits trunk negotiation to access other VLANs. Option A confuses ARP spoofing (a different attack) with MAC spoofing.

---

### Question 16

Which VPN protocol operates at OSI Layer 3 and encapsulates entire IP packets within a new IP envelope to create a tunnel between two network sites?

A. TLS/SSL VPN

B. IPsec in Tunnel mode

C. IPsec in Transport mode

D. L2TP without IPsec

**Correct Answer:** B

**Explanation:** IPsec in Tunnel mode encapsulates the entire original IP packet — including its header — within a new outer IP packet. This is the standard configuration for site-to-site VPNs connecting two networks, because the original packet's addressing is hidden inside the tunnel. IPsec Transport mode only encrypts the payload and leaves the original IP header intact, used for host-to-host communication. TLS/SSL VPN operates at the application layer (Layer 5–7). L2TP without IPsec provides encapsulation but no encryption.

---

### Question 17

A network security team implements an out-of-band management network for all network devices, including switches, routers, and firewalls. What is the PRIMARY security benefit of this architecture?

A. Out-of-band management increases the available bandwidth for production traffic

B. Administrative access to network devices is isolated from the production data plane, limiting an attacker's ability to reach management interfaces

C. Out-of-band management replaces the need for encrypted management protocols like SSH

D. It provides automatic failover if the primary network path fails

**Correct Answer:** B

**Explanation:** An out-of-band management network is a separate, dedicated network used exclusively for administrative access to network devices. By separating management traffic from production traffic, an attacker who compromises a host on the production network cannot reach device management interfaces, which are only accessible via the isolated management plane. This limits lateral movement to network infrastructure even after a production network compromise. Out-of-band management does not replace SSH or increase production bandwidth; it is a segmentation and access control measure.

---

### Question 18

A forward proxy server is deployed at the network edge. An internal user's web request is processed by the proxy. Which statement BEST describes what the external web server sees as the connection source?

A. The internal user's private IP address

B. The proxy server's IP address

C. The NAT gateway's public IP address, bypassing the proxy

D. The internal user's MAC address translated to an IP

**Correct Answer:** B

**Explanation:** When a forward proxy handles a request, it acts as an intermediary — the proxy establishes the connection to the external web server on behalf of the user. The external server sees the proxy's IP address as the connection source, not the internal user's private address. This provides anonymity and allows the proxy to inspect, filter, and log all requests. The NAT gateway handles IP address translation differently from a proxy — a proxy makes its own connection request rather than just translating addresses.

---

### Question 19

An organization wants to ensure that even if an attacker captures traffic from its site-to-site VPN today, compromising the VPN server's long-term private key in the future will not allow decryption of the captured traffic. Which VPN configuration property addresses this requirement?

A. Certificate pinning

B. Perfect Forward Secrecy using ephemeral Diffie-Hellman key exchange

C. AES-256 encryption for the tunnel

D. HMAC-SHA256 message authentication

**Correct Answer:** B

**Explanation:** Perfect Forward Secrecy (PFS) ensures that session keys are derived from ephemeral (temporary) key material generated fresh for each session, not from the long-term private key. Even if the server's long-term private key is later compromised, the ephemeral session keys cannot be derived from it, so past captured traffic remains protected. AES-256 provides confidentiality within a session but does not address retrospective decryption if the key is compromised. HMAC-SHA256 provides integrity. Certificate pinning validates server identity.

---

### Question 20

An organization's flat internal network has no VLANs and no internal firewalls. An attacker who compromises a single workstation in the marketing department can freely scan and connect to HR servers, finance databases, and development systems. Which network architecture change would MOST effectively limit this lateral movement without replacing the existing hardware?

A. Deploy a perimeter NGFW with deep packet inspection

B. Implement VLAN segmentation with inter-VLAN routing through an internal firewall

C. Enable DNSSEC on the internal DNS server

D. Deploy a NAC solution to check device compliance before granting network access

**Correct Answer:** B

**Explanation:** VLAN segmentation divides the flat network into separate logical segments for each department or function. By routing inter-VLAN traffic through an internal firewall with restrictive policies, traffic between departments is inspected and controlled — a compromise in the marketing VLAN cannot directly reach finance or HR VLANs. This can be implemented with existing switch hardware using software configuration. A perimeter NGFW only controls traffic at the network edge and does not address east-west traffic. DNSSEC protects DNS integrity but not network segmentation. NAC controls admission but does not segment traffic once a device is admitted.

---

Module 07 Quiz — End
