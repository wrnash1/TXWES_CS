# Video Script: Module 02 – Campus Network Design: VLANs, STP & EtherChannel
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 1 of 2 | Estimated Duration: 15–18 minutes
## Week 2: October 26 – November 1, 2026 | Due: Sunday, November 1, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 02 Part 1: Campus Network Design — VLANs & Spanning Tree | Texas Wesleyan University | Graduate Level"]

---

### Section 1: Welcome & Module Context

[00:00 – 02:00]
[SHOW SLIDE: Professor Nash on camera, campus network hierarchy diagram visible.]

Welcome back to CSC-6361. In Module 01 we operated at Layer 3 — routing protocols, OSPF, EIGRP, redistribution. This week we descend one layer and focus on the **campus switching infrastructure** that sits beneath all of that routing.

In a real enterprise, no matter how elegantly your routing is designed, if the underlying switched network is misconfigured, unstable, or unoptimized, everything above it fails. Campus network design is where most network engineers spend the majority of their daily work — configuring VLANs, tuning Spanning Tree, and bundling links. Let's understand it at CCNP depth.

---

### Section 2: The Three-Tier Campus Architecture

[02:00 – 05:00]
[SHOW DIAGRAM: Three-tier hierarchy — Core layer (redundant L3 switches) → Distribution layer (L3 switches) → Access layer (L2 switches/APs)]

[Alt-text: A hierarchical diagram with three rows. Top row labeled "Core Layer" shows two switches connected to each other. Middle row labeled "Distribution Layer" shows four switches, each connected to both core switches. Bottom row labeled "Access Layer" shows eight switches, each connected upward to two distribution switches. End devices (PCs, IP phones, APs) connect at the bottom.]

The classic campus network model uses a **three-tier hierarchy**:

**Access Layer:**
- Where end devices connect — PCs, IP phones, wireless APs, printers.
- Typically Layer 2 only (though increasingly Layer 3 access is used).
- Responsible for: port security, 802.1X authentication, VLAN assignment, PoE delivery.
- Design goal: low cost, high port density.

**Distribution Layer:**
- The policy and routing layer.
- Aggregates access layer uplinks.
- Provides inter-VLAN routing (either via SVI or routed ports).
- Enforces QoS policies, ACLs, and route summarization.
- Connects to Core via Layer 3 routed links.

**Core Layer:**
- Pure high-speed switching — no policy processing.
- Connects distribution blocks to each other and to the data center / WAN edge.
- Design principle: **Never do anything slow in the core.** No ACLs, no NAT, no firewall policies.
- Redundancy is paramount — typically two core switches in a fully meshed design.

> **Graduate Design Note:** Cisco now also recommends a collapsed two-tier design (collapsing core and distribution) for smaller campuses. The three-tier model is justified when the campus exceeds ~1,000 users or when inter-distribution traffic requires a dedicated transit path.

---

### Section 3: VLANs — Beyond the Basics

[05:00 – 09:30]
[SHOW DIAGRAM: Multi-VLAN campus with 802.1Q trunks, SVIs, and a DHCP server]

You already know what a VLAN is. At CCNP level, the questions are about **design, scaling, and troubleshooting**.

**VLAN Database vs. VLAN Trunk Protocol (VTP):**
VLANs are stored in the switch's VLAN database (`vlan.dat`), separate from the running configuration. This is important because `copy running-config startup-config` does NOT save VLAN data — `vlan.dat` saves automatically.

**VTP (VLAN Trunk Protocol):**
VTP is Cisco-proprietary and allows VLAN database synchronization across switches in a VTP domain. Modes:
- **Server:** Creates, modifies, and deletes VLANs. Propagates via VTP advertisements. Default mode.
- **Client:** Receives VTP updates and propagates them, but cannot locally create VLANs.
- **Transparent:** Does not participate in VTP synchronization but forwards VTP advertisements. Stores VLANs locally.
- **Off (VTPv3 only):** Completely disables VTP.

> **⚠ VTP Danger (Graduate-Level Awareness):** A switch with a higher **configuration revision number** will overwrite the VLAN database on all other switches in the domain, even a Server. This is a well-known production disaster scenario: a retired switch is re-introduced to the network with a higher revision number, instantly wiping all VLANs from every switch in the domain. **Best practice:** Use VTP Transparent or VTP Off in production, manage VLANs locally or via a management tool.

**802.1Q Trunking:**
Trunks carry traffic for multiple VLANs between switches. The 802.1Q standard inserts a 4-byte tag into the Ethernet frame header containing the VLAN ID (12-bit field = 4,096 VLANs possible, but 0 and 4095 are reserved).

Key trunk configuration:
```
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 10,20,30,100
 switchport trunk native vlan 999
```
The **native VLAN** is the VLAN whose traffic is transmitted untagged on a trunk. Cisco best practice: set the native VLAN to an **unused VLAN** (e.g., 999) to prevent native VLAN mismatch attacks (a form of VLAN hopping).

**Inter-VLAN Routing Options:**
1. **Router on a Stick:** A router with a trunk to a switch, using subinterfaces for each VLAN. Low cost, but a single point of failure and a potential bottleneck.
2. **Layer 3 Switch with SVIs:** The modern standard. Create a Switched Virtual Interface (SVI) for each VLAN on a multilayer switch. Far better performance and no external router needed.
```
interface Vlan10
 ip address 10.10.10.1 255.255.255.0
 no shutdown
```
3. **Routed Access Ports:** Configure individual switch ports as Layer 3 routed ports (`no switchport`) for direct point-to-point L3 connections. Used on distribution-to-core uplinks.

---

### Section 4: Spanning Tree Protocol Deep Dive

[09:30 – 14:30]
[SHOW DIAGRAM: STP topology — root bridge, root ports, designated ports, blocked port]

[Alt-text: A network diagram showing four switches. Switch A is labeled "Root Bridge (Bridge Priority 0, VLAN 10)." Switch B connects to Switch A with a port labeled "Root Port." Switch C connects to Switch A with a port labeled "Root Port." Switch D connects to both B and C. The link between Switch D and Switch C is labeled "Blocked Port (Alternate Port in RSTP)."]

Spanning Tree Protocol prevents Layer 2 loops, which would cause broadcast storms and bring down the network. Understanding STP in depth — including its variants and tuning — is essential CCNP material.

**STP Terminology:**
- **Root Bridge:** The switch with the lowest Bridge ID (priority + MAC). All path calculations are relative to the root.
- **Root Port:** The port on a non-root switch with the best (lowest) path cost to the root.
- **Designated Port:** On each network segment, the port with the best path cost to the root. Always in forwarding state.
- **Non-Designated (Blocked) Port:** A port that is blocked to prevent loops.

**Path Cost Values (802.1D/802.1W):**
| Link Speed | STP Cost |
|---|---|
| 10 Mbps | 100 |
| 100 Mbps | 19 |
| 1 Gbps | 4 |
| 10 Gbps | 2 |

**STP Variants:**

| Protocol | Standard | Convergence | Key Feature |
|---|---|---|---|
| STP (802.1D) | IEEE | 30–50 seconds | Original, slow |
| RSTP (802.1W) | IEEE | 1–5 seconds | Rapid convergence via handshake |
| PVST+ | Cisco | Per-VLAN, ~30 sec | Separate STP instance per VLAN |
| Rapid PVST+ | Cisco | Per-VLAN, ~1–5 sec | RSTP + per-VLAN. **Most common in Cisco enterprise** |
| MST (802.1S) | IEEE | ~1–5 sec | Maps multiple VLANs to fewer STP instances |

**RSTP Port Roles and States:**
RSTP replaces the 5 STP states (Blocking, Listening, Learning, Forwarding, Disabled) with 3 states:
- **Discarding** (replaces Blocking + Listening)
- **Learning**
- **Forwarding**

RSTP achieves rapid convergence through **proposal/agreement handshakes** between directly connected switches — no 30-second wait for topology changes.

**RSTP Port Roles:**
- **Root Port:** Best path to root.
- **Designated Port:** Best port on each segment toward root.
- **Alternate Port:** Backup to Root Port (equivalent to STP Blocking).
- **Backup Port:** Backup to a Designated Port on the same segment (rare).

**Critical STP Tuning Commands:**
```
! Set bridge priority (lower = more likely to be root; must be multiple of 4096)
spanning-tree vlan 10 priority 4096

! Shortcut: make this switch root for specific VLANs
spanning-tree vlan 10,20,30 root primary
spanning-tree vlan 40,50,60 root secondary

! PortFast: immediately transition access ports to Forwarding (skip STP convergence)
! Only on ports connected to end devices — NEVER on trunk ports
interface GigabitEthernet0/3
 spanning-tree portfast

! BPDU Guard: if a BPDU is received on a PortFast port, shutdown immediately
! Prevents rogue switches from disrupting STP
interface GigabitEthernet0/3
 spanning-tree bpduguard enable

! Globally enable BPDU Guard on all PortFast ports
spanning-tree portfast bpduguard default
```

**Root Guard:** Prevents a downstream switch from becoming the root bridge.
```
interface GigabitEthernet0/1
 spanning-tree guard root
```

---

### Section 5: Part 1 Summary

[14:30 – 16:00]
[SHOW SLIDE: Summary slide]

In Part 1 you learned:
- The **three-tier campus hierarchy** and design rationale at each layer.
- **VLANs** at depth — VTP risks, 802.1Q trunking, native VLAN best practices, inter-VLAN routing options.
- **Spanning Tree** — root election, path costs, port roles/states, STP variants (RSTP, Rapid PVST+, MST), and critical tuning commands.

In Part 2, we will cover **EtherChannel** (LACP/PAgP), **MST** configuration, and **CCNP-level STP troubleshooting scenarios**, then preview the Module 02 lab.

---
*End of Part 1 — Module 02*
