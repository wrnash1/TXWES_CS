# Quiz: Module 07 — IoT Communication Protocols

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Format:** 10 questions, multiple choice, 4 options each

---

## Question 1

In an MQTT system, what role does the broker play?

- A) It stores sensor readings in a database
- B) It receives messages from publishers and routes them to matching subscribers
- C) It runs on the IoT device and batches messages before sending to the cloud
- D) It translates between MQTT and HTTP for web clients

### Answer 1

Correct Answer: B

### Distractor Analysis 1

- A is incorrect — The broker routes messages; persistence and database storage are handled by separate backend services subscribed to relevant topics.
- B is correct — The broker is the central server that receives PUBLISH packets and forwards them to all clients subscribed to matching topics, fully decoupling publishers from subscribers.
- C is incorrect — The broker runs on a server or cloud platform, not on the IoT device itself; the IoT device runs an MQTT client library.
- D is incorrect — Protocol translation is the role of an API gateway or IoT rule engine, not the broker itself.

---

## Question 2

A smart building system needs to send a "fire alarm" MQTT message that must arrive exactly once with no possibility of duplication. Which QoS level is required?

- A) QoS 0 — at most once
- B) QoS 1 — at least once
- C) QoS 2 — exactly once
- D) QoS 3 — guaranteed delivery

### Answer 2

Correct Answer: C

### Distractor Analysis 2

- A is incorrect — QoS 0 provides no delivery guarantee; the message may be silently lost if the network is unreliable.
- B is incorrect — QoS 1 guarantees delivery but may deliver the message more than once, which could trigger duplicate alarm actions.
- C is correct — QoS 2 uses a four-step handshake to guarantee the message arrives exactly once, eliminating both loss and duplication.
- D is incorrect — MQTT only defines three QoS levels (0, 1, 2); QoS 3 does not exist in the specification.

---

## Question 3

What does the `#` wildcard in an MQTT topic subscription `sensors/#` match?

- A) Only the topic `sensors/` with no additional levels
- B) Any single level directly under sensors, such as `sensors/room1` but not `sensors/room1/temp`
- C) All topics beginning with `sensors/`, including any number of additional levels
- D) Any topic containing the word "sensors" anywhere in the string

### Answer 3

Correct Answer: C

### Distractor Analysis 3

- A is incorrect — `#` matches zero or more levels beyond the prefix; it is not limited to an empty suffix.
- B is incorrect — That behavior describes the `+` single-level wildcard, not `#`.
- C is correct — `#` matches everything at and below the point where it appears, so `sensors/#` matches `sensors/room1`, `sensors/room1/temp`, and arbitrarily deep subtopics.
- D is incorrect — MQTT topics are matched structurally by level, not by substring search.

---

## Question 4

Which protocol was specifically designed for use over UDP on constrained devices and supports resource observation as a built-in feature?

- A) MQTT
- B) HTTP/2
- C) CoAP
- D) WebSocket

### Answer 4

Correct Answer: C

### Distractor Analysis 4

- A is incorrect — MQTT runs over TCP, not UDP, and uses publish-subscribe rather than request-response with observation.
- B is incorrect — HTTP/2 runs over TCP and is designed for high-performance web communication, not constrained devices.
- C is correct — CoAP (RFC 7252) runs over UDP to minimize overhead, and the Observe extension (RFC 7641) allows clients to receive server-push notifications when resource values change.
- D is incorrect — WebSocket runs over TCP and requires a full HTTP upgrade handshake; it is not suitable for minimal-RAM devices.

---

## Question 5

An ESP32 is sending sensor readings to a cloud API once every 5 seconds. Which message format would minimize bandwidth usage compared to JSON?

- A) XML
- B) Plain text
- C) CBOR
- D) Base64-encoded JSON

### Answer 5

Correct Answer: C

### Distractor Analysis 5

- A is incorrect — XML is significantly more verbose than JSON due to opening and closing tags; it increases bandwidth, not reduces it.
- B is incorrect — Plain text is efficient for single values but loses structure and type information for multi-field readings.
- C is correct — CBOR encodes the same JSON data model in binary form, typically 30–50% smaller than equivalent JSON, making it the best choice for bandwidth reduction.
- D is incorrect — Base64 encoding adds approximately 33% overhead to any payload; Base64-encoded JSON would be larger than regular JSON.

---

## Question 6

What is the purpose of a retained message in MQTT?

- A) It causes the broker to store all messages indefinitely until the subscriber acknowledges them
- B) The broker saves the last message on a topic and delivers it immediately to new subscribers
- C) It prevents the broker from deleting messages during a network outage
- D) It instructs the publishing device to keep a local copy of the message until delivery is confirmed

### Answer 6

Correct Answer: B

### Distractor Analysis 6

- A is incorrect — Retained messages store only the single most recent message per topic, not all historical messages.
- B is correct — When a message is published with the retain flag, the broker stores it and delivers it immediately to any new subscriber on that topic, without waiting for the next publication.
- C is incorrect — Retained messages are not related to broker outage resilience; that is the role of persistent sessions and message queuing.
- D is incorrect — The retain flag is an instruction to the broker, not the publisher; the publisher does not keep a local copy based on this flag.

---

## Question 7

A browser dashboard needs to receive live sensor data pushed from a server with minimal latency and low per-message overhead. Which protocol is most appropriate?

- A) HTTP short polling every 100ms
- B) HTTPS with long polling
- C) WebSocket
- D) CoAP over UDP

### Answer 7

Correct Answer: C

### Distractor Analysis 7

- A is incorrect — HTTP short polling at 100ms generates 10 full HTTP requests per second, each with 200+ bytes of headers; the overhead vastly exceeds the data payload.
- B is incorrect — HTTPS long polling reduces request frequency but still requires new HTTP connections for each data batch and cannot achieve persistent low latency.
- C is correct — WebSockets upgrade to a persistent bidirectional TCP connection with only 2 bytes of framing overhead per small message, enabling true server-push with minimal latency.
- D is incorrect — CoAP runs over UDP and is designed for constrained devices, not browsers; browsers do not natively implement CoAP.

---

## Question 8

What is the minimum header size of a CoAP message?

- A) 200 bytes
- B) 20 bytes
- C) 8 bytes
- D) 4 bytes

### Answer 8

Correct Answer: D

### Distractor Analysis 8

- A is incorrect — 200 bytes is the typical size of HTTP request headers, which is precisely what CoAP was designed to avoid.
- B is incorrect — 20 bytes is the minimum IPv4 header size; the CoAP header itself is much smaller.
- C is incorrect — 8 bytes is the minimum UDP header size; the CoAP fixed header overhead is even smaller.
- D is correct — The CoAP fixed header is exactly 4 bytes: Version (2 bits), Type (2 bits), Token Length (4 bits), Code (8 bits), and Message ID (16 bits).

---

## Question 9

In the MQTT Last Will and Testament feature, when does the broker publish the will message?

- A) When the client explicitly calls `disconnect()`
- B) When the client publishes a message with a special "goodbye" flag
- C) When the client disconnects unexpectedly without sending a DISCONNECT packet
- D) After every session, regardless of how the client disconnects

### Answer 9

Correct Answer: C

### Distractor Analysis 9

- A is incorrect — A clean disconnect using the MQTT DISCONNECT packet suppresses the LWT; the broker only publishes it for ungraceful disconnections.
- B is incorrect — There is no "goodbye" flag in MQTT; publishers use retain flags and QoS levels, not special disconnect signals.
- C is correct — The broker publishes the LWT when it detects that the client's TCP connection closed unexpectedly (network failure, device crash, power loss) without a formal MQTT DISCONNECT packet.
- D is incorrect — If the client disconnects cleanly, the broker discards the LWT without publishing it; it is specifically designed for unexpected failures only.

---

## Question 10

Which combination best suits a battery-powered environmental sensor deployed in a low-power mesh network with unreliable links?

- A) HTTP/REST with JSON over Wi-Fi
- B) MQTT with JSON over TCP/Wi-Fi
- C) CoAP with CBOR over 6LoWPAN/Zigbee
- D) WebSocket with JSON over Ethernet

### Answer 10

Correct Answer: C

### Distractor Analysis 10

- A is incorrect — HTTP over Wi-Fi consumes significant power and is unsuitable for battery-powered devices in mesh networks.
- B is incorrect — MQTT over TCP/Wi-Fi is a good choice for mains-powered devices, but TCP and Wi-Fi are too power-hungry for unreliable low-power mesh links.
- C is correct — CoAP runs over UDP (minimizing overhead), CBOR minimizes payload size, and 6LoWPAN/Zigbee provides IPv6 connectivity over low-power radio. This combination is specifically standardized for IoT mesh deployments.
- D is incorrect — WebSocket requires a persistent TCP connection and a full HTTP upgrade handshake, making it incompatible with mesh radio networks and power-constrained devices.

---

## Question 11 (5 points)

An MQTT broker is configured with `max_keepalive 60`. A connected ESP32 stops transmitting for 75 seconds due to a sensor hang. What does the broker do?

- A) The broker queues all incoming messages for the ESP32 and delivers them when it reconnects.
- B) The broker closes the connection and publishes the ESP32's Last Will and Testament message on its configured will topic.
- C) The broker sends a PINGREQ to the ESP32 and waits indefinitely for a PINGRESP.
- D) The broker downgrades the ESP32's QoS to QoS 0 to reduce keepalive traffic.

### Answer 11

Correct Answer: B

### Distractor Analysis 11

- A is incorrect — Message queuing for offline clients requires the subscriber to reconnect and have a persistent session configured. The broker closes the dead connection; it does not queue outgoing messages to a publisher that it considers disconnected.
- B is correct — When the broker does not receive any traffic (PUBLISH, SUBSCRIBE, PINGREQ, or other packets) from a connected client within 1.5 times the keep-alive interval, it declares the connection dead, closes it, and publishes the registered LWT message if one was configured.
- C is incorrect — The broker does not send PINGREQ to clients; that packet flows from client to broker only. The broker passively monitors for client inactivity.
- D is incorrect — QoS level is set per-message by the publisher. The broker cannot unilaterally change a client's QoS configuration.

---

## Question 12 (5 points)

A CoAP GET request is sent as a Confirmable (CON) message. The server is temporarily unavailable and does not respond. What does the CoAP client do?

- A) The client immediately returns an error code and does not retry.
- B) The client retransmits the CON message using exponential backoff up to a configurable maximum number of retransmissions, then declares a timeout failure.
- C) The client switches to TCP and sends the same request over HTTPS.
- D) The client marks the resource as permanently unavailable and removes it from its local cache.

### Answer 12

Correct Answer: B

### Distractor Analysis 12

- A is incorrect — Confirmable messages provide reliability through retransmission. Immediate failure without retry would remove the reliability benefit of the CON message type.
- B is correct — CoAP Confirmable messages are retransmitted with exponential backoff (starting at 2–3 seconds) up to MAX_RETRANSMIT (default 4) times. After exhausting retransmissions, the client receives a timeout error. This is CoAP's mechanism for providing reliability over UDP without TCP.
- C is incorrect — CoAP has no fallback to TCP. Protocol selection is fixed at design time. CoAP over TCP exists (RFC 8323) but is a separate variant, not an automatic fallback.
- D is incorrect — A temporary non-response does not cause CoAP to permanently invalidate a resource. Cache invalidation follows separate CoAP freshness and Max-Age rules.

---

## Question 13 (5 points)

A JSON payload `{"t":23.5,"h":61}` is 18 bytes. An equivalent CBOR encoding is 12 bytes. A sensor publishes every 10 seconds for 30 days. How many total bytes are saved by using CBOR over JSON?

- A) 6 bytes
- B) 51,840 bytes
- C) 155,520 bytes
- D) 1,555,200 bytes

### Answer 13

Correct Answer: D

### Distractor Analysis 13

- A is incorrect — 6 bytes is the per-message saving for a single transmission. The question asks for cumulative savings over 30 days of continuous publishing.
- B is incorrect — 51,840 bytes = 6 × 8,640 messages, which covers only one day of publishing at 10-second intervals.
- C is incorrect — 155,520 does not correspond to the correct message count. It would require 25,920 messages, not the 259,200 produced over 30 days.
- D is correct — Messages per day = 86,400 s / 10 s = 8,640. Over 30 days: 8,640 × 30 = 259,200 messages. Total savings = 6 bytes × 259,200 = 1,555,200 bytes (approximately 1.5 MB).

---

## Question 14 (5 points)

Which MQTT feature allows a device to publish its current state so that any new subscriber immediately receives the most recent value without waiting for the next publish cycle?

- A) QoS 2 exactly-once delivery
- B) Persistent session with clean_session=false
- C) Retained message with retain=True flag
- D) Last Will and Testament registration

### Answer 14

Correct Answer: C

### Distractor Analysis 14

- A is incorrect — QoS 2 controls delivery reliability, not whether a value is stored for future subscribers. It has no effect on new subscriber behavior.
- B is incorrect — Persistent sessions allow a reconnecting subscriber to receive messages published while it was offline. They do not immediately deliver current state to brand-new subscribers.
- C is correct — When a message is published with `retain=True`, the broker stores it as the last known good value for that topic. Any new subscriber receives this retained message instantly upon subscribing, giving them the current state without waiting for the sensor's next transmission.
- D is incorrect — LWT is a message published when a device disconnects unexpectedly. It is typically used to broadcast an "offline" status, not to share current sensor readings with new subscribers.

---

## Question 15 (5 points)

What is the key architectural difference between HTTP long polling and WebSockets for delivering real-time data to a browser client?

- A) HTTP long polling uses binary framing; WebSockets use plain text headers for all messages.
- B) HTTP long polling holds the request open until data is available, then closes the connection and requires a new request; WebSockets establish a persistent bidirectional channel with minimal per-message overhead.
- C) WebSockets require a separate server port and cannot share port 443 with HTTPS traffic.
- D) HTTP long polling provides lower latency because it bypasses the TCP connection establishment overhead.

### Answer 15

Correct Answer: B

### Distractor Analysis 15

- A is incorrect — The framing characteristic is reversed. HTTP long polling uses standard HTTP text headers. WebSockets use a compact binary frame (2–10 bytes overhead per message vs. 200+ bytes for HTTP headers).
- B is correct — Long polling keeps a pending HTTP request open and the server responds when data is ready, but the connection closes after each response. The client immediately opens a new request. WebSockets perform a one-time HTTP Upgrade handshake, then maintain the same TCP connection indefinitely for all bidirectional messages with minimal overhead.
- C is incorrect — WebSockets can and commonly do operate over port 443 (WSS — WebSocket Secure) sharing the same TLS infrastructure as HTTPS. They are not restricted to a separate port.
- D is incorrect — Long polling has higher latency because each new data point requires a full HTTP request-response round-trip. WebSockets push data immediately on the existing connection.

---

## Question 16 (5 points)

An MQTT topic subscription `home/kitchen/+` would match which of the following topics?

- A) `home/kitchen`
- B) `home/kitchen/fridge/temperature`
- C) `home/kitchen/fridge`
- D) `home/kitchen/fridge/temperature/current`

### Answer 16

Correct Answer: C

### Distractor Analysis 16

- A is incorrect — `home/kitchen/+` requires exactly three levels. `home/kitchen` has only two levels and does not match.
- B is incorrect — `home/kitchen/fridge/temperature` has four levels. The `+` wildcard matches exactly one level, so this four-level topic does not match the three-level filter.
- C is correct — `home/kitchen/fridge` has exactly three levels: `home`, `kitchen`, and `fridge`. The `+` wildcard matches the single level `fridge` in the third position. This is the only option with exactly three levels.
- D is incorrect — `home/kitchen/fridge/temperature/current` has five levels. The `+` wildcard matches only one level, not multiple.

---

## Question 17 (5 points)

Why does the CoAP specification use message IDs and tokens as two separate fields rather than a single identifier?

- A) Message IDs are assigned by the broker; tokens are assigned by the client, allowing both to be tracked independently.
- B) Message IDs detect and deduplicate duplicate UDP retransmissions at the transport layer; tokens correlate request-response pairs at the application layer across multiple concurrent requests.
- C) Message IDs are encrypted with DTLS; tokens are transmitted in plaintext for debugging purposes.
- D) Message IDs are 32-bit values for large deployments; tokens are 8-bit values for constrained devices.

### Answer 17

Correct Answer: B

### Distractor Analysis 17

- A is incorrect — CoAP has no broker. Both message IDs and tokens are generated by the client. They serve different protocol layers, not different parties.
- B is correct — The Message ID (16 bits) is a transport-layer deduplication field. Retransmissions carry the same Message ID so the receiver can drop duplicates. The Token (0–8 bytes, application-defined) correlates a specific request with its response at the application layer, allowing multiple in-flight requests to be matched to their replies independently of retransmission.
- C is incorrect — DTLS encrypts the entire CoAP message including both fields. Tokens are not transmitted in plaintext for security or debugging reasons.
- D is incorrect — Message IDs are 16-bit values (not 32-bit). Tokens are variable length (0–8 bytes, not 8-bit fixed). The distinction is functional, not a size difference for scalability.

---

## Question 18 (5 points)

An IoT device uses MQTT with `clean_session=False` and QoS 1 to publish sensor readings. The device goes offline for 2 hours. When it reconnects, what happens to the messages published by other clients to its subscribed topics during the outage?

- A) All messages are permanently lost because the device was offline.
- B) The broker delivers the queued messages to the device upon reconnection, up to the broker's configured maximum queue depth.
- C) The device re-subscribes automatically and receives only new messages published after reconnection.
- D) The broker requests the device to replay its own published messages to fill the gap.

### Answer 18

Correct Answer: B

### Distractor Analysis 18

- A is incorrect — This would be the behavior with `clean_session=True`. With `clean_session=False`, the broker maintains a persistent session including queued QoS 1 and QoS 2 messages.
- B is correct — A persistent session (`clean_session=False`) causes the broker to store QoS 1 and QoS 2 messages for subscribed topics when the subscriber is offline. Upon reconnection, the broker delivers all queued messages. The number of stored messages is limited by the broker's `max_queued_messages` configuration.
- C is incorrect — With a persistent session, re-subscription is not required. The broker remembers the subscriptions and delivers backlogged messages automatically on reconnect.
- D is incorrect — MQTT has no replay mechanism for a subscriber's own published messages. Message queuing is for incoming subscribed messages, not outgoing published ones.

---

## Question 19 (5 points)

A developer wants to verify TLS certificate authenticity when connecting to a production MQTT broker using the Paho Python library. Which method call configures TLS with full certificate verification?

- A) `client.tls_set(cert_reqs=ssl.CERT_NONE)` — disables certificate checks for development ease.
- B) `client.tls_set(ca_certs="ca.crt")` — loads the CA certificate file and enables full server certificate verification.
- C) `client.tls_insecure_set(True)` — enables TLS encryption while allowing self-signed certificates.
- D) `client.username_pw_set("user", "pass")` — authenticates with credentials instead of a TLS certificate.

### Answer 19

Correct Answer: B

### Distractor Analysis 19

- A is incorrect — `CERT_NONE` disables certificate verification entirely. An attacker can substitute their own certificate and perform a man-in-the-middle attack. This is acceptable only in isolated test environments, never in production.
- B is correct — `client.tls_set(ca_certs="ca.crt")` provides the Certificate Authority file. The Paho library uses it to verify the broker's certificate chain. This is the production-correct configuration that ensures the client is communicating with the legitimate broker.
- C is incorrect — `tls_insecure_set(True)` disables hostname verification in the TLS handshake. While it still uses TLS encryption, it allows certificate spoofing from an attacker who presents any valid certificate for any hostname.
- D is incorrect — Username/password authentication is a separate MQTT-layer credential and does not establish TLS certificate verification. TLS must be configured separately.

---

## Question 20 (5 points)

An MQTT topic hierarchy for a smart city deployment uses the structure `city/district/zone/device-type/device-id/metric`. A subscriber wants to receive all temperature readings from all device types across the entire `downtown` district. Which subscription topic achieves this?

- A) `city/downtown/#`
- B) `city/downtown/+/+/+/temperature`
- C) `city/downtown/*/*/*/temperature`
- D) `city/+/+/+/+/temperature`

### Answer 20

Correct Answer: B

### Distractor Analysis 20

- A is incorrect — `city/downtown/#` matches every topic under downtown — all metrics, all device types, all zones, all metrics. This delivers far more data than just temperature readings.
- B is correct — `city/downtown/+/+/+/temperature` uses three `+` wildcards to match any single value for zone, device-type, and device-id respectively, while requiring the sixth level to be exactly `temperature`. This precisely filters for temperature readings across all zones, device types, and device IDs in downtown.
- C is incorrect — `*` is not a valid MQTT wildcard character. MQTT only defines `+` (single level) and `#` (multi-level). Using `*` would treat it as a literal character in the topic name.
- D is incorrect — `city/+/+/+/+/temperature` would match any district (not just downtown) with any zone, device-type, and device-id. It is too broad — it includes all districts, not just downtown.
