# Video Script: CIS-2320 — Hardware Fundamentals

## Module 01 — Introduction to PC Hardware & Safety

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course &bull; Module 01</strong>
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

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

Welcome to CIS-2320 — Hardware Fundamentals. I'm Professor Nash, and this course is built around the CompTIA A+ certification — the industry-standard credential for IT support technicians. Every module maps directly to the A+ Core 1 (220-1101) and Core 2 (220-1102) exam objectives. Module 16 is your certification exam.

Today we cover the foundation: what's inside a desktop PC, why electrostatic discharge is the silent killer of computer hardware, and the exact safety procedure you follow every single time you open a computer case. These topics appear on Domain 3 of the A+ Core 1 exam — Hardware — and they show up in scenario questions throughout the test. Let's get into it.

---

## Part 1 — Internal PC Components Overview

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

**[SHOW COMPONENT: Desktop PC case with side panel removed]**

Before you can work on a PC, you need to know what you're looking at. Let me walk you through the major internal components.

**[SHOW COMPONENT: Motherboard]**

This is the **motherboard** — the main circuit board. Everything connects to it: CPU, RAM, storage, graphics card, power supply. The motherboard determines which CPU generation you can use, how much RAM you can install, and which expansion cards are supported.

**[SHOW COMPONENT: CPU/Processor]**

This is the **CPU** — central processing unit, or processor. It sits in the CPU socket on the motherboard and is secured by a retention lever or load plate depending on the socket type. It's covered by a **heat sink** — a metal block with fins — and a **CPU fan** that keeps it cool. The CPU is the brain of the system.

**[SHOW COMPONENT: RAM module]**

This is a **RAM module** — random access memory. It snaps into DIMM slots on the motherboard. RAM is volatile — it loses its data when power is off. The A+ exam expects you to know DDR4 and DDR5 generation differences, dual-channel configuration, and physical slot identification.

**[SHOW COMPONENT: Power supply unit]**

This is the **PSU** — power supply unit. It converts AC power from the wall outlet to DC power the components need. It has multiple connectors: a 24-pin ATX connector for the motherboard, a 4-pin or 8-pin CPU power connector, SATA power connectors for drives, and PCIe connectors for graphics cards.

**[SHOW COMPONENT: Storage drive]**

Storage drives — either an **HDD** (hard disk drive, mechanical, spinning platters) or an **SSD** (solid state drive, no moving parts, faster). They connect to the motherboard via SATA data cables and receive power from the PSU via SATA power connectors.

**[SHOW COMPONENT: GPU/Graphics card]**

And the **GPU** — graphics processing unit, or graphics card. It inserts into the PCIe x16 slot on the motherboard. On systems with integrated graphics, this card may be absent.

The A+ exam uses scenario-based questions. You might be told: 'A user's PC powers on but shows no video output.' You need to know: check the monitor cable, check the GPU seating in the PCIe slot, check whether integrated graphics is disabled in BIOS. Knowing what each component does and where it is physically located is non-negotiable for that exam.

---

## Part 2 — Electrostatic Discharge (ESD)

Electrostatic discharge — ESD — is the silent threat in hardware work. It is the sudden flow of static electricity between two objects at different electrical potentials. You know the feeling when you shuffle across carpet in socks and then touch a doorknob — that spark is ESD. On your body, you need thousands of volts to feel it. On a computer chip, 10 volts is enough to cause damage.

**Why is this serious?** The integrated circuits on a CPU, RAM module, or graphics card have traces that are nanometers wide. A static discharge destroys those traces — permanently. The component may still appear to work, or it may fail intermittently for months before dying completely. You cannot see the damage. You cannot repair it.

ESD protection works by keeping the technician and the components at the same electrical potential — no potential difference, no discharge.

**Anti-static wrist strap:** A wrist strap with a 1-megaohm resistor connects your wrist to the metal chassis of the PC. The resistor limits current flow for safety while continuously draining static charge from your body.

**Anti-static mat:** A conductive mat placed on the work surface. Connect it to the chassis ground. Place components on it when they are removed from the system.

**Anti-static bags:** Components are shipped and stored in metallized anti-static bags. When you receive a new RAM module or CPU, it arrives in one of these bags. Do not remove it until you are grounded and ready to install.

**A+ exam tip:** A common distractor is 'the ESD wrist strap protects the technician from electrical shock.' That is wrong. The wrist strap protects the PC components, not the person. The 1-megaohm resistor actually prevents any dangerous current from flowing through the strap to the technician. The exam will offer that distractor — do not select it.

---

## Part 3 — Safety Procedures

Let's talk about the correct safety procedure for opening a PC. The order matters — the A+ exam tests this.

**Step 1: Power down the system properly.** Shut down the OS — don't just press the power button for a hard shutdown unless necessary.

**Step 2: Unplug the AC power cord from the wall outlet.** Not from the PSU — from the wall outlet or power strip. Just turning off the power strip is not sufficient. The PSU has capacitors that retain charge even when the strip is off. You must unplug the cord.

**Step 3: Press the power button on the PC.** With the cord unplugged, pressing the power button drains residual charge stored in the motherboard capacitors. This is the step most beginners skip — and it can result in a brief shock or a component damaged by residual voltage.

**Step 4: Put on your ESD wrist strap and attach it to the bare metal interior of the chassis.** Attach to unpainted metal — paint is an insulator and will not provide a ground path.

**Step 5: Open the case and begin work.**

**Additional safety notes for the A+ exam:**

**PSU capacitors:** Never open a PSU. Even when unplugged, the capacitors inside a PSU can store lethal voltage for extended periods. If a PSU fails, replace it — do not attempt to repair it.

**Sharp edges:** PC cases — especially low-cost steel cases — have sharp metal edges, especially around the case opening and near the power supply mounting area. Use work gloves when necessary and be deliberate about hand placement.

**Lifting heavy equipment:** Servers and large desktop towers can weigh 20–40 pounds. Use proper lifting technique: bend at the knees, not the waist. Get assistance for heavier equipment.

---

## Part 4 — Component Identification for the A+ Exam

The A+ exam uses images and scenario descriptions. You must be able to identify these by sight:

**Connectors and ports:**

- 24-pin ATX motherboard power connector (wide, 2-row connector from PSU)
- 4-pin or 8-pin CPU power connector (square connector near the CPU socket)
- SATA data connector (small L-shaped connector on the motherboard, connects to drives)
- SATA power connector (wider L-shaped connector from PSU)
- PCIe x16 slot (long slot on motherboard for GPU)
- PCIe x1 slot (short slot for expansion cards like network adapters)
- M.2 slot (small slot, often covered by a heatsink, for M.2 NVMe SSDs)

**Physical components:**

- DIMM slots for RAM — usually two or four slots, color-coded for dual-channel pairing
- CPU socket (LGA vs. PGA): LGA (Land Grid Array) has pins in the socket — Intel style. PGA (Pin Grid Array) has pins on the processor — older AMD style. AM5 (AMD) moved to LGA.
- CMOS battery (small coin cell on the motherboard — CR2032 — stores BIOS settings)
- POST diagnostic LED indicators and speaker header

The Module 01 lab has you open a PC case (physical or virtual) and identify each of these components. You will sketch a component map, label each part, and document the connector type for the PSU-to-motherboard connection and the PSU-to-drive connections.

This course builds on itself. Motherboards are Module 02, CPUs are Module 03, RAM is Module 04. Today's identification exercise is the foundation for all of those. Come back and review this video whenever you need a visual anchor for those topics. Good luck.

---

**[END CARD: Texas Wesleyan University | CIS-2320 Hardware Fundamentals | Module 01 — Introduction to PC Hardware & Safety]**

---

## Additional Resources

- [Professor Messer's CompTIA A+ 220-1101 Course — Safety Procedures](https://www.professormesser.com/free-a-plus-training/220-1101/)
- [CompTIA A+ Core 1 (220-1101) Exam Objectives](https://www.comptia.org/certifications/a)
- [Professor Messer's A+ Core 1 Practice Exams](https://www.professormesser.com/practice-exams/a-plus-practice-exams/)
