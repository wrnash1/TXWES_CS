# Discussion Forum: Module 08 — Sensor Integration and Data Collection

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Initial Post Due:** Wednesday 11:59 PM

**Peer Responses Due:** Sunday 11:59 PM

---

## Instructions

Post a substantive initial response to ONE of the three scenarios below. Then reply to at least TWO classmates who chose different scenarios. Your initial post should be 175–225 words. Each peer response should be at least 75 words and add new analysis, a counter-example, or a real-world extension — do not simply agree.

---

## Scenario A — Sensor Selection for a Cold Chain Monitor

A pharmaceutical logistics company needs to build a cold chain monitor for vaccine transport. The device must fit inside a small shipping container and record temperature every 60 seconds for up to 72 hours. Temperature range of interest is -20°C to +8°C. The device must flag any excursion above 8°C within 30 seconds of it occurring. The monitoring device must run on 4 AA batteries for the full 72-hour trip.

Select a specific temperature sensor from the module content and justify your choice using at least four criteria: temperature range, accuracy, interface type, and power consumption. Explain why the DHT22 is inadequate for this specific application and what specification it fails. Describe how you would configure the data smoothing algorithm — which algorithm, what parameter values, and why — to detect a real temperature excursion within 30 seconds while rejecting brief spikes from opening the container door. Finally, identify the calibration procedure you would apply before deployment and explain what happens to measurement validity if you skip it.

---

## Scenario B — I2C Bus Conflict Resolution

An engineering student is building a multi-sensor weather station using an ESP32. The bill of materials includes: one BMP280 (pressure/temperature), one BH1750 (light), one SHT31 (temperature/humidity), and a second BMP280 (for outdoor vs indoor comparison). After wiring everything to the same I2C bus and running the scanner sketch, only three devices appear.

Diagnose why only three of the four devices are detectable. Identify which two devices share the same default address and explain why this creates a conflict. Describe two methods to resolve the conflict — one using the sensor's hardware address pin and one using software multiplexing — and compare the trade-offs of each approach. Include the specific I2C address values and pin settings involved. Then address a second problem: the student is using 3.3V supply but both BMP280 modules have 4.7 kΩ pull-up resistors on their breakout boards. Explain what happens to signal integrity when four breakout modules — each with their own pull-ups — are all connected to the same bus, and how to calculate the effective combined pull-up resistance.

---

## Scenario C — Calibration vs Smoothing Trade-offs

A student completes a lab and notices that after applying their two-point calibration, the DHT22 temperature readings are consistently 0.3°C below the reference thermometer across the entire range. They also notice that the raw readings jump between 23.5 and 24.0°C repeatedly even when room temperature is perfectly stable. The student wonders whether to apply more aggressive EMA smoothing (lower alpha) to remove the 0.5°C jumps or to recalibrate with a third reference point.

Distinguish between systematic error (bias) and random noise (variance) in sensor measurements. Explain which problem the 0.3°C consistent offset represents, and why EMA smoothing does not fix it. Explain which problem the 0.5°C random jumps represent, and why recalibration does not fix that either. Propose the correct fix for each problem independently. Then address the interaction: if you apply aggressive EMA smoothing (alpha=0.05) to temperature readings that update every 2 seconds, calculate how many seconds it takes for the filtered output to reflect 90% of a sudden real temperature step change of 5°C. Show your calculation and explain whether this latency is acceptable for a HVAC control system that must respond within 30 seconds.

---

## Peer Response Guidelines

When responding to a classmate:

- Identify one point you agree with and explain why it is well-reasoned
- Identify one point you would extend, challenge, or add nuance to
- Bring in a specific technical detail from the reading or lab that strengthens or complicates their argument
- Keep your response focused and technical — avoid vague praise

---

## Grading Rubric (10 points total)

| Criterion | Points |
|-----------|--------|
| Initial post is 175–225 words | 1 |
| Scenario chosen is addressed directly and completely | 2 |
| Technical accuracy — correct use of module concepts | 3 |
| Depth of analysis — goes beyond surface description | 2 |
| Two peer responses, each 75+ words with substantive addition | 2 |
| **Total** | **10** |

---

## Professor Nash Note

Scenario A is based on real requirements from FDA 21 CFR Part 11 cold chain monitoring systems. The 30-second excursion detection window is a real regulatory specification, and the battery life requirement makes sensor selection genuinely constrained. Scenario B represents one of the most common wiring problems I see in student labs — I2C address conflicts. The pull-up resistance calculation in B is something every hardware engineer should be able to do on paper. Scenario C is a classic measurement systems engineering question: students who confuse bias with variance apply the wrong fix and end up with a measurement system that is precisely wrong. Know the difference.
