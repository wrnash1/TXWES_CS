# Video Script: Module 07 — Network Security Architecture (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Part 2 of Module 07. In Part 1 we built the infrastructure layer — firewalls, IDS/IPS, DMZ, proxies, load balancers, and segmentation. Now we go deeper on zero-trust network architecture, firewall rule design principles, and the specific exam traps in this domain.

---

### [SECTION 1 — Zero Trust Network Architecture — 0:30]

**Zero Trust** is an architectural philosophy based on the principle: **never trust, always verify**.

Traditional network security operated on a perimeter model: trust the inside, distrust the outside. If a user was on the corporate network, they were implicitly trusted. This model collapses when attackers are already inside the perimeter — via a phishing email, a VPN credential, or a supply chain compromise.

Zero Trust eliminates implicit trust based on network location. Every access request — regardless of whether it comes from inside or outside the network — must be:

- **Authenticated** — identity verified.

- **Authorized** — access explicitly permitted for this specific resource.

- **Inspected** — traffic monitored and analyzed.

#### CISA Zero Trust Pillars

The CISA Zero Trust Maturity Model defines five pillars:

- **Identity** — who is the user? Verified with strong authentication, continuous monitoring.

- **Device** — is the device healthy and compliant? Device posture checked before granting access.

- **Network** — microsegmented; no implicit trust based on subnet.

- **Application/Workload** — applications authenticate to each other; no implicit service trust.

- **Data** — data is classified and access is controlled at the data level.

**Exam point**: Zero Trust is not a product — it is an architecture. No single product makes a network zero-trust. The principles are: verify explicitly, use least privilege, assume breach.

#### Software-Defined Perimeter (SDP)

SDP implements zero trust for network access. Resources are invisible ("dark") until a user authenticates and their device passes posture checks. Only then is a network path created to the specific resource requested.

This is different from VPNs, which grant network access to a broad subnet after authentication. SDP grants access to specific resources, not broad network segments.

---

### [SECTION 2 — Firewall Rule Design — 4:00]

Understanding how firewall rules work is critical for both the exam and real-world practice.

#### Implicit Deny

All modern firewalls use an **implicit deny** rule at the end of their rule list: deny all traffic not explicitly permitted. This is the most important rule in any firewall policy.

**Exam trap**: If a question asks "What allows all traffic to pass through a firewall that has no explicit rules?" — the answer is that it does NOT pass through. The implicit deny blocks everything not explicitly allowed.

#### Rule Order

Firewall rules are evaluated top-to-bottom. The **first matching rule wins**. This means:

- More specific rules go before more general rules.

- A broad "deny all" rule placed before a specific "allow web" rule would block web traffic.

**Exam scenario**: "An administrator adds an allow rule for HTTPS but users still cannot access HTTPS sites." — check whether a deny rule above the allow rule is matching first.

#### Ingress vs. Egress Filtering

- **Ingress filtering** — controls inbound traffic (from untrusted networks to your network).

- **Egress filtering** — controls outbound traffic (from your network to untrusted networks).

Egress filtering is often neglected but critical. Without egress filtering, malware can establish command-and-control connections and exfiltrate data freely. Attackers target environments with no egress controls.

---

### [SECTION 3 — IDS/IPS Tuning and False Positives — 6:30]

An IDS or IPS that is not tuned properly produces enormous volumes of **false positives** — alerts on legitimate traffic.

**False positive** — the system alerts on benign traffic. Security team wastes time investigating non-events; real alerts get buried in noise.

**False negative** — the system fails to alert on actual malicious traffic. An attack succeeds undetected.

These two error types trade off: increasing sensitivity reduces false negatives but increases false positives.

The goal of IDS/IPS tuning is to find the threshold where the signal-to-noise ratio is actionable — high enough to catch real attacks, low enough that analysts can respond.

#### Inline vs. Passive Deployment

**Passive (out-of-band)**: Traffic is mirrored to the sensor via a SPAN port or network tap. The sensor cannot block traffic; it can only alert. This is the IDS model.

**Inline**: All traffic flows through the sensor. The sensor can inspect and block in real time. This is the IPS model.

**Risk of inline deployment**: If the inline device fails or is misconfigured, it can block legitimate traffic. This is why IPS devices support a **fail-open** or **fail-closed** configuration:

- **Fail-open**: If the device fails, traffic passes through uninspected. Prioritizes availability.

- **Fail-closed**: If the device fails, all traffic is blocked. Prioritizes security.

**Exam point**: Fail-open prioritizes availability. Fail-closed prioritizes security. The correct choice depends on the environment's risk tolerance.

---

### [SECTION 4 — Network Access Control (NAC) — 9:00]

**NAC (Network Access Control)** enforces security policy before allowing a device to connect to the network.

When a device attempts to connect, NAC performs a **posture assessment**:

- Is the OS patched?

- Is antivirus installed and current?

- Is the device enrolled in MDM?

- Is the device compliant with the security policy?

Devices that pass are placed on the trusted network. Devices that fail are placed in a **quarantine VLAN** where they can only reach remediation resources — Windows Update, AV update servers — until they are compliant.

NAC is a key component of zero-trust's device pillar — it ensures devices are verified before network access is granted.

---

### [SECTION 5 — VPN Architectures — 10:30]

A **VPN (Virtual Private Network)** creates an encrypted tunnel between two endpoints over an untrusted network.

#### Site-to-Site VPN

Connects two network locations (e.g., headquarters to branch office). The VPN gateway at each site handles encryption/decryption. Individual users' devices are unaware of the VPN.

#### Remote Access VPN

Individual users connect to the corporate network from remote locations. The user's device runs a VPN client that creates an encrypted tunnel to the corporate VPN gateway.

**Split tunneling**: Only traffic destined for corporate resources goes through the VPN; internet traffic goes directly to the internet. Reduces bandwidth on the VPN gateway but reduces visibility into the user's internet traffic.

**Full tunneling**: All traffic — including internet traffic — is routed through the corporate VPN gateway. Provides greater visibility and control but increases latency and VPN load.

**Exam trap**: Split tunneling is a security risk because corporate security controls (proxy, web filtering, IPS) are bypassed for internet-bound traffic.

#### IPsec vs. TLS VPN

**IPsec VPN** — operates at Layer 3; encrypts IP packets. Two modes: Transport (encrypts payload only) and Tunnel (encrypts entire IP packet). Used for site-to-site VPNs.

**TLS VPN (SSL VPN)** — operates at Layer 7; uses HTTPS port 443. Easier to traverse firewalls and NAT. Preferred for remote access.

---

### [SECTION 6 — EXAM TRAPS AND QUESTION ANALYSIS — 12:00]

#### Trap 1: IDS vs. IPS Placement

"An organization wants to monitor traffic without the risk of blocking legitimate connections." — IDS (out-of-band, passive).

"An organization wants to automatically block malicious traffic in real time." — IPS (inline).

The words "monitor" and "alert" = IDS. The words "block" and "prevent" = IPS.

#### Trap 2: Implicit Deny

"A new firewall has been configured with three allow rules: permit HTTP, permit HTTPS, permit SSH. A user reports they cannot send email. Why?"

Answer: The implicit deny at the end of the rule list blocks SMTP. No explicit allow rule exists for SMTP.

#### Trap 3: DMZ vs. Internal Placement

"A company runs a web server that must be accessible from the internet and a database server that stores customer data. Where should each be placed?"

Answer: Web server in the DMZ; database server on the internal network. The database server should never be directly exposed to the internet or the DMZ — the web server should query it through a controlled connection permitted by the inner firewall.

#### Trap 4: WAF vs. NGFW

"An organization wants to protect against SQL injection attacks targeting their web application." — WAF.

"An organization wants to block BitTorrent traffic regardless of which port it uses." — NGFW (application-aware).

#### Trap 5: Zero Trust vs. VPN

"An organization wants to replace their broad-access VPN with a solution where users can only access the specific application they are authorized for." — Zero Trust / SDP / ZTNA (Zero Trust Network Access).

Traditional VPN grants network-level access to a subnet. ZTNA grants access to specific applications only.

#### Trap 6: Fail-Open vs. Fail-Closed

"A hospital deploys an inline IPS on the network segment carrying patient monitoring systems. What should the fail behavior be?" — Fail-open. Patient monitoring availability is critical; security can be degraded temporarily rather than blocking clinical traffic.

"A financial transaction processing network deploys an inline IPS. What fail behavior is most appropriate?" — Fail-closed. Security of financial transactions takes priority over availability.

---

### [OUTRO — 15:00]

Network security architecture is about layered defense — no single control is sufficient, and the goal is to make each layer independently valuable so that when one control fails, others remain in place.

Key exam review:

- Firewalls: stateless → stateful → NGFW → WAF. Know the key distinguishing capability of each.

- IDS = detect/alert, out-of-band. IPS = detect/block, inline.

- Signature-based = known attacks. Anomaly-based = unknown attacks, more false positives.

- DMZ = internet-accessible servers isolated from internal network.

- Segmentation = VLANs between zones. Microsegmentation = policy between individual workloads.

- Zero Trust = never trust, always verify; verify identity, device, and access per request.

- VPN: split tunneling reduces visibility; full tunnel preferred for security.

- Implicit deny: all firewalls deny by default; only explicitly permitted traffic passes.

Complete the quiz and lab before moving to Module 08 — Endpoint Security.

---

End of Part 2 — Module 07
