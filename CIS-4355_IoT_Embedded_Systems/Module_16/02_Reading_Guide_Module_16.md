# Reading Guide: Module 16 - Final Exam Prep and IoT Security Capstone
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 16 – Final Exam Prep and IoT Security Capstone**! This is the final module of CIS-4355. Rather than introducing new topics, this module synthesizes the full 16-week curriculum into a cohesive review framework and prepares you to apply integrated knowledge across all domains on the final exam and in the capstone project.

The IoT security domain is inherently cross-disciplinary: a secure IoT deployment requires correct protocol selection (Modules 03–05), cloud platform authentication (Module 06), sensor data integrity (Module 07), edge compute security (Modules 08, 13), a thorough understanding of the OWASP IoT Top 10 threat model (Module 09), firmware security controls (Module 10), device lifecycle management (Module 11), data pipeline security (Module 12), IIoT/SCADA segmentation (Module 14), and regulatory compliance (Module 15). The final exam will present multi-domain scenarios that require you to reason across these layers simultaneously. This reading guide provides the cross-domain integration framework to prepare you for those scenarios.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **IoT Defense-in-Depth Architecture**: The application of overlapping, independent security controls at the device layer (secure boot, hardware root of trust, firmware signing), the network layer (TLS 1.3, VLAN segmentation, firewall conduits, certificate-based mutual authentication), and the cloud/application layer (IoT policies with least privilege, device registry, encrypted storage). Defense in depth ensures that a failure at any single layer does not result in total system compromise — it is the architectural expression of the principle that no single control is sufficient.
*   **Cross-Domain Attack Chain**: A real-world IoT attack scenario in which an attacker moves across multiple security domains to reach a high-value target. Example: (1) exploit a default credential on an internet-facing camera (OWASP IoT #1), (2) pivot through the corporate network because IoT devices are not VLAN-isolated (OWASP IoT #2), (3) reach an unpatched PLC with a known CVE (OWASP IoT #4/5), (4) send unauthenticated Modbus write commands to a safety system (OWASP ICS threat). Each step exploits a different module's security gap. Understanding these chains is the basis of the capstone threat modeling exercise.
*   **Capstone Threat Model (STRIDE for IoT)**: STRIDE is a threat categorization framework: Spoofing (impersonating a device identity), Tampering (modifying firmware, sensor data, or commands in transit), Repudiation (denying actions due to absent audit logs), Information Disclosure (exposing telemetry or credentials), Denial of Service (disrupting device availability), Elevation of Privilege (gaining unauthorized control). Applying STRIDE to an IoT system architecture diagram produces a threat list that maps directly to OWASP IoT Top 10 categories and drives the security control selection covered throughout this course.
*   **Exam Domain Coverage Map**: The final exam draws from all 16 modules: embedded hardware (Modules 01–02), IoT protocols (Modules 03–05), cloud platforms (Module 06), sensors (Module 07), edge computing (Module 08), OWASP IoT Top 10 (Module 09), firmware security (Module 10), device management (Module 11), data pipelines (Module 12), edge ML (Module 13), IIoT/SCADA (Module 14), standards and compliance (Module 15). High-frequency exam topics across modules: X.509 authentication, TLS, MQTT QoS, INT8 quantization, OWASP categories #1/#2/#7/#8, secure boot chain of trust, staged OTA rollout, Purdue Model levels, ETSI EN 303 645 Provision 1.
*   **Zero-Trust for IoT**: A security model that eliminates implicit trust based on network location — every device must authenticate and every request must be authorized regardless of whether the device is inside or outside the corporate network perimeter. For IoT, zero-trust implementation requires: mutual TLS (mTLS) with per-device X.509 certificates, IoT policies granting only the specific MQTT topics a device publishes/subscribes to, continuous device health attestation (reported firmware version, secure boot status), and microsegmentation so a compromised device cannot reach other devices or cloud services beyond its authorized scope.

---

### 2. Certification Exam Tips
*   **Multi-domain scenario recognition:** The final exam presents scenarios that involve two or more modules' concepts. Strategy: first identify which OWASP IoT Top 10 categories are present, then identify which module's technical controls address each category. This two-step decomposition converts an apparently complex scenario into a checklist of familiar concepts.
*   **Protocol selection decision rules:** Memorize: MQTT = TCP, pub/sub, port 1883/8883 (TLS), lightweight for constrained devices; CoAP = UDP, request/response, port 5683/5684 (DTLS), best for very constrained devices; HTTP/REST = TCP, stateful, high overhead; Zigbee = IEEE 802.15.4, AES-128, mesh, short range; LoRaWAN = chirp spread-spectrum, LPWAN, long range, duty-cycle limited; BLE = AES-128, "Just Works" pairing is MITM-vulnerable. Exam scenarios describe a constraint (battery, range, bandwidth, latency) and test which protocol is most appropriate.
*   **Authentication method decision rules:** X.509 certificate = strongest device identity, required for AWS IoT Policy enforcement and mTLS; JWT (GCP IoT Core) = RSA/EC-signed short-lived token, suitable where cert management is complex; SAS token (Azure IoT Hub) = HMAC-SHA256 with expiry, simpler but requires shared secret management; API key = weakest, acceptable only for server-to-server internal calls. Exam questions presenting a scenario with "impersonation risk" or "shared credential blast radius" point toward X.509.
*   **Compliance framework selection:** ETSI EN 303 645 = consumer IoT device baseline (EU/UK); NIST IR 8259A = U.S. federal IoT procurement baseline; IEC 62443 = ICS/SCADA industrial security; NIST SP 800-82 = U.S. guide for ICS security; California SB-327 = first U.S. law banning universal default passwords; EU CRA = mandatory EU regulation with market enforcement and patch/disclosure timelines. Exam scenarios describe a context (consumer device, industrial plant, federal agency) and test which framework applies.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — reviewing all 10 OWASP IoT Top 10 categories in a single session before the final exam is the highest-ROI study activity. Every exam scenario maps to at least one OWASP category, and the remediation for each category has been covered in a specific module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — complete a full review of all 10 OWASP IoT Top 10 categories and cross-reference each with the course module that covers its primary remediation. This integration exercise is the most effective preparation for multi-domain final exam questions.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) — revisit any module segments covering topics you identified as weak during your domain coverage map review. Focus particularly on protocol comparison, cloud authentication methods, and the firmware security pipeline.

---

### Lab & Command Integration
In this week's capstone lab, you will perform the following integrative exercises:
*   **Build a threat model for a complete IoT system**: Given a system architecture diagram of a smart building deployment (temperature/occupancy sensors → Zigbee coordinator → edge gateway → MQTT broker → cloud platform → web dashboard), apply STRIDE to each component and data flow, produce a threat table mapping each threat to an OWASP IoT Top 10 category and a specific technical control from the course, and identify the top three highest-risk threat/control gaps.
*   **Write a cross-domain security requirements document**: For the smart building system above, write five security requirements in the format "The system SHALL [control] in order to mitigate [threat] as defined by [standard/framework]." Each requirement must cite a different module's technical domain (e.g., authentication, firmware update, network segmentation, data encryption, anomaly detection).
*   **Conduct a final exam mock review**: Complete the 16-question practice set (one question per module) provided in the course portal under timed conditions (32 minutes / 2 minutes per question). Review incorrect answers by tracing each back to the corresponding module's reading guide glossary and distractor analysis.

---

### 3. Study Checklist
- [ ] Read the glossary terms and create a personal cross-reference table mapping each term to its module number.
- [ ] Review all 10 OWASP IoT Top 10 categories at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) and map each to a course module remediation.
- [ ] Watch review sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) covering any weak domains identified in your self-assessment.
- [ ] Complete the capstone threat model lab exercise and the mock exam practice set.
- [ ] Submit the capstone project deliverable per the course syllabus instructions before the final exam date.
