# Video Script: Module 12 - Network Infrastructure Devices

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.2: Compare and contrast common networking hardware
**Estimated Duration:** 20-24 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

**Components to have on camera or in slides:**

- Physical samples or labeled photos: unmanaged switch, managed switch, home wireless router, standalone WAP
- Physical sample or labeled image: cable modem, DSL modem
- Physical sample or image: patch panel (front and back view)
- PoE switch with port labels showing PoE indicators
- OSI layer diagram (Layers 1–3 labeled with device assignments)

**Key exam traps to call out verbally:**

- Hub = Layer 1 (dumb repeater); switch = Layer 2 (MAC); router = Layer 3 (IP) — these OSI assignments are directly tested
- A switch does NOT assign IP addresses — DHCP is the router's or a server's job
- A home "wireless router" is actually three devices in one: router + switch + WAP
- PoE standards: 802.3af = 15.4 W, 802.3at = 30 W, 802.3bt = 60–100 W — exam tests specific wattage values
- A patch panel is passive — it has no power, no intelligence, no MAC table; it is only a termination and organization point

---

## [00:00 - 02:30] Section 1 — Introduction and Certification Alignment

**[SHOW COMPONENT: Title slide — "Module 12: Network Infrastructure Devices"]**

Welcome back, everyone. I am Professor Nash, and this is Module 12 of CIS-2320 Hardware Fundamentals. Today we are covering the devices that make up a functioning network — not the cables, but the actual hardware boxes: switches, routers, wireless access points, firewalls, modems, and patch panels. We will also cover Power over Ethernet, which is the IEEE standard that lets a switch deliver electrical power to devices like phones and cameras over the same Ethernet cable used for data.

Every single one of these devices appears on the CompTIA A+ Core 1 exam. The exam will give you a scenario — a user cannot get an IP address, or an office needs to power ten IP cameras without running electrical outlets to the ceiling — and you need to know which device solves the problem and why. That is what we are building toward today.

**[PAUSE — transition to slide: "What We Cover Today"]**

Our five sections today are: Layer 1 through Layer 3 devices and the OSI model — this is the framework the exam uses to categorize every device we discuss. Then switches in depth. Then routers and how they differ from switches. Then wireless access points, firewalls, modems, and patch panels. And finally, PoE standards and where they fit into a network rack.

---

## [02:30 - 07:30] Section 2 — OSI Layer Assignments and the Hub vs Switch vs Router Hierarchy

**[SHOW COMPONENT: OSI Layer diagram — Layers 1, 2, 3 highlighted with device labels]**

Before we go device by device, I want to give you the conceptual framework the exam uses to test these devices. The OSI model — the Open Systems Interconnection model — has seven layers. For the A+ exam, the three you need to know for device categorization are Layers 1, 2, and 3.

Layer 1 is the Physical layer. It deals with raw electrical or optical signals — ones and zeros moving through a cable. A hub operates at Layer 1. A hub is a simple device with multiple ports that repeats every signal it receives out of every other port simultaneously. It has no intelligence. It does not read MAC addresses or IP addresses. Every device connected to a hub competes for the same bandwidth, which is why hubs are obsolete and you will never install one in a modern network. But you will see them on the exam as the wrong answer for scenarios that require a switch.

**[PAUSE — exam tip on slide: "Hub = Layer 1 = dumb repeater — each port shares total bandwidth"]**

Layer 2 is the Data Link layer. Switches operate at Layer 2. A switch reads the MAC address in every Ethernet frame that arrives on a port. It builds a MAC address table that maps each device's hardware address to the specific port that device is connected to. When a frame arrives for a known destination, the switch sends it only to the correct port — not to every port like a hub. This creates separate collision domains per port and makes much more efficient use of bandwidth. Every port on a modern switch operates at its full rated speed.

**[SHOW COMPONENT: Switch MAC address table diagram on slide]**

Layer 3 is the Network layer. Routers operate at Layer 3. Instead of MAC addresses, routers read IP addresses in packet headers to make forwarding decisions. A router connects two or more different IP networks or subnets. The most common example is a home or office router that connects the internal LAN to the internet. The router has a WAN port connected to the ISP modem and LAN ports connected to the internal network. It performs NAT — Network Address Translation — which maps internal private IP addresses to the single public IP provided by the ISP. Routers also run or forward DHCP to assign IP addresses to clients, though DHCP can also run on a dedicated server.

**[PAUSE — critical exam tip slide: "Switch = Layer 2 MAC. Router = Layer 3 IP. Switch does NOT assign IP addresses."]**

---

## [07:30 - 13:00] Section 3 — Switches, WAPs, Firewalls, and Modems in Depth

**[SHOW COMPONENT: Managed switch on camera or image — showing port LEDs, uplink ports]**

Let us go deeper on switches. There are two main categories: unmanaged and managed.

An unmanaged switch is plug-and-play — you connect cables and it works. There is no configuration interface. Unmanaged switches are common in small offices and home environments. They forward frames based on MAC addresses automatically with no administrator involvement.

A managed switch adds a configuration interface — typically accessible through a web browser or a command-line interface via a console cable. Managed switches support VLANs (Virtual LANs) that segment a network into separate logical groups even on the same physical hardware, Spanning Tree Protocol to prevent network loops, port mirroring for traffic analysis, and Quality of Service settings to prioritize voice or video traffic. Enterprise networks use managed switches exclusively.

**[SHOW COMPONENT: Wireless access point on camera or image — antenna visible, Ethernet port on back]**

A wireless access point, or WAP, is a Layer 2 device. It connects wirelessly through the 2.4 GHz or 5 GHz radio frequency bands and bridges that wireless traffic to a wired Ethernet uplink. The WAP broadcasts an SSID — the network name you see when you scan for Wi-Fi on your phone. Wi-Fi standards have evolved: 802.11a, b, g, n, ac, and now ax — which is marketed as Wi-Fi 6. Each generation added speed, improved frequency band support, or better handling of many simultaneous clients.

**[PAUSE — slide: "WAP broadcasts SSID. Bridges wireless to wired. Operates at Layer 2."]**

A firewall is a security device that inspects network traffic and enforces rules. A basic firewall operates at Layer 3 and 4 — it reads IP addresses and TCP/UDP port numbers to allow or block traffic. Advanced next-generation firewalls inspect traffic all the way up to Layer 7, looking at application-layer content. Every network that connects to the internet should have a firewall between the LAN and the WAN.

A modem — short for modulator-demodulator — converts the digital Ethernet signal from your router into whatever signal format the ISP's infrastructure uses. A cable modem converts to DOCSIS signal over coaxial cable. A DSL modem converts to DSL signal over telephone lines. A fiber ONT (Optical Network Terminal) converts to fiber optic signal. The modem is the device at the boundary between your local network and the ISP's network. In many home deployments, the modem and router are combined in a single unit supplied by the ISP.

**[SHOW COMPONENT: Patch panel — front view showing numbered ports, back view showing punch-down blocks]**

A patch panel is passive — I want to say that word clearly: passive. It has no power supply, no processor, no MAC address table. It is simply a panel of RJ-45 jacks mounted in a rack, with the horizontal cable runs from throughout the building punched down on the back. The patch panel gives you a clean, organized termination point for every permanent cable run, and then short patch cables on the front connect specific ports to specific switch ports. This matters for moves, adds, and changes — if a user moves to a new office, you just move the patch cable on the panel rather than rerouting a cable through the wall.

---

## [13:00 - 17:30] Section 4 — Power over Ethernet Standards

**[SHOW COMPONENT: PoE switch port close-up — showing PoE indicator LEDs and "PoE" port labeling]**

Power over Ethernet is one of the most tested topics in this module. Let me give you the three standards you must memorize.

IEEE 802.3af — this is the original PoE standard. It delivers up to 15.4 watts of power at the switch port, with about 12.95 watts available at the powered device after cable losses. This is enough for IP phones, basic IP cameras, and small wireless access points. If you see a question about a VoIP phone being powered over Ethernet, 802.3af is the standard that covers it.

**[PAUSE — slide: "802.3af = 15.4 W (PoE). 802.3at = 30 W (PoE+). 802.3bt = 60–100 W (PoE++)."]**

IEEE 802.3at — called PoE Plus or PoE+ — delivers up to 30 watts at the switch port, with about 25.5 watts available at the device. This covers higher-powered WAPs, video conferencing cameras, and IP cameras with pan/tilt/zoom motors.

IEEE 802.3bt — called PoE++ or 4PPoE — delivers 60 watts (Type 3) or up to 100 watts (Type 4) by using all four pairs of the Ethernet cable simultaneously for power. This covers laptops, thin clients, and other high-draw devices that were previously impractical to power over Ethernet.

A switch port must be PoE-capable to deliver power. A non-PoE switch will not damage a PoE device plugged into it — the device simply will not receive power over the cable and will need its own power adapter. If a switch port does not have enough PoE budget for all connected devices simultaneously, some devices will not receive power — this is a PoE budget exhaustion issue that the exam tests.

**[SHOW COMPONENT: Network rack diagram — patch panel at top, switch below, modem/router at bottom]**

---

## [17:30 - 21:30] Section 5 — Network Topology in a Rack and Lab Preparation

**[SHOW COMPONENT: Rack diagram with labeled components: patch panel, switch, router, firewall, modem]**

Let me walk you through what a typical small enterprise network rack looks like from bottom to top. At the bottom or outside the rack is the ISP connection — coaxial, fiber, or telephone line — which goes into the modem. The modem's Ethernet output connects to the WAN port of the router or firewall. The router handles DHCP, NAT, and policy routing between the internal network and the internet. Below the firewall or router is the core switch — this is the managed switch that all the patch panel ports connect to. And at the top of the rack is the patch panel, where every horizontal cable run from every wall jack in the building terminates.

Traffic flow goes like this: a workstation sends a frame to a wall jack, through the horizontal run to the patch panel, through a short patch cable to the switch port, the switch makes a Layer 2 forwarding decision, the frame goes to its destination on the local network — or if the destination is outside the LAN, it goes to the router's LAN port, through the router's NAT engine, out the WAN port, through the modem, and onto the internet.

**[PAUSE — slide: "Traffic path: Workstation → Patch Panel → Switch → Router → Modem → Internet"]**

For this week's lab you will be identifying devices by function, labeling a network topology diagram, analyzing PoE port scenarios, and documenting which OSI layer each device operates at. The lab uses written analysis exercises rather than physical configuration — read through all three parts before starting.

---

## [21:30 - End] End Card

Thank you for watching Module 12. Here is what I need you to do before our next session:

First, read the Reading Guide for Module 12. It expands significantly on the OSI layer assignments, PoE standards table, and device comparison tables.

Second, complete Lab 12. Work through all three parts and submit your deliverables to Canvas.

Third, take Quiz 12.

Finally, post to the Module 12 Discussion Board by Wednesday at 11:59 PM and respond to two classmates by Sunday.

**[PAUSE — slide: "Module 12 Resources"]**

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 Study Notes — Network Infrastructure Devices section: professormesser.com
- CompTIA A+ Exam Objectives (220-1101) — Domain 2.2: comptia.org
- IEEE 802.3 PoE Standards Overview — available through your institution's library database
