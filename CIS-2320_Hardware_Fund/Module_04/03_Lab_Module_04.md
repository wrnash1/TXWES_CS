# Lab Activity: Module 04 - Memory (RAM) Types and Configuration

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.3
**Estimated Completion Time:** 60–90 minutes
**Submission:** Canvas LMS — Module 04 Lab Assignment

---

## Overview

In this lab you will identify RAM modules by physical inspection, configure dual-channel memory in the correct slot positions, install a desktop DIMM and examine a laptop SODIMM installation, and analyze memory troubleshooting scenarios. All work involves physical hardware observation, identification, and written analysis. No terminal commands are required.

If physical hardware is not available at your station, your instructor will provide high-resolution reference photographs of RAM modules, motherboard slots, and a laptop SODIMM bay. Complete all tables and answer all questions using those materials and the specification tables in the reading guide.

---

## Safety and Handling Requirements

Before handling any RAM module or motherboard:

- Wear an ESD wrist strap or touch a grounded metal surface before picking up any memory module.
- Hold RAM modules by the short ends (edges) only. Never touch the gold contact fingers along the bottom edge.
- When pressing a DIMM into its slot, apply even pressure with both thumbs on both ends simultaneously. Uneven pressure can crack the PCB.
- For SODIMM: insert at the correct angle before pressing flat. Never force a SODIMM straight down — it inserts at an angle and forces at a wrong angle bend the slot contacts.
- Never install or remove RAM while the system is powered on.

---

## Part 1: RAM Module Identification

### Step 1 — Identify DDR generation by physical inspection

Examine the RAM module(s) provided at your station. Using visual inspection and the reading guide specification tables, complete the identification table for each module present (up to three):

| Field                                        | Module 1 | Module 2 | Module 3 |
|----------------------------------------------|----------|----------|----------|
| Form factor (DIMM / SODIMM)                  |          |          |          |
| Physical length (measure or estimate in mm)  |          |          |          |
| Number of contact pins (count one side x2)   |          |          |          |
| DDR generation (DDR3 / DDR4 / DDR5)          |          |          |          |
| Speed marking on label (e.g., DDR4-3200)     |          |          |          |
| Voltage rating on label (if present)         |          |          |          |
| Capacity per module (GB)                     |          |          |          |
| Manufacturer and part number (if visible)    |          |          |          |

### Step 2 — Locate and examine the notch

Examine the bottom edge of each module. Locate the notch — the gap in the gold contact fingers that physically keys the module to its generation-specific slot.

**Question 1-A:** Describe the notch position on the module(s) you examined. Is it centered, slightly left of center, or slightly right of center? How does the notch prevent a technician from installing the wrong generation of RAM?

Your answer:

**Question 1-B:** Both DDR4 and DDR5 desktop DIMMs have 288 pins. A technician orders a DDR5-4800 module for a system that supports DDR4 only. The module arrives and the technician attempts to install it. What happens, and why?

Your answer:

### Step 3 — Identify module speed notation

The label on a RAM module may express speed in DDR notation (e.g., DDR4-3200) or in PC notation (e.g., PC4-25600).

**Question 1-C:** On the module(s) at your station, which notation is used on the label? Using the formula PC number = data rate x 8, convert the speed of one of your modules from DDR notation to PC notation (or vice versa) and show your calculation.

Your answer:

---

## Part 2: Dual-Channel Slot Configuration

### Step 4 — Identify slot positions on the motherboard

Examine the motherboard at your station. Locate the RAM slots and identify how they are labeled or color-coded.

Fill in the slot identification table:

| Slot Position (physical, counted from CPU socket) | Label on Board (A1/A2/B1/B2 or 1/2/3/4) | Color | Channel (A or B) |
|----------------------------------------------------|------------------------------------------|-------|------------------|
| Slot 1 (closest to CPU)                            |                                          |       |                  |
| Slot 2                                             |                                          |       |                  |
| Slot 3                                             |                                          |       |                  |
| Slot 4 (farthest from CPU)                         |                                          |       |                  |

If your board has only two slots, record both and note that dual-channel is automatic with any two installed modules.

**Question 2-A:** Based on your slot identification table, which two slots should be populated first if only two RAM modules are being installed? Cite the specific slot labels (e.g., A1+B1).

Your answer:

**Question 2-B:** A technician installs two 8 GB DDR4 modules in slots A1 and A2 of a four-slot board. After booting into Windows, Task Manager shows 16 GB of RAM installed but the speed seems slower than expected. A utility reports single-channel mode. What caused this, and what is the fix?

Your answer:

### Step 5 — Perform or document DIMM installation

If a desktop DIMM and motherboard are available at your station, perform the following installation steps. If not, document what each step should look like using the reference photographs provided.

1. Open both locking clips on the RAM slot to the fully outward position.
2. Align the module's notch with the key bump in the slot.
3. Place both thumbs on the ends of the module and press straight down with even pressure until both locking clips snap upward into the module's edge notches.
4. Verify the clips are fully engaged on both sides.

**Question 2-C:** After pressing the module down, one locking clip snaps shut but the other does not. What does this indicate, and what should you do?

Your answer:

**Question 2-D:** If you press a DDR4 DIMM into a slot and it does not seat with moderate pressure, what should you check before applying more force?

Your answer:

---

## Part 3: SODIMM Examination

### Step 6 — Examine laptop SODIMM installation

Using the laptop assigned to your station or the reference photographs provided, locate the SODIMM memory compartment. (On most laptops this is accessed by removing a panel on the underside.)

Fill in the SODIMM identification table:

| Field                                          | Your Observation |
|------------------------------------------------|------------------|
| Number of SODIMM slots in the laptop           |                  |
| SODIMM generation (DDR3 / DDR4 / DDR5)         |                  |
| Module capacity per slot (GB)                  |                  |
| Insertion angle required (degrees, approximate)|                  |
| Retention mechanism (clips / screw / other)    |                  |
| Are both slots populated? (Yes / No)           |                  |
| Is this system running dual-channel? (Yes / No / Cannot determine) | |

**Question 3-A:** Describe the SODIMM installation procedure in your own words, from the angle of insertion to the final locked position. How does this differ from installing a standard desktop DIMM?

Your answer:

**Question 3-B:** A laptop user upgrades from one 8 GB DDR4 SODIMM to two 8 GB DDR4 SODIMMs. Before the upgrade, memory diagnostics showed single-channel operation. After the upgrade with both slots populated, what configuration change has occurred and what performance benefit should the user expect?

Your answer:

---

## Part 4: Memory Troubleshooting Scenarios

Read each scenario and write a 3–5 sentence response identifying the most likely cause and corrective action.

### Scenario A — No Video After RAM Upgrade

A technician adds a second 8 GB DDR4 module to a desktop to bring total RAM from 8 GB to 16 GB. After installation, the system powers on but produces no video output and no beep codes. The original module was in slot A2.

**Question 4-A:** What is the most likely cause of the no-video failure after installing the second module? Describe the diagnostic steps you would take and the most probable fix.

Your answer:

### Scenario B — RAM Running Slower Than Advertised

A user purchases a DDR4-3600 16 GB kit (2x8 GB) and installs both modules in the correct paired slots on a compatible motherboard. After booting into Windows, CPU-Z reports the RAM is running at 2133 MHz (DDR4-2133). The user contacts you saying the RAM is defective.

**Question 4-B:** Is the RAM defective? Explain why the system is running at 2133 MHz despite the modules being rated for 3600 MHz, and describe the exact step the technician must take to resolve this.

Your answer:

### Scenario C — Partial Memory Detection

A desktop system has four DDR4 slots and four 8 GB modules installed (32 GB total). BIOS reports only 16 GB. Two of the four slots are populated in A1 and B1; the other two modules were added in A2 and B2 at the same time.

**Question 4-C:** List at least two possible causes for the BIOS detecting only half the installed RAM. What diagnostic steps would you perform to isolate the cause?

Your answer:

---

## Deliverables and Submission

Submit the following to Canvas by the Module 04 lab deadline:

1. Completed Part 1 identification table (Step 1) and answers to Questions 1-A through 1-C.
2. Completed Part 2 slot configuration table (Step 4) and answers to Questions 2-A through 2-D.
3. Completed Part 3 SODIMM table (Step 6) and answers to Questions 3-A and 3-B.
4. Written answers to all Part 4 scenario questions (Questions 4-A through 4-C).
5. One photograph of the RAM module(s) examined showing the notch position clearly, or an annotated reference image.

---

## Grading Rubric

| Component                                                               | Points  |
|-------------------------------------------------------------------------|---------|
| Part 1 module identification table and questions accurate and complete  | 25      |
| Part 2 dual-channel slot configuration correct and questions answered   | 25      |
| Part 3 SODIMM identification and questions complete                     | 20      |
| Part 4 scenario responses demonstrate module understanding              | 20      |
| Required photograph or annotated image submitted                        | 10      |
| **Total**                                                               | **100** |

Partial credit is awarded for answers that show correct reasoning with minor errors. No credit is awarded for blank responses.

---

## Part 9 — Challenge Exercise

These advanced steps are optional and are not included in the standard grading rubric.

### Challenge Step 1 — RAM Identification with CPU-Z

On any available Windows system, download and run CPU-Z (free at [https://www.cpuid.com/softwares/cpu-z.html](https://www.cpuid.com/softwares/cpu-z.html)):

1. Open the **Memory** tab. Record: Type (DDR4/DDR5), Channel # (Single/Dual/Quad), DRAM Frequency, and CAS Latency.
1. Open the **SPD** tab. Select each memory slot from the drop-down. For each populated slot record: Module Size, Max Bandwidth (the PC notation), Manufacturer, Part Number, and Week/Year of manufacture.
1. Calculate the advertised data rate from the PC notation: divide the PC bandwidth number by 8 to get MT/s (e.g., PC4-25600 ÷ 8 = 3200 MT/s = DDR4-3200).
1. Compare the DRAM Frequency reported in the Memory tab (which shows the actual running frequency, half the data rate) with the SPD max bandwidth. Is the RAM running at its rated XMP speed or at JEDEC base speed? If JEDEC, explain in 2–3 sentences what change would need to be made in BIOS to run the RAM at its rated speed.

### Challenge Step 2 — MemTest86 Diagnostic Run

Download MemTest86 (free at [https://www.memtest86.com/](https://www.memtest86.com/)) and create a bootable USB drive:

1. Boot the system from the MemTest86 USB drive.
1. Allow at least one full test pass (pass 0) to complete. Record the total pass count, error count, and test duration.
1. Note any errors (even a single error in one pass is significant). If errors are found, document the failing memory address range and the test number that found the error.
1. In your lab report, explain: what does a "PASS" result tell you about the physical DRAM cells, what does a single error indicate, and why is running multiple passes (not just one) important for detecting intermittent failures?

### Challenge Step 3 — Memory Bandwidth Benchmark

Using AIDA64 Free Trial ([https://www.aida64.com/downloads](https://www.aida64.com/downloads)) or the free SiSoftware Sandra Lite ([https://www.sisoftware.net/](https://www.sisoftware.net/)):

1. Run a memory bandwidth benchmark with the current RAM configuration (note whether it is single-channel or dual-channel from CPU-Z).
1. If you have access to a system where you can physically move a module to force single-channel mode, run the benchmark again after the change.
1. Record both bandwidth results and calculate the ratio (dual-channel / single-channel).
1. Write a 3–4 sentence analysis: how close is the dual-channel bandwidth to exactly double the single-channel result, why might it not be exactly 2×, and which type of workload (gaming with integrated graphics, video encoding, general office use) benefits most from the dual-channel bandwidth increase?
