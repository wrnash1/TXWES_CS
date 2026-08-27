# Reading Guide: Module 13 - Laptop Components and Disassembly

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 1.3
**Texas Wesleyan University | Professor Nash**

---

## Introduction

Welcome to Module 13 — Laptop Components and Disassembly. This module covers the hardware components unique to portable computers and the safe service procedures required to access and replace them. Laptop repair differs fundamentally from desktop work: components are proprietary, space-constrained, and connected by fragile flex cables rather than standard card-slot connectors. The wrong technique can snap a ZIF lock bar, tear an antenna cable, or crack an LCD panel.

These topics appear on the CompTIA A+ Core 1 (220-1101) exam under Domain 1.3. As a technician, you must know the correct disassembly order, the safety rules governing each step, and how to identify the failing component from a described symptom. Master all sections of this guide before the lab.

---

## Section 1 — ESD Safety and Pre-Service Procedures

### Electrostatic Discharge Principles

Electrostatic discharge (ESD) occurs when a static charge built up on a person or surface discharges rapidly through a sensitive component. The threshold for ESD damage to laptop components is far below what a human can feel — a discharge of 3,000 volts is perceptible to a person, but CMOS damage can occur at as low as 100 volts. Laptop motherboards, RAM, and Wi-Fi cards are particularly susceptible because of their small die size and thin oxide layers.

ESD protection measures for laptop service:

- Wear an ESD wrist strap connected to an unpainted metal surface or a proper ground point.
- Work on an ESD mat connected to the same ground.
- Remove the battery before handling any internal component.
- Keep replacement components in their anti-static bags until the moment of installation.
- Do not touch the gold contact edges of RAM modules or M.2 cards.

### Mandatory Pre-Service Checklist

Before opening any laptop for internal service, in this exact order:

1. Save and back up any critical data on the device.
2. Power off the laptop completely — not sleep, not hibernate, fully powered off.
3. Unplug the AC adapter from the wall and from the laptop.
4. Remove or disconnect the battery (details by type in Section 2).
5. Press and hold the power button for 5 seconds to discharge residual capacitor energy.
6. Put on an ESD wrist strap and connect it to a grounded surface.
7. Gather all required tools before opening the case.

---

## Section 2 — Battery Types and Removal

### Removable Battery

A removable battery is mounted in an external bay on the underside of the laptop and is accessible without any tools. Identification: look for a battery-shaped compartment with one or two sliding latches, often marked with a lock/unlock icon. Removal: slide the latch(es) to the release position and lift the battery free. Common in older consumer laptops (pre-2015), ruggedized laptops, and some business-class models.

### Integrated Battery

An integrated battery is mounted inside the chassis beneath the bottom panel. Identification: the laptop has no external battery bay or latch — the underside is a single smooth panel with screws. Removal: remove all bottom panel screws, lift the panel with a spudger or plastic pry tool, locate the battery connector (a small rectangular multi-wire JST connector), and disconnect it from the motherboard socket by prying the connector body upward with a spudger. Do not pull the wires. Common in all modern thin and ultrabook-style laptops.

### Battery Safety Notes

Lithium-ion batteries can expand, leak, or ignite if punctured or shorted. Never pierce a battery with a screwdriver. Never apply direct heat to a battery. If a battery is visibly swollen (the laptop case is bowing or the battery won't sit flat), handle it with extra care — a swollen battery indicates internal gas pressure from cell degradation and should be disposed of through proper e-waste channels, not thrown in standard trash.

---

## Section 3 — Wi-Fi Card, RAM, and M.2 Storage

### Wi-Fi Card Detail

Most laptop Wi-Fi cards are M.2 2230 form factor (modern laptops) or legacy Mini-PCIe half-height cards. The card seats in a dedicated slot and is held by one Phillips screw. The distinguishing feature of a laptop Wi-Fi card compared to any other M.2 device is the antenna cables.

### Antenna Cable Connector Types and Procedure

| Feature | Description |
|---------|-------------|
| Connector type | MHF4 (Micro Hirose Flat 4) snap-on coaxial connector |
| Connector diameter | Approximately 1.5 mm |
| Cable colors | Typically white (main) and black (auxiliary); sometimes gray as third |
| Routing path | From Wi-Fi card → through hinge → through lid → antenna film in bezel |
| Removal method | Pry connector body straight up with non-conductive spudger |
| Installation method | Press connector straight down until faint click confirms seating |

Critical rule: never pull the antenna cable to remove the connector. The cable is ultra-thin coaxial — the outer braid can separate from the connector at the cable-to-connector junction if pulled. Always pry the connector body itself.

### Laptop RAM — SO-DIMM Form Factor

| Feature | SO-DIMM (Laptop) | DIMM (Desktop) |
|---------|-----------------|----------------|
| Physical length | ~67 mm (DDR4) | ~133 mm (DDR4) |
| Pin count | 260 pins (DDR4) | 288 pins (DDR4) |
| Slot angle | 30–45 degrees during insertion | Vertical |
| Release mechanism | Spring clips on sides | Locking tabs on ends |
| Speeds | Same as desktop (same DDR generation) | Same as laptop |

A SO-DIMM is electrically identical to a desktop DIMM of the same generation and speed — it is only the physical form factor that differs. A DDR4-3200 SO-DIMM and a DDR4-3200 DIMM run at the same speed; they simply use different physical slots.

Increasingly, modern laptops (especially thin ultrabooks) have RAM soldered directly to the motherboard in BGA (Ball Grid Array) packages. Soldered RAM cannot be upgraded or replaced — the service manual will specify whether RAM is removable or soldered. Always verify before purchasing upgrade memory.

### M.2 Storage

M.2 storage cards use the same single-screw removal procedure as a Wi-Fi card. M.2 slots have different keying:

| M.2 Key | Supported Protocols | Common Use |
|---------|-------------------|-----------|
| B key | SATA, USB | Older SATA SSDs, some modems |
| M key | NVMe (PCIe), SATA | High-speed NVMe SSDs |
| B+M key | Both SATA and NVMe | Universal slots on many laptops |

The M.2 card length (2230, 2242, 2260, 2280) must also match the slot length. The most common laptop NVMe SSD is 2280 (22 mm wide × 80 mm long). Before purchasing a replacement, confirm both the key type and the supported length from the service manual.

---

## Section 4 — Display Assembly and Video Cables

### Display Assembly Components

| Component | Description |
|-----------|-------------|
| LCD panel | The glass display element — the part that actually shows the image |
| Backlight | LED (modern) or CCFL (legacy) — provides illumination behind the LCD |
| Digitizer | Touchscreen glass layer bonded over the LCD on touchscreen models |
| Bezel | Plastic frame surrounding the display; held by screws under rubber plugs and by plastic clips |
| Hinges | Metal hinges attaching the lid to the palm rest; screwed to both lid frame and base chassis |
| Video cable | LVDS (older) or eDP (modern) flat flex cable connecting motherboard to panel |

### CCFL vs LED Backlight

| Feature | CCFL | LED |
|---------|------|-----|
| Era | Pre-2012 approximately | 2010-present (now universal) |
| Inverter board required | Yes — CCFL requires high-voltage AC inverter | No |
| Failure symptom | Dim screen, pink tint, backlight flicker | Single dead LEDs or entire backlight off |
| Replacement complexity | More complex — inverter and CCFL tube both potential failure points | Simpler — LED strips or full panel replacement |

### LVDS vs eDP Video Cable

| Feature | LVDS | eDP |
|---------|------|-----|
| Full name | Low Voltage Differential Signaling | Embedded DisplayPort |
| Era | Pre-2013 approximately | 2012-present (now standard) |
| Connector type | Multi-pin flat ribbon with individual contacts | Thin flat flex, smaller connector |
| Max resolution | Limited to approximately 1920×1200 | Supports 4K and above |
| Tested on A+ | Yes — know the name and era | Yes — know the name and era |

### LCD Replacement Procedure Summary

1. Remove rubber plugs from bezel screw holes (typically 4–6 screws around the perimeter).
2. Remove bezel screws.
3. Pry bezel away from lid frame using a spudger, working clockwise from a corner.
4. Remove panel-to-lid-frame retaining screws (typically 2–4 brackets).
5. Carefully tilt the panel forward and disconnect the video cable (LVDS or eDP).
6. On touchscreen models, also disconnect the digitizer flex cable.
7. Install replacement panel in reverse order.
8. Power on and verify display function before closing bezel.

---

## Section 5 — ZIF Connectors and Keyboard Replacement

### ZIF Connector Operation

ZIF (Zero Insertion Force) connectors are used throughout laptops for flat flex cables. The connector body contains a locking bar that rotates 90 degrees:

- Lock bar down (closed): cable is clamped in place; do not attempt to remove cable
- Lock bar up (open): cable slides freely in and out with no resistance

The locking bar is typically 1–2 mm tall and hinges at the back of the connector. It is lifted with a spudger tip or fingernail. Forcing a cable out while the lock is down is the single most common cause of ZIF connector damage in laptop repair. A broken ZIF lock requires soldering a new connector to the motherboard — an advanced repair.

### Keyboard Removal by Retention Method

| Retention Method | How to Identify | Removal Approach |
|-----------------|-----------------|-----------------|
| Top-clip retention | Clips along top edge of keyboard (older consumer laptops) | Press clips with spudger; keyboard lifts slightly from top |
| Bottom-panel screws | Screws on underside labeled with keyboard icon | Remove bottom panel, remove labeled screws, keyboard lifts from top |
| Combination | Screws plus clips | Remove bottom panel screws first, then release clips |

After keyboard is lifted, the ZIF connector on the motherboard is exposed. Flip the lock bar up, slide the flex cable out, and the keyboard is free.

---

## Section 6 — DC Power Jack Failure

### DC Power Jack Construction

The DC power jack (barrel jack) is the port where the laptop's AC adapter connects. Construction varies:

- Motherboard-mounted: the jack is soldered directly to the motherboard. Replacement requires removing the motherboard and desoldering/resoldering the jack — the most invasive repair.
- Daughter board mounted: the jack is on a small sub-board connected to the motherboard via a short cable. Replacement requires disconnecting the cable and swapping the sub-board — significantly simpler than motherboard desoldering.

### Symptom Identification Table

| Symptom | Most Likely Component |
|---------|----------------------|
| Charges only when cable held at specific angle | DC power jack (broken solder joint or cracked housing) |
| Consistently does not charge on any adapter | AC adapter failure (test with known-good adapter first) or battery BMS failure |
| Charges sometimes, not others, not angle-dependent | Adapter cable strain relief failure or intermittent internal adapter fault |
| Battery drains even when plugged in | Battery cell capacity depletion (old battery) or power jack delivering intermittent contact |
| Laptop only works when plugged in, dies instantly on battery | Battery completely dead — cells depleted, not holding charge |

The A+ exam specifically tests the angle-dependent charging symptom as the distinguishing factor for DC power jack failure.

---

## Section 7 — Certification Exam Tips

The following are the eight most commonly tested traps on the CompTIA A+ Core 1 exam for this module.

**Exam Trap 1 — Battery removal is always Step 1:**
Every A+ laptop service scenario starts with removing or disconnecting the battery. This is the single most frequently tested fact in Domain 1.3. The correct first step before replacing keyboard, RAM, Wi-Fi card, or any other internal component is: disconnect the battery.

**Exam Trap 2 — Antenna connectors are pried, not pulled:**
MHF4 antenna connectors must be pried off with a spudger. Pulling the cable breaks the connector or separates the cable from its connector body. Any question describing the correct technique for removing antenna cables from a Wi-Fi card should point to spudger/pry — not "grip and pull."

**Exam Trap 3 — ZIF lock must be open before removing cable:**
A flex cable cannot be removed from a ZIF connector while the lock bar is closed. The lock bar must be flipped to the open position first. Forcing the cable while locked breaks the lock bar. The A+ exam may describe a technician unable to remove a keyboard cable and ask what step was missed.

**Exam Trap 4 — Angle-dependent charging = DC power jack:**
Consistent no-charge = test the AC adapter. Angle-dependent intermittent charging = DC power jack failure. The exam presents both symptoms and expects you to distinguish them.

**Exam Trap 5 — SO-DIMM is the laptop RAM form factor:**
Laptop RAM is SO-DIMM. Desktop RAM is DIMM. They run at the same speeds but cannot be physically interchanged. An A+ question asking which RAM form factor is used in a laptop always has SO-DIMM as the correct answer.

**Exam Trap 6 — CCFL requires an inverter board; LED does not:**
If a question describes an older laptop where the display is dim but the image is still visible (viewable with a flashlight), the failing component is the CCFL backlight or its inverter board. LED backlights fail differently — typically total backlight failure or individual dead zones, not the dim/pink presentation associated with CCFL aging.

**Exam Trap 7 — eDP is the modern video cable standard:**
LVDS is the older display cable (pre-2013). eDP is the modern standard. If a question describes a laptop manufactured recently and asks about its internal display cable type, eDP is the correct answer.

**Exam Trap 8 — Soldered RAM cannot be upgraded:**
Modern thin laptops often have RAM soldered to the motherboard. If a customer brings in a laptop and asks about a RAM upgrade, verify the service manual first. A soldered-RAM laptop cannot be upgraded — the only option is replacing the entire motherboard.

---

## Section 8 — Laptop Disassembly Order Reference

For most laptops, the general disassembly order is:

1. Power off, unplug AC adapter
2. Remove or disconnect battery
3. Discharge residual power (hold power button 5 seconds)
4. Remove bottom panel screws and lift panel
5. Access and remove: RAM, M.2 SSD, Wi-Fi card (from motherboard area)
6. Remove keyboard (screws accessible from bottom panel or top clips)
7. Remove palm rest (screws on bottom, clips along perimeter)
8. Access motherboard area: disconnect flex cables, ribbon connectors
9. Disconnect display cable from motherboard (routes through hinge)
10. Remove hinge screws to separate display assembly from base
11. Disassemble display assembly: bezel → panel → video cable

Always consult the specific service manual for the model being serviced. The order above is a general guide — individual models vary significantly.

---

## Section 9 — Study Checklist

- Know that battery removal is the mandatory first step — non-negotiable.
- Memorize the MHF4 antenna connector removal technique: pry the connector, never pull the cable.
- Know ZIF connector operation: lock bar up = open = cable slides out; lock bar down = locked.
- Know the DC power jack angle-dependent charging symptom.
- Know SO-DIMM vs DIMM: same speeds, different physical form factors, not interchangeable.
- Know CCFL (with inverter) vs LED backlight, and LVDS vs eDP video cable.
- Review the eight Exam Trap items in Section 7.
- Complete Lab 13 and submit deliverables to Canvas.
- Complete Quiz 13 after the lab.
- Post your initial Discussion 13 response by Wednesday at 11:59 PM.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 (220-1101) Study Notes — Laptop Hardware section: professormesser.com
- CompTIA A+ Certification Exam Objectives (220-1101) — available at comptia.org
- Manufacturer service manuals — available from the laptop manufacturer's support site

---

## 9. Supplemental Resources

The following free resources supplement Module 13 content on laptop component identification, disassembly procedures, and hardware diagnostics.

1. **Professor Messer — CompTIA A+ Core 1 (220-1101) Laptop Hardware**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video lectures covering SO-DIMM vs. DIMM, M.2 storage in laptops, display technologies (eDP, LVDS, CCFL, LED), battery replacement procedures, and ZIF connector handling — all primary exam objectives for Domain 1.3.

1. **iFixit — Free Laptop Repair Guides**
   URL: [https://www.ifixit.com/Device/Laptop](https://www.ifixit.com/Device/Laptop)
   Relevance: iFixit publishes free step-by-step laptop disassembly and repair guides for hundreds of laptop models, including photo documentation of ZIF connectors, battery connectors, MHF4 antenna connectors, and display cable routing. Reviewing a guide for a real laptop model reinforces the component identification and disassembly sequencing skills tested in this module and on the A+ exam.

1. **Crucial — Memory Advisor Tool (Free Compatibility Database)**
   URL: [https://www.crucial.com/store/advisor](https://www.crucial.com/store/advisor)
   Relevance: Crucial's free memory advisor tool identifies the correct SO-DIMM type, speed, and maximum capacity for specific laptop models. Using this tool for several laptop models provides hands-on practice with DDR4/DDR5 SO-DIMM specification lookup — a skill directly tested in A+ exam scenarios about laptop RAM compatibility.

1. **Battery University — How to Prolong Lithium-Based Batteries (Free Article)**
   URL: [https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries](https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries)
   Relevance: Battery University provides free, technically detailed articles on lithium-ion battery chemistry, capacity degradation by charge cycle count, storage voltage recommendations, and health assessment methods. This directly supports A+ exam questions about battery replacement indications and expected battery life behavior covered in Module 13.

1. **Panasonic Toughbook Service Manuals (Example of Free OEM Documentation)**
   URL: [https://pc-ap.panasonic.com/pages/support/servicesupport.html](https://pc-ap.panasonic.com/pages/support/servicesupport.html)
   Relevance: Many laptop manufacturers publish free service manuals and field service guides that document disassembly sequences, torque specifications, and component location diagrams. Reviewing an OEM service manual for any available laptop model demonstrates the professional documentation that technicians use in the field and reinforces the systematic disassembly approach emphasized in this module.
