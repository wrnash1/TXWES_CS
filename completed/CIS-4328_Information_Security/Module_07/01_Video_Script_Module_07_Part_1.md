# Video Script: Module 07 — Network Security Architecture (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Module 07, Part 1. I'm Professor Nash.

Network security architecture defines how you design networks to limit the blast radius of an attack, enforce traffic policies, and detect threats in transit. This module covers firewalls, IDS/IPS, the DMZ, proxy servers, load balancers, network segmentation, microsegmentation, and zero-trust network architecture.

Security+ Domain 3 — "Network Architecture" — draws heavily from this content. More importantly, every penetration test engagement and every incident response investigation eventually leads back to network architecture questions: how did the attacker move laterally? What controls were in path? What should have caught this?

Part 1 covers the conceptual foundations — what each control is and why it exists. Part 2 covers deployment configurations, detection, and exam traps.

---

### [SECTION 1 — Firewall Evolution — 1:00]

A firewall inspects network traffic and enforces a policy that permits or denies specific traffic.

#### Packet Filter (Stateless) Firewalls

The earliest firewall type. Inspects each packet independently based on:

- Source and destination IP address.

- Source and destination port.

- Protocol (TCP, UDP, ICMP).

**Critical weakness**: Stateless. The firewall does not track whether a TCP connection was legitimately established. An attacker can craft a packet that appears to be a response to an established connection but is actually an unsolicited inbound connection.

#### Stateful Firewalls

A stateful firewall maintains a **connection state table**. It tracks TCP three-way handshakes and knows which connections are currently established. Return traffic for an established outbound connection is permitted automatically; unsolicited inbound packets are denied.

This is the baseline capability for modern firewalls. Almost all production firewalls are stateful.

#### Application-Layer (Proxy) Firewalls

Inspects traffic at Layer 7 — the application layer. Can understand HTTP, DNS, SMTP, and other protocol semantics. Can block specific URLs, inspect HTTP headers, and detect protocol anomalies.

#### Next-Generation Firewall (NGFW)

The current standard. A NGFW combines:

- Stateful packet inspection.

- Application identification and control (can block Dropbox regardless of port).

- User identity awareness (policies based on user, not just IP).

- Integrated IPS (Intrusion Prevention System).

- SSL/TLS decryption and inspection.

- Threat intelligence feeds.

**Exam point**: The term NGFW specifically implies application awareness and identity-based policies, not just stateful inspection. When the exam mentions "identifying applications regardless of port," that is NGFW.

#### Web Application Firewall (WAF)

A WAF sits in front of a web application and inspects HTTP/HTTPS traffic specifically.

WAFs protect against:

- SQL injection.

- Cross-site scripting (XSS).

- OWASP Top 10 vulnerabilities.

- Volumetric web attacks.

**Exam distinction**: A WAF protects web applications. An NGFW protects network traffic broadly. A scenario involving SQL injection protection or XSS protection points to a WAF.

---

### [SECTION 2 — IDS and IPS — 5:30]

**IDS (Intrusion Detection System)** monitors network traffic or host activity and **alerts** when it detects suspicious behavior.

**IPS (Intrusion Prevention System)** does everything an IDS does but also **takes action** — blocking traffic, resetting connections, or quarantining a host.

**Key distinction**: IDS detects and reports. IPS detects and responds. An IDS is always **out-of-band** (traffic flows past a tap or span port). An IPS is always **inline** (traffic flows through the IPS).

#### Detection Methods

**Signature-based detection** — compares traffic to a database of known attack signatures.

- Advantage: low false positives for known attacks.

- Weakness: cannot detect zero-day attacks with no signature.

**Anomaly-based (behavioral) detection** — builds a baseline of normal behavior and alerts on deviations.

- Advantage: can detect novel attacks.

- Weakness: higher false positive rate; requires baseline tuning.

**Exam trap**: "An organization wants to detect unknown threats." The answer involves anomaly-based or behavioral detection, not signature-based.

#### Network vs. Host IDS/IPS

**NIDS/NIPS** — deployed at network chokepoints; monitors traffic between systems.

**HIDS/HIPS** — installed on individual hosts; monitors local process activity, file changes, system calls.

**Exam point**: HIDS can detect threats that encrypt their network traffic because it observes the endpoint behavior directly, not the wire.

---

### [SECTION 3 — DMZ Architecture — 8:00]

A **DMZ (Demilitarized Zone)** is a network segment that sits between the untrusted internet and the trusted internal network.

Servers that must be accessible from the internet — web servers, mail servers, public DNS, VPN concentrators — are placed in the DMZ. This way, if a DMZ server is compromised, the attacker cannot directly reach internal resources without crossing a second firewall.

#### Classic Dual-Firewall DMZ

The standard architecture uses two firewalls:

- **Outer firewall** (internet-facing): separates internet from DMZ. Permits inbound HTTP/HTTPS, SMTP, etc. to the DMZ. Blocks all other inbound traffic.

- **Inner firewall** (internal-facing): separates DMZ from internal network. Permits only specific, necessary traffic from DMZ to internal systems (e.g., database queries from the DMZ web server to the internal database server on the specific required port). Denies everything else.

**Why two firewalls?** If the outer firewall is compromised, the inner firewall is a second line of defense.

**Exam point**: A screened subnet (the technical term for a DMZ segment) created with a single firewall using multiple interfaces is also valid but provides less defense-in-depth than the dual-firewall design.

---

### [SECTION 4 — Proxy Servers — 10:00]

A proxy server acts as an intermediary between clients and external servers.

#### Forward Proxy

Sits between internal users and the internet. Users' requests go through the proxy, which makes the request on their behalf.

Uses:

- Content filtering (blocking inappropriate or malicious sites).

- Caching (improving performance).

- Anonymization (external sites see the proxy's IP, not the user's).

- TLS inspection (decrypt outbound HTTPS to scan for malware and data exfiltration).

#### Reverse Proxy

Sits in front of internal servers, accepting requests from external clients.

Uses:

- Load balancing across multiple backend servers.

- SSL offloading (handles TLS termination; backend servers receive unencrypted traffic).

- Web application firewall integration.

- Concealing the backend server topology.

**Exam distinction**: A forward proxy protects internal users from the internet. A reverse proxy protects internal servers from internet clients.

---

### [SECTION 5 — Load Balancers — 11:30]

A load balancer distributes incoming traffic across multiple backend servers to improve performance and availability.

Key security relevance:

- Provides **redundancy** — if one server fails, traffic continues to others.

- Absorbs volumetric attacks (part of DDoS mitigation).

- Can perform **health checks** — removes unhealthy servers from the pool.

- Often includes SSL offloading — a security relevant consideration because inspecting encrypted traffic requires decryption.

Load balancer algorithms:

- **Round-robin** — distributes sequentially.

- **Least connections** — sends to the server with the fewest active connections.

- **IP hash** — same client IP always goes to the same server (session persistence).

**Exam point**: Load balancers are primarily an availability control. The Security+ exam tests them in the context of high availability (HA) design and DDoS mitigation.

---

### [SECTION 6 — Network Segmentation and Microsegmentation — 13:00]

**Network segmentation** divides a network into separate zones or subnets, each with different trust levels and access policies.

Why it matters for security: if an attacker compromises one segment, they cannot freely move to other segments. Lateral movement — pivoting from system to system — requires crossing a security boundary.

Traditional segmentation uses VLANs (Virtual LANs) and routers/firewalls between segments. Examples:

- User workstation segment.

- Server segment.

- OT/SCADA segment.

- Guest/IoT segment.

**Microsegmentation** takes segmentation to the workload level. Rather than segmenting by network zone, microsegmentation enforces access policies between individual workloads — even workloads in the same VLAN or subnet.

In a microsegmented environment, a compromised web server cannot initiate connections to a database server on the same subnet unless a policy explicitly permits it. This dramatically reduces the impact of lateral movement.

Microsegmentation is a foundational component of **zero-trust network architecture** — the subject of Part 2.

---

### [OUTRO — 14:30]

Part 1 has covered the core network security infrastructure:

- Firewalls: stateless → stateful → application-layer → NGFW → WAF.

- IDS vs. IPS: out-of-band detection vs. inline prevention; signature vs. anomaly detection.

- DMZ: internet-accessible servers isolated from the internal network.

- Proxy servers: forward proxy for users, reverse proxy for servers.

- Load balancers: availability and DDoS mitigation.

- Segmentation and microsegmentation: limiting lateral movement.

In Part 2 we cover zero-trust architecture in depth, firewall rule design, IDS tuning, and the Security+ exam traps in this domain.

See you in Part 2.

---

End of Part 1 — Module 07
