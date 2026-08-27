# Lab Activity: Module 02 - Motherboards and Form Factors

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5
**Estimated Completion Time:** 60–90 minutes
**Submission:** Canvas LMS — Module 02 Lab Assignment

---

## Overview

In this lab you will examine a physical or instructor-provided reference motherboard and complete a structured identification and analysis exercise. The goal is to connect the terminology from the reading guide to actual hardware components you will encounter on the job and on the CompTIA A+ exam. No terminal commands are used in this lab. All work is hands-on observation, measurement, and written analysis.

If your section does not have access to physical motherboards, your instructor will provide high-resolution reference images and a labeled diagram sheet. Complete all tables and answer all questions using those materials.

---

## Safety and Handling Requirements

Before handling any motherboard:

- Wear an ESD (electrostatic discharge) wrist strap connected to a grounded surface, or touch a bare metal part of the grounded PC case before picking up the board.
- Hold the motherboard by its edges only. Do not touch the gold edge connectors, CPU socket pins, or surface-mount components.
- Place the board on an anti-static mat or its original anti-static bag — never on a bare metal surface or directly on a desk.
- Do not force any connector or card into a slot. If it does not seat with moderate even pressure, re-check alignment.

---

## Part 1: Form Factor Identification and Measurement

### Step 1 — Identify the motherboard form factor

Obtain the motherboard assigned to your station (or open the reference image provided by your instructor). Measure or record the board's dimensions.

Fill in the table below:

| Field                                        | Your Observation |
|----------------------------------------------|------------------|
| Measured length (inches or mm)               |                  |
| Measured width (inches or mm)                |                  |
| Form factor (ATX / mATX / ITX)               |                  |
| Number of PCIe slots present                 |                  |
| Number of RAM slots present                  |                  |
| Number of SATA data ports                    |                  |
| Number of M.2 slots                          |                  |
| Manufacturer and model (if visible on board) |                  |

### Step 2 — Identify each PCIe slot by type

Examine the PCIe slots on the board. Physically compare their lengths. Fill in the table below for each slot present, numbering them from the slot closest to the CPU socket downward (PCIe slot 1 = closest to CPU):

| Slot Number | Physical Length (short/medium/long) | Lane Count (x1 / x4 / x8 / x16) | Intended Use (GPU / NIC / NVMe / other) |
|-------------|-------------------------------------|----------------------------------|-----------------------------------------|
| Slot 1      |                                     |                                  |                                         |
| Slot 2      |                                     |                                  |                                         |
| Slot 3      |                                     |                                  |                                         |
| Slot 4      |                                     |                                  |                                         |

If your board has fewer than four PCIe slots, leave the extra rows blank and note how many slots are present.

### Step 3 — Locate and document power connectors

Find the following connectors on the board and record their location (e.g., "top-right corner," "left edge near RAM slots"):

| Connector                | Location on Board | Number of Pins |
|--------------------------|-------------------|----------------|
| Main ATX power connector |                   |                |
| CPU EPS power connector  |                   |                |
| Front panel header block |                   |                |
| USB 2.0 internal header  |                   |                |
| USB 3.0 internal header  |                   |                |
| CPU_FAN header           |                   |                |

---

## Part 2: CMOS Battery and Clear Jumper Investigation

### Step 4 — Locate the CMOS battery

Find the CR2032 coin cell battery on the motherboard surface. It is usually a round silver disc seated in a horizontal clip holder.

**Question 2-A:** Where on the board is the CMOS battery located? Describe the position relative to a nearby landmark — CPU socket, RAM slots, chipset chip, etc.

Your answer:

**Question 2-B:** What happens to BIOS/UEFI settings — specifically the system date and time — when this battery is removed and the system is fully unplugged? Explain why.

Your answer:

**Question 2-C:** A user reports that their PC always shows January 1, 2000 at 12:00 AM every time they turn it on, even after setting the correct date. The PC boots normally and runs without errors otherwise. What is the most likely cause, and what is the repair?

Your answer:

### Step 5 — Locate the CMOS clear jumper

Find the CMOS clear jumper block. It is typically a three-pin header located near the CMOS battery, sometimes labeled CLR_CMOS, JBAT1, or similar.

**Question 2-D:** Where on the board is the CMOS clear jumper located?

Your answer:

**Question 2-E:** Describe the two jumper positions and what each position does. You do not need to move the jumper — describe the procedure only.

Your answer:

**Question 2-F:** A technician set a BIOS supervisor password on a workstation and then forgot it. The system prompts for the password at every boot and cannot be bypassed through the BIOS menu. What procedure should the technician follow to regain access, and what is the tradeoff of using this procedure?

Your answer:

---

## Part 3: Scenario Analysis

Read each scenario and write a short answer (3–5 sentences) using the concepts from this module.

### Scenario A — Form Factor Mismatch

A customer wants to upgrade their aging desktop to a newer motherboard. Their current case is a standard ATX mid-tower. The salesperson at the electronics store recommends a Mini-ITX board because it is cheaper and compact. The customer asks you whether this is a good choice.

**Question 3-A:** What do you tell the customer? Identify the compatibility issue and recommend the correct alternative form factor for their situation.

Your answer:

### Scenario B — Expansion Card Placement

A technician is building a workstation with the following cards to install: one dedicated GPU, one PCIe NVMe adapter, and one Wi-Fi card. The Micro-ATX motherboard has one x16 slot, one x4 slot, and one x1 slot.

**Question 3-B:** Which card goes in which slot, and why? Is there any slot assignment that would prevent the system from working correctly?

Your answer:

### Scenario C — Chipset Research

A customer purchases a used motherboard listed as "Intel LGA1700 socket." They want to install an Intel 13th generation Core i9 processor. They ask you if the socket alone guarantees compatibility.

**Question 3-C:** What additional information must you verify beyond the socket type, and why does it matter?

Your answer:

---

## Deliverables and Submission

Submit the following to Canvas by the Module 02 lab deadline:

1. Completed Part 1 tables (Steps 1–3) — either typed into the submission document or submitted as clear, legible photographs of your handwritten tables.
2. Written answers to all questions in Parts 2 and 3 (Questions 2-A through 3-C).
3. One photograph of the motherboard you examined showing the CMOS battery location clearly visible (circle or annotate the battery in the photo). If using reference images, annotate the provided image instead.

---

## Grading Rubric

| Component                                                                | Points  |
|--------------------------------------------------------------------------|---------|
| Part 1 tables fully completed and accurate                               | 30      |
| Part 2 questions answered with correct reasoning                         | 30      |
| Part 3 scenario responses demonstrate understanding of module concepts   | 30      |
| Photo/annotation of CMOS battery location                                | 10      |
| **Total**                                                                | **100** |

Partial credit is awarded for answers that show correct reasoning even if a specific detail is incorrect. No credit is awarded for blank responses or answers that indicate the student did not attempt the identification exercise.

---

## Part 9 — Challenge Exercise

These advanced steps are optional for students seeking additional depth and are not included in the standard grading rubric.

### Challenge Step 1 — BIOS/UEFI Feature Audit

Access the UEFI setup on any available system (your lab machine, home PC, or an instructor-provided system):

1. Enter UEFI setup at boot (typically Del, F2, or F12 — consult the board manual).
1. Navigate to the Security or Boot section and locate the **Secure Boot** setting. Record whether it is currently enabled or disabled, and whether the system is in UEFI native mode or CSM/legacy mode.
1. Locate the **Boot Order** configuration. Record the current boot device priority list.
1. Find the **System Information** or **Main** page. Record the UEFI/BIOS version, the CPU model, the installed RAM size and speed (as detected by the firmware), and the current system date/time.
1. Exit without saving changes. In your notes, explain what would happen if you removed the CMOS battery for 30 seconds and rebooted — which of the values you recorded would change and which would not?

### Challenge Step 2 — PCIe Bandwidth Calculation

Using the PCIe bandwidth formula `Bandwidth = Lanes × Transfer Rate per Lane`, calculate the theoretical maximum bidirectional bandwidth for each of the following slot configurations. Show your work.

| Configuration | Transfer Rate per Lane | Total Bandwidth |
|---|---|---|
| PCIe 3.0 x1 | ~985 MB/s | |
| PCIe 3.0 x16 | ~985 MB/s | |
| PCIe 4.0 x4 | ~1,969 MB/s | |
| PCIe 4.0 x16 | ~1,969 MB/s | |
| PCIe 5.0 x16 | ~3,938 MB/s | |

After completing the table, answer: A mainstream NVMe SSD achieves sequential read speeds of approximately 7,000 MB/s. What is the minimum PCIe 4.0 lane configuration required to avoid the SSD being bottlenecked by the interface? Show your calculation.

### Challenge Step 3 — Chipset Compatibility Research

Choose any two modern desktop motherboards from different manufacturers (use the manufacturer's product page or a site like pcpartpicker.com). For each board, document the following using only the official specification sheet or product page:

1. Form factor
1. Socket type
1. Chipset model
1. Supported CPU generations (list the generation names, e.g., "12th and 13th gen Intel Core")
1. Maximum supported RAM speed (XMP/EXPO profile)
1. Number of M.2 slots and their PCIe generation support
1. Whether CPU overclocking is supported (yes/no) and which chipset feature enables or prevents it

Write a one-paragraph summary comparing the two boards: which would you recommend for a budget home office build, and which for a performance workstation, and why?
