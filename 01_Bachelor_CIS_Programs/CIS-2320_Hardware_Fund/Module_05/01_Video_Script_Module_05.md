# Video Script: Module 05 - Storage Devices

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Estimated Duration:** 22-24 minutes

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.1 (Given a scenario, install and configure storage devices) and Domain 5.3 (Given a scenario, troubleshoot hard drives and RAID arrays)

**Recorded by:** Professor Nash | Texas Wesleyan University

---

### Production Notes

SHOW COMPONENT cues in this script:

- [SHOW COMPONENT: 3.5-inch HDD next to 2.5-inch SATA SSD — side-by-side size comparison]
- [SHOW COMPONENT: M.2 2280 NVMe SSD held up to camera, B+M key notch visible]
- [SHOW COMPONENT: M.2 slot on motherboard — show the M-key and B-key notch positions]
- [SHOW COMPONENT: SATA data cable (7-pin flat) and SATA power cable (15-pin L-shaped) labeled]
- [SHOW COMPONENT: RAID 0, 1, 5, 10 diagrams on slides — one slide per RAID level]

Key Exam Traps to call out explicitly:

- "M.2 NVMe and M.2 SATA are NOT interchangeable — the slot looks the same but the protocol is different."
- "RAID 0 has ZERO fault tolerance. Zero. One drive dies and everything is gone."
- "RAID 5 needs THREE drives minimum — you cannot build RAID 5 with two drives."
- "RAID 10 requires FOUR drives minimum and can survive one drive failure per mirrored pair."

Safety Notes:

- Hold all drives by their edges — never touch the circuit board or platters (HDDs)
- Ground yourself with an antistatic wrist strap before handling any drive
- NVMe drives are fragile — the M.2 connector is small; do not force the drive into the slot

---

### [00:00 - 02:30] Section 1: Introduction and Why Storage Matters

[INSTRUCTOR ON CAMERA — title card visible: "Module 05: Storage Devices"]

"Welcome back, everyone. I'm Professor Nash, and today we are covering one of the most heavily tested hardware topics on the CompTIA A+ Core 1 exam: Storage Devices.

Here is why this module matters beyond the exam. Every single computer — whether it's your laptop, a gaming rig, or a server in a data center — needs to store data somewhere permanently. When you power that machine off, the operating system, your files, your applications — they all live on a storage device. Understanding what types exist, how fast they are, how they connect, and how to protect data with RAID is a fundamental competency for any IT technician.

[PAUSE — look directly at camera]

By the end of this lesson you will be able to identify an HDD, a SATA SSD, and an NVMe SSD by sight, explain the performance difference between them, identify the physical form factors and connectors involved, and explain the four main RAID levels. Let's get into it.

Exam Tip: Domain 3.1 on the A+ Core 1 exam asks you to identify storage types and explain their characteristics. Expect both knowledge questions and scenario-based questions where you choose the best drive type for a given situation."

---

### [02:30 - 08:00] Section 2: Drive Types — HDD, SATA SSD, and NVMe

[SLIDE: "The Three Storage Tiers"]

"Let's compare the three main drive types you need to know, starting with the traditional hard disk drive.

#### Hard Disk Drive

[SHOW COMPONENT: 3.5-inch HDD next to 2.5-inch SATA SSD — side-by-side size comparison]

A hard disk drive stores data on spinning magnetic platters. A read/write head floats micrometers above those platters and magnetizes tiny sections to represent ones and zeros. Because it has moving parts, seek time — the time it takes the head to physically move to the correct location — is the bottleneck. Sequential read speeds on a modern 7200 RPM desktop HDD run about 100 to 160 megabytes per second. Random access is much slower.

HDDs come in two form factors: 3.5-inch for desktops and 2.5-inch for laptops. They connect via SATA — you need a 7-pin SATA data cable and a 15-pin SATA power cable from the PSU.

Why would you still buy an HDD in 2025? Price per gigabyte. A 4 TB HDD costs a fraction of a 4 TB SSD. For bulk storage and backups, HDDs are still the economical choice.

[PAUSE]

#### SATA SSD

A SATA SSD replaces spinning platters with NAND flash memory chips — solid-state, no moving parts. It connects via the same SATA interface and uses the same 7-pin data and 15-pin power connectors as an HDD. This makes it a direct drop-in upgrade in most laptops and desktops.

Performance is dramatically better: sequential reads hit about 500 to 550 megabytes per second — right at the ceiling of the SATA III interface. The SATA interface itself is the bottleneck. No matter how fast the NAND chips inside could theoretically run, SATA III caps them at 6 Gbps, which works out to about 550 MB/s in real-world usage.

SATA SSDs come in two physical shapes: the 2.5-inch drive (looks like a laptop hard drive) and the M.2 form factor. That M.2 shape is where things get confusing on the exam — and I'll address that in just a moment.

[PAUSE]

#### NVMe SSD

[SHOW COMPONENT: M.2 2280 NVMe SSD held up to camera, B+M key notch visible]

NVMe stands for Non-Volatile Memory Express. It is a communication protocol specifically designed for flash storage, and it communicates over the PCIe bus — not the SATA bus. PCIe has much higher bandwidth than SATA. A PCIe 3.0 x4 NVMe drive achieves around 3,500 MB/s sequential read. A PCIe 4.0 x4 NVMe drive reaches 5,000 to 7,000 MB/s. That is ten to fourteen times faster than a SATA SSD.

NVMe drives typically use the M.2 physical form factor. The most common size is M.2 2280 — that means 22 mm wide and 80 mm long.

[SHOW COMPONENT: M.2 slot on motherboard — show the M-key and B-key notch positions]

Now — here is the critical exam trap. An M.2 slot on a motherboard can support NVMe OR SATA, depending on the motherboard. The physical connector looks the same. The drives look almost the same. But the protocols are completely different. You cannot put an NVMe drive into a SATA-only M.2 slot and expect it to work. Always check the motherboard specification before purchasing a drive.

The key notch is one visual clue: an M-key notch supports NVMe; a B+M key can support either SATA or NVMe. But the slot notch alone does not guarantee protocol support — the motherboard firmware must also support NVMe in that slot.

Exam Tip: The A+ exam will give you a scenario with an M.2 slot and ask whether an NVMe drive is compatible. Always look for the motherboard specification in the scenario. Never assume M.2 equals NVMe."

---

### [08:00 - 12:30] Section 3: Form Factors and Connectors

[SLIDE: "Identifying Drives and Cables"]

"Let's talk about physical form factors and the cables that connect these drives.

#### 3.5-inch Form Factor

Desktop HDDs are 3.5 inches wide. They mount into a drive bay in the case, usually with four screws on the sides or bottom. They draw power on both the 5V and 12V rails — which is why they use the 15-pin SATA power connector (which carries 3.3V, 5V, and 12V lines).

#### 2.5-inch Form Factor

Laptop HDDs and SATA SSDs use the 2.5-inch form factor. These use the same 7-pin SATA data and 15-pin SATA power connectors as 3.5-inch drives. However, 2.5-inch drives run only on 5V power — they do not use the 12V rail. In desktop cases, 2.5-inch drives often require a bracket adapter to fit a 3.5-inch bay.

[SHOW COMPONENT: SATA data cable (7-pin flat) and SATA power cable (15-pin L-shaped) labeled]

The 7-pin SATA data cable is a flat, thin cable with an L-shaped connector at each end. One end goes to the drive, the other to a SATA port on the motherboard. The 15-pin SATA power cable comes from the PSU and has an L-shaped connector that is noticeably wider. These connectors are keyed — they only insert one way.

#### M.2 Form Factor

The M.2 form factor is a small circuit board that plugs directly into an M.2 slot on the motherboard — no cables needed. The drive sits at an angle (usually 30 degrees above the motherboard surface), then you press it flat and secure it with a single retaining screw. That screw is critical — without it, vibration can cause the drive to unseat over time.

M.2 drives come in different lengths: 2230, 2242, 2260, and 2280 — the last two digits are the length in millimeters. The 2280 (80mm) is by far the most common for consumer NVMe drives.

Exam Tip: On the A+ exam, both 2.5-inch and 3.5-inch drives use SATA data and power connectors. M.2 drives use no external cables. NVMe drives always use M.2 or PCIe add-in card form factors — never a 2.5-inch form factor."

---

### [12:30 - 19:00] Section 4: RAID Levels — 0, 1, 5, and 10

[SLIDE: "RAID — Redundant Array of Independent Disks"]

"RAID stands for Redundant Array of Independent Disks. The idea is to combine multiple physical drives so that the operating system sees one logical volume. RAID configurations can increase performance, add redundancy against drive failure, or both. Let's go through the four levels tested on the A+ exam.

[SHOW COMPONENT: RAID 0 diagram on slide]

#### RAID 0 — Striping

RAID 0 splits data across two or more drives in stripes. Drive 1 gets stripe 1, Drive 2 gets stripe 2, and so on. Because data is written and read from multiple drives simultaneously, sequential performance improves significantly.

But — and this is critical — RAID 0 has zero fault tolerance. Zero. If one drive in the array fails, all data across every drive is lost because each piece of data is split across multiple drives. This is not a backup solution. This is not redundancy. RAID 0 is pure performance.

[PAUSE — let this land]

Minimum drives: 2. Fault tolerance: none. Capacity: 100% of all drives. Use case: scratch drives, video editing workstations that need speed and replace data frequently.

[SHOW COMPONENT: RAID 1 diagram on slide]

#### RAID 1 — Mirroring

RAID 1 writes identical data to two drives simultaneously — one is the mirror of the other. If Drive 1 fails, Drive 2 contains a complete copy of all data. The system can continue operating in degraded mode until you replace the failed drive.

Minimum drives: 2. Fault tolerance: 1 drive failure. Usable capacity: 50% of total capacity (two 1 TB drives give you 1 TB of usable space). Use case: small business servers, boot drives where data integrity is critical.

Some RAID controllers can read from both mirror drives simultaneously, improving read performance. Write performance is the same as a single drive because every write must be duplicated to both drives.

[SHOW COMPONENT: RAID 5 diagram on slide]

#### RAID 5 — Striping with Distributed Parity

RAID 5 stripes data across three or more drives and also distributes parity information across all drives. Parity is a mathematical checksum that can be used to reconstruct the data from a failed drive. The parity is not stored on one dedicated drive — it rotates across all drives.

If one drive fails, the controller uses the parity data on the remaining drives to reconstruct the missing data in real time. The array stays online — in degraded mode — until the failed drive is replaced. After replacement, the controller rebuilds the lost drive's data.

Minimum drives: 3. Fault tolerance: 1 drive failure. Usable capacity: total capacity minus the equivalent of one drive. For example, three 1 TB drives give 2 TB of usable space. Use case: file servers, NAS devices, database servers where both redundancy and capacity efficiency matter.

[PAUSE]

[SHOW COMPONENT: RAID 10 diagram on slide]

#### RAID 10 — Striping plus Mirroring (RAID 1+0)

RAID 10 combines RAID 1 mirroring and RAID 0 striping. You create two or more mirrored pairs, then stripe data across those pairs. You get the redundancy of RAID 1 and the performance of RAID 0.

Minimum drives: 4 (two mirrored pairs). Fault tolerance: one drive per mirrored pair can fail — so if you have two pairs, up to two drives can fail as long as both failures are in different pairs. Usable capacity: 50% of total drives. Use case: high-transaction databases, production application servers where both speed and redundancy are required.

[PAUSE — summary]

Here is the cheat sheet for the exam:

- RAID 0: Fast, no redundancy, minimum 2 drives
- RAID 1: Mirror, 1 drive can fail, minimum 2 drives, 50% capacity
- RAID 5: Striping with parity, 1 drive can fail, minimum 3 drives, lose 1 drive worth of capacity
- RAID 10: Striped mirrors, 1 per pair can fail, minimum 4 drives, 50% capacity

Exam Tip: The most common RAID scenario question on the A+ exam describes a failed drive and asks what happens. Know which RAID levels survive one failure (1, 5, 10) and which do not (0)."

---

### [19:00 - 22:30] Section 5: Lab Preview and Exam Wrap-Up

[SLIDE: "Module 05 Lab Overview"]

"For this week's lab, you are going to do three things.

First, you will complete a drive identification table — looking at photographs of drives and connectors and matching them to their correct type, interface, and form factor. This is exactly the kind of identification task that appears on the A+ performance-based questions.

Second, you will work through a RAID planning scenario. Given a set of organizational requirements — a certain number of drives, a performance goal, and a fault tolerance requirement — you will select the appropriate RAID level, calculate usable capacity, and explain your reasoning. This mirrors real-world decision-making that technicians face every day.

Third, you will complete a connector labeling exercise, identifying SATA data, SATA power, and M.2 connections on a diagram.

[PAUSE]

Before I let you go, let me remind you of the key exam points from this module:

One — M.2 is a form factor, not a protocol. NVMe and SATA M.2 are different. Check the motherboard spec.

Two — SATA III tops out at about 550 MB/s. Any drive on a SATA interface — regardless of form factor — is capped at that speed.

Three — RAID 0 equals zero fault tolerance. Do not confuse the zero in the name with zero problems.

Four — RAID 5 minimum is three drives. RAID 10 minimum is four drives. The exam will try to trick you with two-drive RAID 5 scenarios — it is not valid.

Five — RAID 1, 5, and 10 all survive one drive failure. RAID 0 does not survive any failure.

[OUTRO — instructor on camera]

That covers Module 05. Complete the reading guide and lab before attempting the quiz. I will see you in the discussion board — post your initial response by Wednesday night. Take care, everyone."

---

### End Card

- Complete the Reading Guide before the lab
- Submit Lab 05 via Canvas by the posted deadline
- Initial Discussion Post due Wednesday at 11:59 PM
- Quiz 05 available after the lab submission window closes
- Office hours: see Canvas for current schedule

---

### Additional Resources

- Professor Messer CompTIA A+ Core 1 Free Course (Storage Devices): [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- Professor Messer CompTIA A+ Study Notes (220-1101): [https://www.professormesser.com/](https://www.professormesser.com/)
- CompTIA A+ Exam Objectives (220-1101): [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)
