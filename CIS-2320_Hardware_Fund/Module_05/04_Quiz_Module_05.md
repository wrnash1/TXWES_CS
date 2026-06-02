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
