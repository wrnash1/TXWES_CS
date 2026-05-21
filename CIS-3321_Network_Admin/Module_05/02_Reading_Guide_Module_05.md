# Reading Guide: Module 05 - Network Infrastructure – Cables, Switches, Routers
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 05 – Network Infrastructure: Cables, Switches, and Routers**! The physical and data-link layer components that form a network's foundation are tested throughout the CompTIA Network+ N10-009 exam. You must be able to identify cable types by specification, match them to their use cases, explain how switches build and use MAC address tables, and describe the differences between Layer 2 and Layer 3 devices. This module covers the hardware that makes all higher-layer protocols possible.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cat5e**: Enhanced Category 5 twisted-pair copper cable. Supports up to **1 Gbps** at 100 meters. The minimum recommended standard for new installations. Uses 8P8C (RJ-45) connectors.
*   **Cat6**: Category 6 twisted-pair cable. Supports **1 Gbps at 100 m** or **10 Gbps at 55 m** with reduced crosstalk. Uses a separator spline between pairs. Standard for new enterprise deployments.
*   **Cat6a**: Augmented Category 6. Supports **10 Gbps at 100 m** with full alien crosstalk elimination. Required for 10GBase-T at full distance. Thicker and less flexible than Cat6.
*   **Single-Mode Fiber (SMF)**: Fiber optic cable with a very narrow core (~8–10 µm) that carries a single light ray. Used for long-distance connections (up to 100+ km). Uses laser light sources. Higher cost per meter than MMF.
*   **Multi-Mode Fiber (MMF)**: Fiber optic cable with a wider core (50 or 62.5 µm) that carries multiple light rays. Used for shorter distances (up to ~550 m for OM3/OM4). Uses LED or VCSEL light sources. Lower cost than SMF for short runs.
*   **Straight-Through Cable**: A patch cable where both ends use the same wiring standard (T568A–T568A or T568B–T568B). Used to connect unlike devices: host-to-switch, switch-to-router.
*   **Crossover Cable**: A patch cable where one end uses T568A and the other T568B, crossing the transmit and receive pairs. Historically used to connect like devices (switch-to-switch, host-to-host). Largely obsolete due to **Auto-MDIX**, which automatically detects and corrects cable type.
*   **Rollover/Console Cable**: A flat cable (often light blue, RJ-45 to DB9 or USB) where pin 1 on one end connects to pin 8 on the other. Used exclusively to connect a PC to a Cisco router or switch console port for initial configuration.
*   **Hub**: A Layer 1 device that repeats all incoming signals out all ports simultaneously, creating a single collision domain. All devices on a hub share bandwidth and must use CSMA/CD. Obsolete in modern networks.
*   **Switch**: A Layer 2 device that forwards frames based on destination MAC addresses, creating a separate collision domain per port. Builds a MAC address table (CAM table) by learning source MAC addresses. Provides dedicated bandwidth per port.
*   **MAC Address Table (CAM Table)**: The switch's memory structure mapping MAC addresses to the physical port where each device was last seen. When a destination MAC is unknown, the switch floods the frame out all ports except the source port (unknown unicast flooding).
*   **Router**: A Layer 3 device that forwards packets between different networks (subnets) based on destination IP addresses and a routing table. Creates separate broadcast domains. Connects LANs to WANs and the internet.
*   **Layer 3 Switch (Multilayer Switch)**: A switch that can perform both Layer 2 switching and Layer 3 routing within the same hardware. Used for inter-VLAN routing. More efficient than a separate router for campus LAN environments.
*   **PoE (Power over Ethernet)**: IEEE 802.3af (15.4W per port) and 802.3at/PoE+ (30W per port) standards that deliver DC power over Cat5e/Cat6 cables to devices such as IP phones, wireless access points, and IP cameras — eliminating the need for separate power adapters.
*   **SFP (Small Form-factor Pluggable)**: A hot-swappable transceiver module inserted into a switch or router port to support different media types (copper, single-mode fiber, multi-mode fiber) and speeds (1 Gbps, 10 Gbps for SFP+). Allows flexible port configuration without replacing the entire device.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** Cabling and infrastructure fall under **Domain 2.0 – Network Implementations (20%)** and **Domain 5.0 – Network Troubleshooting (23%)**. Cable identification appears in both theoretical and troubleshooting scenarios.
*   **Cable distance limits — memorize these**: Cat5e/Cat6 = 100 m maximum for all speeds; Cat6a = 100 m for 10 Gbps; MMF OM3 = 300 m for 10GbE; SMF = kilometers. Exceeding these limits causes attenuation errors.
*   **Straight-through vs. crossover shortcut**: The exam almost never requires you to wire cables manually, but you must know which type connects which devices. In modern networks, Auto-MDIX makes this mostly irrelevant — but the exam still tests it conceptually.
*   **Hub vs. switch collision domains**: A hub is one collision domain for all ports; a switch is one collision domain per port. Both hub and switch form one broadcast domain per VLAN (switches can have multiple broadcast domains with VLANs; hubs cannot).
*   **PoE wattage matters**: 802.3af = 15.4W (enough for IP phones, basic APs); 802.3at/PoE+ = 30W (enough for PTZ cameras, dual-radio APs); 802.3bt/PoE++ = 60–100W (enough for laptops). The exam tests which standard supports which device type.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers all cable standards, connector types, and switching fundamentals in the Network Implementations domain section.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **Network Media, Cables, and Switching** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the physical layer cable specifications and the data-link layer switching operation.
*   **Required Video:** Watch Professor Messer's **Copper Cabling**, **Fiber Optic Cabling**, and **Networking Devices** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will use Cisco Packet Tracer to build a switched network, observe MAC address table population using `show mac address-table`, and compare the behavior of a hub versus a switch by examining which ports receive broadcast and unicast frames.

---

### 3. Study Checklist
*   [ ] Memorize cable categories (Cat5e, Cat6, Cat6a), their maximum speeds, and maximum distances.
*   [ ] Know the difference between single-mode and multi-mode fiber and their use cases.
*   [ ] Understand how a switch builds its MAC address table and what happens on an unknown unicast.
*   [ ] Know the PoE standards (802.3af, 802.3at) and their wattage limits.
*   [ ] Read the **Network Media and Switching** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's cabling and switching videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
