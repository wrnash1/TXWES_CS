# Reading Guide: Module 05 - Storage Devices

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


## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Certification Domain:** 3.1 — Given a scenario, install and configure storage devices | 5.3 — Given a scenario, troubleshoot hard drives and RAID arrays

---

### Introduction

Welcome to Module 05 — Storage Devices. This module covers the full range of storage technologies used in modern PCs, from traditional spinning hard drives to high-speed NVMe SSDs, as well as the RAID configurations used to provide redundancy or performance in multi-drive systems. These topics are heavily tested on the **CompTIA A+ Core 1 (220-1101)** exam under Domain 3.1 and Domain 5.3.

As a technician, you must be able to identify storage interfaces, compare drive types by speed and use case, select the correct cable for each drive, and explain RAID levels to clients making data protection decisions. Complete the study checklist and review all glossary terms before beginning the lab.

---

### Section 1: High-Yield Glossary

Review these definitions carefully. The certification exam expects you to recognize and apply these terms in scenario-based questions.

**HDD (Hard Disk Drive):** A storage device that uses spinning magnetic platters and a read/write head to store and retrieve data. Typical sequential read speed is 100-160 MB/s for a 7200 RPM desktop drive. Because it has mechanical moving parts, HDDs are susceptible to physical shock and have higher seek latency than solid-state drives. HDDs remain the most cost-effective option for high-capacity bulk storage and are available in 3.5-inch (desktop) and 2.5-inch (laptop) form factors. Both connect via SATA using a 7-pin data cable and 15-pin power cable.

**SATA SSD (Solid-State Drive, SATA Interface):** A storage device using NAND flash memory chips in a 2.5-inch or M.2 form factor, communicating over the SATA III interface. No moving parts means faster random access and greater resistance to shock compared to HDDs. Sequential read speeds reach approximately 500-550 MB/s — the maximum throughput of the SATA III 6 Gbps interface. A SATA SSD is a direct drop-in replacement for an HDD; it uses the same 7-pin SATA data and 15-pin SATA power connectors.

**NVMe SSD (Non-Volatile Memory Express):** A storage device using NAND flash memory that communicates over the PCIe bus using the NVMe protocol. NVMe was designed specifically for flash storage, removing the latency overhead of the AHCI command set used by SATA. PCIe 3.0 x4 NVMe drives achieve approximately 3,500 MB/s sequential read; PCIe 4.0 x4 drives achieve 5,000-7,000 MB/s. NVMe drives typically use the M.2 form factor or, less commonly, a PCIe add-in card. They connect directly to the motherboard with no external cables.

**M.2 Form Factor:** A small circuit board storage interface standard used by both SATA SSDs and NVMe SSDs. The physical connector and card dimensions are the same regardless of protocol. Common lengths include 2230 (30mm), 2242 (42mm), 2260 (60mm), and 2280 (80mm) — the first two digits indicate 22mm width. An M.2 drive installs by inserting at an angle into the M.2 slot and securing with a single retaining screw. The slot key notch (M-key, B-key, or B+M-key) and motherboard firmware both determine whether SATA, NVMe, or both protocols are supported.

**SATA III (Serial ATA Revision 3):** The third generation of the Serial ATA interface standard, operating at 6 Gbps (approximately 600 MB/s raw; ~550 MB/s effective). SATA III uses a 7-pin data connector and, for power, a 15-pin L-shaped connector from the PSU. SATA III is backward-compatible with SATA II (3 Gbps) and SATA I (1.5 Gbps) devices and ports. All SATA-based drives — HDD or SSD — are limited by this interface ceiling.

**RAID (Redundant Array of Independent Disks):** A technology that combines multiple physical drives into a single logical volume, providing improved performance, fault tolerance, or both. RAID can be implemented in hardware (a dedicated RAID controller card or built into the motherboard chipset) or software (OS-level, such as Windows Storage Spaces or Linux mdadm). Hardware RAID is generally more reliable and offloads processing from the CPU. Software RAID is flexible and requires no additional hardware.

**RAID 0 — Striping:** Data is split into stripes and written alternately across two or more drives. All drives are read and written simultaneously, improving sequential throughput proportionally to the number of drives. No parity or mirroring is involved. If any single drive fails, all data across the entire array is lost. Minimum drives: 2. Fault tolerance: 0. Usable capacity: 100% of total raw capacity.

**RAID 1 — Mirroring:** Data is written identically to two (or more) drives simultaneously. Every block written to Drive 1 is also written to Drive 2. If one drive fails, the other contains a full, intact copy of all data. Some controllers can read from both drives simultaneously for improved read performance. Minimum drives: 2. Fault tolerance: 1 drive. Usable capacity: 50% of total raw capacity.

**RAID 5 — Striping with Distributed Parity:** Data and parity information are striped across three or more drives. Parity is distributed — no single drive holds all parity data, so no single drive is a bottleneck. If one drive fails, the remaining drives use the distributed parity to reconstruct the missing data in real time (degraded mode). The array is fully accessible during rebuild. Minimum drives: 3. Fault tolerance: 1 drive. Usable capacity: total capacity minus one drive's worth.

**RAID 10 — Striped Mirrors (RAID 1+0):** RAID 10 creates mirrored pairs (RAID 1) and then stripes data across those pairs (RAID 0). It delivers both the redundancy of mirroring and the performance of striping. Each mirrored pair can lose one of its drives without data loss. Minimum drives: 4 (two mirrored pairs). Fault tolerance: 1 drive per mirrored pair. Usable capacity: 50% of total raw capacity.

**NAND Flash Memory:** The non-volatile semiconductor storage technology used in all SSDs. NAND stores data as electrical charges in floating-gate transistors arranged in cells. Common types include SLC (1 bit per cell — fastest, most durable, most expensive), MLC (2 bits per cell), TLC (3 bits per cell — most common in consumer drives), and QLC (4 bits per cell — highest density, lowest cost, shorter write endurance). The A+ exam does not heavily test NAND cell types, but understanding them helps explain why NVMe drives vary in price and longevity.

**AHCI (Advanced Host Controller Interface):** The legacy command interface used by SATA drives. AHCI was designed for spinning hard drives and supports up to 32 command queues. NVMe replaced AHCI for SSDs, supporting up to 65,535 command queues and much lower latency. In BIOS/UEFI, the SATA controller mode must be set to AHCI (not IDE) for modern SATA drives to operate correctly, and must be set to NVMe (or RAID, if applicable) for NVMe drives.

---

### Section 2: Drive Comparison Table

| Feature | HDD (SATA) | SATA SSD | NVMe SSD (PCIe 4.0) |
|---|---|---|---|
| Sequential Read Speed | 100-160 MB/s | 500-550 MB/s | 5,000-7,000 MB/s |
| Random Read (4K) | ~0.5 MB/s | ~50 MB/s | ~700 MB/s |
| Interface | SATA III | SATA III | PCIe x4 (NVMe) |
| Form Factors | 3.5-inch, 2.5-inch | 2.5-inch, M.2 | M.2, PCIe card |
| External Cables | 7-pin data + 15-pin power | 7-pin data + 15-pin power | None |
| Moving Parts | Yes (platters, head) | No | No |
| Typical Capacity | 1-20 TB | 250 GB - 4 TB | 250 GB - 4 TB |
| Cost per GB | Lowest | Medium | Higher |
| Best Use Case | Bulk storage, backups | OS drive upgrade | Boot drive, workstation |

---

### Section 3: RAID Summary Reference Table

| RAID Level | Minimum Drives | Drives That Can Fail | Usable Capacity | Key Benefit |
|---|---|---|---|---|
| RAID 0 | 2 | 0 | 100% of all drives | Maximum performance |
| RAID 1 | 2 | 1 | 50% of total | Simple redundancy |
| RAID 5 | 3 | 1 | Total minus 1 drive | Efficient redundancy |
| RAID 10 | 4 | 1 per mirrored pair | 50% of total | Performance + redundancy |

Example capacity calculations:

- Four 2 TB drives in RAID 5: (4 - 1) x 2 TB = 6 TB usable
- Four 2 TB drives in RAID 10: 4 x 2 TB / 2 = 4 TB usable
- Three 1 TB drives in RAID 5: (3 - 1) x 1 TB = 2 TB usable
- Two 500 GB drives in RAID 1: 1 x 500 GB = 500 GB usable

---

### Section 4: Connector Identification Reference

**7-pin SATA Data Connector:**
Small, flat, L-shaped connector. One end attaches to the drive; the other attaches to a SATA port on the motherboard. The L-shaped keying ensures correct orientation. Maximum cable length recommended is 1 meter (39 inches).

**15-pin SATA Power Connector:**
Wider L-shaped connector from the PSU cable bundle. Carries 3.3V, 5V, and 12V power rails. The 3.5-inch HDD uses 5V and 12V; the 2.5-inch drive uses 5V only (the 12V pins are present but unused).

**M.2 Connector (M-key and B+M-key):**
The M.2 slot on the motherboard has a notch position that indicates supported protocols. An M-key slot (single notch on the right side of the connector gap) typically supports NVMe via PCIe. A B+M-key slot (notches on both sides) can support both SATA and NVMe, depending on the motherboard firmware. Always verify protocol support in the motherboard manual.

**Legacy — Molex (4-pin):**
Older large 4-pin connector that was standard before SATA power. Still used for some case fans, optical drives in older systems, and accessories. The A+ exam expects you to recognize it but it is not used with modern SATA or NVMe drives.

---

### Section 5: Certification Exam Tips

The following are specific traps and focus areas documented in CompTIA A+ Core 1 (220-1101) exam preparation resources.

**Trap 1 — M.2 does not equal NVMe.** Many exam questions present an M.2 slot scenario and ask if an NVMe drive will work. Always read whether the motherboard M.2 slot supports PCIe/NVMe. A motherboard with only a SATA M.2 slot cannot run an NVMe drive in that slot, even if the drive physically fits.

**Trap 2 — SATA III caps all SATA drives at ~550 MB/s.** A SATA M.2 SSD and a 2.5-inch SATA SSD are equally fast — both are limited by the SATA III interface, not by their physical form factor.

**Trap 3 — RAID 0 has zero fault tolerance.** The number in the name does not indicate redundancy — it indicates striping only. A single drive failure destroys the entire RAID 0 array.

**Trap 4 — RAID 5 requires a minimum of three drives.** The exam may present a two-drive RAID 5 scenario as a distractor. Two-drive RAID 5 is not a valid configuration; the minimum is three.

**Trap 5 — RAID 10 requires four drives, not two.** RAID 10 is striped mirrors — you need at least two mirrored pairs, which means four physical drives.

**Trap 6 — Fault tolerance in RAID 10 depends on which drives fail.** RAID 10 with four drives can survive two drive failures only if each failure is in a different mirrored pair. If both drives in the same pair fail, all data is lost. The exam may ask: "How many drives can fail in RAID 10?" The accurate answer is one per mirrored pair.

**Trap 7 — SATA data and power connectors are different sizes.** Both are L-shaped, but the power connector (15-pin) is noticeably wider than the data connector (7-pin). They cannot be accidentally swapped. On the exam, "wrong cable" is never the answer when a technician is connecting SATA devices — the connectors are physically incompatible.

**Trap 8 — BIOS/UEFI must be configured for the correct storage mode.** If a SATA SSD is installed but the BIOS controller mode is set to IDE (legacy), the drive may not be recognized correctly or will perform poorly. The correct BIOS setting for modern SATA drives is AHCI. NVMe drives require no special BIOS mode change on most modern systems.

---

### Section 6: Required Readings and Videos

Complete all of the following before attempting the lab and quiz.

**Required Reading:** Review the storage device sections in Professor Messer's CompTIA A+ Study Notes, available at [https://www.professormesser.com/](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections covering HDD, SSD, NVMe, M.2, SATA connectors, and RAID configurations.

**Required Video:** Watch the storage devices segments in Professor Messer's free CompTIA A+ Core 1 course at [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Focus on the drive interface comparisons, M.2 vs. NVMe clarification, and RAID level diagrams.

**Supplemental Reference:** CompTIA A+ Core 1 exam objectives are available at [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a). Review Domain 3.1 and Domain 5.3 objective lists to confirm your coverage.

---

### Section 7: Lab Connection

This module's lab activity reinforces three skills directly tested on the A+ exam:

1. Drive and connector identification from photographs — matching drive types to their interface, protocol, and form factor
2. RAID planning scenarios — given organizational requirements, selecting the appropriate RAID level and calculating usable capacity
3. Connector labeling on a system diagram — distinguishing SATA data, SATA power, and M.2 connections

Complete the Reading Guide glossary review before beginning the lab.

---

### Section 8: Study Checklist

- [ ] Define and distinguish HDD, SATA SSD, and NVMe SSD without referring to notes
- [ ] State the sequential read speed range for each drive type from memory
- [ ] Identify the 7-pin SATA data connector and 15-pin SATA power connector by description
- [ ] Explain why M.2 form factor does not automatically mean NVMe protocol
- [ ] State the minimum drive count for RAID 0, RAID 1, RAID 5, and RAID 10
- [ ] State the fault tolerance (drives that can fail) for each RAID level
- [ ] Calculate usable capacity for a RAID 5 array given drive count and size
- [ ] Calculate usable capacity for a RAID 10 array given drive count and size
- [ ] Read the storage sections in Professor Messer's CompTIA A+ Study Notes
- [ ] Watch the storage device videos in Professor Messer's free A+ Core 1 course
- [ ] Complete Lab 05 and submit via Canvas before the deadline
- [ ] Post your Discussion 05 initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

1. **Professor Messer — Storage Devices (220-1101 Free Video)**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video covering HDD vs. SSD vs. NVMe, M.2 form factors, SATA connectors, RAID levels, and interface speeds — all Module 05 exam objectives.

2. **CrystalDiskInfo (Free HDD/SSD Health Monitor)**
   URL: [https://crystalmark.info/en/software/crystaldiskinfo/](https://crystalmark.info/en/software/crystaldiskinfo/)
   Relevance: Free Windows utility that reads SMART data from HDDs and SSDs to report drive health, temperature, power-on hours, and reallocated sector counts. Use in the challenge exercise to inspect drive health on any available system.

3. **CrystalDiskMark (Free Storage Benchmark)**
   URL: [https://crystalmark.info/en/software/crystaldiskmark/](https://crystalmark.info/en/software/crystaldiskmark/)
   Relevance: Free sequential and random read/write benchmark for all storage types. Allows direct comparison of HDD, SATA SSD, and NVMe SSD performance on real hardware — directly reinforces the speed comparison table in the reading guide.

4. **StorageReview.com — RAID Fundamentals Guide (Free)**
   URL: [https://www.storagereview.com/review/raid-levels-explained](https://www.storagereview.com/review/raid-levels-explained)
   Relevance: Free reference covering RAID 0, 1, 5, 6, and 10 with diagrams showing how data and parity are distributed. Supplements the RAID section of the reading guide with visual representations useful for exam scenario questions.

5. **Backblaze Hard Drive Stats (Free Open Data)**
   URL: [https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data](https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data)
   Relevance: Real-world HDD failure rate data from a cloud storage provider operating tens of thousands of drives. Provides data-driven context for understanding HDD vs. SSD reliability differences discussed in the reading guide.
