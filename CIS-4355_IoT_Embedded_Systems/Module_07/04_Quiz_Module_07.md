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
