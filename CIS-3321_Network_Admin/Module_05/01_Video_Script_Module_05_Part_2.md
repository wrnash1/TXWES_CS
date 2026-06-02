# Video Script: Module 05 – Network Infrastructure: Cables, Switches, Routers
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 11–13 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 05 Part 2 — Switches, Routers, Layer 3 Switching, and PoE"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 05. In Part 1 we covered copper cabling categories, fiber optic specifications, and cable type distinctions. Now in Part 2 we examine the active network devices: hubs, switches, and routers. We look at exactly how a switch makes forwarding decisions, how routers separate broadcast domains, and two key technologies — Layer 3 switching and Power over Ethernet.

---

### Section 2: Hubs — Legacy Layer 1 Devices

[00:45 – 02:30]

[SHOW DIAGRAM: A hub in the center connected to four workstations. An arrow shows a broadcast from PC A flooding out all four ports simultaneously, including back to PC B, C, and D.]

[Alt-text: A diagram showing a hub device in the center connected to four workstations labeled PC A, PC B, PC C, and PC D. An arrow labeled "Data from PC A" leaves PC A and reaches the hub. Four separate arrows then show the same data being sent out to PC B, PC C, PC D, and even back to the port direction of PC A simultaneously, illustrating hub flooding behavior.]

A hub is a Layer 1 device — the simplest type of network device. When a signal arrives on any port, the hub repeats that electrical signal out every other port simultaneously. It has no intelligence — it does not look at MAC addresses, IP addresses, or any frame content. It is purely a signal repeater.

The consequence of this design is that all devices connected to a hub share a single collision domain. Only one device can transmit at a time. When two devices transmit simultaneously, a collision occurs. All devices must run CSMA/CD (Carrier Sense Multiple Access with Collision Detection) to manage collisions.

In modern networks, hubs are obsolete. You will not install a hub in a new deployment. However, the Network+ exam still tests hub behavior because understanding what a hub does wrong explains why switches are better.

---

### Section 3: Switches — Layer 2 Intelligent Forwarding

[02:30 – 06:30]

[SHOW DIAGRAM: A switch with a CAM table visible. The table shows four entries: Port 1 → MAC 00:AA:BB:CC:DD:01, Port 2 → MAC 00:AA:BB:CC:DD:02, Port 3 → MAC 00:AA:BB:CC:DD:03, Port 4 → MAC 00:AA:BB:CC:DD:04. An arrow shows PC A sending a frame to PC C — the switch looks up the destination MAC, finds it on Port 3, and forwards only to Port 3.]

[Alt-text: A diagram showing a managed switch with a MAC address table (CAM table) displayed to the side. The table has two columns: Port and MAC Address. Row 1: Port 1, MAC 00:AA:BB:CC:DD:01. Row 2: Port 2, MAC 00:AA:BB:CC:DD:02. Row 3: Port 3, MAC 00:AA:BB:CC:DD:03. Row 4: Port 4, MAC 00:AA:BB:CC:DD:04. An arrow labeled "Frame to 00:AA:BB:CC:DD:03" travels from the PC on Port 1 to the switch, and only a single outbound arrow goes to Port 3, bypassing Ports 2 and 4.]

A switch is a Layer 2 device that makes intelligent forwarding decisions based on MAC addresses. Each port on a switch is its own collision domain — full duplex communication is possible on every port simultaneously.

The switch builds its MAC address table (also called the CAM table — Content Addressable Memory) dynamically. Here is the process.

When a frame arrives on a switch port, the switch reads the source MAC address in the Ethernet frame header and records it in the CAM table, associated with the port it arrived on. This is called MAC address learning.

When the switch needs to forward a frame, it reads the destination MAC address and looks it up in the CAM table.

If the destination MAC is found (known unicast), the switch forwards the frame only to the specific port where that MAC was last seen. This is called unicast forwarding.

If the destination MAC is not found (unknown unicast), the switch floods the frame out every port except the port it arrived on. This is called unknown unicast flooding. It happens when a device has never communicated before or when the MAC address has aged out of the table.

If the destination is a broadcast address (FF:FF:FF:FF:FF:FF), the switch floods the frame out every port except the source port. All devices in the VLAN receive it.

The CAM table has an aging timer (typically 300 seconds). If no frames are received from a MAC address within the aging period, the entry is removed. The next frame from that device causes re-learning.

> **Network+ Exam Tip:** The exam describes behavior and asks you to identify the device type. "Floods all ports except source port" is a switch responding to an unknown unicast — not a hub (which floods always) and not a router (which routes to a different network). Know the distinction.

---

### Section 4: Routers — Layer 3 Boundary Devices

[06:30 – 09:00]

[SHOW DIAGRAM: A router with two interfaces — Gi0/0 connected to subnet 192.168.1.0/24 (PC A and PC B) and Gi0/1 connected to subnet 192.168.2.0/24 (PC C and PC D). An arrow shows PC A sending a packet to PC C. The packet crosses the router. A routing table is shown with two entries: 192.168.1.0/24 via Gi0/0 and 192.168.2.0/24 via Gi0/1.]

[Alt-text: A network diagram showing a router in the center with two interfaces labeled Gi0/0 and Gi0/1. Connected to Gi0/0 are two PCs on the 192.168.1.0/24 subnet. Connected to Gi0/1 are two more PCs on the 192.168.2.0/24 subnet. A routing table to the side shows two entries: 192.168.1.0/24 is directly connected via Gi0/0, and 192.168.2.0/24 is directly connected via Gi0/1. An arrow shows a packet from 192.168.1.10 crossing through the router to reach 192.168.2.10.]

A router is a Layer 3 device that forwards packets between different networks (subnets). While a switch handles frames on a single network segment, a router connects separate network segments. Each router interface is a different subnet and a separate broadcast domain.

When a packet arrives at a router, the router reads the destination IP address in the packet header and looks it up in its routing table. The routing table contains entries for networks the router knows how to reach, along with the next-hop address or outbound interface.

Routers create broadcast domain boundaries. A broadcast from 192.168.1.0/24 does not cross the router to 192.168.2.0/24. This is critical for network scalability — as networks grow, you do not want broadcasts reaching every device on the entire network.

Routers can be dedicated hardware devices (Cisco ISR series, for example) or they can be software-based on a general-purpose server. In modern enterprise networks, the routing and firewall functions are often combined in a unified device.

---

### Section 5: Layer 3 Switches and PoE

[09:00 – 11:30]

[SHOW DIAGRAM: Side-by-side comparison. Left: Traditional setup with a Layer 2 switch and a separate router connected by a trunk link. Right: A single Layer 3 switch handling both switching within VLANs and routing between VLANs internally.]

[Alt-text: Two topology diagrams. Left diagram shows a Layer 2 switch connected to a separate external router via a trunk link. Three PCs on different VLANs connect to the switch. Traffic between VLANs must traverse the trunk link to reach the router and be routed back. Right diagram shows a single Layer 3 switch. Three PCs on different VLANs connect directly to the Layer 3 switch, which handles both switching within VLANs and inter-VLAN routing internally without an external router.]

**Layer 3 Switch (Multilayer Switch)** — A switch that performs both Layer 2 switching and Layer 3 routing within the same hardware ASIC (Application-Specific Integrated Circuit). Used for inter-VLAN routing in campus LAN environments. More efficient than routing through an external router because the switching and routing happen in hardware rather than in software. Layer 3 switches create Switched Virtual Interfaces (SVIs) — logical IP interfaces for each VLAN — that act as the default gateway for hosts in that VLAN.

**Power over Ethernet (PoE)** — Technology defined by IEEE standards that delivers DC electrical power over the same Cat5e or Cat6 copper cable that carries data. This eliminates the need for a separate power adapter at the remote device.

Three common PoE standards:

IEEE 802.3af — PoE. Delivers up to 15.4 watts per port. Sufficient for basic IP phones, access points with a single radio, and basic IP cameras.

IEEE 802.3at — PoE+ (PoE Plus). Delivers up to 30 watts per port. Sufficient for dual-radio access points, PTZ (pan-tilt-zoom) cameras, and video phones.

IEEE 802.3bt — PoE++ (UPoE or 4PPoE). Delivers up to 60 watts (Type 3) or 100 watts (Type 4) per port. Used for laptops, multi-radio access points, and building automation devices.

Common PoE-powered devices: IP phones, wireless access points, IP security cameras, door access control readers, and LED lighting controllers.

> **Network+ Exam Tip:** The exam will describe a device and ask which PoE standard is appropriate. Know the wattage tiers. If the question says "VoIP phone or basic AP," the answer is 802.3af (15.4W). If it says "dual-radio AP or PTZ camera," 802.3at/PoE+ (30W). Match the wattage requirement to the standard.

---

### Section 6: Module Closing and Lab Preview

[SHOW SLIDE: Lab preview — Packet Tracer switch MAC table observation]

In this week's lab, you will build a switched network in Cisco Packet Tracer and use the `show mac address-table` command on a switch to observe how MAC addresses are learned and stored. You will also test what happens when you send traffic to an unknown destination — observing the flooding behavior in Simulation Mode.

Module 05 key takeaways: Cat5e supports 1 Gbps at 100m. Cat6 supports 10 Gbps at 55m. Cat6a supports 10 Gbps at 100m. SMF for long distances; MMF for short campus runs. Hubs flood everything; switches forward intelligently. Routers separate broadcast domains. Layer 3 switches route between VLANs internally. PoE delivers power over data cables.

In Module 06 we shift to wireless networking — 802.11 standards, frequency bands, and Wi-Fi security protocols.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
