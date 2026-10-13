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

---

### Question 11

A technician replaces a CPU in a desktop. After installation, the system boots but CPU temperatures immediately climb to 95°C at idle within 30 seconds. What is the MOST likely cause?

- A) The CPU is overclocked in BIOS beyond its rated speed
- B) Thermal paste was not applied between the IHS and the heat sink base
- C) The CPU fan is connected to a SYS_FAN header instead of CPU_FAN
- D) The CPU model is incompatible with the motherboard chipset

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Without thermal paste, the metal-to-metal contact between the CPU IHS and the heat sink base has microscopic air gaps (air being a very poor thermal conductor). Heat builds up immediately because it cannot be efficiently transferred to the heat sink. Temperatures climbing to 95°C at idle within seconds is a clear sign the thermal interface is missing or severely inadequate.
- *Why A is incorrect:* Overclocking would increase temperatures under load, not at idle within 30 seconds of boot. An overclock also requires BIOS configuration that would be visible in the system setup.
- *Why C is incorrect:* Connecting the CPU fan to SYS_FAN may trigger a "CPU Fan Error" POST message, but the fan still spins and provides airflow to the heat sink. Temperatures would rise more slowly than without thermal paste. The rapid idle temperature spike points to a thermal interface failure.
- *Why D is incorrect:* CPU incompatibility causes POST failures or the system refusing to boot — not a thermal runaway on a system that has booted successfully into the OS.

---

### Question 12

Which CPU specification is MOST relevant when choosing a processor for a heavily multi-threaded workload such as video rendering or virtual machine hosting?

- A) Boost clock speed (GHz)
- B) Physical core count
- C) L1 cache size per core
- D) Integrated graphics model

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Multi-threaded workloads distribute computation across independent threads that can execute simultaneously on separate cores. More physical cores means more true parallelism — each core executes its own thread independently. Video rendering and VM hosting both scale well with physical core count because they spawn dozens of independent work units.
- *Why A is incorrect:* Boost clock speed benefits single-threaded performance — tasks where only one instruction stream runs at a time (gaming, many business apps). For heavily multi-threaded work, core count matters more than peak single-core frequency.
- *Why C is incorrect:* L1 cache size affects how quickly each core can access its most recently used data. While important for latency-sensitive tasks, a larger L1 cache does not compensate for fewer cores in parallel workloads.
- *Why D is incorrect:* Integrated graphics are entirely irrelevant to multi-threaded compute performance. VMs and rendering workloads run on CPU cores, not the integrated GPU.

---

### Question 13

What is the purpose of the IHS (Integrated Heat Spreader) on a desktop CPU?

- A) It contains the CPU's voltage regulation circuitry to protect the die from power fluctuations
- B) It is a metal lid that protects the fragile CPU die and provides a flat, uniform surface for heat sink contact
- C) It houses the CPU's L3 cache in a thermally isolated chamber to prevent cache data corruption from heat
- D) It is a replaceable copper plate that the technician selects based on the heat sink brand being installed

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The IHS is a flat metal cap (usually copper or nickel-plated copper) factory-bonded over the CPU die. It protects the small, fragile silicon die from direct mechanical contact with the heat sink, and its flat surface ensures consistent contact with the cooler base. Thermal paste fills the microscopic gap between the IHS and the cooler.
- *Why A is incorrect:* Voltage regulation for the CPU is performed by the motherboard's VRM (Voltage Regulator Module) circuitry — not the IHS. The IHS has no electrical function.
- *Why C is incorrect:* L3 cache is embedded in the CPU silicon die. The IHS sits above the die and has no internal structure to house cache memory.
- *Why D is incorrect:* The IHS is factory-installed and not field-replaceable in normal technician practice. It is not selected based on cooler brand — it is a permanent part of the CPU package.

---

### Question 14

A user upgrades from a 4-core/8-thread processor to an 8-core/16-thread processor at the same clock speed. In which scenario would the user see the GREATEST performance improvement?

- A) Opening a web browser and loading a single website
- B) Playing a single-player video game with minimal background tasks
- C) Encoding a 4K video file using a multi-threaded encoder
- D) Typing in a word processor while music plays in the background

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Video encoding is an embarrassingly parallel workload — the encoder splits the video into segments and processes them simultaneously across available threads. Doubling from 8 to 16 threads provides near-linear speedup in encoding time, making this the scenario where the upgrade yields the most measurable benefit.
- *Why A is incorrect:* Opening a web browser and loading a page is primarily single-threaded with brief bursts of activity. The difference between 8 and 16 threads is barely perceptible for this task.
- *Why B is incorrect:* Most games, especially single-player titles, are primarily single-threaded or lightly multi-threaded (4–8 threads used). Clock speed matters more than thread count for gaming frame rates. Doubling thread count at the same GHz yields minimal gaming improvement.
- *Why D is incorrect:* Typing in a word processor uses a single thread. Background music playback uses one or two threads. Total active threads are well within the capacity of even a 4-core CPU; 16 threads provide no measurable benefit here.

---

### Question 15

When replacing a CPU cooler, a technician cleans the old thermal paste off the CPU IHS using a paper towel dampened with water. What is wrong with this method?

- A) Water is too cold and may thermally shock the CPU die
- B) Paper towels leave lint fibers that contaminate the thermal interface
- C) Water is not an effective solvent for the silicone-based compounds in most thermal pastes
- D) Water may cause the IHS to delaminate from the CPU package if applied repeatedly

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Most thermal pastes use silicone oil or silicone grease as a carrier with metallic or ceramic filler particles. These compounds are hydrophobic and water-resistant — water does not dissolve or lift them effectively. The correct cleaning agent is isopropyl alcohol at 90% concentration or higher, which is an effective solvent for silicone-based thermal compounds.
- *Why B is incorrect:* Paper towels can leave lint, which is a real concern, but it is a secondary issue compared to using an ineffective solvent. Lint contamination of the thermal interface is best avoided by using lint-free cloths or coffee filters — but the primary problem stated here is using water.
- *Why A is incorrect:* Room-temperature water is not cold enough to thermally shock a CPU. Thermal shock from cleaning is not a recognized failure mode.
- *Why D is incorrect:* The IHS is permanently bonded to the CPU package with solder or epoxy. Occasional cleaning with water would not delaminate it. This answer describes a non-existent failure mode.

---

### Question 16

A technician notices that the CPU in a desktop PC runs at 2.4 GHz under heavy load, even though the processor's rated base clock is 3.6 GHz and its boost clock is 4.8 GHz. What is the MOST likely explanation?

- A) The CPU is underclocked in BIOS and needs to be reset to default frequency
- B) The CPU is thermal throttling because it is exceeding its maximum safe operating temperature
- C) The system is in power-saving mode, which caps all cores at a reduced frequency
- D) The memory is running at DDR4-2400 speed, bottlenecking the CPU's instruction throughput

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Thermal throttling is an automatic CPU self-protection mechanism. When the CPU temperature reaches TJMax (typically 90–100°C depending on the model), it drops its clock multiplier to reduce heat output. Running below the rated base clock under load is a strong indicator of thermal throttling from inadequate cooling, dried-out thermal paste, or a clogged/failed heat sink.
- *Why A is incorrect:* BIOS underclocking would cause the CPU to run at the underclocked frequency consistently — at idle, light load, and heavy load. Throttling behavior (reducing speed under load when temperatures rise) is specifically a thermal response, not a static BIOS frequency setting.
- *Why C is incorrect:* Power-saving modes (like Windows Balanced power plan) reduce clock speed at idle but allow the CPU to boost under heavy load. A power plan would not result in the CPU running below base clock under full load.
- *Why D is incorrect:* Memory bandwidth affects CPU performance in memory-bound workloads, but it does not directly cause the CPU to reduce its clock frequency. Clock throttling is purely a thermal or power management response.

---

### Question 17

Which of the following best describes the relationship between a CPU's TDP rating and the minimum cooler required for that processor?

- A) TDP is a maximum power draw rating; the cooler must be rated to dissipate at least that many watts
- B) TDP is an average power draw figure; it has no bearing on cooler selection
- C) TDP represents the heat generated only by the CPU die, not including RAM or VRMs
- D) TDP stands for Total Drive Performance; it measures storage I/O capacity, not heat

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* TDP (Thermal Design Power) is expressed in watts and represents the maximum sustained heat output the cooling solution must handle to keep the processor within its rated temperature range. A CPU with a 125W TDP requires a cooler rated at 125W or higher. Using an inadequate cooler (e.g., a 65W-rated stock cooler on a 125W TDP processor) results in thermal throttling or thermal shutdown.
- *Why B is incorrect:* TDP is not an average — it is a design parameter that defines the cooling requirement. Cooler selection is directly based on TDP.
- *Why C is incorrect:* TDP represents the total heat produced by the entire CPU package under sustained workload, including all on-die components. RAM and VRM heat is separate and not included in the CPU's TDP.
- *Why D is incorrect:* TDP stands for Thermal Design Power. It has nothing to do with storage or I/O performance.

---

### Question 18

A CPU has been installed in a LGA1700 socket. The technician notices that the load plate bent slightly during installation. What is the likely consequence if the system is powered on without correcting this?

- A) The CPU will not be damaged because the IHS protects the die from uneven pressure
- B) Uneven pressure from a bent load plate can crack the CPU die or cause incomplete contact, leading to instability or failure
- C) The bent load plate will straighten itself under thermal expansion during the first boot cycle
- D) The only consequence is aesthetic — the system will operate normally with a bent load plate

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The LGA load plate applies even distributed pressure across the CPU's contact pads. A bent load plate creates uneven contact — some pads receive more pressure and some lose contact entirely. This can cause electrical failures (intermittent connection loss on CPU pins) and, in severe cases, physical stress that cracks the CPU die. Cracked silicon is a terminal failure.
- *Why A is incorrect:* The IHS protects the die from direct mechanical contact with the cooler, but it does not protect against uneven clamp pressure from a distorted load plate pressing asymmetrically on the CPU package.
- *Why C is incorrect:* Metal does not self-correct under thermal expansion in the temperature range of normal CPU operation. A bent load plate remains bent and continues to cause uneven contact across thermal cycles.
- *Why D is incorrect:* A bent load plate is not merely aesthetic. Uneven contact on an LGA socket causes signal integrity failures on affected pins, which manifests as POST errors, system instability, or complete boot failure.

---

### Question 19

What is the purpose of cache memory in a CPU, and which cache level is shared across all cores in a modern processor?

- A) Cache memory is a high-speed register that stores the CPU's current instruction pointer; L1 is shared across all cores
- B) Cache memory is SRAM on the CPU die that stores recently accessed data and instructions to reduce RAM access latency; L3 is shared across all cores
- C) Cache memory is DRAM built into the CPU package for lower cost; L2 is shared across all cores
- D) Cache memory stores the CPU's BIOS configuration; L3 is private to each core to protect settings from cross-core access

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* CPU cache is small-capacity, high-speed SRAM integrated on the processor die. It forms a hierarchy: L1 (fastest, smallest, private per core) → L2 (medium, private per core) → L3 (largest, slower, shared among all cores). The L3 cache acts as a shared pool that all cores can access, reducing main RAM reads for frequently used data across the whole workload.
- *Why A is incorrect:* The instruction pointer (program counter) is a CPU register, not cache memory. L1 is private per core, not shared.
- *Why C is incorrect:* CPU cache uses SRAM (Static RAM), not DRAM (Dynamic RAM). SRAM is more expensive and power-hungry but far faster than DRAM, which is why cache is small in size. L2 is private per core on most modern designs.
- *Why D is incorrect:* Cache memory has nothing to do with BIOS configuration. BIOS settings are stored in a dedicated flash chip on the motherboard.

---

### Question 20

A workstation has a CPU spec listed as "16C/32T." What does this notation mean, and what technology enables the thread count to be double the core count?

- A) 16 cores and 32 total cache levels; L1 through L32 caches are distributed across the die
- B) 16 physical cores, each capable of executing 32 simultaneous instructions per clock cycle
- C) 16 physical cores and 32 logical threads, enabled by Hyper-Threading (Intel) or SMT (AMD)
- D) 16 performance cores and 32 efficiency cores for a total of 48 execution units

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The notation 16C/32T means 16 physical cores and 32 logical threads. Intel's Hyper-Threading (HT) and AMD's Simultaneous Multi-Threading (SMT) allow each physical core to execute two threads simultaneously by sharing internal execution resources between two logical processors. The OS sees 32 logical CPUs and can schedule 32 independent threads across them.
- *Why A is incorrect:* "32T" in CPU notation always refers to threads, not cache levels. CPUs have three cache levels (L1, L2, L3) — not 32. Cache levels are not what the thread count notation describes.
- *Why B is incorrect:* Instructions per clock cycle (IPC) is a different architectural metric describing execution efficiency per cycle. It is not encoded in the core/thread count notation. A core executing 32 instructions per clock would require a 32-wide superscalar design — not what 32T means.
- *Why D is incorrect:* Intel's hybrid architecture (P-cores + E-cores) uses a different notation. A chip with 16 P-cores and 32 E-cores would typically be listed differently. The 16C/32T format specifically describes 16 identical cores with SMT/HT enabled.
