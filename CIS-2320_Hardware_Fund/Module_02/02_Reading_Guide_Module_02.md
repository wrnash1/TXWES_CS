# Reading Guide: Module 02 - Motherboards and Form Factors
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 02 - Motherboards and Form Factors**! This week's study material focuses on the motherboard — the central circuit board that connects and coordinates every major component in a PC. You will learn how form factor determines physical size and mounting compatibility, how chipsets manage communication between the CPU and peripherals, and how expansion slots enable upgrades. These topics are directly tested on the **CompTIA A+ Core 1 (220-1101)** exam.

As a technician, you must be able to match a motherboard's form factor to a case, identify chipset functions, and recognize expansion slot types by physical appearance and bandwidth. Make sure to complete the checklist and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **ATX**: Advanced Technology eXtended (ATX) is the most common full-size desktop motherboard form factor, measuring 12 × 9.6 inches. ATX boards support multiple expansion slots, up to 8 RAM slots, and use a 24-pin main power connector. The ATX standard also defines the case mounting hole positions, PSU connector layout, and rear I/O panel cutout location.
*   **Micro-ATX**: Micro-ATX (mATX) is a smaller motherboard form factor measuring 9.6 × 9.6 inches. It is backward-compatible with standard ATX cases and uses the same 24-pin power connector, but typically has fewer expansion slots (usually 4 or fewer PCIe slots) and fewer RAM slots (typically 2–4). It is a common choice for budget and mid-range builds.
*   **Mini-ITX form factors**: Mini-ITX is a compact motherboard form factor measuring just 6.7 × 6.7 inches, designed for small form factor (SFF) systems such as HTPCs and embedded devices. It typically has only one PCIe x16 slot and two RAM slots, making it less expandable but ideal for space-constrained environments. Mini-ITX boards fit in many ATX and mATX cases.
*   **chipsets**: A chipset is a group of integrated circuits on the motherboard that manages data flow between the CPU, RAM, storage, and expansion slots. Modern chipsets (e.g., Intel Z790, AMD X670) are implemented as a single PCH (Platform Controller Hub) chip. The chipset determines which CPU generations are compatible, how many USB/SATA ports are supported, and whether overclocking is possible.
*   **expansion slots (PCIe)**: PCI Express (PCIe) is the standard interface for connecting expansion cards such as GPUs, NVMe SSDs, and network cards to the motherboard. PCIe slots come in different lane counts — x1, x4, x8, and x16 — with x16 being the widest and used for graphics cards. Higher lane counts provide more bandwidth; PCIe 4.0 x16 provides up to 32 GB/s in each direction.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 3.5):** The A+ exam tests form factor identification by scenario. You must know that ATX is the standard desktop form factor, Micro-ATX is smaller but backward-compatible with ATX cases, and Mini-ITX is the most compact. Expect questions asking which form factor fits in which case type.
*   **Scenario Trap:** A common A+ distractor involves PCIe slot compatibility. A shorter card (e.g., x1) will physically fit into a longer slot (e.g., x16), and the exam may ask whether this is allowed — it is, as PCIe is backward-compatible by design. Do not select "incompatible" answers based on slot length mismatch alone.
*   **Study Resource:** Professor Messer's free A+ video series covers motherboard form factors and expansion slots with diagrams. Visit the Core 1 course section on motherboards: [Professor Messer's CompTIA A+ Core 1 Course — Motherboards](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). These videos align directly with 220-1101 exam objectives and include visual comparisons of form factors.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the motherboard and form factor sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on motherboard form factors, chipsets, and expansion slots.
*   **Required Video:** Watch the video lecture on motherboards and form factors from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on the segments covering ATX vs. Micro-ATX vs. Mini-ITX and PCIe slot identification.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Compare ATX vs Mini-ITX dimensions**: Place an ATX and Mini-ITX motherboard side by side (or use reference images). Measure and record the dimensions of each, and identify how many expansion slots and RAM slots each board has.
*   **Identify PCIe x1, x4, and x16 slots on a board**: Examine a motherboard and locate each PCIe slot by physical length. Note which slot would be used for a GPU, an NVMe adapter card, and a Wi-Fi card.
*   **Locate BIOS/UEFI CMOS battery and jumper pins**: Find the CR2032 CMOS battery and the CMOS clear jumper on the motherboard. Document the jumper's location and describe when a technician would use it.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the motherboard and form factor sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on motherboards and form factors in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the component identification steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
