# Video Script: Module 07 — IoT Communication Protocols

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Estimated Duration:** 20–24 minutes

**Certification Alignment:** IoT Fundamentals / Embedded Systems

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4355. I'm Professor Nash. In Module 06 we learned how to make microcontrollers read sensors and control outputs. But a sensor that keeps its data to itself is not an IoT device — it is just an embedded system. The "Internet" part requires communication protocols.

Today we examine the four main protocols used to move data in IoT systems: MQTT, CoAP, HTTP/REST, and WebSockets. We will look at message formats — JSON and CBOR — and finish with a framework for choosing the right protocol for any given project constraint.

These protocols are not interchangeable. Each one makes a specific set of trade-offs between overhead, reliability, real-time capability, and implementation complexity. Understanding those trade-offs is what separates IoT architects from people who just make things blink.

---

## SEGMENT 2 — MQTT Architecture (1:30–5:30)

[SHOW HARDWARE: Laptop running Mosquitto broker, ESP32 connected over Wi-Fi, serial monitor visible]

MQTT stands for Message Queuing Telemetry Transport. It was designed in 1999 by Andy Stanford-Clark at IBM for monitoring oil pipelines over satellite links — an environment with high latency, unreliable connections, and extreme bandwidth constraints. Those same properties make it the dominant protocol in IoT today.

MQTT uses a publish-subscribe architecture. There is no direct device-to-device communication. Instead, all messages flow through a central server called a broker.

A device that produces data is a publisher. A device that consumes data is a subscriber. The broker sits in the middle, receiving publications and routing them to the correct subscribers. The routing key is a topic — a hierarchical slash-separated string such as `building/floor2/room14/temperature`.

Publishers and subscribers never need to know about each other. They only need to know the broker address and the topic string. This decoupling is one of MQTT's greatest strengths.

On an ESP32 using the PubSubClient library, connecting and publishing looks like this:

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid     = "YourNetwork";
const char* password = "YourPassword";
const char* broker   = "192.168.1.100";

WiFiClient   wifiClient;
PubSubClient mqtt(wifiClient);

void setup() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  mqtt.setServer(broker, 1883);
  mqtt.connect("esp32-sensor-01");
}

void loop() {
  if (!mqtt.connected()) mqtt.connect("esp32-sensor-01");
  mqtt.loop();

  float temp = readTemperature();
  char  payload[32];
  snprintf(payload, sizeof(payload), "%.2f", temp);
  mqtt.publish("building/floor2/room14/temperature", payload);
  delay(5000);
}
```

Topic wildcards are powerful. A `+` matches exactly one level. A `#` matches everything below a point in the hierarchy. Subscribing to `building/#` receives every topic under building, across all floors and rooms.

---

## SEGMENT 3 — MQTT QoS Levels (5:30–8:00)

MQTT defines three Quality of Service levels that control delivery guarantees.

QoS 0 is "at most once." The broker delivers the message once with no acknowledgment. If the network drops the packet, the message is lost. This is the fastest, lowest-overhead option. Use it when occasional lost readings are acceptable.

QoS 1 is "at least once." The sender retries until it receives a PUBACK acknowledgment from the broker. The message is guaranteed to arrive, but may arrive more than once if the acknowledgment is lost. Your subscriber must handle duplicates gracefully.

QoS 2 is "exactly once." A four-step handshake — PUBLISH, PUBREC, PUBREL, PUBCOMP — guarantees the message arrives exactly once. This is the safest option but produces four times the network traffic of QoS 0. Use it for commands like "open valve" where duplicate execution causes real problems.

MQTT also supports retained messages — the broker saves the last published message on a topic and delivers it immediately to new subscribers. This is invaluable for configuration and status topics.

---

## SEGMENT 4 — CoAP (8:00–10:00)

CoAP stands for Constrained Application Protocol. Where MQTT is publish-subscribe, CoAP is request-response — it looks a lot like HTTP but is designed for extremely constrained devices and lossy networks.

CoAP runs over UDP instead of TCP. UDP has much lower overhead: no connection setup, no flow control, no three-way handshake. A minimal CoAP message is just 4 bytes. Compare that to an HTTP request, which carries hundreds of bytes of headers.

CoAP supports GET, POST, PUT, and DELETE — the same four methods as HTTP. It also adds two CoAP-specific features: resource observation (server pushes updates when values change) and block-wise transfer for payloads larger than a single UDP datagram.

CoAP is the right choice when devices run on batteries, the network is 6LoWPAN or Zigbee, and you want REST semantics without HTTP overhead. It is dominant in smart metering and industrial sensor deployments.

---

## SEGMENT 5 — HTTP/REST for IoT (10:00–12:00)

HTTP is the foundation of the web, and many IoT devices use it because every cloud platform supports it and developers already know it.

Every HTTP request establishes a TCP connection, performs a TLS handshake if using HTTPS, sends 200–800 bytes of headers, receives a response, then tears down the connection. For a device sending one reading per minute, that overhead is acceptable. For a device sending 100 readings per second, it is catastrophic.

HTTP is the right choice when the device has sufficient RAM, data is sent infrequently, the destination is a REST API or webhook, and you need request-response confirmation of receipt.

On an ESP32, an HTTP POST to a REST API:

```cpp
#include <HTTPClient.h>

void sendReading(float temperature) {
  HTTPClient http;
  http.begin("https://api.example.com/readings");
  http.addHeader("Content-Type", "application/json");

  String body = "{\"temperature\":" + String(temperature, 2) + "}";
  int code = http.POST(body);

  Serial.printf("HTTP response: %d\n", code);
  http.end();
}
```

Note that this code uses the `String` class, which is acceptable on the ESP32 with its 520 KB SRAM. On an Uno, you would use a fixed-size char buffer.

---

## SEGMENT 6 — WebSockets (12:00–13:30)

WebSockets solve a specific problem: bidirectional, real-time communication over a single persistent TCP connection.

A WebSocket connection starts as an HTTP upgrade request. Once the server accepts, the connection upgrades to a full-duplex socket. Either side can send messages at any time with minimal overhead — just a 2-byte framing header for small messages.

WebSockets are ideal for dashboard applications where the browser needs live sensor data, for device control where the cloud sends commands to devices, and for any application requiring both push and pull on the same connection.

On the ESP32 the ArduinoWebsockets library provides client support. WebSockets are less suitable for battery-powered sensors because the persistent connection continuously consumes power and requires a full TCP/IP stack.

---

## SEGMENT 7 — Message Formats: JSON and CBOR (13:30–16:00)

Once you choose a transport protocol, you need a message format. The two most common in IoT are JSON and CBOR.

JSON is human-readable, universally supported, and trivial to parse in every programming language. The downside in IoT is verbosity. A JSON message for one temperature reading:

```cpp
// JSON payload — 52 bytes
const char* json = "{\"sensor_id\":\"room14\",\"temp\":23.45}";
```

CBOR is the Concise Binary Object Representation. It uses the same data model as JSON — objects, arrays, strings, numbers — but encodes them in binary. The same reading in CBOR is roughly 35% smaller and parses faster with less RAM. It is not human-readable, but it is well-suited for high-frequency telemetry and constrained devices.

Use JSON when debugging, flexibility, and human readability matter. Use CBOR when bandwidth is limited, the format is fixed, or the device processes thousands of messages per second. MessagePack is a third alternative — similar to CBOR and popular in high-performance APIs.

---

## SEGMENT 8 — Protocol Selection Framework (16:00–19:00)

How do you choose the right protocol? I use a five-factor framework.

**Factor 1: Device constraints.** Does the device have enough RAM for a TCP stack? An Arduino Uno with 2 KB SRAM cannot run MQTT reliably. An ESP32 with 520 KB can run MQTT, HTTP, and WebSockets simultaneously.

**Factor 2: Network characteristics.** Is the network reliable and low-latency, like Wi-Fi? Or lossy and high-latency, like cellular or LoRa? MQTT handles reconnection gracefully. HTTP assumes reliability. CoAP is designed for lossy links.

**Factor 3: Message frequency.** Sending one reading per hour — HTTP is fine. Sending 10 readings per second — MQTT QoS 0. Sending 1,000 readings per second — binary protocol over UDP.

**Factor 4: Directionality.** Does the cloud need to push commands to the device? HTTP polling is inefficient. MQTT subscriptions or WebSockets handle push cleanly.

**Factor 5: Reliability requirements.** Lost message acceptable — use QoS 0. Every message must arrive — use QoS 1 or 2. Exactly-once semantics required — use QoS 2.

| Scenario | Best Protocol |
|----------|---------------|
| Battery-powered mesh sensor | CoAP over 6LoWPAN |
| Cloud telemetry, many devices | MQTT QoS 0 or 1 |
| Device receives cloud commands | MQTT subscribe |
| One-time REST webhook | HTTP POST |
| Live browser dashboard | WebSocket |
| Extremely constrained bandwidth | CBOR + MQTT |

---

## SEGMENT 9 — MQTT Broker Options (19:00–21:00)

The MQTT broker is the heart of any MQTT-based system. You have three main options.

**Local self-hosted:** Mosquitto is the most widely used open-source broker. It runs on a Raspberry Pi, a Linux server, or a Docker container. Excellent for labs, home automation, and industrial sites where data must stay on-premises.

**Cloud-managed:** HiveMQ Cloud, AWS IoT Core, Azure IoT Hub, and Google Cloud IoT all provide managed MQTT brokers with authentication, TLS, and scalability built in. Suitable for production systems with thousands of devices.

**Development and testing:** broker.hivemq.com and test.mosquitto.org are free public brokers for testing. Never send sensitive data to them — they are completely public.

Broker configuration essentials: always enable TLS on port 8883 instead of the unencrypted port 1883, use client certificates or username/password authentication, and configure access control lists to restrict which clients can publish or subscribe to which topics.

---

## SEGMENT 10 — Wrap-Up and Preview (21:00–23:00)

Let's recap. MQTT's publish-subscribe model is the dominant IoT messaging pattern — lightweight, decoupled, and flexible with QoS levels for different reliability needs. CoAP brings REST semantics to ultra-constrained environments. HTTP/REST is familiar and widely supported but too heavy for high-frequency telemetry. WebSockets enable real-time bidirectional communication over a persistent connection. JSON is readable; CBOR is compact.

The five-factor selection framework — device constraints, network characteristics, message frequency, directionality, and reliability — gives you a principled way to choose the right protocol every time.

In Module 08 we move to sensor integration. You will connect temperature, humidity, motion, and light sensors to your microcontroller, work with I2C and SPI bus protocols, and implement data smoothing algorithms that turn noisy raw ADC readings into reliable measurements.

See you there.

---

## PRODUCTION NOTES

- B-roll: Wireshark capture of MQTT packets, HiveMQ dashboard with live message flow, ESP32 serial monitor showing successful publish
- Slide: QoS comparison table with animated send/acknowledge arrows for each level
- Demo: Live mosquitto_sub terminal window showing messages arriving from ESP32
- Closed captions: verify MQTT, CoAP, CBOR, PubSubClient, QoS, idempotent, 6LoWPAN, PUBACK
- Run time target: 22 minutes
