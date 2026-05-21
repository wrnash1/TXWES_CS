# Reading Guide: Module 12 - Network Infrastructure Devices
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 12 - Network Infrastructure Devices**! This module covers the hardware devices that form a functioning network — switches, routers, wireless access points, firewalls, modems, and patch panels — and the Power over Ethernet standard that eliminates separate power cables for network-attached devices. Understanding what each device does and where it sits in a network topology is essential for the **CompTIA A+ Core 1 (220-1101)** exam and for everyday technician work in any networked environment.

As a technician, you must be able to identify each device by function, explain which OSI layer it operates at, and recommend the correct device for a given network scenario. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **switches vs routers**: A switch operates at OSI Layer 2 (Data Link) and forwards frames between devices on the same local network segment using MAC address tables; each port is a separate collision domain. A router operates at OSI Layer 3 (Network) and forwards packets between different IP networks or subnets using routing tables; a router connects a LAN to the internet or to other networks. A home "wireless router" is actually a combined device containing a router, a switch, and a wireless access point in one unit.
*   **WAPs (Wireless Access Points)**: A wireless access point (WAP) is a Layer 2 device that connects wireless clients to a wired network by bridging Wi-Fi traffic to an Ethernet uplink. A WAP broadcasts an SSID (network name) on a chosen channel within the 2.4 GHz or 5 GHz frequency band. Wi-Fi standards include 802.11a/b/g/n/ac/ax (Wi-Fi 6); the standard determines maximum theoretical throughput and frequency band support. Enterprise environments deploy multiple WAPs managed by a wireless controller to provide seamless roaming coverage.
*   **firewalls and modems**: A firewall is a security device (hardware or software) that inspects incoming and outgoing network traffic and enforces rules to block unauthorized connections; it operates at Layers 3–7 depending on its inspection depth. A modem (modulator-demodulator) converts the digital signals from a router into the analog or encoded signal format used by the ISP's physical medium (cable, DSL, fiber). Cable modems use DOCSIS standards; DSL modems use telephone lines. In most home setups, the modem is the boundary between the ISP's network and the home network.
*   **patch panels and PoE**: A patch panel is a passive mounting point in a network rack where horizontal cable runs from wall jacks terminate and can be connected to switch ports via short patch cables, enabling organized cable management without disturbing permanent runs. PoE (Power over Ethernet) is defined by IEEE 802.3af (15.4W), 802.3at/PoE+ (30W), and 802.3bt/PoE++ (60–100W); it allows a PoE-capable switch port to deliver DC power over the same Ethernet cable used for data, eliminating separate power supplies for IP phones, cameras, and wireless access points.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 2.2):** The A+ exam presents network device identification scenarios. Memorize the OSI layer for each device: hub = Layer 1 (repeats all traffic); switch = Layer 2 (MAC addresses); router = Layer 3 (IP addresses). A common question asks which device to use to connect two separate office subnets — the answer is always a router, not a switch.
*   **Scenario Trap:** A frequent A+ distractor describes a user who cannot get an IP address and asks which device to check. The answer depends on where DHCP is being served — it could be the router or a dedicated DHCP server. Do not automatically select "switch" when IP addressing is the problem; switches do not assign IP addresses by default.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers all network infrastructure devices with OSI layer diagrams and real-world placement examples. Navigate to the networking devices section for side-by-side comparisons of switches, routers, and WAPs: [Professor Messer's CompTIA A+ Core 1 Course — Network Devices](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Study the PoE standard comparison table and the hub vs switch vs router differentiation.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the network infrastructure devices section in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on switches, routers, WAPs, firewalls, modems, patch panels, and PoE standards.
*   **Required Video:** Watch the video lecture on network infrastructure devices from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering OSI layer assignments for each device and PoE power delivery standards.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Identify switch ports vs router WAN interfaces**: Examine a home gateway device. Identify the LAN ports (switch side) versus the WAN port (router side connecting to the modem). Document the physical differences and explain which port a PC connects to versus which port an ISP modem connects to.
*   **Configure a wireless access point SSID and channel**: Access a WAP's web management interface. Set the SSID (network name) and choose a non-overlapping Wi-Fi channel (1, 6, or 11 for 2.4 GHz). Save the configuration and verify a wireless client can detect and connect to the new SSID.
*   **Plug in a VoIP phone using a PoE port on a switch**: Connect a PoE-capable IP phone to a PoE switch port using a single Ethernet cable. Verify the phone powers on and registers without a separate power adapter. Check the switch management interface to confirm the port is delivering PoE and note the power draw in watts.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the network infrastructure devices sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on network infrastructure devices in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the device configuration steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
