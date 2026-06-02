# Lab Activity: Module 05 - Storage Devices

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Certification Alignment:** Domain 3.1 — Install and configure storage devices | Domain 5.3 — Troubleshoot hard drives and RAID arrays

**Estimated Completion Time:** 60-75 minutes

**Submission:** Upload your completed lab worksheet (PDF or Word document) to the Canvas Lab 05 assignment by the posted deadline.

---

### Lab Overview

This lab develops three skills that are directly assessed on the CompTIA A+ Core 1 performance-based exam questions: physical drive and connector identification, RAID level selection and capacity planning, and system diagram annotation. You will work from labeled reference photographs and scenario descriptions — no physical hardware is required, though students with access to PC components are encouraged to examine them alongside the worksheet.

There are three parts:

- Part 1 — Drive and Connector Identification (identification table)
- Part 2 — RAID Planning Scenarios (decision and calculation exercises)
- Part 3 — System Diagram Annotation (connector labeling)

Complete all three parts and answer all observation questions before submitting.

---

### Safety and Handling Notes (for students working with physical hardware)

If you have access to physical drives or a PC for this exercise, observe the following:

- Handle all drives by their edges; do not touch exposed circuit board components or HDD platters
- Use an antistatic wrist strap or touch a grounded metal surface before handling any drive or motherboard
- Never force an M.2 drive into a slot — the connector is small and the board can crack if misaligned
- Power off and unplug any system before installing or removing drives

---

## Part 1 — Drive and Connector Identification

### Part 1 Overview

Below are descriptions of eight storage-related items. For each item, fill in the identification table by recording the drive or connector type, the interface or protocol it uses, the form factor or physical dimensions, and one distinguishing physical characteristic that would allow you to identify it in the field.

Use your reading guide, video lecture notes, and Professor Messer's study materials as references.

### Part 1 Identification Table

| Item # | Item Description | Drive/Connector Type | Interface or Protocol | Form Factor or Size | One Distinguishing Physical Feature |
|---|---|---|---|---|---|
| 1 | A 3.5-inch drive with a spinning platter motor visible through the vent hole on its base, draws 5V and 12V power | | | | |
| 2 | A 2.5-inch drive with no moving parts, connects with a flat 7-pin cable and a 15-pin L-shaped power cable | | | | |
| 3 | A small circuit board approximately 80mm long and 22mm wide, plugs directly into the motherboard, no external cables, M-key notch | | | | |
| 4 | A flat, thin cable with L-shaped connectors at both ends, 7 pins, connects a drive to a motherboard port | | | | |
| 5 | A wider L-shaped connector with 15 pins, originates from the PSU, carries 3.3V, 5V, and 12V rails | | | | |
| 6 | A small circuit board approximately 42mm long, B+M-key notch, installed in a laptop's M.2 slot, uses the SATA protocol | | | | |
| 7 | A large 4-pin connector from an older PSU, used for legacy accessories and some case fans, not used with modern SATA drives | | | | |
| 8 | A drive that achieves 5,500 MB/s sequential read speed, uses PCIe 4.0 x4, installs without cables into the motherboard | | | | |

### Part 1 Observation Questions

Answer each question in 2-4 complete sentences.

**Observation 1A:** Items 3 and 6 are both M.2 form factor drives. Explain how a technician would determine whether each drive uses SATA or NVMe before purchasing a replacement drive for a laptop.

*Your answer:*

---

**Observation 1B:** Items 4 and 5 are both used to connect a 2.5-inch SATA SSD. Explain the difference between them, including why the connectors cannot be accidentally swapped.

*Your answer:*

---

**Observation 1C:** A customer brings in a PC complaining that a newly installed M.2 drive is not being detected in BIOS. The drive is physically secured with the retaining screw and fully seated in the slot. List two possible causes — other than a defective drive — and explain how a technician would investigate each.

*Your answer:*

---

## Part 2 — RAID Planning Scenarios

### Part 2 Overview

Read each business scenario below. For each scenario, select the most appropriate RAID level from the options provided, calculate the usable storage capacity, state the maximum number of drives that can fail without data loss, and justify your choice in 3-5 sentences. Show all capacity calculations.

### Scenario A: Small Business File Server

A small accounting firm has purchased four 2 TB hard drives for a new file server. Their primary requirement is data redundancy — they cannot afford to lose client tax records. Read performance is more important than write performance because staff will frequently retrieve documents. Budget does not allow more than 50% of raw capacity to be reserved for redundancy overhead.

RAID level options: RAID 0, RAID 1, RAID 5, RAID 10

| Field | Your Answer |
|---|---|
| Selected RAID Level | |
| Usable Storage Capacity (show calculation) | |
| Maximum Drives That Can Fail | |
| Justification (3-5 sentences) | |

### Scenario B: Video Production Workstation

A video editor has two 4 TB NVMe drives and needs maximum sequential read and write throughput for editing 8K RAW footage. The raw footage is backed up nightly to an external NAS, so on-system redundancy is not required. The editor's primary concern is performance, not data protection on the workstation itself.

RAID level options: RAID 0, RAID 1, RAID 5, RAID 10

| Field | Your Answer |
|---|---|
| Selected RAID Level | |
| Usable Storage Capacity (show calculation) | |
| Maximum Drives That Can Fail | |
| Justification (3-5 sentences) | |

### Scenario C: Database Server with High Availability Requirement

A hospital IT department is configuring a database server for patient scheduling records. They have purchased six 1 TB SSDs. They need both high read/write performance and fault tolerance, and are willing to accept 50% capacity overhead to achieve both. The server must continue operating if one drive fails.

RAID level options: RAID 0, RAID 1, RAID 5, RAID 10

| Field | Your Answer |
|---|---|
| Selected RAID Level | |
| Usable Storage Capacity (show calculation) | |
| Maximum Drives That Can Fail | |
| Justification (3-5 sentences) | |

### Part 2 Observation Questions

**Observation 2A:** In Scenario A, why is RAID 10 not the optimal choice even though it provides both redundancy and performance? Consider the capacity overhead.

*Your answer:*

---

**Observation 2B:** A colleague suggests using RAID 5 for Scenario C's database server because it uses capacity more efficiently than RAID 10. Describe one reason a database administrator might still prefer RAID 10 over RAID 5 for a high-transaction database, even at the cost of 50% capacity.

*Your answer:*

---

## Part 3 — System Diagram Annotation

### Part 3 Overview

The diagram below represents a simplified PC system with a motherboard, PSU, and three installed storage devices. Label each numbered connection point with the correct cable or interface name and the drive type it connects. Then answer the observation questions.

### Diagram Description

Refer to the following diagram description (your instructor may provide a printed or digital version; if not, sketch this from the description):

The system contains:

- A motherboard with two SATA ports (labeled Port A and Port B), one M.2 slot (labeled Slot C), and a PCIe x4 slot
- A PSU with multiple cable outputs
- A 3.5-inch HDD installed in a drive bay (labeled Drive 1)
- A 2.5-inch SATA SSD installed in a second bay (labeled Drive 2)
- An M.2 NVMe SSD installed in Slot C (labeled Drive 3)

### Part 3 Labeling Table

For each numbered connection point in the diagram, record the cable or interface type, what it connects, and any relevant specification.

| Connection Point | Cable or Interface Name | Connects | Specification (voltage, pin count, protocol, etc.) |
|---|---|---|---|
| 1. Cable from PSU to Drive 1 | | | |
| 2. Cable from motherboard Port A to Drive 1 | | | |
| 3. Cable from PSU to Drive 2 | | | |
| 4. Cable from motherboard Port B to Drive 2 | | | |
| 5. Connection from Drive 3 to Slot C | | | |
| 6. Physical fastener securing Drive 3 in Slot C | | | |

### Part 3 Observation Questions

**Observation 3A:** Drive 3 (the NVMe SSD) is listed as achieving 3,200 MB/s sequential read. Drive 2 (the SATA SSD) achieves 520 MB/s sequential read. Explain why Drive 2 cannot achieve Drive 3's speed even if it were installed in the same M.2 slot.

*Your answer:*

---

**Observation 3B:** A technician accidentally installs Drive 1 (3.5-inch HDD) into a case that only has 2.5-inch drive bays and no adapter brackets. No cables are changed. Describe what physical problem this creates and how a technician would resolve it without purchasing a new drive.

*Your answer:*

---

### Deliverables and Submission

Submit one document (PDF or Word) containing:

1. Completed Part 1 Identification Table with all eight items filled in
2. Answers to all three Part 1 Observation Questions
3. Completed Part 2 RAID Planning tables for all three scenarios, including capacity calculations
4. Answers to both Part 2 Observation Questions
5. Completed Part 3 Labeling Table
6. Answers to both Part 3 Observation Questions

Upload to the Canvas Lab 05 assignment portal before the posted deadline.

---

### Grading Rubric

| Section | Points Possible | Criteria |
|---|---|---|
| Part 1 — Identification Table (8 items) | 16 pts | 2 pts per item: drive type correct (1 pt) + physical feature correct (1 pt) |
| Part 1 — Observation Questions (3) | 12 pts | 4 pts each: accurate technical content, complete sentences, correct terminology |
| Part 2 — RAID Scenarios (3) | 24 pts | 8 pts each: correct RAID level (2), correct capacity calculation (3), fault tolerance correct (1), justification demonstrates understanding (2) |
| Part 2 — Observation Questions (2) | 8 pts | 4 pts each: demonstrates understanding of RAID trade-offs |
| Part 3 — Labeling Table (6 items) | 12 pts | 2 pts per item: cable/interface name correct (1 pt) + specification correct (1 pt) |
| Part 3 — Observation Questions (2) | 8 pts | 4 pts each: accurate technical explanation |
| **Total** | **80 pts** | |

---

### Troubleshooting Reference

If you are unsure about a drive type or connector, refer to the following resources before submitting:

- Reading Guide Section 2 (Drive Comparison Table) and Section 4 (Connector Identification Reference)
- Professor Messer's CompTIA A+ Core 1 free course storage videos at [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- CompTIA A+ exam objectives Domain 3.1 at [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)
