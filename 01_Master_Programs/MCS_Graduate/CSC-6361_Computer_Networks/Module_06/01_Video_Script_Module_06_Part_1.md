# Video Script: Module 06 – Cloud Networking & Hybrid Architectures
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 1 of 2 | Estimated Duration: 15–18 minutes
## Week 6: November 23 – December 1, 2026 (Extended due to Thanksgiving)
## Due: Tuesday, December 1, 2026 at 11:59 PM CST
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CSC-6361 Advanced Computer Networks | Module 06: Cloud Networking & Hybrid Architectures — SD-WAN, VXLAN & EVPN | Texas Wesleyan University | Graduate Level"]

---

### Section 1: Welcome and Thanksgiving Notice

[00:00 – 02:00]
[SHOW SLIDE: Professor Nash on camera, SD-WAN architecture diagram visible behind.]

Welcome to Module 06 of CSC-6361. We are in the final full content module before our capstone week. This module addresses two of the most transformative areas in modern enterprise networking: **SD-WAN** — Software-Defined Wide Area Networking — and **overlay technologies**, specifically VXLAN and EVPN.

Before I begin, an important administrative note: **this module opens Monday, November 23, and Thanksgiving Break runs November 26 through 28**. Because of that break, I have extended all Module 06 deadlines to **Tuesday, December 1 at 11:59 PM CST**. You have two extra days. Please plan accordingly — the research paper and the discussion board are also due on December 1, so do not save everything until December 1 morning.

Now let's get to work.

Part 1 covers the **SD-WAN control plane architecture** — the four Viptela components, the OMP routing protocol, and SD-WAN policy types. Part 1 also covers **VXLAN overlay networking** in depth: VTEP operation, VNI assignment, and BUM traffic handling. Part 2 will cover cloud provider dedicated connectivity (AWS Direct Connect, Azure ExpressRoute) and hybrid routing design patterns. Together, these two lectures represent a substantial portion of the CCNP ENCOR exam's SD-WAN and network infrastructure domains.

Let's begin with SD-WAN.

---

### Section 2: SD-WAN Architecture — The Viptela Control Plane

[02:00 – 07:30]
[SHOW DIAGRAM: Cisco SD-WAN four-component architecture — vManage (management plane), vSmart (control plane), vBond (orchestration plane), vEdge (data plane). Show each component's position and communication paths.]

[Alt-text: A diagram showing four labeled boxes arranged in a layered architecture. At the top: "vManage — Management Plane (HTTPS/NETCONF, centralized policy and monitoring)." Middle left: "vSmart — Control Plane (OMP, policy distribution)." Middle right: "vBond — Orchestration Plane (zero-touch provisioning, authentication)." Bottom: "vEdge/cEdge routers — Data Plane (GRE/IPsec tunnels, BFD, actual traffic forwarding)." Arrows show vManage connects to all components; vSmart connects to vEdge devices via OMP; vBond connects to vEdge devices during onboarding; vEdge-to-vEdge data tunnels bypass the control plane after establishment.]

Cisco's SD-WAN solution — acquired from Viptela in 2017 — separates the WAN into four distinct functional planes. Understanding each plane and its communication protocols is a CCNP ENCOR exam requirement.

**vManage — Management and Policy Plane:**
vManage is the centralized graphical controller. Network operators interact with vManage via a web GUI or REST API to:

- Define configuration templates pushed to all vEdge devices.
- Create and push **centralized policies** (both control and data policies — we will discuss these shortly).
- Monitor real-time device health, tunnel status, and application performance.
- Initiate and validate zero-touch provisioning (ZTP) of new devices.

vManage communicates with vSmart and vEdge devices over a **DTLS (Datagram TLS) or TLS tunnel** using NETCONF for configuration and the SD-WAN control channel.

**vBond — Orchestration and Authentication Plane:**
vBond is the first component a new vEdge device contacts when it comes online. Its two primary functions are:

1. **Mutual authentication** — vBond verifies the device certificate and the device verifies vBond's certificate (using a signed certificate hierarchy from Cisco's PKI infrastructure).
2. **Redirect** — after authentication, vBond provides the vEdge with the addresses of the vSmart controllers and vManage instance to connect to.

> **Key exam point:** vBond must be reachable from the public internet because new vEdge devices use it for zero-touch provisioning. It has a public IP address (unlike vSmart and vManage, which can be in a private network behind NAT, because vBond handles the initial redirect).

**vSmart — Control Plane:**
vSmart is the most critical component for routing and policy. It:

- Maintains a **topology database** of all connected vEdge devices, their WAN transport circuits, and their reachable prefixes.
- Runs **OMP (Overlay Management Protocol)** — the SD-WAN routing protocol — to distribute reachability information to all vEdge devices.
- Distributes **centralized policies** received from vManage to all vEdge devices that need to enforce them.
- Computes and pushes **optimal path selections** to vEdge devices based on policy.

vSmart communicates with vEdge devices using OMP over **DTLS/TLS tunnels**. The vSmart itself is never in the data plane — it does not forward user traffic.

**vEdge / cEdge — Data Plane:**
vEdge devices (Viptela hardware) and cEdge devices (Cisco IOS XE routers running SD-WAN software) are the physical or virtual routers deployed at each site. They:

- Build **IPsec tunnels** directly between each other for data plane traffic (vSmart is NOT involved in forwarding).
- Run **BFD (Bidirectional Forwarding Detection)** on every tunnel to measure loss, latency, and jitter in real time.
- Enforce the **data policies** pushed by vSmart — route matching, DSCP remarking, application-aware routing.
- Connect to one or more **WAN transports** simultaneously (MPLS, broadband internet, LTE — what SD-WAN calls "transports").

> **Graduate Insight:** This architecture scales because vEdge-to-vEdge tunnels are established directly without traversing vSmart. A 500-site SD-WAN has 500 vEdge devices building tunnels to each other (or selectively, based on policy) — vSmart only needs to distribute the routing information once per topology change, not per packet.

---

### Section 3: OMP — Overlay Management Protocol

[07:30 – 10:30]
[SHOW DIAGRAM: OMP route distribution — vEdge-1 advertises prefixes to vSmart, vSmart re-advertises to all other vEdge devices]

[Alt-text: A triangle diagram. At the apex: "vSmart Controller." At the two base corners: "vEdge-HQ" and "vEdge-Branch." Arrows labeled "OMP Updates (TLOC, prefixes, services)" run from each vEdge upward to vSmart. Arrows labeled "OMP re-advertisement" run from vSmart downward to each vEdge. A dashed arrow at the bottom labeled "IPsec data tunnel (established after OMP convergence)" connects vEdge-HQ directly to vEdge-Branch.]

OMP is an SD-WAN proprietary routing protocol that runs between each vEdge device and the vSmart controller. It is not a link-state protocol and not a distance-vector protocol in the traditional sense — it is more analogous to BGP: it uses a session model and carries rich attributes alongside prefixes.

**OMP Route Types:**

OMP carries three types of routing information:

| OMP Route Type | Content | Analogous To |
|---|---|---|
| OMP Routes (vRoutes) | IPv4/IPv6 prefixes reachable at a site | BGP NLRI |
| TLOC Routes | Transport Locator — the WAN IP+transport+color of each vEdge tunnel endpoint | BGP next-hop |
| Service Routes | SD-WAN services available (firewall, IDS) at a site for service chaining | BGP VPN service advertisement |

**TLOC — Transport Locator:**

The TLOC is the triple: `(system-IP, color, encapsulation)`.

- **System-IP:** The vEdge's permanent identity (like a router-ID — never changes, even if WAN IPs change).
- **Color:** A label applied to each WAN transport (e.g., `mpls`, `biz-internet`, `lte`, `public-internet`). Colors allow policies to prefer or avoid specific transports.
- **Encapsulation:** GRE or IPsec — the tunnel type used on this transport.

When a vEdge advertises its prefixes to vSmart via OMP, it includes the TLOC of the next hop. vSmart re-advertises those prefixes with TLOC information to all other vEdge devices. A receiving vEdge now knows: to reach 10.10.10.0/24 at Site B, build an IPsec tunnel to TLOC `(10.10.10.1, biz-internet, ipsec)`.

**OMP Verification Commands:**

```cisco
show sdwan omp peers              ! Show OMP session status to vSmart
show sdwan omp routes             ! Show OMP routing table (vRoutes)
show sdwan omp tlocs              ! Show TLOC table (transport locators)
show sdwan omp services           ! Show service advertisements
```

---

### Section 4: SD-WAN Policies

[10:30 – 13:30]
[SHOW DIAGRAM: Policy flow — vManage pushes policies to vSmart, which pushes to vEdge; centralized vs. localized policy distinction]

SD-WAN has two major policy categories: **centralized policies** and **localized policies**. This distinction appears on the CCNP ENCOR exam.

**Centralized Policies (on vSmart):**

Centralized policies are configured in vManage and pushed to vSmart, which then distributes them to the relevant vEdge devices. There are two types:

**1. Centralized Control Policy:**

Modifies the OMP routing information distributed by vSmart. Think of it as route manipulation at the control plane level — equivalent to BGP route policies on a route reflector.

Use cases:

- **Hub-and-spoke topology enforcement:** Prevent vEdge branches from directly communicating (force all traffic through the HQ hub).
- **Service insertion:** Require all traffic from Branch A to pass through a firewall vEdge at a service node before reaching the destination.
- **TLOC preference:** Prefer MPLS transport for critical sites, use internet only for others.

A centralized control policy does NOT change the forwarding table directly — it changes which OMP routes vSmart advertises to which vEdge devices, which indirectly controls path selection.

**2. Centralized Data Policy:**

Applied directly to data-plane traffic at the vEdge. It is a match/action policy that can:

- Match traffic by **application** (using DPI — Deep Packet Inspection), source/destination prefix, DSCP, or VPN.
- Take actions such as: **set preferred TLOC** (route this traffic over MPLS), **drop**, **count**, **remark DSCP**, or **redirect to a service**.

> **Key Distinction for Exam:** Control policy manipulates which routes exist in the routing table (affects OMP topology). Data policy manipulates how matching packets are forwarded regardless of routing (directly affects packet forwarding decisions). An application-aware routing policy — where video calls are routed over the lowest-latency path — is a **data policy** action.

**Localized Policies (on vEdge):**

Localized policies run on the vEdge device itself and are not distributed via vSmart. Examples:

- **QoS policies** — DSCP classification and queue scheduling on the WAN interface.
- **Access control lists** — filtering traffic at the site.
- **Route policies** — redistributing routes between the SD-WAN overlay and local OSPF/BGP.

---

### Section 5: VXLAN — Virtual Extensible LAN

[13:30 – 17:30]
[SHOW DIAGRAM: VXLAN encapsulation format — inner Ethernet frame, VXLAN header, outer UDP/IP header]

[Alt-text: A layered packet format diagram showing (from innermost to outermost): "Original Layer 2 Frame (Ethernet header + payload)." Then: "VXLAN Header (8 bytes): Flags (8 bits), Reserved (24 bits), VNI — VXLAN Network Identifier (24 bits), Reserved (8 bits)." Then: "Outer UDP Header: Source Port (entropy/hash), Destination Port 4789, Length, Checksum." Then: "Outer IP Header: Source IP = originating VTEP IP, Destination IP = target VTEP IP (or multicast group for BUM)." Then: "Outer Ethernet Header (for transport across L2 underlay if applicable)."]

VXLAN is defined in **RFC 7348** and solves a fundamental limitation of traditional VLAN-based data center networking: the 4,094 VLAN limit and the constraint that Layer 2 segments cannot stretch across Layer 3 boundaries without tunneling.

**VNI — VXLAN Network Identifier:**

The VXLAN header contains a 24-bit VNI field — allowing up to 16 million unique overlay segments (compared to 4,094 VLANs). Each VXLAN segment is logically independent. Hosts in VNI 10001 cannot communicate with hosts in VNI 10002 without inter-VNI routing (a Layer 3 gateway).

**VTEP — VXLAN Tunnel Endpoint:**

A VTEP is any device (physical switch, virtual switch, hypervisor) that performs VXLAN encapsulation and decapsulation. Each VTEP has:

- An **inner (tenant) side:** connects to hosts via normal Ethernet/VLAN interfaces.
- An **outer (underlay) side:** uses a unique IP address (the VTEP IP) for the VXLAN tunnel endpoint.

When a host at VTEP-A sends a frame to a host at VTEP-B:

1. VTEP-A looks up the destination MAC address in its local MAC table — finds it maps to VTEP-B's IP.
2. VTEP-A encapsulates the original Ethernet frame in a VXLAN header (with the destination VNI), then wraps it in a UDP packet (destination port 4789) with source IP = VTEP-A and destination IP = VTEP-B.
3. The underlay IP network routes the outer UDP/IP packet to VTEP-B.
4. VTEP-B decapsulates the VXLAN header and delivers the original Ethernet frame to the destination host.

From the host's perspective, nothing has changed — it sees a normal Layer 2 Ethernet network.

**BUM Traffic — Broadcast, Unknown Unicast, Multicast:**

Traditional Ethernet flooding presents a challenge in VXLAN overlays because the encapsulating VTEP does not always know which VTEP hosts the destination MAC. Two solutions:

| BUM Handling Method | Description | RFC Basis |
|---|---|---|
| **Multicast underlay** | BUM frames are encapsulated and sent to a multicast group. All VTEPs in the segment join the group. | RFC 7348 native recommendation |
| **Ingress replication (head-end)** | The sending VTEP maintains a list of remote VTEP IPs for each VNI and sends a separate unicast copy to each. No multicast required in the underlay. | RFC 8365 (NVO3) |

> **Data Center Design Note:** Ingress replication is the dominant approach in modern data centers because many underlay networks do not support IP multicast. The control plane (EVPN) populates the VTEP list to eliminate the need for flooding entirely.

**VXLAN Verification Commands:**

```cisco
show nve peers                    ! Show VTEP peer table (NX-OS)
show nve vni                      ! Show VNI-to-interface mappings
show mac address-table            ! MAC table (verify overlay MAC learning)
show interfaces nve 1             ! NVE interface stats
```

---

### Section 6: EVPN — Ethernet VPN for VXLAN Control Plane

[17:30 – 20:00]
[SHOW DIAGRAM: EVPN route type overview — Type 2 (MAC/IP), Type 3 (Inclusive Multicast), Type 5 (IP Prefix)]

VXLAN by itself is a data plane technology — it defines how to encapsulate frames. It does not define how VTEPs learn about each other or where remote MAC addresses are located. That is the job of **EVPN — Ethernet VPN**, defined in **RFC 7432**.

EVPN uses BGP (specifically the L2VPN EVPN address family) as a control plane to distribute:

- MAC address reachability (eliminating broadcast-based MAC learning).
- IP address reachability (enabling inter-subnet routing at the VTEP — "distributed anycast gateway").
- VTEP membership (which VTEPs are in which VNI).

**EVPN Route Types (for CCNP ENCOR exam):**

| Type | Name | Purpose |
|---|---|---|
| Type 1 | Ethernet Auto-Discovery | Multi-homing fast convergence |
| Type 2 | MAC/IP Advertisement | Advertises host MAC + IP to remote VTEPs (MAC learning via BGP) |
| Type 3 | Inclusive Multicast Route | Signals VTEP membership in a VNI; used to build BUM replication lists |
| Type 4 | Ethernet Segment Route | Multi-homing designated forwarder election |
| Type 5 | IP Prefix Route | Advertises IP subnets for inter-VNI (inter-subnet) routing |

**Why EVPN Matters for VXLAN:**

Without EVPN, VTEPs learn remote MAC addresses via data plane flooding (BUM). With EVPN:

1. When a host connects to VTEP-A, VTEP-A sends a BGP EVPN **Type 2 route** advertising the host's MAC and IP to all other VTEPs.
2. Other VTEPs install the MAC→VTEP-A mapping directly from BGP — no flooding needed.
3. BUM traffic is reduced to only genuinely unknown destinations (or eliminated entirely with optimal EVPN design).

EVPN with VXLAN — often called **VXLAN-EVPN** — is the standard data center fabric architecture deployed by Cisco, Arista, Juniper, and virtually every modern data center switch vendor.

**EVPN Verification Commands:**

```cisco
show bgp l2vpn evpn               ! View EVPN BGP table
show bgp l2vpn evpn route-type 2  ! MAC/IP advertisement routes
show bgp l2vpn evpn route-type 5  ! IP prefix routes
show evpn evi detail              ! EVPN instance details (NX-OS)
```

---

### Section 7: Part 1 Summary

[20:00 – 21:30]
[SHOW SLIDE: Module 06 Part 1 key concept summary]

In Part 1 you have learned:

- **SD-WAN architecture:** The four Viptela components — vManage (management), vBond (orchestration), vSmart (control), vEdge/cEdge (data plane) — and how they communicate.
- **OMP — Overlay Management Protocol:** The SD-WAN routing protocol, TLOC (transport locator), and vRoute distribution model.
- **SD-WAN policies:** Centralized control policy (manipulates OMP topology) vs. centralized data policy (manipulates packet forwarding). The key distinction that appears on the CCNP exam.
- **VXLAN:** RFC 7348 overlay encapsulation, VTEP operation, VNI (24-bit segment identifier), and BUM traffic handling (multicast vs. ingress replication).
- **EVPN:** RFC 7432 BGP control plane for VXLAN, EVPN route types (especially Type 2 MAC/IP and Type 5 IP Prefix), and why EVPN eliminates data-plane MAC flooding.

In Part 2, we cover **AWS Direct Connect**, **Azure ExpressRoute**, hybrid connectivity design patterns (active/active vs. active/standby), and BGP communities for cloud traffic engineering.

---

### Additional Resources

- IETF RFC 7348 — VXLAN: [https://datatracker.ietf.org/doc/html/rfc7348](https://datatracker.ietf.org/doc/html/rfc7348)
- IETF RFC 7432 — BGP MPLS-Based Ethernet VPN: [https://datatracker.ietf.org/doc/html/rfc7432](https://datatracker.ietf.org/doc/html/rfc7432)
- IETF RFC 8365 — NVO3 Data Plane Requirements: [https://datatracker.ietf.org/doc/html/rfc8365](https://datatracker.ietf.org/doc/html/rfc8365)
- Cisco SD-WAN Design Guide: [https://www.cisco.com/c/en/us/td/docs/solutions/CVD/SDWAN/cisco-sdwan-design-guide.html](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/SDWAN/cisco-sdwan-design-guide.html)
- Cisco Learning Network — CCNP ENCOR Study Hub: [https://learningnetwork.cisco.com/s/encor-study-materials](https://learningnetwork.cisco.com/s/encor-study-materials)

---

End of Part 1 — Module 06
