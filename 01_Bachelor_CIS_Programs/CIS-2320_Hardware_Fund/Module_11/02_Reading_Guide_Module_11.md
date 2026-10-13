# Reading Guide: Module 11 - Network Hardware & Connectors

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
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.1, Domain 2.2
**Texas Wesleyan University | Professor Nash**

---

## Introduction

Welcome to Module 11 — Network Hardware and Connectors. This module covers the physical layer of networking: the cables, connectors, and wiring standards that carry data between every device in a building. You will learn the differences between Ethernet cable categories, how to identify RJ-45 and RJ-11 connectors by sight and by specification, the three fiber optic connector types used in enterprise environments, and the T568A and T568B wiring standards used when terminating patch cables.

These topics appear on the CompTIA A+ Core 1 (220-1101) exam under Domains 2.1 and 2.2. As a working technician you must select the correct cable category for a given speed and distance requirement, identify connectors from a photograph or physical sample, and terminate an RJ-45 plug to the correct pinout. Master these concepts before the lab.

---

## Section 1 — Copper Twisted-Pair Cable Categories

### Overview

Twisted-pair copper cable is the foundation of every modern office Ethernet installation. The cables consist of four pairs of conductors, each pair twisted around each other at a specific rate. The twist reduces electromagnetic interference (EMI) and crosstalk between adjacent pairs. Cable categories are defined by TIA/EIA-568 and specify the conductor gauge, twist rate, and maximum frequency each cable can carry, which determines the achievable data rate and maximum distance.

### Cable Category Specification Table

| Category | Max Speed | Max Distance at Max Speed | Typical Use Case |
|----------|-----------|--------------------------|-----------------|
| Cat3 | 10 Mbps | 100 m | Legacy phone wiring; obsolete for Ethernet |
| Cat5 | 100 Mbps | 100 m | Legacy; no longer installed |
| Cat5e | 1 Gbps | 100 m | Older office installations; minimum standard |
| Cat6 | 1 Gbps / 10 Gbps | 100 m / 55 m | New construction standard; common today |
| Cat6a | 10 Gbps | 100 m | High-performance runs; 10GbE full distance |
| Cat7 | 10 Gbps | 100 m | Shielded; niche/proprietary — not on A+ exam |
| Cat8 | 25–40 Gbps | 30 m | Data center top-of-rack; not on A+ exam |

### Cat5e Detail

Category 5 Enhanced (Cat5e) was the dominant standard from approximately 2000 through 2010. It supports Gigabit Ethernet (1000BASE-T) at up to 100 meters, which satisfies the TIA-568 maximum horizontal run length for structured cabling. Cat5e improved on Cat5 by requiring tighter pair-twist specifications to reduce crosstalk and support Gigabit speeds. It uses 24 AWG conductors. Existing Cat5e installations are still widely found and are functional for 1 Gbps networks.

### Cat6 Detail

Category 6 supports 1 Gbps at 100 meters and extends 10 Gbps support up to 55 meters. The internal construction includes tighter pair twisting than Cat5e and often an internal plastic spline (cross-filler) that physically separates the four pairs to reduce alien crosstalk. Cat6 cable is slightly larger in diameter than Cat5e due to its thicker insulation. The 55-meter limit for 10 Gbps is the single most tested A+ fact about Cat6 — an 80-meter Cat6 run will only support 1 Gbps to a 10GbE switch.

### Cat6a Detail

Category 6 Augmented (Cat6a) is the solution when 10 Gbps is required at the full 100-meter horizontal run. It achieves this through significantly more robust shielding — either F/UTP (foil over the entire bundle) or S/FTP (foil over each individual pair plus an outer braid). Cat6a is physically larger, heavier, and less flexible than Cat6, requiring larger conduit and more careful bend-radius management during installation. Its thicker construction also requires keystone jacks and patch panel ports rated for Cat6a. All three categories (Cat5e, Cat6, Cat6a) use the same RJ-45 connector.

### Shielded vs Unshielded

Unshielded Twisted Pair (UTP) is the most common type in North American office environments — no metallic shielding around the pairs or the overall bundle. Shielded Twisted Pair (STP or F/UTP) adds foil or braid shielding and is used in high-EMI environments such as factory floors, medical equipment areas, and high-density wireless AP deployments. Shielded cable requires proper grounding at both ends; improper grounding of shielded cable can actually increase noise rather than reduce it.

---

## Section 2 — RJ-45 and RJ-11 Connector Identification

### RJ-45 (8P8C)

The RJ-45 connector is an 8-position, 8-contact (8P8C) modular plug and the universal connector for Ethernet twisted-pair cable. Physical characteristics:

- Width: approximately 11.7 mm
- Height: approximately 5.7 mm
- Eight gold-plated IDC (insulation displacement contact) pins visible from the front
- Retaining tab on the underside that clicks into a port latch
- Used with: Cat5e, Cat6, Cat6a patch cables; NIC ports; switch ports; patch panels; wall jacks

### RJ-11 (6P2C)

The RJ-11 connector is a 6-position, 2-contact modular plug used for analog telephone lines and some DSL connections. Physical characteristics:

- Width: approximately 9.6 mm (narrower than RJ-45)
- Height: approximately 5.5 mm
- Typically only 2 center pins are used (positions 3 and 4 of the 6-position housing)
- Used with: telephone handsets, landline wall jacks, analog modem cables, DSL connections

### Identification Table

| Feature | RJ-45 | RJ-11 |
|---------|-------|-------|
| Pin count | 8 (8P8C) | 2 active (6P2C) |
| Width | ~11.7 mm | ~9.6 mm |
| Application | Ethernet data | Telephone / DSL |
| Compatible port | NIC, switch, wall data jack | Phone, DSL modem |
| Fits in other port? | RJ-45 plug will NOT fit in RJ-11 socket | RJ-11 plug WILL fit (loosely) in RJ-45 socket |

### Field Trap

An RJ-11 plug inserted into an RJ-45 socket makes partial physical contact but establishes no valid data connection. In buildings where phone and data wall jacks share the same wall plate or look identical, this swap is a common installation mistake. The technician symptom is "no network connection" from a device that appears physically connected. The fix is to verify the jack type and move to the correct port.

---

## Section 3 — Fiber Optic Connector Types

### Why Fiber Optic Cable

Fiber optic cable transmits data as pulses of light through a glass or plastic core, providing immunity to electromagnetic interference, support for much greater distances than copper, and in the case of single-mode fiber, bandwidth that can reach hundreds of terabits per second with wavelength division multiplexing. For the A+ exam you need to know the three primary connector types and when each is used.

### Connector Type Comparison Table

| Connector | Coupling Mechanism | Body Shape | Size | Typical Use |
|-----------|--------------------|------------|------|-------------|
| ST (Straight Tip) | Bayonet twist-lock | Round | Medium | Legacy campus/enterprise wiring |
| SC (Subscriber Connector) | Push-pull latch | Square/rectangular | Medium | Data center patch panels; ISP installations |
| LC (Lucent Connector) | Push-pull latch | Small rectangular | Small (half of SC) | Modern enterprise; SFP transceivers |

### ST — Straight Tip

ST connectors are identified by their round, cylindrical body and the bayonet-style coupling mechanism — insert and twist to lock, like a BNC connector. The ceramic ferrule tip protrudes from the center of the connector. ST was common in enterprise campus wiring from the mid-1990s through mid-2000s and is still found in older buildings. It is considered a legacy connector and is not deployed in new installations.

### SC — Subscriber Connector

SC connectors have a square body and use a push-pull mechanism — insert straight in until it clicks, pull straight back to remove. SC is widely used in fiber-to-the-premises ISP installations, older data center patch panels, and telecom equipment. Duplex SC (two fibers bonded side by side) is the standard for most two-fiber connections in legacy enterprise environments. The square body makes it easy to identify in photographs.

### LC — Lucent Connector

LC connectors are the standard in modern enterprise networking and data centers. They use the same push-pull latch concept as SC but are roughly half the physical size, enabling much higher port density in patch panels and transceivers. LC is the connector used on SFP (Small Form-factor Pluggable) and SFP+ modules inserted into switch and router fiber ports. Duplex LC uses two LC connectors joined side by side. When you purchase a fiber patch cable for a modern switch or server, it will almost certainly have LC connectors.

### Single-Mode vs Multimode

The fiber type affects distance capability:

- Multimode fiber (MMF) has a larger core (50 or 62.5 microns) that allows multiple light paths. It is used for shorter distances within a building — typically up to 300–550 meters at 10 Gbps depending on the fiber grade. Multimode cable is often identified by its orange or aqua jacket.
- Single-mode fiber (SMF) has a much smaller core (9 microns) that allows only one light path, dramatically reducing attenuation over long distances. Single-mode supports runs of kilometers and is used for inter-building and WAN connections. Single-mode cable is identified by its yellow jacket.

For any A+ scenario involving distances over 100 meters requiring fiber, single-mode is the appropriate choice.

---

## Section 4 — T568A and T568B Wiring Standards

### Wiring Standard Overview

T568A and T568B are the two wiring sequences defined by TIA/EIA-568 for terminating all eight conductors of a twisted-pair cable into an RJ-45 plug or keystone jack. Both standards support the same electrical performance — the difference is purely the position of the orange and green pairs.

### Pin-Out Reference Table

| Pin | T568A Color | T568B Color |
|-----|-------------|-------------|
| 1 | White/Green | White/Orange |
| 2 | Green | Orange |
| 3 | White/Orange | White/Green |
| 4 | Blue | Blue |
| 5 | White/Blue | White/Blue |
| 6 | Orange | Green |
| 7 | White/Brown | White/Brown |
| 8 | Brown | Brown |

Pins 4, 5, 7, and 8 (blue and brown pairs) are in identical positions in both standards. Only pins 1, 2, 3, and 6 differ — the orange and green pairs are swapped.

### Straight-Through Cable

A straight-through cable uses the same wiring standard on both ends — T568B to T568B is the most common in North America. Straight-through cables connect dissimilar devices: PC to switch, switch to router's LAN port, PC to patch panel port. The transmit pins of one device align with the receive pins of the other device by design.

### Crossover Cable

A crossover cable uses T568A on one end and T568B on the other. This swaps the transmit and receive pairs so that two identical devices can communicate directly without a switch. Use cases include PC to PC, switch to switch (uplink without auto-MDI/MDIX), and router to router. Modern switches implement auto-MDI/MDIX, which automatically detects the cable type and adjusts the port's internal wiring electronically. This makes crossover cables largely unnecessary in current enterprise environments. However, the A+ exam still tests the concept.

### Cable Type Summary

| Connection Type | Cable Type | Standard |
|-----------------|-----------|----------|
| PC to switch | Straight-through | T568B — T568B |
| PC to PC (direct) | Crossover | T568A — T568B |
| Switch to switch (no auto-MDI/MDIX) | Crossover | T568A — T568B |
| PC to router LAN port | Straight-through | T568B — T568B |
| Router WAN to modem | Straight-through | T568B — T568B |

---

## Section 5 — Certification Exam Tips

The following are the eight most commonly tested traps on the CompTIA A+ Core 1 exam for this module.

**Exam Trap 1 — Cat6 at 10 Gbps distance limit:**
Cat6 supports 10 Gbps only up to 55 meters. Any scenario describing a run longer than 55 meters that requires 10 Gbps requires Cat6a. If the question offers both Cat6 and Cat6a as answers, identify the cable run distance first.

**Exam Trap 2 — Cat5e cannot be upgraded in software:**
Cable categories are physical hardware standards. Cat5e cannot be configured, patched, or upgraded to support higher speeds. The physical conductors, twist rates, and insulation determine the performance ceiling.

**Exam Trap 3 — RJ-11 in RJ-45 port:**
An RJ-11 plug fits physically into an RJ-45 socket but creates no valid data connection. The symptom is no network connectivity from a device that appears plugged in. Check the jack type and connector type before troubleshooting further.

**Exam Trap 4 — Crossover vs straight-through:**
PC to switch = straight-through (T568B both ends). PC to PC without a switch = crossover (T568A one end, T568B other). The exam tests this by describing a direct connection between two similar devices and asking which cable to use.

**Exam Trap 5 — ST connector is legacy:**
ST connectors are legacy and found in older enterprise installations. New installations use LC. If a scenario describes a modern data center or SFP transceiver, the answer will involve LC connectors, not ST.

**Exam Trap 6 — Single-mode for long distances:**
Multimode fiber is for short runs inside a building. Single-mode is for long runs between buildings or across a campus. Any scenario with a distance over 300–400 meters should point you toward single-mode fiber.

**Exam Trap 7 — All Cat cables use RJ-45:**
Cat5e, Cat6, and Cat6a all terminate with the same RJ-45 connector. The connector does not change between categories. A question that implies different connectors for different categories is incorrect.

**Exam Trap 8 — PoE uses all four pairs:**
When Power over Ethernet is discussed in cable context, know that both PoE (IEEE 802.3af) and PoE+ (802.3at) use the spare pairs or all pairs for power delivery. A cable that passes all eight pins on a cable tester is a PoE-capable cable regardless of category (as long as it meets the minimum Cat5e specification).

---

## Section 6 — Additional Technical Detail: Cable Construction

### UTP Conductor Color Coding

All four twisted pairs in a UTP Ethernet cable follow a standard color convention:

- Pair 1: Blue / White-Blue
- Pair 2: Orange / White-Orange
- Pair 3: Green / White-Green
- Pair 4: Brown / White-Brown

The solid-colored wire and its white-with-stripe partner always travel together as a pair. The pair twist rates differ across the four pairs to minimize crosstalk between pairs — this is why the pairs must be kept twisted as close to the RJ-45 termination point as possible during crimping.

### Plenum vs Riser vs PVC Jacket Ratings

| Rating | Fire Resistance | Installation Location |
|--------|-----------------|----------------------|
| PVC (CMR) | Standard | Between floors in conduit |
| Riser (CMR) | Retards vertical flame spread | Vertical runs between floors |
| Plenum (CMP) | Low-smoke, self-extinguishing | Above-ceiling air-handling spaces |

Plenum-rated cable is required by fire code in air-handling spaces (the space above a drop ceiling used as an air return). Plenum cable costs significantly more than PVC. The exam may present a scenario where cable must be run through an air-handling plenum — the correct answer is always plenum-rated cable, not standard PVC.

---

## Section 7 — Study Checklist

- Review all glossary terms and the specification tables in Sections 1 through 4.
- Memorize the Cat6 55-meter 10 Gbps limit — write it down three times.
- Draw the T568A and T568B pin-out tables from memory and verify against the table in Section 4.
- Know ST vs SC vs LC by shape, coupling mechanism, and era of use.
- Distinguish single-mode (yellow jacket, long distance) from multimode (orange/aqua, short distance).
- Read the eight Exam Trap items in Section 5 carefully.
- Review the Lab 11 document before beginning.
- Complete Lab 11 and submit deliverables to Canvas.
- Complete Quiz 11 after the lab.
- Post your initial Discussion 11 response by Wednesday at 11:59 PM.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 (220-1101) Study Notes — Network Cabling and Connector sections: professormesser.com
- CompTIA A+ Certification Exam Objectives (220-1101) — available at comptia.org
- TIA/EIA-568 Structured Cabling Standard — available through your institution's library

---

## 9. Supplemental Resources

The following free resources supplement Module 11 content on network cabling, connectors, and switching hardware.

1. **Professor Messer — CompTIA A+ Core 1 (220-1101) Network Cables and Connectors**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video lectures covering copper cable categories (Cat5 through Cat8), fiber optic types (single-mode vs. multimode), T568A/T568B wiring standards, and network connector identification — all primary exam objectives for Domain 2.1 and 2.2.

1. **Fluke Networks — Cable Testing Learning Center**
   URL: [https://www.flukenetworks.com/learning-center](https://www.flukenetworks.com/learning-center)
   Relevance: Free educational articles from the leading manufacturer of professional cable testers. Covers wire map testing, pair skew, attenuation, NEXT (near-end crosstalk), and how to interpret cable test results — directly supporting the cable troubleshooting skills tested in Lab 11 and on the A+ exam.

1. **Cisco Networking Academy — Introduction to Networks (Free Preview Chapters)**
   URL: [https://www.netacad.com/courses/networking/ccna-introduction-networks](https://www.netacad.com/courses/networking/ccna-introduction-networks)
   Relevance: Cisco's free Introduction to Networks course covers Ethernet standards, copper and fiber cabling, switches, and the OSI model at a level that directly reinforces A+ Core 1 Domain 2 networking objectives. The interactive cable and connector identification activities are particularly useful for exam preparation.

1. **The Fiber Optic Association (FOA) — Free Online Reference Guide**
   URL: [https://www.thefoa.org/tech/ref/index.html](https://www.thefoa.org/tech/ref/index.html)
   Relevance: The FOA publishes a free comprehensive reference covering fiber optic cable types (single-mode, multimode OM1–OM5), connector types (ST, SC, LC, MTP), installation standards, and testing procedures. Authoritative and free; directly supports the fiber connector identification content in Module 11.

1. **IEEE 802.3 Standard Summary — Ethernet Working Group**
   URL: [https://www.ieee802.org/3/](https://www.ieee802.org/3/)
   Relevance: The official IEEE 802.3 working group page provides free access to standard summaries and amendment descriptions for all Ethernet variants (1000BASE-T, 10GBASE-T, PoE/802.3af/at/bt). Understanding which amendment introduced which standard clarifies the A+ exam questions about cable category requirements for specific Ethernet speeds.
