# Quiz: Module 04 - Memory (RAM) Types and Configuration
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which RAM type is specifically designed for space-constrained laptops and thin clients?
*   A) DIMM
*   B) SODIMM
*   C) SDRAM
*   D) GDDR
*   **Correct Answer:** B) Small Outline Dual Inline Memory Module (SODIMM) is the standard compact form factor for laptop RAM.
*   **Distractor Analysis:**
    *   *Why correct:* Small Outline Dual Inline Memory Module (SODIMM) is the standard compact form factor for laptop RAM.
    *   DIMM is for desktop. GDDR is graphics RAM. SDRAM is the general class of synchronous RAM.

---

**Question 2**
In the context of PC hardware, which of the following most accurately describes the difference between **SODIMM and DIMM**?
*   A) SODIMM modules are approximately 67mm long and designed for laptops and small form factor systems, while full-size DIMMs are approximately 133mm long and used in desktop PCs; both come in DDR4 and DDR5 variants but are not interchangeable.
*   B) SODIMM modules operate at higher voltages than DIMMs, making them faster but less energy-efficient in battery-powered devices.
*   C) DIMMs use a single row of contacts on one side of the module, while SODIMMs use contacts on both sides, doubling their data bus width.
*   D) SODIMM and DIMM refer to the same physical module; the naming difference only indicates whether the RAM is registered (buffered) or unbuffered.
*   **Correct Answer:** A) SODIMM modules are approximately 67mm long and designed for laptops and small form factor systems, while full-size DIMMs are approximately 133mm long and used in desktop PCs; both come in DDR4 and DDR5 variants but are not interchangeable.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the physical size difference, use case, and the fact that the two form factors are not interchangeable despite sharing DDR generations.
    * *Why B is incorrect:* SODIMMs operate at lower or equal voltages compared to DIMMs; DDR4 SODIMMs and DIMMs both run at 1.2V.
    * *Why C is incorrect:* Both DIMM and SODIMM use contacts on both sides; the "dual inline" in both names refers to independent contact rows, not single vs. double sided.
    * *Why D is incorrect:* SODIMM and DIMM are distinct physical form factors with different sizes and pin counts; the distinction is not about buffering.


---

**Question 3**
A technician installs two 8 GB DDR4 DIMMs into a motherboard that supports dual-channel memory. After boot, CPU-Z shows the memory running in single-channel mode. What is the most likely cause?
*   A) The two modules are from different manufacturers, which disables dual-channel
*   B) The modules were installed in adjacent slots (e.g., A1 and A2) instead of paired slots (e.g., A1 and B1)
*   C) DDR4 does not support dual-channel mode; only DDR3 supports this feature
*   D) The total installed RAM exceeds the motherboard's single-channel capacity threshold
*   **Correct Answer:** B) The modules were installed in adjacent slots (e.g., A1 and A2) instead of paired slots (e.g., A1 and B1)
*   **Distractor Analysis:**
    * *Why B is correct:* Dual-channel requires modules in paired (matching channel) slots as defined by the motherboard; adjacent slots typically belong to the same channel.
    * *Why A is incorrect:* Different manufacturers do not prevent dual-channel; matching speed and capacity are what matters.
    * *Why C is incorrect:* DDR4 fully supports dual-channel mode when modules are in the correct paired slots.
    * *Why D is incorrect:* There is no capacity threshold that disables dual-channel; the slot pairing is the only hardware requirement.


---

**Question 4**
A user reports that after upgrading their desktop from 8 GB to 16 GB by adding a second 8 GB DDR4 stick, the system randomly crashes with memory errors. Both sticks are the same brand and speed. What should the technician check first?
*   A) Whether the power supply has enough wattage to support additional RAM
*   B) Whether the new module is seated in the correct dual-channel slot and the locking clips are fully engaged
*   C) Whether the operating system license supports more than 8 GB of RAM
*   D) Whether the SATA data cable needs to be replaced due to interference with the RAM slots
*   **Correct Answer:** B) Whether the new module is seated in the correct dual-channel slot and the locking clips are fully engaged
*   **Distractor Analysis:**
    * *Why B is correct:* Improperly seated RAM is the most common cause of memory errors and instability after an upgrade; the locking clips must snap fully into place.
    * *Why A is incorrect:* RAM draws very little additional power (a few watts per module); a PSU adequate for the original system handles additional RAM easily.
    * *Why C is incorrect:* Windows 10/11 Home supports up to 128 GB; RAM capacity is not a licensing restriction for standard workloads.
    * *Why D is incorrect:* SATA cables route to storage drives and do not interact electrically with RAM slots.


---

**Question 5**
Which of the following correctly identifies how DDR4 and DDR5 DIMMs are physically distinguished from each other to prevent accidental cross-generation installation?
*   A) DDR5 DIMMs are shorter than DDR4 DIMMs, so they will not reach the full length of a DDR4 slot
*   B) DDR5 DIMMs have a different notch position along the bottom edge compared to DDR4, preventing insertion into a DDR4 slot
*   C) DDR5 DIMMs have gold contacts on both sides while DDR4 contacts are only on one side
*   D) DDR5 DIMMs require a locking tab on the top edge of the slot that DDR4 slots do not have
*   **Correct Answer:** B) DDR5 DIMMs have a different notch position along the bottom edge compared to DDR4, preventing insertion into a DDR4 slot
*   **Distractor Analysis:**
    * *Why B is correct:* The key notch position is the physical mechanism that prevents wrong-generation DIMMs from being inserted; DDR3, DDR4, and DDR5 all have distinct notch positions.
    * *Why A is incorrect:* DDR4 and DDR5 DIMMs are both 288-pin modules of the same physical length (133.35mm); length is not the differentiator.
    * *Why C is incorrect:* Both DDR4 and DDR5 DIMMs have gold contacts on both sides; this is not a distinguishing feature between generations.
    * *Why D is incorrect:* There is no top-edge locking tab difference between DDR4 and DDR5 slots; the notch keying mechanism is the standard physical safety feature.

