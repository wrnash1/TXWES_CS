# Reading Guide – Module 04: IoT Protocols – MQTT, CoAP, HTTP/REST, and Zigbee

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Certification Target:** CompTIA IoT+ Domain 3

---

## Introduction

Module 04 examines the protocols that IoT devices use to communicate — from constrained sensors sending a few bytes per hour to enterprise backends routing millions of messages per second. Protocol selection affects system scalability, latency, power consumption, and security. Understanding each protocol's transport layer, overhead, authentication options, and vulnerabilities is directly tested on the CompTIA IoT+ exam.

---

## 1. Core Glossary

- **MQTT (Message Queuing Telemetry Transport):** A lightweight pub/sub protocol running over TCP (port 1883 plaintext, 8883 TLS). Requires a broker. Clients publish messages to topics and subscribe to receive messages on topics. Designed for constrained devices on unreliable networks. OASIS standard.

- **Publish-Subscribe Pattern:** A messaging architecture where publishers emit messages to named topics on a broker without addressing specific receivers, and subscribers register interest in topics. The broker decouples senders from receivers, enabling many-to-many communication. A compromised broker can intercept all messages on all topics.

- **MQTT Broker:** The central routing server in an MQTT deployment. Accepts published messages, maintains subscription registrations, and routes messages to matching subscribers. Examples: Mosquitto (open source), HiveMQ, AWS IoT Core, EMQX.

- **MQTT QoS:** Three delivery guarantee levels. QoS 0 (at most once, fire and forget), QoS 1 (at least once, requires PUBACK acknowledgment), QoS 2 (exactly once, four-packet handshake: PUBLISH, PUBREC, PUBREL, PUBCOMP).

- **MQTT Retained Message:** A message published with the `retain=True` flag. The broker stores the last retained message on a topic and delivers it immediately to any new subscriber, giving them the current state without waiting for the next publish.

- **Last Will and Testament (LWT):** An MQTT feature where a client pre-registers a message to be published by the broker if the client disconnects unexpectedly. Used to detect device outages and publish an "offline" status to monitoring systems.

- **CoAP (Constrained Application Protocol):** A request-response protocol for constrained nodes defined in IETF RFC 7252. Runs over UDP (port 5683 plain, 5684 DTLS). Uses GET/POST/PUT/DELETE methods like HTTP. Secured with DTLS. Supports an Observe extension for resource subscriptions.

- **Confirmable vs. Non-Confirmable CoAP:** Confirmable (CON) messages require an ACK from the recipient. Non-confirmable (NON) messages are sent without acknowledgment. CON maps to QoS 1; NON maps to QoS 0.

- **DTLS (Datagram TLS):** The UDP equivalent of TLS. Provides encryption, authentication, and integrity for datagram-based protocols. Required for securing CoAP in production.

- **HTTP/REST:** Hypertext Transfer Protocol with Representational State Transfer design principles. Request-response over TCP (port 80 plain, 443 TLS). High per-request overhead. Appropriate for cloud APIs, dashboards, and device provisioning.

- **AMQP (Advanced Message Queuing Protocol):** Enterprise-grade pub/sub and message queue protocol over TCP (port 5672 plain, 5671 TLS). OASIS standard. Supports complex routing, guaranteed delivery, and transaction semantics. Used in backend IoT systems, not on constrained devices. Implemented by RabbitMQ.

- **Zigbee:** A wireless mesh protocol built on IEEE 802.15.4 (PHY and MAC layers). Operates at 2.4 GHz. Data rate: 250 kbps. Range: 10–100 m. Supports self-forming, self-healing mesh networks. Uses AES-128 for link and network layer encryption. Common in smart home (Philips Hue, SmartThings) and building automation.

- **IEEE 802.15.4:** The PHY and MAC layer standard underlying Zigbee, 6LoWPAN, Thread, and WirelessHART. Defines low-power, low-data-rate wireless communication for personal area networks (PAN).

- **Zigbee Coordinator:** The single device in a Zigbee network that initializes and maintains the network, manages the routing table, and acts as the Trust Center for key distribution.

- **Zigbee Router:** A Zigbee device that can relay messages for other devices, extending network range. Typically mains-powered.

- **Zigbee End Device:** A leaf node in the Zigbee network (typically battery-powered sensor). Cannot route traffic. Sleeps most of the time to conserve power. Must communicate through a nearby router or coordinator.

---

## 2. IoT Protocol Comparison Table

| Attribute | MQTT | CoAP | HTTP/REST | AMQP |
|---|---|---|---|---|
| Full name | Message Queuing Telemetry Transport | Constrained Application Protocol | Hypertext Transfer Protocol | Advanced Message Queuing Protocol |
| Transport | TCP | UDP | TCP | TCP |
| Message pattern | Publish/subscribe | Request/response | Request/response | Queue + publish/subscribe |
| Overhead | Very low | Very low | High | Medium |
| QoS levels | 0 (fire/forget), 1 (at-least-once), 2 (exactly-once) | CON (ack) / NON (no ack) | None native | Persistent delivery |
| Broker required | Yes | No | No | Yes |
| Plain port | 1883 | 5683 | 80 | 5672 |
| Secure port | 8883 (TLS) | 5684 (DTLS) | 443 (TLS) | 5671 (TLS) |
| Security | TLS + client certs / password | DTLS | TLS | TLS / SASL |
| Standard body | OASIS | IETF RFC 7252 | IETF / W3C | OASIS |
| Suitable for constrained MCU | Yes | Yes | No | No |
| Subscription mechanism | Topic wildcard subscribe | Observe extension (RFC 7641) | Polling / WebSocket | Queue binding |

---

## 3. Wireless Technology Comparison Table

| Technology | Range | Bandwidth | Power | Frequency | Topology | Use case |
|---|---|---|---|---|---|---|
| Wi-Fi (802.11) | 30–100 m | Up to 9.6 Gbps | High | 2.4/5/6 GHz | Star | Cameras, gateways, hubs |
| Bluetooth LE | 10–100 m | 1–2 Mbps | Very low | 2.4 GHz | Star / mesh | Wearables, beacons |
| Zigbee | 10–100 m | 250 kbps | Very low | 2.4 GHz | Mesh | Smart home, building automation |
| Z-Wave | 30–100 m | 100 kbps | Low | 908 MHz (US) | Mesh | Smart home |
| LoRaWAN | 2–15 km | 0.3–50 kbps | Extremely low | 915 MHz (US, unlicensed) | Star-of-stars | Agriculture, smart city |
| NB-IoT | 1–10 km | 200 kbps | Very low | Licensed LTE | Cellular | Smart meters, asset tracking |
| LTE-M | Wide area | 1 Mbps | Low | Licensed LTE | Cellular | Wearables, vehicles |
| 6LoWPAN | 10–100 m | 250 kbps | Very low | 2.4 GHz | Mesh | IPv6 sensor mesh |

---

## 4. OWASP IoT Top 10 Reference

Protocols interact with multiple OWASP items:

1. **OWASP IoT #1 – Weak, Guessable, or Hardcoded Passwords:** MQTT brokers configured with default or no authentication passwords. Mitigation: require strong passwords or X.509 certificates.

2. **OWASP IoT #2 – Insecure Network Services:** MQTT broker running on port 1883 with no authentication. Any device on the network can publish or subscribe. Mitigation: disable port 1883, run only on 8883 with TLS.

3. **OWASP IoT #3 – Insecure Ecosystem Interfaces:** Unprotected HTTP management interfaces on MQTT brokers or Zigbee coordinators. Mitigation: HTTPS with strong authentication on all management interfaces.

4. **OWASP IoT #7 – Insecure Data Transfer and Storage:** MQTT over plaintext port 1883 exposes all telemetry. CoAP over UDP port 5683 without DTLS exposes all sensor readings to interception. Mitigation: enforce TLS/DTLS for all protocol transports.

---

## 5. Sensor Types Reference

| Sensor | Interface | Typical Protocol for Cloud Upload | Notes |
|---|---|---|---|
| DHT22 temperature/humidity | GPIO single-wire | MQTT | ESP32 or Pi gateway publishes readings |
| BME280 environmental | I2C / SPI | MQTT or CoAP | Multi-parameter in one chip |
| Motion (PIR) | GPIO digital | MQTT (event-driven) | Publishes on state change, not timer |
| Smart meter | RS-485 / Zigbee | MQTT (via gateway) | Zigbee gateway bridges to MQTT |
| Industrial PLC | Modbus TCP | AMQP (via gateway) | Enterprise backend routing |
| GPS tracker | UART NMEA | MQTT | Cellular modem + MQTT client |

---

## 6. IIoT Purdue Model Reference

- Level 0: Sensors and actuators. Zigbee end devices, Modbus sensors.
- Level 1: PLCs and RTUs. Local Zigbee/Modbus gateways.
- Level 2: SCADA HMI. MQTT broker serving HMI clients.
- Level 3: MES and historians. AMQP or MQTT feeding data historians.
- Level 3.5: Industrial DMZ. Protocol translation from OT protocols to IT-friendly MQTT/REST.
- Level 4–5: ERP and corporate IT. REST APIs consuming IoT telemetry.

---

## 7. Exam Tips for Module 04

1. MQTT runs over TCP. CoAP runs over UDP. This single distinction eliminates half the wrong answers on protocol selection questions.

2. MQTT requires a broker. CoAP does not — it supports direct device-to-device request-response.

3. The MQTT plain port is 1883. The TLS port is 8883. An unprotected broker on 1883 is OWASP IoT #2 (Insecure Network Services) and OWASP IoT #7 (Insecure Data Transfer).

4. MQTT QoS 2 guarantees exactly-once delivery using a four-packet handshake (PUBLISH, PUBREC, PUBREL, PUBCOMP). QoS 1 uses a two-packet exchange (PUBLISH, PUBACK). QoS 0 is fire and forget.

5. Zigbee uses IEEE 802.15.4 at the physical and MAC layers. AES-128 encryption. Self-healing mesh topology. Three device roles: Coordinator (one per network), Router (relay), End Device (leaf/sleepy).

6. The MQTT `+` wildcard matches exactly one topic level. The `#` wildcard matches all remaining levels. Know an example of each for the exam.

7. CoAP's Observe extension (RFC 7641) allows a CoAP client to subscribe to resource updates, providing push-like behavior over UDP without a broker.

8. AMQP is not used directly on constrained IoT devices. It is a backend enterprise messaging protocol. Gateways translate from MQTT/CoAP to AMQP when integrating with enterprise message brokers.

---

## 8. Study Checklist

- [ ] Memorize all 16 glossary terms.
- [ ] Study the protocol comparison table — be able to fill in every cell from memory.
- [ ] Study the wireless technology table — know range, bandwidth, and spectrum type for LoRaWAN and NB-IoT.
- [ ] Review all four OWASP items and connect each to a specific protocol misconfiguration.
- [ ] Review the MQTT Paho code examples in the video script and trace the full message flow.
- [ ] Review all 8 exam tips.
- [ ] Complete the Module 04 Lab (Paho MQTT publish-subscribe and broker security analysis).
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 9. Official References

- OASIS MQTT specification at docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
- IETF RFC 7252 CoAP at rfc-editor.org/rfc/rfc7252
- Mosquitto MQTT broker documentation at mosquitto.org/documentation
- OWASP IoT Security Project at owasp.org/www-project-internet-of-things

---

End of Reading Guide – Module 04
