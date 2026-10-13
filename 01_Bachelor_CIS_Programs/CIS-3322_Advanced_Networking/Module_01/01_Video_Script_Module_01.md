# Video Script: Module 01 - Network Architectures & Topologies

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for all topology diagrams
- Display CLI commands in a high-contrast terminal font
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: Introduction and Course Roadmap [00:00 - 03:30]

Welcome to Module 01 of CIS-3322 Advanced Networking. I am Professor Nash, and this module lays the architectural foundation for everything that follows in this course.

Before we touch a single CLI command, we need to understand why networks are designed the way they are. The Cisco CCNA 200-301 exam allocates a full 20% of its points to Network Fundamentals, and topology knowledge is one of the first concepts tested.

[SHOW DIAGRAM: Course roadmap showing all 16 modules with Module 01 highlighted as the foundation layer]

Here is what we will cover today:

- Enterprise network design models: three-tier, collapsed core, and spine-leaf
- Physical and logical topology types: star, mesh, hub-and-spoke, point-to-point
- Selecting the right topology for the right environment
- How each design model maps to real Cisco hardware and IOS configurations

By the end of this video you should be able to identify each tier in a three-tier diagram, explain the trade-offs between design models, and answer CCNA scenario questions that ask you to map a network description to its correct topology name.

---

## Section 2: Three-Tier Enterprise Architecture [03:30 - 09:00]

[SHOW DIAGRAM: Three-tier hierarchy with labeled layers - Core (top), Distribution (middle), Access (bottom) with end devices at the bottom edge]

The three-tier model is the gold standard for medium-to-large campus networks. Think of it as a highway system. The Core layer is the interstate: high speed, no detours, no traffic lights. The Distribution layer is the on-ramp and off-ramp: it connects the fast interstate to local roads and enforces the rules. The Access layer is the local street where individual homes, offices, and devices connect.

### Core Layer

The Core layer exists for one reason: fast packet forwarding. Cisco designs this layer with high-capacity multilayer switches such as the Catalyst 9500 series. You never apply ACLs here, you never run complex routing policies here, and you never add unnecessary features that could slow forwarding. If a packet arrives at the Core, it should leave almost instantly.

Key characteristics:

- High-speed redundant links (10G, 40G, 100G)
- No end-device connections
- Redundant core switches for fault tolerance
- Layer 3 routing between Distribution blocks

### Distribution Layer

The Distribution layer is the policy enforcement point. This is where routing happens between VLANs, where ACLs filter traffic between subnets, and where QoS policies are applied before traffic hits the Core.

[SHOW DIAGRAM: Distribution layer switch with uplinks to Core and downlinks to Access, with ACL and VLAN routing labels on the uplinks]

Cisco multilayer switches at this layer — such as the Catalyst 3850 or 9300 — run both Layer 2 and Layer 3 functions. A typical Distribution switch might have:

- SVI (Switched Virtual Interface) routing for 10 to 20 VLANs
- Redundant uplinks to two Core switches
- Downlinks to four to eight Access switches
- Policy-based routing and QoS markings

### Access Layer

The Access layer is where end devices live. Laptops, IP phones, printers, and servers connect to Access layer switches. This layer is primarily Layer 2. The Access switch assigns ports to VLANs, enforces port security, and provides PoE (Power over Ethernet) for IP phones and wireless access points.

CCNA Exam Tip: The CCNA frequently presents a network description and asks you to identify which layer performs a function. If the question mentions "routing between VLANs" or "applying ACLs between departments," the answer is the Distribution layer, not the Core.

---

## Section 3: Collapsed Core and Spine-Leaf Designs [09:00 - 14:30]

[SHOW DIAGRAM: Side-by-side comparison - left shows three-tier with separate Core and Distribution; right shows collapsed core with merged layer labeled "Core/Distribution"]

### Collapsed Core Design

For smaller campus networks — think a single building with fewer than 500 users — a separate Core layer adds cost without adding value. The collapsed core design merges the Core and Distribution layers into one set of switches. The result is a two-tier model: a combined Core/Distribution layer at the top, and an Access layer below.

Cost savings are significant: instead of purchasing six to eight switches for a full three-tier design, a collapsed core might require only two multilayer switches. The trade-off is scalability. When the organization grows, you must either upgrade the existing switches or add a separate Core layer — essentially rebuilding the design.

CCNA Exam Tip: When you read "small campus network" or "single building" in a CCNA scenario, that is the exam hinting at a collapsed core design. When you read "large enterprise" or "multi-building campus," think three-tier.

### Spine-Leaf Topology

[SHOW DIAGRAM: Spine-leaf data center topology - two spine switches at top, four leaf switches below, every leaf connected to every spine with equal-cost links, no connections between leaf switches]

The spine-leaf topology is the dominant design for modern data centers. It replaces the old three-tier model that was common in data centers before hyperscale workloads created new demands.

Architecture rules:

- Every leaf switch connects to every spine switch
- No leaf-to-leaf connections exist
- No spine-to-spine connections exist
- Traffic from any server to any server always crosses exactly two hops: leaf to spine to leaf

This predictability is the key benefit. Because every path between any two servers is the same number of hops, latency is consistent and capacity planning is straightforward. Equal-cost multipath (ECMP) routing distributes traffic across all spine uplinks simultaneously, eliminating the active/standby waste of Spanning Tree Protocol.

CCNA Exam Tip: The CCNA tests your conceptual understanding of spine-leaf, not its CLI configuration. Know these facts: two tiers, every leaf connects to every spine, no STP dependency, ECMP routing, predictable low latency, and used in modern data centers.

---

## Section 4: Physical and Logical Topologies [14:30 - 19:00]

[SHOW DIAGRAM: Grid of six topology diagrams - star, full mesh, partial mesh, hub-and-spoke, point-to-point, ring - each labeled]

Network topology describes how nodes are interconnected. The CCNA tests both physical topology (how cables and hardware are actually connected) and logical topology (how data flows through the network, which may differ from physical connections).

### Star Topology

All devices connect to a central device, typically a switch. This is the most common topology in enterprise access layers. A single switch failure can isolate all connected devices, but the central switch is usually redundant.

### Full Mesh Topology

Every node connects directly to every other node. Full mesh provides maximum redundancy and eliminates any single point of failure. However, cost grows exponentially: n devices require n(n-1)/2 links. A 10-node full mesh requires 45 links. Full mesh is practical for small WAN deployments or as a conceptual model for BGP routing.

### Partial Mesh Topology

A compromise between full mesh and hub-and-spoke. Critical nodes receive multiple connections; edge nodes may have only one or two uplinks. Most enterprise WAN designs are partial mesh.

### Hub-and-Spoke Topology

All remote sites connect to a central hub. No direct spoke-to-spoke connections exist. Traffic between two spoke sites must traverse the hub. This is cost-effective for organizations with many small branch sites that primarily communicate with headquarters.

### Point-to-Point Topology

A dedicated link between exactly two devices. WAN leased lines are a classic example. On the CCNA, serial interfaces on Cisco routers represent point-to-point WAN connections.

[SHOW DIAGRAM: Cisco router with a serial interface labeled s0/0/0 connected via a WAN cloud symbol to another router's serial interface]

---

## Section 5: Lab Preview and Exam Readiness [19:00 - 22:00]

This week's Packet Tracer lab walks you through building a three-tier topology from scratch. You will place Core, Distribution, and Access layer switches, configure trunk links between layers, and verify the topology using show commands.

Here is a preview of the key verification commands you will use:

```text
SW-CORE# show interfaces trunk
SW-DIST# show ip route
SW-ACCESS# show vlan brief
```

[SHOW DIAGRAM: Packet Tracer screenshot of completed three-tier topology with device labels]

CCNA Exam Tip: On exam day, if a scenario asks you to choose between a three-tier design and a collapsed core, always consider the scale of the network described. Also remember that the spine-leaf design belongs to the data center domain, not the campus network domain.

For additional study resources, visit the official Cisco certification training pages at cisco.com/c/en/us/training-events/training-certifications and professormesser.com for free CCNA video notes.

Complete the reading guide before starting the lab, and post your initial discussion response by Wednesday at 11:59 PM. I will see you in Module 02, where we dive into subnetting and VLSM. Good luck!

---

## End Card

Module 01 Complete
Next: Module 02 - Subnetting and VLSM Configurations
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
