# Reading Guide: Module 08 - Custom PC Configurations

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


## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.4

---

## Introduction

Welcome to Module 08. This module covers one of the most scenario-heavy sections of the CompTIA A+ Core 1 exam: custom PC configurations. A technician is rarely asked to build a generic "PC." In professional practice, you evaluate the user's workload, identify the primary hardware bottleneck for that workload, and select components that address that bottleneck within budget constraints.

The A+ exam tests four specific build types under Domain 3.4: CAD and professional workstations, virtualization hosts, gaming PCs, and NAS or home servers. Each build type has a distinct hierarchy of component priorities, and the exam deliberately constructs distractors that offer plausible but incorrect components. Understanding not only the right answer but why the wrong answers are wrong is essential for a high exam score.

Read this guide completely before beginning the lab. Pay particular attention to the specification tables, the RAID comparison section, and the exam tips.

---

## Section 1 — The Four Build Types: Overview and Primary Differentiators

Before drilling into each build type, memorize this priority hierarchy. The A+ exam scenario will describe a user's job role, and your first task is to map that role to the correct build type.

| User Role or Workload | Build Type | Primary Hardware Priority |
|---|---|---|
| Architect, engineer, animator, video editor | CAD / Professional Workstation | Professional GPU + ECC RAM |
| IT admin running multiple VMs, developer testing environments | Virtualization Host | Maximum CPU cores + maximum RAM |
| PC gamer targeting 1080p, 1440p, or 4K | Gaming PC | High-performance consumer GPU |
| Home user storing backups, media, surveillance footage | NAS / Home Server | Drive count + RAID level + low power |

---

## Section 2 — CAD and Professional Workstations

### What Makes a Workstation Different from a Gaming PC

The single most tested concept in this build category is the difference between a professional GPU and a consumer gaming GPU. These two product lines are physically similar but serve fundamentally different purposes.

**Professional GPUs** (NVIDIA RTX A-series / formerly Quadro; AMD Radeon Pro) use drivers that are validated and certified against specific professional software titles. CAD software vendors maintain a hardware compatibility list (HCL) that identifies which GPU driver versions are certified for each release. When an engineer renders a complex structural assembly in SolidWorks, the certified driver guarantees mathematical precision in geometry calculations, stable long-duration rendering, and support for features like Quadro Sync for multi-display workstation configurations.

**Consumer gaming GPUs** (NVIDIA GeForce, AMD Radeon RX) use drivers optimized for maximum frame rates and visual quality in games. These drivers are not validated against professional CAD software and may produce rendering artifacts, stability failures, or incorrect output in professional applications. Using a gaming GPU on a CAD workstation is a common technician mistake that the A+ exam specifically targets.

### CAD Workstation Component Specifications

| Component | Minimum Recommended | Professional Tier | Notes |
|---|---|---|---|
| GPU | NVIDIA RTX A2000 / AMD Radeon Pro W6400 | NVIDIA RTX A5000 / AMD Radeon Pro W6800 | Must be on software vendor HCL |
| CPU | 8-core, 3.5+ GHz | 16-24 core workstation CPU | High core count for rendering |
| RAM | 32 GB DDR4 ECC | 64-128 GB ECC registered | ECC preferred; large model files demand capacity |
| System Storage | 512 GB NVMe SSD | 1-2 TB NVMe SSD | Fast scratch disk reduces file load time |
| PSU | 550W+ 80 Plus Gold | 750W+ for multi-GPU | Professional GPUs draw less power than gaming GPUs |
| Cooling | High-performance air cooler | Tower cooler or 240mm AIO | Sustained rendering loads generate sustained heat |

### Video Editing Workstation Notes

Video editing builds share the same priorities as CAD workstations with one addition: dedicated fast storage for video scratch files. Editing 4K or 8K video requires high sustained sequential read/write speeds. NVMe RAID or dedicated NVMe scratch drives are common in professional video editing builds.

---

## Section 3 — Virtualization Hosts

### The Core Concept

A virtualization host runs a hypervisor — software that creates and manages virtual machines. Each virtual machine (VM) is allocated a share of the host's physical CPU cores (as vCPUs), physical RAM, and storage. Multiple VMs run simultaneously, and each VM's resource allocation is drawn from the host's physical pool.

The critical implication: every VM running on a host consumes real CPU cores and real RAM. If you run 10 VMs, you need enough physical resources to satisfy all 10 VMs plus the hypervisor's own overhead simultaneously.

### Virtualization Host Component Specifications

| Component | Minimum | Recommended | Rationale |
|---|---|---|---|
| CPU | 8 cores (16 threads) | 16-32 cores | Each VM's vCPU allocation draws from physical cores |
| RAM | 32 GB | 64-256 GB | Each VM's RAM is reserved from physical RAM |
| Storage | 1 TB SATA SSD | 2-4 TB NVMe or RAID | VM virtual disk files require fast sequential I/O |
| GPU | Integrated graphics | Low-end discrete GPU | Only management display needed; no 3D rendering |
| NIC | 1 GbE | 10 GbE | Multiple VMs sharing network; bandwidth matters |
| PSU | 400W | 600W+ for high core-count CPU | High core-count CPUs have higher TDP |

### The Virtualization Host RAM Math

When sizing a virtualization host, technicians use this calculation:

Total RAM needed = (number of VMs x RAM per VM) + hypervisor overhead + host OS overhead

Example: 8 VMs at 8 GB each = 64 GB for VMs + approximately 8-16 GB for hypervisor and host OS = 72-80 GB minimum. A 128 GB host provides adequate headroom.

### What Virtualization Hosts Do NOT Need

- High-end gaming or professional GPU (unless GPU passthrough is required for a specific VM)
- High clock speed single-core CPU performance (multithreaded throughput matters, not single-thread speed)
- RAID 0 storage (no fault tolerance — VM data is unrecoverable on a stripe failure)

---

## Section 4 — Gaming PCs

### GPU-First Design

A gaming PC is designed around the display's target resolution and refresh rate. The GPU must produce enough rendered frames per second to match or exceed the monitor's refresh rate. Everything else in a gaming build supports the GPU.

### Gaming PC Resolution and GPU Tier Guide

| Target Resolution | Target Refresh Rate | GPU Tier Required | Example Benchmark |
|---|---|---|---|
| 1080p | 60 Hz | Entry to mid-range | Capable of 60+ FPS in modern titles at high settings |
| 1080p | 144-240 Hz | Mid to high-range | Sustained 144+ FPS demands significantly more GPU power |
| 1440p | 60-144 Hz | High-range | 1440p increases GPU load by roughly 70% vs. 1080p |
| 4K | 60 Hz | High to enthusiast | 4K requires 4x the pixel fill rate of 1080p |

### Gaming PC Component Priorities

| Component | Role in Gaming | Key Consideration |
|---|---|---|
| GPU | Renders frames — primary performance driver | Match GPU tier to target resolution and frame rate |
| CPU | Feeds the GPU with game logic and AI calculations | Fast single-thread performance; modern 6-8 core sufficient |
| RAM | Holds active game assets and OS working set | 16 GB DDR4/DDR5 minimum; 32 GB for future-proofing |
| Storage | Loads game assets from disk | NVMe SSD reduces load times vs. SATA SSD or HDD |
| Monitor | Displays the rendered output | Refresh rate and resolution must match GPU capability |
| PSU | Powers all components | GPU TDP + system TDP + 20% headroom = PSU wattage |

### CPU and GPU Balance

A gaming build should not have a dramatically imbalanced CPU and GPU. Pairing a very slow CPU with a high-end GPU causes CPU bottlenecking — the GPU sits idle waiting for the CPU to feed it draw calls. Pairing a fast CPU with a weak GPU wastes CPU budget. Balanced builds maximize frame rates per dollar spent.

---

## Section 5 — NAS and Home Servers

### Storage as the Primary Design Goal

A NAS (Network-Attached Storage) server's primary purpose is to store large volumes of data reliably over long periods. Power consumption, drive capacity, and redundancy are the design priorities. CPU and GPU performance are secondary.

### RAID Levels for NAS Builds

This table is heavily tested on the A+ exam. Know all four levels.

| RAID Level | Minimum Drives | Fault Tolerance | Usable Capacity | Read Performance | Write Performance | Best Use Case |
|---|---|---|---|---|---|---|
| RAID 0 | 2 | None — one failure loses all data | 100% of total | Very fast | Very fast | Scratch/temp storage only; never for backups |
| RAID 1 | 2 | 1 drive failure | 50% of total | Good (reads from either) | Slower (writes to both) | Small NAS with two drives |
| RAID 5 | 3 | 1 drive failure | Total minus 1 drive | Good | Moderate | Best balance of space and redundancy for 3-6 drives |
| RAID 6 | 4 | 2 drive failures | Total minus 2 drives | Good | Slower than RAID 5 | Large arrays with high-capacity drives (slow rebuild time risk) |
| RAID 10 | 4 | 1 drive per mirror pair | 50% of total | Excellent | Excellent | When performance and redundancy both matter |

### RAID 5 Usable Capacity Formula

For N drives of size S each in RAID 5:

Usable capacity = (N - 1) x S

Example: 4 drives x 4 TB each in RAID 5 = (4 - 1) x 4 TB = 12 TB usable.

### NAS Component Considerations

| Component | NAS Requirement | Rationale |
|---|---|---|
| CPU | Low TDP (15-35W range) | NAS runs 24/7; power bill matters over months and years |
| RAM | 8-16 GB ECC | ZFS file system requires ECC to prevent silent data corruption |
| Drives | 3.5-inch NAS-rated HDDs | Designed for 24/7 operation; standard desktop drives not rated for continuous spin |
| GPU | Integrated or none | Headless operation; no 3D rendering needed |
| NIC | 1 GbE minimum; 2.5 GbE or 10 GbE for large households | Determines maximum network transfer speed |
| Enclosure | Minimum 4 drive bays | More bays = more RAID flexibility |

### ECC RAM and ZFS

Error-Correcting Code (ECC) RAM detects and corrects single-bit memory errors in real time. Standard non-ECC RAM cannot do this. When ZFS writes data, it uses RAM as a write-back cache. If a non-ECC RAM module experiences a bit flip (a 0 becoming a 1 or vice versa), that corrupted data can be written to disk without detection. ZFS was designed with ECC RAM as an assumption; running ZFS on non-ECC RAM is a widely documented risk for NAS builds.

---

## Section 6 — High-Yield Glossary

**CAD (Computer-Aided Design):** Software category used by engineers and architects to create 2D drawings and 3D models. Examples: AutoCAD, SolidWorks, Revit, CATIA. Requires professional GPU with certified drivers.

**Professional GPU:** A graphics card engineered for workstation use with certified drivers for professional software. NVIDIA RTX A-series (formerly Quadro) and AMD Radeon Pro are the primary lines. Distinct from consumer gaming GPUs in driver certification and ECC VRAM support.

**Consumer Gaming GPU:** A graphics card optimized for maximum frame rates in games. NVIDIA GeForce and AMD Radeon RX product lines. Not certified for professional CAD software.

**Hypervisor:** Software that creates and manages virtual machines on a physical host. Type 1 hypervisors (bare-metal): VMware ESXi, Microsoft Hyper-V. Type 2 hypervisors (hosted): VirtualBox, VMware Workstation.

**Virtual Machine (VM):** An isolated software-based computer that runs inside a hypervisor. Each VM has its own OS, allocated vCPUs, allocated RAM, and virtual disk storage.

**vCPU:** Virtual CPU — a logical CPU allocation assigned to a VM. Maps to physical CPU threads on the host.

**ECC RAM (Error-Correcting Code RAM):** RAM that detects and corrects single-bit memory errors automatically. Required for ZFS-based NAS builds and recommended for professional workstations.

**RAID (Redundant Array of Independent Disks):** A technology that combines multiple physical drives into a logical array for redundancy, performance, or both. Key levels for A+ exam: 0, 1, 5, 6, 10.

**RAID 0 (Striping):** Data striped across drives for maximum speed and capacity. No fault tolerance.

**RAID 1 (Mirroring):** Data written identically to two drives. Survives one drive failure. 50% capacity efficiency.

**RAID 5 (Striping with Distributed Parity):** Data and parity striped across 3+ drives. Survives one drive failure. Capacity = total minus one drive.

**RAID 10 (Mirror + Stripe):** Requires 4+ drives. Combines RAID 1 and RAID 0. Survives one drive failure per mirror pair. 50% capacity efficiency but high performance.

**NAS (Network-Attached Storage):** A dedicated file server connected to a local network, providing centralized storage accessible by multiple devices. Often runs a specialized OS such as TrueNAS or Synology DSM.

**TDP (Thermal Design Power):** The maximum sustained heat output a component produces under full load, measured in watts. Used to size CPU coolers and calculate PSU requirements.

**GPU Passthrough:** A virtualization configuration where a physical GPU is dedicated exclusively to a single VM, bypassing the hypervisor's virtualized graphics layer. Requires CPU and motherboard support for IOMMU (Intel VT-d or AMD-Vi).

**ZFS:** A file system and logical volume manager designed for NAS and server use. Key features include data integrity checksums, built-in RAID-Z (similar to RAID 5/6), and write-back caching in RAM. Requires ECC RAM for maximum data integrity.

**PSU (Power Supply Unit):** Converts AC mains power to DC voltages required by PC components. Sized in watts. 80 Plus certification indicates efficiency rating. Should be sized with 20% headroom above peak system load.

---

## Section 7 — Certification Exam Tips

The following traps appear regularly on A+ Core 1 scenario questions for Domain 3.4. Memorize each one.

**Trap 1 — Virtualization host GPU distractor.** A virtualization host scenario will often include a high-end GPU as an answer choice. Unless the scenario explicitly mentions GPU passthrough for a specific VM, the correct answer is maximum CPU cores and RAM. A GPU does not run VMs.

**Trap 2 — Consumer GPU for CAD software.** A scenario will describe a professional design workstation running CAD software poorly. The issue is the GPU type, not the GPU performance tier. Even a high-end consumer GPU lacks the certified drivers required for CAD software. The answer is a professional GPU (Quadro/Radeon Pro), not a faster GeForce.

**Trap 3 — RAID 0 offered as a redundancy solution.** RAID 0 provides zero fault tolerance. It will appear as a distractor in NAS scenarios where redundancy is required. RAID 0 is never correct when the question asks about protecting data.

**Trap 4 — Type-C implies Thunderbolt or USB 3.x speed.** This trap applies to peripheral scenarios but can appear alongside custom PC port selection. A USB-C port may deliver USB 2.0 speeds. The connector shape does not determine the speed — the host controller does.

**Trap 5 — Clock speed over core count for virtualization.** A distractor in virtualization scenarios offers a high clock-speed processor with fewer cores versus a lower clock-speed processor with more cores. For virtualization, core count wins. VMs run concurrently and each needs dedicated vCPU allocations.

**Trap 6 — NAS does not need a gaming GPU.** A NAS scenario answer choice may include a mid-range consumer GPU. A NAS serves files over the network. It has no 3D rendering requirement. Any GPU recommendation for a NAS (beyond integrated graphics for headless management) is wrong.

**Trap 7 — RAID 5 versus RAID 10 capacity.** The exam may ask which RAID level provides more usable storage from a four-drive array. RAID 5 gives three drives' worth of usable space (75% efficiency). RAID 10 gives two drives' worth (50% efficiency). For maximum usable space, RAID 5 wins with four drives. For maximum performance and redundancy, RAID 10 wins.

**Trap 8 — PSU wattage for gaming builds.** A gaming scenario may describe system instability under load. The cause can be an undersized PSU that cannot sustain the GPU's peak power draw during heavy rendering. Always verify that PSU wattage covers CPU TDP + GPU TDP + system overhead + 20% headroom.

---

## Section 8 — Study Checklist

- [ ] Memorize the four build types and their primary hardware priorities from the overview table in Section 1.
- [ ] Study the CAD workstation component specification table and understand why professional GPUs differ from consumer GPUs.
- [ ] Work through the virtualization host RAM math: practice calculating total RAM needed for a given number of VMs.
- [ ] Memorize all five RAID levels in the comparison table: minimum drives, fault tolerance, usable capacity formula, and best use case.
- [ ] Review the eight exam traps in Section 7 and be able to explain why each distractor is wrong.
- [ ] Read the custom PC configuration section in Professor Messer's CompTIA A+ study notes at professormesser.com (navigate to 220-1101 section).
- [ ] Watch Professor Messer's video on custom PC configurations at professormesser.com, focusing on use-case hardware selection.
- [ ] Complete the Module 08 Lab before attempting the quiz.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 free study notes and video course: professormesser.com (220-1101 section, Domain 3.4)
- CompTIA A+ Exam Objectives (220-1101): comptia.org (free download; review Domain 3.4 objectives in full)

---

## 9. Supplemental Resources

1. **Professor Messer — Custom PC Configurations (220-1101 Free Video)**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video covering the four custom PC build types (CAD workstation, virtualization host, gaming PC, NAS) directly aligned to Domain 3.4 objectives and Module 08 exam questions.

2. **VirtualBox (Free Type 2 Hypervisor)**
   URL: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
   Relevance: Free, open-source Type 2 hypervisor for Windows, macOS, and Linux. Use for the Challenge Exercise to create and run actual virtual machines, giving hands-on experience with the virtualization concepts covered in this module.

3. **TrueNAS SCALE (Free NAS OS)**
   URL: [https://www.truenas.com/truenas-scale/](https://www.truenas.com/truenas-scale/)
   Relevance: Free, open-source NAS operating system built on ZFS. Review the documentation to understand real-world NAS hardware requirements (ECC RAM, NAS-rated drives, RAID-Z configuration) as described in the Module 08 reading guide.

4. **Puget Systems Workstation Guides (Free Reference)**
   URL: [https://www.pugetsystems.com/recommended/](https://www.pugetsystems.com/recommended/)
   Relevance: Free professional workstation hardware recommendations with application-specific benchmark data for CAD (SolidWorks, AutoCAD), video editing, and 3D rendering. Reinforces the professional vs. consumer GPU distinction and the After Effects RAM scaling discussion.

5. **PCPartPicker — Build Showcase (Free)**
   URL: [https://pcpartpicker.com/builds/](https://pcpartpicker.com/builds/)
   Relevance: Community PC build database with component lists and total cost estimates. Browse completed builds tagged as "Workstation," "NAS," "Gaming," and "Server" to see real-world examples of how the component selection principles from this module are applied in practice.
