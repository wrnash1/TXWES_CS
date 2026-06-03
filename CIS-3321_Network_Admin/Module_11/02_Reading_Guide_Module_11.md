# Reading Guide: Module 11 — Switching: VLANs, STP, and EtherChannel

## Course: CIS-3321 Network Administration

Certification Alignment: CompTIA Network+ (N10-008)

---

### Introduction

Module 11 covers Layer 2 switching technology: VLANs for logical network segmentation, Spanning Tree Protocol for loop prevention, and EtherChannel for link aggregation. These topics appear throughout Domain 2 (Network Implementation) and Domain 5 (Network Troubleshooting) of the CompTIA Network+ N10-008 exam. Mastery of VLAN design, STP behavior, and EtherChannel configuration is essential for both the exam and day-to-day network administration work.

---

### 1. Core Vocabulary

Switch — A Layer 2 network device that forwards frames based on destination MAC addresses. Maintains a MAC address table (CAM table) mapping MAC addresses to ports.

MAC address table (CAM table) — The switch's internal database mapping learned MAC addresses to specific ports. Used for unicast forwarding decisions.

Flooding — When a switch sends a frame out all ports except the incoming port. Occurs when the destination MAC is unknown or the destination is a broadcast/multicast.

Broadcast domain — The set of devices that receive a broadcast frame. One VLAN = one broadcast domain.

Collision domain — The set of devices that share the same transmission medium and can collide. Each switch port is its own collision domain.

VLAN (Virtual Local Area Network) — A logical segmentation of a switched network creating separate broadcast domains. Devices in different VLANs cannot communicate at Layer 2 without routing.

VLAN ID — A number from 1 to 4094 assigned to each VLAN. VLAN 1 is the default. Standard range: 1–1001. Extended range: 1006–4094.

Access port — A switch port assigned to exactly one VLAN. Carries untagged traffic. End devices (PCs, printers, servers) connect to access ports.

Trunk port — A switch port that carries traffic for multiple VLANs simultaneously using 802.1Q tagging. Used for switch-to-switch and switch-to-router connections.

802.1Q — The IEEE standard for VLAN tagging. Inserts a 4-byte tag into the Ethernet frame header containing the VLAN ID. The native VLAN is not tagged on trunk ports.

Native VLAN — The VLAN whose traffic is sent untagged on a trunk port. Default is VLAN 1 on Cisco switches. Best practice: change to an unused VLAN and match on both ends.

DTP (Dynamic Trunking Protocol) — Cisco proprietary protocol that negotiates trunk formation automatically. Best practice: disable on access ports to prevent VLAN hopping attacks.

SVI (Switch Virtual Interface) — A logical Layer 3 interface on a multilayer switch, one per VLAN, serving as the default gateway for that VLAN. Enables inter-VLAN routing without a separate router.

Router-on-a-Stick (ROAS) — An inter-VLAN routing design using subinterfaces on a single router interface connected to a trunk port. Each subinterface handles one VLAN.

STP (Spanning Tree Protocol) — IEEE 802.1D protocol that prevents Layer 2 loops in switched networks by blocking redundant paths while maintaining them as backups.

Root Bridge — The reference switch in an STP topology. The switch with the lowest Bridge ID. All STP path calculations reference the Root Bridge.

Bridge ID — A value combining a configurable priority (default 32768) and the switch's MAC address. The switch with the lowest Bridge ID becomes Root Bridge.

Root Port — A non-root switch port with the lowest-cost path to the Root Bridge. Each non-root switch has exactly one Root Port.

Designated Port — The port on each network segment that forwards traffic toward the Root Bridge. The Root Bridge has all Designated Ports.

Blocking state — An STP port state where the port receives BPDUs but does not forward frames or learn MAC addresses. Prevents loops.

BPDU (Bridge Protocol Data Unit) — STP control messages exchanged between switches to elect the Root Bridge, calculate port roles, and detect topology changes.

RSTP (Rapid Spanning Tree Protocol) — IEEE 802.1w. Converges in under one second by negotiating port states directly between switches instead of waiting for timers.

Alternate Port — RSTP role. Backup to the Root Port. Immediately takes over if the Root Port fails, with no timer delay.

PortFast — STP feature that bypasses Listening and Learning states for access ports connected to end devices. Port immediately enters Forwarding state.

BPDU Guard — Feature that err-disables a PortFast port if a BPDU is received. Prevents rogue switches from affecting the STP topology.

Root Guard — Feature that prevents a port from becoming a Root Port. If a superior BPDU arrives on a Root Guard port, the port enters root-inconsistent state.

EtherChannel — A technology that bundles multiple physical links into one logical link. STP sees one link; all physical members carry traffic simultaneously.

LACP (Link Aggregation Control Protocol) — IEEE 802.3ad standard for EtherChannel negotiation. Port modes: Active (initiates) and Passive (responds). Requires at least one Active end.

PAgP (Port Aggregation Protocol) — Cisco proprietary EtherChannel negotiation. Port modes: Desirable (initiates) and Auto (responds). Requires at least one Desirable end.

Port-Channel interface — The logical interface representing an EtherChannel bundle. VLAN and trunk configurations are applied here, not to individual physical member ports.

Port Security — Switch feature limiting the number of MAC addresses on a port. Violation actions: Shutdown (err-disable), Restrict (drop and count), Protect (drop silently).

Sticky MAC — Port Security feature that automatically learns and permanently saves allowed MAC addresses to the running configuration.

err-disabled — A Cisco switch port state where the port has been administratively disabled due to a security violation or protocol error. Recovery requires `shutdown` then `no shutdown` after fixing the root cause.

---

### 2. STP Port States (802.1D)

| State | Forward Frames | Learn MACs | Receive BPDUs | Duration |
|-------|---------------|------------|---------------|----------|
| Blocking | No | No | Yes | Up to 20 sec (Max Age) |
| Listening | No | No | Yes | 15 sec (Forward Delay) |
| Learning | No | Yes | Yes | 15 sec (Forward Delay) |
| Forwarding | Yes | Yes | Yes | Indefinite |
| Disabled | No | No | No | Administrative |

Total convergence time for classic 802.1D: up to 50 seconds (Max Age + 2x Forward Delay).

RSTP replaces Blocking, Listening, and Learning with a single Discarding state. Convergence: under 1 second via BPDU negotiation.

---

### 3. STP Administrative Distance Values

| STP Link Speed | Default Port Cost (802.1D) |
|----------------|---------------------------|
| 10 Gbps | 2 |
| 1 Gbps | 4 |
| 100 Mbps | 19 |
| 10 Mbps | 100 |

Lower cost = preferred path toward Root Bridge.

---

### 4. EtherChannel Negotiation Protocols

| Protocol | Standard | Port Modes | Requirement |
|----------|----------|------------|-------------|
| LACP | IEEE 802.3ad (open) | Active / Passive | At least one Active end |
| PAgP | Cisco proprietary | Desirable / Auto | At least one Desirable end |
| Static (On) | None | On / On | Both sides must be On; no error detection |

Mode compatibility:

- LACP Active + LACP Active = Channel forms
- LACP Active + LACP Passive = Channel forms
- LACP Passive + LACP Passive = No channel
- PAgP Desirable + PAgP Desirable = Channel forms
- PAgP Desirable + PAgP Auto = Channel forms
- PAgP Auto + PAgP Auto = No channel

---

### 5. VLAN Cisco IOS Command Reference

| Command | Purpose |
|---------|---------|
| `vlan 10` | Create VLAN 10 |
| `name Finance` | Assign name to VLAN |
| `switchport mode access` | Set port to access mode |
| `switchport access vlan 10` | Assign port to VLAN 10 |
| `switchport mode trunk` | Set port to trunk mode |
| `switchport trunk encapsulation dot1q` | Set trunk encapsulation to 802.1Q |
| `switchport trunk allowed vlan 10,20,30` | Restrict allowed VLANs on trunk |
| `switchport trunk native vlan 999` | Set native VLAN to 999 |
| `switchport nonegotiate` | Disable DTP negotiation |
| `show vlan brief` | Display VLAN assignments and port membership |
| `show interfaces trunk` | Display trunk ports and active VLANs |
| `show interfaces Fa0/1 switchport` | Display port mode and VLAN assignment |

---

### 6. STP Cisco IOS Command Reference

| Command | Purpose |
|---------|---------|
| `show spanning-tree` | Display STP topology for all VLANs |
| `show spanning-tree vlan 10` | Display STP for VLAN 10 specifically |
| `spanning-tree vlan 10 priority 4096` | Set Root Bridge priority |
| `spanning-tree vlan 10 root primary` | Automatically set lowest priority |
| `spanning-tree portfast` | Enable PortFast on an interface |
| `spanning-tree bpduguard enable` | Enable BPDU Guard on an interface |
| `spanning-tree portfast bpduguard default` | Enable BPDU Guard globally on PortFast ports |
| `spanning-tree guard root` | Enable Root Guard on an interface |

---

### 7. Exam Tips

Exam Tip 1: A trunk port carries traffic for multiple VLANs. An access port carries traffic for exactly one VLAN. This distinction is tested frequently.

Exam Tip 2: The native VLAN is sent untagged on a trunk port. A native VLAN mismatch between two switches causes STP issues, CDP warnings, and traffic problems. Best practice: use an unused VLAN as the native VLAN on all trunks.

Exam Tip 3: STP prevents loops by blocking redundant ports. The Root Bridge has all Designated Ports. Non-root switches each have exactly one Root Port. All remaining ports are in Blocking state.

Exam Tip 4: PortFast should only be enabled on ports connected to end devices (PCs, printers, servers). Never enable PortFast on a port that connects to another switch — this could prevent loop detection.

Exam Tip 5: BPDU Guard err-disables a port if a BPDU is received. Root Guard prevents a port from becoming a Root Port. Know which protection applies in which scenario.

Exam Tip 6: LACP is the open-standard protocol (IEEE 802.3ad). PAgP is Cisco proprietary. For multi-vendor environments, always use LACP. The exam will ask which is open-standard.

Exam Tip 7: EtherChannel load balances per-flow (per source/destination pair), not per-packet. This preserves packet ordering within a conversation. Traffic from the same source/destination pair always uses the same physical link.

Exam Tip 8: MAC flooding fills the CAM table, causing the switch to flood all traffic to all ports. Port Security prevents this by limiting allowed MAC addresses per port.

---

### 8. Reading and Viewing Resources

CompTIA Network+ N10-008 Exam Objectives — Domain 2.3 (VLANs), Domain 2.4 (Spanning Tree), Domain 2.5 (EtherChannel)

Professor Messer — Network+ Study Groups (free video series): VLANs, STP, EtherChannel topics aligned to N10-008

Mike Meyers — CompTIA Network+ All-in-One Exam Guide, 8th Edition: Chapter 10 (VLANs), Chapter 11 (STP), Chapter 12 (Link Aggregation)

Cisco Documentation — Cisco Catalyst Switch Configuration Guide: VLAN and STP configuration chapters (available at Cisco.com)

IEEE 802.1Q-2018 — The authoritative VLAN tagging standard specification

IEEE 802.3ad (802.1AX) — The LACP link aggregation standard specification

---

### 9. Study Checklist

Before moving to the next module, confirm you can do each of the following:

- [ ] Explain how a switch uses the MAC address table to make forwarding decisions
- [ ] Define a broadcast domain and explain how VLANs create separate broadcast domains
- [ ] Distinguish between access ports and trunk ports by function and configuration
- [ ] Explain what 802.1Q tagging does and what happens to the native VLAN
- [ ] Describe two VLAN hopping attack methods and the prevention for each
- [ ] Explain why STP is needed and what happens without it (broadcast storm, MAC table instability)
- [ ] Describe the Root Bridge election process using Bridge ID and priority
- [ ] Identify the three non-disabled STP port roles: Root Port, Designated Port, Blocking
- [ ] List the four 802.1D STP port states and their durations
- [ ] Explain the RSTP improvement over 802.1D and what Alternate Port does
- [ ] Explain PortFast: what it does, when to use it, and why BPDU Guard must accompany it
- [ ] Distinguish LACP from PAgP and explain which is the open standard
- [ ] Explain EtherChannel per-flow load balancing and why per-packet is not used
- [ ] State the Port Security violation modes: Shutdown, Restrict, and Protect
- [ ] Identify the commands show vlan brief, show interfaces trunk, and show spanning-tree

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
