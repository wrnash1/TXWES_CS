# Reading Guide: Module 06 – Cloud Networking & Hybrid Architectures

## CSC-6361 Advanced Computer Networks | Graduate Level

## Week: Nov 23 – Dec 1, 2026 | Due: Tuesday, December 1, 2026 (Extended — Thanksgiving Week)

---

## Learning Objectives

By completing this reading guide, you will be able to:

1. Describe the four-component Cisco SD-WAN (Viptela) architecture — vManage, vBond, vSmart, and vEdge/cEdge — and explain the role each plays in the management, orchestration, control, and data planes.
2. Differentiate centralized control policy from centralized data policy in SD-WAN, and construct an example use case for each using OMP TLOC attributes and application-aware routing.
3. Explain VXLAN encapsulation (RFC 7348) including the VNI field, VTEP operation, outer UDP/IP header format, and BUM traffic handling via multicast underlay vs. ingress replication.
4. Identify EVPN BGP route types (RFC 7432) Type 1 through Type 5 and explain how Type 2 MAC/IP advertisements and Type 5 IP Prefix routes enable control-plane-based MAC learning and inter-subnet routing in a VXLAN fabric.
5. Compare AWS Direct Connect Virtual Interface types (Private VIF, Public VIF, Transit VIF) and Azure ExpressRoute peering types (Private Peering, Microsoft Peering) including their routing models and appropriate use cases.
6. Design a hybrid WAN connectivity solution using BGP communities, AS path prepending, and local preference to implement active/active or active/standby path selection between on-premise infrastructure and cloud providers.

---

## Required Free Readings

### 1. IETF RFC 7348 — Virtual eXtensible Local Area Network (VXLAN)

**URL:** [https://datatracker.ietf.org/doc/html/rfc7348](https://datatracker.ietf.org/doc/html/rfc7348)

Focus sections:

- Section 1: Problem Statement (why VLAN 4094 limit matters at cloud scale)
- Section 4: VXLAN Frame Format (the complete encapsulation breakdown — memorize this for the exam)
- Section 4.1: VTEP Behavior (encapsulation/decapsulation logic)
- Section 4.2: BUM Traffic Handling (multicast group approach)

**Graduate Reading Note:** Pay attention to the "MUST," "SHOULD," and "MAY" language (RFC 2119 normative levels). The destination UDP port 4789 is a MUST. The source port as a hash for ECMP is a SHOULD — this is how VXLAN achieves load balancing across equal-cost underlay paths.

### 2. IETF RFC 7432 — BGP MPLS-Based Ethernet VPN (EVPN)

**URL:** [https://datatracker.ietf.org/doc/html/rfc7432](https://datatracker.ietf.org/doc/html/rfc7432)

Focus sections:

- Section 5: BGP EVPN NLRI (the route types — understand the encoding)
- Section 7: MAC/IP Advertisement Route (Type 2 — the most important route type)
- Section 3: Terminology (EVPN Instance, ES, EVI — learn these definitions)

### 3. IETF RFC 8365 — A Network Virtualization Overlay Solution Using EVPN (NVO3)

**URL:** [https://datatracker.ietf.org/doc/html/rfc8365](https://datatracker.ietf.org/doc/html/rfc8365)

Focus sections:

- Section 4: Ingress Replication (the alternative to multicast BUM — understand why this is the dominant approach in cloud environments)
- Section 6: EVPN-VXLAN Control Plane (how EVPN Type 3 routes build the ingress replication list)

### 4. Cisco SD-WAN Design Guide (Free)

**URL:** [https://www.cisco.com/c/en/us/td/docs/solutions/CVD/SDWAN/cisco-sdwan-design-guide.html](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/SDWAN/cisco-sdwan-design-guide.html)

**Focus:** Chapter 2 (Architecture Overview — vManage/vSmart/vBond/vEdge roles), Chapter 4 (Policies — control policy vs. data policy), Chapter 6 (SD-WAN Cloud OnRamp for IaaS)

### 5. AWS Direct Connect User Guide (Free)

**URL:** [https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

**Focus:** "Virtual Interfaces" section (Private VIF, Public VIF, Transit VIF), "Link Aggregation Groups," "BGP Communities for Direct Connect"

### 6. Cisco Learning Network — CCNP ENCOR Study Materials

**URL:** [https://learningnetwork.cisco.com/s/encor-study-materials](https://learningnetwork.cisco.com/s/encor-study-materials)

**Focus:** Review the SD-WAN and Infrastructure sections of the CCNP ENCOR 350-401 exam blueprint. SD-WAN components and policies have appeared heavily on recent exam versions.

---

## Key Concepts to Master

### SD-WAN Component Reference Table

| Component | Plane | Protocol | Reachability Requirement |
|---|---|---|---|
| vManage | Management | HTTPS, NETCONF, REST API | Private or public (NMS access needed) |
| vBond | Orchestration | DTLS/TLS | **Must be publicly reachable** — ZTP requires it |
| vSmart | Control | OMP over DTLS/TLS | Private OK (vBond redirects vEdge to it) |
| vEdge / cEdge | Data | IPsec/GRE, BFD, OMP | Public WAN interface per transport |

### VXLAN Encapsulation Format (RFC 7348) — Field by Field

```text
Outer Ethernet Header
  Destination MAC: Next-hop MAC (underlay)
  Source MAC: VTEP MAC
Outer IP Header
  Source IP:      VTEP-A IP (tunnel source)
  Destination IP: VTEP-B IP (unicast) or multicast group (BUM)
  Protocol:       UDP (17)
Outer UDP Header
  Source Port:    Hashed from inner frame (entropy for ECMP)
  Dest Port:      4789 (IANA-assigned VXLAN port)
VXLAN Header (8 bytes)
  Flags:          I-bit set (VNI present)
  VNI:            24-bit VXLAN Network Identifier (up to 16M segments)
  Reserved:       Must be zero
Inner Ethernet Frame
  Original Layer 2 frame from tenant host
```

The 50-byte overhead (14 outer Ethernet + 20 outer IP + 8 UDP + 8 VXLAN) means jumbo frames (MTU 9000) are highly recommended in the underlay to prevent VXLAN fragmentation.

### EVPN Route Types — Reference Card

| Type | Name | Key Fields | Primary Use |
|---|---|---|---|
| 1 | Ethernet Auto-Discovery | ESI, Ethernet Tag | Multi-homing fast convergence and aliasing |
| 2 | MAC/IP Advertisement | MAC, IP (optional), VTEP NLRI | Remote MAC learning; ARP suppression |
| 3 | Inclusive Multicast Ethernet Tag | Originating IP (VTEP IP) | VTEP membership in VNI; ingress replication list |
| 4 | Ethernet Segment | ESI, Originating Router IP | Designated Forwarder election for multi-homing |
| 5 | IP Prefix | IP prefix, GW IP | Inter-subnet routing (L3 VNI); replaces Type 2 for prefixes |

> **CCNP Exam Focus:** Type 2 and Type 5 appear most frequently. Type 2 is used for host routes (MAC + IP) and enables ARP suppression — the VTEP answers ARP requests locally from the BGP EVPN table instead of flooding. Type 5 is used for IP prefix routes in L3VNI deployments for inter-tenant routing.

### Cloud Connectivity Comparison Table

| Feature | AWS Direct Connect | Azure ExpressRoute | GCP Cloud Interconnect |
|---|---|---|---|
| Circuit speeds | 1G, 10G (hosted: 50M–500M) | 50M to 100G | 10G, 100G (partner: 50M–10G) |
| Routing protocol | BGP | BGP | BGP |
| Private connectivity | Private VIF → VGW | Private Peering → ExpressRoute GW | Dedicated/Partner Interconnect → Cloud Router |
| Public service access | Public VIF | Microsoft Peering (route filters required) | Partner Interconnect to Google APIs |
| Transit connectivity | Transit VIF + Transit Gateway | ExpressRoute + vWAN or Global Reach | Cloud Router + VPC peering |
| Built-in redundancy | Manual (provision 2 circuits) | Automatic (primary + secondary MSEE) | Manual (provision 2 circuits) |
| BGP community filtering | Yes (AWS 7224:9xxx outbound control) | Yes (12076:5xxxx regional, required for MS Peering) | Limited |

### SD-WAN Policy Types — Decision Framework

Use **Centralized Control Policy** when you want to:

- Create a hub-and-spoke topology (prevent direct spoke-to-spoke OMP routes).
- Insert a firewall service node in the path (service chaining via OMP manipulation).
- Prefer specific TLOCs (transport colors) for specific sites — controls what the routing table contains.

Use **Centralized Data Policy** when you want to:

- Route specific applications (identified by DPI) over a preferred transport — application-aware routing.
- Drop, count, or mirror specific traffic flows.
- Set DSCP values for QoS marking at the edge.
- Direct traffic to a cloud security proxy (Zscaler, Umbrella) for internet-bound traffic.

---

## Verification Commands Reference

Practice these commands until they are second nature:

SD-WAN Verification (IOS XE SD-WAN CLI):

```cisco
show sdwan omp peers              ! OMP session status to vSmart (should be ESTABLISHED)
show sdwan omp routes             ! OMP vRoute table — prefixes learned via OMP
show sdwan omp tlocs              ! TLOC table — transport locators for all sites
show sdwan bfd sessions           ! BFD session table — tunnel liveness and quality metrics
show sdwan tunnel statistics      ! Per-tunnel packet/byte counters, loss, latency, jitter
show sdwan policy from-vsmart     ! Policies pushed from vSmart (centralized policies)
show interfaces tunnel            ! Tunnel interface status and encapsulation
```

VXLAN/NVE Verification (NX-OS):

```cisco
show nve peers                    ! Remote VTEP peer table — IP, VNI, state
show nve vni                      ! VNI table — VLAN-to-VNI mappings, ingress replication mode
show bgp l2vpn evpn               ! EVPN BGP table — all route types
show bgp l2vpn evpn route-type 2  ! MAC/IP advertisement routes only
show bgp l2vpn evpn route-type 5  ! IP prefix routes only
show mac address-table dynamic    ! MAC table — verify EVPN-learned remote MACs present
```

---

## Graduate Discussion Prompt

Due: Tuesday, December 1, 2026 at 11:59 PM CST

See the Module 06 Discussion Board for the full scenario prompt covering SD-WAN design decisions and hybrid cloud connectivity trade-offs.

---

## Supplemental Resources

### 1. Cisco SD-WAN Design Guide — Comprehensive Reference

[https://www.cisco.com/c/en/us/td/docs/solutions/CVD/SDWAN/cisco-sdwan-design-guide.html](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/SDWAN/cisco-sdwan-design-guide.html)

Authoritative design reference covering vManage/vSmart/vBond architecture, OMP protocol, policy configuration, and cloud integration. The Chapter 4 policy section directly maps to CCNP ENCOR exam topics.

### 2. AWS Direct Connect Documentation

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

Official AWS documentation covering VIF types, LAG configuration, and BGP community usage. The "Routing Policies and BGP Communities" section is essential exam reading.

### 3. IETF RFC 7348 — VXLAN

[https://datatracker.ietf.org/doc/html/rfc7348](https://datatracker.ietf.org/doc/html/rfc7348)

Original VXLAN specification. Read Sections 1 and 4 in full — this RFC is short (19 pages) and entirely accessible at the graduate level.

### 4. IETF RFC 7432 — BGP MPLS-Based Ethernet VPN

[https://datatracker.ietf.org/doc/html/rfc7432](https://datatracker.ietf.org/doc/html/rfc7432)

The EVPN specification. Focus on Sections 3 (terminology), 5 (NLRI formats), and 7 (Type 2 MAC/IP routes).

### 5. Cisco DevNet — SD-Access Learning Tracks

[https://developer.cisco.com/learning/modules/dnac-1/](https://developer.cisco.com/learning/modules/dnac-1/)

Hands-on labs for Cisco DNA Center and SD-Access, covering VXLAN-LISP campus fabric — complements the SD-WAN material with the campus overlay perspective.
