# Reading Guide: Module 01 - IoT Architecture – Devices, Gateways, Cloud, and Edge

## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction

Welcome to **Module 01 – IoT Architecture: Devices, Gateways, Cloud, and Edge**! This module examines how IoT systems are structured across four functional layers: the Perception layer (sensors and actuators), the Network layer (gateways and routers), the Support/Middleware layer (data processing services), and the Application layer (end-user dashboards and APIs). Understanding this layered model is essential for designing secure and scalable IoT deployments.

As a student, you will learn how physical devices sense the environment, how gateways aggregate and forward data, how cloud platforms store and process telemetry, and why edge nodes reduce latency by processing data closer to the source. Pay close attention to the security implications at each layer — attackers target the weakest link in the chain.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **IoT Perception Layer**: The bottom layer of the IoT architecture, consisting of physical sensors, actuators, RFID tags, and embedded controllers that directly interact with the physical world. Devices in this layer collect raw data (temperature, humidity, motion) and convert physical signals into digital form. Security concerns include physical tampering and hardcoded credentials on constrained devices.
* **Network Layer**: The communication backbone that transports data from perception-layer devices to processing services. It encompasses gateways, routers, protocol translators (e.g., Zigbee-to-IP bridges), and cellular or Wi-Fi access points. Securing this layer involves encrypted transport (TLS/DTLS), device authentication, and network segmentation.
* **Support / Middleware Layer**: The processing and storage tier that receives raw telemetry from the network layer, applies filtering, aggregation, and business logic, and routes results to applications. Typical components include message brokers (MQTT brokers, AWS IoT Core), stream processors, and time-series databases. This layer is responsible for enforcing access policies and data normalization.
* **Application Layer**: The top layer where end-user dashboards, mobile apps, and enterprise APIs present processed IoT data and allow remote control of devices. Security at this layer requires strong authentication (OAuth 2.0, API keys), input validation, and role-based access control to prevent unauthorized commands being sent back down to devices.
* **Edge Device**: A compute node — such as a Raspberry Pi, NVIDIA Jetson, or AWS Greengrass gateway — that executes processing logic locally at the network edge rather than sending all raw data to the cloud. Edge processing reduces bandwidth consumption, cuts latency for time-sensitive actions, and enables offline operation when cloud connectivity is unavailable.
* **Smart Sensor**: An integrated unit combining a physical sensing element (e.g., thermistor, accelerometer) with an onboard microcontroller and wireless radio, capable of digitizing, filtering, and wirelessly transmitting sensor readings without external processing hardware. Examples include Dallas DS18B20 temperature sensors over 1-Wire and BME280 environmental sensors over I2C.
* **IoT Gateway**: A physical or virtual device that bridges local device networks (Zigbee, BLE, Z-Wave) to wide-area IP networks (Ethernet, LTE, Wi-Fi). Gateways perform protocol translation, local caching, device authentication, and certificate management. They act as the primary trust boundary between the untrusted device network and the cloud backend.

---

### 2. Certification Exam Tips

* **Layer Identification:** Exam questions frequently present a scenario device (e.g., "a Zigbee temperature sensor") and ask which architecture layer it belongs to — always map physical/sensing elements to the Perception layer and communication infrastructure to the Network layer.
* **Edge vs. Cloud Trade-offs:** Know that edge processing lowers latency and conserves bandwidth at the cost of limited compute resources, while cloud processing offers elasticity at the cost of latency and connectivity dependency. Exam scenarios often ask you to select the appropriate processing tier given latency or connectivity constraints.
* **Security at Each Layer:** Review the OWASP IoT Top 10 attack categories and map each to the architecture layer where the vulnerability originates. Hardcoded credentials and insecure firmware affect the Perception layer; unencrypted traffic affects the Network layer; weak API authentication affects the Application layer.
* **Study Resource:** The [OWASP IoT Security Project](https://owasp.org/www-project-internet-of-things/) — the open-source community's definitive reference for IoT security — provides a practical framework for assessing security across all IoT architecture layers. Review the Attack Surface Areas document before attempting the quiz.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — the open-source community's definitive reference for IoT security testing — covers the IoT Attack Surface Areas that map directly to each architecture layer discussed in this module.
* **Required Video:** The freeCodeCamp IoT full-course [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) provides a comprehensive walkthrough of IoT architecture, device types, communication protocols, and cloud integration patterns.

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Map IoT component configurations**: Draw a layered diagram placing an Arduino temperature sensor, a Raspberry Pi gateway, an MQTT broker, and a cloud dashboard into their correct architecture layers, then label the protocols connecting each layer.
* **Analyze latency differences of edge processing vs. cloud**: Use a Python script on a local machine to simulate processing 1,000 sensor readings locally versus logging round-trip times to a remote endpoint, comparing median latency values.
* **Identify network trust boundaries**: Review a sample IoT network topology diagram and annotate the trust boundaries — the points where data crosses from a less-trusted zone (device network) to a more-trusted zone (cloud backend) — and propose TLS or mutual authentication controls at each crossing.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the OWASP IoT Attack Surface Areas guide at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
* [ ] Watch the IoT architecture overview sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
* [ ] Review the lab instructions and draw the layered architecture diagram.
* [ ] Proceed to the weekly hands-on lab activity.
