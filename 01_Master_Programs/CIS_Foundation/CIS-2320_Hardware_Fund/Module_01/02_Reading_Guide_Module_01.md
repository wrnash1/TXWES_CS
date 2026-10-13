# Reading Guide: Module 01 — Introduction to PC Hardware & Safety

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


## Course: CIS-2320 Hardware Fundamentals

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3: Hardware

---

## Introduction

Before you touch a component, you must know three things: what it is, where it is, and how to handle it without destroying it. This module builds that foundation. Every subsequent module in CIS-2320 assumes you can identify components on sight and apply safe handling procedures automatically. The CompTIA A+ exam tests these skills directly — Domain 3 (Hardware) contains scenario questions that require you to recognize components from descriptions, choose correct connectors, and identify the right safety procedure for a given situation.

---

## 1. Internal PC Components

### Motherboard

The motherboard (also called the mainboard or system board) is the primary circuit board of the PC. Every other component either plugs into it directly or connects to it via cable. Key features:

- **CPU socket** — accepts the processor; socket type determines CPU compatibility
- **DIMM slots** — two or four slots for RAM modules; color-coded for dual-channel pairing
- **PCIe slots** — expansion slots for GPU, network cards, sound cards; x16 (long) and x1 (short)
- **M.2 slot** — small slot for NVMe SSDs; often under a metal heatsink cover
- **SATA ports** — L-shaped ports for connecting SATA data cables to storage drives
- **24-pin ATX power connector** — receives main power from the PSU
- **4-pin or 8-pin CPU power connector** — provides dedicated power to the CPU; located near the CPU socket
- **CMOS battery** — coin-cell battery (CR2032) that maintains BIOS/UEFI settings and the real-time clock when the system is powered off

### CPU (Central Processing Unit)

The CPU is the processor — the primary computation component. It sits in the CPU socket and is secured by a retention mechanism. Two socket types tested on the A+ exam:

| Socket Type | Pin Location | Example |
|---|---|---|
| LGA (Land Grid Array) | Pins in the socket | Intel (LGA1700, LGA1200) |
| PGA (Pin Grid Array) | Pins on the processor | AMD AM4 and earlier |
| LGA (Land Grid Array) | Pins in the socket | AMD AM5 (moved to LGA) |

**A+ exam note:** LGA sockets are more common on Intel platforms. Bending a pin in an LGA socket damages the motherboard (expensive). Bending a pin on a PGA processor damages the CPU (cheaper replacement). AM5 moved AMD to LGA as well.

The CPU is covered by a **heat sink** — a metal block with fins that conducts heat away from the processor — and a **CPU fan** that moves air across the fins. Thermal paste between the CPU and heat sink ensures proper heat transfer.

### RAM (Random Access Memory)

RAM is volatile working memory — it loses all data when power is removed. Modern desktop RAM uses the **DIMM** (Dual Inline Memory Module) form factor. Key facts:

- **DDR4** — current standard in most systems; 288-pin DIMM
- **DDR5** — newer standard; higher speeds, higher density; also 288-pin but keyed differently (not interchangeable with DDR4)
- **Dual-channel configuration** — install identical modules in matching-colored slots to double the memory bandwidth
- RAM slots are color-coded (e.g., slots 1 and 3 are one color, slots 2 and 4 are another) — consult the motherboard manual for correct dual-channel pairing

### PSU (Power Supply Unit)

The PSU converts AC power from the wall outlet to the DC voltages the PC components require. Key connectors:

| Connector | Pins | Purpose |
|---|---|---|
| 24-pin ATX | 24 | Main motherboard power |
| 4-pin or 8-pin CPU power | 4 or 8 (square) | CPU dedicated power |
| SATA power | 15-pin | Powers SATA drives |
| PCIe power | 6-pin or 8-pin | Powers discrete GPUs |
| Molex | 4-pin (legacy) | Older drives and fans |

**PSU wattage** must be sufficient for all components. A GPU-heavy gaming system may require 750W or more.

**Critical safety fact:** PSU capacitors retain lethal voltage for an extended period after the unit is unplugged. **Never open a PSU.** If it fails, replace the entire unit.

### Storage Drives

| Type | Technology | Speed | Moving Parts |
|---|---|---|---|
| HDD (Hard Disk Drive) | Magnetic platters | ~100–200 MB/s | Yes (spinning platters, read/write head) |
| SATA SSD | NAND flash, SATA interface | ~500–600 MB/s | No |
| NVMe SSD (M.2) | NAND flash, PCIe interface | ~3,000–7,000 MB/s | No |

SATA drives use two cables: a **SATA data cable** (thin, L-shaped, 7-pin) connecting to a SATA port on the motherboard, and a **SATA power cable** (wider, L-shaped, 15-pin) from the PSU.

M.2 NVMe SSDs connect directly to the M.2 slot — no cables required.

### GPU (Graphics Processing Unit)

The GPU handles display output and graphics rendering. A discrete GPU inserts into the **PCIe x16 slot** on the motherboard and is secured by a retention clip at the far end. On systems with integrated graphics (GPU built into the CPU), a discrete card may be absent.

**A+ scenario:** "PC powers on but shows no video." Checklist: monitor cable connected correctly → monitor set to correct input → discrete GPU fully seated in PCIe x16 slot → if integrated graphics disabled in BIOS, a discrete card is required.

---

## 2. Electrostatic Discharge (ESD)

### The Mechanism

Electrostatic discharge (ESD) is the sudden flow of static electricity between objects at different electrical potentials. When you walk across carpet and touch a doorknob, the spark you feel is ESD. The human body typically needs 3,000–4,000 volts before feeling a discharge. Computer chips can be damaged by as little as 10 volts — a discharge you cannot feel, see, or hear.

ESD damage is:

- **Invisible** — no visible burn marks or physical damage
- **Cumulative** — repeated small discharges degrade a component before it fully fails
- **Permanent** — damaged transistor traces (nanometers wide) cannot be repaired

### ESD Protection Tools

**Anti-static wrist strap:**

- A conductive band worn on the wrist, connected by a coiled cable to the PC chassis
- Contains a **1-megaohm (1 MΩ) resistor** in the cable
- The resistor limits current flow — this protects the technician from electrical hazards while still draining static charge continuously
- Attach to **unpainted metal** on the chassis interior — paint is an insulator and will not conduct charge to ground

**Anti-static mat:**

- Placed on the work surface
- Connects to chassis ground via a grounding cable
- Components removed from the system are placed on the mat, not on a desk or cardboard

**Anti-static bags:**

- Metallized (Mylar) bags in which components are shipped and stored
- Static charge on the bag's outer surface is conducted around the component, not through it
- Never store a component on top of an anti-static bag — the outer surface can carry charge. Place it inside the bag.

### Common A+ Exam Trap

> "The ESD wrist strap protects the technician from electrical shock."

**This is incorrect.** The wrist strap protects the PC components from ESD damage. The 1 MΩ resistor actually prevents dangerous current from flowing through the strap to the technician — but the strap's purpose is component protection, not personal safety. Never select "protects the user" on the A+ exam.

---

## 3. PC Hardware Safety Procedure

The A+ exam tests the correct order of safety steps. Memorize this sequence:

| Step | Action | Reason |
|---|---|---|
| 1 | Power down the OS properly | Clean shutdown avoids file system corruption |
| 2 | Unplug the AC power cord from the wall outlet | Removes all live voltage from the PSU and motherboard |
| 3 | Press the power button on the PC | Drains residual charge from motherboard capacitors |
| 4 | Attach ESD wrist strap to unpainted chassis metal | Equalizes potential between technician and chassis |
| 5 | Open the case and begin work | Safe to handle components |

**Step 2 — Wall outlet, not the power strip:** Turning off the power strip is not sufficient. The PSU still has the cord plugged in and its capacitors remain energized. You must physically unplug the cord from the wall outlet or the power strip's socket.

**Step 3 — Why press the power button?** With the cord unplugged, pressing the power button sends a shutdown signal that drains residual charge stored in the motherboard's capacitors. Skipping this step can result in a brief electric shock or component damage from residual voltage.

### Additional Safety Considerations

**PSU capacitors:** Even after unplugging, the large capacitors inside the PSU can hold lethal charge for minutes to hours. The internal 120V AC is filtered through these capacitors. Never open a PSU to repair it — replace the entire unit.

**Sharp case edges:** Budget steel cases frequently have sharp edges around the case opening, the PSU mounting area, and expansion card slots. Use work gloves when working with unfamiliar cases. Keep deliberate hand placement.

**Heavy equipment:** Servers and large towers can weigh 20–40 pounds. Use proper lifting: bend at the knees, not the waist. Request assistance for anything over 30 pounds.

**Thermal paste:** When reseating a CPU heat sink, clean old thermal paste with isopropyl alcohol (90%+) and apply a small pea-sized amount of new thermal paste before reattaching. Too much paste can spread onto the socket and cause issues.

---

## 4. Connector and Port Identification Reference

The A+ exam presents images of connectors and asks you to identify them. Study this table:

| Connector | Shape / Description | Location |
|---|---|---|
| 24-pin ATX | Wide rectangular, 2 rows of 12 pins | Motherboard right edge |
| 4/8-pin CPU power | Square connector, solid or split 4+4 | Near CPU socket, top of motherboard |
| SATA data | Small L-shaped, 7-pin | Motherboard SATA ports; one end plugs to drive |
| SATA power | Wider L-shaped, 15-pin | PSU cable; plugs into drive |
| PCIe x16 slot | Long slot, ~89mm | Motherboard, primary GPU slot |
| PCIe x1 slot | Short slot, ~25mm | Motherboard, for expansion cards |
| M.2 slot | Small rectangular slot, 2242/2280 key | Motherboard surface, often under heatsink |
| CMOS battery | Coin cell (CR2032), ~20mm diameter | Motherboard surface, flat holder |

---

## 5. Certification Exam Tips

1. **ESD wrist strap function:** Protects components — not the technician. The 1 MΩ resistor is for technician safety, but that is a byproduct, not the primary purpose.

2. **Unplug from the wall:** The A+ exam specifically tests whether you know to unplug the power cord from the wall (or the outlet on the power strip), not just turn off the strip.

3. **Press power button after unplugging:** This step is tested directly. It drains capacitor charge from the motherboard.

4. **LGA vs PGA:** LGA = pins in socket (Intel, AMD AM5). PGA = pins on processor (AMD AM4 and older). Damaged LGA socket = damaged motherboard. Damaged PGA processor = damaged CPU.

5. **DDR4 vs DDR5 are not interchangeable:** Both are 288-pin but physically keyed differently (the notch position differs). You cannot accidentally install DDR5 in a DDR4 slot.

6. **M.2 is a form factor, not an interface:** An M.2 slot can host both SATA-based and NVMe-based SSDs. The key (B key vs M key vs B+M key) determines compatibility.

7. **PSU capacitors retain charge:** This is why you never open a PSU. The exam uses this as a scenario — "technician notices PSU is dead; what should they do?" — Answer: replace it.

8. **Integrated graphics:** When a discrete GPU is installed, integrated graphics may be disabled in BIOS by default. Swapping to a system without a discrete GPU and connecting to the motherboard video port may produce no output until BIOS is reconfigured.

---

## Study Checklist

- [ ] Watch the Module 01 video lecture by Professor Nash.
- [ ] Memorize the 5-step safety procedure in order.
- [ ] Identify by name: motherboard, CPU + heat sink, RAM, PSU, HDD/SSD, GPU.
- [ ] Know all connector types in the identification reference table.
- [ ] Know LGA vs PGA socket differences and which platforms use each.
- [ ] Understand the ESD mechanism: what voltage causes damage, why damage is invisible.
- [ ] Know the three ESD protection tools and how each works.
- [ ] Complete the Module 01 Lab.
- [ ] Complete the Module 01 Quiz.

---

## Additional Resources

- [Professor Messer's CompTIA A+ 220-1101 Course — Safety Procedures](https://www.professormesser.com/free-a-plus-training/220-1101/)
- [CompTIA A+ Core 1 (220-1101) Exam Objectives](https://www.comptia.org/certifications/a)

---

## 9. Supplemental Resources

The following free, openly licensed resources extend your understanding of Module 01 topics. Each is suitable for exam preparation and independent study.

1. **Professor Messer — CompTIA A+ 220-1101 Full Course (Free Video Playlist)**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Video lectures covering safety procedures, ESD concepts, internal component identification, and connector types — directly aligned to Domain 3 objectives tested in Module 01.

2. **PC Part Picker — PC Build Guides (Free Component Reference)**
   URL: [https://pcpartpicker.com/guide/](https://pcpartpicker.com/guide/)
   Relevance: Visual walkthroughs of complete PC builds that reinforce motherboard layout, PSU connector routing, and physical component placement. Useful for students who lack access to a physical lab machine.

3. **iFixit — Free Repair Manuals and Component Photos**
   URL: [https://www.ifixit.com/Guide](https://www.ifixit.com/Guide)
   Relevance: High-resolution, step-by-step teardown guides with annotated photos of internal components. Excellent supplement to Part 1 of the lab when a physical machine is unavailable.

4. **Khan Academy — Electricity and Circuits (Free OER Course)**
   URL: [https://www.khanacademy.org/science/physics/circuits-topic](https://www.khanacademy.org/science/physics/circuits-topic)
   Relevance: Background reading for understanding electrical grounding, capacitors, and the physics behind ESD. Helps students build intuition for why the safety procedures work as described.

5. **CompTIA A+ CertMike — Free Study Notes (OER)**
   URL: [https://www.certmike.com/](https://www.certmike.com/)
   Relevance: Free objective-by-objective study notes aligned to the 220-1101 exam blueprint. Useful as a rapid review tool before quizzes and as a cross-reference for any concept in the reading guide.
