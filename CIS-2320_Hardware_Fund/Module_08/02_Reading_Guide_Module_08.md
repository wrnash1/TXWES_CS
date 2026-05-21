# Reading Guide: Module 08 - Custom PC Configurations
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 08 - Custom PC Configurations**! This module covers how a technician selects and matches hardware components to specific real-world workload requirements. Rather than building one generic PC, professionals must evaluate the intended use case — graphic design, video editing, virtualization, gaming, or home server — and choose components that optimize performance, reliability, and budget for that purpose. These selection decisions are tested on the **CompTIA A+ Core 1 (220-1101)** exam.

As a technician, you must be able to recommend the right GPU tier, CPU core count, RAM capacity, and storage type for a given scenario. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Component selection for CAD workstations**: CAD (Computer-Aided Design) and video editing workstations require a high-core-count CPU for rendering, a professional-grade GPU (such as NVIDIA Quadro or AMD Radeon Pro) certified for CAD software precision and stability, a minimum of 32–64 GB of ECC or high-speed RAM to handle large model files, and fast NVMe SSD storage to reduce file load and save times. Consumer gaming GPUs can technically run CAD software but lack certified driver support and may produce rendering errors under professional workloads.
*   **virtualization hosts**: A virtualization host runs multiple virtual machines (VMs) simultaneously using a hypervisor such as VMware ESXi, Microsoft Hyper-V, or VirtualBox. Each VM consumes dedicated vCPUs and RAM allocations from the host, making maximum CPU core count and large RAM capacity (64 GB+) the primary hardware requirements. Storage speed matters for VM disk I/O; fast NVMe or RAID arrays reduce VM load times. A dedicated GPU is generally not required unless VMs require GPU passthrough for graphics workloads.
*   **gaming PCs**: A gaming PC prioritizes GPU performance above all other components, as the graphics card is responsible for rendering frames at the target resolution and refresh rate. A mid-to-high-tier CPU with fast single-threaded performance (high clock speed), 16–32 GB of DDR4/DDR5 RAM, and a fast NVMe SSD for game asset loading complete the build. High-refresh-rate monitors (144Hz or 240Hz) require the GPU to sustain matching frame rates to deliver the benefit of the display.
*   **NAS and home servers**: A NAS (Network-Attached Storage) or home server prioritizes storage capacity, drive redundancy (RAID 1 or RAID 5), and low power consumption over raw compute performance. NAS builds commonly use low-TDP CPUs, 8–16 GB of ECC RAM for ZFS file systems, and multiple 3.5-inch HDDs in a RAID configuration for large capacity and fault tolerance. A dedicated GPU is unnecessary; onboard or integrated graphics are sufficient for headless server management.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 3.4):** The A+ exam presents scenario questions describing a user's job role and asks which PC configuration is most appropriate. Know the primary differentiator for each build type: CAD = professional GPU + high RAM; virtualization = maximum cores + maximum RAM; gaming = high-end consumer GPU + fast CPU; NAS/server = multiple drives + RAID + ECC RAM.
*   **Scenario Trap:** A common A+ distractor presents a virtualization host scenario and offers a high-end gaming GPU as an answer choice. Virtualization hosts do not require powerful GPUs unless GPU passthrough is explicitly stated — the correct answer for virtualization workloads is always maximum CPU cores and RAM, not GPU.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers custom PC configurations with use-case-specific component comparisons. Navigate to the custom PC configuration section for scenario-based hardware selection guidance: [Professor Messer's CompTIA A+ Core 1 Course — Custom PC Configurations](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Review the workstation and gaming build comparisons specifically.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the custom PC configuration section in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on workstation types, gaming PCs, virtualization hosts, and NAS/home servers.
*   **Required Video:** Watch the video lecture on custom PC configurations from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering use-case hardware selection and the differences between workstation, gaming, and server builds.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Build a bill-of-materials for a virtualization host prioritizing RAM and CPU cores**: Research CPU options with 8+ cores and at least 64 GB RAM capacity. Document the component list with TDP values, slot counts, and total estimated power draw. Verify the motherboard supports the required number of DIMM slots and PCIe lanes.
*   **Select appropriate GPU and cooling for a gaming system**: Compare a mid-range and high-end consumer GPU by benchmark scores at 1080p and 1440p. Identify the GPU's TDP and confirm the PSU wattage provides adequate headroom. Select a CPU cooler rated above the CPU's TDP.
*   **Determine storage redundancy requirements for a NAS**: Calculate the usable capacity of a 4-drive array in RAID 5 versus RAID 10 configuration using identical 4 TB drives. Document which RAID level provides more usable space and which provides faster write performance.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the custom PC configuration sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on custom PC configurations in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the build selection steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
