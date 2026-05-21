# Quiz: Module 06 - Power Supplies and System Cooling
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What standard power connector is used to supply direct auxiliary power to high-end PCIe graphics cards?
*   A) 24-pin ATX
*   B) SATA Power
*   C) 6-pin or 8-pin PCIe
*   D) 4-pin Molex
*   **Correct Answer:** C) PCIe graphics cards use 6-pin or 8-pin auxiliary cables to draw up to 150W of power.
*   **Distractor Analysis:**
    *   *Why correct:* PCIe graphics cards use 6-pin or 8-pin auxiliary cables to draw up to 150W of power.
    *   24-pin is for motherboard. SATA is for storage. Molex is for legacy accessories.

---

**Question 2**
In the context of PC hardware, which of the following most accurately describes **case airflow (intake vs exhaust)**?
*   A) The directional movement of air through a PC case where intake fans draw cool air in (typically front/bottom) and exhaust fans push hot air out (typically rear/top), creating a front-to-back, bottom-to-top thermal path across components.
*   B) The process of measuring the voltage differential between the PSU's 12V and 5V rails to determine whether airflow regulators are operating within acceptable tolerances.
*   C) A BIOS setting that controls fan speed curves based on CPU temperature readings, automatically adjusting RPM to balance noise and thermal performance.
*   D) The circulation of coolant fluid through a closed-loop AIO liquid cooling system, where intake refers to the pump inlet and exhaust refers to the radiator outlet.
*   **Correct Answer:** A) The directional movement of air through a PC case where intake fans draw cool air in (typically front/bottom) and exhaust fans push hot air out (typically rear/top), creating a front-to-back, bottom-to-top thermal path across components.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the airflow concept — the physical direction of fan-driven air movement through the case chassis.
    * *Why B is incorrect:* This describes voltage rail measurement, a PSU diagnostic procedure unrelated to airflow direction.
    * *Why C is incorrect:* This describes a fan speed/PWM control feature in BIOS, not the physical concept of intake vs. exhaust airflow.
    * *Why D is incorrect:* This describes AIO liquid cooling loop terminology, not general case airflow strategy.


---

**Question 3**
A technician is building a PC and estimates the total system power draw at 420W under full load. Which PSU wattage provides adequate headroom while following best practices?
*   A) 430W — just above the estimated load is sufficient for normal operation
*   B) 500W — provides approximately 20% headroom above the estimated draw
*   C) 600W — provides approximately 30% headroom, which is the recommended buffer
*   D) 1000W — maximum wattage always ensures the best system stability
*   **Correct Answer:** C) 600W — provides approximately 30% headroom, which is the recommended buffer
*   **Distractor Analysis:**
    * *Why C is correct:* A 25–30% headroom buffer above estimated load is industry best practice; 600W on a 420W system provides ~43% headroom and keeps the PSU operating efficiently at mid-load.
    * *Why A is incorrect:* A PSU running near its maximum rated wattage operates inefficiently, runs hotter, and has a shorter lifespan.
    * *Why B is incorrect:* 500W provides only ~19% headroom, which is below the recommended 25–30% buffer for sustained safe operation.
    * *Why D is incorrect:* Massively oversizing a PSU wastes money and causes the PSU to operate at very low load percentages where efficiency is also reduced.


---

**Question 4**
A desktop PC powers on briefly, all fans spin for 2–3 seconds, then the system shuts off completely. This cycle repeats when the power button is pressed again. Which component is most likely the root cause?
*   A) The RAM modules need to be reseated because loose memory causes immediate shutdown
*   B) The PSU is failing or underpowered and cannot sustain the system's power load during POST
*   C) The operating system is corrupted and cannot complete the boot sequence
*   D) The GPU driver is incompatible with the motherboard BIOS version
*   **Correct Answer:** B) The PSU is failing or underpowered and cannot sustain the system's power load during POST
*   **Distractor Analysis:**
    * *Why B is correct:* A PSU that cannot sustain load causes the system to power cycle; this symptom — brief power-on then immediate shutdown — is a classic PSU failure or insufficient wattage indicator.
    * *Why A is incorrect:* Loose RAM typically causes POST failure with beep codes or no display output, not a rapid power cycle.
    * *Why C is incorrect:* OS corruption occurs after POST and would produce boot error messages, not an immediate power-off before any display output.
    * *Why D is incorrect:* Driver incompatibility is a software issue that occurs after the OS loads, not during the initial power-on phase.


---

**Question 5**
A technician notices a PC running very hot even though all fans are spinning. Opening the case reveals that the front intake fans are installed backwards. What is the consequence of this error, and what is the correct fix?
*   A) Reversed intake fans create positive pressure, which is always preferred; no fix is needed
*   B) Reversed intake fans exhaust warm air out the front instead of drawing cool air in, disrupting the thermal path; fans should be rotated 180 degrees to restore intake direction
*   C) Reversed fans cause a short circuit on the fan header because PWM signals are polarity-sensitive
*   D) Fan direction does not affect system temperature because all fans move the same total volume of air regardless of orientation
*   **Correct Answer:** B) Reversed intake fans exhaust warm air out the front instead of drawing cool air in, disrupting the thermal path; fans should be rotated 180 degrees to restore intake direction
*   **Distractor Analysis:**
    * *Why B is correct:* Fan blades move air in the direction determined by their rotation and orientation; reversed intake fans push hot internal air outward through the front mesh instead of pulling cool external air in, breaking the front-to-back airflow path.
    * *Why A is incorrect:* Positive pressure is created by having more intake than exhaust fans, not by reversing fans; a reversed front fan actually reduces effective intake.
    * *Why C is incorrect:* Fan power headers (3-pin or 4-pin PWM) are keyed connectors; reversing a fan physically (spinning it around) does not affect the electrical connection.
    * *Why D is incorrect:* Fan orientation critically determines airflow direction; moving the same volume of air in the wrong direction still results in poor thermal management.

