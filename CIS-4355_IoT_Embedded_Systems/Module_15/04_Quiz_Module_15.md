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
