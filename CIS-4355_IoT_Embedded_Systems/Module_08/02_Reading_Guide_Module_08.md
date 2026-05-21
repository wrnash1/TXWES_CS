# Reading Guide: Module 08 - Edge Computing and Fog Computing
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 08 – Edge Computing and Fog Computing**! This module examines how IoT architectures distribute computation between the device, the network edge, and the cloud — and why moving processing closer to the data source is often essential for latency-sensitive, bandwidth-constrained, or intermittently connected IoT deployments. Understanding where to place compute logic is one of the most consequential architectural decisions in IoT system design.

You will learn how edge nodes reduce round-trip latency for real-time control loops, how fog computing layers at network aggregation points extend cloud-like services to local clusters of devices, and how container-based edge runtimes (such as AWS Greengrass and Azure IoT Edge) deploy and manage workloads on constrained hardware. Security considerations — including securing edge node management interfaces, protecting data in transit between layers, and applying updates to distributed edge fleets — are central throughout.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Edge Computing**: A distributed computing paradigm that processes data at or near the source of generation — on a gateway, local server, or smart sensor — rather than sending all raw data to a centralized cloud. Edge computing reduces network latency (enabling sub-millisecond control loops), decreases upstream bandwidth consumption, and maintains local operation during cloud connectivity loss. Trade-offs include increased hardware cost at the edge, distributed software management complexity, and the need to secure physically accessible compute nodes.
*   **Fog Computing**: An extension of edge computing that introduces an intermediate processing layer between IoT devices and the cloud, typically at network aggregation points such as industrial switches, campus routers, or telecom edge nodes. Fog nodes provide compute, storage, and networking services to clusters of devices across a local area, enabling analytics and policy enforcement that are too resource-intensive for individual sensors but too latency-sensitive for the cloud.
*   **Edge Runtime / Edge Agent**: Software deployed on an edge node that manages the lifecycle of containerized or script-based workloads on behalf of the cloud. AWS Greengrass Core, Azure IoT Edge, and EdgeX Foundry are common examples. The edge agent maintains a local copy of the deployment manifest, starts and stops modules, routes inter-module messages, and reports health telemetry back to the cloud — even when cloud connectivity is intermittent.
*   **Latency vs. Bandwidth Trade-off**: The two primary drivers for choosing edge over cloud processing. Latency measures the round-trip time between a sensor event and a control response — a cloud round-trip may add 50–200 ms, unacceptable for industrial PLC replacement or autonomous vehicle perception. Bandwidth measures the data volume that must traverse the WAN link — a 4K video analytics pipeline generating 30 Mbps per camera cannot economically transmit all frames to the cloud, so inference runs locally and only metadata (object detections, anomaly flags) is forwarded.
*   **Offline Resilience**: The ability of an edge or fog node to continue operating correctly when connectivity to the central cloud is lost. Resilient designs store data locally (buffering telemetry in a local time-series database), execute local decision logic (rule-based or ML inference), and queue outbound messages for transmission when connectivity is restored. The MQTT "clean session = false" option and AWS Greengrass local messaging are examples of mechanisms that support offline resilience.

---

### 2. Certification Exam Tips
*   **Edge vs. cloud decision matrix:** Memorize: use edge when latency < 10 ms, bandwidth > 10 Mbps, or offline operation required; use cloud when global aggregation, large-scale ML training, or long-term storage is needed. Exam scenarios describe deployment requirements and test whether you select edge, fog, or cloud processing.
*   **Container orchestration at the edge:** AWS Greengrass and Azure IoT Edge both deploy Docker-compatible containers; Azure IoT Edge uses a module hub for inter-module MQTT routing; Greengrass uses subscriptions. Know the key architectural difference: Azure IoT Edge routes messages through a local broker; Greengrass routes via Lambda or stream manager.
*   **Security at the edge:** Edge nodes are physically accessible — they require TPM-based attestation, encrypted storage, and tamper-evident enclosures. An attacker with physical access to an unprotected edge node can extract credentials, inject malicious modules, or intercept all local traffic.
*   **Offline queue sizing:** When designing offline resilience, calculate the maximum queue size needed: queue_size = max_offline_duration × messages_per_second × bytes_per_message. Exam questions may ask whether a given local storage capacity is sufficient.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insecure network services and insufficient physical security — both directly applicable to edge nodes that expose management APIs and are deployed in physically accessible locations such as factory floors or street cabinets.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the insecure network services and physical security sections, which cover vulnerabilities in edge node management interfaces, exposed debug ports on gateway hardware, and unencrypted local message buses.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of edge computing architecture patterns, comparing local versus cloud processing for latency-sensitive workloads, and demonstrating containerized workload deployment on edge hardware.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Deploy a containerized edge workload**: Install Docker on a Raspberry Pi, create a simple Python MQTT subscriber container that processes incoming sensor messages locally and forwards only anomaly alerts upstream, and verify it operates correctly without internet connectivity.
*   **Measure latency difference between edge and cloud processing**: Send 100 identical sensor readings — one batch processed locally on the edge node, one forwarded to a cloud function — and compare the end-to-end response time distributions using timestamps logged in each path.
*   **Implement an offline message buffer**: Configure an MQTT client with `clean_session=False` and a local SQLite queue; disconnect the cloud connection for 60 seconds while publishing sensor data, then reconnect and verify all queued messages are delivered in order.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the insecure network services and physical security sections at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the edge computing architecture sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Calculate the offline queue size for a 1 Hz sensor transmitting 256-byte messages during a 4-hour connectivity outage before the lab.
- [ ] Proceed to the weekly hands-on lab activity.
