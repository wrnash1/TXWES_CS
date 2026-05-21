# Reading Guide: Module 15 - Printers and Imaging
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

### Introduction
Welcome to **Module 15 - Printers and Imaging**! This module covers the four major printer technologies a technician encounters — laser, inkjet, thermal, and 3D printers — including how each technology works, what consumables and maintenance each requires, and how to troubleshoot common print quality failures. The laser printing electrophotographic (EP) process is one of the most heavily tested topics on the **CompTIA A+ Core 1 (220-1101)** exam, and printer troubleshooting scenarios appear on both Core 1 and Core 2.

As a technician, you must be able to sequence all six steps of the EP process, explain common laser printer failures by stage, perform inkjet head maintenance, and identify when thermal paper or a 3D printer filament issue is the cause of a problem. Complete the checklist and review all glossary terms before the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **laser printing process (EP process)**: The electrophotographic (EP) laser printing process consists of six steps in sequence: (1) Cleaning — residual toner is scraped from the drum by the cleaning blade; (2) Charging — the primary corona wire or charge roller applies a uniform high-voltage negative charge to the drum surface; (3) Exposing (Writing) — the laser beam discharges selected areas of the drum to form the latent image; (4) Developing — negatively charged toner particles are attracted to the discharged (relatively positive) areas of the drum; (5) Transferring — the transfer corona wire or transfer roller applies a positive charge to the paper, pulling toner from the drum onto the page; (6) Fusing — the fuser assembly uses heat and pressure rollers to permanently melt the toner into the paper fibers. Cleaning occurs both before and after the transfer step to prepare the drum for the next page.
*   **inkjet maintenance**: Inkjet printers use microscopic nozzles to spray liquid ink droplets onto paper. Clogged nozzles are the most common failure, caused by dried ink from periods of inactivity. The printer driver software provides a nozzle check (prints a test pattern to identify clogged nozzles) and a head cleaning utility (forces ink through the nozzles to clear blockages). Running too many cleaning cycles wastes ink; running too few leaves print quality degraded. Inkjet print heads are either integrated into replaceable cartridges (replaced when the cartridge is swapped) or permanently mounted on the carriage (cleaned in place).
*   **thermal paper and thermal printers**: Thermal printers use heat-sensitive paper coated with a chemical that darkens when exposed to heat from the printhead — no ink or toner is required. Direct thermal printing is used for receipts, shipping labels, and POS terminals. Thermal paper fades when exposed to heat, direct sunlight, or certain chemicals; storing thermal printouts near heat sources will cause them to darken and become unreadable. Thermal transfer printers use a heated ribbon to transfer ink onto plain paper or labels and produce more durable output. Receipt printers and label printers are the most common direct thermal devices a technician services.
*   **3D printing**: 3D printers build physical objects layer by layer from digital models. FDM (Fused Deposition Modeling) is the most common consumer type — it heats a thermoplastic filament (PLA, ABS, PETG) and extrudes it through a nozzle onto a build plate. Common failure points include clogged nozzles (requiring cold pulls or needle cleaning), warped prints (caused by build plate adhesion failure or temperature fluctuation), and under/over-extrusion (caused by incorrect filament diameter settings or feed gear slippage). Slicer software converts 3D model files into layer-by-layer G-code instructions for the printer.

---

### 2. Certification Exam Tips
*   **Focus Area (A+ Core 1 — Domain 3.7):** The A+ exam tests the EP process step sequence extensively. The correct order is: Cleaning → Charging → Exposing → Developing → Transferring → Fusing. A useful mnemonic is "Could Children Ever Do That Fast?" Exam questions will present the steps out of order and ask you to identify the correct sequence, or will describe a print quality problem and ask which step failed.
*   **Scenario Trap:** A common A+ scenario describes a laser printer that produces pages with random black lines or specks. The distractor answers include toner cartridge and fuser problems. The correct answer depends on the pattern: vertical black lines running the full page length indicate a scratched or damaged drum (Charging/Developing stage); small random black specks that repeat at regular intervals indicate a worn drum or debris at a specific rotation point. Fuser failure typically produces smearing or unfused toner that rubs off the page.
*   **Study Resource:** Professor Messer's free A+ Core 1 course covers the laser EP process with step-by-step animation-style explanations, along with inkjet, thermal, and 3D printer comparisons. Navigate to the printer section: [Professor Messer's CompTIA A+ Core 1 Course — Printers](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Memorize the EP process step order and the print quality defect-to-stage mapping before the exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the printers and imaging sections in the OER study guide: [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections on the laser EP process, inkjet maintenance, thermal printers, and 3D printing technologies.
*   **Required Video:** Watch the video lecture on printers and imaging from the official free course playlist: [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2). Focus on segments covering the EP process step sequence, laser print quality troubleshooting by stage, and the comparison of inkjet, thermal, and laser technologies.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Replace the toner cartridge in a laser printer**: Open the printer's front or top access panel. Remove the spent toner cartridge by releasing the locking mechanism. Before inserting the new cartridge, gently rock it side to side to distribute toner evenly. Remove the protective tape seal, insert the cartridge until it clicks, and close the panel. Print a test page to confirm the replacement was successful.
*   **Clean ink nozzles using the software maintenance utility**: Open the printer driver properties on a PC with an inkjet printer connected. Navigate to the Maintenance or Tools tab. Run the Nozzle Check to print a pattern identifying clogged nozzles. If gaps appear in the test pattern, run the Head Cleaning utility. Repeat the nozzle check after cleaning to confirm improvement. Document how many cleaning cycles were needed.
*   **Configure a network print queue and share it**: On a Windows PC connected to a printer, open Settings > Printers & Scanners. Select the printer and enable sharing. Assign a share name. From a second PC on the same network, add the printer using the Add Printer wizard, selecting the network/shared printer option and entering the UNC path (\\computername\printershare). Print a test page from the second PC to confirm the shared queue is functional.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the printers and imaging sections in [Professor Messer's CompTIA A+ Study Notes](https://www.professormesser.com/).
- [ ] Watch the video lecture on printers and imaging in [Professor Messer's CompTIA A+ 220-1101 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnqI_Hsd0upV30E8dK32yVq2).
- [ ] Review the printer maintenance steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
