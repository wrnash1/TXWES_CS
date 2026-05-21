# Quiz: Module 02 - Motherboards and Form Factors
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which form factor is typically used for compact, small-form-factor home theatre PCs?
*   A) ATX
*   B) Micro-ATX
*   C) Mini-ITX
*   D) BTX
*   **Correct Answer:** C) Mini-ITX motherboard dimensions (6.7 x 6.7 inches) make it perfect for compact devices.
*   **Distractor Analysis:**
    *   *Why correct:* Mini-ITX motherboard dimensions (6.7 x 6.7 inches) make it perfect for compact devices.
    *   ATX is full size. Micro-ATX is medium. BTX is an outdated form factor.

---

**Question 2**
In the context of PC hardware, which of the following is the most accurate definition of a motherboard **chipset**?
*   A) A group of integrated circuits on the motherboard that manages data flow between the CPU, RAM, storage, and expansion slots, determining CPU compatibility and available features.
*   B) The set of firmware instructions stored in a flash chip that initializes hardware components and launches the boot process when a PC is powered on.
*   C) A physical connector on the motherboard that accepts expansion cards such as graphics cards and network adapters, providing a direct high-speed link to the CPU.
*   D) The collection of copper traces on the motherboard that carries power and data signals between sockets, slots, and onboard controllers.
*   **Correct Answer:** A) A group of integrated circuits on the motherboard that manages data flow between the CPU, RAM, storage, and expansion slots, determining CPU compatibility and available features.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the chipset's role as the traffic controller between all major board subsystems.
    * *Why B is incorrect:* This describes the BIOS/UEFI firmware, which is stored separately in a flash chip.
    * *Why C is incorrect:* This describes a PCIe expansion slot, not the chipset.
    * *Why D is incorrect:* This describes the PCB trace layout, a physical feature of the board rather than the chipset.


---

**Question 3**
A technician needs to install a graphics card into a desktop PC. The motherboard has PCIe x1, x4, and x16 slots available. Which slot should be used?
*   A) PCIe x1 — it uses the least bandwidth, leaving more for other components
*   B) PCIe x4 — it provides balanced bandwidth for both GPU and CPU tasks
*   C) PCIe x16 — it provides the maximum bandwidth required for GPU operation
*   D) Any slot works equally well since PCIe is fully interchangeable
*   **Correct Answer:** C) PCIe x16 — it provides the maximum bandwidth required for GPU operation
*   **Distractor Analysis:**
    * *Why C is correct:* Graphics cards require a PCIe x16 slot for full performance; this slot provides the highest bandwidth (up to 32 GB/s with PCIe 4.0).
    * *Why A is incorrect:* PCIe x1 slots lack the physical length and bandwidth to seat or run a modern GPU.
    * *Why B is incorrect:* PCIe x4 provides insufficient bandwidth for a dedicated GPU and the card may not physically fit.
    * *Why D is incorrect:* PCIe slots are physically keyed by length — a GPU requires x16 and will not insert into smaller slots.


---

**Question 4**
A technician replaces a motherboard in a desktop PC but the system no longer boots and shows an incorrect date and time on every startup. Which component is most likely missing or failed?
*   A) The CPU thermal paste was not reapplied during the board swap
*   B) The CMOS battery was not transferred to the new board or is dead
*   C) The RAM was not reseated after the motherboard was installed
*   D) The PCIe graphics card is not fully inserted into the x16 slot
*   **Correct Answer:** B) The CMOS battery was not transferred to the new board or is dead
*   **Distractor Analysis:**
    * *Why B is correct:* The CMOS battery (CR2032) maintains BIOS/UEFI settings including date, time, and boot order when the PC is unplugged. A missing or dead battery causes these settings to reset on every power loss.
    * *Why A is incorrect:* Missing thermal paste causes CPU overheating and shutdown, not incorrect date/time.
    * *Why C is incorrect:* Improperly seated RAM causes POST failure or no-boot errors, not clock reset.
    * *Why D is incorrect:* A loose GPU causes display issues, not BIOS setting loss.


---

**Question 5**
When designing a system for **Motherboards and Form Factors**, a customer needs a board that fits in a standard ATX case but wants to save money by using a smaller board with fewer expansion slots. Which form factor best meets this requirement?
*   A) Mini-ITX — smallest available form factor and lowest cost
*   B) Micro-ATX — smaller than ATX but backward-compatible with ATX cases and less expensive
*   C) E-ATX — extended ATX provides more slots at a lower price point
*   D) BTX — the BTX standard replaced ATX for budget builds
*   **Correct Answer:** B) Micro-ATX — smaller than ATX but backward-compatible with ATX cases and less expensive
*   **Distractor Analysis:**
    * *Why B is correct:* Micro-ATX boards fit in standard ATX cases and typically cost less due to fewer layers and fewer slots, making them ideal for budget builds.
    * *Why A is incorrect:* Mini-ITX requires a specific small case and does not fit a standard ATX chassis without an adapter.
    * *Why C is incorrect:* E-ATX is larger and more expensive than standard ATX; it is designed for workstation and enthusiast builds.
    * *Why D is incorrect:* BTX is an obsolete form factor abandoned by most manufacturers; it does not represent a current budget option.

