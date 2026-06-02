# Reading Guide: Module 06 - Power Supplies and System Cooling

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

**Certification Domain:** 3.5 — Install and configure motherboards, CPUs, and add-on cards | 5.2 — Troubleshoot problems related to motherboards, RAM, CPUs, and power

---

### Introduction

Welcome to Module 06 — Power Supplies and System Cooling. This module covers the power supply unit (PSU), which converts AC wall power to the DC voltages used by all PC hardware, and the airflow strategies that keep the entire system thermally healthy. You will learn how to calculate power requirements, understand efficiency ratings, identify all standard PSU connectors, and configure proper case airflow to prevent thermal throttling and component damage.

These topics appear on the CompTIA A+ Core 1 (220-1101) exam under Domain 3.5 and Domain 5.2. As a technician, you must be able to recommend an appropriate PSU wattage, identify every connector type on sight, distinguish PSU form factors, and diagnose both power delivery and airflow problems. Complete the study checklist and review all glossary terms before beginning the lab.

---

### Section 1: High-Yield Glossary

Review these definitions carefully. The certification exam expects you to recognize and apply all of these terms in scenario-based questions.

**PSU (Power Supply Unit):** The component that converts AC (alternating current) power from the wall outlet into the DC (direct current) voltages required by PC components: +12V, +5V, +3.3V, and the -12V and +5VSB (standby) rails. The PSU also provides a Power Good signal to the motherboard once voltages are stable, which allows the system to begin POST. A failed or undersized PSU is one of the most common causes of system instability and random shutdowns.

**PSU Wattage:** The total continuous DC power output a PSU can sustain while delivering all voltages within specification. Wattage is calculated by summing the TDP (Thermal Design Power) of the CPU, GPU, storage devices, RAM, fans, and motherboard, then applying a 20–30% headroom buffer. Operating a PSU at or near its maximum rated wattage reduces efficiency, increases heat, and shortens the unit's lifespan. Common desktop wattages range from 400W (office builds) to 1,000W+ (high-end gaming or workstation systems with multiple GPUs).

**TDP (Thermal Design Power):** A specification published by component manufacturers (Intel, AMD, NVIDIA) indicating the maximum heat a component generates at typical workloads, measured in watts. TDP is used as a proxy for power draw when sizing a PSU. Note that TDP is not an absolute maximum — some CPUs and GPUs can exceed their TDP during power limit overrides. Always add the headroom buffer to account for transient peaks.

**80 Plus Certification:** An industry efficiency standard for PSUs. An 80 Plus-certified PSU converts at least 80% of AC input power to DC output at 20%, 50%, and 100% of rated load — meaning no more than 20% is wasted as heat. Higher tiers: Bronze (82–85%), Silver (85–88%), Gold (87–90%), Platinum (89–92%), Titanium (94%+). The certification label appears on the PSU unit. Higher efficiency translates to lower electricity costs, cooler PSU operation, and reduced fan noise.

**Modular PSU:** A PSU in which cables are detachable from the unit. A fully modular PSU allows the technician to install only the cables the system requires, reducing cable clutter and improving airflow. A semi-modular PSU has the 24-pin ATX and CPU power cables permanently attached while all other cables are detachable. A non-modular PSU has all cables permanently attached regardless of whether they are needed.

**ATX Form Factor (PSU):** The standard PSU physical size for desktop ATX and Micro-ATX cases, measuring 150mm wide x 86mm tall x 140mm (or longer) deep. SFX (Small Form Factor) PSUs are used in compact ITX cases and are approximately half the size of ATX PSUs. The ATX form factor is the dominant standard and is the primary type tested on the CompTIA A+ exam.

**24-pin ATX Connector:** The main motherboard power connector, supplying the 3.3V, 5V, 12V, -12V, and 5VSB rails to the motherboard. It is 24 pins wide and has a locking clip to secure it to the motherboard header. Some connectors split into a 20-pin primary and a 4-pin extension for backward compatibility with older motherboards that used the 20-pin standard.

**4/8-pin EPS Connector (CPU Power):** A dedicated power connector that supplies 12V power directly to the CPU voltage regulator modules on the motherboard. It connects to a header located near the top-left corner of most ATX motherboards. Entry-level boards use a 4-pin connector; enthusiast and overclocking boards use an 8-pin or dual 8-pin connector. Forgetting to connect the CPU power cable is one of the most common mistakes in new builds — the system will not POST without it.

**6/8-pin PCIe Connector (GPU Power):** Supplies auxiliary 12V power directly to the GPU. The PCIe slot on the motherboard can deliver only 75W; any GPU exceeding that power draw requires one or more PCIe power connectors from the PSU. A 6-pin PCIe connector supplies up to 75W of auxiliary power; an 8-pin supplies up to 150W. High-end GPUs may use two 8-pin connectors or a proprietary 16-pin (12VHPWR) connector.

**15-pin SATA Power Connector:** The standard power connector for all SATA storage devices (HDDs and SSDs). It carries 3.3V, 5V, and 12V rails. The L-shaped keying prevents incorrect insertion. The 2.5-inch drive uses only the 5V rail; the 3.5-inch HDD uses both the 5V and 12V rails.

**4-pin Molex Connector:** A legacy large-bodied 4-pin connector used prior to SATA power. It carries 5V and 12V power and was the standard for IDE drives, optical drives, and case fans. Still found in some older cases, fan controllers, and LED accessories. Modern builds rarely use Molex for drives, but the A+ exam expects recognition of the connector.

**Case Airflow:** The directional movement of air through a PC case designed to carry heat away from components. Intake fans bring cool external air into the case; exhaust fans push heated internal air out. The standard ATX case airflow path runs front-to-back and bottom-to-top. Positive pressure (more intake than exhaust) reduces dust accumulation. Negative pressure (more exhaust than intake) pulls dust in through unfiltered gaps.

**Positive vs. Negative Pressure:** In a positive-pressure configuration, the total intake fan area exceeds exhaust, forcing air out only through filtered vents and reducing dust ingress. In a negative-pressure configuration, more air is exhausted than intake, creating a partial vacuum that pulls air in through every unsealed gap in the case — including unfiltered areas — accelerating dust buildup on components.

**Thermal Paste:** A thermally conductive compound (usually silicone-based with metalite or ceramic particles) applied between the CPU heat spreader and the cooler base to eliminate air gaps that would insulate rather than transfer heat. Air has very low thermal conductivity; thermal paste fills microscopic surface imperfections to maximize heat transfer. Proper application is a thin, even layer covering the CPU heat spreader — overapplication can cause overflow onto the socket.

**CPU Cooler Types:** Air coolers use a heatsink (metal fin array) and one or more fans to dissipate heat by convection. All-in-one (AIO) liquid coolers use a pump, sealed water block, tubing, and a radiator mounted in a case fan slot to carry heat away via liquid coolant. AIOs are quieter under load and handle higher TDP chips, but require proper radiator placement (typically top or front exhaust position) to function correctly.

---

### Section 2: PSU Connector Quick-Reference Table

| Connector Name | Pin Count | Voltage Rails | Powers |
|---|---|---|---|
| 24-pin ATX | 24 (or 20+4) | 3.3V, 5V, 12V, -12V, 5VSB | Motherboard main power |
| 4/8-pin EPS (CPU) | 4 or 8 | 12V | CPU voltage regulators |
| 6-pin PCIe | 6 | 12V | GPU (up to 75W aux) |
| 8-pin PCIe | 8 | 12V | GPU (up to 150W aux) |
| 15-pin SATA Power | 15 | 3.3V, 5V, 12V | SATA HDDs and SSDs |
| 4-pin Molex | 4 | 5V, 12V | Legacy drives, fans, accessories |

---

### Section 3: 80 Plus Efficiency Tier Summary

| Certification Tier | Efficiency at 20% Load | Efficiency at 50% Load | Efficiency at 100% Load |
|---|---|---|---|
| 80 Plus (White) | 80% | 80% | 80% |
| 80 Plus Bronze | 82% | 85% | 82% |
| 80 Plus Silver | 85% | 88% | 85% |
| 80 Plus Gold | 87% | 90% | 87% |
| 80 Plus Platinum | 90% | 92% | 89% |
| 80 Plus Titanium | 92% | 94% | 90% |

Note: PSUs operate most efficiently at approximately 50% of rated load. Both under-loading and over-loading reduce efficiency.

---

### Section 4: Wattage Calculation Method

Step 1 — List all components and their TDP or power ratings:

- CPU TDP (from manufacturer spec page)
- GPU TDP (from manufacturer spec page)
- RAM: approximately 3–5W per stick
- Each SATA HDD: approximately 7–10W
- Each SATA or NVMe SSD: approximately 3–6W
- Motherboard: approximately 30–50W
- Case fans: approximately 2–5W each
- Optical drive (if present): approximately 15–25W

Step 2 — Sum all component power values to get the estimated system load.

Step 3 — Multiply the estimated load by 1.25 to 1.30 to determine the minimum recommended PSU wattage with headroom buffer.

Example: CPU 125W + GPU 200W + RAM 10W + two SSDs 10W + motherboard 40W + four fans 12W = 397W estimated load. Multiply 397 x 1.25 = 496W minimum. Select a 550W or 600W PSU as the next standard available wattage.

---

### Section 5: Airflow Configuration Reference

Standard ATX case airflow layout:

- Front bottom: intake (1–3 fans)
- Front top (optional): intake
- Bottom (if filtered vents present): intake
- Rear: exhaust (1 fan, directly behind CPU cooler)
- Top: exhaust (1–3 fans)
- Side: intake toward GPU (optional, not universally recommended)

Fan label reading: The side of the fan with the frame struts (the back of the fan motor housing) is the intake side — air is pulled in from this side. The side with the fan blade hub visible is the exhaust side — air is pushed out from this side. The label arrow confirms the flow direction.

AIO liquid cooler radiator placement:

- Top-mounted radiator: fans push or pull through the radiator; typically exhaust configuration (radiator on top, fans pulling air through from inside the case and out the top)
- Front-mounted radiator: fans pull cool air in from the front; intake configuration

---

### Section 6: Certification Exam Tips

**Trap 1 — Efficiency rating vs. output wattage.** An 80 Plus Gold 500W PSU and an 80 Plus Bronze 500W PSU both deliver exactly 500W of DC output to the system. The efficiency rating determines how much AC wall power is consumed to deliver that 500W, not the amount of DC power delivered. Never select "the Gold PSU powers more components" as a correct answer.

**Trap 2 — Forgetting the CPU power connector.** The A+ exam frequently describes a scenario where a new build will not POST. If the scenario mentions the 24-pin ATX connector is seated but the system does not start, the most likely answer is that the 4/8-pin CPU EPS power connector is not connected.

**Trap 3 — PCIe slot power limit.** The motherboard PCIe slot supplies a maximum of 75W to any card. A GPU requiring more than 75W must have one or more dedicated PCIe power connectors from the PSU. A GPU with no power connector draws all power from the slot — this is only valid for low-power cards.

**Trap 4 — Fan orientation identification.** The A+ exam may show a case diagram and ask which fans are incorrectly oriented. Use the rule: front and bottom = intake; rear and top = exhaust. A rear fan blowing into the case is exhausting hot air back into the system — incorrect.

**Trap 5 — Non-modular vs. modular.** The A+ exam may ask which PSU type is preferred for builds where cable management and airflow are priorities. The correct answer is fully modular. Non-modular PSUs have all cables permanently attached, creating excess cable clutter regardless of what the system actually needs.

**Trap 6 — PSU overcapacity and efficiency.** Massively oversizing a PSU (e.g., 1200W PSU in a 200W system) causes the PSU to operate at very low load percentages where efficiency is reduced. This is both wasteful and more expensive. Correct sizing is 125–130% of estimated system load.

**Trap 7 — Positive pressure and dust.** The A+ exam may ask which airflow configuration reduces dust accumulation inside the case. The correct answer is positive pressure (more intake than exhaust), which forces air out through filtered vents rather than pulling it in through unfiltered gaps.

**Trap 8 — SATA power rail usage.** The 15-pin SATA power connector carries 3.3V, 5V, and 12V rails. A 3.5-inch HDD uses both 5V and 12V; a 2.5-inch drive uses only 5V. Both use the same 15-pin connector — the unused rails are simply not drawn upon by the smaller drive.

---

### Section 7: Required Readings and Videos

Complete all of the following before attempting the lab and quiz.

**Required Reading:** Review the PSU and cooling sections in Professor Messer's CompTIA A+ Study Notes, available at [https://www.professormesser.com/](https://www.professormesser.com/). Navigate to the 220-1101 study notes and read the sections covering PSU types, connector identification, wattage calculation, efficiency ratings, and case airflow.

**Required Video:** Watch the power supply and system cooling segments in Professor Messer's free CompTIA A+ Core 1 course at [https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/](https://www.professormesser.com/free-a-plus-training/220-1101/220-1101-video/). Focus on the connector identification segment and the airflow direction explanation.

**Supplemental Reference:** CompTIA A+ Core 1 exam objectives are available at [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a). Review Domain 3.5 and Domain 5.2 objective lists to confirm your coverage.

---

### Section 8: Lab Connection

This module's lab reinforces three skills directly tested on the A+ exam:

1. PSU connector identification — matching connector names to pin counts, voltages, and the components they power
2. Wattage calculation — summing component TDP values and applying a headroom buffer to determine minimum PSU wattage
3. Airflow diagram analysis — identifying incorrectly oriented fans in a case diagram and explaining the thermal consequence

Complete the Reading Guide glossary review before beginning the lab.

---

### Section 9: Study Checklist

- [ ] Name all six major PSU connector types, their pin counts, and the components they power
- [ ] Explain the 80 Plus efficiency tier scale and what each tier means for AC wall power consumption
- [ ] State clearly that efficiency rating affects AC input, not DC output to components
- [ ] Calculate minimum PSU wattage for a given component list using the 25% headroom method
- [ ] Explain the difference between fully modular, semi-modular, and non-modular PSUs
- [ ] Describe correct case airflow direction (front/bottom intake, rear/top exhaust)
- [ ] Explain positive pressure versus negative pressure airflow and the dust impact of each
- [ ] Identify intake and exhaust sides of a fan using the label arrow method
- [ ] Read the PSU and cooling sections in Professor Messer's CompTIA A+ Study Notes
- [ ] Watch the power supply and cooling videos in Professor Messer's free A+ Core 1 course
- [ ] Complete Lab 06 and submit via Canvas before the deadline
- [ ] Post your Discussion 06 initial response by Wednesday at 11:59 PM
