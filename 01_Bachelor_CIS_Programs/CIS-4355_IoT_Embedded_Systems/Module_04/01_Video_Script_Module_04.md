# Video Script – Module 04: IoT Protocols – MQTT, CoAP, HTTP/REST, and Zigbee

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** CompTIA IoT+ Domain 3 – IoT Connectivity and Protocols

---

## Segment 1: Introduction and Learning Objectives [00:00 – 02:00]

Welcome to Module 04. I am Professor Nash. This module is one of the most protocol-heavy in the course, and it is heavily tested on the CompTIA IoT+ exam. We are going to cover MQTT, CoAP, HTTP/REST, and Zigbee — four protocols that together cover the vast majority of real-world IoT deployments.

By the end of this video you will be able to:

- Explain the publish-subscribe model used by MQTT and trace a message from publisher to subscriber.
- Describe CoAP's request-response model and explain why it runs over UDP rather than TCP.
- Compare MQTT, CoAP, HTTP/REST, and AMQP on the attributes that appear on exam questions: transport, overhead, broker requirement, and QoS.
- Explain how Zigbee forms a mesh network using IEEE 802.15.4 at the physical and MAC layers.
- Write a basic MQTT publish-subscribe example using the Paho Python client library.
- Identify the security risks associated with unprotected MQTT brokers.

Let us begin with the protocol that is most commonly tested: MQTT.

---

## Segment 2: MQTT – Message Queuing Telemetry Transport [02:00 – 08:00]

[SHOW DIAGRAM]

MQTT was designed in the late 1990s by Andy Stanford-Clark at IBM and Arlen Nipper for monitoring oil pipelines over satellite links. The design goals were: minimal bandwidth consumption, minimal battery drain on remote devices, and reliable message delivery over unreliable networks. These goals make MQTT perfect for IoT.

### The Publish-Subscribe Model

MQTT uses a publish-subscribe (pub/sub) pattern. There are three roles:

A publisher is a device (usually a sensor) that sends messages. It does not know or care who receives them. It only knows the topic it is publishing to.

A broker is a server that receives all published messages and routes them to the correct subscribers based on topic matching. The broker is the central hub. Popular brokers: Mosquitto (open source), AWS IoT Core, HiveMQ, EMQX.

A subscriber is a client that has registered interest in one or more topics. When a matching message is published, the broker delivers it to all matching subscribers. A subscriber does not know or care who published the message.

This decoupling is what makes MQTT scalable. Publishers and subscribers do not need to be connected at the same time, do not need to know each other's addresses, and do not need to coordinate.

### Topics and Wildcards

MQTT organizes messages into topics — forward-slash-delimited hierarchical strings. Examples:

- `home/livingroom/temperature`
- `campus/building-a/floor-2/sensor-05/co2`

A subscriber can subscribe to an exact topic or use wildcards:

- `+` matches any single level: `home/+/temperature` matches `home/livingroom/temperature` and `home/bedroom/temperature` but not `home/livingroom/humidity`.
- `#` matches any number of remaining levels: `campus/#` matches everything under `campus/`.

### QoS Levels

MQTT defines three Quality of Service levels:

QoS 0 – At most once (fire and forget). The publisher sends the message once. No acknowledgment. The message may be lost if the network fails. Lowest overhead.

QoS 1 – At least once. The broker acknowledges receipt with a PUBACK packet. If the publisher does not receive PUBACK, it retransmits. The message may be delivered multiple times. Subscribers must be idempotent.

QoS 2 – Exactly once. A four-packet handshake ensures the message is delivered exactly once: PUBLISH, PUBREC, PUBREL, PUBCOMP. Highest reliability, highest overhead.

For most sensor telemetry, QoS 0 or QoS 1 is appropriate. QoS 2 is used for payment transactions or actuator commands where duplicate delivery would cause physical harm.

### MQTT Security

The default MQTT port is 1883 (plaintext). MQTT over TLS uses port 8883. Without TLS, all telemetry is transmitted in plaintext — anyone on the network can read your sensor data and inject malicious messages.

For production: always use port 8883 with TLS, require client authentication (X.509 certificates or username/password), and configure per-topic access control lists so that a sensor can only publish to its own topic.

---

## Segment 3: MQTT Publish-Subscribe Code Example [08:00 – 11:30]

[SHOW CODE]

Let me show you a working MQTT publish-subscribe example using the Paho Python library. This is the library used in professional IoT deployments.

```python
# mqtt_publisher.py
# Publishes a temperature reading to an MQTT broker every 5 seconds
# Requires: pip install paho-mqtt

import paho.mqtt.client as mqtt
import time
import random

BROKER   = "test.mosquitto.org"  # public test broker (non-production)
PORT     = 1883
TOPIC    = "iot4355/temperature"
CLIENT_ID = "sensor-node-01"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed with code {}".format(rc))

client = mqtt.Client(client_id=CLIENT_ID)
client.on_connect = on_connect
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()   # start background thread for network I/O

try:
    while True:
        temperature = round(20.0 + random.uniform(-2, 5), 1)
        payload = '{{"sensor": "{}", "temp_c": {}}}'.format(CLIENT_ID, temperature)
        result = client.publish(TOPIC, payload, qos=1)
        print("Published: {}  rc={}".format(payload, result.rc))
        time.sleep(5)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
```

```python
# mqtt_subscriber.py
# Subscribes to the temperature topic and prints incoming messages

import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT   = 1883
TOPIC  = "iot4355/temperature"

def on_connect(client, userdata, flags, rc):
    print("Connected. Subscribing to {}".format(TOPIC))
    client.subscribe(TOPIC, qos=1)

def on_message(client, userdata, msg):
    print("Received on {}: {}".format(msg.topic, msg.payload.decode()))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, keepalive=60)
client.loop_forever()  # blocking loop — processes all incoming messages
```

The key concepts in this code:

`client.loop_start()` in the publisher starts a background thread that handles all network activity (reconnections, PUBACK processing) while the main thread publishes. `client.loop_forever()` in the subscriber is a blocking equivalent that runs until the script is terminated.

`on_connect` is a callback function that fires when the client establishes the TCP connection and receives CONNACK from the broker. You subscribe inside `on_connect` so that the subscription is restored automatically after reconnection.

`on_message` is a callback that fires every time a subscribed message arrives. The message object has `.topic`, `.payload` (bytes), and `.qos` attributes.

---

## Segment 4: CoAP – Constrained Application Protocol [11:30 – 14:30]

[SHOW DIAGRAM]

CoAP is defined in IETF RFC 7252 and is designed specifically for constrained nodes and constrained networks. Where MQTT uses TCP and a broker, CoAP uses UDP and a direct request-response pattern similar to HTTP.

### Why UDP?

TCP requires a three-way handshake and maintains state for every active connection. On a microcontroller with 16 KB of RAM connecting to a server, TCP overhead is manageable but non-trivial. UDP has no connection state — you send a packet and that is it. This makes CoAP faster to initiate and cheaper on memory.

The tradeoff is reliability: UDP provides no delivery guarantee. CoAP addresses this with message types:

- Confirmable (CON): the sender expects an ACK. If no ACK arrives within a timeout, the sender retransmits.
- Non-confirmable (NON): best-effort, no ACK required. Equivalent to MQTT QoS 0.

### CoAP Methods

CoAP uses the same four methods as HTTP: GET, POST, PUT, DELETE. This makes CoAP easy to map to REST semantics, which is why CoAP is sometimes called "HTTP for IoT." CoAP also adds an Observe extension (RFC 7641) that lets a client subscribe to a resource and receive updates when the resource changes — similar to MQTT's publish-subscribe.

### CoAP Security

CoAP is secured with DTLS (Datagram TLS), which is the UDP equivalent of TLS. DTLS adds encryption and authentication to UDP datagrams. Port 5683 is CoAP over plain UDP; port 5684 is CoAP over DTLS.

---

## Segment 5: HTTP/REST and AMQP in IoT [14:30 – 17:00]

### HTTP/REST

HTTP/REST is the default web protocol and is widely used in IoT cloud APIs, dashboards, and management interfaces. REST over HTTPS provides strong security through TLS and is easily debugged with standard tools. However, HTTP's per-request overhead — full headers, status lines, verbose text payloads — makes it unsuitable for constrained devices with strict bandwidth budgets.

HTTP is appropriate for: cloud-to-cloud API calls, device provisioning, dashboard data retrieval, and any IoT endpoint with reliable broadband connectivity.

HTTP is not appropriate for: battery-powered sensors on cellular data plans, high-frequency telemetry streams, or constrained microcontrollers without a full TCP/IP stack.

### AMQP

AMQP (Advanced Message Queuing Protocol) is an enterprise messaging protocol defined by OASIS. Like MQTT it is a pub/sub broker protocol, but it targets enterprise-grade reliability and security. AMQP supports complex routing logic, guaranteed delivery queues, transaction support, and granular message priority. RabbitMQ is the most widely deployed AMQP broker.

AMQP is common in industrial IoT backends and financial systems where guaranteed message delivery and complex routing are required. It is not used directly on constrained IoT devices — gateways translate from MQTT or CoAP to AMQP.

---

## Segment 6: Zigbee and IEEE 802.15.4 [17:00 – 20:00]

[SHOW DIAGRAM]

Zigbee is a wireless mesh networking protocol designed for low-data-rate, low-power, short-range IoT applications. It is based on IEEE 802.15.4 at the Physical and MAC layers.

### Physical Layer

Zigbee operates at 2.4 GHz globally (and 868 / 915 MHz in some regions). Maximum data rate is 250 kbps at 2.4 GHz. Transmission power is 1–10 mW. Line-of-sight range is 10–100 meters.

### Mesh Topology

Zigbee's defining feature is its self-healing mesh topology. Unlike star-topology protocols (BLE, Wi-Fi) where every device must reach the central access point, Zigbee devices can relay messages through each other.

Three device roles:

- Coordinator: one per network, initiates and maintains the network, stores the routing table.
- Router: forwards messages from other devices to extend network range.
- End Device: leaf node (usually a battery-powered sensor), cannot route, sleeps most of the time.

A message from an end device to the coordinator hops through routers. If one router fails, the mesh automatically finds an alternate route.

### Zigbee Security

Zigbee networks use AES-128 encryption for link-layer and network-layer security. The Trust Center (usually the coordinator) distributes encryption keys. Key vulnerabilities:

- Network key interception during joining: if the key is transmitted in plaintext during device join, an attacker listening can capture it.
- Default link keys: some devices ship with the default Zigbee link key publicly known, allowing any device to join.

Mitigation: use installcode-based joining (replaces broadcast link key with a device-specific derived key) and enable coordinator-side joining restrictions.

---

## Segment 7: Summary and Lab Preview [20:00 – 22:00]

Protocol selection summary: MQTT for low-overhead pub/sub telemetry over TCP. CoAP for constrained request-response over UDP. HTTP/REST for cloud APIs and high-bandwidth endpoints. AMQP for enterprise backend message routing. Zigbee for local wireless mesh sensor networks.

Security summary: all protocols require encrypted transport (TLS for TCP-based, DTLS for UDP-based) and device authentication. Unauthenticated MQTT brokers and Zigbee networks using default keys are among the most commonly exploited configurations in real IoT deployments.

In this week's lab you will configure a Paho MQTT publisher and subscriber in Python, trace the full broker message flow, and harden a simulated broker configuration by identifying and correcting insecure settings.

See you in Module 05 where we cover the radio technologies that carry all these protocols: Wi-Fi, Bluetooth, LoRaWAN, and NB-IoT.

---

End of Module 04 Video Script
