# Reading Guide: Module 03 – WAN Technologies: MPLS, SD-WAN & VPNs
## CSC-6361 Advanced Computer Networks | Graduate Level
## Week 3: November 2–8, 2026

---

## Learning Objectives
By completing this reading guide, you will be able to:
1. Explain the MPLS forwarding architecture including CE/PE/P roles, label operations (push/swap/pop), and LDP.
2. Describe MPLS L3VPN design using VRF, MP-BGP, Route Distinguishers, and Route Targets.
3. Compare MPLS and SD-WAN on key dimensions: cost, QoS, flexibility, and operational model.
4. Explain SD-WAN controller roles (vManage, vSmart, vBond) and the OMP control plane.
5. Configure and verify GRE over IPsec tunnels and run OSPF across them.
6. Evaluate WAN design choices for a given enterprise scenario.

---

## Required Free Readings

### 1. IETF RFC 3031 — Multiprotocol Label Switching Architecture
**URL:** https://datatracker.ietf.org/doc/html/rfc3031
**Focus:** Section 1 (Introduction & label concept), Section 2 (Terminology), Section 3 (Label switching)
This is the foundational RFC for understanding MPLS. Read it critically — note the distinction between label-based forwarding and IP routing table lookup.

### 2. IETF RFC 4364 — BGP/MPLS IP Virtual Private Networks (L3VPN)
**URL:** https://datatracker.ietf.org/doc/html/rfc4364
**Focus:** Section 1 (Overview), Section 4 (VRF tables), Section 7 (Route Distinguishers and Route Targets)
This RFC defines the enterprise MPLS VPN model. Understanding Section 4 and 7 is essential for CCNP-level MPLS VPN knowledge.

### 3. Cisco SD-WAN Design Guide (Free)
**URL:** https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/index.html
Search for the "Cisco SD-WAN Design Guide" PDF. 
**Focus:** Controller architecture (vManage/vSmart/vBond), OMP protocol, transport locators (TLOCs), application-aware routing policies.

### 4. IETF RFC 7348 — VXLAN: A Framework for Overlaying Virtualized Layer 2 Networks
**URL:** https://datatracker.ietf.org/doc/html/rfc7348
**Focus:** Sections 1–3 — VXLAN as a modern overlay encapsulation (context for SD-WAN overlay concepts).

### 5. Cisco IOS IPsec Configuration Guide (Free)
**URL:** https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_vpnips/configuration/xe-16/sec-sec-for-vpns-w-ipsec-xe-16-book.html
**Focus:** IKEv2 configuration, crypto map configuration, GRE over IPsec tunnel setup.

---

## Key Concepts Reference Card

### MPLS L3VPN — Component Summary
| Component | Purpose |
|---|---|
| **VRF** | Separate routing table per customer/tenant on PE router |
| **RD (Route Distinguisher)** | 64-bit value prepended to IPv4 prefix to make it globally unique in MP-BGP (VPNv4) |
| **RT (Route Target)** | BGP extended community — controls VRF import/export (defines which VRFs receive which routes) |
| **MP-BGP** | Carries VPNv4 routes between PE routers (including label binding for the customer route) |

### SD-WAN vs. MPLS Comparison Table
| Dimension | MPLS | SD-WAN |
|---|---|---|
| Transport | Carrier-managed private circuit | Any IP transport (internet, MPLS, LTE) |
| QoS | Guaranteed (CoS bits in MPLS TC field) | BFD-measured, application-aware (internet QoS best-effort) |
| Cost | High (carrier pricing per Mbps) | Lower (internet broadband + controller licensing) |
| Provisioning | Weeks (carrier circuit order) | Hours-days (zero-touch provisioning) |
| Visibility | Limited (carrier black box) | Full application-level telemetry |
| Security | Inherently private | IPsec encrypted overlays |
| Failure detection | ~seconds (carrier SLA) | Sub-second (BFD over each transport) |

### IPsec Algorithms — Modern Best Practices
| Parameter | Recommended | Avoid |
|---|---|---|
| Encryption | AES-256-GCM | 3DES, DES |
| Integrity/Auth | SHA-256 or SHA-384 | MD5, SHA-1 |
| DH Group | Group 14 (2048-bit) or Group 19/20 (ECDH) | Groups 1, 2, 5 |
| IKE Version | IKEv2 | IKEv1 |

### GRE over IPsec — Why Both?
| Protocol | What it Does | What it Lacks |
|---|---|---|
| Pure IPsec | Encrypts unicast traffic | Cannot carry multicast (routing protocol hellos) |
| GRE alone | Creates a tunnel that carries any protocol including multicast | No encryption |
| GRE + IPsec | GRE carries multicast (routing protocols), IPsec encrypts everything | Slightly higher overhead |

---

## Verification Commands Quick Reference
```
! MPLS
show mpls ldp neighbor              ! Verify LDP peers
show mpls forwarding-table          ! View LFIB (label-to-interface mapping)
show mpls ldp bindings              ! View label bindings in the LIB
show ip bgp vpnv4 all               ! View all VPNv4 routes (on PE router)
show ip vrf                         ! View all VRFs configured on a PE router
show ip route vrf CUSTOMER-A        ! Routing table for a specific VRF

! IPsec / GRE
show crypto ikev2 sa                ! View IKEv2 security associations
show crypto ipsec sa                ! View IPsec SAs (encrypt/decrypt packet counts)
show interface tunnel 0             ! GRE tunnel interface status
show ip ospf neighbor               ! OSPF neighbors over GRE tunnel

! SD-WAN (for reference — not configurable in Packet Tracer)
show sdwan omp tlocs                ! View OMP transport locators
show sdwan omp routes               ! View OMP route table
show sdwan bfd sessions             ! View BFD session state per transport
```

---

## Graduate Discussion Prompt (Due Sunday, November 8, 2026, 11:59 PM CST)

**Scenario:** A manufacturing company with headquarters in Dallas, a factory in Monterrey (Mexico), a distribution center in Atlanta, and a European office in Frankfurt is evaluating its WAN strategy. Currently all four sites are connected via private MPLS from a single carrier at a combined cost of $45,000/month. Circuits are 100 Mbps per site. The CTO wants to cut WAN costs by 50% within 18 months while improving application performance for SaaS apps (Microsoft 365, SAP cloud, Salesforce) that the MPLS circuits currently backhaul to headquarters before reaching the internet.

**Write a graduate-level post (400+ words) addressing:**
1. **Root Cause of the SaaS Performance Problem:** Explain exactly why backhauling SaaS traffic through a headquarters MPLS hub creates latency. What happens at each hop?
2. **SD-WAN as a Solution:** Explain how SD-WAN with local internet breakout (Direct Internet Access/DIA) would solve the SaaS latency problem. What specific SD-WAN feature enables traffic to take different paths based on application type?
3. **Migration Risk Analysis:** The factory in Monterrey relies on the MPLS circuit for real-time machine control systems that are extremely latency-sensitive. How would you handle this site in a phased SD-WAN migration? Would you maintain MPLS at Monterrey while migrating other sites?
4. **The MPLS Parallel Period:** During the transition, you will likely run both MPLS and SD-WAN simultaneously. How does SD-WAN handle the coexistence of MPLS and internet transports? What is a TLOC, and how does it enable this?

**Citation:** Cite RFC 3031 (MPLS) or the Cisco SD-WAN Design Guide, or both.

---

## 9. Supplemental Resources

**1. IETF RFC 4271 — A Border Gateway Protocol 4 (BGP-4)**
https://datatracker.ietf.org/doc/html/rfc4271
BGP is the control plane that carries VPNv4 routes between MPLS PE routers (MP-BGP). Understanding BGP fundamentals — UPDATE messages, path attributes, and session establishment — is essential context for the MPLS L3VPN model described in RFC 4364.

**2. Cisco DMVPN Design and Implementation Guide (Free)**
https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/WAN_and_MAN/DMVPN/DMVPN_2.html
DMVPN (Dynamic Multipoint VPN) extends the GRE/IPsec concepts from this module into a scalable hub-and-spoke design where branch-to-branch tunnels build dynamically without pre-configuration. Understanding DMVPN Phase 1, 2, and 3 represents the production evolution of the static GRE topology built in this module's lab.

**3. IETF RFC 5996 — Internet Key Exchange Protocol Version 2 (IKEv2)**
https://datatracker.ietf.org/doc/html/rfc5996
IKEv2 is the modern replacement for IKEv1/ISAKMP configured in the lab. This RFC defines the complete IKEv2 exchange — understanding the differences between IKEv1 and IKEv2 (fewer round trips, built-in EAP support, mobility/multihoming extensions) is directly tested on the CCNP ENCOR exam.
