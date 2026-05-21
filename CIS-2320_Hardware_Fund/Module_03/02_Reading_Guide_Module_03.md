# Reading Guide: Module 03 - Processors (CPUs) and Cooling
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 03 - Processors (CPUs) and Cooling**! This week's study material focuses on the central processing unit — the primary computational component of a PC — and the thermal management systems required to keep it operating safely. You will learn the differences between Intel and AMD socket types, how CPU architecture concepts like cores and threads affect performance, and why proper thermal paste application and heat sink installation are critical skills for a hardware technician.

These topics appear directly on the **CompTIA A+ Core 1 (220-1101)** exam. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Intel vs AMD socket types**: CPU socket type determines which processors are physically and electrically compatible with a motherboard. Intel uses LGA (Land Grid Array) sockets where the pins are on the motherboard socket (e.g., LGA1700 for 12th/13th gen Intel). AMD uses PGA (Pin Grid Array) sockets where the pins are on the CPU itself (e.g., AM4, AM5). These socket types are not interchangeable — installing a CPU in the wrong socket is physically prevented by keying.
*   **CPU architecture (cores and threads)**: A CPU core is an independent processing unit capable of executing instructions; a modern desktop CPU may have 4–24 or more cores. A thread is a virtual execution path; with Hyper-Threading (Intel) or SMT (AMD), each physical core can handle two threads simultaneously, effectively doubling the number of logical processors visible to the OS. More cores and threads improve multitasking and parallel workload performance.
*   **thermal paste**: Thermal paste (also called thermal compound or TIM — Thermal Interface Material) is a thermally conductive substance applied between the CPU's integrated heat spreader (IHS) and the base of the heat sink. It fills microscopic surface imperfections that would otherwise trap air (a poor thermal conductor), ensuring efficient heat transfer from the CPU to the cooling solution. The correct application amount is typically a pea-sized dot centered on the CPU.
*   **heat sinks**: A heat sink is a passive cooling component made of aluminum or copper fins designed to absorb heat from the CPU and dissipate it into the surrounding air. Heat sinks are paired with a fan (creating an active HSF — heat sink and fan assembly) connected to the motherboard's CPU fan header. If the BIOS detects no fan signal on this header, it will trigger a thermal protection shutdown to prevent CPU damage.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 3.5):** The A+ exam frequently asks you to distinguish LGA from PGA sockets. Remember: LGA pins are on the **L**andscape (motherboard); PGA pins are on the **P**rocessor. Expect scenario questions about socket damage — bent pins on an LGA socket indicate motherboard damage, while bent pins on a PGA socket indicate CPU damage.
*   **Scenario Trap:** Watch out for questions about thermal paste quantity. The exam uses scenarios where a technician applies too much thermal paste, causing it to overflow onto the motherboard socket — this is a common distractor. The correct answer is always a small, pea-sized amount centered on the CPU; never spread it manually before seating the cooler.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers CPU sockets, architecture, and cooling with diagrams and photos. Navigate to the processor and cooling sections: [Professor Messer's CompTIA A+ Core 1 Course — Processors](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Pay special attention to the visual comparisons of LGA vs. PGA socket types.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the CPU and cooling sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on processor types, socket standards, and cooling methods.
*   **Required Video:** Watch the video lecture on CPUs and cooling from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on the segments covering LGA vs. PGA sockets, multi-core architecture, and heat sink installation.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Install a simulator CPU into LGA or PGA socket**: Handle a CPU carefully by its edges with an ESD strap on. For an LGA socket, lower the CPU straight down and secure the retention lever. For a PGA socket, align the triangle marker on the CPU with the triangle on the socket and lower it in without force.
*   **Apply thermal paste using the 'pea-size' method**: Place a small, pea-sized dot of thermal paste in the center of the CPU's IHS. Do not spread it — the pressure of the heat sink will distribute it evenly across the surface.
*   **Secure heat sink and connect 4-pin CPU fan header**: Lower the heat sink straight down onto the CPU, apply even pressure to secure all mounting clips or screws, then connect the 4-pin PWM fan cable to the CPU_FAN header on the motherboard. Verify the system recognizes the fan in BIOS.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the CPU and cooling sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on processors and cooling in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the installation steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
