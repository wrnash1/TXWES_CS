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

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CIS-2320 Module 01</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH" title="CompTIA A+ (Core 1 / Core 2) Complete Training Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA A+ (Core 1 / Core 2) Complete Training Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

## Course: CIS-2320 Hardware Fundamentals

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3: Hardware

---

## Introduction

Before you touch a component, you must know three things: what it is, where it is, and how to handle it without destroying it. This module builds that foundation. Every subsequent module in CIS-2320 assumes you can identify components on sight and apply safe handling procedures automatically. The CompTIA A+ exam tests these skills directly — Domain 3 (Hardware) contains scenario questions that require you to recognize components from descriptions, choose correct connectors, and identify the right safety procedure for a given situation.

---

<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-2320 HARDWARE FUNDAMENTALS</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Core Internal PC Components Anatomy &amp; Interconnections</text>

  <!-- Chassis Outline -->
  <rect x="40" y="95" width="770" height="330" fill="#1e293b" stroke="#334155" stroke-width="2" rx="8"/>
  <text x="55" y="115" fill="#64748b" font-size="11" font-weight="bold">DESKTOP CHASSIS (INTERIOR LAYOUT)</text>

  <!-- PSU -->
  <rect x="60" y="130" width="180" height="130" fill="#0f172a" stroke="#d9a74a" stroke-width="1.5" rx="6"/>
  <text x="150" y="160" fill="#d9a74a" font-size="14" font-weight="bold" text-anchor="middle">POWER SUPPLY (PSU)</text>
  <text x="150" y="180" fill="#94a3b8" font-size="11" text-anchor="middle">120V AC → +12V, +5V, +3.3V DC</text>
  <rect x="80" y="200" width="140" height="20" fill="#1e293b" rx="3"/>
  <text x="150" y="214" fill="#38bdf8" font-size="10" text-anchor="middle">24-pin ATX / 8-pin EPS / PCIe</text>
  <rect x="80" y="225" width="140" height="20" fill="#1e293b" rx="3"/>
  <text x="150" y="239" fill="#10b981" font-size="10" text-anchor="middle">80 PLUS Certified Efficiency</text>

  <!-- Drive Bays -->
  <rect x="60" y="280" width="180" height="125" fill="#0f172a" stroke="#64748b" stroke-width="1.5" rx="6"/>
  <text x="150" y="305" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">STORAGE DRIVE BAYS</text>
  <rect x="75" y="320" width="150" height="35" fill="#1e293b" stroke="#0284c7" rx="4"/>
  <text x="150" y="342" fill="#38bdf8" font-size="11" text-anchor="middle">3.5" HDD / 2.5" SATA SSD</text>
  <rect x="75" y="365" width="150" height="25" fill="#1e293b" stroke="#334155" rx="4"/>
  <text x="150" y="382" fill="#94a3b8" font-size="10" text-anchor="middle">SATA 7-pin Data + 15-pin Pwr</text>

  <!-- Motherboard Area -->
  <rect x="270" y="130" width="520" height="275" fill="#0f172a" stroke="#38bdf8" stroke-width="2" rx="6"/>
  <text x="530" y="152" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">SYSTEM MOTHERBOARD (ATX)</text>

  <!-- CPU Socket & Cooler -->
  <rect x="290" y="170" width="115" height="115" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="6"/>
  <rect x="315" y="185" width="65" height="65" fill="#334155" rx="4"/>
  <text x="347" y="215" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">CPU</text>
  <text x="347" y="232" fill="#fca5a5" font-size="9" text-anchor="middle">(LGA / PGA)</text>
  <text x="347" y="272" fill="#cbd5e1" font-size="9" text-anchor="middle">Heatsink + Fan (4-pin)</text>

  <!-- RAM Slots -->
  <g transform="translate(425, 170)">
    <rect x="0" y="0" width="15" height="115" fill="#1e293b" stroke="#3b82f6" rx="2"/>
    <rect x="22" y="0" width="15" height="115" fill="#1e293b" stroke="#10b981" rx="2"/>
    <rect x="44" y="0" width="15" height="115" fill="#1e293b" stroke="#3b82f6" rx="2"/>
    <rect x="66" y="0" width="15" height="115" fill="#1e293b" stroke="#10b981" rx="2"/>
    <text x="40" y="132" fill="#cbd5e1" font-size="10" text-anchor="middle">DIMM Slots (DDR4/DDR5)</text>
    <text x="40" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Dual-Channel Pairs</text>
  </g>

  <!-- M.2 NVMe Slot -->
  <rect x="530" y="175" width="110" height="28" fill="#1e293b" stroke="#d9a74a" rx="4"/>
  <text x="585" y="193" fill="#d9a74a" font-size="10" font-weight="bold" text-anchor="middle">M.2 NVMe SSD (PCIe x4)</text>

  <!-- Expansion Slots -->
  <g transform="translate(290, 305)">
    <rect x="0" y="0" width="230" height="16" fill="#0284c7" rx="3"/>
    <text x="115" y="12" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">PCIe 5.0 ×16 Slot (Discrete GPU / Graphics Card)</text>
    <rect x="0" y="22" width="70" height="12" fill="#64748b" rx="2"/>
    <text x="35" y="31" fill="#ffffff" font-size="8" text-anchor="middle">PCIe ×1</text>
    <rect x="0" y="39" width="140" height="14" fill="#0284c7" rx="2"/>
    <text x="70" y="50" fill="#ffffff" font-size="9" text-anchor="middle">PCIe ×4 Expansion</text>
    <rect x="0" y="58" width="230" height="16" fill="#0284c7" rx="3"/>
    <text x="115" y="70" fill="#ffffff" font-size="10" text-anchor="middle">PCIe ×16 Secondary Slot</text>
  </g>

  <!-- Rear I/O Panel -->
  <rect x="665" y="170" width="110" height="210" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <text x="720" y="190" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">REAR I/O PANEL</text>
  <rect x="680" y="205" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="219" fill="#38bdf8" font-size="9" text-anchor="middle">USB 3.2 Ports</text>
  <rect x="680" y="235" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="249" fill="#10b981" font-size="9" text-anchor="middle">2.5GbE RJ-45 LAN</text>
  <rect x="680" y="265" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="279" fill="#d9a74a" font-size="9" text-anchor="middle">HDMI / DisplayPort</text>
  <rect x="680" y="295" width="80" height="20" fill="#0f172a" rx="2"/>
  <text x="720" y="309" fill="#f43f5e" font-size="9" text-anchor="middle">HD Audio Jacks</text>

  <!-- Footer Banner -->
  <rect x="40" y="435" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="457" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ CompTIA A+ Blueprint: Identify all 7 primary internal components on sight and know their physical interconnects.</text>
</svg>
</div>

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

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 01 — Introduction to PC Hardware & Safety** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 01 — Introduction to PC Hardware & Safety**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 01 — Introduction to PC Hardware & Safety**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 01 — Introduction to PC Hardware & Safety**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**

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
