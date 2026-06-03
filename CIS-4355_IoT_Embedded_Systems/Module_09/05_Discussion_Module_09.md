# Discussion Forum: Module 09 — IoT Wireless Networking

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Initial Post Due:** Wednesday 11:59 PM

**Peer Responses Due:** Sunday 11:59 PM

---

## Instructions

Post a substantive initial response to ONE of the three scenarios below. Then reply to at least TWO classmates who chose different scenarios. Your initial post should be 175–225 words. Each peer response should be at least 75 words and add new analysis, a counter-example, or a real-world extension — do not simply agree.

---

## Scenario A — Smart City Parking Network

A city wants to install parking sensors in 5,000 parking spaces across downtown. Each sensor detects whether the space is occupied (binary) and reports status every 2 minutes. The city wants a 10-year operational life on battery power. The deployment area is 1 km × 1 km. The city's IT department has reliable fiber internet connectivity at city hall and two substations within the deployment area.

Design the wireless network architecture for this deployment. Select the most appropriate wireless technology, justify your choice against all other candidates from this module using specific numbers from the reading (range, data rate, power, node count). Calculate whether a single gateway is sufficient or whether multiple gateways are needed. Estimate battery life using the duty cycle: 2-second transmission time per 120-second interval at 20 mA TX current and 2 µA sleep current. Show your calculation. Finally, identify one significant operational risk in your chosen architecture and propose a mitigation strategy.

---

## Scenario B — Wi-Fi vs BLE for a Smart Home Hub

A company is designing a smart home hub that will communicate with 20 sensors around a home. The sensors include door/window sensors, motion detectors, temperature sensors, and smart plugs. The hub has a mains power supply and a broadband internet connection. The sensors run on coin cell batteries and must last 12 months minimum.

Compare Wi-Fi and BLE as the sensor-to-hub communication technology for this system. Use specific power figures from the reading for both technologies. Calculate battery life for a coin cell battery (250 mAh) under each wireless technology for a door sensor that transmits a state change 20 times per day, with each transmission taking 2 seconds. Identify two scenarios where you would choose Wi-Fi over BLE and two where you would choose BLE over Wi-Fi for the sensors. Conclude by recommending one technology and defending your choice with at least three specific technical criteria from the module. Do not simply say "BLE is better for IoT" — provide quantified justification.

---

## Scenario C — LoRaWAN vs Cellular for Agricultural Deployment

A precision agriculture startup is choosing between LoRaWAN and NB-IoT for a nationwide deployment of 50,000 soil sensors across farms in Texas. Each sensor reports temperature, moisture, and NPK (nitrogen/phosphorus/potassium) readings — about 30 bytes — every hour. Some farms are remote with no cellular coverage. The startup has a 5-year operational plan and needs sensors to last 5 years on battery.

Evaluate LoRaWAN and NB-IoT for this deployment across five dimensions: coverage, power consumption, data capacity (is 30 bytes per hour within each technology's constraints?), infrastructure cost at scale, and coverage gaps in rural Texas. Calculate the LoRaWAN duty cycle compliance for a 30-byte message at SF9 (time on air approximately 185 ms) sent once per hour. Propose a hybrid architecture that uses both technologies to address coverage gaps, and describe how the application layer would handle devices seamlessly switching between LoRaWAN and NB-IoT connectivity. Identify the biggest remaining technical challenge in this hybrid design.

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

All three scenarios represent real deployment decisions being made right now in industry. Scenario A mirrors actual smart city parking projects deployed in Barcelona, San Francisco, and Kansas City. The battery life calculation is not a trick question — work it out carefully, because the answer determines whether your chosen technology is feasible. Scenario B captures the core design question for every smart home product on the market today. Scenario C reflects an actual challenge facing AgTech companies expanding beyond connected-farm pilots into nationwide deployments. The hybrid architecture question is genuinely hard — there is no textbook answer, and the best posts will identify failure modes the question does not mention.
