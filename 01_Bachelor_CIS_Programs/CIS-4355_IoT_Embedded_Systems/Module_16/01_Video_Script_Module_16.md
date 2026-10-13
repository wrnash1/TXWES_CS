# Video Script: Module 16 — IoT Capstone Project and Certification Preparation

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Duration:** 16–20 minutes

---

### [00:00 – 02:00] Introduction and Course Reflection

**Visual:** Instructor on camera with title card: **Module 16 — IoT Capstone: From Sensor to Dashboard**

**Alt-text:** Instructor at desk. Title card reads "Module 16: IoT Capstone Project and Certification Preparation." Background monitor shows a complete IoT system architecture diagram spanning all four tiers: device, gateway, cloud, and dashboard.

**Audio:** "Welcome to Module 16 — the final module of CIS-4355. Today we bring everything together. In Modules 1 through 11 you built the foundation: hardware interfaces, communication protocols, cloud connectivity, and data storage. In Modules 12 through 15 you built the production layer: security, real-time operating systems, machine learning at the edge, and fleet management."

"The capstone project synthesizes all of these into a single, complete IoT system: a sensor that collects data, a gateway that secures and routes it, a cloud backend that stores and processes it, and a dashboard that visualizes it. You will document this system as a professional would — with architecture decisions, security justifications, and deployment considerations — and use it as a portfolio piece."

"We will also review the certification pathways most relevant to this course: AWS IoT Core specialty and Azure IoT certification, as well as the broader IoT Fundamentals certifications available from Cisco and CompTIA. By the end of this module you will know what these certifications cover, how they align with what you have learned, and what additional study is required to be exam-ready."

**Study Link:** [AWS Certified IoT Core Specialty — aws.amazon.com/certification](https://aws.amazon.com/certification/certified-specialty-iot/)

---

### [02:00 – 04:30] Full IoT System Architecture — The Four Tiers

**Visual:** Complete four-tier IoT architecture diagram with all components labeled and communication paths annotated.

**Alt-text:** A vertical stack diagram with four tiers. Bottom tier: Device Layer — ESP32 with DHT22 temperature/humidity sensor, ATECC608A secure element, running FreeRTOS with a sensor task, an MQTT task, and a TinyML anomaly detection task. Second tier: Gateway/Broker Layer — cloud-hosted MQTT broker with TLS on port 8883, device authentication via mTLS, message routing rules. Third tier: Cloud Processing Layer — stream processor receiving MQTT messages, time-series database storing readings, REST API serving data to clients, OTA update service. Top tier: Dashboard Layer — web browser displaying real-time charts, alert indicators, and device fleet status map.

**Audio:** "A complete production IoT system has four tiers. Let's walk through each one and the design decisions that connect them."

"**Tier 1 — The device.** An ESP32 running FreeRTOS. A sensor task reads the DHT22 temperature and humidity sensor every 30 seconds and pushes readings into a queue. An MQTT task dequeues readings and publishes them as JSON to the cloud broker over TLS on port 8883, authenticating with a per-device X.509 certificate. A TinyML anomaly detection task monitors the sensor readings for unusual patterns. A watchdog timer monitors all three tasks and resets the device if any task hangs."

"**Tier 2 — The gateway/broker.** A Mosquitto or AWS IoT Core MQTT broker validates the device certificate via mTLS, receives the published messages, and routes them to the cloud processing tier via a rule or subscription. The broker is the security boundary between the device network and the cloud backend."

"**Tier 3 — Cloud processing.** A stream processor — AWS IoT Rules, Azure Stream Analytics, or a Python consumer — subscribes to the MQTT topic, extracts the payload, and writes each reading to a time-series database. A device management service monitors device health and triggers OTA updates when new firmware is available. An alert engine evaluates telemetry against thresholds and sends notifications when anomalies are detected."

"**Tier 4 — The dashboard.** A web application — Grafana, AWS QuickSight, or a custom React app — queries the time-series database and renders real-time charts of temperature and humidity, device status indicators, and alert history. Operations staff see the current state of the entire fleet at a glance."

---

### [04:30 – 07:00] System Design Documentation

**Visual:** Slide showing a professional architecture documentation template with labeled sections.

**Alt-text:** A document template with six labeled sections: System Overview, Architecture Diagram, Component Descriptions, Security Decisions, Deployment Plan, and Open Issues. Each section has two to three bullet points describing what content belongs there.

**Audio:** "Professional IoT system documentation serves three audiences: engineers who will implement and maintain the system, security reviewers who will audit its design, and operations staff who will run it in production. Good documentation answers the questions each audience has."

"An **architecture diagram** — like the four-tier diagram we just reviewed — shows the components, their relationships, and the communication paths between them. Every arrow should be labeled with the protocol, port, and security mechanism. An architecture diagram with unlabeled arrows is not documentation; it is decoration."

"**Security decision documentation** explains why each security control was chosen. Not 'we use TLS' — but 'we use TLS 1.3 with mTLS on port 8883 because the device traffic traverses an untrusted network, mutual TLS eliminates shared credential risks, and TLS 1.3 reduces handshake latency compared to TLS 1.2.' The reasoning is as important as the decision."

"**Deployment documentation** covers: how devices are provisioned, how the OTA update pipeline works, what the staged rollout policy is, how certificates are renewed, and how devices are decommissioned. This is the documentation that saves the team at 2 AM when something goes wrong."

"**Open issues and known limitations** is the section most teams omit. It documents: what security controls are not yet implemented and why, what failure modes have not been addressed, what the monitoring coverage gaps are. Honest documentation of limitations protects the team when those limitations manifest as incidents."

---

### [07:00 – 10:00] Capstone Project Walkthrough

**Visual:** Live code review of the capstone sketch structure, showing the four FreeRTOS tasks, the MQTT topic hierarchy, and the device twin shadow update code.

**Alt-text:** Code editor showing the project directory structure on the left: main.cpp, sensor_task.cpp, mqtt_task.cpp, anomaly_task.cpp, shadow_client.cpp, certs/ directory. On the right, the main.cpp file shows task creation calls in setup(), with tasks at priorities 3, 2, 2, and 1 respectively.

**Audio:** "Let's walk through the capstone project structure. The top-level sketch creates four FreeRTOS tasks. The sensor task runs at priority 3 — it must never miss a reading interval. The MQTT task and anomaly detection task run at priority 2 — they process data and should not block the sensor. The shadow client task runs at priority 1 — it handles device twin synchronization, which is important but not time-critical."

"The MQTT topic hierarchy follows a convention: `devices/{device_id}/telemetry` for sensor readings, `devices/{device_id}/shadow/reported` for device state reports, `devices/{device_id}/shadow/delta` for configuration updates from the cloud, and `devices/{device_id}/ota/job` for firmware update notifications."

"The shadow client task subscribes to the delta topic and applies configuration changes received from the cloud — just as we built in the Module 15 lab. When it receives a new `firmware_target` value in the delta, it checks whether the current firmware version matches and initiates an OTA download if not."

"The anomaly detection task reads from a secondary queue that the sensor task also writes to. It maintains a sliding window of the last 10 readings and computes a simple z-score anomaly metric: if the current reading is more than 3 standard deviations from the window mean, it publishes an anomaly event to `devices/{device_id}/anomaly`."

"The documentation deliverable for the capstone asks you to explain every architectural decision: why you chose those task priorities, why you structured the MQTT topics that way, how you would extend this system to 10,000 devices, and what the three highest security risks are in your implementation."

---

### [10:00 – 13:00] Certification Pathways

**Visual:** Comparison table showing four IoT certifications with columns for issuer, level, key topic areas, and alignment to this course.

**Alt-text:** A four-row table. Row 1: AWS IoT Specialty — Amazon, Professional level, covers IoT architecture, AWS IoT Core services, security, and fleet management. Row 2: AZ-220 Azure IoT Developer — Microsoft, Associate level, covers Azure IoT Hub, IoT Edge, DPS, and streaming analytics. Row 3: Cisco IoT Fundamentals — Cisco NetAcad, beginner level, covers IoT protocols, networking, and data analysis. Row 4: CompTIA IoT+ — CompTIA, practitioner level, covers IoT hardware, networking, security, and deployment.

**Audio:** "Let's talk about certification pathways. Certifications validate your knowledge to employers, but more importantly, preparing for them forces you to fill gaps you did not know you had."

"**AWS Certified Specialty — IoT Core** is the most technically demanding IoT certification currently available. It covers: AWS IoT Core architecture (Rules Engine, MQTT broker, device registry, shadows), AWS IoT Greengrass for edge computing, AWS IoT Device Defender for fleet security monitoring, and AWS IoT Fleet Hub for management. This course aligns well with the architecture and security sections — the gap to close is AWS-specific service knowledge. Recommended preparation: complete all AWS IoT tutorials in the AWS documentation, get hands-on experience with IoT Core in the free tier, and use the AWS Skill Builder practice exams."

"**AZ-220 Azure IoT Developer** covers Azure IoT Hub, Azure IoT Device Provisioning Service (DPS), Azure IoT Edge, and Azure Stream Analytics. The DPS module aligns directly with our Module 15 provisioning content. AZ-220 is an Associate-level exam — generally considered more approachable than the AWS Specialty. Recommended preparation: complete the Microsoft Learn IoT Developer learning path (free), work through the AZ-220 hands-on labs, and take the official Microsoft practice assessment."

"**Cisco IoT Fundamentals** and **CompTIA IoT+** are entry-level certifications that validate general IoT knowledge across hardware, networking, and security. They are appropriate starting points if you are entering the field and want a recognized credential before taking the cloud-specific specialty exams. This course's content exceeds the level required for both of these certifications — if you have completed all labs and quizzes, you have the knowledge base."

---

### [13:00 – 15:30] Certification Exam Preparation Strategy

**Visual:** Study plan slide showing a 12-week timeline broken into three phases: Foundation Review, Service-Specific Study, and Practice Exams.

**Alt-text:** A timeline with three phases. Phase 1 (weeks 1–4): Foundation Review — re-read all module reading guides, ensure all labs are complete, and review key terms. Phase 2 (weeks 5–8): Service-Specific Study — work through cloud provider documentation and tutorials for the chosen certification target. Phase 3 (weeks 9–12): Practice Exams — complete three full practice exams, review every incorrect answer, and identify weak topic areas for focused review.

**Audio:** "For any IoT certification, my recommended preparation strategy is a 12-week plan divided into three phases."

"In the first four weeks, go back to fundamentals. The certification exams test your ability to apply concepts under time pressure — you need the concepts to be reflexive, not something you have to reconstruct from first principles during the exam. Use the key terms from each module as a self-test checklist. If you cannot explain a term in two sentences without looking it up, put it on your review list."

"In weeks five through eight, focus on the cloud service details specific to your target certification. AWS IoT certifications require deep knowledge of AWS-specific services: IoT Core, Greengrass, Device Defender, Fleet Indexing. Azure certifications require deep knowledge of IoT Hub vs. IoT Central differences, DPS enrollment groups and attestation mechanisms, and IoT Edge module deployment. These details are not in the course — they require hands-on time with the actual platforms."

"In weeks nine through twelve, take practice exams under timed conditions. Do not look up answers while you are taking the practice exam. After completing it, review every wrong answer in detail — understand not just why the correct answer is right, but why each distractor is wrong. This is the most efficient use of study time in the final phase."

"The AWS IoT Specialty exam is 65 questions in 130 minutes. AZ-220 is 40–60 questions in 120 minutes. Time pressure is real — practice under timed conditions from week nine."

---

### [15:30 – End] Course Conclusion and Capstone Guidance

**Visual:** Final summary slide listing all 16 modules in a grid, with the module topics and their interconnections highlighted.

**Audio:** "Let's take a moment to look at what you have built across this course. You started with embedded hardware and basic GPIO. You progressed through communication protocols — UART, SPI, I2C, MQTT. You connected devices to the cloud and stored telemetry data. You applied security from Module 12 forward: TLS, certificates, firmware signing. You built concurrent, deterministic applications with FreeRTOS. You ran machine learning inference on a microcontroller. And you designed fleet management systems that scale from one device to one million."

"The capstone project is your opportunity to demonstrate all of these skills in a single integrated system. The grading rubric values three things equally: working code that demonstrates the required functionality, architecture documentation that explains your design decisions, and security analysis that shows you understand the threat model of your system."

"For the certification exam preparation, remember: the exam tests application of knowledge, not recall of facts. Every practice question in this course was designed to make you explain why an answer is correct and why the distractors are wrong. That habit of thinking is exactly what the certification exams reward."

"Thank you for your work in CIS-4355. The skills you have built in this course — embedded systems, secure communication, real-time programming, machine learning at the edge, and fleet operations — are among the most in-demand in the technology industry today. Good luck on the capstone and on your certification journey."

**Key Terms for This Module:**

- Four-tier IoT architecture — device, gateway, cloud processing, dashboard
- Architecture decision record (ADR)
- MQTT topic hierarchy convention
- AWS IoT Specialty certification
- AZ-220 Azure IoT Developer certification
- Cisco IoT Fundamentals
- CompTIA IoT+
- AWS IoT Core, IoT Greengrass, IoT Device Defender, Fleet Hub
- Azure IoT Hub, Device Provisioning Service (DPS), IoT Edge
- Capstone deliverables — working system, architecture diagram, security analysis

---
