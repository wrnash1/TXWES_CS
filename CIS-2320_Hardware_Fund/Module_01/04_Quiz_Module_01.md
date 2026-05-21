# Quiz: Module 01 - Introduction to PC Hardware & Safety
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What is the primary danger when working inside a computer case without ESD safety?
*   A) Electric shock to the user
*   B) Electrostatic discharge damaging components
*   C) Setting the case on fire
*   D) Damaging the hard drive platter
*   **Correct Answer:** B) ESD can ruin integrated circuits without the user even noticing a spark.
*   **Distractor Analysis:**
    *   *Why correct:* ESD can ruin integrated circuits without the user even noticing a spark.
    *   PSUs store charge, but normal components pose ESD risk to the PC, not electrical shock to the user.

---

**Question 2**
In the context of PC hardware safety, which of the following is the most accurate definition of **grounding**?
*   A) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   B) The process of installing a CPU into its socket and securing it with a retention lever or load plate.
*   C) A method of formatting a hard drive so that all sectors are wiped and the partition table is reset to defaults.
*   D) The technique of re-applying thermal paste between a processor and its heat sink to restore proper heat transfer.
*   **Correct Answer:** A) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Distractor Analysis:**
    * *Why A is correct:* This is the exact definition of grounding as it applies to ESD safety and PC hardware work.
    * *Why B is incorrect:* This describes CPU installation, not grounding.
    * *Why C is incorrect:* This describes low-level disk formatting, an unrelated storage procedure.
    * *Why D is incorrect:* This describes thermal paste application, a cooling procedure not related to grounding.


---

**Question 3**
A technician opens a desktop PC and notices the system powers on but immediately shuts off after a few seconds. Which component is most likely responsible for this thermal-protection shutdown?
*   A) RAM module seated in the wrong slot
*   B) CPU fan not connected to the 4-pin fan header
*   C) SATA data cable disconnected from the hard drive
*   D) PCIe graphics card inserted into an x1 slot instead of x16
*   **Correct Answer:** B) CPU fan not connected to the 4-pin fan header
*   **Distractor Analysis:**
    * *Why B is correct:* Without a CPU fan signal, BIOS/UEFI triggers an immediate thermal shutdown to protect the processor.
    * *Why A is incorrect:* Wrong RAM slot placement causes POST failure or no boot, not a thermal shutdown.
    * *Why C is incorrect:* A disconnected SATA data cable causes a missing OS error, not a shutdown.
    * *Why D is incorrect:* A card in the wrong slot may reduce performance but typically does not cause immediate shutdown.


---

**Question 4**
While handling a RAM module, a technician notices a small visible spark from their fingertip to the DIMM's edge connector. Which of the following best describes the risk this event poses?
*   A) The RAM module may have been permanently damaged by electrostatic discharge, even if it appears physically undamaged.
*   B) The spark indicates the RAM is incompatible with the motherboard and should be returned.
*   C) This is a normal occurrence and does not affect the functionality of the RAM module.
*   D) The spark confirms the RAM module has correct voltage and is properly charged for installation.
*   **Correct Answer:** A) The RAM module may have been permanently damaged by electrostatic discharge, even if it appears physically undamaged.
*   **Distractor Analysis:**
    * *Why A is correct:* A visible ESD spark can exceed thousands of volts and permanently destroy CMOS circuits on the module.
    * *Why B is incorrect:* Compatibility is determined by specification, not by ESD events.
    * *Why C is incorrect:* ESD is never a "normal occurrence" during hardware handling; it always poses a damage risk.
    * *Why D is incorrect:* ESD sparks indicate dangerous charge discharge, not correct voltage levels.


---

**Question 5**
When preparing to work inside a PC case, which of the following represents the correct first step according to PC hardware safety best practices?
*   A) Remove the side panel and immediately begin swapping components to save time.
*   B) Power down the system, unplug the AC power cord, and press the power button to discharge residual capacitor charge.
*   C) Put on an ESD wrist strap before powering down so you are grounded during the shutdown process.
*   D) Turn off the power strip but leave the power cable connected so the PC chassis remains grounded through the outlet.
*   **Correct Answer:** B) Power down the system, unplug the AC power cord, and press the power button to discharge residual capacitor charge.
*   **Distractor Analysis:**
    * *Why B is correct:* Unplugging first eliminates live voltage risk; pressing the power button drains remaining capacitor charge from the motherboard.
    * *Why A is incorrect:* Opening and immediately swapping components without safety steps risks ESD damage and live-voltage exposure.
    * *Why C is incorrect:* The ESD strap should be applied after powering down, not during — and working on a live system is dangerous.
    * *Why D is incorrect:* Leaving the power cable connected keeps the PSU energized and does not make the system safe to work on.

