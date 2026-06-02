# Quiz: Module 06 - Power Supplies and System Cooling

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

Total Questions: 10 | Points: 10 (1 point each)

Certification Domain: 3.5 — Install and configure motherboards, CPUs, and add-on cards | 5.2 — Troubleshoot problems related to motherboards, RAM, CPUs, and power

---

### Question 1

What standard power connector is used to supply dedicated auxiliary power to a high-end PCIe graphics card that requires more than 75W beyond what the slot provides?

- A) 24-pin ATX
- B) 15-pin SATA Power
- C) 6-pin or 8-pin PCIe
- D) 4-pin Molex

Correct Answer: C — The PCIe slot on the motherboard can supply a maximum of 75W to any installed card. A GPU requiring more power must receive it through a dedicated 6-pin (up to 75W additional) or 8-pin (up to 150W additional) PCIe power connector routed directly from the PSU.

Distractor Analysis:

- Why A is incorrect: The 24-pin ATX connector powers the motherboard's logic, USB headers, and PCIe slot voltage rails — it is not connected directly to a GPU.
- Why B is incorrect: The 15-pin SATA power connector is used for storage devices (HDDs and SSDs). It does not connect to a GPU.
- Why D is incorrect: The 4-pin Molex is a legacy connector for older drives and accessories. Modern GPUs require the dedicated PCIe power connector, not Molex.

---

### Question 2

Which of the following most accurately describes case airflow strategy using intake and exhaust fans?

- A) The directional movement of air through a PC case where intake fans draw cool air in (typically front and bottom) and exhaust fans push hot air out (typically rear and top), creating a front-to-back, bottom-to-top thermal path across components.
- B) The process of measuring the voltage differential between the PSU's 12V and 5V rails to determine whether airflow regulators are operating within acceptable tolerances.
- C) A BIOS setting that controls fan speed curves based on CPU temperature readings, automatically adjusting RPM to balance noise and thermal performance.
- D) The circulation of coolant fluid through a closed-loop AIO liquid cooling system, where intake refers to the pump inlet and exhaust refers to the radiator outlet.

Correct Answer: A — Proper case airflow directs cool external air across heat-generating components and expels heated air out of the case. Front and bottom fans serve as intake; rear and top fans serve as exhaust, following the physical principle that heat rises.

Distractor Analysis:

- Why B is incorrect: This describes voltage rail measurement, a PSU diagnostic process unrelated to the physical concept of fan-driven airflow direction.
- Why C is incorrect: This describes a fan speed or PWM control feature in BIOS, which is a performance tuning function, not the physical airflow strategy being described.
- Why D is incorrect: This describes AIO liquid cooling loop terminology. The question asks about case airflow strategy, which applies to the entire chassis fan layout, not internal coolant circulation.

---

### Question 3

A technician is building a PC and estimates the total system power draw at 420W under full load. Which PSU wattage provides adequate headroom while following the 25% buffer best practice?

- A) 430W — just above the estimated load is sufficient for normal operation.
- B) 500W — provides approximately 19% headroom above the estimated draw.
- C) 550W — provides approximately 31% headroom, within the recommended buffer range.
- D) 1000W — maximum wattage always ensures the best system stability.

Correct Answer: C — Applying a 25% headroom buffer to 420W yields 420 x 1.25 = 525W minimum. A 550W PSU is the next standard wattage above that threshold and keeps the PSU operating at roughly 75% of rated capacity under full load — within the most efficient operating range.

Distractor Analysis:

- Why A is incorrect: A PSU running at or above 97% of its rated wattage operates inefficiently, generates more heat, and has a significantly shorter lifespan. The 25–30% headroom buffer exists to prevent this.
- Why B is incorrect: 500W provides only approximately 19% headroom (500 / 420 = 1.19), which is below the recommended 25% buffer for sustained safe operation.
- Why D is incorrect: A 1000W PSU on a 420W system operates at roughly 42% of its rated load — below the efficiency sweet spot. This wastes money and the PSU may operate less efficiently at very low load percentages than a correctly sized unit.

---

### Question 4

A desktop PC powers on briefly, all fans spin for 2–3 seconds, then the system shuts off completely. This cycle repeats when the power button is pressed. The 24-pin ATX connector is fully seated. What is the most likely cause?

- A) The RAM modules need to be reseated because loose memory causes an immediate shutdown loop.
- B) The 4/8-pin CPU EPS power connector is not connected, or the PSU is failing and cannot sustain the load during POST.
- C) The operating system is corrupted and cannot complete the boot sequence.
- D) The GPU driver is incompatible with the motherboard BIOS version.

Correct Answer: B — A missing CPU EPS power connector prevents stable POST. Similarly, a failing or undersized PSU that cannot sustain the startup power spike will cause the system to cycle — brief power-on then immediate shutdown is a classic PSU or CPU power delivery failure symptom.

Distractor Analysis:

- Why A is incorrect: Loose RAM typically causes POST failure with diagnostic beep codes or no display output, not a rapid power-on/power-off cycle before any output is produced.
- Why C is incorrect: OS corruption occurs after POST completes and the system begins the boot process. A system that shuts off within seconds of power-on has not reached the OS loading stage.
- Why D is incorrect: Driver incompatibility is a software issue that presents after the OS loads, not during the initial power-on phase before any display output.

---

### Question 5

A technician notices a PC running very hot even though all fans are spinning. Opening the case reveals that the front intake fans are installed backwards. What is the consequence of this error, and what is the correct fix?

- A) Reversed intake fans create positive pressure, which is always preferred; no fix is needed.
- B) Reversed intake fans exhaust warm air out the front instead of drawing cool air in, disrupting the thermal path; the fans should be rotated 180 degrees so the airflow arrow points inward.
- C) Reversed fans cause a short circuit on the fan header because PWM signals are polarity-sensitive.
- D) Fan direction does not affect system temperature because all fans move the same total volume of air regardless of orientation.

Correct Answer: B — Fan blades move air in the direction determined by their blade angle and rotation. Reversed front fans push warm internal air outward through the front mesh instead of pulling cool external air in, which breaks the front-to-back airflow path and causes heat to accumulate around the CPU and GPU.

Distractor Analysis:

- Why A is incorrect: Positive pressure is created by having more intake fan area than exhaust, not by reversing individual fans. A reversed front fan actually reduces effective intake and creates turbulent airflow near the front of the case.
- Why C is incorrect: Fan power headers (3-pin or 4-pin PWM) are keyed connectors. Rotating a fan 180 degrees physically changes airflow direction but does not affect the electrical connection to the header.
- Why D is incorrect: Moving air in the wrong direction defeats the thermal design of the case. Hot air circulating internally instead of being replaced with cool air still results in rapidly rising component temperatures.

---

### Question 6

A technician examines two PSUs on a workbench. Both are rated at 650W. One is 80 Plus Bronze certified; the other is 80 Plus Gold certified. A colleague claims the Gold PSU "gives the PC more power." Which statement correctly evaluates this claim?

- A) The colleague is correct — higher efficiency tiers unlock additional voltage headroom, so the Gold PSU delivers more usable DC watts to the system.
- B) The colleague is incorrect — both PSUs deliver 650W of DC output to the system; the Gold PSU simply draws less AC power from the wall to deliver that 650W.
- C) The colleague is correct — the Gold PSU has a higher wattage ceiling that activates when temperatures exceed 60 degrees Celsius inside the case.
- D) The colleague is partially correct — the Gold PSU delivers 650W, but the Bronze PSU is derated to approximately 500W due to its lower efficiency tier.

Correct Answer: B — The 80 Plus certification tier describes how efficiently AC input is converted to DC output. Both PSUs deliver exactly 650W to the system. The Gold PSU requires less AC wattage from the wall outlet to produce that 650W, meaning less energy is wasted as heat inside the PSU itself.

Distractor Analysis:

- Why A is incorrect: Efficiency tiers do not change the rated DC output wattage. A 650W Gold PSU delivers 650W; a 650W Bronze PSU delivers 650W. There is no additional "headroom unlock" based on efficiency.
- Why C is incorrect: PSU wattage ratings do not increase or decrease based on temperature. The rated wattage is a fixed specification; actual output can decrease if the PSU overheats (thermal throttling), but this is a failure mode, not a feature.
- Why D is incorrect: Efficiency tier does not derate the rated output wattage. A 650W Bronze PSU is rated at 650W DC output, not 500W. Lower efficiency means more AC watts consumed, not fewer DC watts delivered.

---

### Question 7

Which PSU type is described as having the 24-pin ATX and CPU EPS cables permanently attached, while all PCIe, SATA, and Molex cables are detachable?

- A) Non-modular
- B) Fully modular
- C) Semi-modular
- D) ATX12V

Correct Answer: C — A semi-modular PSU permanently attaches the essential cables (24-pin ATX motherboard power and CPU EPS power) that every build requires, while making the remaining cables (PCIe, SATA, Molex) detachable so the technician can install only what the system needs.

Distractor Analysis:

- Why A is incorrect: A non-modular PSU has all cables permanently attached — including PCIe, SATA, and Molex — with no detachable connections.
- Why B is incorrect: A fully modular PSU has every cable detachable, including the 24-pin ATX and CPU power cables. Nothing is permanently fixed to the unit.
- Why D is incorrect: ATX12V is a specification name referring to the 4-pin CPU power connector standard, not a PSU cable management type.

---

### Question 8

A technician is planning a positive-pressure airflow configuration for a desktop build. Which fan setup correctly describes positive pressure?

- A) Two rear exhaust fans and no intake fans, forcing air to enter the case through the front mesh vents by suction.
- B) Three front intake fans and one rear exhaust fan, so more air enters the case than exits through filtered openings.
- C) Equal numbers of intake and exhaust fans so that air pressure inside the case exactly matches atmospheric pressure.
- D) All fans configured as exhaust, removing all air from the case simultaneously through every available vent.

Correct Answer: B — Positive pressure occurs when total intake airflow volume exceeds total exhaust airflow volume. This forces air out only through filtered vent openings (such as front mesh filters) rather than allowing unfiltered air to be pulled in through case gaps and seams, which reduces dust accumulation inside the system.

Distractor Analysis:

- Why A is incorrect: Having only exhaust fans with no intake creates extreme negative pressure; air would be drawn in through every unfiltered gap, which maximizes dust ingress.
- Why C is incorrect: Equal intake and exhaust produces balanced pressure (neither positive nor negative), not positive pressure. While balanced airflow is reasonable, it is not positive pressure.
- Why D is incorrect: All fans configured as exhaust with no intake is an extreme negative-pressure scenario that would starve the system of cool air and pull unfiltered air through every case gap.

---

### Question 9

A system builder reads the CPU manufacturer's TDP as 125W and the GPU manufacturer's TDP as 250W. After adding all other components, the total estimated system load is 470W. Which calculation correctly determines the minimum recommended PSU wattage using a 25% headroom buffer?

- A) 470W + 25W = 495W; select a 500W PSU.
- B) 470W x 0.25 = 117.5W; select a PSU equal to 117.5W.
- C) 470W x 1.25 = 587.5W; select a 600W or 650W PSU.
- D) 470W / 1.25 = 376W; select a 400W PSU.

Correct Answer: C — The 25% headroom buffer is applied by multiplying the estimated load by 1.25, not by adding 25W or dividing. 470 x 1.25 = 587.5W, so the technician selects the next standard wattage above that figure (600W or 650W).

Distractor Analysis:

- Why A is incorrect: Adding a flat 25W to a 470W load results in only a 5.3% buffer, which is far below the recommended 25%. This provides no meaningful protection against power spikes.
- Why B is incorrect: This calculates 25% of the load as a standalone figure but does not add it back to the load. The result of 117.5W is clearly not a usable PSU wattage for a 470W system.
- Why D is incorrect: Dividing by 1.25 produces a smaller number (376W), which would result in a PSU undersized relative to the actual load — the opposite of the intended headroom calculation.

---

### Question 10

Which of the following symptoms most strongly indicates a failing or undersized PSU as the root cause rather than a software or storage failure?

- A) The PC boots to Windows but displays a "BOOTMGR is missing" error before loading the desktop.
- B) The PC runs normally at idle but shuts down unexpectedly only when starting a GPU-intensive game or video encode.
- C) The PC displays a blue screen of death with a DRIVER_IRQL_NOT_LESS_OR_EQUAL stop code after a driver update.
- D) The PC boots normally but cannot connect to any network, even with a freshly installed network adapter.

Correct Answer: B — An undersized or failing PSU may provide adequate power at idle (low load) but collapse under the sudden spike in power demand when the GPU and CPU are pushed to full load. Unexpected shutdowns correlated specifically with high-load activities are a classic PSU failure pattern.

Distractor Analysis:

- Why A is incorrect: "BOOTMGR is missing" is a storage or boot configuration error (corrupted boot partition, wrong boot device selected in BIOS). It is a software or drive issue, not a PSU symptom.
- Why C is incorrect: A DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen is a driver compatibility or memory access violation issue. This points to a software (driver) problem following a recent driver update, not a PSU failure.
- Why D is incorrect: A network connectivity failure after installing a new network adapter points to a driver, configuration, or hardware compatibility issue with the NIC — not a PSU power delivery failure.
