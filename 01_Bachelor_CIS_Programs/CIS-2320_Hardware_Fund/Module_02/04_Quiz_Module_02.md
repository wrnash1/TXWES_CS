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

---

### Question 11

A motherboard manufacturer releases a new Z790 chipset board with an LGA1700 socket. A technician wants to install an older 10th-generation Intel CPU (also LGA1200 socket). Why will this not work?

- A) The LGA1700 socket has more pins than the LGA1200, making the CPU physically incompatible
- B) Z790 chipsets require DDR5 RAM, which overloads the 10th-gen CPU's memory controller
- C) 10th-generation Intel CPUs require USB 2.0 headers, which Z790 boards have removed
- D) The CMOS battery must be upgraded before installing older CPUs

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* LGA1700 and LGA1200 are different physical sockets — they have different pin counts and different CPU footprints. A 10th-gen CPU with an LGA1200 interface will not physically fit or make contact with an LGA1700 socket. The socket physically determines which CPU generations are compatible, along with chipset firmware support.
- *Why B is incorrect:* DDR5 support is determined by the CPU's memory controller and the board's memory slot type, but this does not prevent a CPU from being installed — it would be a compatibility issue if the RAM type mismatched, but the CPU physical incompatibility is the primary issue here.
- *Why C is incorrect:* USB header availability has no bearing on CPU installation or socket compatibility.
- *Why D is incorrect:* The CMOS battery is unrelated to CPU socket compatibility. It stores BIOS settings and has no role in determining which CPU generations are supported.

---

### Question 12

What is the purpose of the I/O shield that ships with a new motherboard?

- A) It insulates the motherboard's rear edge connectors from static discharge in transport
- B) It snaps into the case rear panel cutout and covers gaps around the motherboard's rear port cluster
- C) It provides a grounding path from the motherboard's rear I/O ports to the PC chassis
- D) It acts as a thermal barrier between the rear I/O area and the PSU fan exhaust

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The I/O shield is a stamped metal plate that installs in the rectangular cutout at the rear of the PC case before the motherboard is seated. It covers the gaps around the USB, audio, video, and network ports on the motherboard's rear I/O panel, preventing dust ingress and providing a clean finish. It must be installed before the board is seated — forgetting it requires removing the board.
- *Why A is incorrect:* The I/O shield is not part of anti-static packaging. ESD protection during transport uses anti-static bags, not the I/O shield.
- *Why C is incorrect:* The I/O shield does provide some incidental electrical contact with the chassis, but its grounding function is not its primary purpose. The motherboard grounds through its mounting standoffs.
- *Why D is incorrect:* The I/O shield is at the opposite end of the case from most PSUs. It provides no thermal barrier function and is not positioned between the PSU and the I/O area in most ATX layouts.

---

### Question 13

A technician is examining a motherboard and notices that one PCIe x16 slot is labeled "x16 (x4 mode)" in the documentation. What does this mean?

- A) The slot physically accepts x16 cards but electrically provides only four PCIe lanes
- B) The slot operates at PCIe generation 4 speeds and cannot be downgraded
- C) The slot requires four separate PCIe cards to be installed simultaneously
- D) The slot is wired for x4 NVMe only and will reject standard GPU cards

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* A PCIe slot can be physically sized as x16 (long) but have fewer lanes electrically connected on the motherboard. This is a common cost-saving measure on Micro-ATX and budget ATX boards — the second x16 slot gets only four physical lanes from the chipset. A GPU installed here will work but at reduced bandwidth, which may limit performance in bandwidth-sensitive applications.
- *Why B is incorrect:* "x4 mode" refers to lane count, not PCIe generation. Generation (3.0, 4.0, 5.0) is a separate characteristic from the number of lanes.
- *Why C is incorrect:* A single PCIe x16-sized card installs in the slot. The lane count determines bandwidth — it does not require multiple cards.
- *Why D is incorrect:* There is no restriction preventing a GPU from being installed in a physical x16 slot running at x4 electrical bandwidth. The GPU will operate normally but with reduced bandwidth, which may not matter for most mid-range cards.

---

### Question 14

Which of the following is a feature of UEFI firmware that is NOT available in legacy BIOS?

- A) POST (Power-On Self-Test) hardware initialization
- B) Configurable boot order
- C) Secure Boot to verify bootloader digital signatures
- D) Display of system temperature and fan speeds

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Secure Boot is a UEFI-exclusive feature. It verifies that the bootloader and operating system are digitally signed and unmodified before handing off execution. Legacy BIOS has no signature verification mechanism and cannot support Secure Boot.
- *Why A is incorrect:* POST (Power-On Self-Test) is performed by both legacy BIOS and UEFI. It is a fundamental part of firmware operation that predates UEFI.
- *Why B is incorrect:* Configurable boot order has existed in legacy BIOS since early PC design. UEFI provides a more sophisticated boot manager, but the concept of a user-configurable boot sequence is not exclusive to UEFI.
- *Why D is incorrect:* System temperature and fan speed monitoring in firmware setup screens was available in legacy BIOS on boards with hardware monitoring chips. UEFI often provides more detailed monitoring, but the basic feature is not UEFI-exclusive.

---

### Question 15

A Micro-ATX build is being assembled in a Micro-ATX case. The technician installs the motherboard and then tries to attach the I/O shield. Why does the shield not fit?

- A) Micro-ATX cases do not use I/O shields; they use a pre-punched rear panel
- B) The I/O shield must be installed in the case before the motherboard is seated — it cannot be installed afterward
- C) Micro-ATX I/O shields are incompatible with ATX-sized shields and must be ordered separately
- D) The I/O shield is optional on Micro-ATX boards and can be discarded

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The I/O shield snaps into the case's rear I/O cutout from the inside. Once the motherboard is seated over it, there is no way to insert the shield without removing the board first. This is a common assembly error that the A+ exam tests procedurally.
- *Why A is incorrect:* Micro-ATX cases do use I/O shields. The rear I/O cutout is a standard rectangular opening that requires the shield to cover unused space around the port cluster.
- *Why C is incorrect:* The I/O shield ships with the motherboard and is specific to that board's port layout. It is not an ATX vs. Micro-ATX sizing issue — the case cutout is the same shape for both form factors.
- *Why D is incorrect:* While the system will still function without the I/O shield, it is not "optional" in professional practice. Missing shields leave large gaps that allow dust ingress and are flagged in quality inspections.

---

### Question 16

What is the Northbridge and why is it no longer present as a separate chip in modern systems?

- A) The Northbridge was a dedicated sound processing chip; its functions were moved to the CPU's integrated audio engine
- B) The Northbridge managed high-speed connections (CPU, RAM, PCIe); its functions were integrated into the CPU die in modern platforms
- C) The Northbridge was an older term for the CMOS battery holder; it was renamed PCH in modern terminology
- D) The Northbridge managed legacy USB and SATA ports; these were moved to the Southbridge which became the PCH

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In the classic hub architecture, the Northbridge handled the CPU's fastest connections — RAM (via the Front Side Bus or HyperTransport), PCIe lanes for the GPU, and the link to the Southbridge. Starting with Intel Nehalem (2008) and AMD Phenom II, the memory controller was integrated directly into the CPU. PCIe lanes followed. By Intel Sandy Bridge (2011), the GPU and memory controller were entirely on-die, eliminating the need for a discrete Northbridge.
- *Why A is incorrect:* Audio processing was handled by the Southbridge's AC'97 or HDA audio controller, not the Northbridge. Modern CPUs do not have integrated audio engines — audio remains in the PCH/chipset or a discrete audio chip.
- *Why C is incorrect:* The Northbridge was a separate die, typically a 20–40mm² chip near the CPU socket. It has nothing to do with the CMOS battery holder.
- *Why D is incorrect:* USB and SATA were Southbridge functions. The Southbridge evolved into what is now called the PCH (Platform Controller Hub). The Northbridge's functions moved to the CPU — not to the Southbridge/PCH.

---

### Question 17

A student needs to install a Wi-Fi card, a dedicated GPU, and a capture card in a new build. The ATX motherboard has the following open slots: one PCIe x16, two PCIe x1, and one PCIe x4. Which assignment is MOST appropriate?

- A) GPU in x16, Wi-Fi in x1, capture card in x4
- B) GPU in x4, Wi-Fi in x16, capture card in x1
- C) GPU in x1, Wi-Fi in x4, capture card in x16
- D) GPU in x16, Wi-Fi in x4, capture card in x1

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The GPU requires the x16 slot for maximum bandwidth. The Wi-Fi card is typically an x1 PCIe card and fits in an x1 slot. A capture card is typically an x1 or x4 card and functions well in the x4 slot. This assignment places each card in the smallest slot that meets or exceeds its requirements, preserving higher-bandwidth slots for bandwidth-hungry devices.
- *Why B is incorrect:* A GPU installed in an x4 slot will physically fit (if the slot is open-ended) but would be severely bandwidth-limited. A Wi-Fi card installed in an x16 slot wastes the slot's bandwidth but would technically work — however, this is not the optimal or exam-correct assignment.
- *Why C is incorrect:* A full-length GPU will not physically fit in a PCIe x1 slot. This assignment is physically impossible.
- *Why D is incorrect:* Placing the Wi-Fi card in the x4 slot and the capture card in the x1 slot works technically (a smaller card fits in a larger slot), but Answer A is a better assignment because it puts the capture card in the x4 slot where it has more headroom for data-intensive captures.

---

### Question 18

Which of the following correctly describes the relationship between PCIe generations in terms of backward compatibility?

- A) PCIe 4.0 cards will not function in PCIe 3.0 slots because they require higher voltage
- B) PCIe 5.0 slots only accept PCIe 5.0 cards; older cards must use a legacy PCIe adapter
- C) PCIe generations are backward and forward compatible; a card and slot of different generations negotiate to the lower generation's speed
- D) PCIe 3.0 and 4.0 use different physical connector shapes and are not interchangeable

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* PCIe generations share the same physical connector and pinout. When a card and slot are different generations, they negotiate the link speed down to the lower generation. A PCIe 4.0 NVMe drive in a PCIe 3.0 M.2 slot operates at PCIe 3.0 speeds — it works, just not at full speed. This cross-generation compatibility is by design and is tested on the A+ exam.
- *Why A is incorrect:* PCIe does not use different voltage levels between generations. All generations operate on the same 3.3V and 12V power rails. Voltage is not the differentiating factor.
- *Why B is incorrect:* PCIe 5.0 slots accept all prior-generation cards. The backward compatibility principle applies across all PCIe generations, including 5.0.
- *Why D is incorrect:* PCIe generations all use the same physical connector design. The number of lanes determines physical slot size; the generation determines electrical bandwidth per lane. There is no difference in connector shape between PCIe 3.0, 4.0, and 5.0.

---

### Question 19

A technician is building a low-power home server using a Mini-ITX motherboard. After completing the build, they realize the case has only one rear expansion slot opening. What physical limitation does this confirm about Mini-ITX builds?

- A) Mini-ITX systems cannot use discrete GPUs because the PCIe x16 slot is not included on Mini-ITX boards
- B) Mini-ITX boards typically provide only one PCIe expansion slot, limiting add-on card options to a single card
- C) Mini-ITX cases only support half-height expansion cards
- D) Mini-ITX systems are limited to x1 PCIe slots due to chipset bandwidth restrictions

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Mini-ITX boards include exactly one PCIe x16 slot in the standard design. This single slot is usually wired for GPU use. The one rear bracket opening in a Mini-ITX case corresponds to this single expansion slot. Adding a second card requires external PCIe extenders, which are not standard configurations.
- *Why A is incorrect:* Mini-ITX boards do include a PCIe x16 slot. They can use discrete GPUs — many Mini-ITX gaming builds use high-end GPUs. The limitation is in the total number of expansion slots, not the absence of an x16 slot.
- *Why C is incorrect:* Mini-ITX cases come in different heights and can support full-height cards if the case is designed for them. Some compact builds use low-profile cards, but this is a case design choice, not a Mini-ITX standard requirement.
- *Why D is incorrect:* The PCIe x16 slot on a Mini-ITX board is wired to the CPU's PCIe lanes, not chipset lanes, and operates at full x16 bandwidth. The chipset bandwidth limitation applies to additional slots when they exist, not to the primary GPU slot.

---

### Question 20

A technician is upgrading an office PC and considers replacing the ATX motherboard with a Micro-ATX board. The existing case is a standard ATX mid-tower with nine standoff positions. After installing the Micro-ATX board, the technician notices three standoff holes on the board do not align with any standoff in the case. What should the technician do?

- A) Add screws through the unmatched holes anyway to provide additional support
- B) Only install screws where the motherboard holes align with case standoffs; leave unmatched standoff positions empty
- C) Install additional standoffs in the case wherever the board has unmatched holes
- D) Return the Micro-ATX board because it is not compatible with the ATX case

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* When mounting a smaller board (Micro-ATX) in a larger case (ATX), only the standoff positions that align with the board's mounting holes are used. The remaining case standoff holes are simply left empty. Forcing screws through misaligned positions or adding standoffs where there are no corresponding board holes would stress the PCB and potentially crack it or cause short circuits.
- *Why A is incorrect:* Adding screws through board holes that do not line up with case standoffs would either mean drilling new case holes (not appropriate) or bending the board to reach a standoff — both of which can damage the motherboard PCB.
- *Why C is incorrect:* Installing standoffs where the board has no corresponding holes would press against the board's PCB surface and potentially short out traces on the back of the board. Never add standoffs that do not correspond to motherboard mounting holes.
- *Why D is incorrect:* Micro-ATX boards are designed to be compatible with ATX cases. The unused standoff positions in an ATX case are expected when a smaller board is installed. Compatibility is confirmed, not denied.
