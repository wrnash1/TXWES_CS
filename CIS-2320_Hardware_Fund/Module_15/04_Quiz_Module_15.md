# Quiz: Module 15 - Printers and Imaging
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What is the correct sequence of steps in the laser printing process?
*   A) Charging, Exposing, Developing, Transferring, Fusing, Cleaning
*   B) Exposing, Charging, Transferring, Fusing, Cleaning, Developing
*   C) Developing, Exposing, Charging, Transferring, Fusing, Cleaning
*   D) Cleaning, Charging, Exposing, Developing, Transferring, Fusing
*   **Correct Answer:** D) The standard sequence is: Cleaning, Charging, Exposing (writing), Developing, Transferring, Fusing.
*   **Distractor Analysis:**
    *   *Why correct:* The standard EP process sequence is Cleaning → Charging → Exposing → Developing → Transferring → Fusing.
    *   The other sequences place the writing (Exposing) or Cleaning steps out of order relative to how the drum must be prepared.

---

**Question 2**
In the context of printer technology, which of the following most accurately describes **inkjet maintenance**?
*   A) The process of clearing clogged print head nozzles using the printer driver's built-in nozzle check and head cleaning utilities, which force ink through blocked nozzles; running too many cleaning cycles wastes ink, while insufficient cleaning leaves print quality degraded.
*   B) The process of replacing the drum unit and primary corona wire in an inkjet printer on a fixed mileage schedule to prevent ink overspray from contaminating the charging circuit.
*   C) The process of recalibrating the inkjet printer's fuser temperature and pressure roller gap after every third toner cartridge replacement to prevent smearing on glossy paper stock.
*   D) The process of degaussing the print head carriage motor using a magnetic calibration tool after an inkjet printer has been moved to a new location to re-establish accurate motor step positioning.
*   **Correct Answer:** A) The process of clearing clogged print head nozzles using the printer driver's built-in nozzle check and head cleaning utilities, which force ink through blocked nozzles; running too many cleaning cycles wastes ink, while insufficient cleaning leaves print quality degraded.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes inkjet maintenance as tested on the CompTIA A+ exam — nozzle clogging from dried ink is the primary maintenance issue, addressed by the nozzle check and head cleaning functions in the printer driver.
    * *Why B is incorrect:* Drum units and corona wires are components of laser printers, not inkjet printers; inkjet printers do not have a charging circuit or photosensitive drum.
    * *Why C is incorrect:* Fusers are components of laser printers; inkjet printers do not use fuser assemblies or toner cartridges and have no fuser temperature settings.
    * *Why D is incorrect:* Degaussing is a procedure used to neutralize magnetic fields in CRT monitors and certain storage media; it is not a real inkjet maintenance procedure and carriage motor calibration, if needed, is performed through the driver software, not a physical magnetic tool.


---

**Question 3**
A laser printer is producing pages with toner that smears when touched and rubs off easily. The print is otherwise clear and properly positioned on the page. Which step of the EP process is most likely failing?
*   A) The Charging step is failing — the primary corona wire is not applying sufficient negative charge to the drum, causing toner to adhere loosely
*   B) The Transferring step is failing — the transfer roller is not pulling toner completely off the drum onto the paper, leaving excess toner unattached
*   C) The Fusing step is failing — the fuser assembly is not applying sufficient heat or pressure to permanently bond the toner particles into the paper fibers
*   D) The Exposing step is failing — the laser is not writing the image correctly, causing toner particles to attach to unintended areas of the drum that smear during output
*   **Correct Answer:** C) The Fusing step is failing — the fuser assembly is not applying sufficient heat or pressure to permanently bond the toner particles into the paper fibers
*   **Distractor Analysis:**
    * *Why C is correct:* Toner that smears when touched is the classic symptom of a failing fuser; the toner has been transferred to the paper but not melted and bonded into the fibers. The fuser assembly uses a heated roller and pressure roller to accomplish this — if either fails, smearing results.
    * *Why A is incorrect:* A charging failure typically produces faded or blank pages because toner cannot attach properly to a poorly charged drum; it does not produce legible but smearing output.
    * *Why B is incorrect:* A transfer roller failure would produce faded or incomplete image transfer — missing portions of the image — not a fully visible image that smears after printing.
    * *Why D is incorrect:* An exposing failure produces incorrect or missing print content (wrong characters, missing sections, or blank pages) because the latent image is not correctly written; it does not produce smearing of otherwise correct output.


---

**Question 4**
A receipt printer at a point-of-sale terminal is producing blank receipts even though the paper roll appears to be loaded correctly and the printer reports no errors. What is the most likely cause?
*   A) The print head needs to be replaced because direct thermal print heads burn out after approximately 500,000 lines of printing and must be replaced on a fixed schedule
*   B) The paper roll is loaded backwards — thermal paper has a heat-sensitive coating on only one side, and the coated side must face the print head to produce output
*   C) The receipt printer's ink ribbon is depleted and must be replaced; without a ribbon the thermal print head cannot transfer ink to the paper surface
*   D) The receipt printer driver needs to be reinstalled because blank output always indicates a corrupted driver that is sending empty print data to the device
*   **Correct Answer:** B) The paper roll is loaded backwards — thermal paper has a heat-sensitive coating on only one side, and the coated side must face the print head to produce output
*   **Distractor Analysis:**
    * *Why B is correct:* Direct thermal printers have no ink or ribbon; output is produced when heat from the print head contacts the chemically treated side of the paper. If the roll is loaded with the uncoated side facing the head, the heat produces no visible marking and the output is blank.
    * *Why A is incorrect:* While thermal print heads do have a finite lifespan, failure is not on a fixed 500,000-line schedule and presents as degraded or partial output, not completely blank output on an otherwise functioning printer reporting no errors.
    * *Why C is incorrect:* Direct thermal printers do not use ink ribbons; the absence of a ribbon is the normal operating state, not a failure condition. Thermal transfer printers use ribbons, but those are a different printer type.
    * *Why D is incorrect:* A corrupted driver would typically cause the printer to report errors, fail to receive jobs, or produce garbled output — a driver issue does not specifically cause perfectly blank output on a functional direct thermal printer with no reported errors.


---

**Question 5**
A 3D printer using FDM technology is producing prints that warp and detach from the build plate partway through the print job. The filament type is ABS. What is the most likely cause and correct fix?
*   A) The nozzle temperature is set too high, causing the ABS to melt too quickly and pool on the build plate before it can solidify into the correct layer shape
*   B) ABS filament shrinks as it cools and requires a heated build plate and an enclosure to maintain ambient temperature; warping is caused by uneven cooling creating stress that lifts edges off the plate
*   C) The slicer software has incorrectly calculated the layer height and is commanding layers that are too thick for ABS, which causes adhesion failure between layers rather than bed adhesion failure
*   D) The filament spool is loaded in the wrong direction on the extruder, causing the motor to pull against the filament coil tension and underextrude material at the corners of each layer
*   **Correct Answer:** B) ABS filament shrinks as it cools and requires a heated build plate and an enclosure to maintain ambient temperature; warping is caused by uneven cooling creating stress that lifts edges off the plate
*   **Distractor Analysis:**
    * *Why B is correct:* ABS has a high thermal shrinkage rate and is notoriously prone to warping when printed in ambient air; it requires a heated bed (typically 90–110°C) and ideally an enclosed printer to prevent the rapid cooling that causes differential contraction and lifting. This is a well-known material property tested in A+ printer troubleshooting scenarios.
    * *Why C is incorrect:* Layer height settings affect print quality and layer adhesion strength, but excessive layer height does not specifically cause the corner-lifting and plate detachment pattern characteristic of warping; warping is a thermal stress phenomenon, not a layer thickness problem.
    * *Why D is incorrect:* Filament spool direction does not affect extrusion direction or motor behavior in a meaningful way on properly designed FDM printers; underextrusion from feed tension would produce gaps in layers throughout the print, not corner warping at the build plate.
