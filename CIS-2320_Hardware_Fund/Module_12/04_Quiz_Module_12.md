# Quiz: Module 12 - Network Infrastructure Devices
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which device directs traffic between different IP subnetworks based on Layer 3 logical addresses?
*   A) Switch
*   B) Hub
*   C) Router
*   D) Access Point
*   **Correct Answer:** C) Routers operate at Layer 3 of the OSI model and route packets between different networks.
*   **Distractor Analysis:**
    *   *Why correct:* Routers operate at Layer 3 of the OSI model and route packets between different networks.
    *   Switches operate at Layer 2 using MAC addresses. Hubs repeat traffic to all ports.

---

**Question 2**
In the context of PC networking, which of the following most accurately describes **switches vs routers**?
*   A) A switch operates at OSI Layer 2, forwarding Ethernet frames between devices on the same local network using MAC address tables; a router operates at OSI Layer 3, forwarding packets between different IP networks or subnets using routing tables.
*   B) A switch assigns IP addresses to clients on the local network using DHCP, while a router filters traffic based on MAC address allow/block lists to enforce access control policies.
*   C) A switch connects a local network to the internet by translating private IP addresses to the public IP address assigned by the ISP, while a router distributes the signal to wireless clients.
*   D) A switch and a router perform identical functions at Layer 2; the distinction is purely physical — switches have more ports and routers have fewer ports with higher throughput per port.
*   **Correct Answer:** A) A switch operates at OSI Layer 2, forwarding Ethernet frames between devices on the same local network using MAC address tables; a router operates at OSI Layer 3, forwarding packets between different IP networks or subnets using routing tables.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the OSI layer and primary function of each device as tested on the CompTIA A+ exam — the Layer 2 MAC/Layer 3 IP distinction is the core tested concept.
    * *Why B is incorrect:* DHCP is typically served by a router or dedicated server, not a switch; switches forward frames and do not assign IP addresses. MAC address filtering is a wireless security feature, not the primary function of a router.
    * *Why C is incorrect:* NAT (Network Address Translation) is a router function, not a switch function; wireless signal distribution is performed by a WAP, which is a separate device from a router even when combined in a home gateway.
    * *Why D is incorrect:* Switches and routers perform fundamentally different functions at different OSI layers; the distinction is not merely physical port count.


---

**Question 3**
A company wants to mount wireless access points throughout a three-story office building and needs all WAPs to be powered without running separate electrical outlet cables to each location. Which technology enables this?
*   A) USB Power Delivery — WAPs connect to nearby computers via USB-C cables that deliver up to 100W for both data and power
*   B) Power over Ethernet (PoE) — the PoE-capable switch delivers DC power over the same Ethernet cable used for network data, eliminating a separate power supply at each WAP
*   C) Wireless charging pads installed in ceiling tiles that inductively charge WAPs through the mounting surface
*   D) Solar panels integrated into the WAP housing that generate enough power from office lighting to run the device continuously
*   **Correct Answer:** B) Power over Ethernet (PoE) — the PoE-capable switch delivers DC power over the same Ethernet cable used for network data, eliminating a separate power supply at each WAP
*   **Distractor Analysis:**
    * *Why B is correct:* PoE (IEEE 802.3af/at/bt) is the standard enterprise solution for powering WAPs, IP cameras, and VoIP phones via the Ethernet cable already running to each device; it requires a PoE-capable switch or PoE injector and eliminates the need for a local electrical outlet at each device location.
    * *Why A is incorrect:* WAPs connect to the network via Ethernet, not USB; USB Power Delivery is a consumer charging standard and is not used to power network infrastructure devices in enterprise deployments.
    * *Why C is incorrect:* Inductive wireless charging requires very close proximity (millimeters) between charger and device and cannot deliver power through ceiling materials over practical distances; this technology does not exist for network infrastructure deployment.
    * *Why D is incorrect:* Office lighting does not provide sufficient energy for photovoltaic generation to power a WAP continuously; enterprise WAP power requirements (typically 12–25W) far exceed what integrated solar could supply from indoor lighting.


---

**Question 4**
A technician is organizing a network rack in a server room. Long horizontal cable runs from wall jacks throughout the building terminate in the rack, and short cables connect rack equipment to a switch. Which device provides the organized termination point for the horizontal runs and allows flexible patching to different switch ports without disturbing the permanent cable runs?
*   A) A PoE injector — it combines power and data signals from the permanent cable runs before they reach the switch
*   B) A patch panel — it provides fixed termination points for horizontal cable runs and allows short patch cables to connect any wall jack to any switch port
*   C) A managed switch — it stores the MAC addresses of all devices connected to the permanent cable runs in its forwarding table, replacing the need for any intermediate termination hardware
*   D) A firewall — it inspects all traffic from the permanent cable runs and acts as the demarcation point between the building wiring and the switch fabric
*   **Correct Answer:** B) A patch panel — it provides fixed termination points for horizontal cable runs and allows short patch cables to connect any wall jack to any switch port
*   **Distractor Analysis:**
    * *Why B is correct:* A patch panel is a passive termination and organization device; permanent cable runs punch down into the back of the patch panel, and short patch cables on the front connect specific wall jack ports to specific switch ports, enabling flexible port assignment without touching the permanent in-wall wiring.
    * *Why A is incorrect:* A PoE injector adds power to an Ethernet cable for a single device — it is not a multi-port termination or cable management device.
    * *Why C is incorrect:* A switch is an active Layer 2 forwarding device; while it does build MAC address tables, it does not replace the cable management and termination function of a patch panel in a structured cabling installation.
    * *Why D is incorrect:* A firewall is a security device that filters traffic by policy rules; it does not serve as a physical cable termination point and is not placed between horizontal runs and a switch in standard structured cabling design.


---

**Question 5**
A small office has a single internet connection from the ISP delivered as a coaxial cable. The office needs multiple wired workstations and wireless laptops to share the connection. Which combination of devices provides internet access to all clients?
*   A) A cable modem connected to the coaxial line, then a wireless router connected to the modem — the modem converts the ISP signal to Ethernet, and the router provides DHCP, NAT, switching, and wireless access for all clients
*   B) A patch panel connected to the coaxial line, then a managed switch — the patch panel converts the ISP signal to Ethernet and the switch provides DHCP and wireless access to all clients
*   C) A WAP connected directly to the coaxial line — modern WAPs include built-in DOCSIS modems and can connect directly to cable TV coaxial outlets without any additional devices
*   D) A firewall connected to the coaxial line, then individual Ethernet cables run directly from the firewall to each workstation and laptop without any switching or routing hardware
*   **Correct Answer:** A) A cable modem connected to the coaxial line, then a wireless router connected to the modem — the modem converts the ISP signal to Ethernet, and the router provides DHCP, NAT, switching, and wireless access for all clients
*   **Distractor Analysis:**
    * *Why A is correct:* This is the standard home and small office internet architecture: the cable modem terminates the ISP's DOCSIS coaxial signal and presents an Ethernet WAN port; the wireless router connects to that Ethernet port and provides DHCP addressing, NAT, LAN switching, and Wi-Fi to all clients through a single combined device.
    * *Why B is incorrect:* A patch panel is a passive cable termination device with no signal conversion capability; it cannot convert a DOCSIS coaxial signal to Ethernet, and a switch does not provide DHCP, NAT, or wireless access.
    * *Why C is incorrect:* Standard WAPs do not include built-in cable modems and cannot connect directly to a coaxial ISP line; DOCSIS modem functionality is a separate hardware component.
    * *Why D is incorrect:* A firewall alone cannot terminate a coaxial ISP connection, and without a switch the firewall would have insufficient ports to connect multiple wired workstations simultaneously using a standard device.
