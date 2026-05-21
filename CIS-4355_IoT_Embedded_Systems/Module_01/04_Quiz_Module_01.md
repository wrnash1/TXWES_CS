# Quiz: Module 01 - IoT Architecture – Devices, Gateways, Cloud, and Edge
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Which IoT architecture layer contains the sensors, actuators, and hardware components that interact with the physical environment?
*   A) Application Layer
*   B) Perception (Sensing) Layer
*   C) Network Layer
*   D) Support Layer
*   **Correct Answer:** B) The Perception layer handles physical signals (temperature, light, motion) and digitizes them for transmission.
*   **Distractor Analysis:**
    *   *Why correct:* The Perception layer handles physical signals (temperature, light, motion) and digitizes them for transmission.
    *   Network layer handles communications routing (gateways, routers); Application layer delivers processed data to end users.

---

**Question 2**
Which of the following is the most accurate definition of an **edge device** in an IoT architecture?
*   A) A cloud server that stores archived sensor data in a relational database for long-term reporting.
*   B) A compute node deployed close to the data source that processes sensor data locally to reduce latency and cloud bandwidth usage.
*   C) A software library used to parse JSON payloads received from an MQTT broker.
*   D) A certificate authority responsible for issuing TLS certificates to cloud application servers.
*   **Correct Answer:** B) A compute node deployed close to the data source that processes sensor data locally to reduce latency and cloud bandwidth usage.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A cloud server is in the cloud tier, not at the network edge near the devices.
    *   *Why B is correct:* Edge devices (e.g., Raspberry Pi, AWS Greengrass) run processing logic near the source to minimize latency and bandwidth usage.
    *   *Why C is incorrect:* A JSON parsing library is a software component, not a physical or logical edge compute node.
    *   *Why D is incorrect:* A certificate authority is a PKI service; it is not the same as an edge compute device.

---

**Question 3**
A smart building deploys 500 temperature sensors reporting every 5 seconds. The system must trigger an alarm within 200 ms of a spike. Which processing tier is most appropriate?
*   A) Batch processing in a centralized data warehouse queried once per day.
*   B) Edge/gateway processing on a local node co-located with the sensors.
*   C) A mobile application polling a REST API every 30 seconds.
*   D) Manual review by a technician reading raw log files.
*   **Correct Answer:** B) Edge/gateway processing on a local node co-located with the sensors.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Batch warehouse queries run on a schedule and cannot meet a 200 ms real-time alarm requirement.
    *   *Why B is correct:* Local edge processing eliminates round-trip latency to the cloud, enabling sub-second alarm responses.
    *   *Why C is incorrect:* A 30-second REST poll interval is far too slow for a 200 ms response requirement.
    *   *Why D is incorrect:* Manual log review introduces human latency and is unsuitable for automated safety alarms.

---

**Question 4**
In an IoT deployment, which of the following best describes the role of an **IoT gateway**?
*   A) A cloud service that trains machine learning models on historical sensor data.
*   B) A device that bridges local low-power wireless networks (e.g., Zigbee, BLE) to IP-based networks, performing protocol translation and device authentication.
*   C) A firmware update server that distributes signed binary images to microcontrollers.
*   D) A VLAN switch that enforces Quality of Service (QoS) rules on enterprise Wi-Fi traffic.
*   **Correct Answer:** B) A device that bridges local low-power wireless networks (e.g., Zigbee, BLE) to IP-based networks, performing protocol translation and device authentication.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ML model training is a cloud analytics function, not a gateway function.
    *   *Why B is correct:* Gateways sit at the boundary between constrained device networks and IP networks, translating protocols and managing device identities.
    *   *Why C is incorrect:* An OTA update server is a separate service, though a gateway may proxy firmware downloads.
    *   *Why D is incorrect:* A VLAN switch operates at Layer 2 and does not perform IoT protocol translation or device identity management.

---

**Question 5**
When securing an IoT system using a **defense-in-depth** approach, which combination of controls best addresses threats across all architecture layers?
*   A) Applying TLS only at the cloud API layer and relying on physical security for all other layers.
*   B) Using a single shared password across all devices to simplify credential management.
*   C) Enforcing unique device credentials at the Perception layer, encrypted transport at the Network layer, and authenticated APIs with least-privilege access at the Application layer.
*   D) Restricting firmware updates to devices that have already been physically inspected by a technician on-site.
*   **Correct Answer:** C) Enforcing unique device credentials at the Perception layer, encrypted transport at the Network layer, and authenticated APIs with least-privilege access at the Application layer.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Applying TLS only at the cloud boundary leaves device-to-gateway and broker communications unprotected.
    *   *Why B is incorrect:* Shared passwords violate least-privilege; a single compromised device exposes the entire fleet.
    *   *Why C is correct:* Defense-in-depth applies independent controls at every layer so a failure at one layer does not cascade through the system.
    *   *Why D is incorrect:* Manual on-site inspection does not scale and does not address network-layer or application-layer threats.
