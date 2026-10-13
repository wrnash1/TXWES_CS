# Quiz: Module 12 - Network Infrastructure Devices

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.2
**Texas Wesleyan University | Professor Nash**
**Total Questions: 10 | Points: 10 (1 point each)**

---

## Questions

### Question 1

Which device directs traffic between different IP subnetworks based on Layer 3 logical addresses?

- A) Switch
- B) Hub
- C) Router
- D) Access Point

Correct Answer: C

- Why C is correct: A router operates at OSI Layer 3 (Network layer) and makes forwarding decisions based on IP addresses in packet headers. It maintains a routing table and directs packets between separate networks or subnets — for example, between the internal LAN and the internet.
- Why A is incorrect: A switch operates at Layer 2 (Data Link) and forwards frames using MAC addresses within a single LAN segment. A switch does not route between different IP networks.
- Why B is incorrect: A hub operates at Layer 1 (Physical) and simply repeats electrical signals to all connected ports. It has no awareness of MAC addresses or IP addresses.
- Why D is incorrect: A wireless access point (WAP) operates at Layer 2 as a bridge between wireless clients and the wired network. It does not route packets between different IP networks.

---

### Question 2

Which of the following most accurately describes the difference between a switch and a router?

- A) A switch operates at OSI Layer 2, forwarding Ethernet frames between devices on the same local network using MAC address tables; a router operates at OSI Layer 3, forwarding packets between different IP networks or subnets using routing tables.
- B) A switch assigns IP addresses to clients on the local network using DHCP, while a router filters traffic based on MAC address allow/block lists to enforce access control policies.
- C) A switch connects a local network to the internet by translating private IP addresses to the public IP address assigned by the ISP, while a router distributes the signal to wireless clients.
- D) A switch and a router perform identical functions at Layer 2; the distinction is purely physical — switches have more ports and routers have fewer ports with higher throughput per port.

Correct Answer: A

- Why A is correct: This accurately describes the OSI layer and primary function of each device as tested on the CompTIA A+ exam. The Layer 2 MAC-based forwarding of the switch versus the Layer 3 IP-based routing of the router is the core tested distinction.
- Why B is incorrect: DHCP is typically served by a router or a dedicated server, not a switch. Switches forward frames based on MAC addresses and do not assign IP addresses. MAC address filtering is a security feature unrelated to the router's primary routing function.
- Why C is incorrect: NAT (Network Address Translation) is a router function, not a switch function. Wireless signal distribution is performed by a WAP — a separate device from the router, even when combined in a home gateway.
- Why D is incorrect: Switches and routers perform fundamentally different functions at different OSI layers. The distinction is not physical port count — it is the layer of the OSI model at which each device makes forwarding decisions.

---

### Question 3

A company wants to mount wireless access points throughout a three-story office building and needs all WAPs to be powered without running separate electrical outlet cables to each ceiling location. Which technology enables this?

- A) USB Power Delivery — WAPs connect to nearby computers via USB-C cables that deliver up to 100 W for both data and power
- B) Power over Ethernet (PoE) — the PoE-capable switch delivers DC power over the same Ethernet cable used for network data, eliminating a separate power supply at each WAP
- C) Wireless charging pads installed in ceiling tiles that inductively charge WAPs through the mounting surface
- D) Solar panels integrated into the WAP housing that generate enough power from office lighting to run the device continuously

Correct Answer: B

- Why B is correct: PoE (IEEE 802.3af/at/bt) is the standard enterprise solution for powering WAPs, IP cameras, and VoIP phones via the Ethernet cable already running to each device. It requires a PoE-capable switch or PoE injector and eliminates the need for a local electrical outlet at each device location.
- Why A is incorrect: WAPs connect to the network via Ethernet, not USB. USB Power Delivery is a consumer charging standard and is not used to power network infrastructure devices in enterprise deployments.
- Why C is incorrect: Inductive wireless charging requires very close proximity — millimeters — between charger and device and cannot deliver usable power through ceiling materials over any practical gap. This technology does not exist for network infrastructure deployment.
- Why D is incorrect: Office lighting does not provide sufficient energy for photovoltaic generation to continuously power a WAP. Enterprise WAP power requirements of 12–25 W far exceed what any integrated solar panel could supply from indoor lighting.

---

### Question 4

A technician is organizing a network rack in a server room. Long horizontal cable runs from wall jacks throughout the building terminate in the rack, and short cables connect rack equipment to a switch. Which device provides the organized termination point for the horizontal runs and allows flexible patching to different switch ports without disturbing the permanent cable runs?

- A) A PoE injector — it combines power and data signals from the permanent cable runs before they reach the switch
- B) A patch panel — it provides fixed termination points for horizontal cable runs and allows short patch cables to connect any wall jack to any switch port
- C) A managed switch — it stores the MAC addresses of all devices connected to the permanent cable runs in its forwarding table, replacing the need for any intermediate termination hardware
- D) A firewall — it inspects all traffic from the permanent cable runs and acts as the demarcation point between the building wiring and the switch fabric

Correct Answer: B

- Why B is correct: A patch panel is a passive termination and organization device. Permanent cable runs punch down into the back of the patch panel, and short patch cables on the front connect specific wall jack ports to specific switch ports, enabling flexible port assignment without touching the permanent in-wall wiring.
- Why A is incorrect: A PoE injector adds power to an Ethernet cable for a single device. It is not a multi-port termination or cable management device and does not serve the organizational role of a patch panel.
- Why C is incorrect: A switch is an active Layer 2 forwarding device. While it does build MAC address tables, it does not replace the cable management and termination function of a patch panel in a structured cabling installation.
- Why D is incorrect: A firewall is a security device that filters traffic by policy rules. It is not placed between horizontal cable runs and a switch, and it does not serve as a physical cable termination point.

---

### Question 5

A small office has a single internet connection from the ISP delivered as a coaxial cable. The office needs multiple wired workstations and wireless laptops to share the connection. Which combination of devices provides internet access to all clients?

- A) A cable modem connected to the coaxial line, then a wireless router connected to the modem — the modem converts the ISP signal to Ethernet, and the router provides DHCP, NAT, switching, and wireless access for all clients
- B) A patch panel connected to the coaxial line, then a managed switch — the patch panel converts the ISP signal to Ethernet and the switch provides DHCP and wireless access to all clients
- C) A WAP connected directly to the coaxial line — modern WAPs include built-in DOCSIS modems and can connect directly to cable TV coaxial outlets without any additional devices
- D) A firewall connected to the coaxial line, then individual Ethernet cables run directly from the firewall to each workstation and laptop without any switching or routing hardware

Correct Answer: A

- Why A is correct: This is the standard home and small office internet architecture. The cable modem terminates the ISP's DOCSIS coaxial signal and presents an Ethernet WAN port. The wireless router connects to that Ethernet port and provides DHCP addressing, NAT, LAN switching, and Wi-Fi to all clients through a single combined device.
- Why B is incorrect: A patch panel is a passive cable termination device with no signal conversion capability. It cannot convert a DOCSIS coaxial signal to Ethernet, and a managed switch does not provide DHCP, NAT, or wireless access.
- Why C is incorrect: Standard WAPs do not include built-in cable modems and cannot connect directly to a coaxial ISP line. DOCSIS modem functionality is a separate hardware component.
- Why D is incorrect: A firewall alone cannot terminate a coaxial ISP connection. Without a switch the firewall would have insufficient ports to connect multiple wired workstations, and wireless clients would have no access at all.

---

### Question 6

A technician installs a VoIP phone that is rated at 6.4 watts of power draw. The phone will be connected to a switch port labeled IEEE 802.3af. Will the switch port deliver sufficient power to the phone?

- A) No — IEEE 802.3af delivers only 3.84 W maximum, which is insufficient for any VoIP phone
- B) Yes — IEEE 802.3af delivers up to 15.4 W at the port, which is more than enough for a 6.4 W VoIP phone
- C) No — IEEE 802.3af is only compatible with wireless access points; VoIP phones require IEEE 802.3at ports
- D) Yes — but only if the phone is also connected to a separate AC power adapter; IEEE 802.3af requires a backup power source to activate the PoE circuit

Correct Answer: B

- Why B is correct: IEEE 802.3af (standard PoE) delivers up to 15.4 W at the switch port, with approximately 12.95 W available at the powered device after cable losses. A 6.4 W VoIP phone is well within this budget and is exactly the type of device PoE was originally designed to power.
- Why A is incorrect: IEEE 802.3af delivers 15.4 W, not 3.84 W. The 3.84 W figure is not a PoE standard value.
- Why C is incorrect: IEEE 802.3af is compatible with any compliant powered device — including VoIP phones, IP cameras, and small WAPs. There is no device-type restriction within the standard.
- Why D is incorrect: The entire purpose of PoE is to eliminate the need for a separate AC power adapter. A PoE-powered device does not require and typically does not use an additional AC adapter when connected to a PoE port.

---

### Question 7

Which network device operates at OSI Layer 1 and sends every received signal out of all other connected ports simultaneously, causing all connected devices to share total available bandwidth?

- A) Managed switch
- B) Router
- C) Hub
- D) Wireless access point

Correct Answer: C

- Why C is correct: A hub is a Layer 1 device that repeats every electrical signal it receives to all other ports. It has no MAC address table and no traffic filtering. All devices on a hub share the same collision domain and the same total bandwidth allocation.
- Why A is incorrect: A managed switch operates at Layer 2, builds a MAC address table, and sends frames only to the specific destination port — not to all ports. Each switch port is its own collision domain.
- Why B is incorrect: A router operates at Layer 3 and makes forwarding decisions based on IP addresses. It connects different networks and does not repeat signals to all ports.
- Why D is incorrect: A WAP operates at Layer 2 as a bridge between wireless and wired segments. It does not repeat all traffic to all connected clients in the manner of a hub.

---

### Question 8

An organization deploys twelve IP cameras in a parking garage. Each camera is rated at 25 W. The network switch in the garage equipment cabinet is a standard unmanaged switch with no PoE capability. What is the most cost-effective solution that avoids running new electrical outlet circuits to each camera?

- A) Replace the unmanaged switch with a PoE+ (802.3at) managed switch that has sufficient per-port wattage and total PoE budget to power all twelve cameras
- B) Connect each camera to a PoE injector placed inline between the switch port and the camera, with the injector drawing power from the cabinet's existing electrical outlet
- C) Replace the Ethernet cable runs with fiber optic cables, which carry optical power as well as data and can supply 25 W per camera without additional hardware
- D) Install a USB hub in the cabinet and connect each camera via USB-to-Ethernet adapters, since USB 3.0 provides up to 900 mA which is sufficient for 25 W cameras

Correct Answer: A

- Why A is correct: At 25 W per camera, the required PoE standard is 802.3at (PoE+), which delivers up to 30 W per port. Replacing the non-PoE switch with a PoE+ managed switch with a total budget of at least 300 W (12 × 25 W) eliminates the need for any separate power infrastructure at the camera locations. This is the enterprise standard solution for IP camera deployments.
- Why B is correct as a secondary option but is not the best answer here: PoE injectors are a valid per-device workaround but require an individual injector for each of twelve cameras plus access to a power outlet at each injector location — significantly more complex than a single switch replacement for a 12-camera system.
- Why C is incorrect: Fiber optic cables carry light signals only. They cannot transmit electrical power. No fiber standard delivers power to attached devices.
- Why D is incorrect: USB hubs operate over USB cables, not Ethernet, and USB 3.0 at 900 mA on 5 V supplies only 4.5 W — far below the 25 W requirement. IP cameras require Ethernet connections, not USB.

---

### Question 9

A home user's wireless router stopped working. A technician replaces it with a standalone wireless access point but the connected devices cannot access the internet or receive IP addresses. What is the most likely reason?

- A) The WAP's SSID was not broadcast on channel 6, which is required for DHCP to function on 2.4 GHz networks
- B) A standalone WAP does not perform routing, NAT, or DHCP — those functions were provided by the router component of the original wireless router, and removing the router left no device to perform them
- C) Wireless access points require fiber optic uplinks to function; a standard Ethernet cable cannot carry the backhaul traffic needed for internet access through a WAP
- D) The WAP is operating at Layer 2, which is incompatible with the ISP's modem; Layer 2 devices can only communicate with other Layer 2 devices and cannot pass traffic through a Layer 3 modem

Correct Answer: B

- Why B is correct: A home "wireless router" contains three functions in one device: a router (Layer 3, DHCP, NAT, WAN connection), a switch (Layer 2 LAN forwarding), and a WAP (wireless radio access). Replacing it with only a standalone WAP removes the routing and DHCP functions. The WAP can bridge wireless clients to the wired network, but without a router there is no device to assign IP addresses or route traffic to the internet.
- Why A is incorrect: DHCP operation is independent of Wi-Fi channel selection. Channel 6 has no special DHCP requirement, and SSID broadcasting is unrelated to IP address assignment.
- Why C is incorrect: WAPs use standard Ethernet uplinks. Fiber optic backhaul is an enterprise option but is not required, and standard copper Ethernet is fully capable of carrying WAP backhaul traffic.
- Why D is incorrect: Layer 2 and Layer 3 devices communicate across the same physical infrastructure constantly. A WAP's Ethernet uplink connects to a switch (Layer 2) which connects to a router (Layer 3) which connects to a modem — this layered communication is the normal design. The layers are not incompatible.

---

### Question 10

A network administrator is designing a rack for a new branch office. The rack will contain a cable modem, a firewall, a router, a 24-port managed PoE switch, and a 24-port patch panel. Place these devices in the correct order from the ISP connection inward to the end devices, and identify which device performs DHCP for the LAN clients.

- A) ISP → cable modem → router → firewall → managed switch → patch panel → end devices. DHCP is performed by the managed switch.
- B) ISP → cable modem → firewall → router → managed switch → patch panel → end devices. DHCP is performed by the router (or a DHCP server on the LAN).
- C) ISP → patch panel → firewall → router → cable modem → managed switch → end devices. DHCP is performed by the firewall.
- D) ISP → cable modem → managed switch → router → firewall → patch panel → end devices. DHCP is performed by the patch panel's built-in DHCP server.

Correct Answer: B

- Why B is correct: The standard placement is: modem (ISP signal conversion) → firewall (perimeter security inspection) → router (Layer 3 routing, DHCP, NAT) → managed switch (Layer 2 LAN distribution) → patch panel (passive termination) → end devices. DHCP is a Layer 3 service performed by the router or a dedicated server on the LAN, not by the switch or patch panel.
- Why A is incorrect: Placing the router before the firewall puts routing and NAT processing ahead of security inspection, which means unfiltered internet traffic reaches the router directly. The firewall should inspect traffic before it reaches the internal routing layer.
- Why C is incorrect: The patch panel is passive and belongs at the distribution layer closest to end devices — not at the perimeter between the modem and firewall. The cable modem also cannot be placed after the router; the modem is always the first device from the ISP.
- Why D is incorrect: A patch panel does not have a built-in DHCP server — it is entirely passive with no electronics, no processor, and no network intelligence of any kind.

---

### Question 11

A small office uses a single consumer wireless router that combines modem, router, switch, and wireless access point functions into one device. An employee connects a second consumer wireless router to one of the LAN ports of the first router to extend coverage to the back office. Users connected to the second router can reach the internet but cannot communicate with users on the first router's LAN. What is the most likely cause?

- A) The second router's wireless radio is transmitting on the same channel as the first router, causing RF interference that blocks inter-router wired communication
- B) The second router is performing NAT and DHCP independently, creating a double-NAT configuration that places users on the second router in a separate private network unable to reach devices on the first router's subnet
- C) The LAN port on the first router that connects to the second router is administratively disabled by default for security reasons and requires a managed switch interface to re-enable it
- D) The second router's MAC address has been blocked by the first router's built-in MAC filtering, which prevents all traffic from the second router from passing to the first router's LAN

Correct Answer: B

- Why B is correct: When a second router (with its own NAT and DHCP) is connected to a LAN port of the first router, it creates a double-NAT topology. Devices behind the second router receive private IP addresses from the second router's DHCP server on a different subnet. NAT on the second router hides these addresses from the first router's LAN, making direct communication between the two subnets impossible without explicit routing configuration.
- Why A is incorrect: RF channel interference affects wireless throughput and reliability but does not block wired communication between a LAN port and a WAN/LAN connection. The symptom describes a routing or NAT issue, not a wireless interference issue.
- Why C is incorrect: Consumer routers do not administratively disable LAN ports by default. All LAN ports on a consumer router are active and switchable by default.
- Why D is incorrect: MAC filtering on consumer routers is typically applied to wireless clients only, not to wired LAN ports. MAC filtering also only blocks specific addresses if explicitly configured — it is not active by default.

---

### Question 12

A network administrator configures a managed switch with VLAN 10 for the finance department and VLAN 20 for the general staff. Finance workstations can communicate with each other, and general staff workstations can communicate with each other, but no communication is possible between VLANs. What device and configuration would allow inter-VLAN communication?

- A) A second managed switch configured as a VLAN bridge — connecting the two switches with an access port on each allows VLANs to communicate across the link
- B) A router (or Layer 3 switch) with sub-interfaces or SVIs configured for each VLAN — the router performs inter-VLAN routing by routing packets between the two VLAN subnets at Layer 3
- C) A wireless access point configured in bridge mode — placing the AP between the two VLAN segments allows it to forward frames between VLANs using its built-in Layer 2 bridging
- D) Enabling VLAN trunking on all access ports — trunking on access ports automatically enables inter-VLAN routing within the switch without requiring an external router

Correct Answer: B

- Why B is correct: VLANs are separate Layer 2 broadcast domains. Communication between VLANs requires a Layer 3 routing decision. A router with sub-interfaces on a trunk port (router-on-a-stick configuration) or a Layer 3 switch with Switched Virtual Interfaces (SVIs) routes packets between the VLAN subnets, enabling inter-VLAN communication.
- Why A is incorrect: A trunk link between two managed switches allows both VLANs to traverse the inter-switch link but does not route between them. Each VLAN remains an isolated broadcast domain across both switches. Connecting switches does not enable inter-VLAN communication.
- Why C is incorrect: A wireless access point in bridge mode forwards Layer 2 frames between wireless and wired segments. It does not perform Layer 3 routing and cannot route between VLANs. Access points have no VLAN routing capability.
- Why D is incorrect: Trunk ports carry multiple VLANs on a single link between switches and routers — they do not enable routing between VLANs. Routing between VLANs requires a Layer 3 device regardless of trunk port configuration.

---

### Question 13

A technician configures a SOHO router for a home office. The external IP address assigned by the ISP is 203.0.113.47. Internal devices receive addresses in the 192.168.1.0/24 range. A user on the internet cannot connect directly to the user's home PC using the 192.168.1.x address. What technology makes internal private addresses inaccessible from the internet, and what configuration would allow an inbound connection?

- A) The private addresses are blocked by the ISP's router, which filters RFC 1918 address space at the network edge. Adding a static route on the ISP's router would allow inbound connections.
- B) Network Address Translation (NAT) on the SOHO router maps the single public IP to multiple private IPs for outbound traffic. Inbound connections require a port forwarding rule that maps a specific external port to the target internal device's IP and port.
- C) The SOHO router's built-in firewall inspects every packet for malware signatures and blocks all inbound connections by default. Disabling the firewall entirely allows inbound connections.
- D) Private IP addresses use a different routing protocol (RIPv2) that is incompatible with the internet's BGP routing. Reconfiguring the SOHO router to use BGP enables inbound connections from the internet.

Correct Answer: B

- Why B is correct: NAT (Network Address Translation) allows multiple devices with RFC 1918 private addresses to share a single public IP for outbound internet communication. The router rewrites source addresses on outbound packets and tracks connections in a translation table. For inbound connections to reach a specific internal device, a port forwarding rule must be configured — mapping an external port on the public IP to the internal device's private IP and port.
- Why A is incorrect: ISPs do filter RFC 1918 address space from internet routing tables, but this is a separate issue. The 192.168.1.x addresses are inaccessible from the internet because NAT on the SOHO router hides them — not because the ISP's router has a static route issue. Adding a static route on the ISP's router would not resolve the NAT translation problem.
- Why C is incorrect: While SOHO router firewalls do block unsolicited inbound connections, the primary mechanism preventing direct access to 192.168.1.x addresses from the internet is NAT, not firewall signature inspection. Disabling the firewall entirely would be a security risk and is not the correct targeted solution.
- Why D is incorrect: NAT is the correct explanation, not routing protocol compatibility. RFC 1918 private addresses are deliberately non-routable on the public internet; this is enforced by BGP filtering at ISP border routers, but the mechanism preventing inbound connections to a home PC is the NAT translation table on the SOHO router, not a routing protocol mismatch.

---

### Question 14

A network administrator needs to provide wireless coverage in a large warehouse with metal shelving. A single wireless router at the office end of the warehouse provides no signal in the far half of the building. Which solution is most appropriate?

- A) Replace the wireless router with a higher-power consumer router — increasing transmit power will overcome the RF attenuation from metal shelving regardless of distance
- B) Deploy wireless access points at multiple locations throughout the warehouse, connected to the wired network via Ethernet, and configure them with the same SSID and overlapping channels to ensure seamless roaming
- C) Install a wired Ethernet hub at the center of the warehouse and connect a second wireless router to it — the second router will automatically extend the first router's signal using wireless mesh protocol
- D) Configure the existing router to use the 2.4 GHz band exclusively, as 2.4 GHz penetrates metal shelving without any signal degradation

Correct Answer: B

- Why B is correct: For large or obstructed spaces, deploying multiple access points connected to the wired network (a controller-based or standalone WAP deployment) is the correct enterprise solution. Same SSID with proper channel planning allows clients to roam between APs. This approach provides reliable coverage without the double-NAT and signal degradation issues of consumer wireless extenders.
- Why A is incorrect: Increasing transmit power helps marginally with distance but does not overcome the reflection and absorption caused by metal shelving. Metal is a significant RF obstacle that requires physical placement of additional APs, not just power increases.
- Why C is incorrect: An Ethernet hub at the center of the warehouse would work for wired connectivity, but consumer routers do not automatically extend a first router's signal using wireless mesh protocol — they would create a double-NAT configuration as described in Question 11. A second consumer router connected to an unmanaged hub is not a wireless mesh solution.
- Why D is incorrect: While 2.4 GHz does penetrate solid obstacles better than 5 GHz due to its longer wavelength, it still suffers significant attenuation through metal shelving. Metal reflects RF energy rather than allowing it to pass through, and this effect applies to both 2.4 GHz and 5 GHz bands.

---

### Question 15

A technician is configuring a new managed switch and needs to ensure that a specific PC connected to port 3 always receives the same IP address from the DHCP server. The DHCP server is a separate device on the network. Which configuration should the technician apply?

- A) Configure a static IP address directly on the PC's network adapter settings and ensure it is outside the DHCP pool range — this eliminates the need for any switch or DHCP server configuration
- B) Configure a DHCP reservation on the DHCP server that maps the PC's MAC address to a specific IP address — the server will always assign this IP to the device with that MAC address
- C) Configure the switch port 3 as a DHCP static port in the switch's management interface — the switch will intercept the DHCP request and inject the configured IP address into the response
- D) Configure a VLAN on port 3 with the desired IP address as the VLAN's gateway IP — the PC will always receive this IP address as its DHCP-assigned address from the VLAN gateway

Correct Answer: B

- Why B is correct: A DHCP reservation (also called a DHCP static mapping or address reservation) is configured on the DHCP server and ties a specific IP address to a specific MAC address. When the device with that MAC address sends a DHCP request, the server always responds with the reserved IP. This is the standard method for ensuring consistent IP assignment without manually configuring static IPs on the client.
- Why A is incorrect: Configuring a static IP directly on the PC is a valid alternative but it bypasses DHCP entirely. The question asks about a DHCP-based solution. Additionally, static IPs require manual management on each device and are more difficult to track in large environments.
- Why C is incorrect: Managed switches do not have a "DHCP static port" configuration feature that injects IP addresses into DHCP responses. Switches do have DHCP snooping (which filters malicious DHCP responses) but this is a security feature, not an IP assignment mechanism.
- Why D is incorrect: VLAN gateway IPs are default gateway addresses for routing, not DHCP assignment mechanisms. A VLAN's gateway IP is the router interface address that clients use to reach other networks — it is not related to what IP address a DHCP server assigns to a client on that VLAN.

---

### Question 16

A company's network has a hub connecting four workstations. One workstation is infected with malware that sends continuous broadcast packets. Which of the following accurately describes the impact on the other three workstations?

- A) The other three workstations are unaffected because a hub's MAC address table identifies the infected workstation and blocks its traffic from being forwarded to the other ports
- B) All four workstations experience degraded performance because a hub repeats every received signal to all ports — every broadcast packet from the infected workstation is transmitted to all other connected workstations simultaneously
- C) Only the workstation directly adjacent to the infected machine is affected, because hubs use a linear bus topology that forwards signals in only one direction
- D) The hub isolates the infected workstation automatically using its built-in port security feature after detecting abnormal broadcast traffic

Correct Answer: B

- Why B is correct: A hub is a Layer 1 device that electrically repeats every signal received on any port to all other ports — it has no MAC address table, no filtering, and no intelligence. Every packet transmitted by the infected workstation, including broadcast floods, is repeated to all three other workstations. The shared collision domain means all workstations compete for the same bandwidth and all receive every packet.
- Why A is incorrect: Hubs have no MAC address table. MAC address learning and selective frame forwarding are Layer 2 switch features. A hub cannot identify source addresses or block traffic from specific ports.
- Why C is incorrect: Modern Ethernet hubs use a star physical topology — all devices connect to a central hub. Signals are repeated to all ports simultaneously, not in one direction around a linear bus.
- Why D is incorrect: Hubs have no processing capability, firmware, or port security features. Auto-isolation of misbehaving ports is a feature found on managed switches (port security, dynamic ARP inspection, DHCP snooping), not on passive hub hardware.

---

### Question 17

A technician sets up a wireless network in a small office using a single 802.11ac (Wi-Fi 5) access point. Users report acceptable performance near the AP but unusable speeds in a conference room 25 meters away with two concrete walls between the AP and the room. Which of the following is the most technically accurate explanation?

- A) 802.11ac operates exclusively on the 5 GHz band, which has shorter wavelengths that attenuate more rapidly through solid barriers than 2.4 GHz signals — the concrete walls are absorbing and reflecting most of the RF energy before it reaches the conference room
- B) 802.11ac has a maximum range of exactly 15 meters indoors regardless of obstacles, so the 25-meter distance alone is the sole cause of the signal failure
- C) The conference room is in a signal shadow created by the access point's directional antenna, which only transmits RF energy in a single beam toward the nearest wall
- D) The 5 GHz channel width of 802.11ac is too narrow to carry enough signal energy through concrete, and switching to a 20 MHz channel width would resolve the attenuation issue

Correct Answer: A

- Why A is correct: 802.11ac operates only on the 5 GHz band. Higher-frequency signals (5 GHz) have shorter wavelengths that are more susceptible to absorption and reflection by dense materials such as concrete compared to 2.4 GHz signals. Each concrete wall causes significant RF attenuation. Two concrete walls at 25 meters on 5 GHz is a common scenario that produces near-zero usable signal.
- Why B is incorrect: 802.11ac does not have a hard 15-meter indoor range limit. Indoor range varies significantly based on obstacles, antenna gain, transmit power, and interference. In open spaces, 5 GHz 802.11ac can reach 30-50 meters or more.
- Why C is incorrect: Consumer and enterprise access points use omnidirectional antennas that radiate RF energy in all directions horizontally (and to some extent vertically). They do not transmit in a single directional beam that would create a signal shadow behind the AP.
- Why D is incorrect: Channel width (20/40/80/160 MHz) affects the amount of spectrum used and the theoretical maximum throughput — it does not affect RF penetration through walls. Narrowing channel width reduces capacity but does not meaningfully improve signal range through solid obstacles.

---

### Question 18

A technician is reviewing a packet capture from a network where a rogue device is sending ARP replies claiming that the gateway's IP address (192.168.1.1) maps to the rogue device's MAC address. What type of attack is this, and which managed switch feature can prevent it?

- A) This is a DNS poisoning attack; the switch feature that prevents it is DHCP snooping, which validates DNS query responses against the switch's trusted port list
- B) This is an ARP poisoning (ARP spoofing) attack; the switch feature that prevents it is Dynamic ARP Inspection (DAI), which validates ARP packets against a trusted DHCP snooping binding table and drops ARP replies that contain incorrect MAC-to-IP mappings
- C) This is a MAC flooding attack; the switch feature that prevents it is port security, which limits the number of MAC addresses that can be learned on a single port
- D) This is a VLAN hopping attack; the switch feature that prevents it is disabling DTP (Dynamic Trunking Protocol) on all access ports so that rogue devices cannot negotiate trunk links

Correct Answer: B

- Why B is correct: ARP poisoning (also called ARP spoofing) involves sending unsolicited ARP replies that associate the attacker's MAC address with a legitimate IP (such as the default gateway), causing traffic intended for the gateway to be sent to the attacker instead. Dynamic ARP Inspection (DAI) on managed switches validates ARP packets against the DHCP snooping binding table (which maps trusted IP-to-MAC associations) and drops ARP replies containing spoofed mappings.
- Why A is incorrect: DNS poisoning involves injecting false DNS responses to redirect domain name lookups to incorrect IP addresses. ARP operates at Layer 2 with no involvement from DNS. DHCP snooping validates DHCP server responses, not DNS query responses.
- Why C is incorrect: MAC flooding involves sending a large number of frames with random source MAC addresses to exhaust the switch's MAC address table, causing the switch to flood traffic to all ports. Port security limits MAC addresses per port to prevent this. This is a different attack from the scenario described, which involves crafted ARP replies rather than MAC address exhaustion.
- Why D is incorrect: VLAN hopping involves an attacker using double-tagging or DTP negotiation to send traffic into a VLAN other than their access VLAN. Disabling DTP prevents rogue trunk negotiation. This is a different attack from ARP poisoning.

---

### Question 19

A company purchases an 8-port unmanaged switch and a 24-port managed switch for a small office. Which statement correctly identifies a capability that the managed switch has and the unmanaged switch does not?

- A) The managed switch can forward Ethernet frames using MAC addresses, while the unmanaged switch can only broadcast all incoming frames to every port simultaneously
- B) The managed switch supports VLAN configuration, port mirroring, SNMP monitoring, QoS, and port security — features that require software configuration through a management interface not present on unmanaged switches
- C) The managed switch operates at Layer 3 (Network layer) and can route between IP subnets, while the unmanaged switch operates at Layer 1 and repeats signals to all ports
- D) The managed switch uses faster Cat7 cables due to its higher processing power, while the unmanaged switch is limited to Cat5e or Cat6 cable

Correct Answer: B

- Why B is correct: Managed switches provide a configuration interface (web GUI, CLI, or SNMP) that allows administrators to configure VLANs, QoS priority queuing, port mirroring for monitoring, SNMP traps for network management systems, and port security features. None of these features are available on unmanaged switches, which operate with fixed factory settings and no configuration interface.
- Why A is incorrect: Both managed and unmanaged switches are Layer 2 devices that forward frames based on MAC addresses learned through the MAC address learning process. An unmanaged switch is not a hub — it does not broadcast all frames to all ports. Both switch types perform selective forwarding based on MAC addresses.
- Why C is incorrect: Unmanaged switches are Layer 2 devices, not Layer 1 devices. Layer 1 devices are hubs and repeaters. Basic Layer 3 routing capability is found on Layer 3 switches, which are a subset of managed switches — not all managed switches route at Layer 3.
- Why D is incorrect: Cable category selection (Cat5e, Cat6, Cat6a, Cat7) depends on the network speed requirements and installation standards — not on whether the switch is managed or unmanaged. Both managed and unmanaged switches connect via standard Ethernet cables regardless of the switch's feature set.

---

### Question 20

A technician installs a cable modem provided by the ISP and connects it directly to a PC with no router in between. The PC receives a public IP address (67.45.22.198) and can browse the internet normally. The company then adds three more PCs. Which device must be added to allow all four PCs to share the single public IP address, and what technology on that device enables sharing?

- A) A network hub — hubs split the available bandwidth equally across all connected ports, allowing four PCs to each use one-quarter of the available bandwidth on the single public IP
- B) A router with NAT (Network Address Translation) — NAT allows the router to assign private IP addresses to all four PCs and translate their private addresses to the single public IP for all outbound internet connections
- C) A managed switch with DHCP enabled — the managed switch assigns private IP addresses to all four PCs and uses VLAN tagging to multiplex their traffic onto the single public IP
- D) A second cable modem — connecting two modems doubles the available public IP addresses, providing one public IP per two PCs

Correct Answer: B

- Why B is correct: NAT (Network Address Translation) on a router allows multiple devices with private RFC 1918 IP addresses to share a single public IP address. The router maintains a NAT translation table that tracks each device's outbound connections by private IP and source port, and rewrites packet headers so all outbound traffic appears to originate from the single public IP. This is the fundamental technology used in nearly every home and small office internet connection.
- Why A is incorrect: A hub is a Layer 1 repeater that has no IP awareness, no DHCP capability, and no NAT function. Connecting four PCs to a hub and a modem would result in all four PCs competing for the single public IP assignment through DHCP — at most one PC would receive the IP address, and the others would get no connectivity.
- Why C is incorrect: A managed switch is a Layer 2 device. While some managed switches include a DHCP server feature, they do not perform NAT. Without NAT, four PCs with private addresses cannot share a single public IP. VLAN tagging is a traffic segmentation mechanism, not a NAT replacement.
- Why D is incorrect: A second cable modem would require a second ISP subscriber account and would provide a second public IP address — it would not allow the original single public IP to serve all four PCs. ISPs assign one IP per modem connection unless a business account with a static IP block is purchased.
