# Reading Guide – Module 01: IoT Architecture – Devices, Gateways, Cloud, and Edge

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Certification Target:** CompTIA IoT+ Domain 1

---

## Introduction

Welcome to Module 01. This reading guide supports your video lecture and lab by providing detailed reference material on IoT architecture layers, the roles of devices and gateways, edge versus cloud processing trade-offs, and the security considerations that apply at each level. Work through every section before attempting the quiz or lab. Pay particular attention to the exam tips – they are drawn directly from CompTIA IoT+ exam objectives.

---

## 1. Core Glossary

Review and memorize these definitions. Quiz questions are scenario-based, so you must recognize these concepts when they appear in unfamiliar contexts.

- **Perception Layer:** The bottom tier of the IoT architecture stack. Contains sensors, actuators, RFID tags, barcode readers, and the embedded microcontrollers that digitize physical measurements. Devices at this layer are typically constrained: low memory, limited CPU, battery-powered, and unable to run full operating systems.

- **Network Layer:** The communication fabric that moves digitized data from perception-layer devices toward processing services. Encompasses all wireless and wired transport technologies, gateways, protocol translators, routers, and firewalls. Responsible for reliable delivery, addressing, and transport security.

- **Processing and Middleware Layer:** The tier that receives raw telemetry and applies filtering, aggregation, transformation, rule evaluation, and storage. Contains message brokers, stream processors, time-series databases, and rules engines. This is where most IoT platform logic executes.

- **Application Layer:** The top tier presenting processed data to humans or consuming systems. Includes dashboards, mobile apps, REST APIs, alerting services, and digital twins. The interface between IoT data and business decision-making.

- **Edge Device:** A compute node deployed physically close to data sources that runs local analytics, filtering, or control logic. Reduces upstream bandwidth consumption and enables sub-millisecond response without cloud round-trips.

- **IoT Gateway:** A device that bridges two or more network protocols, typically translating a local short-range protocol (Zigbee, BLE, Z-Wave, Modbus) to a routable IP protocol (MQTT over TCP, HTTPS). Gateways often buffer data locally during internet outages.

- **Smart Sensor:** An integrated sensing unit combining a physical transducer, an onboard microcontroller for signal conditioning, and a wireless radio. Capable of digitizing, filtering, and transmitting readings autonomously. Examples include the BME280 (I2C, temperature/humidity/pressure) and DS18B20 (1-Wire, temperature).

- **Digital Twin:** A virtual software model of a physical IoT device or system that mirrors the real-time state of its physical counterpart. Used for simulation, predictive analytics, and remote diagnostics.

- **Actuator:** A device that converts a digital or electrical signal into a physical action. Examples include stepper motors, servo motors, relay switches, pneumatic valves, and LED indicators.

- **Protocol Translation:** The process of converting data encoded in one communication protocol into the format required by another. Essential at gateways where device-network protocols and IP-network protocols differ.

- **Defense in Depth:** A security strategy applying multiple independent layers of controls so that the failure of any single control does not compromise the entire system. Foundational to IoT security architecture.

- **Trust Boundary:** A point in a system architecture where data moves from a zone of one trust level to a zone of another. Authentication, encryption, and input validation must be enforced at every trust boundary.

---

## 2. IoT Protocol Comparison Table

The following table summarizes the four most commonly tested IoT messaging protocols. Expect direct comparison questions on the CompTIA IoT+ exam.

| Attribute | MQTT | CoAP | HTTP/REST | AMQP |
|---|---|---|---|---|
| Full name | Message Queuing Telemetry Transport | Constrained Application Protocol | Hypertext Transfer Protocol | Advanced Message Queuing Protocol |
| Transport | TCP | UDP | TCP | TCP |
| Message model | Publish/subscribe | Request/response | Request/response | Message queue + publish/subscribe |
| Overhead | Very low | Very low | High | Medium |
| QoS levels | 0, 1, 2 | None native (CON/NON) | None native | Persistent delivery |
| Suitable for | Constrained devices, unreliable links | Constrained devices, LAN | Web services, high-bandwidth | Enterprise messaging, financial |
| Security | TLS over TCP | DTLS over UDP | TLS | TLS/SASL |
| Typical port | 1883 (plain), 8883 (TLS) | 5683 (plain), 5684 (DTLS) | 80 (plain), 443 (TLS) | 5672 (plain), 5671 (TLS) |
| Broker required | Yes | No (peer-to-peer capable) | No | Yes |
| Standard body | OASIS | IETF RFC 7252 | IETF/W3C | OASIS |

Key exam point: MQTT runs over TCP and requires a broker. CoAP runs over UDP and can operate broker-less. HTTP/REST is too heavyweight for severely constrained devices but is fine for gateways and cloud APIs.

---

## 3. Wireless Technology Comparison Table

| Technology | Range | Bandwidth | Power | Frequency | Topology | Primary IoT Use Case |
|---|---|---|---|---|---|---|
| Wi-Fi (802.11) | 30–100 m | Up to 9.6 Gbps (Wi-Fi 6) | High | 2.4 / 5 / 6 GHz | Star | Cameras, smart home hubs, gateways |
| Bluetooth LE (BLE) | 10–100 m | 1–2 Mbps | Very low | 2.4 GHz | Star/mesh | Wearables, beacons, sensors |
| Zigbee (802.15.4) | 10–100 m | 250 kbps | Very low | 2.4 GHz | Mesh | Smart lighting, home automation |
| Z-Wave | 30–100 m | 100 kbps | Low | 908 MHz (US) | Mesh | Smart home devices |
| LoRaWAN | 2–15 km | 0.3–50 kbps | Extremely low | 915 MHz (US) | Star-of-stars | Agriculture, smart city, metering |
| NB-IoT | 1–10 km | 200 kbps | Very low | Licensed LTE | Cellular | Smart meters, asset tracking |
| LTE-M (Cat-M1) | Wide area | 1 Mbps | Low | Licensed LTE | Cellular | Wearables, vehicle tracking |
| 6LoWPAN | 10–100 m | 250 kbps | Very low | 2.4 GHz | Mesh | IPv6 mesh sensor networks |

Key exam point: LoRaWAN and NB-IoT are the two dominant LPWAN (Low Power Wide Area Network) technologies. LoRaWAN operates on unlicensed spectrum; NB-IoT uses licensed cellular spectrum.

---

## 4. OWASP IoT Top 10 Reference

The OWASP IoT Top 10 is a required reference for the CompTIA IoT+ security domain. You must be able to describe each item, recognize it in a scenario, and propose a mitigation.

1. **Weak, Guessable, or Hardcoded Passwords:** Devices shipped with default or hardcoded credentials that users never change. Mitigate by enforcing unique per-device credentials at manufacturing and requiring password change on first use.

2. **Insecure Network Services:** Unnecessary open ports and services (Telnet, FTP, unauthenticated HTTP management interfaces) expose devices to network attacks. Mitigate by disabling all unused services and applying network segmentation.

3. **Insecure Ecosystem Interfaces:** Weak security on web interfaces, mobile APIs, or cloud backend APIs. Mitigate with HTTPS everywhere, input validation, and strong authentication.

4. **Lack of Secure Update Mechanism:** Firmware updates transmitted over unencrypted channels or without signature verification. Mitigate with signed firmware images and TLS-protected delivery channels.

5. **Use of Insecure or Outdated Components:** Third-party libraries and OS components with known vulnerabilities embedded in device firmware. Mitigate with software bill of materials (SBOM) tracking and regular patching cycles.

6. **Insufficient Privacy Protection:** Devices collecting personal data without proper consent, encryption, or access controls. Mitigate with data minimization, encryption at rest, and GDPR/CCPA-compliant data handling.

7. **Insecure Data Transfer and Storage:** Sensitive data transmitted in plaintext or stored unencrypted on the device. Mitigate with TLS for transport and AES encryption for local storage.

8. **Lack of Device Management:** No mechanism for remote device inventory, monitoring, configuration, or decommissioning. Mitigate with a device management platform (AWS IoT Device Management, Azure IoT Hub) that enforces policy and enables remote wipe.

9. **Insecure Default Settings:** Default configurations with unnecessary features enabled, weak encryption settings, or permissive firewall rules. Mitigate by establishing a secure baseline configuration applied at provisioning.

10. **Lack of Physical Hardening:** Devices deployed without tamper detection, exposed debug ports (JTAG, UART), or unencrypted storage that can be read by physical access. Mitigate with epoxy-covered debug ports, tamper-evident seals, and encrypted flash storage.

---

## 5. Sensor Types Reference

| Category | Example Sensors | Signal Type | Common Interface |
|---|---|---|---|
| Temperature | DS18B20, NTC thermistor, PT100 RTD | Analog / digital | 1-Wire, I2C, SPI, ADC |
| Humidity | DHT11, DHT22, SHT31 | Digital | Single-wire, I2C |
| Pressure | BMP280, MPX5700 | Analog / digital | I2C, SPI, ADC |
| Motion / presence | PIR sensor, HC-SR501 | Digital (binary) | GPIO |
| Proximity | HC-SR04 ultrasonic, LIDAR-Lite | Digital pulse / I2C | GPIO, I2C |
| Light / lux | BH1750, VEML7700, photoresistor | Analog / digital | I2C, ADC |
| Gas / air quality | MQ-2, MQ-135, CCS811 | Analog / digital | ADC, I2C |
| Accelerometer | MPU-6050, ADXL345 | Digital | I2C, SPI |
| Current / power | INA219, ACS712 | Analog / digital | I2C, ADC |
| GPS / location | NEO-6M, ATGM336H | Digital NMEA | UART |

---

## 6. IIoT Purdue Model Reference

The Purdue Enterprise Reference Architecture (PERA) defines the security zone structure for industrial IoT (IIoT) and SCADA systems. It appears in Module 14 in depth but you should begin familiarizing yourself with it now.

- **Level 0 – Physical Process:** Sensors, actuators, physical machinery.
- **Level 1 – Intelligent Devices:** PLCs (Programmable Logic Controllers), RTUs (Remote Terminal Units), drives.
- **Level 2 – Control Systems:** DCS (Distributed Control Systems), SCADA HMI workstations.
- **Level 3 – Manufacturing Operations:** MES (Manufacturing Execution Systems), historians, batch management.
- **Level 3.5 – DMZ (Industrial DMZ):** Segmented buffer zone between OT and IT networks. Patching servers, data historians exposed to IT.
- **Level 4 – Business Logistics:** ERP, plant scheduling, supply chain systems.
- **Level 5 – Enterprise Network:** Corporate IT, internet-connected systems.

The key security principle: traffic between levels must pass through a firewall and be explicitly permitted. No direct connection from Level 0 to Level 4 is ever acceptable.

---

## 7. IoT Architecture Security Exam Tips

1. On architecture layer questions, always map physical sensing and actuation to the Perception layer. Map all communication infrastructure (radios, gateways, routers) to the Network layer.

2. When a question describes a latency requirement under 100 ms, the answer almost always involves edge processing rather than cloud processing.

3. The distinction between a gateway and an edge device is compute capability. A gateway translates protocols. An edge device runs application logic.

4. Defense in depth means applying controls at every layer independently. Never choose an answer that protects only one layer and assumes others are safe.

5. Trust boundaries require authentication, encryption, and input validation. Any answer that skips one of these three controls at a trust boundary is incomplete.

6. OWASP IoT Top 10 item 1 (hardcoded passwords) is the most frequently tested item. Know it, the attack scenario, and the mitigation cold.

7. The five-tier model explicitly separates Edge Processing (Tier 3) from Data Management (Tier 4). The three-tier model collapses these into a single Platform tier.

8. LoRaWAN operates on unlicensed spectrum (915 MHz in the US) and requires a LoRaWAN network server. NB-IoT uses licensed cellular spectrum and connects through a cellular carrier.

---

## 8. Study Checklist

Work through each item before moving to the quiz and lab.

- [ ] Memorize all 12 glossary terms and be able to use each in a sentence without looking.
- [ ] Review the four-layer architecture model and draw it from memory with one example component at each layer.
- [ ] Study the protocol comparison table and be able to explain when to choose MQTT over CoAP and vice versa.
- [ ] Review the wireless technology table and know the range, bandwidth, and power profile of LoRaWAN and NB-IoT.
- [ ] Read all 10 OWASP IoT Top 10 items and identify the architecture layer where each vulnerability primarily originates.
- [ ] Review the sensor types table and understand what interface (I2C, SPI, GPIO, UART) each category typically uses.
- [ ] Read the Purdue Model section and sketch the five levels with their primary system types.
- [ ] Review all 8 exam tips and confirm you can explain each without notes.
- [ ] Complete the Module 01 Lab before attempting the quiz.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 9. Recommended Official References

The following references are authoritative and free. No fabricated or third-party URLs are listed.

- Arduino official documentation and reference at arduino.cc/reference
- Raspberry Pi official documentation at raspberrypi.com/documentation
- OWASP IoT Security Project at owasp.org/www-project-internet-of-things
- IETF RFC 7252 (CoAP specification) at rfc-editor.org/rfc/rfc7252
- OASIS MQTT Version 5.0 specification at docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html

---

End of Reading Guide – Module 01
