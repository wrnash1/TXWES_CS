# Quiz: Module 13 - Laptop Components and Disassembly

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 1.3
**Texas Wesleyan University | Professor Nash**
**Total Questions: 10 | Points: 10 (1 point each)**

---

## Questions

### Question 1

Why must you carefully disconnect laptop antenna wires using a spudger rather than pulling the cable when swapping a Wi-Fi card?

- A) The antenna wires carry high-voltage current that can cause electric shock if the cable insulation is damaged during removal
- B) The antenna wires supply power to the LCD backlight, and pulling them can interrupt the backlight circuit and crack the display panel
- C) The antenna wires are fragile coaxial cables with tiny MHF4 snap-on connectors; pulling the cable rather than prying the connector body can separate the cable from the connector or tear the antenna trace in the bezel
- D) The antenna wires are permanently fused to the Wi-Fi card and cannot be removed without desoldering; attempting to pull them will rip pads off the card's PCB

Correct Answer: C

- Why C is correct: Laptop Wi-Fi antenna cables use MHF4 coaxial connectors that snap onto pins on the Wi-Fi card. The cable is extremely thin — the outer braid can separate from the connector body if the cable is pulled. The correct technique is to insert a non-conductive spudger under the connector body and pry it straight up. Pulling the cable risks a torn connector that would require replacing the entire antenna assembly routed through the hinge and lid.
- Why A is incorrect: Antenna cables carry low-power RF signals, not high-voltage current. They pose no electrical shock hazard. ESD precautions (wrist strap, grounded mat) are the relevant safety concern.
- Why B is incorrect: The display backlight is powered through a separate circuit from the motherboard's backlight driver. Antenna cables are coaxial RF cables with no connection to the backlight power circuit.
- Why D is incorrect: Antenna cables are not permanently fused to the Wi-Fi card. They are designed to be disconnected and reconnected — that is the entire purpose of the snap-on MHF4 connector. No desoldering is involved.

---

### Question 2

Which of the following most accurately describes the LCD screen replacement procedure on a modern laptop?

- A) A repair procedure requiring removal of the display bezel, disconnection of the LVDS or eDP video cable (and digitizer flex cable on touchscreen models), and careful separation of the panel from the lid assembly — all bezel clips, retaining screws, and flex cables must be handled carefully to avoid cracking the panel or damaging connectors.
- B) A repair that requires only removing the single retaining screw on the back of the display lid and sliding the LCD panel out of the chassis, as all laptop displays use a universal HDMI connector that unplugs with no additional cable routing.
- C) A procedure exclusive to CCFL-backlit displays manufactured before 2012; modern LED-backlit laptop displays are fused to the chassis and cannot be replaced without replacing the entire laptop.
- D) A straightforward swap identical to replacing a desktop monitor, where the display detaches via a standard DisplayPort cable and requires no disassembly of the lid assembly or bezel.

Correct Answer: A

- Why A is correct: This accurately describes the complexity of laptop LCD replacement. Bezel removal (screws under rubber plugs, plastic clips), video cable disconnection (LVDS or eDP), and careful handling of all flex cables and hinges are all required steps. Touchscreen models add a digitizer flex cable. The A+ exam tests this procedure and its required caution at each step.
- Why B is incorrect: Laptop displays do not use internal HDMI connectors. They use LVDS (older) or eDP (modern) flat flex cables that route through the hinge assembly and require full bezel disassembly to access. There is no single retaining screw that releases the panel without further disassembly.
- Why C is incorrect: LED-backlit laptop display panels are absolutely user-replaceable. This is a tested A+ repair procedure. Claiming they are permanently fused is factually incorrect.
- Why D is incorrect: Laptop displays are integrated into the lid assembly and are not comparable to external desktop monitors that connect via external cables. Internal disassembly of the bezel and lid is always required.

---

### Question 3

A technician needs to replace a laptop's internal Wi-Fi card. After removing the battery and back panel, the technician finds two thin cables attached to the card labeled "Main" and "Aux." What are these cables, and what is the correct procedure for removing them?

- A) These are the SATA data cables for the internal SSD; they should be unplugged by gripping the cable firmly and pulling straight back with moderate force
- B) These are the wireless antenna coaxial cables routed from the LCD bezel; they should be disconnected by gently prying each snap-on connector off the card using a non-conductive spudger, not by pulling the cable itself
- C) These are the display backlight power cables; they must be cut with scissors and resoldered to the replacement card because they are permanently bonded to the Wi-Fi module
- D) These are USB data cables connecting the Wi-Fi card to the motherboard's USB controller; they unplug by pressing the release tab on each connector and pulling straight up

Correct Answer: B

- Why B is correct: Laptop Wi-Fi cards use MHF4 snap-on coaxial connectors for the antenna leads. The cables route from the card through the hinge assembly to antenna films in the LCD bezel. Removing them requires prying the connector body off the card pin with a spudger — pulling the cable risks separating the cable from the connector. The cables are reused with the replacement card.
- Why A is incorrect: SATA data cables use a completely different connector type and are not present on a Wi-Fi card. Wi-Fi cards use M.2 or Mini-PCIe slots, not SATA.
- Why C is incorrect: Antenna cables are a separate circuit from the backlight. They are never cut. They are designed to be disconnected from one Wi-Fi card and reconnected to the replacement by pressing the connectors back onto the new card's antenna pins.
- Why D is incorrect: Laptop Wi-Fi antenna connectors are coaxial RF connections, not USB connectors. They have no release tab and are removed by prying the connector body, not pressing a tab.

---

### Question 4

A user reports that their laptop charges intermittently — sometimes charging normally, sometimes showing no charge even with the AC adapter plugged in. The issue seems related to the angle at which the power cable sits in the port. Which component is most likely failing?

- A) The laptop battery — lithium-ion batteries develop internal cell failures that cause them to accept charge only when held at specific physical orientations
- B) The DC power jack — a damaged or loose power jack creates an intermittent electrical connection that breaks when the connector shifts, causing inconsistent charging behavior dependent on cable angle
- C) The AC adapter — the adapter's internal transformer overheats and throttles power output based on the cable routing angle to prevent damage to the internal windings
- D) The voltage regulator on the motherboard — regulators fail progressively and accept input power only within a narrow tolerance range that varies depending on connector position

Correct Answer: B

- Why B is correct: The angle-dependent charging symptom is the definitive indicator of a physically damaged or loose DC power jack. The barrel connector makes intermittent contact inside a cracked or worn jack housing. When the connector shifts due to cable angle, the contact opens or closes — which directly causes the charging state to change.
- Why A is incorrect: Battery cell failures cause capacity loss, abnormally fast discharge, or complete failure to hold a charge. Batteries do not respond to physical orientation changes in the way described; lithium-ion cells are not position-sensitive.
- Why C is incorrect: AC adapters deliver a regulated fixed voltage output regardless of how the cable is routed externally. Thermal throttling is not a feature of laptop AC adapters, and no adapter adjusts its output based on the angle of the cable at the barrel connector.
- Why D is incorrect: A failing voltage regulator would produce consistent power delivery problems or cause system instability under load. The distinguishing feature of the described symptom — positional variation at the input connector — points to the physical jack, not to downstream power regulation.

---

### Question 5

Before performing any internal service on a laptop — including replacing the keyboard, Wi-Fi card, or RAM — what is the mandatory first step a technician must always perform?

- A) Update the BIOS/UEFI firmware to the latest version to ensure the replacement component is recognized correctly after reinstallation
- B) Disconnect or remove the battery (and unplug the AC adapter) to eliminate all power from the system before touching any internal components
- C) Run a full virus scan on the laptop to ensure no malware interferes with hardware detection after the repair is complete
- D) Connect the laptop to an ESD mat but leave the battery installed so the mat has a complete ground path through the system's power circuit

Correct Answer: B

- Why B is correct: Disconnecting the battery is the first and most critical step in all laptop internal service. It removes residual power that could cause short circuits, damage components, or injure the technician. The AC adapter must also be unplugged before battery removal. This rule applies to every internal laptop component replacement without exception.
- Why A is incorrect: BIOS firmware updates are a software maintenance task performed before or after physical service, not as a prerequisite to disassembly. Updating firmware has no bearing on safe physical handling of internal components.
- Why C is incorrect: A virus scan is a software security procedure with no relevance to safe physical disassembly. Malware does not affect hardware recognition in the manner implied and is never a step in any hardware repair workflow.
- Why D is incorrect: The battery must be removed before internal service regardless of ESD mat grounding. Leaving the battery connected while the ESD mat is attached does not improve protection — it defeats the entire purpose of removing power, because powered components can still be damaged by electrical discharge or short circuits.

---

### Question 6

A technician is replacing a laptop keyboard and finds the keyboard flex cable connected to a small connector on the motherboard. When the technician attempts to slide the cable out, it will not move and appears locked in place. What is the correct next action?

- A) Grip the flex cable with needle-nose pliers and pull with increased force until the cable releases from the connector
- B) Locate the small rotating lock bar on the ZIF connector, flip it to the open position using a spudger or fingernail, then slide the cable out with no force
- C) Apply a small amount of isopropyl alcohol to the connector as a lubricant, then slide the cable out while the alcohol is still wet
- D) Cut the old flex cable at the connector so the keyboard can be removed, then order a replacement flex cable along with the replacement keyboard

Correct Answer: B

- Why B is correct: A ZIF (Zero Insertion Force) connector holds flex cables with a rotating lock bar. When the lock bar is in the closed position, the cable is clamped and cannot be removed without damage. Flipping the lock bar to the open position (typically 90 degrees) releases the clamp completely, allowing the cable to slide out with essentially zero resistance.
- Why A is incorrect: Pulling a flex cable with pliers while the ZIF lock is closed will tear the cable or snap off the lock bar. Increased force is never the correct approach with a ZIF connector.
- Why C is incorrect: Isopropyl alcohol provides no useful lubrication for a ZIF connector and could damage the connector contacts or leave residue. The resistance is caused by the mechanical lock, not friction, and cannot be addressed with lubricant.
- Why D is incorrect: Cutting the cable is destructive and unnecessary. ZIF connectors are designed for repeated cable insertion and removal. Cutting the cable would require purchasing an additional component and cause unnecessary repair cost.

---

### Question 7

A customer wants to upgrade the RAM in their laptop from 8 GB to 16 GB. The technician opens the service manual and finds the note: "Memory: 8 GB LPDDR4 soldered to system board; not user serviceable." What does this mean for the upgrade request?

- A) The RAM is soldered directly to the motherboard in a BGA package and cannot be removed, replaced, or upgraded without replacing the entire system board; the customer's upgrade is not possible on this laptop
- B) The RAM requires a specialized soldering station available at any electronics store; the technician can upgrade it in approximately 30 minutes by desoldering the existing chips and soldering new ones in their place
- C) Soldered RAM is actually more reliable than socketed SO-DIMM; the technician can still upgrade by adding a second SO-DIMM module in the empty secondary slot that is present on all soldered-RAM laptops
- D) The note means the RAM is permanently set to 8 GB by the BIOS; the technician can upgrade it by flashing a modified BIOS that removes the 8 GB memory limit

Correct Answer: A

- Why A is correct: Soldered RAM — labeled LPDDR4 or LPDDR5 in service manuals — is permanently mounted to the motherboard using Ball Grid Array (BGA) packaging. There are no SO-DIMM slots. A professional reball/reflow operation is technically possible but is beyond A+ scope, is cost-prohibitive, and voids any remaining warranty. For the purposes of this course and the A+ exam, soldered RAM is not upgradeable.
- Why B is incorrect: BGA desoldering and resoldering requires specialized rework stations costing thousands of dollars, precise temperature profiles, and X-ray inspection equipment. It is not available at general electronics stores and is not a realistic field repair option.
- Why C is incorrect: Laptops with soldered RAM do not have empty SO-DIMM slots alongside the soldered chips. The design uses one or the other — not both. Soldered-RAM laptops have no user-accessible memory slots.
- Why D is incorrect: RAM capacity is determined by the physical memory chips installed, not by a BIOS limit. A BIOS flash cannot create physical RAM that does not exist. The BIOS only recognizes memory that is physically present.

---

### Question 8

Which RAM form factor is used in laptops, and how does it differ physically from the standard desktop RAM form factor?

- A) DIMM (Dual Inline Memory Module) — laptop RAM uses the same full-size DIMM form factor as desktop systems, but runs at a lower voltage to conserve battery life
- B) SO-DIMM (Small Outline DIMM) — laptop RAM is approximately half the physical length of a desktop DIMM, uses a different pin count, and seats at an angle rather than vertically in its slot
- C) RIMM (Rambus Inline Memory Module) — laptop RAM uses RIMM technology that allows multiple modules to be daisy-chained together for maximum bandwidth
- D) MicroDIMM — all laptops use the MicroDIMM form factor, which is one-quarter the size of a desktop DIMM and uses a proprietary 144-pin connector regardless of DDR generation

Correct Answer: B

- Why B is correct: Laptop RAM uses the SO-DIMM (Small Outline Dual Inline Memory Module) form factor. A DDR4 SO-DIMM is approximately 67 mm long with 260 pins, compared to 133 mm and 288 pins for a DDR4 full-size DIMM. The SO-DIMM seats at an angle (typically 30–45 degrees) and is retained by two spring clips on the sides of the slot.
- Why A is incorrect: Laptop RAM does not use the full-size DIMM form factor. A full-size DIMM physically cannot fit in a laptop SO-DIMM slot. The voltage difference (1.2 V for DDR4 in both form factors) is the same; lower voltage is not the distinguishing factor between the form factors.
- Why C is incorrect: RIMM was a proprietary Rambus memory standard from the early 2000s that is entirely obsolete. It has not been used in any mainstream laptop or desktop system for over two decades.
- Why D is incorrect: MicroDIMM is a niche form factor used in some ultra-compact embedded systems. It is not the standard laptop RAM form factor and is not tested on the A+ Core 1 exam. Modern laptop RAM is SO-DIMM without exception.

---

### Question 9

An older laptop has a dim display — the image is faintly visible when a flashlight is shone at the screen, but the built-in display produces almost no visible light on its own. The laptop was manufactured in 2007. Which component has most likely failed, and what additional component specific to this era of laptop is also a potential failure point?

- A) The LCD panel glass has delaminated from the display housing; a second potential failure is the eDP video cable which frays internally when the lid is opened and closed repeatedly
- B) The CCFL backlight tube has failed or dimmed; a second potential failure point is the inverter board, which generates the high-voltage AC signal required to power the CCFL tube
- C) The LED backlight driver circuit has burned out; a second potential failure is the display's digitizer layer, which drains power from the backlight when touch input is detected
- D) The screen's anti-glare coating has degraded; a second potential failure is the eDP connector on the motherboard, which corrodes in older laptops and reduces backlight current

Correct Answer: B

- Why B is correct: A 2007 laptop uses CCFL (Cold Cathode Fluorescent Lamp) backlighting. The symptom — image visible under flashlight but no self-illumination — is the classic CCFL failure presentation. CCFL lamps require a high-voltage AC inverter board to operate. Both the CCFL tube and the inverter board are failure points: the CCFL tube itself can dim or fail, and the inverter board can fail and produce no output, causing the same dark-screen symptom.
- Why A is incorrect: A 2007 laptop would not use eDP — that standard was introduced around 2012. LCD panel delamination is a visible physical defect, not the cause of a uniformly dark screen with a still-visible image.
- Why C is incorrect: A 2007 laptop uses CCFL, not LED backlighting. LED backlighting became standard in laptop displays after approximately 2010. The digitizer layer is present only on touchscreen models, which were rare in 2007.
- Why D is incorrect: Anti-glare coating degradation causes visual haze or reduced contrast, not a dark screen. Anti-glare coating is a surface treatment, not a power circuit, and its degradation does not eliminate backlight output.

---

### Question 10

A technician successfully replaces a laptop's LCD panel and begins reassembling the display assembly. Before clipping the bezel back into place, what action should the technician take, and why?

- A) Apply a thin bead of adhesive sealant around the perimeter of the panel to permanently bond it to the lid frame, ensuring it does not shift during normal use
- B) Power on the laptop and verify the new display produces a correct image before closing the bezel, because re-opening the bezel after full reassembly requires repeating the entire bezel removal process if a connection issue is found
- C) Install the drivers for the new display panel from the manufacturer's website before powering on, because the operating system will not output a signal to an unrecognized panel without the correct driver installed
- D) Wrap the exposed video cable in electrical tape where it passes through the hinge to prevent the cable from causing the display to flicker when the lid is opened and closed

Correct Answer: B

- Why B is correct: Powering on with the panel connected but the bezel not yet installed allows the technician to verify the display connection before committing to the full reassembly. If the image is incorrect, missing, or shows artifacts, the video cable connection or panel seating can be corrected at this stage without removing the bezel a second time. This is a standard best practice for any display replacement.
- Why A is incorrect: LCD panels are not adhesive-sealed. They are held by retaining screws and brackets. Applying adhesive sealant would prevent future service, trap heat, and is not a recognized procedure for any laptop display installation.
- Why C is incorrect: Modern operating systems (Windows 10/11, macOS) do not require a separate driver installation for a replacement LCD panel of the same type. The display interface (eDP or LVDS) is handled by the integrated graphics driver already present in the system. The panel will output an image immediately after connection without any additional driver steps.
- Why D is incorrect: Electrical tape is not an appropriate material for protecting the video cable in the hinge. The hinge area is precisely engineered, and adding tape bulk can prevent the hinge from seating correctly or cause cable pinching. The video cable is already routed and protected by the hinge mechanism's design.

---

### Question 11

A technician is upgrading the RAM in a laptop. The laptop's service manual specifies SO-DIMM DDR4-3200. The technician has a spare stick of desktop DDR4-3200 RAM available. Can this stick be used?

- A) Yes — DDR4-3200 is DDR4-3200 regardless of physical form factor; the desktop DIMM will fit in the laptop's SO-DIMM slot with a standard adapter
- B) No — desktop RAM uses full-size DIMM modules (typically 288 pins) while laptop RAM uses SO-DIMM modules (typically 260 pins for DDR4); these are different physical sizes and pin counts and are not interchangeable even with an adapter
- C) Yes — SO-DIMM and full-size DIMM share identical dimensions; the only difference is the label, which is a marketing distinction applied by manufacturers
- D) No — desktop DDR4 operates at 1.5V while laptop DDR4 (SO-DIMM) operates at 1.35V; using the higher-voltage desktop RAM will damage the laptop's memory controller permanently

Correct Answer: B

- Why B is correct: SO-DIMM (Small Outline DIMM) modules used in laptops are physically smaller (67.6mm long) and have 260 pins for DDR4, compared to full-size DIMMs (133.35mm long, 288 pins for DDR4 desktop). They cannot be physically inserted into each other's slots, and no passive adapter exists to make them compatible. The correct replacement must be a DDR4 SO-DIMM module.
- Why A is incorrect: No standard adapter exists that allows a full-size DIMM to be used in a SO-DIMM slot. Even if such an adapter were created, the physical dimensions of the DIMM would not fit within a laptop's chassis.
- Why C is incorrect: SO-DIMM and DIMM are physically distinct module formats with different PCB dimensions, different notch positions, and different pin counts. The size and pin differences are real hardware differences, not marketing labels.
- Why D is incorrect: Both desktop DDR4 DIMMs and laptop DDR4 SO-DIMMs operate at the same 1.2V standard voltage (DDR4 standard). While DDR3L (low-voltage) runs at 1.35V compared to standard DDR3's 1.5V, no such voltage difference exists between SO-DIMM and DIMM variants of DDR4 at the same speed grade.

---

### Question 12

During a laptop keyboard replacement, a technician notices that the new keyboard's ribbon cable is 0.5 mm narrower than the original cable but the number of conductors is the same. The technician forces the ribbon cable into the ZIF (Zero Insertion Force) connector. After assembly, several keys in the middle of the keyboard do not respond. What is the most likely cause?

- A) The keyboard firmware requires a reset procedure after replacement; the non-responsive keys are in sleep mode and will activate after the first system reboot
- B) The mismatched ribbon cable width caused some conductors to misalign with the ZIF connector contacts, resulting in intermittent or open connections to the affected key matrix rows or columns
- C) The operating system's keyboard driver cached the old keyboard's hardware ID; uninstalling and reinstalling the keyboard driver will restore full key functionality
- D) The keyboard controller chip on the motherboard was damaged by ESD during the replacement because no wrist strap was used, and the non-responsive keys indicate partial controller failure

Correct Answer: B

- Why B is correct: ZIF connectors rely on the ribbon cable making precise contact with each conductor pad in the connector housing. A cable that is a different width will misalign the conductor traces relative to the connector contacts, leaving some conductors making partial or no contact. The specific keys affected correspond to the matrix rows or columns whose conductors are misaligned.
- Why A is incorrect: Laptop keyboards do not have independent firmware or sleep modes for individual keys. Key responsiveness is determined entirely by the physical electrical contact between the ribbon cable conductors and the controller.
- Why C is incorrect: The keyboard driver communicates with the keyboard controller via HID (Human Interface Device) protocol. The driver does not cache per-key hardware IDs, and key matrix scanning is a hardware function independent of driver state.
- Why D is incorrect: ESD damage to the keyboard controller would more likely result in complete keyboard failure or random key generation rather than a consistent pattern of non-responsive keys aligned with a physical misalignment. The root cause described (mismatched cable width) directly explains the symptom pattern.

---

### Question 13

A laptop that is three years old can no longer hold a charge for more than 45 minutes despite the battery health indicator showing 78% capacity. The AC adapter is functioning correctly. Which of the following best explains the situation?

- A) The laptop's power management firmware is reporting an incorrect capacity; the battery is actually at 30% health, which is why runtime is so short despite the displayed percentage
- B) Lithium-ion battery capacity degrades as the number of charge cycles accumulates; at 78% capacity, the battery can only deliver 78% of its original energy storage, resulting in proportionally shorter runtime — a 4-hour original battery now provides approximately 3.1 hours (0.78 × 4h), and further degradation will continue
- C) The 45-minute runtime indicates a battery fault that is unrelated to health percentage; lithium-ion batteries should maintain full original runtime until they reach exactly 0% health
- D) The battery health indicator measures voltage, not capacity; a reading of 78% means the battery's maximum voltage has dropped to 78% of rated voltage, reducing current output and causing the shorter runtime

Correct Answer: B

- Why B is correct: Lithium-ion batteries degrade through charge cycles, each cycle causing a small reduction in maximum charge capacity. The battery health percentage reflects the ratio of current maximum capacity to original capacity. At 78%, the battery holds 78% of its original energy, resulting in 78% of the original runtime. This is expected and normal behavior for a three-year-old laptop battery. Replacement is appropriate when capacity drops below 50-60% depending on user needs.
- Why A is incorrect: While battery management system calibration errors exist, a displayed 78% capacity with only 45 minutes of runtime is plausible for many laptop batteries depending on their original runtime. Assuming the indicator is wrong is not the most likely explanation without additional evidence.
- Why C is incorrect: Lithium-ion battery capacity degrades continuously and gradually with each charge cycle. There is no "cliff" at 0% health — runtime shortens progressively as capacity decreases. The claim that batteries should maintain full runtime until exactly 0% health contradicts the known electrochemical degradation behavior of lithium-ion cells.
- Why D is incorrect: Battery health percentage in laptop management systems reflects charge capacity (mAh or Wh), not voltage. The nominal voltage of a lithium-ion cell remains relatively stable throughout most of its capacity range, dropping significantly only near depletion. Capacity and voltage are related but distinct measurements.

---

### Question 14

A technician removes a laptop's bottom cover and identifies a battery connected to the motherboard via a small multi-pin connector. The battery also has a thin adhesive strip holding it to the chassis. What is the correct procedure for removing the battery?

- A) Disconnect the battery connector from the motherboard first, then carefully lift the battery by inserting a spudger or plastic pry tool under the edge to release the adhesive — do not use metal tools that could puncture the battery pouch
- B) Remove the adhesive strip first by pulling sharply upward, then disconnect the battery connector — the order does not matter because disconnecting the connector last prevents the battery from discharging into the motherboard during removal
- C) Cut the battery connector cable with flush-cut pliers close to the battery to avoid disturbing the motherboard connector, then peel the battery out — the connector is replaceable and the cable cut allows safe removal
- D) Heat the battery with a heat gun at 150°C to soften the adhesive before attempting removal — this is the manufacturer-recommended procedure for adhesive-mounted laptop batteries

Correct Answer: A

- Why A is correct: The correct order is to disconnect the battery connector from the motherboard first (disconnecting power from the circuit before handling the battery), then use a plastic pry tool or spudger to gently work under the battery and release the adhesive. Plastic tools are critical because a metal tool puncturing the lithium-ion pouch can cause a thermal runaway reaction. This procedure is consistent with iFixit and manufacturer repair guides.
- Why B is incorrect: Pulling the adhesive strip sharply before disconnecting the connector increases the risk of damaging internal components if the battery shifts suddenly. The order should always be to electrically disconnect the battery first.
- Why C is incorrect: Cutting the battery cable is destructive and unnecessary. The connector is designed to be removed intact, and cutting the cable would require soldering a new connector — adding significant labor and cost to a standard battery replacement.
- Why D is incorrect: Applying 150°C heat directly to a lithium-ion battery is dangerous. While gentle heat (30-40°C from a heat pad or iOpener tool) can soften adhesive on glued batteries, excessive heat can cause thermal runaway in lithium cells. 150°C far exceeds safe handling temperatures for lithium-ion batteries.

---

### Question 15

A laptop is brought in for service with the complaint that the built-in webcam is not detected in Device Manager. The camera functioned correctly one week ago. No software or driver changes were made. What should the technician check first?

- A) Update Windows to the latest version, as Microsoft periodically removes camera driver support for older integrated webcams through Windows Update
- B) Check whether the webcam has a physical privacy shutter that has been accidentally slid to the closed position, which on some laptop models also disconnects the camera electrically rather than just blocking the optical path
- C) Replace the webcam module, as an integrated webcam that stops appearing in Device Manager has definitively failed and requires a hardware replacement
- D) Check the laptop's BIOS/UEFI settings — the webcam being absent from Device Manager always indicates the camera has been disabled in BIOS firmware and must be re-enabled there

Correct Answer: B

- Why B is correct: Many modern laptops have a physical webcam privacy shutter. On some models (particularly privacy-focused business laptops), sliding the shutter to the closed position also triggers a hardware disconnect that removes the device from Device Manager entirely. This is a commonly overlooked cause of sudden "camera not detected" reports and requires no disassembly to check.
- Why A is incorrect: Windows Update does not remove driver support for existing integrated webcams. Camera disappearance from Device Manager after a Windows Update is a documented issue in some cases, but the scenario states no software changes were made.
- Why C is incorrect: Jumping directly to hardware replacement without checking simpler causes violates the A+ troubleshooting methodology. The camera could be disabled in BIOS, have a loose internal connector, or have a hardware privacy switch in the off position — all of which are easier to check than replacing the module.
- Why D is incorrect: While BIOS/UEFI firmware can disable the webcam on some laptops, this is not the most common cause of sudden disappearance. Additionally, the BIOS setting typically requires deliberate user action to change. The physical privacy shutter is a more commonly encountered first cause that should be checked before accessing BIOS settings.

---

### Question 16

A technician needs to upgrade a laptop's storage from a 2.5-inch SATA SSD to an NVMe SSD. After checking the laptop's service manual, the technician confirms the laptop has a single M.2 slot. What two pieces of information are critical to verify before purchasing an NVMe M.2 SSD?

- A) The SSD's color and the laptop's total USB port count — color determines thermal compatibility and USB ports determine whether the SSD will enumerate correctly
- B) The M.2 slot key type (M-key or B+M-key) and the M.2 slot length (2242, 2260, or 2280) — the SSD must use the compatible key and physically fit within the slot's supported length
- C) The NVMe SSD's operating temperature range and the laptop's maximum processor TDP — the SSD will throttle if the CPU generates more heat than the SSD's rated maximum
- D) The SSD brand and the laptop brand — only same-brand SSDs are guaranteed compatible, as different manufacturers use proprietary M.2 slot connector pinouts

Correct Answer: B

- Why B is correct: M.2 slots have defined key types — M-key supports PCIe NVMe (and SATA), while B-key supports SATA only. The SSD must use a key that the slot accepts. The slot also has a physical length limit (most laptops support 2280, some support 2242 only) and the SSD module must fit. Purchasing a 2280 NVMe SSD for a slot that only supports 2242 length will result in a drive that cannot be fully seated or secured.
- Why A is incorrect: SSD color has no technical significance. USB port count has no relationship to M.2 NVMe storage installation or compatibility.
- Why C is incorrect: While NVMe SSDs do generate more heat than SATA SSDs, the operating temperature comparison to CPU TDP is not a standard compatibility criterion for storage selection. SSD thermal throttling is managed by the drive's own firmware and the laptop's cooling design, not by a pre-purchase compatibility check.
- Why D is incorrect: M.2 is a standardized connector specification. The M.2 slot pinout is identical across all manufacturers for the defined key types. There are no proprietary M.2 pinouts that restrict SSD purchases to matching brands.

---

### Question 17

A user reports that their laptop screen image is correct and clear when the lid is fully open, but the image flickers when the lid is tilted to approximately 30 degrees (nearly closed). The external monitor connected to the laptop's HDMI port shows no flicker. What is the most likely cause?

- A) The laptop's GPU is overheating and throttling when the lid restricts airflow from the rear vents, causing the integrated display to flicker at lid angles that block the exhaust path
- B) The display video cable (eDP or LVDS) routing through the hinge has developed a stress fracture or intermittent connection from repeated opening and closing — bending the cable at the hinge point at certain lid angles breaks continuity
- C) The LCD panel itself has a manufacturing defect where the pixel array loses synchronization at specific backlight brightness levels; the 30-degree position causes the ambient light sensor to reduce brightness to a level that triggers the defect
- D) The wireless antenna cables routed through the display assembly are interfering with the video cable signal when the lid is at 30 degrees, because the antenna transmit power is highest at this angle

Correct Answer: B

- Why B is correct: The display video cable (eDP on modern laptops or LVDS on older laptops) is routed from the motherboard through the hinge into the display panel. Repeated opening and closing stresses the cable at the hinge flex point. A stress fracture or loose connection in this cable produces a symptom that is position-dependent — the cable makes intermittent contact at some lid angles but not others. The external monitor working normally confirms the GPU and display controller are functioning correctly; the fault is in the internal cable path.
- Why A is incorrect: GPU thermal throttling affects rendering performance and frame rate across all display outputs simultaneously. It would not produce a position-dependent flicker limited to the internal display while the external monitor remains stable.
- Why C is incorrect: LCD panel defects correlated with backlight brightness would manifest as a brightness-triggered event, not a lid-angle-triggered event. The ambient light sensor changes brightness based on room lighting conditions, not lid angle.
- Why D is incorrect: Wireless antenna cables carry RF signals and use shielded coaxial construction specifically to prevent interference with adjacent cables. Antenna-to-video cable interference is not a recognized failure mode for laptop display flickering.

---

### Question 18

A technician is preparing to replace a failed trackpad on a laptop. After removing the bottom cover, the technician sees that the trackpad is connected to the motherboard via a very thin ribbon cable terminated in a ZIF connector. The ZIF connector on the motherboard has a small brown flip-locking bar. What must the technician do before pulling the ribbon cable out of the connector?

- A) Slide the flip-locking bar toward the connector body (lock it further) to compress the contacts and allow the cable to pull free with reduced friction
- B) Flip the locking bar up (away from the connector body) to release the tension clamp on the ribbon cable, then slide the cable straight out horizontally without any downward force
- C) Cut the ribbon cable close to the ZIF connector to release it from the motherboard, then solder a new cable section to the connector pads during the trackpad installation
- D) Heat the ZIF connector with a heat gun for 10 seconds to soften the locking mechanism, which is permanently bonded at the factory and cannot be released without thermal treatment

Correct Answer: B

- Why B is correct: ZIF (Zero Insertion Force) connectors use a cam-actuated locking mechanism. The locking bar (or flip-lock, actuator, or retainer) must be flipped upward to release the tension on the cable conductors. Only after the locking bar is in the released (open) position can the ribbon cable slide straight out with zero force required. Attempting to pull the cable while the locking bar is closed will tear the cable or rip the connector from the PCB.
- Why A is incorrect: Sliding the locking bar further closed would increase clamping force on the cable, making it impossible to remove and risking cable and connector damage if force is applied.
- Why C is incorrect: Cutting and resoldering ribbon cables is a destructive and unnecessary procedure for ZIF-connected components. ZIF connectors are specifically designed to allow non-destructive cable removal and reinsertion.
- Why D is incorrect: ZIF connectors are plastic and metal mechanical connectors — they are not bonded with adhesive and do not require heat to release. Applying a heat gun to a ZIF connector would melt the plastic housing and permanently damage the connector.

---

### Question 19

A laptop is returned to a technician after a display replacement with the complaint that the laptop makes a continuous low hum and the fan is running at maximum speed, but the CPU temperature is only 45°C (normal operating temperature). What is the most likely cause?

- A) The fan tachometer wire was disconnected or damaged during the display replacement; the motherboard is not receiving RPM feedback from the fan and is running it at maximum speed as a failsafe
- B) The CPU thermal paste dried out during the display replacement and the temperature sensor is reading incorrectly, showing 45°C while actual temperature is 95°C
- C) The display replacement introduced a short circuit in the power delivery circuit, causing the voltage regulators to run at maximum power and generate excess heat that the fan is compensating for
- D) The new display panel draws significantly more current than the original, overloading the motherboard's display controller and causing the system to throttle by running the fan at maximum to dissipate the additional heat

Correct Answer: A

- Why A is correct: Laptop motherboards use the CPU fan tachometer signal (a pulse signal proportional to RPM) to verify the fan is spinning. If the tachometer wire is disconnected or damaged during service, the motherboard receives no speed feedback and assumes the fan is not spinning. The failsafe response is to run the fan at maximum duty cycle. The CPU temperature being normal confirms the thermal path is fine — the issue is the missing tachometer feedback.
- Why B is incorrect: If thermal paste had dried out and the actual temperature were 95°C, the system would likely be throttling the CPU, shutting down automatically, or showing high temperatures in monitoring utilities. A reported temperature of 45°C with high fan speed is inconsistent with thermal paste failure.
- Why C is incorrect: A short circuit in the power delivery circuit would typically trigger overcurrent protection, cause the system to shut down, or generate localized heat measurable by the power management IC's thermal sensors — not simply cause maximum fan speed with normal CPU temperatures.
- Why D is incorrect: LCD panels are passive display devices that draw current from a regulated backlight power circuit. A replacement panel of the same type does not draw significantly more current than the original. Display current does not affect CPU fan speed control logic.

---

### Question 20

A technician is servicing a laptop with a cracked screen. Before ordering a replacement panel, which information must the technician identify to ensure the correct panel is ordered?

- A) The laptop's color and the user's preferred screen resolution — the panel is ordered based on aesthetics and user preference rather than hardware compatibility specifications
- B) The panel resolution, size (measured diagonally in inches), connector type (eDP or LVDS), backlight type (LED or CCFL), and ideally the original panel part number from the manufacturer label on the rear of the panel
- C) The operating system version and the GPU driver version — these determine which panel protocols the motherboard supports and which panels are compatible
- D) The laptop's age and the user's warranty status — newer laptops use eDP automatically and older laptops use LVDS automatically, so age alone determines which panel to order

Correct Answer: B

- Why B is correct: Correct panel replacement requires matching the physical size, resolution, connector type (eDP for modern panels, LVDS for older panels), backlight type (LED for most post-2010 laptops, CCFL for pre-2010), and ideally the full panel part number from the label on the rear of the existing panel. An incorrect connector type physically will not fit, and an LVDS panel cannot be substituted for an eDP panel even if dimensions match.
- Why A is incorrect: Panel compatibility is a hardware specification matter, not an aesthetic or preference matter. Ordering a panel based on color or user preferences without verifying hardware specifications will likely result in an incompatible part.
- Why C is incorrect: Operating system version and GPU driver version are software attributes that have no bearing on which physical LCD panel the laptop's display connector supports. Panel compatibility is determined by the hardware interface on the motherboard.
- Why D is incorrect: While there is a general correlation between laptop age and display interface type (eDP vs. LVDS), the transition period from LVDS to eDP spans several years and varies by manufacturer and model. Assuming panel type based solely on age is unreliable and can result in ordering the wrong part.
