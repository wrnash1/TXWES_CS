# Quiz: Module 05 - Storage Devices

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

Total Questions: 10 | Points: 10 (1 point each)

Certification Domain: 3.1 — Install and configure storage devices | 5.3 — Troubleshoot hard drives and RAID arrays

---

### Question 1

Which RAID level provides data striping across two or more drives with no parity and no redundancy?

- A) RAID 0
- B) RAID 1
- C) RAID 5
- D) RAID 10

Correct Answer: A — RAID 0 stripes data across all drives in the array for maximum sequential performance. No parity data is written and no mirroring occurs, meaning there is zero fault tolerance. One drive failure destroys all data in the array.

Distractor Analysis:

- Why B is incorrect: RAID 1 is mirroring — data is written identically to two drives simultaneously, which provides redundancy, not pure striping with zero fault tolerance.
- Why C is incorrect: RAID 5 stripes data with distributed parity, providing both performance and fault tolerance; it is not a zero-redundancy configuration.
- Why D is incorrect: RAID 10 combines striping with mirroring, providing both performance and redundancy; it is not a zero-redundancy configuration.

---

### Question 2

In the context of PC hardware, which of the following most accurately describes the 2.5-inch drive form factor?

- A) A compact drive size used in laptops and desktop SATA SSDs, measuring approximately 2.5 inches wide, compatible with the same SATA data and power connectors as 3.5-inch drives but requiring only 5V power.
- B) A drive form factor that uses PCIe lanes and the NVMe protocol, plugging directly into an M.2 slot on the motherboard without any external cables.
- C) A drive enclosure size used exclusively for enterprise SAS drives in rack-mounted servers, not compatible with standard desktop SATA controllers.
- D) A physical dimension that refers to the width of the SATA data cable rather than the drive itself, distinguishing it from the wider IDE ribbon cable standard.

Correct Answer: A — The 2.5-inch form factor is the standard for laptop HDDs and most SATA SSDs. It uses the same 7-pin SATA data and 15-pin SATA power connectors as the 3.5-inch desktop form factor but operates on 5V only and does not use the 12V rail.

Distractor Analysis:

- Why B is incorrect: This describes an M.2 NVMe drive. NVMe M.2 drives have no external cables and use the PCIe bus, neither of which applies to a 2.5-inch drive.
- Why C is incorrect: The 2.5-inch form factor is a standard consumer laptop and SSD size; it is not exclusive to enterprise SAS or server hardware.
- Why D is incorrect: Form factor refers to the physical chassis dimensions of the drive itself, not the width or pin count of the connecting cable.

---

### Question 3

A company stores critical data on a four-drive RAID 5 array. One drive fails during business hours. What is the correct immediate action?

- A) Power down the server immediately; all data is now lost because RAID 5 cannot survive any drive failures.
- B) Continue operations normally and replace the failed drive as soon as possible; RAID 5 can survive one drive failure and will rebuild automatically.
- C) Remove a second drive to trigger a full rebuild, which resets the parity calculations across all remaining drives.
- D) Convert the array to RAID 0 before replacing the drive to avoid data corruption during the rebuild process.

Correct Answer: B — RAID 5 uses distributed parity to reconstruct the data from the failed drive by mathematically combining the data and parity on the remaining drives. The array continues in degraded mode and will rebuild automatically once the failed drive is replaced.

Distractor Analysis:

- Why A is incorrect: RAID 5 is specifically designed to survive exactly one drive failure without data loss. Immediate shutdown is unnecessary and disrupts operations.
- Why C is incorrect: Removing a second drive from a RAID 5 array already in degraded mode causes total data loss. The array cannot tolerate a second simultaneous failure.
- Why D is incorrect: Converting to RAID 0 eliminates all fault tolerance and is never a correct response to a production drive failure. RAID conversion is not an emergency procedure.

---

### Question 4

A technician is building a gaming PC and wants the fastest possible boot drive. The motherboard has both SATA ports and an M.2 slot that supports PCIe 4.0 NVMe. Which drive type provides the highest sequential read performance?

- A) 3.5-inch 7200 RPM SATA HDD
- B) 2.5-inch SATA SSD
- C) M.2 SATA SSD
- D) M.2 PCIe 4.0 NVMe SSD

Correct Answer: D — PCIe 4.0 NVMe drives achieve 5,000–7,000+ MB/s sequential read speeds by using PCIe lanes instead of the SATA bus, making them the highest-performance option among all the choices listed.

Distractor Analysis:

- Why A is incorrect: A 7200 RPM HDD achieves approximately 100–160 MB/s sequential reads, limited by platter rotation speed and mechanical seek time.
- Why B is incorrect: A 2.5-inch SATA SSD is capped at approximately 550 MB/s by the SATA III interface regardless of the flash quality inside the drive.
- Why C is incorrect: An M.2 SATA SSD uses the SATA protocol over the M.2 physical connector; it is still limited to approximately 550 MB/s. The M.2 form factor does not change the protocol or speed.

---

### Question 5

A small business needs a storage solution that mirrors data across two drives for redundancy. They have exactly two drives available. Which RAID level is valid with only two drives?

- A) RAID 0 — striping across two drives maximizes both performance and redundancy.
- B) RAID 1 — mirroring provides redundancy and is valid with a minimum of two drives.
- C) RAID 5 — parity distribution provides redundancy across two drives.
- D) RAID 6 — double parity across two drives ensures the highest fault tolerance available.

Correct Answer: B — RAID 1 requires a minimum of two drives and writes identical data to both. One drive can fail without data loss, making it the correct two-drive redundancy solution.

Distractor Analysis:

- Why A is incorrect: RAID 0 provides zero redundancy — one drive failure destroys all data. It does not meet the mirroring requirement described in the scenario.
- Why C is incorrect: RAID 5 requires a minimum of three drives. A two-drive RAID 5 is not a valid configuration; no standard RAID controller will accept it.
- Why D is incorrect: RAID 6 requires a minimum of four drives. It uses double distributed parity to survive two simultaneous failures, which requires at least four members.

---

### Question 6

A technician installs a new M.2 drive in a laptop. The drive is fully seated and secured with the retaining screw, but it does not appear in the BIOS storage device list. The technician confirms the drive is not defective by testing it in another machine. What are the two most likely causes to investigate first?

- A) The SATA data cable is loose, and the SATA power cable needs to be reseated.
- B) The M.2 slot supports only NVMe and the installed drive is a SATA M.2 drive, or the M.2 slot is disabled in BIOS.
- C) The operating system must be reinstalled before the BIOS can detect any new storage device.
- D) The drive's firmware version is incompatible with the BIOS version and must be updated before detection is possible.

Correct Answer: B — Two common causes of M.2 non-detection are protocol mismatch (the slot supports NVMe only but a SATA M.2 drive was installed, or vice versa) and a BIOS setting that has disabled the M.2 slot, which sometimes occurs when RAID is enabled on SATA ports that share PCIe lanes with the M.2 slot.

Distractor Analysis:

- Why A is incorrect: M.2 drives have no external data or power cables. The M.2 interface is a direct connection to the motherboard slot; SATA cable issues do not apply.
- Why C is incorrect: The BIOS detects hardware during POST, before any operating system loads. OS reinstallation is not required for BIOS-level device detection.
- Why D is incorrect: While firmware compatibility is occasionally an issue, it is not among the most common first-step diagnostics. Protocol mismatch and BIOS configuration are the primary causes to investigate first.

---

### Question 7

A storage administrator is configuring a RAID array using six 2 TB hard drives. The requirement is to maximize usable capacity while still tolerating one drive failure. Which RAID level should be selected, and what is the resulting usable capacity?

- A) RAID 0 — 12 TB usable; tolerates one drive failure.
- B) RAID 1 — 2 TB usable; tolerates one drive failure.
- C) RAID 5 — 10 TB usable; tolerates one drive failure.
- D) RAID 10 — 6 TB usable; tolerates one drive failure.

Correct Answer: C — RAID 5 with six 2 TB drives yields (6 - 1) x 2 TB = 10 TB of usable capacity while tolerating one drive failure. This is the most capacity-efficient redundant RAID level among the choices.

Distractor Analysis:

- Why A is incorrect: RAID 0 provides 12 TB usable capacity but tolerates zero drive failures. One failure destroys all data; it does not meet the fault tolerance requirement.
- Why B is incorrect: A simple RAID 1 with six drives would produce only 2 TB of usable space with extreme waste; RAID 1 is highly inefficient at scale and not the optimal choice here.
- Why D is incorrect: RAID 10 with six drives provides only 6 TB usable capacity (50% of 12 TB). When capacity efficiency is the primary goal alongside single-drive fault tolerance, RAID 5 is the better choice.

---

### Question 8

Which statement correctly describes the difference between hardware RAID and software RAID?

- A) Hardware RAID uses a dedicated controller to manage the array, offloading processing from the CPU; software RAID is managed by the operating system and uses CPU resources to calculate parity.
- B) Hardware RAID stores all data in system RAM for faster access; software RAID writes data directly to disk without any parity calculation.
- C) Software RAID is always faster than hardware RAID because the CPU operates at higher clock speeds than dedicated RAID controller chips.
- D) Hardware RAID requires a special driver to be installed in Windows before the array is visible; software RAID is automatically detected by BIOS without any driver.

Correct Answer: A — A hardware RAID controller contains its own processor and cache memory, managing all array operations independently of the system CPU. Software RAID (such as Windows Storage Spaces or Linux mdadm) uses the main CPU for parity calculations and array management, which can impact system performance under heavy storage load.

Distractor Analysis:

- Why B is incorrect: Hardware RAID does not store data in system RAM; both hardware and software RAID write data persistently to the physical drives in the array.
- Why C is incorrect: Dedicated hardware RAID controllers are optimized specifically for RAID operations with onboard cache. General-purpose CPUs must share resources with all other system tasks, making software RAID generally slower under load.
- Why D is incorrect: This statement reverses the expected behavior. Hardware RAID arrays do typically require a controller driver for OS communication, but BIOS detects them through the controller's own firmware during POST.

---

### Question 9

A technician replaces a failed drive in a RAID 5 array with an identical new drive. The RAID controller begins the rebuild process. During the rebuild, the array is in degraded mode. What does "degraded mode" mean, and what is the risk during this period?

- A) The array is completely offline and inaccessible until the rebuild finishes; no read or write operations can occur during the rebuild.
- B) The array remains accessible for reads and writes, but there is no fault tolerance during the rebuild; a second drive failure before the rebuild completes will cause total data loss.
- C) The array operates at double the normal speed during rebuild because the controller reads from all remaining drives simultaneously to populate the new drive.
- D) Degraded mode is a BIOS warning only; the array itself is fully redundant and can survive an additional drive failure during the rebuild without data loss.

Correct Answer: B — In degraded mode, RAID 5 reconstructs missing data on-the-fly from the remaining drives, allowing normal read and write access to continue. However, because the one allowed failure has already occurred, any additional drive failure before the rebuild completes exceeds the array's fault tolerance and causes total data loss.

Distractor Analysis:

- Why A is incorrect: RAID 5 remains online during rebuild. The purpose of degraded mode is to maintain data availability while the replacement drive is being populated.
- Why C is incorrect: The rebuild process typically slows array performance because the controller must read all remaining drives to reconstruct and write parity to the new drive; speed does not double.
- Why D is incorrect: Degraded mode is a real operational state in which fault tolerance is temporarily absent, not merely a BIOS warning. An additional drive failure during rebuild causes complete data loss.

---

### Question 10

A technician needs to identify a SATA data cable versus a SATA power cable in an unlabeled cable bundle. Which physical characteristic most reliably distinguishes them?

- A) The data cable has a blue connector and the power cable has a black connector; all SATA cables follow this color-coding standard.
- B) The data cable has 7 pins and a narrow L-shaped connector; the power cable has 15 pins and a wider L-shaped connector.
- C) The data cable carries 12V power and the power cable carries the data signal; the labels on the connector housing identify which is which.
- D) The data cable is a round braided cable and the power cable is a flat ribbon cable; round cables always carry data and flat cables always carry power.

Correct Answer: B — The 7-pin SATA data connector is narrow and carries only the data signal. The 15-pin SATA power connector is noticeably wider and carries 3.3V, 5V, and 12V power. Their different widths and pin counts make them physically impossible to confuse or swap accidentally.

Distractor Analysis:

- Why A is incorrect: There is no universal SATA color-coding standard. Cable colors vary by manufacturer and are not a reliable identification method.
- Why C is incorrect: The function descriptions are reversed. The data cable carries the SATA data signal; the power cable carries DC voltages from the PSU.
- Why D is incorrect: Both SATA data and power cables are flat. There is no round-versus-flat distinction for SATA cables; identification relies on connector width and pin count.

---

### Question 11

A user purchases a new M.2 SSD labeled "M.2 2280 PCIe 4.0 x4 NVMe." What does "2280" describe?

- A) The drive's maximum sequential read speed in MB/s
- B) The physical dimensions of the drive — 22 mm wide and 80 mm long
- C) The PCIe generation and lane count combined into a single number
- D) The drive's NAND flash chip density in gigabits per die

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* M.2 size codes encode the width and length of the drive card in millimeters. The first two digits (22) are the width in mm; the last two digits (80) are the length in mm. An M.2 2280 drive is 22 mm × 80 mm — the most common desktop M.2 NVMe size.
- *Why A is incorrect:* Sequential read speed is expressed in MB/s separately (e.g., "up to 7000 MB/s") and is not encoded in the size code.
- *Why C is incorrect:* PCIe generation and lane count are expressed separately ("PCIe 4.0 x4") and are not combined into a single number in M.2 nomenclature.
- *Why D is incorrect:* NAND chip density is an internal manufacturing specification not encoded in the consumer drive label's size code.

---

### Question 12

Which of the following correctly describes the key difference between RAID 0 and RAID 1?

- A) RAID 0 stripes data across multiple drives for performance with no redundancy; RAID 1 mirrors data across two drives for redundancy with no performance gain
- B) RAID 0 requires three or more drives; RAID 1 requires exactly two drives
- C) RAID 0 provides fault tolerance against one drive failure; RAID 1 provides no fault tolerance
- D) RAID 0 and RAID 1 both require an identical number of drives and provide the same usable capacity

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* RAID 0 (striping) splits data across all drives, increasing sequential read/write performance. It has zero fault tolerance — one drive failure destroys all data. RAID 1 (mirroring) writes identical data to two drives, providing fault tolerance against one drive failure at the cost of 50% usable capacity (2 × 1 TB = 1 TB usable).
- *Why B is incorrect:* RAID 0 can be implemented with two drives (the minimum). RAID 1 also requires exactly two drives (it is a two-drive mirror). The minimum drive count for RAID 0 is 2, not 3.
- *Why C is incorrect:* This reverses the descriptions. RAID 1 provides fault tolerance; RAID 0 provides no fault tolerance.
- *Why D is incorrect:* RAID 0 and RAID 1 have different capacity calculations. RAID 0 uses 100% of total raw capacity (no redundancy overhead). RAID 1 uses 50% of raw capacity (one drive's worth is the usable space). They have very different usable capacity outcomes.

---

### Question 13

A 7200 RPM hard disk drive experiences a "clicking" sound and the OS cannot access the drive. What is the MOST likely cause?

- A) The drive's SATA data cable is damaged and is causing the drive to spin at the wrong speed
- B) The read/write head is making mechanical contact with the spinning platters due to a head crash
- C) The drive's firmware has become corrupted, causing it to click as it attempts to load its configuration
- D) The SATA power connector is intermittent, causing the spindle motor to repeatedly start and stop

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A clicking sound (often called the "click of death") is the hallmark symptom of a read/write head failure in an HDD. In normal operation, heads float on a thin air cushion above the platters. A head crash occurs when a head physically contacts the platter surface, destroying the platter's magnetic coating and the head itself. This causes the characteristic clicking as the arm repeatedly attempts and fails to seek to the correct position.
- *Why A is incorrect:* A damaged SATA data cable causes connectivity errors (drive not detected, I/O errors) but does not affect spindle speed and does not produce a clicking sound.
- *Why C is incorrect:* Firmware corruption typically causes the drive to be unrecognized by the OS or to appear with an incorrect model number. It does not produce mechanical clicking noises, which are physically caused by head movement.
- *Why D is incorrect:* An intermittent power connection would cause the spindle to stop and restart (audible as a wind-down and spin-up sound), not a rapid repetitive clicking pattern. The clicking is specifically from the head actuator arm, not the spindle motor.

---

### Question 14

Which RAID level requires a minimum of four drives and provides both striping performance and redundancy through mirroring?

- A) RAID 0
- B) RAID 1
- C) RAID 5
- D) RAID 10

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* RAID 10 (also written RAID 1+0) combines mirroring and striping. It requires at minimum four drives: two pairs of mirrored drives, with the pairs striped together. This provides the write performance of striping and the fault tolerance of mirroring. Usable capacity is 50% of raw total.
- *Why A is incorrect:* RAID 0 only stripes — it provides no redundancy and requires a minimum of two drives.
- *Why B is incorrect:* RAID 1 only mirrors — it requires exactly two drives per mirror set and provides no striping performance benefit.
- *Why C is incorrect:* RAID 5 requires a minimum of three drives. It uses distributed parity for redundancy and striping for performance, but it is not a mirror+stripe (RAID 10) implementation.

---

### Question 15

An NVMe SSD is installed in a PCIe 3.0 x4 M.2 slot, but the drive is rated for PCIe 4.0 x4. What is the expected behavior?

- A) The drive will not function because PCIe 4.0 and PCIe 3.0 M.2 slots use different physical key configurations
- B) The drive will operate at PCIe 3.0 speeds, achieving roughly half the rated maximum sequential throughput
- C) The drive will function at full PCIe 4.0 speed because NVMe controllers automatically generate PCIe 4.0 timing on any slot
- D) The drive will overheat because PCIe 3.0 slots do not provide adequate cooling voltage for PCIe 4.0 NVMe drives

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* PCIe is backward compatible across generations using the same physical connector. A PCIe 4.0 x4 NVMe drive installed in a PCIe 3.0 x4 M.2 slot will negotiate down to PCIe 3.0 speeds. PCIe 3.0 x4 provides approximately 3,940 MB/s bandwidth, compared to PCIe 4.0 x4's approximately 7,877 MB/s — roughly half the rated throughput.
- *Why A is incorrect:* M.2 NVMe slots use the same M-key physical connector for both PCIe 3.0 and PCIe 4.0 drives. There is no physical key difference between generations; backward compatibility is electrical.
- *Why C is incorrect:* PCIe generation is determined by the slot (motherboard), not the card (drive). A drive cannot force a slot to operate at a higher generation than the slot is rated for.
- *Why D is incorrect:* PCIe slots do not supply "cooling voltage." All PCIe versions supply the same 3.3V and 12V power rails. Thermal management for NVMe drives is handled by the drive's heatsink and the system's airflow, not by the PCIe version.

---

### Question 16

A technician is configuring storage for a video production workstation. The primary requirement is maximum read and write speed for editing 8K video files; data redundancy is not a concern because the files are regularly backed up. Which storage configuration best meets this requirement?

- A) Two 4 TB HDDs in RAID 1
- B) Two 2 TB NVMe SSDs in RAID 0
- C) One 8 TB HDD with a SATA SSD cache drive
- D) Four 1 TB SATA SSDs in RAID 5

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Two NVMe SSDs in RAID 0 (striping) combines the bandwidth of both drives, potentially achieving 10,000–14,000 MB/s sequential throughput — far exceeding what 8K video editing workflows require. Since backup redundancy is covered externally, RAID 0's lack of fault tolerance is an acceptable tradeoff for maximum performance.
- *Why A is incorrect:* HDDs in RAID 1 provide approximately 150–200 MB/s sequential speed — orders of magnitude slower than NVMe. This configuration prioritizes redundancy over speed, which is the opposite of the requirement.
- *Why C is incorrect:* A hybrid HDD + SSD cache arrangement delivers moderate performance improvement for frequently accessed files but does not provide the sustained high-bandwidth sequential writes needed for 8K video capture and editing.
- *Why D is incorrect:* Four SATA SSDs in RAID 5 provide decent throughput (2,000–2,500 MB/s with a hardware controller) and redundancy, but SATA SSDs are still slower than NVMe and RAID 5's parity calculation overhead reduces peak write throughput. The RAID 0 NVMe option outperforms this for a pure-speed requirement.

---

### Question 17

What is the usable storage capacity of a RAID 5 array built with five 4 TB drives?

- A) 20 TB (full capacity, no overhead)
- B) 16 TB (one drive's worth reserved for distributed parity)
- C) 10 TB (50% overhead for mirroring)
- D) 12 TB (two drives' worth reserved for dual parity)

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* RAID 5 uses distributed parity equivalent to one drive's capacity spread across all drives. Usable capacity = (N − 1) × drive size = (5 − 1) × 4 TB = 4 × 4 TB = 16 TB. One drive's worth (4 TB) is consumed by the distributed parity that enables single-drive fault tolerance.
- *Why A is incorrect:* 20 TB would be RAID 0 (no parity overhead). RAID 5 sacrifices one drive's equivalent capacity for parity.
- *Why C is incorrect:* 50% overhead (10 TB usable from 20 TB raw) describes RAID 1 or RAID 10 (mirroring). RAID 5 parity overhead is 1/N, not 50%.
- *Why D is incorrect:* Dual parity (two drives' worth reserved) describes RAID 6, which can survive two simultaneous drive failures. RAID 5 uses single parity (one drive's equivalent).

---

### Question 18

A SATA SSD and a SATA HDD are both connected to the same motherboard. A technician notices the SSD boots Windows in approximately 8 seconds, while the HDD takes approximately 45 seconds. What is the PRIMARY reason for this speed difference?

- A) The SSD has a faster CPU built into its controller chip
- B) The SSD has no moving parts and accesses all storage locations in microseconds; the HDD requires physical platter rotation and head seeking
- C) The SATA port the SSD uses provides more power than the port used by the HDD
- D) The SSD uses compressed data storage, reducing the amount of data that must be read during boot

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The fundamental speed advantage of SSDs over HDDs is the absence of mechanical components. HDDs must physically spin platters to the correct position and move the read/write head to the target track before reading data — a process taking 3–10 ms per random access. SSDs access any NAND flash cell electrically in microseconds, with no rotational latency or seek time. Boot time is dominated by random I/O (reading many small OS files), where SSDs outperform HDDs by orders of magnitude.
- *Why A is incorrect:* SSD controllers are specialized microcontrollers optimized for NAND management (wear leveling, garbage collection, error correction). They do not contain general-purpose CPUs and their controller speed is not the primary explanation for the performance difference vs. HDDs.
- *Why C is incorrect:* All SATA ports on the same controller provide the same power specifications. Power delivery does not vary between SATA ports on the same board and has no effect on drive speed.
- *Why D is incorrect:* Consumer SSDs typically do not use real-time transparent compression for storage (some enterprise SSD controllers do, but this is not a standard feature of consumer SSDs). The speed advantage is from the NAND flash technology itself, not compression.

---

### Question 19

Which of the following best describes the role of wear leveling in an SSD?

- A) It regulates the SSD's operating temperature to prevent thermal degradation of NAND cells
- B) It distributes write operations evenly across all NAND flash cells to prevent any single cell from wearing out prematurely
- C) It reduces write amplification by compressing data before writing to NAND flash
- D) It monitors SMART data to predict when individual NAND cells will fail and pre-emptively moves data

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* NAND flash cells have a finite number of program/erase (P/E) cycles before they fail (typically 1,000–100,000 cycles depending on cell type). Wear leveling is an algorithm in the SSD controller that ensures write operations are distributed evenly across all available cells, preventing hot spots where frequently written cells wear out while other cells remain unused. This extends the overall lifespan of the drive.
- *Why A is incorrect:* Thermal management in SSDs is handled by the drive's thermal sensor and the system's SMART thermal monitoring — not by wear leveling algorithms. Wear leveling is specifically about distributing write cycles, not managing heat.
- *Why C is incorrect:* Data compression is a separate optional feature in some SSD controllers (primarily Sandforce-based). Write amplification is the ratio of physical writes to logical writes; reducing write amplification is a goal of efficient garbage collection, not directly of wear leveling.
- *Why D is incorrect:* SMART monitoring and predictive failure analysis are separate health monitoring functions. Wear leveling operates proactively on every write, not reactively in response to detected cell failures.

---

### Question 20

A company is deploying storage for a critical financial database server that must survive two simultaneous drive failures without data loss. Which RAID level meets this requirement?

- A) RAID 1
- B) RAID 5
- C) RAID 6
- D) RAID 10

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* RAID 6 uses dual distributed parity, allowing the array to survive two simultaneous drive failures without data loss. It requires a minimum of four drives, with usable capacity = (N − 2) × drive size. For a mission-critical financial database, RAID 6 is the appropriate choice when two-drive fault tolerance is required.
- *Why A is incorrect:* RAID 1 mirrors two drives and tolerates only one drive failure (the failure of one mirror). It does not provide two-drive fault tolerance and is not appropriate for large storage arrays.
- *Why B is incorrect:* RAID 5 uses single distributed parity and can survive only one drive failure. A second drive failure before rebuild completes causes total data loss — unacceptable for a critical financial database.
- *Why D is incorrect:* RAID 10 can survive one drive failure per mirror pair (in the best case, up to N/2 failures if each failing drive is in a different pair). However, if two failures occur in the same mirror pair, all data is lost. RAID 6 is the specified correct answer for guaranteed two-simultaneous-drive fault tolerance.
