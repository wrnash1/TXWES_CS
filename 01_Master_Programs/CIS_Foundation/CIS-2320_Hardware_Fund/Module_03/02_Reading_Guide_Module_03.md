# Reading Guide: Module 03 - Processors (CPUs) and Cooling

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2320 &BULL; HARDWARE FUNDAMENTALS & PC ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5

---

### Introduction

Welcome to Module 03 — Processors (CPUs) and Cooling. The CPU is the primary computational engine of a PC. Every instruction executed by the operating system, every application calculation, every data operation passes through the processor. This module covers the physical socket standards that determine CPU-to-motherboard compatibility, the architectural concepts (cores, threads, cache, clock speed) that determine CPU performance, and the thermal management techniques required to keep a processor operating reliably within its rated temperature limits.

These topics are tested on the CompTIA A+ Core 1 (220-1101) exam under Domain 3.5. You must be able to identify LGA and PGA socket types visually and by description, explain the consequences of incorrect thermal paste application, diagnose thermal shutdown symptoms, and describe proper CPU installation procedure for each socket type. Study all sections of this guide before beginning the lab.

---

### 1. High-Yield Glossary

#### LGA (Land Grid Array)

LGA is a CPU socket type in which the contact pins are embedded in the motherboard socket, not on the processor. The CPU has flat gold contact pads (lands) on its underside that press against the socket pins when the retention lever is closed. Intel uses LGA for all current desktop processors (e.g., LGA1700 for 12th/13th generation Core, LGA1851 for Intel Core Ultra). AMD's current AM5 platform also uses LGA.

Key technician fact: the motherboard socket pins in an LGA socket are extremely fragile. A dropped or misaligned CPU can bend or break socket pins, rendering the motherboard non-functional. Inspect the socket carefully before installation and never apply lateral force to a CPU being placed in an LGA socket.

#### PGA (Pin Grid Array)

PGA is a CPU socket type in which the contact pins are on the CPU itself. The motherboard socket has a grid of receptacle holes. AMD used PGA for its AM4 platform (Ryzen 1000–5000 series). The AM4 socket is a Zero Insertion Force (ZIF) design: the CPU drops into the socket under its own weight with zero downward pressure; the lever applies all clamping force.

Key technician fact: if a PGA CPU is dropped or mishandled, the pins on the CPU bend — not the motherboard. A bent CPU pin may be carefully straightened with a fine needle under magnification, but success is not guaranteed and the CPU may still be damaged internally.

#### BGA (Ball Grid Array)

BGA is a packaging method in which the CPU is permanently soldered to the motherboard via tiny solder balls. There is no socket; no field replacement is possible. BGA is standard in laptops, tablets, smartphones, and embedded systems. If a BGA processor fails, the entire system board must be replaced. Reflow soldering equipment is required to rework a BGA component — this is not a technician-level repair.

For the A+ exam: if a scenario describes a laptop or mobile device CPU failing, the answer is almost always "replace the motherboard/system board," not "replace the CPU."

#### CPU Core

A CPU core is an independent processing unit within the CPU die, capable of fetching, decoding, and executing its own instruction stream. A single CPU package may contain 2, 4, 6, 8, 12, 16, or more cores. Each core operates largely independently, allowing true parallel execution of separate tasks (true parallelism). Core count is the most meaningful spec for workloads that can distribute work across multiple threads: video encoding, 3D rendering, virtualization, and server applications.

#### Thread / Hyper-Threading / SMT

A thread is a sequence of instructions that a CPU core is processing. With Intel Hyper-Threading (HT) or AMD Simultaneous Multi-Threading (SMT), each physical core presents two logical processors to the operating system by sharing certain execution resources. An 8-core CPU with HT/SMT appears to Windows as 16 logical processors. This improves throughput on parallelizable workloads by keeping more of the core's execution units busy, but logical threads do not equal physical cores in raw performance. A physical core running two threads cannot deliver exactly double the performance of that core running one thread.

#### Clock Speed (GHz)

Clock speed measures how many instruction cycles per second a CPU completes, expressed in GHz (gigahertz, billions of cycles per second). Base clock is the sustained speed under all-core load. Boost clock (Turbo Boost on Intel, Precision Boost on AMD) is the higher short-duration speed the CPU reaches when thermal and power headroom allows. Higher clock speed benefits single-threaded tasks (gaming frame rates, web browsing responsiveness, many business applications). The relationship between clock speed and performance is not linear across CPU generations — a newer architecture at a lower GHz often outperforms an older architecture at a higher GHz.

#### CPU Cache (L1 / L2 / L3)

CPU cache is fast SRAM built directly into the processor die that stores recently accessed data and instructions to reduce latency from main RAM access.

- L1 cache: smallest (32–64 KB per core), fastest, private to each core. Stores the most recently accessed instructions and data.
- L2 cache: medium size (256 KB to several MB per core), slightly slower, private to each core on most modern architectures.
- L3 cache: largest (8–64+ MB), shared across all cores, slower than L1/L2 but much faster than main RAM.

A larger L3 cache reduces how often the CPU must fetch data from RAM, which benefits latency-sensitive workloads like gaming and database operations.

#### Thermal Paste (TIM — Thermal Interface Material)

Thermal paste is a thermally conductive compound applied between the CPU's integrated heat spreader (IHS) and the base of the heat sink. Its purpose is to fill microscopic surface imperfections on both surfaces that would otherwise trap air — a very poor thermal conductor. Common thermal paste formulations are silicone-based with metallic or ceramic filler particles.

Correct application: a single pea-sized dot centered on the IHS. The pressure from mounting the heat sink spreads the paste into a thin, even layer. Do not apply a pre-spread layer; uneven spreading creates voids. Do not apply too much; excess paste can squeeze out and potentially short components on older CPU package designs.

When replacing a CPU cooler: clean all old thermal paste from both the IHS and the cooler base using isopropyl alcohol (90% or higher) before applying fresh paste.

#### Heat Sink and Fan Assembly (HSF)

A heat sink is a passive component — typically aluminum or copper fins — that absorbs heat from the CPU via conduction and dissipates it into surrounding air via convection. Most desktop CPU coolers pair a heat sink with an active fan, creating a heat sink and fan (HSF) assembly. The fan attaches to the CPU_FAN header on the motherboard.

Types of CPU coolers:

- Stock/box cooler: included with retail CPU packaging; adequate for stock operation; typically aluminum with a copper heat pipe or none
- Aftermarket air cooler: larger aluminum or copper tower with heat pipes; significantly better thermal headroom than stock; suitable for overclocking and high-TDP CPUs
- AIO (All-In-One) liquid cooler: cold plate on CPU, flexible tubes carry coolant to a radiator; radiator mounts at a case vent; quieter at high thermal loads; pump head connects to CPU_FAN header

#### CPU_FAN Header and Thermal Shutdown

The CPU_FAN header is a 4-pin PWM header on the motherboard dedicated to the CPU cooler fan. The four pins are: ground, +12V, tachometer (fan RPM signal to BIOS), and PWM control (BIOS adjusts fan speed). The BIOS monitors the tachometer signal continuously. If no RPM signal is detected — because the fan is unplugged, failed, or spinning too slowly — the BIOS triggers a thermal protection shutdown to prevent CPU damage from heat accumulation.

Important: even if an aftermarket fan controller is used, the CPU_FAN header should have a fan or speed sensor connected to prevent false thermal shutdowns.

#### Integrated Heat Spreader (IHS)

The IHS is the metal lid on the top surface of a desktop CPU package. It protects the fragile die underneath and provides a flat, uniform surface for heat sink contact. The thermal paste sits between the IHS and the heat sink base. Some enthusiasts perform "delidding" — removing the IHS to replace the lower-quality factory TIM between the die and IHS — but this is not a standard technician procedure and risks destroying the CPU.

---

### 2. CPU Socket Comparison Table

| Feature              | LGA                        | PGA                    | BGA                     |
|----------------------|----------------------------|------------------------|-------------------------|
| Pin location         | Motherboard socket         | CPU underside          | Soldered (no pins)      |
| Field-replaceable    | Yes                        | Yes                    | No                      |
| Insertion force      | None (drop in, lever locks) | None (ZIF lever)      | N/A — soldered          |
| Damage risk          | Bent motherboard pins      | Bent CPU pins          | N/A                     |
| Current Intel use    | Yes (LGA1700, LGA1851)     | No (legacy)            | Mobile/embedded         |
| Current AMD use      | Yes (AM5)                  | Legacy (AM4 and prior) | Mobile/embedded         |
| Repair if damaged    | Motherboard replacement    | CPU replacement        | Motherboard replacement |

---

### 3. Thermal Management Reference

Proper CPU cooler installation sequence:

1. Verify the CPU is seated and the retention lever is fully closed.
2. Clean the IHS surface with isopropyl alcohol if replacing an existing cooler.
3. Apply a pea-sized dot of thermal paste to the center of the IHS.
4. Lower the heat sink straight down onto the CPU without sliding it.
5. Secure all mounting clips or screws using a cross pattern (diagonal corners) to apply even pressure.
6. Connect the 4-pin PWM fan cable to the CPU_FAN header.
7. Boot the system and verify CPU temperature in BIOS; confirm fan speed is displayed.

Common thermal failure symptoms:

- System shuts down after 5–15 minutes of use, restarts fine after cooling: thermal shutdown from inadequate cooling
- BIOS warning "CPU Fan Error" at POST: fan not detected on CPU_FAN header
- CPU throttling (lower than expected performance): thermal throttling from sustained high temperature
- System runs hot but no shutdown: thermal paste dried out or dried poorly applied from initial installation

---

### 4. Certification Exam Tips

**Tip 1 — LGA vs. PGA pin location:** LGA pins are on the motherboard socket. PGA pins are on the CPU. The exam frequently reverses this in distractors. The mnemonic: LGA = Landscape (motherboard) has the pins; PGA = Processor has the pins.

**Tip 2 — BGA means no field repair:** Any scenario involving a laptop CPU failure almost always resolves to motherboard replacement, not CPU replacement, because laptop CPUs are typically BGA-soldered. Never select "replace the CPU" for a laptop CPU failure scenario unless the question specifies a socketed mobile processor.

**Tip 3 — Thermal paste quantity:** The correct answer is always a pea-sized dot in the center. If a question describes a technician spreading a thin layer across the entire IHS surface manually, that is also an acceptable real-world method, but "pea-sized dot in the center" is the standard A+ exam answer. Never choose "apply as much paste as possible."

**Tip 4 — CPU fan header monitoring:** The BIOS monitors the CPU_FAN header for a tachometer signal. A disconnected or failed CPU fan triggers a thermal shutdown or "CPU Fan Error" at POST — it does not just reduce cooling silently. Expect scenario questions about this behavior.

**Tip 5 — Threads are not cores:** A CPU with 4 cores and Hyper-Threading has 8 threads (8 logical processors visible to the OS). The exam may describe "8 processors" in Task Manager and ask how many physical cores the CPU has — the answer is 4.

**Tip 6 — ZIF socket = zero insertion force:** No downward pressure is required or appropriate when seating a PGA CPU. The socket lever is the only mechanism that applies clamping force. Pressing down on a PGA CPU before the lever is engaged bends pins.

**Tip 7 — Thermal shutdown symptom timing:** Thermal shutdown from a failed CPU fan typically occurs after several minutes of operation as the CPU reaches TJMax (its maximum safe operating temperature). A system that shuts down immediately at power-on is more likely a PSU or power connector issue, not thermal.

**Tip 8 — AIO pump connection:** On an AIO liquid cooler, the pump head cable connects to the CPU_FAN header so the BIOS can monitor pump operation. Radiator fans connect to SYS_FAN headers. This is a common assembly question.

---

### 5. Study Checklist

- [ ] Know the three socket types (LGA, PGA, BGA) and which has pins on the motherboard vs. the CPU vs. neither.
- [ ] Be able to name current Intel and AMD socket examples for each type.
- [ ] Explain the difference between physical cores and logical threads; know what Hyper-Threading and SMT mean.
- [ ] Describe the correct thermal paste application method and the consequences of applying too much.
- [ ] Know the CPU_FAN header's four pins and what happens when no fan signal is detected.
- [ ] List the thermal failure symptom patterns and match each to its likely cause.
- [ ] Read the Professor Messer study notes for the 220-1101 processor and cooling sections at [professormesser.com](https://www.professormesser.com/).
- [ ] Watch the Professor Messer free video on CPUs and cooling from the [220-1101 course](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/).
- [ ] Complete the Module 03 lab and submit by the Canvas deadline.
- [ ] Post your Module 03 discussion response by Wednesday at 11:59 PM.

---

### Additional Resources

- [Professor Messer CompTIA A+ Core 1 (220-1101) Free Course — Processors and Cooling](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- [CompTIA A+ Certification Official Page and Exam Objectives](https://www.comptia.org/certifications/a)

---

## 9. Supplemental Resources

1. **Professor Messer — CPU Installation and Cooling (220-1101 Free Video)**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video covering LGA/PGA socket installation, thermal paste application, heat sink types, and CPU_FAN header connections — all core topics for Module 03 lab and quiz preparation.

2. **Tom's Hardware — How to Install a CPU (Free Guide with Photos)**
   URL: [https://www.tomshardware.com/how-to/how-to-install-a-cpu](https://www.tomshardware.com/how-to/how-to-install-a-cpu)
   Relevance: Step-by-step photographic walkthrough of CPU installation for both Intel LGA and AMD PGA/LGA sockets. Supplements the lab procedure section with detailed visual references.

3. **Thermal Grizzly — Thermal Paste Comparison Guide (Free Reference)**
   URL: [https://www.thermal-grizzly.com/products/thermal-grizzly-kryonaut](https://www.thermal-grizzly.com/products/thermal-grizzly-kryonaut)
   Relevance: Overview of thermal paste formulations (silicone vs. metal-filled vs. phase-change). Useful background for understanding why thermal paste selection affects temperature outcomes in the lab challenge exercises.

4. **CPU-Z (Free System Information Tool)**
   URL: [https://www.cpuid.com/softwares/cpu-z.html](https://www.cpuid.com/softwares/cpu-z.html)
   Relevance: Free Windows utility that displays live CPU core count, thread count, base/boost clock, cache sizes, and socket type. Use this tool during the lab to verify your CPU specification table entries without opening the case.

5. **HWiNFO64 — Free Hardware Monitoring Tool**
   URL: [https://www.hwinfo.com/download/](https://www.hwinfo.com/download/)
   Relevance: Free real-time hardware monitoring tool that shows CPU temperature per core, fan RPM, and thermal throttling events. Essential for the challenge step where students observe thermal behavior and document throttling under load.
