# Quiz: Module 08 - Edge Computing and Fog Computing
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
According to the OWASP IoT Top 10, which vulnerability is historically the most exploited entry point for building device botnets?
*   A) SQL Injection via the device web dashboard
*   B) Use of hardcoded, weak, or default credentials on network-accessible services
*   C) High CPU temperatures causing firmware crashes that expose a debug shell
*   D) Missing code comments preventing security reviewers from auditing the firmware
*   **Correct Answer:** B) Use of hardcoded, weak, or default credentials on network-accessible services
*   **Distractor Analysis:**
    *   *Why correct:* The Mirai botnet and its descendants compromised hundreds of thousands of IoT devices by scanning for telnet and SSH services using factory-default username/password pairs. Automated tools can enumerate the entire IPv4 address space in under an hour looking for these open services.
    *   SQL injection requires a relational database backend, which most embedded IoT devices do not expose. CPU temperature and missing comments are operational concerns, not security attack vectors.

---

**Question 2**
Which of the following is the most accurate definition of **edge computing** in an IoT architecture?
*   A) A cloud-native deployment model where all sensor data is streamed to a centralized data center for real-time processing by serverless functions with sub-millisecond response guarantees.
*   B) A distributed computing paradigm that processes data at or near the source of generation — on a gateway or local node — to reduce latency, bandwidth consumption, and dependence on cloud connectivity.
*   C) A network protocol that routes IoT device traffic through a regional proxy server to reduce the number of direct device-to-cloud connections required for large-scale deployments.
*   D) A hardware security module (HSM) embedded in IoT devices that performs cryptographic key storage and signature operations locally without transmitting private keys to the cloud.
*   **Correct Answer:** B) A distributed computing paradigm that processes data at or near the source of generation — on a gateway or local node — to reduce latency, bandwidth consumption, and dependence on cloud connectivity.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes centralized cloud processing, which is the opposite of edge computing. Cloud serverless functions introduce network round-trip latency incompatible with real-time control.
    *   *Why B is correct:* Edge computing moves compute to the data source. Key benefits are sub-10 ms local latency, reduced WAN bandwidth (only summaries or anomalies forwarded), and continued operation when cloud connectivity is lost.
    *   *Why C is incorrect:* This describes a proxy or API gateway pattern, not edge computing. Routing through a proxy does not move computation closer to the sensor.
    *   *Why D is incorrect:* This describes a Hardware Security Module or TPM — a cryptographic device, not a compute paradigm.

---

**Question 3**
A smart factory's robotic arm receives a stop command 180 ms after a collision sensor triggers because the command must travel from the sensor to the cloud and back. The robot causes damage in that time. Which architectural change most directly eliminates this latency problem?
*   A) Upgrade the cloud region to one geographically closer to the factory to reduce network round-trip time from 180 ms to approximately 90 ms.
*   B) Deploy an edge node on the factory floor that processes the collision sensor signal and issues the stop command locally within 2–5 ms, without requiring a cloud round-trip.
*   C) Increase the MQTT QoS level from 0 to 2 so the collision message is guaranteed to be delivered exactly once with no duplicates.
*   D) Switch the sensor communication from Wi-Fi to a wired Ethernet connection to eliminate radio transmission delays.
*   **Correct Answer:** B) Deploy an edge node on the factory floor that processes the collision sensor signal and issues the stop command locally within 2–5 ms, without requiring a cloud round-trip.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Halving the round-trip to 90 ms still produces robot damage in that window — the root cause is architectural (round-trip to cloud), not geographic. The latency requirement for industrial safety systems is typically under 10 ms.
    *   *Why B is correct:* Moving the control logic to an edge node eliminates the WAN round-trip entirely. Local processing over LAN/fieldbus achieves 1–5 ms response times, meeting industrial safety requirements.
    *   *Why C is incorrect:* MQTT QoS 2 guarantees delivery order and exactly-once semantics, but adds additional handshake overhead — it increases latency, not reduces it.
    *   *Why D is incorrect:* Wi-Fi vs. Ethernet is a last-meter latency difference of microseconds, not the source of the 180 ms problem. The cloud round-trip dominates.

---

**Question 4**
An edge node deployed in an outdoor street cabinet runs Azure IoT Edge and manages traffic sensor workloads. A security assessor finds the management REST API (port 15580) is accessible from the public internet with no authentication, and the cabinet has no physical lock. Which two controls most effectively reduce the attack surface?
*   A) Bind the IoT Edge management API to the loopback interface only, and install a tamper-evident lock on the physical cabinet.
*   B) Enable TLS on the management API and change the default port from 15580 to an obscure high-numbered port to reduce automated scanning.
*   C) Disable the IoT Edge management API entirely and deploy a VPN client on the edge node so all management traffic flows through an encrypted tunnel.
*   D) Add IP whitelist rules to allow management API access only from the cloud region's IP range, and place the cabinet in a location visible to security cameras.
*   **Correct Answer:** A) Bind the IoT Edge management API to the loopback interface only, and install a tamper-evident lock on the physical cabinet.
*   **Distractor Analysis:**
    *   *Why A is correct:* Binding to loopback (127.0.0.1) removes the network exposure entirely — the API becomes unreachable from any external host. A physical lock and tamper-evident seal address the physical attack vector, a genuine risk for equipment in street cabinets.
    *   *Why B is incorrect:* TLS encrypts the channel but does not prevent unauthenticated access if no credential is required; port obfuscation (security through obscurity) is trivially bypassed by port scanners and provides negligible protection.
    *   *Why C is incorrect:* Disabling the management API entirely would prevent legitimate remote administration; a VPN is a good additional layer but does not address the physical access vulnerability.
    *   *Why D is incorrect:* IP whitelisting a cloud region's IP range does not prevent attacks from compromised cloud infrastructure; security cameras are a deterrent, not a technical control preventing physical access.

---

**Question 5**
An edge gateway collects sensor readings at 10 Hz and forwards only anomaly alerts to the cloud. During a 2-hour connectivity outage, the edge node must buffer all 10 Hz readings locally to avoid data loss. Each reading is 64 bytes. What minimum local storage capacity is required to buffer the full 2-hour outage?
*   A) Approximately 460 KB
*   B) Approximately 4.6 MB
*   C) Approximately 46 MB
*   D) Approximately 460 MB
*   **Correct Answer:** B) Approximately 4.6 MB
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 460 KB underestimates by a factor of 10 — this would only cover about 12 minutes of data at 10 Hz with 64-byte messages.
    *   *Why B is correct:* 10 readings/sec × 64 bytes × 7,200 seconds = 4,608,000 bytes ≈ 4.6 MB. This is a realistic local flash or SD card requirement well within the capacity of any edge gateway.
    *   *Why C is incorrect:* 46 MB overestimates by a factor of 10; this would require the data rate to be 640 bytes/reading or the duration to be 20 hours.
    *   *Why D is incorrect:* 460 MB is approximately 100x the actual requirement — this would accommodate a 200-hour outage, not a 2-hour one.
