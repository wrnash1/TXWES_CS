# Lab Activity – Module 04: IoT Protocols – MQTT, CoAP, HTTP/REST, and Zigbee

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Points:** 100
**Submission:** Canvas – Module 04 Lab Assignment

---

## Overview

In this lab you will implement a complete MQTT publish-subscribe system using the Paho Python library, trace the MQTT broker message flow, and analyze a misconfigured broker for security vulnerabilities. You will also compare protocol characteristics across MQTT, CoAP, HTTP/REST, and AMQP through structured analysis questions.

---

## Learning Objectives

By completing this lab you will be able to:

- Install and import the Paho MQTT Python library.
- Write a functioning MQTT publisher that connects to a broker and publishes timestamped JSON payloads.
- Write a functioning MQTT subscriber with `on_connect` and `on_message` callbacks.
- Trace the sequence of MQTT control packets for a QoS 1 publish-subscribe transaction.
- Identify broker misconfigurations that expose MQTT deployments to OWASP IoT vulnerabilities.
- Compare MQTT, CoAP, HTTP/REST, and AMQP on protocol-specific attributes.

---

## Prerequisites

- Python 3.8 or later with pip available.
- Install the Paho MQTT library: `pip install paho-mqtt`
- A text editor or IDE (VS Code, PyCharm, or any editor).
- Internet access to connect to the public Mosquitto test broker (test.mosquitto.org) for Parts 1 and 2.

Note on the public test broker: test.mosquitto.org is a public resource for testing. Do not publish sensitive data to it. For production use, deploy your own Mosquitto instance.

---

## Part 1: MQTT Publisher Implementation (30 points)

### Part 1 Background

The Paho MQTT Python client provides `mqtt.Client` as the central class. Key methods:

- `client.connect(host, port, keepalive)` — establishes the TCP connection.
- `client.loop_start()` — starts a background network thread.
- `client.publish(topic, payload, qos)` — publishes a message.
- `client.disconnect()` — cleanly closes the connection.

### Part 1 Code Task

Write a Python script named `lab04_publisher.py` that satisfies all of the following requirements:

- Imports `paho.mqtt.client`, `time`, `json`, and `datetime`.
- Defines constants: `BROKER = "test.mosquitto.org"`, `PORT = 1883`, `TOPIC = "iot4355/lab04/YOUR_FIRSTNAME"` (replace YOUR_FIRSTNAME with your actual first name so your topic is unique on the shared broker).
- Creates an MQTT client with a unique `client_id`.
- Defines an `on_connect` callback that prints "Connected to broker: [BROKER]" when `rc == 0` and "Connection failed: [rc]" otherwise.
- Connects to the broker and starts the loop.
- Runs a loop that publishes 10 messages total, one every 3 seconds.
- Each message payload is a JSON string with these fields:
  - `sensor_id`: your first name as a string
  - `seq`: the message sequence number (1 through 10)
  - `temperature`: a float between 18.0 and 28.0 (use any value, fixed or random)
  - `timestamp`: the current UTC time as an ISO 8601 string using `datetime.utcnow().isoformat()`
- Publishes each message with QoS 1.
- Prints each published payload to the terminal.
- After the 10th message, stops the loop and disconnects cleanly.

### Part 1 Starter Structure

```python
# lab04_publisher.py
# Module 04 Lab – MQTT Publisher
# Course: CIS-4355 IoT and Embedded Systems

import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime

# TASK 1: Define BROKER, PORT, TOPIC constants (use your first name in the topic)
# TASK 2: Define on_connect callback
# TASK 3: Create mqtt.Client with a unique client_id
# TASK 4: Assign on_connect callback to client
# TASK 5: Connect and start loop
# TASK 6: Loop to publish 10 messages with 3-second intervals
# TASK 7: Stop loop and disconnect after 10 messages
```

### Part 1 Deliverables

- Complete `lab04_publisher.py` source code.
- Terminal screenshot showing all 10 published messages with timestamps and sequence numbers.

### Part 1 Grading Rubric

| Criterion | Points |
|---|---|
| All 7 TASK sections implemented correctly | 18 |
| JSON payload contains all four required fields | 6 |
| QoS 1 used for all publishes | 3 |
| Terminal screenshot shows 10 messages with correct format | 3 |
| Total | 30 |

---

## Part 2: MQTT Subscriber Implementation (30 points)

### Part 2 Background

The subscriber must be running before (or simultaneously with) the publisher to receive messages. Run the subscriber in one terminal window and the publisher in another. The `client.loop_forever()` call blocks the subscriber indefinitely, processing incoming messages as they arrive.

### Part 2 Code Task

Write a Python script named `lab04_subscriber.py` that satisfies all of the following requirements:

- Uses the same broker, port, and topic constants as your publisher.
- Defines an `on_connect` callback that subscribes to the topic inside the callback (so re-subscriptions occur automatically after reconnect) using QoS 1.
- Defines an `on_message` callback that:
  - Decodes the payload from bytes to a UTF-8 string.
  - Parses the JSON payload using `json.loads()`.
  - Prints a formatted line: `[Received] seq=N  temp=XX.X C  from=SENSOR_ID  at=TIMESTAMP`
- Connects to the broker and calls `client.loop_forever()`.

### Part 2 Starter Structure

```python
# lab04_subscriber.py
# Module 04 Lab – MQTT Subscriber
# Course: CIS-4355 IoT and Embedded Systems

import paho.mqtt.client as mqtt
import json

# TASK 1: Define BROKER, PORT, TOPIC constants (match your publisher exactly)
# TASK 2: Define on_connect callback that subscribes inside the callback
# TASK 3: Define on_message callback with formatted output
# TASK 4: Create client, assign callbacks, connect, and call loop_forever()
```

### Part 2 Deliverables

- Complete `lab04_subscriber.py` source code.
- Terminal screenshot showing the subscriber receiving all 10 messages published by your publisher.
- The screenshot must show both terminal windows (publisher and subscriber) simultaneously, or two separate screenshots taken at the same session.

### Part 2 Grading Rubric

| Criterion | Points |
|---|---|
| All 4 TASK sections implemented correctly | 18 |
| on_message correctly parses JSON and prints formatted output | 6 |
| Subscription is performed inside on_connect (not in main code) | 3 |
| Screenshot shows subscriber receiving published messages | 3 |
| Total | 30 |

---

## Part 3: MQTT Broker Message Flow Trace (15 points)

### Part 3 Instructions

Using the MQTT control packet trace below, answer each question in complete sentences.

```text
TIME    DIRECTION       PACKET          DETAILS
0.001   Client->Broker  CONNECT         client_id=lab04-publisher  clean_session=1
0.045   Broker->Client  CONNACK         return_code=0  session_present=0
0.046   Client->Broker  PUBLISH         topic=iot4355/lab04/alice
                                        payload={"sensor_id":"alice","seq":1,"temperature":22.4}
                                        qos=1  message_id=1
0.089   Broker->Client  PUBACK          message_id=1
0.090   Subscriber      PUBLISH         (broker delivers to subscriber)
                                        topic=iot4355/lab04/alice
                                        payload={"sensor_id":"alice","seq":1,"temperature":22.4}
0.150   Client->Broker  DISCONNECT
```

Question 1: What does `return_code=0` in the CONNACK packet signify? What would a non-zero return code indicate?

Question 2: Explain the purpose of `message_id=1` in the PUBLISH packet and how the broker uses it during the QoS 1 acknowledgment exchange.

Question 3: The PUBACK at 0.089 ms acknowledges receipt by the broker, not receipt by the subscriber. Explain what "at-least-once delivery" means in this context and what could happen to the message if the publisher disconnected between 0.046 and 0.089.

Question 4: The subscriber receives the message at 0.090 ms. If the subscriber had been offline when the message was published and reconnected later, would it receive the message? Under what condition would it?

Question 5: This trace uses port 1883 (plaintext). Identify two specific security risks visible in the unencrypted payload shown in the trace, and describe the required configuration change.

### Part 3 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: return_code=0 meaning and non-zero implication correct | 3 |
| Question 2: message_id role in QoS 1 handshake explained correctly | 3 |
| Question 3: at-least-once delivery semantics accurate, disconnection scenario correct | 3 |
| Question 4: offline subscriber behavior and persistent session condition accurate | 3 |
| Question 5: two security risks identified and configuration fix stated | 3 |
| Total | 15 |

---

## Part 4: Protocol Comparison and Security Analysis (25 points)

### Part 4 Instructions

Answer each question in complete sentences with specific technical detail.

Question 1: An engineer must choose between MQTT QoS 1 and CoAP Confirmable (CON) messages for a temperature sensor that sends readings every 30 seconds over a 4G cellular connection. The system budget allows a maximum of 200 bytes per reading including all protocol overhead. Compare the two protocols on at least three attributes (transport, overhead, broker requirement, and security transport) and recommend one with justification.

Question 2: A smart city deploys 5,000 smart streetlights. Each light has a Zigbee end device node. A city engineer proposes replacing the Zigbee mesh with direct Wi-Fi connections from each light to a central Wi-Fi access point. Identify three specific technical problems with the Wi-Fi proposal that the Zigbee mesh solves, referencing Zigbee's mesh topology, power characteristics, and data rate requirements.

Question 3: An IoT platform architect discovers that the company's MQTT broker is accessible on port 1883 with no authentication and is broadcasting all device telemetry including GPS coordinates and door-lock status to any subscriber. Identify the OWASP IoT Top 10 items violated, describe the exact attack scenarios each enables, and provide a specific broker configuration recommendation for each item that resolves the violation.

### Part 4 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: Three attributes compared accurately, recommendation justified | 9 |
| Question 2: Three technical problems correctly identified and linked to Zigbee capabilities | 8 |
| Question 3: Correct OWASP items cited, attack scenarios described, configurations specified | 8 |
| Total | 25 |

---

## Submission Checklist

- [ ] Part 1: `lab04_publisher.py` source code and terminal screenshot (10 messages).
- [ ] Part 2: `lab04_subscriber.py` source code and terminal screenshot (receiving 10 messages).
- [ ] Part 3: All 5 trace analysis questions answered.
- [ ] Part 4: All 3 protocol analysis questions answered.

---

## Overall Grading Summary

| Part | Description | Points |
|---|---|---|
| 1 | MQTT publisher | 30 |
| 2 | MQTT subscriber | 30 |
| 3 | Broker message flow trace | 15 |
| 4 | Protocol comparison and security | 25 |
| Total | | 100 |

---

End of Lab – Module 04
