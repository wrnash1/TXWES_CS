# Quiz: Module 15 - Printers and Imaging

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

### Question 1

What is the correct sequence of steps in the laser printing electrophotographic (EP) process?

- A) Charging, Exposing, Developing, Transferring, Fusing, Cleaning
- B) Exposing, Charging, Transferring, Fusing, Cleaning, Developing
- C) Cleaning, Charging, Exposing, Developing, Transferring, Fusing
- D) Developing, Exposing, Charging, Transferring, Fusing, Cleaning

Correct Answer: C — Cleaning, Charging, Exposing, Developing, Transferring, Fusing.

The standard CompTIA A+ EP process sequence begins with Cleaning (removing residual toner from the drum), then Charging (applying a uniform negative charge), then Exposing/Writing (the laser discharges selected areas to form the latent image), then Developing (negatively charged toner adheres to the discharged areas), then Transferring (toner moves from the drum to the positively charged paper), then Fusing (heat and pressure permanently bond the toner to the paper). Answer A skips Cleaning as the first step. Answers B and D both misplace Charging and Exposing relative to each other and to the drum preparation steps.

---

### Question 2

Which of the following most accurately describes inkjet printer maintenance?

- A) Replacing the drum unit and primary corona wire on a fixed mileage schedule to prevent ink overspray from contaminating the charging circuit.
- B) Running the printer driver's nozzle check to identify clogged nozzles, then running a head cleaning cycle to force ink through blocked openings — with the nozzle check repeated after each cleaning cycle to confirm improvement before running another.
- C) Recalibrating the fuser temperature and pressure roller gap after every third cartridge replacement to prevent smearing on glossy paper stock.
- D) Degaussing the print head carriage motor using a magnetic calibration tool after the printer is moved to re-establish accurate motor positioning.

Correct Answer: B — Run the nozzle check first, then one head cleaning cycle, then recheck before running additional cycles.

Inkjet maintenance centers on nozzle clog management. Ink dries in nozzles during inactivity, blocking the microscopic openings. The nozzle check prints a diagnostic pattern revealing which nozzles are blocked. The head cleaning utility forces ink through to clear the blockage. Best practice is one cycle then recheck — running multiple cycles without checking wastes significant ink. Answer A incorrectly applies laser printer components (drum, corona wire) to an inkjet. Answer C applies laser printer fuser concepts to an inkjet, which has no fuser. Answer D describes a non-existent maintenance procedure — degaussing is used for CRT monitors and certain magnetic storage media, not printer carriage motors.

---

### Question 3

A laser printer produces pages where toner smears when touched and rubs off easily, but the print is otherwise sharp and correctly positioned. Which EP process step is failing?

- A) Charging — the corona wire is not applying sufficient negative charge, causing toner to adhere loosely across the drum surface.
- B) Transferring — the transfer roller is not pulling toner completely off the drum, leaving excess toner unattached on the paper.
- C) Fusing — the fuser assembly is not applying sufficient heat or pressure to permanently bond the toner particles into the paper fibers.
- D) Exposing — the laser is not writing the image correctly, causing toner to attach to unintended drum areas that then smear during output.

Correct Answer: C — Fusing failure. Toner that smears when touched is the definitive symptom of a fuser problem.

The fuser uses a heated roller and a pressure roller to melt and bond toner into the paper. If either the heat or pressure is insufficient — due to a failing heater element, worn pressure rollers, or the fuser not reaching operating temperature — the toner reaches the paper (transfer was successful, hence the clear visible image) but is not bonded. Rubbing the page removes it. Answer A (charging failure) produces faded or uneven background toner coverage, not a smear symptom. Answer B (transfer failure) produces faint or incomplete image content — portions are missing, not smearing. Answer D (exposing failure) causes incorrect or missing print content because the latent image is not correctly written.

---

### Question 4

A receipt printer at a POS terminal is producing completely blank receipts. The paper roll appears loaded correctly and the printer reports no errors. What is the most likely cause?

- A) The print head has exceeded its rated lifespan of approximately 500,000 lines and must be replaced on schedule.
- B) The paper roll is loaded with the uncoated side facing the printhead; direct thermal paper has a heat-sensitive coating on one side only and must face the printhead to produce output.
- C) The receipt printer's ink ribbon is depleted and must be replaced; without a ribbon the printhead cannot transfer ink to the paper.
- D) The printer driver is corrupted; blank output on a thermal printer always indicates the driver is sending empty print data to the device.

Correct Answer: B — The paper roll is loaded backward; the uncoated side is facing the printhead.

Direct thermal printers produce output by applying heat from the printhead to the chemically coated side of the paper, causing it to darken. If the uncoated side faces the printhead, the heat contacts plain paper and produces no visible output — perfectly blank receipts with no error. The fix is to reload the roll with the coated (typically shinier or smoother) side facing the printhead. Answer A is incorrect — thermal printhead failure is not on a fixed 500,000-line schedule and presents as degraded partial output, not completely blank output on an otherwise-functioning printer with no errors. Answer C is incorrect — direct thermal printers have no ribbon; that is a thermal transfer printer characteristic. Answer D is incorrect — driver corruption produces error messages or garbled output, not the specific clean-blank pattern caused by reversed paper.

---

### Question 5

A 3D printer using FDM technology is printing with ABS filament. The corners of the print are lifting off the build plate about 45 minutes into the job. The build plate is unheated. What is the most likely cause and the correct fix?

- A) The nozzle temperature is too high, causing the ABS to pool on the plate before solidifying; lower the nozzle temperature by 20 degrees Celsius.
- B) ABS has a high thermal contraction rate and requires a heated build plate (90 to 110 degrees Celsius) and ideally an enclosure to maintain ambient temperature and prevent the warping caused by uneven cooling.
- C) The slicer layer height setting is too large for ABS; reducing the layer height to 0.1 mm will eliminate warping by improving inter-layer adhesion.
- D) The filament spool is mounted in the wrong direction, causing the extruder motor to work against the coil tension and underextrude material at corners.

Correct Answer: B — ABS requires a heated build plate and enclosure; uneven cooling causes thermal contraction that lifts corners.

ABS has a significantly higher coefficient of thermal expansion than PLA. When the bottom layers cool and contract while upper layers are still hot, the differential stress overcomes bed adhesion and lifts the print corners — this is warping. A heated bed at 90 to 110°C slows cooling of the first layers; an enclosure maintains a warm ambient temperature that reduces the thermal gradient between layers. Without these, ABS warping is nearly unavoidable. Answer A is incorrect — while nozzle temperature affects adhesion between layers, the corner-lifting warping pattern is specifically caused by thermal contraction, not by excess nozzle heat. Answer C is incorrect — layer height affects layer bond strength and surface quality but does not address the thermal contraction mechanism responsible for warping. Answer D is incorrect — spool direction does not meaningfully affect extrusion; underextrusion from that cause would appear throughout all layers as gaps, not as corner lifting.

---

### Question 6

A laser printer consistently produces pages with a gray background tint across the entire page surface even when printing content on a white background. The toner cartridge is not empty. What is the most likely cause?

- A) The fuser assembly is overheating and baking excess toner onto the paper as it passes through.
- B) The primary corona wire or charge roller is dirty or failing, resulting in insufficient negative charge on the drum — allowing background toner to adhere where it should be repelled.
- C) The paper tray is loaded with paper that has a gray tint; the printer is reproducing the paper color accurately.
- D) The laser exposure unit is firing continuously, fully discharging the entire drum surface so toner adheres everywhere.

Correct Answer: B — A dirty or failing charge roller causes uneven or weak drum charging, allowing background toner adhesion.

The Charging step applies a strong uniform negative charge to the drum. Background areas (where no content should print) rely on this strong negative charge to repel negatively charged toner particles. If the charge is weak or uneven because the corona wire is contaminated or the charge roller is worn, background areas do not repel toner effectively, and a gray haze of toner deposits across the page. Cleaning or replacing the charge roller resolves this. Answer A is incorrect — fuser overheating causes smearing or paper jams, not a gray background toner haze. Answer C is incorrect — standard white office paper does not produce a gray background tint in a laser printer; the symptom is printer-side, not paper-side. Answer D is incorrect — if the laser discharged the entire drum, output would be solid black pages, not a gray background.

---

### Question 7

Which step of the laser EP process involves the laser diode and rotating polygon mirror working together to create the latent image on the drum?

- A) Charging
- B) Developing
- C) Exposing
- D) Transferring

Correct Answer: C — Exposing (also called Writing)

During the Exposing step, the laser assembly scans across the charged drum using a rotating polygon mirror to deflect the laser beam in a line-by-line pattern. Wherever the laser hits the drum, it discharges that area from approximately -600V to approximately -100V, creating a latent (invisible) electrostatic image. The discharged areas represent where toner will adhere; the undischarged areas represent the white background. Answer A (Charging) is the step before Exposing where the drum receives its uniform negative charge — the laser is not involved. Answer B (Developing) is after Exposing — it brings toner to the already-written drum. Answer D (Transferring) moves toner from the drum to the paper — again, the laser is not involved.

---

### Question 8

A laser printer is producing pages where a small black dot repeats at exactly 94 mm intervals down the page, regardless of the print content. The dot is always in the same horizontal position. What does this pattern indicate and what is the likely fix?

- A) The toner cartridge is nearly empty; toner clumping at 94 mm intervals is normal near end-of-life and the cartridge should be replaced.
- B) A contamination spot or physical defect exists on a rotating component — most likely the photosensitive drum — at a circumferential position that repeats every 94 mm. The drum or toner cartridge should be replaced.
- C) The fuser pressure roller has a flat spot causing the paper to pause briefly every 94 mm, allowing excess heat to concentrate and leave a mark. The fuser assembly should be replaced.
- D) The paper feed roller is slipping every 94 mm due to wear, causing the paper to advance unevenly and receive double exposure at the repeat interval.

Correct Answer: B — A contamination spot or defect on a rotating drum component repeating at the drum's circumference interval.

Repeating defects at a consistent interval indicate a contamination spot or physical damage at a fixed point on a rotating component. The interval between repeats equals the circumference of the faulty component. A 94 mm repeat interval corresponds to the standard circumference of many photosensitive drums (approximately 30 mm diameter × π ≈ 94 mm). Because the drum is inside the toner cartridge in most consumer printers, replacing the toner cartridge (which includes an integrated drum) or the separate drum unit resolves the defect. Answer A is incorrect — toner depletion causes gradual fading across the page, not discrete repeating dots at a precise interval. Answer C is incorrect — a fuser pressure roller flat spot would cause inconsistent fusing (smearing) at that interval, not a clean repeated dot. Answer D is incorrect — feed roller slippage causes paper skew and misalignment, not a repeating dot defect at a precise horizontal position.

---

### Question 9

A technician is comparing inkjet print head configurations. Which statement correctly describes the difference between an integrated print head and a fixed print head in inkjet printers?

- A) An integrated print head is built into the ink cartridge and is replaced when the cartridge is swapped; a fixed print head is permanently mounted on the carriage and is cleaned in place when clogged.
- B) An integrated print head uses thermal inkjet technology exclusively; a fixed print head uses piezoelectric technology exclusively, and the technologies are not interchangeable.
- C) An integrated print head connects directly to the paper and transfers ink by contact; a fixed print head uses a laser to vaporize ink droplets and propel them onto the paper.
- D) An integrated print head requires the printer to be fully disassembled for replacement; a fixed print head can be swapped by the end user in under two minutes without tools.

Correct Answer: A — Integrated heads are inside the cartridge and replaced with it; fixed heads are permanent and maintained by cleaning.

In integrated print head designs (used by HP and Canon among others), the print head nozzle array is physically part of the ink cartridge. Replacing a depleted cartridge also replaces the nozzles — convenient maintenance that prevents permanent nozzle damage from severe clogs. In fixed print head designs (used by Epson), the print head is a permanent component of the printer carriage, and ink cartridges or bottles are separate consumables. Clogs in a fixed head are resolved through cleaning cycles. Fixed heads have a longer operational life if properly maintained. Answer B is incorrect — integrated vs fixed head is a structural distinction, not a technology distinction; thermal and piezoelectric are nozzle firing mechanisms that exist independently of the head mounting style. Answer C describes a fictional mechanism. Answer D has the descriptions reversed — integrated heads (inside the cartridge) are easy to swap; fixed heads require service or advanced disassembly when they fail beyond cleaning.

---

### Question 10

A network printer that has been working reliably for six months suddenly stops receiving print jobs from all client computers simultaneously. The printer's control panel shows it is online and ready. A test page printed directly from the printer control panel prints successfully. What is the most likely cause?

- A) The printer's fuser assembly has failed; fuser failure prevents the printer from accepting network jobs while still allowing local test pages from the control panel.
- B) The printer received a new IP address from the DHCP server; client computers have print queues pointing to the old IP address, which no longer routes to the printer.
- C) All client computers simultaneously lost their printer driver; a mass driver failure is common when the printer goes idle for more than 48 hours on a network.
- D) The printer's network interface card (NIC) has failed; the control panel test page uses a separate internal communication path that does not pass through the NIC.

Correct Answer: B — The printer received a new DHCP IP address; client queues are pointing to the old address.

Network printers configured with dynamic IP addressing can receive a new IP address when their DHCP lease expires or when the printer is power-cycled. When this happens, all existing print queue configurations on client computers — which reference the printer by IP address — stop working because that IP no longer routes to the printer. The printer itself functions normally (it can print test pages locally) but is unreachable at its old address. The fix is to assign the printer a static IP address and update client queues, or to configure the printer by hostname (DNS name) instead of IP address. Answer A is incorrect — fuser failure affects print quality output, not network job reception; a failing fuser does not block network communication. Answer C is incorrect — printer drivers do not fail en masse due to inactivity; driver loss on one computer is possible but simultaneous loss across all clients is not a realistic scenario. Answer D is incorrect — if the network NIC had failed, the printer would not have received the new IP address in the first place; DHCP communication requires a functioning NIC.
