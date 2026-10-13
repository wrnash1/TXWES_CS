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

---

### Question 11 (5 points)

A Mosquitto broker is configured with `allow_anonymous true` in its configuration file. What is the security implication of this setting?

- A) Only devices with valid X.509 certificates can connect; anonymous means certificate-only access.
- B) Any device that can reach the broker's TCP port can connect, publish, and subscribe without providing a username or password.
- C) Anonymous devices can subscribe to topics but cannot publish messages.
- D) The setting enables read-only access to the broker's management API without credentials.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `allow_anonymous true` is the opposite of certificate-only access. It disables all credential requirements entirely for devices that do not present credentials.
  - B) `allow_anonymous true` in Mosquitto means any device that can reach the TCP port (1883 or 8883) may connect without supplying a username or password. Combined with no ACL file, this means any device can publish and subscribe to any topic — a complete absence of access control.
  - C) Anonymous access in Mosquitto does not automatically restrict devices to subscribe-only. Without an ACL file, anonymous clients have full publish and subscribe permissions.
  - D) The Mosquitto management API is a separate configuration namespace. `allow_anonymous` governs MQTT client connections, not the management REST interface.

---

### Question 12 (5 points)

An MQTT Last Will and Testament (LWT) message is configured with topic `devices/sensor-42/status`, payload `"offline"`, and QoS 1. Under which condition does the broker publish this will message?

- A) When the client sends a DISCONNECT packet to cleanly end its session.
- B) When the client's network connection drops without a DISCONNECT packet being sent (unexpected disconnection).
- C) When the client publishes more than 100 messages within one minute, exceeding the rate limit.
- D) When the broker restarts and reloads the client's session from persistent storage.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) A clean DISCONNECT causes the broker to discard the will message, not publish it. LWT is only triggered by unexpected disconnections, not graceful ones.
  - B) The LWT message is published by the broker when the client's network connection terminates without a proper DISCONNECT packet — for example, due to a power failure, network outage, or application crash. This is the entire design purpose of LWT: detecting unexpected device outages.
  - C) Rate limiting is not a feature of standard MQTT. The LWT is not triggered by message frequency.
  - D) Broker restarts do not trigger will messages for all stored sessions. The will is only triggered when the specific client's connection is detected as unexpectedly dropped.

---

### Question 13 (5 points)

In a Zigbee network with AES-128 encryption, which two key types does the Zigbee specification use, and what does each protect?

- A) Master key (encrypts device identity) and session key (encrypts application payloads per transaction).
- B) Network key (encrypts all traffic between all devices in the network) and link key (encrypts traffic on a specific device-to-device link).
- C) Public key (broadcast to all devices) and private key (stored only on the coordinator's Trust Center).
- D) Channel key (unique per radio channel) and mesh key (unique per routing hop).

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) "Master key" and "session key" are TLS/DTLS terminology, not Zigbee. Zigbee uses network and link keys.
  - B) The Zigbee network key is a shared AES-128 key distributed to all devices in the network by the Trust Center. It protects broadcast traffic and device-to-network communications. The link key is a pairwise key negotiated between two specific devices for end-to-end protection of sensitive application data.
  - C) Zigbee uses symmetric AES-128 keys distributed by the Trust Center, not asymmetric public/private key pairs for normal device communication.
  - D) "Channel key" and "mesh key" are not Zigbee specification terms. Zigbee uses network and link keys as the two key hierarchy levels.

---

### Question 14 (5 points)

Which MQTT topic subscription would match the message published to `home/kitchen/fridge/temperature` but NOT match `home/kitchen/temperature`?

- A) `home/#`
- B) `home/kitchen/#`
- C) `home/+/+/temperature`
- D) `home/kitchen/+`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `home/#` matches any topic starting with `home/`, including both `home/kitchen/fridge/temperature` and `home/kitchen/temperature`. It does not distinguish them.
  - B) `home/kitchen/#` matches any topic starting with `home/kitchen/`, including both `home/kitchen/fridge/temperature` and `home/kitchen/temperature`. It matches both, not just the first.
  - C) `home/+/+/temperature` requires exactly four levels: `home`, one single level, one single level, and `temperature`. This matches `home/kitchen/fridge/temperature` (levels: home, kitchen, fridge, temperature) but NOT `home/kitchen/temperature` (only three levels). The `+` wildcard matches exactly one level.
  - D) `home/kitchen/+` matches exactly three-level topics starting with `home/kitchen/`. It matches `home/kitchen/fridge` but NOT `home/kitchen/fridge/temperature` (four levels) or `home/kitchen/temperature` (correct three levels but missing fridge).

---

### Question 15 (5 points)

A CoAP GET request is sent to `coap://192.168.1.50/sensors/temperature`. The server responds with a `2.05 Content` response code. What does this response code indicate?

- A) The request was accepted but the resource has not been created yet.
- B) The resource was not found at the specified URI.
- C) The request succeeded and the response body contains the current value of the requested resource.
- D) The server requires DTLS authentication before serving the resource.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Accepted-but-not-created corresponds to CoAP `2.31 Continue` or `2.01 Created` for POST operations. `2.05` is not a pending-creation response.
  - B) Resource not found is CoAP `4.04 Not Found`, which is analogous to HTTP 404. A 2.xx response always indicates success in CoAP.
  - C) CoAP `2.05 Content` is the standard success response to a GET request. It is the CoAP equivalent of HTTP `200 OK` and indicates the body contains the current representation of the requested resource.
  - D) An authentication requirement would be indicated by CoAP `4.01 Unauthorized`. A `2.xx` code can only be returned after authentication has already succeeded.

---

### Question 16 (5 points)

Which Paho MQTT Python method must be called after `client.connect()` to allow the library to process incoming and outgoing network traffic in a non-blocking background thread?

- A) `client.loop_forever()`
- B) `client.loop_start()`
- C) `client.run()`
- D) `client.start_thread()`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `client.loop_forever()` starts a blocking network loop that does not return until `client.disconnect()` is called. It is appropriate for subscriber scripts that run indefinitely but blocks the calling thread — it cannot be used for publishers that need to continue executing code after connecting.
  - B) `client.loop_start()` starts a background daemon thread that handles network I/O. The main program continues executing. When finished, call `client.loop_stop()`. This is the correct pattern for publisher scripts that need to send messages and then proceed with other logic.
  - C) `run()` is not a method on the Paho `mqtt.Client` class. Using it would raise an `AttributeError`.
  - D) `start_thread()` is not a Paho MQTT method. The correct background thread method is `loop_start()`.

---

### Question 17 (5 points)

An IoT system uses Z-Wave for smart home device control. Which frequency band does Z-Wave use in the United States, and what advantage does this provide over 2.4 GHz protocols?

- A) 2.4 GHz — the same as Zigbee, providing interoperability between the two protocols.
- B) 5 GHz — providing higher bandwidth for video streaming from smart cameras.
- C) 908 MHz — avoiding congestion from Wi-Fi and Bluetooth devices that share the 2.4 GHz band.
- D) 433 MHz — providing multi-kilometer range comparable to LoRaWAN.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Z-Wave uses 908 MHz in the US, not 2.4 GHz. Z-Wave and Zigbee are not interoperable protocols despite both targeting smart home applications.
  - B) Z-Wave's 908 MHz band has lower bandwidth than 5 GHz. Z-Wave's maximum data rate is 100 kbps — entirely unsuitable for video. The 908 MHz choice is about reducing interference, not increasing bandwidth.
  - C) Z-Wave operates at 908 MHz in the US (868 MHz in EU). This sub-GHz frequency avoids the congested 2.4 GHz band where Wi-Fi, Bluetooth, Zigbee, and microwave ovens all coexist. Less interference means more reliable communication in dense environments with many wireless devices.
  - D) 433 MHz is used by some remote controls and older ISM devices but not Z-Wave. Z-Wave uses 908 MHz (US) specifically. LoRaWAN range advantages come from spread-spectrum modulation technique, not from 433 MHz operation.

---

### Question 18 (5 points)

Which characteristic of MQTT's publish-subscribe pattern makes it suitable for IoT deployments where many sensors report to many consumers simultaneously?

- A) Publishers must maintain a persistent TCP connection to every subscriber simultaneously.
- B) Each subscriber polls the broker on a configurable interval to retrieve new messages.
- C) Publishers and subscribers are fully decoupled — a publisher does not need to know how many subscribers exist or their addresses.
- D) The broker enforces a maximum of one subscriber per topic to prevent message duplication.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) In MQTT, publishers connect only to the broker, not to subscribers. The broker distributes messages. Publishers have no knowledge of or connection to subscribers.
  - B) MQTT subscribers receive messages pushed by the broker when they arrive. There is no polling in MQTT's publish-subscribe model. Polling would describe HTTP REST with client-initiated requests.
  - C) Decoupling is MQTT's core architectural advantage. A publisher sends to a topic on the broker. The broker can have zero, one, or thousands of subscribers on that topic without the publisher knowing or caring. This scales to massive IoT deployments without modifying publishers as consumers are added or removed.
  - D) MQTT imposes no subscriber limit per topic. Multiple subscribers can receive the same message, which is fundamental to fan-out architectures (e.g., dashboards, databases, and alerting systems all subscribing to the same sensor topic).

---

### Question 19 (5 points)

A 6LoWPAN network connects IPv6-addressed sensors to an IPv6 backbone network. What function does 6LoWPAN provide that makes this possible?

- A) 6LoWPAN translates Zigbee application layer commands to HTTP REST endpoints.
- B) 6LoWPAN compresses IPv6 headers and fragments large IPv6 packets to fit within the 127-byte IEEE 802.15.4 frame size limit.
- C) 6LoWPAN adds a 64-bit mesh routing layer on top of IPv4 to support sensor addressing.
- D) 6LoWPAN provides a gateway function that converts MQTT messages to CoAP before forwarding to sensors.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) 6LoWPAN is a network adaptation layer, not an application protocol translator. It operates at the network layer (Layer 3) and has no knowledge of application protocols like HTTP or Zigbee application clusters.
  - B) IPv6 headers are 40 bytes. The IEEE 802.15.4 maximum frame payload is 127 bytes. 6LoWPAN (RFC 4944) solves this mismatch by providing header compression (reducing the 40-byte IPv6 header to as few as 2 bytes) and packet fragmentation/reassembly, enabling native IPv6 addressing directly on constrained sensor nodes.
  - C) 6LoWPAN is specifically designed for IPv6, not IPv4. The "6" in 6LoWPAN refers to IPv6. It does not operate over IPv4.
  - D) Protocol translation between MQTT and CoAP is a gateway function unrelated to 6LoWPAN's network adaptation role.

---

### Question 20 (5 points)

A Zigbee End Device in a smart building cannot reach its parent router due to a router failure. What happens next in a properly configured Zigbee mesh network?

- A) The end device broadcasts a distress signal on all channels and waits for the coordinator to respond directly.
- B) The end device autonomously reroutes traffic through an alternate router or finds a new parent — the mesh self-heals.
- C) The entire Zigbee network shuts down until the failed router is replaced.
- D) The end device switches to Wi-Fi to maintain connectivity during the outage.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Zigbee end devices are sleepy leaf nodes — they do not broadcast distress signals or manage routing. Routing decisions are made by routers and the coordinator.
  - B) Zigbee mesh networks are self-healing. When a router fails, other routers detect the topology change and update their routing tables. End devices that have lost their parent will re-associate with an alternative router. This self-healing property is one of the primary advantages of mesh topology over star topology.
  - C) The loss of one router does not bring down a properly designed Zigbee mesh. Redundant routing paths allow the network to continue operating around the failed node.
  - D) Zigbee end devices are single-radio devices. They cannot autonomously switch to a different wireless technology. Technology fallback requires a multi-radio gateway design at a higher layer.

---

End of Quiz – Module 04
