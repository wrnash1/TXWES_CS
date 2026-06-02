# Quiz: Module 03 - Processors (CPUs) and Cooling

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5
**Format:** 10 multiple-choice questions | 10 points each | 100 points total

---

### Question 1

Which CPU socket type features pins located on the motherboard socket rather than on the processor itself?

- A) PGA
- B) LGA
- C) BGA
- D) ZIF

Correct Answer: B — Land Grid Array (LGA) embeds the pins in the motherboard socket. The CPU has flat contact pads (lands) on its underside that press against those socket pins when the retention lever is closed.

Distractor Analysis:

- Why A is incorrect: PGA (Pin Grid Array) is the opposite — the pins are on the CPU underside, and the motherboard socket has receptacle holes.
- Why C is incorrect: BGA (Ball Grid Array) uses solder balls and has no traditional pins at all; the chip is permanently bonded to the board.
- Why D is incorrect: ZIF (Zero Insertion Force) is a socket mechanism description, not a pin-location type. ZIF refers to the lever design that requires no force to seat the CPU, used in PGA sockets.

---

### Question 2

In the context of PC hardware, which of the following most accurately describes a heat sink?

- A) A passive cooling component made of aluminum or copper fins that absorbs heat from the CPU and dissipates it into surrounding air, typically paired with an active fan connected to the CPU_FAN header.
- B) A thermally conductive paste applied between the CPU's IHS and the cooler base to fill microscopic surface imperfections and improve heat transfer.
- C) A temperature sensor embedded in the CPU die that monitors operating temperature and signals the BIOS to throttle clock speed when a threshold is exceeded.
- D) A liquid cooling block that circulates coolant over the CPU surface and transfers heat to a radiator mounted at a case exhaust vent.

Correct Answer: A — The heat sink is the physical finned component that conducts and dissipates heat. Pairing it with an active fan creates a heat sink and fan (HSF) assembly, which is the standard desktop CPU cooling solution.

Distractor Analysis:

- Why B is incorrect: This describes thermal paste (TIM), not the heat sink itself.
- Why C is incorrect: This describes the thermal sensor and throttling logic built into the CPU die — a software/hardware protection mechanism, not a physical cooling component.
- Why D is incorrect: This describes the cold plate of an AIO (All-In-One) liquid cooler, a different cooling technology from a traditional air heat sink.

---

### Question 3

A technician is installing a CPU cooler and applies a thick, manually-spread layer of thermal paste covering the entire IHS surface before mounting the heat sink. What is the most likely consequence of this technique?

- A) The CPU will overheat because spreading the paste reduces its thermal conductivity
- B) Excess paste may overflow onto the motherboard socket or nearby components, potentially causing shorts
- C) The system will refuse to POST because the BIOS detects incorrect thermal interface thickness
- D) Performance will improve because a thicker paste layer creates a more complete thermal interface

Correct Answer: B — Applying too much thermal paste risks overflow onto the CPU socket contacts, surrounding capacitors, or other surface-mount components when compressed by the heat sink, which can cause electrical shorts.

Distractor Analysis:

- Why A is incorrect: Spreading the paste does not reduce conductivity in isolation; the amount and the resulting thickness under the heat sink are the real issues. However, too much paste can trap air and actually insulate rather than conduct.
- Why C is incorrect: BIOS does not measure or detect thermal paste thickness. It monitors temperature sensors and fan RPM, not the physical interface layer.
- Why D is incorrect: More paste does not improve performance. An optimal thermal interface is as thin as possible while covering the full contact surface; excess paste acts as a thermal insulator by increasing the distance between metal surfaces.

---

### Question 4

A user reports that their desktop PC shuts down abruptly after running for about 10 minutes, and the system feels very hot near the CPU area. The PC powers back on after cooling for a few minutes. Which is the most likely cause?

- A) The PSU is failing and cannot sustain load under thermal stress
- B) The CPU fan has stopped working or is disconnected, causing the CPU to overheat and trigger thermal shutdown
- C) The RAM modules are incompatible with the motherboard and generating excessive heat
- D) The hard drive is overheating because it is mounted too close to the CPU cooler

Correct Answer: B — A failed or disconnected CPU fan is the most common cause of the thermal shutdown pattern: the CPU runs fine initially then reaches TJMax after several minutes of operation, triggering the BIOS thermal protection shutdown.

Distractor Analysis:

- Why A is incorrect: PSU failure typically causes immediate power loss, random crashes under load, or failure to power on — not a heat-then-shutdown pattern localized to the CPU area.
- Why C is incorrect: Incompatible RAM causes POST failure, memory error BSODs, or system instability at boot — not cyclical thermal shutdowns timed to heat buildup.
- Why D is incorrect: HDDs do not generate enough heat to trigger CPU thermal shutdown. The symptom pattern (hot CPU area, boots fine after cooling) points specifically to CPU thermal management failure.

---

### Question 5

Which of the following best describes the advantage of a CPU with 8 cores and Hyper-Threading (16 threads) compared to a CPU with 4 cores and no Hyper-Threading?

- A) The 8-core CPU runs at twice the clock speed, making single-threaded tasks faster
- B) The 8-core CPU can handle more parallel tasks simultaneously, improving performance in multi-threaded workloads
- C) The 8-core CPU uses less power because each core handles fewer instructions per cycle
- D) The 8-core CPU has a larger L3 cache, which eliminates the need for RAM in most operations

Correct Answer: B — More physical cores and logical threads allow the CPU to handle more simultaneous instruction streams, directly benefiting workloads that parallelize: video encoding, virtualization, scientific simulation, and server applications.

Distractor Analysis:

- Why A is incorrect: Core count and clock speed are independent specifications. Adding cores does not increase clock speed; some higher-core-count CPUs actually have lower base clock speeds due to power and thermal constraints.
- Why C is incorrect: More cores generally increase total power draw, not decrease it. More transistors switching simultaneously consume more energy.
- Why D is incorrect: Cache size is a separate specification unrelated to core count. Even large L3 caches require main RAM; cache cannot replace system memory.

---

### Question 6

A technician is building a system with an AMD AM4 processor. They attempt to seat the CPU by pressing it firmly into the socket with their thumb before lowering the retention lever. What error has the technician made?

- A) AM4 is an LGA socket and requires a load plate, not a lever
- B) The AM4 socket is a ZIF design; the CPU should drop in with zero force and only the lever applies clamping
- C) The CPU should be inserted at a 45-degree angle first, then lowered flat
- D) Pressing the CPU in before closing the lever is the correct procedure for PGA sockets

Correct Answer: B — AM4 uses a Zero Insertion Force (ZIF) PGA design. Pressing the CPU down before the lever is engaged can bend the CPU's pins. The CPU must be aligned with the triangle marker and then dropped in under its own weight; the lever applies all clamping force.

Distractor Analysis:

- Why A is incorrect: AM4 is a PGA socket, not LGA. Intel's LGA sockets use a load plate; AMD AM4 uses a lever-actuated ZIF mechanism.
- Why C is incorrect: Angled insertion is the method for laptop SODIMM RAM, not desktop CPUs. CPUs are inserted straight down.
- Why D is incorrect: Pressing the CPU down before closing the lever is incorrect and damaging for PGA sockets. There is never a situation in standard PGA installation where downward force is applied before the lever.

---

### Question 7

What is the correct method for applying thermal paste to a desktop CPU before mounting a heat sink?

- A) Apply a thin, manually spread layer across the entire IHS surface using a credit card
- B) Apply a pea-sized dot to the center of the IHS and allow the heat sink pressure to spread it
- C) Apply thermal paste to the base of the heat sink only, not to the CPU
- D) Apply a generous bead along each edge of the IHS to ensure full coverage from all sides

Correct Answer: B — A pea-sized dot centered on the IHS is the standard correct method. The mounting pressure from the heat sink spreads the paste evenly across the contact surface in a thin layer.

Distractor Analysis:

- Why A is incorrect: Manual spreading with a card or finger can introduce air bubbles and uneven coverage. While some advanced users do spread paste, it is not the exam-standard method and is not recommended for beginners.
- Why C is incorrect: Applying paste to the heat sink base only rather than the CPU is not standard practice; paste should be applied to the CPU IHS where it interfaces with the cooler.
- Why D is incorrect: Applying paste along the edges risks significant overflow when compressed. The center dot method is specifically designed to prevent overflow by letting pressure distribute paste naturally inward.

---

### Question 8

A technician builds a new PC and receives a "CPU Fan Error" message at POST, even though the CPU cooler fan appears to be spinning. What should the technician check first?

- A) Whether the correct CPU model is installed for the motherboard's chipset
- B) Whether the fan cable is connected to the CPU_FAN header rather than a SYS_FAN header
- C) Whether the thermal paste was applied correctly, as incorrect paste triggers fan error messages
- D) Whether the RAM is seated correctly, as POST errors often appear as fan errors in BIOS

Correct Answer: B — The BIOS monitors the tachometer signal specifically on the CPU_FAN header. If the fan cable is connected to a SYS_FAN header instead, the BIOS receives no signal from the designated CPU fan channel and generates the error even though the fan is spinning.

Distractor Analysis:

- Why A is incorrect: CPU model/chipset compatibility issues cause POST failure or CPU identification errors, not CPU fan error messages.
- Why C is incorrect: Thermal paste application does not trigger fan error messages. The BIOS has no mechanism to detect paste quality or application method.
- Why D is incorrect: Incorrectly seated RAM causes POST beep codes, memory error messages, or no-boot conditions — not CPU fan errors.

---

### Question 9

Which of the following statements correctly describes BGA packaging?

- A) BGA processors have a grid of pins on their underside that insert into matching holes in the motherboard socket
- B) BGA processors are permanently soldered to the motherboard and cannot be replaced in the field
- C) BGA is the standard socket type used in Intel desktop platforms since the introduction of LGA1156
- D) BGA allows tool-free CPU replacement by releasing a clamp mechanism on the board edge

Correct Answer: B — BGA (Ball Grid Array) uses solder balls to permanently bond the CPU to the board. No socket exists; field replacement requires reflow soldering equipment and is not a standard technician repair.

Distractor Analysis:

- Why A is incorrect: This describes PGA (Pin Grid Array), not BGA. BGA uses solder balls, not pins.
- Why C is incorrect: Intel desktop platforms use LGA sockets. BGA is used in mobile and embedded platforms, not desktop socketed CPUs.
- Why D is incorrect: There is no tool-free clamp mechanism for BGA; the solder bond is permanent and requires heat to reflow for any rework.

---

### Question 10

An AIO liquid cooler is being installed in a desktop PC. The pump head cable and the two radiator fan cables need to be connected to the motherboard. Which headers should each cable connect to?

- A) Pump head to SYS_FAN; both radiator fans to CPU_FAN
- B) Pump head to CPU_FAN; both radiator fans to SYS_FAN headers
- C) All three cables to CPU_FAN using a splitter cable
- D) Pump head and radiator fans all connect to the same PUMP_FAN header

Correct Answer: B — The pump head cable connects to the CPU_FAN header so the BIOS can monitor pump operation (the tachometer signal from the pump counts as the CPU fan signal). Radiator fans connect to available SYS_FAN headers for system-level fan control.

Distractor Analysis:

- Why A is incorrect: The pump head must connect to CPU_FAN so the BIOS detects a signal on that monitored header. Connecting it to SYS_FAN would trigger a CPU Fan Error at POST.
- Why C is incorrect: Using a splitter to put all three cables on CPU_FAN could provide a signal but overwhelms the header's power capacity and prevents independent fan speed control for the radiator fans.
- Why D is incorrect: Some high-end boards have a dedicated PUMP_FAN or W_PUMP header for this purpose, and connecting the pump there is valid on boards that have it — but the standard answer when only CPU_FAN and SYS_FAN are referenced is pump to CPU_FAN.
