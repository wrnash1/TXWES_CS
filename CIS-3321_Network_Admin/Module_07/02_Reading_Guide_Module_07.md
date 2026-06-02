# Reading Guide: Module 07 – WAN and Cloud Connectivity

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 07 bridges local area networking and the broader infrastructure that connects sites, remote users, and cloud services. The CompTIA Network+ exam tests WAN technology identification, cloud service model boundaries (IaaS/PaaS/SaaS), and VPN protocol selection. You must be able to match a business scenario to the correct WAN type, identify the cloud model that best fits a given responsibility requirement, and select the correct VPN protocol for a given network constraint (such as a firewall that blocks all but port 443).

---

### 1. Core Vocabulary

**WAN (Wide Area Network)** — A network spanning a large geographic area, typically using carrier-provided services to connect sites in different cities or countries.

**MPLS (Multiprotocol Label Switching)** — A carrier WAN service that routes packets using short labels rather than IP addresses, enabling traffic engineering and guaranteed QoS. Used for enterprise branch connectivity requiring predictable latency.

**DSL (Digital Subscriber Line)** — Broadband internet over copper telephone lines. ADSL (Asymmetric DSL) provides faster download than upload. Best-effort service; no QoS guarantees. Distance-limited from the carrier's central office.

**ADSL** — Asymmetric DSL. Download speeds are faster than upload speeds. Typical residential and small office WAN connection type.

**DOCSIS (Data Over Cable Service Interface Specification)** — The standard for delivering broadband internet over cable television coaxial infrastructure. Bandwidth is shared among subscribers on the same cable segment. Best-effort service.

**Metro Ethernet** — A carrier service delivering high-bandwidth Ethernet connectivity between sites in the same metropolitan area over fiber infrastructure. Provides defined SLAs. The customer interface is a standard Ethernet port.

**SD-WAN (Software-Defined WAN)** — An overlay technology that uses software control to dynamically route traffic across multiple WAN links (MPLS, internet, LTE) based on application policy and real-time link conditions.

**T1** — A dedicated digital circuit providing 1.544 Mbps across 24 DS0 channels. A leased-line WAN technology providing fixed, guaranteed bandwidth.

**T3** — A dedicated digital circuit providing 44.736 Mbps across 28 T1 channels. Higher-capacity leased-line option.

**Frame Relay** — A legacy packet-switched WAN technology using virtual circuits and committed information rates (CIR). Largely replaced by MPLS. Still exam-relevant for recognition.

**ATM (Asynchronous Transfer Mode)** — A legacy cell-switched technology using fixed 53-byte cells. Used in older WAN backbones and some DSL infrastructure. Exam-relevant for recognition.

**CIR (Committed Information Rate)** — The guaranteed minimum bandwidth on a Frame Relay virtual circuit.

**VPN (Virtual Private Network)** — A secure, encrypted logical connection over an untrusted network (typically the internet) that simulates a private leased-line connection.

**Site-to-Site VPN** — Connects two entire networks. VPN gateways at each site establish the tunnel; end-user devices need no VPN software.

**Remote-Access VPN** — Connects an individual user's device to a corporate network. Requires a VPN client on the user's device.

**IPsec (Internet Protocol Security)** — A Layer 3 protocol suite for authenticating and encrypting IP packets. Used for site-to-site and remote-access VPNs.

**IPsec Transport Mode** — Encrypts only the IP payload; leaves the original IP header (source and destination addresses) in plaintext. Used for host-to-host encryption.

**IPsec Tunnel Mode** — Encrypts the entire original IP packet (header + payload) and wraps it in a new outer IP header using VPN gateway addresses. Used for site-to-site VPNs. Hides internal IP addresses from the transit network.

**AH (Authentication Header)** — An IPsec sub-protocol providing authentication and integrity. Does not encrypt the payload.

**ESP (Encapsulating Security Payload)** — An IPsec sub-protocol providing encryption, authentication, and integrity for the payload. The standard choice for VPN encryption.

**IKE (Internet Key Exchange)** — The protocol that negotiates IPsec security associations. IKEv1 uses two phases; IKEv2 is more efficient. Uses UDP port 500; NAT traversal uses UDP port 4500.

**GRE (Generic Routing Encapsulation)** — A tunneling protocol that encapsulates any network layer protocol inside an IP packet. Provides no encryption. Uses IP Protocol 47 (not TCP or UDP). Often combined with IPsec to add encryption.

**L2TP (Layer 2 Tunneling Protocol)** — A tunneling protocol that encapsulates Layer 2 frames. Provides no encryption by itself. Almost always deployed as L2TP/IPsec, where IPsec provides encryption. Uses UDP port 1701.

**SSL/TLS VPN** — A VPN that uses TLS encryption and operates over TCP port 443. Traverses restrictive firewalls that allow only HTTPS. Supports full-tunnel, split-tunnel, and clientless browser-based modes.

**Split Tunneling** — A VPN configuration where only corporate-bound traffic routes through the VPN tunnel; other internet traffic goes directly to the internet. Reduces corporate bandwidth load but bypasses corporate security controls.

**Full Tunnel** — A VPN configuration where all traffic routes through the VPN, including general internet browsing. All traffic is inspected by corporate security controls.

**VPN Concentrator** — A dedicated device that terminates multiple remote-access VPN sessions at the corporate network edge.

**IaaS (Infrastructure as a Service)** — Cloud service model where the provider delivers compute, storage, and networking. The customer manages OS and everything above.

**PaaS (Platform as a Service)** — Cloud service model where the provider manages infrastructure, OS, and runtime. The customer manages only the application and data.

**SaaS (Software as a Service)** — Cloud service model where the provider manages and delivers a complete application. The customer configures settings and uses the software.

**Public Cloud** — Cloud infrastructure owned by a third-party provider and shared among multiple customers (multi-tenant).

**Private Cloud** — Cloud infrastructure dedicated to a single organization. Provides greater control and security.

**Hybrid Cloud** — A combination of public and private cloud environments connected by secure links.

**Community Cloud** — Cloud infrastructure shared among organizations with common compliance, mission, or regulatory requirements.

---

### 2. WAN Technology Comparison Table

| Technology | Type | Bandwidth | QoS Guarantee | Best For |
|------------|------|-----------|---------------|----------|
| MPLS | Packet-switched carrier | 10 Mbps – 10 Gbps | Yes — defined traffic classes | Enterprise branch, VoIP, video |
| DSL (ADSL) | Broadband (copper) | Up to ~100 Mbps | No — best effort | Small office, home office |
| Cable/DOCSIS | Broadband (coax) | Up to 1 Gbps | No — shared/best effort | Small office, home office |
| Metro Ethernet | Carrier Ethernet (fiber) | 100 Mbps – 10 Gbps | Yes — defined SLA | Intra-city multi-site |
| T1 Leased Line | Dedicated point-to-point | 1.544 Mbps | Yes — dedicated | Critical single-site uplinks |
| T3 Leased Line | Dedicated point-to-point | 44.736 Mbps | Yes — dedicated | High-capacity site links |
| SD-WAN | Overlay (multiple links) | Variable | Policy-based | Modern enterprise WAN |
| Frame Relay | Packet-switched (legacy) | Variable (CIR) | CIR guaranteed | Legacy — exam recognition only |

---

### 3. Cloud Service Model Responsibility Table

| Layer | IaaS | PaaS | SaaS |
|-------|------|------|------|
| Application | Customer | Customer | Provider |
| Runtime/Middleware | Customer | Provider | Provider |
| Operating System | Customer | Provider | Provider |
| Virtualization | Provider | Provider | Provider |
| Physical Hardware | Provider | Provider | Provider |
| Data | Customer | Customer | Customer |

Key rule: In IaaS, the customer manages OS and above. In PaaS, the customer manages application and data only. In SaaS, the customer only configures and uses.

---

### 4. Cloud Deployment Model Comparison

| Model | Who Owns Infrastructure | Shared | Security/Control | Use Case |
|-------|------------------------|--------|-----------------|----------|
| Public | Third-party provider | Multi-tenant | Lower control | General workloads, startups |
| Private | Organization | Single-tenant | Highest control | Regulated industries |
| Hybrid | Both | Mixed | Balanced | Sensitive + variable workloads |
| Community | Shared group | Group members | Shared controls | Government, healthcare consortiums |

---

### 5. VPN Protocol Comparison Table

| Protocol | Layer | Encryption | Ports/Protocol | Site-to-Site | Remote Access |
|----------|-------|------------|----------------|-------------|---------------|
| IPsec Tunnel | 3 | AES/3DES (ESP) | UDP 500, UDP 4500 (NAT-T) | Yes | Yes |
| IPsec Transport | 3 | AES/3DES (ESP) | UDP 500 | No | Host-to-host only |
| GRE | 3 | None | IP Protocol 47 | Yes (no encryption) | No |
| GRE over IPsec | 3 | IPsec ESP | IP 47 + UDP 500/4500 | Yes | No |
| L2TP/IPsec | 2+3 | IPsec ESP | UDP 1701, UDP 500/4500 | No | Yes |
| SSL/TLS VPN | 4–7 | TLS | TCP 443 | No | Yes |
| PPTP | 2 | MPPE (weak) | TCP 1723, GRE 47 | No | Legacy only |

---

### 6. IPsec Mode Comparison

| Feature | Transport Mode | Tunnel Mode |
|---------|---------------|-------------|
| What is encrypted | Payload only | Entire original packet (header + payload) |
| Original IP header | Visible (plaintext) | Hidden (encrypted inside outer packet) |
| Outer IP header | Uses original source/destination | Uses VPN gateway addresses |
| Use case | Host-to-host encryption | Site-to-site VPN |
| Internal addresses visible | Yes | No |

---

### 7. Certification Exam Tips

Tip 1: MPLS provides guaranteed QoS — it is the correct answer when a scenario requires predictable latency for VoIP or video over a WAN. DSL and cable are best-effort.

Tip 2: IPsec Tunnel mode is used for site-to-site VPNs and hides the original IP header. Transport mode is used for host-to-host and leaves the original IP header visible. This distinction is directly tested.

Tip 3: SSL/TLS VPN uses TCP 443. When the exam describes a firewall that allows only port 80 and 443, and a remote user needs VPN access, the answer is SSL/TLS VPN. IPsec and L2TP require ports that would be blocked.

Tip 4: GRE by itself provides no encryption. GRE is purely an encapsulation mechanism. When combined with IPsec, the combination provides both encapsulation of multiprotocol traffic and encryption.

Tip 5: PaaS is the cloud model where developers deploy code without managing virtual machines or OS. The boundary: customer manages application + data only. IaaS requires OS management. SaaS provides a pre-built application.

Tip 6: Full-tunnel VPN routes all traffic through the corporate network, including internet browsing. Split-tunnel sends only corporate traffic through the VPN. Full-tunnel provides more security but uses more corporate bandwidth.

Tip 7: Frame Relay and ATM are legacy WAN technologies. They appear on the exam for identification only — you need to recognize what they are, not configure them.

Tip 8: Private cloud provides the highest control and security but requires capital investment. Public cloud provides elasticity and pay-per-use but requires trust in provider isolation. Hybrid combines both.

---

### 8. Required Reading and Viewing

Required Reading: Computer Networking: Principles, Protocols and Practice — read the sections on WAN technologies and VPNs. Focus on the IPsec protocol suite and SSL/TLS tunneling mechanisms.

Required Viewing: Professor Messer's Network+ N10-008 video series — watch the WAN technologies, cloud computing models, and VPN technologies segments. Available free at professormesser.com.

Supplemental Reference: CompTIA official N10-008 exam objectives at comptia.org — review Domain 1.0 Network Fundamentals for WAN and cloud objectives and Domain 4.0 Network Security for VPN objectives.

---

### 9. Study Checklist

- [ ] Identify each WAN technology (MPLS, DSL, cable, Metro Ethernet, T1/T3) by type, speed, and QoS capability
- [ ] Explain why MPLS is preferred over DSL/cable for enterprise VoIP connectivity
- [ ] Distinguish IaaS, PaaS, and SaaS by customer responsibility boundary
- [ ] Identify the four cloud deployment models and their use cases
- [ ] Explain the difference between IPsec Tunnel mode and Transport mode — what each encrypts and when each is used
- [ ] Explain why SSL/TLS VPN traverses restrictive firewalls when IPsec and L2TP cannot
- [ ] Define GRE — what it encapsulates, what it does not provide, and its IP protocol number
- [ ] Explain split tunneling vs. full tunneling — the security and bandwidth tradeoffs of each
- [ ] Watch Professor Messer's WAN, cloud, and VPN segments at professormesser.com
- [ ] Complete the Lab 07 VPN and WAN connectivity exercises
- [ ] Post your Module 07 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 07 Quiz

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
