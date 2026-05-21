# Reading Guide: Module 04 - IoT Protocols – MQTT, CoAP, HTTP/REST, and Zigbee
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 04 – IoT Protocols: MQTT, CoAP, HTTP/REST, and Zigbee**! This module examines the four most widely deployed IoT messaging and networking protocols. You will learn when to choose MQTT's publish-subscribe model for telemetry streaming, when CoAP's UDP-based request-response suits constrained devices, when HTTP/REST remains appropriate for cloud APIs, and how Zigbee's mesh topology enables dense, low-power sensor networks.

Protocol selection directly affects system security. MQTT without TLS exposes telemetry to eavesdropping; CoAP without DTLS is vulnerable to replay attacks; HTTP without HTTPS is trivially intercepted. Understanding each protocol's security model — default port, transport layer, and authentication mechanism — is essential for designing defensible IoT architectures.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Message Queuing Telemetry Transport (MQTT)**: A lightweight publish-subscribe messaging protocol designed for constrained devices and unreliable networks. MQTT clients connect to a central broker (default port 1883 for plain TCP, 8883 for TLS), publish messages to named topics, and subscribe to receive messages on topics of interest. Its small packet overhead makes it ideal for sensor telemetry over cellular or satellite links, but it must be secured with TLS and client certificate authentication to prevent unauthorized access.
*   **Publish-Subscribe Pattern**: A messaging pattern where senders (publishers) emit messages to a named channel (topic) without knowing which receivers will process them, and receivers (subscribers) register interest in topics without knowing which publishers will send. The broker decouples producers from consumers, enabling many-to-many communication with no direct connection between devices. This decoupling also means a compromised broker can intercept all messages on all topics.
*   **MQTT Broker**: The central server in an MQTT deployment that receives all published messages, maintains topic subscriptions, and routes messages to matching subscribers. Common implementations include Mosquitto (open source), HiveMQ, and AWS IoT Core. Broker security configuration — enforcing TLS, requiring username/password or X.509 certificates, and applying topic-level ACLs — is the single most important control point in an MQTT deployment.
*   **CoAP (Constrained Application Protocol)**: A specialized request-response protocol designed for machine-to-machine communication on constrained nodes and networks (RFC 7252). CoAP runs over UDP (default port 5683) rather than TCP, reducing connection overhead at the cost of requiring application-level retransmission logic. It maps closely to HTTP (GET, POST, PUT, DELETE methods) and is secured using DTLS (Datagram TLS) rather than standard TLS. CoAP is well-suited for sensors on 6LoWPAN/IEEE 802.15.4 networks where TCP overhead is prohibitive.
*   **Zigbee**: A low-power, low-data-rate wireless mesh networking standard (IEEE 802.15.4 PHY/MAC layer) operating in the 2.4 GHz band. Zigbee supports self-forming, self-healing mesh topologies where devices relay messages for each other, extending range without infrastructure. It uses 128-bit AES encryption for network-layer security. Common in smart home automation (Philips Hue, SmartThings), industrial sensor networks, and building automation systems.

---

### 2. Certification Exam Tips
*   **Protocol comparison matrix:** Memorize the key differentiators — MQTT: TCP/pub-sub/broker-mediated/port 1883; CoAP: UDP/request-response/peer-to-peer/port 5683; HTTP: TCP/request-response/stateless/port 80 or 443; Zigbee: IEEE 802.15.4/mesh/AES-128/2.4 GHz. Exam scenarios test which protocol fits a given constraint (power, bandwidth, latency, mesh topology).
*   **Default ports matter:** Know that MQTT plain = 1883, MQTT over TLS = 8883, CoAP = 5683, CoAP over DTLS = 5684, HTTP = 80, HTTPS = 443. Firewall and ACL questions depend on these.
*   **QoS levels in MQTT:** MQTT defines three Quality of Service levels — QoS 0 (at most once, fire-and-forget), QoS 1 (at least once, acknowledged), QoS 2 (exactly once, four-way handshake). Higher QoS consumes more bandwidth and adds latency.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insecure network services and unencrypted communications — two OWASP IoT Top 10 items that directly result from misconfigured MQTT brokers and unencrypted CoAP deployments.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the insecure network services and unencrypted data transfer sections, which map directly to improperly secured MQTT, CoAP, and Zigbee deployments covered in this module.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) demonstrates configuring a Mosquitto MQTT broker, publishing and subscribing to topics using `mosquitto_pub` / `mosquitto_sub`, and comparing CoAP and HTTP request-response patterns on IoT hardware.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a local MQTT broker (Mosquitto) server**: Install Mosquitto, edit `mosquitto.conf` to require password authentication and enable TLS on port 8883, generate a self-signed CA and server certificate, and verify the broker starts cleanly with `systemctl status mosquitto`.
*   **Publish sensor message packets using CLI commands**: Use `mosquitto_pub -h localhost -t "sensors/temperature" -m "23.5" -u user -P password --cafile ca.crt` to publish a TLS-authenticated message, and verify it is received by a subscriber on the same topic.
*   **Subscribe client to topics**: Open a second terminal running `mosquitto_sub -h localhost -t "sensors/#" --cafile ca.crt` and observe wildcard topic matching, then attempt a connection without credentials to confirm the broker rejects unauthenticated clients.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the insecure network services section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the MQTT and protocol comparison sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review the Mosquitto configuration steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
