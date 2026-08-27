# Quiz: Module 08 - Custom PC Configurations

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.4
**Total Questions:** 10 | **Points:** 10 (1 point each)

---

### Question 1

What is the most critical hardware component when designing a virtualization workstation?

- A) High-end consumer GPU
- B) Fast mechanical HDD
- C) Maximum CPU cores and RAM
- D) Liquid nitrogen cooling

**Correct Answer:** C — Virtual machines run concurrently and each VM is allocated a share of the host's physical CPU cores and RAM. Core count and RAM capacity are the primary bottlenecks for virtualization hosts.

**Distractor Analysis:**

- *Why A is incorrect:* A virtualization host does not perform 3D rendering. A high-end GPU adds cost and power draw without improving VM performance unless GPU passthrough is explicitly configured.
- *Why B is incorrect:* Mechanical HDDs introduce high latency for VM disk I/O. When multiple VMs perform disk operations simultaneously, slow storage creates a significant bottleneck. Fast NVMe or SSD storage is preferred.
- *Why D is incorrect:* Liquid nitrogen cooling is an extreme overclocking technique used in competitive benchmarking, not in production virtualization hosts.

---

### Question 2

In the context of PC hardware, which of the following most accurately describes component selection for a CAD workstation?

- A) A CAD workstation requires a professional-grade GPU certified for CAD software (such as NVIDIA RTX A-series or AMD Radeon Pro), a high-core-count CPU for rendering, 32-64 GB of RAM, and fast NVMe storage — prioritizing stability and precision over raw consumer gaming performance.
- B) A CAD workstation is built around the highest-end consumer gaming GPU available, because gaming cards produce the most frames per second and frame rate directly translates to CAD rendering speed.
- C) A CAD workstation requires only a fast CPU and large SSD; the GPU is irrelevant because CAD applications perform all geometry calculations on the CPU rather than the graphics hardware.
- D) A CAD workstation is identical in component selection to a NAS server — both prioritize large-capacity HDDs in RAID arrays because CAD files must be stored redundantly on local drives.

**Correct Answer:** A — This accurately describes the component priorities for a CAD/professional workstation. The certified driver support of a professional GPU, not raw frame rate, is the key differentiator. High core count, large RAM, and fast storage address the rendering and file-handling demands of professional design software.

**Distractor Analysis:**

- *Why B is incorrect:* Consumer gaming GPUs lack the certified drivers required for CAD software accuracy. Professional workstation GPUs are purpose-built for precision rendering and stability, not maximum frame rates.
- *Why C is incorrect:* The GPU handles 3D viewport rendering, shading, and real-time model display in CAD applications. It is a critical component, not irrelevant.
- *Why D is incorrect:* A CAD workstation and a NAS server have opposing priorities. NAS emphasizes multi-drive storage capacity and RAID redundancy. CAD emphasizes compute power, professional GPU certification, and fast RAM.

---

### Question 3

A small business wants to run eight virtual machines simultaneously on a single physical server. The VMs will each be allocated 2 vCPUs and 8 GB RAM. Which hardware configuration best supports this workload?

- A) Intel Core i5 (6 cores), 32 GB RAM, 512 GB SATA SSD
- B) Intel Core i9 (24 cores), 128 GB RAM, 2 TB NVMe SSD
- C) Intel Core i7 (8 cores), 16 GB RAM, 1 TB NVMe SSD with a high-end gaming GPU
- D) AMD Ryzen 5 (6 cores), 64 GB RAM, 4 TB HDD in RAID 0

**Correct Answer:** B — Eight VMs at 2 vCPUs each requires 16 logical cores minimum for VMs alone, plus hypervisor overhead. 128 GB RAM covers 8 x 8 GB = 64 GB for VMs plus substantial host overhead. Fast NVMe storage reduces VM disk I/O latency across concurrent workloads.

**Distractor Analysis:**

- *Why A is incorrect:* 6 cores and 32 GB RAM cannot support eight concurrent 2-vCPU/8 GB VMs. The RAM alone is insufficient — 8 x 8 GB = 64 GB needed before any host overhead.
- *Why C is incorrect:* 16 GB RAM is far below the 64 GB minimum needed for VM allocations alone. A high-end gaming GPU adds unnecessary cost for a headless virtualization host that does not require 3D rendering.
- *Why D is incorrect:* RAID 0 provides no fault tolerance. A single drive failure destroys all VM data. A production virtualization host requires fault-tolerant storage, not a performance-only stripe array.

---

### Question 4

A user wants to build a gaming PC targeting 1440p resolution at 144 Hz. They have selected a powerful CPU and fast RAM. Which component decision most directly determines whether the 144 Hz target is achievable in-game?

- A) Selecting a motherboard with a high-end chipset that includes a built-in 144 Hz signal booster on the PCIe bus
- B) Selecting a GPU powerful enough to render at least 144 frames per second at 1440p in the target games
- C) Selecting a 144 Hz-capable monitor with a DisplayPort input, which automatically forces the GPU to render at 144 fps
- D) Selecting DDR5 RAM over DDR4, because memory bandwidth is the sole bottleneck limiting frame rates above 60 fps

**Correct Answer:** B — The GPU must render enough frames per second to match the display's refresh rate. A 144 Hz monitor only delivers 144 unique frames per second if the GPU is producing that output. GPU selection is the primary determinant of achievable in-game frame rates at any resolution.

**Distractor Analysis:**

- *Why A is incorrect:* Motherboard chipsets do not contain frame rate boosters. The chipset manages I/O, PCIe lane distribution, and connectivity — it does not render graphics frames.
- *Why C is incorrect:* A monitor cannot force the GPU to produce a specific frame rate. The monitor reports its capabilities via EDID, but actual frame output depends entirely on the GPU's rendering performance.
- *Why D is incorrect:* RAM speed has a minor effect in CPU-bound scenarios at low resolutions, but is not the sole or primary bottleneck above 60 fps. GPU performance is the dominant factor at 1440p.

---

### Question 5

A home user wants to set up a NAS with four 4 TB drives to store family photos, videos, and backups. They want both drive redundancy and maximum usable storage capacity from the four drives. Which RAID level best meets both requirements?

- A) RAID 5 — distributes parity across all four drives, allowing one drive failure while providing 12 TB of usable storage from four 4 TB drives
- B) RAID 0 — stripes all four drives together for 16 TB usable capacity and the highest sequential read and write performance
- C) RAID 1 — mirrors data across all four drives for multiple copies of every file, maximizing redundancy at the cost of usable capacity
- D) RAID 10 — combines mirroring and striping across the four drives for both redundancy and high performance, providing 8 TB of usable storage

**Correct Answer:** A — RAID 5 uses one drive's worth of capacity for distributed parity (4 x 4 TB - 4 TB = 12 TB usable) while surviving one drive failure. This is the best balance of redundancy and usable capacity for a four-drive home NAS.

**Distractor Analysis:**

- *Why B is incorrect:* RAID 0 provides zero fault tolerance. One drive failure destroys all data in the array, making it completely unsuitable for a backup NAS.
- *Why C is incorrect:* Standard RAID 1 is a two-drive mirror. A four-drive RAID 1 wastes 75% of capacity and does not scale efficiently beyond two drives for maximizing usable space.
- *Why D is incorrect:* RAID 10 provides only 8 TB usable from four 4 TB drives (50% efficiency), less than RAID 5's 12 TB. While RAID 10 offers better write performance, RAID 5 provides more usable capacity — better meeting the "maximum usable storage" requirement.

---

### Question 6

An engineer runs a professional 3D modeling application. After upgrading from an NVIDIA RTX A4000 (professional GPU) to a high-end NVIDIA GeForce RTX 4080 (consumer gaming GPU) to save money, the engineer notices occasional shading errors in complex model renders that were not present before. What is the most likely cause?

- A) The GeForce RTX 4080 has less VRAM than the RTX A4000, causing the model to exceed the GPU's memory limit
- B) The consumer GeForce GPU uses non-certified drivers that are not validated for professional CAD/3D software, leading to rendering precision errors
- C) The PCIe slot on the motherboard is incompatible with the newer GeForce card and requires a BIOS update before professional rendering is stable
- D) The GeForce RTX 4080 runs at too high a clock speed for professional rendering applications, causing arithmetic overflow errors during shading calculations

**Correct Answer:** B — Professional GPUs use drivers validated by the GPU manufacturer against specific software titles. Consumer gaming GPU drivers are optimized for frame rate, not mathematical precision in professional rendering pipelines. Shading artifacts are a known symptom of running uncertified consumer drivers in professional 3D applications.

**Distractor Analysis:**

- *Why A is incorrect:* The GeForce RTX 4080 has 16 GB of VRAM, comparable to many professional GPU configurations. The scenario describes shading errors, not out-of-memory crashes consistent with VRAM exhaustion.
- *Why C is incorrect:* PCIe compatibility is unrelated to driver-level rendering precision. Both GPU models use the same PCIe interface standard; a slot incompatibility would cause the card to be undetected, not produce rendering artifacts.
- *Why D is incorrect:* GPU clock speed does not cause arithmetic overflow in rendering calculations. Shading errors in this context are caused by driver bugs or uncertified behavior, not clock speed.

---

### Question 7

Which of the following best describes the difference between ECC RAM and standard non-ECC RAM in the context of a NAS build running ZFS?

- A) ECC RAM runs at higher clock speeds than non-ECC RAM, improving the NAS file transfer rate over the network
- B) ECC RAM detects and corrects single-bit memory errors automatically, preventing corrupted data from being written to disk through the ZFS write cache
- C) ECC RAM is required because ZFS cannot address more than 16 GB of standard non-ECC RAM due to a 32-bit memory addressing limitation
- D) ECC RAM provides hardware-level encryption of data in transit between RAM and the NAS drives, preventing network eavesdropping

**Correct Answer:** B — ZFS uses system RAM as a write-back cache. If a bit error occurs in non-ECC RAM, the corrupted data can be written to disk without detection. ECC RAM detects and corrects single-bit errors in real time, ensuring data written through the ZFS cache is intact.

**Distractor Analysis:**

- *Why A is incorrect:* ECC RAM does not run at higher clock speeds than non-ECC RAM. ECC adds error detection and correction circuitry, not raw clock speed.
- *Why C is incorrect:* ZFS has no 16 GB non-ECC addressing limitation. The ECC requirement is about data integrity, not addressing capacity.
- *Why D is incorrect:* ECC RAM provides no encryption capability. It is a data integrity feature, not a security or encryption feature. Drive encryption is handled by the operating system or dedicated hardware.

---

### Question 8

A technician is specifying a new video editing workstation for a post-production studio. The editor works with 4K RAW video files and runs multiple color grading and effects render jobs simultaneously. Which storage configuration is most appropriate?

- A) Two 4 TB 7200 RPM HDDs in RAID 1 as the primary working drive
- B) One 4 TB SATA SSD as the primary working drive
- C) One 2 TB NVMe SSD for the OS and applications, plus a second high-speed NVMe drive or NVMe RAID array as a dedicated video scratch disk
- D) A USB 3.0 external HDD for video storage, because USB 3.0 provides sufficient bandwidth for 4K video playback

**Correct Answer:** C — 4K RAW video editing demands high sustained sequential read and write speeds. Separating the OS/application drive from the video scratch disk prevents I/O competition. NVMe provides significantly higher sequential bandwidth than SATA SSD or HDD.

**Distractor Analysis:**

- *Why A is incorrect:* 7200 RPM HDDs in RAID 1 provide approximately 150-200 MB/s sequential read speeds, which is insufficient for real-time 4K RAW editing. RAID 1 also halves write performance by writing to both drives simultaneously.
- *Why B is incorrect:* A single SATA SSD is limited to approximately 550 MB/s sequential throughput. Using one drive forces the OS, applications, and video scratch to compete for the same I/O bandwidth during intensive render sessions.
- *Why D is incorrect:* A USB 3.0 HDD is limited by the HDD's own sequential speed — typically 150-200 MB/s — which is far below what 4K RAW editing requires for real-time playback and rendering.

---

### Question 9

A technician needs to recommend a PC for an IT administrator who manages a lab of 20 desktop workstations. The administrator needs to test software deployments, run simulated network environments, and maintain multiple isolated OS environments simultaneously. Which system is the best recommendation?

- A) A high-end gaming PC with a consumer GeForce RTX 4090, 32 GB DDR5, and a 2 TB NVMe SSD
- B) A workstation-class system with a 32-core CPU, 256 GB ECC RAM, fast NVMe storage, and integrated or low-end discrete graphics
- C) A NAS server with 6 drives in RAID 6 and a low-TDP processor for power efficiency
- D) A standard office desktop with 16 GB RAM, an Intel Core i5 processor, and a 512 GB SATA SSD

**Correct Answer:** B — Running multiple isolated OS environments and simulated network topologies is a virtualization workload. The primary requirements are maximum CPU core count and maximum RAM. Low-end graphics are sufficient since the host does not perform 3D rendering.

**Distractor Analysis:**

- *Why A is incorrect:* A gaming PC prioritizes GPU performance, which is irrelevant to a virtualization host. 32 GB RAM is insufficient for running many concurrent VMs. The RTX 4090 adds significant cost with no benefit for this workload.
- *Why C is incorrect:* A NAS server is designed for file storage, not for running virtual machines with CPU and RAM-intensive workloads. A low-TDP processor cannot handle the concurrent compute demands of multiple active VMs.
- *Why D is incorrect:* 16 GB RAM and 6 cores cannot support multiple concurrent virtual machines with meaningful per-VM resource allocations. This configuration would be immediately CPU and RAM bottlenecked.

---

### Question 10

A RAID 5 array is built using five 2 TB drives. One drive fails and is replaced. During the rebuild process, a second drive also fails before the rebuild completes. What is the result?

- A) The array completes the rebuild using the four remaining drives and no data is lost, because RAID 5 can survive two simultaneous drive failures
- B) The array enters a degraded state with the two failed drives excluded, but all data remains accessible from the three surviving drives
- C) All data on the array is lost because RAID 5 can only survive a single drive failure; a second failure during rebuild results in unrecoverable data loss
- D) The array automatically converts to RAID 1 between the three surviving drives to preserve the data during the second failure

**Correct Answer:** C — RAID 5 tolerates exactly one drive failure. During a rebuild the array is in a degraded state with no redundancy. If a second drive fails before the rebuild completes, there is insufficient parity information to reconstruct the data, resulting in total array failure and complete data loss.

**Distractor Analysis:**

- *Why A is incorrect:* RAID 5 cannot survive two simultaneous drive failures. RAID 6 is the level designed to survive two concurrent failures by using double distributed parity.
- *Why B is incorrect:* A RAID 5 array degraded by one drive is still readable via parity reconstruction. However, when a second drive fails, parity is no longer sufficient to reconstruct missing data from two drives simultaneously.
- *Why D is incorrect:* RAID arrays do not automatically convert between levels during failure events. Conversion between RAID levels requires deliberate administrative action on a fully healthy array.

---

### Question 11

A graphic design studio needs a workstation to run Adobe After Effects with complex visual effects compositing on 6K footage. What is the MOST important hardware specification to prioritize?

- A) CPU core count above all else, as After Effects is primarily a multi-threaded renderer
- B) GPU with a large VRAM pool and certified GPU-accelerated rendering support (CUDA or OpenCL)
- C) Maximum RAM capacity combined with fast storage, as After Effects is primarily RAM-limited for frame caching
- D) Maximum storage capacity in RAID 0 to ensure frame reads never bottleneck the render pipeline

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Adobe After Effects is famously RAM-intensive. It caches rendered frames in RAM for real-time playback ("RAM Preview"). More RAM means more frames cached before requiring a disk read. Large projects on 6K footage require 64–128 GB of RAM to avoid constant re-rendering. Fast NVMe storage serves as the overflow cache (disk cache). RAM is the primary bottleneck for most After Effects workflows.
- *Why A is incorrect:* While After Effects uses multi-threading during renders, the primary user-facing bottleneck in typical workflows is RAM (frame cache) and storage cache, not CPU core saturation. After Effects does not scale as linearly with core count as video encoding.
- *Why B is incorrect:* GPU acceleration (Mercury GPU Acceleration) helps with certain effects and previews in After Effects, but the GPU is not the primary bottleneck for most compositing work. RAM remains the dominant constraint.
- *Why D is incorrect:* RAID 0 increases sequential throughput and usable capacity but provides zero fault tolerance. Recommending RAID 0 for production data is poor practice. More importantly, storage is a secondary bottleneck compared to RAM in After Effects.

---

### Question 12

Which of the following BEST describes what distinguishes a professional workstation GPU (NVIDIA RTX A-series) from a consumer gaming GPU (NVIDIA GeForce RTX)?

- A) Professional GPUs have more CUDA cores and faster memory than consumer GPUs at the same price point
- B) Professional GPUs have certified drivers for CAD and DCC software and support ECC VRAM for error correction; consumer GPUs do not
- C) Professional GPUs use a different PCIe connector that is incompatible with consumer motherboards
- D) Professional GPUs support up to four displays while consumer GPUs are limited to two displays

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The key distinction between professional and consumer GPUs is driver certification and ECC VRAM. Software vendors (Autodesk, Dassault, Siemens) test and certify specific GPU driver versions with their applications. Using an uncertified consumer driver can cause rendering artifacts, application crashes, and incorrect calculations. ECC VRAM adds error correction to the graphics memory, preventing silent data corruption in long-running simulations.
- *Why A is incorrect:* Professional GPUs typically have fewer CUDA cores and slower clock speeds than consumer GPUs at the same price. They are not faster in raw performance — they are more reliable for specific certified workloads.
- *Why C is incorrect:* Professional workstation GPUs use the same PCIe x16 connector as consumer GPUs. They are physically compatible with any PCIe x16 slot.
- *Why D is incorrect:* Many consumer GPUs support three or more displays. Multi-display support is not the distinguishing characteristic between professional and consumer GPUs.

---

### Question 13

A home lab enthusiast wants to run five virtual machines simultaneously, each allocated 16 GB RAM, 4 vCPUs, and 100 GB storage. What is the minimum physical RAM the host system must have?

- A) 16 GB — VMs share RAM dynamically and the host only needs one VM's worth at a time
- B) 80 GB — 5 VMs × 16 GB each, with no host OS overhead
- C) At least 96–100 GB — 5 VMs × 16 GB (80 GB) plus at least 16–20 GB for the host hypervisor OS
- D) 32 GB — modern hypervisors use memory deduplication to reduce total RAM consumption by 60%

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Physical RAM must cover all VM allocations plus the host OS and hypervisor overhead. Five VMs at 16 GB each = 80 GB minimum for the VMs. The hypervisor OS (VMware ESXi, Hyper-V, Proxmox) requires 8–16 GB or more for its own operation. A minimum of 96–100 GB is required, meaning a 128 GB configuration is the practical minimum standard choice.
- *Why A is incorrect:* RAM is allocated to running VMs and held exclusively while those VMs are powered on. VMs do not dynamically share RAM in a way that reduces the total physical requirement below the sum of all allocations.
- *Why B is incorrect:* 80 GB covers only the VM allocations. The host hypervisor OS itself requires RAM for its own processes, making 80 GB insufficient.
- *Why D is incorrect:* While memory deduplication (memory ballooning/transparent page sharing) exists in some hypervisors, it does not reliably reduce consumption by 60% and should not be used as the basis for hardware sizing decisions. The safe design practice is to provision physical RAM equal to the full sum of all VM allocations plus host overhead.

---

### Question 14

A user wants a home NAS for media storage and backup. They require at least 20 TB of usable storage and must survive one drive failure. They are using 4 TB NAS-rated hard drives. Which RAID level and minimum drive count meets both requirements?

- A) RAID 0 with 5 drives (20 TB usable, no fault tolerance)
- B) RAID 1 with 2 drives (2 TB usable after mirroring — insufficient)
- C) RAID 5 with 6 drives (20 TB usable, one drive fault tolerance)
- D) RAID 10 with 6 drives (12 TB usable, one drive fault tolerance)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* RAID 5 usable capacity = (N − 1) × drive size. With 6 drives at 4 TB each: (6 − 1) × 4 = 20 TB usable. RAID 5 tolerates exactly one drive failure. This configuration meets both the capacity requirement (20 TB) and the redundancy requirement (one drive failure tolerance).
- *Why A is incorrect:* RAID 0 has no fault tolerance. A single drive failure destroys all data. This explicitly fails the fault tolerance requirement.
- *Why B is incorrect:* RAID 1 with two 4 TB drives yields only 4 TB of usable storage — far below the 20 TB requirement.
- *Why D is incorrect:* RAID 10 with 6 drives: usable = 50% × (6 × 4 TB) = 12 TB. This falls short of the 20 TB usable storage requirement.

---

### Question 15

What is the primary hardware consideration that makes a CPU appropriate for a virtualization host compared to a CPU appropriate for a gaming PC?

- A) Gaming CPUs need higher clock speeds; virtualization CPUs need more physical cores to support many concurrent VMs
- B) Gaming CPUs need more physical cores; virtualization CPUs need higher clock speeds for single-threaded game engines
- C) Gaming and virtualization have identical CPU requirements; the GPU is the differentiating factor
- D) Virtualization CPUs must support AVX-512 instructions; gaming CPUs do not require instruction set extensions

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Games are primarily single-threaded or lightly multi-threaded; clock speed (GHz) is the dominant factor for gaming frame rates. Virtualization workloads run multiple complete OS instances simultaneously, each consuming dedicated vCPU allocations. More physical cores = more VMs that can run concurrently without oversubscription. A 16-core CPU at 3.0 GHz will outperform an 8-core CPU at 5.0 GHz for a virtualization host running 8+ VMs.
- *Why B is incorrect:* This reverses the correct relationship. Gaming benefits from clock speed; virtualization benefits from core count.
- *Why C is incorrect:* Gaming and virtualization have very different CPU and GPU requirements. The GPU does not compensate for an inappropriate CPU in either scenario.
- *Why D is incorrect:* AVX-512 supports certain scientific and machine learning workloads but is not a defining requirement for general virtualization. The core count/clock speed tradeoff is the fundamental distinction tested on the A+ exam.

---

### Question 16

A technician building a NAS recommends standard desktop RAM instead of ECC RAM to save money. The NAS will use ZFS for its file system. What is the specific risk of this decision?

- A) Desktop RAM runs at higher voltages than ECC RAM, causing the NAS motherboard to overheat
- B) ZFS relies on RAM integrity for write-back caching; non-ECC RAM bit flip errors can silently corrupt data written to disk
- C) ZFS is only compatible with ECC-registered DIMMs; desktop RAM is incompatible at the driver level
- D) Desktop RAM has a higher failure rate under 24/7 operation; it will fail within days in a NAS environment

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* ZFS uses RAM as a write-back cache (the ARC — Adaptive Replacement Cache). Data passes through RAM before being written to disk. If a non-ECC RAM bit randomly flips a bit in cached data (a known occurrence over time), that corrupted data is written to disk with no indication of error — because non-ECC RAM has no mechanism to detect or correct single-bit errors. ZFS's checksumming detects the on-disk corruption after the fact, but the data is already corrupted.
- *Why A is incorrect:* Desktop DDR4 and ECC DDR4 RAM operate at the same voltage (1.2V). Voltage is not the distinguishing characteristic between ECC and non-ECC.
- *Why C is incorrect:* ZFS is software and has no driver-level incompatibility with non-ECC RAM. It runs on both ECC and non-ECC RAM. The risk is data integrity, not driver compatibility.
- *Why D is incorrect:* Standard desktop RAM can operate continuously in a NAS environment for years without immediate failure. The risk is bit flip events — which are statistical and may not cause obvious failure — corrupting stored data, not rapid hardware failure.

---

### Question 17

Which of the following is the BEST choice of storage for the operating system and application drive in a 4K video editing workstation, separate from the video media scratch disk?

- A) A 7200 RPM 2 TB HDD for fast sequential access to application files
- B) A 512 GB NVMe SSD for fast boot time and application loading
- C) A USB 3.0 flash drive for easy OS portability between editing workstations
- D) A 5400 RPM external HDD for large application library storage

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The OS and application drive primarily handles random I/O — loading application files, writing OS page files, handling background processes. NVMe SSD excels at random I/O with microsecond latency. A 512 GB NVMe drive provides ample space for Windows/macOS, the NLE application (Premiere Pro, DaVinci Resolve), and project files, while the separate media scratch disk handles the large sequential video reads/writes.
- *Why A is incorrect:* HDDs have high seek time (~5 ms) that causes significant application loading lag. For an OS drive, random I/O performance matters most, and HDDs perform poorly here compared to SSDs.
- *Why C is incorrect:* USB 3.0 flash drives have much lower sustained sequential and random write speeds than internal NVMe SSDs, and their NAND wears out faster under OS read/write cycles. Running an OS from a USB flash drive is not a viable production workstation configuration.
- *Why D is incorrect:* A 5400 RPM external HDD has even slower sequential and random performance than a 7200 RPM internal HDD. Using it as an OS drive would produce an extremely slow and unresponsive workstation.

---

### Question 18

A gaming PC runs games well for the first 20 minutes, then frame rates drop dramatically and games become choppy even though temperatures appear acceptable. What is the MOST likely cause?

- A) The CPU is thermal throttling due to inadequate cooling
- B) The PSU is undersized and cannot sustain full GPU and CPU power draw simultaneously under extended load
- C) The GPU VRAM is fully utilized and the system is using system RAM as VRAM overflow, reducing effective GPU bandwidth
- D) The NVMe SSD is overheating and throttling storage I/O for game asset streaming

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* An undersized PSU may pass short-burst benchmarks and early gameplay but collapse under sustained full load when the GPU and CPU are simultaneously drawing peak wattage over an extended period. Voltage rails sag, causing the GPU to reduce power and performance. Temperatures may appear acceptable if hardware monitoring is reading GPU and CPU temp — the PSU is the component failing, not the monitored components.
- *Why A is incorrect:* The question states temperatures appear acceptable, which rules out thermal throttling as the cause. CPU thermal throttling would show elevated temperatures before performance drops.
- *Why C is incorrect:* VRAM overflow to system RAM causes a severe and immediate performance drop (often the game becomes completely unplayable or crashes) rather than a gradual frame rate reduction after 20 minutes of normal play.
- *Why D is incorrect:* NVMe SSD throttling reduces file loading speeds but does not cause frame rate drops in games that have already loaded assets into VRAM. Active gameplay frame rates are determined by GPU processing, not storage I/O.

---

### Question 19

A company is building a thin client deployment for 50 call center employees. Each employee's workstation will connect to a virtual desktop running on a central server. What are the PRIMARY hardware requirements for the thin client endpoint devices?

- A) High-end GPUs in each thin client to render the virtual desktops locally without server load
- B) Minimal CPU and RAM sufficient to run a network client and display output; all compute happens on the server
- C) Local NVMe SSDs in each thin client to cache the virtual desktop OS for offline use
- D) Full workstation-class CPUs in each thin client to ensure consistent desktop performance regardless of server load

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Thin clients are intentionally minimal endpoint devices. Their sole function is to display a remote desktop session received over the network. The server handles all computation. Thin clients typically run a lightweight OS (or firmware) with just enough CPU and RAM to manage the network connection and display protocol (RDP, VDI). This reduces per-seat cost dramatically compared to full workstations.
- *Why A is incorrect:* Thin clients do not render graphics locally. The server renders the desktop and streams a compressed video feed. A GPU in a thin client provides no benefit for remote desktop display — a basic integrated GPU is sufficient.
- *Why C is incorrect:* Thin clients do not run a local OS in the traditional sense; they have no local OS to cache. They boot into a firmware/ROM-based client. Local storage is not a meaningful component in a thin client design.
- *Why D is incorrect:* Workstation-class CPUs would replicate the cost and complexity of full workstations, eliminating the entire cost and management benefit of deploying thin clients.

---

### Question 20

A media company deploys a storage server (NAS) for a team of 10 video editors. The editors experience slow file transfers when multiple editors access the NAS simultaneously. Which hardware upgrade to the NAS would MOST directly resolve this bottleneck?

- A) Add more RAM to the NAS to increase the ZFS ARC cache size
- B) Upgrade the NAS NIC from 1 GbE to 10 GbE and ensure the network switch also supports 10 GbE
- C) Replace the existing RAID 5 with RAID 0 for double the read speed
- D) Add a discrete GPU to the NAS to accelerate file transfer encoding

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Ten simultaneous editors each transferring large 4K video files will quickly saturate a 1 GbE connection (which provides approximately 125 MB/s total shared bandwidth). Upgrading to 10 GbE (approximately 1,250 MB/s total shared bandwidth) provides 10× the network throughput, directly addressing the multi-user bottleneck. The switch must also support 10 GbE for the upgrade to take effect.
- *Why A is incorrect:* More RAM increases the ZFS ARC cache, which benefits repeated access to recently read files (cache hits). For 10 editors accessing different large video files, the working set likely exceeds any practical cache size. Network bandwidth is the direct bottleneck, not cache miss rate.
- *Why C is incorrect:* Replacing RAID 5 with RAID 0 eliminates fault tolerance and risks catastrophic data loss. The performance gain may be marginal compared to the network bottleneck. More importantly, sacrificing redundancy on a production media NAS is not an acceptable trade-off.
- *Why D is incorrect:* GPUs do not accelerate NAS file transfer operations. NAS file service is a CPU and network I/O task. A discrete GPU in a NAS provides no benefit for the described bottleneck.
