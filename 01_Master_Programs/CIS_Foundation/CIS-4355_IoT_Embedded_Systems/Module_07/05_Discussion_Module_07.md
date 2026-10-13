# Discussion Forum: Module 07 — IoT Communication Protocols

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Initial Post Due:** Wednesday 11:59 PM

**Peer Responses Due:** Sunday 11:59 PM

---

## Instructions

Post a substantive initial response to ONE of the three scenarios below. Then reply to at least TWO classmates who chose different scenarios. Your initial post should be 175–225 words. Each peer response should be at least 75 words and add new analysis, a counter-example, or a real-world extension — do not simply agree.

---

## Scenario A — Protocol Selection Under Constraint

A small agricultural company is deploying 200 soil moisture sensors across a 50-acre farm. Each sensor runs on a small solar-charged battery and communicates over a LoRa radio mesh network. The sensors need to report readings every 15 minutes to a central gateway, which then forwards data to a cloud dashboard. The gateway has a full Linux OS and reliable cellular connectivity. The sensors themselves have only 32 KB of flash and 4 KB of RAM.

Apply the five-factor protocol selection framework to this scenario. Address all five factors explicitly: device constraints on the sensors, network characteristics of the LoRa mesh, message frequency requirements, directionality needs, and reliability requirements. Identify which protocol you would use on the sensor-to-gateway link versus the gateway-to-cloud link — they may be different. Justify each choice with specific numbers or architectural reasons from the reading. Conclude with a message format recommendation (JSON or CBOR) for the sensor side and explain why the other format is inappropriate given the sensor's constraints.

---

## Scenario B — QoS Level Mismatch

A team has deployed a medical alert system using MQTT. Patient monitors publish vital sign alerts to the topic `patients/{id}/alert` at QoS 0. A nursing station dashboard subscribes to `patients/#` and displays incoming alerts. During an audit, the team discovers that alerts are occasionally missing from the dashboard log, even though the monitors show they were published. The broker logs confirm the monitors are connecting and publishing successfully.

Diagnose the root cause of the missing alerts. Explain why QoS 0 is insufficient for this use case and what specific scenario causes the message loss. Propose the exact QoS level change needed, which side (publisher, subscriber, or both) needs to change it, and what else must be configured on the broker to support reliable delivery. Then identify a second, unrelated issue in this architecture: the topic design uses patient IDs in the path. What privacy or access control concern does this create, and how would you redesign the topic structure or broker configuration to address it?

---

## Scenario C — MQTT vs HTTP Architecture Decision

A startup is building a fleet management platform for delivery trucks. Each truck has a GPS unit and a cellular modem. The platform needs to: (1) receive GPS coordinates from each truck every 30 seconds, (2) allow dispatchers to send route update commands to individual trucks, (3) alert the operations center immediately when a truck's speed exceeds 80 mph, and (4) store all trip data in a SQL database.

Design the communication architecture for this system. For each of the four requirements above, specify whether you would use MQTT (and at which QoS level) or HTTP, and justify your choice. Identify where a message broker fits in the architecture and what cloud platform you would use (AWS IoT Core, Azure IoT Hub, or self-hosted Mosquitto) given that the fleet size is 500 trucks. Address what happens to requirements 1 and 3 if a truck enters a tunnel and temporarily loses cellular connectivity — how does your protocol selection handle reconnection and message recovery?

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

These scenarios are grounded in real deployment decisions. The agricultural sensor scenario (A) is representative of precision agriculture systems being deployed across the US right now — choosing the wrong protocol stack can mean a sensor that works in the lab but drains its battery in a week in the field. The medical alert scenario (B) is based on an actual incident class that has been documented in healthcare IoT literature. QoS mismatches in clinical settings have real consequences. Scenario C captures the full complexity of a real-time fleet system where different data streams have genuinely different reliability requirements. There is no single correct answer for C — but there are several wrong ones. Show your reasoning.
