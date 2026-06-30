# Video Script: Module 03 – WAN Technologies: MPLS, SD-WAN & VPNs
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 1 of 2 | Estimated Duration: 15–18 minutes
## Week 3: November 2–8, 2026 | Due: Sunday, November 8, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 03 Part 1: WAN Technologies — MPLS & Label Switching | Texas Wesleyan University | Graduate Level"]

---

### Section 1: The WAN Problem

[00:00 – 02:00]
[SHOW SLIDE: Enterprise WAN — headquarters + 10 branch offices connected over carrier network]

Welcome to Module 03. We have built a routed campus (Module 01) and a switched campus (Module 02). Now we need to connect multiple campuses together across a **Wide Area Network (WAN)**. The WAN is the carrier-managed infrastructure between your sites.

At CCNP level, WAN knowledge means understanding three foundational technologies: **MPLS** (the traditional enterprise WAN workhorse), **SD-WAN** (the modern software-defined replacement), and **VPNs** (the overlay technology that provides private connectivity over public infrastructure). Let's start with MPLS.

---

### Section 2: MPLS — Multiprotocol Label Switching

[02:00 – 08:00]
[SHOW DIAGRAM: MPLS network — CE routers at customer sites, PE routers at provider edge, P routers in provider core]

[Alt-text: A network diagram showing two customer sites. Site A has a router labeled "CE-A (Customer Edge)." Site B has a router labeled "CE-B." Between them is a cloud labeled "MPLS Provider Network" containing: two routers labeled "PE-A" and "PE-B" (Provider Edge) connected to the CE routers, and two interior routers labeled "P-1" and "P-2" (Provider core). Labels on packets are shown being added at PE-A and removed at PE-B.]

**What is MPLS?**
MPLS is a high-performance packet-forwarding technology that assigns **short fixed-length labels** to packets and switches them based on those labels — rather than performing a full IP routing table lookup at every hop. This makes MPLS core routers (P routers) extremely fast.

**MPLS Key Roles:**
- **CE (Customer Edge):** The customer's router at the edge of the MPLS network. The CE peers with the PE router using standard routing protocols (BGP, OSPF, EIGRP, or static).
- **PE (Provider Edge):** The carrier's router that sits between the customer and the MPLS core. The PE adds MPLS labels to incoming packets (push operation) and removes them before delivery to the destination CE (pop operation). The PE is responsible for VPN routing using **MP-BGP (Multiprotocol BGP)**.
- **P (Provider Core):** Interior carrier routers. P routers only look at the MPLS label — they never inspect the IP header. This is the source of MPLS speed.

**MPLS Label Operations:**
| Operation | Description | Where |
|---|---|---|
| Push | Add a label to the packet | Ingress PE |
| Swap | Replace the current label with a new label | P routers |
| Pop | Remove the label | Egress PE (or penultimate P — Penultimate Hop Popping) |

**The MPLS Label Stack:**
An MPLS label is a 32-bit field inserted between the Layer 2 (Ethernet) header and the Layer 3 (IP) header. The label stack can have multiple labels (label stacking is used for MPLS VPNs and Traffic Engineering).

Label fields:
- **Label Value:** 20 bits (0–1,048,575).
- **TC (Traffic Class):** 3 bits — used for QoS/CoS marking.
- **S (Stack Bottom bit):** 1 bit — set to 1 on the bottom label of the stack.
- **TTL:** 8 bits — decremented at each hop like IP TTL.

**MPLS LDP — Label Distribution Protocol:**
MPLS uses **LDP (Label Distribution Protocol)** to distribute labels between routers. Each router assigns a label to each IP prefix in its routing table and advertises those label bindings to neighbors via LDP. This creates the **Label Information Base (LIB)** and the **Label Forwarding Information Base (LFIB)** on each router.

```
! Verify LDP neighbors
show mpls ldp neighbor

! View the LFIB (label forwarding table)
show mpls forwarding-table

! View IP routes with MPLS label information
show ip route
```

**MPLS VPN (RFC 4364 — Layer 3 VPN):**
The most common enterprise MPLS use case is **MPLS L3VPN**. This allows a carrier to provide private IP connectivity between multiple customer sites, even when those sites use overlapping IP address space (RFC 1918 private addresses).

MPLS VPN uses **VRF (Virtual Routing and Forwarding)** on PE routers to separate customer routing tables. Each customer gets their own VRF. Routes are distributed between PE routers using **MP-BGP** with **VPNv4 address families** — which prepend a **Route Distinguisher (RD)** to make otherwise identical customer routes globally unique within the carrier's BGP.

**Route Targets (RT):**
While RDs make routes unique, **Route Targets** control which routes are imported/exported between VRFs, enabling flexible topologies (hub-and-spoke, full mesh, extranet).

---

### Section 3: MPLS Traffic Engineering (TE)

[08:00 – 11:00]
[SHOW DIAGRAM: MPLS TE tunnel bypassing congested path]

Standard IP routing always uses the shortest path. **MPLS Traffic Engineering** allows you to route traffic along an explicitly specified path — even if that path is not the shortest — to avoid congestion or meet SLA requirements.

MPLS TE uses **RSVP-TE** (Resource Reservation Protocol — Traffic Engineering) to signal the path and reserve bandwidth. A configured **TE tunnel** appears as a virtual interface and can be used with OSPF/IS-IS TE extensions for automatic path calculation.

**When would you use MPLS TE?**
- A carrier needs to balance load across redundant fiber paths.
- A customer SLA requires that video traffic takes a low-latency path even if a shorter path exists.
- Fast reroute (FRR) is needed — MPLS FRR can switch to a pre-computed backup path in under 50ms, faster than any IGP convergence.

---

### Section 4: Part 1 Summary

[11:00 – 12:30]
[SHOW SLIDE: MPLS key terms summary table]

In Part 1 you learned:
- **MPLS architecture:** CE, PE, P roles and label operations (push, swap, pop).
- **MPLS label structure:** 32-bit label with TC, S-bit, and TTL fields.
- **LDP:** How labels are distributed and the LFIB is built.
- **MPLS L3VPN:** VRF, MP-BGP, RD, and Route Targets for multi-customer private WAN connectivity.
- **MPLS TE:** Path engineering beyond shortest-path routing.

In Part 2 we cover **SD-WAN** architecture, **IPsec VPN** tunnels (site-to-site and remote access), and compare MPLS vs. SD-WAN for enterprise WAN design decisions.

---
*End of Part 1 — Module 03*
