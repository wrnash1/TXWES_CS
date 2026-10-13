# Video Script: Module 08 — Network Security Concepts (Part 2 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

### SLIDE 1 — Welcome Back

Welcome back to Module 8. In Part 1 we covered the CIA triad, stateless and stateful firewalls, IDS/IPS, the DMZ architecture, and the AAA framework. In Part 2 we cover the attack categories you must recognize for the exam — DoS, DDoS, man-in-the-middle, and ARP poisoning — plus honeypots, VPN types in the security context, and key security hardening practices.

---

### SLIDE 2 — DoS: Denial of Service Attacks

A **DoS (Denial of Service)** attack targets the Availability pillar of the CIA triad. The goal is not to steal data but to make a system or service unavailable to legitimate users.

DoS attack mechanisms:

**Flood attack** — Overwhelms the target with more traffic than it can process. The target's CPU, memory, or bandwidth is exhausted. Examples: ICMP flood (ping flood), UDP flood, HTTP flood.

**TCP SYN flood** — Exploits the TCP three-way handshake. The attacker sends a large volume of SYN packets with forged source IP addresses. The server responds with SYN-ACK to each forged source, which never replies, leaving a half-open connection entry in the server's connection table. With enough forged SYNs, the connection table fills completely, preventing the server from accepting any new legitimate connections.

**Vulnerability exploitation DoS** — A specific malformed packet exploits a software vulnerability that causes the target to crash. Requires far fewer packets than a flood attack.

A classic DoS originates from a single source. This makes it relatively easy to mitigate — block the attacking IP at the perimeter firewall.

---

### SLIDE 3 — DDoS: Distributed Denial of Service

A **DDoS (Distributed Denial of Service)** attack is a DoS attack launched simultaneously from thousands or millions of compromised hosts — a botnet.

Key characteristics:

**Botnet** — A network of compromised computers (bots or zombies) controlled by a command-and-control (C2) server. Each bot was infected by malware that allows the attacker to direct its traffic without the owner's knowledge.

**Distributed source** — Traffic originates from many different IP addresses across many geographic locations and ISPs. Simple IP-based blocking is ineffective — there is no single attacking IP to block.

**Scale** — Major DDoS attacks generate hundreds of gigabits or multiple terabits per second of attack traffic, far exceeding any individual organization's internet capacity.

DDoS mitigation:

- **Upstream scrubbing services**: Commercial providers such as Cloudflare and AWS Shield absorb attack traffic at their massive global networks before it reaches the victim.
- **Rate limiting**: Limit traffic rates per source to reduce the impact of any single attacking IP.
- **Blackhole routing**: Route all traffic destined for the attacked IP to null, sacrificing the service to protect the rest of the infrastructure.

Exam key: DoS = single source. DDoS = multiple distributed sources (botnet). This distinction is directly tested.

---

### SLIDE 4 — Man-in-the-Middle (MITM) Attacks

A **man-in-the-middle (MITM)** attack occurs when an attacker secretly intercepts communication between two parties who each believe they are communicating directly with each other.

MITM attack flow:

- Host A wants to communicate with Host B
- Attacker positions themselves between A and B in the traffic path
- A sends data intended for B — the attacker receives it, optionally reads or modifies it, then forwards it to B
- B's replies back to A are also intercepted
- Neither party knows the attacker is in the middle

MITM enables:

- Eavesdropping on confidential data
- Session hijacking — stealing authentication cookies to impersonate a user
- Credential harvesting — capturing plain-text usernames and passwords
- Data modification — altering transactions or injecting malicious content

MITM countermeasures:

- Encrypt all communications with TLS/HTTPS so intercepted data is ciphertext
- Validate TLS certificates — a MITM attacker cannot present a valid certificate for a legitimate domain without compromising a trusted Certificate Authority
- Certificate pinning — applications compare the server's certificate against a pre-stored expected certificate and reject mismatches

---

### SLIDE 5 — ARP Poisoning

**ARP Poisoning** (also called ARP Spoofing or ARP Cache Poisoning) is the most common mechanism used to execute a MITM attack on a local area network segment.

ARP review: ARP maps IP addresses to MAC addresses. A host broadcasts "Who has 192.168.1.1?" The gateway responds with its MAC address. The host caches this mapping and uses the MAC address in Ethernet frames.

ARP is inherently unauthenticated — any host can send an unsolicited ARP Reply and receiving hosts will accept it.

ARP poisoning steps:

1. Attacker sends a forged ARP Reply to Host A: "192.168.1.1 is at MAC AA:BB:CC:DD:EE:FF" (attacker's MAC)
2. Attacker sends a forged ARP Reply to the router: "192.168.1.10 is at MAC AA:BB:CC:DD:EE:FF" (attacker's MAC)
3. Both Host A and the router cache the attacker's MAC address for each other's IP
4. Host A's traffic to the router now flows through the attacker, who forwards it to the real router
5. The attacker sees all traffic between Host A and the router

Countermeasures:

- **Dynamic ARP Inspection (DAI)**: A Cisco switch feature that validates ARP packets against the DHCP snooping binding table. Forged ARP Replies not matching known DHCP-assigned IP-to-MAC bindings are dropped at the ingress port.
- **Static ARP entries**: Manually configure permanent ARP entries for critical hosts — not scalable for large environments.
- **Encryption**: Even with ARP poisoning in place, TLS ensures the attacker cannot read the intercepted payload.

---

### SLIDE 6 — Additional Attack Types

Several additional attack types are tested on the Network+ exam:

**DNS Spoofing / DNS Cache Poisoning** — An attacker injects forged DNS records into a resolver's cache. Users querying that resolver are directed to a malicious IP address instead of the legitimate one. Countermeasure: DNSSEC cryptographically signs DNS records to prevent unauthorized modification.

**VLAN Hopping** — An attacker on an access port attempts to send traffic onto a different VLAN without authorization. Two methods:

- Switch spoofing: The attacker's NIC negotiates a trunk link with the switch, receiving all VLAN traffic
- Double tagging: The attacker sends a double-tagged 802.1Q frame; the first switch strips the outer tag and forwards the frame on the target VLAN's trunk

Countermeasure: Explicitly configure all access ports as `switchport mode access` to prevent auto-trunk negotiation. Set the native VLAN to an unused VLAN ID.

**Brute Force Attack** — Systematically tries all possible passwords until the correct one is found. Countermeasures: account lockout policies after N failed attempts, strong password requirements, MFA.

**Social Engineering / Phishing** — Manipulating people rather than exploiting technology. Phishing uses email; spear-phishing is targeted at specific individuals; vishing uses phone calls. Countermeasure: user security awareness training.

**Insider Threat** — A malicious or negligent authorized user misusing their access. Countermeasure: least privilege, role-based access control, behavioral monitoring.

---

### SLIDE 7 — Honeypots and Honeynets

A **honeypot** is a decoy system intentionally deployed to attract and study attackers.

How honeypots work:

- The honeypot appears to be a valuable target — a domain controller, file server, or database — but contains no real production data
- Legitimate users have no reason to access it; therefore any interaction is by definition suspicious
- All connections and activities are logged in full detail, providing intelligence about attacker tools and techniques
- The attacker wastes time and resources on the decoy instead of real systems

Honeypot types:

**Low-interaction honeypot** — Simulates limited services. Easy to deploy, low maintenance. Detects basic scanning and connection attempts. Does not capture complex attacker behavior.

**High-interaction honeypot** — Runs a real OS and real services. Provides deep behavioral intelligence. More complex to isolate safely.

**Honeynet** — A network of multiple honeypots designed to simulate an entire enterprise environment for richer threat intelligence.

Exam point: A honeypot is a security tool that detects and studies attackers. It is NOT a firewall, IDS, or IPS — it does not block traffic or alert on legitimate network activity. Any connection to a honeypot is inherently suspicious.

---

### SLIDE 8 — VPN in the Security Architecture

In security architecture, VPNs are categorized by scope and posture:

**Remote Access VPN** — Individual users connect encrypted tunnels from remote locations to the corporate network. Common protocols: SSL/TLS VPN on TCP 443, IPsec. VPN concentrator terminates client connections at the perimeter.

**Site-to-Site VPN** — Two networks connected by a persistent encrypted tunnel between edge devices. IPsec Tunnel mode. End users need no VPN client software.

**Always-On VPN** — The VPN connects automatically at device startup before user login. Ensures device management traffic and pre-authentication data are protected. Used in zero-trust and BYOD architectures.

**Split-tunnel security implications**:

- Full-tunnel forces all user traffic through the corporate security stack — DLP, URL filtering, IPS, and logging apply to all traffic
- Split-tunnel sends internet traffic directly from the user device — corporate controls do not inspect internet-bound traffic

From a security policy perspective, regulated industries often mandate full-tunnel VPN to ensure DLP and compliance controls apply to all outbound data.

---

### SLIDE 9 — Network Access Control (NAC)

**Network Access Control (NAC)** enforces security policy compliance on devices before granting full network access.

NAC posture checks:

- Is the OS current (no missing critical patches)?
- Is endpoint protection software installed and updated?
- Is disk encryption enabled?
- Is the device a recognized corporate asset or a personal device?

NAC enforcement modes:

**Pre-admission NAC** — The device is quarantined to a remediation VLAN with limited access (typically only reaching a patch server and antivirus update server) until all posture checks pass. Once compliant, the switch moves the device to the appropriate production VLAN.

**Post-admission NAC** — The device is admitted initially but continuously monitored. Non-compliant behavior triggers automatic quarantine.

Implementation: 802.1X port-based authentication + RADIUS server + NAC policy engine (Cisco ISE, Aruba ClearPass). The switch acts as the enforcer — it challenges the device with 802.1X EAP, forwards credentials to the RADIUS server, which queries the NAC engine before authorizing access.

---

### SLIDE 10 — Security Hardening Quick Reference

The Network+ exam tests several security hardening practices. Memorize this list:

Change default credentials on every managed device immediately upon deployment.

Disable Telnet — use SSH for all remote management. Telnet sends credentials in plain text.

Disable unused ports and services — each open port is an attack surface.

Enable port security on switches — limit the number of MAC addresses per port and disable unused switch ports.

Use HTTPS for web-based management consoles, not HTTP.

Restrict management access by ACL — allow SSH and SNMP only from known administrator IP addresses.

Enable SNMP version 3 — never leave SNMPv2c default community strings unchanged.

Segment the network with VLANs — separate guest, user, server, IoT, and management traffic into isolated segments with firewall rules controlling inter-segment access.

Apply patches regularly — unpatched network devices are one of the most common attack vectors in enterprise breaches.

---

### SLIDE 11 — Module 8 Full Summary and Exam Tips

Let's consolidate Module 8 for the exam:

CIA triad applications: Encryption = Confidentiality. Hashing (SHA-256) = Integrity. Redundancy and patching = Availability.

Firewall progression: Stateless (packet filter, per-packet, no state) → Stateful (state table, understands connections) → NGFW (adds application visibility, DPI, IPS integration).

IDS vs. IPS: IDS is passive, alerts only. IPS is inline, blocks. A SPAN port deployment can only support IDS. Inline deployment supports IPS.

DMZ: Public servers live in the DMZ between outer and inner firewalls. The inner firewall controls what DMZ servers can reach inside the LAN.

AAA protocols: RADIUS uses UDP 1812 and 1813. TACACS+ uses TCP 49 and separates the three AAA functions.

Attacks: DoS = single source. DDoS = botnet. MITM = intercepts A-to-B communication. ARP poisoning = LAN MITM via forged ARP Replies — mitigated by Dynamic ARP Inspection. DNS poisoning = forged DNS cache records — mitigated by DNSSEC. VLAN hopping = mitigated by disabling auto-trunking.

Honeypot: Decoy target. Any access is suspicious. Provides threat intelligence. Does not block.

NAC: 802.1X + RADIUS + NAC engine. Posture check before admission. Quarantine VLAN for non-compliant devices.

Physical: Mantrap prevents tailgating. Lock all network equipment. Secure console ports.

Module 9 covers Wireless Networking — 802.11 standards, frequency bands, CSMA/CA, SSID, site survey, and interference sources.

---

*End of Part 2*
