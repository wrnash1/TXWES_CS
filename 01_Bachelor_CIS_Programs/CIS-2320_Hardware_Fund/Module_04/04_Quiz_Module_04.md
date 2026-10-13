# Quiz: Module 04 - Memory (RAM) Types and Configuration

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.3
**Format:** 10 multiple-choice questions | 10 points each | 100 points total

---

### Question 1

Which RAM type is specifically designed for space-constrained laptops and small form factor systems?

- A) DIMM
- B) SODIMM
- C) SDRAM
- D) GDDR

Correct Answer: B — SODIMM (Small Outline DIMM) is approximately 67 mm long, roughly half the length of a standard DIMM, and is the standard compact memory form factor for laptops and mini-PCs.

Distractor Analysis:

- Why A is incorrect: DIMM is the full-size desktop form factor at approximately 133 mm. It does not fit in laptop memory slots.
- Why C is incorrect: SDRAM (Synchronous DRAM) is the general class of synchronous dynamic RAM — it describes a technology, not a physical form factor. DDR4 is a type of SDRAM.
- Why D is incorrect: GDDR (Graphics DDR) is RAM used on dedicated graphics cards, not installed in system memory slots. It is not a user-installable desktop or laptop RAM module.

---

### Question 2

Which of the following most accurately describes the difference between SODIMM and DIMM?

- A) SODIMM modules are approximately 67 mm long and designed for laptops and small form factor systems, while full-size DIMMs are approximately 133 mm long and used in desktop PCs; both come in DDR4 and DDR5 variants but are not interchangeable.
- B) SODIMM modules operate at higher voltages than DIMMs, making them faster but less energy-efficient in battery-powered devices.
- C) DIMMs use a single row of contacts on one side of the module, while SODIMMs use contacts on both sides, doubling their data bus width.
- D) SODIMM and DIMM refer to the same physical module; the naming difference only indicates whether the RAM is registered (buffered) or unbuffered.

Correct Answer: A — This accurately describes the physical size difference, typical use cases, and the fact that DIMM and SODIMM are not physically interchangeable despite sharing DDR generations.

Distractor Analysis:

- Why B is incorrect: SODIMMs operate at the same or lower voltages compared to DIMMs within the same generation. DDR4 SODIMMs and DIMMs both run at 1.2V standard.
- Why C is incorrect: Both DIMM and SODIMM have the "dual inline" design with electrically independent contacts on both sides. This is not a distinguishing difference between the two form factors.
- Why D is incorrect: SODIMM and DIMM are physically distinct form factors with different sizes and pin counts. The buffered/unbuffered (registered) distinction is a separate specification unrelated to form factor naming.

---

### Question 3

A technician installs two 8 GB DDR4 DIMMs into a motherboard that supports dual-channel memory. After boot, a diagnostic utility shows the memory running in single-channel mode. What is the most likely cause?

- A) The two modules are from different manufacturers, which disables dual-channel
- B) The modules were installed in adjacent slots (e.g., A1 and A2) instead of paired slots (e.g., A1 and B1)
- C) DDR4 does not support dual-channel mode; only DDR3 supports this feature
- D) The total installed RAM exceeds the motherboard's single-channel capacity threshold

Correct Answer: B — Dual-channel requires modules in paired channel slots (one module per channel). Adjacent slots A1 and A2 are both on the same channel, resulting in single-channel operation even with two modules installed.

Distractor Analysis:

- Why A is incorrect: Different manufacturers do not prevent dual-channel. Matching capacity and speed are the key requirements; brand mismatch is not a hardware barrier to dual-channel.
- Why C is incorrect: DDR4 fully supports dual-channel operation. Dual-channel is a motherboard memory controller feature, not a DDR-generation limitation.
- Why D is incorrect: There is no RAM capacity threshold that disables dual-channel. The correct paired slot installation is the only hardware requirement.

---

### Question 4

A user adds a second 8 GB DDR4 stick to their desktop after a memory upgrade. The system randomly crashes with memory errors. Both sticks are the same brand and speed. What should the technician check first?

- A) Whether the power supply has enough wattage to support additional RAM
- B) Whether the new module is seated in the correct dual-channel slot and the locking clips are fully engaged
- C) Whether the operating system license supports more than 8 GB of RAM
- D) Whether the SATA data cable needs to be replaced due to interference with the RAM slots

Correct Answer: B — Improperly seated RAM is the most common cause of memory errors and instability after an upgrade. If a locking clip is not fully engaged, the module makes intermittent contact which causes random crashes and memory errors.

Distractor Analysis:

- Why A is incorrect: RAM draws very little additional power (typically 3–5W per module). A PSU adequate for the original system easily powers additional RAM.
- Why C is incorrect: Windows 10/11 Home supports up to 128 GB RAM. Memory capacity is not a software licensing restriction for standard consumer workloads.
- Why D is incorrect: SATA cables connect to storage drives and have no electrical interaction with RAM slots. They cannot cause memory errors.

---

### Question 5

How are DDR4 and DDR5 DIMMs physically distinguished from each other to prevent accidental cross-generation installation?

- A) DDR5 DIMMs are shorter than DDR4 DIMMs, so they will not reach the full length of a DDR4 slot
- B) DDR5 DIMMs have a different notch position along the bottom edge compared to DDR4, preventing insertion into a DDR4 slot
- C) DDR5 DIMMs have gold contacts on both sides while DDR4 contacts are only on one side
- D) DDR5 DIMMs require a locking tab on the top edge of the slot that DDR4 slots do not have

Correct Answer: B — The key notch along the bottom contact edge is in a different position on DDR4 versus DDR5 DIMMs. This physical key prevents a DDR5 module from seating in a DDR4 slot and vice versa, even though both have 288 pins.

Distractor Analysis:

- Why A is incorrect: DDR4 and DDR5 desktop DIMMs are both 133.35 mm long. Physical length is identical; it is not the distinguishing physical feature.
- Why C is incorrect: Both DDR4 and DDR5 DIMMs have gold contacts on both sides of the PCB. Contact placement on both sides is the "dual inline" design shared by all DIMM generations.
- Why D is incorrect: There is no additional top-edge locking tab unique to DDR5. The notch keying mechanism on the contact edge is the standard physical safety feature for all DDR DIMM generations.

---

### Question 6

A technician is upgrading a system that currently has one 8 GB DDR4-2133 module in slot A1. They add a second 8 GB DDR4-3200 module to slot B1. What is the expected behavior after this upgrade?

- A) The system will not POST because the two modules run at different speeds
- B) The system will run in dual-channel mode at the speed of the slower module (DDR4-2133)
- C) The system will automatically run both modules at DDR4-3200 by overclocking the slower module
- D) The system will use only the faster DDR4-3200 module and ignore the slower one

Correct Answer: B — When modules of different speeds are installed, the system defaults to the speed of the slower module for stability. Dual-channel can still activate if the modules are in paired slots, but the entire system runs at the lower speed.

Distractor Analysis:

- Why A is incorrect: Mismatched DDR4 speeds do not prevent POST. The system negotiates to the lower speed and boots normally.
- Why C is incorrect: The system does not overclock the slower module to match the faster one. Overclocking in BIOS only applies uniformly and requires the slower module to be capable of that speed.
- Why D is incorrect: The system uses both modules and adds their capacity. It does not discard or ignore the slower module; it runs the pair at the lower speed.

---

### Question 7

What does enabling XMP in the BIOS accomplish for a DDR4-3600 RAM kit installed in a compatible motherboard?

- A) It enables error correction on the modules, converting them from standard to ECC operation
- B) It applies the manufacturer's tested speed and timing profile, allowing the RAM to run at its rated 3600 MHz instead of the default JEDEC speed
- C) It activates dual-channel mode by instructing the memory controller to use both channels simultaneously
- D) It increases the operating voltage above 1.2V to improve RAM stability at stock JEDEC speeds

Correct Answer: B — XMP (Intel eXtreme Memory Profile) stores the manufacturer's validated speed, timing, and voltage settings on the module. Enabling XMP in BIOS applies these settings so the RAM runs at its advertised speed (e.g., 3600 MHz) rather than defaulting to the base JEDEC speed (typically DDR4-2133 or DDR4-2400).

Distractor Analysis:

- Why A is incorrect: XMP has nothing to do with error correction. ECC is a separate hardware feature requiring ECC-capable modules and a supporting motherboard/CPU platform.
- Why C is incorrect: Dual-channel is determined by slot placement, not a BIOS profile setting. XMP does not affect which channels are active.
- Why D is incorrect: XMP does apply specific voltages defined by the profile, but these are the manufacturer's rated voltages for the advertised speed — not a generic voltage increase for stock speed stability.

---

### Question 8

A technician needs to upgrade a laptop's RAM from 8 GB to 16 GB. The laptop has two memory slots, currently with one 8 GB DDR4 SODIMM in slot 1 and slot 2 empty. Which action is correct?

- A) Purchase a DDR4 DIMM and install it in slot 2; DIMM and SODIMM are interchangeable in most laptops
- B) Purchase a DDR4 SODIMM and install it in slot 2 at the correct angle before pressing flat to engage the retaining clips
- C) Purchase a DDR5 SODIMM for slot 2 to improve overall system performance through cross-generation pairing
- D) Remove the existing 8 GB module and install a single 16 GB DDR4 DIMM in slot 1

Correct Answer: B — Laptop memory requires SODIMM modules. A DDR4 SODIMM should be installed in the empty slot at the manufacturer-specified insertion angle (typically 30–45 degrees) and then pressed flat until the side retaining clips engage.

Distractor Analysis:

- Why A is incorrect: DIMMs and SODIMMs are physically incompatible. A standard DIMM is approximately twice the length of a SODIMM and will not fit in a laptop SODIMM slot.
- Why C is incorrect: DDR5 and DDR4 SODIMMs have different notch positions and are not interchangeable. A DDR5 SODIMM will not seat in a DDR4 laptop slot and the two generations cannot be mixed.
- Why D is incorrect: A full-size DIMM will not fit in a laptop SODIMM slot, regardless of capacity.

---

### Question 9

Which of the following correctly explains why DDR3 and DDR4 DIMMs are not interchangeable even though both are installed in desktop motherboards?

- A) DDR3 modules are shorter than DDR4 modules and will not make full contact with the slot's gold fingers
- B) DDR3 has 240 pins and DDR4 has 288 pins; the different pin counts and notch positions physically prevent cross-generation installation
- C) DDR3 modules require a higher operating voltage than DDR4 slots can supply, causing immediate damage
- D) DDR3 and DDR4 are electrically compatible but use different BIOS commands that consumer boards cannot translate

Correct Answer: B — DDR3 and DDR4 DIMMs have different pin counts (240 vs. 288) and different notch positions. Both differences physically prevent a DDR3 module from seating in a DDR4 slot or vice versa.

Distractor Analysis:

- Why A is incorrect: DDR3 and DDR4 desktop DIMMs are approximately the same physical length (~133 mm). Length is not the distinguishing physical barrier between these generations.
- Why C is incorrect: While DDR3 (1.5V) and DDR4 (1.2V) do run at different voltages, immediate damage is not the primary reason — the physical key prevents insertion before any electrical contact is made.
- Why D is incorrect: DDR3 and DDR4 are not electrically compatible. The voltage, signaling protocol, and timing architecture are all different. This is not a BIOS translation issue.

---

### Question 10

A desktop system has four RAM slots. A technician wants to install 32 GB of DDR4 RAM using four 8 GB modules. After installation and boot, only 24 GB is reported in BIOS. All four slots appear to have modules installed. What is the most likely explanation?

- A) The motherboard does not support more than 24 GB total RAM capacity
- B) One of the four modules is not fully seated and is not being detected by the memory controller
- C) DDR4 supports a maximum of three active modules; the fourth module is automatically disabled
- D) The operating system cannot display more than 24 GB without a BIOS update

Correct Answer: B — When a DIMM is not fully seated, its locking clips do not engage completely and the module makes insufficient contact with the slot's pins. The memory controller cannot detect or address the module, and BIOS reports only the capacity of the three seated modules.

Distractor Analysis:

- Why A is incorrect: Most modern consumer motherboards support 32–128 GB total capacity across four slots. There is no common platform that caps at 24 GB specifically.
- Why C is incorrect: DDR4 has no three-module limit. All four slots can be populated simultaneously on any standard four-slot board.
- Why D is incorrect: BIOS reports the physical RAM detected by the memory controller, independent of any OS display limitation. An OS display limitation would appear in Windows, not in the BIOS memory readout.

---

### Question 11

A technician needs to install ECC RAM in a workstation for a financial database application. Which of the following is required for ECC to function?

- A) Any DDR4 motherboard with XMP support can use ECC modules
- B) The motherboard and CPU must both support ECC; consumer platforms typically do not
- C) ECC RAM is enabled by installing two matching ECC modules in dual-channel slots
- D) ECC is activated by enabling the error correction setting in Windows Device Manager

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* ECC (Error-Correcting Code) RAM requires explicit hardware support in both the CPU's memory controller and the motherboard's chipset. Consumer Intel Core and AMD Ryzen platforms typically do not support ECC. ECC is natively supported on AMD Ryzen Pro, Intel Xeon, and AMD EPYC platforms, paired with server/workstation motherboards.
- *Why A is incorrect:* XMP support has nothing to do with ECC. XMP profiles define speed and timing overclocking parameters for performance RAM — completely unrelated to error correction. A consumer board with XMP support cannot run ECC modules in ECC mode.
- *Why C is incorrect:* Installing two ECC modules in dual-channel does not activate ECC. ECC operation is determined by hardware support in the CPU and chipset, not by dual-channel slot placement.
- *Why D is incorrect:* ECC is a hardware feature implemented in the memory chips and the CPU's memory controller. It is not a software setting in Windows. Windows reports ECC status but cannot enable or disable the hardware feature.

---

### Question 12

What does the PC4-25600 notation mean for a RAM module, and what is the equivalent DDR notation?

- A) PC4-25600 means the module has 25,600 MB of capacity; it is equivalent to DDR4-12800
- B) PC4-25600 is the module's peak bandwidth in MB/s; it is equivalent to DDR4-3200
- C) PC4-25600 means the module has 25,600 pins arranged in a specific grid pattern; DDR4 notation is not equivalent
- D) PC4-25600 describes the latency in nanoseconds; DDR4-3200 describes the clock speed in MHz

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The PC notation (PC4 = DDR4 generation) expresses the module's peak theoretical bandwidth in MB/s. DDR4-3200 runs at 3200 MT/s × 8 bytes (64-bit bus width) = 25,600 MB/s = PC4-25600. This is a direct mathematical relationship: DDR speed × 8 = PC bandwidth rating.
- *Why A is incorrect:* The PC number is bandwidth in MB/s, not module capacity. The equivalent DDR rating calculation given is also incorrect.
- *Why C is incorrect:* The PC notation has nothing to do with pin count. Pin count (288 for DDR4) is a separate physical characteristic.
- *Why D is incorrect:* PC4-25600 is not a latency value. Latency is expressed in CAS latency timings (e.g., CL16-18-18-38), which are separate from the bandwidth/speed notation.

---

### Question 13

A server administrator orders DDR4 RAM modules described as "Registered (R-DIMM)" for a dual-processor server. How does registered RAM differ from unbuffered RAM?

- A) Registered RAM has an error-correction chip soldered onto the PCB that corrects single-bit errors in real time
- B) Registered RAM includes a register (buffer chip) between the DRAM chips and the memory controller, reducing electrical load and allowing more modules per channel
- C) Registered RAM runs at lower voltages than unbuffered RAM, making it suitable for power-efficient server environments
- D) Registered RAM uses a proprietary connector that only fits server-class motherboard slots

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Registered (buffered) DIMMs contain a register chip (RCD — Registered Clock Driver) that buffers the address and command signals between the memory controller and the DRAM chips. This reduces the electrical load on the memory controller, allowing more DIMMs per channel and enabling very large memory configurations. Consumer platforms do not support R-DIMMs.
- *Why A is incorrect:* This describes ECC functionality, not the registered characteristic. ECC and registered are separate features. A module can be ECC without being registered, or both ECC and registered (ECC R-DIMM).
- *Why C is incorrect:* Registered DIMMs operate at the same voltage as equivalent unbuffered DIMMs within the same DDR generation. Voltage is not the distinguishing characteristic.
- *Why D is incorrect:* R-DIMMs use standard DDR4 or DDR5 DIMM connectors. The physical connector is identical to unbuffered DIMMs; the incompatibility with consumer boards is electrical/protocol-based, not physical.

---

### Question 14

What is the "1R" designation in a RAM module label such as "8GB 1Rx8"?

- A) The module has a single rank, meaning it has one set of DRAM chips that the memory controller addresses at once
- B) The "1R" indicates the module is the first revision in its production run
- C) The module has a refresh cycle rate of 1 ms, faster than standard DDR4 modules
- D) "1R" means the module contains a single row of DRAM chips on one side of the PCB only

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* A "rank" is a set of DRAM chips that the memory controller accesses simultaneously as one 64-bit logical unit. A 1Rx8 module has one rank of eight 8-bit-wide chips (8×8 = 64 bits). A 2Rx8 module has two ranks and provides more capacity at the cost of slightly higher latency during rank switching.
- *Why B is incorrect:* "R" in DDR module labeling always refers to rank count, not production revision number.
- *Why C is incorrect:* Refresh cycle rate is not encoded in the consumer module label. DRAM refresh is managed internally by the memory controller and is not expressed as a rank designation.
- *Why D is incorrect:* Rank refers to an electrical addressing concept, not physical chip placement. A single-rank module can have chips on both sides of the PCB.

---

### Question 15

After installing new RAM, a system produces three short beeps during POST and does not boot. What does this symptom indicate?

- A) The CPU is overclocked beyond its maximum safe frequency
- B) The RAM is not being detected or there is a memory initialization failure
- C) The GPU requires a firmware update before the system can POST
- D) The SSD has failed and the system is broadcasting the failure through the speaker

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* POST beep codes are emitted to signal hardware initialization failures before any display output is possible. Three beeps is a common memory error code on many BIOS implementations (AMI BIOS associates 3 beeps with memory errors). A failure to detect RAM immediately after a RAM installation change is the most exam-appropriate answer.
- *Why A is incorrect:* CPU overclocking failures typically cause a no-boot condition with no beeps, or a continuous single beep. Three beeps is specifically associated with memory errors in standard beep code tables.
- *Why C is incorrect:* GPU firmware is updated from within an operating system. A GPU issue does not generate memory-type beep codes at POST.
- *Why D is incorrect:* Storage drive failures do not generate POST beep codes. Drive failures are reported after POST completes.

---

### Question 16

A DDR4-3200 module has a physical clock frequency of:

- A) 3200 MHz — the data rate equals the clock frequency
- B) 1600 MHz — DDR transfers data on both the rising and falling edges of each clock cycle, so the data rate is double the clock
- C) 800 MHz — DDR uses quadruple data rate internally, so the external clock is divided by four
- D) 6400 MHz — the effective bandwidth is double the advertised data rate

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* DDR stands for Double Data Rate. Data is transferred on both clock edges, yielding two transfers per cycle. DDR4-3200 has a physical base clock of 1600 MHz × 2 = 3200 MT/s. This is why DDR4-3200 is also called PC4-25600: 3200 MT/s × 8 bytes = 25,600 MB/s.
- *Why A is incorrect:* DDR4-3200 does not have a 3200 MHz physical clock oscillation. The "3200" refers to the data transfer rate in MT/s, not the base clock frequency.
- *Why C is incorrect:* 800 MHz is not the correct base clock for DDR4-3200. DDR4 uses an 8n prefetch internally, but the external interface speed is expressed as the full data rate.
- *Why D is incorrect:* 6400 is the data rate of DDR5-6400, not the bandwidth of DDR4-3200.

---

### Question 17

Which free tool is the standard technician utility for verifying dual-channel memory operation without opening the case?

- A) Windows Event Viewer — it logs memory channel configuration at each boot
- B) CPU-Z — the Memory tab shows Channel # as Single, Dual, or Quad
- C) Device Manager — the RAM entry shows channel count in the properties window
- D) Task Manager — the Performance > Memory tab shows the number of active memory channels

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* CPU-Z is a free system information utility. Its Memory tab explicitly reports the Channel # field as "Single," "Dual," or "Quad," confirming whether the memory controller is operating in dual-channel mode. This is the standard technician tool for verifying RAM configuration without hardware disassembly.
- *Why A is incorrect:* Windows Event Viewer logs OS and application events. It does not log memory channel configuration.
- *Why C is incorrect:* Device Manager shows hardware devices and driver status. RAM channel count is not displayed there.
- *Why D is incorrect:* Task Manager's Performance > Memory view shows total RAM, speed, and form factor, but does not display single vs. dual-channel status. That detail requires CPU-Z.

---

### Question 18

Which of the following would cause a Windows system to show less available RAM than physically installed?

- A) The hard drive is nearly full, leaving no room for the virtual memory paging file
- B) A portion of RAM is reserved by the iGPU for shared graphics memory
- C) The OS cannot use RAM above 4 GB unless 64-bit mode is enabled in BIOS
- D) RAM modules from different manufacturers run at different speeds, reducing usable capacity

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Systems with integrated graphics that share system RAM allocate a portion of physical RAM for graphics use. This shows as "Hardware Reserved" in Task Manager's Memory view. For example, a system with 16 GB RAM and 1 GB reserved for iGPU shows 15 GB available to Windows.
- *Why A is incorrect:* Hard drive free space affects the size of the paging file (virtual memory) but does not reduce the physical RAM visible to Windows.
- *Why C is incorrect:* 64-bit mode is not a BIOS setting requiring separate activation. Modern x86-64 systems with a 64-bit OS always run in 64-bit mode. A 32-bit OS is limited to ~4 GB, but that is an OS limitation, not a BIOS toggle.
- *Why D is incorrect:* RAM modules from different manufacturers running at different speeds do not reduce total visible capacity. The system runs all modules at the lower speed but includes all capacity in the total addressable memory.

---

### Question 19

A user installs a DDR5 DIMM in a DDR4-only motherboard. What happens?

- A) The module runs at DDR4 speeds due to automatic cross-generation negotiation
- B) The module physically cannot be inserted because the notch positions differ between DDR4 and DDR5
- C) The system boots but reports a BIOS compatibility warning
- D) The DDR5 module operates in a legacy compatibility mode at 2133 MHz

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* DDR4 and DDR5 DIMMs both have 288 pins but have different notch positions on the contact edge. This physical keying prevents a DDR5 module from seating in a DDR4 slot. The notch alignment stops the module before any pins make contact.
- *Why A is incorrect:* There is no cross-generation DDR auto-negotiation. DDR4 and DDR5 use fundamentally different signaling protocols and electrical specifications.
- *Why C is incorrect:* The module cannot be physically inserted, so no boot sequence or BIOS warning is ever reached.
- *Why D is incorrect:* There is no DDR5-to-DDR4 legacy compatibility mode. The two generations are electrically incompatible.

---

### Question 20

After running MemTest86, a technician finds errors at specific memory addresses. What is the MOST appropriate next step?

- A) Format and reinstall Windows because OS files are corrupted at those memory addresses
- B) Enable XMP in BIOS to correct the memory timing errors MemTest86 detected
- C) Replace the RAM module(s) that tested as faulty, testing each module individually to isolate which one has errors
- D) Update the motherboard BIOS firmware because memory errors are always caused by outdated firmware

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* MemTest86 runs before the OS loads and tests physical DRAM cells by writing and reading patterns. Errors indicate physically faulty cells in the module. The protocol is to test each module individually in a known-good slot to isolate which module has defective cells. Faulty modules must be replaced.
- *Why A is incorrect:* MemTest86 runs entirely from RAM — it has no interaction with OS files on storage. Errors reported are in RAM chips themselves, not in files on the drive.
- *Why B is incorrect:* XMP affects memory overclocking speed and timing. Enabling XMP does not repair defective DRAM cells and may actually increase error rates on a marginal module.
- *Why D is incorrect:* BIOS updates can improve RAM compatibility but do not repair physically defective DRAM cells. A confirmed hardware memory error requires module replacement.
