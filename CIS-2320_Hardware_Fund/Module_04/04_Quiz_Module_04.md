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
