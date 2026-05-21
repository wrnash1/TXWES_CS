# Quiz: Module 06 - IoT Cloud Platforms – AWS IoT Core, Azure IoT Hub, GCP IoT
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Which wireless protocol is best suited for low-power, long-range sensor networks deployed across agricultural fields?
*   A) Bluetooth Low Energy (BLE)
*   B) LoRaWAN
*   C) Wi-Fi (802.11)
*   D) Zigbee
*   **Correct Answer:** B) LoRaWAN offers long-range (kilometers) communications at extremely low power rates, sacrificing bandwidth.
*   **Distractor Analysis:**
    *   *Why correct:* LoRaWAN uses chirp spread-spectrum modulation to achieve 2–15 km range at 0.3–50 kbps, drawing microamps on average — ideal for remote agricultural deployments.
    *   BLE is restricted to short ranges (10–100 m). Wi-Fi consumes 50–300 mA during transmission, draining batteries in days. Zigbee extends range through mesh but requires relay nodes every ~100 m, impractical over kilometers.

---

**Question 2**
Which of the following is the most accurate definition of an **AWS IoT Core IoT Policy**?
*   A) A JSON Web Token signed with an RSA private key that authenticates a device to Google Cloud IoT Core over MQTT.
*   B) A JSON document attached to an X.509 certificate that specifies which MQTT topics a device is permitted to publish or subscribe to, enforcing least-privilege access on the broker.
*   C) A cloud-side JSON document with "desired" and "reported" sections that synchronizes configuration state between the cloud and an offline IoT device.
*   D) A managed container orchestration policy that scales IoT microservices in Kubernetes based on incoming message volume.
*   **Correct Answer:** B) A JSON document attached to an X.509 certificate that specifies which MQTT topics a device is permitted to publish or subscribe to, enforcing least-privilege access on the broker.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes GCP IoT Core's JWT authentication mechanism, not an AWS IoT Policy.
    *   *Why B is correct:* AWS IoT Policies use IAM-style JSON with Allow/Deny rules on IoT actions (iot:Publish, iot:Subscribe) and topic ARNs; they are attached to the device certificate and evaluated on every connection and message.
    *   *Why C is incorrect:* This describes the AWS IoT Device Shadow (or Azure Device Twin) state synchronization document, not a policy.
    *   *Why D is incorrect:* Kubernetes scaling policies are unrelated to IoT device authorization on AWS IoT Core.

---

**Question 3**
An IoT deployment provisions 50,000 environmental sensors, each connecting to AWS IoT Core with the same X.509 certificate and an IoT Policy granting `iot:*` on resource `*`. A single sensor is physically stolen and its certificate is extracted. What is the primary security consequence?
*   A) The stolen certificate can only be used to access the specific device shadow for the sensor it was extracted from.
*   B) The attacker can use the stolen certificate to publish and subscribe to any topic on the broker, potentially impersonating other devices or reading all telemetry.
*   C) AWS IoT Core automatically revokes the certificate when the device goes offline for more than 24 hours.
*   D) The wildcard policy has no effect because AWS IoT Core enforces per-device topic isolation by default regardless of policy content.
*   **Correct Answer:** B) The attacker can use the stolen certificate to publish and subscribe to any topic on the broker, potentially impersonating other devices or reading all telemetry.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A shared certificate with wildcard policy grants access far beyond a single device shadow — the entire broker's topic namespace is accessible.
    *   *Why B is correct:* Sharing a single certificate across devices violates both uniqueness and least-privilege principles. The wildcard `iot:*` on `*` means the stolen credential has unrestricted broker access until manually revoked.
    *   *Why C is incorrect:* AWS IoT Core does not automatically revoke certificates based on device offline duration; revocation requires an explicit administrative action.
    *   *Why D is incorrect:* Topic isolation is not enforced automatically — it must be explicitly configured in the IoT Policy using device-specific topic ARNs such as `devices/${iot:ClientId}/#`.

---

**Question 4**
A device running on Azure IoT Hub reconnects after being offline for 6 hours. During that time, an operator updated the device's desired configuration state in the Device Twin. What happens when the device reconnects?
*   A) The device receives an error because the Device Twin was modified while the device was offline, and the twin must be manually reset before reconnecting.
*   B) Azure IoT Hub discards the desired state changes made while the device was offline to avoid conflicts with the device's reported state.
*   C) The device retrieves the Device Twin delta document containing the difference between the last reported state and the current desired state, then applies the pending configuration changes.
*   D) The device must explicitly request a full firmware re-flash via OTA before the Device Twin can synchronize configuration.
*   **Correct Answer:** C) The device retrieves the Device Twin delta document containing the difference between the last reported state and the current desired state, then applies the pending configuration changes.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Device Twin modifications during offline periods are intentional and supported — the twin persists desired state regardless of device connectivity.
    *   *Why B is correct (why B is incorrect):* Discarding desired changes would defeat the purpose of Device Twins; the entire design goal is to reliably deliver configuration to intermittently connected devices.
    *   *Why C is correct:* The delta document contains only the properties that differ between desired and reported state, minimizing bandwidth on reconnection and enabling reliable configuration delivery to offline devices.
    *   *Why D is incorrect:* Device Twin synchronization handles configuration state; OTA firmware updates are a separate mechanism not triggered by twin synchronization.

---

**Question 5**
A security team reviewing a GCP IoT Core deployment discovers that all 10,000 devices share the same RSA key pair for JWT authentication, and the Pub/Sub topic receiving telemetry has public read access enabled. Which two security controls most effectively remediate these findings?
*   A) Issue unique RSA or EC key pairs per device at provisioning, and restrict the Pub/Sub subscription to authorized service accounts only.
*   B) Switch all devices from MQTT to HTTP transport, and enable Cloud Armor DDoS protection on the Pub/Sub endpoint.
*   C) Rotate the shared RSA key pair every 30 days and keep the Pub/Sub topic public to simplify downstream consumer access.
*   D) Disable JWT authentication entirely and rely on TLS transport encryption alone for device identity verification.
*   **Correct Answer:** A) Issue unique RSA or EC key pairs per device at provisioning, and restrict the Pub/Sub subscription to authorized service accounts only.
*   **Distractor Analysis:**
    *   *Why A is correct:* Unique per-device keys limit the blast radius of any single compromised device to that device alone; restricting Pub/Sub access to authorized service accounts prevents unauthorized parties from reading all telemetry.
    *   *Why B is incorrect:* Switching transport protocols does not address the shared key or public topic vulnerabilities; Cloud Armor protects against volumetric attacks, not data exposure.
    *   *Why C is incorrect:* Rotating a shared key still leaves all devices using the same credential — a single compromised key still exposes all devices; keeping the topic public does not address the data exposure risk.
    *   *Why D is incorrect:* TLS provides transport encryption but not device identity — removing JWT authentication means any client with a valid TLS connection can publish as any device.
