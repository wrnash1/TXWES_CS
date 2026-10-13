# Discussion Forum – Module 04: IoT Protocols – MQTT, CoAP, HTTP/REST, and Zigbee

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Initial Post Due:** Wednesday 11:59 PM
**Peer Responses Due:** Sunday 11:59 PM
**Total Points:** 10

---

## Overview

This discussion asks you to apply IoT protocol selection knowledge to realistic deployment decisions and security scenarios. Choose one of three scenarios, analyze it using Module 04 concepts, and engage substantively with two classmates.

---

## Scenario A: Municipal Water Quality Monitoring

A city water utility deploys turbidity, pH, and chlorine sensors at 80 locations along the water distribution network. Each sensor reads every 10 minutes. The system must alert the operations center within 60 seconds of a reading going out of range. The utility's IT security policy requires all sensor data to be encrypted in transit and all devices to authenticate to the backend before publishing data. The utility uses a small team and prefers open-source software.

In 175–225 words, address all of the following:

- Recommend a specific IoT messaging protocol for this deployment (MQTT, CoAP, or HTTP/REST) and justify your choice by comparing it to at least one alternative on at least two attributes from the reading guide comparison table.
- Describe the specific broker configuration settings required to satisfy the IT security policy's encryption and authentication requirements.
- Explain what an MQTT Last Will and Testament (LWT) message would add to this system and how it would be configured for a water quality sensor.

---

## Scenario B: Connected Retail Smart Shelf

A grocery chain deploys weight sensors on shelves to detect when products need restocking. Each shelf has an ESP32 microcontroller reading 8 load cell sensors. The ESP32 connects to the store's Wi-Fi and must publish restocking alerts to a central inventory system. The deployment has 2,000 shelves across 50 stores. The inventory team is concerned about the scalability of managing 2,000 MQTT client connections.

In 175–225 words, address all of the following:

- Explain how MQTT's publish-subscribe model addresses the scalability concern compared to a design where each shelf contacts the inventory system directly with an HTTP POST request.
- Propose an MQTT topic hierarchy for this deployment. Show at least two full example topic strings and explain the structure you chose.
- Identify one specific OWASP IoT Top 10 risk introduced if the store Wi-Fi network is shared between the shelf sensors and the store's customer Wi-Fi, and propose a network architecture control to mitigate it.

---

## Scenario C: Hospital Building Automation Security Audit

A security auditor reviews a hospital's Zigbee-based building automation system that controls HVAC, lighting, and door access. During the audit, she discovers that a Zigbee network scan reveals 140 devices using the default Zigbee link key. She also discovers that a Zigbee sniffer placed near an air duct can capture all Zigbee frames from the access control system.

In 175–225 words, address all of the following:

- Explain the specific security vulnerability created by using the default Zigbee link key, including what an attacker with a commercial Zigbee development kit could do with this information.
- Identify which OWASP IoT Top 10 item this represents and explain why the physical proximity of the sniffer is relevant to the OWASP item selected.
- Propose a remediation plan covering two specific Zigbee security configuration changes the network administrator should make to prevent unauthorized devices from joining and to protect traffic from passive sniffing.

---

## Discussion Rubric

| Component | Criteria | Points |
|---|---|---|
| Initial Post | Addresses all three bullet points with technical accuracy | 3 |
| Initial Post | Uses specific Module 04 terminology (MQTT, CoAP, QoS, DTLS, LWT, Zigbee, ACL, etc.) | 2 |
| Initial Post | Meets the 175–225 word count | 1 |
| Peer Response 1 | Substantive technical engagement (minimum 60 words) | 2 |
| Peer Response 2 | Substantive technical engagement (minimum 60 words) | 2 |
| Total | | 10 |

---

## Professor Nash's Notes

All three scenarios have technically correct and incorrect answers — these are not purely subjective. If your classmate recommends the wrong protocol for a scenario, explain specifically which attribute of the protocol makes it unsuitable. If they propose a broker configuration that still leaves a security gap, identify the gap and provide the specific missing configuration line. One-sentence peer responses and general agreement receive zero points.

---

End of Discussion – Module 04
