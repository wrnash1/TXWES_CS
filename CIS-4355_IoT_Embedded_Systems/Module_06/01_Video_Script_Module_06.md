# Video Script – Module 06: IoT Cloud Platforms – AWS IoT Core, Azure IoT Hub, GCP IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** CompTIA IoT+ Domain 4 – Cloud and Data Management

---

## Segment 1: Introduction and Learning Objectives [00:00 – 02:00]

Welcome to Module 06. I am Professor Nash. We have covered IoT architecture, hardware, programming, protocols, and wireless networks. Now we move to the cloud side — the platforms that manage thousands or millions of devices, receive their telemetry, and connect IoT data to business applications.

The three dominant IoT cloud platforms are AWS IoT Core, Azure IoT Hub, and Google Cloud IoT. Each has a distinct architecture but shares common concepts: device registration, certificate-based authentication, MQTT ingestion, device shadow or digital twin state synchronization, and integration with cloud analytics pipelines.

By the end of this video you will be able to:

- Describe the core components of AWS IoT Core including Things, Certificates, Policies, and Device Shadows.
- Describe the core components of Azure IoT Hub including Device Twins, Message Routing, and IoT Edge.
- Describe how GCP IoT Core uses JWT authentication and Pub/Sub for telemetry routing.
- Compare the three platforms on authentication method, state synchronization model, and downstream integration.
- Identify the security risks associated with shared device certificates and wildcard IoT policies.

---

## Segment 2: Why Managed IoT Platforms? [02:00 – 04:30]

[SHOW DIAGRAM]

Before we look at specific platforms, let us answer the fundamental question: why use a managed IoT platform at all instead of running your own MQTT broker?

At 10 devices, a self-hosted Mosquitto broker on a small virtual machine works fine. At 10,000 devices, you are managing TLS certificate rotation, broker scaling, connection limits, message queuing, replay attack prevention, and integration with databases and analytics pipelines. At 10 million devices, a self-hosted solution requires a dedicated engineering team and massive infrastructure investment.

Managed IoT platforms handle all of that. They provide:

- Horizontally scalable MQTT ingestion with no practical connection limits.
- Certificate lifecycle management: provisioning, rotation, revocation.
- Device state synchronization through shadow and twin documents.
- Rule engines that route telemetry to databases, serverless functions, analytics pipelines, and other cloud services.
- Global availability and disaster recovery without customer-managed infrastructure.

The tradeoff: vendor lock-in and ongoing per-message and per-device costs.

---

## Segment 3: AWS IoT Core [04:30 – 09:30]

[SHOW DIAGRAM]

AWS IoT Core is Amazon Web Services' managed IoT ingestion platform and is among the most widely deployed enterprise IoT platforms globally.

### Things and the Registry

A Thing is a representation of a physical device in AWS IoT Core. The Things Registry stores metadata about each device: thing name, thing type, attributes such as location, model, and firmware version. Each Thing has a unique Thing Name used as the MQTT client ID and in topic patterns.

### Certificates and Authentication

AWS IoT Core uses mutual TLS with X.509 certificates for device authentication. Every device has its own unique certificate and private key. The certificate is presented during the TLS handshake. AWS IoT Core verifies it against a registered Certificate Authority.

This is critical: every device must have a unique certificate. Sharing a single certificate across multiple devices is a severe security failure. If that shared certificate is compromised, every device using it must be immediately deprovisioned and re-credentialed.

### IoT Policies

An IoT Policy is a JSON document attached to a certificate that specifies what MQTT actions the device is authorized to perform. It uses IAM-style Allow and Deny rules.

A secure per-device policy allows: Connect where the client ID matches the device Thing Name, Publish on the specific topic for this device only, Subscribe and Receive on the specific shadow delta topic for this device only.

A common security mistake: using wildcard policies that allow `iot:*` on resource `*`, giving every device unrestricted access to every topic on the broker. One stolen certificate then compromises the entire fleet.

### Device Shadow

The Device Shadow is a JSON document that maintains the current and desired state of a device. It has two sections:

The desired section: state set by the cloud application or operator, such as a target sampling rate or a firmware version to install.

The reported section: state last reported by the device, such as current sensor reading or current firmware version installed.

When a device is offline and the desired state is updated, the shadow persists the change. When the device reconnects, it receives a delta document containing only the properties where desired and reported differ. The device then applies the pending changes and updates the reported state.

This solves the problem of reliable configuration delivery to intermittently connected devices — a core IoT operational challenge.

### Rules Engine

The Rules Engine listens to incoming MQTT messages and routes them to other AWS services based on SQL-like conditions. Examples: if a temperature reading exceeds a threshold, invoke a Lambda function to send an alert; write all telemetry to a DynamoDB table or Timestream time-series database; route critical events to SNS for notification.

---

## Segment 4: Azure IoT Hub [09:30 – 14:00]

[SHOW DIAGRAM]

Azure IoT Hub is Microsoft's managed IoT platform, tightly integrated with the Azure ecosystem.

### Device Identity and Authentication

Azure IoT Hub supports three authentication methods:

X.509 certificates (recommended for production): the same mutual TLS model as AWS IoT Core.

SAS tokens (Shared Access Signatures): HMAC-SHA256 tokens with configurable expiry. Easier to generate on constrained devices but require careful rotation management. Do not set SAS token expiry beyond 24 hours for production deployments.

TPM attestation: used with Azure Device Provisioning Service for zero-touch provisioning at scale. The device's hardware TPM holds credentials that cannot be extracted.

### Device Twin

The Azure IoT Hub Device Twin is conceptually equivalent to AWS Device Shadow. It is a JSON document with three sections:

Tags: metadata set by the cloud application, not visible to the device. Used for fleet management queries — for example, query all devices in building-A with firmware version older than 2.0.

Desired properties: configuration values set by the cloud application, delivered to the device.

Reported properties: current state reported by the device.

The Device Twin persists across device disconnections. On reconnect, the device receives the delta between its last reported state and the current desired properties, applying any pending configuration changes.

### Message Routing

Azure IoT Hub's message routing engine directs incoming telemetry to multiple endpoints simultaneously based on message content conditions. Common endpoints: Azure Event Hubs for stream analytics, Azure Service Bus for enterprise messaging, Azure Storage for cold archiving, and Event Grid for serverless function triggers.

### Azure IoT Edge

Azure IoT Edge is Azure's edge computing runtime, allowing cloud-managed Docker container modules to run on gateway devices. IoT Edge handles local message routing between edge modules, cloud synchronization of module configurations, offline operation with local caching, and OTA updates of edge modules from the cloud.

---

## Segment 5: Google Cloud IoT Core [14:00 – 17:30]

[SHOW DIAGRAM]

GCP IoT Core is Google Cloud's managed IoT ingestion service. Its primary distinguishing feature is JWT-based device authentication rather than mTLS.

### JWT Authentication

Instead of mutual TLS with X.509 certificates, GCP IoT Core uses JWT (JSON Web Tokens) signed with an RSA or Elliptic Curve private key held by the device. The device generates a signed JWT and presents it as the MQTT password field during connection. GCP IoT Core verifies the JWT signature using the device's registered public key.

JWT authentication is lighter weight than full mTLS — the TLS handshake is faster and does not require a CA infrastructure. However, JWTs expire (recommended: 24 hours or less), requiring devices to generate and submit a new JWT periodically.

The security concern: if the JWT private key is extracted from device firmware (for example, by an attacker with physical access), the attacker can generate valid JWTs indefinitely until the key is manually rotated in the Device Registry.

### Pub/Sub Integration

GCP IoT Core routes all device telemetry to Google Cloud Pub/Sub topics. Pub/Sub provides durable, scalable, at-least-once message delivery. Downstream consumers subscribe to Pub/Sub topics: Cloud Functions for event-driven processing, BigQuery for analytics, Dataflow for stream processing.

The security risk: if a Pub/Sub topic subscription is misconfigured with public read access, all device telemetry is readable by any authenticated Google Cloud account. Always restrict Pub/Sub subscriptions to specific authorized service accounts.

### Device Registry and State

GCP IoT Core's Device Registry manages device configurations (delivered to the device) and device states (reported by the device). Conceptually equivalent to AWS Device Shadow and Azure Device Twin.

---

## Segment 6: Cloud Platform Security Comparison [17:30 – 20:00]

[SHOW DIAGRAM]

Let me summarize the key security controls and risks across all three platforms.

Authentication: AWS uses mTLS with X.509. Azure uses X.509, SAS tokens, or TPM. GCP uses JWT with RSA or EC keys. All three require per-device unique credentials.

Transport: all three use TLS on MQTT port 8883 or HTTPS port 443. This is non-negotiable.

Authorization: AWS uses IAM-style IoT Policies attached to certificates. Azure uses connection string access policies and shared access policies. GCP uses IAM roles on device registries and Pub/Sub topics.

The universal critical principle: unique credentials per device with least-privilege policies limiting each device to its own topics and state documents only.

Common security failures:

- Shared device certificates across a fleet (one stolen cert compromises all devices).
- Wildcard authorization policies giving every device full broker access.
- Private keys stored in plaintext in firmware (OWASP IoT #1 and #7).
- JWT expiry set to months rather than hours.
- Pub/Sub or Event Hub endpoints with public read access.

---

## Segment 7: Summary and Lab Preview [20:00 – 22:00]

AWS IoT Core uses mutual TLS with X.509, IoT Policies for authorization, Device Shadows for state synchronization, and a Rules Engine for downstream routing.

Azure IoT Hub uses X.509 or SAS token authentication, Device Twins with tags and desired and reported properties, Message Routing to Azure services, and IoT Edge for edge compute orchestration.

GCP IoT Core uses JWT authentication with RSA or EC keys, routes to Pub/Sub for downstream consumers, and manages device configuration and state through a Device Registry.

All three share the same security principles: unique per-device credentials, TLS transport, and least-privilege access policies.

In this week's lab you will analyze AWS IoT Core policy documents for security violations, trace a Device Shadow synchronization sequence, and evaluate a GCP Pub/Sub access configuration for data exposure risks.

See you in Module 07 where we integrate real sensors end-to-end.

---

End of Module 06 Video Script
