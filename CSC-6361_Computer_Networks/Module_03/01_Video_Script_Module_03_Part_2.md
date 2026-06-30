# Video Script: Module 03 – WAN Technologies: MPLS, SD-WAN & VPNs
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 2 of 2 | Estimated Duration: 15–18 minutes
## Week 3: November 2–8, 2026 | Due: Sunday, November 8, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 03 Part 2: SD-WAN Architecture & IPsec VPNs | Texas Wesleyan University"]

---

### Section 1: SD-WAN — Software-Defined Wide Area Networking

[00:00 – 07:00]
[SHOW DIAGRAM: SD-WAN architecture — vManage, vSmart, vBond controllers + vEdge/cEdge devices at branch sites over internet/MPLS/LTE transports]

[Alt-text: A diagram showing the Cisco SD-WAN architecture. At the top is a cloud containing three controller boxes: vManage (management plane), vSmart (control plane), and vBond (orchestration plane). Below the cloud, three branch sites each have a device labeled "vEdge/cEdge" connected upward to the controllers and horizontally to each other via data plane tunnels labeled "IPsec over Internet / MPLS / LTE."]

**What is SD-WAN?**
SD-WAN decouples the WAN **control plane** from the **data plane** and centralizes control in cloud-based controllers. Instead of configuring each router individually and relying on distributed routing protocols to build the WAN, SD-WAN uses a centralized controller to push policies to all edge devices simultaneously.

**Cisco SD-WAN (Viptela) Controller Roles:**

| Controller | Role |
|---|---|
| **vManage** | Management plane — GUI and API, configuration management, monitoring, telemetry |
| **vSmart** | Control plane — distributes routing policies, OMP routes, security policies to all vEdge devices |
| **vBond** | Orchestration plane — initial authentication and NAT traversal for vEdge devices joining the overlay |

**OMP — Overlay Management Protocol:**
The SD-WAN control plane uses **OMP** (Overlay Management Protocol) instead of traditional routing protocols. OMP runs between vEdge devices and the vSmart controller. vSmart distributes OMP routes (TLOCs — Transport Location Identifiers) and policies to all vEdge devices, which then build IPsec tunnels directly to each other.

A **TLOC** identifies a specific transport (color) on a specific device: IP address + color (e.g., `internet`, `mpls`, `biz-internet`, `lte`). This is how SD-WAN knows which physical transport to use for a given flow.

**SD-WAN Key Features:**

**1. Transport Independence:**
SD-WAN can use any combination of transports — MPLS, broadband internet, LTE/5G, MPLS — simultaneously. Traffic is distributed across transports based on application SLA policies.

**2. Application-Aware Routing:**
SD-WAN continuously measures latency, jitter, and packet loss on every transport path. Policies can specify: "If latency on the MPLS path exceeds 20ms, route this application's traffic over the internet path instead."

**3. Centralized Policy:**
A single policy pushed from vManage can control routing, QoS, segmentation, and security across hundreds of sites simultaneously — no CLI on each device.

**4. Zero Trust Security:**
All SD-WAN data plane tunnels are IPsec-encrypted by default. Certificates are distributed by the vBond orchestrator.

**SD-WAN vs. MPLS — When to Use Each:**

| Factor | MPLS | SD-WAN |
|---|---|---|
| Guaranteed QoS | ✅ Native CoS | ✅ Application-aware, but internet QoS varies |
| Transport cost | 💰 High (carrier-managed) | 💰 Lower (can use internet) |
| Deployment complexity | Medium (carrier-provisioned) | Medium (controller-managed) |
| Multi-transport flexibility | ❌ Single transport | ✅ Any transport |
| Application visibility | ❌ Limited | ✅ Deep application awareness |
| Convergence after failure | Minutes (carrier SLA) | Seconds (BFD-driven) |
| Best for | Latency-sensitive apps (voice, trading) at scale | Modern hybrid cloud + multi-site with cost optimization |

> **Graduate Design Reality:** Most enterprise networks today are using **MPLS + SD-WAN in parallel** during a migration phase. SD-WAN can overlay MPLS as just another transport color, allowing a phased transition without a hard cutover.

---

### Section 2: IPsec VPNs — Site-to-Site and Remote Access

[07:00 – 13:00]
[SHOW DIAGRAM: IPsec tunnel mode — original IP packet wrapped in ESP header, new outer IP header]

**IPsec Overview:**
IPsec is a suite of protocols that provides authentication, integrity, and encryption for IP packets. IPsec operates at Layer 3 and is used for both **site-to-site VPNs** (connecting offices) and **remote access VPNs** (connecting individual users).

**IPsec Key Protocols:**
- **IKE (Internet Key Exchange):** Negotiates security associations and exchanges encryption keys. IKEv2 is the current standard.
- **ESP (Encapsulating Security Payload):** Provides encryption + authentication of the payload. The most common IPsec protocol.
- **AH (Authentication Header):** Provides authentication only (no encryption). Rarely used in modern deployments.

**IPsec Modes:**
- **Transport Mode:** Encrypts only the payload; original IP header remains intact. Used for host-to-host communication.
- **Tunnel Mode:** Encrypts the entire original IP packet and adds a new outer IP header. Used for **site-to-site VPNs** — the original packet is completely hidden.

**IKEv2 Phase 1 and Phase 2:**
1. **IKE Phase 1 (IKE_SA_INIT + IKE_AUTH):** Establishes a secure, authenticated channel between the two VPN endpoints. Negotiates encryption algorithms, authentication method (pre-shared key or certificates), and exchanges Diffie-Hellman public keys.
2. **IKE Phase 2 (CREATE_CHILD_SA):** Negotiates the IPsec Security Association — the actual encryption parameters for data traffic.

**Site-to-Site IPsec VPN Configuration (IOS):**
```
! Phase 1 — IKEv2 Proposal
crypto ikev2 proposal SITE-TO-SITE-PROP
 encryption aes-cbc-256
 integrity sha256
 group 14

crypto ikev2 policy SITE-TO-SITE-POL
 proposal SITE-TO-SITE-PROP

! Phase 1 — IKEv2 Keyring (pre-shared key)
crypto ikev2 keyring SITE-B-KEY
 peer SITE-B
  address 203.0.113.2
  pre-shared-key cisco12345

! Phase 2 — IPsec Transform Set
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac
 mode tunnel

! Crypto Map — bind Phase 1 and Phase 2
crypto map SITE-TO-SITE-MAP 10 ipsec-isakmp
 set peer 203.0.113.2
 set transform-set TS
 match address VPN-TRAFFIC

! Apply to WAN interface
interface GigabitEthernet0/0
 crypto map SITE-TO-SITE-MAP
```

**GRE over IPsec vs. Pure IPsec:**
Pure IPsec only encrypts unicast traffic — it cannot carry routing protocol multicast (OSPF, EIGRP hellos). To run a routing protocol over a VPN, wrap GRE (Generic Routing Encapsulation) inside IPsec. GRE creates a virtual tunnel interface that can carry any protocol, and IPsec encrypts the GRE traffic.

---

### Section 3: Module 03 Lab Preview

[13:00 – 15:00]
[SHOW SLIDE: Module 03 Lab Topology]

The Module 03 lab builds a WAN simulation in Packet Tracer:
- **3 sites:** HQ, Branch-A, Branch-B, connected through a simulated ISP cloud.
- Configure **GRE tunnels** between HQ-Branch-A and HQ-Branch-B.
- Configure **IPsec** to encrypt the GRE tunnels (GRE over IPsec).
- Run **OSPF** over the GRE tunnels so all sites learn each other's routes.
- Verify end-to-end encrypted connectivity between all three sites.

**Assignments due: Sunday, November 8, 2026 at 11:59 PM CST**

---
*End of Part 2 — Module 03*
