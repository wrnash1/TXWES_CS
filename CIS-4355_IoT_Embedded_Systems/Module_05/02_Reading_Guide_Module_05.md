# Reading Guide – Module 05: IoT Networking – Wi-Fi, Bluetooth, LoRaWAN, NB-IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Certification Target:** CompTIA IoT+ Domain 3

---

## Introduction

Module 05 compares the four dominant wireless technologies in IoT deployments: Wi-Fi, Bluetooth Low Energy, LoRaWAN, and NB-IoT. Protocol selection at this layer determines battery life, deployment cost, coverage area, and the security controls available. All four technologies appear on the CompTIA IoT+ exam — expect scenario questions asking you to select the appropriate technology and justify the choice.

---

## 1. Core Glossary

- **Wi-Fi (IEEE 802.11):** Wireless LAN standard family. IoT-relevant versions: 802.11n (2.4/5 GHz, up to 600 Mbps), 802.11ac/Wi-Fi 5 (5 GHz, up to 3.5 Gbps), 802.11ax/Wi-Fi 6 (2.4/5/6 GHz, up to 9.6 Gbps). High bandwidth, high power consumption, 30–100 m indoor range.

- **WPA3 (Wi-Fi Protected Access 3):** The current recommended Wi-Fi security standard. WPA3-Personal uses SAE (Simultaneous Authentication of Equals) replacing PSK, providing forward secrecy. WPA3-Enterprise uses 192-bit cryptographic suite for high-security environments. Resists offline dictionary attacks that compromised WPA2-Personal.

- **VLAN (Virtual LAN):** A logical network segment configured at the switch/access point level. IoT devices should be placed on a dedicated VLAN, isolated from corporate IT devices by firewall rules. Prevents lateral movement if a device is compromised.

- **Bluetooth Low Energy (BLE):** Low-power Bluetooth mode in the Bluetooth Core Specification. Operates at 2.4 GHz. Uses 40 channels with adaptive frequency hopping. Optimized for short-burst transmissions with long sleep intervals. Range: 10–100 m (Long Range mode: up to 400 m at reduced data rate).

- **BLE Advertising:** The mechanism by which a BLE peripheral broadcasts its presence to nearby central devices. Advertising packets are transmitted on three dedicated advertising channels at regular intervals. Beacons use advertising exclusively — they never form a connected session.

- **BLE Pairing Modes:** Methods for establishing an encrypted BLE connection. Just Works (no authentication, MITM-vulnerable), Passkey Entry (6-digit PIN), Numeric Comparison (both sides confirm same number), Out-of-Band/OOB (exchange via NFC or QR code).

- **LoRa:** Semtech's proprietary chirp spread spectrum (CSS) modulation technique used at the physical layer for long-range, low-power transmission. Spreading factor (SF7–SF12) controls the range/data-rate tradeoff — higher spreading factor means longer range but lower data rate.

- **LoRaWAN:** The MAC and network layer protocol built on top of LoRa modulation. Defines three device classes (A, B, C), security architecture (two AES-128 session keys), and network architecture (end devices, gateways, network server, application server). Managed by the LoRa Alliance.

- **LoRaWAN Device Classes:** Class A (lowest power): device-initiated transmissions only, two downlink windows after each uplink. Class B: synchronized downlink slots in addition to Class A behavior. Class C (lowest latency): device listens continuously except when transmitting; highest power.

- **Spreading Factor (SF):** In LoRa, higher SF = more time on air per bit = longer range but lower data rate and higher energy per bit. SF7 is fastest and shortest range; SF12 is slowest and longest range. The network server performs adaptive data rate (ADR) to select the appropriate SF for each device.

- **NB-IoT (Narrowband IoT):** 3GPP LTE Release 13 cellular IoT standard. Uses 200 kHz licensed LTE spectrum. Supports Power Saving Mode (PSM) and extended Discontinuous Reception (eDRX) for multi-year battery life. Provides superior indoor penetration and carrier-grade SLA compared to LoRaWAN.

- **PSM (Power Saving Mode):** An NB-IoT and LTE-M feature where the device negotiates with the network to sleep for extended periods (minutes to hours) with no network registration, then wake up, transmit, and sleep again. Eliminates the power cost of periodic network keepalives.

- **LPWAN (Low Power Wide Area Network):** A class of wireless technologies designed for long-range, low-power, low-data-rate IoT communications. Includes LoRaWAN, NB-IoT, LTE-M, Sigfox, and RPMA. Fills the gap between short-range personal area networks and power-intensive cellular data.

---

## 2. IoT Protocol Comparison Table

| Attribute | MQTT | CoAP | HTTP/REST | AMQP |
|---|---|---|---|---|
| Transport | TCP | UDP | TCP | TCP |
| Pattern | Publish/subscribe | Request/response | Request/response | Queue + pub/sub |
| Overhead | Very low | Very low | High | Medium |
| Suitable for constrained devices | Yes | Yes | No | No |
| Broker required | Yes | No | No | Yes |
| Security | TLS (port 8883) | DTLS (port 5684) | TLS (port 443) | TLS/SASL |

---

## 3. Wireless Technology Comparison Table

| Technology | Range | Max Bandwidth | Idle Power | Freq. | Spectrum | Topology | Best Use Case |
|---|---|---|---|---|---|---|---|
| Wi-Fi 802.11n | 30–100 m | 600 Mbps | High (~500 mA) | 2.4/5 GHz | Unlicensed | Star | Gateways, cameras, edge nodes |
| BLE 5.0 | 10–100 m | 2 Mbps | Very low (<10 µA sleep) | 2.4 GHz | Unlicensed | Star / mesh | Wearables, beacons, sensors |
| Zigbee | 10–100 m | 250 kbps | Very low | 2.4 GHz | Unlicensed | Mesh | Smart home, building automation |
| Z-Wave | 30–100 m | 100 kbps | Low | 908 MHz (US) | Unlicensed | Mesh | Smart home |
| LoRaWAN | 2–15 km | 50 kbps | Extremely low (<1 µA avg) | 915 MHz (US) | Unlicensed | Star-of-stars | Agriculture, smart city, remote |
| NB-IoT | 1–10 km | 200 kbps | Very low (PSM) | Licensed LTE | Licensed | Cellular | Urban, indoor, carrier SLA |
| LTE-M | Wide area | 1 Mbps | Low | Licensed LTE | Licensed | Cellular | Wearables, vehicle tracking |
| 6LoWPAN | 10–100 m | 250 kbps | Very low | 2.4 GHz | Unlicensed | Mesh | IPv6 sensor mesh |

---

## 4. LoRaWAN Network Architecture Reference

The LoRaWAN architecture has four layers:

- **End Devices:** Sensors and actuators with LoRa radios. Transmit uplink packets. Receive downlink commands in receive windows after uplink.
- **Gateways:** Receive all LoRa signals in range and forward packets over IP to the network server. Simple packet forwarders — no message interpretation. Multiple gateways can receive the same uplink for redundancy.
- **Network Server:** Deduplicates packets received by multiple gateways. Manages device addresses, frame counters, and ADR. Routes decrypted MAC commands. Forwards application payloads to the application server.
- **Application Server:** Decrypts and processes application payloads using the AppSKey. Interfaces with business applications and dashboards.

LoRaWAN security keys:

- **NwkSKey (Network Session Key):** Shared between end device and network server. Authenticates MAC messages and encrypts MAC commands.
- **AppSKey (Application Session Key):** Shared between end device and application server. Encrypts application payload. Network server never sees plaintext payload.

---

## 5. OWASP IoT Top 10 Reference

Items most relevant to Module 05 networking topics:

1. **OWASP IoT #1 – Weak, Guessable, or Hardcoded Passwords:** Wi-Fi SSID and password hardcoded in firmware. Exposed via `strings` on firmware binary or physical UART access. Mitigation: provision credentials via secure manufacturing process or secure element.

2. **OWASP IoT #2 – Insecure Network Services:** Devices on the same network segment as corporate IT. Lack of VLAN segmentation allows lateral movement. Mitigation: dedicated IoT VLAN with firewall rules.

3. **OWASP IoT #9 – Insecure Default Settings:** WPS enabled by default on access points. BLE Just Works pairing enabled by default on door locks. Mitigation: establish and enforce a secure baseline configuration at deployment.

4. **OWASP IoT #10 – Lack of Physical Hardening:** NB-IoT SIM cards accessible via open device enclosures. LoRaWAN root keys extractable from unprotected flash. Mitigation: tamper-evident enclosures, secure element for key storage.

---

## 6. Sensor Types Reference

| Sensor | Typical Wireless Radio | Power Requirement | Notes |
|---|---|---|---|
| Temperature/humidity (indoor) | BLE or Wi-Fi | Battery or USB | Short range sufficient |
| Soil moisture (outdoor, rural) | LoRaWAN | Battery (multi-year) | Long-range, low-rate |
| Smart meter (utility) | NB-IoT or Zigbee | Mains (utility) | Urban, carrier SLA |
| Asset tracker (vehicle) | LTE-M | Vehicle power | Mobility, wide area |
| Smart lock (residential) | Zigbee or BLE | Battery | Short range, mesh |
| Industrial vibration | Wi-Fi or wired | Mains | High data rate |

---

## 7. IIoT Purdue Model Reference

- Level 0: Physical sensors. End nodes using LoRaWAN, BLE, or Zigbee.
- Level 1: PLCs and RTUs. Local gateways converting local radio to IP.
- Level 2: SCADA HMI. Wi-Fi or wired Ethernet to control room.
- Level 3: MES. IP network with IT-style firewall rules.
- Level 3.5: Industrial DMZ. Strict protocol filtering between OT and IT.
- Level 4–5: Corporate IT. Separate from OT by the DMZ.

Network segmentation between Purdue levels is the industrial equivalent of IoT VLAN isolation.

---

## 8. Exam Tips for Module 05

1. LoRaWAN uses unlicensed ISM spectrum (915 MHz US, 868 MHz EU). NB-IoT uses licensed cellular spectrum. This is the most commonly tested distinguishing attribute.

2. BLE Just Works pairing is vulnerable to man-in-the-middle attacks because there is no user confirmation step. Use Numeric Comparison or OOB for any security-sensitive BLE application.

3. Wi-Fi IoT devices require network segmentation via VLAN. Never place IoT devices on the same VLAN as corporate laptops or servers.

4. LoRaWAN spreading factor (SF) tradeoff: higher SF = longer range + lower data rate. SF12 reaches the farthest but sends data slowest.

5. LoRaWAN has two AES-128 session keys: NwkSKey (network layer) and AppSKey (application layer). The network server never decrypts application payloads.

6. NB-IoT Power Saving Mode (PSM) allows the device to sleep for extended periods without network keepalives, enabling multi-year battery life on a cellular connection.

7. WPS should be disabled on any access point serving IoT devices. WPS PIN brute-force attacks can recover the network key in hours.

8. The key distinguisher between LoRaWAN and Zigbee is range. Zigbee is 10–100 m per hop. LoRaWAN is 2–15 km. For deployments spanning kilometers, Zigbee is not viable regardless of its mesh relay capability.

---

## 9. Study Checklist

- [ ] Memorize all 12 glossary terms, especially spreading factor, PSM, VLAN, and BLE pairing modes.
- [ ] Study the wireless technology comparison table — know range, bandwidth, spectrum type, and power for all 8 technologies.
- [ ] Draw the LoRaWAN network architecture (end device to gateway to network server to application server) from memory.
- [ ] Review all four OWASP items and connect each to a specific wireless technology vulnerability.
- [ ] Review the sensor types table and match each sensor to its appropriate radio technology.
- [ ] Review all 8 exam tips.
- [ ] Complete the Module 05 Lab.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 10. Official References

- Wi-Fi Alliance at wi-fi.org
- Bluetooth specification at bluetooth.com/specifications
- LoRa Alliance and LoRaWAN specification at lora-alliance.org
- OWASP IoT Security Project at owasp.org/www-project-internet-of-things

---

## 9. Supplemental Resources

**1. LoRa Alliance — LoRaWAN Specification and Regional Parameters**
[https://lora-alliance.org/resource_hub/lorawan-specification-v1-0-3/](https://lora-alliance.org/resource_hub/lorawan-specification-v1-0-3/)
The official LoRaWAN MAC specification and the companion Regional Parameters document (covering US915, EU868, and other frequency plans). Required reading to understand spreading factors, payload size limits, duty cycle rules, and the OTAA vs. ABP activation procedures tested on the CompTIA IoT+ exam.

**2. Bluetooth SIG — Core Specification Overview**
[https://www.bluetooth.com/specifications/specs/core-specification-5-4/](https://www.bluetooth.com/specifications/specs/core-specification-5-4/)
The official Bluetooth Core Specification from the Bluetooth SIG. The overview section covers BLE advertising, GATT profiles, pairing modes (Just Works, Passkey Entry, Numeric Comparison, OOB), and link encryption. Relevant to Module 05 pairing security questions.

**3. GSMA — NB-IoT and LTE-M Deployment Guide**
[https://www.gsma.com/iot/narrow-band-internet-of-things-nb-iot/](https://www.gsma.com/iot/narrow-band-internet-of-things-nb-iot/)
The GSMA industry group's resource page for NB-IoT, including deployment guides, PSM and eDRX configuration, coverage enhancement modes, and comparisons with LTE-M. Essential reference for understanding cellular IoT connectivity requirements and operator SLA considerations.

---

End of Reading Guide – Module 05
