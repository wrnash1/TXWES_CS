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
