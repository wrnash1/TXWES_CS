# Reading Guide: Module 15 - Printers and Imaging

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

---

### Introduction

Welcome to Module 15 — Printers and Imaging. This module covers the four major printer technologies a technician encounters in the field: laser, inkjet, thermal, and 3D printers. For each technology you will learn how it works mechanically, what consumables it uses, what routine maintenance it requires, and how to diagnose common print quality failures. The laser printing electrophotographic (EP) process is among the most heavily tested topics on the CompTIA A+ Core 1 (220-1101) exam under Domain 3.7, and printer troubleshooting scenarios appear on both Core 1 and Core 2 under Domain 5.7.

As a field technician, you will replace toner cartridges, diagnose smearing and fading on laser printers, clean inkjet nozzles, reload thermal paper correctly, and explain to users why their 3D print warped off the build plate. Complete the study checklist and review all glossary terms before attempting the lab.

---

### Section 1: Laser Printer Technology and the EP Process

A laser printer uses an electrophotographic (EP) process to transfer a toner image permanently onto paper. The process is named for the combination of electrical charges and light (photons from the laser) used to control toner placement. Understanding each step at the component level is essential for both the certification exam and real-world troubleshooting.

**The Photosensitive Drum:**
The photosensitive drum is the central component of the laser printing process. Its surface is coated with a photoconductive material that holds an electrical charge in the dark and loses that charge when exposed to light. This property is what makes the entire EP process possible. The drum rotates once per printed page (or multiple times for long pages) and must be clean and uniformly charged before each cycle.

**The Six Steps of the EP Process in Sequence:**

Step 1 — Cleaning: A rubber cleaning blade scrapes residual toner from the drum surface left over from the previous print cycle. A cleaning roller or brush sweeps away the scraped particles into a waste toner reservoir. The drum must be completely clean before it can accept a new charge. In the official CompTIA A+ sequence, Cleaning is listed as the first step because it prepares the drum for the next cycle.

Step 2 — Charging: The primary corona wire or charge roller applies a uniform high-voltage negative charge (typically -600V) across the entire drum surface. This uniform negative charge is the blank canvas on which the latent image will be written. Without a proper uniform charge, toner will not adhere correctly and the resulting print will be faded, uneven, or contaminated with background toner.

Step 3 — Exposing (Writing): The laser assembly — consisting of a laser diode and a rapidly rotating polygon mirror — scans across the drum one line at a time, firing the laser at points that correspond to content in the printed image. Wherever the laser hits the drum, it discharges that area from approximately -600V to approximately -100V. This creates a latent (invisible) image: charged areas are the background (no toner will stick) and discharged areas form the image (toner will stick). The laser writes the negative of the print — it writes the spaces, not the content directly.

Step 4 — Developing: The developer roller carries negatively charged toner particles past the drum. The strongly negative background areas repel the toner (like charges repel). The relatively positive discharged areas (the latent image) attract the negatively charged toner. Toner adheres to the drum in the exact pattern of the latent image. The image is now visible on the drum but has not yet touched the paper.

Step 5 — Transferring: Paper is pulled from the paper tray by feed rollers and fed between the drum and the transfer corona wire or transfer roller. The transfer component applies a positive charge to the back of the paper. Because the paper is now positively charged, it attracts the negatively charged toner off the drum surface. The toner transfers from the drum to the paper. At this point the toner is sitting loosely on the paper surface — it will smear easily if touched.

Step 6 — Fusing: The paper passes through the fuser assembly, which contains a heated fuser roller (typically 165 to 200 degrees Celsius) and a pressure roller. The heat melts the thermoplastic toner particles; the pressure presses the melted toner into the paper fibers. When the paper exits the fuser and cools, the toner is permanently bonded to the paper and cannot be rubbed off. This is why laser-printed pages exit the printer warm to the touch.

**Mnemonic for the Six Steps:**
Could Children Ever Do That Fast? — Cleaning, Charging, Exposing, Developing, Transferring, Fusing.

---

### Section 2: Laser Printer Components

**Primary Corona Wire / Charge Roller:** Applies the uniform negative charge to the drum during the Charging step. If dirty or damaged, the charge is uneven, producing a gray background or faded streaks on printed pages.

**Photosensitive Drum:** The rotating cylinder that carries the latent image. Drum units have a finite lifespan measured in page count; a worn drum produces repeating defects. The drum is typically included inside the toner cartridge in consumer printers (integrated drum design) or is a separate replaceable unit in enterprise printers (separate drum design).

**Toner Cartridge:** Contains the toner powder and (in integrated designs) the drum and developer components. Toner is a thermoplastic powder — it melts when heated by the fuser. Gently rocking a nearly-empty cartridge redistributes remaining toner and extends print life temporarily.

**Developer Roller:** Within the toner cartridge, the developer roller carries toner to the drum during the Developing step. A worn or contaminated developer roller causes uneven toner application.

**Transfer Corona Wire / Transfer Roller:** Applies a positive charge to the paper during the Transferring step. A worn transfer roller is the most common cause of faint or incomplete toner transfer.

**Fuser Assembly:** Contains the heated fuser roller and pressure roller. The fuser is a high-wear component with a rated page life. A failing fuser causes toner to not bond — output smears when touched. The fuser also causes paper jams when the rollers wear and lose grip.

**Paper Path and Feed Rollers:** Move paper through the printer. Worn feed rollers cause paper jams, double-feeds, and skewed pages. Rollers can be cleaned with a damp cloth or replaced when worn.

---

### Section 3: Laser Printer Print Quality Troubleshooting

Matching a print quality symptom to the responsible EP process step is a core A+ exam skill:

- Faded or light output overall: Low toner (try rocking the cartridge), or a worn/contaminated charge roller producing insufficient drum charge.
- Gray background on page: Dirty primary corona wire or charge roller; the drum is not receiving a strong enough negative charge to fully repel toner from background areas.
- Smearing or toner that rubs off: Fuser failure — the fuser is not reaching operating temperature or the pressure rollers are worn. This is the most commonly tested laser printer defect.
- Faint or incomplete image transfer: Worn transfer roller or contaminated transfer corona wire. The paper is not receiving a strong enough positive charge to fully pull toner from the drum.
- Vertical black lines running the full page length: A scratch or groove in the drum surface. The scratch creates a path of consistent discharge that attracts toner in a vertical line. The drum must be replaced.
- Repeating defect at regular page intervals: A contamination spot on a rotating component. The interval (distance between repeats) corresponds to the circumference of the component — typically the drum, developer roller, or fuser roller. Measure the interval to identify which component to replace.
- Paper jams: Worn feed rollers (double-feeds or misfeeds), debris in the paper path, or wrong paper type/weight for the printer's specification.

---

### Section 4: Inkjet Printer Technology and Maintenance

Inkjet printers create images by spraying microscopic droplets of liquid ink through an array of nozzles in the print head. The print head assembly moves across the paper on a carriage while the paper advances incrementally.

**Inkjet Nozzle Technologies:**
Thermal inkjet (used by HP and Canon) heats a tiny element to vaporize ink, creating a bubble that expels a droplet through the nozzle. Piezoelectric inkjet (used by Epson) uses a piezo crystal that flexes when voltage is applied, mechanically pushing ink out of the nozzle. Piezoelectric heads are more durable and can use a wider range of ink types.

**Print Head Configurations:**
In integrated print head designs (common in HP), the print head is built into the ink cartridge. Replacing the cartridge also replaces the print head — convenient for maintenance but more expensive per cartridge. In fixed print head designs (common in Epson), the print head is permanently mounted on the carriage and ink cartridges are refilled separately. Fixed heads can clog but last longer if maintained.

**Inkjet Maintenance Procedures:**
Clogged nozzles are the primary maintenance concern. Ink dries in nozzles during periods of inactivity, blocking the microscopic openings. The printer driver software provides two maintenance tools accessible from the printer properties or maintenance tab:

- Nozzle Check: Prints a test pattern — typically a grid of colored lines — showing which nozzles are firing correctly and which are clogged. Run this first to confirm the problem and establish a baseline.
- Head Cleaning: Forces ink through all nozzles at high pressure to clear blockages. Each cleaning cycle consumes a significant amount of ink. Running excessive cleaning cycles depletes ink rapidly. Best practice: run one cleaning cycle, then run the nozzle check again before deciding whether to run another cycle.

Additional inkjet maintenance: clean the paper feed rollers with a lint-free cloth if misfeeds occur; ensure the printer is used regularly to prevent ink drying; store ink cartridges in a cool environment to extend shelf life.

---

### Section 5: Thermal Printer Technology

**Direct Thermal Printing:**
Direct thermal printers contain only a printhead — a bar of tiny heating elements — and use specially coated heat-sensitive paper. No ink, no ribbon, no toner is used. When the heating elements contact the paper, the chemical coating darkens, creating the image. Receipts, shipping labels, wristbands, and POS transaction records are the most common direct thermal applications.

Key properties of direct thermal paper: the coating is on one side only (typically the shinier or smoother side). If the paper roll is loaded with the uncoated side facing the printhead, the heat produces no visible output and the receipt appears completely blank. This is the single most common direct thermal printer complaint a technician receives. The fix is to flip or reload the paper roll.

Direct thermal output fades when exposed to heat, direct sunlight, prolonged pressure, or contact with certain plastics and chemicals (including some plastic bags and receipt protectors). For long-term archival, laser printing or thermal transfer are more suitable.

**Thermal Transfer Printing:**
Thermal transfer printers use a heated ribbon coated with wax or resin ink. The printhead heats the ribbon, transferring ink to the label or paper. Output is far more durable than direct thermal — resistant to heat, UV exposure, and chemicals. Thermal transfer is used for labels that must survive harsh environments: warehouse barcode labels, outdoor asset tags, and medical specimen labels.

The consumables in a thermal transfer printer are both the ribbon and the label stock. When the ribbon runs out, output becomes faint and eventually blank. Unlike direct thermal, blank output on a thermal transfer printer indicates a depleted or misloaded ribbon.

**Thermal Printer Maintenance:**
Clean the printhead regularly using 99% isopropyl alcohol on a cotton swab — this removes paper dust and adhesive residue that accumulates over time. A contaminated printhead produces faded lines or white voids in output. Replace the printhead when cleaning no longer restores output quality.

---

### Section 6: 3D Printer Technology (FDM)

Fused Deposition Modeling (FDM) is the most common consumer and prosumer 3D printing technology. The printer heats a thermoplastic filament until it melts, extrudes it through a nozzle, and deposits it in layers on a build plate. A slicer software application (such as PrusaSlicer, Cura, or BambuStudio) converts a 3D model file into layer-by-layer G-code instructions that the printer executes.

**Common FDM Filament Types:**

- PLA (Polylactic Acid) — the most beginner-friendly material. Prints at relatively low temperatures (190 to 220°C nozzle, 50 to 60°C bed). Low warping tendency. Biodegradable. Limited heat resistance.
- ABS (Acrylonitrile Butadiene Styrene) — strong, impact-resistant, and heat-tolerant. Requires higher temperatures (220 to 250°C nozzle, 90 to 110°C bed) and an enclosure to prevent warping from uneven cooling. Emits fumes during printing — ventilation required.
- PETG (Polyethylene Terephthalate Glycol) — good balance of strength, flexibility, and ease of printing. More resistant to moisture and chemicals than PLA. Bridges the gap between PLA ease and ABS durability.

**Common FDM Failure Modes:**

- Warping / bed adhesion failure: The print lifts off the build plate at the corners or edges during printing. Caused by thermal contraction of cooling layers creating stress that overcomes bed adhesion. Solutions: heated build plate (increases bed adhesion), enclosure (reduces ambient temperature differential), bed adhesion aids (glue stick, hairspray, PEI sheet), and brim or raft settings in the slicer.
- Clogged nozzle / under-extrusion: The nozzle partially or fully blocks, causing thin, weak, or missing layers. Visual symptom: layers look stringy or have gaps. Solutions: increase print temperature by 5°C (may clear a partial clog), cold pull procedure (heat nozzle, push fresh filament, cool to semi-solid, pull out sharply to drag debris), or replace the nozzle.
- Stringing: Thin strings of filament appear between separate parts of the print. Caused by oozing molten filament during travel moves. Solutions: increase retraction settings in the slicer, lower print temperature, increase travel speed.
- Layer adhesion failure: Layers split apart or are visibly separated. Caused by insufficient temperature, too-fast print speed, or incorrect layer height for the nozzle diameter.

---

### Section 7: Printer Connectivity and Sharing

Printers connect to computers and networks through several methods:

- USB: Direct connection between a printer and a single computer. The most common local printer connection. USB Type-B connector (square with beveled corners) plugs into the printer.
- Ethernet (RJ-45): Wired network connection allowing the printer to serve multiple computers simultaneously. Enterprise printers typically include a built-in Ethernet NIC. The printer receives an IP address (static preferred for network printers) and is added to client computers using its IP address or hostname.
- Wi-Fi (802.11): Wireless network printer connection. Setup typically requires connecting to the printer's built-in web interface or using the printer's control panel to join the Wi-Fi network. Once on the network, behaves identically to an Ethernet-connected printer.
- Bluetooth: Short-range personal printing, typically for mobile devices and photo printers. Not common for office production printers.

When sharing a locally-connected printer from a Windows PC, enable printer sharing in Settings > Printers and Scanners, assign a share name, and connect from other computers using the UNC path (\\computername\sharename) or through the Add Printer wizard.

---

### Section 8: Certification Exam Tips

Tip 1 — The EP process step order is tested directly. Write out the six steps until you can produce them without looking: Cleaning → Charging → Exposing → Developing → Transferring → Fusing. The exam presents the steps out of order and asks you to identify the correct sequence.

Tip 2 — Smearing toner = fuser failure. Faint toner = transfer failure. Memorize these two symptom-to-component mappings. They appear in nearly every printer troubleshooting question set.

Tip 3 — Drum and corona wire components belong to laser printers only. Never assign a drum unit, corona wire, or toner cartridge to an inkjet printer. The A+ exam deliberately presents these as distractor answers in inkjet questions.

Tip 4 — Direct thermal printers have no ink and no ribbon. If a direct thermal printer produces blank output and no error is reported, the paper is almost certainly loaded backward — coated side must face the printhead.

Tip 5 — Thermal transfer printers do use a ribbon. Blank output on a thermal transfer printer indicates a depleted or misloaded ribbon. This is different from direct thermal.

Tip 6 — ABS filament requires a heated bed to prevent warping. The exam presents ABS warping scenarios and expects the answer to reference thermal contraction and heated bed requirements — not layer height or slicer settings.

Tip 7 — Inkjet maintenance: always run the nozzle check before and after a head cleaning cycle. Do not run multiple cleaning cycles without rechecking — excessive cycles waste ink.

Tip 8 — Repeating defects at regular intervals on a laser printer page indicate a contaminated or damaged rotating component. The measurement between repeats equals the circumference of the faulty component.

---

### Required Readings and Videos

Complete the following before attempting the lab:

- Required Reading: Review the printer sections in Professor Messer's CompTIA A+ study notes at professormesser.com. Navigate to the 220-1101 materials and read the sections on the laser EP process, inkjet maintenance procedures, thermal printer types, and 3D printing failure modes.
- Required Video: Watch the printer and imaging video segments in Professor Messer's CompTIA A+ 220-1101 course at professormesser.com. Focus on the EP process step-by-step walkthrough, the laser print quality defect-to-stage mapping table, and the comparison of inkjet versus thermal versus laser technologies.

---

### Study Checklist

- [ ] Write out all six EP process steps in order without looking at notes.
- [ ] State what component is responsible for each EP step (drum, corona wire, laser, developer roller, transfer roller, fuser).
- [ ] Match each print quality symptom to its EP process stage: smearing, faint output, gray background, vertical lines, repeating defects.
- [ ] Describe the nozzle check and head cleaning procedures for inkjet printers.
- [ ] Explain the difference between direct thermal and thermal transfer printers.
- [ ] State the most common cause of blank output on a direct thermal receipt printer.
- [ ] Name three common FDM filament types and their key properties.
- [ ] Describe what causes warping in FDM 3D printing and how to prevent it.
- [ ] Explain how a network printer is shared from a Windows PC and how client computers connect to it.
- [ ] Complete the Module 15 lab activity.

---

## 9. Supplemental Resources

The following free resources supplement Module 15 content on laser printers, inkjet printers, thermal printers, 3D printers, and printer troubleshooting.

1. **Professor Messer — CompTIA A+ Core 1 (220-1101) Printers and Imaging**
   URL: [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/)
   Relevance: Free video lectures covering the complete laser EP process, inkjet maintenance, thermal printer types, 3D printing technologies, and printer troubleshooting symptom mapping — all directly aligned to Domain 3.7 of the A+ Core 1 exam. The EP process step-by-step animation in the video is particularly useful for memorizing stage sequence and component assignments.

1. **HP Support — Laser Printer Troubleshooting Guide (Free Online)**
   URL: [https://support.hp.com/us-en/product/setup-user-guides/hp-laserjet-printers](https://support.hp.com/us-en/product/setup-user-guides/hp-laserjet-printers)
   Relevance: HP publishes free online troubleshooting guides for LaserJet printers that document print quality defects (streaks, ghosting, fading, vertical lines) with component-level root cause analysis. Reviewing real manufacturer defect-diagnosis content reinforces the symptom-to-component mapping approach tested on the A+ exam and used in Lab 15.

1. **Prusa Research — 3D Printing Knowledge Base (Free)**
   URL: [https://help.prusa3d.com/](https://help.prusa3d.com/)
   Relevance: Prusa Research publishes a free, comprehensive 3D printing knowledge base covering FDM printer calibration, filament properties (PLA, PETG, ABS), layer adhesion issues, under-extrusion, warping, stringing, and first layer adjustment. This is one of the most detailed free resources for understanding FDM 3D printing troubleshooting — relevant to the 3D printing content in Module 15 and A+ exam questions about 3D printing failure modes.

1. **Epson — Printhead Maintenance Documentation (Free)**
   URL: [https://epson.com/support](https://epson.com/support)
   Relevance: Epson's free support documentation covers inkjet printhead nozzle check procedures, head cleaning cycles, and alignment procedures for Epson printers. Following a real manufacturer's maintenance workflow provides hands-on context for the inkjet maintenance steps covered in Module 15 and tested on the A+ exam.

1. **CompTIA A+ Exam Objectives (220-1101) Domain 3.7 — Printers and Multifunction Devices**
   URL: [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)
   Relevance: The official CompTIA A+ exam objectives are available as a free PDF download from comptia.org. Domain 3.7 lists every printer technology, maintenance process, and troubleshooting procedure that is within scope for the exam. Comparing the exam objectives to Module 15 content ensures full coverage of all tested printer topics.
