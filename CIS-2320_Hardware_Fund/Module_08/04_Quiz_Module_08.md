# Quiz: Module 08 - Custom PC Configurations
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What is the most critical hardware component when designing a virtualization workstation?
*   A) High-end GPU
*   B) Fast mechanical HDD
*   C) Maximum CPU cores and RAM
*   D) Liquid nitrogen cooling
*   **Correct Answer:** C) Virtual machines run concurrently and consume logical cores and physical RAM allocations directly.
*   **Distractor Analysis:**
    *   *Why correct:* Virtual machines run concurrently and consume logical cores and physical RAM allocations directly.
    *   Virtualization hosts do not require heavy 3D rendering GPUs or slow hard drives.

---

**Question 2**
In the context of PC hardware, which of the following most accurately describes **component selection for a CAD workstation**?
*   A) A CAD workstation requires a professional-grade GPU certified for CAD software (such as NVIDIA Quadro or AMD Radeon Pro), a high-core-count CPU for rendering, 32–64 GB of RAM, and fast NVMe storage — prioritizing stability and precision over raw consumer gaming performance.
*   B) A CAD workstation is built around the highest-end consumer gaming GPU available, because gaming cards produce the most frames per second and frame rate directly translates to CAD rendering speed.
*   C) A CAD workstation requires only a fast CPU and large SSD; the GPU is irrelevant because CAD applications perform all geometry calculations on the CPU rather than the graphics hardware.
*   D) A CAD workstation is identical in component selection to a NAS server — both prioritize large-capacity HDDs in RAID arrays because CAD files must be stored redundantly on local drives.
*   **Correct Answer:** A) A CAD workstation requires a professional-grade GPU certified for CAD software (such as NVIDIA Quadro or AMD Radeon Pro), a high-core-count CPU for rendering, 32–64 GB of RAM, and fast NVMe storage — prioritizing stability and precision over raw consumer gaming performance.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the component priorities for a CAD/professional workstation: certified professional GPU, high core count CPU, large RAM, and fast storage — all of which are tested in A+ scenario questions.
    * *Why B is incorrect:* Consumer gaming GPUs lack the certified drivers required for CAD software accuracy; professional workstation GPUs are purpose-built for precision rendering and stability, not maximum frame rates.
    * *Why C is incorrect:* The GPU handles 3D viewport rendering, shading, and real-time model display in CAD applications; it is a critical component, not irrelevant.
    * *Why D is incorrect:* A CAD workstation and a NAS server have opposing priorities; NAS emphasizes multi-drive storage and RAID redundancy, while CAD emphasizes compute power and a professional GPU.


---

**Question 3**
A small business wants to run eight virtual machines simultaneously on a single physical server. The VMs will each be allocated 2 vCPUs and 8 GB RAM. Which hardware configuration best supports this workload?
*   A) Intel Core i5 (6 cores), 32 GB RAM, 512 GB SATA SSD
*   B) Intel Core i9 (24 cores), 128 GB RAM, 2 TB NVMe SSD
*   C) Intel Core i7 (8 cores), 16 GB RAM, 1 TB NVMe SSD with a high-end gaming GPU
*   D) AMD Ryzen 5 (6 cores), 64 GB RAM, 4 TB HDD RAID 0
*   **Correct Answer:** B) Intel Core i9 (24 cores), 128 GB RAM, 2 TB NVMe SSD
*   **Distractor Analysis:**
    * *Why B is correct:* Eight VMs at 2 vCPUs each requires 16 logical cores minimum; 128 GB RAM covers 8 × 8 GB VM allocation plus host OS overhead. Fast NVMe storage reduces VM disk I/O latency across concurrent workloads.
    * *Why A is incorrect:* 6 cores and 32 GB RAM cannot support eight concurrent 2-vCPU/8 GB VMs; the RAM alone is insufficient (8 × 8 GB = 64 GB needed before host overhead).
    * *Why C is incorrect:* 16 GB RAM is far below the 64 GB minimum needed; a high-end gaming GPU adds unnecessary cost and power draw for a headless virtualization host that does not need 3D rendering.
    * *Why D is incorrect:* RAID 0 provides no fault tolerance and a single drive failure destroys all VM data; a production virtualization host requires a reliable storage solution, not a performance-only stripe with zero redundancy.


---

**Question 4**
A user wants to build a gaming PC targeting 1440p resolution at 144Hz. They have selected a powerful CPU and fast RAM. Which component decision most directly determines whether the 144Hz target is achievable in-game?
*   A) Selecting a motherboard with a high-end chipset that includes a built-in 144Hz signal booster on the PCIe bus
*   B) Selecting a GPU powerful enough to render at least 144 frames per second at 1440p in the target games
*   C) Selecting a 144Hz-capable monitor with a DisplayPort input, which automatically forces the GPU to render at 144 fps
*   D) Selecting DDR5 RAM over DDR4, because memory bandwidth is the sole bottleneck limiting frame rates above 60 fps
*   **Correct Answer:** B) Selecting a GPU powerful enough to render at least 144 frames per second at 1440p in the target games
*   **Distractor Analysis:**
    * *Why B is correct:* The GPU must render enough frames per second to match the display's refresh rate; a 144Hz monitor only delivers 144 unique frames per second if the GPU is producing that output. GPU selection is the primary determinant of achievable in-game frame rates.
    * *Why A is incorrect:* Motherboard chipsets do not contain frame rate boosters; the chipset manages I/O, PCIe lane distribution, and connectivity — it does not render graphics frames.
    * *Why C is incorrect:* A monitor cannot force the GPU to produce a specific frame rate; the monitor reports its capabilities to the GPU driver, but actual frame output depends entirely on the GPU's rendering performance.
    * *Why D is incorrect:* While RAM speed has a minor effect on frame rates in CPU-bound scenarios, it is not the sole or primary bottleneck above 60 fps; GPU performance is the dominant factor at 1440p resolution.


---

**Question 5**
A home user wants to set up a NAS with four 4 TB drives to store family photos, videos, and backups. They want both drive redundancy and maximum usable storage capacity from the four drives. Which RAID level best meets both requirements?
*   A) RAID 5 — distributes parity across all four drives, allowing one drive failure while providing 12 TB of usable storage from four 4 TB drives
*   B) RAID 0 — stripes all four drives together for 16 TB usable capacity and the highest sequential read and write performance
*   C) RAID 1 — mirrors data across all four drives for four copies of every file, maximizing redundancy at the cost of usable capacity
*   D) RAID 10 — combines mirroring and striping across the four drives for both redundancy and high performance, providing 8 TB of usable storage
*   **Correct Answer:** A) RAID 5 — distributes parity across all four drives, allowing one drive failure while providing 12 TB of usable storage from four 4 TB drives
*   **Distractor Analysis:**
    * *Why A is correct:* RAID 5 uses one drive's worth of capacity for distributed parity (4 × 4 TB − 4 TB = 12 TB usable) while surviving one drive failure — the best balance of redundancy and usable capacity for a four-drive home NAS.
    * *Why B is incorrect:* RAID 0 provides zero redundancy; one drive failure destroys all data, making it completely unsuitable for a backup and long-term storage NAS.
    * *Why C is incorrect:* Standard RAID 1 is a two-drive mirror; a four-drive RAID 1 configuration is non-standard and wastes 75% of capacity — RAID 1 does not scale efficiently beyond two drives in most implementations.
    * *Why D is incorrect:* RAID 10 provides 8 TB usable from four 4 TB drives (50% efficiency), which is less than RAID 5's 12 TB; while RAID 10 offers better write performance, RAID 5 provides more usable capacity for the same drive count, better meeting the "maximum usable storage" requirement.
