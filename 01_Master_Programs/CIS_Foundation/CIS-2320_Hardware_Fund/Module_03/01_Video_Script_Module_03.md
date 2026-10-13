# Video Script: Module 03 - Processors (CPUs) and Cooling

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Estimated Duration:** 21–23 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5: Given a scenario, install and configure motherboards, CPUs, and add-on cards
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

Stage the following components before recording:

- One Intel LGA socket motherboard (LGA1700 or similar) — show the pin array in the socket
- One AMD PGA socket motherboard (AM4 or similar) — show the pins on the CPU underside
- One CPU (Intel or AMD) — show the triangle alignment marker on the corner
- A tube of thermal paste (standard grey compound)
- A stock Intel or AMD heatsink-fan (HSF) assembly
- An aftermarket tower cooler (e.g., Noctua or Cooler Master) if available
- A 4-pin PWM fan cable for the CPU_FAN header demonstration

Key exam traps to call out explicitly:

- LGA pins are on the motherboard socket (not the CPU); PGA pins are on the processor
- BGA means soldered — no field replacement possible; distinct from LGA and PGA
- Thermal paste: pea-sized dot only, do not spread manually
- CPU fan header: BIOS monitors it — missing fan signal triggers shutdown, not just a warning
- Hyper-Threading / SMT: threads are not the same as physical cores

Safety notes:

- Never touch the underside of an LGA CPU (the contact pads) or the pins in an LGA socket
- Always handle a CPU by its edges with an ESD strap or after grounding yourself
- Never apply downward force when seating a PGA CPU — zero insertion force (ZIF) socket requires no pressure to seat; only the lever applies clamping force

---

## Section 1: Introduction and Certification Alignment [00:00 - 03:00]

**[CAMERA: Instructor on camera, title card "Module 03 — Processors (CPUs) and Cooling"]**

"Welcome back, everyone. Professor Nash here. This is Module 03 of CIS-2320 Hardware Fundamentals at Texas Wesleyan University: Processors and Cooling.

This module maps directly to CompTIA A+ Core 1 Domain 3.5 and covers two topics that every technician encounters constantly: installing CPUs correctly, and keeping them cool. These are also areas where mistakes are expensive — a bent pin on an LGA socket can destroy a motherboard, and insufficient cooling will kill a CPU over time through heat degradation.

Today we will cover four areas. First, CPU socket types — LGA and PGA — and how they differ. Second, CPU architecture: cores, threads, and what those specs actually mean for system performance. Third, thermal management: thermal paste application, heat sink installation, and active versus passive cooling. And fourth, a walkthrough of what you will do in the lab this week.

Let's get started."

**[PAUSE — 3 seconds]**

---

## Section 2: CPU Socket Types — LGA vs. PGA vs. BGA [03:00 - 08:30]

**[CAMERA: Cut to component table]**

**[SHOW COMPONENT: Intel LGA socket on motherboard — overhead close-up of the socket showing the dense grid of pin contacts]**

"Let's start with the two primary socket types you will work with in the field and see on the exam: LGA and PGA.

LGA stands for Land Grid Array. In an LGA socket, the pins are on the motherboard socket itself — that dense field of tiny spring-loaded pins you see here. The CPU has flat gold contact pads on its underside — no pins. Intel uses LGA exclusively for desktop processors. LGA1700, the current Intel mainstream socket, has 1,700 of those socket pins.

The critical thing to know about LGA: those motherboard pins are extremely fragile. A single bent pin can prevent the CPU from making electrical contact and the system will not POST. If a customer drops a CPU into an LGA socket without proper alignment, you may be looking at a motherboard replacement. This is why LGA installation technique matters.

**[SHOW COMPONENT: AMD PGA CPU — flip it over to show the pins on the underside]**

PGA stands for Pin Grid Array. In a PGA socket, the pins are on the CPU itself. The motherboard socket has holes that receive those pins. AMD has used PGA for most of its consumer desktop history — the AM4 socket is PGA. AM5, AMD's current platform, moved to LGA — so newer AMD boards now share the LGA design philosophy with Intel.

The critical thing about PGA: if a CPU is dropped or mishandled, the pins on the CPU bend, not the motherboard. A bent CPU pin can sometimes be carefully straightened with a fine needle under magnification — but it is tedious, and the CPU may still be damaged. The key installation rule: zero insertion force. A PGA CPU drops into its socket with NO downward pressure. The lever provides all the clamping force.

**[SHOW COMPONENT: Side-by-side of LGA and PGA CPU underside if available, or slide showing the distinction]**

There is a third type you need to know for the exam: BGA — Ball Grid Array. BGA processors are soldered directly to the motherboard. There is no socket. You find BGA in laptops, tablets, and embedded systems. If a BGA CPU fails, the entire motherboard is replaced — there is no field-swappable CPU. The exam may present a scenario where a technician 'tries to remove the CPU' from a device — if the device uses BGA, this is not possible without reflow soldering equipment.

**[PAUSE — 3 seconds]**

Exam mnemonic: LGA — the **L**andscape has the pins (the motherboard). PGA — the **P**rocessor has the pins. BGA — the ball solder means it is **B**onded permanently."

---

## Section 3: CPU Architecture — Cores, Threads, Cache, and Clock Speed [08:30 - 13:30]

**[CAMERA: Slide showing a CPU die diagram with cores labeled]**

"Now let's talk about what is inside the CPU and how to read the specifications that matter for the exam and for real system selection.

**[SHOW COMPONENT: Hold up a CPU package]**

A core is an independent processing unit inside the CPU die capable of executing its own instruction stream. A modern consumer CPU might have 6, 8, 12, or more cores. Each core can independently fetch, decode, and execute instructions. More cores means more simultaneous tasks can be handled.

Threads are the operating system's view of execution resources. With Intel Hyper-Threading — or AMD's equivalent technology called SMT, Simultaneous Multi-Threading — each physical core presents two logical processors to the operating system. An 8-core CPU with Hyper-Threading appears to the OS as 16 logical processors. This improves throughput on workloads that can parallelize, like video encoding, virtualization, and compiling code. It does not double raw performance, but it keeps the execution pipeline fuller.

Here is the exam trap: threads are not cores. A system with 4 physical cores and Hyper-Threading has 8 threads — but it still only has 4 physical cores. Some A+ questions describe a system with 'eight processors' and expect you to recognize this likely means 4 cores / 8 threads on a single CPU, not eight separate physical CPUs.

**[CAMERA: Slide showing clock speed and cache diagram]**

Clock speed — measured in GHz — describes how many instruction cycles the CPU completes per second. A 3.5 GHz CPU completes 3.5 billion cycles per second per core. Higher clock speed generally means faster single-threaded performance. Many modern CPUs have a base clock speed and a boost clock speed — the processor automatically increases its clock when thermal conditions allow.

Cache is fast memory built directly into the CPU die, arranged in levels: L1 (smallest, fastest, one per core), L2 (medium, one per core or shared), and L3 (largest, shared across all cores). Cache stores recently used data and instructions so the CPU does not have to wait for slower main RAM. L3 cache size is a meaningful spec for tasks like gaming and data processing.

**[PAUSE — 3 seconds]**"

---

## Section 4: Thermal Management — Paste, Heat Sinks, and Fans [13:30 - 19:00]

**[CAMERA: Return to component table]**

**[SHOW COMPONENT: Tube of thermal paste]**

"Heat management is arguably the most practical skill in this module because it is something you will do on every CPU installation. Let's walk through it carefully.

Thermal paste — also called thermal compound or TIM, Thermal Interface Material — fills microscopic surface imperfections between the CPU's integrated heat spreader and the base of the heat sink. Even surfaces that look perfectly flat under the eye have microscopic valleys and peaks. Air caught in those gaps is a terrible conductor of heat. Thermal paste displaces the air with a thermally conductive material, dramatically improving heat transfer.

The correct application method for the A+ exam and for real-world use is the pea-sized dot method: place a single small dot — roughly the size of a pea — in the center of the CPU's integrated heat spreader. Do not spread it. When the heat sink is pressed down and secured, the pressure spreads the paste naturally across the contact surface in a thin, even layer. Too much paste can squeeze out the sides and potentially flow into the CPU socket or onto nearby components. Too little leaves dry spots with poor thermal contact.

**[SHOW COMPONENT: Heat sink and fan assembly]**

The heat sink is the passive cooling component — aluminum or copper fins that conduct heat away from the CPU's heat spreader and dissipate it into the surrounding air. On its own, a heat sink relies on natural convection. That is rarely sufficient for a modern CPU. Virtually all desktop CPU coolers pair the heat sink with an active fan, creating a heat sink and fan assembly, or HSF.

**[SHOW COMPONENT: Connect the 4-pin CPU fan cable to the CPU_FAN header]**

The fan connects to the CPU_FAN header on the motherboard — a 4-pin connector. The four pins carry: ground, 12V power, a tachometer signal (tells the BIOS how fast the fan is spinning), and a PWM signal (the board controls fan speed by varying this pulse-width modulation signal). This is why it matters: the BIOS monitors the tachometer signal on the CPU_FAN header. If no fan signal is detected — because the fan is unplugged or failed — the BIOS will trigger a thermal protection shutdown to prevent CPU damage. Do not leave the CPU_FAN header disconnected even if you intend to use a fan controller.

**[SHOW COMPONENT: Aftermarket tower cooler comparison if available]**

Beyond stock HSF coolers, technicians encounter two other cooling types worth knowing. Air coolers — tower-style coolers with heat pipes — offer significantly better thermal performance than stock HSF and are common in workstation builds. Liquid cooling, specifically AIO (All-In-One) liquid coolers, routes coolant from a cold plate on the CPU to a radiator mounted at a case vent. AIOs offer excellent thermal performance and are common in high-end gaming and content creation builds. The pump head on an AIO connects to the CPU_FAN header; the radiator fans connect to SYS_FAN headers.

**[PAUSE — 3 seconds]**"

---

## Section 5: Lab Walkthrough and Closing [19:00 - 22:30]

**[CAMERA: Instructor on camera]**

"Let me walk you through what the lab covers this week so you know what to expect.

In Part 1 you will examine a CPU and motherboard and complete an identification table: socket type, number of cores, physical pin count, and socket release mechanism. You are practicing the visual identification skill the exam tests with scenario-based questions.

In Part 2 you will perform — or observe and document — a CPU installation procedure for your assigned socket type, a thermal paste application, and a heat sink mounting and fan header connection. You will answer observation questions at each step.

In Part 3 you will work through three cooling-failure scenarios and identify the most likely cause and correction for each one, drawing on this lecture and the reading guide.

Your deliverable is the completed lab document submitted to Canvas with photos or annotations where indicated.

To close: remember the key points from this module. LGA pins are on the motherboard; PGA pins are on the CPU; BGA is soldered. Pea-sized dot of thermal paste in the center — do not spread. Connect the CPU_FAN header or the BIOS will shut the system down on detected fan failure. More cores and threads improve parallel workload performance, but clock speed drives single-threaded tasks.

I will see you in Module 04 for RAM. See you then."

---

## End Card [22:30 - 23:00]

**[CAMERA: Title card with course info]**

"This has been Module 03 of CIS-2320 Hardware Fundamentals at Texas Wesleyan University. Complete the reading guide, take the quiz, and post your discussion response by Wednesday at 11:59 PM."

---

## Additional Resources

- [Professor Messer CompTIA A+ Core 1 (220-1101) Free Course — Processors and Cooling](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- [CompTIA A+ Core 1 Official Exam Objectives](https://www.comptia.org/certifications/a)
