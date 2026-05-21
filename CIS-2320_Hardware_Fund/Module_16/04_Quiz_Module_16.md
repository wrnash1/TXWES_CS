# Quiz: Module 16 - Final Exam Preparation
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
A technician is asked to select a cable that supports 10 Gbps over an 80-meter horizontal run to a new workstation. Which cable category is required?
*   A) Cat5e
*   B) Cat6
*   C) Cat6a
*   D) Cat3
*   **Correct Answer:** C) Cat6a supports 10 Gbps at up to 100 meters. Cat6 supports 10 Gbps only up to 55 meters, making it insufficient for an 80-meter run.
*   **Distractor Analysis:**
    *   *Why correct:* Cat6a supports 10 Gbps at the full 100-meter standard run. Cat6 falls back to 1 Gbps at distances beyond 55 meters.
    *   Cat5e is limited to 1 Gbps. Cat3 is a legacy 10 Mbps standard.

---

**Question 2**
In the context of PC hardware, which of the following most accurately describes **the CompTIA A+ seven-step troubleshooting methodology**?
*   A) A structured problem-solving process: identify the problem, establish a theory of probable cause, test the theory, establish a plan of action, implement the solution, verify full system functionality, and document findings — applied to all hardware and software troubleshooting scenarios.
*   B) A seven-step software development cycle used to build enterprise applications: requirements, design, coding, testing, deployment, maintenance, and decommission — adapted for IT support ticket resolution workflows.
*   C) A seven-layer network reference model (Physical, Data Link, Network, Transport, Session, Presentation, Application) used to isolate which layer of a network stack is causing a connectivity failure.
*   D) A set of seven BIOS/UEFI diagnostic codes that correspond to POST failure stages, where each numbered code maps to a specific hardware component that failed during power-on self-test.
*   **Correct Answer:** A) A structured problem-solving process: identify the problem, establish a theory of probable cause, test the theory, establish a plan of action, implement the solution, verify full system functionality, and document findings — applied to all hardware and software troubleshooting scenarios.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the CompTIA A+ official troubleshooting methodology as defined in the exam objectives; all seven steps and their correct sequence are tested in scenario-based questions on both Core 1 and Core 2.
    * *Why B is incorrect:* This describes a software development lifecycle (SDLC), not a hardware troubleshooting methodology; the A+ exam tests a specific seven-step process for diagnosing and resolving IT problems, not software project management.
    * *Why C is incorrect:* This describes the OSI model — a networking reference model with seven layers — which is a separate concept used for network troubleshooting, not the general A+ hardware troubleshooting methodology.
    * *Why D is incorrect:* POST error codes are BIOS-specific numeric or beep code indicators for hardware failures; while they are part of hardware diagnostics, they are not the seven-step troubleshooting methodology.


---

**Question 3**
A technician is building a workstation and installs two 16 GB DDR4 RAM modules. After boot, the system only reports 32 GB of RAM but the performance in memory-intensive tasks is lower than expected for a dual-channel configuration. Upon inspection, both modules are installed in slots A1 and A2 (adjacent slots). What should the technician do to enable dual-channel operation?
*   A) Install a third RAM module in slot B1 to create a triple-channel configuration, which is required before DDR4 RAM operates at full bandwidth
*   B) Move one module from slot A2 to slot B1 so the two modules occupy the paired A1/B1 slots, which is the correct dual-channel configuration on most motherboards
*   C) Enable XMP (Extreme Memory Profile) in the BIOS, which activates dual-channel mode regardless of which physical slots are used
*   D) Replace both modules with ECC (Error-Correcting Code) RAM, because standard non-ECC DDR4 does not support dual-channel operation on consumer motherboards
*   **Correct Answer:** B) Move one module from slot A2 to slot B1 so the two modules occupy the paired A1/B1 slots, which is the correct dual-channel configuration on most motherboards
*   **Distractor Analysis:**
    * *Why B is correct:* Dual-channel operation requires matching RAM modules to be installed in the correct paired slots as defined by the motherboard — typically A1/B1 or A2/B2, not A1/A2 (same channel). The motherboard manual and color-coded slot indicators show which slots form a dual-channel pair.
    * *Why A is incorrect:* DDR4 consumer platforms use dual-channel (two modules), not triple-channel; triple-channel was associated with older Intel LGA 1366 platforms and is not applicable to standard DDR4 motherboards.
    * *Why C is incorrect:* XMP enables higher RAM speeds (overclocking profiles) stored on the RAM module; it does not activate or control dual-channel operation, which is determined entirely by physical slot placement.
    * *Why D is incorrect:* ECC RAM is a reliability feature used in workstation and server platforms; consumer DDR4 absolutely supports dual-channel operation and ECC is not required for it.


---

**Question 4**
A technician is called to diagnose a laser printer producing pages where the printed text is faint and partially missing, particularly at the edges of the page. The toner cartridge was recently replaced. Which component or EP process step is the most likely cause?
*   A) The fuser assembly is failing — fuser heat causes toner to evaporate before bonding to the paper, producing faint output near the fuser's entry rollers
*   B) The transfer roller or transfer corona wire is worn or failing — insufficient charge transfer pulls toner incompletely from the drum to the paper, producing faint and uneven output
*   C) The laser exposure unit (scanning mirror or laser diode) is dirty — contamination on the mirror scatters the laser beam and prevents full discharge of the drum in affected areas
*   D) The paper tray is loaded with paper that is too thick — high-GSM paper absorbs toner unevenly and always produces faint output regardless of printer condition
*   **Correct Answer:** B) The transfer roller or transfer corona wire is worn or failing — insufficient charge transfer pulls toner incompletely from the drum to the paper, producing faint and uneven output
*   **Distractor Analysis:**
    * *Why B is correct:* The Transferring step uses the transfer roller/corona wire to apply a positive charge to the paper, attracting negatively charged toner from the drum. A worn or weakened transfer component produces insufficient charge, resulting in faint, incomplete toner transfer — especially noticeable at edges where charge may be weakest.
    * *Why A is incorrect:* A failing fuser produces smearing or unfused toner that rubs off the page; it does not cause faint output, because by the transfer stage the toner is already on the paper. Fuser failure affects bonding, not toner deposition.
    * *Why C is incorrect:* A dirty laser mirror would produce consistent missing bands or blank stripes across the width of the page where the beam is blocked; it would not produce generally faint output across the entire page with edge falloff.
    * *Why D is incorrect:* Paper weight/GSM affects media handling and paper jam frequency; it does not cause systematically faint toner output. The printer adjusts fuser temperature for paper type but does not alter toner transfer based on paper thickness.


---

**Question 5**
A user reports that their laptop will not power on at all when pressing the power button, even when the AC adapter is plugged in. The adapter's indicator light is on. A technician swaps the AC adapter with a known-good unit and the problem persists. Which component should the technician suspect next, and what is the correct diagnostic approach?
*   A) Suspect the CPU — a failed CPU prevents the power button circuit from completing; replace the CPU and retest before examining any other components
*   B) Suspect the motherboard DC power jack or the power button circuit — test by attempting to power on with a known-good battery, and inspect the DC jack for physical damage such as broken solder joints or a loose barrel connection
*   C) Suspect the RAM — all laptops require at least one seated RAM module to complete the power-on circuit; remove and reseat the RAM modules and retry the power button
*   D) Suspect the display backlight — a failed backlight causes the laptop to appear off even when running; connect an external monitor to confirm whether the system is actually powering on without a visible internal display
*   **Correct Answer:** B) Suspect the motherboard DC power jack or the power button circuit — test by attempting to power on with a known-good battery, and inspect the DC jack for physical damage such as broken solder joints or a loose barrel connection
*   **Distractor Analysis:**
    * *Why B is correct:* With a confirmed-good AC adapter that is powered (indicator light on) but no laptop response, the fault is either in how the laptop receives that power (DC jack, power rails on motherboard) or in the power button circuit itself. The DC power jack is a common physical failure point on laptops; inspecting for damaged solder joints and testing with a charged battery isolates whether the fault is in the AC input path or internal.
    * *Why A is incorrect:* CPU failure in a laptop does not prevent the power button from completing its circuit; a CPU failure typically results in POST failure or no display output, not a complete no-power state where no fans spin and no indicator lights activate.
    * *Why C is incorrect:* Missing or unseated RAM causes a POST failure with beep codes and no display output — the system still powers on (fans spin, power light activates). It does not cause a complete no-power condition where the system shows zero response to the power button.
    * *Why D is incorrect:* A failed display backlight or even a completely failed display would not prevent the system from powering on; fans would spin, the power LED would activate, and external display output would function. The scenario describes zero response to the power button, which indicates a power delivery problem, not a display problem.
