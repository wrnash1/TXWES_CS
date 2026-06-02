# Quiz – Module 06: IoT Cloud Platforms – AWS IoT Core, Azure IoT Hub, GCP IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Format:** 10 questions, multiple choice, 4 options each
**Certification Alignment:** CompTIA IoT+ Domain 4

---

## Question 1

Which wireless protocol is best suited for low-power, long-range sensor networks deployed across agricultural fields kilometers from the nearest gateway?

- A) Bluetooth Low Energy (BLE)
- B) LoRaWAN
- C) Wi-Fi 802.11ac
- D) Zigbee mesh

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: BLE range is 10–100 m. Agricultural field sensors can be kilometers from any gateway. BLE cannot meet this distance requirement regardless of its excellent power consumption.
- B is correct: LoRaWAN achieves 2–15 km range using chirp spread spectrum modulation, draws microamps on average, and operates on a battery for multiple years. It is specifically designed for this use case.
- C is incorrect: Wi-Fi consumes 170–300 mA during active transmission and has range of 30–100 m. A battery-powered agricultural sensor using Wi-Fi would last days, not years.
- D is incorrect: Zigbee nodes relay through each other in a mesh but each hop is only 10–100 m. Covering several kilometers with Zigbee would require dozens of powered relay nodes, making it impractical for field sensor deployments.

---

## Question 2

Which of the following best defines an AWS IoT Core IoT Policy?

- A) A JWT signed with an RSA private key that authenticates a device to Google Cloud IoT Core over MQTT.
- B) A JSON document attached to an X.509 certificate specifying which MQTT actions a device is permitted to perform on which topic resources.
- C) A cloud-side JSON document with desired and reported sections that synchronizes configuration state between the cloud and an offline device.
- D) A managed container orchestration policy that scales IoT microservices in Kubernetes based on message volume.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: This describes GCP IoT Core's JWT authentication mechanism, not an AWS IoT Policy. AWS IoT Core uses X.509 mTLS, not JWT.
- B is correct: AWS IoT Policies use IAM-style JSON with Allow/Deny rules on IoT actions (iot:Connect, iot:Publish, iot:Subscribe, iot:Receive) and specific topic ARNs. They are attached to device certificates and evaluated on every connection and message operation.
- C is incorrect: This describes the AWS Device Shadow (or Azure Device Twin) state synchronization document, not an authorization policy.
- D is incorrect: Kubernetes scaling policies are unrelated to IoT device authorization on AWS IoT Core.

---

## Question 3

An IoT fleet provisions 50,000 sensors using one shared X.509 certificate with an IoT Policy granting `iot:*` on resource `*`. A single sensor is stolen and its certificate is extracted. What is the consequence?

- A) The attacker can only access the specific device shadow of the sensor from which the certificate was extracted.
- B) The attacker can publish and subscribe to any topic, impersonate any device, and access all device shadows until the certificate is manually revoked.
- C) AWS IoT Core automatically revokes the shared certificate when the device goes offline for more than 24 hours.
- D) The wildcard policy has no effect because AWS IoT Core enforces per-device topic isolation by default.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A shared certificate with a wildcard policy grants access to the entire broker namespace — all topics and all device shadows — not just the stolen device's shadow.
- B is correct: Sharing one certificate across 50,000 devices violates uniqueness and least-privilege. The wildcard `iot:*` on `*` gives the attacker unrestricted access to every action on every resource until an administrator manually revokes the certificate — which would simultaneously disconnect all 50,000 devices.
- C is incorrect: AWS IoT Core does not automatically revoke certificates based on offline duration. Certificate revocation requires an explicit administrative action.
- D is incorrect: Topic isolation is not enforced automatically. It must be explicitly configured in the IoT Policy using device-specific ARNs with `${iot:ClientId}` substitution.

---

## Question 4

A device on Azure IoT Hub reconnects after being offline for 6 hours. During that time, an operator updated the device's desired configuration in the Device Twin. What happens when the device reconnects?

- A) The device receives an error because the Device Twin was modified offline, requiring a manual reset before reconnection.
- B) Azure IoT Hub discards the desired state changes to avoid conflicts with the device's reported state.
- C) The device retrieves a delta document containing only the properties that differ between desired and reported state, then applies the pending configuration.
- D) The device must request a full OTA firmware reflash before the Device Twin can synchronize.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Offline Device Twin modifications are intentional and supported. The twin is specifically designed to persist desired state during device outages.
- B is incorrect: Discarding desired changes would defeat the core purpose of Device Twins. The design goal is reliable delivery of configuration changes to intermittently connected devices.
- C is correct: The delta document contains only the properties where desired and reported values differ. The device applies these specific changes and then updates its reported state to confirm. Bandwidth is minimized because the entire twin document is not resent.
- D is incorrect: OTA firmware updates and Device Twin configuration synchronization are separate mechanisms. A Device Twin delta does not trigger a firmware reflash.

---

## Question 5

A GCP IoT Core deployment uses one RSA key pair for all 10,000 devices, and the Pub/Sub topic has public read access. Which two controls are the most effective remediations?

- A) Issue unique RSA or EC key pairs per device at provisioning, and restrict the Pub/Sub subscription to authorized service accounts only.
- B) Switch all devices from MQTT to HTTP transport, and enable Cloud Armor DDoS protection on the Pub/Sub endpoint.
- C) Rotate the shared RSA key pair every 30 days and keep the Pub/Sub topic public for downstream consumer access.
- D) Disable JWT authentication entirely and rely on TLS encryption alone for device identity.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: Unique per-device keys limit the blast radius of any individual compromise to that single device. Restricting Pub/Sub subscription to authorized service accounts prevents unauthorized parties from reading all telemetry. Both are required.
- B is incorrect: Switching transport protocols does not address the shared key or public topic vulnerabilities. Cloud Armor protects against volumetric attacks, not data exposure from misconfigured IAM.
- C is incorrect: Rotating a shared key still requires all 50,000 devices to be updated simultaneously — a massive operational burden. And keeping the topic public still exposes all telemetry to unauthorized readers.
- D is incorrect: TLS provides transport encryption but not device identity authentication. Removing JWT means any device with a valid TLS connection can impersonate any registered device.

---

## Question 6

What is the purpose of the `${iot:ClientId}` substitution variable in an AWS IoT Core Policy resource ARN?

- A) It inserts the AWS account ID into the topic ARN at policy evaluation time.
- B) It restricts the policy action to the specific client ID used in the current MQTT CONNECT packet, enforcing that each device can only access resources associated with its own identity.
- C) It is a placeholder that must be replaced manually with the device's Thing Name before the policy is attached to a certificate.
- D) It grants temporary elevated permissions to the device during initial provisioning.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The account ID is a static component of the ARN specified explicitly, not substituted from the client ID.
- B is correct: `${iot:ClientId}` is a policy variable that evaluates to the value of the client_id field in the device's MQTT CONNECT packet at runtime. When the policy specifies `arn:aws:iot:region:account:client/${iot:ClientId}`, each device can only connect using its own registered Client ID. Combined with a topic ARN like `topic/sensors/${iot:ClientId}/data`, the device can only publish to its own topic.
- C is incorrect: The variable is evaluated dynamically at runtime, not replaced statically when the policy is created. The same policy document with `${iot:ClientId}` works correctly for every device in a fleet.
- D is incorrect: Policy variables do not confer elevated permissions. They are a scoping mechanism that restricts, not expands, what a device can access.

---

## Question 7

Which Azure IoT Hub Device Twin section contains metadata about the device that is visible to cloud applications but NOT sent to the device?

- A) Desired properties
- B) Reported properties
- C) Tags
- D) Device state

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Desired properties are explicitly delivered to the device — they are the cloud-to-device configuration mechanism.
- B is incorrect: Reported properties are sent by the device to the cloud — they represent the device's current state.
- C is correct: Tags are a Device Twin section that is entirely managed by cloud applications and backend services. The device cannot read or write tags. They are used for fleet management queries: find all devices in building-B, or all devices with firmware older than version 2.0.
- D is incorrect: "Device state" is not a distinct section in the Azure Device Twin document. The three sections are tags, desired properties, and reported properties.

---

## Question 8

A developer building a GCP IoT Core device selects a 30-day JWT expiry to reduce how often the device must re-authenticate. What is the primary security risk of a long JWT expiry?

- A) Long-lived JWTs consume more bandwidth because they are larger token strings.
- B) If the device's private key is compromised, the attacker can generate valid JWTs for 30 days before the key can be rotated to invalidate them.
- C) GCP IoT Core automatically disconnects devices using JWTs older than 24 hours, making a 30-day expiry non-functional.
- D) Long JWT expiry causes clock skew errors in distributed systems that reject tokens with future timestamps.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: JWT token size is essentially fixed regardless of the expiry value (the exp claim is a small integer timestamp). Size is not the concern.
- B is correct: If a device private key is extracted (via physical firmware access or a software vulnerability), the attacker can create signed JWTs using that key. The key remains valid until the operator rotates it in the Device Registry. With a 30-day expiry, the attacker's JWTs are valid for up to 30 days from when they are generated, even after the key is rotated, unless the platform explicitly rejects them. Short expiry (24 hours or less) limits the attacker's window.
- C is incorrect: GCP IoT Core does not automatically disconnect devices on a 24-hour limit. The JWT expiry is developer-controlled. The security recommendation is to set it to 24 hours or less, but this is a best practice, not a platform enforcement.
- D is incorrect: Clock skew is a real concern for JWT validation, but it is handled by the JWT standard's tolerance window (typically a few minutes), not by expiry duration.

---

## Question 9

Which AWS IoT Core component evaluates incoming MQTT messages against SQL-like conditions and routes matching messages to downstream services like Lambda, DynamoDB, or SNS?

- A) Device Shadow service
- B) IoT Policy evaluator
- C) Rules Engine
- D) Certificate Manager

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The Device Shadow service manages the desired and reported state documents for each device. It does not route messages based on payload conditions.
- B is incorrect: The IoT Policy evaluator checks whether a device certificate is authorized to perform a specific MQTT action (Connect, Publish, Subscribe). It is an authorization control, not a message routing engine.
- C is correct: The AWS IoT Core Rules Engine listens to MQTT messages on specified topics, evaluates SQL-like conditions against the message payload, and routes matching messages to configured actions: DynamoDB writes, Lambda invocations, SNS notifications, Kinesis streams, S3 storage, and many others.
- D is incorrect: Certificate Manager (ACM) is an AWS service for managing TLS certificates for web applications. It is not the IoT message routing component.

---

## Question 10

Azure Device Provisioning Service (DPS) enables which capability for large IoT deployments?

- A) It automatically generates firmware update packages and deploys them to all registered devices simultaneously.
- B) It enables zero-touch device provisioning: devices arriving from the factory are automatically authenticated, assigned to the correct IoT Hub, and registered in the device registry on first boot without manual pre-configuration.
- C) It provides a managed database for storing all device telemetry with automatic partitioning by device ID and timestamp.
- D) It replaces the Device Twin by providing a serverless function that responds to device configuration requests in real time.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Firmware update management is handled by Azure IoT Hub's OTA update features, not by DPS. DPS handles initial device identity provisioning, not ongoing firmware distribution.
- B is correct: Azure DPS solves the provisioning at scale problem. A manufacturer ships thousands of devices without pre-configuring them for a specific IoT Hub endpoint. On first boot, the device contacts DPS, presents its attestation credential (X.509, TPM, or symmetric key), and DPS assigns it to the correct IoT Hub, registers its identity, and returns the connection endpoint — all without manual administrator intervention.
- C is incorrect: A managed time-series database is a different Azure service (Azure Data Explorer, Cosmos DB, or blob storage via IoT Hub message routing). DPS has no database storage function.
- D is incorrect: DPS does not replace Device Twins. Device Twins continue to manage ongoing desired and reported state synchronization for already-provisioned devices.

---

End of Quiz – Module 06
