# Reading Guide: Module 06 - IoT Cloud Platforms – AWS IoT Core, Azure IoT Hub, GCP IoT
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 06 – IoT Cloud Platforms: AWS IoT Core, Azure IoT Hub, and GCP IoT**! This module examines how IoT devices connect to and communicate with managed cloud platforms, and how those platforms handle device identity, message routing, state management, and security at scale. Selecting the right cloud platform and configuring it correctly is a critical architectural decision for any production IoT deployment.

You will learn how AWS IoT Core uses X.509 certificates and policy documents to authenticate millions of devices, how Azure IoT Hub's device twins maintain synchronized desired and reported state between cloud and edge, and how GCP IoT Core's Pub/Sub architecture decouples ingestion from processing. Security considerations — including certificate rotation, device policy least-privilege, and secure transport — are central to all three platforms.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AWS IoT Core**: Amazon's fully managed cloud service that enables billions of IoT devices to connect securely over MQTT or HTTPS. Each device authenticates using a unique X.509 client certificate bound to an IoT Policy document that controls which topics the device may publish or subscribe to. AWS IoT Core routes messages to downstream services (Lambda, S3, DynamoDB) via configurable Rules with SQL-like filter expressions.
*   **Azure IoT Hub**: Microsoft's managed service providing bidirectional communication between IoT devices and the cloud. IoT Hub supports MQTT, AMQP, and HTTPS transports and authenticates devices via SAS tokens or X.509 certificates stored in an Identity Registry. The **Device Twin** feature maintains a JSON document with "desired" (cloud-to-device target state) and "reported" (device-to-cloud actual state) sections, enabling reliable configuration synchronization without polling.
*   **GCP IoT Core (Cloud IoT Core)**: Google Cloud's device management service that uses JSON Web Tokens (JWTs) signed with RSA or EC keys for device authentication over MQTT or HTTP. Telemetry messages are published to Cloud Pub/Sub topics, which decouple device ingestion from downstream analytics pipelines in BigQuery or Dataflow.
*   **Device Shadow / Device Twin**: A cloud-side JSON representation of a device's current and desired state. When a device reconnects after being offline, it synchronizes its state with the shadow/twin, applying any pending configuration changes. This pattern eliminates the need for persistent device-to-cloud connections and enables reliable remote configuration of intermittently connected IoT nodes.
*   **X.509 Device Certificate**: A public-key certificate (based on the ITU-T X.509 standard) issued to an individual IoT device that proves its identity during the TLS handshake with the cloud broker. Each device receives a unique certificate and private key generated at provisioning time; the private key must be stored in a hardware secure element or TPM where possible. Certificate rotation — periodically issuing new certificates and revoking old ones — is required by IoT security best practices to limit the blast radius of a compromised device.

---

### 2. Certification Exam Tips
*   **Platform authentication comparison:** Memorize: AWS IoT Core = X.509 certificates + IoT Policy documents; Azure IoT Hub = X.509 certificates or SAS tokens + Identity Registry; GCP IoT Core = JWT signed with RSA/EC private key. Exam scenarios test which authentication mechanism belongs to which platform.
*   **Device Twin vs Shadow:** Azure calls it a "Device Twin"; AWS calls it a "Device Shadow"; GCP uses Device Manager state. All three maintain desired/reported state JSON — the concept is the same across platforms. Questions may swap these terms to test whether you understand the underlying pattern.
*   **Message routing:** AWS IoT Core uses Rules (SQL-like); Azure IoT Hub uses Message Routing with query syntax; GCP forwards to Cloud Pub/Sub. Know that all three support conditional filtering and fan-out to multiple downstream services.
*   **Least-privilege for IoT policies:** An IoT Policy (AWS) or device-level ACL should restrict each device to publishing and subscribing only to its own device-specific topics. A policy granting `iot:*` on `*` violates least-privilege and is a common exam distractor marked as incorrect.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insecure cloud interfaces — one of the OWASP IoT Top 10 items directly relevant to misconfigured AWS IoT policies, exposed Azure IoT Hub connection strings, and unauthenticated GCP Pub/Sub topics covered in this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the insecure cloud interface and insufficient privacy protection sections, which map directly to improperly secured AWS IoT, Azure IoT Hub, and GCP IoT deployments covered in this module.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of cloud platform connectivity patterns, device provisioning workflows, and comparing how major cloud providers handle IoT message ingestion and device state management.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Provision a simulated device on AWS IoT Core**: Use the AWS CLI or console to create a Thing, generate an X.509 certificate and key pair, attach an IoT Policy restricting publish/subscribe to `devices/{clientId}/#`, and connect a simulated MQTT client using the certificate to verify authentication.
*   **Demonstrate Device Shadow state synchronization**: Update the desired state of an AWS IoT Device Shadow via the console, then simulate a device reconnecting and reading the delta document to apply the pending configuration change.
*   **Compare platform authentication models**: Write a comparison table documenting the authentication mechanism, transport protocols, default port, and device state management approach for AWS IoT Core, Azure IoT Hub, and GCP IoT Core.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the insecure cloud interface section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the cloud platform connectivity sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Build the platform authentication comparison table before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
