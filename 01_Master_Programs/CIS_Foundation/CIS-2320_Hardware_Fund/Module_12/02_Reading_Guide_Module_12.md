# Reading Guide: Module 12 - Network Infrastructure Devices

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2320 &BULL; HARDWARE FUNDAMENTALS & PC ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.2
**Texas Wesleyan University | Professor Nash**

---

## Introduction

Welcome to Module 12 — Network Infrastructure Devices. This module covers the hardware devices that form a functioning network: switches, routers, wireless access points, firewalls, modems, patch panels, and the Power over Ethernet standard. Understanding what each device does, which OSI layer it operates at, and where it belongs in a network topology is central to the CompTIA A+ Core 1 (220-1101) exam under Domain 2.2.

As a technician, you must be able to identify each device by function, recommend the correct device for a given network scenario, and explain PoE power delivery standards. Master the content in this guide before the lab.

---

## Section 1 — OSI Layer Device Assignments

### The Three Layers That Matter for A+

The CompTIA A+ exam uses the OSI model to categorize networking devices. You must know the layer assignment for every device in this module without hesitation.

| Device | OSI Layer | Forwarding Method | Intelligence |
|--------|-----------|------------------|-------------|
| Hub | Layer 1 — Physical | Repeats signal to all ports | None — dumb repeater |
| Switch | Layer 2 — Data Link | MAC address table | Learns MAC addresses dynamically |
| Router | Layer 3 — Network | IP routing table | Routes between subnets/networks |
| WAP | Layer 2 — Data Link | MAC bridging (wireless to wired) | SSID, channel, security |
| Firewall | Layers 3–7 | Policy rules (IP, port, application) | Security enforcement |
| Patch Panel | Passive — no layer | Physical termination only | None |

### Hub Detail

A hub is a Layer 1 device. It receives an electrical signal on one port and immediately repeats that signal out of every other port. Every device connected to a hub shares the total bandwidth — if you have a 10 Mbps hub with five devices, all five devices compete for that 10 Mbps. Hubs create a single collision domain for all connected ports. Hubs are obsolete and are never installed in modern networks, but the A+ exam uses them as a distractor answer in switch/router scenarios. When the exam describes a device that "repeats traffic to all ports," the answer is hub.

### Switch Detail

A switch is a Layer 2 device that builds and maintains a MAC address table. When a frame arrives on a port, the switch reads the source MAC address and records which port that device is connected to. When a frame arrives for a known destination MAC, the switch sends it only out the correct port. Unknown destinations cause the switch to flood the frame to all ports — this is called a broadcast or unknown unicast flood. Each switch port is its own collision domain, which eliminates collisions between ports and allows each port to run at its full rated speed.

Switches come in two types: unmanaged (plug-and-play, no configuration) and managed (configurable VLANs, STP, QoS, port mirroring, SNMP monitoring).

### Router Detail

A router is a Layer 3 device that makes forwarding decisions based on IP addresses in packet headers. A router connects two or more different networks or subnets. The most important router functions for the A+ exam:

- Routing: forwards packets between networks using a routing table
- DHCP: assigns IP addresses to clients on the LAN (or forwards requests to a DHCP server)
- NAT: translates internal private IP addresses to the public IP address assigned by the ISP
- WAN connectivity: connects the LAN to the ISP's network via the modem

A home or small-office "wireless router" is actually three devices combined: a router, a multi-port switch, and a wireless access point. The exam may present this as a distractor — the routing function, the switching function, and the wireless access function are all distinct capabilities that can be provided by separate devices in an enterprise environment.

---

## Section 2 — Wireless Access Points

### WAP Function and Operation

A wireless access point (WAP) is a Layer 2 device that bridges wireless client traffic to a wired Ethernet uplink. It broadcasts an SSID (Service Set Identifier — the network name) on a chosen radio channel within the 2.4 GHz or 5 GHz frequency band. Client devices associate with the WAP by authenticating using WPA2 or WPA3 security protocols and then send and receive frames through the WAP as if connected to the wired switch via the Ethernet uplink.

### Wi-Fi Standard Comparison

| Standard | Frequency | Max Theoretical Speed | Common Name |
|----------|-----------|----------------------|-------------|
| 802.11a | 5 GHz | 54 Mbps | — |
| 802.11b | 2.4 GHz | 11 Mbps | — |
| 802.11g | 2.4 GHz | 54 Mbps | — |
| 802.11n | 2.4 / 5 GHz | 600 Mbps | Wi-Fi 4 |
| 802.11ac | 5 GHz | 3.5 Gbps (Wave 2) | Wi-Fi 5 |
| 802.11ax | 2.4 / 5 / 6 GHz | 9.6 Gbps | Wi-Fi 6 |

For the A+ exam, focus on 802.11n (dual-band, MIMO), 802.11ac (5 GHz, high speed), and 802.11ax (Wi-Fi 6, improved multi-client performance). The non-overlapping 2.4 GHz channels are 1, 6, and 11 — a frequently tested detail.

### Enterprise WAP Deployment

In enterprise environments, multiple WAPs are deployed throughout a building and managed by a wireless LAN controller (WLC). The controller handles roaming handoffs between WAPs, uniform SSID configuration, and radio frequency management. Individual WAPs in a controller-based deployment are called lightweight APs. Home-grade WAPs are standalone (autonomous) APs that manage themselves.

---

## Section 3 — Firewalls and Modems

### Firewall Types and Operation

A firewall enforces access control policies on network traffic. Types by capability:

- Packet-filtering firewall: inspects IP source/destination and TCP/UDP port numbers at Layers 3 and 4. Fast but limited — cannot inspect content inside packets.
- Stateful inspection firewall: tracks the state of TCP connections and permits return traffic for established sessions automatically.
- Next-generation firewall (NGFW): adds application-layer inspection (Layer 7), intrusion prevention, and deep packet inspection to stateful filtering.

In a home or small office, firewall functionality is built into the router/gateway device. In enterprise networks, a dedicated hardware firewall appliance sits at the network perimeter between the router and the WAN connection.

### Modem Types

A modem converts between the digital Ethernet signal of the local network and the physical medium used by the ISP.

| Modem Type | ISP Medium | Standard |
|------------|-----------|---------|
| Cable modem | Coaxial cable | DOCSIS (Data Over Cable Service Interface Specification) |
| DSL modem | Telephone copper pair | DSL (ADSL, VDSL variants) |
| Fiber ONT | Fiber optic | GPON or XGS-PON (varies by ISP) |

The modem is the demarcation point between the ISP's network and the customer's equipment. Everything on the customer side of the modem is the customer's responsibility. The ISP owns and supports the modem and everything on the WAN side.

---

## Section 4 — Patch Panels and Structured Cabling

### Patch Panel Purpose and Construction

A patch panel is a passive rack-mounted panel with rows of RJ-45 keystone jacks on the front and 110-type punch-down blocks on the back. Horizontal cable runs from wall jacks throughout the building terminate (punch down) on the back of the patch panel. Short patch cables on the front connect specific panel ports to specific switch ports.

The patch panel serves three purposes:

1. Organization: provides a central, labeled termination point for all horizontal runs
2. Protection: permanent cable runs are never directly connected to switch ports, so moves and changes only require moving a patch cable rather than re-routing a wall run
3. Flexibility: any wall jack can be connected to any switch port by moving one short patch cable on the panel

### Patch Panel Characteristics

- Passive: no power, no electronics, no intelligence
- Typically available in 12, 24, or 48 port configurations for 1U rack space
- Cat5e, Cat6, and Cat6a versions — the panel must match or exceed the cable category
- Ports are numbered and labeled; a port map document shows which panel port corresponds to which wall jack location

---

## Section 5 — Power over Ethernet Standards

### PoE Standards Comparison Table

| Standard | Common Name | Max Power at Port | Typical Devices Powered |
|----------|-------------|------------------|------------------------|
| IEEE 802.3af | PoE | 15.4 W | IP phones, basic IP cameras, simple WAPs |
| IEEE 802.3at | PoE+ | 30 W | Higher-power WAPs, PTZ cameras, video phones |
| IEEE 802.3bt Type 3 | PoE++ | 60 W | Laptops, thin clients, advanced WAPs |
| IEEE 802.3bt Type 4 | PoE++ | 100 W | High-draw devices, small appliances |

### How PoE Works

A PoE switch port detects whether a connected device is a PoE-capable powered device (PD) before delivering power. This detection process uses a low-voltage signal to identify the PD and its power class — if no PD is detected, no power is delivered. This prevents damage to non-PoE devices. The power is delivered over the same four pairs used for data at 100 Mbps and 1 Gbps (802.3af/at use two pairs for power; 802.3bt uses all four pairs).

A PoE injector is a mid-span device that adds PoE capability to a cable run connected to a non-PoE switch. You plug the non-PoE switch port into the injector's data-in port, plug the cable run to the powered device into the data+power port, and the injector adds the power to the line. This allows a single device to be powered over PoE without replacing the entire switch.

### PoE Budget

A PoE switch has a total power budget — the maximum combined wattage it can deliver across all PoE ports simultaneously. If the sum of all connected device power draws exceeds the switch's budget, some ports will not receive power. Technicians must calculate the total PoE draw of all planned devices and verify it fits within the switch's specified power budget before deployment.

---

## Section 6 — Certification Exam Tips

The following are the eight most commonly tested traps on the CompTIA A+ Core 1 exam for this module.

**Exam Trap 1 — Switch does NOT assign IP addresses:**
IP address assignment is a DHCP function. DHCP runs on the router, on a dedicated DHCP server, or sometimes on a WAP. A switch forwards frames at Layer 2 using MAC addresses only. If a user cannot get an IP address, the problem is not the switch unless the switch has a misconfigured VLAN blocking DHCP discovery packets.

**Exam Trap 2 — Hub floods all ports; switch does not:**
A hub repeats every signal to every port — all devices share bandwidth and all see all traffic. A switch sends traffic only to the specific destination port. If a question describes a device where "all connected computers slow down when anyone on the network transfers a large file," the answer is hub, not switch.

**Exam Trap 3 — Home wireless router = three devices in one:**
A home gateway device combines a router, a multi-port switch, and a WAP into one physical unit. The exam may ask which function a "wireless router" provides when a client gets an IP address — the answer is router (DHCP/NAT), not WAP. The WAP function is radio access, not IP addressing.

**Exam Trap 4 — PoE wattage values are memorized facts:**
The exam asks for the specific wattage values. 802.3af = 15.4 W. 802.3at = 30 W. 802.3bt = 60–100 W. If a WAP requires 25 W, only 802.3at or 802.3bt can supply it — 802.3af at 15.4 W is insufficient.

**Exam Trap 5 — Patch panel is passive:**
The patch panel has no processor, no power supply, and no MAC address table. It is never the answer to a connectivity problem that requires an active device function. If a question asks which device "learns MAC addresses and forwards frames," the answer is switch, never patch panel.

**Exam Trap 6 — Firewall sits between LAN and WAN:**
The firewall is positioned at the network perimeter, typically between the router's WAN port and the ISP connection, or between the router and the core switch. It inspects and filters traffic crossing the LAN-WAN boundary. A firewall placed inside the LAN between two internal switches provides internal segmentation security, which is a separate (advanced) use case.

**Exam Trap 7 — WAP does not route; it bridges:**
A WAP is a Layer 2 bridge between the wireless medium and the wired Ethernet uplink. It does not route between networks, does not perform NAT, and does not assign IP addresses unless it includes a built-in DHCP server (a combined device feature, not a standard WAP feature).

**Exam Trap 8 — Modem is the ISP boundary device:**
The modem is the demarcation point. The ISP provides and supports the modem and everything on its WAN side. The customer owns everything on the LAN side. If a question asks which device "converts DOCSIS cable signal to Ethernet," the answer is cable modem — not router, not switch.

---

## Section 7 — Network Device Placement Diagram

For reference, here is the standard device placement order from ISP to end device:

ISP physical medium (coaxial/fiber/phone line)
→ Modem (signal conversion — ISP medium to Ethernet)
→ Firewall (traffic inspection and policy enforcement)
→ Router (Layer 3 routing, DHCP, NAT)
→ Core switch (Layer 2 LAN forwarding)
→ Patch panel (passive termination of horizontal runs)
→ Horizontal cable run through wall
→ Wall jack (keystone jack)
→ Short patch cable
→ End device (PC, IP phone, printer)

WAPs connect to switch ports and bridge wireless clients into the wired LAN at Layer 2.

---

## Section 8 — Study Checklist

- Memorize the OSI layer for each device: hub = Layer 1, switch = Layer 2, router = Layer 3.
- Know the PoE wattage values: 15.4 W (802.3af), 30 W (802.3at), 60–100 W (802.3bt).
- Be able to explain what a patch panel does and does not do.
- Know the difference between a standalone WAP and the WAP function inside a home wireless router.
- Understand that a switch does not assign IP addresses — DHCP does.
- Review the eight Exam Trap items in Section 6 carefully.
- Complete Lab 12 and submit deliverables to Canvas.
- Complete Quiz 12 after the lab.
- Post your initial Discussion 12 response by Wednesday at 11:59 PM.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 (220-1101) Study Notes — Network Infrastructure Devices section: professormesser.com
- CompTIA A+ Certification Exam Objectives (220-1101) — available at comptia.org

---

## 9. Supplemental Resources

The following free resources supplement Module 12 content on network infrastructure devices, switching, routing, and wireless access points.

1. **Professor Messer — CompTIA A+ Core 1 (220-1101) Network Infrastructure Devices**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video lectures covering hubs, switches, routers, access points, firewalls, patch panels, and PoE standards aligned to Domain 2.2. Professor Messer's OSI layer association mnemonics are particularly useful for the device classification questions that appear on the A+ exam.

1. **Cisco Networking Academy — Packet Tracer Free Simulation Software**
   URL: [https://www.netacad.com/courses/packet-tracer](https://www.netacad.com/courses/packet-tracer)
   Relevance: Cisco's free network simulation tool allows students to build virtual networks with routers, switches, access points, and end devices. Hands-on practice building the rack topology from Lab 12 (modem → firewall → router → switch → patch panel) in Packet Tracer reinforces device role understanding without requiring physical hardware.

1. **GNS3 — Free Open-Source Network Simulator**
   URL: [https://www.gns3.com/](https://www.gns3.com/)
   Relevance: GNS3 is a free, open-source network emulator used by professionals and students to simulate real router and switch operating systems. Unlike Packet Tracer, GNS3 supports importing actual Cisco IOS, Juniper JunOS, and other vendor firmware images for high-fidelity simulation. Useful for exploring VLAN configuration, inter-VLAN routing, and managed switch features covered in Module 12.

1. **Wireshark — Free Network Packet Analyzer**
   URL: [https://www.wireshark.org/](https://www.wireshark.org/)
   Relevance: Wireshark is the industry-standard free packet capture and analysis tool. Using Wireshark to capture ARP broadcasts, DHCP transactions, and ICMP ping packets on a real or simulated network provides hands-on context for understanding how switches, routers, and DHCP servers interact — directly reinforcing the network infrastructure concepts in this module.

1. **Subnet-Calculator.com — Free IPv4 Subnet Calculator**
   URL: [https://www.subnet-calculator.com/](https://www.subnet-calculator.com/)
   Relevance: Free browser-based tool for calculating subnet masks, network addresses, broadcast addresses, and host ranges. Understanding subnetting is a prerequisite for router configuration and VLAN design, both of which are core topics in Module 12 and on the A+ Core 1 exam.
