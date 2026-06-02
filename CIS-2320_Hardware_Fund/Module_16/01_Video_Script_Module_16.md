# Video Script: Module 16 - Final Exam Preparation

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

**Estimated Duration:** 22-24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — All Domains (Comprehensive Review)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

### Production Notes

> SHOW SLIDE: Title card — "Module 16: Final Exam Preparation | CIS-2320 Hardware Fundamentals"
> KEY EXAM TRAP 1: Students select "efficiency rating" as why a PSU cannot power a system. The correct answer is always wattage (total capacity), not efficiency. Efficiency rating (80 Plus tiers) describes how much wall power is wasted as heat, not how much the PSU can deliver.
> KEY EXAM TRAP 2: Students choose HDMI for daisy-chaining monitors. DisplayPort MST is the only mainstream display connector that supports daisy-chaining. HDMI cannot.
> KEY EXAM TRAP 3: Students place RAM in adjacent slots (A1/A2) instead of paired slots (A1/B1) for dual-channel. The motherboard color-coding and manual specify the correct paired slots.
> KEY EXAM TRAP 4: Students confuse Cat6 and Cat6a for 10 Gbps runs. Cat6 supports 10 Gbps only to 55 meters; Cat6a supports 10 Gbps to the full 100-meter standard. Any run over 55 meters at 10 Gbps requires Cat6a.
> PRODUCTION NOTE: Use a domain-map graphic on screen throughout this review session. Highlight each domain as it is discussed. The visual reminder of "which domain owns this topic" reinforces exam strategy alongside content recall.

---

### [00:00 - 03:30] Section 1: Introduction — How to Use This Review

SHOW SLIDE: "Module 16: Final Exam Preparation — A+ Core 1 Domain Map"

"Welcome to Module 16 — our final module of CIS-2320 Hardware Fundamentals. This is where we bring everything together. You have covered fifteen modules of CompTIA A+ Core 1 content, and now the goal is to make sure you can recall and apply all of it under exam pressure.

Here is how this review session works. I am going to walk through all five CompTIA A+ Core 1 exam domains and hit the highest-yield topics from each one. I am not going to re-teach everything from scratch — you have the reading guides, the quizzes, and Professor Messer's materials for deep review. What I am going to do is highlight the topics that show up most frequently on the exam, point out the traps that catch the most students, and show you how to read a scenario question strategically.

SHOW SLIDE: "A+ Core 1 (220-1101) Domain Weights"

The five domains and their exam weight distribution: Domain 1, Mobile Devices, is 15%. Domain 2, Networking, is 20%. Domain 3, Hardware, is 25% — this is the largest domain and covers everything from CPUs and RAM to printers and storage. Domain 4, Virtualization and Cloud Computing, is 11%. Domain 5, Hardware and Network Troubleshooting, is 29% — also very heavily weighted. Together, Domains 3 and 5 make up over half the exam. If you are short on time, those two domains deserve your most intensive review.

Your exam strategy: read every question twice before looking at the answers. Identify what the question is actually asking — component identification, process sequence, protocol/port, troubleshooting step? Then eliminate obviously wrong answers before evaluating the remaining choices. The A+ exam uses high-quality distractors — wrong answers that sound plausible. Your job is to identify why each wrong answer is wrong, not just why the right answer is right."

---

### [03:30 - 08:30] Section 2: Domain 1 and Domain 2 Review — Mobile Devices and Networking

SHOW SLIDE: "Domain 1 — Mobile Devices (15%)"

"Let me start with Domain 1 — Mobile Devices. The high-yield topics are: Bluetooth pairing and profiles, cellular data generations, email server port numbers, and USB connector types.

On Bluetooth: know the four SSP pairing models — Numeric Comparison, Passkey Entry, Just Works, and Out of Band. Know the four key profiles — A2DP for audio streaming, HFP for hands-free calls, HID for keyboards and mice, and SPP for serial data. Pairing failure troubleshooting: first check that the peripheral is in active pairing mode, then check whether it is already bonded to another device.

On cellular data: 3G delivered 1 to 10 Mbps. 4G LTE delivers 10 to 100 Mbps. 5G has three tiers — sub-6 GHz for coverage, mid-band for balance, mmWave for very high speeds at very short range. The hardware radio in the device determines which generation it can use — a plan upgrade cannot change the hardware.

On email ports — write these down one more time: IMAP is 143 plain, 993 SSL. POP3 is 110 plain, 995 SSL. SMTP is 25 relay, 587 STARTTLS, 465 SSL. And the key application: a user who can receive but not send has an SMTP problem. A user who cannot receive has an IMAP or POP3 problem.

On USB connectors: Type-A is the rectangular standard host connector. Type-B is the square printer connector. Micro-USB is the small asymmetrical Android connector. Type-C is the oval reversible modern connector. Lightning is Apple's proprietary flat connector. Critical exam trap: USB Type-C connector shape does not determine speed. The port's protocol specification determines speed.

SHOW SLIDE: "Domain 2 — Networking (20%)"

Domain 2 networking high-yield items for Core 1. Cable categories: Cat5e supports 1 Gbps to 100 meters. Cat6 supports 10 Gbps to 55 meters (falls back to 1 Gbps beyond that). Cat6a supports 10 Gbps to the full 100-meter standard. For any 10 Gbps run longer than 55 meters, you need Cat6a. This is a frequently tested cable specification question.

Network device layer roles: switches operate at Layer 2 (Data Link) and use MAC addresses to forward frames. Routers operate at Layer 3 (Network) and use IP addresses to route packets between networks. If a question describes two different subnets needing to communicate, a router is required. If a question describes devices on the same network needing to communicate, a switch is sufficient.

Fiber connectors: LC is the small-form-factor connector (locking tab, common in data centers). SC is the square push-pull connector. ST is the older bayonet-twist connector. Single-mode fiber uses a 9 micron core and carries light farther. Multi-mode fiber uses a 50 or 62.5 micron core for shorter runs.

Wi-Fi channels: 2.4 GHz has three non-overlapping channels — 1, 6, and 11. 5 GHz has many more non-overlapping channels and supports higher data rates. When configuring access points in the same space, use different non-overlapping channels to avoid interference."

---

### [08:30 - 14:00] Section 3: Domain 3 Review — Hardware (25%)

SHOW SLIDE: "Domain 3 — Hardware (25%) — The Largest Domain"

"Domain 3 is the largest domain at 25% of the exam and it covers the widest range of hardware topics. Let me hit the highest-yield items.

CPU socket types: Intel uses LGA sockets — the pins are on the motherboard socket, not the CPU. AMD uses PGA (AM4) and LGA (AM5) sockets — AM4 has pins on the CPU, AM5 moved to LGA with pins on the motherboard. Know which socket has pins where. Mixing a CPU with the wrong socket type will physically damage the pins.

RAM installation: DDR3 has 240 pins. DDR4 has 288 pins. DDR5 has 288 pins but a different key notch position than DDR4. DIMM (full-size) goes in desktops. SODIMM (small outline) goes in laptops. Dual-channel operation requires matching modules in the correct paired slots — typically A1/B1 or A2/B2 — not adjacent slots A1/A2. XMP in BIOS enables higher RAM speed profiles; it does not activate dual-channel.

SHOW SLIDE: "PCIe Slots and PSU Connectors"

PCIe slot sizes: x1 is the smallest, used for add-in cards like sound cards and USB controllers. x4 is mid-size, used for NVMe expansion cards and some capture cards. x8 is used for some GPUs and RAID controllers. x16 is the largest, used for graphics cards and high-throughput cards. PCIe is backward and forward compatible — a shorter card works in a longer slot, running at the shorter card's lane count.

PSU connectors: the 24-pin ATX connector powers the motherboard. The 8-pin EPS12V connector powers the CPU. The 6-pin or 8-pin PCIe power connector powers the GPU. SATA power connectors power drives. Molex connectors power older devices and some fans. A PSU's wattage rating is the maximum it can deliver — efficiency rating (80 Plus Bronze, Silver, Gold, Platinum) describes what percentage of wall power is converted versus wasted as heat. Efficiency is not a limit on output power.

SHOW SLIDE: "Storage Interfaces — SATA, NVMe, M.2"

Storage interface review. SATA III delivers 6 Gbps theoretical maximum, approximately 550 MB/s for SSDs. NVMe over PCIe 3.0 x4 delivers approximately 3,500 MB/s. NVMe over PCIe 4.0 x4 delivers approximately 7,000 MB/s. M.2 is a form factor — an M.2 slot can carry either SATA or NVMe, determined by the motherboard and the drive's keying (B+M key = SATA or NVMe; M key = NVMe only). RAID levels: RAID 0 is striping — no fault tolerance, full capacity. RAID 1 is mirroring — one drive failure tolerated, 50% usable capacity. RAID 5 requires three minimum drives, one drive failure tolerated. RAID 10 requires four minimum drives, one drive per mirror pair failure tolerated.

Display connectors: VGA carries analog video only. DVI carries digital and/or analog. HDMI carries digital video and audio. DisplayPort carries digital video, audio, and data. DisplayPort MST (Multi-Stream Transport) allows daisy-chaining monitors through a single DisplayPort connection. HDMI cannot daisy-chain. This is tested on the exam — if the scenario requires monitor daisy-chaining, DisplayPort is the answer.

The laser EP process: Cleaning → Charging → Exposing → Developing → Transferring → Fusing. Smearing toner equals fuser failure. Faint output equals transfer failure. Gray background equals charge roller contamination. Repeating dots at regular intervals equal a contaminated drum at that circumference. These mappings are tested directly."

---

### [14:00 - 18:30] Section 4: Domain 4 and Domain 5 Review — Cloud and Troubleshooting

SHOW SLIDE: "Domain 4 — Virtualization and Cloud Computing (11%)"

"Domain 4 is the smallest domain at 11% but it contains tested concepts. The key terms are: hypervisor Type 1 (bare-metal) runs directly on hardware without a host OS — examples are VMware ESXi and Microsoft Hyper-V in server mode. Hypervisor Type 2 (hosted) runs on top of a standard operating system — examples are VMware Workstation and VirtualBox. Virtual machines share the host hardware resources and are isolated from one another.

Cloud service models: IaaS (Infrastructure as a Service) provides virtualized compute, storage, and network resources — the customer manages the OS and above. PaaS (Platform as a Service) provides a runtime environment for applications — the customer manages their application code. SaaS (Software as a Service) provides fully managed software — the customer only uses the application.

Cloud deployment models: Public cloud — resources shared among multiple customers. Private cloud — dedicated resources for one organization. Hybrid cloud — combination of public and private. Community cloud — shared among organizations with common requirements.

SHOW SLIDE: "Domain 5 — Hardware and Network Troubleshooting (29%)"

Domain 5 is the second-largest domain and covers the A+ seven-step troubleshooting methodology plus specific hardware and network diagnostic skills.

The seven steps in order: one — identify the problem (gather information, replicate if possible). Two — establish a theory of probable cause (consider multiple possibilities, start with most obvious/common). Three — test the theory to determine cause. Four — establish a plan of action. Five — implement the solution or escalate if beyond scope. Six — verify full system functionality and implement preventive measures. Seven — document findings, actions, and outcomes.

This methodology applies to every troubleshooting scenario on the exam. When a question asks what a technician should do first, the answer is almost always to gather more information and identify the problem — not to immediately replace hardware or reinstall software.

Hardware troubleshooting fundamentals: POST (Power-On Self-Test) runs at boot and tests essential hardware. POST failure produces error codes or beep codes specific to the BIOS manufacturer. No video output with system POST passing suggests a GPU or display issue. No POST at all suggests a power delivery, CPU, or RAM problem. Always test one component change at a time and verify after each change.

Network troubleshooting: ping tests basic IP connectivity. ipconfig (Windows) or ifconfig (Linux/macOS) shows IP configuration. traceroute (tracert on Windows) maps the path between source and destination, showing where connectivity fails. nslookup tests DNS name resolution. The OSI model provides a layered troubleshooting framework — start at Layer 1 (physical) with cable and link light, then Layer 2 (switch port assignment), then Layer 3 (IP addressing and routing)."

---

### [18:30 - 22:30] Section 5: Exam Strategy and Final Preparation

SHOW SLIDE: "A+ Core 1 Exam Format"

"Let me give you the practical information about the exam itself. The CompTIA A+ Core 1 (220-1101) exam contains a maximum of 90 questions. You have 90 minutes. The passing score is 675 on a scale of 100 to 900. Question types include multiple choice (single answer), multiple select (where you must choose two or three correct answers), drag-and-drop, and performance-based questions that simulate a real task.

For multiple-choice questions: read the full question before looking at answers. Identify exactly what is being asked — component, process, protocol, troubleshooting step. Eliminate answers that use components from the wrong technology (like assigning a drum unit to an inkjet printer). When two answers seem both correct, the correct answer is the one that is more specific to the scenario and most directly addresses the described symptom or requirement.

For multiple-select questions: the question will tell you how many answers to select. If it says select two, select exactly two. If you are unsure of one, first identify the answer you are most confident in, then use elimination for the second.

For performance-based questions: these appear at the beginning of the exam. Do not skip them unless you are completely blocked — they are worth more than standard multiple-choice questions. If you cannot complete one, make your best attempt and move on. You can return to it if time permits.

SHOW SLIDE: "Final Week Study Plan"

For your final week of study, I recommend this approach. Day one through two: work through all fifteen module quizzes and the module 16 comprehensive quiz. Mark every question you missed. Day three: review every missed question — do not just note the correct answer, read the full distractor analysis and understand why each wrong answer is wrong. Day four: spend focused time on your weakest domain based on quiz results. Day five: do a timed practice run — set a 90-minute timer and work through a practice question set without stopping. Day six: light review only, no new material. Day seven: rest. A rested mind performs significantly better on a timed certification exam than an exhausted one.

SHOW SLIDE: "Register for Your Exam"

Before you close out this module, take one action right now — go to comptia.org and verify your exam registration information. If you have not registered yet, do it today. The exam is available at Pearson VUE testing centers and through online proctoring. Your A+ certification does not expire; once you earn it, it is valid for three years and renewable through continuing education.

SHOW SLIDE: End Card — "Texas Wesleyan University | CIS-2320 | Professor Nash"

Thank you for being part of CIS-2320 Hardware Fundamentals. This has been a rigorous course covering the full CompTIA A+ Core 1 domain, and you have earned your preparation. Go pass that exam. I will see you in the discussion forum for Module 16, and I hope to hear from you when you get your passing score. Good luck — you are ready."

---

### Additional Resources

For final exam preparation, visit:

- Professor Messer's free CompTIA A+ Core 1 study materials and practice exams at professormesser.com — use the complete 220-1101 course for any domain that needs reinforcement, and work through the practice question sets to simulate exam pacing.
- The official CompTIA A+ certification page at comptia.org — review the official exam objectives document to confirm coverage, check testing center locations, and verify registration details for the 220-1101 exam.
