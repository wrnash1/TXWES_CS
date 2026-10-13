# Video Script: Module 15 — IoT Project Deployment and Management

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Duration:** 15–18 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **IoT Deployment and Fleet Management — From One Device to One Million**

**Alt-text:** Instructor at desk. Title card reads "Module 15: IoT Project Deployment and Management." Background monitor shows a cloud platform dashboard with a map of device locations and health indicators.

**Audio:** "Welcome to Module 15. Everything we have built in this course — sensors, MQTT communication, RTOS tasks, TLS security, TinyML models — has been developed on a single device. In this module we scale up: how do you provision, manage, update, monitor, and eventually decommission not one device, but ten thousand? Or a million?"

"The gap between a working prototype and a production IoT deployment is not just engineering — it is operations. Industrial IoT companies lose millions of dollars annually to device outages caused by bad firmware updates, expired certificates, silent failures, and lack of visibility into fleet health. Understanding fleet management before you deploy protects both your customers and your organization."

"By the end of this module you will be able to: describe device provisioning workflows including zero-touch provisioning, explain fleet management concepts including device registry and device twins, design a safe staged OTA firmware update rollout, define the monitoring metrics and alerting thresholds for an IoT fleet, and describe the full device lifecycle from provisioning through secure decommissioning."

**Study Link:** [AWS IoT Core Device Management — docs.aws.amazon.com](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-management.html)

---

### [02:00 – 04:30] Device Provisioning at Scale

**Visual:** Side-by-side diagrams showing manual provisioning (single device, human with laptop) vs. zero-touch provisioning (factory floor, devices on conveyor, automated certificate injection).

**Alt-text:** Left panel labeled "Manual Provisioning" shows one device connected to a laptop via USB, with a person at the keyboard. Right panel labeled "Zero-Touch Provisioning" shows a factory production line with devices moving on a conveyor. Each device passes a workstation that automatically injects a certificate, registers it in a cloud registry, and prints a QR code on the device packaging.

**Audio:** "Provisioning is the process of giving a device its unique identity and credentials so it can securely connect to the cloud. When you are making one prototype, you manually flash credentials to the device over USB. When you are manufacturing 100,000 devices per month, manual provisioning is completely infeasible."

"**Zero-touch provisioning** — also called Just-In-Time Provisioning (JITP) or Claim-Based Provisioning — automates the provisioning process. The general pattern: during manufacturing, each device receives a bootstrap claim certificate — a temporary credential used only for the initial connection. When the device connects to the cloud for the first time, it presents the claim certificate. The provisioning service validates the claim, creates a unique device identity and certificate, registers the device in the device registry, and sends the unique credentials to the device. The device stores its permanent credentials and connects with those going forward."

"AWS IoT Core, Azure IoT Hub, and Google Cloud IoT Core all provide JITP services. The claim certificate can be the same for all devices in a manufacturing batch — it is a temporary bootstrap credential, not a permanent identity. However, as we covered in Module 12, the claim certificate must be rotated or revoked after provisioning is complete, so it cannot be used to enroll unauthorized devices."

"During provisioning, the device also receives its initial configuration: broker endpoint address, MQTT topic prefix, firmware version target, and any device-specific parameters. This configuration is typically stored in a cloud-managed **device twin** — a JSON document that mirrors the device's desired and reported state."

---

### [04:30 – 07:00] Fleet Management and Device Registry

**Visual:** Dashboard screenshot showing a device registry table with columns for device ID, firmware version, last seen timestamp, connection status, and alert status.

**Alt-text:** A web dashboard table with five column headers: Device ID, Firmware Version, Last Seen, Status, Alerts. Six rows are shown: four rows with green status indicators labeled "Online," one row with a yellow indicator labeled "Degraded," and one row with a red indicator labeled "Offline." The firmware version column shows a mix of "v2.1.0" and "v2.0.3" values, indicating fleet version fragmentation.

**Audio:** "A device registry is the authoritative record of every device in your fleet: its identity, certificate, current firmware version, configuration, and health status. Without a registry, you have no visibility — you cannot answer basic operational questions: how many devices are online right now? Which firmware version are they running? When did each device last connect? Is there a regional cluster of failures suggesting a connectivity issue?"

"The **device twin** — called a device shadow in AWS IoT, a device twin in Azure IoT Hub — is a JSON document with two sections: **desired** state (what you want the device to do, set by the cloud) and **reported** state (what the device is actually doing, set by the device). The gap between desired and reported state drives configuration synchronization."

"For example, the desired firmware version might be 'v2.1.0' while a device reports 'v2.0.3'. The device management system detects this gap and schedules an OTA update job for that device. When the update completes, the device updates its reported firmware version to 'v2.1.0' and the gap closes."

"Fleet management systems also track: last connection timestamp (used to detect offline devices), telemetry health metrics (packet error rates, reconnect counts), certificate expiry dates (trigger renewal before expiry), and location data for geographically distributed fleets. Modern platforms like AWS IoT Fleet Indexing allow SQL-like queries across the entire fleet: 'show me all devices running firmware older than v2.0.0 that have been offline for more than 24 hours in the Texas region.'"

---

### [07:00 – 10:00] OTA Firmware Updates

**Visual:** Staged rollout diagram showing the progression from canary group through pilot group to general availability, with monitoring gates between stages.

**Alt-text:** A horizontal flow diagram showing four boxes connected by arrows: Canary Group (100 devices, 0.1%), then a monitoring gate labeled "Error rate check," then Pilot Group (10,000 devices, 10%), then another monitoring gate, then General Availability (remaining fleet). Below the monitoring gates are labels: "Halt and rollback if error > 1%" and "Proceed only if error < 0.5%." A separate rollback arrow loops from each stage back to the previous firmware version.

**Audio:** "Over-the-air firmware updates are how you fix bugs, patch security vulnerabilities, and add features to deployed devices — without sending a technician to each device. OTA is not optional for production IoT systems; it is a fundamental design requirement, as we discussed when covering OWASP IoT #4."

"The OTA architecture has three components. The **firmware repository** stores the signed firmware binaries, indexed by version number. The **device management platform** maintains a job queue — devices poll for new jobs or receive push notifications, download the firmware, verify the signature, flash the new image to a secondary partition, and reboot into the new firmware. If the new firmware fails to boot or fails its self-test, it falls back to the previous partition. The **update orchestration layer** controls rollout timing, group targeting, and success/failure monitoring."

"**Staged rollouts** are the single most important safety practice for OTA updates. The process: deploy first to a small canary group — perhaps 0.1% of the fleet. Monitor for 24–48 hours for elevated error rates, reboot loops, or offline devices. If metrics are clean, expand to a pilot group — 5–10% of the fleet. Monitor again. Then proceed to general availability. Define halt thresholds at each gate: if more than 1% of canary devices show errors, halt the rollout and investigate before proceeding."

"Critical OTA requirements: firmware signature verification before flashing (covered in Module 12); rollback capability to the previous firmware if the new version fails; power-fail-safe flashing using dual partition or A/B partition scheme — a power loss mid-flash must not brick the device; and resumable download for large firmware files over unreliable connections."

"The ESP32 natively supports A/B partition OTA via the esp_ota_ops API. The bootloader maintains an OTA state register that indicates which partition to boot. After downloading and verifying a new firmware image to the secondary partition, the device calls `esp_ota_set_boot_partition()` and reboots. If the new firmware confirms successful startup with `esp_ota_mark_app_valid_cancel_rollback()`, the update is committed. If the device reboots before confirming, the bootloader automatically rolls back to the previous partition."

---

### [10:00 – 13:00] Monitoring and Alerting

**Visual:** Monitoring architecture diagram showing device → MQTT broker → time-series database → dashboard and alerting.

**Alt-text:** A left-to-right flow diagram. Device icon on left publishes telemetry to MQTT Broker. Broker routes data to a Stream Processor which writes to a Time-Series Database. The database feeds two branches: a real-time Dashboard showing charts, and an Alerting Engine that sends notifications to an on-call engineer's phone via SMS when thresholds are crossed.

**Audio:** "Monitoring means having visibility into what your fleet is doing right now. Alerting means being notified automatically when something goes wrong. Together, they transform fleet management from reactive — 'we got a complaint, let's investigate' — to proactive — 'we detected an anomaly at 3 AM and had an engineer fix it before anyone noticed.'"

"The key telemetry metrics for IoT fleet health fall into four categories. **Connectivity metrics:** connection success rate, reconnect frequency, time between reconnects. A device that reconnects every 30 seconds has a problem. **Data quality metrics:** expected message rate vs. actual message rate, sensor value plausibility (is the temperature reading physically possible?), message timestamp drift. **Device health metrics:** battery voltage (if applicable), free heap memory, CPU temperature, uptime since last reboot. **Business metrics:** the application-specific values your system was deployed to measure — water flow rates, equipment utilization, package location."

"Time-series databases — InfluxDB, TimescaleDB, AWS Timestream, Azure Time Series Insights — are optimized for storing and querying time-stamped sensor data. They automatically handle downsampling for long-term storage (keeping 1-minute averages instead of every 5-second reading after 30 days) and support high-cardinality queries (find all devices of type X in region Y with value Z in the last hour)."

"Alerting thresholds should be based on observed data distributions, not guesses. Run your fleet for two weeks in healthy condition, compute the normal range for each metric, and set alert thresholds at the 1st and 99th percentile of that distribution. Too-sensitive thresholds cause alert fatigue — engineers start ignoring alerts. Too-insensitive thresholds miss real problems. Review and tune thresholds quarterly."

---

### [13:00 – 15:30] Device Lifecycle and Decommissioning

**Visual:** Device lifecycle diagram showing five phases in a circular flow: Manufacture → Provision → Deploy → Manage → Decommission.

**Alt-text:** A circular flow diagram with five labeled phases. Phase 1: Manufacture — hardware production, firmware flashing. Phase 2: Provision — certificate injection, registry enrollment. Phase 3: Deploy — physical installation, network connectivity verification. Phase 4: Manage — OTA updates, telemetry monitoring, configuration management. Phase 5: Decommission — certificate revocation, registry deletion, data retention, physical disposal.

**Audio:** "Every IoT device has a lifecycle. It begins in manufacturing, proceeds through provisioning and deployment, spends most of its life in the managed phase, and eventually must be retired. Decommissioning is the step most organizations get wrong — because it is invisible. A decommissioned device that still has an active certificate can be used to authenticate to your cloud backend, potentially by an attacker who found the device in a dumpster."

"Complete decommissioning requires four steps. First, **certificate revocation** — add the device's certificate to the Certificate Revocation List or disable its registration in the device registry. No certificate, no authentication. Second, **registry deletion** — remove the device twin and all associated metadata from the device registry. Third, **data retention decisions** — determine which historical telemetry data must be retained for regulatory compliance and archive it; delete the rest. Fourth, **physical security** — the device's flash memory may contain encryption keys, certificates, and sensitive configuration data. Devices should be cryptographically erased before physical disposal. Devices with hardware security elements should have those elements destroyed or permanently locked."

"For high-security or high-sensitivity applications, physical destruction of the flash chip or PCB may be required before disposal. Many enterprise IoT providers offer managed decommissioning workflows that automate the first three steps — certificate revocation, registry deletion, and data archival — with a single API call."

---

### [15:30 – End] Summary and Lab Preview

**Visual:** Summary slide with the device lifecycle phases and their key tools.

**Audio:** "Let's recap Module 15. Zero-touch provisioning automates credential injection at manufacturing scale. The device registry and device twins provide fleet visibility and configuration synchronization. Staged OTA rollouts with signature verification and A/B partitioning enable safe firmware updates at scale. Time-series telemetry with tuned alerting thresholds enables proactive monitoring. And complete decommissioning — certificate revocation, registry deletion, data retention, and secure hardware disposal — closes the device lifecycle securely."

"In the lab, you will simulate a fleet management workflow: create device registration records and device twins using the AWS IoT console or a simulated equivalent, push a device shadow update from the cloud, have an ESP32 detect the shadow update and apply a configuration change, simulate an OTA update job, and configure a basic health metric alert."

**Key Terms for This Module:**

- Zero-touch provisioning / Just-In-Time Provisioning (JITP)
- Claim certificate
- Device registry
- Device twin / device shadow (desired state, reported state)
- OTA firmware update
- A/B partition scheme
- `esp_ota_set_boot_partition()`, `esp_ota_mark_app_valid_cancel_rollback()`
- Staged rollout — canary group, pilot group, general availability
- Time-series database (InfluxDB, AWS Timestream)
- Alert threshold, alert fatigue
- Device lifecycle — manufacture, provision, deploy, manage, decommission
- Certificate revocation, registry deletion
- Fleet indexing

"In Module 16 — our final module — we bring everything together in the capstone project and review certification pathways."

---
