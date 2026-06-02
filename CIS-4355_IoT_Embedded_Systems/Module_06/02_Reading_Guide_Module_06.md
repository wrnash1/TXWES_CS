# Reading Guide – Module 06: IoT Cloud Platforms – AWS IoT Core, Azure IoT Hub, GCP IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Certification Target:** CompTIA IoT+ Domain 4

---

## Introduction

Module 06 examines managed IoT cloud platforms: how devices connect to them, how they authenticate at scale, how device state is synchronized between cloud and device, and how telemetry is routed to downstream analytics services. These platforms represent the Processing and Application layers of IoT architecture operating at cloud scale. Security configuration of cloud IoT platforms is a common CompTIA IoT+ exam topic and a critical real-world skill.

---

## 1. Core Glossary

- **AWS IoT Core:** Amazon's managed IoT platform providing MQTT and HTTPS device endpoints, X.509 certificate-based mutual TLS authentication, IoT Policies for authorization, Device Shadows for state management, and a Rules Engine for telemetry routing.

- **Thing (AWS IoT):** A digital representation of a physical device in the AWS IoT Registry. Has a unique Thing Name, optional Thing Type, and custom attributes. The Thing Name is typically used as the MQTT Client ID and in topic patterns.

- **X.509 Certificate (IoT):** A public-key certificate binding a public key to a device identity. Used in mutual TLS (mTLS) authentication where both the server and the device present certificates. In AWS IoT Core, each device requires a unique certificate. The certificate's associated private key is stored securely on the device.

- **IoT Policy (AWS):** A JSON authorization document attached to an X.509 certificate specifying permitted IoT actions (iot:Connect, iot:Publish, iot:Subscribe, iot:Receive) on specific topic resources. Follows IAM Allow/Deny syntax. Least-privilege policies restrict each device to only its own topics.

- **Device Shadow (AWS IoT):** A persistent JSON document in AWS IoT Core representing a device's current state. Contains `desired` (target state set by cloud) and `reported` (state reported by device) sections. A delta document sent to the device on reconnect contains the diff between desired and reported.

- **Rules Engine (AWS IoT):** A SQL-based engine that evaluates incoming MQTT messages and routes them to AWS services: DynamoDB, Lambda, S3, SNS, Kinesis, Timestream, and others based on topic and payload conditions.

- **Azure IoT Hub:** Microsoft's managed IoT platform providing device identity, authentication (X.509, SAS tokens, TPM), Device Twins, message routing to Azure services, and IoT Edge orchestration.

- **SAS Token (Azure):** Shared Access Signature token for Azure IoT Hub device authentication. HMAC-SHA256 signed with a device-specific key and includes an expiry timestamp. Easier to generate on constrained devices than X.509 mTLS but must be rotated before expiry.

- **Device Twin (Azure):** Azure IoT Hub's device state document. Contains Tags (cloud metadata, not visible to device), Desired properties (cloud-to-device configuration), and Reported properties (device-to-cloud current state). Persists across device offline periods.

- **IoT Edge (Azure):** Azure's edge compute runtime. Runs Docker container modules on gateway devices. Supports offline operation, local message routing, and cloud-managed module deployment via the IoT Hub.

- **GCP IoT Core:** Google Cloud's managed IoT ingestion service. Uses JWT authentication signed with device RSA or EC private keys. Routes telemetry to Google Cloud Pub/Sub. Device Registry manages device configuration and state.

- **JWT (JSON Web Token):** A compact, URL-safe token format for authentication. In GCP IoT Core, the device signs a JWT with its private RSA or EC key and presents it as the MQTT password. GCP verifies the signature using the registered public key. JWTs include an expiry claim (exp) and must be renewed periodically.

- **Google Cloud Pub/Sub:** Google Cloud's fully managed message-passing service. In GCP IoT Core deployments, all device telemetry is published to a Pub/Sub topic. Subscribers (Cloud Functions, Dataflow, BigQuery) consume messages asynchronously with at-least-once delivery.

- **Device Provisioning Service (DPS):** Azure's zero-touch device provisioning service. Automates the enrollment, authentication, and assignment of new devices to IoT Hubs at scale. Supports X.509, TPM, and symmetric key attestation.

- **Mutual TLS (mTLS):** A TLS configuration where both the client (device) and server (cloud endpoint) present and verify X.509 certificates. Provides two-way authentication: the device knows it is talking to the legitimate cloud endpoint, and the cloud endpoint knows which registered device is connecting.

---

## 2. IoT Protocol Comparison Table

| Attribute | MQTT | CoAP | HTTP/REST | AMQP |
|---|---|---|---|---|
| Transport | TCP | UDP | TCP | TCP |
| Pattern | Publish/subscribe | Request/response | Request/response | Queue + pub/sub |
| Cloud platform support | All three platforms | GCP IoT (HTTP bridge) | All three (HTTP bridge) | Azure Service Bus |
| Authentication on AWS | mTLS (port 8883) | N/A | mTLS or SigV4 | N/A |
| Authentication on Azure | X.509 / SAS (8883) | N/A | SAS token (443) | SAS (5671) |
| Authentication on GCP | JWT password (8883) | N/A | JWT Bearer (443) | N/A |

---

## 3. Cloud Platform Comparison Table

| Feature | AWS IoT Core | Azure IoT Hub | GCP IoT Core |
|---|---|---|---|
| Authentication | mTLS X.509 | X.509 / SAS token / TPM | JWT (RSA or EC) |
| Authorization | IoT Policy (IAM JSON) | Shared access policies | IAM roles on registry |
| State sync document | Device Shadow | Device Twin | Device Configuration |
| State sections | desired / reported | tags / desired / reported | config / state |
| Rules/routing engine | Rules Engine (SQL) | Message Routing (conditions) | Pub/Sub + Cloud Functions |
| Edge compute | Greengrass | IoT Edge (Docker modules) | Cloud IoT Edge |
| Primary downstream | Lambda, DynamoDB, Kinesis | Event Hubs, Service Bus, Storage | Pub/Sub, BigQuery, Dataflow |
| Multi-region | AWS global regions | Azure global regions | GCP global regions |
| Zero-touch provisioning | Fleet Provisioning | DPS (Device Provisioning Service) | Manual or CA-signed certificates |

---

## 4. OWASP IoT Top 10 Reference

Items most relevant to cloud platform configuration:

1. **OWASP IoT #1 – Weak, Guessable, or Hardcoded Passwords:** Private keys or SAS token strings hardcoded in firmware. Extractable via firmware binary analysis. Mitigation: use hardware secure elements or TPM to protect private keys.

2. **OWASP IoT #2 – Insecure Network Services:** IoT broker endpoints accessible without authentication (anonymous MQTT). Mitigation: disable anonymous access; require certificate or JWT authentication on all cloud platform endpoints.

3. **OWASP IoT #3 – Insecure Ecosystem Interfaces:** Overly permissive IoT Policies or Pub/Sub access controls. A wildcard policy allowing `iot:*` on `*` gives any device full broker access. Mitigation: scope every policy to the specific thing name and topic.

4. **OWASP IoT #7 – Insecure Data Transfer and Storage:** Devices connecting over HTTP port 80 (not 443) or MQTT port 1883 (not 8883). Private keys stored unencrypted in flash. Mitigation: enforce TLS for all connections; store keys in secure elements.

---

## 5. Sensor Types Reference

Sensors relevant to cloud platform integration (what gets published):

| Sensor | Data Published | Cloud Routing Example |
|---|---|---|
| Temperature | Celsius float, timestamp | Rules Engine to DynamoDB time-series |
| GPS | Lat/lon/altitude, speed | IoT Core to Lambda for geofence check |
| Current/power | Watts, kWh | IoT Hub to Event Hub for billing analytics |
| Door lock state | Boolean open/closed | Device Shadow desired/reported |
| Air quality (CO2, PM2.5) | PPM float values | Pub/Sub to BigQuery for long-term trend |
| Smart meter | kWh reading, demand | IoT Hub to blob storage for regulatory archival |

---

## 6. IIoT Purdue Model Reference

Cloud platforms map to the upper Purdue levels:

- Level 3.5 DMZ: Protocol translation from OT protocols to cloud MQTT.
- Level 4: Business logistics – ERP systems consuming IoT telemetry from IoT Hub via Service Bus.
- Level 5: Enterprise / cloud – AWS IoT Core, Azure IoT Hub, GCP IoT Core operating here.

The industrial DMZ is the security boundary between OT device networks and cloud-connected IT systems. All traffic from OT levels to cloud must pass through the DMZ for inspection.

---

## 7. Exam Tips for Module 06

1. AWS IoT Core uses X.509 certificates with mTLS. GCP IoT Core uses JWT signed with device private key. Azure IoT Hub supports X.509, SAS tokens, and TPM. Know the authentication method for each platform.

2. A Device Shadow (AWS) and Device Twin (Azure) both have desired and reported sections. The delta document delivered on reconnect contains only the diff — not the full document. This minimizes bandwidth.

3. An IoT Policy with `iot:*` on resource `*` is the most dangerous misconfiguration in AWS IoT Core. It gives any connected device unrestricted access to all topics and all device shadows.

4. SAS tokens in Azure have an expiry timestamp. If the token expires while the device is offline, the device must generate a new token before reconnecting. Set SAS token expiry to 24 hours or less in production.

5. GCP Pub/Sub topics must have IAM-restricted subscriptions. A publicly readable Pub/Sub subscription exposes all IoT telemetry to any authenticated Google Cloud user.

6. Each device must have a unique certificate or key pair. Sharing one certificate across an entire fleet means one stolen device compromises the credentials of all devices until the shared certificate is revoked.

7. AWS IoT Core Fleet Provisioning and Azure DPS both enable zero-touch device onboarding at scale. Devices arrive from the factory without pre-registered identities and claim their permanent credentials on first boot.

8. The Rules Engine (AWS) and Message Routing (Azure) enable fan-out: one incoming MQTT message can simultaneously trigger a Lambda function, write to a database, and post to a notification queue. This fan-out happens in the cloud without any device-side code change.

---

## 8. Study Checklist

- [ ] Memorize all 16 glossary terms with particular focus on IoT Policy, Device Shadow, Device Twin, and JWT.
- [ ] Study the cloud platform comparison table and be able to state the authentication method and state sync document name for each platform.
- [ ] Review the four OWASP items and connect each to a specific cloud platform misconfiguration.
- [ ] Review the exam tips and confirm you can explain each without notes.
- [ ] Complete the Module 06 Lab.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 9. Official References

- AWS IoT Core documentation at docs.aws.amazon.com/iot
- Azure IoT Hub documentation at learn.microsoft.com/azure/iot-hub
- OWASP IoT Security Project at owasp.org/www-project-internet-of-things

---

End of Reading Guide – Module 06
