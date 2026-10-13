# Video Script: Module 11 — Switching: VLANs, STP, and EtherChannel (Part 1)

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

Estimated Runtime: 13–15 minutes

---

### [INTRO]

Welcome to Module 11. This module covers Layer 2 switching — the technology that makes modern Ethernet LANs possible at scale. We are going to cover three interconnected topics: VLANs, the Spanning Tree Protocol, and EtherChannel link aggregation.

These are topics that appear heavily on the CompTIA Network+ exam, and they are also technologies you will configure and troubleshoot every day in a real network engineering role. Let's start with the foundation: what a switch actually does, and why VLANs exist.

---

### [SECTION 1: HOW SWITCHES WORK — LAYER 2 FORWARDING]

[SHOW DIAGRAM: A switch with four connected PCs, a MAC address table showing entries for each port]

A switch is a Layer 2 device. That means it makes forwarding decisions based on MAC addresses — the hardware addresses burned into every network interface card.

When a frame arrives on a switch port, the switch does three things in sequence:

First, it looks at the source MAC address of the incoming frame. It records that MAC address and the port it arrived on in a table called the MAC address table — also called the CAM table (Content Addressable Memory). This is how the switch learns where devices are.

Second, it looks at the destination MAC address. If that destination MAC is already in the MAC address table, the switch forwards the frame only to the port where that MAC was learned. This is unicast forwarding — traffic goes only to the intended destination, not to every port.

Third, if the destination MAC is not in the table — or if the destination is the broadcast address (FF:FF:FF:FF:FF:FF) — the switch floods the frame out all ports except the one it arrived on. This is called flooding.

[SHOW DIAGRAM: MAC address table with columns: Port, MAC Address, VLAN, Age]

Over time the MAC address table fills in as devices communicate. Entries age out (default 300 seconds on Cisco) to handle devices that are disconnected or moved.

This flooding and learning process is why switches are more efficient than hubs — a hub sends every frame to every port always. A switch sends traffic only to the relevant destination once it has learned the topology.

---

### [SECTION 2: THE PROBLEM THAT VLANS SOLVE]

[SHOW DIAGRAM: A building with three departments — Finance, HR, Engineering — all on one switch, all on one subnet]

In the early days of switched networks, all devices on a switch shared a single broadcast domain. Every broadcast — DHCP Discovers, ARP requests, routing protocol hellos — went to every device on every port of that switch.

The problems:

Problem 1 — Performance. As the network grows, broadcast traffic grows. A 500-device network on one VLAN generates significantly more broadcast noise than the same devices split across five VLANs of 100 each.

Problem 2 — Security. Without segmentation, a workstation in the Finance department and a workstation in Engineering can communicate freely at Layer 2. This is a security problem — lateral movement within a flat network is easy for an attacker.

Problem 3 — Logical isolation. Physical rewiring is the only way to rearrange a flat network. Moving a user from one department to another would require running a new cable to the right switch.

VLANs solve all three problems.

---

### [SECTION 3: VLANS — VIRTUAL LOCAL AREA NETWORKS]

[SHOW DIAGRAM: Same switch, now divided into VLAN 10 (Finance), VLAN 20 (HR), VLAN 30 (Engineering) — each VLAN shown as a separate color]

A VLAN (Virtual Local Area Network) creates a logically separate broadcast domain on a physical switch. Devices in VLAN 10 cannot receive broadcasts from VLAN 20, and cannot communicate with VLAN 20 at Layer 2 — even if they are physically connected to the same switch.

Think of it this way: a 48-port switch with three VLANs behaves like three separate physical switches for broadcast purposes.

Key VLAN concepts:

VLAN ID — A number between 1 and 4094. VLAN 1 is the default VLAN. Best practice: do not use VLAN 1 for user traffic. VLANs 2–1001 are the standard range. VLANs 1006–4094 are the extended range.

Access port — A switch port configured to belong to exactly one VLAN. The port carries untagged traffic. The connected device (a PC, printer, or IP phone) has no knowledge of VLANs.

Trunk port — A switch port that carries traffic for multiple VLANs simultaneously. Used to connect switches to each other or to routers. Trunk ports use IEEE 802.1Q tagging to identify which VLAN each frame belongs to.

---

### [SECTION 4: 802.1Q TAGGING]

[SHOW DIAGRAM: Ethernet frame showing standard fields plus the 802.1Q 4-byte tag inserted between the source MAC and EtherType fields]

When a frame is forwarded on a trunk port, the switch inserts a 4-byte 802.1Q tag into the Ethernet frame header. This tag contains the VLAN ID so the receiving switch knows which VLAN the frame belongs to.

The tag has two main fields:

TPID (Tag Protocol Identifier) — Set to 0x8100 to indicate this is an 802.1Q-tagged frame.

TCI (Tag Control Information) — Contains the 12-bit VLAN ID field (0–4095), a 3-bit Priority Code Point (PCP) for QoS, and a Drop Eligible Indicator bit.

When the frame arrives at the destination switch, the tag is read, the frame is forwarded to the correct VLAN, and the tag is stripped before the frame reaches the end-device access port. End devices never see the 802.1Q tag.

Native VLAN — One VLAN on a trunk port is designated the native VLAN. Frames in the native VLAN are not tagged. By default, the native VLAN is VLAN 1 on Cisco switches. Security best practice: change the native VLAN to an unused VLAN ID (not VLAN 1) and configure it consistently on both ends of a trunk.

---

### [SECTION 5: INTER-VLAN ROUTING]

[SHOW DIAGRAM: Router-on-a-Stick — one physical router interface connected to a switch trunk port, with subinterfaces for VLAN 10, 20, and 30]

VLANs segment traffic at Layer 2. But users in different VLANs often need to communicate. That requires Layer 3 routing.

Two methods:

Method 1 — Router-on-a-Stick (ROAS). A single router interface is configured as a trunk. The router creates logical subinterfaces, one per VLAN. Each subinterface has an IP address that serves as the default gateway for that VLAN. The router routes traffic between VLANs by receiving a frame on one subinterface, making a routing decision, and sending it out another subinterface.

Method 2 — Layer 3 Switch (Multi-Layer Switch). A switch with built-in routing capability. SVIs (Switch Virtual Interfaces) serve as the default gateways for each VLAN. Traffic between VLANs is routed in hardware at wire speed. More common in enterprise networks than ROAS. The command to enable routing on a Cisco multilayer switch is `ip routing`.

---

### [SECTION 6: VLAN HOPPING ATTACKS]

[SHOW DIAGRAM: Attacker sending double-tagged 802.1Q frames to hop from VLAN 10 to VLAN 20]

VLAN hopping is an attack that allows traffic from one VLAN to reach another VLAN without going through a router. Two methods:

Switch Spoofing — The attacker configures their interface to negotiate a DTP (Dynamic Trunking Protocol) trunk link. Once the trunk is established, the attacker can send traffic tagged with any VLAN ID and receive all VLAN traffic.

Double Tagging — The attacker sends a frame with two 802.1Q tags. The outer tag matches the native VLAN and is stripped by the first switch. The inner tag targets the victim VLAN. The second switch sees the inner tag and forwards the frame into that VLAN.

Prevention:

- Disable DTP on all access ports: `switchport mode access` and `switchport nonegotiate`
- Change the native VLAN to an unused VLAN: `switchport trunk native vlan 999`
- Explicitly prune VLANs from trunk ports using `switchport trunk allowed vlan`

---

### [SECTION 7: SPANNING TREE PROTOCOL — WHY IT EXISTS]

[SHOW DIAGRAM: Two switches with two physical links between them, creating a loop — circular arrows showing a broadcast storm saturating the network]

Spanning Tree Protocol exists to solve one problem: loops in switched networks.

Without STP, redundant links create Layer 2 loops. What happens?

A broadcast frame enters the network. Switch A floods it out both links to Switch B. Switch B receives it on both ports, floods it back to Switch A. Switch A floods it again. The frame circulates indefinitely — a broadcast storm. The network saturates at 100% utilization within seconds. No unicast traffic can get through.

A second problem: MAC address table instability. The same frame arrives on different ports from different directions. The switch keeps updating the same MAC address to different ports. Forwarding becomes erratic.

STP prevents loops by blocking redundant paths while keeping them available as backups.

---

### [SECTION 8: STP ROOT BRIDGE ELECTION]

[SHOW DIAGRAM: Three switches — center switch elected Root Bridge, ports labeled Root Port, Designated Port, Blocking Port]

STP operates in four steps:

Step 1 — Root Bridge election. Every switch has a Bridge ID — a combination of a configurable priority value (default 32768) and the switch's MAC address. The switch with the lowest Bridge ID becomes the Root Bridge. If priorities are equal, the switch with the lowest MAC address wins. The Root Bridge is the reference point for all path calculations.

Step 2 — Root Port selection. Every non-root switch selects one Root Port — the port with the lowest-cost path to the Root Bridge. STP cost is based on link speed. Default costs: 10 Gbps = 2, 1 Gbps = 4, 100 Mbps = 19, 10 Mbps = 100.

Step 3 — Designated Port selection. For each network segment, one port is elected to forward traffic toward the Root Bridge. The Root Bridge has all Designated Ports on its segments. On other switches, the port with the lowest cost toward the Root Bridge wins the Designated Port role.

Step 4 — Blocking. Any port that is not a Root Port or Designated Port is placed in Blocking state. It does not forward frames but continues receiving BPDUs (Bridge Protocol Data Units) to detect topology changes.

---

### [SECTION 9: STP PORT STATES AND CONVERGENCE]

[SHOW DIAGRAM: State transition diagram — Blocking → Listening → Learning → Forwarding with timer durations shown]

Classic 802.1D STP port states:

Blocking — Receives BPDUs, does not forward frames or learn MACs. Persists up to Max Age (20 seconds).

Listening — Participates in BPDU exchange and Root Bridge election. Does not forward frames. Duration: Forward Delay (15 seconds).

Learning — Learns MAC addresses from incoming frames but does not yet forward. Duration: Forward Delay (15 seconds).

Forwarding — Full operation — forwards frames and learns MACs.

Total convergence time with classic STP: up to 50 seconds. This is why RSTP was developed.

---

### [SECTION 10: RSTP AND PORTFAST]

[SHOW DIAGRAM: RSTP convergence compared to 802.1D — RSTP converges in under 1 second via direct negotiation]

Rapid Spanning Tree Protocol (RSTP, IEEE 802.1w) replaces classic STP. RSTP converges in under one second by negotiating port states directly between switches rather than waiting for timers.

RSTP port roles:

Root Port — Lowest cost path to Root Bridge (same as STP).

Designated Port — Forwards toward Root Bridge on each segment (same as STP).

Alternate Port — Backup to the Root Port. Immediately takes over if the Root Port fails — no waiting for timers.

Backup Port — Backup to a Designated Port on the same segment.

PortFast — Bypasses Listening and Learning for access ports connected to end devices. The port immediately enters Forwarding state. Only enable on access ports, never on switch-to-switch links.

BPDU Guard — Works with PortFast. If a BPDU is received on a PortFast-enabled port (indicating an unauthorized switch was connected), the port is immediately placed in err-disabled state. Protects the STP topology from rogue switches.

---

### [SUMMARY — PART 1]

In Part 1 we covered:

- How switches learn MAC addresses and make forwarding decisions (the MAC address table)
- VLANs: access ports, trunk ports, 802.1Q tagging, native VLANs, inter-VLAN routing
- VLAN hopping attacks: switch spoofing and double tagging, and how to prevent both
- Spanning Tree Protocol: Root Bridge election, port roles, port states, convergence timers
- RSTP: faster convergence through direct negotiation, PortFast, and BPDU Guard

In Part 2, we cover EtherChannel link aggregation, Cisco VLAN and trunk configuration commands, and how to read the output of show vlan, show interfaces trunk, and show spanning-tree.

See you in Part 2.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
