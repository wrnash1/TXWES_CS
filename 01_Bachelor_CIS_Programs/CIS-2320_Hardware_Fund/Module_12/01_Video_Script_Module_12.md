# Video Script: Module 12 - Network Infrastructure Devices

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.2: Compare and contrast common networking hardware
**Estimated Duration:** 20-24 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course &bull; Module 12</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH" title="Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->


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

<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Network Infrastructure Devices &amp; Standard 19" Rack Architecture</text>

  <!-- OSI Device Hierarchy -->
  <g transform="translate(40, 95)">
    <rect width="420" height="325" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="210" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">OSI Device Layer Assignments</text>

    <!-- Layer 3 Router -->
    <rect x="20" y="40" width="380" height="80" fill="#0f172a" stroke="#ef4444" rx="4"/>
    <text x="35" y="60" fill="#ef4444" font-size="12" font-weight="bold">Layer 3: Network Layer Router / Firewall</text>
    <text x="35" y="78" fill="#f8fafc" font-size="10">• Addresses: Logical IP Addresses (IPv4/IPv6)</text>
    <text x="35" y="94" fill="#cbd5e1" font-size="10">• Function: Connects disparate networks; breaks broadcast domains</text>
    <text x="35" y="108" fill="#94a3b8" font-size="9">PDU: Packet | Protocol: OSPF, BGP, NAT</text>

    <!-- Layer 2 Switch -->
    <rect x="20" y="130" width="380" height="85" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="35" y="150" fill="#10b981" font-size="12" font-weight="bold">Layer 2: Data Link Layer Switch / WAP / Bridge</text>
    <text x="35" y="168" fill="#f8fafc" font-size="10">• Addresses: Physical MAC Addresses (48-bit EUI-48)</text>
    <text x="35" y="184" fill="#cbd5e1" font-size="10">• Function: Forwards frames via MAC Address Table; separates collision domains</text>
    <text x="35" y="200" fill="#94a3b8" font-size="9">PDU: Frame | Features: VLANs (802.1Q), PoE (802.3af/at/bt)</text>

    <!-- Layer 1 Hub -->
    <rect x="20" y="225" width="380" height="85" fill="#0f172a" stroke="#64748b" rx="4"/>
    <text x="35" y="245" fill="#94a3b8" font-size="12" font-weight="bold">Layer 1: Physical Layer Hub / Repeater / Patch Panel</text>
    <text x="35" y="263" fill="#f8fafc" font-size="10">• Signals: Electrical, Optical, or RF Bits</text>
    <text x="35" y="279" fill="#cbd5e1" font-size="10">• Function: Multi-port repeater; single collision &amp; broadcast domain</text>
    <text x="35" y="295" fill="#fca5a5" font-size="9">Legacy device — high collision rates. Replaced by switches.</text>
  </g>

  <!-- 19-inch Equipment Rack Layout -->
  <g transform="translate(480, 95)">
    <rect width="330" height="325" fill="#1e293b" stroke="#d9a74a" stroke-width="1.5" rx="6"/>
    <text x="165" y="24" fill="#d9a74a" font-size="13" font-weight="bold" text-anchor="middle">Standard 19" Rack Elevation (Top to Bottom)</text>

    <!-- Rack Posts -->
    <line x1="20" y1="40" x2="20" y2="310" stroke="#475569" stroke-width="4"/>
    <line x1="310" y1="40" x2="310" y2="310" stroke="#475569" stroke-width="4"/>

    <!-- Patch Panel -->
    <rect x="30" y="45" width="270" height="35" fill="#0f172a" stroke="#94a3b8" rx="2"/>
    <text x="165" y="67" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1U 24-Port Patch Panel (Structured Cable Punchdown)</text>

    <!-- Switch -->
    <rect x="30" y="90" width="270" height="35" fill="#0f172a" stroke="#10b981" rx="2"/>
    <text x="165" y="112" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">1U Managed Gigabit PoE+ Switch</text>

    <!-- Router / Firewall -->
    <rect x="30" y="135" width="270" height="35" fill="#0f172a" stroke="#ef4444" rx="2"/>
    <text x="165" y="157" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">1U Enterprise Next-Gen Firewall / Edge Router</text>

    <!-- Server -->
    <rect x="30" y="180" width="270" height="50" fill="#0f172a" stroke="#38bdf8" rx="2"/>
    <text x="165" y="210" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">2U Rackmount Server (Host / SAN)</text>

    <!-- UPS -->
    <rect x="30" y="240" width="270" height="60" fill="#0f172a" stroke="#f59e0b" rx="2"/>
    <text x="165" y="268" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">2U / 3U UPS Battery Backup</text>
    <text x="165" y="285" fill="#94a3b8" font-size="9" text-anchor="middle">Placed at lowest U for center of gravity stability</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ CompTIA A+ Key Principle: Always mount heavy UPS units at the rack bottom to prevent tipping hazards.</text>
</svg>
</div>

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
