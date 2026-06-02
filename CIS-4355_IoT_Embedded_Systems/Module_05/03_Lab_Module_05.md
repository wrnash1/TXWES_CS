# Lab Activity – Module 05: IoT Networking – Wi-Fi, Bluetooth, LoRaWAN, NB-IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Points:** 100
**Submission:** Canvas – Module 05 Lab Assignment

---

## Overview

In this lab you will analyze wireless technology selection scenarios, evaluate a Wi-Fi network security configuration, trace a LoRaWAN uplink message through the full network architecture, and produce a technology comparison matrix. No radio hardware is required. All work is analytical, written, and diagrammatic.

---

## Learning Objectives

By completing this lab you will be able to:

- Select the appropriate wireless technology for a given set of requirements using quantitative justification.
- Evaluate a Wi-Fi IoT network configuration against OWASP IoT security requirements.
- Trace a LoRaWAN uplink from end device through gateway to network server with correct terminology.
- Explain the two LoRaWAN AES-128 session keys and which system entity holds each key.
- Design a network segmentation plan for a mixed IoT/corporate office environment.

---

## Prerequisites

- Completed Module 05 video lecture and reading guide.
- Access to a text editor or word processor for written responses.
- Drawing tool for the network diagram in Part 4 (draw.io, paper and photo, or any diagram tool).

---

## Part 1: Wireless Technology Selection Matrix (25 points)

### Part 1 Instructions

For each of the five deployment scenarios below, complete a row in the selection table. For each scenario:

- Select the single most appropriate wireless technology from this list: Wi-Fi, BLE, Zigbee, LoRaWAN, NB-IoT, LTE-M.
- State the primary reason for the selection (one specific attribute such as range, power, bandwidth, or spectrum).
- State one specific reason why each of the two noted alternative technologies is unsuitable.

Scenario 1: A cattle ranch deploys GPS-enabled health monitors on 3,000 cattle across 50,000 acres. Each monitor transmits a location and temperature reading once every 2 hours. The monitor must run for 2 years on a battery pack. No cellular coverage exists in the area.

Scenario 2: A marathon race uses chest-worn heart-rate monitors on 5,000 runners. A smartphone app on each runner's phone collects the data in real time. The monitor must weigh under 15 grams and run for 8 hours on a 50 mAh battery.

Scenario 3: A port authority deploys 200 container tracking devices in a fully cellular-covered urban port. Each device must report GPS coordinates every 10 minutes. The port operations center requires 99.9% uptime SLA and access to device firmware updates over the air.

Scenario 4: A 400-unit apartment building deploys smart thermostats, door sensors, and leak detectors in every unit. The building manager uses a central hub on each floor. Battery life of 2 years is required.

Scenario 5: A television production studio deploys 4K wireless cameras. Each camera streams 25 Mbps compressed video to a recording server 15 meters away in the studio control room.

Format your response as a table:

| Scenario | Selected Technology | Primary Reason | Alternative 1 Eliminated Because | Alternative 2 Eliminated Because |
|---|---|---|---|---|
| 1 | (answer) | (answer) | (answer) | (answer) |
| ... | | | | |

### Part 1 Grading Rubric

| Criterion | Points |
|---|---|
| Correct technology selected for all 5 scenarios | 15 |
| Primary reason references a specific attribute (not vague) | 5 |
| Each alternative elimination is technically specific | 5 |
| Total | 25 |

---

## Part 2: Wi-Fi IoT Security Configuration Audit (25 points)

### Part 2 Instructions

A small manufacturing company has deployed 40 IoT temperature and humidity sensors in its production facility. The following configuration currently exists:

- All 40 sensors connect to the company's main corporate Wi-Fi network (SSID: TexasWidgetCo).
- Security: WPA2-Personal with passphrase "widget2020" shared across sensors and employee laptops.
- WPS is enabled on the access point for easy device onboarding.
- The same network hosts the plant manager's laptop, the payroll server, and the production database.
- Sensor firmware has the Wi-Fi SSID and passphrase hardcoded as string literals in the firmware image.

Identify each security issue, map it to the relevant OWASP IoT Top 10 item, and provide a specific remediation.

Use the table format below for each of the five identified issues:

| Issue | OWASP IoT Item | Attack Scenario | Specific Remediation |
|---|---|---|---|
| All devices on one flat network | (OWASP item number and name) | (describe the attack) | (specific config change) |
| ... | | | |

The five issues to find and document:

- Flat network with no IoT/corporate segmentation.
- WPA2-Personal shared passphrase.
- WPS enabled.
- Hardcoded Wi-Fi credentials in firmware.
- Sensors on same segment as payroll and production database.

After your table, write a 3–5 sentence paragraph describing the priority order in which you would remediate these issues and why.

### Part 2 Grading Rubric

| Criterion | Points |
|---|---|
| All 5 issues identified in table | 10 |
| OWASP item correctly cited for each issue | 5 |
| Attack scenario accurately described for each issue | 5 |
| Remediation is specific (not generic advice) | 3 |
| Remediation priority paragraph present and justified | 2 |
| Total | 25 |

---

## Part 3: LoRaWAN Message Trace (25 points)

### Part 3 Instructions

Trace the following LoRaWAN uplink scenario through the full network architecture. Answer all five questions in complete sentences.

Scenario: A Class A soil moisture sensor (DevEUI: AA:BB:CC:DD:01:02:03:04) wakes from sleep and takes a soil moisture reading of 34% relative water content. It formats a 12-byte application payload and transmits an uplink LoRaWAN frame. Three gateways — GW-North (RSSI: -98 dBm), GW-South (RSSI: -89 dBm), and GW-East (RSSI: -102 dBm) — all receive the same uplink frame and forward it to The Things Network (TTN) network server. The network server delivers the payload to the application server. The application server decodes the reading and stores it in a time-series database.

Question 1: What role does each gateway play in forwarding the uplink? Specifically, does each gateway decrypt the application payload before forwarding, or does it forward the encrypted packet? Explain why.

Question 2: The network server receives three copies of the same uplink from three gateways. What does the network server do with the duplicates, and which copy would it prefer and why?

Question 3: The application payload is encrypted with the AppSKey. Which entity — the gateway, the network server, or the application server — holds the AppSKey and decrypts the payload? Explain the security benefit of this design.

Question 4: After processing the uplink, the network server opens two downlink receive windows for the Class A device. Describe the timing of RX1 and RX2 windows and explain what the network server would send in a downlink if it needed to adjust the device's spreading factor.

Question 5: An attacker captures the LoRaWAN uplink frame from the air. The attacker can see the DevAddr (device address) and the encrypted payload. Explain what the attacker cannot do with this information alone, and what would need to be compromised for the attacker to decrypt the payload.

### Part 3 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: Gateway packet forwarding role correctly described (no decryption) | 5 |
| Question 2: Deduplication at network server and best-path selection correct | 5 |
| Question 3: AppSKey holder correctly identified, security benefit explained | 5 |
| Question 4: RX1/RX2 timing and ADR MAC command correctly described | 5 |
| Question 5: Attacker limitation and required compromise correctly explained | 5 |
| Total | 25 |

---

## Part 4: IoT Network Segmentation Diagram (25 points)

### Part 4 Instructions

A Texas Wesleyan office building has the following devices that need network connectivity:

- 20 IP security cameras.
- 15 BLE-to-Wi-Fi bridge gateways (each serves multiple BLE sensors in conference rooms).
- 10 network-connected printers.
- 50 employee laptops.
- 1 HR server containing employee records.
- 1 student records server.
- 2 Wi-Fi access points (both dual-band, VLAN-capable).

Design a network segmentation architecture for this building. Produce a network diagram and a written policy.

The diagram must show:

- At minimum three VLANs: IoT devices, corporate IT (printers and laptops), and servers.
- Both access points, labeled with which SSID maps to which VLAN.
- A firewall or Layer 3 switch at the boundary between VLANs.
- Labeled firewall rules (at least 4 rules shown as annotations on the diagram): what traffic is permitted and what is blocked between each VLAN pair.
- The internet uplink and where it connects.

The written policy (150–200 words) must specify:

- Which device types belong to each VLAN and why.
- The firewall rules in plain English (for example: "IoT VLAN may only initiate outbound HTTPS connections to cloud endpoints on port 443. All other traffic from IoT VLAN is dropped.").
- How a newly purchased IP camera would be onboarded to the correct VLAN.

### Part 4 Grading Rubric

| Criterion | Points |
|---|---|
| Diagram shows minimum three VLANs with correct device placement | 8 |
| Firewall or Layer 3 switch boundary shown with 4 labeled rules | 8 |
| Written policy identifies VLAN membership and firewall rules in plain English | 6 |
| Onboarding procedure for new device described | 3 |
| Total | 25 |

---

## Submission Checklist

- [ ] Part 1: Technology selection matrix table (5 rows complete).
- [ ] Part 2: Security audit table (5 issues documented) and remediation priority paragraph.
- [ ] Part 3: All 5 LoRaWAN trace questions answered in complete sentences.
- [ ] Part 4: Network segmentation diagram file and written policy.

---

## Overall Grading Summary

| Part | Description | Points |
|---|---|---|
| 1 | Wireless technology selection matrix | 25 |
| 2 | Wi-Fi IoT security configuration audit | 25 |
| 3 | LoRaWAN message trace | 25 |
| 4 | IoT network segmentation diagram | 25 |
| Total | | 100 |

---

End of Lab – Module 05
