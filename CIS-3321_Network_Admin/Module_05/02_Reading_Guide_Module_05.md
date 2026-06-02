# Reading Guide: Module 05 – Network Infrastructure: Cables, Switches, Routers
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 05 covers the physical and data-link layer infrastructure that makes all higher-layer networking possible. The CompTIA Network+ exam tests cabling standards extensively — in both theoretical questions about specifications and practical troubleshooting scenarios where a symptom must be matched to a cable or device limitation. You must also understand how switches build MAC address tables, what happens to unknown unicast frames, and how routers differ from switches at the broadcast domain boundary.

---

### 1. Core Vocabulary

**Twisted Pair Cable** — Copper cable using pairs of wires twisted together to reduce electromagnetic interference (EMI). Used for all standard Ethernet connections.

**Cat5e** — Enhanced Category 5. Maximum 1 Gbps at 100 meters. Minimum recommended standard for new installations.

**Cat6** — Category 6. Maximum 1 Gbps at 100 m or 10 Gbps at 55 m. Includes a plastic separator (spline) between pairs. Standard for current enterprise deployments.

**Cat6a** — Augmented Category 6. Maximum 10 Gbps at 100 m. Eliminates alien crosstalk. Required for 10GBase-T at full distance. Thicker and less flexible than Cat6.

**Cat8** — Supports 25–40 Gbps at 30 m maximum. Primarily for data center short-run connections.

**Single-Mode Fiber (SMF)** — Narrow core (8–10 µm) carrying a single light mode. Long distance (up to 100+ km). Uses laser light sources. Higher cost.

**Multi-Mode Fiber (MMF)** — Wider core (50 or 62.5 µm) carrying multiple light modes. Shorter distances (up to 550 m for OM3/OM4). Uses LED or VCSEL. Lower cost for short runs.

**OM Rating** — Multi-mode fiber bandwidth/distance classification: OM1 (62.5 µm), OM2 (50 µm), OM3 (50 µm, 300 m for 10GbE), OM4 (50 µm, 400 m for 10GbE), OM5 (50 µm, 100 Gbps capable).

**Straight-Through Cable** — Both ends wired with the same standard (T568A–T568A or T568B–T568B). Connects unlike devices (PC to switch, switch to router).

**Crossover Cable** — One end T568A, one end T568B. Historically connects like devices (switch to switch, PC to PC). Obsolete due to Auto-MDIX.

**Auto-MDIX** — Automatic Medium-Dependent Interface Crossover. Switch/NIC feature that automatically detects whether a straight-through or crossover cable is connected and adjusts pin assignment accordingly.

**Rollover/Console Cable** — Flat cable (often blue) with reverse pin mapping. RJ-45 to DB9/USB. Used for Cisco device initial CLI configuration via console port.

**Hub** — Layer 1 repeater. Floods all incoming signals to all ports. Single collision domain. Obsolete.

**Switch** — Layer 2 device. Forwards frames based on destination MAC address. Builds MAC address table (CAM table). Separate collision domain per port. Supports full duplex.

**CAM Table** — Content Addressable Memory table in a switch. Maps MAC addresses to physical ports. Built dynamically by reading source MAC addresses. Entries age out after timeout period (default 300 seconds).

**Unknown Unicast Flooding** — Behavior when a switch receives a frame with a destination MAC address not in the CAM table. Switch floods the frame out all ports except the source port.

**Collision Domain** — A network segment where only one device can transmit at a time. Hub = one collision domain for all ports. Switch = one collision domain per port.

**Broadcast Domain** — A group of devices that receive each other's broadcasts. Switches extend broadcast domains (all ports in the same VLAN = same broadcast domain). Routers separate broadcast domains.

**Router** — Layer 3 device that forwards packets between different IP subnets using a routing table. Each interface is a different subnet and broadcast domain.

**Layer 3 Switch (Multilayer Switch)** — Switch that performs both Layer 2 switching and Layer 3 inter-VLAN routing in hardware. Uses Switched Virtual Interfaces (SVIs) as VLAN gateways.

**SVI (Switched Virtual Interface)** — A logical Layer 3 interface on a Layer 3 switch assigned to a VLAN. Acts as the default gateway for hosts in that VLAN.

**PoE (Power over Ethernet)** — Delivers DC power to remote devices over Cat5e/Cat6 cables. Eliminates need for separate power adapters.

**IEEE 802.3af** — PoE standard. Up to 15.4 watts per port.

**IEEE 802.3at** — PoE+ standard. Up to 30 watts per port.

**IEEE 802.3bt** — PoE++ standard. Up to 60 W (Type 3) or 100 W (Type 4) per port.

**SFP (Small Form-factor Pluggable)** — Hot-swappable transceiver module for switch/router ports. Supports different media types (copper, SMF, MMF) and speeds (1 Gbps). SFP+ supports 10 Gbps.

**GBIC (Gigabit Interface Converter)** — Older, larger hot-swappable transceiver. Replaced by SFP in modern equipment.

---

### 2. Copper Cable Category Comparison Table

| Category | Max Speed   | Max Distance | 10 Gbps Distance | Notes                                    |
|----------|------------|--------------|------------------|------------------------------------------|
| Cat3     | 10 Mbps    | 100 m        | Not supported    | Legacy voice-grade; do not use for data  |
| Cat5     | 100 Mbps   | 100 m        | Not supported    | Obsolete; replaced by Cat5e              |
| Cat5e    | 1 Gbps     | 100 m        | Not supported    | Minimum for new installations            |
| Cat6     | 1 Gbps     | 100 m        | 55 m             | Standard enterprise; spline separator    |
| Cat6a    | 10 Gbps    | 100 m        | 100 m            | Full 10GbE at distance; required for 10GBase-T |
| Cat7     | 10 Gbps    | 100 m        | 100 m            | Uses GG45/TERA connectors; rarely deployed |
| Cat8     | 25–40 Gbps | 30 m         | 30 m             | Data center rack cabling only            |

---

### 3. Fiber Optic Comparison Table

| Type       | Core Diameter | Light Source | Max Distance     | Typical Use                          |
|------------|---------------|--------------|------------------|--------------------------------------|
| SMF OS1    | 8–10 µm       | Laser        | Up to 10 km      | Campus/WAN backbone                  |
| SMF OS2    | 8–10 µm       | Laser        | Up to 200 km     | Long-haul/metro fiber                |
| MMF OM1    | 62.5 µm       | LED          | 33 m (10GbE)     | Legacy; not recommended for new work |
| MMF OM2    | 50 µm         | LED          | 82 m (10GbE)     | Legacy                               |
| MMF OM3    | 50 µm         | VCSEL        | 300 m (10GbE)    | Current standard short-run           |
| MMF OM4    | 50 µm         | VCSEL        | 400 m (10GbE)    | Enhanced short-run                   |
| MMF OM5    | 50 µm         | VCSEL        | 150 m (100 Gbps) | Data center 100GbE                   |

---

### 4. Switch MAC Address Learning Process

When a frame arrives at a switch:

1. The switch reads the source MAC address from the frame header.
2. If the source MAC is not in the CAM table, the switch adds it, associating it with the incoming port.
3. The switch reads the destination MAC address.
4. If the destination MAC is in the CAM table (known unicast): forward the frame only to the port associated with that MAC address.
5. If the destination MAC is not in the CAM table (unknown unicast): flood the frame out all ports except the source port.
6. If the destination is FF:FF:FF:FF:FF:FF (broadcast): flood out all ports except source port.
7. CAM table entries age out after 300 seconds of inactivity (default). The next frame from that device triggers re-learning.

---

### 5. Hub vs. Switch vs. Router Comparison

| Characteristic        | Hub (Layer 1)         | Switch (Layer 2)            | Router (Layer 3)               |
|-----------------------|-----------------------|-----------------------------|--------------------------------|
| OSI Layer             | 1 (Physical)          | 2 (Data Link)               | 3 (Network)                    |
| Forwarding basis      | Repeats all signals   | Destination MAC address      | Destination IP address         |
| Collision domains     | 1 (shared)            | 1 per port                  | 1 per interface                |
| Broadcast domains     | 1                     | 1 per VLAN                  | 1 per interface (separate)     |
| Intelligence          | None                  | MAC table (CAM)             | Routing table                  |
| Unknown unicast       | Floods all ports      | Floods all except source    | Does not forward (drops or routes) |
| Full duplex           | No (CSMA/CD required) | Yes (per port)              | Yes                            |
| Modern use            | Obsolete              | Universal LAN device         | WAN/inter-subnet routing       |

---

### 6. PoE Standards Reference Table

| Standard     | Max Power per Port | Common Applications                                   |
|--------------|--------------------|-------------------------------------------------------|
| 802.3af (PoE)| 15.4 W             | IP phones, single-radio APs, basic IP cameras         |
| 802.3at (PoE+)| 30 W              | Dual-radio APs, PTZ cameras, video phones             |
| 802.3bt Type 3 (UPoE)| 60 W    | Multi-radio APs, building automation                  |
| 802.3bt Type 4 (UPoE+)| 100 W  | Laptops, advanced devices                             |

PoE requires a PoE-capable switch (PSE — Power Sourcing Equipment) or a PoE injector (midspan device). The powered device (PD) negotiates power level using LLDP-MED or Cisco Discovery Protocol.

---

### 7. Fiber Connector Types Reference

| Connector | Description                                | Common Use                               |
|-----------|--------------------------------------------|------------------------------------------|
| LC        | Small form factor, latch mechanism         | Enterprise switch SFP ports; most common |
| SC        | Square connector, push-pull                | Older infrastructure                     |
| ST        | Bayonet twist-lock connector               | Legacy installations                     |
| MTP/MPO   | Multi-fiber connector (12 or 24 fibers)   | Data center trunk cables                 |
| FC        | Threaded connector                         | Telecom and test equipment               |

---

### 8. Certification Exam Tips

**Tip 1:** The 100-meter maximum for twisted-pair Ethernet applies to all categories including Cat6a. Exceeding 100 meters causes signal attenuation. The solution is always to add a switch at or before 100 meters.

**Tip 2:** Cat6 supports 10 Gbps only at 55 meters, not 100 meters, due to alien crosstalk. Cat6a eliminates alien crosstalk and achieves 10 Gbps at the full 100-meter distance.

**Tip 3:** SMF for long distances (campus backbone, WAN), MMF for short distances (building runs, data center). If the exam scenario involves anything over 1 km, the answer is always single-mode fiber.

**Tip 4:** A switch performing "unknown unicast flooding" is not a malfunction — it is normal behavior. Flooding occurs when the destination MAC is not in the CAM table. The switch learns the MAC after the destination device responds.

**Tip 5:** Hubs create one collision domain for all ports; switches create one collision domain per port. Switches (like hubs) extend one broadcast domain per VLAN. Only routers (or Layer 3 switches) create separate broadcast domains.

**Tip 6:** PoE wattage is critical. 802.3af = 15.4W for phones and basic APs. 802.3at = 30W for dual-radio APs and PTZ cameras. If the exam describes a high-power device (laptop, industrial sensor), 802.3bt is the answer.

**Tip 7:** Auto-MDIX eliminates the need to use a crossover cable for like-device connections in modern equipment. The exam still tests the concept of which cable type was required before Auto-MDIX, but in practice you will never need to carry crossover cables.

**Tip 8:** SFP modules allow a single switch port to support different media types (copper, MMF, SMF) and speeds without replacing the switch. This is the answer when the exam describes a need for media flexibility or a port type upgrade on existing hardware.

---

### 9. Required Reading and Viewing

**Required Reading:** Computer Networking: Principles, Protocols and Practice — read the sections on network media, cables, and switching. Focus on the cable specifications and Layer 2 forwarding process.

**Required Viewing:** Professor Messer's Network+ N10-008 video series — watch the copper cabling, fiber optic, and networking devices segments. Available free at professormesser.com.

**Supplemental Reference:** CompTIA official N10-008 exam objectives at comptia.org — review Domain 2.0 Network Implementations and Domain 5.0 Network Troubleshooting for cabling and device objectives.

---

### 10. Study Checklist

- [ ] Memorize the cable category comparison table — speeds and distances for Cat5e, Cat6, Cat6a
- [ ] Distinguish single-mode from multi-mode fiber by core size, light source, and maximum distance
- [ ] Explain how a switch builds its MAC address table and what triggers unknown unicast flooding
- [ ] Describe the difference between a collision domain and a broadcast domain
- [ ] Identify which device separates broadcast domains (router or Layer 3 switch)
- [ ] Know the three PoE standards (802.3af, 802.3at, 802.3bt) and their wattage limits
- [ ] Explain when a crossover cable was required and why Auto-MDIX makes it obsolete
- [ ] Describe the purpose of the rollover/console cable
- [ ] Watch Professor Messer's cabling and switching videos at professormesser.com
- [ ] Read the network media and switching chapters in the OER textbook
- [ ] Complete the Lab 05 Packet Tracer switching activity
- [ ] Post your Module 05 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 05 Quiz

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
