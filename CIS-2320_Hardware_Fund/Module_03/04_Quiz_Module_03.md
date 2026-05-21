# Quiz: Module 03 - Processors (CPUs) and Cooling
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which CPU socket type features pins located on the motherboard rather than the processor itself?
*   A) PGA
*   B) LGA
*   C) BGA
*   D) DIP
*   **Correct Answer:** B) Land Grid Array (LGA) has pins on the socket. Pin Grid Array (PGA) has pins on the CPU.
*   **Distractor Analysis:**
    *   *Why correct:* Land Grid Array (LGA) has pins on the socket. Pin Grid Array (PGA) has pins on the CPU.
    *   BGA is soldered. DIP is an old integrated circuit package format.

---

**Question 2**
In the context of PC hardware, which of the following is the most accurate definition of a **heat sink**?
*   A) A passive cooling component made of aluminum or copper fins that absorbs heat from the CPU and dissipates it into surrounding air, typically paired with a fan connected to the CPU fan header.
*   B) A thermally conductive paste applied between the CPU and cooler to fill microscopic surface imperfections and improve heat transfer efficiency.
*   C) A sensor embedded in the CPU die that monitors operating temperature and signals the BIOS to throttle clock speed or shut down if a thermal threshold is exceeded.
*   D) A liquid cooling block that circulates coolant over the CPU surface to transfer heat to a radiator mounted at a case exhaust vent.
*   **Correct Answer:** A) A passive cooling component made of aluminum or copper fins that absorbs heat from the CPU and dissipates it into surrounding air, typically paired with a fan connected to the CPU fan header.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the heat sink's structure, material, and function as the primary passive heat dissipation component.
    * *Why B is incorrect:* This describes thermal paste, not the heat sink itself.
    * *Why C is incorrect:* This describes a thermal sensor/throttling mechanism built into the CPU, not a heat sink.
    * *Why D is incorrect:* This describes an AIO (All-In-One) liquid cooler cold plate, a different cooling technology.


---

**Question 3**
A technician is installing a CPU cooler and has a large amount of thermal paste left over from a previous job. They apply a thick, full-coverage layer across the entire CPU surface before seating the cooler. What is the most likely consequence of this action?
*   A) The CPU will overheat because excess paste reduces contact pressure between the CPU and cooler
*   B) Excess paste may overflow onto the motherboard socket, potentially shorting nearby circuitry
*   C) The system will refuse to POST because the BIOS detects an incorrect thermal interface thickness
*   D) Performance will improve because more paste creates a thicker thermal barrier
*   **Correct Answer:** B) Excess paste may overflow onto the motherboard socket, potentially shorting nearby circuitry
*   **Distractor Analysis:**
    * *Why B is correct:* Applying too much thermal paste risks it flowing into the CPU socket or onto capacitors when compressed by the cooler, which can cause electrical shorts.
    * *Why A is incorrect:* Excess paste does not reduce contact pressure; the cooler mounting hardware controls that. However, too much paste is still incorrect technique.
    * *Why C is incorrect:* BIOS does not detect thermal paste thickness; it monitors fan speed and temperature sensor readings.
    * *Why D is incorrect:* More paste does not improve performance — a thin, even layer is optimal; excess paste can actually insulate rather than conduct heat.


---

**Question 4**
A user reports that their desktop PC shuts down abruptly after running for about 10 minutes, and the system feels very hot near the CPU area. The PC powers back on after cooling down for several minutes. Which is the most likely cause?
*   A) The power supply unit is failing and cannot sustain load under thermal stress
*   B) The CPU fan has stopped working or is disconnected, causing the CPU to overheat and trigger thermal shutdown
*   C) The RAM modules are incompatible with the motherboard and generating excessive heat
*   D) The hard drive is overheating because it is mounted too close to the CPU cooler
*   **Correct Answer:** B) The CPU fan has stopped working or is disconnected, causing the CPU to overheat and trigger thermal shutdown
*   **Distractor Analysis:**
    * *Why B is correct:* A failed or disconnected CPU fan is the most common cause of thermal shutdown after a short run period; modern CPUs throttle then shut down when TJMax is reached.
    * *Why A is incorrect:* PSU failure typically causes sudden power loss rather than a heat-then-shutdown pattern, and the PSU is not located near the CPU.
    * *Why C is incorrect:* Incompatible RAM causes POST failure or BSODs, not cyclical thermal shutdowns.
    * *Why D is incorrect:* HDDs do not generate enough heat to trigger CPU thermal shutdown, and this symptom pattern does not match drive overheating.


---

**Question 5**
Which of the following best describes the advantage of a CPU with 8 cores and Hyper-Threading (16 threads) compared to a CPU with 4 cores and no Hyper-Threading?
*   A) The 8-core CPU runs at twice the clock speed, making single-threaded tasks faster
*   B) The 8-core CPU can execute more parallel tasks simultaneously, improving performance in multithreaded workloads
*   C) The 8-core CPU uses less power because each core handles fewer instructions per cycle
*   D) The 8-core CPU has a larger L3 cache, which eliminates the need for RAM in most operations
*   **Correct Answer:** B) The 8-core CPU can execute more parallel tasks simultaneously, improving performance in multithreaded workloads
*   **Distractor Analysis:**
    * *Why B is correct:* More cores and threads allow the CPU to handle more simultaneous instruction streams, directly benefiting multitasking, video encoding, virtualization, and server workloads.
    * *Why A is incorrect:* Core count and clock speed are independent specifications; more cores do not imply higher clock speeds.
    * *Why C is incorrect:* More cores generally increase total power draw, not decrease it, as more transistors are switching simultaneously.
    * *Why D is incorrect:* Cache size is a separate specification unrelated to core count; RAM is still required regardless of cache size.

