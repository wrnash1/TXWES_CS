# Reading Guide: Module 15 — IoT Project Deployment and Management

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you should be able to:

- Explain zero-touch provisioning and the role of claim certificates in fleet-scale credential injection
- Describe the device twin model and how desired/reported state drives configuration synchronization
- Design a staged OTA firmware rollout strategy with safety gates and automatic rollback
- Define the key telemetry metrics for IoT fleet health monitoring and explain how to set alert thresholds
- Enumerate the four required steps of complete device decommissioning

---

## Section 1 — Device Provisioning at Scale

### The Provisioning Problem

Provisioning — giving each device a unique, secure identity before it can communicate with the cloud — is trivial for a prototype and a fundamental engineering challenge at scale. Three properties make provisioning difficult at scale:

**Uniqueness:** Every device needs credentials that uniquely identify it. Shared credentials mean one compromised device can impersonate any other device in the fleet.

**Security:** Credentials must be injected in a tamper-resistant way. An attacker who intercepts provisioning traffic can create counterfeit devices that appear legitimate to the cloud.

**Scale:** A factory producing 100,000 devices per month cannot manually configure each device. The provisioning flow must be automated, fast (under 10 seconds per device at the production line), and reliable.

### Provisioning Methods

**Manual provisioning** is used for development and small pilots. The developer generates credentials, flashes them to the device via USB, and manually registers the device in the cloud console. This is the workflow most students use for lab exercises.

**Factory provisioning** is used for production at scale. Credentials are injected into each device during the manufacturing process, either by a Manufacturing Execution System (MES) that calls a provisioning API for each device, or by pre-generating credential packages and distributing them to the factory's programming stations. Each device's certificate is unique, generated from the manufacturer's CA hierarchy.

**Just-In-Time Provisioning (JITP)** defers full credential issuance to the device's first cloud connection. The device ships from the factory with a temporary bootstrap credential — the claim certificate. On first connection, the provisioning service validates the claim, creates the device's permanent identity and unique certificate, registers the device in the registry, and delivers the permanent credentials to the device over the encrypted claim-certificate connection. The claim certificate is then invalidated.

**Fleet provisioning by trusted user** is a variant where an IT administrator or installer completes provisioning in the field using an authenticated mobile app that calls the provisioning API on behalf of the device. This is common for commercial HVAC systems and network equipment.

### The Claim Certificate

The claim certificate is a temporary X.509 certificate that all devices in a manufacturing batch may share. It authenticates the device to the provisioning service but does not serve as a permanent device identity.

Critical operational requirements for claim certificates:

- Rotation: generate a new claim certificate per manufacturing batch (monthly or weekly), not per product generation.
- Revocation: after provisioning is complete for a batch, revoke or deactivate the claim certificate immediately.
- Scope restriction: configure the provisioning endpoint to accept only claim certificate connections for the specific provisioning API endpoints — not for operational MQTT topics.

The claim certificate is the IoT equivalent of a factory reset PIN — it is intentionally temporary and must be managed as a high-risk credential.

---

## Section 2 — Fleet Management and Device Twins

### Device Registry

The device registry is the authoritative inventory of every device in the fleet. At minimum, a registry entry contains:

- Device ID (unique identifier, typically the certificate Common Name)
- Certificate fingerprint and status (active, revoked, expired)
- Current firmware version (as reported by the device)
- Last connection timestamp
- Device type and hardware revision
- Geographic location or installation site

The registry is the starting point for all fleet management operations: targeting OTA updates at specific device groups, querying the health of devices at a specific site, and initiating decommissioning for retired devices.

### Device Twins and Shadow Documents

A device twin (called a device shadow in AWS IoT Core, a digital twin in broader IoT contexts) is a persistent JSON document in the cloud that represents the device's state — even when the device is offline. The twin has two sections:

**Desired state:** Set by the cloud application or administrator. Represents the intended configuration of the device. Example: `{"firmware_target": "v2.1.0", "reporting_interval_s": 30}`.

**Reported state:** Set by the device. Represents the device's actual current state. Example: `{"firmware_version": "v2.0.3", "reporting_interval_s": 60, "uptime_s": 86400}`.

**Delta:** The difference between desired and reported state. The device subscribes to the delta topic and receives updates whenever the desired state changes. The device applies the configuration change and updates its reported state. The cloud application monitors the delta topic to confirm synchronization.

This asynchronous synchronization model is important for IoT: the device may be offline for hours. When it reconnects, it immediately receives the accumulated delta of all configuration changes made during its offline period and applies them in order.

### Fleet Indexing and Querying

Modern IoT platforms support SQL-like queries across the entire device registry and twin state. AWS IoT Fleet Indexing allows queries such as:

```sql
SELECT thingName, shadow.reported.firmware_version, shadow.reported.battery_pct
FROM 'AWS/Things'
WHERE shadow.reported.firmware_version < 'v2.1.0'
AND shadow.reported.battery_pct < 15
AND connectivity.connected = false
```

This query returns all offline devices running old firmware with low battery — exactly the devices that need attention before a site visit becomes necessary.

---

## Section 3 — OTA Firmware Updates

### OTA Architecture

A production OTA system has three components:

**Firmware repository:** Stores signed firmware binaries indexed by version. Access is restricted to the build and release pipeline — no manual uploads. Each firmware binary includes a manifest with: version string, target hardware revisions, minimum compatible firmware version (for migration compatibility), and the SHA-256 hash and ECDSA signature.

**Device management platform:** Manages OTA job queues. A job targets a device group, specifies the firmware version, and defines the rollout policy (rate, timeout, error threshold). Devices poll for jobs or receive MQTT notifications. On receiving a job, the device downloads the firmware, verifies the signature, writes to the secondary partition, and reboots.

**Orchestration and monitoring:** Controls staged rollout progression. Monitors success rates, error rates, and device health metrics per stage. Pauses rollout automatically if error rates exceed thresholds.

### A/B Partition Scheme

The ESP32 supports dual-application partitions (OTA_0 and OTA_1) in its partition table. The bootloader reads an OTA state register to determine which partition to boot. The OTA workflow:

1. Device receives OTA job and begins downloading firmware to the inactive partition.
2. Download is resumable — if interrupted, it continues from the last received offset on reconnect.
3. After successful download, the device verifies the firmware signature using the stored public key.
4. The device calls `esp_ota_set_boot_partition()` to mark the new partition as the next boot target.
5. The device reboots. The bootloader boots the new partition.
6. The new firmware runs its self-test. If the self-test passes, it calls `esp_ota_mark_app_valid_cancel_rollback()` to commit the update.
7. If the device reboots again before committing (power loss, crash), the bootloader detects the uncommitted state and boots the previous partition — automatic rollback.

This scheme guarantees that a power failure during an OTA update can never leave the device in an unbootable state — there is always a known-good partition available.

### Staged Rollout Strategy

A staged rollout minimizes the blast radius of a defective firmware release:

**Canary stage:** 0.1–1% of fleet. Target devices selected for hardware diversity, geographic diversity, and operational diversity (high-traffic devices preferred for canaries — they stress-test the firmware faster). Monitor for 24–48 hours with strict error thresholds (halt if >1% error rate).

**Pilot stage:** 5–10% of fleet. Broader coverage. Monitor for 48–72 hours with slightly relaxed thresholds.

**General availability:** Remaining fleet. Can be deployed in parallel or in geographic waves.

Define explicit halt criteria at each gate:

- Elevated device reboot frequency (more than 2 reboots per device per hour)
- Increased MQTT reconnect rate (suggests firmware degrading network stack)
- New error codes appearing in telemetry that were not present in the previous firmware
- Devices not confirming successful OTA boot within expected timeout

---

## Section 4 — Monitoring and Alerting

### Telemetry Categories

Fleet monitoring requires telemetry across four dimensions:

**Connectivity health:** MQTT connection success rate, reconnect frequency (reconnects/hour), time to reconnect after network loss, TLS handshake failure rate. Alert thresholds: >3 reconnects/hour for any device, TLS failure rate >0.1% for any device.

**Data quality health:** Message rate vs. expected rate (ratio of actual to expected messages in a rolling 5-minute window), sensor plausibility checks (temperature outside physically possible range), timestamp monotonicity violations (messages arriving out of order or with future timestamps). Alert thresholds: message rate <50% of expected rate, any plausibility violation.

**Device health:** Available heap memory (alert when free heap drops below 20% of initial free heap — indicates memory leak), CPU temperature (alert when within 10°C of thermal throttle limit), uptime since last reboot (alert when uptime resets unexpectedly — indicates crash). Battery voltage if applicable.

**Application health:** Business-level metrics specific to the application — flow rate, door open/close counts, package location updates. Deviations from expected patterns may indicate sensor failure or environmental issues.

### Time-Series Databases

IoT telemetry is time-series data: sequences of (timestamp, value) pairs at regular intervals. Relational databases are poorly suited to this workload — queries like "give me the average temperature per minute for all devices in Building A over the last 30 days" are extremely slow in SQL on normalized tables with millions of rows.

Time-series databases (TSDBs) solve this with:

**Column-oriented storage:** Each metric is stored in a separate column, enabling highly compressed storage of repeated similar values and fast single-metric queries.

**Automatic downsampling:** TSDBs can automatically compute and store aggregates (hourly averages, daily max/min) and delete raw data after a retention period, controlling storage growth.

**High-cardinality indexing:** TSDBs handle millions of unique device IDs as tag values efficiently — a capability that breaks standard relational database indices.

Common TSDBs for IoT: InfluxDB (open source, common in self-hosted deployments), AWS Timestream (managed, integrated with IoT Core), Azure Time Series Insights (managed, integrated with IoT Hub), TimescaleDB (PostgreSQL extension for time-series workloads).

### Alert Threshold Calibration

The two failure modes of alerting:

**Alert fatigue:** Thresholds set too sensitively cause hundreds of alerts per day. Engineers learn to ignore them. The alert system fails silently — real problems are missed because the alert channel is treated as noise.

**Missed incidents:** Thresholds set too conservatively miss real problems until they become outages. Customers notice before engineers do.

Calibration approach: collect 2–4 weeks of baseline telemetry from a healthy fleet. For each metric, compute the mean and standard deviation of normal values. Set alert thresholds at mean ± 3 standard deviations for normally distributed metrics, or at the 1st and 99th percentiles for skewed distributions. Review and adjust quarterly as the fleet matures.

---

## Section 5 — Device Lifecycle and Decommissioning

### Full Lifecycle

The IoT device lifecycle has five phases:

**Manufacture:** Hardware assembly, firmware flashing, basic hardware testing (power-on self-test, sensor calibration), and credential injection.

**Provision:** Cloud registration, device twin creation, and delivery of operational credentials. First heartbeat to the management platform confirming successful provisioning.

**Deploy:** Physical installation at operational site, connectivity verification, initial configuration delivery via device twin, and operational acceptance testing.

**Manage:** The operational phase — typically the longest phase (months to years). Includes OTA updates, configuration changes via device twin, health monitoring, incident response, and certificate renewal.

**Decommission:** Controlled retirement at end of operational life. Must be complete and verifiable.

### Complete Decommissioning

Incomplete decommissioning creates persistent security risks. A device in a dumpster with an active certificate and valid credentials can authenticate to your cloud backend indefinitely. The four required steps:

**Step 1 — Certificate revocation:** Add the device certificate to the CRL or set the certificate status to INACTIVE in the device registry. This step prevents the physical device from authenticating even if its credentials are extracted.

**Step 2 — Registry deletion:** Remove the device twin and all registry metadata. The device no longer appears in any fleet query, cannot receive OTA updates or configuration pushes, and cannot publish to operational MQTT topics.

**Step 3 — Data handling:** Determine regulatory retention requirements (GDPR, HIPAA, industry standards). Archive data that must be retained to cold storage. Delete data that does not need to be retained. Document the data disposition decision.

**Step 4 — Physical security:** Erase all credentials and sensitive configuration from the device's flash using a cryptographic erase command or a firmware wipe routine. For devices with hardware security elements (ATECC608A, TPM), trigger the device's secure element destruction or permanently lock its key slots. For high-security applications, physically destroy the PCB's flash chip.

---

## Key Terms

- **Zero-touch provisioning / JITP** — automated device credential issuance on first cloud connection using a temporary claim certificate
- **Claim certificate** — temporary bootstrap credential used only for the initial provisioning connection
- **Device registry** — authoritative inventory of all devices, their identities, certificates, and health state
- **Device twin / device shadow** — cloud-side JSON document representing a device's desired and reported configuration state
- **Delta** — the difference between desired and reported state in a device twin
- **OTA firmware update** — wireless delivery and installation of new firmware on deployed devices
- **A/B partition scheme** — dual flash partitions enabling safe firmware updates with automatic rollback
- **`esp_ota_mark_app_valid_cancel_rollback()`** — ESP-IDF call that commits a successful OTA update
- **Staged rollout** — phased OTA deployment through canary, pilot, and general availability stages with monitoring gates
- **Time-series database (TSDB)** — database optimized for timestamp-indexed data with automatic downsampling
- **Alert fatigue** — desensitization to monitoring alerts caused by excessive false positives
- **Device lifecycle** — the five phases from manufacture through decommissioning
- **Certificate revocation** — marking a certificate as invalid before its scheduled expiry date
- **Fleet indexing** — SQL-like querying across all device registry and twin state

---

## Review Questions

1. What are the three properties that make provisioning difficult at scale, and how does zero-touch provisioning address each one?
2. What is the claim certificate, and what two operational requirements must be met for it to be secure?
3. Explain the desired state and reported state sections of a device twin. What is the delta, and how does a device use it?
4. How does the A/B partition scheme on the ESP32 guarantee that a power failure during OTA flashing cannot leave the device unbootable?
5. What does `esp_ota_mark_app_valid_cancel_rollback()` do, and what happens if the device reboots before this function is called?
6. Define the three stages of a staged OTA rollout and explain what monitoring metrics should be checked at each gate before advancing to the next stage.
7. What is alert fatigue, and why does it represent a failure of the monitoring system rather than just an annoyance?
8. Name the four categories of fleet telemetry metrics and give one specific example of an alert condition for each category.
9. Why is a time-series database preferred over a relational database for IoT telemetry storage? Name two TSDB features that are specifically optimized for IoT data.
10. Enumerate the four required steps of complete device decommissioning. For each step, explain what security risk is mitigated by that step.

---

## 9. Supplemental Resources

**1. AWS IoT Core — Fleet Provisioning and Device Management Developer Guide**
[https://docs.aws.amazon.com/iot/latest/developerguide/iot-fleet-provisioning.html](https://docs.aws.amazon.com/iot/latest/developerguide/iot-fleet-provisioning.html)
AWS's official documentation covering Just-In-Time Provisioning (JITP), fleet provisioning by claim certificate, device registry structure, device shadow (twin) desired/reported/delta mechanics, and fleet indexing SQL queries — all of which map directly to the concepts in Sections 1 and 2 of this reading guide. The Fleet Indexing section includes worked query examples for targeting devices by firmware version, battery level, and connectivity state, making it a practical companion to the registry and shadow material in this module.

**2. InfluxDB — Time Series Data Platform Documentation**
[https://docs.influxdata.com/influxdb/cloud/](https://docs.influxdata.com/influxdb/cloud/)
InfluxDB's documentation covers the column-oriented storage model, high-cardinality tag indexing, automatic downsampling with Flux tasks, and retention policy configuration — the four TSDB features described in Section 4 of this reading guide. The "IoT Use Cases" section of the documentation demonstrates the exact pattern of storing device telemetry (device ID as a tag, sensor values as fields), computing per-device rolling averages, and setting alert thresholds — directly applicable to the fleet health monitoring workflow in the lab.

**3. Espressif Systems — ESP-IDF Over-the-Air Updates (OTA) API Reference**
[https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html)
Espressif's official OTA API documentation covering the A/B partition scheme, the `esp_ota_begin()` / `esp_ota_write()` / `esp_ota_end()` download pipeline, `esp_ota_set_boot_partition()`, `esp_ota_mark_app_valid_cancel_rollback()`, the bootloader's rollback detection logic, and resumable downloads via `esp_https_ota_perform()` with HTTP Range requests. This is the authoritative reference for the ESP32-specific OTA mechanics described in Section 3 and directly corresponds to the OTA simulation in the lab exercise.
