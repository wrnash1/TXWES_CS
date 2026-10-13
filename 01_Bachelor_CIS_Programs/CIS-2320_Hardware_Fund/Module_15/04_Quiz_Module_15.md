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

---

### Question 11

A laser printer is producing pages where a repeating smudge mark appears at exactly the same position on every page and wipes off with a finger. What is the most likely cause?

- A) The toner cartridge is running low on toner and the smudge is caused by uneven toner distribution as the supply depletes
- B) The fuser assembly is failing — the smudge wipes off because the toner is not being bonded to the paper by sufficient heat and pressure during the fusing stage
- C) The paper tray is loaded with paper that is too heavy for the printer's specification, and the extra weight prevents the paper from reaching the fuser at the correct speed
- D) The printer drum has a gouge or contamination at a specific point — the drum's circumference determines the repeat interval of the defect, and a contaminated spot transfers excess toner at that position each rotation

Correct Answer: D — A defect or contamination on the drum repeats at a fixed interval equal to the drum's circumference.

A repeating defect at a fixed page interval is a diagnostic indicator of a drum problem. The drum rotates as paper passes through, and any contamination, gouge, or physical defect on the drum surface will transfer excess toner (or fail to pick up toner) at that exact position on every rotation. This produces a mark at the same distance on consecutive pages. Answer B is incorrect because unfused toner (fuser failure) would smear across the entire image area, not produce a small repeating mark at a fixed position. Answer A is incorrect because low toner causes fading and light print across the entire page, not a localized repeating smudge. Answer C is incorrect because paper weight causes feed jams or fuser pressure issues, not a repeating smudge at a fixed position.

---

### Question 12

A user reports that their inkjet printer is producing streaks in the printed output, with certain colors missing entirely in horizontal bands. The printer is two weeks old and has never had a clogged nozzle before. What should the technician do first?

- A) Replace the ink cartridge that corresponds to the missing color immediately — new printers frequently have defective cartridges from the factory
- B) Run the printer's built-in printhead cleaning cycle from the printer's maintenance menu or control panel, as dried ink or air bubbles in a new inkjet printer can temporarily clog nozzles
- C) Increase the print quality setting in the print driver to "Best" quality — lower quality settings skip nozzle rows to increase speed, which appears as streaks and missing bands
- D) Disassemble the printhead and soak it in warm water for 30 minutes to dissolve dried ink — this is the recommended first maintenance step for any inkjet nozzle issue

Correct Answer: B — Run the built-in printhead cleaning cycle first; clogged nozzles are common in new inkjet printers.

Inkjet printers can develop clogged nozzles from dried ink (especially if the printer was stored or sat unused for a period between manufacturing and use). The printhead cleaning cycle fires ink through the nozzles at higher pressure to clear blockages and is the correct first maintenance step before taking any other action. Multiple cleaning cycles may be needed. Answer A is incorrect because replacing a cartridge is a costly first step when a non-destructive cleaning cycle is available and may resolve the issue. Answer C is incorrect because print quality settings affect resolution and ink coverage uniformly, not specific missing color bands corresponding to individual nozzle rows. Answer D is incorrect because manual soaking of the printhead requires disassembly, is not a beginner first step, and can damage the electronic contacts on the printhead if water reaches the wrong areas.

---

### Question 13

A technician installs a new thermal printer for a retail point-of-sale system. After printing the first receipt, the output is completely blank — no text or graphics appear. The printer feeds paper normally. What is the most likely cause?

- A) The thermal printer driver is not installed and the printer is outputting data correctly but the driver is translating all characters to blank spaces
- B) The paper roll is loaded backward — thermal paper only reacts to heat on the coated side, and loading it with the uncoated side facing the thermal printhead produces blank output
- C) The thermal printhead is operating at too low a temperature — increasing the temperature setting in the printer's configuration will make the output visible
- D) The receipt paper is the wrong size and the printer is scaling the output off the printable area, causing the characters to print past the paper edge

Correct Answer: B — The thermal paper roll is loaded backward with the uncoated side facing the printhead.

Thermal printers work by applying heat to heat-sensitive paper coated on one side. If the paper is loaded with the coated side facing away from the printhead, the heat activates nothing and the output is completely blank. The paper still feeds and ejects normally because the paper movement mechanism is independent of the coating. The fix is to reload the paper with the coated side facing the printhead. Answer A is incorrect because a missing driver would cause no output at all (the printer would ignore or reject print jobs) rather than blank output from correctly fed paper. Answer C is incorrect because a thermal printhead operating at low temperature would produce faint output, not completely blank output — the output would be visible but light. Answer D is incorrect because incorrect paper size causes print jobs to be cut off or misaligned, not completely blank output across the entire page.

---

### Question 14

A laser printer consistently outputs pages with a vertical white stripe running from top to bottom on the right side of each page. The stripe is always in the same position. What is the most likely cause?

- A) The right paper guide in the paper tray is set too wide, allowing the paper to shift left during feeding and leaving a white margin on the right where the toner cannot reach
- B) The toner cartridge has a scratch or developer roller defect in the area corresponding to the right side of the page, preventing toner from being applied to that vertical stripe
- C) The printer's imaging drum is charged correctly but the laser scanning unit has a failed mirror segment that prevents the laser from writing to the right portion of the drum, leaving that area uncharged and therefore no toner is applied
- D) The transfer corona wire is dirty on the right side, preventing the positive charge from being applied to the paper in that vertical stripe and preventing toner from transferring from the drum to the paper

Correct Answer: C — A failed or blocked laser scanning unit segment prevents the laser from writing to that portion of the drum.

A vertical white stripe in a consistent position across every page indicates that no toner is being deposited in that area. In a laser printer, toner is applied only to areas where the laser has discharged the drum (the latent image). If the laser scanning assembly has a defective mirror, lens, or blocked beam path for a specific portion of the scan, that horizontal segment of the drum is never discharged and toner is never applied there, producing a vertical white stripe on every page. Answer B is also plausible — a developer roller defect can produce a similar stripe — but laser scanning unit failure is the primary mechanism for a precisely defined vertical white stripe. Answer A is incorrect because paper guide misalignment would produce variable margins, not a sharp vertical stripe at an exact position. Answer D is incorrect because a dirty transfer corona wire produces light or missing areas but typically appears as horizontal banding rather than a precise vertical stripe.

---

### Question 15

A technician is setting up a shared printer on a small office network using Windows. The printer is directly connected to one workstation via USB. Which of the following configurations allows all other workstations to print to this printer?

- A) Connect the printer directly to the network switch via Ethernet and configure it with a static IP address — USB-connected printers cannot be shared on a Windows network
- B) Enable Windows File and Printer Sharing on the host workstation, share the printer through the Windows Control Panel printer settings, and install the appropriate printer driver on each client workstation pointing to the shared printer's network path (for example, \\HostPC\PrinterName)
- C) Install the printer driver on all workstations using the same USB cable — each workstation must physically connect to the printer in turn to receive the driver
- D) Configure the printer as a network printer directly in the switch's management interface — managed switches include a print server feature that can redirect USB printer output to the network

Correct Answer: B — Enable Windows Printer Sharing on the host PC and install the driver on each client pointing to the UNC network path.

Windows printer sharing allows a USB-connected printer on one computer (the host) to be shared over the LAN. Other workstations access the shared printer using its UNC path (\\HostPC\PrinterName). The host computer must be on and running for other workstations to print. This is a standard Windows configuration for small offices that do not have a dedicated print server or a network-capable printer. Answer A is incorrect because USB-connected printers can be shared via Windows Printer Sharing — a direct network connection is not required. Answer C is incorrect because printer drivers are installed from software on each machine, not by sharing a USB cable; only one computer can connect to a USB device at a time. Answer D is incorrect because managed switches do not include print server functionality — switches are Layer 2 network devices with no application-layer print services.

---

### Question 16

During a laser printer maintenance procedure, the technician opens the printer and notices the drum cartridge surface has a deep scratch visible in reflected light. After reinstalling the drum and printing a test page, what symptom should the technician expect?

- A) A horizontal light band across every page at the location corresponding to the scratch, because the scratch prevents the fuser from reaching the paper at that point
- B) A vertical black stripe on every page in the position corresponding to the scratch, because the scratched area of the drum holds toner regardless of laser exposure due to the altered surface charge properties
- C) No visible defect — drum scratches are too microscopic to affect print quality and the OPC coating self-heals minor surface damage through normal use
- D) Complete blank output on all pages because a scratched drum cannot hold any electrostatic charge across its entire surface

Correct Answer: B — A scratched drum produces a vertical black stripe on every page.

The drum's OPC (Organic Photoconductor) coating is sensitive and fragile. A physical scratch on the drum surface damages the OPC, creating an area that either holds toner unconditionally (if the scratch causes the area to attract toner without needing laser exposure) or fails to hold toner in a specific pattern. A deep scratch typically creates a vertical black stripe because the scratch runs the length of the drum and affects the same longitudinal position on every page rotation. This is a definitive sign the drum cartridge must be replaced. Answer A is incorrect because horizontal bands are produced by drum contamination or fuser issues, not drum scratches. Answer C is incorrect because drum OPC coatings do not self-heal and a scratch deep enough to be visible will produce a print defect. Answer D is incorrect because a single scratch does not eliminate charge from the entire drum surface — only the scratched area is affected.

---

### Question 17

A user prints a document and finds that the printed output has a ghosted faint duplicate image slightly below and to the right of the main image on every page. The main image is dark and clear; the ghost is light. This is a laser printer. What component is most likely causing the ghosting?

- A) The fuser assembly is applying too much heat, causing toner from the current pass to leave a residual impression that transfers to the next pass of paper
- B) The drum is not being fully cleaned between print cycles — residual toner left on the drum from the previous page is partially transferring to the next page, creating a ghost of the previous image
- C) The paper is too smooth and reflects the laser beam sideways, causing a secondary latent image to form adjacent to the intended image
- D) The toner cartridge has too much toner loaded, causing toner to spill onto the drum outside the intended image area

Correct Answer: B — Incomplete drum cleaning is leaving residual toner that transfers as a ghost image.

Ghosting on a laser printer (a faint secondary image appearing on each page) is classically caused by incomplete cleaning of the drum. If the cleaning blade or cleaning pad fails to remove all residual toner after the transfer stage, that toner remains on the drum and partially transfers to the next page during the following print cycle. Since the residual image matches the previous page's content, it appears as a ghost. The cleaning assembly (blade or brush) should be inspected and the drum cartridge replaced if the cleaning mechanism is worn. Answer A is incorrect because excess fuser heat causes toner to offset to the fuser roller (which then deposits it later), not a ghost tied to the previous page's content. Answer C is incorrect because paper reflectivity does not create ghost images — the laser is inside the printer and paper does not interact with it. Answer D is incorrect because excess toner in the cartridge causes heavy or smeared output, not a ghost of the previous page.

---

### Question 18

A technician is asked to install a network-attached printer that will be accessed by 30 users in an office. The printer has a built-in Ethernet port. What is the correct installation approach to allow all 30 users to print without a dedicated print server computer?

- A) Connect the printer to the network switch, assign it a static IP address (or configure a DHCP reservation), and install the printer driver on each workstation pointing to the printer's IP address or hostname
- B) Connect the printer to one workstation via USB, share the printer through Windows, and configure each workstation to use the shared printer's UNC path — this is equivalent to a direct network printer for 30 users
- C) Connect the printer to the network switch and configure all 30 workstations to print to the same queue on the switch's built-in print management service
- D) Connect the printer to the network switch and configure one workstation as a domain controller — only domain-joined machines can print directly to a network printer

Correct Answer: A — Connect the printer to the switch, assign a static IP, and install the driver on each workstation pointing to the printer's IP.

A network printer with a built-in Ethernet port acts as its own print server. Each client workstation installs the printer driver and configures the printer using the printer's IP address (or DNS hostname). The printer accepts jobs directly over the network without requiring a host PC. Assigning a static IP (or DHCP reservation) ensures the printer's address does not change and invalidate all client configurations. Answer B is incorrect because a USB-shared printer depends on one workstation being powered on and available at all times — this is not recommended for 30 users. Answer C is incorrect because switches do not include print management services. Answer D is incorrect because network printing does not require Active Directory or domain membership — workgroup configurations work equally well for direct IP-based printing.

---

### Question 19

A color laser printer is producing output where cyan objects appear correctly but all magenta elements are missing from the print. All other colors (yellow, black) are present. What is the most likely cause?

- A) The yellow and magenta toner cartridges are both installed but the magenta drum cartridge is defective, preventing magenta toner from being applied
- B) The magenta toner cartridge is empty or the magenta imaging drum has failed — color laser printers use separate toner cartridges and drum units for each of the four CMYK colors (Cyan, Magenta, Yellow, Black)
- C) The color calibration profile in the print driver has set magenta to zero density; reinstalling the driver will restore the magenta channel
- D) The fuser assembly applies different temperatures for each color pass and the temperature for the magenta pass has dropped too low to bond toner to the paper

Correct Answer: B — The magenta toner cartridge is empty or the magenta imaging drum has failed.

Color laser printers use four separate imaging paths — one for each CMYK color. Each path has its own toner cartridge, developer, and in many designs a separate drum unit. If the magenta cartridge is empty or the magenta drum has failed, magenta is not applied during the transfer process. Cyan, yellow, and black are unaffected because they use independent components. The fix is to replace the magenta toner cartridge (and drum if applicable). Answer A is incorrect because yellow and magenta are distinct components — if yellow appears correctly, the yellow components are functioning, so the issue is specific to the magenta path. Answer C is incorrect because driver color density settings affect all print jobs simultaneously and are typically set by the administrator, not silently changed; a missing-color symptom across all output is more likely a hardware cause than a driver setting. Answer D is incorrect because fuser assemblies in most color laser printers apply heat uniformly to bond all colors in a single pass — the fuser does not have per-color temperature zones.

---

### Question 20

A 3D printer is producing objects where the layers on the bottom portion of the print are solid but the upper layers are visibly separated and porous. The print bed is level. What is the most likely cause?

- A) The print bed temperature is too high, causing the upper layers to melt back into the lower layers and creating a porous surface from re-solidification
- B) The extruder is under-extruding — possible causes include a partial clog in the nozzle, incorrect filament diameter settings in the slicer, or insufficient extruder motor steps per mm, all of which result in insufficient plastic being deposited per layer as the print height increases
- C) The layer height setting in the slicer is too small for the nozzle diameter being used, causing upper layers to fail to bond to lower layers because each layer is thicker than the gap between nozzles
- D) The print cooling fan is causing premature solidification of the upper layers before they can bond to the previous layer — turning off the cooling fan will allow the upper layers to fuse correctly

Correct Answer: B — The extruder is under-extruding, depositing insufficient plastic in the upper layers.

Under-extrusion in 3D printing produces gaps between print lines (porosity) and layer separation, particularly noticeable in upper layers that are further from the first layer (which is typically slower and more carefully deposited). Common causes include: partial nozzle clog, incorrect filament diameter in the slicer settings, extruder motor calibration (steps per mm), and printing too fast for the hotend's melt rate. The bottom layers appear solid because the lower printing speed and prime squish of the first layers compensate for minor under-extrusion. Answer A is incorrect because high bed temperature affects adhesion of the first layer to the bed — it does not cause upper layer porosity. Answer C is incorrect because layer height smaller than appropriate for the nozzle diameter causes over-squish and elephant foot, not separation. Answer D is incorrect because the cooling fan is essential for upper layers to maintain structural integrity — removing it causes warping and drooping in overhanging features, not porosity from poor bonding.
