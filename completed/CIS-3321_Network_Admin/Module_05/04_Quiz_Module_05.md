# Quiz: Module 05 – Network Infrastructure: Cables, Switches, Routers
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

**Instructions:** Select the best answer for each question. Each question is worth 10 points (100 points total).

---

**Question 1**

A network technician needs to support 10 Gbps Ethernet over copper at the full 100-meter distance. Which cable standard meets this requirement?

A) Cat5e

B) Cat6

C) Cat6a

D) Cat3

- **Correct Answer:** C) Cat6a
- **Distractor Analysis:**
  - *Why A is incorrect:* Cat5e supports a maximum of 1 Gbps at 100 m; it cannot carry 10 Gbps over copper at any useful distance.
  - *Why B is incorrect:* Cat6 supports 10 Gbps but only up to 55 m due to alien crosstalk; it cannot reliably achieve 100 m at 10 Gbps.
  - *Why C is correct:* Cat6a (Augmented Category 6) eliminates alien crosstalk and supports 10 Gbps at the full 100-meter maximum distance for twisted-pair Ethernet.
  - *Why D is incorrect:* Cat3 is a legacy voice-grade cable rated for 10 Mbps; it is completely unsuitable for 10 Gbps data transmission.

---

**Question 2**

A switch receives a frame destined for a MAC address that is not in its CAM table. Which action does the switch take?

A) Drops the frame and sends an ICMP Destination Unreachable message to the source.

B) Forwards the frame only to the default gateway port for routing.

C) Floods the frame out all ports except the port it was received on.

D) Sends an ARP request on behalf of the source to discover the destination MAC.

- **Correct Answer:** C) Floods the frame out all ports except the port it was received on.
- **Distractor Analysis:**
  - *Why A is incorrect:* Switches do not drop frames for unknown destinations or generate ICMP messages — that is a Layer 3 router function. Unknown-destination frames are flooded, not dropped.
  - *Why B is incorrect:* A switch forwards based on MAC addresses at Layer 2; it does not route to a default gateway. Routing is performed by Layer 3 devices.
  - *Why C is correct:* Unknown unicast flooding is the standard switch behavior for frames with an unknown destination MAC. The switch floods out all ports except the source to ensure the frame reaches its destination, allowing the destination to respond and be learned.
  - *Why D is incorrect:* ARP is initiated by end hosts to resolve IP-to-MAC mappings; a switch does not send ARP requests on behalf of sources. The switch simply floods the unknown-destination frame.

---

**Question 3**

A wireless access point in a remote location has no nearby power outlet. The network closet is 40 meters away, connected via Cat5e. Which technology eliminates the need for a separate power adapter at the access point?

A) Fiber optic uplink with a media converter

B) Power over Ethernet (PoE) via IEEE 802.3af or 802.3at

C) A crossover cable to connect the AP directly to the router

D) An SFP transceiver module installed in the AP

- **Correct Answer:** B) Power over Ethernet (PoE) via IEEE 802.3af or 802.3at
- **Distractor Analysis:**
  - *Why A is incorrect:* Fiber optic cabling carries data using light and cannot deliver electrical power to a remote device; a media converter would only handle signal conversion.
  - *Why B is correct:* PoE (802.3af up to 15.4W, 802.3at/PoE+ up to 30W) delivers DC power over the same Cat5e cable carrying data. A PoE-capable switch or PoE injector provides power without requiring a separate electrical outlet at the AP.
  - *Why C is incorrect:* A crossover cable is a wiring convention for connecting like devices; it carries data only and does not deliver power to remote equipment.
  - *Why D is incorrect:* An SFP module is a pluggable transceiver that changes the physical media type of a port; it is a data-layer component and has no power-delivery function.

---

**Question 4**

A network segment experiences frequent collisions and slow performance. Investigation reveals all workstations share a single device where every incoming signal is repeated out every port simultaneously. Which device is causing this behavior, and what should replace it?

A) The device is a Layer 2 switch; replace it with a Layer 3 switch for inter-VLAN routing.

B) The device is a hub; replace it with a managed switch to give each device its own collision domain.

C) The device is a router; replace it with a firewall to control inter-network traffic.

D) The device is a wireless access point operating in bridge mode; replace it with one in access point mode.

- **Correct Answer:** B) The device is a hub; replace it with a managed switch to give each device its own collision domain.
- **Distractor Analysis:**
  - *Why A is incorrect:* A switch forwards frames based on MAC addresses to individual ports — it does not repeat all signals out all ports. The described behavior is specific to hubs.
  - *Why B is correct:* A hub is a Layer 1 device that repeats incoming signals to all ports, creating a single shared collision domain. Replacing it with a switch gives each port its own collision domain and eliminates collisions through full-duplex operation.
  - *Why C is incorrect:* A router makes Layer 3 forwarding decisions based on IP addresses between different networks; it does not broadcast all signals to all ports on a segment.
  - *Why D is incorrect:* A wireless AP in bridge mode connects two wired segments wirelessly; it does not cause the Layer 1 signal-flooding behavior described.

---

**Question 5**

A security administrator wants to prevent unauthorized devices from connecting to open switch ports in a corporate office. Which combination of controls provides the most effective defense?

A) Enable IEEE 802.1X port authentication on all access ports and configure Port Security with sticky MAC learning as a backup.

B) Disable unused switch ports in the configuration and place them in an unused VLAN.

C) Deploy network-based IDS sensors on each floor to detect unauthorized connection attempts.

D) Require all users to register their MAC addresses manually with the help desk before connecting.

- **Correct Answer:** A) Enable IEEE 802.1X port authentication on all access ports and configure Port Security with sticky MAC learning as a backup.
- **Distractor Analysis:**
  - *Why A is correct:* 802.1X requires authentication credentials before a port grants network access; Port Security with sticky MAC limits which physical device can use the port — together these form a layered, automated defense.
  - *Why B is incorrect:* Disabling unused ports reduces exposure but does not protect active ports, which remain open for any device to connect.
  - *Why C is incorrect:* An IDS detects and alerts on unauthorized connections after they occur; it does not prevent the initial connection from being established.
  - *Why D is incorrect:* Manual MAC registration is administratively burdensome, easily bypassed via MAC spoofing, and provides no automated enforcement at the port level.

---

**Question 6**

A network engineer is connecting two Cisco switches together without Auto-MDIX support. Which cable type is required to correctly cross the transmit and receive pairs between the two switches?

A) Straight-through cable

B) Rollover/console cable

C) Crossover cable

D) Coaxial cable

- **Correct Answer:** C) Crossover cable
- **Distractor Analysis:**
  - *Why A is incorrect:* A straight-through cable connects unlike devices (PC to switch, switch to router). Connecting two switches with a straight-through cable without Auto-MDIX would result in both switches transmitting on the same wire pair, causing a failed link.
  - *Why B is incorrect:* A rollover/console cable is a flat cable with reversed pin mapping used for console port (CLI) access to network devices, not for switch-to-switch data links.
  - *Why C is correct:* A crossover cable (T568B on one end, T568A on the other) crosses the transmit pair on one switch to the receive pair on the other, enabling proper full-duplex communication between like devices.
  - *Why D is incorrect:* Coaxial cable was used in legacy bus topology networks and is not used for modern switch interconnects.

---

**Question 7**

A network design calls for a 400-meter fiber run between two campus buildings for a 10 Gbps backbone connection. Which fiber type is the most appropriate?

A) Single-mode fiber OS1

B) Multi-mode fiber OM1

C) Multi-mode fiber OM4

D) Cat6a copper twisted pair

- **Correct Answer:** C) Multi-mode fiber OM4
- **Distractor Analysis:**
  - *Why A is incorrect:* While single-mode fiber OS1 would absolutely work for this distance and speed (it exceeds OM4 in distance capability), OM4 is sufficient for 400 m at 10 Gbps and is less expensive than SMF for intra-campus runs. In a cost-optimized scenario, OM4 is the correct answer for 400 m.
  - *Why B is incorrect:* OM1 (62.5 µm) supports only 33 meters for 10 GbE — far too short for a 400-meter run.
  - *Why C is correct:* OM4 multi-mode fiber supports 10 Gbps at up to 400 meters. This meets the design requirement exactly and at lower cost than SMF.
  - *Why D is incorrect:* Cat6a copper is limited to 100 meters maximum. A 400-meter run requires fiber.

---

**Question 8**

Which of the following correctly describes the difference between a collision domain and a broadcast domain?

A) A collision domain is defined by the subnet mask; a broadcast domain is defined by the switch VLAN.

B) A collision domain is a segment where simultaneous transmissions cause interference; a broadcast domain is a group of devices that receive each other's broadcast frames.

C) A collision domain is created by a router separating subnets; a broadcast domain is created by a hub repeating signals.

D) A collision domain and a broadcast domain are the same thing when switches are used.

- **Correct Answer:** B) A collision domain is a segment where simultaneous transmissions cause interference; a broadcast domain is a group of devices that receive each other's broadcast frames.
- **Distractor Analysis:**
  - *Why A is incorrect:* Collision domains are defined by physical layer devices and switch port isolation, not subnet masks. Broadcast domains are separated by routers and VLANs, not just VLANs.
  - *Why B is correct:* A collision domain is defined at Layer 1/2 — it is the segment where only one device may transmit at a time and simultaneous transmissions cause collisions. A switch creates one collision domain per port. A broadcast domain is defined at Layer 2/3 — all devices that receive a broadcast from any member. Switches extend broadcast domains; routers and VLANs separate them.
  - *Why C is incorrect:* Routers separate broadcast domains, not collision domains. Hubs create collision domains, not broadcast domains specifically.
  - *Why D is incorrect:* Switches create separate collision domains per port but still share one broadcast domain (per VLAN) across all ports. These are fundamentally different concepts.

---

**Question 9**

A Layer 3 switch is being used for inter-VLAN routing in a campus network. Which logical interface type on the switch acts as the default gateway for hosts in each VLAN?

A) Physical FastEthernet access port

B) VLAN trunk port (802.1Q)

C) Switched Virtual Interface (SVI)

D) Serial WAN interface

- **Correct Answer:** C) Switched Virtual Interface (SVI)
- **Distractor Analysis:**
  - *Why A is incorrect:* A physical access port connects an end device to a specific VLAN but does not function as a gateway IP interface for inter-VLAN routing.
  - *Why B is incorrect:* A trunk port carries tagged traffic for multiple VLANs between switches; it does not function as an IP gateway for host traffic.
  - *Why C is correct:* An SVI (Switched Virtual Interface) is a logical Layer 3 interface associated with a VLAN on a Layer 3 switch. It is assigned an IP address and functions as the default gateway for all hosts in that VLAN, enabling inter-VLAN routing.
  - *Why D is incorrect:* A serial WAN interface connects to wide area network circuits; it is not used for inter-VLAN routing within a campus LAN.

---

**Question 10**

A company is installing wireless access points throughout a large office building. The APs are dual-radio (2.4 GHz and 5 GHz) models that require 25 watts each. The installed switch supports 802.3af but not 802.3at. What is the problem, and what is the correct solution?

A) There is no problem; 802.3af delivers 25 watts per port by default.

B) The switch supports only 15.4 watts per port (802.3af); upgrade to a switch supporting 802.3at to deliver the required 30 watts per port.

C) Dual-radio APs require fiber uplinks; install a media converter between the switch and each AP.

D) The switch must be configured with a dedicated PoE VLAN to allocate additional power.

- **Correct Answer:** B) The switch supports only 15.4 watts per port (802.3af); upgrade to a switch supporting 802.3at to deliver the required 30 watts per port.
- **Distractor Analysis:**
  - *Why A is incorrect:* 802.3af delivers a maximum of 15.4 watts per port, not 25 watts. It is insufficient for a 25-watt dual-radio AP.
  - *Why B is correct:* 802.3af (PoE) is limited to 15.4W per port. Dual-radio APs requiring 25W need 802.3at (PoE+), which delivers up to 30W per port. Upgrading the switch to 802.3at-capable hardware is the correct solution.
  - *Why C is incorrect:* Fiber uplinks are a cabling medium choice, not a PoE power delivery mechanism. Media converters carry data, not electrical power.
  - *Why D is incorrect:* There is no PoE VLAN configuration that increases a port's physical power delivery limit. Power budget is a hardware specification, not a software configuration parameter.

---

### Question 11

A network administrator uses copper twisted-pair cabling throughout a building. One run measures 110 meters. Which of the following accurately describes whether this installation will function correctly for Gigabit Ethernet?

- A) It will function correctly because the maximum distance for 1000BASE-T is 150 meters.
- B) It will not function correctly because 1000BASE-T has a maximum run of 100 meters including patch cables.
- C) It will function correctly only if Cat5 cable is used instead of Cat5e or Cat6.
- D) Distance does not affect copper Ethernet performance; only fiber optic cables have distance limits.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The IEEE 802.3 standard specifies 100 meters (328 feet) as the maximum for copper-based Ethernet (including 1000BASE-T), not 150 meters. Exceeding this limit causes signal degradation.
- *Why B is correct:* The 100-meter limit includes the total channel length: horizontal cable run plus patch cables at both ends. A 110-meter run exceeds this limit and will result in errors or failed connectivity for 1000BASE-T.
- *Why C is incorrect:* Cat5 cable is not recommended for Gigabit Ethernet. Cat5e (or Cat6) is the minimum recommended cabling standard for 1000BASE-T — Cat5 alone is insufficient, not superior.
- *Why D is incorrect:* Copper Ethernet absolutely has distance limitations (attenuation, crosstalk, and signal integrity degrade over long runs). The 100-meter limit is an IEEE fundamental specification, not a suggestion.

---

### Question 12

Which of the following cable types is most resistant to electromagnetic interference (EMI) and is the best choice for cable runs that must pass near industrial motors or fluorescent lighting?

- A) UTP Cat6
- B) STP Cat6A
- C) Coaxial RG-6
- D) Single-mode fiber optic

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* UTP (Unshielded Twisted Pair) has no metallic shielding and is the most susceptible to EMI of the options listed. It should not be used near high-interference sources.
- *Why B is incorrect:* STP (Shielded Twisted Pair) provides better EMI resistance than UTP, but the metallic shielding still conducts — it is better than UTP in high-EMI environments but not as immune as fiber.
- *Why C is incorrect:* Coaxial cable offers some EMI resistance due to its shielded construction, but it is not commonly used in modern Ethernet LANs and still carries an electrical signal that can be affected by extreme EMI.
- *Why D is correct:* Fiber optic cable transmits light, not electrical signals. It is completely immune to electromagnetic interference regardless of the proximity to motors, transformers, or fluorescent lighting. This makes it the definitive choice for high-EMI environments.

---

### Question 13

A network administrator connects two Cisco switches together using a single gigabit Ethernet cable to carry traffic for 10 VLANs simultaneously. Which port configuration must be applied to the switch ports on each end of this cable?

- A) Access port configured in the native VLAN
- B) Trunk port using 802.1Q encapsulation
- C) PortFast-enabled access port with BPDU guard
- D) PoE-enabled uplink port with 802.3at

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* An access port carries traffic for only one VLAN. It cannot carry multiple VLANs simultaneously.
- *Why B is correct:* A trunk port using 802.1Q encapsulation tags each frame with a VLAN ID, allowing a single physical link to carry traffic for multiple VLANs simultaneously between two switches. Trunk ports are the standard inter-switch link configuration.
- *Why C is incorrect:* PortFast is designed for access ports connecting to end devices (PCs, printers) — enabling it on an inter-switch link can cause Spanning Tree issues. Access ports only carry one VLAN.
- *Why D is incorrect:* PoE is a power delivery mechanism for powered devices such as APs and IP phones. It is unrelated to VLAN trunking.

---

### Question 14

What is the function of the Spanning Tree Protocol (STP) in a switched network?

- A) STP assigns VLAN IDs to switch ports to separate broadcast domains.
- B) STP prevents Layer 2 switching loops by placing redundant switch ports into a blocking state.
- C) STP encrypts inter-switch traffic to prevent VLAN hopping attacks.
- D) STP balances traffic load across multiple equal-cost paths simultaneously.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* VLAN assignment is performed by VLAN configuration (switchport access vlan) — it is not a function of STP.
- *Why B is correct:* STP (IEEE 802.1D) prevents Layer 2 broadcast storms and switching loops by electing a root bridge and then placing all redundant ports into a blocking state, keeping only one active forwarding path between any two switches.
- *Why C is incorrect:* STP has no encryption capability. VLAN hopping prevention is addressed by VLAN access control and port security.
- *Why D is incorrect:* STP blocks redundant paths — it does not load-balance across them. EtherChannel (LACP/PAgP) aggregates links for load sharing while STP treats the bundle as a single logical link.

---

### Question 15

An administrator runs `show mac address-table` on a Cisco switch. The table shows no entry for a destination MAC address. What action does the switch take when forwarding a frame to that unknown destination?

- A) The switch drops the frame and sends an ICMP error to the source.
- B) The switch forwards the frame only to the port that has the best metric route to the destination.
- C) The switch floods the frame out all active ports in the same VLAN except the port the frame arrived on.
- D) The switch discards the frame until the destination device initiates contact first.

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Switches operate at Layer 2 and do not generate ICMP error messages (that is a Layer 3 function). Unknown MAC addresses trigger flooding, not drops.
- *Why B is incorrect:* Forwarding decisions based on routing metrics are a Layer 3 router function. A Layer 2 switch does not use routing metrics — it uses the MAC address table.
- *Why C is correct:* When a switch receives a frame with an unknown destination MAC address (no entry in the MAC address table), it floods (forwards) the frame out all active ports in the same VLAN except the ingress port. This is called unknown unicast flooding.
- *Why D is incorrect:* Switches do not queue frames waiting for a device to initiate contact. Unknown unicast flooding occurs immediately upon receiving the frame.

---

### Question 16

Which fiber optic cable type supports the longest transmission distances and is designed for use between buildings or in core network backbones?

- A) Multimode OM3
- B) Multimode OM4
- C) Single-mode OS2
- D) Multimode OM1

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* OM3 multimode fiber supports 10GbE up to 300 meters — suitable for data center inter-rack runs but not long-distance backbone links between buildings.
- *Why B is incorrect:* OM4 multimode fiber supports 10GbE up to 550 meters — improved over OM3 but still limited to campus or data center distances, not metropolitan or WAN distances.
- *Why C is correct:* Single-mode OS2 fiber uses a smaller 9-micron core that allows light to travel in a single path with minimal dispersion. It supports distances of 10 km to 100+ km, making it the standard choice for inter-building, campus backbone, and WAN fiber runs.
- *Why D is incorrect:* OM1 is the oldest and lowest-performing multimode fiber, supporting only 10GbE up to 33 meters. It is effectively obsolete for new installations.

---

### Question 17

A network administrator needs to connect a switch's SFP port to a copper Cat6 cable rather than a fiber cable. Which device is needed to accomplish this?

- A) A crossover cable adapter
- B) A media converter or copper SFP transceiver
- C) A GBIC transceiver with a fiber pigtail
- D) An inline PoE injector

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A crossover cable only changes the wiring pinout — it cannot convert between optical and electrical signal types.
- *Why B is correct:* A media converter translates between fiber and copper signals, allowing an SFP-equipped switch to connect to a copper Cat6 run. Alternatively, a copper SFP transceiver (RJ45 SFP) can be inserted directly into the SFP slot to provide a copper port.
- *Why C is incorrect:* A GBIC (Gigabit Interface Converter) is an older, larger transceiver form factor that predates SFP. A GBIC with a fiber pigtail would still require fiber, not copper connectivity.
- *Why D is incorrect:* A PoE injector adds Power over Ethernet to a non-PoE switch port — it does not convert signal types between fiber and copper.

---

### Question 18

Which of the following best describes the difference between a collision domain and a broadcast domain in a switched network?

- A) A collision domain is defined by a router; a broadcast domain is defined by a switch.
- B) Each switch port is its own collision domain; a broadcast domain is bounded by a router or VLAN boundary.
- C) Collision domains and broadcast domains are identical in modern switched networks.
- D) A hub breaks up collision domains; a switch breaks up broadcast domains.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Routers define broadcast domain boundaries, and switches define collision domain boundaries — this answer has the devices reversed.
- *Why B is correct:* In a modern switched network, each full-duplex switch port is its own collision domain (collisions cannot occur on full-duplex links, so this is theoretical but correct). Broadcast domains are bounded by routers or VLAN boundaries — all ports in the same VLAN share a broadcast domain.
- *Why C is incorrect:* Switches eliminate collisions (per-port collision domains) but do not break broadcast domains without VLAN configuration or routing. They are not identical.
- *Why D is incorrect:* This is backwards. A hub creates one large collision domain for all connected devices. A switch separates collision domains per port. Routers (not switches by default) break broadcast domains.

---

### Question 19

What is the purpose of a rollover (console) cable when working with Cisco network devices?

- A) To connect two switches together for inter-VLAN routing
- B) To connect a PC's serial or USB port to the console port of a router or switch for out-of-band management
- C) To extend Ethernet distances beyond 100 meters using signal regeneration
- D) To connect an older hub to a modern Gigabit switch using crossover wiring

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Inter-switch connections use straight-through or crossover Ethernet cables (or fiber). A rollover cable is not used for data network connections.
- *Why B is correct:* A rollover cable (also called a Cisco console cable) has reversed wiring — pin 1 on one end connects to pin 8 on the other. It connects a PC's COM port (or USB-to-serial adapter) to the console port on a Cisco router or switch for out-of-band management access via terminal emulation software.
- *Why C is incorrect:* Extending Ethernet beyond 100 meters requires a repeater, switch, or fiber optic cable — not a console cable.
- *Why D is incorrect:* Connecting hubs to switches uses standard Ethernet cables. Rollover cables have a completely different wiring standard and purpose.

---

### Question 20

A Cat6A cable specification advertises a bandwidth of 500 MHz. What does this specification indicate about the cable's performance?

- A) The cable can carry 500 Mbps of data throughput.
- B) The cable supports signal frequencies up to 500 MHz, enabling 10-Gigabit Ethernet at full 100-meter distances.
- C) The cable must be terminated with 500-ohm impedance connectors.
- D) The cable operates at 500 MHz radio frequency and requires wireless antennas.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* MHz is a unit of frequency (bandwidth of the cable's signal channel), not data throughput in megabits per second. 500 MHz bandwidth supports data rates far exceeding 500 Mbps.
- *Why B is correct:* Cat6A is specified for 500 MHz bandwidth, which provides sufficient headroom to support 10GBASE-T (10-Gigabit Ethernet) at the full 100-meter maximum distance. Cat6 is specified for 250 MHz and can only support 10GbE at distances up to 55 meters.
- *Why C is incorrect:* Ethernet cabling uses 100-ohm impedance connectors. The 500 MHz figure refers to signal frequency bandwidth, not impedance.
- *Why D is incorrect:* Cat6A is a copper twisted-pair cable, not a wireless medium. MHz in the context of cabling refers to electrical signal frequency, not radio frequency.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
