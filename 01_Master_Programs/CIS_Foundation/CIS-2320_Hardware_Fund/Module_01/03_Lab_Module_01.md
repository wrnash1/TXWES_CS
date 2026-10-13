# Lab Activity: Module 01 — Introduction to PC Hardware & Safety

## Course: CIS-2320 Hardware Fundamentals

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3: Hardware

**Lab Environment:** Physical desktop PC (preferred) or virtual PC disassembly simulation. If using a physical PC, use a decommissioned or instructor-provided system — do not disassemble a live production machine.

---

## Overview

This lab has two parts:

- **Part 1** — Component identification: open a PC case (physical or virtual) and map every major internal component
- **Part 2** — Safety procedure documentation: perform and document the correct 5-step pre-work safety procedure

Both parts together simulate the physical skills assessed in A+ Domain 3 scenario questions.

---

## Part 1 — Component Identification

### Objective

Identify every major internal component, locate all relevant connectors, and produce a labeled component map. The A+ exam uses images — this lab builds the visual memory required to answer those questions correctly.

---

### 1.1 — Pre-Lab Safety Procedure

Before opening the PC case, perform the 5-step safety procedure in the correct order. Do not skip any step.

**Document each step as you perform it:**

| Step | Action | Your Notes |
|---|---|---|
| 1 | Power down OS properly | |
| 2 | Unplug AC power cord from wall outlet | |
| 3 | Press power button on PC (cord unplugged) | |
| 4 | Attach ESD wrist strap to unpainted chassis metal | |
| 5 | Open the case | |

Write a one-sentence explanation for Step 3 in your own words: why does pressing the power button after unplugging the cord matter?

---

### 1.2 — Component Map Sketch

On a blank sheet of paper (or in a diagramming tool), sketch the interior of the PC case from the side panel view. Label each of the following components with its name and draw an arrow to its physical location:

**Required labels:**

1. Motherboard
2. CPU socket and heat sink/fan assembly
3. RAM / DIMM slots (label how many slots are present and which are occupied)
4. PSU (power supply unit)
5. Storage drive(s) — label as HDD or SSD, and note the connection type (SATA or M.2)
6. GPU / graphics card (if present; if absent, note "integrated graphics")
7. PCIe x16 slot (indicate with an arrow even if the GPU is installed in it)
8. M.2 slot (if present)
9. CMOS battery
10. Front panel header connectors (small 1-2 pin connectors at the bottom of the motherboard)

Photograph or scan your sketch and save it as `lab01_component_map.jpg` (or `.png`).

---

### 1.3 — Connector Identification

Locate and identify the following physical connectors. For each one, note whether you found it and describe what it connects.

| Connector | Found? (Y/N) | Connects (from — to) |
|---|---|---|
| 24-pin ATX motherboard power | | |
| 4-pin or 8-pin CPU power | | |
| SATA data cable | | |
| SATA power cable | | |
| PCIe x16 slot | | |
| Front panel USB header | | |
| Front panel audio header | | |

**Observation question:** The 24-pin ATX connector and the 8-pin CPU power connector both come from the PSU. Why does the CPU need its own dedicated power connector rather than drawing all power through the 24-pin ATX connector?

Write 2–3 sentences answering this in your lab report.

---

### 1.4 — Socket and DIMM Identification

Answer the following about your specific system:

1. What CPU socket type is on the motherboard (if labeled — look for markings near the socket or consult the motherboard model)? _______________
2. How many DIMM slots are present? _______________
3. How many are occupied? _______________
4. Are the occupied slots the same color (dual-channel) or different colors? _______________
5. What generation of RAM is installed (look for a label on the module itself — DDR4, DDR5)? _______________

---

### 1.5 — ESD Tools Inspection

If you have access to an ESD wrist strap, perform the following:

1. Put the wrist strap on your wrist and clip the other end to the unpainted metal interior of the PC chassis.
2. Locate the resistor in the wrist strap cable. It is typically a cylindrical component inside the wrist band or inline in the cable.
3. If you have a multimeter, measure the resistance between the wrist contact and the clip end of the cable. Record your measurement: _______________ Ω
4. The expected value is approximately **1 MΩ (1,000,000 ohms)**. Does your measurement match? _______________

If no wrist strap is available, describe in 2–3 sentences how an anti-static wrist strap prevents ESD damage without posing an electrical shock risk to the technician.

---

## Part 2 — Safety Documentation

### Safety Documentation Objective

Produce a written safety checklist that you would use before working on any PC. This simulates the safety documentation that IT departments require technicians to follow.

---

### 2.1 — Write Your Safety Checklist

In your lab report, write a numbered checklist of every safety step a technician should follow before opening a PC case and handling components. Your checklist must include at minimum:

- The 5-step pre-work procedure (in correct order)
- A reminder about PSU capacitors
- A reminder about ESD protection tools and when to use them
- A reminder about sharp case edges
- A reminder about anti-static bag handling

The checklist should be written in imperative form ("Power down the system") and be specific enough that another technician could follow it without additional instruction.

---

### 2.2 — Failure Scenario Analysis

Read each scenario below. Identify the safety violation committed and explain what damage or injury could result.

**Scenario A:** A technician turns off the power strip the PC is plugged into, then immediately opens the case and begins reseating RAM.

- Safety violation: _______________
- Potential consequence: _______________

**Scenario B:** A technician unplugs the PC, opens the case, and sets the removed RAM module directly on the desk surface (no anti-static mat or bag).

- Safety violation: _______________
- Potential consequence: _______________

**Scenario C:** A technician notices the PSU is making a buzzing sound. They open the PSU case to inspect the capacitors.

- Safety violation: _______________
- Potential consequence: _______________

**Scenario D:** A technician attaches their ESD wrist strap to the painted exterior surface of the PC case.

- Safety violation: _______________
- Potential consequence: _______________

---

## Expected Observations

- The motherboard should be the largest flat board, mounted to the case with standoff screws.
- The PSU is a metal box in one corner of the case with a bundle of power cables exiting from it.
- The CPU heat sink is the largest metal block on the motherboard, directly above the CPU socket.
- DIMM slots are long, thin, parallel slots along one edge of the motherboard, with plastic clips at each end.
- SATA ports on the motherboard are small, L-shaped, grouped together and often labeled SATA0–SATA5.
- The CMOS battery is a coin cell in a circular holder on the motherboard surface.

---

## Deliverables

Submit to Canvas:

1. `lab01_component_map.jpg` — labeled sketch or photo of the PC interior with all 10 components identified
2. `lab01_report.pdf` or `.docx` — lab report containing:
   - Completed 1.1 safety procedure table with your Step 3 explanation
   - Completed 1.3 connector identification table with your CPU power observation answer
   - Completed 1.4 socket and DIMM identification answers
   - 1.5 ESD strap measurement or written explanation (if no strap available)
   - 2.1 safety checklist
   - 2.2 failure scenario analysis (all four scenarios)

---

## Grading Rubric

| Component | Points |
|---|---|
| Component map — all 10 labels correct | 30 |
| Connector identification table — complete and accurate | 20 |
| Socket/DIMM identification — answered fully | 15 |
| Safety checklist — complete, in order, imperative form | 20 |
| Failure scenario analysis — all four correct | 15 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

These advanced steps are optional for students seeking additional depth. They are not graded but develop skills directly tested in A+ performance-based questions.

### Challenge Step 1 — PSU Voltage Rail Verification

Using a digital multimeter set to DC voltage mode and a PSU tester (or a paperclip ATX bench-start jumper with the PSU completely disconnected from the motherboard):

1. Short pin 16 (PS_ON) to any ground pin on the 24-pin ATX connector to turn on the PSU without a motherboard connected (ATX bench test).
1. Probe the following pins on the 24-pin connector and record the measured voltages against expected values:

| Rail | Expected | Your Measurement |
|---|---|---|
| +12V (yellow wire) | +12V ± 5% | |
| +5V (red wire) | +5V ± 5% | |
| +3.3V (orange wire) | +3.3V ± 5% | |
| −12V (blue wire) | −12V ± 10% | |
| +5VSB (purple wire, pin 9) | +5V ± 5% | |

1. Document which rails were within tolerance and which (if any) fell outside the acceptable range. A rail more than 5–10% outside spec under no load indicates a failing PSU.

**Safety note:** Perform this only with a decommissioned or lab-designated PSU. Never probe a PSU that is connected to a live motherboard with this method.

### Challenge Step 2 — ESD Strap Resistance Comparison

1. Obtain two wrist straps: one standard ESD strap (with 1 MΩ resistor) and one inexpensive "heel grounder" or strap of unknown quality.
2. Using a multimeter on the resistance (Ω) setting, measure the end-to-end resistance of each strap cable.
3. Record both values and determine whether each strap provides adequate protection (acceptable range: 800 kΩ – 1.2 MΩ for the standard strap).
4. In your lab report, explain why a strap with zero resistance (a simple wire) would be more dangerous to the technician than a strap with 1 MΩ resistance, even though it would drain static faster.

### Challenge Step 3 — Dual-Channel vs. Single-Channel RAM Benchmark

If you have access to a Windows or Linux machine with at least two RAM slots occupied:

1. Install both RAM modules in matching-color (dual-channel) slots per the motherboard manual.
2. Run a memory bandwidth benchmark using **HWiNFO64** (free, [https://www.hwinfo.com/](https://www.hwinfo.com/)) or the built-in Windows Memory Diagnostic. Record the reported memory clock speed and channel configuration.
3. Move one RAM module to an adjacent slot to force single-channel mode.
4. Re-run the benchmark. Record the new values.
5. Compare the results and write a 3–4 sentence explanation of why dual-channel mode increases memory bandwidth and what real-world performance scenarios benefit most from it (e.g., integrated graphics systems where the GPU shares system RAM bandwidth).
