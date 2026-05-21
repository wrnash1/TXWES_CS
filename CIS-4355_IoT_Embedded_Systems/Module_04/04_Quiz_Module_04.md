# Quiz: Module 04 - IoT Protocols – MQTT, CoAP, HTTP/REST, and Zigbee
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What is the communication pattern utilized in the MQTT protocol?
*   A) Client-Server HTTP request-response over TCP
*   B) Publish-Subscribe via a central broker
*   C) Peer-to-peer streaming with no intermediary
*   D) File transfer using FTP commands
*   **Correct Answer:** B) Clients publish data to topics on a central broker, which routes messages to all matching subscribers.
*   **Distractor Analysis:**
    *   *Why correct:* Clients publish data to topics on a central broker, which routes messages to subscribed clients without direct publisher-to-subscriber connections.
    *   HTTP uses a synchronous Request-Response pattern; MQTT's pub-sub model decouples senders from receivers.

---

**Question 2**
Which of the following is the most accurate definition of **CoAP (Constrained Application Protocol)**?
*   A) A lightweight publish-subscribe protocol running over TCP port 1883, designed for telemetry streaming from constrained IoT sensors to a central broker.
*   B) A request-response application protocol for constrained nodes running over UDP, secured with DTLS, and designed for machine-to-machine communication on low-power networks.
*   C) A mesh networking standard using IEEE 802.15.4 with 128-bit AES encryption, operating at 2.4 GHz for smart home sensor networks.
*   D) A binary serialization format used to compress JSON payloads before transmission over HTTPS from IoT devices to cloud APIs.
*   **Correct Answer:** B) A request-response application protocol for constrained nodes running over UDP, secured with DTLS, and designed for machine-to-machine communication on low-power networks.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes MQTT, not CoAP — MQTT uses TCP and pub-sub; CoAP uses UDP and request-response.
    *   *Why B is correct:* CoAP (RFC 7252) runs over UDP port 5683, uses GET/POST/PUT/DELETE like HTTP, and is secured with DTLS rather than TLS.
    *   *Why C is incorrect:* This describes Zigbee's IEEE 802.15.4 mesh networking, not CoAP.
    *   *Why D is incorrect:* This describes a serialization/compression concept, not a protocol.

---

**Question 3**
A fleet of 10,000 soil moisture sensors must send readings every 60 seconds over a cellular network with a 500-byte monthly data cap per SIM. Which protocol minimizes overhead best?
*   A) HTTP/REST with full JSON payloads and TLS over port 443.
*   B) MQTT with QoS 0 over TLS, publishing a compact binary payload to a shared topic.
*   C) CoAP with confirmable messages over DTLS, using URI query strings for each reading.
*   D) Zigbee mesh with a coordinator gateway forwarding to HTTP/REST cloud endpoints.
*   **Correct Answer:** B) MQTT with QoS 0 over TLS, publishing a compact binary payload to a shared topic.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* HTTP/REST has high per-request overhead (headers, status lines, JSON verbosity) that consumes bandwidth rapidly at scale.
    *   *Why B is correct:* MQTT QoS 0 has minimal framing overhead; compact binary payloads further reduce per-message bytes; TLS adds security without excessive overhead on modern networks.
    *   *Why C is incorrect:* CoAP confirmable messages add acknowledgement round-trips; URI query strings are verbose. CoAP is better suited for LAN/6LoWPAN than wide-area cellular.
    *   *Why D is incorrect:* Zigbee range is limited to ~100 m line-of-sight — unsuitable for geographically distributed field sensors.

---

**Question 4**
An administrator discovers that the company's MQTT broker accepts connections on port 1883 with no authentication and no TLS. Which two OWASP IoT Top 10 vulnerabilities does this represent?
*   A) Insecure data transfer and insecure network services.
*   B) Insecure default passwords and insufficient physical security.
*   C) Lack of secure update mechanism and insecure cloud interface.
*   D) Poor physical security and outdated components.
*   **Correct Answer:** A) Insecure data transfer and insecure network services.
*   **Distractor Analysis:**
    *   *Why A is correct:* No TLS means all telemetry is transmitted in cleartext (insecure data transfer); unauthenticated port 1883 is an open network service accepting any client (insecure network services).
    *   *Why B is incorrect:* Default passwords concern device login credentials, not transport encryption; physical security is unrelated to a network port configuration.
    *   *Why C is incorrect:* Secure update mechanism refers to OTA firmware signing; cloud interface refers to web APIs — neither matches a local broker misconfiguration.
    *   *Why D is incorrect:* Outdated components refers to unpatched software versions, not missing TLS configuration.

---

**Question 5**
When configuring a Mosquitto MQTT broker for production use, which combination of settings best hardens the deployment against unauthorized access?
*   A) Disable TLS to reduce CPU overhead, allow anonymous connections, and rely on firewall rules alone.
*   B) Enable TLS on port 8883 with a valid server certificate, require X.509 client certificates or username/password authentication, and apply per-topic ACLs.
*   C) Enable TLS on port 8883, allow anonymous read-only subscriptions, and restrict publishing to authenticated users only.
*   D) Use a self-signed certificate with no revocation checking, disable password authentication, and restrict access by IP address whitelist.
*   **Correct Answer:** B) Enable TLS on port 8883 with a valid server certificate, require X.509 client certificates or username/password authentication, and apply per-topic ACLs.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Firewall rules alone do not authenticate devices; disabling TLS exposes all messages to network eavesdropping.
    *   *Why B is correct:* TLS encrypts transport, client authentication prevents unauthorized devices from connecting, and ACLs enforce least-privilege access to sensitive topics.
    *   *Why C is incorrect:* Anonymous subscriptions allow any device to receive all published telemetry, violating confidentiality requirements.
    *   *Why D is incorrect:* IP whitelisting is easily bypassed by spoofing; no revocation checking means compromised certificates cannot be invalidated.
