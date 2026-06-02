# Lab Activity: Module 06 - Power Supplies and System Cooling

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Certification Alignment:** Domain 3.5 — Install and configure motherboards, CPUs, and add-on cards | Domain 5.2 — Troubleshoot problems related to motherboards, RAM, CPUs, and power

**Estimated Completion Time:** 60-75 minutes

**Submission:** Upload your completed lab worksheet (PDF or Word document) to the Canvas Lab 06 assignment by the posted deadline.

---

### Lab Overview

This lab develops three skills assessed on the CompTIA A+ Core 1 exam: PSU connector identification, system power requirements calculation, and case airflow analysis. You will work from connector descriptions, component specification tables, and annotated case diagrams. No physical hardware is required for this lab, though students with access to a PC or loose PSU cables are encouraged to examine them alongside the exercises.

There are three parts:

- Part 1 — PSU Connector Identification
- Part 2 — System Wattage Calculation
- Part 3 — Case Airflow Diagram Analysis

Complete all three parts and answer all observation questions before submitting.

---

### Safety and Handling Notes (for students working with physical hardware)

If you have access to a physical PSU or open PC for this exercise, observe the following:

- A PSU retains potentially lethal charge in its capacitors for several minutes after being unplugged from the wall. Never open a PSU housing.
- Always power off and unplug the system before connecting or disconnecting any PSU cable.
- Do not short any PSU connector pins together — this can damage the PSU or connected components.
- Use an antistatic wrist strap when handling any motherboard, RAM, or GPU.

---

## Part 1 — PSU Connector Identification

### Part 1 Overview

Below are descriptions of eight PSU connectors and components. For each item, complete the identification table by recording the connector name, its pin count, the voltage rails it carries, and the specific component or board location it powers.

Use your reading guide connector table and video lecture notes as references.

### Part 1 Identification Table

| Item # | Item Description | Connector Name | Pin Count | Voltage Rails Carried | Component or Location It Powers |
|---|---|---|---|---|---|
| 1 | The largest connector in the cable bundle; plugs into a wide header near the center-right of the motherboard; has a locking clip; provides standby power and the Power Good signal | | | | |
| 2 | Plugs into a small header near the top-left corner of the motherboard; exclusively supplies power to the processor's voltage regulators; system will not POST if missing | | | | |
| 3 | A 6-pin connector from the PSU; connects directly to the graphics card; provides up to 75W of auxiliary power beyond what the PCIe slot supplies | | | | |
| 4 | An 8-pin connector from the PSU; connects directly to the graphics card; provides up to 150W of auxiliary power | | | | |
| 5 | A 15-pin L-shaped connector; powers spinning hard drives and SATA SSDs; carries three voltage rails | | | | |
| 6 | A large 4-pin connector with a rectangular body; legacy power connector from the IDE era; sometimes used for older fans or LED controllers | | | | |
| 7 | An 8-pin EPS connector on a PSU that splits into two 4-pin sections; allows backward compatibility with motherboards that only have a 4-pin CPU header | | | | |
| 8 | A PSU where the 24-pin ATX and 8-pin EPS cables are permanently attached but all SATA, PCIe, and Molex cables are detachable via ports on the PSU body | | | | |

### Part 1 Observation Questions

Answer each question in 2-4 complete sentences.

**Observation 1A:** Items 1 and 2 both provide power to components on the motherboard, but they are separate connectors. Explain why the CPU requires its own dedicated power connector rather than receiving all power through the 24-pin ATX connector.

*Your answer:*

---

**Observation 1B:** A technician builds a new PC and powers it on for the first time. All case fans spin briefly, then the system immediately shuts off. The 24-pin ATX connector is fully seated. What is the most likely missing or incorrectly connected cable, and how would the technician verify this?

*Your answer:*

---

**Observation 1C:** A customer asks why they should pay more for a fully modular PSU (Item 8) instead of a non-modular unit of the same wattage and efficiency tier. Explain two technical benefits of the modular design beyond aesthetics.

*Your answer:*

---

## Part 2 — System Wattage Calculation

### Part 2 Overview

Using the wattage calculation method from the reading guide, calculate the recommended PSU wattage for each of the three system builds described below. Show all arithmetic. Select the appropriate PSU from the standard wattage options provided.

Standard PSU wattage options available: 400W, 500W, 550W, 600W, 650W, 750W, 850W, 1000W

### Build A: Office Workstation

| Component | Specified Power Draw |
|---|---|
| CPU (Intel Core i5, low-power) | 65W TDP |
| GPU (integrated graphics only — no discrete GPU) | 0W additional |
| RAM (2 sticks DDR4) | 8W total |
| 1 SATA SSD | 3W |
| 1 SATA HDD | 8W |
| Motherboard | 35W |
| 3 case fans | 9W total |

Show your calculation below:

- Estimated system load: _____ W
- Estimated load x 1.25 (25% headroom): _____ W
- Selected PSU from standard options: _____ W
- Justification (1-2 sentences explaining your selection):

---

### Build B: Gaming PC

| Component | Specified Power Draw |
|---|---|
| CPU (AMD Ryzen 7, mid-high tier) | 105W TDP |
| GPU (NVIDIA mid-range) | 200W TDP |
| RAM (4 sticks DDR5) | 20W total |
| 2 NVMe SSDs | 10W total |
| 1 SATA HDD | 9W |
| Motherboard | 45W |
| 6 case fans | 18W total |
| AIO liquid cooler pump | 5W |

Show your calculation below:

- Estimated system load: _____ W
- Estimated load x 1.25 (25% headroom): _____ W
- Selected PSU from standard options: _____ W
- Justification (1-2 sentences explaining your selection):

---

### Build C: High-End Content Creation Workstation

| Component | Specified Power Draw |
|---|---|
| CPU (Intel Core i9, HEDT platform) | 253W TDP |
| GPU (high-end professional GPU) | 350W TDP |
| RAM (8 sticks DDR5 ECC) | 40W total |
| 4 NVMe SSDs | 24W total |
| Motherboard (HEDT platform) | 70W |
| 8 case fans | 24W total |
| AIO liquid cooler pump | 6W |
| PCIe capture card | 15W |

Show your calculation below:

- Estimated system load: _____ W
- Estimated load x 1.25 (25% headroom): _____ W
- Selected PSU from standard options: _____ W
- Justification (1-2 sentences explaining your selection):

---

### Part 2 Observation Questions

**Observation 2A:** For Build B, the gaming PC, a classmate suggests purchasing a 1000W PSU because "more wattage is always safer." Using the 80 Plus efficiency principle, explain why running a 1000W PSU in the Build B system may actually be less efficient than the PSU you selected.

*Your answer:*

---

**Observation 2B:** The Build C workstation owner decides to add a second identical high-end GPU in a dual-GPU configuration, adding another 350W of GPU TDP. Recalculate the minimum recommended PSU wattage for the updated configuration and select the appropriate PSU from the standard options.

Show your calculation:

- Updated estimated system load: _____ W
- Updated load x 1.25: _____ W
- Updated PSU selection: _____ W

---

## Part 3 — Case Airflow Diagram Analysis

### Part 3 Overview

The diagram below describes a mid-tower ATX case with six installed fans. Some fans are installed correctly; others are installed in the wrong orientation or in an incorrect position. For each fan listed in the table, identify whether the configuration is correct or incorrect, state what the airflow direction actually is in the described configuration, and if incorrect, describe what the correct configuration should be.

### Case Fan Configuration Description

The case has the following fans installed:

- Fan 1: Front panel, bottom position — label arrow pointing toward the front of the case (outward through the mesh)
- Fan 2: Front panel, top position — label arrow pointing toward the interior of the case (inward)
- Fan 3: Rear panel — label arrow pointing toward the interior of the case (inward)
- Fan 4: Top panel, front position — label arrow pointing upward (outward through the top vents)
- Fan 5: Top panel, rear position — label arrow pointing downward (inward through the top vents)
- Fan 6: Bottom panel — label arrow pointing downward (outward through the bottom vents)

### Part 3 Airflow Analysis Table

| Fan # | Position | Described Orientation | Correct or Incorrect? | Actual Airflow Direction | Correct Configuration (if incorrect) |
|---|---|---|---|---|---|
| 1 | Front bottom | Arrow pointing outward | | | |
| 2 | Front top | Arrow pointing inward | | | |
| 3 | Rear | Arrow pointing inward | | | |
| 4 | Top front | Arrow pointing upward (outward) | | | |
| 5 | Top rear | Arrow pointing downward (inward) | | | |
| 6 | Bottom | Arrow pointing downward (outward) | | | |

### Part 3 Observation Questions

**Observation 3A:** Based on your analysis table, describe the overall airflow problem this case configuration creates. Specifically explain how the incorrectly oriented fans disrupt the front-to-back, bottom-to-top airflow path and what thermal consequence this would have for the CPU and GPU.

*Your answer:*

---

**Observation 3B:** After correcting all fan orientations, the technician counts 4 intake fans and 2 exhaust fans. Is this a positive-pressure or negative-pressure configuration? Explain the dust-accumulation implication of this configuration and whether it is generally preferred or not recommended.

*Your answer:*

---

### Deliverables and Submission

Submit one document (PDF or Word) containing:

1. Completed Part 1 Identification Table with all eight items filled in
2. Answers to all three Part 1 Observation Questions
3. Completed Part 2 wattage calculations for all three builds, with arithmetic shown
4. Answers to both Part 2 Observation Questions (including the recalculation in 2B)
5. Completed Part 3 Airflow Analysis Table
6. Answers to both Part 3 Observation Questions

Upload to the Canvas Lab 06 assignment portal before the posted deadline.

---

### Grading Rubric

| Section | Points Possible | Criteria |
|---|---|---|
| Part 1 — Identification Table (8 items) | 16 pts | 2 pts per item: connector name correct (1 pt) + pin count or voltage correct (1 pt) |
| Part 1 — Observation Questions (3) | 12 pts | 4 pts each: technically accurate, complete sentences, correct terminology |
| Part 2 — Wattage Calculations (3 builds) | 18 pts | 6 pts each: correct load sum (2), correct headroom calculation (2), appropriate PSU selection (2) |
| Part 2 — Observation Questions (2) | 8 pts | 4 pts each: demonstrates understanding of efficiency and wattage planning |
| Part 3 — Airflow Analysis Table (6 fans) | 18 pts | 3 pts per fan: correct/incorrect determination (1), actual airflow direction (1), correct fix stated if needed (1) |
| Part 3 — Observation Questions (2) | 8 pts | 4 pts each: accurately describes airflow disruption and pressure concepts |
| **Total** | **80 pts** | |

---

### Troubleshooting Reference

If you are unsure about a connector, wattage method, or airflow concept, refer to the following resources before submitting:

- Reading Guide Section 1 (Glossary), Section 2 (Connector Table), Section 4 (Wattage Calculation), and Section 5 (Airflow Reference)
- Professor Messer's CompTIA A+ Core 1 free course at [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- CompTIA A+ exam objectives Domain 3.5 at [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)
