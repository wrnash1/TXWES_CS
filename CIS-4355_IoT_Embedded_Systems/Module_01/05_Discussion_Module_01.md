# Discussion Forum – Module 01: IoT Architecture – Devices, Gateways, Cloud, and Edge

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Initial Post Due:** Wednesday 11:59 PM
**Peer Responses Due:** Sunday 11:59 PM
**Total Points:** 10

---

## Overview

This forum asks you to apply the four-layer IoT architecture model to real-world scenarios. You will select one of three scenarios below, analyze it using the terminology and concepts from the Module 01 lecture and reading guide, and engage constructively with your classmates' posts.

---

## Scenario A: Smart Hospital Room Monitoring

A regional hospital is replacing nurse call-light buttons with an IoT monitoring system. Every patient room will have a bed sensor (pressure and posture), a pulse oximeter, a room temperature sensor, and a call button that transmits over BLE to a hallway gateway. The gateway forwards readings over the hospital's Wi-Fi to a central server. Nurses view a real-time dashboard on wall-mounted tablets. The hospital's IT policy requires that all patient data be encrypted in transit and that no patient data leave the hospital's on-premise servers.

In 175–225 words, address all of the following:

- Identify which architecture layer each component type (bed sensor, gateway, central server, nurse dashboard) belongs to.
- Explain one specific security risk at the layer you consider most vulnerable in this deployment, and propose a concrete mitigation that fits within the hospital's policy constraints.
- Explain whether edge processing, cloud processing, or on-premise processing is most appropriate here and why.

---

## Scenario B: City-Wide Smart Parking System

A mid-size city installs magnetic vehicle-detection sensors in 10,000 parking spaces. Each sensor transmits occupancy status once per minute over LoRaWAN to city-owned base stations. A backend server aggregates real-time occupancy data and exposes a public REST API that navigation apps query to show available parking. The city is concerned that the public API could be manipulated to generate fake availability data, causing traffic congestion.

In 175–225 words, address all of the following:

- Map the three major system elements (sensors, base stations, backend server plus API) to their architecture layers.
- Identify which OWASP IoT Top 10 item is most relevant to the city's concern about fake availability data, and explain why.
- Propose two specific controls — one at the device/network level and one at the application level — that would reduce the risk of data manipulation.

---

## Scenario C: Industrial Cold Chain Monitoring

A pharmaceutical distributor ships temperature-sensitive vaccines across the country in refrigerated trucks. Each truck has a temperature logger that samples every 30 seconds and a cellular modem that streams readings to a cloud platform. A compliance dashboard shows regulators whether every shipment remained within the required 2–8 degree Celsius range for its entire journey. If temperature goes out of range, the driver must receive an in-cab alert within 10 seconds.

In 175–225 words, address all of the following:

- Identify all IoT architecture layers present in this system and give one specific component example at each layer.
- Explain why the 10-second alert requirement affects your choice of where the threshold-checking logic should run.
- Identify one potential failure point in the network layer and describe what safeguard should be in place to prevent data loss if that failure occurs.

---

## Discussion Rubric

| Component | Criteria | Points |
|---|---|---|
| Initial Post | Addresses all three bullet points for the chosen scenario with technical accuracy | 3 |
| Initial Post | Uses correct IoT architecture terminology (layer names, component types, protocol names) | 2 |
| Initial Post | Meets the 175–225 word count requirement | 1 |
| Peer Response 1 | Provides substantive technical feedback or an alternative perspective (minimum 60 words) | 2 |
| Peer Response 2 | Provides substantive technical feedback or an alternative perspective (minimum 60 words) | 2 |
| Total | | 10 |

---

## Professor Nash's Notes

Choose one scenario and stick with it — do not partially address two scenarios. Your initial post must use at least three specific technical terms from the Module 01 glossary (examples: Perception layer, trust boundary, MQTT, edge device, protocol translation). Responses that only say "I agree" or "Great post" receive zero points for that response. Challenge a claim, add a detail your classmate missed, or provide a real-world example that supports or complicates their argument.

---

End of Discussion – Module 01
