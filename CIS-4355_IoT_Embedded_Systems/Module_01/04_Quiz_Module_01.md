# Quiz – Module 01: IoT Architecture – Devices, Gateways, Cloud, and Edge

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Format:** 10 questions, multiple choice, 4 options each
**Certification Alignment:** CompTIA IoT+ Domain 1

---

## Question 1

Which IoT architecture layer contains sensors, actuators, and the embedded microcontrollers that digitize physical measurements?

- A) Application Layer
- B) Network Layer
- C) Perception Layer
- D) Processing and Middleware Layer

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The Application layer is the top tier containing dashboards, mobile apps, and APIs. It consumes processed data rather than collecting raw physical measurements.
- B is incorrect: The Network layer handles communication infrastructure — gateways, radios, and routers — not physical sensing or actuation.
- C is correct: The Perception layer is the bottom tier where physical signals are sensed, digitized, and prepared for transmission. Sensors, actuators, RFID tags, and their embedded controllers all belong here.
- D is incorrect: The Processing layer handles brokering, filtering, and storage of data after it has been received from the network. It does not interact directly with the physical environment.

---

## Question 2

Which of the following most accurately distinguishes an edge device from a gateway?

- A) A gateway runs local analytics; an edge device only translates protocols.
- B) An edge device runs local analytics and processing logic; a gateway primarily translates protocols.
- C) An edge device connects to the cloud directly; a gateway does not require internet access.
- D) A gateway requires more CPU and RAM than an edge device.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The description has the two devices reversed. Gateways translate protocols; edge devices run processing logic.
- B is correct: The defining characteristic of an edge device is local compute capability — running algorithms, models, or control logic. A gateway's primary role is protocol translation and buffering.
- C is incorrect: Both edge devices and gateways typically require some internet connectivity. The distinction is processing capability, not connectivity path.
- D is incorrect: Edge devices generally require more computational resources than simple gateways because they run analytics workloads.

---

## Question 3

A smart building deploys 500 temperature sensors reporting every 5 seconds. The system must trigger an alarm within 200 ms of detecting a spike above threshold. Which processing tier best meets this requirement?

- A) Batch processing in a centralized cloud data warehouse queried once per day.
- B) Manual review of raw log files by a technician.
- C) A mobile application polling a cloud REST API every 30 seconds.
- D) Edge processing on a gateway co-located with the sensors.

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: Batch warehouse processing runs on a schedule — once per day — making it incapable of generating a 200 ms alarm.
- B is incorrect: Manual log review introduces human-scale latency, far exceeding the 200 ms requirement.
- C is incorrect: Polling every 30 seconds means up to 30,000 ms of detection delay, 150 times slower than the requirement.
- D is correct: Local edge processing eliminates cloud round-trip latency. A gateway co-located with the sensors can evaluate readings and trigger alarms in well under 200 ms.

---

## Question 4

Which of the following best describes the role of an IoT gateway?

- A) A cloud service that trains machine learning models on historical sensor telemetry.
- B) A firmware update server that distributes signed binary images to microcontrollers over the internet.
- C) A device that bridges local low-power wireless networks to IP-based networks and performs protocol translation.
- D) A VLAN switch that enforces Quality of Service rules on enterprise traffic.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: ML model training is a cloud analytics function. Gateways do not train models.
- B is incorrect: An OTA firmware update server is a separate infrastructure component. A gateway may proxy firmware downloads but is not the update server itself.
- C is correct: Gateways sit at the boundary between constrained device networks (Zigbee, BLE, Modbus) and IP networks, performing protocol translation, local caching, and device authentication.
- D is incorrect: A VLAN switch operates at Layer 2 of the OSI model and does not perform IoT-specific protocol translation or device identity management.

---

## Question 5

A defense-in-depth security strategy for IoT systems applies independent controls at every architecture layer. Which combination best represents this approach?

- A) Applying TLS only at the cloud API and relying on physical security for all other layers.
- B) Using a single shared password across all devices to simplify credential management.
- C) Enforcing unique device credentials at the Perception layer, encrypted transport at the Network layer, and authenticated APIs with least-privilege access at the Application layer.
- D) Restricting firmware updates to devices physically inspected by a technician on site.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Protecting only the cloud boundary leaves device-to-gateway communications completely unprotected. Defense in depth requires controls at every layer.
- B is incorrect: A single shared password violates least-privilege; one compromised device exposes the entire fleet. This is OWASP IoT Top 10 item 1.
- C is correct: Defense in depth applies independent controls at every layer so that compromise of one layer does not cascade throughout the system. Each layer has its own appropriate control.
- D is incorrect: Manual physical inspection does not scale to large deployments and does not address network-layer or application-layer threats.

---

## Question 6

Which IoT architecture layer is responsible for hosting message brokers, stream processors, and time-series databases?

- A) Perception Layer
- B) Network Layer
- C) Application Layer
- D) Processing and Middleware Layer

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: The Perception layer contains only physical sensing and actuation hardware with minimal embedded firmware.
- B is incorrect: The Network layer handles communication transport. It carries messages but does not store or process them.
- C is incorrect: The Application layer presents processed data to users. It consumes data from the processing layer rather than operating message brokers.
- D is correct: The Processing and Middleware layer is where message brokers (MQTT, AMQP), stream processors (Kafka, Flink), and time-series databases (InfluxDB) operate.

---

## Question 7

A soil moisture sensor deployed in a remote agricultural field transmits one reading per hour over LoRaWAN. The sensor operates on a battery expected to last 18 months. Which wireless technology characteristic makes LoRaWAN the appropriate choice here?

- A) High bandwidth suitable for streaming video from the field.
- B) Very long range combined with extremely low power consumption.
- C) Low latency required for real-time irrigation valve control.
- D) Licensed spectrum ensuring guaranteed quality of service.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: LoRaWAN maximum data rate is 50 kbps — far too low for video streaming. Wi-Fi or LTE would be required for video.
- B is correct: LoRaWAN is an LPWAN technology specifically designed for long-range (2–15 km) communication at extremely low power consumption, enabling multi-year battery life for infrequent transmissions.
- C is incorrect: LoRaWAN is not a low-latency technology. It is optimized for low duty-cycle, infrequent transmissions, not for real-time control.
- D is incorrect: LoRaWAN operates on unlicensed spectrum (915 MHz in the US). NB-IoT uses licensed cellular spectrum.

---

## Question 8

In an IoT architecture, a trust boundary is defined as a point where data moves between zones of different trust levels. Which action is always required when data crosses a trust boundary?

- A) Compressing the data to reduce transmission time.
- B) Converting the data from JSON to binary format.
- C) Authenticating the source, encrypting the data in transit, and validating the content.
- D) Caching the data locally for 24 hours before forwarding.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Compression is a performance optimization, not a security requirement at trust boundaries.
- B is incorrect: Format conversion may occur at gateways but is unrelated to the security requirements of a trust boundary.
- C is correct: All three controls — authentication (verify who is sending), encryption (protect the data in transit), and input validation (reject malformed or malicious content) — are required at every trust boundary.
- D is incorrect: Local caching is a reliability feature unrelated to trust boundary security enforcement.

---

## Question 9

Which layer of the IoT architecture is the primary target for attacks exploiting weak API authentication and insecure web interfaces?

- A) Perception Layer
- B) Network Layer
- C) Application Layer
- D) Processing and Middleware Layer

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The Perception layer is targeted by physical attacks and hardcoded credential exploits, not web API attacks.
- B is incorrect: The Network layer is targeted by man-in-the-middle and eavesdropping attacks, not API authentication exploits.
- C is correct: The Application layer hosts the web interfaces, REST APIs, and mobile app backends. Weak authentication and insecure interfaces at this layer allow attackers to issue unauthorized commands or exfiltrate data.
- D is incorrect: The Processing layer may host broker management interfaces, but the primary attack surface for web and mobile API authentication is the Application layer.

---

## Question 10

An engineer is designing a factory monitoring system where vibration sensors generate 50,000 samples per second per machine. Sending raw data to the cloud is too expensive. A machine learning model must also respond to detected faults within 50 ms. Which architecture decision best addresses both constraints?

- A) Increase cloud bandwidth to handle the full raw data stream.
- B) Deploy edge compute nodes at each machine to run local inference and send only result scores to the cloud.
- C) Reduce the sensor sampling rate to 1 sample per second to fit within budget.
- D) Store all raw data on the sensor's onboard flash memory and retrieve it manually each week.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Increasing bandwidth addresses cost but does not meet the 50 ms latency requirement because cloud round-trip time far exceeds 50 ms.
- B is correct: Local edge inference eliminates cloud round-trip latency (meeting the 50 ms requirement) and reduces upstream bandwidth to compressed result scores rather than raw waveforms (meeting the cost constraint).
- C is incorrect: Reducing the sampling rate may destroy the signal features needed for fault detection. This compromises the system's primary purpose.
- D is incorrect: Weekly manual retrieval cannot support real-time fault detection and provides no remote monitoring capability.

---

End of Quiz – Module 01
