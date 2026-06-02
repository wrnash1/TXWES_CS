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
