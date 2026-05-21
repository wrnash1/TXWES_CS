# Reading Guide: Module 05 - Storage Devices
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 05 - Storage Devices**! This module covers the full range of storage technologies used in modern PCs, from traditional spinning hard drives to high-speed NVMe SSDs, as well as the RAID configurations used to provide redundancy or performance in multi-drive systems. These topics are heavily tested on the **CompTIA A+ Core 1 (220-1101)** exam under hardware and network troubleshooting domains.

As a technician, you must be able to identify storage interfaces, compare drive types by speed and use case, and explain RAID levels to clients making data protection decisions. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **HDD vs SATA SSD vs M.2 NVMe**: A Hard Disk Drive (HDD) uses spinning magnetic platters and a read/write head; it connects via SATA and offers high capacity at low cost but slow access speeds (~100–150 MB/s). A SATA SSD uses NAND flash memory in a 2.5-inch or M.2 form factor with the SATA interface, offering ~500–550 MB/s sequential read speeds. An M.2 NVMe drive uses the PCIe bus (NVMe protocol) and achieves 3,000–7,000+ MB/s sequential reads — 5–14x faster than SATA. NVMe drives look similar to M.2 SATA drives but are not interchangeable; the key notch and protocol differ.
*   **drive form factors (3.5 and 2.5)**: Desktop HDDs use the 3.5-inch form factor, which requires a drive bay or adapter bracket in standard ATX cases. Laptop HDDs and most SATA SSDs use the 2.5-inch form factor, which fits in dedicated laptop drive bays and desktop cases with a tray adapter. Both form factors use the same SATA data and SATA power connectors, though 2.5-inch drives draw less power (5V only vs. 5V and 12V for 3.5-inch).
*   **RAID levels (0, 1, 5, 10)**: RAID (Redundant Array of Independent Disks) combines multiple drives for performance or redundancy. RAID 0 stripes data across two or more drives for maximum performance but provides zero fault tolerance — one drive failure loses all data. RAID 1 mirrors data identically across two drives; it survives one drive failure but uses 50% of total capacity. RAID 5 stripes data with distributed parity across three or more drives; it survives one drive failure and is space-efficient. RAID 10 (1+0) combines mirroring and striping across four or more drives for both performance and redundancy.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 3.1):** The A+ exam frequently presents RAID scenarios asking how many drives can fail before data loss occurs. Remember: RAID 0 = 0 drives can fail; RAID 1 = 1 drive can fail; RAID 5 = 1 drive can fail; RAID 10 = up to 1 drive per mirrored pair can fail. These are the most-tested RAID facts.
*   **Scenario Trap:** Watch out for questions that describe an M.2 slot and ask whether an NVMe or SATA drive can be installed. Many M.2 slots support both protocols, but some support only one. The exam answer will depend on the motherboard specification stated in the scenario — read carefully before selecting "it will work in any M.2 slot."
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers all storage technologies with clear comparisons. Navigate to the storage devices section: [Professor Messer's CompTIA A+ Core 1 Course — Storage Devices](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Pay special attention to the RAID level diagrams and the NVMe vs. SATA M.2 comparison.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the storage device sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on HDD, SSD, NVMe, and RAID configurations.
*   **Required Video:** Watch the video lecture on storage devices from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering drive interfaces, form factors, and RAID levels.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Connect a 2.5-inch SATA SSD with power and data cables**: Attach the flat SATA data cable (7-pin) to the drive and motherboard SATA port. Connect the SATA power cable (15-pin) from the PSU. Verify the drive appears in BIOS under storage device detection.
*   **Install an M.2 NVMe drive into PCIe slot and secure it**: Insert the M.2 NVMe drive at the correct angle into the M.2 slot, press it down flat, and secure it with the single retaining screw. Confirm the drive is recognized in BIOS as an NVMe device (not as a SATA device).
*   **Set up a RAID 1 mirror using motherboard BIOS utility**: Enter the BIOS/UEFI storage configuration menu and enable RAID mode on the SATA controller. Use the RAID configuration utility to select two identical drives and configure them as a RAID 1 mirror array.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the storage device sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on storage devices in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the installation steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
