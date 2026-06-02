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
