# Reading Guide: Module 16 — IoT Capstone Project and Certification Preparation

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you should be able to:

- Design a complete four-tier IoT system architecture with documented security decisions
- Write professional-quality architecture documentation including open issues and known limitations
- Identify the key topic areas for AWS IoT Specialty and AZ-220 certifications and map them to course content
- Develop a structured certification exam preparation plan
- Articulate the three highest-priority security risks in any IoT system design

---

## Section 1 — Complete IoT System Design

### The Four-Tier Architecture Model

A production IoT system integrates four tiers, each with distinct responsibilities, communication contracts, and security boundaries.

#### Tier 1 — Device Layer

The device layer consists of the physical hardware running embedded firmware. The key design decisions at this tier are:

- Microcontroller selection: capability (flash, SRAM, connectivity), power budget, security features (secure boot, hardware secure element)
- Firmware architecture: RTOS task structure, priority assignments, inter-task communication primitives
- Sensor interface: protocol selection (I2C, SPI, UART, analog ADC), sampling rate, data representation
- On-device security: TLS certificate storage, firmware signing, secure boot configuration
- Edge intelligence: TinyML models for on-device inference, reducing cloud communication frequency and cost

The device layer is the most constrained and the most physically exposed tier. Security decisions made here — or not made — persist for the device's entire operational lifetime.

#### Tier 2 — Gateway and Connectivity Layer

The gateway layer bridges device communication protocols to cloud-scale infrastructure. For MQTT-based systems, this tier includes:

- MQTT broker (Mosquitto, AWS IoT Core, Azure IoT Hub)
- Transport security: TLS 1.3 on port 8883, device certificate validation
- Authentication: mTLS with per-device X.509 certificates
- Message routing: topic-based routing rules directing messages to appropriate processing services
- Protocol translation: for devices using CoAP, HTTP, or proprietary protocols, gateway translates to the cloud backend's native protocol

The gateway tier is the critical security boundary. Compromise of the gateway can expose all device traffic. The gateway must be hardened, monitored, and its certificates managed with the same rigor as any production-critical service.

#### Tier 3 — Cloud Processing Layer

The cloud processing tier receives telemetry from the gateway and performs:

- Stream processing: real-time transformations, aggregations, and routing of incoming data
- Storage: time-series database for telemetry, relational or document database for device metadata and configuration
- Device management: device registry, device twins, OTA update orchestration
- Analytics: batch processing for historical analysis, ML model training pipelines
- Integration: APIs for dashboard consumption, webhook notifications for external systems

Cloud tier design must account for scale: a fleet of 100,000 devices sending data every 30 seconds generates approximately 3,300 messages per second — requiring message ingestion infrastructure that can handle sustained high throughput.

#### Tier 4 — Dashboard and Application Layer

The dashboard tier provides human and system interfaces to the IoT data:

- Operational dashboards: real-time visualization of fleet health, individual device status, time-series charts
- Alert management: incident feed, acknowledgment workflow, escalation rules
- Configuration interface: device twin management, OTA deployment controls
- Reporting: historical analysis, compliance reporting, capacity planning

Dashboard users have different needs: an operations engineer wants device-level drill-down; a VP wants aggregate KPIs; a security team wants audit logs. Good dashboard design serves multiple audiences without requiring role-specific custom builds.

### Connecting the Tiers: Communication Contracts

The interfaces between tiers must be explicitly documented as contracts — agreed-upon formats, protocols, and semantics. For the course capstone, the communication contracts are:

**Device to broker:** MQTT over TLS on port 8883. Topics: `devices/{device_id}/telemetry`, `devices/{device_id}/shadow/reported`. Message format: JSON with fields `device_id`, `timestamp_ms`, sensor values, `firmware_version`. QoS: 1 (at-least-once delivery).

**Broker to cloud processing:** Rule-based forwarding to time-series database ingestion endpoint. The rule matches topic `devices/+/telemetry` and extracts the payload.

**Cloud processing to dashboard:** REST API or WebSocket subscription providing time-series data queries and real-time event streaming.

These contracts ensure that changes to one tier do not silently break adjacent tiers — a device firmware update that changes the JSON field names must be accompanied by a corresponding cloud processing update.

---

## Section 2 — Architecture Documentation Standards

### What Professional Documentation Contains

Professional IoT system documentation serves three audiences simultaneously: engineers, security reviewers, and operations staff. Documentation that serves only one audience is incomplete.

**For engineers:** Component descriptions with technology choices and version pins, API specifications for inter-tier interfaces, development environment setup instructions, and troubleshooting procedures for the most common failure modes.

**For security reviewers:** Threat model documenting what assets are protected and against which threat actors, security control descriptions with justifications, known limitations and mitigations, and incident response procedures.

**For operations staff:** Deployment architecture, monitoring dashboard description, alert definitions and response playbooks, and escalation procedures.

### Architecture Decision Records

An Architecture Decision Record (ADR) documents a significant technical choice: the context in which the decision was made, the options that were considered, the chosen option, and the reasoning for the choice. ADRs are written once and rarely updated — they preserve the institutional memory of *why* the system was built the way it was, which is invaluable when the original engineers have moved on.

A minimal ADR for an IoT security decision:

**Decision:** Use mTLS with per-device X.509 certificates for device authentication.

**Context:** The system must authenticate 10,000 devices connecting to a shared MQTT broker over the public internet. Devices are deployed in physical locations accessible to adversaries.

**Options considered:**

- Username/password over TLS — simpler to implement, but a shared credential database is a high-value attack target
- API key per device — better than shared passwords, but keys must be securely provisioned and rotated
- Per-device X.509 certificates with mTLS — unique per device, no shared secret, hardware-backed on devices with secure elements

**Decision rationale:** mTLS eliminates shared credential risk. Certificate compromise affects only one device. Certificate revocation provides fleet-level response capability. Hardware secure element storage prevents key extraction.

**Limitations:** More complex initial provisioning. Certificate renewal must be managed before expiry.

### Open Issues Documentation

Many teams skip documenting known limitations because they feel it exposes weakness. The opposite is true: documented known issues demonstrate engineering maturity. Undocumented limitations become surprises during incidents.

Format for open issues:

- Issue description: what the gap is
- Risk level: if exploited or triggered, what is the impact?
- Planned resolution: when and how the issue will be addressed
- Workaround: what mitigates the risk in the current state

---

## Section 3 — Certification Pathways

### AWS Certified Specialty — IoT Core

The AWS IoT Specialty exam validates the ability to design, implement, and maintain IoT solutions using AWS services. Key topic domains:

**Domain 1 — IoT Architecture Design (24% of exam):** AWS IoT Core architecture, message broker, rules engine, device registry, device shadows. Greengrass for local processing. Choosing between IoT Core, IoT Greengrass, and IoT SiteWise for different use cases.

**Domain 2 — Device Connectivity and Protocols (17%):** MQTT, HTTP, WebSocket connectivity to IoT Core. Topic naming conventions, QoS levels, persistent sessions. Offline behavior and message queuing.

**Domain 3 — Processing and Acting on Device Data (20%):** IoT Rules Engine SQL syntax, rule actions (DynamoDB, S3, Lambda, SNS, SQS, Kinesis). Stream processing for real-time analytics. Lambda functions triggered by IoT rules.

**Domain 4 — Security (22%):** IoT Core authentication (certificates, SigV4, custom authorizers). IoT Core authorization (policies, thing groups, policy variables). IoT Device Defender for fleet security monitoring and anomaly detection. Certificate management at scale.

**Domain 5 — Device Management (17%):** Fleet Indexing and search, Device Jobs for OTA updates, Fleet Hub for operator dashboards, Device Provisioning methods (JITP, bulk provisioning, fleet provisioning).

Course alignment: Domains 4 and 5 align directly with Modules 12 and 15. Domain 1 aligns with the four-tier architecture concepts in this module. Gaps to close before exam: AWS-specific service APIs, IoT Rules Engine SQL syntax, Greengrass component model.

### AZ-220 Azure IoT Developer

AZ-220 validates the ability to implement device provisioning, device communication, and IoT solutions using Azure services.

**Key skill areas:**

IoT Hub configuration: message routing, built-in endpoints, custom endpoints, enrichments. Device twin CRUD operations. IoT Hub device authentication and authorization.

Device Provisioning Service (DPS): enrollment groups vs. individual enrollments, attestation mechanisms (TPM, X.509, symmetric key), automatic provisioning workflow, DPS-to-IoT-Hub allocation policies.

Azure IoT Edge: IoT Edge runtime, module development and deployment, Edge hub for local routing, offline capability, nested IoT Edge topologies.

Azure Stream Analytics: time window functions (tumbling, hopping, sliding), joins between streams and reference data, anomaly detection built-in functions.

Course alignment: DPS content aligns with Module 15 provisioning. IoT Hub device twin aligns with the device shadow pattern. IoT Edge aligns with gateway concepts. Gaps: Azure-specific service configuration, Stream Analytics query language, ARM template deployments.

### Entry-Level Certifications

**Cisco Certified IoT Fundamentals** covers IoT concepts, networking (IPv6, 6LoWPAN, Wi-Fi, cellular), sensors, actuators, data processing, and security fundamentals. This course's content significantly exceeds the Cisco IoT Fundamentals scope — graduates should be prepared to pass this exam after completing Modules 1–8.

**CompTIA IoT+** covers IoT hardware, protocols, connectivity, data management, and security fundamentals in a vendor-neutral framework. Approximately equivalent in scope to Cisco IoT Fundamentals. Recommended for students entering the field who want a recognized vendor-neutral credential before specializing.

---

## Section 4 — Capstone Project Requirements

### System Requirements

The capstone project must demonstrate a complete, working four-tier IoT system:

**Device tier requirements:**

- FreeRTOS with at least two tasks at different priority levels
- At least one physical or simulated sensor publishing over MQTT with TLS
- Per-device X.509 certificate for mTLS authentication
- Watchdog timer monitoring at least one task
- Device shadow client that applies at least one configuration change received from the cloud

**Gateway/broker tier requirements:**

- Mosquitto or cloud MQTT broker configured for TLS on port 8883
- Client certificate validation (require_certificate true or equivalent)
- Messages successfully routing from device to cloud processing tier

**Cloud processing tier requirements:**

- Telemetry data stored in a time-series database or file-based equivalent
- At least one alert condition implemented (threshold-based or anomaly-based)
- Device registry with at least one device registered

**Dashboard tier requirements:**

- Visualization of at least 5 minutes of sensor data
- Display of device connection status
- Display of at least one alert that fired during the demonstration

### Documentation Requirements

**Architecture diagram:** Four-tier diagram with all components, communication paths, protocols, ports, and security mechanisms labeled.

**Security analysis:** For each of the OWASP IoT Top 10 categories, classify your system as: (a) fully mitigated, (b) partially mitigated with explanation, or (c) not yet addressed with risk acknowledgment.

**Architecture decision records:** At least three ADRs for significant technical choices made during the project.

**Deployment documentation:** Step-by-step provisioning procedure for a new device, OTA update procedure, and decommissioning procedure.

**Known limitations:** At least three documented open issues with risk level, planned resolution, and current workaround.

---

## Key Terms

- **Four-tier IoT architecture** — device, gateway, cloud processing, dashboard
- **Communication contract** — agreed protocol, format, and semantics between system tiers
- **Architecture Decision Record (ADR)** — document recording a design decision, the options considered, and the rationale
- **Threat model** — enumeration of assets, threat actors, and mitigations in a system design
- **AWS Certified Specialty — IoT Core** — professional-level AWS IoT certification covering architecture, security, and fleet management
- **AZ-220 Azure IoT Developer** — Microsoft associate-level certification covering IoT Hub, DPS, IoT Edge, and Stream Analytics
- **Cisco IoT Fundamentals** — entry-level vendor-specific IoT certification
- **CompTIA IoT+** — entry-level vendor-neutral IoT practitioner certification
- **AWS IoT Device Defender** — AWS service for fleet-wide security monitoring and anomaly detection
- **Azure Device Provisioning Service (DPS)** — Azure service for zero-touch device provisioning at scale
- **IoT Edge** — Azure service for deploying cloud workloads to edge devices
- **Capstone deliverables** — working system, architecture diagram, OWASP analysis, ADRs, deployment docs, known limitations

---

## Review Questions

1. Name the four tiers of the IoT architecture model and describe the primary responsibility of each tier.
2. What is a communication contract, and why must it be explicitly documented for each interface between tiers?
3. What are the three audiences for IoT system documentation, and what questions does each audience need documentation to answer?
4. What is an Architecture Decision Record, and what five elements does a complete ADR contain?
5. Why should documentation include known limitations, even though doing so exposes engineering gaps?
6. What percentage of the AWS IoT Specialty exam covers security, and which course modules most directly prepare for that domain?
7. What is the Azure Device Provisioning Service, and which course module covers the same conceptual material?
8. What is the difference between Cisco IoT Fundamentals and AZ-220 in terms of certification level and technical depth?
9. List the five capstone deliverable categories and describe what must be included in the security analysis deliverable.
10. A graduate completes this course and wants to pursue AWS IoT Specialty certification. They feel strong on security and fleet management but unfamiliar with AWS-specific services. What three-phase study plan would you recommend, and what resource would you use in each phase?

---

## 9. Supplemental Resources

**1. AWS IoT Specialty Certification — Exam Guide and Official Study Path**
[https://aws.amazon.com/certification/certified-iot-specialty/](https://aws.amazon.com/certification/certified-iot-specialty/)
The official AWS IoT Specialty exam guide documents the five domain weights (Architecture Design 24%, Device Connectivity 17%, Processing and Acting 20%, Security 22%, Device Management 17%), the skills assessed in each domain, and links to the official AWS skill builder learning paths and practice exam questions. This resource is the authoritative reference for mapping course module content to exam domains — Domain 4 (Security) aligns with Module 12, Domain 5 (Device Management) aligns with Module 15, and Domain 1 (Architecture Design) aligns directly with the four-tier architecture model in this module.

**2. Microsoft Learn — AZ-220 Azure IoT Developer Study Guide**
[https://learn.microsoft.com/en-us/credentials/certifications/azure-iot-developer-specialty/](https://learn.microsoft.com/en-us/credentials/certifications/azure-iot-developer-specialty/)
Microsoft's official AZ-220 study guide on Microsoft Learn provides the skills measured outline, maps to Azure documentation for each skill area (IoT Hub configuration, DPS enrollment groups, IoT Edge module development, Stream Analytics window functions), and includes free hands-on labs in Azure sandbox environments. The Device Provisioning Service content directly parallels Module 15's JITP material, and the IoT Hub device twin documentation is the Azure equivalent of the shadow synchronization pattern implemented in the Module 15 lab — making this resource highly efficient for course graduates filling the Azure-specific knowledge gap.

**3. CompTIA IoT+ Certification Exam Objectives (CY0-001)**
[https://www.comptia.org/certifications/iot](https://www.comptia.org/certifications/iot)
CompTIA's official IoT+ exam objectives page lists the four exam domains (IoT Hardware and Devices, IoT Networking and Connectivity, IoT Data Management, and IoT Security), each sub-objective with percentage weight, and links to the official study guide and practice exam resources. Reviewing the objectives against course modules confirms which areas require targeted review versus areas where course content already exceeds the exam baseline — particularly useful for students who want to take the IoT+ exam quickly as an early credential before specializing in an AWS or Azure certification track.
