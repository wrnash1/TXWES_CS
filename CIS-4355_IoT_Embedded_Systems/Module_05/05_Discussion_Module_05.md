# Discussion Forum – Module 05: IoT Networking – Wi-Fi, Bluetooth, LoRaWAN, NB-IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Initial Post Due:** Wednesday 11:59 PM
**Peer Responses Due:** Sunday 11:59 PM
**Total Points:** 10

---

## Overview

This discussion challenges you to apply wireless technology selection knowledge to realistic deployment constraints. The scenarios below have technically correct and incorrect answers. Choose one, analyze it with Module 05 concepts, and engage substantively with two classmates.

---

## Scenario A: Emergency Response Vehicle Tracking

A county emergency management agency wants to track the real-time GPS location of all 120 ambulances, fire trucks, and police vehicles on a map in the dispatch center. Each vehicle transmits a GPS update every 15 seconds while in service. The vehicles cover a geographic area of 400 square miles, including dense urban streets and rural highways with no Wi-Fi infrastructure. The dispatch center requires 99.5% message delivery reliability with no more than 30 seconds of location lag. Vehicles already have 12V electrical systems with no battery constraint.

In 175–225 words, address all of the following:

- Recommend a wireless technology for this deployment and justify your choice by comparing it on at least two attributes (range, bandwidth, power, spectrum, or reliability) against one alternative you considered and rejected.
- Explain why the 15-second update interval and 400 square-mile coverage area are decisive factors in your technology selection.
- Identify one security risk specific to the technology you selected, and propose a technical mitigation that a systems engineer would implement at deployment.

---

## Scenario B: University Classroom Occupancy System

Texas Wesleyan University wants to place occupancy sensors in all 85 classrooms. Each sensor detects whether a room is occupied using a passive infrared detector and transmits an occupancy change event (room occupied or room vacant) to a central facilities dashboard. Events are infrequent — the sensor may transmit as few as 4 times per day. Sensors are battery-powered and mounted above doorways. The IT department wants to avoid deploying new radio infrastructure. The campus already has full Wi-Fi coverage in all buildings.

In 175–225 words, address all of the following:

- Explain whether Wi-Fi is an appropriate choice for the battery-powered occupancy sensors in this deployment, citing the specific power consumption tradeoff that makes Wi-Fi problematic.
- Recommend an alternative wireless technology and explain how it connects to the existing campus infrastructure (describe the gateway or bridge device needed).
- Explain how VLAN segmentation should be applied to the occupancy sensors relative to the campus's existing student and faculty Wi-Fi networks, and what firewall rule should govern the sensors' outbound traffic.

---

## Scenario C: Offshore Oil Platform Sensor Network

An oil and gas company operates a fixed offshore platform 40 miles from the nearest shore station. The platform has 600 sensors monitoring pipeline pressure, temperature, gas concentration, and valve positions. Safety regulations require sensor readings to be delivered to the onshore operations center within 5 minutes of measurement. Communication to shore uses a dedicated point-to-point licensed microwave link. On the platform itself, the sensors are mounted throughout structures where running cable is expensive.

In 175–225 words, address all of the following:

- Recommend a wireless technology for the on-platform sensor network (connecting sensors to a central platform gateway) and justify the choice, noting why LoRaWAN and NB-IoT are unsuitable for the on-platform portion of this design.
- Explain what security measures must be applied to a Zigbee or BLE on-platform network operating in a safety-critical environment, referencing at least one OWASP IoT Top 10 item.
- Describe how the architecture would change if the company decided to add real-time 10 Hz vibration monitoring on 20 critical pumps, and explain which wireless technology would be appropriate for that specific subset of sensors.

---

## Discussion Rubric

| Component | Criteria | Points |
|---|---|---|
| Initial Post | Addresses all three bullet points with technical accuracy | 3 |
| Initial Post | Uses specific Module 05 terminology (VLAN, spreading factor, PSM, AppSKey, BLE pairing, etc.) | 2 |
| Initial Post | Meets the 175–225 word count | 1 |
| Peer Response 1 | Substantive technical engagement (minimum 60 words) | 2 |
| Peer Response 2 | Substantive technical engagement (minimum 60 words) | 2 |
| Total | | 10 |

---

## Professor Nash's Notes

Technology selection questions have defensible right answers. If a classmate recommends a technology that cannot meet a stated range, bandwidth, or power requirement, you should challenge it specifically — quote the numbers. If they recommend the right technology but propose a weak security control, add the missing control with an explanation. "I agree" or "Good post" earns zero points regardless of length.

---

End of Discussion – Module 05
