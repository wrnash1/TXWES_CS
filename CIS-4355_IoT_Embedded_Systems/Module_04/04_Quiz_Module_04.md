# Quiz – Module 04: IoT Protocols – MQTT, CoAP, HTTP/REST, and Zigbee

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Format:** 10 questions, multiple choice, 4 options each
**Certification Alignment:** CompTIA IoT+ Domain 3

---

## Question 1

Which communication pattern does MQTT use?

- A) Client-server request-response over TCP with full HTTP headers.
- B) Publish-subscribe via a central broker that decouples senders from receivers.
- C) Peer-to-peer direct socket streaming with no intermediary.
- D) File transfer using FTP-style commands over port 21.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Request-response with HTTP headers describes HTTP/REST, not MQTT. MQTT's key innovation is the pub/sub model and its minimal framing overhead.
- B is correct: MQTT publishers send messages to topics on a broker without addressing specific subscribers. Subscribers register interest in topics. The broker routes messages to all matching subscribers, decoupling senders from receivers completely.
- C is incorrect: MQTT requires a central broker. There is no direct publisher-to-subscriber connection.
- D is incorrect: FTP is a completely different protocol for file transfer. MQTT does not use FTP semantics.

---

## Question 2

Which of the following best defines CoAP (Constrained Application Protocol)?

- A) A lightweight pub/sub protocol running over TCP port 1883, designed for telemetry streaming to a central broker.
- B) A request-response application protocol for constrained nodes running over UDP, secured with DTLS, using GET/POST/PUT/DELETE methods.
- C) A mesh networking standard using IEEE 802.15.4 with AES-128 encryption at 2.4 GHz.
- D) A binary serialization format for compressing JSON payloads before HTTPS transmission.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: This describes MQTT — TCP, port 1883, pub/sub, broker. CoAP uses UDP and request-response, not TCP and pub/sub.
- B is correct: CoAP (IETF RFC 7252) runs over UDP port 5683 (DTLS port 5684), uses the same HTTP-like methods, and is specifically designed for constrained devices on constrained networks.
- C is incorrect: This describes the physical layer of Zigbee (IEEE 802.15.4). Zigbee is a network protocol, not an application protocol.
- D is incorrect: A compression or serialization format (like CBOR or MessagePack) is not a protocol. CoAP is a transport-layer application protocol, not a data encoding format.

---

## Question 3

A fleet of 10,000 soil moisture sensors sends readings every 60 seconds over cellular LTE-M with a strict 500-byte monthly data budget per SIM. Which protocol choice minimizes per-reading overhead?

- A) HTTP/REST with full JSON payloads and TLS over port 443.
- B) MQTT QoS 0 over TLS with a compact binary payload.
- C) CoAP Confirmable (CON) over DTLS with URI query strings per reading.
- D) Zigbee mesh with a coordinator forwarding to HTTP/REST cloud endpoints.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: HTTP/REST adds significant per-request overhead through status lines, multiple headers, and verbose JSON text. This would consume the data budget rapidly at scale.
- B is correct: MQTT QoS 0 has the smallest protocol framing overhead. A compact binary or minimal JSON payload further reduces bytes per message. TLS adds encryption without prohibitive overhead on LTE-M.
- C is incorrect: CoAP CON messages add acknowledgment round-trips. URI query strings are text-based and relatively verbose. CoAP is better suited for local 6LoWPAN networks than wide-area cellular.
- D is incorrect: Zigbee range is 10–100 meters line-of-sight. Field sensors distributed across thousands of acres cannot reach a Zigbee coordinator. Zigbee is a local-area mesh protocol, not a wide-area one.

---

## Question 4

An administrator finds the company MQTT broker accepting connections on port 1883 with no authentication and no TLS. Which OWASP IoT Top 10 items does this violate?

- A) OWASP IoT #4 (Lack of Secure Update) and #10 (Lack of Physical Hardening).
- B) OWASP IoT #2 (Insecure Network Services) and #7 (Insecure Data Transfer and Storage).
- C) OWASP IoT #1 (Weak Passwords) and #5 (Outdated Components).
- D) OWASP IoT #6 (Insufficient Privacy) and #8 (Lack of Device Management).

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: OWASP IoT #4 is about insecure firmware update channels. #10 is about physical debug port exposure. Neither maps to a misconfigured MQTT broker port.
- B is correct: An unauthenticated broker on port 1883 is OWASP IoT #2 — an unnecessary open network service accepting any connection. Transmitting telemetry over port 1883 without TLS is OWASP IoT #7 — insecure data in transit.
- C is incorrect: OWASP IoT #1 is about device credential hardcoding. #5 is about unpatched software components. A missing authentication configuration is a different category than weak or hardcoded passwords.
- D is incorrect: OWASP IoT #6 relates to personal data privacy. #8 relates to missing remote management. Neither directly describes an open, unauthenticated broker port.

---

## Question 5

When configuring a Mosquitto MQTT broker for production, which combination of settings provides the best security posture?

- A) Disable TLS to reduce CPU overhead, allow anonymous connections, and rely on firewall rules only.
- B) Enable TLS on port 8883, require X.509 client certificates or username/password authentication, and apply per-topic ACLs.
- C) Enable TLS on port 8883, allow anonymous read-only subscriptions, and restrict publishing to authenticated users.
- D) Use a self-signed certificate, disable password authentication, and restrict access by static IP whitelist.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Firewall rules alone cannot authenticate individual IoT devices. Disabling TLS exposes all telemetry to eavesdropping by anyone on the same network segment.
- B is correct: TLS encrypts all traffic. Client authentication (certificates or credentials) ensures only authorized devices can connect. Per-topic ACLs enforce least-privilege — a temperature sensor should only be able to publish to its own topic, not subscribe to other devices' topics.
- C is incorrect: Anonymous read-only subscriptions allow any unauthorized device to receive all telemetry, violating confidentiality. An attacker can harvest all sensor data without publishing anything.
- D is incorrect: IP address whitelisting is trivially bypassed by IP spoofing. Self-signed certificates with no revocation checking mean a compromised device certificate cannot be invalidated.

---

## Question 6

What does the MQTT `#` wildcard character match when used in a subscription topic?

- A) Exactly one topic level at the position where `#` appears.
- B) The literal hash character in a topic name.
- C) All remaining topic levels from the position where `#` appears, including all nested sub-levels.
- D) Any single alphanumeric character within a single topic level.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Matching exactly one level is the behavior of the `+` wildcard, not `#`.
- B is incorrect: In MQTT topic strings, `#` is a reserved wildcard character, not a literal character. A topic cannot contain a literal hash unless used as a wildcard at the end.
- C is correct: The `#` wildcard matches zero or more topic levels from its position to the end. For example, `campus/#` matches `campus/building-a`, `campus/building-a/floor-2`, and `campus/building-a/floor-2/sensor-05/co2`. It must appear only at the end of the topic filter.
- D is incorrect: Matching a single character within a level is not a feature of standard MQTT wildcards. Both `+` and `#` match complete levels, not individual characters.

---

## Question 7

In a Zigbee network, which device role is solely responsible for initializing the network, maintaining the global routing table, and distributing encryption keys as the Trust Center?

- A) Zigbee End Device
- B) Zigbee Router
- C) Zigbee Coordinator
- D) Zigbee Gateway

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: A Zigbee End Device is a leaf node — typically a battery-powered sensor. It cannot route traffic and cannot initialize a network. It only communicates with its parent router or coordinator.
- B is incorrect: A Zigbee Router relays messages to extend network range but does not initialize the network. Multiple routers can exist in one network.
- C is correct: The Zigbee Coordinator is the single authoritative node in each Zigbee network. It starts the network on a selected channel and PAN ID, manages the routing table, and acts as the Trust Center distributing the network encryption key.
- D is incorrect: A Zigbee Gateway is an informal term for a device that bridges a Zigbee network to an IP network (for example, Zigbee to MQTT). This is a broader architectural role, not one of the three Zigbee protocol device types.

---

## Question 8

Which transport protocol does CoAP use, and what security protocol secures CoAP in production deployments?

- A) TCP; TLS (Transport Layer Security)
- B) UDP; DTLS (Datagram Transport Layer Security)
- C) TCP; DTLS
- D) UDP; TLS

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: CoAP runs over UDP, not TCP. Using TLS with CoAP would require TCP, which defeats CoAP's design purpose of avoiding TCP overhead on constrained networks.
- B is correct: CoAP is built on UDP to minimize connection overhead on constrained networks. DTLS is the datagram-oriented adaptation of TLS that provides encryption and authentication for UDP-based protocols. CoAP over DTLS uses port 5684.
- C is incorrect: CoAP does not use TCP. TCP is used by MQTT and HTTP, not CoAP.
- D is incorrect: TLS is designed for TCP stream transports. It cannot be used directly with UDP. DTLS is the correct pairing for UDP-based protocols like CoAP.

---

## Question 9

An IoT device must subscribe to resource updates on a CoAP server and receive push notifications when the resource value changes, without polling. Which CoAP extension enables this behavior?

- A) CoAP Block-Wise Transfer (RFC 7959)
- B) CoAP Observe extension (RFC 7641)
- C) CoAP Multicast (RFC 7390)
- D) CoAP DTLS handshake caching

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Block-Wise Transfer (RFC 7959) enables large resource transfers by splitting them into blocks. It addresses payload size, not subscription or push notification.
- B is correct: The CoAP Observe extension (RFC 7641) allows a CoAP client to register as an observer of a resource. The server then sends notifications to the observer each time the resource state changes, without the client needing to poll. This provides MQTT subscribe-like behavior over CoAP.
- C is incorrect: CoAP Multicast (RFC 7390) allows one CoAP message to be delivered to multiple endpoints simultaneously. It addresses group communication, not individual resource subscriptions.
- D is incorrect: DTLS handshake caching is a performance optimization for repeated connections, not a subscription mechanism.

---

## Question 10

AMQP is described as an enterprise-grade IoT backend messaging protocol. Which of the following statements about AMQP is accurate?

- A) AMQP runs over UDP and is suitable for deployment directly on Arduino Uno microcontrollers.
- B) AMQP is a publish-subscribe and message-queue protocol over TCP used in enterprise IoT backends, typically bridged from MQTT via a gateway.
- C) AMQP uses AES-128 mesh encryption and operates at 2.4 GHz in the ISM band.
- D) AMQP replaces MQTT in all deployments because it has lower per-message overhead.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: AMQP runs over TCP (port 5672 plain, 5671 TLS). It is not designed for constrained devices. An Arduino Uno lacks the resources and TCP stack needed for AMQP.
- B is correct: AMQP is an OASIS standard enterprise messaging protocol supporting both publish-subscribe and guaranteed-delivery queues. It runs over TCP. In IoT deployments it is used in the backend (by RabbitMQ, for example) and is reached via gateways that translate from MQTT or CoAP.
- C is incorrect: AES-128 mesh encryption at 2.4 GHz describes Zigbee. AMQP uses TLS or SASL for security and operates over Ethernet/IP networks, not wireless radio.
- D is incorrect: AMQP has significantly higher per-message overhead than MQTT. It is not used on constrained devices precisely for this reason. MQTT remains the preferred protocol for sensor-to-cloud telemetry.

---

End of Quiz – Module 04
