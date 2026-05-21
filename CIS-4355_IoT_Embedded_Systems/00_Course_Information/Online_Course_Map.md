# Online Course Map: CIS-4355 – IoT & Embedded Security (General Principles)
## Texas Wesleyan University | 16-Week Schedule | Fall 2026

---

## How to Read This Map

Each row represents one module week. The **Theme** column groups related modules into the four major curriculum arcs. The **Key Concepts** column identifies the primary testable topics. All assessments are due Sunday 11:59 PM Central of the listed week unless otherwise noted. Labs are submitted via Canvas. Quizzes auto-close at the Sunday deadline.

---

## Arc 1 — Foundations: Hardware, Embedded Systems, and Architecture (Modules 01–03)

| Module | Week | Topic | Key Concepts | Assessments Due |
|---|---|---|---|---|
| 01 | 1 | IoT Architecture and Hardware Fundamentals | IoT architecture layers (Perception/Network/Support/Application), microcontrollers vs microprocessors, GPIO, I2C, SPI, UART, ADC, Arduino vs Raspberry Pi hardware roles | Quiz 01, Discussion 01, Lab 01 |
| 02 | 2 | Embedded C Programming and Memory Safety | Pointers and pointer arithmetic, bitwise operations, register-mapped I/O, static vs dynamic memory allocation, stack vs heap, buffer overflow vulnerabilities in embedded context | Quiz 02, Discussion 02, Lab 02 |
| 03 | 3 | IoT Communication Protocols – MQTT and CoAP | MQTT pub/sub model, QoS levels 0/1/2, ports 1883/8883, broker/client architecture, TLS on MQTT; CoAP request/response over UDP, ports 5683/5684, DTLS, observe mode | Quiz 03, Discussion 03, Lab 03 |

---

## Arc 2 — Connectivity and Cloud Integration (Modules 04–06)

| Module | Week | Topic | Key Concepts | Assessments Due |
|---|---|---|---|---|
| 04 | 4 | IoT Wireless Networking | Wi-Fi (WPA2/WPA3), VLAN isolation for IoT, BLE (AES-128, Just Works MITM vulnerability), Zigbee (IEEE 802.15.4, AES-128, mesh topology) | Quiz 04, Discussion 04, Lab 04 |
| 05 | 5 | Low-Power Wide-Area Networks | LoRaWAN (chirp spread-spectrum, LPWAN, NwkSKey/AppSKey, duty cycle, ADR), NB-IoT (LTE-M, licensed spectrum), duty cycling strategies, LPWAN security trade-offs | Quiz 05, Discussion 05, Lab 05 |
| 06 | 6 | IoT Cloud Platforms | AWS IoT Core (X.509 + IoT Policy, MQTT over TLS), Azure IoT Hub (Device Twin, SAS tokens, AMQP/HTTPS), GCP IoT Core (JWT + RSA/EC keys, Cloud Pub/Sub), device shadow/twin sync pattern | Quiz 06, Discussion 06, Lab 06 |

---

## Arc 3 — Edge Intelligence and Data (Modules 07–08, 12–13)

| Module | Week | Topic | Key Concepts | Assessments Due |
|---|---|---|---|---|
| 07 | 7 | Sensor Integration and Data Collection | Sensor transducers, signal conditioning (amplification, filtering), sampling rate and Nyquist theorem, sensor fusion, data aggregation and decimation, I2C/SPI sensor communication | Quiz 07, Discussion 07, Lab 07 |
| 08 | 8 | Edge Computing and Fog Computing | Edge vs fog vs cloud decision matrix, edge runtimes (AWS Greengrass, Azure IoT Edge), latency vs bandwidth trade-off, offline resilience and store-and-forward queuing, edge runtime attack surface | Quiz 08, Discussion 08, Lab 08 |
| 12 | 12 | Data Processing: Time-Series Databases and Stream Processing | TSDB vs RDBMS trade-offs, InfluxDB/TimescaleDB, data retention policies, downsampling, Apache Kafka (topics/producers/consumers/offsets), stream vs batch processing selection | Quiz 12, Discussion 12, Lab 12 |
| 13 | 13 | IoT Analytics and Machine Learning at the Edge | TensorFlow Lite model pipeline, INT8 quantization (FP32 → INT8, 4x size reduction), anomaly detection vs classification selection, Edge Impulse platform, adversarial input attacks, inference latency vs accuracy trade-off | Quiz 13, Discussion 13, Lab 13 |

---

## Arc 4 — Security: Threats, Controls, Management, and Compliance (Modules 09–11, 14–16)

| Module | Week | Topic | Key Concepts | Assessments Due |
|---|---|---|---|---|
| 09 | 9 | IoT Security – OWASP IoT Top 10 | All 10 OWASP IoT categories; primary focus: #1 (Weak Passwords/Mirai), #2 (Insecure Network Services), #7 (Insecure Data Transfer and Storage), #8 (Lack of Device Management), #10 (Lack of Physical Hardening); multi-category scenario mapping | Quiz 09, Discussion 09, Lab 09 |
| 10 | 10 | Firmware Security and Secure Boot | Secure boot chain of trust, hardware root of trust (ROM/eFuses/TPM), ECDSA firmware signing (SHA-256), OTA update pipeline (TLS download + signature verify + A/B partition + rollback prevention), monotonic counter in OTP/eFuse | Quiz 10, Discussion 10, Lab 10 |
| 11 | 11 | IoT Device Management and OTA Updates | Device provisioning, device registry (AWS IoT/Azure IoT Hub), staged OTA rollout (canary → pilot → GA with monitoring gates), device health monitoring, decommissioning (cert revocation + twin deletion + crypto erasure + disposal), zero-touch provisioning | Quiz 11, Discussion 11, Lab 11 |
| 14 | 14 | Industrial IoT (IIoT) and SCADA Systems | SCADA architecture (RTU/PLC/HMI), Purdue Reference Model (5 levels), IT/OT convergence risks, Modbus/DNP3 authentication gaps, IEC 62443 zone-and-conduit model, OT CIA priority reversal (Availability first), Stuxnet/Ukraine grid/Oldsmar attack case studies | Quiz 14, Discussion 14, Lab 14 |
| 15 | 15 | IoT Standards and Regulatory Compliance | ETSI EN 303 645 (13 provisions, no universal default passwords), NIST IR 8259A (6 capabilities), EU Cyber Resilience Act (mandatory, market enforcement, 24-hour disclosure), California SB-327, Software Bill of Materials (SBOM, NTIA minimum elements), IoT security labeling (FCC Cyber Trust Mark, Singapore CLS) | Quiz 15, Discussion 15, Lab 15 |
| 16 | 16 | Final Exam Prep and IoT Security Capstone | Cross-domain integration, STRIDE threat modeling for IoT, zero-trust architecture for IoT fleets, multi-domain scenario analysis, capstone threat model deliverable | Capstone Project, Final Exam |

---

## Assessment Summary by Week

| Week | Module | Quiz | Discussion | Lab | Special |
|---|---|---|---|---|---|
| 1 | 01 | Quiz 01 | Discussion 01 | Lab 01 | — |
| 2 | 02 | Quiz 02 | Discussion 02 | Lab 02 | — |
| 3 | 03 | Quiz 03 | Discussion 03 | Lab 03 | — |
| 4 | 04 | Quiz 04 | Discussion 04 | Lab 04 | — |
| 5 | 05 | Quiz 05 | Discussion 05 | Lab 05 | — |
| 6 | 06 | Quiz 06 | Discussion 06 | Lab 06 | — |
| 7 | 07 | Quiz 07 | Discussion 07 | Lab 07 | — |
| 8 | 08 | Quiz 08 | Discussion 08 | Lab 08 | — |
| 9 | 09 | Quiz 09 | Discussion 09 | Lab 09 | — |
| 10 | 10 | Quiz 10 | Discussion 10 | Lab 10 | — |
| 11 | 11 | Quiz 11 | Discussion 11 | Lab 11 | — |
| 12 | 12 | Quiz 12 | Discussion 12 | Lab 12 | — |
| 13 | 13 | Quiz 13 | Discussion 13 | Lab 13 | — |
| 14 | 14 | Quiz 14 | Discussion 14 | Lab 14 | — |
| 15 | 15 | Quiz 15 | Discussion 15 | Lab 15 | — |
| 16 | 16 | None | None | None | Capstone Project due Thursday; Final Exam during exam period |

---

## Curriculum Themes at a Glance

*   **Weeks 1–3 (Arc 1):** IoT hardware layer — microcontrollers, embedded C, and the first protocol layer (MQTT/CoAP). Students build the hardware and programming foundation that all later modules assume.
*   **Weeks 4–6 (Arc 2):** Wireless connectivity and cloud platforms — from device-level radio protocols (Wi-Fi, BLE, Zigbee, LoRaWAN) through cloud authentication patterns (X.509, SAS tokens, JWT). Students understand how a sensor's data travels from hardware to cloud.
*   **Weeks 7–8, 12–13 (Arc 3):** Edge intelligence and data — sensor data collection and signal conditioning (Week 7), edge compute architecture (Week 8), data pipeline storage and streaming (Week 12), and ML inference at the edge (Week 13). These four modules collectively cover the full IoT data lifecycle from physical measurement to intelligence.
*   **Weeks 9–11, 14–16 (Arc 4):** Security disciplines — the OWASP IoT Top 10 threat framework (Week 9), firmware and boot security (Week 10), device management and OTA (Week 11), industrial ICS/SCADA security (Week 14), regulatory compliance (Week 15), and capstone integration (Week 16). Security concepts from Arc 4 cross-reference hardware topics from Arc 1 and connectivity topics from Arc 2 throughout.

---

## Key Dates (Fall 2026)

*   **Course Opens:** August 24, 2026
*   **Last Day to Drop Without Academic Record:** September 7, 2026
*   **Last Day to Withdraw (W grade):** November 2, 2026
*   **Capstone Project Due:** December 3, 2026 (Thursday, Week 16)
*   **Final Exam Period:** December 7–11, 2026 (exact date/time assigned by Registrar)
*   **Grades Due to Registrar:** December 18, 2026

Dates subject to change per the Texas Wesleyan University Academic Calendar. Students are responsible for confirming official dates in the University Registrar's published calendar.
