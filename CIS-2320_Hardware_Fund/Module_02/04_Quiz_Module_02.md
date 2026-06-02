# Quiz: Module 02 - Motherboards and Form Factors

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.5
**Format:** 10 multiple-choice questions | 10 points each | 100 points total

---

### Question1

Which form factor is typically used for compact, small-form-factor home theatre PCs?

- A) ATX
- B) Micro-ATX
- C) Mini-ITX
- D) BTX

Correct Answer: C — Mini-ITX dimensions of 6.7 x 6.7 inches make it the smallest standard motherboard form factor, purpose-built for space-constrained SFF and HTPC enclosures.

Distractor Analysis:

- Why A is incorrect: ATX measures 12 x 9.6 inches and is the full-size desktop standard — far too large for a compact HTPC case.
- Why B is incorrect: Micro-ATX at 9.6 x 9.6 inches is smaller than ATX but still a mid-size board intended for standard or mid-tower cases, not SFF builds.
- Why D is incorrect: BTX is an obsolete form factor that Intel abandoned in 2006; it is not used in modern systems and is not a valid answer for a compact build scenario.

---

### Question2

In the context of PC hardware, which of the following is the most accurate definition of a motherboard chipset?

- A) A group of integrated circuits on the motherboard that manages data flow between the CPU, RAM, storage, and expansion slots, determining CPU compatibility and available features.
- B) The set of firmware instructions stored in a flash chip that initializes hardware components and launches the boot process when a PC is powered on.
- C) A physical connector on the motherboard that accepts expansion cards such as graphics cards and network adapters, providing a direct high-speed link to the CPU.
- D) The collection of copper traces on the motherboard that carries power and data signals between sockets, slots, and onboard controllers.

Correct Answer: A — The chipset (PCH in modern systems) is the traffic controller between all major board subsystems and determines which CPUs, RAM speeds, and features the board supports.

Distractor Analysis:

- Why B is incorrect: This describes the BIOS/UEFI firmware, which is stored separately in a dedicated flash ROM chip and is not part of the chipset.
- Why C is incorrect: This describes a PCIe expansion slot — a component the chipset controls, not the chipset itself.
- Why D is incorrect: This describes the PCB trace layout, a physical feature of the board's construction rather than the chipset's function.

---

### Question3

A technician needs to install a graphics card into a desktop PC. The motherboard has PCIe x1, x4, and x16 slots available. Which slot should be used?

- A) PCIe x1 — it uses the least bandwidth, leaving more for other components
- B) PCIe x4 — it provides balanced bandwidth for both GPU and CPU tasks
- C) PCIe x16 — it provides the maximum bandwidth required for GPU operation
- D) Any slot works equally well since PCIe is fully interchangeable

Correct Answer: C — Graphics cards require a PCIe x16 slot for full performance; this slot provides the highest bandwidth (up to 32 GB/s with PCIe 4.0) and the physical length to seat a full-size GPU.

Distractor Analysis:

- Why A is incorrect: PCIe x1 slots lack both the physical length and the bandwidth to seat or run a modern GPU; a GPU will not fit in an x1 slot.
- Why B is incorrect: PCIe x4 provides insufficient bandwidth for a dedicated GPU under load, and a full-length GPU card will not physically seat in a shorter x4 slot.
- Why D is incorrect: PCIe slots are physically sized by lane count; a GPU will not insert into shorter x1 or x4 slots, so the slots are not interchangeable for all card types.

---

### Question4

A technician replaces a motherboard in a desktop PC but the system shows an incorrect date and time on every startup. Which component is most likely missing or failed?

- A) The CPU thermal paste was not reapplied during the board swap
- B) The CMOS battery was not transferred to the new board or is dead
- C) The RAM was not reseated after the motherboard was installed
- D) The PCIe graphics card is not fully inserted into the x16 slot

Correct Answer: B — The CMOS battery (CR2032) maintains BIOS/UEFI settings including date, time, and boot order when the PC is unplugged. A missing or dead battery causes these settings to reset on every power loss; the system still boots but loses clock settings.

Distractor Analysis:

- Why A is incorrect: Missing thermal paste causes CPU overheating and thermal shutdown after some minutes of operation — not incorrect date/time at every boot.
- Why C is incorrect: Improperly seated RAM causes POST failure, no-video errors, or BSODs — not clock resets.
- Why D is incorrect: A loose GPU causes display issues such as no signal or artifacts — not BIOS setting loss.

---

### Question5

A customer needs a board that fits in a standard ATX case but wants to save money by using a smaller board with fewer expansion slots. Which form factor best meets this requirement?

- A) Mini-ITX — smallest available form factor and lowest cost
- B) Micro-ATX — smaller than ATX but backward-compatible with ATX cases and less expensive
- C) E-ATX — extended ATX provides more slots at a lower price point
- D) BTX — the BTX standard replaced ATX for budget builds

Correct Answer: B — Micro-ATX boards fit in standard ATX cases due to shared mounting hole positions and typically cost less than full ATX boards because of fewer layers and fewer expansion slots.

Distractor Analysis:

- Why A is incorrect: Mini-ITX requires a specific small form factor case and does not reliably fit a standard ATX chassis without an adapter bracket.
- Why C is incorrect: E-ATX is larger and more expensive than standard ATX; it is designed for workstation and enthusiast builds — the opposite of a budget requirement.
- Why D is incorrect: BTX is an obsolete form factor abandoned around 2006; it does not represent a current budget option and is incompatible with modern components.

---

### Question6

A PCIe x1 Wi-Fi card needs to be installed in a system, but the only open slot on the motherboard is a PCIe x16 slot. What is the correct course of action?

- A) Do not install the card; a PCIe x1 card is electrically incompatible with an x16 slot
- B) Install the card in the x16 slot; a smaller PCIe card will fit and operate in a larger slot
- C) Install the card in the x16 slot but expect degraded wireless performance due to excess bandwidth
- D) Purchase a riser adapter to convert the x16 slot to x1 before installing the Wi-Fi card

Correct Answer: B — PCIe is physically and electrically backward-compatible in the direction of smaller card into larger slot. The x1 Wi-Fi card will seat in the x16 slot, use one lane of bandwidth, and operate normally.

Distractor Analysis:

- Why A is incorrect: PCIe backward compatibility is by design; smaller cards are electrically compatible with larger slots and will function correctly.
- Why C is incorrect: Excess available bandwidth does not degrade performance; the card uses only what it needs. Wi-Fi throughput is limited by the radio, not the slot bandwidth.
- Why D is incorrect: No adapter is needed; the card seats directly in the larger slot. Riser adapters exist for physical orientation use cases, not electrical compatibility issues.

---

### Question7

Which of the following best describes the function of the CMOS clear jumper on a motherboard?

- A) It resets the CPU clock speed to its factory default when the system overheats
- B) It discharges static electricity from the CPU socket before a processor is installed
- C) It resets all BIOS/UEFI settings to factory defaults, including clearing passwords and custom configurations
- D) It enables legacy BIOS mode by disabling UEFI firmware during POST

Correct Answer: C — Moving the CMOS clear jumper to the clear position (pins 2–3) and back drains the CMOS memory, restoring all BIOS/UEFI settings — including passwords, boot order, and overclocking profiles — to factory defaults.

Distractor Analysis:

- Why A is incorrect: CPU clock speed during overheating is managed by thermal throttling logic in the CPU itself, not by a jumper on the board.
- Why B is incorrect: ESD protection involves wrist straps and anti-static mats, not a board jumper. The CMOS clear jumper has no ESD function.
- Why D is incorrect: Switching between UEFI and legacy BIOS mode is configured inside the UEFI firmware settings menu, not via a physical jumper.

---

### Question8

A technician connects the 24-pin ATX power cable from the PSU to the motherboard, but the system shuts down after about one second without POSTing. Which omission most likely caused this?

- A) The SATA data cables were not connected to the storage drives
- B) The 4-pin or 8-pin CPU EPS power connector was not connected
- C) The front panel USB header was not connected
- D) The I/O shield was not installed before the motherboard was seated

Correct Answer: B — The 4-pin or 8-pin EPS CPU power connector supplies dedicated power to the CPU's voltage regulator module. Without it the CPU receives no power and the system shuts down immediately without POSTing.

Distractor Analysis:

- Why A is incorrect: Unconnected SATA cables mean the system cannot access drives, but it will still POST and reach the boot device selection stage; it does not cause an immediate shutdown.
- Why C is incorrect: A missing front panel USB header disables those USB ports but has no effect on system boot or POST.
- Why D is incorrect: A missing I/O shield is a best-practice issue but has no effect on whether the system powers on or POSTs.

---

### Question9

What is the key difference between BIOS and UEFI most relevant to modern hardware technicians?

- A) BIOS supports larger hard drives (over 2 TB) while UEFI is limited to drives under 2 TB
- B) UEFI replaces legacy BIOS and adds support for drives over 2 TB (GPT), Secure Boot, and faster initialization
- C) BIOS and UEFI are interchangeable terms for the same firmware; the difference is only marketing
- D) UEFI is only available on AMD platforms; BIOS is used exclusively on Intel platforms

Correct Answer: B — UEFI is the modern firmware standard that supersedes legacy BIOS. Key additions include GPT partition support for drives over 2 TB, Secure Boot to prevent unauthorized bootloaders, a graphical setup interface, and faster POST times.

Distractor Analysis:

- Why A is incorrect: This reverses the relationship; legacy BIOS is limited to MBR partitioning (2 TB maximum), while UEFI with GPT handles much larger drives.
- Why C is incorrect: BIOS and UEFI are functionally different firmware standards with meaningful technical distinctions; they are not interchangeable terms.
- Why D is incorrect: UEFI is the standard for all modern platforms from both Intel and AMD; it is not exclusive to either vendor.

---

### Question10

A technician is installing a new Micro-ATX motherboard into a customer's existing full-size ATX mid-tower case. Which statement is correct?

- A) The installation will fail because Micro-ATX boards require a dedicated Micro-ATX case
- B) The installation will succeed because Micro-ATX boards are backward-compatible with ATX cases
- C) The installation will succeed only if a mounting plate adapter is purchased separately
- D) The installation will fail because the 24-pin ATX power connector from the PSU will not fit a Micro-ATX board

Correct Answer: B — The ATX case standard includes mounting holes for both ATX and Micro-ATX boards. No adapter is required; the board seats directly using the existing standoffs, and both form factors use the identical 24-pin ATX power connector.

Distractor Analysis:

- Why A is incorrect: Micro-ATX boards are specifically designed to be backward-compatible with ATX cases; a dedicated mATX case is an option but not a requirement.
- Why C is incorrect: No mounting adapter is needed; ATX cases natively include mATX-compatible standoff positions as part of the ATX specification.
- Why D is incorrect: ATX and Micro-ATX boards use the same 24-pin ATX main power connector. The form factor size difference does not change the power connector standard.
