# Discussion Forum: Module 06 — Microcontroller Programming

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Initial Post Due:** Wednesday 11:59 PM

**Peer Responses Due:** Sunday 11:59 PM

---

## Instructions

Post a substantive initial response to ONE of the three scenarios below. Then reply to at least TWO classmates who chose different scenarios. Your initial post should be 175–225 words. Each peer response should be at least 75 words and add new analysis, a counter-example, or a real-world extension — do not simply agree.

---

## Scenario A — The Memory Crisis

A student is building a data logger on an Arduino Uno. Their sketch reads six analog sensors, formats the readings into a JSON string using the `String` class, and prints it to Serial every second. The sketch works fine in testing, but after running for about 20 minutes the device freezes and must be reset. The student increases the `delay()` value but the problem persists. The freeze always happens at a different time, never at a predictable interval.

Diagnose this failure. Identify the root cause at the hardware and software level, explain why the failure is non-deterministic in timing, and propose at least two concrete code changes that would resolve it. Your answer should reference SRAM layout, heap fragmentation, and the specific Arduino data type causing the problem. Conclude with a general rule you would apply to any embedded project that needs to run continuously for days or weeks without a reset.

---

## Scenario B — Interrupt or Poll?

A robotics team is designing a motor controller that must respond to an emergency stop button within 5 milliseconds of it being pressed. The main loop also reads a quadrature encoder at 1 kHz, updates a PID controller, and sends motor commands over Serial. The senior engineer on the team says the button should be handled with an interrupt. The junior engineer argues that checking `digitalRead()` inside the loop is simpler and "probably fast enough."

Evaluate both arguments using specific timing analysis. Calculate the worst-case response latency for polling if the loop body takes 2ms to execute. Explain what happens to interrupt latency if the ISR performs Serial.print() or calls delay(). Describe the flag-and-handle pattern that makes ISRs safe in this scenario. Finally, identify one situation where polling might actually be preferable to interrupts — there is a valid answer, and it involves debouncing or very noisy signals.

---

## Scenario C — Arduino Uno vs ESP32 Selection

A startup is prototyping two IoT products simultaneously. Product 1 is a smart thermostat that reads a temperature sensor every 30 seconds, drives a relay, and sends data to a cloud dashboard over Wi-Fi. Product 2 is a precision irrigation timer that must open and close solenoid valves at exact 100ms intervals for up to 8 zones, runs on a 9V battery, and has no connectivity requirement.

For each product, select the more appropriate microcontroller platform (Arduino Uno or ESP32) and justify your choice using at least three specific technical criteria from this module — clock speed, SRAM, PWM channels, power consumption, connectivity, or cost. Then identify one significant risk or limitation of your chosen platform for each product and explain how you would mitigate it in the final design. Avoid generic statements; ground every claim in specific numbers or architectural details from the module content.

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

The scenarios in this module are drawn from real embedded systems failures I have encountered professionally. The memory leak scenario (A) took a team three days to diagnose on a production sensor node because the crash was intermittent. The interrupt vs polling debate (B) comes up on nearly every real-time control project. Platform selection (C) is a judgment call that every embedded engineer makes repeatedly — and getting it wrong costs real money. There are defensible answers for every scenario, but vague answers will not earn full credit. Show your reasoning with numbers.
