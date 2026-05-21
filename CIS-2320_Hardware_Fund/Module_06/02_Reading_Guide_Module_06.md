# Reading Guide: Module 06 - Power Supplies and System Cooling
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 06 - Power Supplies and System Cooling**! This module covers the power supply unit (PSU) — the component that converts AC wall power to the DC voltages used by all PC hardware — and the airflow strategies that keep an entire system thermally healthy. You will learn how to calculate power requirements, understand efficiency ratings, and set up proper case airflow to prevent thermal throttling and component damage.

These topics are tested on the **CompTIA A+ Core 1 (220-1101)** exam. As a technician, you must be able to recommend appropriate PSU wattage, identify connector types, and diagnose airflow problems. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **PSU wattage**: PSU wattage is the total continuous DC power output a power supply can deliver to all connected components simultaneously. A technician calculates a system's total power draw by adding the TDP (Thermal Design Power) of the CPU, GPU, RAM, and storage devices, then adds a 20–30% headroom buffer to ensure the PSU never operates at maximum capacity. Undersized PSUs cause random shutdowns, instability, and premature PSU failure. Common desktop wattages range from 400W (basic office builds) to 1000W+ (high-end gaming or workstation systems).
*   **efficiency ratings (80 Plus)**: The 80 Plus certification program rates PSU efficiency — the percentage of AC input power successfully converted to usable DC output. An 80 Plus Bronze PSU is at least 82–85% efficient at typical loads; Gold is 87–90%; Platinum is 89–92%; Titanium reaches 94%+. Higher efficiency means less power is wasted as heat, resulting in lower electricity costs and cooler PSU operation. The 80 Plus label is printed on the PSU and listed in its specifications.
*   **modular vs non-modular**: A non-modular PSU has all cables permanently attached to the unit, which can cause clutter in cases with excess unused cables. A semi-modular PSU has the essential cables (24-pin ATX, CPU power) permanently attached while optional cables are detachable. A fully modular PSU has all cables detachable, allowing the technician to install only the cables needed, improving airflow and cable management. Modular PSUs typically cost more but are preferred in visible or airflow-sensitive builds.
*   **case airflow (intake vs exhaust)**: Proper case airflow directs cool air from outside the case across components and exhausts hot air out. Intake fans are positioned at the front and bottom of the case (drawing in cool air); exhaust fans are positioned at the rear and top (expelling hot air). A positive pressure configuration (more intake than exhaust) reduces dust accumulation. A negative pressure configuration (more exhaust than intake) can pull dust through unfiltered gaps. Balanced airflow with proper fan orientation is critical for sustained system performance.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 3.5):** The A+ exam tests PSU connector identification. Know that the 24-pin connector powers the motherboard, the 4/8-pin EPS connector powers the CPU, the 6/8-pin PCIe connector powers the GPU, the SATA power connector powers drives, and the 4-pin Molex connector powers legacy accessories. Expect scenario questions asking which cable to connect to a specific component.
*   **Scenario Trap:** A common A+ distractor is confusing PSU wattage with efficiency. A 500W 80 Plus Gold PSU and a 500W 80 Plus Bronze PSU both deliver 500W of DC output to the system — the efficiency rating only affects how much AC power is drawn from the wall, not the output to components. Do not select efficiency as the reason a PSU "can't power" a system.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers PSU types, connectors, and airflow with clear visual diagrams. Navigate to the power supply section: [Professor Messer's CompTIA A+ Core 1 Course — Power Supplies](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Study the connector identification segment carefully for the exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the PSU and cooling sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on power supply types, connectors, wattage, and case airflow.
*   **Required Video:** Watch the video lecture on power supplies and system cooling from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering PSU connectors, efficiency ratings, and fan orientation.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Calculate system power requirements based on CPU and GPU draw**: Look up the TDP specifications for a given CPU and GPU. Add storage, RAM, and motherboard power estimates, then apply a 25% headroom buffer to determine the minimum recommended PSU wattage.
*   **Connect 24-pin main motherboard connector**: Identify the 24-pin ATX connector from the PSU cable bundle. Align the locking tab with the notch on the motherboard's 24-pin header and press firmly until the clip snaps into place. Verify no pins are bent or misaligned.
*   **Examine fan orientations for optimal case airflow**: Identify the intake and exhaust fan positions in a case by examining fan label arrows (arrow indicates airflow direction). Verify front/bottom fans draw air in and rear/top fans exhaust air out to create front-to-back, bottom-to-top airflow.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the PSU and cooling sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on power supplies and system cooling in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the installation steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
