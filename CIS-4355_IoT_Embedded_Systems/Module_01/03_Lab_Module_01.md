# Lab Activity – Module 01: IoT Architecture – Devices, Gateways, Cloud, and Edge

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Points:** 100
**Submission:** Canvas – Module 01 Lab Assignment

---

## Overview

In this lab you will apply the four-layer IoT architecture model to a realistic smart campus scenario. You will map components to architecture layers, trace a data-flow path from sensor to dashboard, identify trust boundaries, and analyze a simulated MQTT message trace. No physical hardware is required. All work is analytical and documented.

---

## Learning Objectives

By completing this lab you will be able to:

- Place any IoT system component into the correct architecture layer.
- Draw an annotated IoT architecture diagram showing data flow direction and protocols.
- Identify trust boundaries and specify security controls at each boundary.
- Read an MQTT message trace and explain what happens at each protocol layer.
- Justify an edge-versus-cloud processing decision given specific latency and bandwidth constraints.

---

## Prerequisites

- Completed Module 01 video lecture.
- Completed Module 01 Reading Guide sections 1 through 5.
- Drawing tool of your choice: pen and paper (photograph the result), draw.io at diagrams.net, Lucidchart, PowerPoint, or any diagram application.
- Text editor or word processor for written responses.

---

## Scenario: Rampage Hall Smart Campus Building

Texas Wesleyan has deployed a smart building system in Rampage Hall. The system includes the following 12 components:

1. 40 DHT22 temperature and humidity sensors installed in classrooms and hallways.
2. 8 PIR motion sensors at building entrances and exits.
3. 4 CO2 sensors (MQ-135 module) in large lecture rooms.
4. An ESP32 microcontroller in each sensor housing that reads the sensor and transmits over BLE.
5. A Raspberry Pi 4 gateway in the building's IT closet that receives all BLE transmissions and publishes to an MQTT broker.
6. A campus Wi-Fi access point providing the gateway's uplink to the internet.
7. A Mosquitto MQTT broker running on a campus server.
8. An InfluxDB time-series database receiving MQTT data from the broker.
9. A Node-RED rules engine that evaluates CO2 levels and triggers alerts.
10. A web dashboard on a facilities manager's PC showing live sensor readings.
11. An SMS alert service that notifies the HVAC team when CO2 exceeds 1,000 ppm.
12. A campus facilities manager's smartphone running the monitoring mobile app.

---

## Part 1: Architecture Layer Mapping (25 points)

### Part 1 Instructions

Create a table with four columns: Component Number, Component Name, Architecture Layer, and Justification (one sentence explaining your placement).

Place each of the 12 components listed in the scenario into one of the four layers: Perception, Network, Processing/Middleware, or Application.

Expected table format:

| Component | Name | Layer | Justification |
|---|---|---|---|
| 1 | DHT22 sensor | (your answer) | (your one-sentence justification) |
| ... | ... | ... | ... |

### Part 1 Grading Rubric

| Criterion | Points |
|---|---|
| All 12 components placed in correct layer | 20 |
| Each placement includes a valid one-sentence justification | 5 |
| Total | 25 |

---

## Part 2: Architecture Diagram (25 points)

### Part 2 Instructions

Draw a layered IoT architecture diagram for the Rampage Hall scenario. Your diagram must include:

- Four labeled horizontal bands representing the four architecture layers.
- All 12 components placed in the correct band.
- Arrows showing the direction of data flow between components, labeled with the protocol name (BLE, MQTT, HTTP, etc.).
- Three clearly marked trust boundary lines: one between the Perception and Network layers, one between the Network and Processing layers, and one between the Processing and Application layers.
- A security control label at each trust boundary (example: "TLS 1.3 mutual authentication").

Submit your diagram as a PNG, JPEG, or PDF file attached to your Canvas submission.

### Part 2 Grading Rubric

| Criterion | Points |
|---|---|
| All 12 components appear in the correct layer band | 10 |
| Data flow arrows present with correct protocol labels | 8 |
| Three trust boundaries marked with security control labels | 7 |
| Total | 25 |

---

## Part 3: Data Flow Trace (20 points)

### Part 3 Instructions

Write a numbered step-by-step narrative (minimum 8 steps) tracing the complete path of a single CO2 reading from the moment the MQ-135 sensor measures 1,050 ppm until the HVAC technician receives an SMS alert. For each step identify:

- The component performing the action.
- The layer that component belongs to.
- The protocol or interface used to pass data to the next step.

Example step format (do not copy — write your own original trace):

Step 1: The MQ-135 CO2 sensor (Perception layer) outputs an analog voltage corresponding to 1,050 ppm. The ESP32 microcontroller reads the ADC value and converts it to a ppm reading using a calibration formula.

### Part 3 Grading Rubric

| Criterion | Points |
|---|---|
| Minimum 8 steps present | 5 |
| Each step correctly identifies component and layer | 10 |
| Protocol or interface correctly named at each transition | 5 |
| Total | 20 |

---

## Part 4: MQTT Message Trace Analysis (15 points)

### Part 4 Instructions

Examine the following simulated MQTT message trace and answer the five questions below.

```text
[00:00.001] CONNECT  client_id=esp32-sensor-42  clean_session=true
[00:00.045] CONNACK  return_code=0  session_present=false
[00:00.046] PUBLISH  topic=campus/rampagehall/room204/co2
             payload={"ts":1717300800,"ppm":1050,"unit":"ppm"}
             qos=1  retain=false  message_id=101
[00:00.091] PUBACK   message_id=101
[00:00.092] SUBSCRIBE  topic=campus/rampagehall/room204/+  qos=1
[00:00.103] SUBACK   message_id=102  granted_qos=1
[00:05.001] PUBLISH  topic=campus/rampagehall/room204/co2
             payload={"ts":1717300805,"ppm":1048,"unit":"ppm"}
             qos=1  retain=false  message_id=103
[00:05.047] PUBACK   message_id=103
[00:10.000] PINGREQ
[00:10.022] PINGRESP
```

Answer each question in complete sentences:

1. What does the CONNECT/CONNACK exchange accomplish, and why does clean_session=true matter for a sensor device?
2. The PUBLISH uses QoS level 1. Explain what QoS 1 guarantees and how the PUBACK packet fits into that guarantee.
3. What does the wildcard character (+) in the SUBSCRIBE topic pattern match? Give one example of a topic it would match and one it would not.
4. What is the purpose of the PINGREQ/PINGRESP exchange, and when would a device typically send one?
5. If this traffic were captured on the network without TLS, what specific data would an attacker be able to read?

### Part 4 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1 answered correctly (clean_session=true effect) | 3 |
| Question 2 answered correctly (QoS 1 guarantee and PUBACK role) | 3 |
| Question 3 answered with correct wildcard example and counter-example | 3 |
| Question 4 answered correctly (keepalive purpose) | 3 |
| Question 5 identifies specific exposed data elements | 3 |
| Total | 15 |

---

## Part 5: Edge vs. Cloud Decision Justification (15 points)

### Part 5 Instructions

Read each of the three scenarios below. For each one, state whether edge processing, cloud processing, or a hybrid of both is the best choice. Write a 3–5 sentence justification that references specific latency, bandwidth, or connectivity factors from the scenario.

Scenario A: A natural gas pipeline monitoring system samples pressure sensors every 100 milliseconds along 500 miles of pipe. If pressure drops more than 10 percent in under 500 ms, a valve must close automatically to prevent a rupture. The pipeline crosses remote terrain with no cellular coverage for 40 percent of its length.

Scenario B: A retail chain deploys foot-traffic counters in 2,000 store locations nationwide. Each counter sends one occupancy reading per minute. Store managers view weekly trend reports on a headquarters dashboard.

Scenario C: A smart hospital deploys ventilators with embedded sensors that stream waveform data at 200 Hz. A machine learning model must detect patient-ventilator asynchrony and alert the nurse within 2 seconds. The hospital also needs to train improved models on 6 months of historical waveform data.

### Part 5 Grading Rubric

| Criterion | Points |
|---|---|
| Correct processing tier selected for each scenario | 6 |
| Each justification references a specific latency or bandwidth factor | 6 |
| Hybrid choice for Scenario C explains edge role and cloud role separately | 3 |
| Total | 15 |

---

## Submission Checklist

Before submitting, verify you have included:

- [ ] Part 1: Component mapping table (all 12 rows complete).
- [ ] Part 2: Architecture diagram file (PNG, JPEG, or PDF).
- [ ] Part 3: Data flow trace narrative (minimum 8 numbered steps).
- [ ] Part 4: MQTT trace analysis (all 5 questions answered).
- [ ] Part 5: Edge vs. cloud justifications (all 3 scenarios addressed).

Submit all items as a single PDF or as a combined Canvas submission with the diagram attached separately.

---

## Overall Grading Summary

| Part | Description | Points |
|---|---|---|
| 1 | Architecture layer mapping | 25 |
| 2 | Architecture diagram | 25 |
| 3 | Data flow trace | 20 |
| 4 | MQTT trace analysis | 15 |
| 5 | Edge vs. cloud justification | 15 |
| Total | | 100 |

---

End of Lab – Module 01
