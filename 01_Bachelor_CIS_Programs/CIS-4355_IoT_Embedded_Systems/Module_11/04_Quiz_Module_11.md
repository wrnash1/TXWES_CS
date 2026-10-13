# Quiz: Module 11 - IoT Device Management and OTA Updates
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Why should IoT devices be isolated on a separate network segment (VLAN) from corporate workstations and servers?
*   A) Network isolation increases the battery life of IoT devices by reducing the number of broadcast packets they must process.
*   B) Segmentation contains the blast radius of a compromised device — if a smart thermostat or camera is breached, firewall rules on the VLAN boundary prevent the attacker from reaching corporate file servers or financial systems.
*   C) VLANs double the effective bandwidth available to IoT devices by eliminating contention with laptop traffic on shared switches.
*   D) Placing IoT devices on a separate VLAN hides their MAC addresses from corporate network scanners, preventing asset inventory tools from detecting unauthorized devices.
*   **Correct Answer:** B) Segmentation contains the blast radius of a compromised device, preventing lateral movement from IoT to corporate network segments.
*   **Distractor Analysis:**
    *   *Why correct:* VLAN segmentation with inter-VLAN firewall rules is the OWASP IoT-recommended control for limiting lateral movement. A compromised camera on the IoT VLAN is blocked from TCP connections to the corporate finance server by the firewall policy, even if the attacker has full control of the camera.
    *   Battery life, bandwidth, and MAC address hiding are not the security rationale for VLAN isolation. The purpose is network segmentation to enforce least-privilege communication paths between device classes.

---

**Question 2**
Which of the following is the most accurate definition of **device decommissioning** in an IoT fleet management context?
*   A) The process of resetting a device to factory defaults and redeploying it to a new location with a new configuration, reusing the same X.509 certificate and device registry record.
*   B) The secure retirement of an IoT device at end-of-life, including certificate revocation in the cloud registry, deletion of the device twin, cryptographic erasure of on-device credentials, and physical disposal.
*   C) The scheduled shutdown of a device group during a maintenance window to apply firmware updates without interrupting production operations.
*   D) The archival of a device's historical telemetry data to cold storage after the device has been offline for more than 90 days.
*   **Correct Answer:** B) The secure retirement of an IoT device at end-of-life, including certificate revocation, device twin deletion, on-device credential erasure, and physical disposal.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Reusing a certificate from a decommissioned device on a new deployment is a security risk — if the old certificate was compromised during the device's prior life, the new device inherits that risk. Decommissioning ends, not continues, a device's identity.
    *   *Why B is correct:* Complete decommissioning requires revoking cloud-side credentials (so the certificate can no longer authenticate), removing the device from the registry (so the device twin no longer exists), erasing on-device secrets (so physical recovery of the device cannot yield usable credentials), and disposing of hardware. All four steps are required.
    *   *Why C is incorrect:* This describes a maintenance window or planned downtime, not decommissioning.
    *   *Why D is incorrect:* Archiving telemetry data is a data retention operation, not a device decommissioning process.

---

**Question 3**
A product team is deploying a firmware update to 500,000 smart meters in the field. The new firmware has passed QA testing but has never been deployed to production hardware at scale. Which OTA rollout strategy most effectively limits the risk of a defective firmware release causing a widespread outage?
*   A) Deploy the new firmware to all 500,000 meters simultaneously to minimize the total update window and reduce the period of fleet version fragmentation.
*   B) Deploy sequentially in alphabetical order by device ID — starting with "A" devices and progressing through "Z" — to create a natural gradual rollout without requiring additional tooling.
*   C) Use a staged rollout: deploy to a canary group of 500 devices (0.1%), monitor for errors and reboots for 24 hours, then expand to a pilot group of 50,000 (10%), and finally proceed to general availability only if error rates remain below threshold.
*   D) Require each device to download and verify the firmware locally before reporting readiness to the management system, then trigger all installs simultaneously once every device has verified its copy.
*   **Correct Answer:** C) Use a staged rollout starting with a canary group, monitoring for errors before expanding to the full fleet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A simultaneous full-fleet deployment means a defective firmware version instantly affects all 500,000 devices — a single firmware bug could take the entire fleet offline simultaneously, which is a catastrophic operational risk.
    *   *Why B is incorrect:* Alphabetical-by-device-ID ordering provides no meaningful risk segmentation — it does not group by hardware revision, firmware version, geographic region, or other risk-relevant dimensions, and does not include monitoring gates between stages.
    *   *Why C is correct:* Staged rollouts with monitoring gates are the industry standard for large-scale OTA campaigns. The canary group detects defects that passed QA, the gate prevents propagation to the wider fleet, and the error rate threshold provides an automatic halt trigger.
    *   *Why D is incorrect:* Pre-downloading and verifying before simultaneous install reduces the transmission window but still results in a simultaneous mass install — it does not limit blast radius if the firmware is defective.

---

**Question 4**
A fleet of 10,000 IoT environmental sensors has not received a firmware update in 18 months. A security audit finds 3,200 devices are offline (unreachable), 1,500 devices are running firmware with a known remote code execution CVE published 6 months ago, and no process exists to track which devices are running which firmware version. Which OWASP IoT Top 10 category does this situation primarily represent?
*   A) OWASP IoT #1 (Weak, Guessable, or Hardcoded Passwords) — the devices likely still use factory-default credentials since no management process exists to enforce credential rotation.
*   B) OWASP IoT #8 (Lack of Device Management) — the absence of firmware version tracking, patch deployment processes, and device health monitoring defines this category.
*   C) OWASP IoT #5 (Use of Insecure or Outdated Components) — the CVE in the 18-month-old firmware is the primary risk, classified as a vulnerable software component.
*   D) OWASP IoT #10 (Lack of Physical Hardening) — devices that are offline may have been physically tampered with, which is the root cause of the management gap.
*   **Correct Answer:** B) OWASP IoT #8 (Lack of Device Management).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Default credentials are a separate concern (OWASP IoT #1). While the management gap may permit credential issues to persist, the primary finding — no patch tracking, no health monitoring, no update process — maps to category #8.
    *   *Why B is correct:* OWASP IoT #8 is defined by the absence of: secure update mechanisms, firmware version tracking, device health monitoring, and processes for identifying and patching vulnerable devices. All four are missing here. The 3,200 offline devices and 1,500 unpatched CVE devices are symptoms of this management failure.
    *   *Why C is incorrect:* OWASP IoT #5 (Outdated Components) refers to third-party libraries or OS components with known CVEs embedded in firmware. It is a secondary finding enabled by the #8 management failure, but the root cause is the absence of a management process.
    *   *Why D is incorrect:* Physical hardening (#10) concerns debug port access and tamper-resistant enclosures. Offline devices may simply have connectivity issues — the finding does not indicate physical tampering.

---

**Question 5**
During an IoT device provisioning audit, an engineer discovers that all devices manufactured in the past year used a single "claim certificate" to authenticate to the provisioning service, and this certificate was never rotated or invalidated after provisioning was complete. What is the primary security risk of this configuration?
*   A) Devices provisioned with a shared claim certificate cannot receive OTA firmware updates because the update service requires unique per-device certificates for package delivery authorization.
*   B) The unrevoked shared claim certificate allows any device — including unauthorized or counterfeit devices — to connect to the provisioning service and receive valid production credentials, enabling enrollment of devices not manufactured by the organization.
*   C) Shared claim certificates cause certificate pinning failures in the device registry, resulting in all provisioned devices losing connectivity after 90 days when the certificate's notAfter validity period expires.
*   D) Using a single claim certificate violates X.509 naming conventions, causing the Certificate Authority to automatically revoke all device certificates derived from it.
*   **Correct Answer:** B) The unrevoked shared claim certificate allows unauthorized or counterfeit devices to enroll and receive valid production credentials.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* OTA update authorization uses the device's unique production certificate issued after provisioning, not the claim certificate — the claim certificate's continued existence does not affect OTA delivery.
    *   *Why B is correct:* A claim certificate is a temporary bootstrap credential — it should be revoked or rotated after each provisioning batch completes. An active, unrevoked claim certificate is a standing invitation for anyone who obtains it to enroll arbitrary devices. This is the zero-touch provisioning equivalent of leaving the factory door unlocked.
    *   *Why C is incorrect:* Certificate validity periods and device registry connectivity are independent of whether multiple devices share a certificate. Registry connectivity uses the unique device certificate issued after provisioning, not the claim certificate.
    *   *Why D is incorrect:* X.509 does not specify naming conventions that trigger automatic CA revocation; CAs revoke certificates only on explicit request or upon detecting policy violations, not on naming patterns.

---

**Question 6**
An IoT device management platform shows that 12% of a 20,000-device fleet has not checked in for more than 7 days. What is the most likely operational interpretation of this finding?

*   A) 2,400 devices have been deliberately decommissioned by the operations team and removed from the active fleet.
*   B) The fleet management dashboard has a rendering bug that incorrectly marks recently-active devices as offline.
*   C) 2,400 devices may have lost network connectivity, exhausted battery power, experienced hardware failures, or are otherwise unavailable — requiring investigation to distinguish between temporary outages and devices that need physical intervention.
*   D) The devices have detected a firmware security issue and have self-quarantined by disabling their network interfaces until a patch is applied.

*   **Correct Answer:** C) 2,400 devices may have lost connectivity, battery, or hardware, requiring investigation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deliberate decommissioning produces an explicit registry deletion event, not a silent offline status. If 12% were decommissioned, the registry would show deletions, not stale last-seen timestamps.
    *   *Why B is incorrect:* While UI bugs are possible, the operational response to 12% offline in a device management system is to investigate the devices, not to assume the dashboard is wrong.
    *   *Why C is correct:* In a real fleet, 12% unexplained offline after 7 days is a significant health event. The root causes span connectivity loss, battery depletion (for battery-powered devices), hardware failure, firmware crashes, or location changes. Device health monitoring exists precisely to trigger this investigation.
    *   *Why D is incorrect:* IoT devices do not autonomously self-quarantine by disabling network interfaces — this is not a standard device management behavior. Self-isolation would require explicit firmware logic implementing such a capability.

---

**Question 7**
A firmware update campaign is halted automatically after reaching 5% of the fleet. The rollout monitoring system triggered the halt because the reboot rate in the canary group exceeded the configured threshold of 3% within one hour of installation. What is the correct interpretation of this event?

*   A) The automatic halt is a false positive — reboot rates above 3% are normal during firmware update installation and the system should be configured to allow higher thresholds.
*   B) The canary group detected a defect in the new firmware that causes unexpected reboots; the automatic halt has successfully prevented the defective firmware from reaching 95% of the fleet.
*   C) The rollout system has a configuration error — reboot rate is not a valid metric for firmware health monitoring because all devices reboot exactly once during a firmware update.
*   D) The canary group devices are incompatible with the new firmware due to hardware revision differences, and the campaign should proceed after excluding canary-group hardware revisions from the deployment target.

*   **Correct Answer:** B) The canary detected a defect; the halt prevented the defect from reaching 95% of the fleet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Configuring appropriate halt thresholds is part of rollout design, but a reboot rate of 3%+ within one hour of installation is an abnormal signal — it indicates devices are crash-looping or encountering fatal firmware errors. The threshold was correctly triggered.
    *   *Why B is correct:* This is the entire purpose of canary-based staged rollouts. The canary group caught a defect that would have caused mass reboots across the fleet. The automatic halt contained the blast radius to 5%, and the firmware can now be investigated and fixed before resuming.
    *   *Why C is incorrect:* A single planned reboot during firmware installation is expected and would not trigger a threshold alert. The threshold alert fires when devices continue rebooting beyond the initial installation reboot — indicating a crash loop.
    *   *Why D is incorrect:* While hardware-revision incompatibility is a real OTA risk, the correct response is to investigate the canary group before making assumptions. Assuming hardware mismatch and proceeding without investigation could cause a fleet-wide outage.

---

**Question 8**
In AWS IoT Device Defender, what is the primary function of the "audit" feature?

*   A) It performs runtime behavioral analysis of device MQTT traffic to detect anomalous publish rates or connection patterns.
*   B) It scans the IoT Core configuration for security misconfigurations such as overly permissive policies, uncertified certificates, and devices sharing certificates.
*   C) It audits the device firmware binary for known CVEs using a static analysis engine integrated with the NVD database.
*   D) It records all MQTT messages to an immutable audit log stored in S3 for compliance reporting.

*   **Correct Answer:** B) It scans IoT Core configuration for security misconfigurations such as overly permissive policies and shared certificates.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes Device Defender's "Detect" feature, which performs behavioral anomaly detection on runtime device activity (publish rate, connection patterns, source IPs). The "Audit" feature examines static configuration, not runtime behavior.
    *   *Why B is correct:* AWS IoT Device Defender Audit runs scheduled checks against the IoT Core configuration, flagging issues like: policies with `*` wildcard resources, inactive certificates left attached to things, multiple devices sharing one certificate, logging disabled, and CA certificates not registered with OCSP revocation. These are configuration-plane checks, not runtime monitoring.
    *   *Why C is incorrect:* Device Defender does not perform firmware static analysis or CVE scanning. Firmware vulnerability management is a separate discipline handled by SBOM analysis tools, not the cloud-side IoT management plane.
    *   *Why D is incorrect:* MQTT message logging is handled by AWS IoT Core logging (to CloudWatch) and IoT Rules Engine archival to S3 — not by Device Defender Audit.

---

**Question 9**
When an ESP32 device uses the `esp_https_ota()` function for over-the-air updates, which security property does it provide and which must be added separately?

*   A) It provides firmware signature verification using ECDSA by default; TLS server authentication must be configured separately using a CA certificate.
*   B) It provides TLS-encrypted transport and server certificate validation (preventing MITM substitution of the update URL); firmware binary signature verification must be enabled separately through Secure Boot configuration.
*   C) It provides both TLS transport security and ECDSA firmware signature verification with no additional configuration required beyond the URL and firmware size.
*   D) It provides HTTP/2 multiplexed download for reduced bandwidth; all cryptographic verification must be implemented by the application layer.

*   **Correct Answer:** B) Provides TLS transport + server cert validation; firmware binary signature verification requires separate Secure Boot configuration.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `esp_https_ota()` does NOT verify the firmware binary's ECDSA signature by default — it verifies the TLS server certificate (authenticating the update server), not the firmware content. Secure Boot signature verification is a separate eFuse-based configuration.
    *   *Why B is correct:* `esp_https_ota()` establishes a TLS connection to the OTA update URL and validates the server's certificate against the configured root CA, preventing an attacker from substituting a malicious server. It does not inspect or verify the content of the firmware binary. Firmware signature verification requires enabling Secure Boot with code signing in the ESP-IDF configuration.
    *   *Why C is incorrect:* ECDSA firmware signature verification is not enabled by default in `esp_https_ota()`. It requires explicit Secure Boot configuration in menuconfig.
    *   *Why D is incorrect:* `esp_https_ota()` does use TLS (HTTPS), not HTTP/2 multiplexing. The function's primary security value is TLS transport, not bandwidth optimization.

---

**Question 10**
A device management system maintains a "device twin" for each enrolled sensor. The twin's `reported` property shows `{"firmware": "2.1.0"}` while the `desired` property shows `{"firmware": "3.0.0"}`. The device has been offline for 48 hours. What is the correct state description and expected behavior when the device reconnects?

*   A) The device twin is in a conflict state; the management platform will automatically resolve the conflict by reverting the desired version to 2.1.0 to match the reported state.
*   B) The twin shows a delta (desired ≠ reported); when the device reconnects, it will receive the delta, trigger its OTA update process to apply firmware 3.0.0, and then update reported to {"firmware": "3.0.0"} upon completion.
*   C) The twin is in an error state; the 48-hour offline period exceeded the twin's TTL and the desired property has been automatically deleted by the platform.
*   D) The device twin is read-only when the device is offline; the desired property update to 3.0.0 cannot take effect until the device is online to receive the write.

*   **Correct Answer:** B) The twin shows a delta; on reconnect the device receives it, applies the update, and reports the new version.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Device twin platforms never auto-revert desired state to match reported state. The purpose of desired state is to represent operator intent; the platform waits for the device to converge, not the operator intent to regress.
    *   *Why B is correct:* This is the core value proposition of Device Shadow / Device Twin. The platform durably stores the desired state while the device is offline. On reconnect, the device subscribes to the delta topic and receives the unresolved difference between desired and reported. The device then executes the OTA update and publishes the updated reported state after completion.
    *   *Why C is incorrect:* Device Twin / Shadow documents do not have a short TTL that deletes desired state after 48 hours. The desired state persists until the operator changes it or the device reports it fulfilled.
    *   *Why D is incorrect:* Desired state can absolutely be written to the twin while the device is offline. This is the primary use case — an operator updates desired state at any time, and the device receives it on next reconnect.

---

**Question 11**
Which of the following correctly describes the difference between certificate revocation via CRL and via OCSP in an IoT fleet management context?

*   A) CRL (Certificate Revocation List) is a periodic batch download of all revoked certificate serial numbers; OCSP (Online Certificate Status Protocol) provides real-time per-certificate status queries, but both require the IoT device to have outbound internet access to the CA.
*   B) CRL must be embedded in the device firmware at manufacturing time; OCSP is checked at runtime by the cloud broker, not the device.
*   C) CRL revokes certificates by deleting them from the device's trust store; OCSP revokes certificates by changing the certificate's embedded validity period field.
*   D) CRL and OCSP are identical mechanisms with different names — both involve the CA publishing a list of revoked certificates that devices download at connection time.

*   **Correct Answer:** A) CRL is a periodic batch list; OCSP provides real-time per-certificate status, both requiring CA connectivity.
*   **Distractor Analysis:**
    *   *Why A is correct:* A CRL is a signed list published by the CA at intervals (hourly, daily) containing serial numbers of all revoked certificates. Clients download the full list. OCSP allows a client to query the CA (or a delegated OCSP responder) for the status of a single specific certificate in real time, receiving a signed "good," "revoked," or "unknown" response. Both require connectivity to the CA infrastructure.
    *   *Why B is incorrect:* CRLs are not embedded at manufacturing time — they are dynamic, published periodically as new certificates are revoked. OCSP is typically checked by TLS clients (including IoT devices) at connection time, not exclusively by the broker.
    *   *Why C is incorrect:* Neither CRL nor OCSP modifies the certificate itself. They are external status mechanisms. Certificates are immutable signed documents; their content cannot be changed after issuance.
    *   *Why D is incorrect:* CRL and OCSP are distinct mechanisms with different operational characteristics (batch vs. real-time, list vs. query) and different trade-offs for IoT deployments where CA connectivity may be intermittent.

---

**Question 12**
An IoT platform's device registry shows a device last connected 14 months ago and its firmware version is "1.0.0" while the current fleet standard is "4.2.1". What decommissioning risk does this device pose if it reconnects?

*   A) The device's firmware is too old to parse the current MQTT message format, causing it to corrupt data in the time-series database upon reconnect.
*   B) The device may be running firmware with multiple unpatched CVEs spanning 14 months of releases, and its X.509 certificate — if never revoked — remains valid for authenticating to the broker with full device privileges.
*   C) The device's 14-month offline period means its internal real-time clock has drifted, causing TLS handshake failures due to certificate validity date mismatches.
*   D) The device is running firmware 1.0.0 which predates the current MQTT broker's minimum protocol version, causing automatic broker rejection on the next connection attempt.

*   **Correct Answer:** B) The device may run unpatched CVE firmware and holds a valid certificate that was never revoked.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* MQTT message parsing compatibility and time-series database corruption are not standard concerns tied to version skew. Brokers handle multiple firmware versions simultaneously.
    *   *Why B is correct:* A device missing 14 months of firmware updates may be vulnerable to every CVE published in that period. More critically, if the certificate was never revoked when the device went offline, it remains a valid credential. A reconnecting device — potentially recovered, resold, or compromised — would be authenticated by the broker as a trusted fleet member despite its unpatched state.
    *   *Why C is incorrect:* RTC drift over 14 months is typically seconds to minutes, not years. TLS certificates have validity windows measured in years; minor clock drift does not cause handshake failures. Devices also typically sync NTP on reconnect.
    *   *Why D is incorrect:* MQTT protocol versions (3.1, 3.1.1, 5.0) are not tied to firmware application version numbers. The broker version and the device MQTT library version determine protocol compatibility, not the firmware version string.

---

**Question 13**
In a zero-touch provisioning workflow, what is the role of the Device Provisioning Service (DPS) in Azure IoT Hub?

*   A) DPS acts as a software update server, delivering firmware images to devices during manufacturing before they are shipped to customers.
*   B) DPS provides load balancing across multiple IoT Hub instances, routing telemetry from high-volume device fleets to avoid hub throttling.
*   C) DPS automates device enrollment and assignment — a device with a factory-provisioned certificate connects to DPS, which validates the certificate, looks up the enrollment record, and assigns the device to the correct IoT Hub instance with a unique device identity.
*   D) DPS encrypts device-to-cloud messages using a hub-managed key rather than device certificates, removing the need for per-device key material.

*   **Correct Answer:** C) DPS validates the certificate, looks up the enrollment record, and assigns the device to the correct IoT Hub with a unique identity.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DPS is not a firmware distribution service. OTA firmware delivery in Azure is handled by Azure Device Update for IoT Hub, a separate service.
    *   *Why B is incorrect:* While DPS does support multi-hub deployments and can balance device enrollment across hubs, its primary role is provisioning (identity establishment), not runtime telemetry load balancing.
    *   *Why C is correct:* DPS implements the zero-touch provisioning flow: (1) Device boots with a factory certificate, (2) connects to the global DPS endpoint, (3) DPS validates the certificate against the enrollment group, (4) DPS assigns the device to a specific IoT Hub instance and returns the hub hostname and device ID, (5) device connects to the assigned hub with its final identity. This eliminates per-device manual registration.
    *   *Why D is incorrect:* DPS does not replace per-device key material with hub-managed keys. Each device retains its own certificate; DPS merely routes the device to the correct hub during initial enrollment.

---

**Question 14**
A fleet of 50,000 devices is running firmware with a critical RCE vulnerability. The security team has a patch ready but estimates it will take 72 hours to update the full fleet at the current OTA throughput. What immediate mitigation should be applied during the 72-hour update window?

*   A) Shut down the OTA update server to prevent the attacker from learning which devices have been patched and targeting unpatched devices.
*   B) Apply network-layer ACLs or firewall rules to restrict outbound connections from the IoT VLAN to known-good destinations, limiting what an attacker can do if they exploit the vulnerability during the update window.
*   C) Change the MQTT broker password for all devices simultaneously to invalidate any active attacker sessions.
*   D) Increase the OTA update throttle to push the firmware to all 50,000 devices in parallel, completing the update in under 1 hour regardless of bandwidth impact.

*   **Correct Answer:** B) Apply network ACLs to restrict IoT VLAN outbound connections during the update window.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Shutting down the OTA server stops the patch deployment, which is the primary remediation. This would be counterproductive and leave all 50,000 devices vulnerable.
    *   *Why B is correct:* Defense in depth during a known vulnerability window means layering network controls to limit blast radius. Restricting outbound connections from the IoT VLAN to only the MQTT broker and NTP server prevents exploited devices from calling back to attacker C2 infrastructure, exfiltrating data, or scanning internal networks — buying time while the patch is deployed.
    *   *Why C is incorrect:* MQTT X.509 certificate authentication does not use passwords. Even for username/password MQTT, rotating credentials across 50,000 devices simultaneously without a management system would cause a fleet-wide connectivity outage.
    *   *Why D is incorrect:* Maximum parallel OTA throttle risks overwhelming the OTA server and the devices' own flash write capacity, potentially corrupting firmware on devices that receive partial images due to bandwidth saturation. Staged deployment with monitoring is always safer.

---

**Question 15**
What is "cryptographic erasure" in the context of IoT device decommissioning, and why is it preferable to overwriting flash memory with zeros?

*   A) Cryptographic erasure involves revoking the device's cloud certificate, which mathematically invalidates all data previously encrypted with that certificate's public key.
*   B) Cryptographic erasure deletes the encryption key protecting flash-encrypted storage; since all data is AES-encrypted and the key is gone, the ciphertext is permanently unrecoverable without performing the physically slow process of overwriting every flash sector.
*   C) Cryptographic erasure uses a hardware random number generator to overwrite flash sectors with cryptographically random data rather than zeros, making data recovery harder than a simple zero-fill.
*   D) Cryptographic erasure refers to the secure hash verification performed during decommissioning to confirm that the device's flash contents match the known-good factory image before physical disposal.

*   **Correct Answer:** B) Deleting the encryption key renders all flash-encrypted data permanently unrecoverable without requiring sector-by-sector overwrite.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Revoking a cloud certificate affects authentication capabilities, not data stored on the physical device. Data on flash encrypted with a device key is independent of cloud certificate revocation.
    *   *Why B is correct:* When flash encryption is enabled (e.g., ESP32 AES-XTS), all flash contents are ciphertext. The encryption key lives in eFuse. Deleting or destroying the eFuse key (burning the eFuse key-read-disable bit, or physically destroying the chip) renders all stored ciphertext permanently unreadable in milliseconds. Overwriting flash with zeros on NAND/NOR flash requires erasing every sector (which can take minutes and cannot address wear-leveled blocks), whereas key deletion is instantaneous and cryptographically equivalent to erasing all data.
    *   *Why C is incorrect:* Overwriting with random data is a data sanitization technique (DoD 5220.22-M style) but is not the definition of cryptographic erasure, and it does not have the speed advantage of key deletion.
    *   *Why D is incorrect:* Hash verification of flash contents is an integrity check, not a data destruction process.

---

**Question 16**
Which combination of AWS IoT Core features provides the complete set of controls needed to enforce that each device can only access its own shadow and publish to its own topic?

*   A) IoT Rules Engine with device-specific SQL WHERE clauses, combined with CloudWatch metric alarms for each device topic.
*   B) X.509 certificates for authentication combined with IoT policies using the `${iot:ClientId}` policy variable to scope resource ARNs to the connecting device's own identity.
*   C) AWS Cognito User Pools for device identity management, with Lambda authorizers that check device ID against a DynamoDB registry before allowing MQTT connections.
*   D) VPC-private MQTT endpoints with security groups restricting each device's EC2 instance to its own port, preventing cross-device access.

*   **Correct Answer:** B) X.509 authentication combined with IoT policies using `${iot:ClientId}` policy variable.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Rules Engine SQL operates on message content after publication; it cannot prevent a device from publishing to another device's topic in the first place. CloudWatch alarms are alerting tools, not access control mechanisms.
    *   *Why B is correct:* AWS IoT Core uses X.509 certificates to authenticate device identity (the ClientId must match the certificate's Thing name). IoT policies with `${iot:ClientId}` substitute the connecting device's Client ID into the resource ARN at evaluation time, so a policy like `arn:aws:iot:*:*:topic/sensors/${iot:ClientId}/*` automatically scopes each device to only its own topic hierarchy and shadow path.
    *   *Why C is incorrect:* Cognito User Pools are designed for human user authentication (web/mobile apps), not IoT device identity. Lambda custom authorizers are a valid IoT Core feature but are not the standard approach for per-device scoping.
    *   *Why D is incorrect:* AWS IoT Core is a managed service, not an EC2-based deployment. VPC security groups and port-based access control are not the architecture used by IoT Core device policies.

---

**Question 17**
An IoT device management audit finds that 200 devices share a single X.509 certificate (the factory default certificate was never replaced with per-device certificates). What is the primary operational security risk?

*   A) TLS handshake performance degrades when multiple devices share a certificate because the broker must decrypt all connections with the same key material simultaneously.
*   B) Revoking the single shared certificate to decommission one compromised device immediately disconnects all 200 devices sharing that certificate — making it impossible to isolate a single compromised device.
*   C) Devices sharing a certificate cannot use MQTT QoS 1 or 2 because the PUBACK mechanism requires unique certificate serial numbers for message deduplication.
*   D) The CA will detect the shared certificate usage pattern and automatically revoke the certificate after 30 days per X.509 multi-use policy.

*   **Correct Answer:** B) Revoking the shared certificate to decommission one device disconnects all 200 devices sharing it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* TLS performance is not affected by how many devices share a certificate. Each TLS session is independent; the broker processes each session's cryptographic operations separately.
    *   *Why B is correct:* Certificate-based device isolation requires per-device certificates. If one of the 200 devices is compromised and the security response is to revoke the shared certificate, the broker rejects all 200 devices. Conversely, if the certificate is not revoked to avoid operational disruption, the compromised device retains valid authentication indefinitely. Per-device certificates are mandatory for effective incident response.
    *   *Why C is incorrect:* MQTT QoS mechanisms use packet IDs for deduplication, not certificate serial numbers. Certificate identity plays no role in QoS message acknowledgment.
    *   *Why D is incorrect:* X.509 certificates have no built-in multi-use revocation policy. CAs do not monitor how many devices are using a certificate or automatically revoke based on usage count.

---

**Question 18**
A security engineer proposes implementing firmware integrity verification using SHA-256 hashes stored in a cloud registry. Each device downloads the hash, computes its own flash hash at boot, and refuses to start if they differ. What limitation does this approach have compared to ECDSA firmware signature verification?

*   A) SHA-256 hash computation is too slow for embedded microcontrollers; ECDSA verification is faster because it uses shorter key lengths.
*   B) An attacker who can modify the firmware can also modify the hash value in the cloud registry (or intercept the hash download) to match the tampered firmware, defeating the integrity check; ECDSA requires the attacker to also possess the manufacturer's private key to forge a valid signature.
*   C) SHA-256 hashes cannot be computed over binary firmware images; they are only valid for text-based files, requiring base64 encoding of the firmware before hashing.
*   D) Cloud-hosted hash verification requires a persistent internet connection at every boot, whereas ECDSA signature verification is performed offline using the public key embedded in firmware.

*   **Correct Answer:** B) An attacker can replace both the firmware and the cloud hash; ECDSA requires the manufacturer's private key to forge.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SHA-256 is computationally cheaper than ECDSA; ECDSA verification involves elliptic curve arithmetic that is more expensive than a hash computation. The performance argument is reversed.
    *   *Why B is correct:* A hash value is an unauthenticated integrity check. If the attacker controls the update server or cloud registry (or can perform a MITM on the hash download), they can substitute both the firmware and the matching hash. ECDSA signature verification uses asymmetric cryptography: the private key (held only by the manufacturer) signs the firmware; the device uses the embedded public key to verify. An attacker cannot forge a valid signature without the private key, even if they control the update server.
    *   *Why C is incorrect:* SHA-256 operates on arbitrary byte sequences — it is a binary hash function that works identically on firmware binaries and text files.
    *   *Why D is incorrect:* Both approaches can be made online or offline. ECDSA verification is typically performed offline (public key embedded in device firmware/eFuse), but the hash comparison approach described also requires an online cloud lookup at boot — so D describes the hash approach, not a difference between them.

---

**Question 19**
What does the `reported` section of an AWS IoT Device Shadow represent, and who is responsible for updating it?

*   A) It represents the operator's desired configuration for the device; the IoT Core console updates it when an administrator changes device settings.
*   B) It represents the device's actual current state as last communicated; the device firmware is responsible for publishing updates to it whenever its state changes.
*   C) It represents the historical log of all past states the device has reported, maintained as an append-only time-series by the shadow service.
*   D) It represents the shadow's computed metadata (last update timestamp, version number) maintained by the AWS IoT Core service itself.

*   **Correct Answer:** B) It represents the device's actual current state; device firmware publishes updates to it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes the `desired` section, which represents operator intent. The `reported` section represents what the device has actually confirmed about its own state.
    *   *Why B is correct:* The `reported` section is exclusively written by the device. When the device successfully applies a configuration change, updates sensor readings, or changes its operational state, it publishes a Shadow update to the `reported` path. This is how the cloud knows the device's actual current state, as opposed to what the operator wants it to be.
    *   *Why C is incorrect:* Device Shadow is a point-in-time state document, not an append-only time-series log. It stores only the current state (and the latest version). Historical state requires a separate time-series database (DynamoDB, InfluxDB) populated via a Rules Engine action.
    *   *Why D is incorrect:* Shadow metadata (`metadata` section) is indeed maintained by the service, but it is a separate field from `reported`. The `reported` section contains application-defined state data published by the device.

---

**Question 20**
An IoT fleet manager wants to ensure that any device not seen for more than 30 days is flagged for decommissioning review. Which combination of features supports this process in AWS IoT Core?

*   A) Device Defender Audit (to scan for policy violations) combined with SNS email alerts (to notify the security team of flagged devices).
*   B) IoT Registry `lastConnected` timestamp combined with AWS IoT Events (or a Lambda function triggered by a CloudWatch scheduled rule) to query devices with last-seen > 30 days and publish alerts to SNS.
*   C) IoT Rules Engine SQL that selects from the `$aws/events/presence/disconnected/+` topic and triggers an SNS alert for each disconnection event.
*   D) AWS IoT Greengrass local health monitoring that reports inactive edge devices to the cloud via a periodic heartbeat MQTT message.

*   **Correct Answer:** B) IoT Registry lastConnected timestamp queried by a scheduled Lambda to find devices offline > 30 days.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Device Defender Audit checks configuration misconfigurations (policies, certificates) — it does not track device last-seen timestamps or flag devices for decommissioning based on inactivity periods.
    *   *Why B is correct:* The IoT Registry records metadata including `lastConnectedTime` per device. A scheduled CloudWatch Events rule triggering a Lambda function can query the registry via `list-things` + `describe-thing` (or IoT Fleet Indexing with a query like `connectivity.disconnectedTime > ${30_days_ago}`) to find devices exceeding the 30-day inactivity threshold and publish decommissioning candidates to an SNS topic or ServiceNow ticket.
    *   *Why C is incorrect:* The `$aws/events/presence/disconnected/` lifecycle event fires when a device disconnects (immediately), not after a 30-day inactivity period. Using this event for 30-day tracking would require storing state (last disconnect time) and a separate scheduled check — it is not a direct solution.
    *   *Why D is incorrect:* Greengrass monitors edge-deployed Lambda functions and container workloads on gateway devices — it does not monitor the entire fleet's cloud connectivity as a 30-day inactivity tracking system.
