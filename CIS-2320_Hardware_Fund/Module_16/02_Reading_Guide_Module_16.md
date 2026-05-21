# Reading Guide: Module 16 - Final Exam Preparation
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 16 - Final Exam Preparation**! This is the capstone module of CIS-2320 Hardware Fundamentals. Rather than introducing new content, this module consolidates the high-yield concepts from all fifteen previous modules into a focused review aligned with the **CompTIA A+ Core 1 (220-1101)** exam domains. You will review the topics most frequently tested on the certification exam, work through scenario-based practice, and complete the final lab practical.

As a technician preparing for the A+ exam, your goal this week is to identify any gaps in your knowledge across the hardware, connectivity, troubleshooting, and printer domains, and reinforce those areas before the exam. Complete the checklist and review all glossary terms before the final assessment.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Core hardware identification and safety**: The A+ exam requires you to identify components by appearance and function: CPU socket types (LGA pins on motherboard vs PGA pins on CPU), DIMM vs SODIMM form factors, DDR3/4/5 pin count differences, PCIe slot sizes (x1/x4/x8/x16), and PSU connector types (24-pin ATX, 8-pin EPS, 6/8-pin PCIe, SATA power, Molex). ESD (electrostatic discharge) prevention — wrist strap, anti-static mat, anti-static bags — is tested as a safety prerequisite before any hardware work.
*   **Best practices for hardware installation and troubleshooting**: The A+ exam uses a structured troubleshooting methodology: (1) Identify the problem, (2) Establish a theory of probable cause, (3) Test the theory, (4) Establish a plan of action, (5) Implement the solution, (6) Verify full system functionality, (7) Document findings. Applied to hardware: always remove power first, use the correct tools, test one change at a time, and verify with a POST or boot test after each repair. Scenario questions expect you to follow this methodology.
*   **System configuration and connectivity review**: Key configuration facts for the exam: BIOS/UEFI boot order controls which device boots first; dual-channel RAM requires matching modules in paired slots (A1/B1, not A1/A2); T568B is the standard pinout for straight-through Ethernet patch cables; DisplayPort MST enables monitor daisy-chaining (HDMI cannot); Cat6a is required for 10 Gbps at 100 meters; USB Type-C connector shape does not guarantee USB 3.x or Thunderbolt speeds — the host port protocol determines actual speed. IMAP uses port 993 (SSL), POP3 uses port 995 (SSL), SMTP uses port 587 (STARTTLS) or 465 (SSL).

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — All Domains):** The exam is scenario-heavy. For every question, identify which component, standard, or procedure applies to the described situation before evaluating the answer choices. Common high-frequency topics: EP laser process six-step sequence; RAID level minimum drives and fault tolerance (RAID 0=none, RAID 1=1 drive, RAID 5=1 drive, RAID 10=1 per mirrored pair); CPU socket LGA vs PGA; PSU 80 Plus efficiency tiers; display connector daisy-chaining (DisplayPort only).
*   **Scenario Trap:** The most common A+ trap is selecting a plausible-sounding answer that applies to the wrong component or wrong layer. Examples: choosing a switch when the question requires a router (Layer 2 vs Layer 3); choosing a Cat6 cable for a 10 Gbps 80-meter run (Cat6a required); choosing HDMI for daisy-chaining (DisplayPort required); choosing efficiency rating as the reason a PSU "can't power" a system (wattage is the limiting factor, not efficiency rating).
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers all exam domains with practice questions and domain-by-domain review. Use the full playlist as a final review resource, focusing on any domains where you have identified weak areas: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Supplement with the written study notes for quick reference on port numbers, cable specs, and connector identification: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).

---

### Required Readings & Videos
To prepare for this module's final assessment, you must complete the following review activities:
*   **Required Review Reading:** Revisit all 15 module glossary sections and the high-yield exam tips. Cross-reference any uncertain topics with the corresponding sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Pay special attention to the laser EP process, RAID levels, cable categories, display connectors, and email port numbers — these are among the most frequently tested hardware topics.
*   **Required Video Review:** Watch the review and practice question segments in the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on any domains not yet reviewed, and use the practice question videos to simulate exam pacing and scenario reading technique.

---

### Lab & Command Integration
In this week's final lab practical, you will perform the following steps to demonstrate hands-on competency across course topics:
*   **Component identification and installation audit**: From a provided set of hardware, identify each component by name and type (CPU socket, RAM generation, PCIe slot size, storage interface). Install at least one component (RAM, M.2 SSD, or GPU) using proper ESD precautions and verify detection in BIOS/UEFI after installation.
*   **Cable and connector identification**: From a provided set of cables and connectors, correctly identify each by type: 24-pin ATX, 8-pin EPS, SATA power, 6-pin PCIe, RJ-45, RJ-11, LC fiber, SC fiber, DisplayPort, HDMI, USB Type-A, USB Type-C. Document which standard each cable belongs to and its primary use case.
*   **Troubleshooting scenario exercise**: Given a PC that exhibits a described symptom (technician's choice from boot failure, display issue, or network connectivity failure), apply the A+ seven-step troubleshooting methodology. Document each step taken, the theory tested, the corrective action, and the verification result.


---

### 3. Study Checklist
- [ ] Review all 15 module glossary sections and identify any knowledge gaps.
- [ ] Complete the final review of all domains using [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch remaining or review segments in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Complete the component identification, cable identification, and troubleshooting lab practical.
- [ ] Proceed to the final course assessment.
