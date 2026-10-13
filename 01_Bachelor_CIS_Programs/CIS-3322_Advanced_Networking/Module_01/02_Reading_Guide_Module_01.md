# Reading Guide: Module 01 - Network Architectures & Topologies

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3322 &BULL; ADVANCED NETWORKING & INFRASTRUCTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

This reading guide supports the Module 01 video lecture and prepares you for the lab activity and quiz. Network architecture and topology are foundational CCNA topics. Every subsequent module in this course — VLANs, routing protocols, WAN technologies — builds on the design models covered here. Study this guide thoroughly before proceeding to the lab.

---

## 1. High-Yield Glossary

Review these definitions carefully. The CCNA 200-301 exam expects you to apply these concepts in scenario-based questions, not just recite definitions.

- **Three-tier architecture:** A hierarchical enterprise campus design with three distinct functional layers: Core, Distribution, and Access. Each layer has a defined role and the design scales from small to very large deployments.

- **Core layer:** The high-speed backbone of the three-tier model. Responsible only for fast packet forwarding between Distribution blocks. No ACLs, no end-user connections, no complex services.

- **Distribution layer:** The policy and routing layer. Aggregates traffic from Access switches, performs inter-VLAN routing via SVIs, enforces ACLs, applies QoS markings, and connects to the Core with redundant uplinks.

- **Access layer:** The edge layer where end-user devices connect. Operates primarily at Layer 2. Responsibilities include VLAN assignment, port security, 802.1X authentication, and PoE for phones and APs.

- **Collapsed core design:** A two-tier variant that merges the Core and Distribution functions into a single layer. Used in smaller campus networks to reduce cost. Trades scalability for simplicity.

- **Spine-leaf topology:** A two-tier data center architecture where every leaf switch connects to every spine switch. Provides equal-cost multipath (ECMP) paths, predictable low latency, and no Spanning Tree Protocol dependency.

- **Leaf switch:** In a spine-leaf design, the leaf is the edge tier. Servers and storage connect to leaf switches. Leaf switches never connect to other leaf switches directly.

- **Spine switch:** The aggregation tier in a spine-leaf design. Spine switches connect only to leaf switches. No server connections terminate on a spine switch.

- **Equal-cost multipath (ECMP):** A routing strategy that allows traffic to be distributed across multiple paths of equal cost simultaneously, maximizing bandwidth and providing automatic failover.

- **Physical topology:** The actual physical arrangement of cables and hardware in a network.

- **Logical topology:** The path that data takes through a network, which may differ from the physical layout. For example, a ring may be physically wired as a star through a central hub.

- **Star topology:** All devices connect to a central switch or hub. Most common in enterprise access layers.

- **Full mesh topology:** Every node connects directly to every other node. Provides maximum redundancy at high cost. Number of links = n(n-1)/2.

- **Partial mesh topology:** Selected nodes have redundant connections; others do not. Balances cost and redundancy for WAN designs.

- **Hub-and-spoke topology:** Remote sites (spokes) connect only to a central site (hub). Traffic between spokes must pass through the hub. Common in DMVPN and MPLS WAN designs.

- **Point-to-point topology:** A single dedicated link between exactly two devices. Cisco serial interfaces on routers traditionally represent WAN point-to-point links.

- **SVI (Switched Virtual Interface):** A virtual interface on a multilayer switch that acts as the default gateway for a VLAN. Used for inter-VLAN routing at the Distribution layer.

- **Trunk link:** A switch port configured to carry traffic for multiple VLANs using 802.1Q encapsulation. Used on uplinks between Access and Distribution switches.

---

## 2. Three-Tier Architecture — Design Reference

The following table summarizes the key characteristics of each layer for quick review.

| Layer | Primary Function | Typical Devices | Layer | Key Features |
|---|---|---|---|---|
| Core | Fast backbone forwarding | Catalyst 9500, 6800 | L3 | No ACLs, no end devices, high-speed uplinks |
| Distribution | Policy, routing, aggregation | Catalyst 9300, 3850 | L2/L3 | Inter-VLAN routing, ACLs, QoS, redundant uplinks |
| Access | End-device connectivity | Catalyst 9200, 2960 | L2 | VLAN assignment, port security, PoE, 802.1X |

Design rules to memorize:

- The Core never performs policy functions — keep it simple for speed
- The Distribution layer is always where routing between VLANs occurs
- The Access layer connects to exactly one Distribution switch in a basic design, or two for redundancy
- Trunk links carry 802.1Q tags between Access and Distribution layers

---

## 3. Collapsed Core vs. Three-Tier Comparison

| Criteria | Three-Tier | Collapsed Core |
|---|---|---|
| Number of tiers | 3 (Core, Distribution, Access) | 2 (Core/Distribution, Access) |
| Best for | Large campus, multi-building | Small campus, single building |
| Scalability | High | Limited |
| Cost | Higher (more switches) | Lower |
| Complexity | Higher | Lower |
| CCNA exam hint | "Large enterprise network" | "Small campus" or "single building" |

---

## 4. Spine-Leaf Architecture Reference

Spine-leaf characteristics tested on the CCNA:

- Two tiers only: spine tier and leaf tier
- Every leaf connects to every spine (full mesh between tiers)
- No leaf-to-leaf connections
- No spine-to-spine connections
- Traffic path between any two servers: source leaf → spine → destination leaf (always 2 hops)
- No Spanning Tree Protocol — uses IP routing (ECMP) at both layers
- Scales by adding leaf switches for more servers, or spine switches for more bandwidth
- Modern data centers use this design for cloud, virtualization, and hyperscale workloads

---

## 5. Topology Type Quick Reference

| Topology | Description | Pros | Cons | CCNA Context |
|---|---|---|---|---|
| Star | Central switch connects all devices | Simple, easy to manage | Single point of failure at center | Campus access layer |
| Full mesh | Every node connects to every other node | Maximum redundancy | Expensive: n(n-1)/2 links | Small WAN, BGP concept |
| Partial mesh | Some redundant links, not all | Balances cost and redundancy | Less resilient than full mesh | Enterprise WAN |
| Hub-and-spoke | All spokes connect only to hub | Cost-effective for many branches | Hub is single point of failure; spoke-to-spoke latency | MPLS, DMVPN WAN |
| Point-to-point | Two devices, one dedicated link | Simple, dedicated bandwidth | Does not scale | WAN serial links, leased lines |
| Ring | Devices connected in a loop | Simple cabling | Single break disrupts ring | Legacy SONET/SDH WAN |

---

## 6. Cisco CLI Command Reference

The following commands are used to verify topology and connectivity in a three-tier design. You will use these in the lab.

| Command | Device | Purpose |
|---|---|---|
| `show interfaces trunk` | Switch | Displays all active trunk ports and the VLANs allowed on each trunk |
| `show vlan brief` | Switch | Shows all VLANs and their port assignments |
| `show ip route` | Multilayer switch or router | Displays the routing table; confirms inter-VLAN routes are present |
| `show cdp neighbors` | Any Cisco device | Shows directly connected Cisco neighbors; useful for verifying topology |
| `show cdp neighbors detail` | Any Cisco device | Adds IP addresses and platform info to CDP neighbor output |
| `show ip interface brief` | Router or multilayer switch | Shows interface status and IP addresses at a glance |
| `show running-config` | Any Cisco device | Displays the full active configuration |
| `ping [ip-address]` | Any Cisco device | Tests Layer 3 connectivity to a destination |

---

## 7. CCNA Exam Tips

1. The Distribution layer performs inter-VLAN routing, applies ACLs, and enforces QoS policies. The Core layer never does any of these — it exists only for fast forwarding.

2. Collapsed core is a two-tier design. When a CCNA question describes a "small campus" or "single building," the correct answer is almost always collapsed core.

3. Spine-leaf is a data center topology, not a campus topology. Every leaf connects to every spine; no leaf-to-leaf connections exist.

4. Full mesh requires n(n-1)/2 links. Memorize this formula — the CCNA tests it numerically in scenario questions.

5. A hub-and-spoke topology means all traffic between remote sites must pass through the central hub. This creates a bandwidth bottleneck at the hub.

6. Physical and logical topologies can differ. A Token Ring network was physically wired as a star (through a MAU) but operated logically as a ring. The CCNA sometimes tests this distinction.

7. CDP (Cisco Discovery Protocol) is Layer 2 and vendor-proprietary. LLDP (Link Layer Discovery Protocol) is the IEEE standard equivalent. Both are used to discover neighboring devices.

8. When designing a network, always consider the number of users, the building layout, and future growth requirements before selecting a topology model.

---

## 8. Study Checklist

Work through each item before taking the quiz.

- [ ] Define all 17 glossary terms from memory without looking at notes
- [ ] Sketch a three-tier network diagram from memory, labeling Core, Distribution, and Access layers with example devices at each layer
- [ ] Explain in your own words why ACLs are never applied at the Core layer
- [ ] Describe a scenario where collapsed core is the better choice over three-tier
- [ ] Draw a spine-leaf topology and explain the two-hop rule
- [ ] Calculate the number of links required for a full mesh of 6 nodes
- [ ] Review the CLI command reference table and understand the purpose of each command
- [ ] Complete the Module 01 Packet Tracer lab activity
- [ ] Post your Module 01 discussion response by Wednesday at 11:59 PM
- [ ] Review all 8 CCNA exam tips and confirm you can explain each one

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com
- Cisco Packet Tracer (free download through Cisco Networking Academy): used for all lab exercises in this course

---

## 9. Supplemental Resources

The following open educational resources extend the concepts covered in this module and align directly with CCNA 200-301 exam objectives. All resources are freely available.

1. **Cisco Networking Academy — Network Fundamentals** (skillsforall.com): The "Networking Basics" and "CCNA: Introduction to Networks" courses provide interactive labs and visual animations for three-tier design, spine-leaf architecture, and topology types. These courses are completely free and include built-in Packet Tracer activities.

2. **Jeremy's IT Lab — Free CCNA Course, Day 1–3 (YouTube)**: The opening modules of this CCNA course cover network devices, topology models, and the OSI/TCP-IP models with exam-focused notation. Playlist: youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ

3. **Cisco Learning Network — CCNA Study Group and Exam Topics** (learningnetwork.cisco.com): The Cisco Learning Network provides the official CCNA 200-301 exam topic list, study group discussion threads, and sample questions aligned to Domain 1: Network Fundamentals.

4. **Professor Messer — CompTIA and Cisco Free Study Guides** (professormesser.com): While primarily CompTIA-focused, Professor Messer's networking fundamentals notes on topology types, OSI model, and physical vs. logical topology are directly applicable to CCNA Domain 1 content.

5. **Cisco Packet Tracer Tutorials — Network Topologies Lab** (skillsforall.com/course/getting-started-cisco-packet-tracer): This beginner tutorial guides you through building star, mesh, and three-tier topologies in Packet Tracer and is a strong companion to the Module 01 lab activity.
