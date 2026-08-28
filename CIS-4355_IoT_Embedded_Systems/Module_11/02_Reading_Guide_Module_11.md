# Reading Guide: Module 11 - IoT Device Management and OTA Updates

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4355 &BULL; INTERNET OF THINGS (IOT) & EMBEDDED SYSTEMS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 11 – IoT Device Management and OTA Updates**! This module covers how organizations provision, configure, monitor, and maintain fleets of deployed IoT devices throughout their operational lifecycle. Managing hundreds of thousands of devices distributed across geographies — keeping them patched, monitored, and compliant — is one of the most operationally complex challenges in enterprise IoT. Failure to manage devices at scale leads directly to OWASP IoT Top 10 category #8 (Lack of Device Management) and #4 (Lack of Secure Update Mechanism).

You will learn how device provisioning establishes secure identity at manufacture, how device registries track fleet state, how over-the-air update campaigns deliver firmware patches to segmented rollout groups, how device health monitoring detects anomalies and offline devices, and how decommissioning procedures securely retire credentials and wipe sensitive data when devices reach end-of-life.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Device Provisioning**: The process of establishing a device's unique cryptographic identity at manufacture or first deployment, including generating a unique X.509 certificate and private key, enrolling the device in a registry, and configuring initial network and cloud connection settings. Provisioning must be performed in a secure manufacturing environment to prevent key compromise; the private key should be generated on the device itself and never leave it.
*   **Device Registry**: A cloud-side database that maintains an authoritative record of every enrolled device in a fleet, including device identity, current firmware version, connectivity status, configuration state, and associated metadata. AWS IoT Core, Azure IoT Hub, and GCP IoT Core each maintain a device registry. The registry is the authoritative source for determining which devices need a firmware update and whether a device connecting to the broker is authorized.
*   **OTA Rollout Campaign**: A managed process for deploying a firmware update to a subset or all devices in a fleet, typically in stages: canary group (1–5% of devices) → pilot group (10–20%) → general availability (remaining fleet). Staged rollouts detect defects in the new firmware before they impact the full fleet, and rollout management systems track success rates, error rates, and automatically halt deployment if thresholds are exceeded.
*   **Device Health Monitoring**: Continuous observation of device telemetry — CPU load, memory usage, battery level, connectivity uptime, error rates — to detect devices that are offline, malfunctioning, or behaving anomalously. Health monitoring enables proactive maintenance (dispatching a technician before a device fails) and security monitoring (detecting devices that have been compromised or are behaving outside their baseline profile).
*   **Device Decommissioning**: The secure retirement of an IoT device at end-of-life or when it is replaced, comprising: revocation of the device's X.509 certificate in the cloud registry, deletion of the device's record from the device twin/shadow, cryptographic erasure of sensitive credentials stored on the device's flash memory, and physical disposal. Failure to revoke credentials during decommissioning leaves valid authentication material that an attacker could use to impersonate the device after disposal.

---

### 2. Certification Exam Tips
*   **OWASP IoT #8 (Lack of Device Management):** Exam scenarios describe large fleets with no patch tracking, no monitoring, and no decommissioning process. Recognize this as category #8 and know the remediation: a device registry with firmware version tracking, health monitoring dashboards, and automated OTA campaigns.
*   **Staged OTA rollout logic:** Know the canary → pilot → GA progression. Exam questions may ask why a staged rollout is used (answer: to limit blast radius of defective firmware) or what triggers an automatic rollout halt (answer: error rate or reboot rate exceeds a configured threshold).
*   **Certificate revocation vs. device deletion:** Revoking a certificate removes the device's ability to authenticate even if the certificate is still present on the device. Deleting the device twin/shadow removes the cloud-side state record. Both actions are required for complete decommissioning.
*   **Zero-touch provisioning:** AWS IoT Fleet Provisioning and Azure DPS (Device Provisioning Service) enable devices to self-register and receive their final credentials on first boot, without requiring manual registry enrollment per device. Know that these services require a claim certificate (a temporary credential used only for the provisioning handshake) that is replaced by a unique device certificate upon successful enrollment.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers OWASP IoT Top 10 category #8 (Lack of Device Management) and #4 (Lack of Secure Update Mechanism) — both directly relevant to the device fleet management and OTA update topics in this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on OWASP IoT Top 10 categories #4 (Lack of Secure Update Mechanism) and #8 (Lack of Device Management), which describe the real-world consequences of unmanaged device fleets and insecure OTA pipelines.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) covers device lifecycle management patterns, OTA update workflow design, and fleet monitoring architectures for large-scale IoT deployments.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Simulate device provisioning with a registry**: Using the AWS IoT Core CLI or a local Mosquitto broker with a SQLite device registry, provision three simulated devices with unique certificates, register them in the registry with their firmware version and status, and verify each device can authenticate and publish telemetry.
*   **Execute a staged OTA rollout**: Using a Python script, implement a two-stage rollout that first delivers a new "firmware version" (a JSON config file) to 1 of 3 devices (canary), verifies the device reports the new version back within 60 seconds, then proceeds to update the remaining 2 devices only on success.
*   **Demonstrate decommissioning**: Revoke one device's certificate by removing it from the registry, attempt a connection with the revoked certificate, confirm the broker rejects the connection, and document this as evidence of proper decommissioning procedure.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the five device lifecycle stages: provision, operate, monitor, update, decommission.
- [ ] Read OWASP IoT Top 10 categories #4 and #8 at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the device management sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review the staged rollout and certificate revocation concepts before the lab.
- [ ] Proceed to the weekly hands-on lab activity.

---

## 9. Supplemental Resources

**1. AWS IoT Device Defender — Developer Guide**
[https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html)
Amazon's official documentation for IoT Device Defender, covering both Audit (configuration checks for overly permissive policies, inactive certificates, shared certificates) and Detect (behavioral anomaly detection for runtime MQTT traffic). Directly supports the device health monitoring and fleet security audit topics in Section 1 of this guide.

**2. Azure Device Update for IoT Hub — Overview**
[https://learn.microsoft.com/en-us/azure/iot-hub-device-update/understand-device-update](https://learn.microsoft.com/en-us/azure/iot-hub-device-update/understand-device-update)
Microsoft's documentation for Azure Device Update (ADU), covering staged OTA rollout groups, deployment policies, delta updates, and compliance reporting. Covers the canary/pilot/GA rollout pattern and automatic rollout halt on error thresholds referenced in the certification exam tips.

**3. ESP-IDF OTA Update Guide — esp_https_ota and Secure Boot**
[https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ota.html](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ota.html)
Espressif's reference for the ESP32 OTA update framework, including `esp_https_ota()`, A/B partition configuration, rollback on boot failure, and integration with Secure Boot for firmware signature verification. Essential reading for the embedded OTA implementation aspects of this module.
