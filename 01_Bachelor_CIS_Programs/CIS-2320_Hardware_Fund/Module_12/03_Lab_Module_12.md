# Lab Activity: Module 12 - Network Infrastructure Devices

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.2
**Texas Wesleyan University | Professor Nash**
**Total Points: 100**

---

## Overview

This lab develops the identification and analysis skills required for the CompTIA A+ Core 1 exam's network device domain. You will classify devices by OSI layer and function, analyze PoE port labeling scenarios, construct and annotate a network topology diagram, and work through device selection scenarios that mirror the format of A+ exam questions.

No physical hardware configuration is required. All exercises use written analysis, structured tables, and diagram annotation.

**Learning Objectives:**

- Assign each network infrastructure device to its correct OSI layer and explain how that layer informs the device's forwarding behavior
- Distinguish switch, router, WAP, firewall, modem, and patch panel by function
- Apply PoE standard knowledge to determine whether a given switch port can power a given device
- Construct a correct device-placement diagram for a small office network
- Analyze realistic network scenarios and identify the correct device to solve each problem

**Estimated Completion Time:** 60-90 minutes

**Submission:** Submit your completed lab document (typed responses) to Canvas by the posted due date.

---

## Part 1 — Device Identification by Function (30 points)

### Part 1A — OSI Layer and Function Classification Table

Complete the table below. For each device, fill in the OSI layer it operates at (or write "Passive" if applicable), the primary forwarding or function method, and one real-world example of where you would find it in a small office network.

| Device | OSI Layer | Primary Function / Forwarding Method | Where Found in a Small Office Network |
|--------|-----------|--------------------------------------|--------------------------------------|
| Hub | | | |
| Unmanaged Switch | | | |
| Managed Switch | | | |
| Router | | | |
| Wireless Access Point (WAP) | | | |
| Firewall | | | |
| Cable Modem | | | |
| Patch Panel | | | |

After completing the table, answer the following questions.

**Question 1A-1:** A user reports that their computer is "slow when other people are downloading." The IT manager says the network has not been upgraded since 2003 and uses the original hub-based infrastructure. Explain why the hub causes this symptom and what device replacement would solve it.

*Your answer:*

**Question 1A-2:** A new employee asks why the network closet has a panel with labeled ports connected by short cables to the switch, instead of the wall cables plugging directly into the switch. Explain the purpose of the patch panel and name two operational advantages it provides.

*Your answer:*

---

### Part 1B — Device Selection Scenario Table

For each scenario below, identify the single network infrastructure device that best solves the described problem. Choose from: hub, switch, router, WAP, firewall, cable modem, patch panel, PoE injector. Write your answer and a one-sentence justification.

| Scenario | Device | Justification |
|----------|--------|--------------|
| A company wants to segment visitor Wi-Fi from the employee network using separate SSIDs on shared physical infrastructure. | | |
| An office is adding three IP cameras to a closet that has an Ethernet run but no power outlet nearby. The existing switch is not PoE-capable. | | |
| An ISP delivers internet service via coaxial cable. The office needs to connect the ISP signal to their router. | | |
| The IT manager wants to block all inbound traffic from known malicious IP address ranges before it reaches the internal network. | | |
| Fifty workstations need to communicate with each other on the same local subnet at Gigabit speeds without sharing bandwidth. | | |
| A remote employee in a satellite office needs to connect their office's LAN to the main office's LAN over the internet via a routed IP connection. | | |

---

## Part 2 — PoE Standards Analysis (30 points)

### Part 2A — PoE Standard Identification

Complete the PoE standards reference table from memory, then verify against your Reading Guide.

| Standard | Common Name | Max Power at Port | Typical Device Example |
|----------|-------------|------------------|----------------------|
| IEEE 802.3af | | | |
| IEEE 802.3at | | | |
| IEEE 802.3bt (Type 3) | | | |
| IEEE 802.3bt (Type 4) | | | |

---

### Part 2B — PoE Port Labeling Exercise

A 24-port managed switch has the following PoE port labels. For each device listed in the table, determine whether the switch port can supply adequate power. Write "Yes — adequate" or "No — insufficient" and explain your reasoning.

The switch specifications are:

- Ports 1–12: IEEE 802.3af (15.4 W per port)
- Ports 13–20: IEEE 802.3at (30 W per port)
- Ports 21–24: IEEE 802.3bt Type 3 (60 W per port)
- Total switch PoE budget: 370 W

| Device | Rated Power Draw | Connected to Port | Adequate? | Reasoning |
|--------|-----------------|------------------|-----------|-----------|
| VoIP telephone | 6 W | Port 4 (802.3af) | | |
| IP camera, fixed lens | 12 W | Port 8 (802.3af) | | |
| IP camera, PTZ (pan/tilt/zoom) | 25 W | Port 9 (802.3af) | | |
| Enterprise WAP | 22 W | Port 15 (802.3at) | | |
| Thin client workstation | 50 W | Port 18 (802.3at) | | |
| Laptop dock | 45 W | Port 22 (802.3bt) | | |

**Question 2B-1:** The PTZ camera in the table above is failing to power on. A technician wants to move its cable to a different port to resolve the issue. Which port range (1–12, 13–20, or 21–24) should the technician use, and why?

*Your answer:*

**Question 2B-2:** If all 24 ports are simultaneously connected to devices at their maximum rated power, calculate whether the switch's 370 W budget is sufficient. Show your calculation (12 ports × 15.4 W) + (8 ports × 30 W) + (4 ports × 60 W) and state whether the budget is adequate.

*Your answer:*

---

## Part 3 — Network Topology Diagram and Scenario Analysis (40 points)

### Part 3A — Network Topology Diagram Annotation

The following describes a small office network. Read the description and then fill in the blank device labels in the topology table below.

Network description: The ISP delivers service via coaxial cable. A device at the edge of the network converts the DOCSIS signal to Ethernet. That Ethernet output connects to a security device that inspects all inbound and outbound traffic against policy rules. From the security device, traffic flows to a device that handles IP address assignment (DHCP), NAT, and routing between the internal network and the internet. That device connects to a 24-port managed device that forwards frames on the internal LAN using MAC address tables. All horizontal cable runs from offices throughout the building terminate on a passive rack panel before connecting via patch cables to the managed device. A ceiling-mounted device in the conference room connects wireless laptops to the wired network.

Fill in the device label for each position in the diagram:

| Position in Topology | Device Label |
|---------------------|-------------|
| ISP coaxial cable terminates here; converts to Ethernet | |
| Inspects all traffic at the network perimeter; enforces access policies | |
| Assigns IP addresses via DHCP; performs NAT; routes between LAN and WAN | |
| Forwards frames within the LAN using MAC address tables; 24 ports | |
| Passive rack panel; horizontal runs terminate here; connects to managed device via patch cables | |
| Ceiling-mounted device; bridges wireless laptops to wired LAN | |

**Question 3A-1:** Which device in the topology above is responsible for assigning IP addresses to the office workstations? Identify it by its position label and explain the protocol it uses to perform this function.

*Your answer:*

**Question 3A-2:** A workstation on Port 7 of the managed device cannot reach a web server on the internet, but it can reach other workstations on the same LAN. Which specific device in the topology is the most likely source of this problem, and what function does that device perform that is required for internet access?

*Your answer:*

---

### Part 3B — Device Scenario Analysis

Read each scenario and provide a complete written response.

**Scenario 1:**
A small law firm has a single internet connection and wants to provide Wi-Fi to both clients in the waiting room and employees in the back office, with the client Wi-Fi completely isolated from the employee network. The office currently has a single unmanaged switch and a combined modem/router provided by the ISP.

Describe what additional hardware the firm needs to accomplish this, which devices would need to be replaced or added, and explain what network feature (on which device) enforces the isolation between the two Wi-Fi networks.

*Your answer:*

**Scenario 2:**
A technician installs a new IP security camera system in a warehouse. There are twelve cameras, each rated at 13 W. The warehouse network closet has a standard unmanaged switch with no PoE capability. The cameras must be operational within 48 hours and running new electrical circuits to each camera location is not an option.

Identify the PoE-related solution options available to the technician. Which IEEE PoE standard covers a 13 W device? Calculate the total power requirement for all twelve cameras and determine whether a single switch with a 200 W PoE budget would be adequate.

*Your answer:*

---

## Deliverables and Grading Rubric

Submit your completed lab responses as a single typed document to the Canvas assignment portal.

| Component | Points |
|-----------|--------|
| Part 1A — Classification table (8 rows complete and correct) | 16 pts |
| Part 1A — Written questions 1A-1, 1A-2 (4 pts each) | 8 pts |
| Part 1B — Device selection table (6 rows, 1 pt each) | 6 pts |
| Part 2A — PoE standards table (4 rows complete and correct) | 8 pts |
| Part 2B — PoE port table (6 rows) + questions 2B-1, 2B-2 | 14 pts |
| Part 3A — Topology diagram + questions 3A-1, 3A-2 | 24 pts |
| Part 3B — Scenario analysis (2 scenarios, 12 pts each) | 24 pts |
| **Total** | **100 pts** |

**Grading Notes:**

- Table cells must use correct device names and OSI layers. "I don't know" or blank cells receive zero for that row.
- Scenario responses must identify correct devices and explain the technical reasoning. Vague answers receive partial credit only.
- PoE calculations must show the arithmetic, not just a final answer.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — Packet Tracer Network Build

Download and install Cisco Packet Tracer (free at netacad.com with a free Networking Academy account) and build the following network topology:

1. Place one router, one 24-port managed switch, two PCs, and one wireless access point on the canvas. Connect the devices: PC1 to switch port 1, PC2 to switch port 2, the WAP to switch port 3, and the switch's uplink port to the router's LAN interface. Configure the router with IP address 192.168.1.1/24 on the LAN interface and enable DHCP for the 192.168.1.0/24 subnet. Verify that both PCs receive IP addresses automatically and can ping each other and the router.
1. Create two VLANs on the managed switch: VLAN 10 (name: "Workstations") assigned to ports 1 and 2, and VLAN 20 (name: "Guest") assigned to port 4. Configure the router uplink port as a trunk carrying both VLANs. Configure sub-interfaces on the router for each VLAN (192.168.10.1/24 for VLAN 10; 192.168.20.1/24 for VLAN 20) and enable DHCP for each subnet. Document the commands used and verify that a PC on VLAN 10 can ping the router's VLAN 10 sub-interface.
1. Write 2–3 sentences explaining why two PCs on different VLANs on the same physical switch cannot communicate without the router, even though they are physically connected to the same hardware. Reference the OSI layer at which VLANs operate and the OSI layer at which the router resolves the isolation.

### Challenge Step 2 — Wireshark ARP and DHCP Capture

Download and install Wireshark (free at wireshark.org) on any available Windows or macOS computer connected to a local network:

1. Start a packet capture on the active network interface. Open a command prompt and run `arp -d *` (Windows) or `sudo arp -d -a` (macOS) to clear the ARP cache, then ping the default gateway (find it with `ipconfig` or `ifconfig`). Stop the capture after 30 seconds. Filter the results using the display filter `arp` and locate the ARP request and ARP reply packets. Document: the source MAC, destination MAC (broadcast for request), source IP, and the IP being resolved in the request; and the source MAC, destination MAC, and the MAC-to-IP mapping in the reply.
1. Start a second capture on the same interface. Open a command prompt and run `ipconfig /release` then `ipconfig /renew` (Windows) to force a DHCP transaction. Filter using `bootp` or `dhcp`. Locate the four DHCP exchange packets (Discover, Offer, Request, Acknowledge) and for each one document: the source IP, destination IP, and what information the packet carries (what the client is asking for, what the server is offering or confirming).
1. Write 2–3 sentences explaining what would happen to the ARP and DHCP traffic behavior if you replaced the managed switch in this network with an unmanaged hub — specifically addressing which devices would receive the ARP broadcast and why this creates a security and performance concern that VLANs on a managed switch eliminate.

### Challenge Step 3 — Double-NAT Diagnosis and Resolution

Research the double-NAT problem described in Question 11 and document the complete resolution procedure:

1. Describe two methods for resolving double-NAT when a second consumer router is connected to the LAN port of a first router: (a) putting the second router in AP (Access Point) mode by disabling its DHCP server and connecting it via a LAN-to-LAN cable rather than WAN-to-LAN, and (b) configuring the second router as a true router with proper static routes. For method (a), write the exact configuration steps needed on the second router. For method (b), write the routing table entries that would need to be added to both routers to enable bi-directional communication.
1. Research the term "CGNAT" (Carrier-Grade NAT) — a situation where the ISP itself places the subscriber behind NAT before the public internet, assigning a private RFC 6598 address (100.64.0.0/10) to the modem's WAN interface. Explain in 2–3 sentences how CGNAT creates a triple-NAT scenario in a home with a consumer router, and why port forwarding configured on the consumer router will not work for hosting a server when CGNAT is in use.
1. Research and document what IPv6 eliminates from this entire discussion: explain why IPv6 removes the need for NAT entirely, how IPv6 addresses allow every device to have a globally routable address, and why this is beneficial for peer-to-peer applications and IoT devices while also introducing new security considerations that a firewall must address.
