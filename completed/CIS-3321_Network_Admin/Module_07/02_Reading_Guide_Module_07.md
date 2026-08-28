# Reading Guide: Module 07 — WAN and Cloud Connectivity

## Course: CIS-3321 Network Administration

Certification Alignment: CompTIA Network+ (N10-008)

---

### Introduction

Module 07 expands the course scope from local area networks to wide area connectivity and cloud infrastructure. The CompTIA Network+ exam tests WAN technologies under Domain 1: Networking Concepts and Domain 2: Network Implementation. You must be able to select the appropriate WAN service for a given scenario, distinguish cloud service and deployment models by customer responsibility, and match each VPN technology to its correct use case, port, and protocol. This reading guide organizes all key concepts, comparison tables, and exam tips for the Module 07 video lectures.

---

### 1. Core Vocabulary

WAN (Wide Area Network) — A network that connects sites across cities, countries, or continents using carrier-provided services. WANs span geographic areas too large for LAN technologies.

MPLS (Multiprotocol Label Switching) — A carrier WAN service that forwards packets using short path labels rather than IP addresses. Provides guaranteed Quality of Service (QoS) with defined traffic classes. Runs on dedicated carrier infrastructure, not the public internet.

DSL (Digital Subscriber Line) — Broadband over copper telephone lines. ADSL provides asymmetric speeds (faster download than upload). Best-effort service with no QoS guarantees. Performance degrades with distance from the carrier central office.

Cable / DOCSIS — Broadband over cable television coaxial infrastructure. Bandwidth is shared among neighbors on the same cable segment. Best-effort service.

Metro Ethernet — A carrier service delivering Ethernet connectivity between sites in the same metropolitan area over fiber. High bandwidth (100 Mbps to 10 Gbps) with defined SLAs.

SD-WAN (Software-Defined WAN) — A modern approach using software control to intelligently route traffic across multiple WAN connections based on real-time conditions and application policy.

T1 — A dedicated leased-line circuit providing 1.544 Mbps of fixed bandwidth across 24 DS0 channels. Point-to-point with no sharing.

T3 — A dedicated leased-line circuit providing 44.736 Mbps.

Circuit-Switched — A WAN model where a dedicated path is established on demand for the duration of a session, then released. Example: legacy PSTN and ISDN.

Packet-Switched — A WAN model where data is divided into packets that share network infrastructure. Examples: MPLS, Frame Relay, ATM.

Frame Relay — A legacy packet-switched WAN technology using virtual circuits defined by Committed Information Rate (CIR). Largely replaced by MPLS and Metro Ethernet.

ATM (Asynchronous Transfer Mode) — A legacy cell-switched technology using fixed 53-byte cells. Used in older backbone networks and some DSL infrastructure.

IaaS (Infrastructure as a Service) — Cloud model where the provider delivers virtualized compute, storage, and networking. The customer manages the operating system and above.

PaaS (Platform as a Service) — Cloud model where the provider manages the infrastructure, OS, middleware, and runtime. The customer manages only application code and data.

SaaS (Software as a Service) — Cloud model where the provider manages the complete application. The customer configures settings and uses the software through a browser or client.

Public Cloud — Infrastructure owned and operated by a third-party provider, shared among multiple customers. Examples: AWS, Microsoft Azure, Google Cloud Platform.

Private Cloud — Infrastructure dedicated to a single organization. Provides greater control for regulated industries.

Hybrid Cloud — A combination of public and private cloud environments connected by secure links. Sensitive workloads remain in the private cloud; variable demand bursts to the public cloud.

Community Cloud — Shared infrastructure among organizations with common requirements, such as federal agencies sharing a government-authorized platform.

VPN (Virtual Private Network) — A secure, encrypted logical connection across an untrusted network (typically the public internet) that simulates a private leased-line connection.

IPsec (Internet Protocol Security) — The dominant protocol suite for VPN encryption at Layer 3. Operates in Transport mode or Tunnel mode.

IPsec Transport Mode — Only the IP payload is encrypted. The original IP header remains in plaintext. Used for host-to-host communications.

IPsec Tunnel Mode — The entire original IP packet (header and payload) is encrypted and encapsulated inside a new outer IP packet with VPN gateway addresses. Used for site-to-site VPNs.

AH (Authentication Header) — An IPsec sub-protocol providing authentication and integrity. Does not encrypt the payload.

ESP (Encapsulating Security Payload) — An IPsec sub-protocol providing encryption, authentication, and integrity for the payload. The component that actually encrypts data.

IKE (Internet Key Exchange) — The protocol used to negotiate and establish IPsec security associations. IKEv2 is simplified and more efficient than IKEv1. Uses UDP port 500 for key exchange and UDP port 4500 for NAT traversal (NAT-T).

GRE (Generic Routing Encapsulation) — A Cisco tunneling protocol that encapsulates any network layer protocol inside an IP packet. Provides no encryption. Uses IP Protocol 47. Often combined with IPsec to add encryption.

L2TP (Layer 2 Tunneling Protocol) — A tunneling protocol providing no encryption by itself. Almost always combined with IPsec (L2TP/IPsec) for remote-access VPNs. Uses UDP port 1701.

SSL/TLS VPN — A VPN using Transport Layer Security over TCP port 443. Traverses restrictive firewalls that block IPsec ports. Supports full-tunnel mode, split-tunnel mode, and clientless browser-based mode.

Full-Tunnel VPN — All traffic from the remote device is routed through the VPN tunnel, including general internet browsing. Corporate security controls inspect all traffic.

Split-Tunnel VPN — Only corporate network traffic is routed through the VPN tunnel. Internet traffic goes directly from the user's device. Reduces corporate bandwidth usage but bypasses corporate security for internet-bound traffic.

VPN Concentrator — A dedicated device or software function that terminates multiple VPN client connections at the corporate network edge.

---

### 2. WAN Technology Comparison Table

| Technology | Type | QoS | Bandwidth Typical | Use Case |
|------------|------|-----|-------------------|----------|
| MPLS | Packet-switched (dedicated carrier) | Guaranteed | 1 Mbps – 10 Gbps | Enterprise branch office with VoIP/video |
| DSL/ADSL | Broadband over copper | Best-effort | 1 – 40 Mbps downstream | Small office, home office |
| Cable/DOCSIS | Broadband over coax | Best-effort | 50 – 1000 Mbps | Small office, home office |
| Metro Ethernet | Carrier fiber Ethernet | SLA-defined | 100 Mbps – 10 Gbps | Same-city inter-building connectivity |
| SD-WAN | Software-defined multi-link | Policy-based | Varies | Modern enterprise WAN replacement/supplement |
| T1 Leased Line | Dedicated point-to-point | Dedicated | 1.544 Mbps | Legacy guaranteed-bandwidth circuit |
| T3 Leased Line | Dedicated point-to-point | Dedicated | 44.736 Mbps | Legacy high-bandwidth backbone |

---

### 3. Cloud Service Model Responsibility Table

| Layer | IaaS | PaaS | SaaS |
|-------|------|------|------|
| Physical hardware | Provider | Provider | Provider |
| Hypervisor / Networking | Provider | Provider | Provider |
| Operating System | Customer | Provider | Provider |
| Middleware / Runtime | Customer | Provider | Provider |
| Application code | Customer | Customer | Provider |
| Data | Customer | Customer | Customer |
| Configuration / Settings | Customer | Customer | Customer (limited) |

---

### 4. VPN Protocol Comparison Table

| Protocol | OSI Layer | Encryption | Port or Protocol | Primary Use Case |
|----------|-----------|------------|-----------------|-----------------|
| IPsec | Layer 3 | AES or 3DES | UDP 500 (IKE), UDP 4500 (NAT-T) | Site-to-site and remote-access VPN |
| GRE | Layer 3 | None natively | IP Protocol 47 | Tunnel non-IP or multicast traffic |
| L2TP/IPsec | Layer 2 + 3 | IPsec encryption | UDP 1701 (L2TP) + UDP 500/4500 | Remote-access VPN (legacy OS) |
| SSL/TLS VPN | Layer 4–7 | TLS | TCP 443 | Remote access, clientless browser VPN |

---

### 5. IPsec Modes Comparison

| Feature | Transport Mode | Tunnel Mode |
|---------|---------------|-------------|
| What is encrypted | Payload only | Entire original packet (header + payload) |
| Original IP header | Visible in plaintext | Hidden inside outer packet |
| Outer IP header | Not added | New header with VPN gateway IPs |
| Typical use | Host-to-host encryption | Site-to-site VPN |
| Source/destination IPs visible to transit | Yes | No |

---

### 6. Cloud Deployment Model Comparison

| Model | Owner | Tenancy | Key Characteristic |
|-------|-------|---------|-------------------|
| Public | Third-party provider | Multi-tenant (shared) | Pay-per-use, no capital expense |
| Private | Single organization | Exclusive | Maximum control, higher cost |
| Hybrid | Mixed | Mixed | Combines private security with public elasticity |
| Community | Multiple organizations | Shared among members | Common compliance requirement (HIPAA, FedRAMP) |

---

### 7. Certification Exam Tips

Tip 1: MPLS is the correct answer whenever a scenario requires guaranteed QoS for VoIP, video conferencing, or ERP traffic over a WAN. DSL and cable are best-effort — they cannot guarantee latency.

Tip 2: The IaaS/PaaS/SaaS boundary question is always about customer responsibility. The key phrase is "wants to deploy code without managing servers" — that is PaaS. "Needs to control the OS" — that is IaaS. "Just uses an application" — that is SaaS.

Tip 3: IPsec Tunnel mode is always used for site-to-site VPNs. When the exam says "hide the internal source and destination IP addresses from the transit network," the answer is Tunnel mode. Transport mode leaves the original IP header visible.

Tip 4: GRE provides encapsulation with no encryption. When a scenario says "the GRE tunnel traffic must be protected," the solution is to add IPsec to the GRE tunnel (GRE over IPsec).

Tip 5: SSL/TLS VPN uses TCP 443. This is the answer whenever a scenario describes a restrictive firewall (hotel, coffee shop, guest Wi-Fi) that only allows port 80 and 443. IPsec and L2TP/IPsec use ports that would be blocked.

Tip 6: Split tunneling reduces corporate bandwidth usage but introduces a security risk — internet traffic bypasses corporate security controls. Full tunneling forces all traffic through the corporate firewall but adds latency for internet browsing.

Tip 7: IKE runs over UDP 500. NAT traversal (NAT-T) shifts to UDP 4500 when IPsec endpoints are behind NAT. Both port numbers appear on the exam.

Tip 8: Frame Relay and ATM are legacy technologies that still appear on the Network+ exam for recognition purposes. Frame Relay uses CIR (Committed Information Rate). ATM uses fixed 53-byte cells.

---

### 8. Required Reading and Viewing

Required Reading: Computer Networking: Principles, Protocols and Practice — read the sections on wide area networks, cloud networking, and VPN technologies. Focus on the IPsec protocol suite and the differences between cloud service models.

Required Viewing: Professor Messer's Network+ N10-008 video series — watch the WAN types, cloud concepts, IPsec, and VPN tunneling segments. Available free at professormesser.com.

Supplemental Reference: CompTIA official N10-008 exam objectives — Domain 1.2 (cloud concepts), Domain 2.2 (WAN connectivity), Domain 2.7 (VPN and remote access). Focus on the IPsec modes, VPN protocol ports, and cloud service model boundaries.

---

### 9. Study Checklist

- [ ] Name all five WAN technology types covered in Module 07 and state which provides guaranteed QoS
- [ ] Explain why DSL and cable are classified as best-effort WAN services
- [ ] State the bandwidth of a T1 circuit and explain how it differs from an MPLS service
- [ ] Distinguish IaaS, PaaS, and SaaS by the layer at which customer responsibility begins
- [ ] Name the four cloud deployment models and describe the defining characteristic of each
- [ ] Explain IPsec Transport mode vs. Tunnel mode — what is encrypted, what is visible, and when each is used
- [ ] State the function of AH vs. ESP in the IPsec protocol suite
- [ ] List the port numbers used by IKE and NAT-T for IPsec
- [ ] Explain why GRE is often combined with IPsec and what each protocol contributes
- [ ] State the TCP port used by SSL/TLS VPN and explain why it traverses restrictive firewalls
- [ ] Describe full-tunnel vs. split-tunnel VPN — advantages and security trade-offs of each
- [ ] Explain what a VPN concentrator does and where it is placed in the network
- [ ] Complete Lab 07 and answer all lab questions
- [ ] Post your Module 07 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 07 Quiz

---

## 9. Supplemental Resources

The following free resources extend Module 07 content on network monitoring tools, Wireshark, and SNMP.

**1. Professor Messer — Network Monitoring and Troubleshooting Tools (N10-008)**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer covers SNMP versions, Wireshark, syslog, NetFlow, and packet analysis in videos directly aligned with Network+ exam objectives for this module.

**2. Wireshark Official User Guide (Free)**
URL: https://www.wireshark.org/docs/wsug_html_chunked/
Relevance: The complete free Wireshark documentation including display filter syntax, capture filter syntax, protocol decoding, and follow-stream analysis. The display filter reference appendix is essential for exam questions on Wireshark filter writing.

**3. Cisco — Understanding SNMP**
URL: https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/7282-12.html
Relevance: Cisco's free authoritative documentation explaining SNMP versions, MIBs, OIDs, traps, and community strings. Covers the differences between SNMPv1, v2c, and v3 with configuration examples.

**4. RFC 5424 — The Syslog Protocol**
URL: https://datatracker.ietf.org/doc/html/rfc5424
Relevance: The authoritative IETF syslog protocol standard. Reading Section 6 (Syslog message format) and the severity level definitions (0=Emergency through 7=Debug) is essential for Network+ syslog questions.

**5. NetFlow Protocol Overview — Cisco (Free)**
URL: https://www.cisco.com/c/en/us/products/ios-nx-os-software/ios-netflow/index.html
Relevance: Cisco's free NetFlow product page and documentation explain how NetFlow v5 and v9 work, what data they export, and how flow collectors use the data for traffic analysis — directly relevant to Network+ bandwidth and flow monitoring objectives.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
