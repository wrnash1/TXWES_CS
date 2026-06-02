# Video Script: Module 08 - Custom PC Configurations

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University
**Estimated Duration:** 22-24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.4: Given a scenario, select and configure appropriate components for a custom PC
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

**Slides needed:**

- Slide 1: Title card — "Module 08: Custom PC Configurations"
- Slide 2: Four build types overview (CAD/Workstation, Virtualization Host, Gaming PC, NAS/Home Server)
- Slide 3: CAD workstation specs table — professional GPU vs. consumer GPU comparison
- Slide 4: Virtualization host requirements — core count and RAM allocation math
- Slide 5: Gaming PC build priorities — GPU tier chart by resolution
- Slide 6: NAS/Home Server — RAID level comparison table (RAID 1, 5, 6, 10)
- Slide 7: A+ exam scenario decision tree — matching workload to build type
- Slide 8: End card with study resources

**Components to show on camera (if available):**

- [SHOW COMPONENT] NVIDIA Quadro or AMD Radeon Pro GPU (or printed spec sheet)
- [SHOW COMPONENT] ECC vs. standard DDR4 RAM modules side by side
- [SHOW COMPONENT] Multiple HDDs representing a NAS drive array
- [SHOW COMPONENT] High-end consumer GPU (gaming) vs. professional GPU label comparison

**Key exam traps to address in the script:**

- Virtualization hosts do NOT need a powerful GPU unless GPU passthrough is explicitly stated
- Consumer gaming GPUs lack certified drivers for professional CAD software
- RAID 0 is NOT redundant — never recommend it for data that must be protected
- ECC RAM is required by ZFS-based NAS builds; regular RAM causes silent data corruption under ZFS
- Type of GPU (consumer vs. professional) is tested on the exam — not just performance tier

---

## [00:00 - 02:30] Introduction and Module Overview

[SHOW SLIDE: Title card — "Module 08: Custom PC Configurations"]

Hello, class. Welcome to Module 08. I am Professor Nash, and today we are covering one of my favorite topics in the entire A+ curriculum: Custom PC Configurations.

Here is what I mean by "custom." We are not buying a pre-built system off a shelf and calling it done. We are looking at a real-world scenario — a specific user with a specific workload — and we are selecting every major component to fit that workload as precisely as possible. The CompTIA A+ Core 1 exam, objective 3.4, will give you a scenario describing what a user does for work, and it will ask you which PC configuration is appropriate for that workload.

This module is entirely scenario-based. The exam will not ask you to define what a GPU is. It will say, "An architect is running Autodesk Revit on a machine with 16 GB of RAM and a consumer gaming GPU, and the software is crashing during model rendering. What should be upgraded?" You need to know not only the answer, but why the wrong answers are wrong.

[PAUSE — 3 seconds]

By the end of this video, you will be able to identify the correct build type for four major use-case categories, explain the primary hardware requirements for each category, and recognize the exam traps that cause students to choose the wrong answer. Let's get into it.

---

## [02:30 - 08:00] Section 1 — CAD Workstations and Professional Video Editing

[SHOW SLIDE: "CAD/Workstation Build — Component Priorities"]

[SHOW COMPONENT: Professional GPU or spec sheet]

Our first build type is the CAD workstation or professional content creation machine. This category covers architects, engineers, animators, and video editors. These users run software like Autodesk AutoCAD, SolidWorks, Adobe Premiere Pro, DaVinci Resolve, and similar applications.

Let's break down the four major components for a CAD workstation.

First: the GPU. This is the most critical distinction from a gaming PC. CAD workstations require a professional-grade GPU — the NVIDIA RTX A-series (formerly Quadro) or the AMD Radeon Pro line. Why not a gaming GPU? Two reasons. One: professional GPUs use certified, validated drivers tested specifically against CAD and 3D modeling software. When a geometry calculation is performed in SolidWorks or the rendering pipeline runs in Revit, the professional GPU driver is guaranteed to produce accurate results. Consumer gaming drivers optimize for frame rates and visual effects, not mathematical precision. A geometry error in a structural design file is not a cosmetic problem — it is potentially a safety problem. Two: professional GPUs support features like ECC VRAM, which detects and corrects memory bit errors in the GPU's own video memory.

[SHOW SLIDE: CAD workstation specs table]

Second: CPU. CAD and video rendering are highly multithreaded workloads. You want a high core count — minimum 8 cores for light use, 16 or more cores for heavy rendering. Clock speed matters too, but when rendering complex scenes, the renderer can distribute work across all available cores simultaneously. More cores equals faster renders.

Third: RAM. CAD workstations should have a minimum of 32 GB, with 64 GB or more for large assembly files or high-resolution video editing timelines. CAD assembly files can consume enormous amounts of RAM when multiple components are loaded simultaneously. Some enterprise workstations run 128 GB or more. ECC RAM — Error-Correcting Code RAM — is strongly preferred because it detects and corrects single-bit memory errors, preventing silent data corruption in long rendering sessions.

Fourth: Storage. Fast NVMe SSD is the standard. CAD file load times and scratch disk I/O are significantly impacted by storage speed. A slow SATA SSD or HDD will create noticeable bottlenecks when loading large model files or writing video preview cache.

[PAUSE — 2 seconds]

**A+ Exam Tip:** The exam will present a scenario where a user is running professional design software on a gaming GPU, and the question will be why they are experiencing issues. The answer is always the certified driver requirement, not the GPU's raw performance. Remember: professional GPU equals certified driver support.

---

## [08:00 - 13:00] Section 2 — Virtualization Hosts and Gaming PCs

[SHOW SLIDE: "Virtualization Host — Core Count and RAM Math"]

Our second build type is the virtualization host. This is a physical machine that runs a hypervisor — software like VMware ESXi, Microsoft Hyper-V, or VirtualBox — which divides the physical hardware into multiple isolated virtual machines, or VMs. Each VM runs its own operating system and applications independently.

The key hardware requirement for virtualization is simple: maximum CPU core count and maximum RAM capacity.

Here is the math. If you need to run 8 virtual machines simultaneously, and each VM is allocated 2 virtual CPUs and 8 GB of RAM, you need at minimum 16 logical CPU cores and 64 GB of RAM — just for the VMs — before you account for the host operating system's own overhead. The host OS and hypervisor itself will consume additional cores and RAM on top of that.

[SHOW SLIDE: Virtualization host requirements]

Storage for virtualization hosts should be fast — NVMe SSDs or RAID arrays reduce VM disk I/O latency when multiple VMs are reading and writing simultaneously. Each VM's disk is stored as a virtual disk file on the host's physical storage.

Now here is the critical exam trap for virtualization: GPU. Virtualization hosts do not need a powerful GPU. Unless the scenario specifically mentions GPU passthrough — a configuration where a physical GPU is dedicated to one specific VM for a graphics workload like video encoding or machine learning — the answer for a virtualization host never involves a high-end GPU. A basic integrated graphics or low-end discrete GPU is sufficient for the host to display its own management interface.

[PAUSE — 2 seconds]

**A+ Exam Tip:** If the exam offers a virtualization host scenario and one of the answer choices is a high-end gaming GPU, that answer is almost certainly wrong. The correct answer for virtualization is always maximum cores and maximum RAM.

[SHOW SLIDE: "Gaming PC — GPU Tier by Resolution"]

Our third build type is the gaming PC. This one is simpler in concept but has important nuances. The GPU is the primary performance component for gaming. The GPU renders the game world frame by frame and outputs those frames to the display. If the GPU cannot render frames fast enough, the game stutters.

The resolution and target frame rate of the monitor drive the GPU selection. At 1080p and 60 Hz, a mid-range GPU is sufficient for most games. At 1440p and 144 Hz, you need a significantly more powerful GPU to maintain 144 frames per second. At 4K, you need a high-end GPU.

For CPU in gaming builds, clock speed and single-threaded performance matter more than core count. Most game engines are not heavily multithreaded and rely more on a fast single processing thread than on distributing work across dozens of cores.

RAM for gaming: 16 GB DDR4 or DDR5 is the current standard minimum, with 32 GB preferred for modern titles. RAM speed has a secondary but noticeable effect on CPU-bound gaming scenarios.

Storage for gaming: NVMe SSD dramatically reduces game asset loading times compared to SATA SSD or HDD.

**A+ Exam Tip:** The exam asks specifically about the primary differentiator for gaming builds. The answer is GPU performance — not motherboard features, not monitor refresh rate, and not RAM speed. The GPU is what determines whether the frame rate target is achievable.

---

## [13:00 - 18:30] Section 3 — NAS and Home Servers

[SHOW SLIDE: "NAS/Home Server — RAID Comparison Table"]

[SHOW COMPONENT: Multiple HDDs representing NAS drives]

Our fourth build type is the NAS — Network-Attached Storage — or home/small office server. The priorities here are almost the opposite of a gaming PC or CAD workstation.

A NAS primarily needs: large storage capacity, drive redundancy, and low power consumption. It does not need a high-end GPU, a top-tier CPU, or fast single-threaded performance.

Let's talk about RAID. RAID stands for Redundant Array of Independent Disks. A NAS with multiple drives can configure those drives in a RAID array to provide fault tolerance — the ability to survive a drive failure without losing data.

For the A+ exam, you need to know the key RAID levels used in NAS builds.

RAID 0: Striping. Data is written across two or more drives simultaneously for maximum speed and capacity. Zero fault tolerance. One drive fails, all data is lost. Do not recommend RAID 0 for any NAS or backup system.

RAID 1: Mirroring. Every write is copied to two drives identically. One drive can fail and data is preserved. Usable capacity equals one drive's size regardless of how many drives are mirrored. Simple and reliable for two-drive NAS builds.

RAID 5: Striping with distributed parity. Minimum three drives. Parity information is distributed across all drives so any single drive failure can be recovered. Usable capacity equals total capacity minus one drive. A four-drive RAID 5 with 4 TB drives provides 12 TB of usable space. This is the most common NAS RAID level for balancing usable space and fault tolerance.

RAID 10: A combination of mirroring and striping. Requires at least four drives. Provides both fault tolerance and high performance. Usable capacity is 50% of total capacity. A four-drive RAID 10 with 4 TB drives provides 8 TB usable.

[PAUSE — 2 seconds]

For the CPU and RAM in a NAS build: a low-TDP CPU (low power consumption) is sufficient for file serving. If the NAS runs ZFS — a powerful file system used by many home NAS operating systems like TrueNAS — ECC RAM is strongly recommended. ZFS relies on RAM integrity for its write cache. Using non-ECC RAM with ZFS risks silent data corruption over time as bit errors accumulate.

**A+ Exam Tip:** When a scenario describes a NAS or home server, look for "drive redundancy" and "storage capacity" as the key requirements. RAID 5 maximizes usable space with single-drive fault tolerance. RAID 10 maximizes performance and fault tolerance at the cost of 50% capacity efficiency. RAID 0 is never the correct answer when redundancy is a requirement.

---

## [18:30 - 21:00] Section 4 — Build Type Decision Framework and Exam Strategy

[SHOW SLIDE: "A+ Exam Scenario Decision Tree"]

Let's put together a decision framework you can use on exam day. When you see a custom PC scenario on the A+ exam, ask yourself four questions.

Question one: What is the user's job or workload? An architect running CAD software, a data center admin running VMs, a gamer playing AAA titles, or a home user storing family photos and backups?

Question two: What is the primary hardware bottleneck for that workload? CAD and video: GPU type plus RAM. Virtualization: core count plus RAM. Gaming: GPU performance and frame rate capability. NAS: drive count, RAID level, and storage capacity.

Question three: What is the trap in this question? Is a gaming GPU being offered for a virtualization host? Is RAID 0 being offered for a storage redundancy scenario? Is a consumer GPU offered for a professional design workstation?

Question four: Does the answer address the primary differentiator? The correct answer will match the workload's primary requirement — not just a generally "good" component.

[PAUSE — 2 seconds]

Practice this framework with the five questions in the module quiz. Each question is modeled directly on A+ exam scenario format. Write down why each wrong answer is wrong — not just what the right answer is. Understanding the distractors is what separates students who score 750 on the A+ from students who score 900.

---

## [21:00 - 22:30] Closing and Lab Preview

[SHOW SLIDE: End card]

Here is your lab assignment for this module. You will receive five real-world workload scenarios, and for each one you will select the correct build type, identify the primary hardware requirement, and complete a bill-of-materials table with specific component recommendations and justifications.

There is no physical hardware assembly required this week. The lab is a written analysis and component-matching exercise, but it is graded on your reasoning and justification — not just your final answers. Make sure you explain why each component is appropriate for each workload.

The lab, quiz, and discussion are all due this week. Check Canvas for exact deadlines.

For additional study on this module's topics, Professor Messer's free CompTIA A+ Core 1 course at professormesser.com covers custom PC configurations with excellent use-case comparisons. I also recommend reviewing the official CompTIA A+ exam objectives document, which you can download free from comptia.org.

I will see you in the discussion forum. Good luck.

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 free course notes and video: professormesser.com (navigate to 220-1101 section, Custom PC Configurations)
- CompTIA A+ Exam Objectives (220-1101): comptia.org (free download, review Domain 3.4)
- CompTIA A+ Core 1 acronym list: comptia.org (review GPU, NAS, RAID, ECC, TDP entries)
