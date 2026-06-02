# Video Script: Module 15 - Printers and Imaging

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1 — 220-1101)

**Estimated Duration:** 22-24 minutes
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.7 (Printer Types and Technologies), Domain 5.7 (Printer Troubleshooting)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

### Production Notes

> SHOW SLIDE: Title card — "Module 15: Printers and Imaging | CIS-2320 Hardware Fundamentals"
> KEY EXAM TRAP 1: The EP process step order is tested directly. Students commonly place "Cleaning" at the end only — it actually occurs at the beginning of the next cycle AND at the end of the current cycle. The official A+ sequence starts with Cleaning.
> KEY EXAM TRAP 2: Students confuse fuser failure (smearing) with transfer failure (faint/incomplete). The symptom determines the stage: smearing = fusing problem; faint output = transferring problem.
> KEY EXAM TRAP 3: Direct thermal printers have NO ink and NO ribbon. A blank receipt is almost always loaded paper backward — coated side must face the printhead.
> KEY EXAM TRAP 4: Drum units and corona wires belong to LASER printers only. Never assign these components to inkjet printers on the exam.
> PRODUCTION NOTE: Display the six EP steps as a persistent on-screen graphic throughout Section 2. Highlight the active step in each explanation. This visual reinforcement is critical for retention.

---

### [00:00 - 03:30] Section 1: Introduction and Module Overview

SHOW SLIDE: "Module 15 Overview — Printer Technologies and the EP Process"

"Welcome back, everyone. This is Module 15 of CIS-2320 Hardware Fundamentals at Texas Wesleyan University, and today we are covering printers and imaging devices. This is one of the most heavily tested hardware topics on the CompTIA A+ Core 1 exam. Domain 3.7 covers printer types, and printer troubleshooting questions appear throughout both Core 1 and Core 2.

Here is our agenda for today. We will start with the laser printing electrophotographic process — the six-step EP cycle that you absolutely must know in order and by function. Then we will cover inkjet printers — how they work and what maintenance they require. After that, thermal printers — direct thermal and thermal transfer, and the one failure that catches every first-year technician off guard. Then 3D printing with FDM technology — the A+ exam expects you to know the common failure modes. And finally, we will connect all of this to print quality troubleshooting — matching symptoms to the component or process step that failed.

SHOW SLIDE: "CompTIA A+ Domains: 3.7 Printer Technologies | 5.7 Printer Troubleshooting"

I want to set your expectations for the exam correctly. Laser printer questions are the most numerous printer questions on the A+ exam. The EP process six steps, the components involved in each step, and the print quality defects that map to each step — those are the high-value items. Know them cold. Everything else builds on that foundation."

---

### [03:30 - 10:00] Section 2: The Laser Printing EP Process — All Six Steps

SHOW SLIDE: "The Electrophotographic (EP) Process — Six Steps" (persistent graphic, highlight each step as discussed)

"Let us walk through the complete laser printing EP process. I want you to understand what is physically happening at each step, because that is what allows you to diagnose failures from symptoms.

SHOW SLIDE: Step 1 — Cleaning (highlighted)

Step 1 is Cleaning. Before the drum can be used for a new page, any residual toner from the previous print cycle must be removed. A rubber cleaning blade scrapes the drum surface, and a cleaning roller or brush removes any remaining particles. The drum must be clean and uniformly prepared before charging. A useful exam reminder: Cleaning happens at the start of each new cycle, not just at the end. That is why some textbooks also list it after Fusing — it is the same cleaning step, just described from a different point in the cycle.

SHOW SLIDE: Step 2 — Charging (highlighted)

Step 2 is Charging. A primary corona wire or, in modern printers, a charge roller applies a uniform high-voltage negative charge across the entire surface of the photosensitive drum. Think of this as painting the drum with a uniform layer of static electricity. The drum now carries an even negative charge everywhere. No image has been written yet — the drum is a uniformly charged blank slate.

SHOW SLIDE: Step 3 — Exposing / Writing (highlighted)

Step 3 is Exposing, also called Writing. The laser assembly — a laser diode and a rotating mirror — scans across the drum and selectively discharges areas that correspond to the image being printed. Wherever the laser hits, it neutralizes the negative charge, creating a relatively positive area. The result is a latent (invisible) image on the drum surface: the areas where toner will stick are now relatively positive, and the background areas remain strongly negative.

SHOW SLIDE: Step 4 — Developing (highlighted)

Step 4 is Developing. The toner cartridge contains negatively charged toner particles. The developer roller brings toner near the drum. Because like charges repel, toner is repelled by the strongly negative background areas. But it is attracted to the relatively positive discharged areas — the latent image — and adheres to them. The latent image is now visible as a toner image on the drum surface.

SHOW SLIDE: Step 5 — Transferring (highlighted)

Step 5 is Transferring. Paper feeds from the tray and passes between the drum and a transfer corona wire or transfer roller. The transfer component applies a positive charge to the paper. Since the paper is now positively charged and the toner particles are negatively charged, the toner is pulled off the drum and onto the paper surface. At this point the toner is sitting on the paper but is not bonded to it — it will smear if touched.

SHOW SLIDE: Step 6 — Fusing (highlighted)

Step 6 is Fusing. The paper passes through the fuser assembly, which consists of a heated roller and a pressure roller. The heat melts the thermoplastic toner particles, and the pressure bonds the melted toner into the fibers of the paper. After fusing, the toner is permanently part of the page and cannot be rubbed off. This is why laser-printed pages exit the printer warm.

SHOW SLIDE: "Mnemonic — Could Children Ever Do That Fast?"

Here is the mnemonic I give all my students. The first letter of each step: Cleaning, Charging, Exposing, Developing, Transferring, Fusing. Could Children Ever Do That Fast? Say it a few times. You will have this sequence memorized before the lab."

---

### [10:00 - 14:30] Section 3: Laser Printer Components and Print Quality Troubleshooting

SHOW SLIDE: "EP Process Stage → Print Quality Symptom Mapping"

"Now let us connect each EP process stage to the print quality symptoms that appear when it fails. This is the exam application of everything we just covered.

If the Charging step fails — specifically if the primary corona wire or charge roller is dirty or damaged — the drum does not receive a uniform charge. The result is faded print quality across the page, or dark streaks if the component is dirty in one spot. The background areas do not repel toner properly, so you get a gray or dirty background on the printed page.

If the Exposing step fails — the laser diode is failing or the scanning mirror is dirty — the laser cannot properly write the latent image. You see missing sections of text, blank horizontal bands, or in severe cases a completely blank page.

If the Developing step fails — toner is clumped, bridged at the developer roller, or the toner is depleted — you see faded output, missing colors in a color printer, or random light and dark patches.

If the Transferring step fails — the transfer roller is worn or the transfer corona wire is contaminated — the toner does not fully transfer from the drum to the paper. The result is faint, incomplete, or uneven output. This is the smear-versus-faint distinction I want you to internalize: transfer failure produces faint or incomplete output, not smearing.

If the Fusing step fails — the fuser heater is not reaching temperature, or the pressure rollers are worn — toner is not bonded to the paper. The symptom is output that smears when you rub your finger across it. The print may look correct at a distance but the toner rubs right off. Fuser failure equals smearing. Transfer failure equals faint. Know this distinction cold.

SHOW SLIDE: "Repeating Defects — Drum Rotation Pattern"

One more troubleshooting pattern worth memorizing. If a defect — a dot, a smear, a line — repeats at regular intervals down the page, the interval corresponds to the circumference of a rotating component. A defect repeating every 94 mm is likely on the drum. A defect repeating at a different interval points to a different roller. This is how a technician narrows down which internal component carries a contamination spot without disassembling the printer."

---

### [14:30 - 18:30] Section 4: Inkjet, Thermal, and 3D Printer Technologies

SHOW SLIDE: "Inkjet Printers — How They Work"

"Let us move to inkjet printers. Inkjet printers spray microscopic droplets of liquid ink through an array of tiny nozzles onto paper. Two nozzle technologies exist: thermal inkjet, where a tiny heating element vaporizes ink to create a bubble that forces a droplet out; and piezoelectric inkjet, where a crystal flexes to push ink through the nozzle. The A+ exam does not go deep on inkjet physics — what it does test is inkjet maintenance.

The primary maintenance issue with inkjets is clogged nozzles. When a printer sits unused, ink dries in the nozzles and blocks them. The printer driver includes two maintenance tools: a nozzle check, which prints a test pattern so you can see which nozzles are clogged; and a head cleaning utility, which forces ink through the nozzles to clear the blockage. The exam tip here is that running too many cleaning cycles wastes ink, but not enough leaves print quality degraded. A professional technician runs the nozzle check first to confirm the problem, runs one cleaning cycle, then re-runs the nozzle check before running another cycle.

SHOW SLIDE: "Thermal Printers — Direct Thermal vs Thermal Transfer"

Thermal printers come in two types. Direct thermal printers use heat-sensitive paper coated with a chemical that darkens when exposed to the printhead's heat. No ink, no ribbon, no toner. Receipt printers and shipping label printers are the most common direct thermal devices. The most common failure a technician encounters is blank output — the paper roll loaded with the uncoated side facing the printhead. The fix is simply to reload the roll with the coated side facing the printhead.

Direct thermal printouts fade when exposed to heat, direct sunlight, or certain chemicals. Storing thermal receipts in a hot car or in contact with certain plastics causes them to turn dark and become unreadable.

Thermal transfer printers use a heated ribbon to transfer ink onto the paper or label stock. Output is more durable and resistant to heat and fading. Thermal transfer is used for labels that need to survive harsh environments — shipping, industrial, and medical settings.

SHOW SLIDE: "3D Printing — FDM Technology"

3D printing with FDM technology — Fused Deposition Modeling — builds objects layer by layer by melting a thermoplastic filament and extruding it through a heated nozzle onto a build plate. The A+ exam tests the most common failure modes.

A clogged nozzle produces under-extrusion — thin, weak, or missing layers. The fix is a cold pull: heating the nozzle, pushing fresh filament through, then pulling it out cold to drag debris out of the nozzle.

Warping occurs when the print lifts off the build plate during printing. The cause is uneven cooling — the bottom layers cool and contract before the upper layers are deposited. ABS filament is especially prone to warping and requires a heated build plate, typically 90 to 110 degrees Celsius, and ideally an enclosed printer. PLA is more forgiving but still benefits from a heated bed.

Under-extrusion from feed gear slippage produces gaps in layers throughout the print. Over-extrusion from incorrect filament diameter settings or too-high flow rate produces blobs and stringing between features."

---

### [18:30 - 22:00] Section 5: Printer Connectivity, Maintenance, and Module Summary

SHOW SLIDE: "Printer Connectivity Options"

"Let us quickly cover printer connectivity because this comes up in both setup and troubleshooting scenarios. Printers connect to computers via USB (most common for local single-computer connections), Ethernet (wired network printers in office environments), Wi-Fi (wireless network printers), and Bluetooth (short-range personal use). Network printers are shared through a print server — which can be a dedicated device, a router with print server functionality, or a Windows PC with print sharing enabled.

When a network print queue stops working, the technician checks the printer's IP address first — if the printer received a new DHCP address, existing print queue configurations pointing to the old IP will fail. Assigning a static IP to network printers is a best practice that prevents this class of failure.

SHOW SLIDE: "Printer Maintenance Summary by Type"

A quick maintenance summary by printer type. Laser printers: replace toner cartridge when output fades and the cartridge cannot be redistributed by shaking; replace drum unit on a mileage schedule per manufacturer specification; clean the inside of the printer and the paper path periodically. Inkjet printers: run nozzle check and head cleaning when print quality degrades; replace cartridges when ink depletes; clean the paper feed rollers if paper misfeeds increase. Thermal printers: clean the printhead with isopropyl alcohol and a cotton swab periodically; replace the paper roll before it runs out — a pink or red stripe on the paper indicates the roll is nearly depleted.

SHOW SLIDE: "Module 15 Summary"

Let me bring it all together. The laser EP process: Cleaning → Charging → Exposing → Developing → Transferring → Fusing. Smearing output means fuser failure. Faint output means transfer failure. Repeating defects at regular intervals indicate a contaminated drum or roller at that circumference interval.

Inkjet: clogged nozzles are the primary maintenance concern — use the nozzle check before and after cleaning cycles. Thermal: direct thermal has no ink or ribbon — blank output usually means paper is loaded backward. 3D FDM: warping means cooling management is needed; clogged nozzle means under-extrusion.

For this week's lab you are going to sequence the EP process steps, match print quality symptoms to the responsible EP stage, and complete a printer maintenance checklist. That work maps directly to the exam questions you will see on the A+ Core 1.

SHOW SLIDE: End Card — "Texas Wesleyan University | CIS-2320 | Professor Nash"

Thank you for watching Module 15. Review the EP process mnemonic until you can recite it without looking, then tackle the quiz. See you in the discussion forum."

---

### Additional Resources

For further study on the topics covered in this module, visit:

- Professor Messer's free CompTIA A+ Core 1 study materials at professormesser.com — navigate to the 220-1101 course and review the printer section covering the laser EP process with step-by-step explanations, inkjet maintenance, thermal printers, and 3D printing failure modes.
- The official CompTIA A+ exam objectives document at comptia.org — review Domain 3.7 for the complete list of printer technologies and Domain 5.7 for printer troubleshooting topics tested on the 220-1101 exam.
