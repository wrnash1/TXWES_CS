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

---

### Question 11 (5 points)

Which serial communication protocol uses a master-slave topology, requires only two wires (SDA and SCL), and supports multiple devices sharing the same bus using unique 7-bit addresses?

- A) UART
- B) SPI
- C) I2C
- D) 1-Wire

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) UART is a point-to-point asynchronous protocol using TX/RX lines. It does not support multi-device addressing on a shared bus.
  - B) SPI uses four wires (MOSI, MISO, SCK, SS) and selects devices via individual chip-select lines rather than addressing.
  - C) I2C (Inter-Integrated Circuit) uses two wires — SDA (data) and SCL (clock) — and addresses each device with a unique 7-bit (or 10-bit extended) address, allowing dozens of devices on a single bus.
  - D) 1-Wire uses a single data line and is capable of multi-drop addressing, but it is a separate protocol distinct from I2C and operates at much lower speeds.

---

### Question 12 (5 points)

A Raspberry Pi GPIO pin configured as a digital output is connected directly to the anode of an LED. The cathode is connected to ground through a 330 Ω resistor. The GPIO pin outputs 3.3 V at a maximum current of 16 mA. Approximately how much current flows through the LED?

- A) 0 mA — the GPIO pin cannot source current to an LED.
- B) Approximately 10 mA
- C) Approximately 33 mA — the resistor limits current to a safe level.
- D) Exactly 16 mA — the GPIO pin's max current rating sets the current.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Raspberry Pi GPIO pins can source and sink up to 16 mA when configured as outputs. Current can flow through an LED connected directly to the pin.
  - B) Using Ohm's law: V = 3.3 V, forward voltage drop of a typical red LED ≈ 2.0 V, so V_R = 1.3 V. I = V_R / R = 1.3 / 330 ≈ 3.9–10 mA depending on the specific LED — well within the safe operating range.
  - C) 33 mA would require 10.9 V across the 330 Ω resistor, far exceeding the 3.3 V supply. The arithmetic is incorrect.
  - D) The GPIO maximum rating is a ceiling, not a fixed output current. Actual current is determined by the circuit resistance and voltage per Ohm's law.

---

### Question 13 (5 points)

Which MicroPython statement correctly imports the machine module and configures GPIO pin 4 as a push-pull output on an ESP32?

- A) `import gpio; gpio.pin(4, gpio.OUTPUT)`
- B) `from machine import Pin; p = Pin(4, Pin.OUT)`
- C) `import RPi.GPIO as GPIO; GPIO.setup(4, GPIO.OUT)`
- D) `import wiringpi; wiringpi.pinMode(4, 1)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) There is no standard MicroPython module called `gpio`. The correct module is `machine`.
  - B) The `machine.Pin` class in MicroPython is the standard way to configure GPIO. `Pin(4, Pin.OUT)` sets pin 4 as a digital output.
  - C) `RPi.GPIO` is a Python library specific to Raspberry Pi running Linux. It does not exist in MicroPython on an ESP32.
  - D) `wiringpi` is a C library with Python bindings for Raspberry Pi. It is not available in MicroPython environments.

---

### Question 14 (5 points)

An IoT device publishes sensor readings to an MQTT broker using QoS level 0. A network outage occurs for 10 seconds. Which statement accurately describes the behavior of QoS 0 during this outage?

- A) The broker queues all missed messages and delivers them when the device reconnects.
- B) Messages published during the outage are silently lost with no retransmission.
- C) The broker sends a PUBACK to confirm each missed message.
- D) The device automatically buffers messages and retransmits them after reconnection.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Message queuing for offline clients requires QoS 1 or QoS 2 combined with a persistent session (clean_session=false). QoS 0 provides no such guarantee.
  - B) QoS 0 is "fire and forget." If the network is unavailable, messages are dropped at the sending side with no queuing or retransmission. This is by design — it minimizes overhead at the cost of delivery assurance.
  - C) PUBACK is only exchanged for QoS 1 messages. QoS 0 has no acknowledgement mechanism whatsoever.
  - D) QoS 0 has no built-in client-side buffering or retransmission logic. That behavior requires application-level implementation or use of a higher QoS level.

---

### Question 15 (5 points)

Which IoT network topology arranges all end devices to communicate only through a central coordinator, with no device-to-device communication?

- A) Mesh topology
- B) Star topology
- C) Tree topology
- D) Peer-to-peer topology

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) In a mesh topology, devices can relay messages through multiple intermediate nodes. This is used by Zigbee and Z-Wave to extend range and provide redundancy.
  - B) A star topology has all end devices communicating exclusively through a central hub or coordinator. Wi-Fi infrastructure mode and LoRaWAN both use star topologies. No direct device-to-device path exists.
  - C) A tree (cluster-tree) topology is a hierarchical extension of the star where multiple star clusters are linked through coordinator nodes. It differs from a pure star in allowing multiple tiers.
  - D) Peer-to-peer (or ad-hoc) topology allows any two devices to communicate directly without a central coordinator. Bluetooth classic BR/EDR can operate in this mode.

---

### Question 16 (5 points)

A facilities engineer needs to remotely update the firmware of 10,000 deployed IoT sensors without physical access. Which security control is most critical for this operation?

- A) Compressing firmware images before transmission to reduce update time.
- B) Requiring a technician to approve each individual update via a mobile app.
- C) Digitally signing firmware images so devices reject unsigned or tampered binaries.
- D) Scheduling updates only during business hours to minimize network congestion.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Compression is a performance optimization and does not prevent an attacker from substituting a malicious firmware image during transmission.
  - B) Per-device manual approval does not scale to 10,000 devices and does not prevent delivery of a tampered image if the approval interface itself is compromised.
  - C) Digital signatures (e.g., ECDSA over the firmware binary) ensure the device can cryptographically verify that the image originated from the legitimate manufacturer and has not been modified in transit. This directly addresses OWASP IoT Top 10 item 4.
  - D) Scheduling windows affect operational impact but provide no security protection against firmware tampering.

---

### Question 17 (5 points)

Which statement best describes the difference between NB-IoT and LoRaWAN from a spectrum and infrastructure standpoint?

- A) NB-IoT operates on unlicensed 915 MHz spectrum; LoRaWAN requires a cellular carrier subscription.
- B) Both NB-IoT and LoRaWAN operate on the same unlicensed ISM band at 2.4 GHz.
- C) NB-IoT uses licensed LTE spectrum and cellular carrier infrastructure; LoRaWAN operates on unlicensed spectrum with privately deployable network servers.
- D) LoRaWAN requires dedicated fiber backhaul at each gateway; NB-IoT uses satellite uplinks.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) This reverses the two technologies. NB-IoT uses licensed LTE spectrum through a cellular carrier. LoRaWAN uses unlicensed spectrum (915 MHz in the US).
  - B) Neither NB-IoT nor LoRaWAN operates at 2.4 GHz. LoRaWAN uses 915 MHz (US) / 868 MHz (EU). NB-IoT operates within LTE frequency bands.
  - C) NB-IoT is a 3GPP cellular standard deployed by carriers in licensed LTE spectrum. LoRaWAN operates on unlicensed ISM bands and its network servers can be privately owned or use community networks such as The Things Network.
  - D) Both technologies use standard IP-based internet backhaul at their gateways/base stations. Fiber is not required, and neither uses satellite uplinks by default.

---

### Question 18 (5 points)

In the context of IoT security, what is the primary purpose of network segmentation using VLANs or separate subnets for IoT devices?

- A) To increase the bandwidth available to IoT devices by isolating them from corporate traffic.
- B) To reduce the firmware update cycle time by providing direct cloud access to devices.
- C) To contain a compromised IoT device and prevent lateral movement to critical corporate systems.
- D) To allow IoT devices to communicate directly with industrial control systems without authentication.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Bandwidth improvement is a secondary benefit at best. The primary security motivation is containment, not performance.
  - B) Network segmentation does not speed up firmware updates. OTA update speed depends on the update server and device bandwidth, not VLAN configuration.
  - C) If an IoT device is compromised, network segmentation ensures the attacker cannot pivot from the IoT VLAN to the corporate network or OT systems. This is the primary security justification for IoT network isolation.
  - D) This answer describes an insecure configuration that segmentation is specifically designed to prevent. IoT-to-ICS communication should always be authenticated and minimized.

---

### Question 19 (5 points)

A digital twin of a manufacturing robot is updated every 500 milliseconds with real sensor data. Which statement most accurately describes the value of this digital twin during a planned maintenance window when the physical robot is offline?

- A) The digital twin has no value when the physical device is offline because it cannot receive live updates.
- B) Engineers can use the digital twin to simulate proposed configuration changes and predict outcomes before applying them to the physical robot.
- C) The digital twin automatically controls the physical robot during maintenance.
- D) The digital twin replaces all physical sensor data permanently once it is created.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The last-known state snapshot in the digital twin retains value for simulation even when the physical device is offline. Claiming no value is incorrect.
  - B) Digital twins are used for simulation, predictive analytics, and change testing in a virtual environment before changes are applied to production hardware. This is one of their primary use cases.
  - C) A digital twin is a software model, not a control system. It does not automatically actuate the physical device. Control commands must be explicitly issued through an authorized path.
  - D) A digital twin mirrors reality — it does not replace sensor data. The physical sensor remains the authoritative source; the twin reflects it.

---

### Question 20 (5 points)

An IoT architect must choose between a three-tier architecture (Device – Platform – Application) and a five-tier architecture for a new industrial monitoring deployment. Which scenario most justifies choosing the five-tier model?

- A) A deployment with 10 devices, all on the same LAN, reporting to a single dashboard.
- B) A consumer smart home with 20 off-the-shelf devices connecting to a vendor cloud app.
- C) A large industrial deployment requiring separate edge processing nodes, a distinct data management tier, and formal separation of OT and IT concerns.
- D) A student prototype connecting a single Arduino to a laptop for data logging.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) A 10-device, single-LAN deployment has no need for five tiers. The added complexity of edge processing and data management tiers would be unnecessary overhead.
  - B) Consumer smart home deployments typically use a vendor's three-tier cloud platform. Five-tier architecture would over-engineer this simple use case.
  - C) Industrial deployments benefit from the five-tier model because it explicitly separates edge computing (Tier 3) from data management (Tier 4), and formally defines the boundary between OT device tiers (1–3) and IT tiers (4–5). This maps directly to the Purdue model.
  - D) A student prototype with a single device is the simplest possible case. Even a two-tier model (device + laptop) would be sufficient.

---

End of Quiz – Module 01
