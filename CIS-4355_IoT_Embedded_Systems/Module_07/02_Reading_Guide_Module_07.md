# Reading Guide: Module 07 — IoT Communication Protocols

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4355 &BULL; INTERNET OF THINGS (IOT) & EMBEDDED SYSTEMS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Certification Target:** IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you will be able to:

1. Describe the MQTT publish-subscribe model, broker role, topic hierarchy, and wildcard syntax
2. Explain the three MQTT QoS levels and select the appropriate level for a given reliability requirement
3. Contrast CoAP with HTTP and identify deployment scenarios suited to each
4. Explain how WebSockets differ from HTTP polling and when to use them
5. Compare JSON and CBOR message formats and select between them for constrained vs non-constrained devices
6. Apply the five-factor protocol selection framework to choose among MQTT, CoAP, HTTP, and WebSockets
7. Configure a basic MQTT client on an ESP32 to publish and subscribe

---

## Section 1 — MQTT

### 1.1 Publish-Subscribe Architecture

MQTT separates message producers (publishers) from message consumers (subscribers) through a central message broker. Neither party needs to know the other exists — they only share a topic string.

```text
[Sensor ESP32]  --publish-->  [Broker]  --deliver-->  [Dashboard]
                              [Broker]  --deliver-->  [Database]
                              [Broker]  --deliver-->  [Alert Service]
```

This decoupling provides three benefits:

- **Scalability:** Add consumers without modifying publishers
- **Resilience:** If a consumer is offline, the broker can queue messages (with persistent sessions)
- **Flexibility:** One sensor feeds multiple consumers simultaneously

### 1.2 Topic Hierarchy and Wildcards

Topics are UTF-8 strings with levels separated by `/`. Well-designed topic hierarchies mirror physical or logical structure:

```text
company/site/building/floor/room/device/measurement
vzw/dallas/hq/3/conf-a/thermostat/temperature
```

Wildcard syntax:

| Wildcard | Matches | Example | Matches |
|----------|---------|---------|---------|
| `+` | Exactly one level | `building/+/temperature` | building/floor1/temperature |
| `#` | Zero or more trailing levels | `building/#` | building/floor1/room3/humidity |

The `#` wildcard can only appear at the end of a topic filter.

System topics beginning with `$` are reserved (e.g., `$SYS/broker/clients/connected` reports connected client count).

### 1.3 QoS Levels In Detail

| QoS | Name | Delivery Guarantee | Packets | Use Case |
|-----|------|--------------------|---------|----------|
| 0 | At most once | May be lost | 1 (PUBLISH) | Non-critical telemetry |
| 1 | At least once | Arrives 1+ times | 2 (PUBLISH + PUBACK) | Alerts, status changes |
| 2 | Exactly once | Arrives exactly 1 time | 4 (PUBLISH + PUBREC + PUBREL + PUBCOMP) | Commands, financial events |

QoS applies independently to publish and subscribe. A publisher can publish at QoS 1 while a subscriber receives at QoS 0. The broker downgrades to the lower of the two.

### 1.4 Retained Messages and Last Will

**Retained messages:** The broker stores the last message published on a topic with `retain=true`. New subscribers immediately receive this cached message. Use retained messages for device configuration topics, last-known state, and initialization data.

**Last Will and Testament (LWT):** When a client connects, it registers an LWT message with the broker. If the client disconnects unexpectedly (network failure, crash), the broker automatically publishes the LWT message to the will topic. This enables other subscribers to detect device failures.

```cpp
// Register LWT before connecting
mqtt.setWill("devices/esp32-01/status", "offline", true, 1);
mqtt.connect("esp32-01");
// At startup, publish online status
mqtt.publish("devices/esp32-01/status", "online", true);
```

### 1.5 MQTT Over TLS

Production MQTT should always use TLS on port 8883. On the ESP32:

```cpp
#include <WiFiClientSecure.h>
#include <PubSubClient.h>

WiFiClientSecure tlsClient;
PubSubClient     mqtt(tlsClient);

void setup() {
  tlsClient.setCACert(root_ca_pem);  // CA certificate for broker verification
  mqtt.setServer("broker.example.com", 8883);
}
```

Never use port 1883 (unencrypted) for production devices. Credentials and sensor data are transmitted in plaintext on the open network.

---

## Section 2 — CoAP

### 2.1 Design Goals

CoAP (RFC 7252) was designed for machine-to-machine communication in constrained environments where HTTP is too expensive. Key design decisions:

- **UDP transport:** No connection setup overhead; tolerates lossy networks
- **4-byte minimum header:** Versus 200+ bytes for HTTP
- **Asynchronous messaging:** Non-confirmable messages for fire-and-forget
- **Confirmable messages:** CoAP's equivalent of TCP reliability at the application layer

### 2.2 CoAP Message Types

| Type | Description |
|------|-------------|
| CON (Confirmable) | Must be acknowledged; retransmitted until ACK received |
| NON (Non-confirmable) | Fire-and-forget; no acknowledgment expected |
| ACK (Acknowledgment) | Confirms receipt of a CON message |
| RST (Reset) | Indicates a CON message could not be processed |

### 2.3 CoAP vs HTTP Comparison

| Feature | HTTP | CoAP |
|---------|------|------|
| Transport | TCP | UDP |
| Header size | 200–800 bytes | 4 bytes minimum |
| Methods | GET, POST, PUT, DELETE, PATCH, HEAD | GET, POST, PUT, DELETE |
| Push support | Long-polling / Server-Sent Events | Observe (RFC 7641) |
| Security | TLS (HTTPS) | DTLS |
| Typical port | 80 / 443 | 5683 / 5684 (DTLS) |
| Resource discovery | None built-in | CoRE Link Format (RFC 6690) |

### 2.4 CoAP Observe

The Observe extension allows a CoAP client to register interest in a resource. The server sends notifications whenever the value changes, without the client polling repeatedly. This provides MQTT-like push behavior over UDP.

---

## Section 3 — HTTP/REST for IoT

### 3.1 HTTP Request/Response Cycle

Every HTTP transaction follows this sequence:

1. TCP three-way handshake (SYN, SYN-ACK, ACK)
2. TLS handshake if HTTPS (1–2 round trips)
3. Client sends HTTP request with headers
4. Server processes and responds
5. Connection closed (HTTP/1.1) or kept alive for reuse

For a device making an HTTPS POST every 5 minutes, this overhead is negligible. For a device posting every 100ms, the connection setup time alone may exceed the available time budget.

### 3.2 HTTP Methods in IoT

| Method | Use in IoT |
|--------|------------|
| GET | Read device state, retrieve configuration |
| POST | Send sensor readings, create new records |
| PUT | Update device configuration entirely |
| PATCH | Partial update (e.g., change one setting) |
| DELETE | Remove a device registration or record |

### 3.3 REST API Design Patterns for IoT

Good IoT REST API design follows predictable URL patterns:

```text
GET  /devices/{id}/status          — Read device status
POST /devices/{id}/readings        — Submit sensor reading
PUT  /devices/{id}/config          — Update configuration
GET  /devices/{id}/readings?limit=10 — Last 10 readings
```

### 3.4 HTTP Polling vs Long-Polling

**Short polling:** Client sends GET every N seconds. Simple but wastes bandwidth when no new data exists.

**Long polling:** Client sends GET, server holds the request open until new data is available (up to a timeout), then responds. Simulates push over HTTP. More efficient than short polling but holds server threads open.

**Server-Sent Events (SSE):** The server sends a `text/event-stream` response and continues pushing newline-delimited events. One-directional (server to client). More efficient than long-polling for streaming updates to browsers.

---

## Section 4 — WebSockets

### 4.1 WebSocket Handshake

WebSockets begin with an HTTP upgrade:

```text
Client → Server:
GET /ws HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==

Server → Client:
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

After the 101 response, the TCP connection carries WebSocket frames indefinitely with minimal framing overhead.

### 4.2 WebSocket Frame Overhead

| Payload Size | Frame Header Size |
|-------------|------------------|
| 0–125 bytes | 2 bytes |
| 126–65535 bytes | 4 bytes |
| 65536+ bytes | 10 bytes |

Compare to HTTP, where headers alone are 200+ bytes regardless of payload size.

### 4.3 WebSocket Use Cases in IoT

- **Live dashboards:** Browser client receives sensor data in real time without polling
- **Remote control:** Cloud server sends actuator commands to an ESP32 WebSocket client
- **Bidirectional configuration:** Device sends status; cloud responds with updated parameters
- **Streaming audio/video from edge device:** Camera streams over WebSocket to monitoring server

---

## Section 5 — Message Formats

### 5.1 JSON Structure and Size

JSON is the default message format for IoT REST APIs and MQTT payloads. It is text-based, self-describing, and supported natively by every cloud platform.

```cpp
// Typical IoT JSON payload
const char* payload =
  "{"
  "\"device_id\":\"esp32-sensor-01\","
  "\"timestamp\":1717200000,"
  "\"temperature\":23.45,"
  "\"humidity\":61.2,"
  "\"battery_mv\":3721"
  "}";
// Total: 95 bytes
```

JSON overhead comes from repeated key names, quotation marks, and colons. In a system sending 1 million readings per day, a 95-byte payload versus a 30-byte CBOR payload saves roughly 62 MB of bandwidth daily.

### 5.2 CBOR Encoding

CBOR (RFC 7049) uses a compact type-length-value encoding. The same five-field reading in CBOR:

```text
A5                       -- map of 5 items
  69 device_id           -- text string (9 bytes)
  70 esp32-sensor-01     -- text string (16 bytes)
  69 timestamp           -- text string key
  1A 665FFC80            -- unsigned int (4 bytes for value)
  6B temperature         -- text string key
  F9 4DC7                -- float16 (2 bytes for 23.45)
  ...
// Total: ~55 bytes vs 95 bytes JSON
```

The ArduinoCBOR library and the ESP32's Mbed TLS ecosystem support CBOR encoding and decoding. Python's `cbor2` library handles server-side decoding.

### 5.3 Protocol and Format Matrix

| Combination | Bytes/msg | Human-readable | Cloud support | Best for |
|-------------|-----------|----------------|---------------|----------|
| HTTP + JSON | 300+ | Yes | Universal | REST APIs, infrequent data |
| MQTT + JSON | 100–200 | Yes | Universal | General telemetry |
| MQTT + CBOR | 30–60 | No | Good | High-frequency telemetry |
| CoAP + CBOR | 35–65 | No | Limited | Constrained mesh networks |
| WebSocket + JSON | 100–200 | Yes | Good | Live dashboards |

---

## Section 6 — Protocol Selection Framework

### 6.1 Five Factors

When selecting an IoT protocol, evaluate these five factors in order:

1. **Device constraints** — RAM, processing power, power budget
2. **Network characteristics** — reliability, latency, bandwidth, topology
3. **Message frequency** — readings per second/minute/hour
4. **Directionality** — device-to-cloud only, or cloud-to-device commands also needed
5. **Reliability requirements** — can messages be lost, duplicated, or must they arrive exactly once

### 6.2 Decision Flowchart

```text
START
  |
  Does device have >64KB RAM and full TCP/IP stack?
    NO  → CoAP over UDP
    YES ↓
  Is message frequency > 1/minute?
    YES → MQTT QoS 0 or 1
    NO  ↓
  Does cloud need to push commands to device?
    YES → MQTT with subscription (or WebSocket)
    NO  ↓
  Is this a browser/dashboard real-time display?
    YES → WebSocket
    NO  → HTTP/REST POST
```

### 6.3 Broker Selection Guide

| Broker | Type | Free Tier | TLS | Best For |
|--------|------|-----------|-----|----------|
| Mosquitto | Self-hosted | Yes (open source) | Yes | On-premises, lab, edge |
| HiveMQ Cloud | Managed | Yes (limited) | Yes | Development, small deployments |
| AWS IoT Core | Managed | Pay-per-use | Yes | Production, AWS ecosystem |
| Azure IoT Hub | Managed | Free (8K msg/day) | Yes | Production, Azure ecosystem |
| test.mosquitto.org | Public test | Yes | No | Testing only |

---

## Key Terms

| Term | Definition |
|------|------------|
| Broker | MQTT server that receives and routes messages between publishers and subscribers |
| Publisher | Device or service that sends messages to the broker on a topic |
| Subscriber | Device or service that receives messages from the broker on subscribed topics |
| Topic | Hierarchical string routing key for MQTT messages |
| QoS | Quality of Service — MQTT delivery guarantee level (0, 1, or 2) |
| Retained message | Last published message stored by broker and delivered to new subscribers |
| LWT | Last Will and Testament — message published by broker when a client disconnects unexpectedly |
| CoAP | Constrained Application Protocol — lightweight request-response protocol over UDP |
| CBOR | Concise Binary Object Representation — compact binary encoding of JSON-like data |
| WebSocket | Bidirectional persistent TCP connection with minimal framing overhead |
| DTLS | Datagram TLS — TLS security layer for UDP-based protocols like CoAP |
| 6LoWPAN | IPv6 over Low-Power Wireless Personal Area Networks — carries CoAP in mesh sensor networks |

---

## Review Questions

1. A subscriber joins the topic `sensors/+/temperature`. Which of these topics will it receive — `sensors/room1/temperature`, `sensors/room1/humidity`, `sensors/building1/room1/temperature`?
2. Why is QoS 2 four times more expensive in network traffic than QoS 0?
3. Explain why CoAP uses UDP instead of TCP. What mechanism does CoAP provide to achieve reliability when needed?
4. An ESP32 sends one sensor reading per day. Would MQTT or HTTP be more appropriate? Justify using the five-factor framework.
5. What is the purpose of a Last Will and Testament message in MQTT?
6. Why should you never use port 1883 for production IoT devices?
7. Calculate the bandwidth savings over 24 hours if switching from 95-byte JSON to 55-byte CBOR for a device publishing every 10 seconds.
8. A web browser dashboard needs to display sensor data updated once per second. Compare HTTP polling, WebSocket, and MQTT WebSocket bridge as solutions. Which would you recommend and why?

---

## 9. Supplemental Resources

**1. OASIS MQTT Version 5.0 Specification**
[https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)
The authoritative MQTT specification from OASIS. MQTT 5.0 adds reason codes, user properties, shared subscriptions, and message expiry intervals to the MQTT 3.1.1 baseline. The Section 3 packet format tables are essential for understanding QoS handshakes, LWT, and session management.

**2. IETF RFC 7252 — The Constrained Application Protocol (CoAP)**
[https://www.rfc-editor.org/rfc/rfc7252](https://www.rfc-editor.org/rfc/rfc7252)
The CoAP specification. Sections 4 (message format), 5 (request-response semantics), and 7 (CoAP URIs) provide the technical depth behind Module 07 CoAP content. RFC 7641 (Observe) and RFC 7959 (Block-Wise Transfer) are companion documents.

**3. Eclipse Mosquitto Broker Documentation**
[https://mosquitto.org/documentation/](https://mosquitto.org/documentation/)
Configuration reference for the Mosquitto broker used in the Module 07 lab. Covers `listener`, `allow_anonymous`, `password_file`, `acl_file`, `max_keepalive`, `max_queued_messages`, and TLS configuration. The `mosquitto_pub` and `mosquitto_sub` command-line tools are documented here.
