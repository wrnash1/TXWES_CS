# Video Script: Module 04 - Memory (RAM) Types and Configuration

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Estimated Duration:** 20–22 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.3: Given a scenario, install RAM types
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

Stage the following components before recording:

- One DDR4 DIMM (288-pin desktop)
- One DDR5 DIMM if available (288-pin desktop, different notch position)
- One DDR4 SODIMM (260-pin laptop)
- A motherboard with visible, color-coded RAM slots (ideally 4-slot board showing A1/A2/B1/B2)
- A laptop with the service panel removed showing SODIMM slots (or a reference image)

Key exam traps to call out explicitly:

- DDR4 and DDR5 both have 288 pins on the DIMM form factor — the notch position distinguishes them, not pin count
- Dual-channel requires paired slots (A1+B1 or A2+B2), NOT adjacent slots (A1+A2)
- SODIMM inserts at approximately 45 degrees, then presses flat — different from DIMM which presses straight down
- ECC RAM is not interchangeable with non-ECC on consumer boards

Safety notes:

- Always wear an ESD strap before handling RAM modules
- Hold RAM by the edges; never touch the gold edge contacts
- Press straight down evenly on both ends of a DIMM — uneven pressure can crack the PCB
- For SODIMM, insert at the correct angle before pressing down — forcing at the wrong angle bends the contacts

---

## Section 1: Introduction and Certification Alignment [00:00 - 03:00]

**[CAMERA: Instructor on camera, title card "Module 04 — Memory (RAM) Types and Configuration"]**

"Welcome back, class. Professor Nash here. Module 04 is all about RAM — Random Access Memory — the volatile working memory your CPU uses to hold running programs and active data. When you upgrade a computer's RAM or troubleshoot a system with memory errors, you need to get this right. The wrong RAM generation, the wrong slot configuration, or a module that is not fully seated will either prevent the system from booting or cause intermittent crashes that are difficult to diagnose.

Today we cover three major areas: DDR generations and their physical differences; DIMM versus SODIMM form factors and where each is used; and dual-channel configuration — how to set it up and why it matters for performance.

This material maps to CompTIA A+ Core 1 Domain 3.3. You will see RAM installation scenarios on the exam where you need to identify the correct generation, explain why a module won't seat, or explain why dual-channel isn't activating. Let's go."

**[PAUSE — 3 seconds]**

---

## Section 2: DDR Generations — DDR3, DDR4, and DDR5 [03:00 - 09:00]

**[CAMERA: Cut to component table]**

**[SHOW COMPONENT: Hold up DDR4 DIMM — show both sides]**

"DDR stands for Double Data Rate synchronous DRAM. The 'double data rate' part means the module transfers data on both the rising and falling edges of the clock signal, effectively doubling throughput compared to the original SDR SDRAM that came before it. The number after DDR — 3, 4, 5 — indicates the generation.

Each generation runs faster, uses less voltage, and is physically keyed differently so you cannot insert the wrong generation into a slot. Let me walk through the three generations you need to know.

DDR3. This is older technology — 2007 through roughly 2014 mainstream. DDR3 DIMMs have 240 pins. Operating voltage is 1.5 volts for standard modules, 1.35 volts for low-voltage DDR3L. You will still encounter DDR3 systems in the field when servicing older hardware. The notch — the gap in the gold contacts along the bottom edge — is positioned toward the center of the module.

**[SHOW COMPONENT: Hold up DDR4 DIMM next to DDR3 image if available]**

DDR4. This is the dominant generation for desktops built from roughly 2014 through 2022. DDR4 DIMMs have 288 pins on a desktop DIMM. Operating voltage is 1.2 volts — lower than DDR3, which means less heat and better power efficiency. DDR4 data rates range from DDR4-2133 up to DDR4-3600 and beyond for overclocked kits.

The notch on a DDR4 DIMM is shifted slightly off-center compared to DDR3. This physical key is what prevents you from inserting DDR3 into a DDR4 slot and vice versa. The slot is keyed to match only one generation.

**[SHOW COMPONENT: Hold DDR5 DIMM if available — emphasize similar physical size to DDR4]**

DDR5. The current generation for platforms shipping from 2021 onward. DDR5 DIMMs also have 288 pins — same pin count as DDR4 — but the notch is in a different position than DDR4. You cannot insert a DDR5 DIMM into a DDR4 slot and you cannot insert a DDR4 DIMM into a DDR5 slot, even though the pin counts are the same. The notch is the physical safety mechanism.

DDR5 operating voltage is 1.1 volts. DDR5 integrates the voltage regulator onto the module itself rather than the motherboard — this is why DDR5 and DDR4 are not electrically interchangeable even if you somehow overcame the physical key.

**[PAUSE — 3 seconds]**

Here is the exam trap I want you to remember: DDR4 and DDR5 both have 288 pins on a desktop DIMM. The pin count alone does not distinguish them. The notch position does. If a question says a RAM module has 288 pins and asks what generation it is — without mentioning the notch — the answer could be DDR4 or DDR5. The notch is the only reliable physical identifier between those two generations."

**[CAMERA: Slide with DDR comparison table]**

"Let me lock in the numbers. DDR3: 240 pins, 1.5V. DDR4: 288 pins, 1.2V. DDR5: 288 pins, 1.1V. For laptop SODIMMs: DDR3 SODIMM has 204 pins; DDR4 SODIMM has 260 pins; DDR5 SODIMM has 262 pins. The SODIMM pin counts are all different from each other, which helps distinguish generations in the laptop context."

---

## Section 3: DIMM vs. SODIMM Form Factors [09:00 - 13:30]

**[CAMERA: Hold up DIMM and SODIMM side by side]**

**[SHOW COMPONENT: Full-size DDR4 DIMM in one hand, DDR4 SODIMM in the other]**

"Now let's talk about the two physical form factors: DIMM and SODIMM.

DIMM stands for Dual Inline Memory Module. The word 'dual inline' refers to the fact that the contacts on both sides of the PCB are electrically independent — unlike older SIMMs where both sides were the same circuit. A standard desktop DIMM is approximately 133 millimeters long. This is what you install in desktop motherboards, workstations, and some all-in-one PCs.

SODIMM stands for Small Outline DIMM. It is roughly half the length — about 67 millimeters. SODIMM is the standard memory format for laptops, mini PCs, and some smaller embedded systems. Both DIMM and SODIMM come in DDR3, DDR4, and DDR5 variants. But here is what you must know: a DDR4 SODIMM and a DDR4 DIMM are both DDR4 and run at the same speeds, but they are physically incompatible — different size, different slot, different pin count. You cannot install a laptop SODIMM in a desktop motherboard or vice versa.

**[SHOW COMPONENT: Open laptop with SODIMM slots visible, or reference image]**

Installing a SODIMM is different from installing a DIMM. A SODIMM inserts at approximately a 30–45 degree angle into the slot. Once the module is fully inserted, you press it down flat until the retaining clips on both sides of the slot snap into the notches on the module edges. To remove a SODIMM, you press the retaining clips outward and the module pops up to the insertion angle, allowing you to slide it out.

**[SHOW COMPONENT: Desktop motherboard RAM slot — demonstrate DIMM installation]**

A DIMM installs differently. You press straight down with even pressure on both ends simultaneously until the locking clips on both sides of the slot snap upward into the notches on the module. The clips should click audibly. If only one side snaps and the other does not, the module is not fully seated and the system will likely not POST or will generate memory errors.

**[PAUSE — 3 seconds]**"

---

## Section 4: Dual-Channel Configuration [13:30 - 18:30]

**[CAMERA: Close-up of motherboard RAM slots showing color coding]**

**[SHOW COMPONENT: Point to the color-coded slot pairs on the motherboard]**

"Dual-channel is a memory architecture where two RAM modules are accessed simultaneously in parallel, effectively doubling the memory bandwidth compared to single-channel operation. On a modern DDR4 or DDR5 system, dual-channel can make a noticeable difference in memory-intensive tasks — video editing, large spreadsheets, gaming on integrated graphics — because the CPU's memory controller is pulling data from two modules at once instead of one.

Here is the critical rule: dual-channel requires modules in the correct paired slots. Look at the motherboard. The four slots are labeled — either by color or by text printed on the board: A1, A2, B1, B2. A1 and B1 belong to channel A and channel B respectively. A2 and B2 are the second slots for each channel.

To activate dual-channel with two modules, you install them in A1 and B1 — or A2 and B2. You are pairing one module per channel. This is what the motherboard manual means when it says 'install in slots 1 and 3' or 'install in the blue slots.'

Here is the exam trap: if you install two modules in A1 and A2 — two adjacent slots of the same color — you are putting both modules on the same channel. The system will recognize both modules and show the full capacity, but it will run in single-channel mode. No error message. No warning. Just reduced bandwidth. Many users and beginning technicians make this mistake.

**[CAMERA: Slide showing slot layout diagram]**

'But Professor Nash, my motherboard only shows two RAM slots. How do I do dual-channel?' If you have exactly two slots — which is common on Mini-ITX boards and laptops — then any two installed modules automatically run in dual-channel as long as they are compatible. With only two physical slots and one module per channel, there is no wrong slot to choose.

For a four-slot board with two modules: always use A1+B1 or A2+B2. Consult the motherboard manual if the slot labeling is not printed on the board. Some boards print it in very small text near each slot.

**[PAUSE — 3 seconds]**

What about mixing RAM speeds or brands? The system will work — it runs at the speed of the slower module and may drop into single-channel mode on some boards. For best results and guaranteed dual-channel operation, use a matched pair — two modules of the same brand, speed, capacity, and part number. These are sold as kits for exactly this reason."

---

## Section 5: Memory Errors and Lab Walkthrough [18:30 - 21:00]

**[CAMERA: Instructor on camera]**

"Let me briefly cover memory errors before walking you through the lab.

The most common memory-related POST failure is a system that powers on but produces no video — sometimes with beep codes from the motherboard. Beep codes for memory errors vary by BIOS vendor: AMI BIOS uses a pattern like three long beeps; Award BIOS has its own patterns. Check the motherboard manual for the specific code. The first thing to try: remove all modules, clean the slot contacts with a dry cotton swab or compressed air, reseat the modules firmly, and retry.

If one module works but not the other, you can isolate a failed module by testing each one individually in the known-good slot. A system that boots with module A but not with module B identifies the failing module.

For the lab this week, you will identify DDR generation from physical inspection, complete a slot identification exercise for dual-channel configuration, perform or document a DIMM installation, examine a laptop SODIMM installation, and answer scenario questions about memory troubleshooting. Bring the reading guide; the spec tables in it are directly useful for the identification exercise.

Complete the lab, take the quiz, and post your discussion response by Wednesday at 11:59 PM. I will see you in Module 05."

---

## End Card [21:00 - 22:00]

**[CAMERA: Title card]**

"This has been Module 04 of CIS-2320 Hardware Fundamentals at Texas Wesleyan University. Key takeaways: DDR3 = 240 pins desktop; DDR4 = 288 pins, 1.2V; DDR5 = 288 pins, 1.1V — notch position distinguishes DDR4 from DDR5. DIMM is desktop; SODIMM is laptop. Dual-channel requires paired slots A1+B1, not adjacent A1+A2."

---

## Additional Resources

- [Professor Messer CompTIA A+ Core 1 (220-1101) Free Course — Memory Types and Installation](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
- [CompTIA A+ Core 1 Official Exam Objectives](https://www.comptia.org/certifications/a)
