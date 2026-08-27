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

---

### Question 11

What does the 80 Plus Gold certification guarantee about a PSU?

- A) The PSU provides at least 80W of clean power per output rail without voltage ripple
- B) The PSU is at least 87–90% efficient at 20%, 50%, and 100% of rated load
- C) The PSU will operate for at least 80,000 hours before failure under standard load conditions
- D) The PSU output voltages remain within 80% of rated values under full load

Correct Answer: B — 80 Plus Gold requires 87% efficiency at 20% load, 90% at 50% load, and 87% at 100% load. At 90% efficiency, a 650W DC output system draws ~722W from the AC wall outlet; the remaining ~72W is wasted as heat inside the PSU.

Distractor Analysis:

- Why A is incorrect: The "80" in 80 Plus refers to efficiency percentage, not wattage per rail. Voltage ripple is a separate specification not covered by the 80 Plus rating.
- Why C is incorrect: 80 Plus certification has no bearing on the PSU rated lifespan in hours. MTBF is a separate manufacturer specification.
- Why D is incorrect: Output voltage regulation is a separate ATX specification. The 80 Plus rating is purely an efficiency measurement.

---

### Question 12

A semi-modular PSU differs from a fully modular PSU in which way?

- A) A semi-modular PSU has fixed efficiency; a fully modular PSU efficiency changes based on which cables are attached
- B) A semi-modular PSU has some cables permanently attached while other cables are detachable; a fully modular PSU has all cables detachable
- C) A semi-modular PSU can only power one GPU; a fully modular PSU supports multi-GPU configurations
- D) A semi-modular PSU has a semi-passive fan that spins only at 50% load; a fully modular PSU fan runs at all times

Correct Answer: B — Semi-modular PSUs permanently attach the most commonly used cables (24-pin ATX and 4/8-pin CPU power) since these are always required, while optional cables (SATA, PCIe, Molex) remain modular/detachable.

Distractor Analysis:

- Why A is incorrect: Modularity has no effect on efficiency ratings. Both PSU types of the same efficiency tier will have the same certification regardless of cable design.
- Why C is incorrect: GPU support is determined by available PCIe power connectors and total wattage, not by whether the PSU is semi or fully modular.
- Why D is incorrect: Semi-passive fan behavior is a separate feature found on some premium PSUs. It is independent of modular cable design.

---

### Question 13

A PSU is rated at 80 Plus Bronze (85% efficiency at 50% load). A system draws 400W DC. How many watts does the PSU draw from the AC wall outlet?

- A) 400W — efficiency ratings only apply to the output side
- B) 340W — the PSU uses 85% of its rated capacity
- C) 471W — AC input equals DC output divided by the efficiency ratio
- D) 460W — the 85% efficiency means 15% is added as a flat overhead

Correct Answer: C — Efficiency = DC Output / AC Input. Rearranging: AC Input = 400W / 0.85 = 470.6W ≈ 471W. The ~71W difference is dissipated as heat inside the PSU.

Distractor Analysis:

- Why A is incorrect: Efficiency means the input is greater than the output. A 100% efficient PSU would draw exactly 400W; at 85% efficiency the wall draw must be higher.
- Why B is incorrect: 340W = 400W × 0.85 — this calculates 85% of the output, implying the PSU draws less from the wall than it delivers, which is thermodynamically impossible.
- Why D is incorrect: 400W × 1.15 = 460W, and this multiplication formula is an approximation that diverges from the correct division formula. The correct method is to divide by the efficiency ratio.

---

### Question 14

Which PSU protection feature prevents damage when an output voltage rises significantly above its rated value?

- A) OCP (Over Current Protection)
- B) OVP (Over Voltage Protection)
- C) OTP (Over Temperature Protection)
- D) SCP (Short Circuit Protection)

Correct Answer: B — OVP monitors each output rail and triggers a shutdown if any rail exceeds its rated voltage by more than the specified tolerance. A failed voltage regulator inside the PSU can spike a rail, and without OVP that overvoltage would destroy motherboard components, CPUs, and drives.

Distractor Analysis:

- Why A is incorrect: OCP shuts the PSU down if current draw on a rail exceeds rated amperage. This protects against overloads, not overvoltage conditions.
- Why C is incorrect: OTP shuts the PSU down when internal temperature exceeds a safe threshold, not when output voltage rises above rated values.
- Why D is incorrect: SCP detects a short circuit (low resistance, high current event) and shuts down immediately. This is a current event, not a voltage rise event.

---

### Question 15

A CPU runs at 92°C under sustained load using the stock cooler. The case has filtered front intake fans but no rear exhaust fans. What is the MOST likely cause?

- A) The stock cooler is not rated for the CPU TDP at any ambient temperature
- B) Hot air expelled by the CPU cooler fan has no escape path and recirculates inside the sealed case
- C) The front intake fans are creating positive pressure that compresses air and raises its temperature
- D) The case filters are blocking all airflow to the CPU

Correct Answer: B — Without exhaust fans, hot air heated by the CPU and GPU accumulates inside the case. The CPU fan moves heat off the heat sink, but that hot air stays trapped. Adding a rear exhaust fan creates a front-to-rear airflow path that removes heat from the case.

Distractor Analysis:

- Why A is incorrect: Stock coolers are rated for the CPU TDP under normal airflow conditions. The problem here is case airflow design, not the cooler intrinsic rating.
- Why C is incorrect: Positive pressure does not compress air in a case to a degree that raises temperature through compression. Cases are not sealed pressure vessels.
- Why D is incorrect: Filters reduce airflow somewhat but do not completely block it when fans are operating. The primary issue is the absence of any exhaust path.

---

### Question 16

A technician performs an ATX bench test by shorting pins 16 and ground on the 24-pin connector. The PSU fan spins and all voltages measure correctly. What does this indicate?

- A) The PSU is confirmed faulty and must be replaced
- B) The PSU is functioning normally; the fault is elsewhere — motherboard, power switch, or front panel header
- C) The PSU will only work in bench-test mode
- D) The PSU OCP is triggered by the motherboard and must be reset

Correct Answer: B — The ATX bench test simulates the signal the motherboard sends to turn on the PSU. If the PSU powers on with correct output voltages when this signal is applied directly, the PSU is working. The fault is upstream: the power button, motherboard, or front panel header wiring.

Distractor Analysis:

- Why A is incorrect: A PSU that powers on correctly with correct voltage outputs during the bench test is not faulty. The test specifically isolates the PSU to confirm it operates correctly.
- Why C is incorrect: There is no "bench-test mode." The PSU operates via the same PS_ON signal in both scenarios.
- Why D is incorrect: OCP triggers when a downstream component draws too much current. It does not block power button signaling.

---

### Question 17

How do you identify the air intake versus exhaust side of a case fan using only the fan frame?

- A) The side with the fan blade hub facing outward is always the intake side
- B) The arrow printed on the fan frame points in the direction air moves through the fan
- C) The side with visible fan blade edges is always the exhaust side
- D) The label on the fan only shows the model number; determine airflow by spinning the fan manually

Correct Answer: B — The airflow direction arrow on the fan frame is the reliable field method. If the arrow points toward the case interior, the fan is an intake; if it points outward, the fan is an exhaust.

Distractor Analysis:

- Why A is incorrect: The orientation of the hub depends on which side you view and does not consistently indicate intake vs. exhaust across all fan designs.
- Why C is incorrect: Determining airflow from blade edge appearance is unreliable and varies by fan design. The printed arrow is the definitive indicator.
- Why D is incorrect: Manually spinning a fan creates a weak breeze that is difficult to reliably interpret for direction.

---

### Question 18

A customer reports a high-pitched whining noise that increases with system load, coming from inside the case. What is the MOST likely source?

- A) A failing CPU fan bearing producing resonance under load
- B) Coil whine from PSU or GPU VRM inductors vibrating at high frequency under varying electrical load
- C) The optical drive spinning up to read a disc
- D) The HDD read/write head seeking rapidly due to fragmented files

Correct Answer: B — Coil whine occurs when inductors in a PSU or VRM vibrate at audible frequencies under varying electrical load. The sound scales with load because higher current creates stronger mechanical vibration in the coil windings.

Distractor Analysis:

- Why A is incorrect: A failing fan bearing produces a low-frequency grinding or rattling sound, not a high-pitched whine. Fan bearing noise tends to be constant rather than load-dependent.
- Why C is incorrect: Optical drive spin-up produces a brief mechanical whirring sound, not a continuous high-pitched whine that scales with CPU/GPU load.
- Why D is incorrect: HDD head seeking produces a clicking or clunking sound, not a high-pitched electrical whine.

---

### Question 19

A technician replaces a failed 750W PSU with a 450W unit. The system powers on but immediately shuts off. What is the MOST likely cause?

- A) The 450W PSU firmware is incompatible with the motherboard
- B) The 450W PSU is insufficient for the system power requirements and its OCP/OPP protection triggers at startup
- C) The 24-pin ATX connector on the replacement PSU is reversing polarity on the motherboard
- D) The replacement PSU efficiency rating is too low, causing it to overheat within seconds

Correct Answer: B — Replacing a 750W PSU with a 450W unit in a system that required 750W causes the replacement PSU OCP or OPP (Over Power Protection) to trigger immediately when the system draws more current than the PSU can safely supply.

Distractor Analysis:

- Why A is incorrect: PSUs do not have motherboard-specific firmware requiring compatibility initialization. They supply regulated DC voltages per ATX standards.
- Why C is incorrect: The 24-pin ATX connector is keyed and can only be inserted in one orientation. Polarity reversal is physically prevented by the connector design.
- Why D is incorrect: A lower efficiency rating generates more heat over time, not an instant shutdown. Efficiency affects heat output, not instantaneous power delivery capability.

---

### Question 20

Which PSU protection feature most directly prevents damage to a motherboard if a GPU PCIe power connector develops an internal short circuit?

- A) OVP (Over Voltage Protection)
- B) OTP (Over Temperature Protection)
- C) SCP (Short Circuit Protection)
- D) NLO (No Load Operation) protection

Correct Answer: C — SCP monitors output rails for near-zero resistance conditions indicating a short circuit. When a PCIe connector shorts, resistance drops and current surges. SCP immediately shuts the PSU down, preventing overcurrent from flowing through the motherboard and PCIe slot.

Distractor Analysis:

- Why A is incorrect: OVP triggers when voltage rises above rated values. A short circuit causes voltage to collapse, not rise. OVP would not trigger during a short circuit event.
- Why B is incorrect: OTP triggers when internal temperature exceeds a threshold — a thermal response that takes time to develop. It does not provide immediate protection against a sudden high-current short.
- Why D is incorrect: NLO protection applies when a PSU is powered on with no load attached. It is not relevant to a short circuit protection scenario.
