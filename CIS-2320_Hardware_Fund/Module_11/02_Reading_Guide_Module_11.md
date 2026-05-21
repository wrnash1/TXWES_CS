# Reading Guide: Module 11 - Network Hardware & Connectors
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 11 - Network Hardware & Connectors**! This module covers the physical layer of networking — the cables, connectors, and wiring standards that carry data between devices. You will learn the differences between Ethernet cable categories, how to identify RJ-45 and RJ-11 connectors, the types of fiber optic connectors used in enterprise environments, and the T568A and T568B wiring standards used when terminating patch cables. These topics are tested on the **CompTIA A+ Core 1 (220-1101)** exam under networking hardware domains.

As a technician, you must be able to select the correct cable category for a given speed and distance requirement, crimp an RJ-45 connector using the correct pinout, and identify fiber optic connector types by appearance. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cat5e vs Cat6 vs Cat6a**: Cat5e (Category 5 Enhanced) supports 1 Gbps at up to 100 meters and is the minimum standard for modern Ethernet installations. Cat6 supports 1 Gbps at 100 meters and 10 Gbps at up to 55 meters; its improved insulation reduces crosstalk compared to Cat5e. Cat6a (Category 6 Augmented) supports 10 Gbps at the full 100-meter distance and is required when 10GbE is needed across an entire building run. All three categories use the same RJ-45 connector but differ in conductor gauge, twist rate, and internal shielding.
*   **RJ-45 vs RJ-11**: RJ-45 is an 8-position 8-contact (8P8C) modular connector used for Ethernet network connections; it is wider than RJ-11 and carries up to four twisted pairs. RJ-11 is a 6-position 2-contact (6P2C) connector used for telephone lines and DSL connections; it is narrower and physically smaller than RJ-45. An RJ-11 plug can physically fit into an RJ-45 port but will not establish a data connection — a common installation mistake when phone and network jacks are in close proximity.
*   **fiber optic connectors (ST, SC, LC)**: ST (Straight Tip) connectors use a bayonet-style twist-lock mechanism and are common in older enterprise installations; they are round with a protruding tip. SC (Subscriber Connector) connectors use a push-pull mechanism and have a square body; they are common in data center patch panels. LC (Lucent Connector) connectors are a smaller form factor that also use a push-pull latch and are the most common fiber connector in modern enterprise and data center environments due to their compact size enabling higher port density.
*   **T568A vs T568B pinouts**: T568A and T568B are the two wiring standards for terminating twisted-pair copper cables into RJ-45 connectors, defined by the TIA/EIA-568 standard. They differ only in the position of the orange and green wire pairs (pins 1/2 and 3/6 are swapped). T568B is the more commonly used standard in North America. A straight-through cable uses the same pinout (T568B–T568B) on both ends and connects a PC to a switch. A crossover cable uses T568A on one end and T568B on the other, connecting two like devices (PC to PC) — though modern switches with auto-MDI/MDIX make crossover cables largely unnecessary.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 2.1):** The A+ exam tests cable category selection for speed and distance requirements. The critical distinction to memorize: Cat6 supports 10 Gbps only up to 55 meters; Cat6a supports 10 Gbps up to the full 100-meter standard run. Any scenario requiring 10 Gbps at 100 meters requires Cat6a — Cat6 is a wrong answer in that specific scenario despite also being a valid 10 GbE cable.
*   **Scenario Trap:** Watch for questions that describe a technician making a cable to connect two PCs directly without a switch, then ask which pinout to use on each end. The answer is T568A on one end and T568B on the other (crossover cable). The exam will offer "T568B on both ends" (straight-through) as the distractor — straight-through is for PC-to-switch, not PC-to-PC.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers cable categories, connector types, and wiring pinouts with color-coded diagrams that are extremely useful for visual memorization. Navigate to the network cabling section: [Professor Messer's CompTIA A+ Core 1 Course — Network Cabling](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Study the T568A/B pinout diagrams and fiber connector comparison charts.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the network hardware and cabling sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on cable categories, RJ-45/RJ-11 connectors, fiber optic connectors, and T568A/B wiring standards.
*   **Required Video:** Watch the video lecture on network hardware and connectors from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering cable category speed comparisons, fiber connector identification, and straight-through versus crossover cable construction.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Examine copper pairs in an Ethernet cable**: Strip back the outer jacket of a Cat5e or Cat6 cable and separate the four twisted pairs. Identify the color coding for each pair (blue, orange, green, brown). Count the twists per inch on each pair and note how pair twist rate varies across the four pairs to reduce crosstalk.
*   **Trace fiber optic LC connectors**: Examine an LC fiber patch cable and identify the connector body shape, latch mechanism, and ferrule tip. Compare the LC connector physically to an SC connector and note the size difference. Identify which end of a duplex LC cable carries transmit (Tx) versus receive (Rx) signals by tracing the color convention.
*   **Create a straight-through patch cable using an RJ-45 crimper**: Cut a length of Cat5e or Cat6 cable. Strip 1 inch of outer jacket. Arrange the wire pairs in T568B order (white/orange, orange, white/green, blue, white/blue, green, white/brown, brown). Trim the wires to equal length, insert into an RJ-45 plug, and crimp firmly. Test the finished cable with a cable tester to confirm all eight pins are connected correctly.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the network hardware and cabling sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on network hardware and connectors in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the cabling steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
