# Quiz: Module 15 — IoT Project Deployment and Management

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

### Question 1

A manufacturing company deploys 500,000 IoT sensors to customer sites using Just-In-Time Provisioning (JITP). The claim certificate used for provisioning is the same for all devices in the 2024 product generation and is never rotated or revoked after provisioning. Six months into deployment, a security researcher publishes a post showing they extracted the claim certificate from a device they purchased at retail. What is the impact and the correct immediate remediation?

- A) The impact is low because the claim certificate can only be used to connect to the provisioning endpoint, and the researcher cannot use it to access operational MQTT topics or telemetry data from the 500,000 deployed devices.
- B) The impact is critical: the exposed claim certificate allows the researcher (or any attacker who reads the post) to connect to the provisioning service and enroll unlimited unauthorized devices, obtaining valid production credentials for each. Immediate remediation: revoke or deactivate the claim certificate in the provisioning service, rotate to a new claim certificate for new manufacturing batches, and audit the provisioning logs for unauthorized device enrollments.
- C) The impact is limited to new, unprovisioned devices in the supply chain. The 500,000 already-provisioned devices are unaffected because they use their permanent unique certificates after provisioning is complete. No immediate action is required for the deployed fleet.
- D) The impact is that all 500,000 devices must be re-provisioned because the claim certificate compromise invalidates all certificates issued during that provisioning session. Remediation requires a field technician visit to each site.
- **Correct Answer:** B) Critical impact — unlimited unauthorized enrollment possible; revoke claim certificate immediately.
- **Distractor Analysis:**
  - *Why A is incorrect:* While the claim certificate's access is limited to provisioning operations, "limited to provisioning" means the attacker can enroll unlimited counterfeit devices and receive valid production certificates for each of them. Those production certificates then have full operational access to the MQTT broker and cloud backend. The limitation to provisioning endpoints does not limit the downstream damage.
  - *Why B is correct:* An active, unrevoked claim certificate is a standing invitation for unauthorized enrollment. Any device — including counterfeit hardware — that presents this certificate to the provisioning service will receive valid production credentials. Revocation stops new enrollments. Auditing provisioning logs identifies whether unauthorized enrollments have already occurred. The deployed fleet is not directly compromised, but the provisioning channel is.
  - *Why C is incorrect:* The answer correctly identifies that already-provisioned devices are not directly affected. However, the claim that "no immediate action is required" is incorrect — the provisioning channel is actively exploitable for as long as the claim certificate remains valid. New unauthorized devices can enroll continuously until revocation occurs.
  - *Why D is incorrect:* The already-provisioned devices' permanent unique certificates are independent of the claim certificate. Their certificates were issued by the CA and are valid; the claim certificate compromise does not retroactively invalidate them. Re-provisioning 500,000 devices is not required.

---

### Question 2

A device twin's desired state contains `{"firmware_target": "v2.1.0", "reporting_interval_s": 15}`. The device's reported state contains `{"firmware_version": "v2.0.3", "reporting_interval_s": 15, "uptime_s": 86400}`. What is the delta, and what action should the device take when it receives it?

- A) The delta is `{"reporting_interval_s": 15}` because that field appears in both desired and reported state. The device should reapply the reporting interval setting.
- B) The delta is `{"firmware_target": "v2.1.0"}` because that is the only field where the desired value differs from (or is absent in) the reported state. The device should initiate an OTA firmware update to version v2.1.0.
- C) The delta is the entire desired state document `{"firmware_target": "v2.1.0", "reporting_interval_s": 15}` because the device must acknowledge all desired fields regardless of synchronization status.
- D) The delta is empty because the device has confirmed the reporting interval is correctly set, and firmware version tracking is handled by the OTA service separately from the shadow system.
- **Correct Answer:** B) Delta is `{"firmware_target": "v2.1.0"}` — the only field with a desired/reported mismatch.
- **Distractor Analysis:**
  - *Why A is incorrect:* The reporting interval is already synchronized — desired is 15 and reported is 15. Fields that match are not included in the delta. The delta contains only mismatches between desired and reported state.
  - *Why B is correct:* The delta is computed as the set of desired fields where the desired value does not match the corresponding reported value. `firmware_target` is "v2.1.0" in desired and absent (or "v2.0.3" in the `firmware_version` field) in reported — this is a mismatch. `reporting_interval_s` is 15 in both — no mismatch. The device receives the delta `{"firmware_target": "v2.1.0"}` and should begin the OTA update process.
  - *Why C is incorrect:* Sending the entire desired state as the delta regardless of synchronization would cause the device to redundantly reapply already-correct settings on every connection. The delta is specifically the unsynchronized subset to minimize unnecessary device actions.
  - *Why D is incorrect:* The shadow system is the standard mechanism for OTA job coordination in cloud IoT platforms. AWS IoT Jobs, Azure IoT Hub jobs, and similar systems use the device twin/shadow to communicate the firmware target version. The OTA service does not operate independently of the shadow — it uses the shadow as the coordination mechanism.

---

### Question 3

An ESP32 device in the field is running firmware v2.0.0. An OTA job delivers firmware v2.1.0. The device downloads and verifies the firmware, calls `esp_ota_set_boot_partition()`, and reboots. The new firmware starts, runs for 10 seconds, then crashes due to a null pointer dereference bug. The device reboots again. What happens next, and why?

- A) The device reboots into firmware v2.1.0 again, crashes again after 10 seconds, and enters a reboot loop until a corrected firmware version is pushed via OTA.
- B) The device's ROM bootloader detects that the new partition was never committed with `esp_ota_mark_app_valid_cancel_rollback()`, marks the new partition as invalid, and boots the previous firmware v2.0.0 — restoring the device to a known-good state automatically.
- C) The device boots into a factory reset partition and begins the provisioning process again, because the OTA failure triggered a security exception in the bootloader.
- D) The device remains in a boot loop until a field technician connects via USB and manually resets the OTA state register using the `esptool.py` utility.
- **Correct Answer:** B) Bootloader detects uncommitted partition and rolls back to v2.0.0 automatically.
- **Distractor Analysis:**
  - *Why A is incorrect:* This describes the behavior without automatic rollback — a scenario where the device would indeed be bricked in a crash loop. The A/B partition scheme with commit confirmation exists specifically to prevent this scenario. The bootloader is designed to detect an uncommitted partition and never boot it twice.
  - *Why B is correct:* The ESP-IDF OTA implementation uses a boot state register to track whether the new partition has been successfully confirmed. When `esp_ota_set_boot_partition()` is called, the partition is marked as "pending verification." The device must call `esp_ota_mark_app_valid_cancel_rollback()` within the new firmware to mark the partition as confirmed. If the device reboots before this call — due to a crash — the bootloader detects the unconfirmed partition state and boots the previous partition instead. The device comes back online running v2.0.0, reconnects to the management platform, and can receive a corrected firmware update.
  - *Why C is incorrect:* OTA failures do not trigger factory reset or re-provisioning. The factory reset partition is a separate feature used for manual user-initiated recovery, not for automatic OTA rollback.
  - *Why D is incorrect:* The A/B partition rollback is fully automatic — no human intervention is required. This is the critical advantage of the dual-partition scheme: remote recovery without physical access.

---

### Question 4

A fleet of 200,000 IoT devices is running firmware v1.9.2. The engineering team releases v2.0.0, which includes a significant refactor of the network stack. The team debates whether to deploy to all 200,000 devices simultaneously over a weekend or use a staged rollout. Which argument most accurately represents the case for staged rollout?

- A) A staged rollout is legally required under FCC IoT device regulations, which mandate that firmware updates affecting radio behavior be tested in production deployments of no more than 1% of devices before general availability.
- B) A simultaneous deployment to 200,000 devices means that any defect in v2.0.0 — including defects that passed all QA tests but appear only in production hardware at scale — will affect all 200,000 devices simultaneously. A staged rollout with a 0.1% canary group limits the impact of a defective release to 200 devices and provides 24–48 hours of production signal before the wider deployment.
- C) A staged rollout is preferable because the OTA infrastructure cannot handle 200,000 simultaneous download requests, and the canary group limits peak bandwidth to 0.1% of the theoretical maximum.
- D) A staged rollout provides no meaningful risk reduction because QA testing already validates the firmware on representative hardware, and any defect that appears in production would have been caught during testing.
- **Correct Answer:** B) Staged rollout limits blast radius and provides production signal before wide deployment.
- **Distractor Analysis:**
  - *Why A is incorrect:* No FCC regulation mandates staged rollouts with specific percentage limits for IoT firmware updates. The staged rollout is an engineering best practice, not a regulatory requirement.
  - *Why B is correct:* QA testing can never replicate the full diversity of production conditions: hardware variation across manufacturing lots, extreme temperature environments, unusual network conditions, unusual usage patterns, and interactions with other devices on the same local network. The canary stage provides production signal with real devices in real deployments. A 200-device failure is recoverable; a 200,000-device simultaneous failure may constitute an outage of existential severity for the business.
  - *Why C is incorrect:* While OTA infrastructure scaling is a legitimate operational consideration, it is not the primary risk-reduction argument for staged rollouts. Modern cloud OTA platforms are designed to handle large fleet deployments. The primary argument is defect containment, not bandwidth management.
  - *Why D is incorrect:* This argument represents a common and dangerous misunderstanding of QA testing. QA validates specific test cases on specific hardware in controlled environments. Production deployments expose firmware to: hardware units with marginal components that passed production testing, unusual input sequences, concurrent failure scenarios, and environmental conditions that are difficult or impossible to replicate in a test lab. The history of software engineering is full of bugs that passed QA and failed in production.

---

### Question 5

A company's IoT fleet monitoring system generates 847 alerts in a single day. An operations engineer investigates and finds that 841 of the 847 alerts are for "message rate below threshold" triggered by devices that are reporting at 28 messages/minute instead of the expected 30 messages/minute — a 6.7% deviation caused by minor clock drift. Six of the alerts are for devices that are genuinely offline. What does this situation represent, and what is the correct fix?

- A) This represents appropriate monitoring sensitivity — catching 6 genuine offline devices out of 847 alerts is an acceptable signal-to-noise ratio, and the alert threshold should not be changed.
- B) This represents alert fatigue caused by an incorrectly calibrated threshold. The fix is to recalibrate the "message rate below threshold" alert to trigger only when the rate falls below a value that represents a meaningful deviation from normal (e.g., below 50% of expected rate), which would silence the clock drift false positives while retaining alerts for genuinely offline devices.
- C) This represents a critical fleet-wide network issue — 841 devices simultaneously below their expected rate indicates a systemic network degradation that must be investigated immediately.
- D) This represents a firmware bug in the clock implementation that must be fixed via OTA update before the alerting threshold is adjusted.
- **Correct Answer:** B) Alert fatigue from poorly calibrated threshold; recalibrate to distinguish noise from real failures.
- **Distractor Analysis:**
  - *Why A is incorrect:* A 1-in-141 signal-to-noise ratio (6 real alerts out of 847) is the definition of an unacceptable alert threshold. In practice, engineers who receive 847 alerts per day will learn to dismiss them without reading them — including the 6 genuine offline device alerts. The monitoring system has failed its core purpose.
  - *Why B is correct:* A 6.7% rate deviation from minor clock drift is environmental noise, not a device health signal. An alert threshold of "below 50% of expected rate" would require the device to be reporting at fewer than 15 messages/minute — well below the 28 observed during normal clock-drift operation — to trigger an alert. This threshold would catch genuinely offline devices (0 messages/minute) while ignoring the clock drift false positives.
  - *Why C is incorrect:* 841 devices reporting at 28/30 messages per minute (93% of expected rate) is not a network degradation signal. If the network were degraded, you would expect to see reconnect events, TLS failures, and message delays — not a uniform 6.7% reduction in rate across all devices. The uniform reduction is characteristic of systematic clock drift.
  - *Why D is incorrect:* Minor clock drift is normal behavior in embedded systems. Microcontroller oscillators have manufacturing tolerances (typically ±1–2%) that cause clocks to run slightly fast or slow. This is expected behavior, not a firmware bug. Deploying an OTA update to fix clock drift that is within specification would be wasteful and introduce OTA update risk.

---

### Question 6

An IoT company operates a fleet of 50,000 industrial sensors that report temperature readings every 5 seconds. Each reading is 64 bytes of JSON. After 90 days, the raw data retention policy expires and readings are downsampled to 1-minute averages. What is the daily raw data volume, and why is a time-series database preferred over a relational database for this workload?

- A) Daily raw data volume: 50,000 devices × 17,280 readings/day × 64 bytes = approximately 55 GB/day. A relational database is preferred because its ACID transaction guarantees ensure no data loss during high-throughput writes.
- B) Daily raw data volume: 50,000 devices × 17,280 readings/day × 64 bytes = approximately 55 GB/day. A time-series database is preferred because it provides column-oriented storage (compresses repetitive time-series values efficiently), automatic downsampling (computes 1-minute averages and deletes raw data per policy without manual ETL jobs), and high-cardinality tag indexing (queries across 50,000 device IDs efficiently).
- C) Daily raw data volume: 50,000 devices × 720 readings/day × 64 bytes = approximately 2.3 GB/day (one reading per minute). A time-series database is preferred because it encrypts data at rest by default, which relational databases do not.
- D) Daily raw data volume: 50,000 devices × 17,280 readings/day × 64 bytes = approximately 55 GB/day. A relational database is preferred because time-series databases do not support SQL queries, making operational analysis impossible without custom tooling.
- **Correct Answer:** B) 55 GB/day; TSDB preferred for column storage, auto-downsampling, and high-cardinality indexing.
- **Distractor Analysis:**
  - *Why A is incorrect:* The data volume calculation is correct (50,000 × 86,400/5 × 64 ≈ 55 GB). However, ACID transaction guarantees are not the primary reason to prefer or avoid either database type for IoT telemetry. IoT write workloads are mostly append-only and tolerate occasional write failures — ACID overhead is an unnecessary cost for this use case.
  - *Why B is correct:* Calculation: 86,400 seconds/day ÷ 5 seconds/reading = 17,280 readings/device/day. 50,000 × 17,280 × 64 = approximately 55 GB/day. TSDBs address the three specific challenges of IoT workloads: (1) compressed column storage handles the high volume efficiently; (2) native downsampling handles the 90-day retention policy without manual ETL pipelines; (3) high-cardinality tag indexing handles 50,000 unique device IDs without the index bloat that breaks relational databases.
  - *Why C is incorrect:* The calculation is wrong — devices report every 5 seconds, not every minute, yielding 17,280 readings/day, not 720. Encryption at rest is also not a distinguishing feature of TSDBs vs. relational databases — both support encryption at rest.
  - *Why D is incorrect:* Many TSDBs do support SQL-like query languages. InfluxDB has its own InfluxQL and Flux query languages. TimescaleDB is a PostgreSQL extension and supports full SQL. AWS Timestream supports a SQL-like query syntax. The claim that TSDBs do not support SQL is incorrect.

---

### Question 7

During a decommissioning audit, a security team discovers that 300 retired IoT devices were removed from the device registry and had their certificates revoked, but the devices were sold to a recycler without cryptographic erasure of their flash memory. What residual security risk exists, and what should the team do?

- A) No residual risk exists — certificate revocation is sufficient. Even if an attacker extracts the certificates from the devices, the CRL check in the MQTT broker will reject any connection attempt from a revoked certificate.
- B) Residual risk: an attacker who physically acquires the devices and extracts flash contents may obtain private keys, Wi-Fi credentials, cloud endpoint addresses, and operational data. The private key extraction risk is mitigated by the certificate revocation, but the Wi-Fi credentials and other configuration data remain exploitable. The team should contact the recycler to locate and cryptographically erase or physically destroy the devices before they are resold or scrapped.
- C) Residual risk: the devices' private keys, if extracted, could be used to create fraudulent certificates because the CA root key is stored on each device in flash. The team must rotate the CA root key for the entire fleet.
- D) Residual risk: the devices may reconnect to the Wi-Fi network using stored credentials and attempt to contact the MQTT broker. Since their certificates are revoked, the connection will fail, but the attempted connections will consume broker resources. The team should change the Wi-Fi password to prevent device reconnections.
- **Correct Answer:** B) Private key extraction is mitigated by CRL, but Wi-Fi credentials and config data remain at risk; locate and erase devices.
- **Distractor Analysis:**
  - *Why A is incorrect:* Certificate revocation prevents the extracted certificate from authenticating to the MQTT broker, which is correct. However, the flash may also contain Wi-Fi SSID and password (allowing network access), cloud endpoint URLs (useful for reconnaissance), operational telemetry data (potentially sensitive), and device configuration secrets. These do not require authentication to be misused.
  - *Why B is correct:* This accurately identifies the layered risk. The CRL handles the certificate-based authentication risk. But flash memory typically contains additional sensitive data beyond the certificate: Wi-Fi credentials allow the attacker to access the customer's network; endpoint URLs and API keys may enable attacks on adjacent systems; operational data may be subject to data protection regulations. The appropriate response is to locate the devices and ensure they are securely erased.
  - *Why C is incorrect:* Device certificates are signed by the CA, but the CA private key is not stored on individual devices — it is held on the signing server (ideally an HSM). Individual device private keys cannot be used to forge other devices' certificates or compromise the CA.
  - *Why D is incorrect:* Devices with flat batteries or decommissioned firmware are unlikely to spontaneously reconnect, and a TLS handshake failure consumes negligible broker resources. Changing the Wi-Fi password addresses reconnection attempts but does not address the primary risk of flash data extraction.

---

### Question 8

A product team is designing the OTA update architecture for a new ESP32-based smart thermostat. The firmware update package is 1.8 MB. Devices connect over residential Wi-Fi. The team is choosing between two download approaches: (A) a single HTTP GET request that downloads the entire 1.8 MB in one transaction, and (B) a chunked download using HTTP Range requests that downloads the firmware in 64 KB segments, saves each segment to flash, and resumes from the last saved position after any interruption. Which approach is correct for production IoT deployment and why?

- A) Approach A is preferred because a single HTTP GET is simpler to implement and modern Wi-Fi is reliable enough that connection drops during a 1.8 MB download are extremely rare in residential environments.
- B) Approach B is correct because residential Wi-Fi connections can drop at any time during a multi-minute download. Without resume capability, a connection drop at 99% completion causes the entire download to restart from byte 0. With 100,000 deployed devices across diverse Wi-Fi environments, some devices will always experience interruptions, and Approach A creates a class of devices permanently stuck in an OTA retry loop.
- C) Approach A is preferred because flash wear leveling on the ESP32 is optimized for full-page writes, and chunked writes that write 64 KB at a time will cause uneven wear and shorten the flash lifetime.
- D) Approach B is required because the ESP32 cannot allocate 1.8 MB of SRAM to buffer the complete firmware download before flashing, so chunked flashing is the only technically feasible approach.
- **Correct Answer:** B) Chunked resumable download is required for reliable production OTA at scale.
- **Distractor Analysis:**
  - *Why A is incorrect:* "Modern Wi-Fi is reliable enough" is not an acceptable reliability argument for production at fleet scale. At 100,000 devices across diverse residential environments (basement devices, devices near microwave ovens, devices with marginal signal strength), even a 1% connection failure rate during a 1.8 MB download represents 1,000 devices stuck in retry loops. Production OTA must be designed for the worst case in the fleet, not the average case.
  - *Why B is correct:* HTTP Range requests (the `Range: bytes=start-end` header) allow a download to resume from any byte offset after an interruption. By writing each received chunk to the inactive flash partition as it arrives and tracking the last written offset in NVM, the device can resume from exactly where it left off after a reconnection. This makes OTA updates robust to intermittent connectivity and eliminates the retry-loop failure mode. ESP-IDF's `esp_https_ota` component implements this by default.
  - *Why C is incorrect:* Flash wear leveling operates at the page and block level internally — the write granularity from the application perspective does not affect wear leveling behavior significantly. ESP32 flash controllers handle wear leveling transparently. Chunked writes do not cause meaningfully uneven wear compared to a single-transaction write.
  - *Why D is incorrect:* The ESP32 does not buffer the entire firmware in SRAM before flashing in either approach. Both approaches write to the flash partition as data is received. Approach A would flash in a streaming fashion using the HTTP body as a stream; Approach B does the same but saves a resume offset. The SRAM constraint is not the differentiator.

---

### Question 9

An IoT fleet management platform sends an alert when a device's reported firmware version does not match the desired firmware version after 72 hours. Of 10,000 devices in the fleet, 47 devices have been in this state for more than 72 hours. What operational procedure should the fleet manager follow, and what are the two most likely root causes?

- A) The fleet manager should immediately push a force-update job to all 47 devices with a higher retry priority, as the most likely cause is network congestion causing download timeouts.
- B) The fleet manager should investigate the 47 devices individually: query their last-seen timestamps, reconnect rates, and OTA job status. The two most likely root causes are: (1) devices that are intermittently offline and cannot complete the multi-minute download before losing connectivity, and (2) devices with insufficient flash space for the new firmware due to a large filesystem partition consuming the partition table.
- C) The fleet manager should reclassify the 47 devices as decommissioned and initiate certificate revocation, as devices that cannot update firmware within 72 hours are operationally non-functional.
- D) The fleet manager should extend the OTA job timeout from 72 hours to 7 days to allow devices in poor connectivity environments more time to complete the download.
- **Correct Answer:** B) Investigate individually — most likely intermittent connectivity or insufficient flash space.
- **Distractor Analysis:**
  - *Why A is incorrect:* Applying a force-update without diagnosis risks making the problem worse. If the devices have a flash configuration issue, forcing additional OTA attempts will simply fill the retry log without succeeding. Diagnosis must precede remediation.
  - *Why B is correct:* 47 out of 10,000 (0.47%) devices failing to update within 72 hours is a small but meaningful cohort that warrants individual investigation. The two most common root causes are: connectivity issues (devices in basements, rural areas, or with failing Wi-Fi hardware that cannot sustain a connection long enough for the full download) and partition table mismatches (a firmware update that is larger than the OTA partition due to a changed build configuration or a large SPIFFS filesystem partition). Each root cause requires a different remediation.
  - *Why C is incorrect:* An inability to complete a firmware update does not indicate the device is non-functional — it may simply be in a poor network environment. Decommissioning 47 devices and their certificates would eliminate operational devices, not solve the problem.
  - *Why D is incorrect:* Extending the timeout to 7 days may eventually resolve connectivity-related failures but does not diagnose or address the root cause. It also extends the window during which these devices run outdated firmware with potential security vulnerabilities.

---

### Question 10

Which combination of fleet management capabilities, implemented together, provides the strongest protection against the risk that a security vulnerability in deployed firmware could be exploited across the entire fleet before a patch is deployed?

- A) Device registry with firmware version tracking plus a time-series database for telemetry storage — the combination provides visibility into which devices are running vulnerable firmware and historical data for forensic analysis after an incident.
- B) OTA update capability with staged rollout plus real-time monitoring with automated alerting — OTA enables rapid patch delivery; staged rollout limits blast radius if the patch itself has defects; real-time monitoring detects active exploitation before the patch reaches all devices, enabling targeted incident response.
- C) Certificate-based mutual TLS plus device twin synchronization — mTLS prevents unauthorized devices from connecting, and device twins ensure all devices receive the latest security configuration simultaneously.
- D) Zero-touch provisioning plus automatic certificate renewal — zero-touch ensures all new devices receive secure credentials from day one, and automatic renewal prevents certificate expiry from leaving devices with invalid credentials that could be exploited.
- **Correct Answer:** B) OTA with staged rollout plus real-time monitoring and alerting.
- **Distractor Analysis:**
  - *Why A is incorrect:* Registry visibility and telemetry history are valuable for situational awareness and post-incident forensics, but they do not by themselves reduce the exploitation window. You can see which devices are vulnerable and review historical data, but without OTA capability you cannot deploy the patch, and without alerting you cannot detect active exploitation in real time.
  - *Why B is correct:* This combination directly addresses the timeline of a vulnerability exploitation scenario: OTA capability means a patch can be developed and delivered within hours to days of disclosure; staged rollout ensures the patch does not itself create a new fleet-wide outage; real-time monitoring detects anomalous behavior (unexpected outbound connections, unusual MQTT topic access patterns, elevated error rates) that may indicate active exploitation in the window before the patch reaches all devices. The combination reduces both the exploitation window and the impact of an ongoing attack.
  - *Why C is incorrect:* mTLS and device twin synchronization are important security controls, but they do not reduce the vulnerability exploitation risk. A vulnerability in the firmware itself can be exploited by any device that can connect — including legitimately authenticated devices. mTLS prevents unauthorized devices; it does not prevent authorized devices from being exploited through firmware bugs.
  - *Why D is incorrect:* Zero-touch provisioning and certificate renewal are provisioning-phase and credential-lifecycle controls. They ensure devices have valid credentials but do not address the risk of firmware vulnerabilities in deployed devices. A device with a perfectly valid, recently renewed certificate is equally exploitable if its firmware contains a critical vulnerability.

---

### Question 11

A company's fleet management query returns 12 devices with `shadow.reported.firmware_version < 'v2.3.0'` and `connectivity.connected = false` after a mandatory security patch campaign. The other 9,988 devices have been successfully updated. What is the most appropriate next action, and why is revoking these 12 devices' certificates not the correct first step?

- A) The 12 devices should have their certificates revoked immediately because running outdated firmware with a known security vulnerability is equivalent to a compromised device and poses an ongoing threat to the fleet.
- B) The fleet manager should investigate each of the 12 devices individually — query their last-seen timestamps, connection history, and installation site — before taking action. Certificate revocation is not the correct first step because these devices are offline and running outdated firmware, which may simply indicate connectivity problems, dead batteries, or powered-off installations rather than compromise or abandonment.
- C) The 12 devices should be marked as permanently decommissioned in the registry because devices that fail to receive a mandatory update within the campaign window are operationally non-functional.
- D) The 12 devices should receive a force-update job at the highest priority. If they do not update within 24 hours, their certificates should be revoked as a precautionary measure.
- **Correct Answer:** B) Investigate individually; offline + outdated does not imply compromise or abandonment.
- **Distractor Analysis:**
  - *Why A is incorrect:* Offline devices running outdated firmware are a risk to be remediated, but revoking their certificates immediately eliminates the ability to update them remotely when they reconnect. The correct sequence is: investigate → attempt update → revoke only if the device is confirmed abandoned, lost, or compromised. Premature revocation converts a recoverable situation into a field service call.
  - *Why B is correct:* The fleet indexing query identifies a candidate set for investigation, not a list of compromised devices. Many legitimate reasons explain this state: the device installation is in a vacation property that was powered off for the winter; the device has a failed Wi-Fi module; the device is in a low-signal area and connects only once per week. Investigation using last-seen timestamps, connection history, and contact with the installation site owner disambiguates these scenarios before taking irreversible action.
  - *Why C is incorrect:* "Failed to receive a mandatory update" is a connectivity or access problem, not an operational failure. The device hardware and firmware may be functioning normally — it is simply unreachable. Decommissioning 12 operational devices would require field replacement at significant cost.
  - *Why D is incorrect:* A force-update job is appropriate once connectivity is confirmed. However, the 24-hour revocation deadline is arbitrary and may not align with the device's natural reconnect cycle. Investigation should determine the cause of the missed update before setting deadlines.

---

### Question 12

A fleet of smart thermostats reports telemetry every 60 seconds including `free_heap_bytes`. Over 30 days, the median free heap across 10,000 devices decreases from 85,000 bytes at deployment to 61,000 bytes — a 28% reduction. The minimum observed free heap on any device is 22,000 bytes. What does this trend most likely indicate, and what is the appropriate response?

- A) The free heap decrease is expected — FreeRTOS heap usage naturally increases as connected buffers fill with received MQTT messages over time. The fleet is operating normally.
- B) A 28% heap decrease over 30 days is a fleet-wide memory leak indicator. This trend suggests a slow memory leak in the firmware — likely in a library that allocates memory during each network operation or sensor read without corresponding frees. The response is to investigate the firmware for missing `free()` calls in TLS session handling, MQTT packet processing, or ArduinoJson allocations, then push a corrected firmware via OTA before any device's free heap drops to critical levels (typically <20,000 bytes for ESP32).
- C) The free heap decrease is caused by the device registry accumulating shadow delta messages in MQTT receive buffers. The fix is to increase the MQTT client's receive buffer size on the thermostat.
- D) A 28% decrease over 30 days is within normal variance; alert thresholds should only be set for single-reading spikes, not for gradual trends.
- **Correct Answer:** B) Fleet-wide memory leak; investigate firmware allocations and push corrected OTA.
- **Distractor Analysis:**
  - *Why A is incorrect:* FreeRTOS heap usage does not naturally increase indefinitely under normal operation. A well-written embedded application has a stable steady-state heap footprint after initialization. A monotonically decreasing free heap over 30 days is the defining symptom of a memory leak, not normal behavior.
  - *Why B is correct:* A steady 28% decrease over 30 days extrapolates to 0% free heap (device crash) in approximately 107 days from deployment. The minimum device at 22,000 bytes may crash within days. Common sources of slow memory leaks on ESP32 with MQTT include: not calling `mqtt.loop()` frequently enough (causing receive buffer buildup), creating `ArduinoJson::DynamicJsonDocument` objects on every reading without freeing them, or SSL session state accumulating in heap. The response requires firmware investigation, fix, and OTA deployment before the affected devices crash.
  - *Why C is incorrect:* MQTT receive buffers in PubSubClient are statically sized in the client configuration — they do not grow unboundedly with received messages. Shadow delta messages are processed and discarded in the `on_message` callback; they do not accumulate in the client's heap beyond the static buffer.
  - *Why D is incorrect:* Gradual trends in health metrics are often more operationally important than single-reading spikes. A spike may be a transient anomaly; a 30-day linear decrease is a systematic problem with a predictable failure point. Fleet monitoring systems should implement trend detection (e.g., linear regression on a rolling 7-day window) in addition to threshold checks.

---

### Question 13

A device manufacturer implements JITP (Just-In-Time Provisioning). On first boot, each device connects to the provisioning endpoint using a shared claim certificate, registers itself, and receives a unique device certificate and private key in the provisioning response. The provisioning service stores the newly issued private key in its database for audit purposes. What is the security flaw in this design, and how should it be corrected?

- A) The flaw is that the claim certificate is shared across all devices, allowing any device to observe another device's provisioning exchange. The fix is to generate a unique claim certificate per device before shipment.
- B) The flaw is that the provisioning service is storing the device's private key — a key that should exist only on the device and never be transmitted or stored anywhere else. If the provisioning service's database is breached, all device private keys are compromised. The correct design is for the device to generate its own key pair on-device, send only the public key (or a CSR) to the provisioning service, and receive back a CA-signed certificate — the private key never leaves the device.
- C) The flaw is that the private key is transmitted over the provisioning connection, which is secured by the claim certificate TLS connection. The fix is to use DTLS instead of TLS for the provisioning connection to add an additional encryption layer.
- D) The flaw is that the provisioning service issues the same private key to every device for simplicity. The audit database correctly stores this shared key for recovery purposes.
- **Correct Answer:** B) Storing the device private key server-side is a fundamental security violation; keys must be generated on-device.
- **Distractor Analysis:**
  - *Why A is incorrect:* While unique claim certificates per device are a stronger design than a shared claim certificate, this is not the primary security flaw described. The shared claim certificate allows enrollment of the current device and grants no access to other devices' provisioning sessions (each session is independent). The server-side storage of private keys is the critical flaw.
  - *Why B is correct:* The device private key is the root of that device's security. If it is stored anywhere outside the device — even in an "audit database" — it can be exfiltrated in a server-side breach, granting an attacker permanent impersonation capability for every device whose key was stored. The correct PKI pattern is: the device generates the key pair internally (using the ESP32's hardware RNG), signs a Certificate Signing Request (CSR) with the private key, and submits only the CSR (which contains the public key) to the provisioning service. The provisioning service signs the CSR and returns the certificate. The private key never leaves the device.
  - *Why C is incorrect:* The provisioning connection's transport encryption (TLS) does not address the root problem. Whether the key is transmitted over TLS or DTLS, the server still receives and stores the private key — the fundamental violation is that the key exists outside the device, not that the transmission channel is insufficiently encrypted.
  - *Why D is incorrect:* This describes the exact same flaw as the scenario (stored private key) with an incorrect rationalization. A shared private key across devices means a single extraction compromises all devices — this is never an acceptable design.

---

### Question 14

An IoT fleet health dashboard shows that a specific device has rebooted 47 times in the past 24 hours. The device's firmware version is current (v3.2.1), and the device connects to MQTT successfully after each reboot. Telemetry includes free heap, CPU temperature, and uptime. Which combination of telemetry fields would most help diagnose the cause of the repeated reboots?

- A) Free heap at time of reboot (compare to steady-state) and the OTA partition's firmware signature verification status — repeated reboots often indicate a corrupted OTA partition that passes signature verification but crashes on startup.
- B) Uptime at each reboot (determines whether the device reboots at a consistent time interval, suggesting a scheduled task or timer overflow), free heap trend before reboot (checks for memory exhaustion as a crash trigger), and the exception/fault type from the panic handler output (identifies whether it is a null pointer, stack overflow, or watchdog timeout).
- C) CPU temperature before each reboot (thermal throttling may cause watchdog timeouts) and the Wi-Fi RSSI at the time of last message before reboot (poor connectivity may cause TLS handshake timeouts that trigger a software reset).
- D) Shadow delta synchronization timestamp (devices that receive a configuration change and reboot to apply it would explain the 47 reboots if the delta was published repeatedly) and the device's MQTT keep-alive timeout setting.
- **Correct Answer:** B) Uptime per reboot, heap trend, and panic handler output together provide the most complete diagnostic picture.
- **Distractor Analysis:**
  - *Why A is incorrect:* A corrupted OTA partition causing crashes would prevent the device from connecting to MQTT after each reboot — but the scenario states the device connects successfully after each reboot. This rules out OTA partition corruption as the primary cause.
  - *Why B is correct:* The three-field combination covers the three most common causes of repeated reboots: (1) a consistent uptime interval before reboot (e.g., always crashes at 1,800 seconds) suggests a timer overflow, task watchdog expiry, or periodic task that triggers a fault; (2) declining free heap before reboots confirms memory exhaustion as the trigger; (3) the panic handler fault type from the serial output or crash log (if captured) is the most definitive diagnostic — it identifies the exact failure mode (null pointer dereference, stack canary violation, watchdog timeout, etc.).
  - *Why C is incorrect:* CPU temperature and RSSI are valid secondary diagnostics but less likely to explain 47 reboots in 24 hours. Thermal throttling-induced watchdog timeouts would typically show a gradual warm-up pattern. RSSI-related TLS failures would appear as failed connection attempts, not successful connections after each reboot.
  - *Why D is incorrect:* Shadow delta-triggered reboots would appear in the shadow synchronization log as a received delta, and the firmware would not need to reboot to apply a configuration change (changes like `reporting_interval_s` are applied at runtime). 47 identical delta publications that each trigger a reboot would be visible in the fleet server logs.

---

### Question 15

A JITP provisioning template includes the following policy that is attached to each newly provisioned device. A security reviewer flags this policy as overly permissive. Identify the specific permission that makes this policy dangerous and explain the correct scope restriction.

```json
{
  "Effect": "Allow",
  "Action": ["iot:Connect", "iot:Publish", "iot:Subscribe", "iot:Receive"],
  "Resource": "arn:aws:iot:us-east-1:123456789:*"
}
```

- A) The `iot:Subscribe` permission is the dangerous permission — devices should only be allowed to publish, not subscribe. Subscribing allows a device to receive messages intended for other devices.
- B) The wildcard `*` in the Resource ARN allows each provisioned device to connect as any client ID, publish to any MQTT topic, subscribe to any topic filter, and receive messages on any topic. A compromised device can publish to other devices' shadow topics, subscribe to all telemetry topics, and impersonate any other device. The fix is to scope the resource to the device's own client ID using the `${iot:ClientId}` policy variable.
- C) The `iot:Connect` permission should be removed — devices do not need explicit Connect permission because it is granted by default when a certificate is attached to a policy.
- D) The dangerous permission is `iot:Publish` on the wildcard resource, because it allows devices to publish to the `$aws/provisioning-templates/` topics and trigger additional provisioning enrollments for counterfeit devices.
- **Correct Answer:** B) The wildcard Resource ARN allows cross-device access; use `${iot:ClientId}` to scope each permission to the device's own namespace.
- **Distractor Analysis:**
  - *Why A is incorrect:* Subscribing is a necessary capability for devices that need to receive OTA job notifications, shadow deltas, and cloud-to-device commands. Removing subscribe would break the device's ability to receive configuration updates. The problem is not the action type but the scope of the resource ARN.
  - *Why B is correct:* The wildcard Resource ARN means the policy is equivalent to: "this device can do anything with any IoT resource in this account." The correct pattern uses `${iot:ClientId}` which resolves to the connecting device's MQTT client ID at policy evaluation time. For example: `arn:aws:iot:us-east-1:123:topic/devices/${iot:ClientId}/*` restricts the device to only publish and subscribe to topics under its own namespace. This ensures a compromised device cannot affect other devices' telemetry, shadows, or command topics.
  - *Why C is incorrect:* `iot:Connect` is not granted by default — it must be explicitly permitted in the policy. Without `iot:Connect` on the matching client resource, the device cannot establish an MQTT connection even if its certificate is valid. The connection permission is separate from message-level permissions.
  - *Why D is incorrect:* While publishing to provisioning template topics is a concern, AWS IoT Core's provisioning API endpoints use a separate permission (`iot:CreateKeysAndCertificate`, `iot:RegisterThing`) that is not covered by `iot:Publish`. A device with only `iot:Publish` cannot trigger provisioning enrollments for other devices.

---

### Question 16

An IoT device completes an OTA update, reboots, and runs for 45 seconds. The firmware then calls `esp_ota_mark_app_valid_cancel_rollback()`. One minute later, the device crashes due to an unrelated application bug (a null pointer in a data processing task). What happens next, and why?

- A) The bootloader rolls back to the previous firmware because the device crashed within the first 5 minutes after an OTA update, which triggers the rollback timer.
- B) The bootloader boots the new firmware again (v2.1.0) because `esp_ota_mark_app_valid_cancel_rollback()` was called before the crash — the OTA partition was committed. The crash is treated as a normal application crash, not an OTA failure. Rollback does not occur.
- C) The bootloader enters factory reset mode because two consecutive crashes (boot + application crash) within a short time window trigger the ESP-IDF recovery mechanism.
- D) The bootloader rolls back to the previous firmware because the total uptime before crash (approximately 105 seconds) is below the ESP-IDF rollback timer default of 300 seconds.
- **Correct Answer:** B) Committed OTA is permanent; the device reboots into the same new firmware; no rollback occurs.
- **Distractor Analysis:**
  - *Why A is incorrect:* There is no ESP-IDF "rollback timer" that automatically triggers rollback based on uptime after an OTA update. The rollback decision is binary and based solely on whether `esp_ota_mark_app_valid_cancel_rollback()` was called — not on how long the firmware ran.
  - *Why B is correct:* Once `esp_ota_mark_app_valid_cancel_rollback()` is called, the new partition's OTA state is set to `ESP_OTA_IMG_VALID`. The bootloader will boot this partition on every subsequent boot regardless of crashes. The rollback mechanism only fires when the OTA state is still `ESP_OTA_IMG_PENDING_VERIFY` (not yet committed). After commitment, the firmware behaves like any non-OTA firmware — it crashes and reboots into the same partition. The null pointer crash is an application bug to be fixed via a subsequent OTA update.
  - *Why C is incorrect:* ESP-IDF has no "two consecutive crashes" factory reset mechanism in the standard OTA system. Factory reset functionality (if implemented) is application-defined, not automatically triggered by crash count.
  - *Why D is incorrect:* No 300-second rollback timer exists in the ESP-IDF OTA API. The concept of a "rollback timer" appears in some RTOS designs for self-test periods, but ESP-IDF's OTA rollback is event-driven (commit call) not time-driven.

---

### Question 17

An IoT operations team sets up a Grafana dashboard connected to InfluxDB storing device telemetry. They create a panel showing "Devices not seen in the last 15 minutes." At 2:00 AM on a Saturday, the panel shows 847 devices as offline. At 2:15 AM, all 847 come back online simultaneously. What is the most likely explanation, and what monitoring improvement would detect the root cause earlier?

- A) 847 devices simultaneously went offline because of a coordinated attack — the simultaneous offline event is suspicious and should be treated as a security incident immediately.
- B) A network infrastructure event (ISP outage, cloud broker restart, or gateway maintenance) caused a mass disconnection. All devices reconnected when the infrastructure recovered. The monitoring improvement is to add broker-side telemetry: MQTT broker connection count over time, TLS handshake failure rates, and broker error logs — these would show the infrastructure event before device-level metrics begin to populate.
- C) The InfluxDB ingestion pipeline experienced a 15-minute write lag, causing the dashboard to show stale data. The 847 devices never actually disconnected. The improvement is to add an InfluxDB write latency monitor.
- D) 847 devices simultaneously exceeded their memory limit and crashed, rebooted, and reconnected. This indicates a firmware bug affecting that firmware version. The improvement is to set a heap memory alert threshold.
- **Correct Answer:** B) Infrastructure outage causing mass disconnection; improve monitoring with broker-side connectivity metrics.
- **Distractor Analysis:**
  - *Why A is incorrect:* While a simultaneous mass disconnection is suspicious, the most likely explanation for 847 devices going offline and then all reconnecting is a shared infrastructure dependency (broker, network, DNS) rather than a coordinated attack. An attack would be more likely to show progressive disconnections rather than instant simultaneous disconnect-and-reconnect. The simultaneous reconnection is particularly characteristic of a broker restart — all devices experience the connection drop at the same moment and reconnect with their configured retry intervals.
  - *Why B is correct:* Mass simultaneous device disconnection followed by mass simultaneous reconnection is the signature of a transient infrastructure failure, not a device-level problem. Monitoring the broker's connection count time series would show a vertical drop at 2:00 AM and recovery at 2:15 AM — much faster and clearer than waiting for device-level "not seen" dashboards to populate. Adding TLS handshake failure rate monitoring and broker restart event logging provides the root cause context.
  - *Why C is incorrect:* An InfluxDB write lag of 15 minutes would affect all devices uniformly, not just 847 specific ones. If the lag cleared at 2:15 AM, you would see all devices' data suddenly become current simultaneously — which might match the described pattern — but write lag that long is unusual and would be detectable via InfluxDB's own metrics.
  - *Why D is incorrect:* 847 devices crashing simultaneously from memory exhaustion would require all 847 devices to be running identical firmware, have identical memory usage patterns, and reach exhaustion at the same moment. This is statistically implausible compared to the infrastructure-failure explanation.

---

### Question 18

A device's last OTA update attempt failed at 73% completion (the device lost Wi-Fi connectivity mid-download). The device reconnects 4 hours later. Which ESP-IDF OTA behavior correctly describes what happens, and which API function enables this behavior?

- A) The device starts the download from byte 0 because the ESP-IDF OTA API does not support resumable downloads — partial downloads are discarded when the HTTPS connection drops.
- B) The device resumes the download from the last committed byte (73% completion) because `esp_https_ota()` uses HTTP Range requests to resume from the last flash write position, tracked via the OTA partition's write pointer stored in NVM. The relevant API is `esp_https_ota_perform()` within the `esp_https_ota_begin()` / `esp_https_ota_finish()` context, which supports incremental chunk downloads.
- C) The device cannot resume and must wait for the fleet management platform to push a new OTA job, because the original job's download URL expires after 1 hour.
- D) The device resumes from byte 0 but uses a background download priority that does not affect normal device operation, completing the remaining 100% download over 4 hours to minimize bandwidth impact.
- **Correct Answer:** B) ESP-IDF OTA resumes from the last write position using HTTP Range requests; `esp_https_ota_perform()` handles incremental chunk writes.
- **Distractor Analysis:**
  - *Why A is incorrect:* ESP-IDF's advanced OTA API (`esp_https_ota_begin()` + `esp_https_ota_perform()` + `esp_https_ota_finish()`) explicitly supports resumable downloads. The `esp_ota_begin()` function can be called with an offset parameter, and the HTTP client can send a Range header to continue from an intermediate position. The simplest `esp_https_ota()` convenience function may not support resume, but the full API does.
  - *Why B is correct:* The ESP-IDF OTA API tracks the write position within the inactive partition. On reconnect, the firmware can determine how many bytes were already written (via `esp_ota_get_running_partition()` and the partition state), construct an HTTP Range request (`Range: bytes=N-` where N is the bytes already written), and continue writing from that position. This is the standard production pattern for OTA over unreliable Wi-Fi connections.
  - *Why C is incorrect:* OTA download URL expiry is a server-side policy, not a fixed 1-hour limit. In production deployments, pre-signed S3 URLs or CDN URLs are typically valid for 24 hours or longer. The device reconnecting 4 hours later should find the URL still valid in most deployments.
  - *Why D is incorrect:* ESP-IDF OTA does not have a "background download priority" mode. Downloads happen at the application's requested rate. Restarting from byte 0 after a partial download is the failure mode that resumable downloads were designed to prevent.

---

### Question 19

An IoT company's fleet of 100,000 devices runs on a 3-year certificate lifecycle. The security team sets up automated certificate renewal: certificates expiring within 90 days are automatically renewed by the device using a renewal MQTT topic. A deployment error causes the renewal automation to be disabled for 6 months. When the error is discovered, 2,300 devices have certificates that expire within 7 days. What is the highest-priority remediation action and why?

- A) Immediately revoke the 2,300 expiring certificates and issue new certificates manually, since expired certificates pose a greater security risk than the brief service disruption caused by revocation.
- B) Immediately push an OTA update to all 2,300 devices that triggers the certificate renewal process, prioritizing connectivity continuity — devices that lose their ability to authenticate cannot receive future updates or management commands, effectively bricking them remotely.
- C) Extend the expiry date on all 2,300 certificates by 90 days using the CA's administrative tools, providing time to fix the renewal automation properly without service disruption.
- D) Allow the certificates to expire on schedule and rely on the JITP claim certificate to re-provision each affected device, since all devices should still have their claim certificates stored in firmware.
- **Correct Answer:** B) OTA push to trigger certificate renewal is the highest priority — devices that expire lose all remote management capability.
- **Distractor Analysis:**
  - *Why A is incorrect:* Revoking 2,300 valid certificates would immediately disconnect those devices from the broker and eliminate the ability to push the renewal update to them. Revocation before renewal inverts the correct sequence — it creates the connectivity loss you are trying to prevent. Revocation is appropriate after renewal, not before.
  - *Why B is correct:* A device whose certificate expires can no longer authenticate to the MQTT broker, which means it cannot receive OTA updates, configuration changes, or management commands. It becomes permanently unreachable until a physical intervention. The 7-day window provides time to push an OTA (or a targeted renewal command via MQTT) to all 2,300 devices before they expire. Once expired, the recovery path requires physical access or re-provisioning, which is far more expensive.
  - *Why C is incorrect:* Extending certificate expiry dates via CA administrative tools is technically possible with some CA implementations, but it requires issuing new certificate versions for 2,300 devices and pushing them to the devices — which is the same as renewal. Most standard PKI implementations do not allow in-place extension of an issued certificate's validity period; a new certificate must be issued.
  - *Why D is incorrect:* Claim certificates are the bootstrap provisioning credential — they are used only for the initial JITP enrollment and are typically invalidated or stored with restricted access after that. Relying on claim certificates for re-provisioning 2,300 devices assumes the claim certificates are still active, still stored in firmware, and that the provisioning service accepts them for re-enrollment. This is the most complex and risky recovery path and should be a last resort, not the first response.

---

### Question 20

A zero-touch provisioning system requires devices to send a `RegisterThing` request containing the device serial number. The provisioning template generates a device certificate with a CN matching the serial number. An attacker intercepts the claim certificate from one device and attempts to enroll a device with a serial number `VALID_SERIAL_000001` that already exists in the registry. What should the provisioning service's response be, and what mechanism enforces this?

- A) The provisioning service should issue a new certificate for `VALID_SERIAL_000001` because the serial number is a public identifier — the fact that the attacker knows it does not indicate compromise, and the new certificate would simply replace the original.
- B) The provisioning service should reject the enrollment request because `VALID_SERIAL_000001` is already registered in the device registry. The uniqueness constraint on device IDs in the registry prevents duplicate enrollments for the same serial number, and the provisioning template should include a `CreateThing` operation with a duplicate-check that returns an error if the thing already exists.
- C) The provisioning service should issue the certificate but flag the event for security review, allowing normal operations to continue while the potential duplicate enrollment is investigated.
- D) The provisioning service should automatically revoke the original `VALID_SERIAL_000001` certificate and issue a new one, assuming the original device has been lost or replaced.
- **Correct Answer:** B) The provisioning service rejects the duplicate enrollment; registry uniqueness constraint enforces this.
- **Distractor Analysis:**
  - *Why A is incorrect:* Issuing a new certificate for an already-registered serial number would result in two valid certificates for the same device identity — the original legitimate device and the attacker's counterfeit device could both authenticate as `VALID_SERIAL_000001`. This would break the per-device identity guarantee and allow the attacker's device to publish data masquerading as the legitimate device.
  - *Why B is correct:* The device registry enforces Thing uniqueness. When the provisioning template executes a `CreateThing` operation with the name `VALID_SERIAL_000001`, AWS IoT Core (or equivalent) returns a `ResourceAlreadyExistsException` if the Thing already exists. The provisioning template can be configured to reject the enrollment or return an error in this case. This is a critical security control that prevents serial number replay attacks where an attacker uses an intercepted claim certificate to enroll counterfeit devices with known serial numbers.
  - *Why C is incorrect:* Issuing the certificate and flagging for review creates a window where the attacker's counterfeit device has valid credentials. During this review window, the device can authenticate, publish data, receive commands, and cause harm. The correct behavior is to reject the request synchronously.
  - *Why D is incorrect:* Automatically revoking the original certificate because a duplicate enrollment was attempted would allow the attacker to use the claim certificate as a denial-of-service tool against legitimate devices — connecting once per day with a known serial number would revoke that device's certificate daily.
