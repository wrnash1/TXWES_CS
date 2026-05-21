# Quiz: Module 05 - Storage Devices
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which RAID level provides data striping without parity or redundancy?
*   A) RAID 0
*   B) RAID 1
*   C) RAID 5
*   D) RAID 10
*   **Correct Answer:** A) RAID 0 stripes data for performance but offers zero fault tolerance.
*   **Distractor Analysis:**
    *   *Why correct:* RAID 0 stripes data for performance but offers zero fault tolerance.
    *   RAID 1 is mirroring. RAID 5 uses parity. RAID 10 is striped mirrors.

---

**Question 2**
In the context of PC hardware, which of the following most accurately describes the **2.5-inch drive form factor**?
*   A) A compact drive size used in laptops and desktop SATA SSDs, measuring approximately 2.5 inches wide, compatible with the same SATA data and power connectors as 3.5-inch drives but requiring only 5V power.
*   B) A drive form factor that uses PCIe lanes and the NVMe protocol, plugging directly into an M.2 slot on the motherboard without any external cables.
*   C) A drive enclosure size used exclusively for enterprise SAS drives in rack-mounted servers, not compatible with standard desktop SATA controllers.
*   D) A physical dimension that refers to the width of the SATA data cable rather than the drive itself, distinguishing it from the wider IDE ribbon cable standard.
*   **Correct Answer:** A) A compact drive size used in laptops and desktop SATA SSDs, measuring approximately 2.5 inches wide, compatible with the same SATA data and power connectors as 3.5-inch drives but requiring only 5V power.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the 2.5-inch form factor's dimensions, use cases, and power requirements compared to the 3.5-inch desktop drive standard.
    * *Why B is incorrect:* This describes an M.2 NVMe drive, which is a different form factor entirely, not a 2.5-inch drive.
    * *Why C is incorrect:* 2.5-inch is a standard consumer laptop/SSD form factor; it is not exclusive to enterprise SAS drives.
    * *Why D is incorrect:* Form factor refers to the physical dimensions of the drive chassis, not cable width.


---

**Question 3**
A company stores critical data on a four-drive RAID 5 array. One drive fails during business hours. What is the correct immediate action?
*   A) Power down the server immediately; all data is now lost because RAID 5 cannot survive any drive failures
*   B) Continue operations normally and replace the failed drive as soon as possible; RAID 5 can survive one drive failure and will rebuild automatically
*   C) Remove a second drive to trigger a full rebuild, which resets the parity calculations across all remaining drives
*   D) Convert the array to RAID 0 before replacing the drive to avoid data corruption during the rebuild process
*   **Correct Answer:** B) Continue operations normally and replace the failed drive as soon as possible; RAID 5 can survive one drive failure and will rebuild automatically
*   **Distractor Analysis:**
    * *Why B is correct:* RAID 5 uses distributed parity to reconstruct missing data from the remaining drives; the array remains accessible (in degraded mode) until the failed drive is replaced and rebuilt.
    * *Why A is incorrect:* RAID 5 is specifically designed to survive one drive failure with no data loss; immediate shutdown is unnecessary.
    * *Why C is incorrect:* Removing a second drive from a degraded RAID 5 array will cause total data loss; only one drive failure is tolerated.
    * *Why D is incorrect:* Converting to RAID 0 destroys redundancy entirely and is never the correct response to a drive failure in a production array.


---

**Question 4**
A technician is building a gaming PC and wants the fastest possible boot drive. The motherboard has both SATA ports and an M.2 slot that supports PCIe 4.0 NVMe. Which drive type provides the highest sequential read performance?
*   A) 3.5-inch 7200 RPM SATA HDD
*   B) 2.5-inch SATA SSD
*   C) M.2 SATA SSD
*   D) M.2 PCIe 4.0 NVMe SSD
*   **Correct Answer:** D) M.2 PCIe 4.0 NVMe SSD
*   **Distractor Analysis:**
    * *Why D is correct:* PCIe 4.0 NVMe drives achieve 5,000–7,000+ MB/s sequential reads, far exceeding all SATA-based options.
    * *Why A is incorrect:* A 7200 RPM HDD achieves approximately 100–160 MB/s sequential reads — the slowest option by a large margin.
    * *Why B is incorrect:* SATA SSDs are capped at approximately 550 MB/s by the SATA III interface limitation.
    * *Why C is incorrect:* An M.2 SATA SSD still uses the SATA protocol and is limited to ~550 MB/s regardless of its M.2 physical form factor.


---

**Question 5**
A small business needs a storage solution that mirrors data across two drives for redundancy but also provides the best read performance of any two-drive RAID configuration. Which RAID level meets both requirements?
*   A) RAID 0 — striping across two drives maximizes both performance and redundancy
*   B) RAID 1 — mirroring provides redundancy and some read performance benefit from reading both drives simultaneously
*   C) RAID 5 — parity distribution provides redundancy and high write performance across two drives
*   D) RAID 6 — double parity across two drives ensures the highest fault tolerance available
*   **Correct Answer:** B) RAID 1 — mirroring provides redundancy and some read performance benefit from reading both drives simultaneously
*   **Distractor Analysis:**
    * *Why B is correct:* RAID 1 is the standard two-drive redundant configuration; some RAID controllers can read from both drives simultaneously, improving read throughput while maintaining full mirroring.
    * *Why A is incorrect:* RAID 0 provides zero redundancy — one drive failure destroys all data; it does not meet the redundancy requirement.
    * *Why C is incorrect:* RAID 5 requires a minimum of three drives; it cannot be configured with only two drives.
    * *Why D is incorrect:* RAID 6 requires a minimum of four drives; it is not a valid two-drive configuration.

