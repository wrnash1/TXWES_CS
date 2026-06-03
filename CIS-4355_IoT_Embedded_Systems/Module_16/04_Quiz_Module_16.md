# Quiz: Module 16 — IoT Capstone Project and Certification Preparation

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

### Question 1

A complete four-tier IoT architecture is being reviewed. The architecture diagram shows an ESP32 device connecting directly to a cloud time-series database using a proprietary binary protocol over port 5432, bypassing the MQTT broker. Which architectural concern is most significant?

- A) Using port 5432 is technically incorrect — time-series databases should only accept connections on port 8086 (InfluxDB default), and using a non-standard port violates the architecture specification.
- B) Bypassing the gateway/broker tier eliminates the security boundary between the device and cloud backend. The device now has a direct authenticated connection to the database, meaning a compromised device can write arbitrary data directly to storage, bypassing message validation, rate limiting, and access control rules that would normally be enforced at the broker and stream processing tiers.
- C) The architecture is acceptable for small fleets (under 100 devices) but will not scale because time-series databases cannot handle direct device connections at large scale.
- D) Using a proprietary binary protocol violates the MQTT standard and will prevent the system from receiving firmware updates via OTA, because OTA delivery requires MQTT.
- **Correct Answer:** B) Bypassing the broker tier eliminates the critical security boundary between devices and backend storage.
- **Distractor Analysis:**
  - *Why A is incorrect:* Port numbers are configurable — any service can listen on any port. The port number itself is not the concern. Port 5432 is actually the default PostgreSQL port, which is an interesting detail but irrelevant to the architectural flaw.
  - *Why B is correct:* The broker/gateway tier is the security boundary of the architecture. It enforces: authentication (devices must present valid certificates), authorization (devices can only publish to their own topics, not to other devices' topics), rate limiting (devices cannot flood the backend), and message validation (malformed messages are rejected before reaching storage). A direct device-to-database connection eliminates all of these controls. A compromised device can write arbitrary data, potentially corrupting other devices' records or exhausting storage.
  - *Why C is incorrect:* The scalability concern is real at very large scale, but it is secondary to the security concern. Even at 10 devices, a direct device-to-database connection with no intermediary validation is an architectural security failure.
  - *Why D is incorrect:* OTA firmware delivery does not require MQTT — it can use HTTPS, CoAP, or custom protocols. MQTT is a common OTA notification channel, but the actual firmware binary is typically delivered over HTTPS. The proprietary protocol concern is real but unrelated to OTA capability.

---

### Question 2

An Architecture Decision Record (ADR) for an IoT system documents: "Decision: Use QoS 1 for all MQTT telemetry messages." The "Limitations" section is left blank. Which limitation should be documented?

- A) QoS 1 is not supported by the ESP32's PubSubClient library — the library only supports QoS 0, so this decision cannot be implemented as written.
- B) QoS 1 guarantees at-least-once delivery, which means duplicate messages may be received by the broker during network disruptions (a message sent, no acknowledgment received, message resent). The cloud processing layer must be idempotent — it must handle duplicate telemetry messages without double-counting or corrupting aggregates.
- C) QoS 1 requires a persistent MQTT session, which increases broker memory consumption proportionally with fleet size and may become a scaling constraint above 100,000 devices with frequent disconnections.
- D) QoS 1 violates the OWASP IoT Top 10 #7 (Insecure Data Transfer) because it stores messages in the broker's persistence layer in plaintext before they are acknowledged.
- **Correct Answer:** B) QoS 1 guarantees at-least-once delivery — duplicates are possible and the processing layer must be idempotent.
- **Distractor Analysis:**
  - *Why A is incorrect:* PubSubClient does support QoS 1 for both publish and subscribe operations. The `publish(topic, payload, retained)` and `subscribe(topic, qos)` overloads accept QoS level parameters.
  - *Why B is correct:* QoS 1 semantics guarantee delivery at least once but not exactly once. The "at least once" means: if the sender does not receive a PUBACK acknowledgment before a timeout, it resends the message. During network disruptions, this can result in the same message being delivered twice. Any stream processor or database writer that assumes each message is unique will double-count readings, inflating aggregates. The ADR limitation should document this and note that the processing layer needs duplicate detection (e.g., using the MQTT message ID or a timestamp-based deduplication key).
  - *Why C is incorrect:* QoS 1 does not inherently require a persistent session — persistent sessions are enabled separately with the `cleanSession=false` flag. A QoS 1 client with `cleanSession=true` does not store unacknowledged messages across reconnections on the broker side.
  - *Why D is incorrect:* QoS 1 has no relationship to encryption. The persistence layer concern (messages stored in a broker queue) is a valid security consideration in some contexts, but it is not classified as OWASP IoT #7 and is not caused by the QoS level choice. OWASP #7 addresses the transport encryption of the data in transit.

---

### Question 3

A developer is studying for the AWS Certified IoT Specialty exam. They have completed all course labs and feel confident on security and fleet management concepts. Which AWS-specific topic area represents the largest gap between course content and the exam domain requirements?

- A) OWASP IoT Top 10 and TLS certificate management — these are general security concepts that the course covered thoroughly, and the exam will test the same material in an AWS context.
- B) AWS IoT Rules Engine SQL syntax, AWS IoT Greengrass component deployment model, and AWS-specific service integrations (IoT Core to DynamoDB, S3, Lambda, Kinesis via rules) — these are AWS-proprietary features that require hands-on platform experience beyond the course content.
- C) FreeRTOS task creation and MQTT protocol fundamentals — these are the core topics of the exam and represent the largest knowledge gap for students who have not worked with the Arduino framework.
- D) IPv6 addressing and 6LoWPAN mesh networking — the AWS IoT Specialty exam is heavily focused on low-power wide-area networking protocols that the course did not cover in detail.
- **Correct Answer:** B) AWS-specific service APIs, Rules Engine SQL, and Greengrass deployment model.
- **Distractor Analysis:**
  - *Why A is incorrect:* The course does cover OWASP IoT Top 10 and TLS certificate management thoroughly. While the exam contextualizes these within AWS services (IoT Device Defender, AWS Certificate Manager, IoT Core authentication), the underlying concepts transfer directly. This is not the largest gap.
  - *Why B is correct:* The AWS IoT Specialty exam tests AWS-specific implementation knowledge: IoT Rules Engine SQL (how to write rules that route messages to DynamoDB, S3, Lambda, Kinesis), Greengrass component model (local execution, stream manager, secret manager, inter-process communication), IoT Device Defender (audit findings, detect anomalies, mitigation actions), and Fleet Indexing query syntax. None of these are covered in the course — they require hands-on experience with the AWS console and documentation. This is the primary study gap for course graduates.
  - *Why C is incorrect:* FreeRTOS and MQTT are covered in detail in Modules 13 and Module 1–3 respectively. These are strengths for course graduates, not gaps. The exam tests architectural application of these concepts within AWS, not the fundamentals themselves.
  - *Why D is incorrect:* The AWS IoT Specialty exam focuses on AWS cloud IoT services, not on low-power WAN protocols like LoRaWAN or 6LoWPAN. While these protocols appear in the exam in the context of AWS IoT Core for LoRaWAN, they are a small portion of the exam and not the primary gap.

---

### Question 4

An IoT system's security analysis classifies OWASP IoT #4 (Lack of Secure Update Mechanism) as "Fully mitigated — OTA updates are implemented." A security reviewer challenges this classification. Which additional control must be present for the mitigation to be complete?

- A) The device must be able to receive updates over both Wi-Fi and cellular networks, providing redundancy in the update delivery channel.
- B) OTA firmware images must be cryptographically signed and the bootloader must verify the signature before flashing. An OTA mechanism that downloads and flashes unsigned images without verification allows any attacker who can reach the OTA endpoint to deliver malicious firmware — the update mechanism becomes an attack vector rather than a mitigation.
- C) The OTA update must be delivered via a dedicated out-of-band management network, separate from the operational data network, to prevent interference between update traffic and sensor telemetry.
- D) The device must support downgrade prevention — the ability to roll back to an older firmware version must be explicitly disabled so that attackers cannot force the device to run a known-vulnerable previous version.
- **Correct Answer:** B) Firmware signature verification is required — unsigned OTA is itself a vulnerability.
- **Distractor Analysis:**
  - *Why A is incorrect:* Multi-channel update delivery (Wi-Fi + cellular) is a reliability feature, not a security control. A device that can receive updates over multiple channels but applies them without signature verification is no more secure than a single-channel device.
  - *Why B is correct:* OWASP IoT #4 defines the mitigation as a "secure update mechanism" — and security requires that the update content be authenticated. An OTA mechanism that downloads and flashes any image from the update server, without verifying the image's signature, can be exploited by: compromising the update server (supply chain attack), executing a man-in-the-middle attack on the download channel, or obtaining valid update server credentials. The bootloader's signature verification is the root of trust that makes the OTA mechanism "secure" rather than merely "functional." Module 12 and Module 15 both cover this — it is the integration of firmware signing (Module 12) with OTA delivery (Module 15) that produces a complete OWASP #4 mitigation.
  - *Why C is incorrect:* A dedicated management network is an operational hardening measure but not a requirement of OWASP #4 mitigation. Many production IoT systems deliver OTA updates over the same network as operational telemetry, using topic separation and access control for isolation.
  - *Why D is incorrect:* Downgrade prevention is a valid security hardening measure — it prevents an attacker who can trigger an OTA update from forcing the device to run known-vulnerable firmware. However, it is a defense-in-depth addition, not a requirement for the basic OWASP #4 mitigation. Many production systems allow rollback for operational recovery reasons.

---

### Question 5

In the capstone project, the `vAnomalyTask` reads from a secondary queue that `vSensorTask` also writes to. Both tasks are at priority 2. A developer adds a third task at priority 2 that also needs to read from the same sensor queue. What FreeRTOS problem arises, and what is the correct architectural fix?

- A) Three tasks at the same priority cannot coexist in FreeRTOS — the scheduler requires all tasks to have unique priority levels. The fix is to assign each task a unique priority (1, 2, 3).
- B) A single FreeRTOS queue has only one consumer. If three tasks all call `xQueueReceive()` on the same queue, each item will be received by only one of the three tasks in a non-deterministic order, depending on which task is first to unblock. The correct fix depends on the requirement: if all three tasks need every reading, use a fan-out pattern — the sensor task writes to three separate queues, one per consumer task. If only one task needs each reading, the existing queue with three consumers provides natural load balancing.
- C) A single FreeRTOS queue with three consumers requires `xQueueReceive()` to be called with a mutex guard to prevent two tasks from dequeuing the same item simultaneously. Add a mutex around every `xQueueReceive()` call in all three consumer tasks.
- D) The `vAnomalyTask` at priority 2 will always receive items before the new priority-2 task because FreeRTOS gives priority to the task that has been blocked the longest when multiple equal-priority tasks are waiting on the same queue.
- **Correct Answer:** B) Each item goes to only one consumer; use fan-out queues if all consumers need every reading.
- **Distractor Analysis:**
  - *Why A is incorrect:* FreeRTOS fully supports multiple tasks at the same priority — they share CPU time via round-robin time slicing. There is no requirement for unique priorities.
  - *Why B is correct:* A FreeRTOS queue is a FIFO buffer. `xQueueReceive()` atomically removes one item from the queue. If three tasks call `xQueueReceive()` on the same queue, each item is consumed by exactly one task — the first task to successfully dequeue it. This is correct if the tasks are parallel workers processing different readings (load balancing). It is incorrect if each task needs to see every reading (fan-out requirement). For the anomaly detection use case, if both the MQTT publish task and the anomaly task need every reading, the sensor task must write to two separate queues, one per consumer.
  - *Why C is incorrect:* `xQueueReceive()` is already thread-safe — the FreeRTOS queue implementation uses internal locking. Adding an additional mutex around `xQueueReceive()` is unnecessary and introduces a deadlock risk if the mutex is also used elsewhere.
  - *Why D is incorrect:* FreeRTOS does use "longest blocked" ordering when multiple equal-priority tasks unblock simultaneously (fair scheduling within a priority level), but this is a tie-breaking rule, not a guarantee that a specific task always wins. Both tasks will receive items, not always the same one.

---

### Question 6

A developer documents their capstone system's "Connecting the Tiers" communication contract as: "Device publishes JSON to topic `sensors/temp` over MQTT." A security reviewer marks this documentation as incomplete. What is the minimum additional information required to make this a complete communication contract?

- A) The documentation must include the exact JSON schema with field names and types, because without the schema, the cloud processing tier cannot parse incoming messages.
- B) The documentation must specify the protocol and transport security (MQTT over TLS 1.3 on port 8883), the authentication mechanism (mTLS with per-device X.509 certificate), the QoS level (0, 1, or 2), the message format with required fields and data types, and the expected message rate — these together define the complete contract between the device and the broker tiers.
- C) The documentation must specify the topic access control policy (which devices are authorized to publish to this topic) and the message retention policy (how long the broker retains undelivered messages for offline subscribers).
- D) The documentation must specify the firmware version that first introduced this message format, so that the processing tier can apply version-specific parsing logic for devices running different firmware versions.
- **Correct Answer:** B) Protocol, security, authentication, QoS, message format, and rate are all required for a complete contract.
- **Distractor Analysis:**
  - *Why A is incorrect:* The JSON schema is one component of a complete contract (included in "message format with required fields and data types"), but it is not the only missing element. The security reviewer's concern is that the documented contract omits transport security, authentication, QoS semantics, and rate expectations — all of which affect the broker and processing tier's design.
  - *Why B is correct:* A communication contract specifies everything a receiving tier needs to know to accept and process messages correctly: How does the sender connect? (MQTT over TLS 1.3 on port 8883) How is the sender authenticated? (mTLS with device certificate) What delivery guarantee is provided? (QoS 1 = at-least-once) What does a message look like? (JSON schema with field names and types) How often does the sender publish? (every 30 seconds). Without this information, the broker cannot configure its access control policies correctly, and the processing tier cannot size its ingestion infrastructure or handle the data correctly.
  - *Why C is incorrect:* Topic ACL and message retention are operational configuration details, not contract specifications. They are determined by the contract's requirements, not part of the contract definition itself. Access control policies derive from the authentication contract; retention is a broker configuration choice based on QoS and subscriber availability.
  - *Why D is incorrect:* Firmware versioning in message schemas is a schema evolution concern — important for long-running systems but not a required element of an initial communication contract. The contract should include the current message format; version compatibility is addressed through schema versioning practices documented separately.

---

### Question 7

Which certification is most appropriate for a student who has completed CIS-4355 and wants to demonstrate general IoT knowledge across hardware, networking, and security to entry-level employers, without committing to a specific cloud vendor ecosystem?

- A) AWS Certified Specialty — IoT Core, because it is the most recognized IoT certification and demonstrates both general IoT knowledge and cloud implementation skills.
- B) CompTIA IoT+, because it is vendor-neutral, covers IoT hardware, networking, security, and deployment fundamentals, and is an appropriate entry-level credential for candidates who have completed a practical IoT course like CIS-4355.
- C) AZ-220 Azure IoT Developer, because Microsoft Azure is the most widely deployed enterprise IoT platform and the AZ-220 certification provides the broadest employer recognition.
- D) Cisco IoT Fundamentals, because it is the only certification that covers embedded systems programming with FreeRTOS and MQTT protocol implementation in detail.
- **Correct Answer:** B) CompTIA IoT+ — vendor-neutral, entry-level, appropriate for post-course candidates.
- **Distractor Analysis:**
  - *Why A is incorrect:* AWS IoT Specialty is a professional-level certification requiring significant AWS platform experience beyond the course content. It is not appropriate as an "entry-level" credential immediately after course completion for most students. It is a valid next certification after gaining AWS platform experience.
  - *Why B is correct:* CompTIA IoT+ is specifically designed as a practitioner-level, vendor-neutral IoT certification covering the breadth of topics that an entry-level IoT professional needs: hardware interfaces, connectivity protocols, data management, and security. CIS-4355 graduates have knowledge exceeding the CompTIA IoT+ baseline in several areas. The vendor-neutral positioning means the credential is recognized regardless of which cloud platform a hiring employer uses.
  - *Why C is incorrect:* AZ-220 is an associate-level Microsoft-specific certification. While it is valuable, it commits the candidate to Azure-specific knowledge and requires Azure platform hands-on experience that is not covered in CIS-4355. It is a strong certification target for students pursuing Azure IoT roles specifically, not for general employer recognition.
  - *Why D is incorrect:* Cisco IoT Fundamentals does not cover embedded systems programming with FreeRTOS or detailed MQTT implementation — it covers networking concepts, IoT architecture fundamentals, and basic security. It is a networking-focused credential, not an embedded systems programming credential.

---

### Question 8

A capstone project's known limitations section documents: "Issue: Device certificates are valid for 365 days and must be manually renewed. Risk: HIGH — if certificates expire, devices cannot authenticate and go offline. Planned resolution: Implement automated certificate renewal using AWS IoT certificate rotation. Current workaround: Calendar reminder to renew certificates 30 days before expiry." What is the most significant problem with this known limitations entry?

- A) The risk level "HIGH" is incorrect — certificate expiry causing device offline events is a medium-severity operational issue, not a high-severity security concern.
- B) The "current workaround" (calendar reminder) is not an engineering control — it depends entirely on human memory and process compliance. For a fleet of 1,000 devices with staggered certificate expiry dates, calendar reminders will inevitably be missed, causing device outages. The workaround should be an automated monitoring alert: an alert that fires 60 days before any device certificate expires, giving the team time to renew before the workaround deadline.
- C) The "planned resolution" incorrectly references "certificate rotation" — the correct AWS IoT term is "certificate renewal," and using the wrong term will confuse reviewers familiar with the AWS IoT documentation.
- D) The known limitations entry is complete and well-written — the risk level, workaround, and planned resolution are all appropriate, and no changes are needed.
- **Correct Answer:** B) The workaround relies on human process rather than an automated engineering control.
- **Distractor Analysis:**
  - *Why A is incorrect:* "HIGH" is the correct risk classification. An entire device fleet going offline because certificates were not renewed on schedule is a high-severity operational incident. Certificate expiry issues have caused real production outages in IoT deployments. The risk level is appropriate.
  - *Why B is correct:* The fundamental principle of operational reliability is that human-dependent processes are unreliable at scale. A calendar reminder is appropriate for 5 devices; it is completely inadequate for 1,000 devices with different expiry dates. The minimum acceptable workaround for certificate expiry monitoring is an automated system that queries the device registry for certificates expiring within 60 days and fires an alert. This is an engineering control — it works regardless of whether anyone remembered to set a calendar reminder.
  - *Why C is incorrect:* AWS IoT uses the term "certificate rotation" in its documentation for the process of issuing a new certificate to a device while the old one is still valid. Using this term is technically correct in context. The distinction between "rotation" and "renewal" is minor and would not confuse a knowledgeable reviewer.
  - *Why D is incorrect:* The entry has a real weakness — the human-dependent workaround — that should be improved before the documentation is considered complete. Accepting documentation with known process-dependent workarounds as "complete and well-written" would lower the engineering bar for the entire team.

---

### Question 9

A student reviewing for the AZ-220 Azure IoT Developer exam encounters this question in a practice test: "A company needs to provision 50,000 IoT devices to their Azure IoT Hub without manual intervention at the device level. Devices will be manufactured in batches and must connect to different IoT Hubs based on geographic region. Which Azure service and which enrollment type should they use?" What is the correct answer?

- A) Use Azure IoT Hub with individual device enrollment. Configure each device's connection string manually during manufacturing, targeting the regional IoT Hub directly.
- B) Use Azure Device Provisioning Service (DPS) with enrollment groups. Configure each device with the DPS global endpoint and a group enrollment that uses an X.509 CA certificate. DPS automatically allocates devices to regional IoT Hubs based on a configured allocation policy, enabling zero-touch provisioning without manual per-device configuration.
- C) Use Azure IoT Central with automatic device templates. IoT Central automatically provisions all devices connecting with valid credentials and does not require a separate provisioning service.
- D) Use Azure IoT Edge with nested edge topology. Configure a regional edge gateway in each geographic area; devices connect to the nearest edge gateway, which registers them with the IoT Hub in that region.
- **Correct Answer:** B) Azure DPS with enrollment groups and X.509 CA certificates, using allocation policies for regional routing.
- **Distractor Analysis:**
  - *Why A is incorrect:* Manual per-device connection string configuration during manufacturing is not "without manual intervention at the device level" — it is exactly the opposite. It also hardcodes each device to a specific IoT Hub at manufacturing time, eliminating the ability to rebalance load or recover from a regional IoT Hub outage. This approach does not scale to 50,000 devices.
  - *Why B is correct:* Azure DPS with enrollment groups is the designed solution for fleet-scale zero-touch provisioning. Enrollment groups allow a single CA certificate to authenticate all devices in a batch. The DPS allocation policy can be set to "GeoLatency" or a custom Azure Function that routes devices to regional IoT Hubs based on device metadata. This is exactly the Module 15 JITP pattern applied to the Azure platform — confirming that course content aligns with AZ-220 exam material.
  - *Why C is incorrect:* Azure IoT Central is a higher-level SaaS platform that does provide simplified device management, but it does not support the geographic routing requirement or the same level of customization as IoT Hub + DPS. More importantly, AZ-220 is specifically an IoT Hub/IoT Edge exam — IoT Central is a separate product area.
  - *Why D is incorrect:* Azure IoT Edge nested topology is designed for industrial scenarios where edge devices need local processing capability and intermittent cloud connectivity — not for geographic load balancing of device-to-cloud connections. It adds significant complexity without addressing the registration and routing requirement.

---

### Question 10

A complete IoT system design review is being conducted. The reviewer checks each of the course's key modules against the proposed design. Which combination of missing controls represents the most critical unaddressed risk surface — prioritized by likelihood of exploitation and potential impact?

- A) Missing: MFCC feature extraction optimization (Module 14) and custom ADR format (Module 16). These represent gaps in on-device inference performance and documentation quality that reduce the system's long-term maintainability.
- B) Missing: per-device X.509 certificates for mTLS (Module 12), firmware signature verification on OTA updates (Modules 12 and 15), and watchdog timer monitoring of the MQTT task (Module 13). Together these create a system where devices can be impersonated, malicious firmware can be delivered and executed without detection, and the primary communication task can hang indefinitely causing silent data loss.
- C) Missing: FreeRTOS queue fan-out pattern (Module 13) and device twin delta compression (Module 15). These represent scaling limitations that will become critical when the fleet exceeds 10,000 devices.
- D) Missing: MFCC window size optimization (Module 14) and alert threshold calibration (Module 15). These reduce the accuracy of anomaly detection but do not represent exploitable attack surfaces.
- **Correct Answer:** B) Missing mTLS certificates, firmware signature verification, and watchdog — the three highest-impact security and reliability gaps.
- **Distractor Analysis:**
  - *Why A is incorrect:* MFCC optimization and ADR format are quality-of-implementation concerns, not security vulnerabilities. Neither creates an exploitable attack surface. Missing these items reduces code efficiency and documentation quality but does not create direct security or reliability risk.
  - *Why B is correct:* The three missing controls in this option represent the core security and reliability foundations of the system. Missing mTLS certificates means any device — including unauthorized and counterfeit devices — can authenticate to the broker using username/password, which is guessable or interceptable. Missing firmware signature verification means the OTA mechanism is an unauthenticated code execution path — a critical vulnerability. Missing watchdog monitoring on the MQTT task means the device can silently lose all cloud connectivity indefinitely after a task hang, with no recovery. These three gaps together create a system that can be impersonated, remotely compromised via OTA, and silently fails in production — the three highest-impact failure categories.
  - *Why C is incorrect:* Queue fan-out pattern and device twin delta compression are architectural optimization patterns. Their absence does not create an attack surface — it creates functional limitations (each sensor reading goes to only one consumer, and delta payloads are larger than necessary). These are performance and correctness concerns for a specific architecture, not security vulnerabilities.
  - *Why D is incorrect:* MFCC window size and alert thresholds affect detection accuracy but not security. A poorly calibrated alert threshold generates false positives or misses some anomalies; it does not create an attack vector. These are important operational parameters but are not "critical unaddressed risk surface" in the sense of exploitable vulnerabilities.

---
