# Reading Guide: Module 13 - Laptop Components and Disassembly
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 13 - Laptop Components and Disassembly**! This module covers the hardware components unique to laptop and portable computers — the keyboard assembly, battery, Wi-Fi card, LCD display panel, and DC power jack — and the safe disassembly procedures required to service them. Laptop repair requires a different approach than desktop work due to the tightly integrated, proprietary nature of portable hardware. These topics appear on the **CompTIA A+ Core 1 (220-1101)** exam under laptop hardware and troubleshooting domains.

As a technician, you must be able to safely power down and disassemble a laptop, identify serviceable components, and replace common failure parts without damaging fragile connectors or flex cables. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **laptop keyboard and battery**: Laptop keyboards attach to the chassis via retaining clips, screws, or a ZIF (Zero Insertion Force) flex cable connector seated in a locking socket on the motherboard. Before any internal laptop service, the battery must be removed first to eliminate all power from the system and prevent short circuits. Removable laptop batteries use a sliding latch mechanism; integrated batteries require opening the bottom panel and disconnecting a small JST-style connector from the motherboard. Always confirm the battery is disconnected before touching internal components.
*   **laptop Wi-Fi card**: Most laptop wireless cards are half-mini or full-mini PCIe (M.2 or legacy Mini-PCIe) cards seated in a dedicated slot on the motherboard. The card connects to two or three thin coaxial antenna cables routed through the laptop hinge and into the LCD bezel, where they connect to printed antenna traces. These antenna connectors are tiny snap-on MHF4 connectors that must be carefully pried off with a spudger — not pulled by the cable — to avoid breaking the connector or tearing the antenna trace. The card is retained by one screw and lifts out at an angle.
*   **LCD screen replacement**: A laptop display assembly consists of the LCD panel, backlight (CCFL in older models, LED in modern ones), digitizer (on touchscreen models), bezel, and hinges. Replacement requires removing the bezel screws hidden under rubber plugs, disconnecting the LVDS or eDP video cable from the panel, and on touchscreen models, the digitizer flex cable. The display assembly connects to the lid via hinges screwed to both the lid and the palm rest. Incorrect reassembly can crack the panel, pinch flex cables, or prevent the lid from closing properly.
*   **DC power jacks**: The DC power jack (barrel jack) is the port where the laptop charger connects. It is typically soldered to a small sub-board or directly to the motherboard. A failing power jack causes intermittent charging, no charging, or a laptop that only works on battery. Symptoms include needing to hold the charger at an angle for it to charge, or the laptop only recognizing the charger occasionally. Replacement requires motherboard or sub-board removal and soldering or connector swapping depending on the design.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 1.3):** The A+ exam presents laptop disassembly safety scenarios. The single most important rule tested: always disconnect or remove the battery before performing any internal service on a laptop. This is the first step in every laptop repair scenario question — regardless of which component is being replaced.
*   **Scenario Trap:** A common A+ question describes a laptop that charges intermittently and asks what component is most likely failing. The distractor options include the AC adapter and the battery. The correct answer is the DC power jack — a loose or broken power jack causes exactly this symptom, and AC adapter failure would result in consistent no-charging rather than intermittent behavior.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers laptop hardware components and disassembly procedures with visual examples of antenna cable routing, keyboard connectors, and display assembly construction. Navigate to the laptop hardware section: [Professor Messer's CompTIA A+ Core 1 Course — Laptop Hardware](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Pay close attention to the Wi-Fi card antenna connector and keyboard ZIF cable procedures.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the laptop hardware sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on laptop components, display assemblies, keyboard connectors, Wi-Fi cards, and power jack repair.
*   **Required Video:** Watch the video lecture on laptop components and disassembly from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering battery removal procedures, antenna cable handling, and display assembly replacement.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Remove a laptop battery safely**: Power off the laptop completely. For a removable battery, locate the latch on the underside and slide it to release. For an integrated battery, remove the bottom panel screws, lift the panel, and carefully disconnect the battery connector from the motherboard using a spudger. Confirm the system shows no indicator lights before proceeding to other internal components.
*   **Locate and detach the laptop Mini-PCIe Wi-Fi card and antenna cables**: After battery removal, locate the Wi-Fi card under its plastic cover or heat shield. Use a spudger to gently pry each antenna connector off the card connectors — note which color antenna cable goes to which connector (main and aux). Remove the retaining screw and lift the card out at the angle it was seated.
*   **Swap the laptop keyboard module**: Identify the keyboard retention method (screws accessible from the bottom panel, or retaining clips along the top edge). Release the retention mechanism. Lift the keyboard slightly to access the ZIF connector on the motherboard. Flip up the ZIF lock bar, slide the flex cable out, and set the keyboard aside. Insert the replacement keyboard flex cable, lock the ZIF bar down, and reseat the keyboard.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the laptop hardware sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on laptop components and disassembly in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the disassembly steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
