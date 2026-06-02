# Video Script: CIS-2320 — Hardware Fundamentals

## Module 01 — Introduction to PC Hardware & Safety

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Record with a disassembled desktop PC on the desk for visual reference. Show actual components when naming them.
> - [PAUSE] = 2 seconds of silence.
> - [SHOW COMPONENT] = hold component toward camera.
> - Key emphasis: ESD damage is invisible and cumulative. A spark you cannot feel can destroy a CPU worth hundreds of dollars.
> - The CompTIA A+ exam tests component recognition by sight — show each component clearly.
> - Safety procedure order matters on the exam: Power down → Unplug → Press power button → ESD strap → Open case.
> - Common exam trap: "leaving the power cable in while the strip is off" — this is wrong. Unplug the cord.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 01 | Introduction to PC Hardware & Safety | CIS-2320"]**

"Welcome to CIS-2320 — Hardware Fundamentals. I'm Professor Nash, and this course is built around the CompTIA A+ certification — the industry-standard credential for IT support technicians. Every module maps directly to the A+ Core 1 (220-1101) and Core 2 (220-1102) exam objectives. Module 16 is your certification exam.

Today we cover the foundation: what's inside a desktop PC, why electrostatic discharge is the silent killer of computer hardware, and the exact safety procedure you follow every single time you open a computer case. These topics appear on Domain 3 of the A+ Core 1 exam — Hardware — and they show up in scenario questions throughout the test. Let's get into it."

---

## [01:30 – 06:00] Part 1 — Internal PC Components Overview

**[SHOW COMPONENT: Desktop PC case with side panel removed]**

"Before you can work on a PC, you need to know what you're looking at. Let me walk you through the major internal components.

**[SHOW COMPONENT: Motherboard]**

This is the **motherboard** — the main circuit board. Everything connects to it: CPU, RAM, storage, graphics card, power supply. The motherboard determines which CPU generation you can use, how much RAM you can install, and which expansion cards are supported.

[PAUSE]

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

[PAUSE]

The A+ exam uses scenario-based questions. You might be told: 'A user's PC powers on but shows no video output.' You need to know: check the monitor cable, check the GPU seating in the PCIe slot, check whether integrated graphics is disabled in BIOS. Knowing what each component does and where it is physically located is non-negotiable for that exam."

---

## [06:00 – 12:00] Part 2 — Electrostatic Discharge (ESD)

**[SHOW SLIDE: "ESD — The Invisible Hardware Killer"]**

"Electrostatic discharge — ESD — is the silent threat in hardware work. It is the sudden flow of static electricity between two objects at different electrical potentials. You know the feeling when you shuffle across carpet in socks and then touch a doorknob — that spark is ESD. On your body, you need thousands of volts to feel it. On a computer chip, 10 volts is enough to cause damage.

[PAUSE]

**Why is this serious?** The integrated circuits on a CPU, RAM module, or graphics card have traces that are nanometers wide. A static discharge destroys those traces — permanently. The component may still appear to work, or it may fail intermittently for months before dying completely. You cannot see the damage. You cannot repair it.

**[SHOW DIAGRAM: Human body model — static charge paths]**

ESD protection works by keeping the technician and the components at the same electrical potential — no potential difference, no discharge.

**Anti-static wrist strap:** A wrist strap with a 1-megaohm resistor connects your wrist to the metal chassis of the PC. The resistor limits current flow for safety while continuously draining static charge from your body.

**Anti-static mat:** A conductive mat placed on the work surface. Connect it to the chassis ground. Place components on it when they are removed from the system.

**Anti-static bags:** Components are shipped and stored in metallized anti-static bags. When you receive a new RAM module or CPU, it arrives in one of these bags. Do not remove it until you are grounded and ready to install.

[PAUSE]

**A+ exam tip:** A common distractor is 'the ESD wrist strap protects the technician from electrical shock.' That is wrong. The wrist strap protects the PC components, not the person. The 1-megaohm resistor actually prevents any dangerous current from flowing through the strap to the technician. The exam will offer that distractor — do not select it."

---

## [12:00 – 17:00] Part 3 — Safety Procedures

**[SHOW SLIDE: "PC Hardware Safety Procedure — In Order"]**

"Let's talk about the correct safety procedure for opening a PC. The order matters — the A+ exam tests this.

**Step 1: Power down the system properly.** Shut down the OS — don't just press the power button for a hard shutdown unless necessary.

**Step 2: Unplug the AC power cord from the wall outlet.** Not from the PSU — from the wall outlet or power strip. Just turning off the power strip is not sufficient. The PSU has capacitors that retain charge even when the strip is off. You must unplug the cord.

**Step 3: Press the power button on the PC.** With the cord unplugged, pressing the power button drains residual charge stored in the motherboard capacitors. This is the step most beginners skip — and it can result in a brief shock or a component damaged by residual voltage.

**Step 4: Put on your ESD wrist strap and attach it to the bare metal interior of the chassis.** Attach to unpainted metal — paint is an insulator and will not provide a ground path.

**Step 5: Open the case and begin work.**

[PAUSE]

**Additional safety notes for the A+ exam:**

**PSU capacitors:** Never open a PSU. Even when unplugged, the capacitors inside a PSU can store lethal voltage for extended periods. If a PSU fails, replace it — do not attempt to repair it.

**Sharp edges:** PC cases — especially low-cost steel cases — have sharp metal edges, especially around the case opening and near the power supply mounting area. Use work gloves when necessary and be deliberate about hand placement.

**Lifting heavy equipment:** Servers and large desktop towers can weigh 20–40 pounds. Use proper lifting technique: bend at the knees, not the waist. Get assistance for heavier equipment."

---

## [17:00 – 21:00] Part 4 — Component Identification for the A+ Exam

**[SHOW SLIDE: "A+ Core 1 — What You Must Identify by Sight"]**

"The A+ exam uses images and scenario descriptions. You must be able to identify these by sight:

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

[PAUSE]

The Module 01 lab has you open a PC case (physical or virtual) and identify each of these components. You will sketch a component map, label each part, and document the connector type for the PSU-to-motherboard connection and the PSU-to-drive connections.

This course builds on itself. Motherboards are Module 02, CPUs are Module 03, RAM is Module 04. Today's identification exercise is the foundation for all of those. Come back and review this video whenever you need a visual anchor for those topics. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2320 Hardware Fundamentals | Module 01 — Introduction to PC Hardware & Safety]**

---

## Additional Resources

- [Professor Messer's CompTIA A+ 220-1101 Course — Safety Procedures](https://www.professormesser.com/free-a-plus-training/220-1101/)
- [CompTIA A+ Core 1 (220-1101) Exam Objectives](https://www.comptia.org/certifications/a)
- [Professor Messer's A+ Core 1 Practice Exams](https://www.professormesser.com/practice-exams/a-plus-practice-exams/)
